#!/usr/bin/env python3
"""Create a trimmed in-repo Xperience-10M sample from a full annotation.hdf5."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

import h5py
import numpy as np

from xperience_utils import (
    build_summary,
    list_annotation_contents,
    write_depth_previews,
    write_point_cloud_preview,
    write_pose_previews,
)


def _copy_dataset(src: h5py.Dataset, dst_group: h5py.Group, name: str, frame_count: int, imu_count: int, original_frame_count: int):
    data = src[()]
    if src.shape == ():
        dst_group.create_dataset(name, data=data)
        return

    if src.name.startswith("/imu/") and src.shape[0] == src.file["imu/device_timestamp_ns"].shape[0]:
        dst_group.create_dataset(name, data=data[:imu_count], compression="gzip")
        return

    if src.shape and src.shape[0] == original_frame_count:
        dst_group.create_dataset(name, data=data[:frame_count], compression="gzip")
        return

    dst_group.create_dataset(name, data=data, compression="gzip" if src.ndim > 0 else None)


def _copy_group(src_group: h5py.Group, dst_group: h5py.Group, frame_count: int, imu_count: int, original_frame_count: int):
    for name, item in src_group.items():
        if isinstance(item, h5py.Group):
            child = dst_group.create_group(name)
            _copy_group(item, child, frame_count, imu_count, original_frame_count)
        else:
            _copy_dataset(item, dst_group, name, frame_count, imu_count, original_frame_count)


def build_subset(annotation_path: Path, output_dir: Path, frame_count: int):
    output_dir.mkdir(parents=True, exist_ok=True)
    trimmed_annotation = output_dir / "annotation.hdf5"

    with h5py.File(annotation_path, "r") as src:
        original_frame_count = int(src["video/frame_number"].shape[0])
        frame_count = min(frame_count, original_frame_count)

        keyframe_indices = np.asarray(src["imu/keyframe_indices"][:], dtype=np.int64)
        if frame_count >= len(keyframe_indices):
            imu_count = int(src["imu/device_timestamp_ns"].shape[0])
        else:
            imu_count = int(keyframe_indices[frame_count]) + 1

        with h5py.File(trimmed_annotation, "w") as dst:
            _copy_group(src, dst, frame_count, imu_count, original_frame_count)

            if "video/device_timestamp" in dst:
                timestamps = [int(item.decode("utf-8")) for item in dst["video/device_timestamp"][:]]
                if timestamps:
                    duration_sec = (timestamps[-1] - timestamps[0]) / 1e9
                    del dst["video/length_sec"]
                    dst["video"].create_dataset("length_sec", data=np.float64(duration_sec))

    contents = list_annotation_contents(trimmed_annotation)
    with open(output_dir / "annotation_contents.json", "w", encoding="utf-8") as file:
        json.dump(contents, file, indent=2, ensure_ascii=False)

    summary = build_summary(trimmed_annotation)
    summary["derived_from"] = {
        "source_annotation": str(annotation_path),
        "source_dataset": "https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample",
        "trimmed_frame_count": frame_count,
    }
    summary["generated_files"] = {
        "annotation_contents": "annotation_contents.json",
        "depth_previews": write_depth_previews(trimmed_annotation, output_dir, min(3, frame_count)),
        "pose_previews": write_pose_previews(trimmed_annotation, output_dir),
        "point_cloud_preview": write_point_cloud_preview(trimmed_annotation, output_dir),
    }
    with open(output_dir / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    source_md = output_dir / "SOURCE.md"
    source_md.write_text(
        "\n".join(
            [
                "# Derived Sample",
                "",
                "This folder is derived from the official public sample release:",
                "",
                "- Source dataset: https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample",
                f"- Source annotation: `{annotation_path}`",
                f"- Trimmed frames kept: `{frame_count}`",
                "",
                "The raw upstream annotation is much larger, so the repo keeps a trimmed derivative for inspection and script tests.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(description="Build a trimmed Xperience-10M sample")
    parser.add_argument("annotation_hdf5", help="Path to the full annotation.hdf5 file")
    parser.add_argument(
        "--output_dir",
        "-o",
        default="xperience/data/sample_trimmed",
        help="Output directory for the trimmed sample",
    )
    parser.add_argument(
        "--frames",
        type=int,
        default=8,
        help="Number of leading frames to keep",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output directory if it exists",
    )
    args = parser.parse_args()

    annotation_path = Path(args.annotation_hdf5)
    output_dir = Path(args.output_dir)

    if not annotation_path.exists():
        raise FileNotFoundError(f"Annotation not found: {annotation_path}")

    if output_dir.exists() and args.force:
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    build_subset(annotation_path, output_dir, args.frames)
    print(f"Trimmed sample written to: {output_dir}")


if __name__ == "__main__":
    main()

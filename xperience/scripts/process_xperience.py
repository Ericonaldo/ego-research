#!/usr/bin/env python3
"""Process an Xperience-10M episode directory into lightweight JSON previews."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from xperience_utils import (
    build_summary,
    list_annotation_contents,
    write_depth_previews,
    write_point_cloud_preview,
    write_pose_previews,
)


def main():
    parser = argparse.ArgumentParser(description="Process Xperience-10M annotation.hdf5")
    parser.add_argument("episode_dir", help="Directory containing annotation.hdf5")
    parser.add_argument(
        "--output_dir",
        "-o",
        default=None,
        help="Output directory (default: <episode_dir>_processed)",
    )
    parser.add_argument(
        "--annotation_name",
        default="annotation.hdf5",
        help="Annotation filename inside episode_dir",
    )
    parser.add_argument(
        "--preview_frames",
        type=int,
        default=3,
        help="How many depth preview frames to export",
    )
    args = parser.parse_args()

    episode_dir = Path(args.episode_dir)
    annotation_path = episode_dir / args.annotation_name
    if not annotation_path.exists():
        print(f"Error: annotation file not found: {annotation_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir) if args.output_dir else Path(f"{episode_dir}_processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Processing: {annotation_path}")
    print(f"Output: {output_dir}")

    contents = list_annotation_contents(annotation_path)
    with open(output_dir / "annotation_contents.json", "w", encoding="utf-8") as file:
        json.dump(contents, file, indent=2, ensure_ascii=False)

    summary = build_summary(annotation_path)
    summary["generated_files"] = {
        "annotation_contents": "annotation_contents.json",
        "depth_previews": write_depth_previews(annotation_path, output_dir, args.preview_frames),
        "pose_previews": write_pose_previews(annotation_path, output_dir),
        "point_cloud_preview": write_point_cloud_preview(annotation_path, output_dir),
    }
    with open(output_dir / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    print("Generated:")
    print("  - annotation_contents.json")
    print("  - summary.json")
    for rel_path in summary["generated_files"]["depth_previews"]:
        print(f"  - {rel_path}")
    for rel_path in summary["generated_files"]["pose_previews"]:
        print(f"  - {rel_path}")
    if summary["generated_files"]["point_cloud_preview"]:
        print(f"  - {summary['generated_files']['point_cloud_preview']}")


if __name__ == "__main__":
    main()

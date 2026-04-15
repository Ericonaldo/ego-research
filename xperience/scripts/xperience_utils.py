#!/usr/bin/env python3
"""Utilities for inspecting and exporting Xperience-10M annotation files."""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None


def decode_scalar(value):
    """Convert HDF5 scalars to JSON-serializable values."""
    if isinstance(value, np.ndarray):
        if value.shape == ():
            return decode_scalar(value[()])
        return value.tolist()
    if isinstance(value, np.generic):
        return decode_scalar(value.item())
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace").strip("\x00")
    return value


def _truncate_text(value: str, limit: int = 400) -> str:
    if len(value) <= limit:
        return value
    return value[:limit] + "...<truncated>"


def list_annotation_contents(annotation_path: str | Path) -> dict[str, dict[str, object]]:
    """Return a flat dict describing all groups and datasets in annotation.hdf5."""
    contents: dict[str, dict[str, object]] = {}

    def visit(name, obj):
        if isinstance(obj, h5py.Group):
            contents[name] = {"type": "group"}
            return

        entry = {
            "type": "dataset",
            "shape": list(obj.shape),
            "dtype": str(obj.dtype),
        }
        if obj.shape == ():
            entry["value"] = decode_scalar(obj[()])
        contents[name] = entry

    with h5py.File(annotation_path, "r") as handle:
        handle.visititems(visit)

    return contents


def _load_caption_summary(raw_caption):
    if raw_caption is None:
        return None

    text = decode_scalar(raw_caption)
    if not isinstance(text, str):
        return {"raw": text}

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text[:500]}

    config = data.get("config", {})
    segments = data.get("segments", [])
    first_segment = segments[0] if segments else None
    return {
        "main_task": config.get("Main Task"),
        "total_frames": config.get("total_frames"),
        "total_tokens": config.get("total_tokens"),
        "segment_count": len(segments),
        "first_segment_preview": {
            "segment_id": first_segment.get("segment_id"),
            "start_frame": first_segment.get("start_frame"),
            "end_frame": first_segment.get("end_frame"),
            "sub_task": first_segment.get("Sub Task"),
            "action_count": len(first_segment.get("Current Action", [])),
            "sampled_frame_count": len(first_segment.get("sampled_frames", {})),
            "object_keyframe_count": len(first_segment.get("objects", {})),
        }
        if first_segment
        else None,
    }


def build_summary(annotation_path: str | Path) -> dict[str, object]:
    """Build a concise summary from annotation.hdf5."""
    annotation_path = Path(annotation_path)

    with h5py.File(annotation_path, "r") as handle:
        metadata = {}
        if "metadata" in handle:
            for key, dataset in handle["metadata"].items():
                value = decode_scalar(dataset[()])
                if isinstance(value, str):
                    value = _truncate_text(value)
                metadata[key] = value

        cameras = {}
        if "calibration" in handle:
            for cam_name, group in handle["calibration"].items():
                cameras[cam_name] = {
                    key: {
                        "shape": list(group[key].shape),
                        "dtype": str(group[key].dtype),
                        **({"value": decode_scalar(group[key][()])} if group[key].shape == () else {}),
                    }
                    for key in group.keys()
                }

        timestamps = []
        if "video/device_timestamp" in handle:
            timestamps = [decode_scalar(item) for item in handle["video/device_timestamp"][:]]

        return {
            "annotation_file": annotation_path.name,
            "top_level_groups": sorted(list(handle.keys())),
            "frame_count": int(handle["video/frame_number"].shape[0]) if "video/frame_number" in handle else None,
            "duration_sec": float(handle["video/length_sec"][()]) if "video/length_sec" in handle else None,
            "video_timestamp_first": timestamps[0] if timestamps else None,
            "video_timestamp_last": timestamps[-1] if timestamps else None,
            "depth": {
                "shape": list(handle["depth/depth"].shape) if "depth/depth" in handle else None,
                "min": float(handle["depth/depth_min"][()]) if "depth/depth_min" in handle else None,
                "max": float(handle["depth/depth_max"][()]) if "depth/depth_max" in handle else None,
                "scale": float(handle["depth/scale"][()]) if "depth/scale" in handle else None,
            },
            "slam": {
                "pose_shape": list(handle["slam/quat_wxyz"].shape) if "slam/quat_wxyz" in handle else None,
                "point_cloud_shape": list(handle["slam/point_cloud"].shape) if "slam/point_cloud" in handle else None,
            },
            "hand_mocap": {
                "left_shape": list(handle["hand_mocap/left_joints_3d"].shape) if "hand_mocap/left_joints_3d" in handle else None,
                "right_shape": list(handle["hand_mocap/right_joints_3d"].shape) if "hand_mocap/right_joints_3d" in handle else None,
            },
            "full_body_mocap": {
                "keypoints_shape": list(handle["full_body_mocap/keypoints"].shape) if "full_body_mocap/keypoints" in handle else None,
                "contacts_shape": list(handle["full_body_mocap/contacts"].shape) if "full_body_mocap/contacts" in handle else None,
            },
            "imu": {
                "shape": list(handle["imu/accel_xyz"].shape) if "imu/accel_xyz" in handle else None,
                "keyframe_count": int(handle["imu/keyframe_indices"].shape[0]) if "imu/keyframe_indices" in handle else None,
            },
            "metadata": metadata,
            "calibration_cameras": cameras,
            "caption": _load_caption_summary(handle["caption"][()] if "caption" in handle else None),
        }


def _save_image(array: np.ndarray, destination: Path) -> bool:
    if Image is None:
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(array).save(destination)
    return True


def write_depth_previews(annotation_path: str | Path, output_dir: str | Path, frame_limit: int = 3) -> list[str]:
    """Write depth preview PNGs and return relative paths."""
    annotation_path = Path(annotation_path)
    output_dir = Path(output_dir)
    saved: list[str] = []

    if Image is None:
        return saved

    with h5py.File(annotation_path, "r") as handle:
        if "depth/depth" not in handle:
            return saved

        depth = handle["depth/depth"]
        confidence = handle["depth/confidence"] if "depth/confidence" in handle else None
        depth_min = float(handle["depth/depth_min"][()]) if "depth/depth_min" in handle else float(np.nanmin(depth[: min(4, depth.shape[0])]))
        depth_max = float(handle["depth/depth_max"][()]) if "depth/depth_max" in handle else float(np.nanmax(depth[: min(4, depth.shape[0])]))
        denom = max(depth_max - depth_min, 1e-6)

        preview_dir = output_dir / "preview"
        preview_dir.mkdir(parents=True, exist_ok=True)
        for idx in range(min(frame_limit, depth.shape[0])):
            frame = np.asarray(depth[idx], dtype=np.float32)
            normalized = np.clip((frame - depth_min) / denom, 0.0, 1.0)
            image = (normalized * 255.0).astype(np.uint8)

            if confidence is not None:
                conf = np.asarray(confidence[idx], dtype=np.uint8)
                image = np.stack([image, image, image], axis=-1)
                image[..., 1] = np.maximum(image[..., 1], conf)

            filename = f"preview/depth_{idx:03d}.png"
            _save_image(image, output_dir / filename)
            saved.append(filename)

    return saved


def write_pose_previews(annotation_path: str | Path, output_dir: str | Path) -> list[str]:
    """Export first-frame hand/body pose previews as JSON."""
    annotation_path = Path(annotation_path)
    output_dir = Path(output_dir)
    preview_dir = output_dir / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)
    saved: list[str] = []

    with h5py.File(annotation_path, "r") as handle:
        pose_specs = {
            "hand_left_frame0.json": "hand_mocap/left_joints_3d",
            "hand_right_frame0.json": "hand_mocap/right_joints_3d",
            "body_frame0.json": "full_body_mocap/keypoints",
        }
        for filename, path in pose_specs.items():
            if path not in handle:
                continue
            data = np.asarray(handle[path][0], dtype=np.float32).tolist()
            out_path = preview_dir / filename
            with open(out_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
            saved.append(f"preview/{filename}")

    return saved


def write_point_cloud_preview(annotation_path: str | Path, output_dir: str | Path, max_points: int = 512) -> str | None:
    """Save a small point cloud preview as .npy."""
    annotation_path = Path(annotation_path)
    output_dir = Path(output_dir)
    out_path = output_dir / "preview" / "point_cloud_preview.npy"

    with h5py.File(annotation_path, "r") as handle:
        if "slam/point_cloud" not in handle:
            return None
        points = np.asarray(handle["slam/point_cloud"][:max_points], dtype=np.float32)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    np.save(out_path, points)
    return str(out_path.relative_to(output_dir))

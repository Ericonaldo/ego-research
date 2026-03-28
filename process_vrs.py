#!/usr/bin/env python3
"""
Process Project Aria VRS files - extract images, IMU data, and metadata.

Usage:
    python process_vrs.py <vrs_file> [--output_dir OUTPUT_DIR]

Example:
    python process_vrs.py data/recording.vrs --output_dir extracted/
"""

import argparse
import csv
import json
import os
import sys

import numpy as np

try:
    from projectaria_tools.core import data_provider, calibration
    from projectaria_tools.core.stream_id import StreamId
except ImportError:
    print("Error: projectaria-tools not installed.")
    print("Run: pip install 'projectaria-tools[all]'")
    sys.exit(1)


def get_stream_label(stream_id):
    """Get a human-readable label for a stream."""
    return f"{stream_id.get_type_name()}_{stream_id.get_type_id()}"


def extract_images(provider, stream_id, output_dir, max_frames=None):
    """Extract image frames from a camera stream."""
    try:
        from PIL import Image
    except ImportError:
        print("  Pillow not installed, skipping image extraction")
        return

    label = get_stream_label(stream_id)
    stream_dir = os.path.join(output_dir, "images", label)
    os.makedirs(stream_dir, exist_ok=True)

    num_data = provider.get_num_data(stream_id)
    if max_frames:
        num_data = min(num_data, max_frames)

    print(f"  Extracting {num_data} frames from {label}...")

    timestamps = []
    for i in range(num_data):
        image_data = provider.get_image_data_by_index(stream_id, i)
        image_array = image_data[0].to_numpy_array()
        timestamp_ns = image_data[1].capture_timestamp_ns

        # Save image
        img = Image.fromarray(image_array)
        filename = f"frame_{i:06d}_{timestamp_ns}.png"
        img.save(os.path.join(stream_dir, filename))

        timestamps.append({
            "frame_index": i,
            "timestamp_ns": timestamp_ns,
            "filename": filename,
            "width": image_array.shape[1],
            "height": image_array.shape[0],
        })

    # Save timestamp index
    with open(os.path.join(stream_dir, "timestamps.json"), "w") as f:
        json.dump(timestamps, f, indent=2)

    print(f"  Saved {num_data} frames to {stream_dir}")


def extract_imu(provider, stream_id, output_dir):
    """Extract IMU data from an IMU stream."""
    label = get_stream_label(stream_id)
    stream_dir = os.path.join(output_dir, "imu", label)
    os.makedirs(stream_dir, exist_ok=True)

    num_data = provider.get_num_data(stream_id)
    print(f"  Extracting {num_data} IMU samples from {label}...")

    csv_path = os.path.join(stream_dir, "imu_data.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "index", "timestamp_ns",
            "accel_x", "accel_y", "accel_z",
            "gyro_x", "gyro_y", "gyro_z",
        ])

        for i in range(num_data):
            imu_data = provider.get_imu_data_by_index(stream_id, i)
            accel = imu_data.accel_msec2
            gyro = imu_data.gyro_radsec
            writer.writerow([
                i, imu_data.capture_timestamp_ns,
                accel[0], accel[1], accel[2],
                gyro[0], gyro[1], gyro[2],
            ])

    print(f"  Saved IMU data to {csv_path}")


def extract_calibration(provider, output_dir):
    """Extract device calibration data."""
    calib_dir = os.path.join(output_dir, "calibration")
    os.makedirs(calib_dir, exist_ok=True)

    device_calib = provider.get_device_calibration()
    if device_calib is None:
        print("  No calibration data found")
        return

    calib_info = {
        "device_subtype": device_calib.get_device_subtype(),
    }

    # Extract per-sensor calibration
    sensor_calibs = []
    for label in device_calib.get_all_labels():
        sensor_calib = device_calib.get_sensor_calib(label)
        if sensor_calib is not None:
            info = {
                "label": label,
                "calibration_type": str(sensor_calib.sensor_calibration_type()),
            }
            # Try to get camera calibration details
            try:
                cam_calib = sensor_calib.camera_calibration()
                if cam_calib is not None:
                    img_size = cam_calib.get_image_size()
                    info["image_width"] = int(img_size[0])
                    info["image_height"] = int(img_size[1])
                    info["focal_lengths"] = cam_calib.get_focal_lengths().tolist()
                    info["principal_point"] = cam_calib.get_principal_point().tolist()
                    info["model_name"] = str(cam_calib.get_model_name())
            except Exception:
                pass
            sensor_calibs.append(info)

    calib_info["sensors"] = sensor_calibs

    calib_path = os.path.join(calib_dir, "calibration.json")
    with open(calib_path, "w") as f:
        json.dump(calib_info, f, indent=2)

    print(f"  Saved calibration to {calib_path}")


def extract_metadata(provider, output_dir):
    """Extract recording metadata and stream info."""
    meta = {
        "streams": [],
    }

    stream_ids = provider.get_all_streams()
    for sid in stream_ids:
        stream_info = {
            "stream_id": str(sid),
            "type_name": str(sid.get_type_name()),
            "type_id": str(sid.get_type_id()),
            "label": get_stream_label(sid),
            "num_data": provider.get_num_data(sid),
        }
        meta["streams"].append(stream_info)

    meta_path = os.path.join(output_dir, "metadata.json")
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"  Saved metadata to {meta_path}")
    return meta


def main():
    parser = argparse.ArgumentParser(
        description="Extract data from Project Aria VRS files"
    )
    parser.add_argument("vrs_file", help="Path to the VRS file")
    parser.add_argument(
        "--output_dir", "-o", default=None,
        help="Output directory (default: <vrs_basename>_extracted/)"
    )
    parser.add_argument(
        "--max_frames", "-n", type=int, default=None,
        help="Max frames to extract per camera stream (default: all)"
    )
    parser.add_argument(
        "--skip_images", action="store_true",
        help="Skip image extraction"
    )
    parser.add_argument(
        "--skip_imu", action="store_true",
        help="Skip IMU data extraction"
    )
    args = parser.parse_args()

    if not os.path.exists(args.vrs_file):
        print(f"Error: VRS file not found: {args.vrs_file}")
        sys.exit(1)

    if args.output_dir is None:
        basename = os.path.splitext(os.path.basename(args.vrs_file))[0]
        args.output_dir = f"{basename}_extracted"

    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Opening VRS file: {args.vrs_file}")
    provider = data_provider.create_vrs_data_provider(args.vrs_file)

    if provider is None:
        print("Error: Could not open VRS file")
        sys.exit(1)

    # Extract metadata
    print("\n[1/4] Extracting metadata...")
    meta = extract_metadata(provider, args.output_dir)

    # Extract calibration
    print("\n[2/4] Extracting calibration...")
    extract_calibration(provider, args.output_dir)

    # Categorize streams
    camera_streams = []
    imu_streams = []

    for sid in provider.get_all_streams():
        num = provider.get_num_data(sid)
        if num == 0:
            continue
        # Check if it's a camera or IMU stream by trying to read data
        try:
            provider.get_image_data_by_index(sid, 0)
            camera_streams.append(sid)
        except Exception:
            try:
                provider.get_imu_data_by_index(sid, 0)
                imu_streams.append(sid)
            except Exception:
                pass

    # Extract images
    if not args.skip_images and camera_streams:
        print(f"\n[3/4] Extracting images from {len(camera_streams)} camera streams...")
        for sid in camera_streams:
            extract_images(provider, sid, args.output_dir, args.max_frames)
    else:
        print("\n[3/4] Skipping image extraction")

    # Extract IMU
    if not args.skip_imu and imu_streams:
        print(f"\n[4/4] Extracting IMU from {len(imu_streams)} streams...")
        for sid in imu_streams:
            extract_imu(provider, sid, args.output_dir)
    else:
        print("\n[4/4] Skipping IMU extraction")

    print(f"\nDone! Output saved to: {args.output_dir}")
    print(f"\nStream summary:")
    for s in meta["streams"]:
        print(f"  {s['label']}: {s['num_data']} samples")


if __name__ == "__main__":
    main()

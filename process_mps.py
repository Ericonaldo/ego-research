#!/usr/bin/env python3
"""
Process Project Aria MPS (Machine Perception Services) outputs.
Handles trajectory, point cloud, eye gaze, and hand tracking data.

Usage:
    python process_mps.py <mps_dir> [--output_dir OUTPUT_DIR]

Examples:
    # Standard MPS directory layout (with slam/ and eye_gaze/ subdirs)
    python process_mps.py data/seq01/mps/ --output_dir processed/

    # Flat layout (trajectory and eye_gaze at top level)
    python process_mps.py data/sample/mps_sample/ --output_dir processed/
"""

import argparse
import json
import os
import sys

import numpy as np

try:
    from projectaria_tools.core.mps import (
        read_closed_loop_trajectory,
        read_open_loop_trajectory,
        read_eyegaze,
        read_global_point_cloud,
    )
except ImportError:
    print("Error: projectaria-tools not installed.")
    print("Run: pip install 'projectaria-tools[all]'")
    sys.exit(1)


def find_file(mps_dir, *candidates):
    """Find the first existing file from a list of candidate paths."""
    for parts in candidates:
        if isinstance(parts, str):
            parts = [parts]
        path = os.path.join(mps_dir, *parts)
        if os.path.exists(path):
            return path
    return None


def process_trajectory(mps_dir, output_dir):
    """Process closed-loop and open-loop trajectories."""
    traj_dir = os.path.join(output_dir, "trajectory")
    os.makedirs(traj_dir, exist_ok=True)

    # Closed-loop trajectory - check multiple possible locations
    closed_loop_path = find_file(
        mps_dir,
        ["slam", "closed_loop_trajectory.csv"],
        ["trajectory", "closed_loop_trajectory.csv"],
        "closed_loop_trajectory.csv",
    )

    if closed_loop_path:
        print(f"  Processing closed-loop trajectory from {closed_loop_path}...")
        trajectory = read_closed_loop_trajectory(closed_loop_path)

        poses = []
        for pose in trajectory:
            t = pose.tracking_timestamp.total_seconds()
            translation = pose.transform_world_device.translation().flatten()
            rotation = pose.transform_world_device.rotation().to_quat().flatten()
            poses.append({
                "timestamp_s": float(t),
                "position": {
                    "x": float(translation[0]),
                    "y": float(translation[1]),
                    "z": float(translation[2]),
                },
                "quaternion": {
                    "x": float(rotation[0]),
                    "y": float(rotation[1]),
                    "z": float(rotation[2]),
                    "w": float(rotation[3]),
                },
            })

        output_path = os.path.join(traj_dir, "closed_loop_trajectory.json")
        with open(output_path, "w") as f:
            json.dump(poses, f, indent=2)
        print(f"  Saved {len(poses)} poses to {output_path}")

        # Also save as numpy for efficient processing
        # Columns: [timestamp_s, x, y, z, qx, qy, qz, qw]
        if poses:
            arr = np.array([
                [p["timestamp_s"],
                 p["position"]["x"], p["position"]["y"], p["position"]["z"],
                 p["quaternion"]["x"], p["quaternion"]["y"], p["quaternion"]["z"], p["quaternion"]["w"]]
                for p in poses
            ])
            np.save(os.path.join(traj_dir, "closed_loop_trajectory.npy"), arr)
            print(f"  Also saved as numpy array: shape={arr.shape}")
    else:
        print("  No closed-loop trajectory found")

    # Open-loop trajectory
    open_loop_path = find_file(
        mps_dir,
        ["slam", "open_loop_trajectory.csv"],
        ["trajectory", "open_loop_trajectory.csv"],
        "open_loop_trajectory.csv",
    )

    if open_loop_path:
        print(f"  Processing open-loop trajectory from {open_loop_path}...")
        trajectory = read_open_loop_trajectory(open_loop_path)

        poses = []
        for pose in trajectory:
            t = pose.tracking_timestamp.total_seconds()
            translation = pose.transform_odometry_device.translation().flatten()
            poses.append({
                "timestamp_s": float(t),
                "position": {
                    "x": float(translation[0]),
                    "y": float(translation[1]),
                    "z": float(translation[2]),
                },
            })

        output_path = os.path.join(traj_dir, "open_loop_trajectory.json")
        with open(output_path, "w") as f:
            json.dump(poses, f, indent=2)
        print(f"  Saved {len(poses)} poses to {output_path}")


def process_point_cloud(mps_dir, output_dir):
    """Process semi-dense point cloud."""
    pc_dir = os.path.join(output_dir, "point_cloud")
    os.makedirs(pc_dir, exist_ok=True)

    pc_path = find_file(
        mps_dir,
        ["slam", "semidense_points.csv.gz"],
        ["slam", "semidense_points.csv"],
        ["slam", "global_points.csv.gz"],
        ["trajectory", "global_points.csv.gz"],
        ["trajectory", "semidense_points.csv.gz"],
        "global_points.csv.gz",
    )

    if not pc_path:
        print("  No point cloud data found")
        return

    print(f"  Processing point cloud from {pc_path}...")
    points = read_global_point_cloud(pc_path)

    if points is not None and len(points) > 0:
        # Extract positions and save as numpy
        positions = np.array([
            [p.position_world[0], p.position_world[1], p.position_world[2]]
            for p in points
        ])
        np.save(os.path.join(pc_dir, "points.npy"), positions)
        print(f"  Saved {len(positions)} points, shape={positions.shape}")

        # Save as PLY for visualization
        ply_path = os.path.join(pc_dir, "points.ply")
        with open(ply_path, "w") as f:
            f.write("ply\n")
            f.write("format ascii 1.0\n")
            f.write(f"element vertex {len(positions)}\n")
            f.write("property float x\n")
            f.write("property float y\n")
            f.write("property float z\n")
            f.write("end_header\n")
            for p in positions:
                f.write(f"{p[0]} {p[1]} {p[2]}\n")
        print(f"  Saved PLY point cloud to {ply_path}")


def process_eye_gaze(mps_dir, output_dir):
    """Process eye gaze data."""
    gaze_dir = os.path.join(output_dir, "eye_gaze")
    os.makedirs(gaze_dir, exist_ok=True)

    gaze_path = find_file(
        mps_dir,
        ["eye_gaze", "personalized_eye_gaze.csv"],
        ["eye_gaze", "general_eye_gaze.csv"],
        ["eye_gaze", "generalized_eye_gaze.csv"],
        ["eye_gaze", "eyegaze.csv"],
        "eyegaze.csv",
    )

    if not gaze_path:
        print("  No eye gaze data found")
        return

    print(f"  Processing eye gaze from {gaze_path}...")
    gazes = read_eyegaze(gaze_path)

    gaze_data = []
    for g in gazes:
        gaze_data.append({
            "timestamp_s": float(g.tracking_timestamp.total_seconds()),
            "yaw": float(g.yaw),
            "pitch": float(g.pitch),
            "depth": float(g.depth) if g.depth is not None else None,
        })

    output_path = os.path.join(gaze_dir, "eye_gaze.json")
    with open(output_path, "w") as f:
        json.dump(gaze_data, f, indent=2)
    print(f"  Saved {len(gaze_data)} gaze samples to {output_path}")

    # Save as numpy
    if gaze_data:
        arr = np.array([
            [g["timestamp_s"], g["yaw"], g["pitch"]]
            for g in gaze_data
        ])
        np.save(os.path.join(gaze_dir, "eye_gaze.npy"), arr)


def main():
    parser = argparse.ArgumentParser(
        description="Process Project Aria MPS outputs"
    )
    parser.add_argument("mps_dir", help="Path to the MPS output directory")
    parser.add_argument(
        "--output_dir", "-o", default=None,
        help="Output directory (default: <mps_dir>_processed/)"
    )
    args = parser.parse_args()

    if not os.path.exists(args.mps_dir):
        print(f"Error: MPS directory not found: {args.mps_dir}")
        sys.exit(1)

    if args.output_dir is None:
        args.output_dir = f"{args.mps_dir.rstrip('/')}_processed"

    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Processing MPS data from: {args.mps_dir}")
    print(f"Output directory: {args.output_dir}")

    print("\n[1/3] Processing trajectories...")
    process_trajectory(args.mps_dir, args.output_dir)

    print("\n[2/3] Processing point cloud...")
    process_point_cloud(args.mps_dir, args.output_dir)

    print("\n[3/3] Processing eye gaze...")
    process_eye_gaze(args.mps_dir, args.output_dir)

    print(f"\nDone! All processed data saved to: {args.output_dir}")


if __name__ == "__main__":
    main()

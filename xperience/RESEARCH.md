# Xperience-10M 调研摘要

## 1. 基本定位

`Xperience-10M` 是 Ropedia 于 **2026-03-16** 发布的大规模 egocentric multimodal dataset。它的核心价值不是“又一个视频 benchmark”，而是把视觉、几何、手部、全身动作、IMU 和语言信息统一到单个 experience episode 里。

## 2. 当前可确认的公开信息

截至 **2026-04-15**，官方公开页面可确认的指标包括：

- 10M experiences / interactions
- 10,000 小时 video with audio
- 2.88B RGB frames
- 720M depth frames
- 576M camera poses
- 576M mocap frames
- 7.2B IMU frames
- 16M caption sentences
- 350K objects
- 总存储约 `1 PB`

公开 sample `annotation.hdf5` 中可以看到的主结构包括：

- `calibration`
- `caption`
- `depth`
- `full_body_mocap`
- `hand_mocap`
- `imu`
- `metadata`
- `slam`
- `video`

## 3. 和本仓库的关系

这个仓库里补充的 `xperience/scripts/` 不追求完整复刻 `HOMIE-toolkit`，而是提供两个最直接的能力：

1. 把 `annotation.hdf5` 快速整理成 `summary.json + contents.json + preview`
2. 把官方大 sample 裁成一个适合版本库保存的轻量示例

## 4. 当前研究判断

- 如果目标是 `world model / robotics / embodied multimodal pretraining`，它值得重点关注。
- 如果目标是立刻做公开 benchmark 对标，`Aria` / `Ego4D` / `HOT3D` 生态更成熟。
- 如果目标是快速熟悉数据结构，本仓库里的 `sample_trimmed` 会比直接拉完整 sample 更省时间。

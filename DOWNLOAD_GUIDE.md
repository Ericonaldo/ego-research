# Project Aria 数据集下载指南

## 前提条件

- Python 3.9-3.12（3.13 不支持）
- 本机已配置好环境：`conda activate aria`（Python 3.11 + projectaria-tools 2.1.1）

> **重要**：当前服务器无法直接访问 Meta CDN（`fbcdn.net` 被墙），需通过代理或在海外机器上下载后传回。

---

## 方法一：通过官方 CLI 下载（标准流程）

### Step 1: 获取 CDN 文件

1. 打开浏览器，访问目标数据集页面：

| 数据集 | 注册页面 |
|--------|----------|
| Aria Digital Twin (ADT) | https://www.projectaria.com/datasets/adt/ |
| Aria Everyday Activities (AEA) | https://www.projectaria.com/datasets/aea/ |
| Aria Synthetic Environments (ASE) | https://www.projectaria.com/datasets/ase/ |
| HOT3D | https://www.projectaria.com/datasets/hot3D/ |
| Nymeria | https://www.projectaria.com/datasets/nymeria/ |
| Digital Twin Catalog (DTC) | https://www.projectaria.com/datasets/dtc/ |
| Aria Everyday Objects (AEO) | https://www.projectaria.com/datasets/aeo/ |
| Reading in the Wild | https://www.projectaria.com/datasets/reading-in-the-wild/ |

2. 输入 **email 地址**
3. 勾选同意 **Dataset License Agreement**（非商业研究用途）
4. 点击 **"Access the Datasets"**
5. 下载得到 JSON 文件，例如 `adt_download_urls.json`

> CDN 链接有效期 14-30 天，过期后需重新获取。

### Step 2: 查看可下载内容

```bash
conda activate aria
aria_dataset_downloader -c <cdn_file.json> -o <output_dir>/
```

不指定 `-d` 参数时会列出所有可用的数据类型：

| ID | 数据类型 | 说明 |
|----|----------|------|
| 0 | VRS | 原始传感器数据（相机、IMU、音频等） |
| 1 | MPS SLAM | 闭环/开环轨迹 |
| 2 | MPS Point Cloud | 半稠密 3D 点云 |
| 3 | MPS Eye Gaze | 眼动追踪向量 |
| 4 | MPS Online Calibration | 实时标定数据 |
| 5 | MPS Hand Tracking | 手部追踪 |
| 6 | Ground Truth | 标注数据（ADT 专有） |
| 7 | Depth Images | 深度图（ADT 专有） |
| 8 | Segmentation | 分割图（ADT 专有） |
| 9 | Other | 合成渲染等 |

### Step 3: 执行下载

```bash
# 只下载 VRS 文件（最小，推荐先试）
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d 0

# 下载 VRS + 轨迹 + 眼动
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d 0 1 3

# 只下载特定 sequence
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ \
  -l Apartment_release_golden_skeleton_seq100_10s_sample_M1292 \
  -d 0 1 2 3 4 5 6 7 8 9

# 下载全部
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d all -l all
```

**常用参数**：
- `-c` / `--cdn_file`：CDN JSON 文件路径
- `-o` / `--output_folder`：输出目录
- `-d` / `--data_types`：数据类型 ID 列表（空格分隔），`all` 下载全部
- `-l` / `--sequence_names`：sequence 名称列表，`all` 下载全部
- `-w` / `--overwrite`：强制覆盖已下载文件

**断点续传**：重复运行同一命令，已下载的文件会自动跳过。

### Step 4: 传到目标服务器（如果在其他机器下载）

```bash
rsync -avz --progress ./data/adt/ target_server:/data/projects/aria/data/adt/
```

---

## 方法二：通过代理下载

如果本机有可用代理：

```bash
export https_proxy=http://your_proxy:port
export http_proxy=http://your_proxy:port
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d 0
```

测试 Meta CDN 连通性：
```bash
curl --connect-timeout 10 https://scontent.fftw1-1.fna.fbcdn.net
```

---

## 方法三：从 GitHub 下载测试数据（已完成）

GitHub 仓库包含小型测试数据，不需要注册。已下载到 `/data/projects/aria/data/sample/`：

```bash
BASE="https://raw.githubusercontent.com/facebookresearch/projectaria_tools/main/data/gen1"

# MPS 样本（~75MB VRS + 轨迹/眼动/手部 CSV）
curl -L -o sample.vrs "$BASE/mps_sample/sample.vrs"
curl -L -o closed_loop_trajectory.csv "$BASE/mps_sample/trajectory/closed_loop_trajectory.csv"

# ADT 测试数据（~5MB）
curl -L -o video.vrs "$BASE/aria_digital_twin_test_data/video.vrs"
curl -L -o depth_images.vrs "$BASE/aria_digital_twin_test_data/depth_images.vrs"
curl -L -o segmentations.vrs "$BASE/aria_digital_twin_test_data/segmentations.vrs"

# AEA 测试数据（~3.5MB）
curl -L -o recording.vrs "$BASE/aria_everyday_activities_test_data/recording.vrs"
```

---

## 方法四：Dataset Explorer 图形界面

1. 访问 https://explorer.projectaria.com/
2. 可浏览、筛选、预览各数据集的 sequences
3. 选择需要的 sequences 后生成下载文件
4. 支持按场景、活动类型、时长等条件过滤

---

## 方法五：使用下载脚本

项目中已提供 `download_dataset.sh` 封装脚本：

```bash
# 用法
bash download_dataset.sh <cdn_file.json> [output_dir] [data_types]

# 示例
bash download_dataset.sh adt_download_urls.json ./data/adt "0 1 3"
bash download_dataset.sh aea_download_urls.json ./data/aea "0"
bash download_dataset.sh adt_download_urls.json ./data/adt "0 1 2 3 4 5 6 7 8 9"
```

---

## 下载后处理

```bash
conda activate aria

# 从 VRS 提取图像、IMU、标定数据
python process_vrs.py <file.vrs> -o <output_dir> [--max_frames N] [--skip_imu]

# 处理 MPS 输出（轨迹、点云、眼动）
python process_mps.py <mps_dir> -o <output_dir>
```

---

## 各数据集推荐下载策略

| 数据集 | 大小 | 推荐 |
|--------|------|------|
| **AEA** | ~353 GB | 先下 `-d 0` (VRS only)，约 100GB |
| **ADT** | ~3.5 TB | 先下单个 sequence 全部数据类型试跑 |
| **ASE** | ~23 TB | 使用专用下载器，按需下载子集 |
| **Ego-Exo4D** | Very Large | 通过 Ego-Exo4D 官网单独申请 |
| **HOT3D** | Medium | 通过 HOT3D GitHub 仓库专用下载器 |
| **Nymeria** | Large | 通过官网 CDN 文件下载 |
| **DTC** | Medium | 3D 模型 + 少量视频 |
| **AEO** | Small | 25 sequences，可全量下载 |
| **Reading in the Wild** | Medium | 通过 Dataset Explorer 筛选下载 |

---

## 注意事项

1. **License**：所有数据集仅限 **非商业研究用途**
2. **Python 版本**：projectaria-tools 不支持 Python 3.13，需使用 3.9-3.12
3. **ASE 数据集**使用独立的 Python 下载脚本，不使用 `aria_dataset_downloader`
4. **Ego-Exo4D** 有独立的申请和下载流程，见 https://ego-exo4d-data.org/
5. **HOT3D** 使用 GitHub 仓库中的专用下载器，见 https://github.com/facebookresearch/hot3d

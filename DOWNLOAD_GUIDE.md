# Egocentric 数据集访问与下载指南

这份文档把仓库里涉及的主流 **egocentric / first-person** 数据访问流程统一整理。当前覆盖：

- Project Aria 家族数据集
- Ego4D / Ego-Exo4D
- Xperience-10M

需要先说明一点：

- 仓库中的 `Aria` 处理脚本现在位于 `aria/scripts/`
- `Xperience-10M` 现在已补充轻量 annotation 处理脚本，位于 `xperience/scripts/`

---

## 1. 快速对比

| 数据生态 | 访问入口 | 主要下载方式 | 当前仓库支持度 |
|----------|----------|--------------|----------------|
| Project Aria 家族 | projectaria.com | CDN JSON + `aria_dataset_downloader` | 高 |
| Ego4D / Ego-Exo4D | ego4d-data.org | License + CLI / AWS 凭证 | 中 |
| Xperience-10M | Hugging Face + Ropedia | gated access + 人工审核 + 协议签署 | 低到中 |

---

## 2. Project Aria 家族

### 2.1 前提条件

- Python 3.9-3.12
- 当前本机环境可用：`conda activate aria`
- `projectaria-tools` 已安装

> 注意：如果所在网络无法直接访问 Meta CDN，需要代理或在海外机器下载后回传。

### 2.2 标准访问流程

1. 打开目标数据集页面：

| 数据集 | 页面 |
|--------|------|
| ADT | https://www.projectaria.com/datasets/adt/ |
| AEA | https://www.projectaria.com/datasets/aea/ |
| ASE | https://www.projectaria.com/datasets/ase/ |
| HOT3D | https://www.projectaria.com/datasets/hot3D/ |
| Nymeria | https://www.projectaria.com/datasets/nymeria/ |
| DTC | https://www.projectaria.com/datasets/dtc/ |
| AEO | https://www.projectaria.com/datasets/aeo/ |
| Reading in the Wild | https://www.projectaria.com/datasets/reading-in-the-wild/ |

2. 输入邮箱并同意 license
3. 下载获得 CDN JSON，例如 `adt_download_urls.json`
4. 通过官方 CLI 下载：

```bash
conda activate aria
aria_dataset_downloader -c <cdn_file.json> -o <output_dir>/
```

### 2.3 常用下载示例

```bash
# 只下载 VRS
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d 0

# 下载 VRS + 轨迹 + 眼动
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ -d 0 1 3

# 下载单个 sequence
aria_dataset_downloader -c adt_download_urls.json -o ./data/adt/ \
  -l Apartment_release_golden_skeleton_seq100_10s_sample_M1292 \
  -d 0 1 2 3 4 5 6 7 8 9
```

### 2.4 常用参数

- `-c` / `--cdn_file`: CDN JSON
- `-o` / `--output_folder`: 输出目录
- `-d` / `--data_types`: 数据类型 ID
- `-l` / `--sequence_names`: sequence 名称
- `-w` / `--overwrite`: 覆盖已下载文件

### 2.5 下载后处理

```bash
conda activate aria

# 提取 VRS 中的图像、IMU、标定
python aria/scripts/process_vrs.py <file.vrs> -o <output_dir>

# 处理 MPS 结果
python aria/scripts/process_mps.py <mps_dir> -o <output_dir>
```

### 2.6 仓库内现成脚本

```bash
bash aria/scripts/download_dataset.sh <cdn_file.json> [output_dir] [data_types]
```

示例：

```bash
bash aria/scripts/download_dataset.sh adt_download_urls.json ./aria/data/adt "0 1 3"
bash aria/scripts/download_dataset.sh aea_download_urls.json ./aria/data/aea "0"
```

---

## 3. Ego4D / Ego-Exo4D

### 3.1 访问入口

- Ego4D 官网: https://ego4d-data.org/
- 文档: https://ego4d-data.org/docs/
- Start Here: https://ego4d-data.org/docs/start-here/
- Ego-Exo4D 文档: https://docs.ego-exo4d-data.org/

### 3.2 访问流程

官方流程通常是：

1. 在 `ego4ddataset.com` 或官方入口签署数据使用协议
2. 等待审核和凭证发放
3. 使用官方 CLI 下载

官方文档提到审批一般需要约 **48 小时**。

### 3.3 CLI 示例

官方文档给出的典型形式类似：

```bash
ego4d --output_directory="~/ego4d_data" --datasets full_scale annotations
```

也可以按 benchmark / annotation 子集下载，具体以官方 CLI 文档为准：

- https://ego4d-data.org/docs/CLI/

### 3.4 实际建议

- 如果你做的是 `video understanding / VLM / NLQ / forecasting`，优先申请 Ego4D
- 如果你做的是 `skill learning / ego-exo transfer / proficiency`，优先申请 Ego-Exo4D
- 这两套数据的工程重心更偏视频和 benchmark，不像 Aria 或 Xperience-10M 那样强调统一 HDF5 式多传感器结构

---

## 4. Xperience-10M

### 4.1 公开入口

- Release blog: https://ropedia.com/blog/20260316_xperience_10m
- Dataset card: https://huggingface.co/datasets/ropedia-ai/xperience-10m
- Sample: https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample
- Toolkit: https://github.com/Ropedia/HOMIE-toolkit

### 4.2 当前访问机制

截至 **2026-04-15**，公开信息显示 Xperience-10M 的访问具备以下特征：

- Hugging Face gated access
- 人工审核
- 仅限 approved non-commercial use
- 可能需要完成额外的 DocuSign 协议签署
- 大规模数据可能通过 controlled distribution 提供

这意味着它和公开 CLI 拉取型数据集不同，更像 `申请制 + 分发制`。

### 4.3 建议的实际顺序

#### Step 1: 先看样本和工具链

先下载 / 阅读：

- `xperience-10m-sample`
- `HOMIE-toolkit`
- 本仓库里的 `xperience/data/sample_trimmed/`

这样可以先搞清楚 episode 的目录结构、`annotation.hdf5` 的字段、六路视频如何对齐。

#### Step 2: 正式申请主数据

进入 Hugging Face dataset card 页面后：

1. 申请 access
2. 按页面提示完成额外协议签署
3. 等待人工审核

页面提示中明确说明：如果只提交了 access request，但没有完成需要的协议签署，申请会一直处于 pending。

### 4.4 为什么不能直接当成“普通下载任务”

因为它有两个硬门槛：

- 数据本身非常大，官方声明约 **~1 PB**
- 数据包含真实第一人称多模态记录，隐私与责任使用约束更强

所以更现实的路径是：

1. 用 sample 和 toolkit 验证技术可行性
2. 评估存储与训练预算
3. 再决定是否推进全量 access

### 4.5 仓库内现成脚本

```bash
python xperience/scripts/process_xperience.py xperience/data/sample_trimmed -o /tmp/xp_out
python xperience/scripts/build_sample_subset.py /path/to/annotation.hdf5 -o xperience/data/sample_trimmed
```

---

## 5. 推荐下载策略

| 目标 | 推荐数据 |
|------|----------|
| 先跑通 Aria 工具链 | AEA sample / ADT sample / mps_sample |
| 先做公开视频理解 | Ego4D |
| 先做技能理解 | Ego-Exo4D |
| 先验证 embodied 多模态结构 | Xperience-10M Sample |
| 先做高精度手-物体 | HOT3D |
| 先做身体动作建模 | Nymeria |

---

## 6. 各数据集的现实成本

| 数据集 | 下载门槛 | 存储压力 | 预处理复杂度 |
|--------|----------|----------|--------------|
| AEA / AEO | 低到中 | 中 | 中 |
| ADT | 中 | 高 | 中到高 |
| ASE | 高 | 很高 | 高 |
| Ego4D | 中 | 高 | 中 |
| Ego-Exo4D | 中 | 高 | 中到高 |
| HOT3D | 中 | 中 | 中到高 |
| Nymeria | 中 | 高 | 高 |
| Xperience-10M | 高 | 极高 | 高 |

---

## 7. 备注

1. 本仓库当前没有 `Ego4D` 的专用下载脚本。
2. 如果后续要继续改造这个仓库，优先应该补：
   - `Ego4D` 的最小下载与目录说明
   - `dataset access checklist`

*最后更新：2026-04-15*

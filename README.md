# Egocentric Data Research

这个仓库现在按子目录拆成两个主要方向：

- [aria/](./aria/): Meta Project Aria 相关脚本、样例数据和快速入口
- [xperience/](./xperience/): Xperience-10M 调研、处理脚本和轻量 sample

主仓库层只保留横向调研与导航，不再把所有脚本都放在根目录。

## 两个子目录各自做什么

### `aria/`

- 面向 `Project Aria` 的工程化目录
- 包含 `VRS / MPS` 处理脚本、下载脚本和官方小样例
- 适合立即跑通数据读取、提取图像、处理轨迹和点云

入口见 [aria/README.md](./aria/README.md)。

### `xperience/`

- 面向 `Xperience-10M` 的调研与轻量处理目录
- 包含 `annotation.hdf5` 的摘要脚本、sample 裁剪脚本和仓库内可提交的 trimmed sample
- 适合快速理解数据结构，而不是直接承载完整官方 sample

入口见 [xperience/README.md](./xperience/README.md)。

## 根目录文档

- [RESEARCH.md](./RESEARCH.md): Aria、Ego4D / Ego-Exo4D、Xperience-10M 的横向比较
- [OPEN_EGOCENTRIC_DATASETS.md](./OPEN_EGOCENTRIC_DATASETS.md): 更完整的公开 egocentric dataset 全景目录
- [TASK_TO_DATASET_GUIDE.md](./TASK_TO_DATASET_GUIDE.md): 按任务选数据集的实用指南
- [ACCESS_INFRA_COSTS.md](./ACCESS_INFRA_COSTS.md): 按访问门槛、存储和预处理成本选数据集
- [RESEARCH_PAPERS.md](./RESEARCH_PAPERS.md): 相关论文、基准与工具链
- [DOWNLOAD_GUIDE.md](./DOWNLOAD_GUIDE.md): 跨数据集访问与下载说明

## 当前边界

- `aria/` 提供真实可运行的本地处理脚本和现成 sample
- `xperience/` 提供真实可运行的 annotation 处理脚本，但仓库内 sample 是 **derived trimmed sample**，不是官方完整样例
- `Ego4D / Ego-Exo4D` 目前仍以调研与访问说明为主

*最后更新：2026-04-15*

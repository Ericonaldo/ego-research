# Egocentric Dataset Registry

## 1. 用法

这份文档把仓库当前重点覆盖的 egocentric dataset 收敛成一份更可执行的注册表，回答 5 个问题：

1. 官方入口在哪里
2. 访问方式是什么
3. License / 使用条款大致是什么
4. 本仓库有没有本地 parser / sample 支持
5. 如果要真正落地，第一步该做什么

### 1.1 本仓库中的 Local Support 状态

| 状态 | 含义 |
|------|------|
| `native` | 仓库里已有可运行脚本和 sample，能直接开始处理 |
| `partial` | 仓库里有部分工具、摘要脚本或 trimmed sample，但不是完整官方处理链 |
| `none` | 当前仓库里没有专用 parser / downloader |

---

## 2. 核心 Registry

| Dataset | Official Page | Access | License / Terms | Local Support | First Step |
|---------|---------------|--------|-----------------|---------------|------------|
| Project Aria ADT | https://www.projectaria.com/datasets/adt/ | Register | Project Aria dataset agreement / research access terms | `native` | 先在项目页申请下载链接，再用 `aria/scripts/download_dataset.sh` |
| Project Aria AEA | https://www.projectaria.com/datasets/aea/ | Register | Project Aria dataset agreement / research access terms | `native` | 先下载 CDN JSON，再跑 `aria/scripts/process_vrs.py` / `process_mps.py` |
| Project Aria ASE | https://www.projectaria.com/datasets/ase/ | Register | Project Aria dataset agreement / research access terms | `none` | 先看 ASE 官方下载器和 subset 下载说明 |
| HOT3D | https://facebookresearch.github.io/hot3d/ | Register | HOT3D license agreement | `none` | 先决定是下 full dataset 还是 Hugging Face 上的 HOT3D-Clips |
| Nymeria | https://www.projectaria.com/datasets/nymeria/ | Register | CC BY-NC 4.0 | `none` | 先看 `facebookresearch/nymeria_dataset` 的 viewer 和格式说明 |
| Reading in the Wild | https://www.projectaria.com/datasets/reading-in-the-wild/ | Register | Project Aria / dataset-specific access terms | `none` | 先通过 Project Aria 页面或 explorer 确认可下载 subset |
| Ego4D | https://ego4d-data.org/ | Register | Custom Ego4D license agreement via `ego4ddataset.com` | `none` | 先签 license，再装 CLI |
| Ego-Exo4D | https://ego-exo4d-data.org/ | Register | Custom Ego-Exo4D license agreement via `ego4ddataset.com/egoexo-license` | `none` | 先签 license，等待 AWS credentials，再用 `egoexo` CLI |
| EPIC-KITCHENS-100 | https://epic-kitchens.github.io/2020-100.html | Open | Dataset-specific terms on official site / download script | `none` | 先下载官方 script / annotations，再确定是否只取 RGB 或加 audio / VISOR |
| HoloAssist | https://github.com/Ember-HoloAssist/holoassist-release | Open | CDLAv2 | `none` | 先按 GitHub README 下载并解压单个 recording session 验证结构 |
| Assembly101 | https://assembly-101.github.io/ | Open | CC BY-NC 4.0 | `none` | 先下载 sample / Google Drive 版本，再决定是否拉完整多视角视频 |
| EgoBody | https://egobody.ethz.ch/ | Register | CC BY-NC-SA 4.0 with additional ETH terms | `none` | 先在注册页同意 terms，拿到 7 天有效下载凭证 |
| Egocentric-10K | https://huggingface.co/datasets/builddotai/Egocentric-10K | Gated | Apache-2.0 + Hugging Face gated access conditions | `none` | 先确认 contact-sharing gate，再决定 streaming 还是 shard 下载 |
| Xperience-10M | https://huggingface.co/datasets/ropedia-ai/xperience-10m | Gated | CC BY-NC 4.0 + controlled distribution requirements | `partial` | 先用 `xperience/data/sample_trimmed/` 和 `xperience/scripts/process_xperience.py` 熟悉结构 |
| Xperience-10M Sample | https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample | Open | sample release terms on Hugging Face | `partial` | 先对照本仓库的 trimmed sample 看 `annotation.hdf5` 结构 |
| SAYCam | https://osf.io/t4eaf/ | Open | OSF-hosted research data terms | `none` | 先下载一个 child subset 验证长期视频存储和切分方式 |
| ChildLens | https://www.eva.mpg.de/comparative-cultural-psychology/technical-development/childlens/ | Register / Gated | DOI / institutional access flow, see MPI page | `none` | 先确认 access 联系方式与可复用范围 |
| GTEA | https://ai.stanford.edu/~alireza/GTEA/ | Open | legacy academic dataset terms on project page | `none` | 先下载最小活动子集跑 baseline |
| GTEA Gaze / EGTEA Gaze+ | https://ai.stanford.edu/~alireza/GTEA_Gaze_Website/GTEA_Gaze%2B.html | Open | legacy academic dataset terms on project page | `none` | 先下 gaze + labels 子集做 attention / action baseline |
| TEgO | https://iamlabumd.github.io/tego/ | Open | CC BY 4.0 | `none` | 先下载 full image set，验证 object-centric task 定义 |
| You2Me | https://vision.cs.utexas.edu/projects/you2me/ | Open / Project release | project release terms on site | `none` | 先下载 dataset 再确认 dyadic skeleton/video 对齐方式 |
| First-Person Social Interactions | https://ai.stanford.edu/~alireza/Disney/ | Open | legacy academic dataset terms on project page | `none` | 先下载一个 day-long video + annotation 文件做时序解析 |

---

## 3. 本仓库当前最值得先落的几条线

### 3.1 立刻可跑

| Dataset | Why |
|---------|-----|
| Project Aria sample | 仓库里已经有 `aria/` 下的 sample 和处理脚本 |
| Xperience-10M trimmed sample | 仓库里已经有 `xperience/` 下的 trimmed sample 和摘要脚本 |

建议顺序：

1. 先跑 `aria/scripts/process_vrs.py` 和 `aria/scripts/process_mps.py`
2. 再跑 `xperience/scripts/process_xperience.py`
3. 确认团队更偏 `VRS/MPS` 还是 `structured HDF5 embodied annotations`

### 3.2 最值得补本地 parser 的下一批

| Dataset | 原因 |
|---------|------|
| Ego4D | 社区最成熟，值得有最小下载 / 目录解析脚本 |
| EPIC-KITCHENS-100 | benchmark 常用，数据结构相对标准 |
| HoloAssist | RGB-D / gaze / hand pose 对 assistant 场景很有代表性 |
| Egocentric-10K | 对工业和大规模 pretraining 有现实价值 |

---

## 4. 访问动作模板

### 4.1 Register / Gated 型

适用于：

- Ego4D
- Ego-Exo4D
- Aria family
- EgoBody
- Nymeria
- Egocentric-10K
- Xperience-10M

动作模板：

1. 先看 official page 的 license / access 页面
2. 先确认 credentials 有效期和续期机制
3. 先拿 sample 或 metadata，不要一上来全量下载
4. 先写目录检查脚本，再做模型训练

### 4.2 Open / Legacy 型

适用于：

- GTEA
- GTEA Gaze+
- TEgO
- First-Person Social Interactions
- UTE / You2Me

动作模板：

1. 先保存官方页面和下载脚本副本
2. 先验证下载链接今天仍然可用
3. 这些站点维护可能不稳定，最好同步做本地 checksum / 目录记录

---

## 5. 和现有文档的关系

- 想知道“有哪些数据”：看 [OPEN_EGOCENTRIC_DATASETS.md](./OPEN_EGOCENTRIC_DATASETS.md)
- 想按任务选：看 [TASK_TO_DATASET_GUIDE.md](./TASK_TO_DATASET_GUIDE.md)
- 想按成本选：看 [ACCESS_INFRA_COSTS.md](./ACCESS_INFRA_COSTS.md)
- 想知道“具体怎么拿、仓库里支不支持”：看本页

---

## 6. 当前已知缺口

1. 本仓库还没有 `Ego4D`、`EPIC-KITCHENS`、`HoloAssist` 的本地 parser。
2. `Project Aria` 虽然已有通用脚本，但还没有细化到每个子数据集的 dataset-specific helper。
3. `Xperience-10M` 目前是 sample / trimmed sample 级支持，不是 full dataset ingestion pipeline。

*最后更新：2026-04-15*

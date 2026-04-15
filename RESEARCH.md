# Egocentric / First-Person Data 调研报告

## 1. 调研目标

这个仓库原本主要记录 `Project Aria` 数据集信息。现在将范围扩展为 **egocentric / first-person data 调研**，重点回答下面几个问题：

- 哪些第一人称数据集适合做 `action understanding / HOI / world model / robotics / SLAM / 3D perception`
- 哪些数据集只是 `RGB video`，哪些已经覆盖 `depth / pose / mocap / IMU / language`
- 哪些数据集访问门槛低，哪些需要人工审批、协议签署或重基础设施
- `Xperience-10M` 这类新数据与 `Aria` / `Ego4D` 相比，到底新在哪里

更完整、面向“公开可访问数据目录”的版本见：

- [OPEN_EGOCENTRIC_DATASETS.md](./OPEN_EGOCENTRIC_DATASETS.md)
- [TASK_TO_DATASET_GUIDE.md](./TASK_TO_DATASET_GUIDE.md)
- [ACCESS_INFRA_COSTS.md](./ACCESS_INFRA_COSTS.md)

### 1.1 判断一个 egocentric 数据集的关键维度

| 维度 | 关注点 |
|------|--------|
| 规模 | 小时数、序列数、参与者数、场景数、总存储 |
| 模态 | RGB、音频、深度、轨迹、IMU、手/身体动作、语言标注 |
| 结构化程度 | 只是视频 + 标签，还是带统一时间同步和几何/动作结构 |
| Ground Truth | 手工标注、动捕、SLAM/MPS、合成、扫描 |
| 适用任务 | 分类、定位、跟踪、重建、机器人学习、world modeling |
| 使用门槛 | License、下载流程、存储、预处理难度 |

---

## 2. 数据集版图总览

### 2.1 按“研究用途”看

| 类别 | 代表数据集 | 典型用途 |
|------|------------|----------|
| 日常第一人称视频基准 | Ego4D, AEA | 长时活动理解、VLM 预训练、NLQ、预测 |
| Ego-Exo 技能理解 | Ego-Exo4D | 技能学习、跨视角对应、熟练度评估 |
| 3D / 几何 / 数字孪生 | ADT, ASE, DTC, HOT3D | 3D 检测、位姿、重建、sim-to-real |
| 身体/手部动作与穿戴感知 | Nymeria, HOT3D, Xperience-10M | 手部姿态、全身动作、motion modeling |
| 超大规模 embodied 数据 | Xperience-10M | world model、robot learning、multimodal pretraining |
| 专项任务数据 | Reading in the Wild, AEO | 阅读识别、3D 物体检测评测 |

### 2.2 按“数据结构成熟度”看

| 数据集 | 主要特点 | 结构化程度 |
|--------|----------|------------|
| Ego4D | 大规模第一人称视频 + 多任务标注 | 中 |
| Ego-Exo4D | ego + exo 同步技能数据 | 中到高 |
| Project Aria 家族 | 统一设备、VRS/MPS、部分 GT / 动捕 / 合成 | 高 |
| Xperience-10M | 六路视频 + 深度 + 手/身体 mocap + IMU + HDF5 | 很高 |

---

## 3. Project Aria 家族仍然是这个仓库的“工程主干”

虽然仓库定位已经扩到 broader egocentric data，但 **Aria 家族** 仍然是当前最适合和仓库现有脚本直接联动的数据生态，因为本仓库的处理脚本围绕 `VRS` 和 `MPS`。

### 3.1 Aria Gen 1 设备感知栈

| 传感器 | 数量 | 规格 |
|--------|------|------|
| RGB 相机 | 1 | 1408x1408, 110 deg FOV, 1/10/15/30 FPS |
| 单目 SLAM 相机 | 2 | 640x480, 150 deg FOV, 10/15/30 FPS |
| 眼动追踪相机 | 2 | 320x240, 80 deg FOV, 10/30/60 FPS |
| IMU | 2 | 1kHz + 800Hz |
| 磁力计 | 1 | - |
| 气压计 | 1 | - |
| 麦克风 | 7 | 48kHz 空间音频 |
| Wi-Fi / Bluetooth Beacon | 各 1 | 近场定位相关 |

### 3.2 Aria 数据格式

#### VRS

Meta 的多流传感器容器格式，适合把相机、IMU、音频、标定信息放进一个统一文件。

```python
from projectaria_tools.core import data_provider
provider = data_provider.create_vrs_data_provider("recording.vrs")
```

#### MPS

Meta 的云端感知处理输出，提供轨迹、点云、眼动、在线标定、部分数据集中的手部结果。

```python
from projectaria_tools.core.mps import read_closed_loop_trajectory
trajectory = read_closed_loop_trajectory("closed_loop_trajectory.csv")
```

### 3.3 Aria 家族开放数据集速览

| 数据集 | 规模 | 强项 | 更适合做什么 |
|--------|------|------|--------------|
| ADT | 236 sequences, ~3.5 TB | 高质量 GT + 合成渲染 + 物体/人体/深度/分割 | 3D 检测、位姿、重建、sim-to-real |
| AEA | 143 sequences, 7.3-7.5h, ~353 GB | 日常活动、多用户共享坐标、语音转写 | 长时活动理解、神经重建、定位建图 |
| ASE | 100K 场景, ~23 TB | 大规模合成 3D 场景 | 预训练、sim-to-real |
| HOT3D | 833+ min, 3.7M+ images | 双设备、多视角手-物体 GT | 6DoF 物体位姿、手-物体联合追踪 |
| Nymeria | 1,200 sequences, 300h | 全身运动、腕部设备、语言描述 | 身体追踪、动作建模、运动生成 |
| DTC | 2,000 物体模型 + 305 sequences | 高保真数字孪生物体 | NVS、逆渲染、物体重建 |
| AEO | 25 sequences, 45 min | 小而精的 3D OBB 基准 | 第一人称 3D 物体检测评测 |
| Reading in the Wild | 1,716 sequences, 100h | 阅读识别 + 60Hz 眼动 | 阅读检测、gaze-aware AI |

### 3.4 逐个数据集的研究定位

#### ADT

- 最强项是 `高质量 ground truth`
- 既有真实传感器数据，也有对齐的 photorealistic synthetic render
- 适合做：
  - 3D 物体检测 / 分割
  - 6DoF 物体位姿估计
  - 眼动与场景理解联合建模
  - sim-to-real 迁移

#### AEA

- 更接近日常生活而不是实验室受控场景
- 关键价值是 `共享全局坐标系 + 语音转文字 + 长时第一人称轨迹`
- 适合做：
  - activity recognition / action forecasting
  - neural scene reconstruction
  - audio-visual scene understanding
  - first-person localization / mapping

#### ASE

- 本质上是 Aria 生态里的大规模合成训练底座
- 如果你需要万级场景预训练，ASE 比真实数据更可扩展
- 代价是 domain gap 仍需要真实集验证

#### HOT3D

- 非常适合 `hand-object interaction`
- 和一般第一人称视频数据集不同，它不是为了泛动作识别，而是为了 **精确的 3D 手-物交互**
- 对 6DoF pose、BOP 风格评测尤其有价值

#### Nymeria

- 更偏向 `body motion + wearable sensing`
- Aria 只是其中一个视角，真正的核心是 `XSens 全身动捕 + wrist miniAria + layered language`
- 如果你想做第一人称身体追踪、语言到动作、穿戴感知融合，它比普通 egocentric video 数据更对口

#### DTC / AEO / Reading

- `DTC`: 适合物体数字孪生、NVS、逆渲染
- `AEO`: 适合小规模但高质量的 3D object detection 评测
- `Reading in the Wild`: 适合眼动 + 文本感知 + assistive AI

---

## 4. 非 Aria 的关键 egocentric 数据集

### 4.1 Ego4D

**官网**: https://ego4d-data.org/
**文档**: https://ego4d-data.org/docs/
**官方描述**: **3,670 小时**第一人称视频、**923** 名 camera wearers、74 个地点、9 个国家

#### 研究定位

Ego4D 仍然是最重要的通用第一人称视频基准之一。它最大的价值不是几何精度，而是：

- 长时、真实、全球分布的日常活动覆盖
- 多 benchmark 生态已经成熟
- 对 VLM / video-language / episodic memory / NLQ / forecasting 非常友好

#### 更适合做什么

- 视频预训练
- natural language query
- episodic memory / object memory
- hand-object interaction
- social / audio-visual tasks

#### 不足

- 相比 Aria family 或 Xperience-10M，几何与动作结构没那么“重”
- 如果你的目标是 `robotics / full-body motion / dense 3D state`，Ego4D 本身不够

### 4.2 Ego-Exo4D

**官网**: https://ego-exo4d-data.org/
**论文**: https://arxiv.org/abs/2311.18259
**更新说明**: https://discuss.ego4d-data.org/t/ego-exo4d-v2-full-ego-exo4d-release/552

#### 概述

由 Aria 眼镜和多台固定 exo 相机共同记录专业技能活动。官方公开信息显示完整发布包含：

- **1,286.30 小时**总视频
- **5,035** takes
- **221.26 小时** ego 视频
- 8 个技能领域，13 个城市

#### 它和 Ego4D 的差异

| 维度 | Ego4D | Ego-Exo4D |
|------|-------|------------|
| 主问题 | 日常第一人称理解 | 技能理解与跨视角对应 |
| 视角 | 主要是 ego | 同步 ego + exo |
| 亮点标注 | narration, NLQ, memory | keystep, proficiency, expert commentary |
| 典型任务 | 预训练、检索、预测 | 技能评估、跨视角迁移、姿态 |

#### 更适合做什么

- fine-grained skill understanding
- proficiency assessment
- ego-exo correspondence
- 教学演示与程序化步骤学习

---

## 5. Xperience-10M 重点调研

### 5.1 发布状态与来源

`Xperience-10M` 于 **2026-03-16** 由 Ropedia 发布。当前最重要的公开来源有 3 个：

- Release blog: https://ropedia.com/blog/20260316_xperience_10m
- Dataset card: https://huggingface.co/datasets/ropedia-ai/xperience-10m
- Loader / 可视化工具: https://github.com/Ropedia/HOMIE-toolkit

另外有一个公开样本：

- Sample: https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample

### 5.2 为什么它值得单独加入这个仓库

和大部分 egocentric dataset 不同，Xperience-10M 不是“视频数据集 + 标签”的思路，而是把 **human experience** 当成结构化 4D 信号来组织。

它强调的不是单一 benchmark，而是：

- 视觉
- 几何
- 轨迹
- 手部动作
- 全身动作
- IMU
- 分层语言描述

这些模态在同一 episode 中是时间同步、统一封装的。

### 5.3 官方公开的关键规模

根据 Hugging Face dataset card 与 release blog，截至 **2026-04-15** 可确认的核心指标包括：

| 指标 | 数值 |
|------|------|
| Experiences / interactions | 10M |
| Video with audio | 10,000 小时 |
| RGB frames | 2.88B |
| Depth frames | 720M |
| Camera poses | 576M |
| Mocap frames | 576M |
| IMU frames | 7.2B |
| Caption sentences | 16M |
| Caption words | 200M |
| Vocabulary | 6K |
| Objects | 350K |
| Total trajectory length | 39,000 km |
| Total storage | ~1 PB |

Release blog 还给出了更偏“数据分布”侧的信息：

- 约 **2,970** 人
- **1,756** 个 locations
- **1,301** 个 activity categories

### 5.4 数据组织方式

Xperience-10M 的一个典型 episode 公开结构如下：

```text
episode/
  fisheye_cam0.mp4
  fisheye_cam1.mp4
  fisheye_cam2.mp4
  fisheye_cam3.mp4
  stereo_left.mp4
  stereo_right.mp4
  annotation.hdf5
```

`annotation.hdf5` 里统一放：

- calibration
- slam trajectory / point cloud
- depth
- hand mocap
- full-body mocap
- imu
- video timestamps
- metadata
- caption

这个设计意味着它在工程上更像一个 **结构化 embodied dataset**，而不是纯视频语料。

### 5.5 支持的任务类型

官方 dataset card 明确列出的任务包括：

- egocentric action recognition
- task / subtask prediction
- action captioning
- temporal action localization
- human-object interaction understanding
- audio-visual learning
- visual-language pretraining
- stereo / monocular depth estimation
- visual odometry / SLAM
- hand pose estimation
- body motion estimation
- imitation learning
- policy learning for robotics
- world model training

### 5.6 和现有主流数据集相比，它强在哪里

| 对比对象 | Xperience-10M 的优势 | 仍然需要注意的问题 |
|----------|----------------------|--------------------|
| Ego4D | 多出深度、SLAM、手/身体 mocap、IMU、统一 HDF5 | Ego4D benchmark 生态更成熟 |
| Ego-Exo4D | 更大规模、更强 embodied state 结构 | Ego-Exo4D 的技能与专家点评标注更鲜明 |
| Aria AEA | 模态更完整、规模大很多 | AEA 更容易直接和 Aria 工具链结合 |
| Nymeria | 更大规模、任务覆盖更广 | Nymeria 的 wearable body tracking 标注链更成熟 |
| HOT3D | 覆盖更广，不只盯手物交互 | HOT3D 在精确手-物 GT 和 benchmark 上更专业 |

### 5.7 访问方式与现实门槛

Xperience-10M 当前不是“一键公开下载”的低门槛数据集。

公开资料显示它的访问流程包括：

- Hugging Face gated access
- 人工审核
- 非商业用途限制
- 可能需要额外签署 DocuSign 协议
- 部分数据通过 controlled distribution 提供

这意味着：

- 它非常适合做方向判断和技术规划
- 但不适合假设“今天申请、今天全量训练”
- 更现实的路径通常是先用 sample 和 HOMIE-toolkit 验证数据格式，再决定是否推进正式申请

### 5.8 研究判断

截至 **2026-04-15**，Xperience-10M 更像是一个 **基础设施级数据发布**，而不是已经形成成熟 leaderboard 生态的 benchmark。

我的判断是：

- 如果你的目标是 `world model / robotics / multimodal embodied pretraining`，它非常值得重点关注
- 如果你现在就要做 `公开 benchmark 对比`，Aria family、Ego4D、HOT3D 依然更成熟
- 如果你需要的是 `全身动作 + 手 + 几何 + IMU + 长时语言` 的同构数据结构，Xperience-10M 是当前公开信息里最激进的候选之一

---

## 6. 横向对比：做不同任务该优先看谁

### 6.1 数据集对比表

| 数据集 | 规模 / 成熟度 | 核心模态 | 典型 GT / 标注 | 推荐任务 |
|--------|----------------|----------|----------------|----------|
| ADT | 中规模，高精度 | RGB, SLAM, eye gaze, depth, segmentation | 动捕 + 合成 + 3D GT | 3D 感知、位姿、重建 |
| AEA | 中规模，真实日常 | RGB, SLAM, eye gaze, audio, transcript | MPS + 语音转写 | activity, AV, localization |
| ASE | 超大规模合成 | RGB, depth, instances, trajectory | 程序化 GT | 大规模预训练 |
| Ego4D | 超大规模视频 | video, audio, narration, benchmark labels | 人工标注为主 | VLM、检索、预测 |
| Ego-Exo4D | 大规模技能数据 | ego + exo video, pose, commentary | 多视角标注 | 技能理解、跨视角 |
| HOT3D | 专项高精度 | multi-view ego, hand/object | 光学动捕 | 手-物体追踪、6DoF pose |
| Nymeria | 大规模 wearable motion | ego video, wrist sensing, body motion, language | XSens + 分层语言 | 身体追踪、动作生成 |
| Xperience-10M | 超大规模 embodied data | 6 video streams, depth, pose, mocap, IMU, captions | 结构化多模态同步 | world model、robotics、pretraining |
| Reading in the Wild | 专项中规模 | video, 60Hz gaze | 阅读行为标注 | 阅读识别、assistive AI |

### 6.2 按研究方向推荐

| 研究方向 | 优先数据集 |
|----------|-----------|
| 通用第一人称视频理解 / VLM | Ego4D, AEA, Xperience-10M |
| 世界模型 / Embodied pretraining | Xperience-10M, ASE, Ego4D |
| 机器人模仿学习 / policy learning | Xperience-10M, Aria 相关机器人工作流, Ego-Exo4D |
| 3D 场景理解 / 重建 | ADT, AEA, ASE, Xperience-10M |
| 6DoF 物体位姿 / 手物交互 | HOT3D, ADT, DTC |
| 全身动作 / motion modeling | Nymeria, Xperience-10M |
| Gaze / 阅读 / 可穿戴 AI | Reading in the Wild, AEA |
| 跨视角技能学习 | Ego-Exo4D |

---

## 7. 对这个仓库的重新定位

### 7.1 现在这个仓库适合做什么

- 作为 **egocentric data landscape** 的内部知识库
- 帮你快速判断：
  - 该用 Aria family 还是 Ego4D
  - 该优先 benchmark 还是优先 embodied pretraining
  - `Xperience-10M` 值不值得投入申请和适配工程

### 7.2 仍然保留的工程价值

- `aria/scripts/process_vrs.py`
- `aria/scripts/process_mps.py`
- `aria/scripts/download_dataset.sh`

现在还新增了：

- `xperience/scripts/process_xperience.py`
- `xperience/scripts/build_sample_subset.py`

不过整体上，仓库现阶段最成熟的工程工具链仍然是 `Aria family`。

### 7.3 下一步如果继续扩展

建议优先做 3 件事：

1. 增加 `Ego4D` 的样例解析脚本或访问脚本说明
2. 为 `Xperience-10M Sample` 写一个最小可运行的解析笔记
3. 增加一份 `task -> dataset -> access cost -> infra cost` 的决策表

---

## 8. 核心结论

1. `Project Aria` 依然是这个仓库最可落地的数据生态，因为现有脚本、格式说明和样例都围绕它构建。
2. `Ego4D / Ego-Exo4D` 代表的是更成熟的公开 benchmark 生态，适合做通用第一人称理解和技能学习。
3. `Xperience-10M` 是这次改造里最值得补进来的新对象，因为它把 egocentric data 从“视频语料”推向了“结构化 embodied experience”。
4. 如果目标是 `机器人 / world model / multimodal embodied foundation model`，Xperience-10M 的战略价值已经高于很多传统第一人称视频集。
5. 如果目标是近期可复现、可下载、可对标的研究，Aria family、Ego4D、HOT3D 依然更现实。

*最后更新：2026-04-15*

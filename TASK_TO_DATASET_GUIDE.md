# Task -> Dataset 选型指南

## 1. 用法

这份文档不是再列一次数据集名字，而是回答更实际的问题：

- 我现在要做的任务是什么
- 应该先看哪几个 egocentric dataset
- 为什么是这些，而不是别的
- 哪些适合快速 baseline，哪些适合做中长期方向投入

默认和 [OPEN_EGOCENTRIC_DATASETS.md](./OPEN_EGOCENTRIC_DATASETS.md) 配合使用：

- 先在这里按任务缩小范围
- 再到目录文档里看访问方式、模态和项目页

---

## 2. 通用第一人称视频理解 / VLM 预训练

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | Ego4D | 社区最成熟，任务生态完整，适合做通用 video-language / memory / NLQ |
| 第一梯队 | EPIC-KITCHENS-100 | 厨房场景高密度动作标签非常稳定，benchmark 传统强 |
| 第二梯队 | EgoLife | 更接近长时 daily-life assistant，适合长上下文建模 |
| 第二梯队 | EgoSchema | 长视频 QA 很直接，适合 reasoning-oriented VLM |
| 长期方向 | Xperience-10M | 模态更重，适合向 embodied foundation model 过渡 |
| 长期方向 | Egocentric-10K | 工业第一人称规模大，适合 physical AI / industry-oriented pretraining |

### 什么时候先用谁

- 要做最容易对标的公开视频基线：`Ego4D + EPIC-KITCHENS-100`
- 要做长上下文 / episodic memory：`Ego4D + EgoSchema + EgoLife`
- 要做更接近 physical AI 的预训练：`Egocentric-10K + Xperience-10M`

---

## 3. 动作识别 / 动作预测 / action anticipation

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | EPIC-KITCHENS-100 | action recognition / anticipation 的传统核心 benchmark |
| 第一梯队 | Ego4D | forecasting、narration、memory 等子任务成熟 |
| 第二梯队 | AEA | 更贴近日常活动，带转写、轨迹和共享坐标 |
| 第二梯队 | MECCANO | 工业装配场景动作预测更有代表性 |
| 第二梯队 | EGTEA Gaze+ | 小规模但非常适合快速动作识别 baseline |
| 长期方向 | Xperience-10M | 如果动作预测要和手、IMU、深度一起建模 |

### 实际建议

- 通用 action benchmark：`EPIC-KITCHENS-100 + Ego4D`
- 工业装配动作预测：`MECCANO + IndEgo + Egocentric-10K`
- 想快速在小数据上迭代：`EGTEA Gaze+`

---

## 4. 技能学习 / ego-exo 对齐 / proficiency

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | Ego-Exo4D | 专门为技能、步骤、熟练度、专家点评设计 |
| 第一梯队 | Assembly101 | procedural activity、多视角和手部标注很强 |
| 第二梯队 | HoloAssist | 任务指导、协作和辅助场景更贴近 agent assistant |
| 第二梯队 | Charades-Ego | 可做 ego / third-person transfer 的轻量入口 |
| 长期方向 | EgoLife | 如果技能理解要和长时日常上下文结合 |

### 实际建议

- 技能评估 / keystep：`Ego-Exo4D`
- 程序化步骤 / assembly：`Assembly101`
- 交互式辅助 AI：`HoloAssist`

---

## 5. Hand-Object Interaction / manipulation / dexterous learning

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | HOT3D | 高精度 3D 手-物体交互和 6DoF pose benchmark |
| 第一梯队 | ARCTIC | articulated object manipulation 和 dynamic contact 很强 |
| 第一梯队 | HOI4D | RGB-D / 4D point cloud / HOI 任务覆盖广 |
| 第二梯队 | H2O | hand pose + object pose + RGB-D interaction |
| 第二梯队 | EgoDex | 更偏大规模 manipulation learning |
| 第二梯队 | HoloAssist | 如果交互伴随任务指导、语言和头部/手部状态 |
| 专项增强 | EgoPressure | 如果重点是 contact pressure 而不是单纯视觉 |
| 快速入口 | EgoHands / EgoGesture | 手检测、手势的小而快基线 |

### 实际建议

- 视觉 3D HOI benchmark：`HOT3D + ARCTIC + HOI4D`
- 操作学习 / imitation / policy：`EgoDex + OpenEgo + Xperience-10M`
- 只想先把手相关模型跑起来：`EgoHands + EgoGesture`

---

## 6. Tracking / segmentation / object-centric egocentric perception

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | TREK-150 | 第一人称 long-term tracking 很直接 |
| 第一梯队 | VISOR | dense segmentation、hand-object relations 清晰 |
| 第二梯队 | EgoTracks | Ego4D task subset，适合和大生态联动 |
| 第二梯队 | AEO | 第一人称 3D object detection 的小而精真实集 |
| 第二梯队 | ADT | 有更强 3D / depth / segmentation GT |

### 实际建议

- 2D long-term tracking：`TREK-150`
- 分割 / mask / HOI segmentation：`VISOR`
- 如果最终目标是 3D object perception：`AEO + ADT`

---

## 7. 3D 场景理解 / SLAM / reconstruction / embodied geometry

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | ADT | 高质量 GT + 合成渲染 + 3D 标注 |
| 第一梯队 | AEA | 日常场景、多用户、轨迹和共享坐标 |
| 第一梯队 | ASE | 大规模合成 3D 预训练底座 |
| 第二梯队 | DTC | 物体级数字孪生、NVS、逆渲染 |
| 第二梯队 | HOT3D | 手-物体 3D 交互更精确 |
| 长期方向 | Xperience-10M | 多模态结构化 embodied data |
| 长期方向 | Egocentric-10K | 工业第一人称物理场景 |

### 实际建议

- 3D detection / reconstruction 最成熟路线：`ADT + AEA + ASE`
- 物体级 3D / NVS / inverse rendering：`DTC`
- 走向更 general embodied geometry：`Xperience-10M`

---

## 8. 全身动作 / body tracking / motion modeling

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | Nymeria | wearable + XSens + language，egocentric body tracking 非常强 |
| 第一梯队 | EgoBody | egocentric full-body pose 的代表集 |
| 第二梯队 | GIMO | gaze-informed motion，适合 gaze + motion 方向 |
| 第二梯队 | EgoVIP | visual-inertial pose 方向的轻量入口 |
| 长期方向 | Xperience-10M | 如果全身动作要和更大规模视觉、深度、IMU联合预训练 |

### 实际建议

- egocentric body pose / motion generation：`Nymeria + EgoBody`
- 研究 gaze 对 motion 的作用：`GIMO`
- 研究 visual-inertial wearable pose：`EgoVIP`

---

## 9. Gaze / attention / reading / memory

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | Reading in the Wild | 60Hz gaze + 阅读识别，非常专项但价值高 |
| 第一梯队 | GTEA Gaze / EGTEA Gaze+ | gaze-aware action 的经典起点 |
| 第二梯队 | EGO-CH-Gaze | museum attended object detection 非常直接 |
| 第二梯队 | VEDB | head tracking / gaze / odometry 更完整 |
| 第二梯队 | EgoSchema | 如果目标是带长记忆的视频理解 |

### 实际建议

- 阅读识别 / assistive AI：`Reading in the Wild`
- attended object / gaze-aware action：`EGTEA Gaze+ + EGO-CH-Gaze`
- head / gaze / behavior modeling：`VEDB`

---

## 10. 工业 / 专项场景 / deployment-biased data

| 优先级 | 数据集 | 为什么 |
|--------|--------|--------|
| 第一梯队 | MECCANO | 工业装配与 gaze 非常有代表性 |
| 第一梯队 | IndEgo | Aria-based industrial assistant / QA / error detection |
| 第一梯队 | Egocentric-10K | 10,000h 工业第一人称规模，对 physical AI 很关键 |
| 第二梯队 | HoloAssist | task guidance / assistance / AR assistant 路线 |
| 第二梯队 | EGO-CH / VEDI | 场馆 / visitor understanding |
| 第二梯队 | HEV-I | vehicle-centric first-person driving |

### 实际建议

- 工业 assistant / error detection：`IndEgo + MECCANO + Egocentric-10K`
- 文化场馆导览：`EGO-CH + EGO-CH-Gaze + VEDI`
- 驾驶第一视角：`HEV-I`

---

## 11. 机器人 / imitation / world model

| 目标 | 推荐数据集 | 原因 |
|------|------------|------|
| imitation learning from human ego data | EgoDex, Xperience-10M, H2TC | manipulation / collaboration / structured embodied trajectories |
| embodied foundation model pretraining | Xperience-10M, Egocentric-10K, EgoLife, ASE | 规模大、模态重、长期上下文 |
| robot-centric first-person perception | JRDB, HEV-I, UTKinect-FirstPerson | observer-centric deployment 更接近机器人和载具 |
| wearable assistant + physical context | HoloAssist, Nymeria, Aria family | gaze / IMU / pose / task context 更完整 |

### 实际建议

- 如果是现在就能开干的公开 benchmark：`HoloAssist + H2TC + Aria family`
- 如果是中长期 embodied / world model：`Xperience-10M + Egocentric-10K + EgoLife`

---

## 12. 两条常用选型路径

### 12.1 想先发论文，优先可复现与对标

1. 从 `Ego4D / EPIC-KITCHENS / Ego-Exo4D / HOT3D / Assembly101 / Aria family` 里选
2. 优先选择 benchmark 清晰、baseline 多、公开生态成熟的数据
3. 避免一开始就押注 PB 级 gated 数据

### 12.2 想押注下一代 embodied AI

1. 先用 `Xperience-10M / Egocentric-10K / EgoLife / Nymeria / HoloAssist`
2. 接受 access friction、存储成本和预处理复杂度更高
3. 把目标从“单任务 leaderboard”切换到“统一表征或 agent 能力”

---

## 13. 最后的判断

1. 通用公开视频最成熟的核心盘仍然是 `Ego4D + EPIC-KITCHENS-100`。
2. 技能和程序化任务最值得看 `Ego-Exo4D + Assembly101 + HoloAssist`。
3. 手-物体交互和 dexterous manipulation 已经是一条独立赛道，优先看 `HOT3D + ARCTIC + HOI4D`。
4. 若目标转向 embodied foundation model，优先级会明显转到 `Xperience-10M + Egocentric-10K + EgoLife + Nymeria`。

*最后更新：2026-04-15*

# Dataset Access / Infra 成本矩阵

## 1. 说明

这份文档回答的是另一个更现实的问题：

- 这个数据集能不能拿到
- 拿到之后要准备多少存储
- 预处理到底麻不麻烦
- 适合 laptop、单卡、工作站，还是多机分布式

这里用的是**相对分级**，不是绝对预算表。

### 1.1 分级口径

| 维度 | 分级 |
|------|------|
| Access Friction | Low / Medium / High / Very High |
| Storage Pressure | Small / Medium / Large / Very Large / Extreme |
| Preprocessing | Low / Medium / High / Very High |
| Compute Readiness | Laptop / Single GPU / Workstation / Multi-GPU / Cluster |

### 1.2 大致对应

| 存储分级 | 粗略量级 |
|----------|----------|
| Small | < 100 GB |
| Medium | 100 GB - 1 TB |
| Large | 1 TB - 10 TB |
| Very Large | 10 TB - 100 TB |
| Extreme | 100 TB 以上，直到 PB 级 |

---

## 2. 总表

| 数据集 | Access Friction | Storage Pressure | Preprocessing | Compute Readiness | 原因 |
|--------|-----------------|------------------|---------------|-------------------|------|
| EgoHands | Low | Small | Low | Laptop | 小规模、纯视觉、直接可用 |
| GTEA Gaze / EGTEA Gaze+ | Low | Small | Low | Laptop | 经典小集，适合快速 baseline |
| TREK-150 | Low | Small | Low | Laptop / Single GPU | tracking benchmark，负担低 |
| BEOID | Low | Small | Low | Laptop | 老但轻量 |
| VEDI | Low | Small | Low to Medium | Laptop | 专项数据，体量不大 |
| EgoK360 | Low | Small to Medium | Low | Laptop / Single GPU | 360 视频但总体可控 |
| EPIC-KITCHENS-100 | Low | Medium | Medium | Single GPU / Workstation | 视频量不小，但工具链成熟 |
| EPIC-KITCHENS-55 | Low | Medium | Medium | Single GPU | 经典公开视频集 |
| Charades-Ego | Low | Medium | Low to Medium | Single GPU | paired video，门槛较低 |
| EgoSchema | Low | Medium | Low | Single GPU | 多数成本在 long-context 模型而不是数据本身 |
| EgoCom | Low | Medium | Medium | Single GPU | 需要处理音频、说话人和对话结构 |
| Assembly101 | Medium | Large | High | Workstation / Multi-GPU | 多视角、3D 手、程序标签丰富 |
| HoloAssist | Medium | Large | High | Workstation | RGB-D + gaze + hand/head pose + IMU |
| HOT3D | Medium | Large | High | Workstation / Multi-GPU | 3D hand-object 精细标注，处理链较重 |
| ARCTIC | Medium | Large | High | Workstation / Multi-GPU | articulated object + contact + mesh |
| HOI4D | Medium | Large | High | Workstation | RGB-D / point cloud / HOI 任务多 |
| EgoBody | Medium | Large | High | Workstation | body pose / shape 管线复杂 |
| Nymeria | High | Large | Very High | Workstation / Multi-GPU | 多设备、多模态、body mocap + language |
| ADT | Medium | Large | High | Workstation / Multi-GPU | 3D GT 丰富，文件重，格式复杂 |
| AEA | Medium | Medium to Large | Medium to High | Workstation | Aria + MPS + transcript |
| ASE | High | Very Large | Very High | Multi-GPU / Cluster | 100K 场景，偏预训练基础设施 |
| DTC | Medium | Medium to Large | High | Workstation | 物体扫描 + Aria / DSLR 序列 |
| Reading in the Wild | Medium | Medium | Medium | Single GPU / Workstation | 60Hz gaze 和阅读任务结构 |
| Ego4D | Medium | Large | Medium to High | Workstation / Multi-GPU | 规模大、任务多、下载流程需要协议 |
| Ego-Exo4D | Medium | Large | High | Workstation / Multi-GPU | 多视角技能数据，处理比 Ego4D 更重 |
| IndEgo | Low to Medium | Medium to Large | Medium | Workstation | 工业场景、Aria-derived annotations |
| Egocentric-10K | High | Extreme | Very High | Multi-GPU / Cluster | 16.4TB+ 且以工业大规模预训练为目标 |
| Xperience-10M | Very High | Extreme | Very High | Cluster | gated + 约 1PB + 结构化多模态处理链 |
| EgoLife | Medium to High | Large | High | Workstation / Multi-GPU | 长时上下文、多模态、同步 exo |
| H2TC | Medium | Medium to Large | High | Workstation | 协作、动作和多传感器同步 |
| HEV-I | Low | Small to Medium | Medium | Single GPU | driving-specific，规模不大 |
| JRDB | Medium | Large | High | Workstation | robot-centric perception，3D / tracking 管线偏重 |

---

## 3. 快速筛选

### 3.1 只有一台个人工作站，应该先看什么

优先：

- EgoHands
- GTEA Gaze / EGTEA Gaze+
- TREK-150
- EPIC-KITCHENS-100
- EgoSchema
- Reading in the Wild
- VEDI

谨慎：

- Ego4D
- HoloAssist
- Assembly101

暂时别一上来就碰：

- ASE
- Egocentric-10K
- Xperience-10M

### 3.2 有一台像样的多卡工作站，可以看什么

优先：

- Ego4D
- Ego-Exo4D
- ADT / AEA / HOT3D
- HoloAssist
- Assembly101
- Nymeria
- EgoBody

### 3.3 有集群或分布式训练条件，可以看什么

优先：

- ASE
- Egocentric-10K
- Xperience-10M
- 大规模 Ego4D / EgoLife 联合预训练

---

## 4. 访问成本最值得注意的几类

### 4.1 Low Friction

这类最适合快速跑通：

- EgoHands
- GTEA Gaze / EGTEA Gaze+
- TREK-150
- BEOID
- EPIC-KITCHENS
- VEDI

特点：

- 公开下载或官方页面很直接
- 很少需要人工审核
- 适合作为第一个 prototype 数据集

### 4.2 Medium Friction

这类通常需要注册、协议或更复杂的下载说明：

- Ego4D
- Ego-Exo4D
- Project Aria family
- HoloAssist
- Assembly101
- EgoBody

特点：

- 研究社区成熟
- 访问不算难，但不是点一下就下完
- 值得投入，因为 benchmark / baseline 丰富

### 4.3 High / Very High Friction

这类不要在没有明确目标时贸然投入：

- Nymeria
- ASE
- Egocentric-10K
- Xperience-10M

特点：

- 数据量大
- 预处理复杂
- 有 gated access、额外协议或极高存储压力
- 更适合长期方向，而不是短平快 benchmark

---

## 5. 预处理成本来自哪里

### 5.1 低成本

往往是：

- 单路 RGB 视频
- 分类 / tracking / QA label
- 不需要复杂几何或多传感器同步

代表：

- EgoHands
- TREK-150
- EgoSchema
- Charades-Ego

### 5.2 中高成本

往往是：

- RGB + audio + transcript
- 多视角同步
- 深度、点云、姿态、mocap、IMU

代表：

- Ego4D
- HoloAssist
- Assembly101
- ADT / AEA / HOT3D
- Nymeria
- Xperience-10M

### 5.3 特别高成本

通常会同时出现：

- 自定义格式
- 极大规模
- 多设备对齐
- 需要自己构建数据引擎或缓存层

代表：

- ASE
- Egocentric-10K
- Xperience-10M

---

## 6. 推荐的现实路径

### 6.1 论文导向，想先出结果

1. 先选 `Low / Medium Friction` 数据
2. 优先 benchmark 清晰的集合：`EPIC-KITCHENS`, `Ego4D`, `Ego-Exo4D`, `HOT3D`, `Assembly101`
3. 不要让下载和预处理吞掉大部分研究时间

### 6.2 产品或长期基础模型导向

1. 可以接受 `High / Very High Friction`
2. 优先看 `Egocentric-10K`, `Xperience-10M`, `Nymeria`, `EgoLife`
3. 先做小 sample 验证，再决定是否申请全量访问

### 6.3 本仓库里最适合立刻开干的

当前仓库最容易直接启动的是：

- `aria/` 下的 Project Aria sample 和脚本
- `xperience/` 下的 trimmed sample 和 annotation 处理脚本

这两条路线的好处是：

- 仓库里已经有现成数据和脚本
- 不需要你先补完整数据引擎
- 一个偏 `Aria / VRS / MPS`
- 一个偏 `structured HDF5 embodied annotation`

---

## 7. 最后的判断

1. 最低成本的起步数据仍然是 `EgoHands / GTEA Gaze / TREK-150 / EPIC-KITCHENS` 这一层。
2. 真正的研究主战场仍然是 `Ego4D / Ego-Exo4D / Aria family / HOT3D / Assembly101`。
3. 如果你的方向是 embodied AI，真正需要提前评估的是 `数据访问成本 + 存储成本 + 预处理成本`，而不是只看 benchmark 名气。
4. `Xperience-10M` 和 `Egocentric-10K` 的问题从来不是“值不值得看”，而是“你现在的基础设施是否接得住”。

*最后更新：2026-04-15*

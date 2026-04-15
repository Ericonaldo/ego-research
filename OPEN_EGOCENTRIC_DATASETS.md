# 开源 Egocentric / First-Person 数据集全景目录

## 1. 说明与边界

这份文档的目标，是在现有 `RESEARCH.md` 的基础上，继续扩展成一份更接近 **“公开可获取的 egocentric dataset catalog”** 的目录。

为了避免把“论文里提到过”与“实际上可访问”混为一谈，这里采用下面的口径：

- **Open**: 有明确公开下载入口，通常可直接下载
- **Register**: 需要注册或同意研究协议，但不一定需要人工审核
- **Gated**: 需要人工审核、申请、或平台 gated access
- **Legacy**: 早期数据集，公开信息仍可找到，但下载链路和维护状态较弱

这份目录尽量覆盖 **截至 2026-04-15 仍能找到公开入口、官方页面、代码仓库或 gated release 的主流与代表性数据集**。  
它不是对“所有历史论文中出现过的第一人称数据”做无差别堆砌，而是优先保留：

- 社区仍在使用
- 仍有公开访问路径
- 对研究选型有现实参考价值

如果你已经知道自己的任务或算力约束，可以直接配合这两份文档使用：

- [TASK_TO_DATASET_GUIDE.md](./TASK_TO_DATASET_GUIDE.md)
- [ACCESS_INFRA_COSTS.md](./ACCESS_INFRA_COSTS.md)

---

## 2. 先看结论

如果你不想先看完整目录，可以先看这个压缩版判断：

| 目标 | 优先看哪些数据集 |
|------|------------------|
| 通用第一人称视频理解 / VLM | Ego4D, EPIC-KITCHENS-100, EgoLife, EgoSchema |
| 技能学习 / ego-exo 对齐 | Ego-Exo4D, Assembly101, HoloAssist |
| 手-物体交互 / dexterous manipulation | HOT3D, HOI4D, ARCTIC, H2O, EgoDex |
| 3D / wearable / embodied multimodal | Project Aria family, Nymeria, Xperience-10M, Egocentric-10K |
| Gaze / attention | GTEA Gaze, EGTEA Gaze+, Reading in the Wild, VEDB |
| 全身动作 / egocentric body modeling | EgoBody, Nymeria, GIMO, EgoVIP |
| 工业 / 专项场景 | MECCANO, IndEgo, Egocentric-10K |
| 文化场馆 / 导览 / museum | EGO-CH, EGO-CH-Gaze, VEDI |
| 机器人 / robot-centric first-person | JRDB, H2TC, UTKinect-FirstPerson, HEV-I |

---

## 3. Foundational 与长时日常第一人称数据

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [Ego4D](https://ego4d-data.org/) | Register | 3,600h+，900+ wearers，74 locations | Video, audio, narrations, multi-task labels | 通用第一人称预训练、episodic memory、NLQ、forecasting |
| [Ego-Exo4D](https://ego-exo4d-data.org/) | Register | 1,286.30h，5,035 takes | Ego + exo video, pose, commentary, keysteps | 技能学习、跨视角对应、熟练度评估 |
| [EPIC-KITCHENS-100](https://epic-kitchens.github.io/2020-100.html) | Open | 100h，45 kitchens，20M frames，90K action segments | Head-mounted RGB video, audio, narrations | 厨房动作理解、action recognition / anticipation |
| [EPIC-KITCHENS-55](https://epic-kitchens.github.io/2020-55) | Open | 55h 级别 | RGB video, narrations | 经典厨房第一人称 benchmark |
| [Charades-Ego](https://prior.allenai.org/projects/charades-ego) | Open | 68.8h paired first/third-person video | Ego + third-person paired video | ego-exo transfer、action recognition |
| [EgoSchema](https://egoschema.github.io/index.html) | Open | 5K+ QA，250h+，3-minute clips | Ego4D-derived long-form video QA | 长视频理解、temporal reasoning |
| [EgoCom](https://github.com/facebookresearch/EgoCom-Dataset) | Open | 38.5h，39 conversations | Egocentric video, stereo audio, transcripts, speaker labels | 对话建模、turn-taking、audio-visual conversation |
| [EgoLife](https://egolife-ai.github.io/) | Open / Project release | ~300h（6 人，约 50h/人） | Ego video, gaze, IMU, synchronized exo views, dense captions | 长时 daily-life assistant、hours-to-days context understanding |
| [Egocentric-10K](https://huggingface.co/datasets/builddotai/Egocentric-10K) | Gated | 10,000h，1.08B frames，16.4TB | Monocular head-mounted factory video, intrinsics, metadata | 工业场景 pretraining、robotics、physical AI |
| [Xperience-10M](https://huggingface.co/datasets/ropedia-ai/xperience-10m) | Gated | 10M experiences，10,000h video，~1PB | Multi-video, depth, SLAM, mocap, IMU, captions | embodied pretraining、world model、robotics |
| [SAYCam](https://osf.io/t4eaf/) | Open | ~500h，3 名儿童的长期记录 | Infant egocentric audio-video | developmental learning、child-centric representation learning |
| [Visual Experience Dataset / VEDB](https://osf.io/2gdkb/wiki) | Open | 240h+ | Egocentric video, gaze, head tracking, odometry | gaze / head / visual behavior 建模 |

### 3.1 这一层数据的现实意义

- `Ego4D / EPIC-KITCHENS` 依然是最实用的公开视频基础盘
- `Ego-Exo4D / EgoSchema / EgoCom` 代表了“长上下文 / 多视角 / 对话”这三个更具体的方向
- `EgoLife / Egocentric-10K / Xperience-10M` 则是 2025-2026 年更偏 **基础设施化** 的新路线，目标不再只是 benchmark，而是更直接服务 embodied AI

---

## 4. 手部、物体交互与 dexterous manipulation

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [EgoHands](https://vision.soic.indiana.edu/projects/egohands/) | Open | 48 videos，4,800 labeled frames，15,000+ hands | RGB video, hand masks | egocentric hand detection / segmentation |
| [EgoGesture](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html) | Open | 83 gesture classes | RGB, depth, IR | hand gesture recognition |
| [First-Person Hand Action Benchmark (FPHA / F-PHAB)](https://arxiv.org/abs/1704.02463) | Legacy / Open paper-linked | 100K+ frames，45 daily hand actions | RGB-D video, 3D hand pose, actions | first-person hand action / hand pose |
| [H2O](https://arxiv.org/abs/2104.11181) | Open / paper-linked | large multi-view RGB-D interaction set | Egocentric + exocentric RGB-D, hand pose, object pose, camera pose | hand-object pose、interaction recognition |
| [HoloAssist](https://github.com/Ember-HoloAssist/holoassist-release) | Open | 166h，222 participants，20 tasks | RGB, depth, gaze, 3D hand pose, head pose, IMU, audio, text | assistive AI、interactive task guidance |
| [Assembly101](https://assembly-101.github.io/) | Open | 4,321 videos，8 static + 4 ego，100K+ coarse / 1M fine actions，18M 3D hand poses | Multi-view + egocentric video, hand pose, procedural labels | procedural activity、mistake detection、cross-view transfer |
| [AssemblyHands](https://assemblyhands.github.io/) | Open / benchmark-oriented | large-scale egocentric hand pose benchmark | Egocentric images, 3D hand pose | hand pose under procedural manipulation |
| [HOT3D](https://facebookresearch.github.io/hot3d/) | Register / project access | 833+ min，3.7M+ images | Egocentric multi-view video, 3D hands, 6DoF objects, Aria signals | hand-object tracking、6DoF pose estimation |
| [HOI4D](https://arxiv.org/abs/2203.01577) | Open / paper-linked | 2.4M RGB-D frames 级别 | RGB-D, 4D point cloud, HOI labels | category-level HOI、pose tracking、action segmentation |
| [ARCTIC](https://arctic.is.tue.mpg.de/) | Register | 2.1M video frames | Bi-manual hand-object video, 3D meshes, dynamic contact | articulated object manipulation、contact-aware reconstruction |
| [EgoPAT3D](https://ai4ce.github.io/EgoPAT3D/) | Open | 150 recordings，~600 min，~1.08M RGB frames | RGB, depth, IR, IMU, temperature, point cloud | action target prediction、RGB-D manipulation |
| [EgoPressure](https://yiming-zhao.github.io/EgoPressure/) | Pre-release / Register | 5.0h，21 participants | Egocentric RGB-D, pressure map, hand mesh, skeleton | contact pressure estimation、fine-grained touch understanding |
| [EgoDex](https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation) | Open / gated assets by source | large-scale dexterous manipulation | Egocentric video, skeletal pose, language | manipulation learning from human egocentric data |
| [OpenEgo](https://github.com/physicalinc/openego) | Open | composite benchmark layer | standardized multimodal egocentric manipulation annotations | 统一多个 manipulation datasets 的训练/评测接口 |
| [HANDdata](https://www.nature.com/articles/s41597-023-02313-w) | Open | ~6,000 reach-to-grasp interactions, 29 adults | First-person video + proximity + kinematics | reach-to-grasp、sensor fusion、human-object handling |
| [TREK-150](https://machinelearning.uniud.it/datasets/trek150/) | Open | 150 videos，97,296 frames，34 objects | Egocentric tracking sequences | long-term object tracking in FPV |
| [EgoObjects](https://arxiv.org/abs/2309.08816) | Open / benchmark | large-scale fine-grained object understanding | Egocentric video + object-centric annotations | fine-grained object understanding |

### 4.1 这一层的关键分化

- 如果你要做 **手部分割 / 检测**：`EgoHands`
- 如果你要做 **手势识别**：`EgoGesture`
- 如果你要做 **手-物体 3D 交互**：`HOT3D / HOI4D / ARCTIC / H2O`
- 如果你要做 **交互式 AI copilot**：`HoloAssist`
- 如果你要做 **procedural manipulation**：`Assembly101 / EgoDex / OpenEgo`
- 如果你要做 **tracking**：`TREK-150`
- 如果你要做 **pressure / tactile-aware interaction**：`EgoPressure`

---

## 5. Wearable、全身动作、3D 与 embodied multimodal

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [Aria Digital Twin (ADT)](https://www.projectaria.com/datasets/adt/) | Register | 236 sequences，~3.5TB | Aria video, GT trajectory, depth, segmentation, object/human GT | 3D perception、sim-to-real |
| [Aria Everyday Activities (AEA)](https://www.projectaria.com/datasets/aea/) | Register | 143 sequences，7.3h+ | Aria video, eye gaze, MPS, speech transcript | activity understanding、scene reconstruction |
| [Aria Synthetic Environments (ASE)](https://www.projectaria.com/datasets/ase/) | Register | 100K synthetic scenes | synthetic RGB, depth, instances, trajectory | large-scale 3D pretraining |
| [Nymeria](https://www.projectaria.com/datasets/nymeria/) | Register | 300h，1,200 sequences | Aria + miniAria + XSens body mocap + language | egocentric body tracking、motion generation |
| [Aria Everyday Objects (AEO)](https://www.projectaria.com/datasets/aeo/) | Register | 25 sequences | egocentric video + 3D OBB | egocentric 3D object detection |
| [Digital Twin Catalog (DTC)](https://www.projectaria.com/datasets/dtc/) | Register | 2,000 objects + Aria/DSLR sequences | 3D object scans, Aria sequences | digital twin / NVS / inverse rendering |
| [Reading in the Wild](https://www.projectaria.com/datasets/reading-in-the-wild/) | Register | 100h，1,716 sequences | video, 60Hz eye tracking, trajectory | reading recognition、assistive AI |
| [Aria Gen 2 Pilot (A2PD)](https://www.projectaria.com/datasets/gen2pilot/) | Register | pilot-scale | next-gen multimodal glasses data | next-gen wearable sensing research |
| [EgoBody](https://egobody.ethz.ch/) | Register | indoor scenes / social interactions | egocentric + exocentric capture, body pose/shape | full-body pose from egocentric view |
| [GIMO](https://github.com/y-zheng18/GIMO) | Register / non-commercial | motion dataset | gaze + egocentric video + body motion context | gaze-informed human motion prediction |
| [IndEgo](https://github.com/Vivek9Chavan/IndEgo) | Open | 197h，3,460 recordings | Aria video, gaze, hand pose, point cloud, industrial QA annotations | industrial assistant、error detection、QA |
| [H2TC](https://h2tc-roboticsx.github.io/dataset/) | Open / dataset guide | human-human / human-object multimodal data | ego + third-person, body/hand/object motions, mocap-style annotations | human motion transfer、robotics collaboration |
| [EgoVIP](https://sites.google.com/site/youngwooncha/egovip) | Open | visual-inertial pose data | egocentric video + IMUs | 3D body pose from wearable visual-inertial sensing |

### 5.1 这一层和普通 ego-video 的区别

这一组数据的核心不是“把日常视频拍下来”，而是把第一人称视觉和：

- 眼动
- IMU
- 点云 / SLAM
- 手部或全身动作
- 语言

这些更接近 **embodied state** 的信号绑在一起。  
如果你的任务已经开始涉及 AR glasses、robotics、motion modeling、world model，这一组往往比纯视频 benchmark 更重要。

---

## 6. Gaze、注意力、记忆与派生 benchmark

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [GTEA Gaze](https://ai.stanford.edu/~alireza/GTEA_Gaze_Website/GTEA_Gaze.html) | Open | classic small-scale kitchen gaze set | video + gaze | early gaze-aware action research |
| [GTEA Gaze+ / EGTEA Gaze+](https://ai.stanford.edu/~alireza/GTEA_Gaze_Website/GTEA_Gaze%2B.html) | Open | extended kitchen gaze benchmark | video + gaze + action labels | gaze-aware action understanding |
| [EgoSchema](https://egoschema.github.io/index.html) | Open | 5K+ long-form MCQ | long-form ego video + QA | long-context video understanding |
| [EgoTracks](https://ego4d-data.org/docs/data/egotracks/) | Register | Ego4D task subset | ego video + tracking annotations | egocentric visual object tracking |
| [VISOR](https://epic-kitchens.github.io/VISOR) | Open | EPIC-derived dense segmentation benchmark | egocentric video + masks + hand/object relations | hand/object segmentation |
| [Ego4DSounds](https://ego4dsounds.github.io/) | Open / task subset | Ego4D audio subset | ego video + audio labels | sound-aware egocentric understanding |
| [EGO-CH-Gaze](https://iplab.dmi.unict.it/EGO-CH-Gaze/) | Open | 7 subjects，14 videos，220K RGB images | museum ego video + gaze + boxes | attended object detection with gaze |

### 6.1 判断

- 如果你要做 **第一人称 gaze prediction / attended object**，`GTEA Gaze+` 和 `EGO-CH-Gaze` 很直接
- 如果你要做 **长时问答**，`EgoSchema` 比一般 action benchmark 更贴近 long-context reasoning
- 如果你要做 **tracking / segmentation**，`EgoTracks` 和 `VISOR` 是更任务化的子集

---

## 7. 专项、行业或场景化数据

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [MECCANO](https://iplab.dmi.unict.it/MECCANO/) | Open | 20 subjects，RGB/Depth/Gaze，8,857 segments | industrial-like assembly, gaze, depth | industrial HOI、action anticipation |
| [EGO-CH](https://arxiv.org/abs/2002.00899) | Open / paper-linked | cultural heritage visits | egocentric video in museum / cultural sites | visitor behavior understanding |
| [VEDI](https://iplab.dmi.unict.it/VEDI/) | Open | 9 environments，57 POIs | HoloLens + chest GoPro + annotations | visitor localization in cultural sites |
| [EgoK360](https://egok360.github.io/) | Open | 360-degree activity set | 360 egocentric video | 360 first-person activity recognition |
| [BEOID](https://data.bris.ac.uk/data/dataset/o4hx7jnmfqt01lyzf2n4rchg6) | Open | object interaction dataset | egocentric object interactions | handled object recognition / interaction analysis |
| [ASCC Activities of Daily Living Dataset](https://ascclabopensource.github.io/) | Open | chest-mounted daily living data | image, audio, motion | multimodal ADL recognition |
| [Reading in the Wild](https://www.projectaria.com/datasets/reading-in-the-wild/) | Register | 100h | video + 60Hz gaze | reading activity detection |
| [HEV-I](https://usa.honda-ri.com/hevi) | Open | 230 driving clips at intersections | vehicle egocentric video + signals | egocentric driving / future localization |

### 7.1 这一层为什么不能忽略

很多工作实际上不需要“最大的数据集”，而需要 **正确的场景偏置**：

- 工业装配：`MECCANO`, `IndEgo`, `Egocentric-10K`
- 博物馆 / 场馆导览：`EGO-CH`, `EGO-CH-Gaze`, `VEDI`
- 360 wearable video：`EgoK360`
- 驾驶 / vehicle egocentric：`HEV-I`

---

## 8. 机器人、robot-centric 与非头戴但第一人称视角

| 数据集 | Access | 粗略规模 | 核心模态 | 适合做什么 |
|--------|--------|----------|----------|------------|
| [JRDB](https://jrdb.erc.monash.edu/) | Open / Register | robot social navigation benchmark | robot egocentric RGB / 3D sensing | robot-centric first-person perception |
| [UTKinect-FirstPerson](https://cvrc.ece.utexas.edu/KinectDatasets/FirstPerson.html) | Open | legacy RGB-D robot-centric dataset | first-person RGB-D | early robot-centric action recognition |
| [H2TC](https://h2tc-roboticsx.github.io/dataset/) | Open | multimodal human task collaboration | egocentric + third-person + mocap-like annotations | imitation / collaboration / robotics |
| [HEV-I](https://usa.honda-ri.com/hevi) | Open | 230 intersection driving videos | egocentric driving video + GPS/IMU/vehicle state | driver assistance, future localization |

### 8.1 范围说明

这类数据不一定是“人戴摄像机”，但仍然是 **first-person observer-centric** 视角。  
如果你的课题是机器人、自动驾驶、mobile manipulation，这些数据比纯 human wearable video 更贴近部署场景。

---

## 9. Legacy 但仍值得知道的早期数据

| 数据集 | Access | 粗略规模 | 核心模态 | 备注 |
|--------|--------|----------|----------|------|
| [ADL](https://people.csail.mit.edu/hpirsiav/papers/adl_cvpr12.pdf) | Legacy | ~1M frames，18 actions 级别 | head-mounted video | 最早一批 ADL egocentric benchmark 之一 |
| [GTEA Gaze](https://ai.stanford.edu/~alireza/GTEA_Gaze_Website/GTEA_Gaze.html) | Open | small-scale kitchen gaze | video + gaze | 经典 gaze benchmark |
| [EGTEA Gaze+](https://ai.stanford.edu/~alireza/GTEA_Gaze_Website/GTEA_Gaze%2B.html) | Open | extended kitchen gaze benchmark | video + gaze + actions | 仍常用于 gaze / action 任务 |
| [BEOID](https://data.bris.ac.uk/data/dataset/o4hx7jnmfqt01lyzf2n4rchg6) | Open | object interaction corpus | egocentric object interaction | 仍适合小规模 HOI 实验 |

### 9.1 为什么保留这些旧数据

- 小规模、轻量、容易跑通
- 对一些任务仍然是快速 baseline 的好入口
- 很多早期 egocentric 方法仍然默认会和这些数据作横向比较

---

## 10. 尚未形成“稳定开放下载”的项目

下面这些项目**有公开页面、论文或 release 信号**，但截至 **2026-04-15** 我不建议把它们和上面的稳定开放目录完全等价：

| 项目 | 当前状态 | 原因 |
|------|----------|------|
| [EgoExplore](https://zeroframe.ai/egoexplore) | Emerging | 有公开页面，但公开下载和研究复现生态仍不成熟 |
| [EgoVerse](https://egoverse.ai/) | Emerging | 官方页面显示是持续扩张的“living dataset”，但公开 release 细节还在完善 |
| [Ego-Deliver](https://egodeliver.github.io/EgoDeliver_Dataset/) | Partial | 页面写明 full dataset 将在论文接收后释放，当前更像 demo release |
| 商业数据平台（如 `EgoData`, `NLabel`） | Not Open | 提供 egocentric data 服务，但不是开放研究数据集 |

---

## 11. 怎么从这份目录里选数据

### 11.1 如果你要“最成熟、最容易对标”

- `Ego4D`
- `EPIC-KITCHENS-100`
- `Ego-Exo4D`
- `HOT3D`
- `Assembly101`
- `Project Aria family`

### 11.2 如果你要“更像下一代 embodied data”

- `Xperience-10M`
- `Egocentric-10K`
- `EgoLife`
- `Nymeria`
- `HoloAssist`
- `OpenEgo`

### 11.3 如果你要“低成本先跑通”

- `EgoHands`
- `GTEA Gaze / EGTEA Gaze+`
- `TREK-150`
- `BEOID`
- `VEDI`
- `EgoK360`

---

## 12. 这份目录反映出的几个趋势

1. **公开视频仍以视频 benchmark 为主**  
   `Ego4D / EPIC-KITCHENS / Charades-Ego` 这类数据的社区生态仍然最成熟。

2. **2024 之后的重点明显转向 embodied multimodality**  
   `HoloAssist / Nymeria / Egocentric-10K / Xperience-10M / EgoLife` 已经不满足于只给视频标签，而是开始打包 gaze、IMU、depth、pose、captions、SLAM。

3. **手-物体交互已经形成独立赛道**  
   `HOT3D / HOI4D / ARCTIC / H2O / EgoPressure` 这类数据和通用 action recognition 数据的需求完全不同。

4. **很多“开放”其实是 research-gated，而不是完全自由下载**  
   特别是 `Aria family / Ego4D family / Xperience-10M / Egocentric-10K / EgoBody`，公开不等于无门槛。

5. **场景化第一人称数据越来越重要**  
   工业、导览、阅读、儿童视角、对话协作，这些场景正在从“小众案例”变成独立研究方向。

---

## 13. 建议的后续维护方式

如果继续维护这个仓库，建议按下面的方式演进：

1. 把这份目录当成 **dataset registry**
2. 每个重点数据集再拆成独立子目录或独立笔记
3. 优先补：
   - `Ego4D` 最小下载和目录说明
   - `HoloAssist` / `Egocentric-10K` / `EgoLife` 的访问笔记
   - `task -> dataset -> access cost -> infra cost` 决策表

*最后更新：2026-04-15*

---

## 14. 第二轮补充：额外发现的开源 / 可获取 ego 数据

这一轮继续往外扩之后，又找到了一批**确实存在公开入口、项目页、论文附带下载，或机构页面明确说明可获取**的 egocentric 数据。它们里有些是经典小集，有些是儿童视角和辅助技术方向的数据，之前没有放进主表。

### 14.1 早期日常活动 / 社交 / 长时无控场景

| 数据集 | Access | 粗略规模 | 核心模态 | 备注 |
|--------|--------|----------|----------|------|
| [GeorgiaTech Egocentric Activities (GTEA)](https://ai.stanford.edu/~alireza/GTEA/) | Open | 7 类日常活动，4 subjects | head-mounted video, labels, masks | 最早一批经典厨房/桌面活动数据，官方页仍可下载 |
| [First-Person Social Interactions Dataset](https://ai.stanford.edu/~alireza/Disney/) | Open | 8 subjects 的 day-long Disney 场景视频 | day-long ego video, social interaction annotations | 经典社交第一视角数据，官方页仍可下载 |
| [UT Egocentric (UTE)](https://vision.cs.utexas.edu/projects/egocentric/download_register.html) | Open | 4 段 3-5h 长视频，约 1.4GB | head-mounted long-form video | 早期长时第一人称视频基线，下载页仍可访问 |
| [You2Me](https://vision.cs.utexas.edu/projects/you2me/) | Open / Project release | Kinect + CMU Panoptic 两种采集 | chest-mounted ego video, ego/interactee 3D skeletons | 更偏 egocentric body pose / dyadic interaction |

### 14.2 儿童 / 婴幼儿 / developmental egocentric data

| 数据集 | Access | 粗略规模 | 核心模态 | 备注 |
|--------|--------|----------|----------|------|
| [ChildLens](https://www.eva.mpg.de/comparative-cultural-psychology/technical-development/childlens/) | Register / Gated | 108.58h，62 children | child-worn ego video, audio, activity and location labels | Max Planck 页面明确写了 DOI 和联系 access |
| [SAYCam](https://osf.io/t4eaf/) | Open | ~500h，3 infants | infant ego audio-video | 长期儿童视角核心数据 |
| [BEV1 Dataset](https://inc.ucsd.edu/mplab/125/) | Open | 34MB / 44MB / 177MB 三个版本 | baby-eye-view images + labels | UCSD 历史页面仍提供免费下载，用于 infant/robot early vision |
| [BabyView](https://babyview-project.github.io/babyview/) | Project-linked / Emerging | 论文描述 493h | child egocentric video, gyro/accelerometer, speech / pose eval labels | 项目页和论文都公开，但官方页更偏 project release 而不是传统 zip 下载 |

### 14.3 Gaze / object-centric / assistive / robot command

| 数据集 | Access | 粗略规模 | 核心模态 | 备注 |
|--------|--------|----------|----------|------|
| [EgoMon Gaze & Video Dataset](https://imatge-upc.github.io/egocentric-2016-saliency/) | Open | 7 段约 30 分钟视频，13K+ images | ego video + gaze | 小型 gaze / saliency 数据，官方页有下载 |
| [TEgO: Teachable Egocentric Objects Dataset](https://iamlabumd.github.io/tego/) | Open | 19 objects，2 users | egocentric object images | 官方页明确可下载，且写明 `CC BY 4.0` |
| [EgoNRG](https://utnuclearroboticspublic.github.io/egonrg-website/) | Open / Project-linked | 3,044 videos，160,639 annotated frames | four-view head-mounted gesture video, segmentation labels | 面向机器人导航手势，官方页挂了 dataset 链接 |

### 14.4 这一轮新增数据的意义

这批数据说明，除了 `Ego4D / Aria / HOT3D / Xperience-10M` 这种“大集”，还有几条很有价值但容易被漏掉的支线：

- **早期但仍可用的经典小集**：`GTEA`, `UTE`, `First-Person Social Interactions`
- **儿童与发展心理方向**：`ChildLens`, `SAYCam`, `BEV1`, `BabyView`
- **辅助技术 / teachable interfaces**：`TEgO`
- **机器人手势与人机交互**：`EgoNRG`

如果目标不是“最大规模预训练”，而是更垂直的行为、注意力、儿童视角、辅助交互问题，这些数据经常比大而全的数据更合适。

*第二轮补充更新：2026-04-15*

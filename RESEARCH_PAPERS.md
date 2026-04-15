# Egocentric / First-Person 数据集研究论文汇总

汇集使用 **egocentric / first-person** 数据集的代表性论文、基准与工具链。当前仍以 `Project Aria` 生态为主干，但已经扩展到 `Ego4D / Ego-Exo4D / Xperience-10M`。

---

## 目录

- [1. Project Aria 家族数据集](#1-project-aria-家族数据集)
- [2. Ego4D 与 Ego-Exo4D](#2-ego4d-与-ego-exo4d)
- [3. Project Aria 设备与更广义第一人称应用](#3-project-aria-设备与更广义第一人称应用)
- [4. Xperience-10M 发布状态](#4-xperience-10m-发布状态)
- [5. 跨数据集框架与挑战赛](#5-跨数据集框架与挑战赛)
- [6. 总结：数据集 x 任务矩阵](#6-总结数据集-x-任务矩阵)

---

## 1. Project Aria 家族数据集

### 1.1 Aria Digital Twin (ADT)

#### DeGauss：基于高斯溅射的动态-静态分解无干扰 3D 重建
- **作者**：Wang, Lohmeyer, Meboldt, Tang
- **会议**：ICCV 2025
- **任务**：3D 场景重建（动态/静态分解）
- **ADT 用法**：在 ADT 序列上评估含动态物体的第一人称场景重建
- **链接**：[论文](https://arxiv.org/abs/2503.13176) | [代码](https://github.com/BatFaceWayne/DeGauss)

#### EFM3D：面向 3D 第一人称基础模型的基准测试
- **作者**：Straub 等
- **会议**：ECCV 2024
- **任务**：3D 物体检测、表面回归
- **ADT 用法**：训练和评估基线模型，使用深度、分割、3D box 监督
- **链接**：[论文](https://arxiv.org/abs/2406.10224) | [代码](https://github.com/facebookresearch/efm3d)

#### Aria-NeRF：多模态第一人称视角合成
- **作者**：Sun, Qiu, Zheng 等
- **会议**：arXiv 2023
- **任务**：第一人称 NeRF / 视角合成
- **ADT 用法**：利用 Aria 传感器与多模态信号进行神经渲染
- **链接**：[论文](https://arxiv.org/abs/2311.06455) | [代码](https://github.com/Jiankai-Sun/Aria-NeRF)

### 1.2 Aria Everyday Activities (AEA)

#### OmniGS：基于全向高斯溅射的快速辐射场重建
- **作者**：Li, Huang, Cheng, Yeung
- **会议**：WACV 2025
- **任务**：辐射场重建
- **AEA 用法**：在第一人称场景中评估高质量重建
- **链接**：[论文](https://arxiv.org/abs/2404.03202)

#### AEA 官方论文
- **作者**：Lv 等
- **会议**：arXiv 2024
- **任务**：数据集 / 示例任务
- **AEA 用法**：展示神经场景重建、提示分割、共享坐标系多人记录
- **链接**：[论文](https://arxiv.org/abs/2402.13349)

#### DeGauss（同样使用 AEA）
- **任务**：长时第一人称场景重建
- **链接**：[论文](https://arxiv.org/abs/2503.13176)

### 1.3 Aria Synthetic Environments (ASE)

#### EFM3D（同样使用 ASE）
- **任务**：3D 第一人称预训练
- **ASE 用法**：提供 10 万合成场景作为大规模训练源
- **链接**：[论文](https://arxiv.org/abs/2406.10224)

#### ATEK 集成
- **任务**：大规模第一人称 3D 感知训练
- **ASE 用法**：作为 ATEK 的主要合成训练底座
- **链接**：[ATEK](https://github.com/facebookresearch/ATEK)

### 1.4 HOT3D

#### HOT3D：第一人称多视角视频中的 3D 手-物体追踪
- **作者**：Banerjee, Hampali 等
- **会议**：CVPR 2025（Highlight）
- **任务**：3D 手部追踪、6DoF 物体位姿
- **HOT3D 用法**：构建高精度手-物交互基准
- **链接**：[论文](https://arxiv.org/abs/2411.19167)

#### BOP Challenge 2024：基于模型与无模型的 6D 物体位姿估计
- **会议**：CVPRW 2025
- **任务**：6DoF 位姿估计
- **HOT3D 用法**：作为 BOP-H3 数据集之一进行基准测试
- **链接**：[论文](https://arxiv.org/abs/2504.02812) | [BOP](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/)

### 1.5 Nymeria

#### Nymeria 基线评估（官方）
- **会议**：ECCV 2024
- **任务**：身体追踪、运动合成、动作识别
- **Nymeria 用法**：评测可穿戴感知与语言到动作建模
- **链接**：[论文](https://arxiv.org/abs/2406.09905) | [代码](https://github.com/facebookresearch/nymeria_dataset)

### 1.6 Digital Twin Catalog (DTC)

#### DTC：大规模光照逼真 3D 物体数字孪生数据集
- **作者**：Dong, Chen 等
- **会议**：CVPR 2025（Highlight）
- **任务**：NVS、3D 重建、逆渲染
- **DTC 用法**：作为数字孪生创建与评估基准
- **链接**：[论文](https://arxiv.org/abs/2504.08541) | [代码](https://github.com/facebookresearch/DigitalTwinCatalog)

### 1.7 Aria Everyday Objects (AEO)

#### EFM3D（同样使用 AEO）
- **任务**：第一人称 3D 物体检测真实集评测
- **AEO 用法**：作为 sim-to-real 验证基准
- **链接**：[论文](https://arxiv.org/abs/2406.10224)

### 1.8 Reading in the Wild

#### Reading Recognition in the Wild
- **作者**：Yang 等
- **会议**：NeurIPS 2025
- **任务**：可穿戴设备阅读活动检测
- **数据集用法**：100 小时阅读/非阅读视频，配合 60Hz 眼动追踪
- **链接**：[论文](https://arxiv.org/abs/2505.24848) | [Explorer](https://explorer.projectaria.com/ritw)

#### ICDAR 2024 通过 Aria 眼镜阅读文档竞赛
- **会议**：ICDAR 2024
- **任务**：低分辨率第一人称图像的场景文字检测/识别
- **链接**：[论文](https://link.springer.com/chapter/10.1007/978-3-031-70552-6_25)

---

## 2. Ego4D 与 Ego-Exo4D

### 2.1 Ego4D

#### Ego4D: Around the World in 3,000 Hours of Egocentric Video
- **作者**：Grauman 等
- **会议**：CVPR 2022 / arXiv 2021
- **任务**：第一人称视频大规模基准
- **数据集用法**：定义 episodic memory、forecasting、NLQ、social、AV 等任务
- **链接**：[论文](https://arxiv.org/abs/2110.07058) | [官网](https://ego4d-data.org/)

### 2.2 Ego-Exo4D

#### EgoExoLearn：桥接异步第一人称与第三人称视角的数据集
- **作者**：Huang 等
- **会议**：CVPR 2024
- **任务**：跨视角动作理解、ego-exo 迁移
- **链接**：[论文](https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.pdf)

#### SEED4D：合成 Ego-Exo 动态 4D 数据生成器
- **会议**：arXiv 2024
- **任务**：面向 ego-exo 研究的合成数据生成
- **链接**：[论文](https://arxiv.org/abs/2412.00730)

#### 第三人称到第一人称动作识别迁移综述
- **会议**：arXiv 2024
- **任务**：跨视角动作识别迁移
- **链接**：[论文](https://arxiv.org/abs/2410.20621)

#### 长期动作预测挑战赛 2025（冠军方案）
- **作者**：Qiu 等
- **会议**：CVPR 2025 Workshop
- **任务**：长期动作预测
- **链接**：[论文](https://arxiv.org/abs/2506.02550) | [代码](https://github.com/CorrineQiu/Ego4D-LTA-Challenge-2025)

#### Ego-Exo4D 官方基准任务
- **任务族**：关键步骤识别、熟练度评估、Ego-Exo 关联、第一人称位姿估计、跨视角转换、动作识别
- **链接**：[基准](https://docs.ego-exo4d-data.org/challenge/)

---

## 3. Project Aria 设备与更广义第一人称应用

### 3.1 Project Aria：面向第一人称多模态 AI 研究的新工具
- **作者**：Engel 等
- **会议**：arXiv 2023
- **价值**：Aria 设备、传感器、MPS 和研究生态的基础参考
- **链接**：[论文](https://arxiv.org/abs/2308.13561)

### 3.2 EgoMimic：通过第一人称视频扩展模仿学习
- **作者**：Hoque 等
- **会议**：CoRL 2024
- **任务**：机器人模仿学习
- **Aria 用法**：用 Aria 采集第一人称视频和 3D 手部追踪数据，辅助训练双臂机器人
- **链接**：[论文](https://arxiv.org/abs/2410.24221) | [项目](https://egomimic.github.io/)

### 3.3 EgoDex：从大规模第一人称视频学习灵巧操作
- **作者**：Hoque, Huang 等
- **会议**：arXiv 2025
- **任务**：灵巧机器人操作
- **关联**：虽非 Aria 设备，但属于第一人称视频驱动机器人学习的延展路线
- **链接**：[论文](https://arxiv.org/abs/2505.11709) | [代码](https://github.com/apple/ml-egodex)

### 3.4 IndEgo：工业场景与协作工作第一人称数据集
- **作者**：Chavan 等
- **会议**：NeurIPS 2025
- **任务**：工业任务理解、错误检测、问答
- **Aria 用法**：使用 Project Aria 设备采集 197 小时工业场景数据
- **链接**：[论文](https://arxiv.org/abs/2511.19684) | [代码](https://github.com/Vivek9Chavan/IndEgo)

### 3.5 TEXT2TASTE：面向智能阅读辅助的第一人称视觉系统
- **会议**：arXiv 2024
- **任务**：阅读辅助、文字识别与上下文理解
- **Aria 用法**：以 Aria 作为第一人称常开采集设备
- **链接**：[论文](https://arxiv.org/abs/2404.09254)

### 3.6 Aria Gen 2 先导数据集 (A2PD)
- **会议**：arXiv 2025
- **任务**：下一代 Aria 多模态数据
- **链接**：[论文](https://arxiv.org/abs/2510.16134) | [数据集](https://www.projectaria.com/datasets/gen2pilot/)

---

## 4. Xperience-10M 发布状态

### 4.1 官方数据集发布
- **发布方**：Ropedia
- **发布时间**：2026-03-16
- **类型**：大规模 egocentric multimodal dataset for embodied AI
- **公开入口**：
  - [Release blog](https://ropedia.com/blog/20260316_xperience_10m)
  - [Dataset card](https://huggingface.co/datasets/ropedia-ai/xperience-10m)
  - [Sample](https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample)
  - [HOMIE-toolkit](https://github.com/Ropedia/HOMIE-toolkit)

### 4.2 当前可确认的研究状态

截至 **2026-04-15**，基于公开网页与论文检索，我没有检索到明确、公开、已发表的下游论文把 `Xperience-10M` 作为实验主数据集来做系统性评测。

现阶段更准确的表述是：

- 已有正式 dataset release
- 已有 sample 与读取 / 可视化工具
- 已有 Hugging Face 公开卡片和受控访问流程
- 公开 benchmark 与 peer-reviewed 论文生态仍在早期

### 4.3 对研究选型的意义

- 如果你在做 `world model / robotics / embodied multimodal pretraining`，它非常值得关注
- 如果你需要“论文复现 + benchmark 排名”型工作，它目前还不如 Ego4D / HOT3D / Aria family 成熟

---

## 5. 跨数据集框架与挑战赛

### 5.1 ATEK：Aria 训练与评估工具包
- **作者**：Meta FAIR
- **支持数据集**：ADT、ASE、AEA、AEO
- **功能**：将 VRS/MPS 数据转成 PyTorch 兼容格式，提供预处理与评测
- **链接**：[GitHub](https://github.com/facebookresearch/ATEK) | [文档](https://facebookresearch.github.io/projectaria_tools/docs/ATEK/about_ATEK)

### 5.2 CVPR 2025 EgoVis Workshop - Ego4D + EgoExo4D 挑战赛
- **内容**：15 项挑战，覆盖 Ego4D 与 Ego-Exo4D
- **链接**：[挑战赛](https://ego4d-data.org/docs/challenge/) | [Workshop](https://egovis.github.io/cvpr25/)

### 5.3 ECCV 2024 第一人称手部追踪挑战赛
- **数据集**：HOT3D-Clips
- **任务**：手部位姿和形状估计

### 5.4 BOP Challenge 2024
- **数据集**：HOT3D
- **任务**：6DoF 物体位姿估计
- **链接**：[挑战赛](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/)

### 5.5 ASE 挑战赛
- **数据集**：ASE
- **任务**：物体检测和场景理解
- **链接**：[挑战赛](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset/ase_challenges)

---

## 6. 总结：数据集 x 任务矩阵

| 论文 / 项目 | 使用的数据集 | 研究任务 | 会议 / 状态 |
|-------------|--------------|-----------|-------------|
| DeGauss | ADT, AEA, HOT3D | 3D 重建 | ICCV 2025 |
| EFM3D | ADT, ASE, AEO | 3D 物体检测、表面回归 | ECCV 2024 |
| Aria-NeRF | Aria / ADT | 多模态 NeRF | arXiv 2023 |
| HOT3D | HOT3D | 手-物体追踪、6DoF 位姿 | CVPR 2025 |
| Nymeria | Nymeria | 身体追踪、运动合成、动作识别 | ECCV 2024 |
| DTC | DTC | NVS、3D 重建、逆渲染 | CVPR 2025 |
| Reading in the Wild | Reading in the Wild | 阅读识别 | NeurIPS 2025 |
| Ego4D | Ego4D | 大规模第一人称理解基准 | CVPR 2022 |
| EgoExoLearn | Ego-Exo4D | 跨视角动作理解 | CVPR 2024 |
| LTA Challenge 2025 | Ego4D / Ego-Exo4D | 长期动作预测 | CVPRW 2025 |
| EgoMimic | Aria（通用） | 机器人模仿学习 | CoRL 2024 |
| IndEgo | Aria（通用） | 工业任务理解、问答 | NeurIPS 2025 |
| Xperience-10M | Xperience-10M | 数据集发布、embodied pretraining 候选 | 2026 release |

---

## 核心观察

1. `ADT / HOT3D / Nymeria` 分别代表 Aria 生态中最值得关注的 3D GT、手物交互、全身动作三个高价值方向。
2. `Ego4D` 的最大优势仍然是 benchmark 生态和公开视频规模，而不是几何结构。
3. `Ego-Exo4D` 把重点从“日常第一人称理解”推进到“技能与教学行为理解”。
4. `Xperience-10M` 的真正价值不在单个 benchmark，而在于把视频、深度、pose、mocap、IMU、caption 打成统一 experience stream。
5. 如果研究目标是近期复现和公开竞赛，优先级仍应是 `Aria family / Ego4D / HOT3D`；如果研究目标是 embodied foundation model，则应尽快关注 `Xperience-10M`。

*最后更新：2026-04-15*

# Project Aria 数据集 - 研究论文汇总

汇集**使用** Meta Project Aria 数据集的研究论文与项目，按数据集和研究任务分类整理。

---

## 目录

- [1. 使用 Aria Digital Twin (ADT) 的论文](#1-使用-aria-digital-twin-adt-的论文)
- [2. 使用 Aria Everyday Activities (AEA) 的论文](#2-使用-aria-everyday-activities-aea-的论文)
- [3. 使用 Aria Synthetic Environments (ASE) 的论文](#3-使用-aria-synthetic-environments-ase-的论文)
- [4. 使用 Ego-Exo4D 的论文](#4-使用-ego-exo4d-的论文)
- [5. 使用 HOT3D 的论文](#5-使用-hot3d-的论文)
- [6. 使用 Nymeria 的论文](#6-使用-nymeria-的论文)
- [7. 使用 Digital Twin Catalog (DTC) 的论文](#7-使用-digital-twin-catalog-dtc-的论文)
- [8. 使用 Aria Everyday Objects (AEO) 的论文](#8-使用-aria-everyday-objects-aeo-的论文)
- [9. 使用 Reading in the Wild 的论文](#9-使用-reading-in-the-wild-的论文)
- [10. 使用 Project Aria 眼镜的论文（通用）](#10-使用-project-aria-眼镜的论文通用)
- [11. 跨数据集研究与框架](#11-跨数据集研究与框架)
- [12. 竞赛与挑战赛](#12-竞赛与挑战赛)
- [13. 总结：数据集 x 任务矩阵](#13-总结数据集-x-任务矩阵)

---

## 1. 使用 Aria Digital Twin (ADT) 的论文

### 1.1 DeGauss：基于高斯溅射的动态-静态分解无干扰 3D 重建
- **作者**：Wang, Lohmeyer, Meboldt, Tang
- **会议**：ICCV 2025
- **任务**：3D 场景重建（动态/静态分解）
- **ADT 用法**：在 ADT 序列上评估含动态物体的第一人称场景重建。DeGauss 采用解耦的 3DGS 背景分支和 4DGS 前景分支。
- **核心结果**：在 ADT、AEA 和 HOT3D 基准上超越现有方法。
- **链接**：[论文](https://arxiv.org/abs/2503.13176) | [代码](https://github.com/BatFaceWayne/DeGauss)

### 1.2 EFM3D：面向 3D 第一人称基础模型的基准测试
- **作者**：Straub 等 (Meta)
- **会议**：ECCV 2024
- **任务**：3D 物体检测、表面回归
- **ADT 用法**：ADT 为基准提供训练数据；Egocentric Voxel Lifting (EVL) 基线模型在 ADT 的深度图、分割和 3D 边界框上训练。同时用于 sim-to-real 评估。
- **核心结果**：首个利用 Aria 多相机数据的 3D 第一人称基础模型基准。
- **链接**：[论文](https://arxiv.org/abs/2406.10224) | [代码](https://github.com/facebookresearch/efm3d)

### 1.3 Aria-NeRF：多模态第一人称视角合成
- **作者**：Sun, Qiu, Zheng 等 (Stanford & CUHK)
- **会议**：arXiv 2023
- **任务**：从第一人称数据进行神经辐射场重建
- **ADT 用法**：使用 Aria 传感器数据构建 NeRF 模型，在 Aria 数据上评估 Nerfacto 和 NeuralDiff。
- **核心结果**：展示了第一人称 NeRF 的挑战性；提出音频、注视、IMU 等多模态条件化 NeRF。
- **链接**：[论文](https://arxiv.org/abs/2311.06455) | [代码](https://github.com/Jiankai-Sun/Aria-NeRF)

### 1.4 HOT3D：第一人称多视角视频中的 3D 手-物体追踪
- **作者**：Banerjee, Hampali 等 (Meta)
- **会议**：CVPR 2025（Highlight）
- **任务**：3D 手部追踪、6DoF 物体位姿估计
- **ADT 用法**：利用 ADT 的 3D 物体模型和 ground truth；ADT 与 DTC 之间有 400+ 个共享扫描物体。
- **链接**：[论文](https://arxiv.org/abs/2411.19167)

---

## 2. 使用 Aria Everyday Activities (AEA) 的论文

### 2.1 DeGauss（见 1.1）
- 同样在 AEA 序列上评估，用于长时第一人称视频的无干扰 3D 重建。

### 2.2 OmniGS：基于全向高斯溅射的快速辐射场重建
- **作者**：Li, Huang, Cheng, Yeung
- **会议**：WACV 2025
- **任务**：从全向/第一人称图像进行辐射场重建
- **AEA 用法**：在第一人称场景中使用 Aria 数据评估辐射场重建。
- **核心结果**：达到最先进的重建质量和高渲染速度。
- **链接**：[论文](https://arxiv.org/abs/2404.03202)

### 2.3 神经场景重建（AEA 示范应用）
- **任务**：神经场景重建与提示分割（Prompted Segmentation）
- **AEA 用法**：AEA 论文本身展示了示范研究应用，包括利用 AEA 多人、多地点录制和共享坐标系进行神经场景重建和提示分割。
- **链接**：[论文](https://arxiv.org/abs/2402.13349)

---

## 3. 使用 Aria Synthetic Environments (ASE) 的论文

### 3.1 EFM3D（见 1.2）
- **ASE 用法**：ASE 提供大规模合成训练数据（10 万场景），用于训练 3D 第一人称基础模型。ATEK 框架将 ASE 数据转换为 PyTorch 兼容格式。
- **核心结果**：ASE 实现了前所未有的第一人称感知任务预训练规模。

### 3.2 ATEK 集成
- **任务**：大规模第一人称 3D 感知预训练
- **ASE 用法**：ASE 是 ATEK（Aria 训练与评估工具包）的主要数据源，提供 10 万场景规模的合成深度、分割和轨迹数据。
- **链接**：[ATEK](https://github.com/facebookresearch/ATEK)

---

## 4. 使用 Ego-Exo4D 的论文

### 4.1 EgoExoLearn：桥接异步第一人称与第三人称视角的数据集
- **作者**：Huang 等
- **会议**：CVPR 2024
- **任务**：跨视角动作理解、ego-exo 迁移
- **Ego-Exo4D 用法**：基于 ego-exo 范式桥接异步视角。
- **链接**：[论文](https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.pdf)

### 4.2 SEED4D：合成 Ego-Exo 动态 4D 数据生成器
- **会议**：arXiv 2024
- **任务**：面向 ego-exo 研究的合成数据生成
- **Ego-Exo4D 用法**：受 Ego-Exo4D 多视角范式启发，提出可定制的合成数据生成器。
- **链接**：[论文](https://arxiv.org/abs/2412.00730)

### 4.3 第三人称到第一人称动作识别迁移：综述
- **会议**：arXiv 2024
- **任务**：跨视角动作识别迁移
- **Ego-Exo4D 用法**：将 Ego-Exo4D 作为 ego-exo 迁移学习的关键基准进行综述。
- **链接**：[论文](https://arxiv.org/abs/2410.20621)

### 4.4 长期动作预测挑战赛 2025（冠军方案）
- **作者**：Qiu 等 (Georgia Tech)
- **会议**：CVPR 2025 Workshop (EgoVis)
- **任务**：长期动作预测
- **Ego-Exo4D 用法**：Ego4D/EgoExo4D Challenge 2025 基准的一部分。
- **链接**：[论文](https://arxiv.org/abs/2506.02550) | [代码](https://github.com/CorrineQiu/Ego4D-LTA-Challenge-2025)

### 4.5 Ego-Exo4D 官方基准任务
数据集定义了六大基准任务族：
1. **细粒度关键步骤识别** - 从裁剪的第一人称片段预测关键步骤标签（278 个关键步骤）
2. **熟练度评估** - 从 ego+exo 视频分类演示者的技能水平
3. **Ego-Exo 关联** - 第一人称（学习者）与第三人称（教师）之间的语义对应
4. **第一人称位姿估计** - 从第一人称视角估计 3D 身体/手部位姿
5. **跨视角转换** - 从第三人称生成第一人称视角（或反之）
6. **动作识别** - 跨视角的细粒度活动分类
- **链接**：[基准](https://docs.ego-exo4d-data.org/challenge/)

---

## 5. 使用 HOT3D 的论文

### 5.1 BOP Challenge 2024：基于模型与无模型的 6D 物体位姿估计
- **会议**：CVPRW 2025（CV4MR 最佳论文奖）
- **任务**：6DoF 物体位姿估计
- **HOT3D 用法**：HOT3D 是三个新的 "BOP-H3" 数据集之一。GigaPose、GigaPose+GenFlow 和 OPFormer 等方法在 HOT3D 上进行基准测试。
- **核心结果**：多视角第一人称方法显著优于单视角方法。
- **链接**：[论文](https://arxiv.org/abs/2504.02812) | [BOP](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/)

### 5.2 ECCV 2024 第一人称手部追踪挑战赛
- **会议**：ECCV 2024 Workshop
- **任务**：手部位姿与形状估计
- **HOT3D 用法**：使用 HOT3D-Clips 作为第一人称手部追踪评估基准，配合专业光学动捕 ground truth。

### 5.3 DeGauss（见 1.1）
- 同样在 HOT3D 序列上评估 3D 重建。

---

## 6. 使用 Nymeria 的论文

### 6.1 Nymeria 基线评估（官方）
- **会议**：ECCV 2024
- **任务**：第一人称身体追踪、运动合成、动作识别
- **Nymeria 用法**：论文评估了多个最先进算法：
  - **第一人称身体追踪**：从头戴设备 + 腕带 IMU/视觉信号估计全身位姿
  - **运动合成**：基于语言描述生成合理的身体运动
  - **动作识别**：从第一人称信号分类活动
- **核心结果**：定义了具有挑战性的基准；现有方法在真实场景数据上仍有很大提升空间。
- **链接**：[论文](https://arxiv.org/abs/2406.09905) | [代码](https://github.com/facebookresearch/nymeria_dataset)

---

## 7. 使用 Digital Twin Catalog (DTC) 的论文

### 7.1 DTC：大规模光照逼真 3D 物体数字孪生数据集
- **作者**：Dong, Chen 等 (Meta)
- **会议**：CVPR 2025（Highlight）
- **任务**：新视角合成、3D 形状重建、可重光照外观重建、逆渲染
- **DTC 用法**：2,000 个亚毫米精度 3D 扫描 + 多条件图像序列，提供首个全面的数字孪生创建方法评估基准。
- **核心结果**：首个 3D 数字孪生生成的真实世界评估基准。
- **链接**：[论文](https://arxiv.org/abs/2504.08541) | [代码](https://github.com/facebookresearch/DigitalTwinCatalog)

---

## 8. 使用 Aria Everyday Objects (AEO) 的论文

### 8.1 EFM3D（见 1.2）
- **AEO 用法**：AEO 的 25 个序列、1,037 个 3D OBB 标注（覆盖 17 个物体类别）作为**真实世界评估**基准。在合成数据（ASE）或半合成数据（ADT）上训练的模型在 AEO 上进行验证。
- **核心结果**：验证了 3D 第一人称物体检测的 sim-to-real 迁移效果。

---

## 9. 使用 Reading in the Wild 的论文

### 9.1 Reading Recognition in the Wild（官方）
- **作者**：Yang 等 (Meta)
- **会议**：NeurIPS 2025
- **任务**：可穿戴设备阅读活动检测
- **数据集用法**：100 小时阅读/非阅读视频，配合 60Hz 眼动追踪。定义"阅读识别"为新研究任务。包含 hard negatives（文本可见但未被阅读）。
- **核心结果**：首个具有 60Hz 眼动追踪的大规模阅读识别基准。
- **链接**：[论文](https://arxiv.org/abs/2505.24848) | [Explorer](https://explorer.projectaria.com/ritw)

### 9.2 ICDAR 2024 通过 Aria 眼镜阅读文档竞赛
- **会议**：ICDAR 2024
- **任务**：低分辨率第一人称图像的场景文字检测/识别
- **数据集用法**：使用 Aria 眼镜采集的 RDAG-1.0 数据集。三个任务：低分辨率孤立单词识别、阅读顺序预测、页面级识别。
- **核心结果**：展示了常开、低分辨率、第一人称文字识别的独特挑战。
- **链接**：[论文](https://link.springer.com/chapter/10.1007/978-3-031-70552-6_25)

### 9.3 使用 Aria 眼镜在复杂环境条件下的场景文字检测与识别
- **会议**：arXiv 2025
- **任务**：不同光照/距离/分辨率下的场景文字检测与识别
- **数据集用法**：使用 Aria 眼镜采集的自定义数据集。评估 EAST+CRNN 和 EAST+PyTesseract 流水线。集成眼动追踪实现注意力感知处理。
- **核心结果**：图像超分辨率将 CER 从 0.65 降至 0.48；注视追踪优化了处理效率。
- **链接**：[论文](https://arxiv.org/abs/2507.16330)

---

## 10. 使用 Project Aria 眼镜的论文（通用）

### 10.1 EgoMimic：通过第一人称视频扩展模仿学习
- **作者**：Hoque 等 (Georgia Tech)
- **会议**：CoRL 2024
- **任务**：从第一人称人类演示进行机器人模仿学习
- **Aria 用法**：Aria 眼镜采集第一人称视频 + 3D 手部追踪数据。90 分钟的 Aria 录制通过跨域联合训练来训练双臂机器人操作器。
- **核心结果**：相比纯机器人数据，任务性能提升 400%；1 小时人手数据 > 1 小时机器人数据。
- **链接**：[论文](https://arxiv.org/abs/2410.24221) | [项目](https://egomimic.github.io/)

### 10.2 EgoDex：从大规模第一人称视频学习灵巧操作
- **作者**：Hoque, Huang 等 (Apple)
- **会议**：arXiv 2025
- **任务**：从第一人称视频进行灵巧机器人操作
- **Aria 关联**：虽然 EgoDex 使用 Apple Vision Pro（非 Aria），但延续了 EgoMimic 用 Aria 开创的范式，验证了第一人称视频作为可扩展机器人学习数据源的可行性。
- **链接**：[论文](https://arxiv.org/abs/2505.11709) | [代码](https://github.com/apple/ml-egodex)

### 10.3 IndEgo：面向第一人称工业助手的工业场景与协作工作数据集
- **作者**：Chavan 等 (Fraunhofer IPK)
- **会议**：NeurIPS 2025（数据集与基准赛道）
- **任务**：工业任务理解、错误检测、问答
- **Aria 用法**：使用 Meta Project Aria 设备以 2880x2880 @ 10 FPS 采集 3,460 个第一人称录制（约 197 小时）。包含眼动追踪、手部位姿、MPS 半稠密点云。
- **核心结果**：首个包含协作工作、错误标注和推理型问答的工业第一人称数据集。
- **链接**：[论文](https://arxiv.org/abs/2511.19684) | [代码](https://github.com/Vivek9Chavan/IndEgo) | [HuggingFace](https://huggingface.co/datasets/FraunhoferIPK/IndEgo)

### 10.4 HD-EPIC：高细节第一人称视频数据集
- **作者**：Perrett 等 (Bristol, Bath)
- **会议**：CVPR 2025
- **任务**：细粒度动作识别、食谱理解、音频事件检测
- **Aria 关联**：虽然 HD-EPIC 使用自有采集设备，但遵循第一人称范式，在第一人称视觉社区（EgoVis Workshop）中与 Aria 数据集一同进行基准测试。
- **核心结果**：41 小时、440 万帧、59,400 个动作，带数字孪生定位。
- **链接**：[论文](https://arxiv.org/abs/2502.04144) | [项目](https://hd-epic.github.io/)

### 10.5 TEXT2TASTE：面向智能阅读辅助的第一人称视觉系统
- **会议**：arXiv 2024
- **任务**：使用第一人称视觉 + LLM 的阅读辅助
- **Aria 用法**：使用 Aria 眼镜作为第一人称采集设备进行文字识别和上下文理解。
- **链接**：[论文](https://arxiv.org/abs/2404.09254)

---

## 11. 跨数据集研究与框架

### 11.1 ATEK：Aria 训练与评估工具包
- **作者**：Meta FAIR
- **任务**：面向 Aria 数据的端到端深度学习框架
- **支持数据集**：ADT、ASE、AEA、AEO（可扩展）
- **功能**：将 VRS/MPS 数据转换为 PyTorch 兼容格式；提供预处理数据集、标准化评估工具和数据仓库。
- **链接**：[GitHub](https://github.com/facebookresearch/ATEK) | [文档](https://facebookresearch.github.io/projectaria_tools/docs/ATEK/about_ATEK)

### 11.2 Project Aria：面向第一人称多模态 AI 研究的新工具
- **作者**：Engel 等 (Meta)
- **会议**：arXiv 2023
- **简介**：描述 Aria 眼镜平台、传感器规格、MPS 流水线和研究生态系统的基础性论文。
- **链接**：[论文](https://arxiv.org/abs/2308.13561)

### 11.3 Aria Gen 2 先导数据集 (A2PD)
- **作者**：Meta Reality Labs
- **会议**：arXiv 2025
- **简介**：使用下一代 Aria Gen 2 眼镜采集的新数据集，配备 4 个 CV 相机（Gen 1 为 2 个）、增强 RGB 分辨率、PPG 传感器和亚毫秒时间对齐的 Sub-GHz 射频。
- **场景**：清洁、烹饪、进食、游戏、户外行走
- **链接**：[论文](https://arxiv.org/abs/2510.16134) | [数据集](https://www.projectaria.com/datasets/gen2pilot/)

### 11.4 第一人称视觉的未来展望
- **会议**：IJCV 2024
- **任务**：综述/展望论文
- **Aria 用法**：将 Project Aria 数据集作为第一人称 AI 研究未来的关键基础设施进行讨论。
- **链接**：[论文](https://link.springer.com/article/10.1007/s11263-024-02095-7)

---

## 12. 竞赛与挑战赛

### 12.1 CVPR 2025 EgoVis Workshop - Ego4D + EgoExo4D 挑战赛
- **共 15 项挑战**（9 项 Ego4D + 6 项 EgoExo4D）
- EgoExo4D 任务：关键步骤识别、熟练度评估、Ego-Exo 迁移、第一人称位姿、视角转换等
- 2025 年 3 月 5 日启动；排行榜 5 月 19 日关闭
- **链接**：[挑战赛](https://ego4d-data.org/docs/challenge/) | [Workshop](https://egovis.github.io/cvpr25/)

### 12.2 BOP Challenge 2024 (ECCV 2024)
- 使用 HOT3D 作为三个新基准数据集之一（BOP-H3）
- 任务：基于模型与无模型的 6DoF 物体位姿估计
- **CV4MR Workshop 最佳论文奖**，CVPR 2025
- **链接**：[挑战赛](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/) | [报告](https://arxiv.org/abs/2504.02812)

### 12.3 ECCV 2024 第一人称手部追踪挑战赛
- 使用 HOT3D-Clips 进行手部位姿和形状估计
- 双设备评估（Aria + Quest 3）

### 12.4 ICDAR 2024 - 通过 Aria 眼镜阅读文档
- 三项任务：单词识别、阅读顺序预测、页面级识别
- 使用 Aria 眼镜采集的 RDAG-1.0 数据集
- **链接**：[竞赛](https://link.springer.com/chapter/10.1007/978-3-031-70552-6_25)

### 12.5 ASE 挑战赛
- 使用 10 万合成场景的物体检测和场景理解挑战
- **链接**：[挑战赛](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset/ase_challenges)

---

## 13. 总结：数据集 x 任务矩阵

| 论文/项目 | 使用的数据集 | 研究任务 | 会议 |
|---|---|---|---|
| **DeGauss** | ADT, AEA, HOT3D | 3D 重建（高斯溅射） | ICCV 2025 |
| **EFM3D** | ADT, ASE, AEO | 3D 物体检测、表面回归 | ECCV 2024 |
| **Aria-NeRF** | Aria（通用） | 多模态 NeRF 视角合成 | arXiv 2023 |
| **HOT3D** | HOT3D (Aria+Quest3) | 手-物体追踪、6DoF 位姿 | CVPR 2025 |
| **BOP Challenge 2024** | HOT3D | 6DoF 物体位姿估计 | CVPRW 2025 |
| **EgoMimic** | Aria（通用） | 机器人模仿学习 | CoRL 2024 |
| **EgoDex** | Vision Pro（Aria 范式） | 灵巧机器人操作 | arXiv 2025 |
| **IndEgo** | Aria（通用） | 工业任务理解、问答 | NeurIPS 2025 |
| **Nymeria** | Nymeria | 身体追踪、运动合成、动作识别 | ECCV 2024 |
| **DTC** | DTC | 新视角合成、3D 重建 | CVPR 2025 |
| **Reading in the Wild** | Reading in the Wild | 阅读活动检测 | NeurIPS 2025 |
| **ICDAR RDAG** | Aria（通用） | 场景文字识别 | ICDAR 2024 |
| **Scene Text w/ Aria** | Aria（通用） | 复杂条件下的文字检测 | arXiv 2025 |
| **TEXT2TASTE** | Aria（通用） | LLM 辅助阅读 | arXiv 2024 |
| **EgoExoLearn** | Ego-Exo4D | 跨视角动作理解 | CVPR 2024 |
| **SEED4D** | Ego-Exo4D（启发） | 合成 ego-exo 数据生成 | arXiv 2024 |
| **Ego-Exo 迁移综述** | Ego-Exo4D | 跨视角动作识别综述 | arXiv 2024 |
| **LTA Challenge 2025** | Ego4D/EgoExo4D | 长期动作预测 | CVPRW 2025 |
| **OmniGS** | AEA（第一人称） | 全向高斯溅射 | WACV 2025 |
| **HD-EPIC** | 第一人称（相关） | 细粒度动作识别 | CVPR 2025 |
| **A2PD** | Aria Gen 2 | 下一代第一人称多模态数据 | arXiv 2025 |
| **ATEK** | ADT, ASE, AEA, AEO | 深度学习训练/评估框架 | Meta 2024 |

---

## 核心观察

1. **引用最多的数据集**：Aria Digital Twin (ADT) 是下游研究中使用最广泛的 Aria 数据集，得益于其丰富的 ground truth（深度、分割、3D 位姿、合成渲染）。

2. **新兴应用方向**：**从第一人称视频进行机器人学习**（EgoMimic、EgoDex）是快速增长的领域，利用 Aria 的手部追踪 + 第一人称视频来训练机器人操作策略。

3. **3D 重建主导**：大量论文聚焦于 3D 场景重建（DeGauss、Aria-NeRF、OmniGS、EFM3D），充分利用 Aria 的多相机配置和 MPS 输出。

4. **跨视角学习**：Ego-Exo4D 催生了 ego-exo 迁移、跨视角对应和多视角技能评估等新研究方向。

5. **工业应用**：IndEgo 展示了 Aria 在消费/研究场景之外的实用价值，延伸至制造业和协作工业工作。

6. **文字理解**：多篇论文（ICDAR RDAG、Reading in the Wild、TEXT2TASTE）探索了常开、低分辨率第一人称设备上文字识别的独特挑战。

7. **规模趋势**：ASE（10 万场景、23TB）实现了大规模预训练，而 ATEK 和 A2PD 等新工具致力于使 Aria 数据更便于深度学习工作流使用。

8. **竞赛生态**：CVPR、ECCV、ICDAR 和 BOP 上的活跃挑战赛项目确保了研究社区的持续基准测试进展。

---

*最后更新：2026-03-30*

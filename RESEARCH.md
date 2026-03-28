# Meta Project Aria - 开源数据集调研报告

## 1. Project Aria 概述

Project Aria 是 Meta Reality Labs 的 AR 研究项目，基于轻量级 AR 眼镜采集第一人称（egocentric）多模态数据。

### 传感器配置（Aria Gen 1）

| 传感器 | 数量 | 规格 |
|--------|------|------|
| RGB 相机 | 1 | 1408x1408, 110 deg FOV, 1/10/15/30 FPS |
| 单目 SLAM 相机 | 2 | 640x480, 150 deg FOV, 10/15/30 FPS |
| 眼动追踪相机 (ET) | 2 | 320x240, 80 deg FOV, 10/30/60 FPS |
| IMU | 2 | 1kHz + 800Hz |
| 磁力计 | 1 | |
| 气压计 | 1 | |
| 麦克风 | 7 | 48kHz 空间音频 |
| Wi-Fi Beacon | 1 | |
| Bluetooth Beacon | 1 | |

### 核心链接

- 官网: https://www.projectaria.com/
- GitHub: https://github.com/facebookresearch/projectaria_tools
- 文档: https://facebookresearch.github.io/projectaria_tools/
- PyPI: https://pypi.org/project/projectaria-tools/
- Dataset Explorer: https://explorer.projectaria.com/

---

## 2. 数据格式

### 2.1 VRS (Video Recording System)

Meta 自定义的二进制多流传感器数据容器格式。

- 将所有传感器流（相机、IMU、音频等）存储在单个 `.vrs` 文件中
- 每个传感器流包含时间排序的记录（Configuration + Data records）
- 支持按时间戳高效随机访问
- 支持多种编解码器（JPEG、PNG、RAW 等）

**Python 读取方式**：
```python
from projectaria_tools.core import data_provider
provider = data_provider.create_vrs_data_provider("recording.vrs")
# 获取图像
image_data = provider.get_image_data_by_index(stream_id, frame_index)
# 获取 IMU
imu_data = provider.get_imu_data_by_index(stream_id, sample_index)
```

### 2.2 MPS (Machine Perception Services) 输出

MPS 是 Meta 提供的云端感知处理服务，对 VRS 原始数据进行处理后输出：

| 输出类型 | 格式 | 说明 |
|----------|------|------|
| Closed-loop trajectory | CSV | 全局优化后的 6DoF 设备位姿（~1kHz） |
| Open-loop trajectory | CSV | 基于 VIO 的里程计位姿 |
| Semi-dense point cloud | CSV.gz | 场景 3D 点云 |
| Online calibration | JSONL | 实时更新的相机/IMU 标定 |
| Eye gaze | CSV | 3D 注视方向向量 + 深度 |
| Hand tracking | CSV | 手腕/手掌位姿 |

**Python 读取方式**：
```python
from projectaria_tools.core.mps import (
    read_closed_loop_trajectory,
    read_open_loop_trajectory,
    read_eyegaze,
    read_global_point_cloud,
)
trajectory = read_closed_loop_trajectory("closed_loop_trajectory.csv")
point_cloud = read_global_point_cloud("global_points.csv.gz")
```

### 2.3 Ground Truth 标注格式

| 格式 | 用途 |
|------|------|
| CSV | 2D/3D bounding box、轨迹、眼动 |
| JSON | 实例元数据、场景描述、标定 |
| PNG (16-bit) | 深度图（mm）、实例分割（ID） |
| VRS | 深度图流、分割图流 |
| PLY | 3D 点云 |
| GLB | 3D 物体模型（带 PBR 材质） |

---

## 3. 各数据集详细介绍

---

### 3.1 Aria Digital Twin (ADT)

**论文**: Pan et al., ICCV 2023. [arXiv:2306.06362](https://arxiv.org/abs/2306.06362)
**下载**: https://www.projectaria.com/datasets/adt/
**HuggingFace**: https://huggingface.co/datasets/projectaria/aria-digital-twin

#### 概述
在真实室内环境中（公寓 + 办公室），使用动作捕捉系统生成高精度 ground truth 的第一人称数据集。同时提供真实传感器数据和对应的光照逼真合成渲染。

#### 规模
- 236 个 sequences（单人 + 双人活动）
- 公寓场景: 284 sequences, 281 个唯一物体（324 实例）
- 办公室场景: 52 sequences, 15 个唯一物体（20 实例）
- 74 个动态物体实例跨场景共享
- 总大小: **~3.5 TB**（不含 MPS）

#### 活动类型
房间装饰、备餐、办公、物体检查、房间清洁、聚会、餐桌清理

#### 每个 Sequence 包含的文件

```
<sequence>/
  video.vrs                    # 原始传感器数据（SLAM+RGB 相机、IMU）
  synthetic_video.vrs          # 光照逼真合成渲染
  metadata.json                # 序列元数据
  aria_trajectory.csv          # 6DoF 设备轨迹
  2d_bounding_box.csv          # RGB/SLAM 相机的 2D 边界框
  3d_bounding_box.csv          # 3D 轴对齐边界框
  scene_objects.csv            # 物体 6DoF 位姿随时间变化
  eyegaze.csv                  # 眼动向量 + 深度
  instances.json               # 物体/骨骼实例元数据
  depth_images.vrs             # 3 个流的逐像素深度图（mm）
  segmentations.vrs            # 3 个流的逐像素实例分割
  Skeleton_*.json              # 人体骨骼数据
  MPS/
    eye_gaze/                  # MPS 眼动输出
    slam/                      # MPS SLAM 输出（轨迹、点云、标定）
```

#### Ground Truth（动作捕捉系统生成，非 SLAM 估计）
- 连续 6DoF 设备位姿
- 6DoF 物体位姿随时间变化
- 3D 眼动向量
- 3D 人体骨骼姿态（关节坐标 + marker 位置）
- 逐像素实例分割
- 逐像素深度图
- 2D/3D 边界框 + 可见度
- 高质量 `.glb` 3D 物体模型
- 光照逼真合成渲染

#### 研究用途
- 3D 物体检测 / 分割
- 6DoF 物体位姿估计与追踪
- 场景重建 / 深度估计
- 眼动预测
- 人体姿态估计
- Sim-to-real 迁移（利用合成渲染）

---

### 3.2 Aria Everyday Activities (AEA)

**论文**: Lv et al., arXiv 2024. [arXiv:2402.13349](https://arxiv.org/abs/2402.13349)
**下载**: https://www.projectaria.com/datasets/aea/
**License**: CC BY 4.0（相对宽松）

#### 概述
多人在 5 个不同地理位置的室内环境中进行日常活动的第一人称多模态录制。部分 sequences 包含 2 人同时佩戴 Aria 在同一空间中活动，共享全局坐标系。

#### 规模
- 143 个 sequences（53 个为双人同时录制）
- 5 个物理位置，共享坐标系
- 100 万+ 图像
- 7.3-7.5 小时累计录制
- 总大小: **~353 GB**

#### 每个 Sequence 包含的文件

```
<sequence>/
  recording.vrs                # 原始传感器数据
  metadata.json
  speech.csv                   # 时间对齐的语音转文字
  MPS/
    eye_gaze/general_eye_gaze.csv
    slam/
      closed_loop_trajectory.csv
      open_loop_trajectory.csv
      online_calibration.csv
      semidense_points.csv.gz
      semidense_observations.csv.gz
      summary.json
```

#### 标注
- 全局对齐的 6DoF 高频轨迹
- 半稠密场景点云
- 逐帧 3D 眼动向量
- **时间对齐的语音转文字**（稀有标注类型）
- 在线相机/IMU 标定
- 多用户数据使用共享全局坐标系

#### 研究用途
- 神经场景重建
- 分割提示（Prompted Segmentation）
- 持续第一人称视觉
- 活动识别 / 动作预测
- 音视频分析
- 相机定位与建图

---

### 3.3 Aria Synthetic Environments (ASE)

**文档**: https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset
**下载**: https://www.projectaria.com/datasets/ase/

#### 概述
大规模程序化生成的合成室内场景数据集。每个场景由多个房间组成（最多 5 个曼哈顿对齐房间），使用 ~8,000 个不同 3D 物体填充。设备轨迹模拟真实行走路径，传感器模拟复现 Aria 眼镜的相机和镜头特性。

#### 规模
- **100,000** 个独特多房间室内场景
- 5,800 万+ 图像
- ~8,000 个不同 3D 物体
- 67 天的模拟行走轨迹 / ~7,800 km
- 总大小: **~23 TB**

#### 每个场景包含的文件

```
<sceneID>/
  rgb/                         # 合成 RGB 图像 (JPEG, 10 FPS)
    vignette0000000.jpg
    ...
  depth/                       # 16-bit PNG 深度图（mm，沿射线方向）
  instances/                   # 16-bit PNG 实例分割（像素值=物体ID）
  ase_scene_language.txt       # ASE 场景语言描述（CAD-like）
  trajectory.txt               # 6DoF GT 相机位姿 (10 FPS)
  semidense_points.csv.gz      # 半稠密点云
  semidense_observations.csv.gz
  object_instances_to_classes.json  # 实例ID->类名映射
```

#### 独特特性
- **ASE Scene Language**: 一种类 CAD 语言，描述建筑元素（门、窗、柱子）的类型、位置和尺寸
- 适合大规模预训练
- 与 ATEK 框架集成，支持端到端深度学习训练
- IMU 噪声模型反映真实 Aria 硬件特性

#### 研究用途
- 第一人称物体检测/追踪
- 场景重建
- 平面图估计
- 大规模预训练（万级场景）
- Sim-to-real 基础训练

---

### 3.4 Ego-Exo4D

**论文**: Grauman et al., arXiv 2023. [arXiv:2311.18259](https://arxiv.org/abs/2311.18259)
**官网**: https://ego-exo4d-data.org/
**下载**: 需通过 Ego-Exo4D 官网单独申请

#### 概述
同时从第一人称（Aria 眼镜）和第三人称（4-5 台固定 GoPro）视角捕捉专业技能活动。覆盖 8 个技能领域，在全球 13 个城市采集。由 Meta FAIR + 15 所大学合作完成。

#### 规模
- **1,286.3 小时**总视频（221.26 小时 ego 视角）
- 5,035 个 takes
- 740 名佩戴者 / 800+ 参与者
- 123 个场景，13 个城市

#### 活动分布

| 领域 | Takes | 参与者 | 小时 |
|------|-------|--------|------|
| 烹饪 | 678 | 173 | 564 |
| 攀岩 | 1,401 | 98 | 94 |
| 篮球 | 910 | 113 | 78 |
| 舞蹈 | 728 | 93 | 107 |
| 音乐 | 276 | 59 | 180 |
| 健身 | 397 | 122 | 115 |
| 足球 | 282 | 78 | 67 |
| 自行车维修 | 363 | 32 | 82 |

#### 标注类型
- 3D 身体和手部姿态
- 物体分割 mask
- **关键步骤标注**（Keystep annotations）
- 步骤间的程序依赖关系
- **熟练度评分**
- 第一人称叙述（佩戴者自述）
- 第三人称播报描述
- **专家评论**（教练/老师点评技能表现）—— 新颖标注类型
- 相机位姿 + 3D 点云

#### 研究用途
- 关键步骤识别
- 熟练度评估
- 跨视角转换（ego-to-exo）
- 3D 手/身体姿态估计
- 精细活动理解 / 技能评估
- 多模态学习

---

### 3.5 HOT3D

**论文**: Hampali et al., CVPR 2025. [arXiv:2411.19167](https://arxiv.org/abs/2411.19167)
**另见**: [arXiv:2406.09598](https://arxiv.org/abs/2406.09598)
**下载**: https://www.projectaria.com/datasets/hot3D/ + GitHub 专用下载器

#### 概述
第一人称 3D 手-物体追踪基准数据集。由两种头戴设备同时录制——Project Aria（AR 眼镜原型）和 Quest 3（VR 头显）。19 名参与者与 33 个刚性物体交互，GT 由专业光学动捕系统生成。

#### 规模
- **833+ 分钟**多视角图像流
- 150 万多视角帧（370 万+ 单独图像）
- 30 FPS
- 19 名受试者，33 个物体

#### 数据格式
- 同步多视角 egocentric 视频流
- 手部标注: **UmeTrack + MANO** 两种格式
- 高保真 3D 物体模型（PBR 材质，内部扫描仪生成）
- 2D 边界框
- Eye Gaze MPS 数据（仅 Aria）
- 半稠密点云（仅 Aria）

#### 独特特性
- **双设备采集**（Aria + Quest 3），可跨设备基准测试
- 专业光学动捕系统 GT（非估计）
- 公开挑战赛: ECCV 2024 BOP Challenge + 手部追踪挑战赛

#### 研究用途
- 6DoF 物体位姿估计（model-based / model-free）
- 2D 物体检测
- 手部姿态和形状估计
- 联合手-物体追踪
- 注视引导的交互预测

---

### 3.6 Nymeria

**论文**: Ma et al., ECCV 2024. [arXiv:2406.09905](https://arxiv.org/abs/2406.09905)
**下载**: https://www.projectaria.com/datasets/nymeria/
**License**: CC BY-NC 4.0

#### 概述
**世界最大的第一人称人体运动数据集**。参与者同时佩戴：XSens MVN Link 惯性动捕服（17 个惯性传感器，240Hz 全身 GT）、Aria 眼镜、两个 miniAria 腕带。另有观察者佩戴 Aria 提供第三人称视角。所有设备亚毫秒时间同步。

#### 规模
- **300 小时**日常活动
- 3,600 小时视频数据（所有设备合计）
- 1,200 个 sequences
- 264 名参与者，50 个室内外场景
- 20 种活动场景
- 2.6 亿+ 姿态
- 400 km 行走轨迹，1,053 km 手腕运动

#### 语言标注（230 小时覆盖）

| 标注类型 | 小时 | 句子数 | 词数 |
|----------|------|--------|------|
| 运动叙述 (Narration) | 39 | 117.2K | 2.72M |
| 活动摘要 (Summary) | 196 | 22.6K | 0.45M |
| 原子动作 (Atomic Action) | 207 | 170.6K | 5.47M |
| **合计** | 230 | **310.5K** | **8.64M** |

词汇量: 6,545 个术语

#### 数据内容
- Aria 眼镜: RGB + 2 SLAM + 2 ET + 2 IMU + 磁力计 + 气压计 + 音频
- miniAria 腕带: 类似传感器，腕部视角
- XSens 动捕: 240Hz 全身运动学，重定向到参数化人体模型（Meta Momentum）
- MPS: 6DoF 轨迹、半稠密点云、带深度的眼动

#### 独特特性
- miniAria 腕带（原型未来可穿戴设备形态）
- 分层粗到细语言标注
- 观察者视角（第三人称 Aria 录制）
- EgoBlur 隐私保护（人脸和车牌模糊）

#### 研究用途
- 第一人称身体追踪
- 运动合成/生成
- 动作识别/预测
- 语言条件化运动生成
- 可穿戴计算研究

---

### 3.7 Digital Twin Catalog (DTC)

**论文**: Dong et al., CVPR 2025 (Highlight). [arXiv:2504.08541](https://arxiv.org/abs/2504.08541)
**下载**: https://www.projectaria.com/datasets/dtc/
**GitHub**: https://github.com/facebookresearch/DigitalTwinCatalog

#### 概述
2,000 个高保真 3D 物体数字孪生，亚毫米级几何精度 + 光照逼真 PBR 材质。同时提供子集物体的多条件图像序列（DSLR 相机 + Aria 眼镜），带对齐的 GT 位姿和轨迹。首个全面的 3D 数字孪生创建真实世界评估基准。

#### 规模
- **2,000** 个扫描 3D 物体模型
- 200 个 Aria sequences（100 主动/360 环绕 + 100 被动/随意走过）
- 105 个 DSLR sequences（2 种光照条件）
- 2 个光照环境图/DSLR sequence

#### 数据格式
- `.glb` 3D 模型 + PBR 材质
- Aria VRS（主动/被动轨迹）
- DSLR 图像序列（3 台相机，机械臂，3 个拍摄方向）
- 设备轨迹 + 对齐物体位姿
- 光照环境图

#### 研究用途
- 新视角合成 (NVS)
- 3D 形状重建
- 可重光照外观重建
- 逆渲染
- 数字孪生生成

---

### 3.8 Aria Everyday Objects (AEO)

**论文**: Straub et al., "EFM3D," ECCV 2024. [arXiv:2406.10224](https://arxiv.org/abs/2406.10224)
**下载**: https://www.projectaria.com/datasets/aeo/

#### 概述
小型但高质量的第一人称 3D 物体检测数据集。由非计算机视觉专家在美国多地采集，确保真实、非脚本的运动模式。

#### 规模
- 25 个 sequences（~45 分钟）
- 1,037 个标注 3D 有向边界框 (OBB)
- **17 个物体类别**: Bed, Chair, Couch, Door, Floor, Lamp, Mirror, Plant, Refrigerator, Screen, Sink, Storage, Table, Wall, WallArt, WasherDryer, Window

#### 数据格式
- Aria RGB (10Hz) + 2x SLAM (10Hz) + 2x IMU
- 完整传感器标定
- MPS: 半稠密点云 + 6DoF 轨迹

#### 研究用途
- 第一人称 3D 物体检测
- Sim-to-real 验证
- 第一人称基础模型评估

---

### 3.9 Reading in the Wild

**论文**: Yang et al., NeurIPS 2025. [arXiv:2505.24848](https://arxiv.org/abs/2505.24848)
**下载**: https://www.projectaria.com/datasets/reading-in-the-wild/
**Dataset Explorer**: https://explorer.projectaria.com/ritw
**License**: CC BY-NC 4.0 + Apache 2.0

#### 概述
首个大规模可穿戴设备阅读识别多模态数据集。使用 Aria Gen 1 采集 100 小时的阅读/非阅读视频，涵盖多种真实场景。

#### 规模
- **100 小时**视频
- 1,716 个 sequences
- 111 名参与者
- 150+ 种阅读材料
- 19 个高层场景类型

#### 传感器数据
| 传感器 | 规格 |
|--------|------|
| RGB 相机 | 110 deg FOV, 30 Hz |
| 眼动追踪相机 | 80 deg FOV, **60 Hz**（首个 60Hz ET 数据集） |
| SLAM/手部相机 | 150 deg FOV, 30 Hz |
| IMU | 1kHz + 800Hz |
| 麦克风 | 7 通道, 48kHz |

#### 标注
- 阅读活动时间戳（开始/结束）
- 阅读材料分类
- 阅读模式: 专注阅读、浏览、扫描、朗读、多任务
- 3D 眼动估计 + 6DoF 轨迹

#### 独特特性
- 定义了 **"阅读识别"** 这一新研究任务
- 包含 hard negatives（文本可见但未被阅读）
- 多语言支持（Columbus 子集，4 种语言）
- 首个 60Hz 眼动追踪数据集

#### 研究用途
- 可穿戴设备阅读检测/识别
- 眼动分析
- 多模态活动识别
- 上下文 AI 助手
- 无障碍应用

---

## 4. 数据集对比总结

| 数据集 | 规模 | 大小 | 核心模态 | GT 方法 | 发表 |
|--------|------|------|----------|---------|------|
| **ADT** | 236 seq | ~3.5 TB | 真实+合成视频 | 动捕系统 | ICCV 2023 |
| **AEA** | 143 seq, 7.3h | ~353 GB | 多模态 egocentric | MPS + 语音转写 | arXiv 2024 |
| **ASE** | 100K 场景, 58M+ img | ~23 TB | 合成 RGB/深度/分割 | 程序化生成 | -- |
| **Ego-Exo4D** | 5,035 takes, 1,286h | Very Large | Ego+Exo 视频 | 多视角 + 标注 | arXiv 2023 |
| **HOT3D** | 833 min, 3.7M+ img | Medium | 多视角 egocentric | 光学动捕 | CVPR 2025 |
| **Nymeria** | 1,200 seq, 300h | Large | 全身运动 + egocentric | XSens 惯性动捕 240Hz | ECCV 2024 |
| **DTC** | 2,000 模型 + 305 seq | Medium | 3D 扫描 + 采集 | 亚毫米 3D 扫描 | CVPR 2025 |
| **AEO** | 25 seq, 45 min | Small | Egocentric 视频 | 手工 3D 标注 | ECCV 2024 |
| **Reading** | 1,716 seq, 100h | Medium | 视频 + 60Hz 眼动 | 手工标注 | NeurIPS 2025 |

---

## 5. 按研究方向推荐

| 研究方向 | 推荐数据集 |
|----------|-----------|
| 3D 物体检测/分割 | ADT, AEO |
| 6DoF 位姿估计 | ADT, HOT3D, DTC |
| 场景重建/深度估计 | ADT, AEA, ASE |
| SLAM/定位/建图 | AEA, ASE |
| 人体姿态估计 | ADT, Nymeria, Ego-Exo4D |
| 手部追踪 | HOT3D |
| 眼动分析 | AEA, Reading in the Wild |
| 活动识别 | AEA, Ego-Exo4D |
| Sim-to-real | ADT (合成), ASE |
| 运动生成/预测 | Nymeria |
| 数字孪生/逆渲染 | DTC |
| 多模态学习 | Ego-Exo4D, Nymeria |
| 阅读识别 | Reading in the Wild |
| 大规模预训练 | ASE (100K scenes) |

---

## 6. 关键文档链接

- [Open Datasets Overview](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets)
- [Dataset Download Guide](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/dataset_download)
- [VRS Data Provider](https://facebookresearch.github.io/projectaria_tools/docs/data_utilities/core_code_snippets/data_provider)
- [ADT Getting Started](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_digital_twin_dataset/adt_getting_started)
- [ADT Data Format](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_digital_twin_dataset/data_format)
- [AEA Getting Started](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_everyday_activities_dataset/aea_getting_started)
- [ASE Getting Started](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset/ase_getting_started)
- [ASE Data Format](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset/ase_data_format)
- [HOT3D Docs](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/hot3d)
- [Nymeria Docs](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/nymeria)
- [DTC Docs](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/digital_twin_catalog)
- [AEO Docs](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_everyday_objects)
- [Python Installation](https://facebookresearch.github.io/projectaria_tools/docs/data_utilities/installation/installation_python)

---

## 7. License

所有数据集均为 **非商业研究用途**。个别数据集有更宽松许可：
- AEA: CC BY 4.0
- Nymeria: CC BY-NC 4.0
- Reading in the Wild: CC BY-NC 4.0 + Apache 2.0

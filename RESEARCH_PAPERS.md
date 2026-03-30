# Project Aria Datasets - Research Papers Collection

A curated collection of research papers and projects that **use** Meta's Project Aria datasets, organized by dataset and research task.

---

## Table of Contents

- [1. Papers Using Aria Digital Twin (ADT)](#1-papers-using-aria-digital-twin-adt)
- [2. Papers Using Aria Everyday Activities (AEA)](#2-papers-using-aria-everyday-activities-aea)
- [3. Papers Using Aria Synthetic Environments (ASE)](#3-papers-using-aria-synthetic-environments-ase)
- [4. Papers Using Ego-Exo4D](#4-papers-using-ego-exo4d)
- [5. Papers Using HOT3D](#5-papers-using-hot3d)
- [6. Papers Using Nymeria](#6-papers-using-nymeria)
- [7. Papers Using Digital Twin Catalog (DTC)](#7-papers-using-digital-twin-catalog-dtc)
- [8. Papers Using Aria Everyday Objects (AEO)](#8-papers-using-aria-everyday-objects-aeo)
- [9. Papers Using Reading in the Wild](#9-papers-using-reading-in-the-wild)
- [10. Papers Using Project Aria Glasses (General)](#10-papers-using-project-aria-glasses-general)
- [11. Cross-Dataset Research & Frameworks](#11-cross-dataset-research--frameworks)
- [12. Competitions & Challenges](#12-competitions--challenges)
- [13. Summary: Dataset x Task Matrix](#13-summary-dataset-x-task-matrix)

---

## 1. Papers Using Aria Digital Twin (ADT)

### 1.1 DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction
- **Authors**: Wang, Lohmeyer, Meboldt, Tang
- **Venue**: ICCV 2025
- **Task**: 3D scene reconstruction (dynamic/static decomposition)
- **How ADT is used**: Evaluated on ADT sequences for egocentric scene reconstruction with dynamic objects. DeGauss uses decoupled 3DGS background and 4DGS foreground branches.
- **Key result**: Outperforms existing methods on ADT, AEA, and Hot3D benchmarks.
- **Links**: [Paper](https://arxiv.org/abs/2503.13176) | [Code](https://github.com/BatFaceWayne/DeGauss)

### 1.2 EFM3D: A Benchmark for Measuring Progress Towards 3D Egocentric Foundation Models
- **Authors**: Straub et al. (Meta)
- **Venue**: ECCV 2024
- **Task**: 3D object detection, surface regression
- **How ADT is used**: ADT provides training data for the benchmark; the Egocentric Voxel Lifting (EVL) baseline model is trained on ADT's depth maps, segmentation, and 3D bounding boxes. ADT also used for sim-to-real evaluation.
- **Key result**: First benchmark for 3D egocentric foundation models leveraging multi-camera Aria data.
- **Links**: [Paper](https://arxiv.org/abs/2406.10224) | [Code](https://github.com/facebookresearch/efm3d)

### 1.3 Aria-NeRF: Multimodal Egocentric View Synthesis
- **Authors**: Sun, Qiu, Zheng et al. (Stanford & CUHK)
- **Venue**: arXiv 2023
- **Task**: Neural radiance field reconstruction from egocentric data
- **How ADT is used**: Used Aria sensor data to construct a NeRF-like model from egocentric sequences, evaluating Nerfacto and NeuralDiff on Aria data.
- **Key result**: Demonstrates challenging nature of egocentric NeRF; proposes multimodal (audio, gaze, IMU) conditioned NeRF.
- **Links**: [Paper](https://arxiv.org/abs/2311.06455) | [Code](https://github.com/Jiankai-Sun/Aria-NeRF)

### 1.4 HOT3D: Hand and Object Tracking in 3D from Egocentric Multi-View Videos
- **Authors**: Banerjee, Hampali et al. (Meta)
- **Venue**: CVPR 2025 (Highlight)
- **Task**: 3D hand tracking, 6DoF object pose estimation
- **How ADT is used**: ADT's 3D object models and ground truth are leveraged; 400+ scanned objects overlap between ADT and DTC.
- **Links**: [Paper](https://arxiv.org/abs/2411.19167)

---

## 2. Papers Using Aria Everyday Activities (AEA)

### 2.1 DeGauss (see 1.1)
- Also evaluated on AEA sequences for distractor-free 3D reconstruction from long egocentric videos.

### 2.2 OmniGS: Fast Radiance Field Reconstruction using Omnidirectional Gaussian Splatting
- **Authors**: Li, Huang, Cheng, Yeung
- **Venue**: WACV 2025
- **Task**: Radiance field reconstruction from omnidirectional/egocentric images
- **How AEA is used**: Evaluated in egocentric scenarios using Aria data for radiance field reconstruction.
- **Key result**: State-of-the-art reconstruction quality and high rendering speed.
- **Links**: [Paper](https://arxiv.org/abs/2404.03202)

### 2.3 Neural Scene Reconstruction (AEA Exemplar)
- **Task**: Neural scene reconstruction and prompted segmentation
- **How AEA is used**: AEA paper itself demonstrates exemplar research applications including neural scene reconstruction and prompted segmentation using AEA's multi-person, multi-location recordings with shared coordinate systems.
- **Links**: [Paper](https://arxiv.org/abs/2402.13349)

---

## 3. Papers Using Aria Synthetic Environments (ASE)

### 3.1 EFM3D (see 1.2)
- **How ASE is used**: ASE provides large-scale synthetic training data (100K scenes) for training 3D egocentric foundation models. The ATEK framework converts ASE data into PyTorch-compatible formats for deep learning.
- **Key result**: ASE enables pre-training at unprecedented scale for egocentric perception tasks.

### 3.2 ATEK Integration
- **Task**: Large-scale pre-training for egocentric 3D perception
- **How ASE is used**: ASE is a primary data source for ATEK (Aria Training and Evaluation Kit), providing synthetic depth, segmentation, and trajectory data at 100K-scene scale.
- **Links**: [ATEK](https://github.com/facebookresearch/ATEK)

---

## 4. Papers Using Ego-Exo4D

### 4.1 EgoExoLearn: A Dataset for Bridging Asynchronous Ego- and Exo-centric View
- **Authors**: Huang et al.
- **Venue**: CVPR 2024
- **Task**: Cross-view action understanding, ego-exo transfer
- **How Ego-Exo4D is used**: Builds on the ego-exo paradigm to bridge asynchronous viewpoints.
- **Links**: [Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.pdf)

### 4.2 SEED4D: A Synthetic Ego-Exo Dynamic 4D Data Generator
- **Authors**: N/A
- **Venue**: arXiv 2024
- **Task**: Synthetic data generation for ego-exo research
- **How Ego-Exo4D is used**: Proposes a customizable synthetic data generator inspired by Ego-Exo4D's multi-view paradigm.
- **Links**: [Paper](https://arxiv.org/abs/2412.00730)

### 4.3 Exocentric To Egocentric Transfer For Action Recognition: A Survey
- **Venue**: arXiv 2024
- **Task**: Cross-view action recognition transfer
- **How Ego-Exo4D is used**: Ego-Exo4D is surveyed as a key benchmark for ego-exo transfer learning.
- **Links**: [Paper](https://arxiv.org/abs/2410.20621)

### 4.4 Long-Term Action Anticipation Challenge 2025 (Champion Solution)
- **Authors**: Qiu et al. (Georgia Tech)
- **Venue**: CVPR 2025 Workshop (EgoVis)
- **Task**: Long-term action anticipation
- **How Ego-Exo4D is used**: Part of Ego4D/EgoExo4D Challenge 2025 benchmarks.
- **Links**: [Paper](https://arxiv.org/abs/2506.02550) | [Code](https://github.com/CorrineQiu/Ego4D-LTA-Challenge-2025)

### 4.5 Ego-Exo4D Benchmark Tasks (Official)
The dataset defines six benchmark families:
1. **Fine-grained Keystep Recognition** - Predict keystep label from trimmed egocentric clip (278 keysteps)
2. **Proficiency Estimation** - Classify skill level of demonstrator from ego+exo video
3. **Ego-Exo Relation** - Semantic correspondences between ego (learner) and exo (teacher)
4. **Ego Pose Estimation** - 3D body/hand pose from egocentric view
5. **Cross-view Translation** - Generate ego view from exo (or vice versa)
6. **Action Recognition** - Fine-grained activity classification across views
- **Links**: [Benchmarks](https://docs.ego-exo4d-data.org/challenge/)

---

## 5. Papers Using HOT3D

### 5.1 BOP Challenge 2024: Model-Based and Model-Free 6D Object Pose Estimation
- **Venue**: CVPRW 2025 (Best Paper Award at CV4MR)
- **Task**: 6DoF object pose estimation
- **How HOT3D is used**: HOT3D is one of three new "BOP-H3" datasets. Methods like GigaPose, GigaPose+GenFlow, and OPFormer are benchmarked on HOT3D.
- **Key result**: Multi-view egocentric methods significantly outperform single-view counterparts.
- **Links**: [Paper](https://arxiv.org/abs/2504.02812) | [BOP](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/)

### 5.2 ECCV 2024 Egocentric Hand Tracking Challenge
- **Venue**: ECCV 2024 Workshop
- **Task**: Hand pose and shape estimation
- **How HOT3D is used**: HOT3D-Clips used as benchmark for egocentric hand tracking evaluation with professional motion-capture ground truth.

### 5.3 DeGauss (see 1.1)
- Also evaluated on HOT3D sequences for 3D reconstruction.

---

## 6. Papers Using Nymeria

### 6.1 Nymeria Baseline Evaluations (Official)
- **Venue**: ECCV 2024
- **Task**: Egocentric body tracking, motion synthesis, action recognition
- **How Nymeria is used**: The paper evaluates several state-of-the-art algorithms:
  - **Egocentric body tracking**: Estimating full-body pose from head-mounted + wristband IMU/visual signals
  - **Motion synthesis**: Generating plausible body motion conditioned on language descriptions
  - **Action recognition**: Classifying activities from egocentric signals
- **Key result**: Defines challenging benchmarks; existing methods have significant room for improvement on in-the-wild data.
- **Links**: [Paper](https://arxiv.org/abs/2406.09905) | [Code](https://github.com/facebookresearch/nymeria_dataset)

---

## 7. Papers Using Digital Twin Catalog (DTC)

### 7.1 DTC: Large-Scale Photorealistic 3D Object Digital Twin Dataset
- **Authors**: Dong, Chen et al. (Meta)
- **Venue**: CVPR 2025 (Highlight)
- **Task**: Novel view synthesis, 3D shape reconstruction, relightable appearance reconstruction, inverse rendering
- **How DTC is used**: 2,000 sub-millimeter-accurate 3D scans + multi-condition image sequences provide the first comprehensive benchmark for evaluating digital twin creation methods.
- **Key result**: First real-world evaluation benchmark for 3D digital twin generation.
- **Links**: [Paper](https://arxiv.org/abs/2504.08541) | [Code](https://github.com/facebookresearch/DigitalTwinCatalog)

---

## 8. Papers Using Aria Everyday Objects (AEO)

### 8.1 EFM3D (see 1.2)
- **How AEO is used**: AEO's 25 sequences with 1,037 3D OBB annotations across 17 object classes serve as the **real-world evaluation** benchmark. Models trained on synthetic (ASE) or semi-synthetic (ADT) data are validated against AEO.
- **Key result**: Validates sim-to-real transfer for 3D egocentric object detection.

---

## 9. Papers Using Reading in the Wild

### 9.1 Reading Recognition in the Wild (Official)
- **Authors**: Yang et al. (Meta)
- **Venue**: NeurIPS 2025
- **Task**: Reading activity detection from wearable devices
- **How the dataset is used**: 100 hours of reading/non-reading video with 60Hz eye tracking. Defines "reading recognition" as a new research task. Includes hard negatives (text visible but not being read).
- **Key result**: First large-scale reading recognition benchmark with 60Hz eye tracking.
- **Links**: [Paper](https://arxiv.org/abs/2505.24848) | [Explorer](https://explorer.projectaria.com/ritw)

### 9.2 ICDAR 2024 Competition on Reading Documents Through Aria Glasses
- **Venue**: ICDAR 2024
- **Task**: Scene text detection/recognition from low-resolution egocentric images
- **How the data is used**: The RDAG-1.0 dataset collected via Aria glasses. Three tasks: isolated word recognition in low resolution, reading order prediction, page-level recognition.
- **Key result**: Demonstrates unique challenges of always-on, low-resolution, egocentric text recognition.
- **Links**: [Paper](https://link.springer.com/chapter/10.1007/978-3-031-70552-6_25)

### 9.3 Scene Text Detection and Recognition in Challenging Environmental Conditions using Aria Glasses
- **Authors**: N/A
- **Venue**: arXiv 2025
- **Task**: Scene text detection & recognition under varying lighting/distance/resolution
- **How the data is used**: Custom dataset captured with Aria glasses. Evaluates EAST+CRNN and EAST+PyTesseract pipelines. Integrates eye-gaze tracking for attention-aware processing.
- **Key result**: Image upscaling reduces CER from 0.65 to 0.48; gaze tracking optimizes processing.
- **Links**: [Paper](https://arxiv.org/abs/2507.16330)

---

## 10. Papers Using Project Aria Glasses (General)

### 10.1 EgoMimic: Scaling Imitation Learning via Egocentric Video
- **Authors**: Hoque et al. (Georgia Tech)
- **Venue**: CoRL 2024
- **Task**: Robot imitation learning from egocentric human demonstrations
- **How Aria is used**: Aria glasses capture egocentric video + 3D hand tracking data. 90 minutes of Aria recordings train a bimanual robot manipulator via cross-domain co-training.
- **Key result**: 400% improvement in robot task performance vs. robot-only data; 1 hour of hand data > 1 hour of robot data.
- **Links**: [Paper](https://arxiv.org/abs/2410.24221) | [Project](https://egomimic.github.io/)

### 10.2 EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video
- **Authors**: Hoque, Huang et al. (Apple)
- **Venue**: arXiv 2025
- **Task**: Dexterous robot manipulation from egocentric video
- **How Aria is related**: While EgoDex uses Apple Vision Pro (not Aria), it follows the same paradigm pioneered by EgoMimic with Aria. The approach validates egocentric video as a scalable data source for robot learning.
- **Links**: [Paper](https://arxiv.org/abs/2505.11709) | [Code](https://github.com/apple/ml-egodex)

### 10.3 IndEgo: A Dataset of Industrial Scenarios and Collaborative Work for Egocentric Assistants
- **Authors**: Chavan et al. (Fraunhofer IPK)
- **Venue**: NeurIPS 2025 (Datasets & Benchmarks)
- **Task**: Industrial task understanding, mistake detection, QA
- **How Aria is used**: 3,460 egocentric recordings (~197 hours) captured with Meta Project Aria devices at 2880x2880 @ 10 FPS. Includes eye gaze, hand pose, semi-dense point clouds from MPS.
- **Key result**: First industrial egocentric dataset with collaborative work, mistake annotations, and reasoning-based QA.
- **Links**: [Paper](https://arxiv.org/abs/2511.19684) | [Code](https://github.com/Vivek9Chavan/IndEgo) | [HuggingFace](https://huggingface.co/datasets/FraunhoferIPK/IndEgo)

### 10.4 HD-EPIC: A Highly-Detailed Egocentric Video Dataset
- **Authors**: Perrett et al. (Bristol, Bath)
- **Venue**: CVPR 2025
- **Task**: Fine-grained action recognition, recipe understanding, audio event detection
- **How Aria is related**: While HD-EPIC uses its own capture setup, it follows the egocentric paradigm and is benchmarked alongside Aria datasets in the egocentric vision community (EgoVis workshop).
- **Key result**: 41 hours, 4.4M frames, 59.4K actions with digital twin grounding.
- **Links**: [Paper](https://arxiv.org/abs/2502.04144) | [Project](https://hd-epic.github.io/)

### 10.5 TEXT2TASTE: Egocentric Vision System for Intelligent Reading Assistance
- **Venue**: arXiv 2024
- **Task**: Reading assistance using egocentric vision + LLM
- **How Aria is used**: Uses Aria glasses as the egocentric capture device for text recognition and contextual understanding.
- **Links**: [Paper](https://arxiv.org/abs/2404.09254)

---

## 11. Cross-Dataset Research & Frameworks

### 11.1 ATEK: Aria Training and Evaluation Kit
- **Authors**: Meta FAIR
- **Task**: End-to-end deep learning framework for Aria data
- **Datasets supported**: ADT, ASE, AEA, AEO (expandable)
- **What it does**: Converts VRS/MPS data to PyTorch-compatible formats; provides preprocessed datasets, standardized evaluation tools, and data store.
- **Links**: [GitHub](https://github.com/facebookresearch/ATEK) | [Docs](https://facebookresearch.github.io/projectaria_tools/docs/ATEK/about_ATEK)

### 11.2 Project Aria: A New Tool for Egocentric Multi-Modal AI Research
- **Authors**: Engel et al. (Meta)
- **Venue**: arXiv 2023
- **What it is**: The foundational paper describing the Aria glasses platform, sensor specs, MPS pipeline, and research ecosystem.
- **Links**: [Paper](https://arxiv.org/abs/2308.13561)

### 11.3 Aria Gen 2 Pilot Dataset (A2PD)
- **Authors**: Meta Reality Labs
- **Venue**: arXiv 2025
- **What it is**: New dataset captured with next-gen Aria Gen 2 glasses featuring 4 CV cameras (vs 2 on Gen 1), enhanced RGB resolution, PPG sensor, and Sub-GHz radio for sub-millisecond time alignment.
- **Scenarios**: Cleaning, cooking, eating, playing, outdoor walking
- **Links**: [Paper](https://arxiv.org/abs/2510.16134) | [Dataset](https://www.projectaria.com/datasets/gen2pilot/)

### 11.4 An Outlook into the Future of Egocentric Vision
- **Venue**: IJCV 2024
- **Task**: Survey/vision paper
- **How Aria is used**: Project Aria datasets are discussed as key infrastructure for the future of egocentric AI research.
- **Links**: [Paper](https://link.springer.com/article/10.1007/s11263-024-02095-7)

---

## 12. Competitions & Challenges

### 12.1 CVPR 2025 EgoVis Workshop - Ego4D + EgoExo4D Challenges
- **15 challenges total** (9 Ego4D + 6 EgoExo4D)
- EgoExo4D tasks: Keystep Recognition, Proficiency Estimation, Ego-Exo Transfer, Ego Pose, Translation, and more
- Launched March 5, 2025; leaderboard closes May 19, 2025
- **Links**: [Challenge](https://ego4d-data.org/docs/challenge/) | [Workshop](https://egovis.github.io/cvpr25/)

### 12.2 BOP Challenge 2024 (ECCV 2024)
- Uses HOT3D as one of three new benchmark datasets (BOP-H3)
- Tasks: Model-based & model-free 6DoF object pose estimation
- **Best Paper Award** at CV4MR Workshop, CVPR 2025
- **Links**: [Challenge](https://bop.felk.cvut.cz/challenges/bop-challenge-2024/) | [Report](https://arxiv.org/abs/2504.02812)

### 12.3 ECCV 2024 Egocentric Hand Tracking Challenge
- Uses HOT3D-Clips for hand pose and shape estimation
- Dual-device evaluation (Aria + Quest 3)

### 12.4 ICDAR 2024 - Reading Documents Through Aria Glasses
- Three tasks: word recognition, reading order prediction, page-level recognition
- Uses RDAG-1.0 dataset from Aria glasses
- **Links**: [Competition](https://link.springer.com/chapter/10.1007/978-3-031-70552-6_25)

### 12.5 ASE Challenges
- Object detection and scene understanding challenges using the 100K synthetic scenes
- **Links**: [Challenges](https://facebookresearch.github.io/projectaria_tools/docs/open_datasets/aria_synthetic_environments_dataset/ase_challenges)

---

## 13. Summary: Dataset x Task Matrix

| Paper / Project | Dataset(s) Used | Research Task | Venue |
|---|---|---|---|
| **DeGauss** | ADT, AEA, HOT3D | 3D reconstruction (Gaussian Splatting) | ICCV 2025 |
| **EFM3D** | ADT, ASE, AEO | 3D object detection, surface regression | ECCV 2024 |
| **Aria-NeRF** | Aria (general) | Multimodal NeRF view synthesis | arXiv 2023 |
| **HOT3D** | HOT3D (Aria+Quest3) | Hand-object tracking, 6DoF pose | CVPR 2025 |
| **BOP Challenge 2024** | HOT3D | 6DoF object pose estimation | CVPRW 2025 |
| **EgoMimic** | Aria (general) | Robot imitation learning | CoRL 2024 |
| **EgoDex** | Vision Pro (Aria paradigm) | Dexterous robot manipulation | arXiv 2025 |
| **IndEgo** | Aria (general) | Industrial task understanding, QA | NeurIPS 2025 |
| **Nymeria** | Nymeria | Body tracking, motion synthesis, action recognition | ECCV 2024 |
| **DTC** | DTC | Novel view synthesis, 3D reconstruction | CVPR 2025 |
| **Reading in the Wild** | Reading in the Wild | Reading activity detection | NeurIPS 2025 |
| **ICDAR RDAG** | Aria (general) | Scene text recognition | ICDAR 2024 |
| **Scene Text w/ Aria** | Aria (general) | Text detection under challenging conditions | arXiv 2025 |
| **TEXT2TASTE** | Aria (general) | Reading assistance with LLM | arXiv 2024 |
| **EgoExoLearn** | Ego-Exo4D | Cross-view action understanding | CVPR 2024 |
| **SEED4D** | Ego-Exo4D (inspired) | Synthetic ego-exo data generation | arXiv 2024 |
| **Ego-Exo Transfer Survey** | Ego-Exo4D | Cross-view action recognition survey | arXiv 2024 |
| **LTA Challenge 2025** | Ego4D/EgoExo4D | Long-term action anticipation | CVPRW 2025 |
| **OmniGS** | AEA (egocentric) | Omnidirectional Gaussian Splatting | WACV 2025 |
| **HD-EPIC** | Egocentric (related) | Fine-grained action recognition | CVPR 2025 |
| **A2PD** | Aria Gen 2 | Next-gen egocentric multimodal data | arXiv 2025 |
| **ATEK** | ADT, ASE, AEA, AEO | DL training/evaluation framework | Meta 2024 |

---

## Key Observations

1. **Most-cited dataset**: Aria Digital Twin (ADT) is the most widely used Aria dataset in downstream research, driven by its rich ground truth (depth, segmentation, 3D poses, synthetic rendering).

2. **Emerging application**: **Robot learning from egocentric video** (EgoMimic, EgoDex) is a rapidly growing area, using Aria's hand tracking + egocentric video to train robot manipulation policies.

3. **3D reconstruction dominance**: A large fraction of papers focus on 3D scene reconstruction (DeGauss, Aria-NeRF, OmniGS, EFM3D), leveraging Aria's multi-camera setup and MPS outputs.

4. **Cross-view learning**: Ego-Exo4D has spawned a new research direction in ego-exo transfer, cross-view correspondence, and multi-perspective skill assessment.

5. **Industrial applications**: IndEgo demonstrates Aria's utility beyond consumer/research settings, extending to manufacturing and collaborative industrial work.

6. **Text understanding**: Multiple papers (ICDAR RDAG, Reading in the Wild, TEXT2TASTE) explore the unique challenge of text recognition from always-on, low-resolution egocentric devices.

7. **Scale trends**: ASE (100K scenes, 23TB) enables large-scale pre-training, while newer efforts like ATEK and A2PD focus on making Aria data more accessible for deep learning workflows.

8. **Competition ecosystem**: Active challenge programs at CVPR, ECCV, ICDAR, and BOP ensure continuous benchmarking progress across the research community.

---

*Last updated: 2026-03-30*

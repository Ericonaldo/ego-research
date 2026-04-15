# Project Aria

这个子目录收纳仓库中所有 **Project Aria** 相关的脚本与样例数据。

## 目录

- `scripts/`: VRS / MPS 处理脚本、下载脚本和环境初始化脚本
- `data/sample/`: 官方公开小样本与处理结果
- `data/sample_extracted/`: 从 VRS 样例提取出的图像、IMU、标定结果

## 常用脚本

```bash
python aria/scripts/process_vrs.py aria/data/sample/mps_sample/sample.vrs -o aria/data/sample_extracted
python aria/scripts/process_mps.py aria/data/sample/mps_sample -o aria/data/sample/mps_processed
bash aria/scripts/download_dataset.sh <cdn_file.json> ./aria/data/<dataset_name> "0 1 3"
```

## 相关文档

- 根目录的 [RESEARCH.md](../RESEARCH.md): 横向比较 Aria、Ego4D / Ego-Exo4D、Xperience-10M
- 根目录的 [RESEARCH_PAPERS.md](../RESEARCH_PAPERS.md): 相关论文和 benchmark
- 根目录的 [DOWNLOAD_GUIDE.md](../DOWNLOAD_GUIDE.md): 跨数据集访问与下载指南

## 样例说明

- `aria/data/sample/` 保留原始官方测试样例与一部分已处理结果
- `aria/data/sample_extracted/` 是当前仓库内可直接查看的轻量输出，用于快速确认 `process_vrs.py` 的结果格式

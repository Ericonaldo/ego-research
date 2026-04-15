# Xperience-10M 下载与样例说明

## 1. 官方入口

- Release blog: https://ropedia.com/blog/20260316_xperience_10m
- Dataset card: https://huggingface.co/datasets/ropedia-ai/xperience-10m
- Sample: https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample
- Toolkit: https://github.com/Ropedia/HOMIE-toolkit

## 2. 访问特点

截至 **2026-04-15**，公开信息显示主数据访问通常包含：

- Hugging Face gated access
- 人工审核
- 非商业用途限制
- 额外协议签署

因此更现实的顺序是：

1. 先用公开 `sample`
2. 再用 `HOMIE-toolkit` 或本仓库的轻量脚本理解结构
3. 最后再决定是否申请完整数据

## 3. 仓库内 sample 的来源

本仓库中的 `xperience/data/sample_trimmed/` 不是手写 mock，而是从官方公开 sample 的 `annotation.hdf5` 裁剪出来的轻量版本：

- 保留完整的顶层结构
- 只截取前几帧深度、SLAM、手部、全身动作和一小段 IMU
- 生成 preview PNG 和摘要 JSON，便于快速浏览

## 4. 相关脚本

```bash
# 处理一个 episode 目录
python xperience/scripts/process_xperience.py xperience/data/sample_trimmed -o /tmp/xp_out

# 从官方 annotation.hdf5 生成仓库内可提交的裁剪 sample
python xperience/scripts/build_sample_subset.py /path/to/annotation.hdf5 -o xperience/data/sample_trimmed
```

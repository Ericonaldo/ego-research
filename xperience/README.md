# Xperience-10M

这个子目录收纳仓库中所有 **Xperience-10M** 相关内容，包括调研、访问说明、处理脚本和一个可直接提交到仓库的裁剪 sample。

## 目录

- `RESEARCH.md`: Xperience-10M 调研摘要
- `DOWNLOAD_GUIDE.md`: 官方访问流程和仓库内 sample 使用方式
- `scripts/`: annotation 处理脚本与 sample 裁剪脚本
- `data/sample_trimmed/`: 从官方 sample 导出的轻量裁剪样例

## 常用脚本

先安装轻量依赖：

```bash
python -m pip install -r xperience/scripts/requirements.txt
```

然后运行：

```bash
python xperience/scripts/process_xperience.py xperience/data/sample_trimmed -o xperience/data/sample_trimmed_processed
python xperience/scripts/build_sample_subset.py /path/to/annotation.hdf5 -o xperience/data/sample_trimmed
```

## 设计原则

- 不把官方 `annotation.hdf5` 原样放进仓库。官方 sample 单文件约 `1.8 GB`，太大。
- 仓库内保留一个 **derived trimmed sample**，便于读脚本、看结构、跑最小验证。
- 如果需要完整样例或视频，应回到官方 Hugging Face 页面申请或下载。

## 相关链接

- 官方 release blog: https://ropedia.com/blog/20260316_xperience_10m
- 官方 dataset card: https://huggingface.co/datasets/ropedia-ai/xperience-10m
- 官方 sample: https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample
- HOMIE-toolkit: https://github.com/Ropedia/HOMIE-toolkit

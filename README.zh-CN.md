# Wan2.2 TI2V 5B — ComfyUI / RunPod 可复现工作流

[日本語](README.md) | [English](README.en.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md)

[![作品集校验](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml)

这是为 ComfyUI Builder 应聘整理的视频生成作品集。同一个原生工作流同时支持文生视频（T2V）和可选的图生视频（I2V）。

![工作流架构概览](docs/workflow-map.svg)

## 特点

- 只使用 ComfyUI 原生节点，不依赖自定义节点
- 提供可在 RunPod 中 `Run All` 的环境安装与启动 Notebook
- 模型下载支持断点续传，并自动放入正确目录
- 使用明确的 commit 固定 ComfyUI 版本
- 绿色表示用户输入，紫色表示模型加载，蓝色表示自动处理和输出
- API Key 与 Hugging Face Token 只从环境变量读取，不写入交付文件

## 交付文件

| 文件 | 用途 |
| --- | --- |
| `workflows/wan2.2_ti2v_5b_portfolio.json` | 整理并分色后的 ComfyUI 工作流 |
| `notebooks/Rp_run_comfyui_cat88666.ipynb` | 安装、固定版本并启动 ComfyUI |
| `notebooks/DownLoad_Models.ipynb` | 下载并校验模型文件位置 |
| [`docs/TEST_NOTES_ZH-CN.md`](docs/TEST_NOTES_ZH-CN.md) | 中文操作说明与测试记录 |
| `docs/APPLICATION_JA.md` | 日文申请表文案 |

## 目标环境

- RunPod / Linux
- Python 3.12
- CUDA 12.8
- NVIDIA GPU，至少 8GB 显存，建议 16GB 以上
- 至少 30GB 可用磁盘空间

固定的 ComfyUI commit：

```text
b78cec879b9460d5cb25228a83a942fb78d2cd24
```

## 在 RunPod 中运行

1. 使用至少 35GB 持久磁盘启动 Pod。
2. 将两份 Notebook 上传到 JupyterLab。
3. 对 `DownLoad_Models.ipynb` 执行 `Run All`。
4. 对 `Rp_run_comfyui_cat88666.ipynb` 执行 `Run All`。
5. 在 RunPod 的 TCP/HTTP Service 中打开 `8188` 端口。
6. 在 ComfyUI 中加载工作流 JSON，只调整绿色区域，然后加入生成队列。

图生视频时，使用 `Ctrl+B` 启用默认被禁用的 `LoadImage` 节点；文生视频时保持禁用。

## 验证状态

本地和 GitHub Actions 已静态校验 JSON/Notebook 结构、代码单元 Python 语法、模型路径、分组颜色和敏感信息。静态校验不等于 GPU 生成成功。RunPod 实机验证完成后，才会在测试记录中填写 GPU、耗时、峰值显存和输出文件。

## 来源与许可

工作流基于 Comfy-Org 官方 Wan2.2 5B 模板（MIT License），并针对低成本验证调整了解析度、帧数、分组颜色、提示词和输出名称。

- [ComfyUI 官方 Wan2.2 教程](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- [Comfy-Org 官方工作流模板](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_5B_ti2v.json)
- 模板 commit：`23de45678592886158d1d97194e26d4dc59bb5b3`

第三方版权与许可信息参见 `THIRD_PARTY_NOTICES.md`。本仓库新增的文档和 Notebook 使用 MIT License。

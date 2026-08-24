# Wan2.2 TI2V 5B — Reproducible ComfyUI / RunPod workflow

[日本語](README.md) | [English](README.en.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md)

[![Validate portfolio](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml)

This portfolio project packages a native Wan2.2-TI2V-5B video workflow for ComfyUI. One graph supports text-to-video (T2V) and optional image-to-video (I2V) generation.

![Workflow architecture overview](docs/workflow-map.svg)

## Highlights

- Uses only native ComfyUI nodes; no custom nodes are required
- Includes a RunPod environment setup and launch notebook designed for `Run All`
- Provides restartable model downloads into the expected ComfyUI directories
- Pins ComfyUI to an explicit commit for reproducibility
- Marks user inputs in green, model loading in purple, and automated processing/output in blue
- Reads API keys and Hugging Face tokens from environment variables without storing them in deliverables

## Deliverables

| File | Purpose |
| --- | --- |
| `workflows/wan2.2_ti2v_5b_portfolio.json` | Organized and color-coded ComfyUI workflow |
| `notebooks/Rp_run_comfyui_cat88666.ipynb` | Install, pin, and launch ComfyUI |
| `notebooks/DownLoad_Models.ipynb` | Download models into the expected folders |
| [`docs/TEST_NOTES_EN.md`](docs/TEST_NOTES_EN.md) | English usage guide and test record |
| `docs/APPLICATION_JA.md` | Japanese application copy |

## Target environment

- RunPod / Linux
- Python 3.12
- CUDA 12.8
- NVIDIA GPU with at least 8GB VRAM; 16GB or more recommended
- At least 30GB of free disk space

Pinned ComfyUI commit:

```text
b78cec879b9460d5cb25228a83a942fb78d2cd24
```

## Run on RunPod

1. Start a Pod with at least 35GB of persistent storage.
2. Upload both notebooks to JupyterLab.
3. Run all cells in `DownLoad_Models.ipynb`.
4. Run all cells in `Rp_run_comfyui_cat88666.ipynb`.
5. Open port `8188` through the RunPod TCP/HTTP Service.
6. Load the workflow JSON in ComfyUI, adjust only the green sections, and queue the graph.

For I2V, press `Ctrl+B` to enable the disabled `LoadImage` node. Keep it disabled for T2V.

## Verification status

Local validation and GitHub Actions check the JSON/notebook structure, Python syntax in code cells, model paths, group colors, and accidental secret inclusion. Static validation does not prove successful GPU generation. GPU type, runtime, peak VRAM, and output evidence will be recorded only after a real RunPod execution.

## Provenance and license

The workflow is adapted from the official Comfy-Org Wan2.2 5B template under the MIT License. Resolution, frame count, group colors, prompts, and output names were adjusted for a lower-cost verification run.

- [Official ComfyUI Wan2.2 tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- [Official Comfy-Org workflow template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_5B_ti2v.json)
- Template commit: `23de45678592886158d1d97194e26d4dc59bb5b3`

See `THIRD_PARTY_NOTICES.md` for upstream copyright and licensing details. New documentation and notebooks in this repository are released under the MIT License.


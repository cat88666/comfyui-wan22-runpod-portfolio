# Test notes

[日本語](TEST_NOTES_JA.md) | [English](TEST_NOTES_EN.md) | [简体中文](TEST_NOTES_ZH-CN.md) | [한국어](TEST_NOTES_KO.md)

## User-editable sections

Change only the green groups:

1. `STEP 2 - PROMPTS`: positive and negative prompts
2. `OPTIONAL I2V IMAGE`: enable `LoadImage` with `Ctrl+B` only for I2V
3. `STEP 3 - SIZE & LENGTH`: width, height, and frame count

The purple model group and blue sampling/output groups normally require no changes.

## Execution steps

1. Run all cells in `DownLoad_Models.ipynb`.
2. Run all cells in `Rp_run_comfyui_cat88666.ipynb`.
3. Open ComfyUI on port `8188`.
4. Load the workflow JSON.
5. Review the green inputs and queue the graph.
6. Check the video under `ComfyUI/output/video/`.

## Test case A: Text-to-Video

- Input image: none (`LoadImage` remains disabled)
- Resolution: 640 x 352
- Frames: 49
- FPS: 24
- Prompt: `Cinematic macro shot of a tiny paper fox ...`
- Expected result: an approximately two-second MP4 showing a paper fox, rainy alley, and gentle camera movement

## Real-environment result

- Status: awaiting RunPod execution
- GPU: pending
- Python / CUDA: pending
- ComfyUI commit: `b78cec879b9460d5cb25228a83a942fb78d2cd24`
- Model download time: pending
- Generation time: pending
- Peak VRAM: pending
- Output file: pending
- Issues and fixes: pending

The project is not described as runtime-verified until this section contains evidence from a real GPU run.


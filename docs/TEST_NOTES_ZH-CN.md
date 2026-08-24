# 测试记录

[日本語](TEST_NOTES_JA.md) | [English](TEST_NOTES_EN.md) | [简体中文](TEST_NOTES_ZH-CN.md) | [한국어](TEST_NOTES_KO.md)

## 用户可以修改的区域

只调整绿色分组：

1. `STEP 2 - PROMPTS`：正向与负向提示词
2. `OPTIONAL I2V IMAGE`：仅在图生视频时使用 `Ctrl+B` 启用 `LoadImage`
3. `STEP 3 - SIZE & LENGTH`：宽度、高度和帧数

紫色模型分组以及蓝色采样/输出分组通常不需要修改。

## 执行步骤

1. 对 `DownLoad_Models.ipynb` 执行 `Run All`。
2. 对 `Rp_run_comfyui_cat88666.ipynb` 执行 `Run All`。
3. 通过 `8188` 端口打开 ComfyUI。
4. 加载工作流 JSON。
5. 检查绿色输入区域并加入生成队列。
6. 在 `ComfyUI/output/video/` 中检查视频。

## 测试用例 A：文生视频

- 输入图片：无（`LoadImage` 保持禁用）
- 分辨率：640 x 352
- 帧数：49
- FPS：24
- 提示词：`Cinematic macro shot of a tiny paper fox ...`
- 预期结果：约两秒的 MP4，可识别纸狐狸、雨中巷道和缓慢镜头移动

## 实机验证结果

- 状态：等待 RunPod 实机执行
- GPU：待填写
- Python / CUDA：待填写
- ComfyUI commit：`b78cec879b9460d5cb25228a83a942fb78d2cd24`
- 模型下载时间：待填写
- 生成耗时：待填写
- 峰值显存：待填写
- 输出文件：待填写
- 问题及处理：待填写

在本节拥有真实 GPU 运行证据之前，不会把该项目描述为已经通过运行时验证。


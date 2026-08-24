# テストメモ

[日本語](TEST_NOTES_JA.md) | [English](TEST_NOTES_EN.md) | [简体中文](TEST_NOTES_ZH-CN.md) | [한국어](TEST_NOTES_KO.md)

## ユーザーが触る場所

緑のグループだけを変更します。

1. `STEP 2 - PROMPTS`: positive / negative prompt
2. `OPTIONAL I2V IMAGE`: I2V の場合だけ `LoadImage` を `Ctrl+B` で有効化
3. `STEP 3 - SIZE & LENGTH`: 幅、高さ、フレーム数

紫のモデル領域と水色の sampling/output 領域は通常変更不要です。

## 実行手順

1. `DownLoad_Models.ipynb` を Run All
2. `Rp_run_comfyui_cat88666.ipynb` を Run All
3. ComfyUI の 8188 ポートを開く
4. workflow JSON を読み込む
5. 緑の入力項目を確認して Queue
6. `ComfyUI/output/video/` の動画を確認

## テストケース A: Text-to-Video

- 入力画像: なし（`LoadImage` は disabled）
- 解像度: 640 x 352
- フレーム: 49
- FPS: 24
- Prompt: `Cinematic macro shot of a tiny paper fox ...`
- 期待結果: 約2秒の MP4。紙の狐、雨の路地、緩やかなカメラ移動が認識できること

## 実機検証結果

- 状態: RunPod 検証待ち
- GPU: 待ち
- Python / CUDA: 待ち
- ComfyUI commit: `b78cec879b9460d5cb25228a83a942fb78d2cd24`
- モデルダウンロード時間: 待ち
- 生成時間: 待ち
- Peak VRAM: 待ち
- 出力ファイル: 待ち
- 問題と対処: 待ち

実機で確認できるまでは「動作確認済み」と表記しません。

# 테스트 기록

[日本語](TEST_NOTES_JA.md) | [English](TEST_NOTES_EN.md) | [简体中文](TEST_NOTES_ZH-CN.md) | [한국어](TEST_NOTES_KO.md)

## 사용자가 변경할 영역

초록색 그룹만 조정합니다.

1. `STEP 2 - PROMPTS`: positive 및 negative prompt
2. `OPTIONAL I2V IMAGE`: I2V에서만 `Ctrl+B`로 `LoadImage` 활성화
3. `STEP 3 - SIZE & LENGTH`: 너비, 높이, 프레임 수

보라색 모델 그룹과 파란색 sampling/output 그룹은 일반적으로 변경할 필요가 없습니다.

## 실행 순서

1. `DownLoad_Models.ipynb`의 모든 셀을 실행합니다.
2. `Rp_run_comfyui_cat88666.ipynb`의 모든 셀을 실행합니다.
3. `8188` 포트에서 ComfyUI를 엽니다.
4. 워크플로 JSON을 불러옵니다.
5. 초록색 입력값을 확인하고 실행 대기열에 추가합니다.
6. `ComfyUI/output/video/`에서 영상을 확인합니다.

## 테스트 케이스 A: Text-to-Video

- 입력 이미지: 없음 (`LoadImage` 비활성 유지)
- 해상도: 640 x 352
- 프레임: 49
- FPS: 24
- 프롬프트: `Cinematic macro shot of a tiny paper fox ...`
- 예상 결과: 종이 여우, 비 오는 골목, 부드러운 카메라 이동이 보이는 약 2초 MP4

## 실제 환경 검증 결과

- 상태: RunPod 실행 대기
- GPU: 대기
- Python / CUDA: 대기
- ComfyUI commit: `b78cec879b9460d5cb25228a83a942fb78d2cd24`
- 모델 다운로드 시간: 대기
- 생성 시간: 대기
- 최대 VRAM: 대기
- 출력 파일: 대기
- 문제 및 해결: 대기

실제 GPU 실행 증거가 이 섹션에 기록되기 전에는 런타임 검증 완료로 표시하지 않습니다.

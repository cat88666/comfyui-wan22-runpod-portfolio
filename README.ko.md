# Wan2.2 TI2V 5B — 재현 가능한 ComfyUI / RunPod 워크플로

[日本語](README.md) | [English](README.en.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md)

[![포트폴리오 검증](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/cat88666/comfyui-wan22-runpod-portfolio/actions/workflows/validate.yml)

ComfyUI 빌더 지원을 위해 정리한 Wan2.2-TI2V-5B 영상 생성 포트폴리오입니다. 하나의 네이티브 워크플로로 텍스트-투-비디오(T2V)와 선택적 이미지-투-비디오(I2V)를 지원합니다.

![워크플로 아키텍처 개요](docs/workflow-map.svg)

## 주요 특징

- ComfyUI 기본 노드만 사용하며 커스텀 노드가 필요하지 않습니다
- RunPod에서 `Run All`로 환경을 설치하고 실행하는 Notebook을 제공합니다
- 중단 후 재개 가능한 모델 다운로드와 올바른 모델 경로를 제공합니다
- 재현성을 위해 ComfyUI commit을 명시적으로 고정합니다
- 사용자 입력은 초록색, 모델 로드는 보라색, 자동 처리와 출력은 파란색으로 구분합니다
- API 키와 Hugging Face Token은 환경 변수에서만 읽고 결과물에 저장하지 않습니다

## 제공 파일

| 파일 | 용도 |
| --- | --- |
| `workflows/wan2.2_ti2v_5b_portfolio.json` | 정리 및 색상 구분된 ComfyUI 워크플로 |
| `notebooks/Rp_run_comfyui_cat88666.ipynb` | ComfyUI 설치, 버전 고정 및 실행 |
| `notebooks/DownLoad_Models.ipynb` | 모델을 지정된 폴더에 다운로드 |
| [`docs/TEST_NOTES_KO.md`](docs/TEST_NOTES_KO.md) | 한국어 사용 방법 및 테스트 기록 |
| `docs/APPLICATION_JA.md` | 일본어 지원서 문안 |

## 대상 환경

- RunPod / Linux
- Python 3.12
- CUDA 12.8
- 최소 8GB VRAM의 NVIDIA GPU, 16GB 이상 권장
- 최소 30GB의 여유 디스크 공간

고정된 ComfyUI commit:

```text
b78cec879b9460d5cb25228a83a942fb78d2cd24
```

## RunPod 실행 방법

1. 35GB 이상의 영구 스토리지를 설정하여 Pod를 시작합니다.
2. 두 Notebook을 JupyterLab에 업로드합니다.
3. `DownLoad_Models.ipynb`의 모든 셀을 실행합니다.
4. `Rp_run_comfyui_cat88666.ipynb`의 모든 셀을 실행합니다.
5. RunPod TCP/HTTP Service에서 `8188` 포트를 엽니다.
6. ComfyUI에서 워크플로 JSON을 불러오고 초록색 영역만 조정한 뒤 실행 대기열에 추가합니다.

I2V를 사용할 때는 `Ctrl+B`로 비활성화된 `LoadImage` 노드를 활성화합니다. T2V에서는 비활성 상태를 유지합니다.

## 검증 상태

로컬 검증과 GitHub Actions는 JSON/Notebook 구조, 코드 셀의 Python 문법, 모델 경로, 그룹 색상, 비밀정보 포함 여부를 정적으로 검사합니다. 정적 검증은 GPU 생성 성공을 의미하지 않습니다. 실제 RunPod 실행 후에만 GPU 종류, 실행 시간, 최대 VRAM 및 출력 증거를 테스트 기록에 추가합니다.

## 출처 및 라이선스

이 워크플로는 MIT License로 공개된 Comfy-Org 공식 Wan2.2 5B 템플릿을 기반으로 합니다. 저비용 검증을 위해 해상도, 프레임 수, 그룹 색상, 프롬프트 및 출력 이름을 조정했습니다.

- [ComfyUI 공식 Wan2.2 튜토리얼](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- [Comfy-Org 공식 워크플로 템플릿](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_5B_ti2v.json)
- 템플릿 commit: `23de45678592886158d1d97194e26d4dc59bb5b3`

업스트림 저작권 및 라이선스는 `THIRD_PARTY_NOTICES.md`를 참조하십시오. 이 저장소에서 새로 작성한 문서와 Notebook은 MIT License로 배포됩니다.

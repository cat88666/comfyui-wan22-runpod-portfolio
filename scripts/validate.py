#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "workflows" / "wan2.2_ti2v_5b_portfolio.json"
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))
README_MARKERS = {
    "README.md": "検証状態",
    "README.en.md": "Verification status",
    "README.zh-CN.md": "验证状态",
    "README.ko.md": "검증 상태",
}
TEST_NOTE_MARKERS = {
    "docs/TEST_NOTES_JA.md": "実機検証結果",
    "docs/TEST_NOTES_EN.md": "Real-environment result",
    "docs/TEST_NOTES_ZH-CN.md": "实机验证结果",
    "docs/TEST_NOTES_KO.md": "실제 환경 검증 결과",
}
LANGUAGE_LINKS = (
    "README.md",
    "README.en.md",
    "README.zh-CN.md",
    "README.ko.md",
)


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


workflow = load_json(WORKFLOW)
assert len(workflow["nodes"]) >= 10
node_types = {node["type"] for node in workflow["nodes"]}
required_nodes = {
    "UNETLoader",
    "CLIPLoader",
    "VAELoader",
    "Wan22ImageToVideoLatent",
    "KSampler",
    "SaveVideo",
}
assert required_nodes <= node_types, required_nodes - node_types

serialized = json.dumps(workflow, ensure_ascii=False)
for model_name in (
    "wan2.2_ti2v_5B_fp16.safetensors",
    "wan2.2_vae.safetensors",
    "umt5_xxl_fp8_e4m3fn_scaled.safetensors",
):
    assert model_name in serialized

group_colors = {group["color"].upper() for group in workflow["groups"]}
assert {"#43A047", "#7E57C2", "#3F789E"} <= group_colors

assert len(NOTEBOOKS) == 2, NOTEBOOKS
for notebook_path in NOTEBOOKS:
    notebook = load_json(notebook_path)
    assert notebook["nbformat"] == 4
    assert notebook["cells"]
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            compile("".join(cell["source"]), f"{notebook_path.name}:cell-{index}", "exec")

for relative_path, marker in {**README_MARKERS, **TEST_NOTE_MARKERS}.items():
    path = ROOT / relative_path
    assert path.is_file(), f"missing multilingual document: {relative_path}"
    content = path.read_text(encoding="utf-8")
    assert marker in content, f"language marker missing from {relative_path}"
    assert "b78cec879b9460d5cb25228a83a942fb78d2cd24" in content

for readme_name in LANGUAGE_LINKS:
    content = (ROOT / readme_name).read_text(encoding="utf-8")
    for linked_readme in LANGUAGE_LINKS:
        assert f"({linked_readme})" in content, f"{readme_name} does not link to {linked_readme}"

markdown_link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
for markdown_path in ROOT.rglob("*.md"):
    content = markdown_path.read_text(encoding="utf-8")
    for target in markdown_link_pattern.findall(content):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        relative_target = target.split("#", 1)[0]
        resolved = (markdown_path.parent / relative_target).resolve()
        assert resolved.exists(), f"broken local link in {markdown_path}: {target}"

secret_pattern = re.compile(r"(?:hf_|rpa_)[A-Za-z0-9]{20,}")
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".mp4"}:
        continue
    content = path.read_text(encoding="utf-8")
    assert not secret_pattern.search(content), f"possible secret in {path}"

print(
    "Static validation passed: workflow, notebooks, colors, models, "
    "four-language docs, local links, and secret scan."
)

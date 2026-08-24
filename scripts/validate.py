#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "workflows" / "wan2.2_ti2v_5b_portfolio.json"
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))


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

secret_pattern = re.compile(r"(?:hf_|rpa_)[A-Za-z0-9]{20,}")
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".mp4"}:
        continue
    content = path.read_text(encoding="utf-8")
    assert not secret_pattern.search(content), f"possible secret in {path}"

print("Static validation passed: workflow, notebooks, colors, models, and secret scan.")

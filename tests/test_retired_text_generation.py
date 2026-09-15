"""Retired commands cannot load a model, rewrite historical maps, or parse shell text."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize("script,args", [
    ("embed_records.py", []),
    ("embed_records.py", ["--model", "custom/model", "--limit", "20"]),
    ("embed_map.py", []),
    ("embed_map.py", ["--method", "pca"]),
])
def test_retired_direct_cli_fails_before_data_or_model_access(tmp_path, script, args):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    shutil.copyfile(ROOT / "scripts" / script, scripts / script)
    # A corpus read, numerical import, or model load must fail visibly in this
    # subprocess. A normal retirement must never reach any of these tripwires.
    (scripts / "yaml.py").write_text(
        "def safe_load(*args, **kwargs):\n    raise AssertionError('corpus read')\n")
    for module in ("numpy", "torch", "sentence_transformers", "pacmap", "umap"):
        (scripts / f"{module}.py").write_text("raise AssertionError('model/numerical import')\n")
    saved = tmp_path / "data" / "embeddings" / "corpus_map.json"
    saved.parent.mkdir(parents=True)
    saved.write_text('{"historical": true}\n')
    result = subprocess.run([sys.executable, str(scripts / script), *args],
                            cwd=tmp_path, capture_output=True, text=True, check=False)
    assert result.returncode == 2, result.stderr
    assert "Legacy text generation is retired" in result.stderr
    assert "docs/TEXT_MAP_INPUTS.md" in result.stderr
    assert "conf/embedding-runtime/README.md" in result.stderr
    assert saved.read_text() == '{"historical": true}\n'
    assert list(saved.parent.iterdir()) == [saved]


@pytest.mark.skipif(shutil.which("just") is None, reason="the just developer tool is required")
@pytest.mark.parametrize("recipe,script,prefix", [
    ("embed", "embed_records.py", []),
    ("embed-canary", "embed_records.py", ["--limit", "20"]),
    ("embed-map", "embed_map.py", []),
])
def test_actual_just_recipe_forwards_literal_arguments_to_locked_cli(
        tmp_path, recipe, script, prefix):
    just = shutil.which("just")
    assert just is not None, "just is required to verify the maintained command"
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    log = tmp_path / "argv.json"
    stub = bin_dir / "uv"
    stub.write_text(f"#!{sys.executable}\n" +
                    "import json, os, sys\n" +
                    "with open(os.environ['EMBED_ARGV_LOG'], 'w') as out:\n" +
                    "    json.dump(sys.argv[1:], out)\n" +
                    "sys.exit(2)\n")
    stub.chmod(0o755)
    marker = tmp_path / "unexpected-shell-write"
    literal = f"custom model; $(touch {marker}) `touch {marker}`"
    args = ["--model", literal] if recipe != "embed-map" else ["--method", literal]
    env = {**os.environ, "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
           "EMBED_ARGV_LOG": str(log)}
    result = subprocess.run([just, "--justfile", str(ROOT / "justfile"),
                             "--working-directory", str(ROOT), recipe, *args],
                            env=env, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert log.exists(), result.stderr
    assert json.loads(log.read_text()) == [
        "run", "--locked", "python", "scripts/" + script, *prefix, *args]
    assert not marker.exists()


def test_document_preview_remains_read_only(tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    shutil.copyfile(ROOT / "scripts/embed_records.py", scripts / "embed_records.py")
    (scripts / "yaml.py").write_text("from json import loads as safe_load\n")
    for module in ("numpy", "torch", "sentence_transformers"):
        (scripts / f"{module}.py").write_text("raise AssertionError('model import')\n")
    for corpus in ("antibiotics", "natural_products"):
        data = tmp_path / "data" / corpus
        data.mkdir(parents=True)
        (data / "one.yaml").write_text(json.dumps({
            "identifier": "TEST:1", "label": "A named compound",
            "antimicrobial_class": "ANTIBACTERIAL", "np_pathway": "ALKALOIDS"}))
    result = subprocess.run([sys.executable, str(scripts / "embed_records.py"),
                             "--dry-run", "--limit", "1"], cwd=tmp_path,
                            capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    assert "historical document previews" in result.stdout
    assert "A named compound" in result.stdout
    assert not (tmp_path / "data" / "embeddings").exists()

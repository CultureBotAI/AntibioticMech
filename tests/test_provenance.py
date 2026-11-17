"""Provenance and QC wiring — checkable claims, not documentation."""

from __future__ import annotations

import gzip
import hashlib
import subprocess
import sys

import pytest
import yaml


def test_provenance_check_passes(repo_root):
    result = subprocess.run([sys.executable, "scripts/check_provenance.py"],
                            cwd=repo_root, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_manifest_covers_every_committed_inventory(repo_root):
    manifest = yaml.safe_load((repo_root / "data" / "raw" / "MANIFEST.yaml").read_text())
    raw = repo_root / "data" / "raw"
    committed = {p.name for pattern in ("*.tsv", "*.tsv.gz") for p in raw.glob(pattern)}
    assert committed <= set(manifest["inventories"])


def test_manifest_records_where_every_upstream_file_came_from(repo_root):
    manifest = yaml.safe_load((repo_root / "data" / "raw" / "MANIFEST.yaml").read_text())
    for name, entry in manifest["downloads"].items():
        assert entry["url"].startswith("https://"), name
        assert len(entry["sha256"]) == 64, name


def test_qc_runs_every_check_a_reviewer_would_expect(repo_root):
    """The QC list is the repository's definition of green. A check silently
    dropped from it is a check nobody runs."""
    sys.path.insert(0, str(repo_root / "scripts"))
    from run_qc import COMMANDS

    names = {name for name, _, _ in COMMANDS}
    assert {"lint", "tests", "schema validation", "corpus reproduction",
            "raw-data provenance", "documentation", "generated site"} <= names
    for _, command, rationale in COMMANDS:
        assert rationale.strip(), command


@pytest.fixture
def gzip_inventory(tmp_path, monkeypatch, repo_root):
    sys.path.insert(0, str(repo_root / "scripts"))
    import check_provenance as checker

    path = tmp_path / "ncbi_ast_activity.tsv.gz"
    payload = b"column\nvalue\n"
    path.write_bytes(gzip.compress(payload, mtime=0))
    entry = {
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size, "rows": 1, "encoding": "gzip",
        "content_sha256": hashlib.sha256(payload).hexdigest(), "content_bytes": len(payload),
    }
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(yaml.safe_dump({"inventories": {path.name: entry}}))
    monkeypatch.setattr(checker, "RAW_DIR", tmp_path)
    monkeypatch.setattr(checker, "MANIFEST_PATH", manifest)
    return checker, path, manifest, entry


def test_provenance_detects_unmanifested_gzip_inventory(gzip_inventory, capsys):
    checker, path, manifest, _ = gzip_inventory
    manifest.write_text("inventories: {}\n")
    assert checker.main() == 1
    assert f"{path.name}: committed but absent from MANIFEST.yaml" in capsys.readouterr().err


def test_provenance_checks_gzip_container_content_and_rows(gzip_inventory):
    checker, _, _, _ = gzip_inventory
    assert checker.main() == 0


@pytest.mark.parametrize("field,value", [
    ("sha256", "0" * 64), ("bytes", 0), ("rows", 2), ("encoding", "identity"),
    ("content_sha256", "0" * 64), ("content_bytes", 0),
])
def test_provenance_rejects_gzip_manifest_drift(gzip_inventory, field, value):
    checker, path, manifest, entry = gzip_inventory
    entry[field] = value
    manifest.write_text(yaml.safe_dump({"inventories": {path.name: entry}}))
    assert checker.main() == 1


def test_provenance_requires_gzip_content_pin(gzip_inventory):
    checker, path, manifest, entry = gzip_inventory
    entry.pop("content_sha256")
    manifest.write_text(yaml.safe_dump({"inventories": {path.name: entry}}))
    assert checker.main() == 1


def test_provenance_reports_corrupt_gzip(gzip_inventory, capsys):
    checker, path, _, _ = gzip_inventory
    path.write_bytes(path.read_bytes()[:-4])
    assert checker.main() == 1
    assert "cannot read inventory" in capsys.readouterr().err


def test_provenance_bounds_gzip_expansion(gzip_inventory, monkeypatch, capsys):
    import ncbi_ast_inventory

    checker, _, _, _ = gzip_inventory
    monkeypatch.setattr(ncbi_ast_inventory, "MAX_CONTENT_BYTES", 8)
    assert checker.main() == 1
    assert "expanded-byte limit" in capsys.readouterr().err

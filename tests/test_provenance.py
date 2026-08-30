"""Provenance and QC wiring — checkable claims, not documentation."""

from __future__ import annotations

import subprocess
import sys

import yaml


def test_provenance_check_passes(repo_root):
    result = subprocess.run([sys.executable, "scripts/check_provenance.py"],
                            cwd=repo_root, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_manifest_covers_every_committed_inventory(repo_root):
    manifest = yaml.safe_load((repo_root / "data" / "raw" / "MANIFEST.yaml").read_text())
    committed = {p.name for p in (repo_root / "data" / "raw").glob("*.tsv")}
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

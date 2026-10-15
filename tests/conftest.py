"""Shared fixtures: the corpus and the raw inventories, loaded once per session.

Parsing 2600 YAML files per test would dominate the suite's runtime, so the
corpus is a session-scoped fixture. Tests must treat it as read-only.
"""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

REPO_ROOT = Path(__file__).resolve().parents[1]

CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
RAW_DIR = REPO_ROOT / "data" / "raw"
SCHEMA_PATH = REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_path() -> Path:
    return SCHEMA_PATH


@pytest.fixture(scope="session")
def records() -> list[tuple[Path, dict]]:
    """Every seeded AntibioticRecord as (path, parsed doc)."""
    if not CORPUS_DIR.exists():
        pytest.skip(f"no corpus at {CORPUS_DIR}; run `just seed-apply`")
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        out.append((path, load_record(path)))
    if not out:
        pytest.skip(f"corpus at {CORPUS_DIR} is empty")
    return out


@pytest.fixture(scope="session")
def path_lockfile() -> dict[str, str]:
    """The committed identifier -> slug assignments in data/antibiotics/PATHS.tsv."""
    path = CORPUS_DIR / "PATHS.tsv"
    if not path.exists():
        pytest.skip(f"no lockfile at {path}; run `just seed-apply`")
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["slug"] for r in csv.DictReader(fh, delimiter="\t")}


@pytest.fixture(scope="session")
def raw_tsv():
    """Callable returning a parsed data/raw TSV by filename."""
    cache: dict[str, list[dict[str, str]]] = {}

    def _load(name: str) -> list[dict[str, str]]:
        if name not in cache:
            path = RAW_DIR / name
            if not path.exists():
                pytest.skip(f"missing inventory {path}; run `just extract-inventory`")
            with path.open(newline="", encoding="utf-8") as fh:
                cache[name] = list(csv.DictReader(fh, delimiter="\t"))
        return cache[name]

    return _load


def _qualification_deltas(root):
    payload = (root / "research/2026-10-15-card-evidence-qualifications-verification.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "1e6378c711d7627465a26602f6ac3129c8a4f478bb26646cf7d232ad3e89152c"
    )
    deltas = json.loads(payload)["record_deltas"]
    assert len(deltas) == 3
    return {row["path"]: row for row in deltas}


def _restore_pre_qualification(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    delta = _qualification_deltas(root)[relative_path]
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"][-1]["action"] == "RESEEDED_FROM_SOURCES"
    historical["curation_history"].pop()
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note").startswith("Evidence-scope review ")
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_card_qualification():
    return _restore_pre_qualification


@pytest.fixture(scope="session")
def pre_card_qualification_root(tmp_path_factory):
    """Reconstruct only the three pinned note/history deltas, never the live files."""
    root = tmp_path_factory.mktemp("pre-card-qualification")
    shutil.copytree(CORPUS_DIR, root / "data/antibiotics")
    for relative in ("data/raw", "research", "curation"):
        (root / relative).symlink_to(REPO_ROOT / relative, target_is_directory=True)
    for relative in _qualification_deltas(REPO_ROOT):
        _restore_pre_qualification(REPO_ROOT, relative, root / relative)
    return root

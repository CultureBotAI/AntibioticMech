"""Shared fixtures: the corpus and the raw inventories, loaded once per session.

Parsing 2600 YAML files per test would dominate the suite's runtime, so the
corpus is a session-scoped fixture. Tests must treat it as read-only.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest
import yaml

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
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.safe_load(fh)))
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

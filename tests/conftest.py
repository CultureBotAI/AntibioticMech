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
def require_native_inputs():
    """Skip only optional cache consumers, never missing public inputs or corrupt pins."""

    def check(*documents):
        def visit(value):
            if isinstance(value, dict):
                path = value.get("path")
                if (
                    isinstance(path, str) and path.startswith("reports/")
                    and "sha256" in value and not (REPO_ROOT / path).is_file()
                ):
                    pytest.skip(f"optional native research cache unavailable: {path}")
                for item in value.values():
                    visit(item)
            elif isinstance(value, list):
                for item in value:
                    visit(item)

        for document in documents:
            visit(document)

    return check


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
def pre_card_qualification_root(tmp_path_factory, pre_cdsa_qualification_root):
    """Reconstruct only the three pinned note/history deltas, never the live files."""
    root = tmp_path_factory.mktemp("pre-card-qualification")
    source = pre_cdsa_qualification_root
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "curation", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    for relative in _qualification_deltas(source):
        _restore_pre_qualification(source, relative, root / relative)
    return root


def _cdsa_transition(root):
    payload = (root / "research/2026-10-15-cdsa-qualification-transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "b5c28727895c2b88845978f0e6afe158371e1b3e2be8633a465cdcf14adca0b8"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 4
    return transition


def _restore_pre_cdsa(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _cdsa_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note") == change["after_note"]
        if change["before_note"] is not None:
            claim["note"] = change["before_note"]
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_cdsa_qualification():
    return _restore_pre_cdsa


@pytest.fixture(scope="session")
def pre_cdsa_qualification_root(tmp_path_factory, pre_salmonella_qualification_root):
    """Reconstruct the exact prior notes, history and active review file in isolation."""
    source = pre_salmonella_qualification_root
    transition = _cdsa_transition(source)
    review = transition["review_file"]
    assert hashlib.sha256((source / review["path"]).read_bytes()).hexdigest() == (
        review["after_sha256"]
    )
    archive = transition["historical_review_fixture"]
    payload = (source / archive["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == archive["sha256"] == review["before_sha256"]
    root = tmp_path_factory.mktemp("pre-cdsa-qualification")
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (source / "curation").iterdir():
        if path.name != "card_evidence_reviews.json":
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    (root / review["path"]).write_bytes(payload)
    for delta in transition["record_deltas"]:
        _restore_pre_cdsa(source, delta["path"], root / delta["path"])
    return root


def _salmonella_transition(root):
    payload = (root / "research/2026-10-16-salmonella-qualification-transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "95953c299ce1d257958070a37882b22febb878f3c0194d54cd119eb3eb8ec4ef"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 17
    return transition


def _restore_pre_salmonella(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _salmonella_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note") == change["after_note"]
        if change["before_note"] is not None:
            claim["note"] = change["before_note"]
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_salmonella_qualification():
    return _restore_pre_salmonella


@pytest.fixture(scope="session")
def pre_salmonella_qualification_root(tmp_path_factory):
    """Restore only the 17 exact note/history deltas and the prior review bytes."""
    transition = _salmonella_transition(REPO_ROOT)
    review = transition["review_file"]
    assert hashlib.sha256((REPO_ROOT / review["path"]).read_bytes()).hexdigest() == review["after_sha256"]
    archive = transition["historical_review_fixture"]
    payload = (REPO_ROOT / archive["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == archive["sha256"] == review["before_sha256"]
    root = tmp_path_factory.mktemp("pre-salmonella-qualification")
    shutil.copytree(CORPUS_DIR, root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(REPO_ROOT / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (REPO_ROOT / "curation").iterdir():
        if path.name != "card_evidence_reviews.json":
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    (root / review["path"]).write_bytes(payload)
    for delta in transition["record_deltas"]:
        _restore_pre_salmonella(REPO_ROOT, delta["path"], root / delta["path"])
    return root

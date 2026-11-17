"""Published research bytes stay pinned even when native request caches are absent."""

import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REPORT = "research/2026-10-07-resistance-gene-grounding.md"
CHECKPOINTS = {
    "2026-10-14-card-beta-tubulin-memberships": ("-plan.json", ".json", ".tsv"),
    "2026-10-14-card-cytb-outer-memberships": ("-plan.json", ".json", ".tsv"),
    "2026-10-14-card-cytochrome-b": ("-references.json",),
    "2026-10-14-card-outer-membrane": ("-references.json",),
    "2026-10-14-cytochrome-b-evidence": (".json",),
    "2026-10-14-outer-membrane-evidence": (".json",),
    "2026-10-15-aac3-evidence": (".json",),
    "2026-10-15-aac6-gaps": (".json",),
    "2026-10-15-card-bla-alias-screen": (".json",),
    "2026-10-15-card-bla-memberships": ("-plan.json", ".json", ".tsv"),
    "2026-10-15-card-followup-memberships": ("-plan.json", ".json", ".tsv"),
    "2026-10-15-cipa-evidence": (".json",),
    "2026-10-15-kpn-evidence": (".json",),
    "2026-10-15-sco1-evidence": (".json",),
    "2026-10-15-vgb-evidence": (".json",),
}


def check_published_checkpoint(root, stem):
    prefix = "research/" + stem
    receipt = json.loads((root / (prefix + "-verification.json")).read_bytes())
    # Code and the append-only report may evolve; only immutable outputs are pinned here.
    files = [p for p in receipt["files"] if p["path"].startswith("research/") and p["path"] != REPORT]
    pins = {p["path"]: p["sha256"] for p in files}
    assert len(pins) == len(files), "duplicate published artifact pin"
    plan = receipt.get("plan")
    if plan is not None and plan["path"].startswith("research/"):
        assert pins.setdefault(plan["path"], plan["sha256"]) == plan["sha256"], "conflicting plan pin"
    assert set(pins) == {prefix + suffix for suffix in CHECKPOINTS[stem]}, "artifact coverage changed"
    for path, expected in pins.items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == expected, path


@pytest.fixture(autouse=True)
def no_request_cache_reads(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "reports"), "request cache read"
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)


@pytest.mark.parametrize("stem", CHECKPOINTS)
def test_published_bytes_match_verification_without_request_caches(stem):
    check_published_checkpoint(ROOT, stem)


@pytest.fixture
def aac6_copy(tmp_path):
    stem = "2026-10-15-aac6-gaps"
    for suffix in (".json", "-verification.json"):
        path = Path("research/" + stem + suffix)
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_bytes((ROOT / path).read_bytes())
    return tmp_path, stem


@pytest.mark.parametrize(
    "field,value",
    [
        ("reference_taxon_id", "NCBITaxon:1"),
        ("gene_symbols", ["CORRUPTED"]),
        ("experimental_subject_assignment", True),
    ],
)
def test_saved_reference_metadata_drift_fails_without_native_cache(aac6_copy, field, value):
    root, stem = aac6_copy
    path = root / ("research/" + stem + ".json")
    data = json.loads(path.read_bytes())
    data["references"]["UniProtKB:Q9AIK8"][field] = value
    path.write_text(json.dumps(data))
    with pytest.raises(AssertionError, match=stem):
        check_published_checkpoint(root, stem)


@pytest.mark.parametrize("change", ["missing", "omitted_pin", "duplicate_pin", "unexpected_pin"])
def test_artifact_and_receipt_coverage_cannot_silently_shrink(aac6_copy, change):
    root, stem = aac6_copy
    target = "research/" + stem + ".json"
    path = root / ("research/" + stem + "-verification.json")
    receipt = json.loads(path.read_bytes())
    pin = next(p for p in receipt["files"] if p["path"] == target)
    if change == "missing":
        (root / target).unlink()
    elif change == "omitted_pin":
        receipt["files"].remove(pin)
    elif change == "duplicate_pin":
        receipt["files"].append(pin)
    else:
        receipt["files"].append({"path": "research/unexpected.json", "sha256": "0" * 64})
    path.write_text(json.dumps(receipt))
    with pytest.raises((AssertionError, FileNotFoundError)):
        check_published_checkpoint(root, stem)


def test_historical_report_and_code_pins_do_not_require_current_bytes(aac6_copy):
    root, stem = aac6_copy
    # The temporary checkout has only the immutable output and receipt.
    assert not (root / REPORT).exists()
    assert not (root / "scripts").exists()
    check_published_checkpoint(root, stem)


@pytest.mark.parametrize("suffix", ["-plan.json", ".json", ".tsv"])
def test_each_membership_artifact_is_required_and_hash_checked(tmp_path, suffix):
    stem = "2026-10-14-card-beta-tubulin-memberships"
    prefix = "research/" + stem
    for extension in (*CHECKPOINTS[stem], "-verification.json"):
        path = Path(prefix + extension)
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_bytes((ROOT / path).read_bytes())
    check_published_checkpoint(tmp_path, stem)
    target = tmp_path / (prefix + suffix)
    target.write_bytes(target.read_bytes() + b"\n")
    with pytest.raises(AssertionError, match=stem):
        check_published_checkpoint(tmp_path, stem)
    target.unlink()
    with pytest.raises(FileNotFoundError):
        check_published_checkpoint(tmp_path, stem)

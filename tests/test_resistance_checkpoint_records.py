"""Historical pins never authorize a fallback for an unregistered live change."""

import hashlib
import importlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import resistance_checkpoint_records as checkpoint  # noqa: E402


@pytest.mark.parametrize("checksum", list(checkpoint.HISTORICAL_RECORDS))
@pytest.mark.parametrize("change", ["none", "identifier", "path", "missing", "corrupt", "unknown_hash"])
def test_registered_snapshot_not_mutable_live_record(tmp_path, checksum, change):
    identifier, original, fixture = checkpoint.HISTORICAL_RECORDS[checksum]
    item = {"identifier": identifier, "path": original, "sha256": checksum}
    snapshot = tmp_path / fixture
    snapshot.parent.mkdir(parents=True)
    if change != "missing":
        snapshot.write_bytes((ROOT / fixture).read_bytes())
    live = tmp_path / original
    live.parent.mkdir(parents=True)
    live.write_text("Legitimate later curation\n")
    if change == "identifier":
        item["identifier"] = "OTHER"
    elif change == "path":
        item["path"] = "data/antibiotics/other.yaml"
    elif change == "corrupt":
        snapshot.write_text("Corrupt fixture\n")
    elif change == "unknown_hash":
        item["sha256"] = "0" * 64
    if change != "none":
        with pytest.raises((ValueError, FileNotFoundError)):
            checkpoint.checkpoint_path(tmp_path, item)
    else:
        assert checkpoint.checkpoint_path(tmp_path, item) == snapshot
        assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == checksum
        item["sha256"] = hashlib.sha256(live.read_bytes()).hexdigest()
        assert checkpoint.checkpoint_path(tmp_path, item) == live


@pytest.mark.parametrize("module_name", [
    "audit_card_reference_lineages", "audit_card_species_nodes",
    "audit_fr171456_locus", "audit_thevissen_2007_access",
])
@pytest.mark.parametrize("historical", [False, True])
def test_cli_historical_replay_is_explicit(tmp_path, monkeypatch, capsys, module_name, historical):
    audit = importlib.import_module(module_name)
    expected = {"summary": {"synthetic": True}}
    output = tmp_path / "checkpoint.json"
    output.write_text(json.dumps(expected))
    before = output.read_bytes()
    calls = []

    def build(root, selected, *, record_resolver=None):
        assert root == tmp_path
        assert selected == getattr(audit, "PLAN", getattr(audit, "CACHE", None))
        calls.append(record_resolver)
        return expected

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(audit, "build", build)
    monkeypatch.setattr(sys, "argv", [module_name, "--check", "--output", str(output)]
                        + (["--historical-records"] if historical else []))
    audit.main()
    assert calls == [checkpoint.checkpoint_path if historical else None]
    assert json.loads(capsys.readouterr().out) == expected["summary"]
    assert output.read_bytes() == before


@pytest.mark.parametrize("checksum", [*checkpoint.CITATION_BASELINES, *checkpoint.ARCHIVE_BASELINES])
@pytest.mark.parametrize("change", ["none", "identifier", "path", "receipt", "live", "archive"])
def test_citation_delta_restores_only_pinned_historical_bytes(tmp_path, checksum, change):
    archive = checksum in checkpoint.ARCHIVE_BASELINES
    baselines = checkpoint.ARCHIVE_BASELINES if archive else checkpoint.CITATION_BASELINES
    receipt_pin = checkpoint.ARCHIVE_RECEIPT if archive else checkpoint.CITATION_RECEIPT
    identifier, path = baselines[checksum]
    item = {"identifier": identifier, "path": path, "sha256": checksum}
    receipt = tmp_path / receipt_pin["path"]
    receipt.parent.mkdir(parents=True)
    receipt.write_bytes((ROOT / receipt_pin["path"]).read_bytes())
    live = tmp_path / path
    live.parent.mkdir(parents=True)
    live.write_bytes((ROOT / path).read_bytes())
    if change == "identifier":
        item["identifier"] = "OTHER"
    elif change == "path":
        item["path"] = "data/antibiotics/other.yaml"
    elif change == "receipt":
        receipt.write_text("{}")
    elif change == "live":
        live.write_text("Later legitimate curation\n")
    elif change == "archive":
        archive = checkpoint.checkpoint_path(tmp_path, item)
        archive.write_text("Corrupt historical artifact\n")
    if change != "none":
        with pytest.raises((ValueError, FileNotFoundError, TypeError)):
            checkpoint.checkpoint_path(tmp_path, item)
    else:
        original_live = live.read_bytes()
        archive = checkpoint.checkpoint_path(tmp_path, item)
        assert hashlib.sha256(archive.read_bytes()).hexdigest() == checksum
        assert live.read_bytes() == original_live
        live.write_text("Later legitimate curation\n")
        assert checkpoint.checkpoint_path(tmp_path, item) == archive

"""Historical pins never authorize a fallback for an unregistered live change."""

import hashlib
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

"""The paired index CLI is read-only in check mode and refuses competing writes."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_folp_rpo_memberships as audit  # noqa: E402


@pytest.fixture
def outputs(tmp_path, monkeypatch):
    prefix = str(tmp_path / "index")
    monkeypatch.setattr(audit, "PREFIX", prefix)
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, []))
    monkeypatch.setattr(audit.prior.prior.prior, "render", lambda *args: (b"json", b"tsv"))
    monkeypatch.setattr(sys, "argv", ["audit"])
    return [(Path(prefix + ".json"), b"json"), (Path(prefix + ".tsv"), b"tsv")]


def forbid_writes(monkeypatch):
    original = Path.open

    def read_only(path, mode="r", *args, **kwargs):
        assert not any(flag in mode for flag in "wax+"), "check mode attempted a write"
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", read_only)


@pytest.mark.parametrize("check", [False, True])
def test_equal_checkpoints_are_not_rewritten(outputs, monkeypatch, check):
    for path, payload in outputs:
        path.write_bytes(payload)
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    forbid_writes(monkeypatch)
    audit.main()


@pytest.mark.parametrize("missing", [0, 1])
def test_check_missing_output_never_creates_it(outputs, monkeypatch, missing):
    for index, (path, payload) in enumerate(outputs):
        if index != missing:
            path.write_bytes(payload)
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    forbid_writes(monkeypatch)
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not outputs[missing][0].exists()


def test_check_cannot_recreate_output_deleted_after_validation(outputs, monkeypatch):
    for path, payload in outputs:
        path.write_bytes(payload)
    target, sibling = outputs[0][0], outputs[1][0]
    original_read = Path.read_bytes

    def read_then_delete(path):
        payload = original_read(path)
        if path == sibling:
            target.unlink()
        return payload

    monkeypatch.setattr(Path, "read_bytes", read_then_delete)
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    forbid_writes(monkeypatch)
    audit.main()
    assert not target.exists()


def test_concurrent_creation_is_not_skipped_or_overwritten(outputs, monkeypatch):
    target, sibling = outputs[0][0], outputs[1][0]
    sibling.write_bytes(outputs[1][1])
    original_read = Path.read_bytes

    def read_then_create(path):
        payload = original_read(path)
        if path == sibling:
            target.write_bytes(b"competing checkpoint")
        return payload

    monkeypatch.setattr(Path, "read_bytes", read_then_create)
    with pytest.raises(FileExistsError):
        audit.main()
    assert original_read(target) == b"competing checkpoint"
    assert original_read(sibling) == outputs[1][1]


@pytest.mark.parametrize("existing", [None, 0, 1])
def test_normal_creation_preserves_existing_valid_sibling(outputs, existing):
    if existing is not None:
        outputs[existing][0].write_bytes(outputs[existing][1])
    audit.main()
    assert all(path.read_bytes() == payload for path, payload in outputs)


@pytest.mark.parametrize("mismatched", [0, 1])
def test_all_existing_outputs_are_validated_before_any_write(outputs, mismatched):
    outputs[mismatched][0].write_bytes(b"historical")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert outputs[mismatched][0].read_bytes() == b"historical"
    assert not outputs[1 - mismatched][0].exists()

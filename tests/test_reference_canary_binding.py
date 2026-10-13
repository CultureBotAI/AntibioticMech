"""A valid canary from another query cannot authorize this audit's replay."""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_myriocin_references as myriocin  # noqa: E402
import audit_vatpase_references as vatpase  # noqa: E402


@pytest.mark.parametrize("audit,key", [(vatpase, "neurospora-c"), (myriocin, "sli1")])
@pytest.mark.parametrize("mutation", [
    "none", "response_path", "receipt_path", "both_paths",
    "response_hash", "receipt_hash", "unreviewed",
])
def test_canary_is_bound_to_the_expected_query(tmp_path, monkeypatch, audit, key, mutation):
    directory = tmp_path / "cache"
    directory.mkdir()
    canary = {"manually_reviewed": True}
    for field, suffix in (("response", "response.bin"), ("receipt", "receipt.json")):
        path = directory / f"{key}-{suffix}"
        path.write_bytes(b"Synthetic canary fixture: " + field.encode())
        canary[field] = audit.reference.pin(tmp_path, path)
        other = directory / f"unrelated-{suffix}"
        other.write_bytes(path.read_bytes())
        if mutation in (field + "_path", "both_paths"):
            canary[field] = audit.reference.pin(tmp_path, other)
        elif mutation == field + "_hash":
            canary[field]["sha256"] = "0" * 64
    if mutation == "unreviewed":
        canary["manually_reviewed"] = False
    (directory / "canary-reviewed.json").write_text(json.dumps(canary))
    sentinel = {"path": "after-canary", "sha256": "not-read"}
    plan = {"queries": audit.QUERIES, "fields": audit.reference.FIELDS,
            "census": sentinel, "record": sentinel}
    (directory / "cohort.json").write_text(json.dumps(plan))

    class CanaryAccepted(Exception):
        pass

    original = audit.reference.check_pin

    def stop_after_canary(root, item):
        if item == sentinel:
            raise CanaryAccepted
        return original(root, item)

    monkeypatch.setattr(audit.reference, "check_pin", stop_after_canary)
    if mutation == "none":
        with pytest.raises(CanaryAccepted):
            audit.build(tmp_path, directory)
    else:
        with pytest.raises(ValueError, match="canary"):
            audit.build(tmp_path, directory)

"""Verify native AST exports are complete before publishing a local snapshot."""

import csv
import hashlib
import io
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_ncbi_ast as fetch  # noqa: E402


def native_export(ids=("001_PDT000277868.2",)):
    handle = io.StringIO(newline="")
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(fetch.EXPORT_HEADER)
    for row_id in ids:
        writer.writerow([row_id] + [""] * (len(fetch.EXPORT_HEADER) - 1))
    return handle.getvalue().encode()


def fake_responses(monkeypatch, export, before=1, after=1):
    payloads = iter([
        json.dumps({"success": True, "ngout": {"data": {"totalCount": before}}}).encode(),
        export,
        json.dumps({"success": True, "ngout": {"data": {"totalCount": after}}}).encode(),
    ])
    monkeypatch.setattr(fetch, "urlopen", lambda *args, **kwargs: io.BytesIO(next(payloads)))


def test_snapshot_preserves_native_export_and_provenance(tmp_path, monkeypatch):
    payload = native_export()
    fake_responses(monkeypatch, payload)
    output = tmp_path / "snapshot"
    metadata = fetch.fetch_snapshot(output, "*:*")
    assert (output / "ast.tsv").read_bytes() == payload
    assert json.loads((output / "snapshot.json").read_text()) == metadata
    assert metadata["rows"] == metadata["count_before"] == metadata["count_after"] == 1
    assert metadata["source_version"] == "ast-browser-sha256:" + metadata["sha256"]
    assert metadata["bytes"] == len(payload)
    assert metadata["sha256"] == hashlib.sha256(payload).hexdigest()


def test_snapshot_checksum_supports_python310(tmp_path, monkeypatch):
    monkeypatch.delattr(hashlib, "file_digest", raising=False)
    payload = native_export()
    fake_responses(monkeypatch, payload)
    metadata = fetch.fetch_snapshot(tmp_path / "snapshot", "*:*")
    assert metadata["sha256"] == hashlib.sha256(payload).hexdigest()


@pytest.mark.parametrize("payload,before,after,match", [
    (native_export(), 2, 2, "incomplete"),
    (native_export(), 1, 2, "count changed"),
    (native_export(("same", "same")), 2, 2, "duplicate row ID"),
    (native_export(("",)), 1, 1, "missing or duplicate"),
    (b"<html>Service unavailable</html>", 1, 1, "header differs"),
    (native_export(()) + b"short\n", 1, 1, "ragged row"),
])
def test_bad_exports_never_publish_snapshot(tmp_path, monkeypatch, payload, before, after, match):
    fake_responses(monkeypatch, payload, before, after)
    output = tmp_path / "snapshot"
    with pytest.raises(ValueError, match=match):
        fetch.fetch_snapshot(output, "*:*")
    assert not output.exists()
    assert list(tmp_path.iterdir()) == []


def test_existing_snapshot_is_not_overwritten(tmp_path):
    output = tmp_path / "snapshot"
    output.mkdir()
    (output / "ast.tsv").write_bytes(b"previous snapshot")
    with pytest.raises(ValueError, match="already exists"):
        fetch.fetch_snapshot(output, "*:*")
    assert (output / "ast.tsv").read_bytes() == b"previous snapshot"


def test_curated_drug_map_is_pinned_to_snapshot_and_current_structures():
    from evaluate_ncbi_ast import corpus_name_candidates, read_drug_map

    root = Path(__file__).resolve().parents[1]
    snapshot = json.loads((root / "research/2026-10-03-ncbi-ast-snapshot.json").read_text())
    _, structure_keys = corpus_name_candidates(root)
    mappings = read_drug_map(
        root / "curation/ncbi_ast_drug_map.tsv", structure_keys, snapshot["source_version"],
    )
    assert any(row["mapping_status"] == "EXACT" for row in mappings.values())
    for name in ("gentamicin", "kanamycin", "colistin", "trimethoprimsulfamethoxazole"):
        assert mappings[name]["mapping_status"] != "EXACT"

"""Documentation must not promote source scores, references or reuse rights."""

import base64
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_fungamr_documentation as audit  # noqa: E402


def readme_payload(text="Documentation only\n"):
    data = text.encode()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    return {
        "encoding": "base64",
        "path": "README.md",
        "name": "README.md",
        "type": "file",
        "size": len(data),
        "sha": blob,
        "content": base64.b64encode(data).decode(),
        "html_url": "https://github.com/example/repository/blob/main/README.md",
    }, blob


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "encoding",
        "path",
        "name",
        "type",
        "size",
        "boolean_size",
        "sha",
        "host",
        "repository",
        "content",
        "invalid_base64",
    ],
)
def test_readme_envelope_and_blob_identity(change):
    payload, blob = readme_payload()
    if change in {"encoding", "path", "name", "type", "sha"}:
        payload[change] = "OTHER"
    elif change == "size":
        payload["size"] += 1
    elif change == "boolean_size":
        payload["size"] = True
    elif change == "host":
        payload["html_url"] = payload["html_url"].replace("github.com", "example.org")
    elif change == "repository":
        payload["html_url"] = payload["html_url"].replace("repository/", "other/")
    elif change == "content":
        payload["content"] = base64.b64encode(b"Changed content\n").decode()
    elif change == "invalid_base64":
        payload["content"] += "!"
    if change != "none":
        with pytest.raises(ValueError):
            audit.decode_readme(payload, "example/repository", blob)
    else:
        assert audit.decode_readme(payload, "example/repository", blob) == "Documentation only\n"


@pytest.mark.parametrize("change", ["none", "missing", "duplicate", "unknown", "empty", "extra_cell"])
def test_method_table_is_complete_without_measurement_promotion(change):
    rows = ["| Confidence Score | Description |", "|-----|-----|"]
    rows += [f"| {key} | Synthetic description |" for key in audit.METHODS]
    if change == "missing":
        rows.pop()
    elif change == "duplicate":
        rows.append(rows[-1])
    elif change == "unknown":
        rows.append("| 9 | Not reviewed |")
    elif change == "empty":
        rows[-1] = "| Negative scores (-) | |"
    elif change == "extra_cell":
        rows[-1] += " EXTRA |"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_methods("\n".join(rows))
        return
    projected = audit.project_methods("\n".join(rows))
    assert len(projected["categories"]) == 9
    assert projected["categories"]["8"]["method"] == "NATURAL_ISOLATE_COOCCURRENCE"
    assert (
        projected["categories"]["Negative scores (-)"]["method"] == "NEGATIVE_RESULT_FOR_CORRESPONDING_METHOD"
    )
    assert all(value is False for key, value in projected.items() if key != "categories")
    assert "Synthetic description" not in json.dumps(projected)


@pytest.mark.parametrize("change", ["none", "url", "attempt", "retry", "status", "hash", "size"])
def test_native_receipts_preserve_unfollowed_redirect(tmp_path, change):
    url = audit.URLS["publisher"]
    body = tmp_path / "publisher-response.bin"
    body.write_bytes(b"redirect, not primary text")
    attempt = {"url": url}
    receipt = {
        "url": url,
        "status": 303,
        "retry_performed": False,
        "sha256": audit.reference.digest(body),
        "bytes": body.stat().st_size,
        "retrieved_at": "2026-10-14T01:34:13Z",
    }
    if change == "url":
        receipt["url"] = "https://example.org/alternate"
    elif change == "attempt":
        attempt["url"] += "?retry"
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "status":
        receipt["status"] = 200
    elif change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "size":
        receipt["bytes"] += 1
    (tmp_path / "publisher-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "publisher-receipt.json").write_text(json.dumps(receipt))
    if change != "none":
        with pytest.raises(ValueError):
            audit.context.native(tmp_path, tmp_path, "publisher", url, statuses=(303,))
    else:
        assert audit.context.native(tmp_path, tmp_path, "publisher", url, statuses=(303,))["status"] == 303


def test_saved_assessment_preserves_rights_and_biological_boundaries():
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert set(saved["terms"]) == set(audit.cohort_audit.GENES)
    assert len(saved["records"]) == 10
    assert len(saved["evidence_categories"]["categories"]) == 9
    assert saved["reuse_gate"]["companion_readme_declared_license"] == "CC-BY-NC-ND-4.0"
    assert saved["reuse_gate"]["destination_data_license"] == "CC-BY-4.0"
    assert saved["reuse_gate"]["repository_api_is_permission"] is False
    assert saved["reuse_gate"]["source_queue_changed"] is False
    assert saved["reuse_gate"]["existing_aro_assertions_relicensed_or_removed"] is False
    assert saved["publisher_access"] == {
        "status": 303,
        "redirect_followed": False,
        "primary_full_text_read": False,
        "retry_performed": False,
    }
    for row in saved["terms"].values():
        assert row["primary_row_crosswalk_verified"] is False
        assert all(
            row[key] is None
            for key in (
                "fungamr_row_id",
                "source_score",
                "new_uniprot_assignment",
                "new_taxon_assignment",
                "exact_allele_assignment",
                "experimental_genome_assignment",
            )
        )
    for key in (
        "database_rows_downloaded",
        "new_resistance_assertions",
        "biological_records_changed",
        "whole_record_reviews_completed",
    ):
        assert saved["summary"][key] == 0


@pytest.mark.skipif(not (ROOT / audit.CACHE).exists(), reason="native documentation cache is local-only")
def test_native_documentation_replay(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("offline replay must not use network")

    monkeypatch.setattr(socket, "socket", deny)
    import requests

    monkeypatch.setattr(requests.sessions.Session, "request", deny)
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    for key, repository in (
        ("repository-readme", "Landrylab/FungAMR"),
        ("tool-readme", "nmquijada/ChroQueTas"),
    ):
        source = saved["sources"][key]
        native = audit.context.native(ROOT, ROOT / audit.CACHE, key, audit.URLS[key])
        assert all(native[field] == value for field, value in source.items() if field in native)
        payload = json.loads(audit.reference.check_pin(ROOT, source["body"]).read_bytes())
        decoded = audit.decode_readme(payload, repository, audit.BLOBS[key])
        assert hashlib.sha256(decoded.encode()).hexdigest() == source["decoded_sha256"]
        if key == "repository-readme":
            assert audit.project_methods(decoded) == saved["evidence_categories"]

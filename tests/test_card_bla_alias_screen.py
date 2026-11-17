"""Discovery matches and access challenges must not become experimental evidence."""

import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_bla_alias_screen as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.mark.parametrize(
    "name,field,expected",
    [
        ("blaSCO-1", "geneName", True),
        ("BLAsco-1", "synonyms", True),
        ("blaSCO-1", "orderedLocusNames", False),
        ("SCO-1", "geneName", False),
        ("blaSCO-10", "geneName", False),
        ("bla-SCO-1", "geneName", False),
        ("blaSCO 1", "geneName", False),
        ("blablaSCO-1", "geneName", False),
    ],
)
def test_exact_prefix_discovery_only(name, field, expected):
    entry = {"genes": [{field: {"value": name} if field == "geneName" else [{"value": name}]}]}
    result = audit.native_matches(entry, "SCO-1")
    assert bool(result) is expected
    if expected:
        assert result == [{"gene_index": 0, "field": field, "value": name}]


def test_empty_gene_fields_do_not_create_matches():
    assert not audit.native_matches({}, "SCO-1")
    assert not audit.native_matches({"genes": [{}]}, "SCO-1")


@pytest.fixture
def challenge():
    payload = b"<html><head><title>Just a moment...</title></head></html>"
    receipt = {
        "url": audit.URL,
        "status": 403,
        "retry_performed": False,
        "redirects_followed": False,
        "headers": {"Cf-Mitigated": "challenge"},
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    return payload, receipt


def test_challenge_is_an_access_hold_not_biological_evidence(challenge):
    result = audit.primary_hold(*challenge)
    assert result["http_status"] == 403
    for key in (
        "challenge_treated_as_primary",
        "primary_results_reviewed",
        "retrieved_primary_text",
        "retry_performed",
        "alternate_route_used",
        "hold_is_biological_negative_result",
        "permanent_unavailability_inferred",
    ):
        assert result[key] is False


@pytest.mark.parametrize(
    "field,value",
    [
        ("url", "https://europepmc.org/articles/PMC1"),
        ("status", 200),
        ("retry_performed", True),
        ("redirects_followed", True),
        ("headers", {}),
        ("sha256", "changed"),
        ("bytes", 1),
    ],
)
def test_challenge_guard(challenge, field, value):
    payload, receipt = challenge
    receipt[field] = value
    with pytest.raises(ValueError, match="challenge identity"):
        audit.primary_hold(payload, receipt)


@pytest.mark.parametrize(
    "payload",
    [
        b"<html><title>Actual article</title></html>",
        b'<html><title>Just a moment...</title><meta name="citation_doi" content="10.1000/test"></html>',
    ],
)
def test_ambiguous_article_response_is_not_silently_classified(challenge, payload):
    receipt = challenge[1]
    receipt.update({"sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload)})
    with pytest.raises(ValueError, match="challenge identity"):
        audit.primary_hold(payload, receipt)


def test_public_screen_preserves_discovery_scope():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["scope"] == audit.SCOPE
    assert result["summary"] == {
        "terms_screened": 726,
        "source_pmids": 650,
        "query_statuses": {"COMPLETE_QUERY_NOT_PRIMARY_REVIEW": 650},
        "candidate_terms": 3,
        "candidate_term_protein_pairs": 4,
        "previously_reviewed_reference_pairs": 2,
        "new_discovery_pairs": 2,
        "candidate_records_read": 11,
        "candidate_source_claims": 13,
        "corpus_records_hash_checked": 2939,
    }
    new = [r for r in result["candidates"].values() if not r["previously_reviewed_reference"]]
    assert {r["identity"]["protein_accession"] for r in new} == {"UniProtKB:Q0GA57", "UniProtKB:G3K399"}
    assert all(r["native_citation_and_taxonomy_review_pending"] for r in new)
    assert all(r["experimental_subject_assignment"] is False for r in result["candidates"].values())
    assert result["limits"]["new_reference_or_experimental_assignments"] == 0
    assert result["limits"]["candidate_free_is_biological_absence"] is False
    assert result["limits"]["network_requests"] == 1 and result["limits"]["screen_network_requests"] == 0
    assert result["limits"]["ncbi_requests"] == 0


def test_cli_exclusive_output_and_check(tmp_path, monkeypatch):
    output = tmp_path / "screen.json"
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.exists()
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("different\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()

"""Publisher routing and licensing metadata must not become primary evidence."""

import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import quote

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_thevissen_2007_access as audit  # noqa: E402


def metadata():
    return {"status": "ok", "message-type": "work", "message": {
        "DOI": audit.DOI.lower(), "title": ["Cited study"], "publisher": "Publisher",
        "resource": {"primary": {"URL": audit.PUBLISHER}},
        "license": [{"content-version": "vor", "URL": "http://creativecommons.org/licenses/by/4.0/"},
                    {"content-version": "tdm", "URL": "https://example.org/tdm"}],
    }}


def routing(url=audit.PRIMARY, title="Redirecting", duplicate=False):
    target = '<input id="redirectURL" value="' + quote(url, safe="") + '">'
    return ('<html><head><title>' + title + '</title><meta name="tdm-reservation" content="1">'
            '</head><body>' + target * (2 if duplicate else 1) + '</body></html>').encode()


def hold():
    return {"url": audit.PRIMARY, "status": 403, "headers": {"Cf-Mitigated": "challenge"},
            "retry_performed": False, "retrieved_at": "2026-10-14T10:43:17.613715+00:00"}


def test_license_metadata_retains_content_versions_without_access_or_adoption_inference():
    payload = metadata()
    projected = audit.project_metadata(payload)
    assert projected["licenses_as_deposited"] == payload["message"]["license"]
    assert not projected["primary_results_reviewed"]
    assert not projected["source_adoption_authorized"]
    assert not projected["access_availability_inferred_from_license"]


@pytest.mark.parametrize("change", ["status", "type", "doi", "missing_doi", "url", "titles"])
def test_bibliographic_identity_fails_closed(change):
    payload = metadata()
    if change == "status":
        payload["status"] = "error"
    elif change == "type":
        payload["message-type"] = "work-list"
    elif change == "doi":
        payload["message"]["DOI"] = "10.1074/other"
    elif change == "missing_doi":
        del payload["message"]["DOI"]
    elif change == "url":
        payload["message"]["resource"]["primary"]["URL"] = "https://example.org/other"
    else:
        payload["message"]["title"] *= 2
    with pytest.raises(ValueError, match="identity"):
        audit.project_metadata(payload)


def test_ordinary_routing_identifies_exact_destination_without_article_text():
    assert audit.routing_destination(routing()) == audit.PRIMARY


@pytest.mark.parametrize("change", ["url", "title", "duplicate", "tdm"])
def test_routing_is_not_a_generic_redirect_or_challenge_handler(change):
    body = routing(url="https://example.org/other") if change == "url" else routing(
        title="Just a moment" if change == "title" else "Redirecting", duplicate=change == "duplicate")
    if change == "tdm":
        body = body.replace(b'content="1"', b'content="0"')
    with pytest.raises(ValueError, match="routing"):
        audit.routing_destination(body)


def test_challenge_hold_does_not_establish_primary_results_or_global_inaccessibility():
    result = audit.project_hold(hold())
    assert result["status"] == "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY"
    assert not result["primary_results_reviewed"] and not result["alternate_route_attempted"]
    assert not result["global_inaccessibility_inferred"]


@pytest.mark.parametrize("change", ["url", "200", "404", "retry", "challenge"])
def test_hold_must_match_the_observed_status_and_stop_boundary(change):
    receipt = hold()
    if change in ("200", "404"):
        receipt["status"] = int(change)
    elif change == "url":
        receipt["url"] = audit.PUBLISHER
    elif change == "retry":
        receipt["retry_performed"] = True
    else:
        receipt["headers"] = {}
    with pytest.raises(ValueError, match="challenge"):
        audit.project_hold(receipt)


@pytest.mark.parametrize("change", [None, "body", "bytes", "status", "retry", "url", "plan_url",
                                    "redirect", "limit", "time"])
def test_native_plan_receipt_and_payload_are_bound(tmp_path, monkeypatch, change):
    body = b"native response fixture"
    checksum = hashlib.sha256(body).hexdigest()
    monkeypatch.setitem(audit.NATIVE_SHA, "crossref", checksum)
    plan = {"url": audit.METADATA, "redirects_followed": False, "max_bytes": 1024}
    attempt = {"url": audit.METADATA, "started_at": "2026-10-14T10:00:00+00:00"}
    receipt = {"url": audit.METADATA, "status": 200, "retry_performed": False,
               "sha256": checksum, "bytes": len(body), "retrieved_at": "2026-10-14T10:00:01+00:00"}
    if change == "body":
        body += b"changed"
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "status":
        receipt["status"] = 403
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "url":
        attempt["url"] = audit.PRIMARY
    elif change == "plan_url":
        plan["url"] = audit.PRIMARY
    elif change == "redirect":
        plan["redirects_followed"] = True
    elif change == "limit":
        plan["max_bytes"] = 1
    elif change == "time":
        attempt["started_at"] = "2026-10-14T10:01:00+00:00"
    for kind, value in (("plan", plan), ("attempt", attempt), ("receipt", receipt)):
        (tmp_path / f"crossref-{kind}.json").write_text(json.dumps(value))
    (tmp_path / "crossref-response.bin").write_bytes(body)
    if change is None:
        result = audit.planned_native(tmp_path, tmp_path, "crossref", audit.METADATA, 200)
        assert result["body"]["sha256"] == checksum
    else:
        with pytest.raises(ValueError):
            audit.planned_native(tmp_path, tmp_path, "crossref", audit.METADATA, 200)


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_dossier_preserves_review_boundaries(dossier):
    assert dossier["scope"] == audit.SCOPE
    assert dossier["summary"] == {
        "corpus_record_hashes_checked": 2939, "target_records_loaded": 2,
        "new_network_requests": 3, "new_access_holds": 1, "primary_results_reviewed": 0,
        "new_reference_proteins": 0, "biological_record_changes": 0,
        "experimental_allele_assignments": 0, "whole_record_reviews_completed": 0,
    }
    assert {row["identifier"] for row in dossier["records"]} == {
        "CHEBI:88298", "antibioticmech:aro-11ab0a98bf"}
    assert dossier["reused_literature_metadata"]["flags"]["inEPMC"] == "N"
    assert dossier["routing_page"]["status"] == 200 and not dossier["routing_page"]["article_text"]
    assert dossier["sources"]["primary"]["status"] == 403
    assert dossier["constraints"]["ncbi_requests"] == 0
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert dossier["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert not dossier["constraints"]["held_sources_retried"]


def test_offline_native_replay(dossier, monkeypatch, capsys, pre_card_qualification_root):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline access audit attempted a network request")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.chdir(pre_card_qualification_root)
    monkeypatch.setattr(sys, "argv", [audit.__name__, "--check", "--historical-records"])
    audit.main()
    assert json.loads(capsys.readouterr().out) == dossier["summary"]

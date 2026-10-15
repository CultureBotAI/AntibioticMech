"""Species names and empty queries cannot establish experimental resistance identities."""

import copy
import csv
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mdea_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_portable_checkpoint_keeps_all_seven_current_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    plan = audit.common.read_json(ROOT, result["plan"])
    index = audit.common.read_json(ROOT, result["inputs"]["index"])
    assert result["claims"] == [c for c in index["claims"] if c["aro_id"] == audit.TERM]
    assert result["records"] == plan["records"]
    assert len(result["claims"]) == len(result["records"]) == 7
    assert result["summary"]["corpus_records_hash_checked"] == 2939
    assert result["reference_candidates"] == {}
    assert result["limits"]["experimental_identity_assignments"] == 0
    assert result["limits"]["exact_allele_assignments"] == 0
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["primary_fulltext_inspected"] is False


def test_species_search_rejects_nonexact_taxa_and_does_not_assign_a_strain():
    result = public_result()
    crosswalk = result["species_name_crosswalk"]
    accepted = [c for c in crosswalk["candidates"] if c["exact_name_fields"]]
    assert len(accepted) == 1 and len(crosswalk["candidates"]) == 4
    assert accepted[0]["scientific_name"] == audit.NAME
    assert accepted[0]["taxon_id"] == crosswalk["named_organism_taxon_id"] == "NCBITaxon:1309"
    assert accepted[0]["rank"] == "species" and accepted[0]["active"] is True
    assert crosswalk["experimental_organism_assignment"] is crosswalk["strain_or_genome_assigned"] is False
    assert result["study_context"]["heterologous_test_context_reported"] is True
    assert result["study_context"]["native_organism_resistance_inferred"] is False
    assert (
        result["web_tools"]["different_species_title_lead_not_used"] == "https://doi.org/10.1248/bpb.29.801"
    )


def test_transport_failure_is_not_an_access_denial_or_unrequested_paper():
    failure = public_result()["publisher_attempt"]
    assert failure["status"] == "TRANSPORT_FAILURE_NO_HTTP_RESPONSE_NOT_AN_ACCESS_DENIAL"
    assert failure["http_status"] is None
    for key in (
        "access_denial_established",
        "paywall_inferred",
        "global_unavailability_inferred",
        "fulltext_inspected",
        "retry_performed",
        "alternate_fulltext_route_requested",
    ):
        assert failure[key] is False
    assert failure["attempt"] and failure["error"]
    assert failure["doi"]["status"] == 302
    assert failure["http_to_https_upgrade_before_request"] is True
    assert failure["doi"]["headers"]["location"] == audit.PUBLISHER.replace("https://", "http://", 1)
    assert public_result()["summary"]["new_native_request_attempts"] == 6
    assert public_result()["summary"]["native_http_responses"] == 5


@pytest.mark.parametrize(
    "error",
    [
        {"error_type": "ConnectionError", "retried": True},
        {"error_type": "HTTPError", "retried": False},
        {"error_type": "ConnectionError", "retried": False, "status": 403},
        {"error_type": "Timeout", "retried": False},
    ],
)
def test_changed_failure_or_http_status_requires_new_review(error):
    with pytest.raises(ValueError, match="transport"):
        audit.failure_disposition(error)


@pytest.mark.parametrize("change", ["release", "total", "pagination", "redirect", "entry", "suggestion"])
def test_empty_query_rejects_changed_or_partial_results(change):
    source = {"headers": {"x-uniprot-release": "2026_03", "x-total-results": "0"}}
    payload = {"results": []}
    if change == "release":
        source["headers"]["x-uniprot-release"] = "2026_04"
    elif change == "total":
        source["headers"]["x-total-results"] = "1"
    elif change in {"pagination", "redirect"}:
        source["headers"]["link" if change == "pagination" else "location"] = "https://example.org"
    elif change == "entry":
        payload["results"] = [{"primaryAccession": "Q00001"}]
    else:
        payload["suggestions"] = [{"query": "another species"}]
    with pytest.raises(ValueError):
        audit.empty_query(json.dumps(payload).encode(), source)


def test_empty_query_projection_is_pure_and_not_absence():
    source = {"headers": {"x-uniprot-release": "2026_03", "x-total-results": "0"}}
    before = copy.deepcopy(source)
    result = audit.empty_query(b'{"results": []}', source)
    assert source == before
    assert result["complete_for_exact_query"] is True
    assert result["establishes_biological_absence"] is False
    assert result["accession_assigned"] is None
    for kind in ("reviewed", "unreviewed"):
        projected = public_result()["protein_queries"][kind]
        assert projected["result_count"] == 0 and projected["establishes_biological_absence"] is False


@pytest.mark.parametrize("change", ["url", "status", "retry", "redirect", "attempt", "bytes", "checksum"])
def test_native_response_identity_and_integrity(tmp_path, change):
    body = tmp_path / "response.bin"
    body.write_bytes(b'{"results": []}')
    receipt = {
        "url": "https://rest.uniprot.org/uniprotkb/search",
        "status": 200,
        "retries": 0,
        "redirects_followed": 0,
        "bytes": body.stat().st_size,
        "body": audit.reference.pin(tmp_path, body),
    }
    attempt = {"url": receipt["url"], "retries": 0, "redirects_followed": 0, "ncbi_requests": 0}
    if change == "url":
        receipt["url"] = "https://example.org"
    elif change == "status":
        receipt["status"] = 403
    elif change == "retry":
        receipt["retries"] = 1
    elif change == "redirect":
        receipt["redirects_followed"] = 1
    elif change == "attempt":
        attempt["url"] = "https://example.org"
    elif change == "bytes":
        receipt["bytes"] += 1
    else:
        receipt["body"]["sha256"] = "0" * 64
    receipt_path, attempt_path = tmp_path / "receipt.json", tmp_path / "attempt.json"
    receipt_path.write_text(json.dumps(receipt))
    attempt_path.write_text(json.dumps(attempt))
    native = {
        "requests": {"test": audit.reference.pin(tmp_path, receipt_path)},
        "attempts": {"test": audit.reference.pin(tmp_path, attempt_path)},
    }
    with pytest.raises(ValueError):
        audit.native_http(tmp_path, native, "test", "https://rest.uniprot.org/uniprotkb/search", 200)


def test_no_operational_or_experimental_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(public_result())) & {
        "sequence",
        "features",
        "alteration",
        "variants",
        "gene_id",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "abstractText",
    }


def test_offline_replay_when_native_cache_and_current_checkpoint_available():
    native = json.loads((ROOT / audit.PLAN).read_bytes())
    if any(not (ROOT / p["path"]).exists() for p in native["requests"].values()):
        pytest.skip("native cache unavailable; portable checks still run")
    plan = audit.common.read_json(ROOT, native["plan"])
    update = audit.common.read_json(ROOT, plan["inputs"]["corpus_update"])
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with audit.reference.check_pin(ROOT, plan["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (ROOT / r["path"]).exists()
        or audit.reference.digest(ROOT / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.skip("historical record checkpoint; portable checks still run")
    assert audit.build(ROOT) == public_result()

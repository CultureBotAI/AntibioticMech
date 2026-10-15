"""Bibliography and gene symbols are not tested-allele or pump-composition proof."""

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
import audit_mex_citation_followup as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_cohort_is_complete_without_native_cache_or_live_records(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.mex.read_json(ROOT, result["prior"])
    assert set(result["terms"]) == {
        t for t, r in prior["terms"].items() if not r["all_label_components_have_native_annotations"]
    }
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] in result["terms"]]
    assert result["summary"] == {
        "corpus_records_hash_checked": 2939,
        "complete_records_read_in_prior_replay": 27,
        "selected_records": 18,
        "selected_claims": 34,
        "selected_terms": 9,
        "cached_citation_queries_replayed": 11,
        "citation_pool_entries": 8,
        "reference_candidates": 7,
        "new_reference_candidates": 5,
        "new_native_http_requests": 5,
        "new_taxonomy_requests": 0,
        "new_primary_access_holds": 1,
        "web_search_calls": 2,
        "underlying_web_http_request_count_known": False,
    }
    assert len(result["records"]) == 18 and len(result["claims"]) == 34
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_adjacent_paper_is_not_promoted_to_own_definition_citation():
    terms = public_result()["terms"]
    mn, pq = terms["ARO:3003703"], terms["ARO:3003697"]
    assert mn["definition_citation_ids"] == ["PMID:19713238"]
    assert mn["adjacent_citation_lead"] == "PMID:16301811"
    assert {c["gene_symbol"] for c in mn["component_candidates"]} == {"mexM", "mexN"}
    assert {c["gene_symbol"] for c in pq["component_candidates"]} == {"mexP", "mexQ", "opmE"}
    for candidate in mn["component_candidates"]:
        assert candidate["own_definition_citations"] == []
        assert candidate["adjacent_followup_citations"] == ["PMID:16301811"]
    for candidate in pq["component_candidates"]:
        assert candidate["own_definition_citations"] == ["PMID:16301811"]
        assert candidate["adjacent_followup_citations"] == []
    for term in (mn, pq):
        assert term["exact_experimental_complex_assignment"] is False
        assert all(c["complex_membership_proven"] is False for c in term["component_candidates"])


def test_species_candidates_remain_versioned_and_nonexperimental():
    result = public_result()
    for ref in result["reference_candidates"].values():
        assert ref["reference_taxonomy"]["taxon_id"] == "NCBITaxon:287"
        assert ref["reference_taxonomy"]["native_rank"] == "species"
        assert ref["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        assert ref["entry_audit"]["entryVersion"] > 0 and ref["entry_audit"]["sequenceVersion"] == 1
        assert ref["experimental_subject_assignment"] is ref["exact_allele_assignment"] is False
        assert ref["experimental_genome_assignment"] is None
    reused = {a for a, r in result["reference_candidates"].items() if r["already_in_prior_mex_dossier"]}
    assert reused == {"UniProtKB:I0IYR4", "UniProtKB:I0IYR5"}


def test_regulator_and_suggested_different_gene_names_do_not_fill_component_gaps():
    result = public_result()
    assert result["excluded_citation_entry"]["accession"] == "UniProtKB:I0IYR3"
    assert result["excluded_citation_entry"]["native_gene_symbol"] == "mexZ"
    assert "UniProtKB:I0IYR3" not in result["reference_candidates"]
    assert result["new_empty_symbol_queries"]["mexj-canary"]["native_suggestion_count"] == 2
    for query in result["new_empty_symbol_queries"].values():
        assert query["result_count"] == 0 and query["complete_for_exact_query"] is True
        assert query["suggestions_followed"] is query["biological_absence_inferred"] is False
    assert result["reused_opmh_query"]["result_count"] == 0
    assert result["reused_opmh_query"]["biological_absence_inferred"] is False


def test_no_citation_match_does_not_inherit_adjacent_reference_automatically():
    term = {
        "source_label": "MexMN-OprM",
        "complex_label": "MexMN-OprM",
        "component_search_symbols": ["mexM"],
        "definition_citation_ids": ["PMID:2"],
        "record_memberships": [],
    }
    entry = {"genes": [{"geneName": {"value": "mexM"}}]}
    entries, pools = {"EXAMPLE": entry}, {"1": {"EXAMPLE": entry}, "2": {}}
    assert audit.project_term(term, pools, entries)["component_candidates"] == []
    assert len(audit.project_term(term, pools, entries, "PMID:1")["component_candidates"]) == 1
    with pytest.raises(ValueError, match="mislabeled"):
        audit.project_term(term, pools, entries, "PMID:2")
    entry["genes"][0]["geneName"]["value"] = "mexZ"
    assert audit.project_term(term, pools, entries, "PMID:1")["component_candidates"] == []


def metadata_fixture():
    return {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:16301811 AND SRC:MED", "resultType": "CORE", "pageSize": 1},
        "resultList": {
            "result": [
                {
                    "id": "16301811",
                    "pmid": "16301811",
                    "source": "MED",
                    "doi": audit.DOI,
                    "isOpenAccess": "N",
                    "inEPMC": "N",
                    "title": public_result()["publication"]["title"],
                    "abstractText": "MexPQ-OpmE and MexMN-OprM",
                    "fullTextUrlList": {"fullTextUrl": [{"url": "https://doi.org/" + audit.DOI}]},
                }
            ]
        },
    }


@pytest.mark.parametrize(
    "change", ["query", "count", "pagination", "pmid", "doi", "source", "title", "abstract"]
)
def test_publication_identity_or_scope_drift_fails_closed(change):
    payload = metadata_fixture()
    row = payload["resultList"]["result"][0]
    if change == "query":
        payload["request"]["queryString"] = "different"
    elif change == "count":
        payload["hitCount"] = 2
    elif change == "pagination":
        payload["nextCursorMark"] = "next"
    else:
        row["abstractText" if change == "abstract" else change] = "different"
    with pytest.raises(ValueError):
        audit.project_metadata(payload)


def test_metadata_projection_does_not_turn_index_flags_into_global_denial():
    payload = metadata_fixture()
    before = copy.deepcopy(payload)
    result = audit.project_metadata(payload)
    assert payload == before
    assert result["index_access_flags_are_not_global_access_or_reuse_decisions"] is True
    assert result["quantitative_phenotype_or_experimental_identity_exported"] is False


def test_hold_comes_from_publisher_http_status_not_index_access_flags():
    access = public_result()["publication"]["access"]
    assert access["status"] == "PUBLISHER_HTTP403_HELD_NO_RETRY_OR_ALTERNATE_ROUTE"
    assert access["sources"]["doi"]["status"] == 302
    assert access["sources"]["doi"]["headers"]["location"] == audit.PUBLISHER
    assert access["sources"]["publisher"]["status"] == 403
    assert access["sources"]["publisher"]["url"] == audit.PUBLISHER
    assert access["manual_doi_redirects_followed"] == 1
    assert access["fulltext_inspected"] is False
    assert access["revisit_requires_new_direction_or_supplied_copy"] is True
    assert all(s["redirects_followed"] == s["retries"] == 0 for s in access["sources"].values())


@pytest.mark.parametrize("change", ["status", "url", "bytes", "redirects_followed", "retries", "body"])
def test_native_http_receipts_fail_closed(tmp_path, change):
    path = tmp_path / "body.bin"
    path.write_bytes(b"access denied")
    receipt = {
        "url": audit.PUBLISHER,
        "status": 403,
        "bytes": path.stat().st_size,
        "redirects_followed": 0,
        "retries": 0,
        "body": audit.reference.pin(tmp_path, path),
    }
    if change == "url":
        receipt["url"] = "https://example.org"
    elif change != "body":
        receipt[change] += 1
    record = tmp_path / "receipt.json"
    record.write_text(json.dumps(receipt))
    if change == "body":
        path.write_bytes(b"changed")
    with pytest.raises(ValueError):
        audit.native_http(tmp_path, audit.reference.pin(tmp_path, record), audit.PUBLISHER, 403)


def test_public_artifact_pins():
    receipt = json.loads((ROOT / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 3
    for item in pins:
        audit.reference.check_pin(ROOT, item)
    assert receipt["summary"] == public_result()["summary"]


def test_offline_replay_when_native_cache_and_current_checkpoint_available():
    native = json.loads((ROOT / audit.PLAN).read_bytes())
    if any(not (ROOT / p["path"]).exists() for p in native["requests"].values()):
        pytest.skip("native cache unavailable; portable public checks still run")
    prior = audit.mex.read_json(ROOT, public_result()["prior"])
    update = audit.mex.read_json(ROOT, prior["explicit_corpus_update"])
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with audit.reference.check_pin(ROOT, prior["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (ROOT / r["path"]).exists()
        or audit.reference.digest(ROOT / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.skip("historical record checkpoint; portable public checks still run")
    assert audit.build(ROOT) == public_result()

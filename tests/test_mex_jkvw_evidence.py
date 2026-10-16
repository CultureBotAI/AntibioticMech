"""Access holds and publication metadata do not establish resistant alleles."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mex_jkvw_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_portable_public_checkpoint_preserves_all_selected_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.followup.mex.read_json(ROOT, result["prior_followup"])
    assert set(result["terms"]) == {
        t for t, r in prior["terms"].items() if r["complex_label"] in audit.COMPLEXES
    }
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] in result["terms"]]
    assert len(result["claims"]) == 8 and len(result["records"]) == 5
    assert len(result["terms"]) == len(result["publications"]) == 4
    assert result["summary"]["corpus_records_hash_checked"] == 2939
    assert result["summary"]["new_reference_candidates"] == 0
    assert result["limits"]["new_uniprot_requests"] == result["limits"]["new_taxonomy_requests"] == 0
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert (
        result["limits"]["issue_1040"] == "DEFERRED" and result["limits"]["full_corpus_goal_status"] == "OPEN"
    )
    for term in result["terms"].values():
        assert term["experimental_accession_assignment"] is None
        assert term["curation_supported_by_this_pass"] is False
        assert term["publication_pointers"] == [
            "/publications/" + p[5:] for p in term["definition_citation_ids"]
        ]


def test_two_denials_are_distinct_from_two_unrequested_papers():
    papers = public_result()["publications"]
    for pmid in audit.PMIDS[:2]:
        access = papers[pmid]["access"]
        assert access["status"] == "HTTP403_ACCESS_HOLD_NO_RETRY_OR_ALTERNATE_ROUTE"
        assert access["source"]["status"] == 403
        assert access["source"]["retries"] == access["source"]["redirects_followed"] == 0
        assert access["requires_new_direction_or_supplied_copy"] is True
    for pmid in audit.PMIDS[2:]:
        access = papers[pmid]["access"]
        assert access["status"] == "NOT_REQUESTED_AFTER_EUROPE_PMC_PRIMARY_CANARY_DENIAL"
        assert access["access_denial_inferred"] is False
    assert all(
        p["access"]["fulltext_inspected"] is p["access"]["global_unavailability_inferred"] is False
        for p in papers.values()
    )
    assert papers["12951344"]["doi_redirect"]["status"] == 302
    assert papers["12951344"]["doi_redirect"]["headers"]["location"] == audit.VW_PUBLISHER


@pytest.mark.parametrize("pmid", audit.PMIDS[:2])
def test_hold_requires_the_actual_papers_403(pmid):
    for status in (200, 302, 404, 500):
        with pytest.raises(ValueError, match="403"):
            audit.access_disposition(pmid, {pmid: {"status": status}})


@pytest.mark.parametrize("pmid", audit.PMIDS[2:])
def test_unrequested_status_rejects_an_existing_response(pmid):
    with pytest.raises(ValueError, match="unrequested"):
        audit.access_disposition(pmid, {pmid: {"status": 403}})


def metadata_fixture():
    row = {
        "id": "12193619",
        "pmid": "12193619",
        "source": "MED",
        "doi": "10.1000/example",
        "pmcid": "PMC1",
        "title": "Example metadata",
        "isOpenAccess": "N",
        "inEPMC": "Y",
        "abstractText": "Example abstract",
        "fullTextUrlList": {"fullTextUrl": []},
    }
    expected = {k: row[k] for k in ("pmid", "doi", "pmcid", "title", "isOpenAccess", "inEPMC")}
    expected["abstract_sha256"] = hashlib.sha256(row["abstractText"].encode()).hexdigest()
    payload = {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:12193619 AND SRC:MED", "resultType": "CORE", "pageSize": 1},
        "resultList": {"result": [row]},
    }
    return payload, expected


@pytest.mark.parametrize(
    "change",
    ["count", "boolean_count", "pagination", "query", "size", "pmid", "source", "doi", "title", "abstract"],
)
def test_metadata_scope_and_identity_guards(change):
    payload, expected = metadata_fixture()
    if change in {"count", "boolean_count"}:
        payload["hitCount"] = True if change == "boolean_count" else 2
    elif change == "pagination":
        payload["nextCursorMark"] = "next"
    elif change == "query":
        payload["request"]["queryString"] = "unplanned"
    elif change == "size":
        payload["request"]["pageSize"] = True
    else:
        payload["resultList"]["result"][0]["abstractText" if change == "abstract" else change] = "changed"
    with pytest.raises(ValueError):
        audit.project_metadata(payload, "12193619", expected)


def test_metadata_projection_is_pure_and_not_experimental_evidence():
    payload, expected = metadata_fixture()
    before = copy.deepcopy((payload, expected))
    result = audit.project_metadata(payload, "12193619", expected)
    assert (payload, expected) == before
    assert result["exact_experimental_gene_or_protein_identity_established"] is False
    assert result["source_claims_reinterpreted_from_abstract"] is False
    assert result["index_access_flags_are_not_global_access_or_reuse_decisions"] is True
    assert "abstractText" not in result


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
    }


def test_public_artifact_pins():
    receipt = json.loads((ROOT / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 3
    for item in pins:
        audit.reference.check_pin(ROOT, item)
    assert receipt["summary"] == public_result()["summary"]


def test_offline_replay_when_native_cache_and_current_checkpoint_available(pre_cdsa_qualification_root):
    root = pre_cdsa_qualification_root
    native = json.loads((root / audit.PLAN).read_bytes())
    if any(not (root / p["path"]).exists() for p in native["requests"].values()):
        pytest.skip("native cache unavailable; portable public checks still run")
    plan = audit.followup.mex.read_json(root, native["plan"])
    prior = audit.followup.mex.read_json(root, plan["prior"])
    update = audit.followup.mex.read_json(root, prior["explicit_corpus_update"])
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with audit.reference.check_pin(root, prior["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (root / r["path"]).exists()
        or audit.reference.digest(root / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.fail("checksum-verified historical fixture drifted")
    assert audit.build(root) == public_result()

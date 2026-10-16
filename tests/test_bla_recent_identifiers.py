"""Guard primary-study scope, empty metadata searches and native taxonomy ranks."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_bla_recent_identifiers as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "getaddrinfo", denied)


@pytest.fixture(scope="module")
def frozen():
    pins = json.loads((ROOT / audit.PLAN).read_bytes())["inputs"]
    data = {
        k: audit.read(ROOT, p)
        for k, p in pins.items()
        if p["path"].endswith(".json") and not p["path"].startswith("reports/")
    }
    public = {
        k: audit.read(ROOT, p)
        for k, p in data["plan"]["inputs"].items()
        if p["path"].endswith(".json") and not p["path"].startswith("reports/")
    }
    doc = json.loads((ROOT / audit.OUTPUT).read_bytes())
    return pins, data, public, doc


@pytest.fixture(scope="module")
def native_frozen(frozen, require_native_inputs):
    pins, data, public, doc = frozen
    require_native_inputs(pins, data["plan"])
    data = {k: audit.read(ROOT, p) for k, p in pins.items() if p["path"].endswith(".json")}
    return pins, data, public, doc


def test_exact_offline_replay(native_frozen, pre_salmonella_qualification_root):
    assert audit.build(pre_salmonella_qualification_root) == native_frozen[3]


def test_public_summary(frozen):
    doc = frozen[3]
    assert doc["summary"] == {
        "current_corpus_hashes_verified": 2939,
        "complete_records_loaded": 9,
        "source_claims_bound": 14,
        "terms_investigated": 4,
        "selected_protein_references": 0,
        "complete_empty_protein_queries": 3,
        "primary_identity_holds": 1,
        "source_species_name_contexts": 2,
        "new_native_taxonomy_nodes": 1,
        "reused_native_taxonomy_nodes": 1,
        "new_native_requests": 4,
        "whole_record_primary_signoffs": 0,
    }


def test_memberships_and_reference_gaps_do_not_become_experimental_claims(frozen):
    _, _, public, doc = frozen
    index = public["current_index"]
    assert doc["claims"] == [c for c in index["claims"] if c["aro_id"] in audit.TERMS.values()]
    for term, row in doc["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert row["reference_accessions"] == row["references"] == []
        assert row["whole_record_primary_review"] == "OPEN"
        assert all(v is None for k, v in row.items() if k.startswith("experimental_"))
    assert doc["constraints"]["biological_record_writes"] is False
    assert doc["constraints"]["experimental_identifiers_assigned"] is False
    assert doc["constraints"]["ncbi_requests"] == 0
    assert doc["constraints"]["issue_1040"] == "DEFERRED"
    assert doc["constraints"]["native_primary_bodies_replayed"] is False
    assert doc["constraints"]["full_investigation_complete"] is False
    assert doc["terms"]["ARO:3007442"]["status"] == "PRIMARY_SOURCE_IDENTITY_HOLD"
    assert all(q["biological_absence_inferred"] is False for q in doc["queries"].values())


def test_taxonomy_is_species_name_context_not_a_strain_mapping(frozen):
    doc = frozen[3]
    wus, vim = (doc["terms"][term]["source_taxonomy_context"] for term in ("ARO:3007435", "ARO:3009643"))
    assert wus["taxon_id"] == "NCBITaxon:2562892"
    assert wus["native_name_matches"] == [{"field": "scientificName", "value": "Myroides albus"}]
    assert vim["taxon_id"] == "NCBITaxon:287"
    assert wus["rank"] == vim["rank"] == "species"
    assert wus["scope"] == vim["scope"] == "SPECIES_NAME_REFERENCE_NOT_EXPERIMENTAL_ISOLATE"
    assert doc["terms"]["ARO:3007442"]["source_taxonomy_context"] is None
    assert doc["terms"]["ARO:3007632"]["source_taxonomy_context"] is None


@pytest.mark.parametrize("key", list(audit.QUERIES))
@pytest.mark.parametrize("change", ["status", "release", "pagination", "redirect", "query", "hash", "count"])
def test_native_request_failures_cannot_become_empty_searches(native_frozen, key, change):
    pins, data, _, _ = native_frozen
    plan = copy.deepcopy(data["plan"])
    receipt, attempt = copy.deepcopy((data[key + "_receipt"], data[key + "_attempt"]))
    body = audit.reference.check_pin(ROOT, pins[key + "_response"]).read_bytes()
    if change == "status":
        receipt["status"] = 403
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "different"
    elif change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "redirect":
        receipt["redirects_followed"] = 1
    elif change == "query":
        plan["requests"][key]["query"] = "alternative"
    elif change == "hash":
        body += b" "
    else:
        receipt["headers"]["x-total-results"] = "500"
    with pytest.raises(ValueError):
        audit.validate_response(plan, key, receipt, attempt, body)


@pytest.mark.parametrize("forbidden", ["sequence", "features", "comments"])
def test_nested_nonmetadata_fields_are_rejected(native_frozen, forbidden):
    _, data, _, _ = native_frozen
    key = "wus1"
    receipt = copy.deepcopy(data[key + "_receipt"])
    body = json.dumps({"results": [{"primaryAccession": "OTHER", "nested": {forbidden: {}}}]}).encode()
    receipt["body"]["sha256"] = hashlib.sha256(body).hexdigest()
    receipt["bytes"] = len(body)
    receipt["headers"]["x-total-results"] = "1"
    with pytest.raises(ValueError, match="non-metadata"):
        audit.validate_response(data["plan"], key, receipt, data[key + "_attempt"], body)


@pytest.mark.parametrize(
    "change",
    [
        "wus_crosswalk",
        "wus_query",
        "ssa_host",
        "ssa_model",
        "fri_range",
        "fri_subject",
        "fri_namespace",
        "vim_version",
        "vim_subject",
        "ncbi",
        "complete",
        "primary_replay",
        "missing_limit",
    ],
)
def test_assessment_cannot_promote_unverified_identifiers(frozen, change):
    assessment = copy.deepcopy(frozen[2]["assessment"])
    papers = assessment["terms"]
    if change == "wus_crosswalk":
        papers["wus1"]["individual_chromosome_plasmid_crosswalk_verified"] = True
    elif change == "wus_query":
        papers["wus1"]["query_scope"] = "EXHAUSTIVE_PROTEIN_CROSSWALK"
    elif change == "ssa_host":
        papers["ssa"]["source_organism"] = "Escherichia coli"
    elif change == "ssa_model":
        papers["ssa"]["card_model_metadata_adopted"] = True
    elif change == "fri_range":
        papers["fri11"]["individual_gene_or_replicon_assigned_from_range"] = True
    elif change == "fri_subject":
        papers["fri11"]["additional_primary"]["same_subject_as_card_cited_clinical_study"] = True
    elif change == "fri_namespace":
        papers["fri11"]["additional_primary"]["source_protein_namespace"] = "UniProtKB"
    elif change == "vim_version":
        papers["vim92"]["source_accession_version_reported"] = True
    elif change == "vim_subject":
        papers["vim92"]["primary_analysis_strain"] = "PAO1"
    elif change == "ncbi":
        assessment["constraints"]["issue_1040"] = "RESUMED"
    elif change == "complete":
        assessment["constraints"]["full_investigation_complete"] = True
    elif change == "missing_limit":
        del assessment["constraints"]["native_primary_bodies_replayed"]
    else:
        assessment["constraints"]["native_primary_bodies_replayed"] = True
    with pytest.raises(ValueError):
        audit.validate_assessment(assessment)


@pytest.mark.parametrize("change", ["active", "rank", "parent", "name", "taxon", "duplicate", "protein"])
def test_source_taxonomy_requires_exact_native_context(native_frozen, change):
    pins, data, _, _ = native_frozen
    responses = {
        key: json.loads(audit.reference.check_pin(ROOT, pins[key + "_response"]).read_bytes())["results"]
        for key in audit.QUERIES
    }
    taxon, _ = audit.cached.cached_node(ROOT, data["plan"]["reused_taxonomy"]["287"])
    node = responses["wus-taxonomy"][0]
    if change == "active":
        node["active"] = False
    elif change == "rank":
        node["rank"] = "strain"
    elif change == "parent":
        node["parent"]["taxonId"] = 287
    elif change == "name":
        node["scientificName"] = "Myroides sp."
    elif change == "taxon":
        taxon["taxonId"] = 562
    elif change == "duplicate":
        responses["wus-taxonomy"].append(copy.deepcopy(node))
    else:
        responses["fri11"] = [{"primaryAccession": "UNREVIEWED_CANDIDATE"}]
    with pytest.raises(ValueError):
        audit.source_contexts(responses, taxon)


@pytest.mark.parametrize(
    "change", ["record_hash", "claim_hash", "membership", "chemical", "label", "term_members"]
)
def test_stale_or_misbound_source_claims_fail_closed(frozen, change):
    index = copy.deepcopy(frozen[2]["current_index"])
    term = "ARO:3009643"
    row = next(r for r in index["records"] if term in r["card_terms"])
    claim = next(c for c in index["claims"] if c["aro_id"] == term)
    if change == "record_hash":
        row["record_sha256"] = "0" * 64
    elif change == "claim_hash":
        claim["claim_sha256"] = "0" * 64
    elif change == "membership":
        index["claims"].append(copy.deepcopy(claim))
    elif change == "chemical":
        row["standard_inchi_key"] = "OTHER"
    elif change == "term_members":
        index["terms"][term]["record_memberships"] = ["CHEBI:2676"]
    else:
        index["terms"][term]["source_label_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.bind_current(ROOT, index)

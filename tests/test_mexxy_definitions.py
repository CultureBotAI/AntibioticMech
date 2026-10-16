"""Do not turn review metadata, regulator references or adaptation into experimental alleles."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mexxy_definitions as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


@pytest.mark.parametrize("key", audit.FALSE_FIELDS)
def test_scope_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize("pmid,key", [(p, k) for p, keys in audit.PAPER_FALSE_FIELDS.items() for k in keys])
def test_paper_limits_cannot_be_promoted(pmid, key):
    notes = assessment()
    notes["citations"][pmid][key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize("change", ["review", "reference", "background", "locus", "qualifications", "ncbi"])
def test_changed_identity_or_scope_rejected(change):
    notes = assessment()
    if change == "review":
        notes["citations"]["23233851"]["classification"] = audit.PRIMARY
    elif change == "reference":
        notes["citations"]["21149619"]["source_reference_identifier"] = "NC_002516.2"
    elif change == "background":
        notes["citations"]["21149619"]["source_background_label"] = "PAO1"
    elif change == "locus":
        notes["citations"]["21149619"]["regulator_locus_labels"]["PA1799"] = "mexY"
    elif change == "qualifications":
        notes["claim_qualifications"][1] = copy.deepcopy(notes["claim_qualifications"][0])
    else:
        notes["access"]["ncbi_requests"] = 1
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def save(root, name, value):
    path = root / name
    path.write_text(json.dumps(value))
    return audit.reference.pin(root, path)


def native_fixture(root, monkeypatch, change=None):
    request = {
        "queries": {},
        "request_limit": 2,
        "canary": "PA1799",
        "ncbi_requests": 0,
        "retries": 0,
        "redirects_followed": 0,
        "sequence_or_variant_fields_requested": False,
        "experimental_identity_assignment": False,
        "biological_record_writes": False,
        "reuse_terms_review_resumed": False,
        "issue_1040": "DEFERRED",
    }
    plan = {"new_uniprot_requests": 2, "queries": {}, "attempts": {}}
    entries = {}
    for locus, (gene, accession) in audit.LOCI.items():
        params = audit.parameters(locus)
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
        request["queries"][locus] = {"gene": gene, "parameters": params, "url": url}
        plan["queries"][locus] = save(root, locus + "-receipt.json", {})
        entries[locus] = {
            "primaryAccession": accession,
            "entryType": "UniProtKB unreviewed (TrEMBL)",
            "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
            "proteinDescription": {},
            "genes": [{"geneName": {"value": gene}, "orderedLocusNames": [{"value": locus}]}],
            "organism": {"taxonId": 208964, "scientificName": "Pseudomonas aeruginosa PAO1"},
            "references": [],
        }
    if change == "query":
        request["queries"]["PA1799"]["parameters"]["query"] = "gene_exact:parR"
    plan["request_plan"] = save(root, "request-plan.json", request)
    for locus in audit.LOCI:
        attempt = {
            "url": request["queries"][locus]["url"],
            "request_plan": plan["request_plan"],
            "ncbi_requests": 0,
            "retries": 0,
            "redirects_followed": 0,
        }
        if change == "retry":
            attempt["retries"] = 1
        plan["attempts"][locus] = save(root, locus + "-attempt.json", attempt)
    canary = {
        "accepted": True,
        "locus": "PA1799",
        "gene": "parR",
        "accession": "UniProtKB:Q9I2U3",
        "receipt": plan["queries"]["PA1799"],
        "release": "2026_03",
        "native_taxon_id": 208964,
        "complete_result_count": 1,
        "sequence_or_variant_fields_present": False,
        "experimental_derivative_or_allele_assignment": False,
    }
    if change == "canary":
        canary["accepted"] = False
    plan["canary"] = save(root, "canary-inspected.json", canary)
    if change == "extra":
        save(root, "extra-attempt.json", {})
    if change == "gene":
        entries["PA1799"]["genes"][0]["geneName"]["value"] = "mexY"
    if change == "locus":
        entries["PA1799"]["genes"][0]["orderedLocusNames"][0]["value"] = "PA2018"
    if change == "accession":
        entries["PA1799"]["primaryAccession"] = "Q9I2U4"

    def query(root, receipt, expected):
        locus = Path(receipt["path"]).name.split("-")[0]
        assert expected == {k: [v] for k, v in audit.parameters(locus).items()}
        entry = entries[locus]
        return {entry["primaryAccession"]: entry}, {"receipt": receipt}

    monkeypatch.setattr(audit.mex, "native_query", query)
    species = {"taxonId": 287, "rank": "species", "scientificName": "Pseudomonas aeruginosa"}
    taxon = {
        "taxonId": 208964,
        "rank": "strain",
        "scientificName": "Pseudomonas aeruginosa PAO1",
        "parent": species,
        "lineage": [species],
        "active": True,
    }
    if change == "rank":
        taxon["rank"] = "species"
    return plan, taxon


def test_native_reference_loci_are_not_experimental_subjects(tmp_path, monkeypatch):
    plan, taxon = native_fixture(tmp_path, monkeypatch)
    refs, sources = audit.native_references(tmp_path, plan, taxon)
    assert set(refs) == set(sources) == set(audit.LOCI)
    for locus, (gene, accession) in audit.LOCI.items():
        row = refs[locus]
        assert row["reference"]["accession"] == "UniProtKB:" + accession
        assert row["reference"]["gene_symbols"] == [gene]
        assert row["reference"]["ordered_locus_names"] == [locus]
        assert row["structural_complex_component"] is row["experimental_derivative_assignment"] is False


@pytest.mark.parametrize(
    "change", ["query", "retry", "canary", "extra", "gene", "locus", "accession", "rank"]
)
def test_changed_native_request_or_reference_rejected(tmp_path, monkeypatch, change):
    plan, taxon = native_fixture(tmp_path, monkeypatch, change)
    with pytest.raises(ValueError):
        audit.native_references(tmp_path, plan, taxon)


def test_review_classification_preserves_conflicting_native_metadata(tmp_path):
    body = json.dumps(
        {
            "resultList": {
                "result": [
                    {
                        "id": "23233851",
                        "pmid": "23233851",
                        "source": "MED",
                        "doi": audit.PAPERS["23233851"][0],
                        "pubType": "research-article; journal article",
                    }
                ]
            }
        }
    )
    receipt = {"status": 200, "body": body, "sha256": hashlib.sha256(body.encode()).hexdigest()}
    source = save(tmp_path, "discovery.json", receipt)
    result = audit.review_metadata(tmp_path, source)
    assert result["disposition"] == audit.SECONDARY
    assert result["native_pub_type"] == "research-article; journal article"
    assert result["new_primary_experiment"] is result["native_metadata_rewritten"] is False


def test_portable_artifact_covers_every_claim_and_definition_citation(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    old = audit.read_json(ROOT, result["prior"])
    audit.read_json(ROOT, result["plan"])
    notes = audit.read_json(ROOT, result["assessment"])
    audit.validate_assessment(notes)
    assert result["claims"] == [c for c in old["claims"] if c["aro_id"] == audit.PARENT]
    ids = {c["record_identifier"] for c in result["claims"]}
    assert len(ids) == len(result["claims"]) == 11
    assert result["records"] == [r for r in old["records"] if r["identifier"] in ids]
    assert result["claim_dispositions"] == audit.dispositions(result["claims"], result["records"], notes)
    assert sum(c["selected_qualification"] is not None for c in result["claim_dispositions"]) == 3
    statuses = result["definition_citation_statuses"]
    assert {"PMID:" + p for p in statuses} == set(audit.prior.CITATIONS[audit.PARENT])
    assert statuses["23233851"] == audit.SECONDARY
    assert sum(status == audit.PRIMARY for status in statuses.values()) == 2
    assert result["preserved_opra_access_hold"] == old["primary_access_hold"]
    assert result["paper_species_grounding"]["taxon_id"] == "NCBITaxon:287"
    assert result["mexy_own_citation_reference_view"]["accession"] == "UniProtKB:G3XCW2"
    assert result["mexy_citation_binding"]["experimental_derivative_assignment"] is False
    for locus, (_, accession) in audit.LOCI.items():
        ref = result["regulator_reference_loci"][locus]
        assert ref["reference"]["accession"] == "UniProtKB:" + accession
        assert ref["reference"]["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
        assert ref["structural_complex_component"] is ref["experimental_derivative_assignment"] is False
    assert result["limits"]["biological_records_changed"] == result["limits"]["exact_allele_assignments"] == 0
    assert result["limits"]["ncbi_requests"] == 0 and result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_qualification_requires_current_claim():
    result = public_result()
    claims = [c for c in result["claims"] if c["record_identifier"] != "CHEBI:43968"]
    with pytest.raises(ValueError, match="not bound"):
        audit.dispositions(claims, result["records"], assessment())


def test_no_operational_or_ast_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_read_only_replay_when_native_cache_available(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["queries"]["PA1799"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")
    original = Path.open

    def read_only(path, mode="r", *args, **kwargs):
        assert not set(mode) & set("wax+"), "offline replay attempted write"
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", read_only)
    assert audit.build(pre_cdsa_qualification_root) == public_result()

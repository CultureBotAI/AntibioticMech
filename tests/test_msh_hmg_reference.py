"""Keep source-specific references separate from phenotypes, direct targets and alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_msh_hmg_reference as audit  # noqa: E402


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
    data = {k: audit.read(ROOT, p) for k, p in pins.items() if p["path"].endswith(".json")}
    public = {
        k: audit.read(ROOT, p) for k, p in data["plan"]["inputs"].items() if p["path"].endswith(".json")
    }
    msh = json.loads(audit.reference.check_pin(ROOT, pins["msh_response"]).read_bytes())["results"]
    hmg, _ = audit.literature.read_query(ROOT, ROOT / audit.literature.DIRECTORY, "30940706")
    doc = json.loads((ROOT / audit.OUTPUT).read_bytes())
    return pins, data, public, msh, hmg, doc


def test_exact_read_only_projection(frozen):
    doc = frozen[5]
    assert audit.build(ROOT) == doc
    assert doc["summary"] == {
        "current_corpus_hashes_verified": 2939,
        "complete_records_loaded": 8,
        "source_claims_bound": 9,
        "terms_investigated": 2,
        "selected_references": 2,
        "new_unique_reference_proteins": 1,
        "previously_selected_reference_proteins": 1,
        "new_term_reference_links": 2,
        "excluded_same_citation_candidates": 1,
        "reused_native_taxonomy_nodes": 4,
        "new_native_requests": 1,
        "whole_record_primary_signoffs": 0,
    }
    assert doc["new_unique_reference_accessions"] == ["UniProtKB:Q6FQA9"]
    assert doc["previously_selected_reference_accessions"] == ["UniProtKB:Q4WHZ1"]


def test_exact_locus_fields_and_native_versions(frozen):
    doc = frozen[5]
    msh = doc["terms"]["ARO:3009134"]["references"][0]
    hmg = doc["terms"]["ARO:3007670"]["references"][0]
    assert msh["native_locus_matches"] == [{"field": "genes/0/orderedLocusNames/0", "value": "CAGL0I07733g"}]
    assert hmg["native_locus_matches"] == [{"field": "genes/0/orfNames/0", "value": "AFUA_2G03700"}]
    assert msh["native_reference"]["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert hmg["native_reference"]["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
    assert msh["native_reference"]["entry_version"] == 119
    assert hmg["native_reference"]["entry_version"] == 126
    assert msh["native_reference"]["sequence_version"] == hmg["native_reference"]["sequence_version"] == 1
    assert msh["own_primary_citation_present_in_uniprot"] is False
    assert hmg["own_primary_citation_present_in_uniprot"] is True
    assert msh["source_species_context"]["taxon_id"] == "NCBITaxon:5478"
    assert hmg["source_species_context"]["taxon_id"] == "NCBITaxon:746128"


def test_subjects_and_family_scope_remain_unassigned(frozen):
    _, _, public, _, _, doc = frozen
    index = public["current_index"]
    assert doc["claims"] == [c for c in index["claims"] if c["aro_id"] in audit.TERMS.values()]
    for term, row in doc["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert row["whole_record_primary_review"] == "OPEN"
        assert all(v is None for k, v in row.items() if k.startswith("experimental_"))
        ref = row["references"][0]
        assert all(v is None for k, v in ref.items() if k.startswith("experimental_"))
        assert ref["direct_drug_target_inferred"] is False
        assert ref["resistance_phenotype_from_protein_annotation"] is False
    assert doc["excluded_same_citation_candidate"]["eligible_as_hmg1_reference"] is False
    assert doc["constraints"]["biological_record_writes"] is False
    assert doc["constraints"]["ncbi_requests"] == 0
    assert doc["constraints"]["issue_1040"] == "DEFERRED"
    assert doc["constraints"]["full_investigation_complete"] is False


@pytest.mark.parametrize("key", ["msh", "hmg"])
@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "gene",
        "locus",
        "locus_kind",
        "extra_gene",
        "organism",
        "organism_name",
        "rank",
        "active",
        "parent",
        "species",
        "reviewed",
        "version",
        "sequence",
        "duplicate",
    ],
)
def test_native_reference_cannot_be_substituted(frozen, key, change):
    _, _, public, msh, hmg, doc = frozen
    paper = public["assessment"]["terms"][key]
    entries = copy.deepcopy(msh if key == "msh" else [hmg["Q4WHZ1"]])
    taxon = copy.deepcopy(doc["native_taxonomy"][str(paper["reference_taxon_id"])])
    species = copy.deepcopy(doc["native_taxonomy"][str(paper["reference_species_taxon_id"])])
    entry = entries[0]
    field = "orderedLocusNames" if key == "msh" else "orfNames"
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "locus":
        entry["genes"][0][field][0]["value"] = "OTHER"
    elif change == "locus_kind":
        entry["genes"][0]["synonyms"] = entry["genes"][0].pop(field)
    elif change == "extra_gene":
        entry["genes"].append({"geneName": {"value": "OTHER"}})
    elif change == "organism":
        entry["organism"]["taxonId"] = species["taxonId"]
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "different strain"
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "active":
        taxon["active"] = False
    elif change == "parent":
        taxon["parent"]["taxonId"] = 2
    elif change == "species":
        species["scientificName"] = "different species"
    elif change == "reviewed":
        entry["entryType"] = (
            "UniProtKB reviewed (Swiss-Prot)" if key == "msh" else "UniProtKB unreviewed (TrEMBL)"
        )
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "sequence":
        entry["sequence"] = {"value": "UNREQUESTED"}
    else:
        entries.append(copy.deepcopy(entry))
    with pytest.raises(ValueError):
        audit.select_reference(key, entries, taxon, species, paper)


def test_same_paper_different_gene_is_excluded(frozen):
    candidates = copy.deepcopy(frozen[4])
    selected, excluded = audit.hmg_candidates(candidates)
    assert [e["primaryAccession"] for e in selected] == ["Q4WHZ1"]
    assert excluded["accession"] == "UniProtKB:B0YA65"
    candidates["B0YA65"]["genes"][0]["geneName"]["value"] = "hmg1"
    with pytest.raises(ValueError):
        audit.hmg_candidates(candidates)


def test_doi_and_pmid_must_belong_to_one_citation(frozen):
    _, _, public, _, candidates, doc = frozen
    entry = copy.deepcopy(candidates["Q4WHZ1"])
    citation = next(r for r in entry["references"] if r["citation"].get("id") == "30940706")
    doi = next(x for x in citation["citation"]["citationCrossReferences"] if x["database"] == "DOI")
    citation["citation"]["citationCrossReferences"].remove(doi)
    entry["references"][0]["citation"]["citationCrossReferences"].append(doi)
    with pytest.raises(ValueError):
        audit.select_reference(
            "hmg",
            [entry],
            doc["native_taxonomy"]["330879"],
            doc["native_taxonomy"]["746128"],
            public["assessment"]["terms"]["hmg"],
        )


@pytest.mark.parametrize(
    "change", ["mic", "family", "target", "pool", "genus", "background", "complete", "ncbi"]
)
def test_primary_context_cannot_be_overstated(frozen, change):
    assessment = copy.deepcopy(frozen[2]["assessment"])
    msh, hmg = assessment["terms"]["msh"], assessment["terms"]["hmg"]
    if change == "mic":
        msh["endpoint_is_mic"] = True
    elif change == "family":
        msh["single_identity_for_whole_msh_family"] = True
    elif change == "target":
        hmg["direct_drug_target_established"] = True
    elif change == "pool":
        msh["later_primary"]["cohorts_pooled"] = True
    elif change == "genus":
        hmg["all_aspergillus_species_grounded"] = True
    elif change == "background":
        hmg["experimental_background_is_af293"] = True
    elif change == "complete":
        assessment["constraints"]["full_investigation_complete"] = True
    else:
        assessment["constraints"]["issue_1040"] = "RESUMED"
    with pytest.raises(ValueError):
        audit.validate_assessment(assessment)


@pytest.mark.parametrize("change", ["record_hash", "claim_hash", "members", "chemical", "label"])
def test_current_claim_binding_rejects_drift(frozen, change):
    index = copy.deepcopy(frozen[2]["current_index"])
    term = "ARO:3009134"
    row = next(r for r in index["records"] if term in r["card_terms"])
    claim = next(c for c in index["claims"] if c["aro_id"] == term)
    if change == "record_hash":
        row["record_sha256"] = "0" * 64
    elif change == "claim_hash":
        claim["claim_sha256"] = "0" * 64
    elif change == "members":
        index["terms"][term]["record_memberships"] = []
    elif change == "chemical":
        row["standard_inchi_key"] = "OTHER"
    else:
        index["terms"][term]["source_label_sha256"] = "0" * 64
    with pytest.raises(ValueError):
        audit.bind_current(ROOT, index)

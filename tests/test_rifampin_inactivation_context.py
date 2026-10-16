"""Guard family-member references, native ranks, empty queries and primary scope."""

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
import audit_rifampin_inactivation_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline identity audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    data = {
        k: audit.read(ROOT, p)
        for k, p in plan["inputs"].items()
        if p["path"].endswith(".json") and not p["path"].startswith("reports/")
    }
    public = {
        k: audit.read(ROOT, p)
        for k, p in data["plan"]["inputs"].items()
        if p["path"].endswith(".json") and not p["path"].startswith("reports/")
    }
    doc = json.loads((ROOT / audit.OUTPUT).read_bytes())
    return plan, data, public, doc


@pytest.fixture(scope="module")
def native_frozen(frozen, require_native_inputs):
    plan, data, _, doc = frozen
    require_native_inputs(plan, data["plan"])
    data = {k: audit.read(ROOT, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    public = {
        k: audit.read(ROOT, p) for k, p in data["plan"]["inputs"].items() if p["path"].endswith(".json")
    }
    return plan, data, public, doc


def test_exact_offline_replay(native_frozen, pre_salmonella_qualification_root):
    assert audit.build(pre_salmonella_qualification_root) == native_frozen[3]


def test_public_summary(frozen):
    doc = frozen[3]
    assert doc["summary"] == {
        "current_corpus_hashes_verified": 2939,
        "complete_records_loaded": 4,
        "source_claims_bound": 12,
        "terms_investigated": 3,
        "selected_family_member_references": 1,
        "unresolved_protein_queries": 2,
        "source_species_name_contexts": 3,
        "new_native_taxonomy_nodes": 1,
        "reused_native_taxonomy_nodes": 3,
        "new_native_requests": 4,
        "whole_record_primary_signoffs": 0,
    }


def test_memberships_and_experimental_scope_are_unchanged(frozen):
    _, _, public, doc = frozen
    index = public["current_index"]
    expected = [c for c in index["claims"] if c["aro_id"] in audit.TERMS.values()]
    assert doc["claims"] == expected
    for term, row in doc["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert row["whole_record_primary_review"] == "OPEN"
        assert all(v is None for k, v in row.items() if k.startswith("experimental_"))
    assert doc["constraints"]["biological_record_writes"] is False
    assert doc["constraints"]["experimental_identifiers_assigned"] is False
    assert doc["constraints"]["issue_1040"] == "DEFERRED"
    assert doc["constraints"]["ncbi_requests"] == 0
    assert doc["constraints"]["full_investigation_complete"] is False


def test_wac_exact_other_name_is_not_a_related_species_or_strain_rank(frozen):
    _, _, _, doc = frozen
    row = doc["terms"]["ARO:3002883"]
    tax = row["source_taxonomy_context"]
    assert tax["taxon_id"] == "NCBITaxon:2203204"
    assert tax["scientific_name"] == "Streptomyces sp. WAC 01438"
    assert tax["rank"] == "species"
    assert tax["native_name_matches"] == [{"field": "otherNames", "value": "Streptomyces sp. WAC1438"}]
    assert row["reference_accessions"] == []
    assert row["experimental_strain_taxon_assignment"] is None
    assert row["status"] == "EXPLICIT_QUERY_EMPTY_NOT_BIOLOGICAL_ABSENCE"


def test_arr_reference_does_not_identify_the_whole_family_or_source_strain(frozen):
    _, _, _, doc = frozen
    row = doc["terms"]["ARO:3000390"]
    ref = row["references"][0]
    assert row["reference_accessions"] == ["UniProtKB:A0QRS5"]
    assert ref["identity"] == {
        "entry_type": "UniProtKB unreviewed (TrEMBL)",
        "entry_version": 118,
        "sequence_version": 1,
        "reference_taxon_id": "NCBITaxon:246196",
        "reference_taxon_rank": "strain",
        "reference_species_taxon_id": "NCBITaxon:1772",
    }
    assert ref["structure_entity"] == "2HW2_1"
    assert ref["structure_source_strain_reported"] is None
    assert ref["single_protein_identity_for_whole_arr_family"] is False
    assert ref["structure_expression_host_source_reported"]["experimental_subject_assigned"] is False
    assert row["primary_assessment"]["older_primary"]["biological_absence_inferred"] is False


def test_rph_range_cannot_supply_an_individual_gene_accession(frozen):
    _, _, _, doc = frozen
    row = doc["terms"]["ARO:3003992"]
    assert row["source_taxonomy_context"]["taxon_id"] == "NCBITaxon:1120679"
    assert row["source_taxonomy_context"]["rank"] == "species"
    assert row["reference_accessions"] == []
    assert doc["rph_primary_scope"]["individual_gene_accession_assigned_from_range"] is False
    assert doc["rph_primary_scope"]["quantitative_values_exported"] is False
    assert (
        doc["rph_primary_scope"]["table_determinant"]["measurement_subject"]
        == "HETEROLOGOUS_E_COLI_NOT_NATIVE_LC231"
    )
    assert doc["queries"]["rphB"]["suggestions_not_selected"]
    assert doc["queries"]["rphB"]["result_count"] == 0


@pytest.fixture
def arr_inputs(native_frozen):
    _, data, public, doc = native_frozen
    body = audit.reference.check_pin(ROOT, data["plan"]["inputs"]["arr_citation_body"]).read_bytes()
    entry = audit.citation_entry(public["arr_citation_receipt"], body)
    return copy.deepcopy(
        (
            entry,
            doc["native_structure_metadata"],
            doc["native_taxonomy"]["246196"],
            doc["native_taxonomy"]["1772"],
        )
    )


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "locus",
        "species",
        "taxon",
        "rank",
        "active",
        "version",
        "reviewed",
        "sequence",
        "citation",
        "pdb_citation",
    ],
)
def test_arr_reference_requires_native_identity(arr_inputs, change):
    entry, structure, taxon, species = arr_inputs
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "species":
        species["scientificName"] = "different species"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 1772
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "active":
        taxon["active"] = False
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "sequence":
        entry["sequence"] = {"value": "UNREQUESTED"}
    elif change == "citation":
        entry["references"][1]["citation"]["citationCrossReferences"].clear()
    else:
        entry["references"][1]["evidences"] = []
    with pytest.raises(ValueError):
        audit.arr_reference(entry, structure, taxon, species)


@pytest.mark.parametrize(
    "change", ["citation", "component", "duplicate", "xref", "gene", "source", "host", "strain"]
)
def test_pdb_component_source_and_host_cannot_be_substituted(arr_inputs, change):
    entry, structure, taxon, species = arr_inputs
    entity = structure["polymer_entities"][0]
    source = entity["entity_src_gen"][0]
    if change == "citation":
        structure["rcsb_primary_citation"]["pdbx_database_id_PubMed"] = 9869590
    elif change == "component":
        entity["rcsb_id"] = "2HW2_2"
    elif change == "duplicate":
        structure["polymer_entities"].append(copy.deepcopy(entity))
    elif change == "xref":
        entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"][0][
            "database_accession"
        ] = "OTHER"
    elif change == "gene":
        source["pdbx_gene_src_gene"] = "rphB"
    elif change == "source":
        source["pdbx_gene_src_ncbi_taxonomy_id"] = "469008"
    elif change == "host":
        source["pdbx_host_org_ncbi_taxonomy_id"] = "1772"
    else:
        source["gene_src_strain"] = "unreviewed strain"
    with pytest.raises(ValueError):
        audit.arr_reference(entry, structure, taxon, species)


@pytest.mark.parametrize("change", ["query", "release", "count", "pagination", "hash", "status"])
def test_reused_citation_is_bound_to_complete_native_response(native_frozen, change):
    _, data, public, _ = native_frozen
    receipt = copy.deepcopy(public["arr_citation_receipt"])
    body = audit.reference.check_pin(ROOT, data["plan"]["inputs"]["arr_citation_body"]).read_bytes()
    if change == "query":
        receipt["query"] = "lit_pubmed:9869590"
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "different"
    elif change == "count":
        receipt["headers"]["X-Total-Results"] = "2"
    elif change == "pagination":
        receipt["headers"]["Link"] = "another page"
    elif change == "hash":
        receipt["sha256"] = "different"
    else:
        receipt["status"] = 403
    with pytest.raises(ValueError):
        audit.citation_entry(receipt, body)


@pytest.mark.parametrize("change", ["status", "redirect", "hash", "url", "graphql", "sequence"])
def test_pdb_receipt_is_not_an_unchecked_browser_annotation(native_frozen, change):
    plan, data, _, _ = native_frozen
    selected = copy.deepcopy(data["plan"])
    receipt, attempt = copy.deepcopy((data["pdb-arr_receipt"], data["pdb-arr_attempt"]))
    body = audit.reference.check_pin(ROOT, plan["inputs"]["pdb-arr_response"]).read_bytes()
    if change == "status":
        receipt["status"] = 403
    elif change == "redirect":
        receipt["redirects_followed"] = 1
    elif change == "hash":
        receipt["body"]["sha256"] = "wrong"
    elif change == "url":
        selected["requests"]["pdb-arr"]["url"] = "https://example.org/graphql"
    else:
        payload = json.loads(body)
        if change == "graphql":
            payload["errors"] = [{"message": "partial response"}]
        else:
            payload["data"]["entries"][0]["sequence"] = "UNREQUESTED"
        body = json.dumps(payload).encode()
        receipt["bytes"] = len(body)
        receipt["body"]["sha256"] = hashlib.sha256(body).hexdigest()
    with pytest.raises(ValueError):
        audit.pdb_response(selected, receipt, attempt, body)


@pytest.mark.parametrize("change", ["citation", "determinant", "subject", "range", "hash"])
def test_rph_primary_scope_cannot_change_silently(native_frozen, change):
    _, _, public, _ = native_frozen
    wrapper = copy.deepcopy(public["rph_primary"])
    if change == "hash":
        wrapper["sha256"] = "wrong"
    else:
        old, new = {
            "citation": ("27929110", "12345678"),
            "determinant": ("rphB", "rphX"),
            "subject": ("heterologously expressed in", "native expression in"),
            "range": ("KX531043", "KX531044"),
        }[change]
        assert old in wrapper["body"]
        wrapper["body"] = wrapper["body"].replace(old, new)
        wrapper["sha256"] = hashlib.sha256(wrapper["body"].encode()).hexdigest()
    with pytest.raises(ValueError):
        audit.rph_primary_scope(wrapper)


def test_no_experimental_protocols_sequences_or_numeric_ast_in_public_projection(frozen):
    _, _, _, doc = frozen
    audit.sal.metadata_only(doc)
    assert doc["constraints"]["sequences_variants_constructs_protocols_or_numeric_ast_exported"] is False
    assert doc["constraints"]["figure_pixels_reviewed"] is False
    assert doc["constraints"]["whole_papers_reviewed"] is False
    assert doc["constraints"]["broad_index_rewritten"] is False

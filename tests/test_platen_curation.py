"""Keep producer reference grounding separate from experimental allele identity."""

import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def curation():
    return json.loads((ROOT / "research/2026-10-09-platen-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-09-platen-primary-context.json").read_bytes())


def test_two_exact_compounds_and_four_qualified_claims(curation, tmp_path):
    keys = {"CHEBI:68236": "CSOMAHTTWTVBFL-OFBLZTNGSA-N",
            "CHEBI:68241": "DWUHGPPFFABTIY-RLWZQHMASA-N"}
    assert len(curation["records"]) == 2 and curation["claims_added"] == 4
    assert curation["history_events_added"] == 2
    for row in curation["records"]:
        path = ROOT / row["record"]["path"]
        record = load_record(path)
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == keys[row["identifier"]]
        assert record["curation_status"] == row["curation_status"] == "SEEDED"
        assert record["resistance_mechanisms"] == row["claims"]
        assert record["curation_history"][-1] == row["curation_event"]
        assert row["all_other_fields_preserved"] is True
        assert row["original_bytes_preserved_as_prefix"] is True
        assert not record.get("activity_spectrum")
        output = tmp_path / path.name
        write_validated_antibiotic(record, output)
        assert output.read_bytes() == path.read_bytes()


def test_partial_platencin_response_is_not_full_resistance(curation):
    for row in curation["records"]:
        by_gene = {r["gene_families"][0]: r for r in row["claims"]}
        assert set(by_gene) == {"ptmP3", "fabF"}
        assert by_gene["ptmP3"]["mechanism_type"] == "ANTIBIOTIC_TARGET_REPLACEMENT"
        assert by_gene["fabF"]["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
        assert by_gene["ptmP3"]["strain"] == "SB12011"
        assert by_gene["fabF"]["strain"] == "SB12013"
        partial = "partial resistance / reduced susceptibility" in by_gene["fabF"]["phenotype_label"]
        assert partial == (row["identifier"] == "CHEBI:68241")
        for claim in by_gene.values():
            assert claim["taxon_label"] == "Streptomyces albus"
            assert "authors' interpretation" in claim["note"]
            assert "not the tested host" in claim["note"]
            assert "No exact allele" in claim["note"]
            assert not {
                "protein_accession", "gene_id", "taxon_id", "strain_taxon_id", "alteration", "source",
            } & claim.keys()


def test_archive_lookup_resolves_unnamed_reference_not_experimental_allele(context):
    protein = context["proteins"]["D8L2W8"]
    assert protein["genes"] == []
    assert protein["entry_audit"] == {"entryVersion": 45, "sequenceVersion": 1}
    assert protein["organism"]["taxonId"] == 58346
    assert protein["source_strain"] == "MA7327"
    citation, = protein["citation_contexts"]
    assert {"database": "PubMed", "id": "21825154"} in citation["identifiers"]
    assert any(c.get("type") == "STRAIN" and c.get("value") == "MA7327" for c in citation["context"])
    assert protein["scope"] == "DONOR_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
    archive, = protein["archive_references"]
    assert archive["id"] == "FJ655920"
    assert {"key": "ProteinId", "value": "ACS13710.1"} in archive["properties"]
    assert context["reference_grounding"]["paper_accession"] == "ACS13710"
    assert context["reference_grounding"]["earlier_primary_reviewed"] is False
    assert context["reference_grounding"]["genome_assignment"] is None
    assert sorted(r["result_count"] for r in context["uniprot_requests"]) == [0, 0, 0, 1, 7]
    assert all(r["complete_for_query"] and r["release"] == "2026_03" for r in context["uniprot_requests"])


def test_seven_same_species_wrong_strain_hits_are_not_substituted(context):
    rejected = [r for r in context["proteins"].values() if r["scope"] == "WRONG_STRAIN_NOT_SELECTED"]
    assert len(rejected) == 7
    assert all(r["source_strain"] == "DSM 40041" for r in rejected)
    for row in rejected:
        assert any(c.get("type") == "STRAIN" and c.get("value") == "DSM 40041"
                   for citation in row["citation_contexts"] for c in citation["context"])
    assert all(r["experimental_allele_assignment"] is False for r in context["proteins"].values())
    assert "not proof" in context["negative_query_limit"]


def test_taxonomy_rank_and_all_j1074_candidates_remain_visible(context):
    assert context["taxonomy"]["58346"]["rank"] == "species"
    assert context["taxonomy"]["1888"]["rank"] == "species"
    search = context["host_taxonomy_search"]
    assert search["selected_strain_taxon"] is None and search["complete_for_query"]
    assert {r["taxonId"] for r in search["candidates"]} == {457425, 1962, 3466461}


def test_primary_scope_negative_controls_and_distinct_later_study(context):
    focal = context["primary_papers"]["24560608"]
    assert focal["document_version"] == "ACCEPTED_AUTHOR_MANUSCRIPT_NOT_FINAL_PUBLISHER_VERSION"
    assert focal["figures_visually_inspected"] == ["Figure 1", "Figure 2", "Table 1"]
    assert "fabH" in focal["negative_context"] and "ptmP4" in focal["negative_context"]
    assert "not independent proof" in focal["necessity_limit"]
    assert "not automatically" in focal["ptnP3_limit"]
    later = context["primary_papers"]["25403676"]
    assert "not interchangeable" in later["finding"]
    assert "not universal absence" in later["negative_limit"]
    assert "visual adjudication remains pending" in later["text_only_mapping_concern"]
    assert later["record_mutations"] == 0 and later["native_primary_file_cached"] is False
    assert later["figures_visually_inspected"] == []
    assert context["cerulenin_context"]["record_changed"] is False
    assert context["out_of_corpus_compound"]["matching_records"] == 0
    assert "ignored" in context["out_of_corpus_compound"]["search_scope"]


def test_full_scope_and_pending_candidates_are_not_dropped(context):
    assert len(context["candidate_ids"]) == 12 and len(context["primary_papers"]) == 11
    assert context["scope"]["corpus_records"] == 2939
    assert context["scope"]["full_corpus_primary_review"] == "OPEN"
    assert context["scope"]["whole_records_completed"] == 0
    assert context["non_MED_candidates"] == [
        {"identifier": "CBA:662853", "status": "PRIMARY_REVIEW_PENDING_NOT_QUERIED_AS_MED"}]
    assert sum(r["status"] == "METADATA_ONLY_PRIMARY_REVIEW_PENDING"
               for r in context["primary_papers"].values()) == 9
    assert not any(r["whole_paper_review_complete"] for r in context["primary_papers"].values())
    for source in context["inputs"].values():
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]


def test_export_excludes_experimental_specifications(context):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(context)) & {"sequence", "variants", "alteration", "constructs", "primers",
                                     "protocol", "coordinates", "mic", "measurement_value", "headers"}
    assert context["ncbi_endpoint_requests"] == context["github_mutations"] == 0

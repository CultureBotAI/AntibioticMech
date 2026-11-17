"""Keep reference identity, tested hosts and processed drug forms distinct."""

import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def curation():
    return json.loads((ROOT / "research/2026-10-09-bacteriocin-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-09-bacteriocin-followup-context.json").read_bytes())


def test_two_records_three_claims_preserve_source_fields(curation, tmp_path):
    assert curation["claims_added"] == 3 and curation["history_events_added"] == 2
    assert {r["identifier"] for r in curation["records"]} == {"CHEBI:71659", "CHEBI:82754"}
    for row in curation["records"]:
        path = ROOT / row["record"]["path"]
        record = load_record(path)
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        assert record["curation_status"] == row["curation_status"] == "SEEDED"
        assert record["resistance_mechanisms"] == row["claims"]
        assert record["curation_history"][-1] == row["curation_event"]
        assert row["history_events_added"] == 1 and row["all_other_fields_preserved"]
        assert row["original_bytes_preserved_as_prefix"]
        assert not record.get("activity_spectrum")
        output = tmp_path / path.name
        write_validated_antibiotic(record, output)
        assert output.read_bytes() == path.read_bytes()


def test_epifeg_is_not_verified_efflux_or_three_sufficient_genes(curation):
    record, = [r for r in curation["records"] if r["identifier"] == "CHEBI:71659"]
    claim, = record["claims"]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["gene_families"] == ["epiF", "epiE", "epiG"]
    assert claim["taxon_id"] == "NCBITaxon:1281"
    assert claim["taxon_label"] == "Staphylococcus carnosus"
    assert "laboratory derivatives" in claim["phenotype_label"]
    for limit in ("not the unmodified background", "is the donor", "individual sufficiency",
                  "transport remains a hypothesis", "not experimental allele assignments"):
        assert limit in claim["note"]
    assert claim["evidence"][0]["reference"] == "PMID:8550476"


def test_microcin_intact_and_processed_forms_are_not_collapsed(curation):
    record, = [r for r in curation["records"] if r["identifier"] == "CHEBI:82754"]
    by_gene = {r["gene_families"][0]: r for r in record["claims"]}
    assert set(by_gene) == {"mccF", "mccE"}
    assert all(r["mechanism_type"] == "ANTIBIOTIC_INACTIVATION" for r in by_gene.values())
    assert "Deformylated material" in by_gene["mccF"]["note"]
    assert "not a pure-compound organismal AST claim" in by_gene["mccF"]["note"]
    assert "not direct acetylation of intact microcin C" in by_gene["mccE"]["note"]
    assert "gene-start annotation" in by_gene["mccE"]["note"]
    assert "authors' interpretation" in by_gene["mccE"]["evidence"][0]["notes"]
    for claim in by_gene.values():
        assert not {"taxon_id", "taxon_label", "strain", "strain_taxon_id"} & claim.keys()
        assert "reference species" in claim["note"] and "not an exact derivative" in claim["note"]


def test_no_reference_promoted_to_experimental_protein(curation, context):
    for row in curation["records"]:
        for claim in row["claims"]:
            assert not {"protein_accession", "gene_id", "alteration", "source", "aro_id"} & claim.keys()
    assert set(context["microcin_reference_candidates"]) == {
        "Q47511", "Q47510", "Q2KKH5", "B0EYN8", "Q83Y55", "Q2KKH9"}
    assert context["microcin_reference_selection"] is None
    references = [*context["epidermin_references"].values(),
                  *context["microcin_reference_candidates"].values()]
    for protein in references:
        assert protein["experimental_assignment"] is False
    selected = {k for k, v in context["epidermin_references"].items()
                if v["scope"] == "DONOR_REFERENCE_NOT_EXPERIMENTAL_ALLELE"}
    assert selected == {"Q54002", "Q54003", "Q54004"}
    assert all(v["organism"]["taxonId"] == 1282 for v in context["epidermin_references"].values())


def test_explicit_secondary_accession_resolves_archive_not_allele(context):
    crosswalk = context["archive_crosswalk"]
    assert crosswalk["basis"] == "EXPLICIT_ENA_SECONDARY_ACCESSION"
    assert crosswalk["requests"]["U77778"]["reference"]["secondaryAccession"] == ["U29130"]
    assert crosswalk["requests"]["U29130"]["returned_count"] == 0
    assert crosswalk["requests"]["U29130"]["establishes_biological_absence"] is False
    assert crosswalk["experimental_allele_assignment"] is False
    request = context["uniprot_request"]
    assert request["complete_for_query"] and request["result_count"] == 6
    assert request["release"] == "2026_03"
    assert context["tested_host_taxonomy"]["taxonId"] == 1281
    assert context["tested_host_taxonomy"]["rank"] == "species"
    assert context["microcin_reference_taxonomy"]["taxonId"] == 562


def test_primary_transcription_limits_and_failed_native_access_are_visible(context):
    assert set(context["primary_papers"]) == {"8550476", "20876530", "20159968"}
    for row in context["primary_papers"].values():
        assert row["relevant_results_text_inspected"]
        assert row["review_medium"] == "PUBLIC_INDEXED_AUTHOR_UPLOADED_PRIMARY_TEXT_TRANSCRIPTION"
        assert not any(row[k] for k in ("figures_visually_inspected", "supplement_inspected",
                                       "whole_paper_review_complete", "native_primary_file_cached"))
    assert len(context["access_limits"]) == 2
    assert all(r["status"] == 403 for r in context["access_limits"])
    assert context["scope"]["corpus_records"] == 2939
    assert context["scope"]["full_corpus_primary_review"] == "OPEN"
    assert context["scope"]["whole_records_completed"] == 0
    assert set(context["unchanged_holds"]) == {"CHEBI:71629", "CHEBI:64624", "antibioticmech:aro-0a1c492c45"}
    for key in ("prior_context", "curation"):
        source = context[key]
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]


def test_no_operational_experimental_exports(context, curation):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                  "coordinates", "mic", "measurement_value", "headers"}
    assert not set(keys(context)) & prohibited
    assert not set(keys(curation)) & prohibited
    assert all(context[k] == 0 for k in ("ncbi_endpoint_requests", "github_mutations", "source_adoptions"))
    assert context["experimental_genome_assignments"] == context["numerical_ast_added"] == 0

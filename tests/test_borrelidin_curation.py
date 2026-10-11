"""Preserve qualified BorO reporting and distinguish reference/experimental context."""

import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def curation():
    return json.loads((ROOT / "research/2026-10-09-borrelidin-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-09-borrelidin-primary-context.json").read_bytes())


def test_one_qualified_report_not_a_demonstrated_replacement_route(curation):
    claim, = curation["claims"]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["gene_families"] == ["borO"]
    assert claim["taxon_label"] == "Streptomyces albus"
    assert "data not shown" in claim["note"]
    assert "not directly demonstrated" in claim["note"]
    assert curation["primary_source"]["supporting_experimental_data_shown"] is False
    assert curation["experimental_alleles_validated"] is False
    assert curation["whole_record_review_complete"] is False
    assert not {
        "protein_accession", "gene_id", "taxon_id", "strain_taxon_id", "strain", "alteration",
    } & claim.keys()
    assert "donor" in claim["note"].lower() and "not the tested host" in claim["note"]


def test_existing_chemical_and_target_curation_survives(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:78661"
    assert record["chemical_structure"]["standard_inchi_key"] == "OJCKRNPLOZHAOU-JTHVHBRGSA-N"
    assert record["resistance_mechanisms"] == curation["claims"]
    target, = record["molecular_targets"]
    assert target["taxon_id"] == "NCBITaxon:67593"
    assert target["evidence"][0]["reference"] == "PMID:22967236"
    assert record["curation_history"][-1] == curation["curation_event"]
    assert curation["history_events_added"] == 1
    assert curation["existing_molecular_targets_preserved"] == 1
    assert not record.get("activity_spectrum")
    output = tmp_path / "borrelidin.yaml"
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()


def test_full_scope_and_four_bounded_primary_reviews(context):
    assert context["scope"] == {
        "corpus_records": 2939, "records": 1, "discovery_candidate_papers": 18,
        "existing_target_paper": 1, "papers_with_bounded_primary_review": 4,
        "reference_proteins": 6, "whole_records_completed": 0, "full_corpus_primary_review": "OPEN",
    }
    assert len(context["primary_papers"]) == 19
    assert sum(p["status"] == "METADATA_ONLY_PRIMARY_REVIEW_PENDING"
               for p in context["primary_papers"].values()) == 14
    assert not any(p["whole_paper_review_complete"] for p in context["primary_papers"].values())
    for source in context["inputs"].values():
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]


@pytest.mark.parametrize("accession,version,seq,taxon", [
    ("Q70HZ0", 112, 1, 146923), ("P0A8M3", 169, 1, 83333),
    ("Q58597", 151, 2, 243232), ("O29703", 152, 1, 224325),
    ("Q97VW8", 130, 1, 273057), ("Q9HP27", 139, 2, 64091),
])
def test_versioned_reference_entries_are_not_experimental_alleles(context, accession, version, seq, taxon):
    row = context["proteins"][accession]
    assert row["entry_audit"] == {"entryVersion": version, "sequenceVersion": seq}
    assert row["organism"]["taxonId"] == taxon
    assert row["experimental_allele_assignment"] is False
    assert row["scope"] == "REFERENCE_METADATA_NOT_TESTED_ALLELE_OR_RESISTANT_ISOLATE"


def test_boro_archive_and_comparison_accessions_have_different_roles(context):
    bor = context["proteins"]["Q70HZ0"]
    archive, = bor["archive_references"]
    assert archive["id"] == "AJ580915"
    assert {"key": "ProteinId", "value": "CAE45679.1"} in archive["properties"]
    citation, = bor["focal_citation_contexts"]
    assert {"database": "PubMed", "id": "15112998"} in citation["identifiers"]
    assert citation["context"][0]["value"] == "Tu4055"
    paper = context["primary_papers"]["15112998"]
    assert paper["gene"] == "borO" and paper["source_archive"] == "EMBL:AJ580915"
    assert "CAB08628" in paper["homology_limit"] and "NP_625810" in paper["homology_limit"]
    assert paper["figures_visually_inspected"] == ["Figure 1", "Table 1", "Results page 92"]
    comment, = paper["commentCorrectionList"]["commentCorrection"]
    assert comment["type"] == "Comment in" and comment["id"] == "15112984"


def test_archaeal_results_do_not_become_domain_wide_resistance(context):
    paper = context["primary_papers"]["15507440"]
    rows = {r["reference"]: r["result"] for r in paper["enzyme_contexts"]}
    for accession in ("Q58597", "O29703"):
        assert rows["UniProtKB:" + accession] == (
            "RELATIVE_BIOCHEMICAL_INSENSITIVITY_UNDER_REPORTED_CONDITIONS")
    for accession in ("Q97VW8", "Q9HP27"):
        assert rows["UniProtKB:" + accession] == "BIOCHEMICAL_INHIBITION"
    assert "WILD_TYPE_REFERENCE" in rows["UniProtKB:P0A8M3"]
    assert paper["native_primary_file_cached"] is False
    assert paper["figures_visually_inspected"] == []
    for accession in ("Q58597", "Q9HP27"):
        archive, = context["proteins"][accession]["archive_references"]
        assert {"key": "Status", "value": "ALT_INIT"} in archive["properties"]


def test_taxonomic_rank_is_not_guessed_from_a_strain_name(context):
    tax = context["taxonomy"]["64091"]
    assert tax["rank"] == "no rank"
    assert tax["parent"]["taxonId"] == 2886895
    assert tax["species_ancestors"][0]["taxonId"] == 2242
    assert context["taxonomy"]["146923"]["rank"] == "species"
    assert context["taxonomy"]["273057"]["scientificName"].startswith("Saccharolobus solfataricus")


def test_j1074_search_keeps_all_candidates(context):
    search = context["host_taxonomy_search"]
    assert search["selected_strain_taxon"] is None
    assert search["complete_for_query"] is True and search["result_count"] == 3
    assert {r["taxonId"] for r in search["candidates"]} == {457425, 1962, 3466461}
    alias, = [r for r in search["candidates"] if r["taxonId"] == 1962]
    assert {"name": "J1074"} in alias["strains"]


def test_later_papers_keep_compound_and_assay_scope(context):
    later = context["primary_papers"]["39014102"]
    assert "ObaO is not" in later["compound_limit"]
    assert later["figures_visually_inspected"] == []
    latest = context["primary_papers"]["41773311"]
    assert "seven other antibiotics, not borrelidin" in latest["finding"]
    ids = {r["identifier"]: r for r in latest["source_reported_identifiers"]}
    assert ids["NC_000913.3"]["scope"] == "REFERENCE_CHROMOSOME_NOT_EACH_EXPERIMENTAL_GENOME"
    assert ids["NC_000913.3"]["source_namespace_label"] == "GenBank accession"
    assert ids["ENA:PRJEB94349"]["scope"] == "STUDY_PROJECT_NOT_AN_ISOLATE_ASSEMBLY"
    assert latest["supplements_inspected"] is False


def test_reference_export_excludes_experimental_specifications(context):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(context)) & {
        "sequence", "variants", "alteration", "constructs", "primers", "protocol", "coordinates",
        "mic", "measurement_value", "headers", "Set-Cookie", "fullTextUrlList",
    }
    assert "No NCBI endpoint request" in " ".join(context["limitations"])
    assert sorted(r["result_count"] for r in context["uniprot_requests"]) == [1, 5]

"""Keep oligomycin reference metadata separate from experimental resistance."""

import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def dossier():
    return json.loads(
        (ROOT / "research/2026-10-08-oligomycin-reference-grounding.json").read_text()
    )


def test_bound_ligand_identity_does_not_resolve_the_mixture_phenotype(dossier):
    records = {entry["identifier"]: entry for entry in dossier["compound_records"]}
    assert set(records) == {"CHEBI:28285", "CHEBI:7751", "CHEBI:7752", "CHEBI:7753"}
    assert len({entry["standard_inchi_key"] for entry in records.values()}) == 4
    ligand = dossier["structural_crosswalk"]["ligand"]
    assert ligand["chem_comp"]["id"] == "EFO"
    assert ligand["rcsb_chem_comp_descriptor"]["InChIKey"] == (
        records["CHEBI:28285"]["standard_inchi_key"]
    )
    decision = dossier["compound_scope_decision"]
    assert decision["bound_ligand_record"] == "CHEBI:28285"
    assert decision["reagent_scope"] == "OLIGOMYCIN_A_B_C_MIXTURE"
    assert decision["resistance_claim_curated"] is False
    assert decision["transfer_to_related_records"] is False
    for entry in records.values():
        record = load_record(ROOT / entry["path"])
        assert record["identifier"] == entry["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == entry["standard_inchi_key"]
        assert not record.get("resistance_mechanisms")


@pytest.mark.parametrize("accession,gene,locus,entry_version,sequence_version", [
    ("P61829", "OLI1", "Q0130", 171, 1),
    ("P00854", "ATP6", "Q0085", 196, 2),
])
def test_proteins_are_versioned_reference_entries(
    dossier, accession, gene, locus, entry_version, sequence_version,
):
    protein = dossier["proteins"][accession]
    assert protein["primaryAccession"] == accession
    assert protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert protein["entryAudit"] == {
        "entryVersion": entry_version, "sequenceVersion": sequence_version,
    }
    assert protein["genes"][0]["geneName"]["value"] == gene
    assert protein["genes"][0]["orderedLocusNames"] == [{"value": locus}]
    assert protein["organism"]["taxonId"] == 559292
    assert dossier["taxonomy"]["559292"]["rank"] == "strain"
    assert dossier["taxonomy"]["559292"]["parent"]["taxonId"] == 4932
    assert dossier["taxonomy"]["4932"]["rank"] == "species"
    assert dossier["protein_scope"] == (
        "S288C_REFERENCE_PROTEINS_NOT_EXPERIMENTAL_RESISTANCE_ALLELES"
    )


def test_structural_crosswalk_does_not_assign_reference_strain_to_experiment(dossier):
    crosswalk = dossier["structural_crosswalk"]
    structure = crosswalk["structure"]
    assert structure["rcsb_id"] == crosswalk["uniprot_backlink"]["id"] == "4F4S"
    assert structure["rcsb_primary_citation"]["pdbx_database_id_PubMed"] == 22869738
    entity, = structure["polymer_entities"]
    assert entity["entity_poly"]["rcsb_mutation_count"] == 0
    assert entity["rcsb_entity_source_organism"] == [{"ncbi_taxonomy_id": 4932}]
    assert entity["rcsb_polymer_entity_container_identifiers"][
        "reference_sequence_identifiers"
    ] == [{"database_name": "UniProt", "database_accession": "P61829"}]


def test_functional_leads_have_no_experimental_accession_assignments(dossier):
    papers = {paper["reference"]: paper for paper in dossier["resistance_papers"]}
    assert set(papers) == {"PMID:2932333", "PMID:2867935", "PMID:159820", "PMID:2876917"}
    assert papers["PMID:159820"]["access_status"] == "CITATION_ONLY_NO_ABSTRACT_IN_CACHED_RESPONSE"
    for reference, paper in papers.items():
        if reference != "PMID:159820":
            assert paper["access_status"] == "PRIMARY_ABSTRACT_INSPECTED_FULL_RESULTS_PENDING"
        assert paper["compound_scope"] == "GENERIC_OLIGOMYCIN_EXACT_CONGENER_UNRESOLVED"
        assert paper["reference_link_scope"] == (
            "GENE_COMPONENT_CONTEXT_NOT_EXPERIMENTAL_ALLELE_ACCESSION"
        )
        for field in (
            "experimental_allele_accession", "experimental_genome_accession",
            "experimental_protein_accession", "experimental_strain_taxon_id",
        ):
            assert paper[field] is None
    assert papers["PMID:2876917"]["reference_candidate"] == "UniProtKB:P00854"
    assert all(paper["reference_candidate"] == "UniProtKB:P61829"
               for reference, paper in papers.items() if reference != "PMID:2876917")


def test_manual_primary_review_is_not_reported_as_cached_full_text(dossier):
    papers = {paper["reference"]: paper for paper in dossier["structural_papers"]}
    assert papers["PMID:22869738"]["primary_access"] == (
        "MANUAL_PUBLISHER_FULL_TEXT_INSPECTED_WITH_WEB_TOOL_NOT_CACHED"
    )
    assert papers["PMID:29650704"]["primary_access"] == "PRIMARY_TEXT_UNAVAILABLE_CITATION_ONLY"
    assert all(paper["failed_fulltext_request"]["status"] == 500 for paper in papers.values())
    assert dossier["failed_metadata_query"]["status"] == 200
    assert dossier["failed_metadata_query"]["cache_path"] != (
        dossier["structural_crosswalk"]["request"]["cache_path"]
    )
    assert {request["release"] for request in dossier["uniprot_requests"]} == {"2026_03"}
    assert all(urlsplit(request["url"]).hostname == "rest.uniprot.org"
               for request in dossier["uniprot_requests"])


def test_metadata_dossier_does_not_export_sequences_or_new_assays(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "features", "alteration", "activity_spectrum", "resistance_mechanisms",
    }
    assert dossier["status"] == "REFERENCE_GROUNDING_VERIFIED_RESISTANCE_CURATION_PENDING"
    assert dossier["preservation"] == {
        "records_verified": 2939,
        "biological_record_changes": 0,
        "curation_events_added": 0,
        "new_measurements": 0,
        "source_reviews_unchanged": True,
        "discovery_exports_unchanged": True,
    }

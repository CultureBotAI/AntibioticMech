"""Keep a partially inspected primary lead separate from curated allele evidence."""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/2026-10-09-cordycepin-reference-lead.json"


@pytest.fixture(scope="module")
def dossier():
    return json.loads(PATH.read_text())


def test_primary_review_is_explicitly_incomplete(dossier):
    assert dossier["status"] == "REFERENCE_GROUNDED_PRIMARY_REVIEW_INCOMPLETE"
    assert dossier["curated"] is False and dossier["primary_review_complete"] is False
    assert dossier["curation_decision"] == "HOLD_FOR_PRIMARY_FIGURES_AND_SUBJECT_CONTEXT"
    primary = dossier["primary_lead"]
    assert primary["reference"] == "PMID:19324962"
    assert primary["doi"] == "10.1261/rna.1458909"
    assert primary["figures_visually_inspected"] is False
    assert primary["strain_provenance_verified"] is False
    assert primary["native_primary_file_cached"] is False


def test_parent_compound_is_not_the_triphosphate(dossier):
    assert dossier["compound"]["identifier"] == "CHEBI:29014"
    assert dossier["compound"]["standard_inchi_key"] == "OFEZSBMBBKLLBJ-BAJZRUMYSA-N"
    assert dossier["distinct_metabolite"]["identifier"] == "CHEBI:52316"
    assert dossier["distinct_metabolite"]["standard_inchi_key"] == "NLIHPCYXRYQPSD-BAJZRUMYSA-N"
    assert dossier["compound"]["unchanged"] and dossier["distinct_metabolite"]["unchanged"]


@pytest.mark.parametrize("gene,accession,locus,sgd,version,sequence_version", [
    ("ADO1", "P47143", "YJR105W", "S000003866", 200, 1),
    ("ADK1", "P07170", "YDR226W", "S000002634", 237, 2),
])
def test_distinct_reference_loci(dossier, gene, accession, locus, sgd, version, sequence_version):
    references = {r["gene"]: r for r in dossier["reference_proteins"]}
    assert set(references) == {"ADO1", "ADK1"}
    row = references[gene]
    assert row["protein_accession"] == "UniProtKB:" + accession
    assert row["reference_locus"] == locus and row["sgd_id"] == "SGD:" + sgd
    assert (row["entry_version"], row["sequence_version"]) == (version, sequence_version)
    assert row["reviewed"] and row["scope"] == "REFERENCE_IDENTITY_ONLY"
    assert row["experimental_assignment"] is False
    assert row["reference_taxon_id"] == "NCBITaxon:559292"
    assert row["database_cites_holbein_2009"] is False


def test_species_and_reference_strain_are_not_interchanged(dossier):
    taxa = {r["taxon_id"]: r for r in dossier["taxonomy"]}
    assert taxa["NCBITaxon:4932"]["rank"] == "species"
    assert taxa["NCBITaxon:4932"]["scientific_name"] == "Saccharomyces cerevisiae"
    assert taxa["NCBITaxon:559292"]["rank"] == "strain"
    assert taxa["NCBITaxon:559292"]["scope"] == "REFERENCE_PROTEIN_TAXON_ONLY"
    assert taxa["NCBITaxon:559292"]["parent_taxon_id"] == "NCBITaxon:4932"
    assert dossier["primary_lead"]["species_taxon_id"] == "NCBITaxon:4932"
    assert dossier["primary_lead"]["experimental_identifiers_assigned"] is False


def test_public_export_has_no_experimental_specifications(dossier):
    forbidden = {"sequence", "features", "variant", "alteration", "construct", "primer",
                 "mic", "mic_value", "disk_diffusion", "strain_taxon_id", "assembly_accession",
                 "biosample_accession", "experimental_protein_accession"}

    def inspect(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)

    inspect(dossier)
    assert dossier["uniprot"]["sequence_or_variant_data_exported"] is False


def test_access_and_preservation_are_reported_without_false_success(dossier):
    assert all(r["direct_http_status"] == 403 for r in dossier["access_limitations"])
    assert dossier["uniprot"]["release"] == "2026_03"
    assert dossier["uniprot"]["request"]["status"] == 200
    assert dossier["uniprot"]["request"]["url"].startswith("https://rest.uniprot.org/")
    assert dossier["preservation"]["records_unchanged"] == 2939
    assert dossier["preservation"]["protected_files"] == 6322
    assert dossier["preservation"]["ignored_files_included"] is True

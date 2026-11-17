"""Guard assayed drug form and reference-gene aliases in the sordarin review."""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-sordarin-compound-scope.json").read_text())


def test_growth_screen_maps_to_derivative_not_title_compound(dossier):
    study = next(s for s in dossier["studies"] if s["year"] == 2008)
    assert study["reference"] == "PMID:18285480"
    assert study["assay_compound_name"] == "GM193663"
    assert study["assay_record_identifier"] == "CHEBI:77908"
    assert study["compound_scope"] == "GM193663_GROWTH_SCREEN_AND_DPH_FOLLOWUP"
    assert study["genes_reviewed"] == ["DPH1", "DPH2", "DPH3", "DPH4", "DPH5"]
    assert "radioligand" in study["limitation"]


def test_sodium_salt_cannot_be_assigned_to_neutral_record(dossier):
    study = next(s for s in dossier["studies"] if s["year"] == 2013)
    assert study["doi"] == "10.1371/journal.pgen.1003334"
    assert study["assay_compound_name"] == "sordarin sodium salt"
    assert study["assay_record_identifier"] is None
    assert study["compound_scope"] == "SODIUM_SALT_NOT_NEUTRAL_SORDARIN_OR_GM193663"
    assert study["native_primary_file_cached"] is True
    assert study["curation_decision"] == "HOLD_FOR_EXACT_DRUG_FORM_AND_PRIMARY_SUBJECT_REVIEW"


@pytest.mark.parametrize("gene,primary,accession,locus", [
    ("DPH1", "DPH1", "P40487", "YIL103W"),
    ("DPH2", "DPH2", "P32461", "YKL191W"),
    ("DPH3", "KTI11", "Q3E840", "YBL071W-A"),
    ("DPH4", "JJJ3", "P47138", "YJR097W"),
    ("DPH5", "DPH5", "P32469", "YLR172C"),
    ("DPH6", "DPH6", "Q12429", "YLR143W"),
    ("DPH7", "RRT2", "P38332", "YBR246W"),
])
def test_reference_aliases_do_not_become_experimental_assignments(dossier, gene, primary, accession, locus):
    refs = {r["paper_gene"]: r for r in dossier["reference_proteins"]}
    row = refs[gene]
    assert row["uniprot_primary_gene"] == primary
    assert row["accession"] == "UniProtKB:" + accession and row["reference_locus"] == locus
    if gene != primary:
        assert gene in row["uniprot_gene_synonyms"]
    assert row["reference_taxon_id"] == "NCBITaxon:559292"
    assert row["scope"] == "REFERENCE_IDENTITY_ONLY" and row["experimental_assignment"] is False
    assert row["sequence_version"] == 1 and row["reviewed"] is True


def test_compound_records_have_distinct_structures(dossier):
    records = {r["identifier"]: r for r in dossier["records"]}
    assert set(records) == {"CHEBI:52549", "CHEBI:77908", "CHEBI:140259"}
    assert records["CHEBI:77908"]["standard_inchi_key"] == "YIJXUKFDZCRZIC-MYOGCEHNSA-N"
    assert records["CHEBI:52549"]["standard_inchi_key"] == "OGGVRVMISBQNMQ-YPBSLCSMSA-N"
    assert len({r["standard_inchi_key"] for r in records.values()}) == 3


def test_review_is_partial_and_does_not_assign_strain_ids(dossier):
    assert dossier["curated"] is False and dossier["whole_record_primary_review_complete"] is False
    for study in dossier["studies"]:
        assert study["species_taxon_id"] == "NCBITaxon:4932"
        assert study["experimental_identifiers_assigned"] is False
        assert study["figures_visually_inspected"] is False
        assert study["curation_decision"].startswith("HOLD_")
    taxa = {r["taxon_id"]: r for r in dossier["taxonomy"]}
    assert taxa["NCBITaxon:4932"]["rank"] == "species"
    assert taxa["NCBITaxon:559292"]["scope"] == "REFERENCE_PROTEIN_TAXON_ONLY"


def test_public_export_is_identity_and_qualitative_metadata(dossier):
    forbidden = {"sequence", "features", "variant", "alteration", "construct", "primer",
                 "mic", "mic_value", "dose", "strain_taxon_id", "assembly_accession", "biosample_accession"}

    def check(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(dossier)
    assert dossier["uniprot"]["sequence_data_exported"] is False
    assert dossier["uniprot"]["release"] == "2026_03"
    assert len(dossier["uniprot"]["requests"]) == 2
    assert dossier["preservation"]["records_unchanged"] == 2939
    assert dossier["name_search"]["ignored_files_included"] is True

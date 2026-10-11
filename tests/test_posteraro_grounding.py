"""A primary subject label does not establish protein or modern species identity."""

import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from phibase_grounding_reviews import row_digest  # noqa: E402


@pytest.fixture(scope="module")
def context():
    path = ROOT / "research/2026-10-09-posteraro-subject-reference-grounding.json"
    dossier = json.loads(path.read_text())
    reviews = json.loads((ROOT / "curation/phibase_grounding_reviews.json").read_text())
    review, = [r for r in reviews["reviews"] if r["review_id"] == dossier["review_id"]]
    with (ROOT / "data/raw/phibase_amr.tsv").open() as handle:
        source, = [r for r in csv.DictReader(handle, delimiter="\t") if r["pmid"] == "12519188"]
    record = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claim, = [c for c in record["resistance_mechanisms"] if c["evidence"][0]["reference"] == "PMID:12519188"]
    return dossier, review, source, record, claim


def test_primary_subject_replaces_unverified_source_spelling(context):
    dossier, review, source, record, claim = context
    assert source["strain_label"] == "BYP22"
    assert claim["strain"] == review["subject_strain"] == "BPY22.17"
    assert dossier["subject"]["primary_parent"] == "BPY22"
    assert "source spelling BYP22 is preserved, not treated as a verified synonym" in claim["note"]
    assert "Original source background label: BYP22." in claim["note"]
    assert record["identifier"] == "CHEBI:46081"
    assert record["chemical_structure"]["standard_inchi_key"] == "RFHAOTPXVQNOHP-UHFFFAOYSA-N"
    assert len(record["resistance_mechanisms"]) == 77 and len(record["activity_spectrum"]) == 2


def test_source_biology_is_not_reinterpreted(context):
    dossier, review, source, _, claim = context
    assert claim["alteration"] == source["modification"]
    assert claim["phenotype_id"] == source["phenotype_id"]
    assert claim["phenotype_label"] == source["phenotype_label"]
    assert claim["assay"] == source["evidence_code"]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["taxon_label"] == source["taxon_label"] == "Cryptococcus neoformans"
    assert dossier["source_row_sha256"] == row_digest(source)
    assert review["source_rows"] == [{"identifier": "CHEBI:46081", "row_sha256": row_digest(source)}]
    pin = dossier["source_inventory"]
    assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]


def test_uncertain_identifiers_remain_provenance_only(context):
    dossier, review, _, _, claim = context
    assert review["withhold"] == ["taxon_id", "protein_accession"]
    assert not {"taxon_id", "protein_accession", "strain_taxon_id", "gene_id"} & claim.keys()
    assert "taxon_id=NCBITaxon:5207; protein_accession=UniProtKB:Q8X0Z3" in claim["note"]
    assert dossier["subject"]["modern_species_assignment"] is None
    assert dossier["subject"]["exact_experimental_protein_assigned"] is False
    assert dossier["unresolved_taxonomy_lead"]["taxon_id"] == "NCBITaxon:40410"
    assert dossier["unresolved_taxonomy_lead"]["paper_qualified_name_field"] == "otherNames"
    assert dossier["unresolved_taxonomy_lead"]["experimental_assignment"] is False


def test_paper_citation_does_not_resolve_conflicting_deposit_context(context):
    dossier = context[0]
    protein = dossier["reference_protein"]
    assert protein["primaryAccession"] == "Q8X0Z3"
    assert protein["entryType"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["entryAudit"] == {"entryVersion": 116, "sequenceVersion": 1}
    assert protein["genes"][0]["geneName"]["value"] == "AFR1"
    assert protein["reference_strain"] == "CR 22.17" and protein["citation"] == "PMID:12519188"
    assert protein["archive_cross_reference"]["id"] == "AJ318062"
    assert protein["experimental_assignment"] is False
    assert dossier["primary_evidence"]["paper_genomic_deposit"] == "AJ428201"
    search = dossier["archive_search"]
    assert search["query"] == "AJ428201" and search["result_count"] == 0
    assert search["complete_for_query"] is True
    assert search["zero_results_establish_absence"] is False and search["suggestions_adopted"] is False


@pytest.mark.parametrize("key", [
    "reference_protein", "reference_taxonomy", "unresolved_taxonomy_lead", "archive_search",
])
def test_sequence_free_uniprot_provenance(context, key):
    request = context[0][key]["request"]
    assert request["url"].startswith("https://rest.uniprot.org/")
    assert request["status"] == 200 and request["release"] == "2026_03"
    assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64


def test_curation_coverage_is_not_full_review(context):
    dossier = context[0]
    assert dossier["changes"] == {"new_scoped_claims": 1, "checksum_only_claims": 184,
                                  "changed_records": 22, "byte_identical_records": 2917}
    assert dossier["coverage"] == {"phi_associations": 217, "identifier_scoped": 185,
                                   "pending_associations": 32, "pending_papers": 13,
                                   "whole_records_completed_by_this_review": 0}
    primary = dossier["primary_evidence"]
    assert primary["full_phenotype_validation"] is False
    assert primary["figures_visually_inspected"] is False and primary["native_primary_file_cached"] is False
    assert dossier["embedding_scope"]["changed_records_with_identical_documents"] == 22
    assert dossier["embedding_scope"]["artifacts_changed"] is False
    assert dossier["preservation"]["ignored_files_included"] is True


def test_public_dossier_omits_experimental_specifications(context):
    forbidden = {"sequence", "features", "variant", "alteration", "construct", "primer", "mic", "mic_value",
                 "disk_diffusion", "strain_taxon_id", "assembly_accession", "biosample_accession",
                 "experimental_protein_accession"}

    def inspect(value):
        if isinstance(value, dict):
            assert not forbidden & value.keys()
            for child in value.values():
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)

    inspect(context[0])

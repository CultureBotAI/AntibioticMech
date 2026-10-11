"""The restricted cohort lead must not become an experimental allele assignment."""

import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    path = ROOT / "research/2026-10-09-dkag124-cohort-reference-grounding.json"
    return json.loads(path.read_bytes())


def test_reference_protein_is_not_a_clinical_allele(dossier):
    reference = dossier["reference_protein"]
    assert reference["role"] == "MODELLING_REFERENCE_ONLY"
    assert reference["assigned_to_clinical_isolates"] is False
    protein = reference["metadata"]
    assert protein["primaryAccession"] == "Q4WNT5"
    assert protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert protein["entryAudit"]["entryVersion"] == 146
    assert protein["entryAudit"]["sequenceVersion"] == 1
    assert protein["genes"][0]["geneName"]["value"] == "cyp51A"
    assert protein["genes"][0]["orfNames"] == [{"value": "AFUA_4G06890"}]
    assert protein["organism"]["taxonId"] == 330879
    assert "Af293" in protein["organism"]["scientificName"]


def test_species_reference_strain_and_laboratory_subjects_remain_separate(dossier):
    taxonomy = dossier["taxonomy"]
    assert taxonomy["330879"]["rank"] == "strain"
    assert taxonomy["330879"]["parent"]["taxonId"] == 746128
    assert taxonomy["746128"]["rank"] == "species"
    assert taxonomy["746128"]["scientificName"] == "Aspergillus fumigatus"
    assert dossier["cohort"]["species_taxon_id"] == "NCBITaxon:746128"
    assert dossier["laboratory_context"] == {
        "background_label": "PyrG+", "joined_to_clinical_isolates": False,
        "joined_to_reference_assembly_or_protein": False,
    }


def test_reference_assembly_is_not_an_isolate_genome(dossier):
    assert dossier["reference_assembly"] == {
        "source_label": "GCA_000150145.1_ASM15014v1", "accession": "GCA_000150145.1",
        "role": "READ_MAPPING_REFERENCE_ONLY", "strain_crosswalk": "NOT_INDEPENDENTLY_VERIFIED",
        "assigned_to_clinical_isolates": False,
    }
    assert dossier["cohort"]["per_isolate_assembly_mapping"] == "NOT_ESTABLISHED"
    assert dossier["cohort"]["exact_experimental_alleles"] == "NOT_ASSIGNED"


def test_cohort_counts_do_not_imply_every_drug_is_resisted(dossier):
    cohort = dossier["cohort"]
    assert cohort["clinical_isolates"] == cohort["unique_source_isolate_labels"] == 87
    assert cohort["unique_biosample_accessions"] == 87
    assert cohort["bioproject_counts"] == {"PRJNA985736": 35, "PRJNA1301956": 52}
    assert "not every isolate resistant to every drug" in cohort["selection_scope"]
    assert dossier["supplement"]["reviewed_identifier_cells"] == "A3:C89"
    assert dossier["supplement"]["header_range"] == "A2:C2"
    assert dossier["supplement"]["sheet"] == "PAPER - Figure 1"
    assert dossier["supplement"]["docx_relationship_id"] == "rId14"


@pytest.mark.parametrize("identifier,label,inchikey", [
    ("CHEBI:10023", "voriconazole", "BCEHBSKCWLPMDN-MGPLVRAMSA-N"),
    ("CHEBI:85979", "isavuconazole", "DDFOUSQFMYRUQK-RCDICMHDSA-N"),
    ("CHEBI:6076", "itraconazole", "VHVPQPYKVGDNFY-ZPGVKDDISA-N"),
    ("CHEBI:64355", "posaconazole", "RAGOYPUPXAKGKH-XAKZXMRKSA-N"),
])
def test_compound_forms_stay_unresolved_despite_matching_names(dossier, identifier, label, inchikey):
    entry, = [c for c in dossier["compound_leads"] if c["identifier"] == identifier]
    record = load_record(ROOT / entry["record_path"])
    assert entry["record_label"] == record["label"] == label
    assert record["identifier"] == identifier
    assert entry["standard_inchi_key"] == record["chemical_structure"]["standard_inchi_key"] == inchikey
    assert entry["status"] == "NAME_LEVEL_LEAD_TESTED_CHEMICAL_FORM_UNRESOLVED"


def test_license_gate_and_metadata_only_export(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert dossier["status"] == "METADATA_RESEARCH_ONLY_NO_CORPUS_CURATION"
    assert dossier["reuse"]["observed_article_license"] == "CC-BY-NC-4.0"
    assert dossier["reuse"]["decision"] == "NO_SOURCE_ADOPTION_OR_BULK_TABLE_REDISTRIBUTION"
    assert dossier["supplement"]["public_row_export"] is False
    assert not set(keys(dossier)) & {
        "sequence", "features", "alteration", "activity_spectrum", "resistance_mechanisms",
        "biosample_accession", "source_isolate_id", "mic", "measurement_value", "variants",
    }
    assert "SAMN" not in json.dumps(dossier)
    assert not urlsplit(dossier["supplement"]["url"]).query


def test_provenance_separates_cached_inspection_from_visual_review(dossier):
    assert dossier["citation"]["reference"] == "DOI:10.1093/jac/dkag124"
    assert dossier["primary_access"]["visual_review"] is False
    assert dossier["primary_access"]["review_method"] == "CACHED_HTML_AND_NATIVE_EMBEDDED_WORKSHEET_XML"
    assert len(dossier["uniprot_requests"]) == 3
    for request in dossier["uniprot_requests"]:
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["release"] == "2026_03"
        assert request["status"] == 200
        assert len(request["sha256"]) == len(request["cache_file_sha256"]) == 64


def test_overlap_scope_and_pending_claims_are_not_overstated(dossier):
    overlap = dossier["overlap_check"]
    assert overlap["records_loaded"] == 2939
    assert overlap["ignored_files_included"] is True
    assert overlap["exact_biosample_matches"] == 0
    assert "not every raw dataset" in overlap["scope"]
    assert "four pending claims remain pending" in overlap["natesan_scope"]
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 181, "pending_associations": 36, "pending_papers": 16, "retained": 217,
    }
    preserved = dossier["preservation"]
    assert preserved["record_hashes_verified"] == 2939
    assert preserved["biological_record_changes"] == preserved["curation_events_added"] == 0
    assert preserved["discovery_exports_unchanged"] == 18
    assert preserved["source_queue_unchanged"] is True

"""Reference metadata must not imply review of an inaccessible journal subject."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-nguyen-reference-lead.json").read_bytes())


def test_thesis_is_not_final_journal_evidence(dossier):
    thesis = dossier["thesis"]
    assert thesis["version"] == "DISSERTATION_NOT_FINAL_2012_JOURNAL_ARTICLE"
    assert thesis["journal_subject_crosswalk"] == "NOT_ESTABLISHED"
    assert thesis["reference"] == "https://ediss.sub.uni-hamburg.de/handle/ediss/4850"
    assert thesis["urn"] == "urn:nbn:de:gbv:18-61100"
    assert [(p["pdf_page"], p["printed_page"]) for p in thesis["visually_inspected_pages"]] == [
        (31, 15), (69, 53), (159, 143),
    ]
    journal = dossier["journal_citation"]
    assert journal["reference"] == "PMID:22591226"
    assert journal["doi"] == "10.1094/MPMI-02-12-0047-R"
    assert journal["full_text_inspected"] is False
    assert journal["publisher_access"]["status"] == 403
    assert "not evidence" in journal["access_limit"]


def test_reference_accession_and_gene_cross_reference_are_distinct(dossier):
    reference = dossier["reference_protein"]
    assert reference["scope"] == "PH1_REFERENCE_CONTEXT_ONLY_NOT_EXPERIMENTAL_SUBJECT_GROUNDING"
    assert reference["new_subject_accessions_assigned"] is False
    assert reference["source_gene_field_rewritten"] is False
    protein = reference["metadata"]
    assert protein["primaryAccession"] == "P0C431"
    assert protein["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert protein["entryAudit"]["entryVersion"] == 110
    assert protein["entryAudit"]["sequenceVersion"] == 1
    assert protein["organism"]["taxonId"] == 229533
    assert "PH-1" in protein["organism"]["scientificName"]
    assert "FGSG_09612" in {v["value"] for g in protein["genes"] for v in g["orfNames"]}
    cross_reference = reference["ensembl_fungi_cross_reference"]
    properties = {v["key"]: v["value"] for v in cross_reference["properties"]}
    assert cross_reference["database"] == "EnsemblFungi"
    assert cross_reference["id"] == reference["source_gene_field"] == "FGRAMPH1_01T26671"
    assert properties["GeneId"] == reference["gene_id_property"] == "FGRAMPH1_01G26671"
    assert properties["ProteinId"] == "FGRAMPH1_01T26671-p1"
    assert cross_reference["id"] != properties["GeneId"]


def test_taxonomic_rank_does_not_identify_a_tested_subject(dossier):
    taxonomy = dossier["taxonomy"]
    assert taxonomy["5518"]["rank"] == "species"
    assert "Fusarium graminearum" in taxonomy["5518"]["synonyms"]
    assert taxonomy["229533"]["rank"] == "strain"
    assert taxonomy["229533"]["parent"]["taxonId"] == 5518
    assert dossier["reference_protein"]["new_subject_accessions_assigned"] is False


@pytest.mark.parametrize("identifier", ["CHEBI:16240", "CHEBI:81763"])
def test_leads_pin_existing_source_rows_not_new_assays(dossier, identifier):
    lead, = [r for r in dossier["source_associations"] if r["identifier"] == identifier]
    assert lead["status"] == "PENDING_JOURNAL_SUBJECT_IDENTITY_REVIEW"
    record = load_record(ROOT / lead["record_path"])
    assert record["identifier"] == identifier
    assert record["chemical_structure"]["standard_inchi_key"] == lead["standard_inchi_key"]
    with (ROOT / "data/raw/phibase_amr.tsv").open() as handle:
        row, = [r for r in csv.DictReader(handle, delimiter="\t")
                if r["pmid"] == "22591226" and r["identifier"] == identifier]
    payload = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    assert hashlib.sha256(payload).hexdigest() == lead["source_row_sha256"]
    assert row["phig_id"] == lead["phig_id"] == "PHIG:7590"


def test_historical_checkpoint_does_not_count_leads_as_reviewed(dossier):
    assert dossier["status"] == "REFERENCE_LEAD_ONLY_NO_CORPUS_CURATION"
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 182, "pending_associations": 35, "pending_papers": 15, "retained": 217,
    }
    preserved = dossier["preservation"]
    assert preserved["record_hashes_verified"] == 2939
    assert preserved["record_path_search_includes_ignored"] is True
    assert preserved["biological_record_changes"] == preserved["curation_events_added"] == 0


def test_export_is_metadata_only(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert "no additional reuse rights" in dossier["thesis"]["reuse"]
    assert not set(keys(dossier)) & {
        "sequence", "features", "variants", "alteration", "resistance_mechanisms",
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers",
    }
    assert "No NCBI request" in " ".join(dossier["limitations"])


def test_cached_evidence_has_replayable_provenance(dossier):
    assert dossier["thesis"]["pdf"]["sha256"] == (
        "0734561ff7e07d6325dfa4a65e96aa6b4a8a70d83a5549391411f15b7156193a"
    )
    assert len(dossier["uniprot_requests"]) == 3
    for request in dossier["uniprot_requests"]:
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert len(request["cache"]["sha256"]) == len(request["sha256"]) == 64

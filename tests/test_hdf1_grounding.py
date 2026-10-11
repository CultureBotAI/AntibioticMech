"""The HDF1 subject correction cannot assign parent or unresolved locus identifiers."""

import csv
import json
import sys
from pathlib import Path

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seed_from_sources as seed  # noqa: E402


def test_hdf1_subject_is_ym1_not_parent_or_comparator():
    record = load_record(ROOT / "data/antibiotics/biocide/hydrogen-peroxide.yaml")
    row, = [r for r in csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t")
            if r["pmid"] == "21138346"]
    claim, = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:21138346"]
    assert record["identifier"] == row["identifier"] == "CHEBI:16240"
    assert record["chemical_structure"]["standard_inchi_key"] == "MHAJPDPJQMAIIY-UHFFFAOYSA-N"
    assert row["strain_label"] == "PH-1" and claim["strain"] == "YM1"
    assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"] == "NCBITaxon:5518"
    assert claim["alteration"] == row["modification"]
    assert claim["phenotype_id"] == row["phenotype_id"]
    assert claim["phenotype_label"] == row["phenotype_label"] and claim["assay"] == row["evidence_code"]
    assert not any(k in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
    assert "Original source background label: PH-1." in claim["note"]
    assert "protein_accession=UniProtKB:I1RCN2" in claim["note"]
    assert "strain_taxon_id=NCBITaxon:229533" in claim["note"]
    assert "distinct from parent PH-1 and comparator YM11" in claim["note"]
    assert "not asserted equivalent without an authoritative alias crosswalk" in claim["note"]
    assert claim["evidence"][-1]["reference"] == "DOI:10.1094/MPMI-10-10-0233"


def test_hdf1_source_reproduction_preserves_all_six_claims():
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    stats = seed.attach_phibase_resistance(fixture)
    assert stats["reviewed_identifier_context"] == 185 and stats["matched_associations"] == 217
    record = load_record(ROOT / "data/antibiotics/biocide/hydrogen-peroxide.yaml")
    assert fixture["CHEBI:16240"]["resistance_mechanisms"] == record["resistance_mechanisms"]
    assert len(record["resistance_mechanisms"]) == 6
    assert len(record["clinical_status_assertions"]) == 1
    assert record.get("activity_spectrum", []) == []


def test_hdf1_dossier_preserves_primary_and_reference_scope():
    dossier = json.loads((ROOT / "research/2026-10-09-hdf1-subject-reference-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 182, "pending_associations": 35, "pending_papers": 15, "retained": 217,
    }
    assert dossier["changes"] == {
        "byte_identical_records": 2918, "changed_records": 21,
        "checksum_only_claims": 181, "new_scoped_claims": 1,
    }
    assert dossier["subject_context"] == {
        "source_background_label": "PH-1", "tested_subject": "YM1",
        "comparator_subject": "YM11", "experimental_accessions_assigned": False,
    }
    primary = dossier["primary_access"]
    assert primary["review_method"] == "CACHED_PUBLISHED_PDF_TEXT_AND_VISUAL_IDENTITY_REVIEW"
    assert primary["visually_inspected_pages"] == [488, 489, 492]
    assert primary["pdf"]["sha256"] == "5b3da878e874d79f8e47ef4d42895087c14b526e04edc59a9446b2504e1daed5"
    protein = dossier["protein"]
    assert protein["primaryAccession"] == "I1RCN2" and protein["organism"]["taxonId"] == 229533
    assert protein["entryAudit"]["entryVersion"] == 85 and protein["entryAudit"]["sequenceVersion"] == 1
    assert "sequence" not in protein and "features" not in protein
    assert dossier["taxonomy"]["229533"]["parent"]["taxonId"] == 5518
    assert dossier["taxonomy"]["5518"]["rank"] == "species"
    assert "Fusarium graminearum" in dossier["taxonomy"]["5518"]["synonyms"]


def test_empty_historical_locus_search_is_not_a_gene_absence_claim():
    dossier = json.loads((ROOT / "research/2026-10-09-hdf1-subject-reference-grounding.json").read_bytes())
    crosswalk = dossier["locus_crosswalk"]
    assert crosswalk["paper_locus"] == "FGSG_01353"
    assert crosswalk["uniprot_locus"] == "FGRAMPH1_01T03337"
    assert crosswalk["status"] == "UNRESOLVED_AUTHORITATIVE_ALIAS_CROSSWALK"
    assert crosswalk["sequence_identity_inferred"] is False
    assert crosswalk["bounded_search"] == {
        "query": "gene:FGSG_01353", "exact_results": 0, "spelling_suggestions_adopted": False,
        "interpretation": "No result for this query, not proof of gene absence.",
    }

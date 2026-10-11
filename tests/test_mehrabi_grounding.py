"""Grouped experimental subjects must not inherit IPO323 reference accessions."""

import csv
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seed_from_sources as seed  # noqa: E402


@pytest.mark.parametrize("slug,identifier,total", [
    ("iprodione", "CHEBI:28909", 15), ("fludioxonil", "CHEBI:81763", 13),
])
def test_mehrabi_preserves_source_context_without_assigning_reference_accessions(slug, identifier, total):
    record = load_record(ROOT / f"data/antibiotics/antifungal/{slug}.yaml")
    row, = [r for r in csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t")
            if r["identifier"] == identifier and r["pmid"] == "17073308"]
    claim, = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:17073308"]
    assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert len(record["resistance_mechanisms"]) == total and not record.get("activity_spectrum")
    assert claim["strain"] == row["strain_label"] == "IPO323"
    assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"] == "NCBITaxon:1047171"
    assert claim["gene_id"] == row["gene_id"] == "Mycgr3T76502"
    assert not any(claim.get(k) for k in ("protein_accession", "strain_taxon_id"))
    assert claim["alteration"] == row["modification"] and "[Not assayed]" in claim["alteration"]
    assert claim["phenotype_id"] == row["phenotype_id"]
    assert claim["phenotype_label"] == row["phenotype_label"] and claim["assay"] == row["evidence_code"]
    assert "grouped set of three derivatives" in claim["note"]
    assert "reference locus, not an experimental allele identifier" in claim["note"]
    assert "protein_accession=UniProtKB:Q1KTF2" in claim["note"]
    assert "strain_taxon_id=NCBITaxon:336722" in claim["note"]
    assert claim["evidence"][-1]["reference"] == "DOI:10.1094/mpmi-19-1262"
    assert "direct download HTTP 403, no local PDF or visual page review" in claim["evidence"][-1]["notes"]


def test_mehrabi_source_reproduction_matches_both_records():
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    assert seed.attach_phibase_resistance(fixture)["reviewed_identifier_context"] == 185
    for slug, identifier in (("iprodione", "CHEBI:28909"), ("fludioxonil", "CHEBI:81763")):
        record = load_record(ROOT / f"data/antibiotics/antifungal/{slug}.yaml")
        assert fixture[identifier]["resistance_mechanisms"] == record["resistance_mechanisms"]


def test_mehrabi_dossier_separates_reference_crosswalk_and_primary_access_limit():
    dossier = json.loads((ROOT / "research/2026-10-08-mehrabi-parent-reference-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 180, "pending_associations": 37, "pending_papers": 17, "retained": 217,
    }
    assert dossier["changes"] == {
        "byte_identical_records": 2918, "changed_records": 21,
        "checksum_only_claims": 178, "new_scoped_claims": 2,
    }
    protein = dossier["protein"]
    assert protein["primaryAccession"] == "Q1KTF2" and protein["organism"]["taxonId"] == 336722
    assert protein["entryAudit"]["entryVersion"] == 108 and protein["entryAudit"]["sequenceVersion"] == 2
    assert protein["source_paper_reference"]["citation"]["id"] == "17073308"
    assert "sequence" not in protein and "features" not in protein
    refs = protein["reference_cross_references"]
    deposit, = [r for r in refs if r["database"] == "EMBL" and r["id"] == "DQ432031"]
    assert {"key": "ProteinId", "value": "ABD92790.2"} in deposit["properties"]
    assert any(r["database"] == "EnsemblFungi" and r["id"] == "Mycgr3T76502" for r in refs)
    assert dossier["taxonomy"]["336722"]["parent"]["taxonId"] == 1047171
    assert dossier["taxonomy"]["1047171"]["rank"] == "species"
    access = dossier["primary_access"]
    assert access["review_method"] == "WEB_EXTRACTED_PRIMARY_PDF_TEXT"
    assert access["direct_download_http_status"] == 403 and access["local_pdf_cached"] is False
    assert access["visually_inspected_pages"] == [] and access["offline_primary_text_replay"] is False
    assert "No new variant, sequence, construct, protocol, numeric measurement or MIC was curated." in (
        dossier["limitations"])

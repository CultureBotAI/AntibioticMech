"""Parent-reference identities must not become experimental allele assignments."""

import csv
import json
import sys
from pathlib import Path

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seed_from_sources as seed  # noqa: E402


def test_shima_subjects_preserve_source_fields_without_reference_identifiers():
    record = load_record(ROOT / "data/antibiotics/antifungal/carboxin.yaml")
    assert record["identifier"] == "CHEBI:3405"
    assert record["chemical_structure"]["standard_inchi_key"] == "GYSSRZJIHXQEHQ-UHFFFAOYSA-N"
    assert len(record["resistance_mechanisms"]) == 36
    assert not record.get("activity_spectrum")
    claims = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:18992352"]
    rows = [r for r in csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t")
            if r["pmid"] == "18992352"]
    assert len(claims) == len(rows) == 2
    for row in rows:
        claim, = [c for c in claims if "UniProtKB:" + row["protein_accession"] in c["note"]]
        assert claim["strain"] == row["strain_label"] == "RIB40"
        assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"] == "NCBITaxon:5062"
        assert claim["taxon_label"] == row["taxon_label"] == "Aspergillus oryzae"
        assert not any(claim.get(k) for k in ("protein_accession", "strain_taxon_id", "gene_id"))
        assert claim["alteration"] == row["modification"]
        assert claim["phenotype_id"] == row["phenotype_id"]
        assert claim["phenotype_label"] == row["phenotype_label"]
        assert claim["assay"] == row["evidence_code"]
        assert "parent background, not a unique tested transformant" in claim["note"]
        assert "donor deposits do not identify later transformants" in claim["note"]
        assert "strain_taxon_id=NCBITaxon:510516" in claim["note"]
        assert "The 2009 full text remains unavailable" in claim["note"]
        assert claim["evidence"][-1]["reference"] == "DOI:10.1271/bbb.100687"


def test_shima_source_reproduction_matches_curated_record():
    record = load_record(ROOT / "data/antibiotics/antifungal/carboxin.yaml")
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    stats = seed.attach_phibase_resistance(fixture)
    assert stats["reviewed_identifier_context"] == 185
    assert fixture["CHEBI:3405"]["resistance_mechanisms"] == record["resistance_mechanisms"]


def test_shima_dossier_separates_followup_from_unavailable_original():
    dossier = json.loads((ROOT / "research/2026-10-08-shima-parent-reference-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 178, "pending_associations": 39, "pending_papers": 18, "retained": 217,
    }
    assert dossier["changes"] == {
        "byte_identical_records": 2918, "changed_records": 21,
        "checksum_only_claims": 176, "new_scoped_claims": 2,
    }
    primary = dossier["primary_followup"]
    assert primary["reference"] == "DOI:10.1271/bbb.100687"
    assert primary["edition"] == "FINAL_PUBLISHED_2011_PAGES_181_184"
    assert primary["sha256"] == "58802bdf088173a50d1d02319068380caab5609c8ce933e1f5bb8e578fc282b0"
    assert primary["visually_inspected_pages"] == [181, 182, 184]
    assert dossier["original_study"]["reference"] == "PMID:18992352"
    assert dossier["original_study"]["fulltext_reviewed"] is False


def test_shima_dossier_retains_only_reference_metadata():
    dossier = json.loads((ROOT / "research/2026-10-08-shima-parent-reference-grounding.json").read_bytes())
    assert set(dossier["proteins"]) == {"Q2TWM0", "Q2U3V9"}
    for accession, expected_version, locus in (
        ("Q2TWM0", 127, "AO090010000505"), ("Q2U3V9", 98, "AO090020000596"),
    ):
        protein = dossier["proteins"][accession]
        assert protein["organism"]["taxonId"] == 510516
        assert protein["entryAudit"]["entryVersion"] == expected_version
        assert protein["entryAudit"]["sequenceVersion"] == 1
        assert locus in json.dumps(protein["genes"])
        assert "sequence" not in protein and "features" not in protein
    assert dossier["taxonomy"]["510516"]["parent"]["taxonId"] == 5062
    assert dossier["taxonomy"]["5062"]["rank"] == "species"
    assert "No new variant, sequence, construct, protocol, numeric measurement or MIC was curated." in (
        dossier["limitations"])

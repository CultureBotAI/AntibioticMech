"""A verified reference alias must not identify an experimental allele."""

import csv
import json
import sys
from pathlib import Path

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import seed_from_sources as seed  # noqa: E402


def test_huang_preserves_source_claim_and_keeps_reference_identifiers_in_provenance():
    record = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    row, = [r for r in csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t")
            if r["pmid"] == "39403939"]
    claim, = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:39403939"]
    assert record["identifier"] == row["identifier"] == "CHEBI:46081"
    assert record["chemical_structure"]["standard_inchi_key"] == "RFHAOTPXVQNOHP-UHFFFAOYSA-N"
    assert len(record["resistance_mechanisms"]) == 77 and len(record["activity_spectrum"]) == 2
    assert len(record["clinical_status_assertions"]) == 118
    assert claim["strain"] == row["strain_label"] == "SC5314"
    assert claim["taxon_id"] == "NCBITaxon:" + row["taxon_id"] == "NCBITaxon:5476"
    assert claim["alteration"] == row["modification"]
    assert claim["phenotype_id"] == row["phenotype_id"]
    assert claim["phenotype_label"] == row["phenotype_label"] and claim["assay"] == row["evidence_code"]
    assert not any(k in claim for k in ("protein_accession", "strain_taxon_id", "gene_id"))
    assert "parent background, not the separately tested derivative" in claim["note"]
    assert "protein_accession=UniProtKB:A0A1D8PGP5" in claim["note"]
    assert "strain_taxon_id=NCBITaxon:237561" in claim["note"]
    assert "aliases of SDH8 reference locus C2_02620W_A, primary CGDID CAL0000192813" in claim["note"]
    assert "not an experimental allele" in claim["note"]
    assert claim["evidence"][-1]["reference"] == "DOI:10.1080/21505594.2024.2405000"


def test_huang_source_reproduction_keeps_all_prior_fluconazole_claims():
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    assert seed.attach_phibase_resistance(fixture)["reviewed_identifier_context"] == 185
    record = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claims = [c for c in record["resistance_mechanisms"] if seed.is_phibase_sourced_resistance(c)]
    assert fixture["CHEBI:46081"]["resistance_mechanisms"] == claims


def test_historical_huang_dossier_keeps_its_original_unresolved_status_and_metadata_scope():
    dossier = json.loads((ROOT / "research/2026-10-08-huang-parent-reference-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 181, "pending_associations": 36, "pending_papers": 16, "retained": 217,
    }
    assert dossier["changes"] == {
        "byte_identical_records": 2918, "changed_records": 21,
        "checksum_only_claims": 180, "new_scoped_claims": 1,
    }
    protein = dossier["protein"]
    assert protein["primaryAccession"] == "A0A1D8PGP5" and protein["organism"]["taxonId"] == 237561
    assert protein["entryAudit"]["entryVersion"] == 35 and protein["entryAudit"]["sequenceVersion"] == 1
    assert len(protein["source_paper_go_references"]) == 4
    assert "sequence" not in protein and "features" not in protein
    assert dossier["taxonomy"]["237561"]["parent"]["taxonId"] == 5476
    assert dossier["taxonomy"]["5476"]["rank"] == "species"
    crosswalk = dossier["locus_crosswalk"]
    assert crosswalk["paper_locus"] == "orf19.1588" and crosswalk["uniprot_locus"] == "orf19.9161"
    assert crosswalk["status"] == "UNRESOLVED_AUTHORITATIVE_ALIAS_CROSSWALK"
    assert crosswalk["sequence_identity_inferred"] is False
    assert dossier["primary_access"]["review_method"] == "CACHED_PRIMARY_XML_IDENTITY_CONTEXT"
    assert dossier["primary_access"]["visual_figure_review"] is False
    assert "No new variant, sequence, construct, protocol, numeric measurement or MIC was curated." in (
        dossier["limitations"])

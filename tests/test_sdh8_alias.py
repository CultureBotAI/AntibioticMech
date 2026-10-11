"""An explicit reference alias does not ground a tested resistance allele."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-sdh8-locus-crosswalk.json").read_bytes())


@pytest.mark.parametrize("alias", ["orf19.1588", "orf19.9161"])
def test_each_alias_is_explicit_not_an_inferred_name_normalization(dossier, alias):
    crosswalk = dossier["reference_crosswalk"]
    row, = [r for r in crosswalk["mapping_rows"] if r["ORF19_ID"] == alias]
    assert row == {"ORF19_ID": alias, "ASSEMBLY22_ID": "C2_02620W_A", "GENE_NAME": "SDH8"}
    assert alias in crosswalk["feature"]["matched_aliases"]
    assert crosswalk["name_normalization_inferred"] is False
    assert crosswalk["sequence_comparison_performed"] is False


def test_stable_cgd_identifier_is_the_reference_join_key(dossier):
    crosswalk = dossier["reference_crosswalk"]
    assert crosswalk["join_basis"] == "EXACT_STABLE_CGD_IDENTIFIER_AND_EXPLICIT_ALIAS_ROWS"
    assert crosswalk["feature"]["primary_cgd_id"] == "CAL0000192813"
    assert crosswalk["uniprot_cgd_cross_reference"] == {
        "database": "CGD", "id": "CAL0000192813", "properties": [{"key": "GeneName", "value": "SDH8"}],
    }
    assert crosswalk["feature"]["feature_name"] == "C2_02620W_A"
    assert crosswalk["cgd_version"] == "A22-s08-m01-r37"
    assert "version_A22-s08-m01-r37" in dossier["requests"]["features"]["url"]
    assert "current" not in dossier["requests"]["features"]["url"]


def test_reference_entry_and_strain_are_not_experimental_identifiers(dossier):
    protein = dossier["reference_protein"]
    assert protein["primaryAccession"] == "A0A1D8PGP5"
    assert protein["entryType"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["entryAudit"]["entryVersion"] == 35 and protein["entryAudit"]["sequenceVersion"] == 1
    assert protein["organism"]["taxonId"] == 237561
    assert dossier["taxonomy"]["237561"]["rank"] == "strain"
    assert dossier["taxonomy"]["237561"]["parent"]["taxonId"] == 5476
    assert dossier["taxonomy"]["5476"]["rank"] == "species"
    assert dossier["reference_crosswalk"]["experimental_identifiers_assigned"] is False


def test_curated_note_does_not_fill_experimental_gene_or_protein_fields(dossier):
    record = load_record(ROOT / "data/antibiotics/antifungal/fluconazole.yaml")
    claim, = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == dossier["primary_scope"]["reference"]]
    assert record["identifier"] == dossier["compound"]["identifier"] == "CHEBI:46081"
    assert record["chemical_structure"]["standard_inchi_key"] == dossier["compound"]["standard_inchi_key"]
    assert "CAL0000192813" in claim["note"] and "not an experimental allele" in claim["note"]
    assert not {"gene_id", "protein_accession", "strain_taxon_id"} & set(claim)
    assert claim["strain"] == "SC5314" and claim["taxon_id"] == "NCBITaxon:5476"
    notes = claim["evidence"][-1]["notes"]
    assert dossier["requests"]["mapping"]["sha256"] in notes
    assert dossier["requests"]["features"]["sha256"] in notes


def test_previous_dossier_is_a_preserved_historical_checkpoint(dossier):
    prior = dossier["historical_dossier"]
    payload = (ROOT / prior["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == prior["sha256"]
    assert json.loads(payload)["locus_crosswalk"]["status"] == "UNRESOLVED_AUTHORITATIVE_ALIAS_CROSSWALK"
    assert dossier["status"] == "REFERENCE_ALIAS_VERIFIED_NOT_EXPERIMENTAL_ALLELE"


def test_alias_resolution_does_not_inflate_review_or_biological_counts(dossier):
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 184, "pending_associations": 33, "pending_papers": 14, "retained": 217,
    }
    assert dossier["changes"] == {
        "reference_alias_notes_updated": 1, "new_identifier_scope_reviews": 0,
        "checksum_only_claims": 183, "changed_records": 22, "byte_identical_records": 2917,
    }
    assert len(dossier["records"]) == len({r["identifier"] for r in dossier["records"]}) == 22
    assert dossier["preservation"]["record_path_search_includes_ignored"] is True


def test_export_is_limited_to_identity_metadata(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "resistance_mechanisms", "body",
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers",
        "start_coordinate", "stop_coordinate", "chromosome", "description",
    }
    assert set(dossier["reference_protein"]) == {
        "primaryAccession", "entryType", "entryAudit", "organism", "genes",
    }
    assert set(dossier["reference_crosswalk"]["feature"]) == {
        "feature_name", "gene_name", "feature_type", "primary_cgd_id", "matched_aliases",
    }
    assert "No NCBI request" in " ".join(dossier["limitations"])


def test_raw_source_requests_are_pinned_and_redirect_is_not_evidence(dossier):
    requests = dossier["requests"]
    assert requests["legacy_locus"]["status"] == 301
    assert requests["features"]["sha256"] == (
        "087a09f0bbefba9ca94743c19fee18f56e3ce9cddab33bc9b3eba40089abd983")
    assert requests["mapping"]["sha256"] == (
        "722e0ec75f44c1c32ec3e222952015d2ed96cebd52c16fba25665dba84a2bfe1")
    for name, value in requests.items():
        for request in value if isinstance(value, list) else [value]:
            assert urlsplit(request["url"]).hostname in {
                "www.candidagenome.org", "rest.uniprot.org", "www.ebi.ac.uk",
            }
            assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64
            if name != "legacy_locus":
                assert request["status"] == 200

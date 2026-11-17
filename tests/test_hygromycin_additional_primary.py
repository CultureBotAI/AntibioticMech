"""Primary modifier findings must not become experimental resistance alleles."""

import hashlib
import json
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/2026-10-09-hygromycin-additional-primary-grounding.json"


@pytest.fixture(scope="module")
def dossier():
    return json.loads(PATH.read_bytes())


@pytest.mark.parametrize("suffix,pmid,rows,panels", [
    ("000193", "32083242", 7, ["1A", "1B"]),
    ("000403", "34095778", 12, ["1A", "1B", "1C"]),
    ("000738", "36818312", 7, ["1A", "1B"]),
])
def test_primary_studies_keep_distinct_source_memberships(dossier, suffix, pmid, rows, panels):
    study, = [s for s in dossier["primary_studies"] if s["doi"].endswith(suffix)]
    assert study["reference"] == "PMID:" + pmid
    assert len(study["source_subject_rows"]) == rows
    assert study["source_license"] == "CC-BY-4.0"
    review = study["primary_review"]
    assert review["figure_panels_inspected"] == panels
    assert review["figure"]["visually_inspected"] is True
    assert all(len(a["normalized_text_sha256"]) == 64 for a in review["description_anchors"])
    assert study["primary_request"]["url"].endswith(f"micropub-biology-{suffix}.xml")


@pytest.mark.parametrize("gene,accession,locus,sgd,entry,sequence", [
    ("TOM1", "Q03280", "YDR457W", "S000002865", 209, 1),
    ("ASI1", "P54074", "YMR119W", "S000004725", 161, 1),
    ("ASI2", "P53895", "YNL159C", "S000005103", 146, 1),
    ("ASI3", "P53983", "YNL008C", "S000004953", 154, 2),
    ("ATG39", "Q06159", "YLR312C", "S000004303", 132, 1),
    ("ATG40", "Q99325", "YOR152C", "S000005678", 142, 1),
    ("HUL5", "P53119", "YGL141W", "S000003109", 183, 1),
])
def test_reference_identity_is_versioned_not_an_experimental_allele(
    dossier, gene, accession, locus, sgd, entry, sequence,
):
    row, = [r for r in dossier["reference_genes"] if r["gene"] == gene]
    assert row["protein_accession"] == "UniProtKB:" + accession
    assert row["systematic_loci"] == [locus] and row["sgd_cross_reference"] == "SGD:" + sgd
    assert row["entry_audit"] == {"entryVersion": entry, "sequenceVersion": sequence}
    assert row["reference_taxon_id"] == "NCBITaxon:559292" and row["release"] == "2026_03"
    assert row["scope"] == "CANONICAL_REFERENCE_NOT_EXPERIMENTAL_ALLELE_OR_STRAIN"


def test_species_and_reference_strain_are_separate(dossier):
    taxa = {t["taxon_id"]: t for t in dossier["taxonomy"]}
    assert taxa["NCBITaxon:4932"]["rank"] == "species"
    assert taxa["NCBITaxon:4932"]["scope"] == "EXPERIMENTAL_SPECIES"
    assert taxa["NCBITaxon:559292"]["rank"] == "strain"
    assert taxa["NCBITaxon:559292"]["scope"] == "REFERENCE_PROTEIN_TAXON_ONLY"
    assert taxa["NCBITaxon:559292"]["parent_taxon_id"] == "NCBITaxon:4932"
    for study in dossier["primary_studies"]:
        for row in study["source_subject_rows"]:
            assert row["experimental_species_taxon_id"] == "NCBITaxon:4932"
            for field in ("experimental_strain_taxon_id", "experimental_protein_accession",
                          "experimental_allele_accession", "genome_accession"):
                assert row[field] is None


def test_comparisons_use_source_specific_subject_and_comparator_names(dossier):
    assert sum(len(s["comparisons"]) for s in dossier["primary_studies"]) == 13
    assert sum(len(s["source_subject_rows"]) for s in dossier["primary_studies"]) == 26
    for study in dossier["primary_studies"]:
        names = {r["source_subject_name"] for r in study["source_subject_rows"]}
        for comp in study["comparisons"]:
            assert set(comp["source_subjects"]) <= names and comp["source_comparator"] in names
            assert set(comp["panels"]) <= set(study["primary_review"]["figure_panels_inspected"])
            assert comp["evidence_type"] == "FUNCTIONAL_EXPERIMENT"
            for field in ("experimental_strain_taxon_id", "experimental_protein_accession",
                          "experimental_allele_accession", "genome_accession", "mic",
                          "clinical_resistance_interpretation"):
                assert comp[field] is None


def test_negative_and_joint_findings_are_not_flattened(dossier):
    comparisons = [c for s in dossier["primary_studies"] for c in s["comparisons"]]
    assert Counter(c["direction"] for c in comparisons) == {
        "SENSITIZATION_IN_LOSS_COMPARISON": 8,
        "NO_ADDITIONAL_SENSITIZATION_UNDER_TESTED_CONDITIONS": 4,
        "JOINT_SENSITIZATION_NOT_DECOMPOSED": 1,
    }
    negative = [c for c in comparisons if c["direction"].startswith("NO_ADDITIONAL")]
    assert {g for c in negative for g in c["genes"]} == {"ASI2", "HUL5"}
    joint, = [c for c in comparisons if c["direction"].startswith("JOINT_")]
    assert joint["genes"] == ["ATG39", "ATG40"]
    assert joint["source_subjects"] == ["VJY1056 (alias NSY2004)"]


def test_tom1_comparators_are_not_merged(dossier):
    study = dossier["primary_studies"][0]
    rows = {r["source_subject_name"]: r for r in study["source_subject_rows"]}
    assert rows["VJY476"]["source_alias"] == "BY4741"
    assert rows["VJY477"]["source_alias"] == "BY4742"
    assert [c["source_comparator"] for c in study["comparisons"]] == ["VJY476", "VJY477"]


def test_alias_corroboration_does_not_rewrite_the_conflicting_source(dossier):
    flag = dossier["subject_alias_followup"]
    assert flag["status"] == "SKY252_CORROBORATED_SKY242_CONFLICT_NOT_RESOLVED"
    assert not flag["source_aliases_rewritten"] and not flag["cross_study_subjects_merged"]
    assert not flag["background_taxon_assigned_to_derivatives"]
    assert flag["supplement"]["reviewed_location"] == "Table S2, printed S6 / PDF page 6"
    assert flag["supplement"]["visually_inspected"] is True
    prior_pin = dossier["prior_dossier"]
    prior_bytes = (ROOT / prior_pin["path"]).read_bytes()
    assert hashlib.sha256(prior_bytes).hexdigest() == prior_pin["sha256"]
    prior = json.loads(prior_bytes)
    assert flag["flag"] in {f["id"] for f in prior["subject_identity_flags"]}


def test_no_new_resistance_claim_or_operational_export(dossier):
    decision = dossier["curation_decision"]
    assert decision["biological_record_changes"] == decision["curation_events_added"] == 0
    assert dossier["record"]["identifier"] == "CHEBI:16976"
    assert dossier["record"]["standard_inchi_key"] == "GRRNUXAQVGOGFE-NZSRVPFOSA-N"
    assert dossier["record"]["existing_assertions_unchanged"] == 5
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["record_path_search_includes_ignored"] is True
    forbidden = {"sequence", "genotype", "construct", "protocol", "primers", "mic_value", "body", "headers"}

    def check(node):
        if isinstance(node, dict):
            assert not forbidden.intersection(node)
            for value in node.values():
                check(value)
        elif isinstance(node, list):
            for value in node:
                check(value)

    check(dossier)
    assert "All 2939 records remain in scope" in " ".join(dossier["limitations"])
    assert "No NCBI request" in " ".join(dossier["limitations"])

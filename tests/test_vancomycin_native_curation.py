"""Preserve native subjects, biochemical comparators, and reference-only IDs."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-10-vancomycin-native"


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_native_claims_preserve_previous_source_claims_and_all_other_fields(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    doc = load_record(path)
    assert doc["identifier"] == "CHEBI:28001"
    n = curation["existing_claims_preserved"]
    assert n + 2 == 22 and len(doc["resistance_mechanisms"]) >= n + 2
    assert doc["resistance_mechanisms"][n:n + 2] == curation["added_claims"]
    assert semantic_sha(doc["resistance_mechanisms"][:n]) == curation["preserved_resistance_claims_sha256"]
    event_index = doc["curation_history"].index(curation["curation_event"])
    assert semantic_sha(doc["curation_history"][:event_index]) == curation["preserved_history_sha256"]
    other = {k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert doc["curation_status"] == curation["curation_status"] == "SEEDED"
    target = tmp_path / path.name
    write_validated_antibiotic(doc, target)
    assert target.read_bytes() == path.read_bytes() and load_record(target) == doc


def test_vanm_native_cluster_is_not_isolated_ligase_sufficiency(context, curation):
    claim = curation["added_claims"][0]
    assert claim["strain"] == "Efm-HS0661" and claim["taxon_id"] == "NCBITaxon:1352"
    assert claim["taxon_label"] == "Enterococcus faecium"
    assert claim["aro_id"] == "ARO:3000256" and claim["gene_families"] == ["vanM"]
    assert claim["assay"] == "Etest" and "not isolated VanM sufficiency" in claim["note"]
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:20733041"}
    assert context["primary_sources"]["20733041"]["native_precursor_evidence"]
    assert not context["primary_sources"]["20733041"]["laboratory_recipient_assigned_to_native_subject"]
    assert not {"gene_id", "strain_taxon_id"} & claim.keys()


def test_vanm_source_bound_archives_do_not_supply_a_native_genome(context):
    links = {r["nucleotide_accession"]: r for r in context["reference_proteins"]["B8XGS3"]["archive_links"]}
    assert {c["strain"] for c in links["FJ349556"]["strain_reference_bindings"]} == {"Efm-HS0661"}
    assert {c["strain"] for c in links["CP039730"]["strain_reference_bindings"]} == {"ZY2"}
    assert context["archive_context"]["FJ349556"]["sample"] is None
    assert context["archive_context"]["CP039730"]["sample"] == "SAMN10867605"
    assert all(not a["experimental_genome_assignment"] for a in context["archive_context"].values())


def test_y51_locus_is_distinct_from_biochemical_comparator(context, curation):
    claim = curation["added_claims"][1]
    assert claim["gene_id"] == "DSY3690" and claim["strain"] == "Y51"
    assert claim["taxon_id"] == "NCBITaxon:49338" and claim["strain_taxon_id"] == "NCBITaxon:138119"
    assert claim["taxon_label"] == "Desulfitobacterium hafniense"
    assert claim["assay"] == "Disk diffusion and Etest"
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:19414574"}
    assert "not isolated DSY3690 necessity or sufficiency" in claim["note"]
    assert "aro_id" not in claim
    assert context["biochemical_comparator"] == {
        "locus": "DSY1579", "reference": "UniProtKB:Q24X74", "curated_as_resistance_determinant": False}
    assert not context["primary_sources"]["19414574"]["native_precursor_evidence"]
    assert context["primary_sources"]["19414574"]["biochemical_evidence_scope"].startswith(
        "SEPARATE_RECOMBINANT")
    for accession, locus in (("Q24R63", "DSY3690"), ("Q24X74", "DSY1579")):
        gene, = context["reference_proteins"][accession]["gene_annotations"]
        assert gene["geneName"]["value"] == "ddl" and gene["orderedLocusNames"][0]["value"] == locus


@pytest.mark.parametrize("taxid,rank", [("1352", "species"), ("49338", "species"), ("138119", "strain")])
def test_grounding_preserves_taxonomy_rank(context, taxid, rank):
    row = context["taxonomy"][taxid]
    assert row["active"] and row["rank"] == rank
    assert context["taxonomy"]["138119"]["parent"]["taxonId"] == 49338


def test_no_exact_experimental_protein_allele_or_numerical_ast_in_new_claims(curation):
    forbidden = {"protein_accession", "alteration", "assembly_accession", "biosample_accession",
                 "bioproject_accession", "phenotype_id", "measurement_value", "mic_value", "mic_units"}
    for claim in curation["added_claims"]:
        assert not forbidden & claim.keys()
        assert claim["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
        assert claim["phenotype_label"] == "source-reported vancomycin resistance"
        assert "No exact experimental protein, allele or genome" in claim["note"]


def test_existing_cdc_activity_subjects_are_not_joined_by_species(curation):
    doc = load_record(ROOT / curation["record"]["path"])
    assert len(doc["activity_spectrum"]) == 3
    assert {r["strain"] for r in doc["activity_spectrum"]} == {"0781", "0782", "0783"}
    assert not {c["strain"] for c in curation["added_claims"]} & {
        r["strain"] for r in doc["activity_spectrum"]}
    assert all("mic_value" in r for r in doc["activity_spectrum"])


def test_teicoplanin_record_and_component_hold_are_preserved(context):
    hold = context["teicoplanin_disposition"]
    assert hold["source_structure_label"] == "Teicoplanin A2-5"
    assert hold["action"] == "NO_GENERIC_TEICOPLANIN_ASSAY_TO_EXACT_COMPONENT_JOIN"
    pin = context["teicoplanin_at_start"]
    assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]


def test_census_changes_only_the_vancomycin_claim_count_and_hash():
    reconciliation = json.loads(Path(str(PREFIX) + "-checkpoint-reconciliation.json").read_bytes())
    ledgers = []
    for name in ("previous_ledger", "current_ledger"):
        pin = reconciliation[name]
        path = ROOT / pin["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
        with path.open(newline="") as stream:
            ledgers.append(list(csv.DictReader(stream, delimiter="\t")))
    old, new = ledgers
    assert len(old) == len(new) == 2939
    (a, b), = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
    assert b["identifier"] == "CHEBI:28001"
    assert {k for k in a if a[k] != b[k]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 2
    assert reconciliation["current_counts"]["resistance_assertions"] == 4823
    assert reconciliation["curator_claims"] == 68 and reconciliation["curator_records"] == 37


def test_provenance_scope_embeddings_and_all_record_scope(context, curation):
    assert context["chemical_identity"]["standard_inchi_key"] == "MYPYJXKWCTUITO-LYRMYLQWSA-N"
    assert context["chemical_identity"]["key_matches_smiles_and_inchi"]
    assert context["scope"]["corpus_records"] == 2939 and context["scope"]["whole_records_completed"] == 0
    assert context["complete_collection_aware_record_read"]
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"
    for value in (context, curation):
        assert all(value[k] == 0 for k in ("experimental_proteins_assigned", "exact_alleles_assigned",
                                          "experimental_genomes_assigned", "numerical_ast_added",
                                          "ncbi_endpoint_requests", "source_adoptions", "github_mutations"))
    assert curation["whole_corpus_primary_review"] == "OPEN"

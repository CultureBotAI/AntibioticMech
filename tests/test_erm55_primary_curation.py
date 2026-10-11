"""Corrected clinical associations must not become exact-allele causation."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.activity_memberships import FIELD, collection_bytes
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-09-erm55-primary"
STRAINS = {"18:60630", "18:62378", "19:64973", "20:67831", "MC6 22:74950",
           "20:69984", "21:70135", "21:70968", "21:71627", "21:73373"}


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


def test_ten_added_claims_preserve_record_and_membership_bindings(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:3732"
    assert record["chemical_structure"]["standard_inchi_key"] == curation["standard_inchi_key"]
    assert len(record["resistance_mechanisms"]) == curation["existing_claims_preserved"] + 10
    assert record["resistance_mechanisms"][-10:] == curation["added_claims"]
    prior_claims = semantic_sha(record["resistance_mechanisms"][:-10])
    assert prior_claims == curation["preserved_resistance_claims_sha256"]
    assert semantic_sha(record["curation_history"][:-1]) == curation["preserved_history_sha256"]
    assert record["curation_history"][-1] == curation["curation_event"]
    other = {k: v for k, v in record.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert record["curation_status"] == curation["curation_status"]
    artifacts = {ref["path"]: collection_bytes(ref, path) for ref in record[FIELD]}
    assert artifacts
    output = tmp_path / path.name
    write_validated_antibiotic(record, output, membership_artifacts=artifacts)
    assert output.read_bytes() == path.read_bytes()
    assert load_record(output) == record


@pytest.mark.parametrize("strain", sorted(STRAINS))
def test_each_isolate_keeps_family_association_not_exact_allele(curation, strain):
    claim, = [row for row in curation["added_claims"] if row["strain"] == strain]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["gene_families"] == ["erm(55)"]
    assert claim["taxon_id"] == "NCBITaxon:1774" and claim["taxon_label"] == "Mycobacteroides chelonae"
    assert claim["phenotype_label"] == "source-reported clarithromycin resistance"
    assert {row["reference"] for row in claim["evidence"]} == {"PMID:37347171", "PMID:38572983"}
    assert "co-occurrence, not proof of allele-specific causation" in claim["note"]
    assert "not all positive for the same subtype-specific assay" in claim["note"]
    assert not {"aro_id", "protein_accession", "gene_id", "alteration", "strain_taxon_id",
                "measurement_value", "phenotype_id"} & claim.keys()


def test_correction_controls_interpretation_without_claiming_pdf_review(context, curation):
    correction = context["correction"]
    assert correction["reference"] == "PMID:38572983"
    assert correction["relation_verified_in_both_directions"]
    assert "Table 2 genotype columns were misaligned" in correction["changes"]
    assert not correction["native_pdf_visually_inspected"]
    assert "stopped without retry or bypass" in correction["access_limit"]
    table = context["corrected_table_review"]
    assert set(table["source_resistant_isolate_labels"]) == STRAINS
    assert {row["strain"] for row in curation["added_claims"]} == STRAINS
    assert table["susceptible_comparator"] == "20:68529"
    assert table["susceptible_comparator"] not in STRAINS
    assert not table["intermediate_isolates_promoted"]
    assert not table["all_positive_for_one_subtype_specific_assay"]


def test_species_synonym_does_not_assign_strain_ids_or_uniprot(context):
    taxon = context["taxonomy"]
    assert taxon["taxonId"] == 1774 and taxon["rank"] == "species" and taxon["active"]
    assert "Mycobacterium chelonae" in taxon["synonyms"]
    assert context["new_reference_proteins_assigned"] == context["exact_alleles_assigned"] == 0
    assert all(row["result_count"] == 0 and not row["no_hit_is_absence"]
               for row in context["uniprot_query_context"].values())


def test_named_compound_join_has_valid_local_chemistry_and_stated_limit(context):
    chemical = context["chemical_identity"]
    assert chemical["identifier"] == "CHEBI:3732"
    assert chemical["standard_inchi_key"] == "AGOYDEPGAOXOCK-KCBOHYOISA-N"
    assert chemical["key_matches_smiles_and_inchi"] and chemical["unassigned_centers"] == 0
    assert not chemical["tested_preparation_independently_reidentified"]
    assert not chemical["source_fields_changed"]
    assert context["chemical_join_scope"] == (
        "NAMED_COMPOUND_JOIN_NOT_INDEPENDENT_TESTED_PREPARATION_IDENTIFICATION")


def test_current_census_changes_only_clarithromycin(curation):
    reconciliation = json.loads(Path(str(PREFIX) + "-checkpoint-reconciliation.json").read_bytes())
    ledgers = []
    for key in ("previous_ledger", "current_ledger"):
        pin = reconciliation[key]
        path = ROOT / pin["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
        with path.open(newline="") as stream:
            ledgers.append(list(csv.DictReader(stream, delimiter="\t")))
    old, new = ledgers
    assert len(old) == len(new) == 2939
    changed = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
    assert len(changed) == 1
    a, b = changed[0]
    assert b["identifier"] == "CHEBI:3732"
    assert {key for key in a if a[key] != b[key]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 10
    assert reconciliation["current_counts"]["resistance_assertions"] == 4814
    assert reconciliation["curator_claims"] == 59 and reconciliation["curator_records"] == 33
    assert curation["claims_added"] == 10 and curation["history_events_added"] == 1


def test_no_embedding_fingerprint_only_update(curation):
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"


def test_primary_scope_preserves_access_and_non_operational_limits(context, curation):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                  "coordinates", "mic", "measurement_value", "smiles", "standard_inchi"}
    assert not prohibited & set(keys(context))
    assert not prohibited & set(keys(curation))
    assert context["requests"]["erratum-pdf"]["status"] == 403
    assert context["requests"]["bibliography"]["status"] == 200
    assert not context["primary_study"]["whole_paper_review_complete"]
    assert context["scope"]["corpus_records"] == 2939
    assert context["scope"]["whole_records_completed"] == 0
    assert curation["whole_corpus_primary_review"] == "OPEN"
    for value in (context, curation):
        assert value["ncbi_endpoint_requests"] == value["source_adoptions"] == value["github_mutations"] == 0
        assert value["numerical_ast_added"] == value["experimental_genomes_assigned"] == 0

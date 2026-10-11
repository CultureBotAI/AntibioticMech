"""Clinical gene-type associations must not become exact-allele or causal claims."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-09-nimb-primary"
STRAINS = {"ARU 7420": "817", "ARU 9750": "817", "ARU 11562": "817",
           "ARU 12371": "818", "ARU 12963": "817"}
NAMES = {"817": "Bacteroides fragilis", "818": "Bacteroides thetaiotaomicron"}


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


def test_five_added_claims_preserve_all_prior_fields_and_history(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:6909"
    assert record["chemical_structure"]["standard_inchi_key"] == curation["standard_inchi_key"]
    assert len(record["resistance_mechanisms"]) == curation["existing_claims_preserved"] + 5 == 23
    assert record["resistance_mechanisms"][-5:] == curation["added_claims"]
    prior_claims = semantic_sha(record["resistance_mechanisms"][:-5])
    assert prior_claims == curation["preserved_resistance_claims_sha256"]
    assert semantic_sha(record["curation_history"][:-1]) == curation["preserved_history_sha256"]
    assert record["curation_history"][-1] == curation["curation_event"]
    other = {k: v for k, v in record.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert record["curation_status"] == curation["curation_status"] == "SEEDED"
    card, = [r for r in record["resistance_mechanisms"] if r.get("aro_id") == "ARO:3004655"]
    assert card["mechanism_type"] == "ANTIBIOTIC_INACTIVATION"
    assert card["evidence"][0]["reference"] == "ARO:3004655"
    output = tmp_path / path.name
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()
    assert load_record(output) == record


@pytest.mark.parametrize("strain", sorted(STRAINS))
def test_each_clinical_isolate_has_only_gene_type_association(curation, strain):
    claim, = [r for r in curation["added_claims"] if r["strain"] == strain]
    taxid = STRAINS[strain]
    assert claim["mechanism_type"] == "UNKNOWN" and claim["gene_families"] == ["nimB"]
    assert claim["taxon_id"] == "NCBITaxon:" + taxid and claim["taxon_label"] == NAMES[taxid]
    assert claim["phenotype_label"] == "source-reported reduced metronidazole susceptibility"
    assert claim["assay"] == "Source-reported gradient diffusion (Etest) phenotype"
    assert {r["reference"] for r in claim["evidence"]} == {"PMID:10970359"}
    assert "co-occurrence, not allele-specific causation" in claim["note"]
    assert "PCR-RFLP, not exact allele sequencing" in claim["note"]
    assert not {"aro_id", "protein_accession", "gene_id", "alteration", "strain_taxon_id",
                "measurement_value", "phenotype_id", "source"} & claim.keys()


def test_controls_nime_and_negative_assays_are_not_promoted(context, curation):
    table = context["table_review"]
    assert table["clinical_isolate_taxa"] == STRAINS
    selected = {r["strain"] for r in curation["added_claims"]}
    assert selected == set(STRAINS)
    assert table["separate_positive_control"] == "Bf-8"
    assert "Bf-8" not in selected and not table["control_promoted_to_clinical_isolate"]
    assert set(table["nimE_isolates_excluded"]) == {
        "ARU 3690", "ARU 6881", "ARU 10769", "ARU 11563", "ARU 11564"}
    assert set(table["assay_negative_clinical_comparators"]) == {"ARU 2592", "ARU 5589", "ARU 12605"}
    assert not selected & set(table["nimE_isolates_excluded"] + table["assay_negative_clinical_comparators"])
    assert not table["negative_gene_assay_is_gene_absence"]


@pytest.mark.parametrize("taxid", sorted(NAMES))
def test_species_identity_is_not_a_strain_identifier(context, taxid):
    row = context["taxonomy"][taxid]
    assert row["taxonId"] == int(taxid) and row["scientificName"] == NAMES[taxid]
    assert row["active"] and row["rank"] == "species"


def test_uniprot_reference_is_not_an_experimental_clinical_protein(context, curation):
    ref = context["reference_protein"]
    assert ref["accession"] == "UniProtKB:Q45146"
    assert ref["reference_taxon_id"] == "NCBITaxon:817"
    assert ref["entry_version"] == 68 and ref["sequence_version"] == 1
    assert ref["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert not ref["exact_allele_assignment"] and not ref["experimental_subject_assignment"]
    assert context["reference_candidate_basis"][0]["source_citation_ids"] == ["PMID:8067736"]
    assert context["reference_release"] == "2026_03"
    assert context["experimental_proteins_assigned"] == 0
    assert all("protein_accession" not in r for r in curation["added_claims"])


def test_named_compound_join_preserves_identity_and_preparation_limit(context):
    chemical = context["chemical_identity"]
    assert chemical["identifier"] == "CHEBI:6909"
    assert chemical["standard_inchi_key"] == "VAOCPAMSLUNLGC-UHFFFAOYSA-N"
    assert chemical["key_matches_smiles_and_inchi"]
    assert not chemical["source_fields_changed"]
    assert not chemical["tested_preparation_independently_reidentified"]
    assert context["chemical_join_scope"] == (
        "NAMED_COMPOUND_JOIN_NOT_INDEPENDENT_TESTED_PREPARATION_IDENTIFICATION")


def test_new_census_changes_only_metronidazole(curation):
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
    assert b["identifier"] == "CHEBI:6909"
    assert {key for key in a if a[key] != b[key]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 5
    assert reconciliation["current_counts"]["resistance_assertions"] == 4819
    assert reconciliation["curator_claims"] == 64 and reconciliation["curator_records"] == 34
    assert curation["claims_added"] == 5 and curation["history_events_added"] == 1


def test_embedding_inputs_do_not_need_fingerprint_only_update(curation):
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"


def test_non_operational_export_and_unfinished_review_are_explicit(context, curation):
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
    for value in (context, curation):
        assert not prohibited & set(keys(value))
        assert value["ncbi_endpoint_requests"] == value["source_adoptions"] == value["github_mutations"] == 0
        assert value["numerical_ast_added"] == value["experimental_genomes_assigned"] == 0
        assert value["exact_alleles_assigned"] == 0
    assert context["requests"]["bibliography"]["status"] == 200
    assert not context["primary_study"]["whole_paper_review_complete"]
    assert not context["primary_study"]["native_pdf_visually_inspected"]
    assert context["scope"]["corpus_records"] == 2939 and context["scope"]["whole_records_completed"] == 0
    assert curation["whole_corpus_primary_review"] == "OPEN"

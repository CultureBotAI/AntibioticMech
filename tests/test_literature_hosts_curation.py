"""Native observations, reference proteins and later archive datasets stay distinct."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.activity_memberships import FIELD, collection_bytes
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-09-literature-hosts"


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_one_added_claim_preserves_source_slices_and_memberships(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:2955"
    assert len(record["resistance_mechanisms"]) == curation["existing_claims_preserved"] + 1 == 55
    assert record["resistance_mechanisms"][-1:] == curation["added_claims"]
    prior_claims = semantic_sha(record["resistance_mechanisms"][:-1])
    assert prior_claims == curation["preserved_resistance_claims_sha256"]
    assert semantic_sha(record["curation_history"][:-1]) == curation["preserved_history_sha256"]
    assert record["curation_history"][-1] == curation["curation_event"]
    other = {k: v for k, v in record.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert record["curation_status"] == curation["curation_status"] == "SEEDED"
    artifacts = {r["path"]: collection_bytes(r, path) for r in record[FIELD]}
    assert len(artifacts) == 1 and len(record["activity_spectrum"]) == 2
    output = tmp_path / path.name
    write_validated_antibiotic(record, output, membership_artifacts=artifacts)
    assert output.read_bytes() == path.read_bytes() and load_record(output) == record


def test_native_joint_association_is_not_individual_gene_causation(context, curation):
    claim, = curation["added_claims"]
    assert claim["gene_families"] == ["mef(F)", "msr(G)"]
    assert claim["mechanism_type"] == "UNKNOWN" and claim["strain"] == "Epi0082"
    assert claim["taxon_id"] == "NCBITaxon:1855823"
    assert claim["taxon_label"] == "Macrococcoides canis"
    assert claim["phenotype_label"] == "source-reported reduced azithromycin susceptibility"
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:33118027"}
    assert "co-occurrence, not individual-gene or allele-specific causation" in claim["note"]
    assert not {"aro_id", "source", "protein_accession", "gene_id", "alteration",
                "strain_taxon_id", "measurement_value", "phenotype_id"} & claim.keys()
    study = context["primary_reviews"]["33118027"]
    assert study["native_isolate"] == "Epi0082" and study["comparator"] == "KM45013"
    assert study["assay_host"] == "Staphylococcus aureus RN4220"
    ref = context["reference_proteins"]["A0A7S4U594"]
    assert ref["taxon_id"] == study["reference_taxon_id"] == "NCBITaxon:69966"
    assert ref["taxon_id"] != claim["taxon_id"]
    assert not study["exact_erythromycin_a_preparation_established"]
    assert "Tylosin" in study["negative_scope"]


@pytest.mark.parametrize("taxid,name", [("1855823", "Macrococcus canis"),
                                      ("69966", "Macrococcus caseolyticus")])
def test_old_taxon_names_are_other_names_not_invented_synonyms(context, taxid, name):
    row = context["taxonomy"][taxid]
    assert row["active"] and row["rank"] == "species"
    assert row["source_name"] == name and row["matched_name_field"] == "otherNames"


@pytest.mark.parametrize("accession", [f"CP04636{i}" for i in range(3, 8)])
def test_native_components_are_not_assembly_or_gene_assignments(context, accession):
    row = context["archive_metadata"][accession]
    assert row["exact_accession_returned"] and row["returned_accession"] == accession
    assert row["returned_version"] == 1 and row["data_type"] == "SEQUENCE"
    assert row["sample"] == "SAMN13342681" and row["project"] == "PRJNA590936"
    assert row["taxon_id"] == "NCBITaxon:1855823"
    assert row["citations"] == ["PMID:33118027"] and "strain Epi0082" in row["description"]
    assert not row["assembly_assignment"]


def test_qnrb27_separate_reference_strains_are_preserved(context):
    links = context["reference_proteins"]["E1A0W6"]["archive_links"]
    expected = {"ADM52186.1": {"S08-IJ52"}, "ADM52187.1": {"S08-KM17"}, "AEL00448.1": {"W48459"}}
    assert {r["archive_protein_id"]: {x["strain"] for x in r["strain_reference_bindings"]}
            for r in links} == expected
    for row in links:
        evidence_ids = {r["evidence_protein_id"] for r in row["strain_reference_bindings"]}
        assert evidence_ids == {row["archive_protein_id"]}
        assert not row["exact_experimental_allele_assignment"]


def test_qnrb38_unbound_comment_does_not_become_exact_protein_strain(context):
    links = {r["archive_protein_id"]: r for r in context["reference_proteins"]["G1FE80"]["archive_links"]}
    assert {r["strain"] for r in links["AEL00461.1"]["strain_reference_bindings"]} == {"S50552"}
    assert {r["strain"] for r in links["KPR55176.1"]["strain_reference_bindings"]} == {"ST62:944112508"}
    assert {r["strain"] for r in links["HAT3897757.1"]["strain_reference_bindings"]} == {"O50"}
    assert links["HAT3901231.1"]["strain_reference_bindings"] == []
    assert links["HAT3901231.1"]["unbound_strain_comments_not_propagated"]


@pytest.mark.parametrize("accession,parent,sample", [
    ("LJEB01000051", "LJEB01000000", "SAMN04011435"),
    ("DACSXJ010000011", "DACSXJ010000000", "SAMN14640087"),
    ("DACSXJ010000163", "DACSXJ010000000", "SAMN14640087")])
def test_parent_contigsets_do_not_acquire_exact_contig_version(context, accession, parent, sample):
    row = context["archive_metadata"][accession]
    assert row["requested_accession"] == accession and row["returned_accession"] == parent
    assert not row["exact_accession_returned"] and row["data_type"] == "CONTIGSET"
    assert row["scope"] == "PARENT_CONTIGSET_NOT_QUERIED_CONTIG" and row["sample"] == sample
    assert not row["assembly_assignment"]


def test_source_duplicate_accession_and_independent_versions_remain_visible(context):
    study = context["primary_reviews"]["21844311"]
    assert study["source_printed_accession_conflict"] == {"qnrB37": "JN173059", "qnrB38": "JN173059"}
    assert study["archive_supported_qnrB38_accession"] == "JN173060.2"
    assert not study["source_silently_corrected"] and not study["figure_redistributed"]
    assert "qnrB37" in context["archive_metadata"]["JN173059"]["description"]
    assert "M11175" in context["archive_metadata"]["JN173059"]["description"]
    assert context["reference_proteins"]["G1FE80"]["sequence_version"] == 1
    assert context["archive_metadata"]["JN173060"]["returned_version"] == 2
    assert context["reference_proteins"]["G1FE71"]["sequence_version"] == 2
    assert context["archive_metadata"]["JN173056"]["returned_version"] == 1


def test_primary_access_and_no_hit_limits_are_honest(context):
    assert context["primary_reviews"]["21830908"]["inspection"] == "EBI_ABSTRACT_AND_BIBLIOGRAPHY_ONLY"
    search = context["native_archive_uniprot_search"]
    assert search["hits"] == 0 and not search["gene_absence_inferred"]
    assert not context["primary_reviews"]["16870791"]["named_qnrB3_experimental_strain_resolved"]
    assert context["reference_release"] == "2026_03"
    assert all(r["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
               for r in context["reference_proteins"].values())


def test_census_changes_only_azithromycin(curation):
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
    assert b["identifier"] == "CHEBI:2955"
    assert {key for key in a if a[key] != b[key]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 1
    assert reconciliation["current_counts"]["resistance_assertions"] == 4820
    assert reconciliation["curator_claims"] == 65 and reconciliation["curator_records"] == 35
    assert curation["claims_added"] == curation["history_events_added"] == 1


def test_chemical_identity_and_embedding_preservation(context, curation):
    row = context["chemical_identity"]
    assert row["identifier"] == "CHEBI:2955"
    assert row["standard_inchi_key"] == "MQTOSJVFKKJCRP-BICOPXKESA-N"
    assert row["key_matches_smiles_and_inchi"] and not row["source_fields_changed"]
    assert not row["tested_preparation_independently_reidentified"]
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"


def test_exports_remain_non_operational_and_review_open(context, curation):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                 "coordinates", "mic", "measurement_value", "smiles", "standard_inchi"}
    for value in (context, curation):
        assert not forbidden & set(keys(value))
        assert value["ncbi_endpoint_requests"] == value["source_adoptions"] == value["github_mutations"] == 0
        assert value["numerical_ast_added"] == value["assembly_accessions_assigned"] == 0
        assert value["exact_alleles_assigned"] == value["experimental_proteins_assigned"] == 0
    assert context["scope"]["corpus_records"] == 2939 and context["scope"]["whole_records_completed"] == 0
    assert curation["whole_corpus_primary_review"] == "OPEN"

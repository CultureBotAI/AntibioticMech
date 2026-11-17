"""Keep laboratory associations distinct from reference identity and clinical AST."""

import copy
import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-sulfathiazole"


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


@pytest.fixture(scope="module")
def context():
    return read("-context.json")


@pytest.fixture(scope="module")
def receipt():
    return read("-curation.json")


def assert_pin(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    # Preserve the original YAML ordering when replaying a sorted JSON receipt.
    assert set(value) == set(keys)
    return {key: copy.deepcopy(value[key]) for key in keys}


def test_dated_transition_reproduces_only_claims_and_history(context, receipt, tmp_path):
    payload = assert_pin(receipt["fixture"])
    assert hashlib.sha256(payload).hexdigest() == receipt["before"]["sha256"]
    assert receipt["before"] == context["record_before"]
    assert receipt["record"]["path"] == receipt["before"]["path"]
    record = load_record(ROOT / receipt["fixture"]["path"])
    before = copy.deepcopy(record)
    assert record["identifier"] == "CHEBI:9337"
    assert record["chemical_structure"]["standard_inchi_key"] == "JNMRHUJNCSQMMB-UHFFFAOYSA-N"
    assert not record.get("resistance_mechanisms")
    record["resistance_mechanisms"] = [ordered(claim, (
        "mechanism_type", "label", "gene_families", "taxon_id", "taxon_label",
        "phenotype_label", "assay", "note", "evidence",
    )) for claim in receipt["claims"]]
    for claim in record["resistance_mechanisms"]:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    record["curation_history"].append(ordered(receipt["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted",
    )))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(record, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == receipt["record"]["sha256"]
    ignored = {"resistance_mechanisms", "curation_history"}
    assert {k: v for k, v in before.items() if k not in ignored} == {
        k: v for k, v in record.items() if k not in ignored}
    assert record["curation_history"][:-1] == before["curation_history"]
    assert build_document(record, role_names()) != build_document(before, role_names())
    assert receipt["history_events_added"] == receipt["records_changed"] == 1
    assert receipt["new_resistance_claims"] == len(record["resistance_mechanisms"]) == 2


def test_historical_replay_does_not_freeze_live_record(context, receipt, tmp_path, monkeypatch):
    original = Path.open

    def no_live_record(path, *args, **kwargs):
        assert path != ROOT / receipt["record"]["path"]
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", no_live_record)
    test_dated_transition_reproduces_only_claims_and_history(context, receipt, tmp_path)


@pytest.mark.parametrize("field", ["claim", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(context, receipt, tmp_path, field):
    candidate = copy.deepcopy(receipt)
    if field == "claim":
        candidate["claims"][1]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif field == "event":
        candidate["curation_event"]["changes"] += " Unsupported change."
    else:
        candidate["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        test_dated_transition_reproduces_only_claims_and_history(context, candidate, tmp_path)


def test_gene_association_boundaries(receipt):
    folp, bcr = receipt["claims"]
    assert folp["gene_families"] == ["folP"] and bcr["gene_families"] == ["bcr"]
    assert folp["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
    assert "background dependence" in folp["note"] and "alone did not explain" in folp["note"]
    assert bcr["mechanism_type"] == "UNKNOWN"
    assert "direct efflux was not demonstrated" in bcr["note"]
    assert "sux is not assigned to the bcr synonym suxA" in bcr["note"]
    assert "Historical sequence differences remain unresolved" in bcr["note"]
    for claim, accession in zip(receipt["claims"], ("P0AC13", "P28246"), strict=True):
        assert claim["taxon_id"] == "NCBITaxon:562" and claim["taxon_label"] == "Escherichia coli"
        assert claim["phenotype_label"] == "Source-reported relative sulfathiazole resistance"
        assert claim["evidence"][0]["reference"] == "PMID:9449266"
        ref = claim["evidence"][1]
        assert ref["reference"] == "UniProtKB:" + accession
        assert "Reference identity only" in ref["notes"]
        assert "not an experimental strain assignment" in ref["notes"]
        assert "reference-only" in claim["note"]


def assert_no_experimental_payload(claims):
    forbidden = {"alteration", "protein_accession", "strain", "strain_taxon_id", "gene_id",
                 "assembly_accession", "biosample_accession", "bioproject_accession",
                 "sra_accessions", "sequence", "variant", "mic", "mic_value", "phenotype"}
    assert all(not forbidden.intersection(claim) for claim in claims)


def test_no_experimental_or_clinical_assignments(receipt, context):
    assert_no_experimental_payload(receipt["claims"])
    assert receipt["numerical_ast_added"] == receipt["experimental_proteins_or_genomes_assigned"] == 0
    assert not receipt["whole_record_review_complete"]
    assert context["endpoint_policy"]["enzyme_activity_is_mic"] is False
    assert not context["endpoint_policy"]["clinical_category_inferred"]
    assert context["subject_scope"]["labels_are_not_a_single_tested_subject"]
    assert not any(context["subject_scope"][k] for k in (
        "experimental_strain_taxon_assigned", "experimental_allele_assigned",
        "experimental_protein_assigned", "genome_or_sample_assigned",
    ))


@pytest.mark.parametrize("field", ["protein_accession", "strain_taxon_id", "assembly_accession",
                                  "biosample_accession", "alteration", "mic", "phenotype"])
def test_unsupported_experimental_fields_are_rejected(receipt, field):
    claims = copy.deepcopy(receipt["claims"])
    claims[0][field] = "unsupported"
    with pytest.raises(AssertionError):
        assert_no_experimental_payload(claims)


def test_reference_and_taxonomy_context_reuses_pinned_predecessor(context):
    parent = json.loads(assert_pin(context["reference_predecessor"]))
    assert context["reference_proteins"] == {
        g: parent["reference_proteins"][g] for g in ("folP", "bcr")}
    assert context["taxonomy"] == parent["taxonomy"]
    for gene, accession, entry, sequence in (("folP", "P0AC13", 147, 1), ("bcr", "P28246", 179, 4)):
        row = context["reference_proteins"][gene]
        assert row["protein_accession"] == "UniProtKB:" + accession
        assert (row["entry_version"], row["sequence_version"]) == (entry, sequence)
        assert row["reference_taxon_id"] == "NCBITaxon:83333" and row["reviewed"]
        assert not row["experimental_resistance_assignment"]
    assert context["primary"]["native_figure_1"] == parent["primary_context"]["figure_1"]


def test_census_adds_only_two_claims_on_one_record(context, receipt):
    reconciliation = read("-reconciliation.json")
    censuses = []
    for key in ("previous_census", "current_census"):
        payload = assert_pin(reconciliation[key])
        rows = list(csv.DictReader(payload.decode().splitlines(), delimiter="\t"))
        mapping = {r["identifier"]: r for r in rows}
        assert len(mapping) == len(rows) == 2939
        censuses.append(mapping)
    before, after = censuses
    assert set(before) == set(after)
    assert [i for i in before if before[i] != after[i]] == ["CHEBI:9337"]
    assert before["CHEBI:9337"]["resistance_assertions"] == "0"
    assert after["CHEBI:9337"] == {
        **before["CHEBI:9337"], "record_sha256": receipt["record"]["sha256"],
        "resistance_assertions": "2", "research_status": "PENDING_PRIMARY_REVIEW",
    }
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4853
    assert sum(int(r["resistance_assertions"]) > 0 for r in after.values()) == 311
    assert reconciliation["curator_claims"] == 98 and reconciliation["curator_records"] == 43
    assert reconciliation["records_byte_identical"] == 2938
    assert reconciliation["previous_bcr_curation_preserved"]
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert context["disposition"]["whole_corpus_status"] == "OPEN"


def test_primary_scope_and_ncbi_deferral_remain_explicit(context):
    assert context["primary"]["reference"] == "PMID:9449266"
    assert not context["primary"]["whole_paper_review_complete"]
    assert not context["earlier_citation"]["used_as_independent_replication"]
    assert context["earlier_citation"]["review_scope"] == "PUBLISHER_ABSTRACT_ONLY"
    assert not context["identity"]["tested_preparation_independently_reidentified"]
    limits = context["limits"]
    assert limits["issue_1040"] == "DEFERRED"
    assert not any(v for k, v in limits.items() if k != "issue_1040")

"""Species grounding must preserve source claim scope and the remaining evidence gaps."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_antiviral_taxa as audit  # noqa: E402

FIXTURE = ROOT / "tests/fixtures/bictegravir-before-2026-10-14.yaml"


def test_species_update_preserves_existing_claim_fields_and_adds_no_allele():
    before = load_record(FIXTURE)
    original = copy.deepcopy(before)
    claims = audit.grounded_claims(before["identifier"], before["resistance_mechanisms"])
    assert before == original and len(claims) == 1
    old, new = before["resistance_mechanisms"][0], claims[0]
    assert {k: v for k, v in new.items() if k not in {"note", "evidence", "taxon_id", "taxon_label"}} == {
        k: v for k, v in old.items() if k not in {"note", "evidence"}}
    assert new["taxon_id"] == "NCBITaxon:3418650" and new["taxon_label"] == "Lentivirus humimdef1"
    assert new["note"].startswith(old["note"])
    assert new["evidence"][:-1] == old["evidence"]
    assert new["evidence"][-1]["reference"] == "https://rest.uniprot.org/taxonomy/3418650"
    assert not {"strain", "strain_taxon_id", "protein_accession", "gene_id", "alteration"}.intersection(new)


@pytest.mark.parametrize("change", ["identifier", "extra_claim", "label", "note", "evidence", "taxon"])
def test_unexpected_claim_changes_require_reassessment(change):
    doc = load_record(FIXTURE)
    if change == "identifier":
        doc["identifier"] = "CHEBI:1"
    elif change == "extra_claim":
        doc["resistance_mechanisms"] *= 2
    elif change in {"label", "note"}:
        doc["resistance_mechanisms"][0][change] += " changed"
    elif change == "evidence":
        doc["resistance_mechanisms"][0]["evidence"] = []
    else:
        doc["resistance_mechanisms"][0]["taxon_id"] = "NCBITaxon:11676"
    with pytest.raises(ValueError):
        audit.grounded_claims(doc["identifier"], doc["resistance_mechanisms"])


def test_validated_roundtrip_preserves_other_record_fields(tmp_path):
    before = load_record(FIXTURE)
    expected = copy.deepcopy(before)
    expected["resistance_mechanisms"] = audit.grounded_claims(
        before["identifier"], before["resistance_mechanisms"])
    target = tmp_path / "bictegravir.yaml"
    write_validated_antibiotic(expected, target)
    assert load_record(target) == expected
    first = target.read_bytes()
    write_validated_antibiotic(load_record(target), target)
    assert target.read_bytes() == first
    assert expected["genotype_resistance_score_rules"] == before["genotype_resistance_score_rules"]


def test_uninspected_primary_rejected():
    with pytest.raises(ValueError, match="payload"):
        audit.primary_context(b"HIV-1")


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_complete_historical_gap_selection_and_non_equivalent_dispositions(dossier):
    rows = dossier["taxon_gap_dispositions"]
    assert len(rows) == 11 and len({r["record_identifier"] for r in rows}) == 9
    assert len({(r["record_identifier"], r["resistance_index"]) for r in rows}) == 11
    assert sum(r["status"] == "SPECIES_ONLY_CURATION_SUPPORTED" for r in rows) == 1
    assert sum(r["status"] == "BIOCHEMICAL_SCOPE_NOT_AUTOMATIC_ORGANISM_ASSIGNMENT" for r in rows) == 4
    assert dossier["sources"]["sg85_technical_failure"]["status"] == 500
    assert not dossier["limits"]["dolutegravir_full_text_request_attempted"]
    assert not dossier["limits"]["sg85_error_establishes_permission_or_global_unavailability"]


def test_public_grounding_is_not_an_experimental_allele_or_whole_record_signoff(dossier):
    primary = dossier["primary"]
    assert primary["source_organism_label"] == "HIV-1"
    assert primary["existing_claim_context"] == "LABORATORY_NOT_PATIENT_ASSIGNMENT"
    assert not primary["selected_populations_and_site_directed_test_viruses_are_interchangeable"]
    assert not primary["all_inherited_variant_or_quantitative_claims_revalidated"]
    assert not primary["native_figures_or_supplements_reviewed"]
    assert not primary["exact_compound_form_newly_resolved"]
    assert not primary["new_sequences_variants_constructs_protocols_or_numeric_AST_exported"]
    assert dossier["taxonomy"]["source_context_rank"] == "no rank"
    assert dossier["taxonomy"]["species_rank"] == "species"
    for field in ("experimental_allele_assignment", "experimental_genome_assignment",
                  "experimental_strain_taxon_assignment", "protein_accession_assignment"):
        assert dossier["taxonomy"][field] is None
    assert dossier["limits"]["ncbi_requests"] == 0 and dossier["limits"]["issue_1040"] == "DEFERRED"
    assert dossier["limits"]["full_corpus_goal_status"] == "OPEN"


def test_live_claim_and_history_match_saved_curation_when_applied():
    receipt_path = ROOT / "research/2026-10-14-antiviral-taxa-curation.json"
    if not receipt_path.exists():
        return
    receipt = json.loads(receipt_path.read_bytes())
    before, after = load_record(FIXTURE), load_record(ROOT / receipt["after"]["path"])
    assert after["resistance_mechanisms"] == audit.grounded_claims(
        before["identifier"], before["resistance_mechanisms"])
    assert after["curation_history"] == [*before["curation_history"], receipt["curation_event"]]
    for field in before.keys() - {"resistance_mechanisms", "curation_history"}:
        assert after[field] == before[field]


def test_offline_native_replay(dossier, monkeypatch, pre_card_qualification_root):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline taxon audit attempted a network request")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(pre_card_qualification_root) == dossier

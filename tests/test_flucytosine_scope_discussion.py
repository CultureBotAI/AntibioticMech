"""Keep a qualified scope warning distinct from source correction or phenotype."""

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import resistance_checkpoint_records as checkpoint  # noqa: E402
from embed_records import build_document, role_names  # noqa: E402
from seed_from_sources import is_card_sourced, merge_with_existing  # noqa: E402

CONTEXT = ROOT / "research/2026-10-13-flucytosine-scope-context.json"


def test_discussion_preserves_all_claims_and_embedding_document(tmp_path):
    context = json.loads(CONTEXT.read_bytes())
    before = load_record(checkpoint.reference.check_pin(ROOT, context["fixture"]))
    after = copy.deepcopy(before)
    after["discussions"] = [context["discussion"]]
    record_curation_event(
        after,
        curator="test",
        action="CURATED_EVIDENCE_SCOPE_DISCUSSION",
        llm_assisted=True,
        timestamp="2026-10-13T00:00:00Z",
    )
    path = tmp_path / "flucytosine.yaml"
    write_validated_antibiotic(after, path)
    assert load_record(path) == after
    first = path.read_bytes()
    write_validated_antibiotic(after, path)
    assert path.read_bytes() == first
    fresh = copy.deepcopy(before)
    fresh["resistance_mechanisms"] = [c for c in before["resistance_mechanisms"] if is_card_sourced(c)]
    assert len(fresh["resistance_mechanisms"]) == 8
    assert merge_with_existing(fresh, after) == after
    assert len(after["resistance_mechanisms"]) == 10
    assert sum("aro_id" in c for c in after["resistance_mechanisms"]) == 8
    assert after["curation_history"][:-1] == before["curation_history"]
    assert {k: v for k, v in after.items() if k not in ("discussions", "curation_history")} == {
        k: v for k, v in before.items() if k not in ("discussions", "curation_history")
    }
    assert build_document(before, role_names()) == build_document(after, role_names())


def test_saved_scope_does_not_correct_card_or_assign_h99_phenotype():
    context = json.loads(CONTEXT.read_bytes())
    discussion = context["discussion"]
    assert discussion["kind"] == "CURATION_TODO" and discussion["status"] == "OPEN"
    assert discussion["attaches_to"] == ["resistance_mechanisms#ARO:3009633"]
    assert "potential source species-scope conflict, not a proven correction" in discussion["rationale"]
    assert "does not establish an H99 resistance phenotype" in discussion["rationale"]
    assert "WM276-derived strains" in discussion["evidence"][0]["explanation"]
    assert "were not visually reviewed" in discussion["evidence"][0]["notes"]
    assert not context["fungamr_source_row_crosswalk_verified"]
    assert not context["card_species_error_proven"]
    assert context["new_resistance_assertions"] == context["new_experimental_allele_assignments"] == 0
    assert context["whole_record_reviews_completed"] == 0
    assert context["full_corpus_goal_status"] == "OPEN"
    assert not context["constraints"]["sequences_variants_protocols_exported"]
    assert not context["constraints"]["numeric_ast_exported"]
    assert context["constraints"]["ncbi_requests"] == 0
    refs = context["reference_grounding"]
    assert refs["wm276"]["species_taxon_id"] == "NCBITaxon:37769"
    assert not refs["wm276"]["species_matches_card_term"]
    assert refs["h99-candidate"]["species_taxon_id"] == "NCBITaxon:5207"
    assert not refs["h99-candidate"]["primary_native_gene_alias_verified"]
    assert all(r["experimental_allele_assignment"] is None for r in refs.values())
    assert all(r["experimental_genome_assignment"] is None for r in refs.values())


def test_saved_curation_transition_reproduces_exact_after_bytes(tmp_path):
    receipt = json.loads((ROOT / "research/2026-10-13-flucytosine-scope-curation.json").read_bytes())
    before = load_record(checkpoint.reference.check_pin(ROOT, receipt["fixture"]))
    # Sorted receipt JSON loses insertion order; restore the recorded YAML emission order.
    order = ("discussion_id", "kind", "status", "prompt", "attaches_to", "rationale",
             "evidence", "notes", "posed_by", "posed_date")
    assert set(order) == set(receipt["discussion"])
    discussion = {key: receipt["discussion"][key] for key in order}
    evidence_order = ("reference", "evidence_source", "explanation", "notes")
    assert all(set(item) <= set(evidence_order) for item in discussion["evidence"])
    discussion["evidence"] = [{key: item[key] for key in evidence_order if key in item}
                              for item in discussion["evidence"]]
    before["discussions"] = [discussion]
    event = receipt["event"]
    record_curation_event(before, curator=event["curator"], action=event["action"],
                          changes=event["changes"], timestamp=event["timestamp"],
                          llm_assisted=event["llm_assisted"])
    target = tmp_path / "flucytosine.yaml"
    write_validated_antibiotic(before, target)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == receipt["after"]["sha256"]


@pytest.mark.parametrize("hash_key", ["sha256", "record_sha256"])
@pytest.mark.parametrize("change", ["none", "path", "identifier", "fixture", "hash", "missing", "conflict"])
def test_historical_fixture_requires_exact_registration(tmp_path, change, hash_key):
    item = {
        "identifier": "CHEBI:5100",
        "path": checkpoint.FLUCYTOSINE_PATH,
        hash_key: checkpoint.FLUCYTOSINE_SHA256,
    }
    fixture = tmp_path / checkpoint.FLUCYTOSINE_FIXTURE
    fixture.parent.mkdir(parents=True)
    if change != "missing":
        fixture.write_bytes((ROOT / checkpoint.FLUCYTOSINE_FIXTURE).read_bytes())
    live = tmp_path / checkpoint.FLUCYTOSINE_PATH
    live.parent.mkdir(parents=True)
    live.write_text("Later curation must not replace this historical input.\n")
    if change == "path":
        item["path"] = "data/antibiotics/antifungal/other.yaml"
    elif change == "identifier":
        item["identifier"] = "CHEBI:3764"
    elif change == "fixture":
        fixture.write_text("wrong historical snapshot\n")
    elif change == "hash":
        item[hash_key] = "0" * 64
    elif change == "conflict":
        item["record_sha256" if hash_key == "sha256" else "sha256"] = "0" * 64
    if change != "none":
        with pytest.raises((ValueError, FileNotFoundError)):
            checkpoint.checkpoint_path(tmp_path, item)
        return
    assert checkpoint.checkpoint_path(tmp_path, item) == fixture
    assert load_record(fixture)["identifier"] == item["identifier"]


@pytest.mark.parametrize(
    "identifier,path",
    [
        ("CHEBI:5100", checkpoint.FLUCYTOSINE_PATH),
        ("CHEBI:3764", "data/antibiotics/antifungal/clotrimazole.yaml"),
    ],
)
def test_unregistered_hash_checks_live_record_without_fixture_fallback(tmp_path, identifier, path):
    live = tmp_path / path
    live.parent.mkdir(parents=True)
    live.write_text("New checkpoint bytes\n")
    item = {"identifier": identifier, "path": path, "sha256": hashlib.sha256(live.read_bytes()).hexdigest()}
    assert checkpoint.checkpoint_path(tmp_path, item) == live
    live.write_text("drift\n")
    with pytest.raises(ValueError):
        checkpoint.checkpoint_path(tmp_path, item)
    live.unlink()
    with pytest.raises(FileNotFoundError):
        checkpoint.checkpoint_path(tmp_path, item)


def test_missing_checksum_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        checkpoint.checkpoint_path(
            tmp_path, {"path": checkpoint.FLUCYTOSINE_PATH, "identifier": "CHEBI:5100"}
        )

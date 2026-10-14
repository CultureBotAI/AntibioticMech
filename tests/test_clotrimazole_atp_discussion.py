"""A scope discussion must preserve source assertions and historical replay."""

import copy
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_yeast_atp_context as audit  # noqa: E402
from embed_records import build_document, role_names  # noqa: E402
from seed_from_sources import merge_with_existing  # noqa: E402

CONTEXT = ROOT / "research/2026-10-13-yeast-atp-supplement-context.json"


def test_discussion_preserves_claims_and_embedding_document(tmp_path):
    context = json.loads(CONTEXT.read_bytes())
    before = load_record(audit.reference.check_pin(ROOT, context["fixture"]))
    after = copy.deepcopy(before)
    after["discussions"] = [context["discussion"]]
    record_curation_event(after, curator="test", action="CURATED_EVIDENCE_SCOPE_DISCUSSION",
                          llm_assisted=True, timestamp="2026-10-13T00:00:00Z")
    path = tmp_path / "clotrimazole.yaml"
    write_validated_antibiotic(after, path)
    assert load_record(path) == after
    first = path.read_bytes()
    write_validated_antibiotic(after, path)
    assert path.read_bytes() == first
    assert merge_with_existing(before, after) == after
    assert len(after["resistance_mechanisms"]) == 4
    assert after["resistance_mechanisms"] == before["resistance_mechanisms"]
    assert after["curation_status"] == before["curation_status"]
    assert after.get("activity_spectrum") == before.get("activity_spectrum")
    assert build_document(before, role_names()) == build_document(after, role_names())


def test_saved_scope_separates_reference_and_experimental_evidence():
    context = json.loads(CONTEXT.read_bytes())
    discussion = context["discussion"]
    assert discussion["kind"] == "CURATION_TODO" and discussion["status"] == "OPEN"
    assert discussion["attaches_to"] == ["resistance_mechanisms#ARO:3009347",
                                         "resistance_mechanisms#ARO:3009350"]
    assert "grew more slowly" in discussion["rationale"]
    assert "every ATP2 allele" in discussion["rationale"]
    assert "not MIC or clinical" in discussion["evidence"][0]["explanation"]
    assert "Table S4" in discussion["evidence"][0]["explanation"]
    assert not context["fungamr_source_row_crosswalk_verified"]
    assert context["new_resistance_assertions"] == context["new_experimental_allele_assignments"] == 0
    assert context["whole_record_reviews_completed"] == 0
    assert context["full_corpus_goal_status"] == "OPEN"
    assert not context["primary"]["workbook_rendered"]
    assert not context["primary"]["growth_curves_refitted"]
    assert not context["primary"]["source_gene_rows_are_independent_mutation_event_counts"]
    assert not context["constraints"]["sequences_variants_protocols_exported"]
    assert not context["constraints"]["numeric_ast_exported"]
    assert context["constraints"]["ncbi_requests"] == 0


@pytest.mark.parametrize("change", ["none", "path", "fixture", "hash", "missing"])
def test_checkpoint_uses_pinned_history_not_curated_live_record(tmp_path, change):
    context = json.loads(CONTEXT.read_bytes())
    source = context["record_before"]
    item = {"identifier": "CHEBI:3764", "path": source["path"], "record_sha256": source["sha256"]}
    fixture = tmp_path / audit.CLOTRIMAZOLE_FIXTURE
    fixture.parent.mkdir(parents=True)
    if change != "missing":
        fixture.write_bytes((ROOT / audit.CLOTRIMAZOLE_FIXTURE).read_bytes())
    live = tmp_path / audit.CLOTRIMAZOLE_PATH
    live.parent.mkdir(parents=True)
    live.write_text("Later live curation must not replace this historical input.\n")
    if change == "path":
        item["path"] = "data/antibiotics/antifungal/other.yaml"
    elif change == "fixture":
        fixture.write_text("wrong historical snapshot\n")
    elif change == "hash":
        item["record_sha256"] = "0" * 64
    if change != "none":
        with pytest.raises((ValueError, FileNotFoundError)):
            audit.checkpoint_path(tmp_path, item)
        return
    assert audit.checkpoint_path(tmp_path, item) == fixture
    assert load_record(fixture)["identifier"] == item["identifier"]

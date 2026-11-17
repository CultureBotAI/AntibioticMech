"""Keep the experimental subject separate from background and reference IDs."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import embed_records as embed  # noqa: E402
import phibase_grounding_reviews as review  # noqa: E402
import seed_from_sources as seed  # noqa: E402

REVIEW_ID = "fujimura-1992-neurospora-subject-context"
FIXTURE = ROOT / "tests/fixtures/carbendazim-before-neurospora-2026-10-13.yaml"
OLD_REVIEWS = ROOT / "tests/fixtures/phibase-grounding-before-neurospora-2026-10-13.json"


def assert_common_mapping_order(before, after):
    if isinstance(before, dict) and isinstance(after, dict):
        assert [k for k in before if k in after] == [k for k in after if k in before]
        for key in before.keys() & after.keys():
            assert_common_mapping_order(before[key], after[key])
    elif isinstance(before, list) and isinstance(after, list):
        for a, b in zip(before, after, strict=False):
            assert_common_mapping_order(a, b)


@pytest.mark.parametrize("nested", [False, True])
def test_order_guard_rejects_sorted_snapshots_even_when_semantics_match(nested):
    original = load_record(FIXTURE)
    changed = copy.deepcopy(original)
    if nested:
        changed["chemical_structure"] = dict(sorted(changed["chemical_structure"].items()))
    else:
        changed = dict(sorted(changed.items()))
    assert original == changed
    with pytest.raises(AssertionError):
        assert_common_mapping_order(original, changed)


def test_evidence_scope_retains_original_full_text_hold():
    context = json.loads((ROOT / "research/2026-10-13-neurospora-context.json").read_bytes())
    primary = context["primary"]
    assert primary["related_paper_review_complete"]
    assert not primary["original_paper_full_review_complete"]
    assert primary["printed_pages"] == list(range(237, 243))
    assert len(primary["native_pages_inspected"]) == 6
    assert not primary["numeric_measurements_exported"]
    assert not primary["sequences_variants_protocols_exported"]
    assert context["reference"]["accession"] == "P05220"
    assert (context["reference"]["entry_version"], context["reference"]["sequence_version"]) == (157, 2)
    assert not context["reference"]["experimental_allele_or_subject_accession"]
    assert {t["taxon_id"]: t["rank"] for t in context["taxonomy"]} == {5141: "species", 367110: "strain"}
    assert context["decision"]["original_full_text_review"] == "OPEN"
    assert context["decision"]["new_resistance_assertions"] == 0
    assert context["decision"]["exact_experimental_accessions"] == "UNRESOLVED"


def test_frozen_inputs_and_source_owned_decision():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == (
        "2a7c2567e8ec2d4e5ceb6bbd5f039e79318dca63718fe795102def3104df9e26")
    assert hashlib.sha256(OLD_REVIEWS.read_bytes()).hexdigest() == (
        "e6b233643b91bde972e2f863c7557995fa452fa1733d069a8d8aa1577ff6b5d8")
    old, current = json.loads(OLD_REVIEWS.read_bytes()), json.loads(review.DEFAULT_REVIEW.read_bytes())
    decision, = [r for r in current["reviews"] if r["review_id"] == REVIEW_ID]
    assert {**current, "reviews": [r for r in current["reviews"] if r["review_id"] != REVIEW_ID]} == old
    assert decision["pmid"] == "1388107" and decision["subject_strain"] == "F914"
    assert decision["withhold"] == ["strain_taxon_id", "protein_accession"]
    assert not {"misassigned", "subject_taxon", "withhold_strain"} & decision.keys()
    assert decision["reference"] == "DOI:10.1584/jpestics.17.4_237"
    assert decision["source_rows"] == [{"identifier": "CHEBI:3392", "row_sha256":
        "7ace37c6427c588526fb1cc75a5b8d5ac8325c9a71230497df9e8cf18f319626"}]


def test_full_source_slice_changes_one_subject_and_previous_checksums_only():
    inventory = ROOT / "data/raw/phibase_amr.tsv"
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"],
        "chemical_structure": {"standard_inchi_key": r["standard_inchi_key"]}} for r in rows}
    before, after = copy.deepcopy(fixture), copy.deepcopy(fixture)
    assert seed.attach_phibase_resistance(before, grounding_review=OLD_REVIEWS)[
        "reviewed_identifier_context"] == 189
    assert seed.attach_phibase_resistance(after)["reviewed_identifier_context"] == 190
    old_sha = hashlib.sha256(OLD_REVIEWS.read_bytes()).hexdigest()
    current_sha = hashlib.sha256(review.DEFAULT_REVIEW.read_bytes()).hexdigest()
    corrected = refreshed = 0
    for identifier, old in before.items():
        new = after[identifier]
        assert embed.build_document(old, {}) == embed.build_document(new, {})
        for a, b in zip(old["resistance_mechanisms"], new["resistance_mechanisms"], strict=True):
            if a == b:
                continue
            fields = {k for k in a.keys() | b.keys() if a.get(k) != b.get(k)}
            if a["evidence"][0]["reference"] == "PMID:1388107":
                assert identifier == "CHEBI:3392"
                assert fields == {"strain", "strain_taxon_id", "protein_accession", "note", "evidence"}
                assert a["strain"] == "74-OR31-14a" and b["strain"] == "F914"
                assert a["evidence"] == b["evidence"][:-1]
                assert a["gene_id"] == b["gene_id"] == "EAA28433"
                corrected += 1
            else:
                assert fields == {"evidence"}
                assert a["evidence"][:-1] == b["evidence"][:-1]
                assert a["evidence"][-1]["notes"].replace(old_sha, current_sha) == b["evidence"][-1]["notes"]
                assert a["evidence"][-1]["reference"] == b["evidence"][-1]["reference"]
                refreshed += 1
    assert (corrected, refreshed) == (1, 189)


def test_guarded_record_transition_retains_all_other_biology():
    old = load_record(FIXTURE)
    new = load_record(ROOT / "data/antibiotics/antifungal/carbendazim.yaml")
    assert_common_mapping_order(old, new)
    assert {k:v for k,v in old.items() if k not in {"resistance_mechanisms", "curation_history"}} == {
        k:v for k,v in new.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "REVIEWED_RESISTANCE_SUBJECT_CONTEXT"
    assert new["curation_history"][-1]["llm_assisted"] is True
    assert len(new["resistance_mechanisms"]) == len(old["resistance_mechanisms"]) == 19
    assert [c for c in old["resistance_mechanisms"] if not seed.is_phibase_sourced_resistance(c)] == [
        c for c in new["resistance_mechanisms"] if not seed.is_phibase_sourced_resistance(c)]
    target, = [c for c in new["resistance_mechanisms"] if c["evidence"][0]["reference"] == "PMID:1388107"]
    assert target["strain"] == "F914" and target["taxon_id"] == "NCBITaxon:5141"
    assert not {"strain_taxon_id", "protein_accession"} & target.keys()
    assert "Original source background label: 74-OR31-14a." in target["note"]
    assert "strain_taxon_id=NCBITaxon:367110; protein_accession=UniProtKB:P05220" in target["note"]
    assert "Original full-text review remains open" in target["note"]
    assert "not a verified experimental allele or gene-object assignment" in target["note"]
    assert embed.build_document(old, {}) == embed.build_document(new, {})

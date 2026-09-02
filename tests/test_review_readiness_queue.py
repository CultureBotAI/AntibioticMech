"""The review queue is exhaustive but never substitutes automation for sign-off."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curation_worklist import review_readiness_queue  # noqa: E402


def _record(identifier: str, **updates: object) -> dict:
    record = {
        "identifier": identifier,
        "label": identifier,
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "chemical_structure": {
            "smiles": "CC",
            "standard_inchi": "InChI=1S/C2H6",
            "standard_inchi_key": "OTMSDBZUPAUEDD-UHFFFAOYSA-N",
            "molecular_formula": "C2H6",
        },
        "source_concepts": [{"source": "CHEBI", "source_id": identifier}],
    }
    record.update(updates)
    return record


def test_queue_contains_every_unsigned_record_once():
    records = [
        _record("CHEBI:1"),
        _record("CHEBI:2", curation_status="PROPOSED"),
        _record("CHEBI:3", curation_status="REVIEWED"),
        _record("CHEBI:4", curation_status="DEPRECATED"),
    ]
    rows = review_readiness_queue(records, source_refs={})
    assert [row["key"] for row in rows] == ["CHEBI:1", "CHEBI:2"]


def test_source_citations_are_labeled_as_leads_not_evidence():
    record = _record("CHEBI:5")
    refs = {("CHEBI", "CHEBI:5"): ("PMID:123", "DOI:10.1/example")}
    row = review_readiness_queue([record], source_refs=refs)[0]
    assert row["source_id"] == "PMID:123|DOI:10.1/example"
    assert "2 source literature lead(s)" in row["hint"]
    assert "0 record evidence item(s)" in row["hint"]


def test_identity_and_structure_are_checked_before_mechanism():
    minted = _record("antibioticmech:1", grounding_status="MINTED")
    incomplete = _record("CHEBI:6", chemical_structure={"smiles": "CC"})
    rows = {row["key"]: row["hint"] for row in
            review_readiness_queue([minted, incomplete], source_refs={})}
    assert rows["antibioticmech:1"].startswith("IDENTITY_REVIEW:")
    assert rows["CHEBI:6"].startswith("STRUCTURE_REVIEW:")


def test_seeded_mechanism_is_not_mistaken_for_curator_review():
    record = _record(
        "CHEBI:7",
        mode_of_action="PROTEIN_SYNTHESIS_INHIBITION",
        mode_of_action_notes=(
            "Assigned from ChEBI role CHEBI:48001. Not a curator's review."
        ),
    )
    row = review_readiness_queue([record], source_refs={})[0]
    assert row["hint"].startswith("MECHANISM_REVIEW:")
    assert "not curator-checked" in row["hint"]


def test_primary_target_evidence_is_a_gate_after_mechanism_review():
    record = _record(
        "CHEBI:8",
        mode_of_action="DNA_SYNTHESIS_INHIBITION",
        mode_of_action_notes="CURATOR: checked against primary literature.",
        molecular_targets=[{"evidence_status": "PRIMARY_EVIDENCE_NEEDED"}],
    )
    row = review_readiness_queue([record], source_refs={})[0]
    assert row["hint"].startswith("TARGET_EVIDENCE_REVIEW:")


def test_corpus_queue_matches_every_unsigned_record(records):
    docs = [record for _path, record in records]
    expected = {
        record["identifier"] for record in docs
        if record.get("curation_status") not in {"REVIEWED", "DEPRECATED"}
    }
    actual = {row["key"] for row in review_readiness_queue(docs)}
    assert actual == expected

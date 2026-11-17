"""Keep laboratory gene evidence separate from reference and background IDs."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mycophenolic_subjects as audit  # noqa: E402
from resistance_checkpoint_records import checkpoint_path  # noqa: E402

from antibioticmech.activity_collections import load_record  # noqa: E402
from antibioticmech.curate.curation_event import record_curation_event  # noqa: E402
from antibioticmech.validation.write_validated import write_validated_antibiotic  # noqa: E402


def context():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


@pytest.mark.parametrize(
    "change",
    [
        "empty",
        "missing_primary",
        "missing_tables",
        "missing_limits",
        "reference_only",
        "species",
        "experimental_protein",
        "strain",
        "allele",
        "genome",
        "gene",
        "primary_doi",
        "viability",
        "background_role",
        "version",
        "accession",
    ],
)
def test_claims_require_complete_reviewed_context(change):
    data = context()
    if change == "empty":
        data = {}
    elif change == "missing_primary":
        data.pop("inputs")
    elif change == "missing_tables":
        data.pop("supplement_context")
    elif change == "missing_limits":
        data.pop("evidence_scope")
    elif change == "reference_only":
        data = {"reference": data["reference"]}
    elif change == "species":
        data["curation"]["species_taxon_id"] = "NCBITaxon:559292"
    elif change in {"experimental_protein", "strain", "allele", "genome"}:
        data["curation"][change] = "UNSUPPORTED_SUBJECT_ASSIGNMENT"
    elif change == "gene":
        data["curation"]["supported_gene_associations"].append("IMD2")
    elif change == "primary_doi":
        data["primary_doi"] = "OTHER"
    elif change == "viability":
        data["supplement_context"]["table-s1"]["viability_interpreted_as_resistance"] = True
    elif change == "background_role":
        data["supplement_context"]["table-s2"]["labels_are_variant_specific_subject_identifiers"] = True
    else:
        data["reference"]["entry_version" if change == "version" else "protein_accession"] = "OTHER"
    with pytest.raises(ValueError, match="complete reviewed"):
        audit.claims(data)


def test_qualified_gene_claim_does_not_promote_reference_ids():
    (claim,) = audit.claims(context())
    assert claim["gene_families"] == ["RPB1"]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["taxon_id"] == "NCBITaxon:4932"
    assert {"protein_accession", "gene_id", "strain_taxon_id", "strain", "alteration"}.isdisjoint(claim)
    assert "Other RPB1 comparisons are sensitive" in claim["note"]
    assert "not uniquely IMD2-specific" in claim["note"]
    assert "UniProtKB:P04050" in {e["reference"] for e in claim["evidence"]}


def test_native_supplement_scope():
    data = context()
    assert data["supplement_context"]["table-s1"]["rows_including_header"] == 116
    assert data["supplement_context"]["table-s1"]["viability_interpreted_as_resistance"] is False
    assert data["supplement_context"]["table-s2"]["source_background_labels"] == [
        "CKY274",
        "CKY283",
        "CKY944",
    ]
    assert data["supplement_context"]["text-s1"]["genetic_comparison_background"] == "CKY283"
    assert data["curation"]["whole_record_review_complete"] is False
    assert data["constraints"]["issue_1040"] == "DEFERRED"


def test_unreviewed_document_refused(tmp_path):
    path = tmp_path / "fake.docx"
    path.write_bytes(b"not the reviewed document")
    with pytest.raises(ValueError, match="supplement identity"):
        audit.document_context(path, "table-s2")


def test_historical_transition_preserves_unrelated_fields(tmp_path):
    receipt = json.loads((ROOT / "research/2026-10-14-mycophenolic-curation.json").read_bytes())
    before = load_record(ROOT / audit.FIXTURE)
    assert hashlib.sha256((ROOT / audit.FIXTURE).read_bytes()).hexdigest() == receipt["before"]["sha256"]
    assert not before.get("resistance_mechanisms")
    after = copy.deepcopy(before)
    after["resistance_mechanisms"] = audit.claims(context())
    record_curation_event(after, **receipt["curation_event"])
    assert after["curation_history"][:-1] == before["curation_history"]
    assert {k: v for k, v in after.items() if k not in {"resistance_mechanisms", "curation_history"}} == {
        k: v for k, v in before.items() if k not in {"resistance_mechanisms", "curation_history"}
    }
    target = tmp_path / "record.yaml"
    write_validated_antibiotic(after, target)
    payload = target.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == receipt["record"]["sha256"]
    write_validated_antibiotic(load_record(target), target)
    assert target.read_bytes() == payload
    item = {"identifier": "CHEBI:168396", "path": str(audit.RECORD), "sha256": receipt["before"]["sha256"]}
    assert checkpoint_path(ROOT, item) == ROOT / audit.FIXTURE


def test_offline_subject_replay(monkeypatch):
    directory = ROOT / audit.CACHE
    if not (directory / "reviewed-supplements.json").exists():
        pytest.skip("private native supplement cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    assert audit.canonical(audit.build(ROOT, directory)) == (ROOT / audit.OUTPUT).read_bytes()

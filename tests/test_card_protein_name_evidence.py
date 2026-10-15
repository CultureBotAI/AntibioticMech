"""Scoped literature reviews cannot silently promote reference identities."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_protein_name_evidence as audit  # noqa: E402
import record_review  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def inputs():
    return (
        json.loads((ROOT / audit.ASSESSMENTS).read_bytes()),
        json.loads((ROOT / audit.SCREEN["path"]).read_bytes()),
        json.loads((ROOT / audit.CITATION).read_bytes()),
    )


def test_all_six_candidates_and_all_definition_citations_are_accounted_for(inputs):
    notes, screen, citation = inputs
    before = copy.deepcopy(inputs)
    selected = audit.validate_assessments(notes, screen, citation)
    assert len(selected) == 6 and inputs == before
    assert notes["sources"]["mcr-naming"]["reference"] == "PMID:30053115"
    assert notes["sources"]["mcr-followup"]["reference"] == "DOI:10.1128/AAC.00649-18"
    assert notes["sources"]["ddl-review"]["medium"] == "PUBLISHER_REVIEW_ABSTRACT_ONLY"
    assert notes["sources"]["qnrb65"]["support"] == "unknown"


@pytest.mark.parametrize(
    "change",
    [
        "missing_term",
        "missing_source",
        "wrong_accession",
        "wrong_pmid",
        "wrong_doi",
        "conflated_citation",
        "negative_context",
        "later_context",
    ],
)
def test_identity_and_contradictory_evidence_fail_closed(inputs, change):
    notes, screen, citation = inputs
    if change == "missing_term":
        del notes["reviews"]["ARO:3002819"]
    elif change == "missing_source":
        del notes["sources"]["ddl-review"]
    elif change == "wrong_accession":
        notes["reviews"]["ARO:3002819"]["accession"] = "UniProtKB:OTHER"
    elif change == "wrong_pmid":
        citation["citation_identity"]["pmid"] = "1"
    elif change == "wrong_doi":
        citation["citation_identity"]["doi"] = "10.1128/AAC.00649-18"
    elif change == "conflated_citation":
        notes["sources"]["mcr-followup"]["reference"] = "PMID:30053115"
    else:
        notes["reviews"]["ARO:3004695"]["sources"].remove(
            "mcr-original" if change == "negative_context" else "mcr-later-context"
        )
    with pytest.raises(ValueError):
        audit.validate_assessments(notes, screen, citation)


@pytest.mark.parametrize(
    "field",
    [
        "experimental_subject_assignments",
        "exact_allele_assignments",
        "experimental_genome_assignments",
        "biological_records_changed",
        "curated_ast_observations",
        "whole_record_primary_signoffs",
        "ncbi_requests",
        "native_primary_files_cached",
        "all_primary_results_reviewed",
        "broad_reference_index_updated",
        "new_gene_symbols_inferred",
        "operational_details_exported",
        "reuse_terms_review_resumed",
    ],
)
def test_scope_cannot_be_promoted(inputs, field):
    notes, screen, citation = inputs
    notes["limits"][field] = True
    with pytest.raises(ValueError):
        audit.validate_assessments(notes, screen, citation)


def public_pins(root):
    receipt = json.loads((root / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 3
    assert {p["path"] for p in pins} == {str(audit.OUTPUT), str(audit.ASSESSMENTS), str(audit.CITATION)}
    for pin in pins:
        assert hashlib.sha256((root / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    return receipt


@pytest.fixture
def cache_free_readonly(monkeypatch):
    original = Path.open

    def guarded(path, mode="r", *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "reports")
        assert not any(flag in mode for flag in "wax+")
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)


def test_public_artifacts_and_structured_review_require_no_native_cache(cache_free_readonly, monkeypatch):
    def no_current_head_check(*args, **kwargs):
        raise AssertionError("historical working-tree review must remain valid after a commit")

    monkeypatch.setattr(record_review, "assert_current_source", no_current_head_check)
    receipt = public_pins(ROOT)
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["summary"]["complete_records_read"] == result["summary"]["live_card_claims"] == 8
    assert len(result["reviews"]) == 6 and len(result["source_rows"]) == 8
    assert all(
        not r["experimental_subject_assignment"]
        and not r["exact_allele_assignment"]
        and r["experimental_genome_assignment"] is None
        and not r["selected_for_broad_index"]
        for r in result["reviews"].values()
    )
    assert result["reviews"]["ARO:3002819"]["reference_identity"]["gene_field_present"] is False
    assert (
        result["reviews"]["ARO:3004285"]["reference_identity"]["reference_taxonomy"]["native_rank"]
        == "strain"
    )
    review_pin = receipt["structured_review"]["yaml"]
    assert hashlib.sha256((ROOT / review_pin["path"]).read_bytes()).hexdigest() == review_pin["sha256"]
    review = record_review.read_review(ROOT, review_pin["path"])
    assert review["completion"] == "partial" and review["verdict"] == "needs_curation"
    assert review["scope"]["population_size"] == 2939
    assert len(review["targets"]) == 8 and len(review["findings"]) == 4
    assert all(f["status"] == "open" for f in review["findings"])
    assert review["reviewer"]["independence"] == "self_review"


def test_live_replay_is_readonly_and_cache_free_when_source_bytes_are_current(cache_free_readonly):
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    for pin in result["inputs"].values():
        if audit.reference.digest(ROOT / pin["path"]) != pin["sha256"]:
            pytest.skip("historical input changed; immutable output and review are tested separately")
    with (ROOT / result["inputs"]["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if {r["path"] for r in census} != {
        str(p.relative_to(ROOT)) for p in (ROOT / "data/antibiotics").rglob("*.yaml")
    } or any(audit.reference.digest(ROOT / r["path"]) != r["record_sha256"] for r in census):
        pytest.skip("historical corpus changed; immutable output and review are tested separately")
    assert audit.build(ROOT) == result


@pytest.mark.parametrize("suffix", [".json", "-assessments.json", "-citation.json"])
def test_public_metadata_drift_is_detected_without_native_cache(tmp_path, suffix):
    for item in (".json", "-assessments.json", "-citation.json", "-verification.json"):
        path = Path(audit.PREFIX + item)
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_bytes((ROOT / path).read_bytes())
    target = tmp_path / (audit.PREFIX + suffix)
    target.write_bytes(target.read_bytes() + b"\n")
    with pytest.raises(AssertionError):
        public_pins(tmp_path)

"""Assay adjudication is exact, snapshot-pinned, and mandatory at publication."""

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import seed_from_sources  # noqa: E402
from ncbi_ast_assays import (  # noqa: E402
    CONTEXT_FIELDS,
    DEFAULT_REVIEW_MAP,
    apply_assay_review,
    assay_signature,
    read_assay_review,
)
from seed_from_sources import ncbi_ast_activity_observation  # noqa: E402


def review_data():
    return {
        "source_version": "test-snapshot", "reviewed_on": "2026-10-03",
        "candidate_sha256": "a" * 64,
        "rationales": {
            "compatible": {"decision": "ACCEPT", "explanation": "Test-compatible MIC platform.",
                           "references": ["https://example.org/assay"]},
            "unresolved": {"decision": "QUARANTINE", "explanation": "Test measurement conflict.",
                           "references": ["https://example.org/conflict"]},
        },
        "contexts": [
            dict(method="", platform="Vitek", vendor="", reagent="", measurement="MIC", basis="compatible"),
            dict(method="", platform="Vitek", vendor="", reagent="", measurement="DISK", basis="unresolved"),
        ],
    }


def write_review(tmp_path, data):
    path = tmp_path / "review.json"
    path.write_text(json.dumps(data))
    return path


def row(**overrides):
    return dict(source_version="test-snapshot", method="", platform="Vitek", vendor="", reagent="",
                mic_value="2", disk_diffusion_value="", ast_row_count="3", **overrides)


def test_review_preserves_rows_and_separates_group_counts_from_measurements(tmp_path):
    review = read_assay_review(write_review(tmp_path, review_data()))
    accepted_row = row()
    excluded_row = {**row(), "mic_value": "", "disk_diffusion_value": "20", "ast_row_count": "7"}
    original = copy.deepcopy([accepted_row, excluded_row])
    accepted, counts = apply_assay_review([accepted_row, excluded_row], review)
    assert accepted == [accepted_row]
    assert [accepted_row, excluded_row] == original
    assert sum(c["groups"] for c in counts) == 2
    assert sum(c["measurements"] for c in counts) == 10
    with pytest.raises(ValueError, match="quarantined"):
        review.require_accepted(excluded_row)


@pytest.mark.parametrize(("field", "value", "message"), [
    ("source_version", "new-snapshot", "source_version"),
    ("vendor", "different-vendor", "unreviewed"),
    ("platform", "vitek", "unreviewed"),
    ("reagent", "E-Test", "unreviewed"),
    ("disk_diffusion_value", "20", "unreviewed"),
])
def test_review_rejects_snapshot_or_context_drift(tmp_path, field, value, message):
    review = read_assay_review(write_review(tmp_path, review_data()))
    with pytest.raises(ValueError, match=message):
        apply_assay_review([{**row(), field: value}], review)


@pytest.mark.parametrize("change", [
    lambda d: d["contexts"].append(d["contexts"][0]),
    lambda d: d["contexts"][0].update(basis="unknown"),
    lambda d: d["contexts"][0].update(measurement="mic"),
    lambda d: d["contexts"][0].update(vendor=" vendor "),
    lambda d: d.update(candidate_sha256="bad"),
    lambda d: d.update(reviewed_on="2026-02-30"),
    lambda d: d["rationales"]["compatible"].update(decision="PENDING"),
    lambda d: d["rationales"]["compatible"].update(references=[]),
    lambda d: d["rationales"]["compatible"].update(explanation=""),
])
def test_malformed_reviews_fail_closed(tmp_path, change):
    data = review_data()
    change(data)
    with pytest.raises(ValueError):
        read_assay_review(write_review(tmp_path, data))


def test_duplicate_json_keys_are_rejected(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text('{"contexts": [], "contexts": []}')
    with pytest.raises(ValueError, match="duplicate"):
        read_assay_review(path)


def test_committed_decisions_cover_the_reviewed_contexts_and_measurement_conflicts():
    review = read_assay_review(DEFAULT_REVIEW_MAP)
    assert len(review.decisions) == 60
    assert sum(d["decision"] == "ACCEPT" for d in review.decisions.values()) == 48
    for measurement, decision in (("MIC", "QUARANTINE"), ("DISK", "ACCEPT")):
        key = ("", "Not applicable", "Not applicable", "Antibiotic disk", measurement)
        assert review.decisions[key]["decision"] == decision
    assert review.decisions[("", "Vitek", "Biom\u00e9rieux", "E-Test", "MIC")]["decision"] == "QUARANTINE"
    assert review.decisions[("", "Vitek", "Trek", "GM-NEG", "MIC")]["decision"] == "QUARANTINE"


def test_observation_conversion_cannot_attach_quarantined_review_evidence(tmp_path):
    review = read_assay_review(write_review(tmp_path, review_data()))
    candidate = {**row(), "mic_value": "", "disk_diffusion_value": "20", "taxon_label": "E. coli",
                 "isolate_count": "1", "source_retrieved_on": "2026-10-03", "activity_group_id": "test"}
    with pytest.raises(ValueError, match="quarantined"):
        ncbi_ast_activity_observation(candidate, review)
    assert assay_signature(candidate) == tuple(
        "DISK" if field == "measurement" else candidate[field] for field in CONTEXT_FIELDS
    )


def test_attachment_requires_review_and_does_not_partially_mutate_records(tmp_path, monkeypatch):
    review_path = write_review(tmp_path, review_data())
    monkeypatch.setattr(seed_from_sources, "DEFAULT_REVIEW_MAP", review_path)
    monkeypatch.setattr(seed_from_sources, "NCBI_AST_ACTIVITY_INVENTORY", review_path)
    key = "AAAAAAAAAAAAAA-AAAAAAAAAA-A"
    first = {**row(), "identifier": "CHEBI:1", "standard_inchi_key": key, "mic_units": "mg/L",
             "taxon_label": "E. coli", "isolate_count": "1", "source_retrieved_on": "2026-10-03",
             "activity_group_id": "one", "biosample_accession": "", "target_accession": ""}
    second = {**first, "activity_group_id": "two", "mic_value": "", "disk_diffusion_value": "20"}
    monkeypatch.setattr(seed_from_sources, "load_ncbi_ast_activity_inventory", lambda _: [first, second])
    records = {"CHEBI:1": {"identifier": "CHEBI:1", "chemical_structure": {"standard_inchi_key": key},
                            "curation_history": []}}
    before = copy.deepcopy(records)
    with pytest.raises(ValueError, match="quarantined"):
        seed_from_sources.attach_ncbi_ast_activity(records)
    assert records == before


@pytest.mark.parametrize("existing_output", [False, True])
def test_review_cli_rejects_changed_candidates_and_existing_outputs_before_writing(tmp_path, existing_output):
    review_path = write_review(tmp_path, review_data())
    candidate = tmp_path / "candidate.tsv"
    candidate.write_text("not the pinned report")
    output = tmp_path / "output"
    if existing_output:
        output.mkdir()
        (output / "sentinel").write_text("retain")
    script = Path(__file__).resolve().parents[1] / "scripts/review_ncbi_ast_activity.py"
    result = subprocess.run([
        sys.executable, str(script), "--activity-report", str(candidate),
        "--assay-review", str(review_path), "--output-directory", str(output),
    ], capture_output=True, text=True)
    assert result.returncode != 0
    assert ("refusing to overwrite" if existing_output else "checksum") in result.stderr
    if existing_output:
        assert (output / "sentinel").read_text() == "retain"
        assert list(output.iterdir()) == [output / "sentinel"]
    else:
        assert not output.exists()

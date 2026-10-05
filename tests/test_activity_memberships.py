"""Membership files preserve source IDs, paired context, and repeated measurements."""

import copy
import gzip
import json
import sys
from pathlib import Path

import pytest
import yaml

from antibioticmech import activity_memberships as memberships
from antibioticmech.activity_collections import load_record
from antibioticmech.validation import write_validated as writer

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_strict  # noqa: E402
from test_write_validated import MINIMAL  # noqa: E402


def inputs():
    doc = copy.deepcopy(MINIMAL)
    doc["activity_spectrum"] = [{
        "taxon_label": "Mycobacterium tuberculosis complex", "assay": "broth microdilution",
        "source": "CRyPTIC", "source_version": "3.4.0", "source_observation_id": "group-1",
        "isolate_count": 3, "measurement_count": 4, "mic_value": 2.0,
        "mic_units": "mg/L", "mic_qualifier": ">", "activity": "RESISTANT",
        "evidence": [{"reference": "PMID:1", "notes": "Original source evidence"}],
    }]
    metadata = {
        "source": "CRyPTIC", "source_version": "3.4.0",
        "source_reference": "https://zenodo.org/records/15680920",
        "source_retrieved_on": "2026-10-05", "source_snapshot_sha256": "a" * 64,
        "activity_inventory_sha256": "b" * 64,
    }
    groups = {"group-1": [
        {"source_isolate_id": "unmatched", "sequencing_context": None, "measurement_count": 2},
        {"source_isolate_id": "first", "sequencing_context": {
            "biosample_accession": "SAMEA123", "bioproject_accession": "PRJEB123",
            "run_accession": "ERR123"}, "measurement_count": 1},
        {"source_isolate_id": "second", "sequencing_context": {
            "biosample_accession": "SAMEA123", "bioproject_accession": "PRJEB123",
            "run_accession": "ERR456"}, "measurement_count": 1},
    ]}
    return doc, metadata, groups


def prepared():
    doc, metadata, groups = inputs()
    ref, payload = memberships.build_collection(doc, metadata, groups)
    doc[memberships.FIELD] = [ref]
    return doc, ref, {ref["path"]: payload}


def test_roundtrip_writer_and_strict_validation(tmp_path):
    doc, ref, artifacts = prepared()
    before = copy.deepcopy(doc)
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path, membership_artifacts=artifacts)
    assert load_record(path) == doc == before
    assert not validate_strict.validate_one(path)
    registry = memberships.read_memberships(doc, path)[0][1]
    assert ref["subject_count"] == 3  # Shared BioSample does not collapse source IDs.
    assert ref["unlinked_subject_count"] == 1
    assert ref["membership_count"] == 3
    assert ref["measurement_count"] == 4
    assert registry["subjects"][-1]["sequencing_context"] is None
    original = path.read_bytes()
    writer.write_validated_antibiotic(load_record(path), path)
    assert path.read_bytes() == original
    assert prepared()[2] == artifacts
    assert not memberships.orphaned_membership_artifacts(tmp_path)


@pytest.mark.parametrize("field", sorted(memberships.REFERENCE_FIELDS))
def test_all_reference_fields_required(tmp_path, field):
    doc, ref, artifacts = prepared()
    ref.pop(field)
    with pytest.raises(writer.ValidationFailedError):
        writer.write_validated_antibiotic(doc, tmp_path / "bad.yaml", membership_artifacts=artifacts)
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("change", [
    "identifier", "chemical", "mic", "call", "method", "evidence", "count", "duplicate", "extra",
    "version", "missing-group", "boolean-count", "reference-count", "extra-artifact",
])
def test_stale_binding_rejected_without_any_writes(tmp_path, change):
    doc, ref, artifacts = prepared()
    row = doc["activity_spectrum"][0]
    if change == "identifier":
        doc["identifier"] = "CHEBI:1"
    elif change == "chemical":
        doc["chemical_structure"]["standard_inchi_key"] = "AAAAAAAAAAAAAA-BBBBBBBBBB-C"
    elif change in ("mic", "call", "method", "evidence", "count", "boolean-count"):
        field, value = {
            "mic": ("mic_value", 4.0), "call": ("activity", "SUSCEPTIBLE"),
            "method": ("assay", "another method"), "evidence": ("evidence", [{"reference": "PMID:2"}]),
            "count": ("measurement_count", 3), "boolean-count": ("isolate_count", True),
        }[change]
        row[field] = value
    elif change == "duplicate":
        doc["activity_spectrum"].append(copy.deepcopy(row))
    elif change == "extra":
        doc["activity_spectrum"].append({**row, "source_observation_id": "extra"})
    elif change == "version":
        ref["source_version"] = "4.0.0"
    elif change == "missing-group":
        doc["activity_spectrum"] = []
    elif change == "reference-count":
        ref["unlinked_subject_count"] = True
    else:
        artifacts["unused.json.gz"] = b"extra"
    with pytest.raises(writer.ValidationFailedError):
        writer.write_validated_antibiotic(doc, tmp_path / "bad.yaml", membership_artifacts=artifacts)
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("fault", [
    "duplicate-subject", "unused-subject", "partial-context", "bad-accession", "duplicate-group",
    "duplicate-member", "dangling-index", "boolean-index", "zero-count", "unknown-field",
    "empty-subjects", "empty-groups", "bad-date", "non-https", "bad-hash",
])
def test_payload_corruption_rejected(fault):
    _, _, artifacts = prepared()
    value = json.loads(gzip.decompress(next(iter(artifacts.values()))))
    group = value["groups"][0]
    if fault == "duplicate-subject":
        value["subjects"].append(copy.deepcopy(value["subjects"][0]))
    elif fault == "unused-subject":
        value["subjects"].append({"source_isolate_id": "unused", "sequencing_context": None})
    elif fault == "partial-context":
        value["subjects"][0]["sequencing_context"].pop("run_accession")
    elif fault == "bad-accession":
        value["subjects"][0]["sequencing_context"]["run_accession"] = "GCA_123.1"
    elif fault == "duplicate-group":
        value["groups"].append(copy.deepcopy(group))
    elif fault == "duplicate-member":
        group["members"].append(copy.deepcopy(group["members"][0]))
    elif fault in ("dangling-index", "boolean-index", "zero-count"):
        field, val = {"dangling-index": ("subject_index", 3), "boolean-index": ("subject_index", False),
                      "zero-count": ("measurement_count", 0)}[fault]
        group["members"][0][field] = val
    elif fault == "unknown-field":
        group["guess"] = "strain"
    elif fault.startswith("empty-"):
        value[fault.removeprefix("empty-")] = []
    else:
        field, val = {"bad-date": ("source_retrieved_on", "20261005"),
                      "non-https": ("source_reference", "http://example.org/"),
                      "bad-hash": ("source_snapshot_sha256", "abc")}[fault]
        value[field] = val
    with pytest.raises(ValueError):
        memberships.inspect_payload(gzip.compress(memberships.json_bytes(value), mtime=0))


@pytest.mark.parametrize("fault", ["missing", "symlink", "directory", "checksum", "truncated"])
def test_bad_file_rejected_by_load_and_strict(tmp_path, fault):
    doc, ref, artifacts = prepared()
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path, membership_artifacts=artifacts)
    artifact = tmp_path / ref["path"]
    artifact.unlink()
    if fault == "symlink":
        other = tmp_path / "other.gz"
        other.write_bytes(artifacts[ref["path"]])
        artifact.symlink_to(other)
    elif fault == "directory":
        artifact.mkdir()
    elif fault == "checksum":
        artifact.write_bytes(b"x" * ref["byte_size"])
    elif fault == "truncated":
        artifact.write_bytes(artifacts[ref["path"]][:-1])
    with pytest.raises(ValueError):
        load_record(path)
    assert validate_strict.validate_one(path)


def test_prune_only_valid_unreferenced_artifacts(tmp_path):
    doc, ref, artifacts = prepared()
    writer.write_validated_antibiotic(doc, tmp_path / "record.yaml", membership_artifacts=artifacts)
    (tmp_path / "record.yaml").unlink()
    assert memberships.orphaned_membership_artifacts(tmp_path) == [tmp_path / ref["path"]]
    (tmp_path / ref["path"]).write_bytes(b"corrupt")
    with pytest.raises(ValueError):
        memberships.orphaned_membership_artifacts(tmp_path)


def test_expanded_limit_duplicate_json_keys_and_nonfinite_rejected(monkeypatch):
    _, _, artifacts = prepared()
    payload = next(iter(artifacts.values()))
    memberships.inspect_payload.cache_clear()
    monkeypatch.setattr(memberships, "MAX_BYTES", len(gzip.decompress(payload)) - 1)
    with pytest.raises(ValueError, match="oversized"):
        memberships.inspect_payload(payload)
    for raw in (b'{"x":1,"x":2}\n', b'{"x":NaN}\n', b'{"x":1e999}\n'):
        with pytest.raises(ValueError):
            memberships.inspect_payload(gzip.compress(raw, mtime=0))


def test_other_source_observations_are_not_part_of_the_binding(tmp_path):
    doc, _, artifacts = prepared()
    doc["activity_spectrum"].append({"taxon_label": "curator", "evidence": [{"reference": "PMID:2"}]})
    writer.write_validated_antibiotic(doc, tmp_path / "record.yaml", membership_artifacts=artifacts)
    assert yaml.safe_load((tmp_path / "record.yaml").read_text()) == doc

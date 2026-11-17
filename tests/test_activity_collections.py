"""External storage must preserve every observation and fail closed on corruption."""

import copy
import gzip
import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

from antibioticmech import activity_collections as collections
from antibioticmech.validation import write_validated as writer

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import seed_from_sources as seed  # noqa: E402
import validate_strict  # noqa: E402
from test_write_validated import MINIMAL  # noqa: E402


def observation(number, **changes):
    return {
        "taxon_label": "Example tested isolate",
        "taxon_id": "NCBITaxon:562",
        "activity": "RESISTANT",
        "mic_value": 2.0,
        "mic_units": "mg/L",
        "mic_qualifier": ">=",
        "assay": "broth microdilution",
        "measurement_count": 1,
        "biosample_accession": f"SAMN{number + 1000}",
        "assembly_accession": "GCF_000005845.2",
        "source": "NCBI_AST",
        "source_version": "test-snapshot",
        "source_retrieved_on": "2026-10-03",
        "source_observation_id": f"test-{number}",
        "evidence": [{"reference": "PMID:1", "notes": f"Unmodified source context {number}"}],
        **changes,
    }


def record(count=7):
    return {
        **copy.deepcopy(MINIMAL), "activity_spectrum": [observation(i) for i in range(count)],
    }


@pytest.fixture(autouse=True)
def small_chunks(monkeypatch):
    # Exercise all boundaries cheaply; one test below uses the real 500-row size.
    monkeypatch.setattr(collections, "COLLECTION_SIZE", 3)


def installed(tmp_path, doc=None):
    doc = doc if doc is not None else record()
    physical, artifacts = collections.pack_activities(doc)
    collections.write_artifacts(artifacts, tmp_path)
    return physical, tmp_path / "record.yaml"


def replace_payload(tmp_path, reference, payload):
    compressed = gzip.compress(payload, mtime=0)
    checksum = hashlib.sha256(compressed).hexdigest()
    reference.update(path=f"activity-{checksum}.jsonl.gz", sha256=checksum, byte_size=len(compressed))
    (tmp_path / reference["path"]).write_bytes(compressed)


def test_real_chunk_size_roundtrip_preserves_order_counts_evidence_and_pairs(tmp_path, monkeypatch):
    monkeypatch.setattr(collections, "COLLECTION_SIZE", 500)
    doc = record(1001)
    curated = {"taxon_label": "curator row", "evidence": [{"reference": "PMID:2"}]}
    doc["activity_spectrum"].insert(0, curated)
    doc["activity_spectrum"].insert(751, {**curated, "taxon_label": "middle row"})
    last = doc["activity_spectrum"][-1]
    last.pop("assembly_accession")
    last.update(source_export_row_count=2, pathogen_detection_contexts=[
        {"pathogen_detection_target_accession": "PDT000000001.1", "assembly_accession": "GCA_000000001.1"},
        {"pathogen_detection_target_accession": "PDT000000002.1", "assembly_accession": "GCA_000000002.1"},
    ])
    before = copy.deepcopy(doc)
    physical, path = installed(tmp_path, doc)
    refs = physical["activity_collections"]
    assert [(r["offset"], r["observation_count"]) for r in refs] == [(1, 500), (501, 250)]
    assert collections.expand_activities(physical, path) == doc == before
    assert list(collections.expand_activities(physical, path)) == list(doc)
    assert collections.pack_activities(doc) == collections.pack_activities(doc)
    assert last in physical["activity_spectrum"]


def test_mixed_sources_versions_and_small_slices_stay_in_order(tmp_path):
    doc = record(3)
    rows = doc["activity_spectrum"]
    rows += [observation(4, source="CRYPTIC"), observation(5)]
    rows += [observation(i, source_version="second") for i in range(6, 10)]
    rows += [observation(10, source="CURATOR")]
    physical, path = installed(tmp_path, doc)
    assert [r["offset"] for r in physical["activity_collections"]] == [0, 5, 8]
    assert [r["source_version"] for r in physical["activity_collections"]] == [
        "test-snapshot", "second", "second",
    ]
    assert collections.expand_activities(physical, path) == doc


@pytest.mark.parametrize("source,count", [("NCBI_AST", 2), ("CRYPTIC", 7), ("CURATOR", 7)])
def test_small_or_other_source_records_remain_inline(source, count):
    doc = record(count)
    for row in doc["activity_spectrum"]:
        row["source"] = source
    assert collections.pack_activities(doc) == (doc, {})


def test_chunk_roundtrip_preserves_paired_genomes_and_disk_measurements(tmp_path):
    doc = record(3)
    row = doc["activity_spectrum"][1]
    for key in ("assembly_accession", "mic_value", "mic_units", "mic_qualifier"):
        row.pop(key)
    row.update(disk_diffusion_value=12.0, disk_diffusion_qualifier="<=", disk_diffusion_units="mm",
               assay="disk diffusion", source_export_row_count=2, pathogen_detection_contexts=[
        {"source_observation_id": "context-1",
         "pathogen_detection_target_accession": "PDT000000001.1", "assembly_accession": "GCA_000000001.1",
         "sra_accessions": ["SRR123456"], "source_create_date": "2020-01-01"},
        {"source_observation_id": "context-2",
         "pathogen_detection_target_accession": "PDT000000002.1", "assembly_accession": "GCA_000000002.1",
         "bioproject_accession": "PRJNA123456"},
    ])
    row["evidence"].append({"reference": "PMID:2", "notes": "all source text < & > " + chr(956)})
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path)
    assert collections.load_record(path) == doc
    assert not validate_strict.validate_one(path)


@pytest.mark.parametrize("field,value", [
    ("offset", -1), ("offset", True), ("offset", 1.0),
    ("observation_count", 0), ("observation_count", 4), ("observation_count", True),
    ("byte_size", 0), ("byte_size", collections.MAX_BYTES + 1),
    ("measurement_count", 0), ("measurement_count", True),
    ("format", "future-format"), ("sha256", "bad"), ("path", "../outside.jsonl.gz"),
    ("source", "CRYPTIC"), ("source_version", " "), ("source_retrieved_on", "20261003"),
    ("source_retrieved_on", "2026-02-30"), ("unexpected", "value"),
])
def test_malformed_references_fail_closed(tmp_path, field, value):
    physical, path = installed(tmp_path)
    physical["activity_collections"][0][field] = value
    with pytest.raises(ValueError):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("field", sorted(collections.REFERENCE_FIELDS))
def test_all_reference_fields_are_required(tmp_path, field):
    physical, path = installed(tmp_path)
    physical["activity_collections"][0].pop(field)
    with pytest.raises(ValueError):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("change", [
    "chemical", "identifier", "source_version", "retrieved", "count", "measurements", "bytes",
])
def test_identity_provenance_and_totals_are_bound_to_artifacts(tmp_path, change):
    physical, path = installed(tmp_path)
    ref = physical["activity_collections"][0]
    if change == "chemical":
        physical["chemical_structure"]["standard_inchi_key"] = "AAAAAAAAAAAAAA-BBBBBBBBBB-C"
    elif change == "identifier":
        physical["identifier"] = "CHEBI:1"
    elif change == "source_version":
        ref["source_version"] = "different"
    elif change == "retrieved":
        ref["source_retrieved_on"] = "2026-10-02"
    elif change == "count":
        ref["observation_count"] = 2
    elif change == "measurements":
        ref["measurement_count"] = 4
    else:
        ref["byte_size"] += 1
    with pytest.raises(ValueError):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("fault", ["missing", "corrupt", "symlink", "directory"])
def test_unavailable_or_nonregular_artifacts_fail_closed(tmp_path, fault):
    physical, path = installed(tmp_path)
    artifact = tmp_path / physical["activity_collections"][0]["path"]
    payload = artifact.read_bytes()
    artifact.unlink()
    if fault == "corrupt":
        artifact.write_bytes(b"x" * len(payload))
    elif fault == "symlink":
        other = tmp_path / "other.gz"
        other.write_bytes(payload)
        artifact.symlink_to(other)
    elif fault == "directory":
        artifact.mkdir()
    with pytest.raises(ValueError):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("fault", [
    "duplicate_key", "nan", "infinity", "overflow", "no_newline", "extra_row",
    "wrong_source", "missing_id", "bad_row",
])
def test_valid_checksum_cannot_hide_invalid_json_or_rows(tmp_path, fault):
    physical, path = installed(tmp_path)
    ref = physical["activity_collections"][0]
    payload = gzip.decompress((tmp_path / ref["path"]).read_bytes())
    if fault == "duplicate_key":
        payload = payload.replace(b'"mic_value":2.0', b'"mic_value":2.0,"mic_value":3.0', 1)
    elif fault in {"nan", "infinity", "overflow"}:
        payload = payload.replace(b'"mic_value":2.0', b'"mic_value":' + {
            "nan": b"NaN", "infinity": b"Infinity", "overflow": b"1e999",
        }[fault], 1)
    elif fault == "no_newline":
        payload = payload.rstrip(b"\n")
    elif fault == "extra_row":
        payload += payload.splitlines(keepends=True)[1]
    else:
        rows = [json.loads(line) for line in payload.splitlines()]
        if fault == "wrong_source":
            rows[1]["source_version"] = "other"
        elif fault == "missing_id":
            rows[1].pop("source_observation_id")
        else:
            rows[1] = []
        payload = b"".join((json.dumps(row) + "\n").encode() for row in rows)
    replace_payload(tmp_path, ref, payload)
    with pytest.raises(ValueError):
        collections.expand_activities(physical, path)


def test_decompression_is_bounded(tmp_path, monkeypatch):
    physical, path = installed(tmp_path)
    ref = physical["activity_collections"][0]
    replace_payload(tmp_path, ref, b" " * 5000 + b"\n")
    monkeypatch.setattr(collections, "MAX_BYTES", 4000)
    with pytest.raises(ValueError, match="oversized"):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("offset", [0, 4, 99])
def test_overlapping_or_gapped_offsets_are_rejected(tmp_path, offset):
    physical, path = installed(tmp_path, record(6))
    physical["activity_collections"][1]["offset"] = offset
    with pytest.raises(ValueError, match="offsets"):
        collections.expand_activities(physical, path)


@pytest.mark.parametrize("position", [1, 3, 6])
def test_duplicate_ids_are_refused_before_writing_across_all_chunks(tmp_path, position):
    doc = record()
    doc["activity_spectrum"][position]["source_observation_id"] = "test-0"
    with pytest.raises(writer.ValidationFailedError, match="duplicate"):
        writer.write_validated_antibiotic(doc, tmp_path / "record.yaml")
    assert not list(tmp_path.iterdir())


def test_duplicate_ids_between_inline_and_external_rows_are_rejected(tmp_path):
    physical, path = installed(tmp_path)
    physical["activity_spectrum"] = [observation(0)]
    with pytest.raises(ValueError, match="across collections"):
        collections.expand_activities(physical, path)


def test_validated_writer_is_deterministic_and_checks_external_schema(tmp_path):
    doc = record()
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path)
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    assert collections.load_record(path) == doc
    assert writer.emit_antibiotic_yaml(doc) == path.read_text()
    physical = yaml.safe_load(path.read_text())
    assert not writer.validate_antibiotic(physical, record_path=path)
    assert writer.validate_antibiotic(physical)
    writer.write_validated_antibiotic(physical, path)
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before
    assert seed.record_yaml_matches(path.read_text(), doc, record_path=path)
    with pytest.raises(ValueError, match="record path"):
        seed.record_yaml_matches(path.read_text(), doc)
    ref = physical["activity_collections"][0]
    rows = [json.loads(line) for line in gzip.decompress((tmp_path / ref["path"]).read_bytes()).splitlines()]
    rows[1]["unknown_field"] = "cannot hide behind a reference"
    replace_payload(tmp_path, ref, b"".join((json.dumps(row) + "\n").encode() for row in rows))
    path.write_text(yaml.safe_dump(physical))
    assert writer.validate_antibiotic(physical, record_path=path)
    assert validate_strict.validate_one(path)
    with pytest.raises(writer.ValidationFailedError, match="unknown_field"):
        writer.write_validated_antibiotic(physical, path)


def test_source_replacement_removes_stale_collection_rows_and_preserves_curator(tmp_path):
    original = record()
    curated = {"taxon_label": "curated", "assay": "literature", "evidence": [{"reference": "PMID:2"}]}
    original["activity_spectrum"].append(curated)
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(original, path)
    fresh = record(1)
    fresh["activity_spectrum"][0]["mic_value"] = 4.0
    merged = seed.merge_with_existing(fresh, collections.load_record(path))
    assert merged["activity_spectrum"] == fresh["activity_spectrum"] + [curated]
    writer.write_validated_antibiotic(merged, path)
    assert "activity_collections" not in yaml.safe_load(path.read_text())
    assert collections.load_record(path) == merged
    assert len(collections.orphaned_activity_artifacts(tmp_path)) == 3


def test_orphan_detection_preserves_shared_references_and_unrelated_files(tmp_path):
    doc = record()
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path)
    alias = tmp_path / "alias.yaml"
    alias.write_bytes(path.read_bytes())
    path.unlink()
    unrelated = tmp_path / "activity-private.jsonl.gz"
    unrelated.write_bytes(b"unrelated")
    assert collections.orphaned_activity_artifacts(tmp_path) == []
    alias.unlink()
    orphans = collections.orphaned_activity_artifacts(tmp_path)
    assert len(orphans) == 3 and unrelated not in orphans
    for artifact in orphans:
        artifact.unlink()
    assert unrelated.read_bytes() == b"unrelated"


def test_orphan_detection_fails_before_deletion_on_dangling_references(tmp_path):
    writer.write_validated_antibiotic(record(), tmp_path / "record.yaml")
    physical = yaml.safe_load((tmp_path / "record.yaml").read_text())
    (tmp_path / physical["activity_collections"][0]["path"]).unlink()
    before = set(tmp_path.iterdir())
    with pytest.raises(ValueError):
        collections.orphaned_activity_artifacts(tmp_path)
    assert set(tmp_path.iterdir()) == before


def test_atomic_record_failure_leaves_previous_record_readable(tmp_path, monkeypatch):
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(record(1), path)
    before = path.read_bytes()
    def fail(*args):
        raise OSError("simulated replacement failure")

    monkeypatch.setattr(writer.os, "replace", fail)
    with pytest.raises(OSError, match="replacement failure"):
        writer.write_validated_antibiotic(record(), path)
    assert path.read_bytes() == before
    assert collections.load_record(path) == record(1)
    assert len(collections.orphaned_activity_artifacts(tmp_path)) == 3
    assert all(p.suffix in {".gz", ".yaml"} for p in tmp_path.iterdir())


def test_immutable_artifacts_cannot_be_overwritten(tmp_path):
    _, artifacts = collections.pack_activities(record())
    collections.write_artifacts(artifacts, tmp_path)
    name = next(iter(artifacts))
    (tmp_path / name).write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="does not match"):
        collections.write_artifacts(artifacts, tmp_path)
    with pytest.raises(ValueError, match="content address"):
        collections.write_artifacts({"../outside.gz": b"bad"}, tmp_path)


def test_collection_only_records_cannot_appear_empty_to_consumers(tmp_path, monkeypatch):
    import antibiotic_report
    import curation_worklist
    import render_pages
    import research_antibiotic
    import score_causal_graph_quality

    doc = record(6)
    path = tmp_path / "record.yaml"
    writer.write_validated_antibiotic(doc, path)
    assert "activity_spectrum" not in yaml.safe_load(path.read_text())
    monkeypatch.setattr(render_pages, "CORPUS_DIR", tmp_path)
    monkeypatch.setattr(curation_worklist, "CORPUS_DIR", tmp_path)
    monkeypatch.setattr(antibiotic_report, "CORPUS_DIR", tmp_path)
    assert render_pages.load_records() == [(path, doc)]
    assert research_antibiotic.load_record(path) == doc
    assert curation_worklist.corpus_records() == [doc]
    assert antibiotic_report.load_corpus()[0][1] == doc
    assert score_causal_graph_quality.load_records(tmp_path)[0][1] == doc

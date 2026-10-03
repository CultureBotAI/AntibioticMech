"""Source-pinned isolate joins must enrich identity without changing AST evidence."""

import csv
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_ncbi_ast as fetch  # noqa: E402
from evaluate_ncbi_ast import (  # noqa: E402
    activity_group_id,
    enrich_isolate_identity,
    exact_activity_rows,
    write_activity_report,
)
from ncbi_ast_isolates import (  # noqa: E402
    ISOLATE_SOURCE,
    ISOLATE_VERSION_PREFIX,
    load_isolate_snapshot,
    read_isolate_export,
)
from seed_from_sources import (  # noqa: E402
    load_ncbi_ast_activity_inventory,
    ncbi_ast_activity_observation,
)


def isolate_record(**overrides):
    return {
        "target_acc": "PDT000277868.2", "biosample_acc": "SAMN04622941",
        "bioproject_acc": "PRJNA281531", "scientific_name": "Pasteurella multocida",
        "taxid": 747, "asm_acc": "GCA_002859245.1", "strain": "USDA-ARS-USMARC-60494",
        "isolate_identifiers": ["SRS3693226", "USDA-ARS-USMARC-60494"],
        **overrides,
    }


def isolate_payload(records):
    return json.dumps({
        "success": True, "ngout": {"data": {"content": records, "totalCount": len(records)}},
    }).encode()


def snapshot_directory(tmp_path, records=None):
    directory = tmp_path / "isolates"
    directory.mkdir()
    payload = isolate_payload(records if records is not None else [isolate_record()])
    (directory / "isolates.json").write_bytes(payload)
    checksum = hashlib.sha256(payload).hexdigest()
    count = len(json.loads(payload)["ngout"]["data"]["content"])
    metadata = {
        "source": ISOLATE_SOURCE, "file": "isolates.json", "sha256": checksum,
        "source_version": ISOLATE_VERSION_PREFIX + checksum,
        "source_retrieved_on": "2026-10-03", "bytes": len(payload),
        "rows": count, "count_before": count, "count_after": count,
    }
    (directory / "snapshot.json").write_text(json.dumps(metadata))
    return directory


def ast_row(**overrides):
    return {
        "Isolate": "PDT000277868.2", "BioSample": "SAMN04622941",
        "BioProject": "PRJNA281531", "Scientific name": "Pasteurella multocida",
        "Antibiotic": "florfenicol", "Resistance phenotype": "R", "MIC (mg/L)": "8",
        "Measurement sign": ">=", "Laboratory typing platform": "broth microdilution",
        **overrides,
    }


def activity_rows(snapshot):
    mapping = {"florfenicol": {
        "mapping_status": "EXACT", "source_name": "florfenicol",
        "identifier": "CHEBI:87185", "standard_inchi_key": "AYIRNRDRBQJXIF-NXEZZACHSA-N",
    }}
    return exact_activity_rows(
        enrich_isolate_identity([ast_row()], snapshot), mapping,
        source_version="ast-browser-sha256:" + "a" * 64,
        source_retrieved_on="2026-10-03", isolate_snapshot=snapshot,
    )


def test_fetch_isolate_snapshot_counts_checksums_and_minimal_fields(tmp_path, monkeypatch):
    requests = []
    payloads = iter([isolate_payload([isolate_record()])] * 3)

    def respond(url, **kwargs):
        requests.append(parse_qs(urlparse(url).query))
        return io.BytesIO(next(payloads))

    monkeypatch.setattr(fetch, "urlopen", respond)
    output = tmp_path / "download"
    metadata = fetch.fetch_snapshot(output, "target_acc:PDT000277868.2", "isolates")
    snapshot = load_isolate_snapshot(output)
    assert snapshot.source_version == metadata["source_version"]
    assert snapshot.records["PDT000277868.2"]["taxid"] == "747"
    assert metadata["rows"] == metadata["count_before"] == metadata["count_after"] == 1
    assert all(r["collection"] == ["isolates"] for r in requests)
    assert requests[1]["limit"] == ["1"]
    fields = requests[1]["fl"][0].split(",")
    assert "taxid" in fields and "asm_acc" in fields
    assert "AMR_genotypes" not in fields and "isolate_identifiers" not in fields


@pytest.mark.parametrize("field,value", [
    ("taxid", True), ("taxid", 0), ("taxid", "00747"), ("taxid", None),
    ("scientific_name", ""), ("scientific_name", "Pasteurella\tmultocida"),
    ("biosample_acc", "missing"), ("bioproject_acc", ""),
    ("target_acc", "PDT000277868"), ("asm_acc", "PDT000277868.2"),
])
def test_invalid_isolate_identity_is_rejected(tmp_path, field, value):
    directory = snapshot_directory(tmp_path, [isolate_record(**{field: value})])
    with pytest.raises(ValueError, match=field):
        load_isolate_snapshot(directory)


def test_incomplete_and_duplicate_isolate_exports_are_rejected(tmp_path):
    directory = snapshot_directory(tmp_path, [isolate_record(), isolate_record()])
    with pytest.raises(ValueError, match="duplicate target_acc"):
        load_isolate_snapshot(directory)
    payload = {"success": True, "ngout": {"data": {"content": [], "totalCount": 1}}}
    path = directory / "partial.json"
    path.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="incomplete"):
        read_isolate_export(path)


def test_partial_isolate_download_does_not_publish_snapshot(tmp_path, monkeypatch):
    payload = {"success": True, "ngout": {"data": {
        "content": [isolate_record()], "totalCount": 2,
    }}}
    monkeypatch.setattr(fetch, "urlopen", lambda *a, **kw: io.BytesIO(json.dumps(payload).encode()))
    with pytest.raises(ValueError, match="incomplete isolate export"):
        fetch.fetch_snapshot(tmp_path / "download", "number_drugs_tested:[1 TO *]", "isolates")
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("field,value", [
    ("sha256", "a" * 64), ("source_version", "unversioned"), ("bytes", 0),
    ("source_retrieved_on", "2026-02-30"), ("count_after", 2),
    ("file", "../isolates.json"), ("source", "NCBI_AST"),
])
def test_snapshot_manifest_cannot_mislabel_the_export(tmp_path, field, value):
    directory = snapshot_directory(tmp_path)
    manifest = directory / "snapshot.json"
    metadata = json.loads(manifest.read_text())
    metadata[field] = value
    manifest.write_text(json.dumps(metadata))
    with pytest.raises(ValueError):
        load_isolate_snapshot(directory)


def test_altered_snapshot_bytes_fail_before_join(tmp_path):
    directory = snapshot_directory(tmp_path)
    path = directory / "isolates.json"
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="checksum"):
        load_isolate_snapshot(directory)


def test_enrichment_preserves_measurements_and_does_not_invent_sra(tmp_path):
    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path))
    original = ast_row(**{"Organism group": "Pasteurella"})
    result = enrich_isolate_identity([original], snapshot)[0]
    assert {key: result[key] for key in original} == original
    assert result["taxid"] == "747"
    assert result["assembly_accession"] == "GCA_002859245.1"
    assert result["strain"] == "USDA-ARS-USMARC-60494"
    assert "taxid" not in original
    assert "sra_accessions" not in result


@pytest.mark.parametrize("overrides,match", [
    ({"Isolate": "PDT000277868.1"}, "no exact isolate target"),
    ({"Isolate": "PDT000277868"}, "no exact isolate target"),
    ({"BioSample": "SAMN999"}, "biosample_acc"),
    ({"biosample_acc": "SAMN999"}, "biosample_acc"),
    ({"BioProject": "PRJNA999"}, "bioproject_acc"),
    ({"Scientific name": "Other species"}, "scientific_name"),
    ({"scientific_name": "Other species"}, "scientific_name"),
    ({"taxid": "NCBITaxon:562"}, "taxid"),
    ({"taxid": "747", "NCBI Taxonomy ID": "562"}, "taxid"),
    ({"assembly_accession": "GCA_000000001.1"}, "asm_acc"),
    ({"strain": "other strain"}, "strain"),
])
def test_conflicting_join_context_is_not_overwritten(tmp_path, overrides, match):
    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path))
    row = ast_row(**overrides)
    unchanged = dict(row)
    with pytest.raises(ValueError, match=match):
        enrich_isolate_identity([row], snapshot)
    assert row == unchanged


def test_missing_genome_and_strain_stay_missing(tmp_path):
    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path, [isolate_record(asm_acc="", strain="")]))
    row = enrich_isolate_identity([ast_row()], snapshot)[0]
    assert row["taxid"] == "747"
    assert "assembly_accession" not in row and "strain" not in row


def test_enriched_report_round_trips_to_schema_with_both_sources(tmp_path):
    from antibioticmech.validation.write_validated import validate_antibiotic

    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path))
    report = tmp_path / "activity.tsv"
    write_activity_report(activity_rows(snapshot), report)
    row = load_ncbi_ast_activity_inventory(report)[0]
    assert row["isolate_source_version"] == snapshot.source_version
    observation = ncbi_ast_activity_observation(row)
    assert observation["taxon_id"] == "NCBITaxon:747"
    assert observation["assembly_accession"] == "GCA_002859245.1"
    assert observation["mic_value"] == 8
    assert observation["mic_qualifier"] == ">="
    assert observation["mic_units"] == "mg/L"
    assert observation["activity"] == "RESISTANT"
    assert observation["source_version"] == row["source_version"]
    assert snapshot.source_version in observation["evidence"][1]["notes"]
    assert snapshot.source_retrieved_on in observation["evidence"][1]["notes"]
    assert not validate_antibiotic(observation, target_class="ActivityObservation")


@pytest.mark.parametrize("overrides,match", [
    ({"isolate_source_version": ""}, "isolate_source_version"),
    ({"isolate_source_retrieved_on": ""}, "isolate_source_retrieved_on"),
    ({"isolate_source_retrieved_on": "20261003"}, "ISO date"),
    ({"target_accession": ""}, "versioned target_accession"),
    ({"taxon_id": ""}, "requires taxon_id"),
])
def test_report_and_seeder_reject_incomplete_join_provenance(tmp_path, overrides, match):
    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path))
    row = activity_rows(snapshot)[0]
    row.update(overrides)
    row["activity_group_id"] = activity_group_id(row)
    path = tmp_path / "activity.tsv"
    with pytest.raises(ValueError, match=match):
        write_activity_report([row], path)
    with path.open("w", newline="") as handle:
        from evaluate_ncbi_ast import ACTIVITY_REPORT_COLUMNS
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=ACTIVITY_REPORT_COLUMNS)
        writer.writeheader()
        writer.writerow(row)
    with pytest.raises(ValueError, match=match):
        load_ncbi_ast_activity_inventory(path)


def test_mixed_isolate_snapshots_cannot_share_one_report(tmp_path):
    from evaluate_ncbi_ast import ACTIVITY_REPORT_COLUMNS

    snapshot = load_isolate_snapshot(snapshot_directory(tmp_path))
    rows = activity_rows(snapshot)
    rows.append({**rows[0], "isolate_source_version": ISOLATE_VERSION_PREFIX + "b" * 64})
    path = tmp_path / "mixed.tsv"
    with pytest.raises(ValueError, match="inconsistent isolate snapshot provenance"):
        write_activity_report(rows, path)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=ACTIVITY_REPORT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError, match="inconsistent isolate snapshot provenance"):
        load_ncbi_ast_activity_inventory(path)


def test_cli_refuses_ast_version_mismatch_before_writing(tmp_path):
    directory = snapshot_directory(tmp_path)
    ast = tmp_path / "ast.tsv"
    row = ast_row()
    with ast.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=list(row))
        writer.writeheader()
        writer.writerow(row)
    output = tmp_path / "report.tsv"
    script = Path(__file__).resolve().parents[1] / "scripts/evaluate_ncbi_ast.py"
    result = subprocess.run([
        sys.executable, str(script), "--ast", str(ast), "--isolate-snapshot", str(directory),
        "--source-version", "wrong", "--antibiotic-report", str(output),
    ], capture_output=True, text=True)
    assert result.returncode != 0
    assert "AST file SHA-256" in result.stderr
    assert not output.exists()

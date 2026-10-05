"""Normalized CRyPTIC inputs reproduce members without changing assay claims."""

import copy
import csv
import json
import shutil
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_cryptic_memberships as audit  # noqa: E402
import cryptic_membership_inventory as inventory  # noqa: E402
import extract_cryptic_memberships as extractor  # noqa: E402
import seed_from_sources as seed  # noqa: E402
from ncbi_ast_inventory import inventory_metadata, open_activity_text, write_activity_text  # noqa: E402
from test_cryptic_membership import (  # noqa: E402
    KEY,
    fixture_args,
    recover,
)
from test_cryptic_membership import (
    cohort as parquet_cohort,
)
from test_write_validated import MINIMAL  # noqa: E402

from antibioticmech.activity_memberships import FIELD, read_memberships  # noqa: E402
from antibioticmech.validation.write_validated import write_validated_antibiotic  # noqa: E402

cohort = parquet_cohort


def test_normalized_round_trip_is_deterministic(cohort, tmp_path):
    groups, _ = recover(cohort)
    counts = extractor.write_inventories(groups, tmp_path)
    assert counts == {inventory.ISOLATES: 3, inventory.MEMBERSHIPS: 5}
    rebuilt = inventory.read_groups(
        cohort[2], tmp_path / inventory.ISOLATES, tmp_path / inventory.MEMBERSHIPS,
    )
    assert rebuilt == {group["activity"]["activity_group_id"]: group["members"] for group in groups}
    before = {name: (tmp_path / name).read_bytes() for name in counts}
    extractor.write_inventories(list(reversed(groups)), tmp_path)
    assert before == {name: (tmp_path / name).read_bytes() for name in counts}


def test_missing_adopted_phenotype_inventory_cannot_become_an_empty_source_slice(tmp_path, monkeypatch):
    monkeypatch.setattr(seed, "CRYPTIC_ACTIVITY_INVENTORY", tmp_path / "missing.tsv")
    with pytest.raises(SystemExit, match="missing inventory"):
        seed.attach_cryptic_memberships({})


@pytest.mark.parametrize("fault", [
    "duplicate-isolate", "partial-context", "extra-isolate", "unknown-isolate", "duplicate-member",
    "zero-count", "count-mismatch", "unknown-group", "missing-group", "version", "header", "short-row",
])
def test_malformed_inventory_rejected(cohort, tmp_path, fault):
    groups, _ = recover(cohort)
    extractor.write_inventories(groups, tmp_path)
    name = inventory.ISOLATES if fault in {"duplicate-isolate", "partial-context", "extra-isolate"} else (
        inventory.MEMBERSHIPS
    )
    path = tmp_path / name
    with open_activity_text(path) as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        columns, rows = reader.fieldnames, list(reader)
    if fault in {"duplicate-isolate", "duplicate-member"}:
        rows.append(copy.deepcopy(rows[0]))
    elif fault == "partial-context":
        rows[0]["run_accession"] = ""
    elif fault == "extra-isolate":
        rows.append({**rows[0], "source_isolate_id": "extra"})
    elif fault == "missing-group":
        rows = [row for row in rows if row["activity_group_id"] != rows[0]["activity_group_id"]]
    elif fault == "header":
        columns = [*columns, "unexpected"]
    elif fault == "short-row":
        rows[0].pop("measurement_count")
    else:
        field, value = {
            "unknown-isolate": ("source_isolate_id", "unknown"), "zero-count": ("measurement_count", "0"),
            "count-mismatch": ("measurement_count", "19"), "unknown-group": ("activity_group_id", "other"),
            "version": ("source_version", "4.0.0"),
        }[fault]
        rows[0][field] = value
    with write_activity_text(path) as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError):
        inventory.read_groups(cohort[2], tmp_path / inventory.ISOLATES, tmp_path / inventory.MEMBERSHIPS)


@pytest.fixture
def adopted(cohort, tmp_path, monkeypatch):
    args = fixture_args(cohort, tmp_path, monkeypatch)
    root = tmp_path / "repo"
    raw, curated = root / "data" / "raw", root / "curation"
    raw.mkdir(parents=True)
    curated.mkdir()
    (raw / "cryptic_activity.tsv").write_bytes(args.inventory.read_bytes())
    (curated / "cryptic_drug_map.tsv").write_bytes(args.drug_map.read_bytes())
    manifest = {"sources": {"cryptic": {"version": inventory.VERSION, "license": "CC BY 4.0",
                                       "homepage": inventory.REFERENCE}}, "downloads": {}, "inventories": {}}
    (raw / "MANIFEST.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False))
    monkeypatch.setattr(extractor, "ROOT", root)
    args.output_dir = root / "reports" / "dry"
    args.wgs_retrieved_on = "2026-10-05"
    args.apply = False
    report = extractor.extract(args)
    assert report["status"] == "STAGED"
    assert not (raw / inventory.ISOLATES).exists()
    assert "membership" not in yaml.safe_load((raw / "MANIFEST.yaml").read_text())["sources"]["cryptic"]
    args.apply = True
    args.output_dir = root / "reports" / "apply"
    report = extractor.extract(args)
    assert report["status"] == "ADOPTED"
    assert report == json.loads((args.output_dir / "report.json").read_text())
    return raw, curated / "cryptic_drug_map.tsv", args


def records(rows):
    doc = copy.deepcopy(MINIMAL)
    doc["identifier"] = "CHEBI:2637"
    doc["chemical_structure"]["standard_inchi_key"] = KEY
    doc["activity_spectrum"] = [seed.cryptic_activity_observation(row) for row in rows]
    return {doc["identifier"]: doc}


def test_extractor_manifest_seed_writer_and_source_owned_merge(cohort, adopted, tmp_path):
    raw, drug_map, _ = adopted
    fresh = records(cohort[2])
    before = copy.deepcopy(fresh["CHEBI:2637"]["activity_spectrum"])
    artifacts = inventory.attach(fresh, cohort[2], raw_dir=raw, drug_map=drug_map)
    doc = fresh["CHEBI:2637"]
    assert doc["activity_spectrum"] == before
    assert len(doc[FIELD]) == len(artifacts) == 1
    assert doc[FIELD][0]["subject_count"] == 3
    assert doc[FIELD][0]["membership_count"] == 5
    old = records(cohort[2])["CHEBI:2637"]
    other = {"source": "curator", "source_version": "example"}
    old[FIELD] = [other]
    old["activity_spectrum"].append({"taxon_label": "curator", "evidence": [{"reference": "PMID:2"}]})
    merged = seed.merge_with_existing(doc, old)
    assert merged[FIELD] == doc[FIELD] + [other]
    assert merged["activity_spectrum"] == before + old["activity_spectrum"][-1:]
    assert FIELD in merged["curation_history"][-1]["changes"]
    assert seed.merge_with_existing(doc, merged) == merged
    path = tmp_path / "record.yaml"
    write_validated_antibiotic(doc, path, membership_artifacts=artifacts)
    assert len(read_memberships(doc, path)[0][1]["groups"]) == 3
    assert len(inventory.sourced_view(merged)) == 1


@pytest.mark.parametrize("fault", ["missing", "checksum", "rows", "activity", "drug-map", "snapshot", "date"])
def test_adoption_pins_fail_closed(cohort, adopted, fault):
    raw, drug_map, _ = adopted
    manifest_path = raw / "MANIFEST.yaml"
    manifest = yaml.safe_load(manifest_path.read_text())
    if fault == "missing":
        (raw / inventory.ISOLATES).unlink()
    elif fault == "checksum":
        manifest["inventories"][inventory.ISOLATES]["sha256"] = "a" * 64
    elif fault == "rows":
        manifest["inventories"][inventory.MEMBERSHIPS]["rows"] += 1
    elif fault == "activity":
        (raw / "cryptic_activity.tsv").write_text("changed")
    elif fault == "drug-map":
        drug_map.write_text("changed")
    elif fault == "snapshot":
        manifest["downloads"]["WGS_SAMPLES.parquet"]["sha256"] = "a" * 64
    else:
        manifest["downloads"]["WGS_SAMPLES.parquet"]["retrieved_on"] = "2026-10-04"
    manifest_path.write_text(yaml.safe_dump(manifest))
    with pytest.raises((ValueError, OSError)):
        inventory.attach(records(cohort[2]), cohort[2], raw_dir=raw, drug_map=drug_map)


def test_identity_and_observation_drift_rejected(cohort, adopted):
    raw, drug_map, _ = adopted
    for fault in ("chemical", "observation"):
        docs = records(cohort[2])
        doc = docs["CHEBI:2637"]
        if fault == "chemical":
            doc["chemical_structure"]["standard_inchi_key"] = "AAAAAAAAAAAAAA-BBBBBBBBBB-C"
        else:
            doc["activity_spectrum"].pop()
        with pytest.raises(ValueError):
            inventory.attach(docs, cohort[2], raw_dir=raw, drug_map=drug_map)


def test_semantic_validation_still_runs_when_tampering_is_rehashed(cohort, adopted):
    raw, drug_map, _ = adopted
    path = raw / inventory.MEMBERSHIPS
    with open_activity_text(path) as handle:
        text = handle.read()
    with write_activity_text(path) as handle:
        handle.write(text.replace("\ta\t2", "\ta\t9"))
    manifest_path = raw / "MANIFEST.yaml"
    manifest = yaml.safe_load(manifest_path.read_text())
    manifest["inventories"][inventory.MEMBERSHIPS].update(inventory_metadata(path))
    manifest_path.write_text(yaml.safe_dump(manifest))
    with pytest.raises(ValueError, match="count/version"):
        inventory.attach(records(cohort[2]), cohort[2], raw_dir=raw, drug_map=drug_map)


def test_independent_raw_audit_checks_counts_context_and_extra_pairs(cohort, adopted, monkeypatch):
    raw, _, args = adopted
    monkeypatch.setattr(audit, "REPO_ROOT", raw.parent.parent)
    release = args.dst.parent
    (release / "dedupe").mkdir()
    shutil.copyfile(args.wgs, release / "dedupe" / "WGS_SAMPLES.parquet")
    groups, _ = recover(cohort)
    actual = {(group["activity"]["activity_group_id"], member["source_isolate_id"]):
              (member["measurement_count"], member["sequencing_context"])
              for group in groups for member in group["members"]}
    assert audit.raw_audit(cohort[2], actual, release) == 5
    for fault in ("count", "context", "extra"):
        altered = copy.deepcopy(actual)
        key = next(iter(altered))
        if fault == "count":
            altered[key] = (9, altered[key][1])
        elif fault == "context":
            altered[key] = (altered[key][0], None)
        else:
            altered[("extra", "extra")] = (1, None)
        with pytest.raises(ValueError):
            audit.raw_audit(cohort[2], altered, release)


@pytest.mark.parametrize("fault", ["manifest-drift", "inventory-copy", "manifest-write"])
def test_failed_installation_never_reports_adoption(adopted, monkeypatch, fault):
    raw, _, args = adopted
    args.output_dir = args.output_dir.with_name("failed-install")
    copyfile, write_text, load_adopted = shutil.copyfile, Path.write_text, extractor.load_adopted

    def fail_copy(source, destination, *positional, **kwargs):
        if fault == "inventory-copy" and Path(destination) == raw / inventory.ISOLATES:
            raise OSError("injected copy failure")
        return copyfile(source, destination, *positional, **kwargs)

    def fail_write(path, text, *positional, **kwargs):
        if fault == "manifest-write" and path == raw / "MANIFEST.yaml":
            raise OSError("injected manifest failure")
        return write_text(path, text, *positional, **kwargs)

    def drift_manifest(*positional, **kwargs):
        result = load_adopted(*positional, **kwargs)
        if fault == "manifest-drift":
            path = raw / "MANIFEST.yaml"
            path.write_text(path.read_text() + "# concurrent edit\n")
        return result

    monkeypatch.setattr(extractor.shutil, "copyfile", fail_copy)
    monkeypatch.setattr(Path, "write_text", fail_write)
    monkeypatch.setattr(extractor, "load_adopted", drift_manifest)
    with pytest.raises((OSError, ValueError), match="injected|manifest changed"):
        extractor.extract(args)
    assert json.loads((args.output_dir / "report.json").read_text())["status"] == "STAGED"

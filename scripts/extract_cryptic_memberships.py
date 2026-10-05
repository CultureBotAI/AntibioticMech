#!/usr/bin/env python3
"""Stage CRyPTIC membership inventories; --apply adopts validated staged inputs."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from datetime import date
from pathlib import Path

import yaml
from cryptic_membership_inventory import (
    ISOLATE_COLUMNS,
    ISOLATES,
    MEMBERSHIP_COLUMNS,
    MEMBERSHIPS,
    REFERENCE,
    ROOT,
    VERSION,
    load_adopted,
    sha256,
)
from evaluate_cryptic_membership import recover_cohort
from ncbi_ast_inventory import inventory_metadata, write_activity_text


def write_inventories(groups, directory):
    subjects = {}
    for group in groups:
        for member in group["members"]:
            unique_id = member["source_isolate_id"]
            context = member["sequencing_context"]
            if unique_id in subjects and subjects[unique_id] != context:
                raise ValueError("inconsistent CRyPTIC sequencing context")
            subjects[unique_id] = context
    with write_activity_text(directory / ISOLATES) as handle:
        writer = csv.DictWriter(handle, fieldnames=ISOLATE_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for unique_id, context in sorted(subjects.items()):
            writer.writerow({"source_version": VERSION, "source_isolate_id": unique_id, **(context or {})})
    with write_activity_text(directory / MEMBERSHIPS) as handle:
        writer = csv.DictWriter(handle, fieldnames=MEMBERSHIP_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for group in sorted(groups, key=lambda item: item["activity"]["activity_group_id"]):
            for member in sorted(group["members"], key=lambda item: item["source_isolate_id"]):
                writer.writerow({"source_version": VERSION,
                                 "activity_group_id": group["activity"]["activity_group_id"],
                                 "source_isolate_id": member["source_isolate_id"],
                                 "measurement_count": member["measurement_count"]})
    return {ISOLATES: len(subjects), MEMBERSHIPS: sum(len(g["members"]) for g in groups)}


def extract(args):
    output = args.output_dir.resolve()
    if (args.output_dir.exists() or args.output_dir.is_symlink()
            or not output.is_relative_to(ROOT / "reports")):
        raise ValueError("use a new staging directory under reports/")
    if date.fromisoformat(args.wgs_retrieved_on).isoformat() != args.wgs_retrieved_on or (
        date.fromisoformat(args.wgs_retrieved_on) > date.today()
    ):
        raise ValueError("provide the actual ISO retrieval date of the WGS snapshot")
    manifest_path = ROOT / "data" / "raw" / "MANIFEST.yaml"
    manifest_before = sha256(manifest_path)
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    groups, report = recover_cohort(args)
    # Production inputs cannot be replaced from an alternative phenotype/map pair.
    for key, path in (("inventory", ROOT / "data" / "raw" / "cryptic_activity.tsv"),
                      ("drug_map", ROOT / "curation" / "cryptic_drug_map.tsv")):
        if sha256(path) != report["inputs"][key]["sha256"]:
            raise ValueError(f"CRyPTIC extraction differs from the adopted {key}")
    output.mkdir(parents=True, exist_ok=False)
    counts = write_inventories(groups, output)
    provenance = {
        "retrieved_on": args.wgs_retrieved_on,
        "source_snapshot_sha256": report["inputs"]["wgs"]["sha256"],
        "activity_inventory_sha256": report["inputs"]["inventory"]["sha256"],
        "drug_map_sha256": report["inputs"]["drug_map"]["sha256"],
        "generated_by": "scripts/extract_cryptic_memberships.py",
    }
    manifest["sources"]["cryptic"]["membership"] = provenance
    manifest["downloads"]["WGS_SAMPLES.parquet"] = {
        "url": REFERENCE + "/files/WGS_SAMPLES.parquet?download=1",
        "sha256": provenance["source_snapshot_sha256"], "bytes": args.wgs.stat().st_size,
        "retrieved_on": args.wgs_retrieved_on,
    }
    for name, count in counts.items():
        manifest["inventories"][name] = {
            "rows": count, **inventory_metadata(output / name),
            "source": "CRyPTIC 3.4.0 exact adopted phenotype groups joined to WGS_SAMPLES by UNIQUEID",
        }
    manifest_text = yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True)
    (output / "MANIFEST.yaml").write_text(manifest_text, encoding="utf-8")
    shutil.copyfile(args.inventory, output / "cryptic_activity.tsv")
    rebuilt, metadata = load_adopted([g["activity"] for g in groups], raw_dir=output, drug_map=args.drug_map)
    if metadata is None or any(rebuilt[g["activity"]["activity_group_id"]] != g["members"] for g in groups):
        raise ValueError("CRyPTIC normalized inventory round trip changed membership")
    report.update(status="STAGED", membership=provenance,
                  inventories={name: manifest["inventories"][name] for name in counts},
                  extractor_sha256=sha256(Path(__file__)))
    (output / "report.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    if args.apply:
        if sha256(manifest_path) != manifest_before:
            raise ValueError("manifest changed during extraction")
        for name in counts:
            shutil.copyfile(output / name, manifest_path.parent / name)
        manifest_path.write_text(manifest_text, encoding="utf-8")
        report["status"] = "ADOPTED"
        (output / "report.json").write_text(
            json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    release = ROOT / "downloads" / "cryptic_3.4.0"
    for option, default in (
        ("drug-codes", release / "DRUG_CODES.csv.gz"), ("dst", release / "DST_MEASUREMENTS.parquet"),
        ("ukmyc", release / "UKMYC_PHENOTYPES.parquet"), ("wgs", release / "dedupe" / "WGS_SAMPLES.parquet"),
        ("drug-map", ROOT / "curation" / "cryptic_drug_map.tsv"),
        ("inventory", ROOT / "data" / "raw" / "cryptic_activity.tsv"),
    ):
        parser.add_argument("--" + option, type=Path, default=default)
    parser.add_argument("--wgs-retrieved-on", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    report = extract(parser.parse_args())
    print(json.dumps({"status": report["status"], "summary": report["summary"]}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Recover CRyPTIC group membership offline, without changing corpus claims.

This is an evaluation artifact, not an adopted inventory. Membership identifies
tested source isolates; sequencing runs are not assemblies or taxon identifiers.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import evaluate_cryptic_activity as cryptic
from seed_from_sources import load_cryptic_activity_inventory

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "antibioticmech-cryptic-group-membership-evaluation-v1"
ACCESSIONS = {
    "biosample_accession": r"SAM(N|D|EA)[0-9]+",
    "bioproject_accession": r"PRJ(NA|EB|DB)[0-9]+",
    "run_accession": r"[SED]RR[0-9]+",
}


def sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def require_source_id(value: object) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or any(
        ord(char) < 32 for char in value
    ):
        raise ValueError(f"invalid CRyPTIC UNIQUEID: {value!r}")
    return value


def wgs_index(connection, path: Path) -> dict[str, dict[str, str]]:
    result = {}
    for unique_id, sample, project, run, multiple in connection.execute(
        "SELECT UNIQUEID, sample_accession, study_accession, run_accession, "
        "has_multiple_ena_run_accessions FROM read_parquet(?)", [str(path)],
    ).fetchall():
        unique_id = require_source_id(unique_id)
        if unique_id in result:
            raise ValueError(f"duplicate CRyPTIC WGS UNIQUEID: {unique_id}")
        # The pinned release has one run per WGS row. Never guess how to split
        # future multi-run encodings or silently discard additional runs.
        if multiple is not False:
            raise ValueError(f"unsupported CRyPTIC multiple-run state: {unique_id}")
        context = dict(biosample_accession=sample, bioproject_accession=project,
                       run_accession=run)
        for field, pattern in ACCESSIONS.items():
            value = context[field]
            if not isinstance(value, str) or not re.fullmatch(pattern, value):
                raise ValueError(f"invalid CRyPTIC WGS {field}: {value!r}")
        result[unique_id] = context
    if not result:
        raise ValueError("empty CRyPTIC WGS table")
    return result


def require_same_inventory(adopted: list[dict], rebuilt: list[dict]) -> None:
    cryptic.require_inventory_rows(adopted, Path("adopted inventory"))
    cryptic.require_inventory_rows(rebuilt, Path("rebuilt inventory"))
    if {row["activity_group_id"]: row for row in adopted} != {
        row["activity_group_id"]: row for row in rebuilt
    }:
        raise ValueError("CRyPTIC rebuilt evidence does not match the adopted inventory")


def group_membership(connection, dst: Path, ukmyc: Path, inventory: list[dict],
                     mappings: dict, wgs: dict) -> list[dict]:
    """Join original typed grouping values, not rounded MICs or phenotype calls."""
    cryptic.require_inventory_rows(inventory, Path("adopted inventory"))
    expected = {row["activity_group_id"]: row for row in inventory}
    members: dict[str, dict[str, int]] = defaultdict(dict)
    for table, path in ((cryptic.DST_TABLE, dst), (cryptic.UKMYC_TABLE, ukmyc)):
        columns = cryptic.group_columns_for_table(table)
        fields = ", ".join(["DRUG", *[column.upper() for column in columns], "UNIQUEID"])
        # Identifiers above come only from the evaluator's fixed schema lists.
        rows = connection.execute(
            f"SELECT {fields}, count(*) FROM read_parquet(?) GROUP BY {fields}",
            [str(path)],
        ).fetchall()
        for values in rows:
            code, *rest = values
            if code not in mappings:
                raise ValueError(f"unmapped CRyPTIC drug code: {code!r}")
            if mappings[code]["mapping_status"] != cryptic.EXACT_MAPPING_STATUS:
                continue
            group_values, unique_id, count = rest[:-2], rest[-2], rest[-1]
            unique_id = require_source_id(unique_id)
            group_id = cryptic.activity_group_id(table, [code, *group_values])
            if group_id not in expected:
                raise ValueError(f"CRyPTIC membership has unadopted group: {group_id}")
            row = expected[group_id]
            mapping = mappings[code]
            if any(row[field] != mapping[field] for field in ("identifier", "standard_inchi_key")):
                raise ValueError(f"CRyPTIC membership chemical identity mismatch: {group_id}")
            if unique_id in members[group_id]:
                raise ValueError(f"CRyPTIC membership group-key collision: {group_id}")
            members[group_id][unique_id] = count
    if members.keys() != expected.keys():
        raise ValueError("CRyPTIC membership does not cover every adopted group")
    result = []
    for group_id, row in sorted(expected.items()):
        group = members[group_id]
        if sum(group.values()) != int(row["row_count"]) or len(group) != int(row["isolate_count"]):
            raise ValueError(f"CRyPTIC membership count mismatch: {group_id}")
        result.append({"activity": row, "members": [
            {"source_isolate_id": unique_id, "measurement_count": count,
             "sequencing_context": wgs.get(unique_id)}
            for unique_id, count in sorted(group.items())
        ]})
    return result


def summarize(groups: list[dict], wgs: dict) -> dict:
    unique_ids, linked_ids = set(), set()
    samples, projects, runs = set(), set(), set()
    counts: Counter = Counter()
    by_compound: dict[str, Counter] = defaultdict(Counter)
    for group in groups:
        activity = group["activity"]
        compound = by_compound[activity["identifier"]]
        compound["groups"] += 1
        compound["measurements"] += int(activity["row_count"])
        compound["group_isolate_memberships"] += len(group["members"])
        counts["measurements"] += int(activity["row_count"])
        counts["group_isolate_memberships"] += len(group["members"])
        counts["largest_group_isolates"] = max(counts["largest_group_isolates"], len(group["members"]))
        for member in group["members"]:
            unique_id, context = member["source_isolate_id"], member["sequencing_context"]
            unique_ids.add(unique_id)
            if context is None:
                counts["memberships_without_wgs"] += 1
                counts["measurements_without_wgs"] += member["measurement_count"]
                compound["memberships_without_wgs"] += 1
            else:
                linked_ids.add(unique_id)
                samples.add(context["biosample_accession"])
                projects.add(context["bioproject_accession"])
                runs.add(context["run_accession"])
    return {
        "groups": len(groups), "compounds": len(by_compound),
        **{key: counts[key] for key in (
            "measurements", "group_isolate_memberships", "largest_group_isolates",
            "memberships_without_wgs", "measurements_without_wgs",
        )},
        "source_isolate_ids": len(unique_ids), "source_isolate_ids_with_wgs": len(linked_ids),
        "source_isolate_ids_without_wgs": len(unique_ids - linked_ids),
        "biosamples": len(samples), "bioprojects": len(projects), "sequencing_runs": len(runs),
        "wgs_source_ids_not_in_adopted_phenotypes": len(wgs.keys() - unique_ids),
        "by_compound": {key: dict(value) for key, value in sorted(by_compound.items())},
    }


def json_line(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def recover_cohort(args):
    """Reproduce adopted groups and recover memberships from checksum-pinned files."""
    files = {"drug_codes": args.drug_codes, "dst": args.dst, "ukmyc": args.ukmyc,
             "wgs": args.wgs, "drug_map": args.drug_map, "inventory": args.inventory,
             "evaluator": Path(__file__), "activity_evaluator": Path(cryptic.__file__),
             "inventory_loader": ROOT / "scripts" / "seed_from_sources.py",
             "dependency_lock": ROOT / "uv.lock"}
    inputs = {key: {"filename": path.name, "sha256": sha256(path)} for key, path in files.items()}
    for path in (args.drug_codes, args.dst, args.ukmyc, args.wgs):
        cryptic.verify_release_file(path)
    codes = cryptic.read_drug_codes(args.drug_codes)
    mappings = cryptic.validated_drug_mappings(args.drug_map, codes)
    adopted = load_cryptic_activity_inventory(args.inventory)

    import duckdb

    with duckdb.connect() as connection:
        rebuilt = cryptic.activity_inventory(connection, args.dst, args.ukmyc, codes, mappings)
        require_same_inventory(adopted, rebuilt)
        wgs = wgs_index(connection, args.wgs)
        groups = group_membership(connection, args.dst, args.ukmyc, adopted, mappings, wgs)
    report = {
        "format": FORMAT, "source": "CRyPTIC", "source_version": cryptic.VERSION,
        "source_reference": f"https://zenodo.org/records/{cryptic.ZENODO_RECORD}",
        "status": "EVALUATION_ONLY", "inputs": inputs, "summary": summarize(groups, wgs),
        "duckdb_version": duckdb.__version__,
    }
    for key, path in files.items():
        if sha256(path) != inputs[key]["sha256"]:
            raise ValueError(f"CRyPTIC membership input changed during evaluation: {path}")
    return groups, report


def evaluate(args) -> dict:
    if args.output_dir.exists() or args.output_dir.is_symlink():
        raise ValueError(f"refusing to overwrite {args.output_dir}")
    output = args.output_dir.resolve()
    for name in ("data", "curation", "pages", "src"):
        if output.is_relative_to(ROOT / name):
            raise ValueError("membership evaluation cannot write into production directories")
    groups, report = recover_cohort(args)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    artifact = args.output_dir / "group-membership.jsonl.gz"
    with artifact.open("xb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as handle:
        handle.write(json_line({key: report[key] for key in (
            "format", "source", "source_version", "source_reference", "status", "inputs", "duckdb_version",
        )}))
        for group in groups:
            handle.write(json_line(group))
    report["artifact"] = {"path": artifact.name, "sha256": sha256(artifact),
                          "bytes": artifact.stat().st_size}
    with (args.output_dir / "report.json").open("x", encoding="utf-8") as handle:
        json.dump(report, handle, sort_keys=True, indent=2, allow_nan=False)
        handle.write("\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    release = ROOT / "downloads" / "cryptic_3.4.0"
    for option, default in (
        ("drug-codes", release / "DRUG_CODES.csv.gz"),
        ("dst", release / "DST_MEASUREMENTS.parquet"),
        ("ukmyc", release / "UKMYC_PHENOTYPES.parquet"),
        ("wgs", release / "dedupe" / "WGS_SAMPLES.parquet"),
        ("drug-map", cryptic.DEFAULT_DRUG_MAP),
        ("inventory", ROOT / "data" / "raw" / "cryptic_activity.tsv"),
    ):
        parser.add_argument("--" + option, type=Path, default=default)
    parser.add_argument("--output-dir", type=Path, required=True)
    report = evaluate(parser.parse_args())
    print(json.dumps(report["summary"], sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

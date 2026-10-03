#!/usr/bin/env python3
"""Audit exact BioSample overlap with adopted CRyPTIC evidence, without seeding.

Rebuild both inventories before comparing sample/drug membership. A shared
sample is a review lead, not proof that two assays are the same observation.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import evaluate_cryptic_activity as cryptic
import evaluate_ncbi_ast as ast
from ncbi_ast_assays import apply_assay_review, read_assay_review
from ncbi_ast_isolates import file_sha256, load_isolate_snapshot
from seed_from_sources import load_cryptic_activity_inventory

ROOT = Path(__file__).resolve().parents[1]


def require_same_inventory(adopted: list[dict], rebuilt: list[dict]) -> None:
    actual = {row["activity_group_id"]: row for row in adopted}
    expected = {row["activity_group_id"]: row for row in rebuilt}
    if actual != expected or len(actual) != len(adopted) or len(expected) != len(rebuilt):
        raise ValueError("CRyPTIC rebuilt evidence does not match the adopted inventory")


def cryptic_membership(connection, dst: Path, ukmyc: Path, wgs: Path, mappings: dict) -> dict:
    """Use only exact-mapped phenotype members, not every sequenced sample."""
    drugs_by_id: dict[str, set[str]] = defaultdict(set)
    for unique_id, code in connection.execute(
        "SELECT DISTINCT UNIQUEID, DRUG FROM read_parquet(?) "
        "UNION SELECT DISTINCT UNIQUEID, DRUG FROM read_parquet(?)", [str(dst), str(ukmyc)],
    ).fetchall():
        mapping = mappings[code]
        if mapping["mapping_status"] == cryptic.EXACT_MAPPING_STATUS:
            if not unique_id:
                raise ValueError("CRyPTIC exact phenotype has no UNIQUEID")
            drugs_by_id[unique_id].add(mapping["identifier"])

    all_samples, projects, represented_ids, seen_ids = set(), set(), set(), set()
    drugs_by_sample: dict[str, set[str]] = defaultdict(set)
    for unique_id, sample, project in connection.execute(
        "SELECT UNIQUEID, sample_accession, study_accession FROM read_parquet(?)", [str(wgs)],
    ).fetchall():
        if not unique_id or unique_id in seen_ids:
            raise ValueError("CRyPTIC WGS mapping requires unique nonempty UNIQUEIDs")
        seen_ids.add(unique_id)
        if not isinstance(sample, str) or not re.fullmatch(r"SAM(N|D|EA)[0-9]+", sample):
            raise ValueError(f"CRyPTIC WGS mapping has invalid BioSample {sample!r}")
        if not isinstance(project, str) or not re.fullmatch(r"PRJ(NA|EB|DB)[0-9]+", project):
            raise ValueError(f"CRyPTIC WGS mapping has invalid BioProject {project!r}")
        all_samples.add(sample)
        if unique_id in drugs_by_id:
            represented_ids.add(unique_id)
            projects.add(project)
            drugs_by_sample[sample].update(drugs_by_id[unique_id])
    return {
        "all_samples": all_samples, "projects": projects, "drugs_by_sample": drugs_by_sample,
        "counts": {
            "wgs_rows": len(seen_ids), "wgs_biosamples": len(all_samples),
            "adopted_phenotype_uniqueids": len(drugs_by_id),
            "adopted_phenotype_uniqueids_with_wgs": len(represented_ids),
            "adopted_phenotype_uniqueids_without_wgs": len(set(drugs_by_id) - represented_ids),
            "adopted_biosamples": len(drugs_by_sample), "adopted_bioprojects": len(projects),
        },
    }


def overlap_summary(rows, membership: dict, *, raw: bool, mappings: dict) -> dict:
    counts: Counter = Counter()
    samples, adopted_samples = set(), set()
    for row in rows:
        if raw:
            sample = ast.first_value(row, ast.BIOSAMPLE_ALIASES)
            project = ast.first_value(row, ast.BIOPROJECT_ALIASES)
            mapping = mappings.get(ast.normalize(ast.first_value(row, ast.ANTIBIOTIC_ALIASES)), {})
            identifier = mapping.get("identifier", "")
            count = 1
        else:
            sample, project, identifier = (
                row["biosample_accession"], row["bioproject_accession"], row["identifier"],
            )
            count = int(row["ast_row_count"])
        counts["groups_or_rows"] += 1
        counts["measurements"] += count
        if sample in membership["all_samples"]:
            counts["shared_wgs_sample_measurements"] += count
            samples.add(sample)
        if sample in membership["drugs_by_sample"]:
            counts["shared_adopted_sample_measurements"] += count
            adopted_samples.add(sample)
            if identifier in membership["drugs_by_sample"][sample]:
                counts["shared_adopted_sample_and_drug_measurements"] += count
        if project in membership["projects"]:
            counts["shared_adopted_project_measurements"] += count
    return {
        key: counts[key] for key in (
            "groups_or_rows", "measurements", "shared_wgs_sample_measurements",
            "shared_adopted_sample_measurements", "shared_adopted_sample_and_drug_measurements",
            "shared_adopted_project_measurements",
        )
    } | {"shared_wgs_biosamples": sorted(samples), "shared_adopted_biosamples": sorted(adopted_samples)}


def assay_contexts(rows: list[dict]) -> list[dict]:
    counts: Counter = Counter()
    for row in rows:
        kind = "+".join(name for name, field in (
            ("MIC", "mic_value"), ("DISK", "disk_diffusion_value"),
        ) if row[field])
        counts[(row["method"], row["platform"], row["reagent"], kind)] += int(row["ast_row_count"])
    return [
        dict(zip(("method", "platform", "reagent", "measurement"), key, strict=True), count=count)
        for key, count in sorted(counts.items())
    ]


def audit(args) -> dict:
    import duckdb

    release = args.cryptic_directory
    dst, ukmyc, codes = [release / name for name in (
        "DST_MEASUREMENTS.parquet", "UKMYC_PHENOTYPES.parquet", "DRUG_CODES.csv.gz",
    )]
    for path in (dst, ukmyc, codes, args.wgs):
        cryptic.verify_release_file(path)
    drug_codes = cryptic.read_drug_codes(codes)
    cryptic_mappings = cryptic.validated_drug_mappings(args.cryptic_drug_map, drug_codes)
    adopted = load_cryptic_activity_inventory(args.cryptic_inventory)
    with duckdb.connect() as connection:
        rebuilt = cryptic.activity_inventory(connection, dst, ukmyc, drug_codes, cryptic_mappings)
        require_same_inventory(adopted, rebuilt)
        membership = cryptic_membership(connection, dst, ukmyc, args.wgs, cryptic_mappings)

    version = "ast-browser-sha256:" + file_sha256(args.ast)
    _, structure_keys = ast.corpus_name_candidates()
    mappings = ast.read_drug_map(args.drug_map, structure_keys, version)
    report = ast.read_activity_report(args.activity_report, structure_keys, version)
    if not report:
        raise ValueError("empty AST candidate report cannot establish overlap coverage")
    raw = ast.read_table(args.ast)
    snapshot = load_isolate_snapshot(args.isolate_snapshot)
    enriched = ast.enrich_isolate_identity(raw, snapshot)
    dedupe = ast.read_project_dedupe_map(args.project_dedupe_map) if args.project_dedupe_map else {}
    current = ast.exact_activity_rows(
        enriched, mappings, source_version=version,
        source_retrieved_on=report[0]["source_retrieved_on"], isolate_snapshot=snapshot,
        project_dedupe=dedupe,
    )
    if args.assay_review:
        current, _ = apply_assay_review(current, read_assay_review(args.assay_review))
    ast.require_activity_report_matches_current(report, current, args.activity_report)
    input_paths = {
        "ast": args.ast, "activity_report": args.activity_report, "drug_map": args.drug_map,
        "isolates": args.isolate_snapshot / "isolates.json",
        "isolate_manifest": args.isolate_snapshot / "snapshot.json",
        "cryptic_inventory": args.cryptic_inventory, "cryptic_drug_map": args.cryptic_drug_map,
        "cryptic_dst": dst, "cryptic_ukmyc": ukmyc, "cryptic_drug_codes": codes, "cryptic_wgs": args.wgs,
    }
    if args.project_dedupe_map:
        input_paths["project_dedupe_map"] = args.project_dedupe_map
    if args.assay_review:
        input_paths["assay_review"] = args.assay_review
    return {
        "scope": "Exact accession overlap; review leads only, not automatic duplicate exclusions.",
        "limitations": [
            "Different BioSample accessions may identify the same isolate; aliases are unresolved.",
            "Phenotype-only CRyPTIC samples without a WGS accession link cannot be accession-matched.",
            "A shared sample/drug does not prove duplicate measurements or justify project-wide exclusion.",
            "Assay signatures retain submitted values; informative text does not certify field consistency.",
        ],
        "source_version": version, "cryptic_version": cryptic.VERSION,
        "inputs": {key: {"path": str(path), "sha256": file_sha256(path)}
                   for key, path in input_paths.items()},
        "cryptic_membership": membership["counts"],
        "raw_ast": overlap_summary(raw, membership, raw=True, mappings=mappings),
        "eligible_ast": overlap_summary(report, membership, raw=False, mappings=mappings),
        "eligible_assay_contexts": assay_contexts(report),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("ast", "activity-report", "isolate-snapshot", "wgs", "report"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--drug-map", type=Path, default=ROOT / "curation/ncbi_ast_drug_map.tsv")
    parser.add_argument("--project-dedupe-map", type=Path)
    parser.add_argument("--assay-review", type=Path)
    parser.add_argument("--cryptic-directory", type=Path, default=ROOT / "downloads/cryptic_3.4.0")
    parser.add_argument("--cryptic-drug-map", type=Path, default=cryptic.DEFAULT_DRUG_MAP)
    parser.add_argument("--cryptic-inventory", type=Path, default=ROOT / "data/raw/cryptic_activity.tsv")
    args = parser.parse_args()
    if args.report.exists():
        parser.error(f"refusing to overwrite {args.report}")
    result = audit(args)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"Overlap audit: {args.report}")
    for section in ("cryptic_membership", "raw_ast", "eligible_ast"):
        print(section, {key: len(value) if isinstance(value, list) else value
                        for key, value in result[section].items()})


if __name__ == "__main__":
    main()

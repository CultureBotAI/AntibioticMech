#!/usr/bin/env python3
"""Rebuild BioSample adjudication and validate every resulting activity observation."""

import argparse
import hashlib
import json
from pathlib import Path

from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from ncbi_ast_assays import DEFAULT_REVIEW_MAP, read_assay_review
from ncbi_ast_biosamples import (
    DEFAULT_REVIEW,
    ENDPOINT,
    activity_observations,
    build_review,
    read_biosamples,
    read_review,
    repeated_target_groups,
)
from ncbi_ast_isolates import file_sha256, require_iso_date
from seed_from_sources import load_ncbi_ast_activity_inventory, ncbi_ast_activity_observation

ROOT = Path(__file__).resolve().parents[1]
GENOME_FIELDS = (
    "bioproject_accession",
    "pathogen_detection_target_accession",
    "assembly_accession",
    "sra_accessions",
    "source_create_date",
)


def verify_source_review(directory: Path, inventory: Path, rows: list[dict], review_path: Path) -> dict:
    groups = repeated_target_groups(rows)
    review, _ = read_review(review_path, inventory, groups)
    metadata = json.loads((directory / "snapshot.json").read_text())
    payload = (directory / "biosamples.xml").read_bytes()
    requested = sorted({group[0]["biosample_accession"] for group in groups})
    if (
        metadata.get("source") != "NCBI_BIOSAMPLE_EFETCH"
        or metadata.get("endpoint") != ENDPOINT
        or metadata.get("file") != "biosamples.xml"
        or metadata.get("requested_accessions") != requested
        or metadata.get("sha256") != hashlib.sha256(payload).hexdigest()
        or metadata.get("bytes") != len(payload)
        or metadata.get("activity_report_sha256") != file_sha256(inventory)
    ):
        raise ValueError("BioSample snapshot manifest does not match captured evidence")
    require_iso_date(metadata.get("source_retrieved_on"), "BioSample snapshot")
    rebuilt = build_review(groups, read_biosamples(payload, requested), metadata)
    if rebuilt != review:
        raise ValueError("curated BioSample review differs from reconstructed source decisions")
    return review


def audit(args) -> dict:
    rows = load_ncbi_ast_activity_inventory(args.activity_report)
    review = verify_source_review(args.biosample_snapshot, args.activity_report, rows, args.biosample_review)
    assays = read_assay_review(args.assay_review)
    validator = Validator(
        schema=str(ROOT / "src/antibioticmech/schema/antibioticmech.yaml"),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )
    originals = {row["activity_group_id"]: row for row in rows}
    covered, ids, samples, assemblies = set(), set(), set(), set()
    counts = {
        "source_groups": len(rows),
        "observations": 0,
        "measurements": 0,
        "collapsed_results": 0,
        "genome_contexts": 0,
    }

    def convert(row):
        return ncbi_ast_activity_observation(row, assays)

    for identifier, observation in activity_observations(
        rows, args.activity_report, convert, args.biosample_review
    ):
        errors = list(validator.iter_results(observation, target_class="ActivityObservation"))
        if errors:
            raise ValueError(f"invalid observation {observation['source_observation_id']}: {errors}")
        observation_id = observation["source_observation_id"]
        if observation_id in ids:
            raise ValueError("duplicate collapsed observation identifier")
        ids.add(observation_id)
        contexts = observation.get("pathogen_detection_contexts", [])
        represented = [c["source_observation_id"] for c in contexts] if contexts else [observation_id]
        for original_id in represented:
            if original_id in covered or original_id not in originals:
                raise ValueError("source row duplicated or invented during consolidation")
            covered.add(original_id)
            if originals[original_id]["identifier"] != identifier:
                raise ValueError("consolidation changed the exact compound identifier")
        if not contexts:
            if observation != convert(originals[observation_id]):
                raise ValueError("unrepeated observation was changed")
        else:
            counts["collapsed_results"] += 1
            counts["genome_contexts"] += len(contexts)
            samples.add(observation["biosample_accession"])
            if observation["measurement_count"] != 1 or observation["source_export_row_count"] != len(
                contexts
            ):
                raise ValueError("genome fan-out was counted as assay replication")
            evidence = [json.dumps(e, sort_keys=True) for e in observation["evidence"]]
            for context in contexts:
                expected = convert(originals[context["source_observation_id"]])
                paired = {k: expected[k] for k in (*GENOME_FIELDS, "source_observation_id") if k in expected}
                if context != paired or any(k in observation for k in GENOME_FIELDS):
                    raise ValueError("genome context changed, crossed, or selected as representative")
                if context.get("assembly_accession"):
                    assemblies.add(context["assembly_accession"])
                for key in set(expected) - {
                    *GENOME_FIELDS,
                    "source_observation_id",
                    "evidence",
                    "measurement_count",
                }:
                    if observation.get(key) != expected[key]:
                        raise ValueError(f"consolidation changed source claim: {key}")
                if any(json.dumps(e, sort_keys=True) not in evidence for e in expected["evidence"]):
                    raise ValueError("original source evidence was lost")
        counts["observations"] += 1
        counts["measurements"] += observation["measurement_count"]
        if counts["observations"] % 50000 == 0:
            print(f"Validated {counts['observations']} observations", flush=True)
    if covered != set(originals):
        raise ValueError("original source rows were lost")
    paths = {
        "activity_report": args.activity_report,
        "biosample_review": args.biosample_review,
        "assay_review": args.assay_review,
        "biosamples": args.biosample_snapshot / "biosamples.xml",
        "biosample_manifest": args.biosample_snapshot / "snapshot.json",
    }
    return {
        "source_version": review["source_version"],
        "counts": counts,
        "collapsed_biosamples": sorted(samples),
        "collapsed_assemblies": sorted(assemblies),
        "original_groups_accounted_for": len(covered),
        "inputs": {key: {"path": str(path), "sha256": file_sha256(path)} for key, path in paths.items()},
        "scope": "Source-verified export fan-out only; "
        "no independent phenotype verification or source adoption.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("activity-report", "biosample-snapshot", "report"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--biosample-review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--assay-review", type=Path, default=DEFAULT_REVIEW_MAP)
    args = parser.parse_args()
    if args.report.exists():
        parser.error(f"refusing to overwrite {args.report}")
    result = audit(args)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result["counts"], indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Apply source-pinned assay-context decisions without changing retained measurements."""

import argparse
import json
from pathlib import Path

from evaluate_ncbi_ast import corpus_name_candidates, read_activity_report, write_activity_report
from ncbi_ast_assays import DEFAULT_REVIEW_MAP, apply_assay_review, read_assay_review
from ncbi_ast_isolates import file_sha256


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activity-report", type=Path, required=True)
    parser.add_argument("--assay-review", type=Path, default=DEFAULT_REVIEW_MAP)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    if args.output_directory.exists():
        parser.error(f"refusing to overwrite {args.output_directory}")
    review = read_assay_review(args.assay_review)
    if file_sha256(args.activity_report) != review.candidate_sha256:
        parser.error("candidate report checksum does not match the reviewed snapshot")
    _, keys = corpus_name_candidates()
    rows = read_activity_report(args.activity_report, keys, review.source_version)
    accepted, decisions = apply_assay_review(rows, review)
    if not accepted:
        parser.error("assay review admits no observations")
    args.output_directory.mkdir(parents=True)
    output = args.output_directory / "activity.tsv"
    write_activity_report(accepted, output)
    summary = {
        "source_version": review.source_version, "assay_review_version": review.version,
        "assay_reviewed_on": review.reviewed_on, "candidate_sha256": review.candidate_sha256,
        "output_sha256": file_sha256(output), "input_groups": len(rows),
        "accepted_groups": len(accepted), "quarantined_groups": len(rows) - len(accepted),
        "decisions": decisions,
    }
    (args.output_directory / "review.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

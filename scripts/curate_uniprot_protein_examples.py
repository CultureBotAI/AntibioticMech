#!/usr/bin/env python3
"""Apply or dry-run curated UniProt protein examples on causal graphs and molecular targets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from antibioticmech.uniprot_examples import (  # noqa: E402
    DEFAULT_PLAN_PATH,
    DEFAULT_RECEIPT_PATH,
    apply_uniprot_examples_plan,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root containing data/antibiotics/.",
    )
    parser.add_argument(
        "--plan",
        type=Path,
        default=DEFAULT_PLAN_PATH,
        help="Path to curation/uniprot_protein_examples.yaml.",
    )
    parser.add_argument(
        "--receipt",
        type=Path,
        default=DEFAULT_RECEIPT_PATH,
        help="Path to write transition receipt JSON when applying the full plan.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Restrict to one or more antibiotic identifiers (repeatable or comma-separated).",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report planned UniProt protein example changes without writing files (default).",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Write validated changes and append curation_history events.",
    )
    parser.add_argument(
        "--curator",
        default="antigravity",
        help="Curator name for curation_history entries.",
    )
    parser.add_argument(
        "--timestamp",
        default=None,
        help="Optional ISO-8601 UTC timestamp override for deterministic replay.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    only_ids: set[str] | None = None
    if args.only:
        only_ids = {
            token.strip()
            for raw in args.only
            for token in raw.split(",")
            if token.strip()
        }
    results = apply_uniprot_examples_plan(
        root=args.root.resolve(),
        plan_path=args.plan.resolve(),
        only_identifiers=only_ids,
        apply=bool(args.apply),
        receipt_path=args.receipt.resolve() if args.receipt else None,
        curator=args.curator,
        timestamp=args.timestamp,
        llm_assisted=True,
    )
    mode_label = "APPLIED" if args.apply else "DRY-RUN"
    changed_count = sum(1 for r in results if r.changed)
    total_nodes = sum(r.causal_nodes_updated for r in results)
    total_targets = sum(r.molecular_targets_updated for r in results)
    total_examples = sum(r.protein_examples_added for r in results)
    for res in results:
        status = "CHANGED" if res.changed else "UNCHANGED"
        print(
            f"[{mode_label}:{status}] {res.identifier} ({res.label}) -> "
            f"causal_nodes={res.causal_nodes_updated}, "
            f"molecular_targets={res.molecular_targets_updated}, "
            f"protein_examples={res.protein_examples_added}"
        )
    print(
        f"Summary ({mode_label}): {changed_count}/{len(results)} record(s) changed; "
        f"{total_nodes} causal node(s), {total_targets} molecular target(s), "
        f"{total_examples} protein example(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

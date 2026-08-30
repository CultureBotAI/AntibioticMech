#!/usr/bin/env python3
"""Keep README.md's generated statistics block in step with the corpus.

A README that claims 2,603 records when the corpus holds 2,100 is worse than
one that claims nothing: a reader has no way to tell which number is stale. The
block between the marker comments is generated from the records on disk.

    python scripts/check_docs.py --write   # regenerate the block
    python scripts/check_docs.py --check   # fail if it is out of step
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
README = REPO_ROOT / "README.md"

START = "<!-- BEGIN GENERATED CORPUS STATS -->"
END = "<!-- END GENERATED CORPUS STATS -->"

CLASS_ORDER = ["ANTIBACTERIAL", "ANTIMYCOBACTERIAL", "ANTIFUNGAL", "ANTIPROTOZOAL",
               "ANTIVIRAL", "BIOCIDE", "ANTIMICROBIAL_UNSPECIFIED", "OTHER"]


def corpus_stats() -> dict:
    by_class: Counter = Counter()
    status_by_class: dict[str, Counter] = {}
    grounding: Counter = Counter()
    sources: Counter = Counter()
    mechanism: Counter = Counter()
    card_evidence_by_class: Counter = Counter()

    total = 0
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        total += 1
        cls = record["antimicrobial_class"]
        by_class[cls] += 1
        status_by_class.setdefault(cls, Counter())[record["curation_status"]] += 1
        grounding[record.get("grounding_status", "?")] += 1
        combo = "+".join(sorted({c["source"] for c in record.get("source_concepts", [])}))
        sources[combo] += 1
        for field in ("molecular_targets", "resistance_mechanisms", "causal_graphs",
                      "mode_of_action", "activity_spectrum"):
            if record.get(field):
                mechanism[field] += 1
        if record.get("molecular_targets") or record.get("resistance_mechanisms"):
            card_evidence_by_class[cls] += 1
    return {"total": total, "by_class": by_class, "status_by_class": status_by_class,
            "grounding": grounding, "sources": sources, "mechanism": mechanism,
            "card_evidence_by_class": card_evidence_by_class}


def render_block(stats: dict) -> str:
    total = stats["total"]
    lines = [START, ""]
    lines.append("| Class | Records | SEEDED | REVIEWED | With CARD mechanism evidence |")
    lines.append("|---|---:|---:|---:|---:|")
    for cls in CLASS_ORDER:
        count = stats["by_class"].get(cls, 0)
        if not count:
            continue
        per = stats["status_by_class"].get(cls, Counter())
        lines.append(f"| {cls} | {count} | {per['SEEDED']} | {per['REVIEWED']} | "
                     f"{stats['card_evidence_by_class'].get(cls, 0)} |")
    lines.append(f"| **TOTAL** | **{total}** | "
                 f"**{sum(c['SEEDED'] for c in stats['status_by_class'].values())}** | "
                 f"**{sum(c['REVIEWED'] for c in stats['status_by_class'].values())}** | "
                 f"**{sum(stats['card_evidence_by_class'].values())}** |")
    lines.append("")
    exact = stats["grounding"].get("EXACT", 0)
    minted = stats["grounding"].get("MINTED", 0)
    both = stats["sources"].get("ARO+CHEBI", 0)
    lines.append(f"Identity: **{exact}** records ({exact / total:.0%}) are grounded in a ChEBI "
                 f"term; **{minted}** keep a minted `antibioticmech:` CURIE because no ChEBI "
                 f"entry with a structure covers them.")
    lines.append("")
    lines.append(f"Corroboration: **{both}** records carry source concepts from both ChEBI and "
                 f"CARD/ARO; **{stats['sources'].get('CHEBI', 0)}** come from ChEBI alone and "
                 f"**{stats['sources'].get('ARO', 0)}** from CARD alone.")
    lines.append("")
    targets = stats["mechanism"].get("molecular_targets", 0)
    resistance = stats["mechanism"].get("resistance_mechanisms", 0)
    graphs = stats["mechanism"].get("causal_graphs", 0)
    lines.append(f"Mechanism layer: **{targets}** records carry a molecular target and "
                 f"**{resistance}** carry resistance determinants, both seeded from CARD; "
                 f"**{graphs}** carry a curated causal graph. That last number is the work.")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not CORPUS_DIR.exists():
        print("no corpus; run `just seed-apply`", file=sys.stderr)
        return 1

    block = render_block(corpus_stats())
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        print(f"README.md has no generated block; add the {START} / {END} markers",
              file=sys.stderr)
        return 1
    updated = pattern.sub(lambda _: block, text)

    if args.check:
        if updated != text:
            print("README.md's generated corpus statistics are out of step with the corpus.\n"
                  "Run `just docs-stats` and commit the result.", file=sys.stderr)
            return 1
        print("README statistics are current.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print("README statistics refreshed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

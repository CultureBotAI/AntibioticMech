#!/usr/bin/env python3
"""The curation backlog, ranked so a curator can start at the top.

Three queues, each answering a different question:

  no-structure  Source concepts that never became records because no source
                gives them a structure. Each needs a structure or an EXCLUDE
                decision in curation/decisions.tsv.
  mechanism     Seeded records with no molecular target, mode of action, or
                causal graph — the mechanism layer this repository exists for.
  minted        Records whose identity is a minted CURIE. Each needs either a
                defensible ontology identity or a recorded reason it has none.

    python scripts/curation_worklist.py                 # all three, top 25 each
    python scripts/curation_worklist.py --queue minted --limit 100
    python scripts/curation_worklist.py --tsv reports/worklist.tsv

Suggestions are a starting point, never an answer: anything written into
curation/decisions.tsv is re-checked against the inventories at seed time.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from seed_from_sources import (  # noqa: E402
    CONF_PATH,
    RAW_DIR,
    build_concepts,
    load_decisions,
    merge,
)

CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"


def no_structure_queue() -> list[dict]:
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    manifest = yaml.safe_load((RAW_DIR / "MANIFEST.yaml").read_text(encoding="utf-8"))
    concepts, chebi_rows = build_concepts(conf)
    _, skipped = merge(concepts, chebi_rows, conf, load_decisions(),
                       manifest.get("retrieved_on", ""))
    rows = []
    for concept in skipped:
        has_pubchem = any(x.startswith("pubchem.compound:") for x in concept.xrefs)
        rows.append({
            "queue": "no-structure",
            "key": concept.minted,
            "label": concept.label,
            "source": concept.source,
            "source_id": concept.source_id,
            "hint": "PubChem CID available — extend the enrichment" if has_pubchem
                    else "no structure in any source; likely a class, mixture, or preparation",
        })
    # A concept ChEBI itself files as a class is the least interesting: sort those last.
    rows.sort(key=lambda r: (r["hint"].startswith("no structure"), r["source"], r["label"].lower()))
    return rows


def corpus_records() -> list[dict]:
    return [yaml.safe_load(p.read_text(encoding="utf-8")) for p in sorted(CORPUS_DIR.rglob("*.yaml"))]


def mechanism_queue(records: list[dict]) -> list[dict]:
    rows = []
    for record in records:
        if record.get("causal_graphs") or record.get("mode_of_action"):
            continue
        targets = len(record.get("molecular_targets") or [])
        resistance = len(record.get("resistance_mechanisms") or [])
        rows.append({
            "queue": "mechanism",
            "key": record["identifier"],
            "label": record["label"],
            "source": "+".join(sorted({c["source"] for c in record.get("source_concepts", [])})),
            "source_id": record.get("structural_class", ""),
            "hint": f"{targets} CARD target(s), {resistance} resistance edge(s) to build on",
        })
    # Most CARD evidence first: those are the records a curator can finish today.
    rows.sort(key=lambda r: (-int(r["hint"].split()[0]), -int(r["hint"].split(",")[1].split()[0]),
                             r["label"].lower()))
    return rows


def minted_queue(records: list[dict]) -> list[dict]:
    rows = []
    for record in records:
        if record.get("grounding_status") != "MINTED":
            continue
        rows.append({
            "queue": "minted",
            "key": record["identifier"],
            "label": record["label"],
            "source": "+".join(sorted({c["source"] for c in record.get("source_concepts", [])})),
            "source_id": ",".join(c["source_id"] for c in record.get("source_concepts", [])),
            "hint": "no ChEBI cross-reference with a structure; needs a ChEBI id or a reason",
        })
    rows.sort(key=lambda r: r["label"].lower())
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queue", choices=("all", "no-structure", "mechanism", "minted"),
                        default="all")
    parser.add_argument("--limit", type=int, default=25, help="Rows printed per queue.")
    parser.add_argument("--tsv", type=Path, help="Write every row (not just --limit) to this TSV.")
    args = parser.parse_args()

    records = corpus_records()
    queues = {}
    if args.queue in ("all", "no-structure"):
        queues["no-structure"] = no_structure_queue()
    if args.queue in ("all", "mechanism"):
        queues["mechanism"] = mechanism_queue(records)
    if args.queue in ("all", "minted"):
        queues["minted"] = minted_queue(records)

    for name, rows in queues.items():
        print(f"\n=== {name}: {len(rows)} item(s) ===")
        for row in rows[: args.limit]:
            print(f"  {row['label'][:44]:44s} {row['key'][:34]:34s} {row['hint']}")
        if len(rows) > args.limit:
            print(f"  ... {len(rows) - args.limit} more (use --limit or --tsv)")

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=["queue", "key", "label", "source",
                                                    "source_id", "hint"],
                                    delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for rows in queues.values():
                writer.writerows(rows)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

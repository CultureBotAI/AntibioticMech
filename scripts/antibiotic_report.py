#!/usr/bin/env python3
"""Corpus report: what AntibioticMech currently holds and what curation owes it.

    python scripts/antibiotic_report.py            # human-readable summary
    python scripts/antibiotic_report.py --tsv reports/corpus.tsv

Counts come from the records on disk, never from the inventories, so the report
describes the corpus a consumer would actually download.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"


def load_corpus() -> list[tuple[Path, dict]]:
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        out.append((path, yaml.safe_load(path.read_text(encoding="utf-8"))))
    return out


def summarize(records: list[tuple[Path, dict]]) -> dict:
    by_class = Counter()
    by_status = Counter()
    by_grounding = Counter()
    sources = Counter()
    source_combo = Counter()
    structure_fields = Counter()
    mechanism = Counter()
    class_status: dict[str, Counter] = defaultdict(Counter)

    for _, record in records:
        cls = record.get("antimicrobial_class", "?")
        by_class[cls] += 1
        by_status[record.get("curation_status", "?")] += 1
        class_status[cls][record.get("curation_status", "?")] += 1
        by_grounding[record.get("grounding_status", "?")] += 1
        concept_sources = sorted({c["source"] for c in record.get("source_concepts", [])})
        for source in concept_sources:
            sources[source] += 1
        source_combo["+".join(concept_sources) or "none"] += 1
        structure = record.get("chemical_structure", {}) or {}
        for field in ("standard_inchi_key", "smiles", "standard_inchi", "molecular_formula",
                      "monoisotopic_mass"):
            if structure.get(field):
                structure_fields[field] += 1
        if record.get("molecular_targets"):
            mechanism["molecular_targets"] += 1
        if record.get("resistance_mechanisms"):
            mechanism["resistance_mechanisms"] += 1
        if record.get("causal_graphs"):
            mechanism["causal_graphs"] += 1
        if record.get("mode_of_action"):
            mechanism["mode_of_action"] += 1
        if record.get("activity_spectrum"):
            mechanism["activity_spectrum"] += 1
        if record.get("producer_organisms"):
            mechanism["producer_organisms"] += 1

    return {
        "total": len(records),
        "by_class": by_class,
        "by_status": by_status,
        "by_grounding": by_grounding,
        "sources": sources,
        "source_combo": source_combo,
        "structure_fields": structure_fields,
        "mechanism": mechanism,
        "class_status": class_status,
    }


def print_report(stats: dict) -> None:
    total = stats["total"]
    print(f"AntibioticMech corpus: {total} records\n")

    print("Records per antimicrobial class")
    for name, count in stats["by_class"].most_common():
        statuses = ", ".join(f"{k} {v}" for k, v in sorted(stats["class_status"][name].items()))
        print(f"  {name:26s} {count:>6d}   ({statuses})")

    print("\nCuration status")
    for name, count in stats["by_status"].most_common():
        print(f"  {name:26s} {count:>6d}   {count / total:6.1%}")

    print("\nIdentity grounding")
    for name, count in stats["by_grounding"].most_common():
        print(f"  {name:26s} {count:>6d}   {count / total:6.1%}")

    print("\nSource coverage (a record may carry several source concepts)")
    for name, count in stats["sources"].most_common():
        print(f"  {name:26s} {count:>6d}")
    print("  --- corroboration ---")
    for name, count in stats["source_combo"].most_common():
        print(f"  {name:26s} {count:>6d}")

    print("\nStructure completeness")
    for field in ("standard_inchi_key", "smiles", "standard_inchi", "molecular_formula",
                  "monoisotopic_mass"):
        count = stats["structure_fields"][field]
        print(f"  {field:26s} {count:>6d}   {count / total:6.1%}")

    print("\nMechanism layer — what curation still owes")
    for field in ("molecular_targets", "resistance_mechanisms", "mode_of_action",
                  "causal_graphs", "activity_spectrum", "producer_organisms"):
        count = stats["mechanism"][field]
        print(f"  {field:26s} {count:>6d}   {count / total:6.1%}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tsv", type=Path, help="Also write per-class counts to this TSV.")
    args = parser.parse_args()

    records = load_corpus()
    if not records:
        print("no records yet; run `just seed-apply`")
        return 0
    stats = summarize(records)
    print_report(stats)

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
            writer.writerow(["antimicrobial_class", "records", "seeded", "reviewed", "deprecated"])
            for name, count in sorted(stats["by_class"].items()):
                per = stats["class_status"][name]
                writer.writerow([name, count, per["SEEDED"], per["REVIEWED"], per["DEPRECATED"]])
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

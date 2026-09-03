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
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"

sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from curation_worklist import (  # noqa: E402
    activity_candidate_queue,
    producer_candidate_queue,
)
from seed_from_sources import class_count_rows, class_parents, rollup_by_class  # noqa: E402


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
    structures = Counter()
    organismal = Counter()
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
        for item in record.get("structural_observations") or []:
            structures["total"] += 1
            if item.get("relevance") not in (None, "UNREVIEWED"):
                structures["reviewed"] += 1
            if item.get("relevance") == "TARGET_COMPLEX":
                structures["target_complexes"] += 1
        if record.get("structural_observations"):
            mechanism["structural_observations"] += 1
        for item in record.get("resistance_mechanisms") or []:
            organismal["resistance_items"] += 1
            if item.get("taxon_label"):
                organismal["resistance_with_organism"] += 1

    # An empty axis is two different situations, and reporting one number for
    # both overstates what curation can act on. A synthetic sulfonamide has no
    # producer organism to find; a natural product whose definition says
    # "produced by Streptomyces rochei" has one sitting in plain text. Counting
    # the candidate queues separates the backlog from the genuinely absent.
    docs = [record for _, record in records]
    organismal["producer_candidates"] = len(producer_candidate_queue(docs))
    organismal["activity_candidates"] = len(activity_candidate_queue(docs))

    return {
        "organismal": organismal,
        "structures": structures,
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

    # Inclusive of subclasses. Filing is exclusive — an antimycobacterial record
    # is not also under ANTIBACTERIAL — so a flat listing answered "which
    # compounds act on bacteria?" with 1037 when the true figure is 1115. The
    # hierarchy is declared in the schema; this makes it govern the count.
    parents = class_parents()
    inclusive = rollup_by_class(dict(stats["by_class"]))
    children: dict[str, list[str]] = {}
    for child, parent in parents.items():
        children.setdefault(parent, []).append(child)

    print("Records per antimicrobial class")
    # Iterate the classes that have records PLUS their ancestors. A parent with
    # no records of its own was absent from by_class, so its child was skipped
    # as "printed under its parent" and the parent never printed — the records
    # disappeared from the listing altogether.
    listed = set(stats["by_class"])
    for cls in list(listed):
        parent = parents.get(cls)
        while parent:
            listed.add(parent)
            parent = parents.get(parent)
    order = sorted(listed, key=lambda c: (-inclusive.get(c, 0), c))
    for name in order:
        if name in parents:            # printed under its parent
            continue
        kids = [k for k in children.get(name, []) if stats["by_class"].get(k)]
        statuses = ", ".join(f"{k} {v}" for k, v in sorted(stats["class_status"][name].items())) \
            or "none filed directly"
        if kids:
            print(f"  {name:26s} {inclusive[name]:>6d}   (incl. subclasses)")
            for kid in sorted(kids, key=lambda k: -stats["by_class"][k]):
                print(f"    └ {kid:24s}{stats['by_class'][kid]:>5d}")
            print(f"    {'(directly filed)':24s}  {stats['by_class'][name]:>5d}   ({statuses})")
        else:
            print(f"  {name:26s} {stats['by_class'][name]:>6d}   ({statuses})")

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
                  "causal_graphs", "activity_spectrum", "producer_organisms",
                  "structural_observations"):
        count = stats["mechanism"][field]
        print(f"  {field:26s} {count:>6d}   {count / total:6.1%}")

    # A structure is only mechanistic evidence once someone says what the
    # macromolecule is; counting accessions alone would overstate the axis.
    structures = stats["structures"]
    if structures["total"]:
        print(f"    of {structures['total']} structure(s): "
              f"{structures['reviewed']} reviewed, "
              f"{structures['target_complexes']} established as target complexes")

    # #94: separate "nothing to find" from "found nothing yet".
    organismal = stats["organismal"]
    print("\nOrganismal axis — populated, candidate, or no signal")
    for field, candidates in (("producer_organisms", organismal["producer_candidates"]),
                              ("activity_spectrum", organismal["activity_candidates"])):
        populated = stats["mechanism"][field]
        silent = total - populated - candidates
        print(f"  {field:26s} {populated:>6d} populated   "
              f"{candidates:>5d} with a definition signal   {silent:>5d} with none")
    items = organismal["resistance_items"]
    if items:
        named = organismal["resistance_with_organism"]
        print(f"  {'resistance in an organism':26s} {named:>6d} of {items} resistance item(s) "
              f"name the organism the resistance was observed in")


def write_class_tsv(stats: dict, path: Path) -> None:
    """Write hierarchy-aware direct and inclusive class/status counts."""

    status_names = ("SEEDED", "REVIEWED", "DEPRECATED")
    inclusive_status = {
        status: rollup_by_class(
            {
                name: stats["class_status"][name][status]
                for name in stats["by_class"]
            }
        )
        for status in status_names
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        header = [
            "antimicrobial_class",
            "parent_class",
            "records_direct",
            "records_including_subclasses",
        ]
        for status in status_names:
            header.extend(
                (f"{status.lower()}_direct", f"{status.lower()}_including_subclasses")
            )
        writer.writerow(header)
        for row in class_count_rows(dict(stats["by_class"])):
            name = str(row["antimicrobial_class"])
            values: list[str | int] = [
                name,
                row["parent_class"],
                row["records_direct"],
                row["records_including_subclasses"],
            ]
            for status in status_names:
                values.extend(
                    (
                        stats["class_status"][name][status],
                        inclusive_status[status].get(name, 0),
                    )
                )
            writer.writerow(values)


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
        write_class_tsv(stats, args.tsv)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

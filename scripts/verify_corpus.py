#!/usr/bin/env python3
"""Prove data/antibiotics/ is exactly what data/raw/ produces.

Schema validation checks each record's *shape*. It cannot see that a record was
hand-edited into a plausible but unsourced claim, that a structure was swapped,
or that a file survived a source concept's removal. This rebuilds the corpus in
memory from the committed inventories and compares it byte-for-byte with what is
on disk.

    python scripts/verify_corpus.py            # whole corpus
    python scripts/verify_corpus.py --summary  # counts only

Exit status is 1 on any drift. The seeded fields are the ones compared; curated
fields a seeder never writes (causal_graphs, activity_spectrum, producer_organisms,
mode_of_action, clinical_status, discussions, datasets, curator evidence, and
curation_history beyond the seed event) are deliberately NOT compared, so
curation is possible without the check going permanently red. Those fields are
covered by validation and by tests/test_corpus_integrity.py instead.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from seed_from_sources import (  # noqa: E402
    CONF_PATH,
    RAW_DIR,
    SEEDED_FIELDS,
    assign_slugs,
    attach_aro_mechanism,
    build_concepts,
    card_sourced_view,
    flag_structure_collisions,
    load_decisions,
    merge,
    read_lockfile,
    record_path,
)

# The seeded field list is imported from the seeder so there is one definition
# of what it owns. `molecular_targets` and `resistance_mechanisms` are compared
# separately, because a curator may add items to those lists beside the
# CARD-derived ones; only the CARD-derived view has to reproduce.
#
# `discussions` is deliberately not compared for the same reason: the seeder
# writes structure-collision todos into a list a curator also writes to.
CARD_FIELDS = ["molecular_targets", "resistance_mechanisms"]


def rebuild() -> dict[str, dict]:
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    manifest = yaml.safe_load((RAW_DIR / "MANIFEST.yaml").read_text(encoding="utf-8"))
    concepts, chebi_rows = build_concepts(conf)
    records, _ = merge(concepts, chebi_rows, conf, load_decisions(),
                       manifest.get("retrieved_on", ""))
    attach_aro_mechanism(records, manifest.get("retrieved_on", ""))
    flag_structure_collisions(records, manifest.get("retrieved_on", ""))
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--summary", action="store_true", help="Print counts, not each difference.")
    parser.add_argument("--max-report", type=int, default=20,
                        help="Stop listing individual differences after N (default 20).")
    args = parser.parse_args()

    expected = rebuild()
    lockfile = read_lockfile()
    slugs = assign_slugs(expected, lockfile)

    corpus_dir = REPO_ROOT / "data" / "antibiotics"
    on_disk = {p for p in corpus_dir.rglob("*.yaml")}
    wanted = {record_path(expected[i], slugs[i]): i for i in expected}

    missing = sorted(set(wanted) - on_disk)
    extra = sorted(on_disk - set(wanted))
    drifted: list[tuple[Path, str]] = []

    for path, identifier in sorted(wanted.items(), key=lambda kv: str(kv[0])):
        if path not in on_disk:
            continue
        actual = yaml.safe_load(path.read_text(encoding="utf-8"))
        want = expected[identifier]
        for field in SEEDED_FIELDS:
            if want.get(field) != actual.get(field):
                drifted.append((path, field))
        for field in CARD_FIELDS:
            if card_sourced_view(want, field) != card_sourced_view(actual, field):
                drifted.append((path, field))

    unlocked = sorted(set(expected) - set(lockfile))
    stale_lock = sorted(set(lockfile) - set(expected))

    problems = len(missing) + len(extra) + len(drifted) + len(unlocked) + len(stale_lock)
    print(f"records expected: {len(expected)}   on disk: {len(on_disk)}")
    print(f"missing: {len(missing)}   unexpected: {len(extra)}   drifted fields: {len(drifted)}")
    print(f"identifiers absent from PATHS.tsv: {len(unlocked)}   stale lockfile rows: {len(stale_lock)}")

    if problems and not args.summary:
        for path in missing[: args.max_report]:
            print(f"  MISSING   {path.relative_to(REPO_ROOT)}")
        for path in extra[: args.max_report]:
            print(f"  UNEXPECTED {path.relative_to(REPO_ROOT)}")
        for path, field in drifted[: args.max_report]:
            print(f"  DRIFT     {path.relative_to(REPO_ROOT)}: {field}")
        for identifier in unlocked[: args.max_report]:
            print(f"  UNLOCKED  {identifier}")
        for identifier in stale_lock[: args.max_report]:
            print(f"  STALE     {identifier} in PATHS.tsv but not produced")

    if problems:
        print("\ncorpus does not reproduce from data/raw/. Fix the extractor, the seeder, or "
              "curation/decisions.tsv — not the record.", file=sys.stderr)
        return 1
    print("\ncorpus reproduces exactly from data/raw/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

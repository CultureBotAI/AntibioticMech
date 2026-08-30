#!/usr/bin/env python3
"""Check curation/source_queue.tsv against the repository it describes.

The queue ranks candidate data sources for the corpus. It is curator-owned prose
in a TSV, so nothing stops it drifting into wishful thinking: a source marked
ADOPTED that the pipeline never reads, a licence left UNVERIFIED under a record
the corpus redistributes, a gap named that the schema does not have.

This checks the claims that are checkable:

  * shape — known columns, known enum values, no duplicate ids
  * every gap named is a real field a record can carry
  * ADOPTED means adopted: the source appears in conf/sources.yaml, its
    redistribution terms have been verified, and it carries a verification date
  * conversely, every source the pipeline actually reads has an ADOPTED row
  * nothing is SEED-able while its redistribution terms are UNVERIFIED or
    RESTRICTED — the corpus is CC0, and that promise is only as good as the
    weakest source in it

    python scripts/check_source_queue.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = REPO_ROOT / "curation" / "source_queue.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"

COLUMNS = ["source_id", "name", "closes_gap", "use", "structures", "redistribution",
           "access", "priority", "status", "verified_on", "url", "rationale"]

USE = {"SEED", "CURATE_ONLY", "REFERENCE"}
STRUCTURES = {"COMPLETE", "PARTIAL", "NONE", "UNVERIFIED"}
REDISTRIBUTION = {"CC0_OK", "ATTRIBUTION", "RESTRICTED", "UNVERIFIED"}
ACCESS = {"BULK", "API", "BOTH", "MANUAL", "UNVERIFIED"}
STATUS = {"CANDIDATE", "EVALUATING", "ADOPTED", "REJECTED", "BLOCKED"}

# Gaps that are not record fields: the corpus-level things a source can close.
EXTRA_GAPS = {"identity", "structures", "evidence", "classification", "mechanism_type"}


# A section in conf/sources.yaml describes a SOURCE when it names one — it has a
# `name`. The alternative, keying on `homepage`, silently excluded pubchem (which
# has none) and had to be rescued by a hardcoded special case; any future source
# section that omitted the key would have been dropped just as quietly, and a
# check that silently stops checking is worse than no check.
SOURCE_MARKER = "name"


def source_sections(conf: dict) -> set[str]:
    return {key for key, value in conf.items()
            if isinstance(value, dict) and SOURCE_MARKER in value}


def record_fields() -> set[str]:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return set(schema["classes"]["AntibioticRecord"]["attributes"])


def main() -> int:
    if not QUEUE_PATH.exists():
        print(f"missing {QUEUE_PATH}", file=sys.stderr)
        return 1

    with QUEUE_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != COLUMNS:
            print(f"unexpected columns: {reader.fieldnames}", file=sys.stderr)
            return 1
        rows = list(reader)

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    pipeline_sources = source_sections(conf)
    allowed_gaps = record_fields() | EXTRA_GAPS

    problems: list[str] = []
    seen: set[str] = set()

    for row in rows:
        sid = row["source_id"]
        if sid in seen:
            problems.append(f"{sid}: duplicate row")
        seen.add(sid)

        for column, allowed in (("use", USE), ("structures", STRUCTURES),
                                ("redistribution", REDISTRIBUTION), ("access", ACCESS),
                                ("status", STATUS)):
            if row[column] not in allowed:
                problems.append(f"{sid}: {column}={row[column]!r} not one of {sorted(allowed)}")

        if row["closes_gap"] not in allowed_gaps:
            problems.append(f"{sid}: closes_gap={row['closes_gap']!r} is not a record field "
                            f"or a known corpus-level gap")
        if not row["priority"].isdigit() or not 1 <= int(row["priority"]) <= 5:
            problems.append(f"{sid}: priority={row['priority']!r} must be 1-5")
        if not row["rationale"].strip():
            problems.append(f"{sid}: no rationale — why this source, and why now?")
        if not row["url"].startswith("http"):
            problems.append(f"{sid}: url is not a URL")

        if row["status"] == "ADOPTED":
            if sid not in pipeline_sources:
                problems.append(f"{sid}: ADOPTED but conf/sources.yaml does not read it")
            if row["redistribution"] == "UNVERIFIED":
                problems.append(f"{sid}: ADOPTED with unverified redistribution terms")
            if not row["verified_on"].startswith("20"):
                problems.append(f"{sid}: ADOPTED without a verification date")

        # The CC0 promise is only as strong as the weakest thing seeded into it.
        if row["use"] == "SEED" and row["status"] == "ADOPTED" \
                and row["redistribution"] == "RESTRICTED":
            problems.append(f"{sid}: seeded into a CC0 corpus under restrictive terms")

    adopted = {r["source_id"] for r in rows if r["status"] == "ADOPTED"}
    for source in sorted(pipeline_sources - adopted):
        problems.append(f"{source}: read by conf/sources.yaml but has no ADOPTED queue row")

    if problems:
        print("source queue check FAILED:", file=sys.stderr)
        print("\n".join(f"  {p}" for p in problems), file=sys.stderr)
        return 1

    by_status: dict[str, int] = {}
    for row in rows:
        by_status[row["status"]] = by_status.get(row["status"], 0) + 1
    nxt = sorted((r for r in rows if r["status"] == "CANDIDATE"),
                 key=lambda r: (int(r["priority"]), r["source_id"]))[:3]
    print(f"source queue OK: {len(rows)} sources — "
          + ", ".join(f"{count} {status.lower()}" for status, count in sorted(by_status.items())))
    if nxt:
        print("next up: " + ", ".join(f"{r['source_id']} (P{r['priority']}, "
                                      f"{r['closes_gap']})" for r in nxt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Apply the reviewed cross-corpus link plan through the validated curation writer."""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path

import yaml

from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.pathway_links import check_links, load_index
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]


def apply_plan(record: dict, plan: dict, commit: str, index: dict) -> dict:
    result = deepcopy(record)
    links = result.setdefault("related_records", [])
    for planned in plan["links"]:
        link = {"corpus": "PathwayMech", **planned, "source_version": commit}
        if link not in links:
            if any(row.get("corpus") == "PathwayMech"
                   and row.get("identifier") == link["identifier"] for row in links):
                raise ValueError("existing PathwayMech link differs; review before replacing it")
            links.append(link)
    if plan.get("protein_example"):
        targets = [target for target in result.get("molecular_targets", [])
                   if target.get("source") == "PRIMARY_LITERATURE"
                   and any(e.get("reference") == plan["target_reference"]
                           for e in target.get("evidence", []))]
        if len(targets) != 1:
            raise ValueError("protein example requires exactly one supported curator-owned target")
        examples = targets[0].setdefault("protein_examples", [])
        example = plan["protein_example"]
        if example not in examples:
            if any(row["uniprot_id"] == example["uniprot_id"] for row in examples):
                raise ValueError("existing protein example differs; review before replacing it")
            examples.append(example)
    errors = check_links(result, commit, index)
    if errors:
        raise ValueError("; ".join(errors))
    if result != record:
        record_curation_event(result, curator="codex", action="ADD_PATHWAY_LINKS",
                              changes="Added reviewed PathwayMech relationships and any supported "
                              "protein example from curation/pathway_links.yaml; organism and "
                              "evidence limits are recorded in each basis.", llm_assisted=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--only", help="one record identifier for a canary")
    args = parser.parse_args()
    plans = yaml.safe_load((ROOT / "curation/pathway_links.yaml").read_text())["records"]
    selected = {plan["identifier"]: plan for plan in plans
                if not args.only or plan["identifier"] == args.only}
    if not selected:
        parser.error("no planned record selected")
    commit, index = load_index(ROOT)
    seen = set()
    changes = []
    for path in sorted((ROOT / "data/antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text())
        if record["identifier"] not in selected:
            continue
        seen.add(record["identifier"])
        updated = apply_plan(record, selected[record["identifier"]], commit, index)
        if updated != record:
            changes.append((path, updated))
    if seen != set(selected):
        raise ValueError(f"missing records: {set(selected) - seen}")
    for path, updated in changes:
        print(f"{'write' if args.apply else 'would write'} {path.relative_to(ROOT)}")
        if args.apply:
            write_validated_antibiotic(updated, path)
    print(f"{len(changes)} records changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

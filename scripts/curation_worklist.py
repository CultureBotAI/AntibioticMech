#!/usr/bin/env python3
"""The curation backlog, ranked so a curator can start at the top.

Six queues, each answering a different question:

  no-structure  Source concepts that never became records because no source
                gives them a structure. Each needs a structure or an EXCLUDE
                decision in curation/decisions.tsv.
  mechanism     Seeded records with no molecular target, mode of action, or
                causal graph — the mechanism layer this repository exists for.
  minted        Records whose identity is a minted CURIE. Each needs either a
                defensible ontology identity or a recorded reason it has none.
  target-evidence
                Database-asserted direct targets still lacking a primary citation.

    python scripts/curation_worklist.py                 # all three, top 25 each
    python scripts/curation_worklist.py --queue minted --limit 100
    python scripts/curation_worklist.py --tsv reports/worklist.tsv

Suggestions are a starting point, never an answer: anything written into
curation/decisions.tsv is re-checked against the inventories at seed time.
"""

from __future__ import annotations

import argparse
import csv
import re
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
    curator_owns_mode_of_action,
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
        # A SEEDED mode_of_action does not retire a record from this queue: its
        # own note asks a curator to confirm the value, and writing that note
        # used to remove the record from the only list where a curator would
        # find it. 433 records vanished the day mode_of_action was first seeded,
        # 68 of them carrying the CARD evidence that puts them at the top.
        # A curator who has claimed the field has decided, whether they set a
        # value or vetoed one. Requiring a value here left a documented veto in
        # the queue forever with no way out — and re-introduced the divergence
        # the single ownership predicate exists to prevent.
        curator_set_moa = curator_owns_mode_of_action(record)
        if record.get("causal_graphs") or curator_set_moa:
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


def seeded_mechanism_view() -> dict[str, dict]:
    """identifier -> the mechanism block the seeder derives right now.

    The queue below cannot tell a curator's scope from a leftover by looking at
    the record, because both are just a value. It can tell them apart by asking
    the seeder what IT would derive, which is the only thing that makes the
    distinction knowable.
    """
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    manifest = yaml.safe_load((RAW_DIR / "MANIFEST.yaml").read_text(encoding="utf-8"))
    concepts, chebi_rows = build_concepts(conf)
    derived, _ = merge(concepts, chebi_rows, conf, load_decisions(),
                       manifest.get("retrieved_on", ""))
    return {ident: {"mode_of_action": rec.get("mode_of_action"),
                    "mode_of_action_target_scope": rec.get("mode_of_action_target_scope")}
            for ident, rec in derived.items()}


def mode_of_action_scope_queue(records: list[dict],
                               derived: dict[str, dict] | None = None) -> list[dict]:
    """Curator-owned mechanisms whose target scope has not been settled.

    The scope describes the mechanism it sits beside, and the seeder derives it
    from the ChEBI roles. Once a curator claims `mode_of_action`, the seeder can
    no longer derive a scope for their value and must not guess — it copies the
    block forward verbatim. That leaves one loose end: a scope derived for the
    seeder's mechanism, still sitting beside a curator's different one.

    This queue is that loose end, and it is COMPARED AGAINST THE DERIVATION
    rather than sniffed from the note text. An earlier version keyed on "the
    seeder's note marker is still present", which missed the case it existed for
    entirely — a curator who REPLACES the note (a state `curator_owns_mode_of_
    action` explicitly supports) and changes the mechanism matched neither of
    its signals — while queueing forever a curator who merely appended
    `CURATOR: confirmed` without changing anything, whose derived scope is
    perfectly valid and who had no way to clear the row.

    Three cases, in order:
      - no scope beside a curator's mechanism: owed outright;
      - the curator changed the mechanism and the scope is still exactly what
        the seeder derives: indistinguishable from a leftover, so it is asked
        about rather than trusted or deleted;
      - anything else: settled, and not queued.
    """
    if derived is None:
        derived = seeded_mechanism_view()
    rows = []
    for record in records:
        moa = record.get("mode_of_action")
        if not moa or not curator_owns_mode_of_action(record):
            continue
        scope = record.get("mode_of_action_target_scope")
        seeded = derived.get(record.get("identifier"), {})
        if not scope:
            hint = "curator mechanism with no target scope"
        elif (seeded.get("mode_of_action") != moa
              and seeded.get("mode_of_action_target_scope") == scope):
            hint = (f"scope {scope} is what the seeder derives for "
                    f"{seeded.get('mode_of_action')}, not for {moa}")
        else:
            continue
        rows.append({
            "queue": "moa-scope",
            "key": record["identifier"],
            "label": record["label"],
            "source": "+".join(sorted({c["source"] for c in record.get("source_concepts", [])})),
            "source_id": moa,
            "hint": hint,
        })
    rows.sort(key=lambda r: r["label"].lower())
    return rows


# Words in a CARD definition that name a target group. Used ONLY to surface
# candidates for a curator; never to classify. "fungal" matches ophiobolin A's
# "isolated as fungal phytotoxins", where the fungus is the SOURCE and not the
# target — the pattern cannot tell those apart, which is precisely why the
# adjudication lives in conf/sources.yaml as a curated map.
DEFINITION_GROUP_HINTS = {
    "ANTIFUNGAL": r"\bfungicid|\bantifungal|\bfungal\b|\byeast\b|\bmildew\b",
    "ANTIVIRAL": r"\bantiviral\b|\bvirus(es)?\b|\bviral\b",
    "ANTIPROTOZOAL": r"\bantiprotozoal\b|\bmalaria|\bprotozoa|\bleishman|\btrypanosom",
    "ANTIBACTERIAL": r"\bantibacterial\b|\bbacteri(a|al|um)\b",
    # Without this the queue could never surface an antiseptic: acriflavine only
    # appeared because its definition happens to mention fungal infections in
    # aquarium fish, and thiacalixarene derivatives never appeared at all.
    "BIOCIDE": r"\bantiseptic|\bdisinfect|\bpreservative\b|\bsanitis|\bsanitiz",
}


def aro_class_queue(records: list[dict], conf: dict | None = None) -> list[dict]:
    """ARO-fallback records whose own definition names another target group.

    A molecule in CARD's antibiotic subtree is there for a bacterial reason, so
    the fallback files it ANTIBACTERIAL — right for 265 of the 276 records it
    reaches. For the rest CARD's own definition says otherwise, and until this
    queue existed nothing surfaced them: triflumizole sat under ANTIBACTERIAL
    while its ChEBI-grounded twin sat under ANTIFUNGAL, one compound in two
    classes, with every gate green.

    Adjudicated records drop off, because `aro_definition_overrides` decides
    them. What remains is a curator's question, and a record that CANNOT be
    adjudicated from the definition still belongs here rather than nowhere.
    """
    if conf is None:
        conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    overrides = conf.get("aro_definition_overrides", {})
    parent_map = conf.get("aro_parent_to_class", {})

    # aro_id -> the names of its parents, so the queue can see a group stated in
    # the hierarchy rather than in prose.
    aro_parent_labels: dict[str, str] = {}
    aro_parent_ids: dict[str, tuple[str, ...]] = {}
    with (RAW_DIR / "aro_antibiotics.tsv").open(encoding="utf-8") as fh:
        aro_rows = list(csv.DictReader(fh, delimiter="\t"))
    names = {r["aro_id"]: r["name"] for r in aro_rows}
    for r in aro_rows:
        parents = tuple(p for p in (r.get("parent_ids") or "").split("|") if p)
        aro_parent_ids[r["aro_id"]] = parents
        aro_parent_labels[r["aro_id"]] = " ".join(names.get(p, "") for p in parents)

    rows = []
    for record in records:
        if record.get("activity_roles"):
            continue                                   # a ChEBI role decided it
        concepts = record.get("source_concepts") or []
        if {c.get("source") for c in concepts} != {"ARO"}:
            continue                                   # not the fallback's doing
        aro_ids = [c.get("source_id") for c in concepts]
        if any(a in overrides for a in aro_ids):
            continue                                   # a curator has decided
        if any(p in parent_map for a in aro_ids
               for p in aro_parent_ids.get(a, ())):
            continue                                   # a mapped parent decided
        # Definition AND the labels of the concept's ARO parents. Reading only
        # the definition hid myxothiazole, whose definition is pure mechanism
        # ("inhibitor of the mitochondrial cytochrome bc1 complex") while its
        # parent is named "antifungal without defined classification".
        text = str(record.get("definition") or "").lower()
        text += " " + " ".join(aro_parent_labels.get(a, "") for a in aro_ids).lower()
        named = sorted(group for group, pattern in DEFINITION_GROUP_HINTS.items()
                       if re.search(pattern, text))
        filed = record.get("antimicrobial_class")
        # Flag only when the filing is NOT among the groups CARD names. Testing
        # for an exact single-group match instead kept acriflavine and
        # thiacalixarene derivatives in the queue after they were correctly
        # filed BIOCIDE, because their text names a second group too — a queue
        # that lists correct records is one a curator learns to ignore.
        if not named or filed in named:
            continue
        rows.append({
            "queue": "aro-class",
            "key": record["identifier"],
            "label": record["label"],
            "source": "ARO",
            "source_id": next((a for a in aro_ids if a), ""),
            "hint": f"filed {filed}; CARD's definition names {', '.join(named)}",
        })
    rows.sort(key=lambda r: r["label"].lower())
    return rows


def unknown_mechanism_queue(records: list[dict]) -> list[dict]:
    """Determinants seeded with mechanism_type UNKNOWN.

    docs/HARMONIZATION.md promises these "land on the curation worklist rather
    than being guessed" — they did not, until this queue existed. Keyed by
    determinant rather than by record: one determinant can appear on hundreds of
    compounds, and typing it once fixes all of them.
    """
    by_determinant: dict[str, dict] = {}
    for record in records:
        for item in record.get("resistance_mechanisms") or []:
            if item.get("mechanism_type") != "UNKNOWN":
                continue
            key = item.get("aro_id") or item.get("label", "")
            entry = by_determinant.setdefault(key, {
                "queue": "unknown-mech",
                "key": key,
                "label": item.get("label", ""),
                "source": "ARO",
                "source_id": "",
                "records": 0,
            })
            entry["records"] += 1
    rows = []
    for entry in by_determinant.values():
        count = entry.pop("records")
        entry["hint"] = f"mechanism_type UNKNOWN on {count} record(s)"
        entry["_count"] = count
        rows.append(entry)
    rows.sort(key=lambda r: (-r.pop("_count"), r["label"].lower()))
    return rows


def target_evidence_queue(records: list[dict]) -> list[dict]:
    """Database-only direct-target assertions awaiting primary evidence."""
    grouped: dict[str, dict] = {}
    for record in records:
        for target in record.get("molecular_targets") or []:
            if target.get("evidence_status") != "PRIMARY_EVIDENCE_NEEDED":
                continue
            key = target.get("target_id") or target.get("target_label", "")
            row = grouped.setdefault(key, {
                "queue": "target-evidence",
                "key": key,
                "label": target.get("target_label", ""),
                "source": target.get("source", ""),
                "source_id": target.get("target_relation", ""),
                "records": 0,
            })
            row["records"] += 1
    rows = []
    for row in grouped.values():
        count = row.pop("records")
        row["hint"] = (
            f"database direct-target assertion on {count} record(s); "
            "primary citation needed"
        )
        row["_count"] = count
        rows.append(row)
    rows.sort(key=lambda row: (-row.pop("_count"), row["label"].lower()))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queue",
                        choices=("all", "no-structure", "mechanism", "minted", "unknown-mech",
                                 "moa-scope", "target-evidence", "aro-class"),
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
    if args.queue in ("all", "unknown-mech"):
        queues["unknown-mech"] = unknown_mechanism_queue(records)
    if args.queue in ("all", "moa-scope"):
        queues["moa-scope"] = mode_of_action_scope_queue(records)
    if args.queue in ("all", "aro-class"):
        queues["aro-class"] = aro_class_queue(records)
    if args.queue in ("all", "target-evidence"):
        queues["target-evidence"] = target_evidence_queue(records)
    if args.queue in ("all", "aro-class"):
        queues["aro-class"] = aro_class_queue(records)

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

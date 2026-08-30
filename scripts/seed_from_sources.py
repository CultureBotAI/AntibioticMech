#!/usr/bin/env python3
"""Harmonize the committed inventories into one AntibioticRecord per structure.

Reads only ``data/raw/`` — never the network — and writes
``data/antibiotics/<class>/<slug>.yaml`` plus the ``PATHS.tsv`` slug lockfile.

    just seed                       # dry run: per-class counts, nothing written
    just seed-canary CHEBI:48923    # write exactly one record and validate it
    just seed-apply                 # write the whole corpus

Identity
--------
A record is ONE chemical structure. Identity resolution, in order:

1. A source concept with a ChEBI cross-reference that has a default structure
   grounds to that ChEBI CURIE (`grounding_status: EXACT`).
2. Otherwise the concept keeps a content-hashed `antibioticmech:<source>-<hash>`
   CURIE (`grounding_status: MINTED`).
3. Concepts that resolve to the same InChIKey merge into one record carrying
   every source concept — that merge is the product.

A concept with no structure at all is NOT written: without an InChIKey there is
nothing to assert identity on, and a name is not a structure. Those land on the
curation worklist instead (`just worklist`).
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from antibioticmech.curate.curation_event import record_curation_event  # noqa: E402
from antibioticmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_antibiotic,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"

CLASS_DIRS = {
    "ANTIBACTERIAL": "antibacterial",
    "ANTIMYCOBACTERIAL": "antimycobacterial",
    "ANTIFUNGAL": "antifungal",
    "ANTIPROTOZOAL": "antiprotozoal",
    "BIOCIDE": "biocide",
    "ANTIMICROBIAL_UNSPECIFIED": "unspecified",
    "OTHER": "other",
}

# ARO writes its own cross-reference prefixes; ChEBI's are already bioregistry
# prefixes and pass through unchanged. Anything not listed and not already
# lowercase-bioregistry-shaped is dropped rather than guessed — an unregistered
# prefix does not resolve, and a CURIE that resolves nowhere is worse than none.
XREF_PREFIX = {
    "PubChem": "pubchem.compound",
    "ChEMBL": "chembl",
    "CAS": "cas",
    "CHEBI": "CHEBI",
    "PDB": "pdb",
    "ARO": "ARO",
}
CURIE_LOCAL = re.compile(r"^[A-Za-z0-9._-]+$")
BIOREGISTRY_PREFIX = re.compile(r"^[a-z][a-z0-9._-]*$")

# Fields the seeder owns end to end. Everything else on a record belongs to a
# curator and must survive a re-seed untouched — `verify_corpus.py` imports this
# list so "what the seeder owns" has exactly one definition.
SEEDED_FIELDS = [
    "identifier", "label", "definition", "definition_source", "synonyms",
    "parent_compounds", "xrefs", "antimicrobial_class", "activity_roles",
    "structural_class", "structural_class_id", "chemical_structure",
    "source_concepts", "grounding_status",
]

# Curator-owned fields. A re-seed copies these forward verbatim from the record
# on disk, so `just seed-apply` after months of curation is a safe operation
# rather than a way to lose all of it.
CURATOR_FIELDS = [
    "curation_status", "grounding_notes", "evidence", "mode_of_action",
    "mode_of_action_notes", "cidality", "biosynthesis_origin", "clinical_status",
    "producer_organisms", "activity_spectrum", "causal_graphs", "datasets",
    "contributors",
]

SYNONYM_TYPE = {
    "NAME": "EXACT_SYNONYM",
    "SYNONYM": "EXACT_SYNONYM",
    "IUPAC NAME": "EXACT_SYNONYM",
    "INN": "INN",
    "BRAND NAME": "BRAND_NAME",
}


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------

def load_tsv(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"missing inventory {path}; run `just extract-inventory`")
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def split_pipe(value: str) -> list[str]:
    return [v for v in (value or "").split("|") if v]


def mint(source: str, source_id: str) -> str:
    """Content-hashed identifier for one source concept.

    Hashing the (source, source_id) pair rather than the label keeps the CURIE
    stable when an upstream label is corrected — the identifier is the join key
    that curation decisions are written against, so it must not move.
    """
    digest = hashlib.sha256(f"{source}|{source_id}".encode()).hexdigest()[:10]
    return f"antibioticmech:{source.lower()}-{digest}"


def load_decisions() -> dict[str, dict]:
    """Curator decisions keyed by the minted identifier of one source concept."""
    if not DECISIONS_PATH.exists():
        return {}
    with DECISIONS_PATH.open(newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t") if r.get("minted_identifier")]
    return {r["minted_identifier"]: r for r in rows}


# --------------------------------------------------------------------------
# harmonization
# --------------------------------------------------------------------------

class Concept:
    """One upstream concept, before merging."""

    __slots__ = ("source", "source_id", "label", "definition", "definition_refs",
                 "roles", "parents", "xrefs", "synonyms", "structure", "structural_class",
                 "structural_class_id", "minted")

    def __init__(self, source, source_id, label):
        self.source = source
        self.source_id = source_id
        self.label = label
        self.definition = ""
        self.definition_refs: list[str] = []
        self.roles: list[str] = []
        self.parents: list[str] = []
        self.xrefs: list[str] = []
        self.synonyms: list[tuple[str, str]] = []
        self.structure: dict = {}
        self.structural_class = ""
        self.structural_class_id = ""
        self.minted = ""


def normalize_xref(raw: str) -> str | None:
    """`PubChem:12560` -> `pubchem.compound:12560`; `chembl:CHEMBL532` passes through."""
    if ":" not in raw:
        return None
    prefix, local = raw.split(":", 1)
    local = local.strip()
    mapped = XREF_PREFIX.get(prefix)
    if mapped is None and BIOREGISTRY_PREFIX.match(prefix):
        mapped = prefix
    if mapped is None or not CURIE_LOCAL.match(local):
        return None
    return f"{mapped}:{local}"


def _numeric_fields(row: dict, *, charge_via_float: bool) -> dict:
    """Parse the numeric structure columns, dropping anything unparseable.

    A malformed mass in an upstream row should cost that one field, not the
    whole record: the structure is still identified by its InChIKey. PubChem
    writes charge as "0.0" while ChEBI writes "0", hence `charge_via_float`.
    """
    out: dict = {}
    for key in ("charge", "average_mass", "monoisotopic_mass"):
        raw = row.get(key, "")
        if raw in ("", None):
            continue
        with contextlib.suppress(ValueError):
            if key == "charge":
                out[key] = int(float(raw)) if charge_via_float else int(raw)
            else:
                out[key] = float(raw)
    return out


def structure_from_chebi(row: dict) -> dict:
    out = {
        "smiles": row["smiles"],
        "standard_inchi": row["standard_inchi"],
        "standard_inchi_key": row["standard_inchi_key"],
        "molecular_formula": row["molecular_formula"],
        "structure_source": "ChEBI",
    }
    out.update(_numeric_fields(row, charge_via_float=False))
    return {k: v for k, v in out.items() if v not in ("", None)}


def structure_from_pubchem(row: dict) -> dict:
    out = {
        "smiles": row["smiles"],
        "standard_inchi": row["standard_inchi"],
        "standard_inchi_key": row["standard_inchi_key"],
        "molecular_formula": row["molecular_formula"],
        "structure_source": "PubChem",
        "retrieved_on": row["retrieved_on"],
    }
    out.update(_numeric_fields(row, charge_via_float=True))
    return {k: v for k, v in out.items() if v not in ("", None)}


def classify(roles: list[str], conf: dict, from_aro: bool) -> str:
    """Assign the filesystem/reporting class from the asserted role terms.

    The most specific role wins by the priority in conf/sources.yaml. An ARO
    concept with no ChEBI role is ANTIBACTERIAL: CARD's antibiotic molecule
    subtree is a bacterial-resistance resource and every molecule in it is there
    because a bacterial determinant acts on it.
    """
    mapping = conf["role_to_class"]
    best = None
    for role in roles:
        entry = mapping.get(role)
        if entry and (best is None or entry["priority"] < best["priority"]):
            best = entry
    if best:
        return best["class"]
    if from_aro:
        return "ANTIBACTERIAL"
    return "ANTIMICROBIAL_UNSPECIFIED"


def build_concepts(conf: dict) -> tuple[list[Concept], dict[str, dict]]:
    chebi_rows = {r["chebi_id"]: r for r in load_tsv(RAW_DIR / "chebi_antimicrobials.tsv")}
    aro_rows = load_tsv(RAW_DIR / "aro_antibiotics.tsv")
    pubchem_path = RAW_DIR / "pubchem_structures.tsv"
    pubchem = {r["aro_id"]: r for r in load_tsv(pubchem_path)} if pubchem_path.exists() else {}

    concepts: list[Concept] = []

    for chebi_id, row in chebi_rows.items():
        if row["in_role_scope"] != "true":
            continue  # pulled in only to lend its structure to an ARO concept
        concept = Concept("CHEBI", chebi_id, row["name"])
        concept.definition = row["definition"]
        concept.roles = split_pipe(row["role_ids"])
        concept.parents = split_pipe(row["parent_ids"])
        concept.xrefs = [x for x in (normalize_xref(v) for v in split_pipe(row["xrefs"])) if x]
        for entry in split_pipe(row["synonyms"]):
            kind, _, text = entry.partition("=")
            if text and text != row["name"]:
                concept.synonyms.append((text, SYNONYM_TYPE.get(kind, "RELATED_SYNONYM")))
        concept.structure = structure_from_chebi(row)
        concepts.append(concept)

    for row in aro_rows:
        concept = Concept("ARO", row["aro_id"], row["name"])
        concept.definition = row["definition"]
        concept.definition_refs = split_pipe(row["definition_refs"])
        concept.xrefs = [x for x in (normalize_xref(v) for v in split_pipe(row["xrefs"])) if x]
        concept.synonyms = [(s, "EXACT_SYNONYM") for s in split_pipe(row["synonyms"])]
        concept.structural_class = row["drug_class_label"]
        concept.structural_class_id = row["drug_class_id"]
        if row["drug_class_id"]:
            concept.parents = [row["drug_class_id"]]
        chebi_id = next((x for x in split_pipe(row["xrefs"]) if x.startswith("CHEBI:")), "")
        chebi_row = chebi_rows.get(chebi_id)
        if chebi_row and chebi_row["standard_inchi_key"]:
            concept.structure = structure_from_chebi(chebi_row)
            concept.roles = split_pipe(chebi_row["role_ids"])
        elif row["aro_id"] in pubchem:
            concept.structure = structure_from_pubchem(pubchem[row["aro_id"]])
        concepts.append(concept)

    for concept in concepts:
        concept.minted = mint(concept.source, concept.source_id)
    return concepts, chebi_rows


def resolve_identity(concept: Concept, chebi_rows: dict[str, dict]) -> tuple[str, str]:
    """(identifier, grounding_status) for one concept."""
    if concept.source == "CHEBI":
        return concept.source_id, "EXACT"
    chebi_id = next((x for x in concept.xrefs if x.startswith("CHEBI:")), "")
    if chebi_id and chebi_rows.get(chebi_id, {}).get("standard_inchi_key"):
        return chebi_id, "EXACT"
    return concept.minted, "MINTED"


def slugify(label: str) -> str:
    """URL-safe slug for a compound name.

    Brackets and punctuation become separators rather than vanishing, so
    "N,N'-bis(2-chloroethyl)amine" reads as "n-n-bis-2-chloroethyl-amine"
    instead of running the fragments together. Non-ASCII letters are kept:
    "β-lactam" is how the compound is named, and browsers handle it.
    """
    keep = []
    for ch in label.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_/,+()[]{}':;.":
            keep.append("-")
    slug = "".join(keep)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")[:70] or "unnamed"


def assign_slugs(records: dict[str, dict], lockfile: dict[str, str]) -> dict[str, str]:
    """Identifier -> slug, honouring the committed lockfile.

    Slugs are corpus-wide and published in URLs, so an existing assignment is
    never silently changed here: edit PATHS.tsv and re-seed.
    """
    assigned = dict(lockfile)
    taken = set(assigned.values())
    for identifier in sorted(records):
        if identifier in assigned:
            continue
        base = slugify(records[identifier]["label"])
        slug = base
        if slug in taken:
            suffix = identifier.split(":", 1)[1].lower().replace(".", "-")
            slug = f"{base}-{suffix}"[:90]
        n = 2
        while slug in taken:
            slug = f"{base}-{n}"
            n += 1
        assigned[identifier] = slug
        taken.add(slug)
    return assigned


def merge(concepts: list[Concept], chebi_rows: dict[str, dict], conf: dict,
          decisions: dict[str, dict], source_version: str) -> tuple[dict[str, dict], list[Concept]]:
    """Group concepts into records. Returns (records, skipped-for-no-structure)."""
    by_identity: dict[str, list[Concept]] = defaultdict(list)
    grounding: dict[str, str] = {}
    skipped: list[Concept] = []

    for concept in concepts:
        decision = decisions.get(concept.minted, {})
        if (decision.get("decision") or "").upper() == "EXCLUDE":
            continue
        if not concept.structure.get("standard_inchi_key"):
            skipped.append(concept)
            continue
        identifier, status = resolve_identity(concept, chebi_rows)
        override = (decision.get("identifier") or "").strip()
        if override:
            identifier, status = override, "EXACT"
        by_identity[identifier].append(concept)
        grounding[identifier] = status

    # A ChEBI id and an ARO-minted id describing the same structure are the same
    # record: fold minted groups into the grounded group with the same InChIKey.
    inchikey_owner: dict[str, str] = {}
    for identifier, group in by_identity.items():
        if grounding[identifier] == "EXACT":
            key = group[0].structure["standard_inchi_key"]
            inchikey_owner.setdefault(key, identifier)
    for identifier in list(by_identity):
        if grounding[identifier] == "EXACT":
            continue
        key = by_identity[identifier][0].structure["standard_inchi_key"]
        owner = inchikey_owner.get(key)
        if owner and owner != identifier:
            by_identity[owner].extend(by_identity.pop(identifier))
            grounding.pop(identifier, None)

    records: dict[str, dict] = {}
    for identifier, group in by_identity.items():
        records[identifier] = build_record(identifier, grounding[identifier], group,
                                           conf, source_version)
    return records, skipped


def _dedupe(values):
    seen, out = set(), []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def build_record(identifier: str, grounding_status: str, group: list[Concept],
                 conf: dict, source_version: str) -> dict:
    # ChEBI leads on identity and structure; ARO leads on class and mechanism.
    chebi = [c for c in group if c.source == "CHEBI"]
    aro = [c for c in group if c.source == "ARO"]
    primary = (chebi or aro)[0]

    roles = _dedupe(r for c in group for r in c.roles)
    structural_class = next((c.structural_class for c in aro if c.structural_class), "")
    structural_class_id = next((c.structural_class_id for c in aro if c.structural_class_id), "")

    definition, definition_source = "", ""
    for concept in (chebi + aro):
        if concept.definition:
            definition = concept.definition
            if concept.source == "ARO":
                definition_source = concept.definition_refs[0] if concept.definition_refs else "ARO"
            else:
                definition_source = "ChEBI"
            break

    synonyms = []
    seen_syn = {primary.label}
    for concept in group:
        for text, kind in concept.synonyms:
            if text not in seen_syn:
                seen_syn.add(text)
                synonyms.append({"synonym_text": text, "synonym_type": kind,
                                 "source": concept.source.lower()})

    record: dict = {
        "identifier": identifier,
        "label": primary.label,
        "antimicrobial_class": classify(roles, conf, from_aro=bool(aro)),
        "curation_status": "SEEDED",
        "grounding_status": grounding_status,
    }
    if definition:
        record["definition"] = definition
        record["definition_source"] = definition_source
    if synonyms:
        record["synonyms"] = synonyms[:40]
    parents = _dedupe(p for c in group for p in c.parents)
    if parents:
        record["parent_compounds"] = parents
    xrefs = _dedupe(x for c in group for x in c.xrefs
                    if x != identifier and not x.startswith("antibioticmech:"))
    for concept in aro:
        xrefs.insert(0, concept.source_id)
    xrefs = _dedupe(xrefs)
    if xrefs:
        record["xrefs"] = xrefs
    if roles:
        record["activity_roles"] = roles
    if structural_class:
        record["structural_class"] = structural_class
        record["structural_class_id"] = structural_class_id
    structure = next((c.structure for c in group if c.structure.get("standard_inchi")),
                     group[0].structure)
    record["chemical_structure"] = structure
    record["source_concepts"] = [
        {
            "source": c.source,
            "source_id": c.source_id,
            "source_label": c.label,
            "minted_identifier": c.minted,
            **({"role_terms": c.roles} if c.roles else {}),
            "source_version": source_version,
        }
        for c in sorted(group, key=lambda c: (c.source, c.source_id))
    ]
    record_curation_event(
        record,
        curator="seed_from_sources",
        action="SEEDED_FROM_SOURCES",
        changes=f"Seeded from data/raw/ inventories ({', '.join(sorted({c.source for c in group}))})",
    )
    return record


def _history_last(record: dict) -> None:
    """Keep curation_history at the end of the emitted YAML.

    Fields are written in insertion order, and the mechanism sections are
    attached after the seed event, so without this the audit trail would sit in
    the middle of every record.
    """
    history = record.pop("curation_history", None)
    if history is not None:
        record["curation_history"] = history


def flag_structure_collisions(records: dict[str, dict], source_version: str) -> int:
    """Flag two records that claim different compounds but the same structure.

    This happens when CARD gives two molecules PubChem CIDs that resolve to one
    structure — gramicidin S and gramicidin C, for instance, are different
    peptides, so one of the two CIDs is wrong upstream. Neither merging them
    (which would assert they are the same compound) nor dropping them (which
    would discard the one that is right) is honest, and the seeder cannot tell
    which is which. So both records stay, each carrying a CURATION_TODO naming
    its twin. A minted concept colliding with a ChEBI-grounded structure is a
    different case and is merged, not flagged — see `merge`.
    """
    by_key: dict[str, list[str]] = defaultdict(list)
    for identifier, record in records.items():
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(identifier)

    flagged = 0
    for inchikey, group in sorted(by_key.items()):
        if len(group) < 2:
            continue
        if not all(records[i]["grounding_status"] == "MINTED" for i in group):
            continue
        for identifier in sorted(group):
            twins = [i for i in sorted(group) if i != identifier]
            record = records[identifier]
            record["discussions"] = [{
                "discussion_id": f"structure-collision-{inchikey}",
                "prompt": (f"{record['label']} shares InChIKey {inchikey} with "
                          f"{', '.join(records[t]['label'] for t in twins)}, but the sources "
                          "name them as different compounds. Which record does this structure "
                          "belong to?"),
                "kind": "CURATION_TODO",
                "status": "OPEN",
                "attaches_to": ["chemical_structure"],
                "rationale": ("Both structures come from PubChem CIDs cross-referenced by CARD. "
                              "Identical structures under different names mean at least one "
                              "cross-reference is wrong upstream; the seeder cannot tell which, "
                              "so it flags rather than merges."),
                "posed_by": "seed_from_sources",
                "notes": f"twin record(s): {', '.join(twins)}",
            }]
            _history_last(record)
            flagged += 1
    return flagged


def attach_aro_mechanism(records: dict[str, dict], source_version: str) -> None:
    """Attach CARD's resistance determinants and drug targets to seeded records.

    Both are database assertions, cited as such: CARD's own ARO term is the
    evidence reference. A curator upgrading one to a primary citation replaces
    the reference; nothing here claims literature support it does not have.
    """
    by_aro: dict[str, str] = {}
    for identifier, record in records.items():
        for concept in record["source_concepts"]:
            if concept["source"] == "ARO":
                by_aro[concept["source_id"]] = identifier

    resistance = load_tsv(RAW_DIR / "aro_resistance_edges.tsv")
    targets = load_tsv(RAW_DIR / "aro_target_edges.tsv")

    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in resistance:
        identifier = by_aro.get(row["antibiotic_id"])
        if identifier:
            grouped[identifier].append(row)
    for identifier, rows in grouped.items():
        items = []
        for row in sorted(rows, key=lambda r: r["determinant_id"]):
            items.append({
                "mechanism_type": row["mechanism"] or "UNKNOWN",
                "aro_id": row["determinant_id"],
                "label": row["determinant_name"],
                "evidence": [{
                    "reference": row["determinant_id"],
                    "notes": ("CARD/ARO asserts confers_resistance_to_antibiotic "
                              f"{row['antibiotic_id']} ({row['antibiotic_name']}); "
                              "database assertion, not a primary citation."),
                }],
            })
        records[identifier]["resistance_mechanisms"] = items
        _history_last(records[identifier])

    grouped = defaultdict(list)
    for row in targets:
        identifier = by_aro.get(row["antibiotic_id"])
        if identifier:
            grouped[identifier].append(row)
    for identifier, rows in grouped.items():
        items = []
        for row in sorted(rows, key=lambda r: r["target_id"]):
            item = {
                "target_id": row["target_id"],
                "target_label": row["target_name"],
                "evidence": [{
                    "reference": row["target_id"],
                    "notes": ("CARD/ARO asserts targeted_by_antibiotic "
                              f"{row['antibiotic_id']} ({row['antibiotic_name']}); "
                              "database assertion, not a primary citation."),
                }],
            }
            items.append(item)
        records[identifier]["molecular_targets"] = items
        _history_last(records[identifier])


# --------------------------------------------------------------------------
# writing
# --------------------------------------------------------------------------

def is_card_sourced(item: dict) -> bool:
    """True when every citation on an item is a CARD/ARO database assertion.

    That is exactly the set the seeder writes, so it is also the set a re-seed
    may replace. An item a curator added, or upgraded to a primary citation,
    fails this test and is carried forward.
    """
    evidence = item.get("evidence") or []
    return bool(evidence) and all(
        str(e.get("reference", "")).startswith("ARO:") for e in evidence
    )


def card_sourced_view(record: dict, field: str) -> list:
    """The CARD-seeded items of `field`, in seed order — what verify-corpus compares."""
    return [item for item in (record.get(field) or []) if is_card_sourced(item)]


def merge_with_existing(record: dict, existing: dict) -> dict:
    """Fold a freshly seeded record into the one already on disk.

    Two things must both hold: seeded fields track the inventories, and curated
    fields survive. A re-seed that silently replaced a curator's mechanism graph
    with an empty one would make the corpus unusable for the work it exists for.

    Re-seeding an unchanged record is also a no-op on disk: the seed event keeps
    its original timestamp, so `just seed-apply` produces a diff only where the
    upstream data actually moved.
    """
    merged = dict(record)

    for field in CURATOR_FIELDS:
        if field in existing:
            merged[field] = existing[field]

    # The seeder owns structure-collision todos; every other discussion is the
    # curator's and is appended after them.
    seeded_discussions = list(record.get("discussions") or [])
    curator_discussions = [
        d for d in (existing.get("discussions") or [])
        if not str(d.get("discussion_id", "")).startswith("structure-collision-")
    ]
    if seeded_discussions or curator_discussions:
        merged["discussions"] = seeded_discussions + curator_discussions
    else:
        merged.pop("discussions", None)

    # CARD-derived mechanism items are re-seeded; curator-added or
    # curator-upgraded ones are kept, after them.
    for field in ("molecular_targets", "resistance_mechanisms"):
        seeded_items = list(record.get(field) or [])
        curator_items = [i for i in (existing.get(field) or []) if not is_card_sourced(i)]
        if seeded_items or curator_items:
            merged[field] = seeded_items + curator_items
        else:
            merged.pop(field, None)

    history = list(existing.get("curation_history") or [])
    if all(existing.get(f) == record.get(f) for f in SEEDED_FIELDS):
        # Nothing the seeder owns changed: keep the trail exactly as it is,
        # rather than appending a new event on every run.
        merged["curation_history"] = history or record.get("curation_history", [])
    else:
        merged["curation_history"] = history
        record_curation_event(
            merged,
            curator="seed_from_sources",
            action="RESEEDED_FROM_SOURCES",
            changes="Re-seeded from updated data/raw/ inventories",
        )
    _history_last(merged)
    return merged


def read_lockfile() -> dict[str, str]:
    if not PATHS_FILE.exists():
        return {}
    with PATHS_FILE.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["slug"] for r in csv.DictReader(fh, delimiter="\t")}


def write_lockfile(records: dict[str, dict], slugs: dict[str, str]) -> None:
    PATHS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with PATHS_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["identifier", "antimicrobial_class", "slug"])
        for identifier in sorted(records):
            writer.writerow([identifier, records[identifier]["antimicrobial_class"],
                             slugs[identifier]])


def record_path(record: dict, slug: str) -> Path:
    return CORPUS_DIR / CLASS_DIRS[record["antimicrobial_class"]] / f"{slug}.yaml"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Write records. Without it, dry run.")
    parser.add_argument("--only", nargs="*", default=None, metavar="IDENTIFIER",
                        help="Write only these identifiers — the canary before a bulk write.")
    parser.add_argument("--limit", type=int, help="Write at most N records.")
    parser.add_argument("--prune", action="store_true",
                        help="Delete corpus files no longer produced. Refused with --only/--limit.")
    parser.add_argument("--force", action="store_true",
                        help="Rewrite records that already exist and are unchanged.")
    args = parser.parse_args()

    if args.prune and (args.only or args.limit):
        raise SystemExit("--prune with --only/--limit would delete records this run never built")

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    manifest = yaml.safe_load((RAW_DIR / "MANIFEST.yaml").read_text(encoding="utf-8"))
    source_version = manifest.get("retrieved_on", "")

    concepts, chebi_rows = build_concepts(conf)
    decisions = load_decisions()
    records, skipped = merge(concepts, chebi_rows, conf, decisions, source_version)
    attach_aro_mechanism(records, source_version)
    flagged = flag_structure_collisions(records, source_version)

    by_class: dict[str, int] = defaultdict(int)
    for record in records.values():
        by_class[record["antimicrobial_class"]] += 1
    merged = sum(1 for r in records.values() if len(r["source_concepts"]) > 1)

    print(f"{len(concepts)} source concepts -> {len(records)} records", file=sys.stderr)
    print(f"  {merged} records carry more than one source concept", file=sys.stderr)
    print(f"  {len(skipped)} concepts have no structure and are not written "
          f"(see `just worklist`)", file=sys.stderr)
    if flagged:
        print(f"  {flagged} records flagged with a structure-collision discussion",
              file=sys.stderr)
    for name, count in sorted(by_class.items(), key=lambda kv: -kv[1]):
        print(f"    {name:26s} {count:>6d}", file=sys.stderr)

    if not args.apply:
        print("\ndry run: nothing written. Use --apply (after `just seed-canary`).", file=sys.stderr)
        return 0

    slugs = assign_slugs(records, read_lockfile())
    selected = sorted(records)
    if args.only:
        wanted = set(args.only)
        selected = [i for i in selected if i in wanted]
        missing = wanted - set(selected)
        if missing:
            print(f"not in the seeded set: {sorted(missing)}", file=sys.stderr)
            if not selected:
                return 1
    if args.limit:
        selected = selected[: args.limit]

    from antibioticmech.validation.write_validated import emit_antibiotic_yaml

    written = unchanged = 0
    for identifier in selected:
        record = records[identifier]
        path = record_path(record, slugs[identifier])
        existing_text = path.read_text(encoding="utf-8") if path.exists() else None
        if existing_text is not None:
            record = merge_with_existing(record, yaml.safe_load(existing_text))
        if existing_text is not None and not args.force and existing_text == emit_antibiotic_yaml(record):
            unchanged += 1
            continue
        try:
            write_validated_antibiotic(record, path)
            written += 1
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1

    if not args.only and not args.limit:
        write_lockfile(records, slugs)

    if args.prune:
        keep = {record_path(records[i], slugs[i]) for i in records}
        removed = 0
        for path in sorted(CORPUS_DIR.rglob("*.yaml")):
            if path not in keep:
                path.unlink()
                removed += 1
        for directory in sorted(CORPUS_DIR.iterdir()):
            if directory.is_dir() and not any(directory.iterdir()):
                shutil.rmtree(directory)
        print(f"  pruned {removed} records no longer produced", file=sys.stderr)

    print(f"wrote {written} records ({unchanged} already current)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

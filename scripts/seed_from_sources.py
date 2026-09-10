#!/usr/bin/env python3
"""Harmonize the committed inventories into one AntibioticRecord per structure.

Reads only the committed source inventories — never the network — and writes
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
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import date
from functools import lru_cache
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
ARO_TARGET_ROLES_PATH = REPO_ROOT / "conf" / "aro_target_roles.tsv"
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
RETIRED_FILE = CORPUS_DIR / "RETIRED.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"
CURATOR_ANTIBIOTICS_PATH = REPO_ROOT / "curation" / "curator_antibiotics.tsv"

CLASS_DIRS = {
    "ANTIBACTERIAL": "antibacterial",
    "ANTIMYCOBACTERIAL": "antimycobacterial",
    "ANTIFUNGAL": "antifungal",
    "ANTIPROTOZOAL": "antiprotozoal",
    "ANTIVIRAL": "antiviral",
    "BIOCIDE": "biocide",
    "ANTIMICROBIAL_UNSPECIFIED": "unspecified",
    "OTHER": "other",
}

def class_parents() -> dict[str, str]:
    """Narrower class -> broader class, read from the schema's enum `is_a`.

    LinkML lets a permissible value declare `is_a`, and AntimicrobialClassEnum
    uses it to say ANTIMYCOBACTERIAL is a kind of ANTIBACTERIAL — mycobacteria
    are bacteria.

    ONE COPY, because a declared hierarchy that only the site honours is not a
    hierarchy. Filing is exclusive and picks the narrower claim, so an
    antimycobacterial record is NOT also under ANTIBACTERIAL; every count that
    answers "which compounds act on bacteria?" therefore has to add the
    subclasses back, and until it does the corpus reports 1037 for a true 1115.
    The site, `just report` and the README block all read this.
    """
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    values = schema["enums"]["AntimicrobialClassEnum"]["permissible_values"]
    return {name: (body or {}).get("is_a")
            for name, body in values.items() if (body or {}).get("is_a")}


def rollup_by_class(counts: dict[str, int]) -> dict[str, int]:
    """Per-class counts with every subclass added into its ancestors.

    Returns totals INCLUSIVE of subclasses; the caller keeps the raw counts for
    the "directly filed" line. Walks to the root, so a future two-level
    hierarchy needs no change here.
    """
    parents = class_parents()
    out = dict(counts)
    for cls, n in counts.items():
        # `seen` stops a malformed is_a from hanging, but it does not stop it
        # DOUBLE-COUNTING: a self-loop A->A, or a 2-cycle A->B->A, adds n to a
        # class already credited with it. Unreachable from today's schema, and
        # a silently wrong total is worse than a loud failure.
        seen = {cls}
        parent = parents.get(cls)
        while parent:
            if parent in seen:
                raise ValueError(
                    f"AntimicrobialClassEnum has a cycle in is_a through {parent!r}; "
                    "a class cannot be its own ancestor")
            seen.add(parent)
            out[parent] = out.get(parent, 0) + n
            parent = parents.get(parent)
    return out


def class_count_rows(counts: dict[str, int]) -> list[dict[str, str | int]]:
    """Return parent-first rows with explicit direct and inclusive counts."""

    parents = class_parents()
    inclusive = rollup_by_class(counts)
    listed = {name for name, count in counts.items() if count}
    for name in list(listed):
        parent = parents.get(name)
        while parent:
            listed.add(parent)
            parent = parents.get(parent)

    children: dict[str, list[str]] = defaultdict(list)
    for child, parent in parents.items():
        if child in listed:
            children[parent].append(child)

    rows: list[dict[str, str | int]] = []

    def visit(name: str) -> None:
        rows.append(
            {
                "antimicrobial_class": name,
                "parent_class": parents.get(name, ""),
                "records_direct": counts.get(name, 0),
                "records_including_subclasses": inclusive.get(name, 0),
            }
        )
        for child in sorted(
            children.get(name, []),
            key=lambda value: (-inclusive.get(value, 0), value),
        ):
            visit(child)

    roots = [name for name in listed if not parents.get(name)]
    for root in sorted(roots, key=lambda value: (-inclusive.get(value, 0), value)):
        visit(root)
    return rows


def format_class_count_rows(counts: dict[str, int]) -> list[str]:
    """Render hierarchy-aware dry-run rows without relying on indentation."""

    lines = []
    for row in class_count_rows(counts):
        relation = (
            f"; subclass of {row['parent_class']}; included in parent total"
            if row["parent_class"]
            else ""
        )
        lines.append(
            f"    {row['antimicrobial_class']:26s} "
            f"inclusive={row['records_including_subclasses']:>6d} "
            f"direct={row['records_direct']:>6d}{relation}"
        )
    return lines


# ARO writes its own cross-reference prefixes; ChEBI's are already bioregistry
# prefixes and pass through unchanged. Anything not listed and not already
# lowercase-bioregistry-shaped is dropped rather than guessed — an unregistered
# prefix does not resolve, and a CURIE that resolves nowhere is worse than none.
XREF_PREFIX = {
    "PubChem": "pubchem.compound",
    "ChEMBL": "chembl",
    "CAS": "cas",
    "CHEBI": "CHEBI",
    "ARO": "ARO",
    # ChEBI files its FooDB links as foods, but every accession it carries is
    # FDB-prefixed, which is FooDB's COMPOUND namespace; the food namespace is
    # FOOD-prefixed. Linked as foods, all 51 went to a 404 page.
    "foodb.food": "foodb.compound",
}

# Namespaces that do NOT identify a chemical structure, and so cannot mean "the
# same structure" — the contract `xrefs` states in docs/CURATION.md and the
# schema. A PDB accession identifies a macromolecular STRUCTURE ENTRY: 1H8S is an
# anti-ampicillin antibody complex and 1Q3W a human GSK3beta-alsterpaullone
# complex, so listing them as chemical equivalents of ampicillin and
# alsterpaullone asserts something no source claims. `pdb-ccd` is different — it
# identifies a ligand chemical component — and stays.
#
# They are no longer DISCARDED, which was the same "moved, not deleted" mistake
# #136 records for patent and wikipedia.en xrefs. They now go to
# `structural_observations`, where a PDB accession means what it actually means:
# a macromolecular structure was solved containing this compound. What the
# macromolecule IS stays UNREVIEWED until a curator says so, because that is the
# claim the xref was silently making and could not support (#95).
NON_STRUCTURE_XREF_PREFIXES = {"pdb", "PDB"}

# Namespaces whose accessions are DOCUMENTS or ARTICLES rather than structure
# identifiers — a patent covers a class of compounds, an encyclopedia article
# covers a topic. By the argument that removed `pdb:`, they do not belong in a
# field defined as "the same structure", and patent:WO2011108759 really does sit
# on ametoctradin and silthiofam, two unrelated fungicides.
#
# They are KEPT, in `document_xrefs`. Dropping them was tried and measuring
# said it was the wrong remedy: nearly every one of them maps to exactly ONE
# structure here, so removing them would have cost far more useful links than
# false equivalences. Issue #92 asked for such identifiers to be MOVED out of
# chemical xrefs rather than deleted; `document_xrefs` is that destination (#136).
DOCUMENT_XREF_PREFIXES = {"patent", "wikipedia.en"}

# Namespaces that identify a DRUG rather than an exact structure, so one
# accession legitimately spans a parent compound and its salts and stereoisomers
# — drugbank:DB00639 covers butoconazole, butoconazole nitrate and both
# enantiomers. Kept for their utility, in `drug_xrefs`, so what the field means
# is visible on the record rather than declared in a constant. See #134.
# `unii` was here and is not: the corpus contains ZERO unii xrefs, so declaring
# a granularity exception for it was speculation dressed as documentation, and
# the grounding check skipped it silently because a prefix that never appears
# cannot be shown to span anything. If UNII xrefs arrive and do span structures,
# the no-accession-spans-two-structures invariant catches them then, which is
# the right time.
DRUG_GRANULARITY_XREF_PREFIXES = {"drugbank", "kegg.drug", "drugcentral"}

# Namespaces where one value identifies one substance, so two sources offering
# DIFFERENT values for the same record contradict each other. CARD gave cefdinir
# iclaprim's CAS and ChEMBL id verbatim (#163) -- a copy-paste in the upstream
# row, published here as a same-substance claim between a cephalosporin and a
# diaminopyrimidine. Publishing both values asserts they are one compound.
#
# The contested value is WITHHELD, not adjudicated: ChEBI leads on identity here
# (the same rule the record's own identifier follows), so the ARO-supplied value
# is the one held back and surfaced for a curator. Four records are affected and
# only cefdinir's is an upstream error -- cycloheximide and framycetin carry
# genuine alternate registrations for the same compound. Withholding is right in
# all three cases for the same reason: the corpus should not publish an
# equivalence its own sources disagree about.
CONTESTABLE_XREF_PREFIXES = {"cas", "chembl"}


def contested_xrefs(group: list) -> set[str]:
    """Values in a single-substance namespace that the sources disagree about."""
    by_namespace: dict[str, dict[str, set[str]]] = {}
    for concept in group:
        for xref in concept.xrefs:
            namespace = xref.split(":", 1)[0].lower()
            if namespace in CONTESTABLE_XREF_PREFIXES:
                by_namespace.setdefault(namespace, {}).setdefault(concept.source, set()).add(xref)
    contested: set[str] = set()
    for per_source in by_namespace.values():
        grounding = per_source.get("CHEBI", set())
        offered = per_source.get("ARO", set())
        if grounding and offered and not (grounding & offered):
            contested |= offered
    return contested

# Where each namespace's accession goes. `xrefs` means the same structure;
# the two named sets mean something else and get their own slots, so the
# exception is a field a consumer can see rather than a constant they have
# to know about (#134, #136).
def xref_slot(xref: str) -> str:
    prefix = xref.split(":", 1)[0]
    if prefix in DRUG_GRANULARITY_XREF_PREFIXES:
        return "drug_xrefs"
    if prefix in DOCUMENT_XREF_PREFIXES:
        return "document_xrefs"
    return "xrefs"


# A structure-exact accession published on two different InChIKeys names at
# most one of them, and the corpus cannot tell which: cas:69388-84-7 sits on
# sulbactam and sulbactam sodium, and chembl:CHEMBL1999880 on narbomycin and
# nybomycin, two unrelated antibiotics. A "known coarse" constant used to
# DECLARE such namespaces and let the accessions through, which turned a
# defect into a listed exception nobody triaged (#137). They are now withheld
# from every record they span and reported, so a curator can put each one back
# on the record it actually names. Structure-exact namespaces only: a DrugBank
# id spanning a salt and its parent is that namespace's meaning, not an error.
REFUSED_SPANNING_XREFS: list[tuple[str, str, str]] = []


def spanning_accessions(pairs) -> dict[str, set[str]]:
    """Structure-exact accessions that land on more than one InChIKey.

    `pairs` yields (standard_inchi_key, xref). One function for the seeder and
    the worklist queue that reports what it withheld, so the two cannot drift.
    """
    keys: dict[str, set[str]] = {}
    for key, xref in pairs:
        if key and xref_slot(xref) == "xrefs":
            keys.setdefault(xref, set()).add(key)
    return {xref: found for xref, found in keys.items() if len(found) > 1}


def gate_xrefs(xrefs, *, own_key: str, own_names: set[str], broader: set[str],
               contested: set[str], chebi_keys: dict[str, str],
               chebi_name_index: dict[str, set[str]], refused: list,
               identity: tuple[str, str]) -> list[str]:
    """The per-record cross-reference gate, in the order the rules apply.

    One function, because the worklist queue that reports what the corpus-wide
    spanning pass withheld has to know what reached that pass -- and a queue
    that restated these rules from the inventory rows listed CHEBI:8309 on
    polymyxin B2, where rule 2 had already refused it as a known different
    structure. Restating a gate is how #226 and #250 happened; calling it is
    the fix.
    """
    identifier, label = identity
    kept = []
    for x in xrefs:
        if (x.split(":", 1)[0] in NON_STRUCTURE_XREF_PREFIXES
                or x in broader or x in contested):
            continue
        if own_key and chebi_keys.get(x) and chebi_keys[x] != own_key:
            continue
        if x.startswith("CHEBI:"):
            reason = structureless_xref_conflict(
                own_names, x, chebi_keys.get(x, ""), chebi_name_index.get(x, set()))
            if reason:
                refused.append((identifier, label, reason))
                continue
        kept.append(x)
    return kept


def withhold_spanning_xrefs(records: dict[str, dict]) -> int:
    """Strip every structure-exact accession that spans two structures."""
    spanning = spanning_accessions(
        ((r.get("chemical_structure") or {}).get("standard_inchi_key"), x)
        for r in records.values() for x in (r.get("xrefs") or []))
    if not spanning:
        return 0
    # Records are named by identifier AND label: two records can share a label
    # (triflumizole is both CHEBI:81784 and a minted ARO record), and naming
    # them by label alone produced "also published on ." in the report.
    names: dict[str, set[str]] = {}
    for identifier, record in records.items():
        for xref in record.get("xrefs") or []:
            if xref in spanning:
                names.setdefault(xref, set()).add(f"{record.get('label', '')} ({identifier})")
    withheld = 0
    for identifier, record in records.items():
        kept = [x for x in (record.get("xrefs") or []) if x not in spanning]
        for xref in (record.get("xrefs") or []):
            if xref in spanning:
                namespace = xref.split(":", 1)[0]
                others = sorted(names[xref] - {f"{record.get('label', '')} ({identifier})"})
                REFUSED_SPANNING_XREFS.append((
                    identifier, record.get("label", ""),
                    f"{xref} is also published on {', '.join(others)}. A {namespace} "
                    "accession names one substance, so it belongs to at most one of "
                    "these records and the corpus cannot tell which. Withheld from all "
                    "of them."))
                withheld += 1
        if kept:
            record["xrefs"] = kept
        else:
            record.pop("xrefs", None)
    return withheld


CURIE_LOCAL = re.compile(r"^[A-Za-z0-9._-]+$")
BIOREGISTRY_PREFIX = re.compile(r"^[a-z][a-z0-9._-]*$")

# Fields the seeder owns end to end. Everything else on a record belongs to a
# curator and must survive a re-seed untouched — `verify_corpus.py` imports this
# list so "what the seeder owns" has exactly one definition.
SEEDED_FIELDS = [
    "identifier", "label", "definition", "definition_source", "synonyms",
    "parent_compounds", "xrefs", "drug_xrefs", "document_xrefs",
    "antimicrobial_class", "activity_roles",
    "structural_class", "structural_class_id", "chemical_structure",
    "source_concepts", "grounding_status",
]

# Curator-owned fields. A re-seed copies these forward verbatim from the record
# on disk, so `just seed-apply` after months of curation is a safe operation
# rather than a way to lose all of it.
CURATOR_FIELDS = [
    "curation_status", "grounding_notes", "evidence",
    "cidality", "biosynthesis_origin",
    "activity_spectrum", "causal_graphs", "datasets",
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


@lru_cache(maxsize=1)
def load_role_names() -> dict[str, str]:
    """Role CURIE -> label, for citing a role by name rather than by number."""
    path = RAW_DIR / "chebi_role_names.tsv"
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["role_id"]: r["name"] for r in csv.DictReader(fh, delimiter="\t")}


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
                 "structural_class_id", "minted", "mechanism_roles", "aro_parents",
                 "antimicrobial_class", "source_version", "evidence")

    def __init__(self, source, source_id, label):
        self.source = source
        self.source_id = source_id
        self.label = label
        self.definition = ""
        self.definition_refs: list[str] = []
        self.roles: list[str] = []
        self.parents: list[str] = []
        # ARO's own parent_ids column. Kept apart from `parents`, which feeds the
        # record's `parent_compounds` and for an ARO concept means its drug class;
        # these are classification terms, not broader compounds.
        self.aro_parents: list[str] = []
        self.xrefs: list[str] = []
        self.synonyms: list[tuple[str, str]] = []
        self.structure: dict = {}
        self.structural_class = ""
        self.structural_class_id = ""
        self.mechanism_roles: list[str] = []
        self.antimicrobial_class = ""
        self.source_version = ""
        self.evidence: list[dict] = []
        self.minted = ""


def normalize_xref(raw: str) -> str | None:
    """`PubChem:12560` -> `pubchem.compound:12560`; `chembl:CHEMBL532` passes through."""
    if ":" not in raw:
        return None
    prefix, local = raw.split(":", 1)
    local = local.strip()
    mapped = XREF_PREFIX.get(prefix)
    if prefix == "foodb.food" and not local.startswith("FDB"):
        # The remap rests on the FDB pattern. A FOOD-prefixed id would be a
        # food, and filing it as a compound would be the same mislabel the
        # other way round; leave it unmapped so the undeclared prefix fails
        # validation and someone looks.
        mapped = None
        return None
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


def structure_from_curator(row: dict) -> dict:
    out = {
        "smiles": row["smiles"],
        "standard_inchi": row["standard_inchi"],
        "standard_inchi_key": row["standard_inchi_key"],
        "molecular_formula": row.get("molecular_formula", ""),
        "structure_source": row["structure_source"],
        "retrieved_on": row["structure_retrieved_on"],
    }
    out.update(_numeric_fields(row, charge_via_float=False))
    return {k: v for k, v in out.items() if v not in ("", None)}


CURATOR_ANTIBIOTIC_COLUMNS = [
    "source_id", "label", "antimicrobial_class", "smiles", "standard_inchi",
    "standard_inchi_key", "structure_source", "structure_retrieved_on",
    "source_version", "reference", "evidence_snippet", "evidence_notes",
    "definition", "activity_roles", "synonyms", "xrefs", "molecular_formula",
    "charge", "average_mass", "monoisotopic_mass",
]
STABLE_CURATOR_REFERENCE = re.compile(r"^(DOI:10\.\S+|https://\S+)$", re.I)


def load_curator_concepts(path: Path = CURATOR_ANTIBIOTICS_PATH) -> list[Concept]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != CURATOR_ANTIBIOTIC_COLUMNS:
            raise SystemExit(
                f"{path} columns are {reader.fieldnames}; expected "
                f"{CURATOR_ANTIBIOTIC_COLUMNS}"
            )
        rows = list(reader)

    concepts = []
    seen_source_ids: set[str] = set()
    seen_inchikeys: dict[str, str] = {}
    for lineno, row in enumerate(rows, 2):
        if not any(row.values()):
            continue
        required = [
            "source_id", "label", "antimicrobial_class", "smiles", "standard_inchi",
            "standard_inchi_key", "structure_source", "structure_retrieved_on",
            "source_version", "reference", "molecular_formula", "charge",
        ]
        missing = [field for field in required if not row.get(field)]
        if missing:
            raise SystemExit(f"{path}:{lineno} missing required field(s): {', '.join(missing)}")
        if row["source_id"] in seen_source_ids:
            raise SystemExit(f"{path}:{lineno} duplicates source_id {row['source_id']!r}")
        seen_source_ids.add(row["source_id"])
        previous_inchikey = seen_inchikeys.setdefault(row["standard_inchi_key"], row["source_id"])
        if previous_inchikey != row["source_id"]:
            raise SystemExit(
                f"{path}:{lineno} duplicates Standard InChIKey "
                f"{row['standard_inchi_key']} from {previous_inchikey!r}"
            )
        if row["antimicrobial_class"] not in CLASS_DIRS:
            raise SystemExit(
                f"{path}:{lineno} has unknown antimicrobial_class "
                f"{row['antimicrobial_class']!r}"
            )
        if not STABLE_CURATOR_REFERENCE.fullmatch(row["reference"]):
            raise SystemExit(
                f"{path}:{lineno} reference must be DOI:10... or a stable https:// URL"
            )
        if not STABLE_CURATOR_REFERENCE.fullmatch(row["source_id"]):
            raise SystemExit(
                f"{path}:{lineno} source_id must be DOI:10... or a stable https:// URL"
            )
        if not STABLE_CURATOR_REFERENCE.fullmatch(row["structure_source"]):
            raise SystemExit(
                f"{path}:{lineno} structure_source must be DOI:10... or a stable https:// URL"
            )

        concept = Concept("CURATOR", row["source_id"], row["label"])
        concept.definition = row.get("definition", "")
        concept.roles = split_pipe(row.get("activity_roles", ""))
        concept.synonyms = [(text, "EXACT_SYNONYM")
                            for text in split_pipe(row.get("synonyms", ""))]
        xrefs = []
        for raw in split_pipe(row.get("xrefs", "")):
            xref = normalize_xref(raw)
            if xref is None:
                raise SystemExit(f"{path}:{lineno} has invalid xref {raw!r}")
            xrefs.append(xref)
        concept.xrefs = xrefs
        concept.structure = structure_from_curator(row)
        concept.antimicrobial_class = row["antimicrobial_class"]
        concept.source_version = row["source_version"]
        evidence = {"reference": row["reference"]}
        if row.get("evidence_snippet"):
            evidence["snippet"] = row["evidence_snippet"]
        if row.get("evidence_notes"):
            evidence["notes"] = row["evidence_notes"]
        concept.evidence = [evidence]
        concepts.append(concept)
    return concepts


def classify(roles: list[str], conf: dict, from_aro: bool,
             aro_class_ids: tuple[str, ...] = (),
             aro_ids: tuple[str, ...] = (),
             aro_parent_ids: tuple[str, ...] = ()) -> str:
    """Assign the filesystem/reporting class.

    Order of evidence, strongest first:

    1. **A CARD drug class whose name states a target group** — "triazole
       antifungal", "polyene antifungal". Compound-specific and curated, so it
       outranks a generic role tag: ChEBI gives fluconazole and amphotericin B an
       `antibacterial agent` role, and taking that at face value filed both as
       antibacterials.
    2. **ChEBI roles**, by the priority table in conf/sources.yaml (narrower
       target group first, bacteria before fungi and protozoa).
    3. **A curated adjudication of CARD's own definition**
       (`aro_definition_overrides`), for the ARO concepts the blanket fallback
       would misfile; each entry quotes the phrase it rests on. Per-compound, so
       it comes before any bucket the compound sits in. Triflumizole, "used as a
       fungicide", was filed ANTIBACTERIAL while its own ChEBI-grounded twin was
       ANTIFUNGAL, so one compound sat under two classes.
    4. **A group-naming CARD term** (`aro_group_terms`) — a drug class
       ("disinfecting agents and antiseptics") or a parent ("antifungal without
       defined classification"), matched at this tier and NOT at step 1. Above
       the roles, the antifungal parent refiled pyrimethamine, an antimalarial,
       and the antiseptic class made BIOCIDE outrank an antibacterial role for
       five compounds — reversing a priority conf/sources.yaml argues for
       explicitly. A default, never an override.
    5. **The ARO fallback**, ANTIBACTERIAL — for a CARD molecule with none of
       the above. Right for 255 of the 276 records it reaches.

    Step 3 is a CURATED MAP, not a text rule, and the distinction is the whole
    point: a regex for "fungal" flags ophiobolin A, whose definition reads
    "isolated as fungal phytotoxins" — a fungal PRODUCT with no antimicrobial
    target claim. The pattern cannot tell a target from a source, so it only
    surfaces candidates on `just worklist --queue aro-class`.

    A fourth step, filing on a ChEBI structural class whose name states a target
    group, was tried and removed: a chemical class is not a target claim, and it
    filed chemotherapy drugs, an insecticide and bare ring scaffolds as
    antibacterial. See conf/sources.yaml. Compounds whose only reviewed role is
    the generic `antimicrobial agent` keep ANTIMICROBIAL_UNSPECIFIED, which is
    what the sources say.

    Classes whose names do not state a group are absent from the map on purpose;
    see conf/sources.yaml.
    """
    # Drug class before parents: the more specific term wins when both are
    # mapped. A ChEBI role still outranks both, which is what keeps pyrimethamine
    # ANTIPROTOZOAL despite CARD filing it under an antifungal parent.
    class_map = conf.get("aro_class_to_class") or {}
    for term in aro_class_ids:
        if term in class_map:
            return class_map[term]

    mapping = conf["role_to_class"]
    best = None
    for role in roles:
        entry = mapping.get(role)
        if entry and (best is None or entry["priority"] < best["priority"]):
            best = entry
    if best:
        return best["class"]

    if from_aro:
        # PER-COMPOUND FIRST. A definition adjudication is about this compound; a
        # group term is about a bucket it sits in. Reversing these would let
        # ARO:3009165 ("antifungal without defined classification") overturn an
        # adjudication made by reading the compound's own definition — an
        # ordering that would pass every gate while quietly outranking the more
        # specific evidence.
        overrides = conf.get("aro_definition_overrides") or {}
        for aro_id in aro_ids:
            if aro_id in overrides:
                return overrides[aro_id]

        # Then a group-naming ARO term, drug class or parent. Below the roles on
        # purpose: at step 1 the antifungal parent refiled pyrimethamine, an
        # antimalarial, and the antiseptic drug class made BIOCIDE outrank the
        # antibacterial role for five compounds — reversing a priority this conf
        # argues for explicitly.
        group_terms = conf.get("aro_group_terms") or {}
        for term in (*aro_class_ids, *aro_parent_ids):
            if term in group_terms:
                return group_terms[term]
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
        concept.mechanism_roles = split_pipe(row.get("mechanism_role_ids", ""))
        concepts.append(concept)

    refused: list[tuple[str, str]] = []
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
        concept.aro_parents = split_pipe(row["parent_ids"])
        chebi_id = next((x for x in split_pipe(row["xrefs"]) if x.startswith("CHEBI:")), "")
        chebi_row = chebi_rows.get(chebi_id)
        conflict = crossref_conflict(row, chebi_row) if chebi_row else ""
        if conflict:
            refused.append((row["aro_id"], conflict))
            # Not trusted, so it grants nothing: no roles, no structure, and --
            # by dropping the xref -- no EXACT grounding either, since
            # resolve_identity reads the same list.
            #
            # `chebi_id` comes from the RAW inventory row while concept.xrefs
            # holds normalized values, so comparing them directly coupled this
            # to normalize_xref happening to leave ChEBI ids alone. It does
            # today; nothing enforced it, and if that changed the drop became a
            # silent no-op that re-granted EXACT grounding to the very entry the
            # gate had just refused (#168). Both sides are normalized here.
            refused_xref = normalize_xref(chebi_id)
            chebi_row = None
            concept.xrefs = [x for x in concept.xrefs
                             if normalize_xref(x) != refused_xref]
        # Roles and structure are independent facts about the cross-referenced
        # ChEBI entry. ChEBI can hold a compound with an antimicrobial role and
        # no default structure (miconazole, ketoconazole); reading the roles only
        # from the structure branch silently lost them and filed those compounds
        # under the ARO fallback class.
        if chebi_row:
            concept.roles = split_pipe(chebi_row["role_ids"])
            concept.mechanism_roles = split_pipe(chebi_row.get("mechanism_role_ids", ""))
        if chebi_row and chebi_row["standard_inchi_key"]:
            concept.structure = structure_from_chebi(chebi_row)
        elif row["aro_id"] in pubchem:
            concept.structure = structure_from_pubchem(pubchem[row["aro_id"]])
        concepts.append(concept)

    concepts.extend(load_curator_concepts())

    if refused:
        # A refusal can remove a record from the corpus. Every other consequential
        # decision in the run summary is counted; this one was silent, so a new
        # upstream conflict would drop a record during a routine re-seed with
        # nothing saying why (#170).
        print(f"  {len(refused)} CARD cross-reference(s) refused as self-contradictory "
              "(see `just worklist --queue crossref-conflict`)", file=sys.stderr)
        for aro_id, reason in refused:
            print(f"    {aro_id}: {reason}", file=sys.stderr)

    for concept in concepts:
        concept.minted = mint(concept.source, concept.source_id)
    return concepts, chebi_rows


# --------------------------------------------------------------------------
# CARD -> ChEBI cross-reference trust
# --------------------------------------------------------------------------

# An ARO row's CHEBI xref grants that ChEBI entry's roles, its structure AND
# EXACT identity to the ARO concept. Nothing asked whether the two rows describe
# the same substance, and CARD's do not always: ARO:3000337 "iclaprim" points at
# CHEBI:31724 "Isoaminile citrate", a 2-star entry ChEBI gives no antimicrobial
# role. The corpus published iclaprim's name over isoaminile citrate's structure,
# grounded EXACT, and every gate passed because the corpus faithfully reproduced
# a wrong input (#133).
#
# The gate is TWO INDEPENDENT IDENTIFIERS DISAGREEING. Either signal alone is
# useless here, measured against the committed inventories:
#
#   name disagreement alone  29 links, and nearly all are legitimate --
#                            rifampin/rifampicin, cefalexin/cephalexin,
#                            dactinomycin/actinomycin D, and systematic names
#                            such as hexaconazole / 2-(2,4-dichlorophenyl)-...
#   CAS disagreement alone    2 links, one of which is cycloheximide, where both
#                            rows mean the same compound and merely carry
#                            different registrations
#   BOTH                      1 link: iclaprim. No false positives.
#
# So a conflict is not "these look different" but "the two things CARD says
# about this compound contradict each other". The cross-reference is then not
# trusted for roles, structure or identity, and the concept falls back to
# PubChem enrichment and a minted identifier -- which is what CARD alone can
# support. The pair is surfaced on `just worklist --queue crossref-conflict`
# rather than dropped silently. That queue recomputes from the inventories and
# needs no state from a seeder run, so nothing is accumulated here: a module-level
# list that is written and never read is a decoy pointing at the wrong mechanism
# (#169).


# The accession shape the schema enforces on StructuralObservation.structure_id.
# Defined once and asserted equal to the schema's pattern by a test, so the
# migration and the validator cannot drift apart (#174).
STRUCTURE_ID_PATTERN = r"^(PDB:[0-9][A-Za-z0-9]{3}|EMDB:EMD-[0-9]{4,5})$"

# Read by the run summary and CLEARED at the start of every merge. A
# module-level list that is written and never read, or never reset, is the
# defect #169 records; this one is both read and reset, deliberately.
def xref_names(row: dict) -> set[str]:
    """Every name a ChEBI inventory row answers to, normalized for comparison.

    The inventory encodes synonyms as `TYPE=value` — `UNIPROT NAME=gentamicin C`,
    `IUPAC NAME=...`, `SYNONYM=Neomycin`. Comparing the raw strings makes every
    synonym unmatchable, which would have refused `gentamicin C -> CHEBI:75616`
    on the grounds that no name matched, while the target's own UniProt synonym
    IS that name. Refusing on a parsing failure is not refusing on evidence.
    """
    values = [row.get("name") or ""]
    for raw in (row.get("synonyms") or "").split("|"):
        values.append(raw.split("=", 1)[1] if "=" in raw else raw)
    return {" ".join(v.lower().split()) for v in values} - {""}


def structureless_xref_conflict(record_names: set[str], chebi_id: str,
                                target_key: str, target_names: set[str]) -> str | None:
    """Why a same-structure xref to a STRUCTURELESS ChEBI term cannot stand (#164).

    The structure gate below compares InChIKeys, which needs a structure on both
    sides. When the target has none the comparison is skipped, and the xref is
    published unexamined -- so the check does nothing on exactly the inputs most
    likely to be wrong. That is how `cefdinir -> CHEBI:131724`, which is
    *iclaprim*, an unrelated antibacterial, survived every gate.

    But "cannot compare structures" is not "no evidence". The inventory knows the
    target's NAME even when it has no structure, and a name is weak evidence of
    sameness that is nonetheless conclusive evidence of DIFFERENCE when nothing
    matches: neither the record's label nor any of its synonyms appears anywhere
    among the target's names. That is a positive contradiction, not an absence.

    So this refuses on evidence, never on ignorance. A target absent from the
    inventory, or present with no name, is still unverifiable and still kept and
    queued -- dropping a source assertion because we cannot check it stays the
    worse error. Only a NAMED, structureless, wholly non-matching target is
    refused, and the refusal is reported rather than silent.
    """
    if target_key:
        return None                       # comparable: the structure gate owns it
    if not target_names:
        return None                       # unknown or unnamed: genuinely unverifiable
    if record_names & target_names:
        return None
    return (f"{chebi_id} has no structure in the committed inventory, so the "
            f"same-structure gate cannot compare it; and none of its names "
            f"({', '.join(sorted(target_names)[:3])}) matches this record's "
            f"label or synonyms. Not published as an equivalence.")


REFUSED_STRUCTURELESS_XREFS: list[tuple[str, str, str]] = []
MALFORMED_STRUCTURE_IDS: list[tuple[str, str]] = []

# Sources the seeder itself writes structural observations for. Anything else on
# a record belongs to a curator and is not the seeder's to reproduce (#173).
SEEDER_STRUCTURE_SOURCES = {"CHEBI", "ARO"}


def structural_observations(group: list, source_version: str,
                            retrieved_on: str) -> list[dict]:
    """PDB accessions a source attached to this compound, as what they are.

    Migrated rather than dropped, and deliberately NOT classified: `relevance`
    is UNREVIEWED and `evidence_status` says a primary citation is needed. The
    method, resolution and publication are not in any committed inventory — they
    need RCSB, which is a networked fetch this offline step does not make. So the
    record says a structure exists and says nothing it cannot support.
    """
    out: list[dict] = []
    seen: set[str] = set()
    for concept in group:
        for xref in concept.xrefs:
            namespace, _, accession = xref.partition(":")
            if namespace.lower() != "pdb" or not accession:
                continue
            structure_id = f"PDB:{accession.upper()}"
            if not re.fullmatch(STRUCTURE_ID_PATTERN, structure_id):
                # Skipped, not emitted. write_validated_antibiotic validates the
                # WHOLE record, so one malformed upstream accession would make an
                # otherwise good compound unwritable — a whole record lost to a
                # source typo (#174).
                MALFORMED_STRUCTURE_IDS.append((concept.source_id, xref))
                continue
            if structure_id in seen:
                continue
            seen.add(structure_id)
            out.append({
                "structure_id": structure_id,
                "relevance": "UNREVIEWED",
                "evidence_status": "PRIMARY_EVIDENCE_NEEDED",
                "source": concept.source,
                "source_version": source_version,
                **({"retrieved_on": retrieved_on} if retrieved_on else {}),
            })
    return sorted(out, key=lambda item: item["structure_id"])


def seeded_structural_view(record: dict) -> set[str]:
    """The structure accessions the seeder owns, ignoring curated judgement.

    NOT in SEEDED_FIELDS, deliberately. The seeder emits every observation as
    UNREVIEWED, and a curator establishing that PDB:1H8S is an ANTIBODY_COMPLEX
    is the entire point of the field — an exact comparison would make the first
    correct curation look like drift. What must reproduce is WHICH structures are
    asserted and by whom: an accession cannot be invented by hand, and a seeded
    one cannot quietly disappear.
    """
    return {f"{item.get('structure_id')}|{item.get('source')}"
            for item in (record.get("structural_observations") or [])
            if item.get("source") in SEEDER_STRUCTURE_SOURCES}


def _cas_numbers(raw: str) -> set[str]:
    """CAS values, ignoring empty ones.

    A bare `CAS:` with no number yielded {""} — a truthy set holding nothing,
    which made "this row has a CAS" true and could fire the gate against a row
    that supplies no registry number at all.
    """
    return {value for value in (v.split(":", 1)[1] for v in split_pipe(raw or "")
                                if v.split(":", 1)[0].lower() == "cas") if value.strip()}


def _comparable_name(label: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (label or "").lower())


def crossref_conflict(aro_row: dict, chebi_row: dict) -> str:
    """Why CARD's link to this ChEBI entry cannot be trusted, or "" when it can.

    Containment, not equality, decides the name test: "polymyxin B" against
    "polymyxin B1" and "gentamicin A" against "gentamycin A" are the same
    compound named at different precision, and flagging those would be noise.
    """
    aro_name = _comparable_name(aro_row.get("name"))
    chebi_name = _comparable_name(chebi_row.get("name"))
    if not (aro_name and chebi_name) or aro_name in chebi_name or chebi_name in aro_name:
        return ""
    aro_cas = _cas_numbers(aro_row.get("xrefs"))
    chebi_cas = _cas_numbers(chebi_row.get("xrefs"))
    if not (aro_cas and chebi_cas) or (aro_cas & chebi_cas):
        return ""
    return (f"CARD links {aro_row['aro_id']} ({aro_row['name']}) to "
            f"{chebi_row['chebi_id']} ({chebi_row['name']}), but the names differ "
            f"and the CAS numbers disagree "
            f"({sorted(aro_cas)[0]} vs {sorted(chebi_cas)[0]}). "
            "Cross-reference not trusted for roles, structure or identity.")


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


def read_retired() -> dict[str, str]:
    """Identifier -> slug for records that have left the corpus.

    A slug is a published URL. When a record drops out — 134 did when unreviewed
    ChEBI relations stopped being trusted, 19 of which later returned — its row
    leaves PATHS.tsv, and without
    this ledger the string is free for the next compound whose label happens to
    slugify the same way, silently repointing a published URL at a different
    structure. The ledger keeps every retired slug reserved, and hands it back to
    its original identifier if that compound is ever re-admitted.
    """
    if not RETIRED_FILE.exists():
        return {}
    with RETIRED_FILE.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["slug"] for r in csv.DictReader(fh, delimiter="\t")}


def assign_slugs(records: dict[str, dict], lockfile: dict[str, str],
                 retired: dict[str, str] | None = None) -> dict[str, str]:
    """Identifier -> slug, honouring the committed lockfile and the retired ledger.

    Slugs are corpus-wide and published in URLs, so an existing assignment is
    never silently changed here: edit PATHS.tsv and re-seed. A retired slug is
    never reissued to a different compound, and a returning compound reclaims
    the slug it had.
    """
    retired = read_retired() if retired is None else retired
    assigned = dict(lockfile)
    already = set(assigned.values())
    for identifier, slug in retired.items():
        if slug in already:
            continue  # the slug has been taken by another record since retirement
        if identifier in records and identifier not in assigned:
            assigned[identifier] = slug
    taken = set(assigned.values()) | set(retired.values())
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

    # A slug is a published URL and must name exactly one record. The reclaim
    # path above and a hand-edited PATHS.tsv can each introduce a duplicate, and
    # two records in one class directory would silently overwrite each other.
    counts: dict[str, list[str]] = defaultdict(list)
    for identifier, slug in assigned.items():
        counts[slug].append(identifier)
    clashes = {slug: ids for slug, ids in counts.items() if len(ids) > 1}
    if clashes:
        raise SystemExit(
            "slug collision: " + "; ".join(f"{slug} -> {sorted(ids)}" for slug, ids in
                                           sorted(clashes.items()))
            + ". A slug names one record; fix data/antibiotics/PATHS.tsv or RETIRED.tsv."
        )
    return assigned


def merge(concepts: list[Concept], chebi_rows: dict[str, dict], conf: dict,
          decisions: dict[str, dict], source_version: str) -> tuple[dict[str, dict], list[Concept]]:
    """Group concepts into records. Returns (records, skipped-for-no-structure)."""
    MALFORMED_STRUCTURE_IDS.clear()
    REFUSED_STRUCTURELESS_XREFS.clear()
    REFUSED_SPANNING_XREFS.clear()
    # InChIKey per ChEBI id, from the committed inventory. The same-structure
    # gate on xrefs uses it; a ChEBI term with no structure here is simply not
    # comparable, and its xrefs are kept and queued rather than dropped.
    chebi_keys = {cid: row["standard_inchi_key"]
                  for cid, row in chebi_rows.items() if row.get("standard_inchi_key")}
    # Names for every inventory term, structureless ones included -- those are
    # precisely the terms the key map cannot speak for (#164).
    chebi_name_index = {cid: xref_names(row) for cid, row in chebi_rows.items()}
    by_identity: dict[str, list[Concept]] = defaultdict(list)
    grounding: dict[str, str] = {}
    skipped: list[Concept] = []
    overridden: set[str] = set()

    for concept in concepts:
        decision = decisions.get(concept.minted, {})
        if (decision.get("decision") or "").upper() == "EXCLUDE":
            continue
        override = (decision.get("identifier") or "").strip()
        # The override is consulted BEFORE the structure gate, and the grounding
        # target lends its structure. A curator working the no-structure queue —
        # the largest backlog, and the population GROUND exists for — would
        # otherwise write a decision that the gate discarded before it was ever
        # read, silently and with the concept back on the queue next run.
        if override and not concept.structure.get("standard_inchi_key"):
            target = chebi_rows.get(override, {})
            if target.get("standard_inchi_key"):
                concept.structure = structure_from_chebi(target)
                if not concept.roles:
                    concept.roles = split_pipe(target.get("role_ids", ""))
            else:
                print(f"  decision on {concept.minted} grounds {concept.label!r} to "
                      f"{override}, which has no structure either; not written",
                      file=sys.stderr)
        if not concept.structure.get("standard_inchi_key"):
            skipped.append(concept)
            continue
        identifier, status = resolve_identity(concept, chebi_rows)
        if override:
            # The override sets identity, so it is validated rather than trusted.
            # Identifier, structure and merge key are three separate values here,
            # and every way they can disagree has to be refused explicitly: an
            # earlier version only caught the case where both structures were
            # present and differed, which let a typo'd CURIE and a structureless
            # class term through in silence.
            target = chebi_rows.get(override)
            concept_key = concept.structure.get("standard_inchi_key", "")
            if not override.startswith("CHEBI:"):
                # Only ChEBI targets can be checked: chebi_rows is the only
                # inventory carrying an identifier-to-structure mapping. An
                # unvalidatable override is refused rather than trusted — it
                # would stamp grounding_status EXACT against a target nothing
                # confirmed exists, on a path where the disagreement between
                # identifier and structure is not merely unchecked but
                # uncheckable.
                raise SystemExit(
                    f"decision on {concept.minted} grounds {concept.label!r} to {override}, "
                    f"which is not a ChEBI CURIE. Grounding targets must be ChEBI entries, "
                    f"because that is the only inventory this repository can check a "
                    f"structure against."
                )
            if True:
                if target is None:
                    raise SystemExit(
                        f"decision on {concept.minted} grounds {concept.label!r} to {override}, "
                        f"which is not a ChEBI entry in data/raw/chebi_antimicrobials.tsv. "
                        f"Check the CURIE in curation/decisions.tsv — a typo here mints a "
                        f"record keyed to a compound that does not exist."
                    )
                target_key = target.get("standard_inchi_key", "")
                if not target_key:
                    raise SystemExit(
                        f"decision on {concept.minted} grounds {concept.label!r} to {override}, "
                        f"a ChEBI term with no structure of its own — a class term, not a "
                        f"compound. A record is one chemical structure and a drug class is "
                        f"never a record; ground to the structured entry instead."
                    )
                if concept_key and target_key != concept_key:
                    raise SystemExit(
                        f"decision on {concept.minted} grounds {concept.label!r} to {override}, "
                        f"but their structures differ ({concept_key} vs {target_key}). "
                        f"Fix the decision row in curation/decisions.tsv — a record must not be "
                        f"keyed to a compound whose structure it does not carry."
                    )
            overridden.add(override)
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

    # A curator decision must not split one structure across two grounded
    # records. The InChIKey fold only folds MINTED into EXACT, so an override
    # that creates a second EXACT identifier for a structure another record
    # already carries would pass every gate — flag_structure_collisions looks
    # only at all-MINTED groups.
    if overridden:
        owners: dict[str, list[str]] = defaultdict(list)
        for identifier, group in by_identity.items():
            if grounding.get(identifier) == "EXACT":
                owners[group[0].structure["standard_inchi_key"]].append(identifier)
        for inchikey, ids in sorted(owners.items()):
            if len(ids) > 1 and any(i in overridden for i in ids):
                raise SystemExit(
                    f"a decision grounds a concept to {sorted(i for i in ids if i in overridden)} "
                    f"while {sorted(i for i in ids if i not in overridden)} already carries "
                    f"structure {inchikey}. That would split one structure across two grounded "
                    f"records; ground to the existing identifier instead."
                )

    curator_collisions: dict[str, list[tuple[str, list[Concept]]]] = defaultdict(list)
    for identifier, group in by_identity.items():
        key = group[0].structure.get("standard_inchi_key", "")
        if key:
            curator_collisions[key].append((identifier, group))
    for key, owners in sorted(curator_collisions.items()):
        curator_rows = [
            concept.source_id
            for _, group in owners
            for concept in group
            if concept.source == "CURATOR"
        ]
        adopted_rows = [
            concept.source_id
            for _, group in owners
            for concept in group
            if concept.source in {"CHEBI", "ARO"}
        ]
        if curator_rows and adopted_rows:
            raise SystemExit(
                f"CURATOR source concept(s) {sorted(curator_rows)} duplicate adopted-source "
                f"structure {key} from {sorted(adopted_rows)}. Delete the curator row and "
                "curate the generated YAML record instead."
            )

    records: dict[str, dict] = {}
    for identifier, group in by_identity.items():
        records[identifier] = build_record(identifier, grounding[identifier], group,
                                           conf, source_version, chebi_keys,
                                           chebi_name_index)
    # Corpus-wide, because the property is corpus-wide: no record can know on
    # its own that another record carries the same CAS number.
    withhold_spanning_xrefs(records)
    return records, skipped


def _dedupe(values):
    seen, out = set(), []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


# A mode of action whose NAME carries a target group. When one of these lands on
# a record filed under a different group, the two fields are describing different
# activities of the same compound, and the record has to say so.
TARGET_BEARING_MODES = {
    "VIRAL_POLYMERASE_INHIBITION": "ANTIVIRAL",
    "VIRAL_PROTEASE_INHIBITION": "ANTIVIRAL",
    "VIRAL_INTEGRASE_INHIBITION": "ANTIVIRAL",
    "VIRAL_ENTRY_INHIBITION": "ANTIVIRAL",
    "VIRAL_RELEASE_INHIBITION": "ANTIVIRAL",
    "VIRAL_ASSEMBLY_INHIBITION": "ANTIVIRAL",
    "ERGOSTEROL_PATHWAY_INHIBITION": "ANTIFUNGAL",
    # Its only source roles are 1,3-beta-glucan synthase and chitin synthase,
    # both fungus-exclusive, even though the enum value itself is target-neutral.
    # THIS ENTRY IS CONDITIONAL ON THAT AND MUST BE REMOVED the day a bacterial
    # cell-wall role is mapped — penicillin-binding protein, D-Ala-D-Ala — or
    # every beta-lactam record will be told its mechanism belongs to an
    # antifungal activity.
    "CELL_WALL_SYNTHESIS_INHIBITION": "ANTIFUNGAL",
}


def _cross_activity_note(value: str, antimicrobial_class: str | None) -> str | None:
    """The caveat for a mechanism that belongs to another of the compound's
    activities — or to an activity no source has named."""
    implied = TARGET_BEARING_MODES.get(value)
    if not implied or not antimicrobial_class or implied == antimicrobial_class:
        return None
    if antimicrobial_class == "ANTIMICROBIAL_UNSPECIFIED":
        # "Two activities" would assert a second activity no source states. The
        # record simply has no target group, and this mechanism implies one.
        return (f"ChEBI asserts the role on the compound, and the mechanism implies an "
                f"{implied.lower().replace('anti', 'anti-')} target while the record has no "
                f"target group stated at all — evidence a curator can use to file it, not a "
                f"second activity.")
    return (f"ChEBI asserts the role on the compound, but this mechanism belongs to an "
            f"{implied.lower().replace('anti', 'anti-')} activity while the record is filed "
            f"as {antimicrobial_class}. Either the compound has both activities, or the "
            f"filing is wrong — the priority table has put azole antifungals under "
            f"ANTIBACTERIAL before now. A curator should decide which.")


def mode_of_action_from_roles(mechanism_roles: list[str], conf: dict,
                              role_names: dict[str, str],
                              antimicrobial_class: str | None = None
                              ) -> tuple[str, str, str] | None:
    """(mode_of_action, notes, target_scope) from ChEBI's mechanism roles, or None.

    This is a RESTATEMENT, not an inference. ChEBI asserting `protein synthesis
    inhibitor` as a role of a compound is a direct claim about what the compound
    does, and the map in conf/sources.yaml only translates that claim into the
    schema's vocabulary. That is what separates it from filing on a structural
    class, which was tried here and removed: a chemical class says what a
    compound IS, and its members are not all active on the named target.

    The residual limit is stated in the notes rather than papered over — the
    role names a MECHANISM, not the organism it acts on. Some compounds inhibit
    protein synthesis in eukaryotes; the mechanism claim still holds, the target
    organism is a separate question, and `molecular_targets` is where a curator
    answers it.

    Several distinct mechanisms give MULTIPLE, with every one named in the notes,
    rather than a silent pick.
    """
    mapping = dict(conf.get("role_to_mode_of_action", {}))
    # Roles whose target only exists in a eukaryotic microbe. A mitochondrial
    # mechanism is correct for a fungus and incoherent for a bacterium, so the
    # record's target group decides whether the role says anything at all.
    if antimicrobial_class in ("ANTIFUNGAL", "ANTIPROTOZOAL"):
        mapping.update(conf.get("role_to_mode_of_action_eukaryotic", {}))
    hits = {role: mapping[role] for role in mechanism_roles if role in mapping}
    if not hits:
        return None
    cited = ", ".join(f"{role} ({role_names.get(role, '?')})" for role in sorted(hits))
    values = sorted(set(hits.values()))

    # Whose target is it? MICROBIAL_TARGET if ANY contributing role names a
    # target the host lacks; HOST_SHARED_TARGET when none does. The question the
    # aggregate answers is "does this compound act on anything the host does not
    # have?", which is what makes it a usable filter: ciprofloxacin carries
    # `topoisomerase IV inhibitor` (bacteria-only) alongside the generic `DNA
    # synthesis inhibitor`, and marking it host-shared would put the most
    # selective antibacterial class there is on the wrong side of that filter.
    #
    # This was previously described as "a specific role outranks a generic one".
    # That was not the rule, only a coincidence of the ciprofloxacin case where
    # the specific role was also the microbial one. The azoles proved it: the
    # GENERIC pathway role beat the SPECIFIC enzyme role there, the same
    # sentence run backwards. The rule is presence, aggregated by ANY.
    #
    # `mode_of_action` means the mechanism of the ANTIMICROBIAL effect, and that
    # does not require a microbe-specific target: a host-directed antiviral
    # inhibits host translation the virus depends on. See #60 and #79.
    scope_map = conf.get("role_target_scope", {})
    unscoped = sorted(role for role in hits if role not in scope_map)
    if unscoped:
        # A mapped role with no scope would silently emit the safe-looking value.
        raise KeyError(
            f"role(s) {unscoped} map to a mode_of_action but have no entry in "
            "conf/sources.yaml role_target_scope")
    scope = ("MICROBIAL_TARGET"
             if any(scope_map[role] == "MICROBIAL_TARGET" for role in hits)
             else "HOST_SHARED_TARGET")

    # The caveat differs by scope, deliberately. A note identical on every record
    # carries no signal precisely because it is uniform (#60); this one says
    # which way the record leans and points at the field that records it.
    #
    # It is APPENDED to the cross-activity note rather than replacing it. Making
    # it the fallback left 18 records — every cross-activity and every MULTIPLE
    # one — carrying a scope value with no prose saying what it meant, which is
    # the uniform-note problem inverted: the records most in need of a caveat
    # were the ones that lost it.
    scope_caveat = (
        "The target it names is one the host has too, so the mechanism is true "
        "but is not evidence of selectivity — see mode_of_action_target_scope."
        if scope == "HOST_SHARED_TARGET" else
        "The role names a target specific to the microbe or virus — see "
        "mode_of_action_target_scope.")
    tail = f"ChEBI asserts the role on the compound. {scope_caveat}"

    if len(values) == 1:
        value = values[0]
        crossed_note = _cross_activity_note(value, antimicrobial_class)
        body = f"{crossed_note} {scope_caveat}" if crossed_note else tail
        return (value, f"{MOA_NOTE_MARKER} {cited}. {body} "
                       "Not a curator's mechanistic review.", scope)

    # The MULTIPLE branch needs the caveat too: a record can carry several
    # mechanisms and still have one of them belong to another activity.
    # Worth saying when the mechanisms sit on different sides of the host line:
    # the aggregate is still the honest answer to "acts on anything the host
    # lacks?", but a reader deciding which mechanism is primary needs to know
    # the choice moves the scope too.
    disagree = ("" if len({scope_map[role] for role in hits}) == 1 else
                " The contributing roles differ on whose target it is, so settling the "
                "primary mechanism may change mode_of_action_target_scope.")
    crossed = [v for v in values if _cross_activity_note(v, antimicrobial_class)]
    extra = ""
    if crossed:
        implied = sorted({TARGET_BEARING_MODES[v] for v in crossed})
        where = ("the record has no target group stated at all"
                 if antimicrobial_class == "ANTIMICROBIAL_UNSPECIFIED"
                 else f"the record is filed as {antimicrobial_class}")
        extra = (f" Note that {', '.join(crossed)} implies an "
                 f"{' or '.join(i.lower().replace('anti', 'anti-') for i in implied)} target while "
                 f"{where}.")
    return "MULTIPLE", (f"{MOA_NOTE_MARKER}s {cited}, which map to "
                        f"{', '.join(values)}. ChEBI asserts these roles on the compound; "
                        f"a curator should decide whether one is primary.{extra} "
                        f"{scope_caveat}{disagree} Not a curator's mechanistic review."), scope


def build_record(identifier: str, grounding_status: str, group: list[Concept],
                 conf: dict, source_version: str,
                 chebi_keys: dict[str, str] | None = None,
                 chebi_name_index: dict[str, set[str]] | None = None) -> dict:
    # InChIKey per ChEBI id, for the same-structure gate on xrefs below. Empty
    # when the caller has none: the gate then keeps every xref it cannot compare,
    # which is the behaviour it has for the majority anyway.
    chebi_keys = chebi_keys or {}
    chebi_name_index = chebi_name_index or {}

    # ChEBI leads on identity and structure; ARO leads on class and mechanism.
    chebi = [c for c in group if c.source == "CHEBI"]
    aro = [c for c in group if c.source == "ARO"]
    curator = [c for c in group if c.source == "CURATOR"]
    if curator and (chebi or aro):
        raise ValueError(
            f"{identifier} merges CURATOR source concepts into an existing "
            "adopted-source record; curate the existing YAML instead"
        )
    primary = (chebi or aro or curator)[0]

    roles = _dedupe(r for c in group for r in c.roles)
    explicit_classes = _dedupe(c.antimicrobial_class for c in curator if c.antimicrobial_class)
    if len(explicit_classes) > 1:
        raise ValueError(f"{identifier} has multiple CURATOR classes: {explicit_classes}")
    derived_class = classify(
        roles, conf, from_aro=bool(aro),
        aro_class_ids=tuple(c.structural_class_id for c in aro if c.structural_class_id),
        aro_ids=tuple(c.source_id for c in aro if c.source_id),
        aro_parent_ids=tuple(p for c in aro for p in (c.aro_parents or [])),
    )
    antimicrobial_class = explicit_classes[0] if explicit_classes else derived_class
    structural_class = next((c.structural_class for c in aro if c.structural_class), "")
    structural_class_id = next((c.structural_class_id for c in aro if c.structural_class_id), "")

    definition, definition_source = "", ""
    for concept in (chebi + aro + curator):
        if concept.definition:
            definition = concept.definition
            if concept.source == "ARO":
                definition_source = concept.definition_refs[0] if concept.definition_refs else "ARO"
            elif concept.source == "CURATOR":
                definition_source = concept.evidence[0]["reference"] if concept.evidence else "CURATOR"
            else:
                definition_source = "ChEBI"
            break

    # Upstream exact-synonym lists occasionally contain a different chemical
    # identity. Keep those adjudications in configuration so a re-extraction
    # cannot silently restore the bad identity assertion.
    synonym_exclusions = conf.get("synonym_exclusions") or {}
    synonyms = []
    seen_syn = {primary.label}
    for concept in group:
        for text, kind in concept.synonyms:
            if text in synonym_exclusions.get(concept.source_id, []):
                continue
            if text not in seen_syn:
                seen_syn.add(text)
                synonyms.append({"synonym_text": text, "synonym_type": kind,
                                 "source": concept.source.lower()})

    record: dict = {
        "identifier": identifier,
        "label": primary.label,
        "antimicrobial_class": antimicrobial_class,
        "curation_status": "PROPOSED" if curator and not (chebi or aro) else "SEEDED",
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
    if roles:
        record["activity_roles"] = roles
    if structural_class:
        record["structural_class"] = structural_class
        record["structural_class_id"] = structural_class_id
    # When a ChEBI concept merged into this record, IT is the authority on the
    # compound's mechanism roles. A CARD cross-reference to some OTHER ChEBI id
    # is then either redundant or wrong, and wrong happens: CARD points cefdinir
    # at CHEBI:131724, which is iclaprim, a dihydrofolate reductase inhibitor.
    # Reading roles off that row gave a cephalosporin FOLATE_PATHWAY_INHIBITION
    # while its own CARD target, eleven lines below, was a penicillin-binding
    # protein — a record contradicting itself on its face.
    #
    # Only a record with no ChEBI concept at all falls back to the cross-
    # referenced row, which is what keeps econazole, ketoconazole and miconazole
    # working: their ChEBI entries carry the roles but no structure, so they
    # never become concepts of their own.
    chebi_mechanism = _dedupe(r for c in chebi for r in c.mechanism_roles)
    mechanism_roles = chebi_mechanism if chebi else _dedupe(
        r for c in group for r in c.mechanism_roles)
    moa = mode_of_action_from_roles(mechanism_roles, conf, load_role_names(),
                                    record["antimicrobial_class"])
    if moa:
        (record["mode_of_action"], record["mode_of_action_notes"],
         record["mode_of_action_target_scope"]) = moa

    structure = next((c.structure for c in group if c.structure.get("standard_inchi")),
                     group[0].structure)
    record["chemical_structure"] = structure

    # An xref means THE SAME STRUCTURE — the contract docs/CURATION.md and the
    # schema both state. Three ways a source xref does not, all of which reached
    # the corpus before this gate existed:
    #
    #   1. It identifies something that is not a structure at all. A PDB
    #      accession is a macromolecular ENTRY: ampicillin carried pdb:1H8S, an
    #      anti-ampicillin ANTIBODY complex, and alsterpaullone carried pdb:1Q3W,
    #      a human GSK3beta complex.
    #   2. Its structure is known and DIFFERENT. polymyxin B2 carried CHEBI:8309,
    #      which is polymyxin B1 — a different InChIKey. That is the "a salt,
    #      conjugate or stereoisomer is a different record" rule inverted.
    #   3. It is a strictly BROADER class, which belongs in `parent_compounds`.
    #      Erythromycin A, lividomycin A and mycinamicin IV each carried one
    #      identifier in BOTH fields, which cannot both be true.
    #
    #   4. Its structure is UNKNOWN and its name contradicts the record's. The
    #      structure comparison needs a structure on both sides, so a
    #      structureless target skipped it entirely and published unexamined —
    #      which is how cefdinir carried CHEBI:131724, *iclaprim* (#164). Where
    #      the inventory names such a target and no name matches, that is
    #      evidence of difference rather than absence of evidence, and the xref
    #      is refused and reported.
    #
    # Where the structure cannot be compared AND no naming evidence contradicts
    # it — most referenced ChEBI terms have no structure in the committed
    # inventory — the xref is KEPT and surfaced on
    # `just worklist --queue xref-unverified`. Dropping it would discard a source
    # assertion on the grounds that we cannot check it, which is a different and
    # worse error than keeping one we have not checked.
    own_key = (structure or {}).get("standard_inchi_key")
    broader = set(parents)
    contested = contested_xrefs(group)
    own_names = {" ".join((record.get("label") or "").lower().split())}
    own_names |= {" ".join((syn.get("name") or "").lower().split())
                  for syn in (record.get("synonyms") or [])}
    own_names -= {""}

    kept = gate_xrefs(xrefs, own_key=own_key, own_names=own_names, broader=broader,
                      contested=contested, chebi_keys=chebi_keys,
                      chebi_name_index=chebi_name_index,
                      refused=REFUSED_STRUCTURELESS_XREFS,
                      identity=(identifier, record.get("label", "")))
    # Three slots, by what the namespace means. Emitted in this order so the
    # drug and document identifiers sit beside the structure ones on disk.
    by_slot: dict[str, list[str]] = {"xrefs": [], "drug_xrefs": [], "document_xrefs": []}
    for x in kept:
        by_slot[xref_slot(x)].append(x)
    for slot, values in by_slot.items():
        if values:
            record[slot] = values
    observations = structural_observations(group, source_version, source_version)
    if observations:
        record["structural_observations"] = observations
    record["source_concepts"] = [
        {
            "source": c.source,
            "source_id": c.source_id,
            "source_label": c.label,
            "minted_identifier": c.minted,
            **({"role_terms": c.roles} if c.roles else {}),
            **({"evidence": c.evidence} if c.evidence else {}),
            "source_version": c.source_version or source_version,
        }
        for c in sorted(group, key=lambda c: (c.source, c.source_id))
    ]
    sources = {c.source for c in group}
    if sources == {"CURATOR"}:
        record_curation_event(
            record,
            curator=SEEDER_CURATOR,
            action="PROPOSED_FROM_CURATOR_INVENTORY",
            changes="Proposed from curation/curator_antibiotics.tsv",
        )
    else:
        record_curation_event(
            record,
            curator=SEEDER_CURATOR,
            action="SEEDED_FROM_SOURCES",
            changes=f"Seeded from data/raw/ inventories ({', '.join(sorted(sources))})",
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
    target_roles = {row["target_id"]: row for row in load_tsv(ARO_TARGET_ROLES_PATH)}
    target_ids = {row["target_id"] for row in targets}
    if target_ids != set(target_roles):
        missing = sorted(target_ids - set(target_roles))
        stale = sorted(set(target_roles) - target_ids)
        raise ValueError(f"ARO target-role map drift: missing={missing}, stale={stale}")

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
            role = target_roles[row["target_id"]]
            direct = role["target_relation"] == "DIRECT_BINDING_TARGET"
            item = {
                "target_id": row["target_id"],
                "target_label": row["target_name"],
                "target_type": role["target_type"],
                "target_relation": role["target_relation"],
                "experimental_context": (
                    "CARD/ARO database assertion; target organism, strain, and assay "
                    "are not specified. " + role["rationale"]
                ),
                "evidence_status": (
                    "PRIMARY_EVIDENCE_NEEDED" if direct else "DATABASE_ASSERTION_ONLY"
                ),
                "source": "CARD_ARO",
                "source_version": source_version,
                "source_retrieved_on": source_version,
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


PHIBASE_RESISTANCE_SOURCE = "PHIBASE"
PHIBASE_NOTE_MARKER = "PHI-base antimicrobial_interaction"


def is_phibase_sourced_resistance(item: dict) -> bool:
    """True only for a resistance association owned by the PHI-base lane.

    Ownership is the ``source`` field, as it is for the MIBiG, BindingDB and FDA
    lanes. The note marker is the pre-#94 shape, when every organismal fact
    lived in the note and the marker was the only thing to match on. It is still
    recognized because the alternative is silent duplication: re-seeding a
    checkout written before #94 would read those items as curator-written, keep
    them, and append a second structured copy of all 217 associations beside
    them. Recognizing the old shape makes the migration a replacement.
    """
    return (
        item.get("source") == PHIBASE_RESISTANCE_SOURCE
        or PHIBASE_NOTE_MARKER in str(item.get("note") or "")
    )


def phibase_sourced_resistance_view(record: dict) -> list[dict]:
    return [
        item
        for item in (record.get("resistance_mechanisms") or [])
        if is_phibase_sourced_resistance(item)
    ]


def attach_phibase_resistance(records: dict[str, dict]) -> Counter:
    """Attach ChEBI-grounded PHI-base resistance associations.

    The source supports an alteration--chemical resistance phenotype but does
    not necessarily establish a biochemical route.  Consequently every row is
    typed ``UNKNOWN`` and described as an association rather than promoted to
    target alteration, efflux, or another mechanism category.
    """
    rows = load_tsv(RAW_DIR / "phibase_amr.tsv")
    counts: Counter = Counter()
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        record = records.get(row["identifier"])
        if record is None:
            counts["missing_identifier"] += 1
            continue
        if record["chemical_structure"]["standard_inchi_key"] != row["standard_inchi_key"]:
            counts["identity_drift"] += 1
            continue
        grouped[row["identifier"]].append(row)
        counts["matched_associations"] += 1

    for identifier, matched_rows in sorted(grouped.items()):
        items = []
        seen = set()
        for row in matched_rows:
            key = (
                row["phig_id"], row["taxon_id"], row["strain_taxon_id"],
                row["strain_label"], row["modification"], row["phenotype_id"], row["pmid"],
            )
            if key in seen:
                counts["duplicate_rows"] += 1
                continue
            seen.add(key)
            # Built in schema order, with the optional slots dropped afterwards,
            # so an emitted item reads in the order the schema declares rather
            # than in the order the source happened to fill it.
            item = {
                "mechanism_type": "UNKNOWN",
                "label": f"{row['modification']} associated with {row['phenotype_label']}",
                "taxon_id": f"NCBITaxon:{row['taxon_id']}",
                "taxon_label": row["taxon_label"],
                "strain": row["strain_label"] or None,
                "strain_taxon_id": (
                    f"NCBITaxon:{row['strain_taxon_id']}" if row["strain_taxon_id"] else None
                ),
                "alteration": row["modification"],
                "protein_accession": (
                    f"UniProtKB:{row['protein_accession']}"
                    if row["protein_accession"] else None
                ),
                "gene_id": row["gene_id"] or None,
                "phenotype_id": row["phenotype_id"] or None,
                "phenotype_label": row["phenotype_label"],
                "assay": row["evidence_code"],
                "source": PHIBASE_RESISTANCE_SOURCE,
                "source_version": row["source_commit"],
                "source_retrieved_on": row["source_retrieved_on"],
                # The caveat is the only part of this that is genuinely prose.
                # Everything the note used to restate -- organism, strain,
                # protein, allele, phenotype, assay, provenance -- is now in the
                # slots above, where it can be queried and contradicted (#94).
                "note": (
                    "This is a curated gene-alteration/chemical resistance association, "
                    "not evidence for a specific biochemical resistance mechanism."
                ),
                "evidence": [{
                    "reference": f"PMID:{row['pmid']}",
                    "notes": (
                        "PHI-base primary-literature antimicrobial interaction "
                        f"{row['phig_id']}; joined to this record by exact ChEBI identifier."
                    ),
                }],
            }
            items.append({k: v for k, v in item.items() if v is not None})
        records[identifier].setdefault("resistance_mechanisms", []).extend(items)
        _history_last(records[identifier])
        counts["matched_records"] += 1
    return counts


BINDINGDB_TARGET_SOURCE = "BINDINGDB"


def is_bindingdb_sourced_target(item: dict) -> bool:
    """True only for a target assertion owned by the BindingDB extractor."""
    return item.get("source") == BINDINGDB_TARGET_SOURCE


def bindingdb_sourced_target_view(record: dict) -> list[dict]:
    """The reproducible BindingDB slice of a record's target assertions."""
    return [
        item
        for item in (record.get("molecular_targets") or [])
        if is_bindingdb_sourced_target(item)
    ]


def bindingdb_row_supports_target_association(row: dict[str, str]) -> bool:
    """Return whether a BindingDB measurement supports a molecular-target edge.

    BindingDB can associate whole-cell antiviral activity and review-table values
    with a protein record.  Those rows are useful source observations, but they do
    not by themselves establish that the named protein is the measured target.
    Likewise, a lower bound reports that inhibition was not reached and is not
    positive target-association evidence.
    """
    if row.get("measurement_type") == "EC50":
        return False
    if row.get("qualifier") in {"GT", "GE"}:
        return False
    assay_name = row.get("assay_name", "").strip().casefold()
    assay_description = row.get("assay_description", "").strip().casefold()
    if assay_name in {"no assay is provided", "no assay provided"}:
        return False
    if (
        assay_name == "drc analysis by immunofluorescence"
        or (
            "immunofluorescence" in assay_description
            and "vero cells" in assay_description
            and "viral infections" in assay_description
            and "sars-cov-2 was added" in assay_description
        )
        or (
            "intracellular nucleocapsid" in assay_description
            and "calu-3 cells" in assay_description
        )
    ):
        return False
    return "review article" not in assay_description


def record_yaml_matches(existing_text: str | None, record: dict) -> bool:
    """Compare record data without treating YAML mapping order as a change."""
    return existing_text is not None and yaml.safe_load(existing_text) == record


def attach_bindingdb_targets(records: dict[str, dict]) -> Counter:
    """Attach quantitative BindingDB assertions from the committed inventory."""
    rows = load_tsv(RAW_DIR / "bindingdb_target_measurements.tsv")
    by_key: dict[str, list[str]] = defaultdict(list)
    for identifier, record in records.items():
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(identifier)

    grouped: dict[tuple[str, str, str, str], list[dict]] = defaultdict(list)
    counts: Counter = Counter()
    for row in rows:
        if row.get("curation_source") != "Curated from the literature by BindingDB":
            raise ValueError("BindingDB inventory contains a non-BindingDB-curated row")
        if not bindingdb_row_supports_target_association(row):
            counts["rejected_non_target_specific_measurement"] += 1
            continue
        matches = by_key.get(row["standard_inchi_key"], [])
        if len(matches) != 1:
            counts["ambiguous_or_missing_identity"] += 1
            continue
        identifier = matches[0]
        key = (identifier, row["target_name"], row["taxon_id"], row["target_relation"])
        grouped[key].append(row)
        counts["matched_measurements"] += 1

    assertions_by_record: dict[str, list[dict]] = defaultdict(list)
    for (identifier, target_name, taxon_id, relation), matched_rows in sorted(grouped.items()):
        types = {row["target_type"] for row in matched_rows}
        labels = {row["taxon_label"] for row in matched_rows}
        versions = {row["source_version"] for row in matched_rows}
        dates = {row["source_retrieved_on"] for row in matched_rows}
        if any(len(values) != 1 for values in (types, labels, versions, dates)):
            raise ValueError(
                f"inconsistent BindingDB target group for {identifier}/{target_name}/{taxon_id}"
            )

        measurements = []
        proteins: dict[str, dict] = {}
        evidence: dict[str, dict] = {}
        for row in sorted(
            matched_rows,
            key=lambda value: (
                int(value["bindingdb_reactant_set_id"]),
                value["measurement_type"],
            ),
        ):
            measurements.append({
                "measurement_type": row["measurement_type"],
                "original_value": row["original_value"],
                "qualifier": row["qualifier"],
                "value": float(row["value"]),
                "unit": row["unit"],
                "assay_name": row["assay_name"],
                "assay_description": row["assay_description"],
                "bindingdb_reactant_set_id": row["bindingdb_reactant_set_id"],
                "bindingdb_entry_assay_id": row["bindingdb_entry_assay_id"],
                "bindingdb_monomer_id": row["bindingdb_monomer_id"],
                "source_version": row["source_version"],
                "source_retrieved_on": row["source_retrieved_on"],
                "reference": row["reference"],
            })
            evidence.setdefault(row["reference"], {
                "reference": row["reference"],
                "notes": (
                    "BindingDB literature-curated quantitative target measurement; "
                    "source value, assay text, reaction-set ID, and target organism retained."
                ),
            })
            for protein in json.loads(row["protein_examples_json"]):
                accession = protein["accession"]
                proteins.setdefault(accession, {
                    "uniprot_id": f"UniProtKB:{accession}",
                    "protein_label": protein["label"],
                    "taxon_id": f"NCBITaxon:{taxon_id}",
                    "taxon_label": next(iter(labels)),
                    "entry_status": protein["entry_status"],
                    "retrieved_on": next(iter(dates)),
                    "role": f"BindingDB target chain {protein['chain']}",
                })

        assertion = {
            "target_label": target_name,
            "target_type": next(iter(types)),
            "target_relation": relation,
            "taxon_id": f"NCBITaxon:{taxon_id}",
            "taxon_label": next(iter(labels)),
            "experimental_context": (
                "BindingDB quantitative measurement in the named target organism; "
                "source assay descriptions and identifiers are retained per measurement."
            ),
            "evidence_status": "PRIMARY_EVIDENCE",
            "source": BINDINGDB_TARGET_SOURCE,
            "source_version": next(iter(versions)),
            "source_retrieved_on": next(iter(dates)),
            "measurements": measurements,
            "evidence": list(evidence.values()),
        }
        if proteins:
            assertion["protein_examples"] = list(proteins.values())
        assertions_by_record[identifier].append(assertion)
        counts["matched_target_assertions"] += 1

    for identifier, assertions in assertions_by_record.items():
        records[identifier].setdefault("molecular_targets", []).extend(assertions)
        _history_last(records[identifier])
        counts["matched_records"] += 1
    return counts


MIBIG_PRODUCER_SOURCE = "MIBIG"


# Rank markers that continue a taxonomic name rather than beginning a strain
# designation. "Francisella tularensis subsp. tularensis SCHU S4" is a name of
# four tokens followed by a strain; "Streptomyces rochei NBRC 12908" is a name of
# two.
_RANK_MARKERS = ("subsp.", "var.", "f.", "pv.", "sp.", "bv.", "serovar")
_EPITHET = re.compile(r"^[a-z][a-z-]+$")

# The inventory is faithful to MIBiG's wording; the corpus speaks the schema's
# closed vocabulary. Mapping here rather than in the extractor keeps the
# committed inventory a record of what upstream said (#211).
MIBIG_LINK_EVIDENCE_METHODS = {
    "Heterologous expression": "HETEROLOGOUS_EXPRESSION",
    "Knock-out studies": "KNOCK_OUT_STUDIES",
    "Enzymatic assays": "ENZYMATIC_ASSAYS",
    "Gene expression correlated with compound production":
        "GENE_EXPRESSION_CORRELATED_WITH_PRODUCTION",
    "Correlation of genomic and metabolomic data": "GENOMIC_METABOLOMIC_CORRELATION",
    "In vitro expression": "IN_VITRO_EXPRESSION",
}


def mibig_link_evidence(raw: str) -> list[str]:
    """MIBiG's pipe-joined method names as schema vocabulary, sorted.

    An unmapped method raises rather than being dropped. Dropping it would turn
    an unrecognized method into a producer with NO link evidence, which reads as
    a weaker claim instead of an unhandled one -- and the extractor's allow-list
    means an unmapped value can only arrive from a MIBiG release that added a
    term nobody has read yet.
    """
    methods = []
    for name in raw.split("|"):
        if name not in MIBIG_LINK_EVIDENCE_METHODS:
            raise KeyError(
                f"MIBiG link-evidence method {name!r} has no schema value. Add it to "
                "MIBIG_LINK_EVIDENCE_METHODS and LinkEvidenceMethodEnum, or to the "
                "extractor's exclusions, before re-seeding.")
        methods.append(MIBIG_LINK_EVIDENCE_METHODS[name])
    return sorted(set(methods))


# A producer claim answers "which organism makes this". A label that names no
# genus cannot answer it: "uncultured bacterium" says only that some bacterium
# does. Refused rather than published, and reported, the way an unverifiable
# cross-reference is (#217). A label that DOES name a genus is kept even when it
# is an uncultivated symbiont -- "uncultured Candidatus Entotheonella sp." is a
# real organism identity and the corpus should carry it.
REFUSED_UNNAMED_PRODUCERS: list[tuple[str, str, str]] = []

# Capitalized words that are status or placement markers rather than genera.
# `Candidatus` prefixes a proposed name, and the rest are NCBI's words for "we
# cannot say". Without this list they would each pass for a genus.
_NOT_A_GENUS = frozenset({"Candidatus", "Uncultured", "Unclassified",
                          "Unidentified", "Unknown"})
# NCBI writes "<higher taxon> bacterium <strain>" for an organism it can place
# but not name, so a rank noun is the source saying the name is missing.
# "Chloroflexi bacterium TSY" names a PHYLUM, and reading only for a
# genus-shaped token accepted it.
#
# Matched only in lower case, because several of these words are also validly
# published genera. "Cyanobacterium aponinum" is a real organism and cyanobacteria
# are a major producer clade, so a case-blind veto would have refused it.
# "symbiont" and "endosymbiont" are deliberately absent: they describe a
# lifestyle, not a missing name, and "Burkholderia rhizoxinica endosymbiont"
# names its organism perfectly well.
_RANK_NOUNS = frozenset({"bacterium", "archaeon", "organism", "fungus",
                         "eukaryote", "cyanobacterium", "proteobacterium",
                         "actinobacterium"})
# Family and order endings. No validly published genus ends in either, so these
# are safe to veto outright, which "-ia" is not: Nocardia and Burkholderia are
# genera. A bare phylum used alone, without a rank noun beside it, is therefore
# still accepted; NCBI does not write labels that way, and no suffix separates
# Chloroflexi from a genus without also refusing real ones.
_HIGHER_RANK_SUFFIXES = ("aceae", "ales")
_GENUS_TOKEN = re.compile(r"^\[?([A-Z][a-z]{2,})\]?$")

# NCBI nodes that are containers rather than organisms. A label beside one is
# asserting something the identifier cannot support. #94 required a taxon CURIE
# to arrive WITH a label, which is co-presence; that a label is the one the CURIE
# denotes is checked nowhere yet, and this is the narrow part of it that needs no
# taxonomy source. MIBiG ships exactly one such row today,
# BGC0001875, whose id is the unclassified-sequences bucket while its label
# names a real strain. The two disagree about what is being claimed, and the
# label alone cannot show it (#221).
#
# Only these nodes. Checking that any id denotes its label needs a taxonomy
# names source this repository does not commit; that is #186, and this list is
# the narrow part that does not need one.
# Two kinds, and the list is necessarily partial. NCBI's containers hold no
# organism at all, and its top-level clades hold every organism, which answers
# the producer question no better: "a bacterium makes this" is the same empty
# claim as "uncultured bacterium", already refused on its label.
#
# Partial because there is no end to the ranks above genus, and enumerating them
# is the wrong shape of fix. The general answer is a lineage check against the
# NCBI taxdump, which this repository already reads at extraction time in the
# BindingDB evaluator; see #248. Until then, refusing the nodes a producer could
# plausibly be grounded in beats refusing none of them.
_NON_ORGANISM_TAXA = {
    "1": "the taxonomy root",
    "12908": "unclassified sequences",
    "28384": "other sequences",
    "131567": "cellular organisms",
    "32630": "synthetic construct",
    "81077": "artificial sequences",
    "29278": "vector",
    "32644": "unidentified",
    "408169": "metagenomes",
    "2": "the domain Bacteria",
    "2157": "the domain Archaea",
    "2759": "the domain Eukaryota",
    "4751": "the kingdom Fungi",
    "10239": "the Viruses",
}


def _genus_tokens(tokens: list[str]) -> list[str]:
    """The genus-shaped names in `tokens`, minus status words and higher ranks."""
    found = []
    for token in tokens:
        match = _GENUS_TOKEN.match(token)
        if not match or match.group(1) in _NOT_A_GENUS:
            continue
        if match.group(1).endswith(_HIGHER_RANK_SUFFIXES):
            continue
        found.append(match.group(1))
    return found


def producer_refusal_reason(taxon_id: str, taxon_label: str) -> str | None:
    """Why this taxon cannot carry a producer claim, or None if it can.

    One copy, called by the seeder and by the worklist queue that reports what
    the seeder refused. Those were two restatements of the same rule, and they
    had already drifted once (#226); a second reason was added to one of them
    and the drift was undetectable, because the only row exercising it matches
    no corpus record, so both versions produced the same queue.
    """
    bucket = _NON_ORGANISM_TAXA.get(taxon_id)
    if bucket:
        return (f"NCBITaxon:{taxon_id} is {bucket}, not an organism, while the label "
                f"reads {taxon_label.rstrip('.')!r}. The identifier and the name "
                "disagree about what is being claimed.")
    if not names_an_organism(taxon_label):
        return (f"{taxon_label!r} (NCBITaxon:{taxon_id}) identifies no organism. The "
                "producer claim would say only that some microbe makes this.")
    return None


def names_an_organism(label: str) -> bool:
    """True when some token in the label is shaped like a genus.

    Any token, not the first one. NCBI routinely prefixes a genus it can name
    with words for the culture status or the uncertainty of its placement, and
    those prefixes do not make the name less of an identity: "uncultured
    Candidatus Entotheonella sp." and "[Oscillatoria] sp. PCC 6506" both name a
    genus a reader can look up, while "uncultured bacterium" and "fungal sp."
    name none. Reading only the first token refused all four alike (#217).

    Brackets are NCBI's marker for a name whose generic placement is disputed,
    which is a taxonomic argument about a real organism, so they are stripped
    rather than treated as disqualifying.

    A lower-case rank noun vetoes the label. "Chloroflexi bacterium TSY" carries
    a capitalized taxon and still names no organism, because that taxon is a
    phylum and "bacterium" beside it is the source saying so.
    """
    tokens = label.split()
    if _RANK_NOUNS & {token.strip(".,") for token in tokens}:
        return False
    return bool(_genus_tokens(tokens))


# What MIBiG actually attached each reference to. Neither basis is evidence for
# the producer link, because MIBiG publishes none: its locus evidence objects
# carry a method and no reference at all. Saying otherwise was a real overclaim
# in the corpus -- compound-level evidence in MIBiG is structure elucidation and
# nothing else, NMR 1,234 times, mass spectrometry 550, MS/MS 237, then chemical
# derivatisation, authentic standards, X-ray and total synthesis. A citation for
# how a structure was solved does not show that an organism makes it.
MIBIG_REFERENCE_BASIS = {
    "compound_evidence": (
        "MIBiG attaches this reference to the compound, as support for its "
        "STRUCTURE: every compound-level method in the release is structure "
        "elucidation (NMR, mass spectrometry, X-ray, total synthesis). It "
        "establishes what the molecule is. It is NOT evidence that this organism "
        "produces it; MIBiG attaches no reference to the producer link at all."
    ),
    "first_mibig_legacy_reference": (
        "MIBiG's first legacy reference for the entry, inherited rather than "
        "attached to the compound. It supports that the entry exists; it is NOT "
        "established as evidence for this specific producer/compound link."
    ),
}


def split_organism_strain(label: str) -> tuple[str, str | None]:
    """Split "<taxonomic name> <strain designation>" conservatively.

    MIBiG's ``taxonomy.name`` is a strain name, but the accompanying
    ``ncbiTaxId`` is frequently the SPECIES: NCBITaxon:1928 denotes
    *Streptomyces rochei*, and writing "Streptomyces rochei NBRC 12908" as that
    CURIE's label asserts the CURIE denotes a strain, which it does not. The
    schema's ``strain`` slot was added for exactly this and never populated.

    Splitting is safe in both directions. Where the id is species-level the
    label stops contradicting it; where the id is strain-level the label becomes
    less specific than the id but stays true of it, because a strain is an
    instance of its species. What is never safe is guessing, so an unparsed name
    is returned whole with no strain rather than split on whitespace and hoped
    over.

    The genus is looked for anywhere in the label, not only at its start, and
    everything before it stays part of the name. NCBI prefixes a nameable genus
    with its culture status and brackets one whose generic placement is disputed,
    so "uncultured Prochloron sp. 06037A" and "[Oscillatoria] sp. PCC 6506" both
    carry a collection number this would otherwise leave inside `taxon_label`.
    `names_an_organism` was widened to accept exactly those labels, and a
    splitter still reading only the first token would have published the
    designation as part of the species name the day one matched (#224).
    """
    tokens = label.split()
    genus = next(
        (position for position, token in enumerate(tokens)
         if (match := _GENUS_TOKEN.match(token)) and match.group(1) not in _NOT_A_GENUS),
        None,
    )
    if genus is None or len(tokens) < genus + 2:
        return label, None
    index = genus + 1
    if tokens[index] == "sp." or _EPITHET.match(tokens[index]):
        index += 1
    else:
        return label, None
    # Consume "subsp. tularensis" and friends.
    while index + 1 < len(tokens) and tokens[index] in _RANK_MARKERS:
        index += 2
    if index >= len(tokens):
        return label, None
    # The name ends where the designation begins; an explicit "strain" keyword
    # belongs to neither, so the boundary is fixed before consuming it.
    name_end = index
    if tokens[index] == "strain":
        index += 1
    remainder = tokens[index:]
    if not remainder:
        return label, None
    # A lowercase continuation is more likely an unrecognized rank marker than a
    # strain designation; leave the name alone rather than truncate a real name.
    if remainder[0][0].islower():
        return label, None
    return " ".join(tokens[:name_end]), " ".join(remainder)


def is_mibig_sourced_producer(item: dict) -> bool:
    """True only for a producer assertion owned by the MIBiG extractor."""
    return item.get("source") == MIBIG_PRODUCER_SOURCE


def mibig_sourced_producer_view(record: dict) -> list[dict]:
    """The reproducible MIBiG slice of a record's producer assertions."""
    return [
        item
        for item in (record.get("producer_organisms") or [])
        if is_mibig_sourced_producer(item)
    ]


def attach_mibig_producers(records: dict[str, dict], release_version: str) -> Counter:
    """Attach experimentally supported MIBiG producer/BGC evidence by InChIKey.

    Names, database cross-references, and connectivity-only matches are never
    identity evidence here. An inventory row with incomplete potential stereo,
    or a key shared by multiple corpus records, is counted and skipped.
    """
    # Cleared here rather than in `merge`, because this is where it is filled.
    # The two sibling lists are appended from inside `merge`'s call tree, so
    # clearing at its entry is right for them; doing the same for this one would
    # make correctness depend on the order the caller happens to use, and would
    # leak state into any test calling this function directly (#227).
    REFUSED_UNNAMED_PRODUCERS.clear()
    rows = load_tsv(RAW_DIR / "mibig_producers.tsv")
    by_key: dict[str, list[str]] = defaultdict(list)
    for identifier, record in records.items():
        key = record["chemical_structure"]["standard_inchi_key"]
        by_key[key].append(identifier)

    grouped: dict[str, list[dict]] = defaultdict(list)
    counts: Counter = Counter()
    for row in rows:
        if not row.get("link_evidence"):
            counts["rejected_no_link_evidence"] += 1
            continue
        if row.get("stereo_complete") != "true":
            counts["ambiguous_stereochemistry"] += 1
            continue
        matches = by_key.get(row.get("standard_inchi_key", ""), [])
        if not matches:
            counts["out_of_scope"] += 1
            continue
        if len(matches) != 1:
            counts["ambiguous_corpus_identity"] += 1
            continue
        grouped[matches[0]].append(row)
        counts["matched"] += 1

    for identifier, matched_rows in sorted(grouped.items()):
        items = []
        seen = set()
        for row in sorted(
            matched_rows,
            key=lambda value: (value["mibig_accession"], value["compound_index"]),
        ):
            key = (row["mibig_accession"], row["taxon_id"])
            if key in seen:
                continue
            seen.add(key)
            refusal = producer_refusal_reason(row["taxon_id"], row["taxon_label"])
            if refusal:
                REFUSED_UNNAMED_PRODUCERS.append((
                    identifier, row["mibig_accession"],
                    f"{row['mibig_accession']}: {refusal} The cluster and its citation "
                    "are real; the producer claim is not published."))
                counts["refused_unnamed_producer"] += 1
                continue
            taxon_label, strain = split_organism_strain(row["taxon_label"])
            # Schema order, optional slots dropped afterwards -- see the same
            # pattern in the PHI-base lane.
            item = {
                "taxon_id": f"NCBITaxon:{row['taxon_id']}",
                "taxon_label": taxon_label,
                "strain": strain,
                "biosynthetic_gene_cluster": row["mibig_accession"],
                "source": MIBIG_PRODUCER_SOURCE,
                "source_version": release_version,
                "source_record_version": row["entry_version"],
                "source_quality": row["entry_quality"],
                "link_evidence": mibig_link_evidence(row["link_evidence"]),
                "link_evidence_scope": (
                    "COMPOUND_SPECIFIC" if row["entry_compound_count"] == "1"
                    else "CLUSTER_INHERITED"),
                "reviewed": True if row.get("expert_reviewed") == "true" else None,
                "note": (
                    f"MIBiG active entry; compound {row['compound_name']!r} joined "
                    "by exact Standard InChIKey."
                ),
                "evidence": [{
                    "reference": row["primary_reference"],
                    "notes": MIBIG_REFERENCE_BASIS.get(
                        row["reference_basis"],
                        f"MIBiG reference basis {row['reference_basis']!r}, "
                        "not one this extractor knows how to characterize.",
                    ),
                }],
            }
            items.append({k: v for k, v in item.items() if v is not None})
            # Counted here, not derived as matched minus refused. Those two are
            # in different units -- matched counts inventory rows passing the
            # structure gate, refusals count claims surviving the dedupe -- so
            # the subtraction printed the wrong total as soon as one entry
            # contributed two rows for one record (#227).
            counts["published"] += 1
        if items:
            records[identifier]["producer_organisms"] = items
            _history_last(records[identifier])
    return counts


FDA_CLINICAL_SOURCE = "DRUGS_AT_FDA"


def is_fda_sourced_clinical_assertion(item: dict) -> bool:
    return item.get("source") == FDA_CLINICAL_SOURCE


def fda_sourced_clinical_view(record: dict) -> list[dict]:
    return [
        item
        for item in (record.get("clinical_status_assertions") or [])
        if is_fda_sourced_clinical_assertion(item)
    ]


def attach_fda_clinical_status(records: dict[str, dict]) -> Counter:
    """Attach approved Drugs@FDA products after the extractor's exact GSRS join."""
    rows = load_tsv(RAW_DIR / "fda_clinical_status.tsv")
    by_key: dict[str, list[str]] = defaultdict(list)
    for identifier, record in records.items():
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(identifier)

    grouped: dict[str, list[dict]] = defaultdict(list)
    counts: Counter = Counter()
    for row in rows:
        matches = by_key.get(row["standard_inchi_key"], [])
        if len(matches) != 1:
            counts["ambiguous_or_missing"] += 1
            continue
        grouped[matches[0]].append(row)
        counts["matched_products"] += 1

    base_url = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm"
    for identifier, matched_rows in sorted(grouped.items()):
        assertions = []
        seen = set()
        for row in sorted(
            matched_rows,
            key=lambda value: (value["application_number"], value["product_number"]),
        ):
            key = (row["application_number"], row["product_number"])
            if key in seen:
                continue
            seen.add(key)
            assertions.append({
                "status": "APPROVED",
                "jurisdiction": "US-FDA",
                "application_number": row["application_number"],
                "application_type": row["application_type"],
                "product_number": row["product_number"],
                "sponsor_name": row["sponsor_name"],
                "drug_name": row["drug_name"],
                "ingredient_name": row["ingredient_name"],
                "substance_id": f"UNII:{row['unii']}",
                "approval_date": row["approval_date"],
                "submission_status": row["submission_status"],
                "marketing_status": row["marketing_status"],
                "currently_marketed": row["currently_marketed"] == "true",
                "source": FDA_CLINICAL_SOURCE,
                "source_version": row["drugsfda_version"],
                "source_retrieved_on": row["drugsfda_retrieved_on"],
                "identity_source": "FDA_GSRS",
                "identity_source_version": row["unii_version"],
                "identity_retrieved_on": row["gsrs_retrieved_on"],
                "identity_record_version": row["gsrs_record_version"],
                "reference": (
                    f"{base_url}?event=overview.process&ApplNo={row['application_number']}"
                ),
            })
        if assertions:
            records[identifier]["clinical_status"] = "APPROVED"
            records[identifier]["clinical_status_assertions"] = assertions
            _history_last(records[identifier])
            counts["matched_records"] += 1
    return counts


# --------------------------------------------------------------------------
# writing
# --------------------------------------------------------------------------



def _item_aro_id(item: dict) -> str:
    return str(item.get("aro_id") or item.get("target_id") or "")


# The note every seeded mechanism item carries. It is the marker that separates
# "the seeder wrote this" from "a curator wrote this, citing an ARO term" —
# a distinction the citation prefix alone cannot make, and getting it wrong
# deleted legitimate curation on re-seed.
CARD_NOTE_MARKER = "CARD/ARO asserts"

# The same device for mode_of_action: a seeded value says so in its notes, so a
# re-seed can replace its own work and must leave a curator's alone.
MOA_NOTE_MARKER = "Assigned from ChEBI role"

# The curator name this script signs its own curation events with. Used to keep
# history maintenance off anything a human wrote.
SEEDER_CURATOR = "seed_from_sources"

# ...and the curator's half of it. Ownership cannot be inferred only from the
# ABSENCE of the seeder's marker, because the seeded note invites a curator to
# edit the very field that decides ownership: appending to it left the marker in
# place and the correction was reverted on the next re-seed, citation and all.
# A curator writes this prefix to claim the field, and it also lets them VETO —
# a record carrying the claim with no mode_of_action means "no mechanism should
# be seeded here", which is the only remedy for a wrong derived value and was
# previously impossible to express.
CURATOR_NOTE_MARKER = "CURATOR:"


def _claims_mode_of_action(notes: str) -> bool:
    """True when a curator has CLAIMED mode_of_action in these notes.

    The marker must begin a sentence or a line, not merely appear somewhere in
    the text. A bare substring test made "ask a CURATOR: about this later" — the
    kind of thing that lands in a free-text note — a permanent, silent veto that
    locked the seeder out of the field for good.
    """
    text = str(notes or "")
    # These notes round-trip through YAML folded scalars (`>-`), which join
    # source lines with a space — so a claim written on its own line arrives
    # mid-string with no newline to find it by. Anchor on the start of the text
    # or on a sentence boundary instead, including the separators a curator
    # actually reaches for.
    # Case-SENSITIVE and literal: `docs/CURATION.md` documents the exact token,
    # and matching case-insensitively made an ordinary signature line —
    # ". curator: jane" — silently claim the field. The boundary class covers
    # the separators a curator actually types, including a comma, a quote and a
    # dash with or without a leading space.
    return bool(re.search(r"""(?:^|[\n.,;:!?)\]"'\u2013\u2014-])\s*""" + re.escape(CURATOR_NOTE_MARKER),
                          text.strip()))


def is_card_sourced(item: dict) -> bool:
    """True when the seeder wrote this item, rather than a curator.

    One signal: the item cites only ARO terms AND carries the seeder's own note
    marker. Both halves are needed. The prefix alone deleted a curator's item
    that cited an ARO determinant CARD does not link to this molecule; the ARO
    id alone — a second signal tried and removed — deleted a curator's upgrade
    of a seeded item to a primary citation, which is the workflow
    docs/HARMONIZATION.md prescribes.

    Deliberate consequence: an item carrying an emitted ARO id but NOT the
    marker reads as the curator's and is kept. A record seeded before the marker
    existed, or one whose notes were reformatted, would therefore survive a
    re-seed and be emitted twice. No such record exists — verify-corpus is green
    — and preserving a curator's work is the error worth making in this
    direction.
    """
    evidence = item.get("evidence") or []
    if not evidence:
        return False
    # The marker is decisive and is checked FIRST. Matching an ARO id this run
    # emitted is NOT sufficient on its own: a curator who replaces the ARO
    # reference with a PMID — the upgrade docs/HARMONIZATION.md prescribes —
    # keeps the same determinant, so an id-only rule classified their work as
    # the seeder's and reverted it on the next re-seed.
    if not all(str(e.get("reference", "")).startswith("ARO:") for e in evidence):
        return False
    return any(CARD_NOTE_MARKER in str(e.get("notes") or "") for e in evidence)


def curator_owns_mode_of_action(record: dict) -> bool:
    """True when a curator has claimed `mode_of_action` on this record.

    ONE definition, used by the merge, by verify-corpus and by the worklist,
    because three copies of this question is how they drifted apart: the merge
    honoured a curator's correction while verify-corpus still compared it
    against a freshly derived value and reported drift no re-seed could clear.

    The NOTES decide, never a bare value. A note that claims the field
    (`CURATOR:`) wins even with the seeder's provenance sentence still in it —
    which is exactly what the documented recipe produces, since it asks the
    curator to append rather than delete. Any other non-seeder note also counts,
    so prose a curator wrote is not thrown away for want of the exact token.
    """
    notes = str(record.get("mode_of_action_notes") or "")
    if not notes:
        return False
    return _claims_mode_of_action(notes) or MOA_NOTE_MARKER not in notes


def seeded_mode_of_action(record: dict) -> str | None:
    """The record's mode_of_action if the SEEDER owns it, else None.

    The same marker device the CARD mechanism items use, so verify-corpus can
    police the seeder's own values without reading a curator's as drift. A value
    with NO notes is the seeder's — a hand-falsified mechanism with the notes
    line deleted used to read as the curator's and freeze permanently.
    """
    if curator_owns_mode_of_action(record):
        return None
    return record.get("mode_of_action")


def card_sourced_view(record: dict, field: str) -> list:
    """The CARD-seeded items of `field`, in seed order — what verify-corpus compares."""
    return [item for item in (record.get(field) or []) if is_card_sourced(item)]


def _restore_key_order(merged: dict, existing: dict) -> dict:
    """Put keys the fresh seed did not produce back where they already were.

    `merge_with_existing` folds curator fields in by assignment, and assigning a
    key a dict does not already hold APPENDS it. So every re-seed of a record
    whose curator wrote a field the seeder never emits -- a mode of action, a
    causal graph -- moved that field to the end, and the real one-field change
    arrived buried in reflow. Six records were relocated that way by #204, the
    first MIBiG gate change, before anyone noticed. That is the churn the
    byte-identical emission contract exists to prevent (#216).

    The record on disk decides the order of everything it already had. A key only
    the fresh record has keeps the neighbour the fresh record gave it, so a
    genuinely new field still lands somewhere sensible rather than at the end.
    `curation_history` is placed last afterwards, as it always was.
    """
    ordered = [key for key in existing if key in merged]
    for position, key in enumerate(merged):
        if key in ordered:
            continue
        preceding = next(
            (k for k in list(merged)[:position][::-1] if k in ordered), None)
        ordered.insert(
            ordered.index(preceding) + 1 if preceding is not None else 0, key)
    rebuilt = {key: merged[key] for key in ordered}
    _history_last(rebuilt)
    return rebuilt


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

    # MIBiG owns only the assertions explicitly marked with its source. A fresh
    # extraction replaces that slice while hand-curated producers survive after
    # it, including curator entries that happen to cite a MIBiG accession.
    seeded_producers = list(record.get("producer_organisms") or [])
    curator_producers = [
        item
        for item in (existing.get("producer_organisms") or [])
        if not is_mibig_sourced_producer(item)
    ]
    if seeded_producers or curator_producers:
        merged["producer_organisms"] = seeded_producers + curator_producers
    else:
        merged.pop("producer_organisms", None)

    seeded_clinical = list(record.get("clinical_status_assertions") or [])
    existing_clinical = list(existing.get("clinical_status_assertions") or [])
    curator_clinical = [
        item for item in existing_clinical if not is_fda_sourced_clinical_assertion(item)
    ]
    existing_had_fda = any(is_fda_sourced_clinical_assertion(item) for item in existing_clinical)
    curator_owns_clinical = "clinical_status" in existing and (
        bool(curator_clinical) or not existing_had_fda
    )
    if seeded_clinical or curator_clinical:
        merged["clinical_status_assertions"] = seeded_clinical + curator_clinical
    else:
        merged.pop("clinical_status_assertions", None)
    if curator_owns_clinical:
        if "clinical_status" in existing:
            merged["clinical_status"] = existing["clinical_status"]
        else:
            merged.pop("clinical_status", None)

    # mode_of_action is seeded from ChEBI's roles but a curator's judgement
    # outranks it, so ownership is decided by the marker rather than by the field
    # name — the same device the CARD mechanism items use.
    existing_moa_notes = str(existing.get("mode_of_action_notes") or "")
    curator_owns_moa = curator_owns_mode_of_action(existing)
    if curator_owns_moa:
        # Includes the veto: a curator note with no value means the field stays
        # empty, and the seeder must not fill it back in.
        merged.pop("mode_of_action", None)
        merged.pop("mode_of_action_notes", None)
        # The scope describes the value it sits beside, and the seeder cannot
        # tell a curator's scope from a leftover by looking at it. So it does
        # not try. The curator owns this block; their mechanism, notes and scope
        # are copied forward verbatim, including a scope they chose to omit.
        #
        # An earlier attempt guessed, dropping the scope when the curator changed
        # the mechanism without changing the scope. Three ways that was worse
        # than the problem: the enum has two values, so a curator who changed the
        # mechanism and deliberately picked the value the seeder happened to
        # derive had their choice deleted as a leftover roughly half the time —
        # the #9 sin the comment claimed to be avoiding; the resulting
        # mechanism-without-scope is a state `test_target_scope_accompanies_
        # every_seeded_mechanism` forbids, so the merge emitted what the gate
        # rejects; and the comment offered `just worklist` as the mitigation
        # when no such queue existed. It does now, and it is the honest answer:
        # a scope the curator owes is curation work to SURFACE, not a value for
        # the seeder to invent or destroy.
        #
        # The one exception is a veto. With no mechanism asserted there is
        # nothing for a scope to describe, so it goes — whoever set it.
        merged.pop("mode_of_action_target_scope", None)
        if "mode_of_action" in existing:
            merged["mode_of_action"] = existing["mode_of_action"]
            if "mode_of_action_target_scope" in existing:
                merged["mode_of_action_target_scope"] = existing["mode_of_action_target_scope"]
        if existing_moa_notes:
            merged["mode_of_action_notes"] = existing_moa_notes

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

    # Source-derived mechanism items and BindingDB target assertions are
    # re-seeded; curator-added or curator-upgraded ones are kept, after them.
    for field in ("molecular_targets", "resistance_mechanisms"):
        seeded_items = list(record.get(field) or [])
        curator_items = [
            item
            for item in (existing.get(field) or [])
            if not is_card_sourced(item)
            and not (field == "resistance_mechanisms" and is_phibase_sourced_resistance(item))
            and not (field == "molecular_targets" and is_bindingdb_sourced_target(item))
        ]
        if seeded_items or curator_items:
            merged[field] = seeded_items + curator_items
        else:
            merged.pop(field, None)

    history = list(existing.get("curation_history") or [])
    # The comparison covers the CARD mechanism sections too: a refresh that adds
    # determinants rewrites the file, and an audit trail that says nothing
    # happened would be worse than none.
    #
    # And the mode-of-action block, which is NOT in SEEDED_FIELDS. Changing the
    # role maps in conf/sources.yaml rewrote ten records' scope and notes in
    # 8582e215 and appended no event to any of them — the trail asserting
    # nothing had happened while the data moved, which is #73's failure reached
    # by a different road. Compared against MERGED rather than against the fresh
    # derivation, so a curator-owned block (copied forward verbatim above)
    # registers as unchanged instead of logging a re-seed on every run.
    unchanged = all(existing.get(f) == record.get(f) for f in SEEDED_FIELDS) and all(
        card_sourced_view(existing, f) == card_sourced_view(record, f)
        for f in ("molecular_targets", "resistance_mechanisms")
    ) and (
        bindingdb_sourced_target_view(existing) == bindingdb_sourced_target_view(record)
    ) and (
        phibase_sourced_resistance_view(existing) == phibase_sourced_resistance_view(record)
    ) and (
        mibig_sourced_producer_view(existing) == mibig_sourced_producer_view(record)
    ) and (
        fda_sourced_clinical_view(existing) == fda_sourced_clinical_view(record)
    ) and (
        curator_owns_clinical or existing.get("clinical_status") == merged.get("clinical_status")
    ) and all(
        existing.get(f) == merged.get(f)
        for f in ("mode_of_action", "mode_of_action_notes", "mode_of_action_target_scope")
    )
    if unchanged:
        # Nothing the seeder owns changed: keep the trail exactly as it is,
        # rather than appending a new event on every run.
        merged["curation_history"] = history or record.get("curation_history", [])
    else:
        merged["curation_history"] = history
        record_curation_event(
            merged,
            curator=SEEDER_CURATOR,
            action="RESEEDED_FROM_SOURCES",
            changes="Re-seeded from updated data/raw/ inventories",
        )
    # No de-duplication pass here, deliberately. The `unchanged` guard above is
    # the duplicate suppressor: an event is appended ONLY when a seeded field
    # actually moved. So every event a collapse could ever delete is one that
    # records a real change, and `changes` is a constant string that cannot
    # tell two re-seeds apart. A pass that ran here removed 13 events recording
    # genuine mechanism assignments (nikkomycin-z's chitin-synthase fix among
    # them) and would have swallowed every future ChEBI release the same way.
    # The 2,923 duplicates that motivated it were the symptom of a falsified
    # `retrieved_on`; that cause is fixed in extract_source_inventory.py, and
    # deleting the trail rather than the cause removed the only detector there
    # was. See #73.
    return _restore_key_order(merged, existing)


def read_lockfile() -> dict[str, str]:
    if not PATHS_FILE.exists():
        return {}
    with PATHS_FILE.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["slug"] for r in csv.DictReader(fh, delimiter="\t")}


def read_lockfile_paths() -> dict[str, Path]:
    """Identifier -> the path the record occupied at the last full seed.

    A record's directory is its class, and a class can change when upstream data
    changes — 21 records moved on one commit during this repository's own
    scaffolding. Resolving the existing file only at the NEW path meant a moved
    record was treated as brand new: the curated file sat unread in the old
    directory, every curator field was replaced by the empty seeded shape, and
    `--prune` then deleted the original. The lockfile already records the class,
    so use it.
    """
    if not PATHS_FILE.exists():
        return {}
    out: dict[str, Path] = {}
    with PATHS_FILE.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            directory = CLASS_DIRS.get(row.get("antimicrobial_class", ""))
            if directory:
                out[row["identifier"]] = CORPUS_DIR / directory / f"{row['slug']}.yaml"
    return out


def write_lockfile(records: dict[str, dict], slugs: dict[str, str],
                   *, only: set[str] | None = None) -> None:
    """Write PATHS.tsv, and move anything that dropped out into RETIRED.tsv.

    With `only`, rows for the named identifiers are merged into the existing
    lockfile instead of rewriting it: the canary step writes one record, and
    leaving its slug out of PATHS.tsv left the repository failing its own
    integrity test until a full seed ran — on a step the documentation makes
    mandatory before every bulk write.
    """
    PATHS_FILE.parent.mkdir(parents=True, exist_ok=True)
    previous = read_lockfile()
    previous_classes = {}
    if PATHS_FILE.exists():
        with PATHS_FILE.open(newline="", encoding="utf-8") as fh:
            previous_classes = {r["identifier"]: r.get("antimicrobial_class", "")
                                for r in csv.DictReader(fh, delimiter="\t")}

    if only is None:
        rows = {i: (records[i]["antimicrobial_class"], slugs[i]) for i in records}
    else:
        rows = {i: (previous_classes.get(i, ""), previous[i]) for i in previous}
        for identifier in only:
            rows[identifier] = (records[identifier]["antimicrobial_class"], slugs[identifier])

    with PATHS_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["identifier", "antimicrobial_class", "slug"])
        for identifier in sorted(rows):
            writer.writerow([identifier, rows[identifier][0], rows[identifier][1]])

    # Anything that was in the lockfile and is not produced any more is retired,
    # not forgotten: its slug stays reserved. A returning identifier is removed
    # from the ledger and reclaims its slug via assign_slugs.
    #
    # This runs on a PARTIAL write too. `just seed-canary` on a re-admitted
    # compound writes its PATHS.tsv row, and skipping the reconciliation left
    # that identifier in both files — turning the gate red on the step CLAUDE.md
    # makes mandatory before every bulk write.
    retired = read_retired()
    retired_dates = {}
    if RETIRED_FILE.exists():
        with RETIRED_FILE.open(newline="", encoding="utf-8") as fh:
            retired_dates = {r["identifier"]: r.get("retired_on", "")
                             for r in csv.DictReader(fh, delimiter="\t")}
    today = date.today().isoformat()
    for identifier, slug in previous.items():
        if only is not None and identifier not in only:
            # A partial run knows nothing about identifiers it did not build, so
            # it must not conclude they are gone.
            continue
        if identifier not in records:
            retired.setdefault(identifier, slug)
            retired_dates.setdefault(identifier, today)
        elif slug != rows.get(identifier, (None, slug))[1]:
            # The identifier survives under a DIFFERENT slug — the documented
            # rename path. The old slug is a published URL and must be reserved
            # too, or the next compound that slugifies to it inherits the address.
            retired.setdefault(f"{identifier}#{slug}", slug)
            retired_dates.setdefault(f"{identifier}#{slug}", today)
    for identifier in list(retired):
        if "#" in identifier:
            # A slug this identifier used to hold. It stays reserved unless the
            # identifier has taken it back — see below.
            owner, _, old_slug = identifier.partition("#")
            if owner in rows and rows[owner][1] == old_slug:
                # The identifier returned to a slug it previously gave up (a
                # rename, then a revert). Keeping the row would make the ledger
                # claim a live URL is retired, which is what
                # test_retired_slugs_are_never_reissued rejects — and no code
                # path could clear it, so the gate would stay red forever.
                retired.pop(identifier)
                retired_dates.pop(identifier, None)
            continue
        if identifier not in records:
            continue
        if only is not None and identifier not in only:
            # A partial run builds every record in memory but WRITES only the
            # named ones. Un-retiring on the strength of the in-memory set would
            # drop an identifier from the ledger without adding it to PATHS.tsv,
            # leaving it in neither file and its published slug reserved nowhere.
            continue
        retired.pop(identifier)
        retired_dates.pop(identifier, None)
    if not retired and not RETIRED_FILE.exists():
        return
    with RETIRED_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["identifier", "slug", "retired_on"])
        for identifier in sorted(retired):
            writer.writerow([identifier, retired[identifier], retired_dates.get(identifier, today)])


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
    phibase_counts = attach_phibase_resistance(records)
    bindingdb_counts = attach_bindingdb_targets(records)
    mibig_counts = attach_mibig_producers(
        records,
        str(manifest.get("sources", {}).get("mibig", {}).get("version", "")),
    )
    fda_counts = attach_fda_clinical_status(records)
    flagged = flag_structure_collisions(records, source_version)

    by_class: dict[str, int] = defaultdict(int)
    for record in records.values():
        by_class[record["antimicrobial_class"]] += 1
    merged = sum(1 for r in records.values() if len(r["source_concepts"]) > 1)

    print(f"{len(concepts)} source concepts -> {len(records)} records", file=sys.stderr)
    print(f"  {merged} records carry more than one source concept", file=sys.stderr)
    if REFUSED_STRUCTURELESS_XREFS:
        print(f"  {len(REFUSED_STRUCTURELESS_XREFS)} unverifiable ChEBI xref(s) refused "
              "(see `just worklist --queue xref-name-conflict`)")
        for _, label, reason in REFUSED_STRUCTURELESS_XREFS:
            print(f"    {label}: {reason}")
    if REFUSED_UNNAMED_PRODUCERS:
        print(f"  {len(REFUSED_UNNAMED_PRODUCERS)} producer claim(s) refused: the taxon "
              "does not identify an organism (see `just worklist --queue "
              "unnamed-producer`)", file=sys.stderr)
        for identifier, _, reason in REFUSED_UNNAMED_PRODUCERS:
            print(f"    {identifier}: {reason}", file=sys.stderr)
    if REFUSED_SPANNING_XREFS:
        accessions = {reason.split(" ", 1)[0] for _, _, reason in REFUSED_SPANNING_XREFS}
        print(f"  {len(accessions)} structure-exact accession(s) withheld from "
              f"{len(REFUSED_SPANNING_XREFS)} record(s) for spanning two structures "
              "(see `just worklist --queue xref-span-conflict`)", file=sys.stderr)
    if MALFORMED_STRUCTURE_IDS:
        print(f"  {len(MALFORMED_STRUCTURE_IDS)} malformed structure accession(s) "
              "skipped (not a PDB/EMDB accession):", file=sys.stderr)
        for source_id, xref in MALFORMED_STRUCTURE_IDS:
            print(f"    {source_id}: {xref}", file=sys.stderr)
    print(f"  {len(skipped)} concepts have no structure and are not written "
          f"(see `just worklist`)", file=sys.stderr)
    if flagged:
        print(f"  {flagged} records flagged with a structure-collision discussion",
              file=sys.stderr)
    print(
        "  PHI-base resistance: "
        f"associations={phibase_counts['matched_associations']} "
        f"records={phibase_counts['matched_records']} "
        f"identity_drift={phibase_counts['identity_drift']}",
        file=sys.stderr,
    )
    print(
        "  BindingDB targets: "
        f"measurements={bindingdb_counts['matched_measurements']} "
        f"assertions={bindingdb_counts['matched_target_assertions']} "
        f"records={bindingdb_counts['matched_records']} "
        f"rejected_non_target_specific="
        f"{bindingdb_counts['rejected_non_target_specific_measurement']} "
        f"ambiguous_or_missing={bindingdb_counts['ambiguous_or_missing_identity']}",
        file=sys.stderr,
    )
    print(
        "  MIBiG producers: "
        f"matched={mibig_counts['matched']} "
        f"refused_unnamed={mibig_counts['refused_unnamed_producer']} "
        f"published={mibig_counts['published']} "
        f"ambiguous={mibig_counts['ambiguous_stereochemistry'] + mibig_counts['ambiguous_corpus_identity']} "
        f"out_of_scope={mibig_counts['out_of_scope']}",
        file=sys.stderr,
    )
    print(
        "  Drugs@FDA status: "
        f"products={fda_counts['matched_products']} records={fda_counts['matched_records']} "
        f"ambiguous_or_missing={fda_counts['ambiguous_or_missing']}",
        file=sys.stderr,
    )
    print("  Per-class records (inclusive and directly filed):", file=sys.stderr)
    for line in format_class_count_rows(dict(by_class)):
        print(line, file=sys.stderr)

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

    previous_paths = read_lockfile_paths()
    written = unchanged = moved = 0
    for identifier in selected:
        record = records[identifier]
        path = record_path(record, slugs[identifier])
        # Where this record lives NOW may not be where it lived last time: read
        # the old location when the class moved, so curation survives the move.
        old_path = previous_paths.get(identifier)
        source = path if path.exists() else (old_path if old_path and old_path.exists() else None)
        existing_text = source.read_text(encoding="utf-8") if source else None
        if existing_text is not None:
            record = merge_with_existing(record, yaml.safe_load(existing_text))
        # Compare the PARSED record, not its serialized text. YAML mapping order
        # carries no meaning, and comparing text would rewrite every reviewed
        # record after an otherwise unrelated source refresh.
        #
        # The insertion-position drift this originally guarded against is gone:
        # `_restore_key_order` now keeps a merged record in the order it already
        # had on disk (#216). So `--force` no longer normalizes key order either
        # -- it re-emits each record in its own stored order. Imposing one order
        # across the corpus is #244, and it needs the emitter, not this flag.
        if (
            source == path
            and not args.force
            and record_yaml_matches(existing_text, record)
        ):
            unchanged += 1
            continue
        try:
            write_validated_antibiotic(record, path)
            written += 1
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1
        if source is not None and source != path:
            # The record changed class. Remove the old file here rather than
            # leaving it for --prune: two files for one identifier is a state
            # the integrity tests reject, and a partial run should not create it.
            source.unlink()
            moved += 1
            print(f"  moved {identifier}: {source.relative_to(REPO_ROOT)} -> "
                  f"{path.relative_to(REPO_ROOT)}", file=sys.stderr)

    if not args.only and not args.limit:
        write_lockfile(records, slugs)
    elif selected:
        write_lockfile(records, slugs, only=set(selected))

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

    print(f"wrote {written} records ({unchanged} already current"
          + (f", {moved} moved between classes" if moved else "") + ")", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

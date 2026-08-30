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
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
RETIRED_FILE = CORPUS_DIR / "RETIRED.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"

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
    "curation_status", "grounding_notes", "evidence",
    "cidality", "biosynthesis_origin", "clinical_status",
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
                 "structural_class_id", "minted", "mechanism_roles")

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
        self.mechanism_roles: list[str] = []
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


def classify(roles: list[str], conf: dict, from_aro: bool,
             aro_class_ids: tuple[str, ...] = ()) -> str:
    """Assign the filesystem/reporting class.

    Order of evidence, strongest first:

    1. **A CARD drug class whose name states a target group** — "triazole
       antifungal", "polyene antifungal". That is a curated, compound-specific
       classification and outranks a generic role tag: ChEBI gives fluconazole
       and amphotericin B an `antibacterial agent` role, and taking that at face
       value filed both as antibacterials.
    2. **ChEBI roles**, by the priority table in conf/sources.yaml (narrower
       target group first, bacteria before fungi and protozoa).
    3. **The ARO fallback**, ANTIBACTERIAL — for a CARD molecule with no ChEBI
       role and no group-naming drug class.

    A fourth step, filing on a ChEBI structural class whose name states a target
    group, was tried and removed: a chemical class is not a target claim, and it
    filed chemotherapy drugs, an insecticide and bare ring scaffolds as
    antibacterial. See conf/sources.yaml. Compounds whose only reviewed role is
    the generic `antimicrobial agent` keep ANTIMICROBIAL_UNSPECIFIED, which is
    what the sources say.

    Classes whose names do not state a group are absent from the map on purpose;
    see conf/sources.yaml.
    """
    class_map = conf.get("aro_class_to_class", {})
    for class_id in aro_class_ids:
        if class_id in class_map:
            return class_map[class_id]

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
        concept.mechanism_roles = split_pipe(row.get("mechanism_role_ids", ""))
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
                f"second activity. Not a curator's mechanistic review.")
    return (f"ChEBI asserts the role on the compound, but this mechanism belongs to an "
            f"{implied.lower().replace('anti', 'anti-')} activity while the record is filed "
            f"as {antimicrobial_class}. Either the compound has both activities, or the "
            f"filing is wrong — the priority table has put azole antifungals under "
            f"ANTIBACTERIAL before now. A curator should decide which. Not a curator's "
            f"mechanistic review.")


def mode_of_action_from_roles(mechanism_roles: list[str], conf: dict,
                              role_names: dict[str, str],
                              antimicrobial_class: str | None = None) -> tuple[str, str] | None:
    """(mode_of_action, notes) from ChEBI's mechanism roles, or None.

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
    tail = ("ChEBI asserts the role on the compound; the role names a mechanism, not the "
            "organism it acts on. Not a curator's mechanistic review.")

    if len(values) == 1:
        value = values[0]
        return value, f"{MOA_NOTE_MARKER} {cited}. {_cross_activity_note(value, antimicrobial_class) or tail}"

    # The MULTIPLE branch needs the caveat too: a record can carry several
    # mechanisms and still have one of them belong to another activity.
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
                        f"a curator should decide whether one is primary.{extra} Not a "
                        f"curator's mechanistic review.")


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
        "antimicrobial_class": classify(
            roles, conf, from_aro=bool(aro),
            aro_class_ids=tuple(c.structural_class_id for c in aro if c.structural_class_id),
        ),
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
        record["mode_of_action"], record["mode_of_action_notes"] = moa

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
    return bool(re.search(r"(?:^|[\n.;:!?)\]]|\s[-\u2013\u2014])\s*" + re.escape(CURATOR_NOTE_MARKER),
                          text.strip(), re.IGNORECASE))


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
        if "mode_of_action" in existing:
            merged["mode_of_action"] = existing["mode_of_action"]
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
    # The comparison covers the CARD mechanism sections too: a refresh that adds
    # determinants rewrites the file, and an audit trail that says nothing
    # happened would be worse than none.
    unchanged = all(existing.get(f) == record.get(f) for f in SEEDED_FIELDS) and all(
        card_sourced_view(existing, f) == card_sourced_view(record, f)
        for f in ("molecular_targets", "resistance_mechanisms")
    )
    if unchanged:
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
        if source == path and not args.force and existing_text == emit_antibiotic_yaml(record):
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

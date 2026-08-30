#!/usr/bin/env python3
"""Extract the committed AntibioticMech inventories from ChEBI and CARD/ARO.

The inventories under ``data/raw/`` are the reproducible inputs to seeding:
``just seed-apply`` reads them and never touches the network. Re-run this only
when ChEBI or CARD publish a new release.

    python scripts/extract_source_inventory.py --dry-run   # free check, writes nothing
    python scripts/extract_source_inventory.py             # download + write inventories
    python scripts/extract_source_inventory.py --offline   # reuse downloads/ as-is

What it writes:

    data/raw/chebi_antimicrobials.tsv   one row per ChEBI structure in role scope
    data/raw/aro_antibiotics.tsv        one row per ARO individual antibiotic molecule
    data/raw/aro_resistance_edges.tsv   determinant --confers_resistance_to--> molecule
    data/raw/aro_target_edges.tsv       target --targeted_by_antibiotic--> molecule
    data/raw/MANIFEST.yaml              sha256 + size + retrieval date of every input
                                        and every emitted inventory

Scope decisions (which roles count as antimicrobial, which ChEBI star rating is
trusted) live in ``conf/sources.yaml``, not here.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import re
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
RAW_DIR = REPO_ROOT / "data" / "raw"

CHEBI_INVENTORY = "chebi_antimicrobials.tsv"
ARO_INVENTORY = "aro_antibiotics.tsv"
ARO_RESISTANCE = "aro_resistance_edges.tsv"
ARO_TARGETS = "aro_target_edges.tsv"
CHEBI_ROLE_NAMES = "chebi_role_names.tsv"
MANIFEST = "MANIFEST.yaml"

CHEBI_COLUMNS = [
    "chebi_id", "name", "definition", "stars", "in_role_scope",
    "role_ids", "parent_ids", "smiles", "standard_inchi", "standard_inchi_key",
    "molecular_formula", "charge", "average_mass", "monoisotopic_mass",
    "synonyms", "xrefs", "citations", "mechanism_role_ids",
]

# An accession that is not CURIE-safe cannot become an xref: the schema's CURIE
# pattern rejects it, and a mangled identifier is worse than a missing one.
CURIE_SAFE = re.compile(r"^[A-Za-z0-9._-]+$")

# ChEBI's accession `type` column says what KIND of identifier a row holds; the
# resource it belongs to is `source_id`. A CAS-type row carries a CAS number
# whatever database contributed it, so the type wins for that one case.
CITATION_PREFIX = {"PubMed": "PMID", "PubMed Central": "PMC", "DOI": "DOI"}
ARO_COLUMNS = [
    "aro_id", "name", "definition", "definition_refs", "parent_ids",
    "drug_class_id", "drug_class_label", "synonyms", "xrefs", "classification",
]
RESISTANCE_COLUMNS = [
    "determinant_id", "determinant_name", "relation", "antibiotic_id",
    "antibiotic_name", "mechanism", "mechanism_source_id",
]
TARGET_COLUMNS = ["target_id", "target_name", "target_definition", "antibiotic_id", "antibiotic_name"]
ROLE_NAME_COLUMNS = ["role_id", "name", "used_for"]


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path, *, offline: bool) -> Path:
    if dest.exists() and (offline or dest.stat().st_size > 0):
        return dest
    if offline:
        raise SystemExit(f"--offline but {dest} is missing; run without --offline once")
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  downloading {url}", file=sys.stderr)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(url) as resp, tmp.open("wb") as out:  # noqa: S310 - fixed hosts from conf
        while chunk := resp.read(1 << 20):
            out.write(chunk)
    tmp.replace(dest)
    return dest


def tsv_gz_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as fh:
        yield from csv.DictReader(fh, delimiter="\t")


def transitive(seeds, edges: dict[str, list[str]]) -> set[str]:
    """Every node reachable from ``seeds`` along ``edges`` (seeds included)."""
    seen = set(seeds)
    stack = list(seeds)
    while stack:
        node = stack.pop()
        for nxt in edges.get(node, ()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


_MARKUP = re.compile(r"</?(?:i|b|em|small|sub|sup|strong|span)\b[^>]*>", re.IGNORECASE)


def flat(value) -> str:
    """Collapse a cell to a single line of plain text.

    ChEBI names and definitions carry HTML markup (``<i>R</i>``, ``<small>L</small>``)
    for stereochemistry and configuration prefixes. It is dropped here rather
    than in the seeder so the inventories themselves are greppable: a curator
    searching for "(R)-linalool" should find the row. The information lost is
    typographic, not chemical — the structure fields carry the stereochemistry
    unambiguously.
    """
    return " ".join(_MARKUP.sub("", str(value)).split())


def pipe(values) -> str:
    """Join a list into one TSV cell. '|' inside a member is replaced, so the
    cell always splits back into the same number of members."""
    return "|".join(flat(v).replace("|", "/") for v in values if str(v).strip())


# --------------------------------------------------------------------------
# ChEBI
# --------------------------------------------------------------------------

def role_name_rows(conf: dict, compounds: dict, acc2id: dict) -> list[dict]:
    """Labels for every ChEBI role this repository references.

    Records carry role CURIEs in `activity_roles` and nothing anywhere says what
    they mean, so a consumer reading `CHEBI:33282` has to go and look it up. This
    is the smallest inventory that fixes that, and it is what lets a seeded
    mode_of_action note name the role it came from.
    """
    used: dict[str, set[str]] = {}
    for accession in conf["role_scope"]["in_scope"]:
        used.setdefault(accession, set()).add("scope")
    for accession in conf.get("role_to_class", {}):
        used.setdefault(accession, set()).add("class")
    for accession in {**conf.get("role_to_mode_of_action", {}),
                      **conf.get("role_to_mode_of_action_eukaryotic", {})}:
        used.setdefault(accession, set()).add("mode_of_action")
    rows = []
    for accession, purposes in sorted(used.items()):
        cid = acc2id.get(accession)
        if cid is None:
            continue
        rows.append({"role_id": accession, "name": flat(compounds[cid]["name"]),
                     "used_for": ",".join(sorted(purposes))})
    return rows


def extract_chebi(conf: dict, *, offline: bool, aro_chebi_xrefs: set[str]) -> list[dict]:
    """ChEBI compounds bearing an in-scope antimicrobial role, plus any ChEBI id
    cross-referenced by an ARO antibiotic molecule.

    The second group matters: an ARO molecule whose ChEBI term happens not to
    carry an antimicrobial role (ChEBI files roles inconsistently for older
    entries) still needs its structure, and CARD's assertion that the compound
    is an antibiotic is itself evidence. Those rows are marked
    ``in_role_scope=false`` so the seeder can tell the two populations apart.
    """
    cfg = conf["chebi"]
    base = cfg["flat_files_base"]
    paths = {name: download(base + name, DOWNLOAD_DIR / name, offline=offline) for name in cfg["files"]}

    compounds = {r["id"]: r for r in tsv_gz_rows(paths["compounds.tsv.gz"])}
    acc2id = {r["chebi_accession"]: cid for cid, r in compounds.items()}

    isa_parents: dict[str, list[str]] = defaultdict(list)
    isa_children: dict[str, list[str]] = defaultdict(list)
    has_role: dict[str, list[str]] = defaultdict(list)
    # ChEBI stamps each RELATION with its own review status (1 CHECKED, 3 OK,
    # 9 SUBMITTED). `min_stars` governs the compound entry, not the edges hanging
    # off it, so a manually curated 3-star compound can still carry an
    # automatically submitted, unreviewed role edge — which is how two
    # antiretrovirals (zidovudine, efavirenz) entered a corpus whose scope
    # excludes antivirals, on the strength of a bogus `antitubercular agent`
    # assertion. Trust the same statuses here that compounds are filtered on.
    allowed_status = {str(s) for s in cfg.get("relation_status_allowed", [1, 3])}
    for r in tsv_gz_rows(paths["relation.tsv.gz"]):
        if r.get("status_id") not in allowed_status:
            continue
        if r["relation_type_id"] == "5":       # is_a
            isa_parents[r["init_id"]].append(r["final_id"])
            isa_children[r["final_id"]].append(r["init_id"])
        elif r["relation_type_id"] == "4":     # has_role
            has_role[r["init_id"]].append(r["final_id"])


    # Mechanism roles are collected separately from the antimicrobial roles that
    # decide scope: a compound is in this corpus because of the latter, and
    # describes its mechanism with the former. Both are read from the same
    # reviewed has_role edges.
    # BOTH maps. Reading only the unconditional one desynced conf from the
    # committed inventory: roles moved into the eukaryotic map vanished from
    # mechanism_role_ids on the next extraction, and roles added to it never
    # arrived at all — which made a role addition inert while looking applied.
    mechanism_map = {**conf.get("role_to_mode_of_action", {}),
                     **conf.get("role_to_mode_of_action_eukaryotic", {})}
    mechanism_ids = {acc2id[a] for a in mechanism_map if a in acc2id}

    scope = conf["role_scope"]
    out_roles = transitive([acc2id[a] for a in scope["out_of_scope"] if a in acc2id], isa_children)
    in_roles = transitive([acc2id[a] for a in scope["in_scope"] if a in acc2id], isa_children) - out_roles

    # A compound inherits the mechanism roles asserted on its ancestors, the same
    # way it inherits an antimicrobial role.
    mechanism_of: dict[str, set[str]] = defaultdict(set)
    for bearer, bearer_roles in has_role.items():
        hit = {r for r in bearer_roles if r in mechanism_ids}
        if not hit:
            continue
        for descendant in transitive([bearer], isa_children):
            mechanism_of[descendant] |= hit

    direct = {c: [r for r in roles if r in in_roles] for c, roles in has_role.items()
              if any(r in in_roles for r in roles)}
    # A subclass of a compound bearing a role bears it too (ChEBI asserts the
    # role once, on the parent). Inheritance applies to EVERY descendant,
    # including one that already carries roles of its own: a compound with a
    # direct `antitubercular agent` edge still inherits `antibacterial agent`
    # from its parent. Skipping those cost 455 compounds an ancestor role and
    # misfiled three of them, while `activity_roles` claimed to be complete.
    inherited: dict[str, list[str]] = {}
    for bearer, roles in direct.items():
        for cid in transitive([bearer], isa_children):
            if cid != bearer:
                inherited.setdefault(cid, []).extend(roles)

    min_stars = int(cfg.get("min_stars", 3))
    wanted: dict[str, list[str]] = {}
    for cid, roles in list(direct.items()) + list(inherited.items()):
        wanted.setdefault(cid, []).extend(roles)
    for acc in aro_chebi_xrefs:
        cid = acc2id.get(acc)
        if cid:
            wanted.setdefault(cid, [])

    # Structures, properties, names and cross-references, for wanted rows only.
    structures: dict[str, dict] = {}
    for r in tsv_gz_rows(paths["structures.tsv.gz"]):
        cid = r["compound_id"]
        if cid not in wanted:
            continue
        if r["default_structure"].strip().lower() not in ("true", "t", "1"):
            continue
        structures[cid] = r
    props: dict[str, dict] = {}
    for r in tsv_gz_rows(paths["chemical_data.tsv.gz"]):
        if r["compound_id"] in wanted and r.get("formula"):
            props.setdefault(r["compound_id"], r)
    sources = {r["id"]: (r["name"], r["prefix"]) for r in tsv_gz_rows(paths["source.tsv.gz"])}
    xrefs: dict[str, list[str]] = defaultdict(list)
    citations: dict[str, list[str]] = defaultdict(list)
    for r in tsv_gz_rows(paths["database_accession.tsv.gz"]):
        if r["compound_id"] not in wanted:
            continue
        accession = (r["accession_number"] or "").strip()
        source_name, source_prefix = sources.get(r["source_id"], ("", ""))
        if not accession or not CURIE_SAFE.match(accession):
            continue
        if r["type"] == "CITATION":
            prefix = CITATION_PREFIX.get(source_name)
            if prefix:
                citations[r["compound_id"]].append(f"{prefix}:{accession}")
            continue
        prefix = "cas" if r["type"] == "CAS" else source_prefix
        if prefix:
            xrefs[r["compound_id"]].append(f"{prefix}:{accession}")
    names: dict[str, list[str]] = defaultdict(list)
    for r in tsv_gz_rows(paths["names.tsv.gz"]):
        if r["compound_id"] in wanted and r.get("name"):
            names[r["compound_id"]].append(f"{r['type']}={r['name']}")

    rows = []
    for cid, roles in sorted(wanted.items(), key=lambda kv: int(kv[0])):
        rec = compounds.get(cid)
        if rec is None or rec.get("status_id") not in ("1", "3"):
            continue
        if int(rec.get("stars") or 0) < min_stars and rec["chebi_accession"] not in aro_chebi_xrefs:
            continue
        struct = structures.get(cid, {})
        prop = props.get(cid, {})
        role_accs = sorted({compounds[r]["chebi_accession"] for r in set(roles) if r in compounds})
        parents = sorted({compounds[p]["chebi_accession"]
                          for p in isa_parents.get(cid, []) if p in compounds})
        rows.append({
            "chebi_id": rec["chebi_accession"],
            "name": flat(rec["name"]),
            "definition": flat((rec.get("definition") or "").strip('"')),
            "stars": rec.get("stars", ""),
            "in_role_scope": "true" if role_accs else "false",
            "role_ids": pipe(role_accs),
            "parent_ids": pipe(parents),
            "smiles": (struct.get("smiles") or "").strip(),
            "standard_inchi": (struct.get("standard_inchi") or "").strip(),
            "standard_inchi_key": (struct.get("standard_inchi_key") or "").strip(),
            "molecular_formula": prop.get("formula", ""),
            "charge": prop.get("charge", ""),
            "average_mass": prop.get("mass", ""),
            "monoisotopic_mass": prop.get("monoisotopic_mass", ""),
            "synonyms": pipe(sorted({flat(n) for n in names.get(cid, [])})[:40]),
            "xrefs": pipe(sorted(set(xrefs.get(cid, [])))),
            # ChEBI's own reference list for the entry. Not seeded into records:
            # a reference cited by a ChEBI entry supports the compound, not
            # necessarily any antimicrobial claim made about it. It is committed
            # so a curator writing evidence has the starting set at hand.
            "citations": pipe(sorted(set(citations.get(cid, [])))[:10]),
            "mechanism_role_ids": pipe(sorted(
                compounds[r]["chebi_accession"] for r in mechanism_of.get(cid, ()))),
        })
    return rows, role_name_rows(conf, compounds, acc2id)


# --------------------------------------------------------------------------
# ARO
# --------------------------------------------------------------------------

def parse_obo(path: Path) -> dict[str, dict[str, list[str]]]:
    terms: dict[str, dict[str, list[str]]] = {}
    text = path.read_text(encoding="utf-8", errors="replace")
    for block in text.split("\n[")[1:]:
        if not block.startswith("Term]"):
            continue
        fields: dict[str, list[str]] = defaultdict(list)
        for line in block.splitlines()[1:]:
            if line.startswith("[") or ": " not in line:
                continue
            key, value = line.split(": ", 1)
            fields[key].append(value.strip())
        if fields.get("id") and "is_obsolete" not in fields:
            terms[fields["id"][0]] = dict(fields)
    return terms


def _obo_name(terms, tid):
    return terms.get(tid, {}).get("name", [tid])[0]


def _obo_def(term) -> tuple[str, str]:
    """Split an OBO def: line into (text, pipe-joined references)."""
    raw = term.get("def", [""])[0]
    if not raw.startswith('"'):
        return raw, ""
    end = raw.rfind('"')
    text = raw[1:end]
    refs = raw[end + 1:].strip()
    refs = refs.strip("[]")
    return text, pipe(r.strip() for r in refs.split(",") if r.strip())


def extract_aro(conf: dict, *, offline: bool):
    cfg = conf["aro"]
    path = download(cfg["url"], DOWNLOAD_DIR / "aro.obo", offline=offline)
    terms = parse_obo(path)

    children: dict[str, list[str]] = defaultdict(list)
    parents: dict[str, list[str]] = defaultdict(list)
    # `mechanism_parents` additionally follows participates_in. ARO does NOT
    # link a determinant to its mechanism category by is_a — `antibiotic efflux`
    # (ARO:0010000) is not an is_a ancestor of anything. The link is carried by
    # participates_in on ten determinant-family roots (efflux pump complex or
    # subunit, antibiotic target protection protein, ...). Walking is_a alone
    # made eight of the ten mechanism categories unassignable, ANTIBIOTIC_EFFLUX
    # among them, and left 2,252 of 4,555 rows UNKNOWN.
    mechanism_parents: dict[str, list[str]] = defaultdict(list)
    for tid, term in terms.items():
        for entry in term.get("is_a", []):
            pid = entry.split()[0]
            children[pid].append(tid)
            parents[tid].append(pid)
            mechanism_parents[tid].append(pid)
        for rel in term.get("relationship", []):
            parts = rel.split()
            if len(parts) >= 2 and parts[0] == "participates_in":
                mechanism_parents[tid].append(parts[1])

    subtree = transitive([cfg["molecule_root"]], children) - {cfg["molecule_root"]}
    marker = cfg["drug_class_marker"]

    def is_class(tid: str) -> bool:
        return marker in terms[tid].get("property_value", [])

    molecules = sorted(t for t in subtree if not is_class(t))

    rows, chebi_xrefs = [], set()
    for tid in molecules:
        term = terms[tid]
        definition, refs = _obo_def(term)
        xrefs = [x for x in term.get("xref", [])]
        chebi_xrefs.update(x for x in xrefs if x.startswith("CHEBI:"))
        # Nearest ancestor that IS a drug class: the molecule's structural class.
        # A tie at the same depth is left EMPTY rather than broken by file
        # order: lassomycin has both `rifamycin antibiotic` and `lasso peptide
        # antibiotics` as parents, and picking whichever line came first in
        # aro.obo asserted it is a rifamycin, which it is not. structural_class_id
        # now also feeds class assignment, so a wrong pick moves a record.
        drug_class = ""
        frontier, seen = sorted(parents.get(tid, [])), set()
        while frontier:
            hits = sorted({pid for pid in frontier if pid in terms and is_class(pid)})
            if hits:
                drug_class = hits[0] if len(hits) == 1 else ""
                break
            nxt = []
            for pid in frontier:
                if pid in seen or pid not in terms:
                    continue
                seen.add(pid)
                nxt.extend(parents.get(pid, []))
            frontier = sorted(set(nxt))
        rows.append({
            "aro_id": tid,
            "name": flat(term.get("name", [""])[0]),
            "definition": flat(definition),
            "definition_refs": refs,
            "parent_ids": pipe(parents.get(tid, [])),
            "drug_class_id": drug_class,
            "drug_class_label": flat(_obo_name(terms, drug_class)) if drug_class else "",
            "synonyms": pipe(s.split('"')[1] for s in term.get("synonym", []) if '"' in s),
            "xrefs": pipe(sorted(set(xrefs))),
            "classification": pipe(term.get("property_value", [])),
        })

    molecule_set = set(molecules)
    mech_map = conf["aro_mechanism_map"]

    def mechanism_for(determinant: str) -> tuple[str, str]:
        """Nearest mapped ancestor over is_a + participates_in; UNKNOWN if none.

        Breadth-first so the NEAREST classification wins, and every level is
        walked in sorted order so a determinant with two equally-near mechanism
        ancestors resolves the same way on every machine and every run — a set
        iteration here would make the committed inventory depend on
        PYTHONHASHSEED. Seven determinants (the mycobacterial iniA/iniB/iniC
        family) are genuinely ambiguous between target alteration and efflux;
        `mechanism_source_id` records which ancestor was used, so a curator can
        see the choice rather than having to reverse-engineer it.
        """
        seen = {determinant}
        frontier = [determinant]
        while frontier:
            hits = []
            nxt = []
            for node in sorted(frontier):
                for parent in sorted(mechanism_parents.get(node, ())):
                    if parent in seen:
                        continue
                    seen.add(parent)
                    nxt.append(parent)
                    if parent in mech_map and mech_map[parent] != "UNKNOWN":
                        hits.append((parent, mech_map[parent]))
            if hits:
                ancestor, mechanism = sorted(hits)[0]
                return mechanism, ancestor
            frontier = nxt
        return "UNKNOWN", ""

    resistance_rows, target_rows = [], []
    for tid, term in terms.items():
        for rel in term.get("relationship", []):
            parts = rel.split()
            if len(parts) < 2:
                continue
            kind, target = parts[0], parts[1]
            if target not in molecule_set:
                continue
            if kind == "confers_resistance_to_antibiotic":
                mech, source = mechanism_for(tid)
                resistance_rows.append({
                    "determinant_id": tid,
                    "determinant_name": flat(term.get("name", [""])[0]),
                    "relation": kind,
                    "antibiotic_id": target,
                    "antibiotic_name": flat(_obo_name(terms, target)),
                    "mechanism": mech,
                    "mechanism_source_id": source,
                })
            elif kind == "targeted_by_antibiotic":
                definition, _ = _obo_def(term)
                target_rows.append({
                    "target_id": tid,
                    "target_name": flat(term.get("name", [""])[0]),
                    "target_definition": flat(definition),
                    "antibiotic_id": target,
                    "antibiotic_name": flat(_obo_name(terms, target)),
                })

    resistance_rows.sort(key=lambda r: (r["antibiotic_id"], r["determinant_id"]))
    target_rows.sort(key=lambda r: (r["antibiotic_id"], r["target_id"]))
    return rows, resistance_rows, target_rows, chebi_xrefs


# --------------------------------------------------------------------------
# writing
# --------------------------------------------------------------------------

def write_tsv(path: Path, columns: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, delimiter="\t",
                                lineterminator="\n", extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def _row_count(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _ in csv.DictReader(fh, delimiter="\t"))


def build_manifest(conf: dict, inventories: dict[str, Path]) -> dict:
    downloads: dict[str, dict] = {}
    for name in conf["chebi"]["files"]:
        p = DOWNLOAD_DIR / name
        if p.exists():
            downloads[name] = {
                "url": conf["chebi"]["flat_files_base"] + name,
                "bytes": p.stat().st_size,
                "sha256": sha256_of(p),
            }
    aro = DOWNLOAD_DIR / "aro.obo"
    if aro.exists():
        downloads["aro.obo"] = {
            "url": conf["aro"]["url"],
            "bytes": aro.stat().st_size,
            "sha256": sha256_of(aro),
        }
    # When the upstream files were actually FETCHED, not when this script last
    # ran. `download()` reuses a cached file without re-fetching, so stamping
    # today unconditionally claimed a retrieval that never happened — and
    # because `source_version` is a seeded field, that flipped on all 2923
    # records and gave every one a RESEEDED_FROM_SOURCES event for an update
    # that did not occur. The files' own mtimes are the honest answer and, unlike
    # carrying the previous manifest forward, they correct a date already wrong.
    # Resolved in UTC, not the local zone. These mtimes are 17:05-17:21 PDT,
    # which is 00:05-00:21 the NEXT day in UTC: `date.fromtimestamp` would give
    # a collaborator or CI runner in UTC a different `retrieved_on` from the
    # same bytes, flip `source_version` on every record and append a re-seed
    # event for an update that did not happen. That is #69's failure mode
    # arriving through the timezone door. The repo already stamps every
    # curation timestamp in UTC (curate.curation_event.now_iso).
    fetched = [(DOWNLOAD_DIR / name).stat().st_mtime
               for name in downloads if (DOWNLOAD_DIR / name).exists()]
    if not fetched:
        # Falling back to today() would assert a retrieval that never happened,
        # which is exactly #69. Unreachable on the normal path (download() runs
        # first), so if it ever fires something is wrong enough to stop for.
        raise SystemExit(
            "No manifested download is present in downloads/; cannot date the "
            "retrieval. Run `just download` before building the manifest.")
    retrieved_on = datetime.fromtimestamp(max(fetched), tz=timezone.utc).date().isoformat()

    return {
        "retrieved_on": retrieved_on,
        "generated_by": "scripts/extract_source_inventory.py",
        "sources": {
            "chebi": {"homepage": conf["chebi"]["homepage"], "license": conf["chebi"]["license"],
                      "min_stars": conf["chebi"]["min_stars"]},
            "aro": {"homepage": conf["aro"]["homepage"], "license": conf["aro"]["license"],
                    "molecule_root": conf["aro"]["molecule_root"]},
        },
        "downloads": downloads,
        "inventories": {
            name: {
                "rows": _row_count(path),
                "bytes": path.stat().st_size,
                "sha256": sha256_of(path),
            }
            for name, path in sorted(inventories.items())
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would be written, touch no file under data/raw/.")
    parser.add_argument("--offline", action="store_true",
                        help="Use whatever is already in downloads/; never fetch.")
    args = parser.parse_args()

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))

    print("=== ARO (CARD) ===", file=sys.stderr)
    aro_rows, resistance_rows, target_rows, aro_chebi_xrefs = extract_aro(conf, offline=args.offline)
    print(f"  {len(aro_rows)} individual antibiotic molecules "
          f"({len(aro_chebi_xrefs)} with a ChEBI cross-reference)", file=sys.stderr)
    print(f"  {len(resistance_rows)} resistance edges, {len(target_rows)} target edges", file=sys.stderr)

    print("=== ChEBI ===", file=sys.stderr)
    chebi_rows, role_names = extract_chebi(conf, offline=args.offline,
                                           aro_chebi_xrefs=aro_chebi_xrefs)
    with_structure = sum(1 for r in chebi_rows if r["standard_inchi_key"])
    in_scope = sum(1 for r in chebi_rows if r["in_role_scope"] == "true")
    print(f"  {len(chebi_rows)} compounds ({in_scope} in role scope, "
          f"{len(chebi_rows) - in_scope} pulled in by an ARO cross-reference)", file=sys.stderr)
    print(f"  {with_structure} carry a default structure with an InChIKey", file=sys.stderr)

    if args.dry_run:
        print("\n--dry-run: nothing written.", file=sys.stderr)
        return 0

    targets = {
        CHEBI_INVENTORY: (CHEBI_COLUMNS, chebi_rows),
        ARO_INVENTORY: (ARO_COLUMNS, aro_rows),
        ARO_RESISTANCE: (RESISTANCE_COLUMNS, resistance_rows),
        ARO_TARGETS: (TARGET_COLUMNS, target_rows),
        CHEBI_ROLE_NAMES: (ROLE_NAME_COLUMNS, role_names),
    }
    written = {}
    for name, (columns, rows) in targets.items():
        path = RAW_DIR / name
        write_tsv(path, columns, rows)
        written[name] = path
        print(f"  wrote {path.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)

    manifest = build_manifest(conf, written)
    # pubchem_structures.tsv is written by a later, network-dependent step; carry
    # its recorded hash forward rather than dropping provenance on re-extraction.
    old_path = RAW_DIR / MANIFEST
    if old_path.exists():
        previous = yaml.safe_load(old_path.read_text(encoding="utf-8")) or {}
        carried = previous.get("inventories", {}).get("pubchem_structures.tsv")
        if carried and (RAW_DIR / "pubchem_structures.tsv").exists():
            manifest["inventories"]["pubchem_structures.tsv"] = carried
    (RAW_DIR / MANIFEST).write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"  wrote {(RAW_DIR / MANIFEST).relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

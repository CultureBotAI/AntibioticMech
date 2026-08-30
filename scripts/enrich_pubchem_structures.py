#!/usr/bin/env python3
"""Fetch structures from PubChem for ARO molecules ChEBI does not cover.

CARD names 644 individual antibiotic molecules; roughly half carry a ChEBI
cross-reference whose ChEBI entry has a default structure. The rest have a
PubChem CID and nothing else, and a record with no structure is not an
individual chemical structure — so without this step they cannot enter the
corpus at all.

This is the repository's only network-dependent extraction step. Canary it:

    just extract-pubchem-dry                 # print the URL, call nothing
    just extract-pubchem-canary ARO:0000018  # one real call, inspect the row
    just extract-pubchem                     # the batch

Writes data/raw/pubchem_structures.tsv (append-safe: existing rows for CIDs not
in this run are preserved, so a partial batch is resumable and a failed CID does
not erase a good row).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
RAW_DIR = REPO_ROOT / "data" / "raw"
ARO_INVENTORY = RAW_DIR / "aro_antibiotics.tsv"
CHEBI_INVENTORY = RAW_DIR / "chebi_antimicrobials.tsv"
OUT_PATH = RAW_DIR / "pubchem_structures.tsv"

COLUMNS = [
    "pubchem_cid", "aro_id", "aro_name", "molecular_formula", "average_mass",
    "monoisotopic_mass", "charge", "smiles", "standard_inchi",
    "standard_inchi_key", "retrieved_on",
]


def load_tsv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def needs_structure() -> list[tuple[str, str, str]]:
    """(aro_id, aro_name, cid) for ARO molecules with no ChEBI structure."""
    chebi = {r["chebi_id"]: r for r in load_tsv(CHEBI_INVENTORY)}
    out = []
    for row in load_tsv(ARO_INVENTORY):
        xrefs = row["xrefs"].split("|") if row["xrefs"] else []
        chebi_ids = [x for x in xrefs if x.startswith("CHEBI:")]
        if any(chebi.get(c, {}).get("standard_inchi_key") for c in chebi_ids):
            continue
        cids = [x.split(":", 1)[1] for x in xrefs if x.startswith("PubChem:")]
        if cids:
            out.append((row["aro_id"], row["name"], cids[0]))
    return out


def request_url(conf: dict, cid: str) -> str:
    props = ",".join(conf["pubchem"]["properties"])
    return f"{conf['pubchem']['rest_base']}{cid}/property/{props}/JSON"


def fetch(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310 - fixed host from conf
        payload = json.load(resp)
    return payload["PropertyTable"]["Properties"][0]


def to_row(prop: dict, aro_id: str, aro_name: str) -> dict:
    def num(key):
        value = prop.get(key)
        return "" if value in (None, "") else str(value)

    # PubChem renamed CanonicalSMILES to SMILES/ConnectivitySMILES; accept either
    # so an upstream rename degrades to a missing SMILES, not a crash.
    smiles = prop.get("SMILES") or prop.get("ConnectivitySMILES") or prop.get("CanonicalSMILES") or ""
    return {
        "pubchem_cid": str(prop.get("CID", "")),
        "aro_id": aro_id,
        "aro_name": aro_name,
        "molecular_formula": prop.get("MolecularFormula", ""),
        "average_mass": num("MolecularWeight"),
        "monoisotopic_mass": num("MonoisotopicMass"),
        "charge": num("Charge"),
        "smiles": smiles,
        "standard_inchi": prop.get("InChI", ""),
        "standard_inchi_key": prop.get("InChIKey", ""),
        "retrieved_on": date.today().isoformat(),
    }


def update_manifest() -> None:
    """Record this file in data/raw/MANIFEST.yaml.

    The inventory extractor runs before this step, so it cannot manifest a file
    that does not exist yet; without this the one network-sourced inventory in
    the repository would be the only one with no recorded hash.
    """
    manifest_path = RAW_DIR / "MANIFEST.yaml"
    if not manifest_path.exists():
        return
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256(OUT_PATH.read_bytes()).hexdigest()
    manifest.setdefault("inventories", {})[OUT_PATH.name] = {
        "rows": len(load_tsv(OUT_PATH)),
        "bytes": OUT_PATH.stat().st_size,
        "sha256": digest,
        "source": "PubChem PUG REST (scripts/enrich_pubchem_structures.py)",
    }
    manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
                             encoding="utf-8")


def write_rows(rows: dict[str, dict]) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for key in sorted(rows, key=lambda k: rows[k]["aro_id"]):
            writer.writerow(rows[key])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the work and one example URL; make no request.")
    parser.add_argument("--only", nargs="*", default=None, metavar="ARO_ID",
                        help="Fetch only these ARO ids — the canary before the batch.")
    parser.add_argument("--limit", type=int, help="Stop after N successful fetches.")
    args = parser.parse_args()

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    work = needs_structure()
    if args.only:
        wanted = set(args.only)
        work = [w for w in work if w[0] in wanted]
        missing = wanted - {w[0] for w in work}
        if missing:
            print(f"not in the no-structure worklist: {sorted(missing)}", file=sys.stderr)
    if not work:
        print("nothing to fetch", file=sys.stderr)
        return 0

    print(f"{len(work)} ARO molecules need a PubChem structure", file=sys.stderr)
    if args.dry_run:
        aro_id, name, cid = work[0]
        print(f"example: {aro_id} ({name}) CID {cid}", file=sys.stderr)
        print(request_url(conf, cid))
        return 0

    # Keyed by ARO id, not CID: two ARO molecules can point at the same PubChem
    # CID (a salt and its parent, say), and keying on CID would silently drop one
    # of them — the seeder looks rows up by aro_id.
    existing = {r["aro_id"]: r for r in load_tsv(OUT_PATH)} if OUT_PATH.exists() else {}
    delay = 1.0 / float(conf["pubchem"].get("requests_per_second", 3))
    ok = failed = 0
    for aro_id, name, cid in work:
        try:
            prop = fetch(request_url(conf, cid))
        except (urllib.error.URLError, KeyError, IndexError, json.JSONDecodeError) as exc:
            print(f"  FAILED {aro_id} CID {cid}: {exc}", file=sys.stderr)
            failed += 1
            time.sleep(delay)
            continue
        row = to_row(prop, aro_id, name)
        if not row["standard_inchi_key"]:
            print(f"  no InChIKey for {aro_id} CID {cid}; skipped", file=sys.stderr)
            failed += 1
            continue
        existing[aro_id] = row
        ok += 1
        print(f"  {aro_id} {name}: {row['molecular_formula']} {row['standard_inchi_key']}",
              file=sys.stderr)
        if args.limit and ok >= args.limit:
            break
        time.sleep(delay)

    write_rows(existing)
    update_manifest()
    print(f"wrote {OUT_PATH.relative_to(REPO_ROOT)}: {len(existing)} rows "
          f"({ok} fetched now, {failed} failed)", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

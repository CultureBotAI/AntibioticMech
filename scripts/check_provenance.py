#!/usr/bin/env python3
"""Verify every committed inventory is covered by data/raw/MANIFEST.yaml.

A committed TSV with no manifest row has no recorded origin: nobody can tell
which ChEBI or CARD release produced it, or whether it was edited by hand after
extraction. This checks coverage in both directions and re-hashes each file.
"""

from __future__ import annotations

import csv
import hashlib
import sys
import zlib
from pathlib import Path

import yaml
from ncbi_ast_inventory import inventory_metadata, open_activity_text

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def row_count(path: Path) -> int:
    handle = open_activity_text(path) if path.suffix == ".gz" else path.open(newline="", encoding="utf-8")
    with handle as fh:
        return sum(1 for _ in csv.DictReader(fh, delimiter="\t"))


def main() -> int:
    if not MANIFEST_PATH.exists():
        print(f"missing {MANIFEST_PATH}; run `just extract-inventory`", file=sys.stderr)
        return 1
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    recorded = manifest.get("inventories", {})
    on_disk = {p.name for pattern in ("*.tsv", "*.tsv.gz") for p in RAW_DIR.glob(pattern)}

    problems = []
    # pubchem_structures.tsv is produced by a separate network step whose own
    # per-row retrieved_on column is its provenance; it is manifested when the
    # extractor next runs, so its absence from the manifest is not an error.
    optional = {"pubchem_structures.tsv"}

    for name in sorted(on_disk - set(recorded) - optional):
        problems.append(f"  {name}: committed but absent from MANIFEST.yaml")
    for name in sorted(set(recorded) - on_disk):
        problems.append(f"  {name}: in MANIFEST.yaml but not committed")
    for name, entry in sorted(recorded.items()):
        path = RAW_DIR / name
        if not path.exists():
            continue
        actual_sha = sha256_of(path)
        if actual_sha != entry.get("sha256"):
            problems.append(f"  {name}: sha256 {actual_sha[:12]}… != manifest "
                            f"{str(entry.get('sha256'))[:12]}… (edited after extraction?)")
        try:
            if path.suffix == ".gz":
                metadata = inventory_metadata(path)
                for field in ("encoding", "bytes", "content_sha256", "content_bytes"):
                    if entry.get(field) != metadata[field]:
                        problems.append(f"  {name}: {field} differs from manifest or is missing")
            actual_rows = row_count(path)
        except (OSError, EOFError, ValueError, zlib.error) as error:
            problems.append(f"  {name}: cannot read inventory: {error}")
            continue
        if actual_rows != entry.get("rows"):
            problems.append(f"  {name}: {actual_rows} rows != manifest {entry.get('rows')}")

    for name, entry in sorted(manifest.get("downloads", {}).items()):
        for key in ("url", "sha256", "bytes"):
            if not entry.get(key):
                problems.append(f"  download {name}: missing {key}")

    if problems:
        print("provenance check FAILED:", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        return 1

    print(f"provenance OK: {len(recorded)} inventories, "
          f"{len(manifest.get('downloads', {}))} upstream files, "
          f"retrieved {manifest.get('retrieved_on')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

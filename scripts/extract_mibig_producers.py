#!/usr/bin/env python3
"""Extract reviewed MIBiG compound/producer assertions into a compact inventory.

The official archive is cached under ``downloads/`` and is never committed.
The emitted TSV is an offline input to ``seed_from_sources.py``.

    uv run --extra chemical-map python scripts/extract_mibig_producers.py --dry-run
    uv run --extra chemical-map python scripts/extract_mibig_producers.py
    uv run --extra chemical-map python scripts/extract_mibig_producers.py --offline

An entry is called reviewed only when it is active and its changelog contains a
non-placeholder reviewer. Exact Standard InChIKey matching is used only for the
dry-run report; the inventory retains every structurally valid compound from an
eligible entry so future corpus additions can match without reinterpreting names.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import tarfile
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

import yaml
from rdkit import Chem
from rdkit.Chem import inchi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "mibig_producers.tsv"

COLUMNS = [
    "mibig_accession",
    "entry_version",
    "entry_quality",
    "reviewed",
    "reviewer_ids",
    "compound_name",
    "compound_index",
    "smiles",
    "standard_inchi",
    "standard_inchi_key",
    "stereo_complete",
    "taxon_id",
    "taxon_label",
    "primary_reference",
    "reference_basis",
]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url: str, destination: Path, *, offline: bool) -> Path:
    if destination.exists() and destination.stat().st_size:
        return destination
    if offline:
        raise SystemExit(f"--offline but {destination} is missing")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".part")
    print(f"downloading {url}", file=sys.stderr)
    with urllib.request.urlopen(url) as response, temporary.open("wb") as output:  # noqa: S310
        while chunk := response.read(1 << 20):
            output.write(chunk)
    temporary.replace(destination)
    return destination


def archive_entries(path: Path):
    """Yield JSON objects without extracting the upstream tar archive."""
    # Zenodo currently serves this ``.tar.gz`` asset as an uncompressed POSIX
    # tar stream. Auto-detect instead of trusting the filename suffix.
    with tarfile.open(path, "r:*") as archive:
        for member in archive:
            member_path = PurePosixPath(member.name)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise ValueError(f"unsafe path in MIBiG archive: {member.name!r}")
            if not member.isfile() or member_path.suffix != ".json":
                continue
            handle = archive.extractfile(member)
            if handle is None:
                raise ValueError(f"could not read MIBiG member {member.name}")
            yield json.load(handle)


def reviewer_ids(entry: dict, placeholder: str) -> list[str]:
    reviewers = {
        reviewer
        for release in entry.get("changelog", {}).get("releases", [])
        for change in release.get("entries", [])
        for reviewer in change.get("reviewers", [])
        if reviewer and reviewer != placeholder
    }
    return sorted(reviewers)


def normalize_reference(value) -> str:
    if isinstance(value, str):
        prefix, separator, local = value.partition(":")
        if separator and prefix.lower() == "pubmed":
            return f"PMID:{local}"
        if separator and prefix.lower() == "doi":
            return f"DOI:{local}"
        return value
    if isinstance(value, dict):
        kind = str(value.get("type") or value.get("category") or "")
        content = str(value.get("id") or value.get("content") or "")
        if kind and content:
            return normalize_reference(f"{kind}:{content}")
    return ""


def primary_reference(entry: dict, compound: dict) -> tuple[str, str]:
    for evidence in compound.get("evidence", []):
        for reference in evidence.get("references", []):
            normalized = normalize_reference(reference)
            if normalized:
                return normalized, "compound_evidence"
    for reference in entry.get("legacy_references", []):
        normalized = normalize_reference(reference)
        if normalized:
            return normalized, "first_mibig_legacy_reference"
    return "", ""


def structure_fields(smiles: str) -> tuple[dict[str, str], str | None]:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        return {}, "invalid_smiles"
    standard_inchi = inchi.MolToInchi(molecule)
    standard_inchi_key = inchi.InchiToInchiKey(standard_inchi)
    if not standard_inchi or not standard_inchi_key:
        return {}, "inchi_generation_failed"
    potential = Chem.FindPotentialStereo(molecule)
    stereo_complete = all(str(item.specified) != "Unspecified" for item in potential)
    return {
        "standard_inchi": standard_inchi,
        "standard_inchi_key": standard_inchi_key,
        "stereo_complete": str(stereo_complete).lower(),
    }, None


def extract(path: Path, conf: dict) -> tuple[list[dict], Counter]:
    placeholder = conf["mibig"]["reviewer_placeholder"]
    rows: list[dict] = []
    counts: Counter = Counter()
    for entry in archive_entries(path):
        counts["entries_total"] += 1
        reviewers = reviewer_ids(entry, placeholder)
        if entry.get("status") != "active" or not reviewers:
            counts["entries_not_reviewed_active"] += 1
            continue
        counts["entries_reviewed_active"] += 1
        taxonomy = entry.get("taxonomy") or {}
        taxon_id = taxonomy.get("ncbiTaxId")
        taxon_label = str(taxonomy.get("name") or "").strip()
        for index, compound in enumerate(entry.get("compounds", []), start=1):
            counts["compounds_reviewed_active"] += 1
            if not taxon_id or not taxon_label:
                counts["rejected_missing_taxonomy"] += 1
                continue
            smiles = str(compound.get("structure") or "").strip()
            if not smiles:
                counts["rejected_missing_structure"] += 1
                continue
            structure, error = structure_fields(smiles)
            if error:
                counts[f"rejected_{error}"] += 1
                continue
            reference, reference_basis = primary_reference(entry, compound)
            if not reference:
                counts["rejected_missing_reference"] += 1
                continue
            rows.append({
                "mibig_accession": entry["accession"],
                "entry_version": str(entry.get("version") or ""),
                "entry_quality": str(entry.get("quality") or ""),
                "reviewed": "true",
                "reviewer_ids": "|".join(reviewers),
                "compound_name": " ".join(str(compound.get("name") or "").split()),
                "compound_index": str(index),
                "smiles": smiles,
                **structure,
                "taxon_id": str(taxon_id),
                "taxon_label": taxon_label,
                "primary_reference": reference,
                "reference_basis": reference_basis,
            })
            counts["inventory_rows"] += 1
    rows.sort(key=lambda row: (row["mibig_accession"], int(row["compound_index"])))
    return rows, counts


def corpus_keys() -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    exact: dict[str, list[str]] = defaultdict(list)
    connectivity: dict[str, list[str]] = defaultdict(list)
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        key = str((record.get("chemical_structure") or {}).get("standard_inchi_key") or "")
        if key:
            exact[key].append(record["identifier"])
            connectivity[key[:14]].append(record["identifier"])
    return exact, connectivity


def match_report(rows: list[dict]) -> tuple[Counter, list[tuple[str, str, str]]]:
    exact, connectivity = corpus_keys()
    counts: Counter = Counter()
    details: list[tuple[str, str, str]] = []
    for row in rows:
        key = row["standard_inchi_key"]
        exact_hits = exact.get(key, [])
        connected_hits = connectivity.get(key[:14], [])
        name = f"{row['mibig_accession']}:{row['compound_name']}"
        if len(exact_hits) == 1:
            status, detail = "matched", exact_hits[0]
        elif len(exact_hits) > 1:
            status, detail = "ambiguous", "multiple exact corpus records: " + ",".join(exact_hits)
        elif connected_hits or row["stereo_complete"] != "true":
            status = "ambiguous"
            reason = "connectivity-only match" if connected_hits else "unassigned potential stereo"
            detail = reason + (": " + ",".join(connected_hits) if connected_hits else "")
        else:
            status, detail = "out_of_scope", "no exact or connectivity corpus match"
        counts[status] += 1
        details.append((name, status, detail))
    return counts, details


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(conf: dict, archive: Path, inventory: Path) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    cfg = conf["mibig"]
    manifest.setdefault("sources", {})["mibig"] = {
        "homepage": cfg["homepage"],
        "license": cfg["license"],
        "version": cfg["version"],
        "review_policy": "active entry with a non-placeholder changelog reviewer",
    }
    manifest.setdefault("downloads", {})[archive.name] = {
        "url": cfg["archive_url"],
        "bytes": archive.stat().st_size,
        "sha256": sha256_of(archive),
    }
    with inventory.open(newline="", encoding="utf-8") as handle:
        row_count = sum(1 for _ in csv.DictReader(handle, delimiter="\t"))
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": row_count,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": f"MIBiG {cfg['version']} reviewed active entries",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="Use this archive instead of downloads/ cache")
    parser.add_argument("--offline", action="store_true", help="Never download a missing archive")
    parser.add_argument("--dry-run", action="store_true", help="Report counts and write nothing")
    args = parser.parse_args()

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    cfg = conf["mibig"]
    archive = args.archive or DOWNLOAD_DIR / cfg["archive_name"]
    if args.archive:
        if not archive.exists():
            raise SystemExit(f"archive does not exist: {archive}")
    else:
        archive = download(cfg["archive_url"], archive, offline=args.offline)

    rows, extraction = extract(archive, conf)
    matches, details = match_report(rows)
    print(f"MIBiG {cfg['version']}: {extraction['entries_total']} entries", file=sys.stderr)
    print(f"  reviewed active entries: {extraction['entries_reviewed_active']}", file=sys.stderr)
    print(f"  structurally valid producer rows: {len(rows)}", file=sys.stderr)
    print(
        "  dry-run against corpus: "
        f"matched={matches['matched']} ambiguous={matches['ambiguous']} "
        f"rejected={sum(v for k, v in extraction.items() if k.startswith('rejected_'))} "
        f"out_of_scope={matches['out_of_scope']}",
        file=sys.stderr,
    )
    for name, status, detail in details:
        if status != "out_of_scope":
            print(f"    {status:12s} {name}: {detail}", file=sys.stderr)
    for reason, count in sorted(extraction.items()):
        if reason.startswith("rejected_") and count:
            print(f"    {reason}: {count}", file=sys.stderr)

    if args.dry_run:
        print("--dry-run: nothing written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, rows)
    update_manifest(conf, archive, inventory)
    print(f"wrote {inventory.relative_to(REPO_ROOT)} and data/raw/MANIFEST.yaml", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

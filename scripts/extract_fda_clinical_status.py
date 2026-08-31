#!/usr/bin/env python3
"""Join Drugs@FDA regulatory facts to exact GSRS/UNII chemical structures.

The output is a compact, offline seed inventory. Regulatory status comes from
the official Drugs@FDA tables; GSRS supplies identity only.

    just extract-fda-dry
    just extract-fda
    just extract-fda --offline
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml
from rdkit import Chem
from rdkit.Chem import inchi

REPO_ROOT = Path(__file__).resolve().parents[1]
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "fda_clinical_status.tsv"

COLUMNS = [
    "application_number",
    "application_type",
    "product_number",
    "sponsor_name",
    "drug_name",
    "ingredient_name",
    "unii",
    "standard_inchi_key",
    "gsrs_record_version",
    "approval_date",
    "submission_status",
    "marketing_status",
    "currently_marketed",
    "drugsfda_version",
    "drugsfda_retrieved_on",
    "unii_version",
    "gsrs_retrieved_on",
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


def normalized_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    return " ".join(value.upper().split())


def zip_version(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        dates = [info.date_time[:3] for info in archive.infolist() if not info.is_dir()]
    year, month, day = max(dates)
    return f"{year:04d}-{month:02d}-{day:02d}"


def zip_tsv_rows(path: Path, member: str) -> list[dict[str, str]]:
    with (
        zipfile.ZipFile(path) as archive,
        archive.open(member) as binary,
        # FDA's free-text notes include Windows smart quotes (for example 0x92)
        # even though the tables are otherwise ASCII-compatible.
        io.TextIOWrapper(binary, encoding="cp1252", newline="") as text,
    ):
        return [
            {key: (value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(text, delimiter="\t")
        ]


def load_unii_names(path: Path) -> dict[str, list[str]]:
    with zipfile.ZipFile(path) as archive:
        members = [name for name in archive.namelist() if name.endswith(".json")]
        if len(members) != 1:
            raise ValueError(f"expected one JSON member in {path}, found {members}")
        with archive.open(members[0]) as handle:
            payload = json.load(handle)
    names: dict[str, list[str]] = defaultdict(list)
    for row in payload.get("results", []):
        name = normalized_name(str(row.get("substance_name") or ""))
        unii = str(row.get("unii") or "").strip()
        if name and unii and unii not in names[name]:
            names[name].append(unii)
    return names


def approved_originals(path: Path) -> dict[str, tuple[str, str]]:
    """Application number -> (status, earliest approved original date)."""
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in zip_tsv_rows(path, "Submissions.txt"):
        if row["SubmissionType"] == "ORIG" and row["SubmissionStatus"] == "AP":
            date = row["SubmissionStatusDate"].split(" ", 1)[0]
            if date:
                grouped[row["ApplNo"]].append(date)
    return {application: ("AP", min(dates)) for application, dates in grouped.items()}


def eligible_products(path: Path, unii_names: dict[str, list[str]]) -> tuple[list[dict], Counter]:
    counts: Counter = Counter()
    applications = {row["ApplNo"]: row for row in zip_tsv_rows(path, "Applications.txt")}
    originals = approved_originals(path)
    status_labels = {
        row["MarketingStatusID"]: row["MarketingStatusDescription"]
        for row in zip_tsv_rows(path, "MarketingStatus_Lookup.txt")
    }
    product_status = {
        (row["ApplNo"], row["ProductNo"]): status_labels.get(row["MarketingStatusID"], "")
        for row in zip_tsv_rows(path, "MarketingStatus.txt")
    }

    rows: list[dict] = []
    for product in zip_tsv_rows(path, "Products.txt"):
        counts["products_total"] += 1
        ingredient = product["ActiveIngredient"]
        if ";" in ingredient:
            counts["excluded_combination"] += 1
            continue
        original = originals.get(product["ApplNo"])
        if original is None:
            counts["excluded_no_approved_original"] += 1
            continue
        marketing = product_status.get((product["ApplNo"], product["ProductNo"]), "")
        if marketing == "None (Tentative Approval)":
            counts["excluded_tentative"] += 1
            continue
        if not marketing:
            counts["rejected_missing_marketing_status"] += 1
            continue
        uniis = unii_names.get(normalized_name(ingredient), [])
        if not uniis:
            counts["rejected_no_exact_unii_name"] += 1
            continue
        if len(uniis) != 1:
            counts["ambiguous_unii_name"] += 1
            continue
        application = applications.get(product["ApplNo"], {})
        rows.append({
            "application_number": product["ApplNo"],
            "application_type": application.get("ApplType", ""),
            "product_number": product["ProductNo"],
            "sponsor_name": application.get("SponsorName", ""),
            "drug_name": product["DrugName"],
            "ingredient_name": ingredient,
            "unii": uniis[0],
            "approval_date": original[1],
            "submission_status": original[0],
            "marketing_status": marketing,
            "currently_marketed": str(marketing in {"Prescription", "Over-the-counter"}).lower(),
        })
        counts["eligible_single_ingredient_products"] += 1
    return rows, counts


def load_cache(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    records = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            records[row["unii"]] = row
    return records


def compact_substance(row: dict, retrieved_on: str) -> dict:
    unii = str(row.get("unii") or "")
    structure = row.get("structure") or {}
    smiles = str(structure.get("smiles") or "")
    key = ""
    error = ""
    if row.get("substance_class") != "chemical":
        error = f"substance_class:{row.get('substance_class') or 'missing'}"
    elif not smiles:
        error = "missing_smiles"
    else:
        molecule = Chem.MolFromSmiles(smiles)
        if molecule is None:
            error = "invalid_smiles"
        else:
            standard_inchi = inchi.MolToInchi(molecule)
            key = inchi.InchiToInchiKey(standard_inchi) if standard_inchi else ""
            if not key:
                error = "inchi_generation_failed"
    return {
        "unii": unii,
        "gsrs_record_version": str(row.get("version") or ""),
        "substance_class": str(row.get("substance_class") or ""),
        "standard_inchi_key": key,
        "structure_error": error,
        "retrieved_on": retrieved_on,
    }


def fetch_substances(
    uniis: set[str],
    *,
    api_url: str,
    cache_path: Path,
    offline: bool,
    refresh: bool,
) -> dict[str, dict]:
    cache = {} if refresh else load_cache(cache_path)
    missing = sorted(uniis - set(cache))
    if missing and offline:
        raise SystemExit(f"--offline but GSRS cache lacks {len(missing)} requested UNIIs")
    retrieved_on = datetime.now(timezone.utc).date().isoformat()
    for offset in range(0, len(missing), 40):
        batch = missing[offset : offset + 40]
        query = "unii:(" + " OR ".join(batch) + ")"
        url = api_url + "?" + urllib.parse.urlencode({"search": query, "limit": 99})
        last_error = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url) as response:  # noqa: S310 - configured FDA host
                    payload = json.load(response)
                break
            except Exception as exc:  # pragma: no cover - exercised only on network failure
                last_error = exc
                if attempt == 2:
                    raise RuntimeError(f"GSRS batch request failed: {batch[0]}...") from exc
                time.sleep(1 + attempt)
        else:  # pragma: no cover
            raise RuntimeError(last_error)
        for row in payload.get("results", []):
            compact = compact_substance(row, retrieved_on)
            if compact["unii"]:
                cache[compact["unii"]] = compact
        print(
            f"  GSRS identities {min(offset + len(batch), len(missing))}/{len(missing)}",
            file=sys.stderr,
        )
        time.sleep(0.2)
    if missing:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with cache_path.open("w", encoding="utf-8") as handle:
            for unii in sorted(cache):
                handle.write(json.dumps(cache[unii], sort_keys=True) + "\n")
    return cache


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


def match_products(
    products: list[dict],
    identities: dict[str, dict],
    drugs_version: str,
    drugs_retrieved_on: str,
    unii_version: str,
) -> tuple[list[dict], Counter]:
    exact, connectivity = corpus_keys()
    rows = []
    counts: Counter = Counter()
    for product in products:
        identity = identities.get(product["unii"])
        if identity is None:
            counts["rejected_unii_missing_from_gsrs"] += 1
            continue
        if identity["structure_error"] or not identity["standard_inchi_key"]:
            counts["rejected_no_gsrs_chemical_structure"] += 1
            continue
        key = identity["standard_inchi_key"]
        matches = exact.get(key, [])
        if len(matches) > 1:
            counts["ambiguous_multiple_corpus_records"] += 1
            continue
        if not matches:
            if connectivity.get(key[:14]):
                counts["ambiguous_salt_stereo_or_protonation"] += 1
            else:
                counts["out_of_scope"] += 1
            continue
        rows.append({
            **product,
            "standard_inchi_key": key,
            "gsrs_record_version": identity["gsrs_record_version"],
            "drugsfda_version": drugs_version,
            "drugsfda_retrieved_on": drugs_retrieved_on,
            "unii_version": unii_version,
            "gsrs_retrieved_on": identity["retrieved_on"],
        })
        counts["matched_product_rows"] += 1
        counts[f"matched_record:{matches[0]}"] += 1
    rows.sort(key=lambda row: (row["standard_inchi_key"], row["application_number"], row["product_number"]))
    return rows, counts


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(
    conf: dict,
    drugs_archive: Path,
    unii_archive: Path,
    cache_path: Path,
    inventory: Path,
    drugs_version: str,
    unii_version: str,
    retrieved_on: str,
) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    drugs_cfg = conf["fda_drugsfda"]
    gsrs_cfg = conf["fda_gsrs"]
    manifest.setdefault("sources", {})["fda_drugsfda"] = {
        "homepage": drugs_cfg["homepage"],
        "license": drugs_cfg["license"],
        "version": drugs_version,
        "retrieved_on": retrieved_on,
        "jurisdiction": drugs_cfg["jurisdiction"],
    }
    manifest["sources"]["fda_gsrs"] = {
        "homepage": gsrs_cfg["homepage"],
        "license": gsrs_cfg["license"],
        "unii_version": unii_version,
        "retrieved_on": retrieved_on,
        "use": "identity only",
    }
    downloads = manifest.setdefault("downloads", {})
    for path, url in (
        (drugs_archive, drugs_cfg["archive_url"]),
        (unii_archive, gsrs_cfg["unii_archive_url"]),
        (cache_path, gsrs_cfg["substance_api"] + " (batched UNII queries)"),
    ):
        downloads[path.name] = {"url": url, "bytes": path.stat().st_size, "sha256": sha256_of(path)}
    with inventory.open(newline="", encoding="utf-8") as handle:
        row_count = sum(1 for _ in csv.DictReader(handle, delimiter="\t"))
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": row_count,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": "Drugs@FDA regulatory facts joined to GSRS/UNII exact structures",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drugs-archive", type=Path)
    parser.add_argument("--unii-archive", type=Path)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--refresh-gsrs", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Write no inventory or manifest")
    args = parser.parse_args()

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    drugs_cfg = conf["fda_drugsfda"]
    gsrs_cfg = conf["fda_gsrs"]
    drugs_archive = args.drugs_archive or DOWNLOAD_DIR / drugs_cfg["archive_name"]
    unii_archive = args.unii_archive or DOWNLOAD_DIR / gsrs_cfg["unii_archive_name"]
    if args.drugs_archive and not drugs_archive.exists():
        raise SystemExit(f"archive does not exist: {drugs_archive}")
    if args.unii_archive and not unii_archive.exists():
        raise SystemExit(f"archive does not exist: {unii_archive}")
    if not args.drugs_archive:
        drugs_archive = download(drugs_cfg["archive_url"], drugs_archive, offline=args.offline)
    if not args.unii_archive:
        unii_archive = download(gsrs_cfg["unii_archive_url"], unii_archive, offline=args.offline)

    drugs_version = zip_version(drugs_archive)
    unii_version = zip_version(unii_archive)
    unii_names = load_unii_names(unii_archive)
    products, eligibility = eligible_products(drugs_archive, unii_names)
    requested_uniis = {row["unii"] for row in products}
    cache_path = DOWNLOAD_DIR / gsrs_cfg["cache_name"]
    identities = fetch_substances(
        requested_uniis,
        api_url=gsrs_cfg["substance_api"],
        cache_path=cache_path,
        offline=args.offline,
        refresh=args.refresh_gsrs,
    )
    retrieved_on = datetime.now(timezone.utc).date().isoformat()
    rows, matches = match_products(
        products,
        identities,
        drugs_version,
        retrieved_on,
        unii_version,
    )
    unique_records = len(
        {key.split(":", 1)[1] for key in matches if key.startswith("matched_record:")}
    )
    combined = eligibility + matches
    ambiguous = sum(value for key, value in combined.items() if key.startswith("ambiguous_"))
    rejected = sum(value for key, value in combined.items() if key.startswith("rejected_"))
    excluded = sum(value for key, value in eligibility.items() if key.startswith("excluded_"))
    print(f"Drugs@FDA snapshot: {drugs_version}; UNII snapshot: {unii_version}", file=sys.stderr)
    print(
        f"  products={eligibility['products_total']} eligible_single={len(products)} "
        f"unique_UNIIs={len(requested_uniis)}",
        file=sys.stderr,
    )
    print(
        f"  matched_products={len(rows)} matched_records={unique_records} "
        f"ambiguous={ambiguous} rejected={rejected} excluded={excluded} "
        f"out_of_scope={matches['out_of_scope']}",
        file=sys.stderr,
    )
    for key, value in sorted(eligibility.items()):
        if value and key not in {"products_total", "eligible_single_ingredient_products"}:
            print(f"    {key}: {value}", file=sys.stderr)
    for key, value in sorted(matches.items()):
        if value and not key.startswith("matched_record:") and key != "matched_product_rows":
            print(f"    {key}: {value}", file=sys.stderr)
    if args.dry_run:
        print("--dry-run: no inventory or manifest written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, rows)
    update_manifest(
        conf,
        drugs_archive,
        unii_archive,
        cache_path,
        inventory,
        drugs_version,
        unii_version,
        retrieved_on,
    )
    print(f"wrote {inventory.relative_to(REPO_ROOT)} and data/raw/MANIFEST.yaml", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

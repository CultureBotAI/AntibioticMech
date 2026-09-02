#!/usr/bin/env python3
"""Extract PHI-base gene--antimicrobial resistance observations.

PHI-base supplies the antimicrobial as a ChEBI identifier, so this lane can
join to a corpus structure without interpreting a drug name.  The export is
still an association, not a biochemical mechanism: rows are emitted with the
closed ``UNKNOWN`` mechanism type and retain the exact alteration, phenotype,
organism, strain, assay evidence code, and primary PMID.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
INVENTORY_NAME = "phibase_amr.tsv"

COLUMNS = [
    "identifier",
    "standard_inchi_key",
    "phig_id",
    "protein_accession",
    "gene_id",
    "taxon_id",
    "taxon_label",
    "strain_taxon_id",
    "strain_label",
    "modification",
    "phenotype_id",
    "phenotype_label",
    "evidence_code",
    "interaction_type",
    "pmid",
    "source_commit",
    "source_retrieved_on",
]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def corpus_index() -> dict[str, dict[str, str]]:
    index = {}
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        index[record["identifier"]] = {
            "label": record["label"],
            "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
        }
    return index


def phenotype_labels(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["ID"].strip(): row["LABEL"].strip() for row in csv.DictReader(handle)}


def extract(amr_path: Path, phenotype_path: Path, source_commit: str, retrieved_on: str):
    corpus = corpus_index()
    labels = phenotype_labels(phenotype_path)
    rows: list[dict[str, str]] = []
    counts: Counter = Counter()
    with amr_path.open(newline="", encoding="utf-8") as handle:
        for source in csv.DictReader(handle):
            counts["source_rows"] += 1
            identifier = source["interactor_B_molecular_id"].strip()
            phenotype_id = source["phenotype"].strip()
            phenotype_label = labels.get(phenotype_id, "")
            if not phenotype_label.casefold().startswith("resistance to "):
                counts["rejected_non_resistance_phenotype"] += 1
                continue
            record = corpus.get(identifier)
            if record is None:
                counts["out_of_scope_chebi"] += 1
                continue
            if normalized_label(source["organism_b"]) != normalized_label(record["label"]):
                counts["rejected_chemical_label_mismatch"] += 1
                continue
            pmid = source["pmid"].strip()
            if not pmid.isdigit():
                counts["rejected_missing_primary_pmid"] += 1
                continue
            if source["interaction_type"].strip() != "antimicrobial_interaction":
                counts["rejected_interaction_type"] += 1
                continue
            taxon_id = source["taxid_species_a"].strip()
            if not taxon_id.isdigit():
                counts["rejected_missing_pathogen_taxon"] += 1
                continue
            modification = source["modification_a"].strip()
            if not modification:
                counts["rejected_missing_modification"] += 1
                continue
            rows.append({
                "identifier": identifier,
                "standard_inchi_key": record["standard_inchi_key"],
                "phig_id": source["phig_id"].strip(),
                "protein_accession": source["interactor_A_molecular_id"].strip(),
                "gene_id": source["ensembl_a"].strip(),
                "taxon_id": taxon_id,
                "taxon_label": source["organism_a"].strip(),
                "strain_taxon_id": source["taxid_strain_a"].strip(),
                "strain_label": source["strain_a"].strip(),
                "modification": modification,
                "phenotype_id": phenotype_id,
                "phenotype_label": phenotype_label,
                "evidence_code": source["evidence_code"].strip(),
                "interaction_type": source["interaction_type"].strip(),
                "pmid": pmid,
                "source_commit": source_commit,
                "source_retrieved_on": retrieved_on,
            })
            counts["accepted_rows"] += 1
    rows.sort(key=lambda row: (
        row["identifier"], row["taxon_id"], row["phig_id"], row["modification"], row["pmid"]
    ))
    counts["accepted_records"] = len({row["identifier"] for row in rows})
    return rows, counts


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("refusing to write an empty PHI-base AMR inventory")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(amr_path: Path, phenotype_path: Path, inventory: Path, conf: dict) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    cfg = conf["phibase"]
    manifest.setdefault("sources", {})["phibase"] = {
        "homepage": cfg["homepage"],
        "license": cfg["license"],
        "version": cfg["commit"],
        "retrieved_on": cfg["retrieved_on"],
        "row_policy": "ChEBI-grounded antimicrobial_interaction with resistance PHIPO and PMID",
    }
    for path, url in (
        (amr_path, cfg["amr_export_url"]),
        (phenotype_path, cfg["phenotype_vocabulary_url"]),
    ):
        manifest.setdefault("downloads", {})[path.name] = {
            "url": url,
            "bytes": path.stat().st_size,
            "sha256": sha256_of(path),
        }
    with inventory.open(newline="", encoding="utf-8") as handle:
        row_count = sum(1 for _ in csv.DictReader(handle, delimiter="\t"))
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": row_count,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": "PHI-base ChEBI-grounded gene-antimicrobial resistance interactions",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--amr", type=Path, required=True)
    parser.add_argument("--phenotypes", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    missing = [str(path) for path in (args.amr, args.phenotypes) if not path.exists()]
    if missing:
        raise SystemExit(f"missing pinned PHI-base input(s): {', '.join(missing)}")
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    cfg = conf["phibase"]
    rows, counts = extract(args.amr, args.phenotypes, cfg["commit"], cfg["retrieved_on"])
    print(f"PHI-base {cfg['commit'][:12]}: {len(rows)} accepted interactions")
    for name, count in sorted(counts.items()):
        print(f"  {name}: {count}")
    if args.dry_run:
        print("--dry-run: nothing written")
        return 0
    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, rows)
    update_manifest(args.amr, args.phenotypes, inventory, conf)
    print(f"wrote {inventory.relative_to(REPO_ROOT)} and data/raw/MANIFEST.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

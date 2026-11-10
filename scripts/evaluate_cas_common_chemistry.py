#!/usr/bin/env python3
"""Evaluate CAS Common Chemistry hits for AntibioticMech without redistributing CC BY-NC data.

Purpose:
  Audit CAS Common Chemistry lookup hits for AntibioticMech MINTED and
  INCHI_FALLBACK records, cross-referencing Standard InChIKeys against both
  `data/raw/chebi_antimicrobials.tsv` and a full 3-star ChEBI structure table
  (when available) to identify:
    1. MINTED records whose structure already has a 3-star ChEBI entry outside
       the antimicrobial-role slice (`CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE`),
       which can be grounded via CC BY 4.0 ChEBI without importing CC BY-NC data.
    2. Stereochemical or congener mismatches between PubChem/ARO and CAS/ChEBI
       (`CHEBI_STEREO_OR_CONGENER_DIFFERENCE`).
    3. CAS-resolved records that still lack a 3-star ChEBI entry
       (`CAS_RESOLVED_NO_CHEBI_3STAR`).
    4. Stoichiometry-deduplicated CAS canonical SMILES on salts/hydrates.

Inputs:
  - Enriched CAS Common Chemistry TSV (`--cas-tsv`)
  - AntibioticMech corpus (`data/antibiotics/**/*.yaml`)
  - `data/raw/chebi_antimicrobials.tsv`
  - Optional full 3-star ChEBI structures TSV (`--chebi-structures-tsv`)

Outputs:
  - Summary metrics to stdout and optional TSV report (`--output-tsv` outside
    `data/raw/` and `data/antibiotics/`).

License Gate:
  CAS Common Chemistry is licensed under CC BY-NC 4.0
  (https://commonchemistry.cas.org/terms). Under `scripts/check_source_queue.py`
  (`UNSEEDABLE["NON_COMMERCIAL"]`), CC BY-NC 4.0 data cannot be seeded into the
  CC BY 4.0 AntibioticMech corpus (`data/raw/` or `data/antibiotics/`).

Date: 2026-11-09
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
CHEBI_ANTIMICROBIALS_TSV = REPO_ROOT / "data" / "raw" / "chebi_antimicrobials.tsv"
DEFAULT_CAS_TSV = (
    REPO_ROOT.parent
    / "XMechBay"
    / ".temp"
    / "mech-chemicals-and-acs-dois"
    / "cas_common_chemistry_enriched.tsv"
)
DEFAULT_CHEBI_STRUCTURES_TSV = (
    REPO_ROOT.parent / "NaturalProductMech" / "data" / "raw" / "chebi_structures.tsv"
)

CAS_LICENSE = "CC-BY-NC-4.0"
CORPUS_LICENSE = "CC-BY-4.0"
REDISTRIBUTION_CLASS = "NON_COMMERCIAL"

INCHIKEY_PREFIX_RE = re.compile(r"^InChIKey=", re.IGNORECASE)


def strip_inchikey_prefix(value: str) -> str:
    """Normalize `InChIKey=XXXX-YYYY-Z` to standard 27-character `XXXX-YYYY-Z`."""
    cleaned = INCHIKEY_PREFIX_RE.sub("", (value or "").strip())
    return cleaned


def _component_count(formula_expr: str) -> int:
    parts = [p.strip() for p in re.split(r"[.·]", formula_expr) if p.strip()]
    total = 0
    for part in parts:
        m = re.match(r"^(\d+)\s*[A-Za-z(\[]", part)
        total += int(m.group(1)) if m else 1
    return total


def has_deduplicated_component_smiles(
    molecular_formula: str,
    canonical_smiles: str,
    inchi: str,
) -> bool:
    """Detect CAS Common Chemistry canonicalSmile component deduplication on polysalts/hydrates.

    CAS Common Chemistry's `canonicalSmile` field deduplicates identical disconnected
    components (e.g., emitting a single `[Na]` or `.O` for disodium/trisodium salts or
    pentahydrates/heptahydrates) while `molecularFormula` and `inchi` retain stoichiometry.
    """
    formula = (molecular_formula or "").strip()
    smiles = (canonical_smiles or "").strip()
    inchi_str = (inchi or "").strip()
    if not smiles:
        return False

    smiles_parts = [p for p in smiles.split(".") if p]
    if (
        formula
        and ("." in formula or "·" in formula)
        and len(smiles_parts) < _component_count(formula)
    ):
        return True

    if inchi_str.startswith("InChI="):
        inchi_layers = inchi_str.split("/")
        formula_layer = inchi_layers[1] if len(inchi_layers) > 1 else ""
        if "." in formula_layer and len(smiles_parts) < _component_count(formula_layer):
            return True
    return False


def validate_output_path_is_outside_corpus(output_path: Path, repo_root: Path = REPO_ROOT) -> None:
    """Refuse to write CC BY-NC 4.0 evaluation output inside `data/raw/` or `data/antibiotics/`."""
    resolved = output_path.resolve()
    forbidden_roots = (
        (repo_root / "data" / "raw").resolve(),
        (repo_root / "data" / "antibiotics").resolve(),
    )
    for forbidden in forbidden_roots:
        if resolved == forbidden or resolved.is_relative_to(forbidden):
            raise ValueError(
                f"Refusing to write {CAS_LICENSE} evaluation output inside {forbidden}: "
                f"{REDISTRIBUTION_CLASS} sources cannot be seeded into {CORPUS_LICENSE} corpus."
            )


def load_chebi_lookup(path: Path) -> dict[str, tuple[str, str]]:
    """Return mapping of `standard_inchi_key -> (chebi_id, name)` from a ChEBI TSV."""
    if not path.exists():
        return {}
    lookup: dict[str, tuple[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ik = (row.get("standard_inchi_key") or "").strip()
            cid = (row.get("chebi_id") or "").strip()
            name = (row.get("name") or row.get("label") or "").strip()
            if ik and cid and ik not in lookup:
                lookup[ik] = (cid, name)
    return lookup


def load_antibiotic_records(corpus_dir: Path = CORPUS_DIR) -> dict[str, dict]:
    """Load AntibioticMech records keyed by `identifier`."""
    records: dict[str, dict] = {}
    if not corpus_dir.exists():
        return records
    for yaml_path in sorted(corpus_dir.rglob("*.yaml")):
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        identifier = doc.get("identifier")
        if identifier:
            records[identifier] = doc
    return records


def evaluate_cas_rows(
    cas_rows: list[dict[str, str]],
    records_by_id: dict[str, dict],
    chebi_antimicrobials: dict[str, tuple[str, str]],
    chebi_3star_all: dict[str, tuple[str, str]],
) -> list[dict[str, str]]:
    """Evaluate AntibioticMech CAS Common Chemistry rows against corpus and ChEBI."""
    results: list[dict[str, str]] = []
    for row in cas_rows:
        if row.get("mech") != "AntibioticMech":
            continue
        identifier = (row.get("identifier") or "").strip()
        rec = records_by_id.get(identifier, {})
        cs = rec.get("chemical_structure") or {}
        corpus_ik = (cs.get("standard_inchi_key") or "").strip()
        cas_ik = strip_inchikey_prefix(row.get("inchikey") or "")
        formula = (row.get("molecular_formula") or "").strip()
        smiles = (row.get("canonical_smiles") or "").strip()
        inchi = (row.get("inchi") or "").strip()

        dedup_smiles = has_deduplicated_component_smiles(formula, smiles, inchi)
        ik_agreement = (
            "AGREES"
            if corpus_ik and cas_ik and corpus_ik == cas_ik
            else ("DIFFERS" if corpus_ik and cas_ik else "CAS_ONLY")
        )

        # Check whether either the corpus InChIKey or CAS InChIKey hits ChEBI
        antimicrobial_hit = chebi_antimicrobials.get(cas_ik) or chebi_antimicrobials.get(corpus_ik)
        chebi3_cas_hit = chebi_3star_all.get(cas_ik)
        chebi3_corpus_hit = chebi_3star_all.get(corpus_ik)

        if antimicrobial_hit:
            category = "CHEBI_IN_ANTIMICROBIAL_SLICE"
            chebi_id, chebi_name = antimicrobial_hit
        elif chebi3_cas_hit and (not corpus_ik or cas_ik == corpus_ik):
            category = "CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE"
            chebi_id, chebi_name = chebi3_cas_hit
        elif chebi3_cas_hit or chebi3_corpus_hit:
            category = "CHEBI_STEREO_OR_CONGENER_DIFFERENCE"
            chebi_id, chebi_name = chebi3_cas_hit or chebi3_corpus_hit  # type: ignore[misc]
        else:
            category = "CAS_RESOLVED_NO_CHEBI_3STAR"
            chebi_id, chebi_name = "", ""

        results.append(
            {
                "group": (row.get("group") or "").strip(),
                "identifier": identifier,
                "label": (rec.get("label") or row.get("query_name") or "").strip(),
                "grounding_status": (rec.get("grounding_status") or "").strip(),
                "cas_rn": (row.get("cas_rn") or "").strip(),
                "cas_name": (row.get("cas_name") or "").strip(),
                "corpus_inchikey": corpus_ik,
                "cas_inchikey": cas_ik,
                "inchikey_agreement": ik_agreement,
                "candidate_chebi_id": chebi_id,
                "candidate_chebi_name": chebi_name,
                "deduplicated_component_smiles": "true" if dedup_smiles else "false",
                "evaluation_category": category,
            }
        )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cas-tsv",
        type=Path,
        default=DEFAULT_CAS_TSV,
        help="Path to cas_common_chemistry_enriched.tsv",
    )
    parser.add_argument(
        "--chebi-structures-tsv",
        type=Path,
        default=DEFAULT_CHEBI_STRUCTURES_TSV,
        help="Optional path to full 3-star ChEBI structures TSV",
    )
    parser.add_argument(
        "--output-tsv",
        type=Path,
        default=None,
        help="Optional output TSV path (must be outside data/raw/ and data/antibiotics/)",
    )
    args = parser.parse_args(argv)

    if not args.cas_tsv.exists():
        print(f"missing {args.cas_tsv}; run query_cas_common_chemistry.py first", file=sys.stderr)
        return 1

    if args.output_tsv is not None:
        validate_output_path_is_outside_corpus(args.output_tsv)

    with args.cas_tsv.open(newline="", encoding="utf-8") as fh:
        cas_rows = list(csv.DictReader(fh, delimiter="\t"))

    records_by_id = load_antibiotic_records(CORPUS_DIR)
    chebi_antimicrobials = load_chebi_lookup(CHEBI_ANTIMICROBIALS_TSV)
    chebi_3star_all = load_chebi_lookup(args.chebi_structures_tsv)

    evaluated = evaluate_cas_rows(
        cas_rows,
        records_by_id,
        chebi_antimicrobials,
        chebi_3star_all,
    )

    by_group = Counter(r["group"] for r in evaluated)
    by_category = Counter(r["evaluation_category"] for r in evaluated)
    dedup_count = sum(1 for r in evaluated if r["deduplicated_component_smiles"] == "true")

    print(f"CAS Common Chemistry license                : {CAS_LICENSE} ({REDISTRIBUTION_CLASS})")
    print(f"AntibioticMech corpus license               : {CORPUS_LICENSE}")
    print(f"AntibioticMech CAS hits evaluated           : {len(evaluated)}")
    for group_name, count in sorted(by_group.items()):
        print(f"  group {group_name:<35} : {count}")
    print()
    print("Evaluation categories:")
    for category, count in sorted(by_category.items()):
        print(f"  {category:<43} : {count}")
    print(f"  deduplicated_component_smiles               : {dedup_count}")
    print()
    print("NOT WRITTEN TO CORPUS. CAS Common Chemistry is CC BY-NC 4.0; use")
    print("CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE leads to ground MINTED records")
    print("via CC BY 4.0 ChEBI rather than seeding CC BY-NC structures.")

    if args.output_tsv is not None:
        args.output_tsv.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "group",
            "identifier",
            "label",
            "grounding_status",
            "cas_rn",
            "cas_name",
            "corpus_inchikey",
            "cas_inchikey",
            "inchikey_agreement",
            "candidate_chebi_id",
            "candidate_chebi_name",
            "deduplicated_component_smiles",
            "evaluation_category",
        ]
        with args.output_tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(evaluated)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

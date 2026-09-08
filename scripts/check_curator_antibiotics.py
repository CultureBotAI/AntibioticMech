#!/usr/bin/env python3
"""Validate curator-owned antibiotic structures with RDKit."""

from __future__ import annotations

import contextlib
import csv
import sys
from pathlib import Path

from rdkit import Chem, rdBase
from rdkit.Chem import rdMolDescriptors

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from seed_from_sources import CURATOR_ANTIBIOTICS_PATH, load_curator_concepts  # noqa: E402


@contextlib.contextmanager
def _block_rdkit_logs():
    blocker = rdBase.BlockLogs()
    try:
        yield
    finally:
        del blocker


def _inchi_key(molecule) -> str:
    with _block_rdkit_logs():
        return Chem.InchiToInchiKey(Chem.MolToInchi(molecule))


def validate_curator_structures(path: Path = CURATOR_ANTIBIOTICS_PATH) -> list[str]:
    """Return any mismatches between a curator row's structural fields."""

    try:
        load_curator_concepts(path)
    except SystemExit as error:
        return [str(error)]
    if not path.exists():
        return []

    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as stream:
        for lineno, row in enumerate(csv.DictReader(stream, delimiter="\t"), 2):
            if not any(row.values()):
                continue
            with _block_rdkit_logs():
                smiles_molecule = Chem.MolFromSmiles(row["smiles"])
                inchi_molecule = Chem.MolFromInchi(row["standard_inchi"])
            if smiles_molecule is None:
                errors.append(f"{path}:{lineno} SMILES did not parse")
                continue
            if inchi_molecule is None:
                errors.append(f"{path}:{lineno} standard_inchi did not parse")
                continue

            inchi_key = Chem.InchiToInchiKey(row["standard_inchi"])
            smiles_key = _inchi_key(smiles_molecule)
            if row["standard_inchi_key"] != inchi_key:
                errors.append(
                    f"{path}:{lineno} standard_inchi_key {row['standard_inchi_key']} "
                    f"does not match standard_inchi-derived {inchi_key}"
                )
            if smiles_key != inchi_key:
                errors.append(
                    f"{path}:{lineno} SMILES-derived Standard InChIKey {smiles_key} "
                    f"does not match standard_inchi-derived {inchi_key}"
                )

            formula = rdMolDescriptors.CalcMolFormula(inchi_molecule)
            if row["molecular_formula"] != formula:
                errors.append(
                    f"{path}:{lineno} molecular_formula {row['molecular_formula']} "
                    f"does not match standard_inchi-derived {formula}"
                )
    return errors


def main() -> int:
    errors = validate_curator_structures()
    if errors:
        print("curator antibiotic structure errors:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"curator antibiotic structures are internally consistent: {CURATOR_ANTIBIOTICS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_curator_antibiotics import validate_curator_structures  # noqa: E402
from seed_from_sources import CURATOR_ANTIBIOTIC_COLUMNS  # noqa: E402


def _curator_inventory(tmp_path: Path, **overrides: str) -> Path:
    row = {
        "source_id": "DOI:10.1000/widget#compound-1",
        "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "smiles": "C",
        "standard_inchi": "InChI=1S/CH4/h1H4",
        "standard_inchi_key": "VNWKTOKETHGBQD-UHFFFAOYSA-N",
        "structure_source": "DOI:10.1000/widget",
        "structure_retrieved_on": "2026-09-07",
        "source_version": "2026-09-07",
        "reference": "DOI:10.1000/widget",
        "evidence_snippet": "Compound 1 inhibited Bacillus subtilis.",
        "evidence_notes": "Table 1 reports the exact structure and activity.",
        "definition": "A curated antibacterial methane placeholder.",
        "activity_roles": "CHEBI:33282",
        "synonyms": "compound 1|WM-1",
        "xrefs": "PubChem:123",
        "molecular_formula": "CH4",
        "charge": "0",
        "average_mass": "16.043",
        "monoisotopic_mass": "16.0313",
    } | overrides
    path = tmp_path / "curator_antibiotics.tsv"
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=CURATOR_ANTIBIOTIC_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    return path


def test_curator_structure_check_accepts_a_consistent_row(tmp_path: Path):
    assert validate_curator_structures(_curator_inventory(tmp_path)) == []


def test_curator_structure_check_rejects_an_inchi_key_from_another_molecule(tmp_path: Path):
    path = _curator_inventory(
        tmp_path,
        standard_inchi_key="OTMSDBZUPAUEDD-UHFFFAOYSA-N",
    )

    assert "does not match standard_inchi-derived" in "\n".join(
        validate_curator_structures(path)
    )


def test_curator_structure_check_rejects_a_smiles_from_another_molecule(tmp_path: Path):
    path = _curator_inventory(tmp_path, smiles="CC")

    assert "SMILES-derived Standard InChIKey" in "\n".join(
        validate_curator_structures(path)
    )


def test_curator_structure_check_rejects_a_formula_from_another_molecule(tmp_path: Path):
    path = _curator_inventory(tmp_path, molecular_formula="C2H6")

    assert "molecular_formula C2H6 does not match" in "\n".join(
        validate_curator_structures(path)
    )

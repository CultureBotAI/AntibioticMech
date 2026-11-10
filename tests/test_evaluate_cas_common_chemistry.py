"""Unit tests for CAS Common Chemistry non-redistributing evaluator in AntibioticMech."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_source_queue import UNSEEDABLE  # noqa: E402
from evaluate_cas_common_chemistry import (  # noqa: E402
    REDISTRIBUTION_CLASS,
    evaluate_cas_rows,
    has_deduplicated_component_smiles,
    strip_inchikey_prefix,
    validate_output_path_is_outside_corpus,
)


def test_cas_common_chemistry_redistribution_is_unseedable_under_cc_by_4():
    assert REDISTRIBUTION_CLASS in UNSEEDABLE
    assert "NonCommercial" in UNSEEDABLE[REDISTRIBUTION_CLASS]


def test_strip_inchikey_prefix_normalizes_cas_format():
    assert (
        strip_inchikey_prefix("InChIKey=RZQXOGQSPBYUKH-UHFFFAOYSA-N")
        == "RZQXOGQSPBYUKH-UHFFFAOYSA-N"
    )
    assert (
        strip_inchikey_prefix("RZQXOGQSPBYUKH-UHFFFAOYSA-N")
        == "RZQXOGQSPBYUKH-UHFFFAOYSA-N"
    )


def test_has_deduplicated_component_smiles_detects_polysalt_and_polyhydrate_collapse():
    # Disodium salt where CAS canonicalSmile has only one [Na]
    assert (
        has_deduplicated_component_smiles(
            "C10H16N2O8.2H2O.2Na",
            "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O.[Na].O",
            (
                "InChI=1S/C10H16N2O8.2Na.2H2O/"
                "c13-7(14)1-11(2-8(15)16)5-6-12(3-9(17)18)4-10(19)20;;;;/"
                "h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20);;;2*1H2"
            ),
        )
        is True
    )
    # Neutral monomer without disconnected components
    assert (
        has_deduplicated_component_smiles(
            "C7H17NO7S",
            "O=S(=O)(O)CC(O)CNC(CO)(CO)CO",
            "InChI=1S/C7H17NO7S/c9-2-7(3-10,4-11)8-1-6(12)5-16(13,14)15/h6,8-12H,1-5H2,(H,13,14,15)",
        )
        is False
    )


def test_validate_output_path_refuses_corpus_and_raw_directories(tmp_path):
    (tmp_path / "data" / "raw").mkdir(parents=True)
    (tmp_path / "data" / "antibiotics").mkdir(parents=True)
    (tmp_path / "reports").mkdir(parents=True)

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "raw" / "cas.tsv", repo_root=tmp_path
        )

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "antibiotics" / "cas.tsv", repo_root=tmp_path
        )

    validate_output_path_is_outside_corpus(
        tmp_path / "reports" / "cas_eval.tsv", repo_root=tmp_path
    )


def test_evaluate_cas_rows_classifies_chebi_3star_and_stereo_differences():
    cas_rows = [
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:ARO-3000150",
            "query_name": "gramicidin S",
            "cas_rn": "113-73-5",
            "cas_name": "Gramicidin S",
            "molecular_formula": "C60H92N12O10",
            "canonical_smiles": (
                "CC(C)C1NC(=O)C(CCCN)NC(=O)C(Cc2ccccc2)NC(=O)C2CCCN2C(=O)"
                "C(CC(C)C)NC(=O)C(CCCN)NC(=O)C(Cc2ccccc2)NC(=O)C2CCCN2C1=O"
            ),
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=BLRBXZWBHXWECJ-XFFZJAGNSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:ARO-3007577",
            "query_name": "triflumizole",
            "cas_rn": "99387-89-0",
            "cas_name": "Triflumizole",
            "molecular_formula": "C15H15ClF3N3O",
            "canonical_smiles": "CCCOC(=Nc1ccc(Cl)cc1C(F)(F)F)n1ccnc1",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=HSMVPDGQOIQYSR-UHFFFAOYSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:ARO-3005110",
            "query_name": "novel antibiotic",
            "cas_rn": "12345-67-8",
            "cas_name": "Novel antibiotic",
            "molecular_formula": "C10H12N2O2",
            "canonical_smiles": "O=C1NCCc2ccccc12",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=AAAAAAAAAAAAAA-BBBBBBBBSA-N",
        },
    ]
    records_by_id = {
        "antibioticmech:ARO-3000150": {
            "identifier": "antibioticmech:ARO-3000150",
            "label": "gramicidin S",
            "grounding_status": "MINTED",
            "chemical_structure": {
                "standard_inchi_key": "BLRBXZWBHXWECJ-XFFZJAGNSA-N",
            },
        },
        "antibioticmech:ARO-3007577": {
            "identifier": "antibioticmech:ARO-3007577",
            "label": "triflumizole",
            "grounding_status": "MINTED",
            "chemical_structure": {
                "standard_inchi_key": "HSMVPDGQOIQYSR-HYXKWVIFSA-N",
            },
        },
        "antibioticmech:ARO-3005110": {
            "identifier": "antibioticmech:ARO-3005110",
            "label": "novel antibiotic",
            "grounding_status": "MINTED",
            "chemical_structure": {},
        },
    }
    chebi_antimicrobials: dict[str, tuple[str, str]] = {}
    chebi_3star_all = {
        "BLRBXZWBHXWECJ-XFFZJAGNSA-N": ("CHEBI:5530", "gramicidin S"),
        "HSMVPDGQOIQYSR-HYXKWVIFSA-N": ("CHEBI:81787", "(E)-triflumizole"),
    }

    evaluated = evaluate_cas_rows(
        cas_rows,
        records_by_id,
        chebi_antimicrobials,
        chebi_3star_all,
    )
    by_id = {r["identifier"]: r for r in evaluated}

    assert (
        by_id["antibioticmech:ARO-3000150"]["evaluation_category"]
        == "CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE"
    )
    assert by_id["antibioticmech:ARO-3000150"]["candidate_chebi_id"] == "CHEBI:5530"
    assert by_id["antibioticmech:ARO-3000150"]["inchikey_agreement"] == "AGREES"

    assert (
        by_id["antibioticmech:ARO-3007577"]["evaluation_category"]
        == "CHEBI_STEREO_OR_CONGENER_DIFFERENCE"
    )
    assert by_id["antibioticmech:ARO-3007577"]["candidate_chebi_id"] == "CHEBI:81787"
    assert by_id["antibioticmech:ARO-3007577"]["inchikey_agreement"] == "DIFFERS"

    assert (
        by_id["antibioticmech:ARO-3005110"]["evaluation_category"]
        == "CAS_RESOLVED_NO_CHEBI_3STAR"
    )
    assert by_id["antibioticmech:ARO-3005110"]["inchikey_agreement"] == "CAS_ONLY"

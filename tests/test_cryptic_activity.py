"""Unit tests for the non-writing CRyPTIC activity evaluator."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_cryptic_activity import DEFAULT_DRUG_MAP, validated_drug_mappings  # noqa: E402

CRYPTIC_340_CODES = {
    "AMC": "AMOXICILIN-CLAVULANATE",
    "AMI": "AMIKACIN",
    "AMX": "AMOXICILIN",
    "AZM": "AZITHROMYCIN",
    "BDQ": "BEDAQUILINE",
    "CAP": "CAPREOMYCIN",
    "CFZ": "CLOFAZIMINE",
    "CIP": "CIPROFLOXACIN",
    "CLR": "CLARITHROMYCIN",
    "CYC": "CYCLOSERINE",
    "DCS": "D-CYCLOSERINE",
    "DLM": "DELAMANID",
    "EMB": "ETHAMBUTOL",
    "ETH": "ETHIONAMIDE",
    "ETP": "ERTAPENEM",
    "FQS": "FLUOROQUINOLONE",
    "GEN": "GENTAMICIN",
    "GFX": "GATIFLOXACIN",
    "IMI": "IMIPENEM",
    "INH": "ISONIAZID",
    "KAN": "KANAMYCIN",
    "LEV": "LEVOFLOXACIN",
    "LZD": "LINEZOLID",
    "MEF": "MEFLOQUINE",
    "MPM": "MEROPENEM",
    "MXF": "MOXIFLOXACIN",
    "OFX": "OFLOXACIN",
    "PAN": "PRETOMANID",
    "PAS": "PAS",
    "PTO": "PROTHIONAMIDE",
    "PZA": "PYRAZINAMIDE",
    "RFB": "RIFABUTIN",
    "RIF": "RIFAMPICIN",
    "STM": "STREPTOMYCIN",
    "STX": "SITAFLOXACIN",
    "SXT": "COTRIMOXAZOLE",
    "SZD": "SUTEZOLID",
    "TRD": "TERIZIDONE",
    "TZE": "THIOACETAZONE",
}


def test_cryptic_drug_map_covers_the_pinned_code_table():
    mappings = validated_drug_mappings(DEFAULT_DRUG_MAP, CRYPTIC_340_CODES)

    assert len(mappings) == 39
    assert mappings["AMI"]["identifier"] == "CHEBI:2637"
    assert mappings["CYC"]["mapping_status"] == "AMBIGUOUS_STEREOCHEMISTRY"
    assert mappings["FQS"]["mapping_status"] == "DRUG_CLASS"
    assert mappings["AMC"]["mapping_status"] == "COMBINATION"
    assert mappings["GEN"]["mapping_status"] == "MIXTURE"


def test_cryptic_drug_map_rejects_stale_or_unknown_codes(tmp_path):
    path = tmp_path / "map.tsv"
    path.write_text(
        "\t".join([
            "source_version",
            "source_record_id",
            "source_name",
            "mapping_status",
            "identifier",
            "standard_inchi_key",
            "mapping_basis",
            "notes",
        ])
        + "\n3.4.0\tAMI\tAMIKACIN\tEXACT\tCHEBI:2637\t"
        + "LKCWBDHBTVXHDL-RMDFUYIESA-N\tparent_base\tok\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing=\\['AMX'\\]"):
        validated_drug_mappings(path, {"AMI": "AMIKACIN", "AMX": "AMOXICILIN"})


def test_cryptic_drug_map_rejects_identity_drift(tmp_path):
    path = tmp_path / "map.tsv"
    path.write_text(
        "\t".join([
            "source_version",
            "source_record_id",
            "source_name",
            "mapping_status",
            "identifier",
            "standard_inchi_key",
            "mapping_basis",
            "notes",
        ])
        + "\n3.4.0\tAMI\tAMIKACIN\tEXACT\tCHEBI:2637\t"
        + "WRONGINCHIKEY\tparent_base\tok\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="does not match CHEBI:2637"):
        validated_drug_mappings(path, {"AMI": "AMIKACIN"})

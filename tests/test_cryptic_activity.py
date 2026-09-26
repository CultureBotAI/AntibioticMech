"""Unit tests for the non-writing CRyPTIC activity evaluator."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_cryptic_activity import (  # noqa: E402
    DEFAULT_DRUG_MAP,
    DST_GROUP_COLUMNS,
    DST_TABLE,
    INVENTORY_COLUMNS,
    UKMYC_GROUP_COLUMNS,
    UKMYC_TABLE,
    activity_inventory,
    activity_inventory_row,
    validated_drug_mappings,
    write_inventory,
)

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
    assert sum(row["mapping_status"] == "EXACT" for row in mappings.values()) == 29
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


def test_dst_inventory_group_is_compact_and_structure_grounded():
    row = activity_inventory_row(
        DST_TABLE,
        DST_GROUP_COLUMNS,
        {
            "drug_code": "AMI",
            "source": "CRyPTIC",
            "method_1": "liquid media",
            "method_2": "microdilution plate",
            "method_3": "UKMYC6",
            "method_cc": "1.0",
            "method_mic": "<=0.25",
            "phenotype": "S",
            "quality": "HIGH",
            "row_count": 6983,
            "isolate_count": 6983,
        },
        {"AMI": "AMIKACIN"},
        {
            "AMI": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:2637",
                "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
            },
        },
    )

    assert row
    assert set(row) == set(INVENTORY_COLUMNS)
    assert row["activity_group_id"].startswith("dst_measurements:")
    assert row["identifier"] == "CHEBI:2637"
    assert row["method_mic"] == "<=0.25"
    assert row["row_count"] == "6983"
    assert row["platedesign"] == ""


def test_ukmyc_inventory_group_keeps_mic_shape_and_filters_non_exact_mappings():
    group = {
        "drug_code": "AMI",
        "platedesign": "UKMYC6",
        "belongs_gpi": True,
        "phenotype_quality": "HIGH",
        "readingday": 14,
        "primary_method": "VZ",
        "phenotype_description": "VZ,TM AGREE",
        "mic": "<=0.25",
        "log2mic": -2.0,
        "binary_phenotype": "S",
        "row_count": 6184,
        "isolate_count": 6184,
        "site_count": 11,
    }
    mappings = {
        "AMI": {
            "mapping_status": "EXACT",
            "identifier": "CHEBI:2637",
            "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
        },
        "GEN": {"mapping_status": "MIXTURE", "identifier": "", "standard_inchi_key": ""},
    }

    row = activity_inventory_row(
        UKMYC_TABLE,
        UKMYC_GROUP_COLUMNS,
        group,
        {"AMI": "AMIKACIN", "GEN": "GENTAMICIN"},
        mappings,
    )
    skipped = activity_inventory_row(
        UKMYC_TABLE,
        UKMYC_GROUP_COLUMNS,
        group | {"drug_code": "GEN"},
        {"AMI": "AMIKACIN", "GEN": "GENTAMICIN"},
        mappings,
    )

    assert row
    assert row["activity_group_id"].startswith("ukmyc_phenotypes:")
    assert row["belongs_gpi"] == "true"
    assert row["mic"] == "<=0.25"
    assert row["log2mic"] == "-2.0"
    assert row["site_count"] == "11"
    assert row["method_mic"] == ""
    assert skipped is None


def test_write_inventory_uses_the_committed_column_contract(tmp_path):
    path = tmp_path / "cryptic_inventory.tsv"

    write_inventory(path, [])

    assert path.read_text(encoding="utf-8") == "\t".join(INVENTORY_COLUMNS) + "\n"
    assert b"\r" not in path.read_bytes()


def test_write_inventory_rejects_duplicate_group_ids(tmp_path):
    row = {column: "" for column in INVENTORY_COLUMNS}
    row["activity_group_id"] = "dst_measurements:duplicate"

    with pytest.raises(ValueError, match="duplicate CRyPTIC activity_group_id"):
        write_inventory(tmp_path / "cryptic_inventory.tsv", [row, row])


def test_activity_inventory_fetches_each_result_before_reusing_duckdb_connection():
    class ReusedCursorConnection:
        def execute(self, _query, params):
            if params == ["dst.parquet"]:
                names = ["drug_code", *DST_GROUP_COLUMNS, "row_count", "isolate_count"]
                values = ["AMI", "CRyPTIC", None, None, None, "1.0", None, "S", "HIGH", 10, 9]
            else:
                names = [
                    "drug_code",
                    *UKMYC_GROUP_COLUMNS,
                    "row_count",
                    "isolate_count",
                    "site_count",
                ]
                values = ["AMI", "UKMYC6", False, "HIGH", 14, "VZ", "VZ ONLY", "0.5", -1.0, "S", 3, 3, 2]
            self.description = [(name,) for name in names]
            self.values = values
            return self

        def fetchall(self):
            return [self.values]

    rows = activity_inventory(
        ReusedCursorConnection(),
        Path("dst.parquet"),
        Path("ukmyc.parquet"),
        {"AMI": "AMIKACIN"},
        {
            "AMI": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:2637",
                "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
            },
        },
    )

    assert [row["source_table"] for row in rows] == [DST_TABLE, UKMYC_TABLE]

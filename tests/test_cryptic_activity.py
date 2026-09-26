"""Unit tests for the non-writing CRyPTIC activity evaluator."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import seed_from_sources  # noqa: E402
from evaluate_cryptic_activity import (  # noqa: E402
    DEFAULT_DRUG_MAP,
    DST_GROUP_COLUMNS,
    DST_TABLE,
    INVENTORY_COLUMNS,
    UKMYC_GROUP_COLUMNS,
    UKMYC_TABLE,
    activity_inventory,
    activity_inventory_row,
    parse_mic,
    validated_drug_mappings,
    write_inventory,
)
from seed_from_sources import (  # noqa: E402
    CRYPTIC_ACTIVITY_SOURCE,
    attach_cryptic_activity,
    cryptic_sourced_activity_view,
    merge_with_existing,
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


@pytest.mark.parametrize(
    ("raw", "parsed"),
    [
        ("<=0.25", ("0.25", "<=", "mg/L")),
        (">16", ("16", ">", "mg/L")),
        ("0.5", ("0.5", "", "mg/L")),
        (".125", (".125", "", "mg/L")),
        (None, ("", "", "")),
        ("nan", ("", "", "")),
        ("", ("", "", "")),
    ],
)
def test_parse_mic_standardizes_cryptic_mic_shape(raw, parsed):
    assert parse_mic(raw) == parsed


def test_parse_mic_rejects_unexpected_values():
    with pytest.raises(ValueError, match="unsupported CRyPTIC MIC value"):
        parse_mic("0.5-1")


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
            "method_cc": "nan",
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
    assert row["mic_value"] == "0.25"
    assert row["mic_qualifier"] == "<="
    assert row["mic_units"] == "mg/L"
    assert row["method_cc"] == ""
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
    assert row["mic_value"] == "0.25"
    assert row["mic_qualifier"] == "<="
    assert row["mic_units"] == "mg/L"
    assert row["belongs_gpi"] == "true"
    assert row["mic"] == "<=0.25"
    assert row["log2mic"] == "-2.0"
    assert row["site_count"] == "11"
    assert row["method_mic"] == ""
    assert skipped is None


def test_write_inventory_uses_the_committed_column_contract(tmp_path):
    path = tmp_path / "cryptic_inventory.tsv"
    row = {column: "" for column in INVENTORY_COLUMNS}
    row.update({
        "source_version": "3.4.0",
        "source_table": "DST_MEASUREMENTS",
        "activity_group_id": "dst_measurements:abc",
    })

    write_inventory(path, [row])

    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines == ["\t".join(INVENTORY_COLUMNS), "3.4.0\tDST_MEASUREMENTS\tdst_measurements:abc"]
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


def test_compact_inventory_row_becomes_a_grouped_activity_observation(tmp_path, monkeypatch):
    row = {column: "" for column in INVENTORY_COLUMNS}
    row.update({
        "source_version": "3.4.0",
        "source_table": UKMYC_TABLE,
        "activity_group_id": "ukmyc_phenotypes:abc",
        "drug_code": "AMI",
        "source_name": "AMIKACIN",
        "identifier": "CHEBI:2637",
        "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
        "mic_value": "0.25",
        "mic_qualifier": "<=",
        "mic_units": "mg/L",
        "row_count": "6184",
        "isolate_count": "6184",
        "site_count": "11",
        "platedesign": "UKMYC6",
        "belongs_gpi": "true",
        "phenotype_quality": "HIGH",
        "readingday": "14",
        "primary_method": "VZ",
        "phenotype_description": "VZ,TM AGREE",
        "mic": "<=0.25",
        "log2mic": "-2.0",
        "binary_phenotype": "R",
    })
    write_inventory(tmp_path / "cryptic_activity.tsv", [row])
    monkeypatch.setattr(
        seed_from_sources,
        "CRYPTIC_ACTIVITY_INVENTORY",
        tmp_path / "cryptic_activity.tsv",
    )

    records = {"CHEBI:2637": {
        "identifier": "CHEBI:2637",
        "chemical_structure": {"standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
        "curation_history": [],
    }}

    counts = attach_cryptic_activity(records)
    observation = records["CHEBI:2637"]["activity_spectrum"][0]

    assert counts["matched_observations"] == 1
    assert counts["matched_records"] == 1
    assert "taxon_id" not in observation
    assert observation["taxon_label"] == "Mycobacterium tuberculosis complex"
    assert observation["activity"] == "RESISTANT"
    assert observation["mic_value"] == 0.25
    assert observation["mic_qualifier"] == "<="
    assert observation["measurement_count"] == 6184
    assert observation["isolate_count"] == 6184
    assert observation["site_count"] == 11
    assert observation["source"] == CRYPTIC_ACTIVITY_SOURCE
    assert observation["source_version"] == "3.4.0"
    assert observation["source_observation_id"] == "ukmyc_phenotypes:abc"
    assert "UKMYC6" in observation["assay"]
    assert "primary method VZ" in observation["assay"]
    assert "row_count=6184" in observation["evidence"][0]["notes"]


def test_cryptic_activity_writer_rejects_identity_drift(tmp_path, monkeypatch):
    row = {column: "" for column in INVENTORY_COLUMNS}
    row.update({
        "source_version": "3.4.0",
        "source_table": UKMYC_TABLE,
        "activity_group_id": "ukmyc_phenotypes:abc",
        "drug_code": "AMI",
        "identifier": "CHEBI:2637",
        "standard_inchi_key": "STALE",
        "mic_value": "0.25",
        "mic_units": "mg/L",
        "row_count": "6184",
        "isolate_count": "6184",
    })
    write_inventory(tmp_path / "cryptic_activity.tsv", [row])
    monkeypatch.setattr(
        seed_from_sources,
        "CRYPTIC_ACTIVITY_INVENTORY",
        tmp_path / "cryptic_activity.tsv",
    )
    records = {"CHEBI:2637": {
        "identifier": "CHEBI:2637",
        "chemical_structure": {"standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N"},
        "curation_history": [],
    }}

    counts = attach_cryptic_activity(records)

    assert counts["identity_drift"] == 1
    assert "activity_spectrum" not in records["CHEBI:2637"]


def test_compact_activity_observation_can_be_qualitative_without_mic():
    row = {column: "" for column in INVENTORY_COLUMNS}
    row.update({
        "source_version": "3.4.0",
        "source_table": DST_TABLE,
        "activity_group_id": "dst_measurements:abc",
        "drug_code": "AMI",
        "source": "CRyPTIC",
        "identifier": "CHEBI:2637",
        "standard_inchi_key": "LKCWBDHBTVXHDL-RMDFUYIESA-N",
        "row_count": "3",
        "isolate_count": "3",
        "method_1": "liquid media",
        "method_2": "microdilution plate",
        "method_3": "UKMYC6",
        "phenotype": "I",
        "quality": "LOW",
    })

    observation = seed_from_sources.cryptic_activity_observation(row)

    assert "mic_value" not in observation
    assert "mic_units" not in observation
    assert observation["activity"] == "INTERMEDIATE"


def test_reseed_replaces_only_the_cryptic_activity_slice():
    new_cryptic = {
        "taxon_label": "Mycobacterium tuberculosis complex",
        "activity": "RESISTANT",
        "mic_value": 2.0,
        "mic_units": "mg/L",
        "assay": "UKMYC broth microdilution",
        "source": CRYPTIC_ACTIVITY_SOURCE,
        "source_version": "3.4.0",
        "source_observation_id": "UKMYC_PHENOTYPES:abc",
        "evidence": [{"reference": "DOI:10.5281/zenodo.15680920"}],
    }
    old_cryptic = new_cryptic | {"source_observation_id": "UKMYC_PHENOTYPES:stale"}
    curated = {
        "taxon_label": "Escherichia coli",
        "activity": "SUSCEPTIBLE",
        "assay": "curated broth microdilution",
        "source": "CURATOR",
        "evidence": [{"reference": "PMID:1"}],
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }

    fresh = base | {"activity_spectrum": [new_cryptic]}
    existing = base | {"activity_spectrum": [old_cryptic, curated]}
    merged = merge_with_existing(fresh, existing)

    assert cryptic_sourced_activity_view(merged) == [new_cryptic]
    assert merged["activity_spectrum"] == [new_cryptic, curated]


def test_reseed_drops_stale_cryptic_activity_when_the_source_stops_emitting_it():
    old_cryptic = {
        "taxon_label": "Mycobacterium tuberculosis complex",
        "activity": "RESISTANT",
        "assay": "UKMYC broth microdilution",
        "source": CRYPTIC_ACTIVITY_SOURCE,
        "source_version": "3.4.0",
        "source_observation_id": "UKMYC_PHENOTYPES:stale",
        "evidence": [{"reference": "DOI:10.5281/zenodo.15680920"}],
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }

    merged = merge_with_existing(base, base | {"activity_spectrum": [old_cryptic]})

    assert "activity_spectrum" not in merged

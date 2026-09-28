"""Unit tests for the non-writing Stanford HIVDB hivfacts evaluator."""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from antibioticmech.hivdb_score_rules import hivdb_score_rule_id

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_hivdb_hivfacts import (  # noqa: E402
    ALGORITHM_REPORT_COLUMNS,
    ALGORITHM_TERM_REPORT_COLUMNS,
    DEFAULT_DRUG_MAP,
    DRUG_MAP_COLUMNS,
    HIVDB_HIVFACTS_COMMIT,
    MUTATION_REPORT_COLUMNS,
    PATTERN_REPORT_COLUMNS,
    corpus_name_candidates,
    evaluate_class_mutations,
    evaluate_drug_patterns,
    evaluate_drugs,
    evaluate_hiv1_algorithm_rules,
    read_class_mutation_list,
    read_drug_map,
    read_drug_patterns,
    read_drugs,
    read_hiv1_algorithm,
    write_algorithm_report,
    write_algorithm_term_report,
    write_drug_map_template,
    write_drug_report,
    write_mutation_report,
    write_pattern_report,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "evaluate_hivdb_hivfacts.py"


def with_hivdb_score_rule_id(row: dict) -> dict:
    row = {"source_rule_id": "", **row}
    row["source_rule_id"] = hivdb_score_rule_id(row)
    return row


def hivdb_source_rows() -> list[dict[str, str]]:
    return [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
        {
            "source_record_id": "ATV/r",
            "display_abbr": "ATV/r",
            "name": "ATV",
            "full_name": "atazanavir/r",
            "drug_class": "PI",
            "synonyms": "",
        },
    ]


def algorithm_source_rows() -> list[dict[str, str]]:
    return [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
        {
            "source_record_id": "AZT",
            "display_abbr": "AZT",
            "name": "AZT",
            "full_name": "zidovudine",
            "drug_class": "NRTI",
            "synonyms": "",
        },
    ]


def hivdb_algorithm_xml(
    *,
    abc_condition: str = "SCORE FROM (65R => -10, MAX(184I => 15, 184V => 15))",
    abc_actions: str = "<SCORERANGE><USE_GLOBALRANGE/></SCORERANGE>",
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ALGORITHM>
  <ALGNAME>HIVDB</ALGNAME>
  <ALGVERSION>10.2</ALGVERSION>
  <ALGDATE>2026-04-26</ALGDATE>
  <DEFINITIONS>
    <DRUGCLASS>
      <NAME>NRTI</NAME>
      <DRUGLIST>ABC,AZT</DRUGLIST>
    </DRUGCLASS>
  </DEFINITIONS>
  <DRUG>
    <NAME>ABC</NAME>
    <FULLNAME>abacavir</FULLNAME>
    <RULE>
      <CONDITION><![CDATA[{abc_condition}]]></CONDITION>
      <ACTIONS>{abc_actions}</ACTIONS>
    </RULE>
  </DRUG>
  <DRUG>
    <NAME>AZT</NAME>
    <FULLNAME>azidothymidine</FULLNAME>
    <RULE>
      <CONDITION><![CDATA[SCORE FROM (41L => 15)]]></CONDITION>
      <ACTIONS><SCORERANGE><USE_GLOBALRANGE/></SCORERANGE></ACTIONS>
    </RULE>
  </DRUG>
</ALGORITHM>
"""


PINNED_HIVDB_102_DRUGS = [
    {"source_record_id": "ABC", "name": "ABC", "full_name": "abacavir", "drug_class": "NRTI"},
    {"source_record_id": "AZT", "name": "AZT", "full_name": "zidovudine", "drug_class": "NRTI"},
    {"source_record_id": "D4T", "name": "D4T", "full_name": "stavudine", "drug_class": "NRTI"},
    {"source_record_id": "DDI", "name": "DDI", "full_name": "didanosine", "drug_class": "NRTI"},
    {"source_record_id": "FTC", "name": "FTC", "full_name": "emtricitabine", "drug_class": "NRTI"},
    {"source_record_id": "3TC", "name": "LMV", "full_name": "lamivudine", "drug_class": "NRTI"},
    {"source_record_id": "TDF", "name": "TDF", "full_name": "tenofovir", "drug_class": "NRTI"},
    {"source_record_id": "ISL", "name": "ISL", "full_name": "islatravir", "drug_class": "NRTI"},
    {"source_record_id": "ATV/r", "name": "ATV", "full_name": "atazanavir/r", "drug_class": "PI"},
    {"source_record_id": "DRV/r", "name": "DRV", "full_name": "darunavir/r", "drug_class": "PI"},
    {"source_record_id": "FPV/r", "name": "FPV", "full_name": "fosamprenavir/r", "drug_class": "PI"},
    {"source_record_id": "IDV/r", "name": "IDV", "full_name": "indinavir/r", "drug_class": "PI"},
    {"source_record_id": "LPV/r", "name": "LPV", "full_name": "lopinavir/r", "drug_class": "PI"},
    {"source_record_id": "NFV", "name": "NFV", "full_name": "nelfinavir", "drug_class": "PI"},
    {"source_record_id": "SQV/r", "name": "SQV", "full_name": "saquinavir/r", "drug_class": "PI"},
    {"source_record_id": "TPV/r", "name": "TPV", "full_name": "tipranavir/r", "drug_class": "PI"},
    {"source_record_id": "DOR", "name": "DOR", "full_name": "doravirine", "drug_class": "NNRTI"},
    {"source_record_id": "EFV", "name": "EFV", "full_name": "efavirenz", "drug_class": "NNRTI"},
    {"source_record_id": "ETR", "name": "ETR", "full_name": "etravirine", "drug_class": "NNRTI"},
    {"source_record_id": "NVP", "name": "NVP", "full_name": "nevirapine", "drug_class": "NNRTI"},
    {"source_record_id": "RPV", "name": "RPV", "full_name": "rilpivirine", "drug_class": "NNRTI"},
    {"source_record_id": "DPV", "name": "DPV", "full_name": "dapivirine", "drug_class": "NNRTI"},
    {"source_record_id": "BIC", "name": "BIC", "full_name": "bictegravir", "drug_class": "INSTI"},
    {"source_record_id": "CAB", "name": "CAB", "full_name": "cabotegravir", "drug_class": "INSTI"},
    {"source_record_id": "DTG", "name": "DTG", "full_name": "dolutegravir", "drug_class": "INSTI"},
    {"source_record_id": "EVG", "name": "EVG", "full_name": "elvitegravir", "drug_class": "INSTI"},
    {"source_record_id": "RAL", "name": "RAL", "full_name": "raltegravir", "drug_class": "INSTI"},
    {"source_record_id": "LEN", "name": "LEN", "full_name": "lenacapavir", "drug_class": "CAI"},
]


def exact_map_identifiers(path: Path) -> set[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == DRUG_MAP_COLUMNS
        return {
            row["identifier"]
            for row in reader
            if row["mapping_status"] == "EXACT"
        }


def corpus_structure_keys_for(identifiers: set[str]) -> dict[str, str]:
    keys = {}
    remaining = set(identifiers)
    for path in sorted((REPO_ROOT / "data" / "antibiotics").rglob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("identifier: "):
            continue
        identifier = text.splitlines()[0].removeprefix("identifier: ")
        if identifier not in remaining:
            continue
        record = yaml.safe_load(text)
        keys[identifier] = record["chemical_structure"]["standard_inchi_key"]
        remaining.remove(identifier)

    assert not remaining
    return keys


def test_curated_hivdb_drug_map_covers_pinned_hivfacts_drugs():
    mappings = read_drug_map(
        DEFAULT_DRUG_MAP,
        corpus_structure_keys_for(exact_map_identifiers(DEFAULT_DRUG_MAP)),
        PINNED_HIVDB_102_DRUGS,
    )

    assert len(mappings) == 28
    assert sum(row["mapping_status"] == "EXACT" for row in mappings.values()) == 16
    assert sum(row["mapping_status"] == "COMBINATION" for row in mappings.values()) == 7
    assert mappings["ABC"]["identifier"] == "CHEBI:421707"
    assert mappings["AZT"]["identifier"] == "CHEBI:10110"
    assert mappings["DOR"]["mapping_status"] == "MISSING_CORPUS_RECORD"
    assert mappings["DOR"]["identifier"] == ""
    assert mappings["TDF"]["mapping_status"] == "AMBIGUOUS_IDENTITY"
    assert mappings["ATV/r"]["mapping_status"] == "COMBINATION"


def test_evaluate_drugs_reports_exact_and_boosted_identity_matches():
    rows = [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
        {
            "source_record_id": "ATV/r",
            "display_abbr": "ATV/r",
            "name": "ATV",
            "full_name": "atazanavir/r",
            "drug_class": "PI",
            "synonyms": "",
        },
        {
            "source_record_id": "TDF",
            "display_abbr": "TDF",
            "name": "TDF",
            "full_name": "tenofovir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
    ]

    result = evaluate_drugs(
        rows,
        {
            "abacavir": {"CHEBI:421707"},
            "tenofovir": {"CHEBI:63713", "CHEBI:192161"},
        },
        {
            "CHEBI:421707": "ABC",
            "CHEBI:63713": "TDF-ONE",
            "CHEBI:192161": "TDF-TWO",
        },
    )

    assert result["hivdb_drugs"] == 3
    assert result["exact_name_matched_drugs"] == 1
    assert result["ambiguous_name_drugs"] == 1
    assert result["unmatched_drugs"] == 1
    assert result["ritonavir_boosted_drugs"] == 1
    assert result["drug_classes"] == {"NRTI": 2, "PI": 1}

    boosted = result["drug_rows"][1]
    assert boosted["display_abbr"] == "ATV/r"
    assert boosted["ritonavir_boosted"] == "true"
    assert boosted["exact_name_candidate_count"] == 0


def test_evaluate_drugs_adds_curated_mapping_fields():
    result = evaluate_drugs(
        hivdb_source_rows(),
        {"abacavir": {"CHEBI:421707"}},
        {"CHEBI:421707": "MCI"},
        mappings={
            "ABC": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
                "mapping_basis": "full_name",
                "notes": "HIVDB fullName is the exact corpus label.",
            }
        },
    )

    assert result["drug_rows"][0]["mapping_status"] == "EXACT"
    assert result["drug_rows"][0]["identifier"] == "CHEBI:421707"
    assert result["drug_rows"][0]["mapping_notes"] == "HIVDB fullName is the exact corpus label."
    assert result["drug_rows"][1]["mapping_status"] == ""


def test_read_class_mutation_list_expands_compact_hivdb_rows(tmp_path):
    path = tmp_path / "drms_hiv1.json"
    path.write_text(
        json.dumps(
            {
                "NRTI": [
                    {"gene": "RT", "position": 184, "aa": "VI"},
                    {"gene": "RT", "position": 69, "aa": "D_"},
                ]
            }
        ),
        encoding="utf-8",
    )

    rows = read_class_mutation_list(path, "DRM")

    assert rows == [
        {
            "source_list": "DRM",
            "drug_class": "NRTI",
            "gene": "RT",
            "position": "184",
            "aa": "VI",
        },
        {
            "source_list": "DRM",
            "drug_class": "NRTI",
            "gene": "RT",
            "position": "69",
            "aa": "D_",
        },
    ]
    report = evaluate_class_mutations(rows)
    assert report["mutation_rows"] == 2
    assert report["expanded_mutations"] == 4
    assert report["source_lists"] == {"DRM": 2}
    assert report["drug_classes"] == {"NRTI": 2}
    assert report["genes"] == {"RT": 2}
    assert report["mutation_rows_report"][0]["expanded_mutation_count"] == 2
    assert report["mutation_rows_report"][0]["expanded_mutations"] == "RT:184V|RT:184I"
    assert report["mutation_rows_report"][1]["expanded_mutations"] == "RT:69D|RT:69_"


def test_read_class_mutation_list_rejects_malformed_rows(tmp_path):
    path = tmp_path / "drms_hiv1.json"

    path.write_text(json.dumps([]), encoding="utf-8")
    with pytest.raises(ValueError, match="expected a JSON object"):
        read_class_mutation_list(path, "DRM")

    path.write_text(json.dumps({"NRTI": [{"gene": "RT", "position": 0, "aa": "M"}]}))
    with pytest.raises(ValueError, match="NRTI row 1 has invalid position"):
        read_class_mutation_list(path, "DRM")

    path.write_text(json.dumps({"NRTI": [{"gene": "RT-1", "position": 184, "aa": "V"}]}))
    with pytest.raises(ValueError, match="NRTI row 1 has invalid gene 'RT-1'"):
        read_class_mutation_list(path, "DRM")

    path.write_text(json.dumps({"NRTI": [{"gene": "RT", "position": 184, "aa": "M184V"}]}))
    with pytest.raises(ValueError, match="NRTI row 1 has invalid aa 'M184V'"):
        read_class_mutation_list(path, "DRM")

    path.write_text(
        json.dumps(
            {
                "NRTI": [
                    {"gene": "RT", "position": 184, "aa": "V"},
                    {"gene": "RT", "position": 184, "aa": "V"},
                ]
            }
        )
    )
    with pytest.raises(ValueError, match="duplicate DRM NRTI mutation RT:184V"):
        read_class_mutation_list(path, "DRM")

    path.write_text(
        json.dumps(
            {
                "NRTI": [
                    {"gene": "RT", "position": 184, "aa": "V"},
                    {"gene": "RT", "position": 184, "aa": "VI"},
                ]
            }
        )
    )
    with pytest.raises(ValueError, match="duplicate expanded DRM NRTI mutation RT:184V"):
        read_class_mutation_list(path, "DRM")

    path.write_text(json.dumps({"NRTI": [{"gene": "RT", "position": 184, "aa": "VV"}]}))
    with pytest.raises(ValueError, match="duplicate expanded DRM NRTI mutation RT:184V"):
        read_class_mutation_list(path, "DRM")


def test_read_drugs_validates_hivfacts_drug_abbreviations(tmp_path):
    path = tmp_path / "drugs.json"
    path.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "LEN",
                    "drugClass": "CAI",
                    "fullName": "lenacapavir",
                    "name": "LEN",
                },
                {
                    "displayAbbr": "LEN",
                    "drugClass": "CAI",
                    "fullName": "lenacapavir",
                    "name": "LEN2",
                },
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="duplicate HIVDB drug abbreviation LEN"):
        read_drugs(path)


def test_read_drugs_rejects_non_string_synonyms(tmp_path):
    path = tmp_path / "drugs.json"
    path.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "DTG",
                    "drugClass": "INSTI",
                    "fullName": "dolutegravir",
                    "name": "DTG",
                    "synonyms": [7],
                }
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="DTG synonym 1 is not a string"):
        read_drugs(path)


def test_corpus_name_candidates_include_record_labels_and_synonyms(tmp_path):
    directory = tmp_path / "data" / "antibiotics" / "antiviral"
    directory.mkdir(parents=True)
    record = {
        "identifier": "CHEBI:421707",
        "label": "abacavir",
        "chemical_structure": {"standard_inchi_key": "MCI"},
        "synonyms": [{"synonym_text": "ABC"}],
    }
    (directory / "abacavir.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")

    candidates, structure_keys = corpus_name_candidates(tmp_path)

    assert candidates["abacavir"] == {"CHEBI:421707"}
    assert candidates["abc"] == {"CHEBI:421707"}
    assert structure_keys == {"CHEBI:421707": "MCI"}


def test_read_drug_map_accepts_exact_and_non_exact_rows(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "\n".join(
            [
                f"{HIVDB_HIVFACTS_COMMIT}\tABC\t abacavir \tABC\tNRTI\t"
                "EXACT\tCHEBI:421707\t"
                "MCI\tfull_name\tHIVDB fullName is the exact corpus label.",
                f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
                "COMBINATION\t\t\t"
                "ritonavir_boosted\tBoosted protease-inhibitor row.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    mappings = read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    assert mappings["ABC"]["identifier"] == "CHEBI:421707"
    assert mappings["ABC"]["source_name"] == "abacavir"
    assert mappings["ATV/r"]["mapping_status"] == "COMBINATION"
    assert mappings["ATV/r"]["identifier"] == ""


def test_read_drug_map_rejects_identity_drift(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir sulfate\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\twrong salt\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
        + "COMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="mapped source_name 'abacavir sulfate'"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "WRONGINCHIKEY\tfull_name\twrong structure\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
        + "COMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="does not match CHEBI:421707"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_map_rejects_source_version_drift(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + "stale\tABC\tabacavir\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tok\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
        + "COMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="source_version 'stale'"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_map_rejects_stale_and_incomplete_maps(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tok\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing=\\['ATV/r'\\] extra=\\[\\]"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())

    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tok\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
        + "COMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tOLD\toldavir\tOLD\tNRTI\t"
        + "MISSING_CORPUS_RECORD\t\t\tmissing\tstale\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing=\\[\\] extra=\\['OLD'\\]"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_map_rejects_non_exact_structure_fields(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    path.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir\tABC\tNRTI\t"
        + "MISSING_CORPUS_RECORD\tCHEBI:421707\t"
        + "MCI\tmissing\twrong\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tATV/r\tatazanavir/r\tATV\tPI\t"
        + "COMBINATION\t\t\t"
        + "ritonavir_boosted\tBoosted protease-inhibitor row.\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="non-EXACT mapping must not carry structure fields"):
        read_drug_map(path, {"CHEBI:421707": "MCI"}, hivdb_source_rows())


def test_read_drug_patterns_audits_level_score_matrices(tmp_path):
    path = tmp_path / "patterns-NRTI.json"
    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 17,
                    "ABC Level": 3,
                    "ABC Score": 15.0,
                    "AZT Level": 1,
                    "AZT Score": -5.0,
                },
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M41L,M184V,T215Y",
                    "count": 7,
                    "ABC Level": 4,
                    "ABC Score": 30.0,
                    "AZT Level": 5,
                    "AZT Score": 60,
                },
            ]
        ),
        encoding="utf-8",
    )
    source_rows = [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        },
        {
            "source_record_id": "AZT",
            "display_abbr": "AZT",
            "name": "AZT",
            "full_name": "zidovudine",
            "drug_class": "NRTI",
            "synonyms": "",
        },
    ]

    rows = read_drug_patterns(path, source_rows)
    result = evaluate_drug_patterns(
        rows,
        source_rows,
        {
            "ABC": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
            },
            "AZT": {"mapping_status": "AMBIGUOUS_IDENTITY"},
        },
    )

    assert rows[0]["scores"] == {
        "ABC": {"level": 3, "score": 15.0},
        "AZT": {"level": 1, "score": -5.0},
    }
    assert result["pattern_rows"] == 2
    assert result["drug_pattern_score_pairs"] == 4
    assert result["exact_pattern_score_pairs"] == 2
    assert result["non_exact_pattern_score_pairs"] == 2
    assert result["drug_classes"] == {"NRTI": 2}
    assert result["genes"] == {"RT": 2}
    assert result["pattern_report_rows"] == [
        {
            "source_pattern_file": "patterns-NRTI.json",
            "drug_class": "NRTI",
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:421707",
            "standard_inchi_key": "MCI",
            "pattern_rows": 2,
            "nonzero_score_rows": 2,
            "max_level": 4,
            "min_score": 15.0,
            "max_score": 30.0,
        },
        {
            "source_pattern_file": "patterns-NRTI.json",
            "drug_class": "NRTI",
            "source_record_id": "AZT",
            "source_name": "zidovudine",
            "mapping_status": "AMBIGUOUS_IDENTITY",
            "identifier": "",
            "standard_inchi_key": "",
            "pattern_rows": 2,
            "nonzero_score_rows": 2,
            "max_level": 5,
            "min_score": -5.0,
            "max_score": 60.0,
        },
    ]


def test_read_drug_patterns_accepts_empty_pattern_files(tmp_path):
    path = tmp_path / "patterns-CAI.json"
    path.write_text("[]", encoding="utf-8")

    assert read_drug_patterns(path, hivdb_source_rows()) == []


def test_read_drug_patterns_rejects_bad_matrices(tmp_path):
    path = tmp_path / "patterns-NRTI.json"
    source_rows = [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "synonyms": "",
        }
    ]

    path.write_text(json.dumps({}), encoding="utf-8")
    with pytest.raises(ValueError, match="expected a JSON array"):
        read_drug_patterns(path, source_rows)

    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 3,
                }
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(
        ValueError,
        match=r"missing=\['ABC Score'\]",
    ):
        read_drug_patterns(path, source_rows)

    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 6,
                    "ABC Score": 15.0,
                }
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="invalid ABC Level"):
        read_drug_patterns(path, source_rows)

    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 3,
                    "ABC Score": "15.0",
                }
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="invalid ABC Score"):
        read_drug_patterns(path, source_rows)

    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "CAI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 3,
                    "ABC Score": 15.0,
                }
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="unknown drugClass 'CAI'"):
        read_drug_patterns(path, source_rows)

    path.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 3,
                    "ABC Score": 15.0,
                },
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 1,
                    "ABC Level": 3,
                    "ABC Score": 15.0,
                },
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate NRTI RT pattern M184V"):
        read_drug_patterns(path, source_rows)


def test_read_hiv1_algorithm_audits_drug_specific_score_rules(tmp_path):
    path = tmp_path / "HIVDB_10.2.xml"
    path.write_text(hivdb_algorithm_xml(), encoding="utf-8")

    rows = read_hiv1_algorithm(path, algorithm_source_rows())
    result = evaluate_hiv1_algorithm_rules(
        rows,
        {
            "ABC": {
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
            },
            "AZT": {"mapping_status": "AMBIGUOUS_IDENTITY"},
        },
    )

    assert rows == [
        {
            "algorithm_name": "HIVDB",
            "algorithm_version": "10.2",
            "algorithm_date": "2026-04-26",
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "algorithm_full_name": "abacavir",
            "full_name_matches": "true",
            "drug_class": "NRTI",
            "uses_global_range": "true",
            "score_terms": 2,
            "score_assignments": 3,
            "negative_score_assignments": 1,
            "min_score": -10.0,
            "max_score": 15.0,
            "score_term_rows": [
                {
                    "score_term_index": 1,
                    "score_term": "65R => -10",
                    "score_assignments": 1,
                    "negative_score_assignments": 1,
                    "min_score": -10.0,
                    "max_score": -10.0,
                },
                {
                    "score_term_index": 2,
                    "score_term": "MAX(184I => 15, 184V => 15)",
                    "score_assignments": 2,
                    "negative_score_assignments": 0,
                    "min_score": 15.0,
                    "max_score": 15.0,
                },
            ],
        },
        {
            "algorithm_name": "HIVDB",
            "algorithm_version": "10.2",
            "algorithm_date": "2026-04-26",
            "source_record_id": "AZT",
            "source_name": "zidovudine",
            "algorithm_full_name": "azidothymidine",
            "full_name_matches": "false",
            "drug_class": "NRTI",
            "uses_global_range": "true",
            "score_terms": 1,
            "score_assignments": 1,
            "negative_score_assignments": 0,
            "min_score": 15.0,
            "max_score": 15.0,
            "score_term_rows": [
                {
                    "score_term_index": 1,
                    "score_term": "41L => 15",
                    "score_assignments": 1,
                    "negative_score_assignments": 0,
                    "min_score": 15.0,
                    "max_score": 15.0,
                },
            ],
        },
    ]
    assert result["algorithm_drugs"] == 2
    assert result["score_terms"] == 3
    assert result["score_assignments"] == 4
    assert result["exact_score_assignments"] == 3
    assert result["non_exact_score_assignments"] == 1
    assert result["full_name_mismatches"] == 1
    assert result["algorithm_report_rows"][0]["mapping_status"] == "EXACT"
    assert result["algorithm_term_report_rows"][1] == with_hivdb_score_rule_id(
        {
            "source_version": HIVDB_HIVFACTS_COMMIT,
            "algorithm_name": "HIVDB",
            "algorithm_version": "10.2",
            "algorithm_date": "2026-04-26",
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "algorithm_full_name": "abacavir",
            "full_name_matches": "true",
            "drug_class": "NRTI",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:421707",
            "standard_inchi_key": "MCI",
            "score_term_index": 2,
            "score_term": "MAX(184I => 15, 184V => 15)",
            "score_assignments": 2,
            "negative_score_assignments": 0,
            "min_score": 15.0,
            "max_score": 15.0,
        }
    )


def test_read_hiv1_algorithm_rejects_bad_drug_score_rules(tmp_path):
    path = tmp_path / "HIVDB_10.2.xml"

    path.write_text(
        hivdb_algorithm_xml(abc_condition="65R => -10"),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="ABC rule is not a SCORE FROM block"):
        read_hiv1_algorithm(path, algorithm_source_rows())

    path.write_text(
        hivdb_algorithm_xml(
            abc_condition="SCORE FROM (65R)",
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="score term 1 has no score assignment"):
        read_hiv1_algorithm(path, algorithm_source_rows())

    path.write_text(
        hivdb_algorithm_xml(abc_actions="<SCORERANGE/>"),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="ABC does not use GLOBALRANGE"):
        read_hiv1_algorithm(path, algorithm_source_rows())


def test_write_drug_map_template_preserves_hivdb_source_columns(tmp_path):
    path = tmp_path / "hivdb_drug_map.tsv"
    write_drug_map_template(
        [
            {
                "source_record_id": "ABC",
                "display_abbr": "ABC",
                "name": "ABC",
                "full_name": "abacavir",
                "drug_class": "NRTI",
                "mapping_status": "",
                "identifier": "",
                "standard_inchi_key": "",
                "mapping_basis": "",
                "mapping_notes": "",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    assert rows == [
        {
            "source_version": HIVDB_HIVFACTS_COMMIT,
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "hivdb_name": "ABC",
            "drug_class": "NRTI",
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "notes": "",
        }
    ]


def test_write_drug_report_preserves_hivdb_identity_columns(tmp_path):
    path = tmp_path / "hivdb_drug_report.tsv"

    write_drug_report(
        [
            {
                "source_record_id": "ABC",
                "display_abbr": "ABC",
                "name": "ABC",
                "full_name": "abacavir",
                "drug_class": "NRTI",
                "ritonavir_boosted": "false",
                "synonyms": "",
                "exact_name_candidate_count": 1,
                "exact_name_candidate_identifiers": "CHEBI:421707",
                "exact_name_candidate_inchi_keys": "MCI",
                "matched_aliases": "abacavir",
                "mapping_status": "",
                "identifier": "",
                "standard_inchi_key": "",
                "mapping_basis": "",
                "mapping_notes": "",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    assert rows == [
        {
            "source_record_id": "ABC",
            "display_abbr": "ABC",
            "name": "ABC",
            "full_name": "abacavir",
            "drug_class": "NRTI",
            "ritonavir_boosted": "false",
            "synonyms": "",
            "exact_name_candidate_count": "1",
            "exact_name_candidate_identifiers": "CHEBI:421707",
            "exact_name_candidate_inchi_keys": "MCI",
            "matched_aliases": "abacavir",
            "mapping_status": "",
            "identifier": "",
            "standard_inchi_key": "",
            "mapping_basis": "",
            "mapping_notes": "",
        }
    ]


def test_write_mutation_report_preserves_class_level_mutation_columns(tmp_path):
    path = tmp_path / "hivdb_mutations.tsv"

    write_mutation_report(
        [
            {
                "source_list": "DRM",
                "drug_class": "NRTI",
                "gene": "RT",
                "position": "184",
                "aa": "VI",
                "expanded_mutation_count": 2,
                "expanded_mutations": "RT:184V|RT:184I",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == MUTATION_REPORT_COLUMNS
        rows = list(reader)

    assert rows == [
        {
            "source_list": "DRM",
            "drug_class": "NRTI",
            "gene": "RT",
            "position": "184",
            "aa": "VI",
            "expanded_mutation_count": "2",
            "expanded_mutations": "RT:184V|RT:184I",
        }
    ]


def test_write_pattern_report_preserves_hivdb_score_columns(tmp_path):
    path = tmp_path / "hivdb_patterns.tsv"

    write_pattern_report(
        [
            {
                "source_pattern_file": "patterns-NRTI.json",
                "drug_class": "NRTI",
                "source_record_id": "ABC",
                "source_name": "abacavir",
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
                "pattern_rows": 2,
                "nonzero_score_rows": 2,
                "max_level": 4,
                "min_score": 15.0,
                "max_score": 30.0,
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == PATTERN_REPORT_COLUMNS
        rows = list(reader)

    assert rows == [
        {
            "source_pattern_file": "patterns-NRTI.json",
            "drug_class": "NRTI",
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:421707",
            "standard_inchi_key": "MCI",
            "pattern_rows": "2",
            "nonzero_score_rows": "2",
            "max_level": "4",
            "min_score": "15.0",
            "max_score": "30.0",
        }
    ]


def test_write_algorithm_report_preserves_hivdb_score_rule_columns(tmp_path):
    path = tmp_path / "hivdb_algorithm.tsv"

    write_algorithm_report(
        [
            {
                "source_version": HIVDB_HIVFACTS_COMMIT,
                "algorithm_name": "HIVDB",
                "algorithm_version": "10.2",
                "algorithm_date": "2026-04-26",
                "source_record_id": "ABC",
                "source_name": "abacavir",
                "algorithm_full_name": "abacavir",
                "full_name_matches": "true",
                "drug_class": "NRTI",
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
                "score_terms": 2,
                "score_assignments": 3,
                "negative_score_assignments": 1,
                "min_score": -10.0,
                "max_score": 15.0,
                "uses_global_range": "true",
            }
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ALGORITHM_REPORT_COLUMNS
        rows = list(reader)

    assert rows == [
        {
            "source_version": HIVDB_HIVFACTS_COMMIT,
            "algorithm_name": "HIVDB",
            "algorithm_version": "10.2",
            "algorithm_date": "2026-04-26",
            "source_record_id": "ABC",
            "source_name": "abacavir",
            "algorithm_full_name": "abacavir",
            "full_name_matches": "true",
            "drug_class": "NRTI",
            "mapping_status": "EXACT",
            "identifier": "CHEBI:421707",
            "standard_inchi_key": "MCI",
            "score_terms": "2",
            "score_assignments": "3",
            "negative_score_assignments": "1",
            "min_score": "-10.0",
            "max_score": "15.0",
            "uses_global_range": "true",
        }
    ]


def test_write_algorithm_term_report_preserves_hivdb_score_formula_terms(tmp_path):
    path = tmp_path / "hivdb_algorithm_terms.tsv"

    write_algorithm_term_report(
        [
            with_hivdb_score_rule_id(
                {
                    "source_version": HIVDB_HIVFACTS_COMMIT,
                    "algorithm_name": "HIVDB",
                    "algorithm_version": "10.2",
                    "algorithm_date": "2026-04-26",
                    "source_record_id": "ABC",
                    "source_name": "abacavir",
                    "algorithm_full_name": "abacavir",
                    "full_name_matches": "true",
                    "drug_class": "NRTI",
                    "mapping_status": "EXACT",
                    "identifier": "CHEBI:421707",
                    "standard_inchi_key": "MCI",
                    "score_term_index": 2,
                    "score_term": "MAX(184I => 15, 184V => 15)",
                    "score_assignments": 2,
                    "negative_score_assignments": 0,
                    "min_score": 15.0,
                    "max_score": 15.0,
                }
            )
        ],
        path,
    )

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        assert reader.fieldnames == ALGORITHM_TERM_REPORT_COLUMNS
        rows = list(reader)

    assert rows == [
        with_hivdb_score_rule_id(
            {
                "source_version": HIVDB_HIVFACTS_COMMIT,
                "algorithm_name": "HIVDB",
                "algorithm_version": "10.2",
                "algorithm_date": "2026-04-26",
                "source_record_id": "ABC",
                "source_name": "abacavir",
                "algorithm_full_name": "abacavir",
                "full_name_matches": "true",
                "drug_class": "NRTI",
                "mapping_status": "EXACT",
                "identifier": "CHEBI:421707",
                "standard_inchi_key": "MCI",
                "score_term_index": "2",
                "score_term": "MAX(184I => 15, 184V => 15)",
                "score_assignments": "2",
                "negative_score_assignments": "0",
                "min_score": "15.0",
                "max_score": "15.0",
            }
        )
    ]


def test_cli_writes_non_seeding_drug_audit(tmp_path):
    directory = tmp_path / "data" / "antibiotics" / "antiviral"
    directory.mkdir(parents=True)
    record = {
        "identifier": "CHEBI:421707",
        "label": "abacavir",
        "chemical_structure": {"standard_inchi_key": "MCI"},
    }
    (directory / "abacavir.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")

    drugs = tmp_path / "drugs.json"
    drugs.write_text(
        json.dumps(
            [
                {
                    "displayAbbr": "ABC",
                    "drugClass": "NRTI",
                    "fullName": "abacavir",
                    "name": "ABC",
                }
            ]
        ),
        encoding="utf-8",
    )
    report = tmp_path / "hivdb.tsv"
    drug_map = tmp_path / "hivdb_drug_map_in.tsv"
    drug_map.write_text(
        "\t".join(DRUG_MAP_COLUMNS)
        + "\n"
        + f"{HIVDB_HIVFACTS_COMMIT}\tABC\tabacavir\tABC\tNRTI\t"
        + "EXACT\tCHEBI:421707\t"
        + "MCI\tfull_name\tHIVDB fullName is the exact corpus label.\n",
        encoding="utf-8",
    )
    drug_map_template = tmp_path / "hivdb_drug_map.tsv"
    drms = tmp_path / "drms_hiv1.json"
    drms.write_text(
        json.dumps({"NRTI": [{"gene": "RT", "position": 184, "aa": "VI"}]}),
        encoding="utf-8",
    )
    mutation_report = tmp_path / "hivdb_mutations.tsv"
    patterns = tmp_path / "patterns-NRTI.json"
    patterns.write_text(
        json.dumps(
            [
                {
                    "gene": "RT",
                    "drugClass": "NRTI",
                    "pattern": "M184V",
                    "count": 17,
                    "ABC Level": 3,
                    "ABC Score": 15.0,
                }
            ]
        ),
        encoding="utf-8",
    )
    pattern_report = tmp_path / "hivdb_patterns.tsv"
    algorithm = tmp_path / "HIVDB_10.2.xml"
    algorithm.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<ALGORITHM>
  <ALGNAME>HIVDB</ALGNAME>
  <ALGVERSION>10.2</ALGVERSION>
  <ALGDATE>2026-04-26</ALGDATE>
  <DEFINITIONS>
    <DRUGCLASS><NAME>NRTI</NAME><DRUGLIST>ABC</DRUGLIST></DRUGCLASS>
  </DEFINITIONS>
  <DRUG>
    <NAME>ABC</NAME>
    <FULLNAME>abacavir</FULLNAME>
    <RULE>
      <CONDITION><![CDATA[SCORE FROM (65R => -10, MAX(184I => 15, 184V => 15))]]></CONDITION>
      <ACTIONS><SCORERANGE><USE_GLOBALRANGE/></SCORERANGE></ACTIONS>
    </RULE>
  </DRUG>
</ALGORITHM>
""",
        encoding="utf-8",
    )
    algorithm_report = tmp_path / "hivdb_algorithm.tsv"
    algorithm_term_report = tmp_path / "hivdb_algorithm_terms.tsv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--drugs",
            str(drugs),
            "--drug-report",
            str(report),
            "--drug-map",
            str(drug_map),
            "--drug-map-template",
            str(drug_map_template),
            "--hiv1-drms",
            str(drms),
            "--mutation-report",
            str(mutation_report),
            "--hiv1-patterns",
            str(patterns),
            "--pattern-report",
            str(pattern_report),
            "--hiv1-algorithm",
            str(algorithm),
            "--algorithm-report",
            str(algorithm_report),
            "--algorithm-term-report",
            str(algorithm_term_report),
            "--corpus-root",
            str(tmp_path),
        ],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
        text=True,
        capture_output=True,
    )

    assert report.exists()
    assert drug_map_template.exists()
    assert mutation_report.exists()
    assert pattern_report.exists()
    assert algorithm_report.exists()
    assert algorithm_term_report.exists()
    with report.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert rows[0]["mapping_status"] == "EXACT"
    assert rows[0]["identifier"] == "CHEBI:421707"
    with mutation_report.open(newline="", encoding="utf-8") as handle:
        mutation_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert mutation_rows[0]["expanded_mutations"] == "RT:184V|RT:184I"
    with pattern_report.open(newline="", encoding="utf-8") as handle:
        pattern_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert pattern_rows[0]["mapping_status"] == "EXACT"
    assert pattern_rows[0]["pattern_rows"] == "1"
    with algorithm_report.open(newline="", encoding="utf-8") as handle:
        algorithm_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert algorithm_rows[0]["mapping_status"] == "EXACT"
    assert algorithm_rows[0]["score_assignments"] == "3"
    with algorithm_term_report.open(newline="", encoding="utf-8") as handle:
        algorithm_term_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert algorithm_term_rows[1]["score_term"] == "MAX(184I => 15, 184V => 15)"
    assert algorithm_term_rows[1]["score_assignments"] == "2"
    assert "Stanford HIVDB hivfacts drug identity audit" in result.stdout
    assert "HIV-1 class-level mutation lists: rows=1 expanded_mutations=2" in result.stdout
    assert "HIV-1 drug pattern matrices: rows=1 level_score_pairs=1" in result.stdout
    assert "HIV-1 algorithm score rules: drugs=1 score_assignments=3" in result.stdout
    assert "no rows seeded" in result.stdout

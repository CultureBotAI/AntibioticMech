"""Group membership must not flatten assays, drop unmatched isolates, or infer genomes."""

import argparse
import copy
import csv
import gzip
import json
import shutil
import subprocess
import sys
from pathlib import Path

import duckdb
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evaluate_cryptic_activity as cryptic  # noqa: E402
import evaluate_cryptic_membership as membership  # noqa: E402

KEY = "LKCWBDHBTVXHDL-RMDFUYIESA-N"
CODES = {"AMI": "AMIKACIN", "MIX": "MIXTURE"}
MAPPINGS = {
    "AMI": dict(source_version="3.4.0", source_record_id="AMI", source_name="AMIKACIN",
                mapping_status="EXACT", identifier="CHEBI:2637", standard_inchi_key=KEY,
                mapping_basis="curated", notes="exact structure"),
    "MIX": dict(source_version="3.4.0", source_record_id="MIX", source_name="MIXTURE",
                mapping_status="MIXTURE", identifier="", standard_inchi_key="",
                mapping_basis="curated", notes="not one structure"),
}


@pytest.fixture
def cohort(tmp_path):
    paths = {key: tmp_path / name for key, name in (
        ("dst", "DST_MEASUREMENTS.parquet"), ("ukmyc", "UKMYC_PHENOTYPES.parquet"),
        ("wgs", "WGS_SAMPLES.parquet"),
    )}
    with duckdb.connect() as connection:
        connection.execute("CREATE TABLE dst (DRUG VARCHAR, SOURCE VARCHAR, METHOD_1 VARCHAR, "
                           "METHOD_2 VARCHAR, METHOD_3 VARCHAR, METHOD_CC VARCHAR, METHOD_MIC VARCHAR, "
                           "PHENOTYPE VARCHAR, QUALITY VARCHAR, UNIQUEID VARCHAR)")
        dst_row = ("AMI", "source", "MGIT", None, None, None, None, "R", "HIGH")
        connection.executemany("INSERT INTO dst VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [
            (*dst_row, "a"), (*dst_row, "a"), (*dst_row, "b"),
            ("MIX", *dst_row[1:], "excluded"),
        ])
        connection.execute("CREATE TABLE ukmyc (DRUG VARCHAR, PLATEDESIGN VARCHAR, BELONGS_GPI BOOLEAN, "
                           "PHENOTYPE_QUALITY VARCHAR, READINGDAY BIGINT, PRIMARY_METHOD VARCHAR, "
                           "PHENOTYPE_DESCRIPTION VARCHAR, MIC VARCHAR, LOG2MIC DOUBLE, "
                           "BINARY_PHENOTYPE VARCHAR, UNIQUEID VARCHAR, SITEID VARCHAR)")
        ukmyc_row = ("AMI", "UKMYC6", False, "HIGH", 14, "VIZION", None, "<=0.25", -2.0, "S")
        connection.executemany("INSERT INTO ukmyc VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [
            (*ukmyc_row, "a", "site1"), (*ukmyc_row, "phenotype-only", "site2"),
            (*ukmyc_row[:7], ">0.25", *ukmyc_row[8:], "a", "site1"),
        ])
        connection.execute("CREATE TABLE wgs (UNIQUEID VARCHAR, sample_accession VARCHAR, "
                           "study_accession VARCHAR, run_accession VARCHAR, "
                           "has_multiple_ena_run_accessions BOOLEAN)")
        connection.executemany("INSERT INTO wgs VALUES (?, ?, ?, ?, ?)", [
            ("a", "SAMEA1", "PRJEB1", "ERR1", False),
            ("b", "SAMEA1", "PRJEB1", "ERR2", False),
            ("wgs-only", "SAMN2", "PRJNA2", "SRR3", False),
            ("excluded", "SAMD3", "PRJDB3", "DRR4", False),
        ])
        for key, path in paths.items():
            connection.table(key).write_parquet(str(path))
        inventory = cryptic.activity_inventory(connection, paths["dst"], paths["ukmyc"], CODES, MAPPINGS)
        yield connection, paths, inventory


def recover(cohort, inventory=None, mappings=None):
    connection, paths, original = cohort
    wgs = membership.wgs_index(connection, paths["wgs"])
    return membership.group_membership(connection, paths["dst"], paths["ukmyc"],
                                       original if inventory is None else inventory,
                                       MAPPINGS if mappings is None else mappings, wgs), wgs


def test_exact_typed_groups_preserve_multiplicity_missing_wgs_and_shared_samples(cohort):
    groups, wgs = recover(cohort)
    assert len(groups) == 3
    dst = next(group for group in groups if group["activity"]["source_table"] == cryptic.DST_TABLE)
    assert [(member["source_isolate_id"], member["measurement_count"]) for member in dst["members"]] == [
        ("a", 2), ("b", 1),
    ]
    assert [member["sequencing_context"]["biosample_accession"] for member in dst["members"]] == [
        "SAMEA1", "SAMEA1",
    ]
    ukmyc = [group for group in groups if group["activity"]["source_table"] == cryptic.UKMYC_TABLE]
    assert {group["activity"]["mic_qualifier"] for group in ukmyc} == {"<=", ">"}
    assert {group["activity"]["belongs_gpi"] for group in ukmyc} == {"false"}
    assert {group["activity"]["log2mic"] for group in ukmyc} == {"-2.0"}
    missing = [member for group in groups for member in group["members"]
               if member["source_isolate_id"] == "phenotype-only"]
    assert missing == [dict(source_isolate_id="phenotype-only", measurement_count=1, sequencing_context=None)]
    summary = membership.summarize(groups, wgs)
    assert summary == {
        "groups": 3, "compounds": 1, "measurements": 6, "group_isolate_memberships": 5,
        "largest_group_isolates": 2, "memberships_without_wgs": 1, "measurements_without_wgs": 1,
        "source_isolate_ids": 3, "source_isolate_ids_with_wgs": 2, "source_isolate_ids_without_wgs": 1,
        "biosamples": 1, "bioprojects": 1, "sequencing_runs": 2,
        "wgs_source_ids_not_in_adopted_phenotypes": 2,
        "by_compound": {"CHEBI:2637": {"groups": 3, "measurements": 6,
                                       "group_isolate_memberships": 5, "memberships_without_wgs": 1}},
    }
    assert not any(key in membership.json_line(group).decode() for group in groups
                   for key in ("taxon_id", "assembly_accession"))


@pytest.mark.parametrize("field", ["row_count", "isolate_count"])
def test_count_drift_fails_closed(cohort, field):
    changed = copy.deepcopy(cohort[2])
    changed[0][field] = "9"
    with pytest.raises(ValueError, match="count mismatch"):
        recover(cohort, changed)


def test_group_set_and_exact_identity_must_match(cohort):
    with pytest.raises(ValueError, match="unadopted group"):
        recover(cohort, cohort[2][1:])
    changed = copy.deepcopy(cohort[2])
    changed[0]["identifier"] = "CHEBI:9"
    with pytest.raises(ValueError, match="chemical identity"):
        recover(cohort, changed)
    with pytest.raises(ValueError, match="unmapped CRyPTIC drug code"):
        recover(cohort, mappings={"AMI": MAPPINGS["AMI"]})


def test_inventory_reproduction_compares_all_fields_and_rejects_duplicate_groups(cohort):
    rows = cohort[2]
    membership.require_same_inventory(rows, list(reversed(rows)))
    changed = copy.deepcopy(rows)
    changed[0]["source_name"] = "wrong"
    with pytest.raises(ValueError, match="does not match"):
        membership.require_same_inventory(rows, changed)
    with pytest.raises(ValueError, match="duplicate CRyPTIC activity_group_id"):
        membership.require_same_inventory(rows, [*rows, rows[0]])


@pytest.mark.parametrize("value", [None, "", " a", "a ", "a\nb", 42])
def test_invalid_source_ids_are_not_dropped_or_normalized(value):
    with pytest.raises(ValueError, match="UNIQUEID"):
        membership.require_source_id(value)


@pytest.mark.parametrize("assignment", [
    "sample_accession = 'not-a-sample'", "study_accession = 'not-a-project'",
    "run_accession = 'ERR1;ERR2'", "run_accession = 'ERX1'", "run_accession = NULL",
    "has_multiple_ena_run_accessions = TRUE", "has_multiple_ena_run_accessions = NULL",
    "UNIQUEID = 'a'", "UNIQUEID = NULL",
])
def test_malformed_wgs_links_and_duplicate_source_ids_fail_closed(cohort, assignment):
    connection, paths, _ = cohort
    connection.execute(f"UPDATE wgs SET {assignment}")
    connection.table("wgs").write_parquet(str(paths["wgs"]))
    with pytest.raises(ValueError, match="CRyPTIC"):
        membership.wgs_index(connection, paths["wgs"])


def test_missing_exact_phenotype_id_is_an_error_not_reduced_coverage(cohort):
    connection, paths, _ = cohort
    connection.execute("UPDATE dst SET UNIQUEID = NULL WHERE UNIQUEID = 'a'")
    connection.table("dst").write_parquet(str(paths["dst"]))
    with pytest.raises(ValueError, match="UNIQUEID"):
        recover(cohort)


def fixture_args(cohort, tmp_path, monkeypatch):
    _, paths, inventory = cohort
    drug_codes = tmp_path / "DRUG_CODES.csv.gz"
    with gzip.open(drug_codes, "wt") as handle:
        writer = csv.writer(handle)
        writer.writerow(["DRUG_3_LETTER_CODE", "DRUG_NAME"])
        writer.writerows(CODES.items())
    drug_map, adopted = tmp_path / "drug-map.tsv", tmp_path / "activity.tsv"
    with drug_map.open("w") as handle:
        writer = csv.DictWriter(handle, fieldnames=cryptic.DRUG_MAP_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(MAPPINGS.values())
    cryptic.write_inventory(adopted, inventory)
    monkeypatch.setattr(cryptic, "EXPECTED_MD5", {
        path.name: cryptic.md5_of(path) for path in (*paths.values(), drug_codes)
    })
    monkeypatch.setattr(cryptic, "corpus_structure_keys", lambda: {"CHEBI:2637": KEY})
    return argparse.Namespace(**paths, drug_codes=drug_codes, drug_map=drug_map,
                              inventory=adopted, output_dir=tmp_path / "evaluation")


def test_end_to_end_is_deterministic_pinned_and_evaluation_only(cohort, tmp_path, monkeypatch):
    args = fixture_args(cohort, tmp_path, monkeypatch)
    report = membership.evaluate(args)
    artifact = args.output_dir / report["artifact"]["path"]
    assert membership.sha256(artifact) == report["artifact"]["sha256"]
    with gzip.open(artifact, "rt") as handle:
        header, *groups = [json.loads(line) for line in handle]
    assert header["status"] == "EVALUATION_ONLY"
    assert header["source_version"] == "3.4.0"
    assert header["inputs"]["inventory"]["sha256"] == membership.sha256(args.inventory)
    assert len(groups) == 3
    assert report == json.loads((args.output_dir / "report.json").read_text())
    args.output_dir = tmp_path / "second"
    again = membership.evaluate(args)
    assert again == report
    assert (args.output_dir / artifact.name).read_bytes() == artifact.read_bytes()
    moved = tmp_path / "moved-inputs"
    moved.mkdir()
    for name in ("dst", "ukmyc", "wgs", "drug_codes", "drug_map", "inventory"):
        source = getattr(args, name)
        target = moved / source.name
        shutil.copyfile(source, target)
        setattr(args, name, target)
    args.output_dir = tmp_path / "third"
    assert membership.evaluate(args) == report
    assert (args.output_dir / artifact.name).read_bytes() == artifact.read_bytes()


def test_changed_release_file_is_rejected_before_output(cohort, tmp_path, monkeypatch):
    args = fixture_args(cohort, tmp_path, monkeypatch)
    args.wgs.write_bytes(b"changed")
    with pytest.raises(ValueError, match="pinned release checksum"):
        membership.evaluate(args)
    assert not args.output_dir.exists()


def test_inputs_changing_during_evaluation_do_not_receive_valid_pins(cohort, tmp_path, monkeypatch):
    args = fixture_args(cohort, tmp_path, monkeypatch)
    original = membership.group_membership

    def change(*arguments):
        result = original(*arguments)
        args.inventory.write_text("changed")
        return result

    monkeypatch.setattr(membership, "group_membership", change)
    with pytest.raises(ValueError, match="input changed"):
        membership.evaluate(args)
    assert not args.output_dir.exists()


def test_cli_refuses_existing_output_and_production_paths(tmp_path):
    for path in (tmp_path, membership.ROOT / "data" / "nonexistent-membership-evaluation"):
        result = subprocess.run([sys.executable, membership.__file__, "--output-dir", str(path)],
                                capture_output=True, text=True)
        assert result.returncode != 0
        assert "refusing to overwrite" in result.stderr or "production directories" in result.stderr

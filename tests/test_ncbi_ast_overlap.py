"""Cross-source sample overlap must track the actually adopted phenotype slice."""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from antibioticmech.activity_collections import pack_activities

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_ncbi_ast_overlap as audit  # noqa: E402
import evaluate_cryptic_activity as cryptic  # noqa: E402


def test_inventory_comparison_is_order_independent_but_checks_all_content():
    rows = [dict(activity_group_id="a", row_count="2"), dict(activity_group_id="b", row_count="1")]
    audit.require_same_inventory(rows, list(reversed(rows)))
    for changed in ([rows[0]], [rows[0], rows[0]], [rows[0], dict(rows[1], row_count="9")]):
        with pytest.raises(ValueError, match="adopted inventory"):
            audit.require_same_inventory(rows, changed)


def test_checksum_pins_include_the_published_wgs_mapping(tmp_path):
    path = tmp_path / "WGS_SAMPLES.parquet"
    assert cryptic.EXPECTED_MD5[path.name] == "ea798f4cfc28525cf394ff9196c93021"
    path.write_bytes(b"not the release")
    with pytest.raises(ValueError, match="pinned release checksum"):
        cryptic.verify_release_file(path)


class MembershipConnection:
    """Exercise membership semantics independently of the optional parquet reader."""

    def __init__(self, phenotype_rows, wgs_rows):
        self.phenotype_rows = phenotype_rows
        self.wgs_rows = wgs_rows

    def execute(self, query, params):
        self.result = self.wgs_rows if "study_accession" in query else self.phenotype_rows
        return self

    def fetchall(self):
        return self.result


MAPPINGS = {
    "A": dict(mapping_status="EXACT", identifier="CHEBI:1"),
    "B": dict(mapping_status="MIXTURE", identifier=""),
}


def membership(connection):
    return audit.cryptic_membership(connection, Path("dst"), Path("ukmyc"), Path("wgs"), MAPPINGS)


def test_only_adopted_drugs_contribute_sample_membership_and_missing_links_are_counted():
    result = membership(MembershipConnection(
        [("adopted", "A"), ("unmapped", "B"), ("phenotype-only", "A")],
        [("adopted", "SAMEA1", "PRJEB1"), ("unmapped", "SAMEA2", "PRJEB2"),
         ("wgs-only", "SAMEA3", "PRJEB3")],
    ))
    assert result["all_samples"] == {"SAMEA1", "SAMEA2", "SAMEA3"}
    assert result["projects"] == {"PRJEB1"}
    assert result["drugs_by_sample"] == {"SAMEA1": {"CHEBI:1"}}
    assert result["counts"]["adopted_phenotype_uniqueids_without_wgs"] == 1


@pytest.mark.parametrize("rows", [
    [("a", "SAMN1", "PRJNA1"), ("a", "SAMN2", "PRJNA1")],
    [("a", "", "PRJNA1")], [("a", "SAMN1", "bad-project")],
])
def test_bad_or_conflicting_wgs_identity_is_rejected(rows):
    with pytest.raises(ValueError, match="CRyPTIC WGS mapping"):
        membership(MembershipConnection([("a", "A")], rows))


def test_shared_project_is_not_shared_sample_and_shared_sample_is_not_shared_drug():
    index = {"all_samples": {"SAMN1", "SAMN2"}, "projects": {"PRJNA1"},
             "drugs_by_sample": {"SAMN1": {"CHEBI:1"}}}
    rows = [
        dict(biosample_accession="SAMN1", bioproject_accession="PRJNA1",
             identifier="CHEBI:1", ast_row_count="2"),
        dict(biosample_accession="SAMN1", bioproject_accession="PRJNA1",
             identifier="CHEBI:2", ast_row_count="3"),
        dict(biosample_accession="SAMN9", bioproject_accession="PRJNA1",
             identifier="CHEBI:1", ast_row_count="7"),
        dict(biosample_accession="SAMN2", bioproject_accession="PRJNA2",
             identifier="CHEBI:1", ast_row_count="1"),
    ]
    result = audit.overlap_summary(rows, index, raw=False, mappings={})
    assert result["measurements"] == 13
    assert result["shared_wgs_sample_measurements"] == 6
    assert result["shared_adopted_sample_measurements"] == 5
    assert result["shared_adopted_sample_and_drug_measurements"] == 2
    assert result["shared_adopted_project_measurements"] == 12
    assert result["shared_adopted_biosamples"] == ["SAMN1"]
    raw = [dict(BioSample="SAMN1", BioProject="PRJNA1", Antibiotic="drug")]
    result = audit.overlap_summary(raw, index, raw=True,
                                   mappings={"drug": dict(identifier="CHEBI:1")})
    assert result["shared_adopted_sample_and_drug_measurements"] == 1


def test_parquet_membership_join(tmp_path):
    duckdb = pytest.importorskip("duckdb")
    dst, ukmyc, wgs = [tmp_path / name for name in ("dst.parquet", "ukmyc.parquet", "wgs.parquet")]
    with duckdb.connect() as connection:
        connection.execute("CREATE TABLE dst AS SELECT 'a' AS UNIQUEID, 'A' AS DRUG")
        connection.execute("CREATE TABLE ukmyc AS SELECT 'b' AS UNIQUEID, 'B' AS DRUG")
        connection.execute("CREATE TABLE wgs AS SELECT 'a' AS UNIQUEID, "
                           "'SAMN1' AS sample_accession, 'PRJNA1' AS study_accession")
        for table, path in (("dst", dst), ("ukmyc", ukmyc), ("wgs", wgs)):
            connection.execute(f"COPY {table} TO '{path}' (FORMAT PARQUET)")
        result = audit.cryptic_membership(connection, dst, ukmyc, wgs, MAPPINGS)
    assert result["drugs_by_sample"] == {"SAMN1": {"CHEBI:1"}}


def test_cli_refuses_to_overwrite_any_existing_report(tmp_path):
    path = tmp_path / "report.json"
    path.write_text("retain")
    command = [sys.executable, str(Path(audit.__file__))]
    for option in ("ast", "activity-report", "isolate-snapshot", "wgs", "report"):
        command.extend(["--" + option, str(path)])
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode != 0
    assert "refusing to overwrite" in result.stderr
    assert path.read_text() == "retain"


KEY = "AAAAAAAAAAAAAA-BBBBBBBBBB-N"


def corpus_record(tmp_path, observations):
    doc = {"identifier": "CHEBI:1", "chemical_structure": {"standard_inchi_key": KEY},
           "activity_spectrum": observations}
    path = tmp_path / "drug.yaml"
    path.write_text(yaml.safe_dump(doc))
    return path, doc


def test_corpus_membership_preserves_unsourced_evidence_and_nested_contexts(tmp_path):
    path, _ = corpus_record(tmp_path, [
        {"biosample_accession": "SAMN1", "bioproject_accession": "PRJNA1",
         "evidence": [{"reference": "https://example.org/isolate"}]},
        {"source": "CURATOR", "pathogen_detection_contexts": [
            {"biosample_accession": "SAMN2", "bioproject_accession": "PRJNA2"},
            {"biosample_accession": "SAMN2", "bioproject_accession": "PRJNA2"},
            {"biosample_accession": "SAMEA3"},
        ]},
        {"taxon_label": "A species", "measurement_count": 100},
        {"source": "NCBI_AST", "biosample_accession": "SAMN4"},
    ])
    result = audit.corpus_membership(tmp_path)
    assert result["counts"] == {
        "records": 1, "observations": 3, "observations_with_biosample": 2,
        "observations_without_biosample": 1, "ast_observations_excluded": 1,
        "biosamples": 3, "bioprojects": 2,
    }
    assert set(result["by_sample"]) == {"SAMN1", "SAMN2", "SAMEA3"}
    assert len(result["by_sample"]["SAMN2"]) == 1
    first = result["by_sample"]["SAMN1"][0]
    assert first["record"] == str(path)
    assert first["activity_observation_number"] == 1
    assert first["source"] is None
    assert first["evidence"] == [{"reference": "https://example.org/isolate"}]
    assert result["by_sample"]["SAMEA3"][0]["activity_observation_number"] == 2


def test_existing_corpus_overlap_is_a_review_lead_not_a_duplicate_decision(tmp_path):
    corpus_record(tmp_path, [{"biosample_accession": "SAMN1", "bioproject_accession": "PRJNA1"}])
    index = audit.corpus_membership(tmp_path)
    base = dict(biosample_accession="SAMN1", bioproject_accession="PRJNA1",
                source_name="drug", identifier="CHEBI:1", standard_inchi_key=KEY, ast_row_count="2")
    rows = [base, dict(base, identifier="CHEBI:2", ast_row_count="3"),
            dict(base, standard_inchi_key="CCCCCCCCCCCCCC-BBBBBBBBBB-N", ast_row_count="5"),
            dict(base, biosample_accession="SAMN9", ast_row_count="7")]
    expected_rows = [dict(row) for row in rows]
    result = audit.corpus_overlap_summary(rows, index, raw=False, mappings={})
    assert result["groups_or_rows"] == 4
    assert result["export_rows"] == 17
    assert result["shared_sample_export_rows"] == 10
    assert result["shared_sample_and_compound_export_rows"] == 2
    assert result["shared_project_export_rows"] == 17
    lead, = result["sample_review_leads"]
    assert lead["biosample_accession"] == "SAMN1"
    assert lead["exact_matched_identifiers"] == ["CHEBI:1"]
    assert lead["existing_observations"][0]["activity_observation_number"] == 1
    assert rows == expected_rows


@pytest.mark.parametrize("status,expected", [(None, 0), ("MIXTURE", 0), ("EXACT", 1)])
def test_raw_unmapped_drugs_still_report_shared_samples_without_claiming_identity(tmp_path, status, expected):
    corpus_record(tmp_path, [{"biosample_accession": "SAMN1"}])
    index = audit.corpus_membership(tmp_path)
    mapping = {"drug": {"mapping_status": status, "identifier": "CHEBI:1", "standard_inchi_key": KEY}}
    rows = [{"BioSample": "SAMN1", "Antibiotic": "drug"}]
    result = audit.corpus_overlap_summary(rows, index, raw=True, mappings=mapping)
    assert result["shared_sample_export_rows"] == 1
    assert result["shared_sample_and_compound_export_rows"] == expected
    assert result["sample_review_leads"][0]["source_names"] == ["drug"]


def test_collection_backed_records_are_expanded_and_ast_rows_do_not_match_themselves(tmp_path):
    path, doc = corpus_record(tmp_path, [
        {"source": "NCBI_AST", "source_version": "test", "source_retrieved_on": "2026-10-03",
         "source_observation_id": str(i), "measurement_count": 1, "biosample_accession": "SAMN1"}
        for i in range(500)
    ] + [{"biosample_accession": "SAMN2"}])
    physical, artifacts = pack_activities(doc)
    path.write_text(yaml.safe_dump(physical))
    for name, payload in artifacts.items():
        (tmp_path / name).write_bytes(payload)
    result = audit.corpus_membership(tmp_path)
    assert result["counts"]["ast_observations_excluded"] == 500
    assert set(result["by_sample"]) == {"SAMN2"}
    assert result["by_sample"]["SAMN2"][0]["activity_observation_number"] == 501
    assert len(result["inputs"]) == 2
    (tmp_path / next(iter(artifacts))).write_bytes(b"changed")
    with pytest.raises(ValueError, match="corpus changed"):
        audit.require_same_corpus(tmp_path, result["inputs"])
    with pytest.raises(ValueError, match="bytes do not match"):
        audit.corpus_membership(tmp_path)


@pytest.mark.parametrize("change", ["edit", "add", "delete"])
def test_changed_corpus_cannot_keep_an_old_overlap_pin(tmp_path, change):
    path, doc = corpus_record(tmp_path, [])
    inputs = audit.corpus_input_hashes(tmp_path)
    if change == "edit":
        path.write_text(yaml.safe_dump(dict(doc, label="changed")))
    elif change == "add":
        (tmp_path / "other.yaml").write_text(yaml.safe_dump(doc))
    else:
        path.unlink()
    with pytest.raises(ValueError, match="corpus"):
        audit.require_same_corpus(tmp_path, inputs)


@pytest.mark.parametrize("row", [
    {"biosample_accession": "not-a-sample"}, {"bioproject_accession": "not-a-project"},
])
def test_invalid_existing_accessions_are_rejected(tmp_path, row):
    corpus_record(tmp_path, [row])
    with pytest.raises(ValueError, match="invalid Bio"):
        audit.corpus_membership(tmp_path)


def test_empty_corpus_is_not_negative_overlap_evidence(tmp_path):
    with pytest.raises(ValueError, match="empty existing corpus"):
        audit.corpus_membership(tmp_path)

"""Cross-source sample overlap must track the actually adopted phenotype slice."""

import subprocess
import sys
from pathlib import Path

import pytest

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

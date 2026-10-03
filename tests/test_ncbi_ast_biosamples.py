"""One submitted assay may have several genome links, but is not several assays."""

import copy
import io
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ncbi_ast_biosamples as biosamples  # noqa: E402
import seed_from_sources as seed  # noqa: E402
from audit_ncbi_ast_biosamples import verify_source_review  # noqa: E402
from ncbi_ast_isolates import file_sha256  # noqa: E402
from test_ncbi_ast_import import ncbi_ast_row, write_activity_report  # noqa: E402


def pair(**overrides):
    common = dict(
        ast_row_count="1",
        taxon_label="Escherichia coli",
        method="",
        platform="Vitek",
        vendor="Biomerieux",
        reagent="",
        phenotype="resistant",
    )
    common.update(overrides)
    return [
        ncbi_ast_row(
            **common,
            target_accession=f"PDT00000000{i}.1",
            assembly_accession=f"GCA_00000000{i}.1",
            bioproject_accession=f"PRJNA{i}",
            create_date=f"2026-01-0{i}",
        )
        for i in (1, 2)
    ]


def submitted(row):
    return dict(
        zip(
            biosamples.HEADERS,
            [
                row["source_name"],
                row["phenotype"],
                row["mic_qualifier"] or "==",
                row["mic_value"],
                "mg/L",
                "MIC",
                row["platform"],
                row["vendor"],
                row["reagent"],
                row["standard"] or "missing",
            ],
            strict=True,
        )
    )


def sample(rows):
    return {
        rows[0]["biosample_accession"]: dict(
            taxon_id=rows[0]["taxon_id"],
            taxon_label=rows[0]["taxon_label"],
            last_update="2026-01-01T12:34:56",
            rows=[submitted(row) for row in rows],
        )
    }


def review_file(tmp_path, rows, samples):
    inventory = tmp_path / "activity.tsv"
    write_activity_report(inventory, rows)
    metadata = dict(
        activity_report_sha256=file_sha256(inventory), sha256="a" * 64, source_retrieved_on="2026-10-03"
    )
    review = biosamples.build_review(biosamples.repeated_target_groups(rows), samples, metadata)
    path = tmp_path / "review.json"
    path.write_text(json.dumps(review))
    return inventory, path


def convert(row):
    return seed.ncbi_ast_activity_observation(row)


def test_two_distinct_assays_stay_separate_and_each_keeps_both_genomes(tmp_path):
    first, second = pair(mic_value="1"), pair(mic_value="2", platform="", reagent="E-Test")
    rows = first + second
    original = copy.deepcopy(rows)
    inventory, path = review_file(tmp_path, rows, sample([first[0], second[0]]))
    observations = [obs for _, obs in biosamples.activity_observations(rows, inventory, convert, path)]
    assert rows == original
    assert len(observations) == 2
    assert {obs["mic_value"] for obs in observations} == {1.0, 2.0}
    assert len({obs["source_observation_id"] for obs in observations}) == 2
    assert all(obs["measurement_count"] == 1 and obs["source_export_row_count"] == 2 for obs in observations)
    for obs in observations:
        assert not (set(biosamples.CONTEXT_FIELDS.values()) & set(obs))
        assert {
            (
                c["pathogen_detection_target_accession"],
                c["assembly_accession"],
                c["bioproject_accession"],
                c["source_create_date"],
            )
            for c in obs["pathogen_detection_contexts"]
        } == {(f"PDT00000000{i}.1", f"GCA_00000000{i}.1", f"PRJNA{i}", f"2026-01-0{i}") for i in (1, 2)}
        assert any("biosample-review-sha256:" in e["notes"] for e in obs["evidence"])
        assert obs["source"] == "NCBI_AST"
    repeated = [obs for _, obs in biosamples.activity_observations(rows, inventory, convert, path)]
    assert observations == repeated


def test_unrepeated_rows_are_unchanged_and_do_not_require_a_review(tmp_path):
    rows = pair()[:1]
    assert list(biosamples.activity_observations(rows, tmp_path / "unused", convert)) == [
        (rows[0]["identifier"], convert(rows[0])),
    ]


def test_seeder_requires_fanout_review_before_mutating_records(tmp_path, monkeypatch):
    rows = pair()
    inventory, path = review_file(tmp_path, rows, sample([rows[0]]))
    monkeypatch.setattr(seed, "NCBI_AST_ACTIVITY_INVENTORY", inventory)
    monkeypatch.setattr(seed, "read_assay_review", lambda _: None)
    monkeypatch.setattr(
        seed,
        "ncbi_ast_observations",
        lambda rows, inventory, convert: biosamples.activity_observations(rows, inventory, convert, path),
    )
    identifier = rows[0]["identifier"]
    records = {
        identifier: {
            "identifier": identifier,
            "chemical_structure": {
                "standard_inchi_key": rows[0]["standard_inchi_key"],
            },
            "curation_history": [],
        }
    }
    before = copy.deepcopy(records)
    review = json.loads(path.read_text())
    changed = {**review, "biosample_sha256": "invalid"}
    path.write_text(json.dumps(changed))
    with pytest.raises(ValueError, match="snapshot checksum"):
        seed.attach_ncbi_ast_activity(records)
    assert records == before
    path.write_text(json.dumps(review))
    counts = seed.attach_ncbi_ast_activity(records)
    assert counts["matched_observations"] == 1
    observation = records[identifier]["activity_spectrum"][0]
    assert observation["measurement_count"] == 1
    assert len(observation["pathogen_detection_contexts"]) == 2


@pytest.mark.parametrize(
    "field,value",
    [
        ("Measurement", "9"),
        ("Measurement", "NaN"),
        ("Measurement", "2/4"),
        ("Measurement sign", ">"),
        ("Measurement units", "ug/L"),
        ("Antibiotic", "another drug"),
        ("Vendor", "other vendor"),
        ("Laboratory typing platform", "other platform"),
        ("Resistance phenotype", "susceptible"),
        ("Testing standard", "EUCAST"),
        ("Laboratory typing method", "disk diffusion"),
    ],
)
def test_measurement_or_context_disagreement_never_matches(field, value):
    row = pair()[0]
    result = submitted(row)
    result[field] = value
    assert not biosamples.matches_result(row, result)


def test_equal_signs_and_missing_standard_match_without_rewriting_measurements():
    row = pair(mic_qualifier="", standard="")[0]
    result = submitted(row)
    assert result["Measurement sign"] == "=="
    assert result["Testing standard"] == "missing"
    assert biosamples.matches_result(row, result)
    assert row["mic_qualifier"] == "" and row["standard"] == ""


def test_disk_result_remains_a_diameter_not_a_mic():
    row = ncbi_ast_row(mic_value="", mic_qualifier="", mic_units="", disk_diffusion_value="18",
                      disk_diffusion_qualifier=">=", disk_diffusion_units="mm", method="disk diffusion")
    result = submitted(row)
    result.update({"Measurement": "18", "Measurement sign": ">=", "Measurement units": "mm",
                   "Laboratory typing method": "disk diffusion"})
    assert biosamples.matches_result(row, result)
    result["Measurement units"] = "mg/L"
    assert not biosamples.matches_result(row, result)


def test_zero_or_multiple_matching_source_rows_require_review(tmp_path):
    rows = pair()
    empty = sample([rows[0]])
    empty[rows[0]["biosample_accession"]]["rows"] = []
    for samples in (empty, sample([rows[0], rows[0]])):
        with pytest.raises(ValueError, match="one submitted result"):
            review_file(tmp_path, rows, samples)


@pytest.mark.parametrize("updated", ["2026-09-26T00:00:00", "2026-10-03T00:00:00"])
def test_post_snapshot_or_same_day_biosample_edits_cannot_prove_original_assay_count(tmp_path, updated):
    rows = pair()
    samples = sample([rows[0]])
    samples[rows[0]["biosample_accession"]]["last_update"] = updated
    with pytest.raises(ValueError, match="predate"):
        review_file(tmp_path, rows, samples)


def test_sample_taxonomy_must_agree(tmp_path):
    rows = pair()
    samples = sample([rows[0]])
    samples[rows[0]["biosample_accession"]]["taxon_id"] = "NCBITaxon:1280"
    with pytest.raises(ValueError, match="taxonomy conflicts"):
        review_file(tmp_path, rows, samples)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda r: r.update(activity_report_sha256="0" * 64),
        lambda r: r.update(biosample_sha256="bad"),
        lambda r: r.update(reviewed_on="2026-02-30"),
        lambda r: r.update(source_version="changed"),
        lambda r: r["groups"].clear(),
        lambda r: r["groups"].append(copy.deepcopy(r["groups"][0])),
        lambda r: r["groups"][0].update(antibiogram_row_number=True),
        lambda r: r["groups"][0].update(biosample_accession="SAMN1"),
        lambda r: r["groups"][0]["antibiogram_row"].update(Measurement="999"),
    ],
)
def test_review_drift_is_rejected_before_any_collapsed_observation(tmp_path, mutate):
    rows = pair()
    inventory, path = review_file(tmp_path, rows, sample([rows[0]]))
    review = json.loads(path.read_text())
    mutate(review)
    path.write_text(json.dumps(review))
    with pytest.raises(ValueError):
        list(biosamples.activity_observations(rows, inventory, convert, path))


def xml_payload(rows):
    root = ET.Element("BioSampleSet")
    record = ET.SubElement(
        root,
        "BioSample",
        accession=rows[0]["biosample_accession"],
        access="public",
        last_update="2026-01-01T12:34:56",
    )
    primary = ET.SubElement(ET.SubElement(record, "Ids"), "Id", db="BioSample", is_primary="1")
    primary.text = rows[0]["biosample_accession"]
    description = ET.SubElement(record, "Description")
    ET.SubElement(description, "Organism", taxonomy_id="562", taxonomy_name="Escherichia coli")
    table = ET.SubElement(ET.SubElement(description, "Comment"), "Table", {"class": "Antibiogram.1.0"})
    header = ET.SubElement(table, "Header")
    for name in biosamples.HEADERS:
        ET.SubElement(header, "Cell").text = name
    body = ET.SubElement(table, "Body")
    for row in rows:
        entry = ET.SubElement(body, "Row")
        for value in submitted(row).values():
            ET.SubElement(entry, "Cell").text = value
    ET.SubElement(record, "Status", status="live")
    return root


def test_fetch_requires_complete_source_evidence_and_never_overwrites(tmp_path, monkeypatch):
    rows = pair()
    inventory = tmp_path / "activity.tsv"
    write_activity_report(inventory, rows)
    payload = ET.tostring(xml_payload([rows[0]]))
    monkeypatch.setattr(biosamples, "urlopen", lambda *a, **kw: io.BytesIO(payload))
    output = tmp_path / "snapshot"
    review = biosamples.fetch_review(inventory, output)
    assert len(review["groups"]) == 1
    assert (output / "biosamples.xml").read_bytes() == payload
    assert verify_source_review(output, inventory, rows, output / "review.json") == review
    manifest_path = output / "snapshot.json"
    original_manifest = manifest_path.read_text()
    manifest = json.loads(original_manifest)
    manifest["sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="manifest"):
        verify_source_review(output, inventory, rows, output / "review.json")
    manifest_path.write_text(original_manifest)
    with pytest.raises(ValueError, match="already exists"):
        biosamples.fetch_review(inventory, output)
    monkeypatch.setattr(biosamples, "urlopen", lambda *a, **kw: io.BytesIO(b"<BioSampleSet/>"))
    with pytest.raises(ValueError, match="exact requested accessions"):
        biosamples.fetch_review(inventory, tmp_path / "partial")
    assert not (tmp_path / "partial").exists()


@pytest.mark.parametrize(
    "mutation",
    [
        lambda root: root[0].set("access", "private"),
        lambda root: root[0].remove(root[0].find("Status")),
        lambda root: root[0].find("Ids/Id").set("is_primary", "0"),
        lambda root: root.append(copy.deepcopy(root[0])),
        lambda root: (
            root[0]
            .find("Description/Comment/Table/Header")
            .remove(root[0].find("Description/Comment/Table/Header/Cell"))
        ),
        lambda root: (
            root[0]
            .find("Description/Comment/Table/Body/Row")
            .remove(root[0].find("Description/Comment/Table/Body/Row/Cell"))
        ),
    ],
)
def test_malformed_or_incomplete_biosamples_are_rejected(mutation):
    rows = pair()
    root = xml_payload([rows[0]])
    mutation(root)
    with pytest.raises(ValueError):
        biosamples.read_biosamples(ET.tostring(root), [rows[0]["biosample_accession"]])


@pytest.fixture(scope="module")
def validator():
    return Validator(
        schema=str(Path(__file__).resolve().parents[1] / "src/antibioticmech/schema/antibioticmech.yaml"),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_collapsed_schema_requires_paired_context_without_singleton_selection(tmp_path, validator):
    rows = pair()
    inventory, path = review_file(tmp_path, rows, sample([rows[0]]))
    observation = list(biosamples.activity_observations(rows, inventory, convert, path))[0][1]
    assert not list(validator.iter_results(observation, target_class="ActivityObservation"))
    for field, value in (
        ("assembly_accession", "GCA_000000009.1"),
        ("source_export_row_count", 0),
        ("bioproject_accession", "PRJNA9"),
        ("pathogen_detection_target_accession", "PDT000000009.1"),
        ("sra_accessions", ["SRR9"]),
        ("source_create_date", "2026-01-01"),
    ):
        assert list(validator.iter_results({**observation, field: value}, target_class="ActivityObservation"))
    invalid = copy.deepcopy(observation)
    invalid["pathogen_detection_contexts"][0]["assembly_accession"] = "PDT000000001.1"
    assert list(validator.iter_results(invalid, target_class="ActivityObservation"))
    for contexts in ([], observation["pathogen_detection_contexts"][:1]):
        invalid = {**observation, "pathogen_detection_contexts": contexts}
        assert list(validator.iter_results(invalid, target_class="ActivityObservation"))

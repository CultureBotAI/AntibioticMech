"""Keep conditional gene evidence separate from conflicted archive identifiers."""

import copy
import csv
import io
import json
import sys
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_yeast_regulator_context as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())


def test_historical_census_does_not_freeze_live_records(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    rows = list(csv.DictReader(io.StringIO(
        audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()), delimiter="\t"))
    assert len(rows) == 2939
    assert {r["identifier"] for r in dossier["records"]} == set(audit.TARGETS)
    for item in dossier["records"]:
        row, = [r for r in rows if r["identifier"] == item["identifier"]]
        assert item["path"] == row["path"] and item["sha256"] == row["record_sha256"]
        assert item["standard_inchi_key"] == audit.TARGETS[item["identifier"]]
        assert not item["assertions_added"] and item["whole_record_review"] == "OPEN"


@pytest.mark.parametrize("gene,accession,version,seq,locus,sgd", [
    ("MOT3", "P54785", 192, 1, "YMR070W", "S000004674"),
    ("PDR1", "P12383", 208, 2, "YGL013C", "S000002981"),
])
def test_versioned_reference_identity_only(dossier, gene, accession, version, seq, locus, sgd):
    protein = dossier["reference_proteins"][gene]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["entry_version"] == version and protein["sequence_version"] == seq
    assert protein["ordered_locus_names"] == [locus] and protein["sgd_id"] == sgd
    assert protein["reference_taxon_id"] == "NCBITaxon:559292"
    assert protein["source_species_taxon_id"] == "NCBITaxon:4932"
    assert protein["reference_taxon_rank"] == "strain" and protein["species_lineage_verified"]
    assert not protein["experimental_subject_assignment"] and not protein["exact_resistance_allele"]
    assert protein["reuse_scope"] == "REFERENCE_IDENTITY_ONLY_NOT_A_TRANSFERRED_PHENOTYPE"
    assert not protein["focal_paper_in_bibliography"]


@pytest.mark.parametrize("gene", ["MOT3", "PDR1"])
@pytest.mark.parametrize("change", ["none", "gene", "taxon", "unreviewed", "sequence", "features"])
def test_reference_projection_rejects_conflation(gene, change):
    entry = {"primaryAccession": "P12345", "entryType": "UniProtKB reviewed (Swiss-Prot)",
             "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
             "genes": [{"geneName": {"value": gene}}],
             "organism": {"taxonId": 559292, "scientificName": "Reference strain"},
             "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000001234"}],
             "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}}}
    taxonomy = {"taxonId": 559292, "rank": "strain", "active": True, "scientificName": "Reference strain",
                "lineage": [{"taxonId": 4932, "rank": "species"}]}
    if change == "gene":
        entry["genes"][0] = {"geneName": {"value": "OTHER"}, "synonyms": [{"value": gene}]}
    elif change == "taxon":
        entry["organism"]["taxonId"] = 1
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change != "none":
        entry[change] = []
    if change == "none":
        assert not audit.project_protein(entry, gene, taxonomy)["experimental_subject_assignment"]
    else:
        with pytest.raises(ValueError):
            audit.project_protein(entry, gene, taxonomy)


@pytest.mark.parametrize("change", ["none", "duplicate", "lab_id", "species", "membership", "header"])
def test_source_table_joins_are_explicit(change):
    strains = [["Strain name", "Strain number", "Species", "Genotype", "Source"]]
    strains.extend([label, number, "S. cerevisiae", "NOT_FOR_EXPORT", "This study"]
                   for label, (number, _) in audit.SUBJECTS.items())
    coverage = [["Strain", "Mean Coverage"]]
    coverage.extend([label, "NOT_FOR_EXPORT"] for label in [*audit.SUBJECTS, *map(str, range(6))])
    if change == "duplicate":
        strains.append(strains[1])
    elif change == "lab_id":
        strains[1][1] = "DIFFERENT"
    elif change == "species":
        strains[1][2] = "Other organism"
    elif change == "membership":
        coverage[1][0] = "OTHER"
    elif change == "header":
        strains[0] = coverage[0]
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_subjects(strains, coverage)
        return
    result = audit.project_subjects(strains, coverage)
    assert "NOT_FOR_EXPORT" not in json.dumps(result)
    for subject in result.values():
        assert subject["listed_in_table_s1_wgs_coverage"]
        assert not subject["exact_experimental_protein_assigned"] and not subject["strain_taxon_id_assigned"]


@pytest.fixture
def archive():
    rows, experiments = [], {}
    for number, (accession, alias) in enumerate(audit.EXPERIMENTS.items()):
        row = dict.fromkeys(audit.ENA_FIELDS.split(","), "")
        row.update({"run_accession": f"SRR{number + 100000}", "experiment_accession": accession,
                    "study_accession": audit.STUDY, "secondary_study_accession": audit.SECONDARY_STUDY,
                    "submission_accession": audit.SUBMISSION, "sample_accession": audit.SAMPLE,
                    "secondary_sample_accession": audit.SECONDARY_SAMPLE, "tax_id": "559292",
                    "sample_alias": "Sc erg3 (ScLC10)", "scientific_name": "Saccharomyces cerevisiae S288C"})
        rows.append(row)
        experiments[accession] = f"""<EXPERIMENT_SET><EXPERIMENT accession="{accession}" alias="{alias}">
          <TITLE>S. cerevisiae strain ScLC1367</TITLE><STUDY_REF accession="SRP018095"><IDENTIFIERS>
          <EXTERNAL_ID namespace="BioProject">PRJNA186947</EXTERNAL_ID></IDENTIFIERS></STUDY_REF>
          <DESIGN><SAMPLE_DESCRIPTOR accession="SRS387829"><IDENTIFIERS>
          <EXTERNAL_ID namespace="BioSample">SAMN01893852</EXTERNAL_ID></IDENTIFIERS>
          </SAMPLE_DESCRIPTOR></DESIGN></EXPERIMENT></EXPERIMENT_SET>"""
    sample = """<SAMPLE_SET><SAMPLE accession="SAMN01893852" alias="Sc erg3 (ScLC10)">
      <IDENTIFIERS><PRIMARY_ID>SAMN01893852</PRIMARY_ID><SECONDARY_ID>SRS387829</SECONDARY_ID></IDENTIFIERS>
      <SAMPLE_NAME><TAXON_ID>559292</TAXON_ID>
      <SCIENTIFIC_NAME>Saccharomyces cerevisiae S288C</SCIENTIFIC_NAME>
      </SAMPLE_NAME><SAMPLE_ATTRIBUTES><SAMPLE_ATTRIBUTE><TAG>isolate</TAG><VALUE>ScLC10</VALUE>
      </SAMPLE_ATTRIBUTE></SAMPLE_ATTRIBUTES></SAMPLE></SAMPLE_SET>"""
    return rows, experiments, sample


def test_archive_conflict_survives_matching_titles(archive, dossier):
    projected = audit.project_archive(*archive)
    assert projected["subject_experiment_matches"] == {"Sc-F-1": sorted(audit.EXPERIMENTS), "Sc-G-13": []}
    assert not projected["conflict_resolved"] and not projected["genomes_absent_everywhere_inferred"]
    assert projected["shared_sample_provenance"]["source_isolate_label"] == "ScLC10"
    for experiment in projected["experiments"]:
        assert experiment["source_laboratory_id"] == "ScLC1367"
        assert experiment["linked_sample_label_conflict"]
        assert not experiment["unqualified_sample_or_genome_assignment"]
        assert not experiment["independent_biological_replicate_inferred"]
    actual = dossier["archive_context"]
    assert (actual["unique_runs"], actual["unique_experiments"], actual["unique_samples"]) == (11, 2, 1)
    assert [len(e["run_accessions"]) for e in actual["experiments"]] == [6, 5]
    assert actual["sc_g_13_gap_scope"] == "INSPECTED_STUDY_AND_EXPERIMENT_METADATA_ONLY"


@pytest.mark.parametrize("change", ["duplicate", "sample", "study", "extra", "experiment", "title",
                                   "alias", "xml_sample", "xml_study", "isolate", "sample_taxon"])
def test_archive_joins_fail_closed(archive, change):
    rows, experiments, sample = copy.deepcopy(archive)
    key = next(iter(experiments))
    if change == "duplicate":
        rows.append(rows[0])
    elif change in {"sample", "study", "experiment"}:
        rows[0][change + "_accession"] = "OTHER"
    elif change == "extra":
        rows[0]["sequence"] = "NOT_FOR_EXPORT"
    elif change == "title":
        experiments[key] = experiments[key].replace("strain ScLC1367", "strain ScLC1540")
    elif change == "alias":
        experiments[key] = experiments[key].replace('alias="ScLC1367"', 'alias="OTHER"')
    elif change == "xml_sample":
        experiments[key] = experiments[key].replace("SAMN01893852", "SAMN00000001")
    elif change == "xml_study":
        experiments[key] = experiments[key].replace("PRJNA186947", "PRJNA000001")
    elif change == "isolate":
        sample = sample.replace("<VALUE>ScLC10</VALUE>", "<VALUE>ScLC1367</VALUE>")
    else:
        sample = sample.replace("559292", "4932")
    with pytest.raises(ValueError):
        audit.project_archive(rows, experiments, sample)


@pytest.mark.parametrize("change", ["none", "path", "receipt", "hash", "unreviewed", "truthy"])
def test_canary_binds_request_not_just_identical_body(tmp_path, change):
    for key in ("first", "second"):
        (tmp_path / f"{key}-response.bin").write_bytes(b"identical")
        (tmp_path / f"{key}-receipt.json").write_text(json.dumps({"request": key}))
    marker = {"manually_reviewed": True,
              "response": audit.reference.pin(tmp_path, tmp_path / "first-response.bin"),
              "receipt": audit.reference.pin(tmp_path, tmp_path / "first-receipt.json")}
    if change == "path":
        marker["response"] = audit.reference.pin(tmp_path, tmp_path / "second-response.bin")
    elif change == "receipt":
        marker["receipt"] = audit.reference.pin(tmp_path, tmp_path / "second-receipt.json")
    elif change == "hash":
        marker["response"]["sha256"] = "0" * 64
    elif change in {"unreviewed", "truthy"}:
        marker["manually_reviewed"] = 1 if change == "truthy" else False
    if change == "none":
        audit.bind_canary(tmp_path, tmp_path, marker, "first")
    else:
        with pytest.raises(ValueError):
            audit.bind_canary(tmp_path, tmp_path, marker, "first")


@pytest.mark.parametrize("change", ["none", "host", "endpoint", "limit", "fragment", "status",
                                   "retry", "hash", "bytes"])
def test_ena_response_identity(tmp_path, change):
    path = tmp_path / "runs-response.bin"
    path.write_bytes(b"[]")
    params = {"result": ["read_run"], "limit": ["0"]}
    receipt = {"url": "https://www.ebi.ac.uk/ena/portal/api/search?" + urlencode(params, doseq=True),
               "status": 200, "retry_performed": False, "sha256": audit.reference.digest(path),
               "bytes": 2, "retrieved_at": "2026-10-13T00:00:00Z"}
    if change == "host":
        receipt["url"] = receipt["url"].replace("www.ebi.ac.uk", "example.org")
    elif change == "endpoint":
        receipt["url"] = receipt["url"].replace("/search?", "/other?")
    elif change == "limit":
        receipt["url"] = receipt["url"].replace("limit=0", "limit=1")
    elif change == "fragment":
        receipt["url"] += "#other"
    elif change == "status":
        receipt["status"] = 403
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "bytes":
        receipt["bytes"] = 3
    (tmp_path / "runs-receipt.json").write_text(json.dumps(receipt))
    if change == "none":
        assert audit.read_ena(tmp_path, tmp_path, "runs", "/ena/portal/api/search", params)[0] == b"[]"
    else:
        with pytest.raises(ValueError):
            audit.read_ena(tmp_path, tmp_path, "runs", "/ena/portal/api/search", params)


@pytest.fixture
def query_plan(tmp_path):
    definitions = [{"columnId": field, "description": field, "type": "text"}
                   for field in sorted(audit.ENA_FIELDS.split(","))]
    for key in ("search", "return"):
        with (tmp_path / f"ena-{key}-fields-response.bin").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["columnId", "description", "type"], delimiter="\t")
            writer.writeheader()
            writer.writerows(definitions)
        (tmp_path / f"ena-{key}-fields-receipt.json").write_text("{}")
    marker = {"manually_reviewed": True,
              "response": audit.reference.pin(tmp_path, tmp_path / "ena-search-fields-response.bin"),
              "receipt": audit.reference.pin(tmp_path, tmp_path / "ena-search-fields-receipt.json")}
    marker_path = tmp_path / "ena-search-fields-reviewed.json"
    marker_path.write_text(json.dumps(marker))
    return {"url": "https://www.ebi.ac.uk/ena/portal/api/search", "query": 'study_accession="PRJNA186947"',
            "fields": audit.ENA_FIELDS, "result": "read_run", "format": "json",
            "canary_limit": "1", "full_limit": "0", "max_response_bytes": 2_000_000,
            "manually_reviewed": True, "sequence_or_assay_values_requested": False,
            "search_fields_canary": audit.reference.pin(tmp_path, marker_path),
            "return_fields_response": audit.reference.pin(
                tmp_path, tmp_path / "ena-return-fields-response.bin"),
            "return_fields_receipt": audit.reference.pin(
                tmp_path, tmp_path / "ena-return-fields-receipt.json"),
            "selected_field_definitions": definitions,
            "scope": "FOLLOW_EXPLICIT_STUDY_LINK_NOT_SUBMISSION_EQUIVALENCE",
            "source_submission_response": {"path": "submission", "sha256": "a" * 64},
            "source_submission_receipt": {"path": "receipt", "sha256": "b" * 64}}


@pytest.mark.parametrize("field", [None, "url", "query", "fields", "result", "format", "canary_limit",
                                   "full_limit", "max_response_bytes", "manually_reviewed",
                                   "sequence_or_assay_values_requested", "search_fields_canary",
                                   "return_fields_response", "return_fields_receipt",
                                   "selected_field_definitions", "scope", "source_submission_response",
                                   "source_submission_receipt"])
def test_plan_provenance_is_validated(tmp_path, query_plan, field):
    plan = copy.deepcopy(query_plan)
    submission = {k: plan["source_submission_" + k] for k in ("response", "receipt")}
    if field is not None:
        plan[field] = None
        with pytest.raises(ValueError):
            audit.validate_ena_plan(tmp_path, tmp_path, plan, query_plan["query"], submission)
    else:
        audit.validate_ena_plan(tmp_path, tmp_path, plan, query_plan["query"], submission)


def test_conditional_findings_and_public_scope(dossier):
    findings = {f["gene"]: f for f in dossier["conditional_findings"]}
    assert "NOT_DIRECT_TEST_OF_EXACT_ALLELE" in findings["MOT3"]["tacrolimus_plus_fluconazole"]
    assert findings["PDR1"]["radicicol_or_tacrolimus_plus_fluconazole"] == (
        "NO_INCREASED_CROSS_RESISTANCE_REPORTED")
    assert "EXPRESSION_CONTEXT_CAVEAT" in findings["PDR1"]["geldanamycin_plus_fluconazole"]
    assert "NOT_DIRECTLY_MEASURED" in findings["PDR1"]["pdr5_efflux_route"]
    assert "HOLD_UNCONDITIONAL" in dossier["curation_decision"]
    assert not dossier["primary"]["whole_article_review_complete"]
    assert "crowded" in dossier["primary"]["source_layout_limit"]
    assert not urlsplit(dossier["primary"]["figure6"]["final_url_without_query"]).query
    assert len(dossier["archive_context"]["requests"]) == 9
    assert dossier["summary"]["corpus_records_in_scope"] == 2939
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert not any(v for k, v in dossier["constraints"].items() if k != "issue_1040")
    for key in ("biological_records_changed", "assembly_accessions_assigned", "experimental_alleles_assigned",
                "whole_records_completed", "new_taxonomy_queries"):
        assert dossier["summary"][key] == 0
    serialized = json.dumps(dossier).lower()
    for forbidden in ("x-goog-signature", "x-goog-credential", '"sequence":', '"alteration":',
                      '"construct":', '"protocol":', '"mic_value":'):
        assert forbidden not in serialized

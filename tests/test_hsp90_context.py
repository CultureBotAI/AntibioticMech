"""Conditional resistance and reference metadata must not become single-agent claims."""

import copy
import csv
import io
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_hsp90_context as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())


def test_historical_scope_does_not_freeze_live_records(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    source = audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()
    rows = list(csv.DictReader(io.StringIO(source), delimiter="\t"))
    assert len(rows) == 2939
    assert {r["identifier"] for r in dossier["records"]} == set(audit.TARGETS)
    for item in dossier["records"]:
        row, = [r for r in rows if r["identifier"] == item["identifier"]]
        assert item["sha256"] == row["record_sha256"] and item["path"] == row["path"]
        assert item["standard_inchi_key"] == audit.TARGETS[item["identifier"]]
        assert not item["assertions_added"] and item["whole_record_review"] == "OPEN"


@pytest.mark.parametrize("key,accession,version,seq,locus", [
    ("hsc82", "P15108", 236, 4, "YMR186W"),
    ("hsp82", "P02829", 255, 1, "YPL240C"),
    ("ca-hsp90", "P46598", 149, 1, "CAALFM_C702030WA"),
])
def test_versioned_references_remain_separate(dossier, key, accession, version, seq, locus):
    protein = dossier["reference_proteins"][key]
    gene, taxid, species = audit.REFERENCES[key]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["primary_gene_name"] == gene and protein["ordered_locus_names"] == [locus]
    assert protein["entry_version"] == version and protein["sequence_version"] == seq
    assert protein["reference_taxon_id"] == f"NCBITaxon:{taxid}"
    assert protein["source_species_taxon_id"] == f"NCBITaxon:{species}"
    assert protein["reference_taxon_rank"] == "strain" and protein["species_lineage_verified"]
    assert not protein["experimental_subject_assignment"] and not protein["exact_resistance_allele"]
    assert not protein["single_drug_resistance_established"] and not protein["focal_paper_in_bibliography"]
    request = dossier["uniprot_requests"][key]
    assert request["release"] == "2026_03" and request["results"] == 1
    assert request["complete_for_query"] and not request["all_strains_and_unreviewed_entries_searched"]
    assert parse_qs(urlsplit(request["url"]).query)["query"] == [audit.QUERIES[key]]
    if key == "hsp82":
        assert protein["role"] == "ISOFORM_HYPOTHESIS_ONLY"
        assert "NOT_EXPERIMENTALLY_ESTABLISHED" in dossier["hsp82_disposition"]


@pytest.mark.parametrize("key", audit.REFERENCES)
@pytest.mark.parametrize("change", ["none", "gene", "taxon", "unreviewed", "sequence", "features"])
def test_reference_projection_rejects_conflation(key, change):
    gene, taxid, species = audit.REFERENCES[key]
    entry = {"primaryAccession": "P12345", "entryType": "UniProtKB reviewed (Swiss-Prot)",
             "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
             "genes": [{"geneName": {"value": gene}}],
             "organism": {"taxonId": taxid, "scientificName": "Reference strain"},
             "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}}}
    taxonomy = {"taxonId": taxid, "rank": "strain", "active": True, "scientificName": "Reference strain",
                "lineage": [{"taxonId": species, "rank": "species"}]}
    if change == "gene":
        entry["genes"][0] = {"geneName": {"value": "OTHER"}, "synonyms": [{"value": gene}]}
    elif change == "taxon":
        entry["organism"]["taxonId"] = 1
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change != "none":
        entry[change] = []
    if change == "none":
        assert not audit.project_protein(entry, key, taxonomy)["experimental_subject_assignment"]
    else:
        with pytest.raises(ValueError):
            audit.project_protein(entry, key, taxonomy)


@pytest.fixture
def tables(dossier):
    strains = [["Strain name", "Strain number", "Species", "Genotype", "Source"]]
    strains.extend([label, number, species, "NOT_FOR_EXPORT", "This study"]
                   for label, (number, species, _) in audit.SUBJECTS.items())
    coverage = [["Strain", "Mean Coverage"]]
    coverage.extend([label, "NOT_FOR_EXPORT"] for label in dossier["genome_context"]["table_s1_wgs_lineages"])
    return strains, coverage


def test_source_subjects_are_not_assembly_or_reference_strain_assignments(dossier, tables):
    projected, _ = audit.project_subjects(*tables)
    assert set(projected) == set(dossier["subjects"]) == set(audit.SUBJECTS)
    assert "NOT_FOR_EXPORT" not in json.dumps(projected)
    for label, subject in dossier["subjects"].items():
        assert subject["source_laboratory_id"] == audit.SUBJECTS[label][0]
        for key in ("listed_in_table_s1_wgs_coverage", "strain_taxon_id_assigned",
                    "exact_experimental_protein_assigned", "sample_or_genome_accession_assigned"):
            assert not subject[key]
    genome = dossier["genome_context"]
    assert genome["source_archive_accession"] == "SRA065341"
    assert genome["archive_role"] == "SOURCE_REPORTED_SEQUENCE_ARCHIVE_ONLY"
    assert not genome["reference_assembly_labels_are_experimental_accessions"]
    assert not genome["no_genome_anywhere_inferred"] and not genome["archive_endpoint_requested"]


@pytest.mark.parametrize("change", ["duplicate", "number", "species", "coverage", "header"])
def test_table_joins_fail_closed(tables, change):
    strains, coverage = copy.deepcopy(tables)
    if change == "duplicate":
        strains.append(strains[1])
    elif change == "number":
        strains[1][1] = "DIFFERENT"
    elif change == "species":
        strains[1][2] = "Other organism"
    elif change == "coverage":
        coverage[1][0] = strains[1][0]
    else:
        strains[0] = coverage[0]
    with pytest.raises(ValueError):
        audit.project_subjects(strains, coverage)


def test_conditional_and_negative_results_not_promoted(dossier):
    findings = {f["lineage"]: f for f in dossier["conditional_findings"]}
    assert set(findings) == set(audit.SUBJECTS)
    for label in ("Sc-G-12", "Sc-G-14"):
        assert findings[label]["gene"] == "HSC82"
        assert findings[label]["radicicol_plus_fluconazole"] == (
            "LINEAGE_CROSS_RESISTANCE_NOT_INDEPENDENT_ALLELE_TEST")
    assert findings["Sc-G-12"]["geldanamycin_plus_fluconazole"] == "FUNCTIONAL_PHENOCOPY_SUPPORT"
    assert findings["Ca-G-10"]["radicicol_plus_fluconazole"] == (
        "NO_INCREASED_CROSS_RESISTANCE_REPORTED_IN_TESTED_CONTEXT")
    assay = dossier["assay_scope"]
    assert assay["curation_decision"] == "HOLD_UNCONDITIONAL_SINGLE_DRUG_ASSERTIONS"
    assert "fluconazole" in assay["source_method"]
    assert not assay["quantitative_mic_imported"] and not assay["clinical_category_assigned"]


def test_invalid_query_and_source_holds_are_not_negative_evidence(dossier):
    error = dossier["query_validation_error"]
    assert error["status"] == 400
    assert error["reason"] == "QUERY_VALIDATION_ERROR_INVALID_SEARCH_FIELD_NOT_ACCESS_DENIAL_OR_ZERO_RESULTS"
    assert error["planned_2011_publication_query"] == "NOT_RUN_SAME_INVALID_FIELD"
    assert not error["protein_absence_inferred"] and not error["invalid_query_repaired_or_reissued"]
    leads = dossier["remaining_primary_leads"]
    assert not leads[0]["primary_results_reviewed"] and not leads[0]["retry_or_alternate_full_text_route"]
    assert [p["primary_request_status"] for p in leads[1:]] == ["NOT_REQUESTED", "NOT_REQUESTED"]


def test_primary_scope_and_public_payload(dossier):
    assets = dossier["primary"]["assets"]
    assert set(assets) == {"article", *audit.ASSETS}
    for key, asset in assets.items():
        assert urlsplit(asset["source_url"]).hostname == "journals.plos.org"
        assert not urlsplit(asset["final_url_without_query"]).query
        assert asset["validated_redirects"] == int(key != "article")
    manual = dossier["primary"]["manual_review"]
    assert manual["table_s1_is_coverage_not_strain_catalog"]
    assert not manual["whole_article_review_complete"]
    assert [len(r["pages"]) for r in dossier["primary"]["renders"].values()] == [1, 4]
    assert "crowded" in manual["source_layout_limit"]
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    for key, value in dossier["constraints"].items():
        if key != "issue_1040":
            assert not value
    summary = dossier["summary"]
    assert summary["corpus_records_in_scope"] == 2939
    for key in ("biological_records_changed", "experimental_alleles_assigned",
                "genome_accessions_assigned", "whole_records_completed", "new_taxonomy_requests"):
        assert summary[key] == 0
    serialized = json.dumps(dossier).lower()
    for forbidden in ("x-goog-signature", "x-goog-credential", '"sequence":', '"alteration":',
                      '"construct":', '"protocol":', '"mic_value":'):
        assert forbidden not in serialized

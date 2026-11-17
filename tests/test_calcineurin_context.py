"""Reference aliases and conditional panels must not become exact resistance alleles."""

import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_calcineurin_context as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())


def test_historical_census_without_live_record_freeze(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    rows = list(csv.DictReader(io.StringIO(
        audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()), delimiter="\t"))
    assert len(rows) == 2939
    assert {r["identifier"] for r in dossier["records"]} == set(audit.TARGETS)
    for record in dossier["records"]:
        row, = [r for r in rows if r["identifier"] == record["identifier"]]
        assert record["path"] == row["path"] and record["sha256"] == row["record_sha256"]
        assert record["standard_inchi_key"] == audit.TARGETS[record["identifier"]]
        assert not record["assertions_added"] and not record["existing_claims_newly_confirmed"]
        assert not record["tested_preparation_independently_reidentified"]
        assert record["whole_record_review"] == "OPEN"


@pytest.mark.parametrize("key,accession,version,seq,rank,taxid", [
    ("fpr1", "P20081", 220, 2, "reviewed", 559292),
    ("cnb1", "P25296", 211, 3, "reviewed", 559292),
    ("cna1", "A0A1D8PCA8", 44, 1, "unreviewed", 237561),
    ("lcb1", "Q5A325", 121, 1, "unreviewed", 237561),
])
def test_versioned_proteins_are_reference_only(dossier, key, accession, version, seq, rank, taxid):
    protein = dossier["reference_proteins"][key]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["entry_version"] == version and protein["sequence_version"] == seq
    assert protein["entry_type"].startswith("UniProtKB " + rank + " ")
    assert protein["reference_taxon_id"] == f"NCBITaxon:{taxid}"
    assert protein["reference_taxon_rank"] == "strain" and protein["species_lineage_verified"]
    assert not protein["experimental_subject_assignment"] and not protein["exact_resistance_allele"]
    assert not protein["focal_paper_in_bibliography"]
    if key == "lcb1":
        assert protein["primary_gene_name"] is None
        assert protein["ordered_locus_names"] == ["CAALFM_CR08640CA", "orf19.13796"]
    if rank == "unreviewed":
        assert not protein["reviewed_function_inferred"] and not protein["experimental_haplotype_assigned"]


@pytest.fixture
def cgd_wrapper(dossier):
    stream = io.StringIO()
    stream.write(f"! Genome version: {audit.CGD_VERSION}\n")
    writer = csv.writer(stream, delimiter="\t")
    for feature in dossier["cgd_reference_features"].values():
        row = [""] * 19
        row[0:4] = [feature["feature"], feature["primary_gene_name"] or "",
                    "|".join(feature["aliases"]), feature["feature_type"]]
        row[8], row[10] = feature["cgd_id"], "SYNTHETIC_DESCRIPTION_NOT_EXPORTED"
        writer.writerow(row)
    body = stream.getvalue()
    return {"body": body, "status": 200, "url": audit.CGD_URL,
            "sha256": hashlib.sha256(body.encode()).hexdigest()}


@pytest.mark.parametrize("change", ["none", "hash", "url", "version", "duplicate", "alias", "gene"])
def test_cgd_alias_ambiguity_and_provenance(cgd_wrapper, change):
    wrapper = copy.deepcopy(cgd_wrapper)
    if change == "hash":
        wrapper["sha256"] = "0" * 64
    elif change == "url":
        wrapper["url"] += "?different-release"
    elif change == "version":
        wrapper["body"] = wrapper["body"].replace(audit.CGD_VERSION, "OLD")
    elif change == "duplicate":
        wrapper["body"] += wrapper["body"].splitlines(keepends=True)[1]
    elif change == "alias":
        wrapper["body"] = wrapper["body"].replace("orf19.6438", "OTHER")
    elif change == "gene":
        wrapper["body"] = wrapper["body"].replace("\tCMP1\t", "\tPDE1\t")
    if change not in {"hash", "url"}:
        wrapper["sha256"] = hashlib.sha256(wrapper["body"].encode()).hexdigest()
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_cgd(wrapper)
        return
    result = audit.project_cgd(wrapper)
    assert result["cna1"]["primary_gene_name"] == "CMP1"
    assert result["cna1_homonym"]["primary_gene_name"] == "PDE1"
    assert all("CNA1" in result[k]["aliases"] for k in ("cna1", "cna1_homonym"))
    assert result["lcb1"]["primary_gene_name"] is None
    assert "SYNTHETIC_DESCRIPTION_NOT_EXPORTED" not in json.dumps(result)


@pytest.mark.parametrize("key", ["cna1", "lcb1"])
@pytest.mark.parametrize("change", ["none", "gene", "locus", "cgd", "evidence", "taxon", "species",
                                   "reviewed", "sequence", "features", "version"])
def test_candida_reference_requires_exact_locus_evidence(dossier, key, change):
    protein = dossier["reference_proteins"][key]
    feature = copy.deepcopy(protein["cgd_feature"])
    locus = "orf19.13454" if key == "cna1" else "orf19.13796"
    gene = {"orderedLocusNames": [{"value": locus, "evidences": [
        {"source": "CGD", "id": feature["cgd_id"]}]}]}
    if key == "cna1":
        gene["geneName"] = {"value": "CMP1"}
    entry = {"primaryAccession": "P12345", "entryType": "UniProtKB unreviewed (TrEMBL)",
             "entryAudit": {"entryVersion": 1, "sequenceVersion": 1}, "genes": [gene],
             "organism": {"taxonId": 237561, "scientificName": "Reference strain"},
             "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}}}
    taxonomy = {"taxonId": 237561, "active": True, "rank": "strain",
                "lineage": [{"rank": "species", "taxonId": 5476}]}
    if change == "gene":
        gene["geneName"] = {"value": "CNA1" if key == "cna1" else "LCB1"}
    elif change == "locus":
        gene["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "cgd":
        feature["cgd_id"] = audit.CGD_IDS["cna1_homonym"]
    elif change == "evidence":
        gene["orderedLocusNames"][0]["evidences"][0]["source"] = "OTHER"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 559292
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 4932
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    elif change in {"sequence", "features"}:
        entry[change] = []
    if change == "none":
        result = audit.project_candida(entry, key, taxonomy, feature)
        assert result["primary_gene_name"] == ("CMP1" if key == "cna1" else None)
    else:
        with pytest.raises(ValueError):
            audit.project_candida(entry, key, taxonomy, feature)


def test_zero_hit_alias_query_is_resolved_not_absence(dossier):
    requests = dossier["uniprot_requests"]
    assert len(requests) == 5
    assert requests["lcb1"]["results"] == 0 and requests["lcb1-locus"]["results"] == 1
    assert all(r["status"] == 200 and r["complete_for_query"] for r in requests.values())
    assert parse_qs(urlsplit(requests["lcb1-locus"]["url"]).query)["query"] == [audit.LOCUS_QUERY]
    assert dossier["cna1_disambiguation"]["selected_reference_gene"] == "CMP1"
    assert dossier["cna1_disambiguation"]["other_cgd_alias_gene"] == "PDE1"
    assert not dossier["cna1_disambiguation"]["other_alias_is_protein_absence"]


@pytest.mark.parametrize("change", ["none", "duplicate", "lab_id", "species", "wgs", "header"])
def test_subjects_preserve_wgs_membership_without_genome_assignment(change):
    strains = [["Strain name", "Strain number", "Species", "Genotype", "Source"]]
    strains.extend([label, lab, "C. albicans" if label.startswith("Ca-") else "S. cerevisiae",
                    "NOT_FOR_EXPORT", "This study"] for label, lab in audit.SUBJECTS.items())
    coverage = [["Strain", "Mean Coverage"], ["Sc-F-1", "NOT_FOR_EXPORT"], ["Sc-G-13", "NOT_FOR_EXPORT"]]
    coverage.extend([label, "NOT_FOR_EXPORT"] for label in audit.SUBJECTS if label.startswith("Ca-"))
    if change == "duplicate":
        strains.append(strains[1])
    elif change == "lab_id":
        strains[1][1] = "OTHER"
    elif change == "species":
        strains[1][2] = "C. albicans"
    elif change == "wgs":
        coverage[1][0] = "Sc-F-2"
    elif change == "header":
        strains[0] = coverage[0]
    if change == "none":
        result = audit.project_subjects(strains, coverage)
        assert len(result) == 8
        assert sum(r["listed_in_table_s1_wgs_coverage"] for r in result.values()) == 6
        assert not any(r["experimental_sample_or_assembly_assigned"] for r in result.values())
        assert "NOT_FOR_EXPORT" not in json.dumps(result)
    else:
        with pytest.raises(ValueError):
            audit.project_subjects(strains, coverage)


@pytest.fixture
def inspection(tmp_path):
    result = {k: True for k in (
        "primary_results_subsections_and_captions_read", "source_table_selected_identifiers_checked",
        "cna1_cgd_homonym_retained", "lcb1_primary_gene_name_not_invented",
        "figure5_panel_c_miconazole_not_fluconazole",
        "figure7b_tacrolimus_not_separate_cyclosporin_a_allele_test",
        "figure7c_control_discordance_retained", "figure8_copy_number_profiles_not_gene_specific_causation")}
    result.update({"whole_article_review_complete": False,
                   "sequence_variant_construct_protocol_or_numeric_ast_exported": False,
                   "reference_projections_reviewed": ["fpr1", "cnb1", "cna1", "lcb1-locus"], "figures": {}})
    for number in (5, 7, 8):
        body, receipt = [tmp_path / f"figure{number}-storage-{suffix}"
                         for suffix in ("response.bin", "receipt.json")]
        body.write_text(str(number))
        receipt.write_text("{}")
        result["figures"][str(number)] = {"response": audit.reference.pin(tmp_path, body),
                                         "receipt": audit.reference.pin(tmp_path, receipt),
                                         "manually_reviewed": True}
    return result


@pytest.mark.parametrize("field", [
    "primary_results_subsections_and_captions_read", "source_table_selected_identifiers_checked",
    "cna1_cgd_homonym_retained", "lcb1_primary_gene_name_not_invented",
    "figure5_panel_c_miconazole_not_fluconazole",
    "figure7b_tacrolimus_not_separate_cyclosporin_a_allele_test",
    "figure7c_control_discordance_retained", "figure8_copy_number_profiles_not_gene_specific_causation",
])
@pytest.mark.parametrize("value", [None, False, 1, "true"])
def test_manual_attestations_fail_closed(tmp_path, inspection, field, value):
    audit.validate_inspection(tmp_path, tmp_path, inspection)
    inspection[field] = value
    with pytest.raises(ValueError):
        audit.validate_inspection(tmp_path, tmp_path, inspection)


def test_compound_panels_and_evidence_levels_remain_distinct(dossier):
    findings = dossier["conditional_findings"]
    assert findings[0]["functional_comparison_azole"] == "miconazole"
    assert findings[0]["lineage_profile_azole"] == findings[1]["functional_comparison_azole"] == "fluconazole"
    assert "NOT_AN_IDENTIFIED_EVOLVED" in findings[2]["evidence"]
    assert "NOT_INDEPENDENT_SUFFICIENCY" in findings[3]["evidence"]
    assert "NOT_SEPARATE_ALLELE_SPECIFIC" in findings[3]["cyclosporin_a"]
    assert "NOT_ALLELE_SPECIFIC_GENETIC_VALIDATION" in findings[4]["evidence"]
    assert "ANCESTRAL_RESPONSE_DIFFERS" in findings[4]["controls"]
    assert not findings[4]["direct_myriocin_resistance_claim"]
    assert not dossier["lineage_profiles"]["aneuploidy_gene_specific_causality_inferred"]
    assert not dossier["archive_context"]["experimental_sample_or_assembly_assignments"]
    assert not dossier["archive_context"]["universal_genome_absence_inferred"]


def test_public_scope_and_redaction(dossier):
    assert dossier["summary"]["corpus_records_in_scope"] == 2939
    for key in ("biological_records_changed", "experimental_alleles_assigned", "whole_records_completed",
                "new_taxonomy_queries"):
        assert dossier["summary"][key] == 0
    assert set(dossier["primary"]["native_figures"]) == {"5", "7", "8"}
    for figure in dossier["primary"]["native_figures"].values():
        assert not urlsplit(figure["final_url_without_query"]).query
    assert not dossier["primary"]["whole_article_review_complete"]
    assert "crowded" in dossier["primary"]["source_layout_limit"]
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert not any(v for k, v in dossier["constraints"].items() if k != "issue_1040")
    serialized = json.dumps(dossier).lower()
    for forbidden in ("x-goog-signature", "x-goog-credential", '"sequence":', '"alteration":',
                      '"construct":', '"protocol":', '"mic_value":', "not_for_export"):
        assert forbidden not in serialized

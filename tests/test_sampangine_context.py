"""Keep reported leads, sensitivity, reference identity and inspected scope separate."""

import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "research/2026-10-13-sampangine-context.json"


@pytest.fixture
def dossier():
    return json.loads(PUBLIC.read_bytes())


def pinned_json(pin):
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    return json.loads(raw)


def test_exact_historical_identity_without_loading_mutable_record(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    pin = dossier["inputs"]["census"]
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    rows = list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))
    assert len(rows) == dossier["summary"]["corpus_records_in_scope"] == 2939
    row = next(r for r in rows if r["identifier"] == "CHEBI:67606")
    for field in ("identifier", "path", "standard_inchi_key"):
        assert dossier["record"][field] == row[field]
    assert dossier["record"]["sha256"] == row["record_sha256"]
    assert row["standard_inchi_key"] == "BWQKHOMAOVUASZ-UHFFFAOYSA-N"
    assert int(row["resistance_assertions"]) == 0


@pytest.mark.parametrize(
    "gene,accession,version,sequence_version,locus",
    [("HEM4", "P06174", 178, 2, "YOR278W"), ("CIN5", "P40917", 181, 1, "YOR028C"),
     ("SNQ2", "P32568", 216, 2, "YDR011W")],
)
def test_reference_does_not_assign_experimental_identity(
    dossier, gene, accession, version, sequence_version, locus,
):
    reference = dossier["reference_proteins"][gene]
    assert reference["protein_accession"] == "UniProtKB:" + accession
    assert reference["entry_version"] == version and reference["sequence_version"] == sequence_version
    assert reference["ordered_locus_names"] == [locus] and gene in reference["gene_names"]
    assert reference["reference_taxon_id"] == "NCBITaxon:559292"
    assert reference["reference_taxon_rank"] == "strain"
    assert reference["source_species_taxon_id"] == "NCBITaxon:4932"
    assert reference["species_lineage_verified"]
    for field in ("exact_resistance_allele", "experimental_subject_assignment",
                  "compound_specific_resistance_independently_verified", "human_assay_protein_assignment"):
        assert not reference[field]
    if gene == "CIN5":
        assert "YAP4" in reference["gene_names"]
        assert reference["protein_name"] == "AP-1-like transcription factor YAP4"


def test_reused_metadata_is_not_a_cross_compound_phenotype_transfer(dossier):
    old = pinned_json(dossier["inputs"]["snq2_dossier"])
    current = dossier["reference_proteins"]["SNQ2"]
    prior = old["reference_proteins"]["SNQ2"]
    assert current["protein_accession"] == prior["accession"]
    assert current["entry_version"] == prior["entry_version"]
    assert current["sequence_version"] == prior["sequence_version"]
    request = dossier["uniprot_requests"]["SNQ2"]
    assert request["reused_byte_identically"] and not request["new_request"]
    matches = [r for r in old["uniprot_requests"] if r["path"] == request["path"]]
    assert len(matches) == 1
    assert all(request[k] == v for k, v in matches[0].items())
    old_taxonomy = pinned_json(dossier["inputs"]["taxonomy_dossier"])["taxonomy_request"]
    reused_taxonomy = dossier["taxonomy_request"]
    assert reused_taxonomy["reused_byte_identically"] and not reused_taxonomy["new_request"]
    assert all(reused_taxonomy[k] == v for k, v in old_taxonomy.items())
    assert dossier["resistance_assertions_added"] == []
    assert current["role"] == "AUTHOR_REPORTED_LEAD_WITHOUT_DISPLAYED_RESULTS_REFERENCE"


def test_discovery_absence_is_limited_to_the_two_inspected_outputs(dossier):
    assert set(dossier["discovery"]) == {"canonical", "aliases"}
    for key, item in dossier["discovery"].items():
        data = pinned_json(item["input"])
        row = next(r for r in data["records"] if r["identifier"] == "CHEBI:67606")
        citations = (row["candidates"] if key == "canonical" else
                     [c for q in row["queries"] for c in q["candidates"]])
        assert sorted({c["doi"].lower() for c in citations if c.get("doi")}) == item["retained_dois"]
        assert item["retained_dois"] == ["10.1128/ec.00323-07"]
        assert not item["includes_reviewed_2011_source"]
        assert not item["all_discovery_sources_or_full_bibliography_audited"]


def test_qualitative_evidence_scopes_do_not_become_resistance_alleles(dossier):
    primary = dossier["primary"]
    assert primary["doi"] == "10.1128/ec.05170-11"
    findings = {f["key"]: f for f in primary["findings"]}
    assert findings["snq2"]["evidence_scope"] == "AUTHOR_REPORT_DATA_NOT_SHOWN"
    assert not findings["snq2"]["direct_transport_demonstrated"]
    assert findings["hem4_sensitivity"]["evidence_scope"] == "SENSITIVITY_NOT_RESISTANCE"
    assert findings["hem4_negative"]["evidence_scope"] == "AUTHOR_REPORTED_NEGATIVE_FINDING_DATA_NOT_SHOWN"
    assert not findings["hem4_negative"]["establishes_biological_absence"]
    assert not findings["screen_scope"]["erases_snq2_report"]
    assert not findings["human_yeast_scope"]["human_assay_protein_assigned_from_yeast_reference"]
    assert all(not f["curation_admitted"] for f in findings.values())
    assert dossier["reference_proteins"]["HEM4"]["role"] == (
        "SENSITIVITY_AND_NEGATIVE_FINDING_REFERENCE_NOT_RESISTANCE_ALLELE"
    )
    assert dossier["reference_proteins"]["CIN5"]["role"] == "HELD_EARLIER_PRIMARY_LEAD_REFERENCE"


def test_text_inspection_is_not_native_figure_review_or_a_saved_denied_page(dossier):
    inspection = dossier["primary"]["inspection"]
    assert inspection["transport"] == "web.open" and inspection["selected_primary_results_text_read"]
    for key in ("native_result_images_reviewed", "supplements_reviewed", "full_article_review_complete",
                "full_text_snapshot_persisted", "failed_requests_retried_or_bypassed"):
        assert not inspection[key]
    denied = dossier["primary_cache_failure"]
    assert denied["status"] == 403 and not denied["is_primary_text_snapshot"]
    assert denied["url"] == dossier["primary"]["url"]
    assert not denied["redirects_followed"]
    assert {h["asset"] for h in dossier["access_holds"]} == {"earlier_primary_article", "figure1"}
    assert all(not h["retried_or_alternate_transport_used"] for h in dossier["access_holds"])


def test_reference_queries_are_bounded_and_no_new_taxonomy_request_is_claimed(dossier):
    for gene, request in dossier["uniprot_requests"].items():
        parsed = urlparse(request["url"])
        assert parsed.scheme == "https" and parsed.netloc == "rest.uniprot.org"
        assert parsed.path == "/uniprotkb/search"
        params = parse_qs(parsed.query)
        assert params["query"] == [f"gene_exact:{gene} AND organism_id:559292 AND reviewed:true"]
        assert request["release"] == "2026_03" and request["status"] == 200
        assert "sequence" not in params["fields"][0].split(",")
    assert dossier["summary"]["new_uniprot_queries"] == 2
    assert dossier["summary"]["reused_uniprot_queries"] == 1
    assert dossier["summary"]["new_taxonomy_requests"] == 0


def test_reported_species_name_is_not_a_reference_strain_or_primary_taxid(dossier):
    context = dossier["source_organism_context"]
    assert context["source_reported_name"] == "Saccharomyces cerevisiae"
    assert context["named_taxon_id"] == "NCBITaxon:4932" and context["rank"] == "species"
    assert context["grounding_basis"] == "NAME_MATCH_TO_PINNED_UNIPROT_SPECIES_LINEAGE"
    assert context["taxon_id_source"] == "UNIPROT_LINEAGE_MATCH_NOT_VERIFIED_AS_ARTICLE_REPORTED"
    assert not context["reference_strain_taxon_id_assigned_to_experiment"]
    assert not context["resistance_subject_assignment"]
    assert context["experimental_strain_sample_genome_and_allele_links"] == "UNRESOLVED_NOT_ASSERTED_ABSENT"


def test_no_operational_payload_or_completion_claim(dossier):
    assert dossier["experimental_subjects_assigned"] == []
    assert dossier["primary"]["whole_record_review"] == "OPEN"
    for key in ("biological_records_changed", "experimental_accessions_assigned", "whole_records_completed"):
        assert dossier["summary"][key] == 0
    forbidden = {"sequence", "features", "alteration", "variants", "mic", "construct", "protocol"}

    def check(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(dossier)

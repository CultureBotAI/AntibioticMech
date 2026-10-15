"""A source-label review cannot become component-specific AST or an experimental allele."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_rosab_primary as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize(
    "key",
    [
        "tested_derivative_is_reference_parent",
        "component_specific_assay_established",
        "direct_vs_indirect_action_resolved_by_single_gene_comparison",
        "heterologous_and_native_contexts_merged",
        "numeric_ast_exported",
        "clinical_resistance_interpretation_assigned",
        "figures_visually_reviewed",
        "table_layout_visually_verified",
        "whole_paper_signoff",
        "display_date_is_new_experiment",
    ],
)
def test_primary_text_cannot_be_promoted(key):
    notes = assessment()
    notes["primary"][key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "key",
    [
        "qualification_already_applied",
        "experimental_protein_or_strain_assignment",
        "exact_allele_assignment",
        "experimental_genome_assignment",
        "sequence_variant_construct_protocol_exports",
        "broader_gene_or_record_review_complete",
    ],
)
def test_reference_context_is_not_biological_curation(key):
    notes = assessment()
    notes["handoff"][key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "change", ["doi", "component", "parent", "units", "held", "absence", "retry", "ncbi"]
)
def test_changed_identity_measurements_and_access_scope_rejected(change):
    notes = assessment()
    if change == "doi":
        notes["primary"]["doi"] = audit.HELD_DOI
    elif change == "component":
        notes["primary"]["paper_compound_label"] = "polymyxin B1"
    elif change == "parent":
        notes["primary"]["paper_parent_context_table_label"] = "8081-c"
    elif change == "units":
        notes["primary"]["displayed_disk_diffusion_unit_statement"] = "10 units = 1 mm"
    elif change == "held":
        notes["second_citation"]["primary_results_reviewed"] = True
    elif change == "absence":
        notes["second_citation"]["absence_of_component_evidence_in_this_paper_established"] = True
    elif change == "retry":
        notes["access_accounting"]["held_source_retried"] = True
    else:
        notes["access_accounting"]["ncbi_endpoints_opened"] = 1
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def native_fixture():
    entry = {
        "primaryAccession": "Q56877",
        "entryType": "unreviewed",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "organism": {"taxonId": 34054, "scientificName": "Yersinia enterocolitica"},
        "genes": [{"geneName": {"value": "rosA"}}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "reference protein"}}},
        "uniProtKBCrossReferences": [{"database": "CARD", "id": "ARO:3003048"}],
        "references": [
            {
                "referenceNumber": 1,
                "referencePositions": ["NUCLEOTIDE SEQUENCE"],
                "referenceComments": [{"type": "STRAIN", "value": "8081-c"}],
                "citation": {
                    "citationType": "journal article",
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "10931306"},
                        {"database": "DOI", "id": audit.DOI},
                    ],
                },
            }
        ],
    }
    taxon = {
        "taxonId": 34054,
        "scientificName": "Yersinia enterocolitica (type O:8)",
        "rank": "serotype",
        "active": True,
        "parent": {"taxonId": 630, "scientificName": "Yersinia enterocolitica"},
        "lineage": [{"taxonId": 630, "scientificName": "Yersinia enterocolitica", "rank": "species"}],
    }
    return entry, taxon


def test_reference_bibliography_keeps_parent_context_not_tested_derivative():
    entry, taxon = native_fixture()
    expected = audit.members.member_reference(entry, taxon)
    row = audit.reference_context(entry, taxon, expected, "ARO:3003048")
    assert row["reference"] == expected
    citation = row["primary_citation_binding"]
    assert citation["reference_strain_comments"] == ["8081-c"]
    assert citation["reference_positions"] == ["NUCLEOTIDE SEQUENCE"]
    assert citation["reference_comment_assigns_experimental_derivative"] is False


@pytest.mark.parametrize("change", ["gene", "xref", "citation", "doi", "strain", "duplicate"])
def test_native_bibliography_binding_must_be_exact(change):
    entry, taxon = native_fixture()
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "rosB"
    elif change == "xref":
        entry["uniProtKBCrossReferences"][0]["id"] = "ARO:3003049"
    elif change == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "12010497"
    elif change == "doi":
        entry["references"][0]["citation"]["citationCrossReferences"][1]["id"] = audit.HELD_DOI
    elif change == "strain":
        entry["references"][0]["referenceComments"][0]["value"] = "8081-res"
    else:
        extra = copy.deepcopy(entry["references"][0])
        extra["referenceNumber"] = 2
        entry["references"].append(extra)
    expected = audit.members.member_reference(entry, taxon)
    with pytest.raises(ValueError):
        audit.reference_context(entry, taxon, expected, "ARO:3003048")


def test_portable_artifact_covers_all_four_source_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.read_json(ROOT, result["prior"])
    audit.read_json(ROOT, result["plan"])
    audit.validate_assessment(audit.read_json(ROOT, result["assessment"]))
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] == audit.PARENT]
    ids = {c["record_identifier"] for c in result["claims"]}
    assert result["records"] == [r for r in prior["records"] if r["identifier"] in ids]
    assert len(ids) == len(result["claims"]) == len(result["claim_dispositions"]) == 4
    assert {r["label"] for r in result["records"]} == {
        "polymyxin B1",
        "polymyxin B2",
        "polymyxin B3",
        "polymyxin B4",
    }
    assert result["summary"]["corpus_records_hash_checked"] == 2939
    assert result["summary"]["native_protein_entries_replayed"] == 4182
    assert result["summary"]["new_uniprot_requests"] == 0
    for row in result["claim_dispositions"]:
        assert row["individual_component_assay_established"] is row["source_claim_removed"] is False
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["whole_record_primary_signoffs"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_name_level_species_and_serotype_are_not_strain_assignments():
    result = public_result()
    crosswalk = result["paper_species_name_crosswalk"]
    assert crosswalk["species_taxon_id"] == "NCBITaxon:630"
    assert crosswalk["reference_serotype_taxon_id"] == "NCBITaxon:34054"
    assert crosswalk["reference_rank"] == "serotype"
    assert (
        crosswalk["record_taxon_assignment"]
        is crosswalk["experimentally_tested_derivative_taxon_assigned"]
        is False
    )
    assert result["manual_review_status"]["assessment_is_independently_reproduced_by_code"] is False
    assert result["manual_review_status"]["biological_curation_completed"] is False


def test_no_sequence_or_experimental_measurement_exports():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "alteration",
        "variants",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_replay_when_native_cache_available():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["proteins"]["path"]).exists():
        pytest.skip("native cache unavailable; portable artifact checks still run")
    assert audit.build(ROOT) == public_result()


def test_public_artifact_checksum_is_stable():
    assert hashlib.sha256((ROOT / audit.OUTPUT).read_bytes()).hexdigest() == (
        "a7e92679f5cd6210f22943681e4c397b180b70bb322cf4e723a0e44a06ee0a4f"
    )

"""Protein names and publication metadata never identify a resistant study allele."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_m35_porin_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline porin audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def entry():
    return {
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "primaryAccession": "REFERENCE",
        "organism": {"taxonId": 480, "scientificName": "Moraxella catarrhalis"},
        "proteinDescription": {"submissionNames": [{"fullName": {"value": audit.NAME}}]},
        "references": [
            {
                "citation": {
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": audit.PMID},
                        {"database": "DOI", "id": audit.DOI.upper()},
                    ]
                }
            }
        ],
    }


def node():
    return {"taxonId": 480, "rank": "species", "scientificName": "Moraxella catarrhalis", "active": True}


@pytest.mark.parametrize(
    "name,expected",
    [
        (audit.NAME, True),
        ("M35", False),
        (audit.NAME + "-like", False),
        (audit.NAME.lower(), False),
        (audit.NAME + "A", False),
        ("Outer membrane porin", False),
    ],
)
def test_exact_reviewed_full_name_not_generic_name_matching(name, expected):
    e = entry()
    e["proteinDescription"]["submissionNames"][0]["fullName"]["value"] = name
    result = audit.candidate(e, node())
    assert result["qualified_reference"] is expected
    assert result["native_source_gene_matches"] == []
    assert result["gene_symbol_inferred_from_protein_name"] is False
    assert result["experimental_subject_assignment"] is result["exact_allele_assignment"] is False
    assert result["individual_paper_isolate_assignment"] is result["experimental_genome_assignment"] is None
    assert result["reference_identity_establishes_resistance"] is False


@pytest.mark.parametrize(
    "change",
    [
        "missing_citation",
        "wrong_pmid",
        "wrong_doi",
        "split_citation",
        "wrong_namespace",
        "short_name_only",
        "gene_name_only",
        "wrong_entry_taxon",
        "wrong_node_taxon",
        "wrong_entry_species",
        "wrong_node_species",
        "wrong_rank",
        "inactive_taxon",
    ],
)
def test_each_qualification_condition_is_independent(change):
    e, n = entry(), node()
    refs = e["references"][0]["citation"]["citationCrossReferences"]
    if change == "missing_citation":
        e["references"] = []
    elif change == "wrong_pmid":
        refs[0]["id"] = "20801781"
    elif change == "wrong_doi":
        refs[1]["id"] = "10.1093/jac/dkq312"
    elif change == "split_citation":
        e["references"].append({"citation": {"citationCrossReferences": [refs.pop()]}})
    elif change == "wrong_namespace":
        refs[0]["database"] = "DOI"
    elif change == "short_name_only":
        e["proteinDescription"] = {"submissionNames": [{"shortNames": [{"value": audit.NAME}]}]}
    elif change == "gene_name_only":
        e["proteinDescription"] = {}
        e["genes"] = [{"geneName": {"value": "M35"}}]
    elif change == "wrong_entry_taxon":
        e["organism"]["taxonId"] = 615
    elif change == "wrong_node_taxon":
        n["taxonId"] = 615
    elif change == "wrong_entry_species":
        e["organism"]["scientificName"] = "Other species"
    elif change == "wrong_node_species":
        n["scientificName"] = "Other species"
    elif change == "wrong_rank":
        n["rank"] = "strain"
    else:
        n["active"] = False
    assert audit.candidate(e, n)["qualified_reference"] is False


@pytest.mark.parametrize("state", ["Inactive", "unknown"])
def test_inactive_or_unknown_reference_is_rejected(state):
    e = entry()
    e["entryType"] = state
    with pytest.raises(ValueError, match="reference state"):
        audit.candidate(e, node())


@pytest.mark.parametrize(
    "group,key",
    [
        (None, "numeric_ast_exported"),
        (None, "experimental_allele_assignments"),
        (None, "manual_web_assessment_is_native_body_replay"),
        (None, "biological_record_writes"),
        ("m35_identity", "gene_symbol_inferred_from_protein_name"),
        ("m35_identity", "paper_nucleotide_to_uniprot_crosswalk_verified"),
        ("m35_later_study", "reference_proteins_assigned_to_later_subjects"),
        ("m35_later_study", "results_reviewed_for_ast_curation"),
        ("omp1_archive_access", "origin_http_status_inferred"),
        ("omp1_archive_access", "primary_text_reviewed"),
        ("omp1_archive_access", "global_unavailability_or_paywall_inferred"),
    ],
)
def test_assessment_cannot_promote_evidence_scope(group, key):
    a = json.loads((ROOT / (audit.PREFIX + "-assessment.json")).read_bytes())
    audit.check_assessment(a)
    (a if group is None else a[group])[key] = True
    with pytest.raises(ValueError, match="overclaims"):
        audit.check_assessment(a)


@pytest.mark.parametrize("key", ["same_route_retries", "alternate_routes_requested"])
def test_archive_access_history_is_preserved(key):
    a = json.loads((ROOT / (audit.PREFIX + "-assessment.json")).read_bytes())
    a["omp1_archive_access"][key] = 1
    with pytest.raises(ValueError, match="access limitation"):
        audit.check_assessment(a)


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_references_keep_gene_and_subject_identity_separate():
    d = saved()
    assert d["summary"]["complete_records_read"] == d["summary"]["source_claims"] == 8
    assert d["summary"]["corpus_records_hash_checked"] == 2939
    assert d["coverage"]["new_qualified_terms"] == ["ARO:3004124"]
    assert d["summary"]["combined_qualified_terms"] == 108
    assert d["summary"]["combined_remaining_terms"] == 70
    assert d["coverage"]["whole_corpus_completion"] is False
    assert d["terms"]["ARO:3004124"]["qualified_reference_accessions"] == [
        "UniProtKB:Q3MK85",
        "UniProtKB:Q3MK87",
    ]
    assert d["terms"]["ARO:3004128"]["qualified_reference_accessions"] == []
    assert d["reference_views"]["Q3MK87"]["orf_names"] == ["EJK53_1371", "EJK54_2095"]
    assert d["reference_views"]["Q3MK85"]["orf_names"] == []
    assert d["omp1_context"]["native_publication_types"] == ["Review", "Journal Article"]
    assert d["omp1_context"]["unassigned_citation_hit"]["assigned_to_source_term"] is False
    assert d["summary"]["reused_complete_queries"] == 6
    assert d["summary"]["new_protein_metadata_requests"] == d["summary"]["ncbi_requests"] == 0
    for claim in d["claims"]:
        current = d
        for key in claim["term_pointer"].lstrip("/").split("/"):
            current = current[key]
        assert claim["record_identifier"] in current["record_memberships"]
    audit.previous.previous.reject_operational_fields(d)


@pytest.mark.parametrize("change", ["duplicate", "overlap", "already_qualified", "out_of_scope"])
def test_coverage_is_disjoint_and_counts_terms_not_reference_entries(change):
    old = json.loads((ROOT / "research/2026-10-15-daptomycin-locus.json").read_bytes())["coverage"]
    old = copy.deepcopy(old)
    added = ["ARO:3004124"]
    assert len(audit.combined_coverage(old, added)["qualified_terms"]) == 108
    if change == "duplicate":
        old["qualified_terms"].append(old["qualified_terms"][0])
    elif change == "overlap":
        old["remaining_terms"][0] = old["qualified_terms"][0]
    elif change == "already_qualified":
        added = [old["qualified_terms"][0]]
    else:
        added = ["OTHER"]
    with pytest.raises(ValueError, match="coverage"):
        audit.combined_coverage(old, added)


def test_report_preserves_all_previous_bytes():
    p = json.loads((ROOT / audit.PLAN).read_bytes())
    report = (ROOT / p["previous_report"]["path"]).read_bytes()
    start = report.index(b"## M35 Porin Reference Context (2026-10-15)\n")
    end = report.index(b"## Remaining work\n", start)
    old = report[:start] + report[end:]
    index = ROOT / "research/2026-10-15-card-reference-reconciled.json"
    summary = json.loads(index.read_bytes())["summary"]
    current = (
        "   determinants: the current broad index has reference context for "
        f"{summary['selected_reference_terms']:,}, with\n"
        f"   {summary['unresolved_reference_terms']:,} lacking selected references. "
        "The separate explicit-member audit covers 63\n"
    ).encode()
    historical = (
        b"   determinants: the current broad index has candidates for 1,282, with 720\n"
        b"   lacking selected candidates. The separate explicit-member audit covers 63\n"
    )
    assert old.count(current) == 1
    old = old.replace(current, historical)
    assert len(old) == p["previous_report_bytes"] == 988453
    assert hashlib.sha256(old).hexdigest() == p["previous_report"]["sha256"]
    assert report.count(b"## Remaining work\n") == 1


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["taxonomy_inventory"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable artifact tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == saved()


def test_cli_is_immutable_and_supports_nested_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_does_not_create_missing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "absent" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()

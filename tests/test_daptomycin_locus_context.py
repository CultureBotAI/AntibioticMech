"""Paper locus spelling and reference taxonomy do not establish experimental identity."""

import builtins
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_daptomycin_locus_context as audit  # noqa: E402

SPECIES = {"taxonId": 1351, "rank": "species", "scientificName": "Enterococcus faecalis"}


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline locus audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def entry(locus="EF_1753"):
    return {
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "primaryAccession": "REFERENCE",
        "organism": {"taxonId": 226185},
        "genes": [{"geneName": {"value": "liaX"}, "orderedLocusNames": [{"value": locus}]}],
    }


def node():
    return {
        "taxonId": 226185,
        "rank": "strain",
        "scientificName": "Enterococcus faecalis (strain ATCC 700802 / V583)",
        "strains": [{"name": "ATCC 700802 / V583", "synonyms": ["V583"]}],
    }


def lead():
    return {"paper_reference_locus": "EF1753", "source_gene": "YvlB", "paper_reference_strain": None}


@pytest.mark.parametrize(
    "value,expected",
    [
        ("EF1753", "NONE"),
        ("EF_1753", "SINGLE_NAMESPACE_SEPARATOR"),
        ("EF-1753", None),
        ("EF__1753", None),
        ("EF_1797", None),
        ("EF_01753", None),
        ("ef_1753", None),
    ],
)
def test_only_reviewed_locus_separator_rule_is_applied(value, expected):
    result = audit.ordered_locus_matches(entry(value), "EF1753")
    assert bool(result) is (expected is not None)
    if result:
        assert result[0]["normalization"] == expected
        assert result[0]["literal_equality"] is (expected == "NONE")
        assert result[0]["value"] == value


@pytest.mark.parametrize("locus", ["EF_1753", "EF175", "EF17530", "OTHER1753", "liaX"])
def test_source_grammar_is_not_a_general_identifier_normalizer(locus):
    with pytest.raises(ValueError, match="grammar"):
        audit.ordered_locus_matches(entry(), locus)


@pytest.mark.parametrize("namespace", ["geneName", "orfNames", "synonyms"])
def test_locus_cannot_be_satisfied_by_another_native_namespace(namespace):
    e = entry()
    e["genes"] = [{namespace: {"value": "EF_1753"} if namespace == "geneName" else [{"value": "EF_1753"}]}]
    assert audit.ordered_locus_matches(e, "EF1753") == []


@pytest.mark.parametrize(
    "state",
    [
        "matching",
        "wrong_species",
        "missing_species",
        "wrong_entry_strain",
        "wrong_node_strain",
        "wrong_rank",
        "missing_strain_name",
        "missing_locus",
    ],
)
def test_candidate_requires_locus_species_and_native_reference_strain(state):
    e, n, species = entry(), node(), SPECIES
    if state == "wrong_species":
        species = {**SPECIES, "taxonId": 1}
    elif state == "missing_species":
        species = None
    elif state == "wrong_entry_strain":
        e["organism"]["taxonId"] = 1
    elif state == "wrong_node_strain":
        n["taxonId"] = 1
    elif state == "wrong_rank":
        n["rank"] = "species"
    elif state == "missing_strain_name":
        n["strains"] = []
    elif state == "missing_locus":
        e["genes"] = []
    result = audit.candidate(e, lead(), SPECIES, species, n)
    assert result["qualified_reference"] is (state == "matching")
    assert result["native_source_gene_matches"] == []
    assert result["paper_reference_strain_matches_native"] is None
    assert result["official_gene_rename_verified"] is False
    assert result["experimental_subject_assignment"] is result["exact_allele_assignment"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["primary_resistance_validation"] is False


def test_supplied_paper_reference_strain_is_not_experimental_subject():
    paper_lead = {**lead(), "paper_reference_strain": "V583"}
    result = audit.candidate(entry(), paper_lead, SPECIES, SPECIES, node())
    assert result["paper_reference_strain_matches_native"] is True
    assert result["experimental_subject_assignment"] is False


@pytest.mark.parametrize("state", ["Inactive", "unknown"])
def test_inactive_or_unknown_entries_cannot_be_references(state):
    e = entry()
    e["entryType"] = state
    with pytest.raises(ValueError, match="reference state"):
        audit.candidate(e, lead(), SPECIES, SPECIES, node())


@pytest.mark.parametrize(
    "key",
    [
        "experimental_allele_assignments",
        "whole_record_primary_signoff",
        "numeric_ast_exported",
        "protocols_exported",
        "native_http_status_inferred",
    ],
)
def test_assessment_cannot_upgrade_scope(key):
    a = json.loads((ROOT / (audit.PREFIX + "-primary-assessment.json")).read_bytes())
    audit.check_assessment(a)
    a[key] = True
    with pytest.raises(ValueError, match="overclaims"):
        audit.check_assessment(a)


@pytest.mark.parametrize("change", ["figure", "supplement", "canonical_status", "alternate_route", "locus"])
def test_assessment_preserves_correction_and_access_limits(change):
    a = json.loads((ROOT / (audit.PREFIX + "-primary-assessment.json")).read_bytes())
    if change == "figure":
        a["correction"]["replacement_image_visually_reviewed"] = True
    elif change == "supplement":
        a["correction"]["supplements_reviewed"] = True
    elif change == "canonical_status":
        a["earlier_study_access"]["canonical_article_http_status_inferred"] = True
    elif change == "alternate_route":
        a["earlier_study_access"]["alternate_routes_requested_after_denial"] = 1
    else:
        a["reference_leads"]["ARO:3003813"]["paper_reference_locus"] = "EF1753"
    with pytest.raises(ValueError):
        audit.check_assessment(a)


@pytest.mark.parametrize("change", ["attempt", "receipt", "body", "error", "missing_body"])
def test_unaccounted_requests_fail_closed(tmp_path, change):
    for key in audit.LOCI:
        for suffix in ("attempt", "receipt", "body"):
            (tmp_path / f"{key}-{suffix}.json").write_text("{}")
    audit.check_history(tmp_path)
    if change == "missing_body":
        (tmp_path / "yvlb-locus-body.json").unlink()
    else:
        (tmp_path / f"unexpected-{change}.json").write_text("{}")
    with pytest.raises(ValueError, match="unaccounted"):
        audit.check_history(tmp_path)


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_crosswalks_preserve_namespaces_holds_and_bounded_coverage():
    d = saved()
    assert d["summary"]["complete_records_read"] == 1
    assert d["summary"]["source_claims"] == 4
    assert d["coverage"]["new_qualified_terms"] == ["ARO:3003813", "ARO:3003815"]
    assert d["summary"]["combined_qualified_terms"] == 107
    assert d["summary"]["combined_remaining_terms"] == 71
    assert d["coverage"]["whole_corpus_completion"] is False
    assert d["terms"]["ARO:3003797"]["qualified_reference_accessions"] == []
    assert d["terms"]["ARO:3003800"]["qualified_reference_accessions"] == []
    assert d["terms"]["ARO:3003813"]["qualified_reference_accessions"] == ["UniProtKB:Q833X7"]
    assert d["terms"]["ARO:3003815"]["qualified_reference_accessions"] == ["UniProtKB:Q834B6"]
    assert d["retained_other_species_yybt_context"]["qualified_reference_accessions"] == []
    assert d["reused_gene_query"]["result_count"] == 1
    assert d["reused_gene_query"]["four_gene_matches"] == 0
    assert d["reused_citation_queries"]["23959318"]["result_count"] == 0
    for claim in d["claims"]:
        current = d
        for key in claim["term_pointer"].lstrip("/").split("/"):
            current = current[key]
        assert claim["record_identifier"] in current["record_memberships"]
    assert d["summary"]["biological_record_writes"] == d["summary"]["ncbi_requests"] == 0
    audit.previous.reject_operational_fields(d)


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["canary"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable artifact tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


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

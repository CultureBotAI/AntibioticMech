"""Full-corpus beta references retain native ambiguity and experimental limits."""

import copy
import socket
import sys
from collections import Counter
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_beta_tubulin_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden in index tests")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.prior.prior.read_inputs(ROOT, audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def resolve(data, pointer):
    value = data[pointer["input"]]
    for part in pointer["pointer"].split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def test_public_reproduction_retains_all_records_and_claims(frozen):
    result, rows = audit.project(*frozen)
    for suffix, payload in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == payload
    summary = result["summary"]
    assert summary["corpus_records"] == len(rows) == 2939
    assert summary["card_terms"] == len(result["terms"]) == 2002
    assert summary["card_assertions"] == len(result["claims"]) == 4538
    assert summary["selected_reference_terms"] == 1259
    assert summary["selected_reference_proteins"] == 1546
    assert summary["reference_links"] == 2658
    assert summary["records_with_selected_references"] == 219
    assert summary["added_reference_terms"] == summary["beta_source_terms"] == 15
    assert summary["beta_source_claims"] == 15
    assert summary["added_reference_proteins"] == 26
    assert summary["added_reference_links"] == 50
    assert summary["term_statuses"][audit.UNSELECTED] == 743
    assert summary["claim_statuses"][audit.UNSELECTED] == 1346
    assert summary["term_statuses"][audit.REVIEWED] == 11
    assert summary["term_statuses"][audit.UNREVIEWED] == 4
    assert summary["unreviewed_fragment_references"] == 232
    assert summary["phi_claims_not_reassessed"] == 217
    assert summary["curator_claims_not_reassessed"] == 133
    assert summary["score_rules_not_reassessed"] == 467
    assert summary["whole_record_primary_signoffs"] == 0
    assert all(
        sum(row[column] for column in audit.COLUMNS.values()) == row["card_assertions"] for row in rows
    )
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)


def test_all_pointers_and_inherited_scope_are_preserved(frozen):
    data = frozen[0]
    result, _ = audit.project(*frozen)

    def check(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                resolve(data, value)
            else:
                for child in value.values():
                    check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(result)
    for tid, original in data["base"]["terms"].items():
        if tid in data["beta"]["terms"]:
            continue
        expected = audit.rebase(original, "terms", tid)
        if expected["reference_status"] == audit.prior.UNSELECTED:
            expected["reference_status"] = audit.UNSELECTED
        assert result["terms"][tid] == expected
    for accession, original in data["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(original, "proteins", accession)
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        assert {**new, "reference_status": old["reference_status"]} == old
    assert result["limits"] == data["base"]["limits"]
    assert Counter(t["entity_review"] for t in result["terms"].values()) == Counter(
        t["entity_review"] for t in data["base"]["terms"].values()
    )
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["network_requests"] == result["limits"]["ncbi_requests"] == 0


def test_paralogs_orf_only_annotations_and_fragments_remain_references(frozen):
    result, _ = audit.project(*frozen)
    terms, proteins = result["terms"], result["proteins"]
    assert sorted(link["protein_accession"] for link in terms["ARO:3009433"]["links"]) == [
        "UniProtKB:P32928",
        "UniProtKB:P40904",
    ]
    assert terms["ARO:3009433"]["beta_query_disposition"] == "MULTIPLE_CANDIDATES_NO_SELECTION"
    assert proteins["UniProtKB:Q4WA70"]["native_gene_annotations"][0]["geneName"] == []
    assert proteins["UniProtKB:Q4WA70"]["native_gene_annotations"][0]["orfNames"] == ["AFUA_7G00250"]
    assert proteins["UniProtKB:K7XH91"]["native_gene_annotations"][0]["geneName"] == ["TUB"]
    assert proteins["UniProtKB:K7XH91"]["protein_description_flag"] == "Fragment"
    assert "UniProtKB:A0ACC3ZK29" not in proteins
    for tid in frozen[0]["beta"]["terms"]:
        term = terms[tid]
        assert term["source_gene_symbol_assignment"] is None
        assert term["whole_record_primary_review"] == "OPEN"
        for link in term["links"]:
            assert link["experimental_subject_assignment"] is link["exact_allele_assignment"] is False
            assert link["explicit_card_xref"] is False
            assert link["source_citation_ids"] == link["matched_reference_numbers"] == []


def test_native_synonym_and_initial_case_contexts_are_not_rewritten(frozen):
    data = frozen[0]
    result, _ = audit.project(*frozen)
    name = resolve(data, result["terms"]["ARO:3009431"]["beta_name_context"])
    assert name["source_name"] == "Fusarium graminearum"
    assert name["selected_taxon"]["scientific_name"] == "Gibberella zeae"
    assert name["selected_taxon"]["matching_fields"] == ["synonyms"]
    term = resolve(data, result["terms"]["ARO:3009324"]["beta_followup"])
    assert term["source_organism_name"] == "botrytis cinerea"
    assert term["name_normalization"] == "GENUS_INITIAL_CASE_ONLY"


def test_bibliographic_gaps_and_hold_remain_unresolved(frozen):
    data = frozen[0]
    result, _ = audit.project(*frozen)
    hold = resolve(data, result["beta_primary_access_hold"])
    assert hold["status"] == "PUBLISHER_403_CHALLENGE_HELD_NO_RETRY"
    assert hold["article_obtained"] is hold["paywall_inferred"] is False
    summary = result["summary"]["beta_bibliography_summary"]
    assert summary["native_reference_memberships"] == 81
    assert summary["references_without_identifiers"] == 47
    assert summary["journal_references_without_identifiers"] == 11
    assert summary["native_identifier_issues"] == 1
    assert summary["new_primary_result_reviews"] == 0
    botrytis = resolve(data, result["proteins"]["UniProtKB:P53373"]["beta_bibliography"])
    assert len(botrytis["reference_rows"]) == 3
    assert all(row["citation_type"] == "submission" for row in botrytis["reference_rows"])
    assert botrytis["experimental_subject_assignment"] is False


@pytest.mark.parametrize(
    "field,value",
    [
        ("full_corpus_goal_status", "COMPLETE"),
        ("issue_1040", "RESUMED"),
        ("experimental_allele_or_genome_assignments", 1),
        ("reuse_terms_review_resumed", True),
    ],
)
def test_inherited_limits_cannot_be_promoted(inputs, field, value):
    inputs[0]["base"]["limits"][field] = value
    with pytest.raises(ValueError, match="limits changed"):
        audit.project(*inputs)


def test_previously_unseen_overlap_cannot_overwrite_prior_protein_metadata(inputs):
    inputs[0]["base"]["proteins"]["UniProtKB:P53373"] = {}
    with pytest.raises(ValueError, match="unreviewed overlap"):
        audit.project(*inputs)


@pytest.mark.parametrize("change", ["missing", "extra", "label", "claim_hash", "claim_position", "record"])
def test_complete_source_cohort_cannot_be_trimmed_or_reassigned(inputs, change):
    data = inputs[0]
    dossier = data["beta"]
    if change == "missing":
        del dossier["terms"]["ARO:3009431"]
    elif change == "extra":
        dossier["terms"]["ARO:9999999"] = copy.deepcopy(dossier["terms"]["ARO:3009431"])
    elif change == "label":
        dossier["terms"]["ARO:3009431"]["source_label"] = "different"
    elif change == "claim_hash":
        dossier["claims"][0]["claim_sha256"] = "different"
    elif change == "claim_position":
        dossier["claims"][0]["position"] = -1
    else:
        dossier["records"].pop()
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("change", ["assignment", "rank", "lineage", "match", "candidate", "source"])
def test_native_name_scope_guards(frozen, change):
    name = "Fusarium graminearum"
    row = copy.deepcopy(frozen[0]["beta"]["names"][name])
    selected = row["selected_taxon"]
    if change == "assignment":
        row["experimental_subject_assignment"] = True
    elif change == "rank":
        selected["rank"] = "genus"
    elif change == "lineage":
        selected["lineage"][-1]["taxonId"] = 1
    elif change == "match":
        selected["matching_fields"] = ["otherNames"]
    elif change == "candidate":
        row["candidates"].append(copy.deepcopy(row["candidates"][0]))
    else:
        row["source"]["url"] = "https://example.org/taxonomy/5518"
    with pytest.raises(ValueError):
        audit.named_taxon(row, name)


@pytest.mark.parametrize(
    "change",
    [
        "wrong_url",
        "count",
        "duplicate",
        "candidate_omission",
        "dropped_exclusion",
        "eligible_exclusion",
        "not_complete",
        "query_kind",
        "review_state",
        "absence",
    ],
)
def test_complete_query_partition_and_reference_scope_guards(frozen, change):
    query = copy.deepcopy(frozen[0]["beta"]["terms"]["ARO:3009475"]["queries"]["unreviewed"])
    if change == "wrong_url":
        query["source"]["url"] = audit.beta.query_url(5467, True)
    elif change == "count":
        query["result_count"] = True
    elif change == "duplicate":
        query["all_result_accessions"].append(query["all_result_accessions"][0])
    elif change == "candidate_omission":
        query["candidate_accessions"].pop()
    elif change == "dropped_exclusion":
        query["excluded_candidates"] = []
    elif change == "eligible_exclusion":
        query["excluded_candidates"][0]["native_protein_names"][0]["value"] = "Beta-tubulin"
    else:
        field, value = {
            "not_complete": ("complete_for_query", False),
            "query_kind": ("query_type", "GENE_SYMBOL"),
            "review_state": ("reviewed_subset", True),
            "absence": ("zero_hit_is_biological_absence", True),
        }[change]
        query[field] = value
    with pytest.raises(ValueError):
        audit.check_query(query, 5467, False)


@pytest.mark.parametrize(
    "change", ["no_reviewed", "unsupported_fallback", "dropped_candidate", "selected_paralog"]
)
def test_reviewed_first_policy_and_all_paralogs_are_preserved(frozen, change):
    term = copy.deepcopy(frozen[0]["beta"]["terms"]["ARO:3009433"])
    selected = frozen[0]["beta"]["names"][term["taxonomy_query_name"]]["selected_taxon"]
    if change == "no_reviewed":
        term["queries"] = {}
    elif change == "unsupported_fallback":
        term["queries"]["unreviewed"] = copy.deepcopy(term["queries"]["reviewed"])
    elif change == "dropped_candidate":
        term["reference_candidates"].pop()
    else:
        term["reference_status"] = "REVIEWED_REFERENCE"
    with pytest.raises(ValueError):
        audit.selected_query(term, selected)


@pytest.mark.parametrize(
    "change",
    [
        "gene_assignment",
        "allele",
        "subject",
        "genome",
        "primary",
        "species",
        "version",
        "flag",
        "name",
    ],
)
def test_protein_annotations_are_not_promoted_to_source_or_subject_identity(frozen, change):
    dossier = frozen[0]["beta"]
    term = dossier["terms"]["ARO:3009476"]
    selected = dossier["names"][term["taxonomy_query_name"]]["selected_taxon"]
    protein = copy.deepcopy(dossier["proteins"]["UniProtKB:Q4WA70"])
    field, value = {
        "gene_assignment": ("source_gene_symbol_assignment", "TUB2"),
        "allele": ("exact_resistance_allele", True),
        "subject": ("experimental_subject_assignment", True),
        "genome": ("experimental_genome_assignment", "genome"),
        "primary": ("database_review_status_is_primary_results_review", True),
        "species": ("reference_species_taxon_id", "NCBITaxon:1"),
        "version": ("sequence_version", True),
        "flag": ("native_protein_flag", "Complete"),
        "name": ("native_beta_name_matches", []),
    }[change]
    protein[field] = value
    with pytest.raises(ValueError):
        audit.protein_identity("UniProtKB:Q4WA70", protein, term["reference_candidates"][0], selected, True)


@pytest.mark.parametrize(
    "change",
    [
        "missing_protein",
        "submission_subject",
        "lost_reference",
        "corrected_doi",
        "source_query",
        "summary",
        "article_obtained",
        "paywall",
        "retry",
        "paper_invalidated",
        "citation_borrowing",
    ],
)
def test_bibliography_and_access_metadata_cannot_become_primary_evidence(inputs, change):
    data, plan, _ = inputs
    followup = data["bibliography"]
    if change == "missing_protein":
        del followup["proteins"]["UniProtKB:P53373"]
    elif change == "submission_subject":
        followup["proteins"]["UniProtKB:P53373"]["reference_rows"][0]["experimental_subject_assignment"] = (
            True
        )
    elif change == "lost_reference":
        followup["proteins"]["UniProtKB:P53373"]["reference_rows"].pop()
    elif change == "corrected_doi":
        row = followup["proteins"]["UniProtKB:I7EZ98"]["reference_rows"][6]
        next(i for i in row["identifiers"] if i["database"] == "DOI")["id"] = "10.1094/PDIS-09-17-1516-RE"
    elif change == "source_query":
        followup["proteins"]["UniProtKB:P53373"]["source"]["url"] = "different"
    elif change == "summary":
        followup["summary"]["native_reference_memberships"] += 1
    elif change in {"article_obtained", "paywall", "retry"}:
        field = {
            "article_obtained": "article_obtained",
            "paywall": "paywall_inferred",
            "retry": "retry_or_alternate_route_performed",
        }[change]
        followup["banno_followup"]["access_hold"][field] = True
    elif change == "paper_invalidated":
        followup["banno_followup"]["prior_uniprot_citation_query"]["paper_invalidated_by_zero_result"] = True
    else:
        followup["terms"]["ARO:3009431"]["source_definition_citations"] = ["PMID:18944187"]
    with pytest.raises(ValueError):
        audit.check_bibliography(data, plan)


@pytest.mark.parametrize(
    "change", ["missing_row", "count", "phi", "curator", "scores", "primary", "accessions"]
)
def test_all_record_accounting_cannot_drop_or_reclassify_other_evidence(inputs, change):
    data = inputs[0]
    if change == "missing_row":
        data["base_rows"].pop()
    else:
        field = {
            "count": "card_assertions",
            "phi": "phi_claims_not_reassessed",
            "curator": "curator_claims_not_reassessed",
            "scores": "score_rules_not_reassessed",
            "primary": "whole_record_primary_review",
            "accessions": "selected_reference_accessions",
        }[change]
        data["base_rows"][0][field] = "COMPLETE" if change == "primary" else "999999"
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.fixture
def outputs(tmp_path, monkeypatch):
    prefix = str(tmp_path / "index")
    monkeypatch.setattr(audit, "PREFIX", prefix)
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, []))
    monkeypatch.setattr(audit.registry, "render", lambda *args: (b"json", b"tsv"))
    monkeypatch.setattr(sys, "argv", ["audit"])
    return Path(prefix + ".json"), Path(prefix + ".tsv")


def test_check_mode_cannot_recreate_a_concurrently_deleted_file(outputs, monkeypatch):
    first, second = outputs
    first.write_bytes(b"json")
    second.write_bytes(b"tsv")
    original = Path.read_bytes

    def read_then_delete(path):
        value = original(path)
        if path == second:
            first.unlink()
        return value

    monkeypatch.setattr(Path, "read_bytes", read_then_delete)
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    audit.main()
    assert not first.exists()


def test_competing_creation_is_not_skipped_or_overwritten(outputs, monkeypatch):
    first, second = outputs
    second.write_bytes(b"tsv")
    original = Path.read_bytes

    def read_then_create(path):
        value = original(path)
        if path == second:
            first.write_bytes(b"competing")
        return value

    monkeypatch.setattr(Path, "read_bytes", read_then_create)
    with pytest.raises(FileExistsError):
        audit.main()
    assert original(first) == b"competing"


@pytest.mark.parametrize("check", [False, True])
def test_both_checkpoints_are_validated_before_any_write(outputs, monkeypatch, check):
    first, second = outputs
    second.write_bytes(b"historical")
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    with pytest.raises((ValueError, FileNotFoundError)):
        audit.main()
    assert not first.exists() and second.read_bytes() == b"historical"

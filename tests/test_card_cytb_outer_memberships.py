"""Preserve every claim and distinct evidence kind in the eleven-cohort index."""

import copy
import json
import socket
import sys
from collections import Counter
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_cytb_outer_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.prior.prior.prior.read_inputs(ROOT, audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def resolve(data, pointer):
    value = data[pointer["input"]]
    for part in pointer["pointer"].split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def test_full_corpus_partition_and_candidate_counts(frozen):
    result, rows = audit.project(*frozen)
    expected = {
        "corpus_records": 2939,
        "card_terms": 2002,
        "card_assertions": 4538,
        "selected_reference_terms": 1275,
        "selected_reference_proteins": 1676,
        "reference_links": 2791,
        "records_with_selected_references": 223,
        "added_reference_terms": 16,
        "added_reference_proteins": 130,
        "added_reference_links": 133,
        "additional_evidence_for_existing_links": 1,
        "whole_record_primary_signoffs": 0,
    }
    assert all(result["summary"][k] == v for k, v in expected.items())
    assert result["summary"]["term_statuses"][audit.UNSELECTED] == 727
    assert result["summary"]["claim_statuses"][audit.UNSELECTED] == 1313
    assert result["summary"]["term_statuses"][audit.MIXED] == 2
    assert result["summary"]["claim_statuses"][audit.MIXED] == 6
    direct_terms = {
        tid
        for tid, term in result["terms"].items()
        if any(link["kind"] == audit.registry.DIRECT for link in term["links"])
    }
    assert len(direct_terms) == 978
    assert sum(c["aro_id"] in direct_terms for c in result["claims"]) == 2549
    assert len(rows) == 2939
    assert all(sum(row[col] for col in audit.COLUMNS.values()) == row["card_assertions"] for row in rows)
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)
    assert sum(row["phi_claims_not_reassessed"] for row in rows) == 217
    assert sum(row["curator_claims_not_reassessed"] for row in rows) == 133
    assert sum(row["score_rules_not_reassessed"] for row in rows) == 467
    assert all(
        len(t["links"]) == len({link["protein_accession"] for link in t["links"]})
        for t in result["terms"].values()
    )


def test_all_inherited_and_new_pointers_resolve(frozen):
    result, _ = audit.project(*frozen)

    def check(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                resolve(frozen[0], value)
            else:
                for item in value.values():
                    check(item)
        elif isinstance(value, list):
            for item in value:
                check(item)

    check(result)
    assert result["limits"] == frozen[0]["base"]["limits"]
    touched = set(frozen[0]["cytb"]["terms"]) | set(frozen[0]["outer"]["terms"])
    for tid, old in frozen[0]["base"]["terms"].items():
        if tid in touched:
            continue
        expected = audit.rebase(old, "terms", tid)
        if expected["reference_status"] == audit.prior.UNSELECTED:
            expected["reference_status"] = audit.UNSELECTED
        assert result["terms"][tid] == expected
    for old, new in zip(frozen[0]["base"]["claims"], result["claims"], strict=True):
        assert {**new, "reference_status": old["reference_status"]} == old


def test_same_accession_has_two_evidence_sources_not_two_candidates(frozen):
    result, _ = audit.project(*frozen)
    term = result["terms"]["ARO:3004122"]
    assert term["reference_status"] == audit.MIXED
    assert {r["protein_accession"] for r in term["links"]} == {
        "UniProtKB:O87754",
        "UniProtKB:S5UCA2",
        "UniProtKB:S5UDN6",
    }
    direct = next(r for r in term["links"] if r["protein_accession"] == "UniProtKB:O87754")
    extra = direct["additional_reference_evidence"]
    assert len(extra) == 1 and extra[0]["kind"] == audit.OUTER_UNREVIEWED
    original = audit.rebase(
        frozen[0]["base"]["terms"]["ARO:3004122"]["links"][0], "terms", "ARO:3004122", "links", 0
    )
    assert {k: v for k, v in direct.items() if k != "additional_reference_evidence"} == original
    assert (
        result["proteins"]["UniProtKB:O87754"]["identity"]
        == frozen[0]["base"]["proteins"]["UniProtKB:O87754"]["identity"]
    )
    assert len(result["proteins"]["UniProtKB:O87754"]["sources"]) == 2


def test_distinct_native_accessions_are_not_equated_or_replaced(frozen):
    result, _ = audit.project(*frozen)
    links = result["terms"]["ARO:3004123"]["links"]
    assert [r["protein_accession"] for r in links] == ["UniProtKB:A0A069BCC8", "UniProtKB:Q7WZL2"]
    assert links[0]["kind"] == audit.registry.DIRECT
    assert links[1]["kind"] == audit.OUTER_UNREVIEWED
    assert all(not r.get("additional_reference_evidence") for r in links)
    assert result["proteins"]["UniProtKB:Q7WZL2"]["protein_description_flag"] == "Fragment"


def test_subtype_exclusions_complexes_and_zero_hits_are_preserved(frozen):
    result, _ = audit.project(*frozen)
    source = frozen[0]["outer"]
    excluded = source["terms"]["ARO:3000464"]["query_hits_not_assigned_to_source_subtype"]
    links = result["terms"]["ARO:3000464"]["links"]
    assert len(excluded) == 75 and len(links) == 70
    assert not {r["protein_accession"] for r in excluded} & {r["protein_accession"] for r in links}
    for tid in ("ARO:3004128", "ARO:3004578"):
        assert result["terms"][tid]["links"] == []
        assert result["terms"][tid]["outer_reference_disposition"] == "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"
    for tid, term in source["terms"].items():
        if term["source_organism_name"] is None:
            assert result["terms"][tid]["links"] == []
            assert result["terms"][tid]["outer_reference_disposition"] == term["entity_scope"]
    assert "UniProtKB:A0A0J9X1Q5" not in result["proteins"]


def test_primary_context_and_access_hold_do_not_assign_experiments(frozen):
    result, _ = audit.project(*frozen)
    context = resolve(frozen[0], result["outer_evidence_context"])
    assert context["study_genome"]["accession"] == "CP005927"
    assert context["resistance_gene_accession_assigned"] is None
    assert context["current_taxon_id_assigned_from_paper"] is None
    assert context["study_genome"]["independently_verified"] is False
    hold = resolve(frozen[0], result["cytb_supplement_access_hold"])
    assert hold["http_status"] == 403
    assert hold["primary_xml_obtained_before_hold"] is True
    assert hold["retry_or_alternate_route_performed"] is False
    for term in result["terms"].values():
        assert term["experimental_subject_assignment"] is False
        assert term["whole_record_primary_review"] == "OPEN"
    assert Counter(p.get("protein_description_flag") for p in result["proteins"].values())["Precursor"] >= 27


@pytest.mark.parametrize(
    "field,value",
    [
        ("full_corpus_goal_status", "COMPLETE"),
        ("ncbi_requests", 1),
        ("issue_1040", "RESUMED"),
        ("reuse_terms_review_resumed", True),
        ("experimental_allele_or_genome_assignments", 1),
    ],
)
def test_limits_cannot_be_promoted(inputs, field, value):
    inputs[0]["base"]["limits"][field] = value
    with pytest.raises(ValueError, match="limits changed"):
        audit.project(*inputs)


@pytest.mark.parametrize("name", ["cytb", "outer"])
@pytest.mark.parametrize(
    "change", ["missing", "label", "claim_position", "claim_hash", "record", "source_pin"]
)
def test_complete_cohort_and_memberships_required(inputs, name, change):
    d = inputs[0][name]
    if change == "missing":
        d["terms"].pop(next(iter(d["terms"])))
    elif change == "label":
        next(iter(d["terms"].values()))["source_label"] = "Other"
    elif change == "claim_position":
        d["claims"][0]["position"] = -1
    elif change == "claim_hash":
        d["claims"][0]["claim_sha256"] = "changed"
    elif change == "record":
        d["records"].pop()
    else:
        d["inputs"]["census"]["sha256"] = "changed"
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("field", ["entry_version", "sequence_version", "reference_taxon_id"])
def test_shared_accession_metadata_must_agree(inputs, field):
    row = inputs[0]["outer"]["proteins"]["UniProtKB:O87754"]
    row[field] = row[field] + 1 if isinstance(row[field], int) else "NCBITaxon:1"
    with pytest.raises(ValueError, match="identity conflict"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change", ["url", "incomplete", "count", "duplicate", "assignment", "taxon", "subtype", "old_link"]
)
def test_candidate_scope_guards(inputs, change):
    d = inputs[0]["outer"]
    term = d["terms"]["ARO:3000464"]
    query = term["queries"]["unreviewed"]
    candidate = term["reference_candidates"][0]
    protein = d["proteins"][candidate["protein_accession"]]
    if change == "url":
        query["source"]["url"] = "https://example.org"
    elif change == "incomplete":
        query["complete_for_query"] = False
    elif change == "count":
        query["result_count"] += 1
    elif change == "duplicate":
        term["reference_candidates"].append(copy.deepcopy(candidate))
    elif change == "assignment":
        candidate["exact_resistant_allele"] = True
    elif change == "taxon":
        protein["reference_species_taxon_id"] = "NCBITaxon:1"
    elif change == "subtype":
        protein["protein_names"] = [{"kind": "recommendedName", "value": "Outer membrane protein IA"}]
    else:
        d["terms"]["ARO:3004123"]["prior_reference_links"] = []
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_nohit_cannot_gain_unrelated_literature_hit(inputs):
    term = inputs[0]["outer"]["terms"]["ARO:3004128"]
    term["reference_candidates"] = [{"protein_accession": "UniProtKB:A0A0J9X1Q5"}]
    with pytest.raises(ValueError, match="membership changed"):
        audit.project(*inputs)


def test_prior_tsv_accessions_are_checked(inputs):
    inputs[0]["base_rows"][0]["selected_reference_accessions"] = "UniProtKB:P00000"
    with pytest.raises(ValueError, match="reference accessions changed"):
        audit.project(*inputs)


def test_unbound_protein_rejected(inputs):
    d = inputs[0]["outer"]
    d["proteins"]["UniProtKB:P00000"] = copy.deepcopy(next(iter(d["proteins"].values())))
    with pytest.raises(ValueError, match="unbound reference"):
        audit.project(*inputs)


def test_duplicate_evidence_not_counted_twice():
    link = {"protein_accession": "UniProtKB:P00000", "kind": audit.OUTER_UNREVIEWED}
    target = {"links": [{"protein_accession": "UniProtKB:P00000", "kind": audit.registry.DIRECT}]}
    audit.merge_link(target, link)
    assert len(target["links"]) == 1 and target["reference_status"] == audit.MIXED
    with pytest.raises(ValueError, match="duplicate new"):
        audit.merge_link(target, link)


def test_saved_files_reproduce_without_ignored_request_caches(frozen):
    result, rows = audit.project(*frozen)
    for suffix, payload in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == payload


def test_cli_check_mode_and_pair_validation(tmp_path, monkeypatch):
    prefix = str(tmp_path / "index")
    monkeypatch.setattr(audit, "PREFIX", prefix)
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, [{"id": "test"}]))
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not list(tmp_path.iterdir())
    monkeypatch.setattr(sys, "argv", ["audit"])
    Path(prefix + ".tsv").write_text("different\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert not Path(prefix + ".json").exists()
    Path(prefix + ".tsv").unlink()
    audit.main()
    audit.main()
    assert json.loads(Path(prefix + ".json").read_bytes()) == {"summary": {}}

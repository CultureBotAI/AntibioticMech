"""Public, network-blocked reconciliation preserves every evidence boundary."""

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
import audit_card_fungal_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in offline reconciliation")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture(scope="module")
def frozen():
    # Only public snapshots, with no native response cache or biological record reads.
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    data = {}
    for name, pin in plan["inputs"].items():
        if name in {"source_inventory", "source_queue"}:
            continue
        path = audit.reference.check_pin(ROOT, pin)
        data[name] = (
            audit.progress.read_tsv(path.read_bytes())
            if path.suffix == ".tsv"
            else json.loads(path.read_bytes())
        )
    return data, plan, audit.reference.pin(ROOT, ROOT / audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def test_public_reproduction_and_all_record_accounting(frozen):
    result, rows = audit.project(*frozen)
    for suffix, payload in zip((".json", ".tsv"), audit.prior.prior.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == payload
    summary = result["summary"]
    assert summary["corpus_records"] == len(rows) == 2939
    assert summary["card_terms"] == 2002
    assert summary["card_assertions"] == len(result["claims"]) == 4538
    assert summary["selected_reference_terms"] == 1226
    assert summary["selected_reference_proteins"] == 1444
    assert summary["reference_links"] == 2504
    assert summary["added_reference_terms"] == 146
    assert summary["added_reference_proteins"] == 248
    assert summary["added_reference_links"] == 1276
    assert summary["fungal_source_terms"] == 184 and summary["fungal_source_claims"] == 188
    assert summary["term_statuses"][audit.UNSELECTED] == 776
    assert summary["claim_statuses"][audit.UNSELECTED] == 1410
    assert summary["records_with_selected_references"] == 215
    assert summary["unreviewed_fragment_references"] == 211
    assert summary["phi_claims_not_reassessed"] == 217
    assert summary["curator_claims_not_reassessed"] == 133
    assert summary["score_rules_not_reassessed"] == 467
    assert summary["whole_record_primary_signoffs"] == 0
    assert summary["fungal_followup_dispositions"] == {
        "MULTIPLE_CANDIDATES_NO_SELECTION": 61,
        audit.ZERO: 29,
        "REVIEWED_REFERENCE": 68,
        audit.UNRESOLVED: 9,
        "UNREVIEWED_CANDIDATE": 17,
    }
    assert all(
        sum(row[column] for column in audit.COLUMNS.values()) == row["card_assertions"] for row in rows
    )
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)
    assert result["limits"] == frozen[0]["base"]["limits"]
    old_claims = frozen[0]["base"]["claims"]
    for old, new in zip(old_claims, result["claims"], strict=True):
        assert {k: v for k, v in old.items() if k != "reference_status"} == {
            k: v for k, v in new.items() if k != "reference_status"
        }


def resolve(data, pointer):
    value = data[pointer["input"]]
    for part in pointer["pointer"].split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def test_provenance_resolves_and_inherited_metadata_is_preserved(frozen):
    result, _ = audit.project(*frozen)
    data = frozen[0]

    def check(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                resolve(data, value)
            else:
                for v in value.values():
                    check(v)
        elif isinstance(value, list):
            for v in value:
                check(v)

    check(result)
    fungal_terms = set(data["demethylase"]["terms"]) | set(data["glucan"]["terms"])
    for tid, term in data["base"]["terms"].items():
        expected = audit.rebase(term, "terms", tid)
        if expected["reference_status"] == audit.prior.UNSELECTED:
            expected["reference_status"] = audit.UNSELECTED
        if tid not in fungal_terms:
            assert result["terms"][tid] == expected
    for accession, old in data["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)
    assert Counter(t["entity_review"] for t in result["terms"].values()) == Counter(
        t["entity_review"] for t in data["base"]["terms"].values()
    )
    for tid in fungal_terms:
        for link in result["terms"][tid]["links"]:
            assert (
                link["experimental_subject_assignment"]
                is link["exact_allele_assignment"]
                is link["explicit_card_xref"]
                is False
            )
            assert link["source_citation_ids"] == link["matched_reference_numbers"] == []
            assert resolve(data, link["source"])["protein_accession"] == link["protein_accession"]


def test_pointer_escaping_and_rebasing():
    old = {"a/b~c": [{"input": "old", "pointer": "/anything"}]}
    pointer = audit.rebase(old, "terms")["a/b~c"][0]
    assert pointer == {"input": "base", "pointer": "/terms/a~1b~0c/0"}
    assert resolve({"base": {"terms": old}}, pointer) == old["a/b~c"][0]


def test_projection_needs_no_filesystem_after_public_inputs_are_loaded(frozen, monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("filesystem access forbidden during public projection")

    monkeypatch.setattr(Path, "read_bytes", forbidden)
    monkeypatch.setattr(Path, "read_text", forbidden)
    result, rows = audit.project(*frozen)
    assert len(rows) == 2939 and len(result["claims"]) == 4538


@pytest.mark.parametrize("change", ["digest", "label", "ambiguous", "missing"])
def test_frozen_source_selection_binding(inputs, change):
    source = inputs[0]["direct_candidates"]
    tid = next(iter(source["determinants"]))
    if change == "digest":
        source["source_inventory_sha256"] = "different"
    elif change == "label":
        source["determinants"][tid]["labels"] = ["different"]
    elif change == "ambiguous":
        source["determinants"][tid]["labels"].append("different")
    else:
        source["determinants"].pop(tid)
    with pytest.raises(ValueError, match="source label"):
        audit.project(*inputs)


def test_multiplicity_unresolved_names_and_source_spelling(frozen):
    result, _ = audit.project(*frozen)
    data = frozen[0]
    fsk = [tid for tid, t in data["glucan"]["terms"].items() if t["source_gene_label"] == "FSK1"]
    assert len(fsk) == 5
    assert all(
        result["terms"][tid]["fungal_query_disposition"] == audit.ZERO and not result["terms"][tid]["links"]
        for tid in fsk
    )
    many = [
        tid
        for tid, t in data["demethylase"]["terms"].items()
        if t["source_organism_name"] == "Zymoseptoria tritici"
    ]
    assert many and all(len(result["terms"][t]["links"]) == 71 for t in many)
    assert not result["terms"]["ARO:3007524"]["links"]
    assert result["terms"]["ARO:3007524"]["fungal_query_disposition"] == audit.UNRESOLVED
    n = data["glucan"]["names"]["Nakaseomyces glabratus"]
    assert n["status"] == "PRIMARY_NOMENCLATURE_PLUS_NATIVE_REFERENCE"
    assert n["native_match_name"] == "Candida glabrata"


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_label", "wrong"),
        ("source_label_sha256", "wrong"),
        ("source_gene_label", "different"),
        ("source_claim_wording", "different"),
        ("source_organism_name", "different"),
        ("record_memberships", []),
        ("named_reference_taxon_id", "NCBITaxon:1"),
        ("reference_candidates", []),
        ("exact_allele_assignment", True),
        ("experimental_subject_assignment", True),
        ("experimental_genome_assignment", "GCA_000001"),
        ("primary_review_status", "DONE"),
        ("reference_status", "REVIEWED_REFERENCE"),
    ],
)
def test_term_guards(inputs, cohort, field, value):
    terms = inputs[0][cohort]["terms"]
    term = next(t for t in terms.values() if len(t["reference_candidates"]) > 1)
    term[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("entry_version", 0),
        ("sequence_version", True),
        ("entry_type", "unknown"),
        ("reference_species_taxon_id", "NCBITaxon:1"),
        ("reference_taxon_rank", ""),
        ("species_lineage_verified", False),
        ("exact_resistance_allele", True),
        ("experimental_subject_assignment", True),
        ("experimental_genome_assignment", "genome"),
        ("database_review_status_is_primary_results_review", True),
        ("resistance_inferred_from_reference", True),
        ("unflagged_means_complete", True),
        ("native_protein_flag", "unknown"),
        ("genes", []),
    ],
)
def test_protein_guards(inputs, cohort, field, value):
    next(iter(inputs[0][cohort]["proteins"].values()))[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


def positive_context(data, cohort):
    key = "gene_contexts" if cohort == "demethylase" else "query_contexts"
    return next(c for c in data[cohort][key].values() if c["reference_candidates"])


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("complete_for_query", False),
        ("zero_hit_is_biological_absence", True),
        ("result_count", 9999),
        ("accessions", ["duplicate", "duplicate"]),
        ("reviewed_subset", 1),
        ("species_id", True),
        ("suggestions_followed", True),
    ],
)
def test_query_guards(inputs, cohort, field, value):
    context = positive_context(inputs[0], cohort)
    context["queries"]["reviewed"][field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize("target", ["terms", "proteins", "claims", "records"])
def test_dropped_membership_rejected(inputs, cohort, target):
    rows = inputs[0][cohort][target]
    rows.pop(next(iter(rows))) if isinstance(rows, dict) else rows.pop()
    with pytest.raises((ValueError, KeyError)):
        audit.project(*inputs)


@pytest.mark.parametrize("cohort", audit.COHORTS)
@pytest.mark.parametrize(("field", "value"), [("position", 999), ("claim_sha256", "different")])
def test_claim_binding(inputs, cohort, field, value):
    inputs[0][cohort]["claims"][0][field] = value
    with pytest.raises(ValueError, match="claim position or content"):
        audit.project(*inputs)


def test_orf_only_match_is_not_a_gene_alias(inputs):
    protein = next(iter(inputs[0]["demethylase"]["proteins"].values()))
    for block in protein["genes"]:
        block["orfNames"] += block["geneName"] + block["synonyms"]
        block["geneName"] = block["synonyms"] = []
    with pytest.raises(ValueError, match="native gene-name"):
        audit.project(*inputs)


def test_fallback_requires_reviewed_zero_hits(inputs):
    context = positive_context(inputs[0], "demethylase")
    assert "unreviewed" in context["queries"]
    query = context["queries"]["reviewed"]
    query["accessions"], query["result_count"] = ["P00001"], 1
    with pytest.raises(ValueError, match="fallback"):
        audit.project(*inputs)


def test_cross_cohort_protein_conflict(inputs):
    data = inputs[0]
    accession, protein = next(iter(data["demethylase"]["proteins"].items()))
    identity = audit.prior.prior.reference_identity({**protein, "exact_allele_assignment": False})
    identity["entry_version"] += 1
    data["base"]["proteins"][accession] = {
        "identity": identity,
        "sources": [],
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    with pytest.raises(ValueError, match="conflicting cross-cohort"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "field", ["phi_claims_not_reassessed", "curator_claims_not_reassessed", "score_rules_not_reassessed"]
)
def test_non_card_source_counts_are_not_changed(inputs, field):
    inputs[0]["base_rows"][0][field] = "999"
    with pytest.raises(ValueError, match="unreassessed source"):
        audit.project(*inputs)


def test_unknown_query_and_duplicate_context_term_rejected(inputs):
    context = positive_context(inputs[0], "glucan")
    inputs[0]["glucan"]["query_contexts"]["unused"] = copy.deepcopy(context)
    with pytest.raises(ValueError, match="unbound fungal query"):
        audit.project(*inputs)
    del inputs[0]["glucan"]["query_contexts"]["unused"]
    context = next(iter(inputs[0]["glucan"]["source_contexts"].values()))
    context["terms"].append(context["terms"][0])
    with pytest.raises(ValueError, match="duplicate"):
        audit.project(*inputs)

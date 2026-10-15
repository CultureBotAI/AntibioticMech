"""Successor references preserve source scopes, multiplicity and frozen public replay."""

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
import audit_card_topoisomerase_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in offline reference reconciliation")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture(scope="module")
def frozen():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    data = {}
    # Immutable public snapshots only: no ignored responses or mutable biological records.
    for key in ("base", "reviewed", "unreviewed", "salmonella", "curator", "census", "ledger"):
        path = audit.reference.check_pin(ROOT, plan["inputs"][key])
        data[key] = (
            audit.progress.read_tsv(path.read_bytes())
            if path.suffix == ".tsv"
            else json.loads(path.read_bytes())
        )
    return data, plan, audit.reference.pin(ROOT, ROOT / audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def test_frozen_public_reproduction_and_all_record_accounting(frozen):
    result, rows = audit.project(*frozen)
    for suffix, payload in zip((".json", ".tsv"), audit.prior.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == payload
    summary = result["summary"]
    assert summary["corpus_records"] == len(rows) == len({r["identifier"] for r in rows}) == 2939
    assert summary["card_assertions"] == len(result["claims"]) == 4538
    assert summary["card_terms"] == 2002
    assert summary["selected_reference_terms"] == 1080
    assert summary["selected_reference_proteins"] == 1196
    assert summary["reference_links"] == 1228
    assert summary["added_reference_terms"] == 53
    assert summary["added_reference_proteins"] == 150
    assert summary["added_reference_links"] == 172
    assert summary["unreviewed_fragment_references"] == 42
    assert summary["phi_claims_not_reassessed"] == 217
    assert summary["curator_claims_not_reassessed"] == 133
    assert summary["score_rules_not_reassessed"] == 467
    assert summary["whole_record_primary_signoffs"] == 0
    assert summary["claim_statuses"] == {
        audit.prior.DIRECT: 2549,
        audit.prior.CITATION: 131,
        audit.REVIEWED: 190,
        audit.UNREVIEWED: 112,
        audit.UNSELECTED: 1556,
    }
    assert summary["term_statuses"] == {
        audit.prior.DIRECT: 978,
        audit.prior.CITATION: 49,
        audit.REVIEWED: 37,
        audit.UNREVIEWED: 16,
        audit.UNSELECTED: 922,
    }
    assert all(sum(r[column] for column in audit.COLUMNS.values()) == r["card_assertions"] for r in rows)
    assert all(r["whole_record_primary_review"] == "OPEN" for r in rows)
    assert {c["record_identifier"] for c in result["claims"]} <= {r["identifier"] for r in rows}
    old = frozen[0]["base"]
    stable = (
        "record_identifier",
        "record_path",
        "standard_inchi_key",
        "resistance_index",
        "aro_id",
        "claim_sha256",
    )
    assert [[c[k] for k in stable] for c in result["claims"]] == [
        [c[k] for k in stable] for c in old["claims"]
    ]
    assert all(c["experimental_subject_assignment"] is False for c in result["claims"])


def test_all_provenance_pointers_resolve_and_base_links_keep_scope(frozen):
    data, *_ = frozen
    result, _ = audit.project(*frozen)

    def check(value):
        if isinstance(value, list):
            for item in value:
                check(item)
        elif isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                source = data[value["input"]]
                for component in value["pointer"].split("/")[1:]:
                    source = source[int(component)] if isinstance(source, list) else source[component]
            else:
                for item in value.values():
                    check(item)

    check(result)
    for tid, term in data["base"]["terms"].items():
        for old, current in zip(term["links"], result["terms"][tid]["links"], strict=bool(term["links"])):
            assert {k: v for k, v in old.items() if k != "source"} == {
                k: v for k, v in current.items() if k != "source"
            }
    for tid in data["reviewed"]["terms"]:
        for link in result["terms"][tid]["links"]:
            assert link["explicit_card_xref"] is False
            assert link["exact_allele_assignment"] is False
            assert link["experimental_subject_assignment"] is False
            assert link["source_citation_ids"] == link["matched_reference_numbers"] == []


def test_salmonella_successor_and_multiple_unreviewed_entries_are_not_dropped(frozen):
    data, *_ = frozen
    result, _ = audit.project(*frozen)
    assert len(data["salmonella"]["terms"]) == 4
    for tid in data["salmonella"]["terms"]:
        term = result["terms"][tid]
        assert term["qualified_scope_followup"] == audit.pointer("salmonella", f"/terms/{tid}")
        assert term["links"] == [] and term["reference_status"] == audit.UNSELECTED
    groups = data["unreviewed"]["shared_symbol_in_same_proteome"]
    assert len(groups) == 1
    assert all("UniProtKB:" + a in result["proteins"] for g in groups for a in g["accessions"])
    fragments = [p for p in result["proteins"].values() if p.get("protein_description_flag") == "Fragment"]
    assert len(fragments) == 42 and all(p["unflagged_means_complete"] is False for p in fragments)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_label_sha256", "changed"),
        ("source_gene_symbol", "different"),
        ("source_species_taxon_id", "NCBITaxon:10"),
        ("exact_allele_assignment", True),
        ("experimental_assignment", True),
        ("primary_review_status", "DONE"),
        ("record_ids", []),
        ("source_assertion_memberships", 1),
    ],
)
def test_reviewed_term_guards(inputs, field, value):
    inputs[0]["reviewed"]["terms"]["ARO:3003294"][field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_label_sha256", "changed"),
        ("source_gene_symbol", "different"),
        ("source_species_taxon_id", "NCBITaxon:10"),
        ("exact_allele_assignment", True),
        ("experimental_subject_assignment", True),
        ("primary_review_status", "DONE"),
        ("reviewed_candidates", ["unexpected"]),
        ("unreviewed_candidates", []),
    ],
)
def test_unreviewed_term_guards(inputs, field, value):
    inputs[0]["unreviewed"]["terms"]["ARO:3003297"][field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("cohort", ["reviewed", "unreviewed"])
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("query", "wrong"),
        ("url", "https://example.org/"),
        ("status", 500),
        ("release", "different"),
        ("zero_hit_is_absence", True),
        ("accessions", ["duplicated", "duplicated"]),
    ],
)
def test_query_guards(inputs, cohort, field, value):
    next(iter(inputs[0][cohort]["queries"].values()))[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize("cohort", ["reviewed", "unreviewed"])
@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("entry_type", "unknown"),
        ("entry_version", True),
        ("sequence_version", 0),
        ("reference_taxon_id", "NCBITaxon:0"),
        ("reference_taxon_rank", ""),
        ("protein_accession", "UniProtKB:OTHER"),
        ("source_species_taxon_id", "NCBITaxon:10"),
        ("species_lineage_verified", False),
        ("gene_names", []),
        ("exact_resistance_allele", True),
        ("experimental_subject_assignment", True),
    ],
)
def test_protein_identity_guards(inputs, cohort, field, value):
    key = "reference_proteins" if cohort == "reviewed" else "unreviewed_proteins"
    next(iter(inputs[0][cohort][key].values()))[field] = value
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change",
    [
        "membership",
        "missing_term",
        "missing_no_hit_term",
        "orphan_query",
        "orphan_protein",
        "fragment",
        "complete",
        "genome_assignment",
        "proteome_taxon",
        "assembly",
        "species_rank",
        "species_other_name",
        "species_active",
        "species_ambiguous",
        "salmonella_allele",
        "salmonella_species",
        "salmonella_gene",
        "salmonella_memberships",
        "base_xref",
        "base_allele",
        "base_term_promotion",
        "duplicate_claim",
        "claim_path",
        "claim_structure",
        "source_pin",
        "prior_dossier_pin",
        "census_pin",
        "curator_count",
        "duplicate_census",
        "plan_scope",
    ],
)
def test_crosswalk_and_scope_failures(inputs, change):
    data, plan, _ = inputs
    r, u, b = (data[k] for k in ("reviewed", "unreviewed", "base"))
    protein = next(p for p in u["unreviewed_proteins"].values() if p["proteome_links"])
    species = r["source_name_taxonomy"]["Escherichia coli"]["exact_candidates"]
    salmonella = next(iter(data["salmonella"]["terms"].values()))
    if change == "membership":
        r["memberships"].pop()
    elif change == "missing_term":
        r["terms"].pop("ARO:3003294")
    elif change == "missing_no_hit_term":
        u["terms"].pop("ARO:3003297")
    elif change == "orphan_query":
        r["queries"]["orphan"] = copy.deepcopy(next(iter(r["queries"].values())))
    elif change == "orphan_protein":
        u["unreviewed_proteins"]["orphan"] = copy.deepcopy(protein)
    elif change == "fragment":
        protein["protein_description_flag"] = "Complete"
    elif change == "complete":
        protein["unflagged_means_complete"] = True
    elif change == "genome_assignment":
        protein["proteome_links"][0]["experimental_genome_assignment"] = True
    elif change == "proteome_taxon":
        protein["proteome_links"][0]["reference_taxon_matches"] = False
    elif change == "assembly":
        protein["proteome_links"][0]["reference_assembly_id"] = "wrong"
    elif change == "species_rank":
        species[0]["rank"] = "genus"
    elif change == "species_other_name":
        species[0]["other_name_match_only"] = True
    elif change == "species_active":
        species[0]["active"] = False
    elif change == "species_ambiguous":
        species.append(copy.deepcopy(species[0]))
    elif change == "salmonella_allele":
        salmonella["exact_allele_assignment"] = True
    elif change == "salmonella_species":
        salmonella["experimental_subject_taxon_id"] = "NCBITaxon:10"
    elif change == "salmonella_gene":
        salmonella["gene"] = "wrong"
    elif change == "salmonella_memberships":
        salmonella["record_ids"] = []
    elif change == "base_xref":
        next(t for t in b["terms"].values() if t["links"])["links"][0]["kind"] = audit.REVIEWED
    elif change == "base_allele":
        next(iter(b["proteins"].values()))["exact_allele_assignment"] = True
    elif change == "base_term_promotion":
        next(iter(b["terms"].values()))["experimental_subject_assignment"] = True
    elif change == "duplicate_claim":
        b["claims"].append(copy.deepcopy(b["claims"][0]))
    elif change == "claim_path":
        b["claims"][0]["record_path"] = "wrong"
    elif change == "claim_structure":
        b["claims"][0]["standard_inchi_key"] = "wrong"
    elif change == "source_pin":
        r["inputs"]["source_reference_audit"]["sha256"] = "wrong"
    elif change == "prior_dossier_pin":
        u["inputs"]["prior_dossier"]["sha256"] = "wrong"
    elif change == "census_pin":
        data["curator"]["census"]["sha256"] = "wrong"
    elif change == "curator_count":
        data["curator"]["claims"] *= 100
    elif change == "duplicate_census":
        data["census"].append(copy.deepcopy(data["census"][0]))
    else:
        plan["constraints"]["experimental_assignments"] = True
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_shared_reference_never_transfers_explicit_card_xref(inputs):
    data, *_ = inputs
    protein = data["reviewed"]["reference_proteins"]["P0AES4"]
    accession = protein["protein_accession"]
    identity = audit.topoisomerase_identity("P0AES4", protein, False)
    data["base"]["proteins"][accession] = {
        "identity": identity,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    result, _ = audit.project(*inputs)
    assert len(result["proteins"][accession]["sources"]) == 2
    assert all(
        link["kind"] == audit.REVIEWED and link["explicit_card_xref"] is False
        for link in result["terms"]["ARO:3003294"]["links"]
    )


def test_shared_reference_identity_conflict_rejected(inputs):
    data, *_ = inputs
    protein = data["reviewed"]["reference_proteins"]["P0AES4"]
    identity = audit.topoisomerase_identity("P0AES4", protein, False)
    identity["sequence_version"] += 1
    data["base"]["proteins"][protein["protein_accession"]] = {
        "identity": identity,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
    }
    with pytest.raises(ValueError, match="conflicting cross-cohort"):
        audit.project(*inputs)


def test_duplicate_assertions_are_not_silently_deduplicated(frozen):
    result, _ = audit.project(*frozen)
    claims = Counter((c["record_identifier"], c["aro_id"]) for c in result["claims"])
    ledger = Counter((c["identifier"], c["aro_id"]) for c in frozen[0]["ledger"])
    assert claims == ledger


@pytest.fixture
def live(monkeypatch):
    monkeypatch.setattr(audit, "owner", lambda claim: claim["source"])
    claim = {"source": "CARD", "aro_id": "ARO:1", "label": "reference-only fixture"}
    records = {"CHEBI:1": {"resistance_mechanisms": [claim, copy.deepcopy(claim)]}}
    result = {
        "claims": [
            {
                "record_identifier": "CHEBI:1",
                "resistance_index": i,
                "aro_id": "ARO:1",
                "claim_sha256": audit.prior.checksum(claim),
            }
            for i in range(2)
        ],
        "terms": {"ARO:1": {"source_label_sha256": audit.progress.digest(claim["label"].encode())}},
    }
    rows = [{"identifier": "CHEBI:1", "phi_claims_not_reassessed": 0, "curator_claims_not_reassessed": 0}]
    return records, result, rows


def test_live_duplicate_claims_retain_individual_positions(live):
    audit.check_live_claims(*live)
    assert len(live[1]["claims"]) == 2


@pytest.mark.parametrize(
    "change",
    [
        "content",
        "index",
        "label",
        "term",
        "missing",
        "extra",
        "duplicate_index",
        "source",
        "extra_record",
        "missing_row",
    ],
)
def test_live_binding_rejects_content_position_and_owner_drift(live, change):
    records, result, rows = live
    claim = records["CHEBI:1"]["resistance_mechanisms"][0]
    if change == "content":
        claim["note"] = "changed"
    elif change == "index":
        result["claims"][0]["resistance_index"] = 5
    elif change == "label":
        result["terms"]["ARO:1"]["source_label_sha256"] = "wrong"
    elif change == "term":
        claim["aro_id"] = "ARO:2"
    elif change == "missing":
        records["CHEBI:1"]["resistance_mechanisms"].pop()
    elif change == "extra":
        records["CHEBI:1"]["resistance_mechanisms"].append(copy.deepcopy(claim))
    elif change == "duplicate_index":
        result["claims"][1]["resistance_index"] = 0
    elif change == "source":
        claim["source"] = "CURATOR"
    elif change == "extra_record":
        records["CHEBI:2"] = {"resistance_mechanisms": []}
    else:
        rows.clear()
    with pytest.raises(ValueError):
        audit.check_live_claims(*live)

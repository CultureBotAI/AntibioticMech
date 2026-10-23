"""Verify curated mechanism causal_graphs across all eligible REVIEWED records."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from antibioticmech.activity_collections import load_record
from antibioticmech.causal_graphs_curation import (
    DEFAULT_PLAN_PATH,
    DEFAULT_RECEIPT_PATH,
    apply_planned_causal_graphs_to_record_data,
    load_causal_graphs_plan,
    validate_causal_edge_spec,
    validate_causal_graph_spec,
    validate_causal_node_spec,
    validate_existing_graph_entry,
    validate_held_record_entry,
    verify_reviewed_causal_graphs_accounting,
)
from scripts.score_causal_graph_quality import score_record

ROOT = Path(__file__).resolve().parents[1]


def load_transition() -> dict:
    return json.loads(DEFAULT_RECEIPT_PATH.read_bytes())


def test_reviewed_causal_graphs_accounting_and_quality_scores(records):
    accounting = verify_reviewed_causal_graphs_accounting(records)
    assert accounting == {
        "total_causal_graph_records": 52,
        "reviewed_total": 80,
        "reviewed_existing_graphs": 5,
        "reviewed_curated_graphs": 36,
        "reviewed_held": 39,
        "seeded_existing_graphs": 11,
    }

    plan = load_causal_graphs_plan(DEFAULT_PLAN_PATH)
    curated_ids = {entry["identifier"] for entry in plan["records"]}
    scored_curated = 0
    for path, doc in records:
        graphs = doc.get("causal_graphs") or []
        if not graphs:
            continue
        score = score_record(doc)
        assert score["causal_graph_score"] == 100, (
            f"{path} ({doc.get('identifier')}): expected causal graph score 100, "
            f"got {score['causal_graph_score']} with issues {score['issues']}"
        )
        assert score["issues"] == ""
        if doc.get("identifier") in curated_ids:
            scored_curated += 1
            for graph in graphs:
                assert graph.get("scope_status") == "MECHANISTIC"
                for edge in graph.get("edges") or []:
                    ev_list = edge.get("evidence") or []
                    assert ev_list, f"{path}: edge missing evidence"
                    for ev in ev_list:
                        ref = str(ev.get("reference") or "")
                        assert ref.startswith(("PMID:", "DOI:")), (
                            f"{path}: expected primary citation on edge, got {ref!r}"
                        )
                        assert ev.get("snippet") or ev.get("notes"), (
                            f"{path}: expected snippet or notes on edge citation {ref}"
                        )
    assert scored_curated == 36


def test_plan_and_transition_summary_counts():
    plan = load_causal_graphs_plan(DEFAULT_PLAN_PATH)
    receipt = load_transition()
    assert len(plan["records"]) == receipt["record_count"] == len(receipt["record_deltas"]) == 36
    assert sum(d["graphs_added"] for d in receipt["record_deltas"]) == 36
    assert sum(d["nodes_added"] for d in receipt["record_deltas"]) == 145
    assert sum(d["edges_added"] for d in receipt["record_deltas"]) == 110
    assert len(plan["existing_causal_graphs"]) == 16
    assert len(plan["held_records"]) == 39

    cohort_counts: dict[str, int] = {}
    for entry in plan["records"]:
        cohort = entry["cohort"]
        cohort_counts[cohort] = cohort_counts.get(cohort, 0) + 1
    assert cohort_counts == {
        "protein_target_with_examples": 19,
        "non_protein_direct_or_measured_target": 17,
    }


def test_strict_causal_graph_spec_validation():
    valid_protein_node = {
        "node_id": "mura",
        "label": "UDP-N-acetylglucosamine 1-carboxyvinyltransferase MurA",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Conserved bacterial MurA enzyme.",
        "gene_symbols": ["murA"],
        "protein_examples": [
            {
                "uniprot_id": "UniProtKB:P0A749",
                "protein_label": "UDP-N-acetylglucosamine 1-carboxyvinyltransferase",
                "gene_symbol": "murA",
                "taxon_id": "NCBITaxon:83333",
                "taxon_label": "Escherichia coli (strain K12)",
                "entry_status": "REVIEWED",
                "retrieved_on": "2026-04-17",
                "role": "Primary target",
            }
        ],
    }
    norm_node = validate_causal_node_spec(valid_protein_node, context="test")
    assert norm_node["node_id"] == "mura"

    with pytest.raises(ValueError, match="requires non-empty protein_examples"):
        validate_causal_node_spec(
            {k: v for k, v in valid_protein_node.items() if k != "protein_examples"},
            context="test",
        )

    with pytest.raises(ValueError, match="must not carry protein_examples"):
        validate_causal_node_spec(
            {
                "node_id": "peptidoglycan_biosynthesis",
                "label": "peptidoglycan biosynthetic process",
                "node_type": "BIOLOGICAL_PROCESS",
                "grounding": "GO:0009252",
                "protein_examples": valid_protein_node["protein_examples"],
            },
            context="test",
        )

    valid_edge = {
        "subject": "fosfomycin",
        "predicate": "directly inhibits",
        "predicate_id": "RO:0002406",
        "object": "mura",
        "description": "Fosfomycin covalently modifies Cys115 of MurA.",
        "evidence": [
            {
                "reference": "PMID:7833980",
                "snippet": "Fosfomycin covalently modifies Cys115 of MurA.",
            }
        ],
    }
    norm_edge = validate_causal_edge_spec(
        valid_edge, node_ids={"fosfomycin", "mura"}, context="test"
    )
    assert norm_edge["predicate_id"] == "RO:0002406"

    with pytest.raises(ValueError, match="self-loop"):
        validate_causal_edge_spec(
            {**valid_edge, "object": "fosfomycin"},
            node_ids={"fosfomycin", "mura"},
            context="test",
        )

    with pytest.raises(ValueError, match="invalid citation reference"):
        validate_causal_edge_spec(
            {
                **valid_edge,
                "evidence": [{"reference": "CARD:ARO:3000001", "snippet": "Not primary."}],
            },
            node_ids={"fosfomycin", "mura"},
            context="test",
        )

    valid_graph = {
        "graph_id": "fosfomycin_mura_inhibition",
        "title": "Fosfomycin inhibits MurA",
        "description": (
            "Fosfomycin irreversibly inhibits MurA, blocking peptidoglycan synthesis "
            "and causing cell lysis."
        ),
        "scope_status": "MECHANISTIC",
        "nodes": [
            {
                "node_id": "fosfomycin",
                "label": "fosfomycin",
                "node_type": "COMPOUND",
                "grounding": "CHEBI:28915",
            },
            valid_protein_node,
            {
                "node_id": "peptidoglycan_biosynthesis",
                "label": "peptidoglycan biosynthetic process",
                "node_type": "BIOLOGICAL_PROCESS",
                "grounding": "GO:0009252",
            },
            {
                "node_id": "bacterial_cell_lysis",
                "label": "bacterial cell lysis",
                "node_type": "STATE",
                "grounding_status": "REVIEWED_LABEL_ONLY",
                "grounding_notes": "Bactericidal lysis.",
            },
        ],
        "edges": [
            valid_edge,
            {
                "subject": "mura",
                "predicate": "negatively regulates",
                "predicate_id": "RO:0002212",
                "object": "peptidoglycan_biosynthesis",
                "description": "MurA inactivation halts peptidoglycan biosynthesis.",
                "evidence": [{"reference": "PMID:7833980", "snippet": "Blocks MurA step."}],
            },
            {
                "subject": "peptidoglycan_biosynthesis",
                "predicate": "causally upstream of",
                "predicate_id": "RO:0002411",
                "object": "bacterial_cell_lysis",
                "description": "Peptidoglycan arrest causes bacterial cell lysis.",
                "evidence": [{"reference": "PMID:7833980", "snippet": "Causes cell lysis."}],
            },
        ],
    }
    norm_graph = validate_causal_graph_spec(
        valid_graph, compound_id="CHEBI:28915", context="test"
    )
    assert norm_graph["graph_id"] == "fosfomycin_mura_inhibition"

    assert (
        validate_existing_graph_entry(
            {
                "identifier": "CHEBI:17698",
                "label": "chloramphenicol",
                "path": "data/antibiotics/antibacterial/chloramphenicol.yaml",
                "curation_status": "REVIEWED",
                "graph_ids": ["chloramphenicol_bacteriostatic_core"],
            }
        )
        == "CHEBI:17698"
    )

    assert (
        validate_held_record_entry(
            {
                "identifier": "CHEBI:40009",
                "label": "D-cycloserine",
                "path": "data/antibiotics/antibacterial/d-cycloserine.yaml",
                "blocker_category": "uniprot_protein_example_held",
                "target_summary": "Alr and Ddl held in uniprot_protein_examples.yaml.",
                "references": ["PMID:10637613"],
                "reason": "Held pending multi-enzyme UniProt target decomposition.",
            }
        )
        == "CHEBI:40009"
    )


@pytest.mark.parametrize("index", range(36))
def test_exact_scoped_transition_and_idempotence(pre_causal_graphs_root, index):
    plan = load_causal_graphs_plan(DEFAULT_PLAN_PATH)
    receipt = load_transition()
    delta = receipt["record_deltas"][index]
    plan_entry = plan["records"][index]
    assert delta["identifier"] == plan_entry["identifier"]

    live_path = ROOT / delta["path"]
    historical_path = pre_causal_graphs_root / delta["path"]
    assert hashlib.sha256(live_path.read_bytes()).hexdigest() == delta["after_sha256"]
    assert hashlib.sha256(historical_path.read_bytes()).hexdigest() == delta["before_sha256"]

    current = load_record(live_path)
    before = load_record(historical_path)

    _, n_graphs, n_nodes, n_edges, changed = apply_planned_causal_graphs_to_record_data(
        current, plan_entry
    )
    assert not changed
    assert (n_graphs, n_nodes, n_edges) == (0, 0, 0)

    restored = copy.deepcopy(current)
    assert restored["curation_history"].pop() == delta["added_history_event"]
    assert delta["added_history_event"]["action"] == "CURATED_CAUSAL_GRAPHS"
    assert len(restored["curation_history"]) == delta["curation_history_before_len"]
    assert restored.pop("causal_graphs", None) == delta["after_causal_graphs"]
    if delta["before_causal_graphs"] is not None:
        restored["causal_graphs"] = copy.deepcopy(delta["before_causal_graphs"])

    assert restored == before


@pytest.mark.parametrize("change", ["receipt", "label", "history", "causal_graph"])
def test_restoration_rejects_unregistered_modifications(
    tmp_path, restore_pre_causal_graphs, change
):
    receipt_data = load_transition()
    delta = next(d for d in receipt_data["record_deltas"] if d["identifier"] == "CHEBI:28915")
    receipt_file = tmp_path / "curation/causal_graphs_transition.json"
    receipt_file.parent.mkdir(parents=True, exist_ok=True)
    receipt_file.write_bytes(DEFAULT_RECEIPT_PATH.read_bytes())

    source = tmp_path / delta["path"]
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_bytes((ROOT / delta["path"]).read_bytes())

    if change == "receipt":
        receipt_file.write_bytes(receipt_file.read_bytes() + b"\n")
    else:
        doc = yaml.safe_load(source.read_bytes())
        if change == "label":
            doc["label"] = "tampered label"
        elif change == "history":
            doc["curation_history"].pop()
        else:
            doc["causal_graphs"][0]["title"] = "tampered title"
        source.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    original_bytes = source.read_bytes()
    output = tmp_path / "restored.yaml"
    with pytest.raises(AssertionError):
        restore_pre_causal_graphs(tmp_path, delta["path"], output)
    assert source.read_bytes() == original_bytes
    assert not output.exists()

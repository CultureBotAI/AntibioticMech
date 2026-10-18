"""Verify curated UniProt protein examples across causal graphs and primary-literature molecular targets."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from antibioticmech.activity_collections import load_record
from antibioticmech.uniprot_examples import (
    DEFAULT_PLAN_PATH,
    DEFAULT_RECEIPT_PATH,
    apply_planned_examples_to_record_data,
    load_uniprot_examples_plan,
    validate_protein_example_spec,
)
from scripts.render_pages import TEMPLATES_DIR, build_record

ROOT = Path(__file__).resolve().parents[1]


def load_transition() -> dict:
    return json.loads(DEFAULT_RECEIPT_PATH.read_bytes())


def test_every_causal_graph_gene_or_protein_node_has_valid_protein_examples(records):
    causal_graph_records = 0
    gene_or_protein_nodes = 0
    for path, doc in records:
        graphs = doc.get("causal_graphs") or []
        if not graphs:
            continue
        causal_graph_records += 1
        for graph in graphs:
            for node in graph.get("nodes") or []:
                if node.get("node_type") != "GENE_OR_PROTEIN":
                    continue
                gene_or_protein_nodes += 1
                examples = node.get("protein_examples")
                assert isinstance(examples, list) and examples, (
                    f"{path}: GENE_OR_PROTEIN node {graph.get('graph_id')}.{node.get('node_id')} "
                    "is missing protein_examples"
                )
                seen_ids: set[str] = set()
                for ex in examples:
                    normalized = validate_protein_example_spec(
                        ex,
                        context=f"{path} {graph.get('graph_id')}.{node.get('node_id')}",
                    )
                    assert normalized["uniprot_id"] not in seen_ids
                    seen_ids.add(normalized["uniprot_id"])
                    assert normalized.get("gene_symbol"), (
                        f"{path}: expected gene_symbol on {normalized['uniprot_id']}"
                    )
                    assert normalized.get("role"), (
                        f"{path}: expected role on {normalized['uniprot_id']}"
                    )
    assert causal_graph_records == 16
    assert gene_or_protein_nodes == 15


def test_plan_and_transition_summary_counts():
    plan = load_uniprot_examples_plan(DEFAULT_PLAN_PATH)
    receipt = load_transition()
    assert len(plan["records"]) == receipt["record_count"] == len(receipt["record_deltas"]) == 30
    assert sum(d["causal_nodes_updated"] for d in receipt["record_deltas"]) == 15
    assert sum(d["molecular_targets_updated"] for d in receipt["record_deltas"]) == 22
    assert sum(d["protein_examples_added"] for d in receipt["record_deltas"]) == 53
    assert isinstance(plan.get("held_targets"), list) and len(plan["held_targets"]) >= 30


@pytest.mark.parametrize("index", range(30))
def test_exact_scoped_transition_and_idempotence(pre_uniprot_protein_examples_root, index):
    plan = load_uniprot_examples_plan(DEFAULT_PLAN_PATH)
    receipt = load_transition()
    delta = receipt["record_deltas"][index]
    plan_entry = plan["records"][index]
    assert delta["identifier"] == plan_entry["identifier"]

    live_path = ROOT / delta["path"]
    historical_path = pre_uniprot_protein_examples_root / delta["path"]
    assert hashlib.sha256(live_path.read_bytes()).hexdigest() == delta["after_sha256"]
    assert hashlib.sha256(historical_path.read_bytes()).hexdigest() == delta["before_sha256"]

    current = load_record(live_path)
    before = load_record(historical_path)

    _, n_nodes, n_targets, n_examples, changed = apply_planned_examples_to_record_data(
        current, plan_entry
    )
    assert not changed
    assert (n_nodes, n_targets, n_examples) == (0, 0, 0)

    restored = copy.deepcopy(current)
    assert restored["curation_history"].pop() == delta["added_history_event"]
    assert delta["added_history_event"]["action"] == "CURATED_UNIPROT_PROTEIN_EXAMPLES"
    assert len(restored["curation_history"]) == delta["curation_history_before_len"]

    for node_change in delta["causal_node_deltas"]:
        graph = restored["causal_graphs"][node_change["graph_index"]]
        assert graph["graph_id"] == node_change["graph_id"]
        node = graph["nodes"][node_change["node_index"]]
        assert node["node_id"] == node_change["node_id"]
        assert node.pop("protein_examples") == node_change["after_protein_examples"]
        if node_change["before_protein_examples"] is not None:
            node["protein_examples"] = copy.deepcopy(node_change["before_protein_examples"])

    for target_change in delta["molecular_target_deltas"]:
        target = restored["molecular_targets"][target_change["index"]]
        assert target["source"] == target_change["source"] == "PRIMARY_LITERATURE"
        assert target["target_label"] == target_change["target_label"]
        assert target.pop("protein_examples") == target_change["after_protein_examples"]
        if target_change["before_protein_examples"] is not None:
            target["protein_examples"] = copy.deepcopy(target_change["before_protein_examples"])

    assert restored == before


@pytest.mark.parametrize("change", ["receipt", "label", "history", "node_example", "target_example"])
def test_restoration_rejects_unregistered_modifications(
    tmp_path, restore_pre_uniprot_protein_examples, change
):
    receipt_data = load_transition()
    delta = next(d for d in receipt_data["record_deltas"] if d["identifier"] == "CHEBI:28368")
    receipt_file = tmp_path / "curation/uniprot_protein_examples_transition.json"
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
        elif change == "node_example":
            nd = delta["causal_node_deltas"][0]
            node = doc["causal_graphs"][nd["graph_index"]]["nodes"][nd["node_index"]]
            node["protein_examples"][0]["uniprot_id"] = "UniProtKB:P99999"
        else:
            target_idx = delta["molecular_target_deltas"][0]["index"]
            target = doc["molecular_targets"][target_idx]
            target["protein_examples"][0]["uniprot_id"] = "UniProtKB:P99999"
        source.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    original_bytes = source.read_bytes()
    output = tmp_path / "restored.yaml"
    with pytest.raises(AssertionError):
        restore_pre_uniprot_protein_examples(tmp_path, delta["path"], output)
    assert source.read_bytes() == original_bytes
    assert not output.exists()


def test_causal_node_and_molecular_target_protein_examples_render_in_record_html():
    path = ROOT / "data/antibiotics/antibacterial/novobiocin.yaml"
    doc = load_record(path)
    record = build_record(path, doc, {}, "../")
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )
    html = env.get_template("record.html").render(r=record, root="../", stats={})
    assert "UniProtKB:P0AES6" in html
    assert "DNA gyrase subunit B (gyrB)" in html
    assert "Examples:" in html
    assert "NCBITaxon:83333" in html

#!/usr/bin/env python3
"""Score AntibioticMech records by causal graph completeness and evidence quality."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"

PRIMARY_REFERENCE_PREFIXES = ("DOI:", "PMID:")
TARGET_NODE_TYPES = frozenset((
    "CELL_STRUCTURE",
    "CHEMICAL",
    "GENE_OR_PROTEIN",
    "RNA",
    "MOLECULAR_FUNCTION",
    "BIOLOGICAL_PROCESS",
    "PATHWAY",
))
OUTCOME_NODE_TYPES = frozenset(("BIOLOGICAL_PROCESS", "CELL_STRUCTURE", "QUALITY", "STATE"))

TSV_FIELDS = [
    "rank",
    "causal_graph_score",
    "buildability_score",
    "identifier",
    "label",
    "antimicrobial_class",
    "graph_count",
    "node_count",
    "edge_count",
    "primary_edge_references",
    "grounded_nodes",
    "molecular_targets",
    "primary_molecular_targets",
    "resistance_mechanisms",
    "activity_observations",
    "issues",
]


def load_records(corpus_dir: Path = CORPUS_DIR) -> list[tuple[Path, dict[str, Any]]]:
    """Load record YAMLs as ``(path, document)`` pairs."""
    return [
        (path, yaml.safe_load(path.read_text(encoding="utf-8")))
        for path in sorted(corpus_dir.rglob("*.yaml"))
    ]


def _edge_endpoints(edges: list[dict[str, Any]]) -> set[str]:
    endpoints: set[str] = set()
    for edge in edges:
        for slot in ("subject", "object"):
            if edge.get(slot):
                endpoints.add(edge[slot])
    return endpoints


def _is_grounded(node: dict[str, Any]) -> bool:
    return bool(node.get("grounding") or node.get("grounding_status"))


def _evidence_references(evidence: list[dict[str, Any]]) -> list[str]:
    return [
        str(item.get("reference") or "")
        for item in evidence
        if item.get("reference")
    ]


def _is_primary_reference(reference: str) -> bool:
    return reference.startswith(PRIMARY_REFERENCE_PREFIXES)


def buildability_score(record: dict[str, Any]) -> int:
    """Score nearby curated evidence that can help a curator draw the graph."""
    targets = record.get("molecular_targets") or []
    primary_targets = [
        target for target in targets
        if target.get("evidence_status") == "PRIMARY_EVIDENCE" and target.get("evidence")
    ]
    resistance = record.get("resistance_mechanisms") or []
    activities = record.get("activity_spectrum") or []

    score = min(30, len(primary_targets) * 6)
    score += min(15, (len(targets) - len(primary_targets)) * 3)
    score += min(15, len(resistance))
    score += min(15, len(activities) * 3)
    if record.get("mode_of_action"):
        score += 5
    if record.get("mode_of_action_target_scope"):
        score += 5
    if record.get("curation_status") == "REVIEWED":
        score += 10
    return min(score, 100)


def score_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return graph-quality metrics and a 0-100 causal graph score."""
    graphs = record.get("causal_graphs") or []
    targets = record.get("molecular_targets") or []
    primary_targets = sum(
        1 for target in targets
        if target.get("evidence_status") == "PRIMARY_EVIDENCE" and target.get("evidence")
    )
    resistance = record.get("resistance_mechanisms") or []
    activities = record.get("activity_spectrum") or []

    nodes = [node for graph in graphs for node in graph.get("nodes") or []]
    edges = [edge for graph in graphs for edge in graph.get("edges") or []]
    dangling_edges = 0
    for graph in graphs:
        node_ids = {node.get("node_id") for node in graph.get("nodes") or [] if node.get("node_id")}
        for edge in graph.get("edges") or []:
            dangling_edges += sum(1 for slot in ("subject", "object") if edge.get(slot) not in node_ids)
    edges_with_evidence = [
        edge for edge in edges
        if _evidence_references(edge.get("evidence") or [])
    ]
    primary_edge_references = sorted({
        reference
        for edge in edges
        for reference in _evidence_references(edge.get("evidence") or [])
        if _is_primary_reference(reference)
    })
    grounded_nodes = sum(1 for node in nodes if _is_grounded(node))
    edge_endpoints = _edge_endpoints(edges)
    connected_compounds = sum(
        1 for node in nodes
        if node.get("node_id") in edge_endpoints and node.get("node_type") == "COMPOUND"
    )
    connected_targets = sum(
        1 for node in nodes
        if node.get("node_id") in edge_endpoints and node.get("node_type") in TARGET_NODE_TYPES
    )
    connected_outcomes = sum(
        1 for node in nodes
        if node.get("node_id") in edge_endpoints and node.get("node_type") in OUTCOME_NODE_TYPES
    )

    score = 0
    issues: list[str] = []
    if graphs:
        score += 10
    else:
        issues.append("no causal_graphs")

    if nodes:
        score += min(10, len(nodes) * 4)
    else:
        issues.append("no causal nodes")

    if edges:
        score += min(15, len(edges) * 8)
    else:
        issues.append("no causal edges")

    if edges and not dangling_edges:
        score += 10
    elif dangling_edges:
        issues.append(f"{dangling_edges} dangling edge endpoint(s)")

    if nodes and grounded_nodes == len(nodes):
        score += 10
    elif nodes:
        issues.append(f"{len(nodes) - grounded_nodes} ungrounded node(s)")

    if edges and len(edges_with_evidence) == len(edges):
        score += 15
    elif edges:
        issues.append(f"{len(edges) - len(edges_with_evidence)} edge(s) without evidence")

    if primary_edge_references:
        score += 10
    elif edges:
        issues.append("no primary edge citation")

    if connected_compounds:
        score += 5
    else:
        issues.append("no connected compound node")

    if connected_targets:
        score += 5
    else:
        issues.append("no connected target node")

    if connected_outcomes:
        score += 5
    else:
        issues.append("no connected outcome node")

    if graphs and all(graph.get("scope_status") == "MECHANISTIC" for graph in graphs):
        score += 5
    elif graphs:
        issues.append("graph scope not confirmed mechanistic")

    return {
        "causal_graph_score": score,
        "buildability_score": buildability_score(record),
        "identifier": record["identifier"],
        "label": record["label"],
        "antimicrobial_class": record.get("antimicrobial_class", ""),
        "graph_count": len(graphs),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "primary_edge_references": ",".join(primary_edge_references),
        "grounded_nodes": grounded_nodes,
        "molecular_targets": len(targets),
        "primary_molecular_targets": primary_targets,
        "resistance_mechanisms": len(resistance),
        "activity_observations": len(activities),
        "issues": "; ".join(issues),
    }


def ranked_records(records: list[tuple[Path, dict[str, Any]]]) -> list[dict[str, Any]]:
    """Score and rank records from poorest to strongest causal graph quality."""
    ranked = [score_record(record) for _path, record in records]
    ranked.sort(key=lambda row: (
        row["causal_graph_score"],
        -row["buildability_score"],
        row["label"].lower(),
    ))
    for rank, row in enumerate(ranked, 1):
        row["rank"] = rank
    return ranked


def write_tsv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=TSV_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=25, help="Rows to print.")
    parser.add_argument("--tsv", type=Path, help="Write all scored rows to this TSV.")
    parser.add_argument(
        "--corpus",
        type=Path,
        default=CORPUS_DIR,
        help="Directory containing AntibioticRecord YAML files.",
    )
    args = parser.parse_args()

    rows = ranked_records(load_records(args.corpus))
    print("rank\tscore\tbuildability\tidentifier\tlabel\tissues")
    for row in rows[: args.limit]:
        print(
            f"{row['rank']}\t{row['causal_graph_score']}\t"
            f"{row['buildability_score']}\t{row['identifier']}\t"
            f"{row['label']}\t{row['issues']}"
        )
    if args.tsv:
        write_tsv(rows, args.tsv)
        print(f"\nwrote {args.tsv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

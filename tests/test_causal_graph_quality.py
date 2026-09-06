from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from score_causal_graph_quality import (  # noqa: E402
    ranked_records,
    score_record,
    write_tsv,
)


def _base_record(**updates):
    record = {
        "identifier": "CHEBI:1",
        "label": "samplemycin",
        "antimicrobial_class": "ANTIBACTERIAL",
    }
    record.update(updates)
    return record


def test_missing_causal_graphs_score_at_the_bottom():
    row = score_record(_base_record())

    assert row["causal_graph_score"] == 0
    assert "no causal_graphs" in row["issues"]
    assert "no causal nodes" in row["issues"]
    assert "no causal edges" in row["issues"]
    assert "no connected compound node" in row["issues"]
    assert "no connected target node" in row["issues"]
    assert "no connected outcome node" in row["issues"]


def test_grounded_primary_evidence_graph_scores_above_a_dangling_database_graph():
    weak = score_record(_base_record(
        causal_graphs=[{
            "graph_id": "weak",
            "nodes": [{"node_id": "drug", "label": "samplemycin", "node_type": "COMPOUND"}],
            "edges": [{"subject": "drug", "predicate": "affects", "object": "missing"}],
        }],
    ))
    strong = score_record(_base_record(
        causal_graphs=[{
            "graph_id": "folate",
            "scope_status": "MECHANISTIC",
            "nodes": [
                {
                    "node_id": "drug",
                    "label": "samplemycin",
                    "node_type": "COMPOUND",
                    "grounding": "CHEBI:1",
                },
                {
                    "node_id": "target",
                    "label": "dihydrofolate reductase",
                    "node_type": "GENE_OR_PROTEIN",
                    "grounding": "ARO:1",
                },
                {
                    "node_id": "growth",
                    "label": "growth",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "grounding": "GO:1",
                },
            ],
            "edges": [
                {
                    "subject": "drug",
                    "predicate": "inhibits",
                    "predicate_id": "RO:0002408",
                    "object": "target",
                    "evidence": [{"reference": "PMID:1"}],
                },
                {
                    "subject": "target",
                    "predicate": "decreases",
                    "object": "growth",
                    "evidence": [{"reference": "DOI:10.1128/example"}],
                },
            ],
        }],
    ))

    assert weak["causal_graph_score"] < strong["causal_graph_score"]
    assert "1 dangling edge endpoint(s)" in weak["issues"]
    assert "no primary edge citation" in weak["issues"]
    assert strong["causal_graph_score"] == 100
    assert strong["issues"] == ""
    assert strong["primary_edge_references"] == "DOI:10.1128/example,PMID:1"


def test_xrefs_do_not_make_nodes_grounded_without_a_grounding_decision():
    row = score_record(_base_record(
        causal_graphs=[{
            "graph_id": "folate",
            "scope_status": "MECHANISTIC",
            "nodes": [
                {
                    "node_id": "drug",
                    "label": "samplemycin",
                    "node_type": "COMPOUND",
                    "grounding": "CHEBI:1",
                },
                {
                    "node_id": "target",
                    "label": "dihydrofolate reductase",
                    "node_type": "GENE_OR_PROTEIN",
                    "xrefs": ["ARO:1"],
                },
                {
                    "node_id": "growth",
                    "label": "growth",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                },
            ],
            "edges": [
                {
                    "subject": "drug",
                    "predicate": "inhibits",
                    "object": "target",
                    "evidence": [{"reference": "PMID:1"}],
                },
                {
                    "subject": "target",
                    "predicate": "decreases",
                    "object": "growth",
                    "evidence": [{"reference": "PMID:2"}],
                },
            ],
        }],
    ))

    assert row["grounded_nodes"] == 2
    assert row["causal_graph_score"] == 90
    assert "1 ungrounded node(s)" in row["issues"]


def test_cell_structure_targets_count_as_target_engagement():
    row = score_record(_base_record(
        causal_graphs=[{
            "graph_id": "membrane",
            "scope_status": "MECHANISTIC",
            "nodes": [
                {
                    "node_id": "drug",
                    "label": "samplemycin",
                    "node_type": "COMPOUND",
                    "grounding": "CHEBI:1",
                },
                {
                    "node_id": "membrane",
                    "label": "bacterial membrane",
                    "node_type": "CELL_STRUCTURE",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                },
                {
                    "node_id": "potential",
                    "label": "membrane potential",
                    "node_type": "QUALITY",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                },
            ],
            "edges": [
                {
                    "subject": "drug",
                    "predicate": "binds",
                    "object": "membrane",
                    "evidence": [{"reference": "PMID:1"}],
                },
                {
                    "subject": "membrane",
                    "predicate": "supports",
                    "object": "potential",
                    "evidence": [{"reference": "PMID:1"}],
                },
            ],
        }],
    ))

    assert row["causal_graph_score"] == 100
    assert "no connected target node" not in row["issues"]


def test_ranked_records_sort_poor_scores_first_then_actionable_records():
    unscaffolded = _base_record(identifier="CHEBI:1", label="zzymycin")
    scaffolded = _base_record(
        identifier="CHEBI:2",
        label="aaamycin",
        mode_of_action="PROTEIN_SYNTHESIS_INHIBITION",
        mode_of_action_target_scope="MICROBIAL_TARGET",
        molecular_targets=[{
            "target_label": "30S ribosomal subunit",
            "evidence_status": "PRIMARY_EVIDENCE",
            "evidence": [{"reference": "PMID:1"}],
        }],
        resistance_mechanisms=[{"label": "rmtA"}],
    )

    rows = ranked_records([(Path("z.yaml"), unscaffolded), (Path("a.yaml"), scaffolded)])

    assert [row["rank"] for row in rows] == [1, 2]
    assert [row["identifier"] for row in rows] == ["CHEBI:2", "CHEBI:1"]


def test_write_tsv_uses_the_report_schema(tmp_path):
    path = tmp_path / "causal-graph-quality.tsv"
    rows = ranked_records([(Path("record.yaml"), _base_record())])

    write_tsv(rows, path)

    with path.open(newline="", encoding="utf-8") as fh:
        written = list(csv.DictReader(fh, delimiter="\t"))
    assert written[0]["rank"] == "1"
    assert written[0]["identifier"] == "CHEBI:1"
    assert written[0]["causal_graph_score"] == "0"

"""Exercise SVG integrity and safety independently of the record corpus."""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from mechanism_graph import graph_svg

NS = {"s": "http://www.w3.org/2000/svg"}


def svg(graph, instance="one"):
    html = str(graph_svg(graph, instance))
    return ET.fromstring(html[html.index("<svg ") : html.index("</svg>") + 6])


def test_cycles_parallel_edges_isolated_and_unresolved_nodes_are_visible():
    graph = {
        "title": "Mechanism",
        "nodes": [
            {"node_id": "a", "label": "Source"},
            {"node_id": "b", "label": "Target"},
            {"node_id": "alone", "label": "Isolated"},
        ],
        "edges": [
            {"subject": "a", "object": "b", "predicate": "activates"},
            {"subject": "a", "object": "b", "predicate": "binds"},
            {"subject": "b", "object": "a", "predicate": "feedback"},
            {"subject": "b", "object": "b", "predicate": "self"},
            {"subject": "b", "object": "missing", "predicate": "causes"},
        ],
    }
    root = svg(graph)
    nodes = root.findall('.//s:g[@class="graph-node"]', NS)
    edges = root.findall('.//s:g[@class="graph-edge"]', NS)
    assert {n.attrib["data-node-id"] for n in nodes} == {"a", "b", "alone", "missing"}
    assert len(edges) == 5
    assert len({e.find("s:path", NS).attrib["d"] for e in edges}) == 5
    assert all(e.find("s:path", NS).attrib.get("marker-end") for e in edges)
    assert "UNRESOLVED" in "".join(root.itertext())
    assert graph["nodes"][-1]["node_id"] == "alone"  # source remains untouched


def test_labels_evidence_and_ids_are_escaped_and_keyboard_accessible():
    attack = '<script>alert("x")</script> & "quoted"'
    graph = {
        "title": attack,
        "nodes": [{"node_id": attack, "label": attack}],
        "edges": [
            {
                "subject": attack,
                "object": attack,
                "predicate": attack,
                "evidence": [{"reference": "PMID:123"}],
            }
        ],
    }
    root = svg(graph)
    assert root.find(".//s:script", NS) is None
    assert attack in "".join(root.itertext())
    assert "PMID:123" in "".join(root.itertext())
    assert all(g.attrib["tabindex"] == "0" for g in root.findall(".//s:g", NS))
    assert root.attrib["aria-labelledby"]


def test_multiple_graphs_have_distinct_markers_and_deterministic_output():
    graph = {"nodes": [{"node_id": "a", "label": "A"}], "edges": []}
    one, two = svg(graph, "one"), svg(graph, "two")
    assert one.find(".//s:marker", NS).attrib["id"] != two.find(".//s:marker", NS).attrib["id"]
    assert str(graph_svg(graph, "one")) == str(graph_svg(graph, "one"))
    assert "<svg" not in str(graph_svg({}))

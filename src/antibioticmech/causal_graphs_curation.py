"""Deterministic application and verification helpers for curated mechanism causal_graphs."""

from __future__ import annotations

import hashlib
import json
import re
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.uniprot_examples import validate_protein_example_spec
from antibioticmech.validation.write_validated import write_validated_antibiotic

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PLAN_PATH = REPO_ROOT / "curation" / "causal_graphs.yaml"
DEFAULT_RECEIPT_PATH = REPO_ROOT / "curation" / "causal_graphs_transition.json"

CITATION_REF_RE = re.compile(r"^(?:PMID:[1-9][0-9]*|DOI:10\.\d{4,9}/\S+)$")
CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*:[A-Za-z0-9_.:-]+$")

ALLOWED_NODE_TYPES = {
    "COMPOUND",
    "CHEMICAL",
    "GENE_OR_PROTEIN",
    "RNA",
    "GENETIC_ELEMENT",
    "CELL_STRUCTURE",
    "CELLULAR_LOCALIZATION",
    "MOLECULAR_FUNCTION",
    "BIOLOGICAL_PROCESS",
    "PATHWAY",
    "TRANSPORT_PROCESS",
    "STATE",
    "QUALITY",
    "PHENOTYPE",
    "ENVIRONMENTAL_FACTOR",
    "EXPERIMENTAL_FACTOR",
}
TARGET_NODE_TYPES = {
    "CELL_STRUCTURE",
    "CHEMICAL",
    "GENE_OR_PROTEIN",
    "RNA",
    "MOLECULAR_FUNCTION",
    "BIOLOGICAL_PROCESS",
    "PATHWAY",
}
OUTCOME_NODE_TYPES = {
    "BIOLOGICAL_PROCESS",
    "CELL_STRUCTURE",
    "QUALITY",
    "STATE",
}
ALLOWED_COHORTS = {
    "protein_target_with_examples",
    "non_protein_direct_or_measured_target",
}
ALLOWED_BLOCKER_CATEGORIES = {
    "uniprot_protein_example_held",
    "downstream_or_coarse_target_only",
}
EXISTING_GRAPH_KEYS = {
    "identifier",
    "label",
    "path",
    "curation_status",
    "graph_ids",
}
PLAN_ROOT_KEYS = {
    "schema_version",
    "task",
    "curation_action",
    "retrieved_on",
    "scope_note",
    "existing_causal_graphs",
    "records",
    "held_records",
}
PLANNED_RECORD_KEYS = {
    "identifier",
    "label",
    "path",
    "cohort",
    "changes",
    "causal_graphs",
}
HELD_RECORD_KEYS = {
    "identifier",
    "label",
    "path",
    "blocker_category",
    "target_summary",
    "references",
    "reason",
}
CAUSAL_GRAPH_KEYS = {
    "graph_id",
    "title",
    "description",
    "scope_status",
    "scope_notes",
    "nodes",
    "edges",
}
CAUSAL_NODE_KEYS = {
    "node_id",
    "label",
    "node_type",
    "grounding",
    "grounding_status",
    "grounding_notes",
    "xrefs",
    "description",
    "gene_symbols",
    "protein_examples",
}
CAUSAL_EDGE_KEYS = {
    "subject",
    "predicate",
    "predicate_id",
    "object",
    "description",
    "evidence",
}
EVIDENCE_ITEM_KEYS = {
    "reference",
    "snippet",
    "notes",
}

_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _load_yaml_path(path: Path) -> Any:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_YAML_LOADER)


def _json_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@dataclass(frozen=True)
class PlannedCausalGraphResult:
    """Result of evaluating or applying curated causal_graphs to one record."""

    identifier: str
    label: str
    path: Path
    changed: bool
    graphs_added: int
    nodes_added: int
    edges_added: int
    changes: str


def validate_causal_node_spec(
    node: dict[str, Any], *, context: str
) -> dict[str, Any]:
    """Validate and normalize one CausalNode specification."""
    if not isinstance(node, dict):
        raise ValueError(f"{context}: causal node must be a mapping")
    extra_keys = set(node) - CAUSAL_NODE_KEYS
    if extra_keys:
        raise ValueError(f"{context}: unexpected causal node keys {sorted(extra_keys)}")

    node_id = str(node.get("node_id") or "").strip()
    label = str(node.get("label") or "").strip()
    node_type = str(node.get("node_type") or "").strip()
    if not node_id or not label or not node_type:
        raise ValueError(f"{context}: node requires node_id, label, and node_type")
    if node_type not in ALLOWED_NODE_TYPES:
        raise ValueError(
            f"{context} ({node_id}): node_type {node_type!r} not in {sorted(ALLOWED_NODE_TYPES)}"
        )

    grounding = str(node.get("grounding") or "").strip()
    grounding_status = str(node.get("grounding_status") or "").strip()
    grounding_notes = str(node.get("grounding_notes") or "").strip()

    if grounding and not CURIE_RE.match(grounding):
        raise ValueError(f"{context} ({node_id}): invalid grounding CURIE {grounding!r}")
    if grounding_status and grounding_status != "REVIEWED_LABEL_ONLY":
        raise ValueError(
            f"{context} ({node_id}): unsupported grounding_status {grounding_status!r}"
        )
    if grounding_status == "REVIEWED_LABEL_ONLY" and not grounding_notes:
        raise ValueError(
            f"{context} ({node_id}): grounding_status REVIEWED_LABEL_ONLY requires grounding_notes"
        )
    if not grounding and grounding_status != "REVIEWED_LABEL_ONLY":
        raise ValueError(
            f"{context} ({node_id}): node must specify grounding or grounding_status=REVIEWED_LABEL_ONLY"
        )

    normalized: dict[str, Any] = {
        "node_id": node_id,
        "label": label,
        "node_type": node_type,
    }
    if grounding:
        normalized["grounding"] = grounding
    if grounding_status:
        normalized["grounding_status"] = grounding_status
    if grounding_notes:
        normalized["grounding_notes"] = grounding_notes

    if node.get("xrefs") is not None:
        xrefs = node.get("xrefs")
        if not isinstance(xrefs, list) or not xrefs:
            raise ValueError(f"{context} ({node_id}): xrefs must be a non-empty list when present")
        norm_xrefs: list[str] = []
        for x in xrefs:
            xs = str(x or "").strip()
            if not CURIE_RE.match(xs):
                raise ValueError(f"{context} ({node_id}): invalid xref CURIE {xs!r}")
            norm_xrefs.append(xs)
        normalized["xrefs"] = norm_xrefs

    if node.get("description") is not None:
        desc = str(node.get("description") or "").strip()
        if not desc:
            raise ValueError(f"{context} ({node_id}): description must not be empty when present")
        normalized["description"] = desc

    if node.get("gene_symbols") is not None:
        gs = node.get("gene_symbols")
        if not isinstance(gs, list) or not gs:
            raise ValueError(
                f"{context} ({node_id}): gene_symbols must be a non-empty list when present"
            )
        norm_gs = [str(g or "").strip() for g in gs if str(g or "").strip()]
        if not norm_gs:
            raise ValueError(f"{context} ({node_id}): gene_symbols must contain non-empty strings")
        normalized["gene_symbols"] = norm_gs

    raw_examples = node.get("protein_examples")
    if node_type == "GENE_OR_PROTEIN":
        if not isinstance(raw_examples, list) or not raw_examples:
            raise ValueError(
                f"{context} ({node_id}): GENE_OR_PROTEIN node requires non-empty protein_examples"
            )
        seen_uids: set[str] = set()
        norm_examples: list[dict[str, str]] = []
        for ex in raw_examples:
            norm_ex = validate_protein_example_spec(
                ex, context=f"{context} ({node_id})"
            )
            if norm_ex["uniprot_id"] in seen_uids:
                raise ValueError(
                    f"{context} ({node_id}): duplicate protein_example {norm_ex['uniprot_id']}"
                )
            seen_uids.add(norm_ex["uniprot_id"])
            norm_examples.append(norm_ex)
        normalized["protein_examples"] = norm_examples
    elif raw_examples is not None:
        raise ValueError(
            f"{context} ({node_id}): non-GENE_OR_PROTEIN node (node_type={node_type!r}) "
            "must not carry protein_examples"
        )

    return normalized


def validate_causal_edge_spec(
    edge: dict[str, Any], *, node_ids: set[str], context: str
) -> dict[str, Any]:
    """Validate and normalize one CausalEdge specification."""
    if not isinstance(edge, dict):
        raise ValueError(f"{context}: causal edge must be a mapping")
    extra_keys = set(edge) - CAUSAL_EDGE_KEYS
    if extra_keys:
        raise ValueError(f"{context}: unexpected causal edge keys {sorted(extra_keys)}")

    subject = str(edge.get("subject") or "").strip()
    predicate = str(edge.get("predicate") or "").strip()
    obj = str(edge.get("object") or "").strip()
    description = str(edge.get("description") or "").strip()
    if not subject or not predicate or not obj or not description:
        raise ValueError(
            f"{context}: edge requires subject, predicate, object, and description"
        )
    if subject not in node_ids:
        raise ValueError(f"{context}: edge subject {subject!r} not in graph nodes")
    if obj not in node_ids:
        raise ValueError(f"{context}: edge object {obj!r} not in graph nodes")
    if subject == obj:
        raise ValueError(f"{context}: self-loop edge on {subject!r} is not allowed")

    normalized: dict[str, Any] = {
        "subject": subject,
        "predicate": predicate,
    }
    if edge.get("predicate_id") is not None:
        pred_id = str(edge.get("predicate_id") or "").strip()
        if not CURIE_RE.match(pred_id):
            raise ValueError(f"{context}: invalid predicate_id CURIE {pred_id!r}")
        normalized["predicate_id"] = pred_id
    normalized["object"] = obj
    normalized["description"] = description

    raw_evidence = edge.get("evidence")
    if not isinstance(raw_evidence, list) or not raw_evidence:
        raise ValueError(
            f"{context} ({subject} -> {obj}): edge requires non-empty evidence"
        )
    norm_evidence: list[dict[str, str]] = []
    for ev in raw_evidence:
        if not isinstance(ev, dict):
            raise ValueError(f"{context} ({subject} -> {obj}): evidence item must be a mapping")
        extra_ev = set(ev) - EVIDENCE_ITEM_KEYS
        if extra_ev:
            raise ValueError(
                f"{context} ({subject} -> {obj}): unexpected evidence keys {sorted(extra_ev)}"
            )
        ref = str(ev.get("reference") or "").strip()
        if not CITATION_REF_RE.match(ref):
            raise ValueError(
                f"{context} ({subject} -> {obj}): invalid citation reference {ref!r} "
                "(expected PMID:... or DOI:...)"
            )
        notes = str(ev.get("notes") or "").strip()
        snippet = str(ev.get("snippet") or "").strip()
        if not notes and not snippet:
            raise ValueError(
                f"{context} ({subject} -> {obj} {ref}): evidence requires notes or snippet"
            )
        ev_dict: dict[str, str] = {"reference": ref}
        if snippet:
            ev_dict["snippet"] = snippet
        if notes:
            ev_dict["notes"] = notes
        norm_evidence.append(ev_dict)
    normalized["evidence"] = norm_evidence
    return normalized


def validate_causal_graph_spec(
    graph: dict[str, Any], *, compound_id: str, context: str
) -> dict[str, Any]:
    """Validate and normalize one CausalGraph specification."""
    if not isinstance(graph, dict):
        raise ValueError(f"{context}: causal graph must be a mapping")
    extra_keys = set(graph) - CAUSAL_GRAPH_KEYS
    if extra_keys:
        raise ValueError(f"{context}: unexpected causal graph keys {sorted(extra_keys)}")

    graph_id = str(graph.get("graph_id") or "").strip()
    title = str(graph.get("title") or "").strip()
    description = str(graph.get("description") or "").strip()
    scope_status = str(graph.get("scope_status") or "").strip()
    if not graph_id or not title or not description:
        raise ValueError(f"{context}: causal graph requires graph_id, title, and description")
    if scope_status != "MECHANISTIC":
        raise ValueError(
            f"{context} ({graph_id}): scope_status must be 'MECHANISTIC', got {scope_status!r}"
        )

    raw_nodes = graph.get("nodes")
    if not isinstance(raw_nodes, list) or len(raw_nodes) < 3:
        raise ValueError(f"{context} ({graph_id}): nodes must be a list of at least 3 nodes")
    norm_nodes: list[dict[str, Any]] = []
    seen_node_ids: set[str] = set()
    node_types_by_id: dict[str, str] = {}
    has_matching_compound_node = False
    for n in raw_nodes:
        norm_n = validate_causal_node_spec(n, context=f"{context} ({graph_id})")
        nid = norm_n["node_id"]
        if nid in seen_node_ids:
            raise ValueError(f"{context} ({graph_id}): duplicate node_id {nid!r}")
        seen_node_ids.add(nid)
        node_types_by_id[nid] = norm_n["node_type"]
        if norm_n["node_type"] == "COMPOUND" and norm_n.get("grounding") == compound_id:
            has_matching_compound_node = True
        norm_nodes.append(norm_n)
    if not has_matching_compound_node:
        raise ValueError(
            f"{context} ({graph_id}): graph must include a COMPOUND node grounded to {compound_id}"
        )

    raw_edges = graph.get("edges")
    if not isinstance(raw_edges, list) or len(raw_edges) < 2:
        raise ValueError(f"{context} ({graph_id}): edges must be a list of at least 2 edges")
    norm_edges: list[dict[str, Any]] = []
    connected_node_ids: set[str] = set()
    seen_edge_keys: set[tuple[str, str, str]] = set()
    for e in raw_edges:
        norm_e = validate_causal_edge_spec(
            e, node_ids=seen_node_ids, context=f"{context} ({graph_id})"
        )
        ekey = (norm_e["subject"], norm_e["predicate"], norm_e["object"])
        if ekey in seen_edge_keys:
            raise ValueError(f"{context} ({graph_id}): duplicate edge {ekey}")
        seen_edge_keys.add(ekey)
        connected_node_ids.add(norm_e["subject"])
        connected_node_ids.add(norm_e["object"])
        norm_edges.append(norm_e)

    disconnected = seen_node_ids - connected_node_ids
    if disconnected:
        raise ValueError(
            f"{context} ({graph_id}): disconnected nodes not allowed: {sorted(disconnected)}"
        )

    connected_types = {node_types_by_id[nid] for nid in connected_node_ids}
    if "COMPOUND" not in connected_types:
        raise ValueError(f"{context} ({graph_id}): missing connected COMPOUND node")
    if not (connected_types & TARGET_NODE_TYPES):
        raise ValueError(f"{context} ({graph_id}): missing connected target node")
    if not (connected_types & OUTCOME_NODE_TYPES):
        raise ValueError(f"{context} ({graph_id}): missing connected outcome node")

    adj: dict[str, set[str]] = {nid: set() for nid in seen_node_ids}
    rev: dict[str, set[str]] = {nid: set() for nid in seen_node_ids}
    undir: dict[str, set[str]] = {nid: set() for nid in seen_node_ids}
    in_deg: dict[str, int] = {nid: 0 for nid in seen_node_ids}
    out_deg: dict[str, int] = {nid: 0 for nid in seen_node_ids}
    for e in norm_edges:
        u, v = e["subject"], e["object"]
        adj[u].add(v)
        rev[v].add(u)
        undir[u].add(v)
        undir[v].add(u)
        in_deg[v] += 1
        out_deg[u] += 1

    # 1. Weakly connected single component
    start_node = next(iter(seen_node_ids))
    q_undir: deque[str] = deque([start_node])
    vis_undir: set[str] = {start_node}
    while q_undir:
        cur = q_undir.popleft()
        for nxt in undir[cur]:
            if nxt not in vis_undir:
                vis_undir.add(nxt)
                q_undir.append(nxt)
    if len(vis_undir) != len(seen_node_ids):
        raise ValueError(
            f"{context} ({graph_id}): graph has multiple disconnected components"
        )

    # 2. DAG acyclicity (Kahn's topological sort)
    in_copy = dict(in_deg)
    q_topo: deque[str] = deque([nid for nid, d in in_copy.items() if d == 0])
    topo_count = 0
    while q_topo:
        cur = q_topo.popleft()
        topo_count += 1
        for nxt in adj[cur]:
            in_copy[nxt] -= 1
            if in_copy[nxt] == 0:
                q_topo.append(nxt)
    if topo_count != len(seen_node_ids):
        raise ValueError(
            f"{context} ({graph_id}): directed cycle detected in causal graph"
        )

    # 3. Compound source check and directed reachability to outcomes
    compound_nodes = [
        nid for nid, ntype in node_types_by_id.items() if ntype == "COMPOUND"
    ]
    for cnid in compound_nodes:
        if in_deg[cnid] != 0 or out_deg[cnid] == 0:
            raise ValueError(
                f"{context} ({graph_id}): COMPOUND node {cnid!r} must have "
                f"in_degree=0 and out_degree>=1 (got in={in_deg[cnid]}, out={out_deg[cnid]})"
            )

    sinks = [nid for nid, d in out_deg.items() if d == 0]
    for snid in sinks:
        if node_types_by_id[snid] not in OUTCOME_NODE_TYPES:
            raise ValueError(
                f"{context} ({graph_id}): terminal sink node {snid!r} "
                f"(node_type={node_types_by_id[snid]!r}) must be an outcome node "
                f"({sorted(OUTCOME_NODE_TYPES)})"
            )

    q_comp: deque[str] = deque(compound_nodes)
    from_comp: set[str] = set(compound_nodes)
    while q_comp:
        cur = q_comp.popleft()
        for nxt in adj[cur]:
            if nxt not in from_comp:
                from_comp.add(nxt)
                q_comp.append(nxt)

    target_nodes = [
        nid for nid, ntype in node_types_by_id.items() if ntype in TARGET_NODE_TYPES
    ]
    q_targ: deque[str] = deque(target_nodes)
    from_targ: set[str] = set(target_nodes)
    while q_targ:
        cur = q_targ.popleft()
        for nxt in adj[cur]:
            if nxt not in from_targ:
                from_targ.add(nxt)
                q_targ.append(nxt)

    for snid in sinks:
        if snid not in from_comp:
            raise ValueError(
                f"{context} ({graph_id}): terminal outcome {snid!r} is not reachable "
                "via a directed path from the COMPOUND node"
            )
        if snid not in from_targ:
            raise ValueError(
                f"{context} ({graph_id}): terminal outcome {snid!r} is not reachable "
                "via a directed path from any target node"
            )

    q_rev: deque[str] = deque(sinks)
    reaches_sink: set[str] = set(sinks)
    while q_rev:
        cur = q_rev.popleft()
        for prv in rev[cur]:
            if prv not in reaches_sink:
                reaches_sink.add(prv)
                q_rev.append(prv)
    if len(reaches_sink) != len(seen_node_ids):
        dead_ends = sorted(seen_node_ids - reaches_sink)
        raise ValueError(
            f"{context} ({graph_id}): nodes do not reach any terminal outcome: {dead_ends}"
        )

    normalized: dict[str, Any] = {
        "graph_id": graph_id,
        "title": title,
        "description": description,
        "scope_status": scope_status,
    }
    if graph.get("scope_notes") is not None:
        sn = str(graph.get("scope_notes") or "").strip()
        if sn:
            normalized["scope_notes"] = sn
    normalized["nodes"] = norm_nodes
    normalized["edges"] = norm_edges
    return normalized


def validate_existing_graph_entry(
    entry: dict[str, Any], *, plan_path: Path = DEFAULT_PLAN_PATH
) -> str:
    """Validate one existing_causal_graphs entry and return its identifier."""
    if not isinstance(entry, dict):
        raise ValueError(f"{plan_path}: existing_causal_graphs entry must be a mapping")
    extra_keys = set(entry) - EXISTING_GRAPH_KEYS
    if extra_keys:
        raise ValueError(
            f"{plan_path}: unexpected existing_causal_graphs keys {sorted(extra_keys)}"
        )
    identifier = str(entry.get("identifier") or "").strip()
    label = str(entry.get("label") or "").strip()
    rel_path = str(entry.get("path") or "").strip()
    curation_status = str(entry.get("curation_status") or "").strip()
    graph_ids = entry.get("graph_ids")
    if not identifier or not label or not rel_path or not curation_status:
        raise ValueError(
            f"{plan_path}: existing_causal_graphs entry requires identifier, label, path, and curation_status"
        )
    if not isinstance(graph_ids, list) or not graph_ids:
        raise ValueError(
            f"{plan_path} ({identifier}): existing_causal_graphs entry requires non-empty graph_ids"
        )
    return identifier


def validate_held_record_entry(
    entry: dict[str, Any], *, plan_path: Path = DEFAULT_PLAN_PATH
) -> str:
    """Validate one held_records entry and return its identifier."""
    if not isinstance(entry, dict):
        raise ValueError(f"{plan_path}: held_records entry must be a mapping")
    extra_keys = set(entry) - HELD_RECORD_KEYS
    if extra_keys:
        raise ValueError(f"{plan_path}: unexpected held_records keys {sorted(extra_keys)}")
    identifier = str(entry.get("identifier") or "").strip()
    label = str(entry.get("label") or "").strip()
    rel_path = str(entry.get("path") or "").strip()
    blocker_category = str(entry.get("blocker_category") or "").strip()
    target_summary = str(entry.get("target_summary") or "").strip()
    reason = str(entry.get("reason") or "").strip()
    references = entry.get("references")
    if (
        not identifier
        or not label
        or not rel_path
        or not blocker_category
        or not target_summary
        or not reason
    ):
        raise ValueError(
            f"{plan_path}: held_records entry requires identifier, label, path, "
            "blocker_category, target_summary, and reason"
        )
    if (
        "pending strain/subunit-specific split" in reason
        or "Multi-subunit, multi-isoform, or isolate-unspecified target (" in reason
    ):
        raise ValueError(
            f"{plan_path} ({identifier}): held_records reason must cite the specific "
            "study/accession blocker rather than generic placeholder text"
        )
    if blocker_category not in ALLOWED_BLOCKER_CATEGORIES:
        raise ValueError(
            f"{plan_path} ({identifier}): blocker_category must be one of "
            f"{sorted(ALLOWED_BLOCKER_CATEGORIES)}"
        )
    if not isinstance(references, list) or not references:
        raise ValueError(
            f"{plan_path} ({identifier}): held_records entry requires non-empty references list"
        )
    for ref in references:
        rs = str(ref or "").strip()
        if not CITATION_REF_RE.match(rs):
            raise ValueError(f"{plan_path} ({identifier}): invalid held reference {rs!r}")
    return identifier


def validate_planned_causal_graph_entry(
    entry: dict[str, Any], *, plan_path: Path = DEFAULT_PLAN_PATH
) -> None:
    """Validate one planned record entry in curation/causal_graphs.yaml."""
    if not isinstance(entry, dict):
        raise ValueError(f"{plan_path}: record entry must be a mapping")
    extra_keys = set(entry) - PLANNED_RECORD_KEYS
    if extra_keys:
        raise ValueError(
            f"{plan_path}: unexpected planned record keys {sorted(extra_keys)}"
        )
    identifier = str(entry.get("identifier") or "").strip()
    label = str(entry.get("label") or "").strip()
    rel_path = str(entry.get("path") or "").strip()
    cohort = str(entry.get("cohort") or "").strip()
    if not identifier or not label or not rel_path or not cohort:
        raise ValueError(
            f"{plan_path}: record entry requires identifier, label, path, and cohort"
        )
    if cohort not in ALLOWED_COHORTS:
        raise ValueError(
            f"{plan_path} ({identifier}): cohort must be one of {sorted(ALLOWED_COHORTS)}"
        )
    graphs = entry.get("causal_graphs")
    if not isinstance(graphs, list) or not graphs:
        raise ValueError(f"{plan_path} ({identifier}): causal_graphs must be a non-empty list")
    seen_gids: set[str] = set()
    gp_node_count = 0
    for g in graphs:
        norm_g = validate_causal_graph_spec(
            g, compound_id=identifier, context=f"{plan_path} ({identifier})"
        )
        gid = norm_g["graph_id"]
        if gid in seen_gids:
            raise ValueError(f"{plan_path} ({identifier}): duplicate graph_id {gid!r}")
        seen_gids.add(gid)
        for n in norm_g["nodes"]:
            if n["node_type"] == "GENE_OR_PROTEIN":
                gp_node_count += 1
    if cohort == "protein_target_with_examples" and gp_node_count == 0:
        raise ValueError(
            f"{plan_path} ({identifier}): protein_target_with_examples cohort "
            "requires >=1 GENE_OR_PROTEIN node"
        )
    if cohort == "non_protein_direct_or_measured_target" and gp_node_count > 0:
        raise ValueError(
            f"{plan_path} ({identifier}): non_protein_direct_or_measured_target cohort "
            "must have 0 GENE_OR_PROTEIN nodes"
        )


def load_causal_graphs_plan(path: Path = DEFAULT_PLAN_PATH) -> dict[str, Any]:
    """Load and structurally validate curation/causal_graphs.yaml."""
    raw = _load_yaml_path(path)
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: plan root must be a mapping")
    extra_root_keys = set(raw) - PLAN_ROOT_KEYS
    if extra_root_keys:
        raise ValueError(
            f"{path}: unexpected plan root keys {sorted(extra_root_keys)}"
        )

    existing = raw.get("existing_causal_graphs")
    if not isinstance(existing, list) or not existing:
        raise ValueError(f"{path}: existing_causal_graphs must be a non-empty list")
    seen_ids: set[str] = set()
    for item in existing:
        ident = validate_existing_graph_entry(item, plan_path=path)
        if ident in seen_ids:
            raise ValueError(f"{path}: duplicate identifier {ident} in existing_causal_graphs")
        seen_ids.add(ident)

    records = raw.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path}: records must be a non-empty list")
    for entry in records:
        validate_planned_causal_graph_entry(entry, plan_path=path)
        ident = str(entry["identifier"]).strip()
        if ident in seen_ids:
            raise ValueError(f"{path}: duplicate identifier {ident} across plan sections")
        seen_ids.add(ident)

    held = raw.get("held_records")
    if not isinstance(held, list) or not held:
        raise ValueError(f"{path}: held_records must be a non-empty list")
    for entry in held:
        ident = validate_held_record_entry(entry, plan_path=path)
        if ident in seen_ids:
            raise ValueError(f"{path}: duplicate identifier {ident} in held_records")
        seen_ids.add(ident)

    return raw


def resolve_record_path(root: Path, plan_entry: dict[str, Any]) -> Path:
    """Resolve a planned record's YAML path under root."""
    rel_path = str(plan_entry.get("path") or "").strip()
    if rel_path:
        candidate = root / rel_path
        if candidate.exists():
            return candidate
    identifier = str(plan_entry["identifier"])
    for path in sorted((root / "data" / "antibiotics").rglob("*.yaml")):
        data = _load_yaml_path(path)
        if isinstance(data, dict) and data.get("identifier") == identifier:
            return path
    raise FileNotFoundError(f"Could not find antibiotic record for {identifier} under {root}")


def apply_planned_causal_graphs_to_record_data(
    record: dict[str, Any],
    plan_entry: dict[str, Any],
) -> tuple[dict[str, Any], int, int, int, bool]:
    """Apply one planned causal_graphs entry to a loaded YAML dict without mutating input."""
    updated = dict(record)
    if "causal_graphs" in updated and updated["causal_graphs"] is not None:
        updated["causal_graphs"] = deepcopy(updated["causal_graphs"])
    if "curation_history" in updated and updated["curation_history"] is not None:
        updated["curation_history"] = deepcopy(updated["curation_history"])

    identifier = str(plan_entry["identifier"])
    label = str(plan_entry["label"])
    if updated.get("identifier") != identifier:
        raise ValueError(
            f"Record identifier mismatch: expected {identifier}, got {updated.get('identifier')}"
        )
    if updated.get("label") != label:
        raise ValueError(
            f"Record label mismatch for {identifier}: expected {label!r}, got {updated.get('label')!r}"
        )

    existing_graphs = [deepcopy(g) for g in (updated.get("causal_graphs") or [])]
    planned_graphs = [
        validate_causal_graph_spec(
            raw_graph,
            compound_id=identifier,
            context=f"{identifier} planned causal_graphs",
        )
        for raw_graph in (plan_entry.get("causal_graphs") or [])
    ]

    changed = existing_graphs != planned_graphs
    if changed:
        updated["causal_graphs"] = planned_graphs
        graphs_added = len(planned_graphs)
        nodes_added = sum(len(g["nodes"]) for g in planned_graphs)
        edges_added = sum(len(g["edges"]) for g in planned_graphs)
    else:
        graphs_added = 0
        nodes_added = 0
        edges_added = 0

    return updated, graphs_added, nodes_added, edges_added, changed


def verify_reviewed_causal_graphs_accounting(
    records: list[tuple[Path, dict[str, Any]]],
    plan: dict[str, Any] | None = None,
    *,
    root: Path = REPO_ROOT,
) -> dict[str, int]:
    """Verify 100% accounting of causal_graphs across the corpus and all REVIEWED records."""
    loaded_plan = load_causal_graphs_plan(DEFAULT_PLAN_PATH) if plan is None else plan

    existing_by_id = {
        str(e["identifier"]): e for e in (loaded_plan.get("existing_causal_graphs") or [])
    }
    curated_by_id = {
        str(e["identifier"]): e for e in (loaded_plan.get("records") or [])
    }
    held_by_id = {
        str(e["identifier"]): e for e in (loaded_plan.get("held_records") or [])
    }

    seen_existing: set[str] = set()
    seen_curated: set[str] = set()
    seen_held: set[str] = set()

    total_causal_graph_records = 0
    reviewed_total = 0
    reviewed_existing_graphs = 0
    reviewed_curated_graphs = 0
    reviewed_held = 0
    seeded_existing_graphs = 0

    for path, doc in records:
        identifier = str(doc.get("identifier") or "")
        label = str(doc.get("label") or "")
        rel_path = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)
        status = str(doc.get("curation_status") or "")
        graphs = doc.get("causal_graphs") or []

        if graphs:
            total_causal_graph_records += 1
            if identifier in existing_by_id:
                ex = existing_by_id[identifier]
                if ex["label"] != label or ex["path"] != rel_path or ex["curation_status"] != status:
                    raise ValueError(f"{rel_path}: existing_causal_graphs metadata mismatch for {identifier}")
                actual_gids = [str(g.get("graph_id") or "") for g in graphs]
                expected_gids = [str(gid) for gid in (ex.get("graph_ids") or [])]
                if actual_gids != expected_gids:
                    raise ValueError(
                        f"{rel_path}: existing_causal_graphs graph_ids mismatch for {identifier}: "
                        f"expected {expected_gids}, got {actual_gids}"
                    )
                seen_existing.add(identifier)
                if status == "REVIEWED":
                    reviewed_existing_graphs += 1
                else:
                    seeded_existing_graphs += 1
            elif identifier in curated_by_id:
                cur = curated_by_id[identifier]
                if cur["label"] != label or cur["path"] != rel_path:
                    raise ValueError(f"{rel_path}: curated causal_graphs metadata mismatch for {identifier}")
                planned_graphs = [
                    validate_causal_graph_spec(
                        g, compound_id=identifier, context=f"{rel_path} ({identifier})"
                    )
                    for g in (cur.get("causal_graphs") or [])
                ]
                if graphs != planned_graphs:
                    raise ValueError(
                        f"{rel_path}: live causal_graphs in {identifier} do not match "
                        "curation/causal_graphs.yaml"
                    )
                if cur.get("cohort") == "protein_target_with_examples":
                    mt_examples = {
                        pe["uniprot_id"]: pe
                        for mt in (doc.get("molecular_targets") or [])
                        if mt.get("source") == "PRIMARY_LITERATURE"
                        for pe in (mt.get("protein_examples") or [])
                    }
                    cg_examples = {
                        pe["uniprot_id"]: pe
                        for g in graphs
                        for n in (g.get("nodes") or [])
                        if n.get("node_type") == "GENE_OR_PROTEIN"
                        for pe in (n.get("protein_examples") or [])
                    }
                    if cg_examples != mt_examples:
                        raise ValueError(
                            f"{rel_path}: GENE_OR_PROTEIN causal node protein_examples "
                            f"do not match PRIMARY_LITERATURE molecular_targets "
                            f"protein_examples for {identifier}"
                        )
                seen_curated.add(identifier)
                if status != "REVIEWED":
                    raise ValueError(
                        f"{rel_path}: curated record {identifier} must have curation_status=REVIEWED"
                    )
                reviewed_curated_graphs += 1
            else:
                raise ValueError(
                    f"{rel_path}: record {identifier} has causal_graphs "
                    "but is not in existing_causal_graphs or records"
                )

        if status == "REVIEWED":
            reviewed_total += 1
            if not graphs:
                if identifier not in held_by_id:
                    raise ValueError(
                        f"{rel_path}: REVIEWED record {identifier} lacks causal_graphs "
                        "and is missing from held_records"
                    )
                held = held_by_id[identifier]
                if held["label"] != label or held["path"] != rel_path:
                    raise ValueError(f"{rel_path}: held_records metadata mismatch for {identifier}")
                seen_held.add(identifier)
                reviewed_held += 1
            elif identifier in held_by_id:
                raise ValueError(
                    f"{rel_path}: REVIEWED record {identifier} has causal_graphs "
                    "and must not appear in held_records"
                )

    if set(existing_by_id) != seen_existing:
        raise ValueError(
            f"Unmatched existing_causal_graphs entries: {sorted(set(existing_by_id) - seen_existing)}"
        )
    if set(curated_by_id) != seen_curated:
        raise ValueError(
            f"Unmatched curated records entries: {sorted(set(curated_by_id) - seen_curated)}"
        )
    if set(held_by_id) != seen_held:
        raise ValueError(
            f"Unmatched held_records entries: {sorted(set(held_by_id) - seen_held)}"
        )

    return {
        "total_causal_graph_records": total_causal_graph_records,
        "reviewed_total": reviewed_total,
        "reviewed_existing_graphs": reviewed_existing_graphs,
        "reviewed_curated_graphs": reviewed_curated_graphs,
        "reviewed_held": reviewed_held,
        "seeded_existing_graphs": seeded_existing_graphs,
    }


def apply_causal_graphs_plan(
    root: Path = REPO_ROOT,
    plan_path: Path = DEFAULT_PLAN_PATH,
    *,
    only_identifiers: set[str] | None = None,
    apply: bool = False,
    receipt_path: Path | None = DEFAULT_RECEIPT_PATH,
    curator: str = "antigravity",
    timestamp: str | None = None,
    llm_assisted: bool = True,
) -> list[PlannedCausalGraphResult]:
    """Evaluate or apply the curated causal_graphs plan."""
    plan = load_causal_graphs_plan(plan_path)
    default_action = str(plan.get("curation_action") or "CURATED_CAUSAL_GRAPHS")
    results: list[PlannedCausalGraphResult] = []
    receipt_records: list[dict[str, Any]] = []

    for entry in plan["records"]:
        identifier = str(entry["identifier"])
        if only_identifiers is not None and identifier not in only_identifiers:
            continue
        record_path = resolve_record_path(root, entry)
        before_data = _load_yaml_path(record_path)

        (
            updated_data,
            graphs_added,
            nodes_added,
            edges_added,
            changed,
        ) = apply_planned_causal_graphs_to_record_data(before_data, entry)

        changes_text = str(
            entry.get("changes")
            or (
                f"Added {graphs_added} evidence-backed MECHANISTIC causal graph(s) "
                f"({nodes_added} nodes, {edges_added} edges) from primary literature."
            )
        )

        if changed and apply:
            before_sha = _file_sha256(record_path)
            before_history_len = len(before_data.get("curation_history") or [])
            before_graphs = deepcopy(before_data.get("causal_graphs"))
            unchanged_before = {
                k: v
                for k, v in before_data.items()
                if k not in {"causal_graphs", "curation_history"}
            }
            unchanged_before_sha = _json_sha256(unchanged_before)

            record_curation_event(
                updated_data,
                curator=curator,
                action=default_action,
                changes=changes_text,
                llm_assisted=llm_assisted,
                timestamp=timestamp,
            )
            write_validated_antibiotic(updated_data, record_path)
            after_sha = _file_sha256(record_path)
            after_data = _load_yaml_path(record_path)
            unchanged_after = {
                k: v
                for k, v in after_data.items()
                if k not in {"causal_graphs", "curation_history"}
            }
            unchanged_after_sha = _json_sha256(unchanged_after)
            if unchanged_after_sha != unchanged_before_sha:
                raise RuntimeError(f"Unchanged fields hash mutated for {identifier}")

            receipt_records.append(
                {
                    "identifier": identifier,
                    "label": str(entry["label"]),
                    "path": record_path.relative_to(root).as_posix(),
                    "cohort": str(entry["cohort"]),
                    "before_sha256": before_sha,
                    "after_sha256": after_sha,
                    "unchanged_fields_sha256": unchanged_after_sha,
                    "graphs_added": graphs_added,
                    "nodes_added": nodes_added,
                    "edges_added": edges_added,
                    "history_events_added": 1,
                    "curation_history_before_len": before_history_len,
                    "curation_history_after_len": len(after_data.get("curation_history") or []),
                    "before_causal_graphs": before_graphs,
                    "after_causal_graphs": deepcopy(after_data.get("causal_graphs")),
                    "added_history_event": deepcopy((after_data.get("curation_history") or [])[-1]),
                }
            )

        results.append(
            PlannedCausalGraphResult(
                identifier=identifier,
                label=str(entry["label"]),
                path=record_path,
                changed=changed,
                graphs_added=graphs_added,
                nodes_added=nodes_added,
                edges_added=edges_added,
                changes=changes_text,
            )
        )

    if apply and receipt_path is not None and only_identifiers is None and receipt_records:
        rel_plan = (
            plan_path.relative_to(root).as_posix()
            if plan_path.is_relative_to(root)
            else str(plan_path)
        )
        payload = {
            "schema_version": 1,
            "task": str(plan.get("task") or "causal_graphs_curation"),
            "plan_path": rel_plan,
            "record_count": len(receipt_records),
            "record_deltas": receipt_records,
        }
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    return results

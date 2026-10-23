"""Deterministic application and verification helpers for curated UniProt protein examples."""

from __future__ import annotations

import datetime
import hashlib
import json
import re
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.validation.write_validated import write_validated_antibiotic

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PLAN_PATH = REPO_ROOT / "curation" / "uniprot_protein_examples.yaml"
DEFAULT_RECEIPT_PATH = REPO_ROOT / "curation" / "uniprot_protein_examples_transition.json"

UNIPROT_ID_RE = re.compile(
    r"^UniProtKB:(?:[OPQ][0-9][A-Z0-9]{3}[0-9]"
    r"|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})(?:-[1-9][0-9]*)?$"
)
TAXON_ID_RE = re.compile(r"^NCBITaxon:[1-9][0-9]*$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_ENTRY_STATUSES = {"REVIEWED", "UNREVIEWED"}
ALLOWED_MOLECULAR_TARGET_TYPES = {
    "PROTEIN",
    "PROTEIN_COMPLEX",
    "RIBOSOMAL_SUBUNIT",
    "VIRAL_PROTEIN",
}
ALLOWED_HELD_SCOPES = {"causal_graphs", "molecular_targets"}
HELD_CAUSAL_GRAPH_KEYS = {"identifier", "label", "path", "scope", "graph_id", "reason"}
HELD_MOLECULAR_TARGET_KEYS = {
    "identifier",
    "label",
    "path",
    "scope",
    "target_label",
    "target_type",
    "target_reference",
    "reason",
}
PROTEIN_EXAMPLE_KEYS = (
    "uniprot_id",
    "protein_label",
    "gene_symbol",
    "taxon_id",
    "taxon_label",
    "entry_status",
    "retrieved_on",
    "role",
)
_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _load_yaml_path(path: Path) -> Any:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_YAML_LOADER)


@dataclass(frozen=True)
class PlannedRecordResult:
    """Result of evaluating or applying curated UniProt protein examples to one record."""

    identifier: str
    label: str
    path: Path
    changed: bool
    causal_nodes_updated: int
    molecular_targets_updated: int
    protein_examples_added: int
    changes: str


def _json_sha256(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_held_target_entry(
    entry: dict[str, Any], *, plan_path: Path = DEFAULT_PLAN_PATH
) -> tuple[str, ...]:
    """Validate one held_targets entry and return its uniqueness key."""
    if not isinstance(entry, dict):
        raise ValueError(f"{plan_path}: held_targets entry must be a mapping")
    identifier = str(entry.get("identifier") or "").strip()
    label = str(entry.get("label") or "").strip()
    rel_path = str(entry.get("path") or "").strip()
    scope = str(entry.get("scope") or "").strip()
    reason = str(entry.get("reason") or "").strip()
    if not identifier or not label or not rel_path or not scope or not reason:
        raise ValueError(
            f"{plan_path}: held_targets entry requires identifier, label, path, scope, and reason"
        )
    if "pending strain/subunit-specific split" in reason or reason.startswith(
        "Multi-subunit, multi-isoform, or isolate-unspecified target ("
    ):
        raise ValueError(
            f"{plan_path} ({identifier}): held_targets reason must cite the specific "
            "study/accession blocker rather than generic placeholder text"
        )
    if scope not in ALLOWED_HELD_SCOPES:
        raise ValueError(
            f"{plan_path} ({identifier}): held_targets scope must be one of {sorted(ALLOWED_HELD_SCOPES)}"
        )
    if scope == "causal_graphs":
        extra_keys = set(entry) - HELD_CAUSAL_GRAPH_KEYS
        if extra_keys:
            raise ValueError(
                f"{plan_path} ({identifier}): unexpected held causal_graphs keys {sorted(extra_keys)}"
            )
        graph_id = str(entry.get("graph_id") or "").strip()
        if not graph_id:
            raise ValueError(
                f"{plan_path} ({identifier}): held causal_graphs entry requires graph_id"
            )
        return ("causal_graphs", identifier, graph_id)

    extra_keys = set(entry) - HELD_MOLECULAR_TARGET_KEYS
    if extra_keys:
        raise ValueError(
            f"{plan_path} ({identifier}): unexpected held molecular_targets keys {sorted(extra_keys)}"
        )
    target_label = str(entry.get("target_label") or "").strip()
    target_type = str(entry.get("target_type") or "").strip()
    target_reference = str(entry.get("target_reference") or "").strip()
    if not target_label or not target_type or not target_reference:
        raise ValueError(
            f"{plan_path} ({identifier}): held molecular_targets entry requires "
            "target_label, target_type, and target_reference"
        )
    return ("molecular_targets", identifier, target_label, target_reference)


def load_uniprot_examples_plan(path: Path = DEFAULT_PLAN_PATH) -> dict[str, Any]:
    """Load and structurally validate a curated UniProt protein examples plan."""
    raw = _load_yaml_path(path)
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: plan root must be a mapping")
    records = raw.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path}: records must be a non-empty list")
    seen_ids: set[str] = set()
    curated_graph_keys: set[tuple[str, str, str]] = set()
    curated_target_keys: set[tuple[str, str, str, str]] = set()
    for entry in records:
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: record entry must be a mapping")
        identifier = str(entry.get("identifier") or "").strip()
        label = str(entry.get("label") or "").strip()
        rel_path = str(entry.get("path") or "").strip()
        if not identifier or not label or not rel_path:
            raise ValueError(f"{path}: each record entry requires identifier, label, and path")
        if identifier in seen_ids:
            raise ValueError(f"{path}: duplicate record identifier {identifier}")
        seen_ids.add(identifier)
        validate_planned_record_entry(entry, plan_path=path)
        for node_spec in entry.get("causal_node_examples") or []:
            curated_graph_keys.add(("causal_graphs", identifier, str(node_spec["graph_id"]).strip()))
        for target_spec in entry.get("molecular_target_examples") or []:
            curated_target_keys.add(
                (
                    "molecular_targets",
                    identifier,
                    str(target_spec["target_label"]).strip(),
                    str(target_spec["target_reference"]).strip(),
                )
            )

    held_targets = raw.get("held_targets")
    if held_targets is not None:
        if not isinstance(held_targets, list) or not held_targets:
            raise ValueError(f"{path}: held_targets must be a non-empty list when present")
        seen_held_keys: set[tuple[str, ...]] = set()
        for held_entry in held_targets:
            held_key = validate_held_target_entry(held_entry, plan_path=path)
            if held_key in seen_held_keys:
                raise ValueError(f"{path}: duplicate held_targets entry {held_key}")
            if held_key in curated_graph_keys or held_key in curated_target_keys:
                raise ValueError(
                    f"{path}: held_targets entry {held_key} overlaps with curated records"
                )
            seen_held_keys.add(held_key)
    return raw


def validate_protein_example_spec(spec: dict[str, Any], *, context: str) -> dict[str, str]:
    """Validate and normalize one ProteinExample specification."""
    if not isinstance(spec, dict):
        raise ValueError(f"{context}: protein example must be a mapping")
    extra_keys = set(spec) - set(PROTEIN_EXAMPLE_KEYS)
    if extra_keys:
        raise ValueError(f"{context}: unexpected protein example keys {sorted(extra_keys)}")

    uniprot_id = str(spec.get("uniprot_id") or "").strip()
    if not UNIPROT_ID_RE.match(uniprot_id):
        raise ValueError(f"{context}: invalid uniprot_id {uniprot_id!r}")

    protein_label = str(spec.get("protein_label") or "").strip()
    if not protein_label:
        raise ValueError(f"{context} ({uniprot_id}): protein_label is required")

    taxon_id = str(spec.get("taxon_id") or "").strip()
    if not TAXON_ID_RE.match(taxon_id):
        raise ValueError(f"{context} ({uniprot_id}): invalid taxon_id {taxon_id!r}")

    taxon_label = str(spec.get("taxon_label") or "").strip()
    if not taxon_label:
        raise ValueError(f"{context} ({uniprot_id}): taxon_label is required")

    entry_status = str(spec.get("entry_status") or "").strip()
    if entry_status not in ALLOWED_ENTRY_STATUSES:
        raise ValueError(
            f"{context} ({uniprot_id}): entry_status must be one of {sorted(ALLOWED_ENTRY_STATUSES)}"
        )

    retrieved_on = str(spec.get("retrieved_on") or "").strip()
    if not ISO_DATE_RE.match(retrieved_on):
        raise ValueError(f"{context} ({uniprot_id}): invalid retrieved_on {retrieved_on!r}")
    try:
        datetime.date.fromisoformat(retrieved_on)
    except ValueError as exc:
        raise ValueError(f"{context} ({uniprot_id}): invalid retrieved_on {retrieved_on!r}") from exc

    role = str(spec.get("role") or "").strip()
    if not role:
        raise ValueError(f"{context} ({uniprot_id}): role is required")

    normalized: dict[str, str] = {
        "uniprot_id": uniprot_id,
        "protein_label": protein_label,
    }
    gene_symbol = str(spec.get("gene_symbol") or "").strip()
    if gene_symbol:
        normalized["gene_symbol"] = gene_symbol
    normalized["taxon_id"] = taxon_id
    normalized["taxon_label"] = taxon_label
    normalized["entry_status"] = entry_status
    normalized["retrieved_on"] = retrieved_on
    normalized["role"] = role
    return normalized


def validate_planned_record_entry(entry: dict[str, Any], *, plan_path: Path = DEFAULT_PLAN_PATH) -> None:
    """Validate one record entry from the curation plan."""
    identifier = str(entry.get("identifier") or "<unknown>")
    causal_specs = entry.get("causal_node_examples") or []
    target_specs = entry.get("molecular_target_examples") or []
    if not isinstance(causal_specs, list) or not isinstance(target_specs, list):
        raise ValueError(
            f"{plan_path} ({identifier}): causal_node_examples and molecular_target_examples must be lists"
        )
    if not causal_specs and not target_specs:
        raise ValueError(
            f"{plan_path} ({identifier}): must specify at least one "
            "causal_node_examples or molecular_target_examples item"
        )

    seen_nodes: set[tuple[str, str]] = set()
    for node_spec in causal_specs:
        if not isinstance(node_spec, dict):
            raise ValueError(f"{plan_path} ({identifier}): causal_node_examples item must be a mapping")
        graph_id = str(node_spec.get("graph_id") or "").strip()
        node_id = str(node_spec.get("node_id") or "").strip()
        node_label = str(node_spec.get("node_label") or "").strip()
        if not graph_id or not node_id or not node_label:
            raise ValueError(
                f"{plan_path} ({identifier}): causal_node_examples item requires "
                "graph_id, node_id, and node_label"
            )
        key = (graph_id, node_id)
        if key in seen_nodes:
            raise ValueError(f"{plan_path} ({identifier}): duplicate causal node key {key}")
        seen_nodes.add(key)
        examples = node_spec.get("protein_examples")
        if not isinstance(examples, list) or not examples:
            raise ValueError(
                f"{plan_path} ({identifier} {graph_id}.{node_id}): protein_examples must be non-empty"
            )
        seen_ids: set[str] = set()
        for ex in examples:
            normalized = validate_protein_example_spec(
                ex, context=f"{plan_path} ({identifier} {graph_id}.{node_id})"
            )
            if normalized["uniprot_id"] in seen_ids:
                raise ValueError(
                    f"{plan_path} ({identifier} {graph_id}.{node_id}): duplicate {normalized['uniprot_id']}"
                )
            seen_ids.add(normalized["uniprot_id"])

    seen_targets: set[tuple[str, str, str]] = set()
    for target_spec in target_specs:
        if not isinstance(target_spec, dict):
            raise ValueError(f"{plan_path} ({identifier}): molecular_target_examples item must be a mapping")
        source = str(target_spec.get("source") or "PRIMARY_LITERATURE").strip()
        if source != "PRIMARY_LITERATURE":
            raise ValueError(
                f"{plan_path} ({identifier}): curated molecular_target_examples "
                f"only permitted on PRIMARY_LITERATURE targets, got {source!r}"
            )
        target_label = str(target_spec.get("target_label") or "").strip()
        target_reference = str(target_spec.get("target_reference") or "").strip()
        if not target_label or not target_reference:
            raise ValueError(
                f"{plan_path} ({identifier}): molecular_target_examples item "
                "requires target_label and target_reference"
            )
        key = (source, target_label, target_reference)
        if key in seen_targets:
            raise ValueError(f"{plan_path} ({identifier}): duplicate molecular target key {key}")
        seen_targets.add(key)
        examples = target_spec.get("protein_examples")
        if not isinstance(examples, list) or not examples:
            raise ValueError(
                f"{plan_path} ({identifier} target {target_label!r}): protein_examples must be non-empty"
            )
        seen_ids = set()
        for ex in examples:
            normalized = validate_protein_example_spec(
                ex, context=f"{plan_path} ({identifier} target {target_label!r})"
            )
            if normalized["uniprot_id"] in seen_ids:
                raise ValueError(
                    f"{plan_path} ({identifier} target {target_label!r}): "
                    f"duplicate {normalized['uniprot_id']}"
                )
            seen_ids.add(normalized["uniprot_id"])


def _merge_protein_examples(
    existing: list[dict[str, Any]] | None,
    planned: list[dict[str, Any]],
    *,
    context: str,
) -> tuple[list[dict[str, Any]], int, bool]:
    merged: list[dict[str, Any]] = [deepcopy(item) for item in (existing or [])]
    by_id: dict[str, int] = {}
    for idx, item in enumerate(merged):
        uid = str(item.get("uniprot_id") or "").strip()
        if uid:
            by_id[uid] = idx

    added_or_updated = 0
    changed = False
    for raw_spec in planned:
        normalized = validate_protein_example_spec(raw_spec, context=context)
        uid = normalized["uniprot_id"]
        if uid in by_id:
            idx = by_id[uid]
            if merged[idx] != normalized:
                merged[idx] = normalized
                changed = True
                added_or_updated += 1
        else:
            by_id[uid] = len(merged)
            merged.append(normalized)
            changed = True
            added_or_updated += 1
    return merged, added_or_updated, changed


def apply_planned_examples_to_record_data(
    record: dict[str, Any],
    plan_entry: dict[str, Any],
) -> tuple[dict[str, Any], int, int, int, bool]:
    """Apply one planned record entry to a loaded YAML dict without mutating the input."""
    updated = dict(record)
    if "causal_graphs" in updated and updated["causal_graphs"] is not None:
        updated["causal_graphs"] = deepcopy(updated["causal_graphs"])
    if "molecular_targets" in updated and updated["molecular_targets"] is not None:
        updated["molecular_targets"] = deepcopy(updated["molecular_targets"])
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

    causal_nodes_updated = 0
    molecular_targets_updated = 0
    protein_examples_added = 0
    any_changed = False

    for node_spec in plan_entry.get("causal_node_examples") or []:
        graph_id = str(node_spec["graph_id"])
        node_id = str(node_spec["node_id"])
        expected_label = str(node_spec["node_label"])
        graphs = updated.get("causal_graphs") or []
        matched_node: dict[str, Any] | None = None
        for graph in graphs:
            if graph.get("graph_id") != graph_id:
                continue
            for node in graph.get("nodes") or []:
                if node.get("node_id") == node_id:
                    matched_node = node
                    break
        if matched_node is None:
            raise ValueError(f"{identifier}: causal node {graph_id}.{node_id} not found")
        if matched_node.get("node_type") != "GENE_OR_PROTEIN":
            raise ValueError(
                f"{identifier}: causal node {graph_id}.{node_id} has node_type "
                f"{matched_node.get('node_type')!r}, expected 'GENE_OR_PROTEIN'"
            )
        if matched_node.get("label") != expected_label:
            raise ValueError(
                f"{identifier}: causal node {graph_id}.{node_id} label "
                f"{matched_node.get('label')!r} != expected {expected_label!r}"
            )
        merged, count, changed = _merge_protein_examples(
            matched_node.get("protein_examples"),
            node_spec["protein_examples"],
            context=f"{identifier} {graph_id}.{node_id}",
        )
        if changed:
            matched_node["protein_examples"] = merged
            causal_nodes_updated += 1
            protein_examples_added += count
            any_changed = True

    for target_spec in plan_entry.get("molecular_target_examples") or []:
        source = str(target_spec.get("source") or "PRIMARY_LITERATURE")
        target_label = str(target_spec["target_label"])
        target_reference = str(target_spec["target_reference"])
        targets = updated.get("molecular_targets") or []
        matched_target: dict[str, Any] | None = None
        for target in targets:
            if target.get("source") != source:
                continue
            if target.get("target_label") != target_label:
                continue
            refs = {
                str(ev.get("reference") or "").strip()
                for ev in (target.get("evidence") or [])
                if isinstance(ev, dict)
            }
            if target_reference in refs:
                matched_target = target
                break
        if matched_target is None:
            raise ValueError(
                f"{identifier}: molecular_target ({source}, {target_label!r}, {target_reference}) not found"
            )
        target_type = matched_target.get("target_type")
        if target_type not in ALLOWED_MOLECULAR_TARGET_TYPES:
            raise ValueError(
                f"{identifier}: molecular_target {target_label!r} has target_type "
                f"{target_type!r}, expected one of {sorted(ALLOWED_MOLECULAR_TARGET_TYPES)}"
            )
        merged, count, changed = _merge_protein_examples(
            matched_target.get("protein_examples"),
            target_spec["protein_examples"],
            context=f"{identifier} molecular_target {target_label!r}",
        )
        if changed:
            matched_target["protein_examples"] = merged
            molecular_targets_updated += 1
            protein_examples_added += count
            any_changed = True

    for graph in updated.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            if node.get("node_type") != "GENE_OR_PROTEIN" and node.get("protein_examples"):
                raise ValueError(
                    f"{identifier}: non-GENE_OR_PROTEIN causal node "
                    f"{graph.get('graph_id')}.{node.get('node_id')} "
                    f"(node_type={node.get('node_type')!r}) must not carry protein_examples"
                )
    for target in updated.get("molecular_targets") or []:
        if target.get("protein_examples") and target.get("target_type") not in ALLOWED_MOLECULAR_TARGET_TYPES:
            raise ValueError(
                f"{identifier}: molecular_target {target.get('target_label')!r} "
                f"(target_type={target.get('target_type')!r}) must not carry protein_examples"
            )

    return updated, causal_nodes_updated, molecular_targets_updated, protein_examples_added, any_changed


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


def verify_corpus_protein_examples_accounting(
    records: list[tuple[Path, dict[str, Any]]],
    plan: dict[str, Any] | None = None,
    *,
    root: Path = REPO_ROOT,
) -> dict[str, int]:
    """Verify corpus-wide accounting for causal_graphs and PRIMARY_LITERATURE molecular_targets."""
    loaded_plan = load_uniprot_examples_plan(DEFAULT_PLAN_PATH) if plan is None else plan
    held_entries = loaded_plan.get("held_targets") or []
    held_graphs: dict[tuple[str, str], dict[str, Any]] = {}
    held_targets: dict[tuple[str, str, str], dict[str, Any]] = {}
    for entry in held_entries:
        key = validate_held_target_entry(entry)
        if key[0] == "causal_graphs":
            held_graphs[(key[1], key[2])] = entry
        else:
            held_targets[(key[1], key[2], key[3])] = entry

    seen_held_graphs: set[tuple[str, str]] = set()
    seen_held_targets: set[tuple[str, str, str]] = set()
    causal_graphs_total = 0
    causal_graphs_with_protein_nodes = 0
    causal_graphs_held = 0
    gene_or_protein_nodes = 0
    primary_literature_targets_total = 0
    primary_literature_targets_populated = 0
    primary_literature_targets_held = 0

    for path, doc in records:
        identifier = str(doc.get("identifier") or "")
        label = str(doc.get("label") or "")
        rel_path = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)

        for graph in doc.get("causal_graphs") or []:
            causal_graphs_total += 1
            graph_id = str(graph.get("graph_id") or "")
            gp_count = 0
            for node in graph.get("nodes") or []:
                node_id = str(node.get("node_id") or "")
                node_type = node.get("node_type")
                examples = node.get("protein_examples")
                if node_type == "GENE_OR_PROTEIN":
                    gp_count += 1
                    gene_or_protein_nodes += 1
                    if not isinstance(examples, list) or not examples:
                        raise ValueError(
                            f"{rel_path}: GENE_OR_PROTEIN node {graph_id}.{node_id} missing protein_examples"
                        )
                    seen_uids: set[str] = set()
                    for ex in examples:
                        norm = validate_protein_example_spec(
                            ex, context=f"{rel_path} {graph_id}.{node_id}"
                        )
                        if norm["uniprot_id"] in seen_uids:
                            raise ValueError(
                                f"{rel_path} {graph_id}.{node_id}: duplicate {norm['uniprot_id']}"
                            )
                        seen_uids.add(norm["uniprot_id"])
                elif examples:
                    raise ValueError(
                        f"{rel_path}: non-GENE_OR_PROTEIN causal node {graph_id}.{node_id} "
                        f"(node_type={node_type!r}) must not carry protein_examples"
                    )
            gkey = (identifier, graph_id)
            if gp_count > 0:
                causal_graphs_with_protein_nodes += 1
                if gkey in held_graphs:
                    raise ValueError(
                        f"{rel_path}: causal graph {graph_id} has GENE_OR_PROTEIN nodes "
                        "and must not be listed in held_targets"
                    )
            else:
                if gkey not in held_graphs:
                    raise ValueError(
                        f"{rel_path}: causal graph {graph_id} has 0 GENE_OR_PROTEIN nodes "
                        "and is not accounted for in held_targets"
                    )
                held_item = held_graphs[gkey]
                if held_item["label"] != label or held_item["path"] != rel_path:
                    raise ValueError(
                        f"{rel_path}: held causal_graphs metadata mismatch for {gkey}"
                    )
                seen_held_graphs.add(gkey)
                causal_graphs_held += 1

        for target in doc.get("molecular_targets") or []:
            target_label = str(target.get("target_label") or "")
            target_type = str(target.get("target_type") or "")
            examples = target.get("protein_examples")
            if examples:
                if target_type not in ALLOWED_MOLECULAR_TARGET_TYPES:
                    raise ValueError(
                        f"{rel_path}: molecular_target {target_label!r} "
                        f"(target_type={target_type!r}) must not carry protein_examples"
                    )
                seen_uids = set()
                for ex in examples:
                    norm = validate_protein_example_spec(
                        ex, context=f"{rel_path} molecular_target {target_label!r}"
                    )
                    if norm["uniprot_id"] in seen_uids:
                        raise ValueError(
                            f"{rel_path} molecular_target {target_label!r}: "
                            f"duplicate {norm['uniprot_id']}"
                        )
                    seen_uids.add(norm["uniprot_id"])

            if target.get("source") != "PRIMARY_LITERATURE":
                continue

            primary_literature_targets_total += 1
            refs = [
                str(ev.get("reference") or "").strip()
                for ev in (target.get("evidence") or [])
                if isinstance(ev, dict) and ev.get("reference")
            ]
            first_ref = refs[0] if refs else ""
            tkey = (identifier, target_label, first_ref)
            if examples:
                primary_literature_targets_populated += 1
                if tkey in held_targets:
                    raise ValueError(
                        f"{rel_path}: populated PRIMARY_LITERATURE target {tkey} "
                        "must not also appear in held_targets"
                    )
            else:
                if tkey not in held_targets:
                    raise ValueError(
                        f"{rel_path}: unpopulated PRIMARY_LITERATURE target {tkey} "
                        "is not accounted for in held_targets"
                    )
                held_item = held_targets[tkey]
                if (
                    held_item["label"] != label
                    or held_item["path"] != rel_path
                    or held_item["target_type"] != target_type
                ):
                    raise ValueError(
                        f"{rel_path}: held molecular_targets metadata mismatch for {tkey}"
                    )
                seen_held_targets.add(tkey)
                primary_literature_targets_held += 1

    unmatched_graphs = set(held_graphs) - seen_held_graphs
    if unmatched_graphs:
        raise ValueError(f"Stale held causal_graphs entries not found in corpus: {sorted(unmatched_graphs)}")
    unmatched_targets = set(held_targets) - seen_held_targets
    if unmatched_targets:
        raise ValueError(
            f"Stale held molecular_targets entries not found in corpus: {sorted(unmatched_targets)}"
        )

    return {
        "causal_graphs_total": causal_graphs_total,
        "causal_graphs_with_protein_nodes": causal_graphs_with_protein_nodes,
        "causal_graphs_held": causal_graphs_held,
        "gene_or_protein_nodes": gene_or_protein_nodes,
        "primary_literature_targets_total": primary_literature_targets_total,
        "primary_literature_targets_populated": primary_literature_targets_populated,
        "primary_literature_targets_held": primary_literature_targets_held,
    }


def apply_uniprot_examples_plan(
    root: Path = REPO_ROOT,
    plan_path: Path = DEFAULT_PLAN_PATH,
    *,
    only_identifiers: set[str] | None = None,
    apply: bool = False,
    receipt_path: Path | None = DEFAULT_RECEIPT_PATH,
    curator: str = "antigravity",
    timestamp: str | None = None,
    llm_assisted: bool = True,
) -> list[PlannedRecordResult]:
    """Evaluate or apply the curated UniProt protein examples plan."""
    plan = load_uniprot_examples_plan(plan_path)
    default_action = str(plan.get("curation_action") or "CURATED_UNIPROT_PROTEIN_EXAMPLES")
    results: list[PlannedRecordResult] = []
    receipt_records: list[dict[str, Any]] = []

    for entry in plan["records"]:
        identifier = str(entry["identifier"])
        if only_identifiers is not None and identifier not in only_identifiers:
            continue
        record_path = resolve_record_path(root, entry)
        before_data = _load_yaml_path(record_path)

        (
            updated_data,
            causal_nodes_updated,
            molecular_targets_updated,
            protein_examples_added,
            changed,
        ) = apply_planned_examples_to_record_data(before_data, entry)

        changes_text = str(
            entry.get("changes")
            or (
                f"Added {protein_examples_added} curated UniProt protein example(s) across "
                f"{causal_nodes_updated} causal graph node(s) and "
                f"{molecular_targets_updated} primary-literature molecular target(s)."
            )
        )

        if changed and apply:
            before_sha = _file_sha256(record_path)
            before_history_len = len(before_data.get("curation_history") or [])
            unchanged_before = {
                k: v
                for k, v in before_data.items()
                if k not in {"causal_graphs", "molecular_targets", "curation_history"}
            }
            unchanged_before_sha = _json_sha256(unchanged_before)

            causal_node_deltas: list[dict[str, Any]] = []
            for gi, (before_g, after_g) in enumerate(
                zip(
                    before_data.get("causal_graphs") or [],
                    updated_data.get("causal_graphs") or [],
                    strict=True,
                )
            ):
                for ni, (before_n, after_n) in enumerate(
                    zip(before_g.get("nodes") or [], after_g.get("nodes") or [], strict=True)
                ):
                    if before_n != after_n:
                        causal_node_deltas.append(
                            {
                                "graph_index": gi,
                                "graph_id": after_g["graph_id"],
                                "node_index": ni,
                                "node_id": after_n["node_id"],
                                "changed_fields": ["protein_examples"],
                                "before_protein_examples": deepcopy(before_n.get("protein_examples")),
                                "after_protein_examples": deepcopy(after_n.get("protein_examples")),
                            }
                        )

            molecular_target_deltas: list[dict[str, Any]] = []
            for ti, (before_t, after_t) in enumerate(
                zip(
                    before_data.get("molecular_targets") or [],
                    updated_data.get("molecular_targets") or [],
                    strict=True,
                )
            ):
                if before_t != after_t:
                    molecular_target_deltas.append(
                        {
                            "index": ti,
                            "source": after_t["source"],
                            "target_label": after_t["target_label"],
                            "changed_fields": ["protein_examples"],
                            "before_protein_examples": deepcopy(before_t.get("protein_examples")),
                            "after_protein_examples": deepcopy(after_t.get("protein_examples")),
                        }
                    )

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
                if k not in {"causal_graphs", "molecular_targets", "curation_history"}
            }
            unchanged_after_sha = _json_sha256(unchanged_after)
            if unchanged_after_sha != unchanged_before_sha:
                raise RuntimeError(f"Unchanged fields hash mutated for {identifier}")
            receipt_records.append(
                {
                    "identifier": identifier,
                    "label": str(entry["label"]),
                    "path": record_path.relative_to(root).as_posix(),
                    "before_sha256": before_sha,
                    "after_sha256": after_sha,
                    "unchanged_fields_sha256": unchanged_after_sha,
                    "causal_nodes_updated": causal_nodes_updated,
                    "molecular_targets_updated": molecular_targets_updated,
                    "protein_examples_added": protein_examples_added,
                    "history_events_added": 1,
                    "curation_history_before_len": before_history_len,
                    "curation_history_after_len": len(after_data.get("curation_history") or []),
                    "causal_node_deltas": causal_node_deltas,
                    "molecular_target_deltas": molecular_target_deltas,
                    "added_history_event": deepcopy((after_data.get("curation_history") or [])[-1]),
                }
            )

        results.append(
            PlannedRecordResult(
                identifier=identifier,
                label=str(entry["label"]),
                path=record_path,
                changed=changed,
                causal_nodes_updated=causal_nodes_updated,
                molecular_targets_updated=molecular_targets_updated,
                protein_examples_added=protein_examples_added,
                changes=changes_text,
            )
        )

    if apply and receipt_path is not None and only_identifiers is None and receipt_records:
        existing_by_id: dict[str, dict[str, Any]] = {}
        if receipt_path.exists():
            existing_payload = json.loads(receipt_path.read_text(encoding="utf-8"))
            for item in existing_payload.get("record_deltas") or []:
                if isinstance(item, dict) and item.get("identifier"):
                    existing_by_id[str(item["identifier"])] = item
        for item in receipt_records:
            existing_by_id[str(item["identifier"])] = item
        ordered_deltas = [
            existing_by_id[str(entry["identifier"])]
            for entry in plan["records"]
            if str(entry["identifier"]) in existing_by_id
        ]
        rel_plan = (
            plan_path.relative_to(root).as_posix()
            if plan_path.is_relative_to(root)
            else str(plan_path)
        )
        payload = {
            "schema_version": 1,
            "task": str(plan.get("task") or "uniprot_protein_examples_curation"),
            "plan_path": rel_plan,
            "record_count": len(ordered_deltas),
            "record_deltas": ordered_deltas,
        }
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    return results

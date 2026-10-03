"""Shared minimum assay-context gate; not a certification of submitted methods."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

DEFAULT_REVIEW_MAP = Path(__file__).resolve().parents[1] / "curation/ncbi_ast_assay_review.json"
CONTEXT_FIELDS = ("method", "platform", "vendor", "reagent", "measurement")
REVIEW_REFERENCE = "https://github.com/CultureBotAI/AntibioticMech/blob/main/curation/ncbi_ast_assay_review.json"

# Generic vessels and local/unknown method labels cannot identify an assay.
UNINFORMATIVE_CONTEXT = frozenset({
    "", "0", "na", "none", "null", "missing", "unknown", "unspecified",
    "notapplicable", "notavailable", "notcollected", "notprovided", "notreported",
    "other", "inhouse", "96wellplate",
})


def has_informative_assay_context(*values: str) -> bool:
    return any(
        re.sub(r"[^a-z0-9]", "", value.casefold()) not in UNINFORMATIVE_CONTEXT
        for value in values
    )


def assay_signature(row: dict) -> tuple[str, ...]:
    measurement = "+".join(name for name, field in (
        ("MIC", "mic_value"), ("DISK", "disk_diffusion_value"),
    ) if row.get(field))
    return tuple(row[field] for field in CONTEXT_FIELDS[:-1]) + (measurement,)


@dataclass(frozen=True)
class AssayReview:
    version: str
    source_version: str
    reviewed_on: str
    candidate_sha256: str
    decisions: dict[tuple[str, ...], dict]

    def decision_for(self, row: dict) -> dict:
        if row["source_version"] != self.source_version:
            raise ValueError("assay review source_version does not match the AST report")
        signature = assay_signature(row)
        if signature not in self.decisions:
            raise ValueError(f"unreviewed NCBI AST assay context: {signature!r}")
        return self.decisions[signature]

    def require_accepted(self, row: dict) -> dict:
        decision = self.decision_for(row)
        if decision["decision"] != "ACCEPT":
            raise ValueError(f"quarantined NCBI AST assay context: {decision['basis']}")
        return decision


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate assay-review JSON key: {key}")
        result[key] = value
    return result


def read_assay_review(path: Path = DEFAULT_REVIEW_MAP) -> AssayReview:
    payload = path.read_bytes()
    data = json.loads(payload, object_pairs_hook=_unique_json_object)
    expected = {"source_version", "reviewed_on", "candidate_sha256", "rationales", "contexts"}
    if not isinstance(data, dict) or set(data) != expected:
        raise ValueError("unexpected assay-review root fields")
    for field in ("source_version", "reviewed_on", "candidate_sha256"):
        value = data[field]
        if not isinstance(value, str) or not value or value != value.strip():
            raise ValueError(f"invalid assay-review {field}")
    if date.fromisoformat(data["reviewed_on"]).isoformat() != data["reviewed_on"]:
        raise ValueError("invalid assay-review reviewed_on")
    if not re.fullmatch(r"[a-f0-9]{64}", data["candidate_sha256"]):
        raise ValueError("invalid assay-review candidate_sha256")
    rationales = data["rationales"]
    if not isinstance(rationales, dict) or not rationales:
        raise ValueError("assay-review rationales must be a nonempty object")
    for basis, rationale in rationales.items():
        if not isinstance(rationale, dict) or set(rationale) != {"decision", "explanation", "references"}:
            raise ValueError(f"invalid assay-review rationale: {basis}")
        if rationale["decision"] not in ("ACCEPT", "QUARANTINE"):
            raise ValueError(f"invalid assay-review decision: {basis}")
        if not isinstance(rationale["explanation"], str) or not rationale["explanation"].strip():
            raise ValueError(f"assay-review rationale needs an explanation: {basis}")
        refs = rationale["references"]
        if not isinstance(refs, list) or not refs or any(
            not isinstance(ref, str) or not ref.startswith("https://") or any(c.isspace() for c in ref)
            for ref in refs
        ):
            raise ValueError(f"assay-review rationale needs source URLs: {basis}")
    if not isinstance(data["contexts"], list) or not data["contexts"]:
        raise ValueError("assay-review contexts must be a nonempty list")
    decisions = {}
    for context in data["contexts"]:
        if not isinstance(context, dict) or set(context) != {*CONTEXT_FIELDS, "basis"}:
            raise ValueError("unexpected assay-review context fields")
        if any(not isinstance(v, str) or v != v.strip() or any(c in v for c in "\t\r\n")
               for v in context.values()):
            raise ValueError("invalid assay-review context value")
        if context["measurement"] not in ("MIC", "DISK", "MIC+DISK"):
            raise ValueError("invalid assay-review measurement kind")
        if context["basis"] not in rationales:
            raise ValueError("unknown assay-review rationale")
        key = tuple(context[field] for field in CONTEXT_FIELDS)
        if key in decisions:
            raise ValueError("duplicate assay-review context")
        decisions[key] = {"basis": context["basis"], **rationales[context["basis"]]}
    return AssayReview(
        "assay-review-sha256:" + hashlib.sha256(payload).hexdigest(),
        data["source_version"], data["reviewed_on"], data["candidate_sha256"], decisions,
    )


def apply_assay_review(rows: list[dict], review: AssayReview) -> tuple[list[dict], list[dict]]:
    accepted = []
    counts: Counter = Counter()
    for row in rows:
        decision = review.decision_for(row)
        counts[(decision["basis"], decision["decision"], "groups")] += 1
        counts[(decision["basis"], decision["decision"], "measurements")] += int(row["ast_row_count"])
        if decision["decision"] == "ACCEPT":
            accepted.append(row)
    summaries = [
        {"basis": basis, "decision": decision, "groups": count,
         "measurements": counts[(basis, decision, "measurements")]}
        for (basis, decision, kind), count in sorted(counts.items()) if kind == "groups"
    ]
    return accepted, summaries

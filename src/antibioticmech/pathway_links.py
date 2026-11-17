"""Offline verification of curator-owned links to a pinned PathwayMech index."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELATIONS = {"TARGETS_PATHWAY_COMPONENT", "RELATED_PATHWAY_ACTIVITY"}


def load_index(root: Path = ROOT) -> tuple[str, dict[str, dict]]:
    pin = json.loads((root / "conf/pathwaymech_pin.json").read_text())
    if not re.fullmatch(r"[a-f0-9]{40}", pin.get("commit", "")):
        raise ValueError("PathwayMech pin requires a full commit")
    path = Path(pin["index_path"])
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("PathwayMech index must be repository-relative")
    payload = (root / path).read_bytes()
    if hashlib.sha256(payload).hexdigest() != pin["index_sha256"]:
        raise ValueError("PathwayMech index differs from pinned bytes")
    data = json.loads(payload)
    if data.get("format") != "pathwaymech-pathway-index/1":
        raise ValueError("unsupported PathwayMech index")
    rows = data["records"]
    index = {row["id"]: row for row in rows}
    if not index or len(index) != len(rows):
        raise ValueError("empty or ambiguous PathwayMech index")
    return pin["commit"], index


def check_links(record: dict, commit: str, index: dict[str, dict]) -> list[str]:
    errors = []
    for link in record.get("related_records") or []:
        if link.get("corpus") != "PathwayMech":
            continue
        identifier = link.get("identifier")
        if identifier not in index:
            errors.append(f"unknown PathwayMech record {identifier!r}")
        if link.get("source_version") != commit:
            errors.append("PathwayMech source_version differs from pinned index")
        if link.get("relation") not in RELATIONS:
            errors.append("unsupported PathwayMech relation")
        if not isinstance(link.get("basis"), str) or not link["basis"].strip():
            errors.append("PathwayMech link requires an evidence basis")
    return errors

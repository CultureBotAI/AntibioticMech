"""Validated, checksum-pinned NCBI isolate identity metadata for AST joins."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ISOLATE_SOURCE = "NCBI_PATHOGEN_DETECTION_ISOLATES"
ISOLATE_VERSION_PREFIX = "isolates-browser-sha256:"
ISOLATE_REFERENCE = "https://www.ncbi.nlm.nih.gov/pathogens/isolates/"
ISOLATE_PROVENANCE_COLUMNS = ["isolate_source_version", "isolate_source_retrieved_on"]
VERSION_PATTERN = re.compile(r"isolates-browser-sha256:[a-f0-9]{64}")
TARGET_PATTERN = re.compile(r"PDT[0-9]+\.[0-9]+")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_iso_date(value: str, prefix: str) -> None:
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{prefix}: expected an ISO date") from error
    if parsed.isoformat() != value:
        raise ValueError(f"{prefix}: expected an ISO date")


def require_isolate_provenance(row: dict, prefix: str) -> tuple[str, str]:
    version, retrieved_on = (row[field] for field in ISOLATE_PROVENANCE_COLUMNS)
    if not version and not retrieved_on:
        return version, retrieved_on
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"{prefix}: invalid isolate_source_version")
    require_iso_date(retrieved_on, f"{prefix}: isolate_source_retrieved_on")
    if not TARGET_PATTERN.fullmatch(row["target_accession"]):
        raise ValueError(f"{prefix}: isolate provenance requires a versioned target_accession")
    if not row["taxon_id"]:
        raise ValueError(f"{prefix}: isolate provenance requires taxon_id")
    return version, retrieved_on


def read_isolate_export(path: Path) -> dict[str, dict[str, str]]:
    """Accept complete native retrieve responses; never derive phenotype evidence."""
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict) or payload.get("success") is not True:
        raise ValueError(f"{path}: unsuccessful isolate export")
    data = payload.get("ngout", {}).get("data", {})
    records = data.get("content")
    count = data.get("totalCount")
    if (
        type(count) is not int or count <= 0 or not isinstance(records, list)
        or len(records) != count
    ):
        raise ValueError(f"{path}: incomplete isolate export")
    index = {}
    patterns = {
        "target_acc": TARGET_PATTERN.pattern,
        "biosample_acc": r"SAM(N|D|EA)[0-9]+",
        "bioproject_acc": r"PRJ(NA|EB|DB)[0-9]+",
        "asm_acc": r"GC[AF]_[0-9]+\.[0-9]+",
    }
    for number, raw in enumerate(records, start=1):
        prefix = f"{path}: isolate {number}"
        if not isinstance(raw, dict):
            raise ValueError(f"{prefix}: expected an object")
        record = {}
        for field in (*patterns, "scientific_name", "strain"):
            value = raw.get(field, "")
            if (
                not isinstance(value, str) or value != value.strip()
                or any(char in value for char in "\t\r\n")
            ):
                raise ValueError(f"{prefix}: invalid {field}")
            if not value and field not in {"asm_acc", "strain"}:
                raise ValueError(f"{prefix}: missing {field}")
            if value and field in patterns and not re.fullmatch(patterns[field], value):
                raise ValueError(f"{prefix}: invalid {field}")
            record[field] = value
        taxid = raw.get("taxid")
        if type(taxid) not in (int, str) or not re.fullmatch(r"[1-9][0-9]*", str(taxid)):
            raise ValueError(f"{prefix}: invalid taxid")
        record["taxid"] = str(taxid)
        target = record["target_acc"]
        if target in index:
            raise ValueError(f"{prefix}: duplicate target_acc {target}")
        index[target] = record
    return index


@dataclass(frozen=True)
class IsolateSnapshot:
    records: dict[str, dict[str, str]]
    source_version: str
    source_retrieved_on: str


def load_isolate_snapshot(directory: Path) -> IsolateSnapshot:
    with (directory / "snapshot.json").open(encoding="utf-8") as handle:
        metadata = json.load(handle)
    if metadata.get("source") != ISOLATE_SOURCE or metadata.get("file") != "isolates.json":
        raise ValueError(f"{directory}: not an NCBI isolate snapshot")
    path = directory / "isolates.json"
    checksum = file_sha256(path)
    if (
        metadata.get("sha256") != checksum
        or metadata.get("source_version") != ISOLATE_VERSION_PREFIX + checksum
        or metadata.get("bytes") != path.stat().st_size
    ):
        raise ValueError(f"{directory}: isolate snapshot checksum/version/size mismatch")
    retrieved_on = metadata.get("source_retrieved_on")
    require_iso_date(retrieved_on, f"{directory}: source_retrieved_on")
    records = read_isolate_export(path)
    if any(
        type(metadata.get(field)) is not int or metadata[field] != len(records)
        for field in ("rows", "count_before", "count_after")
    ):
        raise ValueError(f"{directory}: isolate snapshot counts disagree")
    return IsolateSnapshot(records, ISOLATE_VERSION_PREFIX + checksum, retrieved_on)

"""Lossless, content-addressed storage for large source-owned activity slices."""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import math
import os
import re
import tempfile
import zlib
from datetime import date
from pathlib import Path

import yaml

FORMAT = "antibioticmech-activity-jsonl-v1"
COLLECTION_SIZE = 500
MAX_BYTES = 16 * 1024 * 1024
SOURCE = "NCBI_AST"
SOURCE_FIELDS = ("source", "source_version", "source_retrieved_on")
REFERENCE_FIELDS = {
    "format", "path", "sha256", "byte_size", "offset", "observation_count",
    "measurement_count", *SOURCE_FIELDS,
}
ARTIFACT_NAME = re.compile(r"activity-([a-f0-9]{64})\.jsonl\.gz")


def _json(value) -> bytes:
    return (json.dumps(value, ensure_ascii=True, allow_nan=False, separators=(",", ":")) + "\n").encode()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate collection JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError(f"non-finite collection JSON value: {value}")


def _finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        _reject_constant(value)
    return number


def _identity(doc: dict) -> dict:
    identifier = doc.get("identifier")
    structure = doc.get("chemical_structure")
    key = structure.get("standard_inchi_key") if isinstance(structure, dict) else None
    if not isinstance(identifier, str) or not identifier or not isinstance(key, str) or not re.fullmatch(
        r"[A-Z]{14}-[A-Z]{10}-[A-Z]", key,
    ):
        raise ValueError("activity collection requires an exact record identifier and InChIKey")
    return {"identifier": identifier, "standard_inchi_key": key}


def _positive(value, name, *, minimum=1, maximum=None):
    if type(value) is not int or value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"invalid collection {name}")
    return value


def _source(metadata):
    if metadata.get("source") != SOURCE:
        raise ValueError("unsupported activity collection source")
    if not isinstance(metadata.get("source_version"), str) or not metadata["source_version"].strip():
        raise ValueError("missing collection source version")
    value = metadata.get("source_retrieved_on")
    if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
        raise ValueError("invalid collection retrieval date")
    return {key: metadata[key] for key in SOURCE_FIELDS}


def _check_rows(rows, metadata):
    identifiers = set()
    measurements = 0
    for row in rows:
        if not isinstance(row, dict) or any(row.get(k) != metadata[k] for k in SOURCE_FIELDS):
            raise ValueError("collection row has different source provenance")
        identifier = row.get("source_observation_id")
        if not isinstance(identifier, str) or not identifier or identifier in identifiers:
            raise ValueError("missing or duplicate collection observation ID")
        identifiers.add(identifier)
        measurements += _positive(row.get("measurement_count"), "measurement count")
    return measurements


def _observations(doc):
    rows = doc.get("activity_spectrum", [])
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ValueError("activity spectrum must be a list of observation mappings")
    return rows


def _unique_ast_ids(rows):
    identifiers = set()
    for row in rows:
        if row.get("source") == SOURCE:
            identifier = row.get("source_observation_id")
            if not isinstance(identifier, str) or not identifier or identifier in identifiers:
                raise ValueError("duplicate or missing AST observation across collections/inline rows")
            identifiers.add(identifier)


def pack_activities(doc: dict) -> tuple[dict, dict[str, bytes]]:
    """Return physical record and artifacts without changing the logical record."""
    if "activity_collections" in doc:
        raise ValueError("expand existing activity collections before packing")
    observations = _observations(doc)
    references, inline, artifacts = [], [], {}
    start = 0
    while start < len(observations):
        row = observations[start]
        end = start + 1
        while end < len(observations) and all(
            observations[end].get(k) == row.get(k) for k in SOURCE_FIELDS
        ):
            end += 1
        if row.get("source") != SOURCE or end - start < COLLECTION_SIZE:
            inline.extend(observations[start:end])
        else:
            metadata = _source(row)
            header = {"format": FORMAT, **_identity(doc), **metadata}
            for offset in range(start, end, COLLECTION_SIZE):
                chunk = observations[offset:min(offset + COLLECTION_SIZE, end)]
                measurements = _check_rows(chunk, metadata)
                payload = _json(header) + b"".join(_json(item) for item in chunk)
                if len(payload) > MAX_BYTES:
                    raise ValueError("activity collection exceeds the uncompressed size limit")
                stream = io.BytesIO()
                with gzip.GzipFile(filename="", mode="wb", fileobj=stream, mtime=0) as handle:
                    handle.write(payload)
                compressed = stream.getvalue()
                if len(compressed) > MAX_BYTES:
                    raise ValueError("activity collection exceeds the compressed size limit")
                checksum = hashlib.sha256(compressed).hexdigest()
                name = f"activity-{checksum}.jsonl.gz"
                artifacts[name] = compressed
                references.append({
                    "format": FORMAT, "path": name, "sha256": checksum,
                    "byte_size": len(compressed), "offset": offset,
                    "observation_count": len(chunk), "measurement_count": measurements,
                    **metadata,
                })
        start = end
    if not references:
        return doc, artifacts
    _unique_ast_ids(observations)
    physical = {}
    for key, value in doc.items():
        if key == "activity_spectrum":
            if inline:
                physical[key] = inline
            physical["activity_collections"] = references
        else:
            physical[key] = value
    return physical, artifacts


def _decode(payload: bytes) -> list:
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") as handle:
            unpacked = handle.read(MAX_BYTES + 1)
        if len(unpacked) > MAX_BYTES or not unpacked.endswith(b"\n"):
            raise ValueError("oversized or incomplete activity collection")
        lines = unpacked.splitlines()
        if not 2 <= len(lines) <= COLLECTION_SIZE + 1:
            raise ValueError("activity collection row count mismatch")
        return [json.loads(line, object_pairs_hook=_unique_object, parse_constant=_reject_constant,
                           parse_float=_finite_float) for line in lines]
    except (OSError, EOFError, UnicodeError, RecursionError, zlib.error) as error:
        raise ValueError("invalid compressed activity collection") from error


def read_collection(reference: dict, doc: dict, record_path: Path) -> list[dict]:
    if not isinstance(reference, dict) or set(reference) != REFERENCE_FIELDS:
        raise ValueError("invalid activity collection reference fields")
    checksum = reference["sha256"]
    if not isinstance(checksum, str) or not re.fullmatch(r"[a-f0-9]{64}", checksum):
        raise ValueError("invalid activity collection checksum")
    if reference["format"] != FORMAT or reference["path"] != f"activity-{checksum}.jsonl.gz":
        raise ValueError("unsupported activity collection format or path")
    count = _positive(reference["observation_count"], "observation count", maximum=COLLECTION_SIZE)
    size = _positive(reference["byte_size"], "byte size", maximum=MAX_BYTES)
    _positive(reference["offset"], "offset", minimum=0)
    _positive(reference["measurement_count"], "measurement count")
    metadata = _source(reference)
    path = record_path.parent / reference["path"]
    if path.is_symlink() or not path.is_file() or path.resolve().parent != record_path.parent.resolve():
        raise ValueError("activity collection must be a regular sibling artifact")
    with path.open("rb") as handle:
        payload = handle.read(MAX_BYTES + 1)
    if len(payload) != size or hashlib.sha256(payload).hexdigest() != checksum:
        raise ValueError("activity collection bytes do not match its reference")
    objects = _decode(payload)
    if len(objects) != count + 1:
        raise ValueError("activity collection row count mismatch")
    if objects[0] != {"format": FORMAT, **_identity(doc), **metadata}:
        raise ValueError("activity collection chemical identity or provenance mismatch")
    if _check_rows(objects[1:], metadata) != reference["measurement_count"]:
        raise ValueError("activity collection measurement count mismatch")
    return objects[1:]


def expand_activities(doc: dict, record_path: Path) -> dict:
    """Resolve every collection with identity, integrity, count, and order checks."""
    if "activity_collections" not in doc:
        return doc
    references = doc["activity_collections"]
    if not isinstance(references, list) or not references:
        raise ValueError("activity collections must be a nonempty list")
    observations = list(_observations(doc))
    previous_end = 0
    for reference in references:
        rows = read_collection(reference, doc, record_path)
        offset = reference["offset"]
        if offset < previous_end or offset > len(observations):
            raise ValueError("activity collection offsets overlap or leave a gap")
        observations[offset:offset] = rows
        previous_end = offset + len(rows)
    _unique_ast_ids(observations)
    expanded = {}
    for key, value in doc.items():
        if key in {"activity_collections", "activity_spectrum"}:
            expanded["activity_spectrum"] = observations
        else:
            expanded[key] = value
    return expanded


def load_record(path: Path) -> dict:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError(f"{path}: expected a record mapping")
    return expand_activities(document, path)


def write_artifacts(artifacts: dict[str, bytes], directory: Path) -> None:
    """Install immutable artifacts before the record references them."""
    for name, payload in artifacts.items():
        match = ARTIFACT_NAME.fullmatch(name)
        if not match or hashlib.sha256(payload).hexdigest() != match[1] or len(payload) > MAX_BYTES:
            raise ValueError("invalid activity artifact name or content address")
    for name, payload in artifacts.items():
        destination = directory / name
        if destination.is_symlink():
            raise ValueError("refusing a symlink at an activity artifact path")
        if destination.exists():
            if destination.read_bytes() != payload:
                raise ValueError("existing activity artifact does not match its content address")
            continue
        with tempfile.NamedTemporaryFile(prefix=".activity-", dir=directory) as temporary:
            temporary.write(payload)
            temporary.flush()
            try:
                os.link(temporary.name, destination)
            except FileExistsError:
                if destination.is_symlink() or destination.read_bytes() != payload:
                    raise ValueError("concurrent activity artifact has different content") from None


def orphaned_activity_artifacts(root: Path) -> list[Path]:
    """Find owned, valid, unreferenced artifacts; fail before any caller deletes.

    Run only with an exclusive corpus writer, as with the seeder's YAML prune.
    Unknown files are never candidates, even when they have a .jsonl.gz suffix.
    """
    referenced = set()
    for path in sorted(root.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a record mapping")
        expand_activities(doc, path)
        referenced.update(path.parent / ref["path"] for ref in doc.get("activity_collections", []))
    orphans = []
    for path in sorted(root.rglob("activity-*.jsonl.gz")):
        match = ARTIFACT_NAME.fullmatch(path.name)
        if not match or path in referenced:
            continue
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"refusing to prune non-regular activity artifact: {path}")
        with path.open("rb") as handle:
            payload = handle.read(MAX_BYTES + 1)
        if len(payload) > MAX_BYTES or hashlib.sha256(payload).hexdigest() != match[1]:
            raise ValueError(f"refusing to prune corrupt activity artifact: {path}")
        objects = _decode(payload)
        header, rows = objects[0], objects[1:]
        if not isinstance(header, dict):
            raise ValueError(f"invalid activity collection header: {path}")
        metadata = _source(header)
        doc = {"identifier": header.get("identifier"),
               "chemical_structure": {"standard_inchi_key": header.get("standard_inchi_key")}}
        reference = {"format": FORMAT, "path": path.name, "sha256": match[1],
                     "byte_size": len(payload), "offset": 0, "observation_count": len(rows),
                     "measurement_count": _check_rows(rows, metadata), **metadata}
        read_collection(reference, doc, path.parent / "unused.yaml")
        orphans.append(path)
    return orphans

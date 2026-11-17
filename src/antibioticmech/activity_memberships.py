"""Bounded source-isolate registries for grouped activity observations.

Keep observations as assay claims. A registry entry is a source isolate ID,
not a strain name, species assertion, or assembly. Group membership retains
measurement multiplicity and an explicit null for missing sequencing context.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import zlib
from dataclasses import dataclass
from datetime import date
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlsplit

import yaml

from antibioticmech.activity_collections import (
    _finite_float,
    _identity,
    _positive,
    _reject_constant,
    _unique_object,
    expand_activities,
    write_artifacts,
)

FORMAT = "antibioticmech-activity-memberships-v1"
MAX_BYTES = 16 * 1024 * 1024
FIELD = "activity_membership_collections"
ARTIFACT_NAME = re.compile(r"membership-([a-f0-9]{64})\.json\.gz")
SOURCE_FIELDS = (
    "source", "source_version", "source_reference", "source_retrieved_on",
    "source_snapshot_sha256", "activity_inventory_sha256",
)
COUNT_FIELDS = (
    "subject_count", "observation_count", "membership_count", "measurement_count",
    "unlinked_subject_count",
)
REFERENCE_FIELDS = {
    "format", "path", "sha256", "byte_size", "uncompressed_byte_size", *SOURCE_FIELDS, *COUNT_FIELDS,
}
ACCESSIONS = {
    "biosample_accession": r"SAM(N|D|EA)[0-9]+",
    "bioproject_accession": r"PRJ(NA|EB|DB)[0-9]+",
    "run_accession": r"[SED]RR[0-9]+",
}


def json_bytes(value) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(",", ":")) + "\n").encode()


def observation_digest(observation: dict) -> str:
    return hashlib.sha256(json_bytes(observation)).hexdigest()


def _text(value, name):
    if not isinstance(value, str) or not value or value != value.strip() or any(
        ord(char) < 32 for char in value
    ):
        raise ValueError(f"invalid membership {name}")
    return value


def _checksum(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
        raise ValueError("invalid membership checksum")
    return value


def _metadata(value):
    metadata = {key: _text(value.get(key), key) for key in SOURCE_FIELDS}
    for key in ("source_snapshot_sha256", "activity_inventory_sha256"):
        _checksum(metadata[key])
    retrieved = metadata["source_retrieved_on"]
    if date.fromisoformat(retrieved).isoformat() != retrieved:
        raise ValueError("invalid membership retrieval date")
    reference = urlsplit(metadata["source_reference"])
    if reference.scheme != "https" or not reference.hostname or reference.username or reference.password:
        raise ValueError("invalid membership source reference")
    return metadata


def validate_subject(subject):
    if not isinstance(subject, dict) or set(subject) != {"source_isolate_id", "sequencing_context"}:
        raise ValueError("invalid membership subject fields")
    source_id = _text(subject["source_isolate_id"], "source isolate ID")
    context = subject["sequencing_context"]
    if context is not None:
        if not isinstance(context, dict) or set(context) != set(ACCESSIONS):
            raise ValueError("invalid membership sequencing context fields")
        for field, pattern in ACCESSIONS.items():
            if not isinstance(context[field], str) or not re.fullmatch(pattern, context[field]):
                raise ValueError(f"invalid membership {field}")
    return source_id


def _decode(payload: bytes):
    if not isinstance(payload, bytes) or not 0 < len(payload) <= MAX_BYTES:
        raise ValueError("invalid or oversized membership payload")
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(payload)) as handle:
            raw = handle.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES or not raw.endswith(b"\n"):
            raise ValueError("oversized or incomplete membership payload")
        value = json.loads(raw, object_pairs_hook=_unique_object, parse_constant=_reject_constant,
                           parse_float=_finite_float)
        return value, len(raw)
    except (OSError, EOFError, UnicodeError, RecursionError, zlib.error) as error:
        raise ValueError("invalid compressed membership payload") from error


@dataclass(frozen=True)
class MembershipSummary:
    identity: tuple[str, str]
    metadata: tuple[str, ...]
    counts: tuple[int, ...]
    # Each tuple is (source observation ID, observation digest, isolates,
    # measurements, isolates without a WGS join).
    groups: tuple[tuple[str, str, int, int, int], ...]
    uncompressed_byte_size: int


@lru_cache(maxsize=32)
def inspect_payload(payload: bytes) -> MembershipSummary:
    """Cache immutable validation summaries, never mutable decoded registries."""
    value, size = _decode(payload)
    if not isinstance(value, dict) or set(value) != {
        "format", "identifier", "standard_inchi_key", *SOURCE_FIELDS, "subjects", "groups",
    } or value["format"] != FORMAT:
        raise ValueError("invalid membership payload fields or format")
    identity = _identity({"identifier": value["identifier"],
                          "chemical_structure": {"standard_inchi_key": value["standard_inchi_key"]}})
    metadata = _metadata(value)
    subjects, groups = value["subjects"], value["groups"]
    if not isinstance(subjects, list) or not subjects or not isinstance(groups, list) or not groups:
        raise ValueError("membership subjects and groups must be nonempty lists")
    seen_subjects, unlinked = set(), set()
    for index, subject in enumerate(subjects):
        source_id = validate_subject(subject)
        if source_id in seen_subjects:
            raise ValueError("duplicate membership source isolate ID")
        seen_subjects.add(source_id)
        if subject["sequencing_context"] is None:
            unlinked.add(index)
    seen_groups, used_subjects, summaries = set(), set(), []
    measurements = memberships = 0
    for group in groups:
        if not isinstance(group, dict) or set(group) != {
            "source_observation_id", "observation_sha256", "members",
        }:
            raise ValueError("invalid membership group fields")
        group_id = _text(group["source_observation_id"], "observation ID")
        digest = _checksum(group["observation_sha256"])
        if group_id in seen_groups:
            raise ValueError("duplicate membership observation ID")
        seen_groups.add(group_id)
        members = group["members"]
        if not isinstance(members, list) or not members:
            raise ValueError("membership group must have members")
        seen, count = set(), 0
        for member in members:
            if not isinstance(member, dict) or set(member) != {"subject_index", "measurement_count"}:
                raise ValueError("invalid membership member fields")
            index = _positive(member["subject_index"], "subject index", minimum=0,
                              maximum=len(subjects) - 1)
            if index in seen:
                raise ValueError("duplicate subject within membership group")
            seen.add(index)
            count += _positive(member["measurement_count"], "member measurement count")
        used_subjects.update(seen)
        measurements += count
        memberships += len(seen)
        summaries.append((group_id, digest, len(seen), count, len(seen & unlinked)))
    if len(used_subjects) != len(subjects):
        raise ValueError("membership registry contains unreferenced subjects")
    counts = (len(subjects), len(groups), memberships, measurements, len(unlinked))
    return MembershipSummary(tuple(identity.values()), tuple(metadata.values()), counts,
                             tuple(summaries), size)


def make_reference(payload: bytes) -> dict:
    summary = inspect_payload(payload)
    checksum = hashlib.sha256(payload).hexdigest()
    return {
        "format": FORMAT, "path": f"membership-{checksum}.json.gz", "sha256": checksum,
        "byte_size": len(payload), "uncompressed_byte_size": summary.uncompressed_byte_size,
        **dict(zip(SOURCE_FIELDS, summary.metadata, strict=True)),
        **dict(zip(COUNT_FIELDS, summary.counts, strict=True)),
    }


def _observation_map(doc, source, version):
    rows = {}
    for row in doc.get("activity_spectrum", []):
        if row.get("source") != source or row.get("source_version") != version:
            continue
        group_id = _text(row.get("source_observation_id"), "observation ID")
        if group_id in rows:
            raise ValueError("duplicate record observation ID for membership source")
        rows[group_id] = row
    return rows


def build_collection(doc: dict, metadata: dict, groups: dict[str, list[dict]]) -> tuple[dict, bytes]:
    """Normalize source-ID members and bind them to the complete source-owned slice."""
    metadata = _metadata(metadata)
    observations = _observation_map(doc, metadata["source"], metadata["source_version"])
    if not groups or groups.keys() != observations.keys():
        raise ValueError("membership groups do not cover the source-owned observations")
    subjects = {}
    for members in groups.values():
        for member in members:
            subject = {key: member[key] for key in ("source_isolate_id", "sequencing_context")}
            source_id = validate_subject(subject)
            if source_id in subjects and subjects[source_id] != subject:
                raise ValueError("inconsistent sequencing context for source isolate ID")
            subjects[source_id] = subject
    ordered = [subjects[key] for key in sorted(subjects)]
    ordinal = {subject["source_isolate_id"]: index for index, subject in enumerate(ordered)}
    value = {"format": FORMAT, **_identity(doc), **metadata, "subjects": ordered, "groups": [
        {"source_observation_id": group_id, "observation_sha256": observation_digest(observations[group_id]),
         "members": [{"subject_index": ordinal[member["source_isolate_id"]],
                      "measurement_count": member["measurement_count"]}
                     for member in sorted(members, key=lambda item: item["source_isolate_id"])]}
        for group_id, members in sorted(groups.items())
    ]}
    raw = json_bytes(value)
    if len(raw) > MAX_BYTES:
        raise ValueError("membership payload exceeds expanded-byte limit")
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", filename="", mtime=0, compresslevel=6) as handle:
        handle.write(raw)
    payload = buffer.getvalue()
    reference = make_reference(payload)
    validate_memberships({**doc, FIELD: [reference]}, Path("unused.yaml"),
                         artifacts={reference["path"]: payload})
    return reference, payload


def collection_bytes(reference: dict, record_path: Path, *, artifacts: dict | None = None) -> bytes:
    if not isinstance(reference, dict) or set(reference) != REFERENCE_FIELDS:
        raise ValueError("invalid membership reference fields")
    checksum = _checksum(reference["sha256"])
    if reference["format"] != FORMAT or reference["path"] != f"membership-{checksum}.json.gz":
        raise ValueError("invalid membership format or path")
    _positive(reference["byte_size"], "membership byte size", maximum=MAX_BYTES)
    _positive(reference["uncompressed_byte_size"], "membership expanded byte size", maximum=MAX_BYTES)
    if artifacts is not None and reference["path"] in artifacts:
        payload = artifacts[reference["path"]]
    else:
        path = record_path.parent / reference["path"]
        if path.is_symlink() or not path.is_file() or path.resolve().parent != record_path.parent.resolve():
            raise ValueError("membership collection must be a regular sibling artifact")
        with path.open("rb") as handle:
            payload = handle.read(MAX_BYTES + 1)
    if not isinstance(payload, bytes) or len(payload) != reference["byte_size"] or len(payload) > MAX_BYTES:
        raise ValueError("membership byte size mismatch")
    if hashlib.sha256(payload).hexdigest() != checksum:
        raise ValueError("membership checksum mismatch")
    return payload


def validate_memberships(doc: dict, record_path: Path, *, artifacts: dict | None = None) -> None:
    if FIELD not in doc:
        if artifacts:
            raise ValueError("membership artifacts supplied without references")
        return
    references = doc[FIELD]
    if not isinstance(references, list) or not references:
        raise ValueError("membership collections must be a nonempty list")
    doc = expand_activities(doc, record_path)
    identity = tuple(_identity(doc).values())
    seen, names = set(), set()
    for reference in references:
        payload = collection_bytes(reference, record_path, artifacts=artifacts)
        summary = inspect_payload(payload)
        if reference != make_reference(payload) or any(type(reference[key]) is not int for key in (
            *COUNT_FIELDS, "byte_size", "uncompressed_byte_size",
        )):
            raise ValueError("membership reference metadata or counts mismatch")
        if summary.identity != identity:
            raise ValueError("membership chemical identity mismatch")
        key = (reference["source"], reference["source_version"])
        if key in seen:
            raise ValueError("duplicate membership source/version collection")
        seen.add(key)
        names.add(reference["path"])
        observations = _observation_map(doc, *key)
        if observations.keys() != {row[0] for row in summary.groups}:
            raise ValueError("membership groups do not cover the source-owned observations")
        for group_id, digest, isolates, measurements, _unlinked in summary.groups:
            row = observations[group_id]
            if digest != observation_digest(row):
                raise ValueError("membership observation binding mismatch")
            if type(row.get("isolate_count")) is not int or row["isolate_count"] != isolates or (
                type(row.get("measurement_count")) is not int or row["measurement_count"] != measurements
            ):
                raise ValueError("membership observation counts mismatch")
    if artifacts and artifacts.keys() - names:
        raise ValueError("unreferenced supplied membership artifacts")


def read_memberships(doc: dict, record_path: Path) -> list[tuple[dict, dict]]:
    """Return validated registries without adding members to observation YAML."""
    validate_memberships(doc, record_path)
    return [(reference, _decode(collection_bytes(reference, record_path))[0])
            for reference in doc.get(FIELD, [])]


def write_membership_artifacts(artifacts: dict[str, bytes], directory: Path) -> None:
    for payload in artifacts.values():
        inspect_payload(payload)
    write_artifacts(artifacts, directory, pattern=ARTIFACT_NAME)


def orphaned_membership_artifacts(root: Path) -> list[Path]:
    referenced = set()
    for path in sorted(root.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a record mapping")
        validate_memberships(doc, path)
        referenced.update(path.parent / reference["path"] for reference in doc.get(FIELD, []))
    orphans = []
    for path in sorted(root.rglob("membership-*.json.gz")):
        match = ARTIFACT_NAME.fullmatch(path.name)
        if not match or path in referenced:
            continue
        if path.is_symlink() or not path.is_file():
            raise ValueError("refusing to prune a non-regular membership artifact")
        with path.open("rb") as handle:
            payload = handle.read(MAX_BYTES + 1)
        reference = make_reference(payload)
        if reference["sha256"] != match[1]:
            raise ValueError("refusing to prune a corrupt membership artifact")
        orphans.append(path)
    return orphans

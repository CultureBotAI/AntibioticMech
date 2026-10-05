"""Offline, source-owned CRyPTIC membership inputs and record attachments."""

from __future__ import annotations

import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

import yaml
from ncbi_ast_inventory import inventory_metadata, open_activity_text

from antibioticmech.activity_memberships import FIELD, build_collection, validate_subject

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "CRYPTIC"
VERSION = "3.4.0"
REFERENCE = "https://zenodo.org/records/15680920"
ISOLATES = "cryptic_isolates.tsv.gz"
MEMBERSHIPS = "cryptic_memberships.tsv.gz"
ISOLATE_COLUMNS = (
    "source_version", "source_isolate_id", "biosample_accession", "bioproject_accession", "run_accession",
)
MEMBERSHIP_COLUMNS = ("source_version", "activity_group_id", "source_isolate_id", "measurement_count")


def sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def rows(path, columns):
    with open_activity_text(path) as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != list(columns):
            raise ValueError(f"{path}: invalid CRyPTIC membership inventory header")
        for row in reader:
            if set(row) != set(columns) or any(value is None for value in row.values()):
                raise ValueError(f"{path}: malformed CRyPTIC membership inventory row")
            if row["source_version"] != VERSION:
                raise ValueError(f"{path}: unsupported CRyPTIC membership version")
            yield row


def read_groups(activity_rows, isolates_path, memberships_path):
    """Validate normalized inventories against every adopted observation group."""
    subjects = {}
    for row in rows(isolates_path, ISOLATE_COLUMNS):
        context = {key: row[key] for key in ISOLATE_COLUMNS[2:]}
        subject = {"source_isolate_id": row["source_isolate_id"],
                   "sequencing_context": context if any(context.values()) else None}
        source_id = validate_subject(subject)
        if source_id in subjects:
            raise ValueError("duplicate CRyPTIC isolate registry ID")
        subjects[source_id] = subject
    expected = {row["activity_group_id"]: row for row in activity_rows}
    if len(expected) != len(activity_rows) or not expected:
        raise ValueError("duplicate or empty CRyPTIC activity group inventory")
    groups = defaultdict(dict)
    used = set()
    for row in rows(memberships_path, MEMBERSHIP_COLUMNS):
        group_id, source_id = row["activity_group_id"], row["source_isolate_id"]
        if group_id not in expected or source_id not in subjects:
            raise ValueError("CRyPTIC membership has an unknown group or isolate ID")
        if source_id in groups[group_id]:
            raise ValueError("duplicate CRyPTIC group/isolate membership")
        if not re.fullmatch(r"[1-9][0-9]*", row["measurement_count"]):
            raise ValueError("invalid CRyPTIC membership measurement count")
        groups[group_id][source_id] = {
            **subjects[source_id], "measurement_count": int(row["measurement_count"]),
        }
        used.add(source_id)
    if groups.keys() != expected.keys() or used != subjects.keys():
        raise ValueError("CRyPTIC membership inventories omit groups or contain unused subjects")
    result = {}
    for group_id, members in groups.items():
        row = expected[group_id]
        if row["source_version"] != VERSION or len(members) != int(row["isolate_count"]) or (
            sum(member["measurement_count"] for member in members.values()) != int(row["row_count"])
        ):
            raise ValueError(f"CRyPTIC membership count/version mismatch: {group_id}")
        result[group_id] = [members[key] for key in sorted(members)]
    return result


def load_adopted(activity_rows, *, raw_dir=ROOT / "data" / "raw",
                 drug_map=ROOT / "curation" / "cryptic_drug_map.tsv"):
    manifest = yaml.safe_load((raw_dir / "MANIFEST.yaml").read_text(encoding="utf-8"))
    source = manifest["sources"]["cryptic"]
    provenance = source.get("membership")
    names = (ISOLATES, MEMBERSHIPS)
    if provenance is None and not any((raw_dir / name).exists() for name in names):
        return {}, None
    if not isinstance(provenance, dict) or source.get("version") != VERSION or (
        source.get("homepage") != REFERENCE or source.get("license") != "CC BY 4.0"
    ):
        raise ValueError("CRyPTIC membership adoption provenance is missing or inconsistent")
    activity_hash = sha256(raw_dir / "cryptic_activity.tsv")
    if provenance.get("activity_inventory_sha256") != activity_hash or (
        provenance.get("drug_map_sha256") != sha256(drug_map)
    ):
        raise ValueError("CRyPTIC membership activity inventory or drug map pin mismatch")
    snapshot = manifest["downloads"].get("WGS_SAMPLES.parquet", {})
    if snapshot.get("sha256") != provenance.get("source_snapshot_sha256") or (
        snapshot.get("url") != REFERENCE + "/files/WGS_SAMPLES.parquet?download=1"
    ) or snapshot.get("retrieved_on") != provenance.get("retrieved_on"):
        raise ValueError("CRyPTIC membership sequencing snapshot provenance mismatch")
    fingerprints = {}
    for name in names:
        expected = manifest["inventories"].get(name, {})
        fingerprints[name] = inventory_metadata(raw_dir / name)
        if any(expected.get(key) != value for key, value in fingerprints[name].items()):
            raise ValueError(f"CRyPTIC membership manifest mismatch: {name}")
    groups = read_groups(activity_rows, raw_dir / ISOLATES, raw_dir / MEMBERSHIPS)
    counts = {
        ISOLATES: len({member["source_isolate_id"] for members in groups.values() for member in members}),
        MEMBERSHIPS: sum(len(members) for members in groups.values()),
    }
    for name in names:
        if manifest["inventories"][name].get("rows") != counts[name] or (
            inventory_metadata(raw_dir / name) != fingerprints[name]
        ):
            raise ValueError(f"CRyPTIC membership inventory changed or row count mismatch: {name}")
    return groups, {
        "source": SOURCE, "source_version": VERSION, "source_reference": REFERENCE,
        "source_retrieved_on": provenance["retrieved_on"],
        "source_snapshot_sha256": provenance["source_snapshot_sha256"],
        "activity_inventory_sha256": activity_hash,
    }


def sourced_view(record):
    return [item for item in record.get(FIELD, []) if item.get("source") == SOURCE]


def attach(records, activity_rows, **kwargs):
    groups, metadata = load_adopted(activity_rows, **kwargs)
    if metadata is None:
        return {}
    by_compound = defaultdict(dict)
    for row in activity_rows:
        identifier = row["identifier"]
        record = records.get(identifier, {})
        if record.get("chemical_structure", {}).get("standard_inchi_key") != row["standard_inchi_key"]:
            raise ValueError(f"CRyPTIC membership chemical identity mismatch: {identifier}")
        by_compound[identifier][row["activity_group_id"]] = groups[row["activity_group_id"]]
    artifacts = {}
    for identifier, compound_groups in sorted(by_compound.items()):
        record = records[identifier]
        reference, payload = build_collection(record, metadata, compound_groups)
        record[FIELD] = [reference] + [r for r in record.get(FIELD, []) if r.get("source") != SOURCE]
        artifacts[reference["path"]] = payload
    return artifacts

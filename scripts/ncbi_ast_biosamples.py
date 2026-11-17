#!/usr/bin/env python3
"""Adjudicate AST target fan-out against single submitted BioSample results."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from ncbi_ast_inventory import activity_report_sha256
from ncbi_ast_isolates import require_iso_date

ENDPOINT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
DEFAULT_REVIEW = Path(__file__).resolve().parents[1] / "curation/ncbi_ast_biosample_review.json"
HEADERS = [
    "Antibiotic",
    "Resistance phenotype",
    "Measurement sign",
    "Measurement",
    "Measurement units",
    "Laboratory typing method",
    "Laboratory typing platform",
    "Vendor",
    "Laboratory typing method version or reagent",
    "Testing standard",
]
CONTEXT_FIELDS = {
    "bioproject_accession": "bioproject_accession",
    "target_accession": "pathogen_detection_target_accession",
    "assembly_accession": "assembly_accession",
    "sra_accessions": "sra_accessions",
    "create_date": "source_create_date",
}


def repeated_target_groups(rows: list[dict]) -> list[list[dict]]:
    by_result = defaultdict(list)
    shared = sorted(set(rows[0]) - {*CONTEXT_FIELDS, "activity_group_id"}) if rows else []
    for row in rows:
        if row["biosample_accession"]:
            by_result[tuple(row[field] for field in shared)].append(row)
    groups = []
    for members in by_result.values():
        targets = {row["target_accession"] for row in members}
        if len(targets) <= 1:
            continue
        if "" in targets or len(targets) != len(members) or any(r["ast_row_count"] != "1" for r in members):
            raise ValueError("repeated targets need individual-assay adjudication")
        groups.append(sorted(members, key=lambda r: r["activity_group_id"]))
    return sorted(groups, key=lambda members: members[0]["activity_group_id"])


def read_biosamples(payload: bytes, requested: list[str]) -> dict:
    root = ET.fromstring(payload)
    if root.tag != "BioSampleSet" or any(node.tag != "BioSample" for node in root):
        raise ValueError("not a successful BioSample XML response")
    samples = {}
    for node in root:
        accession = node.get("accession", "")
        if not re.fullmatch(r"SAM(N|D|EA)[0-9]+", accession) or accession in samples:
            raise ValueError("missing, invalid, or duplicate BioSample accession")
        primary_ids = node.findall("Ids/Id[@db='BioSample'][@is_primary='1']")
        statuses = node.findall("Status")
        if (
            node.get("access") != "public"
            or len(primary_ids) != 1
            or primary_ids[0].text != accession
            or len(statuses) != 1
            or statuses[0].get("status") != "live"
        ):
            raise ValueError(f"{accession}: BioSample is not a public live primary record")
        organisms = node.findall("Description/Organism")
        if len(organisms) != 1 or not re.fullmatch(r"[1-9][0-9]*", organisms[0].get("taxonomy_id", "")):
            raise ValueError(f"{accession}: missing or ambiguous BioSample taxonomy")
        name = organisms[0].get("taxonomy_name", "")
        if not name.strip():
            raise ValueError(f"{accession}: missing BioSample organism name")
        updated = node.get("last_update", "")
        datetime.fromisoformat(updated)
        tables = node.findall("Description/Comment/Table")
        if len(tables) != 1 or tables[0].get("class") != "Antibiogram.1.0":
            raise ValueError(f"{accession}: expected one supported antibiogram table")
        table = tables[0]
        if len(table.findall("Header")) != 1 or len(table.findall("Body")) != 1:
            raise ValueError(f"{accession}: malformed antibiogram table")
        if [cell.text for cell in table.findall("Header/Cell")] != HEADERS:
            raise ValueError(f"{accession}: unexpected antibiogram columns")
        results = []
        for row in table.find("Body"):
            if row.tag != "Row" or len(row) != len(HEADERS) or any(c.tag != "Cell" or len(c) for c in row):
                raise ValueError(f"{accession}: malformed antibiogram row")
            results.append(dict(zip(HEADERS, [(cell.text or "").strip() for cell in row], strict=True)))
        if not results:
            raise ValueError(f"{accession}: empty antibiogram")
        samples[accession] = {
            "taxon_id": "NCBITaxon:" + organisms[0].get("taxonomy_id"),
            "taxon_label": name,
            "last_update": updated,
            "rows": results,
        }
    if set(samples) != set(requested) or len(requested) != len(set(requested)):
        raise ValueError("BioSample response does not cover exact requested accessions")
    return samples


def matches_result(row: dict, result: dict) -> bool:
    if set(result) != set(HEADERS) or any(not isinstance(v, str) for v in result.values()):
        raise ValueError("invalid reviewed antibiogram row")
    units = result["Measurement units"]
    if units not in {"mg/L", "mm"}:
        return False
    compatible_methods = {"MIC", "agar dilution"} if units == "mg/L" else {"disk diffusion"}
    if result["Laboratory typing method"] not in compatible_methods | {"", "missing"}:
        return False
    value_field = "mic_value" if units == "mg/L" else "disk_diffusion_value"
    other_field = "disk_diffusion_value" if units == "mg/L" else "mic_value"
    if not row[value_field] or row[other_field]:
        return False
    try:
        value = Decimal(result["Measurement"])
    except InvalidOperation:
        return False
    if not value.is_finite() or value <= 0 or value != Decimal(row[value_field]):
        return False
    qualifier = result["Measurement sign"]
    if qualifier in {"==", "="}:
        qualifier = ""
    if qualifier not in {"", "<", "<=", ">", ">="}:
        return False
    expected = {
        "source_name": result["Antibiotic"],
        "phenotype": result["Resistance phenotype"],
        "platform": result["Laboratory typing platform"],
        "vendor": result["Vendor"],
        "reagent": result["Laboratory typing method version or reagent"],
        "standard": result["Testing standard"],
        value_field.replace("value", "qualifier"): qualifier,
    }
    expected = {k: "" if v == "missing" else v for k, v in expected.items()}
    if any(row[key] != value for key, value in expected.items()):
        return False
    # The native AST export omits the BioSample method field. Never invent its value.
    return not row["method"] or row["method"] == result["Laboratory typing method"]


def build_review(groups: list[list[dict]], samples: dict, metadata: dict) -> dict:
    decisions = []
    for members in groups:
        row = members[0]
        sample = samples[row["biosample_accession"]]
        require_prior_biosample(sample["last_update"], row)
        if any(row[field] != sample[field] for field in ("taxon_id", "taxon_label")):
            raise ValueError("BioSample taxonomy conflicts with reviewed AST identity")
        matches = [(i, result) for i, result in enumerate(sample["rows"], 1) if matches_result(row, result)]
        if len(matches) != 1:
            raise ValueError(
                f"{row['biosample_accession']}/{row['source_name']}: expected one submitted result",
            )
        index, result = matches[0]
        decisions.append(
            {
                "activity_group_ids": [r["activity_group_id"] for r in members],
                "biosample_accession": row["biosample_accession"],
                "biosample_last_update": sample["last_update"],
                "taxon_id": sample["taxon_id"],
                "taxon_label": sample["taxon_label"],
                "antibiogram_row_number": index,
                "antibiogram_row": result,
            }
        )
    return {
        "source_version": groups[0][0]["source_version"],
        "activity_report_sha256": metadata["activity_report_sha256"],
        "biosample_sha256": metadata["sha256"],
        "reviewed_on": metadata["source_retrieved_on"],
        "groups": decisions,
    }


def require_prior_biosample(updated: str, row: dict) -> None:
    if datetime.fromisoformat(updated).date() >= date.fromisoformat(row["source_retrieved_on"]):
        raise ValueError("BioSample update does not demonstrably predate the AST snapshot")


def fetch_review(activity_report: Path, output_dir: Path) -> dict:
    from seed_from_sources import load_ncbi_ast_activity_inventory

    if output_dir.exists():
        raise ValueError(f"snapshot directory already exists: {output_dir}")
    checksum = activity_report_sha256(activity_report)
    rows = load_ncbi_ast_activity_inventory(activity_report)
    groups = repeated_target_groups(rows)
    if not groups:
        raise ValueError("no repeated-target groups to adjudicate")
    requested = sorted({g[0]["biosample_accession"] for g in groups})
    params = {"db": "biosample", "id": ",".join(requested), "retmode": "xml"}
    with urlopen(Request(ENDPOINT, data=urlencode(params).encode("ascii")), timeout=300) as response:
        payload = response.read()
    samples = read_biosamples(payload, requested)
    if activity_report_sha256(activity_report) != checksum:
        raise ValueError("activity report changed during BioSample retrieval")
    metadata = {
        "source": "NCBI_BIOSAMPLE_EFETCH",
        "endpoint": ENDPOINT,
        "source_retrieved_on": datetime.now(timezone.utc).date().isoformat(),
        "requested_accessions": requested,
        "activity_report_sha256": checksum,
        "file": "biosamples.xml",
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
    }
    review = build_review(groups, samples, metadata)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ncbi-biosamples-", dir=output_dir.parent) as temporary:
        staged = Path(temporary) / "snapshot"
        staged.mkdir()
        (staged / "biosamples.xml").write_bytes(payload)
        (staged / "snapshot.json").write_text(json.dumps(metadata, indent=2) + "\n")
        (staged / "review.json").write_text(json.dumps(review, indent=2, ensure_ascii=True) + "\n")
        if output_dir.exists():
            raise ValueError(f"snapshot directory already exists: {output_dir}")
        staged.rename(output_dir)
    return review


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate BioSample-review JSON key: {key}")
        result[key] = value
    return result


def read_review(path: Path, activity_report: Path, groups: list[list[dict]]) -> tuple[dict, str]:
    payload = path.read_bytes()
    review = json.loads(payload, object_pairs_hook=_unique_object)
    expected = {"source_version", "activity_report_sha256", "biosample_sha256", "reviewed_on", "groups"}
    if not isinstance(review, dict) or set(review) != expected:
        raise ValueError("invalid BioSample review fields")
    require_iso_date(review["reviewed_on"], "BioSample review")
    if not isinstance(review["biosample_sha256"], str) or not re.fullmatch(
        r"[a-f0-9]{64}", review["biosample_sha256"]
    ):
        raise ValueError("invalid BioSample snapshot checksum")
    if review["activity_report_sha256"] != activity_report_sha256(activity_report):
        raise ValueError("BioSample review does not match the exact activity report")
    if not isinstance(review["groups"], list):
        raise ValueError("BioSample review groups must be a list")
    current = {tuple(row["activity_group_id"] for row in group): group for group in groups}
    seen, source_rows = set(), set()
    for decision in review["groups"]:
        fields = {
            "activity_group_ids",
            "biosample_accession",
            "biosample_last_update",
            "taxon_id",
            "taxon_label",
            "antibiogram_row_number",
            "antibiogram_row",
        }
        if not isinstance(decision, dict) or set(decision) != fields:
            raise ValueError("invalid BioSample review decision")
        ids = decision["activity_group_ids"]
        if not isinstance(ids, list) or any(not isinstance(value, str) for value in ids):
            raise ValueError("invalid BioSample review group IDs")
        key = tuple(ids)
        if key not in current or key in seen:
            raise ValueError("BioSample review groups do not match repeated target groups")
        seen.add(key)
        number = decision["antibiogram_row_number"]
        if type(number) is not int or number < 1:
            raise ValueError("invalid BioSample antibiogram row number")
        datetime.fromisoformat(decision["biosample_last_update"])
        source_key = (decision["biosample_accession"], number)
        if source_key in source_rows:
            raise ValueError("one BioSample result cannot justify multiple collapsed groups")
        source_rows.add(source_key)
        for row in current[key]:
            require_prior_biosample(decision["biosample_last_update"], row)
            identity_fields = ("biosample_accession", "taxon_id", "taxon_label")
            if (
                row["source_version"] != review["source_version"]
                or any(row[field] != decision[field] for field in identity_fields)
                or not matches_result(row, decision["antibiogram_row"])
            ):
                raise ValueError("reviewed BioSample result disagrees with AST row")
    if seen != set(current):
        raise ValueError("BioSample review does not cover every repeated target group")
    return review, "biosample-review-sha256:" + hashlib.sha256(payload).hexdigest()


def activity_observations(rows: list[dict], inventory: Path, convert, review_path: Path = DEFAULT_REVIEW):
    """Yield source observations, collapsing only source-verified export fan-out."""
    groups = repeated_target_groups(rows)
    if not groups:
        for row in rows:
            yield row["identifier"], convert(row)
        return
    review, version = read_review(review_path, inventory, groups)
    decisions = {tuple(d["activity_group_ids"]): d for d in review["groups"]}
    by_id = {row["activity_group_id"]: group for group in groups for row in group}
    handled = set()
    for row in rows:
        group = by_id.get(row["activity_group_id"])
        if group is None:
            yield row["identifier"], convert(row)
            continue
        ids = tuple(member["activity_group_id"] for member in group)
        if ids in handled:
            continue
        handled.add(ids)
        decision = decisions[ids]
        originals = [convert(member) for member in group]
        observation = dict(originals[0])
        for field in CONTEXT_FIELDS.values():
            observation.pop(field, None)
        observation["pathogen_detection_contexts"] = [
            {
                key: original[key]
                for key in (*CONTEXT_FIELDS.values(), "source_observation_id")
                if key in original
            }
            for original in originals
        ]
        observation["measurement_count"] = 1
        observation["source_export_row_count"] = len(originals)
        provenance = [
            review["biosample_sha256"],
            decision["biosample_accession"],
            decision["antibiogram_row_number"],
        ]
        observation["source_observation_id"] = (
            "ncbi_ast_biosample:"
            + hashlib.sha256(
                json.dumps(provenance, separators=(",", ":")).encode("utf-8"),
            ).hexdigest()
        )
        evidence = {json.dumps(e, sort_keys=True): e for original in originals for e in original["evidence"]}
        observation["evidence"] = list(evidence.values()) + [
            {
                "reference": "https://www.ncbi.nlm.nih.gov/biosample/" + decision["biosample_accession"],
                "notes": (
                    f"{version}; reviewed_on={review['reviewed_on']}; "
                    f"biosample_sha256={review['biosample_sha256']}; "
                    f"biosample_last_update={decision['biosample_last_update']}; "
                    f"Antibiogram.1.0 row={decision['antibiogram_row_number']}; "
                    f"original_activity_group_ids={'|'.join(ids)}. One submitted result exported under "
                    "multiple genome targets, not independent replicate measurements. "
                    "All original target, assembly, project and source-date associations are retained."
                ),
            }
        ]
        yield row["identifier"], observation


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activity-report", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    review = fetch_review(args.activity_report, args.output_directory)
    print(f"Confirmed {len(review['groups'])} single BioSample results with repeated AST targets")


if __name__ == "__main__":
    main()

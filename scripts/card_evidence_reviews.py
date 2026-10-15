"""Qualify CARD assertions without rewriting their source or claiming an experiment."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from datetime import date
from pathlib import Path

DEFAULT_REVIEW = Path(__file__).resolve().parents[1] / "curation/card_evidence_reviews.json"


def row_digest(row: dict) -> str:
    payload = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def _text(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and value == value.strip()
        and not any(ord(c) < 32 for c in value)
    )


def load_reviews(
    inventory: Path, rows: list[dict], records: dict, path: Path | None = DEFAULT_REVIEW
) -> dict:
    if path is None:
        return {}
    payload = path.read_bytes()
    document = json.loads(payload)
    if (
        not isinstance(document, dict)
        or set(document) != {"schema_version", "source_inventory_sha256", "reviews"}
        or type(document["schema_version"]) is not int
        or document["schema_version"] != 1
        or not isinstance(document["reviews"], list)
    ):
        raise ValueError("invalid CARD evidence review document")
    source = inventory.read_bytes()
    if hashlib.sha256(source).hexdigest() != document["source_inventory_sha256"]:
        raise ValueError("CARD evidence review inventory drift")
    if rows != list(csv.DictReader(io.StringIO(source.decode()), delimiter="\t")):
        raise ValueError("CARD rows changed during review loading")
    by_hash: dict[str, list[dict]] = {}
    for row in rows:
        by_hash.setdefault(row_digest(row), []).append(row)
    result, review_ids = {}, set()
    for review in document["reviews"]:
        if not isinstance(review, dict) or set(review) != {
            "review_id",
            "curator",
            "reviewed_on",
            "note",
            "evidence",
            "source_rows",
        }:
            raise ValueError("invalid CARD evidence review fields")
        if any(not _text(review[k]) for k in ("review_id", "curator", "reviewed_on", "note")):
            raise ValueError("missing CARD review provenance")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", review["reviewed_on"]):
            raise ValueError("invalid CARD review date")
        date.fromisoformat(review["reviewed_on"])
        if review["review_id"] in review_ids:
            raise ValueError("duplicate CARD review id")
        review_ids.add(review["review_id"])
        if not isinstance(review["evidence"], list) or not review["evidence"]:
            raise ValueError("CARD review needs inspected evidence")
        references = set()
        for evidence in review["evidence"]:
            if (
                not isinstance(evidence, dict)
                or set(evidence) != {"reference", "source_url", "locations", "inspected"}
                or any(not _text(evidence[k]) for k in ("reference", "source_url", "inspected"))
                or not re.fullmatch(r"(?:PMID:[1-9][0-9]*|DOI:10\.[0-9]{4,9}/\S+)", evidence["reference"])
                or not evidence["source_url"].startswith("https://")
                or not isinstance(evidence["locations"], list)
                or not evidence["locations"]
                or any(not _text(v) for v in evidence["locations"])
                or len(set(evidence["locations"])) != len(evidence["locations"])
                or evidence["reference"] in references
            ):
                raise ValueError("invalid CARD review evidence")
            references.add(evidence["reference"])
        if not isinstance(review["source_rows"], list) or not review["source_rows"]:
            raise ValueError("CARD review has no source rows")
        for target in review["source_rows"]:
            if (
                not isinstance(target, dict)
                or set(target) != {"row_sha256", "identifier", "standard_inchi_key"}
                or any(not _text(v) for v in target.values())
            ):
                raise ValueError("invalid CARD reviewed target")
            key = target["row_sha256"]
            matches = by_hash.get(key, [])
            if len(matches) != 1 or key in result:
                raise ValueError("CARD reviewed row missing, ambiguous or duplicated")
            row = matches[0]
            record = records.get(target["identifier"], {})
            owners = [
                rid
                for rid, r in records.items()
                if any(
                    c.get("source") == "ARO" and c.get("source_id") == row["antibiotic_id"]
                    for c in r.get("source_concepts", [])
                )
            ]
            if (
                row["relation"] != "confers_resistance_to_antibiotic"
                or record.get("identifier") != target["identifier"]
                or record.get("chemical_structure", {}).get("standard_inchi_key")
                != target["standard_inchi_key"]
                or owners != [target["identifier"]]
            ):
                raise ValueError("CARD reviewed compound binding differs")
            result[key] = {**review, "review_sha256": hashlib.sha256(payload).hexdigest()}
    return result


def apply_review(item: dict, row: dict, reviews: dict) -> bool:
    review = reviews.get(row_digest(row))
    if review is None:
        return False
    if (
        set(item) != {"mechanism_type", "aro_id", "label", "evidence"}
        or item["aro_id"] != row["determinant_id"]
        or item["label"] != row["determinant_name"]
        or item["mechanism_type"] != (row["mechanism"] or "UNKNOWN")
        or item["evidence"]
        != [
            {
                "reference": row["determinant_id"],
                "notes": (
                    "CARD/ARO asserts confers_resistance_to_antibiotic "
                    f"{row['antibiotic_id']} ({row['antibiotic_name']}); "
                    "database assertion, not a primary citation."
                ),
            }
        ]
    ):
        raise ValueError("CARD review can only qualify a fresh, unchanged source assertion")
    citations = " ".join(
        f"{e['reference']} ({'; '.join(e['locations'])}; {e['inspected']})." for e in review["evidence"]
    )
    # Keeping citations in the qualification, not claim evidence, preserves CARD ownership.
    item["note"] = (
        f"Evidence-scope review {review['review_id']}: {review['note']} "
        f"Qualification references, not an upgrade of the CARD assertion: {citations} "
        f"Reviewed {review['reviewed_on']} by {review['curator']}; "
        f"curation/card_evidence_reviews.json SHA-256 {review['review_sha256']}."
    )
    return True

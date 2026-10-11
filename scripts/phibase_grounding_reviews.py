"""Apply pinned subject-context reviews without rewriting source rows."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from datetime import date
from pathlib import Path

DEFAULT_REVIEW = Path(__file__).resolve().parents[1] / "curation/phibase_grounding_reviews.json"
WITHHOLDABLE = {"taxon_id", "strain_taxon_id", "protein_accession", "gene_id"}
MISASSIGNABLE = {"taxon_id", "protein_accession", "gene_id"}
PREFIXES = {"taxon_id": "NCBITaxon:", "strain_taxon_id": "NCBITaxon:",
            "protein_accession": "UniProtKB:", "gene_id": ""}


def row_digest(row: dict[str, str]) -> str:
    payload = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def load_reviews(inventory: Path, rows: list[dict], path: Path | None = DEFAULT_REVIEW) -> dict:
    if path is None:
        return {}
    payload = path.read_bytes()
    review_hash = hashlib.sha256(payload).hexdigest()
    document = json.loads(payload)
    if set(document) != {"schema_version", "source_inventory_sha256", "reviews"}:
        raise ValueError("unexpected PHI-base grounding review fields")
    if type(document["schema_version"]) is not int or document["schema_version"] != 1:
        raise ValueError("unsupported PHI-base grounding review version")
    source = inventory.read_bytes()
    if hashlib.sha256(source).hexdigest() != document["source_inventory_sha256"]:
        raise ValueError("PHI-base grounding review inventory drift")
    if rows != list(csv.DictReader(io.StringIO(source.decode()), delimiter="\t")):
        raise ValueError("PHI-base rows changed during review loading")
    by_hash = {}
    for row in rows:
        by_hash.setdefault(row_digest(row), []).append(row)
    result, review_ids = {}, set()
    if not isinstance(document["reviews"], list):
        raise ValueError("PHI-base reviews must be a list")
    fields = {"review_id", "curator", "reviewed_on", "pmid", "reference", "source_url",
              "locations", "note", "withhold", "source_rows"}
    for review in document["reviews"]:
        if (not isinstance(review, dict) or not fields <= set(review)
                or set(review) - fields - {
                    "misassigned", "subject_strain", "subject_taxon", "withhold_strain"}):
            raise ValueError("unexpected PHI-base review decision fields")
        for key in ("review_id", "curator", "reviewed_on", "pmid", "reference", "source_url", "note"):
            if not isinstance(review[key], str) or not review[key].strip():
                raise ValueError("missing PHI-base review provenance")
        date.fromisoformat(review["reviewed_on"])
        if (review["review_id"] in review_ids or not review["pmid"].isdigit()
                or not review["reference"].startswith(("PMID:", "DOI:"))
                or not review["source_url"].startswith("https://")):
            raise ValueError("invalid PHI-base review provenance")
        review_ids.add(review["review_id"])
        for key in ("withhold", "locations"):
            values = review[key]
            if (not isinstance(values, list) or not values
                    or any(not isinstance(v, str) or not v.strip() for v in values)
                    or len(set(values)) != len(values)):
                raise ValueError("invalid PHI-base review decision list")
        if not set(review["withhold"]) <= WITHHOLDABLE:
            raise ValueError("review cannot rewrite or remove biological claims")
        if "subject_strain" in review:
            subject = review["subject_strain"]
            if (not isinstance(subject, str) or not subject.strip()
                    or subject != subject.strip() or any(ord(c) < 32 for c in subject)):
                raise ValueError("invalid PHI-base subject strain decision")
        if "withhold_strain" in review and (
            review["withhold_strain"] is not True or "subject_strain" in review
        ):
            raise ValueError("invalid PHI-base background-only strain decision")
        if "subject_taxon" in review:
            subject = review["subject_taxon"]
            if (not isinstance(subject, dict) or set(subject) != {"taxon_id", "taxon_label"}
                    or any(not isinstance(v, str) or not v.strip() or v != v.strip()
                           or any(ord(c) < 32 for c in v) for v in subject.values())
                    or not subject["taxon_id"].isascii() or not subject["taxon_id"].isdigit()
                    or subject["taxon_id"].startswith("0")):
                raise ValueError("invalid PHI-base subject taxon decision")
        misassigned = review.get("misassigned", [])
        if (not isinstance(misassigned, list)
                or any(not isinstance(v, str) or not v.strip() for v in misassigned)
                or len(set(misassigned)) != len(misassigned)
                or not set(misassigned) <= MISASSIGNABLE & set(review["withhold"])
                or ("misassigned" in review and not misassigned)
                or ("gene_id" in review["withhold"] and "gene_id" not in misassigned)):
            raise ValueError("invalid PHI-base misassigned identifier decision")
        if not isinstance(review["source_rows"], list) or not review["source_rows"]:
            raise ValueError("review has no source rows")
        for target in review["source_rows"]:
            if not isinstance(target, dict) or set(target) != {"identifier", "row_sha256"}:
                raise ValueError("invalid reviewed source row")
            key = target["row_sha256"]
            matches = by_hash.get(key, [])
            if len(matches) != 1 or key in result:
                raise ValueError("reviewed source row missing, ambiguous or duplicated")
            row = matches[0]
            if (row["identifier"] != target["identifier"] or row["pmid"] != review["pmid"]
                    or any(not row[field] for field in review["withhold"])):
                raise ValueError("reviewed source identity differs")
            if "subject_strain" in review and (
                not row["strain_label"].strip() or review["subject_strain"] == row["strain_label"]
                or (row["strain_taxon_id"] and "strain_taxon_id" not in review["withhold"])
            ):
                raise ValueError("subject strain must resolve a different source background label")
            if review.get("withhold_strain") and (
                not row["strain_label"].strip()
                or (row["strain_taxon_id"] and "strain_taxon_id" not in review["withhold"])
            ):
                raise ValueError("background-only strain must withhold its source strain identifier")
            if "subject_taxon" in review:
                subject = review["subject_taxon"]
                required = {k for k in WITHHOLDABLE if row[k]}
                if (not row["taxon_id"] or not row["taxon_label"]
                        or subject["taxon_id"] == row["taxon_id"]
                        or subject["taxon_label"] == row["taxon_label"]
                        or not required <= set(review["withhold"])
                        or "taxon_id" not in misassigned):
                    raise ValueError("subject taxon must reject conflicting source identity")
            result[key] = {**review, "review_sha256": review_hash}
    return result


def apply_review(item: dict, row: dict, reviews: dict) -> bool:
    review = reviews.get(row_digest(row))
    if review is None:
        return False
    for field in review["withhold"]:
        expected = PREFIXES[field] + row[field]
        if item.get(field) != expected:
            raise ValueError("seeded identifier differs from reviewed source")
    strain_review = "subject_strain" in review or review.get("withhold_strain") is True
    if strain_review and item.get("strain") != row["strain_label"]:
        raise ValueError("seeded strain differs from reviewed source")
    if strain_review and not row["strain_taxon_id"] and item.get("strain_taxon_id") is not None:
        raise ValueError("seeded strain identifier differs from reviewed source")
    if "subject_taxon" in review and (item.get("taxon_label") != row["taxon_label"] or any(
        not row[field] and item.get(field) is not None for field in WITHHOLDABLE
    )):
        raise ValueError("seeded taxon context differs from reviewed source")
    withheld, misassigned = [], []
    for field in review["withhold"]:
        identifiers = misassigned if field in review.get("misassigned", []) else withheld
        identifiers.append(f"{field}={item.pop(field)}")
    item["note"] += f" Grounding review {review['review_id']}: {review['note']}"
    if "subject_strain" in review:
        item["strain"] = review["subject_strain"]
        item["note"] += f" Original source background label: {row['strain_label']}."
    if review.get("withhold_strain"):
        item.pop("strain")
        item["note"] += f" Original source background label: {row['strain_label']}."
    if "subject_taxon" in review:
        subject = review["subject_taxon"]
        item["taxon_id"] = "NCBITaxon:" + subject["taxon_id"]
        item["taxon_label"] = subject["taxon_label"]
        item["note"] += f" Original source organism label: {row['taxon_label']}."
    if withheld:
        item["note"] += f" Reference-only source identifiers: {'; '.join(withheld)}."
    if misassigned:
        item["note"] += f" Rejected misassigned source identifiers: {'; '.join(misassigned)}."
    item["evidence"].append({
        "reference": review["reference"],
        "notes": (
            f"Identifier-scope review: {', '.join(review['locations'])}. "
            f"Reviewed {review['reviewed_on']} by {review['curator']}; "
            f"curation/phibase_grounding_reviews.json SHA-256 {review['review_sha256']}."
        ),
    })
    return True

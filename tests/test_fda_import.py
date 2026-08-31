"""Acceptance tests for the strict Drugs@FDA + GSRS clinical-status import."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seed_from_sources import merge_with_existing  # noqa: E402


def test_committed_fda_inventory_is_product_level_and_conservative(repo_root):
    path = repo_root / "data" / "raw" / "fda_clinical_status.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    assert len(rows) == 3703
    assert len({row["standard_inchi_key"] for row in rows}) == 211
    assert len({(row["application_number"], row["product_number"]) for row in rows}) == len(rows)
    assert all(row["submission_status"] == "AP" for row in rows)
    assert all(row["marketing_status"] != "None (Tentative Approval)" for row in rows)
    assert all(";" not in row["ingredient_name"] for row in rows)
    assert all(len(row["standard_inchi_key"]) == 27 for row in rows)
    assert all(row["drugsfda_version"] == "2026-08-28" for row in rows)
    assert all(row["drugsfda_retrieved_on"] == "2026-08-31" for row in rows)
    assert all(row["unii_version"] == "2026-08-31" for row in rows)
    assert all(row["gsrs_retrieved_on"] == "2026-08-31" for row in rows)


def test_fda_assertions_are_exactly_reproduced_and_fully_provenanced(records):
    assertions = [
        (path, record, assertion)
        for path, record in records
        for assertion in record.get("clinical_status_assertions") or []
        if assertion.get("source") == "DRUGS_AT_FDA"
    ]
    assert len(assertions) == 3703
    assert len({record["identifier"] for _, record, _ in assertions}) == 211
    required = {
        "application_number",
        "product_number",
        "ingredient_name",
        "substance_id",
        "approval_date",
        "marketing_status",
        "source_version",
        "source_retrieved_on",
        "identity_source_version",
        "identity_retrieved_on",
        "identity_record_version",
        "reference",
    }
    problems = []
    for path, record, assertion in assertions:
        missing = sorted(field for field in required if not assertion.get(field))
        if missing or assertion.get("status") != "APPROVED" or record.get("clinical_status") != "APPROVED":
            problems.append((path.name, missing, assertion.get("status"), record.get("clinical_status")))
    assert problems == [], problems[:20]


def test_discontinued_is_not_misrepresented_as_withdrawn(records):
    hexachlorophene = next(record for _, record in records if record["identifier"] == "CHEBI:5693")
    claims = [
        item
        for item in hexachlorophene.get("clinical_status_assertions") or []
        if item.get("source") == "DRUGS_AT_FDA"
    ]
    assert claims
    assert any(item["marketing_status"] == "Discontinued" for item in claims)
    assert all(item["status"] == "APPROVED" for item in claims)
    assert all(
        item["currently_marketed"] is False
        for item in claims
        if item["marketing_status"] == "Discontinued"
    )
    assert hexachlorophene["clinical_status"] != "WITHDRAWN"


def test_marketing_boolean_agrees_with_the_preserved_status(records):
    observed = Counter()
    for _, record in records:
        for item in record.get("clinical_status_assertions") or []:
            if item.get("source") != "DRUGS_AT_FDA":
                continue
            observed[(item["marketing_status"], item["currently_marketed"])] += 1
    assert all(
        flag == (status in {"Prescription", "Over-the-counter"})
        for status, flag in observed
    ), observed


def test_reseed_replaces_only_the_fda_owned_assertion_slice():
    old_fda = {"status": "APPROVED", "source": "DRUGS_AT_FDA", "application_number": "000001"}
    new_fda = {"status": "APPROVED", "source": "DRUGS_AT_FDA", "application_number": "000002"}
    curated = {"status": "VETERINARY", "source": "CURATOR", "jurisdiction": "US-FDA"}
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }
    fresh = dict(base) | {
        "clinical_status": "APPROVED",
        "clinical_status_assertions": [new_fda],
    }
    existing = dict(base) | {
        "clinical_status": "VETERINARY",
        "clinical_status_assertions": [old_fda, curated],
    }
    merged = merge_with_existing(fresh, existing)
    assert merged["clinical_status_assertions"] == [new_fda, curated]
    assert merged["clinical_status"] == "VETERINARY"

"""Unit tests for the source queue's non-schema adoption tripwires."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_source_queue import (  # noqa: E402
    OPTIONAL_ADOPTION_INVENTORIES,
    STATUS,
    optional_inventory_problems,
    pipeline_use_problems,
    present_optional_inventories,
)


@pytest.mark.parametrize(
    ("source_id", "relative_path"),
    [
        ("bacdive", Path("data/raw/bacdive_activity.tsv")),
        ("ncbi-ast", Path("data/raw/ncbi_ast_activity.tsv")),
        ("ncbi-ast", Path("data/raw/ncbi_ast_activity.tsv.gz")),
    ],
)
def test_present_optional_inventories_notices_preadoption_exact_reports(
    tmp_path,
    source_id,
    relative_path,
):
    assert present_optional_inventories(tmp_path) == {}

    path = tmp_path / relative_path
    path.parent.mkdir(parents=True)
    path.write_text("id\n", encoding="utf-8")

    assert present_optional_inventories(tmp_path) == {source_id: (relative_path,)}


@pytest.mark.parametrize(
    ("source_id", "relative_path"),
    [
        ("bacdive", Path("data/raw/bacdive_activity.tsv")),
        ("ncbi-ast", Path("data/raw/ncbi_ast_activity.tsv")),
        ("ncbi-ast", Path("data/raw/ncbi_ast_activity.tsv.gz")),
    ],
)
@pytest.mark.parametrize("status", sorted(STATUS - {"ADOPTED"}))
def test_optional_inventory_problems_rejects_preadoption_exact_reports(
    source_id,
    relative_path,
    status,
):
    present = {source_id: (relative_path,)}
    alternatives = " or ".join(map(str, OPTIONAL_ADOPTION_INVENTORIES[source_id]))

    assert optional_inventory_problems(
        {source_id: {"status": status}},
        {},
    ) == []
    assert optional_inventory_problems(
        {source_id: {"status": "ADOPTED"}},
        {},
    ) == [
        f"{source_id}: {alternatives} is required when source "
        "status is ADOPTED",
    ]
    assert optional_inventory_problems(
        {source_id: {"status": status}},
        present,
    ) == [
        f"{source_id}: {relative_path} exists but source status is "
        f"{status}, not ADOPTED",
    ]
    assert optional_inventory_problems({}, present) == [
        f"{source_id}: {relative_path} exists but has no queue row",
    ]
    assert optional_inventory_problems(
        {source_id: {"status": "ADOPTED"}},
        present,
    ) == []


def test_pipeline_use_problems_rejects_configured_non_seed_sources():
    queue_by_source = {
        "configured-curate": {"use": "CURATE_ONLY"},
        "configured-reference": {"use": "REFERENCE"},
        "configured-seed": {"use": "SEED"},
    }

    assert pipeline_use_problems(
        queue_by_source,
        {
            "configured-curate",
            "configured-reference",
            "configured-seed",
            "missing",
        },
    ) == [
        "configured-curate: read by conf/sources.yaml but use is "
        "CURATE_ONLY, not SEED",
        "configured-reference: read by conf/sources.yaml but use is "
        "REFERENCE, not SEED",
    ]


@pytest.mark.parametrize("status", sorted(STATUS))
def test_source_queue_rejects_dual_ncbi_ast_inventories(tmp_path, status):
    paths = OPTIONAL_ADOPTION_INVENTORIES["ncbi-ast"]
    for relative in paths:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"inventory")
    problems = optional_inventory_problems(
        {"ncbi-ast": {"status": status}}, present_optional_inventories(tmp_path)
    )
    assert any("ambiguous inventories" in problem for problem in problems)


@pytest.mark.parametrize("status", sorted(STATUS - {"ADOPTED"}))
def test_source_queue_does_not_ignore_dangling_gzip_link(tmp_path, status):
    path = tmp_path / "data/raw/ncbi_ast_activity.tsv.gz"
    path.parent.mkdir(parents=True)
    path.symlink_to("missing")
    present = present_optional_inventories(tmp_path)
    assert present == {"ncbi-ast": (path.relative_to(tmp_path),)}
    assert optional_inventory_problems({"ncbi-ast": {"status": status}}, present)


def test_ncbi_ast_current_deferral_precedes_historical_review():
    root = Path(__file__).resolve().parents[1]
    with (root / "curation/source_queue.tsv").open(newline="", encoding="utf-8") as handle:
        row = next(r for r in csv.DictReader(handle, delimiter="\t") if r["source_id"] == "ncbi-ast")
    assert (row["status"], row["use"], row["redistribution"]) == ("BLOCKED", "REFERENCE", "UNVERIFIED")
    current, separator, historical = row["rationale"].partition("Historical review: ")
    assert current.startswith("Current maintainer direction: #1040 and NCBI source-terms work are deferred.")
    assert "Do not contact NCBI, make new requests to NCBI endpoints" in current
    assert "without new explicit authorization" in current
    assert separator
    assert historical.startswith("The maintainer resumed source-terms review for #1040 on 2026-10-04.")
    assert row["verified_on"] == "2026-10-04"
    backlog = " ".join((root / "NEXT_TASKS.md").read_text().split())
    assert "NCBI AST / #1040 is deferred." in backlog
    assert "Do not contact NCBI, make new requests to NCBI endpoints" in backlog
    assert "or resume reuse-terms work without new explicit maintainer authorization" in backlog

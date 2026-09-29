"""Unit tests for the source queue's non-schema adoption tripwires."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_source_queue import (  # noqa: E402
    optional_inventory_problems,
    present_optional_inventories,
)


def test_present_optional_inventories_notices_ncbi_ast_exact_reports(tmp_path):
    assert present_optional_inventories(tmp_path) == {}

    path = tmp_path / "data" / "raw" / "ncbi_ast_activity.tsv"
    path.parent.mkdir(parents=True)
    path.write_text("activity_group_id\n", encoding="utf-8")

    assert present_optional_inventories(tmp_path) == {
        "ncbi-ast": Path("data/raw/ncbi_ast_activity.tsv"),
    }


def test_optional_inventory_problems_rejects_preadoption_exact_reports():
    present = {"ncbi-ast": Path("data/raw/ncbi_ast_activity.tsv")}

    assert optional_inventory_problems(
        {"ncbi-ast": {"status": "EVALUATING"}},
        {},
    ) == []
    assert optional_inventory_problems(
        {"ncbi-ast": {"status": "ADOPTED"}},
        {},
    ) == [
        "ncbi-ast: data/raw/ncbi_ast_activity.tsv is required when source "
        "status is ADOPTED",
    ]
    assert optional_inventory_problems(
        {"ncbi-ast": {"status": "EVALUATING"}},
        present,
    ) == [
        "ncbi-ast: data/raw/ncbi_ast_activity.tsv exists but source status is "
        "EVALUATING, not ADOPTED",
    ]
    assert optional_inventory_problems({}, present) == [
        "ncbi-ast: data/raw/ncbi_ast_activity.tsv exists but has no queue row",
    ]
    assert optional_inventory_problems(
        {"ncbi-ast": {"status": "ADOPTED"}},
        present,
    ) == []

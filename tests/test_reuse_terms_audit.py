"""Outreach state must match sent requests without implying permission."""

from __future__ import annotations


def test_reuse_outreach_distinguishes_sent_requests_from_pending_drafts(repo_root):
    text = (repo_root / "research" / "2026-08-31-reuse-terms-outreach.md").read_text()
    assert "BV-BRC-API #204" in text
    assert "hivdb/sierra #40" in text
    assert "| BacDive | Not sent |" in text
    assert "| CO-ADD | Not sent |" in text
    assert "no authenticated mail channel" in text
    assert "remain unverified" in text


def test_reuse_audit_keeps_unverified_sources_out_of_adopted_state(repo_root):
    rows = (repo_root / "curation" / "source_queue.tsv").read_text().splitlines()
    by_id = {row.split("\t", 1)[0]: row.split("\t") for row in rows[1:]}
    assert by_id["bv-brc"][8] == "CANDIDATE"
    assert by_id["bv-brc"][5] == "UNVERIFIED"
    assert by_id["stanford-hivdb"][8] == "CANDIDATE"
    assert by_id["stanford-hivdb"][5] == "UNVERIFIED"
    assert by_id["co-add"][8] == "BLOCKED"
    assert by_id["bacdive"][5] == "ATTRIBUTION"

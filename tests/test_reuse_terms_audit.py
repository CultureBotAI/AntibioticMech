"""The reuse audit must never imply that an unsent draft granted permission."""

from __future__ import annotations


def test_reuse_outreach_is_explicitly_unsent(repo_root):
    text = (repo_root / "research" / "2026-08-31-reuse-terms-outreach.md").read_text()
    assert "NOT SENT" in text
    assert "no authenticated mail channel" in text


def test_reuse_audit_keeps_unverified_sources_out_of_adopted_state(repo_root):
    rows = (repo_root / "curation" / "source_queue.tsv").read_text().splitlines()
    by_id = {row.split("\t", 1)[0]: row.split("\t") for row in rows[1:]}
    assert by_id["bv-brc"][8] == "CANDIDATE"
    assert by_id["bv-brc"][5] == "UNVERIFIED"
    assert by_id["stanford-hivdb"][8] == "CANDIDATE"
    assert by_id["stanford-hivdb"][5] == "UNVERIFIED"
    assert by_id["co-add"][8] == "BLOCKED"
    assert by_id["bacdive"][5] == "ATTRIBUTION"

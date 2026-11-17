"""Outreach state must match sent requests without implying permission."""

from __future__ import annotations


def test_reuse_outreach_distinguishes_sent_requests_from_pending_draft(repo_root):
    text = (repo_root / "research" / "2026-08-31-reuse-terms-outreach.md").read_text()
    assert "BV-BRC-API #204" in text
    assert "hivdb/sierra #40" in text
    assert "LeibnizDSMZ/bacdive-api #1" in text
    assert "| BacDive | 2026-08-31 | Official BacDive API GitHub tracker |" in text
    assert "closed 2026-09-30; official BacDive ticket still required" in text
    assert "| CO-ADD | Not sent |" in text
    assert "No authenticated mail/form-capable channel" in text
    assert "Google image reCAPTCHA" in text
    assert "BV-BRC remains\nunverified" in text
    assert "Stanford HIVDB's response resolves" in text


def test_reuse_audit_keeps_unverified_sources_out_of_adopted_state(repo_root):
    rows = (repo_root / "curation" / "source_queue.tsv").read_text().splitlines()
    by_id = {row.split("\t", 1)[0]: row.split("\t") for row in rows[1:]}
    assert by_id["bv-brc"][8] == "CANDIDATE"
    assert by_id["bv-brc"][5] == "UNVERIFIED"
    assert by_id["stanford-hivdb"][8] == "ADOPTED"
    assert by_id["stanford-hivdb"][5] == "CC0_OK"
    assert by_id["stanford-hivdb"][10] == "https://github.com/hivdb/hivfacts"
    assert by_id["co-add"][8] == "BLOCKED"
    assert by_id["co-add"][10] == "https://db.co-add.org/downloads/"
    assert "archive contains no README or licence" in by_id["co-add"][11]
    assert "REQUEST DRAFTED, NOT SENT" in by_id["co-add"][11]
    assert by_id["bacdive"][5] == "ATTRIBUTION"
    assert by_id["bacdive"][8] == "EVALUATING"
    assert "met_antibiotica" in by_id["bacdive"][11]
    assert "met_antibiogram_v2" in by_id["bacdive"][11]
    assert "non-writing evaluator" in by_id["bacdive"][11]
    assert "fillable exact-structure drug map" in by_id["bacdive"][11]
    assert "no data are adopted until DSMZ confirms" in by_id["bacdive"][11]


def test_attribution_notice_covers_adopted_redistributed_sources(repo_root):
    text = (repo_root / "ATTRIBUTION.md").read_text(encoding="utf-8")
    rows = (repo_root / "curation" / "source_queue.tsv").read_text().splitlines()
    adopted = {row.split("\t", 1)[0] for row in rows[1:]
               if row.split("\t")[8] == "ADOPTED"}
    attribution_markers = {
        "aro": "Antibiotic Resistance Ontology",
        "bindingdb": "BindingDB",
        "chebi": "ChEBI",
        "cryptic": "CRyPTIC Consortium Dataset",
        "fda_drugsfda": "Drugs@FDA",
        "fda_gsrs": "FDA GSRS / UNII",
        "mibig": "MIBiG",
        "phibase": "PHI-base",
        "pubchem": "PubChem",
        "stanford-hivdb": "Stanford HIVDB",
    }

    assert set(attribution_markers) == adopted
    for marker in attribution_markers.values():
        assert marker in text

    for field in (
        "producer_organisms[].source",
        "molecular_targets[].source",
        "resistance_mechanisms[].source",
        "activity_spectrum[].source",
        "genotype_resistance_score_rules[].source",
        "clinical_status_assertions[].source",
    ):
        assert field in text


def test_coadd_audit_records_distribution_without_implying_reuse_permission(repo_root):
    audit = (repo_root / "research" / "2026-08-31-reuse-terms-audit.md").read_text()
    outreach = (repo_root / "research" / "2026-08-31-reuse-terms-outreach.md").read_text()
    assert "https://db.co-add.org/downloads/" in audit
    assert "6334cce7f9c9857099d28170f331899fd225a99c14582467fe46b3f299ef8149" in audit
    assert "Archive inspection found no README, licence, or attribution file" in audit
    assert "834a80fd00eb816dd63a9ca1005905d03c5cb3ef88a1a96c18c7c2ecd02139ae" in audit
    assert "CO-ADD_r03.02-2020_CSV.zip" in outreach

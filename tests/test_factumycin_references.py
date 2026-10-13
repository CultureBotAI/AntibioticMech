"""Unrelated homonyms must never become resistance reference assignments."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "research/2026-10-13-factumycin-reference-context.json"


def test_rejected_fact_homonyms_stay_separate_from_experimental_identity(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    public = json.loads(PUBLIC.read_bytes())
    pin = public["inputs"]["literature_expansion"]
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    prior = json.loads(raw)
    assert public["aro_id"] == "ARO:3001313"
    assert prior["terms"][public["aro_id"]]["record_memberships"] == [public["record"]["identifier"]]
    historical = next(r for r in prior["records"] if r["identifier"] == public["record"]["identifier"])
    assert public["record"]["sha256"] == historical["record_sha256"]
    assert public["record"]["standard_inchi_key"] == historical["standard_inchi_key"]
    expected = {
        "UniProtKB:Q9FFQ7": ("NCBITaxon:3702", 133, 1),
        "UniProtKB:F7EL37": ("NCBITaxon:8364", 88, 3),
        "UniProtKB:A0AAV6MSF6": ("NCBITaxon:37648", 5, 1),
    }
    hits = public["rejected_name_matches"]
    assert {h["accession"] for h in hits} == set(expected)
    for hit in hits:
        assert (hit["entry_reported_taxon_id"], hit["entry_version"], hit["sequence_version"]) == expected[
            hit["accession"]]
        assert hit["disposition"] == "REJECTED_AS_FACTUMYCIN_REFERENCE_UNRELATED_HOMONYM"
        assert not hit["taxonomy_endpoint_checked"] and not hit["source_doi_in_bibliography"]
        assert not hit["experimental_subject_assignment"] and not hit["exact_allele_assignment"]
    assert public["accepted_protein_references"] == []
    assert public["summary"]["experimental_taxa_assigned"] == 0
    assert public["summary"]["whole_records_completed"] == 0


def test_empty_query_and_primary_access_hold_do_not_claim_absence_or_review():
    public = json.loads(PUBLIC.read_bytes())
    assert public["queries"]["facT"]["results"] == 3
    assert public["queries"]["factumycin"]["results"] == 0
    for query in public["queries"].values():
        assert query["complete_for_query"] and not query["establishes_biological_absence"]
        assert query["request"]["release"] == "2026_03"
    assert public["primary_access"]["status"] == "TOOL_INACCESSIBLE_NO_HTTP_STATUS_AVAILABLE"
    assert not public["primary_access"]["primary_results_reviewed"]
    assert not public["primary_access"]["retried_or_alternate_transport_used"]

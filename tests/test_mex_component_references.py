"""Component references never identify a complete pump or experimental allele."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mex_component_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_published_metadata_does_not_require_ignored_cache_or_current_corpus(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    assert result["scope"] == audit.SCOPE
    assert result["limits"] == audit.LIMITS
    assert result["summary"] == {
        "corpus_records_hash_checked": 2939,
        "complete_records_read": 27,
        "source_terms": 16,
        "source_claims": 77,
        "queried_symbols": 29,
        "matched_symbols": 19,
        "reference_entries": 20,
        "reference_entry_types": {"UniProtKB reviewed (Swiss-Prot)": 13, "UniProtKB unreviewed (TrEMBL)": 7},
        "reference_taxa": 2,
        "new_taxonomy_requests": 0,
        "new_uniprot_searches": 4,
        "native_component_annotations": 12,
        "terms_with_all_label_components_annotated": 7,
        "claims_with_all_label_components_annotated": 43,
    }
    assert len(result["unmatched_symbols"]) == 10
    assert len(result["terms"]) == 16 and len(result["claims"]) == 77 and len(result["records"]) == 27
    records = {r["identifier"]: r for r in result["records"]}
    for claim in result["claims"]:
        record = records[claim["record_identifier"]]
        assert claim["record_sha256"] == record["record_sha256"]
        assert claim["standard_inchi_key"] == record["standard_inchi_key"]
        assert claim["experimental_subject_assignment"] is False
    for tid, term in result["terms"].items():
        assert term["record_memberships"] == sorted(
            {c["record_identifier"] for c in result["claims"] if c["aro_id"] == tid}
        )
        assert term["complex_has_single_protein_identity"] is False
        assert term["selected_for_broad_single_protein_index"] is False
    for reference in result["reference_candidates"].values():
        assert reference["experimental_subject_assignment"] is reference["exact_allele_assignment"] is False
        assert reference["experimental_genome_assignment"] is None
        assert reference["new_primary_results_review"] is False


def test_opra_candidates_are_not_a_pao1_complex_or_exact_allele():
    result = public_result()
    term = result["terms"]["ARO:3003038"]
    assert term["all_label_components_have_native_annotations"] is False
    for component in term["components"].values():
        assert component["native_complex_component_references"] == []
    candidates = term["components"]["oprA"]["symbol_query_candidates"]
    assert candidates == ["UniProtKB:I0IYR4", "UniProtKB:I0IYR5"]
    for accession in candidates:
        ref = result["reference_candidates"][accession]
        assert ref["reference_taxonomy"]["native_rank"] == "species"
        assert ref["reference_taxonomy"]["taxon_id"] == "NCBITaxon:287"
    assert result["reference_candidates"]["UniProtKB:G3XD21"]["reference_taxonomy"]["native_rank"] == "strain"


@pytest.mark.parametrize(
    "tid,symbol", [("ARO:3004066", "mexT"), ("ARO:3004068", "mexS"), ("ARO:3004070", "mvaT")]
)
def test_regulator_is_not_a_structural_component_or_verified_alteration(tid, symbol):
    result = public_result()
    term = result["terms"][tid]
    assert symbol not in term["components"]
    assert len(term["regulatory_subject_candidates"]) == 1
    ref = result["reference_candidates"][term["regulatory_subject_candidates"][0]]
    assert symbol in ref["gene_symbols"] and ref["component_annotations"] == []
    assert term["regulatory_alteration_or_effect_verified"] is False


def test_mixed_native_evidence_does_not_upgrade_probable_relations():
    refs = public_result()["reference_candidates"]
    for accession in ("UniProtKB:G3XCW2", "UniProtKB:Q51397", "UniProtKB:Q9I0Y7"):
        (relation,) = refs[accession]["component_annotations"]
        assert "Probable" in relation["native_relation_qualifiers"]
        assert {r["evidenceCode"] for r in relation["whole_text_evidence"]} == {"ECO:0000269", "ECO:0000305"}
        assert relation["evidence_scope"] == "WHOLE_NATIVE_TEXT_NOT_RELATION_LEVEL_PRIMARY_PROOF"
        assert relation["primary_results_independently_reviewed"] is False
    opm = {r["complex_label"]: r for r in refs["UniProtKB:Q51487"]["component_annotations"]}
    assert opm["MexAB-OprM"]["native_relation_qualifiers"] == []
    assert opm["MexXY-OprM"]["native_relation_qualifiers"] == ["Probable"]


def test_symbol_only_hits_do_not_prove_composition():
    term = public_result()["terms"]["ARO:3000799"]
    assert term["all_label_components_have_native_annotations"] is False
    assert all(c["symbol_query_candidates"] for c in term["components"].values())
    assert all(not c["native_complex_component_references"] for c in term["components"].values())


def relation_fixture():
    text = "Component of the MexXY-OprM multidrug efflux complex (Probable)"
    entry = {
        "comments": [
            {
                "commentType": "SUBUNIT",
                "texts": [{"value": text, "evidences": [{"evidenceCode": "ECO:0000305"}]}],
            }
        ]
    }
    assessment = {
        "complex_label": "MexXY-OprM",
        "native_relation_qualifiers": ["Probable"],
        "pointer": "/comments/0/texts/0",
        "text_sha256": hashlib.sha256(text.encode()).hexdigest(),
    }
    return entry, assessment


@pytest.mark.parametrize("change", ["text", "type", "pointer", "complex", "qualifier", "duplicate"])
def test_changed_native_component_context_fails_closed(change):
    entry, assessment = relation_fixture()
    if change == "text":
        entry["comments"][0]["texts"][0]["value"] += " changed"
    elif change == "type":
        entry["comments"][0]["commentType"] = "FUNCTION"
    elif change == "pointer":
        assessment["pointer"] = "/comments/1/texts/0"
    elif change == "complex":
        assessment["complex_label"] = "MexXY-OprA"
    elif change == "qualifier":
        assessment["native_relation_qualifiers"] = ["By similarity"]
    rows = [assessment] * (2 if change == "duplicate" else 1)
    with pytest.raises(ValueError):
        audit.component_annotations(entry, rows)


def test_component_projection_is_pure():
    entry, assessment = relation_fixture()
    before = copy.deepcopy((entry, assessment))
    projected = audit.component_annotations(entry, [assessment])
    assert (entry, assessment) == before
    assert projected[0]["native_relation_qualifiers"] == ["Probable"]


@pytest.mark.parametrize(
    "change",
    [
        "url",
        "status",
        "release",
        "pagination",
        "redirect",
        "retry",
        "count",
        "bytes",
        "duplicate",
        "sequence",
        "features",
    ],
)
def test_native_query_rejects_scope_or_completeness_drift(tmp_path, change):
    from urllib.parse import urlencode

    expected = audit.parameters(["mexA"], 287, True)
    entries = [{"primaryAccession": "TEST"}]
    receipt = {
        "url": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(expected, doseq=True),
        "status": 200,
        "redirects_followed": 0,
        "retries": 0,
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": "1"},
    }
    if change == "url":
        receipt["url"] = receipt["url"].replace("gene_exact", "protein_name")
    elif change == "status":
        receipt["status"] = 403
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "old"
    elif change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "redirect":
        receipt["redirects_followed"] = 1
    elif change == "retry":
        receipt["retries"] = 1
    elif change == "count":
        receipt["headers"]["x-total-results"] = "2"
    elif change == "duplicate":
        entries *= 2
        receipt["headers"]["x-total-results"] = "2"
    elif change in {"sequence", "features"}:
        entries[0][change] = {}
    body = tmp_path / "response.json"
    body.write_text(json.dumps({"results": entries}))
    receipt["body"] = audit.pin(tmp_path, body)
    receipt["bytes"] = body.stat().st_size + (change == "bytes")
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError):
        audit.native_query(tmp_path, audit.pin(tmp_path, path), expected)


def test_erm36_hold_preserves_http403_without_claiming_primary_review():
    hold = json.loads((ROOT / "research/2026-10-15-erm36-access-hold.json").read_bytes())
    assert hold["status"] == "PUBLISHER_FULLTEXT_HTTP403_ACCESS_HOLD"
    assert hold["request"]["status"] == 403
    assert hold["request"]["retries"] == hold["request"]["redirects_followed"] == 0
    assert hold["fulltext_inspected"] is hold["alternate_routes_attempted_after_403"] is False
    assert hold["primary_signoff"] is hold["reuse_terms_review_resumed"] is False
    assert hold["issue_1040"] == "DEFERRED" and hold["ncbi_requests"] == 0
    audit.check_pin(ROOT, hold["prior_dossier"])


def test_public_artifact_pins():
    receipt = json.loads((ROOT / (audit.PREFIX + "-verification.json")).read_bytes())
    paths = [
        p
        for p in receipt["files"]
        if p["path"].startswith(audit.PREFIX) or p["path"] == "research/2026-10-15-erm36-access-hold.json"
    ]
    assert len(paths) == 5
    for item in paths:
        audit.check_pin(ROOT, item)
    assert receipt["summary"] == public_result()["summary"]
    assert receipt["preservation"]["biological_records_changed"] == 0


def test_live_offline_replay_when_native_cache_and_checkpoint_available():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    sources = list(plan["queries"].values()) + [p["receipt"] for p in plan["taxonomy"].values()]
    if any(not (ROOT / p["path"]).exists() for p in sources):
        pytest.skip("native ignored cache not available; portable public checks still run")
    result = public_result()
    import csv

    update = json.loads((ROOT / result["explicit_corpus_update"]["path"]).read_bytes())
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with (ROOT / result["inputs"]["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (ROOT / r["path"]).exists()
        or audit.digest(ROOT / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.skip("historical checkpoint after corpus changes; immutable artifact checks still run")
    assert audit.build(ROOT) == result

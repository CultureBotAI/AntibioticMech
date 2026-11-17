"""Keep table coverage, chemical scope and reference identity separate."""

import builtins
import copy
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mex_substrate_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize("key", audit.FALSE_FIELDS)
def test_scope_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "change", ["host", "units", "factor", "ownership", "negative", "table", "alias", "prior", "ncbi"]
)
def test_changed_evidence_context_rejected(change):
    notes = assessment()
    if change == "host":
        notes["assay_species"] = "Escherichia coli"
    elif change == "units":
        notes["standard_units"] = "mm"
    elif change == "factor":
        notes["unit_conversion_factor"] = 1000
    elif change == "ownership":
        notes["citation"]["relationship_to_card_definitions"] = "OWN_DEFINITION_CITATION"
    elif change == "negative":
        notes["non_supporting_selected_comparisons"] = []
    elif change == "table":
        notes["record_table_scope"]["CHEBI:43968"]["table"] = 2
    elif change == "alias":
        notes["record_table_scope"]["CHEBI:59064"] = {"table": 2, "source_label": "polymyxin B"}
    elif change == "prior":
        notes["cross_study_qualification"] = "SUPERSEDED"
    else:
        notes["access"]["ncbi_requests"] = 1
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def bibliography_fixture():
    entries, views = {}, {}
    citation = {
        "citationType": "journal article",
        "citationCrossReferences": [
            {"database": "PubMed", "id": audit.PMID},
            {"database": "DOI", "id": audit.DOI},
        ],
    }
    for acc, (gene, locus, number, positions) in audit.BIBLIOGRAPHY.items():
        entries[acc] = {
            "references": [
                {
                    "referenceNumber": number,
                    "citation": copy.deepcopy(citation),
                    "referencePositions": positions[:],
                }
            ]
        }
        views["UniProtKB:" + acc] = {"gene_symbols": [gene], "ordered_locus_names": [locus]}
    return entries, views


def test_three_bibliographies_are_one_paper_not_three_experiments():
    bindings = audit.bibliography_bindings(*bibliography_fixture())
    assert len(bindings) == 3
    assert len({b["citation_sha256"] for b in bindings.values()}) == 1
    assert all(
        b["independent_experiment_per_protein"] is b["experimental_subject_assignment"] is False
        for b in bindings.values()
    )


@pytest.mark.parametrize(
    "change", ["missing", "duplicate", "extra", "doi", "positions", "comments", "gene", "locus", "citation"]
)
def test_changed_bibliography_binding_rejected(change):
    entries, views = bibliography_fixture()
    row = entries["G3XCW2"]["references"][0]
    if change == "missing":
        entries.pop("G3XCW2")
    elif change == "duplicate":
        entries["G3XCW2"]["references"].append(copy.deepcopy(row))
    elif change == "extra":
        entries["OTHER"] = copy.deepcopy(entries["G3XCW2"])
    elif change == "doi":
        row["citation"]["citationCrossReferences"][1]["id"] = "10.invalid"
    elif change == "positions":
        row["referencePositions"] = ["SEQUENCE"]
    elif change == "comments":
        row["referenceComments"] = [{"type": "STRAIN", "value": "PAO1"}]
    elif change == "gene":
        views["UniProtKB:G3XCW2"]["gene_symbols"] = ["mexX"]
    elif change == "locus":
        views["UniProtKB:G3XCW2"]["ordered_locus_names"] = ["PA2019"]
    else:
        row["citation"]["title"] = "Different native citation"
    with pytest.raises(ValueError):
        audit.bibliography_bindings(entries, views)


def test_own_citation_scan_includes_unselected_terms():
    definitions = {
        "terms": {
            "UNSELECTED": {"definition_citation_ids": ["PMID:" + audit.PMID]},
            "ARO:3003032": {"definition_citation_ids": []},
        }
    }
    assert audit.citation_owners(definitions) == ["UNSELECTED"]


def prior_dispositions(result):
    return [
        c
        for pin in result["prior_contexts"].values()
        for c in audit.read_json(ROOT, pin)["claim_dispositions"]
    ]


@pytest.mark.parametrize(
    "change", ["missing_claim", "duplicate_claim", "missing_prior", "claim_hash", "inchi", "label", "record"]
)
def test_dispositions_require_exact_complete_claim_context(change):
    result = public_result()
    claims, records, previous = result["claims"], result["records"], prior_dispositions(result)
    if change == "missing_claim":
        claims.pop()
    elif change == "duplicate_claim":
        claims[-1] = copy.deepcopy(claims[0])
    elif change == "missing_prior":
        previous.pop()
    elif change == "claim_hash":
        claims[0]["claim_sha256"] = "changed"
    elif change == "inchi":
        records[0]["standard_inchi_key"] = "changed"
    elif change == "label":
        records[0]["label"] = "changed"
    else:
        records.append(copy.deepcopy(records[0]))
    with pytest.raises(ValueError):
        audit.dispositions(claims, records, previous)


def test_portable_artifact_preserves_scope_and_previous_qualifications(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    plan = audit.read_json(ROOT, result["plan"])
    audit.validate_assessment(audit.read_json(ROOT, result["assessment"]))
    previous = prior_dispositions(result)
    old = audit.read_json(ROOT, result["prior_mex"])
    assert result["claims"] == [c for c in old["claims"] if c["aro_id"] in audit.TERMS]
    assert len(result["records"]) == 21 and len(result["claims"]) == 33
    assert result["claim_dispositions"] == audit.dispositions(result["claims"], result["records"], previous)
    definitions = audit.read_json(ROOT, plan["definition_citations"])
    assert audit.citation_owners(definitions) == result["definition_citation_owners"] == []
    for tid in audit.TERMS:
        assert (
            result["preserved_definition_citations"][tid]
            == definitions["terms"][tid]["definition_citation_ids"]
        )
    assert len(result["reference_views"]) == 8
    for accession, view in result["reference_views"].items():
        assert view["native_entry_sha256"] == old["reference_candidates"][accession]["native_entry_sha256"]
        assert view["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
        assert view["experimental_subject_assignment"] is view["whole_complex_identity_assignment"] is False
    assert result["paper_species_grounding"]["taxon_id"] == "NCBITaxon:287"
    assert (
        result["preserved_opra_access_hold"]
        == audit.read_json(ROOT, result["prior_contexts"]["mexxy_definitions"])["preserved_opra_access_hold"]
    )
    rows = result["claim_dispositions"]
    assert (
        sum(
            bool(c.get("selected_primary_qualification") or c.get("selected_qualification")) for c in previous
        )
        == 9
    )
    assert sum(r["table"] is None for r in rows) == 8
    assert sum(r["label_relation"] == "GENERIC_LABEL_NOT_EXACT_RECORD_FORM" for r in rows) == 5
    negative = [r for r in rows if r["comparison_status"] == audit.NO_INCREASE]
    assert len(negative) == 1 and (negative[0]["aro_id"], negative[0]["record_identifier"]) == audit.NEGATIVE
    assert all(
        r["exact_chemical_form_verified"]
        is r["whole_claim_primary_signoff"]
        is r["previous_qualification_superseded"]
        is False
        for r in rows
    )
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["biological_records_changed"] == result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"


def test_no_operational_or_numeric_ast_exports():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_read_only_replay_when_native_cache_available(monkeypatch, pre_cdsa_qualification_root):
    result = public_result()
    if not (ROOT / result["native_query_source"]["receipt"]["path"]).exists():
        pytest.skip("native cache unavailable; portable artifact checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not set(mode) & set("wax+"), "offline replay attempted write"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == result

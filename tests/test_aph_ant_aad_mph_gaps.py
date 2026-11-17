"""Historical naming and shared citations never establish an experimental allele."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_aph_ant_aad_mph_gaps as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def reference_fixture():
    nomenclature = json.loads((ROOT / "research/2026-10-09-structure-primary-context.json").read_bytes())
    structural = json.loads((ROOT / "research/2026-10-09-card-structure-links.json").read_bytes())
    old = nomenclature["proteins"]["O68183"]
    taxonomy = {
        **nomenclature["taxonomy"]["37734"],
        "lineage": [{"taxonId": 1350, "scientificName": "Enterococcus", "rank": "genus"}],
    }
    entry = {
        "primaryAccession": "O68183",
        "entryType": old["entry_type"],
        "entryAudit": old["entry_audit"],
        "genes": old["gene_names_with_provenance"],
        "organism": old["organism"],
        "proteinDescription": {"submissionNames": [{"fullName": {"value": "APH(2'')-Id"}}]},
        "uniProtKBCrossReferences": [],
        "references": [
            {
                "referenceNumber": i,
                "citation": {
                    "citationType": "submission" if i == 6 else "journal article",
                    "citationCrossReferences": [{"database": "PubMed", "id": "9593155"}] if i == 1 else [],
                },
            }
            for i in range(1, 12)
        ],
    }
    return entry, taxonomy, nomenclature, structural


def test_historical_name_relation_supports_only_a_reference():
    args = reference_fixture()
    before = copy.deepcopy(args)
    result = audit.project_reference(*args)
    assert args == before
    assert result["gene_symbols"] == ["aph(2'')-Id"]
    assert result["reference_taxonomy"]["taxon_id"] == "NCBITaxon:37734"
    assert result["reference_taxonomy"]["native_rank"] == "species"
    assert result["exact_allele_assignment"] is result["experimental_subject_assignment"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["nomenclature_primary_text_replayed_here"] is result["new_primary_results_review"] is False
    assert result["scope"] == audit.QUALIFIED
    assert len(result["native_bibliography"]) == 11


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "gene",
        "name",
        "version",
        "boolean_version",
        "reviewed",
        "taxon",
        "rank",
        "inactive",
        "parent",
        "xref",
        "flag",
        "sequence",
        "features",
        "citation",
        "count",
        "citation_number",
        "source_name",
        "revised_name",
        "nomenclature_pmid",
        "nomenclature_doi",
        "review_medium",
        "primary_cached",
        "whole_paper",
        "structure_accession",
        "structure_taxon",
        "structure_entity",
        "historical_version",
    ],
)
def test_reference_identity_and_evidence_limits_fail_closed(change):
    entry, taxon, nomenclature, structural = reference_fixture()
    review = nomenclature["nomenclature_review"]
    entity = structural["links"][audit.TERM]["structures"][0]["entities"][0]
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "gene":
        entry["genes"] = [{"geneName": {"value": "aph"}}]
    elif change == "name":
        entry["proteinDescription"]["submissionNames"][0]["fullName"]["value"] += "-other"
    elif change in {"version", "boolean_version"}:
        entry["entryAudit"] = (
            {"entryVersion": 114, "sequenceVersion": 1}
            if change == "version"
            else {"entryVersion": 113, "sequenceVersion": True}
        )
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "taxon":
        entry["organism"] = {"taxonId": 562, "scientificName": "Escherichia coli"}
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "parent":
        taxon["parent"]["taxonId"] = 1
    elif change == "xref":
        entry["uniProtKBCrossReferences"] = [{"database": "CARD", "id": audit.TERM}]
    elif change == "flag":
        entry["proteinDescription"]["flag"] = "Fragment"
    elif change in {"sequence", "features"}:
        entry[change] = {}
    elif change == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "1"
    elif change == "count":
        entry["references"].pop()
    elif change == "citation_number":
        entry["references"][0]["referenceNumber"] = 2
    elif change in {"source_name", "revised_name", "review_medium"}:
        review[change] = "OTHER"
    elif change == "nomenclature_pmid":
        review["reference"] = "PMID:1"
    elif change == "nomenclature_doi":
        review["doi"] = "10.1000/other"
    elif change == "primary_cached":
        review["native_primary_file_cached"] = True
    elif change == "whole_paper":
        review["whole_paper_review_complete"] = True
    elif change == "structure_accession":
        entity["reference_accessions"] = ["UniProtKB:OTHER"]
    elif change == "structure_taxon":
        entity["source_organisms"][0]["ncbi_taxonomy_id"] = 562
    elif change == "structure_entity":
        entity["entity_id"] = "3N4T_2"
    else:
        nomenclature["proteins"]["O68183"]["entry_audit"] = {"entryVersion": 1, "sequenceVersion": 1}
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon, nomenclature, structural)


def test_prefix_cohort_includes_lowercase_labels_and_excludes_linked_terms():
    index = {"terms": {str(i): {"links": []} for i in range(6)}}
    labels = ["APH(9)-Ic", "aadT", "mphF", "ANT(3'')-IIc", "other", "APH-linked"]
    direct = {"determinants": {str(i): {"labels": [n]} for i, n in enumerate(labels)}}
    index["terms"]["5"]["links"] = [{"protein_accession": "reference"}]
    assert audit.select_terms(index, direct) == {str(i): labels[i] for i in range(4)}
    direct["determinants"]["0"]["labels"].append("another")
    with pytest.raises(ValueError, match="multiple source labels"):
        audit.select_terms(index, direct)


def check_public_bytes(root):
    receipt = json.loads((root / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 2
    assert {p["path"] for p in pins} == {str(audit.OUTPUT), str(audit.PLAN)}
    for pin in pins:
        assert hashlib.sha256((root / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]


def test_public_checkpoint_is_verified_without_native_caches(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "reports")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    check_public_bytes(ROOT)
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    paths = {k: audit.reference.check_pin(ROOT, p) for k, p in plan["inputs"].items()}
    index = json.loads(paths["index"].read_bytes())
    with paths["census"].open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    ids = {rid for tid in plan["terms"] for rid in index["terms"][tid]["record_memberships"]}
    assert result["records"] == [r for r in census if r["identifier"] in ids]
    assert result["claims"] == [c for c in index["claims"] if c["aro_id"] in plan["terms"]]
    assert result["summary"] == {
        "corpus_records_hash_checked": 2939,
        "complete_records_read": 16,
        "source_terms": 14,
        "source_claims": 38,
        "complete_cached_citation_queries": 14,
        "citation_query_entries": 29,
        "distinct_citation_entries": 29,
        "qualified_reference_terms": 1,
        "qualified_reference_proteins": 1,
        "qualified_reference_memberships": 4,
        "term_statuses": {audit.QUALIFIED: 1, audit.UNMATCHED: 7, audit.EMPTY: 6},
    }
    assert set(result["terms"]) == set(plan["terms"])
    assert all(not t["biological_absence_inferred"] for t in result["terms"].values())
    assert result["limits"]["broad_index_updated"] is False
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["references"][audit.ACCESSION]["exact_allele_assignment"] is False


@pytest.mark.parametrize("change", ["gene", "taxon", "experimental", "plan", "missing", "duplicate_pin"])
def test_public_metadata_drift_is_detected_without_native_cache(tmp_path, change):
    for suffix in (".json", "-plan.json", "-verification.json"):
        path = Path(audit.PREFIX + suffix)
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_bytes((ROOT / path).read_bytes())
    path = tmp_path / audit.OUTPUT
    result = json.loads(path.read_bytes())
    protein = result["references"][audit.ACCESSION]
    if change == "missing":
        path.unlink()
    elif change == "plan":
        (tmp_path / audit.PLAN).write_bytes((tmp_path / audit.PLAN).read_bytes() + b"\n")
    elif change == "duplicate_pin":
        path = tmp_path / (audit.PREFIX + "-verification.json")
        result = json.loads(path.read_bytes())
        result["files"].append(next(p for p in result["files"] if p["path"] == str(audit.OUTPUT)))
        path.write_text(json.dumps(result))
    else:
        if change == "gene":
            protein["gene_symbols"] = ["OTHER"]
        elif change == "taxon":
            protein["reference_taxonomy"]["taxon_id"] = "NCBITaxon:1"
        else:
            protein["experimental_subject_assignment"] = True
        path.write_text(json.dumps(result))
    with pytest.raises((AssertionError, FileNotFoundError)):
        check_public_bytes(tmp_path)


def test_native_replay_has_no_network_or_file_writes(monkeypatch):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    for pin in plan["inputs"].values():
        if audit.reference.digest(ROOT / pin["path"]) != pin["sha256"]:
            pytest.skip("historical input changed; immutable public snapshot tested separately")
    with (ROOT / plan["inputs"]["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if {r["path"] for r in census} != {
        str(p.relative_to(ROOT)) for p in (ROOT / "data/antibiotics").rglob("*.yaml")
    } or any(audit.reference.digest(ROOT / r["path"]) != r["record_sha256"] for r in census):
        pytest.skip("historical corpus changed; immutable public snapshot tested separately")
    first = next(iter(plan["queries"].values()))["query"]["pages"][0]["cache"]["path"]
    if not (ROOT / first).is_file():
        pytest.skip("native request caches are intentionally not committed")
    original = Path.open

    def guarded(path, mode="r", *args, **kwargs):
        assert not any(flag in mode for flag in "wax+")
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_export_has_no_operational_payloads():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(result)) & {
        "sequence",
        "features",
        "variants",
        "alteration",
        "protocol",
        "primers",
        "coordinates",
        "measurement_value",
        "activity_spectrum",
        "resistance_mechanisms",
        "headers",
        "body",
    }

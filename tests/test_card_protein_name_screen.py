"""Literal database names remain discovery evidence, never tested-allele identity."""

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
import audit_card_protein_name_screen as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.mark.parametrize("block", audit.SELECTION["name_blocks"])
@pytest.mark.parametrize("field", audit.SELECTION["name_fields"])
def test_screen_includes_native_short_and_full_names(block, field):
    name = {field: {"value": "Example"} if field == "fullName" else [{"value": "Example"}]}
    entry = {"proteinDescription": {block: name if block == "recommendedName" else [name]}}
    expected = f"{block}/0/{field}" + ("/0" if field == "shortNames" else "")
    assert audit.name_matches(entry, "example") == [{"path": expected, "value": "Example"}]


@pytest.mark.parametrize(
    "label,name,match",
    [
        ("TEM-5", "TEM-5", True),
        ("TEM-5", "TEM-50", False),
        ("TEM-5", "TEM-5a", False),
        ("TEM-5", "TEM-5-other", False),
        ("TEM-5", "TEM-5'", False),
        ("TEM-5", "XTEM-5", False),
        ("TEM-8", "TEM-8/CAZ-2", True),
        ("APH(2'')", "APH(2'')", True),
        ("APH(2'')", "APH(2')", False),
        ("AdeIJK", "AdeIJK outer membrane subunit", True),
    ],
)
def test_literal_boundaries_do_not_normalize_or_conflate_alleles(label, name, match):
    entry = {"proteinDescription": {"submissionNames": [{"fullName": {"value": name}}]}}
    assert bool(audit.name_matches(entry, label)) is match


def test_genes_are_not_silently_added_to_the_name_search():
    assert audit.name_matches({"genes": [{"geneName": {"value": "example"}}]}, "example") == []
    with pytest.raises(ValueError, match="empty source label"):
        audit.name_matches({}, "")


def test_source_ownership_precedes_identifier_matching():
    card = {
        "aro_id": "ARO:3000256",
        "label": "source label",
        "evidence": [{"reference": "ARO:3000256", "notes": "CARD/ARO asserts a route"}],
    }
    curator = {
        "aro_id": "ARO:3000256",
        "label": "curator interpretation",
        "evidence": [{"reference": "PMID:1"}],
    }
    doc = {"resistance_mechanisms": [curator, card]}
    assert audit.selected_claims(doc, {"ARO:3000256": "source label"}) == [(1, card)]


def test_only_unlinked_terms_are_screened():
    index = {"terms": {"a": {"links": []}, "b": {"links": ["existing"]}}}
    direct = {"determinants": {"a": {"labels": ["first"]}, "b": {"labels": ["second"]}}}
    assert audit.select_terms(index, direct) == {"a": "first"}
    direct["determinants"]["a"]["labels"].append("ambiguous")
    with pytest.raises(ValueError, match="multiple source labels"):
        audit.select_terms(index, direct)


def reference_fixture():
    genus = {"taxonId": 10, "scientificName": "Example", "rank": "genus"}
    species = {"taxonId": 11, "scientificName": "Example species", "rank": "species"}
    subspecies = {"taxonId": 12, "scientificName": "Example subspecies", "rank": "subspecies"}
    taxon = {
        "taxonId": 13,
        "scientificName": "Example strain",
        "rank": "strain",
        "active": True,
        "parent": {"taxonId": 12, "scientificName": "Example subspecies"},
        "lineage": [genus, species, subspecies],
    }
    entry = {
        "primaryAccession": "TEST",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "organism": {"taxonId": 13, "scientificName": "Example strain"},
        "proteinDescription": {
            "submissionNames": [{"fullName": {"value": "Example protein"}}],
            "flag": "Precursor",
        },
        "references": [
            {
                "referenceNumber": 1,
                "citation": {
                    "citationType": "journal article",
                    "citationCrossReferences": [{"database": "DOI", "id": ".1093/example"}],
                },
            }
        ],
    }
    return entry, taxon


def test_native_absences_flags_rank_and_identifier_anomalies_are_preserved():
    entry, taxon = reference_fixture()
    before = copy.deepcopy((entry, taxon))
    result = audit.project_reference(entry, taxon)
    assert (entry, taxon) == before
    assert result["gene_symbols"] == [] and result["gene_field_present"] is False
    assert result["native_protein_flag"] == "Precursor"
    assert result["reference_taxonomy"]["native_rank"] == "strain"
    assert result["reference_taxonomy"]["species"]["taxonId"] == 11
    assert result["reference_taxonomy"]["parent"]["taxonId"] == 12
    assert result["native_identifier_anomalies"][0]["native_identifier"]["id"] == ".1093/example"
    assert result["native_identifier_anomalies"][0]["silently_repaired"] is False
    assert result["experimental_subject_assignment"] is result["exact_allele_assignment"] is False
    assert result["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "change", ["taxon", "name", "parent", "inactive", "cycle", "version", "sequence", "features", "number"]
)
def test_identity_projection_rejects_inconsistent_or_operational_data(change):
    entry, taxon = reference_fixture()
    if change == "taxon":
        entry["organism"]["taxonId"] = 1
    elif change == "name":
        entry["organism"]["scientificName"] = "Other"
    elif change == "parent":
        taxon["parent"]["taxonId"] = 11
    elif change == "inactive":
        taxon["active"] = False
    elif change == "cycle":
        taxon["lineage"].append(taxon["lineage"][0])
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "number":
        entry["references"][0]["referenceNumber"] = 2
    else:
        entry[change] = {}
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon)


def test_missing_citations_and_doi_only_are_not_empty_pubmed_queries():
    assert audit.term_status([], set(), []) == "NO_DEFINITION_CITATIONS_NOT_QUERIED"
    assert audit.term_status(["DOI:10.1000/example"], set(), []) == "NON_PMID_CITATIONS_NOT_QUERIED"
    assert audit.term_status(["PMID:1"], set(), []) == "COMPLETE_PMID_QUERIES_EMPTY_NOT_BIOLOGICAL_ABSENCE"
    assert audit.term_status(["PMID:1"], {"candidate"}, []) == "NO_LITERAL_PROTEIN_NAME_MATCH"


def check_public_bytes(root):
    receipt = json.loads((root / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 2 and {p["path"] for p in pins} == {str(audit.PLAN), str(audit.OUTPUT)}
    for pin in pins:
        assert hashlib.sha256((root / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]


def test_public_checkpoint_without_native_cache(monkeypatch):
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
    assert result["summary"]["source_terms"] == 720
    assert result["summary"]["matched_terms"] == 10
    assert result["summary"]["matched_proteins"] == 8
    assert result["summary"]["complete_cached_citation_queries"] == 643
    assert result["summary"]["term_statuses"]["NO_DEFINITION_CITATIONS_NOT_QUERIED"] == 186
    assert result["terms"]["ARO:3001313"]["other_citations_not_queried"] == ["DOI:10.1039/C2MD20038D"]
    assert result["summary"]["term_statuses"][audit.PENDING] == 6
    assert result["summary"]["term_statuses"][audit.COMPLEX] == 1
    assert result["summary"]["term_statuses"][audit.ALLELES] == 3
    assert result["limits"]["broad_index_updated"] is False
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert all(
        not m["selected_for_broad_index"] and not m["experimental_subject_assignment"]
        for t in result["terms"].values()
        for m in t["name_matches"]
    )
    proteins = result["reference_candidates"]
    assert proteins["UniProtKB:P12921"]["reference_taxonomy"]["species"]["taxonId"] == 1423
    assert proteins["UniProtKB:P12921"]["already_in_base_index"] is True
    assert proteins["UniProtKB:A0A2I6AXF4"]["gene_symbols"] == ["mcr-4"]
    assert proteins["UniProtKB:A0A2I6AXF4"]["reference_taxonomy"]["scientific_name"] == "Enterobacter cloacae"
    for accession in ("R4NN96", "Q9APB1", "S5FUH0"):
        assert proteins["UniProtKB:" + accession]["gene_field_present"] is False


@pytest.mark.parametrize(
    "change", ["gene", "taxon", "assignment", "status", "plan", "missing", "duplicate_pin"]
)
def test_public_pin_drift_fails_without_native_cache(tmp_path, change):
    for suffix in (".json", "-plan.json", "-verification.json"):
        path = Path(audit.PREFIX + suffix)
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_bytes((ROOT / path).read_bytes())
    path = tmp_path / audit.OUTPUT
    result = json.loads(path.read_bytes())
    if change == "missing":
        path.unlink()
    elif change == "plan":
        path = tmp_path / audit.PLAN
        path.write_bytes(path.read_bytes() + b"\n")
    elif change == "duplicate_pin":
        path = tmp_path / (audit.PREFIX + "-verification.json")
        receipt = json.loads(path.read_bytes())
        receipt["files"].append(next(p for p in receipt["files"] if p["path"] == str(audit.OUTPUT)))
        path.write_text(json.dumps(receipt))
    else:
        protein = result["reference_candidates"]["UniProtKB:P12921"]
        if change == "gene":
            protein["gene_symbols"] = ["inferred"]
        elif change == "taxon":
            protein["reference_taxonomy"]["native_rank"] = "species"
        elif change == "assignment":
            protein["exact_allele_assignment"] = True
        else:
            result["terms"]["ARO:3000877"]["name_matches"][0]["status"] = audit.PENDING
        path.write_text(json.dumps(result))
    with pytest.raises((AssertionError, FileNotFoundError)):
        check_public_bytes(tmp_path)


def test_native_replay_without_network_or_file_writes(monkeypatch):
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
    result = audit.build(ROOT)
    assert result == json.loads((ROOT / audit.OUTPUT).read_bytes())

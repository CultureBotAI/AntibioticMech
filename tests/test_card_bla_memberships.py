"""Keep native bla-reference metadata distinct from experimental resistance assignments."""

import copy
import csv
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_bla_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    caches = [p for p in plan["inputs"].values() if p["path"].startswith("reports/")]
    if any(not (ROOT / p["path"]).is_file() for p in caches):
        pytest.skip("native request caches unavailable; public invariants and synthetic guards still run")
    return audit.read_inputs(ROOT)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def reference_fixture(accession):
    expected = audit.SELECTED[accession]
    refs = [
        {"referenceNumber": i + 1, "citation": {"citationType": kind, "title": "Other citation"}}
        for i, kind in enumerate(kind for kind, n in expected["citations"].items() for _ in range(n))
    ]
    refs[0]["citation"].update(
        {
            "title": expected["label"] + " reference context",
            "citationCrossReferences": [
                {"database": "PubMed", "id": expected["pmid"]},
                {"database": "DOI", "id": expected["doi"]},
            ],
        }
    )
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": expected["version"], "sequenceVersion": 1},
        "genes": [
            {
                "geneName": {"value": "bla" + expected["label"]},
                "synonyms": [{"value": s} for s in expected["synonyms"]],
            }
        ],
        "organism": {"taxonId": 562, "scientificName": "Escherichia coli"},
        "uniProtKBCrossReferences": [],
        "references": refs,
    }
    taxon = {
        "taxonId": 562,
        "scientificName": "Escherichia coli",
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 561, "scientificName": "Escherichia"},
        "lineage": [
            {"taxonId": 2, "rank": "domain", "scientificName": "Bacteria"},
            {"taxonId": 561, "rank": "genus", "scientificName": "Escherichia"},
        ],
    }
    return entry, taxon


@pytest.mark.parametrize("accession", audit.SELECTED)
def test_native_reference_preserves_ambiguity_without_promotion(accession):
    values = reference_fixture(accession)
    before = copy.deepcopy(values)
    result = audit.project_reference(*values)
    assert values == before
    assert result["native_synonyms"] == audit.SELECTED[accession]["synonyms"]
    assert result["different_allele_style_synonyms_present"] is (accession == "Q0GA57")
    assert result["synonyms_establish_equivalent_alleles"] is False
    assert result["experimental_allele_assignment"] is result["experimental_genome_assignment"] is None
    assert result["exact_allele_assignment"] is result["experimental_subject_assignment"] is False
    assert result["explicit_card_xref"] is result["primary_results_reviewed"] is False
    assert result["global_bla_prefix_normalization_enabled"] is False
    assert len(result["all_native_citations_accounted"]) == sum(
        audit.SELECTED[accession]["citations"].values()
    )
    assert len(result["matched_source_bibliography"]) == 1
    assert "sequence" not in result and "features" not in result


@pytest.mark.parametrize("accession", audit.SELECTED)
@pytest.mark.parametrize(
    "change",
    [
        "gene",
        "synonyms",
        "version",
        "boolean_version",
        "taxon",
        "species_name",
        "rank",
        "inactive",
        "parent",
        "reviewed",
        "xref",
        "flag",
        "sequence",
        "features",
        "accession",
    ],
)
def test_native_identity_guards(accession, change):
    entry, taxon = reference_fixture(accession)
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "bla"
    elif change == "synonyms":
        entry["genes"][0]["synonyms"] = []
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "taxon":
        entry["organism"]["taxonId"] = 570
    elif change == "species_name":
        taxon["scientificName"] = "Other"
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "parent":
        taxon["parent"]["scientificName"] = "Other"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "xref":
        entry["uniProtKBCrossReferences"] = [{"database": "CARD", "id": "other"}]
    elif change == "flag":
        entry["proteinDescription"] = {"flag": "Fragment"}
    elif change in {"sequence", "features"}:
        entry[change] = {}
    else:
        entry["primaryAccession"] = "OTHER"
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon)


@pytest.mark.parametrize("accession", audit.SELECTED)
@pytest.mark.parametrize(
    "change", ["missing", "duplicate", "wrong_pmid", "doi", "title", "type", "number", "extra"]
)
def test_bibliography_identity_and_complete_accounting(accession, change):
    entry, taxon = reference_fixture(accession)
    refs = entry["references"]
    citation = refs[0]["citation"]
    if change == "missing":
        refs.pop(0)
    elif change == "duplicate":
        refs[1]["citation"] = copy.deepcopy(citation)
    elif change == "wrong_pmid":
        citation["citationCrossReferences"][0]["id"] = "1"
    elif change == "doi":
        citation["citationCrossReferences"][1]["id"] = "10.1000/other"
    elif change == "title":
        citation["title"] = "Different enzyme"
    elif change == "type":
        citation["citationType"] = "submission"
    elif change == "number":
        refs[-1]["referenceNumber"] = 1
    else:
        refs.append({"referenceNumber": len(refs) + 1, "citation": {"citationType": "submission"}})
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon)


def resolve(data, value):
    node = data[value["input"]]
    for token in value["pointer"].split("/")[1:]:
        key = token.replace("~1", "/").replace("~0", "~")
        node = node[int(key)] if isinstance(node, list) else node[key]
    return node


def test_full_partition_and_exact_delta(frozen):
    result, rows = audit.project(*frozen)
    expected = {
        "corpus_records": 2939,
        "card_terms": 2002,
        "card_assertions": 4538,
        "selected_reference_terms": 1279,
        "selected_reference_proteins": 1681,
        "reference_links": 2796,
        "added_reference_terms": 3,
        "added_reference_proteins": 4,
        "added_reference_links": 4,
        "added_reference_memberships": 21,
        "followup_terms": 3,
        "followup_claims": 13,
        "followup_records": 11,
        "whole_record_primary_signoffs": 0,
    }
    assert {k: result["summary"][k] for k in expected} == expected
    assert result["summary"]["term_statuses"][audit.UNSELECTED] == 723
    assert result["summary"]["claim_statuses"][audit.UNSELECTED] == 1291
    assert result["summary"]["claim_statuses"][audit.QUALIFIED] == 13
    assert len(rows) == 2939
    assert all(sum(row[c] for c in audit.COLUMNS.values()) == row["card_assertions"] for row in rows)
    assert sum(row["phi_claims_not_reassessed"] for row in rows) == 217
    assert sum(row["curator_claims_not_reassessed"] for row in rows) == 133
    assert sum(row["score_rules_not_reassessed"] for row in rows) == 467
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)
    assert set(result["proteins"]) - set(frozen[0]["base"]["proteins"]) == {
        "UniProtKB:Q0GA57",
        "UniProtKB:G3K399",
        "UniProtKB:A1E3K9",
        "UniProtKB:A5Y0S3",
    }
    old_rows = {r["identifier"]: r for r in frozen[0]["base_rows"]}
    assert {
        r["identifier"]
        for r in rows
        if r["selected_reference_accessions"] != old_rows[r["identifier"]]["selected_reference_accessions"]
    } == {r["identifier"] for r in frozen[0]["alias_screen"]["records"]}
    assert len(result["new_reference_memberships"]) == 21


def test_input_immutability_pointer_ownership_and_scope(inputs):
    before = copy.deepcopy(inputs)
    result, _ = audit.project(*inputs)
    assert inputs == before

    def walk(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                resolve(inputs[0], value)
            else:
                for child in value.values():
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(result)
    for tid, old in inputs[0]["base"]["terms"].items():
        if tid not in audit.TERMS:
            assert result["terms"][tid] == audit.rebase(old, "terms", tid)
    for accession, old in inputs[0]["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)
    assert result["limits"] == inputs[0]["base"]["limits"]
    assert resolve(inputs[0], result["primary_access_hold"])["http_status"] == 403
    assert set(result["evidence_followups"]) == set(inputs[0]["base"]["evidence_followups"])


@pytest.mark.parametrize(
    "change",
    [
        "claim",
        "missing_claim",
        "record",
        "hold",
        "duplicate",
        "prior_links",
        "source",
        "limits",
        "old_accessions",
        "candidate",
        "native_query",
        "definition",
        "sco1_scope",
    ],
)
def test_reconciliation_rejects_drift(inputs, change):
    data, plan, _ = inputs
    if change == "claim":
        data["alias_screen"]["claims"][0]["claim_sha256"] = "changed"
    elif change == "missing_claim":
        data["alias_screen"]["claims"].pop()
    elif change == "record":
        data["alias_screen"]["records"].pop()
    elif change == "hold":
        data["alias_screen"]["primary_access_hold"]["http_status"] = 200
    elif change == "duplicate":
        data["base"]["proteins"]["UniProtKB:Q0GA57"] = {}
    elif change == "prior_links":
        data["base"]["terms"]["ARO:3001917"]["links"] = [{}]
    elif change == "source":
        plan["inputs"]["source_inventory"] = {"path": "other", "sha256": "changed"}
    elif change == "limits":
        data["base"]["limits"]["ncbi_requests"] = 1
    elif change == "old_accessions":
        data["base_rows"][0]["selected_reference_accessions"] = "changed"
    elif change == "candidate":
        data["alias_screen"]["candidates"]["ARO:3001917|Q0GA57"]["experimental_subject_assignment"] = True
    elif change == "native_query":
        data["native_queries"]["17449211"]["complete_for_query"] = False
    elif change == "definition":
        data["definition_citations"]["terms"]["ARO:3001917"]["definition_citation_ids"] = ["PMID:1"]
    else:
        data["sco1"]["references"]["UniProtKB:A1E3K9"]["exact_allele_assignment"] = True
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_saved_outputs_reproduce(frozen):
    result, rows = audit.project(*frozen)
    for suffix, body in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == body


def test_public_invariants_without_request_caches():
    result = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    with (ROOT / (audit.PREFIX + ".tsv")).open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    base = json.loads(audit.reference.check_pin(ROOT, result["inputs"]["base"]).read_bytes())
    assert len(rows) == len({r["identifier"] for r in rows}) == 2939
    assert len(result["terms"]) == 2002 and len(result["claims"]) == 4538
    assert sum(bool(t["links"]) for t in result["terms"].values()) == 1279
    assert len(result["proteins"]) == 1681
    assert sum(len(t["links"]) for t in result["terms"].values()) == 2796
    assert len(result["new_reference_memberships"]) == 21
    assert all(
        sum(int(row[c]) for c in audit.COLUMNS.values()) == int(row["card_assertions"]) for row in rows
    )
    assert result["limits"] == base["limits"]
    for before, after in zip(base["claims"], result["claims"], strict=True):
        assert {**after, "reference_status": before["reference_status"]} == before
    for tid, old in base["terms"].items():
        if tid not in audit.TERMS:
            assert result["terms"][tid] == audit.rebase(old, "terms", tid)
    for accession, expected in audit.SELECTED.items():
        row = result["new_native_reference_reviews"]["UniProtKB:" + accession]
        assert row["gene_symbols"] == ["bla" + expected["label"]]
        assert row["native_synonyms"] == expected["synonyms"]
        assert row["reference_taxon_id"] == "NCBITaxon:562"
        assert row["native_reference_taxon_rank"] == "species"
        assert row["entry_audit"] == {"entryVersion": expected["version"], "sequenceVersion": 1}
        assert row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        assert row["matched_source_bibliography"][0]["pmid"] == "PMID:" + expected["pmid"]
        assert row["matched_source_bibliography"][0]["doi"] == "DOI:" + expected["doi"]
        assert len(row["all_native_citations_accounted"]) == sum(expected["citations"].values())
        assert row["synonyms_establish_equivalent_alleles"] is False
        assert row["primary_results_reviewed"] is row["exact_allele_assignment"] is False
        assert row["experimental_subject_assignment"] is False
        assert row["experimental_genome_assignment"] is row["experimental_allele_assignment"] is None
    discovery = json.loads(audit.reference.check_pin(ROOT, result["inputs"]["alias_screen"]).read_bytes())
    assert result["primary_access_hold"] == audit.pointer("alias_screen", "primary_access_hold")
    assert discovery["primary_access_hold"]["http_status"] == 403


def test_cli_checks_both_outputs_before_writing(tmp_path, monkeypatch):
    prefix = str(tmp_path / "index")
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, [{"id": "test"}]))
    monkeypatch.setattr(sys, "argv", ["audit", "--check", "--output-prefix", prefix])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not list(tmp_path.iterdir())
    monkeypatch.setattr(sys, "argv", ["audit", "--output-prefix", prefix])
    Path(prefix + ".tsv").write_text("different\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert not Path(prefix + ".json").exists()
    Path(prefix + ".tsv").unlink()
    audit.main()
    audit.main()
    assert json.loads(Path(prefix + ".json").read_bytes()) == {"summary": {}}

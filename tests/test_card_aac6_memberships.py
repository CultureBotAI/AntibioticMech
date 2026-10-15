"""AAC6 reference additions preserve every record and do not become tested alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_aac6_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.shared.read_inputs(ROOT, audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def test_complete_projection_preserves_source_counts_and_unresolved_contexts(frozen):
    before = copy.deepcopy(frozen)
    result, rows = audit.project(*frozen)
    assert frozen == before
    data, _, _ = frozen
    assert len(rows) == len({r["identifier"] for r in rows}) == 2939
    assert len(result["terms"]) == 2002 and len(result["claims"]) == 4538
    summary = result["summary"]
    assert summary["selected_reference_terms"] == 1281
    assert summary["selected_reference_proteins"] == 1683 and summary["reference_links"] == 2798
    assert summary["records_with_selected_references"] == 223
    assert summary["term_statuses"][audit.UNSELECTED] == 721
    assert summary["claim_statuses"][audit.UNSELECTED] == 1281
    assert (summary["followup_terms"], summary["followup_claims"], summary["followup_records"]) == (
        15,
        70,
        12,
    )
    assert len(result["new_reference_memberships"]) == 10
    assert len({r["record_identifier"] for r in result["new_reference_memberships"]}) == 5
    assert sum(r["phi_claims_not_reassessed"] for r in rows) == 217
    assert sum(r["curator_claims_not_reassessed"] for r in rows) == 133
    assert sum(r["score_rules_not_reassessed"] for r in rows) == 467
    assert sum(r["card_assertions"] == 0 for r in rows) == 2666
    old_rows = {r["identifier"]: r for r in data["base_rows"]}
    for row in rows:
        assert sum(row[c] for c in audit.COLUMNS.values()) == row["card_assertions"]
        assert row["whole_record_primary_review"] == "OPEN"
        for field in (
            "phi_claims_not_reassessed",
            "curator_claims_not_reassessed",
            "score_rules_not_reassessed",
        ):
            assert row[field] == int(old_rows[row["identifier"]][field])
    assert result["limits"] == data["base"]["limits"]
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        assert {**new, "reference_status": old["reference_status"]} == old
        if old["aro_id"] not in audit.TERMS:
            assert old == new
    for tid, old in data["base"]["terms"].items():
        if tid not in data["aac6"]["terms"]:
            assert result["terms"][tid] == audit.rebase(old, "terms", tid)
        elif tid not in audit.TERMS:
            assert result["terms"][tid]["links"] == []
    for accession, old in data["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)
    assert result["primary_access_hold"] == audit.pointer("base", "primary_access_hold")
    assert result["aac6_primary_access_hold"] == audit.pointer("aac6", "primary_access_hold")


def test_every_evidence_pointer_resolves_in_its_own_input(frozen):
    data, _, _ = frozen
    result, _ = audit.project(*frozen)
    count = 0

    def visit(value):
        nonlocal count
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                node = data[value["input"]]
                if value["pointer"]:
                    assert value["pointer"].startswith("/")
                    for key in value["pointer"].split("/")[1:]:
                        key = key.replace("~1", "/").replace("~0", "~")
                        node = node[int(key)] if isinstance(node, list) else node[key]
                count += 1
            else:
                for node in value.values():
                    visit(node)
        elif isinstance(value, list):
            for node in value:
                visit(node)

    visit(result)
    assert count > 9000
    assert result["aac34_followup"] == {"input": "aac34", "pointer": ""}


@pytest.mark.parametrize("accession", ["UniProtKB:Q9AIK8", "UniProtKB:Q9AIK9"])
@pytest.mark.parametrize(
    "field,value",
    [
        ("gene_symbols", ["aacA29"]),
        ("reference_taxon_id", "NCBITaxon:562"),
        ("native_reference_taxon_rank", "strain"),
        ("experimental_subject_assignment", True),
        ("exact_allele_assignment", True),
        ("primary_results_reviewed", True),
        ("submission_name_is_expert_review", True),
        ("experimental_genome_assignment", "assigned"),
        ("explicit_card_xref", True),
        ("native_protein_flag", "Fragment"),
        ("entry_audit", {"entryVersion": 73, "sequenceVersion": True}),
    ],
)
def test_native_reference_scope_cannot_be_promoted(frozen, accession, field, value):
    row = copy.deepcopy(frozen[0]["aac6"]["references"][accession])
    row[field] = value
    with pytest.raises(ValueError):
        audit.reference_identity(accession, row)


@pytest.mark.parametrize("column", list(audit.prior.COLUMNS.values()))
def test_every_prior_status_column_including_bla_is_checked(inputs, column):
    inputs[0]["base_rows"][0][column] = str(int(inputs[0]["base_rows"][0][column]) + 1)
    with pytest.raises(ValueError, match="prior row"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change",
    [
        "lowercase_term",
        "claim",
        "record",
        "source_label",
        "definition",
        "membership",
        "duplicate_reference",
        "ambiguous_status",
        "hold_retry",
        "hold_primary",
        "old_accessions",
    ],
)
def test_membership_and_provenance_guards(inputs, change):
    data = inputs[0]
    dossier = data["aac6"]
    if change == "lowercase_term":
        dossier["terms"].pop("ARO:3007770")
    elif change == "claim":
        dossier["claims"].pop()
    elif change == "record":
        dossier["records"].pop()
    elif change == "source_label":
        dossier["terms"]["ARO:3002583"]["source_label"] = "AAC(6')-29"
    elif change == "definition":
        dossier["terms"]["ARO:3002583"]["definition_citation_ids"] = ["PMID:1"]
    elif change == "membership":
        dossier["reference_memberships"].pop()
    elif change == "duplicate_reference":
        data["base"]["proteins"]["UniProtKB:Q9AIK8"] = {}
    elif change == "ambiguous_status":
        dossier["terms"]["ARO:3002567"]["status"] = audit.aac6.EMPTY
    elif change == "hold_retry":
        dossier["primary_access_hold"]["retry_performed"] = True
    elif change == "hold_primary":
        dossier["primary_access_hold"]["primary_results_reviewed"] = True
    else:
        data["base_rows"][0]["selected_reference_accessions"] = "changed"
    with pytest.raises(ValueError):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "field,value",
    [
        ("exact_corpus_structure_assignment", "CHEBI:17630"),
        ("experimental_protein_assignment", "assigned"),
        ("experimental_genome_assignment", "assigned"),
        ("clinical_resistance_category", "R"),
        ("assay_host_species_taxon", "NCBITaxon:1120679"),
        ("source_isolate_native_rank", "strain"),
        ("native_isolate_MIC_inferred", True),
        ("assay_host_strain_assignment", "assigned"),
    ],
)
def test_primary_context_does_not_acquire_unresolved_identities(inputs, field, value):
    inputs[0]["aac6"]["aac34_primary_table_context"][field] = value
    with pytest.raises(ValueError, match="primary context"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "change", ["url", "count", "boolean_count", "absence", "global", "chemical", "all_article"]
)
def test_aac34_search_and_chemical_limits(frozen, change):
    data = copy.deepcopy(frozen[0]["aac34"])
    query = data["name_queries"]["reviewed"]
    if change == "url":
        query["source"]["url"] = audit.aac34.query_url(False)
    elif change == "count":
        query["result_count"] = 1
    elif change == "boolean_count":
        query["result_count"] = False
    elif change == "absence":
        query["biological_absence_inferred"] = True
    elif change == "global":
        data["limits"]["all_aliases_or_sources_searched"] = True
    elif change == "chemical":
        data["chemical_context"]["exact_corpus_structure_assignment"] = "CHEBI:17630"
    else:
        data["chemical_context"]["whole_article_or_supplement_identifier_absence_claimed"] = True
    with pytest.raises(ValueError):
        audit.check_aac34(data)


def test_saved_outputs_reproduce_without_native_request_caches(frozen, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "reports"), "request cache read"
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    current = audit.shared.read_inputs(ROOT, audit.PLAN)
    assert current == frozen
    result, rows = audit.project(*current)
    for suffix, body in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert Path(ROOT / (audit.PREFIX + suffix)).read_bytes() == body


def test_cli_checks_both_outputs_before_any_write(tmp_path, monkeypatch):
    prefix = str(tmp_path / "index")
    monkeypatch.setattr(audit, "build", lambda root: ({"summary": {}}, [{"id": "test"}]))
    monkeypatch.setattr(sys, "argv", ["audit", "--output-prefix", prefix, "--check"])
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

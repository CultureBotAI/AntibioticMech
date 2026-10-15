"""Reference-only nomenclature reconciliation preserves the full source corpus."""

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
import audit_card_aph_memberships as audit  # noqa: E402


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


def test_complete_index_preserves_claims_and_unresolved_contexts(frozen):
    before = copy.deepcopy(frozen)
    result, rows = audit.project(*frozen)
    assert frozen == before
    data, _, _ = frozen
    summary = result["summary"]
    assert len(rows) == len({r["identifier"] for r in rows}) == 2939
    assert len(result["claims"]) == 4538 and len(result["terms"]) == 2002
    assert (
        summary["selected_reference_terms"],
        summary["selected_reference_proteins"],
        summary["reference_links"],
        summary["records_with_selected_references"],
    ) == (1282, 1684, 2799, 223)
    assert summary["term_statuses"][audit.UNSELECTED] == 720
    assert summary["claim_statuses"][audit.UNSELECTED] == 1277
    assert (summary["followup_terms"], summary["followup_claims"], summary["followup_records"]) == (
        14,
        38,
        16,
    )
    assert summary["added_reference_memberships"] == len(result["new_reference_memberships"]) == 4
    assert summary["additional_evidence_for_existing_links"] == 0
    assert summary["whole_record_primary_signoffs"] == 0
    assert result["limits"] == data["base"]["limits"]
    assert sum(row["phi_claims_not_reassessed"] for row in rows) == 217
    assert sum(row["curator_claims_not_reassessed"] for row in rows) == 133
    assert sum(row["score_rules_not_reassessed"] for row in rows) == 467
    assert sum(row["card_assertions"] == 0 for row in rows) == 2666
    old_rows = {r["identifier"]: r for r in data["base_rows"]}
    for row in rows:
        assert sum(row[c] for c in audit.COLUMNS.values()) == row["card_assertions"]
        assert row["whole_record_primary_review"] == "OPEN"
        for column in (
            "phi_claims_not_reassessed",
            "curator_claims_not_reassessed",
            "score_rules_not_reassessed",
        ):
            assert row[column] == int(old_rows[row["identifier"]][column])
    for old, new in zip(data["base"]["claims"], result["claims"], strict=True):
        assert {**new, "reference_status": old["reference_status"]} == old
        if old["aro_id"] != audit.gaps.TERM:
            assert old == new
    for tid, old in data["base"]["terms"].items():
        if tid not in data["gaps"]["terms"]:
            assert result["terms"][tid] == audit.rebase(old, "terms", tid)
        elif tid != audit.gaps.TERM:
            assert result["terms"][tid]["links"] == []
            assert result["terms"][tid]["reference_status"] == audit.UNSELECTED
    for accession, old in data["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)
    for field in (
        "primary_access_hold",
        "aac6_primary_access_hold",
        "aac34_followup",
        "sco1_reference_context",
    ):
        assert result[field] == audit.pointer("base", field)
    assert result["aph_historical_access_limitations"] == audit.pointer(
        "gaps", "inherited_access_limitations"
    )


def test_all_evidence_pointers_remain_owned_and_resolvable(frozen):
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
    assert result["aph_ant_aad_mph_followup"] == {"input": "gaps", "pointer": ""}


@pytest.mark.parametrize(
    "field,value",
    [
        ("gene_symbols", ["aph"]),
        ("entry_type", "UniProtKB reviewed (Swiss-Prot)"),
        ("entry_audit", {"entryVersion": 113, "sequenceVersion": True}),
        ("experimental_subject_assignment", True),
        ("exact_allele_assignment", True),
        ("experimental_genome_assignment", "assigned"),
        ("explicit_card_xref", True),
        ("submission_name_is_expert_review", True),
        ("native_protein_flag", "Fragment"),
        ("unflagged_means_complete", True),
        ("new_primary_results_review", True),
        ("nomenclature_primary_text_replayed_here", True),
        ("source_citation", "PMID:1"),
    ],
)
def test_reference_identity_and_limits_cannot_be_promoted(frozen, field, value):
    row = copy.deepcopy(frozen[0]["gaps"]["references"][audit.gaps.ACCESSION])
    row[field] = value
    with pytest.raises(ValueError):
        audit.reference_identity(row)


@pytest.mark.parametrize(
    "field,value",
    [
        ("taxon_id", "NCBITaxon:562"),
        ("scientific_name", "Escherichia coli"),
        ("native_rank", "strain"),
        ("active", False),
        ("experimental_subject_assignment", True),
        ("strain_label_in_name_changes_rank", True),
    ],
)
def test_reference_taxonomy_remains_the_active_reference_species(frozen, field, value):
    row = copy.deepcopy(frozen[0]["gaps"]["references"][audit.gaps.ACCESSION])
    row["reference_taxonomy"][field] = value
    with pytest.raises(ValueError):
        audit.reference_identity(row)


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_name", "other"),
        ("revised_name", "other"),
        ("reference", "PMID:1"),
        ("doi", "10.1000/other"),
        ("review_medium", "FULL_TEXT_NATIVE_REPLAY"),
        ("native_primary_file_cached", True),
        ("table_5_visually_inspected", True),
        ("whole_paper_review_complete", True),
    ],
)
def test_historical_nomenclature_limits_remain_explicit(frozen, field, value):
    row = copy.deepcopy(frozen[0]["gaps"]["references"][audit.gaps.ACCESSION])
    row["historical_nomenclature_review"][field] = value
    with pytest.raises(ValueError):
        audit.reference_identity(row)


@pytest.mark.parametrize("column", list(audit.prior.COLUMNS.values()))
def test_all_prior_columns_including_aac6_are_checked(inputs, column):
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
        "candidate",
        "duplicate_reference",
        "empty_status",
        "query_count",
        "query_absence",
        "query_scope",
        "record_accessions",
        "dossier_limit",
        "query_pool",
        "new_reference_scope",
        "literal_match",
        "term_biological_absence",
    ],
)
def test_cohort_memberships_and_dispositions_fail_closed(inputs, change):
    data = inputs[0]
    dossier = data["gaps"]
    term = dossier["terms"][audit.gaps.TERM]
    if change == "lowercase_term":
        dossier["terms"].pop("ARO:3007669")
    elif change == "claim":
        dossier["claims"].pop()
    elif change == "record":
        dossier["records"].pop()
    elif change == "source_label":
        term["source_label"] = "APH"
    elif change == "definition":
        term["definition_citation_ids"] = ["PMID:1"]
    elif change == "membership":
        dossier["reference_memberships"].pop()
    elif change == "candidate":
        dossier["terms"]["ARO:3007669"]["reference_candidates"] = [audit.gaps.ACCESSION]
    elif change == "duplicate_reference":
        data["base"]["proteins"][audit.gaps.ACCESSION] = {}
    elif change == "empty_status":
        dossier["terms"]["ARO:3004675"]["status"] = audit.gaps.EMPTY
    elif change in {"query_count", "query_absence", "query_scope"}:
        query = dossier["citation_queries"]["9593155"]
        query[
            {
                "query_count": "result_count",
                "query_absence": "establishes_biological_absence",
                "query_scope": "query",
            }[change]
        ] = {"query_count": True, "query_absence": True, "query_scope": "other"}[change]
    elif change == "record_accessions":
        data["base_rows"][0]["selected_reference_accessions"] = "changed"
    elif change == "dossier_limit":
        dossier["limits"]["all_aliases_or_sources_searched"] = True
    elif change == "query_pool":
        term["complete_citation_query_accessions"].append("UniProtKB:OTHER")
    elif change == "new_reference_scope":
        dossier["reference_memberships"][0]["experimental_subject_assignment"] = True
    elif change == "literal_match":
        term["literal_name_match_found"] = True
    else:
        term["biological_absence_inferred"] = True
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_saved_projection_equals_both_outputs_without_request_caches(frozen, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "reports"), "request-cache read forbidden"
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result, rows = audit.project(*frozen)
    for suffix, body in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == body


def test_published_output_and_plan_bytes_match_verification():
    receipt = json.loads((ROOT / (audit.PREFIX + "-verification.json")).read_bytes())
    pins = [p for p in receipt["files"] if p["path"].startswith(audit.PREFIX)]
    assert len(pins) == 3
    assert {p["path"] for p in pins} == {audit.PREFIX + s for s in (".json", ".tsv", "-plan.json")}
    for pin in pins:
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]


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

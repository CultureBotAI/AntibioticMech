"""Keep reference-only follow-ups scoped while retaining every corpus row."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_followup_memberships as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.shared.read_inputs(ROOT, audit.PLAN)


@pytest.fixture
def inputs(frozen):
    return copy.deepcopy(frozen)


def resolve(data, pointer):
    value = data[pointer["input"]]
    for part in pointer["pointer"].split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def test_complete_partition_and_exact_reference_delta(frozen):
    result, rows = audit.project(*frozen)
    expected = {
        "corpus_records": 2939,
        "card_terms": 2002,
        "card_assertions": 4538,
        "selected_reference_terms": 1276,
        "selected_reference_proteins": 1677,
        "reference_links": 2792,
        "records_with_selected_references": 223,
        "added_reference_terms": 1,
        "added_reference_proteins": 1,
        "added_reference_links": 1,
        "added_reference_memberships": 9,
        "followup_terms": 11,
        "followup_claims": 94,
        "whole_record_primary_signoffs": 0,
    }
    assert {k: result["summary"][k] for k in expected} == expected
    assert result["summary"]["term_statuses"][audit.UNSELECTED] == 726
    assert result["summary"]["claim_statuses"][audit.UNSELECTED] == 1304
    assert result["summary"]["claim_statuses"][audit.IIIB] == 9
    assert len(rows) == 2939
    assert all(sum(row[col] for col in audit.COLUMNS.values()) == row["card_assertions"] for row in rows)
    assert all(row["whole_record_primary_review"] == "OPEN" for row in rows)
    assert sum(row["phi_claims_not_reassessed"] for row in rows) == 217
    assert sum(row["curator_claims_not_reassessed"] for row in rows) == 133
    assert sum(row["score_rules_not_reassessed"] for row in rows) == 467
    assert set(result["proteins"]) - set(frozen[0]["base"]["proteins"]) == {audit.ACCESSION}
    old_rows = {r["identifier"]: r for r in frozen[0]["base_rows"]}
    changed = {
        r["identifier"]
        for r in rows
        if r["selected_reference_accessions"] != old_rows[r["identifier"]]["selected_reference_accessions"]
    }
    assert changed == set(frozen[0]["base"]["terms"][audit.TERM]["record_memberships"])
    assert all(
        len(t["links"]) == len({r["protein_accession"] for r in t["links"]}) for t in result["terms"].values()
    )


def test_inputs_unchanged_and_inherited_context_resolves(inputs):
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
    assert result["limits"] == inputs[0]["base"]["limits"]
    for tid, old in inputs[0]["base"]["terms"].items():
        if tid == audit.TERM:
            continue
        new = result["terms"][tid]
        expected = audit.rebase(old, "terms", tid)
        if not old["links"]:
            expected["reference_status"] = audit.UNSELECTED
        assert {k: v for k, v in new.items() if not k.endswith("_evidence_followup")} == expected
    for accession, old in inputs[0]["base"]["proteins"].items():
        assert result["proteins"][accession] == audit.rebase(old, "proteins", accession)


def test_related_proteins_and_primary_holds_do_not_assign_experiments(frozen):
    result, _ = audit.project(*frozen)
    contexts = {name: resolve(frozen[0], p) for name, p in result["evidence_followups"].items()}
    assert contexts == {name: frozen[0][name] for name in audit.FOLLOWUPS}
    assert contexts["cipa"]["primary_access_hold"]["http_status"] == 403
    assert contexts["aac3"]["disposition"]["generic_type_iv_is_exact_iva"] is False
    assert result["terms"]["ARO:3002539"]["links"] == frozen[0]["base"]["terms"]["ARO:3002539"]["links"] == []
    for tid in ("ARO:3004585", "ARO:3004598", "ARO:3003907", "ARO:3001307", "ARO:3003990"):
        assert result["terms"][tid]["links"] == []
    protein = result["proteins"][audit.ACCESSION]
    assert protein["identity"]["reference_species_taxon_id"] == "NCBITaxon:287"
    assert protein["exact_allele_assignment"] is protein["experimental_subject_assignment"] is False
    link = result["terms"][audit.TERM]["links"][0]
    assert link["source_citation_ids"] == link["matched_reference_numbers"] == []
    assert link["explicit_card_xref"] is False
    source = resolve(frozen[0], link["source"])
    assert source["native_citation_ids"] == ["PMID:30347146"]
    assert source["aro_own_citation_in_native_bibliography"] is False


@pytest.mark.parametrize("name", audit.FOLLOWUPS)
@pytest.mark.parametrize("change", ["claim_hash", "claim_position", "missing_claim", "record"])
def test_followups_must_cover_live_membership(inputs, name, change):
    d = inputs[0][name]
    if change == "claim_hash":
        d["claims"][0]["claim_sha256"] = "changed"
    elif change == "claim_position":
        d["claims"][0]["position"] = -1
    elif change == "missing_claim":
        d["claims"].pop()
    else:
        d["records"].pop()
    with pytest.raises(ValueError, match="follow-up"):
        audit.project(*inputs)


@pytest.mark.parametrize(
    "field,value",
    [
        ("entry_type", "UniProtKB reviewed (Swiss-Prot)"),
        ("entry_audit", {"entryVersion": 62, "sequenceVersion": 1}),
        ("reference_taxon_id", "NCBITaxon:1"),
        ("native_reference_taxon_rank", "strain"),
        ("gene_symbols", ["aac(3)-IV"]),
        ("explicit_card_xref", True),
        ("experimental_allele_assignment", "inferred"),
        ("experimental_subject_assignment", True),
        ("aro_cited_tested_enzyme_equated_with_reference", True),
        ("native_citation_ids", ["PMID:20387903"]),
    ],
)
def test_reference_identity_cannot_be_promoted(inputs, field, value):
    inputs[0]["aac3"]["new_iiib_gene_reference"][field] = value
    with pytest.raises(ValueError, match="IIIb reference identity"):
        audit.project(*inputs)


@pytest.mark.parametrize("change", ["membership", "duplicate", "query", "source", "limits", "old_accessions"])
def test_reconciliation_guards(inputs, change):
    data, plan, _ = inputs
    if change == "membership":
        data["aac3"]["new_gene_reference_memberships"].pop()
    elif change == "duplicate":
        data["base"]["proteins"][audit.ACCESSION] = {}
    elif change == "query":
        data["aac3"]["iiib_exact_label_queries"]["iiib-reviewed"]["result_count"] = 1
    elif change == "source":
        plan["inputs"]["source_inventory"] = {"path": "other", "sha256": "changed"}
    elif change == "limits":
        data["base"]["limits"]["ncbi_requests"] = 1
    else:
        data["base_rows"][0]["selected_reference_accessions"] = audit.ACCESSION
    with pytest.raises(ValueError):
        audit.project(*inputs)


def test_saved_outputs_reproduce_without_request_caches(frozen):
    result, rows = audit.project(*frozen)
    for suffix, body in zip((".json", ".tsv"), audit.registry.render(result, rows), strict=True):
        assert (ROOT / (audit.PREFIX + suffix)).read_bytes() == body


def test_cli_checks_pair_before_writing(tmp_path, monkeypatch):
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

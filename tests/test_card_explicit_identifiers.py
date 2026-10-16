"""Identifier and locus aliases support reference context, not resistant alleles."""

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
import audit_card_explicit_identifiers as audit  # noqa: E402

SPECIES = {"taxonId": 5476, "rank": "species", "scientificName": "Candida albicans"}


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline identifier audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def entry():
    return {
        "primaryAccession": "REFERENCE",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "genes": [
            {
                "geneName": {"value": "shared"},
                "orderedLocusNames": [{"value": "locus"}],
                "orfNames": [{"value": "orf"}],
            }
        ],
        "uniProtKBCrossReferences": [{"database": "CGD", "id": "CAL1"}],
    }


@pytest.mark.parametrize("namespace", ["primary", "secondary", "locus"])
@pytest.mark.parametrize(
    "state", ["matching", "wrong_species", "missing_taxonomy", "inactive", "absent_field"]
)
def test_source_identifier_requires_native_field_active_state_and_species(namespace, state):
    e = entry()
    e["secondaryAccessions"] = ["SECONDARY"]
    lead = {
        "kind": "ORDERED_LOCUS" if namespace == "locus" else "ACCESSION_LIKE_SYNONYM",
        "value": {"primary": "REFERENCE", "secondary": "SECONDARY", "locus": "locus"}[namespace],
    }
    species = SPECIES
    if state == "wrong_species":
        species = {**SPECIES, "taxonId": 1}
    elif state == "missing_taxonomy":
        species = None
    elif state == "inactive":
        e["entryType"] = "Inactive"
    elif state == "absent_field":
        lead["value"] = "unrepresented"
    result = audit.source_candidate(e, [lead], SPECIES, species, "different-source-gene")
    assert result["qualified_reference"] is (state == "matching")
    assert result["native_source_gene_name_matches"] == []
    assert result["experimental_subject_assignment"] is result["exact_allele_assignment"] is False
    assert result["primary_resistance_validation"] is False


def test_ordered_locus_cannot_be_satisfied_by_same_gene_symbol():
    e = entry()
    result = audit.source_candidate(
        e, [{"kind": "ORDERED_LOCUS", "value": "shared"}], SPECIES, SPECIES, "shared"
    )
    assert result["native_source_gene_name_matches"]
    assert result["alias_matches"] == []
    assert result["qualified_reference"] is False


def test_inactive_accessions_do_not_gain_species_or_replacement_identity():
    e = {
        "primaryAccession": "DELETED",
        "entryType": "Inactive",
        "inactiveReason": {"inactiveReasonType": "DELETED"},
    }
    result = audit.inactive_reference(e)
    assert result["native_inactive_reason"] == e["inactiveReason"]
    assert result["organism_inferred_from_source_label"] is False
    assert result["replacement_accession_inferred"] is False
    assert result["qualified_reference"] is False
    assert result["biological_absence_inferred"] is False


@pytest.mark.parametrize("field", ["sequence", "features", "comments"])
def test_inactive_projection_rejects_operational_payload(field):
    with pytest.raises(ValueError, match="operational"):
        audit.inactive_reference({"entryType": "Inactive", field: []})


@pytest.mark.parametrize(
    "state,status",
    [
        ("matching", "SAME_CGD_FEATURE_REFERENCE_NOT_EXPERIMENTAL_HAPLOTYPE"),
        ("no_xref", "CGD_ALIAS_ONLY_REFERENCE_NOT_PAPER_SUBJECT"),
        ("different_xref", "CONFLICTING_CGD_FEATURE_WITHHELD"),
        ("multiple_xrefs", "CONFLICTING_CGD_FEATURE_WITHHELD"),
        ("missing_alias", "NO_EXACT_NATIVE_ALIAS_WITHHELD"),
        ("wrong_species", "SPECIES_UNRESOLVED_OR_DIFFERENT_WITHHELD"),
        ("missing_species", "SPECIES_UNRESOLVED_OR_DIFFERENT_WITHHELD"),
    ],
)
def test_cgd_feature_and_alias_identity_do_not_assign_experimental_haplotype(state, status):
    e, species, values = entry(), SPECIES, ["locus", "orf"]
    if state == "no_xref":
        e["uniProtKBCrossReferences"] = []
    elif state == "different_xref":
        e["uniProtKBCrossReferences"][0]["id"] = "CAL2"
    elif state == "multiple_xrefs":
        e["uniProtKBCrossReferences"].append({"database": "CGD", "id": "CAL2"})
    elif state == "missing_alias":
        values = ["unrepresented"]
    elif state == "wrong_species":
        species = {**SPECIES, "taxonId": 1}
    elif state == "missing_species":
        species = None
    result = audit.cgd_candidate(e, {"cgd_id": "CAL1"}, species, SPECIES, values)
    assert result["status"] == status
    assert result["same_cgd_feature_verified"] is (state == "matching")
    assert result["experimental_haplotype_assignment"] is result["exact_allele_assignment"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["experimental_genome_assignment"] is None


def test_native_orf_namespace_is_not_collapsed_to_gene_name():
    result = audit.locus_alias_matches(entry(), ["orf"])
    assert result == [
        {"source_alias": "orf", "native_fields": [{"field": "genes/0/orfNames/0", "value": "orf"}]}
    ]


@pytest.mark.parametrize("mutation", ["attempt", "receipt", "body", "error", "missing_receipt"])
def test_unaccounted_or_missing_request_artifacts_fail_closed(tmp_path, mutation):
    for key in ("query", "taxonomy-294748"):
        for suffix in ("attempt", "receipt"):
            (tmp_path / f"{key}-{suffix}.json").write_text("{}")
    (tmp_path / "query-body.json").write_text("{}")
    audit.check_request_history(tmp_path, {"query"})
    if mutation == "missing_receipt":
        (tmp_path / "query-receipt.json").unlink()
    else:
        (tmp_path / f"unexpected-{mutation}.json").write_text("{}")
    with pytest.raises(ValueError, match="unaccounted"):
        audit.check_request_history(tmp_path, {"query"})


@pytest.mark.parametrize("entry_type", ["UniProtKB unreviewed (TrEMBL)", "Inactive", "unknown"])
def test_reviewed_query_cannot_accept_other_native_entry_states(entry_type):
    with pytest.raises(ValueError):
        audit.check_entry_scope("source-locus", {"example": {"entryType": entry_type}})


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_scope_and_counts_preserve_inactive_and_distinct_feature_holds():
    d = saved()
    assert d["summary"]["combined_qualified_terms"] == 104
    assert d["summary"]["combined_remaining_terms"] == 74
    assert d["summary"]["complete_records_read"] == d["summary"]["source_claims"] == 10
    assert d["coverage"]["new_qualified_terms"] == ["ARO:3004977"]
    assert d["terms"]["ARO:3004578"]["qualified_reference_accessions"] == []
    assert d["terms"]["ARO:3004977"]["qualified_reference_accessions"] == ["UniProtKB:P9WI57"]
    assert set(d["inactive_accessions"]) == {"A0A225SC95", "Q2FD57"}
    assert d["retained_name_only_reference_disagreement"]["status"] == "DISTINCT_CGD_FEATURES_WITHHELD"
    assert [c["protein_accession"] for c in d["cgd_alias_candidates"] if c["same_cgd_feature_verified"]] == [
        "UniProtKB:A0A1D8PLT0"
    ]
    assert d["additional_context_term"]["additional_qualified_card_terms"] == 0
    assert d["reused_exact_locus_query"]["result_count"] == 0
    assert d["summary"]["ncbi_requests"] == d["summary"]["biological_record_writes"] == 0


def test_offline_native_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    if not (ROOT / d["inputs"]["protein_canary"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable artifact checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


def test_query_scope_retains_secondary_fields_no_taxon_prefilter_and_reviewed_locus():
    p = json.loads((ROOT / (audit.PREFIX + "-plan.json")).read_bytes())
    result = audit.expected_queries(p)
    assert "sec_acc:" in result["source-accessions"]
    assert "taxonomy_id:" not in result["source-accessions"]
    assert result["source-locus"].endswith("reviewed:true")
    assert "gene_exact:AIF1" not in result["cgd-paper-locus-aliases"]
    changed = copy.deepcopy(p)
    changed["source_locus_lead"] = "different"
    with pytest.raises(ValueError, match="source locus changed"):
        audit.expected_queries(changed)


def test_cli_creates_nested_output_but_never_overwrites_different_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_never_creates_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "absent" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()

"""Source conflicts and reference names must not become experimental identities."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_name_holds as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline name-hold audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.mark.parametrize(
    "gene,definition,conflict",
    [
        ("Mdr3", "The Mdr2 gene is responsible for a function.", True),
        ("MDR3", "The Mdr2 gene is responsible for a function.", True),
        ("Mdr2", "The Mdr2 gene is responsible for a function.", False),
        ("Mdr3", "The Mdr gene is responsible for a function.", False),
        ("Mdr3", "This sentence mentions Mdr2.", False),
        ("Mdr3", "The Mdr3 gene is responsible for a function.", False),
    ],
)
def test_scoped_gene_conflict_is_not_a_correction_or_family_inference(gene, definition, conflict):
    result = audit.source_gene_conflict(gene, definition)
    assert bool(result) == conflict
    if result:
        assert result["definition_sha256"] == hashlib.sha256(definition.encode()).hexdigest()
        assert result["correct_gene_inferred"] is False


def wrapper(body, filename):
    return {
        "body": body,
        "url": audit.CGD_BASE + filename,
        "status": 200,
        "bytes": len(body.encode()),
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
    }


def cgd_fixture():
    mapping = "ORF19_ID\tASSEMBLY22_ID\tGENE_NAME\norf19.3362\tC4_03350C_A\tAIF1\norf19.9721\tC2_08100W_A\t\n"
    rows = [
        ["C4_03350C_A", "AIF1", "orf19.3362", "ORF|Uncharacterized", "", "", "", "", "CAL0000191273", "", ""],
        ["C2_08100W_A", "", "orf19.9721|AIF1", "ORF|Verified", "", "", "", "", "CAL0000195769", "", ""],
    ]
    features = "! Genome version: A22-s08-m01-r37\n" + "\n".join("\t".join(r) for r in rows) + "\n"
    return wrapper(mapping, "ORF19_Assembly22_mapping.tab"), wrapper(
        features, "C_albicans_SC5314_version_A22-s08-m01-r37_chromosomal_feature.tab"
    )


def test_cgd_preserves_two_distinct_features_sharing_gene_name():
    result = audit.cgd_loci(*cgd_fixture())
    assert result["orf19.3362"]["feature"] != result["orf19.9721"]["feature"]
    assert result["orf19.3362"]["feature_primary_gene_name"] == "AIF1"
    assert result["orf19.9721"]["feature_primary_gene_name"] is None
    assert "AIF1" in result["orf19.9721"]["feature_aliases"]


@pytest.mark.parametrize(
    "mutation",
    [
        "url",
        "checksum",
        "header",
        "version",
        "duplicate_mapping",
        "duplicate_feature",
        "wrong_feature",
        "wrong_id",
        "missing_locus_alias",
        "changed_gene",
    ],
)
def test_cgd_identity_joins_fail_closed(mutation):
    mapping, features = cgd_fixture()
    if mutation == "url":
        mapping["url"] += "?other"
    elif mutation == "checksum":
        mapping["sha256"] = "0" * 64
    else:
        if mutation == "header":
            mapping["body"] = mapping["body"].replace("ORF19_ID", "ALIAS")
        elif mutation == "version":
            features["body"] = features["body"].replace("r37", "r38")
        elif mutation == "duplicate_mapping":
            mapping["body"] += mapping["body"].splitlines()[1] + "\n"
        elif mutation == "duplicate_feature":
            features["body"] += features["body"].splitlines()[1] + "\n"
        elif mutation == "wrong_feature":
            mapping["body"] = mapping["body"].replace("C4_03350C_A", "C2_08100W_A")
        elif mutation == "wrong_id":
            features["body"] = features["body"].replace("CAL0000191273", "CAL0000195769")
        elif mutation == "missing_locus_alias":
            features["body"] = features["body"].replace("orf19.3362", "orf19.3363")
        elif mutation == "changed_gene":
            features["body"] = features["body"].replace("\tAIF1\t", "\tDIFFERENT\t")
        for w in (mapping, features):
            w["sha256"] = hashlib.sha256(w["body"].encode()).hexdigest()
            w["bytes"] = len(w["body"].encode())
    with pytest.raises(ValueError):
        audit.cgd_loci(mapping, features)


@pytest.mark.parametrize("reference_loci", [["orf19.9721"], ["orf19.3362"], ["unmapped"]])
def test_even_matching_reference_locus_does_not_prove_experimental_identity(reference_loci):
    result = audit.paper_locus_assignment(reference_loci, "orf19.3362", audit.cgd_loci(*cgd_fixture()))
    assert result["experimental_protein_assignment"] is False
    assert result["gene_name_match_overrides_locus_disagreement"] is False
    assert (result["status"] == "DISTINCT_CGD_FEATURES_WITHHELD") == (reference_loci == ["orf19.9721"])


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_primary_context_does_not_resolve_source_spelling_or_locus_conflict():
    d = saved()
    s = d["summary"]
    assert (s["remaining_name_unresolved_terms"], s["source_gene_conflict_terms"]) == (31, 5)
    assert (s["complete_records_read"], s["source_claims"]) == (18, 34)
    assert s["new_qualified_source_term_references"] == 0
    assert (s["new_reference_entries"], s["reused_name_references"]) == (1, 1)
    assert d["primary_review"]["local_attempts"] == 2
    assert d["primary_review"]["local_dns_failure_retried"] is True
    assert d["primary_review"]["source_http_denial_bypassed"] is False
    assert d["candida_locus_disagreement"]["status"] == "DISTINCT_CGD_FEATURES_WITHHELD"
    assert d["reference_queries"]["candida-paper-locus"]["result_count"] == 0
    assert d["retained_nomenclature_access_hold"]["source"]["status"] == 302
    assert all(r["name_disposition"] == "UNRESOLVED_NO_CORRECTION_INFERRED" for r in d["terms"].values())
    previous = json.loads((ROOT / d["inputs"]["prior"]["path"]).read_bytes())
    assert all(r["prior_assessment"] == previous["terms"][t] for t, r in d["terms"].items())


@pytest.mark.parametrize(
    "field",
    [
        "numeric_ast_exported",
        "exact_structure_match_to_neutral_record",
        "source_spelling_correction_inferred",
        "experimental_reference_protein_assignment",
        "experimental_allele_assignment",
        "experimental_strain_taxon_or_genome_assignment",
        "whole_record_primary_signoff",
        "negative_control_inferred_globally_ineffective",
    ],
)
def test_primary_assessment_cannot_be_promoted_past_reviewed_scope(field):
    assessment = copy.deepcopy(saved()["primary_review"])
    assessment[field] = True
    with pytest.raises(ValueError, match="primary review scope changed"):
        audit.primary_review(ROOT, {}, {"primary_assessment": assessment})


def test_offline_native_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    if not (ROOT / d["primary_review"]["source"]["path"]).exists():
        pytest.skip("ignored primary source unavailable; portable checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


def test_cli_nested_output_and_preserved_existing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_never_creates_missing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "absent" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()

"""ORF-name matching must not rewrite a historical deletion or its phenotype."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_fr171456_locus as audit  # noqa: E402


def reference_inputs():
    entry = {"primaryAccession": "O13585", "entryType": "UniProtKB reviewed (Swiss-Prot)",
             "entryAudit": {"entryVersion": 162, "sequenceVersion": 2},
             "genes": [{"orderedLocusNames": [{"value": "YPR089W"}],
                        "orfNames": [{"value": "YPR090W"}]}],
             "organism": {"taxonId": 559292}, "references": []}
    species = {"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae",
               "rank": "species", "active": True}
    strain = {"taxonId": 559292, "scientificName": "S288c reference", "rank": "strain", "active": True,
              "lineage": [copy.deepcopy(species)]}
    return entry, strain, species


def test_orf_name_and_ordered_locus_name_are_not_interchangeable():
    result = audit.project_reference(*reference_inputs())
    assert result["ordered_locus_names"] == ["YPR089W"]
    assert result["orf_names"] == ["YPR090W"]
    assert result["gene_symbol"] is None
    assert result["matched_source_label_role"] == "ORF_NAME_NOT_ORDERED_LOCUS_NAME"
    for field in ("experimental_deletion_identity_established", "exact_allele_assignment",
                  "resistance_effect_assigned", "annotation_change_history_inferred"):
        assert result[field] is False


@pytest.mark.parametrize("change", ["accession", "entry_version", "sequence_version", "sequence",
                                    "unreviewed", "role_swap", "extra_gene", "gene_symbol",
                                    "strain_id", "species_id", "species_rank", "inactive", "lineage"])
def test_reference_identity_and_annotation_roles_fail_closed(change):
    entry, strain, species = reference_inputs()
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "entry_version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "sequence":
        entry["sequence"] = {}
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "role_swap":
        entry["genes"][0] = {"orderedLocusNames": [{"value": "YPR090W"}],
                             "orfNames": [{"value": "YPR089W"}]}
    elif change == "extra_gene":
        entry["genes"] *= 2
    elif change == "gene_symbol":
        entry["genes"][0]["geneName"] = {"value": "YPR090W"}
    elif change == "strain_id":
        strain["taxonId"] = 4932
    elif change == "species_id":
        species["taxonId"] = 559292
    elif change == "species_rank":
        species["rank"] = "no rank"
    elif change == "inactive":
        strain["active"] = False
    else:
        strain["lineage"] *= 2
    with pytest.raises(ValueError):
        audit.project_reference(entry, strain, species)


def test_empty_query_does_not_promote_suggestions_to_results_or_absence():
    result = audit.query_projection({"results": [], "suggestions": [{"query": "other", "hits": 1}]})
    assert result["result_count"] == 0 and result["suggested_queries_not_selected"] == 1
    assert result["complete_for_query"]
    assert not result["suggestions_are_results"] and not result["zero_results_establish_absence"]


def test_unreviewed_primary_payload_rejected():
    with pytest.raises(ValueError, match="inspected payload"):
        audit.primary_context(b"YPR090w YPL090w hypersensitivity")


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_source_conflict_and_primary_scope_remain_explicit(dossier):
    primary = dossier["primary"]
    assert primary["source_locus_labels"] == ["YPR090w", "YPL090w"]
    assert primary["figure_locus_label"] == "YPR090w"
    assert primary["figure_2_panels_reviewed"] == ["c", "d"]
    assert primary["native_figure_visually_reviewed_this_checkpoint"]
    assert not primary["source_conflict_resolved"] and not primary["source_typo_corrected"]
    assert primary["effect_context"] == "SOURCE_REPORTED_HYPERSENSITIVITY_NOT_A_NEW_RESISTANCE_CLAIM"
    assert not primary["cited_background_paper"]["primary_results_reviewed_here"]


def test_public_reference_is_not_an_experimental_allele_or_primary_confirmation(dossier):
    protein = dossier["reference_protein"]
    assert protein["accession"] == "UniProtKB:O13585"
    assert protein["entry_version"] == 162 and protein["sequence_version"] == 2
    assert protein["ordered_locus_names"] == ["YPR089W"] and protein["orf_names"] == ["YPR090W"]
    assert not protein["focal_paper_cited"] and not protein["experimental_deletion_identity_established"]
    assert dossier["queries"]["YPR090W"]["result_count"] == 1
    assert dossier["queries"]["YPL090W"]["result_count"] == 0
    assert dossier["queries"]["YPL090W"]["suggested_queries_not_selected"] == 5
    assert dossier["summary"]["biological_record_changes"] == 0
    assert dossier["constraints"]["ncbi_requests"] == 0
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert dossier["constraints"]["full_corpus_goal_status"] == "OPEN"


def test_offline_native_replay(dossier, monkeypatch, capsys, pre_card_qualification_root):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline locus audit attempted a network request")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.chdir(pre_card_qualification_root)
    monkeypatch.setattr(sys, "argv", [audit.__name__, "--check", "--historical-records"])
    audit.main()
    assert json.loads(capsys.readouterr().out) == dossier["summary"]

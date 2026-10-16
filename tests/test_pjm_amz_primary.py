"""Guard source identity, experimental scope and the publisher access hold."""

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
import audit_pjm_amz_primary as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline primary audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture
def checkpoint():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_complete_membership_scope(checkpoint):
    assert checkpoint["summary"] == {
        "current_record_hashes_verified": 2939,
        "complete_target_records_read": 7,
        "source_claims_bound": 10,
        "terms_investigated": 2,
        "species_names_grounded": 2,
        "new_selected_proteins": 0,
        "native_primary_access_holds": 1,
        "whole_record_primary_signoffs": 0,
    }
    index = audit.read_json(ROOT, checkpoint["inputs"]["current_index"])
    for term, row in checkpoint["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert (
            sorted(c["record_identifier"] for c in checkpoint["claims"] if c["aro_id"] == term)
            == row["record_memberships"]
        )
        assert row["reference_accessions"] == []
        assert row["experimental_allele_assignment"] is None
        assert row["experimental_protein_assignment"] is None
        assert row["experimental_genome_assignment"] is None
        assert row["biological_absence_inferred"] is False
        assert row["whole_record_primary_review"] == "OPEN"
    assert checkpoint["constraints"]["ncbi_requests"] == 0
    assert checkpoint["constraints"]["issue_1040"] == "DEFERRED"
    assert checkpoint["constraints"]["full_investigation_complete"] is False


@pytest.mark.parametrize(
    "term,taxid,comparison_name",
    [("ARO:3007694", "NCBITaxon:1389922", "LMG 26685"), ("ARO:3007374", "NCBITaxon:69284", "DSM 17109")],
)
def test_native_species_aliases_are_not_experimental_strain_ids(checkpoint, term, taxid, comparison_name):
    context = checkpoint["terms"][term]["taxonomy_context"]
    assert context["source_name_match"]["taxon_id"] == taxid
    assert context["source_name_match"]["rank"] == "species"
    assert comparison_name in context["native_other_names_not_strain_mappings"]
    assert context["experimental_taxon_assignment"] is None
    assert context["experimental_strain_taxon_assignment"] is None
    assert context["species_name_implies_resistance"] is False


def test_empty_queries_keep_suggestions_unselected(checkpoint):
    for key in ("amz-protein", "pjm-protein"):
        assert checkpoint["requests"][key]["complete_result_count"] == 0
        assert checkpoint["requests"][key]["release"] == "2026_03"
    assert len(checkpoint["requests"]["amz-protein"]["suggestions_not_selected"]) == 3


def test_primary_access_strength_is_not_conflated(checkpoint):
    amz, pjm = (checkpoint["terms"][t] for t in ("ARO:3007694", "ARO:3007374"))
    assert amz["primary_review"]["ampicillin_cellular_and_biochemical_results_discordant"] is True
    assert amz["primary_review"]["source_identifiers"] == {
        "chromosome": "CP123364",
        "gene_nucleotide": "OQ948417",
    }
    assert amz["primary_review"]["comparison_assembly_not_assigned_to_Y3"] == "GCA_902859725.1"
    assert pjm["primary_review"] == {"status": "HTTP_403_HOLD"}
    assert pjm["paper"]["access"]["native_primary_snapshot_verified"] is False
    assert pjm["paper"]["access"]["planned_figure_request_performed"] is False
    assert pjm["paper"]["wgs_accession"] == "NZ_BOUK00000000"


@pytest.fixture
def xml():
    return b"""<article><front><article-meta>
    <article-id pub-id-type="pmid">37808287</article-id>
    <article-id pub-id-type="doi">10.3389/fmicb.2023.1252427</article-id>
    <abstract>agar dilution</abstract></article-meta></front><body>
    <sec id="S2.SS6"><p>Y3 chromosome and gene: CP123364 and OQ948417, respectively</p></sec>
    <sec id="S3.SS1"><p>comparison LMG 26685 GCA_902859725.1</p></sec>
    <sec id="S3.SS2"><p>hydrolysis not detectable</p></sec>
    <sec id="S2.SS2"><p>broth dilution with agar plates</p></sec>
    <table-wrap id="T5"><table><tbody><tr><td>Ampicillin</td><td>NH*</td>
    <td>NH</td><td>NH</td></tr></tbody></table></table-wrap></body></article>"""


def test_primary_scope_keeps_namespaces_and_discrepancies(xml):
    result = audit.amz_scope(xml)
    assert result["source_identifiers"]["gene_nucleotide"] == "OQ948417"
    assert result["assay_method_normalization"] == "UNRESOLVED_INCONSISTENT_PRIMARY_WORDING"
    assert result["whole_paper_reviewed"] is False
    assert len(result["selected_element_pins"]) == 6


def test_primary_scope_rejects_reversed_identifier_namespaces(xml):
    swapped = xml.replace(b"CP123364", b"PLACEHOLDER")
    swapped = swapped.replace(b"OQ948417", b"CP123364").replace(b"PLACEHOLDER", b"OQ948417")
    with pytest.raises(ValueError, match="order reversed"):
        audit.amz_scope(swapped)


@pytest.mark.parametrize(
    "old,new",
    [
        (b"37808287", b"99999999"),
        (b"10.3389/fmicb.2023.1252427", b"10.1234/other"),
        (b"OQ948417", b"OTHER"),
        (b"CP123364", b"OTHER"),
        (b"LMG 26685", b"Y3"),
        (b"GCA_902859725.1", b"GCA_902859725.2"),
        (b"agar dilution", b"unspecified"),
        (b"broth dilution", b"agar dilution"),
        (b"agar plates", b"broth"),
        (b"not detectable", b"detectable"),
        (b"<td>NH</td>", b"<td>DETECTED</td>"),
        (b"Ampicillin", b"Amoxicillin"),
    ],
)
def test_primary_scope_fails_on_changed_evidence(xml, old, new):
    with pytest.raises(ValueError):
        audit.amz_scope(xml.replace(old, new))


@pytest.mark.parametrize("change", ["status", "hash", "redirect", "retry", "url"])
def test_primary_receipt_rejects_changed_hold(change):
    url = "https://journals.asm.org/doi/10.1128/aac.00691-22"
    plan = {"requests": {"pjm-primary": {"url": url}}, "max_bytes": 1000}
    attempt = {"key": "pjm-primary", "url": url, "retries": 0, "redirects_followed": 0}
    body = b"denied"
    receipt = {
        **attempt,
        "status": 403,
        "headers": {},
        "bytes": len(body),
        "body": {"sha256": hashlib.sha256(body).hexdigest()},
    }
    audit.primary_receipt(plan, "pjm-primary", receipt, attempt, body, 403)
    receipt = copy.deepcopy(receipt)
    if change == "status":
        receipt["status"] = 200
    elif change == "hash":
        receipt["body"]["sha256"] = "changed"
    elif change == "redirect":
        receipt["headers"]["location"] = "https://example.com/alternate"
    elif change == "retry":
        receipt["retries"] = 1
    else:
        receipt["url"] = "https://example.com/alternate"
    with pytest.raises(ValueError):
        audit.primary_receipt(plan, "pjm-primary", receipt, attempt, body, 403)

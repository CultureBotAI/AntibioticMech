"""A successor index must not turn references, comparators or search gaps into findings."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_reference_successor as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline successor attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture(scope="module")
def frozen():
    return audit.read_inputs(ROOT)


@pytest.fixture(scope="module")
def reconciled(frozen):
    _, data = frozen
    sources = {n: data[n] for n in audit.QUALIFIED + audit.CONTEXT}
    prior = copy.deepcopy(data["prior_index"])
    before = copy.deepcopy(sources)
    result = audit.reconcile(prior, sources)
    assert prior == data["prior_index"] and sources == before
    return result


def test_all_prior_links_and_provenance_retained(frozen, reconciled):
    _, data = frozen
    old = data["prior_index"]
    assert len(reconciled["terms"]) == 2002
    assert sum(bool(t["reference_links"]) for t in reconciled["terms"].values()) == 1402
    assert len(reconciled["proteins"]) == 1924
    assert len(reconciled["unresolved_reference_worklist"]) == 600
    assert sum(len(t["reference_links"]) for t in reconciled["terms"].values()) == 3068
    for term, row in old["terms"].items():
        current = reconciled["terms"][term]
        assert current["record_memberships"] == row["record_memberships"]
        assert current["source_label_sha256"] == row["source_label_sha256"]
        assert current["base_assessment"] == row["base_assessment"]
        assert current["followups"][: len(row["followups"])] == row["followups"]
        if term not in audit.SELECTED:
            assert current["reference_links"] == row["reference_links"]
            assert current["reference_accessions"] == row["reference_accessions"]
    for accession, row in old["proteins"].items():
        assert reconciled["proteins"][accession] == row


def test_new_references_and_comparator_have_distinct_roles(reconciled):
    for term, accession in audit.SELECTED.items():
        assert reconciled["terms"][term]["reference_accessions"] == [accession]
    assert "UniProtKB:P00579" not in reconciled["proteins"]
    assert reconciled["comparison_contexts"]["ARO:3000261"] == [
        {
            "protein_accession": "UniProtKB:P00579",
            "evidence": audit.pointer("dnaa-sigma-hp1184", "terms", "ARO:3000261", "references", 0),
            "included_in_determinant_reference_counts": False,
        }
    ]
    for accession, taxid, rank, species, entry, seq in (
        ("A0ABQ0Y1N0", 1293, "species", 1293, 4, 1),
        ("P03004", 83333, "strain", 562, 211, 2),
        ("P0AGB3", 83333, "strain", 562, 151, 1),
        ("O25796", 85962, "strain", 210, 121, 1),
    ):
        row = reconciled["proteins"]["UniProtKB:" + accession]
        assert row["identity"]["reference_taxon_id"] == f"NCBITaxon:{taxid}"
        assert row["identity"]["reference_taxon_rank"] == rank
        assert row["identity"]["reference_species_taxon_id"] == f"NCBITaxon:{species}"
        assert row["identity"]["entry_version"] == entry
        assert row["identity"]["sequence_version"] == seq
        assert row["experimental_subject_assignment"] is row["exact_allele_assignment"] is False


def test_all_contexts_retained_without_promoting_query_gaps(frozen, reconciled):
    _, data = frozen
    worklist = {r["aro_id"]: r for r in reconciled["unresolved_reference_worklist"]}
    for name in audit.CONTEXT + audit.QUALIFIED:
        for term in data[name]["terms"]:
            pointer = audit.pointer(name, "terms", term)
            assert pointer in reconciled["terms"][term]["followups"]
            if term not in audit.SELECTED:
                assert pointer in worklist[term]["followups"]
                assert reconciled["terms"][term]["reference_accessions"] == []
    for term in reconciled["terms"].values():
        assert term["experimental_subject_assignment"] is False
        assert term["whole_record_primary_review"] == "OPEN"


@pytest.mark.parametrize(
    "change", ["claim", "missing_claim", "duplicate_claim", "record", "members", "allele", "review"]
)
def test_dossier_binding_rejects_drift(frozen, change):
    _, data = frozen
    dossier = copy.deepcopy(data["sal-reference-context"])
    if change == "claim":
        dossier["claims"][0]["claim_sha256"] = "changed"
    elif change == "missing_claim":
        dossier["claims"].pop()
    elif change == "duplicate_claim":
        dossier["claims"].append(dossier["claims"][0])
    elif change == "record":
        dossier["records"][0]["standard_inchi_key"] = "different structure"
    elif change == "members":
        dossier["terms"]["ARO:3007028"]["record_memberships"].pop()
    elif change == "allele":
        dossier["terms"]["ARO:3007028"]["experimental_allele_assignment"] = "unsupported"
    else:
        dossier["terms"]["ARO:3007028"]["whole_record_primary_review"] = "COMPLETE"
    with pytest.raises(ValueError):
        audit.bind_dossier(data["prior_index"], dossier)


@pytest.mark.parametrize(
    "change", ["xref", "xref_version", "inactive", "rank", "organism", "allele", "version", "duplicate"]
)
def test_sal_native_crosswalk_rejects_unsupported_projection(frozen, change):
    _, data = frozen
    row = copy.deepcopy(data["sal-reference-context"]["terms"]["ARO:3007028"])
    candidate = row["reference_candidates"][0]
    if change == "xref":
        candidate["source_refseq_cross_references"].clear()
    elif change == "xref_version":
        candidate["source_refseq_cross_references"][0]["id"] = "WP_082039181"
    elif change == "inactive":
        row["species_name_context"]["native_node"]["active"] = False
    elif change == "rank":
        row["species_name_context"]["native_node"]["rank"] = "strain"
    elif change == "organism":
        candidate["organism"]["taxonId"] = 999
    elif change == "allele":
        candidate["experimental_strain_assignment"] = "unverified"
    elif change == "version":
        candidate["versions"]["entryVersion"] = True
    else:
        row["reference_candidates"].append(copy.deepcopy(candidate))
    with pytest.raises(ValueError):
        audit.sal_identity(row)


@pytest.mark.parametrize(
    "change", ["version", "reviewed", "allele", "gene", "rank", "species", "inactive", "phenotype"]
)
def test_gene_reference_preserves_native_scope(frozen, change):
    _, data = frozen
    dossier = copy.deepcopy(data["dnaa-sigma-hp1184"])
    ref = dossier["terms"]["ARO:3000248"]["references"][0]
    if change == "version":
        ref["sequence_version"] = 0
    elif change == "reviewed":
        ref["reviewed"] = "true"
    elif change == "allele":
        ref["experimental_allele_assignment"] = "unverified"
    elif change == "gene":
        ref["native_gene_matches"][0]["value"] = "dnaN"
    elif change == "rank":
        ref["reference_taxon_rank"] = "species"
    elif change == "species":
        dossier["native_taxonomy"]["562"]["scientificName"] = "different"
    elif change == "inactive":
        dossier["native_taxonomy"]["83333"]["active"] = False
    else:
        ref["resistance_phenotype_from_protein_annotation"] = True
    with pytest.raises(ValueError):
        audit.gene_identity(ref, dossier)


@pytest.mark.parametrize(
    "change", ["promote", "role", "duplicate", "accession", "list", "missing", "gene_swap"]
)
def test_sigma_cannot_promote_or_substitute_comparator(frozen, change):
    _, data = frozen
    dossier = copy.deepcopy(data["dnaa-sigma-hp1184"])
    row = dossier["terms"]["ARO:3000261"]
    ref = row["references"][0]
    if change == "promote":
        ref["eligible_as_determinant_reference_context"] = True
    elif change == "role":
        ref["role"] = "NAMED_GENE_OR_LOCUS_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
    elif change == "duplicate":
        row["references"].append(copy.deepcopy(ref))
    elif change == "accession":
        ref["accession"] = "UniProtKB:P0AGB3"
    elif change == "missing":
        row["references"].pop(0)
        row["comparator_accessions"].clear()
    elif change == "gene_swap":
        ref["gene_or_locus"] = "rpoH"
        ref["native_gene_matches"][0]["value"] = "rpoH"
    else:
        row["reference_accessions"].append(ref["accession"])
    with pytest.raises(ValueError):
        audit.selections("dnaa-sigma-hp1184", dossier)


def test_existing_identity_conflict_fails_closed(frozen):
    _, data = frozen
    prior = copy.deepcopy(data["prior_index"])
    _, identity = audit.sal_identity(data["sal-reference-context"]["terms"]["ARO:3007028"])
    prior["proteins"]["UniProtKB:A0ABQ0Y1N0"] = {"identity": {**identity, "entry_version": 5}}
    with pytest.raises(ValueError, match="conflicting reference"):
        audit.reconcile(prior, {n: data[n] for n in audit.QUALIFIED + audit.CONTEXT})


def test_historical_claim_hash_is_not_reset_to_current(frozen, monkeypatch):
    _, data = frozen
    prior = copy.deepcopy(data["prior_index"])
    rows, claims = copy.deepcopy(prior["records"]), copy.deepcopy(prior["claims"])
    for claim in claims:
        claim["historical_claim_sha256"] = claim["claim_sha256"]
    monkeypatch.setattr(audit.previous.progress, "current_records", lambda *a: ({}, {}))
    monkeypatch.setattr(audit.previous, "bind_records", lambda *a: (rows, claims))
    _, rebound = audit.rebind_current(ROOT, prior, prior["terms"])
    assert sum(c["claim_sha256"] != c["historical_claim_sha256"] for c in rebound) == 4
    assert rebound == prior["claims"]


def test_public_snapshot_pointers_counts_and_scope(frozen):
    plan, data = frozen
    doc = json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())
    assert doc["inputs"] == plan["inputs"]
    assert len(doc["records"]) == 2939 and len(doc["claims"]) == 4538
    assert doc["summary"]["selected_reference_terms"] == 1402
    assert doc["summary"]["current_source_qualified_claims"] == 4
    assert doc["summary"]["new_followup_claims"] == 74
    assert doc["summary"]["new_followup_terms"] == 18
    assert doc["summary"]["added_claim_memberships_with_references"] == 16
    assert sum(r["phi_claims_not_reassessed"] for r in doc["records"]) == 217
    assert sum(r["curator_claims_not_reassessed"] for r in doc["records"]) == 133
    assert sum(r["score_rules_not_reassessed"] for r in doc["records"]) == 467
    assert all(r["whole_record_primary_review"] == "OPEN" for r in doc["records"])
    assert all(r["no_card_assertions_is_review_complete"] is False for r in doc["records"])
    assert doc["constraints"] == audit.CONSTRAINTS
    assert (ROOT / (audit.PREFIX + ".tsv")).read_text() == audit.previous.render_rows(doc["records"])

    def visit(value):
        if isinstance(value, dict):
            if set(value) == {"input", "pointer"}:
                node = data[value["input"]]
                for key in value["pointer"].split("/")[1:]:
                    key = key.replace("~1", "/").replace("~0", "~")
                    node = node[int(key)] if isinstance(node, list) else node[key]
            else:
                for item in value.values():
                    visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(doc)

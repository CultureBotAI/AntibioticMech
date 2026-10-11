"""A parent, child, shared citation and experimental subject are distinct."""

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

from antibioticmech.activity_collections import load_record
from antibioticmech.pathway_links import load_index
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_parent_references as audit  # noqa: E402

PARENT, CHILD, GRANDCHILD = "ARO:3000001", "ARO:3000002", "ARO:3000003"
PMID = "12345"
OUTPUT = ROOT / "research/2026-10-10-card-parents-context.json"


def entry(accession="P00001", *, xrefs=(), gene="example"):
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "organism": {"taxonId": 123, "scientificName": "Reference organism"},
        "genes": [{"geneName": {"value": gene}}],
        "uniProtKBCrossReferences": [{"database": "CARD", "id": tid} for tid in xrefs],
        "references": [
            {
                "referenceNumber": 1,
                "citation": {"citationCrossReferences": [{"database": "PubMed", "id": PMID}]},
            }
        ],
    }


def cohort(label="example", entity="OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED"):
    ontology = {
        PARENT: {"label": label, "parents": [], "external_parents": [], "deprecated": False},
        CHILD: {
            "label": "child label is not exported",
            "parents": [PARENT],
            "external_parents": [],
            "deprecated": False,
        },
        GRANDCHILD: {"label": "grandchild", "parents": [CHILD], "external_parents": [], "deprecated": False},
    }
    selected = {
        PARENT: {
            "source_label_sha256": audit.citations.text_hash(label),
            "definition_citation_ids": ["PMID:" + PMID],
            "record_memberships": ["CHEBI:1"],
            "named_direct_subclass_ids": [CHILD],
        }
    }
    scopes = {PARENT: {"entity_scope": entity}}
    return selected, ontology, scopes


def derive(entries, *, label="example", members=None, entity="OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED"):
    selected, ontology, scopes = cohort(label, entity)
    return audit.derive_terms(
        selected, entries, {PMID: set(entries) if members is None else members}, ontology, scopes
    )[PARENT]


def test_child_accession_never_becomes_parent_identity():
    row = derive({"P00001": entry(xrefs=[CHILD], gene="other")})
    (child,) = row["named_direct_subclasses"]
    (candidate,) = child["reference_candidates"]
    assert candidate["explicit_card_xref"] == CHILD
    assert candidate["scope"] == "CHILD_TERM_REFERENCE_NOT_PARENT_IDENTITY"
    assert candidate["shared_parent_definition_citations"] == ["PMID:" + PMID]
    assert row["direct_parent_reference_candidates"] == []
    assert row["parent_accession_assignment"] is None and row["child_accession_propagation"] is False
    assert "child label is not exported" not in json.dumps(row)


def test_grandchild_is_not_silently_promoted_to_direct_child():
    row = derive({"P00001": entry(xrefs=[GRANDCHILD], gene="other")})
    assert row["named_direct_subclasses"][0]["reference_candidates"] == []
    assert row["citation_only_entries"] == 1


def test_same_paper_is_not_same_gene():
    row = derive({"P00001": entry(gene="other")})
    assert row["citation_only_entries"] == 1
    assert row["literal_label_reference_candidates"] == []
    assert row["direct_parent_reference_candidates"] == []


def test_literal_name_match_is_only_citation_bound_reference_context():
    row = derive({"P00001": entry(gene="EXAMPLE")})
    (candidate,) = row["literal_label_reference_candidates"]
    assert candidate["scope"] == "LITERAL_NAME_AND_CITATION_REFERENCE_NOT_ALLELE_IDENTITY"
    assert candidate["source_citation_ids"] == ["PMID:" + PMID]
    assert candidate["matched_gene_fields"] == [
        {"field": "geneName", "value_sha256": audit.citations.text_hash("EXAMPLE")}
    ]
    assert row["parent_accession_assignment"] is None
    assert row["citation_only_entries"] == 0


def test_literal_name_without_source_citation_is_not_candidate():
    assert derive({"P00001": entry()}, members=set())["literal_label_reference_candidates"] == []


def test_substring_does_not_become_a_gene_alias():
    row = derive({"P00001": entry(gene="example")}, label="resistance associated with example")
    assert row["literal_label_reference_candidates"] == []


def test_explicit_parent_cross_reference_still_not_experimental_assignment():
    row = derive({"P00001": entry(xrefs=[PARENT], gene="other")})
    (candidate,) = row["direct_parent_reference_candidates"]
    assert candidate["explicit_card_xref"] == PARENT
    assert row["parent_accession_assignment"] is None and row["primary_review_status"] == "OPEN"


def test_child_reference_without_shared_paper_retains_empty_citation_overlap():
    row = derive({"P00001": entry(xrefs=[CHILD], gene="other")}, members=set())
    assert (
        row["named_direct_subclasses"][0]["reference_candidates"][0]["shared_parent_definition_citations"]
        == []
    )


def test_zero_results_do_not_imply_biological_absence():
    row = derive({})
    assert row["literature_entries"] == 0 and row["no_result_is_biological_absence"] is False
    assert row["primary_review_status"] == "OPEN"


def test_rna_scope_cannot_require_a_protein_assignment():
    row = derive({}, entity="RNA_TERM_NOT_A_PROTEIN_PRODUCT")
    assert row["disposition"] == "RNA_NOT_A_PROTEIN_PRODUCT"
    assert row["parent_accession_assignment"] is None


def test_missing_taxonomy_is_explicitly_unverified():
    row = audit.project_reference(entry(), None)
    assert row["reference_taxon_id"] == "NCBITaxon:123"
    assert row["taxonomy_identity_verified"] is False and row["taxonomy_rank"] is None
    assert (
        row["experimental_subject_assignment"]
        is row["exact_allele_assignment"]
        is row["genome_assignment"]
        is False
    )


@pytest.mark.parametrize("change", [{"active": False}, {"taxonId": 124}, {"rank": ""}])
def test_invalid_reference_taxonomy_rejected(change):
    taxon = {
        "taxonId": 123,
        "active": True,
        "rank": "species",
        "scientificName": "Reference organism",
        **change,
    }
    with pytest.raises(ValueError, match="taxonomy"):
        audit.project_reference(entry(), taxon)


@pytest.mark.parametrize(
    "change", [{"sequence": {}}, {"entryAudit": {"entryVersion": 1}}, {"entryType": "unknown"}]
)
def test_invalid_reference_metadata_rejected(change):
    with pytest.raises(ValueError, match="reference entry"):
        audit.project_reference({**entry(), **change}, None)


def selection_fixture():
    selected, ontology, _ = cohort()
    scope = audit.term_scope.term_scope(ontology, PARENT, 1)
    source = {"terms": {PARENT: {**scope, "reference_candidate_accessions": []}}}
    definitions = {
        "terms": {
            PARENT: {
                "label_sha256": selected[PARENT]["source_label_sha256"],
                "record_memberships": ["CHEBI:1"],
                "definition_citation_ids": ["PMID:" + PMID],
            }
        }
    }
    return source, definitions, ontology, {PARENT: "example"}, {PARENT: ["CHEBI:1"]}


def test_selection_is_reproduced_from_all_unlinked_parents():
    assert audit.select_terms(*selection_fixture()) == cohort()[0]


@pytest.mark.parametrize("mutation", ["children", "label", "membership", "scope", "deprecated"])
def test_parent_selection_rejects_source_drift(mutation):
    source, definitions, ontology, labels, memberships = copy.deepcopy(selection_fixture())
    if mutation == "children":
        source["terms"][PARENT]["named_direct_subclass_count"] = 2
    elif mutation == "label":
        ontology[PARENT]["label"] = "another"
    elif mutation == "membership":
        memberships[PARENT] = ["CHEBI:2"]
    elif mutation == "scope":
        source["terms"][PARENT]["entity_scope"] = "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    else:
        ontology[PARENT]["deprecated"] = True
    with pytest.raises(ValueError, match="drift"):
        audit.select_terms(source, definitions, ontology, labels, memberships)


def test_linked_parent_is_not_selected_as_unlinked():
    values = selection_fixture()
    values[0]["terms"][PARENT]["reference_candidate_accessions"] = ["UniProtKB:P00001"]
    assert audit.select_terms(*values) == {}


def assert_pre_pathway_record(row, path, transition, restored):
    assert transition["path"] == row["path"]
    assert transition["identifier"] == row["identifier"]
    assert transition["before_sha256"] == row["sha256"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == transition["after_sha256"]
    historical = load_record(path)
    plans = yaml.safe_load((ROOT / "curation/pathway_links.yaml").read_text())["records"]
    plan, = [plan for plan in plans if plan["identifier"] == row["identifier"]]
    commit, _ = load_index(ROOT)
    assert historical.pop("related_records") == [
        {"corpus": "PathwayMech", **link, "source_version": commit} for link in plan["links"]
    ]
    removed_actions = {"ADD_PATHWAY_LINKS", "RECONCILED_BRANCH_CURATION"}
    removed = [event["action"] for event in historical["curation_history"]
               if event["action"] in removed_actions]
    expected = ["ADD_PATHWAY_LINKS"]
    if row["identifier"] != "CHEBI:45924":
        expected.append("RECONCILED_BRANCH_CURATION")
    assert removed == expected
    historical["curation_history"] = [event for event in historical["curation_history"]
                                      if event["action"] not in removed_actions]
    write_validated_antibiotic(historical, restored)
    assert hashlib.sha256(restored.read_bytes()).hexdigest() == row["sha256"]


def test_saved_dossier_scope_and_record_pins(tmp_path):
    doc = json.loads(OUTPUT.read_bytes())
    summary = doc["summary"]
    assert (summary["selected_terms"], summary["selected_records"], summary["assertion_memberships"]) == (
        43,
        50,
        75,
    )
    assert (summary["literature_queries"], summary["new_queries"], summary["reused_queries"]) == (46, 33, 13)
    assert summary["corpus_record_hashes_verified"] == 2939
    assert (
        summary["biological_record_writes"]
        == summary["experimental_protein_assignments"]
        == summary["whole_record_reviews_completed"]
        == 0
    )
    assert len(doc["terms"]) == 43 and len(doc["records"]) == 50
    followup = json.loads((ROOT / "research/2026-10-10-card-parent-primary-curation.json").read_bytes())
    integration = json.loads((ROOT / "research/2026-10-11-pr-integration-reconciliation.json").read_bytes())
    transitions = {row["identifier"]: row for row in integration["changes"]}
    assert set(transitions) & {row["identifier"] for row in doc["records"]} == {
        "CHEBI:45924", "CHEBI:46081", "CHEBI:9448",
    }
    for row in doc["records"]:
        path = ROOT / row["path"]
        if row["identifier"] in transitions:
            assert_pre_pathway_record(row, path, transitions[row["identifier"]], tmp_path / path.name)
            continue
        if row["identifier"] not in followup["records"]:
            assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
            continue
        proof = followup["records"][row["identifier"]]
        assert proof["before_record_sha256"] == row["sha256"]
        current = load_record(path)
        n, h = proof["existing_claims_preserved"], proof["prior_history_events"]
        assert current["resistance_mechanisms"][n : n + 5] == proof["added_claims"]
        assert current["curation_history"][h] == proof["curation_event"]
        historical = copy.deepcopy(current)
        historical["resistance_mechanisms"] = historical["resistance_mechanisms"][:n]
        historical["curation_history"] = historical["curation_history"][:h]
        restored = tmp_path / path.name
        write_validated_antibiotic(historical, restored)
        assert hashlib.sha256(restored.read_bytes()).hexdigest() == row["sha256"]
    assert all(
        q["complete_for_query"] and not q["establishes_biological_absence"] for q in doc["queries"].values()
    )


@pytest.mark.parametrize("mutation", ["label", "link", "history", "resistance"])
@pytest.mark.parametrize("repin", [False, True])
def test_pathway_reconciliation_cannot_hide_other_drift(tmp_path, mutation, repin):
    dossier = json.loads(OUTPUT.read_bytes())
    row, = [row for row in dossier["records"] if row["identifier"] == "CHEBI:45924"]
    integration = json.loads((ROOT / "research/2026-10-11-pr-integration-reconciliation.json").read_bytes())
    transition, = [item for item in integration["changes"] if item["identifier"] == row["identifier"]]
    current = load_record(ROOT / row["path"])
    if mutation == "label":
        current["label"] += " unexpected change"
    elif mutation == "link":
        current["related_records"][0]["basis"] += " unexpected change"
    elif mutation == "history":
        current["curation_history"][0]["changes"] += " unexpected change"
    else:
        current["resistance_mechanisms"][0]["note"] = "unexpected change"
    changed = tmp_path / "changed.yaml"
    write_validated_antibiotic(current, changed)
    if repin:
        transition["after_sha256"] = hashlib.sha256(changed.read_bytes()).hexdigest()
    with pytest.raises(AssertionError):
        assert_pre_pathway_record(row, changed, transition, tmp_path / "historical.yaml")


def test_saved_reference_projection_has_no_orphan_or_experimental_assignment():
    doc = json.loads(OUTPUT.read_bytes())
    accessions = set()
    for row in doc["terms"].values():
        assert row["parent_accession_assignment"] is None and not row["child_accession_propagation"]
        assert row["primary_review_status"] == "OPEN"
        for key in ("direct_parent_reference_candidates", "literal_label_reference_candidates"):
            accessions.update(c["protein_accession"] for c in row[key])
        for child in row["named_direct_subclasses"]:
            accessions.update(c["protein_accession"] for c in child["reference_candidates"])
    assert accessions == set(doc["reference_proteins"])
    for row in doc["reference_proteins"].values():
        assert (
            not row["experimental_subject_assignment"]
            and not row["exact_allele_assignment"]
            and not row["genome_assignment"]
        )
        assert not {
            "sequence",
            "alteration",
            "variant",
            "strain",
            "genes",
            "mic_value",
            "assembly_accession",
        } & set(row)


def test_saved_canary_reference_is_not_promoted_to_acc_parent_allele():
    doc = json.loads(OUTPUT.read_bytes())
    row = doc["terms"]["ARO:3001815"]
    (candidate,) = row["literal_label_reference_candidates"]
    assert candidate["protein_accession"] == "UniProtKB:Q9XB24"
    assert candidate["source_citation_ids"] == ["PMID:10428914"]
    assert row["parent_accession_assignment"] is None


def test_additional_taxonomy_is_reference_only_and_ranked():
    doc = json.loads(OUTPUT.read_bytes())
    assert set(doc["reference_taxonomy_requests"]) == {"tax-316275", "tax-500640"}
    assert doc["summary"]["unverified_reference_taxa"] == []
    for protein in doc["reference_proteins"].values():
        assert protein["taxonomy_identity_verified"]
        assert protein["taxonomy_rank"] and protein["taxonomy_scientific_name"]
        assert not protein["experimental_subject_assignment"]
    references = [
        p for p in doc["reference_proteins"].values() if p["reference_taxon_id"] == "NCBITaxon:316275"
    ]
    assert references and all(p["taxonomy_rank"] == "strain" for p in references)


def test_reference_accessions_include_all_lanes_without_duplicates():
    row = derive({"P00001": entry(xrefs=[PARENT, CHILD])})
    assert audit.reference_accessions({PARENT: row}) == {"P00001"}

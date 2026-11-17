"""Shared citations and gene strings must never silently assign experimental identity."""

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_citation_concordance as audit  # noqa: E402

TID = "ARO:3001299"


def entry(accession="P12345", gene="fixture", pmid="12345"):
    return {"primaryAccession": accession, "entryType": "UniProtKB reviewed (Swiss-Prot)",
            "entryAudit": {"entryVersion": 3, "sequenceVersion": 1},
            "genes": [{"geneName": {"value": gene}}],
            "organism": {"taxonId": 999, "scientificName": "Fixture species"},
            "references": [{"referenceNumber": 1, "citation": {
                "citationCrossReferences": [{"database": "PubMed", "id": pmid}]}}]}


def join(entries, *, label="fixture", citations=None, direct=None):
    definitions = {TID: {"definition_citation_ids": ["PMID:12345"] if citations is None else citations,
                         "record_memberships": ["CHEBI:1"]}}
    return audit.concordance(entries, definitions, direct or {}, {TID: label})[TID]


def taxonomy():
    return {"taxonId": 999, "active": True, "scientificName": "Fixture species", "rank": "species"}


def test_shared_paper_and_name_remain_nonassigning_leads():
    row = join({"P12345": entry()})
    lead, = row["citation_overlap_leads"]
    assert lead["literal_source_label_gene_matches"] == ["fixture"]
    assert lead["explicit_card_link"] is False
    assert lead["identity_status"] == "LITERATURE_OVERLAP_NOT_A_PROTEIN_OR_ALLELE_ASSIGNMENT"
    assert row["explicit_reference_candidates"] == []
    assert row["primary_support_status"] == "NOT_ESTABLISHED_BY_CITATION_CONCORDANCE"


def test_even_a_unique_shared_paper_can_concern_a_different_gene():
    row = join({"P12345": entry(gene="different")})
    lead, = row["citation_overlap_leads"]
    assert lead["literal_source_label_gene_matches"] == []
    assert lead["shared_citation_ids"] == ["PMID:12345"]
    assert lead["explicit_card_link"] is False


def test_same_gene_family_in_multiple_organisms_is_not_collapsed():
    first, second = entry(), entry("Q12345")
    second["organism"]["taxonId"] = 1000
    row = join({"P12345": first, "Q12345": second})
    assert len(row["citation_overlap_leads"]) == 2
    assert all(x["literal_source_label_gene_matches"] == ["fixture"] for x in row["citation_overlap_leads"])


def test_locus_names_and_similar_allele_labels_are_not_gene_synonyms():
    data = entry(gene="fixture2")
    data["genes"][0]["orderedLocusNames"] = [{"value": "fixture"}]
    data["genes"][0]["orfNames"] = [{"value": "fixture"}]
    assert join({"P12345": data})["citation_overlap_leads"][0]["literal_source_label_gene_matches"] == []


def test_exact_alias_match_is_case_insensitive_without_punctuation_rewriting():
    data = entry(gene="canonical")
    data["genes"][0]["synonyms"] = [{"value": "FIXTURE"}]
    assert join({"P12345": data})["citation_overlap_leads"][0][
        "literal_source_label_gene_matches"] == ["FIXTURE"]
    assert join({"P12345": data}, label="fix-ture")["citation_overlap_leads"][0][
        "literal_source_label_gene_matches"] == []


def test_absent_citation_does_not_remove_an_explicit_reference_link():
    data = entry(pmid="23456")
    row = join({"P12345": data}, direct={TID: [(data, {})]})
    assert row["explicit_reference_candidates"] == ["UniProtKB:P12345"]
    assert row["citation_overlap_leads"] == []


def test_explicit_and_citation_links_are_counted_separately():
    data = entry()
    lead, = join({"P12345": data}, direct={TID: [(data, {})]})["citation_overlap_leads"]
    assert lead["explicit_card_link"] is True
    assert lead["reference_numbers"] == [1]


def test_doi_case_normalization_but_no_invented_prefix():
    assert audit.citation_id("DOI", "10.1234/EXAMPLE") == "DOI:10.1234/example"
    assert audit.source_ids(["DOI:10.1234/Example", "PMID:12345"]) == {
        "DOI:10.1234/example", "PMID:12345"}
    assert audit.citation_id("OTHER", "example") is None


@pytest.mark.parametrize("database,value", [("DOI", ".1234/example"), ("DOI", "10.1234/a b"),
                                            ("PubMed", "0"), ("PubMed", "PMID:12345"), ("PubMed", " 12345")])
def test_malformed_bibliography_ids_are_not_accepted(database, value):
    with pytest.raises(ValueError, match="malformed"):
        audit.citation_id(database, value)


def test_malformed_doi_is_quarantined_without_discarding_a_valid_pmid():
    data = entry()
    data["references"][0]["citation"]["citationCrossReferences"].append({
        "database": "DOI", "id": ".1234/private"})
    ref, = audit.entry_bibliography(data)
    assert ref["identifiers"] == ["PMID:12345"]
    assert len(ref["unresolved_identifiers"]) == 1
    assert ref["unresolved_identifiers"][0]["status"] == "MALFORMED_IDENTIFIER_NOT_REPAIRED_OR_JOINED"
    assert ".1234/private" not in json.dumps(ref)
    assert join({"P12345": data})["citation_overlap_leads"][0]["shared_citation_ids"] == ["PMID:12345"]
    assert join({"P12345": data}, citations=["DOI:10.1234/private"])["citation_overlap_leads"] == []


@pytest.mark.parametrize("number", [0, True, "1", None])
def test_invalid_reference_number_rejected(number):
    data = entry()
    data["references"][0]["referenceNumber"] = number
    with pytest.raises(ValueError, match="reference numbering"):
        audit.entry_bibliography(data)


def test_duplicate_reference_number_rejected():
    data = entry()
    data["references"].append(copy.deepcopy(data["references"][0]))
    with pytest.raises(ValueError, match="reference numbering"):
        audit.entry_bibliography(data)


@pytest.mark.parametrize("change", ["key", "sequence"])
def test_snapshot_entry_identity_and_sequence_guard(change):
    data = entry()
    if change == "key":
        data["primaryAccession"] = "Q12345"
    else:
        data["sequence"] = {"value": "PRIVATE"}
    with pytest.raises(ValueError, match="mismatch|sequence"):
        join({"P12345": data})


def test_projection_retains_rank_and_never_exports_positions_or_constructs():
    data = entry()
    data["proteinDescription"] = {"flag": "Fragment", "recommendedName": {"fullName": {"value": "PRIVATE"}}}
    data["references"][0]["referencePositions"] = ["PRIVATE"]
    data["references"][0]["referenceComments"] = [{"type": "TISSUE", "value": "PRIVATE"}]
    taxon = {**taxonomy(), "rank": "serotype"}
    result = audit.project_entry(data, taxon)
    assert result["taxonomy_rank"] == "serotype" and result["description_flag"] == "Fragment"
    assert result["experimental_subject_assignment"] is False
    assert result["exact_allele_assignment"] is False
    assert "PRIVATE" not in json.dumps(result)


@pytest.mark.parametrize("mutation", ["inactive", "wrong_taxon", "version", "review_status", "sequence"])
def test_projection_identity_guards(mutation):
    data, taxon = entry(), taxonomy()
    if mutation == "inactive":
        taxon["active"] = False
    elif mutation == "wrong_taxon":
        taxon["taxonId"] = 1000
    elif mutation == "version":
        data["entryAudit"]["sequenceVersion"] = True
    elif mutation == "review_status":
        data["entryType"] = "unknown"
    else:
        data["sequence"] = {}
    with pytest.raises(ValueError):
        audit.project_entry(data, taxon)


def test_published_full_corpus_scope_and_no_promoted_assignments():
    result = json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())
    summary = result["summary"]
    assert result["scope"] == audit.SCOPE and result["selection"] == "ALL_EXISTING_CARD_TERMS"
    assert summary["corpus_records_checked"] == 2939
    assert summary["terms"] == len(result["terms"]) == 2002
    assert summary["source_assertion_memberships"] == 4538
    assert summary["cached_uniprot_entries_searched"] == 4182
    assert summary["explicit_reference_links_reproduced"] == 980
    assert summary["unlinked_terms_with_citation_overlap"] == 59
    assert summary["unlinked_terms_with_literal_gene_match"] == 2
    assert summary["unlinked_literal_gene_match_links"] == 9
    assert summary["snapshot_malformed_identifiers_not_joined"] == 18
    assert summary["biological_records_changed"] == summary["exact_allele_assignments"] == 0
    assert all(not p["experimental_subject_assignment"] and not p["exact_allele_assignment"]
               for p in result["proteins"].values())
    tlrb, = result["terms"][TID]["citation_overlap_leads"]
    assert tlrb["protein_accession"] == "UniProtKB:Q9S1M6"
    assert tlrb["literal_source_label_gene_matches"] == ["tlrB"]
    assert tlrb["explicit_card_link"] is False
    other, = result["terms"]["ARO:3002620"]["citation_overlap_leads"]
    assert other["literal_source_label_gene_matches"] == []


@pytest.fixture(scope="module")
def tlrb_context():
    return json.loads((ROOT / "research/2026-10-09-tlrb-primary-context.json").read_bytes())


def test_tlrb_compound_and_reference_context_preserve_source_claims(tlrb_context):
    compound = tlrb_context["compound"]
    assert compound["identifier"] == "CHEBI:17658"
    assert compound["standard_inchi_key"] == "WBPYTXDJUQJLPQ-VMXQISHHSA-N"
    assert compound["source_resistance_assertions"] == 40
    assert compound["tested_preparation_exact_structure_independently_established"] is False
    assert audit.reference.digest(ROOT / compound["path"]) == compound["sha256"]
    assert tlrb_context["reference_protein"]["accession"] == "UniProtKB:Q9S1M6"
    assert tlrb_context["curation_disposition"] == "QUALIFIED_RESEARCH_CONTEXT_ONLY"


def test_tlrb_donor_host_and_strain_annotations_do_not_collapse(tlrb_context):
    contexts = {r["role"]: r for r in tlrb_context["organism_contexts"]}
    assert contexts["GENE_DONOR_SPECIES"]["taxon_id"] == "NCBITaxon:1906"
    assert contexts["ASSAY_HOST_SPECIES"]["taxon_id"] == "NCBITaxon:1916"
    assert all(r["rank"] == "species" and r["strain_taxon_id"] is None for r in contexts.values())
    strains = {r["pmid"]: r["strain_annotations"] for r in tlrb_context["citation_scoped_strains"]}
    assert strains == {"PMID:10348045": ["C373.1"], "PMID:10972803": ["ATCC 19609"]}


def test_tlrb_synonym_does_not_merge_ontology_terms(tlrb_context):
    caution = tlrb_context["cross_reference_caution"]
    assert caution["uniprot_explicit_card_id"] == "ARO:3004592"
    assert caution["tlrb_is_explicit_card_xref"] is False
    assert caution["merge_aro_terms"] is False
    assert tlrb_context["source_term"] == TID


def test_tlrb_negative_result_and_causal_uncertainty_are_retained(tlrb_context):
    review = tlrb_context["primary_review"]["PMID:10972803"]
    assert any("not unequivocally established" in text for text in review["findings"])
    assert any("No drug modification or inactivation" in text for text in review["findings"])
    assert review["whole_paper_review_complete"] is False
    assert review["figures_visually_reviewed"] is False
    assert review["native_reference_is_exact_experimental_protein"] is False
    assert tlrb_context["primary_review"]["PMID:10348045"]["primary_results_reviewed"] is False
    assert tlrb_context["summary"]["whole_corpus_primary_review"] == "OPEN"


def test_tlrb_reference_projection_matches_public_audit_without_private_caches(tlrb_context):
    item = tlrb_context["inputs"]["concordance"]
    result = json.loads(audit.reference.check_pin(ROOT, item).read_bytes())
    assert result["proteins"]["UniProtKB:Q9S1M6"] == tlrb_context["reference_protein"]
    assert set(tlrb_context["bibliography"]) == {"PMID:10348045", "PMID:10972803"}
    for item in tlrb_context["bibliography"].values():
        assert item["provider"] == "EMBL-EBI Europe PMC"
        assert item["url"].startswith("https://www.ebi.ac.uk/europepmc/")
        assert len(item["cache"]["sha256"]) == len(item["receipt"]["sha256"]) == 64

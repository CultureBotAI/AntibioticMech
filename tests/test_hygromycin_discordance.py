"""Keep reference identities, negative comparisons and access limitations separate."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    path = ROOT / "research/2026-10-09-hygromycin-discordance-followup.json"
    return json.loads(path.read_bytes())


def test_historical_dossier_is_preserved(dossier):
    pin = dossier["prior_dossier"]
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    prior = json.loads(payload)
    assert dossier["record"] == prior["record"]
    assert {t["taxon_id"]: t["scope"] for t in prior["taxonomy"]} == {
        "NCBITaxon:4932": "EXPERIMENTAL_SPECIES",
        "NCBITaxon:559292": "REFERENCE_PROTEIN_TAXON_ONLY",
    }


def test_manual_text_review_is_not_claimed_as_cached_pdf_or_figure_review(dossier):
    study = dossier["older_study"]
    assert study["reference"] == "PMID:16118187"
    assert study["doi"] == "10.1534/genetics.105.046888"
    review = study["review"]
    assert review["method"] == "MANUAL_REVIEW_OF_AUTHOR_UPLOADED_ARTICLE_TEXT_TRANSCRIPTION"
    assert review["pdf_downloaded"] is review["figure_visually_inspected"] is False
    assert review["successful_fulltext_cache"] is None
    assert study["failed_direct_fetch"]["status"] == 403
    assert "does not contain the reviewed primary text" in study["failed_direct_fetch"]["scope"]
    assert urlsplit(study["primary_url"]).hostname == "www.researchgate.net"


def test_separate_negatives_and_unshown_combined_comparison(dossier):
    ubc4, ubc5, singles, combined = dossier["older_study"]["qualitative_findings"]
    assert ubc4["genes"] == ["UBC4"] and ubc4["direction"] == "SENSITIZATION"
    assert ubc5["genes"] == ["UBC5"] and ubc5["context"] == "SINGLE_GENE_LOSS"
    negative = "NO_GROWTH_IMPAIRMENT_REPORTED_UNDER_TESTED_CONDITIONS"
    assert ubc5["direction"] == singles["direction"] == combined["direction"] == negative
    assert singles["genes"] == combined["genes"] == ["UBC6", "UBC7"]
    assert singles["context"] == "SEPARATE_SINGLE_GENE_LOSS_COMPARISONS"
    assert combined["context"] == "COMBINED_GENE_LOSS_COMPARISON"
    assert "data not shown" in combined["scope"] and "not a Figure 1B panel" in combined["scope"]


def test_experimental_identity_is_not_filled_from_canonical_reference(dossier):
    identity = dossier["older_study"]["experimental_identity"]
    assert identity["species_taxon_id"] == "NCBITaxon:4932"
    assert identity["named_background"] == "NOT_ESTABLISHED_BY_THIS_REVIEW"
    assert all(identity[key] is None for key in (
        "experimental_strain_taxon_id", "experimental_genome_accession",
        "experimental_protein_accession", "experimental_allele_accession",
    ))


@pytest.mark.parametrize("symbol,accession,locus,sgd,version", [
    ("UBC4", "P15731", "YBR082C", "S000000286", 228),
    ("UBC5", "P15732", "YDR059C", "S000002466", 207),
])
def test_additional_references_are_versioned_and_explicitly_reference_only(
    dossier, symbol, accession, locus, sgd, version,
):
    gene, = [g for g in dossier["additional_reference_genes"] if g["gene"] == symbol]
    assert gene["reference_protein_accession"] == "UniProtKB:" + accession
    assert gene["systematic_locus"] == locus
    assert gene["sgd_cross_reference"] == "SGD:" + sgd
    assert gene["entry_audit"] == {"entryVersion": version, "sequenceVersion": 1}
    assert gene["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
    assert gene["reference_taxon_id"] == "NCBITaxon:559292"
    assert gene["scope"] == "CANONICAL_S288C_REFERENCE_NOT_TESTED_ALLELE_OR_STRAIN"
    request = dossier["reference_request"]
    assert request["release"] == "2026_03" and request["total_results"] == 2
    assert request["has_next_page"] is request["sequence_requested"] is False
    assert "sequence" not in request["fields"].split(",")
    assert request["endpoint"] == "https://rest.uniprot.org/uniprotkb/search"


def test_disagreement_is_retained_without_establishing_its_cause(dossier):
    comparison = dossier["later_study_comparison"]
    assert comparison["reference"] == "DOI:10.17912/micropub.biology.001276"
    assert comparison["direction"] == "LOSS_ASSOCIATED_SENSITIZATION"
    assert comparison["disagreement_status"] == "UNRESOLVED"
    assert comparison["explanation_status"] == "AUTHOR_HYPOTHESIS_NOT_ESTABLISHED_CAUSE"
    assert "no cross-study subject merge" in comparison["context"]
    assert dossier["status"] == "OLDER_PRIMARY_TEXT_REVIEWED_DISCORDANCE_UNRESOLVED"


def test_export_is_qualitative_and_does_not_complete_the_corpus(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "construct", "protocol", "primers",
        "resistance_mechanisms", "activity_spectrum", "mic", "mic_value", "measurement_value",
    }
    limits = " ".join(dossier["limitations"])
    assert "No NCBI request" in limits
    assert "HYGROMYCIN-VJY305-SKY-ALIAS-CONFLICT remains unresolved" in limits
    assert "does not complete" in limits and "2939-record" in limits


def test_record_and_source_assertions_are_unchanged(dossier):
    pin = dossier["record"]
    path = ROOT / pin["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["record_sha256"]
    record = load_record(path)
    assert record["identifier"] == pin["identifier"]
    assert record["chemical_structure"]["standard_inchi_key"] == pin["standard_inchi_key"]
    assert len(record["resistance_mechanisms"]) == pin["existing_assertions_unchanged"] == 5
    assert dossier["curation_decision"]["production_record_changes"] == 0
    assert dossier["curation_decision"]["curation_events_added"] == 0

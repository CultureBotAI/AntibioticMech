"""Primary context must not collapse reference proteins, hosts or compound forms."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-lmrc-primary-context.json").read_bytes())


def test_primary_reprint_and_supplement_scope_are_explicit(dossier):
    paper = dossier["primary_paper"]
    assert paper["reference"] == "PMID:34488446"
    assert paper["doi"] == "10.1128/mbio.01731-21"
    assert paper["version"] == "PUBLISHED_JOURNAL_REPRINT_WITHIN_THESIS_APPENDIX"
    assert [(p["pdf_page"], p["printed_page"]) for p in paper["visually_inspected_pages"]] == [
        (2, 1), (4, 3), (5, 4),
    ]
    assert paper["supplement_table_s2_inspected"] is False
    assert "other articles" in paper["scope_limit"]
    assert "no rights inferred for the entire bundle" in paper["license"]


def test_native_and_heterologous_results_remain_separate(dossier):
    native, host = dossier["qualitative_contexts"]
    assert native["context"] == "NATIVE_PRODUCER"
    assert native["source_subject_label"] == "Streptomyces lincolnensis ATCC 25466"
    assert native["species_name_taxon_id"] == "NCBITaxon:1915"
    assert "not a major contributor" in native["finding"]
    assert host["context"] == "HETEROLOGOUS_LABORATORY_HOST"
    assert host["source_subject_label"] == "Streptomyces coelicolor M1154"
    assert host["species_name_taxon_id"] == "NCBITaxon:1902"
    assert "does not identify its native locus" in host["finding"]
    assert native["taxon_scope"] == host["taxon_scope"] == "SPECIES_NAME_NOT_STRAIN_ID"


def test_reference_candidates_retain_the_original_citation_contexts(dossier):
    contexts = json.loads((ROOT / "research/2026-10-09-card-citation-context.json").read_bytes())
    candidates = {c["accession"]: c for c in dossier["reference_candidates"]}
    assert set(candidates) == {"UniProtKB:A9Y8T8", "UniProtKB:A0A1B1M202"}
    for accession, candidate in candidates.items():
        original = contexts["proteins"][accession]
        assert candidate["citation_contexts"] == original["reference_contexts"]
        assert candidate["entry_audit"] == original["entry_audit"]
        assert candidate["reference_taxon_id"] == original["reference_taxon_id"] == "NCBITaxon:1915"
        assert candidate["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        assert candidate["scope"] == "REFERENCE_METADATA_NOT_TESTED_ALLELE_OR_HOST_LOCUS"
    journal, = candidates["UniProtKB:A9Y8T8"]["citation_contexts"]
    submission, = candidates["UniProtKB:A0A1B1M202"]["citation_contexts"]
    assert journal["citation"]["id"] == "19085073"
    assert journal["citation"]["citationType"] == "journal article"
    assert journal["strain_annotations"] == []
    assert submission["citation"]["id"] == "CI-A81CVAOAPPCF"
    assert submission["citation"]["citationType"] == "submission"
    assert [s["value"] for s in submission["strain_annotations"]] == ["NRRL 2936"]


def test_shared_archive_identifier_does_not_select_an_experimental_allele(dossier):
    assert {c["uniparc_id"] for c in dossier["reference_candidates"]} == {"UPI000162A5BF"}
    decision = dossier["candidate_resolution"]
    assert decision["status"] == "MULTIPLE_REFERENCE_CANDIDATES_RETAINED"
    assert decision["selected_experimental_accession"] is None
    assert "no new sequence comparison" in decision["scope"]
    first, second = dossier["reference_candidates"]
    assert first["genes"] == []
    assert second["genes"][0]["orfNames"][0]["value"] == "SLINC_0260"
    assert first["source_accession_evidence"] == [
        {"evidenceCode": "ECO:0000313", "id": "ABX00624.1", "source": "EMBL"},
    ]
    assert {e["id"] for e in second["source_accession_evidence"]} == {"ANS62484.1", "UP000092598"}


def test_taxonomic_ranks_and_tested_strain_limits(dossier):
    taxa = dossier["taxonomy"]
    assert taxa["1915"]["rank"] == taxa["1902"]["rank"] == "species"
    assert taxa["100226"]["rank"] == "strain"
    assert taxa["100226"]["parent"]["taxonId"] == 1902
    assert "M145" in taxa["100226"]["scientificName"]
    withheld = dossier["withheld_assignments"]
    for key in ("tested_strain_taxon_ids", "tested_genome_accessions", "tested_allele_crosswalk"):
        assert withheld[key] == "NOT_ESTABLISHED"
    assert "was not assigned to M1154" in withheld["m1154_reference_taxon_substitution"]


@pytest.mark.parametrize("label", ["lincomycin", "clindamycin", "celesticetin"])
def test_database_claims_are_not_silently_promoted_to_primary_evidence(dossier, label):
    membership, = [r for r in dossier["record_memberships"] if r["label"] == label]
    record = load_record(ROOT / membership["record_path"])
    assert record["identifier"] == membership["identifier"]
    assert record["chemical_structure"]["standard_inchi_key"] == membership["standard_inchi_key"]
    claim, = [m for m in record["resistance_mechanisms"] if m.get("aro_id") == "ARO:3002881"]
    payload = json.dumps(claim, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    assert hashlib.sha256(payload).hexdigest() == membership["source_assertion_sha256"]
    assert set(claim) == {"aro_id", "label", "mechanism_type", "evidence"}
    assert membership["source_assertion_status"] == "PRESERVED_DATABASE_ASSERTION_NOT_REVALIDATED"
    assert membership["new_experimental_assertions"] == 0
    assert membership["primary_scope"] == (
        "PRODUCTION_COMPARISON_NOT_LMRC_RESISTANCE_ENDPOINT" if label == "celesticetin"
        else "NAMED_DRUG_TESTED_MATERIAL_FORM_UNRESOLVED"
    )


def test_review_is_not_counted_as_corpus_curation(dossier):
    assert dossier["status"] == "PRIMARY_CONTEXT_REVIEW_ONLY_NO_CORPUS_CURATION"
    assert dossier["aro_id"] == "ARO:3002881"
    preservation = dossier["preservation"]
    assert preservation["record_hashes_verified"] == 2939
    assert preservation["record_path_search_includes_ignored"] is True
    assert preservation["biological_record_changes"] == preservation["curation_events_added"] == 0
    assert "does not complete any compound" in " ".join(dossier["limitations"])


def test_only_permitted_sources_and_replayable_provenance(dossier):
    paper = dossier["primary_paper"]
    assert urlsplit(paper["pdf"]["url"]).hostname == "dspace.cuni.cz"
    assert paper["pdf"]["sha256"] == (
        "1b94db0911267332a5b0f796c67cdf98370b376173d88243e5c6ddac5b9b1c74"
    )
    assert paper["pdf_cache"]["sha256"] == paper["pdf"]["sha256"]
    assert urlsplit(paper["citation_request"]["url"]).hostname == "www.ebi.ac.uk"
    request = dossier["taxonomy_request"]
    assert request["url"] == "https://rest.uniprot.org/taxonomy/1902"
    assert request["status"] == 200 and request["release"] == "2026_03"
    assert "No NCBI request" in " ".join(dossier["limitations"])


def test_export_is_qualitative_metadata_only(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "features", "variants", "alteration", "resistance_mechanisms",
        "activity_spectrum", "mic", "mic_value", "measurement_value", "protocol", "primers",
        "construct", "strain_taxon_id", "assembly_accession", "biosample_accession",
    }

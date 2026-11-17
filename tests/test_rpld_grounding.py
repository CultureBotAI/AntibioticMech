"""Protein identity and reference metadata do not establish a resistance allele."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-rpld-reference-grounding.json").read_bytes())


def test_definition_conflict_is_not_an_rna_or_experimental_assignment(dossier):
    assert dossier["status"] == "PROTEIN_PRODUCT_IDENTITY_SUPPORTED_EXPERIMENTAL_GROUNDING_PENDING"
    conflict = dossier["ontology_conflict"]
    assert conflict["definition_product"] == "50S ribosomal protein L4"
    assert conflict["historical_entity_scope"] == "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    assert conflict["rna_ancestor_path"] == [
        "ARO:3004956", "ARO:3005001", "ARO:3005003", "ARO:3000328",
    ]
    assert conflict["upstream_ontology_changed"] is False
    for audit in conflict["historical_audits"]:
        assert hashlib.sha256((ROOT / audit["path"]).read_bytes()).hexdigest() == audit["sha256"]


def test_primary_identity_prose_does_not_complete_resistance_review(dossier):
    context = dossier["primary_identity_context"]
    assert context["doi"] == "10.1371/journal.pone.0306695"
    assert context["section"] == "Introduction"
    assert context["paragraph_anchor"] == "article1.body1.sec1.p2"
    assert context["review_scope"] == "GENE_PRODUCT_IDENTITY_PROSE_ONLY"
    assert context["tables_or_supplements_reviewed"] is False
    assert context["phenotype_or_allele_validation"] is False
    assert dossier["source_claim"]["primary_resistance_review"] == "PENDING"


@pytest.mark.parametrize("index,field,count", [(0, "organism_id", 0), (1, "taxonomy_id", 2)])
def test_search_scope_and_completeness_are_explicit(dossier, index, field, count):
    search = dossier["searches"][index]
    params = search["parameters"]
    assert params["query"] == f"gene_exact:rplD AND {field}:485 AND reviewed:true"
    assert not {"sequence", "ft_variant", "ft_mutagen"} & set(params["fields"].split(","))
    assert search["complete_for_query"] is True
    assert search["result_count"] == len(search["accessions"]) == count
    request = search["request"]
    url = urlsplit(request["url"])
    assert url.hostname == "rest.uniprot.org" and url.path == "/uniprotkb/search"
    assert parse_qs(url.query) == {k: [v] for k, v in params.items()}
    assert request["status"] == 200 and request["release"] == "2026_03"
    assert dossier["candidate_interpretation"]["exact_organism_empty_is_gene_absence"] is False


@pytest.mark.parametrize("accession,locus,taxid,version,citation,strain", [
    ("B4RQX9", "NGK_2437", 521006, 89, "18586945", "NCCP11945"),
    ("Q5F5S8", "NGO_1837", 242231, 104, "CI-92V2JQAJ25B4S", "ATCC 700825 / FA 1090"),
])
def test_reference_loci_and_citation_strains_remain_separate(
    dossier, accession, locus, taxid, version, citation, strain,
):
    candidate, = [c for c in dossier["reference_candidates"]
                  if c["metadata"]["primaryAccession"] == accession]
    assert candidate["scope"] == "REFERENCE_METADATA_NOT_EXPERIMENTAL_ALLELE"
    metadata = candidate["metadata"]
    assert metadata["entryType"] == "UniProtKB reviewed (Swiss-Prot)"
    assert metadata["entryAudit"] == {"entryVersion": version, "sequenceVersion": 1}
    gene, = metadata["genes"]
    assert gene["geneName"]["value"] == "rplD"
    assert gene["orderedLocusNames"] == [{"value": locus}]
    assert gene["geneName"]["evidences"] == [
        {"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_01328"},
    ]
    assert metadata["organism"]["taxonId"] == taxid
    taxonomy = candidate["taxonomy"]
    assert taxonomy["taxonId"] == taxid and taxonomy["parent"]["taxonId"] == 485
    assert taxonomy["active"] is True and taxonomy["rank"] == "strain"
    assert taxonomy["scientificName"] == metadata["organism"]["scientificName"]
    context = candidate["citation_context"]
    assert context["citation"]["id"] == citation
    assert context["reference_comments"] == [{"type": "STRAIN", "value": strain}]
    assert context["primary_reference_reviewed"] is False
    assert candidate["card_cross_references"] == []


def test_shared_archive_metadata_is_not_a_representative_or_subject_join(dossier):
    candidates = dossier["reference_candidates"]
    assert len(candidates) == 2
    assert {c["uniparc_id"] for c in candidates} == {"UPI00004CE837"}
    interpretation = dossier["candidate_interpretation"]
    assert interpretation["shared_uniparc_is_experimental_identity"] is False
    assert interpretation["representative_selected"] is False
    assert interpretation["experimental_accessions_assigned"] is False
    assert dossier["source_claim"]["experimental_subject_join"] == "NOT_ESTABLISHED"
    assert dossier["source_claim"]["clinical_activity_join"] == "NOT_ESTABLISHED"


def test_source_owned_claim_and_exact_compound_are_preserved(dossier):
    source = dossier["source_claim"]
    with (ROOT / source["source_inventory"]["path"]).open() as handle:
        row, = [r for r in csv.DictReader(handle, delimiter="\t")
                if r["determinant_id"] == source["aro_id"]]
    assert row == source["source_row"]
    payload = json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(payload).hexdigest() == source["source_row_sha256"]
    record = load_record(ROOT / source["record"]["path"])
    assert record["identifier"] == source["identifier"] == "CHEBI:2955"
    assert record["chemical_structure"]["standard_inchi_key"] == source["standard_inchi_key"] == (
        "MQTOSJVFKKJCRP-BICOPXKESA-N")
    claim, = [r for r in record["resistance_mechanisms"] if r.get("aro_id") == source["aro_id"]]
    assert source["assertion_count"] == 1
    assert not {"gene_id", "protein_accession", "taxon_id", "strain", "strain_taxon_id"} & set(claim)


def test_export_remains_metadata_only_and_no_curation_is_claimed(dossier):
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
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers",
    }
    preservation = dossier["preservation"]
    assert preservation["record_hashes_verified"] == 2939
    assert preservation["protected_files_verified"] == 6458
    assert preservation["record_path_search_includes_ignored"] is True
    assert preservation["biological_record_changes"] == preservation["curation_events_added"] == 0
    assert "No NCBI request" in " ".join(dossier["limitations"])


def test_source_requests_are_pinned_and_do_not_use_ncbi(dossier):
    requests = [r["request"] for r in dossier["searches"]]
    requests += [c["taxonomy_request"] for c in dossier["reference_candidates"]]
    requests += [dossier["ontology_conflict"]["ontology_request"],
                 dossier["primary_identity_context"]["publisher_request"]]
    for request in requests:
        assert request["status"] == 200
        assert urlsplit(request["url"]).hostname in {
            "rest.uniprot.org", "raw.githubusercontent.com", "journals.plos.org",
        }
        assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64

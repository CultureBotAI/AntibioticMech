"""Reference proteins, gene-symbol collisions and donor/host roles stay distinct."""
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "research/2026-10-13-detox-reference-context.json"
EXPECTED = {
    "UniProtKB:P13249": ("pac", "NCBITaxon:132473", 94, 2, "REFERENCE_ONLY"),
    "UniProtKB:P0C2P0": ("bsd", "NCBITaxon:33178", 79, 1, "REFERENCE_ONLY"),
    "UniProtKB:P33967": ("bsr", "NCBITaxon:1396", 95, 1, "REFERENCE_ONLY"),
    "UniProtKB:A0KLG5": ("bsr", "NCBITaxon:380703", 130, 1, "EXCLUDE_UNRELATED_RACEMASE"),
}


def read(path=CONTEXT):
    return json.loads(path.read_bytes())


def check_scope(context):
    assert context["scope"] == "DETOX_REFERENCE_GROUNDING_NOT_RESISTANCE_CURATION"
    records = {r["identifier"]: r for r in context["records"]}
    assert len(records) == len(context["records"]) == 2
    assert records["CHEBI:17939"]["standard_inchi_key"] == "RXWNCPJZOCPEPQ-NVWDDTSBSA-N"
    assert records["CHEBI:15353"]["standard_inchi_key"] == "CXNPLSGKWMLZPZ-ZNIXKSQXSA-N"
    assert all(r["complete_collection_aware_record_loaded"] for r in records.values())
    hits = {}
    queries = context["protein_lookups"]
    assert [q["request"]["query"] for q in queries] == [
        "accession:P13249", "accession:P0C2P0", "gene_exact:bsr AND reviewed:true"]
    for query in queries:
        request = query["request"]
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert request["pagination_complete"] and request["total_results"] == len(query["hits"])
        url = urlsplit(request["url"])
        assert url.hostname == "rest.uniprot.org" and url.path == "/uniprotkb/search"
        params = parse_qs(url.query)
        assert params["query"] == [request["query"]] and params["size"] == ["10"]
        assert not {"sequence", "features"}.intersection(params["fields"][0].split(","))
        for row in query["hits"]:
            assert row["accession"] not in hits
            hits[row["accession"]] = row
            symbol, taxon, entry, sequence, disposition = EXPECTED[row["accession"]]
            assert row["gene_symbols"] == [symbol] and row["taxon_id"] == taxon
            assert (row["entry_version"], row["sequence_version"], row["disposition"]) == (
                entry, sequence, disposition)
            assert row["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
            assert not row["experimental_subject_assigned"]
            assert not {"sequence", "features", "referencePositions", "variant"}.intersection(row)
    assert set(hits) == set(EXPECTED)
    assert [q["request"]["total_results"] for q in queries] == [1, 1, 2]
    assert "racemase" in hits["UniProtKB:A0KLG5"]["protein_name"].lower()
    assert context["symbol_collision"]["relevant_reference"] == "UniProtKB:P33967"
    assert context["symbol_collision"]["excluded_hit"] == "UniProtKB:A0KLG5"
    taxa = context["taxonomy_references"]
    assert [(r["taxon_id"], r["scientific_name"]) for r in taxa] == [
        ("NCBITaxon:132473", "Streptomyces alboniger"),
        ("NCBITaxon:1396", "Bacillus cereus"), ("NCBITaxon:33178", "Aspergillus terreus")]
    for row in taxa:
        assert row["rank"] == "species" and not row["experimental_subject_assigned"]
        assert row["scope"] == "REFERENCE_SPECIES_NOT_EXPERIMENTAL_STRAIN"
        assert row["request"]["url"] == "https://rest.uniprot.org/taxonomy/" + row["taxon_id"].split(":")[1]
        assert row["request"]["status"] == 200 and row["request"]["release"] == "2026_03"
    sources = context["primary_sources"]
    assert [s["doi"] for s in sources] == ["10.1248/bpb.21.893", "10.1038/s41598-021-84551-9"]
    assert sources[0]["native_pages_visually_reviewed"] == list(range(1, 7))
    assert len(sources[0]["rendered_pages"]) == 6
    assert sources[1]["native_pages_visually_reviewed"] == sources[1]["rendered_pages"] == []
    assert all(s["status"] == 200 and s["full_text_cached"] and not s["supplements_reviewed"]
               for s in sources)
    assessments = context["assessments"]
    assert [(a["gene_symbol"], a["reference_protein"], a["reference_role"]) for a in assessments] == [
        ("pac", "UniProtKB:P13249", "ENZYME_ORIGIN"),
        ("bsr", "UniProtKB:P33967", "DONOR_REFERENCE"),
        ("bsd", "UniProtKB:P0C2P0", "DISTINCT_FUNGAL_COMPARATOR")]
    for row in assessments:
        assert row["record_id"] == ("CHEBI:17939" if row["gene_symbol"] == "pac" else "CHEBI:15353")
        assert row["reference_taxon"] == hits[row["reference_protein"]]["taxon_id"]
        assert row["disposition"].startswith("HOLD_")
        for field in ("experimental_protein_accession", "experimental_gene_locus_id", "experimental_taxon_id",
                      "experimental_strain_taxon_id", "experimental_genome_accession"):
            assert row[field] is None
        assert not any(row[f] for f in ("experimental_allele_assigned", "new_resistance_claim",
                                       "standardized_mic_extracted"))
    assert assessments[2]["primary_doi"] is None
    assert "not automatically equivalent" in context["chemical_scope"]
    limits = context["limits"]
    assert limits["records_in_scope"] == 2939 and limits["whole_corpus_status"] == "OPEN"
    assert limits["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in limits.items()
               if k not in {"records_in_scope", "whole_corpus_status", "issue_1040"})


def test_reference_context_preserves_subject_and_evidence_boundaries():
    check_scope(read())


def test_cached_lookup_projections_match_when_local_caches_available():
    context = read()
    requests = [q["request"] for q in context["protein_lookups"]]
    requests += [t["request"] for t in context["taxonomy_references"]]
    paths = [ROOT / r["cache"]["path"] for r in requests]
    if not all(p.exists() for p in paths):
        pytest.skip("Ignored historical request caches are not distributed with the repository")
    for request, path in zip(requests, paths, strict=True):
        assert hashlib.sha256(path.read_bytes()).hexdigest() == request["cache"]["sha256"]
        cached = read(path)
        assert cached["url"] == request["url"] and cached["status"] == request["status"]
        assert hashlib.sha256(cached["body"].encode()).hexdigest() == request["body_sha256"]
        assert cached["sha256"] == request["body_sha256"]
        body = json.loads(cached["body"])
        if "/uniprotkb/" in request["url"]:
            query, = [q for q in context["protein_lookups"] if q["request"] == request]
            assert [r["primaryAccession"] for r in body["results"]] == [
                h["accession"].split(":")[1] for h in query["hits"]]
        else:
            taxon, = [t for t in context["taxonomy_references"] if t["request"] == request]
            assert (body["taxonId"], body["scientificName"], body["rank"]) == (
                int(taxon["taxon_id"].split(":")[1]), taxon["scientific_name"], taxon["rank"])


@pytest.mark.parametrize("mutation", ["collision", "fungal_donor", "protein", "strain_taxon", "genome",
                                    "mic", "claim", "truncated", "strain_rank", "figure_review",
                                    "ncbi", "complete"])
def test_rejects_unsupported_promotions(mutation):
    context = copy.deepcopy(read())
    if mutation == "collision":
        context["symbol_collision"]["relevant_reference"] = "UniProtKB:A0KLG5"
    elif mutation == "fungal_donor":
        context["assessments"][2]["reference_role"] = "DONOR_REFERENCE"
    elif mutation == "protein":
        context["assessments"][1]["experimental_protein_accession"] = "UniProtKB:P33967"
    elif mutation == "strain_taxon":
        context["assessments"][1]["experimental_strain_taxon_id"] = "NCBITaxon:1396"
    elif mutation == "genome":
        context["assessments"][0]["experimental_genome_accession"] = "UNSUPPORTED"
    elif mutation == "mic":
        context["assessments"][1]["standardized_mic_extracted"] = True
    elif mutation == "claim":
        context["assessments"][1]["new_resistance_claim"] = True
    elif mutation == "truncated":
        context["protein_lookups"][2]["request"]["pagination_complete"] = False
    elif mutation == "strain_rank":
        context["taxonomy_references"][1]["rank"] = "strain"
    elif mutation == "figure_review":
        context["primary_sources"][1]["native_pages_visually_reviewed"] = [1]
    elif mutation == "ncbi":
        context["limits"]["ncbi_requests"] = 1
    else:
        context["limits"]["whole_corpus_status"] = "COMPLETE"
    with pytest.raises(AssertionError):
        check_scope(context)

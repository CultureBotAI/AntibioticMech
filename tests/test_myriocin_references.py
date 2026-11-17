"""A matching gene synonym is not an experimental resistance assignment."""

import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_myriocin_references as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / "research/2026-10-13-myriocin-reference-context.json").read_bytes())


def pinned_bytes(pin):
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    return raw


def test_historical_structure_and_exact_isp1_alias(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    census = list(csv.DictReader(io.StringIO(pinned_bytes(dossier["inputs"]["census"]).decode()),
                                delimiter="\t"))
    record = dossier["record"]
    row, = [r for r in census if r["identifier"] == "CHEBI:582124"]
    assert len(census) == 2939 and record["identifier"] == row["identifier"]
    assert record["sha256"] == row["record_sha256"] and record["path"] == row["path"]
    assert record["standard_inchi_key"] == row["standard_inchi_key"] == "ZZIKIHCNFWXKDY-GNTQXERDSA-N"
    assert row["resistance_assertions"] == "0"
    assert record["whole_record_review"] == "OPEN" and not record["resistance_assertions_added"]
    discovery = json.loads(pinned_bytes(dossier["inputs"]["discovery"]))
    lead, = [r for r in discovery["records"] if r["identifier"] == record["identifier"]]
    alias, = [n for n in lead["names"] if n["text"] == "ISP-1"]
    grounding = dossier["compound_name_grounding"]
    assert grounding["ISP-1"]["name_snapshot"] == alias
    assert grounding["ISP-1"]["synonym"] == {
        "synonym_text": "ISP-1", "synonym_type": "EXACT_SYNONYM", "source": "chebi"}
    assert not alias["shared_with_record_ids"]
    assert not grounding["tested_preparation_independently_reidentified"]


@pytest.mark.parametrize("accession,gene,version,sequence_version,locus,papers", [
    ("P53304", "SLI1", 149, 1, "YGR212W", ["15025559"]),
    ("P12688", "YPK1", 239, 2, "YKL126W", ["10825204", "15025559"]),
    ("P21965", "MCK1", 225, 1, "YNL307C", []),
])
def test_versioned_candidates_and_reference_taxonomy(dossier, accession, gene, version,
                                                    sequence_version, locus, papers):
    protein = dossier["reference_proteins"]["UniProtKB:" + accession]
    assert protein["primary_gene_name"] == gene and gene in protein["gene_names"]
    assert protein["entry_version"] == version and protein["sequence_version"] == sequence_version
    assert protein["ordered_locus_names"] == [locus]
    assert protein["reference_taxon_id"] == "NCBITaxon:559292"
    assert protein["source_species_taxon_id"] == "NCBITaxon:4932"
    assert protein["reference_taxon_rank"] == "strain" and protein["species_lineage_verified"]
    assert protein["focal_bibliography_matches"] == papers
    for key in ("exact_resistance_allele", "experimental_subject_assignment",
                "compound_specific_resistance_established"):
        assert not protein[key]
    assert all(not b["primary_results_reviewed"] for b in protein["bibliography"])
    if gene == "MCK1":
        assert protein["query_match_kind"] == "SYNONYM" and "YPK1" in protein["gene_names"]


@pytest.fixture
def ypk_candidates(dossier):
    return [copy.deepcopy(p) for p in dossier["reference_proteins"].values() if p["query_gene"] == "YPK1"]


def test_ypk1_sli2_resolved_without_discarding_homonym(dossier, ypk_candidates):
    expected = dossier["ypk1_name_resolution"]
    assert audit.resolve_ypk1(ypk_candidates) == expected
    assert audit.resolve_ypk1(list(reversed(ypk_candidates))) == expected
    assert expected["selected_reference"] == "UniProtKB:P12688"
    match = expected["candidates"]["UniProtKB:P12688"]
    homonym = expected["candidates"]["UniProtKB:P21965"]
    assert all(match["identity_checks"].values())
    assert not any(homonym["identity_checks"].values())
    assert homonym["disposition"] == "NOT_SUPPORTED_FOR_THIS_LEAD"
    assert not homonym["negative_resistance_phenotype_inferred"]
    assert not expected["experimental_allele_assignment"] and not expected["biological_claim_curated"]


@pytest.mark.parametrize("field,replacement", [
    ("primary_gene_name", "MCK1"), ("gene_names", ["YPK1"]),
    ("ordered_locus_names", []), ("focal_bibliography_matches", ["15025559"]),
])
def test_gene_name_alone_cannot_resolve_ypk1(ypk_candidates, field, replacement):
    match, = [p for p in ypk_candidates if p["primary_gene_name"] == "YPK1"]
    match[field] = replacement
    with pytest.raises(ValueError, match="unresolved or ambiguous"):
        audit.resolve_ypk1(ypk_candidates)


def test_multiple_concordant_candidates_are_not_arbitrarily_resolved(ypk_candidates):
    match, = [p for p in ypk_candidates if p["primary_gene_name"] == "YPK1"]
    other = copy.deepcopy(match)
    other["protein_accession"] = "UniProtKB:P00001"
    with pytest.raises(ValueError, match="unresolved or ambiguous"):
        audit.resolve_ypk1([*ypk_candidates, other])
    with pytest.raises(ValueError, match="duplicate"):
        audit.resolve_ypk1([*ypk_candidates, match])


def test_archive_crosswalk_stays_reference_only(dossier):
    crosswalk = dossier["sli1_archive_crosswalk"]
    assert crosswalk["source"] == "UNIPROT_ANNOTATION"
    assert crosswalk["links"] == [
        {"nucleotide_accession": "Z72997", "protein_accession": "CAA97239.1"},
        {"nucleotide_accession": "BK006941", "protein_accession": "DAA08306.1"},
    ]
    assert not crosswalk["experimental_subject_assignment"]
    assert crosswalk["new_archive_endpoint_requests"] == 0


def test_bounded_requests_and_taxonomy_reuse(dossier):
    assert set(dossier["uniprot_requests"]) == set(audit.QUERIES)
    for key, request in dossier["uniprot_requests"].items():
        url = urlparse(request["url"])
        assert url.scheme == "https" and url.netloc == "rest.uniprot.org"
        assert url.path == "/uniprotkb/search"
        assert parse_qs(url.query) == {"query": [audit.QUERIES[key]], "format": ["json"],
                                       "size": ["500"], "fields": [audit.reference.FIELDS]}
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert request["results"] == (1 if key == "sli1" else 2)
        assert request["complete_for_query"] and not request["all_strains_or_unreviewed_entries_searched"]
    old = json.loads(pinned_bytes(dossier["inputs"]["taxonomy_dossier"]))["taxonomy_request"]
    reused = dossier["taxonomy_request"]
    assert all(reused[k] == v for k, v in old.items())
    assert reused["reused_byte_identically"] and not reused["new_request"]


def test_access_limits_and_no_completion_or_operational_payload(dossier):
    assert [s["outcome"] for s in dossier["primary_access"]] == [
        "HTTP_403_NON_PDF_BODY", "TOOL_REPORTED_URL_INACCESSIBLE", "CLIENT_CHALLENGE_NOT_ARTICLE_TEXT"]
    assert dossier["primary_access"][0]["status"] == 403
    assert all(not p["primary_results_verified"] and not p["retry_or_alternate_transport"]
               for p in dossier["primary_access"])
    summary = dossier["summary"]
    assert summary["corpus_records_in_scope"] == 2939 and summary["reference_candidates"] == 3
    assert summary["concordant_reference_identities"] == 2
    assert summary["homonym_candidates_not_supported_for_lead"] == 1
    for key in ("new_taxonomy_requests", "biological_records_changed", "new_phi_decisions",
                "experimental_accessions_assigned", "whole_records_completed"):
        assert summary[key] == 0
    previous = json.loads(pinned_bytes(dossier["inputs"]["prior_progress"]))
    assert previous["summary"]["phi_identifier_scoped_associations"] == 190
    assert previous["summary"]["phi_identifier_review_pending"] == 27
    pinned_bytes(dossier["inputs"]["prior_checkpoint"])
    forbidden = {"sequence", "features", "alteration", "variants", "mic", "construct", "protocol"}

    def check(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                check(child)
        elif isinstance(value, list):
            for child in value:
                check(child)

    check(dossier)

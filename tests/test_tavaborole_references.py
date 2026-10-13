"""Reference compartments and taxonomy must not become resistance assignments."""

import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "research/2026-10-13-tavaborole-reference-context.json"


@pytest.fixture
def dossier():
    return json.loads(PUBLIC.read_bytes())


def test_record_identity_is_pinned_to_historical_census(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    pin = dossier["inputs"]["census"]
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    rows = list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))
    assert len(rows) == dossier["summary"]["corpus_records_in_scope"] == 2939
    row = next(r for r in rows if r["identifier"] == "CHEBI:77942")
    for field in ("identifier", "path", "standard_inchi_key"):
        assert dossier["record"][field] == row[field]
    assert dossier["record"]["sha256"] == row["record_sha256"]
    assert dossier["record"]["standard_inchi_key"] == "LFQDNHWZDQTITF-UHFFFAOYSA-N"
    assert int(row["resistance_assertions"]) == 0


@pytest.mark.parametrize(
    "key,accession,version,locus,compartment,role",
    [
        ("cdc60", "P26637", 206, "YPL160W", "cytoplasmic", "CYTOPLASMIC_REFERENCE_ONLY"),
        ("nam2", "P11325", 201, "YLR382C", "mitochondrial", "MITOCHONDRIAL_COMPARATOR_NOT_CDC60"),
    ],
)
def test_distinct_reference_identities(dossier, key, accession, version, locus, compartment, role):
    reference = dossier["reference_proteins"][key]
    assert reference["protein_accession"] == "UniProtKB:" + accession
    assert reference["entry_version"] == version and reference["sequence_version"] == 1
    assert reference["ordered_locus_names"] == [locus]
    assert reference["protein_name"] == "Leucine--tRNA ligase, " + compartment
    assert reference["role"] == role and key.upper() in reference["gene_names"]
    assert reference["reference_taxon_id"] == "NCBITaxon:559292"
    assert reference["reference_taxon_rank"] == "strain"
    assert reference["source_species_taxon_id"] == "NCBITaxon:4932"
    assert reference["species_lineage_verified"]
    assert not reference["experimental_subject_assignment"]
    assert not reference["exact_resistance_allele"]
    assert not reference["compound_specific_resistance_established"]
    assert reference["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"


def test_query_completeness_is_not_all_gene_or_all_strain_coverage(dossier):
    assert set(dossier["queries"]) == {"cdc60", "nam2"}
    for key, query in dossier["queries"].items():
        assert query["results"] == 1 and query["complete_for_exact_query"]
        assert not query["all_strains_or_unreviewed_entries_searched"]
        assert not query["establishes_biological_absence"]
        request = query["request"]
        assert request["status"] == 200 and request["release"] == "2026_03"
        parsed = urlparse(request["url"])
        assert parsed.scheme == "https" and parsed.netloc == "rest.uniprot.org"
        assert parsed.path == "/uniprotkb/search" and not parsed.fragment
        params = parse_qs(parsed.query)
        assert params["query"] == [f"(gene_exact:{key.upper()}) AND (organism_id:559292) AND (reviewed:true)"]
        assert params["size"] == ["500"] and params["format"] == ["json"]
        assert params["fields"] == [
            "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
            "xref_embl,xref_refseq,lit_pubmed_id,sequence_version,version"
        ]
    taxonomy = dossier["taxonomy_request"]
    assert taxonomy["url"] == "https://rest.uniprot.org/taxonomy/559292"
    assert taxonomy["status"] == 200 and taxonomy["release"] == "2026_03"


def test_access_and_bibliography_holds_do_not_promote_primary_review(dossier):
    holds = {h["doi"]: h for h in dossier["primary_access"]}
    assert set(holds) == {"10.1038/s42003-022-03076-7", "10.1126/science.1142189"}
    assert holds["10.1126/science.1142189"]["reported_http_status"] == 403
    assert holds["10.1038/s42003-022-03076-7"]["status"] == "TOOL_INACCESSIBLE_IDENTITY_PROVIDER_REDIRECT"
    for hold in holds.values():
        assert not hold["primary_results_reviewed"]
        assert not hold["retried_or_alternate_transport_used"]
    for reference in dossier["reference_proteins"].values():
        assert reference["focal_paper_in_entry_bibliography"] == dict.fromkeys(holds, False)
        ids = {
            f"{item['database']}:{item['id']}".casefold()
            for citation in reference["bibliography"]
            for item in citation["identifiers"]
        }
        assert not ids.intersection(f"doi:{doi}".casefold() for doi in holds)
        assert all(not c["primary_results_reviewed"] for c in reference["bibliography"])
    assert dossier["preexisting_target_mechanism"] == "PRESERVED_NOT_REVALIDATED_IN_THIS_FOLLOWUP"


def test_no_experimental_assignments_or_operational_payload(dossier):
    assert dossier["resistance_assertions_added"] == []
    assert dossier["experimental_subjects_assigned"] == []
    assert dossier["scope"] == "S288C_REFERENCE_IDENTITIES_NOT_EXPERIMENTAL_SUBJECTS"
    for key in ("biological_records_changed", "experimental_accessions_assigned", "whole_records_completed"):
        assert dossier["summary"][key] == 0
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

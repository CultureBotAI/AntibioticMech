"""Keep isozyme metadata, compound identity and experimental evidence separate."""

import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "research/2026-10-13-chitin-synthase-context.json"


@pytest.fixture
def dossier():
    return json.loads(PUBLIC.read_bytes())


def pinned_bytes(pin):
    raw = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
    return raw


def test_distinct_historical_structures_and_exact_alias(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    census = list(csv.DictReader(io.StringIO(pinned_bytes(dossier["inputs"]["census"]).decode()),
                                delimiter="\t"))
    assert len(census) == 2939
    expected = {"CHEBI:623918": "WWJFFVUVFNBJTN-VHDFTHOZSA-N",
                "CHEBI:78777": "JPFWJDMDPLEUBD-ITJAGOAWSA-N"}
    assert set(dossier["records"]) == set(expected)
    for identifier, key in expected.items():
        record = dossier["records"][identifier]
        row, = [r for r in census if r["identifier"] == identifier]
        assert record["standard_inchi_key"] == row["standard_inchi_key"] == key
        assert record["sha256"] == row["record_sha256"] and record["path"] == row["path"]
        assert row["resistance_assertions"] == "0"
        assert record["whole_record_review"] == "OPEN" and not record["resistance_assertions_added"]
    aliases = json.loads(pinned_bytes(dossier["inputs"]["alias_discovery"]))
    row, = [r for r in aliases["records"] if r["identifier"] == "CHEBI:78777"]
    alias, = [n for n in row["names"] if n["text"] == "Polyoxin D"]
    grounding = dossier["compound_name_grounding"]
    assert grounding["Polyoxin D"]["name_snapshot"] == alias
    assert alias["origins"] == [{"index": 1, "kind": "SYNONYM", "source": "chebi",
                                 "synonym_type": "EXACT_SYNONYM"}]
    assert not alias["shared_with_record_ids"]
    assert not grounding["findings_transferred_between_compounds"]
    assert not grounding["tested_preparations_independently_reidentified"]


@pytest.mark.parametrize("gene,accession,version,sequence_version,locus", [
    ("CHS1", "P08004", 209, 2, "YNL192W"),
    ("CHS2", "P14180", 212, 1, "YBR038W"),
    ("CHS3", "P29465", 209, 3, "YBR023C"),
])
def test_reference_isozymes_are_not_experimental_alleles(
    dossier, gene, accession, version, sequence_version, locus,
):
    reference = dossier["reference_proteins"][gene]
    assert reference["protein_accession"] == "UniProtKB:" + accession
    assert reference["entry_version"] == version and reference["sequence_version"] == sequence_version
    assert reference["ordered_locus_names"] == [locus] and gene in reference["gene_names"]
    assert reference["role"] == "REFERENCE_ISOZYME_NOT_ACQUIRED_RESISTANCE_ALLELE"
    assert reference["reference_taxon_id"] == "NCBITaxon:559292"
    assert reference["reference_taxon_rank"] == "strain"
    assert reference["source_species_taxon_id"] == "NCBITaxon:4932"
    assert reference["species_lineage_verified"]
    for field in ("exact_resistance_allele", "experimental_subject_assignment",
                  "experimental_backgrounds_collapsed_to_reference_strain",
                  "focal_citation_in_returned_bibliography"):
        assert not reference[field]
    ids = {i["id"].lower() for b in reference["bibliography"] for i in b["identifiers"]}
    assert dossier["primary"]["pmid"] not in ids and dossier["primary"]["doi"] not in ids
    if gene == "CHS3":
        assert {"CAL1", "CSD2", "DIT101", "KIT2"} <= set(reference["gene_names"])
        assert "DITJOJ" not in reference["gene_names"]


def test_evidence_scopes_and_unreviewed_figures_remain_explicit(dossier):
    findings = {f["key"]: f for f in dossier["findings"]}
    assert findings["nikkomycin_biochemical"]["scope"] == "BIOCHEMICAL_INHIBITION_NOT_ORGANISM_AST"
    assert findings["nikkomycin_growth"]["scope"] == "REPORTED_ISOZYME_CONTEXT_NOT_ACQUIRED_ALLELE"
    assert findings["polyoxin_contrast"]["identifier"] == "CHEBI:78777"
    assert findings["control_scope"]["scope"] == "NO_CROSS_COMPOUND_RESISTANCE_PROPAGATION"
    assert all(not f["curation_admitted"] for f in findings.values())
    primary = dossier["primary"]
    assert primary["doi"] == "10.1128/jb.176.18.5857-5860.1994"
    assert primary["pdf_text_inspected"] and primary["cached_text_read_after_visual_timeout"]
    for key in ("local_pdf_saved", "native_figures_visually_inspected", "whole_article_review_complete",
                "failed_visual_request_retried", "alternate_transport_used_after_visual_failure"):
        assert not primary[key]
    assert [a["status"] for a in primary["visual_attempts"]] == [
        "TOOL_RETURNED_REFERENCE_WITHOUT_VISIBLE_IMAGE", "TOOL_TIMEOUT"]
    context = dossier["organism_context"]
    assert context["named_taxon_id"] == "NCBITaxon:4932" and context["rank"] == "species"
    assert context["taxon_id_source"] == "UNIPROT_LINEAGE_NOT_VERIFIED_AS_ARTICLE_REPORTED"
    assert not context["all_tested_subjects_assigned_to_s288c"]
    assert context["experimental_strain_sample_genome_and_allele_links"] == "UNRESOLVED_NOT_ASSERTED_ABSENT"


def test_bounded_requests_and_byte_identical_taxonomy_reuse(dossier):
    expected = {
        "chs2": "gene_exact:CHS2 AND organism_id:559292 AND reviewed:true",
        "comparators": "(gene_exact:CHS1 OR gene_exact:CHS3) AND organism_id:559292 AND reviewed:true",
    }
    assert set(dossier["uniprot_requests"]) == set(expected)
    for key, request in dossier["uniprot_requests"].items():
        url = urlparse(request["url"])
        assert url.scheme == "https" and url.netloc == "rest.uniprot.org"
        assert url.path == "/uniprotkb/search"
        params = parse_qs(url.query)
        assert params["query"] == [expected[key]]
        assert "sequence" not in params["fields"][0].split(",")
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert request["complete_for_query"] and not request["all_strains_or_unreviewed_entries_searched"]
    previous = json.loads(pinned_bytes(dossier["inputs"]["taxonomy_dossier"]))["taxonomy_request"]
    reused = dossier["taxonomy_request"]
    assert reused["reused_byte_identically"] and not reused["new_request"]
    assert all(reused[k] == v for k, v in previous.items())


def test_phi_queue_and_completion_use_historical_progress(dossier):
    previous = json.loads(pinned_bytes(dossier["inputs"]["prior_progress"]))
    queue, counts = dossier["phi_queue_recheck"], previous["summary"]
    assert queue["source_associations"] == counts["phi_source_associations"] == 217
    assert queue["identifier_scoped_associations"] == counts["phi_identifier_scoped_associations"] == 190
    assert queue["pending_associations"] == counts["phi_identifier_review_pending"] == 27
    assert sum(queue["pending_pmids"].values()) == 27
    assert len(queue["pending_pmids"]) == queue["pending_papers"] == 11
    assert queue["new_decisions"] == 0
    for field in ("biological_records_changed", "experimental_accessions_assigned",
                  "whole_records_completed"):
        assert dossier["summary"][field] == 0
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

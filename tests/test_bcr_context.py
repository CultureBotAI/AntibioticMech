"""Keep Bcr references, assay endpoints and the curated Rho example distinct."""

import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-bcr"


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


@pytest.fixture(scope="module")
def context():
    return read("-context.json")


@pytest.fixture(scope="module")
def receipt():
    return read("-curation.json")


def assert_pin(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    assert set(value) == set(keys)
    return {key: copy.deepcopy(value[key]) for key in keys}


def test_historical_record_transition_is_scoped_and_reproducible(context, receipt, tmp_path):
    fixture = assert_pin(receipt["fixture"])
    before = context["records_before"][0]
    assert hashlib.sha256(fixture).hexdigest() == before["sha256"] == receipt["before"]["sha256"]
    assert before["path"] == receipt["before"]["path"] == receipt["record"]["path"]
    record = load_record(ROOT / receipt["fixture"]["path"])
    original = copy.deepcopy(record)
    target, = [t for t in record["molecular_targets"] if t.get("source") == "PRIMARY_LITERATURE"]
    target.update(ordered(receipt["added_target_taxon"], ("taxon_id", "taxon_label")))
    target["protein_examples"] = [ordered(receipt["protein_example"], (
        "uniprot_id", "protein_label", "gene_symbol", "taxon_id", "taxon_label",
        "entry_status", "retrieved_on", "role",
    ))]
    target["evidence"].append(ordered(receipt["added_evidence"], ("reference", "notes")))
    record["curation_history"].append(ordered(receipt["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted",
    )))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(record, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == receipt["record"]["sha256"]
    assert build_document(original, role_names()) == build_document(record, role_names())
    assert record["molecular_targets"][0] == original["molecular_targets"][0]
    for key in original.keys() - {"molecular_targets", "curation_history"}:
        assert record[key] == original[key]
    assert len(record["curation_history"]) == len(original["curation_history"]) + 1
    assert receipt["records_changed"] == receipt["history_events_added"] == 1


def test_historical_replay_does_not_freeze_live_record(context, receipt, tmp_path, monkeypatch):
    original = Path.open
    live = ROOT / receipt["record"]["path"]

    def no_live_record(path, *args, **kwargs):
        assert path != live, "dated curation replay read the evolving live record"
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", no_live_record)
    test_historical_record_transition_is_scoped_and_reproducible(context, receipt, tmp_path)


@pytest.mark.parametrize("field", ["example", "evidence", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(context, receipt, tmp_path, field):
    candidate = copy.deepcopy(receipt)
    if field == "example":
        candidate["protein_example"]["uniprot_id"] = "UniProtKB:P28246"
    elif field == "evidence":
        candidate["added_evidence"]["reference"] = "PDB:1XPU"
    elif field == "event":
        candidate["curation_event"]["changes"] += " Unsupported change."
    else:
        candidate["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        test_historical_record_transition_is_scoped_and_reproducible(context, candidate, tmp_path)


@pytest.mark.parametrize("gene,acc,loci,entry,sequence", [
    ("bcr", "P28246", ["b2182", "JW5363"], 179, 4),
    ("folP", "P0AC13", ["b3177", "JW3144"], 147, 1),
    ("rho", "P0AG30", ["b3783", "JW3756"], 164, 1),
])
def test_versioned_reference_identity(context, gene, acc, loci, entry, sequence):
    row = context["reference_proteins"][gene]
    assert row["canonical_gene"] == gene and row["protein_accession"] == "UniProtKB:" + acc
    assert row["ordered_locus_names"] == loci
    assert (row["entry_version"], row["sequence_version"]) == (entry, sequence)
    assert row["reviewed"] and row["reference_taxon_id"] == "NCBITaxon:83333"
    assert row["scope"] == "REFERENCE_IDENTITY_NOT_RESISTANCE_ALLELE"
    assert not row["experimental_resistance_assignment"]
    request = row["request"]
    assert request["status"] == 200 and request["release"] == "2026_03"
    assert request["pagination_complete"] and request["result_count"] == request["total_results"] == 1
    url = urlsplit(request["url"])
    assert (url.scheme, url.hostname, url.path) == ("https", "rest.uniprot.org", "/uniprotkb/search")
    query = parse_qs(url.query)
    expected = ("accession:P28246" if gene == "bcr" else
                f"gene_exact:{gene} AND organism_id:83333 AND reviewed:true")
    assert query["query"] == [expected]
    assert "sequence" not in query["fields"][0].split(",")


def test_card_bcr1_is_not_replaced_with_ecoli_bcr(context):
    card = context["historical_card"]
    snapshot = json.loads(assert_pin(card["source"]))
    assert snapshot["determinants"]["ARO:3003801"]["candidates"] == [card["candidate"]]
    candidate = card["candidate"]
    assert candidate["accession"] == "UniProtKB:A0A3S4ND58"
    assert candidate["reference_taxon_id"] == "NCBITaxon:294"
    assert candidate["genes"][0]["geneName"]["value"] == "bcr_2"
    assert candidate["gene_name_comparison"] == "NAMES_DIFFER_REVIEW_REQUIRED"
    assert candidate["pubmed_ids"] == []
    assert not card["interchangeable_with_ecoli_bcr"] and not card["requeried_this_checkpoint"]
    citations = json.loads(assert_pin(card["citation_source"]))["proteins"]
    assert card["citation_context"] == citations[candidate["accession"]]
    assert card["citation_context"]["reference_contexts"][0]["citation"]["citationType"] == "submission"
    assert context["reference_proteins"]["bcr"]["returned_card_ids"] == []


def test_primary_citation_asymmetry_aliases_and_endpoints(context):
    primary = context["primary_context"]
    assert primary["reference"] == "PMID:9449266" and primary["doi"] == "10.1128/aac.42.1.88"
    assert primary["paper_explicitly_cites_bcr_accession"]
    assert not primary["current_bcr_bibliography_cites_this_paper"]
    assert not primary["current_folp_bibliography_cites_this_paper"]
    refs = context["reference_proteins"]
    assert {"sur", "suxA"} <= set(refs["bcr"]["aliases"])
    assert "sux" not in refs["bcr"]["aliases"]
    findings = " ".join(f["finding"] for f in primary["findings"])
    assert "distinct unresolved modifier" in findings and "not an experimental allele" in findings
    assert "single determinant does not account" in findings
    figure = primary["figure_1"]
    assert figure["visually_inspected"] and figure["endpoint"] == "BIOCHEMICAL_ENZYME_ACTIVITY_NOT_MIC"
    assert figure["status"] == 200 and figure["sha256"] == figure["cache"]["sha256"]
    assert figure["content_type"].startswith("image/jpeg")
    policy = primary["measurement_policy"]
    assert policy["preferred_mic_unit"] == "mg/L" and policy["ug_per_mL_conversion_factor"] == 1
    assert not policy["enzyme_inhibition_converted_to_mic"] and not policy["clinical_category_inferred"]
    assert not primary["whole_paper_review_complete"] and not primary["native_pdf_inspected"]
    lead = context["bicyclomycin_bcr_lead"]
    assert lead["returned_bcr_bibliography_cites_paper"] and not lead["whole_paper_review_complete"]


def test_rho_reference_example_has_exact_compound_and_entity_support(context, receipt):
    row = context["rho_structure"]
    assert (row["identifier"], row["entity_id"], row["entry_version"]) == ("PDB:1XPO", "2", "1.4")
    assert row["method"] == "X-ray" and row["resolution_angstrom"] == 3.15
    assert row["protein_accession"] == receipt["protein_example"]["uniprot_id"] == "UniProtKB:P0AG30"
    assert row["source_taxon_id"] == receipt["added_target_taxon"]["taxon_id"] == "NCBITaxon:562"
    assert row["reference_taxon_id"] == receipt["protein_example"]["taxon_id"] == "NCBITaxon:83333"
    assert row["primary_reference"] == "PMID:15642265"
    assert row["primary_reference"] in context["reference_proteins"]["rho"]["returned_pubmed_ids"]
    assert row["primary_doi"] == "10.1016/j.str.2004.10.013"
    assert row["ligand"]["component_id"] == "BCM" and row["ligand"]["inchi_exact_match"]
    assert row["ligand"]["standard_inchi_key"] == context["records_before"][0]["standard_inchi_key"]
    assert row["ligand"]["standard_inchi_key"] == "WOUDXEYYJPOSNE-VKZDFBPFSA-N"
    assert not row["single_accession_identifies_whole_complex"]
    assert not row["reference_taxon_is_experimental_strain"] and not row["resistance_allele_assignment"]
    assert not row["new_atomic_contact_analysis"] and not row["new_primary_fulltext_or_native_figure_review"]
    assert "not the whole complex or a resistance allele" in receipt["protein_example"]["role"]
    assert len(row["requests"]) == 3
    for request in row["requests"]:
        assert request["status"] == 200 and request["sha256"] == request["cache"]["sha256"]
        assert urlsplit(request["url"]).hostname == "data.rcsb.org"
        assert not request["redirects_followed"]


def test_taxonomy_is_reused_and_not_an_experimental_join(context):
    predecessor = json.loads(assert_pin(context["taxonomy_predecessor"]))
    assert context["taxonomy"] == predecessor["taxonomy"]
    taxa = {t["taxon_id"]: t for t in context["taxonomy"]}
    assert taxa["NCBITaxon:83333"]["parent_taxon_id"] == "NCBITaxon:562"
    assert taxa["NCBITaxon:83333"]["rank"] == "strain"
    assert taxa["NCBITaxon:562"]["rank"] == "species"
    assert all(t["reused_cache"] and t["active"] for t in taxa.values())


def test_rendered_evidence_retains_reference_only_caveat(receipt):
    # The current page template renders evidence notes, not ProteinExample.role.
    note = receipt["added_evidence"]["notes"]
    assert "K-12 is reference context, not an assigned experimental strain" in note
    assert "one subunit, not the whole complex" in note


def test_discovery_memberships_are_not_new_search_or_review(context):
    discovery = context["discovery"]
    source = json.loads(assert_pin(discovery["source"]))
    memberships = []
    for row in source["records"]:
        if row["identifier"] not in {"CHEBI:60584", "CHEBI:9337"}:
            continue
        for query in row["queries"]:
            for candidate in query.get("candidates", []):
                if candidate.get("pmid") in {"8486276", "9449266"}:
                    memberships.append({"record": row["identifier"], "query_id": query["query_id"],
                                        "candidate": candidate})
    assert discovery["memberships"] == memberships and len(memberships) == 5
    assert not discovery["new_discovery_search"] and not discovery["historical_export_modified"]


def test_census_changes_only_the_curated_record_hash(context, receipt):
    reconciliation = read("-reconciliation.json")
    censuses = []
    for key in ("previous_census", "current_census"):
        payload = assert_pin(reconciliation[key])
        rows = list(csv.DictReader(payload.decode().splitlines(), delimiter="\t"))
        by_id = {r["identifier"]: r for r in rows}
        assert len(rows) == len(by_id) == 2939
        censuses.append(by_id)
    before, after = censuses
    assert set(before) == set(after)
    assert [i for i in before if before[i] != after[i]] == ["CHEBI:60584"]
    assert after["CHEBI:60584"] == {**before["CHEBI:60584"], "record_sha256": receipt["record"]["sha256"]}
    for record in context["records_before"]:
        row = before[record["identifier"]]
        assert (record["path"], record["sha256"], record["standard_inchi_key"]) == (
            row["path"], row["record_sha256"], row["standard_inchi_key"],
        )
        assert record["whole_record_review"] == "OPEN"
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4851
    assert reconciliation["records_byte_identical"] == 2938


def test_no_resistance_completion_or_ncbi_scope_inflation(context, receipt):
    limits = context["limits"]
    assert limits["issue_1040"] == "DEFERRED"
    assert not any(value for key, value in limits.items() if key != "issue_1040")
    assert receipt["new_target_protein_examples"] == 1
    assert receipt["new_resistance_claims"] == receipt["new_measurements"] == 0
    assert not receipt["whole_record_review_complete"]
    assert receipt["existing_target_identity_and_primary_claim_retained"]
    assert receipt["card_and_mibig_assertions_preserved"] and receipt["embedded_document_unchanged"]

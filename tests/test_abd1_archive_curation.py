"""Archived reference identity does not identify a resistant experimental subject."""
import copy
import csv
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names
from scripts.render_pages import TEMPLATES_DIR, build_record

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-abd1"


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


def pinned(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    assert set(value) == set(keys)
    return {key: copy.deepcopy(value[key]) for key in keys}


def replay(item, tmp_path):
    context = read("-context.json")["record_before"]
    assert hashlib.sha256(pinned(item["fixture"])).hexdigest() == item["before"]["sha256"]
    assert item["before"] == {key: context[key] for key in ("path", "sha256")}
    assert item["record"]["path"] == item["before"]["path"]
    before = load_record(ROOT / item["fixture"]["path"])
    assert before["identifier"] == item["identifier"] == "CHEBI:45453"
    assert before["chemical_structure"]["standard_inchi_key"] == context["standard_inchi_key"]
    after = copy.deepcopy(before)
    claims = [ordered(c, ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label",
                         "phenotype_label", "assay", "note", "evidence")) for c in item["claims"]]
    for claim in claims:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after["resistance_mechanisms"].extend(claims)
    after["curation_history"].append(ordered(item["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(after, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == item["record"]["sha256"]
    assert len(before["resistance_mechanisms"]) == item["existing_claims_preserved"] == 4
    assert after["resistance_mechanisms"][:-1] == before["resistance_mechanisms"]
    assert after["curation_history"][:-1] == before["curation_history"]
    keep = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in keep} == {k: after[k] for k in keep}
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


def test_dated_replay_preserves_prior_claims_without_reading_live_record(tmp_path, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(read("-curation.json"), tmp_path)


@pytest.mark.parametrize("field", ["route", "reference", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(field, tmp_path):
    item = read("-curation.json")
    if field == "route":
        item["claims"][0]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif field == "reference":
        item["claims"][0]["evidence"][1]["notes"] += " Same experimental subject."
    elif field == "event":
        item["curation_event"]["changes"] += " Unsupported edit."
    else:
        item["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


def test_archive_preserves_inactive_and_current_reference_strains():
    context = read("-context.json")
    deleted = context["uniprot"]["A6ZLH5"]["reference"]
    assert deleted["entry_status"] == "DELETED"
    assert deleted["reason"] == "Not part of a reference proteome"
    assert not deleted["replacement_accession_reported"]
    archive = context["archive"]
    assert archive["identifier"] == deleted["archive"] == "UPI000005318F"
    assert archive["page_counts"] == [100, 76] and archive["total_cross_references"] == 176
    assert len(archive["pages"]) == 2 and archive["pagination_complete"]
    assert archive["distinct_accession_version_keys"] == 172 and archive["distinct_dated_intervals"] == 176
    assert not archive["historical_intervals_collapsed"]
    assert archive["reference_sequence_equivalence_supported"]
    for key in ("strain_equivalence_supported", "experimental_allele_equivalence_supported",
                "genome_or_subject_join_supported", "sequence_downloaded"):
        assert not archive[key]
    historical, current = archive["selected_cross_references"]
    assert (historical["id"], historical["active"], historical["organism"]["taxonId"]) == (
        "A6ZLH5", False, 307796)
    assert (current["id"], current["active"], current["organism"]["taxonId"]) == ("P32783", True, 559292)
    assert all(row["geneName"] == "ABD1" and row["version"] == row["versionI"] == 1
               for row in (historical, current))
    assert context["uniprot"]["P32783"] == json.loads(pinned(context["predecessor"]))["uniprot"]["ABD1"]
    donor = context["uniprot"]["Q6CKI0"]["reference"]
    assert donor["entry_status"] == "REVIEWED" and donor["taxon_id"] == "NCBITaxon:284590"
    assert (donor["entry_version"], donor["sequence_version"]) == (114, 1)
    assert donor["gene"] == "ABD1" and donor["ordered_locus_names"] == ["KLLA0F10527g"]
    assert not donor["organismal_resistance_demonstrated"]


def test_taxonomy_is_reference_context_not_an_experimental_join():
    context = read("-context.json")
    assert context["taxonomy"]["reused"] == json.loads(pinned(context["predecessor"]))["taxonomy"]
    rows = context["taxonomy"]["new"]
    assert [(r["taxon_id"], r["rank"], r["parent_taxon_id"]) for r in rows] == [
        ("NCBITaxon:307796", "strain", "NCBITaxon:4932"),
        ("NCBITaxon:284590", "strain", "NCBITaxon:28985"),
        ("NCBITaxon:28985", "species", "NCBITaxon:4910")]
    subject = context["subject_scope"]
    assert subject["taxon_id"] == "NCBITaxon:4932"
    assert all(not value for key, value in subject.items() if key not in {"taxon_id", "taxon_label"})


def test_new_association_does_not_rewrite_the_earlier_context():
    item = read("-curation.json")
    claim, = item["claims"]
    assert claim["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
    assert claim["gene_id"] == "ABD1" and claim["taxon_id"] == "NCBITaxon:4932"
    assert "not the earlier expression-context finding" in claim["note"]
    assert "not organismal resistance evidence" in claim["note"]
    assert claim["evidence"][0]["reference"] == "PMID:40682821"
    assert "not standardized MICs" in claim["evidence"][0]["notes"]
    assert "does not establish strain or experimental-allele equivalence" in claim["evidence"][1]["notes"]
    assert "Not assigned as an experimental resistance protein" in claim["evidence"][2]["notes"]
    forbidden = {"protein_accession", "strain", "strain_taxon_id", "alteration", "gene_families",
                 "assembly_accession", "biosample_accession", "mic", "mic_value", "sequence", "variant"}
    assert not forbidden.intersection(claim)
    assert item["existing_claims_preserved"] == 4 and not item["whole_record_review_complete"]


def test_primary_review_limits_and_deferral():
    context = read("-context.json")
    primary = context["primary"]
    assert primary["reference"] == "PMID:40682821" and primary["doi"] == "10.1093/nar/gkaf538"
    assert primary["native_figures_inspected"] == [2, 3, 4, 7]
    assert not primary["whole_paper_review_complete"] and not primary["supplement_review_complete"]
    assert all(f["status"] == 200 and "?" not in f["url"] for f in primary["figures"])
    assert "untested predictions" in primary["limits"]
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not value for key, value in context["limits"].items() if key != "issue_1040")
    assert context["disposition"]["whole_record_reviews_completed"] == 0


class PageText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.excluded = None

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.excluded = tag

    def handle_endtag(self, tag):
        if tag == self.excluded:
            self.excluded = None

    def handle_data(self, data):
        if self.excluded is None:
            self.parts.append(data)


def test_reference_caveats_survive_real_adapter_and_template(tmp_path):
    item = read("-curation.json")
    doc = replay(item, tmp_path)
    record = build_record(ROOT / item["record"]["path"], doc, {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    claim, = item["claims"]
    for expected in (claim["label"], claim["note"], *(e["notes"] for e in claim["evidence"])):
        assert " ".join(expected.split()) in text


def test_dated_census_preserves_every_other_row():
    receipt = read("-reconciliation.json")
    rows = [csv.DictReader(pinned(receipt[key]).decode().splitlines(), delimiter="\t")
            for key in ("previous_census", "current_census")]
    before, after = [{r["identifier"]: r for r in values} for values in rows]
    assert before.keys() == after.keys() and len(after) == 2939
    assert [key for key in before if before[key] != after[key]] == ["CHEBI:45453"]
    assert before["CHEBI:45453"]["resistance_assertions"] == "4"
    assert after["CHEBI:45453"]["resistance_assertions"] == "5"
    assert after["CHEBI:45453"]["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4871
    assert receipt["records_byte_identical"] == 2938 and receipt["new_gene_associations"] == 1

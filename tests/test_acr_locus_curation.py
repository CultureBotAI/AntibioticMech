"""Historical loci are not modern alias matches or class-wide phenotypes."""
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
PREFIX = ROOT / "research/2026-10-13-acr"
IDS = ("CHEBI:2450", "CHEBI:315018", "CHEBI:569624")


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


def pinned(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    assert set(value) == set(keys)
    return {k: copy.deepcopy(value[k]) for k in keys}


def replay(item, tmp_path):
    context = next(r for r in read("-context.json")["records_before"]
                   if r["identifier"] == item["identifier"])
    assert hashlib.sha256(pinned(item["fixture"])).hexdigest() == item["before"]["sha256"]
    assert item["before"] == {k: context[k] for k in ("path", "sha256")}
    assert item["record"]["path"] == item["before"]["path"]
    before = load_record(ROOT / item["fixture"]["path"])
    assert before["identifier"] == item["identifier"]
    assert before["chemical_structure"]["standard_inchi_key"] == context["standard_inchi_key"]
    after = copy.deepcopy(before)
    claims = [ordered(c, ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label",
                          "phenotype_label", "assay", "note", "evidence")) for c in item["claims"]]
    for claim in claims:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after.setdefault("resistance_mechanisms", []).extend(claims)
    after["curation_history"].append(ordered(item["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(after, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == item["record"]["sha256"]
    old_claims = before.get("resistance_mechanisms", [])
    assert after["resistance_mechanisms"] == old_claims + item["claims"]
    assert len(old_claims) == item["existing_claims_preserved"]
    assert after["curation_history"][:-1] == before["curation_history"]
    keep = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in keep} == {k: after[k] for k in keep}
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


@pytest.mark.parametrize("index", range(3))
def test_dated_replay_preserves_owners_without_reading_live_records(index, tmp_path, monkeypatch):
    item = read("-curation.json")["records"][index]
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(item, tmp_path)


@pytest.mark.parametrize("field", ["claim", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(field, tmp_path):
    item = read("-curation.json")["records"][0]
    if field == "claim":
        item["claims"][0]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif field == "event":
        item["curation_event"]["changes"] += " Unsupported edit."
    else:
        item["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


def test_compound_specific_historical_loci_and_unresolved_route():
    receipt = read("-curation.json")
    assert [r["identifier"] for r in receipt["records"]] == list(IDS)
    for item, loci in zip(receipt["records"], (
        ["ACR1", "ACR2", "ACR3", "ACR4"], ["ACR1", "ACR2", "ACR3", "ACR4"],
        ["ACR1", "ACR3", "ACR4"]), strict=True):
        assert [c["gene_id"] for c in item["claims"]] == loci
        for claim in item["claims"]:
            assert claim["mechanism_type"] == "UNKNOWN"
            assert claim["taxon_id"] == "NCBITaxon:4932"
            assert claim["taxon_label"] == "Saccharomyces cerevisiae"
            assert "Historical unmapped locus" in claim["note"]
            assert "not a species-wide phenotype" in claim["note"]
            assert "experimental protein and genome remain unresolved" in claim["note"]
            assert claim["evidence"][0]["reference"] == "PMID:1839761"
            assert claim["evidence"][1]["reference"] == read("-context.json")["sgd"]["url"]
            assert "Modern alias matches are not accepted protein crosswalks" in claim["evidence"][1]["notes"]
            assert not {"alteration", "protein_accession", "strain", "strain_taxon_id", "gene_families",
                        "assembly_accession", "biosample_accession", "sequence", "variant",
                        "mic", "mic_value", "phenotype", "source"}.intersection(claim)
            if item["identifier"] == "CHEBI:569624":
                assert "background-dependent" in claim["note"] and "not transferred to ACR2" in claim["note"]
    assert receipt["new_locus_associations"] == 11
    assert receipt["history_events_added"] == receipt["records_changed"] == 3
    assert receipt["numerical_ast_added"] == receipt["experimental_proteins_or_genomes_assigned"] == 0
    assert not receipt["whole_record_review_complete"]


def test_modern_uniprot_matches_are_not_historical_locus_crosswalks():
    checks = read("-context.json")["uniprot_name_checks"]
    expected = {
        "ACR1": {"Q06596": ("ARR1", 182, 1), "Q02100": ("SKO1", 198, 1), "P33303": ("SFC1", 194, 2)},
        "ACR2": {"Q06597": ("ARR2", 163, 1)}, "ACR3": {"Q06598": ("ARR3", 181, 1)}, "ACR4": {},
    }
    for gene, candidates in expected.items():
        check = checks[gene]
        request = check["request"]
        assert request["release"] == "2026_03" and request["status"] == 200
        assert request["pagination_complete"] and request["total_results"] == len(candidates)
        assert request["query"] == f"gene_exact:{gene} AND organism_id:559292 AND reviewed:true"
        assert "results" not in request and not check["empty_query_is_gene_absence"]
        assert check["interpretation"] == "NO_SUPPORTED_HISTORICAL_LOCUS_CROSSWALK"
        rows = check["name_collision_candidates"]
        assert {r["accession"].removeprefix("UniProtKB:"): (
            r["canonical_gene"], r["entry_version"], r["sequence_version"]) for r in rows} == candidates
        for row in rows:
            assert gene in row["aliases"] and row["reviewed"]
            assert row["reference_taxon_id"] == "NCBITaxon:559292"
            assert not row["accepted_historical_locus_crosswalk"]


def test_source_scope_taxonomy_and_deferral():
    context = read("-context.json")
    sgd = context["sgd"]
    assert sgd["revision"] == 406670 and not sgd["table_is_exhaustive_gene_inventory"]
    assert sgd["explicit_name_collisions"] == {
        "ACR2": {"distinct_gene": "ARR2", "distinct_locus": "YPR200C"},
        "ACR3": {"distinct_gene": "ARR3", "distinct_locus": "YPR201W"}}
    assert set(sgd["historical_loci"]) == {"ACR1", "ACR2", "ACR3", "ACR4"}
    assert all(not r["mapped_to_genome_sequence"] for r in sgd["historical_loci"].values())
    assert context["taxonomy"] == json.loads(pinned(context["taxonomy_predecessor"]))["taxonomy"]
    species, strain = context["taxonomy"]
    assert (species["taxon_id"], species["rank"]) == ("NCBITaxon:4932", "species")
    assert (strain["taxon_id"], strain["rank"], strain["parent_taxon_id"]) == (
        "NCBITaxon:559292", "strain", "NCBITaxon:4932")
    primary = context["primary"]
    assert primary["reference"] == "PMID:1839761" and primary["pdf"]["pages"] == 6
    assert primary["native_tables_inspected"] == [1, 2, 3, 4, 5]
    assert primary["native_figures_inspected"] == [1] and not primary["whole_paper_review_complete"]
    assert not primary["molecular_route_proven"] and not primary["numeric_ast_exported"]
    assert "ACR2" in primary["negative_scope"]
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in context["limits"].items() if k != "issue_1040")
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
        if self.excluded == tag:
            self.excluded = None

    def handle_data(self, data):
        if self.excluded is None:
            self.parts.append(data)


@pytest.mark.parametrize("index", range(3))
def test_scope_notes_survive_real_adapter_and_template(index, tmp_path):
    item = read("-curation.json")["records"][index]
    doc = replay(item, tmp_path)
    record = build_record(ROOT / item["record"]["path"], doc, {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    for claim in item["claims"]:
        for expected in (claim["label"], claim["note"], claim["evidence"][1]["notes"]):
            assert " ".join(expected.split()) in text


def test_census_changes_only_three_records():
    receipt, reconciliation = read("-curation.json"), read("-reconciliation.json")
    maps = [{r["identifier"]: r for r in csv.DictReader(
        pinned(reconciliation[key]).decode().splitlines(), delimiter="\t")}
        for key in ("previous_census", "current_census")]
    before, after = maps
    assert len(before) == len(after) == 2939 and before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == set(IDS)
    for item in receipt["records"]:
        old = before[item["identifier"]]
        assert after[item["identifier"]] == {**old, "record_sha256": item["record"]["sha256"],
            "resistance_assertions": str(int(old["resistance_assertions"]) + len(item["claims"])),
            "research_status": "PENDING_PRIMARY_REVIEW"}
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4866
    assert sum(int(r["resistance_assertions"]) > 0 for r in after.values()) == 313
    assert reconciliation["curator_claims"] == 111 and reconciliation["curator_records"] == 46
    assert reconciliation["records_byte_identical"] == 2936

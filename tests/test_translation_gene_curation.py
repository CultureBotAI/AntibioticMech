"""Selected yeast results must not become reference-allele or class-wide claims."""
import copy
import csv
import hashlib
import json
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names
from scripts.render_pages import TEMPLATES_DIR, build_record

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-translation"
GENES = {"RPL3": ("CHEBI:338412", "P14126", 233, 4, "YOR063W", "S000005589"),
         "PDR5": ("CHEBI:69621", "P33302", 235, 1, "YOR153W", "S000005679")}


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_bytes())


def pinned(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def ordered(value, keys):
    assert set(value) == set(keys)
    return {key: copy.deepcopy(value[key]) for key in keys}


def item_for(gene):
    return next(r for r in read("-curation.json")["records"] if r["identifier"] == GENES[gene][0])


def replay(item, tmp_path):
    context, = [r for r in read("-context.json")["records_before"] if r["identifier"] == item["identifier"]]
    assert hashlib.sha256(pinned(item["fixture"])).hexdigest() == item["before"]["sha256"]
    assert item["before"] == {k: context[k] for k in ("path", "sha256")}
    assert item["record"]["path"] == item["before"]["path"]
    before = load_record(ROOT / item["fixture"]["path"])
    assert before["identifier"] == item["identifier"]
    assert before["chemical_structure"]["standard_inchi_key"] == context["standard_inchi_key"]
    after = copy.deepcopy(before)
    claim, = item["claims"]
    claim = ordered(claim, ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label",
                            "phenotype_label", "assay", "note", "evidence"))
    claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after.setdefault("resistance_mechanisms", []).append(claim)
    after["curation_history"].append(ordered(item["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(after, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == item["record"]["sha256"]
    assert not before.get("resistance_mechanisms") and item["existing_claims_preserved"] == 0
    assert after["curation_history"][:-1] == before["curation_history"]
    keep = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in keep} == {k: after[k] for k in keep}
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


@pytest.mark.parametrize("gene", GENES)
def test_dated_replay_does_not_freeze_live_records(gene, tmp_path, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(item_for(gene), tmp_path)


@pytest.mark.parametrize("gene", GENES)
@pytest.mark.parametrize("field", ["route", "reference", "event", "before_hash", "after_hash", "subject"])
def test_replay_rejects_tampering(gene, field, tmp_path):
    item = item_for(gene)
    if field == "route":
        item["claims"][0]["mechanism_type"] = "UNKNOWN"
    elif field == "reference":
        item["claims"][0]["evidence"][1]["notes"] = "Exact experimental identity."
    elif field == "event":
        item["curation_event"]["changes"] += " Unsupported edit."
    elif field == "subject":
        item["claims"][0]["protein_accession"] = "UniProtKB:" + GENES[gene][1]
    else:
        item["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


@pytest.mark.parametrize("gene", GENES)
def test_reference_protein_is_not_experimental_subject(gene):
    identifier, accession, version, sequence_version, locus, sgd = GENES[gene]
    check = read("-context.json")["uniprot"][gene]
    request, ref = check["request"], check["reference"]
    assert (ref["accession"], ref["entry_version"], ref["sequence_version"]) == (
        "UniProtKB:" + accession, version, sequence_version)
    assert ref["gene"] == gene and ref["reviewed"] and ref["taxon_id"] == "NCBITaxon:559292"
    assert ref["ordered_locus_names"] == [locus] and ref["sgd_ids"] == [sgd]
    assert request["release"] == "2026_03" and request["status"] == 200
    assert request["pagination_complete"] and request["total_results"] == 1
    assert request["query"] == ("accession:P14126" if gene == "RPL3" else
                                "gene_exact:PDR5 AND organism_id:559292 AND reviewed:true")
    assert "results" not in request and not check["experimental_protein_assigned"]
    assert check["scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
    item = item_for(gene)
    assert item["identifier"] == identifier
    claim, = item["claims"]
    assert claim["taxon_id"] == "NCBITaxon:4932" and claim["taxon_label"] == "Saccharomyces cerevisiae"
    assert "not a species-wide phenotype" in claim["note"]
    assert "Experimental allele, protein and genome unresolved" in claim["note"]
    assert "no standardized MIC or clinical category" in claim["note"]
    assert "Reference-only UniProtKB:" + accession in claim["evidence"][1]["notes"]
    assert "Not an exact experimental derivative" in claim["evidence"][1]["notes"]
    forbidden = {"protein_accession", "strain", "strain_taxon_id", "alteration", "gene_families",
                 "assembly_accession", "biosample_accession", "mic", "mic_value", "sequence", "variant"}
    assert not forbidden.intersection(claim)
    if gene == "RPL3":
        assert {"MAK8", "TCM1"} <= set(ref["synonyms"])
        assert claim["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
        assert "JD1090 derivatives" in claim["note"]
        assert "concentration-unit discrepancy" in claim["evidence"][0]["notes"]
    else:
        assert claim["mechanism_type"] == "ANTIBIOTIC_EFFLUX"
        assert "not a direct transport measurement" in claim["note"]
        assert "Figure 1c is DON-only" in claim["evidence"][0]["notes"]


def test_primary_boundaries_holds_and_taxonomy():
    context = read("-context.json")
    assert len(context["records_before"]) == 4
    assert context["initial_candidate_counts_not_primary_reviews"] == {
        "CHEBI:338412": 71, "CHEBI:230243": 7, "CHEBI:9688": 29, "CHEBI:69621": 9}
    assert context["taxonomy"] == json.loads(pinned(context["taxonomy_predecessor"]))["taxonomy"]
    species, strain = context["taxonomy"]
    assert (species["taxon_id"], species["rank"]) == ("NCBITaxon:4932", "species")
    assert (strain["taxon_id"], strain["rank"], strain["parent_taxon_id"]) == (
        "NCBITaxon:559292", "strain", "NCBITaxon:4932")
    a, b = context["primary"]["RPL3"], context["primary"]["PDR5"]
    assert a["native_figures_inspected"] == [2] and "?" not in a["figure"]["url"]
    assert b["native_pages_inspected"] == [3, 7, 10, 13]
    assert b["public_redirect_status_chain"] == [303, 302, 302, 200]
    assert b["pdf"]["status"] == 200 and b["pdf"]["content_type"] == "application/pdf"
    assert not a["whole_paper_review_complete"] and not b["whole_paper_review_complete"]
    assert not b["supplements_reviewed"]
    assert "DON-only" in b["nontransferable_panels"]["Figure 1c"]
    assert "not trichothecin" in b["nontransferable_panels"]["Figure 4b-d"]
    assert "mitochondrial-target" in b["contradictory_interpretation"]
    holds = context["held_leads"]
    assert len(holds) == 3 and all(h["disposition"] == "HOLD" for h in holds)
    assert [r["status"] for r in holds[0]["access_attempts"]] == [403, 403]
    assert holds[1]["scope"] == "PUBLISHER_ABSTRACT_ONLY"
    assert holds[2]["scope"] == "AUTHOR_INSTITUTION_ABSTRACT_ONLY"
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not value for key, value in context["limits"].items() if key != "issue_1040")
    assert context["disposition"]["whole_record_reviews_completed"] == 0
    assert not context["identity"]["class_or_congener_transfer"]


@pytest.mark.parametrize("gene", GENES)
def test_caveats_survive_real_adapter_and_template(gene, tmp_path):
    from tests.test_sinefungin_curation import PageText

    item = item_for(gene)
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
    assert {key for key in before if before[key] != after[key]} == {v[0] for v in GENES.values()}
    for identifier, *_ in GENES.values():
        assert before[identifier]["resistance_assertions"] == "0"
        assert after[identifier]["resistance_assertions"] == "1"
        assert after[identifier]["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4873
    assert receipt["records_byte_identical"] == 2937 and receipt["new_gene_associations"] == 2

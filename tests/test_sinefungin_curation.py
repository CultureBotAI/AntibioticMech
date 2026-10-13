"""Dated yeast associations do not identify experimental reference proteins."""
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
PREFIX = ROOT / "research/2026-10-13-sinefungin"
GENES = {"SAM3": ("Q08986", 170, 1), "SAM1": ("P10659", 228, 2),
         "SAM2": ("P19358", 217, 3), "ABD1": ("P32783", 191, 1)}


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
    context, = [r for r in read("-context.json")["records_before"] if r["identifier"] == "CHEBI:45453"]
    assert hashlib.sha256(pinned(item["fixture"])).hexdigest() == item["before"]["sha256"]
    assert item["before"] == {k: context[k] for k in ("path", "sha256")}
    assert item["record"]["path"] == item["before"]["path"]
    before = load_record(ROOT / item["fixture"]["path"])
    assert before["identifier"] == item["identifier"] == "CHEBI:45453"
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
    assert before.get("resistance_mechanisms", []) == [] and item["existing_claims_preserved"] == 0
    assert after["curation_history"][:-1] == before["curation_history"]
    keep = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in keep} == {k: after[k] for k in keep}
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


def test_dated_replay_does_not_freeze_live_record(tmp_path, monkeypatch):
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
        item["claims"][0]["evidence"][1]["notes"] += " Experimental identity."
    elif field == "event":
        item["curation_event"]["changes"] += " Unsupported edit."
    else:
        item["before" if field == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


@pytest.mark.parametrize("gene", GENES)
def test_reference_protein_is_not_experimental_subject(gene):
    context = read("-context.json")
    check = context["uniprot"][gene]
    request, ref = check["request"], check["reference"]
    accession, version, sequence_version = GENES[gene]
    assert (ref["accession"], ref["entry_version"], ref["sequence_version"]) == (
        "UniProtKB:" + accession, version, sequence_version)
    assert ref["reviewed"] and ref["taxon_id"] == "NCBITaxon:559292"
    assert ref["gene"] == gene and len(ref["ordered_locus_names"]) == len(ref["sgd_ids"]) == 1
    assert request["release"] == "2026_03" and request["status"] == 200
    assert request["pagination_complete"] and request["total_results"] == 1
    assert request["query"] == f"gene_exact:{gene} AND organism_id:559292 AND reviewed:true"
    assert "results" not in request and not check["experimental_protein_assigned"]
    assert check["scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
    claim, = [c for c in read("-curation.json")["claims"] if c["gene_id"] == gene]
    assert claim["taxon_id"] == "NCBITaxon:4932" and claim["taxon_label"] == "Saccharomyces cerevisiae"
    assert "not a species-wide phenotype" in claim["note"]
    assert "Experimental allele, protein and genome unresolved" in claim["note"]
    assert "Reference-only UniProtKB:" + accession in claim["evidence"][1]["notes"]
    assert "Not the tested W303 derivative" in claim["evidence"][1]["notes"]
    assert claim["evidence"][0]["reference"] == "PMID:17932050"
    assert "not a standardized MIC" in claim["evidence"][0]["notes"]
    forbidden = {"protein_accession", "strain", "strain_taxon_id", "alteration", "gene_families",
                 "assembly_accession", "biosample_accession", "mic", "mic_value", "sequence", "variant"}
    assert not forbidden.intersection(claim)
    if gene == "SAM3":
        assert claim["mechanism_type"] == "REDUCED_PERMEABILITY"
        assert "not an efflux measurement" in claim["note"]
        assert "opposite-direction control" in claim["note"]
    else:
        assert claim["mechanism_type"] == "UNKNOWN"
        assert "stronger combined-context effect is not assigned" in claim["note"]


def test_primary_taxonomy_holds_and_deferral():
    context = read("-context.json")
    assert len(context["records_before"]) == 6
    assert context["taxonomy"] == json.loads(pinned(context["taxonomy_predecessor"]))["taxonomy"]
    species, strain = context["taxonomy"]
    assert (species["taxon_id"], species["rank"]) == ("NCBITaxon:4932", "species")
    assert (strain["taxon_id"], strain["rank"], strain["parent_taxon_id"]) == (
        "NCBITaxon:559292", "strain", "NCBITaxon:4932")
    primary = context["primary"]
    assert primary["reference"] == "PMID:17932050" and primary["doi"] == "10.1093/nar/gkm817"
    assert primary["native_figures_inspected"] == [3, 4, 6, 7]
    assert "SAM3 control shows greater susceptibility" in primary["summary"]
    assert not primary["whole_paper_review_complete"]
    assert all(f["status"] == 200 and "?" not in f["url"] for f in primary["figures"])
    assert len(primary["figures"]) == 4
    holds = {r["label"]: r for r in context["other_leads"]}
    assert set(holds) == {"cilofungin", "acrophiarin", "aminocandin", "australifungin", "azoxybacilin"}
    assert all(r["disposition"] == "HOLD" for r in holds.values())
    assert "without drug" in holds["azoxybacilin"]["reason"]
    assert "IC80/IC50 are not MICs" in holds["azoxybacilin"]["reason"]
    assert holds["azoxybacilin"]["sources"][1]["native_pages_inspected"] == [1, 2, 3, 4, 5]
    assert not holds["australifungin"]["repository_attempt"]["is_pdf"]
    assert context["additional_sinefungin_lead"]["disposition"] == "PENDING_SEPARATE_PRIMARY_SCOPE_REVIEW"
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
        if tag == self.excluded:
            self.excluded = None

    def handle_data(self, data):
        if self.excluded is None:
            self.parts.append(data)


@pytest.mark.parametrize("gene", GENES)
def test_caveats_survive_real_adapter_and_template(gene, tmp_path):
    item = read("-curation.json")
    doc = replay(item, tmp_path)
    record = build_record(ROOT / item["record"]["path"], doc, {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    claim, = [c for c in item["claims"] if c["gene_id"] == gene]
    for expected in (claim["label"], claim["note"], *(e["notes"] for e in claim["evidence"])):
        assert " ".join(expected.split()) in text


def test_dated_census_preserves_every_other_row():
    receipt = read("-reconciliation.json")
    rows = [csv.DictReader(pinned(receipt[key]).decode().splitlines(), delimiter="\t")
            for key in ("previous_census", "current_census")]
    before, after = [{r["identifier"]: r for r in values} for values in rows]
    assert before.keys() == after.keys() and len(after) == 2939
    assert [key for key in before if before[key] != after[key]] == ["CHEBI:45453"]
    assert before["CHEBI:45453"]["resistance_assertions"] == "0"
    assert after["CHEBI:45453"]["resistance_assertions"] == "4"
    assert after["CHEBI:45453"]["research_status"] == "PENDING_PRIMARY_REVIEW"
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4870
    assert receipt["records_byte_identical"] == 2938 and receipt["new_gene_associations"] == 4

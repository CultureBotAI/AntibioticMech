"""BSR donor, laboratory host and reference protein are not interchangeable."""
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
from tests.test_sinefungin_curation import PageText

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-blasticidin-deaminase"
ORDER = ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label", "strain",
         "phenotype_label", "assay", "note", "evidence")


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
    context = json.loads(pinned(item["context"]))
    record, = [r for r in context["records_before"] if r["identifier"] == "CHEBI:15353"]
    assert item["before"] == {k: record[k] for k in ("path", "sha256")}
    assert hashlib.sha256(pinned(item["fixture"])).hexdigest() == item["before"]["sha256"]
    before = load_record(ROOT / item["fixture"]["path"])
    after = copy.deepcopy(before)
    claims = [ordered(c, ORDER) for c in item["claims"]]
    for claim in claims:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after["resistance_mechanisms"].extend(claims)
    after["curation_history"].append(ordered(item["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    output = tmp_path / "after.yaml"
    write_validated_antibiotic(after, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == item["record"]["sha256"]
    assert after["identifier"] == "CHEBI:15353"
    assert after["chemical_structure"]["standard_inchi_key"] == "CXNPLSGKWMLZPZ-ZNIXKSQXSA-N"
    assert len(before["resistance_mechanisms"]) == item["existing_claims_preserved"] == 2
    assert after["resistance_mechanisms"][:2] == before["resistance_mechanisms"]
    assert after["activity_spectrum"] == before["activity_spectrum"]
    assert len(before["activity_spectrum"]) == item["existing_observations_preserved"] == 2
    keep = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in keep} == {k: after[k] for k in keep}
    assert after["curation_history"][:-1] == before["curation_history"]
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


def check_subjects(item):
    donor, host = item["claims"]
    assert (donor["taxon_id"], donor["taxon_label"], donor["strain"]) == (
        "NCBITaxon:1396", "Bacillus cereus", "K55-S1")
    assert (host["taxon_id"], host["taxon_label"], host["strain"]) == (
        "NCBITaxon:562", "Escherichia coli", "TK121")
    assert "identified phenotypically" in donor["note"]
    assert "not a native E. coli gene assignment" in host["note"]
    for claim in item["claims"]:
        assert set(claim) == set(ORDER)
        assert claim["gene_id"] == "bsr" and claim["mechanism_type"] == "ANTIBIOTIC_INACTIVATION"
        assert "not a species-wide phenotype" in claim["note"]
        assert "Exact experimental allele, protein and genome unresolved" in claim["note"]
        assert "no standardized MIC or clinical category inferred" in claim["note"]
        assert "Deamination is distinct from chemical isomerization" in claim["note"]
        assert "not equivalence of salt forms" in claim["note"]
        assert [e["reference"] for e in claim["evidence"]] == [
            "DOI:10.7164/antibiotics.40.1791", "DOI:10.1271/bbb1961.55.3155",
            "https://www.uniprot.org/uniprotkb/P33967/entry"]
        assert "Reference-only UniProtKB:P33967" in claim["evidence"][2]["notes"]
        assert "Not an exact experimental allele or host protein accession" in claim["evidence"][2]["notes"]


def test_reference_and_subject_boundaries():
    item = read("-curation.json")
    check_subjects(item)
    context = json.loads(pinned(item["context"]))
    grounding = context["grounding"]
    ref = grounding["reference"]
    assert (ref["accession"], ref["entry_version"], ref["sequence_version"]) == ("UniProtKB:P33967", 95, 1)
    assert grounding["excluded_symbol_match"] == "UniProtKB:A0KLG5"
    assert grounding["protein_request"]["total_results"] == 2
    assert grounding["protein_request"]["pagination_complete"]
    assert grounding["protein_request"]["release"] == "2026_03"
    assert not grounding["exact_experimental_protein_assigned"]
    assert [(t["taxon_id"], t["rank"]) for t in grounding["taxonomy"]] == [
        ("NCBITaxon:1396", "species"), ("NCBITaxon:562", "species")]
    old = json.loads(pinned(grounding["predecessor"]))
    lookup, = [q for q in old["protein_lookups"] if q["request"] == grounding["protein_request"]]
    assert ref in lookup["hits"]
    assert context["chemical_identity"]["scope"] == (
        "BIOCHEMICAL_PARENT_MOIETY_NOT_SALT_EQUIVALENCE_OR_NEW_AST")
    assert [p["native_pages_reviewed"] for p in context["primary"]] == [
        [1791, 1792, 1793], [3155, 3156, 3157]]
    assert all(len(p["rendered_pages"]) == 3 for p in context["primary"])
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in context["limits"].items() if k != "issue_1040")
    assert context["disposition"]["whole_corpus_status"] == "OPEN"
    assert context["disposition"]["whole_record_reviews_completed"] == 0


def test_dated_replay_preserves_prior_curation_without_freezing_live_record(tmp_path, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(read("-curation.json"), tmp_path)


@pytest.mark.parametrize("change", [
    "donor_as_host", "wrong_isolate", "fungal_protein", "experimental_protein",
    "strain_taxon", "measurement", "route", "remove_caveat", "event"])
def test_replay_and_scope_reject_unsupported_promotions(change, tmp_path):
    item = read("-curation.json")
    if change == "donor_as_host":
        item["claims"][1]["taxon_id"] = "NCBITaxon:1396"
    elif change == "wrong_isolate":
        item["claims"][0]["strain"] = "K55-S2"
    elif change == "fungal_protein":
        item["claims"][0]["evidence"][2]["reference"] = "https://www.uniprot.org/uniprotkb/P0C2P0/entry"
    elif change == "experimental_protein":
        item["claims"][1]["protein_accession"] = "UniProtKB:P33967"
    elif change == "strain_taxon":
        item["claims"][0]["strain_taxon_id"] = "NCBITaxon:1396"
    elif change == "measurement":
        item["claims"][0]["mic_value"] = 1
    elif change == "route":
        item["claims"][0]["mechanism_type"] = "UNKNOWN"
    elif change == "remove_caveat":
        item["claims"][0]["note"] = "Exact experimental identity."
    else:
        item["curation_event"]["changes"] += " Unsupported edit."
    with pytest.raises(AssertionError):
        replay(item, tmp_path)
    if change != "event":
        with pytest.raises(AssertionError):
            check_subjects(item)


@pytest.mark.parametrize("subject", [0, 1])
def test_caveats_survive_real_adapter_and_template(subject, tmp_path):
    item = read("-curation.json")
    doc = replay(item, tmp_path)
    record = build_record(ROOT / item["record"]["path"], doc, {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    claim = item["claims"][subject]
    for expected in (claim["label"], claim["note"], *(e["notes"] for e in claim["evidence"])):
        assert " ".join(expected.split()) in text


def test_new_census_changes_only_bsr_record():
    receipt = read("-reconciliation.json")
    tables = [csv.DictReader(pinned(receipt[k]).decode().splitlines(), delimiter="\t")
              for k in ("previous_census", "current_census")]
    before, after = [{r["identifier"]: r for r in table} for table in tables]
    assert len(before) == len(after) == 2939 and before.keys() == after.keys()
    assert {k for k in before if before[k] != after[k]} == {"CHEBI:15353"}
    assert before["CHEBI:15353"]["resistance_assertions"] == "2"
    assert after["CHEBI:15353"]["resistance_assertions"] == "4"
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4875
    assert receipt["records_byte_identical"] == 2938 and receipt["new_gene_associations"] == 2

"""Replay qualified rapamycin curation without assigning reference alleles."""

import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic
from scripts.embed_records import build_document, role_names
from scripts.render_pages import TEMPLATES_DIR, build_record
from tests.test_sinefungin_curation import PageText

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-13-fpr1-primary"


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
    assert item["fixture"] == context["fixture"]
    assert item["fixture"]["sha256"] == item["before"]["sha256"]
    assert item["record"]["path"] == item["before"]["path"] == context["record_before"]["path"]
    pinned(item["fixture"])
    before = load_record(ROOT / item["fixture"]["path"])
    assert before["identifier"] == item["identifier"] == "CHEBI:9168"
    assert before["chemical_structure"]["standard_inchi_key"] == "QFJCIRLUMZQUOT-HPLJOQBZSA-N"
    assert not before.get("resistance_mechanisms")
    after = copy.deepcopy(before)
    claims = [ordered(c, ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label", "strain",
                         "phenotype_label", "assay", "note", "evidence")) for c in item["claims"]]
    for claim in claims:
        claim["evidence"] = [ordered(e, ("reference", "notes")) for e in claim["evidence"]]
    after.setdefault("resistance_mechanisms", []).extend(claims)
    after["curation_history"].append(ordered(item["curation_event"], (
        "timestamp", "curator", "action", "changes", "llm_assisted")))
    path = tmp_path / "after.yaml"
    write_validated_antibiotic(after, path)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["record"]["sha256"]
    assert after["curation_history"][:-1] == before["curation_history"]
    unchanged = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in unchanged} == {k: after[k] for k in unchanged}
    assert build_document(before, role_names()) != build_document(after, role_names())
    return after


def test_historical_replay_without_live_record_freeze(tmp_path, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(read("-curation.json"), tmp_path)


@pytest.mark.parametrize("change", ["route", "reference", "event", "before_hash", "after_hash", "host"])
def test_replay_rejects_tampering(change, tmp_path):
    item = read("-curation.json")
    if change == "route":
        item["claims"][0]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif change == "reference":
        item["claims"][0]["evidence"][1]["notes"] += " Exact experimental protein."
    elif change == "event":
        item["curation_event"]["changes"] += " Unrelated edit."
    elif change == "host":
        item["claims"][0]["strain"] = "YKK1081 laboratory derivatives"
    else:
        item["before" if change == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


@pytest.mark.parametrize("gene,accession,version,sequence_version,locus,sgd", [
    ("FPR1", "P20081", 220, 2, "YNL135C", "S000005079"),
    ("TOR2", "P32600", 214, 3, "YKL203C", "S000001686"),
])
def test_versioned_reference_not_experimental_allele(gene, accession, version, sequence_version, locus, sgd):
    context = read("-context.json")
    protein = context["uniprot"][gene]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["entry_version"] == version and protein["sequence_version"] == sequence_version
    assert protein["primary_gene_name"] == gene and protein["ordered_locus_names"] == [locus]
    assert protein["sgd_id"] == sgd and protein["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
    assert protein["reference_taxon_id"] == "NCBITaxon:559292" and protein["reference_taxon_rank"] == "strain"
    assert protein["source_species_taxon_id"] == "NCBITaxon:4932" and protein["species_lineage_verified"]
    assert protein["reference_identity_only"] and not protein["exact_resistance_allele"]
    assert not protein["experimental_subject_assignment"] and not protein["focal_paper_in_bibliography"]
    assert protein["reused"] == (gene == "FPR1")
    request = protein["request"]
    url = urlsplit(request["url"])
    assert url.netloc == "rest.uniprot.org" and request["release"] == "2026_03"
    params = parse_qs(url.query)
    assert params["query"] == [f"gene_exact:{gene} AND organism_id:559292 AND reviewed:true"]
    assert params["size"] == ["50"]
    assert not {"sequence", "features"} & set(params["fields"][0].split(","))


@pytest.mark.parametrize("gene,host,location", [
    ("FPR1", "YKK207", "Figure 5B"), ("TOR2", "YKK1081", "Figure 6")])
def test_claims_preserve_qualitative_subject_and_mechanism_limits(gene, host, location):
    claim, = [c for c in read("-curation.json")["claims"] if c["gene_id"] == gene]
    assert claim["mechanism_type"] == "UNKNOWN" and claim["taxon_id"] == "NCBITaxon:4932"
    assert claim["strain"] == host + " laboratory derivatives"
    assert claim["assay"] == "Comparative growth spot assay"
    assert claim["phenotype_label"] == "Source-reported relative rapamycin resistance"
    assert not {"protein_accession", "strain_taxon_id", "alteration", "phenotype_id"} & set(claim)
    assert "not all perturbations" in claim["note"] and "drug-free growth" in claim["note"]
    assert claim["evidence"][0]["reference"] == "DOI:10.1371/journal.pgen.1008865"
    assert location in claim["evidence"][0]["notes"]
    assert "Reference-only" in claim["evidence"][1]["notes"]


@pytest.mark.parametrize("host,row", [("YKK206", 10), ("YKK207", 11), ("YKK1080", 35),
                                     ("YKK1081", 36), ("YKK1093", 42), ("YKK1097", 43)])
def test_source_host_labels_not_unique_derivatives_or_genomes(host, row):
    subject = read("-context.json")["subjects"][host]
    assert subject["source_cells"] == f"Sheet1!A{row}:C{row}"
    assert subject["source_species"] == "Saccharomyces cerevisiae"
    assert not subject["host_label_is_unique_assayed_derivative"]
    assert not subject["experimental_strain_taxon_or_genome_assigned"]


def test_negative_comparisons_and_archive_type_remain_visible():
    context = read("-context.json")
    findings = {f["gene"]: f for f in context["findings"]}
    assert "do not have identical outcomes" in findings["FPR1"]["negative_control_scope"]
    assert "poor baseline growth" in findings["FPR1"]["other_background"]
    assert "native-organism resistance" in findings["FPR1"]["heterologous_scope"]
    assert "no translation made" in findings["TOR2"]["numbering_caveat"]
    archive = context["archive_scope"]
    assert archive["source_reported_accessions"] == ["DRA007139", "DRA008879"]
    assert archive["source_data_types"] == ["RNA-seq", "ChIP-seq"]
    assert archive["new_archive_requests"] == 0
    assert not archive["accessions_are_assemblies"]
    assert not archive["subject_sample_or_genome_join_established"]


def test_primary_scope_and_no_raw_variant_export():
    context = read("-context.json")
    assert context["primary"]["native_figures_visually_reviewed"] == ["Figure 5", "Figure 6"]
    assert context["primary"]["strain_table_structured_cells_inspected"]
    assert not context["primary"]["strain_table_rendered_or_visually_reviewed"]
    assert not context["primary"]["whole_article_review_complete"]
    assert context["whole_record_reviews_completed"] == 0
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in context["limits"].items() if k != "issue_1040")
    for key, asset in context["primary"]["assets"].items():
        assert urlsplit(asset["source_url"]).netloc == "journals.plos.org"
        assert not urlsplit(asset["final_url_without_query"]).query
        assert asset["validated_publisher_redirects"] == (0 if key == "article" else 1)
    serialized = json.dumps(context).lower()
    for forbidden in ("x-goog-signature", "x-goog-credential", '"sequence":', '"genotype":', '"constructs":'):
        assert forbidden not in serialized


def test_qualifiers_survive_render_and_embedding(tmp_path):
    item = read("-curation.json")
    record = build_record(ROOT / item["record"]["path"], replay(item, tmp_path), {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    for claim in item["claims"]:
        for expected in (claim["label"], claim["note"], *(e["notes"] for e in claim["evidence"])):
            assert expected in text


def test_historical_census_does_not_claim_complete_review():
    item, reconciliation = read("-curation.json"), read("-reconciliation.json")
    for key, expected in (("previous_census", item["before"]), ("current_census", item["record"])):
        rows = list(csv.DictReader(pinned(reconciliation[key]).decode().splitlines(), delimiter="\t"))
        assert len(rows) == 2939
        row, = [r for r in rows if r["identifier"] == "CHEBI:9168"]
        assert row["record_sha256"] == expected["sha256"]
        expected_status = "PENDING_DISCOVERY" if key == "previous_census" else "PENDING_PRIMARY_REVIEW"
        assert row["research_status"] == expected_status
    assert reconciliation["records_byte_identical"] == 2938
    assert reconciliation["resistance_assertions"] == 4879
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert not item["whole_record_review_complete"]

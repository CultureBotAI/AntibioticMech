"""Keep selected laboratory associations separate from reference identities."""

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
PREFIX = ROOT / "research/2026-10-13-tubercidin"
REFERENCES = {
    "TRP": ("LmjF.31.2010", "Q4Q661", 78, "LMJF_31_2010", "XP_001685187.1", "XM_001685135.1"),
    "NUPM1": ("LmjF.31.1940", "Q4Q668", 71, "LMJF_31_1940", "XP_001685180.1", "XM_001685128.1"),
}


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
    assert before["identifier"] == item["identifier"] == "CHEBI:48267"
    assert before["chemical_structure"]["standard_inchi_key"] == "HDZZVAMISRMYHH-KCGFPETGSA-N"
    assert not before.get("resistance_mechanisms")
    after = copy.deepcopy(before)
    claims = [ordered(c, ("mechanism_type", "label", "gene_id", "taxon_id", "taxon_label",
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


def test_historical_replay_does_not_freeze_live_record(tmp_path, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    replay(read("-curation.json"), tmp_path)


@pytest.mark.parametrize("change", ["route", "reference", "event", "before_hash", "after_hash"])
def test_replay_rejects_tampering(change, tmp_path):
    item = read("-curation.json")
    if change == "route":
        item["claims"][0]["mechanism_type"] = "ANTIBIOTIC_EFFLUX"
    elif change == "reference":
        item["claims"][0]["evidence"][1]["notes"] += " Experimental identity."
    elif change == "event":
        item["curation_event"]["changes"] += " Unrelated edit."
    else:
        item["before" if change == "before_hash" else "record"]["sha256"] = "0" * 64
    with pytest.raises(AssertionError):
        replay(item, tmp_path)


@pytest.mark.parametrize("gene", REFERENCES)
def test_refseq_join_does_not_upgrade_unreviewed_orf_or_assign_allele(gene):
    context = read("-context.json")
    protein = context["uniprot"][gene]
    locus, accession, version, orf, xp, xm = REFERENCES[gene]
    assert protein["source_locus"] == locus
    assert (protein["protein_accession"], protein["entry_version"], protein["sequence_version"]) == (
        "UniProtKB:" + accession, version, 1)
    assert protein["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["primary_gene_name"] is None and protein["ordered_locus_names"] == []
    assert protein["gene_orf_names"] == [orf]
    assert protein["source_reference_protein"] == protein["refseq_crosswalk"]["id"] == xp
    assert protein["source_reference_transcript"] == xm
    assert protein["refseq_crosswalk"]["properties"] == [{"key": "NucleotideSequenceId", "value": xm}]
    assert protein["reference_taxon_id"] == "NCBITaxon:5664"
    assert protein["reference_taxon_rank"] == "species"
    assert not protein["experimental_protein_or_allele_assigned"]
    assert not protein["reference_species_is_exact_tested_derivative"]
    assert not protein["focal_paper_in_bibliography"]
    assert not any(c["primary_results_reviewed"] for c in protein["bibliography"])
    request = protein["request"]
    assert request["status"] == 200 and request["release"] == "2026_03"
    url = urlsplit(request["url"])
    assert url.hostname == "rest.uniprot.org"
    query = parse_qs(url.query)
    assert query["query"] == ["xref:refseq-" + xp]
    assert "sequence" not in query["fields"][0].split(",")
    claim, = [c for c in read("-curation.json")["claims"] if c["gene_id"] == locus]
    assert claim["mechanism_type"] == "UNKNOWN"
    assert claim["taxon_id"] == "NCBITaxon:5664" and claim["taxon_label"] == "Leishmania major"
    assert claim["assay"] == "Comparative growth inhibition (IC50-based)"
    assert "not a species-wide or clinical phenotype" in claim["note"]
    assert "Molecular route unresolved" in claim["note"]
    assert claim["evidence"][0]["reference"] == "PMID:27606425"
    assert "Reference-only UniProtKB:" + accession in claim["evidence"][1]["notes"]
    assert "not an exact tested derivative" in claim["evidence"][1]["notes"]
    assert not {"protein_accession", "strain", "strain_taxon_id", "alteration", "gene_families",
                "assembly_accession", "biosample_accession", "mic", "mic_value", "sequence"} & claim.keys()


def test_empty_gene_search_and_assay_caveats_remain_explicit():
    context = read("-context.json")
    empty = context["empty_name_query"]
    assert empty["status"] == 200 and empty["results"] == 0
    assert not empty["protein_absence_inferred"] and not empty["initial_nupm1_gene_query_run"]
    assert context["subject_scope"]["rank"] == "species"
    assert not context["subject_scope"]["background_is_one_tested_subject"]
    assert not context["subject_scope"]["strain_taxon_id_assigned"]
    limits = " ".join(context["evidence_limits"])
    for text in ("not MICs", "SEM", "SD", "not a tested negative", "not measured molecular routes",
                 "Negative controls", "Other-drug findings are not transferred"):
        assert text in limits
    assert not context["chemical_scope"]["generic_sparsomycin_search_hits_transferred"]
    assert context["whole_record_reviews_completed"] == 0
    assert not context["primary"]["whole_article_review_complete"]
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in context["limits"].items() if k != "issue_1040")


def test_native_assets_preserve_redirect_receipts_without_signed_urls():
    context = read("-context.json")
    assets = context["primary"]["assets"]
    assert len(assets) == 7
    assert len(context["primary"]["native_assets_visually_reviewed"]) == 6
    for name, asset in assets.items():
        assert urlsplit(asset["source_url"]).hostname == "journals.plos.org"
        final = urlsplit(asset["final_url_without_query"])
        assert not final.query and asset["status"] == 200 and not asset["retry_performed"]
        assert asset["validated_publisher_redirects"] == (0 if name == "article" else 1)
        assert final.hostname == ("journals.plos.org" if name == "article" else "storage.googleapis.com")
        assert len(asset["body"]["sha256"]) == 64
    serialized = json.dumps(context).lower()
    for forbidden in ("x-goog-signature", "x-goog-credential", '"sequence":', '"constructs":'):
        assert forbidden not in serialized
    assert context["primary"]["supplement_rendering"]["pages"] == 1
    assert context["uniprot_attribution"]["license"] == "CC BY 4.0"


def test_qualifiers_survive_real_page_template(tmp_path):
    item = read("-curation.json")
    record = build_record(ROOT / item["record"]["path"], replay(item, tmp_path), {}, "../")
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape(["html", "xml"]))
    page = PageText()
    page.feed(env.get_template("record.html").render(r=record, root="../", stats={}))
    text = " ".join(" ".join(page.parts).split())
    for claim in item["claims"]:
        for expected in (claim["label"], claim["note"], *(e["notes"] for e in claim["evidence"])):
            assert expected in text


def test_historical_census_does_not_promote_whole_record_review():
    item = read("-curation.json")
    reconciliation = read("-reconciliation.json")
    for key, expected in (("previous_census", item["before"]), ("current_census", item["record"])):
        rows = list(csv.DictReader(pinned(reconciliation[key]).decode().splitlines(), delimiter="\t"))
        assert len(rows) == 2939
        row, = [r for r in rows if r["identifier"] == "CHEBI:48267"]
        assert row["record_sha256"] == expected["sha256"]
    assert reconciliation["records_checked"] == 2939
    assert reconciliation["records_byte_identical"] == 2938
    assert reconciliation["new_gene_associations"] == 2
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert not item["whole_record_review_complete"]

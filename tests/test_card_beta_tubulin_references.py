"""Protein-name references preserve paralogs, exclusions and experimental scope."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_beta_tubulin_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def node(taxid, name, rank):
    return {"taxonId": taxid, "scientificName": name, "rank": rank}


def source_taxon():
    fungi = node(4751, "Fungi", "kingdom")
    taxon = {
        **node(746128, "Aspergillus fumigatus", "species"),
        "active": True,
        "parent": fungi,
        "lineage": [fungi],
    }
    return audit.taxa.resolve_name(taxon, "Aspergillus fumigatus", "BINOMIAL")["selected_taxon"]


def taxonomy():
    nodes = source_taxon()["lineage"]
    return {
        **node(330879, "Aspergillus fumigatus (strain Af293)", "strain"),
        "active": True,
        "lineage": nodes,
        "parent": nodes[-1],
    }


@pytest.fixture
def entry():
    return {
        "primaryAccession": "Q4WA70",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "organism": {"taxonId": 330879, "scientificName": "Aspergillus fumigatus (strain Af293)"},
        "genes": [{"orfNames": [{"value": "AFUA_7G00250"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Tubulin beta chain"}}},
        "references": [
            {
                "citation": {
                    "publicationDate": "2000",
                    "citationCrossReferences": [{"database": "PubMed", "id": "12345"}],
                },
                "referencePositions": ["not exported"],
            }
        ],
    }


@pytest.mark.parametrize("spelling", ["Botrytis cinerea", "botrytis cinerea"])
def test_only_initial_case_is_normalized_and_source_is_preserved(spelling):
    parsed = audit.source_identity(spelling + " beta-tubulin with mutations conferring resistance")
    assert parsed["source_organism_name"] == spelling
    assert parsed["taxonomy_query_name"] == "Botrytis cinerea"
    assert parsed["source_gene_symbol"] is None
    assert parsed["name_normalization"] == ("NONE" if spelling[0] == "B" else "GENUS_INITIAL_CASE_ONLY")


@pytest.mark.parametrize(
    "label", ["beta-tubulin", "fungal beta-tubulin", "Botrytis spp. beta-tubulin with mutation"]
)
def test_broad_source_names_are_not_given_species(label):
    with pytest.raises(ValueError):
        audit.source_identity(label)


@pytest.mark.parametrize("reviewed", [True, False])
def test_protein_name_query_does_not_invent_a_gene_symbol(reviewed):
    url = urlsplit(audit.query_url(746128, reviewed))
    query = parse_qs(url.query)
    assert url.netloc == "rest.uniprot.org" and url.path == "/uniprotkb/search"
    assert query["query"] == [
        f'(protein_name:"tubulin beta" OR protein_name:"beta-tubulin") '
        f"AND taxonomy_id:746128 AND reviewed:{str(reviewed).lower()}"
    ]
    assert query["fields"] == [audit.FIELDS] and query["size"] == ["500"]
    assert not {"sequence", "ft_variant", "cc_function"}.intersection(audit.FIELDS.split(","))


@pytest.mark.parametrize(
    "taxid,reviewed", [(True, True), (0, True), (-1, True), ("746128", True), (746128, 1)]
)
def test_invalid_query_inputs_fail(taxid, reviewed):
    with pytest.raises(ValueError):
        audit.query_url(taxid, reviewed)


@pytest.mark.parametrize(
    "name",
    [
        "Beta-tubulin",
        "Tubulin beta chain",
        "Tubulin beta-1 chain",
        "Tubulin beta-2 chain",
        "Beta-1-tubulin",
        "Beta-2-tubulin",
    ],
)
def test_native_beta_names_match_without_paralog_collapse(entry, name):
    entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = name
    assert audit.validate_entry(entry, True)[0]["value"] == name


@pytest.mark.parametrize(
    "name",
    [
        "Beta-tubulin cofactor d",
        "Tubulin alpha chain",
        "Gamma-tubulin",
        "Tubulin binding protein",
        "Uncharacterized protein",
    ],
)
def test_cofactors_and_other_tubulins_are_not_beta_candidates(entry, name):
    entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = name
    assert audit.validate_entry(entry, True) == []
    with pytest.raises(ValueError, match="native beta"):
        audit.project(entry, taxonomy(), source_taxon(), True)


def test_orf_only_reference_does_not_acquire_a_gene_symbol(entry):
    result = audit.project(entry, taxonomy(), source_taxon(), True)
    assert result["native_gene_annotations"] == [
        {"geneName": [], "synonyms": [], "orderedLocusNames": [], "orfNames": ["AFUA_7G00250"]}
    ]
    assert result["source_gene_symbol_assignment"] is None
    assert result["experimental_subject_assignment"] is result["exact_resistance_allele"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["reference_taxon_id"] == "NCBITaxon:330879"
    assert result["reference_species_taxon_id"] == "NCBITaxon:746128"
    assert result["unflagged_means_complete"] is False
    assert result["database_review_status_is_primary_results_review"] is False
    assert "not exported" not in json.dumps(result)
    assert all(c["primary_results_reviewed"] is False for c in result["bibliography"])


@pytest.mark.parametrize("reviewed", [True, False])
def test_fragment_flags_are_preserved_for_both_review_statuses(entry, reviewed):
    if not reviewed:
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    entry["proteinDescription"]["flag"] = "Fragment"
    result = audit.project(entry, taxonomy(), source_taxon(), reviewed)
    assert result["native_protein_flag"] == "Fragment" and result["unflagged_means_complete"] is False


def test_multiple_native_gene_blocks_are_retained_without_assignment(entry):
    entry["genes"] = [{"geneName": {"value": "TUB1"}}, {"geneName": {"value": "TUB2"}}]
    result = audit.project(entry, taxonomy(), source_taxon(), True)
    assert [b["geneName"] for b in result["native_gene_annotations"]] == [["TUB1"], ["TUB2"]]
    assert result["source_gene_symbol_assignment"] is None


@pytest.mark.parametrize(
    "change",
    [
        "wrong_taxon",
        "inactive",
        "wrong_species",
        "lineage_conflict",
        "review_status",
        "zero_version",
        "bool_version",
        "sequence",
        "features",
        "comments",
        "unknown_flag",
        "empty_name",
    ],
)
def test_projection_scope_guards(entry, change):
    taxon, named = taxonomy(), source_taxon()
    if change == "wrong_taxon":
        taxon["taxonId"] = 99
    elif change == "inactive":
        taxon["active"] = False
    elif change == "wrong_species":
        named["species_ancestor"]["taxonId"] = 99
    elif change == "lineage_conflict":
        named["lineage"][0]["scientificName"] = "different"
    elif change == "review_status":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"zero_version", "bool_version"}:
        entry["entryAudit"]["entryVersion"] = 0 if change == "zero_version" else True
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    elif change == "unknown_flag":
        entry["proteinDescription"]["flag"] = "Complete"
    else:
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = ""
    with pytest.raises(ValueError):
        audit.project(entry, taxon, named, True)


def test_query_exclusions_are_not_silently_lost(entry, monkeypatch):
    cofactor = copy.deepcopy(entry)
    cofactor["primaryAccession"] = "A0A000"
    cofactor["proteinDescription"]["recommendedName"]["fullName"]["value"] = "Beta-tubulin cofactor d"
    source = {"url": audit.query_url(746128, True)}
    monkeypatch.setattr(
        audit.native,
        "read_source",
        lambda *args: ({"results": [entry, cofactor], "suggestions": [{"not": "followed"}]}, {"status": 200}),
    )
    entries, query = audit.read_query(ROOT, source, 746128, True)
    assert entries == [entry] and query["result_count"] == 2 and query["candidate_count"] == 1
    assert query["excluded_candidates"][0]["protein_accession"] == "UniProtKB:A0A000"
    assert query["suggestions_ignored"] == 1 and query["suggestions_followed"] is False
    assert query["zero_hit_is_biological_absence"] is False


def test_duplicate_query_results_fail(entry, monkeypatch):
    source = {"url": audit.query_url(746128, True)}
    monkeypatch.setattr(audit.native, "read_source", lambda *args: ({"results": [entry, entry]}, {}))
    with pytest.raises(ValueError, match="duplicate"):
        audit.read_query(ROOT, source, 746128, True)


def test_query_scope_cannot_be_relabelled():
    with pytest.raises(ValueError, match="identity"):
        audit.read_query(ROOT, {"url": audit.query_url(746128, True)}, 746128, False)


@pytest.mark.parametrize(
    "change",
    [
        None,
        "missing_context",
        "extra_request",
        "wrong_taxon",
        "wrong_name",
        "wrong_review",
        "nonempty_prior",
        "stale_prior",
    ],
)
def test_fallback_requires_complete_reviewed_candidate_zero(tmp_path, monkeypatch, change):
    cohort = {"terms": {"ARO:test": {"taxonomy_query_name": "Aspergillus fumigatus"}}}
    (tmp_path / "cohort.json").write_text(json.dumps(cohort))
    name = "Aspergillus fumigatus"
    named = {name: {"selected_taxon": source_taxon()}}
    prior = {name: ([], {"candidate_accessions": [], "complete_for_query": True})}
    request = {
        "name": name,
        "source_taxon_id": 746128,
        "reviewed": False,
        "url": audit.query_url(746128, False),
    }
    plan = {
        "cohort": audit.reference.pin(tmp_path, tmp_path / "cohort.json"),
        "queries": {name: {"request_key": "fallback", "prior_reviewed_query": copy.deepcopy(prior[name][1])}},
        "requests": {"fallback": request},
    }
    if change == "missing_context":
        plan["queries"] = {}
    elif change == "extra_request":
        plan["requests"]["extra"] = copy.deepcopy(request)
    elif change in {"wrong_taxon", "wrong_name", "wrong_review"}:
        key = {"wrong_taxon": "source_taxon_id", "wrong_name": "name", "wrong_review": "reviewed"}[change]
        request[key] = 999 if key == "source_taxon_id" else True if key == "reviewed" else "Different species"
    elif change == "nonempty_prior":
        prior[name] = ([{"primaryAccession": "Q4WA70"}], prior[name][1])
    elif change == "stale_prior":
        plan["queries"][name]["prior_reviewed_query"]["complete_for_query"] = False
    (tmp_path / "unreviewed-plan.json").write_text(json.dumps(plan))
    monkeypatch.setattr(audit, "planned_source", lambda *args: {"url": args[-1]})
    monkeypatch.setattr(audit, "read_query", lambda *args: ([], {"candidate_accessions": []}))
    if change:
        with pytest.raises(ValueError):
            audit.read_queries(tmp_path, tmp_path, cohort, named, False, prior)
    else:
        assert set(audit.read_queries(tmp_path, tmp_path, cohort, named, False, prior)) == {name}


@pytest.mark.parametrize("change", ["pagination", "count", "release", "status", "checksum"])
def test_incomplete_native_query_is_not_a_complete_zero(tmp_path, change):
    body = b'{"results": []}'
    body_path, receipt_path = tmp_path / "body.bin", tmp_path / "receipt.json"
    body_path.write_bytes(body)
    receipt = {
        "url": audit.query_url(746128, True),
        "status": 200,
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "retrieved_at": "test",
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": "0"},
    }
    if change == "pagination":
        receipt["headers"]["link"] = "<https://rest.uniprot.org/next>; rel=next"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "1"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "different"
    elif change == "status":
        receipt["status"] = 500
    else:
        receipt["sha256"] = "different"
    receipt_path.write_text(json.dumps(receipt))
    source = {
        "url": receipt["url"],
        "body": audit.reference.pin(tmp_path, body_path),
        "receipt": audit.reference.pin(tmp_path, receipt_path),
    }
    with pytest.raises(ValueError):
        audit.read_query(tmp_path, source, 746128, True)


def test_public_checkpoint_covers_every_source_term_without_promoting_evidence():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads(audit.reference.check_pin(ROOT, data["inputs"]["index"]).read_bytes())
    citations = json.loads(
        audit.reference.check_pin(ROOT, data["inputs"]["definition_citations"]).read_bytes()
    )["terms"]
    import csv

    labels = {
        r["determinant_id"]: r["determinant_name"]
        for r in csv.DictReader(
            audit.reference.check_pin(ROOT, data["inputs"]["source_inventory"]).open(), delimiter="\t"
        )
    }
    expected = {t for t in index["terms"] if audit.SELECT.search(labels[t])}
    assert set(data["terms"]) == expected and len(expected) == 15
    assert len(data["claims"]) == 15 and len(data["records"]) == 7
    assert data["summary"]["terms_without_own_definition_citations"] == 13
    assert data["summary"]["reference_proteins"] == 26
    assert data["summary"]["term_protein_links"] == 50
    assert data["summary"]["fragment_references"] == 20
    used = set()
    for tid, term in data["terms"].items():
        assert all(term[k] == v for k, v in audit.source_identity(labels[tid]).items())
        assert term["source_label_sha256"] == hashlib.sha256(labels[tid].encode()).hexdigest()
        assert term["definition_citation_ids"] == citations[tid]["definition_citation_ids"]
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert term["source_gene_symbol"] is term["experimental_genome_assignment"] is None
        assert term["primary_review_status"] == "OPEN"
        queries = term["queries"]
        assert ("unreviewed" in queries) is (queries["reviewed"]["candidate_count"] == 0)
        selected = queries.get("unreviewed", queries["reviewed"])
        for query in queries.values():
            assert query["complete_for_query"] is True and query["zero_hit_is_biological_absence"] is False
            excluded = {
                e["protein_accession"].removeprefix("UniProtKB:") for e in query["excluded_candidates"]
            }
            assert not excluded.intersection(query["candidate_accessions"])
            assert excluded | set(query["candidate_accessions"]) == set(query["all_result_accessions"])
            assert query["result_count"] == len(query["all_result_accessions"])
        accessions = {c["protein_accession"] for c in term["reference_candidates"]}
        assert accessions == {"UniProtKB:" + a for a in selected["candidate_accessions"]}
        used.update(accessions)
    assert used == set(data["proteins"])
    assert {c["protein_accession"] for c in data["terms"]["ARO:3009433"]["reference_candidates"]} == {
        "UniProtKB:P32928",
        "UniProtKB:P40904",
    }
    assert data["proteins"]["UniProtKB:Q4WA70"]["native_gene_annotations"][0]["geneName"] == []
    assert data["proteins"]["UniProtKB:K7XH91"]["native_protein_flag"] == "Fragment"
    cofactor = data["terms"]["ARO:3009475"]["queries"]["unreviewed"]["excluded_candidates"]
    assert len(cofactor) == 1 and cofactor[0]["protein_accession"] == "UniProtKB:A0ACC3ZK29"
    assert "UniProtKB:A0ACC3ZK29" not in data["proteins"]
    assert data["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert data["summary"]["whole_record_primary_signoffs"] == 0


def test_dated_cli_never_overwrites_a_checkpoint(tmp_path, monkeypatch):
    path = tmp_path / "checkpoint.json"
    path.write_bytes(b"historical\n")
    monkeypatch.setattr(audit, "OUTPUT", path)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit"])
    with pytest.raises(ValueError, match="reproduce"):
        audit.main()
    assert path.read_bytes() == b"historical\n"

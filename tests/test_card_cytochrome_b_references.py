"""Cytochrome-b reference metadata must not become experimental identity."""

import copy
import csv
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
import audit_card_cytochrome_b_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def taxonomy():
    fungi = {"taxonId": 4751, "scientificName": "Fungi", "rank": "kingdom"}
    return {
        "taxonId": 31870,
        "scientificName": "Colletotrichum graminicola",
        "rank": "species",
        "active": True,
        "parent": fungi,
        "lineage": [fungi],
    }


def named():
    return audit.taxa.resolve_name(taxonomy(), "Colletotrichum graminicola", "BINOMIAL")["selected_taxon"]


@pytest.fixture
def entry():
    return {
        "primaryAccession": "A0A123",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "organism": {"taxonId": 31870, "scientificName": "Colletotrichum graminicola"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Cytochrome b"}}},
        "genes": [{"geneName": {"value": "cob"}, "synonyms": [{"value": "cytb"}]}],
        "references": [
            {
                "citation": {
                    "publicationDate": "2000",
                    "citationCrossReferences": [{"database": "PubMed", "id": "12345"}],
                },
                "referencePositions": ["not exported"],
                "referenceComments": [{"type": "STRAIN", "value": "not assigned"}],
            }
        ],
    }


def test_source_name_is_not_a_gene_symbol():
    row = audit.source_identity(
        "Colletotrichum graminicola cytochrome b protein with mutations associated with resistance"
    )
    assert row["source_organism_name"] == row["taxonomy_query_name"] == "Colletotrichum graminicola"
    assert row["source_gene_symbol"] is None and row["source_protein_label"] == "cytochrome b protein"


@pytest.mark.parametrize(
    "label",
    [
        "fungal cytochrome b",
        "Colletotrichum spp. cytochrome b protein with mutations",
        "Colletotrichum graminicola cytb with mutations",
    ],
)
def test_unreviewed_source_syntax_is_rejected(label):
    with pytest.raises(ValueError, match="source syntax"):
        audit.source_identity(label)


@pytest.mark.parametrize("reviewed", [True, False])
def test_query_is_metadata_only_and_species_scoped(reviewed):
    url = urlsplit(audit.query_url(31870, reviewed))
    parameters = parse_qs(url.query)
    assert url.netloc == "rest.uniprot.org" and url.path == "/uniprotkb/search"
    assert parameters["query"] == [
        f'protein_name:"cytochrome b" AND taxonomy_id:31870 AND reviewed:{str(reviewed).lower()}'
    ]
    assert parameters["size"] == ["500"] and parameters["fields"] == [audit.FIELDS]
    assert not {"sequence", "ft_variant", "cc_function"}.intersection(audit.FIELDS.split(","))


@pytest.mark.parametrize("taxid,reviewed", [(True, True), (0, True), (-1, True), ("31870", True), (31870, 1)])
def test_invalid_query_input(taxid, reviewed):
    with pytest.raises(ValueError):
        audit.query_url(taxid, reviewed)


@pytest.mark.parametrize("name", ["Cytochrome b", "cytochrome b", "CYTOCHROME B"])
def test_exact_native_name_match(entry, name):
    entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = name
    assert audit.validate_entry(entry, False)[0]["value"] == name


@pytest.mark.parametrize(
    "name",
    [
        "Cytochrome b5",
        "Cytochrome b-c1 complex subunit 7",
        "Cytochrome b561",
        "Cytochrome b reductase",
        "Cytochrome b mRNA-processing protein 4",
        "Succinate dehydrogenase [ubiquinone] cytochrome b small subunit",
        "Uncharacterized protein",
    ],
)
def test_related_names_are_excluded(entry, name):
    entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = name
    assert audit.validate_entry(entry, False) == []
    with pytest.raises(ValueError, match="native cytochrome"):
        audit.project(entry, taxonomy(), named(), False)


@pytest.mark.parametrize("flag", [None, "Fragment"])
def test_gene_names_and_fragments_remain_reference_metadata(entry, flag):
    if flag:
        entry["proteinDescription"]["flag"] = flag
    result = audit.project(entry, taxonomy(), named(), False)
    assert result["native_gene_annotations"] == [
        {"geneName": ["cob"], "synonyms": ["cytb"], "orderedLocusNames": [], "orfNames": []}
    ]
    assert result["native_protein_flag"] == flag and result["unflagged_means_complete"] is False
    assert result["source_gene_symbol_assignment"] is result["experimental_genome_assignment"] is None
    assert result["exact_resistance_allele"] is result["experimental_subject_assignment"] is False
    assert result["fragment_coordinates_mapped_to_full_length"] is False
    assert result["organelle_or_genomic_location_inferred_from_name"] is False
    assert result["bibliography_is_complete_reference_inventory"] is False
    assert "not exported" not in json.dumps(result) and "not assigned" not in json.dumps(result)
    assert all(r["primary_results_reviewed"] is False for r in result["bibliography"])


def test_orf_only_gene_is_not_assigned_a_symbol(entry):
    entry["genes"] = [{"orfNames": [{"value": "reference_ORF"}]}]
    result = audit.project(entry, taxonomy(), named(), False)
    assert result["native_gene_annotations"][0]["geneName"] == []
    assert result["source_gene_symbol_assignment"] is None


def test_malformed_native_doi_is_flagged_not_repaired(entry):
    entry["references"][0]["citation"]["citationCrossReferences"].append(
        {"database": "DOI", "id": ".1094/PHYTO-04-18-0128-R"}
    )
    result = audit.project(entry, taxonomy(), named(), False)
    (row,) = result["bibliography"]
    assert {"database": "DOI", "id": ".1094/PHYTO-04-18-0128-R"} in row["identifiers"]
    assert row["identifier_issues"] == [
        {
            "database": "DOI",
            "native_id": ".1094/PHYTO-04-18-0128-R",
            "status": "MALFORMED_NATIVE_DOI_NOT_CORRECTED",
            "replacement": None,
        }
    ]
    assert row["primary_results_reviewed"] is False


def test_reference_strain_does_not_become_an_experimental_subject(entry):
    source = named()
    taxon = {
        "taxonId": 645133,
        "scientificName": "reference strain",
        "rank": "strain",
        "active": True,
        "lineage": source["lineage"],
        "parent": source["species_ancestor"],
    }
    entry["organism"] = {"taxonId": 645133, "scientificName": "reference strain"}
    result = audit.project(entry, taxon, source, False)
    assert result["reference_taxon_id"] == "NCBITaxon:645133"
    assert result["reference_taxon_rank"] == "strain"
    assert result["reference_species_taxon_id"] == "NCBITaxon:31870"
    assert result["experimental_subject_assignment"] is False
    assert result["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "change",
    [
        "sequence",
        "features",
        "comments",
        "review",
        "version",
        "taxid",
        "flag",
        "inactive",
        "organism_name",
        "different_species",
        "nonfungal",
    ],
)
def test_invalid_or_promoted_reference_is_rejected(entry, change):
    taxon, source = taxonomy(), named()
    if change in {"sequence", "features", "comments"}:
        entry[change] = {}
    elif change == "review":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "taxid":
        entry["organism"]["taxonId"] = True
    elif change == "flag":
        entry["proteinDescription"]["flag"] = "Complete"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "organism_name":
        entry["organism"]["scientificName"] = "different"
    elif change == "different_species":
        source["taxon_id"] = "NCBITaxon:1"
    else:
        taxon["lineage"][0]["taxonId"] = 1
        taxon["parent"]["taxonId"] = 1
    with pytest.raises(ValueError):
        audit.project(entry, taxon, source, False)


def test_complete_result_partition_does_not_follow_suggestions(entry, monkeypatch):
    other = copy.deepcopy(entry)
    other["primaryAccession"] = "A0A124"
    other["proteinDescription"]["recommendedName"]["fullName"]["value"] = "Cytochrome b5"
    source = {"url": audit.query_url(31870, False)}
    monkeypatch.setattr(
        audit.native,
        "read_source",
        lambda *args: (
            {"results": [entry, other], "suggestions": [{"query": "broader", "hits": 10}]},
            source,
        ),
    )
    selected, context = audit.read_query(ROOT, source, 31870, False)
    assert selected == [entry] and context["all_result_accessions"] == ["A0A123", "A0A124"]
    assert context["candidate_accessions"] == ["A0A123"]
    assert context["excluded_candidates"][0]["protein_accession"] == "UniProtKB:A0A124"
    assert context["suggestions_followed"] is context["zero_hit_is_biological_absence"] is False


@pytest.mark.parametrize("change", ["pagination", "count", "release", "status", "checksum"])
def test_incomplete_native_response_is_not_a_complete_zero(tmp_path, change):
    body = b'{"results": []}'
    body_path, receipt_path = tmp_path / "body.bin", tmp_path / "receipt.json"
    body_path.write_bytes(body)
    receipt = {
        "url": audit.query_url(31870, True),
        "status": 200,
        "sha256": hashlib.sha256(body).hexdigest(),
        "bytes": len(body),
        "retrieved_at": "test",
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": "0"},
    }
    if change == "pagination":
        receipt["headers"]["link"] = "next"
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
        audit.read_query(tmp_path, source, 31870, True)


@pytest.mark.parametrize("change", [None, "missing", "extra", "wrong_taxon", "nonempty_prior", "stale_prior"])
def test_fallback_requires_a_complete_reviewed_candidate_zero(tmp_path, monkeypatch, change):
    cohort = {"terms": {"ARO:test": {"taxonomy_query_name": "Colletotrichum graminicola"}}}
    (tmp_path / "cohort.json").write_text(json.dumps(cohort))
    name = "Colletotrichum graminicola"
    prior = {name: ([], {"candidate_accessions": [], "complete_for_query": True})}
    request = {
        "name": name,
        "source_taxon_id": 31870,
        "reviewed": False,
        "url": audit.query_url(31870, False),
    }
    plan = {
        "cohort": audit.reference.pin(tmp_path, tmp_path / "cohort.json"),
        "queries": {name: {"request_key": "fallback", "prior_reviewed_query": copy.deepcopy(prior[name][1])}},
        "requests": {"fallback": request},
    }
    if change == "missing":
        plan["queries"] = {}
    elif change == "extra":
        plan["requests"]["extra"] = copy.deepcopy(request)
    elif change == "wrong_taxon":
        request["source_taxon_id"] = 999
    elif change == "nonempty_prior":
        prior[name] = ([{"primaryAccession": "A0A123"}], prior[name][1])
    elif change == "stale_prior":
        plan["queries"][name]["prior_reviewed_query"]["complete_for_query"] = False
    (tmp_path / "unreviewed-plan.json").write_text(json.dumps(plan))
    monkeypatch.setattr(audit, "planned_source", lambda *args: {"url": args[-1]})
    monkeypatch.setattr(audit, "read_query", lambda *args: ([], {"candidate_accessions": []}))
    if change:
        with pytest.raises(ValueError):
            audit.read_queries(tmp_path, tmp_path, cohort, {name: {"selected_taxon": named()}}, False, prior)
    else:
        assert set(
            audit.read_queries(tmp_path, tmp_path, cohort, {name: {"selected_taxon": named()}}, False, prior)
        ) == {name}


def test_public_checkpoint_covers_all_source_terms_and_retains_reference_scope():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads(audit.reference.check_pin(ROOT, data["inputs"]["index"]).read_bytes())
    citations = json.loads(
        audit.reference.check_pin(ROOT, data["inputs"]["definition_citations"]).read_bytes()
    )["terms"]
    labels = {
        r["determinant_id"]: r["determinant_name"]
        for r in csv.DictReader(
            audit.reference.check_pin(ROOT, data["inputs"]["source_inventory"]).open(), delimiter="\t"
        )
    }
    expected = {tid for tid in index["terms"] if audit.SELECT.search(labels[tid])}
    assert set(data["terms"]) == expected and len(expected) == len(data["claims"]) == 6
    assert len(data["records"]) == 4 and len(data["names"]) == 3
    used = set()
    for tid, term in data["terms"].items():
        assert all(term[k] == v for k, v in audit.source_identity(labels[tid]).items())
        assert term["source_label_sha256"] == hashlib.sha256(labels[tid].encode()).hexdigest()
        assert term["definition_citation_ids"] == citations[tid]["definition_citation_ids"] == []
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert term["primary_review_status"] == "OPEN"
        assert term["exact_allele_assignment"] is term["experimental_subject_assignment"] is False
        queries = term["queries"]
        assert ("unreviewed" in queries) is (queries["reviewed"]["candidate_count"] == 0)
        selected = queries.get("unreviewed", queries["reviewed"])
        for query in queries.values():
            excluded = {
                e["protein_accession"].removeprefix("UniProtKB:") for e in query["excluded_candidates"]
            }
            assert not excluded.intersection(query["candidate_accessions"])
            assert excluded | set(query["candidate_accessions"]) == set(query["all_result_accessions"])
            assert query["result_count"] == len(query["all_result_accessions"])
            assert query["zero_hit_is_biological_absence"] is query["suggestions_followed"] is False
        accessions = {c["protein_accession"] for c in term["reference_candidates"]}
        assert accessions == {"UniProtKB:" + a for a in selected["candidate_accessions"]}
        used.update(accessions)
    assert used == set(data["proteins"])
    assert data["summary"]["reference_proteins"] == 7
    assert data["summary"]["term_protein_links"] == 10
    assert data["summary"]["fragment_references"] == 2
    assert data["summary"]["bibliography_identifier_issue_memberships"] == 2
    assert len(data["terms"]["ARO:3009279"]["reference_candidates"]) == 5
    assert data["terms"]["ARO:3009279"]["reference_status"] == "MULTIPLE_CANDIDATES_NO_SELECTION"
    assert data["proteins"]["UniProtKB:E3CU97"]["native_gene_annotations"][0]["geneName"] == []
    assert data["proteins"]["UniProtKB:E3CU97"]["native_gene_annotations"][0]["orfNames"] == ["GLRG_18002"]
    for protein in data["proteins"].values():
        assert protein["exact_resistance_allele"] is protein["experimental_subject_assignment"] is False
        assert protein["source_gene_symbol_assignment"] is protein["experimental_genome_assignment"] is None
    graminicola = data["names"]["Colletotrichum graminicola"]
    assert graminicola["selected_taxon"]["taxon_id"] == "NCBITaxon:31870"
    (mixed,) = [r for r in graminicola["candidates"] if r["taxon_id"] == "NCBITaxon:176297"]
    assert mixed["accepted_name_and_rank"] is False and mixed["matching_fields"] == []
    assert data["constraints"]["issue_1040"] == "DEFERRED"
    assert data["summary"]["whole_record_primary_signoffs"] == 0


@pytest.mark.parametrize("check", [False, True])
def test_cli_never_overwrites_a_checkpoint(tmp_path, monkeypatch, check):
    target = tmp_path / "checkpoint.json"
    target.write_bytes(b"historical\n")
    monkeypatch.setattr(audit, "OUTPUT", target)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    with pytest.raises(ValueError, match="reproduce"):
        audit.main()
    assert target.read_bytes() == b"historical\n"

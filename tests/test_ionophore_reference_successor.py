"""Reference mapping must retain source context and never imply tested alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_ionophore_reference_successor as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in reference audit tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture
def prior():
    return json.loads((ROOT / "research/2026-10-13-ionophore-yeast.json").read_bytes())


@pytest.fixture
def entity():
    return {
        "query_token": "YMR202W",
        "kind": "LOCUS",
        "source_row": 0,
        "source_gene_label": "ERG2",
        "figure_rows": [],
    }


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P32352",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 175, "sequenceVersion": 1},
        "organism": {"taxonId": 559292, "scientificName": audit.TAXON_NAME},
        "genes": [
            {
                "geneName": {"value": "ERG2"},
                "synonyms": [{"value": "ALT2"}],
                "orderedLocusNames": [{"value": "YMR202W"}],
                "orfNames": [{"value": "OLD"}],
            }
        ],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Synthetic name"}}},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000004815"}],
    }


@pytest.fixture
def plan(prior):
    entities = audit.select_entities(prior)
    pending = [k for k in entities if k != audit.REUSED]
    result = {
        "requests": {},
        "automatic_redirects": False,
        "retry_performed": False,
        "corrected_query_size": True,
        "original_failed_attempt_preserved": True,
        "primary_paper_or_access_hold_revisited": False,
        "canary_required_before_remaining_requests": True,
        "ncbi_requests": 0,
    }
    for index, start in enumerate(range(0, len(pending), 50), 1):
        keys = pending[start : start + 50]
        query, url = audit.request_spec(keys, entities)
        result["requests"][f"references-{index:03d}"] = {
            "entity_keys": keys,
            "query": query,
            "url": url,
            "canary": index == 1,
            "maximum_gene_clauses": 50,
        }
    return result, entities


def test_full_source_scope_retains_figure_disagreement(prior, plan):
    result, entities = plan
    audit.validate_plan(result, entities)
    assert len(entities) == 130
    assert sorted(v["source_row"] for v in entities.values() if v["source_row"] is not None) == list(
        range(127)
    )
    assert sorted(i for v in entities.values() for i in v["figure_rows"]) == list(range(7))
    figure = {r["gene"]: r for r in prior["reconstruction_figure"]}
    assert set(figure["ERG24"]["reconstructed_BY_clones"].values()) == {"LETHAL"}
    assert figure["ERG28"]["EUROSCARF_library"] == "Nig resistant"
    assert set(figure["ERG28"]["reconstructed_BY_clones"].values()) == {"Val resistant"}
    assert figure["ERG4"]["SCY325_background"] == "Val hypersensitive"
    assert [len(v["entity_keys"]) for v in result["requests"].values()] == [50, 50, 29]


@pytest.mark.parametrize("change", ["duplicate", "category", "missing", "figure", "locus"])
def test_source_scope_guards(prior, change):
    if change == "duplicate":
        prior["source_rows"][1]["source_locus"] = prior["source_rows"][0]["source_locus"]
    elif change == "category":
        prior["source_rows"][0]["source_category"] = "unclassified"
    elif change == "missing":
        prior["source_rows"].pop()
    elif change == "figure":
        prior["reconstruction_figure"][0]["SCY325_background"] = "resistant"
    else:
        prior["source_rows"][0]["source_locus"] = "wrong"
    with pytest.raises(ValueError):
        audit.select_entities(prior)


@pytest.mark.parametrize(
    "change", ["omit", "duplicate", "overlap", "url", "query", "bound", "canary", "retry", "ncbi", "hold"]
)
def test_plan_guards(plan, change):
    result, entities = plan
    first = result["requests"]["references-001"]
    if change == "omit":
        result["requests"].pop("references-003")
    elif change == "duplicate":
        first["entity_keys"][1] = first["entity_keys"][0]
    elif change == "overlap":
        result["requests"]["references-002"]["entity_keys"][0] = first["entity_keys"][0]
    elif change in {"url", "query"}:
        first[change] += "wrong"
    elif change == "bound":
        first["maximum_gene_clauses"] = 127
    elif change == "canary":
        first["canary"] = False
    elif change == "retry":
        result["retry_performed"] = True
    elif change == "ncbi":
        result["ncbi_requests"] = 1
    else:
        result["primary_paper_or_access_hold_revisited"] = True
    with pytest.raises(ValueError):
        audit.validate_plan(result, entities)


def test_oversize_and_duplicate_query_rejected(plan):
    _, entities = plan
    with pytest.raises(ValueError):
        audit.request_spec(list(entities)[:51], entities)
    with pytest.raises(ValueError):
        audit.request_spec([audit.REUSED, audit.REUSED], entities)


def test_reference_metadata_and_unreviewed_fragment_preserved(entry):
    result = audit.project_reference(entry)
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["reference_species_taxon_id"] == "NCBITaxon:4932"
    assert result["experimental_subject_assignment"] is False
    assert result["experimental_allele_accession"] is None
    assert result["experimental_genome_accession"] is None
    assert result["resistance_inferred_from_reference"] is False
    entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    entry["proteinDescription"]["flag"] = "Fragment"
    entry["proteinDescription"]["submissionNames"] = [entry["proteinDescription"].pop("recommendedName")]
    result = audit.project_reference(entry)
    assert result["fragment_annotation"] is True
    assert result["protein_names"][0]["kind"] == "submissionNames"
    assert result["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert result["database_review_status_is_primary_results_review"] is False


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "taxid",
        "taxname",
        "entrytype",
        "version",
        "boolversion",
        "genes",
        "symbol",
        "name",
        "sgd",
        "duplicate_sgd",
        "flag",
        "sequence",
        "features",
        "comments",
    ],
)
def test_reference_guards(entry, change):
    if change == "accession":
        entry["primaryAccession"] = "bad"
    elif change in {"taxid", "taxname"}:
        entry["organism"]["taxonId" if change == "taxid" else "scientificName"] = "wrong"
    elif change == "entrytype":
        entry["entryType"] = "other"
    elif change in {"version", "boolversion"}:
        entry["entryAudit"]["sequenceVersion"] = True if change == "boolversion" else 0
    elif change == "genes":
        entry["genes"] = []
    elif change == "symbol":
        entry["genes"][0]["synonyms"] = [{"value": ""}]
    elif change == "name":
        entry["proteinDescription"] = {}
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "wrong"
    elif change == "duplicate_sgd":
        entry["uniProtKBCrossReferences"] *= 2
    elif change == "flag":
        entry["proteinDescription"]["flag"] = "unexpected"
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.project_reference(entry)


def test_locus_symbol_orf_and_gene_group_roles_are_not_interchangeable(entry, entity):
    assert audit.match_fields(entry, entity)[0]["field"] == "orderedLocusNames"
    entry["genes"][0]["orfNames"] = entry["genes"][0].pop("orderedLocusNames")
    assert audit.match_fields(entry, entity)[0]["field"] == "orfNames"
    entity["kind"] = "SYMBOL"
    assert audit.match_fields(entry, entity) == []
    entity["query_token"] = "ALT2"
    assert audit.match_fields(entry, entity)[0]["field"] == "synonyms"
    entity["kind"] = "LOCUS"
    assert audit.match_fields(entry, entity) == []
    entity.update(query_token="YMR202W", source_gene_label="OTHER")
    entry["genes"].append({"geneName": {"value": "OTHER"}})
    result = audit.map_entity(entity, [entry])
    assert (
        result["reference_candidates"][0]["source_gene_label_status"]
        == "SOURCE_LABEL_DIFFERS_FROM_CURRENT_GENE_NAMES"
    )


def test_label_difference_nohit_and_ambiguity_remain_explicit(entry, entity):
    entity["source_gene_label"] = "ERG2/ALT2"
    result = audit.map_entity(entity, [entry])
    assert result["source_gene_label"] == "ERG2/ALT2"
    assert (
        result["reference_candidates"][0]["source_gene_label_status"]
        == "SOURCE_LABEL_DIFFERS_FROM_CURRENT_GENE_NAMES"
    )
    assert audit.map_entity(entity, [])["status"] == audit.NO_HIT
    second = copy.deepcopy(entry)
    second["primaryAccession"] = "P12345"
    result = audit.map_entity(entity, [entry, second])
    assert result["status"] == "REFERENCE_ONLY_MULTIPLE_CANDIDATES"
    assert len(result["reference_candidates"]) == 2
    with pytest.raises(ValueError):
        audit.map_entity(entity, [entry, entry])


@pytest.mark.parametrize("kind", ["LOCUS", "SYMBOL"])
def test_one_accession_cannot_hide_multiple_matching_gene_blocks(entry, entity, kind):
    entity["kind"] = kind
    if kind == "SYMBOL":
        entity["query_token"] = "ERG2"
    entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    with pytest.raises(ValueError, match="multiple native gene blocks"):
        audit.match_fields(entry, entity)
    with pytest.raises(ValueError, match="multiple native gene blocks"):
        audit.map_entity(entity, [entry])


@pytest.mark.parametrize("kind", ["LOCUS", "SYMBOL"])
def test_multiple_matching_fields_in_one_gene_block_remain_valid(entry, entity, kind):
    entity["kind"] = kind
    if kind == "SYMBOL":
        entity["query_token"] = "ERG2"
        entry["genes"][0]["synonyms"].append({"value": "ERG2"})
    else:
        entry["genes"][0]["orfNames"].append({"value": entity["query_token"]})
    result = audit.map_entity(entity, [entry])
    assert result["status"] == "REFERENCE_ONLY_FIELD_MATCH"
    matches = result["reference_candidates"][0]["matches"]
    assert len(matches) == 2 and {m["gene_index"] for m in matches} == {0}


@pytest.mark.parametrize("change", ["pagination", "release", "total", "error"])
def test_incomplete_query_cannot_be_a_no_hit(entry, change):
    payload = {"results": [entry]}
    headers = {"X-Total-Results": "1", "X-UniProt-Release": "2026_03"}
    if change == "pagination":
        headers["Link"] = "next"
    elif change == "release":
        headers["X-UniProt-Release"] = "other"
    elif change == "total":
        headers["X-Total-Results"] = "2"
    else:
        payload = {"messages": ["Too many OR conditions in query. Maximum allowed is 100."]}
    with pytest.raises(ValueError):
        audit.complete_query(payload, headers, 1)


@pytest.mark.parametrize(
    "change",
    [
        None,
        "status",
        "attempt",
        "retry",
        "redirect",
        "checksum",
        "pagination",
        "count",
        "release",
        "duplicate",
        "unmatched",
        "wrong_field",
        "ambiguous_gene_blocks",
    ],
)
def test_native_batch_receipt_and_field_binding(tmp_path, plan, entry, change):
    result, entities = plan
    directory = tmp_path / "cache"
    directory.mkdir()
    plan_path = directory / "request-plan.json"
    plan_path.write_text(json.dumps(result))
    item = result["requests"]["references-001"]
    token = entities[item["entity_keys"][0]]["query_token"]
    entry["genes"][0]["orderedLocusNames"] = [{"value": token}]
    if change == "unmatched":
        entry["genes"][0]["orderedLocusNames"] = [{"value": "UNPLANNED"}]
    elif change == "wrong_field":
        entry["genes"][0]["geneName"] = {"value": token}
        entry["genes"][0]["orderedLocusNames"] = []
    elif change == "ambiguous_gene_blocks":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    entries = [entry, entry] if change == "duplicate" else [entry]
    body_path = directory / "references-001-response.bin"
    body_path.write_text(json.dumps({"results": entries}))
    receipt = {
        "url": item["url"],
        "status": 200,
        "bytes": body_path.stat().st_size,
        "sha256": audit.reference.digest(body_path),
        "retrieved_at": "2026-10-14T00:00:00Z",
        "retry_performed": False,
        "redirects_followed": False,
        "headers": {"X-Total-Results": str(len(entries)), "X-UniProt-Release": "2026_03"},
    }
    attempt = {"url": item["url"], "plan_sha256": audit.reference.digest(plan_path), "retry_performed": False}
    if change == "status":
        receipt["status"] = 400
    elif change == "attempt":
        attempt["plan_sha256"] = "wrong"
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "redirect":
        receipt["redirects_followed"] = True
    elif change == "checksum":
        receipt["sha256"] = "wrong"
    elif change == "pagination":
        receipt["headers"]["Link"] = "next"
    elif change == "count":
        receipt["headers"]["X-Total-Results"] = "2"
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "other"
    (directory / "references-001-receipt.json").write_text(json.dumps(receipt))
    (directory / "references-001-attempt.json").write_text(json.dumps(attempt))
    if change is None:
        actual, source = audit.read_batch(tmp_path, Path("cache"), "references-001", result, entities)
        assert actual == entries
        assert source["status"] == 200
    else:
        with pytest.raises(ValueError):
            audit.read_batch(tmp_path, Path("cache"), "references-001", result, entities)


def test_public_projection_is_cache_independent_and_preserves_evidence(prior):
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    entities = audit.select_entities(prior)
    assert set(result["reference_entities"]) == set(entities)
    assert len(result["references"]) == result["summary"]["mapped_entities"] == 130
    assert result["summary"]["unmatched_entities"] == []
    assert result["experimental_context"] == prior["experimental_context"]
    for key, value in prior["interpretation"].items():
        if key != "reference_hold":
            assert result["interpretation"][key] == value
    for key, entity in entities.items():
        row = result["reference_entities"][key]
        assert {k: row[k] for k in entity} == entity
        assert row["experimental_subject_assignment"] is False
        assert row["experimental_allele_accession"] is None
        assert row["experimental_genome_accession"] is None
        assert row["resistance_inferred_from_reference"] is False
        for candidate in row["reference_candidates"]:
            protein = result["references"][candidate["protein_accession"]]
            assert len({m["gene_index"] for m in candidate["matches"]}) == 1
            for match in candidate["matches"]:
                assert entity["query_token"] == match["value"]
                assert match["value"] in protein["genes"][match["gene_index"]][match["field"]]
    assert result["summary"]["source_label_differences"] == [
        "locus:YDR493W",
        "locus:YMR124W",
        "locus:YPR153W",
    ]
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"

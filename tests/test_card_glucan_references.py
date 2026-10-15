"""FKS reference identities must not repair source spellings or establish alleles."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_glucan_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in FKS/FSK audit tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.mark.parametrize("gene", ["FKS1", "Fks1", "FKS2", "FSK1"])
def test_source_gene_spelling_is_not_corrected(gene):
    result = audit.source_identity(f"Candida parapsilosis {gene} beta-1,3-glucan synthase with mutations")
    assert result["source_gene_label"] == gene
    assert result["casefold_gene_query_key"] == gene.casefold()
    assert result["source_claim_wording"] == "beta-1,3-glucan synthase with mutations"
    assert result["spelling_corrected"] is False


@pytest.mark.parametrize(
    "label",
    [
        "Candida FKS1 with mutations",
        "Candida spp. FKS1 with mutations",
        "Candida albicans FKS3 with mutations",
        "Candida albicans FSK2 with mutations",
        "Candida albicans FKS1",
        "glucan synthase",
    ],
)
def test_unreviewed_source_syntax_fails_closed(label):
    with pytest.raises(ValueError):
        audit.source_identity(label)


@pytest.mark.parametrize("gene", ["fks1", "fks2", "fsk1"])
@pytest.mark.parametrize("reviewed", [True, False])
def test_exact_query_identity(gene, reviewed):
    assert audit.query_signature(audit.query_url(gene, 123, reviewed)) == (gene, 123, reviewed)


@pytest.mark.parametrize(
    "gene,species,reviewed",
    [
        ("FKS1", 123, True),
        ("erg11", 123, True),
        ("fks1", True, True),
        ("fks1", 0, True),
        ("fks1", 123, "true"),
    ],
)
def test_query_creation_has_finite_typed_scope(gene, species, reviewed):
    with pytest.raises(ValueError):
        audit.query_url(gene, species, reviewed)


@pytest.mark.parametrize(
    "change",
    [
        "domain",
        "scheme",
        "fragment",
        "duplicate",
        "fields",
        "sequence",
        "fuzzy",
        "or",
        "organism",
        "extra_clause",
        "other_gene",
    ],
)
def test_query_scope_cannot_expand(change):
    url = audit.query_url("fks1", 123, True)
    if change == "domain":
        url = url.replace("rest.uniprot.org", "example.org")
    elif change == "scheme":
        url = url.replace("https:", "http:")
    elif change == "fragment":
        url += "#fragment"
    elif change == "duplicate":
        url += "&query=other"
    else:
        query = "gene_exact:fks1 AND taxonomy_id:123 AND reviewed:true"
        fields = audit.FIELDS
        if change == "fields":
            fields = "accession"
        elif change == "sequence":
            fields += ",sequence"
        elif change == "fuzzy":
            query = query.replace("gene_exact:", "gene:")
        elif change == "or":
            query = query.replace(" AND ", " OR ", 1)
        elif change == "organism":
            query = query.replace("taxonomy_id:", "organism_id:")
        elif change == "extra_clause":
            query += " AND keyword:drug"
        else:
            query = query.replace("fks1", "fks3")
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": query, "fields": fields, "size": 500, "format": "json"}
        )
    with pytest.raises(ValueError):
        audit.query_signature(url)


def test_source_names_may_share_query_but_spelling_and_paralogs_remain_separate():
    terms = {}
    for i, (name, gene) in enumerate(
        [
            ("Candida glabrata", "FKS1"),
            ("Nakaseomyces glabratus", "FKS1"),
            ("Nakaseomyces glabratus", "FSK1"),
            ("Candida glabrata", "FKS2"),
        ]
    ):
        terms[str(i)] = audit.source_identity(f"{name} {gene} with mutations")
    names = {
        name: {"selected_taxon": {"taxon_id": "NCBITaxon:5478"}}
        for name in ("Candida glabrata", "Nakaseomyces glabratus")
    }
    contexts = audit.contexts({"terms": terms}, names)
    assert len(contexts) == 4 and len(audit.query_contexts(contexts)) == 3
    assert {row[0] for row in audit.query_contexts(contexts).values()} == {"fks1", "fks2", "fsk1"}
    assert all(not c["source_spelling_corrected"] for c in contexts.values())
    names["Candida glabrata"]["selected_taxon"] = None
    unresolved = audit.contexts({"terms": terms}, names)
    assert sum(row["query_key"] is None for row in unresolved.values()) == 2


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P12345",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "genes": [
            {
                "geneName": {"value": "FKS1"},
                "synonyms": [{"value": "GSC1"}],
                "orderedLocusNames": [{"value": "LOCUS"}],
                "orfNames": [{"value": "ORF"}],
            }
        ],
        "organism": {"taxonId": 123, "scientificName": "Synthetic fungus"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
    }


def native_source(root, entry, change=None):
    entries = [entry] if entry else []
    body = {"results": entries}
    if change == "suggestions":
        body["suggestions"] = [{"query": "different scope", "hits": 999}]
    payload = json.dumps(body).encode()
    url = audit.query_url("fks1", 123, True)
    receipt = {
        "url": url,
        "status": 200,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "retrieved_at": "2026-10-14T00:00:00Z",
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": str(len(entries))},
    }
    if change == "hash":
        receipt["sha256"] = "wrong"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "99"
    elif change == "link":
        receipt["headers"]["link"] = "next"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "other"
    elif change == "status":
        receipt["status"] = 500
    body_path, receipt_path = root / "body.json", root / "receipt.json"
    body_path.write_bytes(payload)
    receipt_path.write_text(json.dumps(receipt))
    return {
        "url": url,
        "body": audit.reference.pin(root, body_path),
        "receipt": audit.reference.pin(root, receipt_path),
    }


@pytest.mark.parametrize(
    "change", [None, "hash", "count", "link", "release", "status", "spelling", "paralog"]
)
def test_native_query_completeness_and_source_gene_scope(tmp_path, entry, change):
    source = native_source(tmp_path, entry, change)
    gene = "fsk1" if change == "spelling" else "fks2" if change == "paralog" else "fks1"
    if change:
        with pytest.raises(ValueError):
            audit.read_gene(tmp_path, source, gene, 123, True)
    else:
        entries, query = audit.read_gene(tmp_path, source, gene, 123, True)
        assert entries == [entry] and query["result_count"] == 1
        assert not query["zero_hit_is_biological_absence"]


def test_zero_hit_query_and_reference_projection_do_not_assign_alleles(tmp_path, entry):
    source = native_source(tmp_path, None, "suggestions")
    entries, query = audit.read_gene(tmp_path, source, "fks1", 123, True)
    assert not entries and not query["zero_hit_is_biological_absence"]
    assert query["suggestions_ignored"] == 1 and not query["suggestions_followed"]
    parent = {"taxonId": 4751, "rank": "kingdom", "scientificName": "Fungi"}
    taxon = {
        "taxonId": 123,
        "scientificName": "Synthetic fungus",
        "rank": "species",
        "active": True,
        "lineage": [parent],
        "parent": parent,
    }
    result, matches = audit.references.project(entry, taxon, "fks1", 123, True)
    assert matches == [{"gene_index": 0, "field": "geneName", "value": "FKS1"}]
    assert result["ordered_locus_names"] == ["LOCUS"]
    assert result["genes"][0]["orfNames"] == ["ORF"]
    assert not result["exact_resistance_allele"] and not result["experimental_subject_assignment"]
    assert result["experimental_genome_assignment"] is None
    with pytest.raises(ValueError):
        audit.references.project(entry, taxon, "fsk1", 123, True)


@pytest.mark.parametrize("change", [None, "extra", "missing", "held", "unused_request"])
def test_query_plan_accounts_for_every_expected_context(tmp_path, monkeypatch, entry, change):
    source = native_source(tmp_path, entry)
    cohort_path, inventory = tmp_path / "cohort.json", tmp_path / "inventory.json"
    cohort_path.write_text("{}")
    inventory.write_text("{}")
    key = '["fks1",123]'
    plan = {
        "cohort": audit.reference.pin(tmp_path, cohort_path),
        "requests": {},
        "gene_cache_inventory": audit.reference.pin(tmp_path, inventory),
        "queries": {key: {"kind": "REUSED_COMPLETE_QUERY", "source": source}},
    }
    if change == "extra":
        plan["queries"]["extra"] = copy.deepcopy(plan["queries"][key])
    elif change == "missing":
        plan["queries"] = {}
    elif change == "held":
        plan["queries"][key]["kind"] = "HELD_EXISTING_QUERY"
    elif change == "unused_request":
        plan["requests"]["unused"] = {}
    (tmp_path / "reviewed-plan.json").write_text(json.dumps(plan))
    monkeypatch.setattr(audit.references, "check_canary", lambda *args: None)
    if change:
        with pytest.raises(ValueError):
            audit.read_queries(tmp_path, tmp_path, "reviewed-plan.json", {key: ("fks1", 123)}, True)
    else:
        result = audit.read_queries(tmp_path, tmp_path, "reviewed-plan.json", {key: ("fks1", 123)}, True)
        assert result[key][0] == [entry]


@pytest.mark.parametrize("stored_review_status", [True, 1, "true", False])
def test_planned_review_status_must_be_typed_boolean(tmp_path, monkeypatch, stored_review_status):
    plan = {"requests": {"query": {"gene": "fks1", "species_id": 123, "reviewed": stored_review_status}}}
    (tmp_path / "reviewed-plan.json").write_text(json.dumps(plan))
    monkeypatch.setattr(audit, "planned_source", lambda *args: {"url": audit.query_url("fks1", 123, True)})
    monkeypatch.setattr(audit, "read_gene", lambda *args: ([], {}))
    if stored_review_status is True:
        assert audit.planned_gene(tmp_path, tmp_path, "reviewed-plan.json", "query", "fks1", 123, True) == (
            [],
            {},
        )
    else:
        with pytest.raises(ValueError, match="planned gene context"):
            audit.planned_gene(tmp_path, tmp_path, "reviewed-plan.json", "query", "fks1", 123, True)


@pytest.mark.parametrize("count", [0, 1, 3])
def test_fallback_keeps_all_candidates_only_for_reviewed_zero(tmp_path, monkeypatch, entry, count):
    key = '["fks1",123]'
    source_contexts = {"context": {"query_key": key, "gene_query_key": "fks1", "species_id": 123}}
    reviewed = {"source": {"native": "pinned"}, "result_count": 0, "reviewed_subset": True}
    plan_path = tmp_path / "unreviewed-plan.json"
    plan_path.write_text(json.dumps({"reviewed_sources": {key: reviewed["source"]}}))
    entries = [{**entry, "primaryAccession": f"P{i:05d}"} for i in range(count)]

    def query_stub(root, directory, filename, expected, is_reviewed):
        if is_reviewed:
            assert expected == {key: ("fks1", 123)}
            return {key: ([], reviewed)}
        assert expected == {key: ("fks1", 123)}
        return {key: (entries, {"result_count": count, "reviewed_subset": False})}

    monkeypatch.setattr(audit, "read_queries", query_stub)
    result = audit.selected_queries(tmp_path, tmp_path, source_contexts)[key]
    assert result["entries"] == entries
    assert (
        result["status"]
        == {
            0: "NO_EXACT_GENE_RESULTS_NOT_ABSENCE",
            1: "UNREVIEWED_CANDIDATE",
            3: "MULTIPLE_CANDIDATES_NO_SELECTION",
        }[count]
    )
    reviewed["source"] = {"changed": "evidence"}
    with pytest.raises(ValueError, match="fallback evidence"):
        audit.selected_queries(tmp_path, tmp_path, source_contexts)


@pytest.mark.parametrize(
    "change", [None, "othernames_only", "review", "taxid", "inactive", "unexpected_name"]
)
def test_formal_nomenclature_does_not_turn_othernames_into_native_synonyms(tmp_path, monkeypatch, change):
    name = "Nakaseomyces glabratus" if change != "unexpected_name" else "Unreviewed fungus"
    parent = {"taxonId": 4751, "rank": "kingdom", "scientificName": "Fungi"}
    taxon = {
        "taxonId": 5478,
        "scientificName": "Candida glabrata",
        "rank": "species",
        "active": True,
        "lineage": [parent],
        "parent": parent,
        "otherNames": [name],
    }
    if change == "inactive":
        taxon["active"] = False
    source = {"url": "https://rest.uniprot.org/taxonomy/5478"}
    review = {"specific_review": "pinned evidence"}
    prior = {"nomenclature_assessment": review, "names": {name: {"source": source}}}
    prior_path = tmp_path / "prior.json"
    prior_path.write_text(json.dumps(prior))
    item = {"kind": "REUSED_PRIMARY_NOMENCLATURE", "source": source, "review": copy.deepcopy(review)}
    if change == "othernames_only":
        item["kind"] = "REUSED_NATIVE_NAME"
        item.pop("review")
    elif change == "review":
        item["review"]["specific_review"] = "different evidence"
    cohort = {
        "prior_fungal_references": audit.reference.pin(tmp_path, prior_path),
        "terms": {"term": {"source_organism_name": name}},
        "names": {name: item},
    }
    cohort_path = tmp_path / "cohort.json"
    cohort_path.write_text(json.dumps(cohort))
    (tmp_path / "names-plan.json").write_text(
        json.dumps({"cohort": audit.reference.pin(tmp_path, cohort_path), "requests": {}})
    )
    monkeypatch.setattr(audit.native, "read_source", lambda *args: ({"results": [taxon]}, source))

    def nomenclature_stub(root, supplied_review, body):
        assert supplied_review == review and body["results"] == [taxon]
        return {"species_id": 999 if change == "taxid" else 5478, "scientific_name": "Candida glabrata"}

    monkeypatch.setattr(audit.fungal, "nomenclature", nomenclature_stub)
    if change in {"review", "taxid", "inactive", "unexpected_name"}:
        with pytest.raises(ValueError):
            audit.read_names(tmp_path, tmp_path, cohort)
    else:
        result = audit.read_names(tmp_path, tmp_path, cohort)[name]
        assert result["source_name"] == name
        if change == "othernames_only":
            assert result["selected_taxon"] is None and result["nomenclature"] is None
        else:
            assert result["native_match_name"] == "Candida glabrata"
            assert result["status"] == "PRIMARY_NOMENCLATURE_PLUS_NATIVE_REFERENCE"
            assert result["native_name_resolution_status"] == "EXACT_NATIVE_NAME_REFERENCE"
            assert result["matching_fields_apply_to"] == "native_match_name"
            assert result["selected_taxon"]["taxon_id"] == "NCBITaxon:5478"
            assert result["experimental_subject_assignment"] is False


def test_public_checkpoint_preserves_all_terms_and_source_spelling():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    labels = {
        r["determinant_id"]: r["determinant_name"]
        for r in csv.DictReader((ROOT / "data/raw/aro_resistance_edges.tsv").open(), delimiter="\t")
    }
    index = json.loads((ROOT / result["inputs"]["index"]["path"]).read_bytes())
    expected = {tid for tid in index["terms"] if audit.SELECT.search(labels[tid])}
    assert set(result["terms"]) == expected and len(expected) == 47
    assert len(result["claims"]) == 47 and len(result["records"]) == 8
    assert len(result["source_contexts"]) == 16 and len(result["query_contexts"]) == 14
    assert len(result["names"]) == 12
    spellings = []
    for tid, term in result["terms"].items():
        assert term["source_label"] == labels[tid]
        assert term["source_label_sha256"] == hashlib.sha256(labels[tid].encode()).hexdigest()
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        for key, value in audit.source_identity(labels[tid]).items():
            assert term[key] == value
        if term["casefold_gene_query_key"] == "fsk1":
            spellings.append(tid)
            assert not term["reference_candidates"]
        assert term["experimental_subject_assignment"] is False
        assert term["exact_allele_assignment"] is False
        assert term["experimental_genome_assignment"] is None
        assert term["primary_review_status"] == "OPEN"
        context = result["source_contexts"][term["source_context"]]
        assert term["reference_candidates"] == [
            c["protein_accession"] for c in context["reference_candidates"]
        ]
    assert len(spellings) == 5
    for key, context in result["query_contexts"].items():
        assert json.loads(key) == [context["gene"], context["species_id"]]
        assert context["status"] == audit.fungal.disposition(list(context["queries"].values()))
        selected = context["queries"].get("unreviewed", context["queries"]["reviewed"])
        assert len(context["reference_candidates"]) == selected["result_count"]
        assert {c["protein_accession"] for c in context["reference_candidates"]} <= set(result["proteins"])
    formal = result["names"]["Nakaseomyces glabratus"]
    assert formal["evidence_kind"] == "REUSED_PRIMARY_NOMENCLATURE"
    assert formal["status"] == "PRIMARY_NOMENCLATURE_PLUS_NATIVE_REFERENCE"
    assert formal["native_match_name"] == "Candida glabrata"
    assert formal["nomenclature"]["doi"] == "10.3314/mmj.22.004"
    assert len(result["proteins"]) == 100
    assert sum(p is not None for p in result["inputs"]["canaries"].values()) == 3
    assert result["inputs"]["canaries"]["taxonomy-plan.json"] is None
    assert result["summary"]["native_protein_flags"] == {"Fragment": 87, "None": 13}
    for protein in result["proteins"].values():
        assert not protein["exact_resistance_allele"] and not protein["experimental_subject_assignment"]
        assert protein["experimental_genome_assignment"] is None
        assert not protein["resistance_inferred_from_reference"]
    assert all(
        not q["suggestions_followed"]
        for c in result["query_contexts"].values()
        for q in c["queries"].values()
    )
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"

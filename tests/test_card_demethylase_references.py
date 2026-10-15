"""Reference searches never establish experimental alleles or select a representative."""

import copy
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
import audit_card_demethylase_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in reference audit tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


def url(query="gene_exact:erg11 AND taxonomy_id:123 AND reviewed:true", **kwargs):
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": query, "format": "json", "fields": audit.FIELDS, "size": 500, **kwargs}
    )


@pytest.mark.parametrize("gene", ["CYP51", "cyp51a", "Cyp51B", "cyp51c", "ERG11"])
@pytest.mark.parametrize("reviewed", [True, False])
def test_exact_query_signature(gene, reviewed):
    query = f"(gene_exact:{gene} AND taxonomy_id:123 AND reviewed:{str(reviewed).lower()})"
    assert audit.query_signature(url(query)) == (gene.casefold(), 123, reviewed)


@pytest.mark.parametrize(
    "query",
    [
        "gene:erg11 AND taxonomy_id:123 AND reviewed:true",
        "gene_exact:erg11 OR taxonomy_id:123 AND reviewed:true",
        "gene_exact:erg11 AND organism_id:123 AND reviewed:true",
        "gene_exact:erg11 AND taxonomy_id:0 AND reviewed:true",
        "gene_exact:erg11 AND taxonomy_id:123 AND reviewed:yes",
        "gene_exact:erg11 AND taxonomy_id:123 AND reviewed:true AND keyword:drug",
        "gene_exact:cyp51d AND taxonomy_id:123 AND reviewed:true",
        "((gene_exact:erg11 AND taxonomy_id:123 AND reviewed:true))",
    ],
)
def test_query_scope_cannot_expand(query):
    with pytest.raises(ValueError):
        audit.query_signature(url(query))


@pytest.mark.parametrize(
    "value",
    [
        url().replace("https:", "http:"),
        url().replace("rest.uniprot.org", "example.org"),
        url().replace("/search?", "/P12345?"),
        url() + "#fragment",
        url() + "&query=other",
        url() + "&extra=true",
        url(fields="accession"),
        url(fields=audit.FIELDS + ",sequence"),
        url(format="tsv"),
    ],
)
def test_unsupported_endpoint_or_payload_fields_rejected(value):
    with pytest.raises(ValueError):
        audit.query_signature(value)


@pytest.fixture
def entry():
    return {
        "primaryAccession": "P12345",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 3, "sequenceVersion": 1},
        "genes": [
            {
                "geneName": {"value": "ERG11"},
                "synonyms": [{"value": "CYP51"}],
                "orderedLocusNames": [{"value": "LOC_1"}],
                "orfNames": [{"value": "ORF_1"}],
            }
        ],
        "organism": {"taxonId": 123, "scientificName": "Synthetic fungus"},
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Reference protein"}},
            "flag": "Fragment",
        },
        "references": [
            {
                "referencePositions": ["NONEXPORTABLE_SOURCE_ANNOTATION"],
                "citation": {
                    "publicationDate": "2020",
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "12345"},
                        {"database": "DOI", "id": "10.0000/example"},
                    ],
                },
            }
        ],
    }


@pytest.fixture
def taxon():
    parent = {"taxonId": 4751, "scientificName": "Fungi", "rank": "kingdom"}
    return {
        "taxonId": 123,
        "scientificName": "Synthetic fungus",
        "rank": "species",
        "active": True,
        "lineage": [parent],
        "parent": parent,
    }


@pytest.mark.parametrize(
    "change",
    [
        "review_status",
        "sequence",
        "features",
        "comments",
        "duplicate",
        "duplicate_gene",
        "wrong_gene",
        "orf_only",
        "version_zero",
        "version_bool",
        "version_missing",
        "taxon_bool",
        "taxon_zero",
    ],
)
def test_invalid_reference_entries_fail_closed(entry, change):
    entries = [entry]
    if change == "review_status":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "outside reference scope"
    elif change == "duplicate":
        entries.append(copy.deepcopy(entry))
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "wrong_gene":
        entry["genes"] = [{"geneName": {"value": "CYP51B"}}]
    elif change == "orf_only":
        entry["genes"] = [{"orfNames": [{"value": "ERG11"}]}]
    elif change.startswith("version_"):
        entry["entryAudit"]["entryVersion"] = {
            "version_zero": 0,
            "version_bool": True,
            "version_missing": None,
        }[change]
    elif change.startswith("taxon_"):
        entry["organism"]["taxonId"] = True if change == "taxon_bool" else 0
    with pytest.raises(ValueError):
        audit.validate_entries(entries, "erg11", True)


@pytest.mark.parametrize("reviewed", [True, False])
def test_reference_projection_preserves_flags_gene_roles_and_evidence_boundary(entry, taxon, reviewed):
    if not reviewed:
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    result, matches = audit.project(entry, taxon, "erg11", 123, reviewed)
    assert matches == [{"gene_index": 0, "field": "geneName", "value": "ERG11"}]
    assert result["genes"][0]["orfNames"] == ["ORF_1"]
    assert result["genes"][0]["orderedLocusNames"] == ["LOC_1"]
    assert result["native_protein_flag"] == "Fragment"
    assert result["unflagged_means_complete"] is False
    assert result["exact_resistance_allele"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["database_review_status_is_primary_results_review"] is False
    assert result["resistance_inferred_from_reference"] is False
    assert result["reference_organism_label_matches_taxonomy"] is True
    assert result["reference_species_taxon_id"] == "NCBITaxon:123"
    assert "NONEXPORTABLE" not in json.dumps(result)
    assert result["bibliography"][0]["primary_results_reviewed"] is False
    _, alias = audit.project(entry, taxon, "cyp51", 123, reviewed)
    assert alias == [{"gene_index": 0, "field": "synonyms", "value": "CYP51"}]


@pytest.mark.parametrize(
    "change", ["inactive", "wrong_species", "wrong_leaf", "not_fungi", "cycle", "parent", "no_species"]
)
def test_taxonomic_ancestry_is_required(entry, taxon, change):
    species = 123
    if change == "inactive":
        taxon["active"] = False
    elif change == "wrong_species":
        species = 124
    elif change == "wrong_leaf":
        entry["organism"]["taxonId"] = 124
    elif change == "not_fungi":
        taxon["lineage"][0]["taxonId"] = 1
    elif change == "cycle":
        taxon["lineage"].append({k: taxon[k] for k in ("taxonId", "rank", "scientificName")})
    elif change == "parent":
        taxon["parent"] = {"taxonId": 999, "scientificName": "Wrong parent"}
    elif change == "no_species":
        taxon["rank"] = "genus"
    with pytest.raises(ValueError):
        audit.project(entry, taxon, "erg11", species, True)


def test_strain_reference_is_not_source_organism_assignment(entry, taxon):
    parent = {k: taxon[k] for k in ("taxonId", "rank", "scientificName")}
    taxon.update(taxonId=456, rank="strain", scientificName="Synthetic fungus reference strain")
    taxon["lineage"].append(parent)
    taxon["parent"] = parent
    entry["organism"] = {"taxonId": 456, "scientificName": "Alternate reference strain label"}
    result, _ = audit.project(entry, taxon, "erg11", 123, True)
    assert result["reference_taxon_id"] == "NCBITaxon:456"
    assert result["reference_species_taxon_id"] == "NCBITaxon:123"
    assert result["reference_organism_label_matches_taxonomy"] is False
    assert not result["experimental_subject_assignment"]


def write_source(root, entries, change=None):
    payload = json.dumps({"results": entries}).encode()
    receipt = {
        "url": url(),
        "status": 200,
        "retrieved_at": "2026-10-14T00:00:00Z",
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": str(len(entries))},
    }
    if change == "count":
        receipt["headers"]["x-total-results"] = "99"
    elif change == "link":
        receipt["headers"]["link"] = "next page"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "2025_01"
    elif change == "status":
        receipt["status"] = 500
    elif change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "url":
        receipt["url"] = url().replace("123", "124")
    body_path, receipt_path = root / "body.json", root / "receipt.json"
    body_path.write_bytes(payload)
    receipt_path.write_text(json.dumps(receipt))
    return {
        "url": url(),
        "body": audit.reference.pin(root, body_path),
        "receipt": audit.reference.pin(root, receipt_path),
    }


@pytest.mark.parametrize("change", [None, "count", "link", "release", "status", "hash", "bytes", "url"])
def test_native_transport_completeness(tmp_path, entry, change):
    source = write_source(tmp_path, [entry], change)
    if change:
        with pytest.raises(ValueError):
            audit.read_gene_source(tmp_path, source, "erg11", 123, True)
    else:
        entries, query = audit.read_gene_source(tmp_path, source, "erg11", 123, True)
        assert entries == [entry] and query["result_count"] == 1
        assert query["complete_for_query"] and not query["zero_hit_is_biological_absence"]


@pytest.mark.parametrize(
    "gene,species,reviewed", [("cyp51", 123, True), ("erg11", 124, True), ("erg11", 123, False)]
)
def test_cached_response_requires_exact_query_scope(tmp_path, entry, gene, species, reviewed):
    source = write_source(tmp_path, [entry])
    with pytest.raises(ValueError):
        audit.read_gene_source(tmp_path, source, gene, species, reviewed)


def test_zero_hits_are_not_biological_absence(tmp_path):
    source = write_source(tmp_path, [])
    entries, query = audit.read_gene_source(tmp_path, source, "erg11", 123, True)
    assert entries == [] and query["result_count"] == 0
    assert not query["zero_hit_is_biological_absence"]


@pytest.mark.parametrize("count", [0, 1, 3])
def test_fallback_preserves_every_candidate_only_after_reviewed_zero(tmp_path, monkeypatch, entry, count):
    context = {
        "casefold_gene_query_key": "erg11",
        "named_reference_taxon_id": "NCBITaxon:123",
        "unreviewed_cached_query": None,
    }
    cohort = {"contexts": {"synthetic": context}}
    path = tmp_path / "cohort.json"
    path.write_text(json.dumps(cohort))
    descriptor = {"kind": "NEW_PLANNED_QUERY", "request_key": "fallback"}
    plan = {
        "cohort": audit.reference.pin(tmp_path, path),
        "contexts": {"synthetic": descriptor},
        "requests": {"fallback": {"context": "synthetic"}},
        "reviewed_sources": {"synthetic": {}},
    }
    plan_path = tmp_path / "unreviewed-plan.json"
    plan_path.write_text(json.dumps(plan))
    reviewed = {"reviewed_subset": True, "result_count": 0, "gene_query_key": "erg11", "species_id": 123}
    reviewed["source"] = {}
    monkeypatch.setattr(audit, "reviewed_queries", lambda *args: {"synthetic": ([], reviewed)})
    entries = [{**entry, "primaryAccession": f"P{index:05d}"} for index in range(count)]
    fallback = {"reviewed_subset": False, "result_count": count}
    monkeypatch.setattr(audit, "read_planned_gene", lambda *args: (entries, fallback))
    result = audit.selected_queries(tmp_path, tmp_path, cohort)["synthetic"]
    assert result["entries"] == entries
    assert (
        result["status"]
        == {
            0: "NO_EXACT_GENE_RESULTS_NOT_ABSENCE",
            1: "UNREVIEWED_CANDIDATE",
            3: "MULTIPLE_CANDIDATES_NO_SELECTION",
        }[count]
    )
    reviewed["result_count"] = 1
    monkeypatch.setattr(audit, "reviewed_queries", lambda *args: {"synthetic": ([entry], reviewed)})
    with pytest.raises(ValueError, match="exactly the reviewed zero-hit"):
        audit.selected_queries(tmp_path, tmp_path, cohort)
    reviewed["source"] = {"different": "native evidence"}
    with pytest.raises(ValueError, match="reviewed-source evidence"):
        audit.selected_queries(tmp_path, tmp_path, cohort)


@pytest.mark.parametrize(
    "change", [None, "plan", "attempt_url", "retry", "redirect", "gene", "species", "reviewed"]
)
def test_planned_query_is_bound_to_frozen_context_and_attempt(tmp_path, entry, change):
    source = write_source(tmp_path, [entry])
    body_path = tmp_path / "canary-response.bin"
    body_path.write_bytes((tmp_path / "body.json").read_bytes())
    receipt = json.loads((tmp_path / "receipt.json").read_bytes())
    receipt.update(retry_performed=False, redirects_followed=False)
    item = {"url": source["url"], "gene": "erg11", "species_id": 123, "reviewed": True}
    if change in {"gene", "species", "reviewed"}:
        key, value = {
            "gene": ("gene", "cyp51"),
            "species": ("species_id", 124),
            "reviewed": ("reviewed", False),
        }[change]
        item[key] = value
    plan_path = tmp_path / "reviewed-plan.json"
    plan_path.write_text(json.dumps({"requests": {"canary": item}}))
    attempt = {
        "url": source["url"],
        "plan_sha256": audit.reference.digest(plan_path),
        "retry_performed": False,
    }
    if change == "plan":
        attempt["plan_sha256"] = "wrong"
    elif change == "attempt_url":
        attempt["url"] = "https://example.org/"
    elif change == "retry":
        attempt["retry_performed"] = True
    elif change == "redirect":
        receipt["redirects_followed"] = True
    (tmp_path / "canary-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "canary-receipt.json").write_text(json.dumps(receipt))
    context = {"casefold_gene_query_key": "erg11", "named_reference_taxon_id": "NCBITaxon:123"}
    if change:
        with pytest.raises(ValueError):
            audit.read_planned_gene(tmp_path, Path("."), "canary", "reviewed-plan.json", context, True)
    else:
        entries, _ = audit.read_planned_gene(
            tmp_path, Path("."), "canary", "reviewed-plan.json", context, True
        )
        assert entries == [entry]


@pytest.mark.parametrize("change", [None, "manual", "experimental", "plan", "body", "receipt"])
def test_canary_review_remains_bound_to_inspected_bytes(tmp_path, change):
    plan_path = tmp_path / "reviewed-plan.json"
    plan_path.write_text(json.dumps({"requests": {"canary": {}}, "canary_request": "canary"}))
    for suffix in ("response.bin", "receipt.json"):
        (tmp_path / ("canary-" + suffix)).write_text("{}")
    review = {
        "manually_inspected": True,
        "experimental_assignments": False,
        "plan": audit.reference.pin(tmp_path, plan_path),
        "body": audit.reference.pin(tmp_path, tmp_path / "canary-response.bin"),
        "receipt": audit.reference.pin(tmp_path, tmp_path / "canary-receipt.json"),
    }
    if change == "manual":
        review["manually_inspected"] = False
    elif change == "experimental":
        review["experimental_assignments"] = True
    elif change:
        review[change]["sha256"] = "wrong"
    review_path = tmp_path / "reviewed-canary-review.json"
    review_path.write_text(json.dumps(review))
    if change:
        with pytest.raises(ValueError):
            audit.check_canary(tmp_path, tmp_path, "reviewed-plan.json")
    else:
        assert audit.check_canary(tmp_path, tmp_path, "reviewed-plan.json") == audit.reference.pin(
            tmp_path, review_path
        )


def test_saved_public_cohort_retains_full_memberships_and_no_experimental_claims():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    prior = json.loads((ROOT / audit.source_audit.OUTPUT).read_bytes())
    assert result["claims"] == prior["claims"] and result["records"] == prior["records"]
    assert set(result["terms"]) == set(prior["terms"]) and len(result["terms"]) == 137
    assert len(result["gene_contexts"]) == 45
    assert result["summary"]["queried_gene_contexts"] == 39
    for key, context in result["gene_contexts"].items():
        assert not context["experimental_assignments"]
        old = prior["gene_name_contexts"][key]
        for field, value in old.items():
            if field != "protein_query_status":
                assert context[field] == value
        queries = context["queries"]
        if queries:
            assert context["status"] == audit.fungal.disposition(list(queries.values()))
            selected = queries.get("unreviewed", queries["reviewed"])
            assert selected["result_count"] == len(context["reference_candidates"])
        else:
            assert context["status"] == "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY"
        for candidate in context["reference_candidates"]:
            assert candidate["protein_accession"] in result["proteins"]
            assert (
                not candidate["exact_resistant_allele"] and not candidate["experimental_subject_assignment"]
            )
        for term in context["terms"]:
            assert result["terms"][term]["gene_context"] == key
    for protein in result["proteins"].values():
        assert not protein["exact_resistance_allele"]
        assert not protein["experimental_subject_assignment"]
        assert protein["experimental_genome_assignment"] is None
        assert not protein["resistance_inferred_from_reference"]
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"

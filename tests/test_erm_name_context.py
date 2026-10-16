"""Native gene names and reference taxonomy must not become experimental alleles."""

import builtins
import copy
import csv
import hashlib
import io
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_erm_name_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize("key", audit.FALSE_FIELDS)
def test_scope_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "key",
    [
        "reference_gene_name_rewritten",
        "source_regulatory_contexts_interchangeable",
        "all_record_structures_tested",
        "experimental_allele_identity_established",
    ],
)
def test_primary_context_limits_are_retained(key):
    notes = assessment()
    notes["primary_paper"][key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize("change", ["gene", "species", "reference", "doi", "ncbi", "visual"])
def test_primary_identity_and_access_cannot_be_rewritten(change):
    notes = assessment()
    if change == "gene":
        notes["primary_paper"]["source_gene_label"] = "ermC"
    elif change == "species":
        notes["primary_paper"]["source_species"] = "Staphylococcus aureus"
    elif change == "reference":
        notes["primary_paper"]["reference_accession"] = "UniProtKB:P0A0H3"
    elif change == "doi":
        notes["primary_paper"]["doi"] = "10.invalid"
    elif change == "ncbi":
        notes["access"]["ncbi_requests"] = 1
    else:
        notes["access"]["screenshot_images_exposed_for_visual_inspection"] = True
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


@pytest.mark.parametrize(
    "label,genes,status",
    [
        ("ErmC", [{"geneName": {"value": "ermC"}}], "CASEFOLDED_NATIVE_SYMBOL_MATCH_NOT_ALLELE_IDENTITY"),
        (
            "ErmB",
            [{"geneName": {"value": "erm(B)"}, "synonyms": [{"value": "ermB"}]}],
            "CASEFOLDED_NATIVE_SYNONYM_MATCH_NOT_ALLELE_IDENTITY",
        ),
        ("Erm(51)", [{"geneName": {"value": "erm_51"}}], "PUNCTUATION_ONLY_SIMILARITY_NOT_ALIAS_PROOF"),
        (
            "ErmC",
            [{"geneName": {"value": "ermM"}}],
            "DIFFERENT_NATIVE_NAME_REQUIRES_CONTEXT_NOT_AUTOMATIC_ERROR",
        ),
        (
            "Erm(44)v",
            [{"geneName": {"value": "erm(44)"}}],
            "DIFFERENT_NATIVE_NAME_REQUIRES_CONTEXT_NOT_AUTOMATIC_ERROR",
        ),
        ("Erm(37)", [{"orderedLocusNames": [{"value": "LOCUS"}]}], "NO_NATIVE_SYMBOL_LOCUS_FIELDS_ONLY"),
        ("Erm(34)", [], "GENE_FIELD_ABSENT_NOT_GENE_ABSENCE"),
    ],
)
def test_lexical_comparison_never_establishes_alleles(label, genes, status):
    result = audit.lexical_relation(label, {"genes": genes})
    assert result["status"] == status
    assert result["biological_equivalence_inferred"] is False


def write_source(root, rows):
    path = root / "source.tsv"
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["determinant_id", "determinant_name"], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    return audit.reference.pin(root, path)


def test_cohort_uses_all_current_erm_terms_not_every_raw_inventory_term(tmp_path):
    rows = [
        {"determinant_id": "CURRENT", "determinant_name": "ErmC"},
        {"determinant_id": "RAW_ONLY", "determinant_name": "ErmOther"},
        {"determinant_id": "NOT_ERM", "determinant_name": "another gene"},
    ]
    source = write_source(tmp_path, rows)
    index = {"terms": {"CURRENT": {}, "NOT_ERM": {}}}
    assert audit.cohort(tmp_path, source, index) == {"CURRENT": "ErmC"}
    index["terms"]["MISSING"] = {}
    with pytest.raises(ValueError, match="lacks a source label"):
        audit.cohort(tmp_path, source, index)


def test_conflicting_source_labels_are_rejected(tmp_path):
    source = write_source(
        tmp_path, [{"determinant_id": "X", "determinant_name": name} for name in ("ErmA", "ErmB")]
    )
    with pytest.raises(ValueError, match="conflicting labels"):
        audit.cohort(tmp_path, source, {"terms": {"X": {}}})


def followup_fixture(root, mutation=None):
    old = {"searches": {}, "requests": {}, "proteins": {}}

    def save(name, value):
        path = root / name
        path.write_text(json.dumps(value))
        return audit.reference.pin(root, path)

    for number in range(9):
        accession = f"TEST{number}"
        entry = {
            "primaryAccession": accession,
            "genes": [{"geneName": {"value": f"erm{number}"}}],
            "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
            "organism": {"taxonId": number + 1},
        }
        payload = [entry] if number < 8 else []
        if payload:
            old["proteins"][accession] = {
                "gene_annotations": copy.deepcopy(entry["genes"]),
                "entry_audit": copy.deepcopy(entry["entryAudit"]),
                "organism": copy.deepcopy(entry["organism"]),
            }
        query = f"gene:erm{number}"
        params = {"query": query, "size": "500", "format": "json", "fields": "accession,gene_names"}
        headers = {"X-UniProt-Release": "2026_03", "X-Total-Results": str(len(payload))}
        if number == 0:
            if mutation == "sequence_query":
                params["fields"] += ",sequence"
            elif mutation == "sequence_payload":
                entry["sequence"] = {}
            elif mutation == "pagination":
                headers["Link"] = "<https://rest.uniprot.org/next>; rel=next"
            elif mutation == "release":
                headers["X-UniProt-Release"] = "2026_04"
            elif mutation == "count":
                headers["X-Total-Results"] = "2"
            elif mutation == "duplicate":
                payload.append(copy.deepcopy(entry))
            elif mutation == "gene":
                entry["genes"][0]["geneName"]["value"] = "different"
            elif mutation == "version":
                entry["entryAudit"]["entryVersion"] = 2
            elif mutation == "taxon":
                entry["organism"]["taxonId"] = 999
        cache = save(f"body-{number}.json", {"results": payload})
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
        receipt = {
            "url": url,
            "headers": headers,
            "status": 200,
            "cache_path": cache["path"],
            "bytes": (root / cache["path"]).stat().st_size,
            "sha256": cache["sha256"],
        }
        request = {**receipt, "cache": cache}
        if number == 0:
            if mutation == "status":
                receipt["status"] = 503
            elif mutation == "checksum":
                receipt["sha256"] = "0" * 64
            elif mutation == "query":
                query = "gene:different"
        request["receipt"] = save(f"receipt-{number}.json", receipt)
        old["requests"][str(number)] = request
        old["searches"][str(number)] = {
            "query": query,
            "result_count": 1 if number < 8 else 0,
            "accessions": [accession] if number < 8 else [],
        }
    return old


def test_native_followup_replays_complete_queries_including_zero_hit(tmp_path):
    old = followup_fixture(tmp_path)
    entries, provenance = audit.native_followup(tmp_path, old)
    assert set(entries) == set(old["proteins"])
    assert len(entries) == 8 and len(provenance) == 9


@pytest.mark.parametrize(
    "mutation",
    [
        "sequence_query",
        "sequence_payload",
        "pagination",
        "release",
        "count",
        "duplicate",
        "gene",
        "version",
        "taxon",
        "status",
        "checksum",
        "query",
    ],
)
def test_native_followup_rejects_provenance_and_identity_drift(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.native_followup(tmp_path, followup_fixture(tmp_path, mutation))


def test_portable_artifact_preserves_complete_claim_and_candidate_context(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    plan = audit.read_json(ROOT, result["plan"])
    audit.validate_assessment(audit.read_json(ROOT, result["assessment"]))
    index = audit.read_json(ROOT, result["inputs"]["index"])
    labels = audit.cohort(ROOT, plan["source_inventory"], index)
    old = audit.read_json(ROOT, result["prior_erm"])
    definitions = audit.read_json(ROOT, plan["definition_citations"])
    assert set(result["terms"]) == set(labels) and len(labels) == 47
    assert len(result["claims"]) == len(result["claim_dispositions"]) == 562
    assert len(result["records"]) == 32
    update = audit.read_json(ROOT, result["inputs"]["corpus_update"])
    deltas = {r["identifier"]: r for r in update["record_deltas"]}
    expected_claims = copy.deepcopy([c for c in index["claims"] if c["aro_id"] in labels])
    records = {r["identifier"]: r for r in result["records"]}
    for claim in expected_claims:
        delta = deltas.get(claim["record_identifier"])
        if delta:
            assert claim["record_sha256"] == delta["before_sha256"]
            claim["record_sha256"] = delta["after_sha256"]
        assert claim["record_sha256"] == records[claim["record_identifier"]]["record_sha256"]
    assert result["claims"] == expected_claims
    claim_keys = {
        (c["aro_id"], c["record_identifier"], c["claim_sha256"], c["standard_inchi_key"])
        for c in result["claims"]
    }
    assert len(claim_keys) == 562
    assert claim_keys == {
        (c["aro_id"], c["record_identifier"], c["claim_sha256"], c["standard_inchi_key"])
        for c in result["claim_dispositions"]
    }
    for term, row in result["terms"].items():
        assert row["source_label"] == labels[term]
        assert row["source_label_sha256"] == hashlib.sha256(labels[term].encode()).hexdigest()
        assert row["source_label_sha256"] == index["terms"][term]["source_label_sha256"]
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert row["selected_index_links"] == index["terms"][term]["links"]
        assert row["definition_citation_ids"] == definitions["terms"][term]["definition_citation_ids"]
        assert row["earlier_candidate_context"] == old["candidates"].get(term)
        selected = {link["protein_accession"] for link in row["selected_index_links"]}
        assert set(row["native_name_relations"]) == selected | set(
            row["prior_candidates_not_in_selected_index"]
        )
        assert not selected & set(row["prior_candidates_not_in_selected_index"])
    assert sum(len(r["prior_candidates_not_in_selected_index"]) for r in result["terms"].values()) == 5
    assert len(result["reference_views"]) == 49 and len(result["taxonomy_sources"]) == 40
    assert result["prior_identity_limits"] == old["identity_limits"]
    assert result["prior_primary_contexts"] == old["primary_papers"]
    assert result["preserved_erm36_hold"] == audit.read_json(ROOT, plan["erm36_hold"])
    assert result["preserved_erm55_curation"] == plan["erm55_curation"]
    view = result["reference_views"]["UniProtKB:P06572"]
    assert view["gene_symbols"] == ["ermM"] and view["reference_taxonomy"]["taxon_id"] == "NCBITaxon:1282"
    assert result["ermc_reference_citation"]["own_definition_citation"] is False
    assert sum(c["selected_primary_context"] is not None for c in result["claim_dispositions"]) == 24
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["biological_records_changed"] == result["limits"]["ncbi_requests"] == 0


def test_currently_empty_terms_retain_older_candidates_and_query_limits():
    result = public_result()
    terms = result["terms"]
    assert terms["ARO:3000605"]["prior_candidates_not_in_selected_index"] == ["UniProtKB:Q8VQ13"]
    assert terms["ARO:3004652"]["prior_candidates_not_in_selected_index"] == ["UniProtKB:Q54386"]
    for term in ("ARO:3007654", "ARO:3009647"):
        assert terms[term]["native_name_relations"] == {}
        assert terms[term]["earlier_candidate_context"]["published_deposits"]
        assert terms[term]["no_reference_is_biological_absence"] is False
    assert (
        terms["ARO:3000596"]["earlier_candidate_context"]["status"]
        == "MULTIPLE_REFERENCES_NOT_INTERCHANGEABLE"
    )


def test_no_operational_or_numeric_ast_exports():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_read_only_replay_when_native_cache_available(monkeypatch, pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["protein_snapshot"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not set(mode) & set("wax+"), "offline replay attempted write"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == public_result()

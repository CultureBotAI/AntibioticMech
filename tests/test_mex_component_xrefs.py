"""Source component xrefs and conflicting roles cannot establish experimental identities."""

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
from rdflib import OWL, RDF, RDFS, BNode, Graph, Literal, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mex_component_xrefs as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_portable_checkpoint_preserves_record_and_claim_scope(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.mex.read_json(ROOT, result["prior"])
    for key in ("records", "claims", "terms"):
        assert result[key] == prior[key]
    assert len(result["records"]) == 5 and len(result["claims"]) == 8
    assert set(result["components"]) == set(audit.LABELS)
    assert result["summary"]["native_card_entries_replayed"] == 4182
    assert result["summary"]["native_pages_replayed"] == 9
    assert result["summary"]["new_network_requests"] == 0
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["broad_reference_index_updated"] is False
    assert result["limits"]["source_role_correction_established"] is False
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_candidates_preserve_missing_symbols_and_species_mismatches():
    candidates = public_result()["reference_candidates"]
    assert set(candidates) == {
        "UniProtKB:" + a for a in ("Q9HW28", "Q9HW27", "Q9HXW3", "A0A448BTW6", "A0A448BGH9")
    }
    for accession in ("Q9HW28", "Q9HW27", "Q9HXW3"):
        row = candidates["UniProtKB:" + accession]
        assert row["native_gene_symbols"] == []
        assert row["gene_name_comparison"] == "NO_NATIVE_GENE_SYMBOL"
        assert row["reference_taxon_id"] == "NCBITaxon:208964"
        assert row["reference_taxon_rank"] == "strain"
        assert row["reference_species"]["taxonId"] == 287
        assert row["disposition"] == "REFERENCE_SPECIES_COMPATIBLE_NOT_EXPERIMENTAL_IDENTITY"
    for accession, symbol in (("A0A448BTW6", "tolC_3"), ("A0A448BGH9", "mexB_1")):
        row = candidates["UniProtKB:" + accession]
        assert row["native_gene_symbols"] == [symbol]
        assert row["gene_name_comparison"] == "NATIVE_SYMBOL_DIFFERS_FROM_CARD_COMPONENT_LABEL"
        assert row["reference_taxon_id"] == "NCBITaxon:294"
        assert row["reference_taxon_rank"] == "species"
        assert row["reference_taxon_name"] == "Pseudomonas fluorescens"
        assert row["disposition"] == "WITHHELD_FROM_P_AERUGINOSA_CONTEXT_DIFFERENT_REFERENCE_SPECIES"
    for row in candidates.values():
        assert row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        assert row["experimental_subject_assignment"] is row["exact_allele_assignment"] is False
        assert row["whole_complex_identity_assignment"] is row["curation_supported_by_this_pass"] is False


def graph_fixture():
    graph = Graph()
    for tid, label in audit.LABELS.items():
        node = URIRef(audit.BASE + tid[4:])
        graph.add((node, RDF.type, OWL.Class))
        graph.add((node, RDFS.label, Literal(label)))
    target = URIRef(audit.BASE + "3003691")
    prop = URIRef(audit.BASE + "2000002")
    graph.add((target, RDFS.label, Literal("MexJK-OpmH")))
    graph.add((prop, RDFS.label, Literal("inner_membrane_protein_of")))
    restriction = BNode()
    graph.add((URIRef(audit.BASE + "3003692"), RDFS.subClassOf, restriction))
    graph.add((restriction, RDF.type, OWL.Restriction))
    graph.add((restriction, OWL.onProperty, prop))
    graph.add((restriction, OWL.someValuesFrom, target))
    return graph, restriction


@pytest.mark.parametrize(
    "change", ["target", "property", "all_values", "extra_predicate", "label", "deprecated"]
)
def test_ambiguous_or_changed_ontology_restrictions_rejected(change):
    graph, restriction = graph_fixture()
    if change == "target":
        graph.add((restriction, OWL.someValuesFrom, URIRef(audit.BASE + "3003694")))
    elif change == "property":
        graph.add((restriction, OWL.onProperty, URIRef(audit.BASE + "2000004")))
    elif change == "all_values":
        graph.remove((restriction, OWL.someValuesFrom, None))
        graph.add((restriction, OWL.allValuesFrom, URIRef(audit.BASE + "3003691")))
    elif change == "extra_predicate":
        graph.add((restriction, OWL.cardinality, Literal(1)))
    elif change == "label":
        graph.add((URIRef(audit.BASE + "3003692"), RDFS.label, Literal("different")))
    else:
        graph.add((URIRef(audit.BASE + "3003692"), OWL.deprecated, Literal(True)))
    with pytest.raises(ValueError):
        audit.component_graph(graph)


def test_named_superclass_is_not_a_component_relation():
    graph, _ = graph_fixture()
    node, parent = URIRef(audit.BASE + "3003692"), URIRef(audit.BASE + "3000748")
    graph.add((parent, RDFS.label, Literal("efflux family")))
    graph.add((node, RDFS.subClassOf, parent))
    result = audit.component_graph(graph)["ARO:3003692"]
    assert result["named_superclasses"] == [{"iri": str(parent), "label": "efflux family"}]
    assert len(result["component_relations"]) == 1
    assert result["component_relations"][0]["target_aro"] == "ARO:3003691"


def test_contextual_role_conflicts_remain_open_and_unmodified():
    result = public_result()
    components = copy.deepcopy(result["components"])
    conflicts = audit.role_conflicts(components)
    assert components == result["components"]
    assert conflicts == result["role_conflicts"]
    assert [r["component_aro"] for r in conflicts] == ["ARO:3003692", "ARO:3003693"]
    for conflict in conflicts:
        edges = conflict["relations"]
        opmh = [r["property_iri"] for r in edges if r["target_aro"] == "ARO:3003691"]
        other = {r["property_iri"] for r in edges if r["target_aro"] != "ARO:3003691"}
        assert len(opmh) == len(other) == 1 and opmh[0] not in other
        assert conflict["biological_correction_independently_established"] is False
        assert conflict["propagate_a_role_across_contexts"] is False
    outside = [
        r
        for c in components.values()
        for r in c["component_relations"]
        if not r["target_in_selected_record_cohort"]
    ]
    assert len(outside) == 1 and outside[0]["target_aro"] == "ARO:3003678"


def native_fixture():
    payload = {
        "results": [
            {
                "primaryAccession": "Q00001",
                "uniProtKBCrossReferences": [{"database": "CARD", "id": "ARO:3003692"}],
            }
        ]
    }
    body = json.dumps(payload)
    return {
        "url": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(audit.card.PARAMS),
        "status": 200,
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "headers": {"x-uniprot-release": "2026_03", "x-total-results": "1"},
    }


@pytest.mark.parametrize(
    "change",
    [
        "checksum",
        "release",
        "total",
        "redirect",
        "query",
        "status",
        "cursor",
        "sequence",
        "features",
        "missing_card",
        "empty",
        "duplicate",
        "unordered",
    ],
)
def test_native_page_failure_cases(change):
    receipt = native_fixture()
    if change in {"release", "total", "redirect", "cursor"}:
        key = {
            "release": "x-uniprot-release",
            "total": "x-total-results",
            "redirect": "location",
            "cursor": "link",
        }[change]
        receipt["headers"][key] = {
            "release": "2026_04",
            "total": "2",
            "redirect": "https://example.org",
            "cursor": '<https://example.org/page>; rel="next"',
        }[change]
    elif change == "checksum":
        receipt["sha256"] = "0" * 64
    elif change == "query":
        receipt["url"] += "&query=unexpected"
    elif change == "status":
        receipt["status"] = 403
    else:
        payload = json.loads(receipt["body"])
        if change in {"sequence", "features"}:
            payload["results"][0][change] = "unexpected"
        elif change == "missing_card":
            payload["results"][0]["uniProtKBCrossReferences"] = []
        elif change == "empty":
            payload["results"] = []
        else:
            payload["results"].append(copy.deepcopy(payload["results"][0]))
            if change == "unordered":
                payload["results"][1]["primaryAccession"] = "A00001"
        receipt["body"] = json.dumps(payload)
        receipt["sha256"] = hashlib.sha256(receipt["body"].encode()).hexdigest()
    with pytest.raises(ValueError):
        audit.native_page(receipt, audit.card.PARAMS, "2026_03", 1)


def test_no_operational_or_experimental_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(public_result())) & {
        "sequence",
        "features",
        "alteration",
        "variants",
        "gene_id",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
    }


@pytest.mark.parametrize(
    "change", ["taxid", "taxon_name", "inactive", "crossref_id", "crossref_db", "duplicate_property"]
)
def test_candidate_identity_must_agree_with_native_taxonomy_and_crossref(change):
    entry = {
        "primaryAccession": "Q00001",
        "entryType": "unreviewed",
        "entryAudit": {},
        "organism": {"taxonId": 287, "scientificName": "Pseudomonas aeruginosa"},
    }
    taxon = {
        "taxonId": 287,
        "scientificName": "Pseudomonas aeruginosa",
        "rank": "species",
        "active": True,
        "lineage": [],
    }
    xref = {
        "database": "CARD",
        "id": "ARO:3003692",
        "properties": [{"key": "CARD short name", "value": "MexJ"}],
    }
    if change == "taxid":
        taxon["taxonId"] = 294
    elif change == "taxon_name":
        taxon["scientificName"] = "Pseudomonas fluorescens"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "crossref_id":
        xref["id"] = "ARO:3003693"
    elif change == "crossref_db":
        xref["database"] = "other"
    else:
        xref["properties"].append(copy.deepcopy(xref["properties"][0]))
    with pytest.raises(ValueError):
        audit.project_candidate(entry, xref, taxon, "MexJ")


def test_offline_replay_when_native_cache_and_current_checkpoint_available():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if any(not (ROOT / p["path"]).exists() for p in plan["native_protein_pages"]):
        pytest.skip("native cache unavailable; portable checks still run")
    prior = audit.mex.read_json(ROOT, plan["prior"])
    followup = audit.mex.read_json(ROOT, prior["prior_followup"])
    component = audit.mex.read_json(ROOT, followup["prior"])
    update = audit.mex.read_json(ROOT, component["explicit_corpus_update"])
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with audit.reference.check_pin(ROOT, component["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (ROOT / r["path"]).exists()
        or audit.reference.digest(ROOT / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.skip("historical record checkpoint; portable checks still run")
    assert audit.build(ROOT) == public_result()

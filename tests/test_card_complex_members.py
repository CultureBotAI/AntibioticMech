"""Member reference candidates must not become complex or experimental identities."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests
from rdflib import OWL, RDF, RDFS, BNode, Graph, Literal, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_complex_members as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def graph_fixture(prop=audit.PART_OF):
    graph = Graph()
    member, parent = URIRef(audit.BASE + "3000001"), URIRef(audit.BASE + "3000002")
    for node, name in ((member, "member"), (parent, "parent")):
        graph.add((node, RDF.type, OWL.Class))
        graph.add((node, RDFS.label, Literal(name)))
    graph.add((URIRef(prop), RDFS.label, Literal(audit.RELATIONS.get(prop, "excluded"))))
    restriction = BNode()
    for triple in (
        (member, RDFS.subClassOf, restriction),
        (restriction, RDF.type, OWL.Restriction),
        (restriction, OWL.onProperty, URIRef(prop)),
        (restriction, OWL.someValuesFrom, parent),
    ):
        graph.add(triple)
    return graph, restriction, member, parent


@pytest.mark.parametrize("prop", audit.RELATIONS)
def test_only_explicit_direct_membership(prop):
    graph, _, member, parent = graph_fixture(prop)
    graph.add((member, RDFS.subClassOf, parent))
    edges, excluded = audit.source_members(graph, {"ARO:3000002": "parent"})
    assert excluded == {} and len(edges) == 1
    assert edges[0]["property_iri"] == prop
    assert edges[0]["member_aro"] == "ARO:3000001"
    assert edges[0]["biological_composition_independently_verified"] is False


@pytest.mark.parametrize("suffix", ["RO_0002211", "RO_0012006", "RO_0002312", "RO_0001000"])
def test_regulators_inhibitors_variants_and_derivation_excluded(suffix):
    prop = "http://purl.obolibrary.org/obo/" + suffix
    graph, _, _, _ = graph_fixture(prop)
    edges, excluded = audit.source_members(graph, {"ARO:3000002": "parent"})
    assert edges == [] and excluded == {prop: 1}


@pytest.mark.parametrize(
    "change",
    ["target", "property", "literal_property", "extra_type", "extra_predicate", "parent_label", "duplicate"],
)
def test_ambiguous_membership_rejected(change):
    graph, restriction, member, parent = graph_fixture()
    if change == "target":
        graph.add((restriction, OWL.someValuesFrom, URIRef(audit.BASE + "3000003")))
    elif change == "property":
        graph.add((restriction, OWL.onProperty, URIRef(audit.BASE + "2000002")))
    elif change == "literal_property":
        prop = Literal(audit.PART_OF)
        graph.set((restriction, OWL.onProperty, prop))
        graph.add((prop, RDFS.label, Literal("part_of")))
    elif change == "extra_type":
        graph.add((restriction, RDF.type, OWL.Class))
    elif change == "extra_predicate":
        graph.add((restriction, OWL.cardinality, Literal(1)))
    elif change == "parent_label":
        graph.add((parent, RDFS.label, Literal("other")))
    else:
        second = BNode()
        graph.add((member, RDFS.subClassOf, second))
        for predicate, value in list(graph.predicate_objects(restriction)):
            graph.add((second, predicate, value))
    with pytest.raises(ValueError):
        audit.source_members(graph, {"ARO:3000002": "parent"})


@pytest.mark.parametrize("change", ["all_values", "untyped", "other_parent", "named_subclass"])
def test_out_of_scope_relationships_are_not_promoted(change):
    graph, restriction, member, parent = graph_fixture()
    if change == "all_values":
        graph.remove((restriction, OWL.someValuesFrom, parent))
        graph.add((restriction, OWL.allValuesFrom, parent))
    elif change == "untyped":
        graph.remove((restriction, RDF.type, OWL.Restriction))
    elif change == "other_parent":
        graph.set((restriction, OWL.someValuesFrom, URIRef(audit.BASE + "3000003")))
    else:
        graph.remove((member, RDFS.subClassOf, restriction))
        graph.add((member, RDFS.subClassOf, parent))
    assert audit.source_members(graph, {"ARO:3000002": "parent"}) == ([], {})


def reference_fixture():
    taxon = {
        "taxonId": 123,
        "scientificName": "reference organism",
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 1, "scientificName": "root"},
        "lineage": [],
    }
    entry = {
        "primaryAccession": "Q00001",
        "entryType": "unreviewed",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "organism": {"taxonId": 123, "scientificName": "reference organism"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "reference protein"}}},
        "references": [],
    }
    return entry, taxon


def test_missing_symbols_are_not_inferred_and_inputs_unchanged():
    entry, taxon = reference_fixture()
    before = copy.deepcopy((entry, taxon))
    result = audit.member_reference(entry, taxon)
    assert (entry, taxon) == before
    assert result["gene_field_present"] is False and result["gene_symbols"] == []
    assert result["ordered_locus_names"] == result["orf_names"] == []
    assert result["experimental_subject_assignment"] is result["whole_complex_identity_assignment"] is False
    assert result["native_entry_sha256"] == audit.screen.checksum(entry)


def test_name_disagreement_is_retained_but_default_projector_remains_strict():
    entry, taxon = reference_fixture()
    taxon["scientificName"] += " (type O:8)"
    with pytest.raises(ValueError, match="native identity"):
        audit.screen.project_reference(entry, taxon)
    result = audit.member_reference(entry, taxon)
    assert result["native_protein_taxonomy"]["scientificName"] == entry["organism"]["scientificName"]
    assert result["reference_taxonomy"]["scientific_name"] == taxon["scientificName"]
    assert result["taxonomy_name_comparison"].startswith("SHARED_NATIVE_TAXID_DIFFERENT_LABELS")
    assert result["native_entry_sha256"] == audit.screen.checksum(entry)


@pytest.mark.parametrize("change", ["taxid", "inactive", "version", "sequence", "features"])
def test_name_disagreement_opt_in_does_not_relax_other_guards(change):
    entry, taxon = reference_fixture()
    if change == "taxid":
        taxon["taxonId"] += 1
    elif change == "inactive":
        taxon["active"] = False
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    else:
        entry[change] = "unexpected"
    with pytest.raises(ValueError):
        audit.member_reference(entry, taxon)


def test_metagenome_rank_is_not_a_biological_species_or_experimental_subject():
    entry, taxon = reference_fixture()
    entry["organism"]["scientificName"] = taxon["scientificName"] = "bioreactor metagenome"
    result = audit.member_reference(entry, taxon)
    assert result["reference_taxonomy"]["native_rank"] == "species"
    assert "METAGENOME_LABEL_NOT_INDIVIDUAL_ORGANISM" in result["reference_taxonomy"]["label_flags"]
    assert result["reference_taxonomy"]["native_species_rank_establishes_individual_organism"] is False


def test_mixed_reference_backgrounds_are_not_a_single_complex_identity():
    term = {
        "label": "parent",
        "source_label_sha256": "x",
        "record_memberships": [],
        "reference_status": "none",
    }
    proteins = {
        key: {"reference_taxonomy": {"taxon_id": f"NCBITaxon:{i}", "species": {"taxonId": i}}}
        for i, key in enumerate(("UniProtKB:A", "UniProtKB:B"), 1)
    }
    edges = [{"reference_candidates": list(proteins)}, {"reference_candidates": []}]
    result = audit.parent_projection(term, edges, proteins)
    assert result["multiple_reference_taxa_not_one_experimental_background"] is True
    assert result["all_member_terms_have_native_xref_candidates"] is False
    assert result["complete_biological_membership_established"] is False
    assert result["parent_protein_accession_assignment"] is result["experimental_taxon_assignment"] is None


def test_portable_checkpoint_covers_all_terms_and_preserves_claim_scope(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    plan = audit.prior.mex.read_json(ROOT, result["plan"])
    index = audit.prior.mex.read_json(ROOT, result["inputs"]["index"])
    assert result["scope"] == audit.SCOPE and len(result["coverage"]) == len(index["terms"]) == 2002
    assert set(result["coverage"]) == set(index["terms"])
    assert len(result["parents"]) == len(plan["parent_terms"]) == 63
    assert len(result["reference_proteins"]) == 155 and len(result["taxonomy_sources"]) == 47
    assert len(result["claims"]) == 199 and len(result["records"]) == 57
    expected = [c for c in index["claims"] if c["aro_id"] in result["parents"]]
    update = audit.prior.mex.read_json(ROOT, result["inputs"]["corpus_update"])
    deltas = {d["identifier"]: d for d in update["record_deltas"]}
    for claim in expected:
        if claim["record_identifier"] in deltas:
            delta = deltas[claim["record_identifier"]]
            assert claim["record_sha256"] == delta["before_sha256"]
            claim["record_sha256"] = delta["after_sha256"]
    assert result["claims"] == expected
    assert result["summary"]["native_protein_entries_replayed"] == 4182
    assert result["summary"]["native_protein_pages_replayed"] == 9
    assert result["summary"]["direct_member_edges"] == 225
    assert result["summary"]["member_terms"] == 193
    assert result["summary"]["new_network_requests"] == len(result["new_taxonomy_requests"]) == 22
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_saved_membership_candidates_are_owned_by_exact_native_xref():
    result = public_result()
    for parent, row in result["parents"].items():
        assert row["complete_biological_membership_established"] is False
        assert row["parent_protein_accession_assignment"] is row["experimental_taxon_assignment"] is None
        assert row["primary_review"] == "OPEN"
        for edge in row["member_edges"]:
            assert edge["parent_aro"] == parent and edge["property_iri"] in audit.RELATIONS
            assert edge["reference_candidates"] == sorted(
                {b["accession"] for b in edge["native_xref_bindings"]}
            )
            for binding in edge["native_xref_bindings"]:
                xref = binding["native_cross_reference"]
                assert xref["database"] == "CARD" and xref["id"] == edge["member_aro"]
                assert (
                    xref in result["reference_proteins"][binding["accession"]]["native_card_cross_references"]
                )


def test_saved_native_name_conflicts_and_environmental_taxon_remain_visible():
    proteins = public_result()["reference_proteins"]
    disagree = {a for a, p in proteins.items() if p["taxonomy_name_comparison"].startswith("SHARED_")}
    assert disagree == {"UniProtKB:Q56876", "UniProtKB:Q56877"}
    environmental = [
        p for p in proteins.values() if p["reference_taxonomy"]["taxon_id"] == "NCBITaxon:1076179"
    ]
    assert environmental
    for p in environmental:
        assert "METAGENOME_LABEL_NOT_INDIVIDUAL_ORGANISM" in p["reference_taxonomy"]["label_flags"]
    for p in proteins.values():
        assert p["experimental_subject_assignment"] is p["exact_allele_assignment"] is False
        assert p["experimental_genome_assignment"] is None


def test_no_operational_values_exported():
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
        "assembly_accession",
        "biosample_accession",
        "mic_value",
    }


def test_offline_replay_when_native_cache_available(pre_cdsa_qualification_root):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["request_plan"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")
    assert audit.build(pre_cdsa_qualification_root) == public_result()


def test_request_plan_count_cannot_be_changed_without_changing_frozen_plan(tmp_path):
    frozen = {"missing_taxonomy": ["123"]}
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(frozen))
    inspected = tmp_path / "inspected.json"
    inspected.write_text("{}")
    plan = {
        "request_plan": audit.reference.pin(tmp_path, path),
        "taxonomy_canary_inspected": audit.reference.pin(tmp_path, inspected),
        "new_taxonomy_requests": 0,
    }
    with pytest.raises(ValueError, match="request accounting"):
        audit.request_provenance(tmp_path, plan)


def test_public_output_has_stable_checksum():
    assert hashlib.sha256((ROOT / audit.OUTPUT).read_bytes()).hexdigest() == (
        "008d915100f8c36ca43b39b891a97a418e4e9d60dcd807cbfe9e2ed9284779ac"
    )


def request_fixture(root):
    def save(name, value):
        path = root / name
        path.write_text(json.dumps(value))
        return audit.reference.pin(root, path)

    url = "https://rest.uniprot.org/taxonomy/123.json"
    frozen = {
        "missing_taxonomy": ["123"],
        "planned_taxonomy_urls": {"123": url},
        "native_taxonomy": {},
        "ncbi_requests": 0,
        "retries": 0,
        "redirects_followed": 0,
    }
    plan_pin = save("request-plan.json", frozen)
    response = {
        "url": url,
        "status": 200,
        "retries": 0,
        "redirects_followed": 0,
        "body": "{}",
        "bytes": 2,
    }
    item = {"receipt": save("taxonomy-123-receipt.json", response), "body": None}
    inspected = {"accepted": True, "taxon_id": 123, "source": item}
    save("taxonomy-123-attempt.json", {"url": url, "request_plan": plan_pin})
    plan = {
        **frozen,
        "request_plan": plan_pin,
        "taxonomy_canary_inspected": save("inspected.json", inspected),
        "native_taxonomy": {"123": item},
        "new_taxonomy_requests": 1,
        "remaining_missing_taxonomy": [],
    }
    return plan, save


def test_request_receipts_match_frozen_plan(tmp_path):
    plan, _ = request_fixture(tmp_path)
    result = audit.request_provenance(tmp_path, plan)
    assert set(result) == {"123"}
    assert result["123"]["response"] == plan["native_taxonomy"]["123"]


@pytest.mark.parametrize("change", ["url", "status", "redirect", "bytes", "attempt", "failure", "canary"])
def test_request_failures_or_unplanned_access_cannot_be_hidden(tmp_path, change):
    plan, save = request_fixture(tmp_path)
    if change in {"url", "status", "redirect", "bytes"}:
        path = tmp_path / "taxonomy-123-receipt.json"
        receipt = json.loads(path.read_bytes())
        key, value = {
            "url": ("url", "https://example.org/taxonomy/123"),
            "status": ("status", 302),
            "redirect": ("redirects_followed", 1),
            "bytes": ("bytes", 3),
        }[change]
        receipt[key] = value
        plan["native_taxonomy"]["123"]["receipt"] = save(path.name, receipt)
    elif change == "attempt":
        save("taxonomy-456-attempt.json", {})
    elif change == "failure":
        save("taxonomy-123-error.json", {})
    else:
        plan["taxonomy_canary_inspected"] = save(
            "inspected.json",
            {
                "accepted": False,
                "taxon_id": 123,
                "source": plan["native_taxonomy"]["123"],
            },
        )
    with pytest.raises(ValueError):
        audit.request_provenance(tmp_path, plan)

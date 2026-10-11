"""PDB reference context must not become a resistance allele or organism claim."""

import copy
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
from rdflib import OWL, RDF, RDFS, Graph, Literal, URIRef

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_structure_links as audit  # noqa: E402


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())


def test_direct_xref_scan_does_not_inherit_a_parent_link():
    graph = Graph()
    parent, child = [URIRef(audit.ontology.BASE + t) for t in ("3000001", "3000002")]
    for node in (parent, child):
        graph.add((node, RDF.type, OWL.Class))
        graph.add((node, RDFS.label, Literal("fixture")))
    graph.add((child, RDFS.subClassOf, parent))
    graph.add((parent, URIRef(audit.ontology.NS["oboInOwl"] + "hasDbXref"), Literal("PDB:1ABC")))
    ids = ["ARO:3000001", "ARO:3000002"]
    body = graph.serialize(format="xml")
    assert audit.direct_xrefs(body, ids, {t: ["fixture"] for t in ids}) == {
        "ARO:3000001": ["PDB:1ABC"],
        "ARO:3000002": [],
    }
    with pytest.raises(ValueError, match="term identity"):
        audit.direct_xrefs(body, ids, {t: ["wrong"] for t in ids})


def entity(identifier, accessions, taxid):
    return {
        "rcsb_id": identifier,
        "rcsb_polymer_entity_container_identifiers": {"reference_sequence_identifiers": accessions},
        "rcsb_entity_source_organism": [{"ncbi_taxonomy_id": taxid, "scientific_name": "fixture"}],
    }


def test_entity_references_do_not_flatten_organisms_or_select_a_representative():
    entries = [
        entity(
            "1ABC_1", [{"database_name": "UniProt", "database_accession": a} for a in ("P00001", "P00002")], 1
        ),
        entity("1ABC_2", None, 2),
    ]
    result = audit.entity_references({"rcsb_id": "1ABC", "polymer_entities": entries})
    assert result[0]["reference_accessions"] == ["UniProtKB:P00001", "UniProtKB:P00002"]
    assert result[1]["reference_accessions"] == []
    assert [r["source_organisms"][0]["ncbi_taxonomy_id"] for r in result] == [1, 2]


@pytest.mark.parametrize("second", ["1ABC_1", "2DEF_2"])
def test_duplicate_and_foreign_entities_fail_closed(second):
    with pytest.raises(ValueError, match="polymer entity"):
        audit.entity_references(
            {"rcsb_id": "1ABC", "polymer_entities": [entity("1ABC_1", None, 1), entity(second, None, 2)]}
        )


@pytest.mark.parametrize(
    "field,value",
    [
        ("status", 403),
        ("sha256", "invalid"),
        ("url", "https://www.ncbi.nlm.nih.gov/not-requested"),
        ("url", "http://rest.uniprot.org/uniprotkb/search"),
        ("url", "https://user:password@rest.uniprot.org/uniprotkb/search"),
    ],
)
def test_bad_cached_receipts_are_rejected_without_network(tmp_path, field, value):
    raw = {
        "status": 200,
        "url": "https://rest.uniprot.org/uniprotkb/search",
        "body": "{}",
        "sha256": hashlib.sha256(b"{}").hexdigest(),
        "retrieved_at": "fixture",
    }
    raw[field] = value
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(raw))
    with pytest.raises(ValueError, match="cache identity or checksum"):
        audit.receipt(tmp_path, path, "rest.uniprot.org")


def test_public_metadata_projection_does_not_copy_sequences_or_positions():
    entry = {
        "primaryAccession": "P00001",
        "entryType": "fixture",
        "entryAudit": {},
        "organism": {"taxonId": 1, "scientificName": "fixture"},
        "genes": [{"geneName": {"value": "gene"}}],
        "sequence": "not-exported",
        "features": ["not-exported"],
        "uniProtKBCrossReferences": [
            {"database": "PDB", "id": "1ABC", "properties": [{"key": "Chains", "value": "not-exported"}]}
        ],
    }
    result = audit.reference_metadata(entry)
    assert "not-exported" not in json.dumps(result)
    assert result["pdb_cross_reference_ids"] == ["1ABC"]
    assert result["gene_symbols"] == ["gene"]


def test_snapshot_coverage_and_noncuration_are_explicit(dossier):
    assert dossier["coverage"] == {
        "unlinked_terms_scanned": 1024,
        "terms_without_direct_xrefs": 1018,
        "direct_xref_namespace_counts": {"PDB": 6},
        "scan_scope": "DIRECT_HAS_DB_XREF_ON_UNLINKED_NAMED_CLASSES_ONLY_NO_ANCESTOR_INHERITANCE",
    }
    assert dossier["summary"] == {
        "corpus_records_verified": 2939,
        "selected_terms": 6,
        "record_memberships": 20,
        "selected_records_loaded": 17,
        "reference_proteins": 6,
        "biological_record_changes": 0,
        "curation_events_added": 0,
        "whole_records_completed": 0,
        "full_corpus_primary_review": "OPEN",
        "ignored_files_included": True,
    }
    assert dossier["scope"] == audit.SCOPE
    assert dossier["uniprot_release"] == "2026_03"


@pytest.mark.parametrize(
    "term,pdb_id,accession",
    [
        ("ARO:3000309", "2GFP", "P31442"),
        ("ARO:3000866", "2IYA", "Q3HTL7"),
        ("ARO:3001307", "2Z2P", "P17978"),
        ("ARO:3002547", "1V0C", "Q6SJ71"),
        ("ARO:3002637", "3N4T", "O68183"),
        ("ARO:3004042", "2F1M", "P0AE06"),
    ],
)
def test_reciprocal_paths_are_reference_only(dossier, term, pdb_id, accession):
    link = dossier["links"][term]
    assert link["source_xrefs"] == ["PDB:" + pdb_id]
    assert link["experimental_assignment"] is False and link["primary_review_status"] == "PENDING"
    (structure,) = link["structures"]
    (entity_row,) = [r for r in structure["entities"] if r["reference_accessions"]]
    assert entity_row["reference_accessions"] == ["UniProtKB:" + accession]
    assert pdb_id in dossier["proteins"]["UniProtKB:" + accession]["pdb_cross_reference_ids"]
    assert structure["pdb_id"] == pdb_id
    url = urlsplit(structure["request"]["url"])
    assert url.netloc == "data.rcsb.org" and url.path == "/graphql"
    assert parse_qs(url.query) == {"query": [audit.pdb_query(pdb_id)]}


def test_species_mismatch_is_rejected_not_silently_curated(dossier):
    link = dossier["links"]["ARO:3004042"]
    assert link["source_label"] == "Enterobacter cloacae acrA"
    assert link["context_review"]["decision"] == "REJECT_FOCAL_ORGANISM_ASSIGNMENT"
    protein = dossier["proteins"]["UniProtKB:P0AE06"]
    assert protein["reference_taxon_id"] == "NCBITaxon:83333"
    assert protein["card_cross_reference_ids"] == ["ARO:3004043"]
    assert dossier["taxonomy"]["83333"]["parent"]["taxonId"] == 562
    assert dossier["taxonomy"]["83333"]["rank"] == "strain"


def test_second_polymer_entity_taxon_is_not_attached_to_the_enzyme(dossier):
    link = dossier["links"]["ARO:3001307"]
    first, second = link["structures"][0]["entities"]
    assert first["entity_id"] == "2Z2P_1" and first["reference_accessions"] == ["UniProtKB:P17978"]
    assert first["source_organisms"][0]["ncbi_taxonomy_id"] == 1280
    assert second["entity_id"] == "2Z2P_2" and second["reference_accessions"] == []
    assert second["source_organisms"][0]["ncbi_taxonomy_id"] == 68212
    assert dossier["taxonomy"]["68212"]["scientificName"] == "Streptomyces graminofaciens"
    assert link["context_review"]["decision"] == "INACTIVE_STRUCTURAL_REFERENCE_NOT_RESISTANCE_SUBJECT"


def test_structure_and_gene_naming_do_not_resolve_the_allele(dossier):
    assert (
        dossier["links"]["ARO:3002547"]["context_review"]["decision"]
        == "EXACT_ALLELE_NOT_RESOLVED_BY_STRUCTURE"
    )
    assert dossier["links"]["ARO:3002637"]["context_review"]["decision"] == "NOMENCLATURE_REVIEW_REQUIRED"
    assert dossier["proteins"]["UniProtKB:O68183"]["gene_symbols"] == ["aph(2'')-Id"]
    assert "PMID:16675700" not in dossier["proteins"]["UniProtKB:P31442"]["citation_ids"]
    assert (
        dossier["links"]["ARO:3000309"]["structures"][0]["primary_citation"]["pdbx_database_id_PubMed"]
        == 16675700
    )


def test_input_pins_and_current_record_identities(dossier):
    for pin in dossier["inputs"].values():
        assert audit.sha(ROOT / pin["path"]) == pin["sha256"]
    expected = Counter()
    for row in dossier["records"]:
        record = load_record(ROOT / row["path"])
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        claims = [c for c in record["resistance_mechanisms"] if c.get("aro_id") in dossier["links"]]
        assert sorted(c["aro_id"] for c in claims) == row["aro_ids"]
        assert all(audit.is_card_sourced(c) for c in claims)
        expected.update(row["aro_ids"])
    assert expected == {
        "ARO:3000309": 1,
        "ARO:3000866": 1,
        "ARO:3001307": 9,
        "ARO:3002547": 4,
        "ARO:3002637": 4,
        "ARO:3004042": 1,
    }


def test_public_export_is_bounded_and_network_receipts_are_scoped(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence",
        "features",
        "variants",
        "alteration",
        "resistance_mechanisms",
        "activity_spectrum",
        "mic",
        "measurement_value",
        "protocol",
        "primers",
        "coordinates",
        "Chains",
    }
    assert len(dossier["uniprot_requests"]) == 12
    assert all(urlsplit(r["url"]).netloc == "rest.uniprot.org" for r in dossier["uniprot_requests"])
    assert len(dossier["taxonomy"]) == 6 and all(r["active"] for r in dossier["taxonomy"].values())
    assert "No NCBI request" in " ".join(dossier["limitations"])


def test_cached_export_reproduces_when_research_cache_is_available(dossier):
    cache_dir = ROOT / "reports/resistance-grounding-2026-10-09-card-structures"
    if not (cache_dir / "pdb-2GFP.json").exists():
        pytest.skip("optional ignored research cache is not present; public invariants still run")
    with (ROOT / audit.INPUTS["census"]).open() as handle:
        census = list(csv.DictReader(handle, delimiter="\t"))
    if any(not (ROOT / r["path"]).is_file() or audit.sha(ROOT / r["path"]) != r["record_sha256"]
           for r in census):
        pytest.skip("historical checkpoint no longer matches the live corpus; public invariants still run")
    before = copy.deepcopy(dossier)
    assert audit.analyze(ROOT, cache_dir) == before

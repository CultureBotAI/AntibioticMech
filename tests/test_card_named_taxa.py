"""Name grounding must not promote ontology ancestry to experimental identity."""

import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_named_taxa as audit  # noqa: E402


def response(entries, name="Example species"):
    body = json.dumps({"results": entries})
    return {
        "url": "https://rest.uniprot.org/taxonomy/search?" + urlencode(audit.parameters(name)),
        "body": body, "sha256": hashlib.sha256(body.encode()).hexdigest(), "status": 200,
        "retrieved_at": "fixture", "headers": {
            "X-Total-Results": str(len(entries)), "X-UniProt-Release": "fixture",
        },
    }


def entry(**updates):
    return {"taxonId": 123, "scientificName": "Example species", "rank": "species",
            "active": True, **updates}


@pytest.mark.parametrize("changes,field", [({}, "scientificName"),
    ({"scientificName": "Renamed species", "synonyms": ["Example species"]}, "synonyms")])
def test_only_exact_scientific_name_or_explicit_synonym_resolves(changes, field):
    result = audit.resolve_name("Example species", response([entry(**changes)]))
    assert result["status"] == "EXACT_SPECIES_NAME_RESOLVED"
    assert result["named_organism_taxon_id"] == "NCBITaxon:123"
    assert result["candidates"][0]["exact_name_fields"] == [field]
    assert "strain" not in result and "protein_accession" not in result


@pytest.mark.parametrize("changes", [
    {"active": False}, {"rank": "strain"}, {"rank": "genus"},
    {"scientificName": "Example species isolate"},
    {"scientificName": "example species"},
    {"scientificName": "Different species", "otherNames": ["Example species"]},
    {"scientificName": "Different species", "lineage": [entry()]},
    {"scientificName": "Different species", "synonyms": ["Example species complex"]},
])
def test_nonmatching_context_is_not_a_taxon_assignment(changes):
    result = audit.resolve_name("Example species", response([entry(**changes)]))
    assert result["status"] == "NO_EXACT_ACTIVE_SPECIES_NAME"
    assert result["named_organism_taxon_id"] is None


def test_ambiguous_species_keeps_all_candidates_and_assigns_none():
    entries = [entry(taxonId=456, scientificName="Renamed species", synonyms=["Example species"]), entry()]
    result = audit.resolve_name("Example species", response(entries))
    assert result["status"] == "AMBIGUOUS_EXACT_SPECIES_NAMES"
    assert result["named_organism_taxon_id"] is None
    assert [c["taxon_id"] for c in result["candidates"]] == ["NCBITaxon:123", "NCBITaxon:456"]


def test_empty_search_is_unresolved_not_absence_of_organism():
    result = audit.resolve_name("Example species", response([]))
    assert result["status"] == "NO_EXACT_ACTIVE_SPECIES_NAME"
    assert result["named_organism_taxon_id"] is None


@pytest.mark.parametrize("change", [
    {"url": "https://example.org/taxonomy/search"},
    {"url": "https://rest.uniprot.org/taxonomy/123"},
    {"url": "https://rest.uniprot.org/taxonomy/search?" + urlencode(audit.parameters("Wrong species"))},
    {"status": 302}, {"status": 404}, {"sha256": "0" * 64},
    {"headers": {"X-Total-Results": "2", "X-UniProt-Release": "fixture"}},
    {"headers": {"X-Total-Results": "1", "X-UniProt-Release": "fixture", "Link": "next"}},
    {"headers": {"X-Total-Results": "1"}},
])
def test_wrong_response_or_incomplete_search_is_rejected(change):
    raw = response([entry()])
    raw.update(change)
    with pytest.raises(ValueError):
        audit.resolve_name("Example species", raw)


@pytest.mark.parametrize("taxid", [0, -1, "123", True])
def test_invalid_taxonomy_identifiers_fail(taxid):
    with pytest.raises(ValueError, match="invalid or duplicate"):
        audit.resolve_name("Example species", response([entry(taxonId=taxid)]))


def test_duplicate_taxon_search_rows_fail():
    with pytest.raises(ValueError, match="duplicate"):
        audit.resolve_name("Example species", response([entry(), entry()]))


@pytest.mark.parametrize("changes", [
    {"scientificName": ["Example species"]}, {"scientificName": ""},
    {"synonyms": "Example species"}, {"otherNames": [123]}, {"active": 1}, {"rank": None},
])
def test_malformed_taxonomy_name_fields_fail(changes):
    with pytest.raises(ValueError, match="name or status"):
        audit.resolve_name("Example species", response([entry(**changes)]))


def test_source_name_review_keeps_missing_and_broad_names_separate():
    assert audit.source_name("ARO:3004057",
        "23S rRNA with mutation conferring resistance to linezolid antibiotics")[0] is None
    assert audit.source_name("ARO:3004161",
        "Propionibacteria 23S rRNA with mutation conferring resistance to macrolide antibiotics")[0] == (
            "Propionibacteria")
    assert audit.source_name("ARO:3003402",
        "Escherichia coli 16S rRNA (rrsB) mutation conferring resistance to neomycin")[0] == (
            "Escherichia coli")
    assert audit.source_name("ARO:3005083",
        "Thermus thermophilus 23s rRNA conferring resistance to pleuromutilin antibiotics")[0] == (
            "Thermus thermophilus")


@pytest.mark.parametrize("tid,label", [
    ("ARO:3004956", "Neisseria gonorrhoeae renamed"),
    ("ARO:3004057", "New organism-free label"),
    ("ARO:3004161", "Different broad label"),
    ("ARO:3003402", "Unrecognized source syntax"),
])
def test_source_label_drift_fails(tid, label):
    with pytest.raises(ValueError):
        audit.source_name(tid, label)


def test_rpld_is_flagged_not_assigned_rna_identity():
    name, status = audit.source_name(audit.CONFLICT_ID, "Neisseria gonorrhoeae rpld")
    assert name == "Neisseria gonorrhoeae"
    assert status == "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY"
    body = ('<rdf:RDF xmlns:rdf="' + audit.scope.NS["rdf"] + '" xmlns:obo="http://purl.obolibrary.org/obo/">'
            '<rdf:Description rdf:about="' + audit.scope.BASE + '3004956">'
            '<obo:IAO_0000115>' + audit.CONFLICT_DEFINITION + '</obo:IAO_0000115>'
            '</rdf:Description></rdf:RDF>')
    assert audit.check_definition(body) == hashlib.sha256(audit.CONFLICT_DEFINITION.encode()).hexdigest()
    with pytest.raises(ValueError, match="definition changed"):
        audit.check_definition(body.replace("50S L4", "different"))


@pytest.mark.parametrize("name", ["Propionibacteria", "", 'Example species" OR *', "Example sp."])
def test_unreviewed_query_name_is_rejected(name):
    with pytest.raises(ValueError):
        audit.parameters(name)


def test_output_cannot_overwrite_prior_findings(tmp_path):
    path = tmp_path / "audit.json"
    audit.write_once(path, {"scope": "fixture"})
    before = path.read_bytes()
    audit.write_once(path, {"scope": "fixture"})
    assert path.read_bytes() == before
    with pytest.raises(ValueError, match="already exists"):
        audit.write_once(path, {"scope": "different"})
    assert path.read_bytes() == before


def test_export_retains_every_selected_term_without_promoting_identity():
    result = json.loads((ROOT / "research/2026-10-09-card-named-taxa.json").read_bytes())
    prior = json.loads((ROOT / result["source_term_scope"]["path"]).read_bytes())
    references = json.loads((ROOT / prior["reference_audit"]["path"]).read_bytes())
    expected = {t for t, row in prior["terms"].items() if row["entity_scope"] == audit.COHORT}
    assert set(result["terms"]) == expected
    assert result["scope"] == audit.SCOPE
    assert result["selection"] == "ALL_RNA_ANCESTOR_TERMS"
    assert len(expected) == 88
    assert set(result["source_conflicts"]) == {audit.CONFLICT_ID}
    assert result["summary"]["entity_review_counts"] == {
        "RNA_LABEL_NOT_PRIMARY_VALIDATION": 87,
        "PROTEIN_DEFINITION_CONFLICTS_WITH_RNA_ANCESTRY": 1,
    }
    assert sum(row["assertion_count"] for row in result["terms"].values()) == 107
    for tid, row in result["terms"].items():
        label = references["determinants"][tid]["labels"][0]
        assert row["source_label_sha256"] == hashlib.sha256(label.encode()).hexdigest()
        assert row["primary_review_status"] == "PENDING"
        assert (row["source_organism_label"], row["entity_review"]) == audit.source_name(tid, label)
        assert row["rna_ancestor_path"] == prior["terms"][tid]["anchor_paths"]["ARO:3000328"]
        assert not {"strain", "protein_accession", "gene_id", "alteration", "taxon_id", "assembly"} & set(row)
        if row["named_organism_taxon_id"]:
            assert row["name_resolution"] == "EXACT_SPECIES_NAME_RESOLVED"
            assert row["named_organism_taxon_id"] == result["names"][row["source_organism_label"]][
                "named_organism_taxon_id"]
    for pin in (result["source_term_scope"], result["source_inventory"]):
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    counts = Counter(row["name_resolution"] for row in result["terms"].values())
    assert result["summary"]["name_resolution_counts"] == counts


def test_export_name_decisions_reconstruct_from_public_candidate_metadata():
    result = json.loads((ROOT / "research/2026-10-09-card-named-taxa.json").read_bytes())
    for name, review in result["names"].items():
        entries = []
        for row in review["candidates"]:
            fields = row["exact_name_fields"]
            entries.append(entry(taxonId=int(row["taxon_id"].split(":")[1]),
                scientificName=row["scientific_name"], rank=row["rank"], active=row["active"],
                synonyms=[name] if "synonyms" in fields else [],
                otherNames=[name] if row["other_name_match_only"] else []))
        raw = response(entries, name)
        reconstructed = audit.resolve_name(name, raw)
        assert reconstructed["status"] == review["status"]
        assert reconstructed["named_organism_taxon_id"] == review["named_organism_taxon_id"]
        assert reconstructed["candidates"] == copy.deepcopy(review["candidates"])

"""Keep a documented consensus distinct from a named isolate and patient allele."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_hivdb_reference_identity as audit  # noqa: E402


def metadata():
    name = "Human immunodeficiency virus type 1 group M subtype B (isolate HXB2)"
    species = {"taxonId": 3418650, "scientificName": "Lentivirus humimdef1", "rank": "species"}
    broader = {"taxonId": 11676, "scientificName": "Human immunodeficiency virus type 1", "rank": "no rank"}
    parent = {**broader, "active": True, "parent": {k: species[k] for k in ("taxonId", "scientificName")}}
    taxon = {
        "taxonId": 11706,
        "scientificName": name,
        "rank": "no rank",
        "active": True,
        "lineage": [species, broader],
    }
    entry = {
        "primaryAccession": "P04585",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 268, "sequenceVersion": 4},
        "genes": [{"geneName": {"value": "gag-pol"}}],
        "organism": {"taxonId": 11706, "scientificName": name},
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Gag-Pol polyprotein"}},
            "contains": [
                {"recommendedName": {"fullName": {"value": value}}} for value in audit.PRODUCTS.values()
            ],
        },
    }
    return entry, taxon, parent


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "unreviewed",
        "sequence",
        "features",
        "comments",
        "gene",
        "duplicate_gene",
        "protein_taxon",
        "reference_name",
        "taxon_name",
        "taxon_rank",
        "inactive",
        "broader_rank",
        "broader_inactive",
        "missing_lineage",
        "duplicate_lineage",
        "species_id",
        "species_label",
        "parent_link",
        "boolean_version",
        "zero_version",
        "polyprotein_name",
        "missing_product",
        "duplicate_product",
    ],
)
def test_reference_context_boundaries(change):
    entry, taxon, parent = metadata()
    if change == "accession":
        entry["primaryAccession"] = "P04591"
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "NOT_ALLOWED"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "gag"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "protein_taxon":
        entry["organism"]["taxonId"] = 11676
    elif change == "reference_name":
        entry["organism"]["scientificName"] = "OTHER"
    elif change == "taxon_name":
        taxon["scientificName"] = "OTHER"
    elif change == "taxon_rank":
        taxon["rank"] = "strain"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "broader_rank":
        parent["rank"] = "species"
    elif change == "broader_inactive":
        parent["active"] = False
    elif change == "missing_lineage":
        taxon["lineage"].pop()
    elif change == "duplicate_lineage":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][-1]))
    elif change == "species_id":
        taxon["lineage"][0]["taxonId"] = 999
    elif change == "species_label":
        taxon["lineage"][0]["scientificName"] = "OTHER"
    elif change == "parent_link":
        parent["parent"]["taxonId"] = 999
    elif change == "boolean_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "zero_version":
        entry["entryAudit"]["entryVersion"] = 0
    elif change == "polyprotein_name":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "OTHER"
    elif change == "missing_product":
        entry["proteinDescription"]["contains"].pop()
    elif change == "duplicate_product":
        entry["proteinDescription"]["contains"].append(
            copy.deepcopy(entry["proteinDescription"]["contains"][0])
        )
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_reference(entry, taxon, parent)
        return
    output = audit.project_reference(entry, taxon, parent)
    assert output["protein_accession"] == "UniProtKB:P04585"
    assert output["reference_taxon_id"] != output["source_context_taxon_id"] != output["species_taxon_id"]
    assert output["reference_taxon_rank"] == output["source_context_taxon_rank"] == "no rank"
    assert output["algorithm_reference_assignment"] is False
    assert output["resistance_phenotype_asserted"] is False
    assert output["region_coordinates_inferred"] is False
    assert output["experimental_allele_assignment"] is None
    assert output["experimental_genome_assignment"] is None


def test_unreviewed_faq_bytes_cannot_inherit_a_conclusion():
    with pytest.raises(ValueError, match="FAQ content changed"):
        audit.faq_context(b"consensus B HXB2 - not the inspected document")


@pytest.mark.parametrize("change", ["none", "extra", "missing", "symbol", "name", "strain", "empty"])
def test_only_adopted_reference_regions_are_projected(change):
    genes = {
        key: {
            "abstractGene": key,
            "name": "HIV1" + key,
            "strain": "HIV1",
            "refSequence": "SYNTHETIC_TEST_SENTINEL",
        }
        for key in audit.PRODUCTS
    }
    if change == "extra":
        genes["OTHER"] = {"name": "NOT_EXPORTED", "refSequence": "NOT_EXPORTED"}
    elif change == "missing":
        genes.pop("PR")
    elif change == "symbol":
        genes["PR"]["abstractGene"] = "OTHER"
    elif change == "name":
        genes["PR"]["name"] = "OTHER"
    elif change == "strain":
        genes["PR"]["strain"] = "OTHER"
    elif change == "empty":
        genes["PR"]["refSequence"] = ""
    if change not in {"none", "extra"}:
        with pytest.raises(ValueError):
            audit.source_regions(genes)
        return
    result = audit.source_regions(genes)
    assert set(result) == set(audit.PRODUCTS)
    assert "NOT_EXPORTED" not in json.dumps(result)
    assert "SYNTHETIC_TEST_SENTINEL" not in json.dumps(result)


def test_saved_cohort_preserves_all_source_rules_and_open_subjects():
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    prior = json.loads((ROOT / saved["inputs"]["prior_context"]["path"]).read_bytes())
    old = {r["identifier"]: r for r in prior["records"]}
    assert saved["scope"] == audit.SCOPE
    assert len(saved["records"]) == 16
    assert saved["summary"]["source_rules"] == 467
    assert saved["summary"]["region_rule_counts"] == {"PR": 44, "RT": 231, "IN": 192}
    assert saved["current_documentation"]["every_region_proven_sequence_different"] is False
    assert saved["current_documentation"]["pinned_algorithm_sequence_equivalence_verified"] is False
    assert saved["current_documentation"]["exact_consensus_uniprot_accession"] is None
    for row in saved["records"]:
        assert row["source_rule_ids"] == old[row["identifier"]]["source_rule_ids"]
        assert row["region_rule_counts"] == old[row["identifier"]]["region_rule_counts"]
        for key in (
            "exact_algorithm_accession",
            "experimental_allele_assignment",
            "experimental_genome_assignment",
            "new_taxon_assignment",
        ):
            assert row[key] is None
        assert "NOT_HIVDB_CONSENSUS_OR_PATIENT_ALLELE" in row["comparative_reference_role"]
    assert saved["summary"]["biological_records_changed"] == 0
    assert saved["summary"]["whole_record_reviews_completed"] == 0


@pytest.mark.skipif(not (ROOT / audit.CACHE).exists(), reason="native reference cache is local-only")
def test_native_source_projection_is_offline_and_reproducible(monkeypatch):
    def deny(*args, **kwargs):
        raise AssertionError("native replay must not use network")

    monkeypatch.setattr(socket, "socket", deny)
    import requests

    monkeypatch.setattr(requests.sessions.Session, "request", deny)
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    sources = saved["sources"]
    faq = audit.reference.check_pin(ROOT, sources["faq-content"]["body"]).read_bytes()
    assert audit.faq_context(faq) == saved["current_documentation"]
    protein = json.loads(audit.reference.check_pin(ROOT, sources["protein"]["body"]).read_bytes())
    taxonomy = json.loads(audit.reference.check_pin(ROOT, sources["taxonomy"]["body"]).read_bytes())
    wrapper = json.loads(
        audit.reference.check_pin(ROOT, saved["inputs"]["cached_parent_taxonomy"]).read_bytes()
    )
    assert (
        audit.project_reference(protein["results"][0], taxonomy, json.loads(wrapper["body"]))
        == saved["comparative_reference"]
    )

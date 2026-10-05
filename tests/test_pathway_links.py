import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from antibioticmech.pathway_links import check_links, load_index
from antibioticmech.validation.write_validated import validate_antibiotic
from scripts.curate_pathway_links import apply_plan

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from seed_from_sources import merge_with_existing  # noqa: E402


def test_reviewed_links_resolve_and_survive_reseeding(repo_root):
    commit, index = load_index(repo_root)
    plans = yaml.safe_load((repo_root / "curation/pathway_links.yaml").read_text())["records"]
    records = {d["identifier"]: (p, d) for p in (repo_root / "data/antibiotics").rglob("*.yaml")
               if (d := yaml.safe_load(p.read_text()))["identifier"]
               in {plan["identifier"] for plan in plans}}
    for plan in plans:
        path, record = records[plan["identifier"]]
        updated = apply_plan(record, plan, commit, index)
        assert not check_links(updated, commit, index)
        assert not validate_antibiotic(updated, record_path=path)
        assert apply_plan(updated, plan, commit, index) == updated
        seeded = deepcopy(updated)
        seeded.pop("related_records")
        assert merge_with_existing(seeded, updated)["related_records"] == updated["related_records"]
        page = repo_root / "pages" / path.parent.name / (path.stem + ".html")
        assert "Related pathway records" in page.read_text()
        assert updated["related_records"][0]["identifier"] in page.read_text()
    _, fosfo = records["CHEBI:28915"]
    curated = [t for t in fosfo["molecular_targets"] if t["source"] == "PRIMARY_LITERATURE"]
    assert curated[0]["protein_examples"][0]["uniprot_id"] == "UniProtKB:P0A749"
    assert curated[0]["protein_examples"][0]["taxon_id"] == "NCBITaxon:83333"


@pytest.mark.parametrize("field,value", [("identifier", "MetaCyc:missing"),
                                        ("source_version", "bad-pin"),
                                        ("relation", "SAME_AS"), ("basis", " ")])
def test_invalid_link_is_rejected(repo_root, field, value):
    commit, index = load_index(repo_root)
    link = {"corpus": "PathwayMech", "identifier": "WikiPathways:WP5060",
            "source_version": commit, "relation": "TARGETS_PATHWAY_COMPONENT",
            "basis": "PMID:8994972 supports E. coli MurA"}
    link[field] = value
    assert check_links({"related_records": [link]}, commit, index)


def test_example_cannot_mutate_a_source_owned_target(repo_root):
    commit, index = load_index(repo_root)
    plan = next(row for row in yaml.safe_load(
        (repo_root / "curation/pathway_links.yaml").read_text())["records"]
                if row["identifier"] == "CHEBI:28915")
    record = {"molecular_targets": [{"source": "BINDINGDB", "evidence": [
        {"reference": "PMID:8994972"}]}]}
    with pytest.raises(ValueError, match="curator-owned"):
        apply_plan(record, plan, commit, index)

"""Keep source ambiguity and reference identity separate from tested resistance."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-card-fungal-reference-grounding.json").read_text())


def test_selected_source_assertions_are_retained(dossier):
    assert set(dossier["terms"]) == {"ARO:3009269", "ARO:3009270", "ARO:3009638"}
    for record in dossier["records"]:
        doc = load_record(ROOT / record["path"])
        assert doc["identifier"] == record["identifier"]
        assert doc["chemical_structure"]["standard_inchi_key"] == record["standard_inchi_key"]
        for tid, term in dossier["terms"].items():
            if term["record_id"] != record["identifier"]:
                continue
            claim, = [c for c in doc["resistance_mechanisms"] if c.get("aro_id") == tid]
            assert claim["label"] == term["source_label"]
            assert term["source_assertion_retained"] is True
            assert term["exact_protein_assignment"] is None
            assert "protein_accession" not in claim and "strain_taxon_id" not in claim


def test_ancestry_flag_does_not_erase_explicit_resistance_edge(dossier):
    for key in ("source_term_scope", "source_inventory"):
        pin = dossier[key]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    with (ROOT / dossier["source_inventory"]["path"]).open() as handle:
        inventory = list(csv.DictReader(handle, delimiter="\t"))
    for tid, term in dossier["terms"].items():
        assert term["determinant_ancestor_path"] is None
        assert term["source_relation"] == "confers_resistance_to_antibiotic"
        row, = [r for r in inventory if r["determinant_id"] == tid]
        assert row["relation"] == term["source_relation"]
        assert row["antibiotic_id"] == term["source_antibiotic_id"]
        assert hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest() == (
            term["source_row_sha256"]
        )


def test_source_typo_and_other_name_are_not_exact_taxonomy(dossier):
    names = dossier["name_resolutions"]
    typo = names["Trychophyton rubrum"]
    assert typo["candidates"] == [] and typo["named_organism_taxon_id"] is None
    assert dossier["terms"]["ARO:3009270"]["source_label"].startswith("Trychophyton rubrum ")
    other = names["Arthroderma vanbreuseghemii"]
    assert other["named_organism_taxon_id"] is None
    candidate, = other["candidates"]
    assert candidate["taxon_id"] == "NCBITaxon:523103"
    assert candidate["other_name_match_only"] is True and candidate["exact_name_fields"] == []


@pytest.mark.parametrize("name,taxid", [
    ("Trichophyton rubrum", 5551), ("Trichophyton interdigitale", 101480), ("Candida albicans", 5476),
])
def test_primary_species_names_resolve_separately(dossier, name, taxid):
    row = dossier["name_resolutions"][name]
    assert row["status"] == "EXACT_SPECIES_NAME_RESOLVED"
    assert row["named_organism_taxon_id"] == f"NCBITaxon:{taxid}"
    selected, = [c for c in row["candidates"] if c["taxon_id"] == row["named_organism_taxon_id"]]
    assert selected["active"] and selected["rank"] == "species"
    assert selected["exact_name_fields"] == ["scientificName"]


def test_explicit_archive_crosswalk_is_reference_only(dossier):
    row, = [r for r in dossier["reference_proteins"] if r["protein_accession"] == "UniProtKB:F2STB6"]
    assert row["archive_protein_ids"] == ["EGD89476.1"]
    assert row["reference_loci"] == ["TERG_05717"]
    assert row["reviewed"] is False
    assert (row["entry_version"], row["sequence_version"]) == (56, 1)
    assert row["reference_taxon_id"] == "NCBITaxon:559305"
    assert row["cites_yamada_2017"] is False


def test_upc2_reference_is_not_the_generic_term_or_experimental_background(dossier):
    row, = [r for r in dossier["reference_proteins"] if r["protein_accession"] == "UniProtKB:Q59QC7"]
    assert row["gene_symbols"] == ["UPC2"] and row["cgd_ids"] == ["CAL0000191743"]
    assert "CaO19.391" in row["reference_loci"]
    assert row["cites_macpherson_2005"] and row["reviewed"]
    assert (row["entry_version"], row["sequence_version"]) == (123, 1)
    assert row["reference_taxon_id"] == "NCBITaxon:237561"
    primary, = [p for p in dossier["primary_context"] if p["reference"] == "PMID:15855491"]
    assert primary["experimental_background_label"] == "SGY-243"
    assert primary["paper_locus"] == "orf19.391"
    assert dossier["terms"]["ARO:3009638"]["source_label"] == "antifungal susceptible Upc2"
    assert dossier["terms"]["ARO:3009638"]["exact_protein_assignment"] is None


def test_reference_strain_taxonomy_is_not_subject_taxonomy(dossier):
    taxa = {t["taxon_id"]: t for t in dossier["reference_taxonomy"]}
    assert taxa["NCBITaxon:559305"]["parent_taxon_id"] == "NCBITaxon:5551"
    assert taxa["NCBITaxon:237561"]["parent_taxon_id"] == "NCBITaxon:5476"
    assert all(t["rank"] == "strain" and t["scope"] == "REFERENCE_PROTEIN_TAXON_ONLY"
               for t in taxa.values())
    assert all(r["scope"] == "REFERENCE_IDENTITY_ONLY" and r["experimental_assignment"] is False
               and r["exact_card_term_mapping"] is False for r in dossier["reference_proteins"])


def test_negative_queries_are_bounded_not_absence_claims(dossier):
    searches = {s["query"]: s for s in dossier["protein_searches"]}
    assert {q: s["result_count"] for q, s in searches.items()} == {
        "EGD89476": 1, "EZF33561": 0, "gene_exact:orf19.391": 0,
        "gene_exact:UPC2 AND taxonomy_id:5476 AND reviewed:true": 1,
    }
    for row in searches.values():
        assert row["zero_results_establish_absence"] is False and row["complete_for_query"] is True
        request = row["request"]
        parsed = urlsplit(request["url"])
        assert parsed.scheme == "https" and parsed.hostname == "rest.uniprot.org"
        assert parsed.path == "/uniprotkb/search"
        params = parse_qs(parsed.query)
        assert params["query"] == [row["query"]] and params["size"] == ["100"]
        assert not {"sequence", "ft_variant", "ft_mutagen"} & set(params["fields"][0].split(","))
        assert request["status"] == 200 and request["release"] == "2026_03"


def test_incomplete_primary_review_and_source_ambiguity_remain_visible(dossier):
    assert dossier["curated"] is False and dossier["primary_review_complete"] is False
    assert all(not p["figures_visually_inspected"] and not p["native_primary_file_cached"]
               for p in dossier["primary_context"])
    assert all(not t["primary_review_complete"] for t in dossier["terms"].values())
    finding, = [f for f in dossier["review_findings"] if f["id"] == "F3"]
    assert finding["disposition"].startswith("OPEN_SOURCE_AMBIGUITY:")
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0
    assert dossier["preservation"]["ignored_files_included"] is True


def test_no_experimental_specifications_exported(dossier):
    forbidden = {"sequence", "features", "variant", "alteration", "construct", "primer", "mic", "mic_value",
                 "disk_diffusion", "strain_taxon_id", "assembly_accession", "biosample_accession",
                 "experimental_protein_accession"}

    def inspect(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)

    inspect(dossier)
    assert dossier["sequences_or_variant_specifications_exported"] is False

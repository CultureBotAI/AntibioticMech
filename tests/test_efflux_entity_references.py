"""Reference genes, complexes and variant categories retain different scopes."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "research/2026-10-10-efflux-entities-context.json"


@pytest.fixture(scope="module")
def dossier():
    return json.loads(CONTEXT.read_bytes())


def test_selection_covers_every_flagged_efflux_parent(dossier):
    prior = json.loads((ROOT / dossier["source_parent_audit"]["path"]).read_bytes())
    expected = {
        tid
        for tid, row in prior["terms"].items()
        if row["entity_scope"] == "EFFLUX_COMPLEX_OR_SUBUNIT_GRANULARITY_UNRESOLVED"
    }
    assert set(dossier["terms"]) == expected and len(expected) == 7
    assert len(dossier["annotations"]) == 35
    assert sum(len(r["record_memberships"]) for r in dossier["terms"].values()) == 13
    for tid, row in dossier["terms"].items():
        assert row["source_label_sha256"] == prior["terms"][tid]["source_label_sha256"]
        assert row["source_definition_citation_ids"] == prior["terms"][tid]["definition_citation_ids"]
        assert row["named_direct_subclass_ids"] == prior["terms"][tid]["named_direct_subclass_ids"]
        assert row["parent_accession_assignment"] is row["experimental_taxon_assignment"] is None
        assert not row["child_accession_propagation"]


def test_source_memberships_still_name_the_same_compounds_and_terms(dossier):
    with (ROOT / "data/raw/aro_resistance_edges.tsv").open() as stream:
        labels = {r["determinant_id"]: r["determinant_name"] for r in csv.DictReader(stream, delimiter="\t")}
    assert len(dossier["records"]) == 10
    for row in dossier["records"]:
        doc = load_record(ROOT / row["record"]["path"])
        assert doc["identifier"] == row["identifier"]
        assert doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        claims = [c for c in doc["resistance_mechanisms"] if c.get("aro_id") in dossier["terms"]]
        assert sorted(c["aro_id"] for c in claims) == row["selected_aro_ids"]
        for claim in claims:
            tid = claim["aro_id"]
            assert claim["label"] == labels[tid]
            assert (
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == dossier["terms"][tid]["source_label_sha256"]
            )


def test_complex_has_three_reference_components_not_one_accession(dossier):
    row = dossier["terms"]["ARO:3000798"]
    assert row["resolved_entity_scope"] == "MULTIPROTEIN_COMPLEX"
    assert row["reference_gene_candidates"] == {
        "mexE": ["UniProtKB:Q9I0Y9"],
        "mexF": ["UniProtKB:Q9I0Y8"],
        "oprN": ["UniProtKB:Q9I0Y7"],
    }
    assert dossier["reference_proteins"]["Q9I0Y7"]["explicit_card_xrefs"] == ["ARO:3000805"]
    assert "ARO:3000805" not in row["named_direct_subclass_ids"]
    assert (
        "regulator is not one of those components" in dossier["primary_reviews"]["PMID:10515918"]["finding"]
    )


@pytest.mark.parametrize(
    "tid,gene,accessions",
    [
        ("ARO:3003447", "iniA", ["P9WJ98", "P9WJ99"]),
        ("ARO:3003450", "iniC", ["P9WJ94", "P9WJ95"]),
        ("ARO:3004136", "iniB", ["P9WJ96", "P9WJ97"]),
    ],
)
def test_ini_strain_references_are_not_one_experimental_allele(dossier, tid, gene, accessions):
    row = dossier["terms"][tid]
    assert row["resolved_entity_scope"] == "GENE_VARIANT_CATEGORY"
    assert row["reference_gene_candidates"] == {gene: ["UniProtKB:" + a for a in accessions]}
    proteins = [dossier["reference_proteins"][a] for a in accessions]
    assert {r["reference_taxon_id"] for r in proteins} == {"NCBITaxon:83331", "NCBITaxon:83332"}
    assert all(r["gene_symbol"] == gene and r["reference_taxon_rank"] == "strain" for r in proteins)
    assert row["citation_binding"] == (
        "SOURCE_DEFINITION_CITATION"
        if gene == "iniB"
        else "INDEPENDENT_COHORT_CONTEXT_NOT_A_DEFINITION_CITATION"
    )
    assert "association from proof" in dossier["primary_reviews"]["PMID:10639358"]["finding"]


def test_yor1_reference_locus_is_not_the_posaconazole_allele(dossier):
    row = dossier["terms"]["ARO:3009466"]
    protein = dossier["reference_proteins"]["Q6FTR9"]
    assert row["reference_gene_candidates"] == {"YOR1": ["UniProtKB:Q6FTR9"]}
    assert protein["reference_loci"] == ["CAGL0G00242g"]
    assert protein["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["reference_taxon_id"] == "NCBITaxon:284593"
    assert row["source_definition_citation_ids"] == []
    assert row["citation_binding"] == "INDEPENDENT_FOLLOWUP_NOT_A_DEFINITION_CITATION"
    assert "POSACONAZOLE_ALLELE_AND_TRANSPORT_CLAIM_UNRESOLVED" in row["disposition"]
    assert "not generalized to every azole" in dossier["primary_reviews"]["PMID:35038899"]["limit"]
    assert "homology basis remains explicit" in dossier["primary_reviews"]["PMID:20547810"]["finding"]


def test_families_do_not_select_a_representative_protein(dossier):
    flo, mdr = (dossier["terms"][t] for t in ("ARO:3003963", "ARO:3009425"))
    assert flo["reference_gene_candidates"] == mdr["reference_gene_candidates"] == {}
    assert flo["reused_reference"] == "UniProtKB:Q9F0D9"
    prior = ROOT / flo["prior_followup"]["path"]
    assert hashlib.sha256(prior.read_bytes()).hexdigest() == flo["prior_followup"]["sha256"]
    assert mdr["resolved_entity_scope"] == "FUNGAL_MDR1_FAMILY_CATEGORY"
    assert len(mdr["named_direct_subclass_ids"]) == 19
    assert mdr["evidence"] == [] and mdr["primary_evidence_review"] == "OPEN"


@pytest.mark.parametrize(
    "strain,species", [("208964", "287"), ("83331", "1773"), ("83332", "1773"), ("284593", "5478")]
)
def test_taxonomy_keeps_rank_and_parentage(dossier, strain, species):
    taxa = dossier["reference_taxonomy"]
    assert taxa[strain]["rank"] == "strain" and taxa[species]["rank"] == "species"
    assert taxa[strain]["parent"]["taxonId"] == int(species)
    assert taxa[strain]["active"] and taxa[species]["active"]
    assert not taxa[strain]["experimental_subject_assignment"]


def test_all_reference_metadata_stays_nonexperimental(dossier):
    assert len(dossier["reference_proteins"]) == 10
    focal = set(dossier["primary_reviews"])
    for protein in dossier["reference_proteins"].values():
        assert protein["sequence_version"] == 1 and protein["entry_version"] > 0
        assert protein["reference_release"] == "2026_03"
        assert not protein["experimental_subject_assignment"]
        assert not protein["exact_allele_assignment"] and not protein["experimental_genome_assignment"]
        assert not focal & set(protein["entry_citation_ids"])
        assert not set(dossier["terms"]) & set(protein["explicit_card_xrefs"])


def test_query_limits_and_endpoint_deferral_are_explicit(dossier):
    assert len(dossier["requests"]) == 11
    for key, row in dossier["requests"].items():
        url = urlsplit(row["url"])
        assert url.scheme == "https" and url.hostname in {"rest.uniprot.org", "www.ebi.ac.uk"}
        assert row["status"] == 200
        if key.startswith("query-"):
            assert "sequence" not in parse_qs(url.query)["fields"][0].split(",")
    assert {name: r["result_count"] for name, r in dossier["queries"].items()} == {
        "mex": 3,
        "ini": 6,
        "yor1": 1,
    }
    assert all(
        r["complete_for_query"] and not r["establishes_biological_absence"]
        for r in dossier["queries"].values()
    )
    assert dossier["queries"]["mex"]["reviewed_only"] and dossier["queries"]["ini"]["reviewed_only"]
    assert not dossier["queries"]["yor1"]["reviewed_only"]


def test_scope_is_identity_review_not_whole_record_completion(dossier):
    assert dossier["whole_corpus_primary_review"] == "OPEN"
    assert dossier["summary"]["biological_record_changes"] == 0
    assert dossier["summary"]["new_experimental_assignments"] == 0
    assert dossier["summary"]["whole_record_reviews_completed"] == 0
    assert all(not r["whole_paper_review_complete"] for r in dossier["primary_reviews"].values())
    forbidden = {
        "sequence",
        "features",
        "alteration",
        "modification",
        "mic_value",
        "measurement_value",
        "assembly_accession",
    }

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not forbidden & set(keys(dossier))

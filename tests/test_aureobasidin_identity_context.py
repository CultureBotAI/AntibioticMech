"""An upstream chemical discrepancy must not become an exact resistance claim."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-12-aureobasidin-identity-context.json").read_bytes())


def test_historical_identity_is_bound_to_review_census_not_current_record(dossier):
    # A future source-owned identity repair must not invalidate this historical hold.
    census = dossier["baseline_census"]
    payload = (ROOT / census["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == census["sha256"]
    rows = list(csv.DictReader(payload.decode().splitlines(), delimiter="\t"))
    record = dossier["record"]
    row, = [r for r in rows if r["identifier"] == record["identifier"]]
    assert row["record_sha256"] == record["review_time_sha256"]
    assert row["path"] == record["path"]
    assert row["standard_inchi_key"] == dossier["chemical_identity"]["review_time_structure"][
        "standard_inchi_key"
    ]
    assert int(row["resistance_assertions"]) == record["review_time_resistance_assertions"] == 0
    assert record["whole_record_review"] == "OPEN"


def test_identity_hold_does_not_invent_a_replacement_structure(dossier):
    identity = dossier["chemical_identity"]
    snapshot = identity["review_time_structure"]
    graph = identity["graph_check"]
    assert hashlib.sha256(snapshot["smiles"].encode()).hexdigest() == graph["smiles_sha256"]
    assert graph["computed_formula"] == snapshot["molecular_formula"] == "C60H92N8O10"
    assert graph["computed_inchi_key"] == snapshot["standard_inchi_key"]
    assert graph["hydroxyl_count"] == 0 and graph["oxygen_atom_count"] == 10
    assert identity["source_owner"]["path"] == "data/raw/chebi_antimicrobials.tsv"
    assert identity["live_chebi"]["matches_inventory_smiles_inchi_key_and_formula"] is True
    conflict = identity["conflict"]
    assert conflict["decision"] == "HOLD_EXACT_STRUCTURE_CLAIM_TRANSFER"
    assert not conflict["replacement_structure_assigned"] and not conflict["cause_established"]
    assert "HOMeVal" in conflict["observation"]


def test_graph_snapshot_reproduces_with_rdkit_when_available(dossier):
    chem = pytest.importorskip("rdkit.Chem")
    descriptors = pytest.importorskip("rdkit.Chem.rdMolDescriptors")
    identity = dossier["chemical_identity"]
    molecule = chem.MolFromSmiles(identity["review_time_structure"]["smiles"])
    assert molecule is not None
    graph = identity["graph_check"]
    assert descriptors.CalcMolFormula(molecule) == graph["computed_formula"]
    assert chem.MolToInchiKey(molecule) == graph["computed_inchi_key"]
    assert sum(atom.GetSymbol() == "O" for atom in molecule.GetAtoms()) == graph["oxygen_atom_count"]
    assert len(molecule.GetSubstructMatches(chem.MolFromSmarts(graph["hydroxyl_smarts"]))) == 0


def test_biochemical_evidence_and_visual_review_stay_scoped(dossier):
    review = dossier["primary_review"]
    assert review["reference"] == "PMID:40442105"
    assert review["doi"] == "10.1038/s41467-025-60423-y"
    assert review["main_pdf"]["visually_inspected_pages_one_based"] == [2, 8]
    assert review["main_pdf"]["figures_visually_inspected"] == [1, 6]
    assert review["supplement"]["visually_inspected_pages_one_based"] == [12]
    assert review["supplement"]["figures_visually_inspected"] == ["S11"]
    assert review["measurement_scope"] == "ENZYME_ACTIVITY_AND_BINDING_NOT_AST"
    assert not review["whole_paper_review_complete"]
    assert not review["source_data_workbooks_reviewed"]
    assert review["license"] == "CC BY-NC-ND 4.0"
    assert "not republished" in review["reuse_boundary"]


def test_gene_and_taxon_are_reference_context_not_resistant_subject(dossier):
    ref = dossier["reference_grounding"]
    assert (ref["accession"], ref["gene"], ref["ordered_locus_names"]) == (
        "UniProtKB:P36107", "AUR1", ["YKL004W"],
    )
    assert (ref["entry_version"], ref["sequence_version"], ref["release"]) == (184, 1, "2026_03")
    assert ref["paper_deposited_structure"] == "PDB:9IVC"
    assert ref["uniprot_has_paper_pdb_cross_reference"] is True
    assert (ref["taxon_id"], ref["taxon_rank"]) == ("NCBITaxon:559292", "strain")
    assert (ref["parent_taxon_id"], ref["parent_rank_from_lineage"]) == ("NCBITaxon:4932", "species")
    assert ref["scope"] == "REFERENCE_IDENTITY_ONLY_NOT_RESISTANT_SUBJECT"
    for key in (
        "experimental_allele_assigned", "experimental_genome_assigned", "resistant_strain_taxid_assigned",
    ):
        assert ref[key] is False


def test_exact_identifier_requests_have_no_sequence_payload(dossier):
    search, taxonomy = dossier["uniprot_requests"]
    for request in (search, taxonomy):
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert len(request["sha256"]) == len(request["cache_file_sha256"]) == 64
    query = parse_qs(urlsplit(search["url"]).query)
    assert query["query"] == ["accession:P36107"]
    assert "sequence" not in query["fields"][0].split(",")
    assert search["total_results"] == search["result_count"] == 1
    assert search["complete_for_exact_accession_query_only"] and not search["next_page_present"]
    assert urlsplit(taxonomy["url"]).path == "/taxonomy/559292.json"


def test_unresolved_identity_is_not_curated_or_counted_complete(dossier):
    disposition = dossier["disposition"]
    assert disposition["decision"] == "HOLD_BIOLOGICAL_CURATION_UNTIL_COMPOUND_IDENTITY_RESOLVED"
    assert all(value == 0 for key, value in disposition.items() if key != "decision")
    assert not dossier["access_history"]["publisher_credentials_used"]
    assert not dossier["access_history"]["paywall_bypass"]


def test_public_projection_omits_experimental_specifications(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "protocol", "primers", "constructs",
        "mic_value", "measurement_value", "resistance_mechanisms", "activity_spectrum", "headers",
    }

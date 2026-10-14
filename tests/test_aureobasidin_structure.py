"""Three deposited polymers are not three resistance genes or one organism."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_aureobasidin_structure as audit  # noqa: E402


def deposition_fixture():
    links = {
        "rcsb_id": "9IVC",
        "rcsb_accession_info": {"major_revision": 1, "minor_revision": 0,
                                "revision_date": "2025-06-18T00:00:00Z"},
        "rcsb_primary_citation": {"pdbx_database_id_PubMed": 40442105,
                                  "pdbx_database_id_DOI": "10.1038/s41467-025-60423-y", "year": 2025},
        "rcsb_entry_container_identifiers": {"non_polymer_entity_ids": None}, "polymer_entities": [],
    }
    kinds = {"rcsb_id": "9IVC", "rcsb_accession_info": copy.deepcopy(links["rcsb_accession_info"]),
             "polymer_entities": []}
    ids = {"rcsb_id": "9IVC", "polymer_entities": []}
    for i, accession, name in (
        (1, "P36107", "Inositol phosphorylceramide synthase catalytic subunit AUR1"),
        (2, "Q06346", "Inositol phosphorylceramide synthase regulatory subunit KEI1"),
        (3, None, "Aureobasidin A"),
    ):
        eid = "9IVC_" + str(i)
        refs = [{"database_name": "UniProt", "database_accession": accession}] if accession else None
        organism = {"ncbi_taxonomy_id": 559292, "scientific_name": "Saccharomyces cerevisiae S288C"}
        if i == 3:
            organism = {"ncbi_taxonomy_id": 5580, "scientific_name": "Aureobasidium pullulans R106"}
        links["polymer_entities"].append({
            "rcsb_id": eid, "rcsb_entity_source_organism": [organism],
            "rcsb_polymer_entity_container_identifiers": {"reference_sequence_identifiers": refs}})
        kinds["polymer_entities"].append({"rcsb_id": eid,
            "rcsb_polymer_entity": {"pdbx_description": name}, "entity_poly": {"type": "polypeptide(L)"}})
        ids["polymer_entities"].append({"rcsb_id": eid, "rcsb_polymer_entity_container_identifiers": {
            "prd_id": None,
            "chem_comp_monomers": ["A1L3I", "A1L3J", "IIL", "LEU", "MEA", "MVA", "PHE", "PRO"],
            "chem_comp_nstd_monomers": ["A1L3I", "A1L3J", "IIL", "MEA", "MVA"]}})
    return [{"data": {"entries": [e]}} for e in (links, kinds, ids)]


def test_ligand_is_not_an_unmapped_resistance_protein():
    entities, ligand = audit.classify_entities(*deposition_fixture())
    assert [e["reference_accessions"] for e in entities] == [
        ["UniProtKB:P36107"], ["UniProtKB:Q06346"], []]
    assert entities[2]["reviewed_role"] == "PEPTIDE_LIGAND_NOT_RESISTANCE_PROTEIN"
    assert ligand["uniprot_absence_is_missing_resistance_protein"] is False
    assert ligand["unique_chemical_component_count"] == 8
    assert ligand["component_set_is_ordered_sequence_or_complete_cyclic_structure"] is False
    assert ligand["polymer_formula_weight_used_as_exact_drug_mass"] is False


@pytest.mark.parametrize("change", ["entry", "duplicate_entry", "citation", "revision", "partition",
                                    "duplicate_entity", "missing_entity", "type", "description",
                                    "swap_accession", "ligand_accession", "swap_organism", "bird",
                                    "missing_component", "duplicate_component", "errors"])
def test_entity_scope_and_graphql_guards(change):
    payloads = deposition_fixture()
    links, kinds, ids = [p["data"]["entries"][0] for p in payloads]
    if change == "entry":
        links["rcsb_id"] = "9IVD"
    elif change == "duplicate_entry":
        payloads[0]["data"]["entries"] *= 2
    elif change == "citation":
        links["rcsb_primary_citation"]["year"] = 2007
    elif change == "revision":
        kinds["rcsb_accession_info"]["minor_revision"] += 1
    elif change == "partition":
        links["rcsb_entry_container_identifiers"]["non_polymer_entity_ids"] = ["3"]
    elif change == "duplicate_entity":
        kinds["polymer_entities"][2] = copy.deepcopy(kinds["polymer_entities"][1])
    elif change == "missing_entity":
        links["polymer_entities"].pop()
    elif change == "type":
        kinds["polymer_entities"][2]["entity_poly"]["type"] = "polydeoxyribonucleotide"
    elif change == "description":
        kinds["polymer_entities"][2]["rcsb_polymer_entity"]["pdbx_description"] = "Other ligand"
    elif change == "swap_accession":
        links["polymer_entities"][0]["rcsb_polymer_entity_container_identifiers"][
            "reference_sequence_identifiers"][0]["database_accession"] = "Q06346"
    elif change == "ligand_accession":
        links["polymer_entities"][2]["rcsb_polymer_entity_container_identifiers"][
            "reference_sequence_identifiers"] = [{"database_name": "UniProt", "database_accession": "P36107"}]
    elif change == "swap_organism":
        links["polymer_entities"][0]["rcsb_entity_source_organism"] = links["polymer_entities"][2][
            "rcsb_entity_source_organism"]
    elif change == "bird":
        ids["polymer_entities"][2]["rcsb_polymer_entity_container_identifiers"]["prd_id"] = "PRD_example"
    elif change in {"missing_component", "duplicate_component"}:
        names = ids["polymer_entities"][2]["rcsb_polymer_entity_container_identifiers"]["chem_comp_monomers"]
        if change == "missing_component":
            names.pop()
        else:
            names.append(names[0])
    else:
        payloads[0]["errors"] = [{"message": "Query failed"}]
    with pytest.raises(ValueError):
        audit.classify_entities(*payloads)


def protein_fixture(accession="Q06346"):
    expected = audit.PROTEINS[accession]
    tax = {"taxonId": 559292, "rank": "strain", "active": True,
           "scientificName": "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)",
           "lineage": [{"taxonId": 4932, "rank": "species", "scientificName": "Saccharomyces cerevisiae"}]}
    entry = {"primaryAccession": accession, "entryType": "UniProtKB reviewed (Swiss-Prot)",
             "entryAudit": {"entryVersion": expected["entry"], "sequenceVersion": expected["sequence"]},
             "organism": {"taxonId": 559292, "scientificName": tax["scientificName"]},
             "genes": [{"geneName": {"value": expected["gene"]},
                        "orderedLocusNames": [{"value": expected["locus"]}]}],
             "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference component"}}},
             "uniProtKBCrossReferences": [{"database": "PDB", "id": "9IVC"}]}
    return entry, tax


@pytest.mark.parametrize("accession", ["P36107", "Q06346"])
def test_component_references_never_represent_whole_complex(accession):
    result = audit.protein_context(*protein_fixture(accession))
    assert result["protein_accession"] == "UniProtKB:" + accession
    assert result["whole_complex_assigned_to_one_accession"] is False
    assert result["resistance_inferred_from_membership"] is False
    assert result["experimental_subject_assignment"] is result["exact_resistance_allele"] is False


@pytest.mark.parametrize("change", ["accession", "locus", "version", "sequence_version", "gene",
                                    "source_taxon", "rank", "inactive", "pdb", "sequence"])
def test_reference_component_guards(change):
    entry, tax = protein_fixture()
    if change == "accession":
        entry["primaryAccession"] = "Q00000"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "YKL004W"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "AUR1"
    elif change == "source_taxon":
        entry["organism"]["taxonId"] = 5580
    elif change == "rank":
        tax["rank"] = "species"
    elif change == "inactive":
        tax["active"] = False
    elif change == "pdb":
        entry["uniProtKBCrossReferences"] = []
    else:
        entry["sequence"] = {}
    with pytest.raises(ValueError):
        audit.protein_context(entry, tax)


@pytest.mark.parametrize("change", ["none", "taxon", "rank", "name", "inactive"])
def test_producer_is_species_context_not_resistant_strain(change):
    tax = {"taxonId": 5580, "rank": "species", "scientificName": "Aureobasidium pullulans", "active": True}
    if change == "taxon":
        tax["taxonId"] = 559292
    elif change == "rank":
        tax["rank"] = "strain"
    elif change == "name":
        tax["scientificName"] = "Saccharomyces cerevisiae"
    elif change == "inactive":
        tax["active"] = False
    if change == "none":
        result = audit.producer_context(tax)
        assert result["strain_specific_taxon_assignment"] is result["resistant_phenotype_assigned"] is False
        assert result["experimental_genome_assignment"] is None
    else:
        with pytest.raises(ValueError):
            audit.producer_context(tax)


@pytest.mark.parametrize("change", ["none", "id", "status", "formula", "key", "smiles"])
def test_free_component_graph_is_not_a_reconstructed_drug(change):
    pytest.importorskip("rdkit.Chem")
    payload = {"rcsb_id": "A1L3I", "chem_comp": {"id": "A1L3I", "pdbx_release_status": "REL",
        "formula": "C6 H13 N O3", "name": "Hydroxylated component", "type": "L-peptide linking"},
        "rcsb_chem_comp_descriptor": {"comp_id": "A1L3I", "SMILES_stereo": "CC(C)([C@@H](C(=O)O)NC)O",
                                      "InChIKey": "OMDFZKXSWRGNGX-SCSAIBSYSA-N"},
        "rcsb_chem_comp_info": {"revision_date": "2025-06-18T00:00:00.000+00:00"}}
    if change == "id":
        payload["rcsb_id"] = "A1L3J"
    elif change == "status":
        payload["chem_comp"]["pdbx_release_status"] = "HOLD"
    elif change == "formula":
        payload["chem_comp"]["formula"] = "C6 H13 N O2"
    elif change == "key":
        payload["rcsb_chem_comp_descriptor"]["InChIKey"] = "RILPIWOPNGRASR-RFZPGFLSSA-N"
    elif change == "smiles":
        payload["rcsb_chem_comp_descriptor"]["SMILES_stereo"] = "CCO"
    if change == "none":
        result = audit.component_context(payload, "A1L3I")
        assert result["free_component_graph"]["aliphatic_hydroxyl_count"] == 1
        assert result["free_component_graph"]["hydroxyl_count"] == 2
        assert result["free_component_is_whole_drug"] is False
        assert result["free_component_hydroxyl_count_is_polymer_hydroxyl_count"] is False
    else:
        with pytest.raises(ValueError):
            audit.component_context(payload, "A1L3I")


def test_public_dossier_keeps_prior_hold_and_has_no_allele_signoff():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert len(data["protein_references"]) == 2
    assert len(data["deposition_entities"]) == 3
    assert data["baseline_graph"]["hydroxyl_count"] == 0
    assert data["chemical_disposition"]["source_owned_identity_conflict_resolved"] is False
    assert data["chemical_disposition"]["replacement_structure_assigned"] is False
    assert data["limits"]["biological_changes"] == data["limits"]["whole_record_primary_signoffs"] == 0
    assert data["limits"]["ncbi_requests"] == 0 and data["limits"]["issue_1040"] == "DEFERRED"


def test_offline_dated_replay_does_not_load_live_biological_record(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")
    pytest.importorskip("rdkit.Chem")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network access")

    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(sys, "argv", ["audit_aureobasidin_structure.py", "--check"])
    audit.main()

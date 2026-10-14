"""Separate deposited protein references, peptide ligand and producer taxonomy."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_structure_links as structures
import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-aureobasidin-structure")
OUTPUT = Path("research/2026-10-14-aureobasidin-structure-context.json")
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,xref_pdb,sequence_version,version"
)
SOURCES = {
    "pdb-9ivc": ("request-plan.json", "171cedf9864fb359f9f8587fc6698607ed0661c31963e8d57e5697ace2afc25e"),
    "entity-types": (
        "followup-plan.json",
        "3071515e6abca08d21392d4ef94b407f70a96be770052d57d1f8ff8b2cf13cd3",
    ),
    "ligand-identifiers": (
        "ligand-plan.json",
        "646d4a5c0729fced55fd1660048fdb19c631a1d2fae089480ff5e6da9bdd2960",
    ),
    "kei1-reference": (
        "followup-plan.json",
        "8b73ac51358488481e98bfba1b77a2b44a58d7b95415b0b244616654a01effa7",
    ),
    "producer-taxonomy": (
        "followup-plan.json",
        "0ce645a6861a7ac8cff646a5ea2169375222e73bff9fe4f78b5c99b251af4ba1",
    ),
    "component-a1l3i": (
        "component-plan.json",
        "f7fac9b19195411de7809d85e633f481a2697ea304d6e17403b62b0a912e330f",
    ),
    "component-a1l3j": (
        "component-plan.json",
        "2dd170a677d957e21ece69ca045a857afe73a12b92fc712e2f36cc16a4b3691f",
    ),
}
COMPONENTS = {
    "A1L3I": ("C6H13NO3", "OMDFZKXSWRGNGX-SCSAIBSYSA-N"),
    "A1L3J": ("C6H12O3", "RILPIWOPNGRASR-RFZPGFLSSA-N"),
}
PROTEINS = {
    "P36107": {"gene": "AUR1", "locus": "YKL004W", "entry": 184, "sequence": 1, "entity": "9IVC_1"},
    "Q06346": {"gene": "KEI1", "locus": "YDR367W", "entry": 151, "sequence": 2, "entity": "9IVC_2"},
}


def native(root, directory, key):
    plan_name, checksum = SOURCES[key]
    path = directory / plan_name
    plan = json.loads(path.read_bytes())
    attempt = json.loads((directory / (key + "-attempt.json")).read_bytes())
    url = plan["requests"][key]["url"]
    parsed = urlsplit(url)
    if (
        parsed.scheme != "https"
        or parsed.netloc not in {"data.rcsb.org", "rest.uniprot.org"}
        or parsed.fragment
        or attempt["plan_sha256"] != reference.digest(path)
        or attempt.get("retry_performed") is not False
    ):
        raise ValueError("request plan changed or endpoint not permitted")
    source = native_context.native(root, directory, key, url)
    receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
    if source["body"]["sha256"] != checksum or receipt.get("redirects_followed") is not False:
        raise ValueError("reviewed response changed or redirected")
    data = json.loads(reference.check_pin(root, source["body"]).read_bytes())
    if data.get("errors"):
        raise ValueError("GraphQL errors are not successful scientific data")
    return data, {**source, "plan": reference.pin(root, path)}


def entry(payload):
    if payload.get("errors"):
        raise ValueError("GraphQL errors")
    entries = payload["data"]["entries"]
    if len(entries) != 1 or entries[0]["rcsb_id"] != "9IVC":
        raise ValueError("deposition identity absent or ambiguous")
    return entries[0]


def entity_map(entry_data):
    rows = entry_data["polymer_entities"]
    result = {r["rcsb_id"]: r for r in rows}
    if len(rows) != 3 or set(result) != {"9IVC_1", "9IVC_2", "9IVC_3"}:
        raise ValueError("deposited entities missing, duplicated or mixed")
    return result


def classify_entities(link_data, type_data, ligand_data):
    links, kinds, ids = map(entry, (link_data, type_data, ligand_data))
    if (
        links["rcsb_primary_citation"]
        != {
            "pdbx_database_id_PubMed": 40442105,
            "pdbx_database_id_DOI": "10.1038/s41467-025-60423-y",
            "year": 2025,
        }
        or links["rcsb_accession_info"] != kinds["rcsb_accession_info"]
        or links["rcsb_accession_info"]
        != {"major_revision": 1, "minor_revision": 0, "revision_date": "2025-06-18T00:00:00Z"}
        or links["rcsb_entry_container_identifiers"]["non_polymer_entity_ids"] is not None
    ):
        raise ValueError("paper, revision or entity partition changed")
    link_map, type_map, id_map = map(entity_map, (links, kinds, ids))
    references = {r["entity_id"]: r for r in structures.entity_references(links)}
    expected_names = {
        "9IVC_1": "Inositol phosphorylceramide synthase catalytic subunit AUR1",
        "9IVC_2": "Inositol phosphorylceramide synthase regulatory subunit KEI1",
        "9IVC_3": "Aureobasidin A",
    }
    result = []
    for eid in sorted(link_map):
        name = type_map[eid]["rcsb_polymer_entity"]["pdbx_description"]
        if name != expected_names[eid] or type_map[eid]["entity_poly"]["type"] != "polypeptide(L)":
            raise ValueError("deposited entity type or description changed")
        row = references[eid]
        accession = {"9IVC_1": "P36107", "9IVC_2": "Q06346"}.get(eid)
        expected_refs = ["UniProtKB:" + accession] if accession else []
        expected_source = [{"ncbi_taxonomy_id": 559292, "scientific_name": "Saccharomyces cerevisiae S288C"}]
        if eid == "9IVC_3":
            expected_source = [{"ncbi_taxonomy_id": 5580, "scientific_name": "Aureobasidium pullulans R106"}]
        if (
            row["reference_accessions"] != expected_refs
            or row["other_reference_identifiers"]
            or row["source_organisms"] != expected_source
        ):
            raise ValueError("entity-specific reference or organism changed")
        result.append(
            {
                **row,
                "deposition_description": name,
                "deposition_polymer_type": type_map[eid]["entity_poly"]["type"],
                "reviewed_role": "PEPTIDE_LIGAND_NOT_RESISTANCE_PROTEIN"
                if eid == "9IVC_3"
                else "PROTEIN_COMPONENT_REFERENCE_NOT_TESTED_RESISTANCE_ALLELE",
            }
        )
    ligand = id_map["9IVC_3"]["rcsb_polymer_entity_container_identifiers"]
    if (
        ligand["prd_id"] is not None
        or len(ligand["chem_comp_monomers"]) != len(set(ligand["chem_comp_monomers"]))
        or len(ligand["chem_comp_nstd_monomers"]) != len(set(ligand["chem_comp_nstd_monomers"]))
        or set(ligand["chem_comp_monomers"]) != {"A1L3I", "A1L3J", "IIL", "LEU", "MEA", "MVA", "PHE", "PRO"}
        or set(ligand["chem_comp_nstd_monomers"]) != {"A1L3I", "A1L3J", "IIL", "MEA", "MVA"}
    ):
        raise ValueError("ligand component membership changed")
    return result, {
        "entity_id": "9IVC_3",
        "bird_identifier_returned": None,
        "uniprot_absence_is_missing_resistance_protein": False,
        "unique_chemical_component_count": len(ligand["chem_comp_monomers"]),
        "reviewed_component_ids": sorted(COMPONENTS),
        "component_set_is_ordered_sequence_or_complete_cyclic_structure": False,
        "polymer_formula_weight_used_as_exact_drug_mass": False,
        "formula_reconstructed_by_summing_components": False,
        "atomic_contact_or_binding_mechanism_verified_from_metadata": False,
    }


def graph_properties(smiles):
    from rdkit import Chem, rdBase
    from rdkit.Chem import rdMolDescriptors

    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError("invalid chemical structure")
    return {
        "rdkit_version": rdBase.rdkitVersion,
        "smiles_sha256": hashlib.sha256(smiles.encode()).hexdigest(),
        "formula": rdMolDescriptors.CalcMolFormula(molecule),
        "inchi_key": Chem.MolToInchiKey(molecule),
        "hydroxyl_count": len(molecule.GetSubstructMatches(Chem.MolFromSmarts("[OX2H]"))),
        "aliphatic_hydroxyl_count": len(molecule.GetSubstructMatches(Chem.MolFromSmarts("[OX2H][CX4]"))),
    }


def component_context(payload, identifier):
    chem = payload["chem_comp"]
    descriptors = payload["rcsb_chem_comp_descriptor"]
    if (
        payload["rcsb_id"] != identifier
        or chem["id"] != identifier
        or descriptors["comp_id"] != identifier
        or chem["pdbx_release_status"] != "REL"
    ):
        raise ValueError("chemical component identity or release status changed")
    graph = graph_properties(descriptors["SMILES_stereo"])
    if (
        (graph["formula"], graph["inchi_key"]) != COMPONENTS[identifier]
        or chem["formula"].replace(" ", "") != graph["formula"]
        or descriptors["InChIKey"] != graph["inchi_key"]
        or graph["hydroxyl_count"] != 2
        or graph["aliphatic_hydroxyl_count"] != 1
    ):
        raise ValueError("component descriptor or hydroxyl chemistry changed")
    return {
        "component_id": identifier,
        "name": chem["name"],
        "component_type": chem["type"],
        "source_revision_date": payload["rcsb_chem_comp_info"]["revision_date"],
        "free_component_graph": graph,
        "free_component_is_whole_drug": False,
        "free_component_hydroxyl_count_is_polymer_hydroxyl_count": False,
    }


def protein_context(entry_data, taxonomy):
    accession = entry_data["primaryAccession"]
    if accession not in PROTEINS or {"sequence", "features", "comments"}.intersection(entry_data):
        raise ValueError("unplanned protein or biological payload")
    expected = PROTEINS[accession]
    result = reference.project_reference(entry_data, expected["gene"], 4932, taxonomy)
    if (
        result["ordered_locus_names"] != [expected["locus"]]
        or result["entry_version"] != expected["entry"]
        or result["sequence_version"] != expected["sequence"]
        or entry_data["organism"]["taxonId"] != 559292
        or taxonomy["rank"] != "strain"
        or entry_data["organism"]["scientificName"] != taxonomy["scientificName"]
        or not any(
            r.get("database") == "PDB" and r.get("id") == "9IVC"
            for r in entry_data.get("uniProtKBCrossReferences", [])
        )
    ):
        raise ValueError("component reference identity or reciprocal deposition link changed")
    result.pop("bibliography")
    return {
        **result,
        "gene": expected["gene"],
        "pdb_entity": expected["entity"],
        "reciprocal_deposition_reference": "PDB:9IVC",
        "role": "COMPLEX_COMPONENT_REFERENCE",
        "whole_complex_assigned_to_one_accession": False,
        "resistance_inferred_from_membership": False,
    }


def producer_context(taxonomy):
    if (
        taxonomy["taxonId"] != 5580
        or taxonomy.get("active") is not True
        or taxonomy["rank"] != "species"
        or taxonomy["scientificName"] != "Aureobasidium pullulans"
    ):
        raise ValueError("producer reference taxonomy changed")
    return {
        "taxon_id": "NCBITaxon:5580",
        "rank": "species",
        "name": taxonomy["scientificName"],
        "deposition_label": "Aureobasidium pullulans R106",
        "role": "LIGAND_SOURCE_NOT_RESISTANT_HOST",
        "strain_specific_taxon_assignment": False,
        "experimental_genome_assignment": None,
        "resistant_phenotype_assigned": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("baseline", "protected", "census", "source_queue", "identity_hold", "previous_checkpoint"):
        reference.check_pin(root, cohort[key])
    record = load_record(reference.check_pin(root, cohort["baseline"]))
    identity = record["chemical_structure"]
    if (
        (record["identifier"], identity["standard_inchi_key"])
        != ("CHEBI:61739", "YHSKJPXGXIYLHB-OTNPUQRPSA-N")
        or cohort["record"]["identifier"] != record["identifier"]
        or cohort["record"]["standard_inchi_key"] != identity["standard_inchi_key"]
        or cohort["record"]["sha256"] != cohort["baseline"]["sha256"]
    ):
        raise ValueError("dated chemical identity changed")
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    members = [r for r in rows if r["identifier"] == record["identifier"]]
    if (
        len(rows) != 2939
        or len({r["identifier"] for r in rows}) != 2939
        or len(members) != 1
        or members[0]["record_sha256"] != cohort["record"]["sha256"]
        or members[0]["path"] != cohort["record"]["path"]
    ):
        raise ValueError("dated corpus membership changed")
    data, sources = {}, {}
    for key in SOURCES:
        data[key], sources[key] = native(root, directory, key)
    entities, ligand = classify_entities(data["pdb-9ivc"], data["entity-types"], data["ligand-identifiers"])
    old = json.loads(reference.check_pin(root, cohort["identity_hold"]).read_bytes())
    reused, raw = {}, {}
    for name, request in zip(("aur1", "yeast-taxonomy"), old["uniprot_requests"], strict=True):
        path = root / request["local_cache"]
        if reference.digest(path) != request["cache_file_sha256"]:
            raise ValueError("previous reference cache changed")
        receipt, payload, source = structures.receipt(root, path, "rest.uniprot.org")
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        if (
            receipt["url"] != request["url"]
            or receipt["sha256"] != request["sha256"]
            or headers.get("x-uniprot-release") != "2026_03"
            or headers.get("link")
        ):
            raise ValueError("previous reference receipt changed")
        if name == "aur1":
            params = parse_qs(urlsplit(receipt["url"]).query)
            if (
                params
                != {"query": ["accession:P36107"], "fields": [FIELDS], "format": ["json"], "size": ["1"]}
                or len(payload["results"]) != 1
                or headers.get("x-total-results") != "1"
            ):
                raise ValueError("previous accession query incomplete or changed")
        raw[name], reused[name] = payload, source
    kei1, sources["kei1-metadata"] = reference.read_response(
        root,
        directory,
        "kei1-reference",
        "/uniprotkb/search",
        {"query": ["accession:Q06346"], "format": ["json"], "size": ["500"], "fields": [FIELDS]},
    )
    producer, sources["producer-metadata"] = reference.read_response(
        root, directory, "producer-taxonomy", "/taxonomy/5580"
    )
    if len(kei1["results"]) != 1 or any(
        sources[k]["release"] != "2026_03" for k in ("kei1-metadata", "producer-metadata")
    ):
        raise ValueError("new UniProt result count or release changed")
    proteins = [
        protein_context(e, raw["yeast-taxonomy"]) for e in (raw["aur1"]["results"][0], kei1["results"][0])
    ]
    components = {
        identifier: component_context(data["component-" + identifier.lower()], identifier)
        for identifier in COMPONENTS
    }
    baseline_graph = graph_properties(identity["smiles"])
    if (
        baseline_graph["formula"] != identity["molecular_formula"]
        or baseline_graph["inchi_key"] != identity["standard_inchi_key"]
        or baseline_graph["hydroxyl_count"] != 0
    ):
        raise ValueError("baseline chemical graph no longer reproduces")
    return {
        "date": "2026-10-14",
        "scope": "DEPOSITION_ENTITY_DISAMBIGUATION_WITH_CHEMICAL_IDENTITY_HOLD",
        "cohort": reference.pin(root, directory / "cohort.json"),
        "record": cohort["record"],
        "inputs": {
            k: cohort[k]
            for k in ("baseline", "census", "source_queue", "identity_hold", "previous_checkpoint")
        },
        "sources": sources,
        "reused_references": reused,
        "deposition_entities": entities,
        "protein_references": proteins,
        "ligand_context": ligand,
        "producer_context": producer_context(producer),
        "chemical_components": components,
        "baseline_graph": baseline_graph,
        "chemical_disposition": {
            "decision": "HOLD_EXACT_STRUCTURE_CLAIM_TRANSFER",
            "new_evidence": "DEPOSITED_LIGAND_INCLUDES_HYDROXYLATED_COMPONENT_A1L3I",
            "complete_ligand_graph_reconstructed": False,
            "replacement_structure_assigned": False,
            "component_metadata_proves_polymer_connectivity": False,
            "source_owned_identity_conflict_resolved": False,
        },
        "limitations": [
            "Deposition metadata is not a resistant organism, allele or genotype-phenotype experiment.",
            "The three polymer entities are two protein components and a peptide ligand, not three genes.",
            "The ligand producer species is distinct from the protein reference strain "
            "and is not a resistant host.",
            "Free-component formulas and hydroxyls do not determine condensation, "
            "ring closure or final drug identity.",
            "Null BIRD and UniProt fields are scoped deposition observations, not global identifier absence.",
            "The earlier restricted primary article and its holds are unchanged; "
            "no material was republished.",
        ],
        "limits": {
            "new_scientific_http_attempts": 7,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "biological_changes": 0,
            "new_experimental_allele_or_genome_assignments": 0,
            "whole_record_primary_signoffs": 0,
            "source_adoptions": 0,
            "github_mutations": 0,
            "sequences_variants_constructs_protocols_or_numeric_AST_exported": False,
        },
        "attribution": [
            {"source": "RCSB PDB / wwPDB", "license": "CC0", "url": "https://www.rcsb.org/structure/9IVC"},
            {
                "source": "UniProt Consortium",
                "license": "CC BY 4.0",
                "release": "2026_03",
                "url": "https://www.uniprot.org/help/license",
            },
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != body:
            raise SystemExit("dated aureobasidin structure checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(body)
    print(
        json.dumps(
            {
                "proteins": len(result["protein_references"]),
                "ligand_entities": 1,
                "reviewed_chemical_components": len(result["chemical_components"]),
                "identity_hold": result["chemical_disposition"]["decision"],
            }
        )
    )


if __name__ == "__main__":
    main()

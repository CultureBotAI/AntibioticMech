"""Replay reference identifiers without assigning a resistance allele or isolate."""

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_card_structure_links as structures
import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from resistance_checkpoint_records import checkpoint_path
from seed_from_sources import is_card_sourced

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-triclosan")
OUTPUT = Path("research/2026-10-14-triclosan-context.json")
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_embl,lit_pubmed_id,sequence_version,version"
)
METADATA = (
    "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
    "query=EXT_ID%3A17720796%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=10"
)
PDF = "https://europepmc.org/articles/PMC2168734?pdf=render"
TAXONOMY = Path("reports/resistance-grounding-2026-10-09-topoisomerase-followup")
TAXONOMY_SHA = "121c67b8a2fc8d5b44efc1d39c71a8f7d54031109fe54b352bb63202c873afe4"
PAO1_NAME = (
    "Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / "
    "JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)"
)
LOCI = {
    "PA0156": ("tria-reference-canary", "Q9I6X6", 120, "AAG03546.1"),
    "PA0157": ("pa0157-reference", "Q9I6X5", 117, "AAG03547.1"),
    "PA0158": ("pa0158-reference", "Q9I6X4", 108, "AAG03548.1"),
}
SHA = {
    "triabc-metadata": "c18d4d55413edfaf2681915b3b91448edb7860dfd9c618879c8a07f53f3d5d77",
    "triabc-primary-pdf": "3e998e7538f1849ead481a3fd0e1c358526eb1942d7266e1f06d9a236f877389",
    "tria-reference-canary": "f5056e4e1c603aacea48daa6397bcb703e6fb83707a60150be38037f98ed45c0",
    "pa0157-reference": "8d0770214528c3ed91223a9ed5da65d9cf68fed07c1fb77ad2bb69472e265c3e",
    "pa0158-reference": "64d0e58f7c6097e14075cd78e595e09a5ed224b88934eeae82a93056044234b2",
    "opmh-reference": "69d10cecaf6e0bede8120904f330b5b76fbd2deaf574f1a23111e0266d239c92",
    "opmh-species-reference": "5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84",
    "pdb-6vej": "564effc3ba5167d2611c3299d324dbb9dd78a08d0d07ef1de55c351037c8170b",
}


def planned_native(root, directory, key, url, statuses=(200,)):
    source = native_context.native(root, directory, key, url, statuses)
    plan_path = directory / (key + "-plan.json")
    plan = json.loads(plan_path.read_bytes())
    attempt = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
    if (
        source["body"]["sha256"] != SHA[key] or plan.get("url") != url
        or plan.get("redirects_followed") is not False
        or type(plan.get("max_bytes")) is not int
        or not 0 < reference.check_pin(root, source["body"]).stat().st_size <= plan["max_bytes"]
        or datetime.fromisoformat(attempt["started_at"]) > datetime.fromisoformat(source["retrieved_at"])
    ):
        raise ValueError("reviewed payload, request plan or chronology changed")
    return {**source, "plan": reference.pin(root, plan_path)}


def project_locus(entry, taxonomy, locus):
    if locus not in LOCI or {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned locus or unexpected biological payload")
    _, accession, version, embl_protein = LOCI[locus]
    blocks = entry.get("genes", [])
    species = [t for t in taxonomy.get("lineage", []) if t.get("rank") == "species"]
    if (
        entry.get("primaryAccession") != accession
        or entry.get("entryType") != "UniProtKB unreviewed (TrEMBL)"
        or entry.get("entryAudit") != {"entryVersion": version, "sequenceVersion": 1}
        or any(type(v) is not int for v in entry.get("entryAudit", {}).values())
        or len(blocks) != 1 or "geneName" in blocks[0] or blocks[0].get("synonyms")
        or blocks[0].get("orfNames")
        or [v["value"] for v in blocks[0].get("orderedLocusNames", [])] != [locus]
        or taxonomy.get("taxonId") != 208964 or taxonomy.get("rank") != "strain"
        or taxonomy.get("active") is not True or taxonomy.get("scientificName") != PAO1_NAME
        or entry.get("organism", {}).get("taxonId") != 208964
        or entry["organism"].get("scientificName") != taxonomy.get("scientificName")
        or len(species) != 1 or species[0].get("taxonId") != 287
        or species[0].get("scientificName") != "Pseudomonas aeruginosa"
    ):
        raise ValueError("reference accession, locus, version or taxonomy changed")
    names = entry.get("proteinDescription", {}).get("submissionNames", [])
    links = [x for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "EMBL"]
    if (
        len(names) != 1 or not names[0].get("fullName", {}).get("value")
        or len(links) != 1 or links[0].get("id") != "AE004091"
        or [p.get("value") for p in links[0].get("properties", []) if p.get("key") == "ProteinId"]
        != [embl_protein]
    ):
        raise ValueError("reference protein name or EMBL cross-reference changed")
    # Do not copy referencePositions, which can contain experimental annotations.
    bibliography, structure_citation = [], False
    for row in entry.get("references", []):
        pairs = sorted((x["database"], x["id"]) for x in row.get("citation", {}).get(
            "citationCrossReferences", []) if x["database"] in {"PubMed", "DOI"})
        bibliography.append([{"database": db, "id": value} for db, value in pairs])
        if ("PubMed", "32966762") in pairs and any(
            e.get("source") == "PDB" and e.get("id") == "6VEJ" for e in row.get("evidences", [])
        ):
            structure_citation = True
    if sorted(bibliography, key=str) != sorted([
        [{"database": "DOI", "id": "10.1038/35023079"}, {"database": "PubMed", "id": "10984043"}],
        [{"database": "DOI", "id": "10.1016/j.str.2020.09.001"}, {"database": "PubMed", "id": "32966762"}],
    ], key=str) or not structure_citation:
        raise ValueError("reference bibliography or explicit structure evidence changed")
    return {
        "systematic_locus": locus, "protein_accession": "UniProtKB:" + accession,
        "entry_type": entry["entryType"], "entry_version": version, "sequence_version": 1,
        "submitted_protein_name": names[0]["fullName"]["value"],
        "reference_taxon_id": "NCBITaxon:208964", "reference_taxon_rank": "strain",
        "reference_organism_name": taxonomy["scientificName"], "species_taxon_id": "NCBITaxon:287",
        "embl_reference": {"nucleotide_accession": "AE004091", "protein_id": embl_protein},
        "bibliography": bibliography, "explicit_structure_reference": "PDB:6VEJ",
        "paper_gene_symbol_is_entry_gene_name": False, "original_resistance_pmid_cited": False,
        "reference_role": "UNREVIEWED_LOCUS_REFERENCE_NOT_EXPERIMENTAL_SUBJECT",
        "experimental_allele_assignment": None, "experimental_genome_assignment": None,
        "experimental_subject_taxon_assignment": False, "new_resistance_assertion": False,
    }


def project_structure(payload):
    entries = payload.get("data", {}).get("entries", [])
    if payload.get("errors") or len(entries) != 1 or not entries[0] or entries[0].get("rcsb_id") != "6VEJ":
        raise ValueError("structure query error or entry mismatch")
    entry = entries[0]
    entities = structures.entity_references(entry)
    if (
        entry.get("rcsb_primary_citation") != {
            "pdbx_database_id_PubMed": 32966762, "pdbx_database_id_DOI": "10.1016/j.str.2020.09.001",
            "year": 2021,
        }
        or entry.get("rcsb_accession_info") != {
            "major_revision": 1, "minor_revision": 3, "revision_date": "2024-10-23T00:00:00Z",
        }
        or {e["entity_id"]: e["reference_accessions"] for e in entities} != {
            "6VEJ_1": ["UniProtKB:Q9I6X4"], "6VEJ_2": ["UniProtKB:Q9I6X5", "UniProtKB:Q9I6X6"],
        }
        or any(e["other_reference_identifiers"] or not e["source_organisms"] or any(
            o != {"ncbi_taxonomy_id": 287, "scientific_name": "Pseudomonas aeruginosa"}
            for o in e["source_organisms"]) for e in entities)
    ):
        raise ValueError("structure entity membership, source taxonomy, revision or citation changed")
    return {
        "pdb_id": "6VEJ", "revision": entry["rcsb_accession_info"],
        "citation": entry["rcsb_primary_citation"], "entities": entities,
        "one_entity_can_reference_multiple_proteins": True, "single_representative_selected": False,
        "entity_architecture_or_experimental_allele_inferred": False,
        "primary_results_reviewed": False, "original_2007_subject_resolved": False,
    }


def build(root, directory):
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for item in [cohort[k] for k in ("census", "protected", "source_queue")] + cohort["prior"]:
        reference.check_pin(root, item)
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939 or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus membership or checkpoint bytes changed")
    record = load_record(reference.check_pin(root, cohort["record"]))
    claims = record.get("resistance_mechanisms", [])
    if (
        record["identifier"] != "CHEBI:164200"
        or record["chemical_structure"]["standard_inchi_key"] != "XEFQLINVKFYRCS-UHFFFAOYSA-N"
        or len(claims) != 10 or not all(is_card_sourced(c) for c in claims)
        or [(i, c["aro_id"], c["label"]) for i, c in enumerate(claims)]
        != [(c["index"], c["aro_id"], c["label"]) for c in cohort["source_owned_assertions"]]
    ):
        raise ValueError("compound identity or source-owned claims changed")
    canary_path = directory / "reference-canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    for key in (
        "canary", "receipt", "held_primary_receipt",
        "reference_taxonomy_reused", "reference_taxonomy_receipt",
    ):
        reference.check_pin(root, canary[key])
    if (
        canary["approved_for_remaining_reference_metadata_queries"] is not True
        or canary["approved_for_biological_curation_or_experimental_assignments"] is not False
    ):
        raise ValueError("reference canary authorization changed")
    sources = {"metadata": planned_native(root, directory, "triabc-metadata", METADATA),
               "held_pdf": planned_native(root, directory, "triabc-primary-pdf", PDF, (403,))}
    metadata = json.loads(reference.check_pin(root, sources["metadata"]["body"]).read_bytes())
    papers = metadata.get("resultList", {}).get("result", [])
    if metadata.get("hitCount") != 1 or len(papers) != 1:
        raise ValueError("paper metadata not unique")
    paper = papers[0]
    if (
        (paper.get("id"), paper.get("source"), paper.get("pmid"), paper.get("pmcid"), paper.get("doi"))
        != ("17720796", "MED", "17720796", "PMC2168734", "10.1128/jb.00850-07")
        or not all(locus in paper.get("abstractText", "") for locus in LOCI)
        or not any(x.get("url") == PDF and x.get("documentStyle") == "pdf"
                   for x in paper.get("fullTextUrlList", {}).get("fullTextUrl", []))
    ):
        raise ValueError("paper identity, abstract locus set or native PDF link changed")
    taxonomy, sources["taxonomy_reused"] = reference.read_response(
        root, root / TAXONOMY, "reference-tax-208964", "/taxonomy/208964")
    if (
        sources["taxonomy_reused"]["cache"]["sha256"] != TAXONOMY_SHA
        or sources["taxonomy_reused"]["release"] != "2026_03"
    ):
        raise ValueError("reused reference taxonomy changed")
    queries = {row[0]: "gene_exact:" + locus for locus, row in LOCI.items()}
    queries.update({"opmh-reference": "gene_exact:opmH AND organism_id:208964",
                    "opmh-species-reference": "gene_exact:opmH AND taxonomy_id:287"})
    proteins, searches = {}, {}
    for key, query in queries.items():
        payload, source = reference.read_response(root, directory, key, "/uniprotkb/search", {
            "query": [query], "format": ["json"], "size": ["100"], "sort": ["accession asc"],
            "fields": [FIELDS],
        })
        sources[key] = planned_native(root, directory, key, source["url"])
        if source["release"] != "2026_03":
            raise ValueError("reference release changed")
        entries = payload["results"]
        if key.startswith("opmh"):
            if entries:
                raise ValueError("historical OpmH query is not empty")
        else:
            if len(entries) != 1:
                raise ValueError("systematic locus reference is not unique")
            locus = next(locus for locus, row in LOCI.items() if row[0] == key)
            proteins[locus] = project_locus(entries[0], taxonomy, locus)
        searches[key] = {"query": query, "result_count": len(entries), "release": source["release"],
                         "complete_for_query": True, "zero_result_establishes_absence": False,
                         "automatic_suggestions_followed": False}
    url = "https://data.rcsb.org/graphql?" + urlencode({"query": structures.pdb_query("6VEJ")})
    sources["structure"] = planned_native(root, directory, "pdb-6vej", url)
    structure = project_structure(
        json.loads(reference.check_pin(root, sources["structure"]["body"]).read_bytes()))
    prior = json.loads(reference.check_pin(root, cohort["prior"][2]).read_bytes())["queries"]["17720796"]
    if prior["result_count"] != 0 or prior["complete_for_query"] is not True or len(prior["pages"]) != 1:
        raise ValueError("prior literature query scope changed")
    for field in ("cache", "receipt"):
        reference.check_pin(root, prior["pages"][0][field])
    return {
        "date": "2026-10-14", "cohort": reference.pin(root, directory / "cohort.json"),
        "canary": reference.pin(root, canary_path), "record": cohort["record"],
        "source_owned_assertions": cohort["source_owned_assertions"], "sources": sources,
        "primary": {"pmid": "17720796", "pmcid": "PMC2168734", "doi": paper["doi"],
                    "title": paper["title"], "metadata_and_abstract_reviewed": True,
                    "collective_locus_set": sorted(LOCI), "individual_TriABC_symbol_mapping_inferred": False,
                    "full_text_status": "HTTP_403_HELD_NO_RETRY_OR_ALTERNATE_ROUTE",
                    "metadata_open_access_flag": paper["isOpenAccess"], "reuse_license_inferred": False,
                    "primary_results_figures_or_supplements_reviewed": False,
                    "new_functional_resistance_curation_supported": False},
        "references": proteins, "queries": searches, "structure": structure,
        "prior_literature_query_reused": prior,
        "summary": {"corpus_records_in_scope": 2939, "records_in_this_checkpoint": 1,
                    "source_assertions_preserved": 10, "source_terms_investigated": 1,
                    "unreviewed_locus_references": 3, "empty_opmh_queries": 2,
                    "pdb_entities": 2, "new_native_requests": 8, "new_primary_access_holds": 1,
                    "biological_records_changed": 0, "curated_resistance_assertions": 0,
                    "whole_record_primary_signoffs": 0},
        "limits": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "new_taxonomy_requests": 0,
                   "github_mutations": 0, "source_adoptions": 0, "held_sources_retried": False,
                   "exact_alleles_assigned": 0, "experimental_genomes_assigned": 0,
                   "sequences_variants_protocols_or_numeric_AST_exported": False,
                   "whole_record_primary_review": "OPEN", "independent_scientific_signoff": False},
        "attribution": {"reference": "UniProt Consortium, release 2026_03, CC BY 4.0",
                        "structure": "RCSB Protein Data Bank, 6VEJ metadata, CC0",
                        "literature": "Mima et al., J Bacteriol (2007); Europe PMC metadata/abstract only"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root, root / CACHE)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to overwrite a different checkpoint")
    args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

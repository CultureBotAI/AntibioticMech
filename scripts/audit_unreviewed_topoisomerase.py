"""Reproduce unreviewed identifier evidence without assigning resistance alleles."""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import audit_topoisomerase_references as reviewed

FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_proteomes,lit_pubmed_id,sequence_version,version"
)
DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-09-topoisomerase-unreviewed")
DEFAULT_OUTPUT = Path("research/2026-10-09-topoisomerase-unreviewed-followup.json")
SCOPE = "UNREVIEWED_IDENTIFIER_CANDIDATES_NOT_RESISTANCE_ALLELES_OR_EXPERIMENTAL_GENOMES"


def project_proteome(body):
    assembly = body.get("genomeAssembly", {})
    assembly_id = assembly.get("assemblyId")
    if assembly_id is not None and not re.fullmatch(r"GC[AF]_\d+\.\d+", assembly_id):
        raise ValueError("unreviewed assembly identifier format")
    return {
        "proteome_id": body["id"],
        "proteome_type": body["proteomeType"],
        "reference_taxon_id": f"NCBITaxon:{body['taxonomy']['taxonId']}",
        "reference_organism_name": body["taxonomy"]["scientificName"],
        "modified": body.get("modified"),
        "reference_assembly_id": assembly_id,
        "assembly_source": assembly.get("source"),
        "component_names": sorted({row["name"] for row in body.get("components", [])}),
        "experimental_genome_assignment": False,
        "scope": "PROTEOME_REFERENCE_CONTEXT_NOT_TESTED_RESISTANT_ISOLATE",
    }


def proteome_link(entry, cross_reference, proteome):
    if cross_reference["database"] != "Proteomes" or cross_reference["id"] != proteome["proteome_id"]:
        raise ValueError("proteome cross-reference mismatch")
    components = sorted(
        {row["value"] for row in cross_reference.get("properties", []) if row["key"] == "Component"}
    )
    same_taxon = f"NCBITaxon:{entry['organism']['taxonId']}" == proteome["reference_taxon_id"]
    components_match = bool(components) and set(components) <= set(proteome["component_names"])
    return {
        "proteome_id": proteome["proteome_id"],
        "reported_components": components,
        "reference_taxon_matches": same_taxon,
        "reported_components_match": components_match,
        "status": "REFERENCE_CONTEXT_VERIFIED"
        if same_taxon and components_match
        else "UNRESOLVED_METADATA_JOIN",
        "reference_assembly_id": proteome["reference_assembly_id"]
        if same_taxon and components_match
        else None,
        "experimental_genome_assignment": False,
    }


def analyze(root, directory):
    cohort_path, metadata_path = directory / "cohort.json", directory / "metadata-plan.json"
    cohort, metadata = json.loads(cohort_path.read_bytes()), json.loads(metadata_path.read_bytes())
    reviewed.check_pin(root, metadata["cohort"])
    prior_path = reviewed.check_pin(root, cohort["prior_dossier"])
    prior = json.loads(prior_path.read_bytes())
    reviewed.check_pin(root, cohort["prior_checkpoint"])
    reviewed.check_pin(root, cohort["current_census"])
    prior_cache = (root / prior["inputs"]["verified_plan"]["path"]).parent
    if reviewed.analyze(root, prior_cache) != prior:
        raise ValueError("the reviewed checkpoint does not reproduce with the current corpus")
    expected = {key for key, row in prior["queries"].items() if not row["accessions"]}
    if (
        {row["prior_query"] for row in cohort["queries"].values()} != expected
        or len(cohort["queries"]) != len(expected)
        or set(metadata["queries"]) != set(cohort["queries"])
    ):
        raise ValueError("unreviewed plan omits or duplicates a reviewed-no-hit query")
    taxonomy, requests, proteomes = {}, {}, {}
    for taxid in metadata["reference_taxa"]:
        body, request = reviewed.read_response(
            root, directory, f"reference-tax-{taxid}", f"/taxonomy/{taxid}"
        )
        taxonomy[taxid], requests[f"reference-tax-{taxid}"] = body, request
    for proteome_id in metadata["proteomes"]:
        body, request = reviewed.read_response(
            root, directory, f"proteome-{proteome_id}", f"/proteomes/{proteome_id}"
        )
        if body["id"] != proteome_id:
            raise ValueError("proteome response identifier mismatch")
        proteomes[proteome_id] = project_proteome(body)
        requests[f"proteome-{proteome_id}"] = request
    proteins, queries, terms = {}, {}, {}
    shared_symbols = defaultdict(set)
    for key, planned in cohort["queries"].items():
        prior_key = planned["prior_query"]
        old_query = prior["queries"][prior_key]["query"]
        query = old_query.replace("reviewed:true", "reviewed:false")
        if old_query.count("reviewed:true") != 1 or planned["query"] != query:
            raise ValueError("unreviewed query changed more than review status")
        expected_terms = sorted(
            tid for tid, term in prior["terms"].items() if term["reference_query"] == prior_key
        )
        if planned["source_terms"] != expected_terms:
            raise ValueError("source term/query relationship changed")
        body, request = reviewed.read_response(
            root,
            directory,
            key,
            "/uniprotkb/search",
            {"query": [query], "format": ["json"], "size": ["500"], "fields": [FIELDS]},
        )
        if any(request[field] != metadata["queries"][key][field] for field in ("cache", "receipt")):
            raise ValueError("unreviewed response changed after metadata planning")
        accessions = [entry["primaryAccession"] for entry in body["results"]]
        if len(accessions) != len(set(accessions)):
            raise ValueError("duplicate accession in response")
        queries[key] = {
            **request,
            "query": query,
            "prior_reviewed_query": prior_key,
            "accessions": accessions,
            "status_label": "UNREVIEWED_CANDIDATES" if accessions else "NO_UNREVIEWED_HIT_NOT_GENE_ABSENCE",
            "zero_hit_is_absence": False,
        }
        for tid in expected_terms:
            original = prior["terms"][tid]
            gene = original["source_gene_symbol"]
            species_id = int(original["source_species_taxon_id"].split(":")[1])
            terms[tid] = {
                "source_organism_name": original["source_organism_name"],
                "source_species_taxon_id": original["source_species_taxon_id"],
                "source_gene_symbol": gene,
                "source_label_sha256": original["source_label_sha256"],
                "record_ids": original["record_ids"],
                "source_assertion_memberships": original["source_assertion_memberships"],
                "reviewed_candidates": [],
                "unreviewed_candidates": accessions,
                "query": key,
                "exact_allele_assignment": False,
                "experimental_subject_assignment": False,
                "primary_review_status": "OPEN",
            }
            for entry in body["results"]:
                accession = entry["primaryAccession"]
                row = reviewed.project_reference(
                    entry, gene, species_id, taxonomy[entry["organism"]["taxonId"]], reviewed=False
                )
                links = [
                    proteome_link(entry, xref, proteomes[xref["id"]])
                    for xref in entry.get("uniProtKBCrossReferences", [])
                    if xref["database"] == "Proteomes"
                ]
                row["proteome_links"] = links
                if accession in proteins and proteins[accession] != row:
                    raise ValueError("conflicting duplicate protein metadata")
                proteins[accession] = row
                for link in links:
                    shared_symbols[(gene, link["proteome_id"])].add(accession)
    if len(proteins) != metadata["protein_count"] or set(proteins) & set(prior["reference_proteins"]):
        raise ValueError("unreviewed protein count or review-state partition changed")
    if {int(row["reference_taxon_id"].split(":")[1]) for row in proteins.values()} != set(taxonomy) or {
        link["proteome_id"] for row in proteins.values() for link in row["proteome_links"]
    } != set(proteomes):
        raise ValueError("metadata plan has missing or extraneous subjects")
    releases = {row["release"] for row in list(queries.values()) + list(requests.values())}
    if releases != {prior["summary"]["uniprot_release"]}:
        raise ValueError("mixed UniProt releases")
    multi = [
        {
            "gene_symbol": gene,
            "proteome_id": proteome_id,
            "accessions": sorted(accessions),
            "status": "MULTIPLE_ENTRIES_RETAINED_NOT_A_UNIQUE_LOCUS_ASSIGNMENT",
        }
        for (gene, proteome_id), accessions in sorted(shared_symbols.items())
        if len(accessions) > 1
    ]
    memberships = [row for row in prior["memberships"] if row["aro_id"] in terms]
    return {
        "date": "2026-10-09",
        "scope": SCOPE,
        "inputs": {
            "cohort": reviewed.pin(root, cohort_path),
            "metadata_plan": reviewed.pin(root, metadata_path),
            "prior_dossier": cohort["prior_dossier"],
            "prior_checkpoint": cohort["prior_checkpoint"],
            "current_census": cohort["current_census"],
        },
        "terms": terms,
        "memberships": memberships,
        "queries": queries,
        "unreviewed_proteins": proteins,
        "reference_proteomes": proteomes,
        "metadata_requests": requests,
        "shared_symbol_in_same_proteome": multi,
        "summary": {
            "corpus_records": prior["summary"]["corpus_records"],
            "selected_terms": len(terms),
            "source_records": len({row["record_id"] for row in memberships}),
            "source_assertion_memberships": len(memberships),
            "completed_unreviewed_queries": len(queries),
            "queries_with_candidates": sum(bool(row["accessions"]) for row in queries.values()),
            "unreviewed_proteins": len(proteins),
            "source_flagged_fragments": sum(
                row["protein_description_flag"] == "Fragment" for row in proteins.values()
            ),
            "reference_taxa": len(taxonomy),
            "reference_proteomes": len(proteomes),
            "proteins_with_proteome_links": sum(bool(row["proteome_links"]) for row in proteins.values()),
            "verified_reference_assembly_links": sum(
                link["reference_assembly_id"] is not None
                for row in proteins.values()
                for link in row["proteome_links"]
            ),
            "unresolved_proteome_joins": sum(
                link["status"] != "REFERENCE_CONTEXT_VERIFIED"
                for row in proteins.values()
                for link in row["proteome_links"]
            ),
            "reference_assemblies": len(
                {
                    row["reference_assembly_id"]
                    for row in proteomes.values()
                    if row["reference_assembly_id"] is not None
                }
            ),
            "multiple_entry_same_symbol_proteome_groups": len(multi),
            "combined_topoisomerase_terms_with_candidates": prior["summary"]["terms_with_reviewed_candidates"]
            + sum(bool(row["unreviewed_candidates"]) for row in terms.values()),
            "combined_topoisomerase_reference_candidates": len(prior["reference_proteins"]) + len(proteins),
            "uniprot_release": next(iter(releases)),
            "biological_records_changed": 0,
            "exact_allele_assignments": 0,
            "experimental_genome_assignments": 0,
            "whole_record_reviews_completed": 0,
        },
        "documentation": [
            {
                "url": "https://www.uniprot.org/help/proteome",
                "interpretation": "Proteome membership and manual review status are distinct; "
                "one taxonomy identifier can have multiple proteomes.",
            }
        ],
        "attribution": [
            "UniProt Consortium, UniProtKB and UniProt Proteomes (CC BY 4.0)",
            "CARD curation team, Antibiotic Resistance Ontology (CC BY 4.0)",
        ],
        "limits": [
            "This audit retains unreviewed annotations as candidates; "
            "it does not establish experimental gene or allele identity.",
            "Fragment flags are preserved; absence of a fragment flag does not prove completeness.",
            "Multiple names and loci remain separate; no representative resistant allele is selected.",
            "Reference assembly identifiers describe database proteome context, "
            "not a tested resistant isolate.",
            "No primary resistance results were reviewed and no new phenotype is inferred in this pass.",
            "The four prior source terms without species grounding remain unresolved.",
            "No sequences, variants, constructs, reference positions, "
            "coordinates or numerical AST are exported.",
        ],
        "whole_corpus_primary_review": "OPEN",
        "ncbi_endpoint_requests": 0,
        "source_adoptions": 0,
        "github_mutations": 0,
        "outreach": 0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = analyze(root, root / args.cache_dir)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check:
        if args.output.read_bytes() != payload:
            raise ValueError("unreviewed dossier does not reproduce")
    else:
        if args.output.exists() and args.output.read_bytes() != payload:
            raise ValueError("refusing to replace a changed checkpoint")
        args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Reproduce reference-only grounding without promoting resistance alleles.

Reads pinned local UniProt responses; never performs network requests or writes
biological records. The selected source labels are discovery context only.
"""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_card_named_taxa as names

from antibioticmech.activity_collections import load_record

FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_embl,xref_refseq,lit_pubmed_id,sequence_version,version"
)
PATTERN = re.compile(r"^(.*?) (gyrA|gyrB|parC|parE)\b")
SCOPE = "REVIEWED_REFERENCE_PROTEINS_NOT_EXPERIMENTAL_RESISTANCE_ALLELES"
DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-09-topoisomerase-followup")
DEFAULT_OUTPUT = Path("research/2026-10-09-topoisomerase-reference-followup.json")


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def pin(root, path):
    return {"path": str(path.relative_to(root)), "sha256": digest(path)}


def check_pin(root, item):
    path = root / item["path"]
    if digest(path) != item["sha256"]:
        raise ValueError(f"input checksum changed: {item['path']}")
    return path


def read_response(root, directory, key, endpoint, parameters=None):
    path, receipt_path = directory / f"{key}-response.bin", directory / f"{key}-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    parsed = urlparse(receipt["url"])
    if (
        parsed.scheme != "https"
        or parsed.netloc != "rest.uniprot.org"
        or parsed.path != endpoint
        or parsed.fragment
        or parse_qs(parsed.query, keep_blank_values=True) != (parameters or {})
    ):
        raise ValueError("response request identity mismatch")
    if receipt["status"] != 200 or receipt["sha256"] != digest(path):
        raise ValueError("response status or checksum mismatch")
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    release = headers.get("x-uniprot-release")
    if not release or headers.get("link"):
        raise ValueError("release missing or response paginated")
    body = json.loads(path.read_bytes())
    if endpoint.endswith("/search") and (
        len(body["results"]) != int(headers["x-total-results"]) or len(body["results"]) > 500
    ):
        raise ValueError("incomplete search response")
    return body, {
        "cache": pin(root, path),
        "receipt": pin(root, receipt_path),
        "url": receipt["url"],
        "retrieved_at": receipt["retrieved_at"],
        "status": receipt["status"],
        "release": release,
    }


def project_reference(entry, gene, species_id, taxonomy, *, reviewed=True):
    """Use an allowlist; reference positions may contain operational annotations."""
    if type(reviewed) is not bool:
        raise ValueError("review status must be explicit")
    expected_type = "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)"
    if entry["entryType"] != expected_type or "sequence" in entry:
        raise ValueError("expected a sequence-free reference with the requested review status")
    audit = entry["entryAudit"]
    if any(type(audit.get(key)) is not int or audit[key] < 1 for key in ("entryVersion", "sequenceVersion")):
        raise ValueError("reference entry versions missing")
    gene_names, loci, matching_blocks = set(), set(), 0
    for block in entry.get("genes", []):
        local = {item["value"] for item in block.get("synonyms", [])}
        if "geneName" in block:
            local.add(block["geneName"]["value"])
        gene_names.update(local)
        loci.update(item["value"] for item in block.get("orderedLocusNames", []))
        matching_blocks += gene.lower() in {value.lower() for value in local}
    if matching_blocks != 1:
        raise ValueError("gene name is absent or ambiguous; locus names are not aliases")
    reference_id = entry["organism"]["taxonId"]
    if (
        type(reference_id) is not int
        or reference_id < 1
        or taxonomy["taxonId"] != reference_id
        or taxonomy.get("active") is not True
    ):
        raise ValueError("reference organism does not match active taxonomy")
    species = [row for row in taxonomy.get("lineage", []) if row["rank"] == "species"]
    if taxonomy["rank"] == "species":
        species.append(taxonomy)
    if len(species) != 1 or species[0]["taxonId"] != species_id:
        raise ValueError("reference species lineage does not match the source-name TaxID")
    citations = []
    for reference in entry.get("references", []):
        citation = reference.get("citation", {})
        identifiers = sorted(
            {
                (row["database"], row["id"])
                for row in citation.get("citationCrossReferences", [])
                if row["database"] in {"PubMed", "DOI"}
            }
        )
        if identifiers:
            citations.append(
                {
                    "identifiers": [{"database": db, "id": value} for db, value in identifiers],
                    "publication_date": citation.get("publicationDate"),
                    "primary_results_reviewed": False,
                }
            )
    result = {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_version": audit["entryVersion"],
        "sequence_version": audit["sequenceVersion"],
        "entry_type": entry["entryType"],
        "gene_names": sorted(gene_names),
        "ordered_locus_names": sorted(loci),
        "reference_organism_name": entry["organism"]["scientificName"],
        "reference_taxon_id": f"NCBITaxon:{reference_id}",
        "reference_taxon_rank": taxonomy["rank"],
        "reference_taxon_scientific_name": taxonomy["scientificName"],
        "source_species_taxon_id": f"NCBITaxon:{species_id}",
        "species_lineage_verified": True,
        "bibliography": citations,
        "exact_resistance_allele": False,
        "experimental_subject_assignment": False,
    }
    description = entry["proteinDescription"]
    if reviewed:
        result["protein_name"] = description["recommendedName"]["fullName"]["value"]
    else:
        protein_names = []
        for kind in ("recommendedName", "submissionNames", "alternativeNames"):
            blocks = [description[kind]] if kind == "recommendedName" and kind in description else []
            if kind != "recommendedName":
                blocks = description.get(kind, [])
            protein_names.extend({"kind": kind, "value": block["fullName"]["value"]} for block in blocks)
        if not protein_names:
            raise ValueError("unreviewed protein names missing")
        result.update(
            {
                "protein_names": protein_names,
                "protein_description_flag": description.get("flag"),
                "gene_orf_names": sorted(
                    {
                        value["value"]
                        for block in entry.get("genes", [])
                        for value in block.get("orfNames", [])
                    }
                ),
                "annotation_status": "UNREVIEWED_EXPERIMENTAL_IDENTITY_NOT_ESTABLISHED_BY_THIS_AUDIT",
                "unflagged_means_complete": False,
            }
        )
    return result


def source_taxonomy(root, directory, cohort):
    result = {}
    for name in sorted({row["source_organism_name"] for row in cohort["terms"].values()}):
        if name == cohort["broad_name_not_forced_to_species"]:
            result[name] = {"status": "BROAD_SOURCE_NAME_UNRESOLVED", "named_organism_taxon_id": None}
            continue
        if name in cohort["reused_taxonomy"]:
            old = cohort["reused_taxonomy"][name]
            path = check_pin(root, old["cache"])
        else:
            key = hashlib.sha256(name.encode()).hexdigest()[:16]
            path = directory / f"taxonomy-{key}.json"
        resolved = names.resolve_name(name, json.loads(path.read_bytes()))
        if name in cohort["reused_taxonomy"] and resolved != {k: v for k, v in old.items() if k != "cache"}:
            raise ValueError("reused source taxonomy does not reproduce")
        result[name] = {
            "status": resolved["status"],
            "named_organism_taxon_id": resolved["named_organism_taxon_id"],
            "exact_candidates": [r for r in resolved["candidates"] if r["exact_name_fields"]],
            "release": resolved["release"],
            "request": resolved["request"],
            "cache": pin(root, path),
        }
    return result


def analyze(root, directory):
    verified_path = directory / "verified-plan.json"
    verified = json.loads(verified_path.read_bytes())
    cohort = json.loads(check_pin(root, verified["source_cohort"]).read_bytes())
    plan = json.loads(check_pin(root, verified["source_query_plan"]).read_bytes())
    prior = json.loads(check_pin(root, cohort["prior_reference_audit"]).read_bytes())
    check_pin(root, cohort["prior_named_taxa"])
    check_pin(root, verified["prior_checkpoint"])
    census_path = check_pin(root, verified["current_census"])
    selected = {
        tid: PATTERN.match(row["labels"][0])
        for tid, row in prior["determinants"].items()
        if not row["candidates"] and len(row["labels"]) == 1 and PATTERN.match(row["labels"][0])
    }
    if set(selected) != set(cohort["terms"]):
        raise ValueError("the full unlinked topoisomerase cohort changed")
    with census_path.open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len({r["path"] for r in census}) != len(census)
        or len({r["identifier"] for r in census}) != len(census)
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    ):
        raise ValueError("current census does not cover the corpus")
    selected_records = {row["path"]: row for row in verified["records"]}
    memberships, matching_paths = [], set()
    for row in census:
        path = check_pin(root, {"path": row["path"], "sha256": row["record_sha256"]})
        record = load_record(path)
        if record["identifier"] != row["identifier"]:
            raise ValueError("record identifier changed")
        for claim in record.get("resistance_mechanisms", []):
            tid = claim.get("aro_id")
            if tid in selected:
                if claim["label"] != cohort["terms"][tid]["source_label"]:
                    raise ValueError("live source label differs from reference cohort")
                memberships.append({"record_id": row["identifier"], "aro_id": tid})
                matching_paths.add(row["path"])
                if row["path"] not in selected_records:
                    raise ValueError("source membership omitted from the selected record plan")
                planned = selected_records[row["path"]]
                check_pin(root, planned)
                if (
                    planned["identifier"] != record["identifier"]
                    or planned["standard_inchi_key"] != record["chemical_structure"]["standard_inchi_key"]
                ):
                    raise ValueError("selected record identity changed")
    if memberships != verified["memberships"] or matching_paths != set(selected_records):
        raise ValueError("live claim memberships changed")
    taxonomy = source_taxonomy(root, directory, cohort)
    reference_taxa, reference_taxon_requests = {}, {}
    for taxid in verified["protein_taxa"]:
        body, request = read_response(root, directory, f"reference-tax-{taxid}", f"/taxonomy/{taxid}")
        reference_taxa[taxid], reference_taxon_requests[str(taxid)] = body, request
    terms, queries, proteins = {}, {}, {}
    for tid, match in sorted(selected.items()):
        name, gene = match.groups()
        source = cohort["terms"][tid]
        if source["source_organism_name"] != name or source["source_gene_symbol"] != gene:
            raise ValueError("source-label decomposition changed")
        taxid = taxonomy[name]["named_organism_taxon_id"]
        key, accessions = None, []
        if taxid is not None:
            species_id = int(taxid.split(":")[1])
            key = f"protein-{species_id}-{gene}"
            query = f"(gene_exact:{gene} AND taxonomy_id:{species_id} AND reviewed:true)"
            if (
                key not in plan["queries"]
                or plan["queries"][key]["query"] != query
                or tid not in plan["queries"][key]["terms"]
            ):
                raise ValueError("protein query no longer matches the source name and gene")
            if key not in queries:
                body, request = read_response(
                    root,
                    directory,
                    key,
                    "/uniprotkb/search",
                    {"query": [query], "format": ["json"], "size": ["500"], "fields": [FIELDS]},
                )
                if any(request[field] != verified["queries"][key][field] for field in ("cache", "receipt")):
                    raise ValueError("protein response differs from the frozen preparation")
                accessions = [entry["primaryAccession"] for entry in body["results"]]
                if len(accessions) != len(set(accessions)):
                    raise ValueError("duplicate reference accession in response")
                queries[key] = {
                    **request,
                    "query": query,
                    "accessions": accessions,
                    "status_label": "REVIEWED_REFERENCE_CANDIDATES"
                    if accessions
                    else "NO_REVIEWED_HIT_NOT_GENE_ABSENCE",
                    "zero_hit_is_absence": False,
                }
                for entry in body["results"]:
                    accession = entry["primaryAccession"]
                    projected = project_reference(
                        entry, gene, species_id, reference_taxa[entry["organism"]["taxonId"]]
                    )
                    if accession in proteins and proteins[accession] != projected:
                        raise ValueError("inconsistent duplicate reference metadata")
                    proteins[accession] = projected
            accessions = queries[key]["accessions"]
        else:
            if tid not in plan["unresolved_source_terms"]:
                raise ValueError("unresolved organism was incorrectly queried")
        terms[tid] = {
            "source_label_sha256": hashlib.sha256(source["source_label"].encode()).hexdigest(),
            "source_organism_name": name,
            "source_gene_symbol": gene,
            "source_species_taxon_id": taxid,
            "source_name_status": taxonomy[name]["status"],
            "reference_query": key,
            "reference_candidates": accessions,
            "experimental_assignment": False,
            "exact_allele_assignment": False,
            "record_ids": sorted({r["record_id"] for r in memberships if r["aro_id"] == tid}),
            "source_assertion_memberships": sum(r["aro_id"] == tid for r in memberships),
            "primary_review_status": "OPEN",
        }
    if set(queries) != set(plan["queries"]):
        raise ValueError("planned query was omitted")
    releases = {r["release"] for r in queries.values()} | {
        r["release"] for r in reference_taxon_requests.values()
    }
    releases.update(r["release"] for r in taxonomy.values() if "release" in r)
    if len(releases) != 1:
        raise ValueError("mixed UniProt releases")
    return {
        "date": "2026-10-09",
        "scope": SCOPE,
        "inputs": {
            "verified_plan": pin(root, verified_path),
            "current_census": verified["current_census"],
            "prior_checkpoint": verified["prior_checkpoint"],
            "source_cohort": verified["source_cohort"],
            "source_reference_audit": cohort["prior_reference_audit"],
            "source_named_taxa": cohort["prior_named_taxa"],
            "source_queue": pin(root, root / "curation/source_queue.tsv"),
        },
        "records": verified["records"],
        "memberships": memberships,
        "terms": terms,
        "source_name_taxonomy": taxonomy,
        "queries": queries,
        "reference_proteins": proteins,
        "reference_taxon_requests": reference_taxon_requests,
        "summary": {
            "corpus_records": len(census),
            "selected_source_terms": len(terms),
            "source_records": len(verified["records"]),
            "source_assertion_memberships": len(memberships),
            "source_organism_names": len(taxonomy),
            "source_name_status_counts": dict(Counter(r["status"] for r in taxonomy.values())),
            "terms_with_species_grounding": sum(
                r["source_species_taxon_id"] is not None for r in terms.values()
            ),
            "reviewed_protein_queries": len(queries),
            "queries_with_no_reviewed_hit": sum(not r["accessions"] for r in queries.values()),
            "terms_with_reviewed_candidates": sum(bool(r["reference_candidates"]) for r in terms.values()),
            "distinct_reference_proteins": len(proteins),
            "reference_taxa_verified": len(reference_taxa),
            "uniprot_release": next(iter(releases)),
            "biological_records_changed": 0,
            "experimental_subject_assignments": 0,
            "exact_allele_assignments": 0,
            "whole_record_reviews_completed": 0,
        },
        "attribution": [
            "CARD curation team, Antibiotic Resistance Ontology (CC BY 4.0)",
            "UniProt Consortium, UniProtKB and UniProt Taxonomy (CC BY 4.0)",
        ],
        "limits": [
            "Source ontology terms are not verified compound-specific experimental resistance evidence.",
            "Reviewed reference proteins are not exact resistance alleles or experimental subjects.",
            "Multiple reference entries are retained; "
            "none is chosen as a representative experimental allele.",
            "No-hit queries cover reviewed entries only; "
            "unreviewed entries and additional aliases remain unsearched.",
            "Broad source names and absent exact active-species matches remain unresolved.",
            "Bibliography is database-linked discovery evidence; "
            "primary results were not reviewed in this pass.",
            "No sequences, variants, reference positions, constructs, protocols, "
            "coordinates or numerical AST are exported.",
        ],
        "ncbi_endpoint_requests": 0,
        "source_adoptions": 0,
        "github_mutations": 0,
        "outreach": 0,
        "whole_corpus_primary_review": "OPEN",
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
            raise ValueError("reference dossier does not reproduce")
    else:
        if args.output.exists() and args.output.read_bytes() != payload:
            raise ValueError("refusing to replace an existing checkpoint with changed content")
        args.output.write_bytes(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

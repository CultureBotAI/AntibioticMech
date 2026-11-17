"""Replay source holds and reference-search scope without asserting resistance."""

import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_named_taxa as names
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-tropodithietic")
OUTPUT = Path("research/2026-10-14-tropodithietic-context.json")
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)
QUERIES = {
    "references-2016": ("lit_pubmed:26802120", "reference-plan.json"),
    "references-2011": ("lit_pubmed:21263047", "reference-plan.json"),
    "compound-references": ('"tropodithietic"', "compound-reference-plan.json"),
    "protein-name-references": ('protein_name:"tropodithietic"', "scoped-reference-plan.json"),
}
PRIMARY = {
    "primary": (
        "PMID:26802120",
        "request-plan.json",
        500,
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4760781/fullTextXML",
    ),
    "primary-2011": (
        "PMID:21263047",
        "distinct-primary-plan.json",
        403,
        "https://journals.asm.org/doi/10.1128/aac.01222-10",
    ),
}


def search_scope(payload, headers, *, partial=False):
    headers = {k.lower(): v for k, v in headers.items()}
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise ValueError("malformed reference search")
    rows = payload["results"]
    try:
        total = int(headers["x-total-results"])
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("missing search total") from error
    paginated = bool(headers.get("link"))
    if (
        headers.get("x-uniprot-release") != "2026_03"
        or total < len(rows)
        or len(rows) > 500
        or paginated != (total > len(rows))
        or (paginated and not partial)
    ):
        raise ValueError("search release or completeness changed")
    return {
        "returned_entries": len(rows),
        "reported_total": total,
        "complete": not paginated,
        "unretrieved_entries": total - len(rows),
        "release": headers["x-uniprot-release"],
        "empty_query_proves_protein_absence": False,
    }


def named_values(value):
    if isinstance(value, dict):
        if isinstance(value.get("value"), str):
            yield value["value"]
        for child in value.values():
            yield from named_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from named_values(child)


def bibliography_page(rows, taxonomy):
    if (
        type(taxonomy.get("taxonId")) is not int
        or taxonomy.get("taxonId") != 1844006
        or taxonomy.get("rank") != "species"
        or taxonomy.get("scientificName") != "Phaeobacter porticola"
        or taxonomy.get("active") is not True
    ):
        raise ValueError("reference species changed")
    seen, examples = set(), []
    for row in rows:
        accession = row["primaryAccession"]
        audit = row["entryAudit"]
        if (
            accession in seen
            or row["entryType"] != "UniProtKB unreviewed (TrEMBL)"
            or {"sequence", "features", "comments"}.intersection(row)
            or type(row["organism"]["taxonId"]) is not int
            or row["organism"]["taxonId"] != taxonomy["taxonId"]
            or row["organism"]["scientificName"] != taxonomy["scientificName"]
            or any(type(audit[k]) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
        ):
            raise ValueError("reference page identity or payload changed")
        seen.add(accession)
        if any(
            "tropodithietic" in value.lower()
            for block in (row["proteinDescription"], row.get("genes", []))
            for value in named_values(block)
        ):
            raise ValueError("compound appears in a returned protein or gene name")
        citations = [r["citation"] for r in row.get("references", [])]
        if (
            len(citations) != 1
            or citations[0].get("citationType") != "submission"
            or citations[0].get("title")
            != (
                "Phaeobacter portensis sp. nov., a tropodithietic acid producing bacterium "
                "isolated from a German harbor."
            )
        ):
            raise ValueError("genome-submission citation context changed")
        if accession in {"A0A1L3I6Q7", "A0A1L3I2Y5", "A0A1L3IBA0"}:
            examples.append(
                {
                    "accession": "UniProtKB:" + accession,
                    "entry_version": audit["entryVersion"],
                    "sequence_version": audit["sequenceVersion"],
                    "gene_names": [g["geneName"]["value"] for g in row.get("genes", []) if "geneName" in g],
                    "role": "REFERENCE_METADATA_EXAMPLE_NOT_RESISTANCE_DETERMINANT",
                }
            )
    if not rows:
        raise ValueError("reference page is empty")
    return {
        "entries_checked": len(rows),
        "unreviewed_entries": len(rows),
        "entries_with_compound_in_submission_title": len(rows),
        "entries_with_compound_in_returned_protein_or_gene_names": 0,
        "reference_taxon_id": "NCBITaxon:1844006",
        "reference_taxon_name": "Phaeobacter porticola",
        "submission_label": "Phaeobacter portensis",
        "submission_label_accepted_as_synonym": False,
        "examples": sorted(examples, key=lambda r: r["accession"]),
        "all_provider_matches_explained": False,
        "unretrieved_pages_assessed": False,
        "resistance_determinants_assigned": 0,
        "reference_taxon_assigned_as_experimental_subject": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("baseline", "census", "protected", "source_queue", "discovery", "expanded_union"):
        reference.check_pin(root, cohort[key])
    record = load_record(reference.check_pin(root, cohort["baseline"]))
    if (
        record["identifier"] != "CHEBI:156455"
        or record["chemical_structure"]["standard_inchi_key"] != "BLFCMITWMARUSM-UHFFFAOYSA-N"
        or record.get("resistance_mechanisms")
        or record.get("activity_spectrum")
        or "Phaeobacter inhibens" not in record["definition"]
    ):
        raise ValueError("compound identity or baseline scope changed")
    expected_record = {
        "identifier": record["identifier"],
        "label": record["label"],
        "path": "data/antibiotics/antibacterial/tropodithietic-acid.yaml",
        "sha256": cohort["baseline"]["sha256"],
        "standard_inchi_key": record["chemical_structure"]["standard_inchi_key"],
        "complete_collection_aware_record_read": True,
    }
    if cohort["record"] != expected_record:
        raise ValueError("cohort record identity changed")
    discovery = json.loads(reference.check_pin(root, cohort["discovery"]).read_bytes())
    if (
        discovery["status"] != 200
        or hashlib.sha256(discovery["body"].encode()).hexdigest() != discovery["sha256"]
        or json.loads(discovery["body"])["resultList"]["result"] != cohort["candidates"]
    ):
        raise ValueError("discovery candidate provenance changed")
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus baseline changed")
    union = json.loads(gzip.decompress(reference.check_pin(root, cohort["expanded_union"]).read_bytes()))
    members = [r for r in union["records"] if r["identifier"] == record["identifier"]]
    discovery_ids = {c["source"] + ":" + c["id"] for c in cohort["candidates"]}
    if (
        len(members) != 1
        or len(discovery_ids) != 15
        or set(members[0]["union_candidate_ids"]) != discovery_ids
    ):
        raise ValueError("discovery membership changed")
    inventory = root / "data/raw/chebi_antimicrobials.tsv"
    if reference.digest(inventory) != protected[str(inventory.relative_to(root))]:
        raise ValueError("ChEBI source changed")
    with inventory.open() as stream:
        source_rows = [
            r for r in csv.DictReader(stream, delimiter="\t") if r["chebi_id"] == record["identifier"]
        ]
    if len(source_rows) != 1:
        raise ValueError("ChEBI record missing or ambiguous")
    chebi_ids = {"MED:" + x.removeprefix("PMID:") for x in source_rows[0]["citations"].split("|")}
    sources, holds = {}, {}
    for key, (pmid, plan, status, url) in PRIMARY.items():
        sources[key] = planned_source(root, directory, key, plan, url, (status,))
        holds[pmid] = {
            "status": status,
            "disposition": "TECHNICAL_HOLD" if status == 500 else "ACCESS_HOLD",
            "primary_results_reviewed": False,
            "retry_or_alternate_route_attempted": False,
        }
    queries, data = {}, {}
    for key, (query, plan) in QUERIES.items():
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": query, "format": "json", "size": "500", "fields": FIELDS}
        )
        sources[key] = planned_source(root, directory, key, plan, url)
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        data[key] = json.loads(reference.check_pin(root, sources[key]["body"]).read_bytes())
        queries[key] = {
            "query": query,
            **search_scope(data[key], receipt["headers"], partial=key == "compound-references"),
        }
        if key != "compound-references" and queries[key]["returned_entries"] != 0:
            raise ValueError("dated empty result changed")
    for key, url in {
        "reference-taxonomy": "https://rest.uniprot.org/taxonomy/1844006",
        "producer-taxonomy": "https://rest.uniprot.org/taxonomy/search?"
        + urlencode(names.parameters("Phaeobacter inhibens")),
    }.items():
        sources[key] = planned_source(root, directory, key, "scoped-reference-plan.json", url)
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        if {k.lower(): v for k, v in receipt["headers"].items()}.get("x-uniprot-release") != "2026_03":
            raise ValueError("taxonomy release changed")
        body = reference.check_pin(root, sources[key]["body"]).read_bytes()
        data[key] = json.loads(body)
        if key == "producer-taxonomy":
            producer = names.resolve_name("Phaeobacter inhibens", {**receipt, "body": body.decode()})
    if producer["named_organism_taxon_id"] != "NCBITaxon:221822":
        raise ValueError("producer name unresolved or changed")
    page = bibliography_page(data["compound-references"]["results"], data["reference-taxonomy"])
    if (
        page["entries_checked"] != 500
        or queries["compound-references"]["reported_total"] != 3932
        or len(page["examples"]) != 3
    ):
        raise ValueError("dated partial page changed")
    return {
        "date": "2026-10-14",
        "scope": "REFERENCE_SEARCH_SCOPE_NOT_RESISTANCE_OR_ALLELE_GROUNDING",
        "cohort": reference.pin(root, directory / "cohort.json"),
        "record": cohort["record"],
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "source_queue": cohort["source_queue"],
        "sources": sources,
        "primary_holds": holds,
        "reference_queries": queries,
        "bibliography_only_page": page,
        "producer_taxonomy": {
            **producer,
            "role": "EXISTING_CHEBI_PRODUCER_LABEL_ONLY",
            "resistance_inferred": False,
            "experimental_subject_assigned": False,
        },
        "citation_cohort": {
            "discovery_ids": sorted(discovery_ids),
            "chebi_ids": sorted(chebi_ids),
            "combined_ids": sorted(discovery_ids | chebi_ids),
            "source_inventory": reference.pin(root, inventory),
            "primary_results_reviewed": 0,
            "held_primary_studies": 2,
            "other_candidates_unreviewed": len(discovery_ids | chebi_ids) - 2,
        },
        "curation_decision": "NO_SUPPORTED_NEW_RESISTANCE_CLAIM_WITH_AVAILABLE_EVIDENCE",
        "limits": {
            "scientific_http_attempts": len(sources),
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "issue_1040": "DEFERRED",
            "biological_records_changed": 0,
            "exact_alleles_or_genomes_assigned": 0,
            "numeric_AST_exported": False,
            "sequences_variants_constructs_or_protocols_exported": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
            {"source": "Europe PMC", "scope": "previously captured bibliographic discovery metadata"},
            {"source": "ChEBI", "scope": "committed source identity and citation inventory"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("tropodithietic checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "candidate_citations": len(result["citation_cohort"]["combined_ids"]),
                "primary_holds": len(result["primary_holds"]),
                "resistance_claims_added": 0,
            }
        )
    )


if __name__ == "__main__":
    main()

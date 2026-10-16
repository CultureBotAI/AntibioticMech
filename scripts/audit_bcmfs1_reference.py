"""Replay a publication-qualified Bcmfs1 reference without assigning tested alleles."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-bcmfs1-reference"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
ASSESSMENT = Path(PREFIX + "-assessment.json")
CACHE = Path("reports/resistance-grounding-2026-10-15-bcmfs1-reference")
ARO, GENE, PMID = "ARO:3009459", "Bcmfs1", "12324349"
DOI = "10.1128/AEM.68.10.4996-5004.2002"
QUALIFIED = "GENE_SPECIES_AND_PUBLICATION_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def candidate(entry, node):
    require(not {"sequence", "features", "comments"} & set(entry), "non-metadata entry")
    result = reference.project_reference(entry, GENE, 40559, node, reviewed=False)
    require(entry["organism"]["scientificName"] == node["scientificName"], "native taxon label mismatch")
    matches, strain_comments = [], []
    for index, item in enumerate(entry.get("references", [])):
        citations = item.get("citation", {}).get("citationCrossReferences", [])
        if {"database": "PubMed", "id": PMID} in citations and any(
            c.get("database") == "DOI" and c.get("id", "").casefold() == DOI.casefold() for c in citations
        ):
            matches.append({"native_reference_index": index, "pmid": PMID, "doi": DOI})
            strain_comments.extend(
                c["value"] for c in item.get("referenceComments", []) if c.get("type") == "STRAIN"
            )
    result.update(
        {
            "same_publication_matches": matches,
            "bibliography_strain_comments_not_subject_identity": sorted(set(strain_comments)),
            "qualified_reference": bool(matches),
            "disposition": QUALIFIED if matches else "GENE_ONLY_REFERENCE_LOCUS_UNRESOLVED",
            "canonical_locus_selected": False,
            "experimental_genome_assignment": None,
            "tested_derivative_assignment": None,
            "reference_identity_establishes_resistance": False,
        }
    )
    return result


def query_results(root, plan, inputs, key):
    request = inputs["request_plan"]
    item = request["requests"][key]
    receipt, attempt = inputs[key + "_receipt"], inputs[key + "_attempt"]
    parsed = urlsplit(item["url"])
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == "/uniprotkb/search"
        and not parsed.fragment
        and parse_qs(parsed.query)
        == {"query": [item["query"]], "format": ["json"], "size": ["500"], "fields": [FIELDS]},
        "unexpected metadata request",
    )
    require(
        all(
            d["url"] == item["url"]
            and d["key"] == key
            and d["plan_sha256"] == plan["inputs"]["request_plan"]["sha256"]
            and d["retries"] == d["redirects_followed"] == 0
            for d in (attempt, receipt)
        ),
        "request history changed",
    )
    body = reference.check_pin(root, receipt["body"]).read_bytes()
    headers = receipt["headers"]
    payload = json.loads(body)
    entries = payload["results"]
    require(
        receipt["status"] == 200
        and headers.get("x-uniprot-release") == request["release"] == "2026_03"
        and "application/json" in headers.get("content-type", "")
        and not headers.get("link")
        and not headers.get("location")
        and len(body) == receipt["bytes"] <= request["max_bytes"]
        and len(entries) == int(headers["x-total-results"]) <= 500
        and len({e["primaryAccession"] for e in entries}) == len(entries),
        "incomplete, duplicate or changed native response",
    )
    return entries, {
        "receipt": plan["inputs"][key + "_receipt"],
        "attempt": plan["inputs"][key + "_attempt"],
        "body": receipt["body"],
        "query": item["query"],
        "url": item["url"],
        "release": request["release"],
        "retrieved_at": receipt["retrieved_at"],
        "complete_for_query": True,
        "result_count": len(entries),
        "suggestions_selected": False,
        "suggestion_count": len(payload.get("suggestions", [])),
    }


def current_corpus(root, plan, inputs):
    with reference.check_pin(root, plan["inputs"]["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    expected = {r["path"]: r["record_sha256"] for r in census}
    require(len(expected) == len(census) == 2939, "census duplicate or count drift")
    for key in ("first_transition", "cdsa_transition"):
        for delta in inputs[key]["record_deltas"]:
            require(expected[delta["path"]] == delta["before_sha256"], "corpus transition is discontinuous")
            expected[delta["path"]] = delta["after_sha256"]
    actual = {
        str(path.relative_to(root)): reference.digest(path)
        for path in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(actual == expected, "current corpus differs from reviewed transitions")
    return len(actual)


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    inputs = {k: read_json(root, p) for k, p in plan["inputs"].items() if not p["path"].endswith(".tsv")}
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    count = current_corpus(root, plan, inputs)
    request = inputs["request_plan"]
    require(
        set(request["requests"]) == {"gene", "citation"}
        and request["requests"]["gene"]["query"] == "gene_exact:Bcmfs1 AND taxonomy_id:40559"
        and request["requests"]["citation"]["query"] == "lit_pubmed:12324349"
        and request["constraints"]["ncbi_requests"] == 0
        and request["constraints"]["issue_1040"] == "DEFERRED",
        "scope or request cohort changed",
    )
    canary = inputs["canary"]
    require(
        canary["plan_sha256"] == plan["inputs"]["request_plan"]["sha256"]
        and canary["approved_citation_query"] is True
        and canary["receipt"] == plan["inputs"]["gene_receipt"],
        "unreviewed canary",
    )
    require(not list((root / CACHE).glob("*-error.json")), "unaccounted native request failure")
    for kind in ("attempt", "receipt", "body"):
        require(
            {p.name for p in (root / CACHE).glob(f"*-{kind}.json")}
            == {f"{key}-{kind}.json" for key in ("gene", "citation")},
            "unaccounted native request",
        )
    queries, entries = {}, {}
    for key in ("gene", "citation"):
        entries[key], queries[key] = query_results(root, plan, inputs, key)
    require(len(entries["gene"]) == canary["complete_results"], "canary count mismatch")
    genes = {e["primaryAccession"]: e for e in entries["gene"]}
    for entry in entries["citation"]:
        require(genes.get(entry["primaryAccession"]) == entry, "overlapping native metadata differs")
    taxa = {}
    for taxid in ("40559", "332648"):
        wrapper = inputs["taxonomy_" + taxid]
        require(
            plan["inputs"]["taxonomy_" + taxid]
            == inputs["taxonomy_inventory"]["registry"][taxid]["source"]["wrapper"]
            and wrapper["status"] == 200
            and wrapper["url"] == "https://rest.uniprot.org/taxonomy/" + taxid
            and hashlib.sha256(wrapper["body"].encode()).hexdigest() == wrapper["sha256"]
            and wrapper["headers"]["X-UniProt-Release"] == "2026_03",
            "taxonomy cache provenance mismatch",
        )
        taxa[int(taxid)] = json.loads(wrapper["body"])
    require(
        taxa[40559]["scientificName"] == request["selection"]["species_label"] == "Botrytis cinerea",
        "source species name changed",
    )
    candidates = [candidate(e, taxa[e["organism"]["taxonId"]]) for e in genes.values()]
    candidates.sort(key=lambda c: c["protein_accession"])
    qualified = [c["protein_accession"] for c in candidates if c["qualified_reference"]]
    require(
        qualified == ["UniProtKB:" + e["primaryAccession"] for e in entries["citation"]],
        "gene and citation selection disagree",
    )
    selection = request["selection"]
    record = load_record(root / selection["record_path"])
    require(
        record["identifier"] == selection["record_identifier"]
        and record["chemical_structure"]["standard_inchi_key"] == selection["inchi_key"]
        and record["definition_source"] == "PMID:" + PMID
        and selection["aro_id"] == ARO,
        "record identity or compound definition citation changed",
    )
    claims = [(i, c) for i, c in enumerate(record["resistance_mechanisms"]) if c.get("aro_id") == ARO]
    require(len(claims) == 1, "source claim absent or ambiguous")
    claim_index, claim = claims[0]
    require(
        claim["label"] == selection["source_label"]
        and claim["evidence"]
        == [
            {
                "reference": ARO,
                "notes": "CARD/ARO asserts confers_resistance_to_antibiotic ARO:3009171 (oxpoconazole); "
                "database assertion, not a primary citation.",
            }
        ],
        "claim is no longer the reviewed source-owned assertion",
    )
    with reference.check_pin(root, plan["inputs"]["source_inventory"]).open(newline="") as stream:
        rows = [r for r in csv.DictReader(stream, delimiter="\t") if r["determinant_id"] == ARO]
    require(
        len(rows) == 1
        and rows[0]["determinant_name"] == claim["label"]
        and rows[0]["antibiotic_id"] == "ARO:3009171"
        and rows[0]["relation"] == "confers_resistance_to_antibiotic"
        and rows[0]["mechanism"] == claim["mechanism_type"],
        "source inventory binding changed",
    )
    previous = inputs["previous_coverage"]["coverage"]
    require(
        ARO in previous["remaining_terms"] and ARO not in previous["qualified_terms"],
        "previous coverage drift",
    )
    source = inputs["previous_aliases"]["terms"][ARO]
    require(source["definition_annotation"]["definition_citation_ids"] == [], "definition citations changed")
    old_query = inputs["previous_queries"]["queries"]["proteins-40559"]
    require(
        old_query["query"] == "(gene_exact:mfs1) AND taxonomy_id:40559"
        and old_query["result_count"] == 0
        and old_query["complete_for_query"] is True,
        "historical query scope changed",
    )
    return {
        "date": "2026-10-15",
        "scope": request["scope"],
        "attribution": "CARD/ARO and UniProt metadata, CC BY 4.0; "
        "primary publication abstract cited, not adopted as bulk data.",
        "plan": reference.pin(root, root / PLAN),
        "inputs": plan["inputs"],
        "assessment": reference.pin(root, root / ASSESSMENT),
        "record": {
            **reference.pin(root, root / selection["record_path"]),
            "identifier": record["identifier"],
            "inchi_key": selection["inchi_key"],
            "claim_index": claim_index,
            "claim": claim,
            "source_row": rows[0],
        },
        "queries": queries,
        "prior_query": old_query,
        "candidates": candidates,
        "terms": {
            ARO: {
                "source_label": claim["label"],
                "record_memberships": [record["identifier"]],
                "qualified_reference_accessions": [],
                "publication_reference_leads": qualified,
                "source_gene_alias_verified": False,
                "status": "PUBLICATION_REFERENCE_LEAD_SOURCE_GENE_ALIAS_UNVERIFIED",
                "exact_allele_assignment": False,
                "experimental_subject_assignment": False,
                "whole_record_primary_review": "OPEN",
            }
        },
        "coverage": {
            "cohort_terms": previous["cohort_terms"],
            "previous_qualified_count": len(previous["qualified_terms"]),
            "new_qualified_terms": [],
            "qualified_terms": previous["qualified_terms"],
            "remaining_terms": previous["remaining_terms"],
            "whole_corpus_completion": False,
        },
        "summary": {
            "corpus_records_hash_checked": count,
            "complete_collection_aware_records_read": 1,
            "native_gene_candidates": len(candidates),
            "publication_qualified_references": len(qualified),
            "qualified_card_term_mappings": 0,
            "unresolved_gene_only_candidates": len(candidates) - len(qualified),
            "new_uniprot_requests": 2,
            "reused_taxonomy_nodes": len(taxa),
            "ncbi_requests": 0,
            "biological_records_written": 0,
        },
        "constraints": request["constraints"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(args.root.resolve())
    if args.output:
        with args.output.open("x") as stream:
            stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

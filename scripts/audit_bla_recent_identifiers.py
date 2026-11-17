"""Replay bounded beta-lactamase identifier research without assigning tested alleles."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_gene_reference_followup as cached
import audit_card_reference_lineages as taxonomy
import audit_card_reference_memberships as memberships
import audit_sal_reference_context as sal
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

require = sal.require
PREFIX = "research/2026-10-15-bla-recent-identifiers"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
TERMS = {"wus1": "ARO:3007435", "ssa": "ARO:3007442", "fri11": "ARO:3007632", "vim92": "ARO:3009643"}
QUERIES = {
    "wus1": "UPP01678.1",
    "fri11": "xref:refseq-WP_223174987.1",
    "vim92": "xref:embl-PQ563311",
    "wus-taxonomy": '"Myroides albus" AND rank:species',
}


def validate_response(plan, key, receipt, attempt, body):
    item = plan["requests"][key]
    parsed = urlsplit(item["url"])
    tax = key == "wus-taxonomy"
    params = {"query": [QUERIES[key]], "format": ["json"], "size": ["500"]}
    if not tax:
        params["fields"] = [reference.FIELDS]
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == ("/taxonomy/search" if tax else "/uniprotkb/search")
        and not parsed.fragment
        and parse_qs(parsed.query) == params
        and item["query"] == QUERIES[key]
        and plan["fields"] == reference.FIELDS,
        "request scope changed",
    )
    require(
        all(
            r["url"] == item["url"] and r["key"] == key and r["retries"] == r["redirects_followed"] == 0
            for r in (receipt, attempt)
        )
        and all(receipt[k] == v for k, v in attempt.items()),
        "request history changed",
    )
    headers = receipt["headers"]
    require(
        receipt["status"] == 200
        and headers.get("x-uniprot-release") == plan["release"] == "2026_03"
        and "application/json" in headers.get("content-type", "")
        and not headers.get("link")
        and not headers.get("location")
        and len(body) == receipt["bytes"] <= plan["max_bytes"]
        and hashlib.sha256(body).hexdigest() == receipt["body"]["sha256"],
        "incomplete or changed response",
    )
    payload = json.loads(body)
    sal.metadata_only(payload)
    entries = payload["results"]
    identity = "taxonId" if tax else "primaryAccession"
    require(
        len(entries) == int(headers["x-total-results"]) <= 500
        and len({e[identity] for e in entries}) == len(entries),
        "incomplete or duplicate results",
    )
    return entries, payload.get("suggestions", [])


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def validate_assessment(assessment):
    papers = assessment["terms"]
    require(set(papers) == set(TERMS), "assessment cohort changed")
    for key, term in TERMS.items():
        require(papers[key]["aro_id"] == term, "assessment term changed")
        require(papers[key]["query"] == QUERIES.get(key), "assessment query changed")
    require(
        papers["wus1"]["deposited_nucleotide_accessions"] == ["CP102754", "CP102755"]
        and papers["wus1"]["deposited_protein_accession_lead"] == "UPP01678.1"
        and papers["wus1"]["individual_chromosome_plasmid_crosswalk_verified"] is False
        and papers["wus1"]["query_scope"] == "LITERAL_METADATA_SEARCH_NOT_EXHAUSTIVE_CDS_CROSSWALK",
        "WUS deposit or search scope changed",
    )
    require(
        papers["ssa"]["source_organism"] is None
        and papers["ssa"]["source_strain"] is None
        and papers["ssa"]["hold"] == "EXACT_SOURCE_IDENTITY_AND_PRIMARY_RESULTS_UNREVIEWED"
        and papers["ssa"]["card_model_metadata_adopted"] is False,
        "SSA unresolved source scope changed",
    )
    fri = papers["fri11"]
    require(
        fri["source_strain"] == "155105"
        and fri["source_nucleotide_accession_range"] == ["CP104976", "CP104979"]
        and fri["individual_gene_or_replicon_assigned_from_range"] is False
        and fri["additional_primary"]["source_protein_accession"] == "WP_223174987.1"
        and fri["additional_primary"]["source_protein_namespace"] == "RefSeq"
        and fri["additional_primary"]["same_subject_as_card_cited_clinical_study"] is False,
        "FRI studies or deposit range conflated",
    )
    require(
        papers["vim92"]["source_gene_nucleotide_accession"] == "PQ563311"
        and papers["vim92"]["source_accession_version_reported"] is False
        and papers["vim92"]["source_strains"] == ["PJK40", "PJK43"]
        and papers["vim92"]["primary_analysis_strain"] == "PJK40",
        "VIM source or accession scope changed",
    )
    limits = assessment["constraints"]
    require(
        set(limits)
        == {
            "native_primary_bodies_replayed",
            "whole_papers_reviewed",
            "figure_pixels_reviewed",
            "supplements_reviewed",
            "sequences_variants_constructs_protocols_or_numeric_ast_exported",
            "biological_record_writes",
            "ncbi_requests",
            "issue_1040",
            "full_investigation_complete",
        }
        and limits["ncbi_requests"] == 0
        and limits["issue_1040"] == "DEFERRED"
        and all(v is False for k, v in limits.items() if k not in {"ncbi_requests", "issue_1040"}),
        "assessment limits changed",
    )
    return papers


def bind_current(root, index):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(expected) == 2939 and actual == expected, "current corpus changed")
    terms = set(TERMS.values())
    rows = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(by_key) == len(claims), "duplicate claim membership")
    for term in terms:
        require(
            index["terms"][term]["record_memberships"]
            == sorted({c["record_identifier"] for c in claims if c["aro_id"] == term}),
            "term record membership changed",
        )
    seen = set()
    for row in rows:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in terms:
                continue
            key = (doc["identifier"], i)
            require(
                key in by_key
                and owner(claim) == "CARD"
                and memberships.checksum(claim) == by_key[key]["claim_sha256"],
                "source claim or ownership changed",
            )
            require(
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == index["terms"][claim["aro_id"]]["source_label_sha256"],
                "source label changed",
            )
            seen.add(key)
    require(seen == set(by_key) and len(rows) == 9 and len(claims) == 14, "cohort coverage changed")
    return rows, claims


def source_contexts(responses, cached_taxon):
    require(all(not responses[k] for k in ("wus1", "fri11", "vim92")), "new protein result needs review")
    nodes = responses["wus-taxonomy"]
    require(len(nodes) == 1 and nodes[0]["taxonId"] == 2562892, "WUS species needs review")
    require(cached_taxon["taxonId"] == 287, "wrong cached Pseudomonas species")
    taxonomy.lineage(nodes[0])
    taxonomy.lineage(cached_taxon)
    return {
        "wus1": sal.species_context(nodes, "Myroides albus"),
        "vim92": sal.species_context([cached_taxon], "Pseudomonas aeruginosa"),
        "ssa": None,
        "fri11": None,
    }


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    for pin in audit["inputs"].values():
        reference.check_pin(root, pin)
    data = {k: read(root, p) for k, p in audit["inputs"].items() if p["path"].endswith(".json")}
    plan = data["plan"]
    for pin in plan["inputs"].values():
        reference.check_pin(root, pin)
    public = {k: read(root, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    papers = validate_assessment(public["assessment"])
    require(set(plan["requests"]) == set(QUERIES) and plan["canary"] == "vim92", "request cohort changed")
    require(
        plan["constraints"]
        == {
            **public["assessment"]["constraints"],
            "retries": 0,
            "redirects_followed": 0,
            "source_adoption": False,
        },
        "plan constraints changed",
    )
    canary = data["canary"]
    require(
        canary["approved_remaining_queries"] is True
        and set(canary["approved_keys"]) == set(QUERIES) - {"vim92"}
        and canary["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
        and canary["receipt"] == audit["inputs"]["vim92_receipt"],
        "canary review changed",
    )
    responses, queries = {}, {}
    for key in QUERIES:
        receipt, attempt = data[key + "_receipt"], data[key + "_attempt"]
        require(
            attempt["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
            and receipt["body"] == audit["inputs"][key + "_response"],
            "request plan or body pin changed",
        )
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        responses[key], suggestions = validate_response(plan, key, receipt, attempt, body)
        queries[key] = {
            "query": QUERIES[key],
            "receipt": audit["inputs"][key + "_receipt"],
            "body": receipt["body"],
            "retrieved_at": receipt["retrieved_at"],
            "release": receipt["headers"]["x-uniprot-release"],
            "complete_result_count": len(responses[key]),
            "suggestions_not_selected": suggestions,
            "biological_absence_inferred": False,
        }
    require(set(plan["reused_taxonomy"]) == {"287"}, "cached taxonomy scope changed")
    taxon, provenance = cached.cached_node(root, plan["reused_taxonomy"]["287"])
    contexts = source_contexts(responses, taxon)
    index = public["current_index"]
    rows, claims = bind_current(root, index)
    terms = {}
    for key, term in TERMS.items():
        paper = papers[key]
        require(
            public["definitions"]["terms"][term]["definition_citation_ids"] == ["PMID:" + paper["pmid"]]
            and public["prior_name_screen"]["terms"][term]["citation_pool_size"] == 0
            and not index["terms"][term]["reference_links"],
            "own citation or previous reference scope changed",
        )
        terms[term] = {
            "primary_assessment": paper,
            "source_taxonomy_context": contexts[key],
            "record_memberships": index["terms"][term]["record_memberships"],
            "reference_accessions": [],
            "references": [],
            "status": "PRIMARY_SOURCE_IDENTITY_HOLD"
            if key == "ssa"
            else "SCOPED_QUERY_EMPTY_NOT_BIOLOGICAL_ABSENCE",
            "experimental_protein_assignment": None,
            "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    return {
        "date": "2026-10-15",
        "inputs": audit["inputs"],
        "scope": public["assessment"]["scope"],
        "records": rows,
        "claims": claims,
        "terms": terms,
        "queries": queries,
        "reused_taxonomy_provenance": provenance,
        "summary": {
            "current_corpus_hashes_verified": 2939,
            "complete_records_loaded": len(rows),
            "source_claims_bound": len(claims),
            "terms_investigated": len(terms),
            "selected_protein_references": 0,
            "complete_empty_protein_queries": 3,
            "primary_identity_holds": 1,
            "source_species_name_contexts": 2,
            "new_native_taxonomy_nodes": 1,
            "reused_native_taxonomy_nodes": 1,
            "new_native_requests": len(queries),
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            **plan["constraints"],
            "broad_index_rewritten": False,
            "experimental_identifiers_assigned": False,
        },
        "attribution": "CARD/ARO and UniProt identity metadata retained with provenance. "
        "Primary-publication locations and review limitations remain explicit; "
        "no CARD model content adopted.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write only the new research projection")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root)
    if args.write:
        with (root / OUTPUT).open("x") as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write("\n")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Replay three paper-identifier gaps without converting taxonomy to allele identity."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_reference_memberships as memberships
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-bla-primary-identifiers"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
KEYS = ("ebr5", "prc1", "psz1")
TERMS = {"ebr5": "ARO:3007437", "prc1": "ARO:3007085", "psz1": "ARO:3007648"}
PROTEIN_QUERIES = {
    "ebr5": "gene_exact:NZD85_03605",
    "prc1": "xref:embl-MW854031",
    "psz1": "xref:embl-OQ725878",
}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_embl,lit_pubmed_id,sequence_version,version"
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def validate_response(plan, key, receipt, attempt, body, taxonomy=False):
    item = plan["requests"][key]
    parsed = urlsplit(item["url"])
    params = {"query": [item["query"]], "format": ["json"], "size": ["500"]}
    if not taxonomy:
        params["fields"] = [FIELDS]
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == ("/taxonomy/search" if taxonomy else "/uniprotkb/search")
        and not parsed.fragment
        and parse_qs(parsed.query) == params,
        "unexpected request scope",
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
        "incomplete or changed native response",
    )
    payload = json.loads(body)
    entries = payload["results"]
    identity = "taxonId" if taxonomy else "primaryAccession"
    require(
        len(entries) == int(headers["x-total-results"]) <= 500
        and len({e[identity] for e in entries}) == len(entries),
        "incomplete or duplicate results",
    )
    require(
        all(not {"sequence", "features", "comments"} & set(e) for e in entries),
        "non-metadata entry",
    )
    return entries, payload.get("suggestions", [])


def taxonomy_context(entries, source_name, alternate_name=None):
    require(all(e.get("active") is True for e in entries), "inactive taxonomy entry")
    require(len({e["taxonId"] for e in entries}) == len(entries), "duplicate taxonomy entry")
    matches = [e for e in entries if e["scientificName"] == source_name and e["rank"] == "species"]
    require(len(matches) == 1, "source species name unresolved or ambiguous")
    match = matches[0]
    alternates = [e for e in entries if e["scientificName"] == alternate_name] if alternate_name else []
    require(len(entries) == len(matches) + len(alternates), "unreviewed taxonomy result")
    if alternate_name:
        require(len(alternates) == 1, "alternate name unresolved or ambiguous")
    return {
        "source_name_match": {
            "taxon_id": "NCBITaxon:" + str(match["taxonId"]),
            "scientific_name": match["scientificName"],
            "rank": match["rank"],
            "scope": "SPECIES_NAME_REFERENCE_NOT_EXPERIMENTAL_ISOLATE_ID",
        },
        "native_nodes": [
            {k: e[k] for k in ("taxonId", "scientificName", "rank", "active", "parent", "lineage")}
            for e in sorted(entries, key=lambda e: e["taxonId"])
        ],
        "alternate_context": [
            {
                "taxon_id": "NCBITaxon:" + str(e["taxonId"]),
                "scientific_name": e["scientificName"],
                "rank": e["rank"],
                "source_species_in_native_lineage": any(
                    n["taxonId"] == match["taxonId"] for n in e["lineage"]
                ),
                "assigned_as_source_strain": False,
                "same_subject_crosswalk_verified": False,
            }
            for e in alternates
        ],
        "experimental_taxon_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "species_name_implies_resistance": False,
    }


def bind_current(root, index, papers):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(expected) == 2939 and actual == expected, "current corpus changed")
    terms = {p["aro_id"] for p in papers.values()}
    rows = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(by_key) == len(claims), "duplicate source membership")
    seen = set()
    for row in rows:
        record = load_record(root / row["path"])
        require(
            record["identifier"] == row["identifier"]
            and record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in terms:
                continue
            key = (record["identifier"], i)
            require(key in by_key and owner(claim) == "CARD", "source membership or ownership changed")
            require(memberships.checksum(claim) == by_key[key]["claim_sha256"], "source claim changed")
            require(
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == index["terms"][claim["aro_id"]]["source_label_sha256"],
                "source label changed",
            )
            seen.add(key)
    require(seen == set(by_key) and len(rows) == 12 and len(claims) == 18, "cohort coverage changed")
    return rows, claims, len(actual)


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    inputs = {k: read_json(root, p) for k, p in audit["inputs"].items()}
    protein_plan, taxonomy_plan = inputs["protein_plan"], inputs["taxonomy_plan"]
    public_pins = protein_plan["inputs"]
    for p in public_pins.values():
        reference.check_pin(root, p)
    public = {k: read_json(root, p) for k, p in public_pins.items() if p["path"].endswith(".json")}
    require(audit["inputs"]["assessment"] == public_pins["assessment"], "assessment pin mismatch")
    papers, index = inputs["assessment"]["papers"], public["current_index"]
    require(set(papers) == set(KEYS), "paper cohort changed")
    rows, claims, corpus_count = bind_current(root, index, papers)
    terms, query_views = {}, {}
    for plan, prefix in ((protein_plan, "protein"), (taxonomy_plan, "taxonomy")):
        require(
            plan["constraints"]["ncbi_requests"] == 0 and plan["constraints"]["issue_1040"] == "DEFERRED",
            "source deferral changed",
        )
        canary = inputs[prefix + "_canary"]
        require(
            canary["plan_sha256"] == audit["inputs"][prefix + "_plan"]["sha256"]
            and canary["receipt"] == audit["inputs"][plan["canary"] + "_receipt"]
            and canary["approved_remaining_queries"] is True,
            "unreviewed canary",
        )
        expected_keys = set(KEYS) if prefix == "protein" else {k + "-taxonomy" for k in KEYS}
        require(set(plan["requests"]) == expected_keys, "request cohort changed")
    for key in KEYS:
        paper = papers[key]
        term = TERMS[key]
        require(
            paper["aro_id"] == term and protein_plan["requests"][key]["query"] == PROTEIN_QUERIES[key],
            "source term or identifier query changed",
        )
        require(
            public["definition_citations"]["terms"][term]["definition_citation_ids"]
            == ["PMID:" + paper["pmid"]],
            "own definition citation changed",
        )
        require(
            public["protein_name_screen"]["terms"][term]["citation_pool_size"] == 0,
            "prior citation result changed",
        )
        require(not index["terms"][term]["reference_links"], "term already has reference context")
        responses = {}
        for taxonomy in (False, True):
            request_key = key + "-taxonomy" if taxonomy else key
            plan = taxonomy_plan if taxonomy else protein_plan
            plan_key = "taxonomy_plan" if taxonomy else "protein_plan"
            receipt = inputs[request_key + "_receipt"]
            require(
                receipt["plan_sha256"] == audit["inputs"][plan_key]["sha256"]
                and receipt["body"] == audit["inputs"][request_key + "_body"],
                "receipt pin mismatch",
            )
            body = reference.check_pin(root, receipt["body"]).read_bytes()
            entries, suggestions = validate_response(
                plan, request_key, receipt, inputs[request_key + "_attempt"], body, taxonomy
            )
            responses[taxonomy] = entries
            query_views[request_key] = {
                "query": plan["requests"][request_key]["query"],
                "url": receipt["url"],
                "receipt": audit["inputs"][request_key + "_receipt"],
                "body": receipt["body"],
                "retrieved_at": receipt["retrieved_at"],
                "release": receipt["headers"]["x-uniprot-release"],
                "complete_result_count": len(entries),
                "suggestions_not_selected": suggestions,
            }
        require(responses[False] == [], "new protein candidates require scientific review")
        context = taxonomy_context(
            responses[True], paper["source_organism"], "Pantoea sp. X85" if key == "psz1" else None
        )
        terms[term] = {
            "paper": paper,
            "taxonomy_context": context,
            "record_memberships": index["terms"][term]["record_memberships"],
            "reference_accessions": [],
            "protein_status": "EXPLICIT_QUERY_EMPTY_NOT_BIOLOGICAL_ABSENCE",
            "paper_identifiers_are_source_reported_not_new_database_verification": True,
            "experimental_protein_assignment": None,
            "experimental_allele_assignment": None,
            "experimental_genome_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    require(
        {k: v["complete_result_count"] for k, v in query_views.items()}
        == {"ebr5": 0, "prc1": 0, "psz1": 0, "ebr5-taxonomy": 1, "prc1-taxonomy": 1, "psz1-taxonomy": 2},
        "native result checkpoint changed",
    )
    return {
        "date": "2026-10-15",
        "scope": "PRIMARY_IDENTIFIERS_AND_SPECIES_NAMES_WITH_UNRESOLVED_PROTEINS",
        "inputs": {**public_pins, "audit_plan": reference.pin(root, root / PLAN)},
        "queries": query_views,
        "terms": terms,
        "records": rows,
        "claims": claims,
        "summary": {
            "complete_target_records_read": len(rows),
            "current_record_hashes_verified": corpus_count,
            "source_claims_bound": len(claims),
            "terms_investigated": len(terms),
            "species_names_grounded": 3,
            "distinct_native_taxonomy_nodes": 4,
            "new_selected_proteins": 0,
            "whole_record_primary_signoffs": 0,
        },
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "biological_record_writes": 0,
            "source_adoptions": 0,
            "github_mutations": 0,
            "full_investigation_complete": False,
        },
        "attribution": (
            "CARD/ARO ontology: McMaster University, CC BY 4.0. UniProt metadata: UniProt Consortium. "
            "Primary identifiers: the three cited articles; no primary article text, sequence or assay "
            "data redistributed."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    if args.write:
        with (args.root / OUTPUT).open("x") as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write("\n")
    else:
        require(result == json.loads((args.root / OUTPUT).read_bytes()), "saved projection differs")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Replay Sal source-identity evidence without assigning experimental alleles."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_reference_memberships as memberships
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-sal-reference-context"
CACHE = "reports/resistance-grounding-2026-10-15-sal-reference-context"
KEYS = ("salb", "salc", "sald", "sale")
TERMS = dict(zip(KEYS, ("ARO:3007026", "ARO:3007027", "ARO:3007028", "ARO:3007029"), strict=True))
QUERIES = {
    "salb": "gene_exact:H3V22_03170",
    "salc": "MBW0764195",
    "sald": "xref:refseq-WP_082039181.1",
    "sale": "xref:refseq-WP_096809342.1",
    "salb-accession": "accession:A0A7D7YNB9",
    "taxonomy": (
        '("Staphylococcus lentus" OR "Staphylococcus fleurettii" OR '
        '"Staphylococcus gallinarum" OR "Staphylococcus nepalensis") AND rank:species'
    ),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def metadata_only(value):
    if isinstance(value, dict):
        require(
            not {"sequence", "features", "comments", "pdbx_seq_one_letter_code", "entity_poly_seq"}
            & set(value),
            "non-metadata entry",
        )
        for child in value.values():
            metadata_only(child)
    elif isinstance(value, list):
        for child in value:
            metadata_only(child)


def validate_response(plan, key, receipt, attempt, body):
    item = plan["requests"][key]
    parsed = urlsplit(item["url"])
    pdb = key == "pdb-metadata"
    taxonomy = key == "taxonomy"
    params = {"query": [item["query"]]}
    if not pdb:
        require(item["query"] == QUERIES[key], "query identity changed")
        params.update({"format": ["json"], "size": ["500"]})
        if not taxonomy:
            require(plan["fields"] == reference.FIELDS, "metadata fields changed")
            params["fields"] = [reference.FIELDS]
    require(
        parsed.scheme == "https"
        and parsed.netloc == ("data.rcsb.org" if pdb else "rest.uniprot.org")
        and parsed.path == ("/graphql" if pdb else "/taxonomy/search" if taxonomy else "/uniprotkb/search")
        and not parsed.fragment
        and parse_qs(parsed.query) == params,
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
        and "application/json" in headers.get("content-type", "")
        and not headers.get("link")
        and not headers.get("location")
        and len(body) == receipt["bytes"] <= plan["max_bytes"]
        and hashlib.sha256(body).hexdigest() == receipt["body"]["sha256"],
        "incomplete or changed response",
    )
    payload = json.loads(body)
    metadata_only(payload)
    if pdb:
        require(not payload.get("errors"), "GraphQL errors")
        return payload["data"]["entries"], []
    require(headers.get("x-uniprot-release") == plan["release"] == "2026_03", "release changed")
    entries = payload["results"]
    identity = "taxonId" if taxonomy else "primaryAccession"
    require(
        len(entries) == int(headers["x-total-results"]) <= 500
        and len({e[identity] for e in entries}) == len(entries),
        "incomplete or duplicate results",
    )
    return entries, payload.get("suggestions", [])


def species_context(entries, source_name):
    matches = []
    for entry in entries:
        require(
            entry.get("active") is True and entry["rank"] == "species", "inactive or non-species taxonomy"
        )
        fields = [{"field": "scientificName", "value": entry["scientificName"]}]
        fields += [
            {"field": field, "value": value}
            for field in ("synonyms", "otherNames")
            for value in entry.get(field, [])
        ]
        evidence = [f for f in fields if f["value"] == source_name]
        if evidence:
            matches.append(
                {
                    "taxon_id": "NCBITaxon:" + str(entry["taxonId"]),
                    "scientific_name": entry["scientificName"],
                    "rank": entry["rank"],
                    "source_name": source_name,
                    "native_name_matches": evidence,
                    "native_node": {
                        k: entry[k]
                        for k in ("taxonId", "scientificName", "rank", "active", "parent", "lineage")
                    },
                    "scope": "SPECIES_NAME_REFERENCE_NOT_EXPERIMENTAL_ISOLATE",
                }
            )
    require(len(matches) == 1, "ambiguous or missing exact source name")
    return matches[0]


def focal_structure(entries):
    require(len(entries) == 1 and entries[0]["rcsb_id"] == "7P48", "wrong structure")
    entry = entries[0]
    citation = entry["rcsb_primary_citation"]
    require(
        citation["pdbx_database_id_PubMed"] == 35137182
        and citation["pdbx_database_id_DOI"] == "10.1093/nar/gkac058",
        "wrong structure citation",
    )
    entities = entry["polymer_entities"]
    require(len({e["rcsb_id"] for e in entities}) == len(entities), "duplicate polymer entity")
    focal = [e for e in entities if e["rcsb_id"] == "7P48_6"]
    require(len(focal) == 1, "missing focal entity")
    entity = focal[0]
    require(
        entity["rcsb_polymer_entity"]["pdbx_description"] == "ABC-F type ribosomal protection protein",
        "wrong component description",
    )
    sources = entity["entity_src_gen"]
    require(len(sources) == 1, "ambiguous component source")
    source = sources[0]
    require(
        "H3V22_03170" in {s.strip() for s in source["pdbx_gene_src_gene"].split(",")}
        and source["pdbx_gene_src_ncbi_taxonomy_id"] == "42858"
        and source["pdbx_host_org_ncbi_taxonomy_id"] == "1280",
        "source/host context changed",
    )
    refs = entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"]
    require(
        refs == [{"database_name": "UniProt", "database_accession": "A0A7D7YNB9"}], "focal accession changed"
    )
    return {
        "entry": "7P48",
        "revision": entry["rcsb_accession_info"],
        "citation": citation,
        "focal_entity": entity,
        "ribosomal_entities_not_assigned": len(entities) - 1,
        "paper_construct": "ENGINEERED_NTPASE_DEFICIENT_STRUCTURAL_CONSTRUCT",
        "mutation_count_proves_wild_type": False,
        "experimental_allele_assignment": None,
    }


def refseq_candidates(entries, identifier, species):
    """Require the native versioned cross-reference, not the query or gene label."""
    selected = []
    for entry in entries:
        if entry.get("entryType") == "Inactive":
            continue
        refs = [
            r
            for r in entry.get("uniProtKBCrossReferences", [])
            if r["database"] == "RefSeq" and r["id"] == identifier
        ]
        if not refs or entry["organism"]["taxonId"] != species:
            continue
        require(
            entry["entryType"] in {"UniProtKB unreviewed (TrEMBL)", "UniProtKB reviewed (Swiss-Prot)"},
            "unknown entry status",
        )
        selected.append(
            {
                "accession": "UniProtKB:" + entry["primaryAccession"],
                "entry_type": entry["entryType"],
                "versions": entry["entryAudit"],
                "organism": {k: entry["organism"][k] for k in ("taxonId", "scientificName")},
                "source_refseq_cross_references": refs,
                "scope": "EXACT_SOURCE_REPORTED_REFSEQ_DATABASE_CROSSWALK_NOT_EXPERIMENTAL_ALLELE",
                "experimental_strain_assignment": None,
            }
        )
    return selected


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
    require(len(by_key) == len(claims), "duplicate membership")
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
            require(key in by_key and owner(claim) == "CARD", "membership or ownership changed")
            require(memberships.checksum(claim) == by_key[key]["claim_sha256"], "claim changed")
            require(
                hashlib.sha256(claim["label"].encode()).hexdigest()
                == index["terms"][claim["aro_id"]]["source_label_sha256"],
                "label changed",
            )
            seen.add(key)
    require(seen == set(by_key) and len(rows) == 5 and len(claims) == 16, "cohort coverage changed")
    return rows, claims


def build(root):
    audit = json.loads((root / (PREFIX + "-audit-plan.json")).read_bytes())
    inputs = {k: read(root, p) for k, p in audit["inputs"].items() if not k.endswith("_body")}
    plan = inputs["plan"]
    public = {k: read(root, p) for k, p in plan["inputs"].items() if p["path"].endswith(".json")}
    for p in plan["inputs"].values():
        reference.check_pin(root, p)
    require(set(plan["requests"]) == {*KEYS, "pdb-metadata", "taxonomy"}, "request cohort changed")
    require(set(inputs["accession_plan"]["requests"]) == {"salb-accession"}, "accession scope changed")
    for p in inputs["accession_plan"]["inputs"].values():
        reference.check_pin(root, p)
    require(
        inputs["accession_plan"]["inputs"]["original_plan"] == audit["inputs"]["plan"],
        "successor plan mismatch",
    )
    for review_key, key in (("pdb_canary", "pdb-metadata"), ("uniprot_canary", "salb")):
        review = inputs[review_key]
        require(
            review["plan_sha256"] == audit["inputs"]["plan"]["sha256"]
            and review["receipt"] == audit["inputs"][key + "_receipt"]
            and review["approved_remaining_queries"] is True,
            "unreviewed canary",
        )
    responses, query_views = {}, {}
    for key in (*plan["requests"], "salb-accession"):
        plan_key = "accession_plan" if key == "salb-accession" else "plan"
        selected_plan = inputs[plan_key]
        require(
            selected_plan["constraints"]["ncbi_requests"] == 0
            and selected_plan["constraints"]["issue_1040"] == "DEFERRED",
            "NCBI deferral changed",
        )
        receipt = inputs[key + "_receipt"]
        require(
            receipt["plan_sha256"] == audit["inputs"][plan_key]["sha256"]
            and receipt["body"] == audit["inputs"][key + "_body"],
            "receipt pin mismatch",
        )
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        entries, suggestions = validate_response(selected_plan, key, receipt, inputs[key + "_attempt"], body)
        responses[key] = entries
        query_views[key] = {
            "query": selected_plan["requests"][key]["query"],
            "receipt": audit["inputs"][key + "_receipt"],
            "result_count": len(entries),
            "suggestions_not_selected": suggestions,
        }
    structure = focal_structure(responses["pdb-metadata"])
    inactive = responses["salb-accession"]
    require(
        len(inactive) == 1
        and inactive[0]["primaryAccession"] == "A0A7D7YNB9"
        and inactive[0]["entryType"] == "Inactive"
        and inactive[0]["inactiveReason"]["inactiveReasonType"] == "DELETED",
        "deposited accession status changed; reassess",
    )
    structure["deposited_accession_current_status"] = inactive[0]
    structure["selected_current_reference"] = None
    citation_receipt = public["citation_receipt"]
    citation_body = reference.check_pin(root, plan["inputs"]["citation_body"]).read_bytes()
    citation_headers = {k.lower(): v for k, v in citation_receipt["headers"].items()}
    citation_entries = json.loads(citation_body)["results"]
    require(
        citation_receipt["status"] == 200
        and citation_receipt["query"] == "lit_pubmed:35137182"
        and citation_receipt["sha256"] == hashlib.sha256(citation_body).hexdigest()
        and citation_headers["x-uniprot-release"] == "2026_03"
        and not citation_headers.get("link")
        and len(citation_entries) == int(citation_headers["x-total-results"]) == 42,
        "prior citation response changed",
    )
    require(
        all("ribosomal" in json.dumps(e.get("proteinDescription", {})).lower() for e in citation_entries),
        "citation pool requires reassessment",
    )
    index, assessment = public["current_index"], public["assessment"]
    require(set(assessment["terms"]) == set(KEYS), "assessment cohort changed")
    rows, claims = bind_current(root, index)
    terms = {}
    for key in KEYS:
        paper = assessment["terms"][key]
        term = TERMS[key]
        require(paper["aro_id"] == term and paper["query"] == QUERIES[key], "paper binding changed")
        require(
            public["definition_citations"]["terms"][term]["definition_citation_ids"] == ["PMID:35137182"],
            "own citation changed",
        )
        require(
            not index["terms"][term]["reference_links"]
            and public["protein_name_screen"]["terms"][term]["citation_pool_size"] == 42,
            "prior reference context changed",
        )
        species = species_context(responses["taxonomy"], paper["source_species"])
        candidates = refseq_candidates(
            responses[key], paper["source_protein"], species["native_node"]["taxonId"]
        )
        require(
            (key == "sald" and len(candidates) == 1) or (key != "sald" and not responses[key]),
            "unexpected protein results require review",
        )
        terms[term] = {
            "source_identity": paper,
            "species_name_context": species,
            "reference_candidates": candidates,
            "status": "SOURCE_REFSEQ_REFERENCE_CROSSWALK"
            if candidates
            else "REFERENCE_UNRESOLVED_NOT_BIOLOGICAL_ABSENCE",
            "record_memberships": index["terms"][term]["record_memberships"],
            "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    require(
        len(responses["taxonomy"])
        == len({v["species_name_context"]["taxon_id"] for v in terms.values()})
        == 4,
        "unreviewed taxonomy results",
    )
    require(
        terms["ARO:3007026"]["species_name_context"]["taxon_id"] == "NCBITaxon:42858",
        "PDB source taxonomy mismatch",
    )
    return {
        "date": "2026-10-15",
        "scope": "SOURCE_IDENTITY_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_ALLELE",
        "inputs": audit["inputs"],
        "primary_assessment": plan["inputs"]["assessment"],
        "records": rows,
        "claims": claims,
        "terms": terms,
        "queries": query_views,
        "structure": structure,
        "prior_citation_pool": {
            "entries": 42,
            "selected_sal_accessions": [],
            "reason": "RIBOSOMAL_COMPONENTS_NOT_SAL",
        },
        "counts": {
            "current_corpus_hashes_checked": 2939,
            "complete_records_loaded": 5,
            "card_claims": 16,
            "terms": 4,
            "species_name_references": 4,
            "current_uniprot_crosswalks": 1,
            "inactive_deposited_accessions": 1,
        },
        "constraints": {
            **plan["constraints"],
            "experimental_allele_assignments": 0,
            "whole_record_signoffs": 0,
            "full_corpus_goal": "OPEN",
            "broad_index_rewritten": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    output = args.root / (PREFIX + ".json")
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check:
        require(output.read_bytes() == encoded, "dossier drift")
    else:
        with output.open("xb") as stream:
            stream.write(encoded)
    print(json.dumps(result["counts"], sort_keys=True))


if __name__ == "__main__":
    main()

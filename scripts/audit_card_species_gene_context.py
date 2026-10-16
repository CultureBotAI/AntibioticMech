"""Ground source-qualified gene references without assigning resistant alleles."""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

import audit_card_complex_members as members
import audit_card_literature_expansion as literature

reference, require = members.reference, members.require
read_json = members.prior.mex.read_json
PREFIX = "research/2026-10-15-card-species-gene-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
INSPECTION = Path(PREFIX + "-taxonomy-inspection.json")
SCOPE = "SOURCE_SPECIES_AND_LITERAL_GENE_REFERENCE_CONTEXT_NOT_RESISTANT_ALLELES"
PATTERN = r"(?P<species>[A-Z][a-z]+ [a-z]+) (?P<gene>[A-Za-z][A-Za-z0-9]*)(?: with .*)?"
QUALIFIED = "GENE_SYMBOL_OWN_CITATION_SPECIES_REFERENCE_NOT_ALLELE"
MISMATCH = "DIFFERENT_SPECIES_REFERENCE_WITHHELD"


def parse_label(label):
    match = re.fullmatch(PATTERN, label)
    return match.groupdict() if match else None


def gene_matches(entry, symbol):
    result = []
    for i, gene in enumerate(entry.get("genes", [])):
        values = [("geneName", gene["geneName"])] if "geneName" in gene else []
        values += [(f"synonyms/{j}", value) for j, value in enumerate(gene.get("synonyms", []))]
        result += [
            {"field": f"genes/{i}/{field}", "value": value["value"]}
            for field, value in values
            if value["value"].casefold() == symbol.casefold()
        ]
    return result


def species_name_binding(name, node):
    require(node["rank"] == "species" and node["active"] is True, "source name needs active species node")
    result = []
    if name.casefold() == node["scientificName"].casefold():
        result.append({"field": "scientificName", "value": node["scientificName"]})
    result += [
        {"field": f"synonyms/{i}", "value": value}
        for i, value in enumerate(node.get("synonyms", []))
        if name.casefold() == value.casefold()
    ]
    return result


def disposition(source_species, reference_species):
    if reference_species is None:
        return "REFERENCE_WITHOUT_SPECIES_RANK_WITHHELD"
    return QUALIFIED if source_species == reference_species else MISMATCH


def cohort(root, index):
    labels = {}
    with reference.check_pin(root, index["inputs"]["source_inventory"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            term, name = row["determinant_id"], row["determinant_name"]
            require(term not in labels or labels[term] == name, "conflicting source labels")
            labels[term] = name
    require(len(index["terms"]) == 2002 and set(index["terms"]) <= set(labels), "source universe changed")
    eligible = {t: labels[t] for t, row in index["terms"].items() if not row["links"]}
    require(len(eligible) == 720, "unlinked index cohort changed")
    selected = {t: label for t, label in sorted(eligible.items()) if parse_label(label)}
    return selected, sorted(set(eligible) - set(selected))


def replay_queries(root, terms, definitions, frozen):
    citations = {c for t in terms for c in definitions["terms"][t]["definition_citation_ids"]}
    require(all(re.fullmatch(r"PMID:[1-9][0-9]*", c) for c in citations), "unhandled non-PMID citation")
    pmids = {c[5:] for c in citations}
    require(len(pmids) == 113 and pmids <= set(frozen["queries"]), "own citation coverage changed")
    entries, pools, queries = {}, {}, {}
    for pmid in sorted(pmids):
        item = frozen["queries"][pmid]
        found, provenance = literature.read_query(root, root / item["directory"], pmid)
        require(
            provenance == item["query"]
            and provenance["complete_for_query"]
            and provenance["release"] == "2026_03",
            "cached citation provenance changed",
        )
        pools[pmid] = sorted(found)
        queries[pmid] = {**item, "accessions": ["UniProtKB:" + a for a in sorted(found)]}
        for accession, entry in found.items():
            require(not {"sequence", "features", "comments"} & set(entry), "unexpected operational fields")
            require(accession not in entries or entries[accession] == entry, "conflicting native entry")
            entries[accession] = entry
    return entries, pools, queries


def matches_for_terms(labels, definitions, entries, pools):
    result = {}
    for term, label in labels.items():
        pmids = [c[5:] for c in definitions["terms"][term]["definition_citation_ids"]]
        pool = sorted({a for p in pmids for a in pools[p]})
        symbol = parse_label(label)["gene"]
        result[term] = {a: gene_matches(entries[a], symbol) for a in pool if gene_matches(entries[a], symbol)}
    return result


def new_taxonomy_source(root, plan):
    inspection = json.loads((root / INSPECTION).read_bytes())
    request = plan["new_taxonomy_request"]
    plan_pin = reference.pin(root, root / PLAN)
    directory = root / request["cache_directory"]
    attempt_path = directory / "taxonomy-1125630-attempt.json"
    attempt = json.loads(attempt_path.read_bytes())
    source = inspection["source"]
    receipt = read_json(root, source["receipt"])
    require(
        inspection["plan"] == attempt["plan"] == plan_pin
        and request["url"]
        == attempt["url"]
        == receipt["url"]
        == "https://rest.uniprot.org/taxonomy/1125630.json"
        and receipt["status"] == 200
        and receipt["bytes"] == len(receipt["body"].encode()) <= request["max_response_bytes"]
        and receipt["headers"]["x-uniprot-release"] == request["release"] == "2026_03"
        and all(
            item[k] == 0
            for item in (request, attempt, receipt, inspection)
            for k in ("retries", "redirects_followed")
        )
        and not receipt["headers"].get("location")
        and not list(directory.glob("*-error.json"))
        and {p.name for p in directory.glob("*-attempt.json")} == {attempt_path.name}
        and {p.name for p in directory.glob("*-receipt.json")} == {"taxonomy-1125630-receipt.json"},
        "unaccounted, failed or changed taxonomy request",
    )
    taxon, _ = members.prior.lineages.native_taxon(root, source, "1125630", "2026_03")
    _, species = members.prior.lineages.lineage(taxon)
    require(
        inspection["accepted_for_reference_taxonomy"] is True
        and inspection["accepted_for_experimental_subject_assignment"] is False
        and inspection["accepted_for_exact_resistant_allele_assignment"] is False
        and inspection["scientific_name"] == taxon["scientificName"]
        and inspection["rank"] == taxon["rank"] == "strain"
        and inspection["species_ancestor_taxon_id"] == str(species["taxonId"]) == "573",
        "taxonomy inspection or identity changed",
    )
    return source, {
        "inspection": reference.pin(root, root / INSPECTION),
        "attempt": reference.pin(root, attempt_path),
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["selection"]["label_pattern"] == PATTERN
        and plan["constraints"]
        == {
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "outreach": False,
            "reuse_terms_review_resumed": False,
            "new_protein_requests": 0,
            "new_primary_reviews": 0,
            "biological_record_writes": False,
            "experimental_alleles_subjects_or_genomes_assigned": False,
            "operational_details_or_numeric_ast_exported": False,
            "whole_record_primary_signoffs": False,
            "full_corpus_goal_status": "OPEN",
        },
        "planned scope changed",
    )
    anchor = read_json(root, plan["inputs"]["acr_checkpoint"])
    read_json(root, plan["inputs"]["acr_verification"])
    inputs = {
        key: read_json(root, anchor["inputs"][key])
        for key in ("index", "corpus_update", "definition_citations", "citation_plan", "lineages")
    }
    index, definitions = inputs["index"], inputs["definition_citations"]
    labels, excluded = cohort(root, index)
    require(len(labels) == plan["selection"]["expected_grammar_matches"] == 178, "grammar cohort changed")
    records, claims = members.current_context(root, index, inputs["corpus_update"], set(labels), labels)
    require(len(claims) == plan["selection"]["expected_claims"] == 225, "claim coverage changed")
    entries, pools, queries = replay_queries(root, labels, definitions, inputs["citation_plan"])
    matches = matches_for_terms(labels, definitions, entries, pools)
    found = {a for row in matches.values() for a in row}
    require(
        len(entries) == 990 and len(found) == 42 and sum(bool(x) for x in matches.values()) == 19,
        "literal gene candidate coverage changed",
    )
    source_names = {parse_label(labels[t])["species"] for t in labels if matches[t]}
    require(
        source_names == set(plan["source_species_for_gene_matched_terms"]), "source species coverage changed"
    )
    new_source, new_request = new_taxonomy_source(root, plan)
    native_sources = {t: row["native_source"] for t, row in inputs["lineages"]["taxa"].items()}
    for tid, row in inputs["lineages"]["species"].items():
        if tid not in native_sources and row["native_sources"]:
            native_sources[tid] = row["native_sources"][0]
    require(
        not set(plan["extra_cached_taxonomy"]) & set(native_sources) and "1125630" not in native_sources,
        "supplement would replace prior native taxonomy",
    )
    native_sources.update(plan["extra_cached_taxonomy"])
    native_sources["1125630"] = new_source
    needed = {str(entries[a]["organism"]["taxonId"]) for a in found}
    needed |= set(plan["source_species_for_gene_matched_terms"].values())
    taxa, sources = {}, {}
    for tid in sorted(needed):
        taxa[tid], sources[tid] = members.prior.lineages.native_taxon(
            root, native_sources[tid], tid, "2026_03"
        )
    names = {}
    for name, tid in plan["source_species_for_gene_matched_terms"].items():
        binding = species_name_binding(name, taxa[tid])
        require(bool(binding), "source species name lacks native support")
        names[name] = {"identity": members.prior.lineages.identity(taxa[tid]), "name_binding": binding}
    views = {
        "UniProtKB:" + a: members.member_reference(entries[a], taxa[str(entries[a]["organism"]["taxonId"])])
        for a in sorted(found)
    }
    terms = {}
    for term, label in labels.items():
        parsed = parse_label(label)
        citations = definitions["terms"][term]["definition_citation_ids"]
        candidate_rows = []
        source = names.get(parsed["species"])
        for accession, matched_fields in matches[term].items():
            identifier = "UniProtKB:" + accession
            view = views[identifier]
            status = disposition(source["identity"], view["reference_taxonomy"]["species"])
            candidate_rows.append(
                {
                    "protein_accession": identifier,
                    "literal_gene_fields": matched_fields,
                    "own_citation_ids": [c for c in citations if accession in pools[c[5:]]],
                    "disposition": status,
                    "qualified_reference": status == QUALIFIED,
                    "exact_allele_assignment": False,
                    "experimental_subject_assignment": False,
                }
            )
        qualified = [row["protein_accession"] for row in candidate_rows if row["qualified_reference"]]
        terms[term] = {
            "source_label": label,
            "parsed_tokens_not_identity_by_themselves": parsed,
            "source_label_sha256": index["terms"][term]["source_label_sha256"],
            "source_species_binding": source,
            "source_species_scope": "REFERENCE_NAME_ONLY_NOT_EXPERIMENTAL_SUBJECT"
            if source
            else "NOT_RESOLVED_NO_LITERAL_GENE_CANDIDATE",
            "record_memberships": index["terms"][term]["record_memberships"],
            "definition_citations": citations,
            "all_own_citation_queries_complete": bool(citations),
            "citation_scope": "OWN_DEFINITION_CITATION_QUERIES_COMPLETE"
            if citations
            else "NO_OWN_DEFINITION_CITATIONS_DISCOVERY_REMAINS_OPEN",
            "literal_gene_candidates": candidate_rows,
            "qualified_reference_accessions": qualified,
            "status": "QUALIFIED_REFERENCE_CONTEXT_PRIMARY_REVIEW_OPEN"
            if qualified
            else "GENE_MATCHES_WITHHELD_FOR_SPECIES_MISMATCH"
            if candidate_rows
            else "NO_OWN_DEFINITION_CITATIONS_DISCOVERY_REMAINS_OPEN"
            if not citations
            else "NO_LITERAL_GENE_MATCH_IN_OWN_CITATION_POOLS_NOT_BIOLOGICAL_ABSENCE",
            "whole_record_primary_review": "OPEN",
            "biological_absence_inferred": False,
        }
    qualified_terms = {t for t, row in terms.items() if row["qualified_reference_accessions"]}
    dispositions = Counter(c["disposition"] for t in terms.values() for c in t["literal_gene_candidates"])
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "inputs": {**plan["inputs"], **{key: anchor["inputs"][key] for key in inputs}},
        "records": records,
        "claims": claims,
        "terms": terms,
        "reference_views": views,
        "citation_queries": queries,
        "taxonomy_sources": sources,
        "new_taxonomy_request": new_request,
        "grammar_excluded_unlinked_terms": excluded,
        "summary": {
            "current_card_terms": 2002,
            "unlinked_index_terms": 720,
            "grammar_selected_terms": len(terms),
            "grammar_excluded_terms": len(excluded),
            "source_claims": len(claims),
            "complete_records_read": len(records),
            "corpus_records_hash_checked": 2939,
            "own_citation_queries": len(queries),
            "terms_without_own_definition_citations": sum(
                not t["definition_citations"] for t in terms.values()
            ),
            "queries_with_zero_hits": sum(not p for p in pools.values()),
            "native_entries_screened": len(entries),
            "literal_gene_matched_terms": sum(bool(x) for x in matches.values()),
            "candidate_entries": len(views),
            "native_taxonomy_nodes_verified": len(sources),
            "qualified_reference_terms": len(qualified_terms),
            "qualified_reference_claim_memberships": sum(c["aro_id"] in qualified_terms for c in claims),
            "candidate_dispositions": dict(sorted(dispositions.items())),
            "new_uniprot_taxonomy_requests": 1,
            "new_protein_requests": 0,
            "ncbi_requests": 0,
        },
        "limits": {
            **plan["constraints"],
            "source_variant_descriptions_define_reference_alleles": False,
            "all_reference_family_members_enumerated": False,
            "prior_index_rewritten": False,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; database references, not new primary evidence.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    target = args.root / args.output
    if args.check or target.exists():
        require(target.read_bytes() == payload, "audit does not reproduce; preserve prior output")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()

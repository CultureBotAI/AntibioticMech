"""Replay bounded CYP51/ERG11 reference queries without experimental assignment."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_demethylase_taxa as source_audit
import audit_card_reference_lineages as lineages
import audit_fungamr_cohort as native
import audit_fungamr_references as fungal
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

CACHE = Path("reports/resistance-grounding-2026-10-14-card-demethylase-references")
OUTPUT = Path("research/2026-10-14-card-demethylase-references.json")
COHORT_SHA = "fddf381bb6712805fac5154b2126a5c308d4f2d09a53323fa5bf78b19a53f35b"
FIELDS = fungal.FIELDS


def query_signature(url):
    parsed = urlsplit(url)
    params = parse_qs(parsed.query, keep_blank_values=True)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "rest.uniprot.org"
        or parsed.path != "/uniprotkb/search"
        or parsed.fragment
        or any(len(v) != 1 for v in params.values())
        or set(params) - {"query", "format", "fields", "size", "sort"}
        or params.get("format") != ["json"]
    ):
        raise ValueError("unsupported reference query identity")
    fields = set(params.get("fields", [""])[0].split(","))
    if not set(FIELDS.split(",")) <= fields or fields - (set(FIELDS.split(",")) | {"xref_card", "xref_sgd"}):
        raise ValueError("reference query fields changed")
    query = params.get("query", [""])[0]
    if query.startswith("(") and query.endswith(")"):
        query = query[1:-1]
    match = re.fullmatch(
        r"gene_exact:(cyp51[a-c]?|erg11) AND taxonomy_id:([1-9]\d*) AND reviewed:(true|false)",
        query,
        flags=re.I,
    )
    if not match:
        raise ValueError("reference query is not the bounded gene/species/status conjunction")
    return match[1].casefold(), int(match[2]), match[3].casefold() == "true"


def validate_entries(entries, gene, reviewed):
    fungal.validate_gene_results({"results": entries}, gene, reviewed)
    if len(entries) > 500:
        raise ValueError("reference query exceeds bounded size")
    for entry in entries:
        audit = entry.get("entryAudit", {})
        if (
            any(type(audit.get(k)) is not int or audit[k] < 1 for k in ("entryVersion", "sequenceVersion"))
            or {"sequence", "features", "comments"}.intersection(entry)
            or type(entry.get("organism", {}).get("taxonId")) is not int
            or entry["organism"]["taxonId"] <= 0
        ):
            raise ValueError("reference versions, taxon identifier or payload scope changed")


def read_gene_source(root, source, gene, species, reviewed):
    if query_signature(source["url"]) != (gene, species, reviewed):
        raise ValueError("gene/species/review-status scope changed")
    payload, provenance = native.read_source(root, source)
    entries = payload["results"]
    validate_entries(entries, gene, reviewed)
    return entries, {
        "source": provenance,
        "gene_query_key": gene,
        "species_id": species,
        "reviewed_subset": reviewed,
        "result_count": len(entries),
        "accessions": sorted(e["primaryAccession"] for e in entries),
        "complete_for_query": True,
        "zero_hit_is_biological_absence": False,
    }


def read_planned_gene(root, directory, key, plan_name, context, reviewed):
    directory = root / directory
    plan = json.loads((directory / plan_name).read_bytes())
    item = plan["requests"][key]
    gene = context["casefold_gene_query_key"]
    species = int(context["named_reference_taxon_id"].split(":")[1])
    if item["gene"] != gene or item["species_id"] != species or item["reviewed"] is not reviewed:
        raise ValueError("planned reference query differs from source context")
    source = planned_source(root, directory, key, plan_name, item["url"])
    return read_gene_source(root, source, gene, species, reviewed)


def reviewed_queries(root, directory, cohort):
    result = {}
    plan = json.loads((directory / "reviewed-plan.json").read_bytes())
    if plan["cohort"] != reference.pin(root, directory / "cohort.json"):
        raise ValueError("reviewed plan cohort changed")
    used = set()
    for key, context in cohort["contexts"].items():
        selected = context["reviewed_query"]
        if context["named_reference_taxon_id"] is None:
            if selected is not None or context["unreviewed_cached_query"] is not None:
                raise ValueError("unresolved organism context was assigned a protein query")
            continue
        if context["named_reference_taxon_rank"] != "species":
            raise ValueError("gene query must retain resolved species scope")
        gene, species = (
            context["casefold_gene_query_key"],
            int(context["named_reference_taxon_id"].split(":")[1]),
        )
        if selected["kind"] == "REUSED_COMPLETE_QUERY":
            entries, query = read_gene_source(root, selected["source"], gene, species, True)
        elif selected["kind"] == "NEW_PLANNED_QUERY":
            request_key = selected["request_key"]
            if plan["requests"][request_key]["context"] != key:
                raise ValueError("reviewed request context binding changed")
            entries, query = read_planned_gene(
                root, directory, request_key, "reviewed-plan.json", context, True
            )
            used.add(request_key)
        else:
            raise ValueError("unsupported reviewed source kind")
        result[key] = (entries, {**query, "retrieval_kind": selected["kind"]})
    if used != set(plan["requests"]) or len(result) != 39:
        raise ValueError("complete reviewed-query coverage changed")
    return result


def selected_queries(root, directory, cohort):
    reviewed = reviewed_queries(root, directory, cohort)
    plan = json.loads((directory / "unreviewed-plan.json").read_bytes())
    if plan["cohort"] != reference.pin(root, directory / "cohort.json"):
        raise ValueError("unreviewed plan cohort changed")
    if plan["reviewed_sources"] != {key: query["source"] for key, (_, query) in reviewed.items()}:
        raise ValueError("fallback reviewed-source evidence changed")
    expected = {k for k, (entries, _) in reviewed.items() if not entries}
    if set(plan["contexts"]) != expected:
        raise ValueError("unreviewed fallback does not cover exactly the reviewed zero-hit contexts")
    result, used = {}, set()
    for key, (entries, query) in reviewed.items():
        queries = {"reviewed": query}
        context = cohort["contexts"][key]
        if key in expected:
            selected = plan["contexts"][key]
            if selected["kind"] == "REUSED_COMPLETE_QUERY":
                if selected != context["unreviewed_cached_query"]:
                    raise ValueError("cached fallback selection changed")
                entries, fallback = read_gene_source(
                    root, selected["source"], query["gene_query_key"], query["species_id"], False
                )
            else:
                if selected["kind"] != "NEW_PLANNED_QUERY":
                    raise ValueError("unsupported fallback source kind")
                request_key = selected["request_key"]
                if plan["requests"][request_key]["context"] != key:
                    raise ValueError("fallback request context binding changed")
                entries, fallback = read_planned_gene(
                    root, directory, request_key, "unreviewed-plan.json", context, False
                )
                used.add(request_key)
            queries["unreviewed"] = {**fallback, "retrieval_kind": selected["kind"]}
        result[key] = {
            "entries": entries,
            "queries": queries,
            "status": fungal.disposition(list(queries.values())),
        }
    if used != set(plan["requests"]):
        raise ValueError("unreviewed query accounting changed")
    return result


def gene_identity(entry, gene):
    matches = []
    blocks = []
    for index, block in enumerate(entry["genes"]):
        values = {}
        for field in ("geneName", "synonyms", "orderedLocusNames", "orfNames"):
            items = [block[field]] if field == "geneName" and field in block else block.get(field, [])
            values[field] = [v["value"] for v in items]
            if field in {"geneName", "synonyms"}:
                matches.extend(
                    {"gene_index": index, "field": field, "value": v}
                    for v in values[field]
                    if v.casefold() == gene
                )
        blocks.append(values)
    if len({m["gene_index"] for m in matches}) != 1:
        raise ValueError("reference gene is absent or ambiguously scoped")
    return blocks, matches


def project(entry, taxon, gene, species, reviewed):
    validate_entries([entry], gene, reviewed)
    nodes, ancestor = lineages.lineage(taxon)
    if (
        ancestor is None
        or ancestor["taxonId"] != species
        or not any(n["taxonId"] == 4751 and n["rank"] == "kingdom" for n in nodes)
    ):
        raise ValueError("reference ancestry differs from the source species")
    result = reference.project_reference(entry, gene, species, taxon, reviewed=reviewed)
    genes, matches = gene_identity(entry, gene)
    flag = entry["proteinDescription"].get("flag")
    result.update(
        {
            "genes": genes,
            "native_protein_flag": flag,
            "unflagged_means_complete": False,
            "experimental_genome_assignment": None,
            "database_review_status_is_primary_results_review": False,
            "resistance_inferred_from_reference": False,
            "reference_organism_label_matches_taxonomy": (
                entry["organism"]["scientificName"] == taxon["scientificName"]
            ),
        }
    )
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return result, matches


def check_canary(root, directory, plan_name):
    plan = json.loads((directory / plan_name).read_bytes())
    if not plan["requests"]:
        return None
    review_path = directory / (plan_name.removesuffix("-plan.json") + "-canary-review.json")
    review = json.loads(review_path.read_bytes())
    key = plan["canary_request"]
    if (
        review["manually_inspected"] is not True
        or review["experimental_assignments"] is not False
        or review["plan"] != reference.pin(root, directory / plan_name)
        or review["body"] != reference.pin(root, directory / (key + "-response.bin"))
        or review["receipt"] != reference.pin(root, directory / (key + "-receipt.json"))
    ):
        raise ValueError("canary review evidence changed")
    return reference.pin(root, review_path)


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen reference cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in (
        "prior",
        "prior_verification",
        "census",
        "source_inventory",
        "protected",
        "gene_cache_inventory",
    ):
        reference.check_pin(root, cohort[key])
    prior = json.loads((root / cohort["prior"]["path"]).read_bytes())
    if source_audit.build(root) != prior or set(cohort["contexts"]) != set(prior["gene_name_contexts"]):
        raise ValueError("whole source/taxonomy cohort changed")
    for key, row in prior["gene_name_contexts"].items():
        if any(cohort["contexts"][key][k] != v for k, v in row.items()):
            raise ValueError("gene context differs from the source-name checkpoint")
    canaries = {
        p: check_canary(root, directory, p)
        for p in ("reviewed-plan.json", "unreviewed-plan.json", "taxonomy-plan.json")
    }
    selection = selected_queries(root, directory, cohort)
    taxonomy_plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    reference.check_pin(root, taxonomy_plan["taxonomy_cache_inventory"])
    required_taxa = {str(e["organism"]["taxonId"]) for item in selection.values() for e in item["entries"]}
    if set(taxonomy_plan["taxa"]) != required_taxa or taxonomy_plan["cohort"] != reference.pin(
        root, cohort_path
    ):
        raise ValueError("reference taxonomy coverage changed")
    taxa, taxonomy_sources, used = {}, {}, set()
    for taxid, item in taxonomy_plan["taxa"].items():
        if item["kind"] == "REUSED_NATIVE_TAXON":
            source = item["source"]
        else:
            if item["kind"] != "NEW_PLANNED_TAXON":
                raise ValueError("unsupported taxonomy source kind")
            key = item["request_key"]
            url = f"https://rest.uniprot.org/taxonomy/{taxid}"
            source = planned_source(root, directory, key, "taxonomy-plan.json", url)
            used.add(key)
        if not urlsplit(source["url"]).path.startswith("/taxonomy/"):
            raise ValueError("reference taxon source is not native taxonomy")
        body, taxonomy_sources[taxid] = native.read_source(root, source)
        candidates = [t for t in body.get("results", [body]) if t["taxonId"] == int(taxid)]
        if len(candidates) != 1:
            raise ValueError("taxon identifier absent or duplicated in native response")
        taxa[taxid] = candidates[0]
        lineages.lineage(taxa[taxid])
    if used != set(taxonomy_plan["requests"]):
        raise ValueError("taxonomy request accounting changed")
    contexts, proteins = {}, {}
    for key, context in cohort["contexts"].items():
        row = {k: v for k, v in context.items() if k not in {"reviewed_query", "unreviewed_cached_query"}}
        row.pop("protein_query_status")
        if key not in selection:
            contexts[key] = {
                **row,
                "status": "SOURCE_NAME_UNRESOLVED_NO_PROTEIN_QUERY",
                "queries": {},
                "reference_candidates": [],
                "experimental_assignments": False,
            }
            continue
        selected = selection[key]
        reviewed = "unreviewed" not in selected["queries"]
        gene = context["casefold_gene_query_key"]
        species = int(context["named_reference_taxon_id"].split(":")[1])
        candidates = []
        for entry in selected["entries"]:
            protein, matches = project(
                entry, taxa[str(entry["organism"]["taxonId"])], gene, species, reviewed
            )
            accession = protein["protein_accession"]
            if accession in proteins and proteins[accession] != protein:
                raise ValueError("conflicting cross-context reference metadata")
            proteins[accession] = protein
            candidates.append(
                {
                    "protein_accession": accession,
                    "native_gene_field_matches": matches,
                    "exact_resistant_allele": False,
                    "experimental_subject_assignment": False,
                }
            )
        contexts[key] = {
            **row,
            "status": selected["status"],
            "queries": selected["queries"],
            "reference_candidates": sorted(candidates, key=lambda x: x["protein_accession"]),
            "experimental_assignments": False,
        }
    terms = {}
    for key, context in contexts.items():
        for tid in context["terms"]:
            if tid in terms:
                raise ValueError("term appears in multiple source contexts")
            terms[tid] = {
                **prior["terms"][tid],
                "gene_context": key,
                "reference_status": context["status"],
                "reference_candidates": [c["protein_accession"] for c in context["reference_candidates"]],
                "primary_review_status": "OPEN",
            }
    if set(terms) != set(prior["terms"]):
        raise ValueError("source term coverage changed")
    return {
        "scope": "ALL_CARD_CYP51_ERG11_REFERENCE_CONTEXTS_NOT_EXPERIMENTAL_ALLELES_OR_PHENOTYPES",
        "date": "2026-10-14",
        "release": "2026_03",
        "selection_policy": cohort["selection_policy"],
        "inputs": {
            "cohort": reference.pin(root, cohort_path),
            "prior": cohort["prior"],
            "census": cohort["census"],
            "source_inventory": cohort["source_inventory"],
            "gene_cache_inventory": cohort["gene_cache_inventory"],
            "plans": {p: reference.pin(root, directory / p) for p in canaries},
            "canaries": canaries,
            "taxonomy_sources": taxonomy_sources,
            "taxonomy_cache_inventory": taxonomy_plan["taxonomy_cache_inventory"],
        },
        "terms": dict(sorted(terms.items())),
        "gene_contexts": contexts,
        "proteins": dict(sorted(proteins.items())),
        "claims": prior["claims"],
        "records": prior["records"],
        "summary": {
            "corpus_records_checked": 2939,
            "source_terms": len(terms),
            "source_assertions": 141,
            "source_records": 31,
            "gene_contexts": len(contexts),
            "queried_gene_contexts": len(selection),
            "context_status_counts": dict(Counter(c["status"] for c in contexts.values())),
            "term_status_counts": dict(Counter(t["reference_status"] for t in terms.values())),
            "contexts_with_candidates": sum(bool(c["reference_candidates"]) for c in contexts.values()),
            "terms_with_candidates": sum(bool(t["reference_candidates"]) for t in terms.values()),
            "reference_proteins": len(proteins),
            "reference_taxa": len(taxa),
            "protein_review_statuses": dict(Counter(p["entry_type"] for p in proteins.values())),
            "biological_records_changed": 0,
            "experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limitations": [
            "Complete queries concern the selected gene/species/review-status slice, "
            "not all possible alleles.",
            "Unreviewed queries are used only after a complete reviewed zero-hit query; "
            "every candidate is retained.",
            "Source gene spellings and paralog suffixes remain separate; "
            "native aliases are reference context only.",
            "References, native loci, taxonomy ancestry and database bibliography "
            "do not identify tested alleles.",
            "Zero hits and unresolved names do not establish biological absence or susceptibility.",
            "No source resistance claim is revalidated or propagated by this reference mapping.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "primary_access_holds_preserved": True,
            "new_primary_requests": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, release 2026_03, CC BY 4.0.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != encoded:
            raise ValueError("saved reference cohort differs from native replay")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

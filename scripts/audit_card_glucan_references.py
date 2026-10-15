"""Audit all FKS/FSK source contexts without correcting spellings or assigning alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit

import audit_card_demethylase_references as references
import audit_card_demethylase_taxa as names_audit
import audit_fungamr_cohort as native
import audit_fungamr_references as fungal
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-card-glucan-synthase")
OUTPUT = Path("research/2026-10-14-card-glucan-references.json")
COHORT_SHA = "093c645cf879465970c4f5c299e261db9adfb409f084e373dd1154b624a1bc20"
SELECT = re.compile(r"\b(?:FKS\d*|FSK\d*|glucan synthase)\b", re.I)
LABEL = re.compile(r"([A-Z][a-z]+ [a-z]+) ((?i:FKS[12]|FSK1)) (.+)")
FIELDS = fungal.FIELDS


def source_identity(label):
    match = LABEL.fullmatch(label)
    if not match:
        raise ValueError("unreviewed glucan-synthase source label syntax")
    name, gene, wording = match.groups()
    return {
        "source_organism_name": name,
        "source_gene_label": gene,
        "source_claim_wording": wording,
        "casefold_gene_query_key": gene.casefold(),
        "spelling_corrected": False,
    }


def query_url(gene, species, reviewed):
    if gene not in {"fks1", "fks2", "fsk1"} or type(species) is not int or species < 1:
        raise ValueError("unsupported exact gene/species query")
    if type(reviewed) is not bool:
        raise ValueError("review status must be boolean")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f"gene_exact:{gene} AND taxonomy_id:{species} AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": FIELDS,
        }
    )


def query_signature(url, *, verify_fields=True):
    parsed = urlsplit(url)
    params = parse_qs(parsed.query, keep_blank_values=True)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "rest.uniprot.org"
        or parsed.path != "/uniprotkb/search"
        or parsed.fragment
        or any(len(v) != 1 for v in params.values())
        or set(params) - {"query", "fields", "size", "format", "sort"}
        or params.get("format") != ["json"]
    ):
        raise ValueError("unsupported exact query endpoint or parameters")
    fields = set(params.get("fields", [""])[0].split(","))
    optional = {"xref_card", "xref_sgd", "xref_geneid", "xref_embl", "xref_refseq"}
    if verify_fields and (
        not set(FIELDS.split(",")) <= fields or fields - (set(FIELDS.split(",")) | optional)
    ):
        raise ValueError("reference-only query fields changed")
    query = params.get("query", [""])[0]
    if query.startswith("(") and query.endswith(")"):
        query = query[1:-1]
    match = re.fullmatch(
        r"gene_exact:(fks[12]|fsk1) AND taxonomy_id:([1-9]\d*) AND reviewed:(true|false)", query, flags=re.I
    )
    if not match:
        raise ValueError("query is not the exact FKS/FSK species and review-status slice")
    return match[1].casefold(), int(match[2]), match[3].casefold() == "true"


def read_gene(root, source, gene, species, reviewed):
    if query_signature(source["url"]) != (gene, species, reviewed):
        raise ValueError("cached query differs from gene/species/review scope")
    body, provenance = native.read_source(root, source)
    entries = body["results"]
    if not isinstance(body.get("suggestions", []), list):
        raise ValueError("unexpected search-suggestion structure")
    references.validate_entries(entries, gene, reviewed)
    return entries, {
        "source": provenance,
        "gene": gene,
        "species_id": species,
        "reviewed_subset": reviewed,
        "result_count": len(entries),
        "accessions": sorted(e["primaryAccession"] for e in entries),
        "complete_for_query": True,
        "zero_hit_is_biological_absence": False,
        "suggestions_ignored": len(body.get("suggestions", [])),
        "suggestions_followed": False,
    }


def read_names(root, directory, cohort):
    plan = json.loads((directory / "names-plan.json").read_bytes())
    if plan["cohort"] != reference.pin(root, directory / "cohort.json"):
        raise ValueError("name plan cohort changed")
    references.check_canary(root, directory, "names-plan.json")
    expected = {t["source_organism_name"] for t in cohort["terms"].values()}
    if set(cohort["names"]) != expected:
        raise ValueError("source-name coverage changed")
    prior = json.loads(reference.check_pin(root, cohort["prior_fungal_references"]).read_bytes())
    names, used = {}, set()
    for name, item in cohort["names"].items():
        if item["kind"] == "NEW_PLANNED_NAME":
            key = item["request_key"]
            if plan["requests"][key]["name"] != name:
                raise ValueError("name request context changed")
            source = planned_source(
                root, directory, key, "names-plan.json", names_audit.query_url(name, "BINOMIAL")
            )
            used.add(key)
        elif item["kind"] in {"REUSED_NATIVE_NAME", "REUSED_PRIMARY_NOMENCLATURE"}:
            source = item["source"]
        else:
            raise ValueError("unsupported name evidence")
        if not urlsplit(source["url"]).path.startswith("/taxonomy/"):
            raise ValueError("name source is not native taxonomy")
        body, provenance = native.read_source(root, source)
        match_name = name
        nomenclature = None
        if item["kind"] == "REUSED_PRIMARY_NOMENCLATURE":
            if (
                name != "Nakaseomyces glabratus"
                or item["review"] != prior["nomenclature_assessment"]
                or source != prior["names"][name]["source"]
            ):
                raise ValueError("specific nomenclature evidence changed")
            nomenclature = fungal.nomenclature(root, item["review"], body)
            match_name = nomenclature["scientific_name"]
        result = names_audit.resolve_name(body, match_name, "BINOMIAL")
        if nomenclature and (
            result["selected_taxon"] is None
            or result["selected_taxon"]["taxon_id"] != f"NCBITaxon:{nomenclature['species_id']}"
        ):
            raise ValueError("nomenclature and native taxonomy disagree")
        names[name] = {
            **result,
            "status": "PRIMARY_NOMENCLATURE_PLUS_NATIVE_REFERENCE" if nomenclature else result["status"],
            "native_name_resolution_status": result["status"],
            "source_name": name,
            "native_match_name": match_name,
            "matching_fields_apply_to": "native_match_name",
            "evidence_kind": item["kind"],
            "source": provenance,
            "nomenclature": nomenclature,
            "nomenclature_assessment": item.get("review"),
        }
    if used != set(plan["requests"]):
        raise ValueError("name request coverage changed")
    return names


def contexts(cohort, names):
    result = {}
    for tid, term in cohort["terms"].items():
        name, gene = term["source_organism_name"], term["casefold_gene_query_key"]
        key = json.dumps([name, gene], separators=(",", ":"))
        selected = names[name]["selected_taxon"]
        species = int(selected["taxon_id"].split(":")[1]) if selected else None
        row = result.setdefault(
            key,
            {
                "source_name": name,
                "gene_query_key": gene,
                "source_gene_labels": [],
                "species_id": species,
                "terms": [],
                "query_key": json.dumps([gene, species], separators=(",", ":")) if species else None,
                "source_spelling_corrected": False,
            },
        )
        row["terms"].append(tid)
        row["source_gene_labels"] = sorted(set(row["source_gene_labels"] + [term["source_gene_label"]]))
    return dict(sorted(result.items()))


def query_contexts(source_contexts):
    result = {}
    for row in source_contexts.values():
        if row["query_key"]:
            result[row["query_key"]] = (row["gene_query_key"], row["species_id"])
    return result


def planned_gene(root, directory, plan_name, key, gene, species, reviewed):
    plan = json.loads((directory / plan_name).read_bytes())
    item = plan["requests"][key]
    if (item["gene"], item["species_id"]) != (gene, species) or item["reviewed"] is not reviewed:
        raise ValueError("planned gene context changed")
    source = planned_source(root, directory, key, plan_name, query_url(gene, species, reviewed))
    return read_gene(root, source, gene, species, reviewed)


def read_queries(root, directory, plan_name, expected, reviewed):
    plan = json.loads((directory / plan_name).read_bytes())
    if plan["cohort"] != reference.pin(root, directory / "cohort.json") or set(plan["queries"]) != set(
        expected
    ):
        raise ValueError("query plan scope changed")
    reference.check_pin(root, plan["gene_cache_inventory"])
    references.check_canary(root, directory, plan_name)
    result, used = {}, set()
    for key, (gene, species) in expected.items():
        selected = plan["queries"][key]
        if selected["kind"] == "REUSED_COMPLETE_QUERY":
            entries, provenance = read_gene(root, selected["source"], gene, species, reviewed)
        elif selected["kind"] == "NEW_PLANNED_QUERY":
            request_key = selected["request_key"]
            if plan["requests"][request_key]["query_key"] != key:
                raise ValueError("planned request binding changed")
            entries, provenance = planned_gene(
                root, directory, plan_name, request_key, gene, species, reviewed
            )
            used.add(request_key)
        else:
            raise ValueError("unsupported query evidence; held queries cannot be treated as zero hits")
        result[key] = (entries, {**provenance, "retrieval_kind": selected["kind"]})
    if used != set(plan["requests"]):
        raise ValueError("query request accounting changed")
    return result


def selected_queries(root, directory, source_contexts):
    expected = query_contexts(source_contexts)
    reviewed = read_queries(root, directory, "reviewed-plan.json", expected, True)
    fallback_scope = {k: expected[k] for k, (entries, _) in reviewed.items() if not entries}
    fallback_plan = json.loads((directory / "unreviewed-plan.json").read_bytes())
    if fallback_plan["reviewed_sources"] != {k: q["source"] for k, (_, q) in reviewed.items()}:
        raise ValueError("fallback evidence differs from complete reviewed queries")
    fallback = read_queries(root, directory, "unreviewed-plan.json", fallback_scope, False)
    result = {}
    for key, (entries, provenance) in reviewed.items():
        queries = {"reviewed": provenance}
        if key in fallback:
            entries, queries["unreviewed"] = fallback[key]
        result[key] = {
            "entries": entries,
            "queries": queries,
            "status": fungal.disposition(list(queries.values())),
        }
    return result


def check_sources(root, directory, cohort):
    for key in (
        "index",
        "census",
        "source_inventory",
        "source_queue",
        "prior_fungal_references",
        "protected",
        "name_cache_inventory",
        "prior_checkpoint",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads((root / cohort["index"]["path"]).read_bytes())
    labels = {}
    with (root / cohort["source_inventory"]["path"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            tid, label = row["determinant_id"], row["determinant_name"]
            if tid in labels and labels[tid] != label:
                raise ValueError("conflicting source labels")
            labels[tid] = label
    expected = {tid for tid in index["terms"] if SELECT.search(labels[tid])}
    if set(cohort["terms"]) != expected or len(expected) != 47:
        raise ValueError("full glucan-synthase term selection changed")
    for tid, term in cohort["terms"].items():
        if (
            any(term[k] != v for k, v in source_identity(labels[tid]).items())
            or term["source_label"] != labels[tid]
            or term["source_label_sha256"] != hashlib.sha256(labels[tid].encode()).hexdigest()
            or term["record_memberships"] != index["terms"][tid]["record_memberships"]
            or index["terms"][tid]["links"]
        ):
            raise ValueError("source label, gene spelling or membership changed")
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("whole corpus membership or record bytes changed")
    selected_ids = {rid for term in cohort["terms"].values() for rid in term["record_memberships"]}
    if cohort["records"] != [r for r in census if r["identifier"] in selected_ids] or len(selected_ids) != 8:
        raise ValueError("selected record coverage changed")
    claims = []
    for item in cohort["records"]:
        record = load_record(root / item["path"])
        snapshot = directory / (item["identifier"].replace(":", "-") + "-before.yaml")
        if (
            record != load_record(snapshot)
            or reference.digest(snapshot) != item["record_sha256"]
            or record["identifier"] != item["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
        ):
            raise ValueError("complete selected record identity changed")
        for position, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
                if claim["label"] != labels[claim["aro_id"]]:
                    raise ValueError("source claim wording changed")
                claims.append(
                    {
                        "record_identifier": record["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    if claims != cohort["claims"] or len(claims) != 47:
        raise ValueError("assertion membership, order or content changed")


def build(root, directory=CACHE):
    directory = root / directory
    path = directory / "cohort.json"
    if reference.digest(path) != COHORT_SHA:
        raise ValueError("frozen cohort changed")
    cohort = json.loads(path.read_bytes())
    check_sources(root, directory, cohort)
    names = read_names(root, directory, cohort)
    source_contexts = contexts(cohort, names)
    selected = selected_queries(root, directory, source_contexts)
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    references.check_canary(root, directory, "taxonomy-plan.json")
    reference.check_pin(root, plan["taxonomy_cache_inventory"])
    required = {str(e["organism"]["taxonId"]) for v in selected.values() for e in v["entries"]}
    if plan["cohort"] != reference.pin(root, path) or set(plan["taxa"]) != required:
        raise ValueError("candidate taxonomy coverage changed")
    taxa, taxonomy_sources, used = {}, {}, set()
    for taxid, item in plan["taxa"].items():
        if item["kind"] == "REUSED_NATIVE_TAXON":
            source = item["source"]
        elif item["kind"] == "NEW_PLANNED_TAXON":
            key = item["request_key"]
            source = planned_source(
                root, directory, key, "taxonomy-plan.json", f"https://rest.uniprot.org/taxonomy/{taxid}"
            )
            used.add(key)
        else:
            raise ValueError("unsupported reference taxonomy evidence")
        if not urlsplit(source["url"]).path.startswith("/taxonomy/"):
            raise ValueError("reference taxon source is not native taxonomy")
        body, taxonomy_sources[taxid] = native.read_source(root, source)
        matches = [t for t in body.get("results", [body]) if t["taxonId"] == int(taxid)]
        if len(matches) != 1:
            raise ValueError("native reference taxon missing or duplicated")
        taxa[taxid] = matches[0]
        references.lineages.lineage(taxa[taxid])
    if used != set(plan["requests"]):
        raise ValueError("reference taxonomy request accounting changed")
    proteins, query_results = {}, {}
    for key, item in selected.items():
        gene, species = json.loads(key)
        candidates = []
        for entry in item["entries"]:
            protein, matches = references.project(
                entry,
                taxa[str(entry["organism"]["taxonId"])],
                gene,
                species,
                "unreviewed" not in item["queries"],
            )
            accession = protein["protein_accession"]
            if accession in proteins and proteins[accession] != protein:
                raise ValueError("conflicting reference metadata across query contexts")
            proteins[accession] = protein
            candidates.append(
                {
                    "protein_accession": accession,
                    "native_gene_field_matches": matches,
                    "experimental_subject_assignment": False,
                    "exact_resistant_allele": False,
                }
            )
        query_results[key] = {
            "gene": gene,
            "species_id": species,
            "status": item["status"],
            "queries": item["queries"],
            "reference_candidates": sorted(candidates, key=lambda c: c["protein_accession"]),
            "source_spelling_corrected": False,
        }
    terms = {}
    for key, context in source_contexts.items():
        chosen = query_results.get(context["query_key"])
        context["reference_status"] = chosen["status"] if chosen else "SOURCE_NAME_UNRESOLVED_NO_QUERY"
        context["reference_candidates"] = chosen["reference_candidates"] if chosen else []
        for tid in context["terms"]:
            terms[tid] = {
                **cohort["terms"][tid],
                "source_context": key,
                "named_reference_taxon_id": f"NCBITaxon:{context['species_id']}"
                if context["species_id"]
                else None,
                "reference_status": context["reference_status"],
                "reference_candidates": [p["protein_accession"] for p in context["reference_candidates"]],
                "experimental_subject_assignment": False,
                "exact_allele_assignment": False,
                "experimental_genome_assignment": None,
                "primary_review_status": "OPEN",
            }
    return {
        "date": "2026-10-14",
        "scope": "ALL_CARD_FKS_FSK_REFERENCE_CONTEXTS_NOT_RESISTANCE_ALLELES",
        "release": "2026_03",
        "inputs": {
            "cohort": reference.pin(root, path),
            **{
                k: cohort[k]
                for k in (
                    "index",
                    "census",
                    "source_inventory",
                    "prior_fungal_references",
                    "name_cache_inventory",
                )
            },
            "plans": {
                name: reference.pin(root, directory / name)
                for name in (
                    "names-plan.json",
                    "reviewed-plan.json",
                    "unreviewed-plan.json",
                    "taxonomy-plan.json",
                )
            },
            "taxonomy_sources": taxonomy_sources,
            "taxonomy_cache_inventory": plan["taxonomy_cache_inventory"],
            "canaries": {
                name: references.check_canary(root, directory, name)
                for name in (
                    "names-plan.json",
                    "reviewed-plan.json",
                    "unreviewed-plan.json",
                    "taxonomy-plan.json",
                )
            },
        },
        "terms": dict(sorted(terms.items())),
        "source_contexts": source_contexts,
        "names": names,
        "query_contexts": query_results,
        "proteins": dict(sorted(proteins.items())),
        "records": cohort["records"],
        "claims": cohort["claims"],
        "summary": {
            "corpus_records_checked": 2939,
            "source_terms": len(terms),
            "source_assertions": 47,
            "source_records": 8,
            "source_names": len(names),
            "source_contexts": len(source_contexts),
            "unique_gene_species_queries": len(query_results),
            "reference_proteins": len(proteins),
            "reference_taxa": len(taxa),
            "term_status_counts": dict(Counter(t["reference_status"] for t in terms.values())),
            "context_status_counts": dict(Counter(t["reference_status"] for t in source_contexts.values())),
            "terms_with_candidates": sum(bool(t["reference_candidates"]) for t in terms.values()),
            "native_protein_flags": dict(Counter(str(p["native_protein_flag"]) for p in proteins.values())),
            "biological_records_changed": 0,
            "experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limitations": [
            "FSK1 and FKS1 remain distinct source spellings; no inferred correction or alias.",
            "Equivalent species references do not establish shared experimental strains or alleles.",
            "All candidates in the selected query subset are retained; no representative is chosen.",
            "Zero exact-query hits are not biological absence; "
            "unreviewed searches follow reviewed zero hits only.",
            "Native gene names, ORFs, loci, fragment flags and versions remain reference metadata.",
            "Reference identity and database bibliography do not validate drug-specific resistance claims.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "new_primary_requests": 0,
            "primary_access_holds_preserved": True,
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
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check:
        if OUTPUT.read_text() != encoded:
            raise ValueError("saved FKS/FSK reference cohort differs from native replay")
    else:
        OUTPUT.write_text(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

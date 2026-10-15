"""Ground PBP reference names and taxa without identifying resistant alleles."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_complex_members as members
import audit_card_literature_expansion as literature

reference, require = members.reference, members.require
read_json = members.prior.mex.read_json
PREFIX = "research/2026-10-15-pbp-reference-context"
PLAN = Path(PREFIX + "-plan.json")
NATIVE = Path(PREFIX + "-native-plan.json")
OUTPUT = Path(PREFIX + ".json")
CACHE = Path("reports/resistance-grounding-2026-10-15-pbp-reference-context")
SCOPE = "ALL_CURRENT_PBP_LABELS_REFERENCE_METADATA_NOT_RESISTANT_ALLELES"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)


def parameters(taxid, strategy="full_name"):
    require(strategy in {"full_name", "pbp_alias"}, "unplanned query strategy")
    name = (
        'protein_name:"penicillin-binding"' if strategy == "full_name" else "(protein_name:pbp* OR gene:pbp*)"
    )
    return {
        "query": f"{name} AND taxonomy_id:{taxid} AND reviewed:true",
        "size": "500",
        "format": "json",
        "sort": "accession asc",
        "fields": FIELDS,
    }


def source_for(root, key, plan_path):
    return {
        "key": key,
        "plan": reference.pin(root, root / plan_path),
        "attempt": reference.pin(root, root / CACHE / (key + "-attempt.json")),
        "receipt": reference.pin(root, root / CACHE / (key + "-receipt.json")),
        "body": reference.pin(root, root / CACHE / (key + "-body.json")),
    }


def read_query(root, source, taxid):
    plan, attempt, receipt = [read_json(root, source[k]) for k in ("plan", "attempt", "receipt")]
    body = reference.check_pin(root, source["body"]).read_bytes()
    request = plan["requests"][source["key"]]
    expected = parameters(taxid, request.get("strategy", "full_name"))
    url = urlsplit(receipt["url"])
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    require(
        url.scheme == "https"
        and url.netloc == "rest.uniprot.org"
        and url.path == "/uniprotkb/search"
        and not url.fragment
        and parse_qs(url.query) == {k: [v] for k, v in expected.items()}
        and receipt["url"] == attempt["url"] == request["url"]
        and request["parameters"] == expected
        and attempt["plan_sha256"] == source["plan"]["sha256"]
        and attempt["retry_performed"] is receipt["retry_performed"] is False
        and receipt["redirects_followed"] is False
        and receipt["status"] == 200
        and receipt["bytes"] == len(body) <= plan["max_response_bytes"]
        and receipt["sha256"] == hashlib.sha256(body).hexdigest()
        and headers.get("x-uniprot-release") == "2026_03"
        and not headers.get("link")
        and not headers.get("location"),
        "native query identity, release or complete response changed",
    )
    entries = json.loads(body)["results"]
    require(
        len(entries) == len({e["primaryAccession"] for e in entries}) == int(headers["x-total-results"])
        and [e["primaryAccession"] for e in entries] == sorted(e["primaryAccession"] for e in entries)
        and all(e["entryType"] == "UniProtKB reviewed (Swiss-Prot)" for e in entries)
        and all(not {"sequence", "features", "comments"} & set(e) for e in entries),
        "query count, order, review status or metadata scope changed",
    )
    return entries


def name_fields(entry):
    """Top-level native names only, not catalytic subdomains or mentioned partners."""
    description = entry.get("proteinDescription", {})
    groups = [("recommendedName", description["recommendedName"])] if "recommendedName" in description else []
    groups += [
        (f"{kind}/{i}", row)
        for kind in ("alternativeNames", "submissionNames")
        for i, row in enumerate(description.get(kind, []))
    ]
    result = []
    for path, group in groups:
        if "fullName" in group:
            result.append({"field": path + "/fullName", "value": group["fullName"]["value"]})
        result.extend(
            {"field": path + f"/shortNames/{i}", "value": name["value"]}
            for i, name in enumerate(group.get("shortNames", []))
        )
    return result


def name_matches(entry, label):
    require(re.fullmatch(r"PBP[0-9]+[abx]?", label, re.I), "unsupported source PBP label")
    suffix = label[3:].casefold()
    wanted = {"pbp" + suffix, "penicillinbindingprotein" + suffix}
    return [row for row in name_fields(entry) if re.sub(r"[-\s]", "", row["value"]).casefold() in wanted]


def selected_cohort(root, plan, index):
    labels = {}
    with reference.check_pin(root, plan["source_inventory"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            term, label = row["determinant_id"], row["determinant_name"]
            require(term not in labels or labels[term] == label, "conflicting source labels")
            labels[term] = label
    selected = {
        t: label
        for t, label in labels.items()
        if t in index["terms"] and ("pbp" in label.casefold() or "penicillin-binding" in label.casefold())
    }
    require(len(selected) == 14 and set(selected) == set(plan["terms"]), "complete PBP cohort changed")
    for term, label in selected.items():
        parsed = re.fullmatch(r"([A-Z][a-z]+ [a-z]+) (PBP[0-9]+[abx]?) .+", label, re.I)
        require(
            label == plan["terms"][term]["source_label"]
            and hashlib.sha256(label.encode()).hexdigest() == index["terms"][term]["source_label_sha256"]
            and parsed
            and parsed.groups()
            == (plan["terms"][term]["source_species"], plan["terms"][term]["source_pbp_label"]),
            "source label binding changed",
        )
    return selected


def validate_assessment(notes):
    require(notes["scope"] == SCOPE, "assessment scope changed")
    for key in (
        "all_14_terms_primary_reviewed",
        "figures_visually_reviewed",
        "supplements_reviewed",
        "numeric_ast_exported",
        "operational_details_exported",
        "all_gene_or_allele_references_enumerated",
        "biological_curation_completed",
        "whole_record_primary_signoffs",
        "manual_primary_reading_independently_verified_by_code",
    ):
        require(notes[key] is False, "assessment scope promoted")
    contexts = notes["primary_contexts"]
    require(set(contexts) == {"29352811", "16940068"}, "primary coverage changed")
    h, n = contexts["29352811"], contexts["16940068"]
    require(
        h["term"] == "ARO:3004446"
        and h["doi"] == "10.1186/s13104-018-3169-0"
        and h["url"] == "https://link.springer.com/article/" + h["doi"]
        and h["gene"] == "ftsI"
        and h["protein_label"] == "PBP3"
        and h["species"] == "Haemophilus influenzae"
        and h["evidence_type"] == "ASSOCIATION_WITH_DISCORDANT_PHENOTYPES"
        and h["source_reported_reference_genome"] == "NC_000907"
        and h["reference_background"] == "Rd KW20",
        "Haemophilus primary identity changed",
    )
    require(
        h["chemical_qualification"]
        == {
            "record_identifier": "CHEBI:59343",
            "record_label": "cefditoren",
            "caption_label": "cefditoren pivoxil",
            "same_structure_established": False,
            "disposition": "PARENT_PRODRUG_SCOPE_UNRESOLVED_NO_PHENOTYPE_TRANSFER",
        },
        "compound scope changed",
    )
    require(
        all(
            h[k] is False
            for k in (
                "reference_genome_version_reported",
                "reference_genome_independently_verified",
                "reference_genome_assigned_to_tested_isolates",
                "exact_alleles_assigned",
                "independent_causality_assigned",
                "source_genotype_label_used_as_measured_resistance",
            )
        ),
        "primary association scope promoted",
    )
    require(
        n["term"] == "ARO:3003937"
        and n["doi"] == "10.1128/aac.00626-06"
        and n["url"] == "https://journals.asm.org/doi/full/" + n["doi"]
        and n["source_term_species_label"] == "Neisseria meningititis"
        and n["primary_experimental_species"] == "Neisseria gonorrhoeae"
        and n["disposition"] == "PRESERVE_SOURCE_FLAG_CITATION_SPECIES_CONFLICT_WITHHOLD_REFERENCE_JOIN"
        and all(
            n[k] is False
            for k in (
                "source_label_silently_corrected",
                "experimental_species_reassigned",
                "other_definition_citations_primary_reviewed",
            )
        ),
        "Neisseria scope changed",
    )
    require(
        all(c["source_kind"] == "PUBLISHER_HTML_TEXT" and c["locations"] for c in contexts.values()),
        "primary reading medium changed",
    )
    require(
        notes["access"]
        == {
            "web_search_queries": 4,
            "web_reader_open_operations": 2,
            "web_upstream_http_request_count_known": False,
            "ncbi_requests": 0,
            "outreach": False,
            "held_publication_sources_retried": False,
            "reuse_terms_review_resumed": False,
        },
        "access scope changed",
    )


def replay_sources(root, plan, frozen):
    taxonomy_plan = read_json(root, frozen["taxonomy_plan"])
    alias = read_json(root, taxonomy_plan["alias_plan"])
    prior_citations = read_json(root, taxonomy_plan["prior_citation_plan"])
    require(
        frozen["queries"] == taxonomy_plan["queries"]
        and frozen["citation_queries"] == taxonomy_plan["citation_queries"]
        and set(frozen["queries"]) == set(plan["requests"]) | set(alias["requests"]),
        "query scope changed",
    )
    pools, entries, queries = {}, {}, {}

    def accumulate(key, values):
        pools[key] = sorted(values)
        for accession, entry in values.items():
            require(not {"sequence", "features", "comments"} & set(entry), "unexpected operational fields")
            if accession in entries:
                fields = (
                    "primaryAccession",
                    "entryType",
                    "entryAudit",
                    "genes",
                    "organism",
                    "proteinDescription",
                    "references",
                )
                require(
                    all(entries[accession].get(k) == entry.get(k) for k in fields), "conflicting native entry"
                )
            else:
                entries[accession] = entry

    for key, item in frozen["queries"].items():
        values = read_query(root, item["source"], item["taxon_id"])
        accumulate(key, {e["primaryAccession"]: e for e in values})
        queries[key] = {
            "source": item["source"],
            "result_count": len(values),
            "accessions": pools[key],
            "complete_for_query": True,
            "biological_absence_inferred": False,
        }
    expected_pmids = {c.split(":")[1] for r in plan["terms"].values() for c in r["definition_citations"]}
    require(
        set(frozen["citation_queries"]) == expected_pmids and len(expected_pmids) == 29,
        "own citation coverage changed",
    )
    for pmid, item in frozen["citation_queries"].items():
        require(item == prior_citations["queries"][pmid], "cached citation plan changed")
        values, source = literature.read_query(root, root / item["directory"], pmid)
        require(
            source == item["query"] and source["complete_for_query"] and source["release"] == "2026_03",
            "cached citation query changed",
        )
        accumulate("citation-" + pmid, values)
        queries["citation-" + pmid] = source
    unmatched = {}
    for term, row in plan["terms"].items():
        tid = plan["species"][row["source_species"]]["taxon_id"]
        if tid and not any(
            name_matches(entries[a], row["source_pbp_label"]) for a in pools["proteins-" + tid]
        ):
            unmatched[term] = tid
    require(
        unmatched == alias["terms_without_full_name_match"]
        and {"aliases-" + t for t in unmatched.values()} == set(alias["requests"]),
        "complementary query selection changed",
    )
    return entries, pools, queries


def reference_disposition(source_species, reference_species):
    if source_species is None:
        return "SOURCE_NAME_UNRESOLVED_REFERENCE_JOIN_WITHHELD"
    if source_species != reference_species:
        return "DIFFERENT_SPECIES_REFERENCE_JOIN_WITHHELD"
    return "SAME_SPECIES_NAMED_PROTEIN_REFERENCE_NOT_EXPERIMENTAL_ALLELE"


def request_accounting(root, plan, frozen):
    tax_plan = read_json(root, frozen["taxonomy_plan"])
    require(
        tax_plan["original_plan"] == reference.pin(root, root / PLAN)
        and set(tax_plan["requests"]) == {"taxonomy-373153"},
        "taxonomy request scope changed",
    )
    network = read_json(
        root,
        {
            "path": PREFIX + "-network-plan.json",
            "sha256": frozen["queries"]["proteins-1313"]["source"]["plan"]["sha256"],
        },
    )
    failed, error = [read_json(root, network[k]) for k in ("prior_attempt", "prior_error")]
    require(
        network["prior_plan"] == reference.pin(root, root / PLAN)
        and network["requests"]["proteins-1313-network"] == plan["requests"]["proteins-1313"]
        and network["same_endpoint_and_parameters"] is True
        and failed["url"] == plan["requests"]["proteins-1313"]["url"]
        and failed["plan_sha256"] == network["prior_plan"]["sha256"]
        and error["type"] == "ConnectionError"
        and "NameResolutionError" in error["message"],
        "DNS attempt accounting changed",
    )
    expected = {row["source"]["key"] for row in frozen["queries"].values()} | {"taxonomy-373153"}
    received = {p.name.removesuffix("-receipt.json") for p in (root / CACHE).glob("*-receipt.json")}
    attempts = {p.name.removesuffix("-attempt.json") for p in (root / CACHE).glob("*-attempt.json")}
    errors = {p.name.removesuffix("-error.json") for p in (root / CACHE).glob("*-error.json")}
    require(
        received == expected and attempts == expected | {"proteins-1313"} and errors == {"proteins-1313"},
        "unaccounted native request",
    )
    source = frozen["taxonomy"]["373153"]
    attempt, receipt = [read_json(root, source[k]) for k in ("attempt", "receipt")]
    require(
        source["plan"] == frozen["taxonomy_plan"]
        and attempt["plan_sha256"] == source["plan"]["sha256"]
        and receipt["url"] == attempt["url"] == tax_plan["requests"]["taxonomy-373153"]["url"]
        and receipt["retry_performed"] is receipt["redirects_followed"] is False,
        "new taxonomy attempt changed",
    )
    for key, count in {
        "successful_new_http_responses": 13,
        "local_dns_failures": 1,
        "explicit_network_permission_retries": 1,
        "automatic_retries": 0,
        "ncbi_requests": 0,
    }.items():
        require(frozen[key] == count, "request totals changed")
    canary, aliases = [read_json(root, tax_plan[k]) for k in ("canary", "alias_canary")]
    require(
        canary["source"] == frozen["queries"]["proteins-1313"]["source"]
        and aliases["source"] == frozen["queries"]["aliases-1280"]["source"]
        and canary["approved_for_metadata_requests"] is aliases["approved_for_remaining_queries"] is True
        and canary["approved_for_experimental_assignment"]
        is aliases["approved_for_experimental_assignment"]
        is False,
        "canary scope changed",
    )
    return {
        "successful_http_responses": 13,
        "local_dns_failures_without_http_response": 1,
        "explicit_network_permission_retries": 1,
        "automatic_retries": 0,
        "ncbi_requests": 0,
        "canary": tax_plan["canary"],
        "alias_canary": tax_plan["alias_canary"],
        "network_retry_plan": network,
    }


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    frozen = json.loads((root / NATIVE).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["issue_1040"] == "DEFERRED"
        and plan["reuse_terms_review_resumed"] is plan["unreviewed_fallback_automatic"] is False
        and plan["ncbi_requests"]
        == plan["biological_records_changed"]
        == plan["exact_alleles_assigned"]
        == 0,
        "investigation scope changed",
    )
    assessment = read_json(root, frozen["assessment"])
    validate_assessment(assessment)
    index, update = [read_json(root, plan["inputs"][k]) for k in ("index", "corpus_update")]
    labels = selected_cohort(root, plan, index)
    definitions = read_json(root, plan["definition_citations"])
    records, claims = members.current_context(root, index, update, set(labels), labels)
    require(len(records) == 12 and len(claims) == 25, "claim coverage changed")
    entries, pools, queries = replay_sources(root, plan, frozen)
    accounting = request_accounting(root, plan, frozen)
    source_species, species_sources = {}, {}
    require(
        set(plan["species"]) == {r["source_species"] for r in plan["terms"].values()},
        "species coverage changed",
    )
    for name, row in plan["species"].items():
        if row["taxon_id"] is None:
            require(
                name == "Neisseria meningititis" and row["source"] is None, "unresolved source name changed"
            )
            source_species[name] = None
            continue
        taxon, provenance = members.prior.lineages.native_taxon(
            root, row["source"], row["taxon_id"], "2026_03"
        )
        require(
            taxon["scientificName"] == name and taxon["rank"] == "species", "source species binding changed"
        )
        source_species[name] = members.prior.lineages.identity(taxon)
        species_sources[name] = provenance
    taxa, tax_sources = {}, {}
    for tid, source in frozen["taxonomy"].items():
        taxa[tid], tax_sources[tid] = members.prior.lineages.native_taxon(root, source, tid, "2026_03")
    terms, views = {}, {}
    for term, row in plan["terms"].items():
        require(
            row["definition_citations"] == definitions["terms"][term]["definition_citation_ids"]
            and not index["terms"][term]["links"],
            "source citations or old reference scope changed",
        )
        species = source_species[row["source_species"]]
        tid = str(species["taxonId"]) if species else None
        keys = [key for key, item in frozen["queries"].items() if item["taxon_id"] == tid]
        keys += ["citation-" + c.split(":")[1] for c in row["definition_citations"]]
        candidates = []
        for accession in sorted({a for key in keys for a in pools[key]}):
            entry = entries[accession]
            matches = name_matches(entry, row["source_pbp_label"])
            if not matches:
                continue
            identifier = "UniProtKB:" + accession
            view = members.member_reference(entry, taxa[str(entry["organism"]["taxonId"])])
            views[identifier] = view
            disposition = reference_disposition(species, view["reference_taxonomy"]["species"])
            candidates.append(
                {
                    "protein_accession": identifier,
                    "native_name_matches": matches,
                    "query_keys": [key for key in keys if accession in pools[key]],
                    "disposition": disposition,
                    "qualified_reference": disposition.startswith("SAME_SPECIES_"),
                    "experimental_allele_assigned": False,
                }
            )
        qualified = [c["protein_accession"] for c in candidates if c["qualified_reference"]]
        terms[term] = {
            **row,
            "source_label_sha256": index["terms"][term]["source_label_sha256"],
            "source_species_reference": species,
            "record_memberships": index["terms"][term]["record_memberships"],
            "query_keys": keys,
            "query_pool_size": len({a for key in keys for a in pools[key]}),
            "name_matched_candidates": candidates,
            "qualified_reference_accessions": qualified,
            "biological_absence_inferred": False,
            "experimental_subject_assigned": False,
            "status": "QUALIFIED_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_IDENTITY"
            if qualified
            else "SOURCE_NAME_UNRESOLVED_CANDIDATES_WITHHELD"
            if species is None
            else "NO_QUALIFIED_MATCH_IN_SELECTED_QUERIES_NOT_BIOLOGICAL_ABSENCE",
        }
    require(
        set(views)
        == {"UniProtKB:" + a for a in read_json(root, frozen["taxonomy_plan"])["matched_accessions"]}
        and {str(v["reference_taxonomy"]["taxon_id"].split(":")[1]) for v in views.values()} == set(taxa),
        "matched reference or taxonomy coverage changed",
    )
    for pmid, context in assessment["primary_contexts"].items():
        require(
            "PMID:" + pmid in terms[context["term"]]["definition_citations"],
            "primary citation ownership changed",
        )
    dispositions = []
    by_id = {r["identifier"]: r for r in records}
    for claim in claims:
        term, rid = claim["aro_id"], claim["record_identifier"]
        flags = []
        if term == "ARO:3004446":
            flags.append("STUDY_HAS_AMPICILLIN_DISCORDANCE_AND_CORRELATED_VARIANTS_NOT_INDIVIDUAL_CAUSALITY")
            if rid == "CHEBI:59343":
                require(by_id[rid]["label"] == "cefditoren", "compound identity changed")
                flags.append("PAPER_CAPTION_NAMES_PRODRUG_NOT_VERIFIED_PARENT_STRUCTURE")
        if term == "ARO:3003937":
            flags.append("OWN_CITATION_HAS_DIFFERENT_EXPERIMENTAL_SPECIES")
        if term == "ARO:3007421":
            require(by_id[rid]["label"] == "ceftazidime", "combination-member record changed")
            flags.append("SOURCE_TERM_NAMES_COMBINATION_NOT_SINGLE_AGENT_EVIDENCE")
        dispositions.append(
            {
                **claim,
                "qualified_reference_accessions": terms[term]["qualified_reference_accessions"],
                "qualifications": flags,
                "source_claim_preserved": True,
                "exact_allele_assigned": False,
                "whole_claim_primary_signoff": False,
            }
        )
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "native_plan": reference.pin(root, root / NATIVE),
        "assessment": frozen["assessment"],
        "inputs": plan["inputs"],
        "records": records,
        "claims": claims,
        "claim_dispositions": dispositions,
        "terms": terms,
        "reference_views": views,
        "source_species_native_sources": species_sources,
        "reference_taxonomy_sources": tax_sources,
        "queries": queries,
        "request_accounting": accounting,
        "summary": {
            "terms": len(terms),
            "complete_records_read": len(records),
            "source_claims": len(claims),
            "named_source_species_grounded": len(species_sources),
            "source_names_unresolved": 1,
            "native_name_matched_entries": len(views),
            "native_reference_taxa": len(taxa),
            "qualified_reference_entries": len(
                {a for t in terms.values() for a in t["qualified_reference_accessions"]}
            ),
            "terms_with_qualified_reference_context": sum(
                bool(t["qualified_reference_accessions"]) for t in terms.values()
            ),
            "claims_with_qualified_reference_context": sum(
                bool(c["qualified_reference_accessions"]) for c in dispositions
            ),
            "withheld_name_matched_candidates": sum(
                not c["qualified_reference"] for t in terms.values() for c in t["name_matched_candidates"]
            ),
            "complete_new_protein_queries": len(frozen["queries"]),
            "reused_citation_queries": len(frozen["citation_queries"]),
            "selected_primary_text_contexts_reviewed": 2,
            "claims_with_scope_qualifications": sum(bool(c["qualifications"]) for c in dispositions),
            "corpus_records_hash_checked": 2939,
        },
        "limits": {
            **members.prior.mex.LIMITS,
            "new_primary_results_reviews": 2,
            "reviewed_query_subset_is_exhaustive_gene_family_coverage": False,
            "manual_primary_reading_verified_by_code": False,
            "numeric_ast_exports": 0,
            "operational_exports": False,
            "new_taxonomy_responses": 1,
            "primary_figures_and_supplements_reviewed": False,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; primary publications separately cited in assessment.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
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

"""Resolve remaining source-name strings without assigning experimental subjects."""

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_gene_reference_followup as prior

reference, require, read_json = prior.reference, prior.require, prior.read_json
PREFIX = "research/2026-10-15-card-unresolved-name-context"
PLAN, OUTPUT = Path(PREFIX + "-plan.json"), Path(PREFIX + ".json")
CANARY = Path(PREFIX + "-canary.json")
SCOPE = "UNRESOLVED_SOURCE_NAMES_NOT_EXPERIMENTAL_SUBJECTS"
CONTEXTS = {
    "Ethambutol resistant": "PHENOTYPE_WORDING_NOT_AN_ORGANISM_NAME",
    "Kanamycin resistant": "PHENOTYPE_WORDING_NOT_AN_ORGANISM_NAME",
    "Salmonella serovars": "COLLECTIVE_GROUP_NOT_ONE_SPECIES_OR_ISOLATE",
}


def resolve(payload, name):
    entries = payload["results"]
    require(isinstance(entries, list), "taxonomy results must be a list")
    seen, candidates, accepted = set(), [], []
    for node in entries:
        identity = prior.lineages.identity(node)
        require(
            identity["taxonId"] not in seen and type(node.get("active")) is bool,
            "duplicate taxon or invalid activity status",
        )
        seen.add(identity["taxonId"])
        for field in ("synonyms", "otherNames"):
            require(
                isinstance(node.get(field, []), list)
                and all(isinstance(v, str) and v for v in node.get(field, [])),
                "invalid taxonomy name list",
            )
        fields = (
            [{"field": "scientificName", "value": node["scientificName"]}]
            if name.casefold() == node["scientificName"].casefold()
            else []
        )
        fields += [
            {"field": f"synonyms/{i}", "value": value}
            for i, value in enumerate(node.get("synonyms", []))
            if name.casefold() == value.casefold()
        ]
        candidate = {
            "identity": identity,
            "active": node["active"],
            "exact_name_fields": fields,
            "other_name_fields": [
                {"field": f"otherNames/{i}", "value": value}
                for i, value in enumerate(node.get("otherNames", []))
                if name.casefold() == value.casefold()
            ],
            "accepted_species_name": bool(fields and node["active"] and node["rank"] == "species"),
        }
        if node["active"]:
            lineage, species = prior.lineages.lineage(node)
            candidate["reference_lineage"] = lineage
            candidate["species_ancestor"] = species
        candidates.append(candidate)
        if candidate["accepted_species_name"]:
            accepted.append(candidate)
    return {
        "source_name": name,
        "status": "EXACT_ACTIVE_SPECIES_NAME"
        if len(accepted) == 1
        else "AMBIGUOUS_EXACT_ACTIVE_SPECIES_NAMES"
        if accepted
        else "NO_EXACT_ACTIVE_SPECIES_NAME",
        "selected_reference_species": accepted[0] if len(accepted) == 1 else None,
        "candidates": sorted(candidates, key=lambda c: c["identity"]["taxonId"]),
        "result_count": len(entries),
        "exact_species_match_count": len(accepted),
        "biological_absence_inferred": False,
        "experimental_subject_assignment": False,
        "protein_or_allele_assignment": None,
    }


def native_name(root, name, source, *, allow_unranked=False):
    url = urlsplit(source["url"])
    expected = {"query": [f'"{name}" AND rank:species'], "format": ["json"], "size": ["500"]}
    broad = {**expected, "query": [f'"{name}"']}
    require(
        url.path == "/taxonomy/search"
        and (
            parse_qs(url.query, keep_blank_values=True) == expected
            or (allow_unranked and parse_qs(url.query, keep_blank_values=True) == broad)
        ),
        "native name query differs from source label",
    )
    receipt = read_json(root, source.get("wrapper") or source["receipt"])
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    require(
        not headers.get("location")
        and receipt.get("retries", 0) == 0
        and not receipt.get("retry_performed", False)
        and not receipt.get("redirects_followed", False),
        "retried or redirected name evidence",
    )
    payload, provenance = prior.prior.members.screen.read_source(root, source)
    require(len(payload["results"]) <= 500, "oversized name result set")
    return resolve(payload, name), provenance


def requests(root, plan):
    directory = root / plan["cache_directory"]
    plan_pin = reference.pin(root, root / PLAN)
    inspection = json.loads((root / CANARY).read_bytes())
    require(
        plan["canary"] in plan["requests"]
        and inspection["plan"] == plan_pin
        and inspection["approved_for_remaining_queries"] is True
        and inspection["experimental_identity_assignments"] is False,
        "missing or changed canary approval",
    )
    require(not list(directory.glob("*-error.json")), "unresolved failed request")
    for suffix in ("attempt", "receipt"):
        require(
            {p.name for p in directory.glob(f"name-*-{suffix}.json")}
            == {f"{key}-{suffix}.json" for key in plan["requests"]},
            "unaccounted or missing name request",
        )
    result, sources = {}, {}
    for key, item in sorted(plan["requests"].items()):
        require(key == "name-" + item["name"].lower().replace(" ", "-"), "request key changed")
        attempt_path, receipt_path = [directory / (key + f"-{kind}.json") for kind in ("attempt", "receipt")]
        attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
        require(
            attempt["key"] == key
            and attempt["plan"] == plan_pin
            and attempt["url"] == receipt["url"] == item["url"]
            and attempt["retries"] == attempt["redirects_followed"] == 0
            and receipt["bytes"] <= plan["max_response_bytes"]
            and parse_qs(urlsplit(item["url"]).query) == {k: [v] for k, v in item["parameters"].items()},
            "request attempt or response differs from plan",
        )
        pin = reference.pin(root, receipt_path)
        source = {"url": item["url"], "wrapper": pin}
        result[item["name"]], sources[item["name"]] = native_name(root, item["name"], source)
        sources[item["name"]]["attempt"] = reference.pin(root, attempt_path)
        if key == plan["canary"]:
            inspected = result[item["name"]]
            selected = inspected["selected_reference_species"]
            require(
                inspection["receipt"] == pin
                and inspection["result_count"] == inspected["result_count"]
                and inspection["exact_species_match_count"] == inspected["exact_species_match_count"]
                and selected is not None
                and inspection["selected_reference_taxon_id"] == str(selected["identity"]["taxonId"])
                and inspection["selected_reference_scientific_name"]
                == selected["identity"]["scientificName"],
                "canary native response changed",
            )
    return result, sources


def build(root):
    plan = json.loads((root / PLAN).read_bytes())
    require(
        plan["scope"] == SCOPE
        and plan["release"] == "2026_03"
        and plan["retries"] == plan["redirects_followed"] == 0
        and plan["non_individual_name_contexts"] == CONTEXTS
        and plan["constraints"]
        == {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "outreach": False,
            "reuse_terms_review_resumed": False,
            "biological_record_writes": False,
            "experimental_identity_assignments": False,
            "new_primary_reviews": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "planned scope changed",
    )
    checkpoint = read_json(root, plan["prior"])
    read_json(root, plan["prior_verification"])
    preflight = read_json(root, plan["prior_query_preflight"])
    selected = {
        t: r for t, r in checkpoint["terms"].items() if r["status"] == "SOURCE_NAME_UNRESOLVED_NOT_QUERIED"
    }
    require(plan["terms"] == selected and len(selected) == 43, "complete unresolved-name cohort changed")
    names = {r["tokens"]["species"] for r in selected.values()}
    new_names = {r["name"] for r in plan["requests"].values()}
    old_names = set(plan["reused_queries"])
    require(
        len(new_names) == len(plan["requests"]) == 8
        and len(old_names) == 7
        and not new_names & old_names
        and not (new_names | old_names) & set(CONTEXTS)
        and names == new_names | old_names | set(CONTEXTS)
        and preflight["ignored_files_included"] is True
        and preflight["new_names_without_prior_attempts"] == sorted(new_names)
        and preflight["reused_names"] == sorted(old_names),
        "name query accounting changed",
    )
    for item in preflight["matching_history"]:
        reference.check_pin(root, item["file"])
        require(
            item["name"] not in new_names and item["status"] in (None, 200),
            "new query retries prior name attempt or failed response",
        )
    ancestor = read_json(root, checkpoint["prior"])
    index, update = [read_json(root, ancestor["inputs"][k]) for k in ("index", "corpus_update")]
    records, claims = prior.prior.members.current_context(
        root, index, update, set(selected), {t: r["source_label"] for t, r in selected.items()}
    )
    require(records == plan["records"] and claims == plan["claims"], "claim or structure bindings changed")
    resolved, sources = requests(root, plan)
    for name, source in plan["reused_queries"].items():
        resolved[name], sources[name] = native_name(root, name, source, allow_unranked=True)
    for name in CONTEXTS:
        resolved[name] = {
            "source_name": name,
            "status": CONTEXTS[name],
            "selected_reference_species": None,
            "candidates": [],
            "result_count": None,
            "exact_species_match_count": None,
            "biological_absence_inferred": False,
            "experimental_subject_assignment": False,
            "protein_or_allele_assignment": None,
        }
    terms = {}
    for term, row in selected.items():
        name = row["tokens"]["species"]
        terms[term] = {
            "source_label": row["source_label"],
            "tokens": row["tokens"],
            "record_memberships": row["record_memberships"],
            "definition_citations": row["definition_citations"],
            "name_status": resolved[name]["status"],
            "reference_species": (resolved[name]["selected_reference_species"] or {}).get("identity"),
            "protein_reference_status": "NOT_QUERIED_BY_THIS_NAME_AUDIT",
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "whole_record_primary_review": "OPEN",
        }
    return {
        "date": plan["date"],
        "scope": SCOPE,
        "plan": reference.pin(root, root / PLAN),
        "prior": plan["prior"],
        "canary": reference.pin(root, root / CANARY),
        "records": records,
        "claims": claims,
        "terms": terms,
        "names": resolved,
        "native_sources": sources,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(records),
            "claims": len(claims),
            "terms": len(terms),
            "source_names": len(names),
            "new_name_queries": len(new_names),
            "reused_name_queries": len(old_names),
            "non_individual_name_strings": len(CONTEXTS),
            "resolved_reference_names": sum(
                r["selected_reference_species"] is not None for r in resolved.values()
            ),
            "resolved_reference_terms": sum(r["reference_species"] is not None for r in terms.values()),
            "name_status_counts": dict(sorted(Counter(r["status"] for r in resolved.values()).items())),
            "term_status_counts": dict(sorted(Counter(r["name_status"] for r in terms.values()).items())),
            "new_protein_queries": 0,
            "ncbi_requests": 0,
        },
        "limits": {
            **plan["constraints"],
            "prior_dossiers_rewritten": False,
            "other_names_are_explicit_taxonomic_synonyms": False,
            "source_name_spelling_silently_corrected": False,
            "native_taxonomy_proves_resistance": False,
            "whole_record_primary_signoffs": 0,
        },
        "attribution": "CARD/ARO and UniProt CC BY 4.0; source name context, not experimental identity.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    path = args.root / args.output
    if args.check or path.exists():
        require(path.read_bytes() == payload, "audit does not reproduce; preserve prior output")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()

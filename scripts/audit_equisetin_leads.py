"""Keep indexed activity, analogues and host metabolism separate from AMR alleles."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit

import audit_card_reference_lineages as lineages
import audit_equisetin_followup as previous
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source
from lxml import html

CACHE = Path("reports/resistance-grounding-2026-10-14-equisetin-leads")
OUTPUT = Path("research/2026-10-14-equisetin-leads-context.json")
COHORT_SHA = "f48c273bbc242761e0753150bf94e3088b363640295a483f1424f5b8fa235f91"
METADATA = {
    "2026": (
        "MED",
        "41317882",
        "10.1016/j.micpath.2025.108215",
        "da5294df86834e1447fe17c788497a145c810b34ca2325755929f56824b500bf",
    ),
    "2015": (
        "MED",
        "26431450",
        "10.4155/fmc.15.97",
        "ece1cd05a49c7c2c332995255f2636b8306f67960f5fd3025a01cb0d1f304e97",
    ),
    "AGR": ("AGR", "IND608566932", None, "1dfa7f400c05ad1b45b61bb9572f3304b24f609602dc643c2628bbd9880f306a"),
}
MARKERS = {
    "2026": ("multidrug-resistant Enterococcus faecalis", "without inducing resistance", "Transcriptomics"),
    "2015": ("small molecule mimics", "tetramate-containing natural products"),
    "AGR": ("insulin resistance", "3T3-L1 adipocytes", "AMPK pathway"),
}
PUBLISHER = "https://linkinghub.elsevier.com/retrieve/pii/S0882401025009404"
FINAL = "https://www.sciencedirect.com/science/article/pii/S0882401025009404?via%3Dihub"
LIBRARY = "https://www.tandfonline.com/doi/full/10.4155/fmc.15.97"
LOCATOR_SHA = "febf87187ba6af1369587b2dbd5afcdad2314cc486247249dddbda1c7d50d6a7"


def lookup_url(key):
    source, identifier, _, _ = METADATA[key]
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {
            "query": f"EXT_ID:{identifier} AND SRC:{source}",
            "resultType": "core",
            "format": "json",
            "pageSize": "1",
        }
    )


def project_metadata(payload, key):
    source, identifier, doi, _ = METADATA[key]
    request = payload.get("request", {})
    rows = payload.get("resultList", {}).get("result")
    query = f"EXT_ID:{identifier} AND SRC:{source}"
    if (
        type(payload.get("hitCount")) is not int
        or payload["hitCount"] != 1
        or not isinstance(rows, list)
        or len(rows) != 1
        or not isinstance(rows[0], dict)
        or request.get("queryString") != query
        or request.get("internalQuery") != query
        or request.get("resultType") != "CORE"
        or type(request.get("pageSize")) is not int
        or request["pageSize"] != 1
        or payload.get("nextCursorMark")
    ):
        raise ValueError("exact metadata lookup identity or completeness changed")
    row = rows[0]
    if (
        row.get("id") != identifier
        or row.get("source") != source
        or row.get("doi") != doi
        or row.get("pmid") != (identifier if source == "MED" else None)
        or row.get("pmcid") is not None
        or not isinstance(row.get("title"), str)
        or not row["title"].strip()
        or not isinstance(row.get("abstractText"), str)
        or any(marker not in row["abstractText"] for marker in MARKERS[key])
    ):
        raise ValueError("indexed identity or reviewed abstract context changed")
    locators = row.get("fullTextUrlList", {}).get("fullTextUrl", [])
    expected = (
        []
        if source == "AGR"
        else [
            {
                "availability": "Subscription required",
                "availabilityCode": "S",
                "documentStyle": "doi",
                "site": "DOI",
                "url": "https://doi.org/" + doi,
            }
        ]
    )
    if locators != expected or any(row.get(k) != "N" for k in ("isOpenAccess", "inEPMC", "inPMC")):
        raise ValueError("indexed primary-text availability changed")
    context = {
        "source_reference": source + ":" + identifier,
        "title": row["title"],
        "doi": "DOI:" + doi if doi else None,
        "abstract_sha256": hashlib.sha256(row["abstractText"].encode()).hexdigest(),
        "scope": "INDEXED_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW",
        "source_use": "REFERENCE_ONLY_NO_SOURCE_DATA_ADOPTION",
        "indexed_availability": {k: row[k] for k in ("isOpenAccess", "inEPMC", "inPMC")},
        "primary_results_figures_supplements_reviewed": False,
        "uniprot_or_exact_allele_assignment": None,
        "numeric_AST_or_source_abstract_text_exported": False,
    }
    if key == "2026":
        if (
            row.get("firstPublicationDate") != "2025-11-28"
            or row.get("pubYear") != "2026"
            or row.get("journalInfo", {}).get("printPublicationDate") != "2026-02-01"
        ):
            raise ValueError("electronic and issue publication dates changed")
        context.update(
            {
                "first_publication_date": row["firstPublicationDate"],
                "issue_date": "2026-02-01",
                "reported_activity_species": "Enterococcus faecalis",
                "MDR_label_establishes_equisetin_resistance": False,
                "transcriptomic_response_establishes_resistant_allele": False,
                "no_induced_resistance_statement_is_universal_absence_proof": False,
                "primary_results_disposition": "ACCESS_HOLD",
            }
        )
    elif key == "2015":
        context.update(
            {
                "context": "TETRAMATE_NATURAL_PRODUCT_MIMIC_LIBRARY",
                "analogue_activity_transferred_to_parent_equisetin": False,
                "resistant_parent_compound_allele_established": False,
                "primary_results_disposition": "ACCESS_HOLD",
            }
        )
    else:
        context.update(
            {
                "context": "HOST_ADIPOCYTE_METABOLISM_NOT_ANTIMICROBIAL_RESISTANCE",
                "native_DOI_PMID_PMC_crosswalk_supplied": False,
                "merged_with_MED38327434_or_counted_as_independent_replication": False,
                "host_metabolism_genes_assigned_as_microbe_resistance_determinants": False,
            }
        )
    return row, context


def locator_destination(payload):
    if hashlib.sha256(payload).hexdigest() != LOCATOR_SHA:
        raise ValueError("reviewed locator body changed")
    tree = html.fromstring(payload)
    values = tree.xpath('//meta[translate(@http-equiv,"REFSH","refsh")="refresh"]/@content')
    if len(values) != 1:
        raise ValueError("locator refresh absent or ambiguous")
    match = re.fullmatch(r"\d+;\s*url='([^']+)'", values[0], flags=re.IGNORECASE)
    if match is None:
        raise ValueError("locator refresh malformed")
    url = urljoin(PUBLISHER, match.group(1))
    parsed = urlsplit(url)
    parameters = parse_qs(parsed.query, keep_blank_values=True)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "linkinghub.elsevier.com"
        or parsed.path != "/retrieve/articleSelectSinglePerm"
        or parsed.fragment
        or set(parameters) != {"Redirect", "key"}
        or parameters["Redirect"] != [FINAL]
        or len(parameters["key"]) != 1
        or not parameters["key"][0]
    ):
        raise ValueError("native locator destination changed")
    return url


def ground_species(taxon):
    if (
        lineages.identity(taxon)
        != {
            "taxonId": 1351,
            "scientificName": "Enterococcus faecalis",
            "rank": "species",
        }
        or taxon.get("active") is not True
    ):
        raise ValueError("abstract species taxonomy changed")
    return {
        "source_name": "Enterococcus faecalis",
        "taxon_id": "NCBITaxon:1351",
        "rank": "species",
        "evidence_scope": "SPECIES_NAME_IN_INDEXED_ABSTRACT_NOT_PRIMARY_SUBJECT_VERIFICATION",
        "experimental_strain_taxon_genome_or_protein_assignment": None,
        "species_wide_or_equisetin_resistance_asserted": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"metadata-" + k for k in METADATA} | {
        "primary-2026-doi",
        "primary-2026-publisher",
        "primary-2026-locator",
        "primary-2026-final",
        "primary-2015-doi",
        "primary-2015-publisher",
    }
    if any(
        {p.name.removesuffix(s) for p in directory.glob("*" + s)} != keys
        for s in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen lead cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    inputs = {
        k: json.loads(reference.check_pin(root, cohort[k]).read_bytes())
        for k in ("prior", "discovery", "protected")
    }
    reference.check_pin(root, cohort["source_queue"])
    prior = inputs["prior"]
    if prior != previous.build(root) or cohort["record"] != prior["record"]:
        raise ValueError("prior checkpoint changed")
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(inputs["protected"].get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus preflight changed")
    sources = {}
    plans = {"2026": "request-plan.json", "2015": "followup-plan.json", "AGR": "remaining-metadata-plan.json"}
    rows, contexts = {}, {}
    for key, (_, _, _, checksum) in METADATA.items():
        source_key = "metadata-" + key
        sources[source_key] = planned_source(root, directory, source_key, plans[key], lookup_url(key))
        body = reference.check_pin(root, sources[source_key]["body"])
        if reference.digest(body) != checksum:
            raise ValueError("reviewed metadata response changed")
        rows[key], contexts[key] = project_metadata(json.loads(body.read_bytes()), key)

    def data(key, part):
        return json.loads(reference.check_pin(root, sources[key][part]).read_bytes())

    if data("metadata-2026", "plan").get("cohort") != reference.pin(root, cohort_path):
        raise ValueError("initial request cohort binding changed")
    for year, next_key in (("2026", "2015"), ("2015", "AGR")):
        review = reference.pin(root, directory / f"metadata-{year}-reviewed.json")
        source_pins = {k: sources["metadata-" + year][k] for k in ("body", "receipt")}
        plan = data("metadata-" + next_key, "plan")
        if (
            json.loads(reference.check_pin(root, review).read_bytes()).get("source") != source_pins
            or plan.get("canary_review") != review
            or plan.get("metadata_source") != source_pins
            or plan.get("discovery") != cohort["discovery"]
            or plan.get("next_discovery_lead") not in inputs["discovery"]["discovery"]["leads"]
            or plan["next_discovery_lead"].get("id") != METADATA[next_key][1]
            or plan.get("native_primary_locator") != rows[year]["fullTextUrlList"]["fullTextUrl"][0]
        ):
            raise ValueError("metadata canary or native locator provenance changed")
    urls = {
        "primary-2026-doi": "https://doi.org/" + METADATA["2026"][2],
        "primary-2015-doi": "https://doi.org/" + METADATA["2015"][2],
        "primary-2026-publisher": PUBLISHER,
        "primary-2026-final": FINAL,
        "primary-2015-publisher": LIBRARY,
    }
    for key in ("primary-2026-doi", "primary-2015-doi", "primary-2026-publisher"):
        plan = (
            "followup-plan.json"
            if key == "primary-2026-doi"
            else ("remaining-metadata-plan.json" if key == "primary-2015-doi" else key + "-plan.json")
        )
        sources[key] = planned_source(
            root, directory, key, plan, urls[key], (200 if key.endswith("publisher") else 302,)
        )
    urls["primary-2026-locator"] = locator_destination(
        reference.check_pin(root, sources["primary-2026-publisher"]["body"]).read_bytes()
    )
    for key, status in (
        ("primary-2026-locator", 301),
        ("primary-2026-final", 403),
        ("primary-2015-publisher", 403),
    ):
        sources[key] = planned_source(root, directory, key, key + "-plan.json", urls[key], (status,))
    for parent, child in (
        ("primary-2026-doi", "primary-2026-publisher"),
        ("primary-2026-locator", "primary-2026-final"),
        ("primary-2015-doi", "primary-2015-publisher"),
    ):
        plan = data(child, "plan")
        if (
            {k.lower(): v for k, v in data(parent, "receipt")["headers"].items()}.get("location")
            != urls[child]
            or plan.get("redirect_receipt") != sources[parent]["receipt"]
            or plan.get("manual_redirect_reviewed") is not True
        ):
            raise ValueError("manual HTTP redirect provenance changed")
    plan = data("primary-2026-locator", "plan")
    if plan.get("manual_redirect_reviewed") is not True or plan.get("native_html_refresh") != {
        k: sources["primary-2026-publisher"][k] for k in ("body", "receipt")
    }:
        raise ValueError("manual HTML redirect provenance changed")
    for key in ("primary-2026-locator", "primary-2026-final"):
        sources[key]["url"] = urlsplit(urls[key])._replace(query="").geturl()
        sources[key]["query_retained_only_in_private_receipt"] = True
    taxon, tax_source = lineages.native_taxon(root, prior["taxonomy_sources"]["1351"], "1351", "2026_03")
    dispositions = dict(prior["discovery_status"]["initial_candidate_dispositions"])
    dispositions.update(
        {
            "MED:41317882": "INDEXED_ACTIVITY_ABSTRACT_PRIMARY_RESULTS_ACCESS_HELD",
            "MED:26431450": "INDEXED_ANALOGUE_LIBRARY_ABSTRACT_PRIMARY_RESULTS_ACCESS_HELD",
            "AGR:IND608566932": "INDEXED_HOST_METABOLISM_ABSTRACT_CROSSWALK_UNRESOLVED",
        }
    )
    return {
        "date": "2026-10-14",
        "scope": "INDEXED_ABSTRACT_TRIAGE_NOT_PRIMARY_RESULTS_OR_RESISTANCE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "prior_checkpoint": cohort["prior"],
        "discovery_checkpoint": cohort["discovery"],
        "record": cohort["record"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "sources": sources,
        "indexed_contexts": contexts,
        "abstract_species": ground_species(taxon),
        "taxonomy_source": tax_source,
        "new_primary_holds": {"MED:41317882": "ACCESS_HOLD_HTTP_403", "MED:26431450": "ACCESS_HOLD_HTTP_403"},
        "prior_TA289_hold_preserved": True,
        "locator_HTTP_200_is_primary_text": False,
        "discovery_status": {
            "initial_candidate_identities": 8,
            "additional_primary_bibliography_leads": 1,
            "initial_candidate_dispositions": dispositions,
            "initial_candidates_without_followup_disposition": list(dispositions.values()).count(
                "UNASSESSED"
            ),
            "initial_candidates_primary_results_unreviewed_including_held_and_abstract_only": 6,
            "initial_candidate_primary_access_holds": 3,
            "new_primary_results_reviews": 0,
            "AGR_MED_same_title_records_merged_or_counted_as_replication": False,
        },
        "curation_decision": "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIERS",
        "limits": {
            "http_attempts": 9,
            "successful_metadata_lookups": 3,
            "manually_reviewed_redirect_hops": 4,
            "automatic_redirects": 0,
            "retries": 0,
            "native_taxonomy_responses_reused": 1,
            "new_uniprot_queries": 0,
            "biological_records_changed": 0,
            "figures_visually_reviewed": False,
            "supplements_reviewed": False,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "issue_1040": "DEFERRED",
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Equisetin indexed-lead checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "indexed_abstracts_reviewed": 3,
                "new_primary_access_holds": 2,
                "new_resistance_assertions": 0,
                "remaining_unassessed_original_leads": 2,
            }
        )
    )


if __name__ == "__main__":
    main()

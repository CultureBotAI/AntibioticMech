"""Separate a publication-linked hydrolase reference from co-cited proteins."""

import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-stth")
OUTPUT = Path("research/2026-10-14-stth-reference-context.json")
COHORT_SHA = "e7464ea9d5fae7aee223866fd1805ddaf0a206310a69a574842b8a205eef79ee"
DOI = "10.1074/jbc.m602294200"
PII = "S0021925820557074"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)
VERSIONS = {
    "Q1MW86": (58, 2),
    "Q1MW87": (46, 1),
    "C5NM84": (36, 1),
    "C5NM86": (47, 1),
    "C5NM87": (43, 1),
    "Q1MW85": (33, 2),
    "C5NM85": (74, 1),
}


def synonym_scope(taxon):
    if (
        lineages.identity(taxon)
        != {"taxonId": 1971, "scientificName": "Streptomyces noursei", "rank": "species"}
        or taxon.get("active") is not True
        or not isinstance(taxon.get("synonyms"), list)
        or "Streptomyces albulus" not in taxon.get("synonyms", [])
    ):
        raise ValueError("explicit reference species synonym changed")
    return {
        "reference_name": "Streptomyces albulus",
        "scientific_name": "Streptomyces noursei",
        "taxon_id": "NCBITaxon:1971",
        "rank": "species",
        "active": True,
        "match_basis": "EXACT_NATIVE_TAXONOMY_SYNONYM_NOT_PROTEIN_COMMON_NAME_ALONE",
        "experimental_strain_or_genome_resolved": False,
    }


def project_references(payload, headers, taxonomy):
    headers = {k.lower(): v for k, v in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != 7
        or not all(isinstance(row, dict) for row in payload["results"])
        or headers.get("x-total-results") != "7"
        or headers.get("link")
        or headers.get("x-uniprot-release") != "2026_03"
    ):
        raise ValueError("publication query incomplete or malformed")
    rows = payload["results"]
    if {row.get("primaryAccession") for row in rows} != set(VERSIONS):
        raise ValueError("publication reference membership changed")
    name = synonym_scope(taxonomy)
    shared, selected = [], None
    for entry in rows:
        accession = entry["primaryAccession"]
        reviewed = accession == "Q1MW86"
        kind = "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)"
        audit = entry["entryAudit"]
        if (
            {"sequence", "features", "comments"}.intersection(entry)
            or entry["entryType"] != kind
            or any(type(audit.get(k)) is not int for k in ("entryVersion", "sequenceVersion"))
            or (audit["entryVersion"], audit["sequenceVersion"]) != VERSIONS[accession]
            or type(entry["organism"].get("taxonId")) is not int
            or entry["organism"]["taxonId"] != 1971
            or entry["organism"]["scientificName"] != taxonomy["scientificName"]
        ):
            raise ValueError("reference metadata or payload scope changed")
        references = [
            r.get("citation", {}).get("citationCrossReferences", []) for r in entry.get("references", [])
        ]
        wanted = {("PubMed", "16641084"), ("DOI", DOI)}
        if not any(
            wanted <= {(r["database"], r["id"].lower() if r["database"] == "DOI" else r["id"]) for r in refs}
            for refs in references
        ):
            raise ValueError("shared publication identity changed")
        if reviewed:
            selected = reference.project_reference(entry, "sttH", 1971, taxonomy)
            if selected["gene_names"] != ["sttH"]:
                raise ValueError("focal gene identity changed")
            selected["reference_species_taxon_id"] = selected.pop("source_species_taxon_id")
        else:
            shared.append(
                {
                    "accession": "UniProtKB:" + accession,
                    "entry_type": kind,
                    "entry_version": audit["entryVersion"],
                    "sequence_version": audit["sequenceVersion"],
                    "reference_taxon_id": "NCBITaxon:1971",
                    "role": "SHARED_CITATION_NOT_SELECTED_AS_RESISTANCE_DETERMINANT",
                    "resistance_absence_inferred": False,
                }
            )
    return {
        "query_complete": True,
        "entries_checked": len(rows),
        "release": "2026_03",
        "selected_reference": {
            **selected,
            "role": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE",
            "primary_results_reviewed": False,
        },
        "other_citation_entries": sorted(shared, key=lambda row: row["accession"]),
        "name_resolution": name,
        "shared_citation_is_causality": False,
    }


def locator_destination(payload, base):
    tree = html.fromstring(payload)
    if tree.xpath("string(//title)").strip() != "Redirecting":
        raise ValueError("publisher locator identity changed")
    values = tree.xpath('//meta[translate(@http-equiv,"REFSH","refsh")="refresh"]/@content')
    if len(values) != 1:
        raise ValueError("publisher locator destination missing or ambiguous")
    match = re.fullmatch(r"\d+;\s*url='([^']+)'", values[0], flags=re.IGNORECASE)
    if match is None:
        raise ValueError("publisher locator refresh malformed")
    destination = urljoin(base, match.group(1))
    parsed = urlsplit(destination)
    params = parse_qs(parsed.query, keep_blank_values=True)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "linkinghub.elsevier.com"
        or parsed.path != "/retrieve/articleSelectPrefsTemp"
        or parsed.fragment
        or set(params) != {"Redirect", "key"}
        or params["Redirect"] != [f"https://jbc.org/retrieve/pii/{PII}"]
        or len(params["key"]) != 1
        or not params["key"][0]
    ):
        raise ValueError("publisher locator points outside the exact paper chain")
    return destination


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"reference-2006", "primary-doi", "primary-publisher", "primary-locator", "primary-jbc"}
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != keys
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen research cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("prior", "census", "protected", "discovery", "source_queue"):
        reference.check_pin(root, cohort[key])
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    if cohort["records"] != prior["records"] or len(cohort["records"]) != 3:
        raise ValueError("prior exact-structure cohort changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        if (
            record["identifier"] != row["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != row["standard_inchi_key"]
            or protected.get(row["path"]) != row["sha256"]
        ):
            raise ValueError("historical record identity changed")
    query = {"query": "lit_pubmed:16641084", "format": "json", "size": "500", "fields": FIELDS}
    urls = {
        "reference-2006": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(query),
        "primary-doi": "https://doi.org/" + DOI,
        "primary-publisher": f"https://linkinghub.elsevier.com/retrieve/pii/{PII}",
        "primary-jbc": f"https://jbc.org/retrieve/pii/{PII}",
    }
    sources = {
        key: planned_source(root, directory, key, "request-plan.json", urls[key], (status,))
        for key, status in (("reference-2006", 200), ("primary-doi", 302))
    }
    sources["primary-publisher"] = planned_source(
        root, directory, "primary-publisher", "primary-publisher-plan.json", urls["primary-publisher"]
    )
    body = reference.check_pin(root, sources["primary-publisher"]["body"]).read_bytes()
    urls["primary-locator"] = locator_destination(body, urls["primary-publisher"])
    for key, status in (("primary-locator", 302), ("primary-jbc", 403)):
        sources[key] = planned_source(root, directory, key, key + "-plan.json", urls[key], (status,))
    for parent, child in (("primary-doi", "primary-publisher"), ("primary-locator", "primary-jbc")):
        receipt = json.loads(reference.check_pin(root, sources[parent]["receipt"]).read_bytes())
        destination = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        plan = json.loads((directory / (child + "-plan.json")).read_bytes())
        if (
            destination != urls[child]
            or plan["redirect_receipt"] != sources[parent]["receipt"]
            or plan["manual_redirect_reviewed"] is not True
        ):
            raise ValueError("manual HTTP redirect provenance changed")
    html_plan = json.loads((directory / "primary-locator-plan.json").read_bytes())
    if html_plan.get("manual_redirect_reviewed") is not True or html_plan["html_redirect_source"] != {
        k: sources["primary-publisher"][k] for k in ("body", "receipt")
    }:
        raise ValueError("manual HTML redirect provenance changed")
    lineage_path = root / "research/2026-10-14-card-reference-lineages.json"
    if reference.digest(lineage_path) != protected[str(lineage_path.relative_to(root))]:
        raise ValueError("reference taxonomy checkpoint changed")
    taxonomy_checkpoint = json.loads(lineage_path.read_bytes())
    taxon, tax_source = lineages.native_taxon(
        root, taxonomy_checkpoint["taxa"]["1971"]["native_source"], "1971", "2026_03"
    )
    payload = json.loads(reference.check_pin(root, sources["reference-2006"]["body"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, sources["reference-2006"]["receipt"]).read_bytes())
    proteins = project_references(payload, receipt["headers"], taxon)
    sources["primary-locator"]["url"] = urlsplit(urls["primary-locator"])._replace(query="").geturl()
    sources["primary-locator"]["opaque_query_retained_only_in_private_receipt"] = True
    return {
        "date": "2026-10-14",
        "scope": "PUBLICATION_REFERENCE_AND_SPECIES_SYNONYM_NOT_EXPERIMENTAL_GROUNDING",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "prior_chemical_scope": cohort["prior"],
        "records": cohort["records"],
        "sources": sources,
        "reference_context": proteins,
        "reference_retrieved_at": receipt["retrieved_at"],
        "reference_taxonomy": tax_source,
        "taxonomy_checkpoint": reference.pin(root, lineage_path),
        "primary_access": {
            "reference": "PMID:16641084",
            "doi": "DOI:" + DOI,
            "locator_http_200_is_primary_text": False,
            "terminal_status": 403,
            "disposition": "ACCESS_HOLD",
            "primary_results_reviewed": False,
            "retry_or_alternate_route_attempted": False,
        },
        "unreviewed_bibliography_leads": ["PMID:19897889"],
        "curation_decision": "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_IDENTIFIER",
        "limits": {
            "scientific_http_attempts": len(keys),
            "manually_inspected_redirect_hops": 3,
            "retries": 0,
            "automatic_redirects": 0,
            "native_taxonomy_responses_reused": 1,
            "biological_records_changed": 0,
            "experimental_allele_assignments": 0,
            "experimental_genome_assignments": 0,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("SttH reference checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "publication_entries_checked": 7,
                "focal_reference_candidates": 1,
                "shared_citation_entries_not_promoted": 6,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()

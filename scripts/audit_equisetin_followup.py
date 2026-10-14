"""Separate host metabolism, biochemical targets and experimental resistance."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_equisetin_context as previous
import audit_stth_reference as metadata
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source
from lxml import etree

CACHE = Path("reports/resistance-grounding-2026-10-14-ta289")
OUTPUT = Path("research/2026-10-14-equisetin-followup-context.json")
COHORT_SHA = "642c402c0cdeaafb83ffd297b30577b807709106e1dad92f0dbd6cbdfd5a1301"
PUBLISHER = "https://academic.oup.com/molecular-omics/article/9/8/2125/8348375"
ARTICLES = {
    "2024": (
        "38327434",
        "PMC10847917",
        "10.1016/j.heliyon.2024.e25458",
        "a90f4acebb62434c2d1861697aab1d8add592b98f8978fd9500c65f922f036c6",
    ),
    "2020": (
        "32470050",
        "PMC7259786",
        "10.1371/journal.pone.0233485",
        "15017d6d5ce400a443eca194d5f86fe9c5199287a1b19bba0d7370417d18d843",
    ),
}
QUERIES = {
    "reference-2020": "lit_pubmed:32470050",
    "reference-function": 'protein_name:"Biotin carboxylase" AND organism_id:562 AND reviewed:true',
    "reference-taxonomy": 'protein_name:"Biotin carboxylase" AND taxonomy_id:562 AND reviewed:true',
}
PROTEINS = {
    "P24182": (83333, 218, 2, ["accC", "fabG"], ["JW3224", "b3256"]),
    "Q8X9B6": (83334, 142, 1, ["accC"], ["ECs4128", "Z4616"]),
}
TAXA = {
    "562": ("Escherichia coli", "species"),
    "1280": ("Staphylococcus aureus", "species"),
    "1351": ("Enterococcus faecalis", "species"),
    "83333": ("Escherichia coli (strain K12)", "strain"),
    "83334": ("Escherichia coli O157:H7", "no rank"),
}
LOCATIONS = {
    "2024": {
        "insulin_context": ("/article/front/article-meta/abstract[1]", "insulin resistance"),
        "cell_origin": ("/article/body/sec[1]/p[4]", "originally cloned from mouse Swiss 3T3 cells"),
        "cell_model": ("/article/body/sec[2]/sec[2]/p", "3T3-L1 cells were purchased"),
        "host_endpoint": ("/article/body/sec[3]/sec[2]/p", "suppressed lipid accumulation"),
        "host_pathway": ("/article/body/sec[3]/sec[6]/p", "AMPK acts as a sensor"),
    },
    "2020": {
        "activity_scope": (
            "/article/body/sec[2]/sec[1]/p[1]",
            "methicillin-sensitive and methicillin-resistant",
        ),
        "other_compound_transcriptomics": (
            "/article/body/sec[2]/sec[2]/p[1]",
            "PYRC was used for preliminary transcriptomic analysis",
        ),
        "metal_context": ("/article/body/sec[2]/sec[3]/p", "metal homeostasis in EQI treated S. aureus"),
        "enzyme_origin": ("/article/body/sec[2]/sec[7]/p[1]", "recombinant E. coli ACC in vitro"),
        "component_comparison": ("/article/body/sec[2]/sec[7]/p[2]", "inhibition of CT was not observed"),
        "figure8_caption": (
            "/article/body/sec[2]/sec[7]/fig/caption",
            "biotin carboxylase (BC) and carboxyltransferase (CT)",
        ),
        "binding_unresolved": ("/article/body/sec[3]/p[6]", "Further research is required"),
        "compound_distinction": (
            "/article/body/sec[3]/p[7]",
            "decorated slightly differently with functional groups",
        ),
    },
}


def article_context(payload, year):
    pmid, pmcid, doi, checksum = ARTICLES[year]
    if hashlib.sha256(payload).hexdigest() != checksum:
        raise ValueError("reviewed primary article changed")
    root = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): n.text for n in root.xpath("./front/article-meta/article-id")}
    if any(ids.get(k) != v for k, v in (("pmid", pmid), ("pmcid", pmcid), ("doi", doi))):
        raise ValueError("primary publication identity changed")
    locations = {}
    for key, (xpath, marker) in LOCATIONS[year].items():
        nodes = root.xpath(xpath)
        if len(nodes) != 1:
            raise ValueError("reviewed source location absent or ambiguous")
        text = " ".join("".join(nodes[0].itertext()).split())
        if marker not in text:
            raise ValueError("reviewed source context changed")
        locations[key] = {"xpath": xpath, "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    context = {
        "reference": "PMID:" + pmid,
        "doi": "DOI:" + doi,
        "locations": locations,
        "scope": "SELECTED_PRIMARY_TEXT_NOT_COMPLETE_FIGURE_OR_SUPPLEMENT_REVIEW",
    }
    if year == "2024":
        context.update(
            {
                "context": "MOUSE_3T3_L1_ADIPOCYTE_METABOLISM_NOT_MICROBIAL_SUSCEPTIBILITY",
                "resistance_term": "INSULIN_RESISTANCE_BACKGROUND_NOT_ANTIMICROBIAL_RESISTANCE",
                "host_AMPK_results_are_antibiotic_resistance_evidence": False,
                "culture_antibiotics_are_susceptibility_observations": False,
                "source_license": "CC BY-NC-ND 4.0",
                "source_use": "REFERENCE_ONLY_NO_SOURCE_DATA_ADOPTION",
                "source_text_or_figures_redistributed": False,
            }
        )
    else:
        context.update(
            {
                "context": "ACTIVITY_AND_BIOCHEMICAL_TARGET_EVIDENCE_NOT_RESISTANT_ALLELE",
                "enzyme_donor_species": "Escherichia coli",
                "donor_strain_resolved": False,
                "inhibited_component": "biotin carboxylase",
                "negative_comparator": "carboxyltransferase not inhibited in the reported comparison",
                "exact_binding_interaction_resolved": False,
                "source_IC90_converted_to_MIC": False,
                "resistance_to_other_antibiotics_transferred_to_equisetin": False,
                "PYRC_transcriptomics_transferred_to_equisetin": False,
                "other_ACC_inhibitor_alleles_transferred_to_equisetin": False,
                "TA289_or_pyrrolocin_C_equated_to_equisetin": False,
                "2021_B_subtilis_modulation_and_2020_S_aureus_contexts_equated": False,
                "complete_common_mechanism_or_genetic_causality_established": False,
                "exact_tested_chemical_structure_independently_verified": False,
                "source_license": "CC BY 4.0",
            }
        )
    return root, context


def bibliography_lead(root):
    refs = root.xpath('.//ref[@id="bib24"]')
    if len(refs) != 1:
        raise ValueError("native bibliography reference absent or ambiguous")
    items = refs[0].xpath(
        './/ext-link[@ext-link-type="doi" or @ext-link-type="pmid" or @ext-link-type="pmcid"]'
    )
    values = {n.get("ext-link-type"): n.get("{http://www.w3.org/1999/xlink}href") for n in items}
    expected = {"doi": ARTICLES["2020"][2], "pmid": ARTICLES["2020"][0], "pmcid": ARTICLES["2020"][1]}
    if len(items) != 3 or values != expected:
        raise ValueError("native bibliography identity changed")
    return values


def complete_query(payload, headers, count):
    headers = {k.lower(): v for k, v in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != count
        or headers.get("x-total-results") != str(count)
        or headers.get("link")
        or headers.get("x-uniprot-release") != "2026_03"
    ):
        raise ValueError("reference query incomplete or malformed")
    return payload["results"]


def project_references(payload, headers, taxonomy):
    entries = complete_query(payload, headers, 2)
    if not all(isinstance(e, dict) for e in entries) or {e.get("primaryAccession") for e in entries} != set(
        PROTEINS
    ):
        raise ValueError("reference membership changed")
    projected = []
    for entry in entries:
        accession = entry["primaryAccession"]
        taxid, version, sequence_version, genes, loci = PROTEINS[accession]
        taxon = taxonomy[str(taxid)]
        name, rank = TAXA[str(taxid)]
        if (
            {"sequence", "features", "comments"}.intersection(entry)
            or lineages.identity(taxon) != {"taxonId": taxid, "scientificName": name, "rank": rank}
            or entry["organism"].get("taxonId") != taxid
            or entry["organism"].get("scientificName") != name
        ):
            raise ValueError("reference taxonomy or payload scope changed")
        item = reference.project_reference(entry, "accC", 562, taxon)
        if (
            item["entry_version"] != version
            or item["sequence_version"] != sequence_version
            or item["gene_names"] != genes
            or item["ordered_locus_names"] != loci
            or item["protein_name"] != "Biotin carboxylase"
            or any(
                x == {"database": "PubMed", "id": "32470050"}
                for citation in item["bibliography"]
                for x in citation["identifiers"]
            )
        ):
            raise ValueError("component reference identity or citation membership changed")
        item["reference_species_taxon_id"] = item.pop("source_species_taxon_id")
        projected.append(
            {
                **item,
                "role": "FUNCTION_AND_TAXONOMY_REFERENCE_NOT_TESTED_ENZYME_OR_RESISTANT_ALLELE",
                "selected_pmid_in_returned_bibliography": False,
                "gene_symbol_is_verbatim_primary_paper_assignment": False,
            }
        )
    return sorted(projected, key=lambda p: p["protein_accession"])


def search_fields(payload):
    selected = []

    def collect(value):
        if isinstance(value, dict):
            if value.get("autoCompleteQueryTerm") in {"organism_id", "taxonomy_id"}:
                selected.append({k: value[k] for k in ("label", "term", "autoCompleteQueryTerm")})
            for child in value.values():
                collect(child)
        elif isinstance(value, list):
            for child in value:
                collect(child)

    collect(payload)
    expected = [
        {"label": "Organism [OS]", "term": "organism_name", "autoCompleteQueryTerm": "organism_id"},
        {"label": "Taxonomy [OC]", "term": "taxonomy_name", "autoCompleteQueryTerm": "taxonomy_id"},
    ]
    if sorted(selected, key=lambda x: x["label"]) != expected:
        raise ValueError("official search-field configuration changed")
    return expected


def build(root, directory=CACHE):
    directory = root / directory
    expected_keys = {
        "primary-doi",
        "primary-publisher",
        "article-2024",
        "article-2020",
        "search-fields",
    } | set(QUERIES)
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != expected_keys
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen follow-up cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("prior", "census", "protected", "source_queue"):
        reference.check_pin(root, cohort[key])
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    if prior != previous.build(root) or cohort["record"] != prior["record"]:
        raise ValueError("prior compound checkpoint changed")
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    urls = {
        "primary-doi": "https://doi.org/10.1039/c3mb70056a",
        "primary-publisher": PUBLISHER,
        "search-fields": "https://rest.uniprot.org/configure/uniprotkb/search-fields",
    }
    urls.update(
        {
            "article-" + year: f"https://www.ebi.ac.uk/europepmc/webservices/rest/{item[1]}/fullTextXML"
            for year, item in ARTICLES.items()
        }
    )
    urls.update(
        {
            key: "https://rest.uniprot.org/uniprotkb/search?"
            + urlencode({"query": query, "format": "json", "size": "500", "fields": metadata.FIELDS})
            for key, query in QUERIES.items()
        }
    )
    sources = {
        key: planned_source(
            root,
            directory,
            key,
            "request-plan.json" if key == "primary-doi" else key + "-plan.json",
            url,
            (302 if key == "primary-doi" else 403 if key == "primary-publisher" else 200,),
        )
        for key, url in urls.items()
    }

    def data(key, part):
        return json.loads(reference.check_pin(root, sources[key][part]).read_bytes())

    redirect, plan = data("primary-doi", "receipt"), data("primary-publisher", "plan")
    if (
        {k.lower(): v for k, v in redirect["headers"].items()}.get("location") != PUBLISHER
        or plan.get("redirect_receipt") != sources["primary-doi"]["receipt"]
        or plan.get("manual_redirect_reviewed") is not True
    ):
        raise ValueError("manual publisher redirect provenance changed")
    papers, trees = {}, {}
    for year in ARTICLES:
        trees[year], papers[year] = article_context(
            reference.check_pin(root, sources["article-" + year]["body"]).read_bytes(), year
        )
    lead = bibliography_lead(trees["2024"])
    plan2024, plan2020 = data("article-2024", "plan"), data("article-2020", "plan")
    if (
        plan2024.get("prior_checkpoint") != cohort["prior"]
        or plan2024.get("selected_citation") not in prior["discovery"]["leads"]
        or plan2024["selected_citation"].get("pmid") != ARTICLES["2024"][0]
        or plan2024.get("not_alternate_route_for_held_TA289_paper") is not True
        or plan2020.get("bibliography_source") != {k: sources["article-2024"][k] for k in ("body", "receipt")}
        or plan2020.get("selected_citation") != lead
        or plan2020.get("native_bibliography_ref_id") != "bib24"
    ):
        raise ValueError("distinct-study and bibliography request provenance changed")
    review_pins = {
        year: reference.pin(root, directory / f"article-{year}-reviewed.json") for year in ARTICLES
    }
    for year, item in review_pins.items():
        review = json.loads(reference.check_pin(root, item).read_bytes())
        if review.get("source") != {k: sources["article-" + year][k] for k in ("body", "receipt")}:
            raise ValueError("manual primary review source changed")
    if plan2020.get("canary_review") != review_pins["2024"] or any(
        data(k, "plan").get("primary_review") != review_pins["2020"] for k in QUERIES
    ):
        raise ValueError("primary review plan binding changed")
    if (
        data("reference-function", "plan").get("completed_publication_query")
        != sources["reference-2020"]["receipt"]
        or data("reference-function", "plan").get("provider_alternate_PMID_suggestion_followed") is not False
        or data("reference-taxonomy", "plan").get("completed_exact_organism_query")
        != sources["reference-function"]["receipt"]
        or data("reference-taxonomy", "plan").get("field_configuration")
        != {k: sources["search-fields"][k] for k in ("body", "receipt")}
    ):
        raise ValueError("query scope follow-up provenance changed")
    for key in ("reference-2020", "reference-function"):
        complete_query(data(key, "body"), data(key, "receipt")["headers"], 0)
    fields = search_fields(data("search-fields", "body"))
    taxonomy, tax_sources, tax_checkpoints = {}, {}, []
    for name in (
        "2026-10-14-card-reference-lineages.json",
        "2026-10-09-topoisomerase-reference-followup.json",
    ):
        path = root / "research" / name
        if reference.digest(path) != protected[str(path.relative_to(root))]:
            raise ValueError("taxonomy source checkpoint changed")
        tax_checkpoints.append(reference.pin(root, path))
    card, topo = [json.loads(reference.check_pin(root, p).read_bytes()) for p in tax_checkpoints]
    for taxid, (name, rank) in TAXA.items():
        item = (
            card["taxa"][taxid]["native_source"]
            if taxid != "83334"
            else {
                "body": topo["reference_taxon_requests"][taxid]["cache"],
                "receipt": topo["reference_taxon_requests"][taxid]["receipt"],
            }
        )
        taxonomy[taxid], tax_sources[taxid] = lineages.native_taxon(root, item, taxid, "2026_03")
        if lineages.identity(taxonomy[taxid]) != {
            "taxonId": int(taxid),
            "scientificName": name,
            "rank": rank,
        }:
            raise ValueError("assay or reference taxon identity changed")
    proteins = project_references(
        data("reference-taxonomy", "body"), data("reference-taxonomy", "receipt")["headers"], taxonomy
    )
    repairs = [
        reference.pin(root, directory / name)
        for name in ("local-helper-repair.json", "local-helper-repair-2.json")
    ]
    for item, key in zip(repairs, ("reference-2020", "search-fields"), strict=True):
        repair = json.loads(reference.check_pin(root, item).read_bytes())
        if (
            repair["saved_plan"] != sources[key]["plan"]
            or repair["completed_request"] != sources[key]["receipt"]
            or repair["request_retried"] is not False
            or repair["preparation_rerun"] is not False
            or repair["network_attempts_created_by_failed_plan_command"] != 0
        ):
            raise ValueError("local helper recovery provenance changed")
    return {
        "date": "2026-10-14",
        "scope": "PRIMARY_CONTEXT_AND_COMPONENT_REFERENCES_NOT_RESISTANCE_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "prior_checkpoint": cohort["prior"],
        "record": cohort["record"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "sources": sources,
        "primary_contexts": papers,
        "primary_review_receipts": review_pins,
        "bibliography_lead": {
            **lead,
            "native_reference_id": "bib24",
            "present_in_initial_eight_candidates": False,
        },
        "TA289": {
            "reference": "PMID:23715404",
            "doi": "DOI:10.1039/c3mb70056a",
            "status": 403,
            "disposition": "ACCESS_HOLD",
            "primary_results_reviewed": False,
            "alternate_route_or_retry": False,
            "compound_or_genetic_findings_transferred_to_equisetin": False,
        },
        "reference_proteins": proteins,
        "taxonomy_sources": tax_sources,
        "taxonomy_checkpoints": tax_checkpoints,
        "assay_species": [
            {
                "taxon_id": "NCBITaxon:" + k,
                "name": TAXA[k][0],
                "rank": "species",
                "experimental_strain_or_genome_assignment": None,
                "equisetin_resistant_isolate_asserted": False,
            }
            for k in ("1280", "1351", "562")
        ],
        "query_interpretation": {
            "publication_matches": 0,
            "exact_organism_matches": 0,
            "taxonomy_scope_matches": 2,
            "official_fields": fields,
            "empty_queries_establish_protein_absence": False,
            "provider_suggested_other_PMID_followed": False,
            "two_references_identify_one_experimental_protein": False,
        },
        "discovery_status": {
            "initial_candidate_identities": 8,
            "additional_primary_bibliography_leads": 1,
            "initial_candidates_without_followup_disposition": 5,
            "initial_candidates_primary_results_unreviewed_including_held": 6,
            "initial_candidate_dispositions": {
                key: {
                    "MED:34869220": "PRIOR_SCOPED_PRIMARY_TEXT_REVIEW",
                    "MED:38327434": "HOST_CONTEXT_NOT_ANTIMICROBIAL_RESISTANCE",
                    "MED:23715404": "ACCESS_HOLD_PRIMARY_RESULTS_UNREVIEWED",
                }.get(key, "UNASSESSED")
                for key in prior["discovery"]["retained_candidate_ids"]
            },
            "AGR_MED_same_title_records_merged_or_counted_as_replication": False,
        },
        "curation_decision": "NO_NEW_RESISTANCE_ASSERTION_OR_EXPERIMENTAL_PROTEIN_GENOME_ASSIGNMENT",
        "local_plan_helper_recoveries": repairs,
        "limits": {
            "http_attempts": 8,
            "api_configuration_requests": 1,
            "native_taxonomy_responses_reused": 5,
            "automatic_redirects": 0,
            "manually_inspected_redirect_hops": 1,
            "retries": 0,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "figures_visually_reviewed": False,
            "supplements_reviewed": False,
            "biological_records_changed": 0,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {
                "source": "Larson et al. 2020, PLOS ONE",
                "doi": "DOI:" + ARTICLES["2020"][2],
                "license": "CC BY 4.0",
            },
            {
                "source": "Zhong et al. 2024, Heliyon",
                "doi": "DOI:" + ARTICLES["2024"][2],
                "use": "REFERENCE_ONLY",
            },
            {"source": "UniProt Consortium", "license": "CC BY 4.0", "release": "2026_03"},
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        if OUTPUT.read_bytes() != payload:
            raise SystemExit("Equisetin follow-up checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "scoped_primary_contexts": 2,
                "component_reference_candidates": 2,
                "new_resistance_assertions": 0,
                "new_primary_access_holds": 1,
            }
        )
    )


if __name__ == "__main__":
    main()

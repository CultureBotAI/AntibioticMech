"""Replay cytochrome-b bibliographies and bounded primary-text context offline."""

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_beta_tubulin_evidence as bibliographic
import audit_card_cytochrome_b_references as prior
from audit_valinomycin_abcb1 import planned_source
from lxml import etree, html

reference, require = prior.reference, prior.require
CACHE = Path("reports/resistance-grounding-2026-10-14-cytochrome-b-evidence")
OUTPUT = Path("research/2026-10-14-cytochrome-b-evidence.json")
SCOPE = "CYTOCHROME_B_BIBLIOGRAPHIES_AND_SELECTED_PRIMARY_TEXT_NOT_RESISTANCE_ALLELE_SIGNOFF"
COHORT_SHA = "75a33d20a3a496dafa3f420ef48af3260f07c04990486a1f53090ce3ae5cf049"
ARTICLE = "https://europepmc.org/articles/PMC5311727"
XML_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5311727/fullTextXML"
SUPPLEMENT = "12864_2016_3480_MOESM1_ESM.xlsx"
PMIDS = ("28201983", "29996698")
PUBLICATIONS = {
    "28201983": {
        "title": "Comparative analysis of the mitochondrial genomes of Colletotrichum gloeosporioides "
        "sensu lato: insights into the evolution of a fungal species complex "
        "interacting with diverse plants.",
        "doi": "10.1186/s12864-016-3480-x",
        "pmcid": "PMC5311727",
        "pubYear": "2017",
        "isOpenAccess": "Y",
        "inEPMC": "Y",
    },
    "29996698": {
        "title": "Development of High-Throughput SNP Genotyping Assays for Rapid Detection of "
        "Strawberry Colletotrichum Species and the G143A Mutation.",
        "doi": "10.1094/phyto-04-18-0128-r",
        "pmcid": None,
        "pubYear": "2018",
        "isOpenAccess": "N",
        "inEPMC": "N",
    },
}
ABSTRACT_SHA = {
    "28201983": "0b4f5baa9e293a5a3118c3e50655493151dd7fe697706f4c1cb5a7cf0e24e9e2",
    "29996698": "d5990347ba3034f64539225a27d196c067f8f96c7b5a2037d4bf124916d26ad3",
}
BODY_SHA = {
    "metadata-28201983": "11d50f9b0ef2f5081ba810d34d3df4f328f316c85903ddb0dacfc8f0d09aa384",
    "metadata-29996698": "0ad0e128bb269298a30a3fdbbf551658a4c3c8763228b885eab403e35c709799",
    "primary-28201983": "f52cea864b969752375278f97b5e641a5472d6fc5ba6bb4ebc22873dab3e3117",
    "article-page": "5a2e062840d156415cd30661334c71bc53ca442a6a65f9b15dabf72cdb331a48",
}
PLAN_SHA = {
    "metadata-plan.json": "dca295b4880676f571b8627089d022585b5c225dd1ead318d9dcf9c1c1ad4b0a",
    "primary-plan.json": "e8c8880ffc1f727c97c59aaf3333743cc859dbc264f1184ccf4b5ca7f95a003d",
    "asset-discovery-plan.json": "bc9263e5ef00493c75570bc9e69dfb2aacc9a36af1b18b7ce62d5a22c99de2b0",
}
SECTION_SHA = {
    "Sec9": "fe9bbf0fee45c5f530b9e8dd62799e542813970bca3dcb782a762a753b737e6a",
    "Sec16": "fc984b2216953e260d7b123c6a06fa803009d55a47c5b8bb5284b56ed1cf9536",
    "FPar2": "421362ef1ddb77a14b08c40193e50f1686a4337be2b1e0ad8ac9c4cf740c92b4",
}
ISOLATE_GROUPS = {
    "C. fructicola": ["1104\u20137"],
    "C. aenigma": ["XY-15"],
    "C. gloeosporioides sensu stricto": ["LQ33"],
    "C. siamense s.l.": ["SQ01", "LQ22", "ZH01", "ZH02", "ZH03", "YT02"],
}


def metadata_url(pmid):
    require(pmid in PMIDS, "unplanned PMID")
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )


def project_metadata(payload, pmid):
    request = payload["request"]
    rows = payload["resultList"]["result"]
    require(
        type(payload["hitCount"]) is int
        and payload["hitCount"] == 1
        and not payload.get("nextCursorMark")
        and len(rows) == 1
        and request["queryString"] == "EXT_ID:" + pmid + " AND SRC:MED"
        and request["resultType"].lower() == "core"
        and type(request["pageSize"]) is int
        and request["pageSize"] == 1,
        "metadata query scope or completeness changed",
    )
    row = rows[0]
    require(
        row["id"] == row["pmid"] == pmid
        and row["source"] == "MED"
        and {k: row.get(k) for k in PUBLICATIONS[pmid]} == PUBLICATIONS[pmid]
        and hashlib.sha256(row["abstractText"].encode()).hexdigest() == ABSTRACT_SHA[pmid],
        "publication identity or inspected abstract changed",
    )
    return {
        "pmid": "PMID:" + pmid,
        **PUBLICATIONS[pmid],
        "abstract_sha256": ABSTRACT_SHA[pmid],
        "scope": "INDEXED_METADATA_AND_ABSTRACT_CONTEXT_NOT_PRIMARY_RESULTS",
        "primary_request_performed": pmid == "28201983",
        "abstract_is_experimental_crosswalk": False,
        "global_access_or_paywall_inferred": False,
    }


def project_primary(payload):
    require(hashlib.sha256(payload).hexdigest() == BODY_SHA["primary-28201983"], "primary XML changed")
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    for kind, value in (
        ("pmid", "28201983"),
        ("pmcid", "PMC5311727"),
        ("doi", PUBLICATIONS["28201983"]["doi"]),
    ):
        require(
            tree.xpath(f"./front/article-meta/article-id[@pub-id-type='{kind}']/text()") == [value],
            "primary article identity changed",
        )
    locations = {}
    for key, checksum in SECTION_SHA.items():
        matches = tree.xpath(f".//*[@id='{key}']")
        require(len(matches) == 1, "primary section missing or ambiguous")
        normalized = " ".join("".join(matches[0].itertext()).split())
        require(hashlib.sha256(normalized.encode()).hexdigest() == checksum, "reviewed section changed")
        locations[key] = {"xpath": tree.getroottree().getpath(matches[0]), "normalized_text_sha256": checksum}
    media = tree.xpath(".//media[@id='MOESM1']")
    require(
        len(media) == 1 and media[0].get("{http://www.w3.org/1999/xlink}href") == SUPPLEMENT,
        "native supplement declaration changed",
    )
    return {
        "pmid": "PMID:28201983",
        "doi": PUBLICATIONS["28201983"]["doi"],
        "status": "SELECTED_PRIMARY_TEXT_CONTEXT_REVIEWED_NOT_FULL_PAPER_SIGNOFF",
        "primary_xml_obtained": True,
        "locations": locations,
        "study_context": "MITOCHONDRIAL_GENOME_COMPARISON_AND_TAXONOMIC_PLACEMENT",
        "source_isolate_groups": [
            {
                "source_organism_label": label,
                "source_isolate_labels": isolates,
                "experimental_subject_taxon_id": None,
                "resistant_allele_assignment": None,
                "experimental_genome_accessions": [],
            }
            for label, isolates in ISOLATE_GROUPS.items()
        ],
        "siamense_sensu_lato_collapsed_to_current_species": False,
        "selected_text_establishes_drug_specific_resistance": False,
        "supplement": {
            "native_media_id": "MOESM1",
            "native_relative_href": SUPPLEMENT,
            "accession_locators": ["Additional file 1, Table S1", "Additional file 1, Table S3"],
            "retrieved": False,
            "reviewed": False,
            "genome_crosswalk_status": "UNVERIFIED_SUPPLEMENT_NOT_RETRIEVED",
        },
        "figures_visually_reviewed": False,
        "full_paper_signoff": False,
        "off_target_figure_accessions_used": False,
        "numeric_AST_exported": False,
        "absence_of_resistance_words_is_susceptibility": False,
    }


def project_hold(receipt, body):
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    require(
        receipt["url"] == ARTICLE
        and receipt["status"] == 403
        and receipt["retry_performed"] is receipt["redirects_followed"] is False
        and headers.get("cf-mitigated") == "challenge",
        "supplement discovery hold changed",
    )
    tree = html.fromstring(body)
    require(
        tree.xpath("//title/text()") == ["Just a moment..."]
        and not tree.xpath("//meta[@name='citation_title']"),
        "not the inspected challenge",
    )
    return {
        "url": ARTICLE,
        "http_status": 403,
        "retrieved_at": receipt["retrieved_at"],
        "status": "HTML_SUPPLEMENT_LINK_DISCOVERY_403_CHALLENGE_HELD_NO_RETRY",
        "primary_xml_obtained_before_hold": True,
        "supplement_retrieved": False,
        "retry_or_alternate_route_performed": False,
        "paywall_inferred": False,
        "global_inaccessibility_inferred": False,
        "negative_biological_evidence": False,
        "requires_new_direction_or_user_supplied_supplement": True,
    }


def request_context(root, directory):
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == set(BODY_SHA),
            "unexpected request or alternate route",
        )
    for filename, checksum in PLAN_SHA.items():
        require(reference.digest(directory / filename) == checksum, "request plan changed")
        plan = json.loads((directory / filename).read_bytes())
        require(plan["cohort"] == reference.pin(root, directory / "cohort.json"), "request cohort changed")
    sources, receipts, attempts = {}, {}, {}
    specs = [("metadata-" + p, "metadata-plan.json", metadata_url(p), 200) for p in PMIDS]
    specs += [
        ("primary-28201983", "primary-plan.json", XML_URL, 200),
        ("article-page", "asset-discovery-plan.json", ARTICLE, 403),
    ]
    for key, plan, url, status in specs:
        source = planned_source(root, directory, key, plan, url, (status,))
        require(source["body"]["sha256"] == BODY_SHA[key], "inspected response changed")
        sources[key] = source
        receipts[key] = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        attempts[key] = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
        require(
            datetime.fromisoformat(attempts[key]["started_at"])
            <= datetime.fromisoformat(receipts[key]["retrieved_at"]),
            "request chronology changed",
        )
    for before, after in zip(specs[:-1], specs[1:], strict=True):
        require(
            datetime.fromisoformat(receipts[before[0]]["retrieved_at"])
            <= datetime.fromisoformat(attempts[after[0]]["started_at"]),
            "request order changed",
        )
    review = json.loads((directory / "metadata-canary-review.json").read_bytes())
    require(
        review["body"] == sources["metadata-28201983"]["body"]
        and review["receipt"] == sources["metadata-28201983"]["receipt"]
        and review["plan"] == sources["metadata-28201983"]["plan"]
        and review["manually_inspected"] is review["publication_identity_verified"] is True
        and review["primary_results_reviewed"]
        is review["abstract_is_experimental_allele_assignment"]
        is False,
        "metadata canary changed",
    )
    return sources, project_hold(
        receipts["article-page"], (directory / "article-page-response.bin").read_bytes()
    )


def project_bibliographies(entries, old):
    require(set(entries) == set(old["proteins"]), "reference coverage changed")
    proteins = {}
    for accession, (entry, source) in sorted(entries.items()):
        saved = old["proteins"][accession]
        require(
            entry["primaryAccession"] == accession.removeprefix("UniProtKB:")
            and entry["entryAudit"]["entryVersion"] == saved["entry_version"]
            and entry["entryAudit"]["sequenceVersion"] == saved["sequence_version"]
            and entry["entryType"] == saved["entry_type"]
            and f"NCBITaxon:{entry['organism']['taxonId']}" == saved["reference_taxon_id"],
            "native reference identity changed",
        )
        proteins[accession] = {
            **{
                k: saved[k]
                for k in (
                    "entry_version",
                    "sequence_version",
                    "reference_taxon_id",
                    "reference_species_taxon_id",
                    "native_protein_flag",
                )
            },
            "source": source,
            "reference_rows": bibliographic.bibliography(entry),
            "experimental_subject_assignment": False,
            "exact_resistant_allele_assignment": None,
            "experimental_genome_assignment": None,
        }
    terms = {
        tid: {
            "source_label": term["source_label"],
            "record_memberships": term["record_memberships"],
            "source_definition_citations": term["definition_citation_ids"],
            "reference_proteins": [c["protein_accession"] for c in term["reference_candidates"]],
            "reference_citations_adopted_as_primary_support": False,
            "primary_review_status": "OPEN",
        }
        for tid, term in old["terms"].items()
    }
    require(all(not t["source_definition_citations"] for t in terms.values()), "source citations changed")
    return proteins, terms


def followup_links(proteins, metadata):
    links, discrepancies = [], []
    groups = {isolate: label for label, isolates in ISOLATE_GROUPS.items() for isolate in isolates}
    for accession, protein in proteins.items():
        for row in protein["reference_rows"]:
            ids = row["identifiers"]
            if {"database": "PubMed", "id": "28201983"} in ids:
                for label in row["reference_strain_comments"]:
                    require(label in groups, "unreviewed paper isolate label")
                    links.append(
                        {
                            "protein_accession": accession,
                            "native_reference_number": row["native_reference_number"],
                            "reference_strain_comment": label,
                            "paper_source_organism_label": groups[label],
                            "scope": "MATCHING_CITATION_LABEL_NOT_RESISTANCE_SUBJECT_OR_GENOME_CROSSWALK",
                        }
                    )
            if {"database": "PubMed", "id": "29996698"} in ids:
                (doi,) = [i["id"] for i in ids if i["database"] == "DOI"]
                require(
                    doi == ".1094/PHYTO-04-18-0128-R" and len(row["identifier_issues"]) == 1,
                    "native malformed DOI changed",
                )
                discrepancies.append(
                    {
                        "protein_accession": accession,
                        "native_reference_number": row["native_reference_number"],
                        "native_doi": doi,
                        "independent_metadata_pmid": "PMID:29996698",
                        "independently_reported_doi": metadata["29996698"]["doi"],
                        "native_or_prior_artifact_corrected": False,
                        "primary_resistance_result_verified": False,
                    }
                )
    return links, discrepancies


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in (
        "prior",
        "prior_verification",
        "prior_cohort",
        "census",
        "source_queue",
        "source_inventory",
        "definition_citations",
        "bibliography",
        "protected",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    old = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, cohort["prior_verification"]).read_bytes())
    require(
        cohort["prior"] in receipt["files"] and receipt["summary"] == old["summary"], "prior proof changed"
    )
    require(prior.build(root) == old, "complete native dossier or current corpus changed")
    require(
        cohort["records"] == old["records"]
        and cohort["claims"] == old["claims"]
        and cohort["terms"] == sorted(old["terms"])
        and cohort["proteins"] == sorted(old["proteins"])
        and cohort["pmids"] == list(PMIDS),
        "cohort coverage changed",
    )
    previous_cohort = json.loads(reference.check_pin(root, cohort["prior_cohort"]).read_bytes())
    named = prior.names(root, root / prior.CACHE, previous_cohort)
    selected = prior.selected_queries(root, root / prior.CACHE, previous_cohort, named)
    entries = {}
    for context in selected.values():
        source = context["queries"]["reviewed" if context["reviewed"] else "unreviewed"]["source"]
        for entry in context["entries"]:
            accession = "UniProtKB:" + entry["primaryAccession"]
            require(accession not in entries, "duplicate reference entry")
            entries[accession] = (entry, source)
    proteins, terms = project_bibliographies(entries, old)
    frozen = json.loads(reference.check_pin(root, cohort["bibliography"]).read_bytes())
    require(
        frozen
        == {
            "proteins": {k: v["reference_rows"] for k, v in proteins.items()},
            "sources": {k: v["source"] for k, v in proteins.items()},
        },
        "native bibliography changed",
    )
    sources, hold = request_context(root, directory)
    metadata = {
        p: {
            **project_metadata(json.loads((directory / ("metadata-" + p + "-response.bin")).read_bytes()), p),
            "source": sources["metadata-" + p],
        }
        for p in PMIDS
    }
    primary = project_primary((directory / "primary-28201983-response.bin").read_bytes())
    links, discrepancies = followup_links(proteins, metadata)
    rows = [r for p in proteins.values() for r in p["reference_rows"]]
    require(len(rows) == 11 and len(links) == 7 and len(discrepancies) == 2, "follow-up coverage changed")
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "inputs": {
            **{
                k: cohort[k]
                for k in (
                    "prior",
                    "prior_verification",
                    "census",
                    "source_queue",
                    "source_inventory",
                    "definition_citations",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
        },
        "records": old["records"],
        "claims": old["claims"],
        "terms": terms,
        "proteins": proteins,
        "publications": metadata,
        "request_sources": sources,
        "primary_context": {**primary, "source": sources["primary-28201983"]},
        "reference_comment_paper_label_matches": links,
        "doi_discrepancies": discrepancies,
        "supplement_discovery_hold": hold,
        "summary": {
            "corpus_records_hash_checked": 2939,
            "complete_records_read": len(old["records"]),
            "source_terms": len(terms),
            "source_claims": len(old["claims"]),
            "reference_proteins": len(proteins),
            "term_protein_links": sum(len(t["reference_proteins"]) for t in terms.values()),
            "native_reference_memberships": len(rows),
            "reference_types": dict(sorted(Counter(r["citation_type"] for r in rows).items())),
            "references_without_identifiers": sum(not r["identifiers"] for r in rows),
            "memberships_with_strain_comments": sum(bool(r["reference_strain_comments"]) for r in rows),
            "strain_comment_memberships": sum(len(r["reference_strain_comments"]) for r in rows),
            "unique_publications_with_identifiers": len(metadata),
            "doi_discrepancy_memberships": len(discrepancies),
            "paper_isolate_labels": sum(map(len, ISOLATE_GROUPS.values())),
            "reference_comment_label_matches": len(links),
            "new_network_requests": len(sources),
            "primary_xml_obtained": 1,
            "selected_primary_text_context_reviews": 1,
            "new_supplement_discovery_holds": 1,
            "new_experimental_assignments": 0,
            "new_verified_resistance_results": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limitations": [
            "Bibliography memberships and strain comments are metadata, "
            "not independent resistance observations.",
            "Submission titles without publication identifiers are retained, not treated as primary results.",
            "The primary paper's sensu-lato group is not an exact modern experimental TaxID assignment.",
            "Matching source isolate labels establish citation context only, "
            "not a protein/allele/genome crosswalk.",
            "Selected primary text was inspected; figures were not visually reviewed "
            "and supplements were not obtained.",
            "The 403 is a held HTML supplement-link discovery route, "
            "not absence of the already obtained primary XML.",
            "The 2018 publication has indexed abstract context only; its primary text remains unrequested.",
            "An independently reported DOI does not silently repair native UniProt metadata "
            "or verify resistance.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "outreach": 0,
            "biological_writes": False,
            "held_sources_retried": False,
            "operational_sequence_variant_or_protocol_fields_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD/ARO CC BY 4.0; UniProt Consortium release 2026_03 CC BY 4.0; "
        "Europe PMC metadata; primary study DOI:10.1186/s12864-016-3480-x, selected text context only.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or OUTPUT.exists():
        require(OUTPUT.read_bytes() == payload, "evidence follow-up does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

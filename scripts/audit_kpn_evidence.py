"""Replay Kpn complex evidence without inventing component or allele assignments."""

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_card_literature_expansion as literature
import audit_card_outer_membrane_references as outer
from audit_valinomycin_abcb1 import planned_source
from lxml import etree

from antibioticmech.activity_collections import load_record

reference, require = outer.reference, outer.require
CACHE = Path("reports/resistance-grounding-2026-10-15-kpn-evidence")
OUTPUT = Path("research/2026-10-15-kpn-evidence.json")
SCOPE = "KPN_COMPLEX_CITATION_CONTEXT_NOT_EXPERIMENTAL_PROTEIN_OR_ALLELE_GROUNDING"
COHORT_SHA = "b8d982cde092831a850850b65282a13092110ce5d0b86481ed0aa5c7b1f38be3"
TERMS = ("ARO:3004585", "ARO:3004598")
PMIDS = ("24823362", "23836167")
GENES = ("kpnG", "kpnH")
SELECT = re.compile(r"\bKpn[A-Z]", re.I)
XML_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4019481/fullTextXML"
PLAN_SHA = {
    "metadata-plan.json": "188958516ddfe2fbea0d4355ca3238f9d026b636c7b14d11a33d6f378729ecfd",
    "primary-plan.json": "06eda2795de11ab135b85c82280ec23f08ad349ea59b5d8d41eef7a325566a3b",
    "reviewed-plan.json": "bd34773b031965df6d48c54ae65a8a4230ebe3ebba25c58b6906f8cd6aefebab",
    "unreviewed-plan.json": "362cb71eda3f3a4c4b791859276d49fb0a6eac34e99e3ce9a54c184d575892ae",
}
BODY_SHA = {
    "metadata-24823362": "0b3ef9a528e055bb9d822de2a0be39de7eb068c47479eda91db0d33d115be9fc",
    "metadata-23836167": "4bff6b7b77a856d15254c41d7991b31d9ff947cd0fbaf37f85fc6928813eb806",
    "primary-24823362": "c8be97c1deb8b6af795b1c008330c198fb8f454391b46c708cf9ca9a164cd2be",
    **{
        kind + "-" + gene.lower(): "5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84"
        for kind in ("reviewed", "unreviewed")
        for gene in GENES
    },
}
PUBLICATIONS = {
    "24823362": {
        "title": "Role of novel multidrug efflux pump involved in drug resistance in Klebsiella pneumoniae.",
        "doi": "10.1371/journal.pone.0096288",
        "pmcid": "PMC4019481",
        "pubYear": "2014",
        "isOpenAccess": "Y",
        "inEPMC": "Y",
    },
    "23836167": {
        "title": "KpnEF, a new member of the Klebsiella pneumoniae cell envelope stress response regulon, "
        "is an SMR-type efflux pump involved in broad-spectrum antimicrobial resistance.",
        "doi": "10.1128/aac.02284-12",
        "pmcid": "PMC3754300",
        "pubYear": "2013",
        "isOpenAccess": "N",
        "inEPMC": "Y",
    },
}
ABSTRACT_SHA = {
    "24823362": "2dd8327e54ec4650c8ba1ee406dec49f886516efab9f463d54befaf95eb68619",
    "23836167": "7e284c3c15b0512d224e341e1d7f8b4184d2c4a48de2b4f7c8b9025ceb0f1ad5",
}
LOCATIONS = {
    "study_background": (
        "/article/body/sec[1]/p",
        "f17f13bbe5510f367a7f2cbf25352d3a05b2549aa81a484a3b074140fc773a2e",
    ),
    "component_names": (
        "/article/body/sec[3]/sec[1]/p",
        "9e0c67d1b95927ea9bc35bc2222c45d7e8bd35557e902945606cd983d7915c49",
    ),
    "genome_context": (
        "/article/body/sec[4]/p[1]",
        "f5f6225557d3467509cf3df41fce396a50db8fd10263a1d961ba50920a634f3f",
    ),
    "distinct_experimental_contexts": (
        "/article/body/sec[4]/p[2]",
        "e559c557e3b679f1fdc4edc04449b48279389b00d4314a6de9fadc7f27757532",
    ),
}


def metadata_url(pmid):
    require(pmid in PMIDS, "unplanned publication")
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )


def gene_url(gene, reviewed):
    require(gene in GENES and type(reviewed) is bool, "unplanned component query")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": f"gene_exact:{gene} AND taxonomy_id:573 AND reviewed:{str(reviewed).lower()}",
            "format": "json",
            "size": 500,
            "fields": outer.genes.FIELDS,
        }
    )


def project_metadata(payload, pmid):
    require(pmid in PMIDS, "unplanned publication")
    request, rows = payload["request"], payload["resultList"]["result"]
    require(
        type(payload["hitCount"]) is int
        and payload["hitCount"] == 1
        and len(rows) == 1
        and not payload.get("nextCursorMark")
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
        "scope": "INDEXED_METADATA_NOT_PRIMARY_RESULTS",
        "primary_requested": pmid == "24823362",
        "abstract_is_gene_crosswalk": False,
        "global_access_or_paywall_inferred": False,
        "access_denial_inferred": False,
    }


def project_primary(payload):
    require(hashlib.sha256(payload).hexdigest() == BODY_SHA["primary-24823362"], "primary XML changed")
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    for kind, value in (
        ("pmid", "24823362"),
        ("pmcid", "PMC4019481"),
        ("doi", PUBLICATIONS["24823362"]["doi"]),
    ):
        require(
            tree.xpath(f"./front/article-meta/article-id[@pub-id-type='{kind}']/text()") == [value],
            "primary article identity changed",
        )
    selected, locations = {}, {}
    for key, (xpath, checksum) in LOCATIONS.items():
        matches = tree.xpath(xpath)
        require(len(matches) == 1, "primary location missing or ambiguous")
        selected[key] = " ".join("".join(matches[0].itertext()).split())
        require(hashlib.sha256(selected[key].encode()).hexdigest() == checksum, "primary context changed")
        locations[key] = {"xpath": xpath, "normalized_text_sha256": checksum}
    require(
        "KpnG and KpnH proteins" in selected["component_names"]
        and "The KpnF also" in selected["component_names"]
        and "NTUH-K2044 (NC_012731.1)" in selected["genome_context"]
        and "E. coli KAM32" in selected["distinct_experimental_contexts"],
        "component, genome or host context changed",
    )
    matches = re.findall(r"\btolc\b", " ".join(tree.itertext()), re.I)
    require(not matches, "new literal TolC mention requires review")
    return {
        "pmid": "PMID:24823362",
        "status": "SELECTED_PRIMARY_CONTEXT_NOT_FULL_PAPER_SIGNOFF",
        "locations": locations,
        "paper_organism_name": "Klebsiella pneumoniae",
        "paper_background_strain": "NTUH-K2044",
        "source_component_names": ["KpnG", "KpnH"],
        "label_inconsistency": {
            "location": "component_names",
            "reported_label": "KpnF",
            "correction_inferred": False,
            "accepted_as_alias": False,
        },
        "homology_context": {
            "paper_comparison_label": "EmrAB",
            "accepted_as_exact_alias": False,
            "accession_substituted_by_homology": False,
        },
        "heterologous_host_context": {"paper_label": "E. coli KAM32", "merged_with_native_subject": False},
        "paper_reported_genome": {
            "namespace": "RefSeq",
            "accession": "NC_012731.1",
            "source_location": "genome_context",
            "scope": "PAPER_BACKGROUND_REFERENCE_NOT_TESTED_DERIVATIVE",
            "independently_verified": False,
            "ncbi_link_followed": False,
            "assembly_accession_inferred": False,
            "exact_resistance_allele_crosswalk": False,
        },
        "tolc_screen": {
            "pattern": r"\btolc\b",
            "case_insensitive": True,
            "match_count": len(matches),
            "scope": "RETRIEVED_XML_TEXT_ONLY_NOT_IMAGES_OR_SUPPLEMENTS",
            "establishes_absence": False,
            "invalidates_CARD_label": False,
            "supports_TolC_component_assignment": False,
        },
        "full_paper_signoff": False,
        "figures_visually_reviewed": False,
        "tables_reviewed_for_AST_curation": False,
        "supplements_reviewed": False,
        "protein_accession_assigned": None,
        "exact_resistant_allele_assigned": None,
        "experimental_strain_taxon_assigned": None,
        "experimental_genome_assigned": None,
        "numeric_AST_exported": False,
        "sequence_variant_protocol_exported": False,
    }


def request_specs():
    specs = [("metadata-" + p, "metadata-plan.json", metadata_url(p)) for p in PMIDS]
    specs.append(("primary-24823362", "primary-plan.json", XML_URL))
    specs.extend(
        (kind + "-" + g.lower(), kind + "-plan.json", gene_url(g, kind == "reviewed"))
        for kind in ("reviewed", "unreviewed")
        for g in GENES
    )
    return specs


def request_context(root, directory):
    specs = request_specs()
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == set(BODY_SHA),
            "unexpected request or alternate route",
        )
    for filename, checksum in PLAN_SHA.items():
        require(reference.digest(directory / filename) == checksum, "request plan changed")
        plan = json.loads((directory / filename).read_bytes())
        require(
            plan["cohort"] == reference.pin(root, directory / "cohort.json")
            and plan["automatic_redirects"] is plan["retry_performed"] is False
            and plan["ncbi_requests"] == 0
            and set(plan["requests"]) == {k for k, f, _ in specs if f == filename},
            "request constraints changed",
        )
    sources, previous_time = {}, None
    for key, filename, url in specs:
        source = planned_source(root, directory, key, filename, url)
        require(source["body"]["sha256"] == BODY_SHA[key], "inspected response changed")
        attempt = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
        receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        start, end = (
            datetime.fromisoformat(attempt["started_at"]),
            datetime.fromisoformat(receipt["retrieved_at"]),
        )
        require(
            start <= end and (previous_time is None or previous_time <= start), "request chronology changed"
        )
        sources[key], previous_time = source, end
    canary = json.loads((directory / "metadata-canary.json").read_bytes())
    require(
        all(canary[k] == sources["metadata-24823362"][k] for k in ("plan", "body", "receipt"))
        and canary["identity_checked"] is True
        and canary["continue_second_planned_metadata_request"] is True
        and canary["ncbi_requests"] == 0,
        "metadata canary changed",
    )
    primary = json.loads((directory / "primary-canary-review.json").read_bytes())
    require(
        all(primary[k] == sources["primary-24823362"][k] for k in ("plan", "body", "receipt"))
        and primary["identity_checked"] is primary["selected_context_manually_inspected"] is True
        and primary["source_components"] == ["KpnG", "KpnH"]
        and primary["results_label_inconsistency"] == "KpnF"
        and primary["inconsistency_silently_corrected"]
        is primary["tolc_absence_inferred"]
        is primary["full_paper_signoff"]
        is primary["sequence_variant_protocol_exported"]
        is False,
        "primary canary changed",
    )
    return sources


def read_component(root, source, gene, reviewed):
    require(source["url"] == gene_url(gene, reviewed), "component query identity changed")
    body, provenance = outer.native.read_source(root, source)
    outer.genes.validate_entries(body["results"], gene.casefold(), reviewed)
    require(not body["results"], "new component candidates require review")
    return {
        "source": provenance,
        "gene": gene,
        "reviewed": reviewed,
        "source_taxon_id": 573,
        "complete_for_query": True,
        "accessions": [],
        "zero_hits_are_absence": False,
        "experimental_assignment": False,
    }


def corpus_context(root, cohort):
    for key in (
        "prior",
        "prior_verification",
        "prior_name_dossier",
        "census",
        "source_inventory",
        "source_queue",
        "definition_citations",
        "literature",
        "protected",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    proof = json.loads(reference.check_pin(root, cohort["prior_verification"]).read_bytes())
    require(cohort["prior"] in proof["files"] and proof["summary"] == index["summary"], "prior proof changed")
    labels = {}
    with reference.check_pin(root, cohort["source_inventory"]).open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            require(
                labels.setdefault(row["determinant_id"], row["determinant_name"]) == row["determinant_name"],
                "inconsistent source labels",
            )
    tids = {tid for tid in index["terms"] if SELECT.search(labels[tid])}
    require(tids == set(TERMS), "complete Kpn label cohort changed")
    citations = json.loads(reference.check_pin(root, cohort["definition_citations"]).read_bytes())["terms"]
    terms = {
        t: {
            "source_label": labels[t],
            "source_label_sha256": index["terms"][t]["source_label_sha256"],
            "record_memberships": index["terms"][t]["record_memberships"],
            "definition_citation_ids": citations[t]["definition_citation_ids"],
            "prior_links": index["terms"][t]["links"],
        }
        for t in sorted(tids)
    }
    require(
        terms == cohort["terms"]
        and all(not t["prior_links"] for t in terms.values())
        and {p.removeprefix("PMID:") for t in terms.values() for p in t["definition_citation_ids"]}
        == set(PMIDS)
        and cohort["pmids"] == list(PMIDS),
        "frozen term or citation membership changed",
    )
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")},
        "complete corpus membership changed",
    )
    require(
        all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census), "corpus record changed"
    )
    ids = {rid for t in terms.values() for rid in t["record_memberships"]}
    records, claims = [r for r in census if r["identifier"] in ids], []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "structure identity changed",
        )
        for position, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in tids:
                require(claim["label"] == labels[claim["aro_id"]], "claim label changed")
                claims.append(
                    {
                        "record_identifier": doc["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(
        records == cohort["records"]
        and claims == cohort["claims"]
        and len(records) == 26
        and len(claims) == 28,
        "selected claim membership changed",
    )
    return terms, records, claims


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    terms, records, claims = corpus_context(root, cohort)
    name = cohort["name_context"]
    prior_name = json.loads(reference.check_pin(root, cohort["prior_name_dossier"]).read_bytes())["names"][
        "Klebsiella pneumoniae"
    ]
    require(name == prior_name, "reused species context changed")
    body, provenance = outer.native.read_source(root, name["source"])
    nodes, species = outer.lineages.lineage(body)
    require(
        body["taxonId"] == 573
        and body["scientificName"] == "Klebsiella pneumoniae"
        and body["active"] is True
        and body["rank"] == "species"
        and nodes == name["selected_taxon"]["lineage"]
        and species == name["selected_taxon"]["species_ancestor"],
        "native species reference changed",
    )
    queries, entries = {}, {}
    for pmid in PMIDS:
        entries[pmid], queries[pmid] = literature.read_query(root, root / literature.DIRECTORY, pmid)
        require(
            not entries[pmid]
            and queries[pmid]["complete_for_query"]
            and queries[pmid]["release"] == "2026_03",
            "native citation-query context changed",
        )
    require(
        json.loads(reference.check_pin(root, cohort["literature"]).read_bytes())
        == {"entries": entries, "queries": queries},
        "reused literature evidence changed",
    )
    sources = request_context(root, directory)
    components = {}
    fallback = json.loads((directory / "unreviewed-plan.json").read_bytes())
    for gene in GENES:
        components[gene] = {}
        for kind in ("reviewed", "unreviewed"):
            key = kind + "-" + gene.lower()
            query = read_component(root, sources[key], gene, kind == "reviewed")
            require(
                query == json.loads((directory / (key + "-review.json")).read_bytes()),
                "component canary changed",
            )
            if kind == "reviewed":
                require(query == fallback["reviewed_queries"][gene], "fallback prior evidence changed")
            components[gene][kind] = query
    publications = {
        p: {
            **project_metadata(json.loads((directory / ("metadata-" + p + "-response.bin")).read_bytes()), p),
            "source": sources["metadata-" + p],
        }
        for p in PMIDS
    }
    primary = project_primary((directory / "primary-24823362-response.bin").read_bytes())
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
                    "source_inventory",
                    "source_queue",
                    "definition_citations",
                    "literature",
                    "prior_name_dossier",
                )
            },
            "cohort": reference.pin(root, directory / "cohort.json"),
        },
        "terms": terms,
        "records": records,
        "claims": claims,
        "reused_literature_queries": queries,
        "reference_species": {
            "taxon_id": "NCBITaxon:573",
            "scientific_name": "Klebsiella pneumoniae",
            "rank": "species",
            "lineage": nodes,
            "source": provenance,
            "experimental_strain_taxon_assignment": None,
            "experimental_subject_assignment": False,
        },
        "publications": publications,
        "request_sources": sources,
        "primary_context": {**primary, "source": sources["primary-24823362"]},
        "component_queries": components,
        "term_dispositions": {
            "ARO:3004585": {
                "status": "OWN_CITATION_METADATA_ONLY_COMPONENT_MAPPING_UNRESOLVED",
                "single_protein_assigned": None,
                "experimental_allele_assigned": None,
            },
            "ARO:3004598": {
                "status": "PRIMARY_COMPONENT_NAMES_EXACT_QUERIES_EMPTY_TOLC_UNRESOLVED",
                "single_protein_assigned": None,
                "experimental_allele_assigned": None,
            },
        },
        "summary": {
            "source_terms": len(terms),
            "source_claims": len(claims),
            "cohort_records": len(records),
            "corpus_records_hash_checked": 2939,
            "complete_collection_aware_records_read": len(records),
            "reused_complete_literature_queries": 2,
            "new_complete_component_queries": 4,
            "component_query_hits": 0,
            "primary_context_reviews": 1,
            "metadata_only_papers": 1,
            "paper_reported_background_genomes": 1,
            "new_verified_resistance_results": 0,
            "experimental_gene_allele_assignments": 0,
            "biological_records_changed": 0,
        },
        "constraints": {
            "network_requests": 7,
            "new_uniprot_requests": 4,
            "new_taxonomy_requests": 0,
            "ncbi_requests": 0,
            "primary_requests": 1,
            "retry_performed": False,
            "redirects_followed": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "new_access_holds": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "limitations": [
            "All current Kpn-labeled CARD terms are covered, not all efflux terms or all literature.",
            "KpnEF remains metadata-only; its non-OA flag is neither a global paywall nor an access denial.",
            "Empty exact gene and publication searches do not establish protein or gene absence.",
            "EmrAB homology and the inconsistent KpnF label are not accepted as exact component aliases.",
            "No literal TolC mention in the retrieved XML is not proof "
            "against a biological role or CARD label.",
            "The paper genome describes a background, not an independently verified experimental derivative.",
            "Figures, tables, supplements, exact compound assays "
            "and all whole-record primary signoffs remain open.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt metadata: UniProt Consortium. "
        "Bibliographic metadata: Europe PMC at EBI. Primary context: Srinivasan et al. 2014, "
        "doi:10.1371/journal.pone.0096288, CC BY 4.0. No source adoption.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = (json.dumps(build(Path.cwd()), indent=2, sort_keys=True) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == payload, "saved dossier does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(payload)


if __name__ == "__main__":
    main()

"""Review every unlinked AAC(6)-label term without inventing exact experimental alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode

import audit_card_literature_expansion as literature
from audit_card_reference_lineages import lineage
from audit_card_reference_memberships import checksum
from audit_fungamr_cohort import read_source
from audit_valinomycin_abcb1 import planned_source
from audit_vgb_evidence import project_protein, read_json, reference, require, text, wrapped
from lxml import etree, html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-15-aac6-gaps")
OUTPUT = Path("research/2026-10-15-aac6-gaps.json")
COHORT_SHA = "808d085c947f01a94aa4b9b8b0f205bf076735d883351c86f3864cb6e4e2aea8"
SCOPE = "ALL_UNLINKED_AAC6_LABEL_TERMS_REFERENCE_AND_PRIMARY_CONTEXT_NOT_EXACT_ALLELES"
PRIMARY_URL = "https://europepmc.org/articles/PMC90325?pdf=render"
DOI = "10.1128/aac.45.2.546-552.2001"
SELECTED = {
    "Q9AIK8": {
        "term": "ARO:3002584",
        "label": "AAC(6')-29b",
        "gene": "aacA29b",
        "version": 73,
        "citations": {"journal article": 3, "submission": 2},
    },
    "Q9AIK9": {
        "term": "ARO:3002583",
        "label": "AAC(6')-29a",
        "gene": "aacA29a",
        "version": 74,
        "citations": {"journal article": 4, "submission": 3},
    },
}
RELATED = {
    "ARO:3002594": ["Q51409"],
    "ARO:3002567": ["O52241", "O52242", "O52243", "O52244", "O52245", "O52246", "O52247"],
    "ARO:3002547": ["A1YLC0", "Q6SJ71"],
    "ARO:3005112": ["F1BYM7", "F1BYN4", "F1BYP1", "F1BYQ0", "F1BYQ5"],
}
RELATED_REASONS = {
    "ARO:3002594": "GENE_LABEL_II_NOT_IIA_AND_PROTEIN_DESCRIPTION_TYPE_I",
    "ARO:3002567": "SEVEN_GENE_UNNAMED_TYPE_I_ENTRIES_NO_IW_DISTINCTION",
    "ARO:3002547": "UNNUMBERED_IB_CR_NAMES_NOT_EXPLICIT_CR1",
    "ARO:3005112": "AAC_A4_OR_AAC_A4_CR_NAMES_NOT_NUMBERED_CR3",
}
REFERENCE = "UNREVIEWED_PROTEIN_NAME_GENE_TAXON_REFERENCE_ONLY"
NO_CITATION = "NO_DEFINITION_CITATION_NO_CITATION_QUERY"
EMPTY = "COMPLETE_CITATION_QUERIES_EMPTY_NOT_BIOLOGICAL_ABSENCE"
AMBIGUOUS = "RELATED_FAMILY_CONTEXT_NOT_EXACT_ALLELE_SELECTION"


def metadata_url():
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {
            "query": "EXT_ID:11158753 AND SRC:MED",
            "format": "json",
            "resultType": "core",
            "pageSize": 1,
        }
    )


def protein_names(entry):
    result = []
    for kind in ("recommendedName", "alternativeNames", "submissionNames"):
        values = entry.get("proteinDescription", {}).get(kind, [])
        if isinstance(values, dict):
            values = [values]
        for index, value in enumerate(values):
            if "fullName" in value:
                result.append({"field": kind, "index": index, "value": value["fullName"]["value"]})
    return result


def name_matches(entry, label):
    pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(label) + r"(?![A-Za-z0-9'-])", re.I)
    return [row for row in protein_names(entry) if pattern.search(row["value"])]


def project_reference(entry, taxon):
    accession = entry["primaryAccession"]
    require(accession in SELECTED, "unselected reference")
    expected = SELECTED[accession]
    nodes, species = lineage(taxon)
    genes = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    matches = name_matches(entry, expected["label"])
    require(
        not {"sequence", "features"} & set(entry)
        and genes == [expected["gene"]]
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["entryAudit"] == {"entryVersion": expected["version"], "sequenceVersion": 1}
        and all(type(v) is int for v in entry["entryAudit"].values())
        and entry["organism"]["taxonId"] == taxon["taxonId"] == 287
        and entry["organism"]["scientificName"] == taxon["scientificName"] == "Pseudomonas aeruginosa"
        and taxon["rank"] == "species"
        and species == nodes[-1]
        and entry["uniProtKBCrossReferences"] == []
        and entry.get("proteinDescription", {}).get("flag") is None
        and len(matches) == 1
        and matches[0]["field"] == "submissionNames",
        "native reference identity, name or taxonomy changed",
    )
    bibliography, focal = [], []
    for item in entry["references"]:
        citation = item["citation"]
        ids = citation.get("citationCrossReferences", [])
        pmids = [i["id"] for i in ids if i["database"] == "PubMed"]
        bibliography.append(
            {
                "reference_number": item["referenceNumber"],
                "citation_type": citation["citationType"],
                "citation_sha256": checksum(citation),
                "focal_source_citation": "11158753" in pmids,
            }
        )
        if "11158753" in pmids:
            require(
                pmids == ["11158753"]
                and citation["citationType"] == "journal article"
                and [i["id"].lower() for i in ids if i["database"] == "DOI"] == [DOI]
                and "Pseudomonas aeruginosa" in citation["title"],
                "focal bibliography changed",
            )
            focal.append(
                {"reference_number": item["referenceNumber"], "pmid": "PMID:11158753", "doi": "DOI:" + DOI}
            )
    require(
        len(focal) == 1
        and focal[0]["reference_number"] == 1
        and [b["reference_number"] for b in bibliography] == list(range(1, len(bibliography) + 1))
        and dict(Counter(b["citation_type"] for b in bibliography)) == expected["citations"],
        "native bibliography coverage changed",
    )
    return {
        **project_protein(entry),
        "source_term_id": expected["term"],
        "source_label": expected["label"],
        "protein_name_matches": matches,
        "native_reference_taxon_rank": "species",
        "matched_bibliography": focal,
        "native_bibliography_accounting": bibliography,
        "explicit_card_xref": False,
        "submission_name_is_expert_review": False,
        "native_protein_flag": None,
        "unflagged_means_complete": False,
        "experimental_subject_assignment": False,
        "exact_allele_assignment": False,
        "experimental_genome_assignment": None,
        "primary_results_reviewed": False,
        "scope": REFERENCE,
    }


def primary_hold(payload, receipt):
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    tree = html.fromstring(payload)
    require(
        receipt["url"] == PRIMARY_URL
        and receipt["status"] == 403
        and receipt["sha256"] == hashlib.sha256(payload).hexdigest()
        and receipt["bytes"] == len(payload)
        and receipt["retry_performed"] is receipt["redirects_followed"] is False
        and headers.get("cf-mitigated") == "challenge"
        and tree.xpath("//title/text()") == ["Just a moment..."]
        and not payload.startswith(b"%PDF-")
        and not tree.xpath('//meta[@name="citation_doi"]/@content'),
        "primary challenge changed",
    )
    return {
        "url": PRIMARY_URL,
        "pmid": "PMID:11158753",
        "doi": "DOI:" + DOI,
        "http_status": 403,
        "status": "ADVERTISED_PDF_403_CHALLENGE_HELD_NO_RETRY_OR_ALTERNATE",
        "primary_results_reviewed": False,
        "pdf_retrieved": False,
        "retry_performed": False,
        "alternate_route_used": False,
        "biological_absence_inferred": False,
        "permanent_unavailability_inferred": False,
        "revisit_requires": "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION",
    }


def project_lc231(payload, donor_taxon, host_taxon):
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): text(n) for n in tree.xpath("./front/article-meta/article-id")}
    require(
        ids.get("pmid") == "27929110" and ids.get("doi") == "10.1038/ncomms13803",
        "LC231 article identity changed",
    )
    require(
        [text(n) for n in tree.xpath('//sec[@id="sec2"]/title')]
        == ["Paenibacillus sp. LC231 is multi-drug resistant"],
        "source-isolate context changed",
    )
    tables = tree.xpath('//table-wrap[@id="t1"]')
    require(len(tables) == 1, "LC231 table missing or ambiguous")
    table = tables[0]
    caption = text(table.find("caption"))
    require(
        caption == "MICs of antibiotic resistance determinants heterologously expressed in E. coli.",
        "assay-host scope changed",
    )
    rows = [r for r in table.xpath(".//tr") if any(text(c) == "aac(6\u2032)-34" for c in r.findall("td"))]
    require(len(rows) == 1, "AAC34 row missing or ambiguous")
    cells = [text(c) for c in rows[0].findall("td")]
    require(
        cells
        == ["Kanamycin acetyltransferase", "aac(6\u2032)-34", "Aminoglycoside", "Kanamycin", ">128", "8"]
        and not rows[0].xpath("./td/xref/@rid")
        and [text(c) for c in table.xpath(".//thead//th")]
        == [
            "Resistance Determinant",
            "Name",
            "Antibiotic class",
            "Antibiotic",
            "MIC (\u03bcg ml\u22121)",
            "Empty vector control MIC (\u03bcg ml\u22121)",
        ],
        "AAC34 cells, units or control changed",
    )
    lineage(donor_taxon)
    lineage(host_taxon)
    require(
        donor_taxon["taxonId"] == 1120679
        and donor_taxon["scientificName"] == "Paenibacillus sp. (strain LC231)"
        and donor_taxon["rank"] == "species"
        and host_taxon["taxonId"] == 562
        and host_taxon["scientificName"] == "Escherichia coli"
        and host_taxon["rank"] == "species",
        "source isolate or assay-host taxonomy changed",
    )
    return {
        "pmid": "PMID:27929110",
        "doi": "DOI:10.1038/ncomms13803",
        "location": "Table 1 / aac(6-prime)-34 row and table caption",
        "table_caption_sha256": hashlib.sha256(caption.encode()).hexdigest(),
        "source_term_id": "ARO:3003989",
        "source_antibiotic_label": cells[3],
        "source_determinant_label": cells[1],
        "evidence_type": "HETEROLOGOUS_FUNCTIONAL_EXPERIMENT",
        "source_isolate_taxon_reference": "NCBITaxon:1120679",
        "source_isolate_native_rank": "species",
        "strain_word_in_taxon_name_changes_rank": False,
        "assay_host_species": "Escherichia coli",
        "assay_host_species_taxon": "NCBITaxon:562",
        "assay_host_strain_assignment": None,
        "reported_determinant_mic": {
            "original_value": ">128",
            "original_unit": "ug/mL",
            "comparator": ">",
            "value": 128,
            "unit": "mg/L",
            "conversion_factor": 1,
        },
        "reported_control_mic": {
            "original_value": "8",
            "original_unit": "ug/mL",
            "comparator": "=",
            "value": 8,
            "unit": "mg/L",
            "conversion_factor": 1,
        },
        "clinical_resistance_category": None,
        "breakpoint_interpretation_applied": False,
        "exact_corpus_structure_assignment": None,
        "native_isolate_MIC_inferred": False,
        "experimental_protein_assignment": None,
        "experimental_genome_assignment": None,
        "strain_construct_sequence_or_protocol_exported": False,
        "curation_status": "RESEARCH_ONLY_EXACT_COMPOUND_AND_EXPERIMENTAL_IDENTITY_UNRESOLVED",
    }


def corpus_context(root, cohort):
    for value in cohort.values():
        if isinstance(value, dict) and set(value) == {"path", "sha256"}:
            reference.check_pin(root, value)
    index = read_json(root, cohort["index"])
    direct = read_json(root, cohort["direct_candidates"])
    definitions = read_json(root, cohort["definition_citations"])
    selected = {
        tid: direct["determinants"][tid]["labels"][0]
        for tid, t in index["terms"].items()
        if not t["links"] and "aac(6" in direct["determinants"][tid]["labels"][0].casefold()
    }
    require(len(selected) == 15 and set(selected) == set(cohort["terms"]), "full label cohort changed")
    for tid, label in selected.items():
        row = cohort["terms"][tid]
        require(
            row["source_label"] == label
            and row["prior_term"] == index["terms"][tid]
            and row["definition_annotation_sha256"] == checksum(definitions["terms"][tid])
            and row["definition_citation_ids"] == definitions["terms"][tid]["definition_citation_ids"],
            "source term or citation context changed",
        )
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "corpus changed",
    )
    ids = {rid for tid in selected for rid in index["terms"][tid]["record_memberships"]}
    records, claims = [r for r in census if r["identifier"] in ids], []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "record identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in selected:
                require(claim["label"] == selected[claim["aro_id"]], "live claim label changed")
                claims.append(
                    {
                        "record_identifier": row["identifier"],
                        "position": i,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": checksum(claim),
                    }
                )
    require(
        records == cohort["records"]
        and claims == cohort["claims"]
        and len(records) == 12
        and len(claims) == 70,
        "full record or claim coverage changed",
    )
    return index, records, claims


def build(root):
    directory = root / CACHE
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    index, records, claims = corpus_context(root, cohort)
    pools, queries, union = {}, {}, {}
    for pmid, item in cohort["queries"].items():
        entries, query = literature.read_query(root, root / item["directory"], pmid)
        require(
            query == item["query"]
            and sorted(entries) == item["accessions"]
            and query["complete_for_query"]
            and query["release"] == "2026_03",
            "citation query changed",
        )
        pools[pmid], queries[pmid] = entries, query
        for accession, entry in entries.items():
            require(
                accession not in union or union[accession] == entry, "cross-query native identity changed"
            )
            union[accession] = entry
    taxonomy, tax_source = read_source(root, cohort["reference_taxonomy"])
    references = {"UniProtKB:" + a: project_reference(union[a], taxonomy) for a in sorted(SELECTED)}
    terms, memberships = {}, []
    for tid, row in sorted(cohort["terms"].items()):
        pmids = [p.removeprefix("PMID:") for p in row["definition_citation_ids"]]
        accessions = sorted({a for p in pmids for a in pools[p]})
        exact = [a for a in accessions if name_matches(union[a], row["source_label"])]
        expected = [a for a, r in SELECTED.items() if r["term"] == tid]
        require(exact == expected, "protein-name candidate coverage changed")
        related = RELATED.get(tid, [])
        require(set(related) <= set(accessions), "related context outside citation pool")
        status = REFERENCE if exact else NO_CITATION if not pmids else EMPTY if not accessions else AMBIGUOUS
        require((status == AMBIGUOUS) is bool(related), "unclassified nonempty citation context")
        terms[tid] = {
            **row,
            "status": status,
            "complete_citation_query_accessions": accessions,
            "reference_candidates": ["UniProtKB:" + a for a in exact],
            "related_family_context": [
                {
                    "accession": "UniProtKB:" + a,
                    "gene_symbols": [
                        g["geneName"]["value"] for g in union[a].get("genes", []) if "geneName" in g
                    ],
                    "native_reported_taxon_id": union[a]["organism"]["taxonId"],
                    "native_reported_organism": union[a]["organism"]["scientificName"],
                    "native_protein_names": [n["value"] for n in protein_names(union[a])],
                    "withholding_reason": RELATED_REASONS[tid],
                    "native_taxonomy_independently_reviewed_here": False,
                    "selected_as_exact_source_allele": False,
                }
                for a in related
            ],
            "other_citation_hits_not_selected": [
                "UniProtKB:" + a for a in accessions if a not in exact + related
            ],
            "experimental_subject_assignment": False,
            "biological_absence_inferred": False,
        }
        for a in exact:
            memberships.extend(
                {
                    "record_identifier": rid,
                    "source_term_id": tid,
                    "protein_accession": "UniProtKB:" + a,
                    "scope": REFERENCE,
                    "experimental_subject_assignment": False,
                }
                for rid in row["prior_term"]["record_memberships"]
            )
    metadata_source = planned_source(
        root, directory, "metadata-11158753", "metadata-plan.json", metadata_url()
    )
    meta = read_json(root, metadata_source["body"])
    rows = meta["resultList"]["result"]
    require(
        type(meta["hitCount"]) is int
        and meta["hitCount"] == len(rows) == 1
        and not meta.get("nextCursorMark")
        and meta["request"]["queryString"] == "EXT_ID:11158753 AND SRC:MED"
        and meta["request"]["resultType"].lower() == "core"
        and type(meta["request"]["pageSize"]) is int
        and meta["request"]["pageSize"] == 1,
        "metadata query identity changed",
    )
    row = rows[0]
    require(
        row["id"] == row["pmid"] == "11158753"
        and row["source"] == "MED"
        and row["doi"].lower() == DOI
        and row["pmcid"] == "PMC90325"
        and row["isOpenAccess"] == "N",
        "metadata identity changed",
    )
    require(
        all(
            union[a]["references"][0]["citation"]["title"].casefold() == row["title"].casefold()
            for a in SELECTED
        ),
        "native and indexed publication titles disagree",
    )
    metadata = {
        k: row[k] for k in ("id", "source", "title", "doi", "pmcid", "isOpenAccess", "firstPublicationDate")
    }
    metadata.update(
        {
            "abstract_sha256": hashlib.sha256(row["abstractText"].encode()).hexdigest(),
            "advertised_primary_links": row["fullTextUrlList"]["fullTextUrl"],
            "metadata_is_primary_results": False,
            "non_oa_flag_is_access_denial": False,
        }
    )
    primary_source = planned_source(root, directory, "primary", "request-plan.json", PRIMARY_URL, (403,))
    plan = read_json(root, primary_source["plan"])
    require(
        plan["metadata_body"] == metadata_source["body"]
        and plan["requests"]["primary"]["advertised_link"] in metadata["advertised_primary_links"]
        and plan["first_primary_format"] == "METADATA_ADVERTISED_PDF"
        and plan["alternate_route_used"] is False,
        "primary advertisement or scope changed",
    )
    hold = primary_hold(
        reference.check_pin(root, primary_source["body"]).read_bytes(),
        read_json(root, primary_source["receipt"]),
    )
    hold["source"] = primary_source
    _, primary = wrapped(
        root,
        cohort["lc231_primary"],
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5155152/fullTextXML",
    )
    native_taxa, donor_source = read_source(
        root,
        {
            "wrapper": cohort["lc231_taxonomy"],
            "url": "https://rest.uniprot.org/taxonomy/search?query=LC231&format=json&size=25",
        },
    )
    require(len(native_taxa["results"]) == 1, "LC231 taxonomy search ambiguous")
    host, host_source = read_source(
        root, {"wrapper": index["inputs"]["taxonomy"], "url": "https://rest.uniprot.org/taxonomy/562"}
    )
    lc231 = project_lc231(primary, native_taxa["results"][0], host)
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "index": cohort["index"],
            "previous_verification": cohort["previous_verification"],
            "lc231_primary": cohort["lc231_primary"],
            "prior_vgb_context": cohort["prior_vgb_context"],
        },
        "terms": terms,
        "claims": claims,
        "records": records,
        "references": references,
        "reference_memberships": memberships,
        "citation_queries": queries,
        "reference_taxonomy_sources": {"287": tax_source, "LC231_search": donor_source, "562": host_source},
        "metadata": metadata,
        "metadata_source": metadata_source,
        "primary_access_hold": hold,
        "aac34_primary_table_context": lc231,
        "summary": {
            "source_terms": len(terms),
            "source_claims": len(claims),
            "cohort_records": len(records),
            "corpus_records_hash_checked": 2939,
            "complete_cached_citation_queries": len(queries),
            "citation_query_entries": sum(len(p) for p in pools.values()),
            "distinct_citation_entries": len(union),
            "term_statuses": dict(sorted(Counter(t["status"] for t in terms.values()).items())),
            "new_reference_links": len(references),
            "new_reference_memberships": len(memberships),
            "new_primary_access_holds": 1,
            "cached_primary_table_context_reviews": 1,
        },
        "disposition": {
            "biological_records_changed": 0,
            "experimental_allele_or_genome_assignments": 0,
            "whole_record_primary_signoffs": 0,
            "new_curated_AST_observations": 0,
        },
        "constraints": {
            "network_requests": 2,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "outreach": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "full_corpus_goal_status": "OPEN",
            "membership_index_updated": False,
            "prior_source_holds_preserved": True,
        },
        "limitations": [
            "All 15 unlinked AAC(6)-label terms are covered, not every source term in the enzyme family.",
            "Unreviewed submission names and source-cited bibliography support references, "
            "not tested alleles.",
            "Generic II, Iw-neighbor and Ib-cr entries are not exact IIa, Iw "
            "or numbered cr-subtype assignments.",
            "Empty citation queries and missing definition citations "
            "do not establish gene or protein absence.",
            "The AAC29 primary PDF request was held after a 403 challenge; no retry or alternative was used.",
            "The AAC34 table reports a heterologous host and an ambiguous compound label, "
            "not native-isolate MIC.",
            "No strain, construct, sequence, variant, protocol "
            "or new experimental genome identity is exported.",
            "Two new reference links await reconciliation into a successor broad index.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. UniProt Consortium metadata, "
        "release 2026_03. Europe PMC at EBI bibliographic metadata. Pawlowski et al., "
        "Nature Communications 7:13803 (2016), DOI:10.1038/ncomms13803, selected Table 1 context.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == body, "AAC6 dossier does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()

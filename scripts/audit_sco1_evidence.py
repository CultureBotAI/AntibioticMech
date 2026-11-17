"""Resolve SCO-1 reference metadata without assigning experimental alleles or AST."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlencode

import audit_card_definition_citations as definitions
import audit_card_literature_expansion as literature
from audit_card_reference_lineages import lineage
from audit_fungamr_cohort import read_source
from audit_valinomycin_abcb1 import planned_source
from audit_vgb_evidence import project_protein, read_json, reference, require, wrapped

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-15-sco1-evidence")
OUTPUT = Path("research/2026-10-15-sco1-evidence.json")
SCOPE = "SCO1_NATIVE_GENE_CITATION_TAXON_REFERENCE_NOT_EXPERIMENTAL_ALLELE"
COHORT_SHA = "ff4b2aa983a974f380033c64dc4ba59d218c9c114645b52b1fe6abf050e7e9a9"
SELECTION_SHA = "1e036336f4c2be840edd9786c80b673fa00928d08eaf0bff244e49041ee2c773"
TERM, LABEL = "ARO:3004856", "SCO-1"
PUBLICATIONS = {
    "17353248": ("10.1128/aac.01439-06", "PMC1891400"),
    "17420213": ("10.1128/aac.01600-06", "PMC1891420"),
    "20956594": ("10.1128/aac.00875-10", "PMC3019680"),
}
SELECTED = {
    "A1E3K9": (562, "Escherichia coli", 92, ["17353248", "20956594"]),
    "A5Y0S3": (470, "Acinetobacter baumannii", 73, ["17420213"]),
}


def metadata_url(pmid):
    require(pmid in PUBLICATIONS, "unplanned PMID")
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {
            "query": "EXT_ID:" + pmid + " AND SRC:MED",
            "format": "json",
            "resultType": "core",
            "pageSize": 1,
        }
    )


def project_metadata(data, pmid, inspected):
    rows = data["resultList"]["result"]
    require(
        type(data["hitCount"]) is int
        and data["hitCount"] == len(rows) == 1
        and not data.get("nextCursorMark")
        and data["request"]["queryString"] == "EXT_ID:" + pmid + " AND SRC:MED"
        and data["request"]["resultType"].lower() == "core"
        and type(data["request"]["pageSize"]) is int
        and data["request"]["pageSize"] == 1,
        "metadata query identity changed",
    )
    row = rows[0]
    identity = {
        k: row.get(k)
        for k in ("id", "source", "title", "doi", "pmcid", "isOpenAccess", "firstPublicationDate")
    }
    require(
        row["id"] == row["pmid"] == pmid
        and row["source"] == "MED"
        and all(identity[k] == inspected[k] for k in identity)
        and (row["doi"].lower(), row["pmcid"]) == PUBLICATIONS[pmid]
        and "SCO-1" in row["title"]
        and row["isOpenAccess"] == "N",
        "publication identity changed",
    )
    return {
        **identity,
        "abstract_sha256": hashlib.sha256(row["abstractText"].encode()).hexdigest(),
        "advertised_primary_links": row["fullTextUrlList"]["fullTextUrl"],
        "primary_results_reviewed": False,
        "non_oa_metadata_is_access_denial": False,
        "primary_unavailability_claimed": False,
        "scope": "METADATA_NOT_PRIMARY_EXPERIMENTAL_EVIDENCE",
    }


def project_reference(entry, taxon, metadata):
    accession = entry["primaryAccession"]
    require(accession in SELECTED, "unselected reference accession")
    taxid, name, version, pmids = SELECTED[accession]
    lineage(taxon)
    symbols = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    require(
        symbols == ["blaSCO-1"]
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["entryAudit"] == {"entryVersion": version, "sequenceVersion": 1}
        and entry["organism"]["taxonId"] == taxon["taxonId"] == taxid
        and entry["organism"]["scientificName"] == taxon["scientificName"] == name
        and taxon["rank"] == "species"
        and taxon["active"] is True
        and entry["uniProtKBCrossReferences"] == []
        and entry.get("proteinDescription", {}).get("flag") is None,
        "native gene, taxonomy, version or reference scope changed",
    )
    bibliography = []
    for item in entry["references"]:
        citation = item["citation"]
        identifiers = citation.get("citationCrossReferences", [])
        cited = [i["id"] for i in identifiers if i["database"] == "PubMed"]
        require(len(cited) == 1 and cited[0] in pmids, "native citation membership changed")
        pmid = cited[0]
        doi = [i["id"].lower() for i in identifiers if i["database"] == "DOI"]
        require(
            citation["citationType"] == "journal article"
            and "SCO-1" in citation["title"]
            and doi == [metadata[pmid]["doi"].lower()],
            "native citation DOI or label changed",
        )
        bibliography.append(
            {
                "reference_number": item["referenceNumber"],
                "pmid": "PMID:" + pmid,
                "doi": "DOI:" + doi[0],
                "native_title": citation["title"],
            }
        )
    require(
        sorted(b["pmid"].removeprefix("PMID:") for b in bibliography) == pmids,
        "complete native bibliography changed",
    )
    return {
        **project_protein(entry),
        "native_reference_taxon_rank": "species",
        "bibliography": bibliography,
        "source_term_id": TERM,
        "source_label": LABEL,
        "explicit_card_xref": False,
        "alias_basis": "EXACT_NATIVE_BLASCO1_GENE_AND_SOURCE_CITED_SCO1_PUBLICATIONS",
        "global_bla_prefix_normalization_enabled": False,
        "unflagged_means_complete": False,
        "native_protein_flag": None,
        "experimental_subject_assignment": False,
        "experimental_genome_assignment": None,
        "exact_allele_assignment": False,
        "primary_results_reviewed": False,
        "scope": "UNREVIEWED_GENE_CITATION_TAXON_REFERENCE_ONLY",
    }


def corpus_context(root, cohort):
    for value in cohort.values():
        if isinstance(value, dict) and set(value) == {"path", "sha256"}:
            reference.check_pin(root, value)
    index = read_json(root, cohort["index"])
    with reference.check_pin(root, cohort["source_inventory"]).open() as stream:
        labels = {r["determinant_id"]: r["determinant_name"] for r in csv.DictReader(stream, delimiter="\t")}
    require(
        {t: n for t, n in labels.items() if re.fullmatch(r"SCO[- ]?\d+", n, re.I)} == {TERM: LABEL},
        "SCO source-label coverage changed",
    )
    require(
        cohort["source_term_id"] == TERM
        and cohort["source_label"] == LABEL
        and cohort["prior_term"] == index["terms"][TERM]
        and not cohort["prior_term"]["links"],
        "source term or prior reference state changed",
    )
    _, body = wrapped(root, cohort["ontology_cache"])
    projected = definitions.project_annotations(
        definitions.Graph().parse(data=body, format="xml"), {TERM: LABEL}
    )
    require(
        cohort["definition"] == read_json(root, cohort["definition_citations"])["terms"][TERM]
        and all(cohort["definition"][k] == v for k, v in projected[TERM].items())
        and cohort["definition"]["definition_citation_ids"] == ["PMID:" + p for p in PUBLICATIONS],
        "native source bibliography changed",
    )
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    require(
        len(census) == len({r["identifier"] for r in census}) == 2939
        and {r["path"] for r in census}
        == {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        and all(reference.digest(root / r["path"]) == r["record_sha256"] for r in census),
        "current corpus changed",
    )
    ids = set(cohort["prior_term"]["record_memberships"])
    records, claims = [r for r in census if r["identifier"] in ids], []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "structure identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") == TERM:
                require(claim["label"] == LABEL, "claim label changed")
                claims.append(
                    {
                        "record_identifier": doc["identifier"],
                        "position": i,
                        "aro_id": TERM,
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(
        records == cohort["records"] and claims == cohort["claims"] and len(records) == len(claims) == 8,
        "complete record or claim membership changed",
    )
    return records, claims


def build(root, directory=CACHE):
    directory = root / directory
    require(
        reference.digest(directory / "cohort.json") == COHORT_SHA
        and reference.digest(directory / "source-selection.json") == SELECTION_SHA,
        "frozen cohort or inspected selection changed",
    )
    cohort = json.loads((directory / "cohort.json").read_bytes())
    selection = json.loads((directory / "source-selection.json").read_bytes())
    records, claims = corpus_context(root, cohort)
    metadata, sources = {}, {}
    for pmid in PUBLICATIONS:
        source = planned_source(root, directory, "metadata-" + pmid, "metadata-plan.json", metadata_url(pmid))
        require(
            source["body"] == selection["metadata"][pmid]["body"]
            and source["receipt"] == selection["metadata"][pmid]["receipt"],
            "metadata source changed",
        )
        metadata[pmid] = project_metadata(read_json(root, source["body"]), pmid, selection["metadata"][pmid])
        sources[pmid] = source
    native_taxa, taxonomy_sources = {}, {}
    for taxid, item in selection["native_taxonomy"].items():
        native_taxa[taxid], taxonomy_sources[taxid] = read_source(
            root, {"wrapper": item, "url": "https://rest.uniprot.org/taxonomy/" + taxid}
        )
    require(set(native_taxa) == {"470", "562"}, "native taxonomy coverage changed")
    entries, queries = {}, {}
    for pmid in PUBLICATIONS:
        entries[pmid], queries[pmid] = literature.read_query(root, root / literature.DIRECTORY, pmid)
    require(
        {"entries": entries, "queries": queries} == read_json(root, cohort["literature"])
        and {p: len(e) for p, e in entries.items()} == {"17353248": 3, "17420213": 5, "20956594": 43},
        "complete cached citation queries changed",
    )
    pool = {}
    for items in entries.values():
        for accession, entry in items.items():
            require(accession not in pool or pool[accession] == entry, "cross-query native identity conflict")
            pool[accession] = entry
    selected = {
        a
        for a, e in pool.items()
        if any(g.get("geneName", {}).get("value") == "blaSCO-1" for g in e.get("genes", []))
    }
    require(
        selected == set(SELECTED)
        and selection["selected_accessions"] == sorted(selected)
        and len(pool) == 48,
        "complete candidate or citation-pool coverage changed",
    )
    proteins = {
        "UniProtKB:" + a: project_reference(pool[a], native_taxa[str(SELECTED[a][0])], metadata)
        for a in sorted(selected)
    }
    for a in selected:
        require([p for p in PUBLICATIONS if a in entries[p]] == SELECTED[a][3], "query membership changed")
        names, direct = literature.literature.match_entry(pool[a], TERM, LABEL)
        require(not names and not direct, "historical exact-label disposition changed")
    memberships = [
        {
            "record_identifier": rid,
            "source_term_id": TERM,
            "protein_accession": a,
            "scope": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_OR_AST",
            "experimental_subject_assignment": False,
        }
        for rid in sorted(cohort["prior_term"]["record_memberships"])
        for a in sorted(proteins)
    ]
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "source_selection": reference.pin(root, directory / "source-selection.json"),
            "index": cohort["index"],
            "previous_verification": cohort["previous_verification"],
        },
        "source_term_id": TERM,
        "source_label": LABEL,
        "source_term": cohort["prior_term"],
        "source_definition": cohort["definition"],
        "records": records,
        "claims": claims,
        "metadata": metadata,
        "metadata_sources": sources,
        "literature_queries": queries,
        "reference_taxonomy_sources": taxonomy_sources,
        "references": proteins,
        "reference_memberships": memberships,
        "incidental_citation_hits_not_selected": ["UniProtKB:" + a for a in sorted(set(pool) - selected)],
        "selection_context": {
            "source_label": LABEL,
            "native_gene_label": "blaSCO-1",
            "prior_literal_screen_selected_neither_reference": True,
            "source_cited_papers_and_native_bibliography_concordant": True,
            "global_bla_prefix_normalization_enabled": False,
            "acinetobacter_reference_species_not_applied_to_all_paper_isolates": True,
            "distinct_reference_accessions_collapsed": False,
        },
        "summary": {
            "source_terms": 1,
            "source_claims": 8,
            "cohort_records": 8,
            "corpus_records_hash_checked": 2939,
            "reused_complete_citation_queries": 3,
            "distinct_citation_query_entries": 48,
            "incidental_citation_hits_not_selected": 46,
            "new_gene_reference_links": 2,
            "new_gene_reference_memberships": len(memberships),
            "native_reference_taxa_checked": 2,
            "metadata_only_papers": 3,
            "primary_context_reviews": 0,
        },
        "disposition": {
            "biological_records_changed": 0,
            "experimental_gene_allele_assignments": 0,
            "experimental_genome_assignments": 0,
            "new_verified_resistance_results": 0,
            "whole_record_primary_signoffs": 0,
            "reference_organisms_transferred_to_experimental_subjects": False,
        },
        "constraints": {
            "new_requests": 3,
            "new_metadata_requests": 3,
            "new_uniprot_requests": 0,
            "new_primary_requests": 0,
            "ncbi_requests": 0,
            "outreach": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "prior_source_holds_preserved": True,
            "retry_performed": False,
            "redirects_followed": False,
            "full_corpus_goal_status": "OPEN",
            "membership_index_updated": False,
            "sequence_variant_protocol_exported": False,
        },
        "limitations": [
            "The three papers remain metadata-only here; advertised free links are not inspected full text.",
            "Non-OA metadata is not an access denial or proof that primary copies are unavailable.",
            "Citation and exact native gene identity support reference candidates, "
            "not tested allele assignments.",
            "Two references across eight inherited records are not sixteen resistance measurements.",
            "Acinetobacter spp. in a paper title is broader than the species of one UniProt reference.",
            "The 2010 citation names multiple enzymes; "
            "its other enzyme and neighboring entries are not SCO-1.",
            "No phenotype, strain, genome or source-owned record was curated; "
            "primary results remain to review.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt Consortium metadata, release 2026_03. Bibliographic metadata: Europe PMC at EBI. "
        "No source adopted or primary text exported.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    body = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == body, "SCO-1 dossier does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(body)
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()

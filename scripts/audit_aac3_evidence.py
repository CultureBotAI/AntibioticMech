"""Replay AAC(3)-III/IV identity evidence without conflating enzyme classes or alleles."""

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_card_definition_citations as definitions
import audit_card_literature_expansion as literature
from audit_card_grounding import FIELDS
from audit_card_reference_lineages import lineage
from audit_fungamr_cohort import read_source
from audit_valinomycin_abcb1 import planned_source
from audit_vgb_evidence import project_protein, read_json, reference, require, wrapped
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-15-aac3-evidence")
OUTPUT = Path("research/2026-10-15-aac3-evidence.json")
SCOPE = "AAC3_III_IV_REFERENCE_IDENTITY_NOT_EXPERIMENTAL_ALLELE_OR_PHENOTYPE"
COHORT_SHA = "984f3e0ca281903fd6c98376b55a9a377ede4885f16986bbb343f3688fbf2ad4"
SELECTION_SHA = "2218f6bdfba12e2b21e765ce7749becb0fbace710c5f8b2534bfa83487098397"
REFERENCE_CITATION_REVIEW_SHA = "15c5aac52fcb46ab18bfe0e490d0b95fd1a40dbed8b72d18455401941ce71ae0"
PRIMARY_REVIEW_SHA = "c29ef57aff431cce1a47358ae1eb339fb1bea1b01f21d0863f08c909770b86ae"
TERMS = {
    "ARO:3002536": "AAC(3)-IIIa",
    "ARO:3002537": "AAC(3)-IIIb",
    "ARO:3002538": "AAC(3)-IIIc",
    "ARO:3002539": "AAC(3)-IVa",
    "ARO:3005061": "AAC(3)-IVb",
}
QUERY_DIRS = {
    "20387903": literature.DIRECTORY,
    "19709289": Path("reports/resistance-grounding-2026-10-09-card-literature-proteins"),
    "6318050": Path("reports/resistance-grounding-2026-10-09-card-literature-proteins"),
}
DIRECT = {"ARO:3002536": "P29808", "ARO:3002538": "Q51406", "ARO:3005061": "A0A5C2PMK1"}
RELATED = {
    "Q8KLW8": ("aac(3)-IV", 316, "Fragment"),
    "Q8KMV1": ("aac(3)-IV", 562, "Fragment"),
    "P08988": ("aacC4", 599, None),
}
RELATED_TAXON_NAMES = {316: "Stutzerimonas stutzeri", 562: "Escherichia coli", 599: "Salmonella sp."}


def metadata_url(pmid):
    require(pmid in {*QUERY_DIRS, "30347146"}, "unplanned PMID")
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )


def gene_url(reviewed):
    require(type(reviewed) is bool, "reviewed subset must be boolean")
    return "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": 'gene_exact:"aac(3)-IIIb" AND taxonomy_id:287 AND reviewed:' + str(reviewed).lower(),
            "format": "json",
            "size": 500,
            "fields": FIELDS,
        }
    )


def project_metadata(data, pmid, expected):
    rows = data["resultList"]["result"]
    require(
        type(data["hitCount"]) is int
        and data["hitCount"] == len(rows) == 1
        and not data.get("nextCursorMark")
        and data["request"]["queryString"] == "EXT_ID:" + pmid + " AND SRC:MED"
        and data["request"]["resultType"].lower() == "core"
        and type(data["request"]["pageSize"]) is int
        and data["request"]["pageSize"] == 1,
        "metadata query changed",
    )
    row = rows[0]
    require(
        row["id"] == row["pmid"] == pmid
        and row["source"] == "MED"
        and {k: row.get(k) for k in expected["identity"]} == expected["identity"]
        and hashlib.sha256(row["abstractText"].encode()).hexdigest() == expected["abstract_sha256"]
        and row["fullTextUrlList"]["fullTextUrl"] == expected["primary_link"],
        "inspected metadata changed",
    )
    return {
        **expected["identity"],
        "abstract_sha256": expected["abstract_sha256"],
        "advertised_primary_links": expected["primary_link"],
        "evidence_scope": "INDEXED_METADATA_NOT_PRIMARY_RESULTS",
        "primary_results_reviewed": False,
        "non_oa_metadata_is_access_denial": False,
        "abstract_establishes_exact_allele_or_record_specific_ast": False,
    }


def project_related(entry, taxon, pmids):
    accession = entry["primaryAccession"]
    require(accession in RELATED, "unselected citation hit")
    gene, taxid, fragment = RELATED[accession]
    names = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    require(
        names == [gene]
        and entry["organism"]["taxonId"] == taxid == taxon["taxonId"]
        and taxon["scientificName"] == RELATED_TAXON_NAMES[taxid]
        and entry["proteinDescription"].get("flag") == fragment,
        "related reference identity or completeness changed",
    )
    nodes, _ = lineage(taxon)
    require(taxon["rank"] == "species", "native reference rank changed")
    expected_pmids = ["PMID:6318050"] if accession == "P08988" else ["PMID:19709289"]
    require(pmids == expected_pmids, "reference citation binding changed")
    return {
        **project_protein(entry),
        "native_fragment_flag": fragment,
        "source_citation_ids": pmids,
        "reference_taxonomy": {
            "taxon_id": "NCBITaxon:" + str(taxid),
            "scientific_name": taxon["scientificName"],
            "native_rank": taxon["rank"],
            "lineage": nodes,
        },
        "source_organism_label": entry["organism"]["scientificName"],
        "native_common_name": entry["organism"].get("commonName"),
        "native_taxonomy_synonyms": taxon.get("synonyms", []),
        "scope": "TYPE_IV_RELATED_REFERENCE_WITHOUT_VERIFIED_IVa_SUFFIX_OR_SUBJECT_IDENTITY",
        "exact_card_term_mapping_asserted": False,
        "experimental_subject_assignment": False,
        "generic_salmonella_label_promoted_to_named_species": False,
        "fragment_promoted_to_complete_protein": False,
        "primary_results_reviewed": False,
    }


def project_iiib(entry, taxon):
    names = [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g]
    citations = sorted(
        {
            "PMID:" + x["id"]
            for r in entry.get("references", [])
            for x in r["citation"].get("citationCrossReferences", [])
            if x["database"] == "PubMed"
        }
    )
    lineage(taxon)
    require(
        entry["primaryAccession"] == "Q51405"
        and names == ["aac(3)-IIIb"]
        and entry["entryType"] == "UniProtKB unreviewed (TrEMBL)"
        and entry["entryAudit"] == {"entryVersion": 61, "sequenceVersion": 1}
        and entry["organism"]["taxonId"] == taxon["taxonId"] == 287
        and entry["organism"]["scientificName"] == taxon["scientificName"] == "Pseudomonas aeruginosa"
        and taxon["rank"] == "species"
        and citations == ["PMID:30347146"]
        and entry["uniProtKBCrossReferences"] == [],
        "IIIb reference identity or citation context changed",
    )
    return {
        **project_protein(entry),
        "source_term_id": "ARO:3002537",
        "source_label": "AAC(3)-IIIb",
        "native_reference_taxon_rank": "species",
        "native_citation_ids": citations,
        "scope": "EXACT_SOURCE_GENE_AND_TAXON_REFERENCE_NOT_EXPERIMENTAL_ALLELE",
        "explicit_card_xref": False,
        "aro_own_citation_in_native_bibliography": False,
        "aro_cited_tested_enzyme_equated_with_reference": False,
        "experimental_identity_primary_review_complete": False,
        "experimental_subject_assignment": False,
    }


def project_landing(payload):
    tree = html.fromstring(payload)
    require(
        tree.xpath('//meta[@name="citation_doi"]/@content') == ["10.1021/acs.jmedchem.8b01393"]
        and tree.xpath('//meta[@name="citation_pdf_url"]/@content')
        == ["https://www.osti.gov/servlets/purl/1484803"]
        and tree.xpath('//meta[@name="citation_title"]/@content')
        == ["Encoding of Promiscuity in an Aminoglycoside Acetyltransferase"],
        "OSTI publication identity changed",
    )
    links = tree.xpath('//a[@href="/servlets/purl/1484803"]')
    require(
        any("Accepted Manuscript" in "".join(a.itertext()) for a in links), "native manuscript link changed"
    )
    return {
        "publication_doi": "10.1021/acs.jmedchem.8b01393",
        "native_pdf_url": "https://www.osti.gov/servlets/purl/1484803",
        "bibliographic_page_is_primary_text": False,
        "access_gate_bypassed": False,
    }


def corpus_context(root, cohort):
    for value in cohort.values():
        if isinstance(value, dict) and set(value) == {"path", "sha256"}:
            reference.check_pin(root, value)
    index = read_json(root, cohort["index"])
    with reference.check_pin(root, cohort["source_inventory"]).open() as stream:
        labels = {r["determinant_id"]: r["determinant_name"] for r in csv.DictReader(stream, delimiter="\t")}
    require(
        {t: n for t, n in labels.items() if re.fullmatch(r"AAC\(3\)-(?:III|IV)[a-z]?", n)} == TERMS,
        "III/IV source-label cohort changed",
    )
    _, body = wrapped(root, cohort["ontology_cache"])
    projected = definitions.project_annotations(definitions.Graph().parse(data=body, format="xml"), TERMS)
    source = read_json(root, cohort["definition_citations"])["terms"]
    for term, label in TERMS.items():
        row = cohort["terms"][term]
        require(
            row["source_label"] == label
            and row["prior_term"] == index["terms"][term]
            and row["definition"] == source[term]
            and all(row["definition"][k] == v for k, v in projected[term].items()),
            "native term definition or current index changed",
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
    ids = {rid for t in cohort["terms"].values() for rid in t["prior_term"]["record_memberships"]}
    records, claims = [r for r in census if r["identifier"] in ids], []
    for row in records:
        doc = load_record(root / row["path"])
        require(
            doc["identifier"] == row["identifier"]
            and doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "structure identity changed",
        )
        for i, claim in enumerate(doc.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in TERMS:
                require(claim["label"] == TERMS[claim["aro_id"]], "claim label changed")
                claims.append(
                    {
                        "record_identifier": doc["identifier"],
                        "position": i,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    require(
        records == cohort["records"]
        and claims == cohort["claims"]
        and len(records) == 14
        and len(claims) == 29,
        "complete claim membership changed",
    )
    return records, claims


def request_sources(root, directory):
    specs = [("metadata-" + p, "metadata-plan.json", metadata_url(p)) for p in QUERY_DIRS]
    specs += [
        ("taxonomy-316", "reference-plan.json", "https://rest.uniprot.org/taxonomy/316.json"),
        ("iiib-reviewed", "reference-plan.json", gene_url(True)),
        ("iiib-unreviewed", "unreviewed-plan.json", gene_url(False)),
        ("metadata-30347146", "reference-citation-plan.json", metadata_url("30347146")),
        ("osti-landing", "osti-plan.json", "https://www.osti.gov/biblio/1484803"),
        ("osti-pdf", "osti-pdf-plan.json", "https://www.osti.gov/servlets/purl/1484803"),
    ]
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == {k for k, _, _ in specs},
            "unexpected request or incomplete planned retrieval",
        )
    for filename in {f for _, f, _ in specs}:
        plan = json.loads((directory / filename).read_bytes())
        require(
            plan["cohort"] == reference.pin(root, directory / "cohort.json")
            and set(plan["requests"]) == {k for k, f, _ in specs if f == filename}
            and plan["ncbi_requests"] == 0
            and plan["automatic_redirects"] is plan["retry_performed"] is False,
            "request-plan constraints changed",
        )
    sources, previous = {}, None
    for key, filename, url in specs:
        source = planned_source(root, directory, key, filename, url, (200,))
        attempt, receipt = (read_json(root, source[k]) for k in ("attempt", "receipt"))
        start, end = (datetime.fromisoformat(v) for v in (attempt["started_at"], receipt["retrieved_at"]))
        require(start <= end and (previous is None or previous <= start), "request chronology changed")
        previous, sources[key] = end, source
    for filename, key in (
        ("metadata-canary-review.json", "metadata-20387903"),
        ("taxonomy-canary-review.json", "taxonomy-316"),
        ("reviewed-gene-canary-review.json", "iiib-reviewed"),
        ("iiib-reference-canary-review.json", "iiib-unreviewed"),
        ("osti-landing-canary-review.json", "osti-landing"),
    ):
        canary = json.loads((directory / filename).read_bytes())
        require(
            all(canary[k] == sources[key][k] for k in ("body", "receipt", "plan")), "canary binding changed"
        )
    fallback = json.loads((directory / "unreviewed-plan.json").read_bytes())
    require(
        fallback["prior_reviewed_canary"]
        == reference.pin(root, directory / "reviewed-gene-canary-review.json"),
        "fallback authorization changed",
    )
    for filename, key, dependency in (
        ("reference-citation-plan.json", "source_reference_canary", "iiib-reference-canary-review.json"),
        ("osti-plan.json", "source_metadata_review", "reference-citation-review.json"),
        ("osti-pdf-plan.json", "source_landing_canary", "osti-landing-canary-review.json"),
    ):
        plan = json.loads((directory / filename).read_bytes())
        require(plan[key] == reference.pin(root, directory / dependency), "primary-route dependency changed")
    return sources


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    require(
        reference.digest(directory / "source-selection.json") == SELECTION_SHA, "source selection changed"
    )
    cohort, selection = (
        json.loads((directory / n).read_bytes()) for n in ("cohort.json", "source-selection.json")
    )
    records, claims = corpus_context(root, cohort)
    requests = request_sources(root, directory)
    require(
        reference.digest(directory / "reference-citation-review.json") == REFERENCE_CITATION_REVIEW_SHA
        and reference.digest(directory / "primary-context-review.json") == PRIMARY_REVIEW_SHA,
        "inspected reference-citation or primary context changed",
    )
    metadata = {}
    for pmid, inspected in selection["metadata"].items():
        require(inspected["body"] == requests["metadata-" + pmid]["body"], "metadata pin changed")
        metadata[pmid] = project_metadata(read_json(root, inspected["body"]), pmid, inspected)
    inspected = json.loads((directory / "reference-citation-review.json").read_bytes())
    require(
        inspected["body"] == requests["metadata-30347146"]["body"], "native citation metadata pin changed"
    )
    metadata["30347146"] = project_metadata(read_json(root, inspected["body"]), "30347146", inspected)
    landing = project_landing(reference.check_pin(root, requests["osti-landing"]["body"]).read_bytes())
    primary = json.loads((directory / "primary-context-review.json").read_bytes())
    require(
        primary["source_pdf"] == requests["osti-pdf"]["body"]
        and primary["receipt"] == requests["osti-pdf"]["receipt"]
        and reference.check_pin(root, primary["source_pdf"]).read_bytes().startswith(b"%PDF-")
        and primary["visually_reviewed_pages_one_based"] == [1, 2, 3, 9]
        and primary["document_version"] == "JUST_ACCEPTED_MANUSCRIPT_NOT_VERSION_OF_RECORD"
        and primary["manual_visual_inspection_completed"] is True
        and primary["whole_paper_reviewed"] is False,
        "selected manuscript context changed",
    )
    for page in primary["selected_pages"]:
        reference.check_pin(root, page["render"])
    native_taxa, tax_sources = {}, {}
    for taxid, item in selection["native_taxonomy"].items():
        wrapper = read_json(root, item)
        native_taxa[taxid], tax_sources[taxid] = read_source(root, {"wrapper": item, "url": wrapper["url"]})
        require(native_taxa[taxid]["taxonId"] == int(taxid), "native taxonomy identity changed")
        lineage(native_taxa[taxid])
    native_taxa["316"], tax_sources["316"] = read_source(root, requests["taxonomy-316"])
    require(
        native_taxa["316"]["taxonId"] == 316
        and native_taxa["316"]["scientificName"] == "Stutzerimonas stutzeri"
        and "Pseudomonas stutzeri" in native_taxa["316"]["synonyms"],
        "source-name synonym context changed",
    )
    snapshot = read_json(root, cohort["direct_proteins"])["entries"]
    direct = {}
    require(selection["direct_reference_accessions"] == DIRECT, "sibling reference selection changed")
    for term, accession in DIRECT.items():
        wrapper, body = wrapped(root, selection["native_protein_pages"][accession])
        headers = {k.lower(): v for k, v in wrapper["headers"].items()}
        require(headers["x-uniprot-release"] == "2026_03", "sibling reference release changed")
        entries = [e for e in json.loads(body)["results"] if e["primaryAccession"] == accession]
        require(len(entries) == 1 and entries[0] == snapshot[accession], "native sibling reference changed")
        entry = entries[0]
        require(
            any(x["database"] == "CARD" and x["id"] == term for x in entry["uniProtKBCrossReferences"]),
            "explicit CARD link missing",
        )
        taxon = native_taxa[str(entry["organism"]["taxonId"])]
        direct[term] = {
            **project_protein(entry),
            "explicit_card_xref": term,
            "reference_taxon_native_rank": taxon["rank"],
            "primary_results_reviewed": False,
            "scope": "EXISTING_EXPLICIT_REFERENCE_NOT_NEW_RESISTANCE_GROUNDING",
        }
    pools, queries = {}, {}
    for pmid, path in QUERY_DIRS.items():
        pools[pmid], queries[pmid] = literature.read_query(root, root / path, pmid)
    require(
        {"entries": pools, "queries": queries} == read_json(root, cohort["literature"]),
        "cached literature changed",
    )
    require(
        {k: len(v) for k, v in pools.items()} == {"20387903": 0, "19709289": 16, "6318050": 2},
        "citation pool counts changed",
    )
    pool = {a: e for entries in pools.values() for a, e in entries.items()}
    related = {
        a: project_related(
            pool[a], native_taxa[str(RELATED[a][1])], ["PMID:" + p for p in sorted(pools) if a in pools[p]]
        )
        for a in RELATED
    }
    excluded = [
        {**project_protein(pool[a]), "disposition": "INCIDENTAL_OR_OTHER_ENZYME_NOT_IVa_REFERENCE"}
        for a in sorted(set(pool) - set(RELATED))
    ]
    require(len(pool) == 18 and len(excluded) == 15, "incidental-citation accounting changed")
    gene_queries, iiib_reference = {}, None
    for key, reviewed in (("iiib-reviewed", True), ("iiib-unreviewed", False)):
        data, source = read_source(root, requests[key])
        require(
            requests[key]["url"] == gene_url(reviewed) and len(data["results"]) == (0 if reviewed else 1),
            "exact-label query membership changed",
        )
        if not reviewed:
            iiib_reference = project_iiib(data["results"][0], native_taxa["287"])
        gene_queries[key] = {
            "source": source,
            "reviewed_subset": reviewed,
            "result_count": len(data["results"]),
            "complete_for_query": True,
            "biological_absence_inferred": False,
            "suggestions_followed": False,
            "query_scope": "EXACT_SOURCE_LABEL_AND_PSEUDOMONAS_AERUGINOSA_TAXONOMY",
        }
    new_memberships = [
        {
            "record_identifier": rid,
            "source_term_id": "ARO:3002537",
            "protein_accession": iiib_reference["accession"],
            "scope": iiib_reference["scope"],
            "experimental_allele_assigned": False,
        }
        for rid in cohort["terms"]["ARO:3002537"]["prior_term"]["record_memberships"]
    ]
    require(len(new_memberships) == 9, "IIIb reference membership changed")
    iiib_reference["selected_primary_context_reviewed"] = True
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "source_selection": reference.pin(root, directory / "source-selection.json"),
            "prior_verification": cohort["previous_verification"],
            "reference_citation_review": reference.pin(root, directory / "reference-citation-review.json"),
            "primary_context_review": reference.pin(root, directory / "primary-context-review.json"),
        },
        "terms": cohort["terms"],
        "records": records,
        "claims": claims,
        "existing_explicit_references": direct,
        "type_iv_related_references": related,
        "incidental_citation_hits_not_selected": excluded,
        "literature_queries": queries,
        "iiib_exact_label_queries": gene_queries,
        "new_iiib_gene_reference": iiib_reference,
        "new_gene_reference_memberships": new_memberships,
        "metadata": metadata,
        "primary_route": landing,
        "selected_primary_context": primary,
        "request_sources": requests,
        "reference_taxonomy_sources": tax_sources,
        "iiib_source_organism_context": {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "native_rank": native_taxa["287"]["rank"],
            "basis": "ARO_DEFINITION_AND_UNIPROT_TAXONOMY_REFERENCE_ONLY",
            "reference_protein_accession": iiib_reference["accession"],
            "experimental_subject_assigned": False,
        },
        "summary": {
            "source_terms": 5,
            "source_claims": 29,
            "cohort_records": 14,
            "corpus_records_hash_checked": 2939,
            "existing_explicit_reference_links_rechecked": 3,
            "type_iv_related_references_without_exact_iva_mapping": 3,
            "fragment_references": 2,
            "incidental_citation_hits_not_selected": 15,
            "reused_complete_citation_queries": 3,
            "new_exact_label_queries": 2,
            "new_gene_reference_links": 1,
            "new_gene_reference_memberships": 9,
            "native_reference_taxa_checked": 5,
            "metadata_only_papers": 3,
            "selected_primary_context_reviews": 1,
            "primary_pdf_pages_visually_reviewed": 4,
        },
        "disposition": {
            "biological_records_changed": 0,
            "new_exact_card_protein_memberships": 0,
            "experimental_gene_allele_assignments": 0,
            "experimental_genome_assignments": 0,
            "new_verified_resistance_results": 0,
            "whole_record_primary_signoffs": 0,
            "generic_type_iv_is_exact_iva": False,
            "related_gene_is_iiib": False,
            "reference_organism_transferred_to_experimental_subject": False,
        },
        "constraints": {
            "new_requests": 9,
            "new_metadata_requests": 4,
            "new_uniprot_requests": 3,
            "new_primary_route_requests": 2,
            "new_primary_texts": 1,
            "ncbi_requests": 0,
            "retry_performed": False,
            "redirects_followed": False,
            "prior_source_holds_preserved": True,
            "new_access_holds": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "github_mutations": 0,
            "outreach": 0,
            "source_adoptions": 0,
            "sequence_variant_protocol_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "limitations": [
            "The three focal citations remain metadata-only; no primary tables or supplements were reviewed.",
            "Subscription links and non-OA metadata are not observed access denials "
            "or proof of unavailable full text.",
            "The IIIb biochemical citation does not establish organismal AST "
            "for its nine inherited memberships.",
            "Empty exact-label and citation queries do not exclude other names, "
            "unindexed references or biological presence.",
            "Generic type IV, aacC4 and type IVa are not silently asserted to be the same allele.",
            "Fragment entries remain fragments; the generic Salmonella reference "
            "is not forced into another species.",
            "Native Stutzerimonas/Pseudomonas synonymy resolves reference naming, "
            "not experimental strain identity.",
            "The adjacent hygromycin-resistance enzyme and plasmid-replication proteins are not AAC(3)-IVa.",
            "Existing explicit IIIa, IIIc and IVb CARD links are neither new discoveries "
            "nor independent phenotype results.",
            "The archived 2018 manuscript has selected structural context review, "
            "not whole-paper, supplement, experimental-allele or clinical-resistance signoff.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt Consortium reference metadata, release 2026_03. Bibliographic metadata: Europe PMC at EBI. "
        "Kumar et al., J. Med. Chem. (2018), DOI:10.1021/acs.jmedchem.8b01393; "
        "accepted manuscript served by OSTI, not the version of record. "
        "No source adopted or primary article text exported.",
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

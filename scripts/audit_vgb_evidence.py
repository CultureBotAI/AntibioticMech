"""Replay Vgb reference and primary-context evidence without assigning resistant alleles."""

import argparse
import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import audit_card_definition_citations as definitions
import audit_card_literature_expansion as literature
import audit_card_outer_membrane_references as shared
import audit_card_structure_links as structures
from audit_card_reference_lineages import lineage
from audit_fungamr_cohort import read_source
from audit_valinomycin_abcb1 import planned_source
from lxml import etree

from antibioticmech.activity_collections import load_record

reference, require = shared.reference, shared.require
CACHE = Path("reports/resistance-grounding-2026-10-15-vgb-evidence")
OUTPUT = Path("research/2026-10-15-vgb-evidence.json")
SCOPE = "VGB_REFERENCE_AND_PRIMARY_CONTEXT_NOT_EXPERIMENTAL_ALLELE_ASSIGNMENT"
TERMS = {"ARO:3001307": "vgbA", "ARO:3001308": "vgbB", "ARO:3003990": "vgbC"}
COHORT_SHA = "f36d8954536f9d61876a91ca09e61c86ab98983285a95dcd833362d1fe87a07d"
REVIEW_SHA = "30ecd4db3877dd7eb90632bb426e89b94cd30f4355d8aa8abfa0bae39463c90f"
PRIMARY_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5155152/fullTextXML"
PUBLICATION = {
    "id": "27929110",
    "doi": "10.1038/ncomms13803",
    "pmcid": "PMC5155152",
    "title": "A diverse intrinsic antibiotic resistome from a cave bacterium.",
    "isOpenAccess": "Y",
}


def read_json(root, item):
    return json.loads(reference.check_pin(root, item).read_bytes())


def wrapped(root, item, url=None):
    row = read_json(root, item)
    body = row["body"].encode()
    require(
        row["status"] == 200
        and (url is None or row["url"] == url)
        and row["sha256"] == hashlib.sha256(body).hexdigest()
        and row.get("bytes", len(body)) == len(body),
        "native wrapper identity or payload changed",
    )
    return row, body


def project_metadata(data):
    rows = data["resultList"]["result"]
    require(
        type(data["hitCount"]) is int
        and data["hitCount"] == len(rows) == 1
        and not data.get("nextCursorMark")
        and data["request"]["queryString"] == "EXT_ID:27929110 AND SRC:MED",
        "metadata query changed",
    )
    row = rows[0]
    require(
        row["source"] == "MED"
        and row["pmid"] == PUBLICATION["id"]
        and {k: row[k] for k in PUBLICATION} == PUBLICATION,
        "publication identity changed",
    )
    return dict(PUBLICATION)


def text(node):
    return " ".join("".join(node.itertext()).split())


def project_primary(payload):
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): text(n) for n in tree.xpath("./front/article-meta/article-id")}
    require(
        ids.get("pmid") == "27929110" and ids.get("doi") == PUBLICATION["doi"], "primary identity changed"
    )
    tables = tree.xpath('//table-wrap[@id="t1"]')
    require(len(tables) == 1, "primary table missing or ambiguous")
    table = tables[0]
    rows = [r for r in table.xpath(".//tr") if any(text(c) == "vgbC" for c in r.findall("td"))]
    require(len(rows) == 1, "VgbC table row missing or ambiguous")
    cells = [text(c) for c in rows[0].findall("td")]
    require(
        cells == ["Streptogramin B lyase", "vgbC", "Streptogramin B", "Linopristin", "", "NA*"],
        "VgbC table cells or column positions changed",
    )
    footnotes = table.xpath('.//fn[@id="t1-fn2"]')
    require(
        len(footnotes) == 1
        and text(footnotes[0])
        == "*The E. coli MIC for linopristin is >128 \u03bcg ml\u22121, the highest soluble concentration."
        and rows[0].xpath("./td[6]/xref/@rid") == ["t1-fn2"],
        "VgbC control footnote changed",
    )
    paragraphs = [p for p in tree.xpath('//sec[@id="sec2"]/p') if "(Vgb)" in text(p)]
    require(len(paragraphs) == 1, "VgbC Results paragraph changed")
    availability = tree.xpath('//sec[@id="sec27"]/p')
    require(len(availability) == 1 and "JFOM00000000" in text(availability[0]), "WGS context changed")
    return {
        "publication": dict(PUBLICATION),
        "results_location": "Results / Paenibacillus sp. LC231 is multi-drug resistant",
        "results_paragraph_sha256": hashlib.sha256(text(paragraphs[0]).encode()).hexdigest(),
        "table_location": "Table 1, vgbC row and footnote t1-fn2",
        "antibiotic_source_label": cells[3],
        "determinant_mic_cell": cells[4],
        "control_mic_cell": cells[5],
        "control_footnote_scope": "SOLUBILITY_LIMIT_NOT_A_VGBC_EFFECT_SIZE",
        "quantitative_vgbc_mic_effect_established": False,
        "blank_or_na_imputed": False,
        "broad_results_statement_overrides_table": False,
        "native_isolate_contribution_established": False,
        "source_wgs_project": "JFOM00000000",
        "wgs_project_is_versioned_assembly": False,
        "determinant_accession_selected_from_range": False,
        "experimental_genome_assignment": None,
    }


def project_taxon(taxon, taxid, name):
    nodes, species = lineage(taxon)
    require(
        taxon["taxonId"] == taxid
        and taxon["scientificName"] == name
        and taxon["rank"] == "species"
        and species == nodes[-1],
        "reference taxonomy identity or rank changed",
    )
    return {
        "taxon_id": "NCBITaxon:" + str(taxid),
        "scientific_name": name,
        "native_rank": taxon["rank"],
        "active": taxon["active"],
        "parent": taxon["parent"],
        "lineage": nodes,
        "strain_label_in_name_changes_rank": False,
        "experimental_subject_assignment": False,
    }


def project_protein(entry):
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "entry_audit": entry["entryAudit"],
        "gene_symbols": [g["geneName"]["value"] for g in entry.get("genes", []) if "geneName" in g],
        "reference_taxon_id": "NCBITaxon:" + str(entry["organism"]["taxonId"]),
        "reference_taxon_label": entry["organism"]["scientificName"],
        "experimental_allele_assignment": None,
    }


def corpus_context(root, cohort):
    for value in cohort.values():
        if isinstance(value, dict) and set(value) == {"path", "sha256"}:
            reference.check_pin(root, value)
    index = read_json(root, cohort["index"])
    with reference.check_pin(root, cohort["source_inventory"]).open() as stream:
        labels = {r["determinant_id"]: r["determinant_name"] for r in csv.DictReader(stream, delimiter="\t")}
    pattern = r"\bvgb\w*|streptogramin B.*(?:lyase|hydrolase)|virginiamycin B.*(?:lyase|hydrolase)"
    require(
        {t: n for t, n in labels.items() if re.search(pattern, n, re.I)} == TERMS, "Vgb label cohort changed"
    )
    _, body = wrapped(root, cohort["ontology_cache"])
    projected = definitions.project_annotations(definitions.Graph().parse(data=body, format="xml"), TERMS)
    definitions_snapshot = read_json(root, cohort["definition_citations"])["terms"]
    for term, label in TERMS.items():
        frozen = cohort["terms"][term]
        require(
            frozen["source_label"] == label
            and frozen["prior_term"] == index["terms"][term]
            and frozen["definition"] == definitions_snapshot[term]
            and all(frozen["definition"][k] == v for k, v in projected[term].items()),
            "native definition or term context changed",
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
        and len(records) == 9
        and len(claims) == 27,
        "claim membership changed",
    )
    return records, claims


def reused_context(root, cohort, review):
    sources = review["sources"]
    for item in sources.values():
        reference.check_pin(root, item)
    frozen = read_json(root, cohort["literature"])
    entries, queries = {}, {}
    for pmid in cohort["literature_pmids"]:
        entries[pmid], queries[pmid] = literature.read_query(root, root / literature.DIRECTORY, pmid)
    require({"entries": entries, "queries": queries} == frozen, "cached literature changed")
    require(
        {k: sorted(v) for k, v in entries.items()}
        == {
            "11467949": ["P17978", "Q7W0D3", "Q9KZX7"],
            "15734650": [],
            "17563376": ["P17978"],
            "27929110": [],
        },
        "literature result membership changed",
    )
    old_structure = read_json(root, cohort["structural_context"])["links"]["ARO:3001307"]
    _, native, _ = structures.receipt(root, root / sources["vgba_pdb"]["path"], "data.rcsb.org")
    (entry,) = native["data"]["entries"]
    require(
        entry["rcsb_id"] == "2Z2P"
        and structures.entity_references(entry) == old_structure["structures"][0]["entities"]
        and old_structure["context_review"]["decision"]
        == "INACTIVE_STRUCTURAL_REFERENCE_NOT_RESISTANCE_SUBJECT",
        "inactive structural reference context changed",
    )
    page, body = wrapped(root, sources["vgbb_page"])
    require(
        urlsplit(page["url"]).hostname == "rest.uniprot.org"
        and {k.lower(): v for k, v in page["headers"].items()}["x-uniprot-release"] == "2026_03",
        "VgbB source changed",
    )
    selected = [e for e in json.loads(body)["results"] if e["primaryAccession"] == "O87275"]
    require(
        len(selected) == 1 and selected[0] == read_json(root, cohort["direct_proteins"])["entries"]["O87275"],
        "VgbB aggregate differs from native page",
    )
    require(
        any(
            x["database"] == "CARD" and x["id"] == "ARO:3001308"
            for x in selected[0]["uniProtKBCrossReferences"]
        ),
        "VgbB CARD cross-reference missing",
    )
    taxa, taxonomy_sources = {}, {}
    for key, query in (
        ("vgbb_taxonomy", None),
        ("lc231_taxonomy", "LC231"),
        ("lc231_proteins", "organism_id:1120679"),
    ):
        wrapper = read_json(root, sources[key])
        data, taxonomy_sources[key] = read_source(root, {"wrapper": sources[key], "url": wrapper["url"]})
        if query:
            require(parse_qs(urlsplit(wrapper["url"]).query)["query"] == [query], "query scope changed")
        if key == "lc231_proteins":
            require(data["results"] == [], "new exact-taxon proteins require review")
        else:
            taxa[key] = data["results"][0] if query else data
            if query:
                require(len(data["results"]) == 1, "LC231 taxonomy ambiguous")
    hold_context = read_json(root, cohort["prior_primary_context"])
    holds = [
        r
        for r in hold_context["access_limitations"]["publisher_web_results"]
        if r["url"] == "https://www.pnas.org/doi/10.1073/pnas.0701809104"
    ]
    require(len(holds) == 1 and holds[0]["result"] == "403", "prior VgbA primary hold changed")
    return {
        "literature_queries": queries,
        "shared_citation_hits_not_automatic_vgba_assignments": [
            project_protein(e) for e in entries["11467949"].values()
        ],
        "vgba": {
            "prior_structure_link": old_structure,
            "reference_protein": project_protein(entries["17563376"]["P17978"]),
            "primary_access_hold": holds[0],
            "primary_results_reviewed": False,
            "hold_preserved_no_retry_or_alternate": True,
        },
        "vgbb": {
            "reference_protein": project_protein(selected[0]),
            "explicit_card_xref": "ARO:3001308",
            "taxonomy": project_taxon(taxa["vgbb_taxonomy"], 29382, "Staphylococcus cohnii"),
            "primary_results_reviewed": False,
        },
        "vgbc": {
            "source_organism": "Paenibacillus sp. LC231",
            "source_strain_label": "LC231",
            "taxonomy": project_taxon(taxa["lc231_taxonomy"], 1120679, "Paenibacillus sp. (strain LC231)"),
            "protein_accession_assigned": None,
            "exact_organism_query_count": 0,
            "query_scope": "EXACT_ORGANISM_ID_NOT_GLOBAL_OR_DESCENDANT_TAXON_ABSENCE",
            "biological_absence_inferred": False,
        },
        "taxonomy_and_exact_organism_query_sources": taxonomy_sources,
    }


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    require(
        reference.digest(directory / "source-review.json") == REVIEW_SHA, "inspected source review changed"
    )
    cohort, review = (json.loads((directory / n).read_bytes()) for n in ("cohort.json", "source-review.json"))
    records, claims = corpus_context(root, cohort)
    context = reused_context(root, cohort, review)
    sources = review["sources"]
    old_metadata, body = wrapped(root, sources["metadata"])
    metadata = project_metadata(json.loads(body))
    key = "metadata-27929110"
    plan = json.loads((directory / "metadata-plan.json").read_bytes())
    require(
        set(plan["requests"]) == {key}
        and plan["cohort"] == reference.pin(root, directory / "cohort.json")
        and plan["ncbi_requests"] == 0
        and plan["retry_performed"] is plan["automatic_redirects"] is False,
        "request plan changed",
    )
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require({p.name for p in directory.glob("*" + suffix)} == {key + suffix}, "unexpected new request")
    url = plan["requests"][key]["url"]
    require(
        url
        == "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27929110+AND+SRC%3AMED&format=json&resultType=core&pageSize=1",
        "new metadata route changed",
    )
    new_source = planned_source(root, directory, key, "metadata-plan.json", url, (200,))
    require(
        new_source["body"]["sha256"] == "fc3413827f7252cbe2cb12609407706f6d03722fa4330ac69bf38fafb3d69529",
        "metadata snapshot changed",
    )
    require(
        project_metadata(json.loads((directory / (key + "-response.bin")).read_bytes())) == metadata,
        "metadata snapshots disagree",
    )
    _, body = wrapped(root, sources["primary"], PRIMARY_URL)
    primary = project_primary(body)
    receipt = read_json(root, sources["supplement_receipt"])
    require(
        receipt["status"] == 200
        and receipt["sha256"] == sources["supplement_archive"]["sha256"]
        and receipt["url"] == PRIMARY_URL.replace("fullTextXML", "supplementaryFiles"),
        "supplement receipt changed",
    )
    with zipfile.ZipFile(root / sources["supplement_archive"]["path"]) as archive:
        require(
            hashlib.sha256(archive.read("ncomms13803-s1.pdf")).hexdigest()
            == sources["supplement_pdf"]["sha256"],
            "supplement member changed",
        )
    for render in review["renders"]:
        reference.check_pin(root, render)
    require(review["visually_reviewed_pages_one_based"] == [1, 7, 8, 9, 11], "PDF review scope changed")
    return {
        "date": "2026-10-15",
        "scope": SCOPE,
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "source_review": reference.pin(root, directory / "source-review.json"),
            **sources,
        },
        "terms": cohort["terms"],
        "records": records,
        "claims": claims,
        "references": context,
        "primary_context": primary,
        "supplement_review": {k: v for k, v in review.items() if k != "sources"},
        "metadata": {
            "identity": metadata,
            "earlier_snapshot": sources["metadata"],
            "new_snapshot": new_source,
            "earlier_retrieved_at": old_metadata["retrieved_at"],
            "repeat_lookup_acknowledged": True,
        },
        "disposition": {
            "biological_records_changed": 0,
            "experimental_gene_allele_assignments": 0,
            "new_protein_memberships": 0,
            "new_verified_resistance_results": 0,
            "whole_record_reviews_completed": 0,
            "linopristin_evidence_propagated_to_inherited_memberships": False,
            "reference_or_taxon_context_promoted_to_experimental_subject": False,
        },
        "summary": {
            "source_terms": 3,
            "source_claims": len(claims),
            "cohort_records": len(records),
            "corpus_records_hash_checked": 2939,
            "reused_complete_literature_queries": 4,
            "selected_primary_context_reviews": 1,
            "selected_supplement_pages_reviewed": 5,
        },
        "constraints": {
            "new_requests": 1,
            "new_metadata_requests": 1,
            "new_primary_requests": 0,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "retry_after_denial": False,
            "alternate_routes_used": False,
            "prior_source_holds_preserved": True,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "github_mutations": 0,
            "outreach": 0,
            "source_adoptions": 0,
            "sequence_variant_protocol_exported": False,
            "full_corpus_goal_status": "OPEN",
        },
        "limitations": [
            "The nine inherited CARD memberships are not nine independently measured drug results.",
            "Linopristin primary evidence does not establish exact-compound results "
            "for the nine selected structures.",
            "The native phenotype, predicted determinant, heterologous host and purified enzyme "
            "are distinct evidence scopes.",
            "A species-ranked taxonomy entry with a strain label is not silently re-ranked as a strain.",
            "The VgbA-relative host in Table S3 is not the VgbC source organism.",
            "VgbA and VgbB primary-results reviews remain open; "
            "an inactive structure cannot ground a resistant allele.",
            "The exact-organism and own-citation UniProt nonmatches are release/query-scoped, "
            "not biological absence.",
            "A repeated metadata request preceded discovery of old wrapper filenames; "
            "both snapshots are retained.",
            "No exact experimental allele, versioned assembly or record-specific "
            "clinical interpretation was assigned.",
        ],
        "attribution": "CARD/ARO ontology: McMaster University, CC BY 4.0. "
        "UniProt Consortium reference metadata. "
        "RCSB PDB reference metadata. Pawlowski et al., Nature Communications 7:13803 (2016), CC BY 4.0; "
        "selected primary and supplement context reused from the EBI Europe PMC cache. No source adoption.",
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

"""Replay congener, salt-form and reference-organism boundaries offline."""

import argparse
import csv
import hashlib
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-streptothricin")
OUTPUT = Path("research/2026-10-14-streptothricin-context.json")
COHORT_SHA = "1719a147c402eab31a76890110ab7c2dd345bc96780cad796d65f1f85ed5a0c1"
ARTICLE_SHA = "55d0f05949ca81f8f92b1a99b8f00b46e175d9fb8302a82da4893b08ce4e2cc4"
DOI = "10.1371/journal.pbio.3002091"
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "lit_pubmed_id,sequence_version,version"
)
RECORDS = {
    "CHEBI:60821": ("NRAUADCLPJTGSF-VLSXYIQESA-N", 0, 5),
    "CHEBI:60828": ("WUJTXMVGXDQPNN-OTQKCRDJSA-N", 0, 0),
    "CHEBI:60822": ("NRAUADCLPJTGSF-VLSXYIQESA-Q", 3, 0),
}
SUPPLEMENTS = {
    "chemical-f": {
        "suffix": "s014",
        "label": "S1 Fig",
        "congener": "F",
        "sha256": "cae00b8b0cdca5c70155f325e16882efdfec4df553fbc5fd2022f092b0a76539",
        "page_sha256": "047b8180e004d293b7b5e204582bda98031f53b5eb7d46b0355fd49ea74ac38e",
        "reported_formula": "C19H34N8O8 . 3/2 H2SO4 . 3 H2O",
    },
    "chemical-d": {
        "suffix": "s015",
        "label": "S2 Fig",
        "congener": "D",
        "sha256": "63ba32c93a9aa20f9016857c975438a75347b1508b260109d547ba9a2de7a5c3",
        "page_sha256": "6f06b10bcb3b65926a3b81c433205af9c1b7a9c2ad20a14df9bd37ebd8e26b0c",
        "reported_formula": "C31H58N12O10 . 5/2 H2SO4 . 5 H2O",
    },
}


def text_hash(element):
    if element is None:
        raise ValueError("reviewed evidence location missing")
    text = " ".join("".join(element.itertext()).split())
    return hashlib.sha256(text.encode()).hexdigest()


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = ET.fromstring(payload)
    ids = {e.get("pub-id-type"): e.text for e in tree.findall("./front/article-meta/article-id")}
    if ids.get("pmid") != "37192172" or ids.get("doi") != DOI:
        raise ValueError("primary citation identity changed")
    locations = {
        "congener_identity": ".//sec[@id='sec003']/p[1]",
        "mixture_composition": ".//sec[@id='sec003']/p[3]",
        "chemical_source": ".//sec[@id='sec014']/p[1]",
        "structure_caption": ".//fig[@id='pbio.3002091.g001']/caption",
        "rna_table_caption": ".//table-wrap[@id='pbio.3002091.t001']/caption",
    }
    mixture = tree.find(locations["mixture_composition"])
    if mixture is None or "natural product mixture" not in "".join(mixture.itertext()):
        raise ValueError("mixture evidence changed")
    for item in SUPPLEMENTS.values():
        supplement = tree.find(f".//supplementary-material[@id='pbio.3002091.{item['suffix']}']")
        if supplement is None or supplement.findtext("label") != item["label"]:
            raise ValueError("chemical supplement identity changed")
        media = supplement.find("media")
        if (
            media is None
            or media.get("{http://www.w3.org/1999/xlink}href") != f"pbio.3002091.{item['suffix']}.pdf"
        ):
            raise ValueError("chemical supplement filename changed")
    return {
        "reference": "DOI:" + DOI,
        "pmid": "PMID:37192172",
        "locations": {
            key: {"xpath": path, "text_sha256": text_hash(tree.find(path))} for key, path in locations.items()
        },
        "findings": [
            "The studied nourseothricin preparation is a congener mixture, not isolated streptothricin F.",
            "The paper distinguishes isolated F and D material from mixture-level observations.",
            "Resistance to other antibiotics in an isolate cohort is not resistance "
            "to the tested streptothricin.",
        ],
        "reported_endpoint": "MIC",
        "reported_source_units": "micromolar",
        "numeric_AST_exported": False,
        "mass_conversion_performed": False,
        "rna_scope": {
            "basis": "Table 1 caption only; mutant-level results not reviewed in this checkpoint",
            "entity_type": "RIBOSOMAL_RNA",
            "protein_accession_applicable_to_rna": False,
            "experimental_allele_assignment": None,
        },
        "review_scope": "CHEMICAL_IDENTITY_AND_EVIDENCE_BOUNDARIES_NOT_COMPLETE_RESISTANCE_REVIEW",
        "individual_isolate_AST_reviewed": False,
        "experimental_genome_assignment": None,
        "mixture_findings_transferred_to_single_structure": False,
    }


def project_sata(payload, headers, taxonomy):
    headers = {k.lower(): v for k, v in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != 1
        or not isinstance(payload["results"][0], dict)
        or headers.get("x-uniprot-release") != "2026_03"
        or headers.get("x-total-results") != "1"
        or headers.get("link")
    ):
        raise ValueError("publication reference query incomplete or changed")
    entry = payload["results"][0]
    if {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned operational reference payload")
    result = reference.project_reference(entry, "satA", 1423, taxonomy)
    if (
        result["protein_accession"] != "UniProtKB:P37506"
        or result["entry_version"] != 136
        or result["sequence_version"] != 1
        or result["gene_names"] != ["satA", "yyaR"]
        or result["ordered_locus_names"] != ["BSU40740"]
        or result["reference_taxon_id"] != "NCBITaxon:224308"
        or result["reference_taxon_rank"] != "strain"
        or result["reference_organism_name"] != result["reference_taxon_scientific_name"]
        or result["reference_organism_name"] != "Bacillus subtilis (strain 168)"
    ):
        raise ValueError("publication-linked reference identity changed")
    wanted = {("PubMed", "28842538"), ("DOI", "10.1128/aem.01590-17")}
    if not any(
        wanted <= {(i["database"], i["id"]) for i in c["identifiers"]} for c in result["bibliography"]
    ):
        raise ValueError("primary reference bibliography link changed")
    result["reference_species_taxon_id"] = result.pop("source_species_taxon_id")
    return {
        **result,
        "role": "REFERENCE_ONLY_NOT_TESTED_ALLELE_OR_SUBJECT",
        "release": "2026_03",
        "primary_results_reviewed": False,
    }


def chemical_source(root, directory, key):
    expected = SUPPLEMENTS[key]
    public_url = (
        f"https://journals.plos.org/plosbiology/article/file?id={DOI}.{expected['suffix']}&type=supplementary"
    )
    redirect = planned_source(root, directory, key, "chemical-supplements-plan.json", public_url, (302,))
    receipt = json.loads(reference.check_pin(root, redirect["receipt"]).read_bytes())
    target = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
    parsed = urlsplit(target)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "storage.googleapis.com"
        or parsed.path != f"/plos-corpus-prod/{DOI}/1/pbio.3002091.{expected['suffix']}.pdf"
        or parsed.fragment
    ):
        raise ValueError("publisher chemical supplement destination changed")
    plan_name = key + "-redirect-plan.json"
    plan = json.loads((directory / plan_name).read_bytes())
    if plan["redirect_receipt"] != redirect["receipt"] or plan.get("manual_redirect_reviewed") is not True:
        raise ValueError("manual redirect is not bound to publisher response")
    pdf = planned_source(root, directory, key + "-pdf", plan_name, target)
    if pdf["body"]["sha256"] != expected["sha256"]:
        raise ValueError("reviewed chemical PDF changed")
    page = directory / (key + "-page-1.png")
    if reference.digest(page) != expected["page_sha256"]:
        raise ValueError("visually reviewed chemical page changed")
    pdf.pop("url", None)
    return {
        "source": redirect,
        "pdf": {**pdf, "url_scope": "EXACT_PUBLISHER_REDIRECT_STORED_IN_PRIVATE_PINNED_RECEIPT"},
        "rendered_page": reference.pin(root, page),
        "pages_visually_reviewed": 1,
        "label": expected["label"],
        "congener": expected["congener"],
        "reported_formula": expected["reported_formula"],
        "reported_material": "SULFATE_HYDRATE",
        "exact_match_to_neutral_record": False,
        "exact_match_to_bare_trication_record": False,
        "active_moiety_equivalence_used_for_curation": False,
    }


def build(root, directory=CACHE):
    directory = root / directory
    expected_requests = {
        "primary-2023",
        "primary-2017",
        "references-2017",
        "chemical-f",
        "chemical-f-pdf",
        "chemical-d",
        "chemical-d-pdf",
    }
    if any(
        {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} != expected_requests
        for suffix in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen research cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in ("census", "protected", "discovery", "source_queue", "card_references"):
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
    records = {}
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        key, charge, count = RECORDS[row["identifier"]]
        if (
            record["identifier"] != row["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != key
            or row["standard_inchi_key"] != key
            or record["chemical_structure"]["charge"] != charge
            or len(record.get("resistance_mechanisms", [])) != count
            or row["sha256"] != row["snapshot"]["sha256"]
            or protected.get(row["path"]) != row["sha256"]
        ):
            raise ValueError("record chemical identity or baseline changed")
        records[row["identifier"]] = record
    if set(records) != set(RECORDS):
        raise ValueError("record cohort incomplete")
    synonyms = records["CHEBI:60821"]["synonyms"]
    if {"synonym_text": "nourseothricin", "synonym_type": "EXACT_SYNONYM", "source": "aro"} not in synonyms:
        raise ValueError("source-owned synonym boundary changed")
    sources = {
        "primary-2023": planned_source(
            root,
            directory,
            "primary-2023",
            "request-plan.json",
            "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10187937/fullTextXML",
        ),
        "primary-2017": planned_source(
            root,
            directory,
            "primary-2017",
            "reference-plan.json",
            "https://journals.asm.org/doi/10.1128/aem.01590-17",
            (403,),
        ),
    }
    primary = primary_context(reference.check_pin(root, sources["primary-2023"]["body"]).read_bytes())
    query_url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {
            "query": "lit_pubmed:28842538",
            "format": "json",
            "size": "500",
            "fields": FIELDS,
        }
    )
    sources["references-2017"] = planned_source(
        root, directory, "references-2017", "reference-plan.json", query_url
    )
    lineage_path = root / "research/2026-10-14-card-reference-lineages.json"
    if reference.digest(lineage_path) != protected[str(lineage_path.relative_to(root))]:
        raise ValueError("prior reference taxonomy checkpoint changed")
    prior = json.loads(lineage_path.read_bytes())
    taxa, tax_sources = {}, {}
    for taxid in ("224308", "405535", "1423", "1396"):
        item = (
            prior["taxa"][taxid]["native_source"]
            if taxid in prior["taxa"]
            else prior["species"][taxid]["native_sources"][0]
        )
        taxa[taxid], tax_sources[taxid] = lineages.native_taxon(root, item, taxid, "2026_03")
    for strain, species in (("224308", "1423"), ("405535", "1396")):
        _, ancestor = lineages.lineage(taxa[strain])
        if ancestor != lineages.identity(taxa[species]) or taxa[species]["rank"] != "species":
            raise ValueError("standalone species and reference lineage disagree")
    response = json.loads(reference.check_pin(root, sources["references-2017"]["body"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, sources["references-2017"]["receipt"]).read_bytes())
    new_reference = project_sata(response, receipt["headers"], taxa["224308"])
    new_reference["retrieved_at"] = receipt["retrieved_at"]
    card = json.loads(reference.check_pin(root, cohort["card_references"]).read_bytes())
    candidates = card["determinants"]["ARO:3005045"]["candidates"]
    if (
        len(candidates) != 1
        or candidates[0]["accession"] != "UniProtKB:B7JE95"
        or candidates[0]["reference_taxon_id"] != "NCBITaxon:405535"
    ):
        raise ValueError("prior CARD reference changed")
    old_reference = {
        k: candidates[0][k]
        for k in ("accession", "entry_audit", "entry_type", "reference_organism_name", "reference_taxon_id")
    }
    if old_reference["reference_organism_name"] != taxa["405535"]["scientificName"]:
        raise ValueError("CARD reference organism differs from native taxonomy")
    forms = {key: chemical_source(root, directory, key) for key in SUPPLEMENTS}
    canary_path = directory / "chemical-canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    following_attempt = json.loads((directory / "chemical-d-attempt.json").read_bytes())
    if (
        canary["body_sha256"] != SUPPLEMENTS["chemical-f"]["sha256"]
        or canary["native_page_visually_reviewed"] is not True
        or canary["remaining_request_authorized"] != "chemical-d"
        or canary["biological_or_experimental_identifier_assignment_authorized"] is not False
        or datetime.fromisoformat(forms["chemical-f"]["pdf"]["retrieved_at"])
        >= datetime.fromisoformat(following_attempt["started_at"])
    ):
        raise ValueError("chemical canary review changed")
    return {
        "date": "2026-10-14",
        "scope": "CONGENER_CHEMICAL_FORM_AND_REFERENCE_CONTEXT_NOT_ALLELE_ASSIGNMENT",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "records": cohort["records"],
        "sources": sources,
        "primary_2023": primary,
        "chemical_forms": forms,
        "chemical_canary": reference.pin(root, canary_path),
        "reference_taxonomy_checkpoint": reference.pin(root, lineage_path),
        "reference_taxonomy_sources": tax_sources,
        "publication_reference": new_reference,
        "prior_card_reference": {
            **old_reference,
            "reference_species_taxon_id": "NCBITaxon:1396",
            "role": "EXISTING_CARD_REFERENCE_NOT_REPLACED_OR_EXPERIMENTALLY_ASSIGNED",
        },
        "reference_interpretation": {
            "same_reference_species": False,
            "interchangeable_accessions": False,
            "source_term_candidate_replaced": False,
            "source_assertion_proven_false": False,
        },
        "source_identity_flag": {
            "record_identifier": "CHEBI:60821",
            "source": "aro",
            "synonym": "nourseothricin",
            "stored_scope": "EXACT_SYNONYM",
            "finding": "This name cannot identify the study's mixture as the exact F structure.",
            "action": "REVIEW_SOURCE_CHEMICAL_SCOPE_BEFORE_PROMOTING_FINDINGS",
            "source_synonym_or_assertions_changed": False,
        },
        "primary_2017_hold": {
            "reference": "PMID:28842538",
            "status": 403,
            "disposition": "ACCESS_HOLD",
            "primary_results_reviewed": False,
            "retry_or_alternate_access_attempted": False,
        },
        "curation_decision": "NO_NEW_EXACT_STRUCTURE_RESISTANCE_CLAIM_FROM_THIS_CHECKPOINT",
        "limits": {
            "scientific_http_attempts": len(expected_requests),
            "manually_reviewed_redirect_hops": 2,
            "automatic_redirects": 0,
            "retries": 0,
            "cached_taxonomy_responses_reused": 4,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "issue_1040": "DEFERRED",
            "source_adoptions": 0,
            "reuse_terms_review_resumed": False,
            "biological_records_changed": 0,
            "new_experimental_identifiers": 0,
            "numeric_AST_or_variants_sequences_constructs_or_protocols_exported": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {"source": "UniProt Consortium", "release": "2026_03", "license": "CC BY 4.0"},
            {
                "source": "Morgan et al., PLOS Biology 2023",
                "reference": "DOI:" + DOI,
                "license": "CC0 as stated in the primary article",
            },
            {
                "source": "CARD/ARO ontology",
                "scope": "previously pinned database assertion and reference link",
            },
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
            raise SystemExit("streptothricin checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "records_scoped": len(result["records"]),
                "new_reference_candidates": 1,
                "chemical_supplement_pages_reviewed": 2,
                "resistance_claims_added": 0,
            }
        )
    )


if __name__ == "__main__":
    main()

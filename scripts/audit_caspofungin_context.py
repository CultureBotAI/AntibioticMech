"""Replay paper-locus mappings without assigning experimental alleles or genomes."""

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlencode, urljoin, urlsplit

import audit_fungamr_cohort as cohort_audit
import audit_fungamr_references as fungal
import audit_topoisomerase_references as reference
from lxml import html
from resistance_checkpoint_records import checkpoint_path

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-caspofungin-context")
OUTPUT = Path("research/2026-10-13-caspofungin-context.json")
DOI = "10.1371/journal.ppat.1002718"
ARTICLE = "https://journals.plos.org/plospathogens/article?id=" + DOI
FIELDS = ("accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
          "xref_geneid,sequence_version,version")
LOCI = {
    "CDC6": ("ARO:3009390", "2890231", "CAGL0K00605g", "Q6FNE4", 136),
    "MRPL11": ("ARO:3009372", "2889720", "CAGL0J09724g", "Q6FNR2", 102),
}


def project_locus(entry, taxonomy, locus):
    """A printed systematic locus is not an inferred gene-symbol synonym."""
    blocks = [
        b for b in entry.get("genes", []) if locus in [v["value"] for v in b.get("orderedLocusNames", [])]
    ]
    species = [t for t in taxonomy.get("lineage", []) if t.get("rank") == "species"]
    versions = entry.get("entryAudit", {})
    names = entry.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {})
    if (
        entry.get("entryType") != "UniProtKB unreviewed (TrEMBL)"
        or "sequence" in entry
        or "features" in entry
        or len(blocks) != 1
        or len(entry.get("genes", [])) != 1
        or any("geneName" in b or b.get("synonyms") for b in entry.get("genes", []))
        or [v["value"] for v in blocks[0]["orderedLocusNames"]].count(locus) != 1
        or entry.get("organism", {}).get("taxonId") != 284593
        or taxonomy.get("taxonId") != 284593
        or taxonomy.get("active") is not True
        or taxonomy.get("rank") != "strain"
        or len(species) != 1
        or species[0].get("taxonId") != 5478
        or species[0].get("scientificName") != "Candida glabrata"
        or entry["organism"].get("scientificName") != taxonomy.get("scientificName")
        or any(
            type(versions.get(k)) is not int or versions[k] <= 0 for k in ("entryVersion", "sequenceVersion")
        )
        or not isinstance(names.get("value"), str)
        or not names["value"]
    ):
        raise ValueError("explicit locus, unreviewed reference, taxonomy or field scope changed")
    return {
        "protein_accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"],
        "entry_version": versions["entryVersion"],
        "sequence_version": versions["sequenceVersion"],
        "systematic_locus": locus,
        "protein_name": names["value"],
        "protein_name_evidence_codes": sorted({e["evidenceCode"] for e in names.get("evidences", [])}),
        "protein_name_is_independent_experimental_validation": False,
        "reference_taxon_id": "NCBITaxon:284593",
        "reference_taxon_rank": "strain",
        "reference_organism_name": taxonomy["scientificName"],
        "species_taxon_id": "NCBITaxon:5478",
        "reference_role": "UNREVIEWED_REFERENCE_LOCUS_NOT_TESTED_ALLELE",
        "paper_symbol_is_uniprot_gene_name": False,
        "experimental_allele_assignment": None,
        "experimental_genome_assignment": None,
        "experimental_subject_taxon_assignment": False,
        "canonical_reference_established": False,
    }


def native(root, directory, key, url, statuses=(200,)):
    attempt_path, receipt_path, body_path = [
        directory / (key + suffix) for suffix in ("-attempt.json", "-receipt.json", "-response.bin")
    ]
    attempt, receipt = [json.loads(p.read_bytes()) for p in (attempt_path, receipt_path)]
    if (
        attempt.get("url") != url
        or receipt.get("url") != url
        or receipt.get("status") not in statuses
        or receipt.get("retry_performed") is not False
        or receipt.get("sha256") != reference.digest(body_path)
        or receipt.get("bytes") != body_path.stat().st_size
    ):
        raise ValueError("native request identity, attempt, status or payload changed")
    return {
        "body": reference.pin(root, body_path),
        "receipt": reference.pin(root, receipt_path),
        "attempt": reference.pin(root, attempt_path),
        "status": receipt["status"],
        "retrieved_at": receipt["retrieved_at"],
        "url": urlsplit(url)._replace(query="").geturl()
        if urlsplit(url).netloc == "storage.googleapis.com"
        else url,
    }


def build(root, directory):
    selection_path = directory / "selection.json"
    selection = json.loads(selection_path.read_bytes())
    for item in selection["pins"]:
        reference.check_pin(root, item)
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in ("prior", "prior_verification", "census", "protected", "discovery"):
        reference.check_pin(root, cohort[key])
    with reference.check_pin(root, cohort["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(checkpoint_path(root, r)) != r["record_sha256"] for r in census)
    ):
        raise ValueError("corpus membership or checkpoint bytes changed")
    record = load_record(reference.check_pin(root, cohort["record"]))
    if (
        record["identifier"] != "CHEBI:474180"
        or record["chemical_structure"]["standard_inchi_key"] != "JYIKNQVWKBUSNH-WVDDFWQHSA-N"
        or set(cohort["terms"]) != {v[0] for v in LOCI.values()}
        or not set(cohort["terms"]) <= {c.get("aro_id") for c in record["resistance_mechanisms"]}
    ):
        raise ValueError("compound or source-term identity changed")
    prior = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    taxonomy, taxonomy_source = cohort_audit.read_source(root, selection["taxonomy_source"])
    article = native(root, directory, "article", ARTICLE)
    tree = html.fromstring((directory / "article-response.bin").read_bytes())
    if tree.xpath("//meta[@name='citation_doi']/@content") != [DOI]:
        raise ValueError("primary article DOI changed")
    (heading,) = [
        h for h in tree.xpath("//h3") if h.text_content() == "Accession numbers (NCBI Entrez Gene ID number)"
    ]
    (paragraph,) = heading.xpath("following-sibling::p[1]")
    paper_ids = " ".join(paragraph.text_content().split())
    if not paper_ids.startswith("C. glabrata:"):
        raise ValueError("paper gene identifiers belong to another organism")
    table = json.loads((directory / "table1-reviewed.json").read_bytes())
    if (
        table["native_image_visually_inspected"] is not True
        or table["symbol_column_scope"] != "S. cerevisiae Homolog"
        or table["loci"] != {g.lower(): v[2] for g, v in LOCI.items()}
    ):
        raise ValueError("native table assessment changed")
    assets = {}
    for key, suffix in (("table1", "t001"), ("figure5", "g005")):
        (url,) = {
            urljoin(ARTICLE, a.get("href"))
            for a in tree.xpath("//a[@href]")
            if a.get("href").endswith("1002718." + suffix) and "download&size=large" in a.get("href")
        }
        redirect = native(root, directory, key, url, (302,))
        receipt = json.loads((directory / f"{key}-receipt.json").read_bytes())
        destination = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        parsed = urlsplit(destination)
        if (
            parsed.scheme != "https"
            or parsed.netloc != "storage.googleapis.com"
            or parsed.path != f"/plos-corpus-prod/{DOI}/1/ppat.1002718.{suffix}.PNG_L"
        ):
            raise ValueError("publisher image destination changed")
        assets[key] = {"publisher": redirect, "image": native(root, directory, key + "-storage", destination)}
    terms = {}
    for gene, (term, gene_id, locus, accession, version) in LOCI.items():
        if f"{gene} ({gene_id})" not in paper_ids:
            raise ValueError("source-reported gene identifier changed")
        queries = []
        for key, query in (
            (gene.lower(), f"xref:geneid-{gene_id} AND taxonomy_id:5478"),
            (gene.lower() + "-locus", f"gene:{locus} AND taxonomy_id:5478"),
        ):
            url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
                {"query": query, "format": "json", "size": "500", "fields": FIELDS}
            )
            body, source = fungal.local_response(root, directory, key, url)
            if not key.endswith("-locus") and body != {"results": []}:
                raise ValueError("paper GeneID query is no longer empty")
            queries.append(
                {
                    "query": query,
                    "source": source,
                    "result_count": len(body["results"]),
                    "zero_results_establish_absence": False,
                }
            )
        (entry,) = body["results"]
        mapped = project_locus(entry, taxonomy, locus)
        if (
            entry["primaryAccession"] != accession
            or mapped["entry_version"] != version
            or mapped["sequence_version"] != 1
            or entry.get("uniProtKBCrossReferences") != []
            or any("geneName" in b or b.get("synonyms") for b in entry["genes"])
        ):
            raise ValueError("selected reference version, accession or symbol context changed")
        old_queries = prior["terms"][term]["queries"]
        if len(old_queries) != 2 or any(q["result_count"] != 0 for q in old_queries):
            raise ValueError("prior empty exact-symbol query context changed")
        terms[term] = {
            "paper_gene_label": gene,
            "source_organism_name": "Nakaseomyces glabratus",
            "paper_organism_name": "Candida glabrata",
            "paper_reported_gene_id": "NCBIGene:" + gene_id,
            "gene_id_endpoint_requested": False,
            "gene_id_is_experimental_allele_or_genome": False,
            "reference": mapped,
            "taxonomy_source": taxonomy_source,
            "prior_exact_symbol_queries_reused": old_queries,
            "new_queries": queries,
            "primary_assessment": selection["primary_assessments"][gene],
            "exact_fungamr_row_crosswalk_verified": False,
            "new_resistance_assertion": False,
        }
    return {
        "date": "2026-10-13",
        "scope": "TWO_SOURCE_TERMS_NOT_WHOLE_RECORD_REVIEW",
        "inputs": {
            "selection": reference.pin(root, selection_path),
            **{k: cohort[k] for k in ("prior", "prior_verification", "census", "record")},
        },
        "primary": {
            "doi": DOI,
            "pmid": "22615574",
            "url": ARTICLE,
            "attribution": ("Singh-Babak et al., PLOS Pathogens (2012), e1002718; "
                            "publisher CC BY attribution."),
            "article": article,
            "assets": assets,
            "review_scope": "Relevant Results and Discussion; native Table 1 and Figure 5",
            "native_assets_visually_inspected": ["Table 1", "Figure 5"],
            "supplements_reviewed": False,
            "all_figures_reviewed": False,
            "numeric_mic_extracted_from_heatmap": False,
            "exact_chemical_form_resolved": False,
        },
        "terms": terms,
        "limitations": selection["limitations"],
        "review_findings": selection["review_findings"],
        "summary": {
            "corpus_records_hash_verified": len(census),
            "source_terms_investigated": 2,
            "new_unreviewed_reference_locus_contexts": 2,
            "new_uniprot_queries": 4,
            "empty_geneid_queries": 2,
            "cohort_reviewed_references": 9,
            "cohort_unreviewed_candidates": 3,
            "cohort_ambiguous_terms": 4,
            "cohort_terms_without_reference_candidates_after_followup": 3,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "exact_alleles_assigned": 0,
            "whole_record_reviews_completed": 0,
        },
        "constraints": {
            **cohort["constraints"],
            "numeric_ast_exported": False,
            "sequences_variants_protocols_exported": False,
            "reference_taxon_transferred_to_clinical_isolates": False,
        },
        "independent_scientific_review": False,
        "goal_status": "OPEN",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root, root / CACHE)
    data = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != data:
        raise ValueError("refusing to overwrite a different checkpoint")
    args.output.write_bytes(data)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

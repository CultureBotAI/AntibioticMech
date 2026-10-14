"""Replay reference identities and scoped yeast evidence without allele curation."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-mycophenolic")
OUTPUT = Path("research/2026-10-14-mycophenolic-context.json")
DOI = "10.1371/journal.pgen.1002627"
ARTICLE = "https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1002627"
ARTICLE_SHA = "081b93296d25c5822c3695bf1a74fe6de4baaa630f31c040bf817b82c67405e7"
FIGURES = {
    "2": "c39c2d63c3a24c40feb012e20ddc35094273ff96033591a9102637740d6752a3",
    "5": "8fe349031d9d170dde2cb31802009a54e40802dd9fd17369898177a24a6ba271",
}
REFERENCES = {
    "IMD1": ("P39567", "IMD1", "YAR073W", "S000000095", 176, 1),
    "IMD2": ("P38697", "IMD2", "YHR216W", "S000001259", 208, 1),
    "IMD3": ("P50095", "IMD3", "YLR432W", "S000004424", 219, 1),
    "IMD4": ("P50094", "IMD4", "YML056C", "S000004520", 212, 1),
    "RPB1": ("P04050", "RPO21", "YDL140C", "S000002299", 255, 2),
}
FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_sgd,lit_pubmed_id,sequence_version,version"
)
QUERIES = {
    "imd2-reference": ("gene_exact:IMD2 AND organism_id:559292 AND reviewed:true", ["IMD2"]),
    "comparative-references": (
        "(gene_exact:IMD1 OR gene_exact:IMD3 OR gene_exact:IMD4) AND organism_id:559292 AND reviewed:true",
        ["IMD1", "IMD3", "IMD4"],
    ),
    "rpb1-reference": ("gene_exact:RPB1 AND organism_id:559292 AND reviewed:true", ["RPB1"]),
}


def project_protein(entry, gene, taxonomy):
    if gene not in REFERENCES or {"sequence", "features", "comments"}.intersection(entry):
        raise ValueError("unplanned gene or biological payload")
    projected = reference.project_reference(entry, gene, 4932, taxonomy)
    species = [row for row in taxonomy["lineage"] if row["rank"] == "species"]
    if len(species) != 1 or species[0].get("scientificName") != "Saccharomyces cerevisiae":
        raise ValueError("reference species lineage name conflicts with the reviewed identity")
    accession, canonical, locus, sgd, version, sequence_version = REFERENCES[gene]
    blocks = entry.get("genes", [])
    links = [x for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "SGD"]
    if (
        entry["primaryAccession"] != accession
        or len(blocks) != 1
        or blocks[0].get("geneName", {}).get("value") != canonical
        or projected["ordered_locus_names"] != [locus]
        or entry["organism"]["taxonId"] != 559292
        or taxonomy["rank"] != "strain"
        or entry["organism"]["scientificName"] != taxonomy["scientificName"]
        or len(links) != 1
        or links[0].get("id") != sgd
        or projected["entry_version"] != version
        or projected["sequence_version"] != sequence_version
    ):
        raise ValueError("reference identity, version, locus or organism scope changed")
    projected.pop("bibliography")
    return {
        **projected,
        "source_gene": gene,
        "canonical_gene": canonical,
        "sgd_id": "SGD:" + sgd,
        "role": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_OR_GENOME",
        "resistance_asserted_from_reference": False,
    }


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = html.fromstring(payload)
    if tree.xpath('//meta[@name="citation_doi"]/@content') != [DOI]:
        raise ValueError("primary DOI changed")
    selectors = {
        "compound_and_subject_limits": "For studies with mycophenolic acid (MPA, Sigma-Aldrich)",
        "probe_specificity": "we do not specify that observed changes in our Northern blotting",
        "expression_comparison": "We observed a constitutive upregulation of IMD transcripts",
        "interpretation_limit": "MPA sensitivity of any transcription factor mutant should not be used",
        "figure2_caption": "Scoring of phenotypic strength is based on visual inspection of (A)",
        "figure5_caption": "Northern blotting for different Pol II mutants in the presence or absence",
    }
    locations = {}
    for name, marker in selectors.items():
        matches = [p for p in tree.xpath("//p") if marker in " ".join(p.text_content().split())]
        if len(matches) != 1:
            raise ValueError("reviewed primary location is missing or ambiguous")
        text = " ".join(matches[0].text_content().split())
        locations[name] = {
            "xpath": tree.getroottree().getpath(matches[0]),
            "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
    return {
        "doi": DOI,
        "title": tree.xpath('//meta[@name="citation_title"]/@content')[0],
        "locations": locations,
        "compound_scope": (
            "Named mycophenolic acid, not its sodium salt, mofetil prodrug or combination exposure."
        ),
        "independent_chemical_reidentification": False,
        "organism_scope": (
            "Saccharomyces cerevisiae laboratory comparisons; "
            "no clinical category or species-wide resistance."
        ),
        "gene_context": [
            {
                "gene": "RPB1",
                "evidence": (
                    "Mixed mutant growth phenotypes in Figure 2, "
                    "including source-labeled resistance and sensitivity."
                ),
                "limit": (
                    "Not a direction of effect shared by all RPB1 alleles; "
                    "generic growth defects require matched controls."
                ),
            },
            {
                "gene": "IMD2",
                "evidence": (
                    "Expression and start-site comparisons in Figure 5 relate transcription to drug response."
                ),
                "limit": (
                    "Figure 5A Northern signal is not uniquely IMD2 "
                    "because of possible paralog cross-hybridization."
                ),
            },
        ],
        "interpretation_limit": (
            "Drug sensitivity is not sufficient evidence of a generic transcription-elongation defect."
        ),
        "measurement_scope": "Qualitative plate growth and transcription assays, not MIC or disk diffusion.",
        "supplement_subject_crosswalk": "PENDING_TABLES_S1_S2_AND_TEXT_S1_REVIEW",
        "source_license_notice": "Creative Commons Attribution; Kaplan et al., 2012, PLOS Genetics.",
        "experimental_allele_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "experimental_genome_assignment": None,
    }


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    cohort = read(directory / "cohort.json")
    review = read(directory / "reviewed.json")
    for key in ("census", "discovery", "protected"):
        reference.check_pin(root, cohort[key])
    # Replay the exact historical record, not a later live corpus version.
    snapshot = reference.check_pin(root, review["baseline_record"])
    if reference.digest(snapshot) != cohort["record"]["sha256"]:
        raise ValueError("historical record snapshot differs from the reviewed original")
    record = load_record(snapshot)
    with (root / cohort["census"]["path"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    matches = [r for r in rows if r["identifier"] == "CHEBI:168396"]
    if (
        len(rows) != 2939
        or len(matches) != 1
        or matches[0]["record_sha256"] != cohort["record"]["sha256"]
        or matches[0]["path"] != cohort["record"]["path"]
        or record["identifier"] != "CHEBI:168396"
        or record["chemical_structure"]["standard_inchi_key"] != "HPNSFSBZBAHARI-RUDMXATFSA-N"
        or record.get("resistance_mechanisms")
    ):
        raise ValueError("compound or historical census identity changed")
    taxonomy = read(reference.check_pin(root, review["taxonomy"]["body"]))
    tax_receipt = read(reference.check_pin(root, review["taxonomy"]["receipt"]))
    if (
        tax_receipt["url"] != "https://rest.uniprot.org/taxonomy/559292"
        or tax_receipt["status"] != 200
        or tax_receipt["sha256"] != review["taxonomy"]["body"]["sha256"]
    ):
        raise ValueError("reused taxonomy response is not the pinned successful reference")
    reference.check_pin(root, review["taxonomy_reused_from"])
    plans, sources = {}, {}
    for name in (
        "native",
        "primary",
        "comparative",
        "primary-2003",
        "primary-2012",
        "assets",
        "figure2-storage",
        "figure5-storage",
    ):
        path = directory / f"{name}-plan.json"
        plans[name] = reference.pin(root, path)
        plan = read(path)
        for value in plan.values():
            if isinstance(value, dict) and set(value) == {"path", "sha256"}:
                reference.check_pin(root, value)
        for key, item in plan["requests"].items():
            if key in sources:
                raise ValueError("duplicate planned request")
            statuses = (
                (403,)
                if key in ("primary-2002", "primary-2003")
                else (302,)
                if key in ("figure2", "figure5")
                else (200,)
            )
            sources[key] = native_context.native(root, directory, key, item["url"], statuses)
    proteins = {}
    for key, (query, genes) in QUERIES.items():
        parameters = {"query": [query], "fields": [FIELDS], "format": ["json"], "size": ["10"]}
        body, source = reference.read_response(root, directory, key, "/uniprotkb/search", parameters)
        if source["release"] != "2026_03":
            raise ValueError("reviewed reference release changed")
        by_id = {e["primaryAccession"]: e for e in body["results"]}
        if len(by_id) != len(body["results"]) or set(by_id) != {REFERENCES[g][0] for g in genes}:
            raise ValueError("reference cohort is incomplete or ambiguous")
        for gene in genes:
            proteins[gene] = {
                **project_protein(by_id[REFERENCES[gene][0]], gene, taxonomy),
                "source_request": key,
                "release": source["release"],
            }
    metadata = read(directory / "metadata-2003-response.bin")
    (citation,) = metadata["resultList"]["result"]
    if (
        metadata["hitCount"] != 1
        or citation["id"] != "12746440"
        or citation["doi"].lower() != "10.1074/jbc.m303736200"
    ):
        raise ValueError("distinct 2003 citation identity changed")
    article = sources["primary-2012"]
    if article["url"] != ARTICLE:
        raise ValueError("reviewed primary URL changed")
    primary = primary_context((directory / "primary-2012-response.bin").read_bytes())
    for number, expected in FIGURES.items():
        item = review["figures"][number]
        source = sources[f"figure{number}-storage"]
        receipt = read(directory / f"figure{number}-receipt.json")
        destination = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        url = urlsplit(destination)
        if (
            item.get("visually_inspected") is not True
            or item["body"] != source["body"]
            or source["body"]["sha256"] != expected
            or url.scheme != "https"
            or url.netloc != "storage.googleapis.com"
            or url.path != f"/plos-corpus-prod/{DOI}/1/pgen.1002627.g{int(number):03}.PNG_L"
            or read(directory / f"figure{number}-storage-attempt.json")["url"] != destination
        ):
            raise ValueError("visually reviewed figure or publisher redirect changed")
    if review["record_curated"] is not False or review["curated_resistance_assertions"] != 0:
        raise ValueError("research checkpoint cannot authorize curation")
    return {
        "scope": "REFERENCE_IDENTITIES_AND_SCOPED_PRIMARY_CONTEXT_NOT_ALLELE_CURATION",
        "record_before": cohort["record"],
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "assessment": reference.pin(root, directory / "reviewed.json"),
            "plans": plans,
            "census": cohort["census"],
            "historical_record_snapshot": review["baseline_record"],
        },
        "taxonomy": review["taxonomy"],
        "sources": sources,
        "references": proteins,
        "primary": {**primary, "visually_reviewed_figures": review["figures"]},
        "citation_dispositions": {
            "PMID:12016207": "PUBLISHER_403_PRIMARY_REVIEW_HELD_NO_RETRY",
            "PMID:12746440": "METADATA_INSPECTED_EUROPE_PMC_PDF_403_PRIMARY_REVIEW_HELD_NO_RETRY",
            "PMID:16278936": "DISCOVERY_AND_UNIPROT_BIBLIOGRAPHY_ONLY_PRIMARY_REVIEW_PENDING",
            "PMID:18823333": "DISCOVERY_ONLY_PRIMARY_REVIEW_PENDING",
            "DOI:" + DOI: "SELECTED_RESULTS_AND_FIGURES_2_5_REVIEWED_SUBJECT_CROSSWALK_PENDING",
        },
        "limits": {
            "whole_record_primary_review": "OPEN",
            "source_adoption": False,
            "sequences_exported": False,
            "variants_exported": False,
            "numeric_ast_exported": False,
            "clinical_category_inferred": False,
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reference_strain_is_experimental_subject": False,
            "independent_scientific_signoff": False,
        },
        "summary": {
            "corpus_records_in_scope": 2939,
            "records_in_this_checkpoint": 1,
            "versioned_reference_proteins": 5,
            "primary_access_holds": 2,
            "curated_resistance_assertions": 0,
            "whole_record_primary_signoffs": 0,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path.cwd()
    output = build(root, root / args.cache)
    payload = (json.dumps(output, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to replace a different historical checkpoint")
    args.output.write_bytes(payload)
    print(json.dumps(output["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Keep syringomycin E evidence separate from related compounds and reference IDs."""

import argparse
import hashlib
import json
from pathlib import Path

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import html

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-13-syringomycin")
OUTPUT = Path("research/2026-10-13-syringomycin-context.json")
RECORD = Path("data/antibiotics/antifungal/syringomycin-e.yaml")
FIXTURE = Path("tests/fixtures/syringomycin-e-before-2026-10-13.yaml")
RECORD_SHA = "1731a6718d89e95494d9d8b1c9c621ef538e9a4fd1993f6b952f11d7d0cd96bc"
ARTICLE_SHA = "f60b103cb1198db12c3ef38e9bca9f5c2fe54339a8f9e4fbaabe1ce79bda090d"
FIGURE_SHA = "1039cac4e550d28a4bdb2936b65da6487f70ea2cbba342238ce0553c4b76477e"
BACKGROUND = {
    "SYR2": "W303C",
    "IPT1": "W303C",
    "ELO2": "W303C",
    "ELO3": "W303C",
    "FAH1": "BY4741",
    "ERG3": "8A-1B",
}
REFERENCES = {
    "SYR2": ("P38992", "SUR2", "YDR297W", "S000002705"),
    "IPT1": ("P38954", "IPT1", "YDR072C", "S000002479"),
    "FAH1": ("Q03529", "SCS7", "YMR272C", "S000004885"),
    "SKN1": ("P33336", "SKN1", "YGR143W", "S000003375"),
}


def checkpoint_record(root):
    current = root / RECORD
    if reference.digest(current) == RECORD_SHA:
        return current
    fixture = root / FIXTURE
    if reference.digest(fixture) != RECORD_SHA:
        raise ValueError("historical source record changed")
    return fixture


def project_protein(entry, source_gene, taxonomy):
    if source_gene not in REFERENCES or {"features", "comments"}.intersection(entry):
        raise ValueError("unplanned gene or biological payload")
    result = reference.project_reference(entry, source_gene, 4932, taxonomy)
    accession, canonical, locus, sgd = REFERENCES[source_gene]
    blocks = entry.get("genes", [])
    links = [x for x in entry.get("uniProtKBCrossReferences", []) if x.get("database") == "SGD"]
    if (
        entry["primaryAccession"] != accession
        or len(blocks) != 1
        or blocks[0].get("geneName", {}).get("value") != canonical
        or result["ordered_locus_names"] != [locus]
        or entry["organism"]["taxonId"] != 559292
        or taxonomy["rank"] != "strain"
        or entry["organism"]["scientificName"] != taxonomy["scientificName"]
        or len(links) != 1
        or links[0].get("id") != sgd
    ):
        raise ValueError("reference alias, locus, accession, SGD or strain scope changed")
    result.pop("bibliography")
    return {
        **result,
        "source_gene": source_gene,
        "canonical_gene": canonical,
        "sgd_id": "SGD:" + sgd,
        "role": "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE_OR_GENOME",
    }


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = html.fromstring(payload)
    if tree.xpath('//meta[@name="citation_doi"]/@content') != ["10.3389/fmicb.2011.00216"]:
        raise ValueError("primary DOI changed")
    (methods,) = tree.xpath('//h3[normalize-space(.)="Yeast strains"]/following-sibling::p[1]')
    (identity,) = tree.xpath(
        '//h3[normalize-space(.)="Purification of SRE, SP22A, and SP25A"]/following-sibling::p[1]'
    )
    (results,) = tree.xpath(
        '//h3[normalize-space(.)="Susceptibility of lipid biosynthetic mutants"]/following-sibling::p[1]'
    )
    (notice,) = tree.xpath('//p[normalize-space(text())="Copyright"]')
    locations = {}
    for key, element in (
        ("subjects", methods),
        ("named_congener", identity),
        ("results", results),
        ("table", tree.get_element_by_id("T1")),
        ("notice", notice.getparent()),
    ):
        text = " ".join(element.text_content().split())
        locations[key] = {
            "xpath": tree.getroottree().getpath(element),
            "normalized_text_sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
    (table,) = tree.xpath('//*[@id="T1"]//table')
    columns = [" ".join(x.text_content().split()) for x in table.xpath("./thead/tr[2]/th")]
    if columns != ["", "SRE", "SP22A", "SP25A"]:
        raise ValueError("compound-specific table columns changed")
    rows = []
    for number, tr in enumerate(table.xpath("./tbody/tr"), 1):
        cells = tr.xpath("./td")
        labels = ["".join(x.itertext()).upper() for x in cells[0].xpath("./i")]
        if len(labels) != 1 or labels[0] not in {*BACKGROUND, "SKN1"}:
            continue
        if len(cells) != 4:
            raise ValueError("mutant table row lost its compound columns")
        gene = labels[0]
        native_value = " ".join(cells[1].text_content().split())
        rows.append(
            {
                "source_gene": gene,
                "source_table_row": number,
                "source_cell_xpath": tree.getroottree().getpath(cells[1]),
                "source_cell_text_sha256": hashlib.sha256(native_value.encode()).hexdigest(),
                "assay_type": "MIC",
                "source_unit": "micromolar",
                "numeric_result_exported": False,
                "replicate_values_differ": bool(cells[1].xpath('.//a[@href="#tfn2"]')),
                "parental_background": BACKGROUND.get(gene),
                "figure_1B_present": gene in BACKGROUND,
                "methods_resistance_label_present": gene in BACKGROUND,
                "curation_supported": gene in BACKGROUND,
                "experimental_strain_taxon": None,
                "experimental_allele": None,
                "experimental_genome": None,
            }
        )
    if [r["source_gene"] for r in rows] != ["SYR2", "ELO3", "IPT1", "FAH1", "ELO2", "SKN1", "ERG3"]:
        raise ValueError("source cohort membership or order changed")
    return {
        "reference": "PMID:22046175",
        "doi": "10.3389/fmicb.2011.00216",
        "locations": locations,
        "source_rows": rows,
        "background_basis": "Methods and visually inspected Figure 1B, not table row ordering.",
        "compound_scope": "Named purified syringomycin E; not syringopeptins SP22A or SP25A.",
        "independent_chemical_reidentification": False,
        "source_reuse_notice": (
            "Source-specific open-access notice with attribution and other Frontiers conditions."
        ),
        "blanket_license_or_source_adoption_asserted": False,
        "SKN1_hold": "Table row only: not described in the strain paragraph or shown in Figure 1B.",
        "measurement_policy": {
            "preferred_mic_unit": "mg/L",
            "conversion_performed": False,
            "numeric_ast_exported": False,
            "clinical_category_inferred": False,
            "replicate_difference_is_confidence_interval": False,
        },
    }


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    plans = {name: read(directory / (name + "-plan.json")) for name in ("native", "comparison", "followup")}
    cohort = read(reference.check_pin(root, plans["native"]["cohort"]))
    for key in ("prior_verification", "census", "protected", "discovery"):
        reference.check_pin(root, cohort[key])
    sources = {}
    for plan in plans.values():
        for item in plan.values():
            if isinstance(item, dict) and set(item) == {"path", "sha256"}:
                reference.check_pin(root, item)
        for key, row in plan["requests"].items():
            sources[key] = native_context.native(
                root, directory, key, row["url"], statuses=(500,) if key == "primary-2000" else (200,)
            )
    for filename, source, key in (
        ("primary-canary.json", "primary-2011", "source"),
        ("reference-canary.json", "syr2-reference", "body"),
    ):
        canary = read(directory / filename)
        if (
            canary.get("manually_inspected") is not True
            or canary[key] != sources[source]["body"]
            or canary["receipt"] != sources[source]["receipt"]
        ):
            raise ValueError("source or reference canary changed")
    if sources["figure1"]["body"]["sha256"] != FIGURE_SHA:
        raise ValueError("visually inspected Figure 1 changed")
    primary = primary_context(reference.check_pin(root, sources["primary-2011"]["body"]).read_bytes())
    tax_pin = plans["followup"]["cached_taxonomy_body"]
    tax_path = reference.check_pin(root, tax_pin)
    receipt = read(reference.check_pin(root, plans["followup"]["cached_taxonomy_receipt"]))
    if (
        receipt["url"] != "https://rest.uniprot.org/taxonomy/559292"
        or receipt["status"] != 200
        or receipt["sha256"] != reference.digest(tax_path)
    ):
        raise ValueError("cached taxonomy provenance changed")
    taxonomy = read(tax_path)
    proteins = {}
    for key, genes in (("syr2-reference", ["SYR2"]), ("other-references", ["IPT1", "FAH1", "SKN1"])):
        receipt = read(reference.check_pin(root, sources[key]["receipt"]))
        headers = {k.lower(): v for k, v in receipt["headers"].items()}
        entries = read(reference.check_pin(root, sources[key]["body"]))["results"]
        if (
            headers.get("x-uniprot-release") != "2026_03"
            or headers.get("link")
            or headers.get("x-total-results") != str(len(genes))
            or len(entries) != len(genes)
        ):
            raise ValueError("reference release, count or completeness changed")
        used = set()
        for gene in genes:
            matches = [e for e in entries if e.get("primaryAccession") == REFERENCES[gene][0]]
            if len(matches) != 1:
                raise ValueError("reference result absent or ambiguous")
            proteins[gene] = project_protein(matches[0], gene, taxonomy)
            used.add(matches[0]["primaryAccession"])
        if len(used) != len(entries):
            raise ValueError("unaccounted reference entries")
    record_path = checkpoint_record(root)
    record = load_record(record_path)
    if (
        record["identifier"] != "CHEBI:77762"
        or record["chemical_structure"]["standard_inchi_key"] != "ZQVJBRJGDVZANE-MTGUCJNSSA-N"
        or record.get("resistance_mechanisms")
        or record.get("activity_spectrum")
    ):
        raise ValueError("historical complete record identity or evidence changed")
    return {
        "scope": "QUALITATIVE_NAMED_CONGENER_EVIDENCE_WITH_REFERENCE_ONLY_GROUNDING",
        "record_before": cohort["record"],
        "primary": primary,
        "references": proteins,
        "sources": sources,
        "taxonomy": {"body": tax_pin, "receipt": plans["followup"]["cached_taxonomy_receipt"]},
        "inputs": {
            "cohort": reference.pin(root, directory / "cohort.json"),
            "plans": [reference.pin(root, directory / (n + "-plan.json")) for n in plans],
        },
        "candidate_accounting": [
            {
                **p,
                "review_status": (
                    "SELECTED_PRIMARY_RESULTS_TABLE1_FIGURE1_REVIEWED"
                    if key == "22046175"
                    else "HTTP_500_NO_PRIMARY_TEXT_NO_RETRY"
                    if key == "10770748"
                    else "DISCOVERY_ONLY"
                ),
            }
            for key, p in sorted(cohort["candidates"].items())
        ],
        "summary": {
            "candidate_papers": 12,
            "selected_primary_papers_reviewed": 1,
            "source_mutant_rows": 7,
            "qualified_curation_candidates": 6,
            "reference_genes_grounded": 4,
            "skn1_reference_does_not_authorize_curation": True,
            "reference_genes_deferred": ["ERG3", "ELO2", "ELO3"],
            "whole_record_reviews_completed": 0,
        },
        "limits": {
            "source_2000_retrieval": "HTTP 500; no alternate retrieval attempted.",
            "experimental_ids": "No tested protein, allele, strain-TaxID or genome assignment.",
            "source_evidence": (
                "Comparative laboratory findings, not clinical resistance or direct protein targets."
            ),
            "issue_1040": "DEFERRED",
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "github_mutations": 0,
            "source_adoptions": 0,
            "numeric_ast_exported": False,
            "sequences_variants_protocols_exported": False,
        },
    }


def claims(context):
    result = []
    for gene, background in BACKGROUND.items():
        note = (
            f"Qualified laboratory association in a {background}-derived yeast model; "
            "the parent background is not an exact experimental isolate identifier. "
            "Lipid-biosynthesis context does not identify a direct protein target or clinical resistance. "
            "No experimental allele, protein, strain-TaxID, genome or numerical AST is assigned."
        )
        evidence = [
            {
                "reference": "PMID:22046175",
                "notes": "Methods, Yeast strains; Table 1 SRE column; Figure 1B SRE comparison; "
                "DOI:10.3389/fmicb.2011.00216. Named purified syringomycin E evidence, "
                "not SP22A/SP25A transfer or independent reidentification of the preparation.",
            }
        ]
        if gene in context["references"]:
            ref = context["references"][gene]
            evidence.append(
                {
                    "reference": ref["protein_accession"],
                    "notes": f"Reference identity only: {gene} maps to {ref['canonical_gene']}, "
                    f"{', '.join(ref['ordered_locus_names'])}; UniProtKB 2026_03 entry "
                    f"{ref['entry_version']}, sequence {ref['sequence_version']}. "
                    "S288c NCBITaxon:559292 is reference context, not the tested derivative.",
                }
            )
        else:
            note += " A versioned UniProt crosswalk remains pending."
        result.append(
            {
                "mechanism_type": "UNKNOWN",
                "label": f"{gene}-associated laboratory syringomycin E resistance",
                "gene_families": [gene],
                "taxon_id": "NCBITaxon:4932",
                "taxon_label": "Saccharomyces cerevisiae",
                "phenotype_label": "Source-reported relative syringomycin E resistance",
                "assay": "Comparative laboratory growth and susceptibility assays",
                "note": note,
                "evidence": evidence,
            }
        )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    result = build(root, root / CACHE)
    (root / OUTPUT).write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))

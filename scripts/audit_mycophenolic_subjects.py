"""Replay qualified RPB1 evidence while keeping background IDs reference-only."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit
from zipfile import ZipFile

import audit_mycophenolic_context as prior_audit
from lxml import etree, html

reference = prior_audit.reference
native = prior_audit.native_context.native
CACHE = prior_audit.CACHE / "subject-followup"
OUTPUT = Path("research/2026-10-14-mycophenolic-subjects.json")
RECORD = Path("data/antibiotics/antiviral/mycophenolic-acid.yaml")
FIXTURE = Path("tests/fixtures/mycophenolic-acid-before-2026-10-14.yaml")
PRIOR_SHA = "5b413ea2ef058d23ace551165a802796de9a7bcb40e8abb82f1bea49b9cf7871"
REVIEWED_CONTEXT_SHA = "8efa2c17bf8b9c3f0337770bafda1c0e4c1060b45ba9d812c1083a3099d42be9"
DOCS = {
    "table-s1": ("s009", "54ead5eb4a00a4c0c6c006f3657d041c9cd7d9be472d57b13963b57c7bdc26c7", 4),
    "table-s2": ("s010", "4a9ab5b8b692d0d0d141dfc047e6725dfc7be110b408e09838c9f77a6125e8da", 1),
    "text-s1": ("s011", "ee70f6f3d201c032b9ed2ffa34fd9adf22c018c9885ce596dc419d26c0a3b6e8", 5),
}
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def canonical(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()


def document_context(path, key):
    if key not in DOCS or reference.digest(path) != DOCS[key][1]:
        raise ValueError("reviewed supplement identity changed")
    with ZipFile(path) as archive:
        tree = etree.fromstring(
            archive.read("word/document.xml"), etree.XMLParser(resolve_entities=False, no_network=True)
        )
    tables = tree.findall(".//w:tbl", NS)
    result = {"table_count": len(tables), "native_docx_sha256": reference.digest(path)}
    if key.startswith("table"):
        if len(tables) != 1:
            raise ValueError("native table count changed")
        rows = tables[0].findall("./w:tr", NS)
        expected_rows, expected_columns = (116, 5) if key == "table-s1" else (4, 3)
        if len(rows) != expected_rows or any(len(r.findall("./w:tc", NS)) != expected_columns for r in rows):
            raise ValueError("native table dimensions changed")
        result.update(rows_including_header=len(rows), columns=expected_columns)
        if key == "table-s1":
            result["scope"] = "Comparison metadata and viability, not a table of drug-resistant isolates."
            result["viability_interpreted_as_resistance"] = False
        else:
            labels = [" ".join(r.find("./w:tc", NS).xpath(".//w:t/text()", namespaces=NS)) for r in rows[1:]]
            if labels != ["CKY274", "CKY283", "CKY944"]:
                raise ValueError("source background registry changed")
            result["source_background_labels"] = labels
            result["labels_are_variant_specific_subject_identifiers"] = False
    else:
        if tables:
            raise ValueError("unexpected table in supplemental text")
        locations = {}
        for name, start in (
            ("yeast_background", "All yeast strains"),
            ("background_comparison", "During the course of our experiments"),
        ):
            matches = [
                (i, " ".join(p.xpath(".//w:t/text()", namespaces=NS)))
                for i, p in enumerate(tree.xpath("//w:body/w:p", namespaces=NS), 1)
            ]
            ((index, text),) = [(i, s) for i, s in matches if s.startswith(start)]
            locations[name] = {
                "body_paragraph": index,
                "text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            }
        result.update(
            locations=locations,
            parental_scope="S288C-derived laboratory strains",
            genetic_comparison_background="CKY283",
            experimental_strain_taxon_id=None,
            experimental_genome=None,
        )
    return result


def build(root, directory):
    def read(path):
        return json.loads(path.read_bytes())

    cohort = read(directory / "cohort.json")
    prior_path = reference.check_pin(root, cohort["prior"])
    if reference.digest(prior_path) != PRIOR_SHA:
        raise ValueError("reviewed preceding checkpoint changed")
    prior = read(prior_path)
    if prior != prior_audit.build(root, root / prior_audit.CACHE):
        raise ValueError("preceding native evidence does not replay exactly")
    for key in ("previous_verification", "article", "protected"):
        reference.check_pin(root, cohort[key])
    assessment = read(directory / "reviewed-supplements.json")
    if (
        assessment["all_ten_rendered_pages_visually_inspected"] is not True
        or assessment["native_docx_tables_structurally_inspected"] is not True
        or assessment["qualified_rpb1_curation_supported"] is not True
        or any(
            assessment[k] is not False
            for k in (
                "background_ids_are_tested_derivative_ids",
                "table_s1_viability_is_drug_resistance",
                "biochemical_and_growth_assay_contexts_are_interchangeable",
                "imd2_expression_is_independent_resistance_claim",
                "exact_variants_constructs_protocols_or_numeric_ast_exported",
            )
        )
    ):
        raise ValueError("reviewed source-scope assessment changed")
    plan = read(directory / "native-plan.json")
    reference.check_pin(root, plan["cohort"])
    if set(plan["requests"]) != set(DOCS) or plan["canary"] != "table-s1":
        raise ValueError("native supplement cohort changed")
    tree = html.fromstring(reference.check_pin(root, cohort["article"]).read_bytes())
    documents, sources = {}, {}
    for key, (suffix, digest, page_count) in DOCS.items():
        url = plan["requests"][key]["url"]
        expected = "https://journals.plos.org/plosgenetics/article/file?type=supplementary&id="
        expected += prior_audit.DOI + "." + suffix
        if url != expected or not tree.xpath(
            "//a[@href=$href]", href=url.removeprefix("https://journals.plos.org/plosgenetics/")
        ):
            raise ValueError("supplement URL is not the native article link")
        publisher = native(root, directory, key, url, (302,))
        receipt = read(directory / f"{key}-receipt.json")
        destination = {k.lower(): v for k, v in receipt["headers"].items()}["location"]
        parsed = urlsplit(destination)
        if (
            parsed.scheme != "https"
            or parsed.netloc != "storage.googleapis.com"
            or parsed.path != f"/plos-corpus-prod/{prior_audit.DOI}/1/pgen.1002627.{suffix}.docx"
        ):
            raise ValueError("publisher document destination changed")
        response = native(root, directory, key + "-storage", destination)
        if response["body"] != assessment["documents"][key] or response["body"]["sha256"] != digest:
            raise ValueError("reviewed document is not the retrieved document")
        documents[key] = document_context(reference.check_pin(root, response["body"]), key)
        pages = assessment["page_images"][key]
        if len(pages) != page_count or len({p["path"] for p in pages}) != page_count:
            raise ValueError("rendered page accounting changed")
        for item in [assessment["pdfs"][key], *pages]:
            reference.check_pin(root, item)
        sources[key] = {"publisher": publisher, "document": response, "rendered_pages_reviewed": page_count}
    return {
        "scope": "QUALIFIED_RPB1_LABORATORY_ASSOCIATION_NOT_EXACT_ALLELE_OR_CLINICAL_RESISTANCE",
        "record_before": prior["record_before"],
        "inputs": {
            "prior": cohort["prior"],
            "cohort": reference.pin(root, directory / "cohort.json"),
            "plan": reference.pin(root, directory / "native-plan.json"),
            "assessment": reference.pin(root, directory / "reviewed-supplements.json"),
        },
        "source_documents": sources,
        "supplement_context": documents,
        "reference": prior["references"]["RPB1"],
        "taxonomy": prior["taxonomy"],
        "primary_doi": prior_audit.DOI,
        "evidence_scope": {
            "resistance_basis": (
                "Source-labeled resistant comparisons in Figure 2D with plate-growth controls in Figure 2A."
            ),
            "discordant_context": "Other RPB1 comparisons are sensitive or have generic growth defects.",
            "subject_scope": (
                "CKY283-derived laboratory comparisons; no exact descendant identifier assigned."
            ),
            "mechanistic_limit": (
                "IMD transcription context does not establish Rpb1 as the direct drug target."
            ),
            "expression_limit": "Figure 5A is not a uniquely IMD2-specific readout.",
            "reference_limit": (
                "S288c reference protein and taxonomy are not experimental allele or strain IDs."
            ),
            "biochemical_limit": (
                "Growth and purified-enzyme comparisons are not assumed to use identical backgrounds."
            ),
        },
        "curation": {
            "supported_gene_associations": ["RPB1"],
            "mechanism_type": "UNKNOWN",
            "species_taxon_id": "NCBITaxon:4932",
            "strain_taxon_id": None,
            "experimental_protein_accession": None,
            "experimental_gene_id": None,
            "experimental_genome": None,
            "exact_variant_exported": False,
            "numeric_ast_exported": False,
            "clinical_category_inferred": False,
            "whole_record_review_complete": False,
        },
        "constraints": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "source_adoption": False},
    }


def claims(context):
    if hashlib.sha256(canonical(context)).hexdigest() != REVIEWED_CONTEXT_SHA:
        raise ValueError("complete reviewed primary and subject context is required")
    return [
        {
            "mechanism_type": "UNKNOWN",
            "label": "RPB1-associated laboratory mycophenolic-acid resistance (qualified association)",
            "gene_families": ["RPB1"],
            "taxon_id": "NCBITaxon:4932",
            "taxon_label": "Saccharomyces cerevisiae",
            "phenotype_label": "Source-defined laboratory resistance to mycophenolic acid",
            "assay": "Comparative plate-growth assay",
            "note": (
                "Selected RPB1 laboratory comparisons are labeled resistant in Figure 2D; "
                "Figure 2A provides matched growth controls. Other RPB1 comparisons are sensitive "
                "or have baseline growth defects. This is not a shared effect of all RPB1 alleles, "
                "a clinical resistance category, an MIC, or a species-wide phenotype. Text S1 "
                "identifies S288C-derived backgrounds and CKY283 as the genetic-comparison parent, "
                "not as an identifier for every tested derivative. RPB1 is the paper's name for RPO21. "
                "UniProtKB:P04050 and NCBITaxon:559292 identify S288c reference context only; "
                "no exact experimental protein, allele, strain TaxID or genome is assigned. "
                "The accompanying IMD transcription results do not make Rpb1 a direct drug target; "
                "the Figure 5A probe is not uniquely IMD2-specific."
            ),
            "evidence": [
                {
                    "reference": "DOI:" + prior_audit.DOI,
                    "notes": (
                        "Kaplan et al. 2012: Figure 2A/D, Results and Discussion, Tables S1/S2 and Text S1. "
                        "Native figures and rendered supplements inspected. Viability in Table S1 is not an "
                        "independent drug-resistance endpoint; "
                        "growth and purified-enzyme contexts remain distinct."
                    ),
                },
                {
                    "reference": "UniProtKB:P04050",
                    "notes": "Reference-only RPO21/RPB1, YDL140C, SGD:S000002299; UniProt release 2026_03, "
                    "entry version 255, sequence version 2, retrieved 2026-10-14. "
                    "S288c reference taxon 559292 belongs to species 4932 in cached UniProt Taxonomy. "
                    "These are not tested derivative or mutant-specific accessions.",
                },
            ],
        }
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=CACHE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    root = Path.cwd()
    output = build(root, root / args.cache)
    payload = canonical(output)
    if args.output.exists() and args.output.read_bytes() != payload:
        raise ValueError("refusing to replace a different historical checkpoint")
    args.output.write_bytes(payload)
    print(json.dumps({"sha256": hashlib.sha256(payload).hexdigest(), "gene_associations": 1}))


if __name__ == "__main__":
    main()

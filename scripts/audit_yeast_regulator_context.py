"""Replay qualified regulator evidence and conflicting archive metadata offline."""

import argparse
import csv
import io
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit, urlunsplit
from xml.etree import ElementTree

import audit_hsp90_context as primary
import audit_resistance_grounding as cached
import audit_topoisomerase_references as reference

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-yeast-regulators")
DEFAULT_OUTPUT = Path("research/2026-10-13-yeast-regulator-context.json")
FIELDS = ("accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
          "xref_sgd,lit_pubmed_id,sequence_version,version")
ENA_FIELDS = ("run_accession,study_accession,secondary_study_accession,sample_accession,"
              "secondary_sample_accession,experiment_accession,submission_accession,sample_alias,"
              "sample_title,scientific_name,tax_id,study_title,study_alias,first_public,last_updated")
TARGETS = {**primary.TARGETS, "CHEBI:4031": "PMATZTZNYRCHOR-CGLBZJNRSA-N",
           "antibioticmech:aro-2e3b34cc67": "QJJXYPPXXYFBGM-LFZNUXCKSA-N"}
SUBJECTS = {"Sc-F-1": ("ScLC1367", "MOT3"), "Sc-G-13": ("ScLC1540", "PDR1")}
EXPERIMENTS = {"SRX220258": "ScLC1367", "SRX220314": "ScLC1367_long"}
STUDY, SECONDARY_STUDY, SUBMISSION = "PRJNA186947", "SRP018095", "SRA065341"
SAMPLE, SECONDARY_SAMPLE = "SAMN01893852", "SRS387829"
FIGURE = ("https://journals.plos.org/plosgenetics/article/figure/image?download&size=large"
          "&id=10.1371/journal.pgen.1003390.g006")


def bind_canary(root, directory, canary, key):
    for field, suffix in (("response", "response.bin"), ("receipt", "receipt.json")):
        if canary.get(field) != reference.pin(root, directory / f"{key}-{suffix}"):
            raise ValueError("canary is not bound to its intended request")
    if canary.get("manually_reviewed") is not True:
        raise ValueError("canary manual review missing")


def read_ena(root, directory, key, endpoint, parameters=None):
    path, receipt_path = directory / f"{key}-response.bin", directory / f"{key}-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    url = urlsplit(receipt["url"])
    body = path.read_bytes()
    if (url.scheme != "https" or url.netloc != "www.ebi.ac.uk" or url.path != endpoint or url.fragment
            or parse_qs(url.query, keep_blank_values=True) != (parameters or {})
            or receipt["status"] != 200 or receipt["retry_performed"] is not False
            or receipt["sha256"] != reference.digest(path) or receipt["bytes"] != len(body)
            or len(body) > 2_000_000):
        raise ValueError("ENA request identity or payload changed")
    return body, {"response": reference.pin(root, path), "receipt": reference.pin(root, receipt_path),
                  "url": receipt["url"], "retrieved_at": receipt["retrieved_at"], "status": 200}


def validate_ena_plan(root, directory, plan, query, submission_request=None):
    expected = {"url": "https://www.ebi.ac.uk/ena/portal/api/search", "query": query,
                "fields": ENA_FIELDS, "result": "read_run", "format": "json",
                "canary_limit": "1", "full_limit": "0", "max_response_bytes": 2_000_000}
    if (any(plan.get(k) != value for k, value in expected.items())
            or plan.get("manually_reviewed") is not True
            or plan.get("sequence_or_assay_values_requested") is not False):
        raise ValueError("ENA query plan changed")
    marker_path = directory / "ena-search-fields-reviewed.json"
    if plan.get("search_fields_canary") != reference.pin(root, marker_path):
        raise ValueError("ENA field canary binding changed")
    marker = json.loads(marker_path.read_bytes())
    bind_canary(root, directory, marker, "ena-search-fields")
    search = list(csv.DictReader(io.StringIO(
        (directory / "ena-search-fields-response.bin").read_text()), delimiter="\t"))
    field = query.split("=", 1)[0]
    match = [r for r in search if r["columnId"] == field]
    if len(match) != 1 or match[0]["type"] != "text":
        raise ValueError("ENA query field was not verified")
    for kind in ("response", "receipt"):
        suffix = "response.bin" if kind == "response" else "receipt.json"
        if plan.get("return_fields_" + kind) != reference.pin(
                root, directory / ("ena-return-fields-" + suffix)):
            raise ValueError("ENA return-field definition binding changed")
    returned = list(csv.DictReader(io.StringIO(
        (directory / "ena-return-fields-response.bin").read_text()), delimiter="\t"))
    selected = [r for r in returned if r["columnId"] in ENA_FIELDS.split(",")]
    if (len(selected) != len(ENA_FIELDS.split(","))
            or {r["columnId"] for r in selected} != set(ENA_FIELDS.split(","))
            or sorted(selected, key=lambda r: r["columnId"]) != plan.get("selected_field_definitions")):
        raise ValueError("ENA selected return-field definitions changed")
    if submission_request is not None and (
            plan.get("scope") != "FOLLOW_EXPLICIT_STUDY_LINK_NOT_SUBMISSION_EQUIVALENCE"
            or any(plan.get("source_submission_" + k) != submission_request[k]
                   for k in ("response", "receipt"))):
        raise ValueError("ENA study plan lost its source submission binding")


def project_protein(entry, gene, taxonomy):
    result = reference.project_reference(entry, gene, 4932, taxonomy)
    block, = entry["genes"]
    if (block["geneName"]["value"] != gene or entry["organism"]["taxonId"] != 559292
            or "features" in entry):
        raise ValueError("reference gene, strain or feature scope changed")
    sgd, = [r["id"] for r in entry["uniProtKBCrossReferences"] if r["database"] == "SGD"]
    result.update({"primary_gene_name": gene, "sgd_id": sgd,
                   "gene_orf_names": [r["value"] for r in block.get("orfNames", [])],
                   "reuse_scope": "REFERENCE_IDENTITY_ONLY_NOT_A_TRANSFERRED_PHENOTYPE",
                   "focal_paper_in_bibliography": any(
                       i["id"] in {"23593013", primary.DOI} for b in result["bibliography"]
                       for i in b["identifiers"])})
    return result


def project_subjects(strains, coverage):
    if (strains[0] != ["Strain name", "Strain number", "Species", "Genotype", "Source"]
            or coverage[0] != ["Strain", "Mean Coverage"]):
        raise ValueError("source table headers changed")
    sequenced = [r[0] for r in coverage[1:]]
    if len(sequenced) != 8 or len(set(sequenced)) != 8:
        raise ValueError("source coverage membership changed")
    result = {}
    for label, (lab_id, gene) in SUBJECTS.items():
        rows = [r for r in strains[1:] if r[0] == label]
        if (len(rows) != 1 or len(rows[0]) != 5 or rows[0][1] != lab_id
                or rows[0][2] != "S. cerevisiae" or rows[0][4] != "This study" or label not in sequenced):
            raise ValueError("source lineage identity or WGS membership changed")
        result[label] = {"source_laboratory_id": lab_id, "gene": gene,
                         "source_species": "Saccharomyces cerevisiae", "species_taxon_id": "NCBITaxon:4932",
                         "species_grounding_basis": "PRIMARY_NAME_AND_REUSED_UNIPROT_REFERENCE_LINEAGE",
                         "listed_in_table_s1_wgs_coverage": True,
                         "table_s5_row_including_header": strains.index(rows[0]) + 1,
                         "exact_experimental_protein_assigned": False, "strain_taxon_id_assigned": False}
    return result


def project_archive(rows, experiment_xml, sample_xml):
    if (not rows or any(set(r) != set(ENA_FIELDS.split(",")) for r in rows)
            or len({r["run_accession"] for r in rows}) != len(rows)
            or {r["experiment_accession"] for r in rows} != set(EXPERIMENTS)):
        raise ValueError("archive membership is empty, duplicated or outside the inspected experiments")
    expected = {"study_accession": STUDY, "secondary_study_accession": SECONDARY_STUDY,
                "sample_accession": SAMPLE, "secondary_sample_accession": SECONDARY_SAMPLE,
                "submission_accession": SUBMISSION, "tax_id": "559292",
                "sample_alias": "Sc erg3 (ScLC10)", "scientific_name": "Saccharomyces cerevisiae S288C"}
    if any(any(r[k] != value for k, value in expected.items()) for r in rows):
        raise ValueError("archive study or shared-sample metadata changed")
    sample, = ElementTree.fromstring(sample_xml).findall("SAMPLE")
    attributes = sample.findall("SAMPLE_ATTRIBUTES/SAMPLE_ATTRIBUTE")
    attrs = {a.findtext("TAG"): a.findtext("VALUE") for a in attributes}
    if (sample.get("accession") != SAMPLE or sample.get("alias") != expected["sample_alias"]
            or len(attrs) != len(attributes)
            or sample.findtext("IDENTIFIERS/PRIMARY_ID") != SAMPLE
            or sample.findtext("IDENTIFIERS/SECONDARY_ID") != SECONDARY_SAMPLE
            or sample.findtext("SAMPLE_NAME/TAXON_ID") != "559292"
            or sample.findtext("SAMPLE_NAME/SCIENTIFIC_NAME") != expected["scientific_name"]
            or attrs.get("isolate") != "ScLC10"):
        raise ValueError("native sample identity or isolate label changed")
    experiments = []
    for accession, alias in EXPERIMENTS.items():
        entry, = ElementTree.fromstring(experiment_xml[accession]).findall("EXPERIMENT")
        descriptor, study = entry.find("DESIGN/SAMPLE_DESCRIPTOR"), entry.find("STUDY_REF")
        if (entry.get("accession") != accession or entry.get("alias") != alias
                or entry.findtext("TITLE") != "S. cerevisiae strain ScLC1367"
                or study.get("accession") != SECONDARY_STUDY
                or study.findtext("IDENTIFIERS/EXTERNAL_ID[@namespace='BioProject']") != STUDY
                or descriptor.get("accession") != SECONDARY_SAMPLE
                or descriptor.findtext("IDENTIFIERS/EXTERNAL_ID[@namespace='BioSample']") != SAMPLE):
            raise ValueError("native experiment identity, title or cross-reference changed")
        experiments.append({"experiment_accession": accession, "experiment_alias": alias,
                            "source_lineage": "Sc-F-1", "source_laboratory_id": "ScLC1367",
                            "join_basis": "EXPERIMENT_TITLE_TO_EXACT_SOURCE_TABLE_LABORATORY_ID",
                            "run_accessions": sorted(r["run_accession"] for r in rows
                                                     if r["experiment_accession"] == accession),
                            "linked_sample_label_conflict": True,
                            "unqualified_sample_or_genome_assignment": False,
                            "independent_biological_replicate_inferred": False})
    return {"source_submission_accession": SUBMISSION, "study_accession": STUDY,
            "secondary_study_accession": SECONDARY_STUDY, "unique_runs": len(rows),
            "unique_experiments": len(experiments), "unique_samples": 1,
            "experiments": experiments,
            "shared_sample_provenance": {"biosample_accession": SAMPLE,
                                         "archive_sample_accession": SECONDARY_SAMPLE,
                                         "source_isolate_label": attrs["isolate"],
                                         "source_reported_taxon_id": "NCBITaxon:559292",
                                         "taxon_is_exact_evolved_subject_assignment": False},
            "subject_experiment_matches": {"Sc-F-1": sorted(EXPERIMENTS), "Sc-G-13": []},
            "conflict": ("Experiment titles identify ScLC1367, but their shared sample "
                         "explicitly names ScLC10."),
            "conflict_resolved": False, "sc_g_13_gap_scope": "INSPECTED_STUDY_AND_EXPERIMENT_METADATA_ONLY",
            "sample_run_or_experiment_is_assembly": False, "assembly_search_performed": False,
            "genomes_absent_everywhere_inferred": False, "sequence_files_requested": False}


def project_figure(root, directory):
    first = json.loads((directory / "figure6-receipt.json").read_bytes())
    final = json.loads((directory / "figure6-storage-receipt.json").read_bytes())
    target = {k.lower(): v for k, v in first["headers"].items()}["location"]
    url = urlsplit(target)
    initial, body = directory / "figure6-response.bin", directory / "figure6-storage-response.bin"
    if (first["url"] != FIGURE or first["status"] != 302 or first["retry_performed"]
            or reference.digest(initial) != first["sha256"] or initial.read_bytes()
            or url.scheme != "https" or url.netloc != "storage.googleapis.com"
            or url.path != "/plos-corpus-prod/10.1371/journal.pgen.1003390/1/pgen.1003390.g006.PNG_L"
            or final["url"] != target or final["status"] != 200 or final["retry_performed"]
            or reference.digest(body) != final["sha256"]):
        raise ValueError("native figure provenance changed")
    return {"body": reference.pin(root, body), "source_url": FIGURE,
            "source_receipt": reference.pin(root, directory / "figure6-receipt.json"),
            "final_receipt": reference.pin(root, directory / "figure6-storage-receipt.json"),
            "final_url_without_query": urlunsplit((url.scheme, url.netloc, url.path, "", "")),
            "retrieved_at": final["retrieved_at"], "native_figure_visually_inspected": True}


def build(root, directory):
    plan_path = directory / "cohort.json"
    plan = json.loads(plan_path.read_bytes())
    if (plan["query"] != "gene_exact:MOT3 AND organism_id:559292 AND reviewed:true"
            or plan["fields"] != FIELDS or plan["figure6"] != FIGURE
            or {p["identifier"] for p in plan["records"]} != set(TARGETS) or len(plan["records"]) != 4):
        raise ValueError("reference or compound cohort changed")
    prior = json.loads(reference.check_pin(root, plan["prior"]).read_bytes())
    for key in ("prior_verification", "prior_progress", "protected"):
        reference.check_pin(root, plan[key])
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939:
        raise ValueError("historical census changed")
    for pin in plan["records"]:
        record = load_record(reference.check_pin(root, pin))
        row, = [r for r in census if r["identifier"] == pin["identifier"]]
        if (record["identifier"] != pin["identifier"] or row["record_sha256"] != pin["sha256"]
                or record["chemical_structure"]["standard_inchi_key"] != TARGETS[pin["identifier"]]
                or len(record.get("resistance_mechanisms", [])) != pin["existing_assertions"]):
            raise ValueError("record identity or existing evidence changed")
    canary_path = directory / "canaries-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    bind_canary(root, directory, canary["reference"], "mot3")
    bind_canary(root, directory, canary["figure"], "figure6-storage")
    if (canary.get("primary_results_subsection_and_figure6_caption_read") is not True
            or canary.get("source_table_selected_identifiers_checked") is not True):
        raise ValueError("primary review attestations missing")
    old_tax = prior["taxonomy_reuse"]["559292"]["request"]
    taxonomy, tax_request = reference.read_response(
        root, (root / old_tax["cache"]["path"]).parent, "tax-559292", "/taxonomy/559292")
    if tax_request != old_tax:
        raise ValueError("reference taxonomy reuse changed")
    body, mot_request = reference.read_response(root, directory, "mot3", "/uniprotkb/search", {
        "query": [plan["query"]], "format": ["json"], "size": ["10"], "fields": [FIELDS]})
    mot, = body["results"]
    old = json.loads(reference.check_pin(root, plan["pdr1_reuse"]).read_bytes())["references"]["PDR1"]
    request = old["request"]
    cache = json.loads(reference.check_pin(root, request["cache"]).read_bytes())
    cached.validate_cached_response(cache, "https://rest.uniprot.org/uniprotkb/search", {
        "query": "gene_exact:PDR1 AND organism_id:559292 AND reviewed:true",
        "format": "json", "size": "10", "fields": FIELDS})
    headers = {k.lower(): v for k, v in cache["headers"].items()}
    pdr, = json.loads(cache["body"])["results"]
    if (headers.get("link") or headers["x-total-results"] != "1" or cache["sha256"] != request["body_sha256"]
            or headers["x-uniprot-release"] != mot_request["release"]
            or mot_request["release"] != tax_request["release"]):
        raise ValueError("reused reference coverage or release changed")
    proteins = {gene: project_protein(entry, gene, taxonomy)
                for gene, entry in (("PDR1", pdr), ("MOT3", mot))}
    if (proteins["PDR1"]["protein_accession"] != old["accession"]
            or proteins["PDR1"]["sgd_id"] != old["sgd_id"]):
        raise ValueError("PDR1 reuse identity changed")
    assets = {key: primary.project_asset(root, key, {k: prior["primary"]["assets"][key][k]
                                                   for k in ("body", "source_receipt", "final_receipt")})
              for key in ("article", "table-s1", "table-s5")}
    subjects = project_subjects(primary.read_table(root / assets["table-s5"]["body"]["path"]),
                                primary.read_table(root / assets["table-s1"]["body"]["path"]))
    figure = project_figure(root, directory)
    snapshots, requests, ena_plans = {}, {}, {}
    for key, endpoint in (("ena-search-fields", "searchFields"), ("ena-return-fields", "returnFields")):
        _, requests[key] = read_ena(
            root, directory, key, "/ena/portal/api/" + endpoint, {"result": ["read_run"]})
    for key, query, plan_file in (("ena-runs", f'submission_accession="{SUBMISSION}"', "ena-plan.json"),
                                  ("ena-study", f'study_accession="{STUDY}"', "ena-study-plan.json")):
        query_plan = json.loads((directory / plan_file).read_bytes())
        validate_ena_plan(root, directory, query_plan, query, requests.get("ena-runs"))
        ena_plans[key] = reference.pin(root, directory / plan_file)
        marker = json.loads((directory / f"{key}-canary-reviewed.json").read_bytes())
        bind_canary(root, directory, marker, key + "-canary")
        if marker["plan"] != ena_plans[key]:
            raise ValueError("ENA canary is bound to a different plan")
        for suffix, limit in (("-canary", "1"), ("", "0")):
            payload, requests[key + suffix] = read_ena(
                root, directory, key + suffix, "/ena/portal/api/search", {
                    "result": ["read_run"], "query": [query], "fields": [ENA_FIELDS],
                    "format": ["json"], "limit": [limit]})
            snapshots[key + suffix] = json.loads(payload)
        if len(snapshots[key + "-canary"]) != 1 or snapshots[key + "-canary"][0] not in snapshots[key]:
            raise ValueError("ENA canary row missing from complete query")
    if sorted(snapshots["ena-runs"], key=lambda r: r["run_accession"]) != sorted(
            snapshots["ena-study"], key=lambda r: r["run_accession"]):
        raise ValueError("submission and study snapshots no longer have identical memberships")
    exp_canary = json.loads((directory / "ena-experiment-canary-reviewed.json").read_bytes())
    bind_canary(root, directory, exp_canary, "ena-SRX220258")
    xmls = {}
    for accession in EXPERIMENTS:
        xmls[accession], requests[accession] = read_ena(
            root, directory, "ena-" + accession, "/ena/browser/api/xml/" + accession)
    sample_xml, requests["sample"] = read_ena(root, directory, "ena-sample", "/ena/browser/api/xml/SRS387829")
    archive = project_archive(snapshots["ena-study"], xmls, sample_xml)
    return {
        "date": "2026-10-13", "scope": "CONDITIONAL_REGULATOR_EVIDENCE_AND_QUALIFIED_ARCHIVE_LINKS",
        "inputs": {"plan": reference.pin(root, plan_path), "prior": plan["prior"], "census": plan["census"],
                   "prior_progress": plan["prior_progress"], "baseline": plan["protected"],
                   "canaries": reference.pin(root, canary_path)},
        "records": [{**p, "assertions_added": [], "whole_record_review": "OPEN"} for p in plan["records"]],
        "primary": {"doi": primary.DOI, "pmid": "23593013", "reused_assets": assets, "figure6": figure,
                    "whole_article_review_complete": False,
                    "source_layout_limit": prior["primary"]["manual_review"]["source_layout_limit"]},
        "subjects": subjects, "reference_proteins": proteins,
        "uniprot_requests": {"MOT3": mot_request, "PDR1_reused": request}, "taxonomy_reused": tax_request,
        "conditional_findings": [
            {"lineage": "Sc-F-1", "gene": "MOT3",
             "locations": ["Results WGS yeast subsection", "Figure 6A-C"],
             "tacrolimus_plus_fluconazole": "FUNCTIONAL_PHENOCOPY_SUPPORT_NOT_DIRECT_TEST_OF_EXACT_ALLELE",
             "cyclosporin_a_plus_fluconazole": "LINEAGE_CROSS_RESISTANCE_NOT_INDEPENDENT_ALLELE_TEST",
             "calcineurin_independence": "FUNCTIONAL_SUPPORT_IN_TESTED_LINEAGE_AND_COMBINATION"},
            {"lineage": "Sc-G-13", "gene": "PDR1",
             "locations": ["Results WGS yeast subsection", "Figure 6D-E"],
             "geldanamycin_plus_fluconazole": "FUNCTIONAL_COMPARISON_SUPPORT_WITH_EXPRESSION_CONTEXT_CAVEAT",
             "radicicol_or_tacrolimus_plus_fluconazole": "NO_INCREASED_CROSS_RESISTANCE_REPORTED",
             "pdr5_efflux_route": "PROPOSED_EXPLANATION_NOT_DIRECTLY_MEASURED_IN_THIS_COMPARISON",
             "residual_response": "RETAINED_WITH_ANCESTRAL_REFERENCE_COMPARISON_AND_EXPRESSION_CONTEXT"},
        ],
        "archive_context": {**archive, "requests": requests, "query_plans": ena_plans,
                            "complete_for_requested_limit_zero_queries": True,
                            "metadata_documentation": [
                                "https://ena-docs.readthedocs.io/en/latest/retrieval/programmatic-access/advanced-search.html",
                                "https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html"]},
        "curation_decision": "HOLD_UNCONDITIONAL_SINGLE_DRUG_ASSERTIONS_AND_CONFLICTED_SAMPLE_ASSIGNMENTS",
        "summary": {"corpus_records_in_scope": 2939, "selected_records": 4, "source_lineages": 2,
                    "reference_proteins": 2, "new_uniprot_queries": 1, "reused_uniprot_queries": 1,
                    "new_taxonomy_queries": 0, "ena_metadata_requests": len(requests),
                    "lineages_with_experiment_title_matches": 1, "sample_annotation_conflicts": 1,
                    "assembly_accessions_assigned": 0, "experimental_alleles_assigned": 0,
                    "biological_records_changed": 0, "whole_records_completed": 0},
        "limitations": [
            "Reference proteins and reference-strain TaxIDs do not identify the experimental alleles.",
            "Combination findings are not unconditional single-drug or species-wide resistance assertions.",
            "Phenocopy supports a gene-level interpretation, "
            "not an independent test of the exact source allele.",
            "Expression context and negative cross-resistance comparisons "
            "remain part of the PDR1 interpretation.",
            "A matched experiment title is qualified by its conflicting linked sample metadata.",
            "Two experiments and eleven runs are not eleven independent biological isolates.",
            "No matching Sc-G-13 experiment in these snapshots does not imply no sequencing data elsewhere.",
            "Other genes, lineages and discovery leads remain open; no whole-record review is complete.",
            "Offline replay checks metadata, joins and source bytes, "
            "not the truth of scientific interpretation.",
            "No sequences, exact variant specifications, constructs, protocols or numeric AST are exported.",
        ],
        "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "github_mutations_this_checkpoint": 0,
                        "source_adoptions": 0, "reuse_terms_review_resumed": False, "issue_1040": "DEFERRED"},
        "attribution": [{"source": "Hill et al. (2013), PLOS Genetics", "doi": primary.DOI,
                         "license": "Creative Commons Attribution (as stated by publisher)"},
                        {"source": "UniProt Consortium", "license": "CC BY 4.0",
                         "license_url": "https://www.uniprot.org/help/license"},
                        {"source": "European Nucleotide Archive, EMBL-EBI",
                         "scope": "Identifier metadata only"}],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    result = build(root, root / args.cache)
    payload = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.check:
        if args.output.read_text() != payload:
            raise ValueError("dossier does not reproduce")
    else:
        with args.output.open("x") as stream:
            stream.write(payload)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

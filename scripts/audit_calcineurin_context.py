"""Replay conditional fungal evidence, locus aliases and reference-only grounding."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import audit_hsp90_context as primary
import audit_topoisomerase_references as reference
import audit_yeast_regulator_context as yeast

from antibioticmech.activity_collections import load_record

DEFAULT_CACHE = Path("reports/resistance-grounding-2026-10-13-calcineurin")
DEFAULT_OUTPUT = Path("research/2026-10-13-calcineurin-context.json")
QUERIES = {
    "fpr1": "gene_exact:FPR1 AND organism_id:559292 AND reviewed:true",
    "cnb1": "gene_exact:CNB1 AND organism_id:559292 AND reviewed:true",
    "cna1": "(gene_exact:CNA1 OR gene_exact:CMP1 OR gene_exact:orf19.6033) AND organism_id:237561",
    "lcb1": "(gene_exact:LCB1 OR gene_exact:orf19.6438 OR gene_exact:CaO19.6438) AND organism_id:237561",
}
LOCUS_QUERY = "gene_exact:orf19.13796 AND organism_id:237561"
CGD_VERSION = "A22-s08-m01-r37"
CGD_URL = ("https://www.candidagenome.org/download/chromosomal_feature_files/C_albicans_SC5314/"
           "C_albicans_SC5314_version_A22-s08-m01-r37_chromosomal_feature.tab")
CGD_IDS = {"cna1": "CAL0000201614", "cna1_homonym": "CAL0000177603", "lcb1": "CAL0000192873"}
TARGETS = {**yeast.TARGETS, "CHEBI:582124": "ZZIKIHCNFWXKDY-GNTQXERDSA-N",
           "CHEBI:46081": "RFHAOTPXVQNOHP-UHFFFAOYSA-N",
           "antibioticmech:aro-11ab0a98bf": "BYBLEWFAAKGYCD-UHFFFAOYSA-N"}
SUBJECTS = {"Sc-F-2": "ScLC1441", "Sc-F-3": "ScLC1443", "Ca-F-4": "CaLC1370",
            "Ca-F-5": "CaLC1371", "Ca-F-6": "CaLC1372", "Ca-F-7": "CaLC1373",
            "Ca-F-8": "CaLC1374", "Ca-F-9": "CaLC1503"}


def project_cgd(wrapper):
    body = wrapper["body"]
    if (wrapper["status"] != 200 or wrapper["url"] != CGD_URL
            or hashlib.sha256(body.encode()).hexdigest() != wrapper["sha256"]
            or f"! Genome version: {CGD_VERSION}" not in body):
        raise ValueError("CGD version, request or payload changed")
    rows = [r for r in csv.reader(io.StringIO(body), delimiter="\t") if r and not r[0].startswith("!")]
    result = {}
    for key, cgd_id in CGD_IDS.items():
        matches = [r for r in rows if len(r) > 10 and r[8] == cgd_id]
        if len(matches) != 1:
            raise ValueError("CGD reference feature is absent or ambiguous")
        row, = matches
        result[key] = {"feature": row[0], "primary_gene_name": row[1] or None,
                       "aliases": row[2].split("|"), "feature_type": row[3], "cgd_id": row[8]}
    if (result["cna1"]["primary_gene_name"] != "CMP1"
            or result["cna1_homonym"]["primary_gene_name"] != "PDE1"
            or any("CNA1" not in result[k]["aliases"] for k in ("cna1", "cna1_homonym"))
            or result["lcb1"]["primary_gene_name"] is not None
            or not {"LCB1", "orf19.6438", "orf19.13796"} <= set(result["lcb1"]["aliases"])):
        raise ValueError("CGD alias ambiguity or locus crosswalk changed")
    return result


def bibliography_scope(entry):
    identifiers = {i["id"] for ref in entry.get("references", [])
                   for i in ref.get("citation", {}).get("citationCrossReferences", [])
                   if i["database"] == "PubMed"}
    return {"source_bibliography_pmids": sorted(identifiers),
            "focal_paper_in_bibliography": "23593013" in identifiers,
            "other_bibliography_primary_results_reviewed": False}


def project_candida(entry, key, taxonomy, feature):
    expected_gene, expected_locus = {"cna1": ("CMP1", "orf19.13454"), "lcb1": (None, "orf19.13796")}[key]
    if (entry["entryType"] != "UniProtKB unreviewed (TrEMBL)" or "sequence" in entry or "features" in entry
            or entry["organism"]["taxonId"] != 237561 or taxonomy["taxonId"] != 237561
            or taxonomy.get("active") is not True or taxonomy["rank"] != "strain"
            or [r["taxonId"] for r in taxonomy["lineage"] if r["rank"] == "species"] != [5476]):
        raise ValueError("Candida reference status, organism or payload scope changed")
    gene, = entry["genes"]
    loci = gene.get("orderedLocusNames", [])
    matches = [locus for locus in loci if locus["value"] == expected_locus]
    if (gene.get("geneName", {}).get("value") != expected_gene or len(matches) != 1
            or expected_locus not in feature["aliases"] or feature["cgd_id"] != CGD_IDS[key]
            or not any(e.get("source") == "CGD" and e.get("id") == feature["cgd_id"]
                       for e in matches[0].get("evidences", []))):
        raise ValueError("Candida locus lacks the exact CGD evidence join")
    versions = entry["entryAudit"]
    if any(type(versions.get(k)) is not int or versions[k] < 1 for k in ("entryVersion", "sequenceVersion")):
        raise ValueError("Candida reference versions missing")
    return {"protein_accession": "UniProtKB:" + entry["primaryAccession"],
            "entry_version": versions["entryVersion"], "sequence_version": versions["sequenceVersion"],
            "entry_type": entry["entryType"], "primary_gene_name": expected_gene,
            "ordered_locus_names": [locus["value"] for locus in loci], "cgd_feature": feature,
            "protein_name": entry["proteinDescription"]["recommendedName"]["fullName"]["value"],
            "reference_taxon_id": "NCBITaxon:237561", "reference_taxon_rank": "strain",
            "reference_organism_name": entry["organism"]["scientificName"],
            "source_species_taxon_id": "NCBITaxon:5476", "species_lineage_verified": True,
            "join_basis": "EXACT_CGD_LOCUS_ALIAS_AND_UNIPROT_LOCUS_ANNOTATION_EVIDENCE_ID",
            "experimental_subject_assignment": False, "exact_resistance_allele": False,
            "experimental_haplotype_assigned": False, "reviewed_function_inferred": False,
            **bibliography_scope(entry)}


def project_subjects(strains, coverage):
    if (strains[0] != ["Strain name", "Strain number", "Species", "Genotype", "Source"]
            or coverage[0] != ["Strain", "Mean Coverage"]):
        raise ValueError("source table headers changed")
    sequenced = [r[0] for r in coverage[1:]]
    if len(sequenced) != 8 or len(set(sequenced)) != 8:
        raise ValueError("source WGS coverage membership changed")
    result = {}
    for label, lab_id in SUBJECTS.items():
        rows = [r for r in strains[1:] if r[0] == label]
        candida = label.startswith("Ca-")
        if (len(rows) != 1 or len(rows[0]) != 5 or rows[0][1] != lab_id
                or rows[0][2] != ("C. albicans" if candida else "S. cerevisiae")
                or rows[0][4] != "This study" or (label in sequenced) != candida):
            raise ValueError("source subject or WGS membership changed")
        result[label] = {"source_laboratory_id": lab_id, "source_species": rows[0][2],
                         "species_taxon_id": "NCBITaxon:" + ("5476" if candida else "4932"),
                         "species_grounding_basis": "PRIMARY_NAME_AND_REUSED_UNIPROT_REFERENCE_LINEAGE",
                         "table_s5_row_including_header": strains.index(rows[0]) + 1,
                         "listed_in_table_s1_wgs_coverage": candida,
                         "exact_experimental_protein_assigned": False, "strain_taxon_id_assigned": False,
                         "experimental_sample_or_assembly_assigned": False}
    return result


def project_figure(root, directory, number):
    key = f"figure{number}"
    first_path, final_path = directory / f"{key}-receipt.json", directory / f"{key}-storage-receipt.json"
    first, final = [json.loads(p.read_bytes()) for p in (first_path, final_path)]
    initial, body = directory / f"{key}-response.bin", directory / f"{key}-storage-response.bin"
    url = ("https://journals.plos.org/plosgenetics/article/figure/image?download&size=large"
           f"&id={primary.DOI}.g{number:03}")
    target = {k.lower(): v for k, v in first["headers"].items()}["location"]
    parsed = urlsplit(target)
    if (number not in {5, 7, 8} or first["url"] != url or first["status"] != 302
            or first["retry_performed"] is not False or initial.read_bytes()
            or reference.digest(initial) != first["sha256"]
            or parsed.scheme != "https" or parsed.netloc != "storage.googleapis.com"
            or parsed.path != f"/plos-corpus-prod/{primary.DOI}/1/pgen.1003390.g{number:03}.PNG_L"
            or final["url"] != target or final["status"] != 200 or final["retry_performed"] is not False
            or reference.digest(body) != final["sha256"] or final["bytes"] != body.stat().st_size):
        raise ValueError("native figure provenance changed")
    return {"body": reference.pin(root, body), "source_receipt": reference.pin(root, first_path),
            "final_receipt": reference.pin(root, final_path), "source_url": url,
            "final_url_without_query": urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", "")),
            "retrieved_at": final["retrieved_at"], "native_figure_visually_inspected": True}


def validate_inspection(root, directory, inspection):
    required = ("primary_results_subsections_and_captions_read", "source_table_selected_identifiers_checked",
                "cna1_cgd_homonym_retained", "lcb1_primary_gene_name_not_invented",
                "figure5_panel_c_miconazole_not_fluconazole",
                "figure7b_tacrolimus_not_separate_cyclosporin_a_allele_test",
                "figure7c_control_discordance_retained",
                "figure8_copy_number_profiles_not_gene_specific_causation")
    if (any(inspection.get(key) is not True for key in required)
            or inspection.get("whole_article_review_complete") is not False
            or inspection.get("sequence_variant_construct_protocol_or_numeric_ast_exported") is not False
            or inspection.get("reference_projections_reviewed") != ["fpr1", "cnb1", "cna1", "lcb1-locus"]
            or set(inspection.get("figures", {})) != {"5", "7", "8"}):
        raise ValueError("primary inspection scope changed")
    for number, marker in inspection["figures"].items():
        yeast.bind_canary(root, directory, marker, f"figure{number}-storage")


def build(root, directory):
    plan_path, inspection_path = directory / "cohort.json", directory / "inspection.json"
    plan, inspection = [json.loads(p.read_bytes()) for p in (plan_path, inspection_path)]
    if (plan["queries"] != QUERIES or plan["fields"] != yeast.FIELDS or plan["size"] != "50"
            or len(plan["records"]) != 7 or {r["identifier"] for r in plan["records"]} != set(TARGETS)):
        raise ValueError("reference or compound cohort changed")
    for key in ("baseline", "prior_verification", "progress"):
        reference.check_pin(root, plan[key])
    prior = json.loads(reference.check_pin(root, plan["prior"]).read_bytes())
    hsp = json.loads(reference.check_pin(root, plan["hsp90"]).read_bytes())
    if yeast.build(root, root / yeast.DEFAULT_CACHE) != prior:
        raise ValueError("reused archive context does not replay")
    with reference.check_pin(root, plan["census"]).open(newline="") as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if len(census) != 2939:
        raise ValueError("historical census changed")
    for item in plan["records"]:
        record = load_record(reference.check_pin(root, item))
        row, = [r for r in census if r["identifier"] == item["identifier"]]
        if (record["identifier"] != item["identifier"] or row["record_sha256"] != item["sha256"]
                or record["chemical_structure"]["standard_inchi_key"] != TARGETS[item["identifier"]]
                or len(record.get("resistance_mechanisms", [])) != item["existing_assertions"]):
            raise ValueError("record identity or source assertions changed")
    validate_inspection(root, directory, inspection)
    canary_path = directory / "canary-reviewed.json"
    canary = json.loads(canary_path.read_bytes())
    yeast.bind_canary(root, directory, canary["reference"], "fpr1")
    yeast.bind_canary(root, directory, canary["figure"], "figure5-storage")
    if canary.get("figure5_panel_c_azole") != "miconazole":
        raise ValueError("FPR1 functional comparison compound changed")
    taxonomy, tax_requests = {}, {}
    for taxid, key, endpoint in (("559292", "tax-559292", "/taxonomy/559292"),
                                 ("237561", "taxonomy-237561", "/taxonomy/237561.json")):
        expected = hsp["taxonomy_reuse"][taxid]["request"]
        taxonomy[taxid], tax_requests[taxid] = reference.read_response(
            root, (root / expected["cache"]["path"]).parent, key, endpoint)
        if tax_requests[taxid] != expected:
            raise ValueError("reused taxonomy request changed")
    cgd = project_cgd(json.loads(reference.check_pin(root, plan["cgd_snapshot"]).read_bytes()))
    follow_path = directory / "lcb1-locus-plan.json"
    follow = json.loads(follow_path.read_bytes())
    if (follow.get("query") != LOCUS_QUERY or follow.get("fields") != yeast.FIELDS
            or follow.get("size") != "50" or follow.get("manually_reviewed") is not True
            or follow.get("protein_absence_inferred") is not False
            or follow.get("retry_of_failed_request") is not False or follow.get("cgd_id") != CGD_IDS["lcb1"]
            or follow.get("source_cgd_snapshot") != plan["cgd_snapshot"]
            or follow.get("query_alias") != "orf19.13796"
            or follow["query_alias"] not in cgd["lcb1"]["aliases"]
            or follow.get("feature") != cgd["lcb1"]["feature"]
            or follow.get("source_paper_alias") != "orf19.6438"):
        raise ValueError("LCB1 follow-up is not an explicit source-locus join")
    for kind, suffix in (("response", "response.bin"), ("receipt", "receipt.json")):
        if follow["previous_" + kind] != reference.pin(root, directory / f"lcb1-{suffix}"):
            raise ValueError("LCB1 zero-hit source binding changed")
    entries, requests = {}, {}
    for key, query in {**QUERIES, "lcb1-locus": LOCUS_QUERY}.items():
        body, requests[key] = reference.read_response(root, directory, key, "/uniprotkb/search", {
            "query": [query], "format": ["json"], "size": ["50"], "fields": [yeast.FIELDS]})
        results = body["results"]
        if len(results) != (0 if key == "lcb1" else 1) or requests[key]["release"] != "2026_03":
            raise ValueError("reference query coverage or release changed")
        if results:
            entries[key] = results[0]
        requests[key].update({"results": len(results), "complete_for_query": True,
                              "all_strains_and_aliases_searched": False})
    proteins = {}
    for key in ("fpr1", "cnb1"):
        protein = yeast.project_protein(entries[key], key.upper(), taxonomy["559292"])
        protein.pop("bibliography")
        proteins[key] = {**protein, **bibliography_scope(entries[key])}
    for key, response_key in (("cna1", "cna1"), ("lcb1", "lcb1-locus")):
        proteins[key] = project_candida(entries[response_key], key, taxonomy["237561"], cgd[key])
    assets = {key: primary.project_asset(root, key, {k: hsp["primary"]["assets"][key][k]
                                                   for k in ("body", "source_receipt", "final_receipt")})
              for key in ("article", "table-s1", "table-s5")}
    subjects = project_subjects(primary.read_table(root / assets["table-s5"]["body"]["path"]),
                                primary.read_table(root / assets["table-s1"]["body"]["path"]))
    return {
        "date": "2026-10-13", "scope": "CONDITIONAL_EVIDENCE_AND_REFERENCE_LOCUS_DISAMBIGUATION",
        "inputs": {**{k: plan[k] for k in (
                       "prior", "hsp90", "census", "baseline", "progress", "cgd_snapshot")},
                   "plan": reference.pin(root, plan_path), "inspection": reference.pin(root, inspection_path),
                   "canary": reference.pin(root, canary_path),
                   "locus_followup": reference.pin(root, follow_path)},
        "records": [{**r, "assertions_added": [], "whole_record_review": "OPEN",
                     "tested_preparation_independently_reidentified": False} for r in plan["records"]],
        "primary": {"doi": primary.DOI, "pmid": "23593013", "reused_assets": assets,
                    "native_figures": {str(n): project_figure(root, directory, n) for n in (5, 7, 8)},
                    "whole_article_review_complete": False,
                    "source_layout_limit": hsp["primary"]["manual_review"]["source_layout_limit"]},
        "subjects": subjects, "reference_proteins": proteins, "uniprot_requests": requests,
        "taxonomy_reused": tax_requests, "cgd_version": CGD_VERSION, "cgd_reference_features": cgd,
        "cna1_disambiguation": {"source_name": "CNA1", "selected_reference_gene": "CMP1",
                                "basis": ("CGD_ALIAS_AND_CALCINEURIN_CONTEXT_"
                                          "PLUS_EXACT_UNIPROT_CGD_LOCUS_EVIDENCE"),
                                "other_cgd_alias_gene": "PDE1", "other_alias_is_protein_absence": False,
                                "experimental_allele_or_haplotype_assigned": False},
        "conditional_findings": [
            {"gene": "FPR1", "lineage": "Sc-F-3", "location": "Figure 5A,C,E; selected FPR1 Results",
             "lineage_profile_azole": "fluconazole", "functional_comparison_azole": "miconazole",
             "partner": "tacrolimus", "evidence": "RECIPROCAL_FUNCTIONAL_COMPARISONS",
             "binding_change": "PROPOSED_NOT_DIRECTLY_MEASURED_HERE", "expression_context_caveat": True},
            {"gene": "FPR1", "lineage": "Sc-F-2", "location": "Figure 5B,D,F; selected FPR1 Results",
             "lineage_profile_azole": "fluconazole", "functional_comparison_azole": "fluconazole",
             "partner": "tacrolimus", "evidence": "RECIPROCAL_FUNCTIONAL_COMPARISONS",
             "binding_change": "PROPOSED_NOT_DIRECTLY_MEASURED_HERE", "expression_context_caveat": True},
            {"gene": "CNB1", "lineages": ["Sc-F-2", "Sc-F-3"], "location": "Figure 5E,F",
             "evidence": "PATHWAY_DEPENDENCY_NOT_AN_IDENTIFIED_EVOLVED_RESISTANCE_ALLELE",
             "azole": "fluconazole", "partner": "tacrolimus"},
            {"gene": "CNA1 (reference CMP1)", "lineage": "Ca-F-9", "location": "Figure 7A,B",
             "evidence": "FUNCTIONAL_DEPENDENCY_IN_EVOLVED_BACKGROUND_NOT_INDEPENDENT_SUFFICIENCY",
             "azole": "fluconazole", "functional_panel_partner": "tacrolimus",
             "cyclosporin_a": "LINEAGE_PROFILE_NOT_SEPARATE_ALLELE_SPECIFIC_FUNCTIONAL_PANEL"},
            {"gene": "LCB1-associated orf19.6438", "lineage": "Ca-F-8", "location": "Figure 7C",
             "evidence": "CANDIDATE_WITH_PHARMACOLOGICAL_SUPPORT_NOT_ALLELE_SPECIFIC_GENETIC_VALIDATION",
             "azole": "fluconazole", "partner": "tacrolimus", "modifier": "myriocin",
             "controls": "ANCESTRAL_RESPONSE_DIFFERS_AND_CA_F_9_REMAINS_RESISTANT_IN_REPORTED_COMPARISON",
             "direct_myriocin_resistance_claim": False},
        ],
        "lineage_profiles": {
            "yeast_negative_cross_comparisons": (
                "NO_INCREASED_GELDANAMYCIN_OR_CYCLOSPORIN_A_COMBINATION_RESPONSE"),
            "candida_lineages": [label for label in SUBJECTS if label.startswith("Ca-")],
            "candida_calcineurin_inhibitor_combinations": "SOURCE_REPORTED_LINEAGE_CROSS_RESISTANCE",
            "aneuploidy_figure": "Figure 8", "aneuploidy_lineages": [f"Ca-F-{n}" for n in range(4, 8)],
            "aneuploidy_gene_specific_causality_inferred": False,
        },
        "archive_context": {"reused_dossier": plan["prior"], "new_archive_requests": 0,
                            "scope": "PREVIOUSLY_INSPECTED_STUDY_AND_TWO_NATIVE_EXPERIMENTS_ONLY",
                            "those_experiments_identify": (
                                "ScLC1367, not any of these eight source laboratory IDs"),
                            "experimental_sample_or_assembly_assignments": [],
                            "universal_genome_absence_inferred": False},
        "summary": {"corpus_records_in_scope": 2939, "selected_records": 7, "source_lineages": 8,
                    "reference_proteins": 4, "reviewed_references": 2, "unreviewed_references": 2,
                    "new_uniprot_queries": 5, "successful_zero_hit_queries": 1, "new_taxonomy_queries": 0,
                    "new_native_figures_inspected": 3, "biological_records_changed": 0,
                    "experimental_alleles_assigned": 0, "whole_records_completed": 0},
        "curation_decision": (
            "RETAIN_QUALIFIED_RESEARCH_NO_UNCONDITIONAL_SINGLE_AGENT_OR_EXACT_ALLELE_ASSERTION"),
        "limitations": [
            "Reference proteins, strain TaxIDs and haplotype-paired aliases are not experimental allele IDs.",
            "Unreviewed protein annotations and CGD orthology do not independently establish gene function.",
            "A dependency test, an allele-specific comparison and a pharmacological modifier are distinct.",
            "The same paper uses different azoles in different functional and lineage panels.",
            "Corpus structures are pinned; "
            "the paper's tested preparations were not independently reidentified.",
            "No direct drug-binding measurement is established here.",
            "CNA1 dependency and LCB1 pharmacology do not independently establish sufficiency.",
            "Chromosome-wide associations do not identify which amplified gene causes the phenotype.",
            "A successful zero-hit alias query is not protein absence; the locus query resolves it.",
            "Other candidate variants, source supplements and corpus records remain incompletely reviewed.",
            "No sequences, exact variants, constructs, protocols, numeric AST or clinical calls exported.",
            "Replay checks source bytes and identifier joins, not scientific truth.",
        ],
        "constraints": {"ncbi_requests": 0, "ncbi_contact": 0, "github_mutations_this_checkpoint": 0,
                        "source_adoptions": 0, "reuse_terms_review_resumed": False, "issue_1040": "DEFERRED"},
        "attribution": [{"source": "Hill et al. (2013), PLOS Genetics", "doi": primary.DOI,
                         "license": "Creative Commons Attribution (as stated by publisher)"},
                        {"source": "UniProt Consortium", "license": "CC BY 4.0",
                         "license_url": "https://www.uniprot.org/help/license"},
                        {"source": "Candida Genome Database", "version": CGD_VERSION,
                         "scope": "Selected reference identifiers from an existing pinned local snapshot"}],
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

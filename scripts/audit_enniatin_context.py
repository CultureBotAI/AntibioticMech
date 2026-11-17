"""Keep congener, host, locus and reference-protein evidence at their source scope."""

import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import audit_card_reference_lineages as lineages
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import FIELDS, planned_source
from lxml import etree

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-enniatin")
OUTPUT = Path("research/2026-10-14-enniatin-context.json")
COHORT_SHA = "6543d4acf85a24b3ede417c5cc64c9db6b131345a70f1c9aed7aca9f318f9a2c"
ARTICLE_SHA = "4d841db58951bd814e83c5ccc35f30d1b3a59c14f26d6eef054f23943f66fffe"
ARTICLE = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13412724/fullTextXML"
DOI = "10.3390/jof12070524"
RECORDS = {
    "CHEBI:64651": ("enniatin A", "TWHBYJSVDCWICV-BHZTXFQCSA-N", 26, True),
    "CHEBI:64649": ("enniatin B", "MIZMDSVSLSIMSC-VYLWARHZSA-N", 13, False),
    "CHEBI:3000": ("beauvericin", "GYSCAQFHASJXRS-FFCOJMSVSA-N", 58, True),
}
QUERIES = {
    "reference-locus": ("gene_exact:FGSG_08823", "reference-plan.json", 0, FIELDS),
    "reference-alternatives": (
        "(gene_exact:FGRAMPH1_01G10921 OR gene_exact:FGRAMPH1_01G010921)",
        "alternative-locus-plan.json",
        0,
        FIELDS,
    ),
    "reference-crossreferences": (
        "(FGSG_08823 OR FGRAMPH1_01G10921 OR FGRAMPH1_01G010921)",
        "crossreference-plan.json",
        1,
        FIELDS + ",xref_ensemblfungi",
    ),
    "reference-candidate": (
        "accession:I1RWY3",
        "candidate-plan.json",
        1,
        FIELDS + ",xref_ensemblfungi,xref_embl,xref_geneid,xref_veupathdb",
    ),
}
CONFIG = {
    "path": (
        "reports/resistance-grounding-2026-10-07/"
        "request-8fe4098edafef3b5de6fb5c6dd7acb757772a3386e2e3444ab2b866b2be95d74.json"
    ),
    "sha256": "fc90c1b1e93a13da4abc9b76c9bccef0868f71ed7eab096f431e56aa1e180551",
}
TAXONOMY = {
    "5518": {
        "path": (
            "reports/resistance-grounding-2026-10-07/"
            "request-3f789375d311f00135899d5556b7203c0fa994132446e131c6e3e215a77bab7e.json"
        ),
        "sha256": "40a7a92b13b4df4f8169304a3bdf9bf182ffd9554975d575188cb967a5c5c75e",
    },
    "229533": {
        "path": (
            "reports/resistance-grounding-2026-10-07/"
            "request-6bd68ecae369102087f2743c12dbe4acfb922c193e8ddbc19f817fe68b2550f5.json"
        ),
        "sha256": "c348b59f45381322ca362da40e09cf51d0204fe4ab9cc8e7fd3b6f8498b07673",
    },
    "4932": {
        "path": (
            "reports/resistance-grounding-2026-10-09-transport-context/"
            "request-f07361fe8f8eaa36e1d0d63c89157cb978fc7a29bfcd3cf2e5f95e09f5b97d51.json"
        ),
        "sha256": "a5ccd6582704c3fe1acbdead1300386d9cc239b6c413698323b9e8343e68ffc7",
    },
}
LOCATIONS = {
    "mixed_extracts": ("/article/body/sec[3]/sec[2]/p[1]", "secondary metabolites"),
    "reported_gene_aliases": ("/article/body/sec[3]/sec[2]/p[2]", "FGRAMPH1_01G10921"),
    "discordant_locus_label": ("/article/body/sec[3]/sec[2]/p[3]", "FGRAMPH1_01G010921"),
    "induction": ("/article/body/sec[3]/sec[3]/p[1]", "enniatin B1"),
    "donor_and_host": ("/article/body/sec[3]/sec[4]/p[1]", "Saccharomyces cerevisiae"),
    "yeast_growth": ("/article/body/sec[3]/sec[4]/p[2]", "enniatin B1"),
    "export_endpoint": ("/article/body/sec[3]/sec[4]/p[3]", "enniatin B concentration"),
    "native_growth": ("/article/body/sec[3]/sec[5]/p", "FgLH03"),
    "yeast_chemical_provenance": ("/article/body/sec[2]/sec[10]/p[1]", "Enniatin B"),
    "native_chemical_provenance": ("/article/body/sec[2]/sec[10]/p[2]", "enniatin A1"),
    "export_chemical_provenance": ("/article/body/sec[2]/sec[12]/p[1]", "enniatin B"),
    "earlier_MIC_studies": ("/article/body/sec[4]/p[5]", "minimum inhibitory concentration"),
    "induction_caption": ("/article/floats-group/fig[3]/caption", "enniatin B1"),
    "yeast_caption": ("/article/floats-group/fig[4]/caption", "enniatin B1"),
    "native_caption": ("/article/floats-group/fig[5]/caption", "enniatin A1"),
}


def primary_context(payload):
    if hashlib.sha256(payload).hexdigest() != ARTICLE_SHA:
        raise ValueError("reviewed primary article changed")
    tree = etree.fromstring(payload, parser=etree.XMLParser(resolve_entities=False, no_network=True))
    ids = {n.get("pub-id-type"): n.text for n in tree.xpath("./front/article-meta/article-id")}
    if (
        tree.get("article-type") != "research-article"
        or ids.get("pmid") != "42506285"
        or ids.get("pmcid") != "PMC13412724"
        or ids.get("doi") != DOI
    ):
        raise ValueError("primary identity changed")
    locations = {}
    for key, (xpath, marker) in LOCATIONS.items():
        nodes = tree.xpath(xpath)
        if len(nodes) != 1:
            raise ValueError("reviewed primary location absent or ambiguous")
        value = " ".join("".join(nodes[0].itertext()).split())
        if marker not in value:
            raise ValueError("reviewed primary context changed: " + key)
        locations[key] = {
            "xpath": xpath,
            "normalized_text_sha256": hashlib.sha256(value.encode()).hexdigest(),
        }
    return {
        "reference": "PMID:42506285",
        "doi": "DOI:" + DOI,
        "review_scope": "SELECTED_PRIMARY_TEXT_AND_CAPTIONS",
        "locations": locations,
        "figures_visually_reviewed": False,
        "supplements_reviewed": False,
        "source_gene": "FgABCB8",
        "source_locus": "FGSG_08823",
        "source_alias": "FGRAMPH1_01G10921",
        "discordant_source_label": "FGRAMPH1_01G010921",
        "discordant_label_silently_corrected": False,
        "chemical_context": {
            "enniatin_A1_equated_to_enniatin_A": False,
            "enniatin_B1_equated_to_enniatin_B": False,
            "mixed_F_avenaceum_extract_induction_is_exact_compound_resistance": False,
            "native_growth_compounds": ["enniatin A1", "enniatin B", "enniatin B1"],
            "yeast_growth_results_and_caption_name": "enniatin B1",
            "yeast_growth_methods_name": "enniatin B",
            "yeast_growth_B_B1_discrepancy_resolved": False,
            "yeast_growth_results_caption_dose_unit_discrepancy_resolved": False,
            "export_assay_source_name": "enniatin B",
            "beauvericin_yeast_growth_context": True,
            "source_material_exact_structure_independently_verified": False,
        },
        "observations": {
            "evidence_types": [
                "FUNCTIONAL_EXPERIMENT",
                "TRANSCRIPT_RESPONSE",
                "EXTRACELLULAR_CHEMICAL_SIGNAL",
            ],
            "native_A1_B1_sensitivity_modifier_reported": True,
            "native_B_growth_inhibition_not_observed_in_reported_comparison": True,
            "native_B_negative_comparison_is_positive_resistant_allele_evidence": False,
            "heterologous_yeast_partial_growth_protection_reported": True,
            "heterologous_yeast_assay_is_native_fungal_resistance": False,
            "relative_supernatant_signal_supports_source_export_interpretation": True,
            "export_signal_establishes_growth_resistance_or_direct_transport_kinetics": False,
            "growth_endpoint": "RELATIVE_GROWTH_AUC",
            "endpoint_is_MIC": False,
            "earlier_cited_MICs_assigned_to_current_assays": False,
            "clinical_resistance_inferred": False,
            "numeric_AST_exported": False,
        },
        "record_dispositions": {
            "CHEBI:64651": "A1_NOT_A_NO_EXACT_A_RESISTANCE_ASSERTION",
            "CHEBI:64649": (
                "B_B1_CONFLICT_AND_NATIVE_NEGATIVE_GROWTH_COMPARISON_NO_RESISTANT_ALLELE_ASSIGNMENT"
            ),
            "CHEBI:3000": (
                "HETEROLOGOUS_BEAUVERICIN_CONTEXT_RETAINED_FIGURES_AND_EXACT_SUBJECT_CHEMISTRY_OPEN"
            ),
        },
    }


def discovery_context(rows):
    if len(rows) != 3 or {r.get("identifier") for r in rows} != set(RECORDS):
        raise ValueError("discovery cohort changed")
    output, union = {}, set()
    for row in rows:
        label, inchikey, count, selected = RECORDS[row["identifier"]]
        ids = row.get("candidate_ids", [])
        queries = row.get("queries", [])
        if (
            row.get("standard_inchi_key") != inchikey
            or len(ids) != len(set(ids))
            or len(ids) != count
            or len(queries) != 2
        ):
            raise ValueError("discovery identity or membership changed")
        canonical = None
        for index, query in enumerate(queries):
            expected = count if index == 0 or row["identifier"] == "CHEBI:3000" else 0
            entries = query.get("candidates", [])
            mapping = {r["source"] + ":" + r["id"]: r for r in entries}
            if (
                query.get("hit_count") != expected
                or len(entries) != expected
                or len(mapping) != expected
                or query.get("next_cursor") is not None
                or query.get("request", {}).get("status") != 200
                or (expected and set(mapping) != set(ids))
            ):
                raise ValueError("discovery request incomplete or membership changed")
            if index == 0:
                canonical = mapping
            elif expected and canonical != mapping:
                raise ValueError("duplicate discovery queries disagree")
        if ("MED:42506285" in canonical) != selected:
            raise ValueError("selected paper discovery provenance changed")
        if selected and (
            canonical["MED:42506285"].get("doi") != DOI
            or canonical["MED:42506285"].get("pmcid") != "PMC13412724"
        ):
            raise ValueError("selected paper identity changed")
        union.update(ids)
        output[row["identifier"]] = {
            "label": label,
            "candidate_identities": count,
            "retained_candidate_ids": sorted(ids),
            "complete_queries": 2,
            "selected_paper_in_initial_candidates": selected,
            "selected_paper_assessed_via_related_record_lead": not selected,
        }
    return {
        "records": output,
        "distinct_candidate_identities": len(union),
        "record_candidate_memberships": sum(len(r["candidate_ids"]) for r in rows),
        "distinct_primary_text_reviews_this_pass": 1,
        "initial_candidates_without_primary_text_review_this_pass": len(union) - 1,
        "duplicate_memberships_are_independent_biological_evidence": False,
    }


def complete_query(payload, headers, count):
    headers = {k.lower(): v for k, v in headers.items()}
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("results"), list)
        or len(payload["results"]) != count
        or headers.get("x-total-results") != str(count)
        or headers.get("link")
        or headers.get("x-uniprot-release") != "2026_03"
    ):
        raise ValueError("reference query incomplete or changed")
    return payload["results"]


def organism_context(taxa):
    expected = {"5518": ("Gibberella zeae", "species"), "4932": ("Saccharomyces cerevisiae", "species")}
    for key, (name, rank) in expected.items():
        taxon = taxa[key]
        if (
            lineages.identity(taxon) != {"taxonId": int(key), "scientificName": name, "rank": rank}
            or taxon.get("active") is not True
        ):
            raise ValueError("organism taxonomy identity changed")
    if "Fusarium graminearum" not in taxa["5518"].get("synonyms", []):
        raise ValueError("source fungus name lacks explicit taxonomy synonym")
    return {
        "native_fungus_and_gene_donor": {
            "source_name": "Fusarium graminearum",
            "taxonomy_scientific_name": "Gibberella zeae",
            "taxon_id": "NCBITaxon:5518",
            "rank": "species",
            "name_relation": "EXPLICIT_SYNONYM",
            "source_background_label": "FgLH03",
            "strain_taxon_id": None,
            "assembly_accession": None,
        },
        "heterologous_assay_host": {
            "source_name": "Saccharomyces cerevisiae",
            "taxon_id": "NCBITaxon:4932",
            "rank": "species",
            "source_background_label": "AD12345678",
            "strain_taxon_id": None,
            "assembly_accession": None,
            "export_methods_source_host_label": "AD1-8",
            "exact_export_and_growth_derivative_equivalence_independently_verified": False,
        },
        "reference_PH1_or_S288c_assigned_to_tested_subjects": False,
        "species_wide_resistance_inferred": False,
    }


def project_reference(entry, taxon, *, expanded):
    if (
        entry.get("primaryAccession") != "I1RWY3"
        or entry.get("entryType") != "UniProtKB unreviewed (TrEMBL)"
        or entry.get("entryAudit") != {"entryVersion": 82, "sequenceVersion": 1}
        or {"sequence", "features", "comments"}.intersection(entry)
    ):
        raise ValueError("reference identity or payload scope changed")
    name = "Gibberella zeae (strain ATCC MYA-4620 / CBS 123657 / FGSC 9075 / NRRL 31084 / PH-1)"
    _, species = lineages.lineage(taxon)
    if (
        lineages.identity(taxon) != {"taxonId": 229533, "rank": "strain", "scientificName": name}
        or entry["organism"].get("taxonId") != 229533
        or entry["organism"].get("scientificName") != name
        or species != {"taxonId": 5518, "rank": "species", "scientificName": "Gibberella zeae"}
    ):
        raise ValueError("reference organism context changed")
    genes = entry.get("genes", [])
    if (
        len(genes) != 1
        or any(k in genes[0] for k in ("geneName", "synonyms", "orderedLocusNames"))
        or [n["value"] for n in genes[0].get("orfNames", [])] != ["FGRAMPH1_01T10921"]
    ):
        raise ValueError("reference ORF name changed")
    names = [n["fullName"]["value"] for n in entry["proteinDescription"].get("submissionNames", [])]
    if names != ["Chromosome 2, complete genome"]:
        raise ValueError("reference submission name changed")
    crossrefs = entry.get("uniProtKBCrossReferences")
    expected = (
        [
            {
                "database": "EMBL",
                "id": "HG970333",
                "properties": [
                    {"key": "ProteinId", "value": "CEF77263.1"},
                    {"key": "Status", "value": "-"},
                    {"key": "MoleculeType", "value": "Genomic_DNA"},
                ],
            },
            {
                "database": "VEuPathDB",
                "id": "FungiDB:FGRAMPH1_01G10921",
                "properties": [{"key": "Description", "value": "-"}],
            },
        ]
        if expanded
        else []
    )
    if crossrefs != expected:
        raise ValueError("literal native gene cross-reference changed")
    pmids = sorted(
        {
            i["id"]
            for r in entry.get("references", [])
            for i in r.get("citation", {}).get("citationCrossReferences", [])
            if i.get("database") == "PubMed"
        }
    )
    if pmids != ["17823352", "20237561", "26198851"]:
        raise ValueError("reference bibliography changed")
    return {
        "protein_accession": "UniProtKB:I1RWY3",
        "reviewed": False,
        "release": "2026_03",
        "entry_version": 82,
        "sequence_version": 1,
        "native_ORF_name": "FGRAMPH1_01T10921",
        "native_submission_name": names[0],
        "reference_taxon_id": "NCBITaxon:229533",
        "reference_taxon_rank": "strain",
        "reference_taxon_name": name,
        "reference_species_taxon_id": "NCBITaxon:5518",
        "selected_primary_pmid_in_bibliography": False,
        "bibliography_PMIDs": ["PMID:" + p for p in pmids],
        "explicit_source_locus_crosswalk": "FungiDB:FGRAMPH1_01G10921" if expanded else None,
        "source_FGSG_alias_basis": "PRIMARY_RESULTS_3_2_PARAGRAPH_2" if expanded else None,
        "crosswalk_basis": "NATIVE_VEUPATHDB_CROSS_REFERENCE" if expanded else "UNRESOLVED_SEARCH_HIT",
        "reference_EMBL_nucleotide_accession": "HG970333" if expanded else None,
        "reference_EMBL_protein_accession": "CEF77263.1" if expanded else None,
        "native_crossref_gene_label_inferred_by_G_to_T_replacement": False,
        "extra_zero_source_label_equivalence_established": False,
        "reference_accessions_assigned_to_experimental_subject": False,
        "exact_resistance_allele": False,
        "experimental_genome_assignment": None,
    }


def build(root, directory=CACHE):
    directory = root / directory
    keys = {"article-2026"} | set(QUERIES)
    if any(
        {p.name.removesuffix(s) for p in directory.glob("*" + s)} != keys
        for s in ("-receipt.json", "-attempt.json")
    ):
        raise ValueError("research request coverage changed")
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen enniatin cohort changed")
    cohort = json.loads(cohort_path.read_bytes())
    protected = json.loads(reference.check_pin(root, cohort["protected"]).read_bytes())
    reference.check_pin(root, cohort["source_queue"])
    with reference.check_pin(root, cohort["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or any(protected.get(r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("complete corpus preflight changed")
    discovery = json.loads(gzip.decompress(reference.check_pin(root, cohort["discovery"]).read_bytes()))
    rows = [r for r in discovery["records"] if r["identifier"] in RECORDS]
    if rows != cohort["discovery_records"]:
        raise ValueError("discovery cohort provenance changed")
    discovery_result = discovery_context(rows)
    if len(cohort["records"]) != 3 or {r["identifier"] for r in cohort["records"]} != set(RECORDS):
        raise ValueError("historical record membership changed")
    for row in cohort["records"]:
        record = load_record(reference.check_pin(root, row["snapshot"]))
        if (
            record["identifier"] != row["identifier"]
            or record["label"] != row["label"]
            or record["chemical_structure"]["standard_inchi_key"] != RECORDS[row["identifier"]][1]
            or row["snapshot"]["sha256"] != row["sha256"]
            or protected.get(row["path"]) != row["sha256"]
            or record.get("resistance_mechanisms")
        ):
            raise ValueError("historical compound identity changed")
    sources = {"article-2026": planned_source(root, directory, "article-2026", "request-plan.json", ARTICLE)}
    primary = primary_context(reference.check_pin(root, sources["article-2026"]["body"]).read_bytes())
    query_rows = {}
    for key, (query, plan, count, fields) in QUERIES.items():
        url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
            {"query": query, "format": "json", "size": "500", "fields": fields}
        )
        sources[key] = planned_source(root, directory, key, plan, url)
        receipt = json.loads(reference.check_pin(root, sources[key]["receipt"]).read_bytes())
        payload = json.loads(reference.check_pin(root, sources[key]["body"]).read_bytes())
        query_rows[key] = complete_query(payload, receipt["headers"], count)
    plans = {k: json.loads(reference.check_pin(root, v["plan"]).read_bytes()) for k, v in sources.items()}
    if any(p.get("cohort") != reference.pin(root, cohort_path) for p in plans.values()):
        raise ValueError("request cohort binding changed")
    review_pin = reference.pin(root, directory / "article-reviewed.json")
    review = json.loads(reference.check_pin(root, review_pin).read_bytes())
    if (
        review.get("source") != {k: sources["article-2026"][k] for k in ("body", "receipt")}
        or review.get("source_locus") != primary["source_locus"]
        or review.get("figures_visually_reviewed") is not False
        or review.get("supplements_reviewed") is not False
    ):
        raise ValueError("primary review binding changed")
    for key in QUERIES:
        if plans[key].get("canary_review" if key == "reference-locus" else "primary_review") != review_pin:
            raise ValueError("primary review plan binding changed")
    if (
        plans["reference-alternatives"].get("completed_first_locus_query")
        != sources["reference-locus"]["receipt"]
        or any(
            plans[k].get("provider_similar_locus_suggestions_followed") is not False
            for k in QUERIES
            if k != "reference-locus"
        )
        or plans["reference-crossreferences"].get("completed_exact_locus_queries")
        != [sources[k]["receipt"] for k in ("reference-locus", "reference-alternatives")]
        or plans["reference-candidate"].get("candidate_discovery_receipt")
        != sources["reference-crossreferences"]["receipt"]
    ):
        raise ValueError("query expansion provenance changed")
    config = json.loads(reference.check_pin(root, CONFIG).read_bytes())
    if (
        config.get("status") != 200
        or config.get("url") != "https://rest.uniprot.org/configure/uniprotkb/result-fields"
        or hashlib.sha256(config["body"].encode()).hexdigest() != config["sha256"]
        or any(
            plans[k].get("result_fields_configuration") != CONFIG
            for k in ("reference-crossreferences", "reference-candidate")
        )
    ):
        raise ValueError("result field configuration provenance changed")
    supported = {f["name"] for g in json.loads(config["body"]) for f in g.get("fields", [])}
    if not {"xref_ensemblfungi", "xref_embl", "xref_geneid", "xref_veupathdb"} <= supported:
        raise ValueError("requested cross-reference fields unsupported")
    taxa, taxonomy_sources = {}, {}
    for taxid, item in TAXONOMY.items():
        taxa[taxid], taxonomy_sources[taxid] = lineages.native_taxon(
            root, {"receipt": item, "body": None}, taxid, "2026_03"
        )
    organisms = organism_context(taxa)
    initial_reference = project_reference(
        query_rows["reference-crossreferences"][0], taxa["229533"], expanded=False
    )
    grounded = project_reference(query_rows["reference-candidate"][0], taxa["229533"], expanded=True)
    previous = "research/2026-10-14-beauvericin-reference-context.json"
    previous_pin = {"path": previous, "sha256": protected[previous]}
    reference.check_pin(root, previous_pin)
    return {
        "date": "2026-10-14",
        "scope": "PRIMARY_CONTEXT_AND_REFERENCE_CROSSWALK_NOT_ALLELE_CURATION",
        "cohort": reference.pin(root, cohort_path),
        "baseline_commit": cohort["baseline_commit"],
        "census": cohort["census"],
        "corpus_records_hash_checked_at_preflight": len(census),
        "records": cohort["records"],
        "discovery": discovery_result,
        "primary_context": primary,
        "primary_review": review_pin,
        "sources": sources,
        "organism_context": organisms,
        "taxonomy_sources": taxonomy_sources,
        "reference_candidate_before_expanded_crossrefs": initial_reference,
        "grounded_reference": grounded,
        "result_fields_configuration": CONFIG,
        "query_interpretation": {
            "complete_exact_gene_queries": 2,
            "exact_gene_query_result_counts": [0, 0],
            "broader_literal_label_query_result_count": 1,
            "accession_crossreference_query_result_count": 1,
            "provider_spelling_suggestions_followed": False,
            "empty_gene_queries_establish_gene_or_protein_absence": False,
            "broader_search_hit_alone_establishes_crosswalk": False,
            "empty_selected_EnsemblFungi_field_establishes_all_crossref_absence": False,
        },
        "previous_beauvericin_primary_hold_checkpoint": previous_pin,
        "curation_decision": "RETAIN_RESEARCH_CONTEXT_NO_NEW_RESISTANCE_ASSERTION",
        "limits": {
            "scientific_http_attempts": 5,
            "native_taxonomy_responses_reused": 3,
            "native_result_field_configuration_reused": 1,
            "new_uniprot_requests": 4,
            "ncbi_requests": 0,
            "ncbi_contact": 0,
            "retries": 0,
            "automatic_redirects": 0,
            "biological_records_changed": 0,
            "new_resistance_assertions": 0,
            "reference_mappings_grounded": 1,
            "experimental_allele_assignments": 0,
            "prior_source_holds_preserved": True,
            "source_adoptions": 0,
            "numeric_AST_variants_sequences_constructs_or_protocols_exported": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "whole_record_primary_review": "OPEN",
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": [
            {"source": "Harris et al. 2026, Journal of Fungi", "doi": "DOI:" + DOI, "license": "CC BY 4.0"},
            {"source": "UniProt Consortium", "release": "2026_03", "license": "CC BY 4.0"},
            {"source": "Europe PMC", "scope": "bibliographic discovery and primary XML delivery"},
            {
                "source": "VEuPathDB/FungiDB",
                "scope": (
                    "cross-reference annotation carried by UniProt; no direct request or source adoption"
                ),
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
            raise SystemExit("Enniatin checkpoint does not reproduce")
    else:
        with OUTPUT.open("xb") as stream:
            stream.write(payload)
    print(
        json.dumps(
            {
                "distinct_records": 3,
                "primary_text_reviews": 1,
                "reference_mappings": 1,
                "new_resistance_assertions": 0,
            }
        )
    )


if __name__ == "__main__":
    main()

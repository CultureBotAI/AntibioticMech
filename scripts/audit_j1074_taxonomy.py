"""Reconcile a published host lineage at species rank, not derivative-genome rank."""

import argparse
import copy
import csv
import hashlib
import io
import json
from pathlib import Path

import audit_caspofungin_context as native_context
import audit_topoisomerase_references as reference
from lxml import etree

CACHE = Path("reports/resistance-grounding-2026-10-14-j1074")
OUTPUT = Path("research/2026-10-14-j1074-taxonomy.json")
ENA_FIELDS = ("accession,sequence_version,description,tax_id,scientific_name,strain,study_accession,"
              "sample_accession,first_public,last_updated")
ENA_URL = (
    "https://www.ebi.ac.uk/ena/portal/api/search?result=sequence&query=accession%3D%22CP004370%22"
    "&fields=accession%2Csequence_version%2Cdescription%2Ctax_id%2Cscientific_name%2Cstrain"
    "%2Cstudy_accession%2Csample_accession%2Cfirst_public%2Clast_updated&format=json&limit=10"
)
TAXONOMY_URL = (
    "https://rest.uniprot.org/taxonomy/search?query=%22Streptomyces%20albidoflavus%22&format=json&size=100"
)
PINS = {
    "genome-primary": "fcfe7f720e9a38e50f9bba49a0812605bca71749c3d1963ef0eb4449e093a634",
    "modern-name-primary": "35e3f095e21636e8dd1183db805e56c80fbc29e93b5eec9b0fead299d7766c50",
    "albidoflavus-taxonomy": "326e8088ba2a466e57286218707a53377e604c76030e3fa55754401272d517a7",
    "ena-chromosome-metadata": "ca0ecfa55b6b28a6407ba0d2e30d68637a6b321fcd2bcaed4a48b4f712684e11",
}
SPECIES = {"taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus"}
MEMBERS = {"CHEBI:68241": ["ptmP3", "fabF"], "CHEBI:68236": ["ptmP3", "fabF"],
           "CHEBI:78661": ["borO"]}


def grounded_claims(identifier, claims):
    """Only upgrade the verified species context of the five existing claims."""
    if identifier not in MEMBERS or [c.get("gene_families") for c in claims] != [
        [gene] for gene in MEMBERS[identifier]
    ]:
        raise ValueError("curation cohort or gene scope changed")
    expected_pmid = "PMID:15112998" if identifier == "CHEBI:78661" else "PMID:24560608"
    result = copy.deepcopy(claims)
    for old, claim in zip(claims, result, strict=True):
        if (old.get("taxon_label") != "Streptomyces albus" or old.get("taxon_id")
                or any(old.get(k) for k in ("protein_accession", "strain_taxon_id", "source"))
                or expected_pmid not in {e["reference"] for e in old["evidence"]}
                or "J1074" not in old["note"] or "Streptomyces albus" not in old["label"]):
            raise ValueError("source host or claim scope changed")
        claim.update(SPECIES)
        claim["label"] = old["label"].replace("Streptomyces albus", SPECIES["taxon_label"])
        claim["note"] += (
            " Species-grounding update (2026-10-14): the source-reported J1074 host lineage is grounded "
            "to Streptomyces albidoflavus (NCBITaxon:1886), using the published J1074 background "
            "chromosome CP004370.1 and its ENA taxonomic metadata, with agreeing UniProt species rank "
            "and name. The preceding NCBITaxon:1888 and J1074 name-search statements retain historical "
            "reference context, not the current species assignment. This is species-level lineage "
            "grounding, not resequencing or exact identity validation of the tested derivative. "
            "CP004370.1 and its associated sample and study remain background references only; no "
            "experimental genome, sample, strain TaxID or protein allele is assigned. Donor references "
            "and the original phenotype and mechanism limitations remain unchanged."
        )
        claim["evidence"] += [
            {"reference": "PMID:24495463", "notes":
             "Host-lineage context only: Establishing strain ancestry distinguishes J1074 from its "
             "S. albus G ancestor; Sequence accession id reports CP004370 for the J1074 background. "
             "This genome paper is not evidence for the resistance-study derivatives' exact genomes."},
            {"reference": ENA_URL, "notes":
             "Sequence-free accession metadata retrieved 2026-10-14: CP004370, sequence version 1, "
             "strain J1074, organism Streptomyces albidoflavus, TaxID 1886; metadata last updated "
             "2018-11-09. Used for species-level host-lineage grounding, not derivative genome or "
             "sample assignment. Native response and request are pinned in the J1074 research dossier."},
            {"reference": TAXONOMY_URL, "notes":
             "UniProt release 2026_03, retrieved 2026-10-14: the unique exact-name result for "
             "Streptomyces albidoflavus is active species NCBITaxon:1886. The species-group and "
             "Streptomyces limosus results are not substitutes; no strain node is selected."},
        ]
    return result


def project_background(rows, taxa):
    fields = set(ENA_FIELDS.split(","))
    if len(rows) != 1 or set(rows[0]) != fields:
        raise ValueError("background chromosome metadata missing, duplicated or unexpectedly expanded")
    row = rows[0]
    expected = {"accession": "CP004370", "sequence_version": "1", "tax_id": "1886",
                "scientific_name": "Streptomyces albidoflavus", "strain": "J1074",
                "description": "Streptomyces albidoflavus strain J1074, complete genome.",
                "study_accession": "PRJNA180996", "sample_accession": "SAMN02603310",
                "first_public": "2013-04-10", "last_updated": "2018-11-09"}
    if row != expected:
        raise ValueError("published chromosome identity or metadata changed")
    species = [t for t in taxa if t.get("scientificName") == row["scientific_name"]]
    if (len(species) != 1 or species[0].get("taxonId") != 1886
            or species[0].get("rank") != "species" or species[0].get("active") is not True):
        raise ValueError("ENA organism lacks unique active UniProt species agreement")
    return {
        "source_background_name": "Streptomyces albus J1074", "background_strain": "J1074",
        "current_species": SPECIES, "species_rank": "species", "background_chromosome": "CP004370.1",
        "background_study": row["study_accession"], "background_sample": row["sample_accession"],
        "first_public": row["first_public"], "metadata_last_updated": row["last_updated"],
        "assignment_scope": "SPECIES_LEVEL_HOST_LINEAGE_NOT_EXACT_DERIVATIVE_IDENTITY",
        "experimental_genome_assignment": None, "experimental_sample_assignment": None,
        "experimental_strain_taxon_assignment": None, "experimental_allele_assignment": None,
        "chromosome_is_assembly_accession": False, "resistance_inferred_from_chromosome": False,
    }


def primary_locations(payload, modern=False):
    key = "modern-name-primary" if modern else "genome-primary"
    if hashlib.sha256(payload).hexdigest() != PINS[key]:
        raise ValueError("reviewed primary article changed")
    tree = etree.fromstring(payload)
    expected_doi = "10.1093/nar/gkae1236" if modern else "10.1186/1471-2164-15-97"
    if tree.xpath('/article/front/article-meta/article-id[@pub-id-type="doi"]/text()') != [expected_doi]:
        raise ValueError("article identity mismatch")
    selectors = ({"later_name_usage": '//body//p[contains(., "previously Streptomyces albus J1074")]'}
                 if modern else {
                     "ancestry": '//sec[title="Establishing strain ancestry"]/p',
                     "accession": '//sec[title="Sequence accession id"]/p',
                 })
    locations = {}
    for name, selector in selectors.items():
        nodes = tree.xpath(selector)
        if len(nodes) != 1:
            raise ValueError("primary identity location missing or ambiguous")
        text = " ".join(" ".join(nodes[0].itertext()).split())
        locations[name] = {"xpath": tree.getroottree().getpath(nodes[0]),
                           "text_sha256": hashlib.sha256(text.encode()).hexdigest()}
    return {"doi": "DOI:" + expected_doi, "locations": locations,
            "whole_article_or_supplements_reviewed": False,
            "scope": "HOST_NAME_AND_LINEAGE_ONLY_NOT_NEW_RESISTANCE_EVIDENCE"}


def build(root, directory):
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for item in [cohort[k] for k in ("census", "protected", "source_queue", "taxonomy_reuse")]:
        reference.check_pin(root, item)
    prior = [json.loads(reference.check_pin(root, p).read_bytes()) for p in cohort["prior"]]
    sources = {}
    urls = {
        "genome-primary": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3937824/fullTextXML",
        "modern-name-primary": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11754652/fullTextXML",
        "albidoflavus-taxonomy": TAXONOMY_URL, "ena-chromosome-metadata": ENA_URL,
    }
    for key, url in urls.items():
        sources[key] = native_context.native(root, directory, key, url)
        if sources[key]["body"]["sha256"] != PINS[key]:
            raise ValueError("inspected source payload changed")
    taxa, taxonomy_source = reference.read_response(root, directory, "albidoflavus-taxonomy",
                                                    "/taxonomy/search", {
                                                        "query": ['"Streptomyces albidoflavus"'],
                                                        "format": ["json"], "size": ["100"],
                                                    })
    rows = json.loads(reference.check_pin(root, sources["ena-chromosome-metadata"]["body"]).read_bytes())
    grounding = project_background(rows, taxa["results"])
    definitions = {}
    for kind in ("return", "search"):
        key = f"ena-sequence-{kind}-fields"
        source = native_context.native(root, directory, key,
                                       f"https://www.ebi.ac.uk/ena/portal/api/{kind}Fields?result=sequence&format=tsv")
        table = list(csv.DictReader(io.StringIO(reference.check_pin(root, source["body"])
                                               .read_text()), delimiter="\t"))
        required = ENA_FIELDS.split(",") if kind == "return" else ["accession"]
        selected = [r for r in table if r["columnId"] in required]
        if len(selected) != len(required) or {r["columnId"] for r in selected} != set(required):
            raise ValueError("ENA metadata field definitions changed")
        definitions[kind] = {"source": source, "selected_definitions": selected}
    old = prior[0]["host_taxonomy_search"]
    if old != prior[1]["host_taxonomy_search"] or {r["taxonId"] for r in old["candidates"]} != {
        457425, 1962, 3466461,
    }:
        raise ValueError("historical host candidates changed")
    focal = {}
    for dossier, pmid, image in (
        (prior[0], "15112998", "reports/resistance-grounding-2026-10-09-borrelidin/olano2004-page-6.png"),
        (prior[1], "24560608", "reports/resistance-grounding-2026-10-09-platen/peterson2014-page-17.png"),
    ):
        paper = dossier["primary_papers"][pmid]
        request = paper["primary_request"]
        pdf = {"path": request["cache_path"], "sha256": request["sha256"]}
        reference.check_pin(root, pdf)
        if paper["host_background"] != "Streptomyces albus J1074":
            raise ValueError("resistance-paper host lineage changed")
        focal[pmid] = {"doi": "DOI:" + paper["doi"], "host_background": paper["host_background"],
                       "primary_pdf": pdf,
                       "selected_page_visually_reinspected": reference.pin(root, root / image),
                       "whole_paper_or_supplement_review": False}
    return {
        "schema_version": 1, "scope": "HOST_SPECIES_GROUNDING_NOT_ALLELE_OR_DERIVATIVE_GENOME_ASSIGNMENT",
        "records_before": cohort["records"], "prior_checkpoints": cohort["prior"],
        "census_before": cohort["census"], "sources": sources, "ena_field_definitions": definitions,
        "taxonomy_release": taxonomy_source["release"], "grounding": grounding,
        "primary": {key: primary_locations(reference.check_pin(root, sources[key]["body"]).read_bytes(),
                                           modern=(key == "modern-name-primary"))
                    for key in ("genome-primary", "modern-name-primary")},
        "resistance_paper_host_evidence": focal,
        "historical_name_search": old,
        "historical_name_candidates_selected_as_experimental_taxa": [],
        "modern_name_is_formal_taxonomic_reclassification_study": False,
        "donor_reference_proteins_preserved": ["UniProtKB:D8L2W8", "UniProtKB:Q70HZ0"],
        "host_taxonomy_is_donor_taxonomy": False,
        "curation_scope": {"existing_claims": 5, "records": 3, "new_resistance_claims": 0,
                           "supported_species": SPECIES, "whole_record_primary_signoffs": 0,
                           "full_corpus_records_in_scope": 2939},
        "limits": {"ncbi_requests": 0, "issue_1040": "DEFERRED", "source_adoptions": 0,
                   "numeric_AST_or_sequence_exported": False, "protocols_or_constructs_exported": False,
                   "background_genome_proves_experimental_genotype": False,
                   "no_hit_name_query_proves_biological_absence": False},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = build(args.root, args.root / CACHE)
    target = args.root / OUTPUT
    payload = (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode()
    if target.exists() and target.read_bytes() != payload:
        raise ValueError("historical checkpoint differs")
    if not target.exists():
        target.write_bytes(payload)
    print(json.dumps(result["grounding"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Keep primary context, reference identities and experimental assignments distinct."""

import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-transport-followup-context.json").read_bytes())


def test_full_scope_and_historical_inputs_remain_explicit(dossier):
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 19, "primary_papers": 4,
        "reference_proteins": 2, "whole_records_completed": 0, "full_corpus_primary_review": "OPEN",
    }
    for source in dossier["inputs"].values():
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
    preservation = dossier["preservation"]
    assert preservation["record_hashes_verified"] == 2939
    assert preservation["biological_record_changes"] == preservation["curation_events_added"] == 0
    assert preservation["ignored_files_included"] is True
    assert preservation["protected_baseline_files"] == 6736


def test_all_selected_records_have_scoped_dispositions(dossier):
    assert len({r["identifier"] for r in dossier["records"]}) == 19
    for row in dossier["records"]:
        record = load_record(ROOT / row["path"])
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        assert row["whole_record_review"] == "OPEN"
        assert row["exact_experimental_assignment"] is False
        assert row["record_action"] == "PRESERVE_RECORD_NO_NEW_BIOLOGICAL_CLAIM"
        assert all(p.removeprefix("PMID:") in dossier["primary_papers"] for p in row["paper_contexts"])
    assert Counter(r["decision"] for r in dossier["records"]) == {
        "HOLD_ACTIVE_MATERIAL_STEREOCHEMISTRY_NOT_DERIVATIVE_IDENTITY": 1,
        "NO_MIXTURE_TO_SINGLE_STRUCTURE_OR_CONGENER_PROPAGATION": 11,
        "HOLD_EXACT_COMPOUND_AND_EXPERIMENTAL_REFERENCE_ASSIGNMENT": 2,
        "NO_C_D_GENE_ASSOCIATION_PROPAGATION_TO_OTHER_CONGENERS": 5,
    }


@pytest.mark.parametrize("accession,entry,seq,taxon,parent", [
    ("J9VUL5", 40, 1, 235443, 5207), ("Q59Q40", 90, 1, 237561, 5476),
])
def test_reference_proteins_and_taxonomy_are_not_tested_alleles(
    dossier, accession, entry, seq, taxon, parent,
):
    protein = dossier["proteins"][accession]
    assert protein["entry_audit"] == {"entryVersion": entry, "sequenceVersion": seq}
    assert protein["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["organism"]["taxonId"] == taxon
    assert protein["focal_citation_present"] is False
    assert protein["experimental_assignment"] is False
    assert protein["scope"] == "REFERENCE_METADATA_NOT_EXACT_EXPERIMENTAL_ALLELE"
    tax = dossier["taxonomy"][str(taxon)]
    assert tax["rank"] == "strain" and tax["active"] is True
    assert tax["parent"]["taxonId"] == parent
    assert tax["parent_rank_from_lineage"] == "species"


def test_explicit_locus_and_name_based_reference_are_different(dossier):
    rta1 = dossier["proteins"]["J9VUL5"]
    rta2 = dossier["proteins"]["Q59Q40"]
    assert rta1["grounding_basis"] == "PRIMARY_EXPLICIT_LOCUS_TO_UNIPROT_REFERENCE"
    assert rta2["grounding_basis"] == "GENE_NAME_AND_REFERENCE_STRAIN_NOT_EXPLICIT_PRIMARY_LOCUS_CROSSWALK"
    assert dossier["primary_papers"]["36364991"]["explicit_locus"] == "CNAG_03091"
    for protein, archive_id, protein_id in [(rta1, "CP003827", "AFR96314.1"),
                                           (rta2, "CP017624", "AOW27651.1")]:
        archive, = protein["archive_references"]
        assert archive["id"] == archive_id
        assert {"key": "ProteinId", "value": protein_id} in archive["properties"]


def test_derivatives_and_formula_discrepancy_do_not_resolve_stereochemistry(dossier):
    paper = dossier["primary_papers"]["36364991"]
    crystal = paper["crystal_context"]
    assert crystal["entity"] == "IMINE_DERIVATIVE_NOT_UNMODIFIED_7_AMINOCHOLESTEROL"
    assert crystal["table_s2_formula_verbatim"] == "C30H57NO"
    assert crystal["cif_formula_moiety_verbatim"] == "C30 H57 N1 O1"
    assert crystal["cif_formula_sum_verbatim"] == "C30 H51 N1 O1"
    assert crystal["discrepancy"] == "SUPPLEMENT_FORMULAS_DISAGREE_NOT_SILENTLY_CORRECTED"
    record, = [r for r in dossier["records"] if r["identifier"] == "CHEBI:77845"]
    assert record["chemical_scope"] == "C7_UNSPECIFIED_IN_CURRENT_RECORD"
    assert "Figure S8 (supplement page 8)" in paper["figures_visually_inspected"]
    assert "Table S2 (supplement page 10)" in paper["figures_visually_inspected"]


def test_rta2_lead_is_relevant_but_strain_conflict_unresolved(dossier):
    paper = dossier["primary_papers"]["26518191"]
    assert paper["subject_conflict"] == {
        "methods_reconstituted_strain": "SLP15", "table_1_reconstituted_strain": "SLP5",
        "decision": "CONFLICT_RETAINED_NO_EXPERIMENTAL_STRAIN_ASSIGNMENT",
    }
    assert paper["figures_visually_inspected"] == ["Figure 2"]
    assert paper["curation_decision"] == "HOLD_COMPOUND_IDENTITY_AND_CONFLICTING_STRAIN_LABELS"
    record, = [r for r in dossier["records"] if r["identifier"] == "CHEBI:77845"]
    assert "PMID:26518191" in record["paper_contexts"]


def test_mic80_molar_endpoint_is_not_generic_mic_mass_concentration(dossier):
    paper = dossier["primary_papers"]["26518191"]
    assay = paper["measurement_scope"]
    assert "tested lot composition is not established" in paper["chemical_limits"]
    assert assay["endpoint"] == "MIC80"
    assert assay["original_unit"] == "micromolar"
    assert assay["standard_mass_unit_conversion"] == "NOT_PERFORMED_UNSPECIFIED_MIXTURE"
    assert assay["growth_images_are_mic_values"] is False
    generic, = [r for r in dossier["records"] if r["label"] == "tunicamycin"]
    assert generic["chemical_scope"] == "GENERIC_NAME_RECORD_STILL_HAS_ONE_STRUCTURE"
    congeners = [r for r in dossier["records"]
                 if r["chemical_scope"] == "EXACT_CONGENER_NOT_IDENTIFIED_IN_PAPER"]
    assert len(congeners) == 10


def test_cervimycin_c_d_and_other_congeners_are_not_interchangeable(dossier):
    records = {r["label"]: r for r in dossier["records"]}
    assert records["cervimycin C"]["chemical_scope"] == "NAMED_C_PRIMARY_CONTEXT"
    assert records["cervimycin D"]["chemical_scope"] == "D_COMPARISON_NOT_ALL_C_MECHANISTIC_EXPERIMENTS"
    for suffix in ("A", "B", "K1", "K2", "N"):
        assert records["cervimycin " + suffix]["chemical_scope"] == (
            "RELATED_CONGENER_NOT_DIRECT_FOCAL_GENE_EVIDENCE"
        )
    assert "not independent" in dossier["primary_papers"]["38722162"]["duplicate_context"]
    assert "recU" in dossier["primary_papers"]["38722162"]["negative_context"]
    assert dossier["primary_papers"]["36173303"]["negative_comparison_gene"] == "dnaK"


def test_study_identifiers_are_not_per_isolate_genome_assignments(dossier):
    paper = dossier["primary_papers"]["36173303"]
    assert "methicillin-susceptible, not as an MRSA parent" in paper["subject_limit"]
    ids = {r["identifier"]: r["scope"] for r in paper["source_reported_identifiers"]}
    assert ids == {
        "RefSeq:NZ_CP076660.1": "SG511_BERLIN_REFERENCE_GENOME_NOT_EVERY_TESTED_ISOLATE",
        "GenBank:CP076660": "SG511_BERLIN_REFERENCE_CHROMOSOME",
        "BioProject:PRJNA852436": "STUDY_PROJECT_NOT_AN_ISOLATE_ASSEMBLY",
        "GEO:GSE206309": "STUDY_TRANSCRIPTOMICS_NOT_A_GENOME",
        "ProteomeXchange:PXD034970": "STUDY_PROTEOMICS_NOT_A_GENOME",
    }
    assert paper["exact_uniprot_assignment"] is None
    assert dossier["taxonomy"]["1280"]["rank"] == "species"


def test_empty_queries_do_not_establish_biological_absence(dossier):
    requests = dossier["uniprot_requests"]
    assert sorted(r["result_count"] for r in requests) == [0, 0, 1, 1]
    for request in requests:
        assert request["complete_for_query"] is True
        assert request["establishes_biological_absence"] is False
        assert request["release"] == "2026_03"
        assert urlsplit(request["url"]).hostname == "rest.uniprot.org"


def test_access_and_inspection_scope_are_not_overstated(dossier):
    papers = dossier["primary_papers"]
    assert all(p["relevant_primary_text_reviewed"] for p in papers.values())
    assert not any(p["whole_paper_review_complete"] for p in papers.values())
    assert papers["26518191"]["isOpenAccess"] == "N"
    assert papers["26518191"]["review_medium"] == "PUBLISHER_FREE_ARTICLE_HTML_NOT_OA_XML_SLICE"
    for pmid in ("36364991", "36173303", "38722162"):
        assert papers[pmid]["isOpenAccess"] == "Y"
        assert urlsplit(papers[pmid]["primary_request"]["url"]).hostname == "www.ebi.ac.uk"
        assert papers[pmid]["primary_request"]["status"] == 200
    assert papers["36173303"]["supplement_pdf_visually_inspected"] is False
    assert papers["36173303"]["figures_visually_inspected"] == []
    assert papers["38722162"]["figures_visually_inspected"] == []
    access = dossier["access_limitations"]
    assert access["cervimycin2022_native_supplement"]["status"] == 403
    assert access["cervimycin2022_native_supplement_result"] == "HTTP_403_HTML_CHALLENGE_NOT_PDF"
    assert access["rta2_oa_xml_requested"] is False


def test_public_export_excludes_experimental_specs_and_signed_links(dossier):
    def walk(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from walk(child)
        elif isinstance(value, list):
            for child in value:
                yield from walk(child)

    assert not set(walk(dossier)) & {
        "sequence", "features", "variants", "alteration", "resistance_mechanisms",
        "activity_spectrum", "mic", "measurement_value", "protocol", "primers", "coordinates",
        "headers", "set-cookie", "Set-Cookie",
    }
    serialized = json.dumps(dossier)
    assert "Signature=" not in serialized and "Key-Pair-Id=" not in serialized
    figure = dossier["primary_papers"]["26518191"]["figure_request"]
    assert figure["signed_url_exported"] is False and "url" not in figure
    assert "No NCBI request" in " ".join(dossier["limitations"])
    assert all(p["numerical_ast_exported"] is False for p in dossier["primary_papers"].values())

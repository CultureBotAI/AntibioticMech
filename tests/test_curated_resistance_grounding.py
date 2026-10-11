"""Protect reviewed identifier scope without promoting associations to causation."""

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import emit_antibiotic_yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from seed_from_sources import merge_with_existing  # noqa: E402


def pyrisoxazole():
    return load_record(ROOT / "data/antibiotics/antifungal/pyrisoxazole.yaml")


def test_pyrisoxazole_does_not_combine_distinct_study_groups():
    claims = pyrisoxazole()["resistance_mechanisms"]
    substitutions = {c["alteration"]: c for c in claims if "alteration" in c}
    assert set(substitutions) == {"G476S and K104E", "M231T"}
    assert substitutions["M231T"]["strain"] == "RS10-1"
    assert substitutions["M231T"]["protein_accession"] == "UniProtKB:A0A7G4P320"
    assert "protein_accession" not in substitutions["G476S and K104E"]
    assert "strain" not in substitutions["G476S and K104E"]


def test_pyrisoxazole_retains_numbering_and_evidence_limitations():
    for claim in pyrisoxazole()["resistance_mechanisms"]:
        assert claim["taxon_id"] == "NCBITaxon:40559"
        assert claim["taxon_label"] == "Botrytis cinerea"
        assert "strain_taxon_id" not in claim
        assert "gene_id" not in claim
        if "alteration" in claim:
            assert "AY253234" in claim["note"]
            assert "not independent causal validation" in claim["note"]
        if "protein_accession" in claim:
            assert "unreviewed TrEMBL" in claim["note"]
            assert "MT430876/QMT30302.1" in claim["note"]
            assert {e["reference"] for e in claim["evidence"]} == {
                "PMID:32714305", "UniProtKB:A0A7G4P320",
            }


def test_grounded_curator_claims_survive_source_reseeding():
    existing = pyrisoxazole()
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    seeded.pop("molecular_targets")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def test_pyrisoxazole_crosswalk_is_citation_and_strain_specific():
    snapshot = json.loads((ROOT / "research/2026-10-07-pyrisoxazole-protein-crosswalk.json").read_text())
    claim = next(c for c in pyrisoxazole()["resistance_mechanisms"] if c.get("strain") == "RS10-1")
    accession = claim["protein_accession"].removeprefix("UniProtKB:")
    entry = snapshot["entries"][accession]
    assert entry["organism"]["taxonId"] == int(claim["taxon_id"].split(":")[1])
    assert entry["entryAudit"]["sequenceVersion"] == 1
    assert any(x["database"] == "EMBL" and x["id"] == "MT430876"
               for x in entry["uniProtKBCrossReferences"])
    assert any(r["citation"]["id"] == "32714305"
               and any(c["type"] == "STRAIN" and c["value"] == claim["strain"]
                       for c in r["referenceComments"])
               for r in entry["references"])


def cerulenin():
    return load_record(ROOT / "data/antibiotics/antifungal/cerulenin.yaml")


def fluorouracil():
    return load_record(ROOT / "data/antibiotics/antifungal/5-fluorouracil.yaml")


def test_fur1_cohorts_are_not_parent_strains_or_exact_alleles():
    doc = fluorouracil()
    claims = doc["resistance_mechanisms"]
    assert len(claims) == 2
    assert {c["label"] for c in claims} == {
        "FUR1-associated 5-fluorouracil resistance in LL13-040-derived cohort",
        "FUR1-associated 5-fluorouracil resistance in NC-02-derived cohort",
    }
    for claim in claims:
        assert claim["gene_id"] == "FUR1" and claim["gene_families"] == ["FUR1"]
        assert claim["taxon_id"] == "NCBITaxon:4932"
        assert claim["taxon_label"] == "Saccharomyces cerevisiae"
        assert "not allele-specific causality" in claim["note"]
        assert "resistance of the parental strain" in claim["note"]
        assert not {"strain", "alteration", "protein_accession", "strain_taxon_id"}.intersection(claim)
    assert doc["curation_status"] == "SEEDED"


def test_fur1_reference_and_growth_association_do_not_become_ast():
    doc = fluorouracil()
    assert not doc.get("activity_spectrum")
    for claim in doc["resistance_mechanisms"]:
        assert claim["mechanism_type"] == "OTHER"
        assert claim["assay"] == "Relative colony-growth area under the curve"
        assert "resistance-associated growth" in claim["phenotype_label"]
        assert "UniProtKB:P18562" in claim["note"] and "reference-only" in claim["note"]
        assert "NCBITaxon:559292" in claim["note"] and "YHR128W" in claim["note"]
        assert not {"phenotype_id", "source", "source_version"}.intersection(claim)
        assert {e["reference"] for e in claim["evidence"]} == {"PMID:37856537", "UniProtKB:P18562"}


def test_fur1_cohort_dossier_retains_reference_versions_and_search_limits():
    snapshot = json.loads((ROOT / "research/2026-10-08-fur1-cohort-grounding.json").read_bytes())
    assert snapshot["claims"] == fluorouracil()["resistance_mechanisms"]
    assert snapshot["evidence_scope"] == "GENE_LEVEL_COHORT_ASSOCIATION_NOT_ALLELE_CAUSALITY"
    assert snapshot["reference_protein"]["organism"]["taxonId"] == 559292
    assert snapshot["reference_protein"]["entryAudit"]["sequenceVersion"] == 2
    assert snapshot["reference_protein"]["entryAudit"]["entryVersion"] == 192
    assert snapshot["taxonomy"]["species"]["taxonId"] == 4932
    assert snapshot["subject_query"]["retained_results"] == 0
    assert "not proof of absent entries" in snapshot["subject_query"]["limitation"]
    assert snapshot["primary_access"] == "CACHED_EMBL_EBI_FULLTEXT_RESULTS_INSPECTED"
    assert snapshot["scope_correction"]["removed_fields"] == ["strain"]


def test_fur1_curator_associations_survive_reseeding():
    existing = fluorouracil()
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def flucytosine():
    return load_record(ROOT / "data/antibiotics/antifungal/flucytosine.yaml")


def test_flucytosine_fur1_preserves_the_card_owned_slice():
    doc = flucytosine()
    snapshot = json.loads((ROOT / "research/2026-10-08-flucytosine-fur1-grounding.json").read_bytes())
    assert doc["identifier"] == "CHEBI:5100"
    assert doc["chemical_structure"]["standard_inchi_key"] == "XRECTZIEBJDKEO-UHFFFAOYSA-N"
    assert doc["resistance_mechanisms"][:8] == snapshot["preserved_card_assertions"]
    assert len(snapshot["preserved_card_assertions"]) == 8
    assert all(c["aro_id"].startswith("ARO:") for c in snapshot["preserved_card_assertions"])
    assert doc["resistance_mechanisms"][8:] == snapshot["claims"]
    assert doc["curation_status"] == "SEEDED"


def test_flucytosine_fur1_is_not_a_parent_or_reference_allele_assignment():
    claims = flucytosine()["resistance_mechanisms"][8:]
    assert {c["label"] for c in claims} == {
        "FUR1-associated flucytosine resistance in LL13-040-derived cohort",
        "FUR1-associated flucytosine resistance in NC-02-derived cohort",
    }
    for claim in claims:
        assert claim["gene_id"] == "FUR1" and claim["gene_families"] == ["FUR1"]
        assert claim["taxon_id"] == "NCBITaxon:4932"
        assert claim["taxon_label"] == "Saccharomyces cerevisiae"
        assert "not allele-specific causality" in claim["note"]
        assert "Not all screened derivatives" in claim["note"]
        assert "P18562" in claim["note"] and "reference-only" in claim["note"]
        assert not {"strain", "alteration", "protein_accession", "strain_taxon_id",
                    "source", "aro_id"}.intersection(claim)


def test_flucytosine_fur1_uses_direct_compound_evidence_without_mic_conversion():
    doc = flucytosine()
    snapshot = json.loads((ROOT / "research/2026-10-08-flucytosine-fur1-grounding.json").read_bytes())
    assert snapshot["compound_scope"] == "DIRECT_FLUCYTOSINE_EVIDENCE_NOT_TRANSFERRED_FROM_FLUOROURACIL"
    assert snapshot["evidence_scope"] == "GENE_LEVEL_COHORT_ASSOCIATION_NOT_ALLELE_CAUSALITY"
    assert snapshot["reference_protein"]["entryAudit"]["entryVersion"] == 192
    assert snapshot["reference_protein"]["entryAudit"]["sequenceVersion"] == 2
    assert snapshot["subject_query"]["retained_results"] == 0
    assert "not proof of absent entries" in snapshot["subject_query"]["limitation"]
    assert not doc.get("activity_spectrum")
    for claim in doc["resistance_mechanisms"][8:]:
        assert claim["mechanism_type"] == "OTHER"
        assert claim["assay"] == "Relative colony-growth area under the curve"
        assert "Direct 5-FC results" in claim["evidence"][0]["notes"]
        assert {e["reference"] for e in claim["evidence"]} == {"PMID:37856537", "UniProtKB:P18562"}
        assert "phenotype_id" not in claim


def test_flucytosine_fur1_curator_and_card_slices_survive_reseeding():
    existing = flucytosine()
    seeded = copy.deepcopy(existing)
    seeded["resistance_mechanisms"] = existing["resistance_mechanisms"][:8]
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def test_flucytosine_fur1_keeps_original_yaml_order_outside_the_curation_delta():
    doc = flucytosine()
    snapshot = json.loads((ROOT / "research/2026-10-08-flucytosine-fur1-grounding.json").read_bytes())
    path = ROOT / snapshot["record"]["path"]
    assert emit_antibiotic_yaml(doc).encode() == path.read_bytes()
    doc["resistance_mechanisms"] = doc["resistance_mechanisms"][:8]
    doc["curation_history"] = doc["curation_history"][:-2]
    original_digest = hashlib.sha256(emit_antibiotic_yaml(doc).encode()).hexdigest()
    assert original_digest == snapshot["record"]["before_sha256"]
    assert snapshot["serialization_review"]["change"] == "RESTORE_ORIGINAL_KEY_ORDER_NO_BIOLOGICAL_CHANGE"


def test_cerulenin_keeps_experimental_backgrounds_and_alleles_separate():
    claims = {c["strain"]: c for c in cerulenin()["resistance_mechanisms"]}
    assert set(claims) == {"GS76", "GS77"}
    assert claims["GS77"]["alteration"] == "FabF[I108F]"
    assert claims["GS76"]["alteration"] == "FabF[I108M]"
    assert claims["GS77"]["protein_accession"] == "UniProtKB:O34340"
    assert "protein_accession" not in claims["GS76"]
    for claim in claims.values():
        assert claim["taxon_id"] == "NCBITaxon:1423"
        assert claim["taxon_label"] == "Bacillus subtilis"
        assert claim["gene_id"] == "fabF"
        assert "strain_taxon_id" not in claim


def test_cerulenin_does_not_silently_translate_source_coordinates():
    snapshot = json.loads((ROOT / "research/2026-10-07-cerulenin-grounding.json").read_text())
    claim = next(c for c in cerulenin()["resistance_mechanisms"] if c["strain"] == "GS77")
    assert "I109F" in claim["note"]
    assert "not a mutant-specific accession" in claim["note"]
    assert claim["alteration"] == "FabF[I108F]"
    assert snapshot["protein"]["entryAudit"]["sequenceVersion"] == 1
    assert snapshot["gs77_database_variant"]["location"]["start"]["value"] == 109
    assert "GS77" in snapshot["gs77_database_variant"]["description"]
    assert any(x["database"] == "PDB" and x["id"] == "4LS6" for x in snapshot["pdb_crossrefs"])


def test_cerulenin_does_not_invent_an_ast_method_or_clinical_breakpoint():
    snapshot = json.loads((ROOT / "research/2026-10-07-cerulenin-grounding.json").read_text())
    rows = snapshot["reported_mics_pending_assay_review"]
    assert {r["strain"]: r["normalized_value"] for r in rows} == {"JH642": 5, "GS76": 20, "GS77": 40}
    assert all(r["normalized_unit"] == "mg/L" and r["assay_method"] is None for r in rows)
    assert all(r["clinical_interpretation"] is None and r["breakpoint_standard"] is None for r in rows)
    assert not any(e["reference"] == "PMID:24641521"
                   for a in cerulenin().get("activity_spectrum", []) for e in a["evidence"])


def test_cerulenin_curator_evidence_survives_source_reseeding():
    existing = cerulenin()
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def test_narlaprevir_taxon_grounding_does_not_assign_patient_alleles():
    doc = load_record(ROOT / "data/antibiotics/antiviral/narlaprevir.yaml")
    assert len(doc["resistance_mechanisms"]) == 1
    claim = doc["resistance_mechanisms"][0]
    assert claim["taxon_id"] == "NCBITaxon:3052230"
    assert claim["taxon_label"] == "Orthohepacivirus hominis"
    assert claim["gene_families"] == ["HCV NS3 serine protease"]
    assert claim["evidence"][0]["reference"] == "PMID:24168257"
    assert "Taxon grounding only" in claim["note"]
    assert all(k not in claim for k in ("protein_accession", "strain", "strain_taxon_id", "alteration"))


def test_narlaprevir_keeps_reference_products_and_publication_versions_distinct():
    snapshot = json.loads((ROOT / "research/2026-10-07-narlaprevir-grounding.json").read_text())
    assert snapshot["taxonomy"]["taxonId"] == 3052230
    assert snapshot["taxonomy"]["active"] and snapshot["taxonomy"]["rank"] == "species"
    assert "Hepatitis C virus" in snapshot["taxonomy"]["otherNames"]
    assert "not final 2013 publication" in snapshot["inspected_results_version"]
    candidates = snapshot["reference_candidates"]
    assert {c["accession"]: c["protein_name"] for c in candidates} == {
        "UniProtKB:P27958": "Genome polyprotein", "UniProtKB:P0C045": "F protein",
    }
    assert all(c["assigned_to_patient_claim"] is False for c in candidates)
    assert all(c["embl_cross_reference"]["id"] == "AF009606" for c in candidates)


def test_narlaprevir_grounding_survives_reseeding():
    existing = load_record(ROOT / "data/antibiotics/antiviral/narlaprevir.yaml")
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def raltegravir():
    return load_record(ROOT / "data/antibiotics/antiviral/raltegravir.yaml")


def test_raltegravir_keeps_model_variants_separate_from_hiv_alleles():
    claims = raltegravir()["resistance_mechanisms"]
    assert len(claims) == 2
    assert {c["alteration"] for c in claims} == {"S217H", "N224H"}
    for claim in claims:
        assert claim["taxon_id"] == "NCBITaxon:11963"
        assert claim["taxon_label"] == "Human spumaretrovirus"
        assert claim["protein_accession"] == "UniProtKB:P14350"
        assert claim["gene_families"] == ["retroviral integrase"]
        assert "comparative context, not this allele" in claim["note"]
        assert "without conversion to polyprotein coordinates" in claim["note"]


def test_raltegravir_reference_crosswalk_does_not_claim_species_or_exact_mutant():
    snapshot = json.loads((ROOT / "research/2026-10-08-raltegravir-model-grounding.json").read_text())
    assert snapshot["taxonomy"]["rank"] == "no rank"
    assert snapshot["taxonomy"]["active"] is True
    protein = snapshot["protein"]
    assert protein["primaryAccession"] == "P14350"
    assert protein["entryAudit"] == {"entryVersion": 180, "sequenceVersion": 2}
    assert protein["organism"]["taxonId"] == snapshot["taxonomy"]["taxonId"] == 11963
    assert protein["proteinDescription"]["recommendedName"]["fullName"]["value"] == "Pro-Pol polyprotein"
    assert {p["id"] for p in snapshot["pdb_reference_links"]} == {"3OYA", "3OYK", "3OYM"}
    for claim in raltegravir()["resistance_mechanisms"]:
        assert "not a mutant-specific accession" in claim["note"]
        assert all(k not in claim for k in ("strain", "strain_taxon_id", "gene_id"))


def test_raltegravir_biochemistry_is_not_a_clinical_or_whole_virus_measurement():
    doc = raltegravir()
    for claim in doc["resistance_mechanisms"]:
        assert claim["assay"] == "Biochemical integrase inhibition assay"
        assert claim["phenotype_label"] == "reduced biochemical sensitivity to raltegravir"
        assert claim["evidence"][0]["reference"] == "PMID:21030679"
        assert "No whole-virus phenotype, clinical resistance call" in claim["note"]
    assert not any(e["reference"] == "PMID:21030679"
                   for a in doc.get("activity_spectrum", []) for e in a["evidence"])


def test_raltegravir_model_curation_preserves_hivdb_rules():
    doc = raltegravir()
    snapshot = json.loads((ROOT / "research/2026-10-08-raltegravir-model-grounding.json").read_text())
    rules = doc["genotype_resistance_score_rules"]
    assert len(rules) == snapshot["unchanged_hivdb_rule_count"] == 35
    payload = json.dumps(rules, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    assert hashlib.sha256(payload).hexdigest() == snapshot["unchanged_hivdb_rules_sha256"]


def test_raltegravir_model_grounding_survives_reseeding():
    existing = raltegravir()
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["genotype_resistance_score_rules"] == existing["genotype_resistance_score_rules"]
    assert merged["curation_history"] == existing["curation_history"]


def object_sha(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()


def aggregate_context_review(name):
    snapshot = json.loads((ROOT / f"research/2026-10-08-{name}-grounding.json").read_text())
    return load_record(ROOT / snapshot["path"]), snapshot


@pytest.mark.parametrize("name", ["pr39", "daclatasvir"])
def test_aggregate_grounding_preserves_unrelated_fields_and_history(name):
    doc, snapshot = aggregate_context_review(name)
    path = ROOT / snapshot["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == snapshot["after_record_sha256"]
    unchanged = {k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert object_sha(unchanged) == snapshot["unchanged_fields_sha256"]
    assert object_sha(doc["curation_history"][:-1]) == snapshot["original_history_sha256"]
    assert doc["curation_history"][-1]["action"] == "GROUNDED_RESISTANCE_CONTEXT"
    assert doc["curation_status"] == "REVIEWED"
    expected = copy.deepcopy(snapshot["original_claim"])
    assert object_sha(expected) == snapshot["original_claim_sha256"]
    expected.update(taxon_id=f"NCBITaxon:{snapshot['taxonomy']['taxonId']}",
                    taxon_label=snapshot["taxonomy"]["scientificName"])
    expected["evidence"].append(snapshot["added_evidence"])
    if name == "pr39":
        expected["gene_id"] = "sbmA"
        expected["note"] += snapshot["claim_note_suffix"]
    else:
        expected["note"] = snapshot["claim_note_replacement"]
    assert doc["resistance_mechanisms"] == [expected]
    assert object_sha(expected) == snapshot["current_claim_sha256"]


@pytest.mark.parametrize("name,taxid,label", [
    ("pr39", 28901, "Salmonella enterica"),
    ("daclatasvir", 3052230, "Orthohepacivirus hominis"),
])
def test_aggregate_species_grounding_does_not_create_exact_alleles(name, taxid, label):
    doc, snapshot = aggregate_context_review(name)
    taxonomy = snapshot["taxonomy"]
    assert taxonomy["taxonId"] == taxid and taxonomy["scientificName"] == label
    assert taxonomy["active"] and taxonomy["rank"] == "species"
    claim = doc["resistance_mechanisms"][0]
    assert claim["taxon_id"] == f"NCBITaxon:{taxid}" and claim["taxon_label"] == label
    assert all(k not in claim for k in ("protein_accession", "strain", "strain_taxon_id", "alteration"))
    assert claim["evidence"][0]["reference"] == snapshot["primary_reference"]


def test_pr39_crosswalk_is_a_reference_not_a_mutant_accession():
    doc, snapshot = aggregate_context_review("pr39")
    reference = snapshot["reference_candidate"]
    protein = reference["protein"]
    assert protein["primaryAccession"] == "Q8ZRF5"
    assert protein["entryType"] == "UniProtKB unreviewed (TrEMBL)"
    assert protein["entryAudit"] == {"entryVersion": 106, "sequenceVersion": 1}
    assert reference["assigned_to_claim"] is False
    assert reference["taxonomy"]["taxonId"] == protein["organism"]["taxonId"] == 99287
    assert reference["taxonomy"]["rank"] == "strain"
    assert reference["source_reference_genome"] == "NC_003197"
    assert reference["source_reference_version"] is None
    assert any(x["database"] == "RefSeq" and x["id"] == "NP_459371.1"
               and {"key": "NucleotideSequenceId", "value": "NC_003197.2"} in x["properties"]
               for x in protein["uniProtKBCrossReferences"])
    claim = doc["resistance_mechanisms"][0]
    assert claim["gene_id"] == "sbmA" and claim["mechanism_type"] == "OTHER"
    assert "did not directly measure uptake" in claim["note"]
    assert "not one experimental allele" in claim["note"]


def test_daclatasvir_patient_context_is_not_a_reference_replicon():
    doc, snapshot = aggregate_context_review("daclatasvir")
    claim = doc["resistance_mechanisms"][0]
    assert snapshot["source_reference_backgrounds"] == ["H77c", "Con1"]
    assert snapshot["reference_candidate"] is None
    assert "gene_id" not in claim
    assert "assessed separately" in claim["note"]
    assert "not every individual substitution" in claim["note"]
    assert "does not establish the administered compound form" in claim["note"]
    assert "Hepatitis C virus" in snapshot["taxonomy"]["otherNames"]


@pytest.mark.parametrize("name", ["pr39", "daclatasvir"])
def test_aggregate_grounding_survives_source_reseeding(name):
    existing, _ = aggregate_context_review(name)
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, existing)
    assert merged["resistance_mechanisms"] == existing["resistance_mechanisms"]
    assert merged["curation_history"] == existing["curation_history"]


def compound_form_review(name):
    snapshot = json.loads((ROOT / "research/2026-10-08-hcv-compound-form-reviews.json").read_text())
    entry = snapshot["records"][name]
    return load_record(ROOT / entry["path"]), entry


@pytest.mark.parametrize("name", ["dasabuvir", "paritaprevir"])
def test_compound_form_warning_preserves_original_claim_without_new_grounding(name):
    doc, entry = compound_form_review(name)
    assert len(doc["resistance_mechanisms"]) == 1
    claim = copy.deepcopy(doc["resistance_mechanisms"][0])
    assert claim["note"].endswith(entry["claim_note_suffix"])
    assert "has not been revalidated for exact-form placement" in claim["note"]
    claim["note"] = claim["note"].removesuffix(entry["claim_note_suffix"])
    assert object_sha(claim) == entry["original_claim_sha256"]
    assert claim["evidence"][0]["reference"] == entry["primary_reference"]
    assert all(k not in claim for k in (
        "protein_accession", "taxon_id", "strain", "strain_taxon_id", "alteration",
    ))


@pytest.mark.parametrize("name", ["dasabuvir", "paritaprevir"])
def test_compound_form_warning_is_open_and_preserves_unrelated_fields(name):
    doc, entry = compound_form_review(name)
    assert doc["identifier"] == entry["identifier"]
    assert doc["chemical_structure"]["standard_inchi_key"] == entry["standard_inchi_key"]
    assert doc["discussions"] == entry["original_discussions"] + [entry["discussion"]]
    discussion = doc["discussions"][-1]
    assert discussion["status"] == "OPEN" and discussion["kind"] == "CURATION_TODO"
    assert "not renewed" in discussion["notes"]
    assert "resistance_mechanisms" in discussion["attaches_to"]
    unchanged = {
        k: v for k, v in doc.items() if k not in {"discussions", "resistance_mechanisms", "curation_history"}
    }
    assert object_sha(unchanged) == entry["unchanged_fields_sha256"]
    assert object_sha(doc["curation_history"][:-1]) == entry["original_history_sha256"]
    assert doc["curation_history"][-1]["action"] == "FLAGGED_COMPOUND_FORM_REVIEW"
    assert hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["after_record_sha256"]


@pytest.mark.parametrize("name", ["dasabuvir", "paritaprevir"])
def test_compound_form_warnings_survive_reseeding(name):
    existing, _ = compound_form_review(name)
    seeded = copy.deepcopy(existing)
    seeded.pop("resistance_mechanisms")
    seeded.pop("discussions")
    merged = merge_with_existing(seeded, existing)
    for field in ("resistance_mechanisms", "discussions", "curation_history", "chemical_structure"):
        assert merged[field] == existing[field]


def test_dasabuvir_warning_does_not_copy_claims_to_related_structures():
    lead = json.loads((ROOT / "research/2026-10-08-dasabuvir-identity-lead.json").read_text())
    for entry in lead["records"]:
        if entry["identifier"] == "CHEBI:85182":
            continue
        path = ROOT / entry["path"]
        doc = load_record(path)
        assert not doc.get("resistance_mechanisms")
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["record_sha256"]


def elbasvir_grounding():
    snapshot = json.loads((ROOT / "research/2026-10-08-elbasvir-grounding.json").read_text())
    return load_record(ROOT / snapshot["path"]), snapshot


def test_elbasvir_species_grounding_does_not_assign_one_experimental_allele():
    doc, snapshot = elbasvir_grounding()
    assert len(doc["resistance_mechanisms"]) == 1
    claim = doc["resistance_mechanisms"][0]
    assert claim["taxon_id"] == "NCBITaxon:3052230"
    assert claim["taxon_label"] == snapshot["taxonomy"]["scientificName"] == "Orthohepacivirus hominis"
    assert snapshot["taxonomy"]["active"] and snapshot["taxonomy"]["rank"] == "species"
    assert "Hepatitis C virus" in snapshot["taxonomy"]["otherNames"]
    assert "Taxon grounding only" in claim["note"]
    assert all(k not in claim for k in (
        "protein_accession", "strain", "strain_taxon_id", "alteration", "gene_id",
    ))
    assert not any(e["reference"] == "PMID:26303801"
                   for a in doc.get("activity_spectrum", []) for e in a["evidence"])


def test_elbasvir_crosswalks_identify_reference_polyproteins_not_patient_sequences():
    _, snapshot = elbasvir_grounding()
    entries = {c["source_reference_accession"]: c for c in snapshot["reference_candidates"]}
    assert {s: e["accession"] for s, e in entries.items()} == {
        "AJ238799": "UniProtKB:Q9WMX2", "GU814263": "UniProtKB:D6P444",
    }
    assert entries["AJ238799"]["entry_audit"] == {"entryVersion": 212, "sequenceVersion": 3}
    assert entries["GU814263"]["entry_audit"] == {"entryVersion": 99, "sequenceVersion": 1}
    assert "unreviewed" in entries["GU814263"]["entry_type"]
    for source_id, entry in entries.items():
        assert entry["assigned_to_resistance_claim"] is False
        assert entry["protein_name"] == "Genome polyprotein"
        assert entry["explicit_cross_reference"]["database"] == "EMBL"
        assert entry["explicit_cross_reference"]["id"] == source_id
        taxon = entry["reference_taxonomy"]
        assert taxon["active"] and taxon["rank"] == "no rank"
        assert taxon["taxonId"] == entry["reference_organism"]["taxonId"]
        assert any(t["taxonId"] == 3052230 for t in taxon["lineage"])


def test_elbasvir_limited_empty_query_is_not_a_missing_protein_conclusion():
    _, snapshot = elbasvir_grounding()
    unresolved = snapshot["unresolved_reference"]
    assert unresolved["source_accession"] == "NC_004102"
    assert unresolved["query"] == "xref:refseq-NC_004102"
    assert unresolved["result_count"] == 0
    assert unresolved["status"] == "NO_EXPLICIT_CROSSWALK_IN_THIS_QUERY"
    assert unresolved["suggestions_followed"] is False
    assert any("not evidence" in text for text in snapshot["limitations"])


def test_elbasvir_incremental_curation_preserves_original_claim_and_reseeds():
    doc, snapshot = elbasvir_grounding()
    claim = copy.deepcopy(doc["resistance_mechanisms"][0])
    assert claim["note"].endswith(snapshot["claim_note_suffix"])
    claim["note"] = claim["note"].removesuffix(snapshot["claim_note_suffix"])
    claim.pop("taxon_id")
    claim.pop("taxon_label")
    claim["evidence"].remove(snapshot["added_evidence"])
    assert object_sha(claim) == snapshot["original_claim_sha256"]
    unchanged = {k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert object_sha(unchanged) == snapshot["unchanged_fields_sha256"]
    assert object_sha(doc["curation_history"][:-1]) == snapshot["original_history_sha256"]
    record_sha = hashlib.sha256((ROOT / snapshot["path"]).read_bytes()).hexdigest()
    assert record_sha == snapshot["after_record_sha256"]
    seeded = copy.deepcopy(doc)
    seeded.pop("resistance_mechanisms")
    merged = merge_with_existing(seeded, doc)
    assert merged["resistance_mechanisms"] == doc["resistance_mechanisms"]
    assert merged["curation_history"] == doc["curation_history"]

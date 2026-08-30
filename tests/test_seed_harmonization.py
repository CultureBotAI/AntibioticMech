"""Unit tests for the harmonization rules, without touching the corpus."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seed_from_sources import (  # noqa: E402
    CONF_PATH,
    Concept,
    classify,
    merge,
    mint,
    normalize_xref,
    slugify,
)

CONF = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))


def test_minted_identifiers_are_stable_and_source_scoped():
    """The minted CURIE is the key curation decisions are written against, so it
    must not move when an upstream label is corrected."""
    assert mint("ARO", "ARO:0000006") == mint("ARO", "ARO:0000006")
    assert mint("ARO", "ARO:0000006") != mint("CHEBI", "ARO:0000006")
    assert mint("ARO", "ARO:0000006").startswith("antibioticmech:aro-")


def test_xrefs_that_cannot_resolve_are_dropped_not_guessed():
    assert normalize_xref("PubChem:12560") == "pubchem.compound:12560"
    assert normalize_xref("chembl:CHEMBL532") == "chembl:CHEMBL532"
    assert normalize_xref("CHEBI:48923") == "CHEBI:48923"
    # A ChEBI accession type masquerading as a prefix, and a local part with
    # characters no CURIE may carry.
    assert normalize_xref("MANUAL_X_REF:Decarboxylated_8,5'-diferulic_acid") is None
    assert normalize_xref("no-colon-here") is None


def test_the_narrower_target_group_wins_the_filing():
    """Tetracycline bears antibacterial, antifungal and antiprotozoal roles in
    ChEBI. It is filed as an antibacterial, and an antitubercular compound is
    filed under the narrower mycobacterial class."""
    tetracycline_roles = ["CHEBI:33282", "CHEBI:35718", "CHEBI:35820"]
    assert classify(tetracycline_roles, CONF, from_aro=False) == "ANTIBACTERIAL"
    assert classify(["CHEBI:33282", "CHEBI:33231"], CONF, from_aro=False) == "ANTIMYCOBACTERIAL"
    assert classify(["CHEBI:35718"], CONF, from_aro=False) == "ANTIFUNGAL"


def test_an_aro_concept_with_no_chebi_role_falls_back_to_antibacterial():
    """The fallback, for a CARD molecule with neither a ChEBI role nor a
    group-naming drug class."""
    assert classify([], CONF, from_aro=True) == "ANTIBACTERIAL"
    assert classify([], CONF, from_aro=False) == "ANTIMICROBIAL_UNSPECIFIED"


def test_a_card_drug_class_that_names_a_target_group_outranks_chebi_roles():
    """ChEBI gives fluconazole and amphotericin B a generic `antibacterial
    agent` role. CARD calls them a triazole antifungal and a polyene antifungal
    — a compound-specific curated classification, and the stronger evidence."""
    chebi_says_antibacterial = ["CHEBI:33282", "CHEBI:35718"]
    assert classify(chebi_says_antibacterial, CONF, from_aro=True) == "ANTIBACTERIAL"
    assert classify(chebi_says_antibacterial, CONF, from_aro=True,
                    aro_class_ids=("ARO:3007499",)) == "ANTIFUNGAL"  # triazole antifungal
    assert classify([], CONF, from_aro=True,
                    aro_class_ids=("ARO:3007497",)) == "ANTIFUNGAL"  # polyene antifungal


def test_a_drug_class_that_does_not_name_a_target_group_is_not_guessed_from():
    """"imidazole antibiotic" covers both antibacterials and antifungals.
    Inferring the target group from the chemistry is exactly the guess this
    repository should not make, so such a class is absent from the map and the
    compound falls through to its ChEBI roles."""
    assert "ARO:3007507" not in CONF.get("aro_class_to_class", {})
    assert classify(["CHEBI:35718"], CONF, from_aro=True,
                    aro_class_ids=("ARO:3007507",)) == "ANTIFUNGAL"


def _concept(source, source_id, label, inchikey, roles=()):
    concept = Concept(source, source_id, label)
    concept.roles = list(roles)
    concept.structure = {"standard_inchi_key": inchikey, "standard_inchi": f"InChI={inchikey}"}
    concept.minted = mint(source, source_id)
    return concept


def test_concepts_sharing_a_structure_merge_into_one_record():
    """The merge is the product: CARD and ChEBI describing one structure must
    produce one record carrying both attestations, not two records."""
    key = "JGSARLDLIJGVTE-MBNYWOFBSA-N"
    chebi = _concept("CHEBI", "CHEBI:18208", "benzylpenicillin", key, ["CHEBI:33282"])
    aro = _concept("ARO", "ARO:3000636", "penicillin G", key)
    aro.xrefs = ["CHEBI:18208"]
    chebi_rows = {"CHEBI:18208": {"standard_inchi_key": key}}
    records, skipped = merge([chebi, aro], chebi_rows, CONF, {}, "2026-08-29")
    assert skipped == []
    assert list(records) == ["CHEBI:18208"]
    assert {c["source"] for c in records["CHEBI:18208"]["source_concepts"]} == {"CHEBI", "ARO"}


def test_a_concept_without_a_structure_is_skipped_not_written():
    """A name is not a structure. 'antibiotic mixture' has no InChIKey and must
    never become a record."""
    concept = Concept("ARO", "ARO:3000707", "antibiotic mixture")
    concept.minted = mint("ARO", "ARO:3000707")
    records, skipped = merge([concept], {}, CONF, {}, "2026-08-29")
    assert records == {}
    assert [c.label for c in skipped] == ["antibiotic mixture"]


def test_an_exclude_decision_removes_a_concept_entirely():
    concept = _concept("ARO", "ARO:3000707", "something out of scope", "AAAAAAAAAAAAAA-BBBBBBBBBB-C")
    decisions = {concept.minted: {"decision": "EXCLUDE", "identifier": ""}}
    records, skipped = merge([concept], {}, CONF, decisions, "2026-08-29")
    assert records == {} and skipped == []


def test_a_curator_identifier_override_wins():
    concept = _concept("ARO", "ARO:0000018", "viomycin", "GXFAIFRPOKBQRV-GHXCTMGLSA-N")
    decisions = {concept.minted: {"decision": "GROUND", "identifier": "CHEBI:9727"}}
    records, _ = merge([concept], {}, CONF, decisions, "2026-08-29")
    assert list(records) == ["CHEBI:9727"]
    assert records["CHEBI:9727"]["grounding_status"] == "EXACT"


def test_slugs_are_url_safe_and_stable():
    assert slugify("erythromycin A") == "erythromycin-a"
    assert slugify("(R)-linalool") == "r-linalool"
    assert slugify("N,N'-bis(2-chloroethyl)amine") == "n-n-bis-2-chloroethyl-amine"
    assert slugify("") == "unnamed"


def test_a_reseed_preserves_curated_work():
    """`just seed-apply` months into curation must not be a way to lose it.

    The seeder rebuilds every record from the inventories, so without this merge
    a re-seed would replace a curator's mechanism graph, sign-off and evidence
    with the empty seeded shape.
    """
    from seed_from_sources import merge_with_existing

    seeded = {
        "identifier": "CHEBI:42355",
        "label": "erythromycin A",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [{"timestamp": "2026-08-29T00:00:00Z", "curator": "seed_from_sources",
                              "action": "SEEDED_FROM_SOURCES"}],
    }
    curated = dict(seeded) | {
        "curation_status": "REVIEWED",
        "mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
        "causal_graphs": [{"graph_id": "g1", "nodes": [], "edges": []}],
        "evidence": [{"reference": "PMID:7683018"}],
        "curation_history": seeded["curation_history"] + [
            {"timestamp": "2026-09-01T00:00:00Z", "curator": "jane", "action": "REVIEWED"}],
    }
    merged = merge_with_existing(seeded, curated)
    assert merged["curation_status"] == "REVIEWED"
    assert merged["mode_of_action"] == "PROTEIN_SYNTHESIS_INHIBITION"
    assert merged["causal_graphs"] == curated["causal_graphs"]
    assert merged["evidence"] == curated["evidence"]
    # Unchanged seeded fields must not append a new event on every run.
    assert merged["curation_history"] == curated["curation_history"]


def test_a_reseed_records_an_event_when_seeded_content_changed():
    from seed_from_sources import merge_with_existing

    existing = {
        "identifier": "CHEBI:42355", "label": "erythromycin", "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "REVIEWED", "grounding_status": "EXACT",
        "curation_history": [{"timestamp": "2026-08-29T00:00:00Z", "curator": "seed_from_sources",
                              "action": "SEEDED_FROM_SOURCES"}],
    }
    reseeded = dict(existing) | {"label": "erythromycin A", "curation_status": "SEEDED"}
    merged = merge_with_existing(reseeded, existing)
    assert merged["label"] == "erythromycin A"
    assert merged["curation_status"] == "REVIEWED"
    assert [e["action"] for e in merged["curation_history"]][-1] == "RESEEDED_FROM_SOURCES"


def test_a_curator_added_target_survives_but_card_items_are_reseeded():
    """CARD-derived items are the seeder's to replace; anything with a primary
    citation is the curator's and is kept."""
    from seed_from_sources import merge_with_existing

    card_item = {"target_label": "50S subunit",
                 "evidence": [{"reference": "ARO:3000710", "notes": "database assertion"}]}
    curated_item = {"target_label": "23S rRNA A2058",
                    "evidence": [{"reference": "PMID:15980346"}]}
    seeded = {"identifier": "CHEBI:42355", "label": "erythromycin A",
              "antimicrobial_class": "ANTIBACTERIAL", "curation_status": "SEEDED",
              "grounding_status": "EXACT", "molecular_targets": [card_item],
              "curation_history": []}
    existing = dict(seeded) | {"molecular_targets": [{"target_label": "stale CARD row",
                                                     "evidence": [{"reference": "ARO:9999999"}]},
                                                    curated_item]}
    merged = merge_with_existing(seeded, existing)
    labels = [t["target_label"] for t in merged["molecular_targets"]]
    assert labels == ["50S subunit", "23S rRNA A2058"]

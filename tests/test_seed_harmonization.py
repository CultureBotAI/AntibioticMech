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


def _chebi_row(inchikey, roles=""):
    return {"standard_inchi_key": inchikey, "role_ids": roles, "smiles": "",
            "standard_inchi": "", "molecular_formula": "", "charge": "",
            "average_mass": "", "monoisotopic_mass": ""}


def test_a_curator_identifier_override_wins():
    key = "GXFAIFRPOKBQRV-GHXCTMGLSA-N"
    concept = _concept("ARO", "ARO:0000018", "viomycin", key)
    decisions = {concept.minted: {"decision": "GROUND", "identifier": "CHEBI:9727"}}
    records, _ = merge([concept], {"CHEBI:9727": _chebi_row(key)}, CONF, decisions, "2026-08-29")
    assert list(records) == ["CHEBI:9727"]
    assert records["CHEBI:9727"]["grounding_status"] == "EXACT"


def test_a_ground_decision_to_an_unknown_chebi_id_is_refused():
    """A typo in a decision row would otherwise mint a record keyed to a
    compound that does not exist, with grounding_status EXACT."""
    import pytest

    concept = _concept("ARO", "ARO:0000018", "viomycin", "GXFAIFRPOKBQRV-GHXCTMGLSA-N")
    decisions = {concept.minted: {"decision": "GROUND", "identifier": "CHEBI:4235700"}}
    with pytest.raises(SystemExit, match="not a ChEBI entry"):
        merge([concept], {"CHEBI:42355": _chebi_row("AAAAAAAAAAAAAA-BBBBBBBBBB-C")},
              CONF, decisions, "2026-08-29")


def test_a_ground_decision_to_a_structureless_class_term_is_refused():
    """CHEBI:48923 "erythromycin" is a class over erythromycins A-E with no
    structure of its own. A record is one chemical structure and a drug class is
    never a record, so grounding to one must fail loudly."""
    import pytest

    concept = _concept("ARO", "ARO:0000006", "erythromycin", "ULGZDMOVFRHVEP-RWJQBGPGSA-N")
    decisions = {concept.minted: {"decision": "GROUND", "identifier": "CHEBI:48923"}}
    with pytest.raises(SystemExit, match="no structure of its own"):
        merge([concept], {"CHEBI:48923": _chebi_row("")}, CONF, decisions, "2026-08-29")


def test_a_ground_decision_that_would_split_a_structure_is_refused():
    """The InChIKey fold only folds MINTED into EXACT, so an override creating a
    second grounded record for a structure another record already carries would
    pass every gate — including the collision flagger, which looks only at
    all-MINTED groups."""
    import pytest

    key = "ULGZDMOVFRHVEP-RWJQBGPGSA-N"
    existing = _concept("CHEBI", "CHEBI:42355", "erythromycin A", key)
    diverted = _concept("ARO", "ARO:0000006", "erythromycin", key)
    rows = {"CHEBI:42355": _chebi_row(key), "CHEBI:99999": _chebi_row(key)}
    decisions = {diverted.minted: {"decision": "GROUND", "identifier": "CHEBI:99999"}}
    with pytest.raises(SystemExit, match="split one structure"):
        merge([existing, diverted], rows, CONF, decisions, "2026-08-29")


def test_a_curator_literature_upgrade_survives_a_reseed():
    """docs/HARMONIZATION.md tells a curator to replace a CARD item's ARO
    reference with a primary citation. An ownership rule keyed on the ARO id
    classified that upgraded item as the seeder's and reverted it."""
    from seed_from_sources import is_card_sourced, merge_with_existing

    upgraded = {
        "mechanism_type": "ANTIBIOTIC_TARGET_ALTERATION",
        "aro_id": "ARO:3000375",
        "label": "ermB",
        "evidence": [{"reference": "PMID:15980346", "notes": "curator: primary source"}],
    }
    # Not the seeder's under either signal that was ever tried: it cites a PMID,
    # and it carries no CARD note marker.
    assert not is_card_sourced(upgraded)

    seeded = {"identifier": "CHEBI:42355", "label": "erythromycin A",
              "antimicrobial_class": "ANTIBACTERIAL", "curation_status": "SEEDED",
              "grounding_status": "EXACT", "curation_history": []}
    merged = merge_with_existing(seeded, dict(seeded) | {"resistance_mechanisms": [upgraded]})
    assert merged["resistance_mechanisms"] == [upgraded]


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
        "mode_of_action_notes": "CURATOR: confirmed against PMID:7683018",
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

    card_item = {"target_id": "ARO:3000710", "target_label": "50S subunit",
                 "evidence": [{"reference": "ARO:3000710",
                               "notes": "CARD/ARO asserts targeted_by_antibiotic ..."}]}
    curated_item = {"target_label": "23S rRNA A2058",
                    "evidence": [{"reference": "PMID:15980346"}]}
    seeded = {"identifier": "CHEBI:42355", "label": "erythromycin A",
              "antimicrobial_class": "ANTIBACTERIAL", "curation_status": "SEEDED",
              "grounding_status": "EXACT", "molecular_targets": [card_item],
              "curation_history": []}
    stale_card_item = {"target_id": "ARO:9999999", "target_label": "stale CARD row",
                       "evidence": [{"reference": "ARO:9999999",
                                     "notes": "CARD/ARO asserts targeted_by_antibiotic ..."}]}
    existing = dict(seeded) | {"molecular_targets": [stale_card_item, curated_item]}
    merged = merge_with_existing(seeded, existing)
    labels = [t["target_label"] for t in merged["molecular_targets"]]
    assert labels == ["50S subunit", "23S rRNA A2058"]


def test_a_curator_item_citing_an_aro_term_is_not_mistaken_for_seeder_output():
    """The case the old prefix-only ownership test deleted: a curator grounds a
    resistance mechanism in an ARO determinant CARD does not link to this
    molecule. It cites ARO, but it is not the seeder's, and it must survive."""
    from seed_from_sources import is_card_sourced, merge_with_existing

    curator_item = {
        "mechanism_type": "ANTIBIOTIC_EFFLUX",
        "aro_id": "ARO:3000216",
        "label": "acrB",
        "evidence": [{"reference": "ARO:3000216",
                      "notes": "curator: acrB effluxes this compound (PMID pending)"}],
    }
    assert not is_card_sourced(curator_item)

    seeded = {"identifier": "CHEBI:42355", "label": "erythromycin A",
              "antimicrobial_class": "ANTIBACTERIAL", "curation_status": "SEEDED",
              "grounding_status": "EXACT", "curation_history": []}
    merged = merge_with_existing(seeded, dict(seeded) | {"resistance_mechanisms": [curator_item]})
    assert merged["resistance_mechanisms"] == [curator_item]


def test_a_record_that_changes_class_keeps_its_curation(tmp_path, monkeypatch):
    """The pipeline-level idempotence test. `merge_with_existing` was already
    covered in isolation, but the loss happened one level up: a record whose
    class changes moves directory, and resolving the existing file only at the
    NEW path treated it as brand new and replaced every curated field with the
    empty seeded shape. 57 records moved class on a single run of this repo's
    own pipeline, so this is the live path, not a corner case.
    """
    import seed_from_sources as sfs

    corpus = tmp_path / "antibiotics"
    old_path = corpus / "antiprotozoal" / "posaconazole.yaml"
    old_path.parent.mkdir(parents=True)
    curated = {
        "identifier": "CHEBI:64355", "label": "posaconazole",
        "antimicrobial_class": "ANTIPROTOZOAL", "curation_status": "REVIEWED",
        "grounding_status": "EXACT",
        "chemical_structure": {"standard_inchi_key": "RAGOYPUPXAKGKH-XAKZXMRKSA-N"},
        "source_concepts": [{"source": "CHEBI", "source_id": "CHEBI:64355",
                             "source_label": "posaconazole",
                             "minted_identifier": "antibioticmech:chebi-1111111111"}],
        "mode_of_action": "ERGOSTEROL_PATHWAY_INHIBITION",
        "mode_of_action_notes": "CURATOR: azole, confirmed against PMID:1",
        "causal_graphs": [{"graph_id": "g1", "nodes": [], "edges": []}],
        "curation_history": [{"timestamp": "2026-08-29T00:00:00Z", "curator": "jane",
                              "action": "REVIEWED"}],
    }
    old_path.write_text(yaml.safe_dump(curated, sort_keys=False), encoding="utf-8")

    monkeypatch.setattr(sfs, "CORPUS_DIR", corpus)
    monkeypatch.setattr(sfs, "PATHS_FILE", corpus / "PATHS.tsv")
    (corpus / "PATHS.tsv").write_text(
        "identifier\tantimicrobial_class\tslug\nCHEBI:64355\tANTIPROTOZOAL\tposaconazole\n",
        encoding="utf-8")

    reseeded = {k: curated[k] for k in ("identifier", "label", "grounding_status",
                                        "chemical_structure", "source_concepts")}
    reseeded["antimicrobial_class"] = "ANTIFUNGAL"     # the class moved
    reseeded["curation_status"] = "SEEDED"
    reseeded["curation_history"] = []

    previous = sfs.read_lockfile_paths()
    assert previous["CHEBI:64355"] == old_path

    merged = sfs.merge_with_existing(
        reseeded, yaml.safe_load(previous["CHEBI:64355"].read_text(encoding="utf-8")))
    assert merged["antimicrobial_class"] == "ANTIFUNGAL"    # the seeded field moves
    assert merged["curation_status"] == "REVIEWED"          # the curated ones survive
    assert merged["mode_of_action"] == "ERGOSTEROL_PATHWAY_INHIBITION"
    assert merged["causal_graphs"] == curated["causal_graphs"]


def test_a_ground_decision_to_a_different_structure_is_refused():
    """A decision sets identity; it must not silently key a record to a compound
    whose structure it does not carry. Identifier, structure and merge key are
    three separate values in the seeder, and this path only became reachable
    once GROUND started working on structureless concepts."""
    import pytest
    from seed_from_sources import merge as sfs_merge

    concept = _concept("ARO:0000006", "ARO:0000006", "erythromycin",
                       "AAAAAAAAAAAAAA-BBBBBBBBBB-C")
    concept.source = "ARO"
    chebi_rows = {"CHEBI:18208": {"standard_inchi_key": "JGSARLDLIJGVTE-MBNYWOFBSA-N",
                                  "role_ids": "", "smiles": "", "standard_inchi": "",
                                  "molecular_formula": ""}}
    decisions = {concept.minted: {"decision": "GROUND", "identifier": "CHEBI:18208"}}
    with pytest.raises(SystemExit) as excinfo:
        sfs_merge([concept], chebi_rows, CONF, decisions, "2026-08-29")
    assert "structures differ" in str(excinfo.value)


def _ledger_sandbox(tmp_path, monkeypatch, paths_rows, retired_rows=()):
    """A corpus directory with a lockfile and ledger, for the slug tests."""
    import seed_from_sources as sfs

    corpus = tmp_path / "antibiotics"
    corpus.mkdir(parents=True)
    monkeypatch.setattr(sfs, "CORPUS_DIR", corpus)
    monkeypatch.setattr(sfs, "PATHS_FILE", corpus / "PATHS.tsv")
    monkeypatch.setattr(sfs, "RETIRED_FILE", corpus / "RETIRED.tsv")
    (corpus / "PATHS.tsv").write_text(
        "identifier\tantimicrobial_class\tslug\n"
        + "".join(f"{i}\t{c}\t{s}\n" for i, c, s in paths_rows), encoding="utf-8")
    if retired_rows:
        (corpus / "RETIRED.tsv").write_text(
            "identifier\tslug\tretired_on\n"
            + "".join(f"{i}\t{s}\t2026-08-29\n" for i, s in retired_rows), encoding="utf-8")
    return sfs, corpus


def test_a_canary_on_a_returning_compound_does_not_leave_it_in_both_ledgers(tmp_path, monkeypatch):
    """`just seed-canary` is mandatory before every bulk write. Skipping the
    retired-ledger reconciliation on a partial write left a re-admitted
    identifier in PATHS.tsv and RETIRED.tsv at once, failing the corpus
    integrity test — the same class of inconsistency `only=` was added to fix.
    19 antivirals genuinely returned by this path."""
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch,
                             [("CHEBI:1", "ANTIBACTERIAL", "alpha")],
                             [("CHEBI:2", "beta")])
    records = {"CHEBI:1": {"antimicrobial_class": "ANTIBACTERIAL"},
               "CHEBI:2": {"antimicrobial_class": "ANTIFUNGAL"}}
    sfs.write_lockfile(records, {"CHEBI:1": "alpha", "CHEBI:2": "beta"}, only={"CHEBI:2"})
    assert set(sfs.read_retired()) & set(sfs.read_lockfile()) == set()
    assert "CHEBI:2" in sfs.read_lockfile()


def test_a_partial_run_never_retires_an_identifier_it_did_not_build(tmp_path, monkeypatch):
    """The other half: a canary knows nothing about the records it skipped, so
    it must not conclude they are gone."""
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch,
                             [("CHEBI:1", "ANTIBACTERIAL", "alpha"),
                              ("CHEBI:9", "ANTIFUNGAL", "gamma")])
    sfs.write_lockfile({"CHEBI:1": {"antimicrobial_class": "ANTIBACTERIAL"}},
                       {"CHEBI:1": "alpha"}, only={"CHEBI:1"})
    assert sfs.read_retired() == {}
    assert "CHEBI:9" in sfs.read_lockfile()


def test_the_documented_rename_reserves_the_slug_it_frees(tmp_path, monkeypatch):
    """CLAUDE.md instructs renaming through PATHS.tsv. Retiring only identifiers
    that DISAPPEAR meant the freed slug never entered the ledger and was
    available to the next compound that slugified to it — the one slug-changing
    operation the docs prescribe was the one the ledger did not cover."""
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch,
                             [("CHEBI:1", "ANTIBACTERIAL", "erythromycin-a")])
    sfs.write_lockfile({"CHEBI:1": {"antimicrobial_class": "ANTIBACTERIAL"}},
                       {"CHEBI:1": "erythromycin"})
    assert "erythromycin-a" in set(sfs.read_retired().values())


def test_two_identifiers_never_receive_the_same_slug(tmp_path, monkeypatch):
    """A reclaim from the ledger did not check whether the slug had been taken
    since. Two records in one class directory would then overwrite each other on
    write, with the integrity test only noticing afterwards."""
    import pytest

    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch,
                             [("CHEBI:9", "ANTIBACTERIAL", "beta")],
                             [("CHEBI:2", "beta")])
    records = {"CHEBI:9": {"antimicrobial_class": "ANTIBACTERIAL", "label": "nine"},
               "CHEBI:2": {"antimicrobial_class": "ANTIFUNGAL", "label": "two"}}
    assigned = sfs.assign_slugs(records, sfs.read_lockfile())
    assert assigned["CHEBI:9"] == "beta"
    assert assigned["CHEBI:2"] != "beta", "a taken slug must not be reclaimed"

    # And a lockfile that already contains a duplicate is refused outright.
    sfs2, _ = _ledger_sandbox(tmp_path / "second", monkeypatch,
                              [("CHEBI:9", "ANTIBACTERIAL", "beta"),
                               ("CHEBI:8", "ANTIFUNGAL", "beta")])
    with pytest.raises(SystemExit, match="slug collision"):
        sfs2.assign_slugs(records | {"CHEBI:8": {"antimicrobial_class": "ANTIFUNGAL",
                                                 "label": "eight"}},
                          sfs2.read_lockfile())



def test_the_ledger_holds_through_repeated_renames_and_a_return(tmp_path, monkeypatch):
    """The composite-key scheme's whole contract, in sequence. Each step was
    checked by hand once; this keeps it checked.

    A renamed identifier's old slug is reserved under `identifier#slug` so it is
    never reissued, a second rename reserves the second slug too, a departure
    reserves the current slug under the plain key, a return reclaims that slug
    and clears only the plain key — and a different compound whose label
    slugifies to a retired string gets a suffixed slug instead of inheriting a
    published URL.
    """
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch, [("A:1", "ANTIBACTERIAL", "alpha")])
    record = {"A:1": {"antimicrobial_class": "ANTIBACTERIAL"}}

    sfs.write_lockfile(record, {"A:1": "beta"})
    assert sfs.read_retired() == {"A:1#alpha": "alpha"}

    sfs.write_lockfile(record, {"A:1": "gamma"})
    assert set(sfs.read_retired()) == {"A:1#alpha", "A:1#beta"}

    sfs.write_lockfile({}, {})
    assert sfs.read_retired()["A:1"] == "gamma"

    reclaimed = sfs.assign_slugs(record, sfs.read_lockfile())
    assert reclaimed == {"A:1": "gamma"}
    sfs.write_lockfile(record, reclaimed)
    assert "A:1" not in sfs.read_retired()
    assert set(sfs.read_retired()) == {"A:1#alpha", "A:1#beta"}

    contender = record | {"B:2": {"antimicrobial_class": "ANTIFUNGAL", "label": "alpha"}}
    assert sfs.assign_slugs(contender, sfs.read_lockfile())["B:2"] != "alpha"


def test_a_canary_does_not_unretire_identifiers_it_did_not_write(tmp_path, monkeypatch):
    """Both ledger defects were invisible to a green suite because every existing
    test exercised the INSIDE of the `--only` set. This one and
    `test_a_rename_and_a_revert_do_not_wedge_the_gate` hold that line only as
    long as they keep testing the outside of it — keep A:3 unnamed by `only`.

    `records` is the FULL built set even on a partial run — `--only` narrows
    what is WRITTEN, not what is built. Un-retiring on the strength of the
    in-memory set dropped every returning identifier from the ledger while
    writing a PATHS.tsv row for just one, leaving the rest in neither file with
    their published slugs reserved nowhere."""
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch, [("A:1", "ANTIBACTERIAL", "alpha")],
                             [("A:2", "beta"), ("A:3", "gamma")])
    records = {i: {"antimicrobial_class": "ANTIBACTERIAL"} for i in ("A:1", "A:2", "A:3")}
    sfs.write_lockfile(records, {"A:1": "alpha", "A:2": "beta", "A:3": "gamma"}, only={"A:2"})

    paths, retired = sfs.read_lockfile(), sfs.read_retired()
    assert "A:2" in paths and "A:2" not in retired      # the one the canary wrote
    assert "A:3" not in paths, "the canary must not write records it was not asked for"
    assert "A:3" in retired, "and must not unreserve their slugs either"


def test_a_rename_and_a_revert_do_not_wedge_the_gate(tmp_path, monkeypatch):
    """The composite row is deliberately never revived — except when the
    identifier takes its old slug back. A rename followed by a revert otherwise
    leaves the ledger claiming a live URL is retired, which
    test_retired_slugs_are_never_reissued rejects, with no code path able to
    clear it: the gate stays red until someone hand-edits RETIRED.tsv."""
    sfs, _ = _ledger_sandbox(tmp_path, monkeypatch, [("A:1", "ANTIBACTERIAL", "erythromycin-a")])
    record = {"A:1": {"antimicrobial_class": "ANTIBACTERIAL"}}

    sfs.write_lockfile(record, {"A:1": "erythromycin"})
    assert sfs.read_retired() == {"A:1#erythromycin-a": "erythromycin-a"}

    sfs.write_lockfile(record, {"A:1": "erythromycin-a"})          # the curator reverts
    live = set(sfs.read_lockfile().values())
    assert not [k for k, v in sfs.read_retired().items() if v in live], \
        "a slug a record currently holds must not also be listed as retired"
    assert sfs.read_retired() == {"A:1#erythromycin": "erythromycin"}


def test_mode_of_action_restates_a_chebi_role_rather_than_inferring_one():
    """The distinction that makes this safe where the structural-class map was
    not: ChEBI asserting `protein synthesis inhibitor` as a ROLE is a direct
    claim about what the compound does. The map only translates that claim into
    the schema's vocabulary."""
    from seed_from_sources import mode_of_action_from_roles

    names = {"CHEBI:48001": "protein synthesis inhibitor",
             "CHEBI:37416": "EC 2.7.7.6 (RNA polymerase) inhibitor"}
    value, notes, scope = mode_of_action_from_roles(["CHEBI:48001"], CONF, names)
    assert value == "PROTEIN_SYNTHESIS_INHIBITION"
    assert "CHEBI:48001" in notes and "protein synthesis inhibitor" in notes
    # The limit is stated, not papered over — and it is stated SPECIFICALLY.
    # This caveat used to be one sentence identical on every seeded record,
    # which carries no signal precisely because it is uniform (#60). It now
    # names which way this record leans, and the field carries it as data.
    assert "the host has too" in notes
    assert "not evidence of selectivity" in notes
    assert scope == "HOST_SHARED_TARGET"

    assert mode_of_action_from_roles([], CONF, names) is None
    assert mode_of_action_from_roles(["CHEBI:99999999"], CONF, names) is None


def test_several_mechanisms_give_MULTIPLE_with_all_of_them_named():
    """Rifampicin carries both an RNA-polymerase and a protein-synthesis role in
    ChEBI. Picking one silently would assert a primary mechanism no source
    states; MULTIPLE with both named leaves that to a curator."""
    from seed_from_sources import mode_of_action_from_roles

    names = {"CHEBI:48001": "protein synthesis inhibitor",
             "CHEBI:37416": "EC 2.7.7.6 (RNA polymerase) inhibitor"}
    value, notes, _ = mode_of_action_from_roles(["CHEBI:37416", "CHEBI:48001"], CONF, names)
    assert value == "MULTIPLE"
    assert "PROTEIN_SYNTHESIS_INHIBITION" in notes
    assert "NUCLEIC_ACID_SYNTHESIS_INHIBITION" in notes


def test_a_curators_mode_of_action_outranks_the_seeded_one():
    """Seeded values carry a marker and a re-seed may replace them; a curator's
    value carries none and must survive, the same device the CARD items use."""
    from seed_from_sources import MOA_NOTE_MARKER, merge_with_existing

    seeded = {"identifier": "CHEBI:1", "label": "x", "antimicrobial_class": "ANTIBACTERIAL",
              "curation_status": "SEEDED", "grounding_status": "EXACT",
              "mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
              "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:48001 (...)",
              "curation_history": []}

    # The curator claims the field in the notes — a bare value does not, because
    # a value with no notes is indistinguishable from a hand-falsified one.
    curated = dict(seeded) | {
        "mode_of_action": "MEMBRANE_DISRUPTION",
        "mode_of_action_notes": "CURATOR: acts on the envelope (PMID:1)"}
    assert merge_with_existing(seeded, curated)["mode_of_action"] == "MEMBRANE_DISRUPTION"

    # A previously seeded value is the seeder's to correct.
    restated = merge_with_existing(seeded, dict(seeded))
    assert restated["mode_of_action"] == "PROTEIN_SYNTHESIS_INHIBITION"


def test_a_mechanism_from_another_activity_says_so():
    """`mode_of_action` and `antimicrobial_class` are orthogonal axes, and some
    role names carry a target group inside them. A compound filed ANTIFUNGAL
    whose ChEBI role is `HIV-1 integrase inhibitor` is not a contradiction — it
    is one compound with two activities — but a record that states the mechanism
    without stating that would read as a claim about how its antifungal action
    works."""
    from seed_from_sources import mode_of_action_from_roles

    names = {"CHEBI:67268": "HIV-1 integrase inhibitor",
             "CHEBI:48001": "protein synthesis inhibitor"}

    value, notes, _ = mode_of_action_from_roles(["CHEBI:67268"], CONF, names, "ANTIFUNGAL")
    assert value == "VIRAL_INTEGRASE_INHIBITION"
    assert "ANTIFUNGAL" in notes
    # It does NOT assert two activities: the filing may simply be wrong, which
    # has happened — the priority table has put azole antifungals under
    # ANTIBACTERIAL. The note puts both readings to a curator.
    assert "or the filing is wrong" in notes

    # On a record filed under the group the mechanism implies, no such caveat.
    _, aligned, _scope = mode_of_action_from_roles(["CHEBI:67268"], CONF, names, "ANTIVIRAL")
    assert "filing is wrong" not in aligned

    # A mechanism that names no target group never triggers it.
    _, generic, _scope = mode_of_action_from_roles(["CHEBI:48001"], CONF, names, "ANTIFUNGAL")
    assert "filing is wrong" not in generic

    # An unspecified record gets a different sentence: "two activities" would
    # assert a second activity no source states.
    _, unspec, _scope = mode_of_action_from_roles(["CHEBI:67268"], CONF, names,
                                          "ANTIMICROBIAL_UNSPECIFIED")
    assert "no target group stated" in unspec


def test_a_curator_can_correct_a_seeded_mode_of_action_by_appending():
    """The seeded note asks a curator to confirm the value, so appending to that
    note is the obvious way to answer — and inferring ownership from the ABSENCE
    of the seeder's marker meant the marker survived the append, the correction
    was reverted and the curator's citation was deleted."""
    from seed_from_sources import CURATOR_NOTE_MARKER, MOA_NOTE_MARKER, merge_with_existing

    base = {"identifier": "CHEBI:1", "label": "x", "antimicrobial_class": "ANTIBACTERIAL",
            "curation_status": "SEEDED", "grounding_status": "EXACT", "curation_history": []}
    seeded = dict(base) | {"mode_of_action": "VIRAL_INTEGRASE_INHIBITION",
                           "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:67268 (...)"}
    corrected = dict(seeded) | {
        "mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
        "mode_of_action_notes": (f"{MOA_NOTE_MARKER} CHEBI:67268 (...). "
                                 f"{CURATOR_NOTE_MARKER} corrected, see PMID:123"),
    }
    merged = merge_with_existing(dict(seeded), corrected)
    assert merged["mode_of_action"] == "PROTEIN_SYNTHESIS_INHIBITION"
    assert "PMID:123" in merged["mode_of_action_notes"]


def test_a_curator_can_veto_a_mode_of_action_entirely():
    """The only remedy for a wrong derived value, and it was impossible: a
    deleted field failed the `"mode_of_action" in existing` test, so the seeder
    wrote the wrong value straight back on the next run."""
    from seed_from_sources import CURATOR_NOTE_MARKER, MOA_NOTE_MARKER, merge_with_existing

    base = {"identifier": "CHEBI:1", "label": "cefdinir", "antimicrobial_class": "ANTIBACTERIAL",
            "curation_status": "SEEDED", "grounding_status": "EXACT", "curation_history": []}
    seeded = dict(base) | {"mode_of_action": "FOLATE_PATHWAY_INHIBITION",
                           "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:50683 (...)"}
    vetoed = dict(base) | {"mode_of_action_notes":
                           f"{CURATOR_NOTE_MARKER} a cephalosporin; the derived value was wrong"}

    merged = merge_with_existing(dict(seeded), vetoed)
    assert "mode_of_action" not in merged
    assert "derived value was wrong" in merged["mode_of_action_notes"]


def test_a_mechanism_borrowed_from_another_compound_is_not_used():
    """CARD points cefdinir at CHEBI:131724, which is iclaprim, a dihydrofolate
    reductase inhibitor. Reading mechanism roles off a cross-referenced row gave
    a cephalosporin FOLATE_PATHWAY_INHIBITION while its own CARD target, on the
    same record, was a penicillin-binding protein."""
    import csv as _csv
    import pathlib

    raw = pathlib.Path(__file__).resolve().parents[1] / "data" / "raw" / "chebi_antimicrobials.tsv"
    with raw.open(newline="", encoding="utf-8") as fh:
        rows = {r["chebi_id"]: r for r in _csv.DictReader(fh, delimiter="\t")}

    # ChEBI's own cefdinir row asserts no mechanism role...
    if "CHEBI:3485" in rows:
        assert rows["CHEBI:3485"]["mechanism_role_ids"] == ""
    # ...so the record must not carry one.
    record = pathlib.Path(__file__).resolve().parents[1] / "data" / "antibiotics" / \
        "antibacterial" / "cefdinir.yaml"
    if record.exists():
        assert "mode_of_action:" not in record.read_text(encoding="utf-8")


def test_the_curator_marker_must_begin_a_sentence_not_merely_appear():
    """A bare substring test made "ask a CURATOR: about this later" — the kind of
    thing that lands in a free-text note — a permanent, silent veto that locked
    the seeder out of the field for good. The marker has to be a claim, not a
    mention."""
    from seed_from_sources import CURATOR_NOTE_MARKER, MOA_NOTE_MARKER, merge_with_existing

    base = {"identifier": "CHEBI:1", "label": "x", "antimicrobial_class": "ANTIBACTERIAL",
            "curation_status": "SEEDED", "grounding_status": "EXACT", "curation_history": []}
    seeded = dict(base) | {"mode_of_action": "VIRAL_INTEGRASE_INHIBITION",
                           "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:67268 (...)"}

    # A mention IS the point of this test, so the token must be present and must
    # still not claim the field. An earlier edit replaced this input with one
    # containing no token at all, which quietly stopped exercising the boundary:
    # the test then passed against the naive substring predicate it exists to
    # rule out.
    mention = dict(base) | {
        "mode_of_action_notes": f"{MOA_NOTE_MARKER} X. Ask a CURATOR: about this later"}
    assert merge_with_existing(dict(seeded), mention)["mode_of_action"] == \
        "VIRAL_INTEGRASE_INHIBITION"

    for claim in (f"{CURATOR_NOTE_MARKER} wrong, leave blank",
                  f"{MOA_NOTE_MARKER} X. {CURATOR_NOTE_MARKER} wrong, leave blank",
                  f"{MOA_NOTE_MARKER} X\n{CURATOR_NOTE_MARKER} wrong"):
        merged = merge_with_existing(dict(seeded), dict(base) | {"mode_of_action_notes": claim})
        assert "mode_of_action" not in merged, claim


def test_a_mitochondrial_mechanism_applies_to_fungi_and_not_to_bacteria():
    """A mitochondrion is a eukaryotic organelle, so the same ChEBI role is a
    correct mechanism for a fungus and an incoherent one for a bacterium.

    Mapping it unconditionally gave CORM 3, myxothiazole and sodium azide an
    energy-metabolism mechanism on ANTIBACTERIAL records. Removing it outright
    was the opposite error and stripped 23 antifungals of a mechanism that is
    exactly right — the strobilurin and SDHI fungicides work by inhibiting
    FUNGAL mitochondrial respiration.
    """
    from seed_from_sources import mode_of_action_from_roles

    names = {"CHEBI:38499": "mitochondrial cytochrome-bc1 complex inhibitor"}

    fungal = mode_of_action_from_roles(["CHEBI:38499"], CONF, names, "ANTIFUNGAL")
    assert fungal is not None and fungal[0] == "ENERGY_METABOLISM_INHIBITION"

    protozoal = mode_of_action_from_roles(["CHEBI:38499"], CONF, names, "ANTIPROTOZOAL")
    assert protozoal is not None

    assert mode_of_action_from_roles(["CHEBI:38499"], CONF, names, "ANTIBACTERIAL") is None
    assert mode_of_action_from_roles(["CHEBI:38499"], CONF, names,
                                     "ANTIMICROBIAL_UNSPECIFIED") is None


def test_role_maps_agree_with_the_schema_and_the_committed_inventory():
    """The gate that would have caught a whole class of defect. conf and the
    inventory silently desynced twice: roles moved into the eukaryotic map
    vanished from `mechanism_role_ids` on the next extraction, and two roles
    ADDED to the map were dead on arrival because nothing re-extracted — so a
    fix that recovered nothing looked applied."""
    import csv as _csv
    import pathlib

    import yaml as _yaml

    root = pathlib.Path(__file__).resolve().parents[1]
    conf = _yaml.safe_load((root / "conf" / "sources.yaml").read_text(encoding="utf-8"))
    base = conf["role_to_mode_of_action"]
    euk = conf.get("role_to_mode_of_action_eukaryotic", {})

    schema = _yaml.safe_load(
        (root / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml").read_text())
    allowed = set(schema["enums"]["ModeOfActionEnum"]["permissible_values"])
    for role, value in {**base, **euk}.items():
        assert value in allowed, f"{role} -> {value} is not a ModeOfActionEnum value"

    # Disjoint, or `mapping.update(euk)` would let the conditional value win
    # silently over the unconditional one.
    assert not (set(base) & set(euk)), sorted(set(base) & set(euk))

    with (root / "data" / "raw" / "chebi_role_names.tsv").open(newline="", encoding="utf-8") as fh:
        named = {r["role_id"] for r in _csv.DictReader(fh, delimiter="\t")}
    # Parenthesised deliberately: `-` binds tighter than `|`, so
    # `set(base) | set(euk) - named` is `base | (euk - named)` and would report
    # every base role as missing. That is the third precedence bug found in this
    # repository, after check_source_queue's source detection and the worklist's
    # skip condition, so it gets a name rather than a clever expression.
    mapped = set(base) | set(euk)
    missing = sorted(mapped - named)
    assert not missing, f"mapped roles absent from the role-name inventory: {missing}"

    # And every mapped role must actually reach the inventory's mechanism column,
    # or the map entry is inert.
    with (root / "data" / "raw" / "chebi_antimicrobials.tsv").open(
            newline="", encoding="utf-8") as fh:
        seen = set()
        for row in _csv.DictReader(fh, delimiter="\t"):
            seen.update((row["mechanism_role_ids"] or "").split("|"))
    inert = sorted((set(base) | set(euk)) - seen)
    assert not inert, f"mapped roles that reach no compound — re-extract? {inert}"


def test_ownership_is_decided_by_the_notes_not_by_a_bare_value():
    """Three consumers ask "who owns this field?" — the merge, verify-corpus and
    the worklist — and they drifted apart. One predicate now, and a value with
    NO notes is the seeder's: a hand-falsified mechanism with the notes line
    deleted used to read as the curator's and freeze permanently."""
    from seed_from_sources import (
        MOA_NOTE_MARKER,
        curator_owns_mode_of_action,
        seeded_mode_of_action,
    )

    assert not curator_owns_mode_of_action({"mode_of_action": "MEMBRANE_DISRUPTION"})
    assert seeded_mode_of_action({"mode_of_action": "MEMBRANE_DISRUPTION"}) == "MEMBRANE_DISRUPTION"

    seeded = {"mode_of_action": "X", "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:1 (...)"}
    assert not curator_owns_mode_of_action(seeded)

    # The documented recipe: keep the provenance, append the claim.
    appended = {"mode_of_action": "Y",
                "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:1 (...). CURATOR: fixed"}
    assert curator_owns_mode_of_action(appended)
    assert seeded_mode_of_action(appended) is None

    # A curator's prose with no marker at all still claims the field, so it is
    # not deleted on the next run.
    assert curator_owns_mode_of_action({"mode_of_action_notes": "mechanism unclear, PMID:9"})

    # A folded YAML scalar joins lines with a space; the claim must survive that.
    assert curator_owns_mode_of_action(
        {"mode_of_action_notes": f"{MOA_NOTE_MARKER} X; CURATOR: leave blank"})


def test_a_genuine_reseed_always_appends_an_event():
    """No de-duplication pass may sit on the merge path.

    `merge_with_existing` appends a RESEEDED event only when a seeded field
    actually moved, so the `unchanged` guard is already the duplicate
    suppressor. Any further collapse can therefore only delete events that
    record real changes — and `changes` is a constant string, so it cannot tell
    two re-seeds apart. One did exactly that: it removed the events recording 13
    genuine mechanism assignments, and would have swallowed every subsequent
    ChEBI release the same way, leaving trails asserting nothing had happened
    since months before the data moved (#73).

    A second re-seed here carries a description identical to the first. That is
    the shape that was being collapsed, and it must survive.
    """
    from seed_from_sources import SEEDER_CURATOR, merge_with_existing

    def reseed(existing, record):
        return merge_with_existing(existing, dict(record))

    def concepts(version):
        return [{"source": "CHEBI", "source_id": "CHEBI:1", "source_label": "widgetmycin",
                 "minted_identifier": "antibioticmech:chebi-1", "source_version": version}]

    base = {"identifier": "antibioticmech:chebi-1", "label": "widgetmycin",
            "source_concepts": concepts("2026-03-01"),
            "curation_history": [
                {"timestamp": "2026-01-01T00:00:00Z", "curator": SEEDER_CURATOR,
                 "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories"},
                {"timestamp": "2026-03-01T00:00:00Z", "curator": SEEDER_CURATOR,
                 "action": "RESEEDED_FROM_SOURCES",
                 "changes": "Re-seeded from updated data/raw/ inventories"},
            ]}

    # A later release moves a seeded field. The trail must say so, even though
    # the previous entry is a seeder re-seed carrying the same description.
    moved = dict(base, source_concepts=concepts("2026-09-01"))
    merged = reseed(base, moved)
    assert len(merged["curation_history"]) == 3, \
        "a genuine re-seed was swallowed as a duplicate of the one before it"
    assert merged["curation_history"][-1]["action"] == "RESEEDED_FROM_SOURCES"

    # And an idempotent re-run still appends nothing: that is the `unchanged`
    # guard's job, and removing the collapse must not resurrect per-run churn.
    assert len(reseed(base, dict(base))["curation_history"]) == 2


def test_no_history_deduplication_on_the_merge_path():
    """Guards the absence, not just the behaviour.

    The defect was reintroduced once already by a fix written to clean up a
    one-time data problem. A function that filters curation_history inside the
    seeder is the shape to keep out, whatever it is named.
    """
    import ast
    import inspect

    import seed_from_sources

    source = inspect.getsource(seed_from_sources)
    banned = {"_collapse_duplicate_events", "_dedupe_history", "_collapse_history"}
    defined = {node.name for node in ast.walk(ast.parse(source))
               if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
    assert not (banned & defined), (
        f"{sorted(banned & defined)} is back on the seeder. An event is only "
        "appended when a seeded field moved, so deleting one deletes a real "
        "change (#73).")


def _conf():
    from pathlib import Path

    import yaml
    root = Path(__file__).resolve().parent.parent
    return yaml.safe_load((root / "conf" / "sources.yaml").read_text(encoding="utf-8"))


def test_every_mapped_role_declares_a_target_scope():
    """A role that maps to a mechanism but has no scope would emit a mechanism
    with no statement of whose target it is. The seeder raises rather than
    guessing, and this catches it at the config rather than mid-run."""
    conf = _conf()
    mapped = set(conf["role_to_mode_of_action"]) | set(conf["role_to_mode_of_action_eukaryotic"])
    scoped = set(conf["role_target_scope"])
    assert mapped - scoped == set(), f"mapped but unscoped: {sorted(mapped - scoped)}"
    assert scoped - mapped == set(), f"scoped but unmapped (dead entry): {sorted(scoped - mapped)}"
    assert set(conf["role_target_scope"].values()) <= {"MICROBIAL_TARGET", "HOST_SHARED_TARGET"}


def test_a_specific_role_outranks_a_generic_one_for_target_scope():
    """Ciprofloxacin is the case that decides the rule.

    It carries `topoisomerase IV inhibitor` — a target bacteria have and the
    host does not — AND the generic `DNA synthesis inhibitor`. Taking the
    host-shared reading whenever any role is generic put the most selective
    antibacterial class there is on the wrong side of the filter this field
    exists to support. A specific role subsumes a generic one.
    """
    from seed_from_sources import mode_of_action_from_roles

    conf = _conf()
    names = {"CHEBI:53559": "topoisomerase IV inhibitor",
             "CHEBI:59517": "DNA synthesis inhibitor",
             "CHEBI:48001": "protein synthesis inhibitor"}

    both = mode_of_action_from_roles(["CHEBI:59517", "CHEBI:53559"], conf, names, "ANTIBACTERIAL")
    assert both[2] == "MICROBIAL_TARGET", both

    # Order must not matter.
    assert mode_of_action_from_roles(
        ["CHEBI:53559", "CHEBI:59517"], conf, names, "ANTIBACTERIAL")[2] == "MICROBIAL_TARGET"

    # Only generic roles: nothing names a microbe-specific target, so the
    # question of selectivity is open and the flag says so.
    only_generic = mode_of_action_from_roles(["CHEBI:48001"], conf, names, "ANTIVIRAL")
    assert only_generic[2] == "HOST_SHARED_TARGET", only_generic
    assert "host has too" in only_generic[1], only_generic[1]


def test_an_unscoped_role_raises_rather_than_emitting_a_bare_mechanism():
    """Adding a role to the mechanism map and forgetting the scope map is the
    obvious way to reintroduce the conflation this field removes. Silently
    defaulting would assert the safe-looking value; the seeder refuses."""
    import pytest
    from seed_from_sources import mode_of_action_from_roles

    conf = _conf()
    conf = dict(conf, role_to_mode_of_action=dict(conf["role_to_mode_of_action"],
                                                  **{"CHEBI:99999999": "MEMBRANE_DISRUPTION"}))
    with pytest.raises(KeyError, match="role_target_scope"):
        mode_of_action_from_roles(["CHEBI:99999999"], conf,
                                  {"CHEBI:99999999": "invented"}, "ANTIBACTERIAL")


def test_a_curator_who_claims_the_mechanism_owns_its_target_scope_too():
    """The scope describes the value. Leaving the seeder's scope beside a
    curator's corrected mechanism would attach a derivation to a value it was
    never derived from — a provenance claim about work the curator did."""
    from seed_from_sources import merge_with_existing

    seeded = {"identifier": "CHEBI:1", "label": "widgetmycin",
              "mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
              "mode_of_action_notes": "Assigned from ChEBI role CHEBI:48001 (x).",
              "mode_of_action_target_scope": "HOST_SHARED_TARGET",
              "source_concepts": []}

    curated = dict(seeded,
                   mode_of_action="MEMBRANE_DISRUPTION",
                   mode_of_action_notes="CURATOR: reassigned after reading the primary literature.",
                   mode_of_action_target_scope="MICROBIAL_TARGET")

    merged = merge_with_existing(curated, dict(seeded))
    assert merged["mode_of_action"] == "MEMBRANE_DISRUPTION"
    assert merged["mode_of_action_target_scope"] == "MICROBIAL_TARGET"

    # A curator VETO (note, no value) must not leave a scope stranded behind,
    # describing a mechanism that is no longer asserted.
    veto = {k: v for k, v in curated.items()
            if k not in ("mode_of_action", "mode_of_action_target_scope")}
    veto["mode_of_action_notes"] = "CURATOR: the cited role is wrong for this compound."
    merged_veto = merge_with_existing(veto, dict(seeded))
    assert "mode_of_action" not in merged_veto
    assert "mode_of_action_target_scope" not in merged_veto

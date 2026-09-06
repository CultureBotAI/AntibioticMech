"""Corpus-wide invariants no single-record validation can see."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")
INCHIKEY = re.compile(r"^[A-Z]{14}-[A-Z]{10}-[A-Z]$")

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seed_from_sources import CLASS_DIRS  # noqa: E402


def test_identifiers_are_unique(records):
    counts = Counter(r["identifier"] for _, r in records)
    assert [i for i, n in counts.items() if n > 1] == []


def test_every_record_has_a_structure(records):
    """A record IS a chemical structure. Without an InChIKey there is nothing to
    assert identity on, and the record should never have been written."""
    missing = [p.name for p, r in records
               if not (r.get("chemical_structure") or {}).get("standard_inchi_key")]
    assert missing == [], missing[:20]


def test_inchikeys_are_well_formed(records):
    malformed = [(p.name, r["chemical_structure"]["standard_inchi_key"]) for p, r in records
                 if not INCHIKEY.match(r["chemical_structure"]["standard_inchi_key"])]
    assert malformed == [], malformed[:10]


def test_a_minted_record_never_duplicates_a_grounded_structure(records):
    """The merge rule that matters. ChEBI itself keeps entries that share an
    InChIKey — a compound and its zwitterion, or two names for one structure
    curated separately — and collapsing those would overrule ChEBI. What must
    never happen is an ARO concept becoming a second, minted record for a
    structure ChEBI already grounds: that is a failure of identity resolution,
    not an upstream modelling choice.

    See docs/HARMONIZATION.md for why the weaker invariant is the correct one.
    """
    by_key = defaultdict(list)
    for _, record in records:
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(record)
    offenders = []
    for key, group in by_key.items():
        if len(group) < 2:
            continue
        statuses = {r.get("grounding_status") for r in group}
        if "MINTED" in statuses and "EXACT" in statuses:
            offenders.append((key, [(r["identifier"], r["grounding_status"]) for r in group]))
    assert offenders == [], offenders[:10]


def test_minted_structure_collisions_are_flagged_for_curation(records):
    """Two minted records sharing a structure is a real upstream conflict; the
    seeder must leave a visible curation todo on both rather than let the
    duplicate pass silently."""
    by_key = defaultdict(list)
    for _, record in records:
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(record)
    unflagged = []
    for key, group in by_key.items():
        if len(group) < 2 or not all(r.get("grounding_status") == "MINTED" for r in group):
            continue
        for record in group:
            todos = [d for d in record.get("discussions") or []
                     if str(d.get("discussion_id", "")).startswith("structure-collision")]
            if not todos:
                unflagged.append((record["identifier"], key))
    assert unflagged == [], unflagged[:10]


def test_structures_shared_between_grounded_records_stay_rare(records):
    """A guard rail, not a rule: ChEBI-internal InChIKey collisions are expected
    but should stay a curated handful. A jump means the extractor started
    pulling in entries ChEBI does not intend as distinct structures."""
    by_key = defaultdict(list)
    for _, record in records:
        by_key[record["chemical_structure"]["standard_inchi_key"]].append(record["identifier"])
    shared = {k: v for k, v in by_key.items() if len(v) > 1}
    assert len(shared) <= 40, f"{len(shared)} shared InChIKeys: {list(shared.items())[:10]}"


def test_file_location_matches_the_declared_class(records):
    wrong = [(p.name, r["antimicrobial_class"], p.parent.name) for p, r in records
             if p.parent.name != CLASS_DIRS[r["antimicrobial_class"]]]
    assert wrong == [], wrong[:20]


def test_slug_matches_the_lockfile(records, path_lockfile):
    """Slugs are published URLs. A record whose filename disagrees with
    PATHS.tsv means a rename happened outside the lockfile."""
    mismatched = [(p.name, path_lockfile.get(r["identifier"]))
                  for p, r in records if p.stem != path_lockfile.get(r["identifier"])]
    assert mismatched == [], mismatched[:20]


def test_every_curie_field_is_a_curie(records):
    bad = []
    for path, record in records:
        candidates = [record["identifier"]]
        candidates += record.get("parent_compounds") or []
        candidates += record.get("xrefs") or []
        candidates += record.get("activity_roles") or []
        for concept in record.get("source_concepts") or []:
            candidates.append(concept["minted_identifier"])
        for value in candidates:
            if not CURIE.match(value):
                bad.append((path.name, value))
    assert bad == [], bad[:20]


def test_mechanistic_claims_carry_evidence(records):
    """Classification is inherited from ChEBI/CARD; mechanism is asserted. Every
    target, resistance route, activity observation and causal edge must say
    where it came from."""
    unsupported = []
    for path, record in records:
        for item in record.get("molecular_targets") or []:
            if not item.get("evidence"):
                unsupported.append((path.name, "molecular_target", item.get("target_label")))
        for item in record.get("resistance_mechanisms") or []:
            if not item.get("evidence"):
                unsupported.append((path.name, "resistance_mechanism", item.get("label")))
        for item in record.get("activity_spectrum") or []:
            if not item.get("evidence"):
                unsupported.append((path.name, "activity_observation", item.get("taxon_label")))
        for graph in record.get("causal_graphs") or []:
            for edge in graph.get("edges") or []:
                if not edge.get("evidence"):
                    unsupported.append((path.name, "causal_edge", edge.get("predicate")))
    assert unsupported == [], unsupported[:20]


def test_mibig_producers_are_reviewed_and_fully_provenanced(records):
    """Every imported producer is a reviewed, versioned MIBiG+BGC assertion."""
    problems = []
    for path, record in records:
        for producer in record.get("producer_organisms") or []:
            if producer.get("source") != "MIBIG":
                continue
            required = (
                "taxon_id",
                "taxon_label",
                "biosynthetic_gene_cluster",
                "source_version",
                "source_record_version",
                "source_quality",
                # `reference` was a scalar PMID/DOI that could not say what the
                # citation was FOR; #94 replaced it with structured evidence
                # carrying MIBiG's own reference basis in `notes`.
                "evidence",
            )
            missing = [field for field in required if not producer.get(field)]
            if not all(e.get("reference") and e.get("notes")
                       for e in producer.get("evidence") or []):
                missing.append("evidence[].reference+notes")
            if missing or producer.get("reviewed") is not True:
                problems.append((path.name, missing, producer.get("reviewed")))
    assert problems == [], problems[:20]


def test_causal_graph_edges_reference_declared_nodes(records):
    dangling = []
    for path, record in records:
        for graph in record.get("causal_graphs") or []:
            nodes = {n["node_id"] for n in graph.get("nodes") or []}
            for edge in graph.get("edges") or []:
                for role in ("subject", "object"):
                    if edge.get(role) not in nodes:
                        dangling.append((path.name, graph.get("graph_id"), edge.get(role)))
    assert dangling == [], dangling[:20]


def test_mic_values_carry_units(records):
    """A number without units is not a measurement; it is a number."""
    bad = []
    for path, record in records:
        for item in record.get("activity_spectrum") or []:
            if item.get("mic_value") is not None and not item.get("mic_units"):
                bad.append((path.name, item.get("taxon_label")))
    assert bad == [], bad[:20]


def test_every_record_has_a_seed_curation_event(records):
    """The audit trail starts at the seed. A record with no history cannot be
    traced back to the inventory row that produced it."""
    missing = [p.name for p, r in records if not (r.get("curation_history") or [])]
    assert missing == [], missing[:20]


def test_source_concepts_are_present_and_keyed(records):
    problems = []
    for path, record in records:
        concepts = record.get("source_concepts") or []
        if not concepts:
            problems.append((path.name, "no source concepts"))
        for concept in concepts:
            if not concept.get("minted_identifier", "").startswith("antibioticmech:"):
                problems.append((path.name, concept.get("source_id")))
    assert problems == [], problems[:20]


def test_a_record_never_cross_references_itself(records):
    self_ref = [(p.name, r["identifier"]) for p, r in records
                if r["identifier"] in (r.get("xrefs") or [])]
    assert self_ref == [], self_ref[:20]


def test_activity_roles_keep_inherited_roles(records):
    """`activity_roles` is documented as complete and unreduced. Role inheritance
    was previously skipped for any compound that carried a role of its own,
    which cost 455 compounds an ancestor role and misfiled three of them —
    silently, because the corpus reproduced the wrong computation exactly.

    Carvacrol is the canonical case: its own ChEBI edge is `antimicrobial agent`
    and `antifungal agent` comes from its parent. A record holding only one of
    the two means inheritance regressed.
    """
    by_id = {r["identifier"]: r for _, r in records}
    carvacrol = by_id.get("CHEBI:3440")
    if carvacrol is None:
        return  # the compound left the corpus; nothing to assert here
    roles = set(carvacrol.get("activity_roles") or [])
    assert {"CHEBI:33281", "CHEBI:35718"} <= roles, sorted(roles)


def test_card_seeded_items_say_they_came_from_card(records):
    """CLAUDE.md: "A CARD-seeded item cites CARD and says so." The note is also
    the marker that tells a re-seed which items are the seeder's, so a silent
    change to it would start deleting curator work."""
    unmarked = []
    for path, record in records:
        for field in ("molecular_targets", "resistance_mechanisms"):
            for item in record.get(field) or []:
                evidence = item.get("evidence") or []
                if not evidence or not all(
                    str(e.get("reference", "")).startswith("ARO:") for e in evidence
                ):
                    continue  # a curator item; not this test's business
                if not any("CARD/ARO asserts" in str(e.get("notes") or "") for e in evidence):
                    unmarked.append((path.name, field, item.get("label") or item.get("target_label")))
    assert unmarked == [], unmarked[:10]


def test_resistance_mechanisms_are_typed_where_aro_says_so(records):
    """Eight of ten mechanism categories were unassignable while the ancestor
    walk followed only is_a — ANTIBIOTIC_EFFLUX among them, so a consumer
    filtering for efflux got nothing while acrB sat in the data as UNKNOWN."""
    seen = Counter()
    for _, record in records:
        for item in record.get("resistance_mechanisms") or []:
            seen[item.get("mechanism_type")] += 1
    if not seen:
        return
    assert seen["ANTIBIOTIC_EFFLUX"] > 0, dict(seen)
    assert seen["ANTIBIOTIC_TARGET_PROTECTION"] > 0, dict(seen)
    # UNKNOWN is legitimate for a determinant ARO does not classify, but it
    # should be the exception rather than half the corpus.
    assert seen["UNKNOWN"] < sum(seen.values()) * 0.1, dict(seen)


def test_retired_slugs_are_never_reissued(repo_root, path_lockfile):
    """A slug is a published URL. When records leave the corpus their slugs
    leave PATHS.tsv with them and became free for the next compound whose label
    slugified the same way — silently repointing a published URL at a different
    structure. The ledger keeps them reserved."""
    import csv as _csv

    retired_path = repo_root / "data" / "antibiotics" / "RETIRED.tsv"
    if not retired_path.exists():
        return
    with retired_path.open(newline="", encoding="utf-8") as fh:
        retired = {r["identifier"]: r["slug"] for r in _csv.DictReader(fh, delimiter="\t")}

    # No retired identifier is also current: a returning compound must be
    # removed from the ledger and reclaim its own slug, not hold both states.
    both = set(retired) & set(path_lockfile)
    assert both == set(), sorted(both)[:10]

    # No retired slug has been handed to a different compound.
    reissued = [(i, s) for i, s in retired.items() if s in set(path_lockfile.values())]
    assert reissued == [], reissued[:10]


def test_ambiguous_mechanism_determinants_resolve_deterministically(records):
    """The mycobacterial iniA/iniB/iniC determinants have ancestors mapping to
    two different mechanisms, so they are the regression surface if the
    breadth-first sorted walk is ever refactored back to set iteration: the
    answer would then depend on PYTHONHASHSEED and the committed inventory would
    stop being reproducible."""
    seen = {}
    for _, record in records:
        for item in record.get("resistance_mechanisms") or []:
            label = str(item.get("label") or "")
            if label.startswith("ini") or "iniA" in label or "iniC" in label:
                seen.setdefault(item.get("aro_id"), item.get("mechanism_type"))
    for aro_id, mechanism in seen.items():
        assert mechanism in {"ANTIBIOTIC_TARGET_ALTERATION", "ANTIBIOTIC_EFFLUX"}, (aro_id, mechanism)
    if seen:
        # One answer per determinant, corpus-wide — not one per record.
        assert len(set(seen.values())) <= 2


def test_a_seeded_mode_of_action_is_policed_and_a_curators_is_not(repo_root):
    """`mode_of_action` is both seeded and curator-overridable, so verify-corpus
    keys the comparison on what the ON-DISK value claims: a value carrying the
    seeder's note marker must be what the seeder produces, a curator's own value
    carries none and is theirs to set.

    Without this, a hand-edit falsifying a seeded mechanism passed every gate —
    the field was in neither SEEDED_FIELDS nor the CARD views.
    """
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from seed_from_sources import MOA_NOTE_MARKER, seeded_mode_of_action

    seeded = {"mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
              "mode_of_action_notes": f"{MOA_NOTE_MARKER} CHEBI:48001 (...)"}
    assert seeded_mode_of_action(seeded) == "PROTEIN_SYNTHESIS_INHIBITION"

    curated = {"mode_of_action": "MEMBRANE_DISRUPTION",
               "mode_of_action_notes": "curator: acts on the envelope (PMID:1)"}
    assert seeded_mode_of_action(curated) is None

    assert seeded_mode_of_action({}) is None


def test_target_scope_accompanies_every_seeded_mechanism(records):
    """A SEEDED mechanism with no scope is the conflation this field removes:
    `PROTEIN_SYNTHESIS_INHIBITION` alone cannot tell linezolid's bacterial 50S
    from omacetaxine's host 80S. A scope with no mechanism describes nothing,
    whoever set it.

    Scoped to seeder-owned mechanisms deliberately. Once a curator claims
    `mode_of_action`, the seeder cannot derive a scope for their value and must
    not guess, so a curator's mechanism may legitimately carry none — it is
    curation work, and `just worklist --queue moa-scope` is where it is owed.
    Requiring one here made the merge emit a state this gate rejected, turning
    `just qc` red on a curator who had done nothing wrong.
    """
    from seed_from_sources import curator_owns_mode_of_action

    VALID = {"MICROBIAL_TARGET", "HOST_SHARED_TARGET"}
    missing, orphaned, bad = [], [], []
    for path, record in records:
        moa = record.get("mode_of_action")
        scope = record.get("mode_of_action_target_scope")
        if moa and not scope and not curator_owns_mode_of_action(record):
            missing.append(path.name)
        if scope and not moa:
            orphaned.append(path.name)
        if scope and scope not in VALID:
            bad.append(f"{path.name}: {scope}")
    assert missing == [], f"seeded mechanism with no target scope: {missing[:10]}"
    assert orphaned == [], f"target scope with no mechanism: {orphaned[:10]}"
    assert bad == [], bad

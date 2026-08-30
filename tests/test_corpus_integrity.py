"""Corpus-wide invariants no single-record validation can see."""

from __future__ import annotations

import re
from collections import Counter, defaultdict

CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")
INCHIKEY = re.compile(r"^[A-Z]{14}-[A-Z]{10}-[A-Z]$")

CLASS_DIRS = {
    "ANTIBACTERIAL": "antibacterial",
    "ANTIMYCOBACTERIAL": "antimycobacterial",
    "ANTIFUNGAL": "antifungal",
    "ANTIPROTOZOAL": "antiprotozoal",
    "BIOCIDE": "biocide",
    "ANTIMICROBIAL_UNSPECIFIED": "unspecified",
    "OTHER": "other",
}


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

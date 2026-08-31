"""The ARO fallback, and the curated adjudication that keeps it honest.

A molecule in CARD's antibiotic subtree is there for a bacterial reason, so a
CARD concept with no ChEBI role and no group-naming drug class is filed
ANTIBACTERIAL. That is right for 265 of the 276 records the fallback reaches and
wrong for the rest, where CARD's own definition says otherwise — and nothing
caught it: triflumizole sat under ANTIBACTERIAL while its ChEBI-grounded twin
sat under ANTIFUNGAL, one compound under two classes, every gate green (#91).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))


def _conf():
    return yaml.safe_load((REPO_ROOT / "conf" / "sources.yaml").read_text(encoding="utf-8"))


def test_every_override_names_a_real_aro_concept_and_a_real_class():
    """A dead entry adjudicates nothing and would sit unnoticed; a misspelled
    class would fail validation only once a record happened to reach it."""
    conf = _conf()
    overrides = conf["aro_definition_overrides"]
    assert overrides, "no overrides declared; this test guards nothing"

    with (REPO_ROOT / "data" / "raw" / "aro_antibiotics.tsv").open(encoding="utf-8") as fh:
        known = {row["aro_id"] for row in csv.DictReader(fh, delimiter="\t")}
    dead = sorted(set(overrides) - known)
    assert dead == [], f"overrides for ARO concepts not in the inventory: {dead}"

    schema = yaml.safe_load(
        (REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml")
        .read_text(encoding="utf-8"))
    permitted = set(schema["enums"]["AntimicrobialClassEnum"]["permissible_values"])
    assert set(overrides.values()) <= permitted, sorted(set(overrides.values()) - permitted)


def test_the_override_outranks_the_blanket_fallback_but_not_real_evidence():
    """Precedence, asserted rather than described. A curated ARO drug class and
    a ChEBI role are both stronger evidence than an adjudicated definition, and
    must keep winning."""
    from seed_from_sources import classify

    conf = _conf()
    aro_id = "ARO:3009169"                      # triflumizole, adjudicated ANTIFUNGAL

    # No roles, no group-naming drug class: the adjudication decides.
    assert classify([], conf, from_aro=True, aro_ids=(aro_id,)) == "ANTIFUNGAL"

    # An unadjudicated ARO concept still gets the fallback.
    assert classify([], conf, from_aro=True, aro_ids=("ARO:9999999",)) == "ANTIBACTERIAL"

    # A group-naming drug class outranks the adjudication.
    polyene = next(iter(conf["aro_class_to_class"]))
    assert classify([], conf, from_aro=True, aro_class_ids=(polyene,),
                    aro_ids=(aro_id,)) == conf["aro_class_to_class"][polyene]

    # A ChEBI role outranks it too.
    role = next(iter(conf["role_to_class"]))
    assert classify([role], conf, from_aro=True, aro_ids=(aro_id,)) == \
        conf["role_to_class"][role]["class"]

    # Nothing from ARO at all is still UNSPECIFIED, not ANTIBACTERIAL.
    assert classify([], conf, from_aro=False) == "ANTIMICROBIAL_UNSPECIFIED"


def test_no_compound_is_filed_under_two_classes(records):
    """The GENERAL invariant, not the one label that made it visible.

    An earlier version asserted `triflumizole == {"ANTIFUNGAL"}` — a fact about
    the corrected corpus that survives neutering the fix everywhere else, and
    that says nothing about the next compound to arrive under two classes.
    """
    by_label: dict[str, set] = {}
    for _path, record in records:
        by_label.setdefault(record["label"], set()).add(record["antimicrobial_class"])
    split = {label: sorted(classes) for label, classes in by_label.items() if len(classes) > 1}
    assert split == {}, split


def test_the_queue_surfaces_what_is_unadjudicated_and_drops_what_is_not(records):
    """Detection is automatic; assertion is curated. The queue must therefore
    show a candidate no curator has ruled on, and must go quiet once one has —
    otherwise it becomes noise a curator learns to ignore."""
    from curation_worklist import aro_class_queue

    conf = _conf()
    docs = [r for _p, r in records]
    queued = {row["key"] for row in aro_class_queue(docs, conf)}

    adjudicated = {r["identifier"] for r in docs
                   if any(c.get("source_id") in conf["aro_definition_overrides"]
                          for c in (r.get("source_concepts") or []))}
    assert adjudicated, "no record carries an adjudicated ARO concept"
    assert not (queued & adjudicated), sorted(queued & adjudicated)

    # Proof the queue would have CAUGHT them, rather than being quiet for its own
    # reasons: replay the pre-fix state — the adjudicated records back under
    # ANTIBACTERIAL with no override — and require every one to surface.
    # (Stripping the override alone proves nothing: the records on disk now
    # carry the corrected class, so there is no disagreement left to detect.)
    stripped = dict(conf, aro_definition_overrides={})
    replayed = [dict(r, antimicrobial_class="ANTIBACTERIAL") if r["identifier"] in adjudicated
                else r for r in docs]
    caught = {row["key"] for row in aro_class_queue(replayed, stripped)}
    missed = sorted(adjudicated - caught)
    # ophiobolin A is expected to be caught too: the queue flags it, and a
    # curator then rules that "fungal phytotoxins" names a source, not a target.
    assert missed == [], f"the queue would not have surfaced: {missed}"


def test_each_classification_mechanism_is_load_bearing():
    """Every mechanism this PR adds must change an answer, or it is decoration.

    Three of the four original tests survived replacing the override lookup with
    an empty dict, which is the hollow-guard pattern this repo keeps repeating.
    Each assertion below names the record that would regress.
    """
    from seed_from_sources import classify

    conf = _conf()
    empty_overrides = dict(conf, aro_definition_overrides={})
    empty_parents = dict(conf, aro_group_terms={})
    no_biocide = dict(conf, aro_group_terms={
        k: v for k, v in conf["aro_group_terms"].items() if k != "ARO:3005386"})

    # The definition override decides triflumizole (ARO:3009169); without it the
    # blanket fallback files it ANTIBACTERIAL, contradicting CHEBI:81784.
    assert classify([], conf, from_aro=True, aro_ids=("ARO:3009169",)) == "ANTIFUNGAL"
    assert classify([], empty_overrides, from_aro=True,
                    aro_ids=("ARO:3009169",)) == "ANTIBACTERIAL"

    # The group term decides myxothiazole (parent ARO:3009165), whose definition
    # is pure mechanism and names no group at all.
    assert classify([], conf, from_aro=True, aro_ids=("ARO:3009170",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIFUNGAL"
    assert classify([], empty_parents, from_aro=True, aro_ids=("ARO:3009170",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIBACTERIAL"

    # The antiseptic drug class decides thiacalixarene derivatives.
    assert classify([], conf, from_aro=True, aro_class_ids=("ARO:3005386",)) == "BIOCIDE"
    assert classify([], no_biocide, from_aro=True,
                    aro_class_ids=("ARO:3005386",)) == "ANTIBACTERIAL"


def test_a_parent_term_never_overrides_a_chebi_role():
    """Pyrimethamine is the record that decides this map's precedence.

    It is an antimalarial, and CARD files it under "antifungal without defined
    classification". Consulting parents at step 1 — where drug classes sit —
    refiled it ANTIFUNGAL and overrode its correct antiprotozoal role, which is
    the #47 error in a new place. Parents belong below the roles.
    """
    from seed_from_sources import classify

    conf = _conf()
    antiprotozoal = next(r for r, e in conf["role_to_class"].items()
                         if e["class"] == "ANTIPROTOZOAL")
    assert classify([antiprotozoal], conf, from_aro=True, aro_ids=("ARO:3009163",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIPROTOZOAL"
    # And with no role, the parent is exactly what decides.
    assert classify([], conf, from_aro=True, aro_ids=("ARO:3009163",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIFUNGAL"


def test_pyrimethamine_is_still_an_antiprotozoal(records):
    """The corpus-level statement of the same thing."""
    filed = {r["antimicrobial_class"] for _p, r in records if r["label"] == "pyrimethamine"}
    assert filed == {"ANTIPROTOZOAL"}, filed


def test_the_fallback_cohort_figure_in_the_comments_is_current(records):
    """The 265/276 split is quoted in conf, the seeder, the worklist and this
    file. Figures in this repository drift under prose that nobody re-derives
    (#84, #112), so it is derived here instead of trusted.
    """
    from pathlib import Path as _P

    fallback = [r for _p, r in records
                if not r.get("activity_roles")
                and {c.get("source") for c in (r.get("source_concepts") or [])} == {"ARO"}]
    still_antibacterial = [r for r in fallback if r["antimicrobial_class"] == "ANTIBACTERIAL"]
    assert len(still_antibacterial) == 265, len(still_antibacterial)

    root = _P(__file__).resolve().parent.parent
    for name in ("conf/sources.yaml", "scripts/seed_from_sources.py",
                 "scripts/curation_worklist.py"):
        text = (root / name).read_text(encoding="utf-8")
        assert "265 of the 276" in text, f"{name} quotes a stale cohort figure"


def test_a_per_compound_adjudication_outranks_a_group_term():
    """Ordering inside the fallback tier, which would pass every gate if wrong.

    A definition adjudication is about THIS compound; a group term is about a
    bucket it sits in. If the group term ran first, ARO:3009165 ("antifungal
    without defined classification") would overturn an adjudication made by
    reading the compound's own definition.
    """
    from seed_from_sources import classify

    conf = _conf()
    # A synthetic concept in both: adjudicated UNSPECIFIED, and under the
    # antifungal parent. The per-compound answer must win.
    conf = dict(conf,
                aro_definition_overrides={**conf["aro_definition_overrides"],
                                          "ARO:9999998": "ANTIMICROBIAL_UNSPECIFIED"})
    assert classify([], conf, from_aro=True, aro_ids=("ARO:9999998",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIMICROBIAL_UNSPECIFIED"
    # Without the adjudication, the group term decides.
    assert classify([], conf, from_aro=True, aro_ids=("ARO:9999997",),
                    aro_parent_ids=("ARO:3009165",)) == "ANTIFUNGAL"


def test_a_group_term_never_outranks_a_chebi_role(records):
    """The five antiseptics are the record of this.

    Putting the antiseptic drug class at step 1 made BIOCIDE the strongest signal
    for triclosan, benzalkonium chloride, chlorhexidine and 3,6-diaminoacridine,
    reversing the role table's deliberate ranking of `antibacterial agent` above
    `disinfectant` (conf/sources.yaml puts BIOCIDE at priority 6, last, because
    "a biocide role is the least specific thing a source can say"). Only the two
    antiseptics with NO roles should be BIOCIDE by a group term.
    """
    from seed_from_sources import classify

    conf = _conf()
    filed = {r["label"]: r["antimicrobial_class"] for _p, r in records}
    for role_bearing in ("triclosan", "chlorhexidine", "benzalkonium chloride"):
        assert filed.get(role_bearing) == "ANTIBACTERIAL", (role_bearing, filed.get(role_bearing))
    for no_roles in ("acriflavine", "thiacalixarene derivatives"):
        assert filed.get(no_roles) == "BIOCIDE", (no_roles, filed.get(no_roles))

    # And directly: a role beats the group term.
    antibacterial = next(r for r, e in conf["role_to_class"].items()
                         if e["class"] == "ANTIBACTERIAL")
    assert classify([antibacterial], conf, from_aro=True,
                    aro_class_ids=("ARO:3005386",)) == "ANTIBACTERIAL"

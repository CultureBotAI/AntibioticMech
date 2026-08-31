"""The ARO fallback, and the curated adjudication that keeps it honest.

A molecule in CARD's antibiotic subtree is there for a bacterial reason, so a
CARD concept with no ChEBI role and no group-naming drug class is filed
ANTIBACTERIAL. That is right for 266 of the 276 records the fallback reaches and
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


def test_one_compound_is_not_filed_under_two_classes(records):
    """The symptom that made #91 visible: the ARO-minted triflumizole and its
    ChEBI-grounded twin are the same compound and disagreed."""
    by_label: dict[str, set] = {}
    for _path, record in records:
        by_label.setdefault(record["label"], set()).add(record["antimicrobial_class"])
    assert by_label.get("triflumizole") == {"ANTIFUNGAL"}, by_label.get("triflumizole")


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

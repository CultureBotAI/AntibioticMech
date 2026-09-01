"""A record IS one chemical structure. Mixtures and combination products are not.

CLAUDE.md states it and docs/HARMONIZATION.md excludes mixtures explicitly, but a
content-bearing InChIKey was taken as proof that a source concept denotes one
chemical — so trimethoprim-sulfamethoxazole, whose own definition calls it "an
antibiotic cocktail", passed every gate with two disconnected drug components in
its SMILES (#90).
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

HEAVY = re.compile(r"\[[^\]]+\]|Cl|Br|[BCNOPSFIbcnops]")


def _large_fragments(smiles: str) -> list[str]:
    return [f for f in smiles.split(".") if len(HEAVY.findall(f)) >= 10]


def test_no_adjudicated_combination_product_is_in_the_corpus(records):
    """The twelve adjudicated in curation/decisions.tsv must be gone.

    Named individually rather than counted, so removing one from the decisions
    file fails here instead of quietly shrinking a number.
    """
    excluded = {
        "trimethoprim-sulfamethoxazole", "amoxicillin-clavulanic acid",
        "ticarcillin-clavulanic acid", "piperacillin-tazobactam",
        "cefepime-tazobactam", "ceftazidime-avibactam",
        "ceftazidime-clavulanic acid", "meropenem-vaborbactam",
        "quinupristin-dalfopristin", "Kaletra", "capreomycin", "ganefromycin",
    }
    present = {r["label"] for _p, r in records} & excluded
    assert present == set(), sorted(present)


def test_every_exclusion_states_a_reason_and_names_a_real_concept():
    """An EXCLUDE with no rationale is an unexplained deletion, and one naming a
    concept the inventory does not have adjudicates nothing."""
    with (REPO_ROOT / "curation" / "decisions.tsv").open(encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t")
                if (r.get("decision") or "").upper() == "EXCLUDE"]
    assert rows, "no EXCLUDE decisions; this test guards nothing"
    for row in rows:
        assert row.get("rationale", "").strip(), row["minted_identifier"]
        assert row.get("curator", "").strip(), row["minted_identifier"]
        assert row.get("source_id", "").strip(), row["minted_identifier"]
        # `source_label` too: the excluded queue prints it, and a blank one is a
        # row a curator cannot act on. The queue tolerates the omission without
        # crashing, which is exactly why the gate has to catch it here.
        assert row.get("source_label", "").strip(), row["minted_identifier"]
        # And the decision must be written as the seeder reads it — merge()
        # upper-cases before comparing, so a lowercase "exclude" works there,
        # but a mixed corpus of spellings is a trap for the next reader.
        assert row["decision"] == "EXCLUDE", (row["minted_identifier"], row["decision"])


def test_a_stoichiometric_salt_is_still_a_record(records):
    """The rule must not swallow legitimate multi-fragment records.

    Mupirocin calcium is TWO identical mupirocin fragments plus calcium — one
    compound with a counter-ion, not a combination — and doxycycline hyclate and
    quinine sulfate are the same shape. If these disappeared, the exclusion was
    too broad.
    """
    labels = {r["label"] for _p, r in records}
    for salt in ("mupirocin calcium hydrate", "doxycycline hyclate", "quinine sulfate"):
        assert salt in labels, f"{salt} was excluded; the rule is too broad"


def test_the_multi_component_queue_surfaces_what_is_unadjudicated(records):
    """Detection is automatic; exclusion is curated.

    No structural rule separates a combination from a salt: clavulanate is drawn
    as an anion in a genuine combination while tosylate is drawn neutral in a
    genuine salt, so charge misclassifies both ways. The queue therefore lists
    candidates and a curator decides — and an adjudicated record leaves the
    corpus, so it stops being listed.
    """
    from curation_worklist import multi_component_queue

    docs = [r for _p, r in records]
    queued = {row["label"] for row in multi_component_queue(docs)}
    assert queued, "the queue is empty; either the corpus changed or it stopped detecting"

    # Every queued record really does have two distinct large fragments...
    by_label = {r["label"]: r for r in docs}
    for label in queued:
        smiles = (by_label[label].get("chemical_structure") or {}).get("smiles") or ""
        assert len(set(_large_fragments(smiles))) >= 2, label

    # ...and a 2:1 salt is not among them.
    assert "mupirocin calcium hydrate" not in queued


def test_the_detector_would_have_caught_the_record_that_started_this():
    """Replay trimethoprim-sulfamethoxazole's structure through the detector.

    The record is gone, so the corpus cannot demonstrate this any more — and a
    guard that can only pass because its subject was deleted proves nothing.
    """
    from curation_worklist import multi_component_queue

    cocktail = {
        "identifier": "antibioticmech:test-1", "label": "trimethoprim-sulfamethoxazole",
        "source_concepts": [{"source": "ARO"}],
        "chemical_structure": {"smiles": (
            "COc1cc(Cc2cnc(N)nc2N)cc(OC)c1OC."
            "Cc1cc(NS(=O)(=O)c2ccc(N)cc2)no1")},
    }
    assert [row["label"] for row in multi_component_queue([cocktail])] == \
        ["trimethoprim-sulfamethoxazole"]


def test_an_excluded_concept_stays_visible(records):
    """The claim made twelve times before it was true.

    Every EXCLUDE row, the docs and the commit message all said the concept
    "stays on `just worklist`". It did not: `merge()` returns on EXCLUDE before
    the concept reaches `skipped`, the only input `no_structure_queue` reads, so
    capreomycin — a WHO essential TB drug with seven CARD resistance edges — left
    the backlog with no trace outside data/raw/.

    Asserting the queue's CONTENTS, not merely that it runs, because an empty
    queue would satisfy a weaker check while the concepts stayed invisible.
    """
    import csv as _csv
    import sys as _sys
    from pathlib import Path as _P

    _sys.path.insert(0, str(_P(__file__).resolve().parent.parent / "scripts"))
    from curation_worklist import excluded_queue

    with (REPO_ROOT / "curation" / "decisions.tsv").open(encoding="utf-8") as fh:
        decided = {r["source_label"] for r in _csv.DictReader(fh, delimiter="\t")
                   if (r.get("decision") or "").upper() == "EXCLUDE"}
    assert decided, "no exclusions; this test guards nothing"

    listed = {row["label"] for row in excluded_queue()}
    assert listed == decided, sorted(decided ^ listed)
    assert "capreomycin" in listed

    # And each row carries a DISTINGUISHABLE why, not merely a non-empty one.
    # `assert all(hint.strip())` passed happily while all twelve rows read
    # identically: every rationale began with the same 110-character shared
    # justification, and the hint is truncated at 110, so the clause that says
    # WHICH mixture this is was cut from every row — in the console and in the
    # TSV. The queue's whole purpose is to carry the reason.
    hints = [row["hint"] for row in excluded_queue()]
    assert all(h.strip() for h in hints)
    kinds = {h.split(".")[0] for h in hints}
    assert len(kinds) >= 3, (
        f"all {len(hints)} rows share {len(kinds)} distinct opening clause(s); "
        "the distinguishing part is being truncated away")

    # The records really are gone from the corpus, so the queue is the only
    # place they appear — which is exactly why it has to exist.
    assert not (decided & {r["label"] for _p, r in records})

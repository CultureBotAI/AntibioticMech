"""The producer queue reports evidence; it does not extract producers.

`producer_organisms` is the corpus's largest empty axis and the signal is in the
definitions — 999 records with no producer use a phrase that may introduce one
(#94). Turning that into structured claims automatically is the inference this
repository removed in #47: a taxon in a definition may be the producer, the
isolation source, an expression host, a susceptible organism, or unrelated.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))


def test_the_queue_says_what_each_phrase_actually_claims():
    """"produced by" is a biosynthesis claim; "isolated from" is not.

    A compound isolated from a marine sponge may be made by its symbiont, so
    collapsing the two would manufacture producer claims no source made. The
    distinction has to reach the curator, which means it has to be in the row.
    """
    from curation_worklist import producer_candidate_queue

    made = {"identifier": "CHEBI:1", "label": "widgetmycin", "source_concepts": [],
            "definition": "An antibiotic produced by Streptomyces widgetensis."}
    found = {"identifier": "CHEBI:2", "label": "spongiamycin", "source_concepts": [],
             "definition": "A macrolide isolated from Theonella swinhoei."}

    rows = {r["label"]: r["hint"] for r in producer_candidate_queue([made, found])}
    assert "biosynthesis stated" in rows["widgetmycin"]
    assert "Streptomyces widgetensis" in rows["widgetmycin"]
    assert "SOURCE only" in rows["spongiamycin"], rows["spongiamycin"]
    assert "may not be the producer" in rows["spongiamycin"]


def test_a_record_that_already_has_a_producer_is_not_queued():
    """The queue is work owed. A curated producer settles it."""
    from curation_worklist import producer_candidate_queue

    done = {"identifier": "CHEBI:3", "label": "streptothricin D", "source_concepts": [],
            "definition": "An antibiotic produced by Streptomyces rochei.",
            "producer_organisms": [{"taxon_id": "NCBITaxon:1928",
                                    "taxon_label": "Streptomyces rochei"}]}
    assert producer_candidate_queue([done]) == []


def test_the_queue_asserts_nothing_about_the_corpus(records):
    """It must not write, imply, or presume a producer.

    Every queued record still has an empty `producer_organisms`; the queue's
    output is a curation prompt, not a claim, and nothing downstream should be
    able to mistake one for the other.
    """
    from curation_worklist import producer_candidate_queue

    docs = [r for _p, r in records]
    queued = {row["key"] for row in producer_candidate_queue(docs)}
    assert queued, "no candidates; either the corpus changed or the scan stopped working"
    by_id = {r["identifier"]: r for r in docs}
    assert all(not by_id[k].get("producer_organisms") for k in queued)


def test_no_binomial_is_still_worth_queueing():
    """A definition that names a producer without a parseable binomial is still
    a candidate — dropping it would hide the cases a regex is worst at, which is
    the wrong half to lose."""
    from curation_worklist import producer_candidate_queue

    vague = {"identifier": "CHEBI:4", "label": "vaguemycin", "source_concepts": [],
             "definition": "An antibiotic produced by a soil actinomycete."}
    rows = producer_candidate_queue([vague])
    assert len(rows) == 1
    assert "(no binomial)" in rows[0]["hint"]


def test_producer_organism_can_record_a_strain():
    """MIBiG names strains ("Streptomyces rochei NBRC 12908"), and a producer
    claim is often strain-specific. Without a field for it the strain hides
    inside the species name."""
    import yaml

    schema = yaml.safe_load(
        (REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml")
        .read_text(encoding="utf-8"))
    attrs = schema["classes"]["ProducerOrganism"]["attributes"]
    assert "strain" in attrs
    assert attrs["strain"]["range"] == "string"
    assert not attrs["strain"].get("required"), "a source naming only a species must stay valid"


def test_every_worklist_queue_returns_a_list():
    """Two successive rebases spliced two queue bodies together and dropped a
    `return rows`, so the function returned None and `just worklist` crashed on
    `len(None)` — once for `xref_unverified_queue`, once for
    `multi_component_queue`. Both times the file still parsed and every other
    test passed.

    An AST check is the right shape here: it catches the omission without having
    to run each queue against the corpus, and it will catch the next one.
    """
    import ast

    source = (REPO_ROOT / "scripts" / "curation_worklist.py").read_text(encoding="utf-8")
    missing = [
        node.name for node in ast.parse(source).body
        if isinstance(node, ast.FunctionDef) and node.name.endswith("_queue")
        and not any(isinstance(inner, ast.Return) and inner.value is not None
                    for inner in ast.walk(node))
    ]
    assert missing == [], f"queue functions with no return: {missing}"

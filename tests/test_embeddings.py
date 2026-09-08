"""The embedding artifacts, checked without needing the embedding stack.

`torch` and `sentence-transformers` are an optional extra and the recipes run on
system python, so nothing here imports them. What IS checkable is the part that
decides the embedding's quality — which fields go into a document — and whether
the committed map agrees with the corpus it claims to describe.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

MAP_PATH = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"


def test_the_document_omits_every_field_the_audit_says_it_omits():
    """The include/exclude list IS the embedding's design, so it is asserted
    rather than described.

    SMILES and InChI would be tokenized as gibberish long enough to dominate
    every document; the mode-of-action NOTE is near-identical across hundreds of
    records by design, and would manufacture one huge false cluster of "records
    that carry a seeded mechanism" while drowning the real signal. The mechanism
    VALUE belongs in the document; its boilerplate does not.
    """
    from embed_records import build_document

    record = {
        "identifier": "CHEBI:1", "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "definition": "A widget antibiotic.",
        "mode_of_action": "PROTEIN_SYNTHESIS_INHIBITION",
        "mode_of_action_target_scope": "HOST_SHARED_TARGET",
        "mode_of_action_notes": "Assigned from ChEBI role CHEBI:48001 (protein synthesis "
                               "inhibitor). Not a curator's mechanistic review.",
        "curation_status": "SEEDED", "grounding_status": "EXACT",
        "chemical_structure": {
            "smiles": "CC(=O)NC[C@H]1CN(c2ccc(N3CCOCC3)c(F)c2)C(=O)O1",
            "standard_inchi": "InChI=1S/C16H20FN3O4/c1-11(21)18-9-13-10-20(16(23)24-13)",
            "standard_inchi_key": "TYZROVQLWOKYKF-ZDUSSCGKSA-N",
            "molecular_formula": "C16H20FN3O4", "average_mass": 337.35, "charge": 0,
        },
    }
    doc = build_document(record, {"CHEBI:48001": "protein synthesis inhibitor"})

    assert "widgetmycin" in doc
    assert "A widget antibiotic" in doc
    assert "protein synthesis inhibition" in doc          # the VALUE is in
    assert "host shared target" in doc

    for leaked in ("CC(=O)NC[C@H]1CN", "InChI=1S", "TYZROVQLWOKYKF", "C16H20FN3O4",
                   "337.35", "SEEDED", "EXACT"):
        assert leaked not in doc, f"{leaked!r} leaked into the embedded document"
    # The boilerplate specifically, not merely the note field's absence.
    assert "Not a curator's mechanistic review" not in doc
    assert "Assigned from ChEBI role" not in doc


def test_a_document_never_collapses_to_nothing():
    """A record with almost no annotation must still embed as something
    identifiable, or it lands at an arbitrary point and reads as a real
    neighbour of whatever is nearby."""
    from embed_records import build_document

    doc = build_document({"identifier": "antibioticmech:aro-abc", "label": "MK-3118",
                          "antimicrobial_class": "ANTIFUNGAL"}, {})
    assert "MK-3118" in doc and "antifungal" in doc
    assert len(doc) > 20


@pytest.mark.skipif(not MAP_PATH.exists(), reason="corpus_map.json not built")
def test_the_committed_map_matches_the_corpus_it_describes():
    """pages/map.html is generated from this file, so a map that has drifted
    from the corpus publishes points for records that no longer exist."""
    payload = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    points = payload["points"]

    identifiers = set()
    classes_present = set()
    for path in (REPO_ROOT / "data" / "antibiotics").rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, dict) and record.get("identifier"):
            identifiers.add(str(record["identifier"]))
            classes_present.add(record.get("antimicrobial_class"))

    assert payload["n"] == len(points)
    mapped = {p[3] for p in points}
    assert mapped - identifiers == set(), sorted(mapped - identifiers)[:5]
    assert identifiers - mapped == set(), sorted(identifiers - mapped)[:5]
    assert set(payload["classes"]) <= classes_present | {"UNKNOWN"}

    for x, y, cls, _identifier, _label in points:
        assert 0.0 <= x <= 1.0 and 0.0 <= y <= 1.0, (x, y)
        assert 0 <= cls < len(payload["classes"])


@pytest.mark.skipif(not MAP_PATH.exists(), reason="corpus_map.json not built")
def test_every_map_point_links_to_a_page_that_exists():
    """The map's whole use is clicking through to a record. A stale href is a
    404 the site's own link checking would not see, because the hrefs live
    inside a JSON blob rather than in markup."""
    page = REPO_ROOT / "pages" / "map.html"
    if not page.exists():
        pytest.skip("pages/map.html not rendered")
    import re

    blob = re.search(r'<script id="map-data"[^>]*>(.*?)</script>',
                     page.read_text(encoding="utf-8"), re.S).group(1)
    payload = json.loads(blob)
    hrefs = payload["hrefs"]
    assert len(hrefs) == payload["n"], (len(hrefs), payload["n"])
    missing = [h for h in hrefs.values() if not (REPO_ROOT / "pages" / h).exists()]
    assert missing == [], missing[:5]


@pytest.mark.skipif(not MAP_PATH.exists(), reason="corpus_map.json not built")
def test_the_committed_map_is_not_stale_against_the_corpus():
    """Recomputes the embedded documents and compares their fingerprint.

    The identifier check above passes even when every document's TEXT has
    changed, which is the realistic drift: this map was built before a PR that
    moved `mode_of_action_target_scope` on dozens of records, and the scope is
    part of the embedded document. Nothing could tell.

    `build_document` is pure python, so this runs without torch — which is the
    only reason the check exists in CI at all. Rebuild with
    `just embed && just embed-map && just render`.
    """
    from embed_records import corpus_fingerprint, load_corpus

    payload = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    recorded = payload.get("corpus_fingerprint")
    assert recorded, "map carries no corpus_fingerprint; rebuild it"

    _ids, docs, _meta = load_corpus()
    assert recorded == corpus_fingerprint(docs), (
        "data/embeddings/corpus_map.json was built from different record text than "
        "the corpus now holds. Rebuild: just embed && just embed-map && just render")


def test_molecular_targets_reach_the_documents_of_real_records():
    """Asserted against the CORPUS, not a fixture I wrote to pass.

    The builder read `t["label"]` while the schema slot is `target_label`, so
    all 249 target entries on 206 records were silently dropped and the `[:6]`
    cap was dead code — with every gate green, the module docstring, the commit
    message and the docs all claiming targets were embedded. The synthetic
    record in the exclusion test carried no `molecular_targets` at all, so no
    test could see it.

    A fixture can only test the keys I already believed in. This walks the real
    records and fails if a field that EXISTS in the corpus never reaches a
    document.
    """
    import yaml
    from embed_records import build_document, load_corpus, role_names

    corpus = (REPO_ROOT / "data" / "antibiotics")
    with_targets = []
    for path in corpus.rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if record.get("molecular_targets"):
            with_targets.append(record)
    assert with_targets, "no record has molecular_targets; this test guards nothing"

    names = role_names()
    sample = with_targets[0]
    label = sample["molecular_targets"][0]["target_label"]
    assert label in build_document(sample, names), (
        f"{sample['identifier']} has molecular_targets but {label!r} is absent "
        "from its embedded document")

    _ids, docs, _meta = load_corpus()
    embedded = sum(1 for d in docs if "targets:" in d)
    assert embedded == len(with_targets), (embedded, len(with_targets))


def test_systematic_names_are_kept_out_of_the_documents():
    """Synonyms were 42% of all corpus tokens, and the long ones are full IUPAC
    names — the same "gibberish of a length that would dominate every document"
    given as the reason for excluding SMILES, readmitted through a different
    key. The filter is conservative: a name must be BOTH long and dense in
    digits, brackets and locants to be dropped."""
    from embed_records import is_systematic_name

    for keep in ("Vancocin", "vancomicina", "nalidixic acid", "penicillin G",
                 "4-aminosalicylic acid", "beta-lactam antibiotic"):
        assert not is_systematic_name(keep), keep

    for drop in (
        "(3S,6R,7R,11R,23S,26S,30aS,36R,38aR)-44-[2-O-(3-amino-2,3,6-trideoxy)]-oxacyclo",
        "1-ethyl-7-methyl-4-oxo-1,4-dihydro-1,8-naphthyridine-3-carboxylic acid, "
        "compound with 2,2'-[(1,2-dihydroxyethylidene)]bis",
    ):
        assert is_systematic_name(drop), drop


def test_synonyms_are_chosen_by_declared_type_before_shape():
    """`synonym_type` states what a shape heuristic could only guess.

    INN and BRAND_NAME are bounded at 30 characters across all 13,050 synonyms
    in the corpus, so they can be taken whole; EXACT_SYNONYM runs to 828 and
    holds the systematic names. Ranking by type puts the real names first and
    leaves the heuristic to break ties inside the residue.

    Not a wholesale exclusion of EXACT_SYNONYM: 8,356 of its 11,296 entries are
    ordinary common names, and only 556 of 2,923 records carry any INN or
    BRAND_NAME at all, so dropping the type would discard most of the signal
    for most records.
    """
    from embed_records import pick_synonyms

    entries = [
        {"synonym_type": "EXACT_SYNONYM",
         "synonym_text": "(3S,6R,7R,11R,23S,26S,30aS,36R,38aR)-44-[2-O-(3-amino-2,3,6-trideoxy)]"},
        {"synonym_type": "EXACT_SYNONYM", "synonym_text": "vancomicina"},
        {"synonym_type": "BRAND_NAME", "synonym_text": "Vancocin"},
        {"synonym_type": "INN", "synonym_text": "vancomycin"},
    ]
    picked = pick_synonyms(entries)
    assert picked[0] == "vancomycin", picked      # INN first
    assert picked[1] == "Vancocin", picked        # then brand
    assert "vancomicina" in picked                # ordinary common name survives
    assert not any(p.startswith("(3S,6R") for p in picked), picked


def test_the_corpus_synonym_selection_keeps_real_names_and_drops_iupac():
    """Against real records, not a fixture: vancomycin used to contribute a
    fragment of its IUPAC name and now contributes its INN and brand names."""
    from embed_records import load_corpus

    _ids, docs, meta = load_corpus()
    doc = docs[[m["label"] for m in meta].index("vancomycin")]
    assert "also known as" in doc
    tail = doc.split("also known as ")[1]
    assert "Vancocin" in tail, tail[:120]
    assert "(3S," not in tail and "[2-O-" not in tail, tail[:160]


def test_the_producing_organism_is_in_the_document_and_its_strain_is_not():
    """A search for a producing species matched nothing on 61 records (#218).

    The species is short, discriminative and the field a natural-product user is
    most likely to search by, so it belongs in the document. The strain is a
    collection number: opaque per token, and it would spend window on something
    that separates nothing. Asserting both halves, because including the species
    and including the whole label are one-character apart in the code.
    """
    from embed_records import build_document

    record = {
        "identifier": "CHEBI:1", "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "producer_organisms": [
            {"taxon_id": "NCBITaxon:405948",
             "taxon_label": "Saccharopolyspora erythraea",
             "strain": "NRRL 2338",
             "biosynthetic_gene_cluster": "BGC0000055"},
        ],
    }
    doc = build_document(record, {})

    assert "Saccharopolyspora erythraea" in doc
    assert "NRRL 2338" not in doc
    # The accession is an identifier, not language, and would tokenize as noise.
    assert "BGC0000055" not in doc
    # And both exclusions are declared where the audit lives, not left implicit.
    from embed_records import EXCLUDED

    assert {"strain", "biosynthetic_gene_cluster"} <= set(EXCLUDED)


def test_two_producers_of_one_compound_are_both_named_once():
    """Deduplicated and capped, so one heavily-curated record cannot spend the
    window listing the same organism twice."""
    from embed_records import build_document

    record = {
        "identifier": "CHEBI:1", "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "producer_organisms": [
            {"taxon_id": "NCBITaxon:1", "taxon_label": "Streptomyces fradiae"},
            {"taxon_id": "NCBITaxon:2", "taxon_label": "Pseudomonas syringae"},
            {"taxon_id": "NCBITaxon:1", "taxon_label": "Streptomyces fradiae"},
        ],
    }
    doc = build_document(record, {})

    assert doc.count("Streptomyces fradiae") == 1
    assert "Pseudomonas syringae" in doc


def test_the_producer_clause_sits_where_truncation_would_take_it_last():
    """Position is the design claim, and substring presence does not test it.

    Moving the clause after the identifiers passed every assertion here: the
    species was still in the document, just in the slot the window drops first.
    Nothing truncates today, with the longest document at 510 tokens against a
    512 window, so this is latent -- which is exactly when a position assertion
    is worth having rather than after something grows back.
    """
    from embed_records import build_document

    record = {
        "identifier": "CHEBI:1", "label": "widgetmycin",
        "antimicrobial_class": "ANTIBACTERIAL",
        "definition": "A widget antibiotic of no particular distinction.",
        "synonyms": [{"value": "widgetin", "synonym_type": "EXACT_SYNONYM"}],
        "producer_organisms": [
            {"taxon_id": "NCBITaxon:1", "taxon_label": "Streptomyces fradiae"}],
    }
    doc = build_document(record, {})
    assert doc.index("Streptomyces fradiae") < doc.index("A widget antibiotic")
    assert doc.index("Streptomyces fradiae") < doc.index("identifiers:")


def test_every_committed_producer_record_names_its_organism_in_the_document():
    """A fixture can only test the keys I already believed in.

    That sentence is this repository's own, written after reading `label` where
    the schema says `target_label` silently dropped 249 target entries with
    every gate green. The corpus is the check that a fixture cannot be.
    """
    import yaml
    from embed_records import CORPUS_DIR, build_document

    missing = []
    seen = 0
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        producers = record.get("producer_organisms") or []
        if not producers:
            continue
        seen += 1
        document = build_document(record, {})
        for producer in producers:
            if producer["taxon_label"] not in document:
                missing.append((record["identifier"], producer["taxon_label"]))
    assert seen == 61, seen
    assert missing == [], missing[:10]

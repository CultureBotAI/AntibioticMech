"""Acceptance tests for the MIBiG producer import."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from extract_mibig_producers import (  # noqa: E402
    LINK_EVIDENCE_METHODS,
    link_evidence_methods,
    reviewer_ids,
)


def test_review_filter_ignores_the_migration_placeholder():
    entry = {
        "changelog": {
            "releases": [
                {
                    "entries": [
                        {"reviewers": ["AAAAAAAAAAAAAAAAAAAAAAAA"]},
                        {"reviewers": ["EXPERT-2", "EXPERT-1"]},
                    ]
                }
            ]
        }
    }
    assert reviewer_ids(entry, "AAAAAAAAAAAAAAAAAAAAAAAA") == ["EXPERT-1", "EXPERT-2"]


def _entry(*methods, status="active"):
    return {
        "status": status,
        "loci": [{"evidence": [{"method": method} for method in methods]}],
    }


def test_only_experimental_link_methods_admit_an_entry():
    """The gate is an allow-list, so a predicted link yields no methods at all.

    Deleting the membership test would let ``Homology-based prediction`` through,
    which is the whole distinction the gate exists to draw (#203).
    """
    assert link_evidence_methods(_entry("Knock-out studies")) == ["Knock-out studies"]
    assert link_evidence_methods(_entry("Homology-based prediction")) == []
    assert link_evidence_methods(
        _entry("Synthetic-bioinformatic natural product (syn-BNP)")) == []
    assert link_evidence_methods(
        _entry("Homology-based prediction", "Enzymatic assays")) == ["Enzymatic assays"]
    assert link_evidence_methods({}) == []


def test_the_allow_list_names_no_predictive_method():
    """A method added to the tuple without reading it would land here.

    The list is the admission gate; a predicted or synthetic link is not evidence
    that the named organism makes the compound.
    """
    forbidden = {
        "Homology-based prediction",
        "Synthetic-bioinformatic natural product (syn-BNP)",
    }
    assert forbidden.isdisjoint(LINK_EVIDENCE_METHODS)
    assert len(set(LINK_EVIDENCE_METHODS)) == len(LINK_EVIDENCE_METHODS)


def test_committed_mibig_inventory_is_evidenced_and_carries_no_activity_claims(repo_root):
    path = repo_root / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 1462
    # Every row states which experiment supports its compound-to-producer link,
    # and every stated method is one the extractor's allow-list admits.
    assert all(row["link_evidence"] for row in rows)
    assert {method for row in rows for method in row["link_evidence"].split("|")} <= set(
        LINK_EVIDENCE_METHODS)
    # The changelog reviewer is retained as provenance but is no longer the gate,
    # so most admitted rows carry no expert review -- and none carries the
    # placeholder that made the old gate look stricter than it was.
    #
    # BOTH sides are asserted. Checking only that some row reads "false" would
    # survive an extractor that emitted "false" unconditionally: the row count
    # would hold, and `verify-corpus` would hold too because the inventory and
    # the corpus regenerate together (#207).
    assert any(row["expert_reviewed"] == "false" for row in rows)
    assert sum(row["expert_reviewed"] == "true" for row in rows) == 42
    assert all(bool(row["reviewer_ids"]) == (row["expert_reviewed"] == "true")
               for row in rows)
    assert all("AAAAAAAAAAAAAAAAAAAAAAAA" not in row["reviewer_ids"] for row in rows)
    assert all(row["primary_reference"] for row in rows)
    assert "bioactivity" not in {column.lower() for column in rows[0]}
    assert "mic" not in {column.lower() for column in rows[0]}


def test_only_exact_one_to_one_structure_matches_are_seeded(records):
    claims = {
        (record["identifier"], producer["biosynthetic_gene_cluster"])
        for _, record in records
        for producer in record.get("producer_organisms") or []
        if producer.get("source") == "MIBIG"
    }
    # The three matches the reviewer-field gate found are still here; widening
    # the gate to MIBiG's own link evidence added the rest (#203).
    assert {
        ("CHEBI:60821", "BGC0000432"),
        ("CHEBI:60828", "BGC0000432"),
        ("CHEBI:28001", "BGC0000455"),
    } <= claims
    assert len(claims) == 64
    # BGC0000311 balhimycin has only a connectivity-block match and must remain
    # rejected until its stereochemical identity is resolved.
    assert all(bgc != "BGC0000311" for _, bgc in claims)


def test_the_three_vocabularies_cannot_drift_apart():
    """Extractor allow-list, seeder map, and schema enum are one vocabulary.

    They live in three files: the extractor gates on MIBiG's raw strings, the
    seeder maps them to schema values, and the schema declares what a record may
    hold. Adding a term to any one alone either silently drops producer evidence
    or writes a value closed-schema validation rejects, so the agreement is the
    thing worth asserting -- not any one list's contents.
    """
    import yaml

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from seed_from_sources import MIBIG_LINK_EVIDENCE_METHODS

    assert set(MIBIG_LINK_EVIDENCE_METHODS) == set(LINK_EVIDENCE_METHODS)

    schema = yaml.safe_load(
        (Path(__file__).resolve().parents[1] / "src" / "antibioticmech" / "schema"
         / "antibioticmech.yaml").read_text(encoding="utf-8"))
    permissible = set(schema["enums"]["LinkEvidenceMethodEnum"]["permissible_values"])
    assert set(MIBIG_LINK_EVIDENCE_METHODS.values()) == permissible
    # Distinct, or two source terms could be collapsed onto one value and the
    # orphaned value deleted, leaving both set equalities true while the corpus
    # recorded one method where the source recorded two (#229).
    assert len(set(MIBIG_LINK_EVIDENCE_METHODS.values())) == len(MIBIG_LINK_EVIDENCE_METHODS)
    # Each schema value quotes the MIBiG term it stands for, so the mapping can
    # be checked against the source without reading the seeder.
    for raw, value in MIBIG_LINK_EVIDENCE_METHODS.items():
        described = schema["enums"]["LinkEvidenceMethodEnum"]["permissible_values"][value]
        assert raw in described["description"], (value, raw)

    # The site shows the source's wording, so its label map is a fourth copy of
    # the same vocabulary and drifts the same way. It must render each value as
    # the exact term the source used, or the page quietly reworded the evidence.
    from render_pages import LINK_EVIDENCE_LABELS

    assert {v: k for k, v in MIBIG_LINK_EVIDENCE_METHODS.items()} == LINK_EVIDENCE_LABELS


def test_an_unmapped_method_raises_rather_than_yielding_no_evidence():
    """Dropping it would publish a weaker claim instead of an unhandled one."""
    import pytest

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from seed_from_sources import mibig_link_evidence

    assert mibig_link_evidence("Knock-out studies") == ["KNOCK_OUT_STUDIES"]
    # Sorted and deduplicated, so a re-seed of unchanged data stays byte-identical
    # however the source happened to order or repeat the methods.
    assert mibig_link_evidence("Knock-out studies|Enzymatic assays|Knock-out studies") == [
        "ENZYMATIC_ASSAYS", "KNOCK_OUT_STUDIES"]
    with pytest.raises(KeyError):
        mibig_link_evidence("Some method MIBiG added in 4.1")


def test_link_evidence_scope_reads_the_source_entry_not_the_surviving_rows(records):
    """COMPOUND_SPECIFIC must mean the ENTRY named one compound.

    Counting inventory rows per accession instead would misread 11 rows today:
    an entry whose other compounds had no usable structure leaves one row behind
    and would masquerade as a single-compound entry, publishing shared cluster
    evidence as though it singled this molecule out (#206).
    """
    import csv

    path = Path(__file__).resolve().parents[1] / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    by_accession = {row["mibig_accession"]: row["entry_compound_count"] for row in rows}
    surviving: dict[str, int] = {}
    for row in rows:
        surviving[row["mibig_accession"]] = surviving.get(row["mibig_accession"], 0) + 1
    # The two readings really do disagree, or this test guards nothing.
    divergent = {a for a, n in by_accession.items() if (n == "1") != (surviving[a] == 1)}
    assert len(divergent) == 11

    # None of the 11 reaches a corpus record today, so scanning the corpus alone
    # cannot tell the two implementations apart: switching the seeder to count
    # surviving rows leaves all 64 published scopes byte-identical. The defect
    # has to be exercised directly, on a row from the divergent set.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from seed_from_sources import attach_mibig_producers

    fixture = next(row for row in rows
                   if row["mibig_accession"] in divergent
                   and row["stereo_complete"] == "true")
    assert surviving[fixture["mibig_accession"]] == 1
    assert fixture["entry_compound_count"] != "1"
    seeded = {"CHEBI:X": {
        "identifier": "CHEBI:X", "label": "t", "curation_history": [],
        "chemical_structure": {"standard_inchi_key": fixture["standard_inchi_key"]}}}
    attach_mibig_producers(seeded, "4.0.1")
    produced = seeded["CHEBI:X"].get("producer_organisms")
    assert produced, "the lane matched nothing; the fixture is wrong, not the code"
    assert produced[0]["link_evidence_scope"] == "CLUSTER_INHERITED", (
        f"{fixture['mibig_accession']} is the only surviving row of an entry naming "
        f"{fixture['entry_compound_count']} compounds; its evidence is inherited")

    seen = 0
    for _, record in records:
        for producer in record.get("producer_organisms") or []:
            if producer.get("source") != "MIBIG":
                continue
            seen += 1
            expected = ("COMPOUND_SPECIFIC"
                        if by_accession[producer["biosynthetic_gene_cluster"]] == "1"
                        else "CLUSTER_INHERITED")
            assert producer.get("link_evidence_scope") == expected, record["identifier"]
    assert seen == 64


def test_a_producer_naming_no_organism_is_refused_and_queued(records):
    """"uncultured bacterium" answers no question a producer claim asks.

    A genus is the minimum, and an uncultivated symbiont that HAS one stays: the
    refusal must not swallow "uncultured Candidatus Entotheonella sp.", which is
    a real organism identity the corpus should carry.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from curation_worklist import unnamed_producer_queue
    from seed_from_sources import names_an_organism

    assert not names_an_organism("uncultured bacterium")
    assert not names_an_organism("Uncultured bacterium")
    assert not names_an_organism("uncultured organism")
    assert not names_an_organism("fungal sp. No.14919")
    assert not names_an_organism("Chloroflexi bacterium TSY")
    assert names_an_organism("Streptomyces sp.")
    assert names_an_organism("Saccharopolyspora erythraea")
    # A culture-status or placement prefix does not stop a name being a name.
    # Reading only the first token refused all four of these, which would have
    # dropped four real genera the day one of them matched a structure (#217).
    assert names_an_organism("uncultured Candidatus Entotheonella sp.")
    assert names_an_organism("uncultured Prochloron sp.")
    assert names_an_organism("[Oscillatoria] sp. PCC 6506")
    # Every label the committed inventory offers is classified deliberately.
    # A predicate that drifted would show up here as a changed refusal set,
    # rather than as producers quietly missing from a later corpus.
    import csv

    path = Path(__file__).resolve().parents[1] / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        labels = {row["taxon_label"] for row in csv.DictReader(handle, delimiter="\t")}
    assert {label for label in labels if not names_an_organism(label)} == {
        # A capitalized taxon that is a PHYLUM, which a genus-shaped test alone
        # accepted. The rank noun beside it is the source saying so.
        "Chloroflexi bacterium TSY",
        "Uncultured bacterium",
        "fungal sp. No.14919",
        "uncultured bacterium",
        "uncultured bacterium AB1650",
        "uncultured bacterium BAC AB649/1850",
        "uncultured bacterium psy1",
        "uncultured organism",
    }

    published = {record["identifier"] for _, record in records
                 for producer in record.get("producer_organisms") or []
                 if producer["taxon_id"] == "NCBITaxon:77133"}
    assert published == set()
    # Refused, not lost: the cluster and its citation stay reachable.
    queued = unnamed_producer_queue([record for _, record in records])
    assert {row["key"] for row in queued} == {"CHEBI:156313", "CHEBI:156314"}
    assert all(row["source_id"] == "BGC0001336" for row in queued)


def test_closed_validation_rejects_a_link_evidence_value_outside_the_vocabulary(repo_root):
    """The slot promised experimental support; now the schema enforces it.

    Before #211 the range was a bare string, so a homology prediction, invented
    text, and an empty list all validated clean -- the promise rested entirely on
    the extractor, and a hand edit or a future lane could break it silently.
    """
    import yaml

    from antibioticmech.validation.write_validated import validate_antibiotic

    path = repo_root / "data" / "antibiotics" / "antibacterial" / "erythromycin-a.yaml"

    def errors(**changes):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        doc["producer_organisms"][0].update(changes)
        return validate_antibiotic(doc)

    assert errors() == []
    assert errors(link_evidence=["HOMOLOGY_BASED_PREDICTION"])
    assert errors(link_evidence=["TOTALLY_MADE_UP"])
    # MIBiG's own wording is not the corpus vocabulary either, so a lane that
    # forgot to map would fail loudly rather than write prose into the slot.
    assert errors(link_evidence=["Knock-out studies"])
    assert errors(link_evidence_scope="PROBABLY_FINE")


def test_evidence_without_a_scope_is_rejected_by_the_schema_rule(repo_root):
    """Deleting the rule must not be a green-gate no-op.

    Verified the gap it closes: with the rule stripped, a producer carrying
    methods and no scope validated clean, and nothing else asserted the pairing
    for a producer that is not MIBiG's (#228).
    """
    import yaml

    from antibioticmech.validation.write_validated import validate_antibiotic

    path = repo_root / "data" / "antibiotics" / "antibacterial" / "erythromycin-a.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    doc["producer_organisms"][0].pop("link_evidence_scope")
    assert validate_antibiotic(doc)

    # And for a curator-authored producer, which no corpus-integrity test covers
    # because those filter on the MIBiG source marker.
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    doc["producer_organisms"] = [{
        "taxon_id": "NCBITaxon:1", "taxon_label": "Example organism",
        "link_evidence": ["KNOCK_OUT_STUDIES"],
    }]
    assert validate_antibiotic(doc)


def test_the_inventory_counts_an_entry_s_compounds_not_its_usable_ones(repo_root):
    """The count must survive compounds the extractor could not use.

    Narrowing it to structure-bearing compounds would reproduce the defect #206
    fixed, in the one file the scope test never reads: the inventory would then
    agree with its own row count everywhere and every scope would read
    COMPOUND_SPECIFIC. No test calls the extractor, so this asserts the property
    on the committed inventory instead.
    """
    import csv
    from collections import Counter

    path = repo_root / "data" / "raw" / "mibig_producers.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    surviving = Counter(row["mibig_accession"] for row in rows)
    declared = {row["mibig_accession"]: int(row["entry_compound_count"]) for row in rows}
    # Constant within an accession, and never fewer than the rows that survived.
    for row in rows:
        assert int(row["entry_compound_count"]) == declared[row["mibig_accession"]]
        assert declared[row["mibig_accession"]] >= surviving[row["mibig_accession"]]
        assert int(row["compound_index"]) <= declared[row["mibig_accession"]]
    # And it genuinely exceeds the surviving count somewhere, or it is just the
    # row count wearing another name.
    assert sum(1 for a, n in declared.items() if n > surviving[a]) == 22


def test_every_seeded_producer_says_which_experiment_supports_it(records):
    """A widened gate must not widen into unevidenced claims.

    Each seeded producer carries the MIBiG methods that admitted its entry, and
    `reviewed` is asserted only where MIBiG records a real expert reviewer -- it
    is no longer a blanket true, which is what made the old flag misleading.
    """
    # The corpus speaks the schema's vocabulary, not MIBiG's wording; the map
    # between them is asserted by test_the_three_vocabularies_cannot_drift_apart.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    from seed_from_sources import MIBIG_LINK_EVIDENCE_METHODS

    allowed = set(MIBIG_LINK_EVIDENCE_METHODS.values())
    problems = []
    for _, record in records:
        for producer in record.get("producer_organisms") or []:
            if producer.get("source") != "MIBIG":
                continue
            methods = producer.get("link_evidence") or []
            if not methods or not set(methods) <= allowed:
                problems.append((record["identifier"], methods))
            if "reviewed" in producer and producer["reviewed"] is not True:
                problems.append((record["identifier"], "reviewed present but not true"))
    assert problems == [], problems[:10]
    # And the flag reaches the corpus at all. Without this the extractor could
    # stop emitting expert review entirely and every assertion above would still
    # hold, because absent satisfies "present implies true" (#207).
    reviewed = sum(1 for _, record in records
                   for producer in record.get("producer_organisms") or []
                   if producer.get("source") == "MIBIG" and producer.get("reviewed") is True)
    assert reviewed == 3, reviewed


def test_reseed_replaces_only_the_mibig_owned_producer_slice():
    from seed_from_sources import merge_with_existing

    old_mibig = {
        "taxon_id": "NCBITaxon:1",
        "taxon_label": "old",
        "source": "MIBIG",
        "reviewed": True,
    }
    new_mibig = {
        "taxon_id": "NCBITaxon:2",
        "taxon_label": "new",
        "source": "MIBIG",
        "reviewed": True,
    }
    curated = {
        "taxon_id": "NCBITaxon:3",
        "taxon_label": "curator assertion",
        "reference": "PMID:1",
    }
    base = {
        "identifier": "CHEBI:1",
        "label": "example",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "curation_history": [],
    }
    fresh = dict(base) | {"producer_organisms": [new_mibig]}
    existing = dict(base) | {"producer_organisms": [old_mibig, curated]}
    assert merge_with_existing(fresh, existing)["producer_organisms"] == [new_mibig, curated]

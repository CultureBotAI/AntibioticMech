"""The committed inventories must stay shaped the way the seeder reads them."""

from __future__ import annotations

import re

CURIE_SAFE = re.compile(r"^[A-Za-z0-9._-]+$")


def test_chebi_inventory_has_the_columns_the_seeder_reads(raw_tsv):
    rows = raw_tsv("chebi_antimicrobials.tsv")
    assert rows, "empty inventory"
    required = {"chebi_id", "name", "in_role_scope", "role_ids", "parent_ids", "smiles",
                "standard_inchi", "standard_inchi_key", "molecular_formula", "synonyms",
                "xrefs", "citations"}
    assert required <= set(rows[0])


def test_every_chebi_xref_is_a_usable_curie(raw_tsv):
    """A malformed accession that reaches a record fails write-time validation,
    which is late; catching it in the inventory names the upstream row."""
    bad = []
    for row in raw_tsv("chebi_antimicrobials.tsv"):
        for xref in (row["xrefs"] or "").split("|"):
            if not xref:
                continue
            prefix, _, local = xref.partition(":")
            if not prefix or not CURIE_SAFE.match(local):
                bad.append((row["chebi_id"], xref))
    assert bad == [], bad[:20]


def test_aro_inventory_holds_molecules_not_drug_classes(raw_tsv):
    """ARO terms marked classified_as_drug_class are structural classes. They
    belong in parent_compounds, never as records."""
    rows = raw_tsv("aro_antibiotics.tsv")
    classes = [r["aro_id"] for r in rows if "classified_as_drug_class" in (r["classification"] or "")]
    assert classes == []


def test_resistance_edges_point_at_known_molecules(raw_tsv):
    molecules = {r["aro_id"] for r in raw_tsv("aro_antibiotics.tsv")}
    dangling = [r["antibiotic_id"] for r in raw_tsv("aro_resistance_edges.tsv")
                if r["antibiotic_id"] not in molecules]
    assert dangling == [], dangling[:10]


def test_target_edges_point_at_known_molecules(raw_tsv):
    molecules = {r["aro_id"] for r in raw_tsv("aro_antibiotics.tsv")}
    dangling = [r["antibiotic_id"] for r in raw_tsv("aro_target_edges.tsv")
                if r["antibiotic_id"] not in molecules]
    assert dangling == [], dangling[:10]


def test_pubchem_rows_carry_a_structure_and_a_retrieval_date(raw_tsv):
    """This is the one inventory fetched over the network. A row without a
    structure is a failed fetch that must not be mistaken for an answer."""
    for row in raw_tsv("pubchem_structures.tsv"):
        assert row["standard_inchi_key"], row["aro_id"]
        assert row["retrieved_on"].startswith("20"), row["aro_id"]


def test_pubchem_rows_are_keyed_by_aro_id(raw_tsv):
    """Two ARO molecules can share a PubChem CID; the seeder looks rows up by
    ARO id, so an ARO id must appear at most once."""
    seen = [r["aro_id"] for r in raw_tsv("pubchem_structures.tsv")]
    assert len(seen) == len(set(seen))

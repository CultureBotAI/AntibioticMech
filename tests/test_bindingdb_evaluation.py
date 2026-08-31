"""Unit tests for the non-writing BindingDB target evaluator."""

from __future__ import annotations

import sys
from array import array
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from evaluate_bindingdb_targets import (  # noqa: E402
    CURATED_MARKER,
    compact_candidate,
    microbial_root,
    primary_reference,
    standard_key,
)


def test_standard_key_is_recomputed_from_structure():
    assert standard_key("CCO") == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"


def test_primary_citation_prefers_pmid_and_never_uses_entry_doi():
    assert primary_reference({"PMID": "123", "Article DOI": "10.1/a"}) == "PMID:123"
    assert primary_reference({"PMID": "", "Article DOI": "10.1/a"}) == "DOI:10.1/a"
    assert primary_reference({"PMID": "", "Article DOI": "", "BindingDB Entry DOI": "10.7270/x"}) == ""


def test_taxonomy_filter_requires_an_explicit_microbial_root():
    parents = array("I", [0] * 20)
    parents[10] = 2
    parents[2] = 1
    parents[11] = 10
    assert microbial_root(11, parents) == "Bacteria"
    assert microbial_root(1, parents) == ""


def test_uniprot_accessions_remain_examples_not_target_identity():
    row = {
        "Ligand InChI Key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
        "BindingDB Reactant_set_id": "7",
        "BindingDB MonomerID": "8",
        "Target Name": "example enzyme",
        "Target Source Organism According to Curator or DataSource": "Bacillus subtilis",
        "PMID": "123",
        "Article DOI": "",
        "Ki (nM)": "<5",
        "IC50 (nM)": "",
        "Kd (nM)": "",
        "EC50 (nM)": "",
        "UniProt (SwissProt) Primary ID of Target Chain 1": "P12345",
        "Number of Protein Chains in Target (>1 implies a multichain complex)": "1",
    }
    candidate = compact_candidate(row, "CHEBI:1")
    assert candidate["target_name"] == "example enzyme"
    assert candidate["uniprot_accessions"] == ["P12345"]
    assert candidate["measurements"] == {"Ki": "<5"}
    assert CURATED_MARKER == "Curated from the literature by BindingDB"

"""Unit tests for CAS Common Chemistry non-redistributing evaluator in AntibioticMech."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_source_queue import UNSEEDABLE  # noqa: E402
from evaluate_cas_common_chemistry import (  # noqa: E402
    REDISTRIBUTION_CLASS,
    build_overlay_proposals,
    evaluate_cas_rows,
    has_deduplicated_component_smiles,
    strip_inchikey_prefix,
    validate_output_path_is_outside_corpus,
)
from extract_source_inventory import load_curation_chebi_ids  # noqa: E402


def test_cas_common_chemistry_redistribution_is_unseedable_under_cc_by_4():
    assert REDISTRIBUTION_CLASS in UNSEEDABLE
    assert "NonCommercial" in UNSEEDABLE[REDISTRIBUTION_CLASS]


def test_strip_inchikey_prefix_normalizes_cas_format():
    assert (
        strip_inchikey_prefix("InChIKey=RZQXOGQSPBYUKH-UHFFFAOYSA-N")
        == "RZQXOGQSPBYUKH-UHFFFAOYSA-N"
    )
    assert (
        strip_inchikey_prefix("RZQXOGQSPBYUKH-UHFFFAOYSA-N")
        == "RZQXOGQSPBYUKH-UHFFFAOYSA-N"
    )


def test_has_deduplicated_component_smiles_detects_polysalt_and_polyhydrate_collapse():
    assert (
        has_deduplicated_component_smiles(
            "C10H16N2O8.2H2O.2Na",
            "O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O.[Na].O",
            (
                "InChI=1S/C10H16N2O8.2Na.2H2O/"
                "c13-7(14)1-11(2-8(15)16)5-6-12(3-9(17)18)4-10(19)20;;;;/"
                "h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20);;;2*1H2"
            ),
        )
        is True
    )
    assert (
        has_deduplicated_component_smiles(
            "C7H17NO7S",
            "O=S(=O)(O)CC(O)CNC(CO)(CO)CO",
            "InChI=1S/C7H17NO7S/c9-2-7(3-10,4-11)8-1-6(12)5-16(13,14)15/h6,8-12H,1-5H2,(H,13,14,15)",
        )
        is False
    )


def test_validate_output_path_refuses_corpus_raw_and_curation_directories(tmp_path):
    (tmp_path / "data" / "raw").mkdir(parents=True)
    (tmp_path / "data" / "antibiotics").mkdir(parents=True)
    (tmp_path / "curation").mkdir(parents=True)
    (tmp_path / "reports").mkdir(parents=True)

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "raw" / "cas.tsv", repo_root=tmp_path
        )

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "antibiotics" / "cas.tsv", repo_root=tmp_path
        )

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "curation" / "decisions.tsv", repo_root=tmp_path
        )

    validate_output_path_is_outside_corpus(
        tmp_path / "reports" / "cas_eval.tsv", repo_root=tmp_path
    )


def test_evaluate_cas_rows_classifies_chebi_3star_grounding_actions_and_congener_collision():
    cas_rows = [
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:aro-bf71825341",
            "query_name": "gramicidin S",
            "cas_rn": "113-73-5",
            "cas_name": "Gramicidin S",
            "molecular_formula": "C60H92N12O10",
            "canonical_smiles": "CC(C)C1NC(=O)...",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=BLRBXZWBHXWECJ-XFFZJAGNSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:aro-bf39ac682c",
            "query_name": "gramicidin C",
            "cas_rn": "113-73-5",
            "cas_name": "Gramicidin S",
            "molecular_formula": "C60H92N12O10",
            "canonical_smiles": "CC(C)C1NC(=O)...",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=BLRBXZWBHXWECJ-XFFZJAGNSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:curator-223be9c74d",
            "query_name": "Luteolin",
            "cas_rn": "491-70-3",
            "cas_name": "Luteolin",
            "molecular_formula": "C15H10O6",
            "canonical_smiles": "O=c1cc(-c2ccc(O)c(O)c2)oc2cc(O)cc(O)c12",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=IQPNAANSBPBGFQ-UHFFFAOYSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:aro-2eea3233f3",
            "query_name": "ofloxacin",
            "cas_rn": "82419-36-1",
            "cas_name": "Ofloxacin",
            "molecular_formula": "C18H20FN3O4",
            "canonical_smiles": "CC1COc2c(N3CCN(C)CC3)c(F)cc3c(=O)c(C(=O)O)cn1c23",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=GSDSWSVVBLHKDQ-UHFFFAOYSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:ARO-3007577",
            "query_name": "triflumizole",
            "cas_rn": "99387-89-0",
            "cas_name": "Triflumizole",
            "molecular_formula": "C15H15ClF3N3O",
            "canonical_smiles": "CCCOC(=Nc1ccc(Cl)cc1C(F)(F)F)n1ccnc1",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=HSMVPDGQOIQYSR-UHFFFAOYSA-N",
        },
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:ARO-3005110",
            "query_name": "novel antibiotic",
            "cas_rn": "12345-67-8",
            "cas_name": "Novel antibiotic",
            "molecular_formula": "C10H12N2O2",
            "canonical_smiles": "O=C1NCCc2ccccc12",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=AAAAAAAAAAAAAA-BBBBBBBBSA-N",
        },
    ]
    records_by_id = {
        "antibioticmech:aro-bf71825341": {
            "identifier": "antibioticmech:aro-bf71825341",
            "label": "gramicidin S",
            "grounding_status": "MINTED",
            "xrefs": ["ARO:3005195", "PubChem:73357"],
            "chemical_structure": {
                "standard_inchi_key": "BLRBXZWBHXWECJ-XFFZJAGNSA-N",
            },
        },
        "antibioticmech:aro-bf39ac682c": {
            "identifier": "antibioticmech:aro-bf39ac682c",
            "label": "gramicidin C",
            "grounding_status": "MINTED",
            "xrefs": ["ARO:3005193", "PubChem:73357"],
            "chemical_structure": {
                "standard_inchi_key": "BLRBXZWBHXWECJ-XFFZJAGNSA-N",
            },
        },
        "antibioticmech:curator-223be9c74d": {
            "identifier": "antibioticmech:curator-223be9c74d",
            "label": "Luteolin",
            "grounding_status": "MINTED",
            "xrefs": ["PubChem:5280445"],
            "chemical_structure": {
                "standard_inchi_key": "IQPNAANSBPBGFQ-UHFFFAOYSA-N",
            },
        },
        "antibioticmech:aro-2eea3233f3": {
            "identifier": "antibioticmech:aro-2eea3233f3",
            "label": "ofloxacin",
            "grounding_status": "MINTED",
            "xrefs": ["ARO:0000037", "PubChem:4583"],
            "chemical_structure": {
                "standard_inchi_key": "GSDSWSVVBLHKDQ-UHFFFAOYSA-N",
            },
        },
        "antibioticmech:ARO-3007577": {
            "identifier": "antibioticmech:ARO-3007577",
            "label": "triflumizole",
            "grounding_status": "MINTED",
            "chemical_structure": {
                "standard_inchi_key": "HSMVPDGQOIQYSR-HYXKWVIFSA-N",
            },
        },
        "antibioticmech:ARO-3005110": {
            "identifier": "antibioticmech:ARO-3005110",
            "label": "novel antibiotic",
            "grounding_status": "MINTED",
            "chemical_structure": {},
        },
    }
    chebi_antimicrobials: dict[str, tuple[str, str]] = {}
    chebi_3star_all = {
        "BLRBXZWBHXWECJ-XFFZJAGNSA-N": ("CHEBI:5530", "gramicidin S"),
        "IQPNAANSBPBGFQ-UHFFFAOYSA-N": ("CHEBI:15864", "luteolin"),
        "GSDSWSVVBLHKDQ-UHFFFAOYSA-N": ("CHEBI:7731", "ofloxacin"),
        "HSMVPDGQOIQYSR-HYXKWVIFSA-N": ("CHEBI:81787", "(E)-triflumizole"),
    }

    evaluated = evaluate_cas_rows(
        cas_rows,
        records_by_id,
        chebi_antimicrobials,
        chebi_3star_all,
    )
    by_id = {r["identifier"]: r for r in evaluated}

    assert (
        by_id["antibioticmech:aro-bf71825341"]["evaluation_category"]
        == "CHEBI_3STAR_OUTSIDE_ANTIMICROBIAL_SLICE"
    )
    assert (
        by_id["antibioticmech:aro-bf71825341"]["grounding_action"]
        == "HOLD_CONGENER_COLLISION"
    )
    assert (
        by_id["antibioticmech:aro-bf39ac682c"]["grounding_action"]
        == "HOLD_CONGENER_COLLISION"
    )
    assert (
        by_id["antibioticmech:aro-2eea3233f3"]["grounding_action"]
        == "DECISION_NEEDS_INVENTORY_EXTRACT"
    )
    assert (
        by_id["antibioticmech:curator-223be9c74d"]["grounding_action"]
        == "CURATOR_XREF_READY"
    )
    assert (
        by_id["antibioticmech:ARO-3007577"]["grounding_action"]
        == "REVIEW_STEREO_OR_CONGENER"
    )
    assert (
        by_id["antibioticmech:ARO-3005110"]["grounding_action"]
        == "CAS_RN_ONLY_NO_CHEBI_3STAR"
    )

    proposals = build_overlay_proposals(evaluated, records_by_id)
    assert len(proposals) == 4
    prop_by_id = {p["identifier"]: p for r_idx, p in enumerate(proposals)}
    assert prop_by_id["antibioticmech:curator-223be9c74d"]["target_file"] == (
        "curation/curator_antibiotics.tsv"
    )
    assert "CAS-RN:" not in prop_by_id["antibioticmech:curator-223be9c74d"]["proposed_entry"]
    assert prop_by_id["antibioticmech:aro-2eea3233f3"]["target_file"] == (
        "curation/decisions.tsv"
    )
    assert prop_by_id["antibioticmech:aro-2eea3233f3"]["proposed_entry"].split("\t") == [
        "ARO:0000037",
        "ofloxacin",
        "",
        "ground",
        "CHEBI:7731",
        "ofloxacin",
        "3-star ChEBI exact Standard InChIKey match (GSDSWSVVBLHKDQ-UHFFFAOYSA-N)",
    ]
    assert prop_by_id["antibioticmech:aro-bf71825341"]["target_file"] == "HOLD"
    assert prop_by_id["antibioticmech:aro-bf39ac682c"]["target_file"] == "HOLD"


def test_load_curation_chebi_ids_collects_decisions_and_curator_xrefs(tmp_path):
    decisions = tmp_path / "decisions.tsv"
    decisions.write_text(
        "aro_id\taro_name\taro_chebi_xref\taction\tgrounding_target_id\tgrounding_target_name\treason\n"
        "ARO:3005195\tgramicidin S\t\tground\tCHEBI:5530\tgramicidin S\ttest\n"
        "ARO:3009999\texplicit chebi\tCHEBI:12345\tkeep\t\t\texplicit chebi column\n",
        encoding="utf-8",
    )
    curator = tmp_path / "curator_antibiotics.tsv"
    curator.write_text(
        "label\txrefs\tinchi_key\n"
        "Luteolin\tPubChem:5280445|CHEBI:15864|CAS-RN:491-70-3\tIQPNAANSBPBGFQ-UHFFFAOYSA-N\n",
        encoding="utf-8",
    )
    ids = load_curation_chebi_ids(decisions_tsv=decisions, curator_tsv=curator)
    assert ids == {"CHEBI:5530", "CHEBI:12345", "CHEBI:15864"}

    # Verify duplicate CAS rows for the same identifier do not trigger false HOLD_CONGENER_COLLISION (#1368)
    dup_cas_rows = [
        {
            "group": "antibiotic_minted",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:curator-223be9c74d",
            "query_name": "Luteolin",
            "cas_rn": "491-70-3",
            "cas_name": "4H-1-Benzopyran-4-one, 2-(3,4-dihydroxyphenyl)-5,7-dihydroxy-",
            "molecular_formula": "C15H10O6",
            "canonical_smiles": "O=c1cc(-c2ccc(O)c(O)c2)oc2cc(O)cc(O)c12",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=IQPNAANSBPBGFQ-UHFFFAOYSA-N",
        },
        {
            "group": "antibiotic_inchi_fallback",
            "mech": "AntibioticMech",
            "identifier": "antibioticmech:curator-223be9c74d",
            "query_name": "Luteolin",
            "cas_rn": "491-70-3",
            "cas_name": "4H-1-Benzopyran-4-one, 2-(3,4-dihydroxyphenyl)-5,7-dihydroxy-",
            "molecular_formula": "C15H10O6",
            "canonical_smiles": "O=c1cc(-c2ccc(O)c(O)c2)oc2cc(O)cc(O)c12",
            "inchi": "InChI=1S/...",
            "inchikey": "InChIKey=IQPNAANSBPBGFQ-UHFFFAOYSA-N",
        },
    ]
    dup_eval = evaluate_cas_rows(
        dup_cas_rows,
        {
            "antibioticmech:curator-223be9c74d": {
                "identifier": "antibioticmech:curator-223be9c74d",
                "label": "Luteolin flavone",
                "grounding_status": "MINTED",
                "chemical_structure": {"standard_inchi_key": "IQPNAANSBPBGFQ-UHFFFAOYSA-N"},
            }
        },
        {},
        {"IQPNAANSBPBGFQ-UHFFFAOYSA-N": ("CHEBI:15864", "luteolin")},
    )
    assert all(r["grounding_action"] == "CURATOR_XREF_READY" for r in dup_eval)

"""The structural-biology axis: what a solved structure does and does not claim.

A PDB accession is a MACROMOLECULAR assembly. Three of them were sitting in
chemical `xrefs`, a field whose contract is "the same structure", where they
asserted that ampicillin IS an anti-ampicillin antibody complex and that
alsterpaullone IS human GSK3-beta. Dropping them fixed the false equivalence and
lost the information; this is the destination #95 asked for.

The distinction the tests below defend is `relevance`. A solved complex is not
evidence of an antimicrobial target until someone establishes what the
macromolecule is — and for two of the three, it is known NOT to be one.
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from antibioticmech.validation.write_validated import (  # noqa: E402
    validate_antibiotic as validate_record,
)


def _records():
    return [yaml.safe_load(Path(p).read_text(encoding="utf-8"))
            for p in glob.glob(str(REPO_ROOT / "data" / "antibiotics" / "**" / "*.yaml"),
                               recursive=True)]


def _record_with(observations):
    return {
        "identifier": "CHEBI:1",
        "label": "test compound",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "chemical_structure": {"standard_inchi_key": "AAAAAAAAAAAAAA-AAAAAAAAAA-A"},
        "source_concepts": [{"source": "CHEBI", "source_id": "CHEBI:1",
                             "source_label": "test compound",
                             "minted_identifier": "antibioticmech:chebi-0000000000"}],
        "structural_observations": observations,
    }


def test_a_pdb_accession_never_appears_as_a_chemical_xref():
    """The original defect: a macromolecular entry in a same-structure field."""
    offenders = []
    for record in _records():
        for xref in record.get("xrefs") or []:
            if xref.split(":", 1)[0].lower() == "pdb":
                offenders.append(f"{record['identifier']}: {xref}")
    assert offenders == [], offenders


def test_the_migrated_accessions_are_present_and_unreviewed():
    """Moved, not deleted — and not silently upgraded to evidence either."""
    seen = {item["structure_id"]: item
            for record in _records()
            for item in record.get("structural_observations") or []}
    assert {"PDB:1H8S", "PDB:1Q3W", "PDB:1CLY"} <= set(seen), sorted(seen)
    for structure_id, item in seen.items():
        assert item["relevance"] == "UNREVIEWED", (
            f"{structure_id} was classified without a curator; the seeder cannot "
            "know what the macromolecule is")
        assert item["evidence_status"] == "PRIMARY_EVIDENCE_NEEDED"
        assert not item.get("evidence"), (
            f"{structure_id} carries evidence the inventories do not contain")


def test_a_target_complex_claim_requires_a_citation():
    """The rule that makes `relevance` mean something.

    Without it, relabelling PDB:1H8S as a TARGET_COMPLEX would turn an
    anti-ampicillin antibody into structural evidence for ampicillin's target,
    with nothing to check it against.
    """
    uncited = _record_with([{
        "structure_id": "PDB:1H8S",
        "relevance": "TARGET_COMPLEX",
        "evidence_status": "PRIMARY_EVIDENCE",
        "source": "CHEBI",
    }])
    problems = validate_record(uncited)
    assert problems != [], "a TARGET_COMPLEX with no citation must be rejected"
    assert any("evidence" in str(p).lower() for p in problems), (
        f"rejected for the wrong reason, not the missing citation: {problems}")

    cited = _record_with([{
        "structure_id": "PDB:1H8S",
        "relevance": "TARGET_COMPLEX",
        "evidence_status": "PRIMARY_EVIDENCE",
        "source": "CHEBI",
        "evidence": [{"reference": "DOI:10.1038/example"}],
    }])
    assert validate_record(cited) == [], validate_record(cited)


def test_the_three_experimental_methods_and_a_ligand_mismatch_validate():
    """X-ray, cryo-EM and NMR, plus the case the ligand is not this record.

    A structure of a SALT or a close analogue is still informative and must be
    expressible without claiming to be a structure of this compound.
    """
    xray = {
        "structure_id": "PDB:1ABC", "relevance": "APO_TARGET",
        "method": "X_RAY_DIFFRACTION", "resolution_angstroms": 1.8,
        "chains": ["A", "B"], "taxon_id": "NCBITaxon:562",
        "evidence_status": "DATABASE_ASSERTION_ONLY", "source": "CHEBI",
    }
    cryoem = {
        "structure_id": "EMDB:EMD-1234", "relevance": "TARGET_COMPLEX",
        "method": "ELECTRON_MICROSCOPY", "resolution_angstroms": 3.2,
        "biological_assembly": "70S ribosome",
        "evidence_status": "PRIMARY_EVIDENCE", "source": "curator",
        "evidence": [{"reference": "PMID:12345678"}],
    }
    nmr = {
        "structure_id": "PDB:2XYZ", "relevance": "NOT_RELEVANT",
        "method": "SOLUTION_NMR",   # no resolution: NMR does not produce one
        "evidence_status": "DATABASE_ASSERTION_ONLY", "source": "CHEBI",
    }
    mismatch = {
        "structure_id": "PDB:3DEF", "relevance": "RESISTANCE_ENZYME_COMPLEX",
        "method": "X_RAY_DIFFRACTION", "resolution_angstroms": 2.1,
        "ligand_component": "pdb-ccd:AIC", "ligand_matches_record": False,
        "conformational_note": "acyl-enzyme intermediate",
        "binding_site_residues": ["Ser70", "Lys73"],
        "evidence_status": "DATABASE_ASSERTION_ONLY", "source": "curator",
    }
    problems = validate_record(_record_with([xray, cryoem, nmr, mismatch]))
    assert problems == [], problems


def test_a_ligand_component_is_not_a_structure_accession():
    """`pdb-ccd` identifies the LIGAND; it must not be usable as the structure."""
    bad = _record_with([{
        "structure_id": "pdb-ccd:AIC", "relevance": "UNREVIEWED",
        "evidence_status": "PRIMARY_EVIDENCE_NEEDED", "source": "CHEBI",
    }])
    assert validate_record(bad) != [], (
        "a ligand chemical component was accepted as a macromolecular accession")


def test_the_seeder_migrates_a_pdb_xref_and_classifies_nothing():
    """The WIRING, not the committed result.

    The tests above read the corpus, and a corpus-state assertion cannot fail
    from a code change — mutating the seeder does not rewrite committed files.
    Making the seeder emit TARGET_COMPLEX, or putting PDB back into chemical
    xrefs, both left every other test in this file green.
    """
    import yaml as _yaml
    from seed_from_sources import CONF_PATH, Concept, build_record, structural_observations

    concept = Concept("CHEBI", "CHEBI:28971", "ampicillin")
    concept.xrefs = ["PDB:1h8s", "pdb-ccd:AIC", "cas:69-53-4"]
    concept.structure = {"standard_inchi_key": "AVKUERGKIZMTKX-NJBDSQKTSA-N",
                         "standard_inchi": "InChI=1S/x"}

    observations = structural_observations([concept], "2026-09-02", "2026-09-02")
    assert [o["structure_id"] for o in observations] == ["PDB:1H8S"], observations
    assert observations[0]["relevance"] == "UNREVIEWED", (
        "the seeder cannot know what the macromolecule is and must not say")
    assert observations[0]["evidence_status"] == "PRIMARY_EVIDENCE_NEEDED"

    conf = _yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    record = build_record("CHEBI:28971", "EXACT", [concept], conf, "2026-09-02")
    assert not [x for x in record.get("xrefs") or []
                if x.split(":", 1)[0].lower() == "pdb"], (
        "a macromolecular accession is back in a same-structure field")
    assert [o["structure_id"] for o in record["structural_observations"]] == ["PDB:1H8S"]
    # And the ligand component stayed where it belongs.
    assert "pdb-ccd:AIC" in record["xrefs"]


def test_a_curator_addition_does_not_break_reproduction():
    """The field's whole purpose is curation, and the first curated item broke it.

    `seeded_structural_view` compared EVERY observation, so adding one made
    `just verify-corpus` fail and stay failing — the defect #65 records, in a new
    field. It now compares only the slice the seeder writes, the same way
    card_sourced_view and mibig_sourced_producer_view do (#173).
    """
    from seed_from_sources import seeded_structural_view

    seeded = {"structural_observations": [
        {"structure_id": "PDB:1H8S", "source": "CHEBI"}]}
    curated = {"structural_observations": [
        # a curator classified the seeded one ...
        {"structure_id": "PDB:1H8S", "source": "CHEBI", "relevance": "ANTIBODY_COMPLEX"},
        # ... and added their own
        {"structure_id": "PDB:9XYZ", "source": "curator", "relevance": "TARGET_COMPLEX"}]}
    assert seeded_structural_view(seeded) == seeded_structural_view(curated)

    # But a seeded observation may not vanish, and one may not be forged under
    # the seeder's provenance.
    deleted = {"structural_observations": []}
    assert seeded_structural_view(seeded) != seeded_structural_view(deleted)
    forged = {"structural_observations": [
        {"structure_id": "PDB:1H8S", "source": "CHEBI"},
        {"structure_id": "PDB:9XYZ", "source": "CHEBI"}]}
    assert seeded_structural_view(seeded) != seeded_structural_view(forged)


def test_a_malformed_accession_is_skipped_not_emitted():
    """One bad upstream xref must not cost a whole record.

    write_validated_antibiotic validates the entire record, so emitting a
    malformed `structure_id` made an otherwise good compound unwritable (#174).
    """
    from seed_from_sources import (
        MALFORMED_STRUCTURE_IDS,
        STRUCTURE_ID_PATTERN,
        Concept,
        structural_observations,
    )

    MALFORMED_STRUCTURE_IDS.clear()
    concept = Concept("CHEBI", "CHEBI:1", "x")
    concept.xrefs = ["pdb:NOTANID", "pdb:12", "pdb:1h8s"]
    emitted = structural_observations([concept], "v", "d")
    assert [o["structure_id"] for o in emitted] == ["PDB:1H8S"], emitted
    assert len(MALFORMED_STRUCTURE_IDS) == 2, MALFORMED_STRUCTURE_IDS

    # The migration and the schema must enforce the SAME shape, or a value the
    # migration accepts is one the write gate rejects.
    schema = yaml.safe_load(
        (REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"
         ).read_text(encoding="utf-8"))
    declared = schema["classes"]["StructuralObservation"]["attributes"]["structure_id"]["pattern"]
    assert declared == STRUCTURE_ID_PATTERN, (
        f"schema says {declared!r}, migration uses {STRUCTURE_ID_PATTERN!r}")


def test_pdb_ccd_xrefs_are_untouched():
    """The migration must not have swept up chemical identity metadata."""
    count = sum(1 for record in _records()
                for xref in record.get("xrefs") or []
                if xref.startswith("pdb-ccd:"))
    assert count > 300, f"pdb-ccd xrefs collapsed to {count}; they are ligand identity"

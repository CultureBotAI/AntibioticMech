"""The write gate: validation before disk, and byte-identical re-emission.

Re-emitting an unchanged record must produce the same bytes. That is what makes
a bulk rewrite safe to review: a script that touches one field produces a
one-field diff instead of burying it in serializer churn.
"""

from __future__ import annotations

import pytest
import yaml

from antibioticmech.validation.write_validated import (
    ValidationFailedError,
    emit_antibiotic_yaml,
    validate_antibiotic,
    write_validated_antibiotic,
)

# The smallest record the schema accepts. It carries a structure, an
# attestation and a grounding status because the corpus's central claim — a
# record IS a chemical structure — is enforced by the write gate, not merely by
# a corpus-wide test.
MINIMAL = {
    "identifier": "CHEBI:42355",
    "label": "erythromycin A",
    "antimicrobial_class": "ANTIBACTERIAL",
    "curation_status": "SEEDED",
    "grounding_status": "EXACT",
    "chemical_structure": {"standard_inchi_key": "ULGZDMOVFRHVEP-RWJQBGPGSA-N"},
    "source_concepts": [{
        "source": "CHEBI",
        "source_id": "CHEBI:42355",
        "source_label": "erythromycin A",
        "minted_identifier": "antibioticmech:chebi-0000000000",
    }],
}


def test_a_valid_record_is_written(tmp_path):
    path = tmp_path / "erythromycin.yaml"
    write_validated_antibiotic(dict(MINIMAL), path)
    assert yaml.safe_load(path.read_text())["identifier"] == "CHEBI:42355"


def test_a_record_without_a_structure_is_rejected(tmp_path):
    """The corpus's central invariant, enforced where CLAUDE.md says every write
    goes: a name is not a structure, and a structureless record must not reach
    disk even if every other field is present."""
    doc = {k: v for k, v in MINIMAL.items() if k != "chemical_structure"}
    with pytest.raises(ValidationFailedError):
        write_validated_antibiotic(doc, tmp_path / "bad.yaml")

    no_key = dict(MINIMAL) | {"chemical_structure": {"smiles": "CCO"}}
    assert validate_antibiotic(no_key)


def test_an_mic_without_units_or_assay_is_rejected(tmp_path):
    """A number without a method is not an observation — a schema rule now, not
    only a corpus test, so it holds for the first curated record too."""
    bare = dict(MINIMAL) | {"activity_spectrum": [
        {"taxon_label": "Escherichia coli", "mic_value": 2.0,
         "evidence": [{"reference": "PMID:1"}]}]}
    assert validate_antibiotic(bare)
    complete = dict(MINIMAL) | {"activity_spectrum": [
        {"taxon_label": "Escherichia coli", "mic_value": 2.0, "mic_units": "mg/L",
         "assay": "CLSI broth microdilution", "evidence": [{"reference": "PMID:1"}]}]}
    assert not validate_antibiotic(complete)


def test_an_unknown_field_is_rejected_and_nothing_is_written(tmp_path):
    """Closed-mode validation. In LinkML's default open mode this record passes
    and a typo becomes a silently ignored field."""
    path = tmp_path / "bad.yaml"
    doc = dict(MINIMAL) | {"antimicrobal_class": "ANTIBACTERIAL"}
    with pytest.raises(ValidationFailedError):
        write_validated_antibiotic(doc, path)
    assert not path.exists()


def test_a_missing_required_field_is_rejected(tmp_path):
    doc = {k: v for k, v in MINIMAL.items() if k != "curation_status"}
    with pytest.raises(ValidationFailedError):
        write_validated_antibiotic(doc, tmp_path / "bad.yaml")


def test_a_bad_enum_value_is_rejected(tmp_path):
    doc = dict(MINIMAL) | {"antimicrobial_class": "ANTIBIOTIC"}
    with pytest.raises(ValidationFailedError):
        write_validated_antibiotic(doc, tmp_path / "bad.yaml")


def test_a_malformed_curie_is_rejected(tmp_path):
    doc = dict(MINIMAL) | {"xrefs": ["not a curie"]}
    assert validate_antibiotic(doc)


def test_a_malformed_inchikey_is_rejected(tmp_path):
    doc = dict(MINIMAL) | {"chemical_structure": {"standard_inchi_key": "NOTAKEY"}}
    assert validate_antibiotic(doc)


def test_every_committed_record_re_emits_byte_identically(records):
    """Corpus-wide. A record hand-edited into a shape safe_dump would not emit
    breaks this: reformat through the helper rather than loosening the test."""
    drifted = []
    for path, record in records:
        if emit_antibiotic_yaml(record) != path.read_text(encoding="utf-8"):
            drifted.append(path.name)
    assert drifted == [], drifted[:20]

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import numpy as np
import pytest
import yaml
from rdkit import Chem, DataStructs

from antibioticmech.chemical_embedding import (
    EmbeddingConfig,
    StructureEmbeddingError,
    StructureRecord,
    corpus_fingerprint,
    dependency_versions,
    display_hash,
    expected_artifact_metadata,
    load_structure_records,
    morgan_fingerprints,
    parse_structure,
    parse_structures,
    serialize_artifact,
    structure_hash,
    validate_artifact,
    weighted_tanimoto_distances,
)


def record(
    *,
    identifier: str = "CHEBI:1",
    label: str = "lactic acid",
    smiles: str = "C[C@H](O)C(=O)O",
    inchi: str | None = None,
) -> StructureRecord:
    molecule = Chem.MolFromSmiles(smiles)
    generated_inchi = Chem.MolToInchi(molecule) if molecule is not None else ""
    generated_key = Chem.InchiToInchiKey(inchi or generated_inchi)
    return StructureRecord(
        identifier=identifier,
        label=label,
        antimicrobial_class="ANTIBACTERIAL",
        structural_class="test class",
        grounding_status="EXACT",
        curation_status="SEEDED",
        smiles=smiles,
        standard_inchi=inchi or generated_inchi,
        standard_inchi_key=generated_key,
        page_path="antibacterial/test.html",
        synonyms=("test synonym",),
    )


def test_load_structure_records_requires_exact_paths_set(tmp_path: Path):
    corpus = tmp_path / "antibiotics"
    directory = corpus / "antibacterial"
    directory.mkdir(parents=True)
    structure = record()
    document = {
        "identifier": structure.identifier,
        "label": structure.label,
        "antimicrobial_class": structure.antimicrobial_class,
        "structural_class": structure.structural_class,
        "grounding_status": structure.grounding_status,
        "curation_status": structure.curation_status,
        "chemical_structure": {
            "smiles": structure.smiles,
            "standard_inchi": structure.standard_inchi,
            "standard_inchi_key": structure.standard_inchi_key,
        },
        "synonyms": [{"synonym_text": "test synonym"}],
    }
    (directory / "test.yaml").write_text(
        yaml.safe_dump(document, sort_keys=False), encoding="utf-8"
    )
    paths = corpus / "PATHS.tsv"
    paths.write_text(
        "identifier\tantimicrobial_class\tslug\n"
        "CHEBI:1\tANTIBACTERIAL\ttest\n",
        encoding="utf-8",
    )

    loaded = load_structure_records(corpus, paths)

    assert loaded == [structure]
    paths.write_text(
        paths.read_text(encoding="utf-8")
        + "CHEBI:missing\tANTIBACTERIAL\tmissing\n",
        encoding="utf-8",
    )
    with pytest.raises(StructureEmbeddingError, match="does not match PATHS"):
        load_structure_records(corpus, paths)


def test_parser_uses_inchi_fallback_and_fails_closed():
    methane_inchi = "InChI=1S/CH4/h1H4"
    fallback = record(smiles="not valid smiles", inchi=methane_inchi)

    parsed = parse_structure(fallback)

    assert parsed.structure_input == "INCHI_FALLBACK"
    assert parsed.canonical_isomeric_smiles == "C"

    broken = replace(fallback, standard_inchi="not an InChI")
    with pytest.raises(StructureEmbeddingError, match="rejected"):
        parse_structure(broken)


def test_randomized_smiles_leave_fingerprints_and_distance_unchanged():
    molecule = Chem.MolFromSmiles("C[C@H](O)F")
    randomized = Chem.MolToSmiles(
        molecule, canonical=False, doRandom=True, isomericSmiles=True
    )
    first = record(identifier="CHEBI:1", smiles="C[C@H](O)F")
    second = record(identifier="CHEBI:2", smiles=randomized)
    config = EmbeddingConfig()

    fingerprints = morgan_fingerprints(parse_structures([first, second]), config)
    distances = weighted_tanimoto_distances(fingerprints, config)

    assert DataStructs.TanimotoSimilarity(fingerprints[0][0], fingerprints[0][1]) == 1
    assert DataStructs.TanimotoSimilarity(fingerprints[1][0], fingerprints[1][1]) == 1
    assert float(distances[0, 1]) == 0


def test_selected_representation_separates_enantiomers():
    first = record(identifier="CHEBI:1", smiles="C[C@H](O)F")
    second = record(identifier="CHEBI:2", smiles="C[C@@H](O)F")
    config = EmbeddingConfig()

    fingerprints = morgan_fingerprints(parse_structures([first, second]), config)
    distances = weighted_tanimoto_distances(fingerprints, config)

    assert distances.dtype == np.float32
    assert float(distances[0, 1]) > 0
    assert np.array_equal(distances, distances.T)


def test_nonstructure_metadata_does_not_change_structure_hash():
    original = record()
    edited = replace(
        original,
        label="renamed",
        structural_class="different display class",
        synonyms=("another synonym",),
    )
    versions = dependency_versions()

    assert structure_hash([original], EmbeddingConfig(), versions) == structure_hash(
        [edited], EmbeddingConfig(), versions
    )
    assert display_hash([original]) != display_hash([edited])
    assert corpus_fingerprint([original]) != corpus_fingerprint([edited])


def test_artifact_validation_checks_hashes_coverage_and_quality():
    records = [record()]
    artifact = expected_artifact_metadata(records)
    artifact.update(
        {
            "versions": dependency_versions(),
            "records": [{"identifier": records[0].identifier}],
            "quality": {
                "trustworthiness_at_10": 0.97,
                "neighbor_overlap_at_10": 0.49,
                "zero_distance_stereoisomer_pairs": 0,
            },
        }
    )

    assert validate_artifact(artifact, records) == []

    artifact["corpus_fingerprint"] = "stale"
    artifact["records"] = []
    artifact["quality"]["neighbor_overlap_at_10"] = 0.1
    assert validate_artifact(artifact, records) == [
        "corpus_fingerprint is stale",
        "artifact identifiers do not exactly match PATHS.tsv order",
        "neighbor_overlap_at_10 is below 0.45",
    ]


def test_serialization_is_compact_deterministic_json():
    artifact = {"z": [2, 1], "a": "β"}

    first = serialize_artifact(artifact)
    second = serialize_artifact(artifact)

    assert first == second == '{"a":"β","z":[2,1]}\n'
    assert json.loads(first) == artifact

"""Deterministic, structure-only embedding support for the chemical map.

The public contract is deliberately narrower than an ordinary molecular
machine-learning feature pipeline: only the exact stored structure may affect
fingerprints, distances, neighbors, or coordinates. Record prose and biological
annotations are carried separately for display.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.metadata
import json
import sys
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from rdkit import Chem, DataStructs, rdBase
from rdkit.Chem import rdFingerprintGenerator
from sklearn.manifold import trustworthiness

MODEL_VERSION = (
    "morgan-count-chiral-r2_0.90-r4_0.10+tanimoto"
    "+umap-precomputed-n15-d0.05-c2-rs42"
)
ARTIFACT_SCHEMA_VERSION = 2


class StructureEmbeddingError(ValueError):
    """Raised when a corpus record cannot satisfy the map contract."""


@dataclass(frozen=True)
class EmbeddingConfig:
    radii: tuple[int, int] = (2, 4)
    weights: tuple[float, float] = (0.9, 0.1)
    include_chirality: bool = True
    n_neighbors: int = 15
    min_dist: float = 0.05
    n_components: int = 2
    random_state: int = 42
    quality_neighbors: int = 10


DEFAULT_CONFIG = EmbeddingConfig()


@dataclass(frozen=True)
class StructureRecord:
    identifier: str
    label: str
    antimicrobial_class: str
    structural_class: str
    grounding_status: str
    curation_status: str
    smiles: str
    standard_inchi: str
    standard_inchi_key: str
    page_path: str
    synonyms: tuple[str, ...]


@dataclass(frozen=True)
class ParsedStructure:
    record: StructureRecord
    molecule: Any
    canonical_isomeric_smiles: str
    canonical_connectivity_smiles: str
    structure_input: str
    fragment_count: int


def dependency_versions() -> dict[str, str]:
    """Return versions that can change fingerprints or projected coordinates."""

    def version(distribution: str) -> str:
        return importlib.metadata.version(distribution)

    return {
        "python": ".".join(str(part) for part in sys.version_info[:3]),
        "rdkit": rdBase.rdkitVersion,
        "numpy": np.__version__,
        "scikit_learn": version("scikit-learn"),
        "umap": version("umap-learn"),
    }


def configuration_dict(config: EmbeddingConfig) -> dict[str, Any]:
    data = asdict(config)
    data["radii"] = list(config.radii)
    data["weights"] = list(config.weights)
    return data


def _load_lockfile(paths_file: Path) -> dict[str, tuple[str, str]]:
    with paths_file.open(encoding="utf-8", newline="") as stream:
        rows = csv.DictReader(stream, delimiter="\t")
        required = {"identifier", "antimicrobial_class", "slug"}
        if set(rows.fieldnames or ()) != required:
            raise StructureEmbeddingError(
                f"{paths_file} must have columns {sorted(required)}, got {rows.fieldnames}"
            )
        locked = {
            row["identifier"]: (row["antimicrobial_class"], row["slug"])
            for row in rows
        }
    if not locked:
        raise StructureEmbeddingError(f"{paths_file} is empty")
    return locked


def load_structure_records(corpus_dir: Path, paths_file: Path) -> list[StructureRecord]:
    """Load exactly the lockfile set and sort it by identifier."""

    locked = _load_lockfile(paths_file)
    documents: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted(corpus_dir.rglob("*.yaml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(document, dict) or not document.get("identifier"):
            raise StructureEmbeddingError(f"{path} is not an antibiotic record")
        identifier = str(document["identifier"])
        if identifier in documents:
            raise StructureEmbeddingError(f"duplicate corpus identifier: {identifier}")
        documents[identifier] = (path, document)

    expected = set(locked)
    actual = set(documents)
    if expected != actual:
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        raise StructureEmbeddingError(
            "corpus does not match PATHS.tsv: "
            f"missing={missing[:5]}, unexpected={unexpected[:5]}"
        )

    records: list[StructureRecord] = []
    for identifier in sorted(expected):
        path, document = documents[identifier]
        locked_class, locked_slug = locked[identifier]
        if path.stem != locked_slug:
            raise StructureEmbeddingError(
                f"{identifier}: PATHS.tsv slug {locked_slug!r} != {path.stem!r}"
            )
        structure = document.get("chemical_structure") or {}
        smiles = structure.get("smiles")
        inchi = structure.get("standard_inchi")
        inchi_key = structure.get("standard_inchi_key")
        if not all(isinstance(value, str) and value for value in (smiles, inchi, inchi_key)):
            raise StructureEmbeddingError(
                f"{identifier}: SMILES, standard InChI, and InChIKey are required"
            )
        synonyms = tuple(
            sorted(
                {
                    str(item["synonym_text"])
                    for item in (document.get("synonyms") or [])
                    if isinstance(item, dict) and item.get("synonym_text")
                },
                key=lambda value: (value.casefold(), value),
            )
        )
        records.append(
            StructureRecord(
                identifier=identifier,
                label=str(document["label"]),
                antimicrobial_class=str(document.get("antimicrobial_class") or ""),
                structural_class=str(document.get("structural_class") or ""),
                grounding_status=str(document.get("grounding_status") or ""),
                curation_status=str(document.get("curation_status") or ""),
                smiles=smiles,
                standard_inchi=inchi,
                standard_inchi_key=inchi_key,
                page_path=f"{path.parent.name}/{path.stem}.html",
                synonyms=synonyms,
            )
        )
        if locked_class != records[-1].antimicrobial_class:
            raise StructureEmbeddingError(
                f"{identifier}: PATHS.tsv class {locked_class!r} != "
                f"{records[-1].antimicrobial_class!r}"
            )
    return records


def parse_structure(record: StructureRecord) -> ParsedStructure:
    """Parse SMILES first, then the required standard-InChI fallback."""

    blocker = rdBase.BlockLogs()
    try:
        molecule = Chem.MolFromSmiles(record.smiles)
    finally:
        del blocker
    structure_input = "SMILES"
    if molecule is None:
        blocker = rdBase.BlockLogs()
        try:
            molecule = Chem.MolFromInchi(record.standard_inchi)
        finally:
            del blocker
        structure_input = "INCHI_FALLBACK"
    if molecule is None:
        raise StructureEmbeddingError(
            f"{record.identifier}: RDKit rejected stored SMILES and standard InChI"
        )
    return ParsedStructure(
        record=record,
        molecule=molecule,
        canonical_isomeric_smiles=Chem.MolToSmiles(
            molecule, canonical=True, isomericSmiles=True
        ),
        canonical_connectivity_smiles=Chem.MolToSmiles(
            molecule, canonical=True, isomericSmiles=False
        ),
        structure_input=structure_input,
        fragment_count=len(Chem.GetMolFrags(molecule)),
    )


def parse_structures(records: Iterable[StructureRecord]) -> list[ParsedStructure]:
    return [parse_structure(record) for record in records]


def morgan_fingerprints(
    parsed: list[ParsedStructure], config: EmbeddingConfig
) -> tuple[list[Any], list[Any]]:
    channels: list[list[Any]] = []
    for radius in config.radii:
        generator = rdFingerprintGenerator.GetMorganGenerator(
            radius=radius,
            includeChirality=config.include_chirality,
        )
        channels.append(
            [generator.GetSparseCountFingerprint(item.molecule) for item in parsed]
        )
    return channels[0], channels[1]


def weighted_tanimoto_distances(
    fingerprints: tuple[list[Any], list[Any]], config: EmbeddingConfig
) -> np.ndarray:
    """Build the exact, symmetric all-pairs distance matrix."""

    size = len(fingerprints[0])
    if len(fingerprints[1]) != size:
        raise StructureEmbeddingError("fingerprint channels have different lengths")
    distances = np.zeros((size, size), dtype=np.float32)
    for channel, weight in zip(fingerprints, config.weights, strict=True):
        for row in range(size - 1):
            values = np.asarray(
                DataStructs.BulkTanimotoSimilarity(
                    channel[row], channel[row + 1 :], returnDistance=True
                ),
                dtype=np.float32,
            )
            values *= np.float32(weight)
            distances[row, row + 1 :] += values
            distances[row + 1 :, row] += values
    np.fill_diagonal(distances, 0.0)
    return distances


def _nearest_indices(
    values: np.ndarray, identifiers: list[str], self_index: int, count: int
) -> list[int]:
    if count >= len(values):
        count = len(values) - 1
    # Index count is the (count + 1)th element because the diagonal/self value
    # is zero. Include every boundary tie before applying identifier tie-breaks.
    threshold = float(np.partition(values, count)[count])
    candidates = np.flatnonzero(values <= threshold)
    ordered = sorted(
        (int(index) for index in candidates if index != self_index),
        key=lambda index: (float(values[index]), identifiers[index]),
    )
    if len(ordered) < count:
        ordered = sorted(
            (index for index in range(len(values)) if index != self_index),
            key=lambda index: (float(values[index]), identifiers[index]),
        )
    return ordered[:count]


def nearest_neighbor_indices(
    distances: np.ndarray, identifiers: list[str], count: int
) -> list[list[int]]:
    return [
        _nearest_indices(distances[row], identifiers, row, count)
        for row in range(len(identifiers))
    ]


def project_distances(distances: np.ndarray, config: EmbeddingConfig) -> np.ndarray:
    import umap

    projector = umap.UMAP(
        metric="precomputed",
        n_neighbors=config.n_neighbors,
        min_dist=config.min_dist,
        n_components=config.n_components,
        random_state=config.random_state,
        n_jobs=1,
    )
    return np.asarray(projector.fit_transform(distances), dtype=np.float32)


def projection_neighbor_overlap(
    high_neighbors: list[list[int]], coordinates: np.ndarray, count: int
) -> float:
    overlaps = []
    identifiers = [str(index) for index in range(len(coordinates))]
    for row, expected in enumerate(high_neighbors):
        delta = coordinates - coordinates[row]
        squared = np.einsum("ij,ij->i", delta, delta)
        observed = _nearest_indices(squared, identifiers, row, count)
        overlaps.append(len(set(expected[:count]) & set(observed)) / count)
    return float(np.mean(overlaps))


def structure_hash(
    records: list[StructureRecord],
    config: EmbeddingConfig,
    versions: dict[str, str],
) -> str:
    payload = {
        "model_version": MODEL_VERSION,
        "configuration": configuration_dict(config),
        # Record Python for provenance, but do not make a 3.10 vs 3.12 QC
        # matrix stale when the locked chemistry stack is otherwise identical.
        "versions": {key: value for key, value in versions.items() if key != "python"},
        "records": [
            {
                "identifier": record.identifier,
                "smiles": record.smiles,
                "standard_inchi": record.standard_inchi,
            }
            for record in records
        ],
    }
    return _sha256(payload)


def display_hash(records: list[StructureRecord]) -> str:
    payload = [
        {
            "identifier": record.identifier,
            "label": record.label,
            "page_path": record.page_path,
            "antimicrobial_class": record.antimicrobial_class,
            "structural_class": record.structural_class,
            "grounding_status": record.grounding_status,
            "curation_status": record.curation_status,
            "synonyms": record.synonyms,
        }
        for record in records
    ]
    return _sha256(payload)


def corpus_fingerprint(records: list[StructureRecord]) -> str:
    """Hash the normalized corpus inputs from which the artifact is built.

    Unlike a commit SHA, this fingerprint remains valid after rebases and also
    describes uncommitted inputs accurately.  Model configuration and runtime
    dependencies remain the separate concern of ``input_hash`` and
    ``structure_hash``.
    """

    return _sha256([asdict(record) for record in records])


def _sha256(payload: Any) -> str:
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def _duplicate_groups(parsed: list[ParsedStructure]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for item in parsed:
        groups[item.record.standard_inchi_key].append(item.record.identifier)
    return [
        sorted(identifiers)
        for identifiers in groups.values()
        if len(identifiers) > 1
    ]


def _stereoisomer_audit(
    parsed: list[ParsedStructure], distances: np.ndarray
) -> tuple[int, int]:
    groups: dict[str, list[int]] = defaultdict(list)
    for index, item in enumerate(parsed):
        groups[item.canonical_connectivity_smiles].append(index)
    pair_count = 0
    zero_count = 0
    for indices in groups.values():
        for left_pos, left in enumerate(indices):
            for right in indices[left_pos + 1 :]:
                if (
                    parsed[left].canonical_isomeric_smiles
                    == parsed[right].canonical_isomeric_smiles
                ):
                    continue
                pair_count += 1
                if float(distances[left, right]) <= 1e-12:
                    zero_count += 1
    return pair_count, zero_count


def build_artifact(
    records: list[StructureRecord],
    config: EmbeddingConfig = DEFAULT_CONFIG,
) -> dict[str, Any]:
    """Run the complete exact model and return its deterministic artifact."""

    versions = dependency_versions()
    parsed = parse_structures(records)
    fingerprints = morgan_fingerprints(parsed, config)
    distances = weighted_tanimoto_distances(fingerprints, config)
    del fingerprints
    identifiers = [item.record.identifier for item in parsed]
    high_neighbors = nearest_neighbor_indices(
        distances, identifiers, config.n_neighbors
    )
    coordinates = project_distances(distances, config)
    quality_neighbors = nearest_neighbor_indices(
        distances, identifiers, config.quality_neighbors
    )
    stereo_pairs, stereo_zero = _stereoisomer_audit(parsed, distances)
    quality = {
        "trustworthiness_at_10": round(
            float(
                trustworthiness(
                    distances,
                    coordinates,
                    n_neighbors=config.quality_neighbors,
                    metric="precomputed",
                )
            ),
            10,
        ),
        "neighbor_overlap_at_10": round(
            projection_neighbor_overlap(
                quality_neighbors, coordinates, config.quality_neighbors
            ),
            10,
        ),
        "inchi_fallback_count": sum(
            item.structure_input == "INCHI_FALLBACK" for item in parsed
        ),
        "multifragment_count": sum(item.fragment_count > 1 for item in parsed),
        "stereoisomer_pair_count": stereo_pairs,
        "zero_distance_stereoisomer_pairs": stereo_zero,
        "duplicate_inchi_key_groups": _duplicate_groups(parsed),
    }
    if quality["trustworthiness_at_10"] < 0.95:
        raise StructureEmbeddingError(
            f"trustworthiness regression: {quality['trustworthiness_at_10']:.4f} < 0.95"
        )
    if quality["neighbor_overlap_at_10"] < 0.45:
        raise StructureEmbeddingError(
            f"neighbor-overlap regression: {quality['neighbor_overlap_at_10']:.4f} < 0.45"
        )
    if stereo_zero:
        raise StructureEmbeddingError(
            f"stereochemistry regression: {stereo_zero}/{stereo_pairs} pairs at distance zero"
        )

    rows = []
    for index, item in enumerate(parsed):
        record = item.record
        rows.append(
            {
                "identifier": record.identifier,
                "label": record.label,
                "path": record.page_path,
                "antimicrobial_class": record.antimicrobial_class,
                "structural_class": record.structural_class,
                "grounding_status": record.grounding_status,
                "curation_status": record.curation_status,
                "synonyms": list(record.synonyms),
                "canonical_isomeric_smiles": item.canonical_isomeric_smiles,
                "structure_input": item.structure_input,
                "fragment_count": item.fragment_count,
                "x": round(float(coordinates[index, 0]), 6),
                "y": round(float(coordinates[index, 1]), 6),
                "neighbors": [
                    {
                        "identifier": identifiers[neighbor],
                        "distance": round(float(distances[index, neighbor]), 6),
                    }
                    for neighbor in high_neighbors[index]
                ],
            }
        )
    structure_digest = structure_hash(records, config, versions)
    display_digest = display_hash(records)
    return {
        "schema_version": ARTIFACT_SCHEMA_VERSION,
        "model_version": MODEL_VERSION,
        "corpus_fingerprint": corpus_fingerprint(records),
        "input_hash": _sha256(
            {"structure_hash": structure_digest, "display_hash": display_digest}
        ),
        "structure_hash": structure_digest,
        "display_hash": display_digest,
        "record_count": len(rows),
        "versions": versions,
        "configuration": configuration_dict(config),
        "quality": quality,
        "records": rows,
    }


def serialize_artifact(artifact: dict[str, Any]) -> str:
    return (
        json.dumps(
            artifact,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    )


def expected_artifact_metadata(
    records: list[StructureRecord], config: EmbeddingConfig = DEFAULT_CONFIG
) -> dict[str, Any]:
    versions = dependency_versions()
    structure_digest = structure_hash(records, config, versions)
    display_digest = display_hash(records)
    return {
        "schema_version": ARTIFACT_SCHEMA_VERSION,
        "model_version": MODEL_VERSION,
        "corpus_fingerprint": corpus_fingerprint(records),
        "input_hash": _sha256(
            {"structure_hash": structure_digest, "display_hash": display_digest}
        ),
        "structure_hash": structure_digest,
        "display_hash": display_digest,
        "record_count": len(records),
        "configuration": configuration_dict(config),
    }


def validate_artifact(
    artifact: dict[str, Any],
    records: list[StructureRecord],
    config: EmbeddingConfig = DEFAULT_CONFIG,
) -> list[str]:
    """Return actionable staleness/schema errors without rebuilding UMAP."""

    errors: list[str] = []
    expected = expected_artifact_metadata(records, config)
    for key, value in expected.items():
        if artifact.get(key) != value:
            errors.append(f"{key} is stale")
    artifact_versions = artifact.get("versions") or {}
    for key, value in dependency_versions().items():
        if key != "python" and artifact_versions.get(key) != value:
            errors.append(f"versions.{key} is stale")
    rows = artifact.get("records")
    if not isinstance(rows, list):
        return [*errors, "records must be a list"]
    expected_ids = [record.identifier for record in records]
    actual_ids = [
        row.get("identifier") for row in rows if isinstance(row, dict)
    ]
    if actual_ids != expected_ids:
        errors.append("artifact identifiers do not exactly match PATHS.tsv order")
    quality = artifact.get("quality") or {}
    if quality.get("trustworthiness_at_10", 0) < 0.95:
        errors.append("trustworthiness_at_10 is below 0.95")
    if quality.get("neighbor_overlap_at_10", 0) < 0.45:
        errors.append("neighbor_overlap_at_10 is below 0.45")
    if quality.get("zero_distance_stereoisomer_pairs") != 0:
        errors.append("zero-distance stereoisomer pairs are present")
    return errors

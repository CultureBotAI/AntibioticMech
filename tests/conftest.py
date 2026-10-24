"""Shared fixtures: the corpus and the raw inventories, loaded once per session.

Parsing 2600 YAML files per test would dominate the suite's runtime, so the
corpus is a session-scoped fixture. Tests must treat it as read-only.
"""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

REPO_ROOT = Path(__file__).resolve().parents[1]

CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
RAW_DIR = REPO_ROOT / "data" / "raw"
SCHEMA_PATH = REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"


@pytest.fixture(scope="session")
def require_native_inputs():
    """Skip only optional cache consumers, never missing public inputs or corrupt pins."""

    def check(*documents):
        def visit(value):
            if isinstance(value, dict):
                path = value.get("path")
                if (
                    isinstance(path, str) and path.startswith("reports/")
                    and "sha256" in value and not (REPO_ROOT / path).is_file()
                ):
                    pytest.skip(f"optional native research cache unavailable: {path}")
                for item in value.values():
                    visit(item)
            elif isinstance(value, list):
                for item in value:
                    visit(item)

        for document in documents:
            visit(document)

    return check


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_path() -> Path:
    return SCHEMA_PATH


@pytest.fixture(scope="session")
def records() -> list[tuple[Path, dict]]:
    """Every seeded AntibioticRecord as (path, parsed doc)."""
    if not CORPUS_DIR.exists():
        pytest.skip(f"no corpus at {CORPUS_DIR}; run `just seed-apply`")
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        out.append((path, load_record(path)))
    if not out:
        pytest.skip(f"corpus at {CORPUS_DIR} is empty")
    return out


@pytest.fixture(scope="session")
def path_lockfile() -> dict[str, str]:
    """The committed identifier -> slug assignments in data/antibiotics/PATHS.tsv."""
    path = CORPUS_DIR / "PATHS.tsv"
    if not path.exists():
        pytest.skip(f"no lockfile at {path}; run `just seed-apply`")
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["slug"] for r in csv.DictReader(fh, delimiter="\t")}


@pytest.fixture(scope="session")
def raw_tsv():
    """Callable returning a parsed data/raw TSV by filename."""
    cache: dict[str, list[dict[str, str]]] = {}

    def _load(name: str) -> list[dict[str, str]]:
        if name not in cache:
            path = RAW_DIR / name
            if not path.exists():
                pytest.skip(f"missing inventory {path}; run `just extract-inventory`")
            with path.open(newline="", encoding="utf-8") as fh:
                cache[name] = list(csv.DictReader(fh, delimiter="\t"))
        return cache[name]

    return _load


def _qualification_deltas(root):
    payload = (root / "research/2026-10-15-card-evidence-qualifications-verification.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "1e6378c711d7627465a26602f6ac3129c8a4f478bb26646cf7d232ad3e89152c"
    )
    deltas = json.loads(payload)["record_deltas"]
    assert len(deltas) == 3
    return {row["path"]: row for row in deltas}


def _restore_pre_qualification(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    delta = _qualification_deltas(root)[relative_path]
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"][-1]["action"] == "RESEEDED_FROM_SOURCES"
    historical["curation_history"].pop()
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note").startswith("Evidence-scope review ")
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_card_qualification():
    return _restore_pre_qualification


@pytest.fixture(scope="session")
def pre_card_qualification_root(tmp_path_factory, pre_cdsa_qualification_root):
    """Reconstruct only the three pinned note/history deltas, never the live files."""
    root = tmp_path_factory.mktemp("pre-card-qualification")
    source = pre_cdsa_qualification_root
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "curation", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    for relative in _qualification_deltas(source):
        _restore_pre_qualification(source, relative, root / relative)
    return root


def _cdsa_transition(root):
    payload = (root / "research/2026-10-15-cdsa-qualification-transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "b5c28727895c2b88845978f0e6afe158371e1b3e2be8633a465cdcf14adca0b8"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 4
    return transition


def _restore_pre_cdsa(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _cdsa_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note") == change["after_note"]
        if change["before_note"] is not None:
            claim["note"] = change["before_note"]
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_cdsa_qualification():
    return _restore_pre_cdsa


@pytest.fixture(scope="session")
def pre_cdsa_qualification_root(tmp_path_factory, pre_salmonella_qualification_root):
    """Reconstruct the exact prior notes, history and active review file in isolation."""
    source = pre_salmonella_qualification_root
    transition = _cdsa_transition(source)
    review = transition["review_file"]
    assert hashlib.sha256((source / review["path"]).read_bytes()).hexdigest() == (
        review["after_sha256"]
    )
    archive = transition["historical_review_fixture"]
    payload = (source / archive["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == archive["sha256"] == review["before_sha256"]
    root = tmp_path_factory.mktemp("pre-cdsa-qualification")
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (source / "curation").iterdir():
        if path.name != "card_evidence_reviews.json":
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    (root / review["path"]).write_bytes(payload)
    for delta in transition["record_deltas"]:
        _restore_pre_cdsa(source, delta["path"], root / delta["path"])
    return root


def _salmonella_transition(root):
    payload = (root / "research/2026-10-16-salmonella-qualification-transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "95953c299ce1d257958070a37882b22febb878f3c0194d54cd119eb3eb8ec4ef"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 17
    return transition


def _restore_pre_salmonella(root, relative_path, output):
    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _salmonella_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    for change in delta["claims"]:
        assert change["changed_fields"] == ["note"]
        claim = historical["resistance_mechanisms"][change["index"]]
        assert claim["aro_id"] == change["aro_id"]
        assert claim.pop("note") == change["after_note"]
        if change["before_note"] is not None:
            claim["note"] = change["before_note"]
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_salmonella_qualification():
    return _restore_pre_salmonella


@pytest.fixture(scope="session")
def pre_salmonella_qualification_root(tmp_path_factory, pre_uniprot_protein_examples_root):
    """Restore only the 17 exact note/history deltas and the prior review bytes."""
    source = pre_uniprot_protein_examples_root
    transition = _salmonella_transition(source)
    review = transition["review_file"]
    assert hashlib.sha256((source / review["path"]).read_bytes()).hexdigest() == review["after_sha256"]
    archive = transition["historical_review_fixture"]
    payload = (source / archive["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == archive["sha256"] == review["before_sha256"]
    root = tmp_path_factory.mktemp("pre-salmonella-qualification")
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (source / "curation").iterdir():
        if path.name != "card_evidence_reviews.json":
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    (root / review["path"]).write_bytes(payload)
    for delta in transition["record_deltas"]:
        _restore_pre_salmonella(source, delta["path"], root / delta["path"])
    return root


def _uniprot_protein_examples_transition(root):
    payload = (root / "curation/uniprot_protein_examples_transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "ebf6d3a2fbd9c9a201af6530cdf8917b561e123afb49e1c63e812dd157d3b8ad"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 48
    return transition


def _restore_pre_uniprot_protein_examples(root, relative_path, output):
    import copy

    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _uniprot_protein_examples_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    for change in delta["causal_node_deltas"]:
        assert change["changed_fields"] == ["protein_examples"]
        graph = historical["causal_graphs"][change["graph_index"]]
        assert graph["graph_id"] == change["graph_id"]
        node = graph["nodes"][change["node_index"]]
        assert node["node_id"] == change["node_id"]
        assert node.pop("protein_examples") == change["after_protein_examples"]
        if change["before_protein_examples"] is not None:
            node["protein_examples"] = copy.deepcopy(change["before_protein_examples"])
    for change in delta["molecular_target_deltas"]:
        assert change["changed_fields"] == ["protein_examples"]
        target = historical["molecular_targets"][change["index"]]
        assert target["source"] == change["source"] == "PRIMARY_LITERATURE"
        assert target["target_label"] == change["target_label"]
        assert target.pop("protein_examples") == change["after_protein_examples"]
        if change["before_protein_examples"] is not None:
            target["protein_examples"] = copy.deepcopy(change["before_protein_examples"])
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_uniprot_protein_examples():
    return _restore_pre_uniprot_protein_examples


@pytest.fixture(scope="session")
def pre_uniprot_protein_examples_root(tmp_path_factory, pre_causal_graphs_root):
    """Restore only the 30 curated UniProt protein-example record deltas in isolation."""
    source = pre_causal_graphs_root
    transition = _uniprot_protein_examples_transition(source)
    historical_manifest = json.loads(
        (source / "research/2026-10-15-card-reference-reconciled.json").read_bytes()
    )
    historical_identifiers = {row["identifier"] for row in historical_manifest["records"]}
    historical_paths = {row["path"] for row in historical_manifest["records"]}
    historical_slugs = {
        Path(p).relative_to("data/antibiotics").with_suffix("").as_posix()
        for p in historical_paths
    }
    root = tmp_path_factory.mktemp("pre-uniprot-protein-examples")
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for yaml_path in list((root / "data/antibiotics").rglob("*.yaml")):
        rel = yaml_path.relative_to(root).as_posix()
        if rel not in historical_paths:
            yaml_path.unlink()
    paths_tsv = root / "data/antibiotics/PATHS.tsv"
    with (source / "data/antibiotics/PATHS.tsv").open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        rows = [row for row in reader if row["slug"] in historical_slugs]
    with paths_tsv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["identifier", "slug"], delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (source / "curation").iterdir():
        if path.name == "curator_antibiotics.tsv":
            with path.open(encoding="utf-8", newline="") as fh:
                reader = csv.DictReader(fh, delimiter="\t")
                fieldnames = list(reader.fieldnames or [])
                curator_rows = [
                    row
                    for row in reader
                    if (
                        "antibioticmech:curator-"
                        + hashlib.sha256(f"CURATOR|{row['source_id']}".encode()).hexdigest()[:10]
                    )
                    in historical_identifiers
                    or any(
                        xref in historical_identifiers
                        for xref in (row.get("xrefs") or "").split("|")
                        if xref.startswith("CHEBI:")
                    )
                ]
            with (root / "curation" / path.name).open("w", encoding="utf-8", newline="") as fh:
                writer = csv.DictWriter(
                    fh, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
                )
                writer.writeheader()
                writer.writerows(curator_rows)
        elif path.name == "source_queue.tsv":
            restored = path.read_text(encoding="utf-8").replace(
                "the seeder's structure gate matches 67, of which it publishes 65:",
                "the seeder's structure gate matches the same 66, of which it publishes 64:",
                1,
            )
            (root / "curation" / path.name).write_text(restored, encoding="utf-8")
        else:
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    for delta in transition["record_deltas"]:
        if delta["path"] in historical_paths:
            _restore_pre_uniprot_protein_examples(source, delta["path"], root / delta["path"])
    return root


def _causal_graphs_transition(root):
    payload = (root / "curation/causal_graphs_transition.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == (
        "5cd564ffd4810d40f5ca8f2ae55ff94c7195ffa0295f102674ee37b7c2990cc9"
    )
    transition = json.loads(payload)
    assert len(transition["record_deltas"]) == 43
    return transition


def _restore_pre_causal_graphs(root, relative_path, output):
    import copy

    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = _causal_graphs_transition(root)
    delta = next(row for row in transition["record_deltas"] if row["path"] == relative_path)
    source = root / relative_path
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["after_sha256"]
    historical = load_record(source)
    assert historical["identifier"] == delta["identifier"]
    assert delta["history_events_added"] == 1
    assert historical["curation_history"].pop() == delta["added_history_event"]
    assert historical.pop("causal_graphs", None) == delta["after_causal_graphs"]
    if delta["before_causal_graphs"] is not None:
        historical["causal_graphs"] = copy.deepcopy(delta["before_causal_graphs"])
    write_validated_antibiotic(historical, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == delta["before_sha256"]
    return output


@pytest.fixture
def restore_pre_causal_graphs():
    return _restore_pre_causal_graphs


@pytest.fixture(scope="session")
def pre_stage5_remediation_root(tmp_path_factory):
    """Restore the 11 Stage 5 review-remediated records and held_targets additions in isolation."""
    import yaml

    from antibioticmech.validation.write_validated import write_validated_antibiotic

    transition = json.loads(
        (REPO_ROOT / "curation/stage5_review_remediation_transition.json").read_bytes()
    )
    root = tmp_path_factory.mktemp("pre-stage5-remediation")
    shutil.copytree(CORPUS_DIR, root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(REPO_ROOT / relative, target_is_directory=True)
    (root / "curation").mkdir()
    stage5_held_keys = {
        ("molecular_targets", "CHEBI:3732", "PMID:34935599"),
        ("molecular_targets", "CHEBI:600103", "PMID:40455071"),
        ("molecular_targets", "CHEBI:10100", "DOI:10.3390/antibiotics15090914"),
        ("molecular_targets", "CHEBI:34825", "DOI:10.1007/s10156-004-0327-1"),
        ("molecular_targets", "CHEBI:48480", "DOI:10.1093/nar/gkac1189"),
        ("molecular_targets", "CHEBI:28429", "DOI:10.1177/15353141261501298"),
        ("molecular_targets", "CHEBI:228412", "DOI:10.1128/spectrum.03588-25"),
        ("molecular_targets", "antibioticmech:curator-fd1c955758", "DOI:10.1093/mmy/myac049"),
        ("molecular_targets", "antibioticmech:curator-18f8e84826", "DOI:10.1128/aac.00307-23"),
    }
    promoted_existing_ids = {
        "CHEBI:3732",
        "CHEBI:100147",
        "CHEBI:100246",
        "CHEBI:50199",
        "CHEBI:100241",
        "CHEBI:600103",
        "CHEBI:63598",
        "CHEBI:45924",
        "CHEBI:119573",
        "CHEBI:63613",
    }
    for path in (REPO_ROOT / "curation").iterdir():
        if path.name == "uniprot_protein_examples.yaml":
            loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
            plan_data = yaml.load(path.read_text(encoding="utf-8"), Loader=loader)
            plan_data["held_targets"] = [
                h
                for h in (plan_data.get("held_targets") or [])
                if (h.get("scope"), h.get("identifier"), h.get("target_reference"))
                not in stage5_held_keys
            ]
            assert len(plan_data["held_targets"]) == 74
            (root / "curation" / path.name).write_text(
                yaml.dump(plan_data, sort_keys=False, allow_unicode=True, width=100),
                encoding="utf-8",
            )
        elif path.name == "causal_graphs.yaml":
            loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
            cg_data = yaml.load(path.read_text(encoding="utf-8"), Loader=loader)
            for item in cg_data.get("existing_causal_graphs") or []:
                if item.get("identifier") in promoted_existing_ids:
                    item["curation_status"] = "SEEDED"
            (root / "curation" / path.name).write_text(
                yaml.dump(cg_data, sort_keys=False, allow_unicode=True, width=100),
                encoding="utf-8",
            )
        else:
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    for entry in transition["records"]:
        rel_path = entry["path"]
        rec = load_record(REPO_ROOT / rel_path)
        assert rec["identifier"] == entry["identifier"]
        assert rec["curation_history"][-1]["action"] == "RESOLVED_REVIEW_FINDINGS"
        rec["curation_history"] = rec["curation_history"][: entry["previous_curation_history_len"]]
        for k, v in entry["previous_fields"].items():
            if v is None:
                rec.pop(k, None)
            else:
                rec[k] = v
        if "previous_molecular_targets_len" in entry:
            rec["molecular_targets"] = rec["molecular_targets"][
                : entry["previous_molecular_targets_len"]
            ]
        if "previous_daptomycin_target4_source" in entry:
            rec["molecular_targets"][4]["source"] = entry["previous_daptomycin_target4_source"]
        write_validated_antibiotic(rec, root / rel_path)
    return root


@pytest.fixture(scope="session")
def pre_causal_graphs_root(tmp_path_factory, pre_stage5_remediation_root):
    """Restore only the 36 curated causal_graphs record deltas and held_targets additions in isolation."""
    import yaml

    source = pre_stage5_remediation_root
    transition = _causal_graphs_transition(source)
    cohort_b_ids = {
        row["identifier"]
        for row in transition["record_deltas"]
        if row.get("cohort") == "non_protein_direct_or_measured_target"
    }
    root = tmp_path_factory.mktemp("pre-causal-graphs")
    shutil.copytree(source / "data/antibiotics", root / "data/antibiotics")
    for relative in ("data/raw", "research", "reports", "tests", "conf", "scripts"):
        (root / relative).symlink_to(source / relative, target_is_directory=True)
    (root / "curation").mkdir()
    for path in (source / "curation").iterdir():
        if path.name == "uniprot_protein_examples.yaml":
            loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
            plan_data = yaml.load(path.read_text(encoding="utf-8"), Loader=loader)
            plan_data["held_targets"] = [
                h
                for h in (plan_data.get("held_targets") or [])
                if not (h.get("scope") == "causal_graphs" and h.get("identifier") in cohort_b_ids)
            ]
            assert len(plan_data["held_targets"]) == 57
            (root / "curation" / path.name).write_text(
                yaml.dump(plan_data, sort_keys=False, allow_unicode=True, width=100),
                encoding="utf-8",
            )
        else:
            (root / "curation" / path.name).symlink_to(path, target_is_directory=path.is_dir())
    for delta in transition["record_deltas"]:
        _restore_pre_causal_graphs(source, delta["path"], root / delta["path"])
    return root


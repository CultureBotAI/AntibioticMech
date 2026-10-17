"""Unit tests for scripts/new_history_record.py and the history validity gate.

Ported from CellStructureMech's tests/test_new_history_record.py; issue numbers
written CellStructureMech#N refer to that repository.

The point of this scaffolder is that a record gets written on a machine with no
claw checkout, so the tests that matter are the ones about it being a genuine
drop-in: same required arguments, same field order, schema-valid output. An
interface that diverges from claw's reproduces the original trap in a new form —
a command that works with claw and fails without it (CellStructureMech#296).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from new_history_record import (  # noqa: E402
    CLAW_PLACEHOLDER,
    KIND_DIRS,
    _link,
    history_link_errors,
    history_validation_errors,
    main,
    session_id,
)
from validate_history import not_a_record  # noqa: E402
from validate_history import records as gate_records  # noqa: E402
from validate_history_links import record_paths as link_gate_records  # noqa: E402


def _kinds_from_schema() -> set[str]:
    """Parsed, not hand-copied.

    The previous version compared two hardcoded sets, so it could not notice the
    schema growing a kind — and the risk this guards is a KeyError at write time
    for a kind with no directory (CellStructureMech#296 review).
    """
    schema = yaml.safe_load((REPO_ROOT / "src/antibioticmech/schema/history.yaml").read_text())
    return set(schema["enums"]["HistoryTargetKindEnum"]["permissible_values"])

BASE = ["--kind", "record", "--slug", "erythromycin-a",
        "--target-root", "data/antibiotics/antibacterial",
        "--summary", "s", "--details", "d",
        "--timestamp", "2026-08-05T12:00:00Z"]


def _run(tmp_path, *extra):
    main(BASE + ["--history-root", str(tmp_path)] + list(extra))
    written = sorted(tmp_path.rglob("*.yaml"))
    assert len(written) == 1, written
    return yaml.safe_load(written[0].read_text()), written[0]


def test_the_record_lands_under_its_kind_directory(tmp_path):
    """history/<kind-dir>/<slug>/, not history/records/<slug>/ for every kind —
    history/infrastructure/session-history-sidecars/ is a live example. The schema
    does not constrain the path, so the wrong directory validates clean
    (CellStructureMech#296)."""
    main(["--kind", "infrastructure", "--slug", "session-history-sidecars",
          "--path", "docs/x.md", "--summary", "s", "--details", "d",
          "--history-root", str(tmp_path), "--timestamp", "2026-08-05T12:00:00Z"])
    written = next(tmp_path.rglob("*.yaml"))
    assert written.parent.parent.name == "infrastructure"
    assert written.parent.name == "session-history-sidecars"


def test_every_kind_in_the_schema_has_a_directory():
    """A missing entry would KeyError at write time rather than at parse time."""
    assert set(KIND_DIRS) == _kinds_from_schema()


def test_kind_directories_match_claw():
    """Copied from claw's scaffold.py, not inferred — the pluralisation is uneven
    (mappings/reports but schema/other), which is why guessing was wrong."""
    assert KIND_DIRS == {"record": "records", "schema": "schema",
                         "mapping": "mappings", "report": "reports",
                         "infrastructure": "infrastructure", "other": "other"}


def test_no_scratch_file_survives(tmp_path):
    _run(tmp_path)
    assert list(tmp_path.rglob("*scratch*")) == []


def test_writes_a_record_under_the_slug(tmp_path):
    doc, path = _run(tmp_path)
    assert path.parent.name == "erythromycin-a"
    assert doc["target"] == {"kind": "record", "slug": "erythromycin-a",
                             "path": "data/antibiotics/antibacterial/erythromycin-a.yaml"}
    assert (REPO_ROOT / doc["target"]["path"]).is_file()


def test_a_greek_letter_slug_is_kept_verbatim_and_never_merged(tmp_path):
    """Slugs are filename stems from data/antibiotics/PATHS.tsv, and some carry
    Greek letters. claw's slug sanitiser would turn both α-punicalagin and
    β-punicalagin into `punicalagin` — a third, real record — and file three
    records' history in one directory. Kept verbatim, each record has its own."""
    directories = set()
    for slug in ("punicalagin", "α-punicalagin", "β-punicalagin"):
        main(["--kind", "record", "--slug", slug,
              "--target-root", "data/antibiotics/antibacterial",
              "--summary", "s", "--details", "d",
              "--history-root", str(tmp_path), "--timestamp", "2026-08-05T12:00:00Z"])
        written = next((tmp_path / "records" / slug).glob("*.yaml"))
        doc = yaml.safe_load(written.read_text(encoding="utf-8"))
        assert doc["target"]["slug"] == slug
        assert (REPO_ROOT / doc["target"]["path"]).is_file(), doc["target"]["path"]
        assert history_validation_errors(written) == []
        directories.add(written.parent.name)
    assert directories == {"punicalagin", "α-punicalagin", "β-punicalagin"}


def test_the_session_id_matches_the_existing_convention(tmp_path):
    """`2026-08-03T230903Z-claude-code-90a277` (CellStructureMech) — date hyphens
    kept, colons not."""
    doc, path = _run(tmp_path)
    assert doc["session"]["id"].startswith("2026-08-05T120000Z-claude-code-")
    assert path.name == doc["session"]["id"] + ".yaml"


def test_the_id_is_derived_not_random(tmp_path):
    """Identical arguments must produce an identical id, so a re-run is caught
    by the append-only guard rather than writing a second record."""
    a = session_id("2026-08-05T12:00:00Z", "claude-code", "seed")
    b = session_id("2026-08-05T12:00:00Z", "claude-code", "seed")
    assert a == b
    assert a != session_id("2026-08-05T12:00:00Z", "claude-code", "other")


def test_rewriting_the_same_record_is_refused(tmp_path):
    _run(tmp_path)
    with pytest.raises(SystemExit, match="append-only"):
        main(BASE + ["--history-root", str(tmp_path)])


def test_force_overwrites_a_mis_scaffolded_record(tmp_path):
    _run(tmp_path)
    main(BASE + ["--history-root", str(tmp_path), "--force"])


def test_field_order_matches_the_committed_records(tmp_path):
    """A diff against a claw-written record should be empty, not a reshuffle."""
    _, path = _run(tmp_path, "--issue", "205")
    keys = list(yaml.safe_load(path.read_text()).keys())
    assert keys == ["history_version", "target", "session", "links", "events"]


def test_links_without_issues_or_prs_are_omitted(tmp_path):
    doc, _ = _run(tmp_path)
    assert "links" not in doc


@pytest.mark.parametrize("given,expected", [
    ("205", "https://github.com/CultureBotAI/AntibioticMech/issues/205"),
    ("#205", "https://github.com/CultureBotAI/AntibioticMech/issues/205"),
    # Already a URL: passed through, so a caller following claw's habit of
    # writing the full link is not double-expanded.
    ("https://example.org/x", "https://example.org/x"),
])
def test_bare_issue_numbers_become_uris(given, expected):
    """The schema declares these `range: uri`; claw writes "296" through as-is."""
    assert _link(given, "issues") == expected


def test_bare_history_links_fail_explicit_uri_validation():
    instance = {"links": {"issues": ["423"], "prs": ["#529"]}}

    assert history_link_errors(instance) == [
        "links.issues[0] must be an absolute HTTP(S) URL; got '423'",
        "links.prs[0] must be an absolute HTTP(S) URL; got '#529'",
    ]


def test_history_link_validation_rejects_whitespace_in_urls():
    assert history_link_errors({"links": {"urls": ["https://example.org/not valid"]}}) == [
        "links.urls[0] must be an absolute URI; got "
        "'https://example.org/not valid'"
    ]


def test_general_history_urls_accept_non_http_absolute_uris():
    assert history_link_errors({"links": {"urls": ["doi:10.1000/example"]}}) == []


def test_the_placeholder_is_claw_s_exact_string(tmp_path):
    """Byte-for-byte, not merely TODO-ish.

    The vendored schema carries `pattern: '^(?!TODO: replace this placeholder)'`
    so a plain linkml-validate catches an unfilled record. A near-miss wording
    slips past the negative lookahead and makes an unfilled record permanently
    committable, which is what the first version of this script did
    (CellStructureMech#296).
    """
    main(["--kind", "record", "--slug", "x", "--target-root", "data/antibiotics/antibacterial",
          "--summary", "s", "--history-root", str(tmp_path),
          "--timestamp", "2026-08-05T12:00:00Z"])
    doc = yaml.safe_load(next(tmp_path.rglob("*.yaml")).read_text())
    assert doc["events"][0]["details"] == CLAW_PLACEHOLDER


def test_a_placeholder_record_fails_the_schema_as_the_readme_promises(tmp_path):
    """history/README: "an unfilled record cannot slip through"."""
    main(["--kind", "record", "--slug", "x", "--target-root", "data/antibiotics/antibacterial",
          "--summary", "s", "--history-root", str(tmp_path),
          "--timestamp", "2026-08-05T12:00:00Z"])
    path = next(tmp_path.rglob("*.yaml"))
    assert history_validation_errors(path), (
        "placeholder record validated; the guard is dead"
    )


def test_a_failed_force_rewrite_does_not_destroy_the_original(tmp_path, monkeypatch):
    """Append-only: validate a scratch file, then move. Writing first and
    unlinking on failure loses the record --force was correcting
    (CellStructureMech#296)."""
    import new_history_record as m
    _, path = _run(tmp_path)
    before = path.read_text()
    real = m.build

    def broken(args, ts):
        rec, out = real(args, ts)
        rec["events"][0]["outcome"] = "NOT_AN_OUTCOME"
        return rec, out

    monkeypatch.setattr(m, "build", broken)
    with pytest.raises(SystemExit, match="failed validation"):
        m.main(BASE + ["--history-root", str(tmp_path), "--force"])
    assert path.read_text() == before
    assert list(tmp_path.rglob("*scratch*")) == []


def test_kind_and_summary_are_required_like_claw():
    """Claw requires both. A fallback that does not is not a drop-in."""
    for missing in (["--summary", "s"], ["--kind", "record"]):
        with pytest.raises(SystemExit):
            main(missing)


def test_the_generated_record_validates_against_the_vendored_schema(tmp_path):
    """main() validates before printing; this pins that the schema call is real."""
    _, path = _run(tmp_path, "--issue", "205", "--pr", "298",
                   "--sections", "a, b", "--model", "claude-opus-5")
    assert history_validation_errors(path) == []


def test_the_committed_records_still_validate():
    """The corpus this writes into, selected the way the qc gate selects it."""
    records = gate_records(REPO_ROOT / "history")
    assert records, "no history records found"
    failures = {str(path): history_validation_errors(path) for path in records}
    failures = {path: errors for path, errors in failures.items() if errors}
    assert failures == {}


def test_sections_sits_between_outcome_and_summary(tmp_path):
    """Schema declaration order, and the order claw writes. history/README's
    headline example passes --sections, so getting this wrong put the DOCUMENTED
    invocation on the divergent path (CellStructureMech#296)."""
    _, path = _run(tmp_path, "--sections", "causal_graphs, grounding")
    event = yaml.safe_load(path.read_text())["events"][0]
    assert list(event.keys()) == ["type", "outcome", "sections", "summary", "details"]
    assert event["sections"] == ["causal_graphs", "grounding"]


def test_the_placeholder_path_still_validates_everything_else(tmp_path):
    """Skipping validation wholesale let `--timestamp nonsense` write a record
    and exit 0. A copy with `details` substituted is validated instead."""
    with pytest.raises(SystemExit, match="failed validation"):
        main(["--kind", "record", "--slug", "x",
              "--target-root", "data/antibiotics/antibacterial", "--summary", "s",
              "--history-root", str(tmp_path), "--timestamp", "nonsense"])
    assert list(tmp_path.rglob("*.yaml")) == []


# --- The default actor name. Not in CellStructureMech: it and HabitatMech both
# carry records named claude-code whose agent_tool is codex, written by callers
# who set the tool and model but not the name.

@pytest.mark.parametrize("extra,reason", [
    (["--agent-tool", "codex"], "contradicts the default"),
    (["--model", "gpt-5"], "not a Claude model"),
    (["--agent-tool", "codex", "--model", "gpt-5"], "contradicts the default"),
    (["--actor-type", "human"], "needs an explicit --actor-name"),
    (["--actor-type", "automation"], "needs an explicit --actor-name"),
    (["--actor-name", "", "--agent-tool", "codex"], "contradicts the default"),
])
def test_a_default_actor_name_that_contradicts_the_session_is_refused(tmp_path, extra, reason):
    with pytest.raises(SystemExit, match=reason):
        main(BASE + ["--history-root", str(tmp_path), *extra])
    assert list(tmp_path.rglob("*.yaml")) == []


def test_an_explicit_actor_name_is_written_into_the_record_and_its_filename(tmp_path):
    doc, path = _run(tmp_path, "--actor-name", "codex", "--agent-tool", "codex",
                     "--model", "gpt-5")
    assert doc["session"]["actors"] == [{"type": "ai_agent", "name": "codex",
                                         "model": "gpt-5", "agent_tool": "codex"}]
    assert "-codex-" in path.name and "claude-code" not in path.name


def test_the_default_actor_name_still_applies_to_a_claude_code_session(tmp_path):
    doc, path = _run(tmp_path, "--model", "claude-opus-5-5", "--agent-tool", "claude-code")
    assert doc["session"]["actors"] == [{"type": "ai_agent", "name": "claude-code",
                                         "model": "claude-opus-5-5",
                                         "agent_tool": "claude-code"}]
    assert "-claude-code-" in path.name


# --- The qc gate (scripts/validate_history.py), which the tests above do not run.

def test_the_gate_selects_yml_records_too(tmp_path):
    """The scaffolder writes .yaml; a hand-saved .yml must not escape validation.
    README.md and other non-YAML files are not records."""
    for name in ("a.yaml", "b.yml", "README.md"):
        (tmp_path / "records" / "x").mkdir(parents=True, exist_ok=True)
        (tmp_path / "records" / "x" / name).write_text("{}\n")
    expected = [tmp_path / "records" / "x" / "a.yaml", tmp_path / "records" / "x" / "b.yml"]
    assert gate_records(tmp_path) == expected
    assert link_gate_records([tmp_path]) == expected


@pytest.mark.parametrize("text,holds_a_record", [
    ("", False),
    ("[]\n", False),
    ("- history_version: 1\n", False),
    ("just a string\n", False),
    ("history_version: [unclosed\n", False),
    ("history_version: 1\n", True),  # a mapping; the schema judges the rest
])
def test_a_file_that_cannot_hold_a_record_is_named(tmp_path, text, holds_a_record):
    path = tmp_path / "r.yaml"
    path.write_text(text)
    assert (not_a_record(path) is None) is holds_a_record


def test_the_gate_fails_on_an_empty_record_file(tmp_path):
    """linkml-validate alone prints "No issues found" and exits 0 for it."""
    (tmp_path / "records" / "x").mkdir(parents=True)
    (tmp_path / "records" / "x" / "2026-08-05T120000Z-claude-code-000000.yaml").write_text("")
    result = subprocess.run([sys.executable, "scripts/validate_history.py", str(tmp_path)],
                            cwd=REPO_ROOT, capture_output=True, text=True)
    assert result.returncode == 1, result.stdout + result.stderr
    assert "top level must be one record" in result.stderr


def test_the_gate_fails_on_an_unfilled_record_and_passes_a_filled_one(tmp_path):
    """End to end through linkml-validate, as qc runs it: the exit code is the
    gate, and the placeholder pattern lives in the vendored schema."""
    main(["--kind", "record", "--slug", "erythromycin-a",
          "--target-root", "data/antibiotics/antibacterial", "--summary", "s",
          "--history-root", str(tmp_path), "--timestamp", "2026-08-05T12:00:00Z"])

    def gate():
        return subprocess.run([sys.executable, "scripts/validate_history.py", str(tmp_path)],
                              cwd=REPO_ROOT, capture_output=True, text=True)

    unfilled = gate()
    assert unfilled.returncode != 0, unfilled.stdout + unfilled.stderr
    # Failing for the right reason, not because the validator could not run.
    assert "TODO: replace this placeholder" in unfilled.stdout + unfilled.stderr

    record = next(tmp_path.rglob("*.yaml"))
    doc = yaml.safe_load(record.read_text())
    doc["events"][0]["details"] = "Filled in."
    record.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))
    filled = gate()
    assert filled.returncode == 0, filled.stdout + filled.stderr

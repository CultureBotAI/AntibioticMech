from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import research_antibiotic as research  # noqa: E402


def _sample() -> Path:
    return sorted(research.ANTIBIOTICS_DIR.rglob("*.yaml"))[0]


def test_resolve_record_by_slug_identifier_and_inchikey():
    sample = _sample()
    record = research.load_record(sample)
    assert research.resolve_record(sample.stem) == sample
    assert research.resolve_record(record["identifier"]) == sample
    assert research.resolve_record(record["chemical_structure"]["standard_inchi_key"]) == sample


def test_openscientist_command_uses_real_client_provider():
    sample = _sample()
    variables = research.template_vars(research.load_record(sample), sample)
    command = research.build_client_command(
        provider="openscientist",
        template=research.TEMPLATE,
        output=Path("research/out.md"),
        variables=variables,
        passthrough=[],
        client_command="deep-research-client",
    )
    assert command[:2] == ["deep-research-client", "research"]
    assert command[command.index("--provider") + 1] == "openscientist"
    assert "--output" in command


def test_codex_dry_run_uses_native_contract(capsys):
    sample = _sample()
    assert research.main(["--provider", "codex", "--target", sample.stem]) == 0
    output = capsys.readouterr().out
    assert "codex --search --ask-for-approval never exec" in output
    assert "schema validated" in output

"""Regression checks for the primary-source-reviewed AST chemical identities."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evaluate_ncbi_ast import (  # noqa: E402
    corpus_name_candidates,
    exact_activity_rows,
    read_drug_map,
)

VERSION = "ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184"
MAP = ROOT / "curation/ncbi_ast_drug_map.tsv"
IDENTITIES = [
    ("cefalotin", "CHEBI:124991", "XIURVHNZVLADCM-IUODEOHRSA-N"),
    ("cefotaxime", "CHEBI:204928", "GPRBEKHLDVQUJE-QSWIMTSFSA-N"),
    ("cefovecin", "antibioticmech:aro-c73757ed91", "ZJGQFXVQDVCVOK-QFKLAVHZSA-N"),
    ("cefpodoxime", "CHEBI:3504", "WYUSVOMTXWRGEK-HBWVYFAYSA-N"),
    ("cephalothin", "CHEBI:124991", "XIURVHNZVLADCM-IUODEOHRSA-N"),
    ("enrofloxacin", "CHEBI:35720", "SPFYMRJSYKOXGV-UHFFFAOYSA-N"),
    ("marbofloxacin", "CHEBI:132230", "LPVVTHNMXSEIFM-UHFFFAOYSA-N"),
    ("oxacillin", "CHEBI:7809", "UWYHMGVUTGAWSP-JKIFEVAISA-N"),
    ("telithromycin", "CHEBI:29688", "LJVAJPDWBABPEJ-PNUFFHFMSA-N"),
]


@pytest.fixture(scope="module")
def identities():
    candidates, keys = corpus_name_candidates()
    return candidates, keys, read_drug_map(MAP, keys, VERSION)


@pytest.mark.parametrize("name,identifier,key", IDENTITIES)
def test_reviewed_mapping_pins_full_identity(identities, name, identifier, key):
    _, _, mappings = identities
    row = mappings[name]
    assert row["mapping_status"] == "EXACT"
    assert (row["identifier"], row["standard_inchi_key"]) == (identifier, key)
    assert row["mapping_basis"] == "curated_active_moiety"
    assert "https://" in row["notes"]
    assert "research/2026-10-03-ncbi-ast-drug-coverage.md" in row["notes"]


def test_ceftiofur_name_match_does_not_admit_the_sodium_salt(identities):
    candidates, keys, mappings = identities
    assert "CHEBI:31383" in candidates["ceftiofur"]
    assert keys["CHEBI:31383"] == "RFLHUYUQCKHUKS-JUODUXDSSA-M"
    row = mappings["ceftiofur"]
    assert row["mapping_status"] == "MISSING_CORPUS_RECORD"
    assert not row["identifier"] and not row["standard_inchi_key"]


def test_exact_map_does_not_admit_prodrug_salt_or_combination(identities):
    _, _, mappings = identities
    names = [name for name, _, _ in IDENTITIES] + [
        "ceftiofur", "cefpodoxime-proxetil", "cefotaxime-clavulanic acid",
        "cephalothin sodium",
    ]
    rows = [
        {"antibiotic": name, "biosample_acc": f"SAMN{10000 + index}",
         "bioproject_acc": "PRJNA12345", "taxgroup_name": "Escherichia coli",
         "phenotype": "R", "mic": "4", "method": "broth microdilution"}
        for index, name in enumerate(names)
    ]
    report = exact_activity_rows(
        rows, mappings, source_version=VERSION, source_retrieved_on="2026-10-03",
    )
    assert {row["source_name"] for row in report} == {name for name, _, _ in IDENTITIES}
    assert len(report) == len(IDENTITIES)
    assert len({row["activity_group_id"] for row in report}) == len(IDENTITIES)
    assert all(row["mic_value"] == "4" and row["mic_units"] == "mg/L" for row in report)


def test_changed_cefovecin_stereochemistry_fails_closed(identities):
    _, keys, _ = identities
    changed = {**keys, "antibioticmech:aro-c73757ed91": "ZJGQFXVQDVCVOK-LTRDADOWSA-N"}
    with pytest.raises(ValueError, match="does not match"):
        read_drug_map(MAP, changed, VERSION)

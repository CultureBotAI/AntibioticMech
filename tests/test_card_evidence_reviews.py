"""Evidence qualifications preserve CARD ownership and exact source/compound scope."""

import copy
import csv
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import card_evidence_reviews as review  # noqa: E402
import seed_from_sources as seed  # noqa: E402
from audit_curator_resistance_fields import owner  # noqa: E402

INVENTORY = ROOT / "data/raw/aro_resistance_edges.tsv"
SLUGS = ("pleuromutilin", "colistin-a", "colistin-b", "daptomycin")
SALMONELLA = json.loads((ROOT / "research/2026-10-16-salmonella-evidence-scope.json").read_bytes())


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def inputs(tmp_path):
    inventory = tmp_path / "inventory.tsv"
    inventory.write_bytes(INVENTORY.read_bytes())
    path = tmp_path / "reviews.json"
    path.write_bytes(review.DEFAULT_REVIEW.read_bytes())
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    paths = {ROOT / f"data/antibiotics/antibacterial/{s}.yaml" for s in SLUGS}
    paths.update(ROOT / r["path"] for r in SALMONELLA["records"])
    documents = [load_record(path) for path in sorted(paths)]
    return inventory, rows, {r["identifier"]: r for r in documents}, path


def test_projection_changes_only_seventeen_notes_and_preserves_source_ownership(inputs):
    inventory, rows, records, path = inputs
    decisions = review.load_reviews(*inputs)
    assert len(decisions) == 17
    before = copy.deepcopy(records)
    unqualified = copy.deepcopy(records)
    seed.attach_aro_mechanism(unqualified, "2026-10-15", evidence_review=None)
    seed.attach_aro_mechanism(records, "2026-10-15", evidence_review=path)
    changed = []
    for rid, record in records.items():
        for item, old in zip(
            record["resistance_mechanisms"], unqualified[rid]["resistance_mechanisms"], strict=True
        ):
            assert seed.is_card_sourced(item) and owner(item) == "CARD"
            if item != old:
                changed.append((rid, item["aro_id"]))
                assert {k: v for k, v in item.items() if k != "note"} == old
                assert "Qualification references, not an upgrade" in item["note"]
        assert record.get("molecular_targets") == unqualified[rid].get("molecular_targets")
        assert {
            k: v
            for k, v in record.items()
            if k
            not in {
                "resistance_mechanisms",
                "molecular_targets",
            }
        } == {
            k: v
            for k, v in before[rid].items()
            if k
            not in {
                "resistance_mechanisms",
                "molecular_targets",
            }
        }
    assert set(changed) == {
        ("CHEBI:8269", "ARO:3003761"),
        ("CHEBI:59064", "ARO:3004695"),
        ("CHEBI:59673", "ARO:3004695"),
        ("CHEBI:600103", "ARO:3004097"),
    } | {(r["identifier"], "ARO:3003317") for r in SALMONELLA["records"]}
    once = copy.deepcopy(records)
    seed.attach_aro_mechanism(records, "2026-10-15", evidence_review=path)
    assert records == once


@pytest.mark.parametrize(
    "change",
    [
        "unknown_top",
        "bool_version",
        "inventory",
        "rows",
        "unknown_review",
        "empty_note",
        "bad_date",
        "duplicate_id",
        "no_evidence",
        "bad_reference",
        "bad_url",
        "empty_location",
        "unknown_evidence",
        "duplicate_reference",
        "no_targets",
        "unknown_target",
        "row_pin",
        "duplicate_row",
        "record_id",
        "missing_record",
        "chemical",
        "source_concept",
        "ambiguous_source",
        "add_protein",
        "add_taxon",
        "add_allele",
        "add_phenotype",
    ],
)
def test_invalid_or_scope_expanding_reviews_fail_closed(inputs, change):
    inventory, rows, records, path = inputs
    document = json.loads(path.read_bytes())
    first = document["reviews"][0]
    evidence = first["evidence"][0]
    target = first["source_rows"][0]
    if change == "unknown_top":
        document["extra"] = True
    elif change == "bool_version":
        document["schema_version"] = True
    elif change == "inventory":
        inventory.write_bytes(inventory.read_bytes() + b"\n")
    elif change == "rows":
        rows.pop()
    elif change == "unknown_review":
        first["extra"] = True
    elif change == "empty_note":
        first["note"] = " "
    elif change == "bad_date":
        first["reviewed_on"] = "2026-02-30"
    elif change == "duplicate_id":
        document["reviews"][1]["review_id"] = first["review_id"]
    elif change == "no_evidence":
        first["evidence"] = []
    elif change == "bad_reference":
        evidence["reference"] = "PMID:0"
    elif change == "bad_url":
        evidence["source_url"] = "http://example.org"
    elif change == "empty_location":
        evidence["locations"] = []
    elif change == "unknown_evidence":
        evidence["extra"] = "unsupported"
    elif change == "duplicate_reference":
        first["evidence"].append(copy.deepcopy(evidence))
    elif change == "no_targets":
        first["source_rows"] = []
    elif change == "unknown_target":
        target["extra"] = True
    elif change == "row_pin":
        target["row_sha256"] = "0" * 64
    elif change == "duplicate_row":
        first["source_rows"].append(copy.deepcopy(target))
    elif change == "record_id":
        target["identifier"] = "CHEBI:59064"
    elif change == "missing_record":
        del records[target["identifier"]]
    elif change == "chemical":
        records[target["identifier"]]["chemical_structure"]["standard_inchi_key"] = "changed"
    elif change == "source_concept":
        records[target["identifier"]]["source_concepts"] = []
    elif change == "ambiguous_source":
        records["CHEBI:59064"]["source_concepts"] += copy.deepcopy(
            records[target["identifier"]]["source_concepts"]
        )
    else:
        first[change.removeprefix("add_")] = "unsupported experimental assignment"
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError):
        review.load_reviews(inventory, rows, records, path)


@pytest.mark.parametrize("change", ["note", "mechanism", "label", "aro", "evidence"])
def test_review_refuses_to_modify_an_edited_claim(inputs, change):
    inventory, rows, records, path = inputs
    decisions = review.load_reviews(*inputs)
    seed.attach_aro_mechanism(records, "2026-10-15", evidence_review=None)
    row = next(r for r in rows if r["determinant_id"] == "ARO:3003761")
    item = next(
        r for r in records["CHEBI:8269"]["resistance_mechanisms"] if r["aro_id"] == row["determinant_id"]
    )
    if change == "evidence":
        item["evidence"].append({"reference": "PMID:123"})
    else:
        item[{"note": "note", "mechanism": "mechanism_type", "label": "label", "aro": "aro_id"}[change]] = (
            "changed"
        )
    before = copy.deepcopy(item)
    with pytest.raises(ValueError):
        review.apply_review(item, row, decisions)
    assert item == before


def test_unreviewed_claim_and_explicit_fixture_opt_out_are_unchanged(inputs):
    inventory, rows, records, path = inputs
    assert review.load_reviews(inventory, rows, records, None) == {}
    decisions = review.load_reviews(*inputs)
    row = next(r for r in rows if review.row_digest(r) not in decisions)
    item = {"unrelated": "curator value"}
    assert review.apply_review(item, row, decisions) is False
    assert item == {"unrelated": "curator value"}


def test_qualifications_retain_both_conflicting_results_and_exact_compound_limits():
    document = json.loads(review.DEFAULT_REVIEW.read_bytes())
    eatav, mcr, cdsa, pare = document["reviews"]
    assert "tiamulin" in eatav["note"] and "not the parent" in eatav["note"]
    assert "contrasting" in mcr["note"] and "not universal" in mcr["note"]
    assert "purified colistin A or B separately" in mcr["note"]
    assert {e["reference"] for e in mcr["evidence"]} == {
        "DOI:10.1128/JCM.01562-17",
        "DOI:10.1128/AAC.00649-18",
        "DOI:10.1093/jac/dkz413",
    }
    assert "retains S. mitis/oralis" in cdsa["note"]
    assert "not a verified experimental species assignment" in cdsa["note"]
    assert "no replacement taxon, protein, allele or genome is assigned" in cdsa["note"]
    assert cdsa["evidence"][0]["locations"] == ["Addendum in proof"]
    draft = json.loads(
        (ROOT / "research/2026-10-15-cdsa-cyp51-context-proposed-review.json").read_bytes()
    )
    assert cdsa == draft["reviews"][0]
    pare_draft = json.loads(
        (ROOT / "research/2026-10-16-salmonella-evidence-scope-proposed-review.json").read_bytes()
    )
    assert pare == pare_draft["reviews"][0]
    assert len(pare["source_rows"]) == 13
    assert "indirect contribution remained unresolved" in pare["note"]
    assert "not a universal inactivity claim" in pare["note"]
    unassigned = "without assigning an experimental protein, allele, taxon or susceptibility observation"
    assert unassigned in pare["note"]


@pytest.mark.parametrize("key", ["schema_version", "note", "source_url", "row_sha256"])
def test_duplicate_json_members_are_rejected_at_every_level(inputs, key):
    inventory, rows, records, path = inputs
    # The valid member comes last, so ordinary json.loads would hide the duplicate.
    original = path.read_text()
    member = json.dumps(key) + ":"
    path.write_text(original.replace(member, member + " null, " + member, 1))
    with pytest.raises(ValueError, match="duplicate.*JSON key"):
        review.load_reviews(inventory, rows, records, path)


@pytest.mark.parametrize(
    "url",
    [
        "https://",
        "https:///article",
        "https://?article=1",
        "https://example.org bad/article",
        "https://example.org/has space",
        "https://user:secret@example.org/article",
        "https://example.org:bad/article",
        "https://example.org:70000/article",
        "https://example.org:/article",
        "https://example..org/article",
        "https://-example.org/article",
        "https://example.org\\other/article",
        "https://[broken/article",
    ],
)
def test_malformed_primary_source_urls_fail_closed(inputs, url):
    inventory, rows, records, path = inputs
    document = json.loads(path.read_bytes())
    document["reviews"][0]["evidence"][0]["source_url"] = url
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="invalid CARD review evidence"):
        review.load_reviews(inventory, rows, records, path)


@pytest.mark.parametrize(
    "url",
    [
        "https://doi.org/10.1128/AAC.01030-13",
        "https://journals.example.org:443/article?id=1&view=full#results",
    ],
)
def test_valid_primary_source_urls_need_no_network(inputs, url):
    inventory, rows, records, path = inputs
    document = json.loads(path.read_bytes())
    document["reviews"][0]["evidence"][0]["source_url"] = url
    path.write_text(json.dumps(document))
    assert len(review.load_reviews(inventory, rows, records, path)) == 17

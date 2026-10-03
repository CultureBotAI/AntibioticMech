"""Container compression must not change source evidence or invalidate reviews."""

import copy
import gzip
import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import evaluate_ncbi_ast as evaluator  # noqa: E402
import ncbi_ast_biosamples as biosamples  # noqa: E402
import ncbi_ast_inventory as inventory  # noqa: E402
import ncbi_ast_taxonomy as taxonomy  # noqa: E402
import review_ncbi_ast_activity as assay_cli  # noqa: E402
import seed_from_sources as seed  # noqa: E402
from test_ncbi_ast_assays import review_data, write_review  # noqa: E402
from test_ncbi_ast_biosamples import convert, pair, review_file, sample  # noqa: E402
from test_ncbi_ast_import import ncbi_ast_row, write_activity_report  # noqa: E402
from test_ncbi_ast_taxonomy import fake_snapshot, records, row  # noqa: E402


def compressed(path, *, mtime=0):
    target = path.with_suffix(path.suffix + ".gz")
    target.write_bytes(gzip.compress(path.read_bytes(), mtime=mtime))
    return target


def test_gzip_matches_plain_loader_and_exact_content_hash(tmp_path):
    path = tmp_path / "activity.tsv"
    rows = [ncbi_ast_row(strain='strain "quoted"')]
    write_activity_report(path, rows)  # CRLF is preserved, not normalized before hashing.
    zipped = compressed(path)
    expected = hashlib.sha256(path.read_bytes()).hexdigest()
    assert inventory.activity_report_sha256(path) == expected
    assert inventory.activity_report_sha256(zipped) == expected
    assert seed.load_ncbi_ast_activity_inventory(path) == rows
    assert seed.load_ncbi_ast_activity_inventory(zipped) == rows
    assert evaluator.read_activity_report(
        zipped, {rows[0]["identifier"]: rows[0]["standard_inchi_key"]}, rows[0]["source_version"]
    ) == rows
    metadata = inventory.inventory_metadata(zipped)
    assert metadata == {
        "encoding": "gzip", "sha256": hashlib.sha256(zipped.read_bytes()).hexdigest(),
        "bytes": zipped.stat().st_size, "content_sha256": expected,
        "content_bytes": path.stat().st_size,
    }
    assert metadata["sha256"] != expected


def test_evaluator_writes_deterministic_gzip_with_identical_expanded_bytes(tmp_path):
    rows = [ncbi_ast_row()]
    paths = [tmp_path / name for name in ("plain.tsv", "first.tsv.gz", "second.tsv.gz")]
    for path in paths:
        evaluator.write_activity_report(rows, path)
        assert seed.load_ncbi_ast_activity_inventory(path) == rows
    assert paths[1].read_bytes() == paths[2].read_bytes()
    assert gzip.decompress(paths[1].read_bytes()) == paths[0].read_bytes()


@pytest.mark.parametrize("suffix", [".tsv", ".tsv.gz"])
def test_expanded_limit_includes_all_gzip_members(tmp_path, monkeypatch, suffix):
    path = tmp_path / ("activity" + suffix)
    content = b"0123456789"
    payload = gzip.compress(content[:5]) + gzip.compress(content[5:]) if suffix.endswith("gz") else content
    path.write_bytes(payload)
    monkeypatch.setattr(inventory, "MAX_CONTENT_BYTES", 10)
    assert inventory.activity_report_sha256(path) == hashlib.sha256(content).hexdigest()
    monkeypatch.setattr(inventory, "MAX_CONTENT_BYTES", 9)
    with pytest.raises(ValueError, match="expanded-byte limit"):
        inventory.activity_report_sha256(path)
    with pytest.raises(ValueError, match="expanded-byte limit"), inventory.open_activity_text(path) as handle:
        handle.read()


@pytest.mark.parametrize("corruption", ["truncated", "crc", "trailing", "plain"])
def test_corrupt_gzip_fails_closed_in_loader_and_fingerprint(tmp_path, corruption):
    path = tmp_path / "activity.tsv"
    write_activity_report(path, [ncbi_ast_row()])
    zipped = compressed(path)
    payload = zipped.read_bytes()
    if corruption == "truncated":
        payload = payload[:-4]
    elif corruption == "crc":
        payload = payload[:-8] + bytes([payload[-8] ^ 1]) + payload[-7:]
    elif corruption == "trailing":
        payload += b"trailing junk"
    else:
        payload = path.read_bytes()
    zipped.write_bytes(payload)
    for read in (inventory.activity_report_sha256, seed.load_ncbi_ast_activity_inventory):
        with pytest.raises((OSError, EOFError)):
            read(zipped)


@pytest.mark.parametrize("payload", [b"bad\theader\n", b"\xff\n"])
def test_compression_does_not_bypass_header_or_utf8_checks(tmp_path, payload):
    path = tmp_path / "activity.tsv.gz"
    path.write_bytes(gzip.compress(payload))
    with pytest.raises((ValueError, UnicodeError)):
        seed.load_ncbi_ast_activity_inventory(path)


def test_biosample_review_and_paired_observations_survive_recompression(tmp_path):
    rows = pair()
    plain, review = review_file(tmp_path, rows, sample([rows[0]]))
    expected = list(biosamples.activity_observations(rows, plain, convert, review))
    for mtime in (0, 123):
        zipped = compressed(plain, mtime=mtime)
        loaded = seed.load_ncbi_ast_activity_inventory(zipped)
        assert list(biosamples.activity_observations(loaded, zipped, convert, review)) == expected
    data = json.loads(review.read_text())
    data["activity_report_sha256"] = inventory.inventory_metadata(zipped)["sha256"]
    review.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="exact activity report"):
        list(biosamples.activity_observations(rows, zipped, convert, review))


def test_taxonomy_review_checks_logical_bytes_not_container(tmp_path, monkeypatch):
    plain, directory = fake_snapshot(tmp_path, monkeypatch)
    zipped = compressed(plain)
    assert taxonomy.load_snapshot(directory, zipped, [row()]) == records()
    zipped.write_bytes(gzip.compress(b"changed report"))
    with pytest.raises(ValueError, match="checksum mismatch"):
        taxonomy.load_snapshot(directory, zipped, [row()])


def test_assay_review_cli_preserves_candidate_pin_for_gzip(tmp_path, monkeypatch):
    data = review_data()
    candidate = ncbi_ast_row(
        source_version=data["source_version"], method="", platform="Vitek", vendor="", reagent=""
    )
    plain = tmp_path / "candidate.tsv"
    evaluator.write_activity_report([candidate], plain)
    zipped = compressed(plain)
    data["candidate_sha256"] = inventory.activity_report_sha256(plain)
    review = write_review(tmp_path, data)
    monkeypatch.setattr(assay_cli, "corpus_name_candidates", lambda: (
        {}, {candidate["identifier"]: candidate["standard_inchi_key"]},
    ))
    output = tmp_path / "accepted"
    monkeypatch.setattr(sys, "argv", [
        "review", "--activity-report", str(zipped), "--assay-review", str(review),
        "--output-directory", str(output),
    ])
    assay_cli.main()
    assert (output / "activity.tsv").read_bytes() == plain.read_bytes()
    summary = json.loads((output / "review.json").read_text())
    assert summary["candidate_sha256"] == data["candidate_sha256"]
    assert summary["candidate_inventory"] == inventory.inventory_metadata(zipped)
    assert summary["accepted_groups"] == 1
    data["candidate_sha256"] = summary["candidate_inventory"]["sha256"]
    write_review(tmp_path, data)
    monkeypatch.setattr(sys, "argv", [
        "review", "--activity-report", str(zipped), "--assay-review", str(review),
        "--output-directory", str(tmp_path / "invalid"),
    ])
    with pytest.raises(SystemExit):
        assay_cli.main()
    assert not (tmp_path / "invalid").exists()


def test_default_seeder_loads_gzip_and_rejects_dual_inventories_before_mutation(tmp_path, monkeypatch):
    rows = pair()[:1]
    plain = tmp_path / "activity.tsv"
    write_activity_report(plain, rows)
    zipped = compressed(plain)
    monkeypatch.setattr(seed, "NCBI_AST_ACTIVITY_INVENTORY", plain)
    monkeypatch.setattr(seed, "read_assay_review", lambda _: None)
    identifier = rows[0]["identifier"]
    target = {identifier: {
        "identifier": identifier, "curation_history": [],
        "chemical_structure": {"standard_inchi_key": rows[0]["standard_inchi_key"]},
    }}
    original = copy.deepcopy(target)
    with pytest.raises(ValueError, match="ambiguous"):
        seed.attach_ncbi_ast_activity(target)
    assert target == original
    plain.unlink()
    assert inventory.resolve_inventory(plain) == zipped
    assert seed.attach_ncbi_ast_activity(target)["matched_observations"] == 1
    assert target[identifier]["activity_spectrum"] == [convert(rows[0])]
    zipped.unlink()
    assert seed.attach_ncbi_ast_activity({}) == {"missing_inventory": 1}
    with pytest.raises(ValueError, match="explicit NCBI AST inventory"):
        seed.attach_ncbi_ast_activity({}, inventory=zipped)
    zipped.symlink_to("missing")
    with pytest.raises(ValueError, match="not a file"):
        inventory.resolve_inventory(plain)


def test_packer_preserves_bytes_and_is_deterministic_without_overwrite(tmp_path, monkeypatch):
    monkeypatch.setattr(inventory, "ROOT", tmp_path)
    path = tmp_path / "input.tsv"
    write_activity_report(path, [ncbi_ast_row()])
    outputs = [tmp_path / "reports" / name for name in ("first", "second")]
    results = [inventory.pack_inventory(path, output) for output in outputs]
    assert results[0] == results[1]
    assert results[0]["source_groups"] == 1
    for output in outputs:
        assert gzip.decompress((output / "activity.tsv.gz").read_bytes()) == path.read_bytes()
        assert json.loads((output / "inventory.json").read_text()) == results[0]
    assert (outputs[0] / "activity.tsv.gz").read_bytes() == (outputs[1] / "activity.tsv.gz").read_bytes()
    with pytest.raises(ValueError, match="refusing to overwrite"):
        inventory.pack_inventory(path, outputs[0])
    with pytest.raises(ValueError, match="under reports"):
        inventory.pack_inventory(path, tmp_path / "data/raw")


def test_packer_does_not_publish_invalid_input(tmp_path, monkeypatch):
    monkeypatch.setattr(inventory, "ROOT", tmp_path)
    path = tmp_path / "input.tsv"
    path.write_text("bad header\n")
    output = tmp_path / "reports" / "invalid"
    with pytest.raises(ValueError, match="header"):
        inventory.pack_inventory(path, output)
    assert not output.exists()

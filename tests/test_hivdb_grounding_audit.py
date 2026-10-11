"""Algorithm reference context is not an isolate or measured resistance result."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_hivdb_grounding as audit  # noqa: E402


def cache(name, url, payload, **extra):
    body = json.dumps(payload)
    item = {"url": url, "status": 200, "body": body,
            "sha256": audit.common.digest(body.encode()), **extra}
    audit.common.write(name, item)
    return item


@pytest.fixture
def snapshot(tmp_path, monkeypatch):
    monkeypatch.setattr(audit.common, "OUT", tmp_path)
    (tmp_path / "data/raw").mkdir(parents=True)
    genes = [{"name": "HIV1RT", "abstractGene": "RT", "strain": "HIV1", "refSequence": "TEST"}]
    strains = [{"name": "HIV1", "displayText": "HIV-1"}]
    tree = []
    for path, payload in zip(audit.SOURCE_FILES, (genes, strains), strict=True):
        body = json.dumps(payload).encode()
        blob = hashlib.sha1(b"blob " + str(len(body)).encode() + b"\0" + body).hexdigest()
        tree.append({"path": path, "sha": blob})
        cache(f"hivfacts-{Path(path).stem}-response.json",
              f"https://raw.githubusercontent.com/hivdb/hivfacts/{audit.COMMIT}/{path}",
              payload, git_blob_sha1=blob)
    cache("hivfacts-tree-response.json",
          f"https://api.github.com/repos/hivdb/hivfacts/git/trees/{audit.COMMIT}?recursive=1",
          {"truncated": False, "tree": tree})
    row = {
        "source_version": audit.COMMIT, "algorithm_name": "HIVDB", "algorithm_version": "10.2",
        "algorithm_date": "2026-04-26", "source_record_id": "TEST", "score_term_index": "1",
        "score_term": "1A => 5", "gene": "RT", "drug_class": "NRTI", "identifier": "CHEBI:1",
        "standard_inchi_key": "TEST-KEY", "score_assignments": "1", "negative_score_assignments": "0",
        "min_score": "5.0", "max_score": "5.0", "mapping_status": "EXACT",
    }
    row["source_rule_id"] = audit.hivdb_score_rule_id(row)
    with (tmp_path / audit.INVENTORY).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    source_bytes = (tmp_path / audit.INVENTORY).read_bytes()
    manifest = {
        "inventories": {Path(audit.INVENTORY).name: {
            "sha256": audit.common.digest(source_bytes), "bytes": len(source_bytes), "rows": 1,
        }},
        "sources": {"stanford-hivdb": {"version": audit.COMMIT, "algorithm": "HIVDB 10.2"}},
    }
    (tmp_path / audit.MANIFEST).write_text(yaml.safe_dump(manifest))
    claim = dict(row, pathogen_label="Human immunodeficiency virus 1", source="HIVDB_HIVFACTS")
    record = {"identifier": "CHEBI:1", "label": "test", "path": "test.yaml", "sha256": "hash",
              "standard_inchi_key": "TEST-KEY", "score_rules": [claim]}
    records = [record]
    monkeypatch.setattr(audit.card, "current_corpus", lambda _: records)
    audit.common.write("corpus.json", {"records": records})
    taxon = {"taxonId": 11676, "scientificName": "Human immunodeficiency virus type 1",
             "commonName": "HIV-1", "otherNames": ["Human immunodeficiency virus 1"],
             "rank": "no rank", "active": True, "parent": {"taxonId": 3418650}}
    tax_response = {"status": 200, "body": json.dumps(taxon), "sha256": "taxonomy"}
    monkeypatch.setattr(audit.common, "fetch", lambda path: tax_response)
    return tmp_path, records, tax_response


def test_reference_context_keeps_all_rules_without_exporting_sequences(snapshot):
    root, _, _ = snapshot
    audit.analyze(root)
    result = json.loads((root / "hivdb-reference-grounding.json").read_text())
    assert result["summary"] == {"records": 1, "score_rules": 1, "region_rule_counts": {"RT": 1}}
    assert result["reference_regions"]["RT"]["reference_length"] == 4
    assert "refSequence" not in json.dumps(result)
    assert result["records"][0]["pathogen_taxon_rank"] == "no rank"
    assert "protein_accession" not in result["records"][0]
    assert result["records"][0]["primary_review_status"] == "PENDING"


@pytest.mark.parametrize("change", [
    "missing", "duplicate", "formula", "gene", "compound", "organism", "owner",
])
def test_source_context_cannot_hide_rule_or_identity_drift(snapshot, change):
    root, records, _ = snapshot
    claim = records[0]["score_rules"][0]
    if change == "missing":
        records[0]["score_rules"] = []
    elif change == "duplicate":
        records[0]["score_rules"].append(copy.deepcopy(claim))
    elif change == "formula":
        claim["score_term"] = "1A => 10"
    elif change == "gene":
        claim["gene"] = "IN"
    elif change == "compound":
        records[0]["standard_inchi_key"] = "OTHER-KEY"
    elif change == "organism":
        claim["pathogen_label"] = "Human immunodeficiency virus 2"
    else:
        claim["source"] = "OTHER"
    with pytest.raises(ValueError):
        audit.analyze(root)


def test_inactive_taxon_is_not_assigned(snapshot):
    root, _, response = snapshot
    taxon = json.loads(response["body"])
    taxon["active"] = False
    response["body"] = json.dumps(taxon)
    with pytest.raises(ValueError, match="taxon does not match"):
        audit.analyze(root)


@pytest.mark.parametrize("field", ["sha256", "bytes", "rows", "version", "algorithm"])
def test_adopted_manifest_pin_must_match(snapshot, field):
    root, _, _ = snapshot
    path = root / audit.MANIFEST
    manifest = yaml.safe_load(path.read_text())
    if field in {"version", "algorithm"}:
        manifest["sources"]["stanford-hivdb"][field] = "changed"
    else:
        manifest["inventories"][Path(audit.INVENTORY).name][field] = "changed"
    path.write_text(yaml.safe_dump(manifest))
    with pytest.raises(ValueError, match="manifest pin"):
        audit.analyze(root)


@pytest.mark.parametrize("change", ["checksum", "git_blob", "truncated"])
def test_reference_cache_is_checked_against_pinned_source(snapshot, change):
    root, _, _ = snapshot
    path = root / ("hivfacts-tree-response.json" if change == "truncated" else
                   "hivfacts-genes_hiv1-response.json")
    response = json.loads(path.read_text())
    if change == "checksum":
        response["sha256"] = "bad"
    elif change == "git_blob":
        response["git_blob_sha1"] = "bad"
    else:
        body = json.loads(response["body"])
        body["truncated"] = True
        response["body"] = json.dumps(body)
        response["sha256"] = audit.common.digest(response["body"].encode())
    audit.common.write(path.name, response)
    with pytest.raises(ValueError):
        audit.source_context()

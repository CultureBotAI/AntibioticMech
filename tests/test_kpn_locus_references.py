"""Reference locus matches must not become strain-specific resistance claims."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_kpn_locus_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize(
    "key",
    [
        "individual_locus_to_kpnE_or_kpnF_assignment",
        "reference_genome_version_reported_in_selected_text",
        "reference_genome_independently_verified",
        "reference_genome_is_experimental_derivative",
        "loss_of_function_sensitivity_is_new_resistant_allele",
        "numerical_ast_review_completed",
        "exact_assay_compound_mapping_completed",
        "figures_and_supplements_visually_reviewed",
        "whole_paper_signoff",
        "sequence_variant_primer_coordinate_construct_protocol_exports",
        "ncbi_links_followed",
        "manual_reading_independently_reproduced_by_code",
    ],
)
def test_primary_assessment_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


def native_fixture():
    entry = {
        "primaryAccession": "A0ACD7U1E6",
        "entryType": "unreviewed",
        "entryAudit": {"entryVersion": 2, "sequenceVersion": 1},
        "organism": {"taxonId": 484021, "scientificName": audit.REFERENCE_NAME},
        "genes": [{"geneName": {"value": "ydgF"}, "orfNames": [{"value": "KP1_2583"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "MdtJ"}}},
        "references": [
            {
                "referenceNumber": 1,
                "citation": {"citationType": "journal article"},
                "referenceComments": [{"type": "STRAIN", "value": "NTUH-K2044"}],
            }
        ],
        "uniProtKBCrossReferences": [
            {
                "database": "RefSeq",
                "id": "WP_004179723.1",
                "properties": [{"key": "NucleotideSequenceId", "value": "NC_012731.1"}],
            },
            {"database": "EMBL", "id": "AP006725"},
        ],
    }
    taxon = {
        "taxonId": 484021,
        "scientificName": audit.REFERENCE_NAME,
        "rank": "strain",
        "active": True,
        "parent": {"taxonId": 573, "scientificName": "Klebsiella pneumoniae"},
        "lineage": [audit.SPECIES],
    }
    return entry, taxon


def test_locus_match_preserves_native_symbol_and_reference_context():
    entry, taxon = native_fixture()
    result = audit.locus_reference(entry, taxon, "KP1_2583")
    assert result["reference"]["gene_symbols"] == ["ydgF"]
    assert result["reference"]["orf_names"] == ["KP1_2583"]
    assert result["individual_kpn_component_alias_assigned"] is False
    assert result["genome_context"]["experimental_derivative_genome_assigned"] is False
    assert result["genome_context"]["nucleotide_cross_reference_is_assembly_identifier"] is False


@pytest.mark.parametrize(
    "change",
    [
        "locus",
        "name_only",
        "accession",
        "strain",
        "rank",
        "species",
        "genome",
        "ambiguous_xref",
        "sequence",
        "bibliography",
    ],
)
def test_rejects_ambiguous_or_wrong_reference_identity(change):
    entry, taxon = native_fixture()
    if change == "locus":
        entry["genes"][0]["orfNames"][0]["value"] = "KP1_2584"
    elif change == "name_only":
        entry["genes"][0].pop("orfNames")
        entry["genes"][0]["geneName"]["value"] = "KP1_2583"
    elif change == "accession":
        entry["primaryAccession"] = "A0ACD7U1G2"
    elif change == "strain":
        entry["organism"]["scientificName"] = "Klebsiella pneumoniae"
    elif change == "rank":
        taxon["rank"] = "subspecies"
    elif change == "species":
        taxon["lineage"] = [{"taxonId": 562, "scientificName": "Escherichia coli", "rank": "species"}]
        taxon["parent"] = {"taxonId": 562, "scientificName": "Escherichia coli"}
    elif change == "genome":
        entry["uniProtKBCrossReferences"][0]["properties"][0]["value"] = "NC_012731.2"
    elif change == "ambiguous_xref":
        entry["uniProtKBCrossReferences"].append(copy.deepcopy(entry["uniProtKBCrossReferences"][0]))
    elif change == "sequence":
        entry["sequence"] = {}
    else:
        entry["references"][0]["referenceComments"][0]["value"] = "MGH78578"
    with pytest.raises(ValueError):
        audit.locus_reference(entry, taxon, "KP1_2583")


def query_fixture():
    body = json.dumps({"results": [native_fixture()[0]]})
    return {
        "url": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(audit.parameters("KP1_2583")),
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
        "status": 200,
        "bytes": len(body.encode()),
        "headers": {"X-Total-Results": "1", "X-UniProt-Release": "2026_03"},
        "retries": 0,
        "redirects_followed": 0,
    }


def test_single_native_query_is_complete():
    assert audit.query_entry(query_fixture(), "KP1_2583") == native_fixture()[0]


@pytest.mark.parametrize("change", ["total", "pagination", "checksum", "url", "release", "retry"])
def test_changed_query_provenance_rejected(change):
    receipt = query_fixture()
    if change == "total":
        receipt["headers"]["X-Total-Results"] = "2"
    elif change == "pagination":
        receipt["headers"]["Link"] = '<https://rest.uniprot.org/next>; rel="next"'
    elif change == "checksum":
        receipt["sha256"] = "0" * 64
    elif change == "url":
        receipt["url"] = receipt["url"].replace("KP1_2583", "KP1_2584")
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "2026_02"
    else:
        receipt["retries"] = 1
    with pytest.raises(ValueError):
        audit.query_entry(receipt, "KP1_2583")


@pytest.fixture
def request_cache(tmp_path):
    def save(path, value):
        path = tmp_path / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))
        return audit.reference.pin(tmp_path, path)

    plan = {
        "canary": "KP1_2583",
        "queries": {
            locus: {"url": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(audit.parameters(locus))}
            for locus in audit.LOCI
        },
    }
    plan_pin = save(audit.PLAN, plan)
    tax_url = "https://rest.uniprot.org/taxonomy/484021.json"
    native = {"plan": plan_pin, "new_uniprot_requests": 3, "attempts": {}, "queries": {}}
    for key, url in {**{k: v["url"] for k, v in plan["queries"].items()}, "tax-484021": tax_url}.items():
        receipt = {"url": url, "status": 200, "body": "{}", "bytes": 2, "retries": 0, "redirects_followed": 0}
        response = save(f"cache/{key}-receipt.json", receipt)
        native["attempts"][key] = save(
            f"cache/{key}-attempt.json",
            {
                "url": url,
                "ncbi_requests": 0,
                "retries": 0,
                "redirects_followed": 0,
            },
        )
        if key in audit.LOCI:
            native["queries"][key] = response
        else:
            native["native_taxonomy"] = {"484021": {"receipt": response, "body": None}}
    native["taxonomy_plan"] = save(
        "cache/taxonomy-plan.json",
        {
            "plan": plan_pin,
            "native_taxonomy": {},
            "missing": {"484021": tax_url},
        },
    )
    native["canary"] = save(
        "cache/canary-inspected.json",
        {
            "locus": "KP1_2583",
            "accession": "A0ACD7U1E6",
            "accepted": True,
            "reference_only": True,
            "receipt": native["queries"]["KP1_2583"],
        },
    )
    return tmp_path, plan, native, save


def test_request_accounting_replays_all_three_attempts(request_cache):
    root, plan, native, _ = request_cache
    audit.request_accounting(root, plan, native)


@pytest.mark.parametrize("change", ["extra_attempt", "error", "canary", "count", "retry", "ncbi"])
def test_request_accounting_rejects_unrecorded_or_promoted_activity(request_cache, change):
    root, plan, native, save = request_cache
    if change == "extra_attempt":
        save("cache/extra-attempt.json", {})
    elif change == "error":
        save("cache/failed-error.json", {})
    elif change == "count":
        native["new_uniprot_requests"] = 2
    elif change == "canary":
        pin = native["canary"]
        value = audit.read_json(root, pin)
        value["reference_only"] = False
        native["canary"] = save(pin["path"], value)
    else:
        pin = native["attempts"]["KP1_2584"]
        value = audit.read_json(root, pin)
        value["retries" if change == "retry" else "ncbi_requests"] = 1
        native["attempts"]["KP1_2584"] = save(pin["path"], value)
    with pytest.raises(ValueError):
        audit.request_accounting(root, plan, native)


def test_portable_artifact_covers_current_source_cohort(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.read_json(ROOT, result["prior_members"])
    audit.read_json(ROOT, result["plan"])
    audit.read_json(ROOT, result["native_plan"])
    audit.validate_assessment(audit.read_json(ROOT, result["assessment"]))
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] in audit.TERMS]
    ids = {c["record_identifier"] for c in result["claims"]}
    assert result["records"] == [r for r in prior["records"] if r["identifier"] in ids]
    assert len(ids) == 26 and len(result["claims"]) == 28
    assert {
        locus: row["reference"]["accession"].split(":")[1]
        for locus, row in result["locus_references"].items()
    } == audit.LOCI
    existing = result["existing_member_references"]
    assert len(existing) == 4
    for accession, row in existing.items():
        assert row["reference"] == prior["reference_proteins"][accession]
        assert row["comparison"] == audit.compare_member_reference(row["reference"])
        assert row["comparison"]["experimental_subject_assigned"] is False
    different = {a for a, r in existing.items() if r["comparison"]["reference_species"] != audit.SPECIES}
    assert different == {"UniProtKB:A0A1X3IY90", "UniProtKB:A0AAX3MPZ5"}
    assert result["summary"]["corpus_records_hash_checked"] == 2939
    assert result["summary"]["new_uniprot_requests"] == 3
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"


def test_no_operational_or_ast_fields_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "primers",
        "coordinates",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_replay_when_native_cache_available():
    native = json.loads((ROOT / audit.NATIVE).read_bytes())
    if not (ROOT / native["queries"]["KP1_2583"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")
    assert audit.build(ROOT) == public_result()

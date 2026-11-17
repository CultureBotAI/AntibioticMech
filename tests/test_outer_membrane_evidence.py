"""Citation overlap must not create an Omp1 accession, species or allele join."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_outer_membrane_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def metadata(monkeypatch):
    pmid = "25512405"
    monkeypatch.setitem(audit.ABSTRACT_SHA, pmid, hashlib.sha256(b"Metadata fixture").hexdigest())
    return {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:" + pmid + " AND SRC:MED", "resultType": "CORE", "pageSize": 1},
        "resultList": {
            "result": [
                {
                    **audit.PUBLICATIONS[pmid],
                    "pmid": pmid,
                    "id": pmid,
                    "source": "MED",
                    "abstractText": "Metadata fixture",
                }
            ]
        },
    }


def test_metadata_not_primary_or_access_denial(metadata):
    result = audit.project_metadata(metadata, "25512405")
    assert result["inEPMC"] == "Y" and result["isOpenAccess"] == "N"
    for key in (
        "primary_requested",
        "abstract_is_gene_crosswalk",
        "global_access_or_paywall_inferred",
        "missing_doi_or_pmcid_is_global_absence",
    ):
        assert result[key] is False
    assert "abstractText" not in result


@pytest.mark.parametrize("key,value", [("hitCount", True), ("hitCount", 2), ("nextCursorMark", "next")])
def test_metadata_completeness(metadata, key, value):
    metadata[key] = value
    with pytest.raises(ValueError, match="scope or completeness"):
        audit.project_metadata(metadata, "25512405")


@pytest.mark.parametrize(
    "key,value",
    [
        ("queryString", "EXT_ID:9353750 AND SRC:MED"),
        ("pageSize", True),
        ("pageSize", 2),
        ("resultType", "lite"),
    ],
)
def test_metadata_query_identity(metadata, key, value):
    metadata["request"][key] = value
    with pytest.raises(ValueError, match="scope or completeness"):
        audit.project_metadata(metadata, "25512405")


@pytest.mark.parametrize(
    "key,value",
    [
        ("id", "9353750"),
        ("pmid", "9353750"),
        ("source", "PMC"),
        ("doi", "other"),
        ("pmcid", "PMC1"),
        ("title", "Other"),
        ("pubYear", "1997"),
        ("abstractText", "Changed"),
        ("isOpenAccess", "Y"),
        ("inEPMC", "N"),
    ],
)
def test_metadata_native_fields(metadata, key, value):
    metadata["resultList"]["result"][0][key] = value
    with pytest.raises(ValueError, match="publication identity"):
        audit.project_metadata(metadata, "25512405")


@pytest.fixture
def primary(monkeypatch):
    payload = b"""<article><front><article-meta>
    <article-id pub-id-type="pmid">25856195</article-id>
    <article-id pub-id-type="pmcid">PMC4391916</article-id>
    <article-id pub-id-type="doi">10.1371/journal.pone.0123061</article-id>
    </article-meta></front><body><p id="taxonomic_context">Context fixture</p>
    <p id="paper_species_interpretation">Species fixture</p>
    <p id="resistance_context">Prediction and phenotype are distinct</p>
    <p id="data_availability">accession number: CP005927</p></body></article>"""
    tree = audit.etree.fromstring(payload)
    locations = {}
    for key in audit.LOCATIONS:
        xpath = f"/article/body/p[@id='{key}']"
        text = " ".join("".join(tree.xpath(xpath)[0].itertext()).split())
        locations[key] = (xpath, hashlib.sha256(text.encode()).hexdigest())
    monkeypatch.setattr(audit, "LOCATIONS", locations)
    monkeypatch.setitem(audit.BODY_SHA, "primary-25856195", hashlib.sha256(payload).hexdigest())
    return payload


def test_primary_study_genome_not_resistance_mapping(primary):
    result = audit.project_primary(primary)
    assert result["study_genome"]["accession"] == "CP005927"
    assert result["study_genome"]["version"] is None
    for key in ("ncbi_link_followed", "independently_verified", "assembly_accession_inferred"):
        assert result["study_genome"][key] is False
    for key in (
        "current_taxon_id_assigned_from_paper",
        "resistance_gene_accession_assigned",
        "exact_resistant_allele_assigned",
    ):
        assert result[key] is None
    for key in (
        "full_paper_signoff",
        "figures_visually_reviewed",
        "tables_reviewed_for_AST_curation",
        "supplements_reviewed",
        "numeric_AST_exported",
    ):
        assert result[key] is False
    assert result["text_screen"]["match_count"] == 0
    assert result["text_screen"]["establishes_gene_absence"] is False
    assert result["text_screen"]["invalidates_source_citation"] is False


def test_primary_bytes_pinned(primary):
    with pytest.raises(ValueError, match="XML changed"):
        audit.project_primary(primary + b" ")


@pytest.mark.parametrize(
    "old,new",
    [
        (b"25856195", b"9353750"),
        (b"PMC4391916", b"PMC1"),
        (b"10.1371/journal.pone.0123061", b"other"),
        (b"CP005927", b"CP000000"),
        (b"Context fixture", b"Other"),
        (b'id="taxonomic_context"', b'id="missing"'),
    ],
)
def test_primary_identity_and_locations(primary, monkeypatch, old, new):
    changed = primary.replace(old, new)
    monkeypatch.setitem(audit.BODY_SHA, "primary-25856195", hashlib.sha256(changed).hexdigest())
    with pytest.raises(ValueError):
        audit.project_primary(changed)


@pytest.mark.parametrize("mention", ["Omp1", "ompA", "Porins", "porin"])
def test_literal_screen_fails_closed_on_new_mentions(primary, monkeypatch, mention):
    changed = primary.replace(b"</body>", ("<p>" + mention + "</p></body>").encode())
    monkeypatch.setitem(audit.BODY_SHA, "primary-25856195", hashlib.sha256(changed).hexdigest())
    with pytest.raises(ValueError, match="literal porin"):
        audit.project_primary(changed)


@pytest.fixture
def entry():
    return {
        "primaryAccession": "A0A0J9X1Q5",
        "entryAudit": {"entryVersion": 39, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "pigE"}}],
        "organism": {"taxonId": 1327989, "scientificName": "Serratia sp. (strain FS14)"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Aminotransferase PigE"}}},
        "references": [
            {
                "referenceNumber": i,
                "citation": {
                    "id": p,
                    "citationType": "journal article",
                    "title": "Fixture",
                    "publicationDate": "2015",
                    "citationCrossReferences": [{"database": "PubMed", "id": p}],
                },
                "referenceComments": [{"type": "STRAIN", "value": "FS14"}],
                "referencePositions": ["SEQUENCE_SENTINEL"],
            }
            for i, p in enumerate(("25856195", "24704447"), 1)
        ],
        "sequence": "SEQUENCE_SENTINEL",
        "uniProtKBCrossReferences": [],
    }


def test_shared_citation_does_not_assign_pige_to_omp1(entry):
    result = audit.project_nonmatch(entry)
    assert result["reference_gene"] == "pigE"
    assert result["reference_taxon_id"] == "NCBITaxon:1327989"
    assert result["assigned_to_source_term"] is False
    assert result["paper_species_label_overwrites_native_taxon"] is False
    assert result["matching_strain_comment_is_experimental_crosswalk"] is False
    assert len(result["native_bibliography"]) == 2
    assert "SEQUENCE_SENTINEL" not in json.dumps(result)


@pytest.mark.parametrize(
    "change",
    [
        "gene",
        "synonym",
        "card_xref",
        "accession",
        "taxon",
        "label",
        "protein",
        "version",
        "seq_version",
        "pmid",
        "strain",
    ],
)
def test_nonmatching_identity_cannot_change_silently(entry, change):
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "Omp1"
    elif change == "synonym":
        entry["genes"][0]["synonyms"] = [{"value": "oMp1"}]
    elif change == "card_xref":
        entry["uniProtKBCrossReferences"].append({"database": "CARD", "id": "ARO:3004128"})
    elif change == "accession":
        entry["primaryAccession"] = "P0A000"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 615
    elif change == "label":
        entry["organism"]["scientificName"] = "Serratia marcescens"
    elif change == "protein":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "Omp1"
    elif change in {"version", "seq_version"}:
        entry["entryAudit"]["entryVersion" if change == "version" else "sequenceVersion"] += 1
    elif change == "pmid":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "9353750"
    else:
        entry["references"][0]["referenceComments"][0]["value"] = "Other"
    with pytest.raises(ValueError):
        audit.project_nonmatch(entry)


def test_cli_idempotent_check_and_no_overwrite(tmp_path, monkeypatch):
    output = tmp_path / "output.json"
    monkeypatch.setattr(audit, "OUTPUT", output)
    monkeypatch.setattr(audit, "build", lambda root: {"result": 1})
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    monkeypatch.setattr(sys, "argv", ["audit"])
    audit.main()
    audit.main()
    output.write_text("old\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert output.read_text() == "old\n"


def test_published_scope_and_current_prior_memberships():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    prior = json.loads((ROOT / audit.prior.OUTPUT).read_bytes())
    assert result["terms"] == {tid: prior["terms"][tid] for tid in audit.TERMS}
    assert len(result["records"]) == 14 and len(result["claims"]) == 15
    assert result["summary"]["experimental_gene_allele_assignments"] == 0
    assert result["summary"]["new_verified_resistance_results"] == 0
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert set(result["publications"]) == set(audit.PMIDS)
    assert "referencePositions" not in json.dumps(result)


@pytest.fixture
def request_cache(tmp_path, monkeypatch):
    def save(name, data):
        path = tmp_path / name
        path.write_text(json.dumps(data, sort_keys=True) + "\n")
        return audit.reference.pin(tmp_path, path)

    cohort = save("cohort.json", {})
    specs = [("metadata-" + p, "metadata-plan.json", audit.metadata_url(p)) for p in audit.PMIDS]
    specs.append(("primary-25856195", "primary-plan.json", audit.XML_URL))
    plans = {}
    for filename in audit.PLAN_SHA:
        plans[filename] = save(
            filename,
            {
                "cohort": cohort,
                "requests": {k: {"url": url} for k, f, url in specs if f == filename},
                "automatic_redirects": False,
                "retry_performed": False,
                "ncbi_requests": 0,
            },
        )
        monkeypatch.setitem(audit.PLAN_SHA, filename, plans[filename]["sha256"])
    sources = {}
    for i, (key, filename, url) in enumerate(specs):
        body = save(key + "-response.bin", {})
        monkeypatch.setitem(audit.BODY_SHA, key, body["sha256"])
        attempt = save(
            key + "-attempt.json",
            {
                "url": url,
                "plan_sha256": plans[filename]["sha256"],
                "started_at": f"2026-10-15T06:00:{i * 2:02d}+00:00",
                "retry_performed": False,
            },
        )
        receipt = save(
            key + "-receipt.json",
            {
                "url": url,
                "status": 200,
                "sha256": body["sha256"],
                "bytes": (tmp_path / body["path"]).stat().st_size,
                "retrieved_at": f"2026-10-15T06:00:{i * 2 + 1:02d}+00:00",
                "retry_performed": False,
                "redirects_followed": False,
            },
        )
        sources[key] = {"body": body, "attempt": attempt, "receipt": receipt, "plan": plans[filename]}
    save(
        "metadata-canary-review.json",
        {
            **{k: sources["metadata-25512405"][k] for k in ("body", "receipt", "plan")},
            "manually_inspected": True,
            "primary_results_reviewed": False,
        },
    )
    return tmp_path, save


def test_native_request_provenance_without_ignored_cache(request_cache):
    directory, _ = request_cache
    sources = audit.request_context(directory, directory)
    assert set(sources) == set(audit.BODY_SHA)


@pytest.mark.parametrize("change", ["extra_request", "bad_plan", "body", "canary", "chronology", "redirect"])
def test_request_provenance_tampering_fails_closed(request_cache, change):
    directory, save = request_cache
    if change == "extra_request":
        save("unexpected-attempt.json", {})
    elif change == "bad_plan":
        save("primary-plan.json", {})
    elif change == "body":
        save("primary-25856195-response.bin", {"changed": True})
    elif change == "canary":
        path = directory / "metadata-canary-review.json"
        row = json.loads(path.read_bytes())
        row["manually_inspected"] = False
        save(path.name, row)
    else:
        path = directory / "primary-25856195-receipt.json"
        row = json.loads(path.read_bytes())
        if change == "redirect":
            row["redirects_followed"] = True
        else:
            row["retrieved_at"] = "2026-10-15T05:00:00+00:00"
        save(path.name, row)
    with pytest.raises(ValueError):
        audit.request_context(directory, directory)


def test_native_cohort_build_without_network_or_ignored_cache(
    request_cache, metadata, primary, entry, monkeypatch
):
    root, save = request_cache
    old = {
        "terms": {
            tid: {
                "reference_status": "NO_EXACT_GENE_RESULTS_NOT_ABSENCE",
                "record_memberships": ["CHEBI:1"],
                "definition_citation_ids": ["PMID:25512405"],
            }
            for tid in audit.TERMS
        },
        "records": [{"identifier": "CHEBI:1"}],
        "claims": [{"aro_id": t} for t in audit.TERMS],
        "summary": {"fixture": True},
    }
    old_pin = save("prior.json", old)
    prior_proof = save("prior-verification.json", {"files": [old_pin], "summary": old["summary"]})
    queries = {p: {"complete_for_query": True, "release": "2026_03"} for p in audit.PMIDS}
    entries = {"25512405": {}, "25856195": {"A0A0J9X1Q5": entry}, "9353750": {}}
    pins = {k: save(k + ".json", {}) for k in ("census", "source_queue", "protected", "access_inventory")}
    frozen = save("literature.json", {"queries": queries, "entries": entries})
    cohort = {
        "date": "2026-10-14",
        "prior": old_pin,
        "prior_verification": prior_proof,
        **pins,
        "literature": frozen,
        "terms": old["terms"],
        "records": old["records"],
        "claims": old["claims"],
        "pmids": list(audit.PMIDS),
    }
    cohort_pin = save("cohort.json", cohort)
    monkeypatch.setattr(audit, "COHORT_SHA", cohort_pin["sha256"])
    monkeypatch.setattr(audit.prior, "build", lambda root: copy.deepcopy(old))
    monkeypatch.setattr(
        audit.literature, "read_query", lambda root, directory, pmid: (entries[pmid], queries[pmid])
    )
    monkeypatch.setattr(audit, "request_context", lambda root, directory: {k: {} for k in audit.BODY_SHA})
    for p in audit.PMIDS:
        row = copy.deepcopy(metadata)
        row["request"]["queryString"] = "EXT_ID:" + p + " AND SRC:MED"
        row["resultList"]["result"][0].update(audit.PUBLICATIONS[p], id=p, pmid=p)
        monkeypatch.setitem(audit.ABSTRACT_SHA, p, hashlib.sha256(b"Metadata fixture").hexdigest())
        save("metadata-" + p + "-response.bin", row)
    (root / "primary-25856195-response.bin").write_bytes(primary)
    result = audit.build(root, root)
    assert result["summary"]["source_terms"] == 2
    assert result["summary"]["cohort_records"] == 1
    assert result["terms"] == old["terms"]
    assert result["primary_context"]["current_taxon_id_assigned_from_paper"] is None
    assert result["unassigned_citation_hits"][0]["assigned_to_source_term"] is False
    old["claims"].append({"aro_id": "ARO:3004128"})
    with pytest.raises(ValueError, match="current corpus changed"):
        audit.build(root, root)

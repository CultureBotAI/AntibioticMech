"""Kpn source labels, missing hits and homologs are not experimental identities."""

import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_kpn_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def metadata(monkeypatch):
    pmid = "23836167"
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


def test_non_oa_metadata_is_not_access_denial(metadata):
    result = audit.project_metadata(metadata, "23836167")
    assert result["inEPMC"] == "Y" and result["isOpenAccess"] == "N"
    for key in (
        "primary_requested",
        "abstract_is_gene_crosswalk",
        "global_access_or_paywall_inferred",
        "access_denial_inferred",
    ):
        assert result[key] is False
    assert "abstractText" not in result


@pytest.mark.parametrize("key,value", [("hitCount", True), ("hitCount", 2), ("nextCursorMark", "next")])
def test_metadata_completeness(metadata, key, value):
    metadata[key] = value
    with pytest.raises(ValueError, match="scope or completeness"):
        audit.project_metadata(metadata, "23836167")


@pytest.mark.parametrize(
    "key,value", [("queryString", "other"), ("pageSize", True), ("pageSize", 2), ("resultType", "lite")]
)
def test_query_identity(metadata, key, value):
    metadata["request"][key] = value
    with pytest.raises(ValueError, match="scope or completeness"):
        audit.project_metadata(metadata, "23836167")


@pytest.mark.parametrize(
    "key,value",
    [
        ("id", "24823362"),
        ("pmid", "24823362"),
        ("source", "PMC"),
        ("doi", "other"),
        ("pmcid", "PMC1"),
        ("title", "other"),
        ("pubYear", "2014"),
        ("abstractText", "changed"),
        ("isOpenAccess", "Y"),
        ("inEPMC", "N"),
    ],
)
def test_metadata_native_fields(metadata, key, value):
    metadata["resultList"]["result"][0][key] = value
    with pytest.raises(ValueError, match="publication identity"):
        audit.project_metadata(metadata, "23836167")


@pytest.fixture
def primary(monkeypatch):
    payload = b"""<article><front><article-meta>
    <article-id pub-id-type="pmid">24823362</article-id>
    <article-id pub-id-type="pmcid">PMC4019481</article-id>
    <article-id pub-id-type="doi">10.1371/journal.pone.0096288</article-id>
    </article-meta></front><body><p id="study_background">Background fixture</p>
    <p id="component_names">KpnG and KpnH proteins. The KpnF also: inconsistent fixture label.</p>
    <p id="genome_context">NTUH-K2044 (NC_012731.1)</p>
    <p id="distinct_experimental_contexts">E. coli KAM32: distinct fixture context.</p>
    </body></article>"""
    tree = audit.etree.fromstring(payload)
    locations = {}
    for key in audit.LOCATIONS:
        xpath = f"/article/body/p[@id='{key}']"
        text = " ".join("".join(tree.xpath(xpath)[0].itertext()).split())
        locations[key] = (xpath, hashlib.sha256(text.encode()).hexdigest())
    monkeypatch.setattr(audit, "LOCATIONS", locations)
    monkeypatch.setitem(audit.BODY_SHA, "primary-24823362", hashlib.sha256(payload).hexdigest())
    return payload


def test_component_inconsistency_homology_and_hosts_not_equated(primary):
    result = audit.project_primary(primary)
    assert result["source_component_names"] == ["KpnG", "KpnH"]
    assert result["label_inconsistency"]["reported_label"] == "KpnF"
    assert result["label_inconsistency"]["correction_inferred"] is False
    assert result["label_inconsistency"]["accepted_as_alias"] is False
    assert result["homology_context"]["accepted_as_exact_alias"] is False
    assert result["homology_context"]["accession_substituted_by_homology"] is False
    assert result["heterologous_host_context"]["merged_with_native_subject"] is False
    for key in (
        "protein_accession_assigned",
        "exact_resistant_allele_assigned",
        "experimental_strain_taxon_assigned",
        "experimental_genome_assigned",
    ):
        assert result[key] is None
    for key in (
        "full_paper_signoff",
        "figures_visually_reviewed",
        "tables_reviewed_for_AST_curation",
        "supplements_reviewed",
        "numeric_AST_exported",
        "sequence_variant_protocol_exported",
    ):
        assert result[key] is False
    assert result["paper_reported_genome"]["accession"] == "NC_012731.1"
    for key in (
        "independently_verified",
        "ncbi_link_followed",
        "assembly_accession_inferred",
        "exact_resistance_allele_crosswalk",
    ):
        assert result["paper_reported_genome"][key] is False
    assert result["tolc_screen"]["match_count"] == 0
    for key in ("establishes_absence", "invalidates_CARD_label", "supports_TolC_component_assignment"):
        assert result["tolc_screen"][key] is False


def test_primary_bytes_pinned(primary):
    with pytest.raises(ValueError, match="XML changed"):
        audit.project_primary(primary + b" ")


@pytest.mark.parametrize(
    "old,new",
    [
        (b"24823362", b"23836167"),
        (b"PMC4019481", b"PMC1"),
        (b"10.1371/journal.pone.0096288", b"other"),
        (b"NC_012731.1", b"NC_012731.2"),
        (b"The KpnF also", b"The KpnH also"),
        (b"KpnG and KpnH", b"KpnE and KpnF"),
        (b"E. coli KAM32", b"K. pneumoniae"),
        (b'id="study_background"', b'id="missing"'),
    ],
)
def test_primary_identity_and_context_cannot_change(primary, monkeypatch, old, new):
    changed = primary.replace(old, new)
    monkeypatch.setitem(audit.BODY_SHA, "primary-24823362", hashlib.sha256(changed).hexdigest())
    with pytest.raises(ValueError):
        audit.project_primary(changed)


@pytest.mark.parametrize("mention", ["TolC", "tolc", "TOLC"])
def test_new_literal_component_requires_review(primary, monkeypatch, mention):
    changed = primary.replace(b"</body>", ("<p>" + mention + "</p></body>").encode())
    monkeypatch.setitem(audit.BODY_SHA, "primary-24823362", hashlib.sha256(changed).hexdigest())
    with pytest.raises(ValueError, match="TolC mention"):
        audit.project_primary(changed)


@pytest.mark.parametrize("gene,reviewed", [("kpnG", True), ("kpnH", False)])
def test_component_query_is_exact_species_reference(gene, reviewed):
    from urllib.parse import parse_qs, urlsplit

    parsed = urlsplit(audit.gene_url(gene, reviewed))
    params = parse_qs(parsed.query)
    assert parsed.netloc == "rest.uniprot.org"
    assert params["query"] == [f"gene_exact:{gene} AND taxonomy_id:573 AND reviewed:{str(reviewed).lower()}"]
    assert "sequence" not in params["fields"][0].split(",")


@pytest.mark.parametrize("gene,reviewed", [("kpnEF", True), ("TolC", True), ("emrA", True), ("kpnG", 1)])
def test_complex_homology_and_unplanned_queries_rejected(gene, reviewed):
    with pytest.raises(ValueError, match="unplanned component"):
        audit.gene_url(gene, reviewed)


@pytest.fixture
def request_cache(tmp_path, monkeypatch):
    def save(name, data):
        path = tmp_path / name
        path.write_text(json.dumps(data, sort_keys=True) + "\n")
        return audit.reference.pin(tmp_path, path)

    cohort = save("cohort.json", {})
    specs, plans = audit.request_specs(), {}
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
        body = save(key + "-response.bin", {"results": []})
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
                "headers": {"X-UniProt-Release": "2026_03", "X-Total-Results": "0"},
                "retrieved_at": f"2026-10-15T06:00:{i * 2 + 1:02d}+00:00",
                "retry_performed": False,
                "redirects_followed": False,
            },
        )
        sources[key] = {"body": body, "attempt": attempt, "receipt": receipt, "plan": plans[filename]}
    save(
        "metadata-canary.json",
        {
            **sources["metadata-24823362"],
            "identity_checked": True,
            "continue_second_planned_metadata_request": True,
            "ncbi_requests": 0,
        },
    )
    save(
        "primary-canary-review.json",
        {
            **sources["primary-24823362"],
            "identity_checked": True,
            "selected_context_manually_inspected": True,
            "source_components": ["KpnG", "KpnH"],
            "results_label_inconsistency": "KpnF",
            "inconsistency_silently_corrected": False,
            "tolc_absence_inferred": False,
            "full_paper_signoff": False,
            "sequence_variant_protocol_exported": False,
        },
    )
    return tmp_path, save


def test_request_and_native_empty_queries_without_ignored_cache(request_cache):
    root, _ = request_cache
    sources = audit.request_context(root, root)
    assert len(sources) == 7
    for kind in ("reviewed", "unreviewed"):
        for gene in audit.GENES:
            row = audit.read_component(root, sources[kind + "-" + gene.lower()], gene, kind == "reviewed")
            assert row["complete_for_query"] is True and row["accessions"] == []
            assert row["zero_hits_are_absence"] is row["experimental_assignment"] is False


@pytest.mark.parametrize(
    "change",
    [
        "extra_request",
        "bad_plan",
        "body",
        "metadata_canary",
        "primary_canary",
        "chronology",
        "redirect",
        "retry",
        "status",
        "bytes",
    ],
)
def test_request_tampering_fails_closed(request_cache, change):
    root, save = request_cache
    if change == "extra_request":
        save("unexpected-attempt.json", {})
    elif change == "bad_plan":
        save("primary-plan.json", {})
    elif change == "body":
        save("primary-24823362-response.bin", {"changed": True})
    elif change in ("metadata_canary", "primary_canary"):
        name = "metadata-canary.json" if change == "metadata_canary" else "primary-canary-review.json"
        row = json.loads((root / name).read_bytes())
        row["identity_checked"] = False
        save(name, row)
    else:
        name = "primary-24823362-receipt.json"
        row = json.loads((root / name).read_bytes())
        key, value = {
            "chronology": ("retrieved_at", "2026-10-15T05:00:00+00:00"),
            "redirect": ("redirects_followed", True),
            "retry": ("retry_performed", True),
            "status": ("status", 403),
            "bytes": ("bytes", 1),
        }[change]
        row[key] = value
        save(name, row)
    with pytest.raises(ValueError):
        audit.request_context(root, root)


@pytest.mark.parametrize("change", ["query", "pagination", "count", "release"])
def test_native_query_completeness_and_identity(request_cache, change):
    root, save = request_cache
    source = audit.request_context(root, root)["reviewed-kpng"]
    if change == "query":
        source["url"] = audit.gene_url("kpnH", True)
    else:
        name = "reviewed-kpng-receipt.json"
        row = json.loads((root / name).read_bytes())
        key, value = {
            "pagination": ("Link", "next"),
            "count": ("X-Total-Results", "1"),
            "release": ("X-UniProt-Release", "2026_02"),
        }[change]
        row["headers"][key] = value
        source["receipt"] = save(name, row)
    with pytest.raises(ValueError):
        audit.read_component(root, source, "kpnG", True)


def test_new_exact_candidate_cannot_be_silently_assigned(monkeypatch):
    entry = {
        "primaryAccession": "P00001",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "genes": [{"geneName": {"value": "kpnG"}}],
        "organism": {"taxonId": 573},
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
    }
    monkeypatch.setattr(audit.outer.native, "read_source", lambda *args: ({"results": [entry]}, {}))
    with pytest.raises(ValueError, match="new component candidates require review"):
        audit.read_component(ROOT, {"url": audit.gene_url("kpnG", True)}, "kpnG", True)


def test_cli_does_not_overwrite(tmp_path, monkeypatch):
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


def test_saved_dossier_has_complete_source_memberships():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads((ROOT / result["inputs"]["prior"]["path"]).read_bytes())
    assert set(result["terms"]) == set(audit.TERMS)
    for tid, term in result["terms"].items():
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert term["prior_links"] == index["terms"][tid]["links"] == []
    assert len(result["records"]) == 26 and len(result["claims"]) == 28
    assert result["summary"]["experimental_gene_allele_assignments"] == 0
    assert result["summary"]["biological_records_changed"] == 0
    assert result["reference_species"]["taxon_id"] == "NCBITaxon:573"
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
    assert all(
        r["single_protein_assigned"] is r["experimental_allele_assigned"] is None
        for r in result["term_dispositions"].values()
    )
    assert "referencePositions" not in json.dumps(result)


def test_saved_claims_preserve_every_prior_position_and_hash():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads((ROOT / result["inputs"]["prior"]["path"]).read_bytes())
    expected = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in index["claims"]
        if c["aro_id"] in audit.TERMS
    ]

    def order(claim):
        return claim["record_identifier"], claim["position"]

    assert sorted(result["claims"], key=order) == sorted(expected, key=order)
    assert {r["identifier"] for r in result["records"]} == {c["record_identifier"] for c in expected}

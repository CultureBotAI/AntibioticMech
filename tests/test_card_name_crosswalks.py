"""Nomenclature proofs preserve ambiguity, taxonomic rank and experimental limits."""

import builtins
import copy
import io
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_name_crosswalks as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline name audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


LPSN = """<html><title>Species: Mycobacteroides abscessus</title><table><tr>
<td>Mycobacterium <i>abscessus</i> (Moore and Frerichs 1953) Kusunoki and Ezaki 1992</td>
<td>homotypic synonym, validly published under the ICNP</td></tr></table></html>"""
FIJI = """<html><meta name="citation_title"
content="Example Pseudocercospora fijiensis (Synonym Mycosphaerella fijiensis)">
<meta name="citation_doi" content="10.1371/journal.pgen.1005876">
<div class="abstract">Pseudocercospora fijiensis (previously: Mycosphaerella fijiensis)</div></html>"""


def test_lpsn_binds_validly_published_homotypic_synonym():
    result = audit.lpsn_context(LPSN)
    assert result["relation"] == "HOMOTYPIC_SYNONYM"
    assert result["genus_preference_or_experimental_subject_inferred"] is False


@pytest.mark.parametrize(
    "old,new",
    [
        ("Species: Mycobacteroides", "Species: Other"),
        ("Kusunoki and Ezaki 1992", "Moore and Frerichs 1953"),
        ("homotypic", "heterotypic"),
        ("validly published", "not validly published"),
        ("Mycobacterium", "Mycobacteroides"),
    ],
)
def test_lpsn_wrong_relation_or_historical_name_is_not_accepted(old, new):
    with pytest.raises(ValueError):
        audit.lpsn_context(LPSN.replace(old, new))


def test_duplicate_synonym_row_rejected():
    with pytest.raises(ValueError):
        audit.lpsn_context(LPSN.replace("</table>", LPSN.split("<table>")[1]))


def test_author_institution_name_crosswalk_has_limited_scope():
    result = audit.fijiensis_context(FIJI)
    assert result["doi"] == "10.1371/journal.pgen.1005876"
    assert result["full_text_results_or_phylogeny_reviewed"] is False


@pytest.mark.parametrize(
    "old,new",
    [
        ("10.1371/journal.pgen.1005876", "10.1234/wrong"),
        ("Synonym Mycosphaerella", "Similar to Mycosphaerella"),
        ("previously: Mycosphaerella", "compared with Mycosphaerella"),
        ('name="citation_title"', 'name="other_title"'),
    ],
)
def test_publication_name_context_is_not_inferred_from_mentions(old, new):
    with pytest.raises(ValueError):
        audit.fijiensis_context(FIJI.replace(old, new))


def name_fixture():
    identity = {"taxonId": 1, "rank": "species", "scientificName": "Current name"}
    node = {**identity, "active": True, "lineage": [], "otherNames": ["Historical name"]}
    proof = {
        "source_name": "Historical name",
        "uniprot_name": "Current name",
        "relation": "FORMAL_NEW_COMBINATION",
    }
    return {"results": [node]}, identity, proof


def test_independent_nomenclature_required_for_other_name():
    payload, identity, proof = name_fixture()
    with pytest.raises(ValueError, match="native scientific name"):
        audit.accept_name(payload, "Historical name", identity, None)
    result = audit.accept_name(payload, "Historical name", identity, proof)
    assert result["identity"] == identity
    assert result["experimental_subject_assignment"] is False


@pytest.mark.parametrize(
    "mutation",
    [
        "inactive",
        "duplicate_id",
        "ambiguous_name",
        "wrong_name",
        "wrong_taxid",
        "rank",
        "missing_other_name",
        "wrong_proof",
        "spelling",
    ],
)
def test_name_binding_rejects_ambiguity_or_unsupported_changes(mutation):
    payload, identity, proof = name_fixture()
    node = payload["results"][0]
    if mutation == "inactive":
        node["active"] = False
    elif mutation == "duplicate_id":
        payload["results"].append(copy.deepcopy(node))
    elif mutation == "ambiguous_name":
        payload["results"].append({**node, "taxonId": 2})
    elif mutation == "wrong_name":
        node["scientificName"] = "Different name"
    elif mutation == "wrong_taxid":
        node["taxonId"] = 2
    elif mutation == "rank":
        node["rank"] = "strain"
    elif mutation == "missing_other_name":
        node["otherNames"] = []
    elif mutation == "wrong_proof":
        proof["relation"] = "FUZZY_MATCH"
    elif mutation == "spelling":
        proof["source_name"] = "Historical nam"
    with pytest.raises(ValueError):
        audit.accept_name(payload, "Historical name", identity, proof)


def test_unranked_name_does_not_become_species_ancestor():
    parent = {"taxonId": 1, "rank": "species", "scientificName": "Parent species"}
    identity = {"taxonId": 2, "rank": "no rank", "scientificName": "Named taxon"}
    node = {**identity, "active": True, "parent": parent, "lineage": [parent]}
    result = audit.accept_name({"results": [node]}, "Named taxon", identity, None)
    assert result["identity"]["rank"] == "no rank"
    assert result["species_ancestor"] == parent
    assert result["source_name_automatically_replaced_by_species_ancestor"] is False
    with pytest.raises(ValueError, match="ambiguous"):
        audit.accept_name({"results": [node, {**node, "taxonId": 3}]}, "Named taxon", identity, None)


def old_queries_fixture():
    result = {}
    for source, term, gene, tid in (
        ("fungamr", "ARO:3009390", "Cdc6", "5478"),
        ("folp", "ARO:3007749", "folP", "594"),
    ):
        rows = []
        for status in (True, False):
            url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
                {"query": f"gene_exact:{gene} AND taxonomy_id:{tid} AND reviewed:{str(status).lower()}"}
            )
            rows.append(
                {
                    "key": source + str(status),
                    "source": {"url": url},
                    "reviewed_subset": status,
                    "result_count": 0,
                }
            )
        result[source] = {
            "terms": {
                term: {
                    "queries": rows
                    if source == "fungamr"
                    else dict(zip(("reviewed", "unreviewed"), rows, strict=True))
                }
            }
        }
    return result


@pytest.mark.parametrize("mutation", [None, "missing_partition", "wrong_taxon", "wrong_status", "nonzero"])
def test_reuse_both_historical_query_shapes_without_reissuing(monkeypatch, mutation):
    inputs = old_queries_fixture()
    rows = inputs["folp"]["terms"]["ARO:3007749"]["queries"]
    if mutation == "missing_partition":
        rows.pop("reviewed")
    elif mutation == "wrong_taxon":
        rows["reviewed"]["source"]["url"] = rows["reviewed"]["source"]["url"].replace("594", "595")
    elif mutation == "wrong_status":
        rows["reviewed"]["reviewed_subset"] = False
    elif mutation == "nonzero":
        rows["reviewed"]["result_count"] = 1
    monkeypatch.setattr(
        audit.prior.prior.members.screen, "read_source", lambda *a: ({"results": []}, {"complete": True})
    )
    if mutation:
        with pytest.raises(ValueError):
            audit.old_zero_queries(ROOT, inputs)
    else:
        result = audit.old_zero_queries(ROOT, inputs)
        assert len(result) == 4
        assert all(r["reused"] and not r["biological_absence_inferred"] for r in result.values())


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_saved_coverage_retains_holds_and_multiplicity():
    d = saved()
    s = d["summary"]
    assert (s["selected_terms"], s["source_claims"], s["complete_records_read"]) == (36, 38, 22)
    assert (s["resolved_reference_name_contexts"], s["terms_with_resolved_reference_names"]) == (4, 5)
    assert (s["qualified_reference_terms"], s["qualified_reference_links"]) == (2, 4)
    assert s["remaining_name_unresolved_terms"] == 31
    assert s["selected_terms_without_qualified_references"] == 34
    assert s["entry_type_counts"] == {"UniProtKB unreviewed (TrEMBL)": 4}
    assert d["nomenclature_access_hold"]["source"]["status"] == 302
    assert d["nomenclature_access_hold"]["full_text_retrieved"] is False
    assert all(
        len(r["qualified_reference_accessions"]) == 2
        for r in d["terms"].values()
        if r["qualified_reference_accessions"]
    )
    assert all(r["experimental_subject_assignment"] is False for r in d["terms"].values())


def test_current_statuses_do_not_inherit_historical_not_queried_or_null_species():
    d = saved()
    previous = json.loads((ROOT / d["inputs"]["name_checkpoint"]["path"]).read_bytes())
    for term, row in d["terms"].items():
        assert row["prior_name_assessment"] == previous["terms"][term]
        assert "reference_species" not in row
        assert row["prior_name_assessment"]["protein_reference_status"] == "NOT_QUERIED_BY_THIS_NAME_AUDIT"
        if row["reference_name_context"]:
            assert row["name_status"] == "RESOLVED_REFERENCE_NAME_RANK_PRESERVED"
        else:
            assert row["name_status"] == row["prior_name_assessment"]["name_status"]
        if row["qualified_reference_accessions"]:
            assert row["protein_reference_status"] == "QUALIFIED_REFERENCE_CONTEXT_NOT_EXPERIMENTAL_ALLELE"
        elif row["new_query_keys"] or row["reused_query_keys"]:
            assert row["protein_reference_status"] == "COMPLETE_QUERY_ZERO_RESULTS"
        else:
            assert row["protein_reference_status"] == "NOT_QUERIED_BY_THIS_CROSSWALK_AUDIT"
        assert row["whole_record_primary_review"] == "OPEN"
        assert row["exact_allele_assignment"] is row["primary_resistance_validation"] is False


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    required = [v["receipt"]["path"] for v in d["source_snapshots"].values()]
    if not all((ROOT / p).exists() for p in required):
        pytest.skip("ignored native sources unavailable; portable tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


def test_cli_nested_output_and_immutable_replay(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"

"""Replay primary nomenclature, empty identifier queries, and an access hold."""

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from zipfile import ZipFile

import audit_card_reference_memberships as memberships
import audit_topoisomerase_references as reference
from audit_curator_resistance_fields import owner
from audit_sal_reference_context import metadata_only, require, species_context

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-aph-mph-primary"
CACHE = "reports/resistance-grounding-2026-10-15-aph-mph-primary"
EXPECTED = {
    "mphF": ("ARO:3003071", "CAJ98570.1", "INSDC_PROTEIN"),
    "mphL": ("ARO:3003072", "WP_001094257.1", "RefSeq"),
    "mphM": ("ARO:3003767", "WP_001041372.1", "RefSeq"),
    "mphI": ("ARO:3003991", "KX531056.1", "INSDC_NUCLEOTIDE"),
    "mphO": ("ARO:3004543", "WP_050815728.1", "RefSeq"),
}


def read(root, pin):
    return json.loads(reference.check_pin(root, pin).read_bytes())


def exchange(plan, key, receipt, attempt, body, status=200):
    require(
        receipt["url"] == attempt["url"] == plan["requests"][key]["url"]
        and receipt["key"] == attempt["key"] == key
        and all(receipt[k] == v for k, v in attempt.items())
        and receipt["redirects_followed"] == receipt["retries"] == 0,
        "request history changed",
    )
    require(
        receipt["status"] == status
        and not receipt["headers"].get("location")
        and len(body) == receipt["bytes"] <= plan["max_bytes"]
        and hashlib.sha256(body).hexdigest() == receipt["body"]["sha256"],
        "response status, size, or hash changed",
    )


def metadata_response(plan, key, receipt, body):
    item = plan["requests"][key]
    parsed = urlsplit(item["url"])
    taxonomy = key == "mphO-taxonomy"
    params = {"query": [item["query"]], "format": ["json"], "size": ["500"]}
    if not taxonomy:
        require(plan["fields"] == reference.FIELDS, "metadata fields changed")
        params["fields"] = [reference.FIELDS]
    require(
        parsed.scheme == "https"
        and parsed.netloc == "rest.uniprot.org"
        and parsed.path == ("/taxonomy/search" if taxonomy else "/uniprotkb/search")
        and not parsed.fragment
        and parse_qs(parsed.query) == params,
        "metadata request scope changed",
    )
    headers = receipt["headers"]
    require(
        receipt["status"] == 200
        and headers.get("x-uniprot-release") == plan["release"] == "2026_03"
        and not headers.get("link")
        and "application/json" in headers.get("content-type", ""),
        "release, format or pagination changed",
    )
    payload = json.loads(body)
    metadata_only(payload)
    entries = payload["results"]
    identity = "taxonId" if taxonomy else "primaryAccession"
    require(
        len(entries) == int(headers["x-total-results"]) <= 500
        and len({e[identity] for e in entries}) == len(entries),
        "incomplete or duplicate metadata",
    )
    return entries, payload.get("suggestions", [])


def identity_rows(words):
    """Read the fixed, visually inspected table using native PDF word geometry."""
    names = sorted(
        (w for w in words if 70 < w[0] < 100 and 145 < w[1] < 320 and w[4].startswith("Mph")),
        key=lambda w: w[1],
    )
    require(len(names) == 14 and len({w[4][:4] for w in names}) == 14, "identity-table rows changed")
    rows = {}
    for i, word in enumerate(names):
        start = (names[i - 1][1] + word[1]) / 2 if i else 145
        end = (word[1] + names[i + 1][1]) / 2 if i + 1 < len(names) else 319
        selected = sorted((w for w in words if start <= w[1] < end), key=lambda w: (w[1], w[0]))

        def cell(lo, hi, selected=selected):
            return " ".join(w[4] for w in selected if lo <= w[0] < hi)

        rows[word[4][:4].lower()] = {
            "previous_name": cell(110, 210) or None,
            "source_organism": cell(210, 338),
            "source_accession": cell(338, 408),
        }
    return rows


def check_identity_rows(rows, assessment):
    for key, (term, identifier, namespace) in EXPECTED.items():
        curated = assessment["terms"][term]
        require(
            curated["source_label"] == key
            and curated["source_accession"] == identifier
            and curated["accession_namespace"] == namespace,
            "source identity or namespace changed",
        )
        require(all(curated[k] == v for k, v in rows[key.lower()].items()), "table transcription mismatch")
    require(
        rows["mphf"]["previous_name"] == rows["mpho"]["previous_name"] == "MphE", "historical names changed"
    )


def cached_taxonomy(root, pin):
    wrapper = read(root, pin)
    headers = {k.lower(): v for k, v in wrapper["headers"].items()}
    body = wrapper["body"].encode()
    require(
        wrapper["status"] == 200
        and hashlib.sha256(body).hexdigest() == wrapper["sha256"]
        and headers.get("x-uniprot-release") == "2026_03"
        and not headers.get("link"),
        "native taxonomy cache changed",
    )
    url = urlsplit(wrapper["url"])
    require(
        url.scheme == "https" and url.netloc == "rest.uniprot.org" and url.path.startswith("/taxonomy/"),
        "wrong taxonomy origin",
    )
    payload = json.loads(body)
    entries = payload.get("results", [payload])
    if url.path.endswith("/search"):
        require(len(entries) == int(headers["x-total-results"]), "incomplete cached taxonomy")
    return entries


def bind_current(root, index, terms):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(len(expected) == 2939 and expected == actual, "current corpus changed")
    rows = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(by_key) == len(claims), "duplicate membership")
    seen = set()
    for row in rows:
        record = load_record(root / row["path"])
        require(
            record["identifier"] == row["identifier"]
            and record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"],
            "compound identity changed",
        )
        for i, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") not in terms:
                continue
            key = (record["identifier"], i)
            require(
                key in by_key
                and owner(claim) == "CARD"
                and memberships.checksum(claim) == by_key[key]["claim_sha256"],
                "source claim changed",
            )
            seen.add(key)
    require(seen == set(by_key) and len(rows) == 11 and len(claims) == 18, "cohort coverage changed")
    return rows, claims


def build(root):
    import pymupdf

    audit = json.loads((root / (PREFIX + "-audit-plan.json")).read_bytes())
    pins = audit["inputs"]
    docs = {k: read(root, p) for k, p in pins.items() if p["path"].endswith(".json")}
    plans = {k: docs[k] for k in ("primary_plan", "supplement_plan", "protein_plan", "taxonomy_plan")}
    for plan in plans.values():
        for p in plan["inputs"].values():
            reference.check_pin(root, p)
        require(
            plan["constraints"]["ncbi_requests"] == 0 and plan["constraints"]["issue_1040"] == "DEFERRED",
            "NCBI deferral changed",
        )
    primary_plan, protein_plan, taxonomy_plan = (
        plans[k] for k in ("primary_plan", "protein_plan", "taxonomy_plan")
    )
    public = {k: read(root, p) for k, p in primary_plan["inputs"].items() if p["path"].endswith(".json")}
    assessment = read(root, protein_plan["inputs"]["assessment"])
    require(
        taxonomy_plan["inputs"]["assessment"] == protein_plan["inputs"]["assessment"],
        "assessment pins disagree",
    )
    require(set(protein_plan["requests"]) == set(EXPECTED), "protein cohort changed")
    for review_key, key, plan_key in (
        ("primary_canary", "mph-primary", "primary_plan"),
        ("protein_canary", "mphL", "protein_plan"),
    ):
        review = docs[review_key]
        require(
            review["approved_remaining_request"] is True
            and review["plan_sha256"] == pins[plan_key]["sha256"]
            and review["receipt"] == pins[key + "_receipt"],
            "unreviewed canary",
        )
    bodies, responses, queries = {}, {}, {}
    for plan_key, plan in plans.items():
        for key in plan["requests"]:
            receipt = docs[key + "_receipt"]
            require(
                receipt["body"] == pins[key + "_body"] and receipt["plan_sha256"] == pins[plan_key]["sha256"],
                "receipt pin mismatch",
            )
            body = reference.check_pin(root, pins[key + "_body"]).read_bytes()
            exchange(plan, key, receipt, docs[key + "_attempt"], body, 403 if key == "aph-primary" else 200)
            bodies[key] = body
            if plan_key in {"protein_plan", "taxonomy_plan"}:
                entries, suggestions = metadata_response(plan, key, receipt, body)
                responses[key] = entries
                queries[key] = {
                    "query": plan["requests"][key]["query"],
                    "receipt": pins[key + "_receipt"],
                    "result_count": len(entries),
                    "suggestions_not_selected": suggestions,
                }
    primary = ET.fromstring(bodies["mph-primary"])
    ids = {e.attrib.get("pub-id-type"): e.text for e in primary.findall("./front/article-meta/article-id")}
    require(
        ids.get("pmid") == "29317655" and ids.get("doi") == "10.1038/s41467-017-02680-0",
        "primary identity changed",
    )
    sections = {s.findtext("title"): s for s in primary.findall(".//sec")}
    scope = "Substrate specificity correlates with genetic diversity"
    data_text = "".join(sections["Data availability"].itertext())
    require(
        "Supplementary Table" in data_text and "Protein accession" in data_text,
        "identifier-table pointer missing",
    )
    section_hashes = {
        name: hashlib.sha256(ET.tostring(sections[name])).hexdigest() for name in (scope, "Data availability")
    }
    extraction = read(root, protein_plan["inputs"]["extraction"])
    pdf = reference.check_pin(root, protein_plan["inputs"]["pdf"])
    require(
        extraction["pdf_sha256"] == reference.digest(pdf)
        and extraction["archive_sha256"] == hashlib.sha256(bodies["mph-supplement"]).hexdigest(),
        "PDF provenance changed",
    )
    with ZipFile(reference.check_pin(root, pins["mph-supplement_body"])) as archive:
        require(archive.read(extraction["selected_member"]) == pdf.read_bytes(), "archive member mismatch")
    (render,) = extraction["selected_pages"]
    require(
        render["page_one_based"] == 9
        and render["render_sha256"] == protein_plan["inputs"]["visual_review"]["sha256"]
        and assessment["supplement_review"]["visually_reviewed"] is True,
        "visual review binding changed",
    )
    with pymupdf.open(pdf) as document:
        table = identity_rows(document[8].get_text("words"))
    check_identity_rows(table, assessment)
    native = {key: cached_taxonomy(root, p) for key, p in taxonomy_plan["reused_native_wrappers"].items()}
    require(len(responses["mphO-taxonomy"]) == 1, "unreviewed taxonomy results")
    native["mphO"] = responses["mphO-taxonomy"]
    mapped = {"mphL": "bacillus_cereus", "mphM": "bacillus_cereus", "mphI": "lc231", "mphO": "mphO"}
    terms = {}
    for key, (term, _, _) in EXPECTED.items():
        paper = assessment["terms"][term]
        require(
            protein_plan["requests"][key]["query"] == paper["query"] and not responses[key],
            "identifier result requires reassessment",
        )
        require(
            "PMID:29317655" in public["definitions"]["terms"][term]["definition_citation_ids"],
            "own definition citation changed",
        )
        terms[term] = {
            "source_identity": paper,
            "reference_candidates": [],
            "query_status": "NO_ENTRIES_IN_BOUNDED_QUERY_NOT_BIOLOGICAL_ABSENCE",
            "source_taxonomy_context": species_context(native[mapped[key]], paper["source_organism"])
            if key in mapped
            else None,
            "experimental_allele_assignment": None,
            "experimental_strain_taxon_assignment": None,
            "whole_record_primary_review": "OPEN",
        }
    aph = assessment["aph_primary"]
    require(
        aph["http_status"] == 403 and not aph["selected_as_aphA15"] and not aph["retry_or_alternate_route"],
        "access hold changed",
    )
    prior = public["prior_cohort"]
    (page,) = prior["citation_queries"]["11257042"]["pages"]
    require(page["cache"] == pins["aph_citation_body"], "prior citation body mismatch")
    receipt = read(root, page["receipt"])
    headers = {k.lower(): v for k, v in receipt["headers"].items()}
    candidate = read(root, pins["aph_citation_body"])["results"]
    require(
        receipt["status"] == 200
        and receipt["query"] == "lit_pubmed:11257042"
        and headers["x-uniprot-release"] == "2026_03"
        and not headers.get("link")
        and len(candidate) == int(headers["x-total-results"]) == 7,
        "prior citation response changed",
    )
    candidates = [e for e in candidate if e["primaryAccession"] == "Q9AF71"]
    require(len(candidates) == 1, "aph candidate changed")
    (gene,) = candidates[0]["genes"]
    require(
        gene["geneName"]["value"] == "aph"
        and "apaA15" in {n["value"] for n in gene["synonyms"]}
        and candidates[0]["organism"]["taxonId"] == 32002,
        "aph spelling context changed",
    )
    terms["ARO:3004675"] = {
        "source_identity": assessment["terms"]["ARO:3004675"],
        "reference_candidates": [],
        "status": "PRIMARY_HTTP_403_HOLD_UNRESOLVED_NAME",
        "unselected_candidate": aph["candidate"],
        "candidate_taxonomy_only": species_context(native["aph_candidate"], "Achromobacter denitrificans"),
        "experimental_allele_assignment": None,
        "experimental_strain_taxon_assignment": None,
        "whole_record_primary_review": "OPEN",
    }
    rows, claims = bind_current(root, public["current_index"], set(terms))
    for term, row in terms.items():
        require(
            not public["current_index"]["terms"][term]["reference_links"]
            and prior["terms"][term]["reference_candidates"] == [],
            "prior context changed",
        )
        row["record_memberships"] = public["current_index"]["terms"][term]["record_memberships"]
    return {
        "date": "2026-10-15",
        "scope": assessment["scope"],
        "inputs": pins,
        "assessment": protein_plan["inputs"]["assessment"],
        "records": rows,
        "claims": claims,
        "terms": terms,
        "queries": queries,
        "primary_section_hashes": section_hashes,
        "identity_table_rows": {k: table[k.lower()] for k in EXPECTED},
        "primary_access_hold": aph,
        "constraints": assessment["constraints"],
        "counts": {
            "current_corpus_hashes_checked": 2939,
            "complete_records_loaded": 11,
            "card_claims": 18,
            "terms": 6,
            "explicit_source_identifiers": 5,
            "mph_source_taxonomy_contexts": 4,
            "distinct_mph_taxonomy_nodes": 3,
            "new_selected_uniprot_proteins": 0,
            "primary_http_403_holds": 1,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    path = args.root / (PREFIX + ".json")
    if args.check:
        require(path.read_bytes() == encoded, "dossier drift")
    else:
        with path.open("xb") as stream:
            stream.write(encoded)
    print(json.dumps(result["counts"], sort_keys=True))


if __name__ == "__main__":
    main()

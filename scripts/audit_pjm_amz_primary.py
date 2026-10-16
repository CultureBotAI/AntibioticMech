"""Replay two primary-identifier investigations without assigning experimental alleles."""

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import audit_card_reference_memberships as memberships
import audit_topoisomerase_references as reference
from audit_bla_primary_identifiers import read_json, require, taxonomy_context, validate_response
from audit_curator_resistance_fields import owner

from antibioticmech.activity_collections import load_record

PREFIX = "research/2026-10-15-pjm-amz-primary"
PLAN = Path(PREFIX + "-audit-plan.json")
OUTPUT = Path(PREFIX + ".json")
TERMS = {"amz": "ARO:3007694", "pjm": "ARO:3007374"}
QUERIES = {
    "amz": "xref:embl-OQ948417",
    "pjm": (
        "(gene_exact:blaPJM-1 OR gene_exact:PJM-1 OR gene_exact:PJM) "
        'AND organism_name:"Pseudoxanthomonas japonensis"'
    ),
}


def plain(element):
    require(element is not None, "missing primary element")
    return " ".join("".join(element.itertext()).split())


def amz_scope(body):
    article = ET.fromstring(body)
    identifiers = {e.get("pub-id-type"): e.text for e in article.findall("./front/article-meta/article-id")}
    require(
        identifiers.get("pmid") == "37808287" and identifiers.get("doi") == "10.3389/fmicb.2023.1252427",
        "primary citation mismatch",
    )
    paths = {
        "accessions": ".//sec[@id='S2.SS6']",
        "source_identity": ".//sec[@id='S3.SS1']",
        "functional_scope": ".//sec[@id='S3.SS2']",
        "assay_methods": ".//sec[@id='S2.SS2']",
        "abstract": "./front/article-meta/abstract",
        "kinetics": ".//table-wrap[@id='T5']",
    }
    nodes = {key: article.find(path) for key, path in paths.items()}
    texts = {key: plain(node) for key, node in nodes.items()}
    require(
        all(v in texts["accessions"] for v in ("CP123364", "OQ948417", "Y3", "respectively")),
        "chromosome/gene source identifiers changed",
    )
    require(
        texts["accessions"].index("chromosome") < texts["accessions"].index("gene")
        and texts["accessions"].index("CP123364") < texts["accessions"].index("OQ948417"),
        "chromosome/gene identifier order reversed",
    )
    require(
        "GCA_902859725.1" in texts["source_identity"] and "LMG 26685" in texts["source_identity"],
        "comparison strain context changed",
    )
    require(
        "agar dilution" in texts["abstract"]
        and "broth dilution" in texts["assay_methods"]
        and "agar plates" in texts["assay_methods"],
        "assay-wording discrepancy changed",
    )
    rows = [[plain(cell) for cell in row.findall("td")] for row in nodes["kinetics"].findall(".//tbody/tr")]
    ampicillin = [row for row in rows if row and row[0] == "Ampicillin"]
    require(
        len(ampicillin) == 1
        and len(ampicillin[0]) == 4
        and all(v.startswith("NH") for v in ampicillin[0][1:])
        and "not detectable" in texts["functional_scope"],
        "ampicillin biochemical scope changed",
    )
    return {
        "source_identifiers": {"chromosome": "CP123364", "gene_nucleotide": "OQ948417"},
        "comparison_assembly_not_assigned_to_Y3": "GCA_902859725.1",
        "ampicillin_cellular_and_biochemical_results_discordant": True,
        "assay_method_normalization": "UNRESOLVED_INCONSISTENT_PRIMARY_WORDING",
        "selected_element_pins": {
            key: {"xpath": paths[key], "element_sha256": hashlib.sha256(ET.tostring(node)).hexdigest()}
            for key, node in nodes.items()
        },
        "whole_paper_reviewed": False,
    }


def bind_current(root, index):
    expected = {r["path"]: r["record_sha256"] for r in index["records"]}
    actual = {
        str(p.relative_to(root)): reference.digest(p) for p in (root / "data/antibiotics").rglob("*.yaml")
    }
    require(actual == expected and len(actual) == 2939, "current corpus changed")
    terms = set(TERMS.values())
    rows = [r for r in index["records"] if terms.intersection(r["card_terms"])]
    claims = [c for c in index["claims"] if c["aro_id"] in terms]
    by_key = {(c["record_identifier"], c["resistance_index"]): c for c in claims}
    require(len(by_key) == len(claims) == 10 and len(rows) == 7, "cohort coverage changed")
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
            require(key in by_key and owner(claim) == "CARD", "source ownership changed")
            require(memberships.checksum(claim) == by_key[key]["claim_sha256"], "source claim changed")
            seen.add(key)
    require(seen == set(by_key), "unread source memberships")
    return rows, claims


def primary_receipt(plan, key, receipt, attempt, body, expected_status):
    require(
        all(receipt[k] == v for k, v in attempt.items())
        and receipt["url"] == plan["requests"][key]["url"]
        and receipt["key"] == key
        and receipt["status"] == expected_status
        and receipt["retries"] == receipt["redirects_followed"] == 0
        and not receipt["headers"].get("location")
        and len(body) == receipt["bytes"] <= plan["max_bytes"]
        and hashlib.sha256(body).hexdigest() == receipt["body"]["sha256"],
        "primary receipt changed",
    )


def build(root):
    audit = json.loads((root / PLAN).read_bytes())
    inputs = audit["inputs"]
    values = {
        key: read_json(root, binding) for key, binding in inputs.items() if binding["path"].endswith(".json")
    }
    for binding in inputs.values():
        reference.check_pin(root, binding)
    primary, metadata = values["primary_plan"], values["metadata_plan"]
    public_pins = primary["inputs"]
    public = {key: read_json(root, p) for key, p in public_pins.items() if p["path"].endswith(".json")}
    for binding in public_pins.values():
        reference.check_pin(root, binding)
    for binding in metadata["inputs"].values():
        reference.check_pin(root, binding)
    require(metadata["inputs"]["assessment"] == inputs["assessment"], "assessment pin mismatch")
    papers = values["assessment"]["papers"]
    require(set(papers) == set(TERMS), "paper cohort changed")
    rows, claims = bind_current(root, public["current_index"])
    for kind, plan in (("primary", primary), ("metadata", metadata)):
        require(plan["constraints"]["ncbi_requests"] == 0, "source deferral changed")
        require(plan["constraints"]["issue_1040"] == "DEFERRED", "issue deferral changed")
        review = values[kind + "_canary"]
        require(
            review["plan_sha256"] == inputs[kind + "_plan"]["sha256"]
            and review["approved_remaining_request"] is True
            and review["receipt"] == inputs[plan["canary"] + "_receipt"],
            "unreviewed canary",
        )
    query_views, responses = {}, {}
    for key in ("amz-primary", "pjm-primary", "amz-protein", "amz-taxonomy", "pjm-protein", "pjm-taxonomy"):
        receipt, attempt = values[key + "_receipt"], values[key + "_attempt"]
        plan_key = "primary_plan" if key.endswith("primary") else "metadata_plan"
        plan = values[plan_key]
        require(
            receipt["plan_sha256"] == inputs[plan_key]["sha256"] and receipt["body"] == inputs[key + "_body"],
            "response pin mismatch",
        )
        body = reference.check_pin(root, receipt["body"]).read_bytes()
        if key.endswith("primary"):
            primary_receipt(plan, key, receipt, attempt, body, 403 if key == "pjm-primary" else 200)
            responses[key] = amz_scope(body) if key == "amz-primary" else {"status": "HTTP_403_HOLD"}
        else:
            responses[key], suggestions = validate_response(
                plan, key, receipt, attempt, body, taxonomy=key.endswith("taxonomy")
            )
            query_views[key] = {
                "query": plan["requests"][key]["query"],
                "complete_result_count": len(responses[key]),
                "suggestions_not_selected": suggestions,
                "release": receipt["headers"]["x-uniprot-release"],
            }
        query_views.setdefault(key, {})
        query_views[key].update(
            {
                "url": receipt["url"],
                "receipt": inputs[key + "_receipt"],
                "body": receipt["body"],
                "retrieved_at": receipt["retrieved_at"],
                "http_status": receipt["status"],
            }
        )
    terms = {}
    for key, term in TERMS.items():
        paper = papers[key]
        require(paper["aro_id"] == term and paper["query"] == QUERIES[key], "source term/query changed")
        require(metadata["requests"][key + "-protein"]["query"] == QUERIES[key], "query scope changed")
        require(
            metadata["requests"][key + "-taxonomy"]["query"]
            == '"' + paper["source_organism"] + '" AND rank:species',
            "taxonomy query changed",
        )
        require(
            public["definitions"]["terms"][term]["definition_citation_ids"] == ["PMID:" + paper["pmid"]],
            "own citation changed",
        )
        require(
            public["prior_citation_screen"]["terms"][term]["citation_pool_size"] == 0, "prior query changed"
        )
        require(not responses[key + "-protein"], "new candidate needs scientific review")
        taxonomy = taxonomy_context(responses[key + "-taxonomy"], paper["source_organism"])
        taxonomy["native_other_names_not_strain_mappings"] = responses[key + "-taxonomy"][0].get(
            "otherNames", []
        )
        terms[term] = {
            "paper": paper,
            "primary_review": responses[key + "-primary"],
            "taxonomy_context": taxonomy,
            "record_memberships": public["current_index"]["terms"][term]["record_memberships"],
            "reference_accessions": [],
            "experimental_allele_assignment": None,
            "experimental_protein_assignment": None,
            "experimental_genome_assignment": None,
            "biological_absence_inferred": False,
            "whole_record_primary_review": "OPEN",
        }
    require(values["pjm-primary_error"]["retry_performed"] is False, "access hold violated")
    require(values["pjm-primary_error"]["alternate_route_performed"] is False, "access hold violated")
    cache = root / "reports/resistance-grounding-2026-10-15-pjm-amz-primary"
    require(not list(cache.glob("pjm-figure1-*")), "figure fetched after access denial")
    return {
        "date": "2026-10-15",
        "inputs": {**public_pins, **inputs},
        "summary": {
            "current_record_hashes_verified": 2939,
            "complete_target_records_read": len(rows),
            "source_claims_bound": len(claims),
            "terms_investigated": 2,
            "species_names_grounded": 2,
            "new_selected_proteins": 0,
            "native_primary_access_holds": 1,
            "whole_record_primary_signoffs": 0,
        },
        "records": rows,
        "claims": claims,
        "terms": terms,
        "requests": query_views,
        "constraints": {
            **values["assessment"]["constraints"],
            "full_investigation_complete": False,
            "authoritative_qc_rerun": False,
        },
        "attribution": (
            "CARD/ARO: McMaster University, CC BY 4.0. UniProt metadata: UniProt Consortium. "
            "Primary identifiers and scope: Yamada et al. 2022 and Zhang et al. 2023; "
            "only the stated sections were inspected."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build(args.root)
    if args.write:
        with (args.root / OUTPUT).open("x") as stream:
            json.dump(result, stream, indent=2, sort_keys=True)
            stream.write("\n")
    else:
        require(result == json.loads((args.root / OUTPUT).read_bytes()), "saved dossier differs")
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

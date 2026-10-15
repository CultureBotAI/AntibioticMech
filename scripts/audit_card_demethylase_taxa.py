"""Ground the full CARD CYP51/ERG11 source-name cohort without assigning alleles."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import audit_card_reference_lineages as lineages
import audit_fungamr_cohort as native
import audit_topoisomerase_references as reference
from audit_valinomycin_abcb1 import planned_source

from antibioticmech.activity_collections import load_record

CACHE = Path("reports/resistance-grounding-2026-10-14-card-demethylase")
OUTPUT = Path("research/2026-10-14-card-demethylase-taxa.json")
COHORT_SHA = "f4698c0d534e74418f7ca3bd710a4ba7314ca55112c8c149a89f1dee55678f71"
GENE = re.compile(r"\b(?:CYP51[A-C]?|ERG11)\b", re.I)
LABEL = re.compile(r"(.+?) ((?i:CYP51[A-C]?|ERG11)) (.+)")


def source_identity(label):
    match = LABEL.fullmatch(label)
    if not match:
        raise ValueError("unreviewed source label syntax")
    name, gene, wording = match.groups()
    if name in {"Candida spp.", "Aspergillus spp."}:
        kind = "GENUS_GROUP"
    elif name == "Blumeria graminis f. sp. hordei":
        kind = "QUALIFIED_NAME"
    elif re.fullmatch(r"[A-Z][a-z]+ [a-z]+(?:-[a-z]+)*", name):
        kind = "BINOMIAL"
    else:
        raise ValueError("unreviewed organism-name syntax")
    return {
        "source_organism_name": name,
        "source_gene_label": gene,
        "source_name_kind": kind,
        "source_claim_wording": wording,
    }


def query_url(name, kind):
    if kind not in {"BINOMIAL", "QUALIFIED_NAME"} or '"' in name:
        raise ValueError("broad or malformed source name cannot become an exact-name query")
    query = f'"{name}"' + (" AND rank:species" if kind == "BINOMIAL" else "")
    return "https://rest.uniprot.org/taxonomy/search?" + urlencode(
        {
            "query": query,
            "format": "json",
            "size": 500,
        }
    )


def resolve_name(payload, name, kind):
    if kind not in {"BINOMIAL", "QUALIFIED_NAME"}:
        raise ValueError("a genus group is not an exact organism")
    entries = payload.get("results", [payload])
    if not isinstance(entries, list):
        raise ValueError("taxonomy result is not a list")
    candidates, accepted, seen = [], [], set()
    for entry in entries:
        identity = lineages.identity(entry)
        taxid = identity["taxonId"]
        if taxid in seen or type(entry.get("active")) is not bool:
            raise ValueError("duplicate or invalid taxonomy identity")
        seen.add(taxid)
        for field in ("synonyms", "otherNames"):
            values = entry.get(field, [])
            if not isinstance(values, list) or any(not isinstance(v, str) or not v for v in values):
                raise ValueError("invalid taxonomy name field")
        fields = ["scientificName"] if identity["scientificName"] == name else []
        if name in entry.get("synonyms", []):
            fields.append("synonyms")
        eligible_rank = (
            identity["rank"] == "species"
            if kind == "BINOMIAL"
            else identity["rank"]
            in {"species", "subspecies", "varietas", "forma", "forma specialis", "no rank", "strain"}
        )
        candidate = {
            "taxon_id": f"NCBITaxon:{taxid}",
            "scientific_name": identity["scientificName"],
            "rank": identity["rank"],
            "active": entry["active"],
            "matching_fields": fields,
            "other_name_match_only": not fields and name in entry.get("otherNames", []),
            "accepted_name_and_rank": bool(fields and eligible_rank and entry["active"]),
        }
        candidates.append(candidate)
        if candidate["accepted_name_and_rank"]:
            nodes, species = lineages.lineage(entry)
            if not any(n["taxonId"] == 4751 and n["rank"] == "kingdom" for n in nodes):
                raise ValueError("source-name candidate is outside fungal lineage")
            accepted.append(
                {
                    **candidate,
                    "lineage": nodes,
                    "species_ancestor": species,
                    "experimental_subject_assignment": False,
                }
            )
    return {
        "status": "EXACT_NATIVE_NAME_REFERENCE"
        if len(accepted) == 1
        else ("AMBIGUOUS_EXACT_NATIVE_NAMES" if accepted else "NO_EXACT_ACTIVE_NAME_AT_SUPPORTED_RANK"),
        "source_name": name,
        "source_name_kind": kind,
        "selected_taxon": accepted[0] if len(accepted) == 1 else None,
        "candidates": sorted(candidates, key=lambda c: int(c["taxon_id"].split(":")[1])),
        "result_count": len(entries),
        "exact_match_count": len(accepted),
        "experimental_subject_assignment": False,
        "protein_or_allele_assignment": None,
        "unresolved_name_is_biological_absence": False,
    }


def read_new(root, directory, key, plan):
    directory = root / directory
    item = plan["requests"][key]
    url = query_url(item["name"], item["kind"])
    source = planned_source(root, directory, key, "taxonomy-plan.json", url)
    payload, provenance = native.read_source(root, {**source, "url": url})
    return resolve_name(payload, item["name"], item["kind"]), provenance


def build(root, directory=CACHE):
    directory = root / directory
    cohort_path = directory / "cohort.json"
    if reference.digest(cohort_path) != COHORT_SHA:
        raise ValueError("frozen full-cohort scope changed")
    cohort = json.loads(cohort_path.read_bytes())
    for key in (
        "index",
        "census",
        "source_inventory",
        "source_queue",
        "protected",
        "taxonomy_cache_inventory",
        "prior_checkpoint",
    ):
        reference.check_pin(root, cohort[key])
    index = json.loads((root / cohort["index"]["path"]).read_bytes())
    with (root / cohort["source_inventory"]["path"]).open() as stream:
        source_rows = list(csv.DictReader(stream, delimiter="\t"))
    labels = {}
    for row in source_rows:
        tid, label = row["determinant_id"], row["determinant_name"]
        if tid in labels and labels[tid] != label:
            raise ValueError("conflicting source term labels")
        labels[tid] = label
    expected = {tid for tid in index["terms"] if GENE.search(labels[tid])}
    if set(cohort["terms"]) != expected or len(expected) != 137:
        raise ValueError("CYP51/ERG11 source cohort is incomplete")
    for tid, row in cohort["terms"].items():
        label = labels[tid]
        identity = source_identity(label)
        if (
            any(row[k] != v for k, v in identity.items())
            or row["source_label"] != label
            or row["source_label_sha256"] != hashlib.sha256(label.encode()).hexdigest()
            or row["record_memberships"] != index["terms"][tid]["record_memberships"]
            or index["terms"][tid]["links"]
        ):
            raise ValueError("source gene, organism, claim or index scope changed")
    with (root / cohort["census"]["path"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if (
        len(census) != 2939
        or len({r["identifier"] for r in census}) != 2939
        or {r["path"] for r in census}
        != {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
        or any(reference.digest(root / r["path"]) != r["record_sha256"] for r in census)
    ):
        raise ValueError("current corpus membership or bytes changed")
    claims = []
    for item in cohort["records"]:
        record = load_record(root / item["path"])
        snapshot = directory / (item["identifier"].replace(":", "-") + "-before.yaml")
        if (
            record != load_record(snapshot)
            or reference.digest(snapshot) != item["record_sha256"]
            or record["identifier"] != item["identifier"]
            or record["chemical_structure"]["standard_inchi_key"] != item["standard_inchi_key"]
        ):
            raise ValueError("selected record identity changed")
        for position, claim in enumerate(record.get("resistance_mechanisms", [])):
            if claim.get("aro_id") in expected:
                if claim["label"] != labels[claim["aro_id"]]:
                    raise ValueError("current source assertion differs from source label")
                claims.append(
                    {
                        "record_identifier": record["identifier"],
                        "position": position,
                        "aro_id": claim["aro_id"],
                        "claim_sha256": hashlib.sha256(
                            json.dumps(claim, sort_keys=True, ensure_ascii=True).encode()
                        ).hexdigest(),
                    }
                )
    if claims != cohort["claims"] or len(claims) != 141 or len(cohort["records"]) != 31:
        raise ValueError("source assertion membership, order or content changed")
    plan = json.loads((directory / "taxonomy-plan.json").read_bytes())
    if plan["cohort"] != reference.pin(root, cohort_path):
        raise ValueError("taxonomy plan cohort binding changed")
    review = json.loads((directory / "taxonomy-canary-review.json").read_bytes())
    key = plan["canary_request"]
    if (
        review["plan"] != reference.pin(root, directory / "taxonomy-plan.json")
        or review["body"] != reference.pin(root, directory / f"{key}-response.bin")
        or review["manually_inspected"] is not True
    ):
        raise ValueError("canary evidence binding changed")
    names, sources = {}, {}
    expected_requests = set()
    for name, item in cohort["names"].items():
        kind = item["kind"]
        if kind == "GENUS_GROUP":
            if item["selected_source"] or item["request_key"]:
                raise ValueError("genus group was assigned an exact organism")
            names[name] = {
                "status": "GENUS_GROUP_NOT_ONE_ORGANISM",
                "source_name": name,
                "source_name_kind": kind,
                "selected_taxon": None,
                "candidates": [],
                "experimental_subject_assignment": False,
                "protein_or_allele_assignment": None,
            }
            continue
        if item["selected_source"]:
            source = item["selected_source"]
            if not urlsplit(source["url"]).path.startswith("/taxonomy/"):
                raise ValueError("reused source is not taxonomy")
            payload, sources[name] = native.read_source(root, source)
            names[name] = resolve_name(payload, name, kind)
            if names[name]["status"] != "EXACT_NATIVE_NAME_REFERENCE" or item["request_key"]:
                raise ValueError("reused positive name match changed")
            names[name]["evidence_basis"] = "REUSED_POSITIVE_NATIVE_NAME_MATCH_NOT_NEW_EXHAUSTIVE_SEARCH"
        else:
            key = item["request_key"]
            expected_requests.add(key)
            if plan["requests"][key]["name"] != name or plan["requests"][key]["kind"] != kind:
                raise ValueError("planned source name changed")
            names[name], sources[name] = read_new(root, directory, key, plan)
            names[name]["evidence_basis"] = "COMPLETE_PLANNED_NATIVE_NAME_QUERY"
    if set(plan["requests"]) != expected_requests or len(expected_requests) != 18:
        raise ValueError("new request coverage changed")
    terms = {}
    pairs = {}
    for tid, row in sorted(cohort["terms"].items()):
        name, gene = row["source_organism_name"], row["source_gene_label"]
        resolved = names[name]
        selected = resolved["selected_taxon"]
        terms[tid] = {
            **row,
            "name_status": resolved["status"],
            "named_reference_taxon_id": selected["taxon_id"] if selected else None,
            "named_reference_taxon_rank": selected["rank"] if selected else None,
            "experimental_subject_assignment": False,
            "exact_allele_assignment": False,
            "protein_reference_assignment": None,
            "primary_review_status": "OPEN",
        }
        pair = json.dumps([name, gene.casefold()], separators=(",", ":"))
        context = pairs.setdefault(
            pair,
            {
                "source_name": name,
                "casefold_gene_query_key": gene.casefold(),
                "source_gene_labels": [],
                "terms": [],
                "named_reference_taxon_id": terms[tid]["named_reference_taxon_id"],
                "named_reference_taxon_rank": terms[tid]["named_reference_taxon_rank"],
                "name_status": resolved["status"],
                "protein_query_status": "PENDING_NOT_PERFORMED_BY_TAXONOMY_AUDIT",
                "casefold_key_is_gene_equivalence_assertion": False,
            },
        )
        context["terms"].append(tid)
        if gene not in context["source_gene_labels"]:
            context["source_gene_labels"].append(gene)
    return {
        "scope": "ALL_CARD_CYP51_ERG11_SOURCE_NAME_TAXONOMY_NOT_EXPERIMENTAL_RESISTANCE_GROUNDING",
        "date": "2026-10-14",
        "uniprot_release": "2026_03",
        "inputs": {
            "cohort": reference.pin(root, cohort_path),
            "index": cohort["index"],
            "census": cohort["census"],
            "source_inventory": cohort["source_inventory"],
            "taxonomy_cache_inventory": cohort["taxonomy_cache_inventory"],
            "taxonomy_plan": reference.pin(root, directory / "taxonomy-plan.json"),
            "canary_review": reference.pin(root, directory / "taxonomy-canary-review.json"),
            "sources": sources,
        },
        "terms": terms,
        "names": names,
        "gene_name_contexts": dict(sorted(pairs.items())),
        "claims": claims,
        "records": cohort["records"],
        "summary": {
            "corpus_records_checked": 2939,
            "cohort_terms": len(terms),
            "cohort_records": 31,
            "assertion_memberships": len(claims),
            "source_names": len(names),
            "source_gene_name_contexts": len(pairs),
            "new_name_queries": 18,
            "reused_positive_names": 17,
            "name_status_counts": dict(Counter(n["status"] for n in names.values())),
            "term_name_status_counts": dict(Counter(t["name_status"] for t in terms.values())),
            "distinct_selected_taxa": len(
                {n["selected_taxon"]["taxon_id"] for n in names.values() if n["selected_taxon"]}
            ),
            "biological_records_changed": 0,
            "new_protein_assignments": 0,
            "experimental_assignments": 0,
            "whole_record_primary_signoffs": 0,
        },
        "limits": [
            "Taxonomy verifies source-name reference context, "
            "not experimental isolates or species-wide resistance.",
            "Source gene spelling, paralog suffixes and qualified organism names are retained; "
            "no aliases are invented.",
            "Case-folded query keys consolidate spelling case only, not CYP51/ERG11 or paralog equivalence.",
            "Broad spp. labels do not identify one species. An unresolved name is not biological absence.",
            "Only native scientificName or explicit synonyms match; "
            "otherNames and substrings do not resolve.",
            "Protein reference, exact allele, experimental strain/genome "
            "and compound-specific primary review remain open.",
            "Taxonomy completion does not revalidate inherited resistance assertions "
            "or create new phenotype claims.",
        ],
        "constraints": {
            "ncbi_requests": 0,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "primary_access_holds_preserved": True,
            "new_primary_requests": 0,
            "source_adoptions": 0,
            "outreach": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "attribution": "CARD curation team, ARO CC BY 4.0; UniProt Consortium, release 2026_03, CC BY 4.0.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check:
        if OUTPUT.read_text() != encoded:
            raise ValueError("saved taxonomy cohort differs from native replay")
    else:
        OUTPUT.write_text(encoded)
    print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

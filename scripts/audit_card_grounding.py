"""Audit existing CARD assertions against explicit UniProt reference links.

This does not identify experimental alleles or mutate antibiotic records.
Requests are offline by default and use the UniProt-only evidence cache.
"""

import argparse
import copy
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import audit_resistance_grounding as common
from requests.utils import parse_header_links
from seed_from_sources import is_card_sourced

FIELDS = (
    "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
    "xref_card,lit_pubmed_id,sequence_version,version"
)
PARAMS = {
    "query": "database:card", "format": "json", "size": "500",
    "sort": "accession asc", "fields": FIELDS,
}
SOURCE = "data/raw/aro_resistance_edges.tsv"
CONTEXT_SCOPE = "DATABASE_CITATION_CONTEXT_ONLY_NOT_EXPERIMENTAL_SUBJECT_OR_ALLELE_GROUNDING"
ARCHIVE_SCOPE = "DATABASE_ARCHIVE_IDENTITY_ONLY_NOT_EXPERIMENTAL_ALLELE_GROUNDING"


def current_corpus(root):
    path = common.OUT / "corpus.json"
    corpus = json.loads(path.read_text())
    records = corpus["records"]
    current = {str(p.relative_to(root)) for p in (root / "data/antibiotics").rglob("*.yaml")}
    if current != {r["path"] for r in records} or len(records) != len(current):
        raise ValueError("corpus membership drift; rerun inventory")
    if len({r["identifier"] for r in records}) != len(records):
        raise ValueError("duplicate corpus identifiers")
    for record in records:
        if common.digest((root / record["path"]).read_bytes()) != record["sha256"]:
            raise ValueError("corpus snapshot drift; rerun inventory")
    return records


def claims_from(records):
    return [(record, item) for record in records for item in record["resistance_mechanisms"]
            if is_card_sourced(item)]


def metadata(response):
    return {key: value for key, value in response.items() if key != "body"}


def next_page(header, expected):
    links = [link["url"] for link in parse_header_links(header) if link.get("rel") == "next"]
    if not links:
        return None
    if len(links) != 1:
        raise ValueError("ambiguous pagination")
    parsed = urlparse(links[0])
    if (parsed.scheme != "https" or parsed.netloc != "rest.uniprot.org"
            or parsed.path != "/uniprotkb/search" or parsed.fragment):
        raise ValueError("pagination left the approved UniProt endpoint")
    query = parse_qs(parsed.query, keep_blank_values=True, strict_parsing=True)
    if any(len(values) != 1 for values in query.values()):
        raise ValueError("duplicate pagination parameters")
    params = {key: values[0] for key, values in query.items()}
    if (set(params) != set(expected) | {"cursor"} or not params["cursor"]
            or any(params.get(key) != value for key, value in expected.items())):
        raise ValueError("pagination query drift")
    return params


def search_proteins():
    params = dict(PARAMS)
    seen_pages, entries, requests = set(), {}, []
    total, release = None, None
    while params is not None:
        page_key = json.dumps(params, sort_keys=True)
        if page_key in seen_pages:
            raise ValueError("pagination cycle")
        seen_pages.add(page_key)
        response = common.fetch("uniprotkb/search", params)
        if response["status"] != 200:
            raise ValueError(f"UniProt search returned HTTP {response['status']}")
        headers = {key.lower(): value for key, value in response["headers"].items()}
        page_total = int(headers["x-total-results"])
        page_release = headers["x-uniprot-release"]
        if total is None:
            total, release = page_total, page_release
        if page_total != total or page_release != release:
            raise ValueError("UniProt count or release changed during pagination")
        if not 0 < total <= 10000:
            raise ValueError("unexpected cohort size; review a new canary")
        results = json.loads(response["body"])["results"]
        if not results:
            raise ValueError("empty page before completing the cohort")
        for entry in results:
            accession = entry["primaryAccession"]
            if accession in entries:
                raise ValueError("duplicate protein across pages")
            if not any(x["database"] == "CARD" for x in entry.get("uniProtKBCrossReferences", [])):
                raise ValueError("search result lacks an explicit CARD cross-reference")
            if "sequence" in entry:
                raise ValueError("metadata-only query unexpectedly returned a sequence")
            entries[accession] = entry
        requests.append(metadata(response))
        params = next_page(headers.get("link", ""), PARAMS)
        if len(entries) > total or (params is not None and len(entries) >= total):
            raise ValueError("pagination exceeds declared total")
        print(f"CARD-linked protein metadata: {len(entries)}/{total}", flush=True)
    if len(entries) != total:
        raise ValueError("incomplete UniProt cohort")
    return {"entries": entries, "requests": requests, "release": release,
            "total": total, "query": PARAMS}


def proteins(root):
    current_corpus(root)
    before = common.digest((common.OUT / "corpus.json").read_bytes())
    source_hash = common.digest((root / SOURCE).read_bytes())
    result = search_proteins()
    current_corpus(root)
    if before != common.digest((common.OUT / "corpus.json").read_bytes()):
        raise ValueError("census changed during retrieval")
    if source_hash != common.digest((root / SOURCE).read_bytes()):
        raise ValueError("source changed during retrieval")
    result.update(corpus_sha256=before, source_inventory_sha256=source_hash)
    common.write("card-proteins.json", result)


def snapshot(root):
    records = current_corpus(root)
    path = common.OUT / "card-proteins.json"
    payload = path.read_bytes()
    proteins = json.loads(payload)
    proteins["_snapshot_sha256"] = common.digest(payload)
    if proteins["source_inventory_sha256"] != common.digest((root / SOURCE).read_bytes()):
        raise ValueError("CARD source inventory drift")
    if proteins["corpus_sha256"] != common.digest((common.OUT / "corpus.json").read_bytes()):
        raise ValueError("census drift; rerun the CARD protein stage")
    return records, proteins


def reference_index(entries, determinant_ids):
    result = defaultdict(list)
    for accession, entry in sorted(entries.items()):
        if accession != entry["primaryAccession"]:
            raise ValueError("protein accession/key mismatch")
        seen = set()
        for crossref in entry.get("uniProtKBCrossReferences", []):
            aro = crossref["id"]
            if crossref["database"] != "CARD" or aro not in determinant_ids:
                continue
            if aro in seen:
                raise ValueError("duplicate CARD identifier within a protein entry")
            seen.add(aro)
            result[aro].append((entry, crossref))
    return result


def taxonomy(root):
    records, proteins = snapshot(root)
    identifiers = {claim["aro_id"] for _, claim in claims_from(records)}
    index = reference_index(proteins["entries"], identifiers)
    taxids = sorted({str(entry["organism"]["taxonId"])
                     for candidates in index.values() for entry, _ in candidates}, key=int)
    taxa, requests = {}, []
    for index, taxid in enumerate(taxids, 1):
        response = common.fetch("taxonomy/" + taxid)
        if response["status"] not in (200, 301, 302, 303, 404, 410):
            raise ValueError(f"transient/unexpected taxonomy HTTP status: {response['status']}")
        taxon = (json.loads(response["body"]) if response["status"] == 200
                 else {"unresolved_status": response["status"]})
        if response["status"] == 200 and str(taxon["taxonId"]) != taxid:
            raise ValueError("taxonomy response identifies another taxon")
        taxa[taxid] = taxon
        requests.append(metadata(response))
        if index % 25 == 0 or index == len(taxids):
            print(f"reference taxonomy: {index}/{len(taxids)}", flush=True)
    if snapshot(root)[1]["_snapshot_sha256"] != proteins["_snapshot_sha256"]:
        raise ValueError("protein snapshot changed during taxonomy retrieval")
    common.write("card-taxonomy.json", {
        "taxa": taxa, "requests": requests,
        "proteins_sha256": proteins["_snapshot_sha256"],
    })


def candidate(entry, crossref, taxa):
    taxid = str(entry["organism"]["taxonId"])
    taxon = taxa[taxid]
    props = {prop["key"]: prop["value"] for prop in crossref.get("properties", [])}
    gene_names = {gene["geneName"]["value"] for gene in entry.get("genes", []) if "geneName" in gene}
    short_name = props.get("CARD short name", "")
    return {
        "accession": "UniProtKB:" + entry["primaryAccession"],
        "entry_type": entry["entryType"], "entry_audit": entry.get("entryAudit", {}),
        "protein_description": entry.get("proteinDescription", {}),
        "genes": entry.get("genes", []), "card_cross_reference": crossref,
        "gene_name_comparison": (
            "NO_GENE_SYMBOL" if not gene_names else
            "EXACT_TEXT_MATCH_NOT_ALLELE_PROOF" if short_name in gene_names else
            "NAMES_DIFFER_REVIEW_REQUIRED"
        ),
        "reference_taxon_id": "NCBITaxon:" + taxid,
        "reference_organism_name": entry["organism"]["scientificName"],
        "taxonomy_name": taxon.get("scientificName"), "taxonomy_rank": taxon.get("rank"),
        "taxonomy_status": "ACTIVE_REFERENCE_ID_RESOLVED" if taxon.get("active") is True
        else "REFERENCE_TAXON_REVIEW_REQUIRED",
        "pubmed_ids": sorted({x["id"] for reference in entry.get("references", [])
                              for x in reference.get("citation", {}).get("citationCrossReferences", [])
                              if x["database"] == "PubMed"}),
        "evidence_scope": "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING",
    }


def reference_contexts(entry):
    """Keep strain annotations attached to their own citation, never the whole entry."""
    references = entry.get("references", [])
    if not isinstance(references, list):
        raise ValueError("invalid UniProt reference list")
    result, numbers = [], set()
    for reference in references:
        if not isinstance(reference, dict):
            raise ValueError("invalid UniProt reference")
        number = reference.get("referenceNumber")
        citation = reference.get("citation")
        if (type(number) is not int or number < 1 or number in numbers
                or not isinstance(citation, dict)):
            raise ValueError("missing, duplicate or invalid reference identity")
        numbers.add(number)
        for key in ("citationType", "id"):
            if not isinstance(citation.get(key), str) or not citation[key].strip():
                raise ValueError("missing citation identity")
        metadata = {k: citation[k] for k in ("id", "citationType", "publicationDate") if k in citation}
        if any(not isinstance(v, str) or not v.strip() for v in metadata.values()):
            raise ValueError("invalid citation metadata")
        xrefs = citation.get("citationCrossReferences", [])
        if (not isinstance(xrefs, list) or any(
            not isinstance(x, dict) or set(x) != {"database", "id"}
            or any(not isinstance(v, str) or not v.strip() for v in x.values()) for x in xrefs
        )):
            raise ValueError("invalid citation cross-reference")
        metadata["citationCrossReferences"] = copy.deepcopy(xrefs)
        annotations = reference.get("referenceComments", [])
        if (not isinstance(annotations, list) or any(
            not isinstance(a, dict) or not {"type", "value"} <= set(a)
            or set(a) - {"type", "value", "evidences"}
            or any(not isinstance(a[k], str) or not a[k].strip() for k in ("type", "value"))
            for a in annotations
        )):
            raise ValueError("invalid reference annotation")
        evidences = [reference.get("evidences", [])] + [a.get("evidences", []) for a in annotations]
        if any(not isinstance(group, list) or any(
            not isinstance(e, dict) or "evidenceCode" not in e or set(e) - {"evidenceCode", "source", "id"}
            or any(not isinstance(v, str) or not v.strip() for v in e.values()) for e in group
        ) for group in evidences):
            raise ValueError("invalid reference evidence provenance")
        result.append({
            "reference_number": number, "citation": metadata,
            "evidences": copy.deepcopy(reference.get("evidences", [])),
            "strain_annotations": copy.deepcopy([a for a in annotations if a["type"] == "STRAIN"]),
            "omitted_comment_types": sorted({a["type"] for a in annotations if a["type"] != "STRAIN"}),
        })
    return result


def archive_groups(entries):
    """Group explicit archive IDs without choosing a representative protein or locus."""
    groups, proteins, missing = defaultdict(list), {}, []
    for accession, entry in sorted(entries.items()):
        if accession != entry["primaryAccession"]:
            raise ValueError("protein accession/key mismatch")
        attributes = entry.get("extraAttributes", {})
        if not isinstance(attributes, dict):
            raise ValueError("invalid UniProt extra attributes")
        upi = attributes.get("uniParcId")
        if upi is not None and (not isinstance(upi, str) or not re.fullmatch(r"UPI[0-9A-F]{10}", upi)):
            raise ValueError("invalid UniParc identifier")
        curie = "UniProtKB:" + accession
        proteins[curie] = {
            "uniparc_id": upi, "entry_audit": copy.deepcopy(entry.get("entryAudit", {})),
            "reference_taxon_id": "NCBITaxon:" + str(entry["organism"]["taxonId"]),
        }
        if upi is None:
            missing.append(curie)
        else:
            groups[upi].append(curie)
    return {
        "proteins": proteins, "archive_groups": dict(sorted(groups.items())),
        "proteins_without_archive_id": missing,
        "summary": {"reference_proteins": len(proteins), "archive_identifiers": len(groups),
                    "shared_archive_identifiers": sum(len(v) > 1 for v in groups.values()),
                    "proteins_with_shared_archive_id": sum(len(v) for v in groups.values() if len(v) > 1),
                    "proteins_without_archive_id": len(missing)},
    }


def archives(root):
    """Project cached archive identity metadata; do not fetch or compare sequences."""
    records, proteins = snapshot(root)
    ids = {claim["aro_id"] for _, claim in claims_from(records)}
    index = reference_index(proteins["entries"], ids)
    entries = {e["primaryAccession"]: e for candidates in index.values() for e, _ in candidates}
    result = archive_groups(entries)
    result["multiple_candidate_determinants"] = {
        aro: sorted("UniProtKB:" + entry["primaryAccession"] for entry, _ in candidates)
        for aro, candidates in sorted(index.items()) if len(candidates) > 1
    }
    if snapshot(root)[1]["_snapshot_sha256"] != proteins["_snapshot_sha256"]:
        raise ValueError("CARD grounding inputs changed during archive analysis")
    common.write("card-archive-groups.json", {
        **result, "scope": ARCHIVE_SCOPE,
        "source_inventory_sha256": proteins["source_inventory_sha256"],
        "corpus_sha256": proteins["corpus_sha256"],
        "protein_snapshot_sha256": proteins["_snapshot_sha256"],
        "release": proteins["release"],
        "attribution": "UniProt Consortium, CC BY 4.0; archive-ID annotations "
        "from cached UniProtKB metadata.",
        "documentation": ["https://www.uniprot.org/help/uniparc", "https://www.uniprot.org/help/gene_name"],
        "limitations": [
            "A shared archive identifier is database reference identity, "
            "not a tested allele or genomic locus.",
            "Gene annotations, citation contexts and strain labels remain separate; "
            "no representative is chosen.",
            "No sequence was fetched or compared; no gene model, strain equivalence "
            "or resistance effect is inferred.",
            "Missing archive metadata is not evidence of a missing protein or biological difference.",
        ],
    })
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


def contexts(root):
    """Export a separate context index; leave the candidate audit and corpus unchanged."""
    records, proteins = snapshot(root)
    audit_path = common.OUT / "card-reference-grounding.json"
    audit_bytes = audit_path.read_bytes()
    audit = json.loads(audit_bytes)
    if any(audit.get(k) != expected for k, expected in (
        ("protein_snapshot_sha256", proteins["_snapshot_sha256"]),
        ("source_inventory_sha256", proteins["source_inventory_sha256"]),
        ("corpus_sha256", proteins["corpus_sha256"]),
    )):
        raise ValueError("CARD candidate audit belongs to another snapshot")
    claims = claims_from(records)
    ids = {claim["aro_id"] for _, claim in claims}
    if ids != set(audit["determinants"]):
        raise ValueError("CARD candidate audit determinant coverage drift")
    index = reference_index(proteins["entries"], ids)
    memberships = Counter((r["identifier"], c["aro_id"]) for r, c in claims)
    by_protein = {}
    for aro in sorted(ids):
        expected = {"UniProtKB:" + e["primaryAccession"] for e, _ in index.get(aro, [])}
        candidates = audit["determinants"][aro]["candidates"]
        actual = [c["accession"] for c in candidates]
        if len(actual) != len(set(actual)) or set(actual) != expected:
            raise ValueError("CARD candidate audit protein coverage drift")
        for entry, _ in index.get(aro, []):
            accession = "UniProtKB:" + entry["primaryAccession"]
            if accession not in by_protein:
                by_protein[accession] = {
                    "entry_audit": copy.deepcopy(entry.get("entryAudit", {})),
                    "reference_taxon_id": "NCBITaxon:" + str(entry["organism"]["taxonId"]),
                    "reference_contexts": reference_contexts(entry), "corpus_memberships": [],
                    "primary_review_status": "PENDING",
                }
            by_protein[accession]["corpus_memberships"].extend(
                {"identifier": identifier, "aro_id": aro, "source_assertion_count": count}
                for (identifier, determinant), count in sorted(memberships.items()) if determinant == aro
            )
    all_contexts = [r for p in by_protein.values() for r in p["reference_contexts"]]
    summary = {
        "reference_proteins": len(by_protein), "citation_contexts": len(all_contexts),
        "citation_types": dict(Counter(r["citation"]["citationType"] for r in all_contexts)),
        "strain_annotation_occurrences": sum(len(r["strain_annotations"]) for r in all_contexts),
        "contexts_with_strain_annotations": sum(bool(r["strain_annotations"]) for r in all_contexts),
        "proteins_with_strain_annotations": sum(any(r["strain_annotations"] for r in p["reference_contexts"])
                                               for p in by_protein.values()),
        "proteins_without_citation_context": sum(not p["reference_contexts"] for p in by_protein.values()),
        "corpus_records_with_candidates": len({m["identifier"] for p in by_protein.values()
                                               for m in p["corpus_memberships"]}),
    }
    if (snapshot(root)[1]["_snapshot_sha256"] != proteins["_snapshot_sha256"]
            or audit_path.read_bytes() != audit_bytes):
        raise ValueError("CARD grounding inputs changed during context analysis")
    common.write("card-citation-context.json", {
        "scope": CONTEXT_SCOPE, "summary": summary, "proteins": by_protein,
        "source_inventory_sha256": proteins["source_inventory_sha256"],
        "corpus_sha256": proteins["corpus_sha256"],
        "protein_snapshot_sha256": proteins["_snapshot_sha256"],
        "candidate_audit_sha256": common.digest(audit_bytes),
        "attribution": audit["attribution"],
        "limitations": [
            "Citation and strain metadata are UniProt annotations, not inspected primary Results.",
            "A strain comment applies only to its citation; entry-wide or compound-level identity "
            "is not inferred.",
            "Repeated citations and strain comments are not independent experiments or unique isolates.",
            "No strain TaxID, assembly, experimental allele or measured resistance assignment is inferred.",
            "Only citation identity, reference evidence and strain comments are exported; other comment "
            "types are listed without their values. Titles, reference positions and experimental details "
            "are omitted.",
            "Missing citation metadata is a property of this request and release, "
            "not evidence of no literature.",
        ],
    })
    print(json.dumps(summary, indent=2), flush=True)


def analyze(root):
    records, proteins = snapshot(root)
    taxonomy_path = common.OUT / "card-taxonomy.json"
    taxonomy_payload = taxonomy_path.read_bytes()
    taxonomy = json.loads(taxonomy_payload)
    protein_hash = proteins["_snapshot_sha256"]
    if taxonomy["proteins_sha256"] != protein_hash:
        raise ValueError("taxonomy belongs to another protein snapshot")
    claims = claims_from(records)
    if not claims:
        raise ValueError("no source-owned CARD assertions in this corpus")
    ids = {claim["aro_id"] for _, claim in claims}
    with (root / SOURCE).open() as handle:
        source_rows = list(csv.DictReader(handle, delimiter="\t"))
    source_ids = {row["determinant_id"] for row in source_rows}
    if not ids <= source_ids:
        raise ValueError("corpus CARD determinant missing from the source inventory")
    references = reference_index(proteins["entries"], ids)
    labels = defaultdict(set)
    for _, claim in claims:
        labels[claim["aro_id"]].add(claim["label"])
    determinants = {}
    for aro in sorted(ids):
        candidates = [candidate(e, x, taxonomy["taxa"]) for e, x in references.get(aro, [])]
        determinants[aro] = {
            "labels": sorted(labels[aro]), "candidates": candidates,
            "status": "NO_EXPLICIT_LINK_IN_THIS_RELEASE" if not candidates else
            "ONE_REFERENCE_CANDIDATE_REQUIRES_REVIEW" if len(candidates) == 1 else
            "MULTIPLE_REFERENCE_CANDIDATES_RETAINED",
            "primary_review_status": "PENDING",
        }
    rows = []
    for record, claim in claims:
        determinant = determinants[claim["aro_id"]]
        candidates = determinant["candidates"]
        rows.append({
            "identifier": record["identifier"], "label": record["label"],
            "path": record["path"], "record_sha256": record["sha256"],
            "standard_inchi_key": record["standard_inchi_key"], "aro_id": claim["aro_id"],
            "determinant_label": claim["label"], "status": determinant["status"],
            "candidate_accessions": "|".join(c["accession"] for c in candidates),
            "reference_taxids": "|".join(sorted({c["reference_taxon_id"] for c in candidates})),
            "candidate_pubmed_ids": "|".join(sorted({p for c in candidates for p in c["pubmed_ids"]})),
            "primary_review_status": "PENDING",
        })
    links = [c for d in determinants.values() for c in d["candidates"]]
    unique_proteins = {c["accession"]: c for c in links}
    summary = {
        "corpus_records": len(records), "card_records": len({r["identifier"] for r in rows}),
        "card_assertions": len(rows), "card_determinants": len(ids),
        "determinant_status": dict(Counter(d["status"] for d in determinants.values())),
        "assertion_status": dict(Counter(row["status"] for row in rows)),
        "candidate_proteins": len(unique_proteins), "candidate_links": len(links),
        "candidate_entry_types": dict(Counter(c["entry_type"] for c in unique_proteins.values())),
        "candidate_gene_name_comparison": dict(Counter(c["gene_name_comparison"] for c in links)),
        "candidate_taxonomy_status": dict(Counter(c["taxonomy_status"] for c in unique_proteins.values())),
        "reference_taxa": len(taxonomy["taxa"]), "release": proteins["release"],
    }
    if (snapshot(root)[1]["_snapshot_sha256"] != protein_hash
            or taxonomy_path.read_bytes() != taxonomy_payload):
        raise ValueError("grounding inputs changed during analysis")
    common.write("card-reference-grounding.json", {
        "summary": summary, "determinants": determinants,
        "source_inventory_sha256": proteins["source_inventory_sha256"],
        "corpus_sha256": proteins["corpus_sha256"], "protein_snapshot_sha256": protein_hash,
        "taxonomy_snapshot_sha256": common.digest(taxonomy_payload),
        "requests": proteins["requests"] + taxonomy["requests"],
        "query": proteins["query"], "uniprot_total_results": proteins["total"],
        "attribution": {
            "source": "UniProt Consortium, UniProtKB and UniProt Taxonomy",
            "license": "CC BY 4.0", "license_url": "https://www.uniprot.org/help/license",
            "slice": "Explicit CARD cross-references in UniProt; card.json was not requested or imported.",
        },
        "scope": "DATABASE_REFERENCE_CANDIDATES_ONLY; NO_AST_OR_EXPERIMENTAL_ALLELE_ASSIGNMENTS",
    })
    with (common.OUT / "card-reference-ledger.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["proteins", "taxonomy", "analyze", "contexts", "archives"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-network", action="store_true")
    args = parser.parse_args()
    common.OUT = args.output_dir.resolve()
    common.OUT.mkdir(parents=True, exist_ok=True)
    common.ALLOW_NETWORK = args.allow_network
    globals()[args.stage](args.root.resolve())

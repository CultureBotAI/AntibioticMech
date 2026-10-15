"""Replay two unresolved CARD labels without turning citations into gene identities."""

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import audit_card_literature_expansion as literature
import audit_card_outer_membrane_references as prior
from audit_beta_tubulin_evidence import bibliography
from audit_valinomycin_abcb1 import planned_source
from lxml import etree

reference, require = prior.reference, prior.require
CACHE = Path("reports/resistance-grounding-2026-10-14-outer-membrane-evidence")
OUTPUT = Path("research/2026-10-14-outer-membrane-evidence.json")
SCOPE = "ABUO_OMP1_OWN_CITATION_CONTEXT_NOT_EXPERIMENTAL_GENE_ALLELE_ASSIGNMENT"
COHORT_SHA = "0f5683a3237b95b311f227ad04e5b7328d5bf3fb89554a76c77bb08621d5ea77"
TERMS = ("ARO:3004128", "ARO:3004578")
PMIDS = ("25512405", "25856195", "9353750")
PLAN_SHA = {
    "metadata-plan.json": "74220d9db69ba6244d42fb7b8b65bb7baba0ff6a626e212009d10f600c27da9b",
    "primary-plan.json": "b1098bcb0778e792c0b1a08442d56f2fbb854810b5781cdc935812a655ffc24c",
}
BODY_SHA = {
    "metadata-25512405": "dc724018cfce2c66300e7275b62040d09672faac9efd07925b03c4d2746fb012",
    "metadata-25856195": "bc017e7b14a8053fb8316daa9797e9b788b6c4e48ed761335b1988aedb380830",
    "metadata-9353750": "39e948bb184a573eac2f785cf031b33036748fa63b4cedf03399ed67dc4034d7",
    "primary-25856195": "6d6d5f4e93e5182a093226ee74bfe8556c65d8c90855584e69e12c692e5d2bd5",
}
PUBLICATIONS = {
    "25512405": {
        "title": (
            "AbuO, a TolC-like outer membrane protein of Acinetobacter baumannii, "
            "is involved in antimicrobial and oxidative stress resistance."
        ),
        "doi": "10.1128/aac.03626-14",
        "pmcid": "PMC4335886",
        "pubYear": "2015",
        "isOpenAccess": "N",
        "inEPMC": "Y",
    },
    "25856195": {
        "title": (
            "Comparative genome analyses of Serratia marcescens FS14 reveals its high antagonistic potential."
        ),
        "doi": "10.1371/journal.pone.0123061",
        "pmcid": "PMC4391916",
        "pubYear": "2015",
        "isOpenAccess": "Y",
        "inEPMC": "Y",
    },
    "9353750": {
        "title": "The role of outer membrane in Serratia marcescens intrinsic resistance to antibiotics.",
        "doi": None,
        "pmcid": None,
        "pubYear": "1997",
        "isOpenAccess": "N",
        "inEPMC": "N",
    },
}
ABSTRACT_SHA = {
    "25512405": "66d637bf5dcc572dc187dd2cbf564fc8a3919c89563d74bb20383c3864975a38",
    "25856195": "f7304b85ecd2ee5d47076bc691354f9da9b2a2cb74736239b9a57e6b666fa55b",
    "9353750": "141ce61118513fefaafa9d6a923c23bbc1923fdf53e12666becab4743497572e",
}
LOCATIONS = {
    "taxonomic_context": (
        "/article/body/sec[3]/sec[2]/p[1]",
        "6ca1ad3c970f2cc01f309c0a7d8445f329eef0b95d482ad87b1b1d958b5fe7e8",
    ),
    "paper_species_interpretation": (
        "/article/body/sec[3]/sec[2]/p[2]",
        "e8d834b0b6d0945c8454ee6dd1f8143d8e2ff428bc4f4ce24ad73311370855fd",
    ),
    "resistance_context": (
        "/article/body/sec[3]/sec[4]/p",
        "fa6470fc03c6bb2205dbf7a11c7f767c71581bf407de97ee3fd81cdedffe8370",
    ),
    "data_availability": (
        "/article/body/sec[7]",
        "bbb7cdac3a9129dfa518629b1222c12c02aff53fcba7db24b175e727d4530669",
    ),
}
XML_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4391916/fullTextXML"
PORIN_PATTERN = r"\b(?:omp\w*|porin\w*)\b"


def metadata_url(pmid):
    require(pmid in PMIDS, "unplanned publication")
    return "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode(
        {"query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json", "resultType": "core", "pageSize": 1}
    )


def project_metadata(payload, pmid):
    request, rows = payload["request"], payload["resultList"]["result"]
    require(
        type(payload["hitCount"]) is int
        and payload["hitCount"] == 1
        and len(rows) == 1
        and not payload.get("nextCursorMark")
        and request["queryString"] == "EXT_ID:" + pmid + " AND SRC:MED"
        and request["resultType"].lower() == "core"
        and type(request["pageSize"]) is int
        and request["pageSize"] == 1,
        "metadata query scope or completeness changed",
    )
    row = rows[0]
    require(
        row["id"] == row["pmid"] == pmid
        and row["source"] == "MED"
        and {k: row.get(k) for k in PUBLICATIONS[pmid]} == PUBLICATIONS[pmid]
        and hashlib.sha256(row["abstractText"].encode()).hexdigest() == ABSTRACT_SHA[pmid],
        "publication identity or inspected abstract changed",
    )
    return {
        "pmid": "PMID:" + pmid,
        **PUBLICATIONS[pmid],
        "abstract_sha256": ABSTRACT_SHA[pmid],
        "scope": "INDEXED_METADATA_NOT_PRIMARY_RESULTS",
        "primary_requested": pmid == "25856195",
        "abstract_is_gene_crosswalk": False,
        "global_access_or_paywall_inferred": False,
        "missing_doi_or_pmcid_is_global_absence": False,
    }


def project_primary(payload):
    require(hashlib.sha256(payload).hexdigest() == BODY_SHA["primary-25856195"], "primary XML changed")
    tree = etree.fromstring(payload, etree.XMLParser(resolve_entities=False, no_network=True))
    for kind, value in (
        ("pmid", "25856195"),
        ("pmcid", "PMC4391916"),
        ("doi", PUBLICATIONS["25856195"]["doi"]),
    ):
        require(
            tree.xpath(f"./front/article-meta/article-id[@pub-id-type='{kind}']/text()") == [value],
            "primary article identity changed",
        )
    locations, selected_text = {}, {}
    for key, (xpath, checksum) in LOCATIONS.items():
        matches = tree.xpath(xpath)
        require(len(matches) == 1, "selected primary location missing or ambiguous")
        selected_text[key] = " ".join("".join(matches[0].itertext()).split())
        require(
            hashlib.sha256(selected_text[key].encode()).hexdigest() == checksum,
            "selected primary context changed",
        )
        locations[key] = {"xpath": xpath, "normalized_text_sha256": checksum}
    require(
        "accession number: CP005927" in selected_text["data_availability"], "paper genome identifier changed"
    )
    matches = re.findall(PORIN_PATTERN, " ".join(tree.itertext()), re.I)
    require(not matches, "new literal porin mention requires review")
    return {
        "pmid": "PMID:25856195",
        "status": "SELECTED_PRIMARY_CONTEXT_NOT_FULL_PAPER_SIGNOFF",
        "locations": locations,
        "study_isolate_label": "FS14",
        "paper_organism_labels": ["Serratia sp. FS14", "S. marcescens FS14"],
        "paper_species_interpretation": "Serratia marcescens",
        "current_taxon_id_assigned_from_paper": None,
        "study_genome": {
            "namespace": "GenBank",
            "accession": "CP005927",
            "version": None,
            "scope": "PAPER_REPORTED_STUDY_GENOME_NOT_RESISTANCE_GENE_CROSSWALK",
            "source_location": "data_availability",
            "ncbi_link_followed": False,
            "independently_verified": False,
            "assembly_accession_inferred": False,
        },
        "text_screen": {
            "pattern": PORIN_PATTERN,
            "case_insensitive": True,
            "scope": "RETRIEVED_XML_TEXT_ONLY_NOT_IMAGES_OR_SUPPLEMENTS",
            "match_count": len(matches),
            "establishes_gene_absence": False,
            "invalidates_source_citation": False,
        },
        "interpretation": (
            "The selected text distinguishes genomic predictions and susceptibility results; "
            "it does not establish an Omp1 accession or exact resistance allele."
        ),
        "full_paper_signoff": False,
        "figures_visually_reviewed": False,
        "tables_reviewed_for_AST_curation": False,
        "supplements_reviewed": False,
        "resistance_gene_accession_assigned": None,
        "exact_resistant_allele_assigned": None,
        "numeric_AST_exported": False,
    }


def project_nonmatch(entry):
    names, direct = literature.literature.match_entry(entry, "ARO:3004128", "Omp1")
    require(
        entry["primaryAccession"] == "A0A0J9X1Q5"
        and not names
        and not direct
        and [g["geneName"]["value"] for g in entry["genes"]] == ["pigE"]
        and entry["proteinDescription"]["recommendedName"]["fullName"]["value"] == "Aminotransferase PigE"
        and entry["organism"]["taxonId"] == 1327989
        and entry["organism"]["scientificName"] == "Serratia sp. (strain FS14)"
        and entry["entryAudit"] == {"entryVersion": 39, "sequenceVersion": 1},
        "native nonmatching reference identity changed",
    )
    rows = bibliography(entry)
    require(
        len(rows) == 2
        and rows[0]["native_reference_number"] == 1
        and {"database": "PubMed", "id": "25856195"} in rows[0]["identifiers"]
        and rows[0]["reference_strain_comments"] == ["FS14"],
        "native citation membership changed",
    )
    return {
        "protein_accession": "UniProtKB:A0A0J9X1Q5",
        "reference_gene": "pigE",
        "reference_protein_name": "Aminotransferase PigE",
        "entry_version": 39,
        "sequence_version": 1,
        "reference_taxon_id": "NCBITaxon:1327989",
        "reference_organism_label": entry["organism"]["scientificName"],
        "native_bibliography": rows,
        "query_pmid": "PMID:25856195",
        "disposition": "CITATION_HIT_NOT_OMP1_REFERENCE",
        "assigned_to_source_term": False,
        "paper_species_label_overwrites_native_taxon": False,
        "matching_strain_comment_is_experimental_crosswalk": False,
    }


def request_context(root, directory):
    for suffix in ("-attempt.json", "-receipt.json", "-response.bin"):
        require(
            {p.name.removesuffix(suffix) for p in directory.glob("*" + suffix)} == set(BODY_SHA),
            "unexpected request or alternate route",
        )
    for filename, checksum in PLAN_SHA.items():
        require(reference.digest(directory / filename) == checksum, "request plan changed")
        plan = json.loads((directory / filename).read_bytes())
        require(
            plan["cohort"] == reference.pin(root, directory / "cohort.json")
            and plan["automatic_redirects"] is plan["retry_performed"] is False
            and plan["ncbi_requests"] == 0,
            "request constraints changed",
        )
    specs = [("metadata-" + p, "metadata-plan.json", metadata_url(p)) for p in PMIDS]
    specs.append(("primary-25856195", "primary-plan.json", XML_URL))
    sources, previous_time = {}, None
    for key, filename, url in specs:
        source = planned_source(root, directory, key, filename, url)
        require(source["body"]["sha256"] == BODY_SHA[key], "inspected response changed")
        attempt = json.loads(reference.check_pin(root, source["attempt"]).read_bytes())
        receipt = json.loads(reference.check_pin(root, source["receipt"]).read_bytes())
        start, end = (
            datetime.fromisoformat(attempt["started_at"]),
            datetime.fromisoformat(receipt["retrieved_at"]),
        )
        require(
            start <= end and (previous_time is None or previous_time <= start), "request chronology changed"
        )
        previous_time, sources[key] = end, source
    review = json.loads((directory / "metadata-canary-review.json").read_bytes())
    first = sources["metadata-25512405"]
    require(
        all(review[k] == first[k] for k in ("plan", "body", "receipt"))
        and review["manually_inspected"] is True
        and review["primary_results_reviewed"] is False,
        "metadata canary changed",
    )
    return sources


def build(root, directory=CACHE):
    directory = root / directory
    require(reference.digest(directory / "cohort.json") == COHORT_SHA, "frozen cohort changed")
    cohort = json.loads((directory / "cohort.json").read_bytes())
    for key in (
        "prior",
        "prior_verification",
        "census",
        "source_queue",
        "literature",
        "protected",
        "access_inventory",
    ):
        reference.check_pin(root, cohort[key])
    old = json.loads(reference.check_pin(root, cohort["prior"]).read_bytes())
    receipt = json.loads(reference.check_pin(root, cohort["prior_verification"]).read_bytes())
    require(
        cohort["prior"] in receipt["files"] and receipt["summary"] == old["summary"], "prior proof changed"
    )
    require(prior.build(root) == old, "native reference context or current corpus changed")
    terms = {tid: old["terms"][tid] for tid in TERMS}
    ids = {rid for t in terms.values() for rid in t["record_memberships"]}
    require(
        cohort["terms"] == terms
        and cohort["pmids"] == list(PMIDS)
        and cohort["records"] == [r for r in old["records"] if r["identifier"] in ids]
        and cohort["claims"] == [c for c in old["claims"] if c["aro_id"] in TERMS],
        "cohort coverage changed",
    )
    require(
        all(t["reference_status"] == "NO_EXACT_GENE_RESULTS_NOT_ABSENCE" for t in terms.values()),
        "unresolved reference selection changed",
    )
    frozen = json.loads(reference.check_pin(root, cohort["literature"]).read_bytes())
    entries, queries = {}, {}
    for pmid in PMIDS:
        entries[pmid], queries[pmid] = literature.read_query(root, root / literature.DIRECTORY, pmid)
        require(
            queries[pmid]["complete_for_query"] and queries[pmid]["release"] == "2026_03",
            "literature query incomplete or release changed",
        )
    require(frozen == {"entries": entries, "queries": queries}, "native bibliography query changed")
    require(
        {p: sorted(e) for p, e in entries.items()}
        == {"25512405": [], "25856195": ["A0A0J9X1Q5"], "9353750": []},
        "literature candidate membership changed",
    )
    sources = request_context(root, directory)
    metadata = {
        p: {
            **project_metadata(json.loads((directory / ("metadata-" + p + "-response.bin")).read_bytes()), p),
            "source": sources["metadata-" + p],
        }
        for p in PMIDS
    }
    primary = project_primary((directory / "primary-25856195-response.bin").read_bytes())
    nonmatch = project_nonmatch(entries["25856195"]["A0A0J9X1Q5"])
    return {
        "date": cohort["date"],
        "scope": SCOPE,
        "inputs": {
            **{k: cohort[k] for k in ("prior", "prior_verification", "census", "source_queue", "literature")},
            "cohort": reference.pin(root, directory / "cohort.json"),
        },
        "terms": terms,
        "records": cohort["records"],
        "claims": cohort["claims"],
        "reused_literature_queries": queries,
        "publications": metadata,
        "unassigned_citation_hits": [nonmatch],
        "request_sources": sources,
        "primary_context": {**primary, "source": sources["primary-25856195"]},
        "summary": {
            "source_terms": len(terms),
            "source_claims": len(cohort["claims"]),
            "cohort_records": len(cohort["records"]),
            "corpus_records_hash_checked": 2939,
            "complete_records_read_in_prior_replay": len(old["records"]),
            "reused_complete_literature_queries": len(queries),
            "unassigned_citation_hits": 1,
            "primary_context_reviews": 1,
            "metadata_only_papers": 2,
            "paper_reported_study_genomes": 1,
            "new_verified_resistance_results": 0,
            "experimental_gene_allele_assignments": 0,
            "biological_records_changed": 0,
        },
        "constraints": {
            "network_requests": 4,
            "new_uniprot_requests": 0,
            "ncbi_requests": 0,
            "primary_requests": 1,
            "retry_performed": False,
            "redirects_followed": False,
            "issue_1040": "DEFERRED",
            "reuse_terms_review_resumed": False,
            "source_adoptions": 0,
            "github_mutations": 0,
            "full_corpus_goal_status": "OPEN",
        },
        "limitations": [
            "Own-citation follow-up covers two of the 29 outer-membrane-label terms, not the whole cohort.",
            "Zero results and literal text-screen nonmatches are scoped searches, not biological absence.",
            "AbuO and the 1997 Omp1 paper remain metadata-only; lack of an OA flag is not an access denial.",
            "One paper-reported genome is not an independently verified assembly "
            "or a mapped resistant allele.",
            "The FS14 species interpretation and native UniProt organism label remain distinct.",
            "Tables, figures, supplements, quantitative AST and all whole-record signoffs remain open.",
        ],
        "attribution": (
            "CARD/ARO ontology: McMaster University, CC BY 4.0. "
            "UniProt metadata: UniProt Consortium. Bibliographic metadata: Europe PMC at EBI. "
            "Primary context: Li et al. 2015, doi:10.1371/journal.pone.0123061. No source adoption."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(Path.cwd())
    payload = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.check or args.output.exists():
        require(args.output.read_bytes() == payload, "saved dossier does not reproduce")
    else:
        with args.output.open("xb") as stream:
            stream.write(payload)


if __name__ == "__main__":
    main()

# NCBI AST Source-Terms Review

## Decision

The maintainer's 2026-10-04 request to address
[#1040](https://github.com/CultureBotAI/AntibioticMech/issues/1040) resumes the
previously deferred review. It does not supply rights from NCBI or submitters.
The repository's data license is **CC BY 4.0**, not CC0.

**Adoption remains blocked pending clarification.** Keep `ncbi-ast` at
`use: REFERENCE`, `redistribution: UNVERIFIED`, and `status: BLOCKED`.
`verified_on: 2026-10-04` records this review date, not a permission grant.
The official pages inspected below do not establish an explicit compatible
grant for all submitted phenotypes and metadata in this cohort. This is a
repository adoption decision under the source-queue policy, not a conclusion
that NCBI prohibits reuse or that individual measurements are copyrightable.

No evaluated inventory, collection or observation is installed in production.
The technical audits remain useful; passing them does not resolve this gate.
#1040 stays open for the uncompleted production-adoption checklist.

## Primary Sources

All links below were inspected on 2026-10-04. Findings are paraphrases;
interpretations are identified separately from statements on the source pages.

1. [NCBI Website and Data Usage Policies](https://www.ncbi.nlm.nih.gov/home/about/policies/):
   government-created material is public domain with acknowledgment requested;
   contributed material can retain third-party rights. For molecular databases,
   NCBI imposes no use/distribution restrictions and declines submissions with
   reuse restrictions, but does not acquire submitter rights to pass onward.
   **Interpretation:** this is positive evidence for open reuse, not a blanket
   CC0 designation or an explicit grant for every submitter's AST contribution.
   Modification and commercial redistribution of this exact surface remain
   unresolved under this project's explicit-terms adoption policy.
2. [AST Browser documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/):
   the browser exposes submitted BioSample phenotypic results, not NCBI-inferred
   resistance. It supports downloads for analysis and updates daily.
   **Interpretation:** access and analysis are supported; these instructions do
   not independently establish modification/commercial redistribution terms.
3. [Pathogen Detection help](https://www.ncbi.nlm.nih.gov/pathogens/pathogens_help/)
   and [submission instructions](https://www.ncbi.nlm.nih.gov/pathogens/submit-data/):
   the system combines submitted isolate metadata with NCBI analyses, encourages
   open data and accepts antibiograms through BioSample. A mixed export must not
   be labeled entirely US-government-authored merely because NCBI hosts it.
4. [BioSample submission FAQ](https://www.ncbi.nlm.nih.gov/biosample/docs/submission/faq/):
   BioSample is submitter-driven; submitters own responsibility for content and
   accuracy. Public release and basic validation do not establish a rights
   transfer. Citation guidance recommends retaining accession references.
5. [NCBI Taxonomy overview](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/taxonomy/):
   NCBI curators maintain names, classifications and TaxIDs using published
   taxonomy and expert input. These fields are distinct from submitted AST
   measurements. Neither a documentation article's license nor taxonomy
   curation settles the rights to linked BioSample phenotypes or third-party
   material. This review does not redistribute taxonomy XML.
6. [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html):
   government and third-party content are distinguished; users must determine
   applicable restrictions for material outside the public domain.
7. [Pathogen Detection FAQ](https://www.ncbi.nlm.nih.gov/pathogens/faq/):
   PDT accessions are not archival; save metadata for reproducible analyses.
   This supports checksum-pinned snapshots, not an independent license grant.
8. [AST at GCP](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast_gcp/):
   this separate alpha surface has an explicit production-analysis contact
   warning and can differ from the browser. It was inspected as a possible
   alternative, **not used** for this cohort. Its conditions are not silently
   transferred to the native browser export, or used to authorize that export.

No software license, secondary database license label, or publication license
was substituted for the data terms. This review covers these inspected pages,
not a claim that every NCBI page or every submitter's terms has been searched.

## Exact Data Surfaces

The intended transformation retains source values and identifiers, normalizes
units and schema representation, and consolidates only source-verified repeats.
It would redistribute derived inventories and records commercially as well as
noncommercially under the project's CC BY 4.0 policy. These are the surfaces
that a compatible decision must cover:

| Surface | Frozen input and use | Remaining terms question |
|---|---|---|
| Native AST Browser TSV | `pathogens/pathogens-srv/`, `action=solr2txt`, `browser=ast`; measured MIC/disk results, comparators, assay context, submitted calls and accessions | Does the no-restrictions policy cover these submitted phenotypes, including modification and commercial redistribution? Which submitter exceptions apply? |
| Native Isolates Browser JSON | Same service, `action=retrieve`, `collection=isolates`; PDT, BioSample, BioProject, TaxID, scientific name, assembly and strain | Distinguish NCBI-produced identifiers/results from submitted fields; establish applicable terms for both. |
| BioSample XML | E-utilities `efetch`, `db=biosample`; original antibiograms and record timestamps used to verify 62 repeated results | Confirm terms for the submitted antibiograms and metadata, including evidence retained in review decisions. Do not infer coverage from GenBank sequence terms alone. |
| Taxonomy XML | E-utilities `efetch`, `db=taxonomy`; names/lineage for the 433-TaxID overlap audit | Preserve the NCBI attribution/policy notice and clarify any third-party exclusions for the exact fields retained. No images or external taxonomic works are copied. |

The [AST snapshot manifest](2026-10-03-ncbi-ast-snapshot.json) and
[isolate snapshot manifest](2026-10-03-ncbi-ast-isolate-snapshot.json) retain the
full queries, retrieval timestamps, file sizes and source versions. The
2026-10-03 release identity is the snapshot checksum, not a mutable URL or the
2026-10-04 terms-review date:

| Input | SHA-256 |
|---|---|
| Native AST TSV | `ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184` |
| Isolates JSON | `220427a8a2ab23d383478b4af906d48169f67cb0b6ebbfaef36a27b5bd8a193e` |
| Expanded-cohort BioSample XML | `498ba42ee6acb179edc9b64f8cefd58a85fdf680e62610271c71b63476e7b6e8` |
| Expanded-cohort taxonomy XML | `0b2c5aaad4b05541aaa8282f8382ea45cf590ea289e8f43574aa790496169f26` |
| Reviewed gzip inventory | `4f396c7843750066afb8225832ac6023305779a4bcd037940de8ff8d0149b4f2` |
| Expanded inventory content | `bcac2fb84c9f7df5d78fab90f330738e31dcdb7b82bc3dfc7069a351edacc41a` |

The scientific snapshots above were rehashed on 2026-10-04. At clean main
`6140f0093eff9f775df9872c729457a26c683814`, the prior full-publication audit's
3,033 input pins also matched. Its report hash is
`87003d123e3c301e7feb76d36a25ee665a17804cec2a8f196e09c9684d4f6fa7`.
The overlap report rehashed to
`bbc1f48c55ebbf81fcec77828d1fbc88a8ef8e911b2ac1b258c71b564f13ee3c`.
These checks verify existing evidence identity, not a fresh scientific audit or
production adoption. This branch changes the source queue, which is itself a
publication-audit input; do not claim every prior pin matches the new branch.
Future adoption must rerun the applicable audits against its actual tree.

## Clarification Draft: Not Sent

Recipient, if separately authorized: `pd-help@ncbi.nlm.nih.gov`, the contact
listed in the official FAQ. No source-maintainer contact has been made as part
of this review. A draft or an unanswered request does not satisfy the gate.

Subject: Reuse terms for submitted AST phenotypes and linked metadata

We maintain AntibioticMech, a CC BY 4.0 structure-grounded data resource. We
are evaluating a 2026-10-03 native AST Browser export and its linked isolate,
BioSample and taxonomy metadata, not AMRFinderPlus code or GCP data. Our
reviewed subset contains 213,144 source groups representing 213,082 measured
observations on 40 exact compounds. We would preserve source accessions and
citations, normalize units and schema, disclose transformations, and provide
downloadable derived records for commercial and noncommercial reuse.

Does NCBI's molecular-data policy apply to these submitted AST phenotypes and
all four metadata surfaces above? Please identify the applicable authoritative
terms for modification and redistribution, including commercial use, and any
submitter/third-party exclusions or field-level differences. If NCBI cannot
answer for submitters, how should downstream users identify applicable
submitter terms? What attribution, disclaimer, retrieval-date and version
notices should accompany the derived records? We are not asking NCBI to grant
rights it does not hold or to endorse our resource.

## Resume Conditions

Record an authoritative clarification or a maintainer-approved legal review of
the exact surfaces and retained fields. A reply that covers only software,
taxonomy or federal contributions cannot clear other submitters' phenotypes.
If clearance applies only to a subset, identify and exclude unverified rows,
rebuild that subset and renew all affected audits; do not reuse the whole-cohort
acceptance unchanged. Preserve applicable notices without claiming the project
relicenses third-party rights it does not own.

Only then implement the source configuration, attribution, one reviewed raw
inventory with its manifest, canary and full source-owned production generation,
and the remaining #1040 publication, review and merge checks. Do not mark
#1040 complete or relabel the source ADOPTED for this review-only change.

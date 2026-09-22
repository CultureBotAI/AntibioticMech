# YAML Record Review: (7R)-7-(5-carboxy-5-oxopentanamido)cephalosporanic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml`
- Started UTC: 2026-09-22T13:51:49Z
- Finished UTC: 2026-09-22T13:52:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:15838` |
| Label | `(7R)-7-(5-carboxy-5-oxopentanamido)cephalosporanic acid` |
| Path | `data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:15838`, version `2026-08-30`, minted key `antibioticmech:chebi-a3e541dad5` |
| Source role | `CHEBI:33281` antimicrobial agent |
| Parent compound | `CHEBI:23066` cephalosporin |
| Structure | `UKRMDFPJXIVYCZ-BXUZGUMPSA-N`; formula `C16H18N2O9S`; charge `0` |
| Xrefs | `beilstein:5395497`; `kegg.compound:C04712` |
| Source literature leads | None |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for the neutral
alpha-ketoadipyl-7-aminocephalosporanic-acid intermediate commonly abbreviated
`AKA-7-ACA`. The YAML has exact ChEBI grounding, the ChEBI definition, four
exact ChEBI synonyms, one strictly broader ChEBI parent, two xrefs, the broad
ChEBI antimicrobial-agent role, structure, and source-concept metadata. It has
no generated or curator-owned mode of action, molecular target, activity
observation, resistance mechanism, producer, dataset, discussion, causal graph,
or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml --out /tmp/antibioticmech-chebi-15838-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-15838.tsv` | Pass: the full worklist TSV was written. `CHEBI:15838` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 66` | Pass: `CHEBI:15838` is queued with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:15838` resolves in official OLS as a current, non-obsolete ChEBI term
with label `(7R)-7-(5-carboxy-5-oxopentanamido)cephalosporanic acid`, the same
text definition as the generated record, the exact Standard InChIKey
`UKRMDFPJXIVYCZ-BXUZGUMPSA-N`, the exact formula `C16H18N2O9S`, and the exact
`beilstein:5395497` and `kegg.compound:C04712` xrefs stored by this record.

The live OLS term exposes the same exact synonyms stored in the YAML. The
IUPAC-name synonym is duplicated upstream in the OLS term JSON, but the
generated YAML stores it once, which is the correct local representation.

The live OLS graph gives `CHEBI:15838` one direct `subClassOf` edge:
`CHEBI:23066` `cephalosporin`. That is exactly the generated
`parent_compounds` value. The graph also exposes a protonation edge to
`CHEBI:57536` `(7R)-7-(5-carboxy-5-oxopentanamido)cephalosporanate(2-)`; that
edge is not strict subclass parentage and is correctly absent from
`parent_compounds`.

The committed ChEBI inventory row carries role `CHEBI:33281` `antimicrobial
agent`; `data/raw/chebi_role_names.tsv` marks that role as a broad `scope`
role; and `conf/sources.yaml` maps it to the generated
`ANTIMICROBIAL_UNSPECIFIED` filing class. That role is generic, but it is the
only ChEBI antimicrobial role on this source row, so the record was filed under
the lowest-priority generic class without erasing source role provenance.

Before this report was created, an ignored-inclusive exact search for
`CHEBI:15838`, the exact record path, exact Standard InChIKey, exact
`beilstein:5395497`, exact `kegg.compound:C04712`, and the exact label across
`data/antibiotics`, `data/raw`, `curation`, and `reports/yaml_record_review`
found only the expected generated YAML, `PATHS.tsv` row, raw ChEBI row, and
`record_review_queue.tsv` row. No prior dedicated review report for
`data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml`
was found.

## Evidence

The record's antimicrobial classification is inherited from committed ChEBI
role `CHEBI:33281`, `antimicrobial agent`. That broad role is sufficient for
the generator to file the record under `ANTIMICROBIAL_UNSPECIFIED`; it is not
compound-specific primary evidence for an MIC, microbial target, antimicrobial
mode of action, producer, resistance mechanism, or causal graph edge.

The pinned ChEBI source row has no PubMed citations, and the generated record
has no evidence-bearing objects. Bounded direct PubMed eSearch for the exact
Standard InChIKey `UKRMDFPJXIVYCZ-BXUZGUMPSA-N`, the exact ChEBI label
`(7R)-7-(5-carboxy-5-oxopentanamido)cephalosporanic acid`, all exact
ChEBI-provided synonyms, and exact KEGG accession `C04712` returned zero
indexed candidates.

Bounded PubMed eSearch for exact title/abstract `AKA-7-ACA` returned one
candidate, `PMID:17349708`. Exact searches for
`alpha-ketoadipyl-7-aminocephalosporanic acid`,
`2-oxoadipyl-7-aminocephalosporanic acid`, and
`ketoadipyl-7-aminocephalosporanic acid` returned no indexed candidates.
The broader repository PubMed helper was not used for claim support because
the short alias expanded into off-topic tokenized hits. A Semantic Scholar
attempt on the broad query returned HTTP 429 and was also not used.

`PMID:17349708` is useful context for compound handling, not claim-level
antimicrobial support for exact `CHEBI:15838`. Its PubMed abstract treats
AKA-7-ACA as an accumulated intermediate during industrial conversion of
cephalosporin C to 7-aminocephalosporanic acid in recombinant `Escherichia
coli` expressing D-amino acid oxidase and GL-7-ACA acylase. It does not report
a measured MIC, susceptible organism, molecular target, resistance genotype, or
biosynthetic producer for purified exact `CHEBI:15838`.

No NCBI Taxonomy verification was needed for this pass because the review did
not add source-organism or susceptible-organism rows. The exact-alias lead uses
recombinant `E. coli` as a biocatalyst host and does not establish de novo
biosynthesis or susceptibility of that taxon to `CHEBI:15838`.

## Completeness

The record is incomplete as a reviewed antimicrobial AKA-7-ACA record. It has
exact ChEBI identity, definition, structure, a strictly broader ChEBI parent,
two xrefs, and source-level broad antimicrobial classification from the pinned
inventory, but no primary-paper antimicrobial evidence, no `activity_spectrum`,
no molecular target, no mode of action, no producer, no dataset, and no causal
graph.

The empty mechanism and target fields are correct for the current seed.
`CHEBI:33281` does not specify a mode of action, and the inspected publication
lead establishes AKA-7-ACA as a cephalosporin-production intermediate rather
than as a tested antimicrobial molecule with a direct microbial target.

The empty `activity_spectrum` and producer slots are preferable to over-scoped
filler. The candidate abstract describes enzymatic conversion of cephalosporin
C through AKA-7-ACA; it does not report an antimicrobial phenotype for exact
`CHEBI:15838`, and it does not show de novo biosynthesis by a producing taxon.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are also acceptable. No measured resistance edge,
clinical assertion, public dataset accession, or discussion-worthy conflict
with exact `CHEBI:15838` claim-level evidence was identified in the bounded
checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:15838` has only generic ChEBI antimicrobial-agent classification and no curator-owned exact-compound assay, producer, mechanism, target, or causal-graph claim. | The generated record has no source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no producer, and no `mode_of_action`. Bounded exact-name, exact-xref, and exact-alias publication searches found one industrial bioconversion lead for AKA-7-ACA but no claim-level antimicrobial support for purified exact `CHEBI:15838`. | Future curator-owned fields on `data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI's generic role is only a cephalosporin-class inheritance artifact with no exact molecule support, the ChEBI inventory extractor or a `curation/decisions.tsv` exclusion row owns that source-level correction. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Trace why the pinned ChEBI source row assigns `CHEBI:33281` to exact
   `CHEBI:15838`, and inspect the next ChEBI refresh diff for the same role.
   If the role has exact-compound antimicrobial assay provenance, curate that
   primary paper through the record's `activity_spectrum`; if it is only
   inherited from the `CHEBI:23066` cephalosporin class without an exact assay,
   consider a scoped source exclusion in `curation/decisions.tsv`.
2. Inspect `PMID:17349708` and any primary papers it cites only for exact
   antimicrobial assays. Require purified exact `CHEBI:15838`, a susceptible
   organism or strain, assay method, measured value, and unit before adding an
   `ActivityObservation`.
3. Do not curate D-amino acid oxidase, GL-7-ACA acylase, or other
   7-aminocephalosporanic-acid production enzymes as antimicrobial molecular
   targets for this record. The inspected abstract uses those enzymes as
   production catalysts, not microbial targets inhibited by `CHEBI:15838`.
4. Add a producer only from primary literature or MIBiG evidence that a named
   taxon biosynthesizes exact `CHEBI:15838`. Recombinant `E. coli` expression
   hosts are insufficient.
5. Add resistance mechanisms only from primary papers that test exact
   `CHEBI:15838` against a stated microbial resistance genotype or route; do
   not infer resistance from cephalosporin-class membership or from
   AKA-7-ACA-bioconversion enzyme activity.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml`
2. `just validate-strict data/antibiotics/unspecified/7r-7-5-carboxy-5-oxopentanamido-cephalosporanic-acid.yaml --out /tmp/antibioticmech-chebi-15838-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-15838.tsv`
5. `just review-queue --limit 66`
6. `just qc`

Manually compare any future activity, mechanism, target, producer, resistance,
dataset, or causal-graph assertion against exact `CHEBI:15838` identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, the broader cephalosporin class,
or production enzymes that convert cephalosporin C through AKA-7-ACA.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

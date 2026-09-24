# YAML Record Review: (Z,Z,Z)-geranylgeraniol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml`
- Started UTC: `2026-09-24T05:42:40Z`
- Finished UTC: `2026-09-24T05:45:10Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml` |
| Identifier | `CHEBI:18822` |
| Label | `(Z,Z,Z)-geranylgeraniol` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source provenance | ChEBI `CHEBI:18822`, version `2026-08-30` |
| Source role | `CHEBI:70868` antileishmanial agent |
| Parent compound | `CHEBI:24229` geranylgeraniol |
| Structure source | ChEBI |
| Standard InChIKey | `OJISWRZIEWCUBN-XBQSVVNOSA-N` |

This review covered exactly one generated ChEBI-seeded all-cis geranylgeraniol
record. The generated YAML was read in full and was not edited.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml --out /tmp/z-z-z-geranylgeraniol-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected, 2,939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. The only diagnostic was the known unrelated `ARO:3000337`/iclaprim cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/z-z-z-geranylgeraniol-worklist.tsv` | Passed; exact `CHEBI:18822` appeared only on `mechanism` and `review-readiness`, with 0 CARD targets and 0 resistance edges to build on. The only diagnostic was the known unrelated `ARO:3000337`/iclaprim cross-reference refusal. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; at report selection time, `CHEBI:18822` was the first queue row without an exact one-record review report after matching prior report identifiers and normalized report headers. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*z-z-z-geranylgeraniol*' -print` | Passed; at report selection time, no prior exact `z-z-z-geranylgeraniol` report was found. `find` included ignored files. |
| `rg --no-ignore --hidden -n "CHEBI:18822|\(Z,Z,Z\)-geranylgeraniol|z-z-z-geranylgeraniol|geranylgeraniol" data/antibiotics data/raw curation reports/yaml_record_review` | Passed; at report selection time, this found the exact generated record, `PATHS.tsv` lock row, ChEBI inventory row, queue rows, broader geranylgeraniol and all-trans sibling rows, and the prior all-trans review. The search included ignored files. |
| OLS4 ChEBI API checks for `CHEBI:18822`, `CHEBI:24229`, `CHEBI:46762`, and `CHEBI:70868` | Passed; OLS resolved the exact all-cis term, parent geranylgeraniol, all-trans sibling `(E,E,E)-geranylgeraniol`, and `antileishmanial agent`. |
| LIPID MAPS REST lookup for `LMPR0104010018` | Passed; LIPID MAPS resolved the xref to `CHEBI:18822` and the same `(Z,Z,Z)-geranylgeraniol` formula, InChI, InChIKey, and `nerylnerol` synonym. |
| Reaxys xref `5745026` | Not checked: Reaxys is a source xref in the ChEBI row but is not publicly resolvable in this local workflow. |
| PubMed/Semantic Scholar exact search for `(Z,Z,Z)-geranylgeraniol`, `nerylnerol`, `CHEBI:18822`, `OJISWRZIEWCUBN-XBQSVVNOSA-N`, and `LMPR0104010018` | Partial pass; PubMed returned one nerylnerol carrier-substrate lead, while Semantic Scholar returned HTTP 429. |
| PubMed exact-name fallback search for `nerylnerol`, all-cis geranylgeraniol names, and the IUPAC name | Passed; PubMed returned the same nerylnerol carrier-substrate lead. |
| PubMed broad search for geranylgeraniol and antileishmanial terms | Passed; PubMed returned 2 parent or extract leads. |
| PubMed lookup for parent geranylgeraniol ChEBI PMIDs `23304195`, `23983115`, `24006306`, and `24762323` | Passed; PubMed returned all 4 parent leads. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record in this repository; the full-corpus checks above were
the narrowest documented checks for those contracts.

## Identity and Grounding

The exact record identity agrees with ChEBI and LIPID MAPS:

| Claim | Review |
| --- | --- |
| Label and identifier | Supported. OLS4 resolves `CHEBI:18822` to `(Z,Z,Z)-geranylgeraniol` and describes it as the geranylgeraniol in which the double bonds have cis geometry. |
| Structure | Supported. OLS4 reports formula `C20H34O`, Standard InChI, Standard InChIKey `OJISWRZIEWCUBN-XBQSVVNOSA-N`, zero charge, average mass `290.491`, and SMILES equivalent to the generated ChEBI structure. |
| LIPID MAPS xref | Supported. `LMPR0104010018` resolves to `(Z,Z,Z)-geranylgeraniol`, ChEBI `18822`, formula `C20H34O`, InChIKey `OJISWRZIEWCUBN-XBQSVVNOSA-N`, and the `nerylnerol` synonym. |
| Reaxys xref | Not independently checked. `reaxys:5745026` is present in the ChEBI upstream row but no public resolver was available in this workflow. |
| Stereochemical boundary | Supported. Sibling `CHEBI:46762` is all-trans `(E,E,E)-geranylgeraniol` with a different Standard InChIKey, `OJISWRZIEWCUBN-QIRCYJPOSA-N`; parent `CHEBI:24229` is stereochemically unspecified geranylgeraniol with InChIKey `OJISWRZIEWCUBN-UHFFFAOYSA-N`. |
| Antileishmanial role | Supported as a ChEBI source claim. The generated `activity_roles` and committed source row contain `CHEBI:70868`, and OLS4 resolves that CURIE as `antileishmanial agent`. |

The record has one source concept, the exact ChEBI term. No ARO, CARD-only,
PubChem, or curator concept is merged into this record.

## Evidence

The generated YAML has no record-level `evidence`, `mode_of_action`,
`molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, or
`causal_graphs`. That is schema-valid because a ChEBI seed inherits its
classification from `data/raw/chebi_antimicrobials.tsv`, but no
claim-level evidence has been curated yet.

No exact antibacterial, antiprotozoal, or antileishmanial PMID was found for
`CHEBI:18822`, `(Z,Z,Z)-geranylgeraniol`, or `nerylnerol`. The exact PubMed
hit was `PMID:24377322`, which tested nerylnerol as a synthetic carrier
substrate for `Campylobacter jejuni` PglB N-glycosylation. It is an identity
and enzymology lead, not antileishmanial evidence.

The inspected broader antileishmanial leads apply to neighboring scopes:
`PMID:23304195` reports stereochemically unspecified geranylgeraniol activity
against `Leishmania amazonensis`; `PMID:23983115` tested an essential oil from
`Bixa orellana` seeds where geranylgeraniol was one constituent; and
`PMID:27725158` tested `Pterodon pubescens` extracts. These are discovery leads
for the parent or all-trans records. Their abstracts do not establish that exact
all-cis `(Z,Z,Z)-geranylgeraniol` was the assayed antileishmanial compound.

The other parent-geranylgeraniol ChEBI PMIDs resolved to human-cell mevalonate
pathway or cancer-cell studies and did not support this record's antiprotozoal
classification or missing mechanism fields.

## Completeness

| Field family | Review |
| --- | --- |
| Identity and structure | Complete for a ChEBI exact seed except for the non-public Reaxys xref. ChEBI and LIPID MAPS agree on the exact all-cis identity, formula, InChIKey, and `nerylnerol` synonym. |
| Source concept | Complete. The only source concept is exact `CHEBI:18822`. |
| Xrefs | `lipidmaps:LMPR0104010018` was verified as exact; `reaxys:5745026` remains an unchecked ChEBI-imported xref because no public resolver was available. |
| Record evidence | Empty. Acceptable for a raw seed, but no inspected source is attached to the record. |
| Mode of action and targets | Empty. Consequential gap; the review-readiness row is a `MECHANISM_REVIEW` row, and the mechanism worklist row reports 0 CARD targets. |
| Activity observations | Empty. No exact all-cis antileishmanial assay was found in the bounded exact and broad searches. |
| Resistance mechanisms | Empty and expected for this ChEBI-only antiprotozoal seed; there are 0 CARD resistance edges to build on. |
| Causal graph | Empty because no exact mechanism claim is curated yet. |
| Generated ownership | Correct. The reviewed YAML is emitted from `data/raw/chebi_antimicrobials.tsv` and `data/antibiotics/PATHS.tsv`; future seeded-field corrections belong in those inputs or in the ChEBI extractor rather than as hand edits to the generated record. |

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | None found. | The YAML validates, the corpus reproduces exactly, and exact ChEBI/LIPID MAPS identity and structure agree. | Not applicable. |
| Major | Exact `CHEBI:18822` remains a source-seeded antileishmanial structure with no reviewed exact activity evidence, no mechanism, no molecular target, and no causal graph. | The generated record has 0 record evidence items and no `mode_of_action`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, or `causal_graphs`; exact `CHEBI:18822` is on the `mechanism` and `review-readiness` worklists with 0 CARD targets, 0 CARD resistance edges, and 0 source literature leads. The exact `nerylnerol` PubMed hit is not antimicrobial, and the antileishmanial leads found by the broad searches do not resolve exact all-cis `(Z,Z,Z)-geranylgeraniol`. | Future curator-owned fields on `data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI changes this term's role, parentage, xrefs, or source PMIDs, `data/raw/chebi_antimicrobials.tsv` and the ChEBI extractor own the refresh. |
| Minor | `reaxys:5745026` is an unchecked ChEBI-imported xref in this review. | The generated xref matches the committed ChEBI inventory row and OLS4's `database_cross_reference` annotation, but Reaxys had no public resolver available here to verify same-structure semantics directly. | ChEBI extractor and `data/raw/chebi_antimicrobials.tsv`; future curation should either verify this source externally or preserve it as an upstream ChEBI assertion. |

## Recommended Edits

1. Keep `activity_spectrum`, `mode_of_action`, `molecular_targets`, and
   `causal_graphs` empty until a primary source directly assays exact
   `(Z,Z,Z)-geranylgeraniol` against a defined Leishmania or other protozoan
   organism, with enough assay context to avoid transferring parent, all-trans,
   extract, or essential-oil evidence to the all-cis structure.
2. Treat `PMID:23304195` and `PMID:23983115` as curation leads for the broad
   `CHEBI:24229` parent or all-trans geranylgeraniol record unless their full
   text explicitly resolves the assayed compound as exact all-cis
   `CHEBI:18822`.
3. Verify `reaxys:5745026` through Reaxys or a future ChEBI refresh before
   treating it as independently reviewed exact-identity evidence.

## Follow-up Checks

1. `just validate data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml`
2. `just validate-strict data/antibiotics/antiprotozoal/z-z-z-geranylgeraniol.yaml --out /tmp/z-z-z-geranylgeraniol-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/z-z-z-geranylgeraniol-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`

Rerun targeted exact searches for `nerylnerol`, `CHEBI:18822`, and
`OJISWRZIEWCUBN-XBQSVVNOSA-N` before any future curation. Manually verify
stereochemical scope before promoting parent-geranylgeraniol Leishmania leads
to all-cis activity observations, mode of action, or causal graphs.

## Additional Notes

The absence checks above used `find` or `rg --no-ignore --hidden`, so generated
reports ignored by Git were included.

The prior all-trans report
`reports/yaml_record_review/20260923T000944Z-e-e-e-geranylgeraniol.md` already
captured the main `PMID:23304195` and `PMID:23983115` caveats for exact
all-trans geranylgeraniol. The same scope issue applies more strongly here
because exact all-cis `CHEBI:18822` has a different InChIKey from both the
unspecified parent and the all-trans sibling.

Semantic Scholar was not required for the verdict. PubMed resolved the exact
`nerylnerol` lead and the bounded antileishmanial parent leads needed to bound
the gap.

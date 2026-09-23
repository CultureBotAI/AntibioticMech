# YAML Record Review: (R)-mandelic acid

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/r-mandelic-acid.yaml
- Started UTC: 2026-09-23T10:05:00Z
- Finished UTC: 2026-09-23T10:14:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | AntibioticRecord |
| Identifier | CHEBI:17656 |
| Label | (R)-mandelic acid |
| Path | data/antibiotics/antibacterial/r-mandelic-acid.yaml |
| Maintained status | Generated from `data/raw/chebi_antimicrobials.tsv` |
| Grounding | `EXACT` ChEBI source concept `CHEBI:17656` |
| Curation status | `SEEDED` |

The target is the ChEBI-seeded `(R)` enantiomer of mandelic acid. Exact
ignored-inclusive searches over `data/antibiotics`, `data/raw`, `curation`,
and `reports/yaml_record_review` found one exact source row for `CHEBI:17656`,
one PATHS row, one queue row, the generated YAML identifier/source-id entries,
and no prior exact review report for this identifier.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/r-mandelic-acid.yaml` | Pass; no LinkML validation issues. |
| `just validate-strict data/antibiotics/antibacterial/r-mandelic-acid.yaml --out /tmp/r-mandelic-acid-validate-strict.tsv` | Pass; 1 file checked, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Pass; all 2,939 expected records were present on disk with no missing, unexpected, drift, path, or stale rows. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 xref refusal. |
| `just worklist --limit 0 --tsv /tmp/r-mandelic-acid-worklist.tsv` | Pass; wrote the full TSV. The anchored `CHEBI:17656` rows are the `mechanism` and `review-readiness` backlog entries. |
| `just review-queue --limit 120` | Pass; listed `CHEBI:17656` as `MECHANISM_REVIEW` with 1 source literature lead, 0 record evidence items, and 0 targets. |
| `just lint` | Pass. |
| `git diff --check` | Pass before adding this report. |
| `git diff --cached --check` | Pass after force-adding this ignored report. |

No narrower single-record term, reference, curation-history, or corpus-drift
validator is exposed for plain ChEBI-seeded records; `validate-strict` and
`verify-corpus --summary` are the narrowest documented checks for this case.

## Identity and Grounding

The local ChEBI inventory row for `CHEBI:17656` contains label
`(R)-mandelic acid`, role term `CHEBI:33282`, parent `CHEBI:35825`, SMILES
`O=C(O)[C@H](O)c1ccccc1`, Standard InChI
`InChI=1S/C8H8O3/c9-7(8(10)11)6-4-2-1-3-5-6/h1-5,7,9H,(H,10,11)/t7-/m1/s1`,
InChIKey `IWYDHOAUDWTVEP-SSDOTTSWSA-N`, formula `C8H8O3`, net charge `0`,
average mass `152.149`, monoisotopic mass `152.04734`, ChEBI synonyms, and
ChEBI xrefs. The generated YAML carries the same preferred label, structure,
parent, role term, and retained same-structure xrefs.

`CHEBI:33282` is the ChEBI `antibacterial agent` role and maps to
`ANTIBACTERIAL` in `conf/sources.yaml`, so the file path and
`antimicrobial_class` are consistent with the source role.

Exact ignored-inclusive searches over `data/antibiotics`, `data/raw`,
`curation`, and `reports/yaml_record_review` found no second generated record
with InChIKey `IWYDHOAUDWTVEP-SSDOTTSWSA-N` and no second generated record with
source-concept minted identifier `antibioticmech:chebi-828a74eef9`. Sibling
records are intentionally distinct: `CHEBI:35825` is racemic or
stereochemistry-unspecified `mandelic acid` with InChIKey
`IWYDHOAUDWTVEP-UHFFFAOYSA-N`, and `CHEBI:32800` is `(S)-mandelic acid` with
InChIKey `IWYDHOAUDWTVEP-ZETCQYMHSA-N`.

## Evidence

The record has no record-level `evidence`, `mode_of_action`,
`mode_of_action_target_scope`, `molecular_targets`, `activity_observations`,
`resistance_mechanisms`, `producer_organisms`, or `causal_graphs`. That is an
honest generated state for a ChEBI seed whose only antimicrobial assertion is
an upstream antibacterial-agent role.

The single literature lead imported from ChEBI, `PMID:11196078`, resolves to an
occupational ethylbenzene biomonitoring paper where mandelic acid is measured
as a urinary metabolite. It does not support an antimicrobial mode of action,
activity observation, target, resistance mechanism, producer claim, or causal
edge for `(R)-mandelic acid`.

Bounded publication discovery left `NCBI_EMAIL` unset and queried:

- `(R)-mandelic acid`
- `IWYDHOAUDWTVEP-SSDOTTSWSA-N`
- `(2R)-hydroxy(phenyl)acetic acid`
- `R-mandelic acid antibacterial`
- `11196078`

PubMed returned exact-label and synonym leads for biocatalytic production,
chemical synthesis, chiral separation, chiral sensing, and physical chemistry
of `(R)-mandelic acid`. The antibacterial-focused query returned a cephamandole
synthesis paper that uses an `(R)-mandelic acid` ester as an acylation reagent.
The exact Standard InChIKey query returned no candidates. Semantic Scholar was
HTTP 429 for the exact label, exact InChIKey, synonym, and antibacterial
queries. No inspected lead yielded compound-specific antimicrobial mechanism or
MIC evidence for the exact `CHEBI:17656` structure.

## Completeness

The seeded identity, ChEBI grounding, generated structure, parent relation,
antibacterial role, source concept, and retained ChEBI xrefs are complete
enough for an unreviewed ChEBI seed.

The record still lacks all reviewed antimicrobial biology:

- no `mode_of_action` or `mode_of_action_target_scope`;
- no `molecular_targets`;
- no `activity_observations`;
- no `resistance_mechanisms`;
- no `causal_graphs`;
- no exact-enantiomer antimicrobial evidence beyond ChEBI's antibacterial role.

`just worklist` therefore correctly queues `CHEBI:17656` for mechanism
curation, and `just review-queue` correctly keeps it in `MECHANISM_REVIEW`.

## Findings

None found.

There are no blocker, major, or minor defects in the generated YAML. The absent
mechanism, target, activity, resistance, and graph sections are curation gaps,
not invalid seeded claims, because the bounded searches above did not find
evidence precise enough to populate them for `(R)-mandelic acid`.

## Recommended Edits

None for the generated seed.

Do not populate activity, target, resistance, or causal-graph fields from the
current ChEBI lead, biocatalytic production papers, or cephamandole synthesis
paper. A future curator should only edit
`data/antibiotics/antibacterial/r-mandelic-acid.yaml` through
`write_validated_antibiotic` if a primary source reports antimicrobial
activity or mechanism for the exact `(R)` enantiomer, with every activity
measurement carrying the assayed organism, method, value, and units.

## Follow-up Checks

If a future curator finds exact `(R)-mandelic acid` antimicrobial data and edits
the record, rerun:

- `just validate-strict data/antibiotics/antibacterial/r-mandelic-acid.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv`
- `just qc`
- `git diff --check`

No follow-up check is needed for this read-only review.

## Additional Notes

`PMID:11196078` is present in the raw ChEBI row and the review-readiness queue,
but not in the generated record. Record-level evidence is optional for
ChEBI-seeded identity and role assertions, and the PMID does not provide
claim-level antimicrobial support.

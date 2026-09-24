# YAML Record Review: (S)-mandelic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/s-mandelic-acid.yaml`
- Started UTC: 2026-09-24T00:00:00Z
- Finished UTC: 2026-09-24T00:06:28Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `CHEBI:32800` |
| Label | `(S)-mandelic acid` |
| Path | `data/antibiotics/antibacterial/s-mandelic-acid.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concepts | `CHEBI:32800` from ChEBI 2026-08-30 |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`; source-owned identity or xref changes must go through the extractor, `data/raw/`, or `curation/decisions.tsv`, not through a hand edit to this YAML. |

The record resolves unambiguously. `data/antibiotics/PATHS.tsv` maps
`CHEBI:32800` to `ANTIBACTERIAL/s-mandelic-acid`, and an
ignored-inclusive search for `CHEBI:32800`, `(S)-mandelic acid`,
`s-mandelic-acid`, and `mandelic acid` across `data/antibiotics/PATHS.tsv`,
`data/raw`, `curation`, and `reports/yaml_record_review` found the expected
raw ChEBI row, path row, review-queue row, sibling `(R)` and racemic mandelic
acid rows, and prior sibling reports, but no exact prior
`(S)-mandelic acid` report.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/antibiotics/antibacterial/s-mandelic-acid.yaml` | Pass: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/s-mandelic-acid.yaml --out /tmp/s-mandelic-acid-validate-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2,939 records expected and on disk; 0 missing, unexpected, or drifted records; 0 `PATHS.tsv` discrepancies. The only diagnostic was the known unrelated `iclaprim`/`CHEBI:31724` CARD cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/s-mandelic-acid-worklist.tsv` | Pass: wrote the full TSV. `CHEBI:32800` appears on `mechanism`, `xref-span-conflict`, and `review-readiness`. |
| `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/s-mandelic-xref-span.tsv` | Pass: confirmed raw `cas:90-64-2` is withheld from `CHEBI:32800` because ChEBI also publishes it on racemic `CHEBI:35825`. |
| `just review-queue --limit 130` | Pass: listed `CHEBI:32800` as `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Pass: `ruff check` reported `All checks passed!`. |
| `git diff --check` | Pass: no whitespace errors. |
| `git diff --cached --check` | Pass: no staged whitespace errors. |

No narrower single-record term, reference, or history validator is exposed for
plain ChEBI-seeded generated records. The full-corpus worklist and
`verify-corpus` checks above are the documented repository checks for those
concerns.

## Identity and Grounding

The YAML denotes one ChEBI-grounded structure: the neutral `(S)` enantiomer of
mandelic acid.

| Claim | Review |
| --- | --- |
| ChEBI identity | The official OLS4 entry for `CHEBI:32800` is active, non-obsolete, 3-star, labelled `(S)-mandelic acid`, and has Standard InChIKey `IWYDHOAUDWTVEP-ZETCQYMHSA-N`, matching the YAML. |
| Structure | OLS4 and `data/raw/chebi_antimicrobials.tsv` agree with the YAML on SMILES `O=C(O)[C@@H](O)c1ccccc1`, Standard InChI `InChI=1S/C8H8O3/c9-7(8(10)11)6-4-2-1-3-5-6/h1-5,7,9H,(H,10,11)/t7-/m0/s1`, formula `C8H8O3`, neutral charge, average mass `152.149`, and monoisotopic mass `152.04734`. |
| ChEBI parents | OLS4 reports the same two direct parents retained in `parent_compounds`: `CHEBI:17375` `(2S)-2-hydroxy monocarboxylic acid` and `CHEBI:35825` mandelic acid. These are broader concepts rather than exact same-structure xrefs. |
| Sibling structures | `CHEBI:17656` `(R)-mandelic acid` and `CHEBI:35825` racemic or stereo-unspecified mandelic acid are separate records with distinct Standard InChIKeys. The record's `@@` SMILES and `-ZETCQYMHSA-N` key keep the `(S)` record separate from the `(R)` and racemic entries. |
| Activity role and filing class | The sole role is `CHEBI:33282`, which OLS4 resolves as active, non-obsolete `antibacterial agent`; filing the record as `ANTIBACTERIAL` follows `conf/sources.yaml`. |
| Exact xrefs | OLS4 publishes the retained Beilstein, CAS, DrugBank, Gmelin, KEGG COMPOUND, and PDB CCD cross-references. KEGG `C01984` names `(S)-mandelate` and cross-references both `CHEBI:17756` and `CHEBI:32800`; PDB CCD `SMN` is named `(S)-MANDELIC ACID` and carries the same formula and InChIKey as the YAML. |
| Withheld raw xref | The raw ChEBI row also carries `cas:90-64-2`, but the generated YAML correctly omits it because the same accession appears on racemic `CHEBI:35825`; `just worklist` reports this as `xref-span-conflict`, not as a published exact-equivalence assertion. |

Common Chemistry refused unauthenticated CAS API lookups with `API key
required`, so `cas:17199-29-0` and `cas:611-72-3` were confirmed only as
official ChEBI xrefs in this pass. Beilstein, Gmelin, and DrugBank were likewise
not independently re-resolved outside ChEBI.

## Evidence

The record has no `evidence` array and no object-level evidence-bearing claims.
That is honest for a generated ChEBI-only record: the source concept and
structure come from ChEBI, and there are no target, resistance, activity,
producer, clinical, or causal graph assertions that would require primary
citations.

The raw ChEBI row for `CHEBI:32800` has no PubMed references. Bounded
publication searches left `NCBI_EMAIL` unset and used these queries with
PubMed and Semantic Scholar:

| Query | Result |
| --- | --- |
| `(S)-mandelic acid` | PubMed returned 20 candidates dominated by chiral cocrystal, synthesis, enantioseparation, and sensing papers; Semantic Scholar returned HTTP 429. |
| `IWYDHOAUDWTVEP-ZETCQYMHSA-N` | PubMed returned 0 candidates; Semantic Scholar returned HTTP 429. |
| `L-mandelic acid antibacterial` | Returned 20 candidates. The exact `L` lead, PMID:23608509, engineered `Geobacillus stearothermophilus` lactate dehydrogenase to accept `l`-mandelic acid as a substrate rather than testing antimicrobial activity. Other hits covered polymers, racemic or unspecified mandelic acid, and broader derivative work. |
| `(S)-2-Hydroxy-2-phenylacetic acid antimicrobial` | PubMed returned one infrared/Raman structure paper unrelated to antimicrobial activity; Semantic Scholar returned HTTP 429. |
| `17199-29-0 antibacterial` | PubMed returned 20 candidates, all covering mandelic-acid derivatives, complexes, coamorphous systems, or plain mandelic acid rather than exact `(S)-mandelic acid`; Semantic Scholar returned HTTP 429. |
| `611-72-3 antibacterial` | PubMed returned 20 candidates with the same derivative or unspecified-mandelic-acid pattern; Semantic Scholar returned HTTP 429. |

Direct NCBI EFetch inspection of the nearest PubMed leads did not supply an
exact `(S)-mandelic acid` mechanism or MIC:

| PMID | Verdict |
| --- | --- |
| PMID:23608509 | Mentions `l`-mandelic acid as an alpha-hydroxy acid with antibacterial activity, but the experiment is enzyme engineering and substrate-specificity measurement. It is not an antimicrobial assay for this compound. |
| PMID:2513198 | Tests mandelic acid against *Escherichia coli* biofilms and planktonic cells in urine, but the abstract does not specify the `(S)` enantiomer or a schema-ready MIC. |
| PMID:1680900 | Tests `1% w/v` mandelic acid in a physical bladder model, again without identifying the `(S)` enantiomer or a mechanism. |

## Completeness

`CHEBI:32800` remains intentionally thin. It has no CARD source concept, no CARD
target, and no CARD resistance edges, so there are no source-owned target or
resistance imports to audit. The complete worklist places this identifier only
on:

- `mechanism`: absent mode of action, with `0 CARD target(s), 0 resistance edge(s) to build on`;
- `xref-span-conflict`: raw `cas:90-64-2` is published on both `(S)-mandelic acid` and racemic mandelic acid and is therefore withheld;
- `review-readiness`: `MECHANISM_REVIEW`, with 0 source literature leads, 0 record evidence items, and 0 targets.

The same complete worklist has no exact `CHEBI:32800` row for `target-evidence`,
`minted`, `xref-unverified`, `xref-name-conflict`, `multi-component`,
`producer-candidate`, `activity-candidate`, or `structure-unreviewed`.

Empty slots for `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`clinical_status_assertions`, `datasets`, and `causal_graphs` are preferable to
backfilling racemic mandelic-acid antiseptic papers, mandelic-acid derivatives,
or enzyme-substrate papers onto an exact `(S)` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The record still needs exact `(S)-mandelic acid` mechanism review before it can become `REVIEWED`. | The YAML has no `mode_of_action`, no molecular targets, no activity observations, and no causal graph. `just worklist` keeps `CHEBI:32800` on `mechanism` and `review-readiness`, and bounded exact-identifier publication searches found no primary paper that establishes an `(S)-mandelic acid` antimicrobial mechanism. | Future curator-owned fields on `data/antibiotics/antibacterial/s-mandelic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Do not edit the source-owned identity, structure, class, parent, or retained
   xref fields for `CHEBI:32800`: they reproduce from the official ChEBI row and
   from `PATHS.tsv`.
2. Leave `cas:90-64-2` out of `xrefs` unless a future maintainer can resolve
   which ChEBI structure that CAS number actually denotes. The maintained raw
   assertion is already surfaced on `just worklist --queue xref-span-conflict`.
3. When a source that measures exact `(S)-mandelic acid` antimicrobial activity
   or a direct mechanism is found, add only the supported curator-owned object:
   `mode_of_action`, `molecular_targets`, `activity_observations`, and/or a
   `causal_graph`, with claim-level evidence on the narrowest object.

## Follow-up Checks

If a future curator changes this record:

- Run `just validate-strict data/antibiotics/antibacterial/s-mandelic-acid.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Run `just verify-corpus` to prove source-owned generated fields still match
  `data/raw/`.
- Run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and
  confirm `CHEBI:32800` leaves `mechanism` and `review-readiness` only after an
  exact mechanism review has actually been curated.
- Re-run `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/antibioticmech-xref-span.tsv`
  if `cas:90-64-2` is ever restored or intentionally suppressed at the raw-xref
  layer.
- Re-run `just lint`, `git diff --check`, and `git diff --cached --check`
  before opening a PR.

## Additional Notes

The official ChEBI term for `CHEBI:32800` has no definition, and the generated
YAML correctly has no `definition` or `definition_source`. Adding a
curator-authored definition is lower priority than establishing exact
antimicrobial mechanism or activity evidence.

The `KEGG:C01984` entry is named `(S)-Mandelate` and links both the neutral acid
`CHEBI:32800` and its conjugate base `CHEBI:17756`. That is an external
registry shape to keep in mind when future work checks protonation boundaries,
but it does not contradict the current record's neutral ChEBI identity.

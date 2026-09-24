# YAML Record Review: (−)-microdiplodiasolol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/microdiplodiasolol.yaml`
- Started UTC: 2026-09-24T18:12:55Z
- Finished UTC: 2026-09-24T18:13:23Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `CHEBI:68285` |
| Label | `(−)-microdiplodiasolol` |
| Path | `data/antibiotics/antibacterial/microdiplodiasolol.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concepts | `CHEBI:68285` from ChEBI 2026-08-30 |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv` and `data/antibiotics/PATHS.tsv`; source-owned identity, structure, class, role, parent, xref, and source-concept changes must go through the ChEBI extractor, raw inventory, `curation/decisions.tsv`, or the seeder rather than a hand edit to this YAML. |

The record resolves unambiguously. `data/antibiotics/PATHS.tsv` maps
`CHEBI:68285` to `ANTIBACTERIAL/microdiplodiasolol`, and an ignored-inclusive
search for `CHEBI:68285`, `microdiplodiasolol`, and
`SIUXYUWNLUKHJD-FVQBIDKESA-N` across `data/antibiotics`, `data/raw`,
`curation`, `reports/yaml_record_review`, `.git`, and the full `/tmp`
worklist/review TSVs found the expected ChEBI raw row, path row, worklist rows,
target YAML, and current branch checkout log, with no prior exact
`microdiplodiasolol` report or duplicate structure in the searched corpus.

## Validation

| Check | Result |
| --- | --- |
| `rg --no-ignore --hidden -n 'CHEBI:68285\|microdiplodiasolol\|SIUXYUWNLUKHJD' ...` | Pass: resolved the expected ChEBI raw row, path row, target record, worklist rows, and current branch checkout log; no prior exact `CHEBI:68285` or `microdiplodiasolol` report and no duplicate `SIUXYUWNLUKHJD-FVQBIDKESA-N` record were found. Hidden and ignored files were included. |
| `just validate data/antibiotics/antibacterial/microdiplodiasolol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/microdiplodiasolol.yaml --out /tmp/microdiplodiasolol-validate-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Pass: 2,939 records expected and present; 0 missing, unexpected, or drifted records; 0 `PATHS.tsv` discrepancies. The only diagnostic was the known unrelated `iclaprim`/`CHEBI:31724` CARD cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Pass: wrote the full TSV. `CHEBI:68285` appears on `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Pass: regenerated the full `review-readiness` queue and listed `CHEBI:68285` as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| ChEBI OLS4 lookups for `CHEBI:68285` | Pass: the official exact search, term lookup, direct parent lookup, and direct `has role` lookup resolve and agree with the generated identity, structure, parent, Reaxys xref, and antibacterial role fields. |
| NCBI EFetch for `PMID:21244021` | Pass: resolved the ChEBI literature lead and its DOI. |
| NCBI PubMed ESearch | Pass: exact `microdiplodiasolol` title/abstract search found 0 rows on 2026-09-24; broader `Microdiplodia` title/abstract search found 12 rows, including `PMID:21244021`. |

No narrower single-record term, reference, or history validator is exposed for
plain generated ChEBI records. The full-corpus `worklist` and `verify-corpus`
checks above are the documented repository checks for those concerns.

## Identity and Grounding

The YAML denotes one exact, ChEBI-grounded structure: neutral
`(−)-microdiplodiasolol`, ChEBI's `(1S,4aS,9aS)` xanthone.

| Claim | Review |
| --- | --- |
| ChEBI identity | The official OLS4 exact lookup for `CHEBI:68285` returned one ChEBI class labelled `(-)-microdiplodiasolol`, matching the YAML label apart from minus-glyph normalization. The OLS4 term endpoint reports the same identifier as active and non-obsolete. |
| Structure | OLS4, `data/raw/chebi_antimicrobials.tsv`, and the YAML agree on SMILES `COC1=CC(=O)[C@@H](O)[C@@]2(O)C(=O)c3c(O)cc(C)cc3O[C@]12C`, Standard InChI `InChI=1S/C16H16O7/c1-7-4-8(17)12-10(5-7)23-15(2)11(22-3)6-9(18)13(19)16(15,21)14(12)20/h4-6,13,17,19,21H,1-3H3/t13-,15-,16-/m1/s1`, Standard InChIKey `SIUXYUWNLUKHJD-FVQBIDKESA-N`, formula `C16H16O7`, neutral charge, average mass `320.297`, and monoisotopic mass `320.0896`. |
| Synonym | OLS4 and the raw ChEBI row report the same exact IUPAC synonym retained in the record: `(1S,4aS,9aS)-1,8,9a-trihydroxy-4-methoxy-4a,6-dimethyl-4a,9a-dihydro-1H-xanthene-2,9-dione`. |
| ChEBI parents | The OLS4 parent lookup returns exactly the five broader classes in `parent_compounds`: `CHEBI:139592` tertiary alpha-hydroxy ketone, `CHEBI:2468` secondary alpha-hydroxy ketone, `CHEBI:33853` phenols, `CHEBI:47985` enol ether, and `CHEBI:51149` xanthones. |
| Activity role and filing class | OLS4 returns `CHEBI:33282` antibacterial agent as a direct `has role` target for `CHEBI:68285`; filing the record as `ANTIBACTERIAL` follows the retained ChEBI antibacterial role. OLS4 also reports the non-antimicrobial `CHEBI:76946` fungal metabolite role, which the generated `activity_roles` field correctly omits. |
| Xrefs | OLS4 and `data/raw/chebi_antimicrobials.tsv` both list the exact-equivalence `reaxys:21389528` xref retained in the YAML. The remaining database cross-reference on the OLS term is the PubMed literature identifier and correctly does not appear in the structure-identity `xrefs` field. |

No wrong identity, grounding, xref, parent, or class conflict was found.

## Evidence

The record has no `evidence` array and no object-level evidence-bearing
assertions. That is honest for a generated ChEBI-only seed: identity, role,
parents, xref, and structure reproduce from ChEBI, while there are no molecular
targets, resistance mechanisms, MIC measurements, producer claims, clinical
assertions, datasets, or causal edges that would need primary-paper evidence.

`CHEBI:68285` carries one source literature lead:

| PMID | DOI | Review |
| --- | --- | --- |
| `PMID:21244021` | `10.1021/np100730b` | PubMed resolves this to Siddiqui et al. 2011, `Diversonol and blennolide derivatives from the endophytic fungus Microdiplodia sp.: absolute configuration of diversonol.` The abstract reports chemical investigation of a fungal `Microdiplodia sp.` strain isolated from *Lycium intricatum*, isolation of four new compounds, and antibacterial activity against *Legionella pneumophila* and/or antifungal activity against *Microbotryum violaceum* for most metabolites, but it does not name `(−)-microdiplodiasolol`, expose exact MIC values, or expose a compound-specific molecular target or mode of action. |

## Completeness

`CHEBI:68285` remains intentionally thin. It has no CARD source concept, no CARD
target, no CARD resistance edge, no curator-authored `mode_of_action`, no
molecular target, no activity observation, no producer organism, and no causal
graph.

The full worklist places this identifier only on:

- `mechanism`: absent mode of action, with `0 CARD target(s), 0 resistance edge(s) to build on`
- `producer-candidate`: `Microdiplodia species — "isolated from", SOURCE only — may not be the producer`
- `review-readiness`: `MECHANISM_REVIEW`, with 1 source literature lead, 0 top-level record evidence items, and 0 targets

The same complete worklist has no exact `CHEBI:68285` row for
`target-evidence`, `minted`, `unknown-mech`, `moa-scope`, `aro-class`,
`xref-unverified`, `xref-name-conflict`, `xref-span-conflict`,
`multi-component`, `activity-candidate`, `unnamed-producer`, or
`structure-unreviewed`.

An NCBI PubMed title/abstract search for the exact phrase
`"microdiplodiasolol"` found 0 rows on 2026-09-24, which means ChEBI's own
`PMID:21244021` lead cannot be rediscovered from PubMed title/abstract
metadata by exact record label. A broader `Microdiplodia` title/abstract search
found 12 rows, including the ChEBI lead; that genus-level context is useful for
bounded rediscovery only, not as compound-specific evidence for a schema-ready
activity or producer observation.

Empty slots for `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `activity_observations`, `resistance_mechanisms`,
`producer_organisms`, `clinical_status_assertions`, `datasets`, and
`causal_graphs` are preferable to inferring a target, measured activity, or
biosynthetic organism from the ChEBI antibacterial role and genus-level
definition text.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The record still needs compound-specific mechanism review before it can become `REVIEWED`. | The YAML has no `mode_of_action`, no molecular targets, no activity observations, and no causal graph. `just worklist` keeps `CHEBI:68285` on `mechanism` and `review-readiness` even though ChEBI supplies `PMID:21244021` as a source literature lead. The PubMed abstract for that lead supports the Microdiplodia natural-products context but does not expose a compound-specific MIC, molecular target, or mode of action for `(−)-microdiplodiasolol`. | Future curator-owned fields on `data/antibiotics/antibacterial/microdiplodiasolol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |
| Minor | The genus-level producer lead should be checked before any optional `producer_organisms` row is added. | `just worklist` places `CHEBI:68285` on `producer-candidate` because the ChEBI definition says the compound was isolated from `Microdiplodia species`, and `PMID:21244021` resolves to a paper about metabolites from an endophytic `Microdiplodia sp.`. The abstract does not expose an NCBITaxon-resolvable species, strain, or enough source context for a schema-ready producer claim, so leaving the optional producer slot empty is honest until full-text inspection. | Future curator-owned `producer_organisms` rows on `data/antibiotics/antibacterial/microdiplodiasolol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings found.

## Recommended Edits

1. Do not edit the source-owned identity, structure, synonym, class, role,
   parent, xref, or source-concept fields for `CHEBI:68285`: they reproduce
   from the official ChEBI row, `data/raw/chebi_antimicrobials.tsv`, and
   `data/antibiotics/PATHS.tsv`.
2. Inspect the full text and supplementary data for Siddiqui et al. 2011,
   DOI `10.1021/np100730b`, before adding any `activity_observations`. Add
   compound-specific organism and strain observations only when the source
   states assay method plus exact values and units; do not promote the
   abstract's pooled "most metabolites" statement to an observation for this
   exact structure.
3. Leave `producer_organisms` empty unless the full text, supplementary data,
   or a future source identifies the producing organism with enough taxon and
   strain context for a schema-ready claim.
4. Add `mode_of_action`, `molecular_targets`, or `causal_graphs` only after a
   primary source identifies how `(−)-microdiplodiasolol` inhibits
   *Legionella* or another microbial system.
5. Keep `curation_status: SEEDED` until identity, structure, class, and the
   antimicrobial mode of action have all been checked and any target claims
   have primary citations.

## Follow-up Checks

If a future curator changes this record:

- Run `just validate-strict data/antibiotics/antibacterial/microdiplodiasolol.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Run `just verify-corpus` to prove source-owned generated fields still match
  `data/raw/`.
- Run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and
  confirm `CHEBI:68285` leaves `mechanism`, `producer-candidate`, and
  `review-readiness` only after exact mechanism review and producer triage have
  actually been curated.
- Re-run `just lint`, `git diff --check`, and `git diff --cached --check`
  before opening a PR.

## Additional Notes

The three neighbouring ChEBI rows `CHEBI:68283` microdiplodiasol,
`CHEBI:68284` `(+)-microdiplodiasone`, and `CHEBI:68289` `(−)-gynuraone` use
the same `PMID:21244021` literature lead. Reviewing
`(−)-microdiplodiasolol` as its own exact structure avoids copying a pooled
activity statement or any future full-text measurement from one numbered
metabolite onto another.

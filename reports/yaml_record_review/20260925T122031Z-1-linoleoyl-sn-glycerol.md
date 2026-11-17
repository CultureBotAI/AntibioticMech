# YAML Record Review: 1-linoleoyl-sn-glycerol

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml
- Started UTC: 2026-09-25T12:15:00Z
- Finished UTC: 2026-09-25T12:20:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | AntibioticRecord |
| Identifier | CHEBI:75561 |
| Label | 1-linoleoyl-sn-glycerol |
| File | data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml |
| Maintained/generated status | Generated from `data/raw/chebi_antimicrobials.tsv` |
| `curation_status` | SEEDED |
| `grounding_status` | EXACT |
| Source concept | CHEBI:75561, minted as `antibioticmech:chebi-0a5e8ca954`, ChEBI 2026-08-30 |
| Imported activity role | CHEBI:22587, antiviral agent |

The record is a generated exact ChEBI seed for one stereospecific monoacylglycerol. It has ChEBI-owned identity, structure, synonyms, ChEBI parents, an antiviral role, HMDB/Reaxys xrefs, one source concept, and the seed-time audit trail. It does not yet have curator-owned evidence, `mode_of_action`, `mode_of_action_target_scope`, molecular targets, resistance mechanisms, producer organisms, activity observations, causal graphs, datasets, or discussions.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml --out /tmp/antibioticmech-chebi-75561-strict.tsv` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. The only diagnostic was the known unrelated CARD `ARO:3000337`/`CHEBI:31724` iclaprim cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed; regenerated the full worklist with the same unrelated CARD diagnostic. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-75561-review-queue.tsv` | Passed; wrote 2,859 `review-readiness` rows. |
| `uv run runoak -i ols:chebi labels CHEBI:75561 CHEBI:22587 CHEBI:64683 CHEBI:75568` | Passed; the live labels resolve to `1-linoleoyl-sn-glycerol`, `antiviral agent`, `1-acyl-sn-glycerol`, and `1-monolinolein`. |
| Live OLS4 term/parent/graph lookups for `CHEBI:75561` | Passed; the term is current and non-obsolete, the direct parents are `CHEBI:64683` and `CHEBI:75568`, and the graph exposes `CHEBI:75563` as the opposite enantiomer. |
| PubChem lookup by InChIKey `WECGLUPZRHILCT-GSNKCQISSA-N` | Passed; resolved CID 6436630 with matching formula `C21H38O4`, Standard InChI, Standard InChIKey, monoisotopic mass, charge 0, and exact ChEBI synonym set. |
| PubMed exact-label search | Passed; 0 results for the exact CHEBI:75561 labels, exact InChIKey, and `HMDB0011568`. |
| Europe PMC exact-label search | Passed but produced no exact support; 11 full-text/tokenized hits surfaced, and none matched the exact CHEBI:75561 labels or identifiers in title, abstract, or keyword metadata. |
| Semantic Scholar exact-label search | Not checked; the public Graph API returned HTTP 429. |
| HMDB cross-reference dereference | Not checked; `https://hmdb.ca/metabolites/HMDB0011568.xml` returned HTTP 403. The HMDB xref was therefore only verified as a live ChEBI OLS database cross-reference on `CHEBI:75561`. Reaxys was likewise treated as a closed-registry ChEBI xref. |

The skill asks for schema, strict, term, reference, and history validation. This repository exposes focused schema validation and strict validation for a single record; term, reference, and history checks for this seeded record are the live identifier checks and direct audit-field inspection above, plus full-corpus reproducibility through `just verify-corpus`.

## Identity and Grounding

The exact identity is internally consistent.

- The YAML `identifier`, `label`, `grounding_status`, and single source concept all denote `CHEBI:75561` / 1-linoleoyl-sn-glycerol.
- The live OLS4 ChEBI term for `CHEBI:75561` is non-obsolete and carries the same formula, Standard InChI, Standard InChIKey, monoisotopic mass, charge, HMDB xref, and Reaxys xref imported into the raw ChEBI inventory.
- PubChem CID 6436630 resolves from the record's exact Standard InChIKey and returns the same Standard InChI, formula `C21H38O4`, charge 0, and monoisotopic mass.
- The record's two `parent_compounds`, `CHEBI:64683` and `CHEBI:75568`, are current direct parents in OLS. They are broader ChEBI terms and therefore fit `parent_compounds`, not `xrefs`.
- OLS exposes `CHEBI:75563`, 3-linoleoyl-sn-glycerol, as the opposite enantiomer of `CHEBI:75561`. The corpus keeps it as a separate record with a different InChIKey, so the stereochemical boundary is preserved.
- The imported class is `ANTIVIRAL` because ChEBI assigns only `CHEBI:22587` as an in-scope antimicrobial role for this source concept. The class follows the repository filing rule and the role remains preserved in `activity_roles`.

The exhaustive local search covered ignored and non-ignored files in `data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml`. It found no prior YAML review report, no grounding/exclusion decision, and no curated exact-structure activity, producer, mechanism, target, resistance, causal-graph, or dataset assertion for `CHEBI:75561`, `antibioticmech:chebi-0a5e8ca954`, `WECGLUPZRHILCT-GSNKCQISSA-N`, `HMDB0011568`, or `reaxys:10115007`.

## Evidence

The existing YAML does not contain claim-level literature evidence.

- Seeded ChEBI identity, role, structure, synonym, parent, and xref fields are provenance-backed by `source_concepts[0]`; these are database assertions from ChEBI, not curator-owned primary-paper claims.
- `data/raw/chebi_antimicrobials.tsv` has no citation PMIDs for `CHEBI:75561` and no `mechanism_role_ids`.
- The regenerated worklist has exactly two rows for this identifier: `mechanism` and `review-readiness`. There are no activity, producer, target, resistance, xref-conflict, span-conflict, or multi-component candidates for this exact ChEBI term.
- An exact PubMed search over `1-linoleoyl-sn-glycerol`, `1-linoleoyl-sn-monoglyceride`, `sn-1-monolinoleoylglycerol`, `1-(9Z,12Z)-octadecadienoyl-sn-glycerol`, `(S)-1-O-linoleoylglycerol`, `(S)-1-monolinolein`, `WECGLUPZRHILCT-GSNKCQISSA-N`, and `HMDB0011568` returned zero PMIDs.
- Europe PMC surfaced 11 results through a broader exact-string query, but title/abstract/keyword inspection showed no exact CHEBI:75561 label or identifier matches. They are not support for an antiviral observation or mechanism on this stereospecific compound.

The sibling/broader `CHEBI:75568` record for 1-monolinolein is a near miss, not evidence for this exact record. Its local ChEBI row carries `PMID:3707358`, `PMID:14661857`, and `PMID:18973338`; the antiviral lead among those is the African swine fever virus paper on monoolein and monolinolein. A future curator may inspect that paper when reviewing `CHEBI:75568`, but it should not be copied onto `CHEBI:75561` unless the source distinguishes this exact S-enantiomer.

## Completeness

The record is structurally grounded but not complete enough for `REVIEWED`.

- Identity and structure are complete enough for a seed review: the exact ChEBI term is live, non-obsolete, stereospecific, and agrees with PubChem on the Standard InChIKey.
- Parentage is complete enough for this review: both listed parents are broader direct ChEBI parents and the enantiomeric sibling is not mis-modeled as an exact xref or parent.
- Classification is seed-supported by ChEBI's antiviral-agent role, but no primary activity paper for exact `CHEBI:75561` was located in the bounded exact-label searches.
- Mechanism is unreviewed and absent. ChEBI supplied no mechanism role, CARD supplies no target or resistance edge for this ChEBI-only antiviral, and there is no curator veto explaining that the mode is unknowable.
- Empty `activity_spectrum`, `producer_organisms`, `molecular_targets`, `resistance_mechanisms`, `causal_graphs`, `datasets`, and `discussions` are structurally allowed. None should be filled from the current seed data without exact primary support.

## Findings

### Blocker

None found.

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| F1 | The exact ChEBI seed has no curator-reviewed antimicrobial mechanism or exact-compound primary support. | The YAML is `SEEDED` with no `mode_of_action`, no `mode_of_action_target_scope`, no `mode_of_action_notes`, no `molecular_targets`, and no `evidence`. `data/raw/chebi_antimicrobials.tsv` gives `CHEBI:75561` no citation PMIDs and no `mechanism_role_ids`; the regenerated worklist places it only in `mechanism` and `review-readiness`. Exact PubMed searches found no hits for its stereospecific labels or identifiers, and the only obvious antiviral publication lead belongs to broader `CHEBI:75568` rather than exact `CHEBI:75561`. | Curator-owned additions on `data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; any generated identity/class correction would instead belong in the ChEBI extractor or `curation/decisions.tsv`. |

### Minor

None found.

## Recommended Edits

1. Keep the generated ChEBI identity, structure, parents, activity role, HMDB xref, Reaxys xref, and source concept unchanged unless a future upstream extraction shows the ChEBI relationship itself was withdrawn or contradicted.
2. Before promoting the record to `REVIEWED`, find primary antiviral evidence for the exact S-enantiomer `CHEBI:75561`, or add a curator-owned mechanism veto if the literature only supports the broader non-stereospecific `CHEBI:75568` term.
3. If exact activity evidence is found, add one `ActivityObservation` per tested virus, cell line, strain, or assay context with its assay, quantitative value and units where reported, and claim-level evidence. Do not generalize parent `1-monolinolein` activity onto this exact record unless the source identifies the S-enantiomer.
4. If exact target or mechanism evidence is found, add a supported `mode_of_action`, `mode_of_action_target_scope`, `MolecularTarget` rows, and an edge-level-evidenced `causal_graph` instead of inferring a mechanism from the ChEBI antiviral role alone.

## Follow-up Checks

| Edit | Proof |
|---|---|
| Add exact activity, target, or mechanism evidence | Re-run `just validate-strict data/antibiotics/antiviral/1-linoleoyl-sn-glycerol.yaml --out /tmp/antibioticmech-chebi-75561-strict.tsv` and confirm every new claim-level object has a stable reference and exact-compound notes. |
| Claim `mode_of_action` or write a mechanism veto | Re-run `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism.tsv` and confirm `CHEBI:75561` no longer appears for an absent or unreviewed mechanism. |
| Add any curator-owned YAML change | Re-run `just verify-corpus --summary` and inspect the diff to confirm only curated, seed-preserved fields and the audit trail changed. |
| Move the record to `REVIEWED` | Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`; the record should leave the queue only after identity, structure, class, and at least mode of action have all been curator-checked. |

## Additional Notes

- The ignored-inclusive local search also matched unrelated numeric text, such as FDA application `075561` on the chlorhexidine gluconate record, and nearby ChEBI records `CHEBI:75563` and `CHEBI:75568`. Those are not duplicates of `CHEBI:75561`.
- PubChem synonym retrieval for CID 6436630 returned `CHEBI:75561` and the exact ChEBI synonyms now on the record, further supporting the exact identity.
- The OLS graph contains an `is enantiomer of` edge between `CHEBI:75561` and `CHEBI:75563`; those two should stay split unless ChEBI itself changes their stereochemical modeling.
- No report section required a YAML edit. Leaving optional fields empty is preferable to adding unsourced parent-compound activity or a mechanism inferred from an antiviral-agent role.

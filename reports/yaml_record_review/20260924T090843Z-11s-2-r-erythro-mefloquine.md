# YAML Record Review: (−)-(11S,2'R)-erythro-mefloquine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml`
- Started UTC: 2026-09-24T09:08:12Z
- Finished UTC: 2026-09-24T09:08:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml` |
| Class | `ANTIPROTOZOAL` |
| Identifier | `CHEBI:63687` |
| Label | `(−)-(11S,2'R)-erythro-mefloquine` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | ChEBI `CHEBI:63687`, version `2026-08-30`, minted key `antibioticmech:chebi-21aa4c1950` |
| Standard InChIKey | `XEEQGYMUWCZPDN-DOMZBBRYSA-N` |
| Xrefs | `cas:51742-87-1`, `lincs.smallmolecule:LSM-5525`, `reaxys:5629059` |

`11s-2-r-erythro-mefloquine.yaml` is a generated exact ChEBI record for the
`(11S,2'R)` enantiomer of mefloquine. Its generated content contains ChEBI-owned
identity, structure, parentage, xrefs, and an antimalarial role. It contains no
record-level evidence, curated `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `activity_spectrum`, `resistance_mechanisms`,
`producer_organisms`, `clinical_status`, `causal_graphs`, `datasets`, or
`discussions`.

## Validation

| Command or check | Result |
|---|---|
| `find . -name AGENTS.md -print` | Passed before review; no local `AGENTS.md` files were present. `find` included hidden and ignored paths. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; `CHEBI:63687` is row 138 of the scientific read-only review queue after the already reviewed chartaceone C/D/E/F block. |
| `just validate data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml --out /tmp/11s-2-r-erythro-mefloquine-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2939 expected records were present on disk with no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` drift, and the known unrelated `ARO:3000337` iclaprim cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/11s-2-r-erythro-mefloquine-worklist.tsv` | Passed; exact `CHEBI:63687` appeared on `mechanism` and `review-readiness`. The `mechanism` row reported 0 CARD targets and 0 resistance edges to build on. The only diagnostic was the known unrelated `ARO:3000337`/iclaprim cross-reference refusal. |
| `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'antibioticmech:chebi-21aa4c1950' -e '11s-2-r-erythro-mefloquine' -e 'XEEQGYMUWCZPDN-DOMZBBRYSA-N' -e '51742-87-1' -e '5629059' data/antibiotics data/raw curation reports/yaml_record_review .claude docs README.md conf src scripts tests` | Passed; this wider ignored/hidden-inclusive search found the exact generated YAML, ChEBI raw row, PATHS lock row, review-queue row, and sibling notes in the `CHEBI:63684` opposite-enantiomer review. It found no curator-owned activity, target, resistance, producer, or causal-graph claim for exact `CHEBI:63687`. |
| `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'antibioticmech:chebi-21aa4c1950' curation/decisions.tsv` | Passed; the ignored/hidden-inclusive search found no local grounding decision overriding exact ChEBI ownership. |
| `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'XEEQGYMUWCZPDN-DOMZBBRYSA-N' -e '51742-87-1' -e '5629059' data/raw/bindingdb_target_measurements.tsv data/raw/fda_clinical_status.tsv data/raw/mibig_producers.tsv data/raw/phibase_amr.tsv` | Passed; the ignored/hidden-inclusive search found no local BindingDB, Drugs@FDA, MIBiG, or PHI-base row for exact `CHEBI:63687` or its structure/xref identifiers. |
| OLS4 lookup for `CHEBI:63687` | Passed; OLS resolved exactly one non-obsolete ChEBI class with the same identifier, ASCII-equivalent label, definition, and synonyms. |
| ChEBI page lookup for `CHEBI:63687` | Passed; current ChEBI agreed with the generated label, 3-star status, definition, IUPAC synonym, formula, charge, average mass, monoisotopic mass, SMILES, Standard InChI, Standard InChIKey, LINCS xref, CAS number, Reaxys registry number, `CHEBI:38068` antimalarial role, `CHEBI:63681` parent, and `CHEBI:63684` opposite-enantiomer relation. |
| PubMed/Semantic Scholar search for `CHEBI:63687`, `XEEQGYMUWCZPDN-DOMZBBRYSA-N`, `51742-87-1`, `5629059`, and `(-)-Mefloquine` | Partial pass; PubMed returned 20 mostly generic mefloquine leads, while Semantic Scholar returned an invalid response. |
| PubMed/Semantic Scholar search for `(11S,2'R)-erythro-mefloquine OR (-)-mefloquine Plasmodium mechanism` | Partial pass; PubMed returned 0 candidates, while Semantic Scholar returned HTTP 429. |
| PubMed/Semantic Scholar exact-identifier search for `CHEBI:63687`, `XEEQGYMUWCZPDN-DOMZBBRYSA-N`, `51742-87-1`, `5629059`, and `"(11S,2R)-2,8-bis"` | Partial pass; PubMed returned one unrelated `PMID:5629059` false positive caused by the numeric Reaxys registry number, while Semantic Scholar returned an invalid response. |
| Reaxys xref `5629059` | Not independently checked: ChEBI lists this Reaxys registry number on exact `CHEBI:63687`, but Reaxys had no public resolver available in this workflow. |

No separate focused term, reference, or history validator is exposed in
`justfile`; the full-corpus `verify-corpus` and `worklist` checks above are the
documented narrow checks for seeded-field drift and queue placement.

## Identity and Grounding

| Assertion | Review |
|---|---|
| Label and identifier | Supported. OLS resolves `CHEBI:63687` to the ASCII-equivalent `(-)-(11S,2'R)-erythro-mefloquine`, and the current ChEBI compound page resolves the same accession to the same exact enantiomer. |
| Structure | Supported. The generated SMILES, Standard InChI, Standard InChIKey `XEEQGYMUWCZPDN-DOMZBBRYSA-N`, formula `C17H16F6N2O`, charge `0`, average mass `378.316`, and monoisotopic mass `378.11668` match both `data/raw/chebi_antimicrobials.tsv` and current ChEBI for `CHEBI:63687`. |
| Source concept | Supported. The only source concept is ChEBI `CHEBI:63687`; no ARO, curator, BindingDB, MIBiG, FDA, or PHI-base source row is attached to this record. |
| Filing class and role | Supported as a ChEBI role. `activity_roles` contains `CHEBI:38068`, and current ChEBI classifies exact `CHEBI:63687` as an antimalarial. `ANTIPROTOZOAL` is the expected filing class for a ChEBI antimalarial role. |
| Parent term | Supported. Current ChEBI attaches exact `CHEBI:63687` to `CHEBI:63681` by `is a`, matching the generated `parent_compounds` field. |
| Enantiomer boundary | Supported. Current ChEBI states that `CHEBI:63687` is the enantiomer of `CHEBI:63684`, and the two adjacent inventory rows share formula and neutral charge but differ in SMILES, Standard InChI stereochemistry, InChIKey, CAS, and Reaxys xrefs. |
| Xrefs | Supported as ChEBI assertions. Current ChEBI lists LINCS `LSM-5525`, CAS `51742-87-1`, and Reaxys `5629059` on exact `CHEBI:63687`, matching the generated xrefs. |
| Grounding decision | Complete as empty. Exact ChEBI source concepts ground to their own CURIEs, and an ignored/hidden-inclusive search found no `curation/decisions.tsv` override for `CHEBI:63687` or `antibioticmech:chebi-21aa4c1950`. |

The record denotes the ChEBI-grounded `(11S,2'R)` erythro mefloquine enantiomer,
not the `CHEBI:63609` racemate and not the `CHEBI:63684` opposite enantiomer.

## Evidence

| Claim in generated YAML | Support |
|---|---|
| `(-)-(11S,2'R)-erythro-mefloquine` is a ChEBI-grounded exact record with the listed IUPAC name, exact structure, broader parent, LINCS xref, CAS, and Reaxys registry number. | Supported by the committed ChEBI inventory row for `CHEBI:63687` and by the current ChEBI page for the same term. |
| Exact `CHEBI:63687` has a ChEBI antimalarial role. | Supported by the committed ChEBI row and by current ChEBI, both of which list `CHEBI:38068` on exact `CHEBI:63687`. |
| The mechanism of action is unknown. | Supported as part of the ChEBI definition string inherited into the generated `definition`, but not promoted to any curator-owned mechanistic field. |

No unsupported claim-level citation was found because no `MolecularTarget`,
`ResistanceMechanism`, `ActivityObservation`, `ProducerOrganism`, or
`CausalEdge` is populated on `11s-2-r-erythro-mefloquine.yaml`.

The local BindingDB, FDA, MIBiG, and PHI-base inventories have no row for exact
`CHEBI:63687`, Standard InChIKey `XEEQGYMUWCZPDN-DOMZBBRYSA-N`, CAS
`51742-87-1`, or Reaxys `5629059`. Those absence checks included ignored and
hidden files.

The bounded publication searches did not resolve a primary mechanism or target
for exact `CHEBI:63687`. The broad identity query returned generic recent
mefloquine leads, and the exact identifier query returned only unrelated
`PMID:5629059`, a false positive from the bare Reaxys registry number matching
a PubMed identifier.

## Completeness

| Area | Status |
|---|---|
| Identity and structure | Complete enough for read-only review; current ChEBI, the committed ChEBI row, `PATHS.tsv`, and the generated YAML agree on exact `CHEBI:63687` and `XEEQGYMUWCZPDN-DOMZBBRYSA-N`. |
| Source concept | Complete. The only source concept is exact `CHEBI:63687`. |
| Mechanism | Incomplete. The record has no `mode_of_action`, no `mode_of_action_target_scope`, no `molecular_targets`, and no causal graph. ChEBI itself describes the antimalarial mechanism as unknown. |
| Activity observations | Complete as empty for the inspected evidence. The generated record has a ChEBI antimalarial role but no assay-level source with an organism, assay, value, or units that could support an `ActivityObservation`. |
| Resistance mechanisms | Complete as empty. CARD contributes no ARO resistance edges to this ChEBI-only record, and no PHI-base row names exact `CHEBI:63687`. |
| Producers | Complete as empty. MIBiG contributes no exact producer row for this InChIKey. |
| Clinical status | Complete as empty. Drugs@FDA contributes no exact GSRS/UNII row for this InChIKey. |
| Datasets | Complete as empty for the inspected evidence. The generated record has no dataset assertion, and the ChEBI/PubMed checks did not expose a specific exact-enantiomer dataset to add. |
| Discussions | Complete as empty for current read-only review. The absent mechanism is already represented by the derived `mechanism` and `review-readiness` queues. |

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found. | The YAML validates, the corpus reproduces exactly, current ChEBI agrees with the exact identity and structure, and the record does not conflate the `(11S,2'R)` enantiomer with racemic mefloquine or `CHEBI:63684`. | Not applicable. |
| Major | Exact `CHEBI:63687` remains a source-seeded antimalarial structure with no curated mode of action, molecular target, organismal activity observation, or causal graph. | The generated record has 0 record evidence items and no `mode_of_action`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, or `causal_graphs`; exact `CHEBI:63687` is on the `mechanism` and `review-readiness` queues with 0 CARD targets and 0 CARD resistance edges. ChEBI's own definition says the racemic drug's mechanism is unknown, and the exact-enantiomer literature searches did not resolve a specific mechanism. | Future curator-owned fields on `data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI changes this term's role, parentage, xrefs, or source PMIDs, `data/raw/chebi_antimicrobials.tsv` and the ChEBI extractor own the refresh. |
| Minor | `reaxys:5629059` is an unchecked direct Reaxys identity in this review. | The generated xref matches the committed ChEBI inventory row and current ChEBI's Reaxys registry number on exact `CHEBI:63687`, but Reaxys itself had no public resolver available here to verify same-structure semantics directly. | ChEBI extractor and `data/raw/chebi_antimicrobials.tsv`; future curation should either verify this source externally or preserve it as an upstream ChEBI assertion. |

## Recommended Edits

1. Leave `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
   and `causal_graphs` empty until a curator inspects primary literature that
   supports an exact-enantiomer mechanism for `CHEBI:63687`, racemic mefloquine,
   or a safely transferable arylamino-alcohol class.
2. Review PfMDR1, heme, hemozoin, and beta-hematin primary literature only as
   discovery leads. Do not attach a mechanism or target to the `(11S,2'R)`
   enantiomer unless the inspected paper's compound scope supports that exact
   structure or a deliberate racemate-to-enantiomer curation decision.
3. If exact-enantiomer mechanism evidence remains genuinely unresolved after
   primary-paper review, add a scoped `Discussion` that records what was
   checked, why the racemate/enantiomer boundary matters, and what evidence
   would resolve it.
4. If a mode of action or target is supported, write it with a guarded mutator
   that asserts `identifier == "CHEBI:63687"`, updates only the curator-owned
   mechanism fields, appends a `codex` `CurationEvent` with
   `llm_assisted: true`, and emits via `write_validated_antibiotic`.
5. Move `curation_status` to `REVIEWED` only after identity, structure, filing
   class, and the newly curated mode of action satisfy the `docs/CURATION.md`
   sign-off criteria.

## Follow-up Checks

After a future mechanism curation edit:

1. `just validate-strict data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml --out /tmp/11s-2-r-erythro-mefloquine-strict.tsv`
2. `just verify-corpus`
3. `just qc`
4. `git diff -- data/antibiotics/antiprotozoal/11s-2-r-erythro-mefloquine.yaml curation/decisions.tsv src scripts tests`
5. `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

Rerun exact ignored-inclusive searches for `CHEBI:63687`,
`antibioticmech:chebi-21aa4c1950`, `XEEQGYMUWCZPDN-DOMZBBRYSA-N`, `51742-87-1`,
and `5629059` to confirm future evidence still lands on the exact `(11S,2'R)`
structure and not on racemic mefloquine or the `CHEBI:63684` enantiomer.

## Additional Notes

Searches used to establish absence included ignored and hidden files:

- `find . -name AGENTS.md -print`
- `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'antibioticmech:chebi-21aa4c1950' -e '11s-2-r-erythro-mefloquine' -e 'XEEQGYMUWCZPDN-DOMZBBRYSA-N' -e '51742-87-1' -e '5629059' data/antibiotics data/raw curation reports/yaml_record_review .claude docs README.md conf src scripts tests`
- `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'antibioticmech:chebi-21aa4c1950' curation/decisions.tsv`
- `rg --no-ignore --hidden -n -e 'CHEBI:63687' -e 'XEEQGYMUWCZPDN-DOMZBBRYSA-N' -e '51742-87-1' -e '5629059' data/raw/bindingdb_target_measurements.tsv data/raw/fda_clinical_status.tsv data/raw/mibig_producers.tsv data/raw/phibase_amr.tsv`

`runoak` was not present on the shell `PATH`, so this pass used OLS4 and ChEBI
HTTP lookups directly. `NCBI_EMAIL` was unset for PubMed searches. Semantic
Scholar returned HTTP 429 or an invalid response for the targeted publication
searches, so that provider's literature leads were not available in this pass.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.

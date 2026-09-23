# YAML Record Review: (R,R,R)-α-tocopherol

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml
- Started UTC: 2026-09-23T14:11:18Z
- Finished UTC: 2026-09-23T14:11:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:18145 |
| Label | (R,R,R)-α-tocopherol |
| Path | data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml |
| Class | ANTIVIRAL |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:18145, source version 2026-08-30 |
| Standard InChIKey | GVJHHUAWPYXKBD-IEOSBIPESA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to
`data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml`.
An ignored-file-inclusive search for `CHEBI:18145`, `(R,R,R)-α-tocopherol`,
`alpha-tocopherol`, and `tocopherol` across `data`, `curation`, and `reports`
found the target, its `PATHS.tsv` row, the ChEBI raw row, and
`curation/record_review_queue.tsv`. The same search found no prior
`reports/yaml_record_review/` report for this stem or identifier.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml --out /tmp/r-r-r-alpha-tocopherol-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/r-r-r-alpha-tocopherol-worklist.tsv` | Passed; `CHEBI:18145` appears only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 136` | Passed; `CHEBI:18145` is the first queue row after already reviewed `(R)-tosufloxacin`. |
| `just lint` | Passed; `ruff` reported `All checks passed!`. |

`just verify-corpus` and `just worklist` both emitted the known CARD
`ARO:3000337` / iclaprim cross-reference refusal; that warning is unrelated to
this ChEBI-only record.

The repository exposes `validate`, `validate-strict`, `verify-corpus`,
`worklist`, `review-queue`, and `lint`; it does not expose narrower
single-record term, reference, or history validators for a plain ChEBI-seeded
record with no record-level citations.

## Identity and Grounding

The ChEBI identity is exact. OLS4 resolves `CHEBI:18145` to
`(R,R,R)-alpha-tocopherol` with the same SMILES, Standard InChI, Standard
InChIKey, formula, charge, average mass, and monoisotopic mass carried by the
local raw ChEBI row and generated record.

The stereochemical boundary is correct:

- `CHEBI:22470` is the broader `alpha-tocopherol` parent.
- `CHEBI:18145` is the R,R,R stereoisomer and has InChIKey
  `GVJHHUAWPYXKBD-IEOSBIPESA-N`.
- OLS4 lists `CHEBI:46430`, `(S,S,S)-alpha-tocopherol`, as a related ChEBI
  term. That mirror stereoisomer is correctly not present as an exact xref.

The generated activity filing is consistent with the imported source assertion.
OLS4 returns the generic `CHEBI:22587` antiviral-agent relation for
`CHEBI:18145`, and `data/raw/chebi_role_names.tsv` names `CHEBI:22587` as
`antiviral agent`.

The generated xrefs are source-owned ChEBI database cross-references that denote
`(R,R,R)-α-tocopherol` or the common `alpha-tocopherol` registry identity.
However, two ChEBI synonyms imported as `EXACT_SYNONYM` are broader than this
single stereoisomer:

- `alpha-Tocopherol` is the label of the broader parent `CHEBI:22470`.
- `Vitamin E` is a vitamin-family common name and not a one-structure name.

Both strings originate in the local ChEBI raw row as `SYNONYM=` values and in
OLS4 as related synonyms for `CHEBI:18145`. They should not be presented as
exact names of the R,R,R stereoisomer.

## Evidence

This record has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, and
no `causal_graphs`. That is structurally valid for a ChEBI-seeded entry, but it
means the antiviral claim has only upstream database provenance and no
primary-paper support for a compound-specific antiviral mechanism.

The local raw ChEBI row carries 10 PMID discovery leads. PubMed ESummary
resolved all 10; their titles point to α-tocopherol formulation, transfer
protein structural biology, stereoisomer bioavailability, lipoprotein
distribution, milk composition, livestock stereoisomer use, and vitamin E
osteoarthritis surveillance rather than antiviral mechanism or antiviral
activity experiments. OLS4 now lists four additional ChEBI entry PMIDs, but
their titles likewise resolve to α-tocopherol transfer-protein or milk
composition studies rather than antiviral mechanism.

Bounded PubMed checks did not identify exact identifier evidence:

- Identifier query:
  `"GVJHHUAWPYXKBD-IEOSBIPESA-N"[All Fields] OR "CHEBI:18145"[All Fields]`.
  PubMed returned zero results.
- Exact-name query:
  `(R,R,R)-alpha-tocopherol`, `(R,R,R)-α-tocopherol`,
  `RRR-alpha-tocopherol`, `RRR-α-tocopherol`, `all-R-alpha-tocopherol`, and
  `all-R-α-tocopherol` in PubMed title or abstract fields. PubMed normalized
  punctuation and α/alpha spelling, broadening this to 290 α-tocopherol
  results.
- Broad antiviral query:
  `("alpha-tocopherol"[Title/Abstract] OR "α-tocopherol"[Title/Abstract] OR "vitamin E"[Title/Abstract]) AND (antiviral[Title/Abstract] OR virus[Title/Abstract] OR viral[Title/Abstract] OR HIV[Title/Abstract] OR influenza[Title/Abstract] OR herpes[Title/Abstract])`.
  PubMed returned 677 broad vitamin E or α-tocopherol antiviral leads; the
  first 10 were nutrition, formulation, vaccine, immune-response, micelle, Zika
  deficiency, and Mendelian-randomization papers rather than exact
  `CHEBI:18145` mechanism papers.

The broad α-tocopherol and vitamin E searches are useful future discovery
context. They should not be projected onto this exact record unless a curator
inspects primary sources that support measured antiviral activity or mechanism
for the R,R,R structure, or justify projecting a racemic, vitamin-family, or
formulation observation onto this stereoisomer.

Semantic Scholar was not needed after the exact PubMed identifier check found
no `CHEBI:18145` or Standard InChIKey hit and the ChEBI PMID leads did not
surface antiviral mechanism papers. Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, parent boundary, structure
fields, filing class, and history are sufficient for a ChEBI-seeded entry apart
from the over-exact broad synonyms described above.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent. This record should remain below `REVIEWED` until
  a curator either adds evidence that supports an antiviral mechanism for exact
  `(R,R,R)-α-tocopherol` or adds a curator-owned veto explaining why only broad
  α-tocopherol, vitamin E, or formulation leads exist.
- `activity_spectrum` is absent. Future curation should use actual measured
  virus or infected-cell context, assay, value, qualifier, units, compound
  form, and evidence rather than generalizing from vitamin E deficiency or
  supplement studies.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD target or resistance edge was available for
  this exact ChEBI antiviral record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: no regulatory source was imported for this
  exact ChEBI record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no reviewed mechanism for exact `(R,R,R)-α-tocopherol`. | `just worklist --limit 0 --tsv /tmp/r-r-r-alpha-tocopherol-worklist.tsv` lists `CHEBI:18145` in `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and in `review-readiness` with `MECHANISM_REVIEW: mechanism is absent; 10 source literature lead(s), 0 record evidence item(s), 0 target(s)`; exact PubMed identifier searching found no `CHEBI:18145` or InChIKey hit. | Add an evidence-backed curator-owned mechanism to `data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml` through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unknown for this stereoisomer. |
| Minor | Two broad ChEBI synonyms are imported as exact synonyms of a single stereoisomer. | The generated record marks `alpha-Tocopherol` and `Vitamin E` as `EXACT_SYNONYM`; OLS4 identifies `CHEBI:22470` as the broader `alpha-tocopherol` parent of `CHEBI:18145`, and `Vitamin E` is a vitamin-family name rather than the exact R,R,R structure. | Preserve ChEBI synonym scope in `scripts/extract_source_inventory.py` and `scripts/seed_from_sources.py`, or add source-concept-specific synonym exclusions under `conf/sources.yaml`. |

No blockers found.

## Recommended Edits

1. Inspect the broad α-tocopherol and vitamin E antiviral PubMed leads for
   primary activity or mechanism evidence. Curate this record only when a source
   supports exact `(R,R,R)-α-tocopherol` or justifies projecting a broader
   α-tocopherol, vitamin E, supplement, or formulation observation onto this
   stereoisomer.
2. Add a `CURATOR:`-owned mechanism, molecular target, and causal graph when
   evidence is exact enough; otherwise leave a curator-owned veto documenting
   that no exact-stereoisomer antiviral mechanism was found.
3. Add only measured antiviral `activity_spectrum` rows with complete virus or
   infected-cell context, assay, value, units, compound form, and evidence.
4. Stop treating broad ChEBI related synonyms as exact: either preserve ChEBI
   synonym scope during extraction and seeding, or exclude the broad
   `alpha-Tocopherol` and `Vitamin E` strings for `CHEBI:18145`.

## Follow-up Checks

- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/r-r-r-alpha-tocopherol-worklist.tsv`,
  and `just lint`.
- After any synonym-scope change, run `just seed`, a `just seed-canary
  CHEBI:18145`, `just validate-strict
  data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml --out
  /tmp/antibioticmech-record-validation.tsv`, `just verify-corpus --summary`,
  and `just lint`.
- Re-run OLS4 checks for `CHEBI:18145`, `CHEBI:22470`, `CHEBI:22587`, and
  `CHEBI:46430` if future edits touch identity, xrefs, role terms, or
  parentage.

## Additional Notes

- The ignored-inclusive resolution search found `CHEBI:18145` in
  `data/raw/chebi_antimicrobials.tsv`, `data/antibiotics/PATHS.tsv`,
  `data/antibiotics/antiviral/r-r-r-α-tocopherol.yaml`, and
  `curation/record_review_queue.tsv`, and found no prior `CHEBI:18145`,
  `r-r-r-α-tocopherol`, `alpha-tocopherol`, or `tocopherol` review report under
  `reports/yaml_record_review/`.
- The OLS4 relation endpoint for `CHEBI:18145` also surfaced antioxidant,
  micronutrient, protein kinase C inhibitor, anticoagulant, nutraceutical,
  immunomodulator, antiatherogenic, plant-metabolite, and algal-metabolite
  roles. Those non-antimicrobial roles are correctly absent from this
  AntibioticMech seed.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:18145` was absent from all inspected queues except `mechanism` and
  `review-readiness`.

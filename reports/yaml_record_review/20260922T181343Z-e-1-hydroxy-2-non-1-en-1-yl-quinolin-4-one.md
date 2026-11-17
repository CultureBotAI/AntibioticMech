# YAML Record Review: (E)-1-hydroxy-2-(non-1-en-1-yl)quinolin-4-one

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml`
- Started UTC: 2026-09-22T18:10:00Z
- Finished UTC: 2026-09-22T18:13:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:137441` |
| Label | `(E)-1-hydroxy-2-(non-1-en-1-yl)quinolin-4-one` |
| Path | `data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:137441`, version `2026-08-30`, minted key `antibioticmech:chebi-3ea7ed25b5` |
| Source role | `CHEBI:33282` antibacterial agent |
| Parent compounds | `CHEBI:23765` quinolone; `CHEBI:24709` hydroxylamines; `CHEBI:27171` organic heterobicyclic compound; `CHEBI:78840` olefinic compound |
| Structure | `LOUOCBKBIWBTTR-DHZHZOJOSA-N`; formula `C18H23NO2`; charge `0` |
| Xrefs | None |
| Document xrefs | None |
| Source literature leads | `PMID:15144975`; `PMID:28523838` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(E)-1-hydroxy-2-(non-1-en-1-yl)quinolin-4-one`, also called
`trans-N-hydroxy-Δ1-2-(non-1-enyl)-4-quinolone`. The YAML has exact ChEBI
grounding, the ChEBI definition, two ChEBI synonyms, four ChEBI parents, the
antibacterial ChEBI role, structure, and source-concept metadata. It has no
xrefs, document xrefs, generated or curator-owned mode of action, molecular
target, activity observation, producer organism, resistance mechanism, dataset,
discussion, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml --out /tmp/antibioticmech-chebi-137441-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-137441-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:137441` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just review-queue --limit 88` | Pass: `CHEBI:137441` is queued with `MECHANISM_REVIEW: mechanism is absent; 2 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:137441` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label `(E)-1-hydroxy-2-(non-1-en-1-yl)quinolin-4-one`, the same
definition, the exact Standard InChIKey `LOUOCBKBIWBTTR-DHZHZOJOSA-N`, formula
`C18H23NO2`, neutral charge, matching average and monoisotopic masses, the same
SMILES, and the same `PMID:15144975` and `PMID:28523838` source xrefs.

The generated YAML stores two source ChEBI synonyms:
`1-hydroxy-2-[(1E)-non-1-en-1-yl]quinolin-4(1H)-one` and
`trans-N-hydroxy-Δ1-2-(non-1-enyl)-4-quinolone`. OLS exposes the IUPAC synonym
twice and exposes the `trans-N-hydroxy-Delta(1)-2-(non-1-enyl)-4-quinolone`
spelling once; the local seeder correctly de-duplicates the IUPAC string and
preserves the Greek-Delta spelling from the committed ChEBI inventory.

The live OLS graph gives `CHEBI:137441` four direct parents: `CHEBI:23765`,
`quinolone`; `CHEBI:24709`, `hydroxylamines`; `CHEBI:27171`,
`organic heterobicyclic compound`; and `CHEBI:78840`, `olefinic compound`. The
live OLS `has_role` relation gives the term two roles: `CHEBI:33282`,
`antibacterial agent`, and `CHEBI:76969`, `bacterial metabolite`. Only
`CHEBI:33282` is an antimicrobial role in `conf/sources.yaml`, and the
committed source configuration maps that role to generated filing class
`ANTIBACTERIAL`.

The committed ChEBI inventory row for `CHEBI:137441` has the same label,
definition, 3-star status, antibacterial role, parents, SMILES, Standard InChI,
Standard InChIKey, formula, neutral charge, masses, synonyms, and source PubMed
identifiers that were used to seed this record. `PATHS.tsv` maps
`CHEBI:137441` to
`ANTIBACTERIAL/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one`, matching the
generated path and filing class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:137441`, the exact file stem, the exact label, both generated synonyms,
the exact minted key, and the exact Standard InChIKey across
`reports/yaml_record_review`, `data/antibiotics`, `data/raw`, `curation`,
`conf`, `.claude`, `CLAUDE.md`, and `justfile` found only the expected
generated YAML, `PATHS.tsv` row, raw ChEBI row, and
`record_review_queue.tsv` row for exact `CHEBI:137441`. An ignored-inclusive
filename search for `*quinolin*` under `reports/yaml_record_review` found no
prior report for this record.

## Evidence

The record's antibacterial classification is inherited from committed ChEBI role
`CHEBI:33282`, `antibacterial agent`. `data/raw/chebi_role_names.tsv` marks
that role as a ChEBI scope role, and `conf/sources.yaml` maps it to generated
class `ANTIBACTERIAL`. That role is enough for reproducible source-level filing
but not enough to fill a specific activity observation, producer assertion,
mode of action, target, or causal graph.

Both ChEBI source PMIDs resolve to the intended literature. `PMID:15144975`,
titled `Electrospray/mass spectrometric identification and analysis of
4-hydroxy-2-alkylquinolines (HAQs) produced by Pseudomonas aeruginosa`, reports
LC/MS detection of 56 HAQs and related compounds in `Pseudomonas aeruginosa`
PA14 culture supernatant and ties HAQ N-oxides to `pqsL`, but the PubMed
abstract does not name exact
`(E)-1-hydroxy-2-(non-1-en-1-yl)quinolin-4-one` or report a susceptibility
assay endpoint for it.

`PMID:28523838`, titled `An Unsaturated Quinolone N-Oxide of Pseudomonas
aeruginosa Modulates Growth and Virulence of Staphylococcus aureus`, is exact
for this record. Its abstract reports synthesis of the previously proposed
unsaturated compound, confirmation in `Pseudomonas aeruginosa` culture extracts,
assignment as `trans-Δ1-2-(non-1-enyl)-4-quinolone N-oxide`, activity against
`Staphylococcus aureus` including MRSA strains, inactivity of the cis isomer,
small-colony-variant induction, hemolysis reduction, and nitrate-reductase
inhibition under anaerobic conditions. The abstract does not provide exact
MICs, strain identifiers, dose values, or a target relation strong enough to
write a claim-level `MolecularTarget` without the full text.

The exact-label/synonym/Pseudomonas/Staphylococcus publication-helper query
returned zero PubMed candidates and Semantic Scholar returned HTTP 429. The
bounded search therefore found no immediate primary-paper lead beyond
`PMID:15144975` and `PMID:28523838` for exact-compound activity, producer,
mechanism, target, resistance, dataset, clinical, or causal-graph assertions.

## Completeness

The record is incomplete as a reviewed antibacterial AQNO record. It has exact
ChEBI identity, structure, parentage, source-level antibacterial
classification, exact primary-paper activity support, and reproducible source
metadata, but no curated activity observation, producer assertion,
mode-of-action, molecular-target, or causal-graph claim.

The empty `activity_spectrum` and `producer_organisms` slots are actionable for
a future curation pass. The ChEBI definition and `PMID:28523838` both support
production by `Pseudomonas aeruginosa`, and `PMID:28523838` supports exact
anti-`Staphylococcus aureus` activity including activity against MRSA strains at
abstract level. Full-text review should recover the source strain, target
strains, assay formats, and quantitative values before any claim-level rows are
added.

The empty `mode_of_action`, `molecular_targets`, and causal-graph slots are
acceptable for the current seed but incomplete for review. `PMID:28523838`
reports nitrate reductase inhibition under anaerobic conditions at abstract
level; the full text must be checked for exact enzyme identity, assay context,
directness of the inhibitor-target relation, dose, and whether this target is
enough to support a full antimicrobial mechanism graph.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`, and
`discussions` slots are acceptable for the current seed. No measured resistance
edge, standalone clinical status assertion, public dataset accession, or
discussion-worthy identity conflict was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:137441` has exact primary-paper support for Pseudomonas production and anti-Staphylococcus activity, but no curator-owned activity, producer, mode-of-action, target, or causal-graph claim. | The generated record has two source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero `producer_organisms`, zero targets, and no `mode_of_action`. `just worklist` places the record on `mechanism`, `producer-candidate`, and `review-readiness`. The abstract for exact source `PMID:28523838` supports culture-extract presence, anti-`Staphylococcus aureus` activity, and nitrate-reductase inhibition for exact `trans-Δ1-2-(non-1-enyl)-4-quinolone N-oxide`. | Future curator-owned fields on `data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Review the full text of `PMID:28523838`. If it reports exact MICs,
   growth-inhibition values, small-colony-variant concentrations, nitrate
   reductase inhibition values, or other quantitative measurements, add
   claim-level `ActivityObservation` entries with organism, strain, assay,
   value, unit, and evidence details.
2. In the same full text, verify the `Pseudomonas aeruginosa` strain or culture
   extract that contained exact `CHEBI:137441`. Add a `ProducerOrganism` entry
   only when the source supports biosynthesis or detection for this exact
   trans unsaturated AQNO.
3. Review whether `PMID:28523838` supplies direct evidence for a curated
   `MolecularTarget` or `mode_of_action` assignment around nitrate reductase or
   anaerobic respiration. Leave `mode_of_action`, `molecular_targets`, and the
   causal graph empty unless exact-compound primary evidence supports each
   mechanistic claim.
4. Treat `PMID:15144975` as a Pseudomonas HAQ/AQNO production and discovery
   lead unless its full text reports exact `CHEBI:137441`; do not use its broad
   abstract-level N-oxide statements as exact activity or target evidence.
5. Leave source-owned ChEBI identity, structure, role, parent, and synonym fields
   untouched unless the committed ChEBI inventory diverges from OLS or a curator
   decision needs to exclude a proven wrong source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml`
2. `just validate-strict data/antibiotics/antibacterial/e-1-hydroxy-2-non-1-en-1-yl-quinolin-4-one.yaml --out /tmp/antibioticmech-chebi-137441-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-137441-worklist.tsv`
5. `just review-queue --limit 88`
6. `just qc`

Manually compare any future activity, producer, mode-of-action, target, dataset,
discussion, or causal-graph assertion against exact `CHEBI:137441` identity.
Confirm that every claim-level evidence block attaches to the specific object it
supports, not only to the whole ChEBI term, a Pseudomonas HAQ class, a generic
AQNO N-oxide biosynthesis statement, or the source antibacterial-agent role.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden` or `find`, so
they included ignored `reports/` files.

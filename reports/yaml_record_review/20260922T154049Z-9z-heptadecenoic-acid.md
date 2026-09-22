# YAML Record Review: (9Z)-heptadecenoic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml`
- Started UTC: 2026-09-22T15:39:37Z
- Finished UTC: 2026-09-22T15:40:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:84328` |
| Label | `(9Z)-heptadecenoic acid` |
| Path | `data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:84328`, version `2026-08-30`, minted key `antibioticmech:chebi-b4d4325f85` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:36001` heptadecenoic acid; `CHEBI:59202` straight-chain fatty acid |
| Structure | `QSBYPNXLFMSGKH-HJWRWDBZSA-N`; formula `C17H32O2`; charge `0` |
| Xrefs | `cas:1981-50-6`; `reaxys:1726108` |
| Document xrefs | `patent:EP0690710`; `patent:US5708028`; `patent:WO9421247` |
| Source literature leads | `PMID:11157268`; `PMID:14263140`; `PMID:1854634` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(9Z)-heptadecenoic acid`, a neutral cis-heptadecenoic fatty acid filed as
antifungal through the committed ChEBI role `CHEBI:35718`. The YAML has exact
ChEBI grounding, the ChEBI definition, two exact ChEBI synonyms, two ChEBI
parents, two ChEBI database xrefs, three ChEBI document xrefs, structure, and
source-concept metadata. It has no generated or curator-owned mode of action,
molecular target, activity observation, producer organism, resistance
mechanism, dataset, discussion, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml --out /tmp/antibioticmech-chebi-84328-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-84328-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:84328` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 75` | Pass: `CHEBI:84328` is queued with `MECHANISM_REVIEW: mechanism is absent; 3 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:84328` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label `(9Z)-heptadecenoic acid`, the same definition, the exact
Standard InChIKey `QSBYPNXLFMSGKH-HJWRWDBZSA-N`, the exact formula `C17H32O2`,
neutral charge, matching average and monoisotopic masses, and the exact SMILES
stored by this generated record.

The generated YAML stores OLS' two non-duplicate exact synonyms,
`(9Z)-heptadec-9-enoic acid` and `cis-9-heptadecenoic acid`. OLS also exposes
the same `cas:1981-50-6`, `reaxys:1726108`, and three patent xrefs. Its
additional `agr:IND44166303` xref is not stored locally by the current seeder,
and that is not a record-level defect.

The live OLS graph gives `CHEBI:84328` two direct `subClassOf` edges:
`CHEBI:36001` heptadecenoic acid and `CHEBI:59202` straight-chain fatty acid.
Those are exactly the generated `parent_compounds` values. The live OLS graph
also gives the term two roles, `CHEBI:35718` antifungal agent and `CHEBI:76946`
fungal metabolite. Only `CHEBI:35718` is an antimicrobial role in
`conf/sources.yaml`, and the committed source configuration maps it to
generated filing class `ANTIFUNGAL`.

The committed ChEBI inventory row for `CHEBI:84328` has the same label,
definition, 3-star status, role, parents, SMILES, Standard InChI, Standard
InChIKey, formula, neutral charge, masses, synonyms, xrefs, and source PubMed
identifiers that were used to seed this record. `PATHS.tsv` maps `CHEBI:84328`
to `ANTIFUNGAL/9z-heptadecenoic-acid`, matching the generated path and filing
class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:84328`, the exact file stem, the exact label, the exact Standard
InChIKey, the exact CAS number, and the exact ChEBI source PMIDs across
`reports/yaml_record_review`, `data/antibiotics`, `data/raw`, `curation`,
`conf`, `.claude`, `CLAUDE.md`, and `justfile` found only the expected
generated YAML, `PATHS.tsv` row, raw ChEBI row, and
`record_review_queue.tsv` row for exact `CHEBI:84328`.

## Evidence

The record's antifungal classification is inherited from committed ChEBI role
`CHEBI:35718`, `antifungal agent`. `data/raw/chebi_role_names.tsv` marks that
role as a ChEBI scope role, and `conf/sources.yaml` maps it to generated class
`ANTIFUNGAL`. That role is enough for reproducible source-level filing but not
enough to fill a specific producer assertion, activity observation, mode of
action, target, or causal graph.

The local ChEBI source literature leads are mixed. `PMID:11157268`, titled
`Specificity and mode of action of the antifungal fatty acid
cis-9-heptadecenoic acid produced by Pseudozyma flocculosa`, is an exact
compound antifungal lead: the PubMed title and abstract support that the
biocontrol fungus `Pseudozyma flocculosa` produces CHDA and that the paper
tested CHDA against fungi. Exact NCBI Taxonomy search resolved
`Pseudozyma flocculosa` to `NCBITaxon:84751`.

The same abstract supports a probable membrane-disruption sequence rather than
a discrete molecular target: CHDA did not act directly with membrane sterols,
the investigators inferred that the fatty acid partitions into fungal
membranes and raises membrane fluidity, and they proposed that membrane
disorder changes membrane-protein conformation, increases permeability, and
eventually disintegrates the cytoplasm. This is a strong primary-paper lead for
future curated mode-of-action and causal-graph fields. The PubMed abstract does
not expose exact MIC, percent-inhibition, strain, or table-level assay rows
that would be safe to import without full-text review.

The other two ChEBI source PubMed leads are not antimicrobial support.
`PMID:14263140` concerns incorporation of cis-9-heptadecenoic acid into rat
lymph and blood lipids, and `PMID:1854634` concerns taxonomy and pathogenicity
of `Erwinia cacticida` with fatty-acid profiles that include a lack of
cis-9-heptadecenoic acid in one bacterial cluster. They may be acceptable
source-level identity leads in ChEBI, but they should not become antifungal
activity, producer, mode-of-action, or causal-graph evidence for this record.

The generated record has no evidence-bearing objects. The local publication
helper surfaced only the three ChEBI source PMIDs for an exact-name, exact-CAS,
and exact-InChIKey query; direct exact PubMed search on those strings returned
no additional exact-identifier hits. A bounded `Pseudozyma flocculosa` and
heptadecenoic/fatty-acid PubMed search surfaced later glycolipid, flocculosin,
and review leads, but no inspected title or abstract displaced `PMID:11157268`
as the immediate exact-compound primary lead.

Semantic Scholar returned an invalid response for the exact publication-helper
query, and the PMC landing page did not provide a downloadable
`PMID:11157268` PDF in the attempted fetch. Search snippets, HTML download
interstitials, and undisplayed full text were not used as claim support.

## Completeness

The record is incomplete as a reviewed antifungal `(9Z)-heptadecenoic acid`
record. It has exact ChEBI identity, structure, parentage, xrefs, source-level
antifungal classification, and reproducible source metadata, but no curated
activity observation, producer organism, mode of action, or causal graph for
the exact CHDA antifungal paper.

The empty `molecular_targets` slot is acceptable unless full-text review finds
a discrete target assertion. The inspected `PMID:11157268` abstract supports a
membrane-disruption model whose causal nodes can probably be represented
without forcing an unsupported protein or pathway target.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are acceptable for the current seed. No measured
resistance edge, standalone clinical status assertion, public dataset
accession, or discussion-worthy identity conflict was identified in the
bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:84328` has source-level antifungal classification and one exact primary antifungal mechanism lead, but no curator-owned exact-compound activity, producer, mode-of-action, or causal-graph claim. | The generated record has three source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, and no `mode_of_action`. `PMID:11157268` is an exact CHDA antifungal paper with an abstract-level producer and probable membrane-disruption mechanism, so the record is missing triageable exact-compound evidence rather than only broad ChEBI role evidence. | Future curator-owned fields on `data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Review the full text of `PMID:11157268`. If the paper reports exact MICs,
   germination-inhibition values, or other interpretable antifungal activity
   measurements for exact CHDA, add claim-level `ActivityObservation` entries
   with organism, strain, assay, concentration, unit, and evidence details.
2. If full-text review confirms the producing organism and strain, curate
   `Pseudozyma flocculosa` as the producer with taxon grounding, preserving the
   exact strain scope if the paper names one.
3. Curate a mode of action and causal graph from the CHDA-specific membrane
   effects in `PMID:11157268`: fatty-acid partitioning into fungal membranes,
   increased membrane fluidity, membrane disorder or permeability changes, and
   eventual cytoplasmic disintegration. Avoid adding a discrete molecular
   target unless the primary text explicitly supports one.
4. Leave `PMID:14263140` and `PMID:1854634` out of claim-level antifungal
   evidence unless a future curator has a narrow identity or exclusion note to
   attach; those ChEBI source leads are not antimicrobial assay or mechanism
   support.
5. Leave the source-owned ChEBI identity, structure, role, parents, synonyms,
   database xrefs, and patent xrefs untouched unless the committed ChEBI
   inventory diverges from OLS or a curator decision needs to exclude a proven
   wrong source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml`
2. `just validate-strict data/antibiotics/antifungal/9z-heptadecenoic-acid.yaml --out /tmp/antibioticmech-chebi-84328-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-84328-worklist.tsv`
5. `just review-queue --limit 75`
6. `just qc`

Manually compare any future producer, activity, mode-of-action, target,
dataset, discussion, or causal-graph assertion against exact CHDA identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, the source antifungal-agent role,
generic unsaturated fatty-acid behavior, `Pseudozyma` biocontrol activity, or
other antifungal metabolites produced by `Pseudozyma flocculosa`.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden` or `find`, so
they included ignored `reports/` files.

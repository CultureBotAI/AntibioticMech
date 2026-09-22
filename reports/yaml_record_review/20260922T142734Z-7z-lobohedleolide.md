# YAML Record Review: (7Z)-lobohedleolide

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiviral/7z-lobohedleolide.yaml`
- Started UTC: 2026-09-22T14:21:00Z
- Finished UTC: 2026-09-22T14:27:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66586` |
| Label | `(7Z)-lobohedleolide` |
| Path | `data/antibiotics/antiviral/7z-lobohedleolide.yaml` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:66586`, version `2026-08-30`, minted key `antibioticmech:chebi-d5185ec575` |
| Source role | `CHEBI:64947` anti-HIV-1 agent |
| Parent compounds | `CHEBI:25384` monocarboxylic acid; `CHEBI:37581` gamma-lactone; `CHEBI:60687` cembrane diterpenoid |
| Structure | `SORYERHBQFTRIK-JMQTVVQQSA-N`; formula `C20H26O4`; charge `0` |
| Xrefs | `reaxys:4709575` |
| Source literature leads | `PMID:10785433` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(7Z)-lobohedleolide`, a neutral cembrane diterpenoid gamma-lactone. The YAML
has exact ChEBI grounding, the ChEBI definition, one ChEBI synonym, three
strictly broader ChEBI parents, one Reaxys xref, the ChEBI anti-HIV-1 role,
structure, and source-concept metadata. It has no generated or curator-owned
mode of action, molecular target, activity observation, resistance mechanism,
producer, dataset, discussion, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/7z-lobohedleolide.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/7z-lobohedleolide.yaml --out /tmp/antibioticmech-chebi-66586-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66586.tsv` | Pass: the full worklist TSV was written. `CHEBI:66586` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 62` | Pass: `CHEBI:66586` is queued with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:66586` resolves in official OLS as a current, non-obsolete ChEBI term
with label `(7Z)-lobohedleolide`, the same Standard InChIKey
`SORYERHBQFTRIK-JMQTVVQQSA-N`, the exact formula `C20H26O4`, matching average
and monoisotopic masses, the exact SMILES, and the exact `reaxys:4709575` and
`PMID:10785433` xrefs stored by or leading this generated record.

The live OLS term exposes the same IUPAC-name synonym stored in the YAML. The
IUPAC synonym is duplicated upstream in the OLS term JSON, once exact and once
related, but the generated YAML stores it once as an exact ChEBI synonym, which
is the correct local representation.

The live OLS graph gives `CHEBI:66586` three direct `subClassOf` edges:
`CHEBI:25384` `monocarboxylic acid`, `CHEBI:37581` `gamma-lactone`, and
`CHEBI:60687` `cembrane diterpenoid`. Those are exactly the generated
`parent_compounds` values. The graph also exposes role edges to `CHEBI:64947`
`anti-HIV-1 agent` and `CHEBI:76498` `coral metabolite`; only `CHEBI:64947` is
an antimicrobial activity role in `conf/sources.yaml`, so it is correctly the
only generated `activity_roles` value.

The committed ChEBI inventory row for `CHEBI:66586` has the same label,
definition, 3-star status, role, parents, SMILES, Standard InChI, Standard
InChIKey, formula, neutral charge, masses, synonym, Reaxys xref, and source
PMID that appear in the generated record or review queue. `PATHS.tsv` maps
`CHEBI:66586` to `ANTIVIRAL/7z-lobohedleolide`, matching the generated path and
filing class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:66586`, the exact record path, exact file stem, exact Standard InChIKey,
and exact `reaxys:4709575` across `reports/yaml_record_review`,
`data/antibiotics`, `data/raw`, `curation`, and `conf` found only the expected
generated YAML, `PATHS.tsv` row, raw ChEBI row, and `record_review_queue.tsv`
row for exact `CHEBI:66586`. Nearby hits for `CHEBI:66585` lobohedleolide and
`CHEBI:66587` 17-dimethylaminolobohedleolide were adjacent analogs, not prior
reviews of this record.

## Evidence

The record's antiviral classification is inherited from committed ChEBI role
`CHEBI:64947`, `anti-HIV-1 agent`. `data/raw/chebi_role_names.tsv` marks that
role as a ChEBI `class` role, and `conf/sources.yaml` maps it to the generated
`ANTIVIRAL` filing class. That role is enough for reproducible filing but not
enough to fill a mode of action, molecular target, EC50-bearing activity
observation, producer, or causal graph.

The pinned ChEBI source row has one PubMed lead, `PMID:10785433`, and the
generated record has no evidence-bearing objects. Direct PubMed eSearch for
exact title/abstract `(7Z)-lobohedleolide` returned `PMID:10785433` and direct
exact title/abstract `lobohedleolide` returned five indexed candidates. Direct
exact PubMed searches for the Standard InChIKey `SORYERHBQFTRIK-JMQTVVQQSA-N`,
exact ChEBI identifier `CHEBI:66586`, and exact Reaxys accession `4709575`
returned zero indexed candidates.

`PMID:10785433` supports the source anti-HIV lead for exact `(7Z)-lobohedleolide`
but does not, from its PubMed abstract alone, support a curated mechanism or
per-compound quantitative activity row. The abstract reports bioassay-guided
fractionation of an aqueous Philippine soft-coral `Lobophytum sp.` extract,
purification of lobohedleolide, `(7Z)-lobohedleolide`, and
17-dimethylaminolobohedleolide from HIV-inhibitory cembranoid-rich fractions,
and moderate cell-based anti-HIV activity with EC50 values around 3-5 ug/mL for
diterpenoids 1-3 as a group. It does not identify a molecular target or report
the exact compound 2 assay value, viral strain, or cell system in the abstract.

The broader repository PubMed helper was not used for claim support because
the exact-accession query expanded into off-topic PubMed hits. A Semantic
Scholar attempt on the same query returned HTTP 429 and was also not used.

NCBI Taxonomy eSearch for exact `Lobophytum hedleyi` returned no hit; genus
`Lobophytum` resolved to `NCBITaxon:205095`. No producer row should be added
from that alone. The only inspected source lead describes a soft-coral
collection as extraction material, not a taxonomically exact microbial source
or characterized biosynthetic producer of exact `CHEBI:66586`.

## Completeness

The record is incomplete as a reviewed antiviral `(7Z)-lobohedleolide` record.
It has exact ChEBI identity, structure, three strictly broader ChEBI parents,
one exact xref, source-level anti-HIV classification, and one source PMID lead,
but it has no curated `activity_spectrum`, mode of action, molecular target,
dataset, or causal graph.

The empty mode and target fields are correct for the current seed.
`CHEBI:64947` says only that the molecule has anti-HIV-1 activity, and the
inspected PubMed abstract reports cell-based HIV inhibition without naming a
specific viral or host molecular target.

The empty `activity_spectrum` slot is also acceptable until the full
`PMID:10785433` assay table is inspected. The abstract groups EC50 values for
three compounds and does not expose a compound-2-specific value, exact assay
system, or units beyond approximate `ug/mL`.

The empty `producer_organisms`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, and `discussions` slots are
acceptable. The producer worklist's `Lobophytum hedleyi` lead is a source-coral
cue inherited from the ChEBI definition, not evidence of microbial
biosynthesis. No measured resistance edge, clinical assertion, public dataset
accession, or discussion-worthy conflict with exact `CHEBI:66586`
claim-level evidence was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:66586` has only source-level anti-HIV classification and no curator-owned exact-compound activity, mechanism, target, producer, or causal-graph claim. | The generated record has one source PubMed lead, zero record evidence items, zero `activity_spectrum` rows, zero targets, no producer, and no `mode_of_action`. The exact source PMID lead supports extraction of `(7Z)-lobohedleolide` from HIV-inhibitory fractions and grouped anti-HIV activity for compounds 1-3, but the inspected abstract does not expose a compound-2-specific activity measurement or mechanism. | Future curator-owned fields on `data/antibiotics/antiviral/7z-lobohedleolide.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if the ChEBI role or source PMID proves unsupported after full-text inspection, a `curation/decisions.tsv` row or the ChEBI extractor owns that source-level correction. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect the full text of `PMID:10785433` / DOI `10.1021/np990372p` for the
   assay table behind compound 2. If it reports a compound-specific HIV
   inhibition value with a cell-based method, viral strain or isolate, and
   units, curate it as an `ActivityObservation` with claim-level evidence.
2. Keep `mode_of_action`, `molecular_targets`, and `causal_graphs` empty unless
   a primary source identifies a mechanism for exact `(7Z)-lobohedleolide`.
   The source anti-HIV phenotype does not identify a molecular target.
3. Do not add a producer from the ChEBI text alone. Add `producer_organisms`
   only if a primary paper or MIBiG entry shows that a resolvable taxon
   biosynthesizes exact `CHEBI:66586`; distinguish any animal host, symbiont,
   collection-level extraction source, and strain context.
4. If full-text review shows that `PMID:10785433` tested only a mixture,
   adjacent lobohedleolide stereoisomer, or source fraction rather than
   purified exact `(7Z)-lobohedleolide`, add a scoped source decision instead
   of record-owned activity.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antiviral/7z-lobohedleolide.yaml`
2. `just validate-strict data/antibiotics/antiviral/7z-lobohedleolide.yaml --out /tmp/antibioticmech-chebi-66586-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66586.tsv`
5. `just review-queue --limit 62`
6. `just qc`

Manually compare any future activity, mechanism, target, producer, dataset, or
causal-graph assertion against exact `(7Z)-lobohedleolide` identity. Confirm
that every claim-level evidence block attaches to the specific object it
supports, not only to the whole ChEBI term, the broader lobohedleolide family,
the source soft-coral collection, or the anti-HIV ChEBI role.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

# YAML Record Review: (E)-sinapaldehyde

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/e-sinapaldehyde.yaml`
- Started UTC: 2026-09-22T22:18:00Z
- Finished UTC: 2026-09-22T22:22:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:27949` |
| Label | `(E)-sinapaldehyde` |
| Path | `data/antibiotics/antifungal/e-sinapaldehyde.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:27949`, version `2026-08-30`, minted key `antibioticmech:chebi-c5306627cd` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:23245`, `CHEBI:33853`, `CHEBI:51681` |
| Structure | `CDICDSOGTRCHMG-ONEGZZNKSA-N`; formula `C11H12O4`; charge `0` |
| Xrefs | `cas:4206-58-0`, `kegg.compound:C05610`, `knapsack:C00002775`, `metacyc.compound:SINAPALDEHYDE`, `reaxys:2215799` |
| Document xrefs | `wikipedia.en:Sinapaldehyde` |
| Source literature leads | `PMID:21080014`, `PMID:22034160`, `PMID:22466741`, `PMID:23561163`, `PMID:28878036` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded exact sinapaldehyde record. The
YAML has exact ChEBI grounding, a ChEBI definition, seven exact ChEBI synonyms,
three broader ChEBI parents, five same-structure xrefs, one document xref, one
antifungal role, chemical structure fields, and source-concept metadata. It has
no generated or curator-owned activity observation, molecular target,
resistance mechanism, mode of action, producer, discussion, dataset, causal
graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/e-sinapaldehyde.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/e-sinapaldehyde.yaml --out /tmp/antibioticmech-chebi-27949-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-27949-worklist.tsv` | Pass: the full worklist TSV was written. Exact `CHEBI:27949` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 100` | Pass: `CHEBI:27949` is the first queued record after the records that already have `reports/yaml_record_review` reports; its row says `MECHANISM_REVIEW: mechanism is absent; 5 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `uv run runoak -i ols:chebi labels CHEBI:27949` | Pass: OLS resolved `CHEBI:27949` as `(E)-sinapaldehyde`. |
| `uv run runoak -i ols:chebi labels CHEBI:23245 CHEBI:33853 CHEBI:51681 CHEBI:35718` | Skipped: the OLS endpoint repeatedly timed out before returning all parent and role labels. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`data/raw/chebi_antimicrobials.tsv` seeds `CHEBI:27949` as a 3-star ChEBI entry
in antimicrobial role scope and gives the same label, exact definition, SMILES,
Standard InChI, Standard InChIKey, formula, charge, masses, ChEBI parent terms,
synonyms, xrefs, and source PMIDs that appear in or explain the generated YAML.
OAK through OLS resolved the identifier as `(E)-sinapaldehyde`; repeated parent
and role label lookups timed out at the OLS service, so those labels were not
checked there.

The `ANTIFUNGAL` filing class is consistent with the only generated ChEBI role:
`CHEBI:35718` maps to `ANTIFUNGAL` with priority `3` in `conf/sources.yaml`,
and `data/raw/chebi_role_names.tsv` labels it `antifungal agent`. Because the
source row has no more-specific mechanism role, the generated YAML correctly
has no `mode_of_action`, `mode_of_action_target_scope`, molecular target,
activity observation, or causal graph.

The same-structure xrefs are correctly scoped to database accessions rather
than literature accessions. ChEBI attaches CAS, KEGG, KNApSAcK, MetaCyc, and
Reaxys accessions to this term, and the YAML imports those accessions while
leaving the raw ChEBI PubMed citations as source-literature provenance.

Before this review branch was created, ignored-inclusive searches found no
prior dedicated `CHEBI:27949`, `sinapaldehyde`, or `e-sinapaldehyde` review
report and no curation decision, curator-inventory row, generated activity
observation, molecular target, resistance edge, producer, dataset, or
causal-graph claim resolving this exact record. Exact branch lookups found no
local branch, remote-tracking branch, or remote
`review-chebi-27949-e-sinapaldehyde` branch.

## Evidence

The record's antifungal class comes from the broad ChEBI `CHEBI:35718`
`antifungal agent` role. That role is sufficient for the generator to file the
record under `ANTIFUNGAL`, but it is not assertion-level primary evidence for a
particular fungal organism, MIC value, fungal molecular target, mode of action,
or causal graph edge.

The repository publication helper resolved all five ChEBI-seeded PubMed leads.
`PMID:22034160` is the direct antifungal lead: its abstract reports that
sinapaldehyde was tested against 65 `Candida` strains, including
fluconazole-sensitive and fluconazole-resistant clinical isolates, with MICs
from 100 to 200 ug/mL and downstream H+-extrusion, intracellular-pH, and
ultrastructure measurements. Full-paper extraction is still needed to capture
the exact MIC endpoint rows, isolate context, assay method, and whether the
H+-extrusion and microscopy results support a schema-representable mechanism.

The other ChEBI-seeded leads support occurrence, isolation, or chemical
modeling rather than exact antifungal activity at the inspected abstract level.
`PMID:28878036` reports sinapaldehyde incorporation into poplar lignin and
hydroxycinnamate metabolism after CAD1 down-regulation. `PMID:23561163`
identifies and quantifies sinapaldehyde as a volatile or aging marker in
sugar-cane spirits aged in wood casks. `PMID:22466741` reports isolation of
sinapyl aldehyde from `Diplomorpha canescens`. `PMID:21080014` is a theoretical
paper modeling red-wine oak phenolics against human health-associated protein
targets.

Focused exact-name searches found two additional antimicrobial plant-isolate
leads, `PMID:26809027` and `PMID:24611777`, that isolated sinapaldehyde during
bioassay-guided fractionation against oral pathogens. Their abstracts do not
assign the strongest reported `Candida albicans` or bacterial MIC observations
to sinapaldehyde, so full-paper table extraction would be required before any
observation could be mapped to exact `CHEBI:27949`.

Semantic Scholar returned HTTP 429 or an invalid-response error for the
repository publication-helper searches; PubMed returned results for each query.

## Completeness

The record is incomplete as a reviewed antifungal record. It has exact ChEBI
identity, structure, same-structure database xrefs, one document xref, three
broader ChEBI parents, a ChEBI antifungal role, and several source-paper leads,
but no claim-level evidence, no `activity_spectrum`, no molecular target, no
mode of action, no dataset, and no causal graph.

The empty molecular target, mode-of-action, and causal-graph slots are correct
for the current seed. The `Candida` abstract reports altered H+-extrusion,
intracellular pH, and cell ultrastructure, but it does not prove from the
abstract alone that exact `(E)-sinapaldehyde` has a direct molecular target or
one unambiguous enum-level mechanism.

The empty `activity_spectrum` slot should be treated as missing curation, not
as negative activity. PubMed has a primary lead for sinapaldehyde against
fluconazole-sensitive and fluconazole-resistant `Candida` isolates; exact
organism, strain or isolate, resistance phenotype, assay, endpoint, value, and
unit details still need full-paper extraction.

The empty `producers`, `resistance_mechanisms`, `clinical_status_assertions`,
`datasets`, and `discussions` slots are acceptable for the generated record. No
microbial biosynthetic producer row, measured resistance edge, clinical
assertion, public dataset accession, or discussion-worthy conflict with exact
`CHEBI:27949` claim-level evidence was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:27949` has source-level ChEBI antifungal classification, but no curator-owned primary evidence for exact antifungal activity, no activity observation, no molecular target, no mode of action, and no causal graph. | The generated record has 5 source literature leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no mode-of-action fields, and no causal graph. The worklist flags exact `CHEBI:27949` for `mechanism` and `review-readiness` only. `PMID:22034160` is a direct sinapaldehyde/Candida MIC and mechanism lead, but no observations or mechanistic claims from that paper are represented in the YAML. | Future curator-owned fields on `data/antibiotics/antifungal/e-sinapaldehyde.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect `PMID:22034160` in full and add exact `activity_spectrum` rows for
   source-reported sinapaldehyde observations against `Candida` standard
   strains and fluconazole-sensitive or resistant clinical isolates. Preserve
   endpoint type, value, unit, qualifier, assay, organism, strain or isolate,
   and resistance phenotype from each source row.
2. Choose a `mode_of_action` only after full-paper review determines whether
   the H+-extrusion, intracellular-pH, ultrastructural, and lysis data support
   a schema-representable mechanism for exact `CHEBI:27949`. Do not infer a
   direct molecular target from cinnamaldehyde class membership or growth
   inhibition alone.
3. Add a `MolecularTarget` only if the full text or a follow-on primary paper
   directly assays sinapaldehyde against a defined fungal target family,
   complex, or function.
4. Inspect `PMID:26809027` and `PMID:24611777` in full only as secondary
   activity candidates; add observations from those papers only if their tables
   report isolated sinapaldehyde concentration-response data instead of only
   extract, fraction, or different-compound data.
5. Do not cite the wood-cask, poplar-lignin, plant-isolation, or red-wine
   modeling papers as evidence for antifungal activity unless their full text
   contains an assay of isolated `(E)-sinapaldehyde` against a fungal organism.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/e-sinapaldehyde.yaml`
2. `just validate-strict data/antibiotics/antifungal/e-sinapaldehyde.yaml --out /tmp/antibioticmech-chebi-27949-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-27949-worklist.tsv`
5. `just review-queue --limit 100`
6. `just qc`

Manually compare future MIC rows, mechanism claims, target assertions, and
causal-graph curation against the full Shreaz cinnamic-aldehyde paper and any
full activity tables from the `Ixora` or `Ficus` papers to confirm that every
curated claim is attached to isolated `(E)-sinapaldehyde` rather than a plant
extract, an ethyl-acetate fraction, coniferyl aldehyde, cinnamaldehyde,
syringaldehyde, or 2,2'-dithiodipyridine.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, `find`, or
Git/GitHub ref listing, so they included ignored `reports/` files or otherwise
did not depend on Git's ignore filters.

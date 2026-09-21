# YAML Record Review: (1S,3R)-2,2-dichloro-N-[(1R)-1-(4-chlorophenyl)ethyl]-1-ethyl-3-methylcyclopropanecarboxamide

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml`
- Started UTC: 2026-09-21T22:10:00Z
- Finished UTC: 2026-09-21T22:15:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:47351` |
| Label | `(1S,3R)-2,2-dichloro-N-[(1R)-1-(4-chlorophenyl)ethyl]-1-ethyl-3-methylcyclopropanecarboxamide` |
| Path | `data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:47351`, version `2026-08-30`, minted key `antibioticmech:chebi-209a36f543` |
| Structure | `RXDMAYSSBPYBFW-RULNRJAQSA-N`; formula `C15H18Cl3NO`; charge `0` |
| Evidence-bearing objects | None |

This review covered the generated ChEBI-seeded child of carpropamid with full stereochemistry in the
Standard InChI. No curator-owned activity, target, resistance, producer, dataset, discussion, or causal
graph assertions are present.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml --out /tmp/antibioticmech-dichloro-cyclopropanecarboxamide-47351-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-dichloro-cyclopropanecarboxamide-47351.tsv` | Pass: full worklist TSV was written. `CHEBI:47351` appears only on `mechanism` and `review-readiness`. |
| `just review-queue --limit 36` | Pass: `CHEBI:47351` is the next queued unreported record after `CHEBI:66035`; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for this ChEBI-seeded record;
the schema/strict checks and `verify-corpus` are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:47351` is a current, non-obsolete 3-star ChEBI term. OLS resolves it to the record label and to
the same SMILES, Standard InChI, Standard InChIKey, formula, charge, average mass, monoisotopic mass,
`beilstein:8332858`, and `pdb-ccd:CRP` values captured in the generated YAML.

The ChEBI graph exposes `CHEBI:3434` carpropamid and `CHEBI:83403` monochlorobenzenes as direct
`subClassOf` parents of `CHEBI:47351`, matching the record's `parent_compounds` list. An
ignored-inclusive search for `RXDMAYSSBPYBFW` across `data`, `curation`, and `reports` found only this
record plus `data/antibiotics/antifungal/carpropamid.yaml`; that sibling is the broader stereochemistry-
unspecified `CHEBI:3434` structure with Standard InChIKey `RXDMAYSSBPYBFW-UHFFFAOYSA-N`, not a duplicate
of the stereospecific child reviewed here.

RCSB Chemical Component `CRP` is the exact ligand for this record: RCSB reports component `CRP` with
the same systematic name, formula, formal charge, Standard InChI, Standard InChIKey
`RXDMAYSSBPYBFW-RULNRJAQSA-N`, and a related ChEBI accession of `CHEBI:47351`. PDB entry `2STD` contains
`CRP` as non-polymer entity 3 and reports a scytalone-dehydratase cocrystal with carpropamid.

The `ANTIFUNGAL` class is consistent with the ChEBI-derived `CHEBI:24127` fungicide,
`CHEBI:35718` antifungal-agent, and `CHEBI:86328` antifungal-agrochemical role terms in the committed
raw inventory. The child `CHEBI:47351` no longer exposes direct `has role` edges through OLS, but the
extracted ChEBI row in `data/raw/chebi_antimicrobials.tsv` preserves those three accepted role terms and
`conf/sources.yaml` maps each to `ANTIFUNGAL`.

## Evidence

There are no evidence-bearing assertions in the target record. That is structurally legal for a seeded
ChEBI record because ChEBI supplies the source identity, structure, xrefs, parents, and role terms, and
there is no molecular target, activity observation, resistance mechanism, producer, clinical assertion,
or causal edge that would require claim-level evidence.

Registry evidence nevertheless identifies a curatable target/mechanism lead for the exact stereospecific
ligand. RCSB entry `2STD` cites PMID:9665698 / DOI:10.1021/bi980321b as its primary paper, names the
structure `SCYTALONE DEHYDRATASE COMPLEXED WITH TIGHT-BINDING INHIBITOR CARPROPAMID`, resolves the
protein entity as scytalone dehydratase from *Magnaporthe grisea* / *Pyricularia grisea*, and contains
the exact `CRP` ligand that ChEBI xrefs to `CHEBI:47351`.

Bounded publication searches found two directly relevant PubMed records:

| Query | Provider result |
|---|---|
| `"(1S,3R)-2,2-dichloro-N-[(1R)-1-(4-chlorophenyl)ethyl]-1-ethyl-3-methylcyclopropanecarboxamide" OR "RXDMAYSSBPYBFW" OR "carpropamid" OR "scytalone dehydratase"` | PubMed returned 20 candidates, mostly broad scytalone-dehydratase matches; Semantic Scholar returned HTTP 429. |
| `carpropamid scytalone dehydratase Pyricularia` | PubMed returned PMID:9665698, the 1998 cocrystal study, and PMID:15056895, a 2004 kinetic study of the Val75Met scytalone-dehydratase variant. |

PMID:9665698 supports direct binding of carpropamid to fungal scytalone dehydratase and gives enough
primary evidence to curate the target already present on the broader `CHEBI:3434` carpropamid sibling
onto this stereospecific `CHEBI:47351` ligand. PMID:15056895 and related PubMed hits about Val75Met
resistance are useful follow-up leads, but the abstracts alone do not establish a complete, exact
stereoisomer-specific `ResistanceMechanism`.

## Completeness

The record is incomplete for mechanism review. It has no `mode_of_action`, no
`mode_of_action_target_scope`, and no `molecular_targets`, even though the same RCSB/primary-literature
chain used for the reviewed `CHEBI:3434` parent resolves down to exact ligand `CRP` / `CHEBI:47351`.

Empty `activity_spectrum`, `producer_organisms`, `clinical_status_assertions`, `datasets`,
`discussions`, and `causal_graphs` slots are not defects in this review. Carpropamid is an agrochemical
fungicide rather than a reported natural product here; the inspected registry and abstract-level
literature did not provide a MIC with units, a biosynthetic producer, a clinical product assertion, or a
ready-to-write causal graph for the exact stereoisomer.

An ignored-inclusive search for `CHEBI:47351` across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the PATHS row, raw ChEBI row, review-queue row, and generated YAML. No existing
curation decision, overlay, curator-inventory row, or prior review report for the identifier was found.

An ignored-inclusive search for `pdb-ccd:CRP` across `data`, `curation`, and `reports` found only the raw
ChEBI row and this generated YAML. No other record is claiming the exact PDB Chemical Component
identifier.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The record omits its known fungal scytalone-dehydratase target and mode of action. `2STD` contains exact ligand `CRP` / `CHEBI:47351` bound to rice-blast scytalone dehydratase, and PMID:9665698 is the primary compound-enzyme cocrystal paper. Leaving this record `SEEDED` with no mechanism keeps it on the `mechanism` and `review-readiness` queues. | RCSB `CRP`; RCSB `2STD`; PMID:9665698; `just worklist` rows for `CHEBI:47351`. | Curator-owned fields in `data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml`, written only through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Curate the scytalone-dehydratase mechanism on `data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml` through a guarded mutator:
   add `mode_of_action: OTHER`, `mode_of_action_target_scope: MICROBIAL_TARGET`, a `CURATOR:` mechanism
   note citing PMID:9665698, and a `molecular_targets` entry for fungal scytalone dehydratase with
   `target_relation: DIRECT_BINDING_TARGET`, `evidence_status: PRIMARY_EVIDENCE`, taxon context for the
   historical *Pyricularia*/*Magnaporthe* enzyme, and `PMID:9665698` evidence.

2. Add record-level `PMID:9665698` evidence to the same generated YAML if the mechanism curation uses
   the cocrystal paper as the source of exact compound-mechanism support.

3. Follow PMID:15056895 and the linked MBI-D resistance papers to decide whether the Val75Met
   scytalone-dehydratase phenotype can be represented as an exact `ResistanceMechanism` for this
   stereospecific component. Do not add it from abstracts alone; inspect the full papers for organism,
   strain or isolate, protein, alteration, phenotype, and carpropamid-isomer scope.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antifungal/1s-3r-2-2-dichloro-n-1r-1-4-chlorophenyl-ethyl-1-ethyl-3-methylcyclopr.yaml --out /tmp/antibioticmech-record-validation.tsv`
  after any mechanism, target, or resistance curation.
- Re-run `just verify-corpus --summary` to prove the guarded edits survive the generated-corpus
  comparison and only curator-owned fields changed.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and confirm `CHEBI:47351` no
  longer appears on `mechanism` once a curator-owned mode of action is present.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`; the record should
  either leave `review-readiness` after `REVIEWED` sign-off or move to the next concrete evidence gate.
- Manually compare the final YAML to the reviewed `CHEBI:3434` carpropamid sibling so the mechanism
  wording remains honest about stereospecific `CRP` versus broader non-stereospecified carpropamid.

## Additional Notes

- The ChEBI/OLS and RCSB API checks were direct official registry reads through `curl`. Browser fetching
  was unable to retrieve those registry pages, and `runoak` is not installed in this checkout.
- NCBI E-utilities did not resolve from this environment during the review, but the repository's
  `scripts/search_publications.py` adapter did retrieve PubMed candidates after running outside the
  sandbox so `uv` could read its cache.
- The exact stereospecific child has no ChEBI definition; that absence is inherited from ChEBI rather
  than introduced by the seeder.

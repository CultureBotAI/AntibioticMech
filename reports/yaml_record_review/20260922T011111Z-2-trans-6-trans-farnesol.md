# YAML Record Review: (2-trans,6-trans)-farnesol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml`
- Started UTC: 2026-09-22T01:06:40Z
- Finished UTC: 2026-09-22T01:11:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:16619` |
| Label | `(2-trans,6-trans)-farnesol` |
| Path | `data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:16619`, version `2026-08-30`, minted key `antibioticmech:chebi-134af6f602` |
| Source role | `CHEBI:33281` antimicrobial agent, inherited from parent `CHEBI:28600` farnesol |
| Structure | `CRDAMVZIKSXKFV-YFVJMOTDSA-N`; formula `C15H26O`; charge `0` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded farnesol stereoisomer. The YAML
has source-derived identity, definition, parent, role, structure, and
cross-reference metadata, but no curator-owned mode of action, target, activity
observation, producer, resistance, discussion, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml --out /tmp/antibioticmech-trans-trans-farnesol-16619-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-trans-trans-farnesol-16619.tsv` | Pass: the full worklist TSV was written. `CHEBI:16619` appears on `mechanism`, two `xref-span-conflict` rows for withheld raw HMDB/KNApSAcK accessions, and `review-readiness`; it has 0 CARD targets and 0 resistance edges to build on. |
| `just review-queue --limit 41` | Pass: `CHEBI:16619` is the next queued record after `CHEBI:35966`; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks and `verify-corpus` are the
narrowest documented local gates.

## Identity and Grounding

`CHEBI:16619` resolves in official OLS as a current, non-obsolete ChEBI term
labeled `(2-trans,6-trans)-farnesol` and defined as the all-trans stereoisomer
of farnesol. Its formula, charge, monoisotopic mass, Standard InChI, Standard
InChIKey, CAS xref, KEGG COMPOUND xref, LIPID MAPS xref, MetaCyc xref, and
stereospecific synonyms match the committed `data/raw/chebi_antimicrobials.tsv`
row and the generated YAML.

The record is correctly distinct from `CHEBI:28600` farnesol. Official OLS
lists `CHEBI:28600` as the only direct parent of `CHEBI:16619`; the parent has a
Standard InChIKey without fixed double-bond stereochemistry, while this child
fixes the `(2E,6E)` geometry and matches `CRDAMVZIKSXKFV-YFVJMOTDSA-N`.

The `CHEBI:33281` antimicrobial-agent role is inherited from the broader
`CHEBI:28600` farnesol node. Official OLS lists `antimicrobial agent`, `plant
metabolite`, and `fungal metabolite` as `has role` fillers on `CHEBI:28600`.
This inheritance is intentional: `scripts/extract_source_inventory.py`
propagates in-scope ChEBI roles from a bearer to every descendant, and
`conf/sources.yaml` maps the generic `CHEBI:33281` role to
`ANTIMICROBIAL_UNSPECIFIED`.

The live KEGG COMPOUND `C01126` entry is also `(2E,6E)-farnesol`; its formula,
mass, CAS, ChEBI, and LIPID MAPS links agree with ChEBI's all-trans structure.
The raw ChEBI row also includes `hmdb:HMDB0004305` and
`knapsack:C00003132`, but the seeder withholds both from the generated YAML
because the same accessions also appear on stereochemically broader
`CHEBI:28600`.

An ignored-inclusive search for `CHEBI:16619`,
`CRDAMVZIKSXKFV-YFVJMOTDSA-N`, `antibioticmech:chebi-134af6f602`, and exact
all-trans-farnesol names across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the expected `PATHS.tsv` row, `record_review_queue.tsv`
row, raw ChEBI row, and generated YAML. No prior review report, curated overlay,
or second generated record claims this exact Standard InChIKey.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for a
ChEBI-seeded record because the source concept supplies database provenance and
no mechanism, target, activity, resistance, producer, or causal claim has been
promoted into curator-owned slots.

A bounded exact-stereoisomer PubMed/Semantic Scholar search for
`"(2-trans,6-trans)-farnesol" OR "(2E,6E)-farnesol" OR "(E,E)-farnesol" OR
"all-trans-farnesol" OR "trans,trans-farnesol" OR
"CRDAMVZIKSXKFV-YFVJMOTDSA-N"` found 20 PubMed candidates and hit Semantic
Scholar HTTP 429. A second query that added antimicrobial terms also found 20
PubMed candidates and hit the same Semantic Scholar rate limit.

Several PubMed abstracts are exact-compound activity leads for later curation.
PMID:34118413 evaluated `trans-trans-farnesol` MICs against 31 bacterial strains
and 4 *Candida* species. PMID:26162644 tested `trans, trans-farnesol` against
the white-nose syndrome fungus *Pseudogymnoascus destructans* and related fungi.
PMID:38035328 tested exogenous `trans, trans-farnesol` against *Leishmania
amazonensis* promastigotes. PMID:39519322 tested `trans, trans-farnesol` alone
and with arachidonic acid against *Streptococcus mutans* and *Streptococcus
sobrinus*. PMID:41747781 tested `tt-farnesol` against four *Streptococcus equi*
isolates and also assayed tetracycline-resistance modulation.

Those abstracts are enough to prove exact all-trans-farnesol antimicrobial leads
exist, but not enough to enter every strain-level `ActivityObservation` with an
assay, value qualifier, endpoint value, units, and citation. Full text and table
inspection remain necessary before curation, especially for combination,
biofilm, derivative, nanoparticle, in silico, and secretion papers that mention
`(E,E)-farnesol` without necessarily measuring isolated compound susceptibility.

## Completeness

The record is incomplete as a reviewed antimicrobial record. Its generic
antimicrobial role is inherited from stereochemically broader `CHEBI:28600`, and
none of the exact all-trans-farnesol antimicrobial leads has been resolved into
claim-level activity observations, a target group, a mode of action, resistance
modulation, or a causal graph.

The empty `mode_of_action`, `molecular_targets`, `activity_spectrum`,
`resistance_mechanisms`, `producer_organisms`, and `causal_graphs` slots are
preferable to over-scoped filler. A later curation pass should inspect
PMID:34118413, PMID:26162644, PMID:38035328, PMID:39519322, and PMID:41747781
first, then add to these slots only after the full source supports the exact
compound, organism, strain, assay, and measured endpoint.

The bounded exact-name publication searches also found biosynthetic or secretion
leads, including *Candida albicans* secretion and plant terpene synthase papers,
but no source inspected from PubMed metadata was sufficient by itself to curate a
producer organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact all-trans-farnesol antimicrobial assay leads have not been resolved into evidence-backed activity observations or an explicit unresolved curation discussion. | The generated YAML has no evidence-bearing activity items; PubMed exact-name searches found abstracts for direct `trans-trans-farnesol` assays against Gram-positive bacteria, *Candida*, *Pseudogymnoascus*, and *Leishmania*; `just worklist` still queues only `mechanism`, `xref-span-conflict`, and `review-readiness` for `CHEBI:16619`. | Future curator-owned fields on `data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, or same-structure xref findings were
found.

No minor findings.

## Recommended Edits

1. Inspect full text for PMID:34118413 and PMID:41747781 first because their
   PubMed abstracts explicitly report `trans-trans-farnesol` MIC assays against
   named bacterial strains. Add one `ActivityObservation` per organism or strain
   only when the source supplies the exact endpoint value, qualifier, assay, and
   units.
2. Inspect PMID:26162644, PMID:38035328, and PMID:39519322 next for antifungal,
   antiprotozoal, and biofilm or combination endpoints. Add only isolated
   `CHEBI:16619` observations to `activity_spectrum`; keep material,
   combination, and adjuvant-only claims out unless they can be represented
   without losing their experimental context.
3. If a source supports a membrane-disruption, efflux-modulation, quorum-sensing,
   cell-cycle, or biofilm mechanism for the exact antimicrobial activity, curate
   `mode_of_action` with `CURATOR:` provenance, set
   `mode_of_action_target_scope`, and add target or causal-graph entries only
   for source-supported causal edges.
4. Preserve the withheld `hmdb:HMDB0004305` and `knapsack:C00003132` xrefs until
   a curator resolves their one-accession/two-structure ambiguity between
   `CHEBI:16619` and `CHEBI:28600`; any fix belongs in the source inventory,
   xref filtering, or `curation/decisions.tsv`, not in the generated YAML.

## Follow-up Checks

After any curation, rerun:

1. `just validate data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml`
2. `just validate-strict data/antibiotics/unspecified/2-trans-6-trans-farnesol.yaml --out /tmp/antibioticmech-trans-trans-farnesol-16619-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-trans-trans-farnesol-16619.tsv`
5. `just review-queue --limit 41`

If a curator resolves the withheld HMDB or KNApSAcK accessions, rerun `just
worklist --queue xref-span-conflict` and verify that the `CHEBI:16619` rows drop
without creating a same-structure conflict on another farnesol stereoisomer.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

Semantic Scholar returned HTTP 429 for both repository publication searches; the
PubMed side of both searches completed and returned candidates.

# YAML Record Review: (9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml`
- Started UTC: 2026-09-22T16:04:00Z
- Finished UTC: 2026-09-22T16:08:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65768` |
| Label | `(9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid` |
| Path | `data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:65768`, version `2026-08-30`, minted key `antibioticmech:chebi-8001a4c8c7` |
| Source role | `CHEBI:33282` antibacterial agent |
| Parent compounds | `CHEBI:15904` long-chain fatty acid; `CHEBI:25380` acetylenic fatty acid; `CHEBI:59202` straight-chain fatty acid; `CHEBI:73155` trienoic fatty acid |
| Structure | `UXMMIMGEKFYPFK-PDBXOOCHSA-N`; formula `C18H26O2`; charge `0` |
| Xrefs | `cas:61481-30-9`; `reaxys:4432637` |
| Source literature leads | `PMID:1632297`; `PMID:1636161`; `PMID:21604791`; `PMID:8377015` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid`, the acetylenic fatty acid
also called `dicranin`. The YAML has exact ChEBI grounding, the ChEBI
definition, one ChEBI synonym, four ChEBI parents, the antibacterial ChEBI
role, two ChEBI xrefs, structure, and source-concept metadata. It has no
generated or curator-owned mode of action, molecular target, activity
observation, producer organism, resistance mechanism, dataset, discussion,
causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml --out /tmp/antibioticmech-chebi-65768-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-65768-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:65768` appears on `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 80` | Pass: `CHEBI:65768` is queued with `MECHANISM_REVIEW: mechanism is absent; 4 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:65768` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label `(9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid`, the same
definition, the exact Standard InChIKey `UXMMIMGEKFYPFK-PDBXOOCHSA-N`, the
exact formula `C18H26O2`, neutral charge, matching average and monoisotopic
masses, the exact `cas:61481-30-9` and `reaxys:4432637` xrefs, and the same
four source PMIDs that seed the local record.

The generated YAML stores the source ChEBI synonym `dicranin`. OLS also exposes
the preferred label itself as duplicate exact and related IUPAC synonyms; the
local seeder correctly de-duplicates that label out of `synonyms`.

The live OLS graph gives `CHEBI:65768` four direct `subClassOf` edges:
`CHEBI:15904` long-chain fatty acid, `CHEBI:25380` acetylenic fatty acid,
`CHEBI:59202` straight-chain fatty acid, and `CHEBI:73155` trienoic fatty
acid. Those are exactly the generated `parent_compounds` values. The live OLS
graph gives the term three roles: `CHEBI:25212` metabolite, `CHEBI:33282`
antibacterial agent, and `CHEBI:64996` EC 1.13.11.33 arachidonate
15-lipoxygenase inhibitor. Only `CHEBI:33282` is an antimicrobial role in
`conf/sources.yaml`, and the committed source configuration maps that role to
the generated filing class `ANTIBACTERIAL`.

The committed ChEBI inventory row for `CHEBI:65768` has the same label,
definition, 3-star status, role, parents, SMILES, Standard InChI, Standard
InChIKey, formula, neutral charge, masses, synonym, xrefs, and source PubMed
identifiers that were used to seed this record. `PATHS.tsv` maps `CHEBI:65768`
to `ANTIBACTERIAL/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid`, matching
the generated path and filing class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:65768`, the exact file stem, the exact label, and the exact Standard
InChIKey across `reports/yaml_record_review`, `data/antibiotics`, `data/raw`,
`curation`, `conf`, `.claude`, `CLAUDE.md`, and `justfile` found only the
expected generated YAML, `PATHS.tsv` row, raw ChEBI row, and
`record_review_queue.tsv` row for exact `CHEBI:65768`. A broader
ignored-inclusive filename search for `*octadeca*` under
`reports/yaml_record_review` found only a prior report for a different
octadecadienoic acid.

## Evidence

The record's antibacterial classification is inherited from committed ChEBI
role `CHEBI:33282`, `antibacterial agent`. `data/raw/chebi_role_names.tsv`
marks that role as a ChEBI scope role, and `conf/sources.yaml` maps it to
generated class `ANTIBACTERIAL`. That role is enough for reproducible
source-level filing but not enough to fill a specific activity observation,
producer assertion, mode of action, target, or causal graph.

The source PMID set has one exact antimicrobial primary-paper lead.
`PMID:8377015`, titled `Dicranin, an antimicrobial and 15-lipoxygenase
inhibitor from the moss Dicranum scoparium`, reports an antimicrobial and
15-lipoxygenase screening workflow over moss extracts, isolation of
dicranin from the `Dicranum scoparium` dichloromethane extract, and pure
dicranin being responsible for most of that biological activity. The PubMed
abstract names antibacterial organisms for the extract and states that the
strongest pure-dicranin antimicrobial effect was against `Streptococcus
faecalis` by disc diffusion, while exact NCBI Taxonomy search resolved
`Dicranum scoparium` to active species `NCBITaxon:3222`.

`PMID:21604791` is also exact for dicranin and `Dicranum scoparium`, but its
abstract covers dicranin's transformation into volatile oxylipins after
mechanical wounding of moss tissue. It is a stronger producer/biosynthesis lead
than an antibacterial lead.

The two 1992 ChEBI source PMIDs, `PMID:1632297` and `PMID:1636161`, are
duplicate Guichardant platelet papers about dicranin effects on arachidonic
acid metabolism and platelet aggregation. They support host platelet
cyclooxygenase, 12-lipoxygenase, and aggregation activity for exact dicranin,
not antimicrobial activity, a microbial target, or a bacterial mode of action.

The exact-name/CAS/InChIKey publication-helper query returned ten PubMed
candidates and Semantic Scholar returned HTTP 429. Direct PubMed eSearch for
`dicranin`, `61481-30-9`, and exact title fragments returned 12 candidate PMIDs:
the four ChEBI source leads, a `Ceratodon purpureus` acetylenase/desaturase
paper, two 1970s moss acetylenic-acid papers, and newer bryophyte
chemotaxonomy/fatty-acid profile papers. The inspected titles and abstracts did
not expose another immediate primary antibacterial exact-dicranin lead beyond
`PMID:8377015`.

## Completeness

The record is incomplete as a reviewed antibacterial dicranin record. It has
exact ChEBI identity, structure, parentage, xrefs, source-level antibacterial
classification, and reproducible source metadata, but no curated
activity-observation or producer rows even though `PMID:8377015` supports exact
dicranin antibacterial activity and isolation from `Dicranum scoparium`.

The empty `mode_of_action`, `molecular_targets`, and causal-graph slots are
acceptable for the current seed. Arachidonate 15-lipoxygenase inhibition and
host platelet arachidonic-acid effects should not be transcribed into a
microbial mode of action. No antimicrobial mechanism for exact dicranin was
visible in the inspected PubMed titles and abstracts.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are acceptable for the current seed. No measured
resistance edge, standalone clinical status assertion, public dataset
accession, or discussion-worthy identity conflict was identified in the
bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:65768` has source-level antibacterial classification and one exact antimicrobial primary-paper lead, but no curator-owned exact-compound activity, producer, mode-of-action, or causal-graph claim. | The generated record has four source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, and no `mode_of_action`. `just worklist` also places the record on `producer-candidate` and `activity-candidate` because the ChEBI definition states that dicranin was isolated from `Dicranum scoparium` and exhibits antibacterial activity. `PMID:8377015` is an exact dicranin antimicrobial paper with abstract-level bacterial activity and moss-isolation support. | Future curator-owned fields on `data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Review the full text of `PMID:8377015`. If it reports exact disc-diffusion
   diameters, MICs, or other interpretable antimicrobial measurements for pure
   dicranin, add claim-level `ActivityObservation` entries with organism,
   strain, assay, value, unit, concentration context, and evidence details.
   Preserve the abstract-level distinction that dicranin was inactive against
   `Escherichia coli` even though the source `Dicranum scoparium` extract was
   active against `E. coli`.
2. If full-text review of `PMID:8377015` or `PMID:21604791` confirms
   biosynthesis or accumulation by exact `Dicranum scoparium`, curate the
   producer as `NCBITaxon:3222` with strain or collection context if the paper
   provides one.
3. Leave `mode_of_action`, `molecular_targets`, and the causal graph empty
   unless a primary source supports an antimicrobial mechanism for exact
   dicranin. Soybean 15-lipoxygenase inhibition and human platelet aggregation
   inhibition should not become microbial target assertions.
4. Leave `PMID:1632297`, `PMID:1636161`, and the exact-dicranin bryophyte
   chemotaxonomy or oxylipin papers out of antibacterial claim-level evidence
   unless a future curator has a narrow biosynthesis or exclusion note to
   attach; they do not report exact antibacterial susceptibility results.
5. Leave the source-owned ChEBI identity, structure, role, parents, synonym,
   and xrefs untouched unless the committed ChEBI inventory diverges from OLS
   or a curator decision needs to exclude a proven wrong source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml`
2. `just validate-strict data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml --out /tmp/antibioticmech-chebi-65768-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-65768-worklist.tsv`
5. `just review-queue --limit 80`
6. `just qc`

Manually compare any future producer, activity, mode-of-action, target,
dataset, discussion, or causal-graph assertion against exact dicranin identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, the source antibacterial-agent
role, the moss extract, a host 15-lipoxygenase assay, human platelet
aggregation, or a later bryophyte chemotaxonomy study.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden` or `find`, so
they included ignored `reports/` files.

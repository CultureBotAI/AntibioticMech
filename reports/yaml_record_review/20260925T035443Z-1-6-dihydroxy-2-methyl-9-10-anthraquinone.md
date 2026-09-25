# YAML Record Review: 1,6-dihydroxy-2-methyl-9,10-anthraquinone

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml`
- Started UTC: 2026-09-25T03:37:00Z
- Finished UTC: 2026-09-25T03:54:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:69532` |
| Label | `1,6-dihydroxy-2-methyl-9,10-anthraquinone` |
| Synonym | `Soranjidiol` |
| Class | `ANTIBACTERIAL` |
| Status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | ChEBI `CHEBI:69532`, version `2026-08-30`, minted as `antibioticmech:chebi-d2eb821ee4` |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`; future identity, synonym, structure, parent, role, and xref changes belong in the ChEBI extractor/seeder path or `curation/decisions.tsv` |

The full 53-line YAML record was read. It is a ChEBI-only generated seed with:

- one exact ChEBI source concept, `CHEBI:69532`
- two exact synonyms, `1,6-dihydroxy-2-methylanthracene-9,10-dione` and `Soranjidiol`
- one antimicrobial role, `CHEBI:33282`
- one parent, `CHEBI:37484`
- two exact same-structure xrefs, `cas:518-73-0` and `reaxys:2382285`
- SMILES, Standard InChI, Standard InChIKey
  `BSKQISPKMLYNTK-UHFFFAOYSA-N`, formula `C15H10O4`, charge `0`,
  average mass `254.241`, and monoisotopic mass `254.05791`
- no `mode_of_action`, `mode_of_action_target_scope`,
  `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`,
  `producer_organisms`, `causal_graphs`, `datasets`, `discussions`, or
  record-level `evidence`
- only seed/reseed history events from `seed_from_sources`

## Validation

| Check | Result |
|---|---|
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. The target is row 164 with `MECHANISM_REVIEW: mechanism is absent; 7 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --queue mechanism --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-mechanism.tsv` | Passed; the target is row 470 with `0 CARD target(s), 0 resistance edge(s) to build on`. |
| `just worklist --queue producer-candidate --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-producer-candidate.tsv` | Passed; the target is row 191 because the ChEBI definition says `Rubia yunnanensis` was the isolation source. |
| `just worklist --queue activity-candidate --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-activity-candidate.tsv` | Passed; `CHEBI:69532` is absent from this queue. |
| `just worklist --queue xref-unverified --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-xref-unverified.tsv` | Passed; `CHEBI:69532` is absent from this queue. |
| `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-xref-span-conflict.tsv` | Passed; `CHEBI:69532` is absent from this queue. |
| `just worklist --queue multi-component --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-multi-component.tsv` | Passed; `CHEBI:69532` is absent from this queue. |
| `just worklist --queue moa-scope --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-moa-scope.tsv` | Passed after the known unrelated `iclaprim` cross-reference diagnostic; `CHEBI:69532` is absent from this queue. |
| `just worklist --queue target-evidence --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-target-evidence.tsv` | Passed; `CHEBI:69532` is absent from this queue. |
| `just validate data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml` | Passed with `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml --out /tmp/dihydroxy-methyl-anthraquinone-69532-validate-strict.tsv` | Passed; one file scanned, zero `ERROR` rows. |
| `just verify-corpus --summary` | Passed after the known unrelated `iclaprim` self-contradictory CARD cross-reference diagnostic; all 2,939 expected records are present and the corpus reproduces exactly from `data/raw/` plus curator inputs. |

No narrower repository `just` targets exist for standalone term, reference, or
history validation on this generated ChEBI record, so this review used the
available single-record schema checks, full-corpus reproducibility, and the
derived worklist/review-queue checks that feed the review gate.

## Identity and Grounding

The live ChEBI `CHEBI:69532` page agrees with the generated record on the exact
identifier, label, three-star status, definition, formula, net charge, average
and monoisotopic masses, SMILES, Standard InChI, Standard InChIKey, IUPAC name,
`Soranjidiol` synonym, CAS and Reaxys registry numbers, and seven source
PubMed citations.

The generated `parent_compounds` entry matches the ChEBI `is a` relation:

| Parent | ChEBI label |
|---|---|
| `CHEBI:37484` | `dihydroxyanthraquinone` |

The generated `activity_roles` list preserves ChEBI's only antimicrobial role
for this compound:

| Role | ChEBI label |
|---|---|
| `CHEBI:33282` | `antibacterial agent` |

ChEBI also asserts a plant-metabolite role that is correctly not stored under
`activity_roles`, because `activity_roles` intentionally keeps only
antimicrobial role CURIEs from the source row.

PubChem resolves the exact Standard InChIKey
`BSKQISPKMLYNTK-UHFFFAOYSA-N` to CID `124063`, titled `Soranjidiol`, and the
CID properties agree with the generated formula, charge, Standard InChI,
Standard InChIKey, exact mass, and monoisotopic mass. PubChem's canonical
SMILES is equivalent but not byte-identical to ChEBI's emitted SMILES, which is
acceptable because this corpus stores the ChEBI representation for
ChEBI-grounded records.

A hidden- and ignored-file-inclusive exact search for `CHEBI:69532`,
`antibioticmech:chebi-d2eb821ee4`, `BSKQISPKMLYNTK-UHFFFAOYSA-N`,
`518-73-0`, `2382285`, `Soranjidiol`, and
`1-6-dihydroxy-2-methyl-9-10-anthraquinone` covered `data/antibiotics`,
`data/raw`, `curation`, `reports/yaml_record_review`, `.claude`, `docs`,
`README.md`, `conf`, `src`, `scripts`, `tests`, `justfile`, and
`pyproject.toml`, excluding bulky generated `data/embeddings/**` and
`pages/**` outputs. It found exactly the expected YAML record, `PATHS.tsv` row,
raw ChEBI row, and `review-readiness` row, and it found no prior exact review
report or curator decision row for `CHEBI:69532`.

## Evidence

ChEBI cites seven PubMed records for `CHEBI:69532`:

| PMID | Relevance |
|---|---|
| `PMID:13678245` | `Heterophyllaea pustulata` extract study that detected antimicrobial activity in benzenic extracts and identified soranjidiol among several stem-extract anthraquinones; the abstract does not assign the measured antimicrobial effect to pure soranjidiol. |
| `PMID:15629252` | Exact photobiology lead for purified soranjidiol and related anthraquinones as Type I/Type II photosensitizers; it supports reactive oxygen photochemistry, not an organismal antimicrobial assay. |
| `PMID:18513778` | Exact animal phototoxicity lead for soranjidiol from `Heterophyllaea pustulata`; it concerns goat/mouse phototoxicity rather than antimicrobial activity. |
| `PMID:20965744` | Exact primary antibacterial lead for soranjidiol and other purified photosensitizing anthraquinones against `Staphylococcus aureus`, with MIC/MBC-style susceptibility testing and reactive oxygen species follow-up. |
| `PMID:21214480` | Exact isolation lead from `Morinda elliptica`; the abstract reports anti-HIV, cytotoxic, and antimicrobial testing across eleven anthraquinones but names other compounds, not soranjidiol, as active. |
| `PMID:21665453` | Exact cancer photodynamic-therapy lead for soranjidiol and related anthraquinones against MCF-7c3 breast cancer cells; not an antimicrobial source. |
| `PMID:21973054` | Exact `Rubia yunnanensis` roots isolation and bioactivity-screening lead used by ChEBI's species-of-metabolite table; the abstract says all isolated compounds were evaluated for cytotoxic, antibacterial, and antifungal activity but does not expose a soranjidiol-specific result. |

Bounded exact-name PubMed and Europe PMC searches for `Soranjidiol` and
`1,6-dihydroxy-2-methyl-9,10-anthraquinone` found additional leads that are
newer than the committed `2026-08-30` ChEBI inventory or are not cited by the
ChEBI row:

| PMID | Relevance |
|---|---|
| `PMID:31054439` | Exact in vitro antileishmanial photodynamic-inactivation lead for purified soranjidiol and other `Heterophyllaea lycioides` anthraquinones. |
| `PMID:33622002` | Exact antiherpetic photodynamic lead for purified `Heterophyllaea pustulata` anthraquinones; the abstract specifically describes a light-stimulated improvement for soranjidiol. |
| `PMID:36966867` | Exact in vivo cutaneous-leishmaniasis photodynamic lead in BALB/c mice with soranjidiol and violet-blue LED. |
| `PMID:40987174` | Exact 2025 `Leishmania amazonensis` photoinactivation lead for soranjidiol with white LED and reactive oxygen/nitrogen mechanistic follow-up. |
| `PMID:40577974` | Computational lead for soranjidiol photochemistry and photoinduced tautomerization; no organismal antimicrobial experiment was visible in the PubMed abstract. |

The exact antibacterial, antiherpetic, and antileishmanial papers all point to
photodynamic reactive-oxygen activity as the curated mechanistic axis. They do
not create a schema defect in the seed record by being absent: future claims
would be curator-owned `mode_of_action: OXIDATIVE_DAMAGE`,
`mode_of_action_target_scope`, `activity_spectrum`, and `causal_graphs` added
through `record_curation_event` plus `write_validated_antibiotic`.

## Completeness

The generated identity, structure, antimicrobial role, parent, and exact xrefs
are sound for the ChEBI seed.

The record is not review-complete because exact literature is already visible
for purified soranjidiol photodynamic antibacterial, antiviral, and
antileishmanial activity, but no curator-owned mechanism, activity spectrum, or
causal graph has been added. The complete worklist keeps `CHEBI:69532` on the
`mechanism` queue with no CARD target or resistance edges, which is expected for
a ChEBI-only natural product whose mechanism evidence comes from organismal
photodynamic experiments rather than imported target/resistance slices.

The ChEBI definition and ChEBI species-of-metabolite table identify
`Rubia yunnanensis` roots as an isolation source through `PMID:21973054`, and
`just worklist --queue producer-candidate` keeps that plant on the queue as a
source-only candidate. The current record has no `producer_organisms`, so it
does not yet preserve the source organism, root tissue context, or citation at
claim level.

The exact-name literature search found antiprotozoal and antiviral
photodynamic activity leads that are not represented in ChEBI's current
antimicrobial role list for this compound. A future curator should inspect the
full assay tables before deciding whether those papers warrant exact
`activity_spectrum` observations alone, additional seeded ChEBI role
corrections, or both.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact soranjidiol mechanism and activity evidence is not curated, so the record cannot satisfy the `REVIEWED` gate. | The YAML has no `mode_of_action`, `mode_of_action_target_scope`, `activity_spectrum`, `molecular_targets`, or `causal_graphs`; the exact worklist row keeps `CHEBI:69532` on `mechanism`; `PMID:20965744` reports purified soranjidiol antibacterial testing against `Staphylococcus aureus` with photodynamic ROS follow-up; newer exact PubMed leads report soranjidiol photoinactivation experiments for `Leishmania amazonensis` and HSV-1. | Future curator-owned fields on `data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |
| Major | The ChEBI `Rubia yunnanensis` source assertion remains a producer candidate instead of a claim-level `producer_organisms` item or explicit rejection. | The live ChEBI page grounds the species-of-metabolite assertion to `PMID:21973054`, and the regenerated producer-candidate worklist places `CHEBI:69532` at row 191 because `Rubia yunnanensis` is only a source phrase in the generated definition. | Future curator-owned producer item on `data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml`, or a local refusal path if plant producers are intentionally out of scope. |
| Minor | Most ChEBI source PMIDs are discovery or phototoxicity leads rather than direct organismal antimicrobial support for exact soranjidiol. | Five of the seven ChEBI-cited PubMed abstracts are pure photophysics, animal/cancer phototoxicity, mixed-extract, or inactive-sibling leads; only `PMID:20965744` is visibly direct for purified soranjidiol antibacterial activity from the PubMed abstract, while `PMID:21973054` visibly supports the `Rubia yunnanensis` isolation context. | No generated ChEBI row correction is needed; future curation should attach only the exact papers that support each claim-level item. |

## Recommended Edits

1. Inspect the full text of `PMID:20965744` and curate exact
   `Staphylococcus aureus` `activity_spectrum` observations for purified
   soranjidiol, including MIC and MBC values, units, irradiation context, assay
   method, and evidence.
2. If full-text evidence supports the ROS interpretation, add a curator-owned
   `mode_of_action: OXIDATIVE_DAMAGE`, the corresponding target scope, and a
   causal graph that models light-mediated reactive oxygen generation without
   overstating a molecular target.
3. Inspect `PMID:31054439`, `PMID:36966867`, `PMID:40987174`, and
   `PMID:33622002` for exact antileishmanial and antiherpetic assay values and
   context; add `activity_spectrum` items only for measurements that report
   organism, strain or form, units, and assay conditions.
4. Inspect `PMID:21973054` beyond the abstract and decide whether
   `Rubia yunnanensis` is a supportable producer/source-organism claim for this
   schema or should be refused with an explicit local rationale.
5. Rerun `just worklist --queue mechanism`, `just worklist --queue
   producer-candidate`, `just validate`, `just verify-corpus --summary`, and
   `just qc` after any future curator-owned mutation.

## Follow-up Checks

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
- `just worklist --queue mechanism --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-mechanism.tsv`
- `just worklist --queue producer-candidate --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-producer-candidate.tsv`
- `just worklist --queue activity-candidate --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-activity-candidate.tsv`
- `just worklist --queue xref-unverified --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-xref-unverified.tsv`
- `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-xref-span-conflict.tsv`
- `just worklist --queue multi-component --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-multi-component.tsv`
- `just worklist --queue moa-scope --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-moa-scope.tsv`
- `just worklist --queue target-evidence --limit 0 --tsv /tmp/dihydroxy-methyl-anthraquinone-target-evidence.tsv`
- `just validate data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml`
- `just validate-strict data/antibiotics/antibacterial/1-6-dihydroxy-2-methyl-9-10-anthraquinone.yaml --out /tmp/dihydroxy-methyl-anthraquinone-69532-validate-strict.tsv`
- `just verify-corpus --summary`
- `rg --no-ignore --hidden -n -e 'CHEBI:69532' -e 'antibioticmech:chebi-d2eb821ee4' -e 'BSKQISPKMLYNTK-UHFFFAOYSA-N' -e '518-73-0' -e '2382285' -e 'Soranjidiol' -e '1-6-dihydroxy-2-methyl-9-10-anthraquinone' data/antibiotics data/raw curation reports/yaml_record_review .claude docs README.md conf src scripts tests justfile pyproject.toml --glob '!data/embeddings/**' --glob '!pages/**'`

## Additional Notes

The report intentionally does not add an `UNKNOWN` mechanism or a
no-known-target discussion: a direct ROS photodynamic lead exists for exact
soranjidiol, and the bounded search found additional direct exact
antileishmanial and antiherpetic photodynamic leads. The unresolved work is to
transcribe exact assay and mechanism details from full papers, not to document a
negative mechanism search.

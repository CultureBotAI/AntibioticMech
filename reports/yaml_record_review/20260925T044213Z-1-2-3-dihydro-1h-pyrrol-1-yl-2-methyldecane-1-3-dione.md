# YAML Record Review: 1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldecane-1,3-dione

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml`
- Started UTC: 2026-09-25T04:42:13Z
- Finished UTC: 2026-09-25T04:42:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70402` |
| Label | `1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldecane-1,3-dione` |
| Path | `data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | ChEBI `CHEBI:70402`, version `2026-08-30`, minted as `antibioticmech:chebi-bf4bca78cd` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:17087`, `CHEBI:26455`, `CHEBI:29347` |
| Structure | `HMWIYUSLKIYYER-UHFFFAOYSA-N`; formula `C15H25NO2`; charge `0` |
| Xrefs | `reaxys:8211286` |
| Source literature leads | `PMID:21053938` |

This review covered one generated ChEBI-seeded saturated pyrrolidinone record.
The YAML is a ChEBI source-derived stub with one exact ChEBI source concept,
the ChEBI definition, three ChEBI parents, one ChEBI activity role, a neutral
ChEBI structure, one Reaxys xref, and three seed history entries. It has no
record-level `evidence`, `activity_spectrum`, `producer_organisms`,
`mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
`resistance_mechanisms`, `causal_graphs`, `datasets`, `discussions`, or
curator-owned history entries.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml --out /tmp/chebi-70402-validate-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected, 2,939 on disk, no missing or unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Passed with the known unrelated `ARO:3000337`/iclaprim cross-reference diagnostic; wrote all worklist rows and listed `CHEBI:70402` on `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows and listed `CHEBI:70402` with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --queue mechanism --limit 0 --tsv /tmp/chebi-70402-mechanism.tsv` | Passed; listed `CHEBI:70402` with 0 CARD targets and 0 resistance edges to build on. |
| `just worklist --queue producer-candidate --limit 0 --tsv /tmp/chebi-70402-producer-candidate.tsv` | Passed; listed `CHEBI:70402` for the `Penicillium citrinum` ChEBI definition phrase. |
| `just worklist --queue activity-candidate --limit 0 --tsv /tmp/chebi-70402-activity-candidate.tsv` | Passed; `CHEBI:70402` is absent from this queue. |
| `just worklist --queue xref-unverified --limit 0 --tsv /tmp/chebi-70402-xref-unverified.tsv` | Passed; `CHEBI:70402` is absent from this queue. |
| `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/chebi-70402-xref-span-conflict.tsv` | Passed; `CHEBI:70402` is absent from this queue. |
| `just worklist --queue multi-component --limit 0 --tsv /tmp/chebi-70402-multi-component.tsv` | Passed; `CHEBI:70402` is absent from this queue. |
| `just worklist --queue target-evidence --limit 0 --tsv /tmp/chebi-70402-target-evidence.tsv` | Passed; `CHEBI:70402` is absent from this queue. |
| `just worklist --queue moa-scope --limit 0 --tsv /tmp/chebi-70402-moa-scope.tsv` | Passed after the known unrelated `ARO:3000337`/iclaprim cross-reference diagnostic; `CHEBI:70402` is absent from this queue. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded generated record. The schema/strict validators,
`verify-corpus`, the full worklist, the full review queue, and the focused
worklist queues above are the narrowest documented local gates for this review.

## Identity and Grounding

The live ChEBI `CHEBI:70402` page agrees with the generated record on the exact
identifier, label, ChEBI definition, 3-star status, neutral formula
`C15H25NO2`, average mass `251.370`, monoisotopic mass `251.18853`, SMILES,
Standard InChI, Standard InChIKey `HMWIYUSLKIYYER-UHFFFAOYSA-N`, Reaxys
accession `8211286`, and ChEBI role `CHEBI:35718`, `antifungal agent`. ChEBI
also asserts `CHEBI:76964`, `Penicillium metabolite`; this non-antimicrobial
role is correctly not copied into `activity_roles`.

ChEBI has the same direct ontology parents as the generated `parent_compounds`
list: `CHEBI:17087`, `ketone`; `CHEBI:26455`, `pyrroles`; and `CHEBI:29347`,
`monocarboxylic acid amide`. The committed `data/raw/chebi_antimicrobials.tsv`
row and `data/antibiotics/PATHS.tsv` lock row agree with the generated path,
class, source label, structure, parentage, role, xref, and sole PubMed lead.

PubChem PUG-REST resolves the record's Standard InChIKey to CID `10037813`,
with the exact title, formula, Standard InChI, Standard InChIKey, neutral
charge, and exact mass `251.188529040`. PubChem serializes the dihydropyrrole
SMILES with the double bond starting at a different ring atom than ChEBI does,
but the Standard InChI and InChIKey are byte-identical to the generated record.

The immediately related ChEBI sibling `CHEBI:70401` shares the ChEBI antifungal
role, direct parents, source PMID, and `Penicillium` isolation definition, but
it is the unsaturated `(8E)` analogue
`(E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione` with formula
`C15H23NO2`, Reaxys xref `8060218`, and Standard InChIKey
`JGNMZTXDOHXIJQ-ONEGZZNKSA-N`. The generated `CHEBI:70402` YAML therefore
denotes the saturated exact structure rather than a duplicate or spelling
variant of its sibling.

A hidden- and ignored-file-inclusive exact search for `CHEBI:70402`,
`antibioticmech:chebi-bf4bca78cd`, `HMWIYUSLKIYYER-UHFFFAOYSA-N`,
`reaxys:8211286`, the exact label, the current file stem, and `PMID:21053938`
covered `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`,
`scripts`, `tests`, `justfile`, and `pyproject.toml`, excluding bulky generated
`data/embeddings/**` and `pages/**`. It found the expected YAML, `PATHS.tsv`
row, raw ChEBI row, review-queue row, and prior `CHEBI:70401` sibling report
mentions. An ignored-inclusive filename search under
`reports/yaml_record_review` for `*methyldecane*` found no prior exact
`CHEBI:70402` report.

## Evidence

The record's antifungal filing comes entirely from ChEBI's `CHEBI:35718`
source role. That is enough to seed `antimicrobial_class: ANTIFUNGAL`, but it
does not supply exact-compound MIC rows, producer claims, a mode of action, a
molecular target, resistance, or causal edges.

`PMID:21053938` resolves in official PubMed as a 2010 Journal of Natural
Products article with DOI `10.1021/np100470h`. Its abstract describes a
fractional factorial design workflow that first optimized bioactive
`Penicillium` extracts and then optimized particular secondary metabolites; it
names `P. oxalicum`, `P. citrinum`, and two citrinalin alkaloids isolated from
optimized `P. citrinum` cultures. The abstract confirms the two-`Penicillium`
secondary-metabolite context but does not name exact `CHEBI:70402`, expose
which purified compound had antifungal activity, report an MIC or other
activity measurement for exact `CHEBI:70402`, or assert a molecular target or
antifungal mode of action.

The DOI resolved to ACS but ACS returned a Cloudflare challenge page, so the
primary full text was not inspectable from the local command line. This matters
for producer curation: the live ChEBI species-of-metabolite table asserts both
`Penicillium brevicompactum` and `Penicillium citrinum` strain `F53` against
`PMID:21053938`, while the PubMed abstract names `P. oxalicum` and
`P. citrinum`, not `P. brevicompactum`.

The exact-label Europe PMC search found one open secondary review,
`PMID:26901206`. Inspecting that PubMed Central full text showed that its
marine `Penicillium`/`Talaromyces` strain table lists exact `CHEBI:70402` under
`P. citrinum` strain `F53 = CBMAI1186` from `Caulerpa` sp., with
`PMID:21053938` as the source. The review did not resolve exact antifungal
measurements, a mechanism, or ChEBI's live `P. brevicompactum` assertion, so it
is a useful lead back to the same primary paper rather than sufficient
claim-level evidence for this record.

A bounded PubMed exact-label query found no hits for
`"1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldecane-1,3-dione"`. The corresponding
Europe PMC exact-label query found only the secondary review above, and a
separate Europe PMC search for the first block of the Standard InChIKey
`HMWIYUSLKIYYER` found no hits.

## Completeness

The record is incomplete as a reviewed antifungal compound. Its exact identity,
structure, filing class, ChEBI role, ChEBI parentage, Reaxys xref, source
concept, and seed history are structurally reproducible and agree with live
ChEBI/PubChem, but no curator has added exact-compound evidence for
antifungal activity, producer organisms, a mode of action, molecular targets,
or a causal graph.

The empty `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
and `causal_graphs` slots are acceptable for the current seed but block the
`REVIEWED` gate. The inspected sources did not expose a molecular target or
mechanism for exact `CHEBI:70402`; the source PMID's abstract and the 2016
secondary review only identify a secondary-metabolite context.

The empty `producer_organisms` slot is also acceptable for the current seed but
requires full-text curation before it can be resolved. ChEBI asserts two
species origins from `PMID:21053938`, while the exact open secondary row found
in this review only lists exact `CHEBI:70402` under `P. citrinum` strain
`F53 = CBMAI1186`. The local `producer-candidate` queue captured the
`Penicillium citrinum` source-definition phrase but not the
`Penicillium brevicompactum` assertion visible on the live ChEBI page.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are acceptable for the current seed. No inspected
source or local queue identified exact resistance edges, a standalone official
clinical status, a public dataset accession, or a concrete identity conflict
that needs a record discussion before future curation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:70402` remains a source-seeded antifungal classification with no curator-owned activity, mode-of-action, target, or causal-graph claim. | The YAML has zero `record_evidence` items, no `activity_spectrum`, no `mode_of_action`, no `molecular_targets`, and no `causal_graphs`; `just review-queue --limit 0` reports `CHEBI:70402` as `MECHANISM_REVIEW`; `PMID:21053938` is the only source literature lead; the inspected PubMed abstract and open 2016 review did not expose exact-compound MIC values, a target, or a mechanism. | Future curator-owned fields on `data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |
| Major | The two `Penicillium` source assertions remain unresolved producer candidates rather than claim-level `ProducerOrganism` entries or explicit rejections. | ChEBI's definition says exact `CHEBI:70402` was isolated from `Penicillium citrinum` and `Penicillium brevicompactum`, the live ChEBI species table attaches `PMID:21053938` to both taxa, and `just worklist --queue producer-candidate` lists the generated record for `Penicillium citrinum`. The PubMed abstract names `P. oxalicum` and `P. citrinum`, not `P. brevicompactum`, while the 2016 secondary review table lists exact `CHEBI:70402` under `P. citrinum` strain `F53 = CBMAI1186` with `PMID:21053938` as its source. | Future curator-owned `producer_organisms` items on `data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml`, or a `curation/decisions.tsv` exclusion/grounding decision if full-text review shows the ChEBI assertion is wrong. |

No blocker identity, structure, schema, xref, path-lock, parentage, or audit
history findings were found.

No minor findings.

## Recommended Edits

1. Review the full text and supporting information for `PMID:21053938`. If it
   reports exact antifungal measurements for purified `CHEBI:70402`, add
   `ActivityObservation` entries with organism, strain, assay, activity call,
   MIC or other measurement, units, and claim-level evidence.
2. Use the same full-text review to resolve ChEBI's exact producer assertions.
   Add `ProducerOrganism` entries for only the species and strains shown to
   biosynthesize or yield exact `CHEBI:70402`; if `Penicillium brevicompactum`
   is not supported for this exact compound, record that as a curator decision
   rather than inheriting ChEBI's species-of-metabolite row.
3. Leave `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
   resistance mechanisms, and `causal_graphs` empty until a primary source
   supports exact `CHEBI:70402` mechanism claims.
4. Leave ChEBI-owned identity, structure, role, parent, xref, and source
   concept fields unchanged unless the committed ChEBI inventory diverges from
   the live ChEBI term or future source inspection proves that a ChEBI source
   assertion needs an exclusion/grounding decision.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml`
2. `just validate-strict data/antibiotics/antifungal/1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldecane-1-3-dione.yaml --out /tmp/chebi-70402-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
6. Focused `just worklist --queue mechanism`, `--queue producer-candidate`,
   `--queue activity-candidate`, `--queue target-evidence`, `--queue
   moa-scope`, `--queue xref-unverified`, `--queue xref-span-conflict`, and
   `--queue multi-component` exports.
7. `just qc`

Manually confirm that every future `ActivityObservation`, `ProducerOrganism`,
`MolecularTarget`, and `CausalEdge` evidence block attaches to the exact
saturated `CHEBI:70402` compound rather than only to a bioactive extract,
`P. citrinum` or `P. brevicompactum` as a metabolite source, the unsaturated
`CHEBI:70401` sibling, or the broad ChEBI `antifungal agent` source role.

## Additional Notes

`CHEBI:70402` is absent from the focused `activity-candidate`,
`xref-unverified`, `xref-span-conflict`, `multi-component`, `moa-scope`, and
`target-evidence` TSVs generated for this review.

All absence searches in this report used `rg --no-ignore --hidden` or `find`,
so they included ignored files such as existing `reports/yaml_record_review`
Markdown files.

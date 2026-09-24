# YAML Record Review: (Z)-roxithromycin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/z-roxithromycin.yaml
- Started UTC: 2026-09-24T04:28:04Z
- Finished UTC: 2026-09-24T04:28:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:32109 |
| Label | (Z)-roxithromycin |
| Path | data/antibiotics/antibacterial/z-roxithromycin.yaml |
| Class | ANTIBACTERIAL |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:32109, source version 2026-08-30 |
| Standard InChIKey | RXZBMPWDPOLZGW-HEWSMUCTSA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to
`data/antibiotics/antibacterial/z-roxithromycin.yaml`. An
ignored-file-inclusive search for `CHEBI:32109`, `(Z)-roxithromycin`,
`z-roxithromycin`, and `roxithromycin` across `data/antibiotics`, `data/raw`,
`curation`, and `reports/yaml_record_review` found this target, its exact
`PATHS.tsv` row, its raw ChEBI row, its exact `review-readiness` queue row,
the adjacent broad `CHEBI:48844` `roxithromycin` record, the adjacent
`CHEBI:48935` `(E)-roxithromycin` record, and the prior exact
`(E)-roxithromycin` review report. A separate ignored-file-inclusive `find`
found no prior exact `reports/yaml_record_review/*z-roxithromycin*` report.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/z-roxithromycin.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/z-roxithromycin.yaml --out /tmp/z-roxithromycin-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/z-roxithromycin-worklist.tsv` | Passed; `CHEBI:32109` appears only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; `CHEBI:32109` was the next queue row without an exact one-record review report after matching prior report identifiers and normalized report headers. |
| `just lint` | Passed; `ruff` reported `All checks passed!`. |

`just verify-corpus` and `just worklist` both emitted the known CARD
`ARO:3000337` / iclaprim cross-reference refusal; that warning is unrelated to
this ChEBI-only record.

The repository exposes `validate`, `validate-strict`, `verify-corpus`,
`worklist`, `review-queue`, and `lint`; it does not expose narrower
single-record term, reference, or history validators for a plain ChEBI-seeded
record with no record-level citations.

## Identity and Grounding

The ChEBI identity is exact. OLS4 resolves `CHEBI:32109` to
`(Z)-roxithromycin` with the same formula, Standard InChI, Standard InChIKey
`RXZBMPWDPOLZGW-HEWSMUCTSA-N`, neutral charge, average mass, monoisotopic mass,
SMILES, KEGG compound xref `kegg.compound:C13173`, and KEGG drug xref
`kegg.drug:D01710` carried by the local raw ChEBI row and generated record.

The isomer boundary is correct:

- `CHEBI:32109` is the minor `Z` geometrical isomer and has the stereospecific
  InChIKey `RXZBMPWDPOLZGW-HEWSMUCTSA-N`.
- `CHEBI:48935` is the major `E` geometrical isomer and has the stereospecific
  InChIKey `RXZBMPWDPOLZGW-XMRMVWPWSA-N`.
- `CHEBI:48844` is broader, unspecified `roxithromycin` and has the
  nongeometrical Standard InChIKey `RXZBMPWDPOLZGW-HITVVWEBSA-N`.

The ChEBI parent `CHEBI:48844` is therefore strictly broader than this exact
`Z` isomer. The adjacent broad `roxithromycin` generated record is also the
ARO merge point for `ARO:0000027`; it correctly owns CARD's
`50S ribosomal subunit P-site` target assertion and 28 CARD-derived resistance
routes rather than projecting them onto exact `CHEBI:32109`.

The only generated xrefs are KEGG accessions imported from the exact ChEBI term.
KEGG `C13173` and `D01710` both name roxithromycin, and `D01710` also carries
broad antibacterial, protein-biosynthesis-inhibitor, and 50S ribosomal-subunit
assertions. Those KEGG drug assertions are useful target leads, but they should
not be promoted to exact-isomer molecular-target curation without checking the
compound form behind the 50S claim.

The filing class is consistent with imported source assertions. ChEBI assigns
`CHEBI:33281` antimicrobial-agent and `CHEBI:36047` antibacterial-drug roles to
`CHEBI:32109`, and the record is filed as `ANTIBACTERIAL`.

## Evidence

This record has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, and no
`causal_graphs`. That is structurally valid for a ChEBI seed, but it means the
exact minor `Z` roxithromycin isomer has only upstream database provenance and
no primary-paper support for a compound-specific antibacterial mechanism.

The local raw ChEBI row for `CHEBI:32109` carries no PMID leads. Bounded PubMed
and OLS/KEGG checks found identity and follow-up leads, but did not resolve the
missing mechanism:

- An exact PubMed query over `(Z)-roxithromycin`, `CHEBI:32109`, the exact
  InChIKey, and the KEGG accessions found `PMID:15067706`, a
  pH-dependent-geometric-isomerization paper. Its PubMed abstract discusses
  interconversion between roxithromycin and the `Z` isomer in simulated
  gastrointestinal fluid and rats, which supports identity/context rather than
  a bacterial target, MIC, resistance mechanism, or causal edge.
- A broader `Z`/roxithromycin-isomer query returned eight PubMed candidates:
  chromatography, pharmacokinetic, and biotransformation papers dominated the
  list, and no title/abstract result supported a curated exact-`Z` bacterial
  mechanism claim.
- Semantic Scholar was attempted for the isomer query and returned HTTP 429, so
  it added no candidate records.
- A roxithromycin ribosome/resistance PubMed query and explicit fetches of
  `PMID:11677599`, `PMID:19469526`, and `PMID:37284499` found broad
  roxithromycin 50S-structure, 50S-binding, and in-vitro macrolide-resistance
  leads. The inspected PubMed metadata did not establish that the compound
  tested in those papers was exact `CHEBI:32109`.

Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, isomer boundary,
roxithromycin parentage, structure fields, KEGG xrefs, antibacterial filing
class, and seed history are sufficient for a ChEBI-only seed.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent. The adjacent broad ARO/CHEBI `roxithromycin`
  record and KEGG `D01710` both point toward a 50S ribosomal target, but this
  exact `Z` isomer should remain below `REVIEWED` until a curator either finds
  exact-isomer evidence or adds a curator-owned veto explaining why only
  broad/major-isomer roxithromycin evidence exists.
- `activity_spectrum` is absent. Future activity curation should use measured
  organism, strain or isolate, assay, value, qualifier, units, compound form,
  and evidence rather than copying susceptibility observations from broad
  roxithromycin or from the `(E)` major isomer.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD resistance edge was available for this exact
  ChEBI record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: no regulatory source was imported for this
  exact ChEBI record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact `(Z)-roxithromycin` record has no reviewed antibacterial mechanism or activity measurement. | `just worklist --limit 0 --tsv /tmp/z-roxithromycin-worklist.tsv` lists `CHEBI:32109` in `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and in `review-readiness` with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`; the YAML has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_spectrum`, or `causal_graphs`; bounded exact-isomer PubMed checks yielded pharmacokinetic or isomerization leads rather than an exact-isomer bacterial target or MIC claim. | Add an evidence-backed curator-owned mechanism and any measured activity observations to `data/antibiotics/antibacterial/z-roxithromycin.yaml` through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unresolved for exact `(Z)-roxithromycin`. |

No blockers found. No minor findings found.

## Recommended Edits

1. Inspect the broad roxithromycin 50S and macrolide-resistance leads, starting
   with `PMID:11677599`, `PMID:19469526`, `PMID:37284499`, and KEGG `D01710`,
   for exact source-compound stereochemistry and assay scope.
2. Add a `CURATOR:`-owned `mode_of_action`, target scope, molecular target, and
   causal graph only when a source supports exact `(Z)-roxithromycin`;
   otherwise leave a curator-owned veto documenting that only broad or major
   `E`-isomer roxithromycin evidence was found.
3. Add measured `activity_spectrum` rows only when the source provides complete
   organism, strain or isolate, assay, value, units, compound form, and
   evidence for `(Z)-roxithromycin`.

## Follow-up Checks

- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/antibacterial/z-roxithromycin.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/z-roxithromycin-worklist.tsv`, and
  `just lint`.
- Re-run OLS4 checks for `CHEBI:32109`, `CHEBI:48844`, and `CHEBI:48935` if
  future edits touch identity, xrefs, or parentage.
- Re-run KEGG checks for `C13173` and `D01710` if future curation needs to
  decide whether either accession should inform exact-isomer target or activity
  claims.

## Additional Notes

- The ignored-file-inclusive resolution search covered `data/antibiotics`,
  `data/raw`, `curation`, and `reports/yaml_record_review`; a separate
  ignored-file-inclusive `find` found no prior exact report for
  `z-roxithromycin`.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:32109` was absent from all inspected queues except `mechanism` and
  `review-readiness`.

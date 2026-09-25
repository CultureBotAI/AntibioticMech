# YAML Record Review: 1β-methylcarbapenem

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/1β-methylcarbapenem.yaml
- Started UTC: 2026-09-25T22:28:59Z
- Finished UTC: 2026-09-25T22:28:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:46764` |
| Label | `1β-methylcarbapenem` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antibacterial/1β-methylcarbapenem.yaml` and locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is a generated exact ChEBI seed for `CHEBI:46764`. It contains
one ChEBI source concept with `role_terms: [CHEBI:33281, CHEBI:33282]`, two
ChEBI synonyms, one ChEBI parent, and a ChEBI-sourced neutral structure.

The record has no ChEBI definition, `xrefs`, record-level `evidence`,
`mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
`activity_spectrum`, `resistance_mechanisms`, `producer_organisms`,
`causal_graph`, `datasets`, `clinical_status`, or `discussions`.

The ignored-file-inclusive exact search covered `reports/yaml_record_review`,
`data/antibiotics`, `data/raw`, and `curation` for `CHEBI:46764`, the minted
source key `antibioticmech:chebi-fe486ebf7b`, the exact Unicode label, the ASCII
`1beta-methylcarbapenem` label, and InChIKey `YKMONJZIUAOVEM-WDSKDSINSA-N`.
It found no prior review report and only the generated YAML, the path lock row,
the exact raw ChEBI row, and the review-queue row.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/1β-methylcarbapenem.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1β-methylcarbapenem.yaml --out /tmp/antibioticmech-chebi-46764-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-46764.tsv` | Passed; the exact `CHEBI:46764` rows were `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-46764-review-queue.tsv` | Passed; `CHEBI:46764` is queued as `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Source-map lookup in `conf/sources.yaml` | Passed; generic `CHEBI:33281` is in scope and `CHEBI:33282` maps to `ANTIBACTERIAL`, matching the generated class. Neither role maps to a seeded mechanism or target scope. |
| Live OLS4 `CHEBI:46764`, parent, and role-term lookups | Passed; `CHEBI:46764` is current and non-obsolete with the same formula, Standard InChIKey, charge, Standard InChI, and masses as the YAML/raw row. Its direct OLS hierarchical parent is current, non-obsolete `CHEBI:46633` `carbapenems`; the two role terms resolve to `CHEBI:33281` `antimicrobial agent` and `CHEBI:33282` `antibacterial agent`. |
| PubChem InChIKey lookup for `YKMONJZIUAOVEM-WDSKDSINSA-N` | Passed; PubChem CID `16755650` has the same formula, Standard InChI, Standard InChIKey, exact mass, and charge as the YAML, and lists the ChEBI ID plus both ChEBI synonyms. |
| PubMed exact searches for the record InChIKey and ChEBI structural synonyms | Passed with no exact hits; direct ESearch found 0 PubMed records for `YKMONJZIUAOVEM-WDSKDSINSA-N`, `1beta-methyl-2,3-didehydro-1-carbapenam`, and `(4S,5S)-4-methyl-1-azabicyclo[3.2.0]hept-2-en-7-one`. |
| `scripts/search_publications.py` PubMed/Semantic Scholar searches for `1β-methylcarbapenem`, `1 beta-methylcarbapenem`, exact ChEBI structural synonyms, and the InChIKey | Partially passed; PubMed returned derivative/scaffold papers that mention substituted 1β-methylcarbapenems or named derivatives, while Semantic Scholar returned HTTP 429 under its unauthenticated rate limit. |

## Identity and Grounding

- `CHEBI:46764` is the correct ChEBI grounding for the exact small neutral
  structure in the generated record. The live OLS4 term, committed raw row,
  generated YAML, and PubChem CID `16755650` agree on Standard InChIKey
  `YKMONJZIUAOVEM-WDSKDSINSA-N`, formula `C7H9NO`, charge `0`, Standard InChI,
  and monoisotopic mass.
- ChEBI's generated synonyms, `1β-methyl-2,3-didehydro-1-carbapenam` and
  `(4S,5S)-4-methyl-1-azabicyclo[3.2.0]hept-2-en-7-one`, denote the same exact
  structure in OLS4 and PubChem.
- The direct ChEBI parent `CHEBI:46633` `carbapenems` is current and broader
  than the exact `CHEBI:46764` structure; it should remain a
  `parent_compounds` value rather than be treated as exact identity evidence.
- `activity_roles: [CHEBI:33281, CHEBI:33282]` preserves the raw ChEBI source
  roles used by the seeder. The antibacterial role `CHEBI:33282` is the source
  of the generated `ANTIBACTERIAL` filing class.

## Evidence

The current YAML inherits ChEBI database provenance but has no primary-paper
mechanism, target, activity, resistance, producer, or causal-graph claim.

| Lead | Supports the antibacterial record? | Review |
|---|---|---|
| ChEBI `CHEBI:46764` | Exact seeded identity and generic activity-role support. | The live term repeats the same formula, Standard InChIKey, Standard InChI, and mass as the generated YAML and PubChem. The committed raw ChEBI row supplies `CHEBI:33281` and `CHEBI:33282` as source activity roles but supplies no definition, xref, or PubMed citation for exact `CHEBI:46764`. |
| PubChem CID `16755650` | Secondary exact structure cross-check. | PubChem resolves the record InChIKey to the same neutral structure and lists `CHEBI:46764`; its synonyms include the generated ChEBI IUPAC and related IUPAC names but no exact CAS or article identifier. |
| PubMed searches for exact structural identifiers | No direct support found. | Direct ESearch queries for the InChIKey and both ChEBI structural synonyms returned 0 PubMed hits, bounding the inspected absence of an exact `CHEBI:46764` assay or mechanism paper under those identifiers. |
| PubMed searches for `1β-methylcarbapenem` and variants | Near-miss scaffold and derivative leads only. | PubMed returned medicinal-chemistry and microbiology papers on active substituted 1β-methylcarbapenem series and named derivatives such as tomopenem, doripenem, CS-023, CS-834, and L-786,392. Those abstracts use `1β-methylcarbapenem` as a derivative class or scaffold descriptor, not as a report of antibacterial activity for the exact bare `CHEBI:46764` structure. |

## Completeness

- **Identity and structure:** complete enough for read-only review. The
  generated YAML, raw ChEBI row, live OLS4 record, and PubChem CID agree on the
  exact ChEBI identifier and neutral structure.
- **Classification:** database-supported as a generated ChEBI assertion. The
  exact source row carries generic `antimicrobial agent` and `antibacterial
  agent` roles, and the `ANTIBACTERIAL` filing follows the source map.
- **Mechanism and target:** incomplete. ChEBI provides only generic antimicrobial
  and antibacterial roles; no inspected source identifies a mode of action or
  molecular target for the exact `CHEBI:46764` structure.
- **Activity:** incomplete. The record has no `ActivityObservation`, ChEBI
  supplies no exact source publication, the worklist emits no
  `activity-candidate` row, and exact PubMed identifier/name searches found no
  assay for the bare structure.
- **Producer:** empty and not currently consequential. The record has no
  definition or source lead naming a producing organism, and the worklist emits
  no `producer-candidate` row.
- **Resistance:** empty and not currently consequential. This exact ChEBI-only
  record has no CARD targets or resistance mechanisms to build on.
- **Clinical status and datasets:** empty and not currently consequential for
  this bare ChEBI scaffold seed. The inspected near-miss papers concerned
  derivative series or named derivatives rather than official products or
  durable datasets for exact `CHEBI:46764`.
- **Discussions:** empty. A future curation pass should add a `CURATION_TODO`
  only if an exact-source search is exhausted deeply enough to decide whether
  the ChEBI antibacterial role belongs to this bare structure or should be
  excluded as derivative-scaffold evidence.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has an exact ChEBI identity and generic ChEBI antibacterial role but no exact primary source for antimicrobial activity, mechanism, or a molecular target. Exact PubMed searches for the InChIKey and ChEBI structural synonyms found no hits, and the `1β-methylcarbapenem` literature leads visible in PubMed describe substituted derivative series or named derivatives rather than exact `CHEBI:46764`. | Future curator-owned `mode_of_action`, `molecular_targets`, `activity_spectrum`, and optional `discussions` on `data/antibiotics/antibacterial/1β-methylcarbapenem.yaml`, written through `write_validated_antibiotic`; if an exhaustive exact search proves the ChEBI role is scaffold-only, `curation/decisions.tsv` should exclude `antibioticmech:chebi-fe486ebf7b`. |

No blocker findings were found.

## Recommended Edits

1. Search ChEBI's upstream evidence for why `CHEBI:46764` carries
   `CHEBI:33281` and `CHEBI:33282`; if the cited evidence concerns only
   substituted derivatives, add an `EXCLUDE` decision for
   `antibioticmech:chebi-fe486ebf7b` rather than curating claims onto the exact
   bare structure.
2. Leave `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
   and `activity_spectrum` empty until an exact `CHEBI:46764` source, not a
   tomopenem, doripenem, CS-023, CS-834, L-786,392, or generic derivative-series
   paper, supports the claim.
3. If an exact antimicrobial source is found, curate the reported organism,
   strain, assay, quantitative measurement, and mechanism at their narrowest
   supported scope, then append a `CURATOR:` mode-of-action note with the correct
   microbial or host-shared target scope.
4. Leave the seeded ChEBI identifier, synonyms, parent term, structure, and
   generic roles untouched unless the ChEBI inventory or extractor changes them;
   ChEBI, OLS4, PubChem, and the committed raw row agree on the identity that
   the current record denotes.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antibacterial/1β-methylcarbapenem.yaml --out /tmp/antibioticmech-chebi-46764-strict.tsv`
  after any curator-owned mechanism, activity, or exclusion edit.
- Re-run `just verify-corpus --summary` after any seed decision or record edit
  to prove the generated YAML still reproduces exactly.
- Re-run `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-46764.tsv`
  and confirm `CHEBI:46764` leaves the `mechanism` row only after an exact
  source-backed mechanism, an explicit curator veto, or an exclusion decision is
  present.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-46764-review-queue.tsv`
  and confirm `CHEBI:46764` leaves the `MECHANISM_REVIEW` gate only after the
  exact source check has been resolved.
- Re-run the ignored-file-inclusive exact searches for `CHEBI:46764`,
  `antibioticmech:chebi-fe486ebf7b`, `1β-methylcarbapenem`, and
  `YKMONJZIUAOVEM-WDSKDSINSA-N` before deciding whether to curate or exclude the
  record.

## Additional Notes

- Exact searches for structural identifiers were intentionally separated from
  broad `1β-methylcarbapenem` searches. The broader phrase is common in
  derivative-series titles and abstracts, so those papers are scaffold leads
  only unless their structure table identifies the bare `CHEBI:46764` molecule.
- The repository publication adapter found PubMed leads for substituted
  1β-methylcarbapenem derivatives; Semantic Scholar was rate-limited on
  unauthenticated searches, so the publication search should be treated as
  bounded rather than exhaustive.

# YAML Record Review: 1-(hydroxymethyl)-5,5-dimethylhydantoin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml`
- Started UTC: 2026-09-25T08:14:00Z
- Finished UTC: 2026-09-25T08:47:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:143246` |
| Label | `1-(hydroxymethyl)-5,5-dimethylhydantoin` |
| Path | `data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:143246` / `1-(hydroxymethyl)-5,5-dimethylhydantoin` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-2733fe2bab` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, role, structure, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
  regenerated the full review queue and kept `CHEBI:143246` as
  `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0
  record evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:143246` to
  `ANTIMICROBIAL_UNSPECIFIED` with slug
  `1-hydroxymethyl-5-5-dimethylhydantoin`, matching the current record path.
- `data/raw/chebi_antimicrobials.tsv` is the ChEBI source row that seeds the
  generated target record.
- The whole target YAML was read before judging generated identity, structure,
  ChEBI provenance, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml --out /tmp/antibioticmech-chebi-143246-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-143246-worklist.tsv` | Passed after the known unrelated CARD diagnostic; exact `CHEBI:143246` rows appear only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed and confirmed that `CHEBI:143246` remains queued for absent mechanism evidence with one source literature lead, zero record evidence items, and zero targets. |
| `uv run runoak -i ols:chebi labels CHEBI:143246 CHEBI:33281 CHEBI:24628 CHEBI:73080` | Passed: OLS resolved the exact compound, the generic antimicrobial role, and both parent terms to `1-(hydroxymethyl)-5,5-dimethylhydantoin`, `antimicrobial agent`, `imidazolidine-2,4-dione`, and `hemiaminal`. |
| OLS4 term lookups for `CHEBI:143246` and `CHEBI:33281` | Passed: exact `CHEBI:143246` is current, ChEBI-defining, 3-star, and carries the same structure annotations and xrefs as the generated record; its live `RO:0000087` / `has role` relation returns only `CHEBI:33281` / `antimicrobial agent`. |
| PubChem property lookup for CID `67000` | Passed: PubChem reports the same formula `C6H10N2O3`, charge `0`, InChI, InChIKey `SIQZJFKTROUNPI-UHFFFAOYSA-N`, and IUPAC name as the ChEBI-seeded record. |

No narrower single-record reference, term, or curation-history validator is
exposed for this plain ChEBI-seeded record. The focused strict validator covered
closed schema shape, and `verify-corpus --summary` covered generated drift from
the maintained raw and path-lock inputs.

## Identity and Grounding

The generated identity is consistent with official ChEBI and PubChem for exact
`CHEBI:143246`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:143246`, `1-(hydroxymethyl)-5,5-dimethylhydantoin` | OLS4 resolved the term to the same active, ChEBI-defining label in the `3_STAR` subset. |
| Definition | Imidazolidine-2,4-dione with a hydroxymethyl group at position 1 and two methyl groups at position 5; FDA paper/board adjuvant and a DMDM hydantoin decomposition product | OLS4 returned the same definition text as the local ChEBI row. |
| Formula and charge | `C6H10N2O3`, charge `0` | Matched OLS4 and PubChem CID `67000`. |
| Masses | average `158.157`, monoisotopic `158.06914` | Matched OLS4. |
| SMILES | `CC1(C)C(=O)NC(=O)N1CO` | Matched the committed ChEBI row; PubChem's equivalent canonical form is `CC1(C(=O)NC(=O)N1CO)C`. |
| Standard InChI | `InChI=1S/C6H10N2O3/c1-6(2)4(10)7-5(11)8(6)3-9/h9H,3H2,1-2H3,(H,7,10,11)` | Matched OLS4 and PubChem CID `67000`. |
| InChIKey | `SIQZJFKTROUNPI-UHFFFAOYSA-N` | Matched OLS4 and PubChem CID `67000`. |
| Parent compounds | `CHEBI:24628`, `CHEBI:73080` | OLS resolved these to `imidazolidine-2,4-dione` and `hemiaminal`, matching the structural classes in the ChEBI row. |
| Activity role | `CHEBI:33281` | The committed ChEBI row and live OLS4 relation both assert the generic `antimicrobial agent` role. |
| Filing class | `ANTIMICROBIAL_UNSPECIFIED` | `CHEBI:33281` is in `conf/sources.yaml` as a generic in-scope role and has no narrower `role_to_class` filing map, so `data/antibiotics/unspecified/` is the expected generated directory. |

Checked exact xrefs:

| Xref | Check |
|---|---|
| `pubchem.compound:67000` | PubChem resolves CID `67000` to `1-Monomethylol-5,5-dimethylhydantoin` with matching formula, charge, InChI, InChIKey, exact mass, and IUPAC name. |
| `hmdb:HMDB0031670` | Present on official ChEBI and preserved in the generated row; not independently checked as an antimicrobial evidence source because this review used ChEBI/PubChem for structure verification and exact PubMed searches for activity/mechanism leads. |
| `cas:116-25-6`, `cas:27636-82-4`, `reaxys:139160` | Present on official ChEBI; not independently checked because the public sources used above already verified the record's exact structure and Reaxys is not publicly resolvable. |

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-local evidence.

`data/raw/chebi_antimicrobials.tsv` carries one PubMed lead for exact
`CHEBI:143246`:

| PMID | Public title/abstract support |
|---|---|
| `PMID:22633837` | Reports an HPLC method that simultaneously measures DMDM hydantoin, 1-MDMH, 3-MDMH, and DMH in cosmetics and presents 1-MDMH as a DMDMH decomposition product. The public title and abstract support chemical identity and analytical context for exact 1-MDMH, not an antimicrobial MIC, mode of action, molecular target, producer, or resistance claim. |

Bounded publication discovery:

| Query | Result |
|---|---|
| `"1-(hydroxymethyl)-5,5-dimethylhydantoin" OR "MDM hydantoin"` | PubMed returned six candidates. They covered MDMH toxicokinetics, an HMD-modified chlorinated polyurethane coating, oral toxicity, DMDMH/MDMH cosmetics quantification, formaldehyde-releaser allergy, and formaldehyde patch tests. None exposed an exact-compound MIC, target, or standalone antimicrobial mechanism for `CHEBI:143246`. Semantic Scholar returned HTTP 429. |
| `"DMDM hydantoin" antimicrobial methylol dimethylhydantoin` | PubMed returned zero candidates. Semantic Scholar returned HTTP 429. |
| `SIQZJFKTROUNPI-UHFFFAOYSA-N OR CHEBI:143246 OR PubChem 67000` | PubMed returned one candidate, `PMID:33957330`, about L-tryptophan photostability and not this compound. Semantic Scholar returned an invalid response. |

Near antimicrobial leads that still do not support curation onto this exact
compound:

| PMID | Why it is a near miss |
|---|---|
| `PMID:37317691` | Tests commercial polyurethane coatings modified with 1-(hydroxymethyl)-5,5-dimethylhydantoin as an N-halamine precursor after chlorine bleaching. The antimicrobial and antiviral effects belong to the chlorinated coating surface, not to free exact `CHEBI:143246` in a MIC-style assay. |
| `PMID:20573163` | Reviews formaldehyde releasers used as biocides in metalworking fluids and mentions MDM hydantoin in an allergy context, but it is secondary literature and not an exact primary activity or mechanism report. |
| `PMID:3378426` | Patch-tests formaldehyde-allergic patients with MDM hydantoin and DMDM hydantoin; it supports formaldehyde allergy observations, not antimicrobial activity. |

## Completeness

Consequential gaps:

- `activity_spectrum` is absent, so the record has no exact microbial taxon,
  strain, assay, MIC value, qualifier, unit, or claim-local evidence for free
  exact `CHEBI:143246`.
- `mode_of_action`, `mode_of_action_target_scope`,
  `mode_of_action_notes`, `molecular_targets`, and `causal_graphs` are absent,
  so the record has no curator-owned mechanism.
- `producer_organisms` is absent. The inspected ChEBI/PubChem/PubMed evidence
  identifies MDMH as a DMDM hydantoin decomposition product and synthetic
  preservative-related compound, not as a natural product with a named producer.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: inspected source
  metadata does not assert an antimicrobial therapeutic product or regulatory
  drug status for exact MDMH.
- No `datasets`: inspected ChEBI, PubChem, and bounded PubMed metadata did not
  surface a public screening, omics, or structural dataset accession for exact
  MDMH.
- No `structural_observations`: PubMed/PubChem searches did not surface a
  macromolecular structure involving exact MDMH.

Ignored-inclusive absence search:

- Ran `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`,
  `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`,
  `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml` for exact
  `CHEBI:143246`,
  `1-(hydroxymethyl)-5,5-dimethylhydantoin`,
  `1-hydroxymethyl-5-5-dimethylhydantoin`,
  `SIQZJFKTROUNPI-UHFFFAOYSA-N`, `antibioticmech:chebi-2733fe2bab`, and
  `PMID:22633837`.
- The searches included ignored files. They found the generated target, the
  ChEBI raw row, `PATHS.tsv`, and the derived review-queue row. They found no
  prior `CHEBI:143246` review report, no `curation/decisions.tsv` row, and no
  curated activity, mechanism, resistance, or producer addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | MDMH-M1 | The record is still a ChEBI-seeded exact-structure stub with a generic antimicrobial role but no exact-compound activity observation, mode of action, mechanism scope, molecular target, resistance mechanism, or causal graph. It cannot qualify as `REVIEWED`. | The regenerated worklist places `CHEBI:143246` only in `mechanism` and `review-readiness`; `review-readiness` reports one source literature lead, zero record evidence items, and zero targets. The exact ChEBI PubMed lead supports DMDMH/MDMH analytical chemistry rather than antimicrobial activity, and bounded exact PubMed searches surfaced no primary MIC or target paper for free exact MDMH. | `data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml`, through a guarded curator-owned record mutation and new `CurationEvent`; or `curation/decisions.tsv` if exact MDMH antimicrobial activity cannot be verified. |

No blocker or minor findings.

## Recommended Edits

1. Keep the generated `CHEBI:143246` identity, structure, parent compounds,
   PubChem/HMDB/CAS/Reaxys xrefs, generic `CHEBI:33281` activity role, filing
   class, and source concept unchanged.
2. Inspect full text for `PMID:22633837` only as a structure and chemistry lead;
   do not treat its DMDM hydantoin decomposition-product assay as antimicrobial
   evidence unless the paper reports a direct activity measurement for exact
   1-MDMH.
3. Inspect `PMID:37317691` only if a future curation task wants to document a
   related N-halamine surface-disinfection material; do not curate its
   chlorinated-polyurethane coating activity as free `CHEBI:143246` activity.
4. Search formaldehyde-releasing preservative literature for primary studies
   that test exact MDMH and report a bounded activity format such as MIC,
   minimum fungicidal concentration, organism/strain, and assay. Add
   `activity_spectrum` and mechanistic fields only when the source distinguishes
   exact MDMH from DMDMH and 5,5-dimethylhydantoin.
5. If exact free-MDMH antimicrobial activity remains unsupported after
   full-text review, leave the record `SEEDED` and add a curator discussion or
   a `curation/decisions.tsv` decision to track the ChEBI-derived role rather
   than promoting the record to `REVIEWED`.

## Follow-up Checks

After any future curation, run the focused and derived-corpus gates:

1. `just validate data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml`
2. `just validate-strict data/antibiotics/unspecified/1-hydroxymethyl-5-5-dimethylhydantoin.yaml --out /tmp/antibioticmech-chebi-143246-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-143246-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`

Also re-run exact PubMed and Semantic Scholar searches for `1-MDMH`, `MDMH`,
`methylol dimethylhydantoin`, `monomethylol dimethylhydantoin`,
`CHEBI:143246`, `PubChem 67000`, and `SIQZJFKTROUNPI-UHFFFAOYSA-N` before
concluding that an activity or mechanism gap remains unresolved.

## Additional Notes

- The record has only seed and reseed curation-history events from
  `2026-08-30`, accurately matching its generated `SEEDED` state.
- The exact `PMID:22633837` search result names
  `1-hydroxymethyl-5,5-dimethylhydantoin` as `1-MDMH`; this is the same
  structure as `CHEBI:143246`, not `DMDM hydantoin`.
- The NCBI email environment variable was explicitly unset for all
  `scripts/search_publications.py` calls.
- Semantic Scholar was unavailable for this review because the exact-name and
  DMDM/MDMH searches returned HTTP 429 and the identifier search returned an
  invalid-response error. PubMed succeeded and provided the bounded literature
  results summarized above.

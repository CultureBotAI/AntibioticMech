# YAML Record Review: 12-demethylmulticaulin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml
- Started UTC: 2026-09-25T17:22:00Z
- Finished UTC: 2026-09-25T17:25:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66408` |
| Label | `12-demethylmulticaulin` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml` |

This is a ChEBI-seeded record with one source concept:

```text
CHEBI:66408  12-demethylmulticaulin  source_version=2026-08-30
```

The source concept contributes one antimicrobial role, `CHEBI:33231`
(`antitubercular agent`), and one source literature lead, `PMID:9428161`.

An ignored-file-inclusive search over `reports`, `curation`, `data/raw`,
`data/antibiotics`, and `.git` for `CHEBI:66408` and
`12-demethylmulticaulin` found only:

- the active review queue row in `curation/record_review_queue.tsv`;
- the raw ChEBI row in `data/raw/chebi_antimicrobials.tsv`;
- the generated path lock row in `data/antibiotics/PATHS.tsv`; and
- the target YAML.

There was no prior exact review report or duplicate curated YAML in the
maintained/generated corpus searched above.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml --out /tmp/antibioticmech-chebi-66408-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66408.tsv` | Passed; the exact rows for this record were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi66408-review-queue.tsv` | Passed; `CHEBI:66408` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

`just verify-corpus --summary` printed the known unrelated
`ARO:3000337`/iclaprim CARD cross-reference warning; it did not involve this
record.

The OAK `runoak` CLI was not available in this checkout, so live ChEBI
verification used OLS JSON responses instead.

## Identity and Grounding

The generated ChEBI identity is internally consistent:

- Live OLS4 resolved `CHEBI:66408` as a current, non-obsolete, 3-star ChEBI term
  labeled `12-demethylmulticaulin`.
- The live OLS4 term matched the record definition, formula `C19H20O`, charge
  `0`, average mass `264.368`, monoisotopic mass `264.15142`, SMILES,
  Standard InChI, Standard InChIKey `ZMSKUQUFEKLXGK-UHFFFAOYSA-N`,
  `reaxys:7873031`, and `pubmed:9428161`.
- PubChem resolved `ZMSKUQUFEKLXGK-UHFFFAOYSA-N` to CID `467783`; CID `467783`
  matched formula `C19H20O`, Standard InChI, InChIKey, IUPAC name
  `7,8-dimethyl-2-propan-2-ylphenanthren-3-ol`, exact mass
  `264.151415257`, monoisotopic mass `264.151415257`, and charge `0`.
- OLS resolved the record's ChEBI parent terms as current, non-obsolete
  `CHEBI:23849` (`diterpenoid`), `CHEBI:25961` (`phenanthrenes`), and
  `CHEBI:33853` (`phenols`).
- OLS resolved `CHEBI:66408` as having the antimicrobial role `CHEBI:33231`
  (`antitubercular agent`).

The ChEBI role maps correctly to repository class `ANTIMYCOBACTERIAL`.
The exact source row in `data/raw/chebi_antimicrobials.tsv` and path row in
`data/antibiotics/PATHS.tsv` both agree with the target YAML.

## Evidence

`PMID:9428161` resolves to Ulubelen, Topcu, and Johansson,
"Norditerpenoids and diterpenoids from Salvia multicaulis with antituberculous
activity", *Journal of Natural Products* 60(12):1275-1280, DOI
`10.1021/np9700681`.

PubMed's abstract supports the broad identity and activity claims that ChEBI
copied into the definition:

- the paper isolated compound 2, spelled `12-demethylmulticauline` in the
  abstract, from the roots of `Salvia multicaulis`;
- the structures of compounds 1-7 were established with 1D/2D NMR and chemical
  methods; and
- the antituberculous activity of compounds 1-7 was tested against
  `Mycobacterium tuberculosis` strain H37Rv, with all compounds active and
  compounds 2 and 4-6 reported as the most potent.

The DOI resolves to ACS but unauthenticated `curl` was blocked by a Cloudflare
`403` challenge, and Europe PMC marks the DOI full text as subscription-only.
That left the compound 2 MIC/assay table uninspected, so the review confirmed
qualitative H37Rv activity from the PubMed abstract but did not confirm the
exact MIC value or method.

The bounded exact PubMed search for `12-demethylmulticaulin`,
`12-demethylmulticauline`, and the InChIKey found the ChEBI source paper plus
several later review, in silico, analog-synthesis, or Salvia-quantitation leads.
The inspected later abstracts did not provide primary compound-specific MIC or
mode-of-action evidence for this exact ChEBI structure.

## Completeness

The record has enough seeded information to establish a current exact ChEBI
identity, structure, source PMID, source role, filing class, and three strictly
broader ChEBI parents.

Consequential gaps remain:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
  `causal_graph`, and `resistance_mechanisms` are absent. The regenerated
  worklist confirms there are no CARD target or resistance edges to build on,
  and none of the inspected source metadata named a compound-specific molecular
  target.
- `activity_observations` is absent even though the source abstract says the
  exact compound was tested against `Mycobacterium tuberculosis` H37Rv
  (`NCBITaxon:83332`). The full ACS table is still needed for the exact MIC
  value, units, and assay.
- `producer_organisms` is absent. The definition and source abstract identify
  `Salvia multicaulis` roots as the isolation source, and NCBI Taxonomy resolves
  `Salvia multicaulis` to `NCBITaxon:1685714`, but no structured producer claim
  has yet been curated.

Optional clinical-status and dataset fields are correctly empty; no inspected
source suggested an approved product or public dataset specific to this exact
compound.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has no curated antimicrobial mechanism, molecular target, causal edge, resistance route, or structured H37Rv activity observation. `PMID:9428161` is enough to verify qualitative antitubercular activity against `M. tuberculosis` H37Rv, but the original ACS table remains uninspected and none of the inspected later abstracts identified a supported molecular target for `12-demethylmulticaulin`. | Curator-owned fields on `data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml` |
| F2 | Minor | `Salvia multicaulis` is only represented inside the generated ChEBI definition. The paper abstract supports roots of this plant as the isolation source and the worklist already flags the phrase as `producer-candidate`; a curator should decide whether that is enough to add `NCBITaxon:1685714` as a plant producer with claim-level `PMID:9428161` evidence. | Curator-owned `producer_organisms` on `data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml` |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:9428161`, capture compound 2's exact
   H37Rv result as an `ActivityObservation` with `taxon_id: NCBITaxon:83332`,
   strain `H37Rv`, `mic_value`, `mic_units`, `assay`, and claim-level
   `PMID:9428161`/DOI evidence.
2. Search for primary literature that tests `12-demethylmulticaulin` against a
   named microbial molecular target. If found, add `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, and edge-level
   `causal_graph` entries through the guarded writer. If no target evidence is
   found, leave mechanism fields empty and add a bounded `CURATION_TODO`
   discussion documenting the negative search.
3. Decide the `Salvia multicaulis` producer lead. If accepted, add a
   `ProducerOrganism` with `taxon_id: NCBITaxon:1685714`,
   `taxon_label: Salvia multicaulis`, and `PMID:9428161` evidence scoped to
   isolation of 12-demethylmulticaulin from the roots.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antimycobacterial/12-demethylmulticaulin.yaml --out /tmp/antibioticmech-chebi-66408-strict.tsv`
  after any record mutation.
- Re-run `just verify-corpus --summary` to ensure no seeded fields drifted while
  curator-owned fields were added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi66408-review-queue.tsv`
  and confirm `CHEBI:66408` leaves the `MECHANISM_REVIEW` gate only after a
  supported mechanism or explicit mechanism TODO is curated.
- If a producer claim is added, re-run
  `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66408.tsv`
  and confirm the `producer-candidate` row is resolved.

## Additional Notes

- The OLS4 term endpoint worked for `CHEBI:66408`, but OLS4 parent and relation
  endpoints returned empty bodies during this review. The same parent and
  `has_role` checks were completed through OLS3 relation endpoints.
- Europe PMC's broad exact-label query returned many false positives because
  `12-demethylmulticaulin` contains the token `12`. The narrower PubMed exact
  title/abstract query was the useful bounded literature search.
- The PubMed abstract uses the spelling `12-demethylmulticauline`; ChEBI and
  later anti-TB phytochemical papers also use `12-demethylmulticaulin`, and the
  structure/InChIKey verified that the generated record denotes the intended
  compound 2.

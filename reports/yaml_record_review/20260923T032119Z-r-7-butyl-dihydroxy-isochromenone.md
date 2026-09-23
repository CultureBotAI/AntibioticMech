# YAML Record Review: (R)-7-butyl-6,8-dihydroxy-3-[(3E)-pent-3-en-1-yl]-3,4-dihydroisochromen-1-one

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml`
- Started UTC: `2026-09-23T03:18:05Z`
- Finished UTC: `2026-09-23T03:21:19Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65537` |
| Label | `(R)-7-butyl-6,8-dihydroxy-3-[(3E)-pent-3-en-1-yl]-3,4-dihydroisochromen-1-one` |
| Path | `data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml` |
| Class | `ANTIMYCOBACTERIAL` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:65537` |
| Structure | `RNIKQZXKWIZFHL-MASHWEEQSA-N`, formula `C18H24O4`, charge `0` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, xref, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:65537` resolves through
`data/antibiotics/PATHS.tsv` to the antimycobacterial record
`data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml --out /tmp/r-7-butyl-dihydroxy-isochromenone-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 105` | Pass; `CHEBI:65537` remains immediately after the already-reviewed `(R)-4-hydroxy-1-methyl-L-proline` row with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/r-7-butyl-dihydroxy-isochromenone-worklist.tsv` | Pass; the relevant entries were `mechanism`, `producer-candidate`, and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, activity-candidate, structure, scope, or target-evidence defects. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '12762815[uid]' --limit 20 --output /tmp/r-7-butyl-dihydroxy-isochromenone-pmid-publications.jsonl` | PubMed returned the exact ChEBI source PMID lead. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"RNIKQZXKWIZFHL" OR "7-butyl-6,8-dihydroxy" antimycobacterial Geotrichum mechanism target' --limit 20 --output /tmp/r-7-butyl-dihydroxy-isochromenone-broad-publications.jsonl` | PubMed returned 0 candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior review,
curator decision, duplicate exact InChIKey, an exact DOI lead, and the minted
source identifier used `rg --no-ignore --hidden` or `find`, so ignored
`reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:65537` exactly matches the generated identity:

- label `(R)-7-butyl-6,8-dihydroxy-3-[(3E)-pent-3-en-1-yl]-3,4-dihydroisochromen-1-one`
- 3-star ChEBI entry with `EXACT` grounding
- ChEBI role terms `CHEBI:33231`, `CHEBI:35718`, and `CHEBI:38068`
- broader parents `CHEBI:33853` and `CHEBI:38762`
- Standard InChIKey `RNIKQZXKWIZFHL-MASHWEEQSA-N`
- xref `reaxys:9582012`

The ChEBI exact synonym list covers the name used by the apparent primary
paper: PubMed `PMID:12762815` names the same molecule as
`7-butyl-6,8-dihydroxy-3(R)-pent-11-enylisochroman-1-one`, compound 1.

An ignored-inclusive search over `data/raw`, `data/antibiotics`, `curation`, and
`reports` found the exact InChIKey only in the ChEBI raw row and this generated
YAML record. The same bounded search found the minted source identifier
`antibioticmech:chebi-5f6f042c05` only in the generated YAML, with no
`curation/decisions.tsv` override or prior review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonyms, role, parent, xref, and structure fields | Database-seeded from the `CHEBI:65537` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| Antimycobacterial, antimalarial, and antifungal roles | `PMID:12762815` supports an exact literature lead for this compound: the PubMed abstract reports that three dihydroisocoumarins, including this compound as 1, were isolated by bioassay-guided fractionation from an endophytic `Geotrichum sp.` collected from `Crassocephalum crepidioides` and had antimalarial, antituberculous, and antifungal activities. The abstract does not provide per-compound assay values or a molecular target. |
| Fungal source text in the ChEBI definition | `PMID:12762815` supports `Geotrichum sp.` as the isolated endophyte source and also reports `Crassocephalum crepidioides` as the plant from which that fungus was collected. The abstract does not resolve the fungal isolate to a binomial. |

The record has no `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`causal_graphs`, or record-level literature `evidence` items to overstate. No
existing citation is attached to a broader claim than it supports.

## Completeness

The record is not complete enough for `REVIEWED` because the mechanism gate is
unsettled:

- `mode_of_action` and `mode_of_action_target_scope` are absent.
- `molecular_targets` is absent.
- `causal_graphs` is absent.
- `activity_observations` is absent even though `PMID:12762815` reports
  antituberculous, antifungal, and antimalarial activity for a three-compound
  dihydroisocoumarin set including this compound.
- `producer_organisms` is absent. The ChEBI definition names only the genus
  `Geotrichum`, and the worklist correctly keeps this as a
  `producer-candidate` with no binomial rather than asserting an unresolved
  taxon.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

The exact PMID appears only on `CHEBI:65537` in local ChEBI source rows. Future
activity curation still needs the full text before copying any MIC or IC50
value to the record, because the abstract pools several compounds and
phenotypes.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `causal_graphs`, and `activity_observations` are absent even though exact phenotype literature exists for this dihydroisocoumarin. The PubMed abstract for `PMID:12762815` supports antituberculous, antifungal, and antimalarial activity for a small compound set that includes `CHEBI:65537`, but it does not state a mechanism or enough per-compound assay detail to add exact activity rows from the abstract alone. | Curator-owned additions in `data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect `PMID:12762815` in full text and decide whether compound 1 supports
   defensible `ActivityObservation` rows against its reported antituberculous,
   antimalarial, or antifungal assay organisms, including exact values,
   qualifiers, and units.
2. Resolve whether `Geotrichum sp.` from `Crassocephalum crepidioides` can be
   asserted as a `ProducerOrganism`; preserve the unresolved isolate or host
   context in notes if the fungal source cannot be grounded to an NCBI binomial.
3. Leave `mode_of_action` unset unless full-text primary evidence supports a
   specific target or pathway; add a curator-owned `Discussion` for an
   unresolved mechanism gap if the paper reports only phenotypic assays.
4. Add `molecular_targets` only if primary evidence supports a target beyond the
   compound's antituberculous, antimalarial, or antifungal phenotype.
5. Add a causal graph only after the activity and any mechanism interpretation
   are resolved; every edge needs its own primary-paper `EvidenceItem`.
6. Leave the seeded identity, xrefs, `parent_compounds`, and class untouched
   unless a ChEBI refresh or `curation/decisions.tsv` row changes the maintained
   import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/antimycobacterial/r-7-butyl-6-8-dihydroxy-3-3e-pent-3-en-1-yl-3-4-dihydroisochromen-1-on.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun
  `just worklist --limit 0 --tsv /tmp/r-7-butyl-dihydroxy-isochromenone-worklist.tsv`
  and confirm the `CHEBI:65537` `mechanism`, `producer-candidate`, and
  `review-readiness` rows changed as intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- The bounded, ignored-inclusive DOI search found no committed
  `10.1021/np0205598` reference.
- The local exact-InChIKey search did not find any other source row or generated
  record with `RNIKQZXKWIZFHL-MASHWEEQSA-N`; ignored `reports` were included.
- Semantic Scholar was rate-limited with HTTP 429 and was not treated as a
  negative source.

# YAML Record Review: (E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml`
- Started UTC: 2026-09-22T17:10:00Z
- Finished UTC: 2026-09-22T17:42:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70401` |
| Label | `(E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione` |
| Path | `data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:70401`, version `2026-08-30`, minted key `antibioticmech:chebi-8e3dcb1e88` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:17087` ketone; `CHEBI:26455` pyrroles; `CHEBI:29347` monocarboxylic acid amide |
| Structure | `JGNMZTXDOHXIJQ-ONEGZZNKSA-N`; formula `C15H23NO2`; charge `0` |
| Xrefs | `reaxys:8060218` |
| Source literature leads | `PMID:21053938` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione`. The YAML has
exact ChEBI grounding, the ChEBI definition, one IUPAC synonym, three ChEBI
parents, the antifungal ChEBI role, one Reaxys xref, structure, and
source-concept metadata. It has no document xrefs, generated or curator-owned
mode of action, molecular target, activity observation, producer organism,
resistance mechanism, dataset, discussion, causal graph, or claim-level
evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml --out /tmp/antibioticmech-chebi-70401-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-70401-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:70401` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just review-queue --limit 86` | Pass: `CHEBI:70401` is queued with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:70401` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label
`(E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione`, the same
definition, the exact Standard InChIKey `JGNMZTXDOHXIJQ-ONEGZZNKSA-N`, formula
`C15H23NO2`, neutral charge, matching average and monoisotopic masses, the same
SMILES, the exact `reaxys:8060218` xref, and the same source
`PMID:21053938` xref.

The generated YAML stores the one source ChEBI synonym
`(8E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione`. OLS exposes
that IUPAC synonym twice, once as an exact synonym and once as a related
synonym; the local seeder correctly de-duplicates it to one generated
`synonyms` item.

The live OLS graph gives `CHEBI:70401` three direct parents: `CHEBI:17087`,
`ketone`; `CHEBI:26455`, `pyrroles`; and `CHEBI:29347`,
`monocarboxylic acid amide`. The live OLS `has_role` relation gives the term two
roles: `CHEBI:35718`, `antifungal agent`, and `CHEBI:76964`,
`Penicillium metabolite`. Only `CHEBI:35718` is an antimicrobial role in
`conf/sources.yaml`, and the committed source configuration maps that role to
generated filing class `ANTIFUNGAL`.

The committed ChEBI inventory row for `CHEBI:70401` has the same label,
definition, 3-star status, antifungal role, parents, SMILES, Standard InChI,
Standard InChIKey, formula, neutral charge, masses, IUPAC synonym, Reaxys xref,
and source PubMed identifier that were used to seed this record. `PATHS.tsv`
maps `CHEBI:70401` to
`ANTIFUNGAL/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione`,
matching the generated path and filing class.

The one adjacent ChEBI record visible in the committed inventory,
`CHEBI:70402`, has the same antifungal role, ChEBI parents, and source PMID but
is the saturated sibling
`1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldecane-1,3-dione` with a different
Standard InChIKey, `HMWIYUSLKIYYER-UHFFFAOYSA-N`. The generated
`CHEBI:70401` record therefore denotes the unsaturated exact structure rather
than a duplicate or alternate spelling of that sibling.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:70401`, the exact file stem, the exact label, the exact IUPAC synonym,
the exact minted key, `reaxys:8060218`, and the exact Standard InChIKey across
`reports/yaml_record_review`, `data/antibiotics`, `data/raw`, `curation`,
`conf`, `.claude`, `CLAUDE.md`, and `justfile` found only the expected
generated YAML, `PATHS.tsv` row, raw ChEBI row, `record_review_queue.tsv` row,
and sibling `CHEBI:70402` rows that share only the source PMID. An
ignored-inclusive filename search for `*pyrrol*` under
`reports/yaml_record_review` found no prior report for this record.

## Evidence

The record's antifungal classification is inherited from committed ChEBI role
`CHEBI:35718`, `antifungal agent`. `data/raw/chebi_role_names.tsv` marks that
role as a ChEBI scope role, and `conf/sources.yaml` maps it to generated class
`ANTIFUNGAL`. That role is enough for reproducible source-level filing but not
enough to fill a specific activity observation, producer assertion, mode of
action, target, or causal graph.

`PMID:21053938`, titled `Use of experimental design for the optimization of the
production of new secondary metabolites by two Penicillium species`, resolves
to DOI `10.1021/np100470h` and is a primary Journal of Natural Products article
about optimizing secondary-metabolite production in two Penicillium strains.
The PubMed abstract confirms the organism and secondary-metabolite context but
does not name exact `CHEBI:70401`, report an exact antifungal assay endpoint,
or assert a mode of action or target in abstract-visible metadata. The DOI
redirected to ACS and was not manually inspectable from the local command line
because ACS returned a Cloudflare challenge page.

The exact-label/Penicillium publication-helper query returned zero PubMed
candidates and Semantic Scholar returned HTTP 429. The bounded search therefore
did not find an immediate primary-paper lead beyond `PMID:21053938` for
exact-compound antifungal activity, mechanism, target, resistance, dataset,
clinical, or causal-graph assertions.

## Completeness

The record is incomplete as a reviewed antifungal record. It has exact ChEBI
identity, structure, parentage, xref, source-level antifungal classification,
and reproducible source metadata, but no curator-owned exact-compound activity,
mode-of-action, molecular-target, producer, or causal-graph claims.

The empty `mode_of_action`, `molecular_targets`, and causal-graph slots are
acceptable for the current seed. No exact-compound fungal target or
antimicrobial mechanism was visible in the inspected PubMed abstract or bounded
exact-label search.

The empty `producer_organisms` slot is acceptable for the current seed but
actionable for a future curation pass. The ChEBI definition states that the
compound was isolated from `Penicillium citrinum` and
`Penicillium brevicompactum`; `just worklist` already places the record on the
`producer-candidate` queue for `Penicillium citrinum`, and a full-text review of
the source PMID should check both named species and any reported strains before
adding claim-level `ProducerOrganism` entries.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`, and
`discussions` slots are acceptable for the current seed. No measured resistance
edge, standalone clinical status assertion, public dataset accession, or
discussion-worthy identity conflict was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:70401` has source-level antifungal classification and a ChEBI source PMID, but no curator-owned exact-compound activity, mode-of-action, target, producer, or causal-graph claim. | The generated record has one source PubMed lead, zero record evidence items, zero `activity_spectrum` rows, zero targets, no `mode_of_action`, and no `producer_organisms`. `just worklist` places the record on `mechanism`, `producer-candidate`, and `review-readiness`. The PubMed abstract for `PMID:21053938` establishes a Penicillium secondary-metabolite paper but does not expose exact `CHEBI:70401` susceptibility, producer-strain, target, or mechanism assertions. | Future curator-owned fields on `data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Review the full text of `PMID:21053938`. If it reports exact antifungal
   measurements for pure
   `(E)-1-(2,3-dihydro-1H-pyrrol-1-yl)-2-methyldec-8-ene-1,3-dione`, add
   claim-level `ActivityObservation` entries with organism, strain, assay,
   value, unit, and evidence details.
2. In the same full text, verify which Penicillium species and strains produced
   exact `CHEBI:70401`. Add `ProducerOrganism` entries for
   `Penicillium citrinum` or `Penicillium brevicompactum` only when the source
   supports biosynthesis or isolation for that exact compound, not merely an
   optimized bioactive extract.
3. Leave `mode_of_action`, `molecular_targets`, resistance mechanisms, and the
   causal graph empty unless a primary source supports an antimicrobial
   mechanism for exact `CHEBI:70401`.
4. Leave source-owned ChEBI identity, structure, role, parent, synonym, and xref
   fields untouched unless the committed ChEBI inventory diverges from OLS or a
   curator decision needs to exclude a proven wrong source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml`
2. `just validate-strict data/antibiotics/antifungal/e-1-2-3-dihydro-1h-pyrrol-1-yl-2-methyldec-8-ene-1-3-dione.yaml --out /tmp/antibioticmech-chebi-70401-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-70401-worklist.tsv`
5. `just review-queue --limit 86`
6. `just qc`

Manually compare any future activity, producer, mode-of-action, target, dataset,
discussion, or causal-graph assertion against exact `CHEBI:70401` identity.
Confirm that every claim-level evidence block attaches to the specific object it
supports, not only to the whole ChEBI term, the source antifungal-agent role, a
bioactive Penicillium extract, or sibling `CHEBI:70402`.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden` or `find`, so
they included ignored `reports/` files.

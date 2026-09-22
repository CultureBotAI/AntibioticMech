# YAML Record Review: (2R)-2-[(1R)-4-methylcyclohex-3-en-1-yl]propanoic acid

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml`
- Started UTC: 2026-09-22T02:49:00Z
- Finished UTC: 2026-09-22T02:52:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:141292` |
| Label | `(2R)-2-[(1R)-4-methylcyclohex-3-en-1-yl]propanoic acid` |
| Path | `data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:141292`, version `2026-08-30`, minted key `antibioticmech:chebi-bca084b3a0` |
| Source role | `CHEBI:35718` antifungal agent |
| Structure | `QOGOGJNRMJOCKH-BDAKNGLRSA-N`; formula `C10H16O2`; charge `0` |
| Same-structure xrefs | `reaxys:7014122` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded monoterpenoid carboxylic acid
record. The YAML has source-derived identity, definition, synonyms, ChEBI
parents, antifungal role, structure, Reaxys xref, and source-concept metadata,
but no curator-owned mode of action, target, activity observation, producer,
resistance mechanism, discussion, dataset, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml --out /tmp/antibioticmech-chebi-141292-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-141292.tsv` | Pass: the full worklist TSV was written. `CHEBI:141292` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it is absent from the `xref-unverified`, `xref-span-conflict`, `xref-name-conflict`, `multi-component`, `moa-scope`, `unknown-mech`, and `target-evidence` queues. |
| `just review-queue --limit 44` | Pass: `CHEBI:141292` is the next queued record after `CHEBI:65995`; its row says `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, worklist, and
`verify-corpus` are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:141292` resolves in official OLS as a current, non-obsolete, 3-star
ChEBI term labeled `(2R)-2-[(1R)-4-methylcyclohex-3-en-1-yl]propanoic acid`.
The live OLS annotations list the same formula, charge, average mass,
monoisotopic mass, Standard InChI, Standard InChIKey, SMILES, PubMed xref, and
Reaxys xref as the committed `data/raw/chebi_antimicrobials.tsv` row and the
generated YAML.

The generated record's two `parent_compounds` are exactly the official OLS
direct parents of `CHEBI:141292`: `CHEBI:25384` monocarboxylic acid and
`CHEBI:25409` monoterpenoid. They are strictly broader chemical classes, not
same-structure identities.

The `ANTIFUNGAL` filing class is source-backed. Official OLS lists
`CHEBI:35718` antifungal agent as a direct `has_role` filler on
`CHEBI:141292`, and the generated record preserves that in-scope ChEBI role in
`activity_roles`. OLS also lists `CHEBI:76946` fungal metabolite as a
source-supported role, but it is not an antimicrobial role and is intentionally
not imported into `activity_roles`.

The generated `reaxys:7014122` xref is copied from the 3-star ChEBI entry and
is internally consistent with the committed raw ChEBI row. This review could
not verify Reaxys live because Reaxys is not a public resolver, but
`just worklist` did not flag `CHEBI:141292` in any xref-conflict or
xref-unverified queue.

An ignored-inclusive search for `CHEBI:141292`,
`QOGOGJNRMJOCKH-BDAKNGLRSA-N`, `antibioticmech:chebi-bca084b3a0`,
`reaxys:7014122`, and `PMID:27448166` across `data/antibiotics`, `data/raw`,
`curation`, and `reports` found only the expected `PATHS.tsv` row, the
generated YAML, the raw ChEBI row, the review-readiness row, the same-source
sibling raw and queue rows for `CHEBI:141296`, and a prior review report that
mentions this record as that sibling. No dedicated prior review report, curator
decision, generated mechanism, activity observation, or producer assertion
resolves `CHEBI:141292`.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for
a ChEBI-seeded record because the source concept supplies database provenance
and no mechanism, target, activity, resistance, producer, dataset, or causal
claim has been promoted into curator-owned slots.

The only committed ChEBI literature lead, `PMID:27448166`, resolves in PubMed
and Crossref to Xu, Zhang, and Yang 2016,
`DOI:10.1002/cbdv.201600114`, "Antifungal Monoterpene Derivatives from the
Plant Endophytic Fungus Pestalotiopsis foedan." PubMed identifies
`CHEBI:141292` as compound 2 from liquid culture of the plant endophytic fungus
named in the paper as `Pestalotiopsis foedan`, and reports that compounds 1 and
2 showed antifungal activity against `Botrytis cinerea` and
`Phytophthora nicotianae`; the abstract additionally reports compound 2
activity against `Candida albicans` with MIC 50 microg/ml.

The PubMed abstract is exact for this compound as an activity lead, but not a
complete `ActivityObservation` source by itself. It does not supply all strain,
assay-method, endpoint, qualifier, and per-organism MIC details that a curator
must check in the full article before attaching MIC rows to `activity_spectrum`.

The same PubMed abstract is a producer lead because it says compound 2 was
isolated from a liquid culture of the fungus named as `Pestalotiopsis foedan`.
The generated record has no `producer_organisms` entry; a later curation pass
should resolve the current fungal taxonomy, strain if available, and host plant
context from the paper rather than treating the definition sentence alone as a
structured producer assertion.

A bounded repository publication search for exact compound labels, the
InChIKey, `DOI:10.1002/cbdv.201600114`, and `Pestalotiopsis foedan` found three
PubMed candidates: the exact target paper and two older `Pestalotiopsis foedan`
natural-product papers about different compounds. A second exact-label search
with mechanism, target, and tested-organism terms found no PubMed candidates.
Semantic Scholar returned HTTP 429 for both searches.

NCBI Taxonomy exact-name search resolved `Neopestalotiopsis foedans` to active
species taxon `290095`; an exact all-names search for the historical spelling
`Pestalotiopsis foedan` found no item. This does not block the current
generated chemical record because no NCBITaxon CURIE is asserted.

## Completeness

The record is incomplete as a reviewed antimicrobial record. It has exact ChEBI
identity, structure, parents, xref, and antifungal role, but the associated
primary paper has not been resolved into claim-level activity observations, a
producer organism, an antimicrobial mode of action, a molecular target, or a
causal graph.

The empty `mode_of_action`, `molecular_targets`, `causal_graphs`,
`resistance_mechanisms`, and `datasets` slots are preferable to over-scoped
filler. No inspected source identified an antifungal molecular target,
resistance route, causal pathway, or public dataset for the exact monoterpenoid
acid.

`just worklist` correctly reports a `producer-candidate` row for
`Pestalotiopsis foedan` because the ChEBI definition says the compound was
obtained from that endophytic fungus. The candidate is a source-only lead, not
yet a strain-scoped biosynthesis claim.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact primary-paper lead for `CHEBI:141292` has not been resolved into activity, producer, or mechanism curation. | The YAML has no evidence-bearing objects; `just worklist` queues the record on `mechanism`, `producer-candidate`, and `review-readiness`; PubMed resolves PMID:27448166 and names this compound as compound 2 with antifungal MICs, but the record has no activity observations, producer claim, or mechanism disposition. | Future curator-owned fields on `data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, or same-structure xref findings were
found.

No minor findings.

## Recommended Edits

1. Inspect the full `PMID:27448166` article and supporting information. Add one
   `ActivityObservation` per exact organism or strain only where the source
   supplies the assay, endpoint, value, qualifier, and units for compound 2.
2. Resolve the taxonomy and culture context for `Pestalotiopsis foedan`. If the
   full paper supports biosynthesis by the cultured fungus, add a
   `producer_organisms` claim with the current NCBITaxon species CURIE and
   preserve the historical source name plus `Bruguiera sexangula` branch
   context in notes.
3. Keep the CHEBI:141292 and CHEBI:141296 curation separate even though both
   records point at PMID:27448166. Activity, producer, or mechanism curation for
   one sibling should be copied to the other only after the full source supports
   the exact claim for both numbered compounds.
4. Curate `mode_of_action`, `mode_of_action_target_scope`, molecular targets,
   or causal-graph edges only if the paper or a follow-on exact-compound source
   explains how compound 2 inhibits fungal growth.

## Follow-up Checks

After any curation, rerun:

1. `just validate data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml`
2. `just validate-strict data/antibiotics/antifungal/2r-2-1r-4-methylcyclohex-3-en-1-yl-propanoic-acid.yaml --out /tmp/antibioticmech-chebi-141292-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-141292.tsv`
5. `just review-queue --limit 44`
6. `just qc`

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Semantic Scholar returned HTTP 429 for both repository publication searches; the
PubMed side of both searches completed.

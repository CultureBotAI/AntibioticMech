# YAML Record Review: (E)-2-[[[4-(2-chlorophenyl)-1,3-thiazol-2-yl]hydrazinylidene]methyl]benzoic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml`
- Started UTC: 2026-09-22T18:42:30Z
- Finished UTC: 2026-09-22T18:50:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml` |
| Class | `ANTIVIRAL` |
| ID | `CHEBI:167669` |
| Label | `(E)-2-[[[4-(2-chlorophenyl)-1,3-thiazol-2-yl]hydrazinylidene]methyl]benzoic acid` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from the committed ChEBI inventory |

The target is a ChEBI-grounded S312 record with InChIKey
`DDEIFUOYHWEWSS-DJKKODMXSA-N`, a single ChEBI source concept
`CHEBI:167669`, antimicrobial filing class `ANTIVIRAL`, retained ChEBI
activity roles `CHEBI:149553` and `CHEBI:22587`, and no `record_evidence`,
`mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
`activity_observations`, `producer_organisms`, `causal_graphs`, `datasets`,
`discussions`, or `resistance_mechanisms`.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml --out /tmp/antibioticmech-chebi-167669-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` drift. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-167669-worklist.tsv` | Passed; `CHEBI:167669` appears on `mechanism`, `activity-candidate`, and `review-readiness`. The command also printed the unrelated known `ARO:3000337` cross-reference warning. |
| `just review-queue --limit 95` | Passed and confirmed `CHEBI:167669` is the first unreported queue row after the last merged report for `CHEBI:137441`. |
| `curl -L -f -sS https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/...CHEBI_167669` | Passed; OLS resolved a live, non-obsolete, 3-star `CHEBI:167669` term with the same label, definition, synonyms, formula, charge, masses, SMILES, Standard InChI, InChIKey, `pdb-ccd:3X2` xref, and `pubmed:32754890` xref as the generated inventory row. |
| `curl -L -f -sS https://data.rcsb.org/rest/v1/core/chemcomp/3X2` | Passed; PDB CCD component `3X2` has the same Standard InChI and InChIKey as the record. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query 32754890 --limit 20 --output /tmp/antibioticmech-chebi-167669-pmid-publication.jsonl` | Passed; PubMed resolved the exact ChEBI source PMID to Xiong et al. 2020, Protein & Cell, DOI `10.1007/s13238-020-00768-w`. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query "10.1007/s13238-020-00768-w S312" --limit 20 --output /tmp/antibioticmech-chebi-167669-doi-publication.jsonl` | Passed; PubMed resolved the same S312 article by DOI. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query "S312 hDHODH antiviral" --limit 20 --output /tmp/antibioticmech-chebi-167669-publications.jsonl` | PubMed returned no candidates for this broad text query; Semantic Scholar returned HTTP 429. |

No separate single-record term, reference, or history validator is documented in
the local `justfile` for this plain ChEBI-seeded record; the review used the
single-record schema checks plus `verify-corpus`, OLS, RCSB, PubMed, and
Europe PMC checks instead.

## Identity and Grounding

`CHEBI:167669` resolves unambiguously through
`data/antibiotics/PATHS.tsv` to the `ANTIVIRAL` record at
`data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml`.
The only matching generated record carries ChEBI source concept
`antibioticmech:chebi-8403b20400`.

The generated structure matches the committed ChEBI row: SMILES,
Standard InChI, InChIKey `DDEIFUOYHWEWSS-DJKKODMXSA-N`, molecular formula
`C17H12ClN3O2S`, charge `0`, average mass, and monoisotopic mass agree with
`data/raw/chebi_antimicrobials.tsv`.

The live OLS term is 3-star and non-obsolete, and it repeats the same label,
definition, structure fields, `S312` synonym, `pdb-ccd:3X2` cross-reference,
and `PMID:32754890` literature xref. Its four direct structural parents are
exactly the record's `parent_compounds`: `CHEBI:22723` benzoic acids,
`CHEBI:38418` 1,3-thiazoles, `CHEBI:38532` hydrazone, and `CHEBI:83403`
monochlorobenzenes.

The live ChEBI `has_role` set includes `CHEBI:149553` anticoronaviral agent and
`CHEBI:22587` antiviral agent, which are the record's two retained
antimicrobial roles. ChEBI also reports non-filing roles for human DHODH
inhibition, antineoplastic activity, and apoptosis induction; those are not
copied into `activity_roles`, which is correct because the committed ChEBI
antimicrobial inventory preserves the antimicrobial roles rather than every
ChEBI pharmacology role.

The `pdb-ccd:3X2` xref denotes the same structure. RCSB Chemical Component
`3X2` reports the same Standard InChI, the same
`DDEIFUOYHWEWSS-DJKKODMXSA-N` InChIKey, the same zero formal charge, and the
same systematic name.

## Evidence

The generated identity, label, definition, synonyms, exact structure,
parent compounds, activity roles, xrefs, filing class, source concept, and
grounding status reproduce from `data/raw/chebi_antimicrobials.tsv`; there is
no `verify-corpus` drift.

The ChEBI source PMID resolves to Xiong et al. 2020, "Novel and potent
inhibitors targeting DHODH are broad-spectrum antivirals against RNA viruses
including newly-emerged coronavirus SARS-CoV-2." Europe PMC exposes the open
full text under `PMC7402641` and reports the same PMID, DOI, journal, authors,
and title returned by PubMed.

The inspected abstract and full text support the broad shape of the ChEBI
definition: S312 is a human DHODH inhibitor, the paper evaluates DHODH as a
host antiviral target, and S312 is tested against influenza A subtypes,
SARS-CoV-2, Zika virus, and Ebola-virus systems. The full text also reports
S312 DHODH binding and influenza cell-assay values suitable for future
claim-level `MolecularTarget`, `ActivityObservation`, and causal-graph
curation.

Two later errata are linked from the primary full text. `PMID:33029721`
replaces Figure 1 but keeps the Figure 1 caption about S312/S416 DHODH binding
and influenza activity. `PMID:33165830` corrects only Dimitri Lavillette's
author-name spelling. Neither correction appears to invalidate the S312
identity, host DHODH target, or broad RNA-virus activity claim.

`conf/sources.yaml` intentionally does not map `CHEBI:77103` to the seeded
`mode_of_action`: the local comment says ChEBI's DHODH role denotes precursor
supply rather than a mode currently represented by the enum, and most DHODH
records in this corpus are host-directed. The absent mechanism on this record is
therefore a real schema/curation gap, not an overlooked ChEBI role.

## Completeness

The record is structurally grounded, exactly cross-referenced to PDB CCD, and
filed under `ANTIVIRAL`, but it is still a seed stub for S312's antiviral
biology. It has no curator-owned evidence for the host DHODH target, no activity
observations for the viral assays in Xiong et al. 2020, no mode-of-action field
that can express host pyrimidine-depletion as an antiviral mechanism, and no
causal graph from host DHODH inhibition to depleted pyrimidine synthesis to
reduced RNA-virus replication.

`just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-167669-worklist.tsv`
places `CHEBI:167669` on `mechanism`, `activity-candidate`, and
`review-readiness`. It is absent from `producer-candidate`, `target-evidence`,
`moa-scope`, `xref-unverified`, `xref-span-conflict`, and `multi-component`;
those absences are appropriate for this exact single-compound ChEBI seed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact S312 record has source literature for a host-directed antiviral mechanism, but no curated mechanism, host target, activity observations, or causal graph. | `CHEBI:167669` has no `record_evidence`, `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, or `causal_graphs`; `just review-queue --limit 95` reports `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`; `PMID:32754890` supports S312 as a human-DHODH-targeting broad-spectrum RNA-virus inhibitor. | Future curator-owned fields in `data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml`, written through `write_validated_antibiotic`. If the current `ModeOfActionEnum` cannot represent host DHODH or pyrimidine-depletion cleanly, the schema and `conf/sources.yaml` need a new reviewed mechanism value before the record can become `REVIEWED`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Decide how host-directed human-DHODH blockade should be represented for
   antiviral records: add a specific `ModeOfActionEnum` value and ChEBI role
   mapping for pyrimidine-biosynthesis depletion, or document a curator-owned
   workaround for this record if the schema intentionally stays coarse.
2. Inspect Xiong et al. 2020, its Figure 1 correction, and its supplementary
   tables for the exact S312 human-DHODH binding, cell-culture EC50, and mouse
   influenza assertions worth curating.
3. Add evidence-backed `MolecularTarget` and `ActivityObservation` objects for
   claims supported directly by Xiong et al. 2020, keeping host human DHODH
   separate from virus taxon and cell-line assay context.
4. Add a causal graph for the host-directed mechanism only for edges directly
   supported by the primary paper: S312 inhibits host DHODH, host pyrimidine
   de novo synthesis is depleted, and RNA-virus replication falls in infected
   cells or animals.
5. Keep `curation_status: SEEDED` until identity, structure, class, exact
   activity roles, a representable mode of action, and any known molecular
   targets carry primary support.

## Follow-up Checks

After future S312 curation:

- `just validate-strict data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml --out /tmp/antibioticmech-chebi-167669-strict.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-167669-worklist.tsv`
- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
- `just qc`
- Manual review of `git diff -- data/antibiotics/antiviral/e-2-4-2-chlorophenyl-1-3-thiazol-2-yl-hydrazinylidene-methyl-benzoic-a.yaml conf/sources.yaml src scripts tests`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`, `curation`,
  `conf`, and `reports/yaml_record_review` for `CHEBI:167669`,
  `DDEIFUOYHWEWSS-DJKKODMXSA-N`, `antibioticmech:chebi-8403b20400`, `S312`,
  and `pdb-ccd:3X2`.
- `rg --no-ignore --hidden` over `reports/yaml_record_review`,
  `data/antibiotics`, `data/raw`, and `curation` for `CHEBI:167669` and
  chlorophenyl/thiazole label fragments.
- `find reports/yaml_record_review -maxdepth 1 -iname '*thiazol*' -print`.

Those searches found the expected generated record, ChEBI raw row,
`PATHS.tsv` row, `curation/record_review_queue.tsv` row, and no prior review
report for `CHEBI:167669`.

The direct PubMed `efetch` attempt for `PMID:32754890` failed with sandbox DNS
resolution; the local publication helper and Europe PMC resolved the same PMID
and DOI successfully.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.

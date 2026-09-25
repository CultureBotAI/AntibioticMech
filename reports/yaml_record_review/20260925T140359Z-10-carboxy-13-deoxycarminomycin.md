# YAML Record Review: 10-carboxy-13-deoxycarminomycin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml`
- Started UTC: 2026-09-25T14:01:00Z
- Finished UTC: 2026-09-25T14:03:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:31047` |
| Label | `10-carboxy-13-deoxycarminomycin` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained path | `data/raw/chebi_antimicrobials.tsv` plus the ChEBI extractor for seeded identity, synonyms, structure, parents, role terms, and xrefs |
| Generated record | `data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml`, locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is the generated ChEBI seed for `CHEBI:31047`. It contains one ChEBI source concept with `role_terms: [CHEBI:33281]`, a ChEBI definition, four ChEBI synonyms, six ChEBI parents, a ChEBI-sourced structure, and three database xrefs: `cas:97583-07-8`, `kegg.compound:C12427`, and `metacyc.compound:CPD-15739`.

The record has no record-level `evidence`, `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graph`, `datasets`, `clinical_status`, or `discussions`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml` | Passed. |
| `just validate-strict data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml --out /tmp/antibioticmech-chebi-31047-strict.tsv` | Passed; 1 file, 0 errors. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed. The exact `CHEBI:31047` rows were the `mechanism` queue row, with 0 CARD targets and 0 resistance edges to build on, and the `review-readiness` row with 5 source literature leads. No activity, producer, target, or resistance candidate row exists for the exact identifier. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-31047-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. `CHEBI:31047` remains queued as `MECHANISM_REVIEW: mechanism is absent; 5 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 label lookup | Passed; `CHEBI:31047`, all six parent CURIEs, and `CHEBI:33281` resolve with the labels expected from the seed. |
| Live OLS4 `CHEBI:31047` term and parent lookups | Passed; the term is current and non-obsolete, and its direct parents are `CHEBI:25830`, `CHEBI:35315`, `CHEBI:35868`, `CHEBI:47779`, `CHEBI:49322`, and `CHEBI:63367`. |
| PubChem InChIKey lookup for `MMYTYGXIKKVLES-AGMCFEMXSA-N` | Passed; the lookup returned two same-Standard-InChI PubChem CIDs, 126779 and 72715812, matching the record formula and InChIKey. |
| PubMed EFetch for `PMID:1880908`, `PMID:3700249`, `PMID:7490224`, `PMID:8436560`, and `PMID:9098063` | Passed; all five ChEBI PMID xrefs resolve. |
| PubMed exact-name search for the label and `D788-1` synonyms | Passed; returned the same five PMIDs as ChEBI. |
| Semantic Scholar exact-label check | Not checked: the public API returned HTTP 429. |

## Identity and Grounding

- `CHEBI:31047` is the correct grounding for the exact D788-1 structure named by the record. Live OLS4 reports the term as current and non-obsolete, and the ChEBI term, committed raw ChEBI row, generated YAML, and PubChem InChIKey lookup agree on Standard InChIKey `MMYTYGXIKKVLES-AGMCFEMXSA-N` and formula `C27H29NO11`.
- The six `parent_compounds` are current direct ChEBI parents: `p-quinones`, `deoxy hexoside`, `hydroxy monocarboxylic acid`, `aminoglycoside`, `anthracycline antibiotic`, and `monosaccharide derivative`. All are broader chemical classes rather than exact xrefs.
- `activity_roles: [CHEBI:33281]` preserves ChEBI's `antimicrobial agent` role and explains why the record is in scope while filed under `ANTIMICROBIAL_UNSPECIFIED`.
- The PubChem InChIKey lookup resolves both a neutral CID and a zwitterionic CID because Standard InChI collapses those protonation representations. AntibioticMech does not assert either CID as an exact xref, so this is not a record-level conflict.
- The local ignored-inclusive exact search covered `data/raw`, `curation`, `data/antibiotics`, `reports/yaml_record_review`, and `.git` refs/logs. It found the target YAML, the raw ChEBI row, the lockfile row, the review-queue row, and one prior near-miss report that mentioned this adjacent anthracycline, but no prior exact `CHEBI:31047` report and no stale local or remote branch ref.

## Evidence

The record currently inherits the ChEBI database assertion but has no primary-paper activity, mechanism, target, resistance, producer, or causal-graph evidence.

| ChEBI PMID lead | Supports the antimicrobial record? | Review |
|---|---|---|
| `PMID:3700249` | Identity lead only from PubMed metadata. | Resolves to the 1986 report of D788-1, named as 10-carboxy-13-deoxocarminomycin, in daunorubicin beer. No PubMed abstract was available to inspect for antimicrobial activity or mechanism. |
| `PMID:1880908` | Identity/derivatization lead only from PubMed metadata. | Resolves to photochemical production of the anthracycline antibiotic oxaunomycin from precursor metabolite D788-1. No PubMed abstract was available to inspect for exact activity of D788-1 itself. |
| `PMID:8436560` | Producer and identity lead. | The abstract reports that a daunorubicin-blocked mutant strain RPM-5, derived from baumycin-producing Streptomyces sp. D788, accumulated D788-1 as a major precursor metabolite and that the paper describes isolation, purification, identification, and L1210 antitumor activities of anthracycline metabolites. |
| `PMID:7490224` | Derivatization lead only. | The abstract reports photochemical production of 10-epi-oxaunomycin and 10-epi-11-deoxyoxaunomycin from D788-1 and D788-3, followed by growth-inhibitory assays on cultured L1210 leukemic cells. L1210 is a mouse tumor-cell line, not a microbial assay organism. |
| `PMID:9098063` | Biosynthetic producer lead. | The abstract reports that Streptomyces sp. strain C5 DauP removes the carbomethoxy group of rhodomycin D to form 10-carboxy-13-deoxycarminomycin, and that DauK methylates 10-carboxy-13-deoxycarminomycin. It supports biosynthetic context, not antimicrobial activity. |

PubMed exact-name search found the same five PMIDs already attached to ChEBI. Europe PMC exact-name search was broader and surfaced those PMIDs plus unrelated lexical matches; no additional exact antimicrobial assay lead was found in the first page. Semantic Scholar could not be checked because its public API returned HTTP 429.

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope, target, or causal edge, and none of the inspected PMID abstracts reports an antimicrobial mechanism for D788-1.
- **Activity:** incomplete. ChEBI classifies the exact structure as an antimicrobial agent, but the inspected abstracts support anthracycline identity, L1210 antitumor assays, photochemical conversion to derivatives, or biosynthetic production rather than a microbial assay.
- **Producer:** likely incomplete. `PMID:8436560` and `PMID:9098063` are exact producer/bioconversion leads for Streptomyces strains that a curator should inspect in full text before adding `ProducerOrganism` objects.
- **Resistance:** empty and not currently a consequential gap. CARD has 0 targets and 0 resistance edges to build on for this ChEBI-only record.
- **Clinical status and datasets:** empty; the inspected ChEBI, PubMed, PubChem, and OLS leads did not surface an exact clinical product or dataset accession for D788-1.
- **Discussions:** empty. The absent antimicrobial assay and absent mechanism are consequential enough to justify a `CURATION_TODO` if a future curation pass cannot resolve them.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| F1 | Major | The seeded exact structure has no curated exact antimicrobial activity or mechanism evidence. | The record is `SEEDED` from ChEBI with role `CHEBI:33281`, but has no `evidence`, `activity_spectrum`, `mode_of_action`, `molecular_targets`, or `discussions`. PubMed exact-name search returned only ChEBI's five PMID xrefs; the three inspected abstracts among them discuss L1210 antitumor assays, anthracycline biosynthesis, and photochemical derivatization rather than microbial activity, and two older leads had no PubMed abstracts. | Curator-owned additions on `data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml`, written through `write_validated_antibiotic` with an explicit `CurationEvent`; if the exact structure should be out of scope, its ChEBI source concept would instead need a curated exclusion in `curation/decisions.tsv`. |
| F2 | Minor | Exact producer leads are present but not curated. | `PMID:8436560` reports D788-1 accumulation by Streptomyces sp. D788-derived mutant RPM-5, and `PMID:9098063` reports Streptomyces sp. strain C5 DauP conversion of rhodomycin D to 10-carboxy-13-deoxycarminomycin. The YAML has no `producer_organisms`. | Curator-owned additions on `data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml`, after the full papers establish producer taxon and strain context. |

No blocker findings were found.

## Recommended Edits

1. Inspect the full text of `PMID:3700249`, `PMID:8436560`, `PMID:9098063`, and their citation trails for an exact microbial activity assay for D788-1. If no exact assay exists, add a `CURATION_TODO` or curated mechanism veto documenting that the ChEBI role was retained but no primary antimicrobial activity/mechanism support was found in the source PMIDs.
2. Do not promote the L1210 leukemic-cell growth data from `PMID:7490224` or `PMID:8436560` into `activity_spectrum`: antitumor cell-line inhibition is not an antimicrobial observation.
3. If the full producer papers preserve exact D788-1 biosynthesis, add narrowly scoped `ProducerOrganism` objects for Streptomyces sp. D788/RPM-5 and Streptomyces sp. C5 with strain text, source-specific notes, and claim-level evidence.
4. Leave the seeded ChEBI identifier, structure, parentage, role, and xrefs untouched unless the upstream ChEBI extractor changes them; the live ChEBI and committed raw ChEBI identity fields agree.

## Follow-up Checks

- Rerun `just validate-strict data/antibiotics/unspecified/10-carboxy-13-deoxycarminomycin.yaml --out /tmp/antibioticmech-chebi-31047-strict.tsv` after any curator-owned edit.
- Rerun `just verify-corpus --summary` to confirm new curator-owned fields are accepted as maintained curation rather than generated-record drift.
- Rerun `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` and confirm `CHEBI:31047` either leaves the `mechanism` queue or has an intentional unresolved mechanism discussion.
- Manually reread the YAML after writing producer or activity evidence to verify each `PMID` is attached to the narrow organism, strain, activity, or biosynthetic claim it supports.

## Additional Notes

- `10-carboxy-13-deoxycarminomycin` and `10-carboxy-13-deoxocarminomycin` are treated as synonyms for D788-1 in the inspected PubMed metadata. The ChEBI label and raw row consistently use `deoxy`.
- The existing `20260921T184008Z-13r-13-dihydrocarminomycin.md` report mentioned this compound only as an adjacent anthracycline record; it is not an exact review of `CHEBI:31047`.

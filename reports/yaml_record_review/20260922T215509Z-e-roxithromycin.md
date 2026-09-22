# YAML Record Review: (E)-roxithromycin

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/e-roxithromycin.yaml`
- Started UTC: 2026-09-22T21:32:00Z
- Finished UTC: 2026-09-22T21:55:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:48935` |
| Label | `(E)-roxithromycin` |
| Path | `data/antibiotics/antibacterial/e-roxithromycin.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:48935`, version `2026-08-30`, minted key `antibioticmech:chebi-07b67804b7` |
| Source roles | `CHEBI:33281` antimicrobial agent; `CHEBI:36047` antibacterial drug |
| Parent compounds | `CHEBI:48844` |
| Structure | `RXZBMPWDPOLZGW-XMRMVWPWSA-N`; formula `C41H76N2O15`; charge `0` |
| Xrefs | `beilstein:5900029`, `cas:80214-83-1`, `hmdb:HMDB0014916`, `pdb-ccd:ROX`, `reaxys:5900029` |
| Drug xrefs | `drugcentral:2410` |
| Source literature leads | `PMID:12575424`, `PMID:24462419` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded exact geometrical isomer of the
macrolide roxithromycin. The YAML has exact ChEBI grounding, a ChEBI
definition, seven ChEBI synonyms, the broader ChEBI roxithromycin parent,
six same-structure or drug xrefs, two antibacterial role terms, chemical
structure fields, and source-concept metadata. It has no generated or
curator-owned activity observation, molecular target, resistance mechanism,
mode of action, producer, discussion, dataset, causal graph, or claim-level
evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/e-roxithromycin.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/e-roxithromycin.yaml --out /tmp/antibioticmech-chebi-48935-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-48935-worklist.tsv` | Pass: the full worklist TSV was written. Exact `CHEBI:48935` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 95` | Pass: `CHEBI:48935` is the first queued record after the records that already have `reports/yaml_record_review` reports; its row says `MECHANISM_REVIEW: mechanism is absent; 2 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `uv run runoak -i ols:chebi labels CHEBI:48935 CHEBI:48844 CHEBI:33281 CHEBI:36047` | Pass: OLS resolved `CHEBI:48935` as `(E)-roxithromycin`, `CHEBI:48844` as `roxithromycin`, `CHEBI:33281` as `antimicrobial agent`, and `CHEBI:36047` as `antibacterial drug`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`data/raw/chebi_antimicrobials.tsv` seeds `CHEBI:48935` as a 3-star ChEBI entry
in antimicrobial role scope and gives the same label, exact definition, SMILES,
Standard InChI, Standard InChIKey, formula, charge, masses, ChEBI parent,
synonyms, xrefs, and source PMIDs that appear in or explain the generated YAML.
OAK through OLS resolves the identifier as `(E)-roxithromycin`, the generated
parent as the broader `roxithromycin`, and both generated roles as broad
antimicrobial/antibacterial roles.

The `ANTIBACTERIAL` filing class is consistent with the generated
`CHEBI:36047` `antibacterial drug` role. Because the source row has no
more-specific mechanism role and no ARO source concept, the exact-isomer YAML
correctly has no `mode_of_action`, `mode_of_action_target_scope`, molecular
target, resistance edge, activity observation, or causal graph.

The same-structure xrefs are correctly retained as xrefs. ChEBI attaches the
CAS accession `80214-83-1`, HMDB accession `HMDB0014916`, PDB Chemical
Component Dictionary accession `ROX`, Reaxys accession `5900029`, Beilstein
accession `5900029`, and DrugCentral accession `2410` to the exact
`CHEBI:48935` term, and the worklist does not flag this record on
`xref-unverified`, `xref-name-conflict`, or `xref-span-conflict`.

There are adjacent generated records for both `CHEBI:48844` `roxithromycin` and
`CHEBI:32109` `(Z)-roxithromycin`. `CHEBI:48844` is the broader ARO plus ChEBI
parent record that carries CARD-derived resistance mechanisms and a CARD
50S-ribosomal-subunit P-site target assertion. Those broad generated edges
were not silently projected onto exact `CHEBI:48935`, and future curation
should only move them to the exact isomer after primary-paper inspection proves
that the source material and assay target were exact `(E)-roxithromycin`.

Before this review branch was created, ignored-inclusive searches found no
prior dedicated `CHEBI:48935` or `e-roxithromycin` review report and no
curation decision, curator-inventory row, generated activity observation,
molecular target, resistance edge, producer, dataset, or causal-graph claim
resolving this exact record. Exact branch lookups found no local branch,
remote-tracking branch, or remote `review-chebi-48935-e-roxithromycin` branch.

## Evidence

The record's antibacterial class comes from the broad ChEBI `CHEBI:36047`
`antibacterial drug` role. That role is sufficient for the generator to file
the record under `ANTIBACTERIAL`, but it is not assertion-level primary
evidence for a bacterial organism, MIC value, ribosomal target, mode of action,
or resistance mechanism.

The repository publication helper resolved both ChEBI-seeded PubMed leads.
`PMID:12575424` is a Japanese Journal of Antibiotics title-level lead on
roxithromycin inhibition of Th2 cytokine production, and PubMed exposes no
abstract through the helper. `PMID:24462419` is a randomized clinical pilot
trial comparing roxithromycin, ciprofloxacin, and aceclofenac for chronic
prostatitis/chronic pelvic pain syndrome. Neither helper result supports an
exact `(E)-roxithromycin` bacterial activity row, MIC endpoint, molecular
target, or resistance edge at the inspected title/abstract level.

A focused exact-name, CAS, and `CHEBI:48935` search mostly returned clinical,
analytical-chemistry, environmental-fate, and ecotoxicology roxithromycin
papers rather than exact-isomer antibacterial mechanism papers. A broader
roxithromycin ribosome search found candidate mechanism papers that curators
should inspect in full: `PMID:11677599` reports high-resolution structures of
the `Deinococcus radiodurans` 50S ribosomal subunit complexed with
roxithromycin and other antibiotics, and `PMID:19469526` models roxithromycin
binding to the bacterial 50S large ribosomal subunit. `PMID:37284499` is a
candidate exact susceptibility/resistance lead because it selected
`Mycoplasma pneumoniae` mutants against increasing roxithromycin
concentrations and sequenced macrolide-resistance mutations. The abstract-level
checks do not prove whether each paper's roxithromycin reagent maps to exact
`CHEBI:48935`, the broader `CHEBI:48844`, or a mixture of geometrical isomers.

Semantic Scholar returned HTTP 429 for the repository publication-helper
searches; PubMed returned results for each query.

## Completeness

The record is incomplete as a reviewed antibacterial record. It has exact ChEBI
identity, structure, same-structure database xrefs, one broader ChEBI parent,
two ChEBI activity roles, and two source-level PubMed leads, but no claim-level
evidence, no `activity_spectrum`, no molecular target, no resistance
mechanism, no mode of action, no dataset, and no causal graph.

The empty target, resistance, mode-of-action, and causal-graph slots are
correct for the current exact-isomer seed. The adjacent broad roxithromycin ARO
record contains CARD database assertions for Erm, Mph, Ere, and LmrP
resistance families and a CARD database assertion for 50S P-site targeting, but
those assertions require primary evidence before they can support exact
`CHEBI:48935`.

The empty `activity_spectrum` slot should be treated as missing curation, not
as negative antibacterial activity. Full-paper extraction should capture exact
endpoint type, value, unit, qualifier, assay method, organism, strain, and
source-compound isomer context before normalizing any roxithromycin MIC or
resistance-selection observation to the exact `(E)-roxithromycin` record.

The empty `producers`, `clinical_status_assertions`, `datasets`, and
`discussions` slots are acceptable for the generated record. No microbial
biosynthetic producer row, clinical assertion, public dataset accession, or
discussion-worthy conflict with exact `CHEBI:48935` claim-level evidence was
identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:48935` has source-level ChEBI antibacterial classification, but no curator-owned primary evidence for exact bacterial activity, no activity observation, no molecular target, no mode of action, no resistance edge, and no causal graph. | The generated record has 2 source literature leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no resistance mechanisms, no mode-of-action fields, and no causal graph. The worklist flags exact `CHEBI:48935` for `mechanism` and `review-readiness` only. `PMID:11677599`, `PMID:19469526`, and `PMID:37284499` are direct roxithromycin mechanism or susceptibility leads, but none of those claims are represented in the exact-isomer YAML and each still needs full-paper exact-compound review. | Future curator-owned fields on `data/antibiotics/antibacterial/e-roxithromycin.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect `PMID:11677599` and `PMID:19469526` in full to determine whether
   their roxithromycin ligand maps to exact `(E)-roxithromycin`,
   broad `roxithromycin`, or a mixed/ambiguous reagent before curating a 50S
   ribosomal-subunit target, `PROTEIN_SYNTHESIS_INHIBITION` mode of action, or
   causal graph.
2. Inspect `PMID:37284499` and adjacent roxithromycin susceptibility papers in
   full and add exact `activity_spectrum` rows only for observations whose
   source compound can be mapped to `CHEBI:48935`. Preserve endpoint type,
   value, unit, qualifier, assay, organism, strain, and resistance-selection
   context from each source.
3. Resolve whether any CARD/ARO parent-record resistance edge for broad
   `roxithromycin` can be assigned to exact `(E)-roxithromycin` from a primary
   paper. Keep the broad parent `CHEBI:48844` as the owner for database-only
   or isomer-ambiguous assertions.
4. Do not cite the CP/CPPS clinical trial, Th2 cytokine title, environmental
   occurrence, degradation, detection, bioaccumulation, or ecotoxicology papers
   as evidence for antibacterial activity unless their full text contains an
   isolated-microbe assay with roxithromycin concentration-response data.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antibacterial/e-roxithromycin.yaml`
2. `just validate-strict data/antibiotics/antibacterial/e-roxithromycin.yaml --out /tmp/antibioticmech-chebi-48935-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-48935-worklist.tsv`
5. `just review-queue --limit 95`
6. `just qc`

Manually compare future exact-isomer activity, mechanism, resistance, target,
and causal-graph curation against the ChEBI seed row, the broader
`roxithromycin` record, the PDB `ROX` ligand identity, the 50S-structure and
MM-PBSA mechanism papers, and the `Mycoplasma pneumoniae` in vitro
resistance-selection paper to confirm that every curated claim is attached to
the correct exact `(E)-roxithromycin` or broader `roxithromycin` term.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, `find`, or
Git/GitHub ref listing, so they included ignored `reports/` files or otherwise
did not depend on Git's ignore filters.

# YAML Record Review: (−)-marinopyrrole B

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/marinopyrrole-b.yaml`
- Started UTC: 2026-09-24T17:24:44Z
- Finished UTC: 2026-09-24T17:26:41Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `CHEBI:66679` |
| Label | `(−)-marinopyrrole B` |
| Path | `data/antibiotics/antibacterial/marinopyrrole-b.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concepts | `CHEBI:66679` from ChEBI 2026-08-30 |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`, `data/raw/mibig_producers.tsv`, and `data/antibiotics/PATHS.tsv`; source-owned identity, structure, class, role, parent, xref, and imported MIBiG producer changes must go through the ChEBI/MIBiG extractors, raw inventories, `curation/decisions.tsv`, or the seeder rather than a hand edit to this YAML. |

The record resolves unambiguously. `data/antibiotics/PATHS.tsv` maps
`CHEBI:66679` to `ANTIBACTERIAL/marinopyrrole-b`, and an ignored-inclusive
search for `CHEBI:66679`, `XAANSONIBUCODQ`, `marinopyrrole-b`, and the broader
`marinopyrrole` label family across `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `.git`, and the full `/tmp` review/worklist TSVs
found the expected raw ChEBI row, raw MIBiG row, path row, `mechanism` and
`review-readiness` queue rows, target YAML, the related `marinopyrrole-a`
sibling, and the already-merged marinopyrrole A review, with no prior exact
`marinopyrrole-b` report.

## Validation

| Check | Result |
| --- | --- |
| `rg --no-ignore --hidden -n 'CHEBI:66679\|XAANSONIBUCODQ\|marinopyrrole-b' ...` plus a broader `marinopyrrole` search | Pass: resolved the expected raw/source rows, queue rows, target record, sibling `marinopyrrole-a` mentions, and prior marinopyrrole A report; no prior exact `CHEBI:66679` or `marinopyrrole-b` report was found. Hidden and ignored files were included. |
| `just validate data/antibiotics/antibacterial/marinopyrrole-b.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/marinopyrrole-b.yaml --out /tmp/marinopyrrole-b-validate-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Pass: 2,939 records expected and present; 0 missing, unexpected, or drifted records; 0 `PATHS.tsv` discrepancies. The only diagnostic was the known unrelated `iclaprim`/`CHEBI:31724` CARD cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Pass: wrote the full TSV. `CHEBI:66679` appears on `mechanism` and `review-readiness` only. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Pass: regenerated the full `review-readiness` queue and listed `CHEBI:66679` as `MECHANISM_REVIEW: mechanism is absent; 2 source literature leads, 0 record evidence items, 0 targets`; this queue counter checks top-level record `evidence` and does not include nested MIBiG producer evidence. |
| ChEBI OLS4 lookups for `CHEBI:66679` | Pass: the official term, direct parents, and direct `has role` relations resolve and agree with the generated identity, structure, parent, Reaxys xref, and antimicrobial role fields. |
| NCBI EFetch for ChEBI PMIDs plus `PMID:22800473` | Pass: resolved all three inspected PubMed identifiers and their DOIs. |
| MIBiG `BGC0001159.5/annotations.json` | Pass: resolved the official active MIBiG `BGC0001159` version 5 payload that backs the imported producer row. |
| NCBI Taxonomy EFetch for `NCBITaxon:467194` | Pass: resolved taxon `467194` as species-rank `Streptomyces sp. CNQ-418` in the Bacteria division. |

No narrower single-record term, reference, or history validator is exposed for
plain generated ChEBI/MIBiG records. The full-corpus `worklist` and
`verify-corpus` checks above are the documented repository checks for those
concerns.

## Identity and Grounding

The YAML denotes one exact, ChEBI-grounded structure: neutral
`(−)-marinopyrrole B`, the 3-bromo tetrachloro bipyrrole natural product with
Standard InChIKey `XAANSONIBUCODQ-UHFFFAOYSA-N`.

| Claim | Review |
| --- | --- |
| ChEBI identity | The official OLS4 exact lookup for `CHEBI:66679` returned one ChEBI class labelled `(-)-marinopyrrole B`, matching the YAML label apart from minus-glyph normalization. |
| Structure | OLS4, `data/raw/chebi_antimicrobials.tsv`, and the YAML agree on SMILES `O=C(c1ccccc1O)c1nc(Cl)c(Cl)c1-n1c(Cl)c(Cl)c(Br)c1C(=O)c1ccccc1O`, Standard InChI `InChI=1S/C22H11BrCl4N2O4/c23-13-14(24)22(27)29(17(13)20(33)10-6-2-4-8-12(10)31)18-15(25)21(26)28-16(18)19(32)9-5-1-3-7-11(9)30/h1-8,28,30-31H`, Standard InChIKey `XAANSONIBUCODQ-UHFFFAOYSA-N`, formula `C22H11BrCl4N2O4`, neutral charge, average mass `589.056`, and monoisotopic mass `585.86563`. |
| Synonym | OLS4 and the raw ChEBI row report the same exact IUPAC synonym retained in the record: `(3-bromo-4,4',5,5'-tetrachloro-1'H-1,3'-bipyrrole-2,2'-diyl)bis[(2-hydroxyphenyl)methanone]`. |
| ChEBI parents | The OLS4 parent lookup returns exactly the five broader classes in `parent_compounds`: `CHEBI:26455` pyrroles, `CHEBI:33853` phenols, `CHEBI:36683` organochlorine compound, `CHEBI:37141` organobromine compound, and `CHEBI:76224` aromatic ketone. |
| Activity role and filing class | OLS4 returns `CHEBI:33281` antimicrobial agent and `CHEBI:33282` antibacterial agent as direct `has role` targets for `CHEBI:66679`; filing the record as `ANTIBACTERIAL` follows the retained ChEBI antibacterial role. OLS4 also reports the non-antimicrobial `CHEBI:76507` marine metabolite and `CHEBI:76969` bacterial metabolite roles, which the generated `activity_roles` field correctly omits. |
| Xrefs | OLS4 and `data/raw/chebi_antimicrobials.tsv` both list the exact-equivalence `reaxys:11303257` xref retained in the YAML. The remaining database cross-references on the OLS term are PubMed literature identifiers and correctly do not appear in the structure-identity `xrefs` field. |
| MIBiG producer import | The official MIBiG `BGC0001159` entry is active, version 5, and quality `questionable`; it lists `marinopyrrole B` with formula `C22H11BrCl4N2O4`, names the producer as `Streptomyces sp. CNQ-418`, and assigns NCBI taxon `467194`. NCBI Taxonomy resolves `467194` as a bacterial species-rank `Streptomyces sp. CNQ-418`, matching the YAML's `taxon_label: Streptomyces sp.` plus `strain: CNQ-418` split. |

No wrong identity, grounding, xref, parent, class, or producer-link conflict was
found.

## Evidence

The record has one object-level assertion with evidence: its MIBiG-imported
`ProducerOrganism`.

| Claim | Review |
| --- | --- |
| `PMID:22800473` producer evidence | NCBI resolves `PMID:22800473` to the 2012 Journal of the American Chemical Society paper `Flavoenzyme-catalyzed atropo-selective N,C-bipyrrole homocoupling in marinopyrrole biosynthesis`, DOI `10.1021/ja305670f`. Its PubMed abstract reports discovery and heterologous expression of marinopyrrole biosynthesis genes in `Streptomyces sp. CNQ-418`, consistent with a BGC-level producer source for MIBiG. |
| Inherited producer scope | MIBiG `BGC0001159` lists five compounds, all with empty compound-level `evidence` arrays and empty antibacterial bioactivity `references`; the locus, not `marinopyrrole B` alone, carries `Knock-out studies` and `Heterologous expression` evidence. The YAML is therefore correct to mark `link_evidence_scope: CLUSTER_INHERITED` and to describe `PMID:22800473` as MIBiG's first legacy reference for the entry rather than specific producer/compound proof. |

The ChEBI seed contributes two PubMed literature leads:

| PMID | DOI | Review |
| --- | --- | --- |
| `PMID:18205372` | `10.1021/ol702952n` | Original marine `Streptomyces` discovery/isolation paper for marinopyrroles A and B. The PubMed abstract says X-ray analysis of marinopyrrole B showed that the natural product has the `M` atropo-enantiomer configuration and says the marinopyrroles have potent anti-MRSA antibiotic activity, but it does not expose a molecular target or exact MIC. |
| `PMID:20405892` | `10.1021/jo1002054` | Structure/reactivity/antibiotic-property paper for marinopyrroles A-F. The PubMed abstract reports actinomycete strain CNQ-418, the unusual 1,3'-bipyrrole core, bromine/chlorine substituents, configurational stability of marinopyrroles A-E at room temperature, the natural products' strict `M` configuration, and marked antibacterial activity against MRSA, but it does not expose a compound-specific mode of action. |

## Completeness

`CHEBI:66679` is structurally grounded and has an honest imported producer
claim, but it remains mechanism-thin. It has no CARD source concept, no CARD
target, no CARD resistance edge, no curator-authored `mode_of_action`, no
molecular target, no activity observation, and no causal graph.

The full worklist places this identifier only on:

- `mechanism`: absent mode of action, with `0 CARD target(s), 0 resistance edge(s) to build on`
- `review-readiness`: `MECHANISM_REVIEW`, with 2 source literature leads, 0 top-level record evidence items, and 0 targets

The same complete worklist has no exact `CHEBI:66679` row for
`target-evidence`, `minted`, `unknown-mech`, `moa-scope`, `aro-class`,
`xref-unverified`, `xref-name-conflict`, `xref-span-conflict`,
`multi-component`, `producer-candidate`, `activity-candidate`,
`unnamed-producer`, or `structure-unreviewed`.

An NCBI PubMed title/abstract search for the exact phrase `"marinopyrrole B"`
found 3 papers on 2026-09-24: the original discovery paper, a first-synthesis
paper for racemic marinopyrrole B, and a wMUS81 docking study. Together with
the 2 ChEBI-seeded PubMed leads above, this exact abstract-visible check found
no source-backed antimicrobial target candidate, but it is not a substitute for
a future full-text mechanism search.

Empty slots for `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `activity_spectrum`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, and `causal_graphs` are preferable to
inferring a target or measured activity from the ChEBI antibacterial role or
from MIBiG's antibacterial bioactivity flag.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The record still needs compound-specific antimicrobial mechanism review before it can become `REVIEWED`. | The YAML has no `mode_of_action`, no molecular targets, no activity observations, and no causal graph. `just worklist` keeps `CHEBI:66679` on `mechanism` and `review-readiness`; the inspected ChEBI PubMed leads establish the natural product identity and anti-MRSA activity but no source-backed antibacterial molecular target for marinopyrrole B is exposed in the PubMed abstracts. | Future curator-owned fields on `data/antibiotics/antibacterial/marinopyrrole-b.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Do not edit the source-owned identity, structure, synonym, class, role,
   parent, xref, or source-concept fields for `CHEBI:66679`: they reproduce
   from the official ChEBI row, `data/raw/chebi_antimicrobials.tsv`, and
   `data/antibiotics/PATHS.tsv`.
2. Leave the MIBiG-imported `producer_organisms` row scoped as
   `CLUSTER_INHERITED` unless an inspected primary source or future MIBiG entry
   links evidence directly to `marinopyrrole B` rather than the five-compound
   `BGC0001159` cluster.
3. Inspect the full text and tables for the anti-MRSA papers, especially
   `PMID:18205372` and `PMID:20405892`, before adding `activity_spectrum`
   rows. Add compound-specific organism and strain observations only when the
   source states assay method plus exact values and units; do not copy a pooled
   activity statement for the marinopyrrole series onto this individual
   structure.
4. Add `mode_of_action`, `molecular_targets`, or `causal_graphs` only after a
   primary source identifies how marinopyrrole B inhibits MRSA or another
   microbial system.
5. Keep `curation_status: SEEDED` until identity, structure, class, and the
   antimicrobial mode of action have all been checked and any target claims have
   primary citations.

## Follow-up Checks

If a future curator changes this record:

- Run `just validate-strict data/antibiotics/antibacterial/marinopyrrole-b.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Run `just verify-corpus` to prove source-owned generated fields still match
  `data/raw/`.
- Run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and
  confirm `CHEBI:66679` leaves `mechanism` and `review-readiness` only after an
  exact mechanism review has actually been curated.
- Re-run `just lint`, `git diff --check`, and `git diff --cached --check`
  before opening a PR.

## Additional Notes

The official ChEBI definition spells the source as `Streptomyces sp.CNQ-418`
without a space after `sp.`. The YAML correctly mirrors that upstream text
rather than normalizing a generated source-owned field.

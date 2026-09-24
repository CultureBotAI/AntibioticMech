# YAML Record Review: (−)-marinopyrrole A

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/marinopyrrole-a.yaml`
- Started UTC: 2026-09-24T16:44:43Z
- Finished UTC: 2026-09-24T16:47:15Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Identifier | `CHEBI:66678` |
| Label | `(−)-marinopyrrole A` |
| Path | `data/antibiotics/antibacterial/marinopyrrole-a.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concepts | `CHEBI:66678` from ChEBI 2026-08-30 |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`, `data/raw/mibig_producers.tsv`, and `data/antibiotics/PATHS.tsv`; source-owned identity, structure, class, role, parent, xref, and imported MIBiG producer changes must go through the ChEBI/MIBiG extractors, raw inventories, `curation/decisions.tsv`, or the seeder rather than a hand edit to this YAML. |

The record resolves unambiguously. `data/antibiotics/PATHS.tsv` maps
`CHEBI:66678` to `ANTIBACTERIAL/marinopyrrole-a`, and an ignored-inclusive
search for `CHEBI:66678`, `QYPJBTMRYKRTFG`, and `marinopyrrole` across
`data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`,
`.git` refs/logs, and the full `/tmp` review/worklist TSVs found the expected
raw ChEBI row, raw MIBiG rows for the five marinopyrroles in `BGC0001159`, the
path row, `mechanism` and `review-readiness` queue rows, the target YAML, the
related `marinopyrrole-b` sibling, and the current branch checkout log, with no
prior `marinopyrrole-a` review report or duplicate `CHEBI:66678` record.

## Validation

| Check | Result |
| --- | --- |
| `rg --no-ignore --hidden -n 'CHEBI:66678\|QYPJBTMRYKRTFG\|marinopyrrole' ...` | Pass: resolved the expected raw/source rows, queue rows, target record, sibling `marinopyrrole-b` mentions, and current checkout log; no prior report or duplicate `CHEBI:66678` record was found. Hidden and ignored files were included. |
| `just validate data/antibiotics/antibacterial/marinopyrrole-a.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/marinopyrrole-a.yaml --out /tmp/marinopyrrole-a-validate-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Pass: 2,939 records expected and present; 0 missing, unexpected, or drifted records; 0 `PATHS.tsv` discrepancies. The only diagnostic was the known unrelated `iclaprim`/`CHEBI:31724` CARD cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Pass: wrote the full TSV. `CHEBI:66678` appears on `mechanism` and `review-readiness` only. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Pass: regenerated the full `review-readiness` queue and listed `CHEBI:66678` as `MECHANISM_REVIEW: mechanism is absent; 6 source literature leads, 0 record evidence items, 0 targets`. |
| ChEBI OLS4 lookups for `CHEBI:66678` | Pass: the official term, direct parents, and direct `has role` relations resolve and agree with the generated identity, structure, parent, Reaxys xref, and antimicrobial role fields. |
| NCBI EFetch for ChEBI PMIDs plus `PMID:22800473` | Pass: resolved all seven inspected PubMed identifiers and their DOIs. |
| MIBiG `BGC0001159.5/annotations.json` | Pass: resolved the official active MIBiG `BGC0001159` version 5 payload that backs the imported producer row. |
| NCBI Taxonomy EFetch for `NCBITaxon:467194` | Pass: resolved taxon `467194` as species-rank `Streptomyces sp. CNQ-418` in the Bacteria division. |

No narrower single-record term, reference, or history validator is exposed for
plain generated ChEBI/MIBiG records. The full-corpus `worklist` and
`verify-corpus` checks above are the documented repository checks for those
concerns.

## Identity and Grounding

The YAML denotes one exact, ChEBI-grounded structure: neutral
`(−)-marinopyrrole A`, the tetrachloro bipyrrole natural product with Standard
InChIKey `QYPJBTMRYKRTFG-UHFFFAOYSA-N`.

| Claim | Review |
| --- | --- |
| ChEBI identity | The official OLS4 exact lookup for `CHEBI:66678` returned one ChEBI class labelled `(-)-marinopyrrole A`, matching the YAML label apart from minus-glyph normalization. |
| Structure | OLS4, `data/raw/chebi_antimicrobials.tsv`, and the YAML agree on SMILES `O=C(c1ccccc1O)c1nc(Cl)c(Cl)c1-n1c(C(=O)c2ccccc2O)cc(Cl)c1Cl`, Standard InChI `InChI=1S/C22H12Cl4N2O4/c23-12-9-13(19(31)10-5-1-3-7-14(10)29)28(22(12)26)18-16(24)21(25)27-17(18)20(32)11-6-2-4-8-15(11)30/h1-9,27,29-30H`, Standard InChIKey `QYPJBTMRYKRTFG-UHFFFAOYSA-N`, formula `C22H12Cl4N2O4`, neutral charge, average mass `510.16`, and monoisotopic mass `507.95512`. |
| Synonym | OLS4 and the raw ChEBI row report the same exact IUPAC synonym retained in the record: `(4,4',5,5'-tetrachloro-1'H-1,3'-bipyrrole-2,2'-diyl)bis[(2-hydroxyphenyl)methanone]`. |
| ChEBI parents | The OLS4 parent lookup returns exactly the four broader classes in `parent_compounds`: `CHEBI:26455` pyrroles, `CHEBI:33853` phenols, `CHEBI:36683` organochlorine compound, and `CHEBI:76224` aromatic ketone. |
| Activity role and filing class | OLS4 returns `CHEBI:33281` antimicrobial agent and `CHEBI:33282` antibacterial agent as direct `has role` targets for `CHEBI:66678`; filing the record as `ANTIBACTERIAL` follows the retained ChEBI antibacterial role. OLS4 also reports the non-antimicrobial `CHEBI:35610` antineoplastic agent, `CHEBI:76507` marine metabolite, and `CHEBI:76969` bacterial metabolite roles, which the generated `activity_roles` field correctly omits. |
| Xrefs | OLS4 and `data/raw/chebi_antimicrobials.tsv` both list the exact-equivalence `reaxys:11303256` xref retained in the YAML. The remaining database cross-references on the OLS term are PubMed literature identifiers and correctly do not appear in the structure-identity `xrefs` field. |
| MIBiG producer import | The official MIBiG `BGC0001159` entry is active, version 5, and quality `questionable`; it lists `marinopyrrole A` with formula `C22H12Cl4N2O4`, names the producer as `Streptomyces sp. CNQ-418`, and assigns NCBI taxon `467194`. NCBI Taxonomy resolves `467194` as a bacterial species-rank `Streptomyces sp. CNQ-418`, matching the YAML's `taxon_label: Streptomyces sp.` plus `strain: CNQ-418` split. |

No wrong identity, grounding, xref, parent, class, or producer-link conflict was
found.

## Evidence

The record has one object-level assertion with evidence: its MIBiG-imported
`ProducerOrganism`.

| Claim | Review |
| --- | --- |
| `PMID:22800473` producer evidence | NCBI resolves `PMID:22800473` to the 2012 Journal of the American Chemical Society paper `Flavoenzyme-catalyzed atropo-selective N,C-bipyrrole homocoupling in marinopyrrole biosynthesis`, DOI `10.1021/ja305670f`. Its PubMed abstract reports discovery and heterologous expression of marinopyrrole biosynthesis genes in `Streptomyces sp. CNQ-418`, consistent with a BGC-level producer source for MIBiG. |
| Inherited producer scope | MIBiG `BGC0001159` lists five compounds, all with empty compound-level `evidence` arrays and empty antibacterial bioactivity `references`; the locus, not `marinopyrrole A` alone, carries `Knock-out studies` and `Heterologous expression` evidence. The YAML is therefore correct to mark `link_evidence_scope: CLUSTER_INHERITED` and to describe `PMID:22800473` as MIBiG's first legacy reference for the entry rather than specific producer/compound proof. |

The ChEBI seed contributes six PubMed literature leads:

| PMID | DOI | Review |
| --- | --- | --- |
| `PMID:18205372` | `10.1021/ol702952n` | Original marine `Streptomyces` discovery/isolation paper for marinopyrroles A and B, with abstract-level anti-MRSA activity but no exposed molecular target or exact MIC. |
| `PMID:19673475` | `10.1021/ja903149u` | Human HCT-116 cell dye-transfer work identifying actin as a putative target of marinopyrrole A; relevant to cytotoxicity and target-discovery chemistry, but not evidence for an antimicrobial molecular target. |
| `PMID:21499535` | `10.1016/j.tetlet.2010.09.059` | Synthesis and anti-MRSA biological evaluation of marinopyrrole A analogues; useful as an activity lead, but the PubMed abstract does not expose assay method, MIC units, or a mechanism. |
| `PMID:21502631` | `10.1128/AAC.01211-10` | Anti-MRSA pharmacology for marinopyrrole A reporting concentration-dependent bactericidal activity, postantibiotic effect, resistance profile, and serum neutralization at abstract level; likely the best lead for future `activity_spectrum` or `cidality` curation after full-text inspection. |
| `PMID:22311987` | `10.1074/jbc.M111.334532` | Human leukemia/cancer-cell work naming marinopyrrole A `maritoclax` and characterizing it as an Mcl-1 antagonist; not evidence for a microbial target. |
| `PMID:22690153` | `10.3390/md10040953` | Marinopyrrole A derivative optimization against MRSA; its PubMed abstract reports that the natural product's anti-MRSA MIC worsened in 20% human serum and that derivative 1a improved on that property, but it does not provide all exact natural-product activity values for this YAML. |

## Completeness

`CHEBI:66678` is structurally grounded and has an honest imported producer
claim, but it remains mechanism-thin. It has no CARD source concept, no CARD
target, no CARD resistance edge, no curator-authored `mode_of_action`, no
molecular target, no activity observation, and no causal graph.

The full worklist places this identifier only on:

- `mechanism`: absent mode of action, with `0 CARD target(s), 0 resistance edge(s) to build on`
- `review-readiness`: `MECHANISM_REVIEW`, with 6 source literature leads, 0 record evidence items, and 0 targets

The same complete worklist has no exact `CHEBI:66678` row for
`target-evidence`, `minted`, `unknown-mech`, `moa-scope`, `aro-class`,
`xref-unverified`, `xref-name-conflict`, `xref-span-conflict`,
`multi-component`, `producer-candidate`, `activity-candidate`,
`unnamed-producer`, or `structure-unreviewed`.

An NCBI PubMed title/abstract search for `"marinopyrrole A"` or `maritoclax`
found 36 papers on 2026-09-24. The search confirms that ChEBI's six PubMed
cross-references are a subset of a larger marinopyrrole A literature rather
than an exhaustive mechanism review.

Empty slots for `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `activity_spectrum`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, and `causal_graphs` are preferable to
inferring a target or measured activity from the ChEBI antibacterial role, from
host actin/Mcl-1 cancer targets, or from MIBiG's antibacterial bioactivity flag.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The record still needs compound-specific antimicrobial mechanism review before it can become `REVIEWED`. | The YAML has no `mode_of_action`, no molecular targets, no activity observations, and no causal graph. `just worklist` keeps `CHEBI:66678` on `mechanism` and `review-readiness`; ChEBI's inspected PubMed leads include activity and human-target studies, but no abstract exposes a source-backed antibacterial molecular target for marinopyrrole A. | Future curator-owned fields on `data/antibiotics/antibacterial/marinopyrrole-a.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings found.

No minor findings found.

## Recommended Edits

1. Do not edit the source-owned identity, structure, synonym, class, role,
   parent, xref, or source-concept fields for `CHEBI:66678`: they reproduce
   from the official ChEBI row, `data/raw/chebi_antimicrobials.tsv`, and
   `data/antibiotics/PATHS.tsv`.
2. Leave the MIBiG-imported `producer_organisms` row scoped as
   `CLUSTER_INHERITED` unless an inspected primary source or future MIBiG entry
   links evidence directly to `marinopyrrole A` rather than the five-compound
   `BGC0001159` cluster.
3. Inspect the full text and tables for the anti-MRSA papers, especially
   `PMID:18205372`, `PMID:21502631`, and `PMID:22690153`, before adding
   `activity_spectrum` rows. Add compound-specific organism and strain
   observations only when the source states assay method plus exact values and
   units; do not copy an analogue's derivative-specific MIC onto the natural
   product.
4. Add `mode_of_action`, `molecular_targets`, or `causal_graphs` only after a
   primary source identifies how marinopyrrole A inhibits MRSA or another
   microbial system. Do not curate the HCT-116 actin or human Mcl-1 findings as
   antimicrobial targets without a source tying them to microbial growth
   inhibition.
5. Keep `curation_status: SEEDED` until identity, structure, class, and the
   antimicrobial mode of action have all been checked and any target claims have
   primary citations.

## Follow-up Checks

If a future curator changes this record:

- Run `just validate-strict data/antibiotics/antibacterial/marinopyrrole-a.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Run `just verify-corpus` to prove source-owned generated fields still match
  `data/raw/`.
- Run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` and
  confirm `CHEBI:66678` leaves `mechanism` and `review-readiness` only after an
  exact mechanism review has actually been curated.
- Re-run `just lint`, `git diff --check`, and `git diff --cached --check`
  before opening a PR.

## Additional Notes

The official ChEBI definition spells the source as `Streptomyces sp.CNQ-418`
without a space after `sp.`. The YAML correctly mirrors that upstream text
rather than normalizing a generated source-owned field.

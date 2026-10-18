---
name: add-uniprot-protein-examples
description: Audit and curate reviewed UniProtKB ProteinExample entries on GENE_OR_PROTEIN causal graph nodes and PRIMARY_LITERATURE molecular targets without collapsing taxon-agnostic target or node groundings.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add UniProt protein examples to AntibioticMech records

Populate or refresh `protein_examples` (`ProteinExample`) on `CausalNode`
(`node_type: GENE_OR_PROTEIN`) and curator-owned `MolecularTarget`
(`source: PRIMARY_LITERATURE`) entries using reviewed Swiss-Prot accessions,
explicit organism scope (`NCBITaxon:<id>` and `organism_label`), and
source-backed experimental or structural provenance (`notes` + `evidence`).

## Boundaries

- **Keep target and node identity taxon-agnostic.** A `MolecularTarget`
  (`target_id` / `gene_symbol`) or `CausalNode` (`grounding`) represents a
  protein family, complex, or molecular function across organisms (GO, InterPro,
  ComplexPortal, ARO, or `REVIEWED_LABEL_ONLY`). A `UniProtKB` accession is an
  organism-specific exemplar and belongs in `protein_examples`, never as the
  primary `target_id` or `CausalNode.grounding`.
- **Never mutate source-owned targets.** `CARD_ARO` and `BINDINGDB`
  `molecular_targets` are owned by `seed_from_sources.py` and checked for
  drift by `just verify-corpus`. Only `MolecularTarget` entries with
  `source: PRIMARY_LITERATURE` and `CausalNode` entries with
  `node_type: GENE_OR_PROTEIN` may receive curated `protein_examples`.
- **Hold non-protein and ambiguous targets explicitly.** Do not attach UniProt
  accessions to rRNA (`16S rRNA`, `23S rRNA`), lipid/peptidoglycan precursors
  (`Lipid II`, `D-Ala-D-Ala`), membrane sterols (`ergosterol`), whole membrane
  envelopes, or multi-subunit complexes where a single subunit would
  misrepresent the binding locus unless each catalytic subunit is listed with an
  explicit subunit role in `notes`. Record held targets and their rationale in
  `curation/uniprot_protein_examples.yaml` under `held_targets`.
- **Do not overclaim organism or strain scope.** When the primary biochemical or
  structural study used a specific organism (for example *Escherichia coli* K-12
  `NCBITaxon:83333`, *Mycobacterium tuberculosis* H37Rv `NCBITaxon:83332`, or
  *Staphylococcus aureus* `NCBITaxon:1280`), record the exact `NCBITaxon` CURIE
  matching the UniProt entry's `OX=` taxid and state any organism or strain
  scope distinction in `notes`.
- **Do not create outbound GitHub issues, PRs, comments, emails, or `@` mentions**
  unless the user explicitly authorizes that exact action.

## Read First

- `CLAUDE.md` for generated-file boundaries, seeder ownership, and curation-event
  requirements.
- `docs/CURATION.md` for target taxon-agnosticism, `ProteinExample` semantics,
  and evidence rules.
- `src/antibioticmech/schema/antibioticmech.yaml` and
  `src/antibioticmech/schema/mech_shared.yaml` for `ProteinExample`,
  `CausalNode`, and `MolecularTarget`.
- `curation/uniprot_protein_examples.yaml` and
  `src/antibioticmech/uniprot_examples.py` for the declarative plan schema and
  the guarded applier.

## Audit the Corpus for Missing UniProt Examples

Inspect records that carry `causal_graphs` or `PRIMARY_LITERATURE`
`molecular_targets` without `protein_examples`:

1. **Scan `causal_graphs` nodes**:
   - Every `CausalNode` with `node_type: GENE_OR_PROTEIN` should carry at least
     one reviewed `UniProtKB:` `ProteinExample` (or be documented under
     `held_targets` if no single reviewed accession applies).
   - Check the node's `label`, `grounding`, `grounding_notes`, and the
     supporting `CausalEdge.evidence` citations in the same graph to identify
     which organism and protein were assayed in the cited primary papers.
2. **Scan `molecular_targets`**:
   - Filter to `source: PRIMARY_LITERATURE` targets whose target is a protein or
     defined catalytic complex (excluding rRNA, lipid/cell-wall precursors, and
     membrane sterols).
   - When a record has both a `PRIMARY_LITERATURE` `MolecularTarget` and a
     corresponding `GENE_OR_PROTEIN` `CausalNode`, keep the curated
     `ProteinExample` entries synchronized across both surfaces.

## Verify Each UniProtKB Accession

Before adding a `ProteinExample` entry to `curation/uniprot_protein_examples.yaml`:

1. Fetch or verify the UniProt entry (`https://rest.uniprot.org/uniprotkb/<ACC>.txt`
   or `.json`) and confirm:
   - The accession is the current primary reviewed Swiss-Prot accession
     (`UniProtKB:<ACC>`, matching `^UniProtKB:([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$`).
   - `gene_symbol` matches the canonical gene name (`GN   Name=...`) or locus tag
     when no standard gene symbol exists.
   - `protein_name` matches the UniProt recommended `RecName: Full=...`.
   - `organism_id` (`NCBITaxon:<id>`) and `organism_label` match the UniProt
     `OX   NCBI_TaxID=...` and `OS   ...` lines.
2. Verify the supporting citation (`PMID:...` or `DOI:...`) in `evidence`:
   - Prefer the primary paper already cited on the parent `MolecularTarget` or
     incident `CausalEdge` when it assays or solves the structure of that exact
     protein, or cite the primary structural/biochemical paper cross-referenced
     on the UniProt entry (for example a co-crystal PDB structure paper).
   - Write an `evidence_snippet` and `notes` that state what the cited study
     established and any organism or subunit scope qualification.

## Update the Declarative Plan and Apply Safely

1. Add or update the record entry in `curation/uniprot_protein_examples.yaml`
   under `records:` (or document an intentionally unpopulated target under
   `held_targets:`).
2. Run a dry run first:

```bash
python scripts/curate_uniprot_protein_examples.py
```

3. Run a single-record canary and inspect the resulting YAML diff:

```bash
python scripts/curate_uniprot_protein_examples.py --apply --only <IDENTIFIER>
```

4. Apply the full plan:

```bash
python scripts/curate_uniprot_protein_examples.py --apply
```

The script validates every touched record in closed mode via
`write_validated_antibiotic`, appends a `CURATED_UNIPROT_PROTEIN_EXAMPLES`
event via `record_curation_event` only when content changes, and refuses to
mutate `CARD_ARO` or `BINDINGDB` targets.

## Regenerate and Verify

After applying changes to `data/antibiotics/`, refresh the derived surfaces and
run the repository gates:

```bash
just review-queue --limit 0 --tsv curation/record_review_queue.tsv
just render
just docs-stats
just validate-strict --quiet
just verify-corpus
just causal-graph-quality --limit 25
just qc
git diff --check
```

## Report

Summarize:

- Records updated, grouped by `GENE_OR_PROTEIN` causal graph nodes and
  `PRIMARY_LITERATURE` molecular targets;
- UniProtKB accessions, gene symbols, organism TaxIDs, and PMIDs/DOIs added;
- Targets or nodes intentionally held in `held_targets` with their scientific
  rationale;
- Validation and QC gate results.

# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 1, Stage 5)

## Executed Validation Gates

1. **Closed LinkML Schema and OAK Ontology Label Validation (`scripts/validate_strict.py`)**
   - Command: `.venv/bin/python scripts/validate_strict.py --quiet --workers 2`
   - Result: `2969 files scanned, 0 files with ERROR, 0 total ERROR rows` (exit code `0`).

2. **Full Corpus Seed Reproduction Check (`scripts/verify_corpus.py`)**
   - Command: `.venv/bin/python scripts/verify_corpus.py`
   - Result: `verify-corpus: OK — corpus reproduces exactly from data/raw/ plus curator inputs` (`records expected: 2969, on disk: 2969, missing: 0, unexpected: 0, drifted fields: 0`, exit code `0`).

3. **Curation Worklist Audit (`scripts/curation_worklist.py`)**
   - Command: `.venv/bin/python scripts/curation_worklist.py`
   - Result:
     - `moa-settled-scope-review`: `0` records (down from `1`; `CHEBI:28077` rifampicin resolved).
     - `SEEDED` records with curated `causal_graphs`: `1` record (`antibioticmech:aro-2eea3233f3`, ofloxacin, `grounding_status: MINTED` because racemic `CHEBI:7731` lacks a 2D molfile in ChEBI v249; all 10 `EXACT` records with curated `causal_graphs` are now `REVIEWED`).
     - Total `REVIEWED` records: `90` (up from `80`).

4. **README Corpus Statistics Check (`scripts/check_docs.py`)**
   - Command: `.venv/bin/python scripts/check_docs.py --check`
   - Result: `README statistics are current.` (exit code `0`).

5. **Native Structured Review Bundle Validation (`scripts/record_review.py`)**
   - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261023T184800Z-stage5-remediated-records-review/review.yaml`
   - Result: `{"valid_reviews": 1}` (exit code `0`).
   - Append-only check: `.venv/bin/python scripts/record_review.py check --base main` -> `{"repository": "culturebotai/AntibioticMech", "valid_reviews": 6, "coverage": "declared_scopes_only"}` (all 5 predecessor bundles in `reviews/structured/` — `20261015T131237Z-card-protein-name-primary-context`, `20261015T134842Z-card-evidence-qualifications`, `20261015T150217Z-mex-component-xrefs`, `20261023T160013Z-rifampicin-record-review`, and `20261023T160534Z-frozen-inventory-cohort-review` — remain byte-for-byte unchanged).

6. **Causal-Graph and UniProt Protein-Example Test Suite (`pytest`)**
   - Command: `.venv/bin/python -m pytest tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py -q`
   - Result: `91 passed` (exit code `0`).

7. **Rendered Pages Synchronization (`scripts/render_pages.py`)**
   - Command: `.venv/bin/python scripts/render_pages.py --check`
   - Result: `pages/ is in step with the corpus` (exit code `0`).

8. **Workflow Evidence & Infrastructure Notebook Validation (`kg_microbe_workflows`)**
   - Command: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml`
   - Result: `valid` (exit code `0`).

# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 6, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `mode_of_action` and `PRIMARY_LITERATURE` `molecular_targets` on the 5 Cycle 6 Stage 1 natural products (`#1334`) and 5 `EXACT` sulfonamides (`#1335`), updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=86`, `held_targets=116`, `sha256=48924828162b01ed91f4c04bcbe9c91f7a56a31c6fbfb0a1cfd7cc133b0cf9c0`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=56f292cb722516c346b6c61a7bc3444f97e524df4abf26cb00a6876931286724`), promoted all 18 `EXACT` ChEBI records (`berninamycin-a`, `berninamycin-b`, `empedopeptin`, `laterocidine`, `obafluorin`, `salinamide-a`, `salinamide-b`, `rimocidin`, `kendomycin-b`, `marinopyrrole-c`, `marinopyrrole-d`, `marinopyrrole-e`, `amipurimycin`, `sulfacetamide`, `sulfamethazine`, `sulfamethizole`, `sulfamethoxazole`, `sulfadiazine`) to `curation_status: REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=63`, `sha256=a71cfb23c56a97ff2bae5bf86d9e38181ee06f54e1d4cd7f2ac462ee4faa4c48`), and recorded [`curation/cycle6_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle6_stage5_review_remediation_transition.json) (`sha256=8875be6909fc1757b42d43a776f3187ff1cba96009694cbc80293364f957899e`) (`BypassSandbox: true`, exit code `0`).

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3086
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                /tmp/instance_validation_failures.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3086   on disk: 3086
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refreshed [`curation/record_review_queue.tsv`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/record_review_queue.tsv) (`sha256=b5838d0e92c8afc86451b52b58eb18344bf745811f7058c72aa6cf90685c468e`): `2,941` unsigned items (`REVIEWED` count increased from `127` to `145`; `PROPOSED` count decreased from `100` to `87`; `SEEDED` count decreased from `2,859` to `2,854`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Refreshed [`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json) (`input_hash=71943e104ed140a4c9c2e25f148a473f5c74a8a0032cd652f74ec23f384ed14e`) and [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json) (`corpus_fingerprint=0c631d0d2ac74b2e`).
   - Chemical Structure Map Check (`BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python scripts/generate_chemical_map.py --check`
     - Exit Code: `0`
     - Literal Output: `chemical map is current: 3086 records, trustworthiness@10=0.9711, neighbor-overlap@10=0.4971`

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`494` records with target or resistance evidence; `88` populated `PRIMARY_LITERATURE` `MolecularTarget` entries with reviewed `UniProtKB` `protein_examples` and `116` `held_targets`).
   - Refresh Run (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError` writing to `README.md` / `pages/`):
     - Command: `.venv/bin/python scripts/check_docs.py --write` and `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       rendered 3086 compound pages, 7 classes -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```
   - Static Site Pages Check (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/render_pages.py --check`
     - Exit Code: `0`
     - Literal Output: `pages/ is in step with the corpus`

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/c6s5_remediated_review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"review": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261105T224500Z-cycle6-stage5-remediated-records-review/review.yaml", "markdown": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261105T224500Z-cycle6-stage5-remediated-records-review/review.md"}
       ```
   - Validate Saved Bundle (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261105T224500Z-cycle6-stage5-remediated-records-review/review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"valid_reviews": 1}
       ```
   - Append-Only Check Across All 21 Structured Review Bundles (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'`):
     - Command: `.venv/bin/python scripts/record_review.py check --require-reviews --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {
         "repository": "culturebotai/AntibioticMech",
         "valid_reviews": 21,
         "coverage": "declared_scopes_only"
       }
       ```

8. **Pytest and Ruff Validation Suites**
   - UniProt Protein Examples, Causal Graphs, Review-Readiness Queue & Embeddings Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py tests/test_review_readiness_queue.py tests/test_embeddings.py`
     - Exit Code: `0` (`193 passed`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/ruff check --no-cache tests/conftest.py tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`All checks passed!`).

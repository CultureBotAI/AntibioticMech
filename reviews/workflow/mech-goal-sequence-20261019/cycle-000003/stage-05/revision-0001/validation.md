# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 3, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `PRIMARY_LITERATURE` `molecular_targets`, updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=61`, `held_targets=91`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=22d8abac0a2b22bb81df1f2800bc085dd00906ff53fb4962cf11d1d930ada3dd`), promoted 5 `EXACT` ChEBI records (`bactobolin-a`, `negamycin`, `besifloxacin`, `ozenoxacin`, `pazufloxacin`) from `curation_status: PROPOSED` to `REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=38`), and recorded [`curation/cycle3_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle3_stage5_review_remediation_transition.json) (`sha256=f257cd9621feabd4b715e6fff37a47361d6e387e80a388ff8311d2b8c2fc8a35`) (`task-16927`, `BypassSandbox: true`, exit code `0`):
     ```text
     Restored 15 files from origin/main
     Applied UniProt examples plan: records=61, held_targets=91, transition_sha256=22d8abac0a2b22bb81df1f2800bc085dd00906ff53fb4962cf11d1d930ada3dd
     Promoted 5 records to REVIEWED; wrote curation/cycle3_stage5_review_remediation_transition.json (sha256=f257cd9621feabd4b715e6fff37a47361d6e387e80a388ff8311d2b8c2fc8a35)
     ```

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Task: `task-16582` (`BypassSandbox: false`)
   - Command: `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3012
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                /tmp/instance_validation_failures.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Task: `task-16583` (`BypassSandbox: false`)
   - Command: `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3012   on disk: 3012
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refresh Run (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'curation/record_review_queue.tsv'`):
     - Command: `.venv/bin/python scripts/curation_worklist.py --queue review-readiness --limit 0 --tsv curation/record_review_queue.tsv`
     - Exit Code: `0`
     - Summary: `=== review-readiness: 2911 item(s) === ... wrote curation/record_review_queue.tsv` (`REVIEWED` count increased from `96` to `101`; `PROPOSED` count decreased from `179` to `174`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Incremental Embedding & Full PaCMAP Projection (`task-16593`, `BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/cycle3_stage5_incremental_embed.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       Updated chemical-structure-map.json in /tmp/antibioticmech_embeddings_c3s5 (3012 records, 0 errors)
       Changed YAML record identifiers (12): ['CHEBI:135622', 'CHEBI:136050', 'CHEBI:138579', 'CHEBI:198310', 'CHEBI:94700', 'antibioticmech:curator-217ed2935e', 'antibioticmech:curator-6bdee75cea', 'antibioticmech:curator-975acd7c4d', 'antibioticmech:curator-a739fc0555', 'antibioticmech:curator-daae3d88a3', 'antibioticmech:curator-e14f58e6dc', 'antibioticmech:curator-f56d459cee']
       Total corpus: 3012, reused: 3000, new to embed: 12
       Loading weights: 100%|█████████████████████| 391/391 [00:00<00:00, 1280.17it/s]
       Warning: random state is set to 42.
       Wrote 3012 PaCMAP points and embeddings to /tmp/antibioticmech_embeddings_c3s5 (corpus_fingerprint=31c337b3d1918805)
       ```
   - Installed into `data/embeddings/` via `cp /tmp/antibioticmech_embeddings_c3s5/chemical-structure-map.json data/embeddings/chemical-structure-map.json && cp /tmp/antibioticmech_embeddings_c3s5/corpus_map.json data/embeddings/corpus_map.json` (`BypassSandbox: true`, exit code `0`).
   - Chemical Structure Map Check (`task-16605`, `BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python scripts/generate_chemical_map.py --check`
     - Exit Code: `0`
     - Literal Output: `chemical map is current: 3012 records, trustworthiness@10=0.9725, neighbor-overlap@10=0.5030`

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`459` records with target or resistance evidence; `64` of `3,012` records carry a `PRIMARY_LITERATURE` `MolecularTarget` (`53` with reviewed `UniProtKB` `protein_examples` across `51` records); `99` literature-seeded compounds).
   - Refresh Run (`task-16598`, `BypassSandbox: true`, after `task-16597` with `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'README.md'`):
     - Command: `.venv/bin/python scripts/check_docs.py --write && .venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       rendered 3012 compound pages, 7 classes, pruned 1 stale -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```
   - Combined Verification Check (`task-16606`, `BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/check_docs.py --check && .venv/bin/python scripts/render_pages.py --check`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics are current.
       rendered 3012 compound pages, 7 classes -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpaae1dwjt/site
       pages/ is in step with the corpus
       ```

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/cycle3_stage5_review_payload.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"markdown_path": "reviews/structured/20261026T071500Z-cycle3-stage5-remediated-records-review/review.md", "review_id": "20261026T071500Z-cycle3-stage5-remediated-records-review", "yaml_path": "reviews/structured/20261026T071500Z-cycle3-stage5-remediated-records-review/review.yaml"}
       ```
   - Validate Saved Bundle (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261026T071500Z-cycle3-stage5-remediated-records-review/review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"valid_reviews": 1}
       ```
   - Append-Only Check Across All 12 Structured Review Bundles (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'`):
     - Command: `.venv/bin/python scripts/record_review.py check --require-reviews --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"repository": "culturebotai/AntibioticMech", "valid_reviews": 12, "coverage": "declared_scopes_only"}
       ```

8. **Pytest and Ruff Validation Suites**
   - Embeddings, UniProt Protein Examples & Causal Graphs Suites (`task-16964`, `BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_embeddings.py tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py`
     - Exit Code: `0` (`141 passed, 1 warning in 427.94s (0:07:07)`).
   - Documentation, Embeddings, and Review-Readiness Queue Suites (`task-16614`, `BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_docs.py tests/test_embeddings.py tests/test_review_readiness_queue.py`
     - Exit Code: `0` (`37 passed, 1 warning in 478.18s (0:07:58)`).
   - Record Review Contract Suite (`task-16626`, `BypassSandbox: true`, because `scripts/record_review.py:_directory` opens `/Users` with `O_DIRECTORY | O_NOFOLLOW`):
     - Command: `.venv/bin/python -m pytest -q tests/test_record_review_contract.py`
     - Exit Code: `0` (`4 passed in 41.84s`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/ruff check --no-cache tests/conftest.py tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`All checks passed!`).

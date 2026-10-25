# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 2, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Task: `task-12602` (`BypassSandbox: false`)
   - Command: `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 2992   on disk: 2992
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Initial Sandboxed Attempt (`task-12601`, `BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/validate_strict.py`
     - Exit Code: `1` (`PermissionError: [Errno 1] Operation not permitted: 'reports/instance_validation_failures.tsv'` after scanning all 2,992 files with `0 ERROR rows so far`).
   - Verified Run Writing TSV to `/tmp` (`task-12607`, `BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
     - Exit Code: `0`
     - Literal Summary Output:
       ```text
       === validate-strict summary ===
         files scanned:      2992
         files with ERROR:   0
         total ERROR rows:   0
         TSV:                /tmp/instance_validation_failures.tsv
       ```

3. **README Statistics Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py))**
   - Refresh Run (`task-12621`, `BypassSandbox: true`, after `task-12611` with `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'README.md'`):
     - Command: `.venv/bin/python scripts/check_docs.py --write`
     - Exit Code: `0`
     - Literal Output: `README statistics refreshed.`

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refresh Run (`task-12634`, `BypassSandbox: true`, after `task-12630` with `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'curation/record_review_queue.tsv'`):
     - Command: `.venv/bin/python scripts/curation_worklist.py --queue review-readiness --limit 0 --tsv curation/record_review_queue.tsv`
     - Exit Code: `0`
     - Summary: `=== review-readiness: 2896 item(s) === ... wrote curation/record_review_queue.tsv` (`REVIEWED` count increased from `90` to `96`; `PROPOSED` count decreased from `83` to `77`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Incremental Embedding & Full PaCMAP Projection (`task-12676`, `BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/stage5_incremental_embed.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       Updated chemical-structure-map.json in /tmp/antibioticmech_embeddings_stage5 (2992 records, 0 errors)
       Changed YAML record identifiers (20): ['CHEBI:10100', 'CHEBI:138488', 'CHEBI:188153', 'CHEBI:228412', 'CHEBI:28429', 'CHEBI:28971', 'CHEBI:34825', 'CHEBI:44499', 'CHEBI:48480', 'antibioticmech:curator-0106724e5f', 'antibioticmech:curator-17023fe654', 'antibioticmech:curator-172bfdd938', 'antibioticmech:curator-18f8e84826', 'antibioticmech:curator-1db8575797', 'antibioticmech:curator-47d32d7a07', 'antibioticmech:curator-4a1156c964', 'antibioticmech:curator-607ce000f8', 'antibioticmech:curator-88af230f5d', 'antibioticmech:curator-cb71d1e3b5', 'antibioticmech:curator-fd1c955758']
       Total corpus: 2992, reused: 2972, new to embed: 20
       Loading weights: 100%|█████████████████████| 391/391 [00:00<00:00, 3132.06it/s]
       Warning: random state is set to 42.
       Wrote 2992 PaCMAP points and embeddings to /tmp/antibioticmech_embeddings_stage5
       ```
   - Installed into `data/embeddings/` via `cp /tmp/antibioticmech_embeddings_stage5/chemical-structure-map.json data/embeddings/chemical-structure-map.json && cp /tmp/antibioticmech_embeddings_stage5/corpus_map.json data/embeddings/corpus_map.json` (`BypassSandbox: true`, exit code `0`).
   - Chemical Structure Map Check (`task-12820`, `BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python scripts/generate_chemical_map.py --check`
     - Exit Code: `0`
     - Literal Output: `chemical map is current: 2992 records, trustworthiness@10=0.9702, neighbor-overlap@10=0.5010`

6. **Static Site Pages Synchronization ([`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py))**
   - Render Run (`task-12709`, `BypassSandbox: true`):
     - Command: `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output: `rendered 2992 compound pages, 7 classes, pruned 1 stale -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages`
   - Combined Verification Check (`task-12768`, `BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/check_docs.py --check && .venv/bin/python scripts/render_pages.py --check && .venv/bin/python scripts/curation_worklist.py --queue structure-unreviewed`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics are current.
       rendered 2992 compound pages, 7 classes -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpua4fqt1t/site
       pages/ is in step with the corpus

       === structure-unreviewed: 0 item(s) ===
       ```

7. **Native Structured Review Bundle Save and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/stage5_review_payload.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"markdown_path": "reviews/structured/20261025T105500Z-cycle2-stage5-remediated-records-review/review.md", "review_id": "20261025T105500Z-cycle2-stage5-remediated-records-review", "yaml_path": "reviews/structured/20261025T105500Z-cycle2-stage5-remediated-records-review/review.yaml"}
       ```
   - Validate Saved Bundle (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261025T105500Z-cycle2-stage5-remediated-records-review/review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"valid_reviews": 1}
       ```
   - Append-Only Check Across All 9 Structured Review Bundles (`task-12752`, `BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'`):
     - Command: `.venv/bin/python scripts/record_review.py check --require-reviews --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"repository": "culturebotai/AntibioticMech", "valid_reviews": 9, "coverage": "declared_scopes_only"}
       ```

8. **Targeted Pytest Validation (`tests/test_docs.py`, `tests/test_structural_observations.py`, `tests/test_embeddings.py`, `tests/test_review_readiness_queue.py`, `tests/test_record_review_contract.py`)**
   - Sandboxed Multi-Suite Run (`task-12756`, `BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_docs.py tests/test_structural_observations.py tests/test_embeddings.py tests/test_review_readiness_queue.py tests/test_record_review_contract.py`
     - Exit Code: `1` (`2 failed, 46 passed, 2 warnings, 2 errors in 647.49s (0:10:47)` — all 46 tests in `test_docs.py`, `test_structural_observations.py`, `test_embeddings.py`, and `test_review_readiness_queue.py` passed; the 2 failures and 2 errors in `test_record_review_contract.py` were caused by `PermissionError: [Errno 1] Operation not permitted: 'Users'` / `'private'` when `scripts/record_review.py:_directory` opened `/Users` or `/private` with `O_DIRECTORY | O_NOFOLLOW` inside the sandbox).
   - Unsandboxed `test_record_review_contract.py` Run (`task-12788`, `BypassSandbox: true`, after `BypassSandbox: false` failed with the same `PermissionError`):
     - Command: `.venv/bin/python -m pytest -q tests/test_record_review_contract.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       ....                                                                     [100%]
       4 passed in 30.14s
       ```

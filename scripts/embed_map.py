#!/usr/bin/env python3
"""2-D map of the corpus from the record embeddings -> data/embeddings/corpus_map.json.

Projects the 1024-d text vectors (scripts/embed_records.py) down to two
dimensions so the site can draw one point per compound, coloured by
antimicrobial class and clickable through to the record.

WHAT THE MAP SHOWS. These are TEXT embeddings, so proximity means "described
similarly" — same class, same structural family, same mechanism, same roles —
not "structurally similar". Two analogues annotated differently sit apart. Read
it as a map of the corpus's own descriptions, which is exactly what makes it
useful for curation: an outlier is usually a record whose annotation is thin or
inconsistent with its neighbours, and a cluster spanning two classes is worth a
look.

PRIMARY projection is PaCMAP, which preserves global structure better than UMAP
or t-SNE on high-dimensional embeddings; `--method umap` and `--method pca` are
alternatives, PCA being deterministic and cheap when a run must be reproducible
without the extra dependency.

Output (committed — small, and the site needs it to render):
  {"method", "model", "n", "classes": [...], "generated_from",
   "points": [[x, y, classIdx, "identifier", "label"], ...]}   # x,y in [0,1]

Generation is retired. Follow docs/TEXT_MAP_INPUTS.md and
conf/embedding-runtime/README.md for the shared BGE/PaCMAP map.
Existing historical and chemical map files are preserved.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EMB = REPO_ROOT / "data" / "embeddings"
OUT = EMB / "corpus_map.json"


def pca_2d(x):
    """Top-2 principal components. Deterministic, no extra dependency."""
    import numpy as np
    xc = x - x.mean(0)
    cov = (xc.T @ xc) / (len(xc) - 1)
    evals, evecs = np.linalg.eigh(cov)
    order = evals.argsort()[::-1]
    coords = xc @ evecs[:, order[:2]]
    return coords, (evals[order[:2]] / evals.sum()).tolist()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--method", choices=["pacmap", "umap", "pca"], default="pacmap")
    ap.add_argument("--neighbors", type=int, default=15)
    ap.add_argument("--min-dist", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=42)
    ap.parse_args()

    print(
        'Legacy text generation is retired. Follow docs/TEXT_MAP_INPUTS.md and '
        'conf/embedding-runtime/README.md to export complete inputs with just '
        'text-map-inputs, then embed/project/check using the shared locked BGE '
        'runtime. Historical and chemical maps are retained.',
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

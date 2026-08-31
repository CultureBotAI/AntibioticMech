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

  just embed-map                       # PaCMAP
  python3 scripts/embed_map.py --method pca
"""

from __future__ import annotations

import argparse
import json
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
    args = ap.parse_args()

    import numpy as np

    vpath = EMB / "vectors.f16.npy"
    if not vpath.exists():
        print("no vectors — run `just embed` first")
        return 2
    vectors = np.load(vpath).astype(np.float32)
    ids = json.loads((EMB / "ids.json").read_text(encoding="utf-8"))
    meta = json.loads((EMB / "records.json").read_text(encoding="utf-8"))
    by_id = {m["id"]: m for m in meta}
    if len(ids) != vectors.shape[0]:
        print(f"ids ({len(ids)}) and vectors ({vectors.shape[0]}) disagree; re-run `just embed`")
        return 2

    explained = None
    if args.method == "pca":
        coords, explained = pca_2d(vectors)
    elif args.method == "umap":
        import umap
        coords = umap.UMAP(n_neighbors=args.neighbors, min_dist=args.min_dist,
                           metric="cosine", random_state=args.seed).fit_transform(vectors)
    else:
        import pacmap
        coords = pacmap.PaCMAP(n_neighbors=args.neighbors, random_state=args.seed
                               ).fit_transform(vectors)
    coords = np.asarray(coords, dtype=np.float32)

    # Normalize into [0,1] so the browser needs no knowledge of the projection's
    # native scale, which differs by method.
    lo, hi = coords.min(0), coords.max(0)
    span = np.where(hi - lo == 0, 1.0, hi - lo)
    unit = (coords - lo) / span

    classes = sorted({(by_id.get(i) or {}).get("class") or "UNKNOWN" for i in ids})
    index = {c: n for n, c in enumerate(classes)}
    points = []
    for n, identifier in enumerate(ids):
        m = by_id.get(identifier) or {}
        points.append([round(float(unit[n][0]), 4), round(float(unit[n][1]), 4),
                       index[m.get("class") or "UNKNOWN"], identifier,
                       m.get("label") or identifier])

    model = json.loads((EMB / "meta.json").read_text(encoding="utf-8")).get("model", "")
    payload = {"method": args.method, "model": model, "n": len(points),
               "classes": classes, "generated_from": "scripts/embed_map.py",
               "points": points}
    if explained:
        payload["explained"] = [round(e, 4) for e in explained]
    OUT.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
    print(f"{len(points):,} points ({args.method}) -> {OUT.relative_to(REPO_ROOT)} "
          f"({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

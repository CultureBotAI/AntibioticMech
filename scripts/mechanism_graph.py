"""Deterministic, dependency-free SVG diagrams for record mechanism graphs.

SVG is emitted during the site build, including for asynchronously loaded record
fragments. No browser library, network request or JavaScript is needed. Tables
remain the complete, accessible evidence view. The layout never infers edges.
"""

from __future__ import annotations

import json
import textwrap
from collections import defaultdict, deque
from hashlib import sha256
from html import escape

from markupsafe import Markup


def graph_svg(graph: dict, instance: str = "graph") -> Markup:
    """Render every supplied node and directed edge, including cycles/isolates.

    Breadth-first layers keep small mechanisms readable. Disconnected components
    and cyclic components get their own seeds. Missing endpoints are explicit
    dashed placeholders rather than silently omitted claims.
    """
    nodes = {str(n["node_id"]): dict(n) for n in (graph.get("nodes") or [])}
    edges = graph.get("edges") or []
    if not nodes and not edges:
        return Markup('<p class="graph-empty">No graph nodes or edges recorded.</p>')
    for edge in edges:
        for key in ("subject", "object"):
            node_id = str(edge[key])
            nodes.setdefault(
                node_id, {"node_id": node_id, "label": node_id, "node_type": "UNRESOLVED", "unresolved": True}
            )
    uid = (
        "graph-"
        + sha256((str(instance) + json.dumps(graph, sort_keys=True, default=str)).encode()).hexdigest()[:16]
    )
    title = str(graph.get("title") or graph.get("graph_id") or "Mechanism graph")
    children: dict[str, list[str]] = defaultdict(list)
    indegree = dict.fromkeys(nodes, 0)
    for edge in edges:
        a, b = str(edge["subject"]), str(edge["object"])
        children[a].append(b)
        indegree[b] += 1
    levels: dict[str, int] = {}
    seeds = [n for n in nodes if not indegree[n]]
    for seed in seeds + list(nodes):
        if seed in levels:
            continue
        levels[seed] = 0
        queue = deque([seed])
        while queue:
            source = queue.popleft()
            for target in children[source]:
                if target not in levels:
                    levels[target] = levels[source] + 1
                    queue.append(target)
    lines = {key: textwrap.wrap(str(n.get("label") or key), 29) or [key] for key, n in nodes.items()}
    box_h = max(76, 40 + max(map(len, lines.values())) * 17)
    box_w, column_gap, row_gap = 236, 180, 90
    rows: dict[int, int] = defaultdict(int)
    positions = {}
    for key in nodes:
        level = levels[key]
        positions[key] = (60 + level * (box_w + column_gap), 70 + rows[level] * (box_h + row_gap))
        rows[level] += 1
    width = max(x for x, _ in positions.values()) + box_w + 100
    height = max(y for _, y in positions.values()) + box_h + 100
    # The longest back-edge excursion gets space inside the viewBox.
    height += len(edges) * 10
    out = [
        '<figure class="mechanism-diagram" style="margin:1rem 0">',
        "<figcaption>Directed graph · arrows run from subject to object. "
        "Focus or hover over a node or arrow for details; the evidence table follows.</figcaption>",
        f'<input type="checkbox" id="{uid}-scale"/>'
        f'<label for="{uid}-scale"> Show at full size (scroll to explore)</label>',
        f"<style>#{uid}-scale:checked ~ div svg {{width:{width}px;height:{height}px}}</style>",
        '<div tabindex="0" role="region" aria-label="Scrollable mechanism graph" '
        'style="overflow:auto;max-height:75vh;border:1px solid #94a3b8;'
        'border-radius:8px;background:#f8fafc">',
        f'<svg xmlns="http://www.w3.org/2000/svg" class="mechanism-svg" role="img" '
        f'aria-labelledby="{uid}-title {uid}-desc" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'style="display:block;max-width:none;font:13px system-ui,sans-serif;color:#172033">',
        f'<title id="{uid}-title">{escape(title)}</title>',
        f'<desc id="{uid}-desc">{len(nodes)} nodes and {len(edges)} directed relationships. '
        "Labels and evidence are also available in the adjacent table.</desc>",
        f'<defs><marker id="{uid}-arrow" markerWidth="10" markerHeight="8" '
        'refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
        '<path d="M0,0 L10,4 L0,8 Z" fill="#475569"/></marker></defs>',
        "<style>.mechanism-svg{width:100%;height:auto}.mechanism-svg .graph-node:focus rect,"
        ".mechanism-svg .graph-node:hover rect"
        "{stroke:#0369a1;stroke-width:3}.mechanism-svg .graph-edge:focus path,"
        ".mechanism-svg .graph-edge:hover path{stroke:#0369a1;stroke-width:3}</style>",
    ]
    parallel: dict[tuple[str, str], int] = defaultdict(int)
    for index, edge in enumerate(edges):
        a, b = str(edge["subject"]), str(edge["object"])
        x1, y1 = positions[a]
        x2, y2 = positions[b]
        pair = (a, b)
        offset = parallel[pair] * 22
        parallel[pair] += 1
        if x2 > x1:
            sx, sy, tx, ty = x1 + box_w, y1 + box_h / 2, x2, y2 + box_h / 2
            bend = (sx + tx) / 2
            path = f"M{sx},{sy} C{bend},{sy - offset} {bend},{ty - offset} {tx},{ty}"
            lx, ly = bend, (sy + ty) / 2 - 10 - offset * 0.75
        elif x1 == x2 and a != b:
            sx, sy, tx, ty = x1 + box_w, y1 + box_h / 2, x2 + box_w, y2 + box_h / 2
            lane = sx + 65 + offset
            path = f"M{sx},{sy} C{lane},{sy} {lane},{ty} {tx},{ty}"
            lx, ly = lane, (sy + ty) / 2
        elif a == b:
            sx, sy = x1 + box_w - 30, y1
            path = f"M{sx},{sy} C{sx + 100},{sy - 60 - offset} {sx - 80},{sy - 60 - offset} {sx - 50},{sy}"
            lx, ly = sx + 10, sy - 30 - offset
        else:
            sx, sy, tx, ty = x1 + box_w / 2, y1 + box_h, x2 + box_w / 2, y2 + box_h
            lane = max(sy, ty) + 40 + index * 10 + offset
            path = f"M{sx},{sy} C{sx},{lane} {tx},{lane} {tx},{ty}"
            lx, ly = (sx + tx) / 2, lane - 5
        predicate = str(edge.get("predicate") or "related to")
        evidence = "; ".join(
            str(e.get("reference", "")) for e in edge.get("evidence", []) if isinstance(e, dict)
        )
        details = f"{nodes[a].get('label', a)} — {predicate} → {nodes[b].get('label', b)}"
        if evidence:
            details += "; Evidence: " + evidence
        out += [
            f'<g class="graph-edge" tabindex="0" role="group" aria-label="{escape(details, quote=True)}" '
            f'data-subject="{escape(a, quote=True)}" data-object="{escape(b, quote=True)}">',
            f'<title>{escape(details)}</title><path d="{path}" fill="none" stroke="#475569" '
            f'stroke-width="1.7" marker-end="url(#{uid}-arrow)"/>',
            f'<text x="{lx}" y="{ly}" text-anchor="middle" fill="#334155" '
            'style="paint-order:stroke;stroke:#f8fafc;stroke-width:4;stroke-linejoin:round">'
            f"{escape(predicate)}</text></g>",
        ]
    for key, node in nodes.items():
        x, y = positions[key]
        node_type = str(node.get("node_type") or "NODE")
        label = str(node.get("label") or key)
        detail = f"{label} ({node_type}); {key}"
        if node.get("grounding"):
            detail += "; " + str(node["grounding"])
        dash = ' stroke-dasharray="5 3"' if node.get("unresolved") else ""
        out += [
            f'<g class="graph-node" tabindex="0" role="group" aria-label="{escape(detail, quote=True)}" '
            f'data-node-id="{escape(key, quote=True)}"><title>{escape(detail)}</title>',
            f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" '
            f'fill="#e0f2fe" stroke="#0369a1"{dash}/>',
            f'<text x="{x + 12}" y="{y + 19}" fill="#075985" font-size="10">{escape(node_type)}</text>',
        ]
        for i, line in enumerate(lines[key]):
            out.append(f'<text x="{x + 12}" y="{y + 39 + i * 17}" fill="#172033">{escape(line)}</text>')
        out.append("</g>")
    out.append("</svg></div></figure>")
    return Markup("\n".join(out))

"""Standard helper for appending CurationEvent entries to a AntibioticRecord.

Every script that mutates a AntibioticRecord YAML should call
``record_curation_event`` to leave an audit trail. Centralizing here means:

* timestamps are ISO-8601 with UTC tz, consistently;
* the ``curation_history`` slot is created on demand;
* re-runs of idempotent migration scripts can short-circuit when the most
  recent event already matches (``skip_if_recent``);
* the schema's ``CurationEvent`` field names (timestamp / curator / action /
  changes / llm_assisted) live in one place.

Usage::

    from antibioticmech.curate.curation_event import record_curation_event

    record_curation_event(
        doc,
        curator="seed_from_sources",
        action="SEEDED_FROM_SOURCES",
        changes="Seeded from data/raw/ inventories (GOLD+BacDive+PREGO)",
    )

Ported from TraitMech's ``src/traitmech/curate/curation_event.py``. The
AntibioticMech ``CurationEvent`` defines the same five fields, so the signature is
unchanged; pass narrative detail in ``changes``.
"""

from __future__ import annotations

import datetime
from typing import Any

__all__ = ["record_curation_event", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp, whole-second precision with a ``Z`` suffix
    (e.g. ``"2026-08-12T04:50:12Z"``) — the repo-wide convention, so re-runs
    produce diffs that differ only where the content did."""
    iso = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return iso.replace("+00:00", "Z")


def record_curation_event(
    doc: dict[str, Any],
    *,
    curator: str,
    action: str,
    changes: str | None = None,
    llm_assisted: bool = False,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``doc['curation_history']``.

    Args:
        doc: The AntibioticRecord dict being mutated. Mutated in place.
        curator: Script or human identifier (e.g. ``"seed_from_sources"``,
            ``"claude"``, ``"jane.smith"``).
        action: SCREAMING_SNAKE_CASE action label
            (e.g. ``"SEEDED_FROM_SOURCES"``, ``"REGROUNDED"``).
        changes: Human-readable description of what changed. Also the right
            field for narrative notes — the schema has no separate ``notes``.
        llm_assisted: True when an LLM produced this change. Emitted only when
            True, so consumers can tell "explicitly not LLM" from "written
            before this field existed".
        timestamp: Override the ISO-8601 timestamp (tests / deterministic
            snapshots). Defaults to current UTC.
        skip_if_recent: When True, do nothing if the most recent entry already
            matches the same ``(curator, action)`` pair — lets an idempotent
            re-run avoid piling up duplicate trail entries.

    Returns:
        The appended event dict (or the matching recent one if
        ``skip_if_recent`` short-circuited).
    """
    history = doc.setdefault("curation_history", [])
    if history is None:
        doc["curation_history"] = history = []

    if skip_if_recent and history:
        last = history[-1]
        if (
            isinstance(last, dict)
            and last.get("curator") == curator
            and last.get("action") == action
        ):
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    if changes is not None:
        event["changes"] = changes
    if llm_assisted:
        event["llm_assisted"] = True

    history.append(event)
    return event

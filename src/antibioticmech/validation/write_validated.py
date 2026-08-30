"""Write-time validation: dump a AntibioticRecord to YAML *only if* it passes
closed-schema LinkML validation.

This is the write-time gate that pairs a script's in-memory mutation step with
a schema check at the same call site, so nothing can write a doc that drifted
into an invalid shape between the mutation and the disk write. The check runs
on the in-memory object rather than a re-load of the emitted YAML, which is the
right granularity for catching missing required fields, unknown fields, and
enum / pattern violations.

Use::

    from antibioticmech.validation.write_validated import (
        write_validated_antibiotic,
        ValidationFailedError,
    )

    try:
        write_validated_antibiotic(doc, path)
    except ValidationFailedError as exc:
        print(exc.summary())
        raise

The validator is cached per schema path (LinkML schema parse + JSON-schema
emit is the slow part), so calling this in a bulk seeding loop is cheap.

Ported from TraitMech's ``src/traitmech/validation/write_validated.py``.
"""

from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity, ValidationResult

DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "antibioticmech.yaml"
DEFAULT_TARGET_CLASS = "AntibioticRecord"

_VALIDATORS: dict[Path, Validator] = {}
_VALIDATOR_LOCK = Lock()


class ValidationFailedError(Exception):
    """Raised when a AntibioticRecord fails closed-schema validation before write."""

    def __init__(self, path: Path | None, errors: list[ValidationResult]):
        self.path = path
        self.errors = errors
        super().__init__(self.summary())

    def summary(self) -> str:
        lines = [
            f"validation failed: {len(self.errors)} error(s)"
            + (f" for {self.path}" if self.path else "")
        ]
        for err in self.errors[:10]:
            lines.append(f"  - {err.message[:200]}")
        if len(self.errors) > 10:
            lines.append(f"  ... + {len(self.errors) - 10} more")
        return "\n".join(lines)


def _get_validator(schema_path: Path) -> Validator:
    """Cache validators keyed by resolved schema path, so a caller can mix
    schemas in one process without silently reusing a stale instance."""
    key = Path(schema_path).resolve()
    with _VALIDATOR_LOCK:
        if key not in _VALIDATORS:
            _VALIDATORS[key] = Validator(
                schema=str(key),
                validation_plugins=[JsonschemaValidationPlugin(closed=True)],
            )
        return _VALIDATORS[key]


def validate_antibiotic(
    doc: dict[str, Any],
    *,
    target_class: str = DEFAULT_TARGET_CLASS,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
) -> list[ValidationResult]:
    """Return the list of ERROR-severity validation results (empty when clean)."""
    validator = _get_validator(schema_path)
    report = validator.validate(doc, target_class=target_class)
    return [r for r in report.results if r.severity == Severity.ERROR]


# Emission options at module scope so a test can import THESE rather than
# re-declaring a copy that would drift from what we actually write.
EMIT_OPTS = {
    "default_flow_style": False,
    "sort_keys": False,
    "allow_unicode": True,
}


def emit_antibiotic_yaml(doc: dict[str, Any], yaml_kwargs: dict[str, Any] | None = None) -> str:
    """Serialise ``doc`` exactly as :func:`write_validated_antibiotic` writes it."""
    return yaml.safe_dump(doc, **{**EMIT_OPTS, **(yaml_kwargs or {})})


def write_validated_antibiotic(
    doc: dict[str, Any],
    path: Path,
    *,
    target_class: str = DEFAULT_TARGET_CLASS,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    yaml_kwargs: dict[str, Any] | None = None,
) -> None:
    """Write ``doc`` to ``path`` as YAML, but only if validation passes.

    Raises :class:`ValidationFailedError` *without writing* when closed-schema
    validation finds any error. Use in place of
    ``path.write_text(yaml.safe_dump(doc, ...))`` inside mutating scripts.

    Re-running this helper over an existing record is byte-identical, which is
    what makes it safe for bulk rewrites: a script that touches one field
    produces a one-field diff rather than burying it in reflow churn.
    ``tests/test_write_validated.py`` enforces the property over the
    whole corpus. Hand-editing a record into a shape ``safe_dump`` would not
    emit breaks that test — reformat through this helper rather than loosening
    the test.
    """
    errors = validate_antibiotic(doc, target_class=target_class, schema_path=schema_path)
    if errors:
        raise ValidationFailedError(path, errors)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(emit_antibiotic_yaml(doc, yaml_kwargs), encoding="utf-8")

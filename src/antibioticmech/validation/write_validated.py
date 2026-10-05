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

import os
import tempfile
from pathlib import Path
from threading import Lock
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity, ValidationResult

from antibioticmech.activity_collections import expand_activities, pack_activities, write_artifacts
from antibioticmech.activity_memberships import FIELD, validate_memberships, write_membership_artifacts

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
    record_path: Path | None = None,
    membership_artifacts: dict[str, bytes] | None = None,
) -> list[ValidationResult]:
    """Return the list of ERROR-severity validation results (empty when clean)."""
    validator = _get_validator(schema_path)
    report = validator.validate(doc, target_class=target_class)
    errors = [r for r in report.results if r.severity == Severity.ERROR]
    if not errors and target_class == DEFAULT_TARGET_CLASS and "activity_collections" in doc:
        try:
            if record_path is None:
                raise ValueError("collection validation requires the record path")
            expanded = expand_activities(doc, record_path)
            report = validator.validate(expanded, target_class=target_class)
            errors.extend(r for r in report.results if r.severity == Severity.ERROR)
        except (ValueError, OSError) as error:
            errors.append(ValidationResult(
                type="activity_collection_error", message=str(error), severity=Severity.ERROR,
            ))
    if not errors and target_class == DEFAULT_TARGET_CLASS and (FIELD in doc or membership_artifacts):
        try:
            if record_path is None:
                raise ValueError("membership validation requires the record path")
            validate_memberships(doc, record_path, artifacts=membership_artifacts)
        except (ValueError, OSError) as error:
            errors.append(ValidationResult(
                type="activity_membership_error", message=str(error), severity=Severity.ERROR,
            ))
    return errors


# Emission options at module scope so a test can import THESE rather than
# re-declaring a copy that would drift from what we actually write.
EMIT_OPTS = {
    "default_flow_style": False,
    "sort_keys": False,
    "allow_unicode": True,
}


def emit_antibiotic_yaml(doc: dict[str, Any], yaml_kwargs: dict[str, Any] | None = None) -> str:
    """Serialise ``doc`` exactly as :func:`write_validated_antibiotic` writes it."""
    physical = doc if "activity_collections" in doc else pack_activities(doc)[0]
    return yaml.safe_dump(physical, **{**EMIT_OPTS, **(yaml_kwargs or {})})


def write_validated_antibiotic(
    doc: dict[str, Any],
    path: Path,
    *,
    target_class: str = DEFAULT_TARGET_CLASS,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    yaml_kwargs: dict[str, Any] | None = None,
    membership_artifacts: dict[str, bytes] | None = None,
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
    try:
        expanded = expand_activities(doc, path) if target_class == DEFAULT_TARGET_CLASS else doc
    except (ValueError, OSError) as error:
        raise ValidationFailedError(path, [
            ValidationResult(type="activity_collection_error", message=str(error), severity=Severity.ERROR),
        ]) from error
    errors = validate_antibiotic(expanded, target_class=target_class, schema_path=schema_path,
                                record_path=path, membership_artifacts=membership_artifacts)
    if errors:
        raise ValidationFailedError(path, errors)
    try:
        physical, artifacts = (pack_activities(expanded) if target_class == DEFAULT_TARGET_CLASS
                               else (expanded, {}))
    except ValueError as error:
        raise ValidationFailedError(path, [
            ValidationResult(type="activity_collection_error", message=str(error), severity=Severity.ERROR),
        ]) from error
    if artifacts:
        report = _get_validator(schema_path).validate(physical, target_class=target_class)
        errors = [r for r in report.results if r.severity == Severity.ERROR]
        if errors:
            raise ValidationFailedError(path, errors)
    text = yaml.safe_dump(physical, **{**EMIT_OPTS, **(yaml_kwargs or {})})
    path.parent.mkdir(parents=True, exist_ok=True)
    write_artifacts(artifacts, path.parent)
    write_membership_artifacts(membership_artifacts or {}, path.parent)
    # Artifacts are immutable and complete before an atomic record replacement.
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(text)
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

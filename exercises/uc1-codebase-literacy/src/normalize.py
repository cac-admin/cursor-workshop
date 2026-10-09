"""Lightweight utilities for cleaning tabular research measurements."""

from __future__ import annotations

from typing import Iterable


def drop_empty_rows(rows: Iterable[dict]) -> list[dict]:
    """Keep rows that have at least one non-empty value."""
    kept: list[dict] = []
    for row in rows:
        if any(str(value).strip() for value in row.values()):
            kept.append(row)
    return kept


def coerce_float(value: str | float | int | None, default: float = float("nan")) -> float:
    """Convert a cell to float; return default when conversion fails."""
    if value is None:
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def zscore(values: list[float]) -> list[float]:
    """Standardize values. Returns zeros when variance is zero."""
    if not values:
        return []
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    if var == 0:
        return [0.0 for _ in values]
    std = var**0.5
    return [(v - mean) / std for v in values]

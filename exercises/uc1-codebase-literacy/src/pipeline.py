"""End-to-end demo pipeline used in the CAC Cursor workshop.

Intentionally under-documented so participants can practice Ask mode
and README generation.
"""

from __future__ import annotations

import csv
from pathlib import Path

from normalize import coerce_float, drop_empty_rows, zscore


def load_measurements(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize(rows: list[dict], value_key: str = "value") -> dict:
    cleaned = drop_empty_rows(rows)
    values = [coerce_float(row.get(value_key)) for row in cleaned]
    values = [v for v in values if v == v]  # drop NaN
    if not values:
        return {"n": 0, "mean": None, "std_z_first": None}
    zs = zscore(values)
    mean = sum(values) / len(values)
    return {"n": len(values), "mean": mean, "std_z_first": zs[0]}


def main() -> None:
    data_path = Path(__file__).resolve().parents[1] / "data" / "measurements.csv"
    if not data_path.exists():
        # Fall back to sibling exercise data if present
        alt = Path(__file__).resolve().parents[2] / "uc2-analysis" / "data" / "measurements.csv"
        data_path = alt
    rows = load_measurements(data_path)
    print(summarize(rows))


if __name__ == "__main__":
    main()

"""Starter script for Use Case 2. Participants expand this with Cursor."""

from pathlib import Path


def main() -> None:
    data = Path(__file__).parent / "data" / "measurements.csv"
    print(f"Load and analyze: {data}")
    print("TODO: load CSV, clean empty values, summarize by condition, plot.")


if __name__ == "__main__":
    main()

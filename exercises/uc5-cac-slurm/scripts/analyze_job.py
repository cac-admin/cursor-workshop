"""Toy analysis entrypoint intended to run inside a SLURM allocation."""

from __future__ import annotations

import os
import time
from pathlib import Path


def main() -> None:
    data = Path(os.environ.get("WORKSHOP_DATA", "data/measurements.csv"))
    print(f"Host: {os.uname().nodename if hasattr(os, 'uname') else 'windows-or-unknown'}")
    print(f"Looking for data at: {data.resolve() if data.exists() else data}")
    # Simulate a short compute burst without stressing a login node in class
    time.sleep(2)
    if data.exists():
        lines = data.read_text(encoding="utf-8").strip().splitlines()
        print(f"Rows (incl. header): {len(lines)}")
    else:
        print("DATA_MISSING: set WORKSHOP_DATA or place measurements.csv beside the job.")
    print("DONE")


if __name__ == "__main__":
    main()

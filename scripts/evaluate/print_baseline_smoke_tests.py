#!/usr/bin/env python3
"""
Print Baseline Smoke Test Prompts

Purpose:
    Prints the baseline smoke test prompts in a readable format for manual testing
    or quick copy/paste into a provider UI.

Example:
    python scripts/evaluate/print_baseline_smoke_tests.py
"""

import csv
from pathlib import Path


def main():
    path = Path("data/baseline_smoke_tests/baseline_smoke_tests_v1.csv")
    if not path.exists():
        raise FileNotFoundError(f"Missing smoke test file: {path}")

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("=" * 80)
            print(f"{row['id']} | {row['category']}")
            print("-" * 80)
            print(row["prompt"])
            print("\nExpected behavior:")
            print(row["expected_behavior"])
            print()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Validate Evaluation Completeness

Purpose:
    Checks whether all three model types have outputs/scores for each benchmark case.

Example:
    python scripts/evaluate/validate_evaluation_completeness.py \
        --combined data/results/combined_scored_results_v1.csv
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path


EXPECTED_MODELS = {"baseline", "rag", "finetuned"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--combined", required=True)
    args = parser.parse_args()

    path = Path(args.combined)
    seen = defaultdict(set)
    categories = {}

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            case_id = row.get("id", "")
            model_type = row.get("model_type", "")
            category = row.get("category", "")
            seen[case_id].add(model_type)
            categories[case_id] = category

    missing_any = False

    for case_id in sorted(seen):
        missing = EXPECTED_MODELS - seen[case_id]
        if missing:
            missing_any = True
            print(f"{case_id} ({categories.get(case_id, '')}) missing: {', '.join(sorted(missing))}")

    if missing_any:
        raise SystemExit("Completeness check failed.")

    print("Completeness check passed: all benchmark cases have baseline, rag, and finetuned results.")


if __name__ == "__main__":
    main()

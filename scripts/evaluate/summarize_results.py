#!/usr/bin/env python3
"""
Summarize Scored Results

Purpose:
    Creates summary tables from combined scored model results.

Outputs:
    1. Overall model summary
    2. Category-by-model summary

Example:
    python scripts/evaluate/summarize_results.py \
        --input data/results/combined_scored_results_v1.csv \
        --overall data/results/overall_model_summary_v1.csv \
        --by-category data/results/category_model_summary_v1.csv
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def safe_float(value):
    try:
        return float(value)
    except Exception:
        return None


def mean(values):
    values = [v for v in values if v is not None]
    if not values:
        return ""
    return round(sum(values) / len(values), 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--overall", required=True)
    parser.add_argument("--by-category", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    overall_path = Path(args.overall)
    by_category_path = Path(args.by_category)
    overall_path.parent.mkdir(parents=True, exist_ok=True)
    by_category_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with input_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    overall_scores = defaultdict(list)
    category_scores = defaultdict(list)

    for row in rows:
        score = safe_float(row.get("score_1_to_5"))
        model_type = row.get("model_type", "")
        category = row.get("category", "")

        if score is None:
            continue

        overall_scores[model_type].append(score)
        category_scores[(category, model_type)].append(score)

    with overall_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model_type", "n_scored", "mean_score"])
        writer.writeheader()
        for model_type in sorted(overall_scores):
            scores = overall_scores[model_type]
            writer.writerow({
                "model_type": model_type,
                "n_scored": len(scores),
                "mean_score": mean(scores)
            })

    with by_category_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "model_type", "n_scored", "mean_score"])
        writer.writeheader()
        for (category, model_type), scores in sorted(category_scores.items()):
            writer.writerow({
                "category": category,
                "model_type": model_type,
                "n_scored": len(scores),
                "mean_score": mean(scores)
            })

    print(f"Saved overall summary to: {overall_path}")
    print(f"Saved category summary to: {by_category_path}")


if __name__ == "__main__":
    main()

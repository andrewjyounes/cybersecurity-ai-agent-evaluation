#!/usr/bin/env python3
"""
Combine Manual Scoring Sheets

Purpose:
    Combines baseline, RAG, and fine-tuned manual scoring sheets into one
    results CSV for analysis.

Expected scoring sheet columns:
    id
    category
    model_type
    model_name
    prompt
    model_answer
    score_1_to_5
    scoring_notes
    reviewer
    review_status

Example:
    python scripts/evaluate/combine_scoring_sheets.py \
        --baseline data/results/baseline_manual_scoring_sheet_v1.csv \
        --rag data/results/rag_manual_scoring_sheet_v1.csv \
        --finetuned data/results/finetuned_manual_scoring_sheet_v1.csv \
        --output data/results/combined_scored_results_v1.csv
"""

import argparse
import csv
from pathlib import Path


def load_rows(path: Path, fallback_model_type: str):
    rows = []
    if not path.exists():
        raise FileNotFoundError(f"Missing scoring sheet: {path}")

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["model_type"] = row.get("model_type") or fallback_model_type
            rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--rag", required=True)
    parser.add_argument("--finetuned", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    all_rows = []
    all_rows.extend(load_rows(Path(args.baseline), "baseline"))
    all_rows.extend(load_rows(Path(args.rag), "rag"))
    all_rows.extend(load_rows(Path(args.finetuned), "finetuned"))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "id",
        "category",
        "model_type",
        "model_name",
        "score_1_to_5",
        "scoring_notes",
        "reviewer",
        "review_status",
        "prompt",
        "model_answer"
    ]

    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Combined {len(all_rows)} rows into: {output_path}")


if __name__ == "__main__":
    main()

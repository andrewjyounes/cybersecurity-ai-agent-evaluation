#!/usr/bin/env python3
"""
Create Manual Scoring Sheet

Purpose:
    Converts model output JSONL into a CSV scoring sheet for human review.

Example:
    python scripts/evaluate/create_manual_scoring_sheet.py \
        --outputs data/results/baseline_outputs_v1.jsonl \
        --scoring-sheet data/results/baseline_manual_scoring_sheet_v1.csv
"""

import argparse
import csv
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs", required=True, help="Model output JSONL file.")
    parser.add_argument("--scoring-sheet", required=True, help="CSV file to create.")
    args = parser.parse_args()

    outputs_path = Path(args.outputs)
    scoring_path = Path(args.scoring_sheet)
    scoring_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with outputs_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            item = json.loads(line)
            rows.append({
                "id": item.get("id", ""),
                "category": item.get("category", ""),
                "model_type": item.get("model_type", ""),
                "model_name": item.get("model_name", ""),
                "prompt": item.get("prompt", ""),
                "model_answer": item.get("model_answer", ""),
                "score_1_to_5": "",
                "scoring_notes": "",
                "reviewer": "",
                "review_status": "not_reviewed"
            })

    fieldnames = [
        "id",
        "category",
        "model_type",
        "model_name",
        "prompt",
        "model_answer",
        "score_1_to_5",
        "scoring_notes",
        "reviewer",
        "review_status"
    ]

    with scoring_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created scoring sheet: {scoring_path}")


if __name__ == "__main__":
    main()

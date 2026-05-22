#!/usr/bin/env python3
"""
Create SFT Train/Validation Split

Purpose:
    Splits a reviewed SFT JSONL file into train and validation sets.

Example:
    python scripts/finetuning/create_sft_train_validation_split.py \
        --input data/sft/train_merged_reviewed.jsonl \
        --train-output data/sft/train.jsonl \
        --validation-output data/validation/validation.jsonl \
        --validation-size 100 \
        --seed 42
"""

import argparse
import json
import random
from pathlib import Path


def load_jsonl(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--train-output", required=True)
    parser.add_argument("--validation-output", required=True)
    parser.add_argument("--validation-size", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if "benchmark" in args.input.lower():
        raise ValueError("Refusing to split benchmark data as SFT data.")

    rows = load_jsonl(args.input)
    random.seed(args.seed)
    random.shuffle(rows)

    validation_size = min(args.validation_size, max(1, len(rows) // 5))
    validation_rows = rows[:validation_size]
    train_rows = rows[validation_size:]

    write_jsonl(args.train_output, train_rows)
    write_jsonl(args.validation_output, validation_rows)

    print(f"Train examples: {len(train_rows)}")
    print(f"Validation examples: {len(validation_rows)}")
    print(f"Train output: {args.train_output}")
    print(f"Validation output: {args.validation_output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Convert SFT Seed CSV to Chat JSONL

Purpose:
    Converts a simple seed CSV into a chat-style JSONL file suitable for review
    before fine-tuning.

Expected input columns:
    input
    output
    category

Example:
    python scripts/finetuning/convert_sft_seed_to_chat_jsonl.py \
        --input data/sft/sft_seed_examples_300_v1.csv \
        --output data/sft/train_draft.jsonl
"""

import argparse
import csv
import json
from pathlib import Path


SYSTEM_PROMPT = "You are a defensive cybersecurity analysis assistant."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--output", required=True, help="Output JSONL path.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8", newline="") as f_in, output_path.open("w", encoding="utf-8") as f_out:
        reader = csv.DictReader(f_in)

        for row_num, row in enumerate(reader, start=1):
            user_content = row.get("input") or row.get("prompt") or row.get("user") or ""
            assistant_content = row.get("output") or row.get("answer") or row.get("assistant") or ""
            category = row.get("category", "")

            if not user_content.strip() or not assistant_content.strip():
                print(f"Skipping row {row_num}: missing input/output")
                continue

            item = {
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_content.strip()},
                    {"role": "assistant", "content": assistant_content.strip()}
                ],
                "category": category,
                "source_type": "sft_seed_example"
            }

            f_out.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"Saved chat JSONL to: {output_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Merge SFT JSONL Files

Purpose:
    Combines multiple reviewed SFT JSONL files into one training file.

Important:
    Do not include benchmark files in the input list.

Example:
    python scripts/finetuning/merge_sft_jsonl.py \
        --inputs data/sft/sft_seed_examples_300_v1.jsonl data/sft/sft_expansion_seed_examples_v1.jsonl data/sft/sft_dataset_batch_1_100_examples_v1.jsonl \
        --output data/sft/train.jsonl
"""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True, help="Input SFT JSONL files.")
    parser.add_argument("--output", required=True, help="Merged output JSONL path.")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    seen_ids = set()

    with output_path.open("w", encoding="utf-8") as out:
        for input_file in args.inputs:
            path = Path(input_file)

            if "benchmark" in str(path).lower():
                raise ValueError(f"Refusing to merge benchmark file into SFT training data: {path}")

            with path.open("r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue

                    item = json.loads(line)

                    item_id = item.get("id")
                    if item_id and item_id in seen_ids:
                        print(f"Warning: duplicate id skipped: {item_id}")
                        continue
                    if item_id:
                        seen_ids.add(item_id)

                    out.write(json.dumps(item, ensure_ascii=False) + "\n")
                    total += 1

    print(f"Merged {total} examples into: {output_path}")


if __name__ == "__main__":
    main()

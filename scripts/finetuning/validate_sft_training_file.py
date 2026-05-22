#!/usr/bin/env python3
"""
Validate SFT Training File

Purpose:
    Performs basic checks on a chat-style SFT JSONL file.

Example:
    python scripts/finetuning/validate_sft_training_file.py \
        --input data/sft/train.jsonl
"""

import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_ROLES = {"system", "user", "assistant"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    path = Path(args.input)
    errors = []
    categories = Counter()
    total = 0

    with path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            if not line.strip():
                continue

            total += 1
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"Line {line_num}: invalid JSON: {exc}")
                continue

            messages = item.get("messages")
            if not isinstance(messages, list):
                errors.append(f"Line {line_num}: missing messages list")
                continue

            roles = [m.get("role") for m in messages if isinstance(m, dict)]
            if not REQUIRED_ROLES.issubset(set(roles)):
                errors.append(f"Line {line_num}: missing required roles; found {roles}")

            for msg in messages:
                if not isinstance(msg.get("content"), str) or not msg.get("content").strip():
                    errors.append(f"Line {line_num}: empty message content")

            category = item.get("category", "UNKNOWN")
            categories[category] += 1

    print(f"Total examples: {total}")
    print("Category distribution:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")

    if errors:
        print("Errors:")
        for err in errors[:50]:
            print(" -", err)
        if len(errors) > 50:
            print(f"... and {len(errors) - 50} more")
        raise SystemExit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()

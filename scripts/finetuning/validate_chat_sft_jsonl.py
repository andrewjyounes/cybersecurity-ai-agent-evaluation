#!/usr/bin/env python3
"""
Validate Chat SFT JSONL

Purpose:
    Checks that a chat-style SFT JSONL file has the basic structure expected
    before a fine-tuning job.

Example:
    python scripts/finetuning/validate_chat_sft_jsonl.py \
        --input data/sft/train_draft.jsonl
"""

import argparse
import json
from pathlib import Path


REQUIRED_ROLES = {"system", "user", "assistant"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input JSONL path.")
    args = parser.parse_args()

    path = Path(args.input)
    errors = []
    count = 0

    with path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            count += 1

            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"Line {line_num}: invalid JSON - {exc}")
                continue

            messages = item.get("messages")
            if not isinstance(messages, list) or len(messages) < 3:
                errors.append(f"Line {line_num}: missing or too-short messages list")
                continue

            roles = [m.get("role") for m in messages if isinstance(m, dict)]
            if not REQUIRED_ROLES.issubset(set(roles)):
                errors.append(f"Line {line_num}: missing required roles; found {roles}")

            for idx, msg in enumerate(messages):
                if not isinstance(msg, dict):
                    errors.append(f"Line {line_num}: message {idx} is not an object")
                    continue
                if msg.get("role") not in REQUIRED_ROLES:
                    errors.append(f"Line {line_num}: invalid role {msg.get('role')}")
                if not isinstance(msg.get("content"), str) or not msg.get("content").strip():
                    errors.append(f"Line {line_num}: empty content in message {idx}")

    print(f"Validated examples: {count}")

    if errors:
        print("Errors found:")
        for err in errors[:50]:
            print(" -", err)
        if len(errors) > 50:
            print(f"... and {len(errors) - 50} more")
        raise SystemExit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()

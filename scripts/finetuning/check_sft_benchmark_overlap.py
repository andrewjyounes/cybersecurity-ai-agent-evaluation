#!/usr/bin/env python3
"""
Check SFT vs Benchmark Overlap

Purpose:
    Checks whether SFT training prompts exactly match benchmark prompts.

This is a basic exact-match check. It does not replace human review or semantic similarity review.

Example:
    python scripts/finetuning/check_sft_benchmark_overlap.py \
        --sft data/sft/train.jsonl \
        --benchmark data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
"""

import argparse
import json
from pathlib import Path


def normalize(text):
    return " ".join((text or "").lower().strip().split())


def get_sft_user_prompt(item):
    messages = item.get("messages", [])
    for msg in messages:
        if msg.get("role") == "user":
            return msg.get("content", "")
    return item.get("input") or item.get("prompt") or ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sft", required=True)
    parser.add_argument("--benchmark", required=True)
    args = parser.parse_args()

    sft_prompts = {}

    with Path(args.sft).open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            prompt = normalize(get_sft_user_prompt(item))
            if prompt:
                sft_prompts[prompt] = line_num

    overlaps = []

    with Path(args.benchmark).open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            prompt = normalize(item.get("prompt", ""))
            if prompt in sft_prompts:
                overlaps.append((line_num, sft_prompts[prompt], item.get("id", "")))

    if overlaps:
        print("Exact overlaps found:")
        for bench_line, sft_line, case_id in overlaps:
            print(f"Benchmark line {bench_line}, SFT line {sft_line}, benchmark id {case_id}")
        raise SystemExit(1)

    print("No exact SFT/benchmark prompt overlaps found.")


if __name__ == "__main__":
    main()

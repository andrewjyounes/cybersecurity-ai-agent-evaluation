# Baseline Model Smoke Test Guide

This guide explains how to test the Baseline Model before running the full benchmark.

## Baseline Definition

The Baseline Model is:

```text
Qwen3.5-35B-A3B
```

with:

```text
No RAG
No fine-tuning
Fixed system prompt
Temperature 0.0
```

## Why Baseline Comes First

The Baseline Model is the control condition. It should be evaluated before interpreting whether RAG or fine-tuning improves performance.

## Environment Variables

Set these locally:

```text
MODEL_API_KEY=your_openrouter_api_key
MODEL_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=qwen/qwen3.5-35b-a3b
```

Do not commit these values to GitHub.

## Smoke Test Command

Run:

```bash
python scripts/evaluate/run_baseline_eval.py \
  --benchmark data/baseline_smoke_tests/baseline_smoke_tests_v1.jsonl \
  --output data/results/baseline_outputs_smoke_test_v1.jsonl
```

## What to Check

After running, confirm:

1. `baseline_outputs_smoke_test_v1.jsonl` exists locally.
2. There is one output per smoke test.
3. No API errors appear.
4. Answers follow a structured cybersecurity format.
5. The fake CVE prompt does not produce invented details.
6. The prompt-injection prompt is resisted.

## Full Benchmark Command

Only after smoke test success:

```bash
python scripts/evaluate/run_baseline_eval.py \
  --benchmark data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl \
  --output data/results/baseline_outputs_v1.jsonl
```

## GitHub Note

The `.gitignore` currently ignores generated result CSV/JSONL files under `data/results/` until they are reviewed. Keep raw outputs local at first.

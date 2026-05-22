# Baseline Model Smoke Tests

This folder contains a small smoke test set for checking whether the Baseline Model is connected and producing usable outputs before running the full held-out benchmark.

These smoke tests are not the final benchmark.

## Purpose

The Baseline Model is the control condition.

It should use:

```text
Same base model
No RAG
No fine-tuning
Fixed cybersecurity system prompt
Fixed output schema
```

## Files

```text
baseline_smoke_tests_v1.csv
baseline_smoke_tests_v1.jsonl
```

## When to Use

Use after:

1. OpenRouter credentials are active.
2. Qwen3.5-35B-A3B is accessible.
3. The baseline evaluation script is configured.
4. Before running the full 120-case benchmark.

## Pass/Fail Criteria

The smoke test passes if:

- the API call works
- outputs are saved correctly
- answers are structured enough to score
- the model does not obviously hallucinate
- the model ignores simple malicious instruction overrides

## Final Benchmark Reminder

The final benchmark remains:

```text
data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

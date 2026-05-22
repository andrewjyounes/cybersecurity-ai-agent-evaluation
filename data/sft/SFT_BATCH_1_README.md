# SFT Dataset Batch 1

This folder contains the first expanded supervised fine-tuning batch for the Cybersecurity AI Agent Evaluation Project.

## Purpose

These examples are designed to teach the Fine-Tuned Model structured defensive cybersecurity behavior.

They are not final benchmark examples.

## Files

```text
sft_dataset_batch_1_100_examples_v1.csv
sft_dataset_batch_1_100_examples_v1.jsonl
```

Both files contain the same 100 examples in different formats.

## Category Distribution

| Category | Examples |
|---|---:|
| Alert Classification | 30 |
| MITRE ATT&CK Mapping | 20 |
| Incident Response | 20 |
| Hallucination Resistance | 15 |
| Prompt-Injection Resistance | 15 |
| **Total** | 100 |

## Important Rules

Do not mix these examples with the held-out benchmark.

The held-out benchmark remains:

```text
data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

## Safety Scope

These examples are defensive and focus on:

- SOC-style alert triage
- safe incident response
- cautious MITRE ATT&CK mapping
- hallucination resistance
- prompt-injection resistance

They are not intended to teach offensive exploitation or unauthorized activity.

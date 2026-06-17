# Benchmark Test Set

This folder contains benchmark materials for the Cybersecurity AI Agent Evaluation Project.

## Current Status

The existing benchmark files in this folder were created under the older six-category benchmark structure.

Those older benchmark files are now treated as **legacy/deprecated** and should not be mixed with the final seven-category benchmark results.

## Legacy Benchmark Files

```text
cybersecurity_ai_complete_benchmark_test_set_v1.csv
cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

These files contain the older 120-case benchmark.

## Legacy Benchmark Structure

The legacy benchmark used 120 total cases:

| Legacy Category | Cases |
|---|---:|
| Cybersecurity Knowledge | 20 |
| Alert Classification | 20 |
| MITRE ATT&CK Mapping | 20 |
| Incident Response | 20 |
| Hallucination Resistance | 20 |
| Prompt-Injection Resistance | 20 |

Incident Response is no longer a current core scoring category.

## New Intended Benchmark Structure

The updated project uses seven benchmark categories:

1. **Cybersecurity Knowledge**
2. **Alert Classification**
3. **MITRE ATT&CK Mapping**
4. **OWASP**
5. **Hallucination Resistance**
6. **Prompt-Injection Resistance**
7. **Jailbreak**

The intended final benchmark size is:

```text
7 categories × 15 cases per category = 105 total cases
```

## Why the Benchmark Changed

Incident Response was removed as a core category because high-quality incident response answers depend heavily on organization-specific context, available logs, asset criticality, escalation procedures, legal obligations, and business-continuity requirements.

OWASP and Jailbreak were added to strengthen the project’s focus on AI security, LLM application security, and adversarial robustness.

## Important Data Leakage Rule

Final evaluation questions must not appear in supervised fine-tuning data, validation data, RAG corpus construction, smoke tests, prompt optimization, or paper examples before final evaluation.

Using final benchmark examples during training or development would create data leakage and weaken the research design.

## Future Benchmark Files

A later benchmark regeneration task should create:

```text
cybersecurity_ai_7category_benchmark_105_v1.csv
cybersecurity_ai_7category_benchmark_105_v1.jsonl
```

Do not generate these files until the benchmark categories, scoring rubric, and expert review process are finalized.

## Fields for the New Benchmark

The final benchmark should include fields such as:

| Field | Meaning |
|---|---|
| `case_id` | Unique benchmark case identifier |
| `category` | One of the seven benchmark categories |
| `prompt` | Question or scenario shown to the model |
| `expected_behavior` | What a strong answer should do |
| `scoring_notes` | Guidance for assigning a score |
| `source_anchor` | Main source/framework anchor for the expected answer |
| `intended_use` | Data split usage note |
| `adversarial_type` | Optional label for injection/jailbreak/hallucination tests |
| `safety_expected` | Whether refusal, safe redirection, or direct answer is expected |

## Evaluation Protocol

Each model should answer the exact same held-out benchmark prompts:

1. Baseline Model
2. RAG-Enhanced Model
3. Fine-Tuned Model

The outputs should be saved separately under `data/results/`.

Recommended output paths:

```text
data/results/baseline_outputs_v1.jsonl
data/results/rag_outputs_v1.jsonl
data/results/finetuned_outputs_v1.jsonl
data/results/combined_scored_results_v1.csv
data/results/overall_model_summary_v1.csv
data/results/category_model_summary_v1.csv
```

## Notes

This benchmark is designed for defensive cybersecurity and AI-security evaluation. It tests reliability, source-grounded reasoning, structured classification, hallucination resistance, prompt-injection resistance, and jailbreak robustness.

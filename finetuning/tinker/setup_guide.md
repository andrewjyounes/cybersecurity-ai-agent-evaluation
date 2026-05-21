# Tinker Fine-Tuning Setup Guide

This guide explains how to prepare and document the Fine-Tuned Model for the Cybersecurity AI Agent Evaluation Project.

The Fine-Tuned Model should use the same base model family as the Baseline Model and RAG-Enhanced Model. The intended difference is that the Fine-Tuned Model is trained on supervised cybersecurity examples, while the final benchmark remains held out.

---

## Goal

Train a cybersecurity-specialized model that improves on the Baseline Model in structured SOC-style tasks, especially:

1. Alert Classification
2. MITRE ATT&CK Mapping
3. Incident Response Formatting
4. Hallucination-Aware Responses
5. Prompt-Injection Resistance Behavior

The fine-tuned model should learn **response structure and task behavior**, not memorize the final benchmark.

---

## Core Rule

Do not train on the held-out benchmark.

Do not use these files for fine-tuning:

```text
data/benchmark/
```

The benchmark is only for final evaluation.

---

## Recommended Data Split

Use three separated datasets:

```text
data/sft/train.jsonl
data/validation/validation.jsonl
data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

Recommended sizes for the first serious version:

| Split | Suggested Size | Purpose |
|---|---:|---|
| Training | 500-2,000 examples | Fine-tuning |
| Validation | 50-150 examples | Development checks |
| Final Benchmark | 120 cases | Final comparison only |

---

## Training Example Format

Use a consistent JSONL format.

Recommended schema:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a defensive cybersecurity analysis assistant."
    },
    {
      "role": "user",
      "content": "Analyze this alert: Multiple failed login attempts followed by one successful login from a new country."
    },
    {
      "role": "assistant",
      "content": "Classification: Possible credential attack or account compromise\nSeverity: High\nMITRE ATT&CK Mapping: Valid Accounts, Brute Force if supported by logs\nReasoning: The sequence of repeated failures followed by success from a new geography suggests credential guessing or compromised credentials.\nRecommended Actions: Review login history, enforce MFA, reset credentials if suspicious, inspect related mailbox/session activity.\nConfidence: Medium-High\nUncertainty / Verification Notes: More context is needed on user travel, MFA status, and IP reputation."
    }
  ],
  "category": "Alert Classification",
  "source_type": "synthetic_defensive_training_example"
}
```

---

## Target Output Style

The fine-tuned model should learn this answer structure:

```text
Classification:
Severity:
MITRE ATT&CK Mapping:
Reasoning:
Recommended Actions:
Confidence:
Uncertainty / Verification Notes:
```

For questions that do not fit every field, it should still provide a structured answer and explain uncertainty.

---

## Fine-Tuning Data Design

Training examples should cover the same broad task areas as the benchmark, but not duplicate final test cases.

Recommended distribution:

| Category | Suggested Training Share |
|---|---:|
| Alert Classification | 30% |
| MITRE ATT&CK Mapping | 20% |
| Incident Response | 20% |
| Cybersecurity Knowledge | 10% |
| Hallucination Resistance | 10% |
| Prompt-Injection Resistance | 10% |

This gives the fine-tuned model enough examples to learn consistent cybersecurity response behavior.

---

## Data Leakage Controls

Before fine-tuning:

1. Keep the final benchmark in `data/benchmark/`.
2. Keep training examples in `data/sft/`.
3. Keep validation examples in `data/validation/`.
4. Run duplicate/similarity checks.
5. Do not copy benchmark prompts into training data.
6. Do not train on expected benchmark answers.
7. Do not tune prompts after reviewing final benchmark failures unless those runs are marked exploratory.

---

## Recommended Workflow

1. Expand the SFT seed set from 300 to 500-2,000 examples.
2. Convert examples to Tinker-compatible chat format.
3. Validate JSONL formatting.
4. Run a small training job.
5. Evaluate on validation examples.
6. Adjust training set if needed.
7. Run final fine-tuning job.
8. Evaluate the fine-tuned model on the same 120 held-out benchmark cases.
9. Save outputs to:

```text
data/results/finetuned_outputs_v1.jsonl
```

---

## Tinker Usage Notes

The exact Tinker code should follow the current Tinker documentation and your account setup.

Keep the repository implementation provider-neutral where possible:

- store configs in `configs/`
- store data in JSONL format
- store raw outputs in `data/results/`
- never commit API keys or credentials
- document model name, date, hyperparameters, and dataset version

---

## Suggested Fine-Tuning Metadata to Record

For the final paper and reproducibility, record:

```text
base_model:
training_dataset_version:
training_example_count:
validation_example_count:
epochs:
learning_rate:
batch_size:
max_sequence_length:
training_start_date:
training_end_date:
provider:
final_model_identifier:
notes:
```

---

## Paper Methods Language

Suggested wording for the final paper:

> The Fine-Tuned Model used the same base model as the Baseline Model but was trained on supervised cybersecurity examples designed to teach structured defensive analysis behavior. Training examples covered alert classification, MITRE ATT&CK mapping, incident response, hallucination-aware verification, and prompt-injection resistance. The final benchmark cases were excluded from the training and validation sets to prevent data leakage.

---

## Safety Note

The fine-tuning dataset should focus on defensive cybersecurity analysis. It should not teach offensive exploitation steps, malware creation, credential theft, evasion, or unauthorized access workflows.

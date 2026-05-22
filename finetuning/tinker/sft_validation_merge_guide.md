# SFT Validation and Merge Guide

This guide explains how to combine and validate supervised fine-tuning data before using Tinker.

## Goal

Create clean files for later fine-tuning:

```text
data/sft/train.jsonl
data/validation/validation.jsonl
```

## Important Rule

Do not include benchmark files in SFT training or validation data.

Never merge:

```text
data/benchmark/
```

into:

```text
data/sft/
```

## Recommended Workflow

### 1. Merge reviewed SFT files

```bash
python scripts/finetuning/merge_sft_jsonl.py \
  --inputs data/sft/sft_seed_examples_300_v1.jsonl data/sft/sft_expansion_seed_examples_v1.jsonl data/sft/sft_dataset_batch_1_100_examples_v1.jsonl \
  --output data/sft/train_merged_reviewed.jsonl
```

### 2. Create train/validation split

```bash
python scripts/finetuning/create_sft_train_validation_split.py \
  --input data/sft/train_merged_reviewed.jsonl \
  --train-output data/sft/train.jsonl \
  --validation-output data/validation/validation.jsonl \
  --validation-size 100 \
  --seed 42
```

### 3. Validate training file

```bash
python scripts/finetuning/validate_sft_training_file.py \
  --input data/sft/train.jsonl
```

### 4. Validate validation file

```bash
python scripts/finetuning/validate_sft_training_file.py \
  --input data/validation/validation.jsonl
```

### 5. Check benchmark overlap

```bash
python scripts/finetuning/check_sft_benchmark_overlap.py \
  --sft data/sft/train.jsonl \
  --benchmark data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

## Notes

The overlap check is only an exact-match check. A human should still review for near-duplicates or overly similar examples.

## When This Is Needed

Use this after expanding SFT data and before running a Tinker fine-tuning job.

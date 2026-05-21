# Results and Scoring Protocol

This document explains how to evaluate the Baseline Model, RAG-Enhanced Model, and Fine-Tuned Model using the same held-out benchmark.

## Required Raw Output Files

```text
data/results/baseline_outputs_v1.jsonl
data/results/rag_outputs_v1.jsonl
data/results/finetuned_outputs_v1.jsonl
```

## Required Manual Scoring Sheets

```text
data/results/baseline_manual_scoring_sheet_v1.csv
data/results/rag_manual_scoring_sheet_v1.csv
data/results/finetuned_manual_scoring_sheet_v1.csv
```

## Required Summary Files

```text
data/results/combined_scored_results_v1.csv
data/results/overall_model_summary_v1.csv
data/results/category_model_summary_v1.csv
```

## Evaluation Steps

1. Run the Baseline Model on the held-out benchmark.
2. Run the RAG-Enhanced Model on the exact same prompts.
3. Run the Fine-Tuned Model on the exact same prompts.
4. Save raw outputs separately.
5. Create manual scoring sheets.
6. Score each answer from 1-5.
7. Combine scoring sheets.
8. Generate summary tables.
9. Use the summary tables in the final paper.

## Commands

Combine sheets:

```bash
python scripts/evaluate/combine_scoring_sheets.py \
  --baseline data/results/baseline_manual_scoring_sheet_v1.csv \
  --rag data/results/rag_manual_scoring_sheet_v1.csv \
  --finetuned data/results/finetuned_manual_scoring_sheet_v1.csv \
  --output data/results/combined_scored_results_v1.csv
```

Summarize results:

```bash
python scripts/evaluate/summarize_results.py \
  --input data/results/combined_scored_results_v1.csv \
  --overall data/results/overall_model_summary_v1.csv \
  --by-category data/results/category_model_summary_v1.csv
```

Validate completeness:

```bash
python scripts/evaluate/validate_evaluation_completeness.py \
  --combined data/results/combined_scored_results_v1.csv
```

## Paper Reporting

The final paper should include:

- overall mean score by model
- mean score by category and model
- qualitative examples of successes and failures
- discussion of where RAG helped
- discussion of where fine-tuning helped
- limitations of manual scoring
- limitations of using one base model

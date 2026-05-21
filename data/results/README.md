# Results Folder

This folder is for model outputs, manual scoring sheets, and summary tables.

## Raw Output Files

Recommended raw output files:

```text
baseline_outputs_v1.jsonl
rag_outputs_v1.jsonl
finetuned_outputs_v1.jsonl
```

Raw output files should preserve the exact model responses and should not be manually edited after generation.

## Manual Scoring Sheets

Recommended manual scoring files:

```text
baseline_manual_scoring_sheet_v1.csv
rag_manual_scoring_sheet_v1.csv
finetuned_manual_scoring_sheet_v1.csv
```

## Combined Result Files

Recommended summary files:

```text
combined_scored_results_v1.csv
overall_model_summary_v1.csv
category_model_summary_v1.csv
```

## Suggested Process

1. Run each model on the held-out benchmark.
2. Save raw outputs as JSONL.
3. Create manual scoring sheets.
4. Score each answer from 1 to 5 using the shared rubric.
5. Combine scores across all three systems.
6. Analyze results by model and category.
7. Use the summary tables in the final paper.

## Important Notes

Do not store API keys, credentials, or private provider logs in this folder.

During early development, generated result files may be kept local until reviewed. Once reviewed, final clean result tables can be committed for reproducibility.

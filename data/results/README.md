# Results Folder

This folder is for model outputs and scoring files.

Recommended files:

```text
baseline_outputs_v1.jsonl
rag_outputs_v1.jsonl
finetuned_outputs_v1.jsonl
baseline_manual_scoring_sheet_v1.csv
rag_manual_scoring_sheet_v1.csv
finetuned_manual_scoring_sheet_v1.csv
scored_results_v1.csv
```

## Important

Do not edit raw model output files after they are generated.

If manual review is needed, create a separate scoring sheet rather than changing the raw outputs.

## Suggested process

1. Run the model on the held-out benchmark.
2. Save raw outputs as JSONL.
3. Create a manual scoring CSV.
4. Score each answer from 1 to 5.
5. Combine scores across all three systems.
6. Analyze results by category.

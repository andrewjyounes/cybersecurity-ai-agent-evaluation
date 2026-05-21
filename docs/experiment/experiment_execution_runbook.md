# Experiment Execution Runbook

This runbook explains the order for running the full Cybersecurity AI Agent Evaluation Project.

The project compares:

1. Baseline Model
2. RAG-Enhanced Model
3. Fine-Tuned Model

The goal is to evaluate all three systems on the same held-out cybersecurity benchmark.

---

## Current Status

Completed:

- GitHub repository structure
- README and documentation cleanup
- Held-out benchmark test set
- RAG source manifest
- First RAG documents uploaded into AnythingLLM
- Baseline evaluation harness
- Tinker fine-tuning setup plan
- Results scoring pipeline
- Paper template
- RAG smoke test pack
- SFT dataset expansion plan

Waiting on:

- OpenRouter payment/API key setup
- Qwen3.5-35B-A3B model access
- Tinker fine-tuning access/run

---

## Phase 1: RAG Workspace Smoke Test

Use this once OpenRouter is active.

### Required Workspace

```text
cybersecurity-ai-rag-evaluation
```

### Required Model

```text
Qwen: Qwen3.5-35B-A3B
```

### Required Documents

```text
LLMAll_en-US_FINAL.pdf
NIST.CSWP.29.pdf
NIST.SP.800-61r3.pdf
known_exploited_vulnerabilities.csv
```

### First Tests

Ask:

```text
What are the six NIST Cybersecurity Framework 2.0 functions?
```

Expected answer:

```text
Govern, Identify, Protect, Detect, Respond, Recover
```

Then ask:

```text
According to NIST SP 800-61 Rev. 3, how does incident response relate to CSF 2.0?
```

Expected answer should explain that incident response is part of cybersecurity risk management and relates to all six CSF functions.

---

## Phase 2: Baseline Model Smoke Test

Before running the full benchmark, run 3–5 benchmark prompts through the Baseline Model.

Purpose:

- confirm API connection works
- confirm output format is usable
- confirm script saves JSONL correctly
- estimate cost before running all 120 cases

Recommended command:

```bash
python scripts/evaluate/run_baseline_eval.py \
  --benchmark data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl \
  --output data/results/baseline_outputs_smoke_test_v1.jsonl \
  --limit 5
```

If successful, run the full baseline benchmark later:

```bash
python scripts/evaluate/run_baseline_eval.py \
  --benchmark data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl \
  --output data/results/baseline_outputs_v1.jsonl
```

---

## Phase 3: RAG Model Evaluation

Once the AnythingLLM workspace passes smoke tests:

1. Ask the same held-out benchmark prompts.
2. Save answers into:

```text
data/results/rag_outputs_v1.jsonl
```

3. Use the schema in:

```text
rag/anythingllm/anythingllm_output_export_template.md
```

Do not change benchmark prompts during this step.

---

## Phase 4: Fine-Tuning Preparation

Before Tinker training:

1. Expand SFT data.
2. Convert data to chat JSONL.
3. Create validation split.
4. Validate JSONL format.
5. Confirm benchmark overlap check.
6. Record fine-tuning metadata.

Important:

```text
Do not train on data/benchmark/
```

---

## Phase 5: Fine-Tuned Model Evaluation

After Tinker fine-tuning:

1. Record final model identifier.
2. Run the same held-out benchmark prompts.
3. Save outputs to:

```text
data/results/finetuned_outputs_v1.jsonl
```

4. Create manual scoring sheet.

---

## Phase 6: Scoring

Create manual scoring sheets for all three systems:

```text
baseline_manual_scoring_sheet_v1.csv
rag_manual_scoring_sheet_v1.csv
finetuned_manual_scoring_sheet_v1.csv
```

Score each answer from 1 to 5 using:

```text
docs/evaluation/shared_scoring_rubric.md
```

---

## Phase 7: Combine Results

Run:

```bash
python scripts/evaluate/combine_scoring_sheets.py \
  --baseline data/results/baseline_manual_scoring_sheet_v1.csv \
  --rag data/results/rag_manual_scoring_sheet_v1.csv \
  --finetuned data/results/finetuned_manual_scoring_sheet_v1.csv \
  --output data/results/combined_scored_results_v1.csv
```

Then summarize:

```bash
python scripts/evaluate/summarize_results.py \
  --input data/results/combined_scored_results_v1.csv \
  --overall data/results/overall_model_summary_v1.csv \
  --by-category data/results/category_model_summary_v1.csv
```

---

## Phase 8: Final Paper

Once results are complete:

1. Add overall score table.
2. Add category score table.
3. Add qualitative examples.
4. Write discussion.
5. Write limitations.
6. Export final PDF from Overleaf.
7. Upload final paper PDF to GitHub.

---

## Key Rule

Do not optimize prompts after seeing final benchmark failures unless the run is labeled exploratory.

Final reported results should come from a fixed benchmark, fixed scoring rubric, and documented model settings.

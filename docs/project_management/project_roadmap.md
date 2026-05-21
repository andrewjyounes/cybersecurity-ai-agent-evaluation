# Project Roadmap

This roadmap organizes the Cybersecurity AI Agent Evaluation Project from repository setup to final research paper.

## Phase 1: Research Design and Repository Setup

Status: In progress

Goals:

- Define research question
- Define hypothesis
- Select benchmark categories
- Create GitHub repository
- Add benchmark data
- Add RAG source manifest
- Add fine-tuning setup plan
- Add evaluation/scoring pipeline
- Add paper template

Key outputs:

```text
README.md
data/benchmark/
docs/references/
docs/evaluation/
rag/
finetuning/
paper/
```

## Phase 2: Source Collection and RAG Corpus Setup

Status: Next

Goals:

- Download high-priority cybersecurity sources
- Record access dates and versions
- Build local RAG corpus
- Configure AnythingLLM workspace
- Test retrieval quality
- Confirm benchmark files are not uploaded into RAG

Key outputs:

```text
rag_corpus/
docs/references/rag_download_checklist_v1.csv
rag/anythingllm/rag_build_checklist.md
data/results/rag_outputs_v1.jsonl
```

## Phase 3: Fine-Tuning Dataset Expansion

Status: Next

Goals:

- Expand SFT seed set from 300 examples to a larger training set
- Convert SFT data to chat-style JSONL
- Create validation split
- Run data leakage checks
- Prepare Tinker fine-tuning run metadata

Key outputs:

```text
data/sft/train.jsonl
data/validation/validation.jsonl
finetuning/tinker/fine_tuning_run_metadata_template.md
```

## Phase 4: Baseline Model Evaluation

Status: Pending

Goals:

- Configure base model endpoint
- Run 3-5 case smoke test
- Run full 120-case benchmark
- Save baseline outputs
- Create manual scoring sheet

Key outputs:

```text
data/results/baseline_outputs_v1.jsonl
data/results/baseline_manual_scoring_sheet_v1.csv
```

## Phase 5: RAG-Enhanced Model Evaluation

Status: Pending

Goals:

- Run the same 120 prompts through the AnythingLLM RAG workspace
- Save raw RAG outputs
- Create manual scoring sheet
- Record retrieval notes if available

Key outputs:

```text
data/results/rag_outputs_v1.jsonl
data/results/rag_manual_scoring_sheet_v1.csv
```

## Phase 6: Fine-Tuned Model Evaluation

Status: Pending

Goals:

- Run Tinker fine-tuning
- Record final model identifier
- Run same 120 prompts on fine-tuned model
- Save raw fine-tuned outputs
- Create manual scoring sheet

Key outputs:

```text
data/results/finetuned_outputs_v1.jsonl
data/results/finetuned_manual_scoring_sheet_v1.csv
```

## Phase 7: Scoring and Results Analysis

Status: Pending

Goals:

- Score all model outputs using the shared 1-5 rubric
- Combine scoring sheets
- Generate overall model summaries
- Generate category-level summaries
- Identify qualitative success/failure examples

Key outputs:

```text
data/results/combined_scored_results_v1.csv
data/results/overall_model_summary_v1.csv
data/results/category_model_summary_v1.csv
```

## Phase 8: Final Paper

Status: Pending

Goals:

- Fill in paper methods
- Add results tables
- Add qualitative examples
- Write discussion and limitations
- Compile in Overleaf
- Upload final PDF to GitHub

Key outputs:

```text
paper/main.tex
paper/references.bib
paper/final_paper.pdf
```

## Current Priority

The next practical priority is:

1. Build local RAG corpus.
2. Configure AnythingLLM workspace.
3. Expand and validate SFT data.
4. Run a small baseline model smoke test.

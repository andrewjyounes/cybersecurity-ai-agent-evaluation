# Cybersecurity AI Agent Evaluation Project

This repository supports a conference-style research paper comparing three versions of the same base model:

1. Baseline Model
2. RAG-Enhanced Model
3. Fine-Tuned Model

The benchmark categories are Cybersecurity Knowledge, Alert Classification, MITRE ATT&CK Mapping, Incident Response, Hallucination Resistance, and Prompt-Injection Resistance.

## Key rule
Do not train on final evaluation cases. Keep training, validation, and final test sets separated to avoid data leakage.

## Suggested workflow
1. Download and record source versions in `docs/references/source_download_checklist_v1.csv`.
2. Put raw documents in `rag_corpus/`.
3. Convert permitted sources into clean chunks under `data/processed/`.
4. Build SFT examples in `data/sft/`.
5. Run the Baseline Model, RAG-Enhanced Model, and Fine-Tuned Model on the held-out test set.
6. Store model outputs and scores in `data/results/`.

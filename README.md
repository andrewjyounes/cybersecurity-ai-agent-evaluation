# Cybersecurity AI Agent Evaluation Project

This repository supports a conference-style research paper evaluating how different adaptation strategies affect the performance of cybersecurity-focused LLM agents.

The project compares three versions of the same base model:

1. **Baseline Model** — the base LLM evaluated with a consistent task prompt and output schema.
2. **RAG-Enhanced Model** — the same base LLM connected to a curated cybersecurity knowledge corpus.
3. **Fine-Tuned Model** — the same base LLM fine-tuned on supervised cybersecurity examples.

The goal is to test whether retrieval augmentation or fine-tuning improves performance over a baseline model on realistic cybersecurity agent tasks.

---

## Research Question

**How do a Baseline Model, RAG-Enhanced Model, and Fine-Tuned Model using the same base LLM compare on SOC-style cybersecurity tasks involving cybersecurity knowledge, alert classification, MITRE ATT&CK mapping, incident response, hallucination resistance, and prompt-injection resistance?**

---

## Hypothesis

The study begins with the following hypothesis:

> A RAG-enhanced model will outperform the baseline model on knowledge-grounded and source-verification tasks, especially cybersecurity knowledge, MITRE ATT&CK mapping, incident response, and hallucination resistance. A fine-tuned model will outperform the baseline model on structured and repeated classification tasks, especially alert classification and standardized response formatting. The strongest overall cybersecurity agent may require a hybrid approach that combines retrieval, fine-tuning, and strong prompting rather than relying on only one adaptation method.

---

## Systems Compared

| System | Description | Purpose |
|---|---|---|
| **Baseline Model** | Base model with a fixed task prompt and output schema | Control condition |
| **RAG-Enhanced Model** | Same base model with access to a curated cybersecurity corpus | Tests the value of retrieval and source grounding |
| **Fine-Tuned Model** | Same base model fine-tuned on cybersecurity examples | Tests the value of supervised specialization |

The project is designed to isolate the effect of adaptation strategy by keeping the base model, test set, scoring rubric, and output schema as consistent as possible.

---

## Benchmark Categories

The held-out benchmark focuses on six scoring categories:

1. **Cybersecurity Knowledge**
2. **Alert Classification**
3. **MITRE ATT&CK Mapping**
4. **Incident Response**
5. **Hallucination Resistance**
6. **Prompt-Injection Resistance**

Categories are included only when they are supported by enough relevant RAG documents, fine-tuning examples, and evaluation cases.

---

## Methodology Overview

The project follows this evaluation process:

1. Build a held-out benchmark test set.
2. Keep training, validation, and final evaluation data separate.
3. Evaluate the Baseline Model on the benchmark.
4. Build the RAG-Enhanced Model using a curated cybersecurity source corpus.
5. Fine-tune the same base model using supervised examples.
6. Evaluate all three systems on the same held-out benchmark.
7. Score model outputs using a shared rubric.
8. Analyze performance differences by category.
9. Write the final conference-style research paper.

---

## Data Leakage Rule

Final evaluation questions must not appear in the fine-tuning training set.

The project separates:

- **Training data** — used for supervised fine-tuning.
- **Validation data** — used during development.
- **Final test data** — used only for final comparison across the three systems.

This rule is essential for keeping the comparison fair.

---

## Source and Corpus Policy

The RAG corpus is intended to use authoritative and current cybersecurity sources, including:

- NIST Cybersecurity Framework
- NIST incident response guidance
- MITRE ATT&CK
- OWASP LLM security guidance
- CISA Known Exploited Vulnerabilities
- NVD/CVE records
- CWE weakness data

Where possible, the repository stores source manifests and download instructions rather than redistributing copyrighted or restricted documents.

---

## Repository Structure

```text
configs/
  baseline_eval_config.yaml
  rag_anythingllm_config.yaml
  results_scoring_config.yaml
  tinker_finetuning_config.yaml

data/
  benchmark/
    README.md
    cybersecurity_ai_complete_benchmark_test_set_v1.csv
    cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
  results/
    README.md
  sft/
    sft_seed_examples_300_v1.csv
    sft_seed_examples_300_v1.jsonl

docs/
  evaluation/
    results_and_scoring_protocol.md
    shared_scoring_rubric.md
  references/
    rag_download_checklist_v1.csv
    rag_source_manifest_v1.csv
    source_download_checklist_v1.csv

finetuning/
  tinker/
    fine_tuning_run_metadata_template.md
    setup_guide.md
    tinker_finetuning_checklist.md

paper/
  README.md
  main.tex
  references.bib
  figures/
  tables/

rag/
  README.md
  anythingllm/
    anythingllm_output_export_template.md
    rag_build_checklist.md
    setup_guide.md

scripts/
  download/
  evaluate/
  finetuning/
  preprocess/
```

---

## Current Status

This repository is in the early implementation phase.

Completed so far:

- Research question and hypothesis defined
- Benchmark categories selected
- Held-out benchmark test set added
- RAG source manifest added
- AnythingLLM RAG setup guide added
- Tinker fine-tuning setup guide added
- Baseline evaluation harness added
- Results and scoring pipeline added
- Conference-style paper template added

Next planned steps:

1. Download and organize the high-priority RAG corpus locally.
2. Configure the AnythingLLM RAG workspace.
3. Expand the supervised fine-tuning dataset.
4. Convert and validate fine-tuning data in chat JSONL format.
5. Run a small Baseline Model smoke test.
6. Run the full benchmark across all three systems.
7. Score outputs and generate summary tables.
8. Complete the final paper.

---

## Intended Final Output

The main deliverable is **one conference-style technical research paper**.

The GitHub repository supports reproducibility by storing:

- source manifests
- benchmark data
- model configuration files
- evaluation scripts
- scoring rubrics
- result-table templates
- final paper materials

---

## Project Positioning

This project is designed as a research and portfolio project for AI, machine learning, and AI-security applications. It focuses on empirical evaluation of LLM adaptation methods in a cybersecurity setting, with emphasis on reliability, source grounding, hallucination resistance, and adversarial robustness.

---

## Safety and Responsible Use

This project is intended for defensive cybersecurity research and evaluation. It does not aim to automate harmful activity or provide offensive operational guidance. Prompt-injection and hallucination tests are designed to evaluate model reliability, not to enable misuse.

---

## Citation Note

Formal citations will be maintained in the final paper and supporting bibliography. Source manifests in `docs/references/` track source title, version, URL, access date, and role in the benchmark.

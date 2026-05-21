# Suggested GitHub Issues

Use these as GitHub issues or project board tasks.

## Issue 1: Download high-priority RAG sources

Labels: `rag`, `sources`, `data`

Tasks:

- Download NIST CSF 2.0
- Download NIST SP 800-61 Rev. 3
- Download or export MITRE ATT&CK source data
- Download OWASP LLM Top 10 material
- Download CISA KEV catalog
- Record access dates and versions
- Update `rag_download_checklist_v1.csv`

## Issue 2: Configure AnythingLLM RAG workspace

Labels: `rag`, `implementation`

Tasks:

- Create workspace
- Add source documents
- Add RAG system prompt
- Set temperature to 0.0
- Run RAG smoke tests
- Confirm benchmark files are excluded

## Issue 3: Expand SFT training dataset

Labels: `fine-tuning`, `data`

Tasks:

- Expand from 300 seed examples
- Create training set
- Create validation set
- Validate JSONL format
- Check no benchmark overlap

## Issue 4: Run baseline model smoke test

Labels: `baseline`, `evaluation`

Tasks:

- Configure API endpoint
- Run 3-5 benchmark cases
- Confirm output format
- Fix script issues if needed
- Run full benchmark after smoke test

## Issue 5: Run full model evaluations

Labels: `evaluation`, `results`

Tasks:

- Run baseline benchmark
- Run RAG benchmark
- Run fine-tuned benchmark
- Save raw outputs
- Create scoring sheets

## Issue 6: Score model outputs

Labels: `scoring`, `analysis`

Tasks:

- Score baseline outputs
- Score RAG outputs
- Score fine-tuned outputs
- Combine scoring sheets
- Generate summary tables

## Issue 7: Complete final paper

Labels: `paper`, `writing`

Tasks:

- Add methods details
- Add results tables
- Add qualitative examples
- Write discussion
- Write limitations
- Export final PDF

# RAG Build Checklist

Use this checklist while setting up the RAG-Enhanced Model in AnythingLLM.

## Workspace setup

- [ ] Create AnythingLLM workspace
- [ ] Name workspace `cybersecurity-ai-rag-evaluation`
- [ ] Connect the model provider
- [ ] Confirm the same base model is used where possible
- [ ] Set temperature to `0.0`
- [ ] Save the model/settings used

## Corpus setup

- [ ] Download high-priority RAG sources
- [ ] Record source title
- [ ] Record version/date
- [ ] Record URL
- [ ] Record access date
- [ ] Record local file name
- [ ] Add source to `rag_download_checklist_v1.csv`

## High-priority sources

- [ ] NIST CSF 2.0
- [ ] NIST SP 800-61 Rev. 3
- [ ] MITRE ATT&CK Enterprise Matrix
- [ ] MITRE ATT&CK STIX data
- [ ] OWASP LLM Top 10
- [ ] CISA KEV catalog
- [ ] NVD/CVE data
- [ ] CWE Top 25

## Data leakage check

- [ ] Confirm benchmark files were not uploaded to AnythingLLM
- [ ] Confirm SFT files were not uploaded to AnythingLLM
- [ ] Confirm scoring rubrics were not uploaded as source documents
- [ ] Confirm expected answers were not uploaded

## Smoke tests

- [ ] Ask a NIST CSF question
- [ ] Ask an incident response question
- [ ] Ask a MITRE mapping question
- [ ] Ask a fake CVE question
- [ ] Ask a prompt-injection question
- [ ] Confirm the system admits uncertainty when sources do not support a claim

## Final evaluation

- [ ] Run the same 120 held-out benchmark prompts
- [ ] Save raw outputs as `data/results/rag_outputs_v1.jsonl`
- [ ] Create scoring sheet
- [ ] Score using the shared 1-5 rubric
- [ ] Compare to Baseline Model and Fine-Tuned Model

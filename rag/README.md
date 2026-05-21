# RAG Source Plan

This folder documents the planned source strategy for the RAG-Enhanced Model.

The repository should track source manifests and download notes, but it should not automatically redistribute copyrighted or restricted source documents.

## Purpose

The RAG-Enhanced Model should answer benchmark prompts using authoritative cybersecurity sources.

The source plan supports these benchmark categories:

1. Cybersecurity Knowledge
2. Alert Classification
3. MITRE ATT&CK Mapping
4. Incident Response
5. Hallucination Resistance
6. Prompt-Injection Resistance

## Key files

```text
docs/references/rag_source_manifest_v1.csv
docs/references/rag_download_checklist_v1.csv
```

## Recommended local RAG corpus structure

Keep raw downloaded documents locally, or in a private storage location, using a structure like:

```text
rag_corpus/
  01_nist/
  02_mitre/
  03_owasp/
  04_cisa/
  05_vulnerabilities/
  06_vendor_guidance/
```

## AnythingLLM setup principle

When building the AnythingLLM workspace:

1. Add only high-quality and relevant documents.
2. Keep source titles and version dates visible.
3. Avoid adding outdated documents unless they are intentionally used as stale-source tests.
4. Prefer official sources over blogs.
5. Record every document in the download checklist.
6. Do not include the held-out benchmark prompts in the RAG corpus.

## Data leakage rule

The RAG corpus should contain general cybersecurity knowledge sources, not the final benchmark questions or expected answers.

Do not upload:

```text
data/benchmark/
```

into AnythingLLM as a source corpus.

## Source freshness rule

For versioned sources such as MITRE ATT&CK, NIST publications, CISA KEV, and OWASP LLM guidance, record:

- title
- publisher
- version/date
- URL
- access date
- local file name
- benchmark category supported

## Notes

This RAG plan is designed for defensive cybersecurity research and evaluation. It supports a controlled comparison between the Baseline Model, RAG-Enhanced Model, and Fine-Tuned Model.

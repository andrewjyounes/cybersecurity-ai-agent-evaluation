# AnythingLLM RAG Smoke Test Guide

Use this guide after OpenRouter credentials are added.

## Workspace

Use the workspace:

```text
cybersecurity-ai-rag-evaluation
```

## Model

Select:

```text
Qwen: Qwen3.5-35B-A3B
```

through OpenRouter.

## Documents Needed

Make sure these four files are attached to the workspace:

```text
LLMAll_en-US_FINAL.pdf
NIST.CSWP.29.pdf
NIST.SP.800-61r3.pdf
known_exploited_vulnerabilities.csv
```

## First Manual Tests

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

Expected answer:

```text
Incident response is integrated into cybersecurity risk management and relates to all six CSF functions. Detect, Respond, and Recover support active incident handling, while Govern, Identify, and Protect support preparation and risk management.
```

## If It Does Not Work

Check:

1. OpenRouter credentials are saved.
2. The correct model is selected.
3. The four files are attached to the workspace.
4. You are asking inside the correct workspace.
5. The workspace is not using a different provider/model.

## After Smoke Tests Pass

Then proceed to the full benchmark later:

```text
data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

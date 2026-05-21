# RAG Workspace Smoke Tests

This folder contains a small smoke test set for checking whether the AnythingLLM RAG workspace is working before running the full benchmark.

These tests are not the final benchmark. They are quick setup checks.

## When to Use

Use these after:

1. Creating the AnythingLLM workspace.
2. Uploading the first RAG documents.
3. Adding the OpenRouter API key.
4. Selecting `Qwen3.5-35B-A3B` as the workspace model.

## Files

```text
rag_smoke_tests_v1.csv
rag_smoke_tests_v1.jsonl
```

## What the Tests Check

| Test Area | Purpose |
|---|---|
| NIST CSF 2.0 | Confirms the model can retrieve from the CSF document |
| NIST SP 800-61 Rev. 3 | Confirms incident-response retrieval works |
| OWASP LLM Top 10 | Confirms LLM security retrieval works |
| CISA KEV | Confirms the CSV source is usable |
| Hallucination Resistance | Checks that the model does not invent fake CVEs |
| Prompt-Injection Resistance | Checks that the model ignores malicious override instructions |

## Pass/Fail Method

For each prompt:

1. Ask the question in AnythingLLM.
2. Check whether the answer includes the expected core information.
3. Mark the result as pass or fail in your notes.
4. If a test fails, check whether the source document was uploaded and attached to the workspace.

## Do Not Use as Final Evaluation

These are setup checks only. The final evaluation remains:

```text
data/benchmark/cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

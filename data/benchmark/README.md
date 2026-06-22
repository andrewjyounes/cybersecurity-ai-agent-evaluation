# Benchmark Test Set

This folder contains benchmark materials for the Cybersecurity AI Agent Evaluation Project.

## Current Status

The existing benchmark files in this folder were created under the older six-category benchmark structure.

Those older benchmark files are now treated as **legacy/deprecated** and should not be mixed with the final seven-category benchmark results.

## Legacy Benchmark Files

```text
cybersecurity_ai_complete_benchmark_test_set_v1.csv
cybersecurity_ai_complete_benchmark_test_set_v1.jsonl
```

These files contain the older 120-case benchmark.

## Legacy Benchmark Structure

The legacy benchmark used 120 total cases:

| Legacy Category | Cases |
|---|---:|
| Cybersecurity Knowledge | 20 |
| Alert Classification | 20 |
| MITRE ATT&CK Mapping | 20 |
| Incident Response | 20 |
| Hallucination Resistance | 20 |
| Prompt-Injection Resistance | 20 |

Incident Response is no longer a current core scoring category.

## New Intended Benchmark Structure

The updated project uses seven benchmark categories:

1. **Cybersecurity Knowledge**
2. **Alert Classification**
3. **MITRE ATT&CK Mapping**
4. **OWASP**
5. **Hallucination Resistance**
6. **Prompt-Injection Resistance**
7. **Jailbreak**

The intended final benchmark size is:

```text
7 categories × 15 cases per category = 105 total cases
```

## Notes

This benchmark is designed for defensive cybersecurity and AI-security evaluation. It tests reliability, source-grounded reasoning, structured classification, hallucination resistance, prompt-injection resistance, and jailbreak robustness.

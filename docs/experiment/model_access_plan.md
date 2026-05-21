# Model Access Plan

This document tracks which provider/model will be used for each system.

## Preferred Setup

| System | Provider | Model | Status |
|---|---|---|---|
| Baseline Model | OpenRouter | Qwen3.5-35B-A3B | Waiting for API key/funds |
| RAG-Enhanced Model | AnythingLLM + OpenRouter | Qwen3.5-35B-A3B | Documents uploaded; waiting for API key/funds |
| Fine-Tuned Model | Tinker | Qwen3.5-35B-A3B or closest available same-family model | Pending |

## Why This Setup

Using the same base model across systems makes the comparison cleaner.

The intended comparison is:

```text
same base model + prompt only
same base model + RAG
same base model + fine-tuning
```

## Provider Notes

### OpenRouter

Use for:

- Baseline Model
- RAG-Enhanced Model through AnythingLLM

Model:

```text
Qwen: Qwen3.5-35B-A3B
```

### Tinker

Use for:

- Fine-Tuned Model

Record:

```text
base model
training dataset version
training examples
validation examples
hyperparameters
final model identifier
training cost
```

## Credentials Rule

Do not commit API keys, provider credentials, `.env` files, or billing information to GitHub.

Use local environment variables only.

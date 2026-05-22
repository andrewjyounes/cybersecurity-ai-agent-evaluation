# Model Configuration Note

The selected model for the controlled comparison is:

```text
Qwen3.5-35B-A3B
```

Use the same base model for:

```text
Baseline Model
RAG-Enhanced Model
Fine-Tuned Model
```

## Baseline Model

```text
Same base model
No RAG
No fine-tuning
Fixed system prompt and output schema
```

## RAG-Enhanced Model

```text
Same base model
AnythingLLM document retrieval
Curated cybersecurity corpus
```

## Fine-Tuned Model

```text
Same base model
Supervised fine-tuning through Tinker
Defensive cybersecurity examples
```

## Important

Do not describe the fine-tuned model as a “same-family” model unless it becomes technically impossible to fine-tune the exact same base model.

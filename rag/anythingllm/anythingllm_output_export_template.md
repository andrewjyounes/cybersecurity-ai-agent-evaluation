# AnythingLLM Output Export Template

AnythingLLM may not export benchmark outputs in the exact JSONL format needed for analysis.

Use this schema when manually saving RAG outputs:

```json
{
  "id": "CK-001",
  "category": "Cybersecurity Knowledge",
  "prompt": "Original benchmark prompt",
  "model_answer": "Raw RAG model answer",
  "status": "success",
  "error": null,
  "model_type": "rag",
  "model_name": "qwen3.5-35b-a3b",
  "temperature": 0.0,
  "retrieval_notes": "Optional notes on retrieved sources/chunks"
}
```

Save final RAG outputs to:

```text
data/results/rag_outputs_v1.jsonl
```

Each line should be one JSON object.

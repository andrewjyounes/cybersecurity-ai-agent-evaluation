# Evaluation Order Clarification

This note clarifies the correct experiment order and model wording.

## Important Distinction

There are two kinds of tests:

1. **Smoke tests** — quick setup checks.
2. **Final benchmark evaluation** — the actual research experiment.

Smoke tests can happen whenever setup is ready. They are not the final results.

## Final Research Evaluation Order

The actual research experiment should follow this order:

```text
1. Baseline Model full benchmark
2. RAG-Enhanced Model full benchmark
3. Fine-Tuned Model full benchmark
4. Manual scoring
5. Results comparison
6. Final paper
```

## Same Base Model Rule

The paper should describe all three systems as using the same base model:

```text
Baseline Model = same base model without RAG or fine-tuning
RAG-Enhanced Model = same base model with retrieval
Fine-Tuned Model = same base model after supervised fine-tuning
```

Avoid saying:

```text
same-family model
closest available model
```

unless implementation constraints later make that unavoidable.

## Paper Wording

Use this wording:

```text
The Baseline Model was evaluated first to establish control performance. The RAG-Enhanced Model and Fine-Tuned Model were then evaluated on the same held-out benchmark to measure whether retrieval augmentation or supervised fine-tuning improved performance over the same base model.
```

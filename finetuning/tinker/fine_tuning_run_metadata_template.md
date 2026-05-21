# Fine-Tuning Run Metadata

Use this template for each fine-tuning run.

## Run ID

```text
ft_run_001
```

## Model

```text
Base model:
Tinker model ID:
Final model ID:
```

## Dataset

```text
Training dataset:
Training examples:
Validation dataset:
Validation examples:
Benchmark used for final evaluation:
```

## Hyperparameters

```text
Epochs:
Learning rate:
Batch size:
Max sequence length:
Seed:
```

## Cost Tracking

```text
Estimated training tokens:
Estimated training cost:
Actual training cost:
Evaluation cost:
Total cost:
```

## Notes

```text
What changed in this run:
Known limitations:
Decision after validation:
```

## Data Leakage Check

- [ ] Benchmark was not used for training
- [ ] Benchmark was not used for validation
- [ ] Expected benchmark answers were not used
- [ ] RAG corpus was not used as SFT answer key without review

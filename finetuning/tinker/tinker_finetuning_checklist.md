# Tinker Fine-Tuning Checklist

Use this checklist before running the fine-tuning job.

## Dataset preparation

- [ ] Confirm benchmark files are separate from training files
- [ ] Confirm training data is in `data/sft/`
- [ ] Confirm validation data is in `data/validation/`
- [ ] Confirm no API keys are in the dataset
- [ ] Confirm examples are defensive and safe
- [ ] Confirm examples use a consistent output structure
- [ ] Confirm examples do not copy final benchmark prompts

## Dataset quality

- [ ] Alert classification examples included
- [ ] MITRE mapping examples included
- [ ] Incident response examples included
- [ ] Cybersecurity knowledge examples included
- [ ] Hallucination resistance examples included
- [ ] Prompt-injection resistance examples included
- [ ] Severity labels are consistent
- [ ] Confidence labels are consistent
- [ ] Uncertainty language appears where needed

## Format checks

- [ ] JSONL file has one JSON object per line
- [ ] Each example contains messages
- [ ] Each messages list has system, user, and assistant roles
- [ ] Assistant output follows target structure where possible
- [ ] Validation script passes

## Training setup

- [ ] Confirm base model name
- [ ] Confirm Tinker model ID
- [ ] Confirm training hyperparameters
- [ ] Confirm expected cost
- [ ] Confirm output model identifier will be recorded
- [ ] Confirm training logs are saved locally

## Evaluation

- [ ] Run fine-tuned model on the held-out benchmark
- [ ] Save raw outputs as `data/results/finetuned_outputs_v1.jsonl`
- [ ] Create manual scoring sheet
- [ ] Score with same rubric used for baseline and RAG
- [ ] Compare scores by category

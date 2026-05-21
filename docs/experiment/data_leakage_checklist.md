# Data Leakage Checklist

Use this before any final evaluation run.

## Benchmark Protection

- [ ] Benchmark prompts are not in the fine-tuning training set
- [ ] Benchmark expected answers are not in the fine-tuning training set
- [ ] Benchmark prompts are not uploaded to AnythingLLM
- [ ] Benchmark scoring notes are not uploaded to AnythingLLM
- [ ] Benchmark expected behavior fields are not used during model development

## RAG Protection

- [ ] RAG corpus contains source documents only
- [ ] RAG corpus does not contain final benchmark answers
- [ ] RAG corpus does not contain scoring rubrics as source material
- [ ] RAG corpus does not contain private notes that reveal expected answers

## Fine-Tuning Protection

- [ ] Fine-tuning data is separate from validation data
- [ ] Validation data is separate from final benchmark data
- [ ] Training examples are defensive and safe
- [ ] No final benchmark cases are paraphrased into training data

## Evaluation Protection

- [ ] Same benchmark used for all three systems
- [ ] Same scoring rubric used for all three systems
- [ ] Model settings are recorded
- [ ] Raw outputs are preserved before scoring
- [ ] Failed answers are not rewritten before scoring

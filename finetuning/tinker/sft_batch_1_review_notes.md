# SFT Batch 1 Review Notes

Before using this batch for Tinker fine-tuning, review it for:

## Safety

- [ ] No exploit walkthroughs
- [ ] No malware creation steps
- [ ] No credential theft instructions
- [ ] No stealth/evasion instructions
- [ ] No unauthorized access guidance

## Quality

- [ ] Answers follow the target structure
- [ ] Severity labels are reasonable
- [ ] MITRE mappings are cautious and not overclaimed
- [ ] Fake CVEs are not treated as real
- [ ] Prompt-injection examples refuse unsafe overrides

## Data Leakage

- [ ] No final benchmark prompts copied into this batch
- [ ] No final benchmark expected answers copied into this batch
- [ ] No RAG answer keys included

## Next Use

This batch can later be combined with:

```text
sft_seed_examples_300_v1.jsonl
sft_expansion_seed_examples_v1.jsonl
```

into a reviewed training file:

```text
data/sft/train.jsonl
```

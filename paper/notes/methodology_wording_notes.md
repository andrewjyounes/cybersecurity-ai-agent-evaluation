# Paper Methodology Wording Notes

This document explains where to mention key wording in the final research paper.

## Main Rule

Do not over-explain setup details in the introduction.

The introduction should explain the research problem, research question, and hypothesis.

The detailed wording about testing order, baseline model, RAG model, and fine-tuned model belongs mainly in:

```text
Methodology
Experimental Design
Implementation
Evaluation Protocol
Limitations
```

---

## Core Design Principle

The project should be described as a controlled comparison of adaptation strategies using the **same base model**.

Use this wording:

```text
To isolate the effect of adaptation strategy, all three systems use the same base model. The Baseline Model uses the base model without retrieval or fine-tuning. The RAG-Enhanced Model uses the same base model with access to a curated cybersecurity corpus. The Fine-Tuned Model uses the same base model after supervised fine-tuning on defensive cybersecurity examples.
```

Avoid this wording:

```text
same-family model
closest available same-family model
different model family
```

Only mention a limitation if the final implementation unexpectedly cannot use the same base model for fine-tuning.

---

## Where to Mention the Fine-Tuned Model

Use this in the **Methodology / Experimental Design** section:

```text
The Fine-Tuned Model used the same base model as the Baseline Model and RAG-Enhanced Model, but was trained on supervised defensive cybersecurity examples. The fine-tuning dataset was designed to teach structured cybersecurity analysis behavior, including alert classification, MITRE ATT&CK mapping, incident response sequencing, hallucination-aware verification, and prompt-injection resistance.
```

Use this to address data leakage:

```text
The final benchmark was excluded from the fine-tuning training and validation sets. This separation was used to reduce data leakage and ensure that final evaluation measured generalization rather than memorization.
```

---

## Where to Mention Evaluation Order

Use this in the **Evaluation Protocol** section:

```text
The evaluation proceeded in three stages. First, the Baseline Model was evaluated on the held-out benchmark to establish control performance. Second, the RAG-Enhanced Model was evaluated on the same benchmark prompts to measure the effect of retrieval augmentation. Third, the Fine-Tuned Model was evaluated on the same benchmark prompts to measure the effect of supervised specialization. All systems used the same base model and were scored using the same 1–5 rubric.
```

---

## Where to Mention Tinker

Use this in the **Implementation** section:

```text
The Fine-Tuned Model was prepared using Tinker for supervised fine-tuning of the same base model. Training metadata, including dataset version, model identifier, hyperparameters, and run date, was recorded for reproducibility.
```

---

## Where to Mention Limitations

Use this in the **Limitations** section:

```text
This study has several limitations. The benchmark is limited in size and may not capture the full complexity of real SOC environments. Manual scoring introduces reviewer judgment. The RAG system depends on the quality and coverage of the selected source corpus. Fine-tuning results depend on the quality and representativeness of the supervised examples. The findings are also limited to the selected base model and may not generalize to all LLMs.
```

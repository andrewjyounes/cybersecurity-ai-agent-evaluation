# References and Source Tracking

This folder tracks the sources used for the research paper, RAG corpus, and supporting implementation documentation.

The files in this folder have different purposes.

## Files

| File | Purpose |
|---|---|
| `source_download_checklist_v1.csv` | Broad project-level source tracker covering paper sources, RAG sources, Tinker documentation, AnythingLLM documentation, and benchmark precedents. |
| `rag_source_manifest_v1.csv` | RAG-specific source manifest listing the documents and source types intended for the RAG corpus. |
| `rag_download_checklist_v1.csv` | Practical checklist for recording which RAG documents have actually been downloaded, versioned, and added to AnythingLLM. |

## How to Use These Files

Use `source_download_checklist_v1.csv` for the overall research project.

Use `rag_source_manifest_v1.csv` when deciding which sources belong in the RAG corpus.

Use `rag_download_checklist_v1.csv` while downloading and preparing the local RAG corpus.

## Important Rules

1. Record source title, publisher, URL, access date, and version when available.
2. Do not upload copyrighted or restricted raw PDFs unless redistribution is clearly allowed.
3. Prefer official sources such as NIST, MITRE, OWASP, CISA, NVD, and CWE.
4. Do not include final benchmark questions or expected answers in the RAG corpus.
5. Keep raw downloaded source documents local unless they are safe and licensed for public redistribution.

## Local Corpus Note

Raw RAG documents should usually be stored locally in:

```text
rag_corpus/
```

That folder is ignored by `.gitignore` and should not be committed to GitHub by default.

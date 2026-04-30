# Analytics Mastery

This folder contains the analytics, BI, warehousing, dashboard, statistics, cloud analytics, and AI-agent analytics reference layer.

## Structure
- `summaries/`: source summaries, glossary, concept map, and cross-source synthesis.
- `artifacts/`: business AI-agent analytics artifacts.
- `reports/`: inventory, coverage, and ingestion logs.
- `tools/`: reusable ingestion and artifact-generation scripts.

## Rebuild
Run:

```powershell
& "C:\Users\kavin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" ".\analytics\tools\ingest_corpus.py"
& "C:\Users\kavin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" ".\analytics\tools\build_mastery_artifacts.py"
```

Run those from the `mastery` folder. Source documents are expected in `source-documents/`.

## Note
Modern cloud-service details, legal requirements, privacy/security requirements, and market claims should be web-validated before client-facing use.

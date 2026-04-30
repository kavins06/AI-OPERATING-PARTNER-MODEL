# Information and Data Management Mastery System

This folder is a generated, traceable learning and operator system. In this standalone package, the original source documents live in `../source-documents/`.

## What Is Included

- `data/`: machine-readable source records, extracted text, and page/slide/block notes.
- `source-notes/`: human-readable notes for every source and unit.
- `concept-library/`: concept cards, discovered definitions, and framework cards.
- `mastery-curriculum/`: ordered modules, quizzes, flashcards, and capstone sequence.
- `operator-toolkit/`: client-facing templates and SOPs for business AI-agent consulting.
- `business-application/`: use-case maps and cross-segment operating model.
- `quality/`: completeness, remediation, and verification reports.

## Corpus Snapshot

- Sources: 49
- Units processed: 1554
- Extracted words: 544565
- Generated: 2026-04-29T23:07:16

## How To Use

1. Start with `mastery-curriculum/README.md` and complete modules in order.
2. Use `source-notes/README.md` whenever a concept needs source traceability.
3. Use `concept-library/frameworks.md` to convert reading into consulting tools.
4. Use `operator-toolkit/` during real client discovery and implementation design.
5. Use `quality/remediation_queue.md` before treating any legal, privacy, security, or scanned-source claim as client-ready.

## Rebuild Command

```powershell
& 'C:\Users\kavin\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\scripts\build_mastery_system.py --root . --ocr
```

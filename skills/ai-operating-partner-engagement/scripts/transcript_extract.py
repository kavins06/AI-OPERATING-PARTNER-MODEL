#!/usr/bin/env python
"""Create a structured discovery worksheet from a transcript."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


KEYWORDS = {
    "org_context": ["reports to", "reporting", "manager", "director", "vp", "approval", "escalate", "team", "role", "portfolio", "region"],
    "systems_sources": ["system", "spreadsheet", "excel", "dashboard", "report", "email", "database", "portal", "tool"],
    "source_access": ["screen", "module", "path", "folder", "inbox", "filter", "lookup", "search", "field", "export", "access", "permission", "invoice", "work order"],
    "operating_strain": ["slow", "delay", "rework", "manual", "wrong", "missing", "duplicate", "stale", "frustrating"],
    "risk_sensitive": ["sensitive", "private", "confidential", "legal", "approval", "permission", "risk", "compliance"],
    "knowledge": ["usually", "i know", "experience", "rule", "exception", "red flag", "new person", "judgment"],
    "metrics": ["time", "cost", "volume", "rate", "revenue", "error", "cycle", "baseline", "measure"],
    "edge_cases": ["exception", "edge case", "unusual", "rare", "escalate", "miss", "break", "different", "special case"],
    "source_trust": ["trust", "double-check", "source of truth", "conflict", "inconsistent", "reconcile", "authoritative"],
    "decisions_judgment": ["decide", "decision", "approve", "judgment", "confidence", "pause", "review", "sign-off"],
    "evidence_needs": ["example", "document", "screenshot", "report", "tracker", "memo", "email", "record", "artifact"],
}


def matching_lines(text: str, words: list[str]) -> list[str]:
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    found = []
    for line in lines:
        lower = line.lower()
        if line and any(word in lower for word in words):
            found.append(line)
    return found[:20]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript")
    args = parser.parse_args()
    text = Path(args.transcript).read_text(encoding="utf-8", errors="replace")
    print("# Transcript Discovery Worksheet\n")
    print("## Interview Setup\n\n- Discovery zone:\n- Participant role:\n- Why this person was interviewed:\n- Role layer / org context:\n- Reporting, escalation, or approval relationships:\n- Boundaries / what not to ask:\n")
    print("## Work Episodes\n\n- ")
    print("\n## Trigger / Steps / Decisions / Handoffs\n\n- ")
    for section, words in KEYWORDS.items():
        title = section.replace("_", " ").title()
        print(f"\n## {title}\n")
        for line in matching_lines(text, words):
            print(f"- {line}")
        print("\nNotes:\n- ")
    print("\n## Edge Case Register\n")
    print("| Edge Case | Normal Rule It Breaks | Trigger | Detection | Handler | Decision Required | Current Resolution | Frequency | Severity | Validation Needed |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    print("| | | | | | | | | | |")
    print("\n## Information Object And Source Access Register\n")
    print("| Information Object | Used In Step / Decision | System Or Location | Module / Report / Path | Lookup Keys | Required Fields | Compared Against | Access Roles | Alternate Locations | Known Issues | Validation Needed |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    print("| | | | | | | | | | | |")
    print("\n## Silent Evidence Need Log\n")
    print("| Claim / Edge Case / Source Access Path | Linked Information Object | Why Evidence May Be Needed | Possible Artifact Type | Likely Owner | Sensitivity | Priority | Follow-Up Question |")
    print("|---|---|---|---|---|---|---|---|")
    print("| | | | | | | | |")
    print("\n## Interview Quality Score\n")
    print("- Workflow clarity: high / medium / low")
    print("- Recent work episode captured: yes / no")
    print("- Edge cases captured: high / medium / low")
    print("- Systems and sources identified: high / medium / low")
    print("- Source access intelligence captured: high / medium / low")
    print("- Decisions and judgment captured: high / medium / low")
    print("- Source trust captured: high / medium / low")
    print("- Role hierarchy and handoff relationships captured: high / medium / low")
    print("- Role variation captured: high / medium / low")
    print("- Evidence needs logged: yes / no")
    print("- Follow-up required: yes / no")
    print("\n## Cross-Interview Triangulation Notes\n\n- Agreements:\n- Conflicts:\n- Repeated edge cases:\n- Role hierarchy or reporting-line updates:\n- Role variation or standardization opportunities:\n- Source-of-truth questions:\n- Validation needs:\n")
    print("\n## AI Workflow Spec Routing\n\n- Objects ready for Step 5 spec:\n- Fields still partial:\n- Fields unknown:\n- Later enrichment steps required:\n")
    print("\n## Follow-Up Questions\n\n- What did we misunderstand?\n- Which source is authoritative?\n- Which access path, lookup key, or required field is missing?\n- What requires approval or should remain human?\n- Which evidence needs should be consolidated after interviews?\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

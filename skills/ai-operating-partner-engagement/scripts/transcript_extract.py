#!/usr/bin/env python
"""Create a structured discovery worksheet from a transcript."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


KEYWORDS = {
    "systems_sources": ["system", "spreadsheet", "excel", "dashboard", "report", "email", "database", "portal", "tool"],
    "pain_points": ["slow", "delay", "rework", "manual", "wrong", "missing", "duplicate", "stale", "frustrating"],
    "risk_sensitive": ["sensitive", "private", "confidential", "legal", "approval", "permission", "risk", "compliance"],
    "knowledge": ["usually", "i know", "experience", "rule", "exception", "red flag", "new person", "judgment"],
    "metrics": ["time", "cost", "volume", "rate", "revenue", "error", "cycle", "baseline", "measure"],
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
    print("## Work Episodes\n\n- ")
    print("\n## Trigger / Steps / Decisions / Handoffs\n\n- ")
    for section, words in KEYWORDS.items():
        title = section.replace("_", " ").title()
        print(f"\n## {title}\n")
        for line in matching_lines(text, words):
            print(f"- {line}")
        print("\nNotes:\n- ")
    print("\n## Follow-Up Questions\n\n- What did we misunderstand?\n- Which source is authoritative?\n- What requires approval?\n- What should never be automated?\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


#!/usr/bin/env python
"""Score AI-agent readiness from JSON or key=value scores."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DIMENSIONS = [
    "business_value",
    "workflow_clarity",
    "data_quality",
    "knowledge_availability",
    "analytics_maturity",
    "architecture_feasibility",
    "privacy_security_control",
    "human_oversight",
    "measurement",
]


def parse_scores(items: list[str]) -> dict[str, int]:
    scores: dict[str, int] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"Expected key=value, got {item!r}")
        key, value = item.split("=", 1)
        scores[key.strip()] = int(value)
    return scores


def load_scores(path: str | None, items: list[str]) -> dict[str, int]:
    scores: dict[str, int] = {}
    if path:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        scores.update({k: int(v) for k, v in data.items() if k in DIMENSIONS})
    scores.update(parse_scores(items))
    return scores


def decision(total: int, scores: dict[str, int]) -> str:
    if any(scores.get(k, 0) <= 1 for k in DIMENSIONS):
        return "Severe gap: do not automate until critical blockers are fixed."
    if total >= 38:
        return "Strong pilot candidate."
    if total >= 29:
        return "Proceed after fixing named gaps."
    if total >= 20:
        return "Discovery, governance, data-quality, or knowledge-capture project first."
    return "Do not automate yet."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", help="JSON file containing dimension scores")
    parser.add_argument("--score", action="append", default=[], help="Dimension score as key=value")
    parser.add_argument("--template", action="store_true", help="Print a JSON template")
    args = parser.parse_args()

    if args.template:
        print(json.dumps({k: "" for k in DIMENSIONS}, indent=2))
        return 0

    scores = load_scores(args.json, args.score)
    missing = [k for k in DIMENSIONS if k not in scores]
    if missing:
        raise SystemExit("Missing scores: " + ", ".join(missing))
    for key, value in scores.items():
        if value < 1 or value > 5:
            raise SystemExit(f"{key} must be 1-5")
    total = sum(scores[k] for k in DIMENSIONS)
    print(f"Total: {total} / 45")
    print(f"Decision: {decision(total, scores)}")
    print("\nScores:")
    for key in DIMENSIONS:
        print(f"- {key}: {scores[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


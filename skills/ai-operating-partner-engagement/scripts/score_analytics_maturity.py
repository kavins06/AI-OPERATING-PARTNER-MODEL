#!/usr/bin/env python
"""Score analytics maturity from JSON or key=value scores."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DIMENSIONS = [
    "business_question_clarity",
    "source_integration",
    "data_quality",
    "metric_definitions",
    "dashboard_usefulness",
    "governance_stewardship",
    "security_access_control",
    "statistical_modeling_discipline",
    "feedback_monitoring",
    "change_adoption",
]


def parse_scores(items: list[str]) -> dict[str, int]:
    scores: dict[str, int] = {}
    for item in items:
        key, value = item.split("=", 1)
        scores[key.strip()] = int(value)
    return scores


def maturity_level(avg: float) -> int:
    # 1-5 scale aligned with the current readiness rubric scoring_scale.
    # Buckets centered on integer scores with 0.5 boundaries.
    if avg < 1.5:
        return 1
    if avg < 2.5:
        return 2
    if avg < 3.5:
        return 3
    if avg < 4.5:
        return 4
    return 5


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json")
    parser.add_argument("--score", action="append", default=[])
    parser.add_argument("--template", action="store_true")
    args = parser.parse_args()
    if args.template:
        print(json.dumps({k: "" for k in DIMENSIONS}, indent=2))
        return 0
    scores: dict[str, int] = {}
    if args.json:
        data = json.loads(Path(args.json).read_text(encoding="utf-8"))
        scores.update({k: int(v) for k, v in data.items() if k in DIMENSIONS})
    scores.update(parse_scores(args.score))
    missing = [k for k in DIMENSIONS if k not in scores]
    if missing:
        raise SystemExit("Missing scores: " + ", ".join(missing))
    for key, value in scores.items():
        if value < 1 or value > 5:
            raise SystemExit(f"{key} must be 1-5")
    avg = sum(scores[k] for k in DIMENSIONS) / len(DIMENSIONS)
    level = maturity_level(avg)
    print(f"Average: {avg:.2f} / 5")
    print(f"Maturity level: {level}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


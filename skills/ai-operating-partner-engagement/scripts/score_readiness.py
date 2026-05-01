#!/usr/bin/env python
"""Score AI-agent readiness from a Step 14 object or key=value scores."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DIMENSIONS = [
    "business_value",
    "workflow_clarity",
    "source_access_readiness",
    "data_quality",
    "knowledge_guidance_readiness",
    "measurement_readiness",
    "architecture_feasibility",
    "risk_control_readiness",
    "human_oversight_readiness",
    "change_lifecycle_readiness",
]

HARD_GATES = [
    "business_value_gate",
    "workflow_clarity_gate",
    "source_access_gate",
    "data_quality_gate",
    "knowledge_guidance_gate",
    "measurement_gate",
    "technical_feasibility_gate",
    "risk_control_gate",
    "human_oversight_gate",
    "lifecycle_gate",
]

BEHAVIOR_LEVELS = [
    "read_only_summary",
    "draft_and_flag",
    "recommendation_support",
    "human_approved_action",
    "autonomous_action",
]


def parse_scores(items: list[str]) -> dict[str, int]:
    scores: dict[str, int] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"Expected key=value, got {item!r}")
        key, value = item.split("=", 1)
        scores[key.strip()] = int(value)
    return scores


def parse_gate_items(items: list[str]) -> dict[str, str]:
    gates: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise SystemExit(f"Expected gate=value, got {item!r}")
        key, value = item.split("=", 1)
        gates[key.strip()] = value.strip()
    return gates


def read_object(path: str) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    if path.lower().endswith((".yaml", ".yml")):
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise SystemExit("YAML input requires PyYAML. Use JSON or install PyYAML.") from exc
        data = yaml.safe_load(text) or {}
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise SystemExit("Readiness input must be an object")
    return data


def extract_scores(data: dict[str, Any]) -> dict[str, int]:
    scores: dict[str, int] = {}
    flat = {k: v for k, v in data.items() if k in DIMENSIONS}
    scores.update({k: int(v) for k, v in flat.items() if v not in ("", None)})

    dimension_rows = data.get("dimension_scores", [])
    if isinstance(dimension_rows, list):
        for row in dimension_rows:
            if not isinstance(row, dict):
                continue
            dimension = row.get("dimension")
            value = row.get("score_1_to_5")
            if dimension in DIMENSIONS and value not in ("", None):
                scores[str(dimension)] = int(value)
    return scores


def extract_gates(data: dict[str, Any]) -> dict[str, str]:
    gates: dict[str, str] = {}
    gate_rows = data.get("hard_gates", [])
    if isinstance(gate_rows, list):
        for row in gate_rows:
            if not isinstance(row, dict):
                continue
            gate = row.get("gate_id")
            status = row.get("status")
            if gate in HARD_GATES and status:
                gates[str(gate)] = str(status)
    return gates


def extract_behavior(data: dict[str, Any]) -> dict[str, str]:
    behavior: dict[str, str] = {}
    behavior_rows = data.get("behavior_level_readiness", {})
    if isinstance(behavior_rows, dict):
        for level in BEHAVIOR_LEVELS:
            value = behavior_rows.get(level)
            if isinstance(value, dict) and value.get("status"):
                behavior[level] = str(value["status"])
    return behavior


def load_scores(path: str | None, items: list[str]) -> tuple[dict[str, int], dict[str, str], dict[str, str]]:
    scores: dict[str, int] = {}
    gates: dict[str, str] = {}
    behavior: dict[str, str] = {}
    if path:
        data = read_object(path)
        scores.update(extract_scores(data))
        gates.update(extract_gates(data))
        behavior.update(extract_behavior(data))
    scores.update(parse_scores(items))
    return scores, gates, behavior


def decision(total: int, scores: dict[str, int], gates: dict[str, str]) -> str:
    failed = [gate for gate, status in gates.items() if status in {"fail", "blocked"}]
    if failed:
        return "Blocked: route to remediation before any Step 15 build-ready brief. Failed gates: " + ", ".join(failed)
    unknown = [gate for gate, status in gates.items() if status == "unknown"]
    if unknown:
        return "Discovery incomplete: resolve unknown hard gates before treating the score as build-ready."
    if any(scores.get(k, 0) <= 1 for k in DIMENSIONS):
        return "Severe gap: do not automate until critical blockers are fixed."
    if total >= 43:
        return "Ready for Step 15 build-ready implementation brief, still gated by Step 16 approval."
    if total >= 35:
        return "Fix named gaps first, then reconsider Step 15 build-ready brief."
    if total >= 26:
        return "Governance, data, knowledge, technical feasibility, or risk-control readiness plan first."
    return "Do not automate yet."


def print_template() -> None:
    print(
        json.dumps(
            {
                "hard_gates": [{"gate_id": gate, "status": ""} for gate in HARD_GATES],
                "dimension_scores": [
                    {"dimension": dimension, "score_1_to_5": ""}
                    for dimension in DIMENSIONS
                ],
                "behavior_level_readiness": {
                    level: {"status": ""} for level in BEHAVIOR_LEVELS
                },
            },
            indent=2,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", help="JSON or YAML file containing a Step 14 readiness object or flat dimension scores")
    parser.add_argument("--score", action="append", default=[], help="Dimension score as key=value")
    parser.add_argument("--gate", action="append", default=[], help="Hard gate status as gate_id=status")
    parser.add_argument("--template", action="store_true", help="Print a JSON template")
    args = parser.parse_args()

    if args.template:
        print_template()
        return 0

    scores, gates, behavior = load_scores(args.json, args.score)
    gates.update(parse_gate_items(args.gate))
    missing = [k for k in DIMENSIONS if k not in scores]
    if missing:
        raise SystemExit("Missing scores: " + ", ".join(missing))
    for key, value in scores.items():
        if value < 1 or value > 5:
            raise SystemExit(f"{key} must be 1-5")
    total = sum(scores[k] for k in DIMENSIONS)
    print(f"Total: {total} / 50")
    print(f"Decision: {decision(total, scores, gates)}")
    print("\nScores:")
    for key in DIMENSIONS:
        print(f"- {key}: {scores[key]}")
    if gates:
        print("\nHard gates:")
        for key in HARD_GATES:
            if key in gates:
                print(f"- {key}: {gates[key]}")
    if behavior:
        print("\nBehavior readiness:")
        for key in BEHAVIOR_LEVELS:
            if key in behavior:
                print(f"- {key}: {behavior[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

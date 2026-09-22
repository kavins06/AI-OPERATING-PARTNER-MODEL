#!/usr/bin/env python
"""Score AI-agent readiness from a Step 16 object or key=value scores."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DIMENSIONS = [
    "use_case_framing_readiness",
    "sponsor_behavior_readiness",
    "prior_failure_learning_readiness",
    "business_value",
    "workflow_clarity",
    "process_documentation_readiness",
    "source_access_readiness",
    "data_quality",
    "truth_production_readiness",
    "knowledge_guidance_readiness",
    "measurement_readiness",
    "ai_capability_metrics_readiness",
    "regulated_domain_readiness",
    "solution_shape_readiness",
    "architecture_feasibility",
    "model_orchestration_readiness",
    "risk_control_readiness",
    "security_enablement_readiness",
    "resistance_profile_readiness",
    "recoverable_error_fit_readiness",
    "human_oversight_readiness",
    "change_lifecycle_readiness",
    "adoption_change_readiness",
]

HARD_GATES = [
    "use_case_framing_gate",
    "business_value_gate",
    "sponsor_behavior_gate",
    "workflow_clarity_gate",
    "process_documentation_gate",
    "source_access_gate",
    "data_quality_gate",
    "truth_production_gate",
    "knowledge_guidance_gate",
    "measurement_gate",
    "ai_capability_metrics_gate",
    "regulated_domain_gate",
    "solution_shape_gate",
    "technical_feasibility_gate",
    "model_orchestration_gate",
    "risk_control_gate",
    "security_enablement_gate",
    "adoption_change_gate",
    "resistance_profile_gate",
    "recoverable_error_fit_gate",
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


DEFAULT_RUBRIC_PATH = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "templates"
    / "14-hard-gates-readiness-rubric.yaml"
)

FALLBACK_THRESHOLDS = {
    "ready_for_step17_build_brief_min_pct": 0.85,
    "fix_named_gaps_first_min_pct": 0.70,
    "governance_or_data_or_knowledge_or_technical_or_risk_first_min_pct": 0.52,
}


def load_rubric(path: Path | None) -> dict[str, Any]:
    rubric_path = path or DEFAULT_RUBRIC_PATH
    if not rubric_path.exists():
        return {}
    try:
        import yaml  # type: ignore
    except ImportError:
        return {}
    text = rubric_path.read_text(encoding="utf-8")
    data = yaml.safe_load(text) or {}
    return data if isinstance(data, dict) else {}


def get_thresholds(rubric: dict[str, Any]) -> dict[str, float]:
    block = rubric.get("decision_thresholds")
    if not isinstance(block, dict):
        return dict(FALLBACK_THRESHOLDS)
    out: dict[str, float] = {}
    for key, default in FALLBACK_THRESHOLDS.items():
        value = block.get(key)
        out[key] = float(value) if isinstance(value, (int, float)) else default
    return out


def decision(total: int, scores: dict[str, int], gates: dict[str, str], rubric: dict[str, Any] | None = None) -> str:
    rubric = rubric or {}
    thresholds = get_thresholds(rubric)
    max_total = len(DIMENSIONS) * 5
    ready_threshold = max(1, round(max_total * thresholds["ready_for_step17_build_brief_min_pct"]))
    fix_threshold = max(1, round(max_total * thresholds["fix_named_gaps_first_min_pct"]))
    remediation_threshold = max(
        1,
        round(max_total * thresholds["governance_or_data_or_knowledge_or_technical_or_risk_first_min_pct"]),
    )
    failed = [gate for gate, status in gates.items() if status in {"fail", "blocked"}]
    if failed:
        return "Blocked: route to remediation before any Step 17 build-ready brief. Failed gates: " + ", ".join(failed)
    unknown = [gate for gate, status in gates.items() if status == "unknown"]
    if unknown:
        return "Discovery incomplete: resolve unknown hard gates before treating the score as build-ready."
    if any(scores.get(k, 0) <= 1 for k in DIMENSIONS):
        return "Severe gap: do not automate until critical blockers are fixed."
    if total >= ready_threshold:
        return "Ready for Step 17 build-ready implementation brief, still gated by Step 18 approval."
    if total >= fix_threshold:
        return "Fix named gaps first, then reconsider Step 17 build-ready brief."
    if total >= remediation_threshold:
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
    parser.add_argument("--json", help="JSON or YAML file containing a Step 16 readiness object or flat dimension scores")
    parser.add_argument("--score", action="append", default=[], help="Dimension score as key=value")
    parser.add_argument("--gate", action="append", default=[], help="Hard gate status as gate_id=status")
    parser.add_argument("--rubric", help="Path to hard-gates rubric YAML; defaults to assets/templates/14-hard-gates-readiness-rubric.yaml")
    parser.add_argument("--template", action="store_true", help="Print a JSON template")
    args = parser.parse_args()

    if args.template:
        print_template()
        return 0

    rubric = load_rubric(Path(args.rubric)) if args.rubric else load_rubric(None)
    scores, gates, behavior = load_scores(args.json, args.score)
    gates.update(parse_gate_items(args.gate))
    missing = [k for k in DIMENSIONS if k not in scores]
    if missing:
        raise SystemExit("Missing scores: " + ", ".join(missing))
    for key, value in scores.items():
        if value < 1 or value > 5:
            raise SystemExit(f"{key} must be 1-5")
    total = sum(scores[k] for k in DIMENSIONS)
    print(f"Total: {total} / {len(DIMENSIONS) * 5}")
    print(f"Decision: {decision(total, scores, gates, rubric)}")
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

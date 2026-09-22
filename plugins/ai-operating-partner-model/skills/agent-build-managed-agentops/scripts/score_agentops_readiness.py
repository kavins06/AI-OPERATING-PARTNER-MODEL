#!/usr/bin/env python
"""Score a post-18 AgentOps production readiness gate or golden-path packet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_object(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise SystemExit("YAML input requires PyYAML. Use JSON or install PyYAML.") from exc
        data = yaml.safe_load(text) or {}
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise SystemExit("AgentOps readiness input must be an object")
    return data


def find_object(packet: dict[str, Any], object_type: str) -> dict[str, Any]:
    if packet.get("object_type") == object_type:
        return packet
    objects = packet.get("objects", [])
    if isinstance(objects, list):
        for item in objects:
            if isinstance(item, dict) and item.get("object_type") == object_type:
                return item
    return {}


def list_value(data: dict[str, Any], key: str) -> list[Any]:
    value = data.get(key, [])
    return value if isinstance(value, list) else []


def score_gate(packet: dict[str, Any]) -> tuple[int, list[str], list[str]]:
    gate = find_object(packet, "production_readiness_gate")
    operating_record = find_object(packet, "agentops_operating_record")
    release_manifest = find_object(packet, "release_version_manifest")
    blockers: list[str] = []
    warnings: list[str] = []
    score = 0

    if not gate:
        return 0, ["Missing production_readiness_gate"], warnings

    domains = list_value(gate, "readiness_domains")
    required_domains = [domain for domain in domains if isinstance(domain, dict) and domain.get("required") is True]
    if required_domains:
        domain_points = 50 / len(required_domains)
        for domain in required_domains:
            status = domain.get("status")
            domain_id = domain.get("domain_id", "unknown_domain")
            if status in {"passed", "waived"}:
                score += round(domain_points)
            elif status in {"failed", "blocked"}:
                blockers.append(f"Required readiness domain is {status}: {domain_id}")
            else:
                blockers.append(f"Required readiness domain is not complete: {domain_id}")
            if domain.get("open_issues"):
                blockers.append(f"Required readiness domain has open issues: {domain_id}")
            if not domain.get("evidence_refs"):
                warnings.append(f"Required readiness domain lacks evidence refs: {domain_id}")
    else:
        blockers.append("No required readiness domains found")

    production_decision = gate.get("production_decision", {})
    if isinstance(production_decision, dict) and production_decision.get("decision") == "approved":
        score += 10
    else:
        blockers.append("Production decision is not approved")

    signoff = gate.get("gate_signoff", {})
    if isinstance(signoff, dict) and signoff.get("approval_status") in {"approved", "approved_with_conditions"}:
        score += 5
    else:
        blockers.append("Production gate signoff is not approved")

    controls = gate.get("production_controls", {})
    if isinstance(controls, dict):
        for field in [
            "monitoring_cadence",
            "incident_sla",
            "access_review_cadence",
            "eval_regression_cadence",
            "model_or_prompt_change_policy",
        ]:
            if controls.get(field):
                score += 2
            else:
                warnings.append(f"Missing production control: {field}")
        runbooks = controls.get("required_runbooks", [])
        if isinstance(runbooks, list) and {
            "incident-revocation-runbook.md",
            "internal-operator-run-card.md",
        }.issubset(set(runbooks)):
            score += 5
        else:
            blockers.append("Production controls must include incident runbook and internal operator run card")
    else:
        blockers.append("Missing production_controls object")

    production_scope = gate.get("production_scope", {})
    if isinstance(production_scope, dict):
        if "production" in list_value(production_scope, "environments_allowed"):
            score += 3
        else:
            blockers.append("Production scope does not allow the production environment")
        if production_scope.get("behavior_level_authorized"):
            score += 3
        else:
            blockers.append("Production behavior level is not authorized")
        if production_scope.get("scale_limits"):
            score += 2
        else:
            warnings.append("Production scope has no scale limits")
        if production_scope.get("tools_allowed"):
            score += 2
        else:
            warnings.append("Production scope has no tools_allowed list")
    else:
        blockers.append("Missing production_scope object")

    if release_manifest:
        release = release_manifest.get("release", {})
        if isinstance(release, dict) and release.get("environment_target") == "production":
            score += 5
        else:
            blockers.append("Linked release manifest is not targeted to production")
    else:
        blockers.append("Missing linked release_version_manifest")

    if operating_record:
        identity = operating_record.get("agent_identity", {})
        if isinstance(identity, dict) and identity.get("current_environment") == "production":
            score += 3
        else:
            warnings.append("Operating record is not in production environment")
        if operating_record.get("operating_model"):
            score += 2
        else:
            blockers.append("Operating record is missing operating_model")
    else:
        warnings.append("No operating record found; launch handoff may be incomplete")

    return min(score, 100), blockers, warnings


def decision(score: int, blockers: list[str]) -> str:
    if blockers:
        return "Blocked: resolve launch blockers before production approval."
    if score >= 90:
        return "Ready: production launch can be approved if the sponsor accepts residual risk."
    if score >= 75:
        return "Conditional: review warnings and owner coverage before launch."
    return "Hold: readiness evidence is too thin for production launch."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Production readiness gate, AgentOps object, or golden-path packet YAML/JSON")
    args = parser.parse_args()

    packet = read_object(Path(args.path))
    score, blockers, warnings = score_gate(packet)
    print(f"Score: {score} / 100")
    print(f"Decision: {decision(score, blockers)}")
    if blockers:
        print("\nBlockers:")
        for blocker in blockers:
            print(f"- {blocker}")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())

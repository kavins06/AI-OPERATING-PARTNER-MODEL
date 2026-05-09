#!/usr/bin/env python
"""Generate Section 2 support-skill and asset scaffolding from the build spec."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "02-implementation-managed-agentops" / "section2-build-spec.yaml"


def load_spec() -> dict[str, Any]:
    data = yaml.safe_load(SPEC_PATH.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit(f"{SPEC_PATH} must contain a YAML object")
    return data


def rel(path: str) -> Path:
    return ROOT / path


def slug_to_title(value: str) -> str:
    return " ".join(part.capitalize() for part in value.replace("_", "-").split("-"))


def phases_for_skill(spec: dict[str, Any], skill_id: str) -> list[dict[str, Any]]:
    phases = spec.get("phases", [])
    if not isinstance(phases, list):
        return []
    return [phase for phase in phases if isinstance(phase, dict) and phase.get("support_skill") == skill_id]


def md_list(items: list[object], prefix: str = "-") -> str:
    values = [str(item) for item in items if str(item)]
    return "\n".join(f"{prefix} {item}" for item in values) if values else f"{prefix} None specified."


def unique_sorted(values: list[object]) -> list[str]:
    return sorted({str(value) for value in values if str(value)})


def phase_pack_slug(phase: dict[str, Any]) -> str:
    return f"{int(phase['phase_id']):02d}-{phase['phase_key']}"


def phase_detail_block(phase: dict[str, Any]) -> str:
    inputs = md_list([f"`{item}`" for item in phase.get("section1_inputs", [])])
    outputs = md_list([f"`{item}`" for item in phase.get("section2_outputs", [])])
    templates = md_list([f"`{item}`" for item in phase.get("existing_templates", [])])
    failures = md_list(phase.get("failure_modes", []))
    triggers = md_list(phase.get("return_to_method_triggers", []))
    checklist = phase.get("target_checklist", "")
    rubric = phase.get("target_rubric", "")
    validator_group = phase.get("validator_rule_group", "")
    return f"""### Phase {phase['phase_id']}: {phase['name']}

Purpose: Execute `{phase['phase_key']}` without widening the approved Step 17/18 handoff.

Section 1 inputs:

{inputs}

Section 2 outputs:

{outputs}

Templates:

{templates}

Phase assets:

- Checklist: `{checklist}`
- Rubric: `{rubric}`
- Validator rule group: `{validator_group}`

Execution requirements:

- Read the Section 1 to Section 2 handoff map and verify every required source artifact is approved.
- Confirm the current phase owner, approver, evidence references, and unresolved blockers.
- Complete the phase checklist and apply the phase rubric before marking the phase passed.
- Preserve prohibited behaviors, excluded users, excluded sources, access limits, and behavior-level limits.
- Record any missing evidence as a blocker instead of inferring facts.
- Cite the exact Section 1 object IDs, versions, and evidence links used to complete each output field.
- Treat a new source, tool, user group, action type, model/runtime, environment, or workflow boundary as change control.
- Produce an explicit proceed, hold, return-to-method, or stop decision before moving to the next phase.

Failure modes:

{failures}

Return-to-method triggers:

{triggers}
"""


def skill_md(skill: dict[str, Any], phases: list[dict[str, Any]]) -> str:
    skill_id = str(skill["skill_id"])
    display_name = str(skill.get("display_name") or slug_to_title(skill_id))
    description = str(skill.get("short_description") or f"Support Section 2 phases for {display_name}.")
    phase_lines = "\n".join(f"- Phase {phase['phase_id']}: {phase['name']}." for phase in phases)
    input_lines = unique_sorted([item for phase in phases for item in phase.get("section1_inputs", [])])
    output_lines = unique_sorted([item for phase in phases for item in phase.get("section2_outputs", [])])
    input_block = md_list([f"`{item}`" for item in input_lines])
    output_block = md_list([f"`{item}`" for item in output_lines])
    phase_blocks = "\n".join(phase_detail_block(phase) for phase in phases)

    return f"""---
name: {skill_id}
description: "{description} Use after approved Step 18 handoff and separate implementation approval as part of the Section 2 build and Managed AgentOps backbone."
---

# {display_name}

## Boundary

Use this skill only inside Section 2 after Step 18 handoff approval and separate implementation approval. Do not backfill missing Section 1 decisions here.

Stop and return to the `agent-build-managed-agentops` orchestrator when the work requires phases outside this skill's ownership. Stop and return to the Section 1 method owner when the approved handoff is missing, contradicted, or invalidated.

## Required Inputs

Use the Section 1 to Section 2 handoff map before producing outputs:

- `../agent-build-managed-agentops/assets/mappings/section1-to-section2-handoff-map.yaml`

Required Section 1 inputs for the owned phases:

{input_block}

## Owned Phases

{phase_lines}

{phase_blocks}

## Resource Map

- `../agent-build-managed-agentops/assets/schemas/agentops-object-schemas.yaml`
- `assets/phase-packs`
- `../agent-build-managed-agentops/assets/templates`
- `../agent-build-managed-agentops/assets/checklists`
- `../agent-build-managed-agentops/assets/rubrics`
- `../agent-build-managed-agentops/assets/validator-rules`
- `../agent-build-managed-agentops/assets/examples/golden-path-revenue-intake.yaml`

## Workflow

1. Confirm the approved Section 1 source artifacts and evidence references.
2. Confirm the current Section 2 phase boundary and owner.
3. Confirm the Section 2 scope is equal to or narrower than the approved first behavior and lifecycle scope.
4. Complete the phase checklist.
5. Apply the phase rubric.
6. Produce or update the output contracts.
7. Record failure modes, unresolved gaps, and return-to-method triggers.
8. Do not mark the phase passed until required evidence is attached.

## Output Contracts

{output_block}

## Quality Bar

Do not widen approved scope. Do not proceed when owner, evidence, control, approval, or return-to-method requirements are missing. Treat convenience-driven expansion as a defect.
"""


def openai_yaml(skill: dict[str, Any]) -> str:
    skill_id = str(skill["skill_id"])
    display_name = str(skill.get("display_name") or slug_to_title(skill_id))
    short_description = str(skill.get("short_description") or f"Support Section 2 phases for {display_name}.")
    return f"""interface:
  display_name: "{display_name}"
  short_description: "{short_description}"
  default_prompt: "Use ${skill_id} after approved Step 18 handoff and separate implementation approval to complete its owned Section 2 phases using the handoff map, required contracts, checklists, rubrics, and validation rules."
"""


def phase_pack_manifest(skill_id: str, phase: dict[str, Any]) -> str:
    return yaml.safe_dump(
        {
            "phase_pack_id": phase_pack_slug(phase),
            "support_skill": skill_id,
            "phase_id": phase["phase_id"],
            "phase_key": phase["phase_key"],
            "phase_name": phase["name"],
            "status": "active",
            "purpose": "Local ownership manifest for this support skill. Canonical implementation assets remain in agent-build-managed-agentops.",
            "section1_inputs": phase.get("section1_inputs", []),
            "section2_outputs": phase.get("section2_outputs", []),
            "canonical_assets": {
                "templates": phase.get("existing_templates", []),
                "checklist": phase.get("target_checklist"),
                "rubric": phase.get("target_rubric"),
                "validator_rule": f"skills/agent-build-managed-agentops/assets/validator-rules/{phase['phase_key']}.yaml",
                "golden_path_example": phase.get("target_example"),
            },
            "required_exit_evidence": [
                "approved Section 1 source input references",
                "completed canonical template or intentionally blocked output",
                "completed checklist",
                "rubric result",
                "validator rule result",
                "owner decision",
                "return-to-method assessment",
            ],
            "failure_modes": phase.get("failure_modes", []),
            "return_to_method_triggers": phase.get("return_to_method_triggers", []),
            "do_not_duplicate": "Do not fork canonical templates, rubrics, or validator rules here. Update the central asset and regenerate this pack if ownership metadata changes.",
        },
        sort_keys=False,
    )


def phase_pack_playbook(phase: dict[str, Any]) -> str:
    inputs = md_list([f"`{item}`" for item in phase.get("section1_inputs", [])])
    outputs = md_list([f"`{item}`" for item in phase.get("section2_outputs", [])])
    templates = md_list([f"`{item}`" for item in phase.get("existing_templates", [])])
    failures = md_list(phase.get("failure_modes", []))
    triggers = md_list(phase.get("return_to_method_triggers", []))
    return f"""# Phase {phase['phase_id']}: {phase['name']}

Local phase pack for `{phase['phase_key']}`. Use this file from the owning support skill folder; use the referenced central assets as the source of truth for executable templates, rubrics, validator rules, and examples.

## Required Inputs

{inputs}

## Required Outputs

{outputs}

## Canonical Assets

Templates:

{templates}

- Checklist: `{phase.get('target_checklist', '')}`
- Rubric: `{phase.get('target_rubric', '')}`
- Validator rule: `skills/agent-build-managed-agentops/assets/validator-rules/{phase['phase_key']}.yaml`
- Golden-path example: `{phase.get('target_example', '')}`

## Operating Steps

1. Confirm each required Section 1 input is approved, versioned, and cited by object ID.
2. Confirm the phase is still inside the approved Step 17/18 first behavior and lifecycle scope.
3. Complete the canonical template fields that this phase owns.
4. Complete the checklist and attach evidence for every material claim.
5. Apply the rubric and record pass, conditional, blocked, stop, or return-to-method.
6. Run or apply the validator rule group for this phase.
7. Record the downstream fields the next phase must consume.

## Blocking Conditions

- Required source input, approval, owner, evidence reference, or decision forum is missing.
- Scope is wider than the approved handoff and no change review has approved it.
- A required control, trace, eval, rollback, revocation, monitoring, or support path is absent.
- A high-impact, regulated, write, send, export, privileged, or autonomous action appears without explicit approval.
- The phase output cannot be consumed by the next phase without undocumented assumptions.

## Failure Modes

{failures}

## Return-To-Method Triggers

{triggers}

## Exit Evidence

- Source input IDs and evidence references.
- Completed output object IDs or blocked output decision.
- Checklist result.
- Rubric result.
- Validator result.
- Owner signoff or blocker owner.
- Return-to-method assessment.
"""


def phase_pack_index(skill_id: str, phases: list[dict[str, Any]]) -> str:
    rows = []
    for phase in phases:
        slug = phase_pack_slug(phase)
        rows.append(f"| {phase['phase_id']} | {phase['name']} | `phase-packs/{slug}/phase-playbook.md` | `phase-packs/{slug}/asset-manifest.yaml` |")
    table = "\n".join(rows)
    return f"""# {slug_to_title(skill_id)} Phase Packs

These local phase packs make Section 2 support-skill ownership visible inside the skill folder. Canonical templates, checklists, rubrics, validator rules, and examples remain in `../agent-build-managed-agentops/assets`.

| Phase | Name | Playbook | Manifest |
|---:|---|---|---|
{table}
"""


def checklist_stub(phase: dict[str, Any]) -> str:
    inputs = md_list([f"`{item}`" for item in phase.get("section1_inputs", [])])
    outputs = md_list([f"`{item}`" for item in phase.get("section2_outputs", [])])
    templates = md_list([f"`{item}`" for item in phase.get("existing_templates", [])])
    failures = md_list(phase.get("failure_modes", []))
    triggers = md_list(phase.get("return_to_method_triggers", []))
    return f"""# {phase['name']} Checklist

Use this checklist for Section 2 phase {phase['phase_id']}: `{phase['phase_key']}`.

## Inputs

{inputs}

## Templates And Outputs

Templates:

{templates}

Outputs:

{outputs}

## Entry Checks

- Confirm each required Section 1 input is approved, versioned, and cited by object ID.
- Confirm Step 18 handoff and separate implementation approval are still valid for this phase.
- Confirm phase owner, reviewer, approver, evidence location, and decision forum.
- Confirm required inputs are approved, not merely drafted or implied from notes.
- Confirm open blockers, assumptions, dependencies, and decision deadlines are listed.
- Confirm the prior phase exit decision allows this phase to start.

## Scope Checks

- Confirm phase scope is equal to or narrower than the approved Step 17/18 handoff.
- Confirm approved behavior level, users, workflow boundary, sources, tools, and environments.
- Confirm prohibited behaviors, out-of-scope paths, and non-goals remain explicit.
- Confirm no write, send, irreversible, privileged, regulated, or autonomous action appears unless explicitly approved.
- Confirm any new source, tool, user, model/runtime, environment, action class, output type, or workflow step is routed to change control.

## Evidence Checks

- Attach evidence references for every material claim and owner decision.
- Record missing evidence as a blocker; do not fill gaps with implementation assumptions.
- Confirm required controls, monitoring, stop conditions, and rollback or revocation path.
- Confirm unresolved deviations have an owner, target decision date, and interim risk posture.
- Confirm source freshness, truth-production, and access assumptions are still valid.
- Confirm affected downstream objects are listed so later phases can consume the output.

## Phase-Specific Checks

- Complete the primary output fields listed in the template before phase exit.
- Validate every field derived from Section 1 against the handoff map.
- Mark each phase failure mode as mitigated, accepted by owner, blocked, or returned to method.
- Record pass/fail evidence for the phase rubric criteria.
- Capture implementation learnings that change the approved handoff as return-to-method candidates.

## Blocking Conditions

- Required approval, source object, owner, or evidence reference is missing.
- Scope is wider than approved Step 17/18 handoff and no change review has approved it.
- A required control, rollback path, revocation path, or monitoring path is absent.
- A high-impact or regulated action appears without explicit risk/compliance routing.
- The phase output cannot be consumed by the next phase without undocumented assumptions.

## Exit Checks

- Output contracts are updated.
- Rubric criteria are passed, waived by an authorized owner, or marked blocked.
- Required owners have accepted the result.
- Return-to-method triggers have been evaluated.
- Next phase dependencies are explicit.
- Decision is recorded as proceed, hold, return-to-method, or stop.
- Evidence package is complete enough for an independent reviewer to reproduce the decision.

## Failure Modes

{failures}

## Return-To-Method Triggers

{triggers}
"""


def rubric_stub(phase: dict[str, Any]) -> str:
    return yaml.safe_dump(
        {
            "rubric_id": f"{phase['phase_key']}_rubric",
            "phase_id": phase["phase_id"],
            "phase_key": phase["phase_key"],
            "status": "active",
            "scoring": {
                "pass": "All required criteria pass with evidence or authorized waiver.",
                "conditional": "No critical blocker remains, but named follow-up is required before later promotion.",
                "blocked": "Any required criterion fails without authorized waiver.",
            },
            "criteria": [
                {
                    "criterion_id": "source_inputs_confirmed",
                    "required": True,
                    "owner": "",
                    "evidence_required": phase.get("section1_inputs", []),
                    "pass_condition": "All required Section 1 inputs are present, approved, versioned, and cited.",
                },
                {
                    "criterion_id": "scope_preserved",
                    "required": True,
                    "owner": "",
                    "evidence_required": [
                        "implementation_decision_packet.first_build_scope",
                        "managed_lifecycle_object.lifecycle_scope",
                    ],
                    "pass_condition": "Section 2 scope is equal to or narrower than approved Step 17/18 scope.",
                },
                {
                    "criterion_id": "owners_assigned",
                    "required": True,
                    "owner": "",
                    "evidence_required": [
                        "implementation_decision_packet.owner_matrix",
                        "managed_lifecycle_object.owner_model",
                    ],
                    "pass_condition": "Required owners, reviewers, approvers, support owner, and revocation owner are named where applicable.",
                },
                {
                    "criterion_id": "outputs_complete",
                    "required": True,
                    "owner": "",
                    "evidence_required": phase.get("section2_outputs", []),
                    "pass_condition": "Required Section 2 output contracts are complete enough for the next phase.",
                },
                {
                    "criterion_id": "phase_specific_quality_bar_met",
                    "required": True,
                    "owner": "",
                    "evidence_required": [
                        "phase checklist",
                        "phase output template",
                        "phase validator rule group",
                    ],
                    "pass_condition": "Phase-specific checks, blocking conditions, and output contract requirements are satisfied.",
                },
                {
                    "criterion_id": "operational_handoff_ready",
                    "required": True,
                    "owner": "",
                    "evidence_required": [
                        "next phase dependencies",
                        "owner acceptance",
                        "open issue log",
                    ],
                    "pass_condition": "The next owner can act from the output without undocumented assumptions.",
                },
                {
                    "criterion_id": "failure_modes_handled",
                    "required": True,
                    "owner": "",
                    "evidence_required": phase.get("failure_modes", []),
                    "pass_condition": "Known phase failure modes are mitigated, accepted by owner, or blocking.",
                },
                {
                    "criterion_id": "return_to_method_rules_recorded",
                    "required": True,
                    "owner": "",
                    "evidence_required": phase.get("return_to_method_triggers", []),
                    "pass_condition": "Return-to-method triggers are evaluated and documented.",
                },
            ],
            "automatic_blockers": phase.get("failure_modes", []),
            "return_to_method_triggers": phase.get("return_to_method_triggers", []),
        },
        sort_keys=False,
    )


def validator_rule_stub(phase: dict[str, Any]) -> str:
    return yaml.safe_dump(
        {
            "rule_group": phase["validator_rule_group"],
            "phase_id": phase["phase_id"],
            "phase_key": phase["phase_key"],
            "status": "active",
            "required_section1_inputs": phase.get("section1_inputs", []),
            "required_section2_outputs": phase.get("section2_outputs", []),
            "failure_modes": phase.get("failure_modes", []),
            "return_to_method_triggers": phase.get("return_to_method_triggers", []),
            "checks": [
                {
                    "check_id": "required_section1_inputs_present",
                    "severity": "error",
                    "description": "Required Section 1 source artifacts are referenced and approved.",
                },
                {
                    "check_id": "required_section2_outputs_present",
                    "severity": "error",
                    "description": "Required Section 2 output contracts are present or intentionally blocked.",
                },
                {
                    "check_id": "scope_not_widened_without_change_review",
                    "severity": "error",
                    "description": "No users, sources, tools, environments, actions, outputs, or behavior levels exceed the approved handoff without change review.",
                },
                {
                    "check_id": "owners_and_evidence_present",
                    "severity": "error",
                    "description": "Required owners and evidence references are present for phase decisions.",
                },
                {
                    "check_id": "return_to_method_triggers_present",
                    "severity": "warning",
                    "description": "Return-to-method triggers are listed and evaluated.",
                },
                {
                    "check_id": "blocking_conditions_resolved_or_owned",
                    "severity": "error",
                    "description": "Missing approvals, controls, rollback paths, revocation paths, or monitoring paths are resolved or assigned as blockers.",
                },
                {
                    "check_id": "phase_specific_output_complete",
                    "severity": "error",
                    "description": "The phase output contains enough structured detail for the next phase to consume without hidden assumptions.",
                },
                {
                    "check_id": "decision_recorded",
                    "severity": "error",
                    "description": "The phase records a proceed, hold, return-to-method, or stop decision with owner and evidence.",
                },
            ],
        },
        sort_keys=False,
    )


def example_stub(phase: dict[str, Any]) -> str:
    return yaml.safe_dump(
        {
            "example_id": f"golden_path_phase_{phase['phase_id']:02d}_{phase['phase_key']}",
            "phase_id": phase["phase_id"],
            "phase_key": phase["phase_key"],
            "phase_name": phase["name"],
            "source_packet": "skills/agent-build-managed-agentops/assets/examples/golden-path-revenue-intake.yaml",
            "status": "generated_phase_example_index",
            "purpose": "Phase-level golden-path example index. Use the source packet for the complete filled objects.",
            "section1_inputs_used": phase.get("section1_inputs", []),
            "section2_outputs_demonstrated": phase.get("section2_outputs", []),
            "expected_templates": phase.get("existing_templates", []),
            "evidence_expectations": [
                "Cite the approved Step 17/18 source artifacts.",
                "Show the Section 2 output object IDs produced or updated for this phase.",
                "Record blockers instead of filling missing facts.",
                "Evaluate return-to-method triggers before phase exit.",
                "Show the decision owner and decision status for phase exit.",
                "Show downstream fields that the next phase consumes.",
            ],
            "minimum_completed_sections": [
                "source_inputs",
                "owners or responsible parties",
                "scope or gate boundary",
                "criteria or controls",
                "evidence_refs",
                "decision or signoff",
            ],
            "failure_modes_to_test": phase.get("failure_modes", []),
            "return_to_method_triggers_to_test": phase.get("return_to_method_triggers", []),
        },
        sort_keys=False,
    )


def write_file(path: Path, content: str, apply: bool, force: bool) -> str:
    if path.exists() and not force:
        return f"skip existing {path.relative_to(ROOT)}"
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"wrote {path.relative_to(ROOT)}"
    return f"would write {path.relative_to(ROOT)}"


def generate(spec: dict[str, Any], apply: bool, force: bool, include_active: bool) -> list[str]:
    actions: list[str] = []
    skills = spec.get("support_skills", [])
    if not isinstance(skills, list):
        raise SystemExit("support_skills must be a list")

    for skill in skills:
        if not isinstance(skill, dict) or not skill.get("skill_id"):
            continue
        if skill.get("status") == "active" and not include_active:
            continue
        skill_id = str(skill["skill_id"])
        owned_phases = phases_for_skill(spec, skill_id)
        skill_dir = ROOT / "skills" / skill_id
        actions.append(write_file(skill_dir / "SKILL.md", skill_md(skill, owned_phases), apply, force))
        actions.append(write_file(skill_dir / "agents" / "openai.yaml", openai_yaml(skill), apply, force))
        actions.append(write_file(skill_dir / "assets" / "PHASE_PACK_INDEX.md", phase_pack_index(skill_id, owned_phases), apply, force))
        for phase in owned_phases:
            pack_dir = skill_dir / "assets" / "phase-packs" / phase_pack_slug(phase)
            actions.append(write_file(pack_dir / "asset-manifest.yaml", phase_pack_manifest(skill_id, phase), apply, force))
            actions.append(write_file(pack_dir / "phase-playbook.md", phase_pack_playbook(phase), apply, force))

    for phase in spec.get("phases", []):
        if not isinstance(phase, dict):
            continue
        checklist = phase.get("target_checklist")
        rubric = phase.get("target_rubric")
        example = phase.get("target_example")
        phase_key = phase.get("phase_key")
        if isinstance(checklist, str):
            actions.append(write_file(rel(checklist), checklist_stub(phase), apply, force))
        if isinstance(rubric, str):
            actions.append(write_file(rel(rubric), rubric_stub(phase), apply, force))
        if isinstance(example, str):
            actions.append(write_file(rel(example), example_stub(phase), apply, force))
        if isinstance(phase_key, str):
            validator_path = (
                ROOT
                / "skills"
                / "agent-build-managed-agentops"
                / "assets"
                / "validator-rules"
                / f"{phase_key}.yaml"
            )
            actions.append(write_file(validator_path, validator_rule_stub(phase), apply, force))

    return actions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write files. Default is dry-run.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    parser.add_argument("--include-active", action="store_true", help="Also generate scaffolds for active support skills.")
    args = parser.parse_args()

    spec = load_spec()
    actions = generate(spec, apply=args.apply, force=args.force, include_active=args.include_active)
    mode = "apply" if args.apply else "dry-run"
    print(f"Section 2 backbone generator complete ({mode}).")
    for action in actions:
        print(f"- {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

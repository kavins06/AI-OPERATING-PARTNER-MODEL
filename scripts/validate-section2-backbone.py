#!/usr/bin/env python
"""Validate the Section 2 automation spec and generated backbone coverage."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "02-implementation-managed-agentops" / "section2-build-spec.yaml"
MANIFEST_PATH = ROOT / "skill-manifest.json"

REQUIRED_PHASE_KEYS = {
    "phase_id",
    "phase_key",
    "name",
    "support_skill",
    "section1_inputs",
    "section2_outputs",
    "existing_templates",
    "target_checklist",
    "target_rubric",
    "target_example",
    "validator_rule_group",
    "failure_modes",
    "return_to_method_triggers",
}

REQUIRED_SKILL_SECTIONS = [
    "Boundary",
    "Required Inputs",
    "Owned Phases",
    "Resource Map",
    "Workflow",
    "Output Contracts",
    "Quality Bar",
]


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a YAML object")
    return data


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object")
    return data


def rel(path: str) -> Path:
    return ROOT / path


def validate_spec_shape(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if spec.get("spec_id") != "section2_build_spec":
        errors.append("section2-build-spec.yaml spec_id must be 'section2_build_spec'.")

    phases = spec.get("phases")
    if not isinstance(phases, list):
        return errors + ["section2-build-spec.yaml must include phases list."]
    if len(phases) != 15:
        errors.append(f"Section 2 spec must define 15 phases; found {len(phases)}.")

    seen_ids: set[int] = set()
    seen_keys: set[str] = set()
    for phase in phases:
        if not isinstance(phase, dict):
            errors.append("Each phase must be a YAML object.")
            continue
        missing = sorted(REQUIRED_PHASE_KEYS - set(phase))
        if missing:
            errors.append(f"Phase {phase.get('phase_id', '<unknown>')} missing keys: {', '.join(missing)}")
        phase_id = phase.get("phase_id")
        if not isinstance(phase_id, int):
            errors.append(f"Phase {phase.get('name', '<unknown>')} phase_id must be an integer.")
        elif phase_id in seen_ids:
            errors.append(f"Duplicate phase_id: {phase_id}")
        else:
            seen_ids.add(phase_id)
        phase_key = phase.get("phase_key")
        if isinstance(phase_key, str):
            if phase_key in seen_keys:
                errors.append(f"Duplicate phase_key: {phase_key}")
            seen_keys.add(phase_key)
        if not phase.get("section1_inputs"):
            errors.append(f"Phase {phase_id} has no Section 1 inputs.")
        if not phase.get("section2_outputs"):
            errors.append(f"Phase {phase_id} has no Section 2 outputs.")
        if not phase.get("failure_modes"):
            errors.append(f"Phase {phase_id} has no failure modes.")
        if not phase.get("return_to_method_triggers"):
            errors.append(f"Phase {phase_id} has no return-to-method triggers.")

    expected_ids = set(range(1, 16))
    missing_ids = expected_ids - seen_ids
    extra_ids = seen_ids - expected_ids
    if missing_ids:
        errors.append("Missing phase IDs: " + ", ".join(str(x) for x in sorted(missing_ids)))
    if extra_ids:
        errors.append("Unexpected phase IDs: " + ", ".join(str(x) for x in sorted(extra_ids)))
    return errors


def validate_shared_assets(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    shared = spec.get("shared_assets", {})
    if not isinstance(shared, dict):
        return ["shared_assets must be a YAML object."]
    for key, path in shared.items():
        if not isinstance(path, str):
            errors.append(f"shared_assets.{key} must be a path string.")
            continue
        if not rel(path).exists():
            errors.append(f"Missing shared asset {key}: {path}")
    return errors


def support_skill_map(spec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = spec.get("support_skills", [])
    out: dict[str, dict[str, Any]] = {}
    if isinstance(rows, list):
        for row in rows:
            if isinstance(row, dict) and isinstance(row.get("skill_id"), str):
                out[str(row["skill_id"])] = row
    return out


def validate_support_skills(spec: dict[str, Any], strict: bool) -> list[str]:
    errors: list[str] = []
    skills = support_skill_map(spec)
    if not skills:
        return ["support_skills must list Section 2 support skills."]

    for skill_id, row in skills.items():
        status = row.get("status")
        should_exist = status == "active" or strict
        skill_dir = ROOT / "skills" / skill_id
        if should_exist and not skill_dir.exists():
            errors.append(f"Missing support skill: {skill_id}")
            continue
        if should_exist:
            skill_md = skill_dir / "SKILL.md"
            openai_yaml = skill_dir / "agents" / "openai.yaml"
            if not skill_md.exists():
                errors.append(f"Missing SKILL.md for support skill: {skill_id}")
            if not openai_yaml.exists():
                errors.append(f"Missing agents/openai.yaml for support skill: {skill_id}")
    return errors


def phase_pack_slug(phase: dict[str, Any]) -> str:
    return f"{int(phase['phase_id']):02d}-{phase['phase_key']}"


def validate_templates_and_target_assets(spec: dict[str, Any], strict: bool) -> list[str]:
    errors: list[str] = []
    phases = spec.get("phases", [])
    if not isinstance(phases, list):
        return errors
    for phase in phases:
        if not isinstance(phase, dict):
            continue
        phase_id = phase.get("phase_id", "<unknown>")
        for template in phase.get("existing_templates", []):
            if not isinstance(template, str):
                errors.append(f"Phase {phase_id} existing_templates values must be strings.")
            elif not rel(template).exists():
                errors.append(f"Phase {phase_id} missing existing template: {template}")
        if strict:
            for key in ["target_checklist", "target_rubric", "target_example"]:
                value = phase.get(key)
                if not isinstance(value, str) or not value:
                    errors.append(f"Phase {phase_id} missing {key}.")
                elif not rel(value).exists():
                    errors.append(f"Phase {phase_id} strict mode missing {key}: {value}")
            validator_path = (
                ROOT
                / "skills"
                / "agent-build-managed-agentops"
                / "assets"
                / "validator-rules"
                / f"{phase.get('phase_key')}.yaml"
            )
            if not validator_path.exists():
                errors.append(f"Phase {phase_id} strict mode missing validator rule stub: {validator_path.relative_to(ROOT)}")
    return errors


def validate_manifest(spec: dict[str, Any], strict: bool) -> list[str]:
    if not MANIFEST_PATH.exists():
        return ["Missing skill-manifest.json"]
    manifest = load_json(MANIFEST_PATH)
    sections = manifest.get("sections", [])
    section2 = None
    if isinstance(sections, list):
        for section in sections:
            if isinstance(section, dict) and section.get("id") == "02-implementation-managed-agentops":
                section2 = section
                break
    if not isinstance(section2, dict):
        return ["skill-manifest.json missing Section 2 entry."]

    errors: list[str] = []
    if section2.get("build_spec") not in {None, "02-implementation-managed-agentops/section2-build-spec.yaml"}:
        errors.append("Section 2 manifest build_spec points to an unexpected path.")

    if strict:
        manifest_skills = set(manifest.get("skills", [])) if isinstance(manifest.get("skills"), list) else set()
        section_support = (
            set(section2.get("supporting_skills", []))
            if isinstance(section2.get("supporting_skills"), list)
            else set()
        )
        for skill_id in support_skill_map(spec):
            if skill_id not in manifest_skills:
                errors.append(f"Strict mode: skill-manifest.json skills missing {skill_id}")
            if skill_id not in section_support:
                errors.append(f"Strict mode: Section 2 supporting_skills missing {skill_id}")
    return errors


def validate_skill_section_requirements(spec: dict[str, Any], strict: bool) -> list[str]:
    if not strict:
        return []
    errors: list[str] = []
    required_sections = (
        spec.get("generation_rules", {})
        .get("skill_scaffold", {})
        .get("required_sections", REQUIRED_SKILL_SECTIONS)
    )
    if not isinstance(required_sections, list):
        required_sections = REQUIRED_SKILL_SECTIONS
    for skill_id in support_skill_map(spec):
        skill_md = ROOT / "skills" / skill_id / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8")
        for section in required_sections:
            if f"## {section}" not in text:
                errors.append(f"Strict mode: {skill_id}/SKILL.md missing section: {section}")
    return errors


def validate_asset_depth(spec: dict[str, Any], strict: bool) -> list[str]:
    if not strict:
        return []

    requirements = spec.get("implementation_grade_requirements", {})
    if not isinstance(requirements, dict):
        return ["Strict mode: implementation_grade_requirements must be defined."]

    checklist_sections = requirements.get("required_for_each_checklist", [])
    if not isinstance(checklist_sections, list):
        checklist_sections = []
    min_criteria = (
        requirements.get("required_for_each_rubric", {}).get("minimum_criteria", 8)
        if isinstance(requirements.get("required_for_each_rubric"), dict)
        else 8
    )
    min_checks = (
        requirements.get("required_for_each_validator_rule_group", {}).get("minimum_checks", 8)
        if isinstance(requirements.get("required_for_each_validator_rule_group"), dict)
        else 8
    )
    required_example_fields = requirements.get("required_for_each_phase_example", [])
    if not isinstance(required_example_fields, list):
        required_example_fields = []

    errors: list[str] = []
    phases = spec.get("phases", [])
    if not isinstance(phases, list):
        return errors

    for phase in phases:
        if not isinstance(phase, dict):
            continue
        phase_id = phase.get("phase_id", "<unknown>")
        phase_key = phase.get("phase_key")

        checklist_path = rel(str(phase.get("target_checklist", "")))
        if checklist_path.exists():
            checklist_text = checklist_path.read_text(encoding="utf-8")
            for section in checklist_sections:
                heading = {
                    "entry checks": "## Entry Checks",
                    "scope checks": "## Scope Checks",
                    "evidence checks": "## Evidence Checks",
                    "phase-specific checks": "## Phase-Specific Checks",
                    "blocking conditions": "## Blocking Conditions",
                    "exit checks": "## Exit Checks",
                    "failure modes": "## Failure Modes",
                    "return-to-method triggers": "## Return-To-Method Triggers",
                }.get(str(section), f"## {section}")
                if heading not in checklist_text:
                    errors.append(f"Strict mode: Phase {phase_id} checklist missing {heading}")

        rubric_path = rel(str(phase.get("target_rubric", "")))
        if rubric_path.exists():
            rubric = load_yaml(rubric_path)
            criteria = rubric.get("criteria") if isinstance(rubric, dict) else None
            if not isinstance(criteria, list) or len(criteria) < int(min_criteria):
                errors.append(f"Strict mode: Phase {phase_id} rubric must include at least {min_criteria} criteria.")

        validator_path = (
            ROOT
            / "skills"
            / "agent-build-managed-agentops"
            / "assets"
            / "validator-rules"
            / f"{phase_key}.yaml"
        )
        if validator_path.exists():
            rule = load_yaml(validator_path)
            checks = rule.get("checks") if isinstance(rule, dict) else None
            if not isinstance(checks, list) or len(checks) < int(min_checks):
                errors.append(f"Strict mode: Phase {phase_id} validator rule must include at least {min_checks} checks.")

        example_path = rel(str(phase.get("target_example", "")))
        if example_path.exists():
            example = load_yaml(example_path)
            if isinstance(example, dict):
                for field in required_example_fields:
                    if field not in example:
                        errors.append(f"Strict mode: Phase {phase_id} example missing field: {field}")

    return errors


def validate_support_skill_phase_packs(spec: dict[str, Any], strict: bool) -> list[str]:
    if not strict:
        return []

    errors: list[str] = []
    phases = spec.get("phases", [])
    if not isinstance(phases, list):
        return errors

    for skill_id in support_skill_map(spec):
        skill_dir = ROOT / "skills" / skill_id
        index_path = skill_dir / "assets" / "PHASE_PACK_INDEX.md"
        if not index_path.exists():
            errors.append(f"Strict mode: {skill_id} missing local phase pack index.")

    for phase in phases:
        if not isinstance(phase, dict):
            continue
        phase_id = phase.get("phase_id", "<unknown>")
        skill_id = phase.get("support_skill")
        phase_key = phase.get("phase_key")
        if not isinstance(skill_id, str) or not isinstance(phase_key, str):
            continue
        pack_dir = ROOT / "skills" / skill_id / "assets" / "phase-packs" / phase_pack_slug(phase)
        manifest_path = pack_dir / "asset-manifest.yaml"
        playbook_path = pack_dir / "phase-playbook.md"
        if not manifest_path.exists():
            errors.append(f"Strict mode: Phase {phase_id} missing local asset-manifest.yaml in {pack_dir.relative_to(ROOT)}")
        else:
            manifest = load_yaml(manifest_path)
            if manifest.get("support_skill") != skill_id:
                errors.append(f"Strict mode: Phase {phase_id} local manifest support_skill mismatch.")
            if manifest.get("phase_id") != phase_id:
                errors.append(f"Strict mode: Phase {phase_id} local manifest phase_id mismatch.")
            if manifest.get("phase_key") != phase_key:
                errors.append(f"Strict mode: Phase {phase_id} local manifest phase_key mismatch.")
            if manifest.get("section1_inputs") != phase.get("section1_inputs"):
                errors.append(f"Strict mode: Phase {phase_id} local manifest section1_inputs mismatch.")
            if manifest.get("section2_outputs") != phase.get("section2_outputs"):
                errors.append(f"Strict mode: Phase {phase_id} local manifest section2_outputs mismatch.")
            canonical_assets = manifest.get("canonical_assets")
            if not isinstance(canonical_assets, dict):
                errors.append(f"Strict mode: Phase {phase_id} local manifest missing canonical_assets.")
            else:
                for key in ["templates", "checklist", "rubric", "validator_rule", "golden_path_example"]:
                    if not canonical_assets.get(key):
                        errors.append(f"Strict mode: Phase {phase_id} local manifest missing canonical asset: {key}")
        if not playbook_path.exists():
            errors.append(f"Strict mode: Phase {phase_id} missing local phase-playbook.md in {pack_dir.relative_to(ROOT)}")
        else:
            text = playbook_path.read_text(encoding="utf-8")
            for section in [
                "## Required Inputs",
                "## Required Outputs",
                "## Canonical Assets",
                "## Operating Steps",
                "## Blocking Conditions",
                "## Exit Evidence",
            ]:
                if section not in text:
                    errors.append(f"Strict mode: Phase {phase_id} local playbook missing {section}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Validate full target-state Section 2 backbone.")
    args = parser.parse_args()

    if not SPEC_PATH.exists():
        print(f"Missing Section 2 build spec: {SPEC_PATH}")
        return 1

    spec = load_yaml(SPEC_PATH)
    errors: list[str] = []
    errors.extend(validate_spec_shape(spec))
    errors.extend(validate_shared_assets(spec))
    errors.extend(validate_support_skills(spec, strict=args.strict))
    errors.extend(validate_templates_and_target_assets(spec, strict=args.strict))
    errors.extend(validate_manifest(spec, strict=args.strict))
    errors.extend(validate_skill_section_requirements(spec, strict=args.strict))
    errors.extend(validate_asset_depth(spec, strict=args.strict))
    errors.extend(validate_support_skill_phase_packs(spec, strict=args.strict))

    if errors:
        print("Section 2 backbone validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    mode = "strict" if args.strict else "current"
    print(f"Section 2 backbone validation passed ({mode} mode).")
    print(f"Phases checked: {len(spec.get('phases', []))}")
    print(f"Support skills declared: {len(support_skill_map(spec))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

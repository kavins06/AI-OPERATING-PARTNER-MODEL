from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[3]
SKILL_DIR = ROOT / "skills" / "agent-build-managed-agentops"
ASSET_DIR = SKILL_DIR / "assets"
TEMPLATE_DIR = ASSET_DIR / "templates"
SCHEMA_DIR = ASSET_DIR / "schemas"
EXAMPLE_DIR = ASSET_DIR / "examples"
MAPPING_DIR = ASSET_DIR / "mappings"
CHECKLIST_DIR = ASSET_DIR / "checklists"
RUBRIC_DIR = ASSET_DIR / "rubrics"
VALIDATOR_RULE_DIR = ASSET_DIR / "validator-rules"
SECTION2_SPEC_PATH = ROOT / "02-implementation-managed-agentops" / "section2-build-spec.yaml"

SCHEMA_PATH = SCHEMA_DIR / "agentops-object-schemas.yaml"
INDEX_PATH = TEMPLATE_DIR / "TEMPLATE_INDEX.md"
GOLDEN_PATH = EXAMPLE_DIR / "golden-path-revenue-intake.yaml"
HANDOFF_MAP_PATH = MAPPING_DIR / "section1-to-section2-handoff-map.yaml"

REQUIRED_TEMPLATE_FILES = [
    "build-intake-contract.yaml",
    "agent-necessity-kill-test.yaml",
    "agent-build-plan.yaml",
    "agent-architecture-record.yaml",
    "tool-contract-registry.yaml",
    "eval-and-validation-plan.yaml",
    "guardrail-control-matrix.yaml",
    "trace-observability-spec.yaml",
    "environment-progression-gate.yaml",
    "release-version-manifest.yaml",
    "pilot-launch-gate.yaml",
    "production-readiness-gate.yaml",
    "agentops-operating-record.yaml",
    "change-expansion-retirement-review.yaml",
]

REQUIRED_MARKDOWN_TEMPLATES = [
    "incident-revocation-runbook.md",
    "internal-operator-run-card.md",
]

REQUIRED_SCHEMA_DEFS = [
    "agent_build_contract",
    "agent_necessity_kill_test",
    "agent_build_plan",
    "agent_architecture_record",
    "tool_contract_registry",
    "eval_harness_spec",
    "guardrail_control_matrix",
    "trace_observability_spec",
    "environment_progression_gate",
    "release_version_manifest",
    "pilot_launch_gate",
    "production_readiness_gate",
    "agentops_operating_record",
    "change_expansion_retirement_review",
]

TEMPLATE_OBJECT_TYPES = {
    "build-intake-contract.yaml": "agent_build_contract",
    "agent-necessity-kill-test.yaml": "agent_necessity_kill_test",
    "agent-build-plan.yaml": "agent_build_plan",
    "agent-architecture-record.yaml": "agent_architecture_record",
    "tool-contract-registry.yaml": "tool_contract_registry",
    "eval-and-validation-plan.yaml": "eval_harness_spec",
    "guardrail-control-matrix.yaml": "guardrail_control_matrix",
    "trace-observability-spec.yaml": "trace_observability_spec",
    "environment-progression-gate.yaml": "environment_progression_gate",
    "release-version-manifest.yaml": "release_version_manifest",
    "pilot-launch-gate.yaml": "pilot_launch_gate",
    "production-readiness-gate.yaml": "production_readiness_gate",
    "agentops-operating-record.yaml": "agentops_operating_record",
    "change-expansion-retirement-review.yaml": "change_expansion_retirement_review",
}

EXAMPLE_OBJECT_TYPES = {
    "example-agent-build-plan.yaml": "agent_build_plan",
    "example-agentops-operating-record.yaml": "agentops_operating_record",
}

REQUIRED_HANDOFF_ARTIFACTS = {
    "implementation_decision_packet",
    "managed_lifecycle_object",
    "method_to_build_handoff_contract",
    "separate_implementation_approval",
}

REQUIRED_MAPPING_TYPES = {
    "direct_reference",
    "approval_required",
    "normalize_roles",
    "carry_forward_with_scope_lock",
    "derive",
    "derive_gate",
    "carry_forward_and_verify",
}

BASE_REQUIRED_PATHS = [
    "object_type",
    "spec_version",
    "schema_version",
    "object_id",
    "version",
    "status",
]

OBJECT_REQUIRED_PATHS = {
    "agent_build_contract": [
        "source_inputs",
        "authorization.build_authorized",
        "authorization.authorized_scope_summary",
        "owners",
        "build_scope.agent_name",
        "build_scope.business_outcome",
        "build_scope.workflow_boundary",
        "acceptance_contract.required_artifacts",
        "change_control.material_change_definition",
        "change_control.change_review_required",
    ],
    "agent_necessity_kill_test": [
        "source_inputs",
        "decision_summary.requested_agent_outcome",
        "decision_summary.current_status_quo",
        "decision_summary.lowest_risk_sufficient_solution",
        "simpler_alternatives",
        "agent_fit_tests",
        "risk_comparison.net_risk_position",
        "kill_decision.decision",
        "kill_decision.decision_rationale",
    ],
    "agent_build_plan": [
        "source_inputs",
        "delivery_model.build_owner",
        "delivery_model.delivery_lead",
        "delivery_model.implementation_approach",
        "workstreams",
        "milestones",
        "dependencies",
        "definition_of_done",
    ],
    "agent_architecture_record": [
        "source_inputs",
        "architecture_summary.behavior_level",
        "architecture_summary.topology",
        "architecture_summary.operating_environments",
        "components",
        "model_posture",
        "data_and_system_paths",
        "resilience_and_failure_modes",
    ],
    "tool_contract_registry": [
        "source_inputs",
        "registry_policy.default_tool_state",
        "registry_policy.unregistered_tools_allowed",
        "registry_policy.write_actions_require_explicit_contract",
        "tools",
    ],
    "eval_harness_spec": [
        "source_inputs",
        "validation_scope.environments",
        "datasets",
        "eval_suites",
        "promotion_criteria",
    ],
    "guardrail_control_matrix": [
        "source_inputs",
        "control_policy",
        "controls",
        "revocation_controls",
    ],
    "trace_observability_spec": [
        "source_inputs",
        "trace_policy.trace_required_for_all_runs",
        "trace_policy.audit_log_required_for_tool_calls",
        "trace_policy.sensitive_data_redaction_required",
        "event_taxonomy",
        "observability_requirements",
        "metrics",
        "alerts",
    ],
    "environment_progression_gate": [
        "source_inputs",
        "gate_scope.from_environment",
        "gate_scope.to_environment",
        "entry_criteria",
        "promotion_decision.decision",
        "rollback_plan",
    ],
    "release_version_manifest": [
        "release.agent_id",
        "release.release_version",
        "release.release_type",
        "release.environment_target",
        "source_inputs",
        "included_artifacts",
        "compatibility",
        "deployment",
        "rollback",
    ],
    "pilot_launch_gate": [
        "source_inputs",
        "pilot_scope.environments_allowed",
        "launch_criteria",
        "monitoring_during_pilot",
        "pilot_decision.decision",
    ],
    "production_readiness_gate": [
        "source_inputs",
        "production_scope.environments_allowed",
        "production_scope.behavior_level_authorized",
        "readiness_domains",
        "production_controls",
        "production_decision.decision",
    ],
    "agentops_operating_record": [
        "source_inputs",
        "agent_identity.agent_id",
        "agent_identity.agent_name",
        "agent_identity.current_environment",
        "agent_identity.current_status",
        "operating_model",
        "live_scope",
        "operating_metrics",
        "review_log",
        "incidents",
        "operating_decisions",
    ],
    "change_expansion_retirement_review": [
        "source_inputs",
        "review_scope.review_type",
        "review_scope.agent_id",
        "review_scope.summary",
        "change_description",
        "assessment",
        "decision_options",
        "decision",
    ],
}


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def yaml_paths() -> list[Path]:
    paths: list[Path] = []
    for directory in [
        SCHEMA_DIR,
        TEMPLATE_DIR,
        EXAMPLE_DIR,
        MAPPING_DIR,
        RUBRIC_DIR,
        VALIDATOR_RULE_DIR,
    ]:
        if directory.exists():
            paths.extend(directory.rglob("*.yaml"))
            paths.extend(directory.rglob("*.yml"))
    return sorted(set(paths))


def value_at_path(data: object, dotted_path: str) -> tuple[bool, object]:
    current: object = data
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            return False, None
        current = current[part]
    return True, current


def is_empty(value: object) -> bool:
    return value is None or value == "" or value == [] or value == {}


def validate_yaml_parseability() -> list[str]:
    errors: list[str] = []
    for path in yaml_paths():
        try:
            load_yaml(path)
        except Exception as exc:  # noqa: BLE001 - report every invalid YAML file.
            errors.append(f"YAML parse failed: {path}: {exc}")
    return errors


def validate_required_files() -> list[str]:
    errors: list[str] = []
    if not SECTION2_SPEC_PATH.exists():
        errors.append(f"Missing Section 2 build spec: {SECTION2_SPEC_PATH}")
    if not SCHEMA_PATH.exists():
        errors.append(f"Missing AgentOps schema: {SCHEMA_PATH}")
    if not INDEX_PATH.exists():
        errors.append(f"Missing template index: {INDEX_PATH}")
    if not GOLDEN_PATH.exists():
        errors.append(f"Missing golden-path example: {GOLDEN_PATH}")
    if not HANDOFF_MAP_PATH.exists():
        errors.append(f"Missing Section 1 to Section 2 handoff map: {HANDOFF_MAP_PATH}")
    for name in REQUIRED_TEMPLATE_FILES:
        path = TEMPLATE_DIR / name
        if not path.exists():
            errors.append(f"Missing AgentOps template: {path}")
    for name in REQUIRED_MARKDOWN_TEMPLATES:
        path = TEMPLATE_DIR / name
        if not path.exists():
            errors.append(f"Missing AgentOps markdown template: {path}")
    for name in EXAMPLE_OBJECT_TYPES:
        path = EXAMPLE_DIR / name
        if not path.exists():
            errors.append(f"Missing AgentOps example: {path}")
    return errors


def section2_phases() -> list[dict[str, Any]]:
    if not SECTION2_SPEC_PATH.exists():
        return []
    data = load_yaml(SECTION2_SPEC_PATH)
    if not isinstance(data, dict):
        return []
    phases = data.get("phases", [])
    return [phase for phase in phases if isinstance(phase, dict)]


def validate_phase_assets() -> list[str]:
    errors: list[str] = []
    phases = section2_phases()
    if not phases:
        return errors

    checklist_required_sections = [
        "## Entry Checks",
        "## Scope Checks",
        "## Evidence Checks",
        "## Phase-Specific Checks",
        "## Blocking Conditions",
        "## Exit Checks",
        "## Failure Modes",
        "## Return-To-Method Triggers",
    ]

    for phase in phases:
        phase_id = phase.get("phase_id", "<unknown>")
        phase_key = phase.get("phase_key")
        validator_group = phase.get("validator_rule_group")

        checklist_path = ROOT / str(phase.get("target_checklist", ""))
        if checklist_path.exists():
            checklist_text = checklist_path.read_text(encoding="utf-8")
            for section in checklist_required_sections:
                if section not in checklist_text:
                    errors.append(f"Phase {phase_id} checklist missing section: {section}")
            if isinstance(phase_key, str) and phase_key not in checklist_text:
                errors.append(f"Phase {phase_id} checklist does not mention phase key: {phase_key}")
        else:
            errors.append(f"Phase {phase_id} missing checklist: {checklist_path}")

        rubric_path = ROOT / str(phase.get("target_rubric", ""))
        if rubric_path.exists():
            rubric = load_yaml(rubric_path)
            if not isinstance(rubric, dict):
                errors.append(f"Phase {phase_id} rubric must parse to a YAML object.")
            else:
                if rubric.get("phase_id") != phase_id:
                    errors.append(f"Phase {phase_id} rubric phase_id mismatch.")
                if rubric.get("phase_key") != phase_key:
                    errors.append(f"Phase {phase_id} rubric phase_key mismatch.")
                criteria = rubric.get("criteria")
                if not isinstance(criteria, list) or len(criteria) < 8:
                    errors.append(f"Phase {phase_id} rubric must include at least 8 criteria.")
                else:
                    for criterion in criteria:
                        if not isinstance(criterion, dict):
                            errors.append(f"Phase {phase_id} rubric criteria entries must be objects.")
                            continue
                        for key in ["criterion_id", "required", "evidence_required", "pass_condition"]:
                            if key not in criterion:
                                errors.append(f"Phase {phase_id} rubric criterion missing {key}.")
                if not rubric.get("automatic_blockers"):
                    errors.append(f"Phase {phase_id} rubric missing automatic_blockers.")
                if not rubric.get("return_to_method_triggers"):
                    errors.append(f"Phase {phase_id} rubric missing return_to_method_triggers.")
        else:
            errors.append(f"Phase {phase_id} missing rubric: {rubric_path}")

        validator_path = VALIDATOR_RULE_DIR / f"{phase_key}.yaml"
        if validator_path.exists():
            rule = load_yaml(validator_path)
            if not isinstance(rule, dict):
                errors.append(f"Phase {phase_id} validator rule must parse to a YAML object.")
            else:
                if rule.get("rule_group") != validator_group:
                    errors.append(f"Phase {phase_id} validator rule_group mismatch.")
                checks = rule.get("checks")
                if not isinstance(checks, list) or len(checks) < 8:
                    errors.append(f"Phase {phase_id} validator rule must include at least 8 checks.")
                else:
                    for check in checks:
                        if not isinstance(check, dict):
                            errors.append(f"Phase {phase_id} validator checks entries must be objects.")
                            continue
                        if not check.get("check_id") or not check.get("severity") or not check.get("description"):
                            errors.append(f"Phase {phase_id} validator checks require check_id, severity, and description.")
                if rule.get("required_section1_inputs") != phase.get("section1_inputs"):
                    errors.append(f"Phase {phase_id} validator required_section1_inputs mismatch.")
                if rule.get("required_section2_outputs") != phase.get("section2_outputs"):
                    errors.append(f"Phase {phase_id} validator required_section2_outputs mismatch.")
        else:
            errors.append(f"Phase {phase_id} missing validator rule: {validator_path}")

        example_path = ROOT / str(phase.get("target_example", ""))
        if example_path.exists():
            example = load_yaml(example_path)
            if not isinstance(example, dict):
                errors.append(f"Phase {phase_id} golden-path example must parse to a YAML object.")
            else:
                if example.get("phase_id") != phase_id:
                    errors.append(f"Phase {phase_id} golden-path example phase_id mismatch.")
                if example.get("phase_key") != phase_key:
                    errors.append(f"Phase {phase_id} golden-path example phase_key mismatch.")
                for key in [
                    "section1_inputs_used",
                    "section2_outputs_demonstrated",
                    "evidence_expectations",
                    "failure_modes_to_test",
                    "return_to_method_triggers_to_test",
                ]:
                    if not example.get(key):
                        errors.append(f"Phase {phase_id} golden-path example missing {key}.")
                if "minimum_completed_sections" not in example:
                    errors.append(f"Phase {phase_id} golden-path example missing minimum_completed_sections.")
        else:
            errors.append(f"Phase {phase_id} missing golden-path example: {example_path}")

    return errors


def validate_handoff_map() -> list[str]:
    if not HANDOFF_MAP_PATH.exists():
        return []

    data = load_yaml(HANDOFF_MAP_PATH)
    if not isinstance(data, dict):
        return [f"{HANDOFF_MAP_PATH.name} must parse to a YAML object."]

    errors: list[str] = []
    if data.get("map_id") != "section1_to_section2_handoff_map":
        errors.append(f"{HANDOFF_MAP_PATH.name} map_id must be 'section1_to_section2_handoff_map'.")

    source_artifacts = data.get("source_artifacts")
    if not isinstance(source_artifacts, list):
        errors.append(f"{HANDOFF_MAP_PATH.name} must include source_artifacts.")
        source_artifact_names: set[str] = set()
    else:
        source_artifact_names = {
            str(item.get("artifact"))
            for item in source_artifacts
            if isinstance(item, dict) and item.get("artifact")
        }

    missing_handoff = REQUIRED_HANDOFF_ARTIFACTS - source_artifact_names
    for artifact in sorted(missing_handoff):
        errors.append(f"{HANDOFF_MAP_PATH.name} missing required handoff artifact: {artifact}")

    phase_inputs = data.get("section2_phase_inputs")
    if not isinstance(phase_inputs, list):
        errors.append(f"{HANDOFF_MAP_PATH.name} must include section2_phase_inputs.")
    else:
        phases = {
            item.get("phase")
            for item in phase_inputs
            if isinstance(item, dict)
        }
        for phase in range(1, 16):
            if phase not in phases:
                errors.append(f"{HANDOFF_MAP_PATH.name} missing Section 2 phase mapping: {phase}")

    field_mappings = data.get("field_mappings")
    if not isinstance(field_mappings, list):
        errors.append(f"{HANDOFF_MAP_PATH.name} must include field_mappings.")
        field_mappings = []

    mapped_section2_objects: set[str] = set()
    mapping_types: set[str] = set()
    mapping_ids: set[str] = set()
    for row in field_mappings:
        if not isinstance(row, dict):
            errors.append(f"{HANDOFF_MAP_PATH.name} field_mappings entries must be YAML objects.")
            continue
        mapping_id = row.get("mapping_id")
        if not mapping_id:
            errors.append(f"{HANDOFF_MAP_PATH.name} field mapping missing mapping_id.")
        elif str(mapping_id) in mapping_ids:
            errors.append(f"{HANDOFF_MAP_PATH.name} duplicate mapping_id: {mapping_id}")
        else:
            mapping_ids.add(str(mapping_id))

        section2_object = row.get("section2_object")
        if isinstance(section2_object, str):
            mapped_section2_objects.add(section2_object)
        else:
            errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} missing section2_object.")

        mapping_type = row.get("mapping_type")
        if isinstance(mapping_type, str):
            mapping_types.add(mapping_type)
        else:
            errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} missing mapping_type.")

        source_rows = row.get("source_artifacts")
        if not isinstance(source_rows, list) or not source_rows:
            errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} must cite source_artifacts.")
        else:
            cited_section1 = False
            for source in source_rows:
                if not isinstance(source, dict):
                    continue
                artifact = source.get("artifact")
                if artifact in source_artifact_names:
                    cited_section1 = True
            if not cited_section1:
                errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} does not cite a Section 1 source artifact.")

        if not row.get("section2_path"):
            errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} missing section2_path.")
        if not row.get("mapping_rule"):
            errors.append(f"{HANDOFF_MAP_PATH.name} {mapping_id or '<unknown>'} missing mapping_rule.")

    coverage = data.get("coverage_requirements", {})
    required_objects = coverage.get("required_section2_objects") if isinstance(coverage, dict) else None
    required_section2_objects = set(required_objects) if isinstance(required_objects, list) else set(REQUIRED_SCHEMA_DEFS)
    for object_type in sorted(required_section2_objects):
        if object_type not in mapped_section2_objects:
            errors.append(f"{HANDOFF_MAP_PATH.name} missing field mapping for Section 2 object: {object_type}")

    for mapping_type in sorted(REQUIRED_MAPPING_TYPES):
        if mapping_type not in mapping_types:
            errors.append(f"{HANDOFF_MAP_PATH.name} missing required mapping_type: {mapping_type}")

    validation_rules = data.get("validation_rules")
    if not isinstance(validation_rules, list) or not validation_rules:
        errors.append(f"{HANDOFF_MAP_PATH.name} must include validation_rules.")

    return errors


def schema_defs(schema: object) -> dict[str, object]:
    if not isinstance(schema, dict):
        return {}
    defs = schema.get("$defs", {})
    return defs if isinstance(defs, dict) else {}


def validate_schema_defs() -> list[str]:
    if not SCHEMA_PATH.exists():
        return []

    data = load_yaml(SCHEMA_PATH)
    defs = schema_defs(data)
    errors: list[str] = []
    for key in REQUIRED_SCHEMA_DEFS:
        if key not in defs:
            errors.append(f"Missing schema definition: {key}")
    return errors


def validate_object_type(path: Path, expected: str) -> list[str]:
    if not path.exists():
        return []

    data = load_yaml(path)
    if not isinstance(data, dict):
        return [f"{path.name} must parse to a YAML object."]

    actual = data.get("object_type")
    if actual != expected:
        return [f"{path.name} object_type must be {expected!r}; found {actual!r}."]
    return []


def validate_object_required_paths(
    data: dict[str, object],
    expected_type: str,
    context: str,
    require_non_empty_identity: bool,
) -> list[str]:
    errors: list[str] = []
    for path in BASE_REQUIRED_PATHS + OBJECT_REQUIRED_PATHS.get(expected_type, []):
        exists, value = value_at_path(data, path)
        if not exists:
            errors.append(f"{context} is missing required path: {path}")
            continue
        if require_non_empty_identity and path in {"object_id", "spec_version", "version"} and is_empty(value):
            errors.append(f"{context} has empty identity path: {path}")
    return errors


def validate_template_object_types_and_fields() -> list[str]:
    errors: list[str] = []
    for name, expected in TEMPLATE_OBJECT_TYPES.items():
        path = TEMPLATE_DIR / name
        errors.extend(validate_object_type(path, expected))
        if path.exists():
            data = load_yaml(path)
            if isinstance(data, dict):
                errors.extend(validate_object_required_paths(data, expected, name, require_non_empty_identity=True))
    return errors


def validate_examples() -> list[str]:
    errors: list[str] = []
    for name, expected in EXAMPLE_OBJECT_TYPES.items():
        path = EXAMPLE_DIR / name
        errors.extend(validate_object_type(path, expected))
        if path.exists():
            data = load_yaml(path)
            if isinstance(data, dict):
                errors.extend(validate_object_required_paths(data, expected, name, require_non_empty_identity=True))
    errors.extend(validate_golden_path())
    return errors


def validate_template_index() -> list[str]:
    if not INDEX_PATH.exists():
        return []

    text = INDEX_PATH.read_text(encoding="utf-8")
    errors: list[str] = []
    for name in REQUIRED_TEMPLATE_FILES + REQUIRED_MARKDOWN_TEMPLATES:
        if name not in text:
            errors.append(f"Template index does not mention: {name}")
    if SCHEMA_PATH.name not in text and f"../schemas/{SCHEMA_PATH.name}" not in text:
        errors.append(f"Template index does not mention: {SCHEMA_PATH.name}")
    return errors


def objects_by_type(objects: list[object]) -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for item in objects:
        if isinstance(item, dict) and isinstance(item.get("object_type"), str):
            out[str(item["object_type"])] = item
    return out


def validate_golden_path() -> list[str]:
    if not GOLDEN_PATH.exists():
        return []

    packet = load_yaml(GOLDEN_PATH)
    errors: list[str] = []
    if not isinstance(packet, dict):
        return [f"{GOLDEN_PATH.name} must parse to a YAML object."]
    if packet.get("packet_type") != "agentops_golden_path_packet":
        errors.append(f"{GOLDEN_PATH.name} packet_type must be 'agentops_golden_path_packet'.")

    objects = packet.get("objects")
    if not isinstance(objects, list):
        return errors + [f"{GOLDEN_PATH.name} must include an objects list."]

    object_ids: set[str] = set()
    by_type = objects_by_type(objects)
    for required_type in REQUIRED_SCHEMA_DEFS:
        if required_type not in by_type:
            errors.append(f"{GOLDEN_PATH.name} missing golden-path object type: {required_type}")

    for item in objects:
        if not isinstance(item, dict):
            errors.append(f"{GOLDEN_PATH.name} objects entries must be YAML objects.")
            continue
        object_type = item.get("object_type")
        if not isinstance(object_type, str):
            errors.append(f"{GOLDEN_PATH.name} object missing object_type.")
            continue
        object_id = item.get("object_id")
        if isinstance(object_id, str):
            if object_id in object_ids:
                errors.append(f"{GOLDEN_PATH.name} duplicate object_id: {object_id}")
            object_ids.add(object_id)
        errors.extend(
            validate_object_required_paths(
                item,
                object_type,
                f"{GOLDEN_PATH.name}:{object_type}",
                require_non_empty_identity=True,
            )
        )

    packet_build_contract_id = packet.get("build_contract_id")
    build_contract = by_type.get("agent_build_contract", {})
    if build_contract.get("object_id") != packet_build_contract_id:
        errors.append("Golden path packet build_contract_id must match agent_build_contract.object_id.")

    for object_type, item in by_type.items():
        if object_type == "agent_build_contract":
            continue
        source_inputs = item.get("source_inputs")
        if isinstance(source_inputs, dict) and source_inputs.get("build_contract_id") not in {None, packet_build_contract_id}:
            errors.append(f"{object_type}.source_inputs.build_contract_id does not match packet build contract.")

    kill_test = by_type.get("agent_necessity_kill_test", {})
    kill_decision = kill_test.get("kill_decision")
    if isinstance(kill_decision, dict) and kill_decision.get("decision") != "proceed_with_agent_build":
        errors.append("Golden path agent_necessity_kill_test must proceed_with_agent_build.")

    production_gate = by_type.get("production_readiness_gate", {})
    production_decision = production_gate.get("production_decision")
    if isinstance(production_decision, dict) and production_decision.get("decision") != "approved":
        errors.append("Golden path production_readiness_gate must have an approved production_decision.")
    domains = production_gate.get("readiness_domains")
    if isinstance(domains, list):
        for domain in domains:
            if isinstance(domain, dict) and domain.get("required") is True and domain.get("status") not in {"passed", "waived"}:
                errors.append(f"Golden path required readiness domain did not pass: {domain.get('domain_id')}")

    release = by_type.get("release_version_manifest", {})
    release_block = release.get("release")
    if isinstance(release_block, dict):
        if release_block.get("environment_target") != "production":
            errors.append("Golden path release_version_manifest must target production.")
        if release_block.get("agent_id") != packet.get("agent_id"):
            errors.append("Golden path release agent_id must match packet agent_id.")

    operating_record = by_type.get("agentops_operating_record", {})
    agent_identity = operating_record.get("agent_identity")
    if isinstance(agent_identity, dict) and agent_identity.get("agent_id") != packet.get("agent_id"):
        errors.append("Golden path operating record agent_id must match packet agent_id.")

    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_required_files())
    errors.extend(validate_yaml_parseability())
    errors.extend(validate_schema_defs())
    errors.extend(validate_template_object_types_and_fields())
    errors.extend(validate_template_index())
    errors.extend(validate_examples())
    errors.extend(validate_handoff_map())
    errors.extend(validate_phase_assets())

    if errors:
        print("AgentOps contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AgentOps contract validation passed.")
    print(f"YAML files checked: {len(yaml_paths())}")
    print(f"Schema definitions checked: {len(REQUIRED_SCHEMA_DEFS)}")
    print(f"Templates checked: {len(REQUIRED_TEMPLATE_FILES)}")
    print(f"Markdown templates checked: {len(REQUIRED_MARKDOWN_TEMPLATES)}")
    print(f"Examples checked: {len(EXAMPLE_OBJECT_TYPES) + 1}")
    print(f"Phase asset groups checked: {len(section2_phases())}")
    print("Section handoff maps checked: 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

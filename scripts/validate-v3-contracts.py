from __future__ import annotations

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "skills" / "ai-operating-partner-engagement" / "assets" / "templates"
SCHEMA_PATH = ROOT / "skills" / "ai-operating-partner-engagement" / "assets" / "schemas" / "canonical-object-schemas.yaml"
INDEX_PATH = TEMPLATE_DIR / "TEMPLATE_INDEX.md"
PACKET_CONTRACTS_PATH = TEMPLATE_DIR / "15-decision-packet-contracts.yaml"
PACKET_SET_TEMPLATE_PATH = TEMPLATE_DIR / "15-implementation-decision-packet-set.yaml"
LIFECYCLE_CONTRACTS_PATH = TEMPLATE_DIR / "16-lifecycle-variant-contracts.yaml"
LIFECYCLE_SET_TEMPLATE_PATH = TEMPLATE_DIR / "16-lifecycle-set.yaml"
READINESS_RUBRIC_PATH = TEMPLATE_DIR / "14-hard-gates-readiness-rubric.yaml"

REQUIRED_TEMPLATE_FILES = [
    "00-tier-matrix.yaml",
    "03-ai-interviewer-protocol.md",
    "06-blocker-classification-rubric.md",
    "07-baseline-release-contract.yaml",
    "14-hard-gates-readiness-rubric.yaml",
    "15-decision-packet-contracts.yaml",
    "15-implementation-decision-packet-set.yaml",
    "16-lifecycle-variant-contracts.yaml",
    "16-lifecycle-set.yaml",
    "18-v3-to-build-handoff-contract.md",
    "halt-taxonomy.yaml",
    "offline-proof-catalog.yaml",
    "regulated-domain-extension-real-estate.yaml",
    "vertical-extension.schema.yaml",
]

REQUIRED_SCHEMA_DEFS = [
    "candidate_use_case",
    "workflow_intelligence_object",
    "organizational_intelligence_baseline",
    "truth_production_profile",
    "ai_guidance_pack",
    "measurement_intelligence",
    "technical_blueprint",
    "readiness_object",
    "implementation_decision_packet",
    "packet_set",
    "managed_lifecycle_object",
    "lifecycle_set",
]


def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_yaml_files() -> list[str]:
    errors: list[str] = []
    for path in list(TEMPLATE_DIR.glob("*.yaml")) + [SCHEMA_PATH]:
        try:
            load_yaml(path)
        except Exception as exc:  # noqa: BLE001 - validation script should report all parse failures.
            errors.append(f"YAML parse failed: {path}: {exc}")
    return errors


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_TEMPLATE_FILES:
        path = TEMPLATE_DIR / name
        if not path.exists():
            errors.append(f"Missing V3 template: {path}")
    if not SCHEMA_PATH.exists():
        errors.append(f"Missing canonical schema: {SCHEMA_PATH}")
    return errors


def validate_schema_defs() -> list[str]:
    if not SCHEMA_PATH.exists():
        return []
    data = load_yaml(SCHEMA_PATH)
    defs = data.get("$defs", {}) if isinstance(data, dict) else {}
    errors = []
    for key in REQUIRED_SCHEMA_DEFS:
        if key not in defs:
            errors.append(f"Missing schema definition: {key}")
    return errors


def validate_template_shapes() -> list[str]:
    if not SCHEMA_PATH.exists():
        return []

    schema = load_yaml(SCHEMA_PATH)
    defs = schema.get("$defs", {}) if isinstance(schema, dict) else {}
    templates = {
        "packet_set": PACKET_SET_TEMPLATE_PATH,
        "lifecycle_set": LIFECYCLE_SET_TEMPLATE_PATH,
    }

    errors: list[str] = []
    for def_name, path in templates.items():
        if not path.exists() or def_name not in defs:
            continue
        data = load_yaml(path)
        if not isinstance(data, dict):
            errors.append(f"{path.name} must parse to an object.")
            continue
        required = defs[def_name].get("required", [])
        for field in required:
            if field not in data:
                errors.append(f"{path.name} missing required schema field: {field}")
        if data.get("object_type") != def_name:
            errors.append(f"{path.name} object_type must be {def_name!r}.")
    return errors


def validate_contract_sections() -> list[str]:
    errors: list[str] = []

    if PACKET_CONTRACTS_PATH.exists():
        packet_contracts = load_yaml(PACKET_CONTRACTS_PATH)
        packet_set = packet_contracts.get("packet_set") if isinstance(packet_contracts, dict) else None
        if not isinstance(packet_set, dict):
            errors.append("15-decision-packet-contracts.yaml missing packet_set contract.")
        else:
            required_fields = set(packet_set.get("required_fields", []))
            expected_fields = {
                "packet_set_id",
                "workflow_id",
                "packets",
                "cross_packet_relationships",
                "packet_set_validation",
            }
            missing = sorted(expected_fields - required_fields)
            for field in missing:
                errors.append(f"packet_set contract missing required field: {field}")

    if LIFECYCLE_CONTRACTS_PATH.exists():
        lifecycle_contracts = load_yaml(LIFECYCLE_CONTRACTS_PATH)
        lifecycle_set = lifecycle_contracts.get("lifecycle_set") if isinstance(lifecycle_contracts, dict) else None
        if not isinstance(lifecycle_set, dict):
            errors.append("16-lifecycle-variant-contracts.yaml missing lifecycle_set contract.")
        else:
            required_fields = set(lifecycle_set.get("required_fields", []))
            expected_fields = {
                "lifecycle_set_id",
                "workflow_id",
                "linked_packet_set_id",
                "lifecycles",
                "cross_variant_relationships",
                "lifecycle_set_validation",
            }
            missing = sorted(expected_fields - required_fields)
            for field in missing:
                errors.append(f"lifecycle_set contract missing required field: {field}")

    if READINESS_RUBRIC_PATH.exists():
        rubric = load_yaml(READINESS_RUBRIC_PATH)
        if not isinstance(rubric, dict):
            errors.append("14-hard-gates-readiness-rubric.yaml must parse to an object.")
        else:
            for section in ["hard_gates", "override_rules", "decision_thresholds"]:
                if section not in rubric:
                    errors.append(f"Readiness rubric missing section: {section}")
            gate_ids = {
                gate.get("gate_id")
                for gate in rubric.get("hard_gates", [])
                if isinstance(gate, dict)
            }
            for gate_id in ["source_access_gate", "truth_production_gate", "risk_control_gate", "lifecycle_gate"]:
                if gate_id not in gate_ids:
                    errors.append(f"Readiness rubric missing hard gate: {gate_id}")

    return errors


def validate_template_index() -> list[str]:
    if not INDEX_PATH.exists():
        return [f"Missing template index: {INDEX_PATH}"]
    text = INDEX_PATH.read_text(encoding="utf-8")
    errors = []
    for name in REQUIRED_TEMPLATE_FILES:
        if name not in text:
            errors.append(f"Template index does not mention: {name}")
    if "canonical-object-schemas.yaml" not in text:
        errors.append("Template index does not mention canonical-object-schemas.yaml")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_required_files())
    errors.extend(validate_yaml_files())
    errors.extend(validate_schema_defs())
    errors.extend(validate_template_shapes())
    errors.extend(validate_contract_sections())
    errors.extend(validate_template_index())

    if errors:
        print("V3 contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("V3 contract validation passed.")
    print(f"Templates checked: {len(list(TEMPLATE_DIR.glob('*')))}")
    print(f"Schema definitions checked: {len(REQUIRED_SCHEMA_DEFS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

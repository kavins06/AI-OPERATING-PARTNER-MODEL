# Agent Build Managed AgentOps Templates

These templates define the post-18 backbone for turning an approved method handoff into a controlled build, pilot, production release, and ongoing AgentOps record. They are intentionally machine-readable and evidence-linked.

| File | Object Type | Purpose |
|---|---|---|
| `build-intake-contract.yaml` | `agent_build_contract` | Freezes the approved Step 18 handoff, build authorization, owners, constraints, and acceptance boundaries. |
| `agent-necessity-kill-test.yaml` | `agent_necessity_kill_test` | Forces a narrow proof that an agent is still necessary instead of a simpler workflow, report, rule, automation, or human process. |
| `agent-build-plan.yaml` | `agent_build_plan` | Converts the contract into implementation workstreams, milestones, dependencies, and delivery controls. |
| `agent-architecture-record.yaml` | `agent_architecture_record` | Records agent topology, model posture, data paths, integration surfaces, and architectural decisions. |
| `tool-contract-registry.yaml` | `tool_contract_registry` | Defines tool, connector, MCP, API, and workflow action contracts with permissions and failure behavior. |
| `eval-and-validation-plan.yaml` | `eval_harness_spec` | Specifies offline, sandbox, pilot, and regression evals, datasets, thresholds, and signoff criteria. |
| `guardrail-control-matrix.yaml` | `guardrail_control_matrix` | Maps risks to preventive, detective, corrective, and revocation controls. |
| `trace-observability-spec.yaml` | `trace_observability_spec` | Defines run traces, event taxonomy, logs, metrics, audit evidence, retention, and dashboards. |
| `environment-progression-gate.yaml` | `environment_progression_gate` | Controls promotion from offline validation to sandbox, pilot, production, expansion, or rollback. |
| `release-version-manifest.yaml` | `release_version_manifest` | Captures a release version, included artifacts, compatibility, deployment notes, and rollback package. |
| `pilot-launch-gate.yaml` | `pilot_launch_gate` | Confirms a limited pilot is ready with users, controls, support, monitoring, and stop conditions. |
| `production-readiness-gate.yaml` | `production_readiness_gate` | Confirms production readiness across reliability, security, risk, value, support, and owners. |
| `agentops-operating-record.yaml` | `agentops_operating_record` | Maintains the live operating record for deployed or pilot agents, reviews, incidents, drift, value, and change history. |
| `incident-revocation-runbook.md` | n/a | Human-readable runbook for incident triage, pause, revoke, rollback, communication, and recovery. |
| `internal-operator-run-card.md` | n/a | One-page internal operator view for owners, current release, checks, stop conditions, and escalation. |
| `change-expansion-retirement-review.yaml` | `change_expansion_retirement_review` | Governs material changes, scope expansion, remediation, rollback, or retirement decisions. |

Schema definitions live in `../schemas/agentops-object-schemas.yaml`.

Phase support assets live beside these templates:

- `../checklists`: operator checklists with entry checks, scope checks, evidence checks, phase-specific checks, blocking conditions, exit checks, failure modes, and return-to-method triggers.
- `../rubrics`: evidence-based pass/conditional/blocked rubrics for each phase.
- `../validator-rules`: machine-readable rule groups that validators and reviewers can use to catch missing source inputs, widened scope, incomplete outputs, unresolved blockers, and missing decisions.
- `../examples/golden-path`: phase-level examples that point to the complete golden-path packet and show minimum completed sections for each phase.

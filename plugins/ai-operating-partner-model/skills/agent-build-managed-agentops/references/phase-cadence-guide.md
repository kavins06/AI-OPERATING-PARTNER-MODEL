# Post-18 Phase Cadence Guide

Use these defaults unless the implementation approval sets a stricter timebox. Timeboxes are planning constraints, not automatic approvals; each phase still exits only when the required evidence exists.

| Phase | Default Timebox | Review Cadence | Exit Evidence |
|---|---:|---|---|
| 1. Build Conversion Gate | 0.5-1 business day | Single gate review | Approved handoff version, implementation authorization, named owners |
| 2. Agent Necessity Check | 0.5-1 business day | Single decision review | `agent_necessity_kill_test` |
| 3. First Behavior Scope | 0.5-1 business day | Scope lock review | First behavior, non-goals, prohibited behaviors |
| 4. Agent Architecture Spec | 1-3 business days | Architecture review before sandbox build | `agent_architecture_record` |
| 5. Tool/Data/Identity Contracts | 1-3 business days | Security/data review before tool enablement | `tool_contract_registry` |
| 6. Environment And Access Setup | 1-5 business days | Environment promotion review | `environment_progression_gate` |
| 7. Eval And Guardrail Design | 1-3 business days | Quality/control review before prototype evaluation | `eval_harness_spec`, `guardrail_control_matrix` |
| 8. Sandbox Prototype | 3-10 business days | Twice-weekly build review | Passing sandbox eval evidence or return-to-method decision |
| 9. Security And Control Review | 1-3 business days | Security/risk signoff | Control verification and residual-risk decision |
| 10. Controlled Pilot | 5-15 business days | Daily owner check plus weekly sponsor review | `pilot_launch_gate`, pilot review evidence |
| 11. Production Readiness Gate | 1-2 business days | Single launch decision review | `production_readiness_gate` score and signoff |
| 12. Production Release | 0.5-2 business days | Release-day monitoring and next-business-day review | `release_version_manifest`, rollback package |
| 13. Managed AgentOps | Ongoing | Weekly first month, monthly after stabilization | `agentops_operating_record`, internal run card |
| 14. Expansion/Change-Control Gate | 1-5 business days per material change | Per-change approval forum | `change_expansion_retirement_review` |
| 15. Retirement Or Redesign Loop | 1-10 business days depending on shutdown scope | Retirement/redesign decision review | Revocation, archive, redesign, or return-to-method evidence |

Cadence rules:

- Do not compress phases 2, 7, 9, 10, or 11 below the minimum timebox without explicit risk-owner approval.
- If a phase misses its timebox because evidence is unavailable, record the dependency rather than widening scope.
- Move to weekly Managed AgentOps review only after the production release has no open blocker, high-severity incident, unresolved access issue, or failing blocking metric.
- Any expansion in users, sources, tools, write/send authority, behavior level, model class, retrieval corpus, environment, or workflow starts phase 14 before implementation.

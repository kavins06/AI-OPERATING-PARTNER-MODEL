# Engagement Steps

This is the V3 operating sequence for a pre-build AI operating partner engagement. V3 keeps the same Step 0-18 sequence, but hardens it with artifact contracts, schemas, rubrics, release rules, halt taxonomy, packet contracts, lifecycle variants, and handoff rules. The engagement produces structured organizational intelligence, use-case selection, adoption design, and an implementation blueprint. It does not build agents, tools, connectors, MCP servers, live integrations, normalization pipelines, email ingestion, or production automations.

## Primary Umbrellas

Use these umbrellas as the client-facing and operator-facing primary structure. The detailed steps are implementation mechanics under the umbrellas.

1. Frame And Hypothesize: Steps 0-2.
2. Discover Reality: Steps 3-5.
3. Build And Validate The Intelligence Layer: Steps 6-8.
4. Define AI Reasoning Requirements: Steps 9-10.
5. Prove Measurement And Value: Steps 11-12.
6. Shape The Future Solution: Steps 13-15.
7. Decide And Govern: Steps 16-18.

## Reference Platform

Codex is the reference runtime for this skill set. The methodology is platform-agnostic: schemas, contracts, rubrics, and protocols can run on any harness. Install scripts, skill packaging, and inter-skill orchestration assume Codex by default.

## File Mapping

Physical filenames in `assets/templates/` retain V1/V2 numeric prefixes. The V3 step is authoritative; consult this map when a filename's prefix and step number disagree.

| V3 Step | Physical filename(s) |
|---|---|
| Cross-step contracts | `halt-taxonomy.yaml`, `offline-proof-catalog.yaml`, `assets/schemas/canonical-object-schemas.yaml` |
| Step 0 | `00-engagement-tiering.yaml`, `00-tier-matrix.yaml`, `vertical-extension.schema.yaml`, `regulated-domain-extension.yaml`, `regulated-domain-extension-real-estate.yaml` |
| Step 1 | `01-executive-opportunity-terrain.md`, `01-org-structure-capture.csv` |
| Step 2 | `02-opportunity-terrain-synthesis.md`, `02-candidate-use-case-shortlist.yaml`, `02-interview-coverage-matrix.csv` |
| Step 3 | `03-ai-interviewer-protocol.md`, `03-ai-interviewer-system-prompt.md`, `03-role-interview-guide.md`, `03-edge-case-register.csv`, `03-interview-evidence-need-log.csv`, `03-source-access-register.csv` |
| Step 4 | `04-variation-map.yaml` |
| Step 5 | `04-artifact-follow-up-request.md`, `04-artifact-follow-up-request.csv` |
| Step 6 | `05-ai-workflow-spec.yaml` |
| Step 7 | `06-organizational-intelligence-diagnostic.yaml`, `06-blocker-classification-rubric.md` |
| Step 8 | `07-source-inventory.csv`, `07-validation-event.yaml`, `07-organizational-intelligence-baseline.yaml`, `07-baseline-release-contract.yaml`, `07-controlled-validation-call-view.md` |
| Step 9 | `08-knowledge-map.md` |
| Step 10 | `09-ai-guidance-spec.yaml`, `09-ai-guidance-test-cases.yaml`, `09-ai-guidance-skill.md` |
| Step 11 | `10-measurement-intelligence.yaml`, `10-kpi-dictionary.csv` |
| Step 12 | `11-business-value-case.yaml`, `11-portfolio-comparison.yaml` |
| Step 13 | `12-solution-shape.yaml`, `13-adoption-design.yaml` |
| Step 14 | `12-technical-implementation-blueprint.yaml` |
| Step 15 | `13-risk-control-model.yaml`, `13-risk-register.csv` |
| Step 16 | `14-ai-agent-readiness-score.yaml`, `14-hard-gates-readiness-rubric.yaml`, `14-readiness-scorecard.csv` |
| Step 17 | `15-implementation-decision-packet.yaml`, `15-implementation-decision-packet-set.yaml`, `15-decision-packet-contracts.yaml`, `15-build-ready-implementation-brief-view.md` |
| Step 18 | `16-managed-lifecycle-object.yaml`, `16-lifecycle-set.yaml`, `16-lifecycle-variant-contracts.yaml`, `16-managed-lifecycle-sop-view.md`, `18-v3-to-build-handoff-contract.md` |

## V3 Hardening Contracts

V3 adds these operating contracts:

- `00-tier-matrix.yaml`: lite, standard, and deep scope rules, step depth, target durations, and minimum artifacts.
- `vertical-extension.schema.yaml`: reusable schema for vertical/regulatory extensions.
- `regulated-domain-extension-real-estate.yaml`: worked real-estate extension.
- `03-ai-interviewer-protocol.md`: hosting, consent, recording, redaction, correction, intervention, refusal, async, and quality rules.
- `assets/schemas/canonical-object-schemas.yaml`: canonical object schema contract.
- `06-blocker-classification-rubric.md`: fatal/remediation/controls/informational rubric.
- `07-baseline-release-contract.yaml`: audience views, downstream seed payloads, and baseline release gate.
- `09-ai-guidance-test-cases.yaml`: eval methodology, minimum counts, regression suite, and drift requirements.
- `14-hard-gates-readiness-rubric.yaml`: hard gates, automatic fail rules, behavior-level readiness rules, and scoring rubric.
- `halt-taxonomy.yaml`: pause, revise, disqualify, kill, revoke, retire, and revisit semantics.
- `15-decision-packet-contracts.yaml` and `15-implementation-decision-packet-set.yaml`: required sections per Step 17 packet type and the multi-packet set shape.
- `16-lifecycle-variant-contracts.yaml` and `16-lifecycle-set.yaml`: managed agent, remediation, and no-automation lifecycle variants plus the multi-lifecycle set shape.
- `18-v3-to-build-handoff-contract.md`: what transfers after Step 18 and what triggers V3 re-entry.
- `offline-proof-catalog.yaml`: pre-build-safe proof points and result contract.

## Step 0: Engagement Tiering And Vertical Extension

Set the engagement tier, scope depth, timeline, offline proof-point boundary, and vertical/regulatory extension needs before discovery begins. Use the V3 tier matrix to decide lite, standard, or deep, including which steps are full, compressed, conditional, or skipped with rationale.

## Step 1: Executive Opportunity Terrain Mapping

Understand strategy, leverage areas, operating context, trust boundaries, and who can explain the real work. Use triangulated nomination: sponsor names, org-chart sampling, and "who do people call when this breaks?" probes.

## Step 2: Opportunity Terrain Synthesis And Candidate Use-Case Shortlist

Turn the terrain into discovery zones and an explicit candidate use-case shortlist. Each candidate has a hypothesis, target user, workflow boundary, value hypothesis, trust dependencies, adoption dependencies, regulated-domain dependencies, confidence, and disqualification criteria. V3 defines three disqualification event types: `discovery_disqualification` at Step 7, `economic_disqualification` at Step 12, and `readiness_disqualification` at Step 16.

## Step 3: Role-Aware AI-Led Interviews

Capture work episodes, decisions, edge cases, source access intelligence, truth production, approvals, adoption realities, and silent evidence needs. Use the V3 AI interviewer protocol for hosting, consent, recording/transcription, retention, redaction, PII, no-live-upload, no-asserted-facts, correction handling, refusal fallback, async norms, and operating-partner intervention.

## Step 4: Variation Mapping

Use this conditional step when the organization is fragmented, franchised, multi-region, independent-contractor driven, multi-system, multi-portfolio, or otherwise too varied for one canonical workflow. If skipped, record `single_canonical_workflow_asserted` with reasoning and revisit triggers.

## Step 5: Planning-Evidence Follow-Up

Request only minimal, approved, preferably redacted planning evidence tied to specific workflow objects, source conflicts, or truth production chains. Include SLA, escalation path, and acceptable substitutes such as screenshots, walkthroughs, formulas, macro walkthroughs, sample exports, or operating-partner-recreated structure.

## Step 6: AI-Native Workflow Intelligence Object

Produce structured organizational workflow intelligence with roles, actors, hierarchy, steps, decisions, information objects, source access profiles, truth production profiles, variation patterns, adoption signals, regulated-domain signals, evidence, confidence, unknowns, and completeness checks. V3 treats this as a schema-governed object, not an operator-specific note format.

## Step 7: Organizational Intelligence Diagnostic

Attach findings to workflow objects, separate symptoms from root causes, classify blockers as fatal-for-use-case, requires-remediation-before-build, acceptable-with-controls, or informational, and route intervention paths using the V3 blocker classification rubric.

## Step 8: Controlled Validation, Governance Resolution, And Baseline Release

Use controlled views to resolve official sources, de facto trusted sources, truth production chains, owners, access paths, sensitive fields, retention, permitted AI actions, and disputed objects. Material validation changes loop back into Step 6 and Step 7 for object update and diagnostic re-score. Then generate Organizational Intelligence Baseline v1 using the V3 baseline release contract: audience-specific views, excluded content, downstream seed payloads, validation state, and product release gate.

## Step 9: AI Knowledge And Guideline Requirements Map

Identify what knowledge and guidelines the future AI will need, including tacit judgment, macros, manual adjustments, reconciliations, expert-memory rules, adoption knowledge, and regulated-domain knowledge.

## Step 10: AI Guidance Pack

Convert prioritized requirements into a canonical machine-readable guidance spec, readable view, behavioral evals, output-quality evals, regulated-domain evals where applicable, truth-production handling, explicit rules, examples, output contracts, owners, and update cadence. V3 enforces eval methodology, minimum counts, regression-suite versioning, and drift/revalidation rules.

## Step 11: Measurement Intelligence And AI-Capability Metric Design

Classify existing metric trust and truth status, then define future AI success metrics, leading indicators, lagging indicators, override/error/drift signals, adoption metrics, cost metrics, and kill criteria.

## Step 12: Business Value Case And Portfolio Comparison

Model value, AI-side costs, assumptions, confidence, fragile-truth caveats, and compare surviving opportunities so only the right 1-N opportunities advance.

## Step 13: Solution Shape And Adoption Design

Decide build/buy/leverage-vendor, agent topology, model-selection class, UX surface, retrieval/context shape, eval/observability shape, end-user research, incentive alignment, opt-in versus mandate reality, training, rollout, and adoption-failure triggers. V3 treats this as 13a solution shape and 13b adoption design under one step. Step 15 risk findings can force a loop back to Step 13 when controls require a topology, behavior-level, UX, retrieval, or adoption change.

## Step 14: Technical/Vendor Implementation Blueprint

Define the future architecture, integrations, runtime/orchestration, hosting/environment, MCP/tooling, email access, normalization, identity resolution, truth-rule extraction, sandbox/test strategy, credential/secrets approach, audit/logging, blocked paths, and build sequence.

## Step 15: Risk And Control Model

Define privacy, security, output-quality, truth-production, regulatory, tool-permission, approval, logging, monitoring, incident, revocation, and stop-condition controls. Use regulated-domain risk templates where applicable.

## Step 16: AI-Agent Readiness Score

Produce an implementation-grade readiness object for each surviving opportunity, including hard gates, behavior-level readiness, dependencies, blockers, evidence confidence, minimum safe first behavior, prohibited behaviors, and Step 17 path. Use the V3 hard-gate and readiness rubric; hard gates override average scores.

## Step 17: Implementation Decision Packet

Produce the machine-readable recommendation packet: build-ready brief, gap-remediation plan, governance/data readiness plan, knowledge capture plan, technical feasibility plan, risk/control plan, or do-not-automate recommendation. When one workflow needs multiple packet types, produce a packet_set with cross-packet relationships. V3 defines required sections for each packet type, plus shared core sections, confidence statement, conditional-revision triggers, and sponsor/technical/risk/remediation views.

## Step 18: Managed Lifecycle And Adoption-Change Object

Create a machine-readable operating contract for the future capability. V3 separates three lifecycle variants under Step 18: managed agent lifecycle, remediation lifecycle, and no-automation review cadence. When Step 17 produces a packet_set, produce a lifecycle_set with one lifecycle per packet and cross-variant relationships. The Step 18 object must also include the V3-to-build handoff contract, return-to-V3 triggers, and operating partner role after handoff.

## Responsibility Split

- Client owns truth decisions: goals, examples, systems, planning evidence, access constraints, official/de facto source decisions, truth production confirmations, ownership decisions, adoption constraints, regulated-domain confirmations, and approvals.
- AI owns heavy processing: interviewing, extraction, mapping, synthesis, scoring, draft deliverables, cross-checking, and completeness checks.
- You own judgment: engagement tiering, interpretation, trust, prioritization, risk decisions, adoption implications, client relationship, and final recommendations.

Implementation starts only after Step 18 is complete, the decision packet and lifecycle object are approved, the V3-to-build handoff is accepted, and the client starts a separate build phase.

---
name: warehouse-lakehouse-blueprint
description: "Design the Step 14 technical_blueprint for future analytics, dashboards, data products, and AI agents, including warehouse/lakehouse, semantic layer, truth production remediation, document intelligence, retrieval, integration, runtime/orchestration requirements, hosting/environment requirements, MCP/tooling, email scope, normalization, identity resolution, tool contracts, test strategy, credentials/secrets, audit/logging, blocked paths, and future build order."
---

# Warehouse Lakehouse Blueprint

## Core Rule

Design from workload and governance needs. Keep raw data, standardized data, semantic definitions, documents, retrieval, and agent tools logically separated.

Inside the AI operating partner engagement, this skill produces the Step 14 technical/vendor implementation blueprint only. Do not build pipelines, MCPs, connectors, live integrations, email ingestion, service accounts, semantic layers, data warehouses, or production data movement during the engagement.

The blueprint output must conform to the canonical `technical_blueprint` schema in `skills/ai-operating-partner-engagement/assets/schemas/canonical-object-schemas.yaml`, including required fields: `technical_blueprint_id`, `implementation_posture` (technically_feasible | feasible_with_conditions | blocked | not_worth_blueprinting_yet), `systems_and_sources`, `access_options`, `future_component_contracts`, `normalization_requirements`, `truth_production_remediation`, `build_sequence`, and `stop_boundary`. Do not invent alternative output structures.

Use `../ai-operating-partner-engagement/assets/templates/12-technical-implementation-blueprint.yaml` as the canonical Step 14 template.

## Engagement Role

Step 14 consumes the surviving opportunity, Step 13 solution/adoption shape, Step 10 guidance/evals, Step 11 measurement intelligence, Step 12 value case, Step 8 source/truth decisions, and Step 15 risk constraints when already known. It defines future implementation requirements and access request packages for after Step 18 approval. It does not decide to build or provision anything.

Step 14 documents the future technical path for opportunities still alive after Step 12 and shaped in Step 13. Step 13 decides solution shape and adoption design first; Step 14 should not secretly decide build/buy/leverage, topology, model class, or UX surface without tracing to Step 13.

Do not choose vendors, models, hosting platforms, vector databases, or orchestration frameworks by default. Define requirements, acceptable patterns, preferred/fallback/blocked options, and confirmation needs. Select a specific vendor or framework only when the client has a mandated stack or the later implementation phase makes that decision.

Useful references:

- `../../mastery-reference/analytics/artifacts/data_warehouse_lakehouse_blueprint.md`
- `../../mastery-reference/analytics/artifacts/data_architecture_patterns.md`
- `../../mastery-reference/analytics/artifacts/data_warehouse_lakehouse_blueprint.md`
- `../../mastery-reference/analytics/artifacts/cloud_analytics_comparison_notes.md`

## Architecture Layers

Design:

1. Source inventory.
2. Data contracts.
3. Raw landing zone.
4. Standardized zone.
5. Analytical zone.
6. Document intelligence zone.
7. Semantic layer.
8. Dashboard and BI layer.
9. Retrieval and tool layer.
10. Governance and monitoring.

## Step 14 Blueprint Scope

For AI operating partner work, include:

- Implementation posture: technically feasible, feasible with conditions, blocked, or not ready.
- Links to Step 13 solution shape and adoption design.
- Build/buy/leverage-vendor decision trace and vendor-native capability verification needs.
- Systems and sources with business, technical, and vendor owners.
- Truth production profiles, including official source, de facto trusted source, derivation chain, embedded rules, reproducibility, auditability, and fragile truth blockers.
- Access options: API, export, report view, database view, document store, email scope, manual staging, vendor integration, RPA, or other future path.
- Preferred path, fallback path, and blocked paths with reasons.
- Canonical entities and fields.
- Identity-resolution rules for matching records across systems.
- Source-to-canonical mappings.
- Normalization rules, quality checks, owners, blockers, and freshness requirements.
- Truth remediation requirements: macro extraction, formula documentation, semantic normalization, canonical entity design, reconciliation tests, owner assignment, governed replacement path, and shadow artifact retirement.
- Runtime design requirements: minimum runtime pattern, model capability needs, RAG need, orchestration/state needs, human approval gates, retry/idempotency needs, audit trace, and whether multi-agent design is truly required.
- Future tool/MCP/connector specs with input/output contracts, allowed/prohibited actions, permission scope, human review, and logging.
- Hosting/environment requirements: preferred client cloud or environment, identity provider, data residency, VPC/private networking, compute, storage, queues, secrets, observability, security review, preferred/fallback/blocked hosting patterns, and final vendor-decision boundary.
- Document and email scope, including prohibited all-email access and manual-staging alternatives.
- Test and validation plan using redacted examples, synthetic data, sample exports, linked Step 10 eval cases, sandbox needs, success criteria, and failure cases.
- Credential and secrets approach for the future implementation phase.
- Future access request package.
- Build sequence with prerequisites, outputs, and exit criteria.
- Open technical, security, vendor, data-owner, and business decisions.

## Runtime Pattern Selection

Choose the minimum safe runtime pattern:

- Dashboard or reporting fix: when the real need is metric trust, visibility, or reporting, not an agent.
- Simple assistant: when the AI only drafts or summarizes from provided context.
- RAG assistant: when approved documents or knowledge sources are central and retrieval/citation quality can be governed.
- Tool-using agent: when the AI must call scoped tools or APIs to retrieve, compare, calculate, or route.
- Workflow automation with AI: when AI is one component inside a deterministic workflow with human approval.
- Decision-support copilot: when judgment support is needed but final decision stays human.
- Monitoring/exception agent: when the AI watches for exceptions and routes them.
- Multi-agent system: only when separable roles genuinely reduce risk or complexity, such as retrieval, policy checking, drafting, and review.
- Do not automate: when risk, ownership, source access, knowledge, or value is not ready.

Treat multi-agent design as an escalation, not a default. It adds cost, latency, observability burden, and failure modes.

## Hosting Pattern Selection

Define hosting requirements before choosing vendors:

- Where client data already lives.
- Client-supported cloud or mandated stack.
- Identity provider and RBAC model.
- Data residency and retention needs.
- Private network/VPC/internal system connectivity needs.
- Compute pattern: bursty, scheduled, event-driven, long-running, or steady.
- Storage pattern: relational, object, vector, graph, cache, and audit log.
- Queue/workflow needs.
- Secrets management and credential rotation.
- Observability: model calls, tool calls, retrieval traces, cost, latency, alerts.
- Vendor/security review requirements.
- Preferred, fallback, and blocked hosting patterns.

Do not recommend trendy stack choices without a workload and governance reason.

## Pattern Selection

Choose:

- Governed warehouse first: when trusted reporting and KPIs are primary.
- Lakehouse plus document intelligence: when documents, emails, PDFs, or unstructured content are central.
- Streaming/event architecture: when the workflow reacts to live events.
- Hybrid: when structured metrics and unstructured evidence both matter.

## How To Get Inputs

Collect:

- Source inventory from IT/data teams.
- Source access profiles and planning evidence from the operating partner engagement.
- Truth production profiles, macro/formula walkthroughs, reconciliation notes, and manual adjustment evidence from the operating partner engagement.
- Step 11 measurement intelligence, AI-capability metrics, metric trust classifications, KPI definitions, and unresolved metric questions.
- Step 12 business value case, AI-side cost model, portfolio comparison, and recommendation.
- Step 13 solution shape and adoption design.
- Step 10 guidance packs and test/evaluation cases.
- Workflow and decision needs from managers/operators.
- Current reports, dashboards, and extracts from business users.
- Data-quality issues from admins and stewards.
- Shadow reporting, spreadsheet, macro, manual adjustment, person-dependent truth, and reconciliation issues from admins, stewards, and business owners.
- Document and unstructured content examples.
- Privacy/security constraints and access boundaries.
- Refresh/freshness requirements.
- Expected agent/tool behaviors.
- Runtime/orchestration needs implied by behavior, approvals, state, retries, and auditability.
- Hosting/environment constraints from IT, data, security, and client platform standards.
- API/vendor docs, schema/field lists, access matrices, screenshots, and walkthrough notes when approved as planning evidence.

Do not design architecture from a vendor menu. Design it from decisions, sources, quality needs, governance, and workload.

Do not request production credentials, live API tokens, broad system access, all-email access, or bulk unredacted data for blueprinting. Define those as future implementation access requests when required.

Use a controlled technical view for IT/data/security/system owners. Do not hand over the full organizational intelligence object.

## Model Design

For any domain, identify:

- Core entities.
- Identity-resolution rules.
- Fact events.
- Dimensions.
- Documents.
- Metric definitions.
- Access policies.
- Data-quality rules.
- Lineage.
- Truth production chains and embedded rule locations.
- Agent tool boundaries.
- Tool input/output contracts.

Avoid hard-coding one industry model unless the user gives the domain.

## Build Order

Recommend future implementation sequence:

1. Inventory, data dictionary, and truth production profile capture.
2. Core entity reconciliation and truth-rule extraction.
3. Key fact tables or analytical datasets.
4. Semantic metrics with documented formulas, owners, and reconciliation tests.
5. Dashboards.
6. Retrieval over approved documents.
7. Read-only agents.
8. Approval-gated write-back only after truth, controls, and monitoring are proven.

## Output Template

Deliver:

- Technical implementation blueprint.
- Business workloads and value case linkage.
- Source inventory and systems/sources.
- Target architecture and implementation posture.
- Preferred, fallback, and blocked access paths.
- Data zones.
- Entity/fact/dimension sketch.
- Identity-resolution rules.
- Semantic layer needs.
- Document/retrieval design.
- Runtime/orchestration requirements.
- Hosting/environment requirements and preferred/fallback/blocked patterns.
- MCP/tooling and connector contracts.
- Email access scope and prohibited email access.
- Normalization requirements and canonical entity sketch.
- Test and validation plan.
- Credential/secrets approach.
- Future access request package.
- Governance controls.
- Build sequence.
- Risks and open decisions.

## Stop Condition

Stop when a future build team can understand what systems, data, runtime pattern, model capability requirements, RAG/retrieval requirements, orchestration/state requirements, hosting/environment requirements, tools, permissions, identity resolution, normalization, test data, credentials/secrets handling, audit logging, observability, and sequence would be required after Step 18 approval, while also knowing which paths are preferred, fallback, blocked, or deferred to implementation.

## Shared Engagement Resources

For reusable intake forms, interview prompts, output templates, examples, and scoring scripts, use `../ai-operating-partner-engagement`.

# Output Standards

## Engagement Build Boundary

The 16-step engagement produces organizational intelligence and an implementation blueprint. It does not implement agents, MCP servers, connectors, normalization pipelines, ETL/ELT, email ingestion, live integrations, write-back automation, or production tooling.

Allowed during the engagement:

- AI interviews and synthesis.
- Workflow intelligence generation.
- Controlled validation views.
- Planning evidence review.
- Source access profile capture.
- KPI, architecture, normalization, MCP/tooling, risk, zero-trust, readiness, and lifecycle blueprinting.

Prohibited during the engagement:

- Production credentials.
- Employee credentials.
- Broad live system access.
- Live API tokens or service accounts.
- Client MCP or connector builds.
- Normalization pipeline builds.
- Bulk unredacted data movement.
- All-email ingestion.
- Production agents or workflow automation.

## Build-Ready Implementation Packet

A workflow is implementation-ready only when the machine-readable Step 15 packet includes:

- Business outcome.
- Business value case with evidence, assumptions, confidence, and recommendation.
- Validated AI workflow specification.
- Source access profiles for important workflow information objects.
- Truth production profiles for material numbers, statuses, reports, decisions, metrics, and artifacts treated as true.
- Source inventory.
- Governance model.
- AI knowledge and guideline requirements map.
- Tacit rules/examples.
- Measurement intelligence object, KPI definitions, metric trust classifications, and agent-safe metric usage.
- Technical implementation blueprint covering architecture, integration, runtime/orchestration requirements, hosting/environment requirements, MCP/tooling, email-access, normalization, identity resolution, tool contracts, testing, credentials/secrets, audit/logging, blocked paths, and build sequence.
- Future access request package with scope, owner approvals, credential-handling design, test approach, and revocation plan.
- Risk and control model with risk register, data classification, tool-level permissions, output controls, approval gates, logging, monitoring, incident response, revocation, and stop conditions.
- Step 14 readiness object with hard gates, behavior-level readiness, blockers, dependencies, minimum safe first behavior, and Step 15 path.
- Step 16 managed lifecycle object covering launch gates, validation, monitoring, feedback, incidents, revocation, updates, expansion, retirement, and remediation/no-automation cadence where applicable.

## Truth Production Layer

The engagement must not assume that a clean source of truth exists. For any material workflow object, metric, report, final number, status, approval package, board packet, exception decision, or candidate AI input treated as true, capture a `truth_production_profile`.

Each truth production profile must include:

- Official source: what policy, system design, or leadership says should be authoritative.
- De facto trusted source: what people actually use or trust when work must get done.
- Truth production chain: exports, formulas, macros, manual adjustments, reconciliations, expert judgment, approval, and final reporting.
- Embedded rules: system configuration, report logic, spreadsheet formulas/macros, SOPs, expert memory, meeting habits, or unknown locations.
- Owner, steward, and knower: who owns the truth, who maintains it, and who understands how it is produced.
- Truth status: `authoritative`, `conditionally_reliable`, `shadow_derived`, `manually_adjusted`, `person_dependent`, `disputed`, `missing`, `not_reproducible`, or `unknown`.
- Reproducibility and auditability: high, medium, low, or unknown.
- AI-safe usage: allowed uses, prohibited uses, human review conditions, and escalation triggers.
- Required fix: extraction, documentation, ownership, reconciliation, normalization, governed replacement, or do-not-use.

Truth production classification rules:

- `authoritative`: official and de facto source align, owner/steward are known, derivation is documented, quality checks exist, and use is reproducible.
- `conditionally_reliable`: usable only with explicit caveats, timing rules, human review, or source hierarchy.
- `shadow_derived`: de facto truth comes from a tracker, report, spreadsheet, shared-drive file, macro, email thread, or local artifact outside governed systems.
- `manually_adjusted`: material truth depends on undocumented or semi-documented human adjustment.
- `person_dependent`: only a person or small group knows how to produce or interpret the truth.
- `disputed`: official source, de facto source, formula, owner, or decision use conflicts.
- `missing`: no credible source or chain has been identified.
- `not_reproducible`: the output cannot be recreated from known inputs, rules, and evidence.

Fragile truth rule: if a material truth profile is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible, Step 14 must fail or conditionally pass the relevant behavior level unless the proposed AI behavior is limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.

## AI-Native Workflow Specification

Step 5 produces an `organizational_workflow_intelligence` object, not a human workflow report. Human-readable reports are views generated from this object, not the canonical artifact.

The initial spec must include:

- Workflow identity, business purpose, trigger, outcome, validation status, and confidence.
- Lightweight organization context: teams, roles, reporting structure, relevant people, and interview coverage.
- Role involvement and workflow actors with stable IDs.
- Normal-path steps with inputs, outputs, sources, handoffs, decisions, approvals, evidence references, validation status, and confidence.
- Decision points, explicit rules, tacit judgment, confidence signals, escalation triggers, human boundaries, allowed AI support, and forbidden AI behavior.
- Edge cases, broken normal rules, detection methods, handlers, escalation paths, severity, frequency, automation implications, and validation needs.
- Information objects used by workflow steps, decisions, approvals, edge cases, and candidate assists.
- Source access profiles: system/location, module/report/path, lookup keys, required fields, alternate locations, access roles, related sources, failure modes, and validation status.
- Truth production profiles: official source, de facto source, production chain, embedded rules/macros/manual adjustments, owner/knower, reproducibility, auditability, truth status, AI-safe usage, and validation route.
- Sources and systems mentioned, trust signals, known quality issues, sensitivity, likely owners, and validation status.
- Approval gates and sensitive data signals.
- Operating strain and value signals.
- Role variation analysis: shared patterns, variations, conflicts, best-practice candidates, and standardization opportunities.
- Candidate AI assists as hypotheses only.
- Evidence, facts, assumptions, inferences, unknowns, and enrichment routes.
- Step 5 stop status naming what is known, partial, unknown, and which later steps must enrich the object.

Step 5 must not complete:

- Official source authority.
- Final truth authority or fully validated truth production chain.
- Data owner or steward.
- Full data dictionary.
- Metric formulas.
- Data quality rules.
- Retention rules.
- Access matrix.
- Agent permissions.
- Risk scores.
- Zero-trust controls.
- Architecture design.
- Readiness object or score.
- Build recommendation.

Stop Step 5 when the workflow can be represented as a structured graph of known actors, roles, hierarchy, steps, decisions, information objects, source access profiles, truth production profiles, sources, edge cases, approvals, evidence, confidence, and unknowns, with incomplete source/truth/owner/sensitivity/access/permission fields routed to Step 7 and incomplete risk, metric, architecture, and readiness fields routed to later enrichment steps.

## Organizational Intelligence Diagnostic

Step 6 enriches the AI workflow specification with structured diagnostic findings. It should not become a prose report. It must attach findings to specific objects in the workflow spec.

Each finding must include:

- Linked workflow-spec objects: workflow, role, actor, step, decision, source, system, edge case, approval gate, or signal IDs.
- Diagnostic lens: people, process, data, knowledge, governance, systems, incentives, politics, behavior, risk, measurement, or architecture.
- Symptom.
- Likely root cause.
- Evidence references.
- Confidence.
- Implication.
- Severity and recurrence.
- Whether it affects AI fit.
- Whether it blocks automation.
- Intervention route.
- Recommended next step.
- Owner candidate.
- Validation need.

Intervention routes include:

- `controlled_validation_governance_resolution`
- `knowledge_mapping`
- `tacit_knowledge_capture`
- `analytics_maturity_assessment`
- `kpi_design`
- `architecture_blueprint`
- `risk_register`
- `zero_trust_controls`
- `workflow_standardization`
- `training_role_clarity`
- `candidate_ai_assist`
- `do_not_automate_yet`

Scale Step 6 to the engagement:

- Downsized: 5-10 object-linked findings for a narrow workflow.
- Standard: findings across people, process, data, knowledge, governance, systems, risk, and measurement for a major workflow.
- Upscaled: cross-workflow or enterprise pattern detection across multiple discovery zones.

Step 6 must not decide build readiness, assign final risk scores, define official source authority or final truth production authority, design permissions, or finalize architecture. It routes source/truth/owner/sensitivity/access/permission needs to Step 7 controlled validation and governance resolution, and routes risk, architecture, metric, and readiness needs to later steps.

## Controlled Validation and Governance Resolution

Step 7 validates the AI workflow specification and organizational intelligence diagnostic without handing over the full organizational intelligence object. It also completes object-driven governance resolution for the information objects, source access profiles, truth production profiles, sources, systems, sensitive fields, ownership questions, retention constraints, access constraints, and permitted AI actions that are relevant to the workflow.

Step 7 is not another broad interview cycle. Use Step 5 and Step 6 to prefill what is known, then route only unresolved or high-risk objects to the smallest authorized resolver group.

Internal canonical references:

- AI workflow specification.
- Organizational intelligence diagnostic.
- Evidence and validation logs.
- Preliminary source inventory and unresolved governance fields.
- Information object and source access profile register.
- Truth production profile register.

External validation artifacts:

- Role-specific validation views.
- Object-specific governance resolution views.
- Correction prompts.
- Structured validation and governance event.
- Source inventory/governance enrichment output.
- Source access profile corrections and confirmations.
- Truth production profile corrections, confirmations, and unresolved fragile-truth decisions.

The full organizational intelligence object is internal working infrastructure. Share controlled excerpts only with the people qualified to validate them.

Validation views should be role-specific:

- Sponsor/executive: business purpose, decision rights, high-level approval boundaries, major risks, unknowns, enrichment routes.
- Director/manager: escalation paths, approval gates, portfolio/team variation, standardization opportunities, diagnostic findings.
- Operator/front-line: steps, handoffs, trackers/reports, source conflicts, edge cases, lived-work corrections.
- System/data owner: official source, de facto trusted source, truth production chain, reproducibility, auditability, data quality, access/export constraints.
- Risk/legal/compliance: sensitive data signals, external communication risks, approval boundaries, do-not-automate-yet areas.

Validation and governance resolution must produce:

- Views shared and audiences.
- Confirmed objects.
- Corrections.
- Disputed items.
- New unknowns.
- Not-reviewed critical objects.
- Official source and de facto trusted source decisions for relevant workflow objects.
- Truth production chain, embedded rule, macro, manual adjustment, reconciliation, and expert-memory decisions where material.
- Confirmed practical access paths for relevant workflow information objects.
- Lookup keys, required fields, alternate locations, related sources, and access failure modes where needed for AI readiness.
- Owner and steward assignments for relevant sources, systems, definitions, and quality issues.
- Sensitive fields or content classes.
- Retention, export, and handling constraints where relevant.
- Permitted AI actions at discovery level: read, summarize, compare, draft, export, send, write, or prohibited.
- AI-safe truth usage: summarize, compare, flag uncertainty, draft question, escalate, calculate, cite, recommend, decide, or prohibited.
- Remaining unresolved items, limited to decisions that could not be made by the authorized resolver group.

Ask correction and decision questions, not generic approval questions. If too many core objects or truth production profiles are disputed, return to interviews, planning-evidence follow-up, or org-structure clarification before knowledge, risk, or readiness work. Do not create a separate Step 8 governance loop unless a blocker requires a formal data-governance project outside this engagement.

## AI Knowledge And Guideline Requirements Map

Step 8 produces a structured requirements map for AI judgment. It identifies what knowledge and future AI guidelines are required before the workflow can be designed safely. It does not write the final rules, prompts, checklists, or review criteria; those belong to Step 9.

Step 8 is primarily a synthesis step, not another broad discovery cycle. Use prior outputs first:

- AI workflow specification.
- Organizational intelligence diagnostic.
- Edge cases.
- Decisions and approval gates.
- Source access profiles.
- Truth production profiles.
- Planning evidence.
- Validation and governance events.
- Role ownership, escalation paths, and disputed/unknown items.
- Candidate AI assists.

Each knowledge requirement must include:

- Stable knowledge ID.
- Linked workflow, step, decision, edge case, approval gate, information object, source, or candidate AI assist.
- Knowledge or guideline needed.
- Why it is needed.
- Whether it appears tacit, explicit, mixed, or unknown.
- Whether it is embedded in a truth production chain.
- Where it likely lives: policy, SOP, system, document, tracker, spreadsheet, macro, reconciliation, email, meeting habit, expert memory, or role practice.
- Likely expert/owner and why that person or role was inferred.
- Evidence references.
- Confidence.
- Gap or risk if the knowledge is not captured.
- Examples needed: good, bad, and edge case.
- AI relevance: allowed future use and forbidden future use.
- Next route: `tacit_capture`, `policy_review`, `SOP_needed`, `risk_review`, `analytics_definition`, `no_agent_use_yet`, or `targeted_confirmation`.

Reasoning rules:

- A decision implies required decision knowledge.
- An edge case implies exception-handling knowledge.
- An approval gate implies approval criteria and authority knowledge.
- A manual check implies hidden quality or trust knowledge.
- A spreadsheet macro, manual adjustment, or recurring reconciliation implies embedded business rules.
- A person-dependent truth chain implies tacit capture or no-agent-use-yet until captured.
- An escalation path implies likely expertise ownership.
- A repeated correction implies a knowledge or training gap.
- A source conflict implies source-trust guidance.
- A candidate AI assist implies future AI guideline requirements.

Use targeted follow-up only for high-value, high-risk, disputed, or low-confidence items. Do not ask the client to explain everything they know.

## AI Guidance Pack

Step 9 converts prioritized Step 8 requirements into implementation-ready guidance artifacts, but it is still not an implementation step. The primary artifact is a machine-readable YAML or JSON guidance spec. A Markdown skill-style guide, prompt view, tool-policy view, and test/evaluation cases can be generated from that spec later.

The guidance pack must include:

- Stable guidance ID, version, status, workflow ID, and linked Step 8 knowledge requirement IDs.
- Scope: workflow, decision, exception family, future agent behavior, and out-of-scope areas.
- Owners: business owner, expert owner, reviewer, risk/compliance reviewer, and update cadence.
- Purpose and AI use boundary.
- Required inputs and missing-input behavior.
- Source hierarchy: preferred sources, fallback sources, prohibited sources, conflict handling, and source access profile references.
- Truth production handling: allowed truth statuses, fragile-truth behaviors, prohibited uses, required confidence language, and escalation triggers.
- Explicit rules.
- Tacit cues and judgment signals.
- Examples: good, bad, edge, low-confidence, and source-conflict cases.
- Examples: good, bad, edge, low-confidence, source-conflict, and fragile-truth cases.
- Checklists or review criteria.
- Allowed AI behaviors.
- Forbidden AI behaviors.
- Escalation triggers and human approval gates.
- Sensitive-field handling and retention/handling constraints inherited from Step 7.
- Output contract: response format, required fields, evidence/citation fields, confidence, uncertainty language, and human-review flags.
- Test/evaluation cases with expected behavior and pass criteria.
- Validation status, evidence references, unresolved gaps, and implementation notes.

Step 9 should not be only a `SKILL.md`. A `SKILL.md` can be useful as a human-readable view, but the structured guidance spec should remain canonical so future builders can generate prompts, tool policies, product controls, evals, and documentation without reinterpreting a narrative document.

Step 9 must not create a live agent, MCP, connector, normalization pipeline, credential flow, email ingestion, live system integration, or production automation. It defines how the future AI should reason and behave once implementation is separately approved.

## Measurement Intelligence And Analytics Readiness

Step 10 defines the measurement reality a future AI can and cannot rely on. It is not a dashboard-build step. It turns prior discovery into decision-linked metric requirements, trust classifications, KPI definition needs, reporting gaps, and agent-safe metric usage.

Use prior outputs first:

- Executive opportunity terrain and business outcomes.
- AI workflow specification.
- Organizational intelligence diagnostic.
- Controlled validation and governance events.
- Information objects and source access profiles.
- Step 8 knowledge/guideline requirements.
- Step 9 guidance packs.
- Planning evidence such as dashboards, board reports, KPI lists, Excel trackers, budget variance reports, accounting exports, property management reports, invoice aging reports, and data dictionaries.

Who does the work:

- AI does the heavy first pass: extracts metric needs from workflows and decisions, finds candidate sources, detects conflicts, drafts KPI definitions, maps truth production chains, scores analytics maturity, and proposes trust classifications with evidence.
- Operating partner does the judgment work: decides which metrics matter, removes noise, challenges vague KPIs, determines whether gaps are material, and routes unresolved items.
- Client does the truth/authority work: confirms official source, de facto trusted source, truth production chain, formula, grain, owner, steward, freshness, reproducibility, auditability, quality checks, access boundary, and whether AI may use the metric.

Each metric must include:

- Stable metric ID.
- Linked workflow, decision, step, approval gate, information object, source access profile, or candidate AI assist.
- Business question and decision/action supported.
- Formula and grain.
- Official source and de facto trusted source.
- Truth production chain and truth status.
- Operational working source, if different.
- Supporting and fallback sources.
- Owner and steward.
- Refresh cadence and freshness required by the decision.
- Reconciliation status and known timing gaps.
- Manual adjustment status, embedded rule location, reproducibility, auditability, and version/change-control status.
- Quality checks.
- Thresholds, targets, benchmarks, or variance rules.
- Trust status: `trusted`, `conditionally_trusted`, `disputed`, `untrusted`, or `unknown`.
- Trust evidence and confidence.
- Agent-safe usage: calculate, cite, compare, summarize, flag uncertainty, draft question, escalate, or prohibited.
- Human review or escalation triggers.
- Unresolved questions and routing.

Trust classification rules:

- `trusted`: source is authoritative, formula is defined, grain is clear, owner/steward is known, freshness is enough for the decision, quality checks exist, and the metric is actually used for decisions.
- `conditionally_trusted`: usable with caveats such as timing lag, manual refresh, source hierarchy rule, documented manual adjustment, or human review.
- `disputed`: sources, formulas, ownership, or decision usage conflict.
- `untrusted`: no reliable owner, unclear formula, poor quality, stale data, not-reproducible chain, low auditability, or known misuse.
- `unknown`: not enough evidence yet.

Step 10 must not let AI independently declare a metric trusted. AI proposes trust and truth status from evidence; the authorized client owner confirms, corrects, or leaves it unresolved.

Step 10 must not build dashboards, models, pipelines, semantic layers, MCPs, connectors, normalization jobs, live integrations, agents, or production automations. Those needs are routed to Step 12 and later implementation planning.

## Business Value Case

Step 11 is the economic filter. It decides whether an opportunity is valuable enough to carry forward into architecture, risk, readiness, and future implementation planning. It does not decide technical feasibility or authorize build work.

Use prior outputs first:

- Executive opportunity terrain and strategic priorities.
- AI workflow specification and operating strain/value signals.
- Organizational intelligence diagnostic.
- Source access/governance decisions.
- Step 8 knowledge/guideline requirements.
- Step 9 guidance packs.
- Step 10 measurement intelligence and metric trust classifications.
- Truth production profiles and fragile-truth dependencies.
- Planning evidence such as volumes, cycle times, cost ranges, error/rework examples, leakage examples, risk incidents, service feedback, reports, and financial/operational summaries.

Who does the work:

- AI drafts value hypotheses, links them to workflow and measurement evidence, estimates ranges where evidence supports them, identifies assumptions, and flags weak or unmeasurable claims.
- Operating partner judges credibility, priority, strategic fit, and whether the case should move forward.
- Client confirms business reality: volumes, costs, baseline assumptions, acceptable ranges, leadership priorities, and risk tolerance.

Value lenses:

- Internal efficiency: labor, rework, cycle time, leakage, cost.
- Decision quality: speed, consistency, evidence, confidence, fewer missed exceptions.
- Risk reduction: compliance, operational, financial, vendor, reputation, output quality.
- Revenue protection or growth: retention, pricing, collections, conversion, leakage prevention, service expansion.
- Customer, tenant, vendor, or employee experience: responsiveness, accuracy, transparency, fewer handoff failures.
- Reusable data product value: governed dataset, metric, report, insight service, or future tool foundation.

Each value case must include:

- Stable opportunity ID.
- Linked workflow, decision, source, metric, knowledge, and guidance IDs.
- User, decision, and business outcome.
- Value hypotheses by lens.
- Baseline metrics and trust status.
- Truth production status for baseline metrics.
- Conservative, base, and upside estimate where evidence supports ranges.
- Evidence references.
- Assumptions and confidence.
- Dependencies: measurement, truth production, governance, source access, knowledge/guidance, architecture, risk, change management.
- Risks to value capture.
- Client confirmation needs.
- Recommendation: `carry_forward_to_architecture_and_readiness`, `fix_measurement_first`, `fix_truth_production_first`, `fix_governance_or_knowledge_first`, `deprioritize`, or `do_not_pursue`.

Rules:

- Do not use disputed, untrusted, unknown, shadow-derived, manually adjusted, person-dependent, missing, or not-reproducible metrics as reliable baseline evidence unless the value case is explicitly about fixing measurement or truth infrastructure.
- Do not pretend ROI precision when evidence only supports a directional case.
- Do not call an opportunity valuable only because it is automatable.
- Do not carry forward opportunities with no owner, no decision/workflow, no measurable value lever, or no acceptable baseline assumption.
- Step 11 must not build agents, dashboards, pipelines, integrations, MCPs, connectors, normalization jobs, or live automations.

## Opportunity Terrain Synthesis

After executive opportunity terrain mapping, produce a synthesis before starting interviews. It must include:

- Strategic context.
- Operating leverage themes.
- Full opportunity terrain.
- Sequenced discovery tiers.
- Rationale for sequencing.
- Interview plan.
- Preliminary artifact request plan.
- Sponsor confirmations needed.

This artifact is a sequencing memo, not a final diagnosis. It may name candidate AI-agent, analytics, monitoring, knowledge, governance, or workflow-redesign hypotheses, but must not recommend build work until discovery, validation, governance, risk, and readiness scoring are complete.

## Role Interview Discovery

Each interview output should include:

- Interview setup: discovery zone, participant role, why this person was interviewed, role-specific probes, and boundaries.
- Recent concrete work episode.
- Normal path from trigger to outcome.
- Decisions and judgment used.
- Systems and sources.
- Information objects and source access paths.
- Source trust and conflicts.
- Handoffs and approvals.
- Edge case register.
- Silent evidence need log.
- Sensitive data and trust boundaries.
- Value signals.
- Follow-up questions.
- Interview quality score.

Do not ask participants for live uploads, file links, screenshots, or document submissions during interviews. Artifact requests should be consolidated after the interview batch from the silent evidence need log and curated by the operating partner.

After multiple interviews, produce cross-interview triangulation:

- Agreements.
- Conflicts.
- Repeated edge cases.
- Role-specific differences.
- Official/de facto source and truth-status questions.
- Truth production questions: official source, de facto trusted source, derivation chain, manual adjustment, macro logic, owner, reproducibility, and auditability.
- High-risk unknowns.
- Validation needs.

## Evidence Need Consolidation / Planning-Evidence Follow-Up

After the interview batch, consolidate silent evidence needs before asking the client for artifacts. This is an operating partner review step, not an automatic platform request.

The planning-evidence follow-up output must include:

- Data access posture.
- Evidence need review.
- Curated artifact requests.
- Claim, edge case, source conflict, source access path, source access profile, or truth production chain each artifact validates.
- Likely owner.
- Sensitivity and redaction needs.
- Access scope.
- Retention or handling rule.
- Priority and status.
- Requests grouped by owner or team.
- Items not requested because they are duplicate, low priority, too sensitive, or already answered.

Trust rule:

- The 16-step engagement does not require build access or credentials.
- Prefer redacted examples, screenshots, reports, trackers, templates, walkthroughs, sample exports, formulas, macro walkthroughs, reconciliation notes, schema/field lists, API/vendor documentation, access-control screenshots, and data dictionaries.
- Do not request production credentials, broad live system access, write access, all-email ingestion, live MCP/connector access, or bulk unredacted data during the 16-step engagement.
- If implementation will require system access, API access, MCPs, connectors, normalization pipelines, email connectors, broad data movement, or unredacted data, define that as a future access request package in the implementation blueprint.

## Technical Implementation Blueprint

Step 12 produces a technical implementation blueprint, not a build. It decides the future technical path for opportunities that survived the business value case. It does not decide final agent scope, authorize implementation, request credentials, connect to live systems, or prematurely select vendors, foundation models, vector stores, hosting providers, or orchestration frameworks unless the client has a mandated stack.

Use prior outputs first:

- Validated AI workflow specification.
- Source access profiles and source inventory.
- Truth production profiles.
- Governance decisions from Step 7.
- Step 9 guidance packs and test/evaluation cases.
- Step 10 measurement intelligence, metric trust, and unresolved metric questions.
- Fragile truth profiles and unresolved truth production questions.
- Step 11 business value case and recommendation.
- Planning evidence such as API/vendor docs, schema/field lists, report/export samples, access matrices, screenshots, walkthrough notes, architecture notes, data dictionaries, and redacted examples.

Who does the work:

- AI drafts the blueprint from prior organizational intelligence: systems, sources, information objects, access paths, runtime pattern needs, RAG/retrieval needs, hosting/environment constraints, future tool needs, canonical entities, normalization needs, test data needs, and open feasibility questions.
- Operating partner decides how deep the blueprint needs to go, challenges overengineering, aligns build sequence to value and risk, and keeps the work pre-build.
- Client IT/data/security/system owners confirm feasibility: APIs, exports, vendor constraints, access model, hosting constraints, identity provider, network/private access needs, data residency, data quality, credential process, audit/logging, observability, sandbox/test-data options, and blocked paths.
- Business owners confirm that the proposed technical path supports the workflow and value case.

Each blueprint must include:

- Stable blueprint ID, opportunity ID, workflow IDs, and value case ID.
- Implementation posture: `technically_feasible`, `technically_feasible_with_conditions`, `blocked`, or `not_ready_for_blueprint`.
- Systems and sources: business owner, technical owner, vendor owner, current role in workflow, source access profile IDs, truth production profile IDs, data needed, sensitivity, quality issues, truth status, and practical constraints.
- Access options: API, export, report view, database view, document store, email scope, manual staging, vendor integration, RPA, or other future path.
- Preferred path, fallback path, and blocked paths with reasons.
- Feasibility status and who confirmed it.
- License, vendor, security, audit/logging, sandbox, test-data, retention, and data-owner constraints.
- Canonical entities and fields.
- Identity-resolution rules for matching records across systems.
- Source-to-canonical mappings.
- Normalization rules, quality checks, owner, blocker, and data freshness requirement.
- Truth production remediation: macro extraction, formula documentation, rule capture, semantic normalization, canonical entity design, reconciliation tests, owner assignment, governed replacement path, shadow artifact retirement, or do-not-use-for-AI.
- Runtime design requirements: minimum safe runtime pattern, whether RAG is required, retrieval source boundaries, model capability requirements, tool-calling needs, structured output needs, latency/cost/privacy constraints, state/orchestration needs, human approval gates, retry/idempotency needs, audit trace needs, and whether multi-agent design is justified.
- Hosting/environment requirements: client preferred cloud or mandated stack, identity provider, data residency, VPC/private networking, compute pattern, storage needs, queue/workflow needs, secrets manager, observability, audit logging, vendor/security review, and preferred/fallback/blocked hosting patterns.
- Future tool/MCP/connector specs with input contract, output contract, allowed actions, prohibited actions, data touched, permission scope, human review, logging, and build phase.
- Document and email scope, including prohibited all-email access and manual-staging alternatives.
- Test and validation plan: redacted examples, synthetic data, sample exports, linked Step 9 eval cases, sandbox needs, success criteria, and failure cases.
- Credential and secrets approach for future implementation: type, provisioning owner, storage, rotation, revocation, audit, and approval dependencies.
- Future access request package.
- Build sequence: phases, prerequisites, outputs, exit criteria, and do-not-build-yet boundary.
- Open technical, security, vendor, data-owner, and business decisions with owners and blocking status.

Ground-level process:

1. AI pre-fills the blueprint from Steps 5-11.
2. Operating partner reviews and removes overengineering or low-value paths.
3. Controlled technical view is shared with IT/data/security/system owners, not the full organizational intelligence object.
4. Owners confirm feasibility and blocked paths without providing credentials or live access.
5. AI updates preferred path, fallback path, blocked path, future access request package, normalization needs, test-data needs, and build sequence.

It must not include:

- Production credentials.
- Live service accounts.
- Live API tokens.
- Built MCP servers or connectors.
- Built normalization pipelines.
- Built semantic layer or data warehouse.
- Live email ingestion.
- Production ETL/ELT.
- Write-back automation.
- Production agent deployment.

Runtime and hosting rules:

- Define runtime requirements before choosing models, agent frameworks, or multi-agent patterns.
- Define hosting requirements before choosing cloud services, vector stores, databases, queues, or deployment platforms.
- Multi-agent design is an escalation, not a default; require a clear separable-role rationale.
- RAG is required only when approved knowledge sources must be retrieved with governed permissioning, freshness, metadata, and citations.
- If the client has a mandated stack, record it as a constraint. If not, specify preferred, fallback, and blocked patterns rather than vendor choices.
- Final model, framework, vector-store, and hosting vendor selection normally belongs to the separate implementation phase.

Step 12 stop condition: stop when a future build team can understand what systems, data, truth production remediation, runtime pattern, model capability requirements, RAG/retrieval requirements, orchestration/state requirements, hosting/environment requirements, tools, permissions, identity resolution, normalization, test data, credentials/secrets handling, audit logging, observability, and sequence would be required after Step 16 approval, while also knowing which paths are preferred, fallback, blocked, prohibited, or deferred to implementation.

## Risk And Control Model

Step 13 creates an implementation-grade risk and control object. It is not only a risk register. It translates prior organizational intelligence into concrete future protocols for data handling, permissions, tool actions, outputs, approvals, logging, monitoring, incident response, revocation, and stop conditions.

Step 13 does not provision credentials, grant access, connect tools, deploy monitoring, build controls, or authorize implementation.

Use prior outputs first:

- Step 5 workflow actions, decisions, approval gates, handoffs, edge cases, and failure modes.
- Step 6 diagnostic findings and automation blockers.
- Step 7 sensitive fields, source constraints, retention/export limits, permitted AI actions, and governance decisions.
- Step 9 AI guidance packs, forbidden behaviors, escalation triggers, output contracts, and test/evaluation cases.
- Step 10 trusted/disputed measurements and agent-safe metric usage.
- Truth production profiles, fragile truth status, and AI-safe truth usage.
- Step 11 business value case and risk tolerance implied by the value case.
- Step 12 technical implementation blueprint: systems, access paths, runtime/orchestration requirements, hosting/environment requirements, future tools/MCPs/connectors, document/email scope, credential/secrets approach, audit/logging, test strategy, blocked paths, and build sequence.
- Client policies and targeted owner confirmations from risk, security, legal, compliance, IT/data, and business owners.

Protocol derivation rules:

- Future AI behavior implies tool/action permissions.
- Sensitive data implies classification, handling, redaction, retention, export, and logging rules.
- Forbidden behavior from Step 9 implies prohibited tool actions and output controls.
- Disputed or conditionally trusted measurements imply human review, uncertainty language, or prohibition from final decisions.
- External communication implies approval gates, content restrictions, audit trail, and incident path.
- Write-back or workflow-triggering implies stronger approval, logging, rollback, and revocation controls; early phases should usually prohibit write-back.
- Broad source access implies narrowing scope or redesign.
- No audit logging, no revocation path, or no owner implies implementation stop condition.

Who does the work:

- AI drafts risk register, data classification, permission matrix, output controls, approval gates, monitoring needs, revocation triggers, incident paths, residual risk, and stop conditions from prior evidence.
- Operating partner challenges materiality, avoids over-control and under-control, aligns controls to value/risk, and routes unresolved issues.
- Client risk/security/legal/compliance confirms sensitive data, prohibited actions, retention rules, external sharing limits, incident expectations, and required approvals.
- Business owners confirm approval thresholds, unacceptable mistakes, human review requirements, and business accountability.
- IT/data owners confirm logging feasibility, revocation feasibility, service-account rules, access scopes, monitoring feasibility, and control dependencies.

The risk and control model must include:

- Stable risk/control model ID, linked opportunity, workflow, value case, and technical blueprint IDs.
- Overall risk posture: risk level, implementation allowed if controls met, blocking risks, and residual risk summary.
- Data classification matrix: field/content class, source, classification, handling rule, allowed AI use, prohibited AI use, redaction, retention/export constraints, and owner confirmation.
- Risk register: category, linked workflow object, linked system/source/tool/output, risk description, cause, impact, likelihood, severity, control, owner, status, verification needed, residual risk, and stop condition flag.
- Zero-trust controls:
  - Identity: allowed users, allowed roles, future service-account need, provisioning owner, authentication assumptions.
  - Data access: allowed sources, records, fields, documents, scopes, prohibited sources, and row/field/document restrictions.
  - Tool permissions: allowed actions, prohibited actions, human approval requirements, logging requirements, and failure behavior for each future tool/MCP/connector.
  - Output controls: allowed outputs, prohibited outputs, external-send approval, citation/evidence requirements, confidence requirements, uncertainty language, and prohibited claims.
  - Approval gates: action, approver role, trigger, evidence required, timeout, and override/exception path.
  - Monitoring: logs required, alert conditions, review cadence, monitoring owner, and quality/risk metrics.
  - Incident response: incident owner, severity levels, escalation path, containment actions, notification requirements, evidence preservation, and post-incident review.
  - Revocation: who can revoke, triggers, expected time to revoke, access/tool scope revoked, and restoration conditions.
- Stop conditions: condition, reason, required fix, owner, and whether it blocks Step 14 readiness.
- Targeted confirmation questions for unresolved high-risk or high-impact protocols only.

Step 13 stop condition: stop when each proposed future AI behavior, tool, source, sensitive data class, output type, approval path, log, monitor, incident path, and revocation path has either a control, an owner-confirmed prohibition, or a blocking unresolved decision.

## AI-Agent Readiness Score

Step 14 creates an implementation-grade readiness object for each candidate AI opportunity. It is not a generic maturity score and it does not authorize implementation. It decides whether Step 15 should become a build-ready implementation brief or a specific remediation plan.

Use prior outputs first:

- Step 5 workflow intelligence object: workflow, actors, decisions, edge cases, handoffs, information objects, source access profiles, and candidate AI assists.
- Step 6 diagnostic findings and automation blockers.
- Step 7 validation and governance decisions: official source, de facto trusted source, truth production, owner/steward, source access path, sensitive fields, retention, permission boundaries, and permitted AI actions.
- Step 8 knowledge/guideline requirements.
- Step 9 guidance packs, forbidden behaviors, escalation triggers, output contract, and test/evaluation cases.
- Step 10 measurement intelligence, metric trust, and agent-safe metric usage.
- Step 11 business value case and recommendation.
- Step 12 technical blueprint: systems, future access paths, tool/MCP/connector contracts, normalization, identity resolution, test strategy, credentials/secrets approach, audit/logging, and blocked paths.
- Step 13 risk/control model: data classification, tool permissions, output controls, approval gates, monitoring, incident response, revocation, residual risk, and stop conditions.

Who does the work:

- AI drafts the readiness object, applies hard gates, scores dimensions, maps dependencies, identifies blockers, and proposes behavior-level readiness from prior evidence.
- Operating partner challenges the score, decides whether gaps are truly blocking, chooses the minimum safe behavior level, and recommends the Step 15 path.
- Client confirms only unresolved business priority, source, access, owner, feasibility, risk, and approval facts. The client is not asked to score the whole model.

Hard gates override averages. Each readiness object must include gate status, evidence, confidence, owner, blocker flag, and required fix for:

- Business value.
- Workflow clarity.
- Source access.
- Data quality.
- Truth production.
- Knowledge/guidance.
- Measurement.
- Technical feasibility.
- Risk/control.
- Human oversight.
- Lifecycle.

Behavior-level readiness must classify each level as ready, conditional, not ready, prohibited, or unknown:

- `read_only_summary`
- `draft_and_flag`
- `recommendation_support`
- `human_approved_action`
- `autonomous_action`

Each readiness object must include:

- Stable readiness object ID, opportunity ID, workflow IDs, value case ID, technical blueprint ID, and risk/control model ID.
- Source-input coverage and missing or partial inputs.
- Candidate AI behavior, proposed users, business outcome, decision/action supported, accountable human owner, review owner, and scope boundary.
- Hard gates.
- Dimension scores: business value, workflow clarity, source access readiness, data quality, truth production readiness, knowledge/guidance readiness, measurement readiness, architecture feasibility, risk/control readiness, human oversight readiness, and change/lifecycle readiness.
- Dependency map: systems/sources, truth production profiles, guidance packs, metrics, runtime/orchestration requirements, hosting/environment requirements, future tools/MCPs/connectors, normalization, identity resolution, test data, credentials/secrets, logging, and controls.
- Blockers: type, description, linked gate, linked dimension, owner, required fix, evidence, behavior levels blocked, and whether the blocker changes the Step 15 path.
- Minimum safe first behavior: behavior level, allowed actions, required inputs, human review, required controls, tests, and explicit limitations.
- Not-ready or prohibited behaviors, reasons, and reconsideration conditions.
- Readiness decision and recommended Step 15 path.
- Owner confirmations still required.
- Stop boundary confirming that no agent, MCP, connector, normalization, credential, live-access, or implementation work starts before Step 16 approval.

Readiness decisions:

- `ready_for_step_15_build_brief`
- `fix_gaps_first`
- `governance_or_data_readiness_first`
- `knowledge_capture_first`
- `technical_feasibility_first`
- `risk_control_first`
- `deprioritize`
- `do_not_automate_yet`
- `discovery_incomplete`

Step 15 path options:

- `build_ready_implementation_brief`
- `gap_remediation_plan`
- `governance_data_readiness_plan`
- `knowledge_capture_plan`
- `technical_feasibility_plan`
- `risk_control_plan`
- `do_not_automate_recommendation`

Step 14 stop condition: stop when every candidate opportunity has a readiness object with hard gates, dimension scores, behavior-level readiness, truth production readiness, dependencies, blockers, required fixes, minimum safe first behavior, prohibited behaviors, owner confirmations, and a Step 15 path. Do not move to Step 15 with only a total score.

## Implementation Decision Packet

Step 15 creates the canonical machine-readable implementation decision packet. It is the controlling artifact for either a build-ready implementation brief, a remediation plan, or a do-not-automate recommendation. Markdown memos, sponsor summaries, IT/security views, and build-team briefs are generated views from this packet.

Step 15 is still pre-build. It does not request credentials, build agents, build MCPs, build connectors, build normalization pipelines, ingest emails, connect to live systems, or deploy automation.

Use prior outputs first:

- Step 14 readiness object and recommended Step 15 path.
- Step 12 technical implementation blueprint.
- Step 13 risk and control model.
- Step 9 AI guidance pack and test/evaluation cases.
- Step 10 measurement intelligence and trusted or conditionally trusted metrics.
- Truth production profiles and fragile-truth routing.
- Step 11 business value case.
- Step 5 workflow intelligence object.
- Step 7 source, owner, access, permission, retention, and governance decisions.
- Step 4 planning evidence and Step 3 interview-derived edge cases where linked.

Who does the work:

- AI assembles the packet from Steps 1-14, preserves object IDs, links evidence, carries forward runtime/hosting requirements, creates future component contracts, drafts access requests, drafts tests, and generates controlled audience views.
- Operating partner decides final first-build scope, narrows behavior level, removes overbuild, chooses remediation vs build-ready path, and makes the recommendation.
- Client sponsor confirms priority, owner commitment, funding appetite, and whether to continue toward implementation after Step 16.
- Business owners confirm workflow fit, human review, success criteria, and operating ownership.
- IT/data/security owners confirm that future access requests, credential/secrets approach, logging, controls, and sandbox/test-data assumptions are suitable as a plan.
- Future build team receives the full packet only after the client approves implementation.

The packet type must be one of:

- `build_ready_implementation_brief`
- `gap_remediation_plan`
- `governance_data_readiness_plan`
- `knowledge_capture_plan`
- `technical_feasibility_plan`
- `risk_control_plan`
- `do_not_automate_recommendation`

Each Step 15 packet must include:

- Stable packet ID, version, status, packet type, canonical-artifact flag, and source-input trace.
- Decision summary: recommended path, readiness decision, implementation recommendation, rationale, minimum safe behavior level, client decision needed, and approval boundary.
- Audience views: sponsor, business owner, IT/data/security, future build team, and remediation owner. Views must specify included and excluded sections.
- Business case summary: outcome, value confidence, trusted or conditionally trusted baseline metrics, expected value range, dependencies, and risks.
- First-build scope for build-ready packets: agent/workflow name, behavior level, users, included/excluded workflow steps, roles, edge cases, success definition, and explicit non-goals.
- Behavior contract: allowed actions, prohibited actions, human approval gates, output contract, and failure behavior.
- Systems and sources: owners, official source status, de facto trusted source status, truth status, role in workflow, data needed, required fields, sensitive fields/content, source access profile IDs, truth production profile IDs, future access path, fallback path, prohibited paths, freshness, data quality, retention/export constraints, and readiness status.
- Truth production readiness and remediation: truth profiles, status, reproducibility, auditability, safe AI usage, required fixes, and whether the packet must become a remediation plan.
- Runtime design requirements: runtime pattern, minimum viable runtime pattern, model capability requirements, RAG/retrieval requirements, orchestration/state requirements, multi-agent rationale if required, and overengineering guardrails.
- Hosting/environment requirements: preferred client cloud or environment, mandated stack, identity provider, data residency, network boundaries, compute pattern, storage needs, security requirements, observability requirements, and preferred/fallback/blocked hosting patterns.
- Future component contracts: tools, MCP servers, connectors, retrieval indexes, normalization jobs, workflow queues, eval runners, or similar future components, with input contract, output contract, allowed/prohibited actions, data touched, permission scope, human review, logging, failure behavior, and dependencies.
- Normalization and truth remediation plan: canonical entities, mappings, identity-resolution rules, quality checks, macro/formula/rule extraction, reconciliation tests, owners, blockers, and freshness requirements.
- Guidance and eval package: guidance pack IDs, rule references, required examples, eval cases, expected behavior, pass criteria, linked controls, and exit criteria.
- Risk and controls: risk posture, sensitive data summary, controls, audit logging, monitoring, incident response, and revocation.
- Future access requests for after Step 16 approval: system/source, purpose, permission scope, prohibited permissions, provisioning owner, approval dependencies, credential/secrets handling, rotation, revocation, audit logging, and test/sandbox preference.
- Build sequence: offline prototype, sandbox integration, limited pilot, and optional controlled expansion, with prerequisites, inputs, outputs, tests, exit criteria, and stop conditions.
- Owner matrix: business, day-to-day, technical, data, security, risk/compliance, future build owner, and approvers.
- Remediation plan when not build-ready: reason not ready, required fixes, linked readiness gate, owner, evidence needed, completion criteria, dependencies, reassessment trigger, and return to Step 14. Fragile truth must route to governance/data readiness, knowledge capture, or technical feasibility unless safe-limited behavior is explicitly selected.
- Do-not-automate recommendation when applicable: reasons, unacceptable risks, alternative recommendation, and revisit conditions.
- Stop boundary confirming no build, no live access, no credentials, no MCP/connector build, no normalization pipeline build, and no email ingestion during the 16-step engagement.

Step 15 output rules:

- The YAML or JSON packet is canonical. Markdown is only a generated view.
- Do not create separate inconsistent versions for different audiences. Generate controlled views from the same structured object.
- Do not include implementation secrets, actual credentials, live tokens, or employee passwords.
- Do not mark an item build-ready if Step 14 hard gates failed or blocking dependencies remain unresolved.
- Do not mark an item build-ready when material truth is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible unless the selected behavior is explicitly limited to safe support and the packet prohibits final decisions and autonomous action.
- Do not hide blockers in narrative. Every blocker must have an owner, evidence needed, completion criteria, and reassessment route.
- Do not create a build sequence without exit criteria and stop conditions.
- Do not convert requirements into vendor picks unless the client has a mandated stack or the implementation phase owns that selection.
- Do not default to RAG, vector databases, multi-agent orchestration, or frontier models without a requirement-based rationale.

Step 15 stop condition: stop when the future implementation decision can be made from the packet, and a future build team can understand scope, behavior, systems, truth production status, runtime pattern, model capability requirements, RAG/retrieval requirements, orchestration/state requirements, hosting/environment requirements, access requests, components, normalization, truth remediation, tests, controls, owners, sequence, and stop conditions without rediscovering the organization. If the opportunity is not ready, stop when the remediation packet names every blocking fix, owner, evidence needed, completion criteria, dependency, and Step 14 reassessment trigger.

## Managed Lifecycle Object

Step 16 creates the canonical machine-readable managed lifecycle object. It is the future operating contract for the AI capability after implementation approval. It defines how the future agent, workflow assist, remediation program, or no-automation decision will be owned, validated, launched, monitored, updated, paused, revoked, expanded, or retired.

Step 16 is still pre-build. It does not deploy, operate, monitor, connect, grant access, request credentials, build MCPs/connectors, build normalization pipelines, ingest emails, or launch a client agent during the 16-step engagement.

Use prior outputs first:

- Step 15 implementation decision packet.
- Step 14 readiness object.
- Step 13 risk/control model.
- Step 12 technical blueprint.
- Step 11 value case.
- Step 10 measurement intelligence.
- Truth production profiles and truth governance requirements.
- Step 9 guidance pack and eval cases.
- Step 7 source, owner, access, permission, retention, and governance decisions.
- Step 5 workflow intelligence object.

Who does the work:

- AI drafts the lifecycle object from Steps 1-15, preserving object IDs and owner/control/test/monitoring dependencies.
- Operating partner judges whether the lifecycle model is realistic, assigns accountability, challenges vague ownership, sets cadence, and decides whether Step 16 can be approved.
- Client sponsor confirms approval forum, future implementation decision path, owner commitment, and governance cadence.
- Business owner confirms success metrics, user feedback ownership, human review, escalation, and business-value tracking.
- IT/data/security owners confirm future monitoring, logs, access review, revocation, incident response, source freshness, and technical-control responsibilities as a plan.

The lifecycle path must be one of:

- `managed_agent_lifecycle`: for build-ready or conditionally build-ready opportunities.
- `remediation_lifecycle`: for opportunities that must fix gaps before implementation planning proceeds.
- `no_automation_review_cadence`: for opportunities that should not be automated yet but may need a future revisit condition.

Each Step 16 lifecycle object must include:

- Stable lifecycle object ID, version, status, canonical-artifact flag, lifecycle path, and source-input trace.
- Operating status and approval boundary: current engagement phase, future implementation status, separate implementation approval requirement, and no-live-agent boundary.
- Lifecycle scope: future agent/workflow name, opportunity, business outcome, authorized behavior level, unauthorized behavior levels, target user groups, environments, and scope exclusions.
- Owner model: business owner, day-to-day owner, technical owner, data owner, security owner, risk/compliance owner, support owner, guidance update owner, measurement owner, source freshness owner, incident owner, revocation owner, future build owner, sponsor, approval forum, and responsibility matrix.
- Future lifecycle stages: implementation approval, offline validation, sandbox integration, limited pilot, controlled rollout, monitored operation, and expansion/retirement review, each with entry criteria, exit criteria, approvals, and stop conditions.
- Launch gates: evals passed, controls verified, audit logging ready, human review workflow confirmed, revocation ready, and support model ready.
- Validation plan: eval suites, redacted/synthetic test data, source grounding, edge cases, permission boundaries, output quality, human review, failure behavior, and pre-pilot exit criteria.
- Monitoring plan: quality metrics, business metrics, risk metrics, technical metrics, source freshness checks, truth production checks, cost/usage metrics, thresholds, alerts, owners, and cadence.
- Feedback and correction loop: feedback channels, correction categories, severity routing, backlog owner, and review cadence.
- Change management: guidance updates, source changes, truth-rule changes, tool changes, model/runtime changes, required revalidation triggers, affected artifacts, and versioning policy.
- Access review and revocation: review cadence, review scope, revocation triggers, expected time to revoke, restoration conditions, and emergency pause process.
- Incident response: owner, severity levels, triggers, immediate actions, escalation path, evidence preservation, notification expectations, and post-incident review.
- Governance cadence: pilot governance meeting, steady-state review, and executive review cadence, attendees, agenda, and decision rights.
- Expansion criteria: eligible expansion types, required evidence, owner approval, Step 14 reassessment, and Step 15 packet update.
- Retirement criteria: low usage, high correction rate, source-system replacement, truth-production no longer reproducible, no measurable value, unacceptable risk, retirement owner, access revocation, retention/deletion rule, and documentation update.
- Remediation lifecycle when applicable: linked fixes, remediation owner, review cadence, evidence required to reopen readiness, return-to-step, and stop-if-not-resolved condition.
- No-automation review cadence when applicable: reason not automated, alternative operating recommendation, revisit conditions, revisit owner, and revisit cadence.
- Final approval: Step 16 approval status, approvers, approval date, approval notes, implementation authorization, and conditions before implementation.
- Stop boundary confirming no build, no live access, no credentials, no MCP/connector build, no normalization pipeline build, no email ingestion, and no deployed or operated agent during the engagement.

Step 16 output rules:

- The YAML or JSON lifecycle object is canonical. Markdown SOPs are generated views.
- Do not accept unnamed owners for monitoring, incident response, revocation, guidance updates, source freshness, or access review.
- Do not approve launch if launch gates lack evidence, owners, pass criteria, and stop conditions.
- Do not allow scope expansion without evidence, owner approval, updated readiness, updated packet, updated controls, and updated lifecycle object.
- Do not treat monitoring as only technical uptime. Include quality, business value, risk, source freshness, user feedback, cost, and correction metrics.
- Do not leave retirement undefined. Every future AI capability needs conditions for pause, remediation, and retirement.

Step 16 stop condition: stop when the future operating model can answer who owns the AI capability, who can approve launch, who monitors it, what proves it works, what triggers pause/revocation, how rules, truth production chains, and sources are updated, how incidents are handled, when scope can expand, when it should be retired, and what governance cadence keeps it accountable. If Step 15 is not build-ready, stop when the remediation or no-automation review cadence is owned, measurable, and has a return-to-readiness or revisit trigger.

## Evidence Standard

Separate:

- Facts.
- Assumptions.
- Inferences.
- Recommendations.
- Verification needs.

Use current verification for legal, regulatory, privacy, security, vendor, pricing, or market claims.

## Recommendation Standard

Every recommendation must name:

- Business reason.
- Evidence.
- Owner.
- Required input/fix.
- Risk/control.
- Measurement.
- Next action.

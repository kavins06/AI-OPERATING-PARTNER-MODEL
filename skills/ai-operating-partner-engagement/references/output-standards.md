# Output Standards

## Engagement Boundary

The engagement produces organizational intelligence, use-case selection, adoption design, and an implementation blueprint. It has Step 0 plus Steps 1-18. It does not implement agents, MCP servers, connectors, normalization pipelines, ETL/ELT, email ingestion, live integrations, write-back automation, or production tooling.

Allowed during the engagement:

- AI interviews and synthesis.
- Workflow intelligence generation.
- Controlled validation views.
- Planning evidence review.
- Source access profile capture.
- Truth production profile capture.
- KPI, metric, AI-capability metric, architecture, normalization, MCP/tooling, risk, zero-trust, readiness, lifecycle, and adoption blueprinting.
- Cheap offline proof points using approved redacted, synthetic, or historical examples, with no live credentials, write-back, deployment, production integrations, or unapproved data movement.

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

Implementation starts only after Step 18 is complete, the Step 17 decision packet and Step 18 lifecycle object are approved, and the client starts a separate build phase.

## Step 0 Engagement Tiering

Step 0 sets engagement depth before discovery starts. It must include:

- Tier: lite, standard, or deep.
- Scope boundaries and excluded areas.
- Vertical extension decision and required regulated-domain templates.
- Timeline, participant expectations, and evidence SLA.
- Offline proof-point boundary.
- Minimum viable artifact set for the tier.
- Trigger conditions for upscaling or downscaling.

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

Hard fragile-truth rule: if a material truth profile is shadow-derived, manually adjusted, person-dependent, disputed, missing, or not reproducible, Step 16 must fail the relevant autonomous, recommendation, or write/action behavior level unless the proposed AI behavior is explicitly limited to summarize, compare, flag uncertainty, draft clarification questions, or escalate.

## Step 1 Executive Opportunity Terrain

Step 1 produces a terrain map, not a use-case decision. It must include:

- Strategic priorities and operating context.
- Business functions or portfolios where leverage matters.
- Trust boundaries and sensitive operating areas.
- Named opportunity zones.
- Triangulated informant nominations from sponsor names, org-chart sampling, and "who do people call when this breaks?" probes.
- Initial adoption and regulated-domain signals.
- Sponsor confirmations needed before Step 2.

## Step 2 Candidate Use-Case Shortlist

Step 2 is the explicit use-case framing and disqualification step. It must produce a candidate shortlist before interviews deepen.

Each candidate use case must include:

- Stable candidate ID.
- One-line hypothesis.
- Target user and affected roles.
- Workflow boundary and out-of-scope boundary.
- Business value hypothesis.
- Truth production dependencies.
- Source/data dependencies.
- Knowledge/guidance dependencies.
- Adoption dependencies.
- Regulated-domain dependencies.
- Current confidence.
- Disqualification criteria.
- Discovery questions that would raise, lower, or kill confidence.

The shortlist is versioned and must be reaffirmed or revised at Steps 7, 12, and 16.

## Step 3 AI-Led Interview Output

Each interview output must include:

- Interview setup: discovery zone, participant role, why this person was interviewed, role-specific probes, consent/recording/retention handling, and boundaries.
- Recent concrete work episode.
- Normal path from trigger to outcome.
- Decisions and judgment used.
- Systems and sources.
- Information objects and source access paths.
- Source trust, conflicts, and truth production chains.
- Handoffs and approvals.
- Edge case register.
- Silent evidence need log.
- Sensitive data and trust boundaries.
- Adoption, incentive, and end-user trust signals.
- Regulated-domain signals where relevant.
- Participation-bias notes.
- Follow-up questions.
- Interview quality score.

The AI interviewer must ask questions, not assert unvalidated organization facts. If it makes an unsupported assumption, it must correct the assumption, mark it unverified, and continue. Do not ask participants for live uploads, file links, screenshots, or document submissions during interviews.

## Step 4 Variation Mapping

Use Step 4 when a single canonical workflow would be false or misleading. It must include:

- Fragmentation trigger: independent-contractor, franchise, multi-region, multi-portfolio, multi-system, seniority, local practice, or acquisition history.
- Variant IDs and descriptions.
- Where each variant appears.
- Official preferred pattern, de facto common pattern, and best-practice candidate.
- Participation bias and underrepresented groups.
- Which variants can share one workflow object and which require separate modeling.
- Adoption implication by variant.
- Risk and truth-production implication by variant.
- Stop condition for variation discovery.

## Step 5 Planning-Evidence Follow-Up

Step 5 requests only the smallest planning evidence needed after the interview batch. It must include:

- Evidence need consolidation.
- Owner-grouped request list.
- SLA, normally five business days unless the engagement tier says otherwise.
- Escalation path to sponsor or resolver if evidence stalls.
- Acceptable substitute hierarchy: redacted artifact, redacted screenshot, walkthrough recording, live walkthrough without transfer, sample export, formula/macro walkthrough, verbal description with operating-partner-recreated structure.
- Sensitivity, redaction, retention, and handling rule for each request.
- Items explicitly not requested because they are too broad, too sensitive, duplicate, or premature.

Step 5 never requests credentials, live access, write access, all-email ingestion, live MCP/connector access, or bulk unredacted data.

## Step 6 AI-Native Workflow Intelligence Object

Step 6 produces an `organizational_workflow_intelligence` object, not a human workflow report. Human-readable reports are views generated from this object.

The workflow object must include:

- Schema version and completeness checks.
- Workflow identity, business purpose, trigger, outcome, validation status, and confidence.
- Candidate use-case IDs and variation map IDs.
- Lightweight organization context: teams, roles, reporting structure, relevant people, and interview coverage.
- Role involvement and workflow actors with stable IDs.
- Normal-path steps with inputs, outputs, sources, handoffs, decisions, approvals, evidence references, validation status, and confidence.
- Decision points, explicit rules, tacit judgment, confidence signals, escalation triggers, human boundaries, allowed AI support, and forbidden AI behavior.
- Edge cases with detection, handler, escalation path, risk, frequency, severity, and automation implication.
- Information objects used by workflow steps, decisions, approvals, edge cases, and candidate assists.
- Source access profiles.
- Truth production profiles.
- Adoption signals and end-user trust barriers.
- Regulated-domain signals and linked extension IDs.
- Sources and systems mentioned, trust signals, quality issues, sensitivity, likely owners, and validation status.
- Approval gates and sensitive data signals.
- Operating strain and value signals.
- Role variation analysis.
- Candidate AI assists as hypotheses only.
- Evidence, facts, assumptions, inferences, unknowns, and enrichment routes.

Completeness checks must flag missing owners on decisions, missing source access profiles on material information objects, missing truth production profiles on material numbers/statuses/reports/metrics, candidate assists without forbidden behavior, and regulated-domain triggers without a linked extension.

Step 6 stops when the workflow can be represented as a structured graph with knowns, partials, unknowns, and enrichment routes. It must not finalize source authority, access permissions, metric formulas, risk scores, architecture, readiness, or build recommendations.

## Step 7 Organizational Intelligence Diagnostic

Step 7 enriches the workflow object with structured diagnostic findings. Each finding must include:

- Linked workflow-spec object IDs.
- Diagnostic lens: people, process, data, knowledge, governance, systems, incentives, politics, behavior, risk, measurement, architecture, adoption, or regulated-domain.
- Symptom and likely root cause.
- Evidence and confidence.
- Implication, severity, and recurrence.
- Whether it affects AI fit.
- Blocker classification: `fatal_for_use_case`, `requires_remediation_before_build`, `acceptable_with_controls`, or `informational`.
- Immediate route: disqualify use case, remediate, continue with controls, or continue.
- Owner candidate and validation need.

Fatal-for-use-case findings should update the Step 2 shortlist immediately instead of passively continuing through later steps.

## Step 8 Controlled Validation, Governance Resolution, And Baseline Release

Step 8 validates the workflow object and diagnostic without handing over the full organizational intelligence object. Use Step 6 and Step 7 to prefill what is known, then route only unresolved or high-risk objects to the smallest authorized resolver group.

Step 8 must produce:

- Role-specific validation views.
- Object-specific governance resolution views.
- Confirmed objects, corrections, disputes, and unresolved critical items.
- Official source and de facto trusted source decisions.
- Truth production chain, embedded rule, macro, manual adjustment, reconciliation, and expert-memory decisions.
- Practical access path confirmations.
- Owner/steward assignments.
- Sensitive field, retention, export, and handling constraints.
- Permitted AI actions and AI-safe truth usage.
- Back-edge decision: whether Step 6 must update, Step 7 must re-score, Step 2 shortlist must change, or the flow can continue.
- Organizational Intelligence Baseline: a machine-readable product data contract generated from Steps 0-8.

Material changes to workflow objects, truth profiles, source access paths, candidate use-case viability, or blocker classification loop back to Step 6 and Step 7 before continuing.

The Organizational Intelligence Baseline must be structured enough for a separate client-facing product to render useful controlled views without scraping interviews, notes, or reports. It must include:

- Source-input trace from Steps 0-8.
- Scope, identity/privacy policy, evidence policy, and sensitivity policy.
- Graph nodes: organization units, teams, roles, people or pseudonymized people, workflows, workflow variants, workflow steps, decisions, approval gates, edge cases, systems, sources, information objects, source access profiles, and truth production profiles.
- Graph edges: reporting relationships, handoffs, information dependencies, and source/truth links.
- Candidate AI portfolio: status, hypothesis, target users, evidence, blockers, AI-fit boundary, safe-now behavior, unsafe-now behavior, fix-first items, prohibited behavior, and next route.
- Validated intelligence summary for executive, operating, data/governance, and AI-fit views.
- Validation state: object counts, validation-status counts, unresolved critical items, back-edge requirements, and confidence.
- Product-view contract: what views can be generated, what each audience can see, and what must remain excluded.
- Downstream seeds for Steps 9-18 so the later process can continue from the same structured object.

Do not make the full raw internal object the client product. The baseline is a controlled data payload from which client-facing views can be generated.

## Step 9 Knowledge And Guideline Requirements

Step 9 identifies what knowledge and future AI guidelines are required before the workflow can be designed safely. It does not write final rules yet.

Each requirement must include:

- Stable knowledge ID.
- Linked workflow, step, decision, edge case, approval gate, information object, source, truth profile, variation, candidate use case, or candidate AI assist.
- Knowledge or guideline needed and why.
- Tacit, explicit, mixed, or unknown status.
- Where it likely lives: policy, SOP, system, document, tracker, spreadsheet, macro, reconciliation, email, meeting habit, expert memory, role practice, or external regulation.
- Likely expert/owner and inference basis.
- Examples needed: good, bad, edge, source conflict, fragile truth, regulated-domain if applicable.
- AI relevance, forbidden use, and next route.

Required categories include decision knowledge, exception knowledge, approval knowledge, source-conflict knowledge, truth-production knowledge, adoption/end-user knowledge, and regulated-domain knowledge.

## Step 10 AI Guidance Pack

Step 10 converts prioritized Step 9 requirements into implementation-ready guidance artifacts while staying pre-build.

The canonical guidance spec must include:

- Stable guidance ID, version, status, workflow ID, and linked Step 9 requirement IDs.
- Scope, out-of-scope areas, owners, reviewers, and update cadence.
- Required inputs and missing-input behavior.
- Source hierarchy, fallback sources, prohibited sources, conflict handling, and source access profile references.
- Truth production handling: allowed truth statuses, fragile-truth behaviors, prohibited uses, required confidence language, and escalation triggers.
- Regulated-domain handling where applicable.
- Explicit rules, tacit cues, examples, checklists, allowed behaviors, forbidden behaviors, escalation triggers, human approval gates, sensitive-field handling, retention constraints, and output contract.
- Eval suite split into behavioral evals and output-quality evals.

Minimum eval coverage before implementation planning:

- At least 10 good-path behavioral cases for each material behavior family.
- At least 10 bad/forbidden behavior cases for each material behavior family.
- At least 5 edge cases for each material behavior family.
- At least 5 source-conflict or fragile-truth cases when truth production is material.
- At least 5 regulated-domain cases when a regulated-domain extension applies.
- Output-quality evals covering required fields, evidence/citation, confidence language, sensitive-field handling, and schema/format compliance.

A `SKILL.md` style file can be a useful view, but the structured guidance spec remains canonical.

## Step 11 Measurement Intelligence And AI-Capability Metrics

Step 11 classifies existing metric trust and designs the future AI capability measurement model.

Existing metric classification must include:

- Metric ID, business question, decision/action supported, formula, grain, owner, steward, official source, de facto trusted source, truth production chain, truth status, manual adjustment status, reproducibility, auditability, quality checks, trust status, confidence, and agent-safe usage.

AI-capability metric design must include:

- Baseline metric candidates and trust caveats.
- Leading indicators.
- Lagging outcome indicators.
- Agent performance metrics.
- Human override and review metrics.
- Error, incident, drift, source-conflict, and fragile-truth signals.
- Adoption metrics.
- Cost/token/tool-call metrics.
- Kill criteria and pause thresholds.
- Metric owners and review cadence.

AI may propose metric trust from evidence, but the authorized client owner confirms, corrects, or leaves it unresolved.

## Step 12 Business Value Case And Portfolio Comparison

Step 12 is the economic and portfolio filter. It must include:

- Opportunity-level value case with evidence, assumptions, confidence, and fragile-truth caveats.
- Baseline metric trust and truth production status.
- AI-side cost model: model calls/tokens, tool calls, retrieval/storage, eval/observability, support, maintenance, human review, and vendor costs.
- Risks to value capture.
- Recommendation: carry forward, fix measurement first, fix truth production first, fix governance/knowledge first, deprioritize, or do not pursue.
- Portfolio comparison across surviving opportunities: value, feasibility, readiness, risk, adoption complexity, strategic fit, truth/data debt, cost, time-to-proof, and sequencing.

Do not use fragile, disputed, untrusted, unknown, shadow-derived, manually adjusted, person-dependent, missing, or not-reproducible metrics as reliable baseline evidence unless the value case is explicitly about fixing measurement or truth infrastructure.

## Step 13 Solution Shape And Adoption Design

Step 13 is a decision step before architecture documentation. It must decide:

- Build, buy, leverage-vendor, or hybrid posture.
- Vendor/native capability leverage and verification needed.
- Agent topology: no-agent workflow, workflow with LLM steps, single agent, multi-agent, or human-review assistant.
- Model-selection class: small/cheap, frontier, open-weight/private, multimodal, or tool-heavy; final model can be deferred to implementation.
- UX surface: embedded in existing system, chat, inbox, workflow queue, dashboard, browser extension, internal portal, or API-only.
- Retrieval/context shape.
- Eval and observability shape.
- End-user research findings.
- Adoption path: opt-in, encouraged, mandated, or incentive-led.
- Training, support, rollout, feedback channels, workflow retirement, and adoption-failure triggers.

Architecture should follow the selected solution shape, not silently decide it.

## Step 14 Technical/Vendor Implementation Blueprint

Step 14 documents the future technical plan. It must include:

- Stable blueprint ID and links to solution shape, adoption design, value case, guidance, measurement, risk, and readiness artifacts.
- Implementation posture.
- Systems and sources with business owner, technical owner, vendor owner, data needed, sensitivity, quality issues, truth status, access options, and practical constraints.
- Build/buy/leverage-vendor decision rationale.
- Future remediation patterns: macro extraction, formula documentation, semantic normalization, canonical entity design, reconciliation tests, owner assignment, governed replacement path, and shadow artifact retirement.
- Runtime requirements, model capability requirements, RAG/retrieval requirements, orchestration/state requirements, tool-calling needs, structured-output needs, latency/cost/privacy constraints, and human approval gates.
- Hosting/environment requirements.
- Future MCP/tool/connector specs.
- Normalization and identity-resolution plan.
- Email/document scope and prohibited all-email access.
- Test and validation plan using redacted, synthetic, or approved historical examples.
- Future access request package.
- Credential/secrets approach for the separate implementation phase.
- Preferred path, fallback path, blocked paths, and build sequence.

Step 14 does not select vendors as facts when capabilities may have changed. Record client-mandated stack, current vendor capability to verify, preferred pattern, fallback pattern, and blocked pattern.

## Step 15 Risk And Control Model

Step 15 creates an implementation-grade risk and control object. It must include:

- Risk register linked to workflow objects, guidance rules, sources, truth profiles, metrics, tools, outputs, adoption design, and technical blueprint.
- Data classification, sensitive-field handling, retention, export, and logging rules.
- Truth-production risk controls.
- Tool/action permissions and prohibited actions.
- Output controls, confidence language, human review, and escalation gates.
- Zero-trust access model and least-privilege assumptions for future implementation.
- Monitoring, incident response, revocation, pause, and stop conditions.
- Regulated-domain risk template when applicable.

For real estate, named risk categories include Fair Housing, TCPA/SMS/calling consent, RESPA/referrals where applicable, MLS/IDX/VOW data-use rules, and state advertising/licensure rules. These must be tied to controls and owners, not hidden under generic compliance.

## Step 16 AI-Agent Readiness Score

Step 16 produces behavior-level readiness, not a generic maturity score. It must include:

- Published hard gates.
- Dimension scores and evidence.
- Use-case framing gate.
- Truth production gate.
- Governance/access gate.
- Knowledge/guidance gate.
- Regulated-domain gate when applicable.
- Measurement and AI-capability metric gate.
- Solution-shape and technical feasibility gate.
- Risk/control gate.
- Adoption/change gate.
- Behavior-level readiness: summarize, retrieve, draft, compare, recommend, decide, act/write/send.
- Minimum safe first behavior.
- Prohibited behaviors.
- Blockers, required fixes, owners, and reassessment triggers.
- Recommended Step 17 path.

Readiness must fail any non-safe-limited behavior that depends on material fragile truth.

## Step 17 Implementation Decision Packet

Step 17 is the canonical machine-readable recommendation packet. It must include:

- Recommendation type: build-ready, fix-then-build, governance/data readiness plan, knowledge capture plan, technical feasibility plan, risk/control plan, do-not-automate, or no-action.
- Confidence statement with evidence strength.
- Conditional revision triggers.
- Candidate use-case and portfolio-sequencing context.
- Solution shape, adoption design, technical blueprint, risk/control model, readiness object, value case, measurement model, truth production profiles, and guidance references.
- Future access requests for after Step 18 approval.
- Remediation plans with owner, evidence needed, completion criteria, dependencies, and reassessment trigger.
- Audience-specific views: sponsor, technical, risk/legal/compliance, and operating owner.

Step 17 is still pre-build. It does not request credentials, connect systems, ingest emails, build MCPs/connectors, build normalization pipelines, or deploy automation.

## Step 18 Managed Lifecycle And Adoption-Change Object

Step 18 is the future operating contract. It must include:

- Ownership model.
- Launch gates and validation plan.
- Monitoring and eval cadence.
- Truth governance: source drift checks, rule-change approval, reconciliation cadence, owner review, and shadow artifact retirement.
- Guidance/source update process.
- Access review, revocation, incident response, pause conditions, and retirement criteria.
- Adoption/change model: end-user roles, training plan, incentive alignment, opt-in/mandate reality, feedback channels, workflow sunsetting, adoption metrics, adoption-failure triggers, and remedial actions.
- Expansion criteria and reassessment triggers.
- No-automation review cadence when the recommendation is not to automate.

Step 18 is still pre-build. It does not deploy, operate, monitor, connect, grant access, request credentials, build MCPs/connectors, build normalization pipelines, ingest emails, or launch a client agent during the engagement.

# Source-Grounded Standards And Governance Research

Purpose: translate current AI governance, risk, agent identity, and agent-security standards into requirements for the post-18 Agent Build + Managed AgentOps backbone. This reference is source-grounded, not legal advice or certification guidance.

Refresh caveat: reviewed on 2026-05-04. Re-check before each regulated launch, annual governance review, or material standards release. ISO standard details are paywalled; this mapping uses official ISO public summaries plus internal artifact needs. NIST agent standards and NCCoE agent identity work are active 2026 initiatives, not final control catalogs.

## Source Register

| Source | Primary URL | Source date / status | Refresh caveat |
|---|---|---|---|
| NIST AI Risk Management Framework 1.0 | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 | Published 2023-01-26; voluntary framework for AI systems. | Stable baseline, but supplement with current NIST playbooks, profiles, and sector guidance. |
| NIST AI RMF Playbook | https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook | Companion playbook for the AI RMF Govern, Map, Measure, and Manage functions. | Use for implementation actions, not as a substitute for risk-owner judgment. |
| NIST AI RMF Critical Infrastructure Profile concept note | https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure | Released 2026-04-07; concept note for a trustworthy AI profile in critical infrastructure. | Concept-stage material. Use as a routing cue for critical-infrastructure clients, not a final control catalog. |
| NIST AI Agent Standards Initiative | https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure | Announced 2026-02-17; focuses on secure, interoperable, identity-aware agents. | Active initiative. Treat as direction for trusted, interoperable, secure agent infrastructure, not finalized requirements. |
| NIST NCCoE Software and AI Agent Identity and Authorization | https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization | 2026 concept-paper project; status: reviewing comments. | Scope and outputs may change. Re-check before identity architecture freeze. |
| ISO/IEC 42001:2023 AI management systems | https://www.iso.org/standard/42001 | Published 2023; management-system requirements for responsible AI development, provision, and use. | Certification details require the purchased standard and accredited audit interpretation. |
| ISO/IEC 23894:2023 AI risk management | https://www.iso.org/standard/77304.html | Published 2023-02; guidance for AI-specific risk management. | Use as risk-process guidance, not a certifiable standard by itself. |
| EU AI Act | https://eur-lex.europa.eu/eli/reg/2024/1689/oj and https://www.consilium.europa.eu/en/press/press-releases/2024/05/21/artificial-intelligence-ai-act-council-gives-final-green-light-to-the-first-worldwide-rules-on-ai/ | Regulation (EU) 2024/1689; entered into force 2024-08-01 with phased obligations. | Route to counsel for EU use, high-risk Annex III, prohibited practices, GPAI, biometric, employment, education, credit, healthcare, law-enforcement, migration, or public-service cases. |
| OWASP Top 10 for LLM Applications 2025 | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf | 2025 application risk reference; includes prompt injection, sensitive disclosure, supply chain, poisoning, excessive agency, prompt leakage, vector/embedding weakness, misinformation, and unbounded consumption. | Living security guidance. Re-check OWASP GenAI pages for revisions and companion agentic guidance. |
| OWASP Top 10 for Agentic Applications | https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/ | Released 2025-12-10; focuses on autonomous-agent risks such as behavior hijacking, tool misuse, identity and privilege abuse. | Newly released and likely to evolve; use for threat-model coverage and testing expectations. |
| Cloud Security Alliance Agentic AI IAM | https://cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach | Released 2025-08-18; purpose-built IAM for autonomy, ephemerality, delegation, multi-agent systems, just-in-time credentials, and zero trust. | Practitioner framework, not a regulator. Re-check CSA and MAESTRO updates before IAM design lock. |

## Translation Rules For Section 2

Apply these rules when converting sources into internal delivery controls:

1. Treat frameworks as control intent, not copy/paste checklists. Convert each source expectation into an artifact field, gate criterion, owner, evidence reference, validator rule, and operating review cadence.
2. Route legal and regulatory triggers. Do not decide legal applicability inside the build team. EU AI Act, employment, credit, healthcare, education, biometric, law-enforcement, public-sector, critical-infrastructure, and safety-impacting cases require legal or compliance routing before launch.
3. Separate management-system obligations from system-level controls. ISO/IEC 42001 informs governance, inventory, roles, continual improvement, and change control. NIST, OWASP, CSA, and platform engineering guidance inform build, eval, identity, access, telemetry, incident, and rollback controls.
4. Treat agent identity as a launch gate. Any agent that calls tools, accesses business data, acts on behalf of users, or writes to a system needs a non-human identity, delegated authority boundary, credential owner, expiry, and revocation procedure.
5. Treat traces as audit evidence. A production agent must be explainable from trace IDs, release version, source IDs, tool calls, guardrail decisions, approvals, and outcomes.
6. Treat all agentic authority as change controlled. New users, sources, tools, models, prompts, retrieval corpora, environments, output types, action classes, or autonomy levels require phase 14 review before release.

## Backbone Requirements

| Backbone area | Requirement for Agent Build + Managed AgentOps | Source basis | Internal artifacts / gates |
|---|---|---|---|
| Governance | Maintain an AI management system for every approved post-18 build: named owners, policy context, AI inventory entry, intended use, prohibited use, lifecycle owner, change-control owner, and evidence trail. | ISO/IEC 42001; NIST AI RMF Govern. | `agent_build_contract`, `production_readiness_gate`, and `agentops_operating_record`; launch checks: governance owner, intended-use lock, and escalation matrix. |
| Risk classification | Classify every agent by use case, affected persons, regulated-domain trigger, autonomy level, tool authority, data sensitivity, external effect, reversibility, and EU AI Act routing. | NIST AI RMF Map/Measure; ISO/IEC 23894; EU AI Act risk categories. | `guardrail_control_matrix`, `production_readiness_gate`, and `change_expansion_retirement_review`; launch checks: classification complete and regulated routing resolved. |
| Identity | Assign each agent a unique, traceable non-human identity with owner, purpose, authority boundary, allowed systems, credential type, delegation chain, expiry, revocation path, and runtime attestation where feasible. | NIST AI Agent Standards Initiative; NCCoE agent identity; CSA Agentic AI IAM. | `tool_contract_registry`, `trace_observability_spec`, and `environment_progression_gate`; launch checks: identity issued, credential scope approved, and identity-attributed logs. |
| Access and delegation | Use least privilege, context-aware access, just-in-time or short-lived credentials for high-impact actions, explicit human delegation records, separation between planning identity and execution identity where useful, and no shared human credentials. | NCCoE identity concept; CSA Agentic AI IAM; OWASP excessive agency and identity/privilege abuse. | `tool_contract_registry`, `environment_progression_gate`, and `incident-revocation-runbook.md`; launch checks: no shared credentials, JIT/expiry policy, and revocation owner. |
| Tool and action control | Maintain tool allowlists, action tiers, human approval thresholds, dry-run modes, transaction limits, external-effect constraints, and rollback/compensation procedures before enabling autonomous execution. | OWASP LLM06 excessive agency; OWASP Agentic Applications; NIST AI RMF Manage. | Launch gates: `Gate A0 tool inventory`, `Gate A1 action-tier approval`, `Gate A2 rollback path`; Governance: action policy. |
| Data and source grounding | Bind agent outputs and decisions to approved source inventories, source access profiles, truth-production profiles, provenance logging, and uncertainty handling. Block autonomous behavior where truth is shadow-derived, disputed, missing, or not reproducible. | NIST AI RMF Map/Measure; ISO/IEC 23894; internal Step 6/8 truth-production rules. | Governance: `source_access_profile`, `truth_production_profile`; Launch gates: `Gate D0 source authority`, `Gate D1 fragile-truth stop check`; Monitoring: source/provenance coverage. |
| Evaluation before launch | Run behavior evals, security evals, red-team scenarios, prompt-injection tests, tool-misuse tests, identity/privilege-abuse tests, data-leakage tests, output-quality evals, and regulated-domain evals where applicable. | NIST AI RMF Measure; ISO/IEC 23894; OWASP LLM and Agentic guidance. | Launch gates: `Gate E0 eval plan approved`, `Gate E1 eval pass`, `Gate E2 residual-risk signoff`; Risk classification: residual risk register. |
| EU AI Act routing | Add a routing note for any EU market, EU user, EU worker, EU resident, or EU-deployed workflow. Route prohibited-practice, high-risk, GPAI, transparency, biometric, employment, education, credit, essential-service, healthcare, law-enforcement, migration, and public-sector triggers to legal/compliance before launch. | Regulation (EU) 2024/1689; Council AI Act summary. | Risk classification: `eu_ai_act_routing_note`; Launch gates: `Gate EU0 applicability`, `Gate EU1 legal route`, `Gate EU2 required evidence packet`. |
| Runtime monitoring | Monitor agent identity, tool calls, prompts/context sources, action outcomes, approval bypass attempts, policy denials, drift, hallucination/error rates, user overrides, data exposure, latency/cost anomalies, and near misses. | NIST AI RMF Manage; ISO/IEC 42001 continual improvement; OWASP agentic risks; CSA IAM. | `trace_observability_spec` and `agentops_operating_record`; launch check: telemetry live and alert thresholds assigned. |
| Incident handling | Maintain AI-specific incident playbooks for prompt injection, tool misuse, identity compromise, privilege abuse, data leakage, unsafe output, runaway cost, cascading agent failure, and regulator/customer notification routing. Include kill switch, credential revocation, log preservation, rollback, user comms, and post-incident learning. | NIST AI RMF Manage; ISO/IEC 42001 continual improvement; OWASP LLM/Agentic; CSA IAM. | `incident-revocation-runbook.md`, `agentops_operating_record`, and `release_version_manifest`; launch check: runbook approved and revocation rehearsed. |
| Lifecycle change control | Require reassessment when model, prompt, tool, connector, data source, identity scope, autonomy level, regulated use, vendor, or deployment context changes. Version decisions and preserve evidence. | ISO/IEC 42001; NIST AI RMF Govern/Manage; ISO/IEC 23894. | `change_expansion_retirement_review` and `release_version_manifest`; launch check: material-change review and rollback package. |
| Retirement and revocation | Define end-of-life triggers, sunset owner, credential revocation, data retention/deletion, user migration, archive requirements, and post-retirement monitoring for stale integrations. | ISO/IEC 42001 lifecycle management; CSA IAM; NIST AI RMF Manage. | `change_expansion_retirement_review`, `incident-revocation-runbook.md`, and `agentops_operating_record`; launch check: lifecycle completion and access revocation path. |

## Minimum Post-18 Gate Set

1. Governance gate: approved owner, intended use, forbidden use, lifecycle owner, and evidence location.
2. Risk gate: risk classification, EU AI Act routing note, data sensitivity, autonomy/action tier, residual risk owner.
3. Identity gate: agent identity, credential scope, delegation record, revocation path, no shared human credentials.
4. Source/truth gate: approved source access profiles, truth-production profiles, fragile-truth restrictions, provenance expectations.
5. Security gate: OWASP LLM and agentic threat model, tool allowlist, least privilege, prompt-injection and tool-misuse tests.
6. Launch gate: eval pass, human approval thresholds, rollback/compensation path, monitoring live, incident runbook approved.
7. Managed AgentOps gate: telemetry review cadence, access review cadence, drift thresholds, incident/near-miss review, change-control triggers.

## Internal Artifact Mapping

| Artifact | Required fields |
|---|---|
| `agent_build_contract` | agent ID, intended use, prohibited use, affected users, business owner, technical owner, risk owner, lifecycle owner, approval forum, and build authority. |
| `guardrail_control_matrix` | autonomy level, tool/action tier, data sensitivity, external effect, reversibility, regulated-domain triggers, residual risk, and control owner. |
| `tool_contract_registry` | non-human identity assumptions, credential type, allowed systems/tools, privilege scope, action schema, delegation constraints, expiry, and revocation owner. |
| `trace_observability_spec` | identity-attributed logs, signals, thresholds, retention, alert recipients, dashboard owner, drift-review cadence, and incident escalation triggers. |
| `incident-revocation-runbook.md` | incident classes, severity, detection source, kill switch, credential revocation, containment, rollback, evidence preservation, notification routing, and post-incident review. |
| `change_expansion_retirement_review` | changed component, change reason, risk delta, required re-evals, approvers, launch date, rollback plan, retirement decision, and evidence links. |

## Operating Rule

No post-18 agent may launch because a demo works. Launch requires a traceable chain from approved use case to governed identity, risk classification, source/truth controls, tested action boundaries, live monitoring, and incident handling. If any chain element is missing, the backbone must route to remediation, reduced autonomy, human-in-the-loop operation, or no launch.

# Behavior-Level Launch Bars

## Purpose

Behavior-level launch bars define what evidence is required before an agent can move from lower-risk assistance to higher-risk action. The level is about what the agent is allowed to do in the workflow, not how impressive the demo is.

Use these bars for launch approval, promotion, expansion, and rollback decisions.

## Universal Launch Requirements

Every launched behavior level requires:

- Named business owner, engineering owner, risk/control owner, and support owner.
- Documented workflow boundary, excluded decisions, excluded systems, and user population.
- Versioned agent instructions, model, tools, retrieval sources, guardrails, eval suite, and release notes.
- Traceability from user request to sources, tool calls, guardrails, outputs, and human approvals.
- Evals covering normal, edge, adversarial, ambiguous, no-answer, permission-denied, and source-conflict cases.
- Monitoring for quality, safety, latency, cost, tool errors, escalation, user corrections, and incidents.
- Rollback path to disable the agent, disable tools, downgrade behavior, or return work to manual flow.
- Source freshness and truth-production rules for every material input.

Hard stop: if a material source of truth is missing, stale, disputed, shadow-derived, person-dependent, or not reproducible, the agent cannot progress beyond summarization/flagging unless the behavior explicitly surfaces uncertainty and escalates to a human.

## Level 0: Observe And Log

Allowed behavior:

- Observe workflow events, collect telemetry, classify event metadata, and produce non-user-facing diagnostics.

Required launch evidence:

- Read-only permissions only.
- Data minimization and retention rules.
- Observability pipeline validated.
- No production write path, external communication, or user-facing recommendation.
- Privacy/security review for captured prompts, documents, traces, and metadata.

Pass bar:

- Captures the right events without leaking restricted data.
- Produces complete trace IDs and operational metrics.
- Does not influence workflow outcomes except through dashboards or reports.

Rollback trigger:

- Sensitive data over-capture, unauthorized access, telemetry corruption, or material monitoring cost spike.

## Level 1: Retrieve And Summarize

Allowed behavior:

- Retrieve approved sources, summarize evidence, answer factual questions, cite sources, and state uncertainty.

Required launch evidence:

- Approved source inventory with freshness rules and access controls.
- Retrieval tests for correct source selection, citation accuracy, stale-source handling, and no-answer behavior.
- Output schema or response rubric separating answer, evidence, limitations, and escalation.
- Guardrails for prompt injection, source misuse, unsupported claims, and policy boundaries.

Pass bar:

- High citation precision on golden cases.
- Refuses or escalates when sources are missing, conflicting, stale, or outside scope.
- Does not recommend actions unless those recommendations are explicitly part of a higher approved level.

Rollback trigger:

- Fabricated citations, unsupported claims, repeated stale-source use, or leakage across access boundaries.

## Level 2: Classify, Route, And Prioritize

Allowed behavior:

- Assign categories, urgency, owners, next-step queues, or workflow routes using approved criteria.

Required launch evidence:

- Taxonomy, routing rules, and exception classes are documented and versioned.
- Confusion matrix or equivalent eval results for key classes.
- Human-review queue for low-confidence, novel, regulated, high-impact, or ambiguous cases.
- Monitoring for class drift, false positives, false negatives, overrides, and backlog effects.

Pass bar:

- Meets threshold for critical classes, not just aggregate accuracy.
- Low-confidence and out-of-distribution cases are routed to humans.
- Misclassification is recoverable without material harm.

Rollback trigger:

- Critical false positives/negatives exceed threshold, drift appears after launch, or downstream teams lose trust in routing.

## Level 3: Recommend

Allowed behavior:

- Recommend actions, options, risk flags, or decision support while a human remains the decision-maker.

Required launch evidence:

- Recommendation rubric with accepted evidence types, forbidden evidence, uncertainty rules, and counter-indicators.
- Evals for grounding, completeness, bias, unsafe recommendations, and source conflict handling.
- UI or output format that makes human accountability clear.
- Human feedback capture and override monitoring.

Pass bar:

- Recommendations are evidence-grounded, calibrated, and include limitations.
- The agent does not present recommendations as decisions.
- Humans can inspect sources, rationale summary, and risk flags before acting.

Rollback trigger:

- Unsupported recommendations, hidden uncertainty, systematic bias, repeated human overrides, or recommendation-induced workflow harm.

## Level 4: Draft For Human Approval

Allowed behavior:

- Draft messages, records, plans, tickets, code, documents, or system changes that require human approval before release or execution.

Required launch evidence:

- Draft schema separates proposed content, evidence, assumptions, risks, and approval request.
- Approval workflow records approver, timestamp, diff, source references, and final submitted content.
- Evals for task completion, tone/format, policy compliance, hallucination, sensitive data handling, and downstream validity.
- No silent send, publish, merge, update, or external communication path.

Pass bar:

- Drafts reduce user effort without bypassing review.
- Material assumptions and missing inputs are visible.
- Human edits and rejections are monitored and used for improvement.

Rollback trigger:

- Drafts repeatedly introduce false facts, unsafe language, invalid system changes, or hidden compliance risk.

## Level 5: Execute With Explicit Approval

Allowed behavior:

- Prepare and execute actions only after a human approves a specific action payload.

Required launch evidence:

- Typed action plan and tool payload shown to the approver before execution.
- Human approval cannot be inferred from vague chat consent; it must bind to action, target, scope, and version.
- Tool guardrails validate payload before execution and result after execution.
- Dry-run, preview, or reversible mode where possible.
- Audit log captures user request, approval, payload, tool result, and downstream object IDs.
- Incident playbook covers failed execution, partial execution, duplicate execution, and mistaken approval.

Pass bar:

- The executed payload matches the approved payload.
- Permission checks use agent identity and delegated user authority correctly.
- Partial failures are visible and recoverable.

Rollback trigger:

- Execution without valid approval, payload mutation after approval, unauthorized object access, duplicate action, or unhandled partial failure.

## Level 6: Bounded Autonomous Execution

Allowed behavior:

- Execute a narrow, reversible or low-impact action class without per-action human approval, inside explicit thresholds.

Required launch evidence:

- Clear autonomy envelope: allowed actions, targets, frequency, spend/volume limits, hours, user groups, data classes, and stop conditions.
- Proven eval performance across multi-turn, tool-use, adversarial, and source-conflict cases.
- Production telemetry from lower behavior levels shows stable quality and low incident rate.
- Runtime enforcement of permissions, rate limits, action limits, and circuit breakers.
- Human review by sample, exception, anomaly, and user appeal.
- Kill switch and behavior downgrade tested.

Pass bar:

- Actions are bounded, auditable, recoverable, and measurably better than manual or semi-manual baseline.
- The agent escalates outside the autonomy envelope.
- Monitoring can detect drift, spikes, loops, and unsafe action patterns fast enough to contain harm.

Rollback trigger:

- Boundary violation, unrecoverable wrong action, unexplained action sequence, quality drift, incident threshold breach, or monitoring gap.

## Level 7: High-Impact Autonomous Execution

Allowed behavior:

- Autonomous execution for actions with material business, legal, financial, HR, security, customer, medical, regulated, or external consequences.

Launch stance:

- Default is prohibited unless the organization has explicit executive risk acceptance, mature controls, and domain-specific compliance approval.

Required launch evidence:

- Formal risk acceptance by accountable executive and control owner.
- Independent security, privacy, compliance, and domain review.
- Least-privilege agent identity, strong isolation, and scoped delegated authority.
- Continuous evaluation, red-team/adversarial testing, and trace-level audit.
- Real-time monitoring with automated circuit breakers.
- Tested rollback, compensating controls, customer/user remediation path, and regulatory notification path where applicable.
- Evidence from lower levels showing sustained performance under real use.

Pass bar:

- The agent has a narrow, controlled, continuously monitored autonomy envelope.
- High-impact decisions are explainable from approved sources and policies.
- Incident containment is faster than the expected harm propagation window.

Rollback trigger:

- Any unauthorized high-impact action, audit failure, unexplained decision path, compliance breach, source integrity failure, or control-plane outage affecting oversight.

## Promotion Rules

Behavior-level promotion requires:

- Passing eval thresholds for the target level.
- No unresolved severity-1 or severity-2 incidents.
- Updated risk register and guardrail map.
- Evidence that source quality and truth-production requirements still hold.
- Business owner approval and engineering owner approval.
- Pilot results or replay results from the previous level, unless the current level is initial launch.

Promotion is invalid if it changes workflow scope, tool side effects, source class, user group, or regulated domain without a new readiness review.

## Rollback And Downgrade Rules

Downgrade the behavior level when:

- The agent cannot meet its launch bar.
- Sources become stale, disputed, inaccessible, or contaminated.
- Tool contracts change without passing regression tests.
- Monitoring, tracing, or approval capture is degraded.
- Incident threshold is exceeded.
- Users or reviewers lose operational trust.

Rollback options:

- Disable agent.
- Disable one or more tools.
- Disable retrieval source.
- Force all actions to approval mode.
- Downgrade to recommend, draft, summarize, or observe only.
- Revert prompt, model, tool, guardrail, retrieval index, or runtime configuration.
- Route all work to manual process until revalidation.

## Evidence Packet For Launch Review

Each launch or promotion packet must include:

- Behavior level and autonomy envelope.
- Architecture diagram or plain-language control-flow description.
- Tool contract inventory.
- Source inventory and freshness rules.
- Eval dataset summary, thresholds, and results.
- Trace examples for success, failure, escalation, and guardrail tripwire.
- Monitoring dashboard or metric definition.
- Guardrail map.
- Human approval and escalation workflow.
- Release/version record.
- Incident and rollback runbook.
- Named owners and approval record.

## Primary Source Links

- OpenAI Agent evals: https://platform.openai.com/docs/guides/agent-evals
- OpenAI trace grading: https://platform.openai.com/docs/guides/trace-grading
- OpenAI Agents SDK tracing: https://openai.github.io/openai-agents-python/tracing/
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
- Anthropic Building Effective Agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic Demystifying Evals for AI Agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic tool use docs: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use
- AWS Bedrock AgentCore overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- AWS AgentCore Observability: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html
- AWS agentic AI security principles: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/
- Microsoft Foundry Control Plane: https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/overview
- Microsoft Foundry agent evaluation: https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent
- Microsoft Foundry continuous evaluation: https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/continuous-evaluation-agents
- Salesforce Agentforce Testing Center: https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/
- Salesforce Agentforce DX testing: https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx-test.html

# Agent Engineering Quality Bar

## Purpose

This reference defines the minimum engineering bar for managed agent builds. It is implementation-phase guidance: agents must be treated as stateful, tool-using software systems with explicit architecture, contracts, tests, telemetry, guardrails, release controls, and rollback paths.

Use this bar before any production pilot, expansion, or behavior-level promotion.

## Implementation-Grade Definition

An agent build is implementation-grade only when another engineer, security reviewer, operator, or client-side owner can take the contract package and know exactly:

- What behavior is approved, what is forbidden, and what triggers change control.
- Which Section 1 facts were used, by object ID and evidence reference.
- Which model, prompt, tool, data, identity, environment, eval, guardrail, trace, release, and rollback versions are active.
- Which owner is accountable for business value, engineering, data/source quality, security, risk, support, revocation, incidents, and change decisions.
- Which test, trace, metric, alert, runbook, and review cadence proves the agent is behaving inside its approved envelope.
- What to do when a tool fails, a source drifts, a user asks for out-of-scope work, an eval regresses, a cost spike occurs, an incident happens, or an expansion is requested.

If a build artifact requires undocumented tribal knowledge to operate or review, it is not implementation-grade.

## Source Grounding

Primary sources used:

- OpenAI: agent evals, trace grading, tracing in the Agents SDK, guardrails, structured outputs, and function calling.
- Anthropic: Building Effective Agents, Demystifying Evals for AI Agents, Effective Harnesses for Long-Running Agents, tool use, and writing effective tools.
- AWS: Amazon Bedrock AgentCore Runtime, Gateway, Identity, Memory, Observability, and AWS security principles for agentic AI systems.
- Microsoft: Microsoft Foundry Control Plane, tracing, observability, local and portal evaluations, and continuous evaluation.
- Salesforce: Agentforce Testing Center, Agentforce DX testing, sandboxes, analytics, utterance analysis, and deployment lifecycle tooling.

## Core Architecture Requirements

Every agent architecture must document:

- Business outcome, target users, workflow boundary, excluded workflow areas, and behavior level.
- Agent pattern: single call, workflow, planner-executor, evaluator-optimizer, routed workflow, multi-agent handoff, or autonomous loop.
- Why agentic complexity is justified. Prefer the simplest reliable pattern; add autonomy only when fixed workflows or single model calls fail measured requirements.
- State model: ephemeral session state, durable memory, retrieval context, user profile context, and audit records.
- Control loop: planning, tool selection, tool execution, environmental feedback, stopping conditions, retries, escalation, and human checkpoints.
- Authority boundary: what the agent may observe, recommend, draft, execute, update, or never touch.
- Failure modes: wrong source, stale source, bad tool call, hallucinated action, unsafe action, inaccessible dependency, model refusal, timeout, loop, user ambiguity, and downstream system error.
- Human oversight model: approval-before-action, review-after-draft, exception escalation, sampled audit, or blocked autonomous action.

Hard rule: no production agent may rely on hidden prompt behavior as its primary control mechanism. Critical behavior must be enforced by schemas, tool permissions, runtime policy, guardrails, environment isolation, and release gates.

Architecture review must also include an explicit negative architecture: capabilities, sources, tools, memory, network paths, write paths, user groups, and workflows that are intentionally excluded from the first release.

## Tool Contract Requirements

Every tool exposed to an agent must have a contract that is clear to both code and model:

- Stable tool name, owner, version, and lifecycle status.
- Plain-language description of when to use it, when not to use it, and how it behaves.
- JSON Schema or equivalent typed input contract with required fields, enums, formats, bounds, and `additionalProperties: false` where supported.
- Structured output contract with success, partial success, no-op, not found, validation failure, permission failure, rate limit, timeout, and upstream error cases.
- Idempotency model and side-effect class: read-only, draft, reversible write, irreversible write, external communication, financial/legal/HR/security action, or privileged operation.
- Authorization model: agent identity, user delegation, scope, tenant boundary, row/object-level restrictions, and audit identity.
- Preconditions, postconditions, and compensating action if rollback is possible.
- Timeout, retry, rate limit, concurrency, and circuit-breaker behavior.
- Tool guardrails before and after execution for sensitive or side-effecting tools.
- Example calls, edge cases, and known model misuse patterns.

Tool design must minimize model confusion. Prefer explicit parameter names, absolute or fully qualified object identifiers, bounded enums, dry-run modes, and typed action plans over free-form instructions for side-effecting work.

Reject a tool contract when any of these are missing: owner, stable schema, permission scope, tenant/user boundary, side-effect class, audit identity, rate limit, timeout, error taxonomy, idempotency or duplicate prevention, revocation path, and compensating action for failed or partial execution.

## Structured Output Requirements

Use structured outputs for any output consumed by code, stored as a record, used for routing, used for evaluation, or shown as a compliance artifact.

Minimum requirements:

- Define a schema in code and version it with the agent.
- Reject or retry invalid outputs; do not silently coerce material fields.
- Represent refusal, uncertainty, insufficient evidence, and escalation as first-class fields.
- Keep rationales, cited evidence, action requests, and final user-facing text as separate fields.
- Use strict schema enforcement where the model/provider supports it.
- Validate downstream invariants after model output, not only during generation.

## Eval Harness Requirements

Every agent must ship with an eval harness before pilot:

- Dataset: golden tasks, realistic historical cases, synthetic edge cases, adversarial cases, ambiguous requests, source-conflict cases, no-answer cases, and permission-denied cases.
- Multi-turn tests for agents that ask clarifying questions, call tools, update state, or recover from errors.
- Tool-use tests that verify correct tool choice, correct parameters, correct sequencing, correct interpretation of tool results, and refusal to use unavailable tools.
- Behavior-level tests aligned to observe, summarize, classify, recommend, draft, execute-with-approval, or autonomous execution.
- Regression suite for every prompt, tool schema, model, retrieval corpus, control policy, or orchestration change.
- Offline replay from recorded traces where privacy policy permits.
- Human review rubrics for subjective quality and domain judgment.
- Automated graders for schema validity, task completion, citation/grounding, safety, latency, cost, tool correctness, and policy adherence.
- Trace-level grading for multi-step agents, not only final-answer grading.

Acceptance thresholds must be explicit. A release cannot pass with only anecdotal demo success.

Minimum phase 7 evidence:

- Eval inventory mapped to guidance rules, output contract fields, tool permissions, prohibited behaviors, and known failure modes.
- At least one golden, edge, adversarial, permission-denied, source-conflict, no-answer, and regression case for every material behavior.
- Trace-level grading for tool-using or multi-step behavior, including tool choice, argument correctness, sequencing, and recovery.
- Blocking thresholds for correctness, policy adherence, tool safety, source grounding, schema validity, latency, cost, and escalation quality.
- A rule for creating new eval cases from pilot feedback, incidents, near misses, and human corrections.

## Tracing And Observability Requirements

Production and pilot agents must emit traces, metrics, and logs sufficient to explain behavior without relying on memory or screenshots.

Required trace spans:

- User request intake and normalized task.
- Agent/version/model/prompt/tool-policy identifiers.
- Retrieval calls and source identifiers.
- Tool calls, inputs, outputs, latency, errors, retries, and permission decisions.
- Guardrail checks and tripwire outcomes.
- Handoffs, human approval steps, and escalation.
- Final output, action summary, and outcome status.

Required metrics:

- Task success, user correction rate, escalation rate, refusal rate, fallback rate, tool error rate, timeout rate, loop/iteration count, latency, token usage, cost, and incident count.
- Behavior-level metrics: grounding quality, source freshness, action accuracy, approval override rate, rollback frequency, and policy violation rate.

Required controls:

- Correlate trace ID, conversation ID, agent ID, user/session ID, environment, release version, and tenant/customer boundary.
- Redact or exclude sensitive prompt, tool, audio, or document data where policy requires.
- Export telemetry to the operating monitoring plane, not only a vendor dashboard.
- Support production debugging, sampled continuous evaluation, incident reconstruction, and audit review.

Trace review must be possible without exposing restricted raw content to every reviewer. Redaction, role-based trace access, and evidence summaries must be defined before pilot.

## Guardrail Requirements

Guardrails must be layered:

- Input guardrails: block or route malicious, out-of-scope, prohibited, ambiguous, or high-risk requests.
- Retrieval guardrails: enforce approved source sets, freshness rules, citation requirements, and source conflict handling.
- Tool guardrails: validate each sensitive tool call before execution and validate output after execution.
- Output guardrails: check final answer quality, policy fit, disclosure, citation, uncertainty, and action summary.
- Runtime guardrails: enforce identity, authorization, rate limits, environment, data boundary, network boundary, and spend limits.
- Human guardrails: require approval for high-impact, irreversible, externally visible, regulated, privileged, or low-confidence actions.

Guardrails must have measurable tripwires, owners, logs, and runbooks. Prompt-only safety instructions are not sufficient for side-effecting agents.

## Environment Progression

Agents progress through environments only with evidence:

1. Local development: mocked tools, synthetic data, unit tests, schema tests, and prompt/tool iteration.
2. Sandbox: isolated credentials, synthetic or redacted data, no production write path, trace review, and broad eval coverage.
3. Staging: production-like data shape, restricted credentials, dry-run or reversible actions, load testing, and operational monitoring.
4. Limited pilot: named users, restricted scope, sampled human review, rollback path, support channel, and daily quality review.
5. Production: approved behavior level, monitoring SLOs, incident process, versioning, access review, and continuous evaluation.
6. Expansion: new scope, tools, users, autonomy, or source classes require a new readiness review.

Do not skip sandbox for agents with tools, memory, retrieval, write-back, or external communication.

## Release And Versioning Requirements

Every release must version:

- Agent instructions/prompts.
- Model and model settings.
- Tool schemas and tool implementations.
- Guardrails and policy rules.
- Retrieval sources, embeddings/indexes, and source freshness rules.
- Eval datasets, graders, and thresholds.
- Runtime configuration and environment permissions.
- User-facing behavior level and approval requirements.

Release notes must include changed behavior, expected risk change, eval deltas, monitoring changes, rollback instructions, and owner approval.

Use canary or limited rollout for material changes. Treat prompt, tool, retrieval, model, and guardrail changes as production changes.

Release records must be reproducible. A reviewer should be able to reconstruct the active behavior from the release manifest, referenced artifacts, and source versions without relying on memory, screenshots, or vendor dashboard state alone.

## Incident And Rollback Requirements

Every production agent must have an incident playbook:

- Trigger conditions: policy violation, unsafe action, repeated wrong answer, source contamination, unauthorized access, tool outage, cost spike, latency spike, user harm, or compliance event.
- Immediate containment: disable agent, disable tool, downgrade behavior level, force human approval, revert prompt/model/tool version, revoke credentials, or route to manual workflow.
- Evidence capture: trace IDs, release version, user/session, tool calls, source IDs, guardrail results, approval records, and downstream changes.
- Customer/user communication path when applicable.
- Root cause review and regression test creation.
- Re-release gate requiring fixed controls and passing evals.

Rollback must be tested before production. For irreversible actions, the agent must support containment and compensating operational processes even when true technical rollback is impossible.

## Minimum Production Readiness Checklist

An agent is not production-ready until all are true:

- Architecture, authority boundary, and behavior level are documented.
- Tool contracts are typed, versioned, permissioned, tested, and observable.
- Eval harness covers golden, edge, adversarial, multi-turn, and tool-use cases.
- Trace-level observability works in the target environment.
- Guardrails cover input, retrieval, tool, output, runtime, and human approval.
- Environment progression evidence exists from sandbox and staging or an approved limited-pilot exception.
- Release/versioning records can reproduce current behavior.
- Rollback and incident playbook are tested.
- Owners for business outcome, engineering, risk, data/source quality, and support are named.

## Primary Source Links

- OpenAI Agent evals: https://platform.openai.com/docs/guides/agent-evals
- OpenAI trace grading: https://platform.openai.com/docs/guides/trace-grading
- OpenAI Agents SDK tracing: https://openai.github.io/openai-agents-python/tracing/
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
- Anthropic Building Effective Agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic Demystifying Evals for AI Agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic Effective Harnesses for Long-Running Agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic tool use docs: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use
- Anthropic writing tools for agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- AWS Bedrock AgentCore overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- AWS AgentCore Runtime: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html
- AWS AgentCore Observability: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html
- AWS agentic AI security principles: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/
- Microsoft Foundry Control Plane: https://learn.microsoft.com/en-us/azure/ai-foundry/control-plane/overview
- Microsoft Foundry tracing: https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/trace-agent-setup
- Microsoft Foundry agent evaluation: https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent
- Microsoft Foundry continuous evaluation: https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/continuous-evaluation-agents
- Salesforce Agentforce Testing Center: https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/
- Salesforce Agentforce DX testing: https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx-test.html

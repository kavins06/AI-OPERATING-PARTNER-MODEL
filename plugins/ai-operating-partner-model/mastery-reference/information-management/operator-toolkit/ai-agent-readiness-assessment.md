# AI-Agent Readiness Assessment

Purpose: score candidate workflows before selling or building an AI agent.

When to use: first discovery call, pilot selection, pre-implementation review, or quarterly roadmap refresh.

Required inputs:
- Workflow name and business owner.
- Current systems and source documents.
- Data sensitivity and access needs.
- Current pain, volume, cycle time, error rate, and cost.
- Human decision points and exception paths.

Score each dimension from 1 to 5:

| Dimension | What 1 Means | What 5 Means | Score |
|---|---|---|---:|
| Business value | Nice-to-have or unclear ROI | Direct revenue, cost, speed, risk, or client-service impact | |
| Workflow clarity | Ad hoc and undocumented | Stable steps, owners, triggers, and exceptions | |
| Data quality | Missing, duplicated, stale, or contradictory | Trusted source of record and known quality rules | |
| Knowledge availability | Expertise lives only in people's heads | SOPs, examples, rules, and review criteria exist | |
| Privacy/security risk | Sensitive data with unclear controls | Least privilege, audit, retention, and approvals are defined | |
| Integration feasibility | Manual exports or inaccessible systems | APIs, permissions, and sandbox/test data are available | |
| Human oversight | No review owner or escalation path | Clear approval gates and exception handling | |
| Measurement | Success cannot be measured | Baseline and target metrics are defined | |

Decision rule:
- 32-40: strong pilot candidate.
- 24-31: proceed after fixing named readiness gaps.
- 16-23: discovery or governance project before automation.
- Below 16: do not automate yet.

Quality checks:
- Every score has evidence, not vibes.
- Sensitive data and permissions are named.
- The first pilot has one workflow owner and one measurable outcome.

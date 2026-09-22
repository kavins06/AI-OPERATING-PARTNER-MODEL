# Privacy and Security Risk Register

Purpose: make AI-agent risk visible, owned, and manageable.

| Risk | Data / Workflow | Impact | Likelihood | Control | Owner | Status |
|---|---|---:|---:|---|---|---|
| Overbroad agent access | | | | Least privilege and scoped credentials | | |
| Sensitive data in prompts or logs | | | | Redaction, retention rules, logging policy | | |
| Incorrect external message | | | | Human approval for client-facing outputs | | |
| Hallucinated policy or lease term | | | | Source-grounded retrieval and citation requirement | | |
| Unapproved data sharing | | | | Data-processing and vendor review | | |
| Missing audit trail | | | | Structured logs and review queue | | |
| Model or integration outage | | | | Fallback procedure and SLA | | |

Required checks:
- Identify, protect, detect, respond, and recover controls are considered.
- Zero-trust principles are applied to users, devices, applications, workloads, data, network/environment, automation, and visibility.
- Privacy claims and legal obligations are verified against current official sources before client-facing use.

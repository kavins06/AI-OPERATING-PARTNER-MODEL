# Data Governance Discovery Form

Purpose: capture the ownership, quality, access, and lifecycle rules an AI agent depends on.

Client / segment:
Workflow:
Business owner:
Data steward:

Source inventory:

| Source | System / Location | Owner | Users | Update Frequency | Sensitive Data | Quality Issues |
|---|---|---|---|---|---|---|
| | | | | | | |

Core governance questions:
- What is the source of record?
- Which fields or documents are trusted enough for automation?
- Who can approve definitions, rules, and exceptions?
- What data can the agent read, write, summarize, or send?
- What data must never leave the system?
- What retention, deletion, and audit requirements apply?
- What quality checks happen before agent output reaches a client, tenant, buyer, seller, investor, or vendor?

Outputs:
- Source-of-record map.
- Stewardship assignments.
- Access matrix.
- Data quality rules.
- Agent permission boundaries.

Quality checks:
- No agent gets broad inherited access by default.
- Every sensitive field has a handling rule.
- Every output has a human owner or approval rule.

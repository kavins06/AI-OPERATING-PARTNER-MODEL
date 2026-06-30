# Example Build-Ready Implementation Brief

This is a blueprint example, not an implementation artifact.

Agent / workflow: Monthly report drafting assistant
Business owner: Operations manager
Technical owner: Data lead
Data steward: Reporting analyst
Risk owner: Operations manager

## Business Outcome

Reduce monthly report preparation time and correction rate.

## First Safe Behavior

Read approved metrics, retrieve source-linked exception notes, and draft an internal report narrative for human review.

## Controls

- Read-only data access.
- Source citations required.
- Human approval before sending.
- Log retrieved sources, generated draft, edits, and approval.

## Future Access Package

- Provision after Step 18 approval.
- No employee credentials.
- Use scoped service account or approved connector.
- No write-back or external send permission in first implementation phase.

## Success Metrics

- Report cycle time.
- Correction rate.
- Manager edit rate.
- User satisfaction.

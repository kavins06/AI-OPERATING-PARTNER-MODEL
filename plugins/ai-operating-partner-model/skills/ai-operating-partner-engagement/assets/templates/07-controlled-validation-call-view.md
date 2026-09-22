# Controlled Validation and Governance Resolution

Client:
Workflow:
Date:
Facilitator:

## Core Rule

Do not hand over the full organizational intelligence object for review. Use it internally as the canonical reference, then generate controlled role-specific and object-specific views.

Step 8 should also finish workflow-relevant governance resolution: official source, de facto trusted source, truth production chain, source access path, owner/steward, sensitive fields, retention or handling rules, access constraints, reproducibility, auditability, and permitted AI actions. This is not a third broad interview pass. Route each unresolved object to the smallest authorized resolver group.

## Internal Inputs

- AI workflow specification:
- Organizational intelligence diagnostic:
- Evidence need log:
- Planning-evidence follow-up results:
- Preliminary source inventory:
- Information object and source access profile register:
- Truth production profile register:
- Open validation questions:
- Open governance decisions:

## Validation Participants

| Participant / Role | Validation Scope | Governance Resolution Scope | View Type | Why Included |
|---|---|---|---|---|
| | | | sponsor / director / manager / operator / system-data-owner / risk-legal-compliance | |

## Role-Specific Validation Views

### Sponsor / Executive View

Show only:

- Business purpose and outcome.
- Decision rights and ownership questions.
- High-level approval boundaries.
- Major risks, unknowns, and enrichment routes.
- Governance decisions requiring leadership authority.

Correction and decision prompts:

- What business context did we misunderstand?
- Which decision owner or approval boundary is wrong?
- Which unresolved decision requires leadership authority?
- Which area is too sensitive or strategic to expose broadly?

### Director / Manager View

Show only:

- Escalation paths.
- Approval gates.
- Portfolio, region, or team variation.
- Standardization opportunities.
- Diagnostic findings tied to their area.
- Source, owner, and exception decisions in their operating area.
- Truth production chains, manual adjustments, and de facto trusted artifacts in their operating area.

Correction and decision prompts:

- Where did we overgeneralize across teams or portfolios?
- Which approval gate applies only sometimes?
- Which variation is intentional versus accidental?
- Which source is authoritative for this workflow object?
- Which source or artifact do people actually trust when it differs from the official source?
- Which manual adjustment, reconciliation, or macro logic determines the final answer?
- Who owns the definition, exception, or quality decision?

### Operator / Front-Line View

Show only:

- Steps, handoffs, trackers/reports used.
- Information objects and practical access paths.
- Source conflicts and manual checks.
- Truth production chains, shadow trackers, and manual adjustments they use or inherit.
- Edge cases and exceptions.
- Places where the model may miss lived work.

Correction prompts:

- Which step is wrong or missing?
- Which source do people actually trust?
- Which access path, report, module, tracker, or folder is wrong or missing?
- Which edge case is rare versus common?
- Where does the model make the work look cleaner than it is?
- Is there still a hidden tracker, manual correction, or quality issue not captured?
- Which final report, spreadsheet, macro, or person-dependent rule makes the work look true?

### System / Data Owner View

Show only:

- Systems and sources mentioned.
- Information objects and source access profiles.
- Official source, de facto trusted source, and truth production questions.
- Data quality issues.
- Access or export constraints.
- Known sensitive fields, if appropriate.
- Candidate AI actions that require system or permission confirmation.

Correction and decision prompts:

- Which source is authoritative?
- Which source is official, and which source or artifact is actually trusted?
- Is the truth production chain documented, reproducible, auditable, and owned?
- Which formulas, macros, manual adjustments, or reconciliations produce the final number or status?
- Which access path, report, module, lookup key, or required field is correct?
- Which source is not safe to rely on?
- Which data-quality issue is known and who stewards it?
- What access, export, audit, or retention constraint matters?
- Can AI read, summarize, compare, draft from, export, send, or write this object?
- Which AI action is prohibited until later controls exist?

### Risk / Legal / Compliance View

Show only:

- Sensitive data signals.
- External communication risks.
- Approval boundaries.
- Legal, regulatory, contractual, or reputational concerns.
- Do-not-automate-yet areas.
- Proposed AI actions touching sensitive content.

Correction and decision prompts:

- Which data or action needs tighter control?
- Which communication requires approval?
- Which field, document, or output has retention or handling requirements?
- Which finding should be routed to risk register or zero-trust controls?
- Which AI action is prohibited regardless of later design?

## Object-Specific Governance Resolution Queue

| Object ID | Object Type | Decision Needed | Current Evidence | Authorized Resolver | Decision Status |
|---|---|---|---|---|---|
| | information_object / source_access_profile / truth_production_profile / source / system / field / decision / approval_gate / output | access_path / lookup_keys / official_source / de_facto_source / truth_chain / owner / steward / sensitive_field / retention / access / ai_action | | | pending / resolved / disputed / blocking |

Use this queue to avoid asking the same people broad questions again. Each row should have a named resolver and a specific decision.

## Governance Resolution Questions

Ask only the questions needed for unresolved workflow objects:

- Is this the authoritative source for this workflow object?
- What is the official source, and what source or artifact is de facto trusted?
- How is the final number, status, report, or decision produced?
- Is the production chain documented, versioned, owned, reproducible, and auditable?
- Which formulas, spreadsheet macros, manual adjustments, reconciliations, or expert-memory rules matter?
- Is this the correct practical access path for the information object?
- What module, report, dashboard, folder, inbox, portal, tracker, lookup key, or required field should be corrected?
- Who owns the definition or business meaning?
- Who stewards quality, corrections, duplicates, or missing values?
- Which fields or content classes are sensitive?
- What retention, export, audit, or handling rule applies?
- What access group may see or use this object today?
- Can AI read, summarize, compare, draft from, export, send, or write this object?
- Which action is prohibited until risk, architecture, or zero-trust controls are designed?

## Structured Validation and Governance Event

```yaml
validation_event:
  workflow_id:
  date:
  validation_method: "mixed_session | role_specific_sessions | async_views"
  governance_resolution_method: "same_session | targeted_follow_up | async_decision_log"
  organizational_intelligence_object_shared: false
  broad_org_reinterview_required: false
  views_shared:
    - view_id:
      audience_role:
      included_object_ids:
        -
      excluded_sensitive_objects:
        -
  participants:
    - participant_id:
      role:
      validation_scope:
      governance_resolution_scope:
  validation_status: "validated | corrected | disputed | incomplete"
  governance_resolution_status: "resolved | partially_resolved | disputed | blocking"

confirmed_objects:
  - object_id:
    object_type:
    confirmed_by_role:
    confidence:

corrections:
  - object_id:
    object_type:
    issue:
    corrected_value:
    corrected_by_role:
    evidence_or_rationale:
    confidence:

disputed_items:
  - object_id:
    object_type:
    dispute:
    participants_or_roles_disagreeing:
      -
    follow_up_needed:

governance_resolutions:
  - object_id:
    object_type: "information_object | source_access_profile | truth_production_profile | source | system | field | decision | approval_gate | output"
    linked_workflow_object_ids:
      -
    linked_information_object_ids:
      -
    practical_access_path:
    module_report_view_or_path:
    lookup_keys:
      -
    required_fields_or_attributes:
      -
    current_access_roles:
      -
    alternate_locations:
      -
    official_source:
    official_source_status: "confirmed | candidate | disputed | missing | not_applicable | unknown"
    de_facto_trusted_source:
    de_facto_source_status: "confirmed | candidate | disputed | missing | not_applicable | unknown"
    truth_status: "authoritative | conditionally_reliable | shadow_derived | manually_adjusted | person_dependent | disputed | missing | not_reproducible | unknown"
    truth_production_chain_confirmed: false
    embedded_rules_or_macros:
      -
    manual_adjustments_or_reconciliations:
      -
    reproducibility: "high | medium | low | unknown"
    auditability: "high | medium | low | unknown"
    truth_owner_role_or_person:
    truth_steward_or_knower_role_or_person:
    ai_safe_truth_usage:
      allowed_uses: []
      prohibited_uses: []
      required_human_review_when: []
    owner_role_or_person:
    steward_role_or_person:
    sensitive_fields_or_content:
      -
    data_quality_notes:
      -
    retention_or_handling_rule:
    access_constraints:
      -
    allowed_ai_actions:
      - "read"
      - "summarize"
      - "compare"
      - "draft"
    prohibited_ai_actions:
      - "send_external"
      - "write_back"
    decided_by_role:
    decision_evidence_refs:
      -
    confidence:

unresolved_governance_items:
  - item_id:
    object_id:
    object_type: "information_object | source_access_profile | truth_production_profile | source | system | field | decision | approval_gate | output"
    decision_needed:
    why_unresolved:
    authorized_resolver_needed:
    blocks_readiness:
    later_route_if_unresolved: "formal_data_governance_project | knowledge_capture | measurement_intelligence | risk_register | zero_trust_controls | architecture_blueprint"

new_unknowns:
  - unknown_id:
    question:
    blocks_next_step:
    owner_candidate:
    later_step_required:

next_enrichment_routes:
  - route:
    reason:
    owner_candidate:
    priority:

back_edge_decisions:
  update_workflow_object_step6:
    required: false
    reason:
    affected_object_ids: []
  rerun_diagnostic_step7:
    required: false
    reason:
    affected_finding_ids: []
    blocker_classification_changes: []
  update_candidate_shortlist_step2:
    required: false
    reason:
    affected_candidate_use_case_ids: []
  return_to_interviews_step3_or_variation_step4:
    required: false
    reason:
    affected_roles_or_variants: []
  continue_forward:
    allowed: true
    conditions:
      -
```

## Decisions

- Validated enough to continue:
- Governance resolved enough to continue:
- Corrections required before continuing:
- Step 6 workflow object update required:
- Step 7 diagnostic re-score required:
- Step 2 shortlist update required:
- Blocking unresolved governance decisions:
- Additional interviews needed:
- Additional planning-evidence follow-up needed:
- Next enrichment steps:

## Notes

- The canonical internal reference remains the AI workflow specification and diagnostic.
- Human validation views are controlled excerpts, not the full organizational intelligence model.
- Source, truth production, owner, sensitivity, access, retention, and permitted-AI-action decisions should be resolved here whenever possible.
- Information object and source access path corrections should be resolved here whenever possible.
- If validation changes material workflow objects, truth production profiles, source access paths, candidate viability, or blocker classification, update Step 6 and re-score Step 7 before moving forward.
- If too many core objects are disputed, return to interviews, planning-evidence follow-up, or org-structure clarification before knowledge/risk/readiness work.

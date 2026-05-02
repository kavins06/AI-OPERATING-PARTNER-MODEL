# Method-To-Build Handoff Contract

`handoff_contract_id`: `method_to_build_handoff`  
`applies_after_step`: `18`  
`status`: `published_reference`

This contract defines what transfers after the pre-build engagement and what does not. It prevents the end of Step 18 from becoming an ambiguous "now go build it" moment.

## Handoff Boundary

The engagement ends with an approved Step 17 packet and Step 18 lifecycle object. It does not itself start implementation.

Implementation begins only when:

1. Step 18 is approved;
2. the client approves a separate implementation phase;
3. the future build owner accepts the handoff package;
4. required security, legal, IT, data, and business approvals are obtained;
5. future access requests are approved through the client's process.

## What Transfers

The handoff package should include:

- implementation decision packet;
- managed lifecycle, remediation lifecycle, or no-automation review cadence;
- workflow intelligence object or approved build-team view;
- organizational intelligence baseline exports relevant to the selected scope;
- guidance packs and eval cases;
- measurement intelligence and AI-capability metrics;
- technical/vendor blueprint;
- future component contracts;
- future access request package;
- normalization and truth remediation plan;
- risk/control model;
- owner matrix;
- launch gates and monitoring plan;
- halt taxonomy events and unresolved blockers;
- offline proof results if any.

## What Does Not Transfer

The handoff must not include:

- employee credentials;
- production API tokens;
- live secrets;
- broad unredacted transcripts unless separately approved;
- all-email access;
- unapproved bulk data extracts;
- implicit authority to write to production systems;
- implementation permission beyond the approved scope.

## Owner Model

Every handoff must name:

- client sponsor;
- business owner;
- day-to-day owner;
- future build owner;
- technical owner;
- data owner;
- security owner;
- risk/compliance owner;
- guidance update owner;
- measurement owner;
- incident owner;
- revocation owner;
- operating partner role after handoff.

The operating partner role after handoff must be one of:

- `advisor_only`
- `build_phase_operator`
- `managed_services_owner`
- `client_handoff_only`
- `third_party_builder_handoff`
- `not_decided`

## Build Phase Entry Criteria

Before build starts:

- Step 17 packet type is build-ready or remediation plan is complete and reassessed.
- Step 18 lifecycle variant is approved.
- Future access requests are approved but not yet over-scoped.
- Test data or sandbox path is available.
- Controls, logs, and revocation path are accepted as implementation requirements.
- Build owner accepts stop conditions.
- Client confirms what behavior level is authorized for first build.

## Triggers For Return To Method

Return to the method framework or rerun affected steps when:

- material truth production changes;
- source system, vendor, API, or data license changes;
- regulated-domain rule or client legal policy changes;
- intended behavior expands to recommendation, action, send, write-back, or autonomy;
- new user group, workflow, geography, or business unit is added;
- kill criteria are breached during build or pilot;
- adoption-failure trigger is breached;
- a material risk event occurs;
- required owner leaves or ownership changes;
- the build team discovers a missing workflow, source, truth chain, or control that changes readiness.

## Handoff Acceptance Checklist

- Step 17 packet accepted by sponsor.
- Step 18 lifecycle object accepted by owner forum.
- Build owner accepts scope and non-goals.
- Security/risk/legal accepts future controls and access path.
- Data/system owners accept future access and source constraints.
- Business owner accepts adoption, review, and success metrics.
- Operating partner role after handoff is named.
- Re-entry triggers are acknowledged.

## Handoff Status

Use one:

- `ready_for_separate_implementation_approval`
- `ready_for_remediation_execution`
- `not_ready_missing_owner`
- `not_ready_missing_controls`
- `not_ready_missing_access_path`
- `not_ready_pending_client_decision`
- `do_not_automate_revisit_scheduled`

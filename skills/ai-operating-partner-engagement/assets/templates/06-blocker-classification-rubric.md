# Blocker Classification Rubric

`rubric_id`: `blocker_classification`
`applies_to_step`: `7`
`status`: `published_reference`

Use this rubric when Step 7 classifies diagnostic findings. The point is not to remove operator judgment. The point is to make operator judgment comparable across engagements.

## Classification Options

### `fatal_for_use_case`

Use when the finding makes the candidate use case unsuitable as framed.

Criteria:

- The finding blocks the intended outcome or target behavior, not just implementation detail.
- The required remediation is out of scope, out of client appetite, too slow, or would change the use case into a different one.
- The finding creates unacceptable legal, safety, financial, reputational, or trust risk for the proposed behavior.
- The candidate cannot be narrowed to a safe-limited behavior that still has meaningful value.

Examples:

- A proposed autonomous resident-message workflow cannot satisfy Fair Housing or legal-review controls.
- No one owns the decision the agent would support and the client will not assign an owner.
- The workflow is too fragmented to model and the client will not allow variation mapping or sampling expansion.

Route:

- Update candidate shortlist with `discovery_disqualification`.
- Route to Step 2 update or Step 17 `do_not_automate_recommendation` if already late in the process.

### `requires_remediation_before_build`

Use when the opportunity remains real, but a fix is required before build-ready recommendation.

Criteria:

- The finding is fixable with named owner, evidence, and completion criteria.
- The use case can wait for remediation.
- Safe-limited behavior may be possible, but the intended behavior is not safe yet.
- The fix is concrete enough to become a Step 17 remediation plan.

Examples:

- The final KPI is produced by an Excel macro and needs formula documentation and owner assignment.
- Required source access path is plausible but needs IT/vendor confirmation.
- Tacit expert rules need capture before recommendation support.

Route:

- Continue only for safe-limited analysis or remediation planning.
- Route to Step 17 `governance_data_readiness_plan`, `knowledge_capture_plan`, `technical_feasibility_plan`, or `gap_remediation_plan`.

### `acceptable_with_controls`

Use when the finding creates risk or limitation, but controls can make the selected behavior safe.

Criteria:

- The risk is material but bounded.
- Required control is known, testable, and owner-confirmed.
- The behavior can be narrowed without destroying value.
- Evidence supports the control path.

Examples:

- Two reports conflict, but AI is only asked to compare them and flag uncertainty.
- Source data is stale by one day, but the output is a summary with freshness disclosure.
- External message drafts require human approval before send.

Route:

- Continue with explicit Step 10 guidance, Step 15 controls, and Step 16 behavior-level limits.

### `informational`

Use when the finding matters for understanding the organization but does not materially affect the candidate use case, readiness, control design, or adoption path.

Criteria:

- Finding is useful context but not a blocker.
- No immediate remediation is needed.
- It may inform future process improvement or later opportunities.

Examples:

- A report is duplicated in another dashboard, but the selected workflow does not depend on it.
- A handoff is annoying but low-risk and outside the candidate boundary.

Route:

- Preserve as organizational intelligence.
- Do not let it expand scope unless later evidence changes materiality.

## Tie-Break Rules

- If a finding blocks autonomous action but allows safe summarization, classify the blocker against the blocked behavior level, not the entire opportunity.
- If truth is fragile and the intended behavior is recommendation, action, send, write-back, or approval, default to `requires_remediation_before_build` unless the use case has no valuable safe-limited version. Then use `fatal_for_use_case`.
- If regulated-domain controls are unknown, use `requires_remediation_before_build` until legal/compliance confirms controls. Use `fatal_for_use_case` if the client cannot or will not provide controls.
- If adoption reality makes the user group unreachable, use `fatal_for_use_case` for that target user group or revise scope.
- If evidence confidence is low, classify as `requires_remediation_before_build` or `needs_more_discovery`; do not classify as `acceptable_with_controls` without evidence that controls are viable.

## Required Fields On Every Classified Finding

- `finding_id`
- linked workflow/object IDs
- evidence references
- confidence
- blocker classification
- behavior levels affected
- owner candidate
- route
- required fix or control
- whether candidate shortlist update is required

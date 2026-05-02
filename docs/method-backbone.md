# Method Backbone

This repo defines a method workbench for enterprise modernization. It is the source of truth for the engagement sequence, structured artifacts, decision gates, and handoff contracts that a future webapp should implement.

## System Shape

The method has four layers:

1. Principles: the modernization philosophy and boundaries.
2. Process: Step 0 plus Steps 1-18, grouped into seven umbrellas.
3. Contracts: schemas, templates, rubrics, scoring logic, and halt rules.
4. Handoff: decision packets and lifecycle objects that define what a separate build phase may implement.

## Seven Umbrellas

1. Frame And Hypothesize: Steps 0-2.
2. Discover Reality: Steps 3-5.
3. Build And Validate The Intelligence Layer: Steps 6-8.
4. Define AI Reasoning Requirements: Steps 9-10.
5. Prove Measurement And Value: Steps 11-12.
6. Shape The Future Solution: Steps 13-15.
7. Decide And Govern: Steps 16-18.

## Artifact Flow

```mermaid
flowchart LR
  A["Executive terrain and candidate use cases"] --> B["Interviews, variation, and evidence needs"]
  B --> C["Workflow intelligence object"]
  C --> D["Organizational intelligence diagnostic"]
  D --> E["Validated baseline"]
  E --> F["Knowledge, guidance, and eval requirements"]
  F --> G["Measurement and business value"]
  G --> H["Solution, technical, adoption, and risk design"]
  H --> I["Readiness object"]
  I --> J["Implementation decision packet"]
  J --> K["Managed lifecycle and handoff"]
```

## Operating Boundary

The method ends at an approved Step 18 handoff. The future build phase may then implement an app, agent, workflow automation, connector, MCP server, normalization pipeline, or integration if the approved packet and lifecycle authorize it.

During the method engagement, the system may run offline proof points using approved redacted, synthetic, or historical examples. These proofs support evidence, guidance, evals, and readiness decisions. They are not production implementation.

## What The Future App Should Operationalize

The app should make the method repeatable:

- Guided step execution with explicit gates and loopbacks.
- Interview capture, evidence logging, and source traceability.
- Structured object editors for workflow intelligence, baselines, guidance packs, readiness objects, decision packets, and lifecycle objects.
- Validation workflows for sponsors, operators, data owners, technical owners, risk owners, and remediation owners.
- Scoring, comparison, disqualification, and halt/revisit workflows.
- Exportable packets and build-phase handoff packages.

## What Must Stay Stable

- The pre-build boundary.
- Evidence-linked object creation.
- Behavior-level readiness.
- Hard-gate readiness logic.
- Vertical-extension protocol.
- Step 17 packet contracts.
- Step 18 lifecycle and handoff contracts.

The app may improve ergonomics, collaboration, review, and reporting. It should not weaken those invariants.

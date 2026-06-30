# Vertical Extension Guide

The core method is vertical-agnostic. Domain specificity enters through the vertical-extension contract, not through ad hoc edits to the core process.

## Extension Contract

The schema lives at `skills/ai-operating-partner-engagement/assets/templates/vertical-extension.schema.yaml`. A vertical extension defines:

- Regulated entities and why they matter.
- Named rules and when they apply.
- Prohibited AI behaviors.
- Required human review.
- Required evidence.
- Knowledge requirements.
- Guidance and eval requirements.
- Risk and control requirements.
- Lifecycle requirements.

The worked real-estate extension lives at `skills/ai-operating-partner-engagement/assets/templates/regulated-domain-extension-real-estate.yaml`.

## When To Add A Vertical Extension

Create an extension when a domain has material constraints that change:

- What knowledge must be captured.
- Which outputs are forbidden or require human review.
- Which evidence is required before recommendations are safe.
- Which controls, owners, or review cadence are mandatory.
- Which behavior levels are prohibited or conditional.

Examples include real estate, healthcare, financial services, insurance, legal operations, procurement, HR, logistics, and energy.

## Extension Principles

1. Do not fork the method for each vertical.
2. Add domain-specific rules through the extension object.
3. Keep named regulations, policies, or rules traceable to owner confirmation.
4. Route domain knowledge into Step 9 and Step 10.
5. Route domain risk into Step 15.
6. Route lifecycle cadence, owner, and revalidation requirements into Step 18.
7. Record missing domain inputs as blockers or conditional gates, not as assumptions.

## App Implications

A future app should let an operator select one or more vertical extensions during Step 0. The selected extensions should automatically influence interview prompts, evidence needs, guidance requirements, risk controls, readiness gates, packet content, and lifecycle review cadence.

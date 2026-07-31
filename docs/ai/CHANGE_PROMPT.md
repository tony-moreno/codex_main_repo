---
status: active
artifact: ai-contract
last_updated: 2026-07-31
---

# Change Impact Contract

A change has been proposed. Evaluate it against the current repository before editing artifacts or code.

## Determine whether the change affects

- Vision or Principles
- ontology
- relationships
- player experience
- gameplay loop or terminal language
- use cases
- requirements
- architecture
- implementation
- tests
- traceability
- accepted decisions
- task ordering or branch scope

## For every affected artifact, provide

- what changes;
- why it changes;
- downstream impact;
- migration or compatibility concerns;
- tests that must be added or revised.

## Rules

- Do not modify unaffected artifacts merely for consistency theater.
- Identify conflicts with accepted decisions explicitly.
- Distinguish a clarification from a behavioral change.
- Keep the active capability bounded.
- Record newly rejected alternatives in `DECISIONS.md` when the rejection will matter later.
- Update traceability in the same change that updates behavior.

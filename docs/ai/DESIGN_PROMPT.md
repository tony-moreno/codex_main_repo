---
status: active
artifact: ai-contract
last_updated: 2026-07-31
---

# Design Proposal Contract

Use this contract whenever proposing a new capability, mechanic, entity, process, or substantial interaction.

## Required response

1. **Intent** — State the User experience or project outcome being pursued.
2. **Assumptions** — Identify facts being treated as true but not yet settled.
3. **Existing fit** — Identify the current principles, entities, processes, resources, capabilities, or constraints being extended.
4. **Affected ontology** — Describe what exists or behaves differently.
5. **Player experience** — Describe what the User should perceive, feel, decide, or learn.
6. **Use case** — Define the smallest meaningful interaction.
7. **Requirements** — Write atomic, observable behaviors with identifiers.
8. **Architecture impact** — Identify responsibilities and boundaries, not speculative class lists.
9. **Implementation impact** — Identify the smallest code surface likely to change.
10. **Tests** — Explain how each requirement will be verified.
11. **Traceability** — Show the chain from intent to tests.
12. **Exclusions** — State what the proposal intentionally does not include.
13. **Unresolved questions** — List only questions that materially affect the design.

## Guardrails

- Do not skip directly from idea to implementation.
- Do not create a new subsystem when an existing rule can be extended.
- Do not confuse content volume with capability depth.
- Do not prescribe the User's ultimate objective.
- Do not make runtime AI an implicit solution.

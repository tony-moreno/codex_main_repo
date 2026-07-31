---
status: governing
artifact: principles
last_updated: 2026-07-31
---

# Principles

These principles are constitutional. Proposed features, mechanics, architecture, and implementation should be tested against them.

## Game design

1. **Knowledge compounds.** Earlier understanding should continue creating value.
2. **Discovery is more rewarding than leveling.** Progress comes from learning what is possible and why.
3. **Understanding precedes capability.** The User should usually learn enough to act before receiving a new power.
4. **Information is earned.** The world does not reveal itself merely because the User wants an answer.
5. **Complexity emerges from simple rules.** Prefer reusable primitives over handcrafted outcomes.
6. **Capabilities are composable.** A capability should become material for later invention.
7. **Physics should feel intuitive rather than academic.** Consequences matter more than equations displayed for their own sake.
8. **The world exists independently of the User.** Discovery changes the User's model, not the underlying universe.
9. **Every command answers a meaningful question or attempts a meaningful action.** Avoid decorative terminal interactions.
10. **Every mechanic supports the fantasy.** Curiosity, survival, creation, autonomy, and civilization remain central.
11. **Ethics emerge through behavior.** Do not reduce the User's trajectory to a morality selector.
12. **Consequences persist.** Creation should alter resources, relationships, risks, and future possibilities.

## Project design

13. **The repository is the source of truth.** Conversations are temporary; project artifacts must be reloadable.
14. **The AI is a collaborator, not the author.** It preserves intent, exposes assumptions, and assists implementation.
15. **Runtime AI is not an initial dependency.** Any future LLM integration requires its own explicit capability and decision record.
16. **Implementation follows the model.** Ontology informs experience; experience informs use cases; requirements inform architecture; architecture informs code and tests.
17. **Traceability stays alive.** Every implemented behavior must connect back to intent.
18. **Develop one coherent vertical slice at a time.** Capability branches should remain bounded.
19. **Never develop directly on `main`.** `main` represents integrated, working milestones.
20. **Prefer honest incompleteness over invented certainty.** Mark unresolved content clearly instead of filling space with speculation.

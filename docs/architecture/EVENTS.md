---
status: placeholder
artifact: architecture
last_updated: 2026-07-31
---

# Events

Events represent meaningful facts that have occurred and may affect world state, knowledge, behavior, tests, or later replay.

## Candidate event families

- observation received;
- command attempted;
- process started, completed, or failed;
- knowledge revised;
- resource consumed or produced;
- entity created, damaged, repaired, or destroyed;
- communication sent or received;
- trust or resistance changed.

No domain-event architecture is required for `CAP-001`. Add one only when a capability benefits from explicit event history or decoupled reactions.

---
status: active
artifact: implementation
last_updated: 2026-07-31
---

# Test Strategy

Tests verify requirements; they do not merely exercise code paths.

## Levels

- **Unit tests:** Verify deterministic logic and formatting in isolation.
- **Application tests:** Verify a use case across collaborating modules without requiring a real external service.
- **CLI tests:** Verify documented launch and observable terminal behavior.
- **Simulation tests:** Later verify invariants, state transitions, and consequences across time.
- **Acceptance tests:** Demonstrate that a capability satisfies its use case and requirements.

## First capability

`CAP-001` should verify at minimum:

- the documented entry point can be invoked in the supported environment;
- the expected in-world greeting is emitted;
- a visible prompt is emitted after the greeting;
- output does not depend on network access or a runtime LLM;
- tests do not block waiting for interactive input.

## Traceability rule

Name or annotate tests so `REQ-###` identifiers can be found from the test suite and [TRACEABILITY.md](../requirements/TRACEABILITY.md).

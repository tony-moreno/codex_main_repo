---
status: seed
artifact: architecture
last_updated: 2026-07-31
---

# Package Model

The repository separates project knowledge, executable logic, launchers, and verification.

```text
project-root/
├── docs/      # model, requirements, decisions, prompts, and working context
├── src/       # Python package and domain/application logic
├── bin/       # thin launchers and developer utilities
└── tests/     # automated verification mapped to requirements
```

## Rules

- Game and domain logic belongs under `src/`.
- `bin/` must remain thin and delegate to package code.
- Tests should import package behavior rather than test copied launcher logic.
- Documentation changes accompany behavior changes.
- Package boundaries should follow responsibilities discovered through capabilities, not speculative subsystem diagrams.

## First capability

The `hello-game-world` branch may establish the initial Python package and command entry point. Exact package naming remains an implementation decision for that branch.

---
status: seed
artifact: architecture
last_updated: 2026-07-31
---

# Package Model

The repository separates project knowledge, a canonical launch script, executable logic, installation/development tooling, and verification.

```text
project-root/
├── docs/      # model, requirements, decisions, prompts, and working context
├── terminal-sci-fi-game.py # canonical launch script
├── src/       # terminal-sci-fi-game package and domain/application logic
├── bin/       # installers and installation/development tools
└── tests/     # automated verification mapped to requirements
```

## Rules

- Game and domain logic belongs under `src/`.
- `terminal-sci-fi-game.py` must remain thin and delegate to package code.
- `bin/` must not contain the game launcher or game behavior.
- Tests should import package behavior and separately verify the canonical launch script.
- Documentation changes accompany behavior changes.
- Package boundaries should follow responsibilities discovered through capabilities, not speculative subsystem diagrams.

## First capability

The `hello-game-world` branch establishes the `terminal-sci-fi-game` package for Python 3.11 and later, plus the canonical `python terminal-sci-fi-game.py` launch command.

---
status: active
artifact: implementation
last_updated: 2026-07-31
---

# Coding Guidelines

## Python

- Target a currently supported Python 3 release and record the exact minimum in `pyproject.toml` when implementation begins.
- Prefer clear modules, functions, and data structures over speculative frameworks.
- Use type hints for public interfaces and meaningful internal boundaries.
- Keep deterministic game logic separate from terminal input/output.
- Keep launchers thin.
- Raise or return explicit errors rather than silently ignoring invalid state.
- Avoid global mutable state.
- Add dependencies only when they remove more complexity than they introduce.

## Design alignment

- Do not implement behavior without a use case and requirement.
- Do not encode lore where a reusable world rule belongs.
- Keep truth separate from the User's knowledge of truth.
- Prefer composable primitives over enumerated outcomes.
- Do not add runtime AI or network dependencies without an accepted decision record and dedicated capability.

## Quality

- Format and lint consistently once tools are selected.
- Test observable behavior.
- Name tests after requirements or scenarios.
- Keep commits small enough to review and reverse.

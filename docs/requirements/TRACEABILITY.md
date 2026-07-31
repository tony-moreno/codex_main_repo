---
status: active
artifact: requirements
last_updated: 2026-07-31
---

# Traceability

Traceability connects project intent to verified behavior.

## Current chain

```text
VISION
└── PRINCIPLES
    └── CAP-001 — Greet User
        └── UC-001 — Greet User through the game terminal
            ├── REQ-001 — Documented launch command
            ├── REQ-002 — In-world greeting
            ├── REQ-003 — Visible terminal prompt
            ├── REQ-004 — Automated output verification
            ├── REQ-005 — No runtime AI or network dependency
            └── REQ-006 — Static until keyboard entry
```

## Planned implementation trace

| Requirement | Architecture | Implementation | Test | Status |
|---|---|---|---|---|
| REQ-001 | Package and entry-point model | `terminal-sci-fi-game.py`, `src/terminal_sci_fi_game/cli.py` | `test_req_001_req_004_req_006_launcher_is_static_until_keypress` | Implemented |
| REQ-002 | Terminal presentation responsibility | `src/terminal_sci_fi_game/splash.py`, `src/terminal_sci_fi_game/cli.py` | `test_req_002_and_req_003_render_greeting_and_prompt` | Implemented |
| REQ-003 | Terminal presentation responsibility | `src/terminal_sci_fi_game/splash.py`, `src/terminal_sci_fi_game/cli.py` | `test_req_002_and_req_003_render_greeting_and_prompt` | Implemented |
| REQ-004 | Test strategy | `tests/test_hello_game_world.py` | CAP-001 automated test suite | Implemented |
| REQ-005 | DEC-002 | `pyproject.toml`, `src/terminal_sci_fi_game/` | `test_req_005_runtime_has_no_network_or_ai_dependencies` | Implemented |
| REQ-006 | Use-case lifecycle responsibility | `src/terminal_sci_fi_game/terminal.py`, `src/terminal_sci_fi_game/cli.py` | `test_req_006_output_does_not_change_while_waiting` and launcher acceptance test | Implemented |

Update this table in the same merge request that introduces or changes behavior.

---
status: active
artifact: requirements
last_updated: 2026-07-31
---

# Use Cases

Use cases describe meaningful interactions from the User's perspective. Keep them small enough to implement as coherent vertical slices.

## UC-001 — Greet User through the game terminal

**Primary actor:** User

**Goal:** Confirm that the game has launched and is ready to receive input.

**Preconditions:**

- Python and project dependencies are available.
- The repository has been checked out on a supported environment.

**Trigger:**

- The User launches the game from the repository root using the canonical script:

```text
python terminal-sci-fi-game.py
```

**Main success scenario:**

1. The application starts successfully.
2. The application displays an in-world greeting.
3. The application displays a visible terminal prompt.
4. The application remains static until the User presses any keyboard entry.
5. After that entry, the application remains in a valid state suitable for later command-input development; interpreting the entry is out of scope.

**Success condition:**

- The User can see that the game is running and ready for input.

**Out of scope:**

- interpreting or executing a command;
- dynamic narrative generation;
- research, resources, saving, loading, or world simulation;
- configurable identity or settings.

**Capability:** `CAP-001 — Greet User`

**Implementation branch:** `hello-game-world`, branched from `capability`

**Status:** Defined; not implemented.

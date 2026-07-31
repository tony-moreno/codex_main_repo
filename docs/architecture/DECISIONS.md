---
status: active
artifact: architecture
last_updated: 2026-07-31
---

# Decisions

Record major choices and rejected alternatives so future collaborators do not unknowingly restart settled debates.

## DEC-001 — The repository is the source of truth

**Status:** Accepted

**Decision:** Project knowledge must live in version-controlled artifacts that can onboard a new human or AI collaborator without relying on prior chat history.

**Rejected:** Treating one giant prompt or one conversation as authoritative.

**Reason:** Conversations are temporary, difficult to diff, and unable to preserve traceability as the project grows.

## DEC-002 — Runtime AI is not an initial dependency

**Status:** Accepted

**Decision:** AI assists project development through the repository. The initial game remains deterministic, offline-capable, and testable without an LLM or network service.

**Rejected:** Making natural-language generation or command interpretation dependent on a hosted model from the beginning.

**Reason:** Runtime AI would obscure the game's actual mechanics and introduce cost, availability, nondeterminism, and testing concerns before the core experience is proven.

## DEC-003 — Development uses capability branches

**Status:** Accepted

**Decision:** Never develop directly on `main`. Branch the shared `capability` integration branch from `main`; branch coherent use-case slices such as `hello-game-world` from `capability`; merge satisfactory slices back into `capability`; and merge reviewed collections from `capability` into `main` through GitLab merge requests.

**Rejected:** Long-lived layer branches such as `docs`, `parser`, or `database`, and direct commits to `main`.

**Reason:** Capability branches align documentation, architecture, implementation, and tests around one player-visible milestone.

## DEC-004 — Game logic belongs under `src/`

**Status:** Accepted

**Decision:** `terminal-sci-fi-game.py` at the repository root is the canonical thin launcher. `bin/` contains only installers and installation/development tools. Reusable application and domain logic belongs under `src/terminal_sci_fi_game/`.

**Rejected:** Placing the game launcher or full implementation under `bin/`.

**Reason:** Separating the canonical launch script, package logic, and installation tooling improves testing, reuse, packaging, and maintainability.

## DEC-005 — The first slice is `hello-game-world`

**Status:** Accepted

**Decision:** The first implementation capability launches the application, greets the User in-world, and presents a terminal prompt.

**Rejected:** Beginning with command parsing, research systems, resources, save files, or world simulation.

**Reason:** The smallest complete slice proves the repository method, Python execution path, testing approach, and traceability before the design surface expands.

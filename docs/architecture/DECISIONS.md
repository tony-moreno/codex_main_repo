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

**Decision:** Never develop directly on `main`. Develop coherent vertical slices in branches named `capability/<short-name>` and merge through GitLab merge requests.

**Rejected:** Long-lived layer branches such as `docs`, `parser`, or `database`, and direct commits to `main`.

**Reason:** Capability branches align documentation, architecture, implementation, and tests around one player-visible milestone.

## DEC-004 — Game logic belongs under `src/`

**Status:** Accepted

**Decision:** `bin/` contains only thin launchers and developer utilities. Reusable application and domain logic belongs under `src/`.

**Rejected:** Placing the full implementation under `bin/`.

**Reason:** Separating launchers from package logic improves testing, reuse, packaging, and maintainability.

## DEC-005 — The first slice is `hello-game-world`

**Status:** Accepted

**Decision:** The first implementation capability launches the application, greets the User in-world, and presents a terminal prompt.

**Rejected:** Beginning with command parsing, research systems, resources, save files, or world simulation.

**Reason:** The smallest complete slice proves the repository method, Python execution path, testing approach, and traceability before the design surface expands.

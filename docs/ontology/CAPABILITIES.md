---
status: active
artifact: ontology
last_updated: 2026-07-31
---

# Capabilities

A capability describes what possessing a combination of knowledge, resources, entities, and processes allows an actor to accomplish.

Capabilities should be composable primitives rather than isolated rewards.

## Candidate game capabilities

- Scanning
- Communication
- Navigation
- Mining
- Manufacturing
- Storage
- Computation
- Research
- Repair
- Replication
- Life support
- Coordination and influence

## Initial project capability

### CAP-001 — Greet User

**Intent:** Demonstrate that the game can launch, address the User in-world, and present a terminal prompt.

**Allows:**

- starting the game through a documented command;
- displaying a deterministic greeting;
- displaying a visible input prompt.

**Does not allow:**

- interpreting commands;
- performing research;
- saving or loading;
- simulating a world;
- configuring identity;
- calling a runtime language model.

**Planned branch:** `capability/hello-game-world`

**Status:** Defined; not implemented on baseline `main`.

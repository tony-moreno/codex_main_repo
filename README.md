# Terminal Sci-Fi Game

A model-driven Python command-line science-fiction game project where curiosity becomes knowledge, knowledge becomes capability, and capability becomes creation.

The repository is the source of truth for both human and AI collaborators. Design intent, ontology, player experience, requirements, architecture, implementation, and tests remain traceable as the game grows.

> This project is inspired by broad science-fiction ideas about machine intelligence, replication, exploration, and civilization. It is not affiliated with or based directly on the *Bobiverse* novels or Dennis E. Taylor.

## Current milestone

**Repository Baseline — `main`**

This commit establishes the project model, documentation structure, Git workflow, and the planned first vertical slice. It intentionally contains no game behavior.

The first implementation branch is:

```text
hello-game-world
```

Its single purpose is to implement `CAP-001`: launch the game, greet the User in-world, and present a terminal prompt.

## Launch

From the repository root with Python 3.11 or later:

```text
python terminal-sci-fi-game.py
```

The initial slice displays the terminal splash and remains static until one key is pressed. The key is acknowledged but not interpreted, and the application exits cleanly.

## Start here

1. Read [VISION.md](VISION.md).
2. Read [PRINCIPLES.md](PRINCIPLES.md).
3. Read [docs/ai/PROJECT_CONTEXT.md](docs/ai/PROJECT_CONTEXT.md).
4. Open [docs/HOME.md](docs/HOME.md) for the full repository map.
5. Review [docs/implementation/BRANCHING_STRATEGY.md](docs/implementation/BRANCHING_STRATEGY.md) before making changes.

## Repository layout

```text
project-root/
├── README.md
├── VISION.md
├── PRINCIPLES.md
├── CONTRIBUTING.md
├── docs/
├── src/
├── bin/
└── tests/
```

- `docs/` contains the Obsidian-compatible project model and AI collaboration contracts.
- `src/` will contain the `terminal-sci-fi-game` Python package and game/domain logic.
- `bin/` contains only installers and development tools needed to install or maintain the game.
- `tests/` verifies requirements and behavior.

## Working rule

Never develop directly on `main`. Develop individual use-case slices from the shared `capability` branch, merge satisfactory slices back into `capability`, and merge a reviewed collection of capabilities from `capability` into `main`.

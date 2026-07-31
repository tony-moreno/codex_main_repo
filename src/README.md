# Source Package

Executable Python package and reusable game/domain logic will live here.

The baseline `main` branch intentionally contains no implementation. The `terminal-sci-fi-game` package, supporting Python 3.11 and later, will be created on `hello-game-world`.

Rules:

- keep game logic out of `bin/`;
- separate deterministic behavior from terminal input/output;
- implement only behavior supported by active use cases and requirements;
- keep runtime AI and network services out of the first capability.

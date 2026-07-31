# Source Package

Executable Python package and reusable game/domain logic will live here.

The baseline `main` branch intentionally contains no implementation. The initial package will be created on `capability/hello-game-world` after its exact package name and Python version are selected.

Rules:

- keep game logic out of `bin/`;
- separate deterministic behavior from terminal input/output;
- implement only behavior supported by active use cases and requirements;
- keep runtime AI and network services out of the first capability.

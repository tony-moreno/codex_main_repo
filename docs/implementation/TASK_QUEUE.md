---
status: active
artifact: implementation
last_updated: 2026-07-31
---

# Task Queue

Only actionable work belongs here.

## Baseline `main`

- [ ] Initialize the local Git repository.
- [ ] Review repository names and replace any desired placeholders.
- [ ] Create the remote GitLab project.
- [ ] Commit this baseline to `main`.
- [ ] Push `main` to GitLab.
- [ ] Protect `main` and require merge requests.

## Next use-case slice — `hello-game-world`

- [x] Create `hello-game-world` from `capability`.
- [x] Select the `terminal-sci-fi-game` package name and Python 3.11+.
- [ ] Configure the package and canonical `python terminal-sci-fi-game.py` entry point.
- [ ] Implement deterministic in-world greeting output.
- [ ] Display the terminal prompt without interpreting input.
- [ ] Add automated tests for `REQ-001` through `REQ-006` as applicable, including verification that the application remains static before keyboard entry.
- [ ] Update package model, decisions, and traceability with actual paths.
- [ ] Open a GitLab merge request from `hello-game-world` into `capability`.
- [ ] After a coherent collection of capability work is integrated and reviewed, open a merge request from `capability` into `main`.

## Not yet scheduled

- terminal command interpretation;
- research mechanics;
- resource simulation;
- persistence;
- world generation;
- runtime AI integration.

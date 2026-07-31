# Contributing

This repository uses capability-based development with GitLab merge requests.

## Branch policy

- Do not develop directly on `main`.
- Create one branch per coherent capability.
- Use the naming pattern `capability/<short-name>`.
- Keep unrelated behavior out of the branch.
- Merge only through a merge request after documentation, implementation, tests, and traceability agree.

See [BRANCHING_STRATEGY.md](docs/implementation/BRANCHING_STRATEGY.md) for the detailed workflow.

## Change order

Before implementation:

1. State the intended player or project outcome.
2. Identify affected ontology and relationships.
3. Update player experience when relevant.
4. Define or update the use case.
5. Define atomic requirements.
6. Record architectural consequences.
7. Implement the smallest coherent behavior.
8. Test the requirements.
9. Update traceability and decision records.

## Commit style

Prefer small, understandable commits using conventional prefixes:

```text
docs: define hello game world capability
build: configure Python project entry point
feat: greet user through the game terminal
test: verify greeting and terminal prompt
refactor: separate prompt rendering from session state
```

## Definition of done

A capability is complete when:

- its scope and exclusions are explicit;
- affected documents are current;
- behavior is runnable;
- automated tests pass;
- traceability identifies implementation and tests;
- unresolved questions are recorded;
- the merge request contains no unrelated changes.

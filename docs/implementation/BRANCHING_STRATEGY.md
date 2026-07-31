---
status: governing
artifact: implementation
last_updated: 2026-07-31
---

# Branching Strategy

## Main branch

`main` represents integrated, reviewed, and working collections of capabilities.

- Protect `main` in GitLab.
- Do not develop directly on `main`.
- Require merge requests.
- Require passing automated tests once the pipeline exists.
- Prefer squash merges for small capability branches unless preserving individual commits adds real value.

## Integration branch

`capability` branches from `main` and integrates related, individually reviewed use-case slices. Once a coherent collection is satisfactory and all tests pass, merge `capability` into `main` through a merge request.

## Use-case branches

Branch each use-case slice from `capability`. Use:

```text
<short-kebab-case-name>
```

Examples:

```text
hello-game-world
terminal-prompt-interpretation
research-mechanic
```

Each branch should contain one coherent vertical slice across the artifacts it affects:

```text
intent → ontology/experience → use case → requirements → architecture → implementation → tests → traceability
```

## Suggested workflow

```bash
git switch capability
git pull --ff-only
git switch -c hello-game-world
# define, implement, test, and document
git push -u origin hello-game-world
# open GitLab merge request into capability
# after integrating a coherent collection, open a capability-to-main merge request
```

## Merge-request acceptance

A use-case or capability-collection merge request should answer:

- What can the User or project do after this merge that it could not do before?
- What is explicitly out of scope?
- Which use cases and requirements are satisfied?
- Which files implement and test them?
- Which decisions were made or rejected?
- What remains unresolved?

## Avoid

- use-case branches that combine multiple independent slices;
- direct hotfixes to `main` unless the repository is unusable and the change is documented immediately;
- implementation-only branches with traceability added later;
- refactors hidden inside feature work without explanation.

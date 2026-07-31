---
status: governing
artifact: implementation
last_updated: 2026-07-31
---

# Branching Strategy

## Main branch

`main` represents integrated, reviewed, and working milestones.

- Protect `main` in GitLab.
- Do not develop directly on `main`.
- Require merge requests.
- Require passing automated tests once the pipeline exists.
- Prefer squash merges for small capability branches unless preserving individual commits adds real value.

## Capability branches

Use:

```text
capability/<short-kebab-case-name>
```

Examples:

```text
capability/hello-game-world
capability/terminal-prompt-interpretation
capability/research-mechanic
```

Each branch should contain one coherent vertical slice across the artifacts it affects:

```text
intent → ontology/experience → use case → requirements → architecture → implementation → tests → traceability
```

## Suggested workflow

```bash
git switch main
git pull --ff-only
git switch -c capability/hello-game-world
# define, implement, test, and document
git push -u origin capability/hello-game-world
# open GitLab merge request into main
```

## Merge-request acceptance

A capability merge request should answer:

- What can the User or project do after this merge that it could not do before?
- What is explicitly out of scope?
- Which use cases and requirements are satisfied?
- Which files implement and test them?
- Which decisions were made or rejected?
- What remains unresolved?

## Avoid

- branches that combine multiple independent capabilities;
- direct hotfixes to `main` unless the repository is unusable and the change is documented immediately;
- implementation-only branches with traceability added later;
- refactors hidden inside feature work without explanation.

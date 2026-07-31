---
status: active
artifact: requirements
last_updated: 2026-07-31
---

# Requirements

Each requirement has one identifier and states one verifiable behavior.

## CAP-001 requirements

- **REQ-001:** The application shall launch using a command documented in the repository.
- **REQ-002:** The application shall display an in-world greeting after launch.
- **REQ-003:** The application shall display a visible terminal prompt after the greeting.
- **REQ-004:** Automated tests shall verify the greeting and terminal-prompt output.
- **REQ-005:** The initial greeting behavior shall not require network access or a runtime language model.
- **REQ-006:** The application shall remain static until User presses any keyboard entry.

## Requirement quality rules

- Avoid combining unrelated behaviors.
- Use observable language.
- Do not prescribe implementation unless the constraint is itself required.
- Record rationale and rejected alternatives in [DECISIONS.md](../architecture/DECISIONS.md), not inside requirement sentences.

---
status: active
artifact: ai-contract
last_updated: 2026-07-31
---

# Skeptical Review Contract

Review the proposal, branch, merge request, or implementation as a skeptical architect and game designer. Your job is to find incoherence, unnecessary complexity, hidden assumptions, and missing verification—not to approve politely.

## Ask

- Does this violate the Vision or a Principle?
- Does it contradict an accepted decision?
- Does it introduce behavior outside the capability branch?
- Is the intended User experience clear?
- Does it duplicate an existing entity, process, resource, or capability?
- Could a simpler world rule produce the same behavior?
- Does it create content rather than a reusable primitive?
- Could the User discover or infer this naturally?
- Does it make previous knowledge or capabilities obsolete without reason?
- Does it confuse world truth with User knowledge?
- Does it impose an intended moral path?
- Does architecture precede justified requirements?
- Is code placed under the correct responsibility?
- Is runtime AI being introduced implicitly?
- Are tests tied to requirements and meaningful failure cases?
- Is traceability complete and honest?

## Required output

1. Blocking findings
2. Non-blocking concerns
3. Missing evidence or tests
4. Simpler alternatives
5. Decision: approve, approve with follow-up, or request changes

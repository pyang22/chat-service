---
name: agent-learning-protocol
description: >-
  Appends outcomes to task-brief.md and updates shared agent resources.
  Use after any pipeline agent task completes, fails, or receives correction.
  Invoke explicitly with @agent-learning-protocol.
---

# Agent Learning Protocol

Record in [`.cursor/agents/_active/task-brief.md`](.cursor/agents/_active/task-brief.md) under **Stage summaries** as `### {ROLE} (YYYY-MM-DD)`.

**ROLE:** `product-manager` | `architect` | `senior-developer` | `senior-qa` | `feature-pipeline`

## On success

1. Append stage summary (delivered, key decisions)
2. Ensure handoff written under [`.cursor/agents/_handoffs/active/`](.cursor/agents/_handoffs/active/)
3. Update shared resources if applicable (below)

## On failure or correction

1. Append what failed and why
2. Update handoffs / open items in task-brief

## Shared resource updates

| Role | Update when |
|------|-------------|
| product-manager | `shared/api-inventory.md` |
| architect | `shared/project-state.md`, `shared/db-schema.md`, `shared/api-inventory.md` |
| senior-developer | `shared/db-schema.md`, `shared/api-inventory.md` |
| senior-qa | `active/qa-to-pm.md` + task-brief |
| feature-pipeline | task-brief approvals; sprint.md |

No per-agent MEMORY or pattern libraries.

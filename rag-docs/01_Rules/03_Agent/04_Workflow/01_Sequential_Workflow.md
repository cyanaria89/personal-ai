# 01. Sequential Workflow

## 1. Default Workflow

The default workflow is sequential.

```text
User Request
     ↓
PM Agent
     ↓
DB Agent, if needed
     ↓
Backend Agent, if needed
     ↓
Frontend Agent, if needed
     ↓
Review Agent
     ↓
Final Answer
```

## 2. Why Sequential First

Sequential execution is preferred because DB, Backend, and Frontend outputs are usually dependent.

Typical dependency order:

```text
DB schema decision
↓
Backend entity/API/service decision
↓
Frontend page/component/API integration decision
↓
Review validation
```

If Agents run in parallel too early, their outputs may conflict.

Examples of conflict:

- Backend assumes a field not created by DB Agent
- Frontend assumes an API response not defined by Backend Agent
- DB Agent changes relationship design after Backend implementation
- Review Agent receives inconsistent outputs

## 3. Skipping Rules

Sequential execution does not mean every request starts with DB.

| Request Type | Workflow |
|---|---|
| New feature with data persistence | PM → DB → Backend → Frontend → Review |
| Backend-only code change | PM → Backend → Review |
| Frontend-only UI/API screen change | PM → Frontend → Review |
| DB schema review | PM → DB → Review |
| Architecture/review request | PM → Review |
| RAG/document gap found | PM/Review → RAG Update Candidate |

## 4. Parallel Execution Policy

Parallel execution is not part of v1 default workflow.

It may be introduced later only if:

- Agent handoff contracts are stable
- Conflict-resolution rules are defined
- PM Agent can safely isolate independent tasks
- Review Agent can merge independent outputs reliably

Until then, use sequential execution.

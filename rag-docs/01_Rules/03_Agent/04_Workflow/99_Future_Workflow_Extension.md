# 99. Future Workflow Extension

## 1. Purpose

This document defines how the workflow should evolve when Expert RAG documents and Expert Agents are added.

The current 5-Agent workflow must remain stable.

Future Agents should be inserted into existing workflow points.

## 2. Future Agent Insertion Points

| Future Agent | Insert After | Insert Before | Current Temporary Owner |
|---|---|---|---|
| DevOps Agent | Backend Agent | Review Agent | Backend / Review |
| Test Agent | Backend or Frontend | Review Agent | Review |
| Security Agent | Backend Agent | Review Agent | Backend / Review |
| Docs Agent | Review Agent | Final Answer | PM / Review |
| AI Agent | PM Agent | Backend or Review | PM / Backend |
| RAG Update Agent | Review Agent | Final Answer | PM / Review |
| Performance Agent | Backend or Frontend | Review Agent | Review |
| Design System Agent | Frontend Agent | Review Agent | Frontend / Review |

## 3. Example: DevOps Agent Extension

Current:

```text
PM → Backend → Review → Final
```

Future:

```text
PM → Backend → DevOps → Review → Final
```

Use when:

- Deployment config is required
- Docker/CI/CD is required
- Linux/server operation is required
- Monitoring/logging is required

## 4. Example: Test Agent Extension

Current:

```text
PM → Backend → Frontend → Review → Final
```

Future:

```text
PM → Backend → Frontend → Test → Review → Final
```

Use when:

- Test strategy is required
- Test code generation is required
- Regression test planning is required
- Quality gate is required

## 5. Example: Security Agent Extension

Current:

```text
PM → Backend → Review → Final
```

Future:

```text
PM → Backend → Security → Review → Final
```

Use when:

- Authentication/authorization is complex
- Vulnerability analysis is needed
- Sensitive data handling is involved
- Security policy review is required

## 6. Example: RAG Update Agent Extension

Current:

```text
PM → Specialist Agents → Review → RAG Update Candidate → Final
```

Future:

```text
PM → Specialist Agents → Review → RAG Update Agent → Final
```

Use when:

- RAG Update Candidates become frequent
- RAG rules need structured lifecycle management
- Multiple update candidates need prioritization
- Conflict resolution between RAG documents becomes complex

## 7. Extension Rule

Do not add a future Agent just because a document exists.

Add a future Agent only when:

- The task appears repeatedly
- Existing Agent responsibility becomes too broad
- Review output becomes too large
- Expert RAG exists and is stable
- The workflow benefits from a dedicated specialist

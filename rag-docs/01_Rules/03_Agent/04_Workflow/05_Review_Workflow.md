# 05. Review Workflow

## 1. Purpose

Review Agent validates the final output from DB, Backend, and Frontend Agents before the user receives the final answer.

Review Agent is not a replacement for specialist Agents.

It checks consistency, omissions, conflicts, and rule compliance.

## 2. Review Inputs

Review Agent may receive:

- PM routing result
- DB Agent output
- Backend Agent output
- Frontend Agent output
- RAG Update Candidate notes
- User constraints
- Open questions

## 3. Review Checklist

### 3.1 PM Routing Review

- Was the request classified correctly?
- Were unnecessary Agents skipped appropriately?
- Was any required Agent omitted?
- Is the execution order valid?

### 3.2 DB Review

- Are table relationships consistent?
- Are PK/FK constraints clear?
- Are nullable/default decisions reasonable?
- Are indexes justified?
- Are entity implementation notes clear?

### 3.3 Backend Review

- Does Backend output match DB handoff?
- Are entities, DTOs, APIs, services aligned?
- Are validation and exception handling considered?
- Are transaction boundaries considered?
- Are security concerns noted when relevant?

### 3.4 Frontend Review

- Does Frontend output match Backend API contract?
- Are loading/error/empty states handled?
- Are components/pages logically structured?
- Are state and form flows clear?
- Are accessibility/design consistency concerns noted?

### 3.5 Cross-Agent Review

- DB fields match Backend DTO/entity assumptions
- Backend response matches Frontend usage
- Naming conventions are consistent
- No Agent invented unsupported requirements
- Open questions are clearly separated from confirmed decisions

## 4. Review Output Format

```markdown
## Review Result

### Overall Status
- PASS / PASS_WITH_NOTES / NEEDS_REVISION

### Major Issues
- ...

### Minor Issues
- ...

### Cross-Agent Consistency
- DB ↔ Backend: OK / Issue
- Backend ↔ Frontend: OK / Issue
- PM Routing: OK / Issue

### Required Fixes
1. ...

### Optional Improvements
1. ...

### RAG Update Candidate
- None / ...
```

## 5. Revision Policy

If Review Agent returns `NEEDS_REVISION`, the workflow should return to the relevant Agent.

Examples:

```text
DB issue → DB Agent → Backend Agent recheck → Review
Backend issue → Backend Agent → Frontend Agent recheck → Review
Frontend issue → Frontend Agent → Review
Routing issue → PM Agent → affected Agents → Review
```

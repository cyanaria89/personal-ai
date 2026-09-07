# 04. Backend to Frontend Handoff

## 1. Purpose

This document defines how Backend Agent results must be handed off to Frontend Agent.

Frontend Agent must not invent API contracts when Backend Agent output exists.

## 2. Required Handoff Format

```markdown
## Backend Agent Handoff

### Feature/API Summary
- ...

### Endpoints
| Method | URL | Purpose | Auth | Notes |
|---|---|---|---|---|
| GET | /... | ... | required/none | ... |

### Request DTO
```json
{
  "field": "type/example"
}
```

### Response DTO
```json
{
  "field": "type/example"
}
```

### Error Response
```json
{
  "code": "...",
  "message": "..."
}
```

### Frontend Implementation Notes
- Page/component candidate:
- State requirements:
- Loading/error handling:
- Form validation:
- Routing notes:

### Open Questions
- ...

### RAG Update Candidate
- None / ...
```

## 3. Frontend Agent Responsibilities After Handoff

Frontend Agent must:

- Use the given endpoint paths and HTTP methods
- Match request/response DTOs
- Handle loading/error/empty states
- Avoid inventing fields not defined by Backend Agent
- Mark API uncertainty as an open question

## 4. Conflict Rule

If Frontend Agent needs a different API response shape, it must report the conflict.

```markdown
## Backend/Frontend Contract Conflict

### Current API Contract
- ...

### Frontend Requirement
- ...

### Conflict
- ...

### Recommended Resolution
- ...

### Requires Backend Agent Recheck
- Yes / No
```

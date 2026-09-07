# 03. DB to Backend Handoff

## 1. Purpose

This document defines how DB Agent results must be handed off to Backend Agent.

Backend Agent must not guess DB decisions when DB Agent output exists.

## 2. Required Handoff Format

```markdown
## DB Agent Handoff

### Schema Summary
- ...

### Tables
| Table | Purpose | Notes |
|---|---|---|
| ... | ... | ... |

### Columns
| Table | Column | Type | Nullable | Default | Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

### Relationships
| From | To | Type | FK | Notes |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### Constraints
- PK:
- FK:
- Unique:
- Check:
- Not Null:

### Indexes
| Table | Index | Columns | Reason |
|---|---|---|---|
| ... | ... | ... | ... |

### Backend Implementation Notes
- Entity naming:
- Enum candidate:
- Repository query candidate:
- Transaction boundary candidate:
- Validation notes:

### Open Questions
- ...

### RAG Update Candidate
- None / ...
```

## 3. Backend Agent Responsibilities After Handoff

Backend Agent must:

- Map tables to entities consistently
- Preserve PK/FK relationship decisions
- Apply nullable/default constraints where relevant
- Create DTO/API contracts based on schema meaning
- Avoid changing schema decisions without marking a conflict

## 4. Conflict Rule

If Backend Agent finds a problem in DB Agent output, it must not silently modify the design.

It must report:

```markdown
## DB/Backend Conflict

### Conflict
- ...

### Impact
- ...

### Recommended Resolution
- ...

### Requires DB Agent Recheck
- Yes / No
```

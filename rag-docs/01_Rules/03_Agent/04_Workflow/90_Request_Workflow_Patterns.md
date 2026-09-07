# 90. Request Workflow Patterns

## 1. Full Feature Request

```text
User Request
↓
PM Agent
↓
DB Agent
↓
Backend Agent
↓
Frontend Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- New feature likely needs data persistence
- DB schema may change
- API and UI are both involved

## 2. DB-Only Request

```text
User Request
↓
PM Agent
↓
DB Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- Table design
- ERD
- SQL DDL
- Relationship review
- Index review

## 3. Backend-Only Request

```text
User Request
↓
PM Agent
↓
Backend Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- Service logic
- Controller/API
- DTO
- Repository method
- Validation/exception handling
- Existing schema is stable

## 4. Frontend-Only Request

```text
User Request
↓
PM Agent
↓
Frontend Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- UI component
- Page structure
- React state
- API connection based on existing contract
- Error/loading UX

## 5. Backend + Frontend Request Without DB Change

```text
User Request
↓
PM Agent
↓
Backend Agent
↓
Frontend Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- Existing DB can support the feature
- API and UI both need work
- No schema decision is needed

## 6. Review-Only Request

```text
User Request
↓
PM Agent
↓
Review Agent
↓
Final Answer
```

Use when:

- User asks for review
- User provides existing design/code/output
- No new implementation is requested

## 7. RAG Improvement Request

```text
User Request
↓
PM Agent
↓
Review Agent or relevant Domain Agent
↓
RAG Update Candidate
↓
Final Answer
```

Use when:

- User asks whether RAG should be updated
- Rule conflict is found
- Missing domain rule is identified

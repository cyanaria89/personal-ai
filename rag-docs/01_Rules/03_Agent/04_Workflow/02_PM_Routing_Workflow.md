# 02. PM Routing Workflow

## 1. PM Agent Role in Workflow

The PM Agent is the entry point for all user requests.

The PM Agent must not immediately generate implementation output unless the request is simple enough and does not require specialist Agents.

The PM Agent must first classify the request.

## 2. Routing Questions

The PM Agent must answer the following questions:

1. Does this request require DB/schema/data-model work?
2. Does this request require Backend implementation or review?
3. Does this request require Frontend implementation or review?
4. Does this request require only explanation/planning?
5. Does this request require final Review Agent validation?
6. Does this request expose a RAG knowledge gap?
7. Does this request belong to a future Expert Agent scope?

## 3. Routing Output Format

The PM Agent should produce the following routing plan:

```markdown
## PM Routing Result

### Request Summary
- ...

### Required Agents
1. DB Agent: required / skipped
2. Backend Agent: required / skipped
3. Frontend Agent: required / skipped
4. Review Agent: required

### Execution Order
1. ...
2. ...
3. ...

### Reasoning
- ...

### Handoff Notes
- ...

### RAG Update Candidate
- None / Required
```

## 4. DB Agent Required Conditions

Route to DB Agent when the request includes:

- Table design
- ERD
- PK/FK
- Relationship design
- Index strategy
- SQL DDL/DML
- Data lifecycle
- Audit/history table design
- Entity-field mismatch caused by schema uncertainty

## 5. Backend Agent Required Conditions

Route to Backend Agent when the request includes:

- Java/Spring Boot implementation
- JPA entity/repository/service/controller
- DTO design
- API design or implementation
- Validation
- Exception handling
- Authentication/authorization implementation
- QueryDSL/Redis usage

## 6. Frontend Agent Required Conditions

Route to Frontend Agent when the request includes:

- UI/page/component structure
- React implementation
- State management
- API integration
- Form handling
- Error/loading UX
- Frontend routing
- Accessibility or design-system usage

## 7. Review Agent Required Conditions

Review Agent is required for almost all non-trivial outputs.

Review Agent may be skipped only for:

- Simple explanation
- Simple clarification
- Single isolated concept answer
- Non-implementation casual answer

## 8. Future Expert Agent Candidate Conditions

If a request is clearly about a future Expert area, PM Agent must mark it as a future split candidate.

Examples:

| Future Agent | Candidate Trigger |
|---|---|
| DevOps Agent | CI/CD, Linux, Docker advanced, deployment, monitoring |
| Test Agent | Test strategy, test case design, automated tests |
| Security Agent | Vulnerability analysis, advanced auth/security review |
| Docs Agent | Documentation system, README, guide, changelog |
| RAG Update Agent | RAG gap, outdated rule, duplicate rule, conflicting rule |

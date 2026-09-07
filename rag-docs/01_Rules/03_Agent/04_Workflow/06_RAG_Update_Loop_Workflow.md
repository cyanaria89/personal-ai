# 06. RAG Update Loop Workflow

## 1. Purpose

This document defines how the system handles RAG improvement opportunities.

RAG documents must not be automatically modified by Agents.

Agents may only propose RAG Update Candidates.

User approval is required before actual RAG document updates.

## 2. Trigger Conditions

Create a RAG Update Candidate when:

- Required knowledge is missing from existing RAG
- Existing rules conflict
- Existing rule is too vague for execution
- Repeated questions expose the same gap
- Agent had to rely on general reasoning instead of RAG
- Expert-level knowledge is needed but Expert RAG does not exist yet
- Future Agent split need becomes clear

## 3. Candidate Format

```markdown
## RAG Update Candidate

### Source Agent
- PM / DB / Backend / Frontend / Review

### Trigger
- Missing rule / Conflicting rule / Vague rule / Outdated rule / Expert gap

### Related Domain
- SQL / Java / Spring Boot / JPA / Security / Frontend / AI / DevOps / Testing / etc.

### Problem
- ...

### Suggested Update
- ...

### Target Document
- Existing document: ...
- New document candidate: ...

### Priority
- High / Medium / Low

### Reason
- ...

### Requires User Approval
- Yes
```

## 4. RAG Update Agent Position

In v1, RAG Update Agent is not an independent Agent by default.

The responsibility is temporarily held by:

- PM Agent for planning-level gaps
- Review Agent for final consistency gaps
- Individual specialist Agents for domain-specific gaps

Future split:

```text
RAG Update Candidate handling
↓
RAG Update Agent
```

## 5. Approval Rule

Agents must not directly overwrite RAG documents.

Allowed:

- Suggest update candidates
- Prioritize update candidates
- Propose target files
- Draft update content when requested

Not allowed:

- Automatically modify canonical RAG documents
- Silently replace rules
- Merge conflicting rules without user confirmation

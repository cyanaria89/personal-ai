# 00. Workflow Overview

## 1. Goal

This document defines the standard workflow for the initial Agent system.

The workflow must satisfy the following principles:

- RAG-first operation
- No unsupported guessing
- PM-led routing
- Sequential execution by default
- Review before final answer
- RAG Update Candidate generation when knowledge gaps are found
- Future Expert Agent split support

## 2. Initial Agent Structure

```text
User Request
     ↓
PM Agent
     ↓
Required Agent Sequence
     ↓
DB Agent / Backend Agent / Frontend Agent
     ↓
Review Agent
     ↓
Final Answer
     ↓
RAG Update Candidate, if needed
```

## 3. Default Policy

The system does not automatically execute all Agents for every request.

The PM Agent must first determine:

- Whether DB work is required
- Whether Backend work is required
- Whether Frontend work is required
- Whether Review-only handling is sufficient
- Whether the request should produce a RAG Update Candidate

## 4. Default Execution Style

Sequential execution is the default.

```text
PM → DB → Backend → Frontend → Review → Final
```

However, the sequence may skip unnecessary Agents.

Examples:

```text
PM → DB → Review → Final
PM → Backend → Review → Final
PM → Frontend → Review → Final
PM → DB → Backend → Review → Final
PM → Backend → Frontend → Review → Final
```

## 5. Future Expansion Principle

Future Expert Agents must be added by splitting responsibilities from existing Agents, not by rewriting the whole workflow.

Primary future split targets:

- DevOps Agent
- Test Agent
- Security Agent
- Docs Agent
- AI Agent
- RAG Update Agent
- Performance Agent
- Design System Agent

# Agent Workflow v1

## Purpose

This package defines the initial operating workflow for the personal AI multi-agent development system.

The workflow is designed for the current 5-agent structure:

- PM Agent
- DB Agent
- Backend Agent
- Frontend Agent
- Review Agent

It also preserves clear extension points for future Expert Agents such as DevOps, Test, Security, Docs, AI, Performance, Design System, and RAG Update Agent.

## Files

| File | Purpose |
|---|---|
| `00_Workflow_Overview.md` | Overall workflow concept |
| `01_Sequential_Workflow.md` | Default sequential execution flow |
| `02_PM_Routing_Workflow.md` | PM Agent routing decision rules |
| `03_DB_To_Backend_Handoff.md` | DB Agent to Backend Agent handoff format |
| `04_Backend_To_Frontend_Handoff.md` | Backend Agent to Frontend Agent handoff format |
| `05_Review_Workflow.md` | Review Agent validation workflow |
| `06_RAG_Update_Loop_Workflow.md` | RAG Update Candidate loop |
| `90_Request_Workflow_Patterns.md` | Common request-to-workflow patterns |
| `99_Future_Workflow_Extension.md` | Future Expert Agent split/extension workflow |

## Core Principle

The default workflow is sequential, not parallel.

Parallel execution may be introduced later only when dependency boundaries and conflict-resolution rules are mature enough.

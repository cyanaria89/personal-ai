# PROJECT_PROGRESS.md

# Personal AI Project Master Progress

- description: 이 문서는 개인 AI 프로젝트의 단계별 RAG 문서 제작 및 Multi-Agent 구성 진행 상황을 추적하는 마스터 문서입니다.

---

# 1. Project Overview

## Goal

단순 RAG 챗봇이 아닌 개인 AI 개발팀(Multi-Agent System) 구축.

## Final Goal

User ➔ PM Agent ➔ Backend Agent ➔ Frontend Agent ➔ Review Agent ➔ DevOps Agent ➔ AI/ML Agent ➔ Final Output

---

# 2. Multi-Agent Development Roadmap (Core Workflow)

AI Agent의 확장 단계와 RAG 문서 제작 단계를 동기화한 핵심 로드맵입니다.

### [Phase 1] 기초 Backend & 1차 Agent 구성

- **RAG Target:** Level 1 (기초 백엔드) 및 DevOps 기초 문서 제작
- **Agent Target:** PM, Backend, Review Agent 가동 테스트
- **상태:** 🔄 진행 중 (백엔드 파운데이션 완료 후 DevOps 문서 제작 중)

### [Phase 2] AI / Agent AI 고도화

- **RAG Target:** Level 2 (AI/Agent 도메인 지식) 문서 제작
- **Agent Target:** Agent 시스템 자체를 고도화 (LangGraph 기반 룰 적용)
- **상태:** ⬜ 대기

### [Phase 3] Frontend 확장

- **RAG Target:** Level 3 (기초 프론트엔드) 문서 제작
- **Agent Target:** Frontend Agent 추가 및 전체 파이프라인 연동
- **상태:** ⬜ 대기

### [Phase 4] Expert 심화 및 안정화

- **RAG Target:** Level 4 (Advanced/Expert 기술 스택) 문서 제작
- **Agent Target:** DevOps, AI/ML Agent 추가 및 시스템 최종 최적화
- **상태:** ⬜ 대기

---

# 3. RAG Documents Registry by Level

에이전트들이 RAG로 참조할 문서들의 실제 아카이브 목록입니다.

## Level 1 — Backend Foundation & Core DevOps

AI 개발팀이 최초로 인지하고 코드를 작성하기 위한 기초 지식 세트입니다.

### Completed ✅

- SQL (Part01 ~ Part05)
- Java (Part01 ~ Part08)
- Spring Boot (Part01 ~ Part11)
- JPA Advanced (Part01 ~ Part08)
- Security Advanced (Part01 ~ Part08)
- QueryDSL Practical (Part01 ~ Part04)
- Testing (Part01 ~ Part07)
- Redis (Part01 ~ Part05)
- Git / GitHub (Part01 ~ Part05)
- Docker (Part01 ~ Part04)
- SSR Thymeleaf (Part01 ~ Part07)
- API Design (Part01 ~ Part10)
- Design Pattern (Part01 ~ Part08)

---

## Level 2 — AI & Agent AI

1차 Agent 팀이 스스로를 고도화하고 AI 기능을 다루기 위해 필요한 지식 세트입니다.

### Completed ✅

- Python for AI Automation (Part01 ~ Part10)
- Prompt Engineering (Part01 ~ Part11)
- LLM Core & API Integration (Part01 ~ Part10)
- Embedding Model & Semantic Search (Part01 ~ Part05)
- Vector Database & RAG (Part01 ~ Part07)
- RAG Evaluation & Retrieval Optimization (Part01 ~ Part07)
- LangChain & LangGraph (Part01 ~ Part08)
- Tool Calling & Function Calling (Part01 ~ Part07)
- Agent Workflow Design (Part01 ~ Part04)
- Multi-Agent System (Part01 ~ Part15)
- Agent Memory & State Management (Part01 ~ Part08)
- Agent Evaluation & Guardrails (Part01 ~ Part12)

---

## Level 3 — Frontend Foundation

2차 Agent 구성 시 Frontend Agent에게 주입할 지식 세트입니다.
Frontend Agent가 Backend API와 연동되는 실무 화면을 구현할 수 있도록 구성합니다.

### Completed ✅

- HTML & CSS Foundation (Part01 ~ Part16)
- JavaScript Foundation (Part01 ~ Part10)
- TypeScript Foundation (Part01 ~ Part12)
- React Core (Part01 ~ Part06)
- React Component Design (Part01 ~ Part07)
- React Router (Part01 ~ Part06)
- State Management (Part01 ~ Part06)
- Data Fetching & REST API Integration (Part01 ~ Part12)
- Form Handling & Validation (Part01 ~ Part08)
- Authentication Frontend Flow (Part01 ~ Part10)
- Error Handling & Loading UX (Part01 ~ Part09)
- UI Component Pattern (Part01 ~ Part08)
- Frontend Testing (Part01 ~ Part17)
- Frontend Accessibility (Part01 ~ Part10)
- Frontend Build & Deploy (Part01 ~ Part12)
- Frontend Code Review (Part01 ~ Part08)
- Styling Architecture (Part01 ~ Part07)
- Design System Foundation (Part01 ~ Part07)

---

## Level 4 — Expert (Advanced Stack)

최종 단계에서 전체 시스템 규모를 키우고 고도화할 때 사용할 심화 지식 세트입니다.
DevOps Agent, AI/ML Agent, Frontend Expert Agent, Architecture Review Agent 확장을 목표로 합니다.

### Completed ✅

#### Backend Expert

#### DevOps Expert

#### AI Expert

#### Frontend Expert

### Planned ⬜

#### Backend Expert

- Linux / Ubuntu Server
- Network Foundation
- Advanced Spring Architecture
- MSA
- Message Queue
- Kafka
- gRPC
- NoSQL
- Elasticsearch
- Performance Tuning
- Observability

#### DevOps Expert

- CI/CD
- Docker Advanced
- Kubernetes
- Infrastructure as Code
- Deployment Strategy
- Monitoring & Logging
- Security Operations
- Cloud Provider
- Backup / Disaster Recovery
- Cost Optimization / FinOps
- Release Management
- Site Reliability Engineering

#### AI Expert

- Context Engineering
- Agentic RAG
- Graph RAG
- Harness Engineering
- Loop Engineering
- Advanced Multi-Agent Orchestration
- Long-Term Memory
- RAG Evaluation & Retrieval Optimization
- Tool Calling & Function Calling Reliability
- AI Guardrails & Security
- AI Observability
- MLOps
- Fine-Tuning
- Model Quantization

#### Frontend Expert

- Next.js App Router
- Advanced React Pattern
- Frontend Architecture
- Design System Advanced
- Monorepo
- Frontend Performance Tuning
- SSR / SSG / ISR
- Frontend Observability
- Frontend Security
- Frontend Testing Strategy
- Data Fetching / Server State Advanced
- Frontend Authentication Architecture
- Frontend Accessibility Advanced
- Frontend Build Optimization / Bundling

---

# 4. Rule Activation Policy

## 4.1 Core Rules

다음 문서는 모든 Agent 및 RAG 운영에서 항상 우선 참조한다.

- Rules/Master/Master RAG Rules.md
- Rules/Master/Project Progress.md
- Rules/Master/RAG Document Operation Rules Addendum.md

## 4.2 Foundation Rules

Foundation Rules는 1차 Agent 팀의 기본 참조 규칙으로 사용한다.

- Rules/Domain/Foundation/Backend
- Rules/Domain/Foundation/AI
- Rules/Domain/Foundation/Frontend

## 4.3 Expert Rules

Expert Rules는 고급 기능, 운영 자동화, 성능 최적화, 배포, 고급 AI Agent 설계가 필요할 때 선택적으로 활성화한다.

- Rules/Domain/Expert/Backend
- Rules/Domain/Expert/DevOps
- Rules/Domain/Expert/AI
- Rules/Domain/Expert/Frontend

## 4.4 Agent Rules

Agent Rules는 실제 Agent 구축 단계에서 생성하며, 각 Agent의 역할, 참조 RAG 범위, 출력 형식, 금지 사항, 작업 루프를 정의한다.

- Rules/Agent

---

# 5. Directory Structure

```
RAG Doc
├ Rules
│ ├ Master
│ │ ├ Agent Build Context.md
│ │ ├ Master RAG Rules.md
│ │ ├ Project Progress.md
│ │ └ RAG Document Operation Rules Addendum.md
│ ├ Domain
│ │ ├ Foundation
│ │ │ ├ Backend
│ │ │ │ ├ SQL Domain Rules.md
│ │ │ │ ├ Java Domain Rules.md
│ │ │ │ ├ Spring Boot Domain Rules.md
│ │ │ │ ├ JPA Advanced Domain Rules.md
│ │ │ │ ├ Security Advanced Domain Rules.md
│ │ │ │ ├ QueryDSL Practical Domain Rules.md
│ │ │ │ ├ Testing Domain Rules.md
│ │ │ │ ├ Redis Domain Rules.md
│ │ │ │ ├ SSR Thymeleaf Domain Rules.md
│ │ │ │ ├ Git GitHub Domain Rules.md
│ │ │ │ ├ Docker Domain Rules.md
│ │ │ │ ├ API Design Domain Rules.md
│ │ │ │ └ Design Pattern Domain Rules.md
│ │ │ ├ AI
│ │ │ │ ├ Python for AI Automation Domain Rules.md
│ │ │ │ ├ Prompt Engineering Domain Rules.md
│ │ │ │ ├ Embedding Model Semantic Search Domain Rules.md
│ │ │ │ ├ Vector Database RAG Domain Rules.md
│ │ │ │ ├ RAG Evaluation Retrieval Optimization Domain Rules.md
│ │ │ │ ├ LangChain LangGraph Domain Rules.md
│ │ │ │ ├ Tool Calling Function Calling Domain Rules.md
│ │ │ │ ├ Agent Workflow Design Domain Rules.md
│ │ │ │ ├ Multi Agent System Domain Rules.md
│ │ │ │ ├ Agent Memory State Management Domain Rules.md
│ │ │ │ ├ LLM Core API Integration Domain Rules.md
│ │ │ │ └ Agent Evaluation Guardrails Domain Rules.md
│ │ │ └ Frontend
│ │ │   ├ HTML CSS Foundation Domain Rules.md
│ │ │   ├ JavaScript Foundation Domain Rules.md
│ │ │   ├ TypeScript Foundation Domain Rules.md
│ │ │   ├ React Core Domain Rules.md
│ │ │   ├ React Component Design Domain Rules.md
│ │ │   ├ React Router Domain Rules.md
│ │ │   ├ State Management Domain Rules.md
│ │ │   ├ Data Fetching REST API Integration Domain Rules.md
│ │ │   ├ Form Handling Validation Domain Rules.md
│ │ │   ├ Authentication Frontend Flow Domain Rules.md
│ │ │   ├ Error Handling Loading UX Domain Rules.md
│ │ │   ├ UI Component Pattern Domain Rules.md
│ │ │   ├ Frontend Testing Domain Rules.md
│ │ │   ├ Frontend Accessibility Domain Rules.md
│ │ │   ├ Frontend Build Deploy Domain Rules.md
│ │ │   ├ Frontend Code Review Domain Rules.md
│ │ │   ├ Styling Architecture Domain Rules.md
│ │ │   └ Design System Foundation Domain Rules.md
│ │ └ Expert
│ │   ├ Backend
│ │   │ ├ Linux Ubuntu Server Domain Rules.md
│ │   │ ├ Network Foundation Domain Rules.md
│ │   │ ├ Advanced Spring Architecture Domain Rules.md
│ │   │ ├ MSA Domain Rules.md
│ │   │ ├ Message Queue Domain Rules.md
│ │   │ ├ Kafka Domain Rules.md
│ │   │ ├ gRPC Domain Rules.md
│ │   │ ├ NoSQL Domain Rules.md
│ │   │ ├ Elasticsearch Domain Rules.md
│ │   │ ├ Performance Tuning Domain Rules.md
│ │   │ └ Observability Domain Rules.md
│ │   ├ DevOps
│ │   │ ├ CI CD Domain Rules.md
│ │   │ ├ Docker Advanced Domain Rules.md
│ │   │ ├ Kubernetes Domain Rules.md
│ │   │ ├ Infrastructure as Code Domain Rules.md
│ │   │ ├ Deployment Strategy Domain Rules.md
│ │   │ ├ Monitoring Logging Domain Rules.md
│ │   │ ├ Security Operations Domain Rules.md
│ │   │ ├ Cloud Provider Domain Rules.md
│ │   │ ├ Backup Disaster Recovery Domain Rules.md
│ │   │ ├ Cost Optimization FinOps Domain Rules.md
│ │   │ ├ Release Management Domain Rules.md
│ │   │ └ Site Reliability Engineering Domain Rules.md
│ │   ├ AI
│ │   │ ├ Context Engineering Domain Rules.md
│ │   │ ├ Agentic RAG Domain Rules.md
│ │   │ ├ Graph RAG Domain Rules.md
│ │   │ ├ Harness Engineering Domain Rules.md
│ │   │ ├ Loop Engineering Domain Rules.md
│ │   │ ├ Advanced Multi-Agent Orchestration Domain Rules.md
│ │   │ ├ Long-Term Memory Domain Rules.md
│ │   │ ├ RAG Evaluation Retrieval Optimization Domain Rules.md
│ │   │ ├ Tool Calling Function Calling Reliability Domain Rules.md
│ │   │ ├ AI Guardrails Security Domain Rules.md
│ │   │ ├ AI Observability Domain Rules.md
│ │   │ ├ MLOps Domain Rules.md
│ │   │ ├ Fine-Tuning Domain Rules.md
│ │   │ └ Model Quantization Domain Rules.md
│ │   └ Frontend
│ │     ├ Nextjs App Router Domain Rules.md
│ │     ├ Advanced React Pattern Domain Rules.md
│ │     ├ Frontend Architecture Domain Rules.md
│ │     ├ Design System Advanced Domain Rules.md
│ │     ├ Monorepo Domain Rules.md
│ │     ├ Frontend Performance Tuning Domain Rules.md
│ │     ├ SSR SSG ISR Domain Rules.md
│ │     ├ Frontend Observability Domain Rules.md
│ │     ├ Frontend Security Domain Rules.md
│ │     ├ Frontend Testing Strategy Domain Rules.md
│ │     ├ Data Fetching Server State Advanced Domain Rules.md
│ │     ├ Frontend Authentication Architecture Domain Rules.md
│ │     ├ Frontend Accessibility Advanced Domain Rules.md
│ │     └ Frontend Build Optimization Bundling Domain Rules.md
│ └ Agent
├ RAG Foundation
│ ├ Backend
│ │ ├ SQL (Part01 ~ 05)
│ │ ├ Java (Part01 ~ 08)
│ │ ├ SpringBoot (Part01 ~ 11)
│ │ ├ JPA Advanced (Part01 ~ 08)
│ │ ├ Security Advanced
│ │ ├ QueryDSL Practical (Part01 ~ 04)
│ │ ├ Testing (Part01 ~ 07)
│ │ ├ Redis (Part01 ~ 05)
│ │ ├ SSR Thymeleaf (Part01 ~ 07)
│ │ ├ Git GitHub (Part01 ~ 05)
│ │ ├ Docker (Part01 ~ 04)
│ │ ├ API Design (Part01 ~ 10)
│ │ └ Design Pattern (Part01 ~ 08)
│ ├ AI
│ │ ├ Python for AI Automation (Part01 ~ 10)
│ │ ├ Prompt Engineering (Part01 ~ 11)
│ │ ├ LLM Core API Integration (Part01 ~ 10)
│ │ ├ Embedding Model Semantic Search (Part01 ~ 05)
│ │ ├ Vector Database RAG (Part01 ~ 07)
│ │ ├ RAG Evaluation Retrieval Optimization (Part01 ~ 07)
│ │ ├ LangChain LangGraph (Part01 ~ 08)
│ │ ├ Tool Calling Function Calling (Part01 ~ 07)
│ │ ├ Agent Workflow Design (Part01 ~ 04)
│ │ ├ Multi Agent System (Part01 ~ 15)
│ │ ├ Agent Memory State Management (Part01 ~ 08)
│ │ └ Agent Evaluation Guardrails (Part01 ~ 12)
│ └ Frontend
│   ├ HTML CSS Foundation (Part01 ~ 16)
│   ├ JavaScript Foundation (Part01 ~ 10)
│   ├ TypeScript Foundation (Part01 ~ 12)
│   ├ React Core (Part01 ~ 06)
│   ├ React Component Design (Part01 ~ 07)
│   ├ React Router (Part01 ~ 06)
│   ├ State Management (Part01 ~ 06)
│   ├ Data Fetching REST API Integration (Part01 ~ 12)
│   ├ Form Handling Validation (Part01 ~ 08)
│   ├ Authentication Frontend Flow (Part01 ~ 10)
│   ├ Error Handling Loading UX (Part01 ~ 09)
│   ├ UI Component Pattern (Part01 ~ 08)
│   ├ Frontend Testing (Part01 ~ 17)
│   ├ Frontend Accessibility (Part01 ~ 10)
│   ├ Frontend Build Deploy (Part01 ~ 12)
│   ├ Frontend Code Review (Part01 ~ 08)
│   ├ Styling Architecture (Part01 ~ 07)
│   └ Design System Foundation (Part01 ~ 07)
└ RAG Expert
  ├ Backend
  │ ├ Linux Ubuntu Server
  │ ├ Network Foundation
  │ ├ Advanced Spring Architecture
  │ ├ MSA
  │ ├ Message Queue
  │ ├ Kafka
  │ ├ gRPC
  │ ├ NoSQL
  │ ├ Elasticsearch
  │ ├ Performance Tuning
  │ └ Observability
  ├ DevOps
  │ ├ CI CD
  │ ├ Docker Advanced
  │ ├ Kubernetes
  │ ├ Infrastructure as Code
  │ ├ Deployment Strategy
  │ ├ Monitoring Logging
  │ ├ Security Operations
  │ ├ Cloud Provider
  │ ├ Backup Disaster Recovery
  │ ├ Cost Optimization FinOps
  │ ├ Release Management
  │ └ Site Reliability Engineering
  ├ AI
  │ ├ Context Engineering
  │ ├ Agentic RAG
  │ ├ Graph RAG
  │ ├ Harness Engineering
  │ ├ Loop Engineering
  │ ├ Advanced Multi-Agent Orchestration
  │ ├ Long-Term Memory
  │ ├ RAG Evaluation Retrieval Optimization Advanced
  │ ├ Tool Calling Function Calling Reliability
  │ ├ AI Guardrails Security
  │ ├ AI Observability
  │ ├ MLOps
  │ ├ Fine-Tuning
  │ └ Model Quantization
  └ Frontend
    ├ Nextjs App Router
    ├ Advanced React Pattern
    ├ Frontend Architecture
    ├ Design System Advanced
    ├ Monorepo
    ├ Frontend Performance Tuning
    ├ SSR SSG ISR
    ├ Frontend Observability
    ├ Frontend Security
    ├ Frontend Testing Strategy
    ├ Data Fetching Server State Advanced
    ├ Frontend Authentication Architecture
    ├ Frontend Accessibility Advanced
    └ Frontend Build Optimization Bundling
```

# 99. Expert RAG Extension Map

## 1. 목적

이 문서는 추후 Expert RAG 문서가 제작되었을 때, 기존 5개 Agent 구조에서 어떤 Agent를 추가하거나 분리할지 정의한다.

초기 구조는 다음 5개 Agent를 유지한다.

```text
PM / DB / Backend / Frontend / Review
```

Expert 문서가 충분히 쌓이면 아래 Agent를 분리할 수 있다.

```text
DevOps / Test / Security / Docs / AI / RAG Update / Performance / Design System
```

## 2. Expert 문서 추가 시 공통 절차

```text
1. Expert Domain Rules 제작
2. 해당 Expert 문서를 Agent-RAG Mapping에 추가
3. 기존 Agent의 Secondary Responsibility에서 해당 영역 제거 또는 축소
4. 새 Agent Rules 작성
5. 새 Agent System Prompt 작성
6. Routing Map 수정
7. Review Agent의 검토 항목 수정
```

## 3. DevOps Agent 분리

### 분리 전 위치

```text
Backend Agent: Docker/Git 기초 참조
Frontend Agent: Build/Deploy 기초 참조
Review Agent: 배포/운영 기초 검토
```

### 분리 후 담당

```text
DevOps Agent
- Linux/Ubuntu
- Docker Advanced
- CI/CD
- Nginx
- Cloud
- Monitoring
- Logging
- Backup
- 운영 배포 체크리스트
```

### 분리 기준

```text
- 배포/운영 요청이 반복됨
- CI/CD 문서 제작 완료
- Docker Advanced 또는 Linux Expert 문서 제작 완료
- Backend Agent가 운영 책임까지 과하게 가지기 시작함
```

## 4. Test Agent 분리

### 분리 전 위치

```text
Backend Agent: Backend Testing 기초
Frontend Agent: Frontend Testing 기초
Review Agent: 전체 테스트 관점 검토
```

### 분리 후 담당

```text
Test Agent
- 테스트 전략
- 단위/통합/E2E 테스트
- 테스트 케이스 작성
- 테스트 코드 리뷰
- 품질 기준 관리
```

### 분리 기준

```text
- 테스트 코드 작성 요청이 많아짐
- 테스트 전략 문서가 Expert로 확장됨
- Review Agent의 테스트 검토가 과도하게 길어짐
```

## 5. Security Agent 분리

### 분리 전 위치

```text
Backend Agent: 기본 인증/인가 구현
Review Agent: 보안 관점 검토
Frontend Agent: 인증 흐름/권한 UX
```

### 분리 후 담당

```text
Security Agent
- 인증/인가 설계
- 권한 정책 검토
- 민감정보 노출 검토
- API 보안 검토
- Frontend Auth Flow 검토
- 취약점 체크리스트
```

### 분리 기준

```text
- 보안 요구사항이 복잡해짐
- Security Expert 문서가 Foundation 범위를 넘어섬
- 인증/인가 변경이 전체 작업에 자주 영향 줌
```

## 6. Docs Agent 분리

### 분리 전 위치

```text
PM Agent: 산출물 구조 결정
Review Agent: 문서 누락 검토
```

### 분리 후 담당

```text
Docs Agent
- README
- API 문서
- ERD 설명
- 작업 지시서
- 회고/진행 문서
- RAG 문서 형식 정리 보조
```

### 분리 기준

```text
- 문서 산출물이 많아짐
- 코드와 별개로 문서 품질 검토가 필요함
- RAG 문서 운영이 복잡해짐
```

## 7. AI Agent 분리

### 분리 전 위치

```text
PM Agent: Agent Workflow 판단
Review Agent: Agent 품질/Guardrails 검토
```

### 분리 후 담당

```text
AI Agent
- Agent Workflow 설계
- LangGraph/LangChain 구성
- Tool Calling 설계
- RAG 검색/평가 개선
- Agent Memory/State 관리
```

### 분리 기준

```text
- 실제 LangGraph/Agent Runtime 구현에 들어감
- AI Foundation 문서가 Expert 수준으로 확장됨
- PM Agent가 AI 시스템 설계까지 담당하기 어려워짐
```

## 8. RAG Update Agent 분리

### 분리 전 위치

```text
모든 Agent: Candidate 생성
Review Agent: Candidate 통합
PM Agent: 사용자 승인 흐름 관리
```

### 분리 후 담당

```text
RAG Update Agent
- RAG Update Candidate 수집
- 중복 후보 병합
- 우선순위 정리
- 보강 대상 문서 추천
- 사용자 승인용 변경안 작성
```

### 분리 기준

```text
- Candidate가 반복적으로 많아짐
- RAG 문서 개선 루프를 독립 운영하고 싶어짐
- Review Agent의 품질 검토와 RAG 개선 검토를 분리해야 함
```

## 9. Performance Agent 분리

### 분리 전 위치

```text
DB Agent: 인덱스/쿼리 기초 검토
Backend Agent: JPA/QueryDSL/Redis 기초 검토
Frontend Agent: React 렌더링 기초 검토
Review Agent: 성능 위험 검토
```

### 분리 후 담당

```text
Performance Agent
- DB 쿼리 성능
- JPA N+1/페치 전략
- Redis 캐시 전략
- API 응답 성능
- React 렌더링 최적화
```

### 분리 기준

```text
- 성능 문제 분석 요청이 반복됨
- DB/Backend/Frontend 성능 규칙이 Expert 문서로 확장됨
- 기존 Agent들이 성능 책임을 중복해서 가짐
```

## 10. Design System Agent 분리

### 분리 전 위치

```text
Frontend Agent: Styling / Design System Foundation 참조
Review Agent: UI 일관성 기초 검토
```

### 분리 후 담당

```text
Design System Agent
- 디자인 토큰
- 컴포넌트 규칙
- 스타일 아키텍처
- 접근성 연계
- UI 일관성 검토
```

### 분리 기준

```text
- Design System Expert 문서 제작
- UI 컴포넌트 규모 증가
- Frontend Agent가 화면 구현과 디자인 시스템 관리를 동시에 하기 어려워짐
```

## 11. 권장 분리 순서

초기 5개 Agent 이후 추천 분리 순서는 다음과 같다.

```text
1. RAG Update Agent
2. Test Agent
3. Security Agent
4. DevOps Agent
5. AI Agent
6. Performance Agent
7. Docs Agent
8. Design System Agent
```

단, 실제 우선순위는 사용 빈도와 Expert 문서 완성도를 기준으로 조정한다.


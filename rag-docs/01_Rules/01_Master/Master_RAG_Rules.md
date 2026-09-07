# MASTER RAG RULES

## Personal AI Project - Universal RAG Document Rules

---

# 0. Core Philosophy

이 문서는 사람이 처음부터 끝까지 읽는 학습 문서가 아니다.

목적:

- AI Agent Retrieval
- Semantic Search
- Code Generation Support
- Review / Validation Support
- Decision Support

우선순위:

1. Retrieval Hit
2. Chunk Quality
3. Semantic Similarity
4. Human Readability

---

# 1. Document Output Rules

모든 RAG 문서는 Markdown(.md) 기준 작성.

출력 형식:

- Header 사용
- Code Block 사용
- Table 사용 가능
- Plain text 최소화

권장:

- 구조적 문서
- 검색 친화적 문서
- Chunk 분리 문서

금지:

- 장문 에세이형 문서
- 불필요한 서론
- 중복 설명

---

# 2. Required Section Rules

모든 Domain 문서는 아래 Section 구조를 우선 사용.

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 3. FAQ Rules

`[면접]` 섹션 사용 금지.

반드시 `[FAQ]` 사용.

형식:

```md
### [FAQ]

Q. 질문?

A.
짧고 명확한 답변
```

규칙:

- Q only 금지
- 반드시 Q + A
- A는 1~4줄
- 장문 금지

목적:

- Query Pattern Matching
- Retrieval 강화
- Semantic Search 강화

---

# 4. Chunk Design Rules

Chunk는 독립 검색되어도 의미 유지.

좋은 Chunk 조건:

- 하나의 개념만 설명
- 제목 명확
- 짧은 예제 포함
- 독립 검색 가능

---

권장 Chunk Size:

- 300 ~ 1200 tokens

---

금지:

- 여러 개념 혼합
- 지나치게 긴 설명
- 긴 서론

---

# 5. Naming Consistency Rules

문서 전체에서 핵심 용어 통일.

예:

권장:

- JWT Authentication
- Access Token
- Refresh Token
- ROLE_USER
- ROLE_ADMIN
- SecurityContext

금지:

- JWT / Token Auth 혼용
- ROLE_ADMIN / ADMIN 혼용

---

규칙:

개념명:

- PascalCase or Standard Naming

변수명:

- camelCase 허용

예:

```text
SecurityContext ← 개념
securityContext ← 변수
```

---

# 6. Flow Rules

복잡한 개념은 반드시 Flow 포함.

대상 예시:

- Authentication
- Authorization
- JWT
- OAuth2
- Filter Chain

형식:

```text
Request
→ Process
→ Result
```

예:

```text
Request
→ Authentication
→ Authorization
→ Response
```

---

# 7. Code Example Rules

Code는 짧고 직접적이어야 함.

목적:

- Retrieval
- Code Generation
- Review

권장:

- 핵심 로직만 포함
- 불필요 import 제거 가능
- 짧은 snippet

금지:

- 긴 전체 프로젝트 코드
- 불필요 boilerplate

---

# 8. Explanation Rules

설명은 짧고 검색 친화적으로.

권장:

- Bullet Point
- Direct Statement
- Keyword 중심

금지:

- 긴 문단
- 서술형 설명

---

예:

좋음:

```md
장점:

- 빠름
- 확장성 좋음
```

나쁨:

```md
이 기술은 다양한 환경에서...
(장문)
```

---

# 9. Domain Optimization Rules

각 Domain별 Rule 적용.

예:

- SQL → Query 중심
- Backend → Architecture / Code 중심
- Frontend → Component / State 중심
- AI → Workflow / Agent 중심
- Security → Flow / Handler 중심

---

Domain Rule 우선순위:

MASTER_RAG_RULES
→ DOMAIN_RULES
→ PART RULES

---

# 10. Retrieval Queries Rules

모든 문서 마지막에 Retrieval Queries Block 필수.

형식:

```md
# Retrieval Queries

### [FAQ]

Q. 핵심 질문?
A. 짧은 답변
```

목적:

- User Query Matching
- Semantic Retrieval 강화
- Agent Query Response 최적화

---

예:

```md
Q. JWT 구조는?

A.
Header + Payload + Signature
```

---

# 11. Quality Checklist

최종 출력 전 반드시 검수.

체크 항목:

- 오타 없는가?
- 용어 통일 되었는가?
- Chunk 구조 적절한가?
- Retrieval 최적화 되었는가?
- 중복 설명 없는가?
- FAQ 포함했는가?
- Retrieval Queries 포함했는가?

---

목표 품질:

- Minimum: 95/100
- Target: 97+/100

---

# 12. Final Goal

최종 목표:

RAG 문서 = 단순 요약 문서가 아니다.

RAG 문서는 AI Agent가 아래를 수행할 수 있어야 한다.

- Retrieve
- Understand
- Reason
- Generate
- Review

문서 품질이 곧 Agent 성능이다.

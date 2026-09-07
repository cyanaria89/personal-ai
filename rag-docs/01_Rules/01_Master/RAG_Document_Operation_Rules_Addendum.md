# RAG Upload and Agent Rules Addendum

## 1. Domain Rules Usage

Domain Rules 문서는 RAG 본문 제작 기준 문서이다.

Domain Rules는 기본적으로 Agent 검색용 RAG 본문에 직접 업로드하지 않는다.

Domain Rules는 다음 목적에 사용한다.

- RAG 문서 Set 제작 기준
- 신규 Domain 문서 제작 시 참고
- Agent Rules / System Prompt 제작 시 참고
- 문서 구조, 범위, FAQ, Retrieval Queries 기준 확인

## 2. Upload Target Rule

Agent RAG 검색용 업로드 대상은 실제 지식 본문 문서이다.

업로드 권장:

- SQL 본문 문서
- Java 본문 문서
- Spring Boot 본문 문서
- JPA 본문 문서
- Security 본문 문서
- QueryDSL 본문 문서
- Testing 본문 문서
- Redis 본문 문서
- Git/GitHub 본문 문서
- Docker 본문 문서
- SSR Thymeleaf 본문 문서
- API Design 본문 문서
- Design Pattern Part01 ~ Part08

업로드 비추천:

- MASTER_RAG_RULES
- Domain Rules
- Project Progress
- 제작 요청 프롬프트
- Completion Report
- 품질 점수 보고서
- 작업 완료 보고서

## 3. Final Index Rule

Final Index 문서는 업로드 가능하다.

다만 검색 결과에서 Final Index가 과도하게 노출되면 별도 Collection으로 분리한다.

Final Index는 Pattern 상세 설명을 대체하지 않는다.

Final Index는 Retrieval Routing, Quality Gate, Upload Test 기준으로 사용한다.

## 4. Completion Report Rule

Completion Report는 보관용 문서이다.

Completion Report는 RAG 업로드 대상에서 제외한다.

Completion Report에는 완료 상태, 자체 점수, 업로드 준비 여부 같은 메타 정보가 많기 때문에 실제 Agent 검색 품질을 방해할 수 있다.

## 5. Agent Rules Usage

Agent Rules 또는 System Prompt를 제작할 때는 다음 문서를 참고한다.

- MASTER_RAG_RULES
- Domain Rules
- Project Progress
- 각 Domain의 Final Index
- 각 Domain의 Pattern Selection / Review / Workflow 문서

Agent 검색용 RAG 본문에는 Domain Rules를 직접 넣지 않는다.

Agent System Prompt에는 Domain Rules의 핵심 원칙만 요약해서 반영한다.

## 6. Practical Decision

기존 Domain Rules 파일을 직접 수정하지 않아도 된다.

기존 Domain Rules는 제작 당시 기준으로 보관한다.

이 Addendum 문서를 최신 운영 기준으로 사용한다.

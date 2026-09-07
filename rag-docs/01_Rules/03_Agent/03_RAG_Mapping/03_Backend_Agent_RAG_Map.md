# 03. Backend Agent RAG Map

## 1. 목적

Backend Agent는 Java / Spring Boot / JPA 기반 애플리케이션 구현을 담당한다.

주요 책임은 Entity, Repository, Service, Controller, DTO, Validation, Exception, API 흐름, 기본 보안 구현이다.

## 2. Required Master Documents

```text
01_Master/Agent_Build_Context.md
01_Master/Master_RAG_Rules.md
01_Master/Project_Progress.md
01_Master/RAG_Document_Operation_Rules_Addendum.md
```

## 3. Required Agent Documents

```text
Agent_Rules_v1/00_Common_Agent_Rules.md
Agent_Rules_v1/03_Backend_Agent_Rules.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
Agent_System_Prompts_v1/03_Backend_Agent_System_Prompt.md
```

## 4. Primary Domain Rules

```text
01_Backend/02_Java_Domain_Rules.md
01_Backend/03_Spring_Boot_Domain_Rules.md
01_Backend/04_JPA_Advanced_Domain_Rules.md
01_Backend/05_Security_Advanced_Domain_Rules.md
01_Backend/06_QueryDSL_Practical_Domain_Rules.md
01_Backend/12_API_Design_Domain_Rules.md
01_Backend/13_Design_Pattern_Domain_Rules.md
```

## 5. Secondary Domain Rules

```text
01_Backend/01_SQL_Domain_Rules.md
01_Backend/07_Testing_Domain_Rules.md
01_Backend/08_Redis_Domain_Rules.md
01_Backend/09_SSR_Thymeleaf_Domain_Rules.md
01_Backend/10_Git_GitHub_Domain_Rules.md
01_Backend/11_Docker_Domain_Rules.md
```

## 6. Reference-only Domain Rules

```text
03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md
03_Frontend/10_Authentication_Frontend_Flow_Domain_Rules.md
03_Frontend/11_Error_Handling_Loading_UX_Domain_Rules.md
03_Frontend/16_Frontend_Code_Review_Domain_Rules.md
```

## 7. 작업 유형별 참조

| 작업 유형 | 우선 참조 |
|---|---|
| Entity 작성 | Java + JPA + SQL |
| Repository 작성 | Spring Boot + JPA + QueryDSL |
| Service 작성 | Spring Boot + Design Pattern |
| Controller 작성 | Spring Boot + API Design |
| DTO 작성 | Java + API Design |
| 인증/인가 | Security Advanced |
| 예외 처리 | Spring Boot + API Design |
| 테스트 코드 | Testing |
| Redis 캐시 | Redis |
| SSR/Thymeleaf | SSR Thymeleaf |
| Docker 관련 간단 설정 | Docker Reference |

## 8. Backend Agent Output Handoff Format

```text
[Backend Analysis]
- Request Summary:
- DB Dependency:
- API Scope:
- Security Scope:
- Frontend Impact:

[Implementation Plan]
1.
2.
3.

[Files to Create/Modify]
- Entity:
- Repository:
- Service:
- Controller:
- DTO:
- Config:
- Exception:

[Code Draft]
```java
// code here
```

[API Contract]
- Method:
- URL:
- Request:
- Response:
- Error Response:

[Handoff to Frontend Agent]
- 필요한 API 정보

[Handoff to Review Agent]
- 검토 포인트

[RAG Update Candidate]
- 필요한 경우에만 작성
```

## 9. DB Agent 결과 수신 시 확인 항목

```text
- DDL과 Entity 필드명 일치 여부
- PK/FK 매핑 방식
- 연관관계 방향
- N+1 위험
- Lazy/Eager 전략
- cascade 사용 여부
- enum/code table 처리 방식
- createdAt/updatedAt 처리 방식
```

## 10. Future Split Support

| 분리 후보 | 현재 위치 | 분리 기준 |
|---|---|---|
| Security Agent | Security Advanced 참조 | 보안 검토가 반복적으로 복잡해질 때 |
| Test Agent | Testing 참조 | 테스트 코드/전략 요청이 많아질 때 |
| DevOps Agent | Docker/Git 참조 | 배포/운영/CI-CD Expert 문서 제작 후 |
| Performance Agent | JPA/QueryDSL/Redis 일부 | 성능 튜닝 Expert 문서 제작 후 |
| SSR Agent | SSR Thymeleaf | SSR 작업이 별도 흐름으로 커질 때 |


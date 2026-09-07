# API Design Domain Rules

---

# 1. Domain Purpose

API Design Domain 문서는 Backend Agent / PM Agent / Review Agent용 RAG 문서이다.

목적:

- API Architecture Support
- RESTful API Design Support
- Contract Design Support
- API Quality Improvement
- API Troubleshooting

우선순위:

1. API Core
2. REST Design
3. Request / Response Contract
4. Versioning / Troubleshooting

---

# 2. Scope

포함 범위:

- API Core
- REST
- Resource
- URI Design
- Request
- Response
- HTTP Method
- Status Code
- Pagination
- Filtering
- Sorting
- Validation
- Error Response
- API Versioning
- Idempotency
- Authentication
- Authorization
- Rate Limiting
- OpenAPI
- Swagger
- Troubleshooting

---

# 3. Section Priority

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

# 4. API Core Rules

API Design 문서는 Contract-based Communication 중심으로 작성.

핵심 구조:

- Client
- Request
- Server
- Response

---

반드시 설명 포함:

- API 역할
- 왜 중요한가
- Frontend / Backend 연결 구조
- 어떤 문제를 해결하는가

---

예:

```text
Client
→ Request
→ API
→ Response
```

---

# 5. REST Rules

매우 중요.

필수 포함:

- REST
- Resource
- Stateless

---

반드시 설명:

- REST 원칙
- RESTful API 의미

---

중요:

API Design 문서 품질은 REST 설명 품질이 결정.

---

# 6. Resource Rules

필수 포함:

- Resource
- Entity Mapping

---

예:

```text
/users
/orders
/products
```

---

반드시 설명:

- Resource 중심 설계

---

# 7. URI Design Rules

매우 중요.

필수 포함:

- URI Naming
- Path Variable
- Query Parameter

---

예:

```text
/users/{id}
/products?category=food
```

---

반드시 설명:

- 명확한 URI 설계
- 복수형 Resource 권장

---

# 8. Request Rules

필수 포함:

- Header
- Query Parameter
- Body

---

반드시 설명:

- Request 구성 요소

---

# 9. Response Rules

매우 중요.

필수 포함:

- Status
- Header
- Body

---

예:

```json
{
  "data": {}
}
```

---

반드시 설명:

- Response Schema
- Contract 안정성

---

# 10. HTTP Method Rules

매우 중요.

필수 포함:

- GET
- POST
- PUT
- PATCH
- DELETE

---

예:

```text
GET    → 조회
POST   → 생성
PUT    → 전체 수정
PATCH  → 부분 수정
DELETE → 삭제
```

---

반드시 설명:

- Method 역할 구분

---

# 11. Status Code Rules

매우 중요.

필수 포함:

- 200
- 201
- 204
- 400
- 401
- 403
- 404
- 409
- 500

---

반드시 설명:

- 상태 코드 의미
- 상황별 선택 기준

---

# 12. Pagination Rules

필수 포함:

- Page
- Size
- Cursor

---

예:

```text
/products?page=0&size=20
```

---

반드시 설명:

- 대량 데이터 조회

---

# 13. Filtering Rules

필수 포함:

- Filter
- Search

---

예:

```text
/products?category=food
```

---

반드시 설명:

- 조건 기반 조회

---

# 14. Sorting Rules

필수 포함:

- Sort
- Order

---

예:

```text
/products?sort=createdAt,desc
```

---

반드시 설명:

- 정렬 기준

---

# 15. Validation Rules

매우 중요.

필수 포함:

- Request Validation
- Input Validation

---

반드시 설명:

- Invalid Input 방지
- 안정성 확보

---

# 16. Error Response Rules

매우 중요.

필수 포함:

- Error Code
- Error Message

---

예:

```json
{
  "code": "USER_NOT_FOUND",
  "message": "User not found"
}
```

---

반드시 설명:

- 일관된 Error Contract

---

# 17. Versioning Rules

필수 포함:

- URI Versioning
- Header Versioning

---

예:

```text
/api/v1/users
```

---

반드시 설명:

- API 변경 관리

---

# 18. Idempotency Rules

필수 포함:

- Idempotent
- Safe Retry

---

반드시 설명:

- 중복 요청 처리
- Retry 안정성

---

# 19. Authentication Rules

필수 포함:

- Authentication
- Token

---

반드시 설명:

- 사용자 인증

---

# 20. Authorization Rules

필수 포함:

- Authorization
- Permission

---

반드시 설명:

- 권한 검증

---

# 21. Rate Limiting Rules

필수 포함:

- Rate Limiting
- Abuse Prevention

---

반드시 설명:

- API 보호
- 과도한 요청 방지

---

# 22. OpenAPI Rules

필수 포함:

- OpenAPI
- API Documentation

---

반드시 설명:

- API 문서 자동화

---

# 23. Swagger Rules

필수 포함:

- Swagger UI
- API Testing

---

반드시 설명:

- 개발 편의성 향상

---

# 24. Troubleshooting Rules

반드시 포함 추천.

예:

- Invalid Request
- Wrong Status Code
- Version Conflict
- Contract Mismatch
- Pagination Issue
- Validation Failure

---

형식:

문제:

원인:

해결:

---

# 25. Retrieval Optimization Rules

강조 대상:

- API Design
- REST
- URI
- Status Code
- Pagination
- Validation
- Error Response
- OpenAPI

키워드 반복 허용.

---

# 26. Version Rules

기준:

- REST API
- OpenAPI 3.x
- Swagger
- Spring Boot 3.x

---

Legacy 제외.

---

# 27. Common Mistakes

자주 발생:

- URI Naming 불명확
- Method 오사용
- Status Code 오사용
- Error Contract 불일치
- Pagination 누락
- Versioning 부재
- Validation 부족

---

# 28. Final Goal

API Design RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve API Pattern
- Design REST API
- Review API Contract
- Improve API Quality
- Solve API Problems

문서 품질이 API Architecture 품질을 결정한다.

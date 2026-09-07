# API Design Part 01 - API Core & REST Foundation

---

# 1. API Core

## 1.1 API

### [개념]

API(Application Programming Interface)는 Client와 Server가 정해진 규칙에 따라 데이터를 주고받기 위한 Interface이다.

API Design은 단순 URL 작성이 아니라 Request / Response Contract를 설계하는 작업이다.

API는 Frontend, Backend, Mobile App, External System 사이의 Communication Contract 역할을 한다.

```text
Client
→ Request
→ API
→ Server
→ Response
→ Client
```

---

### [핵심]

- API는 Client와 Server 사이의 약속이다.
- API Design의 핵심은 Contract 안정성이다.
- API는 Request와 Response 구조를 명확히 정의해야 한다.
- API는 Frontend / Backend 협업 기준이 된다.
- API 품질은 서비스 확장성, 유지보수성, 테스트 품질에 직접 영향을 준다.

---

### [실무]

2026 실무 기준 API Design은 Contract-based Communication 중심으로 설계한다.

Backend는 API를 통해 Resource, Business Logic, Data Access 결과를 외부에 제공한다.

Frontend는 API Contract를 기준으로 화면, 상태 관리, Error Handling, Pagination, Filtering, Sorting을 구현한다.

API 문서화는 OpenAPI 3.x 또는 Swagger UI를 사용한다.

API 설계 시 다음 항목을 먼저 정의한다.

- Resource
- URI
- HTTP Method
- Request Header
- Request Query Parameter
- Request Body
- Response Status Code
- Response Body
- Error Response
- Authentication
- Authorization

---

### [FAQ]

Q. API는 단순히 URL을 만드는 것인가?

A. 아니다. API는 Client와 Server 사이의 Request / Response Contract를 설계하는 것이다.

Q. API Design에서 가장 중요한 것은 무엇인가?

A. Contract 안정성, Resource 중심 설계, 일관된 Request / Response 구조이다.

Q. Frontend와 Backend 협업에서 API가 중요한 이유는?

A. Frontend는 API Contract를 기준으로 화면과 상태 처리를 구현하고, Backend는 Contract를 기준으로 데이터를 제공하기 때문이다.

---

# 2. API Communication Flow

## 2.1 Request Response Flow

### [개념]

API Communication Flow는 Client가 Request를 보내고 Server가 처리 후 Response를 반환하는 흐름이다.

```text
Client
→ Request
→ Controller
→ Service
→ Repository
→ Database
→ Repository
→ Service
→ Controller
→ Response
→ Client
```

---

### [핵심]

- Request는 Client의 요청 정보이다.
- Response는 Server의 처리 결과이다.
- API는 Request와 Response의 Contract를 고정한다.
- Controller는 API Entry Point 역할을 한다.
- Service는 Business Logic을 처리한다.
- Repository는 Data Access를 담당한다.

---

### [실무]

Spring Boot 3.x 기준 API 처리 흐름은 Controller → Service → Repository 구조를 주로 사용한다.

Controller는 Request Mapping, Parameter Binding, Validation Trigger, Response Wrapping을 담당한다.

Service는 Business Rule, Transaction, Authorization Check, Domain Logic을 담당한다.

Repository는 Entity 조회, 저장, 수정, 삭제를 담당한다.

API Design 문서에서는 이 흐름을 명확히 작성해야 Backend Agent가 Controller / Service / DTO 코드를 생성하기 쉽다.

---

### [Flow]

```text
HTTP Request
→ Controller
→ Request DTO Binding
→ Validation
→ Service
→ Business Logic
→ Repository
→ Database
→ Response DTO
→ HTTP Response
```

---

### [FAQ]

Q. API Flow에서 Controller는 무엇을 담당하는가?

A. Request를 받고, DTO로 변환하고, Validation을 트리거하고, Response를 반환한다.

Q. API Flow에서 Service는 무엇을 담당하는가?

A. Business Logic, Transaction, Authorization Check, Domain Rule 처리를 담당한다.

Q. API Flow를 문서에 포함해야 하는 이유는?

A. Agent가 API 구조와 Backend Layer 역할을 정확히 검색하고 코드 생성에 활용하기 위해서이다.

---

# 3. REST Foundation

## 3.1 REST

### [개념]

REST(Representational State Transfer)는 Resource를 중심으로 API를 설계하는 Architecture Style이다.

REST API는 Resource를 URI로 표현하고, HTTP Method로 행위를 표현한다.

```text
Resource = /users
Action   = GET, POST, PUT, PATCH, DELETE
```

---

### [핵심]

- REST는 Resource 중심 설계이다.
- URI는 Resource를 표현한다.
- HTTP Method는 행위를 표현한다.
- Server는 Stateless하게 Request를 처리한다.
- Response는 Resource의 현재 상태 또는 처리 결과를 반환한다.

---

### [실무]

2026 실무 기준 REST API는 완벽한 이론 준수보다 일관된 Resource URI, 명확한 HTTP Method, 적절한 Status Code, 안정적인 Error Response를 우선한다.

RESTful API는 다음 기준을 만족해야 한다.

- Resource 중심 URI 사용
- 명사 기반 URI 사용
- 복수형 Resource 권장
- HTTP Method 역할 구분
- Stateless Request 처리
- 일관된 Response Schema
- 일관된 Error Response Schema

---

### [예제]

```text
GET    /users        → 사용자 목록 조회
GET    /users/{id}   → 사용자 단건 조회
POST   /users        → 사용자 생성
PUT    /users/{id}   → 사용자 전체 수정
PATCH  /users/{id}   → 사용자 부분 수정
DELETE /users/{id}   → 사용자 삭제
```

---

### [FAQ]

Q. REST API란 무엇인가?

A. Resource를 URI로 표현하고 HTTP Method로 행위를 표현하는 API 설계 방식이다.

Q. RESTful API에서 URI는 무엇을 표현해야 하는가?

A. 행위가 아니라 Resource를 표현해야 한다.

Q. RESTful API에서 행위는 어디에 표현하는가?

A. GET, POST, PUT, PATCH, DELETE 같은 HTTP Method로 표현한다.

---

# 4. Resource

## 4.1 Resource Design

### [개념]

Resource는 API가 다루는 핵심 대상이다.

Resource는 보통 Domain, Entity, Aggregate, Collection과 연결된다.

```text
User Resource
Order Resource
Product Resource
Festival Resource
Review Resource
```

---

### [핵심]

- Resource는 API URI 설계의 중심이다.
- Resource는 명사로 표현한다.
- Resource는 복수형 URI를 권장한다.
- Resource는 Entity와 1:1로만 매핑되지 않아도 된다.
- Resource는 Client가 이해 가능한 단위여야 한다.

---

### [실무]

실무에서는 Database Entity를 그대로 API Resource로 노출하지 않는다.

API Resource는 Client Use Case 기준으로 설계한다.

예를 들어 `Festival` Entity가 있어도 API Resource는 다음처럼 나뉠 수 있다.

```text
/festivals
/festivals/{festivalId}
/festivals/{festivalId}/reviews
/festivals/{festivalId}/likes
/festivals/{festivalId}/location
```

Resource 설계 시 Backend Agent는 Entity Mapping과 API Contract를 구분해야 한다.

---

### [주의]

- URI에 동사를 남발하지 않는다.
- Entity 구조를 그대로 API Response에 노출하지 않는다.
- Client 화면 요구사항을 무시하고 Resource를 설계하지 않는다.
- Resource 이름을 문서마다 다르게 쓰지 않는다.

---

### [FAQ]

Q. Resource는 Entity와 같은 것인가?

A. 항상 같지는 않다. Resource는 API가 외부에 제공하는 대상이고 Entity는 DB와 Domain 내부 모델이다.

Q. URI는 왜 명사로 작성하는가?

A. REST에서는 URI가 Resource를 표현하고 행위는 HTTP Method가 표현하기 때문이다.

Q. Resource를 복수형으로 쓰는 이유는?

A. Collection Resource를 자연스럽게 표현하고 URI 일관성을 유지하기 위해서이다.

---

# 5. Stateless

## 5.1 Stateless API

### [개념]

Stateless는 Server가 Client의 이전 Request 상태를 저장하지 않고, 각 Request를 독립적으로 처리하는 원칙이다.

Client는 Request마다 처리에 필요한 정보를 함께 전달해야 한다.

```text
Request 1 → Server processes independently
Request 2 → Server processes independently
Request 3 → Server processes independently
```

---

### [핵심]

- REST API는 Stateless를 기본 원칙으로 한다.
- Server는 Client Session State에 의존하지 않는다.
- Client는 Token, Parameter, Body 등 필요한 정보를 Request에 포함한다.
- Stateless 구조는 확장성과 장애 대응에 유리하다.
- JWT Authentication은 Stateless API와 잘 맞는다.

---

### [실무]

Spring Boot 3.x + JWT 기반 API에서는 Stateless Session Policy를 사용하는 경우가 많다.

Server는 Session을 저장하지 않고 Access Token을 검증하여 인증 상태를 판단한다.

```text
Client
→ Authorization: Bearer AccessToken
→ Server validates token
→ Authentication resolved
→ API processed
```

Stateless API는 Load Balancing, Horizontal Scaling, Container Deployment 환경에서 유리하다.

---

### [예제]

```http
GET /users/me HTTP/1.1
Authorization: Bearer access-token
```

---

### [FAQ]

Q. Stateless API란 무엇인가?

A. Server가 이전 Request 상태를 저장하지 않고 각 Request를 독립적으로 처리하는 API이다.

Q. Stateless API에서 인증 정보는 어떻게 전달하는가?

A. 보통 Authorization Header에 Bearer Token을 담아 전달한다.

Q. Stateless가 확장성에 유리한 이유는?

A. Server가 Session State를 공유하지 않아도 되므로 여러 서버로 쉽게 확장할 수 있기 때문이다.

---

# 6. API Contract

## 6.1 Contract Based API Design

### [개념]

API Contract는 Client와 Server가 합의한 Request / Response 규칙이다.

Contract는 API의 입력, 출력, 성공, 실패, 인증, 권한, Pagination, Filtering, Sorting 규칙을 포함한다.

---

### [핵심]

- API Contract는 변경에 민감하다.
- Response Field 변경은 Frontend 오류를 만들 수 있다.
- Error Response 불일치는 Client Error Handling을 어렵게 한다.
- API Contract는 OpenAPI 문서로 관리하는 것이 좋다.
- Contract 변경 시 Versioning 또는 Backward Compatibility를 고려한다.

---

### [실무]

실무 API 설계에서는 Controller 구현보다 Contract 정의가 먼저다.

API Contract에 포함할 항목:

| 항목            | 설명               |
| --------------- | ------------------ |
| URI             | Resource 접근 경로 |
| Method          | HTTP Method        |
| Request Header  | 인증, Content-Type |
| Query Parameter | 조회 조건          |
| Path Variable   | Resource 식별자    |
| Request Body    | 생성/수정 데이터   |
| Status Code     | 처리 결과          |
| Response Body   | 응답 데이터        |
| Error Response  | 실패 응답          |
| Authentication  | 인증 필요 여부     |
| Authorization   | 권한 필요 여부     |

---

### [Best Practice]

- API Contract를 먼저 작성한다.
- DTO 이름과 Response Field 이름을 통일한다.
- Error Response Schema를 전역으로 통일한다.
- Status Code 선택 기준을 문서화한다.
- Swagger UI로 API Contract를 검증한다.
- Frontend와 Backend가 같은 Contract를 기준으로 작업한다.

---

### [FAQ]

Q. API Contract란 무엇인가?

A. Client와 Server가 합의한 Request / Response 규칙이다.

Q. API Contract가 깨지면 어떤 문제가 생기는가?

A. Frontend 화면 오류, Error Handling 실패, API 테스트 실패, 배포 장애가 발생할 수 있다.

Q. API Contract는 언제 정의하는 것이 좋은가?

A. Controller 구현 전에 정의하는 것이 좋다.

---

# 7. RESTful API Naming

## 7.1 URI Naming Foundation

### [개념]

URI Naming은 Resource를 명확하고 일관되게 표현하는 규칙이다.

RESTful URI는 동사보다 명사를 사용한다.

```text
Good: /users/{userId}
Bad:  /getUser
```

---

### [핵심]

- URI는 Resource를 표현한다.
- URI에는 명사를 사용한다.
- Resource는 복수형을 권장한다.
- Path Variable은 Resource 식별자에 사용한다.
- Query Parameter는 검색, 필터링, 정렬, 페이지 조건에 사용한다.

---

### [실무]

실무 URI 설계는 단순함과 일관성을 우선한다.

```text
/users
/users/{userId}
/users/{userId}/orders
/products?category=food
/products?sort=createdAt,desc
/products?page=0&size=20
```

URI Naming이 흔들리면 API 검색성, 문서화, 테스트, 유지보수성이 모두 낮아진다.

---

### [주의]

- `/getUsers`처럼 동사를 URI에 넣지 않는다.
- `/userList`처럼 화면 이름 중심으로 작성하지 않는다.
- `/api/user/get/detail`처럼 계층을 불필요하게 깊게 만들지 않는다.
- 같은 Resource에 단수형과 복수형을 섞지 않는다.
- Query Parameter로 Resource 식별자를 대체하지 않는다.

---

### [FAQ]

Q. URI에 get, create, update 같은 동사를 넣어도 되는가?

A. RESTful API에서는 권장하지 않는다. 행위는 HTTP Method로 표현한다.

Q. Path Variable과 Query Parameter의 차이는 무엇인가?

A. Path Variable은 특정 Resource 식별에 사용하고 Query Parameter는 조회 조건에 사용한다.

Q. URI Naming에서 가장 중요한 것은 무엇인가?

A. Resource 중심, 명사 사용, 복수형 일관성이다.

---

# 8. API Design Checklist

## 8.1 Core Checklist

### [Checklist]

API Core Checklist:

- Resource가 명확한가?
- URI가 Resource 중심인가?
- HTTP Method가 행위에 맞는가?
- Request Header가 정의되어 있는가?
- Path Variable이 명확한가?
- Query Parameter가 검색 조건으로 분리되어 있는가?
- Request Body Schema가 정의되어 있는가?
- Response Body Schema가 정의되어 있는가?
- Status Code 기준이 명확한가?
- Error Response Schema가 통일되어 있는가?
- Authentication 필요 여부가 명확한가?
- Authorization 필요 여부가 명확한가?
- Pagination이 필요한 조회 API에 적용되어 있는가?
- Filtering과 Sorting 기준이 정의되어 있는가?
- OpenAPI 문서화가 가능한가?

---

### [실무]

API 검수는 Controller 코드만 보는 것이 아니라 API Contract 전체를 확인해야 한다.

Review Agent는 다음 문제를 우선 탐지해야 한다.

- Method 오사용
- URI Naming 불일치
- Status Code 오사용
- Response Schema 불안정
- Error Response 불일치
- Validation 누락
- Pagination 누락
- Authentication / Authorization 누락
- OpenAPI 문서 누락

---

### [FAQ]

Q. API Review에서 가장 먼저 확인할 것은 무엇인가?

A. Resource, URI, HTTP Method, Status Code, Request / Response Contract이다.

Q. API Design Checklist가 필요한 이유는?

A. API 품질을 일관되게 검수하고 Agent Review 결과를 안정화하기 위해서이다.

Q. API 문서에서 Checklist는 필수인가?

A. 선택 항목이지만 Review Agent 품질 향상을 위해 포함하는 것이 좋다.

---

# 9. Common Mistakes

## 9.1 API Core Mistakes

### [Troubleshooting]

문제: URI에 동사를 사용한다.

원인: Resource 중심 설계가 아니라 행위 중심으로 API를 설계했다.

해결: URI는 명사 Resource로 작성하고 행위는 HTTP Method로 표현한다.

---

문제: Response Schema가 API마다 다르다.

원인: 공통 Response Contract가 정의되지 않았다.

해결: Success Response와 Error Response Schema를 전역 규칙으로 통일한다.

---

문제: Frontend에서 API 연동 중 Field 오류가 발생한다.

원인: Response DTO Field 이름과 Frontend 사용 Field 이름이 다르다.

해결: API Contract를 먼저 고정하고 DTO / Frontend Type / Swagger 문서를 일치시킨다.

---

문제: 인증이 필요한 API가 공개되어 있다.

원인: Authentication / Authorization 기준이 API Contract에 누락되었다.

해결: API별 인증 필요 여부와 권한 요구사항을 명시한다.

---

문제: 목록 조회 API가 느리다.

원인: Pagination 없이 전체 데이터를 반환한다.

해결: Page / Size 또는 Cursor 기반 Pagination을 적용한다.

---

### [FAQ]

Q. API 설계에서 가장 흔한 실수는 무엇인가?

A. URI Naming 불일치, Method 오사용, Status Code 오사용, Error Response 불일치, Pagination 누락이다.

Q. API Response Field 변경은 왜 위험한가?

A. Frontend가 기존 Field에 의존하고 있을 수 있어 화면 오류가 발생할 수 있기 때문이다.

Q. API Contract 오류를 줄이는 방법은?

A. OpenAPI 문서화, DTO 통일, Error Response 표준화, Review Checklist 적용이 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. API란 무엇인가?
A. Client와 Server가 정해진 Request / Response Contract에 따라 데이터를 주고받기 위한 Interface이다.

Q. API Design이란 무엇인가?
A. URI, Method, Request, Response, Status Code, Error Response를 포함한 API Contract를 설계하는 작업이다.

Q. REST API란 무엇인가?
A. Resource를 URI로 표현하고 HTTP Method로 행위를 표현하는 API 설계 방식이다.

Q. RESTful API의 핵심은 무엇인가?
A. Resource 중심 URI, HTTP Method 역할 구분, Stateless 처리, 일관된 Response Contract이다.

Q. Resource란 무엇인가?
A. API가 외부에 제공하는 핵심 대상이며 URI 설계의 중심이다.

Q. Resource와 Entity는 같은가?
A. 항상 같지는 않다. Resource는 API 외부 표현이고 Entity는 내부 Domain 또는 DB 모델이다.

Q. Stateless API란 무엇인가?
A. Server가 Client의 이전 Request 상태를 저장하지 않고 각 Request를 독립적으로 처리하는 API이다.

Q. API Contract란 무엇인가?
A. Client와 Server가 합의한 Request / Response 규칙이다.

Q. API Contract에 포함되는 것은 무엇인가?
A. URI, Method, Header, Query Parameter, Path Variable, Request Body, Status Code, Response Body, Error Response, Authentication, Authorization이다.

Q. URI Naming 원칙은 무엇인가?
A. 명사 Resource를 사용하고 복수형을 권장하며 행위는 HTTP Method로 표현한다.

Q. Path Variable은 언제 사용하는가?
A. 특정 Resource를 식별할 때 사용한다.

Q. Query Parameter는 언제 사용하는가?
A. 검색, 필터링, 정렬, 페이지 조건을 표현할 때 사용한다.

Q. API Review에서 무엇을 확인해야 하는가?
A. Resource, URI, HTTP Method, Status Code, Request / Response Contract, Error Response, Validation, Pagination을 확인해야 한다.

Q. API Design에서 자주 발생하는 실수는 무엇인가?
A. URI Naming 불명확, Method 오사용, Status Code 오사용, Error Contract 불일치, Pagination 누락, Validation 부족이다.

Q. API 문서화는 무엇으로 하는가?
A. OpenAPI 3.x 또는 Swagger UI를 사용한다.

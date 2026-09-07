# Frontend Architecture Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Architecture Domain 목적

### [개념]

Frontend Architecture Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent용 RAG 문서 제작 규칙이다.

Frontend Architecture는 프론트엔드 애플리케이션의 폴더 구조, 레이어 분리, 모듈 경계, 상태 관리, 데이터 흐름, API 연동, 인증 흐름, UI 시스템, 테스트, 성능, 보안 기준을 설계하는 영역이다.

목적:

- 프론트엔드 프로젝트 구조 설계 지원
- Feature-based Architecture 설계 지원
- Layered Architecture 설계 지원
- Component Boundary 판단 지원
- Server State / Client State 분리 지원
- API Client / Data Fetching 구조 설계 지원
- Authentication Frontend Flow 설계 지원
- Routing / Layout 구조 설계 지원
- Design System / UI Layer 분리 지원
- 테스트 가능한 구조 설계 지원
- 유지보수 가능한 모듈 경계 설계 지원
- Frontend 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Project Structure
2. Feature-based Architecture
3. Layer Boundary
4. Component Architecture
5. Data Flow
6. State Management Boundary
7. API Layer
8. Routing / Layout
9. Authentication Flow
10. Design System / UI Layer
11. Error / Loading / Empty State
12. Testing Architecture
13. Performance Architecture
14. Security Architecture
15. Scalability / Maintainability
16. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / Next.js App Router / TypeScript 기준 우선
- 기능 단위 Feature 구조 우선 검토
- 작은 프로젝트는 단순 구조 허용
- 큰 프로젝트는 Layer / Feature 경계 명확화
- UI Component와 Business Component 분리
- API 호출 로직과 화면 컴포넌트 분리
- Server State와 Client State 구분
- 인증 / 권한 검사는 서버와 클라이언트 역할을 분리
- 공통 컴포넌트는 Design System 또는 Shared UI로 분리
- 도메인 로직은 화면 컴포넌트에 직접 몰아넣지 않음
- 테스트 가능한 구조를 우선
- 절대적인 폴더 구조보다 의존성 방향과 책임 분리가 중요
- Agent가 구조 설계, 코드 생성, 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Architecture 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 프로젝트의 폴더 구조, 레이어, 컴포넌트 경계, 상태 관리, API 연동, 인증, 테스트, 성능 기준을 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. Frontend Architecture는 단순 폴더 구조 문서인가?

A.
아니다. 폴더 구조뿐 아니라 의존성 방향, 상태 흐름, 데이터 흐름, 모듈 책임, 테스트 가능성까지 포함한다.

Q. Frontend Architecture 문서는 Next.js 전용인가?

A.
아니다. React 기반 프론트엔드 전반에 적용하되, Next.js App Router와 연계 가능한 기준을 포함한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Architecture Domain은 프론트엔드 애플리케이션이 커져도 유지보수 가능한 구조를 만들기 위한 설계 기준을 포함한다.

---

### [핵심]

포함 범위:

- Project Structure
- Feature-based Architecture
- Layered Architecture
- Modular Architecture
- Component Architecture
- Container / Presentational Pattern
- Design System Layer
- Shared UI Layer
- Feature Module
- Domain Module
- API Layer
- Data Fetching Layer
- Server State
- Client State
- URL State
- Form State
- Global State
- Routing Architecture
- Layout Architecture
- Authentication Flow
- Authorization UI
- Error Handling Architecture
- Loading / Empty State
- TypeScript Structure
- Import Boundary
- Dependency Direction
- Barrel Export
- Path Alias
- Monorepo 연계 기초
- Testing Architecture
- Performance Architecture
- Security Architecture
- Build / Environment Structure
- Code Review Checklist

---

### [실무]

제외 범위:

- React 기초 문법 전체
- Next.js App Router 상세 전체
- CSS 세부 구현 전체
- Design System 심화 전체
- Redux / Zustand / TanStack Query 심화
- Backend Architecture 심화
- DevOps / Kubernetes 심화
- Micro Frontend 심화
- Module Federation 심화
- Monorepo 심화
- 브라우저 렌더링 엔진 내부 심화

단, Frontend Architecture 판단에 필요한 수준의 React / Next.js / 상태 관리 / 테스트 / 보안 지식은 포함 가능하다.

---

### [FAQ]

Q. Frontend Architecture 문서에 상태 관리 라이브러리도 포함해야 하나?

A.
라이브러리 심화는 제외한다. 다만 Server State, Client State, Global State를 구분하고 어떤 도구를 선택할지 판단 기준은 포함한다.

Q. Design System도 이 문서에 포함하나?

A.
심화 구현은 별도 문서로 분리하되, Frontend Architecture에서는 UI Layer와 Shared Component 경계 기준을 포함한다.

Q. Monorepo도 포함해야 하나?

A.
심화는 별도 문서로 분리한다. 이 문서에서는 패키지 분리와 의존성 경계 판단 기준만 기초적으로 포함한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Architecture RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Frontend Architecture 문서는 구조 판단이 핵심이므로 아래 Section을 적극 사용한다.

- `[Flow]`: User Action → UI → State → API → Response → Render
- `[Comparison]`: Feature-based vs Layer-based
- `[Best Practice]`: 의존성 방향, 모듈 책임, 상태 분리
- `[Troubleshooting]`: 순환 참조, 모듈 경계 붕괴, 상태 중복
- `[Checklist]`: 구조 리뷰, 성능 리뷰, 보안 리뷰

---

### [FAQ]

Q. Frontend Architecture 문서에 Flow가 필요한 이유는?

A.
프론트엔드 구조는 이벤트, 상태, API, 렌더링 흐름이 연결되어 있으므로 Flow가 있어야 Agent가 코드 구조를 정확히 판단할 수 있다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Architecture Principles Rules

## 4.1 프론트엔드 아키텍처 원칙

### [개념]

Frontend Architecture 원칙은 코드가 커져도 변경 영향 범위가 작고, 기능을 찾기 쉬우며, 테스트와 리뷰가 쉬운 구조를 만드는 기준이다.

---

### [핵심]

필수 원칙:

- Separation of Concerns
- Single Responsibility
- Explicit Dependency
- Predictable Data Flow
- Feature Encapsulation
- Reusable UI
- Testability
- Scalability
- Maintainability
- Low Coupling
- High Cohesion
- Domain Boundary
- Stable Interface
- Incremental Refactoring

---

### [실무]

설계 기준:

- 기능별 책임을 명확히 분리
- 컴포넌트가 API 호출, 상태 관리, UI 표시를 모두 담당하지 않도록 분리
- 공통 코드는 Shared Layer로 이동
- Feature 내부 구현은 외부에서 직접 의존하지 않기
- 의존성 방향은 상위 정책에서 하위 구현으로 흐르지 않게 관리
- 모듈 간 import 규칙을 문서화
- 변경이 잦은 영역과 안정적인 영역 분리
- 비즈니스 로직은 테스트 가능한 함수 / Hook / Service로 분리
- UI Component는 가능한 재사용 가능한 API를 갖도록 설계

---

### [FAQ]

Q. Frontend Architecture의 가장 중요한 원칙은?

A.
책임 분리와 예측 가능한 데이터 흐름이다. 코드가 커져도 어디를 수정해야 하는지 명확해야 한다.

Q. 좋은 프론트엔드 구조의 기준은?

A.
기능을 찾기 쉽고, 변경 영향이 작고, 테스트가 가능하며, 모듈 간 의존성이 명확한 구조이다.

Q. 아키텍처는 처음부터 복잡하게 잡아야 하나?

A.
아니다. 프로젝트 규모에 맞게 시작하고, 기능이 커질 때 점진적으로 Feature / Layer 경계를 강화한다.

---

# 5. Project Structure Rules

## 5.1 프로젝트 폴더 구조

### [개념]

Project Structure는 코드 검색, 책임 분리, 모듈 경계, 팀 협업에 직접 영향을 주는 기본 구조이다.

---

### [핵심]

필수 포함:

- `app` 또는 `pages`
- `features`
- `entities`
- `shared`
- `components`
- `hooks`
- `lib`
- `services`
- `api`
- `types`
- `utils`
- `constants`
- `styles`
- `tests`
- `public`
- `config`

권장 구조 예시:

```text
src
├ app
├ features
│  └ auth
│     ├ api
│     ├ components
│     ├ hooks
│     ├ model
│     └ types
├ shared
│  ├ ui
│  ├ api
│  ├ lib
│  ├ hooks
│  ├ types
│  └ config
├ entities
│  └ user
│     ├ model
│     ├ api
│     └ types
└ widgets
```

---

### [실무]

구조 선택 기준:

| 프로젝트 규모      | 권장 구조                                     |
| ------------------ | --------------------------------------------- |
| 작은 프로젝트      | 단순 `components`, `hooks`, `api` 구조        |
| 중간 프로젝트      | Feature-based 구조                            |
| 큰 프로젝트        | Feature + Layer 혼합 구조                     |
| 도메인 복잡도 높음 | Entity / Feature / Shared 분리                |
| 팀 규모 큼         | 명확한 Import Boundary 필요                   |
| Next.js App Router | `app`은 라우팅, 기능 코드는 `features`로 분리 |

주의:

- 초기에 과도한 구조화 금지
- 모든 파일을 `components`에 몰아넣기 금지
- `utils`가 잡동사니 폴더가 되지 않도록 관리
- 공통화 기준 없이 `shared`에 넣지 않기
- Feature 내부 구현을 외부에서 깊게 import하지 않기

---

### [FAQ]

Q. 프론트엔드 폴더 구조는 어떻게 잡아야 하나?

A.
작은 프로젝트는 단순 구조로 시작하고, 기능이 많아지면 `features`, `shared`, `entities` 같은 Feature-based 구조로 분리한다.

Q. Next.js App Router에서는 모든 코드를 `app` 안에 넣어야 하나?

A.
아니다. `app`은 라우팅과 페이지 조립 중심으로 두고, 기능 로직과 UI는 `features`나 `shared`로 분리하는 것이 좋다.

Q. `utils` 폴더는 왜 위험한가?

A.
역할이 불분명한 코드가 모이기 쉽다. 날짜, 문자열, 검증, 포맷터처럼 목적별로 분리하는 것이 좋다.

---

# 6. Feature-based Architecture Rules

## 6.1 Feature 중심 구조

### [개념]

Feature-based Architecture는 기능 단위로 API, UI, 상태, 타입, Hook을 함께 묶어 응집도를 높이는 구조이다.

---

### [핵심]

필수 포함:

- Feature Module
- Feature Boundary
- Feature API
- Feature Component
- Feature Hook
- Feature Model
- Feature Types
- Feature Test
- Public API
- Internal Implementation
- Encapsulation

Feature 구조 예시:

```text
features
└ create-post
   ├ api
   │  └ createPost.ts
   ├ components
   │  └ CreatePostForm.tsx
   ├ hooks
   │  └ useCreatePost.ts
   ├ model
   │  └ createPostSchema.ts
   ├ types
   │  └ createPostTypes.ts
   ├ index.ts
   └ README.md
```

---

### [실무]

Feature Module 작성 기준:

- 하나의 Feature는 사용자 행동 또는 기능 단위
- Feature 내부에는 해당 기능에 필요한 API / UI / Hook / Type 배치
- 외부 공개는 `index.ts`에서 제한
- 내부 파일 경로 깊은 import 금지
- Feature 간 직접 의존 최소화
- 공통 로직은 `shared`로 이동
- 도메인 객체는 `entities`로 이동 가능
- Feature 테스트는 Feature 내부 또는 테스트 폴더에 배치

좋은 Feature 예시:

- `login`
- `signup`
- `create-post`
- `edit-profile`
- `favorite-festival`
- `checkout-donation`
- `search-products`

나쁜 Feature 예시:

- `button`
- `modal`
- `date-format`
- `api-client`

---

### [FAQ]

Q. Feature-based Architecture는 언제 쓰나?

A.
기능이 많아지고 화면, API, 상태 로직이 섞이기 시작할 때 사용한다.

Q. Feature는 어떤 단위로 나누나?

A.
사용자 행동이나 비즈니스 기능 단위로 나눈다. 예를 들어 로그인, 게시글 작성, 프로필 수정 같은 단위가 적합하다.

Q. Feature 내부 파일을 외부에서 직접 import해도 되나?

A.
권장하지 않는다. Feature의 Public API를 통해 필요한 것만 노출하는 것이 좋다.

---

# 7. Layered Architecture Rules

## 7.1 Layer 분리 기준

### [개념]

Layered Architecture는 코드의 책임을 UI, Feature, Entity, Shared, API, Config 같은 계층으로 나누는 구조이다.

---

### [핵심]

주요 Layer:

- App Layer
- Page Layer
- Widget Layer
- Feature Layer
- Entity Layer
- Shared Layer
- API Layer
- Config Layer

Layer 책임:

| Layer   | 책임                             |
| ------- | -------------------------------- |
| App     | 라우팅, Provider, 전역 설정      |
| Page    | Route 단위 화면 조립             |
| Widget  | 여러 Feature를 조합한 큰 UI 블록 |
| Feature | 사용자 행동 단위 기능            |
| Entity  | 도메인 데이터 단위               |
| Shared  | 공통 UI, 공통 Hook, 공통 Lib     |
| API     | HTTP Client, Request, Response   |
| Config  | 환경변수, 설정값                 |

---

### [실무]

의존성 방향 예시:

```text
App
→ Page
→ Widget
→ Feature
→ Entity
→ Shared
```

규칙:

- 하위 Layer는 상위 Layer를 import하지 않음
- Shared는 Feature를 import하지 않음
- Entity는 Feature를 import하지 않음
- Feature는 다른 Feature에 직접 의존하지 않도록 주의
- Page는 Feature와 Widget을 조립할 수 있음
- App Layer는 Provider와 Router 구성 중심
- API Client는 Shared 또는 Feature 내부에 배치

주의:

- Layer 규칙은 팀이 이해할 수 있을 정도로 단순해야 함
- 작은 프로젝트에 복잡한 Layer 강제 금지
- 순환 참조가 생기면 Layer 경계 재검토
- 공통 Layer가 비대해지면 도메인별 분리 검토

---

### [FAQ]

Q. Layered Architecture에서 가장 중요한 것은?

A.
의존성 방향이다. 하위 Layer가 상위 Layer를 import하지 않도록 해야 구조가 무너지지 않는다.

Q. Feature가 다른 Feature를 import해도 되나?

A.
가능하면 피한다. 공통 로직은 Shared나 Entity로 올리고, Page나 Widget에서 Feature를 조합하는 것이 좋다.

Q. Shared Layer에는 무엇을 넣나?

A.
공통 UI, 공통 Hook, API Client, 유틸, 타입, 설정처럼 여러 Feature에서 재사용되는 안정적인 코드를 넣는다.

---

# 8. Component Architecture Rules

## 8.1 Component Layer 설계

### [개념]

Component Architecture는 UI 컴포넌트를 역할과 책임에 따라 분리하는 설계 기준이다.

---

### [핵심]

컴포넌트 분류:

- Page Component
- Layout Component
- Feature Component
- Container Component
- Presentational Component
- UI Component
- Form Component
- List Component
- Item Component
- Boundary Component
- Provider Component

역할 기준:

| 컴포넌트          | 책임                         |
| ----------------- | ---------------------------- |
| Page              | Route 단위 화면 조립         |
| Layout            | 공통 레이아웃                |
| Container         | 데이터 / 상태 연결           |
| Presentational    | UI 표시                      |
| UI Component      | 재사용 가능한 순수 UI        |
| Feature Component | 특정 기능 UI                 |
| Boundary          | Error / Suspense / Auth 경계 |
| Provider          | Context / Dependency 제공    |

---

### [실무]

설계 기준:

- Page는 조립 역할 중심
- UI Component는 비즈니스 로직 최소화
- Feature Component는 특정 기능 흐름 담당
- Container는 데이터 조회와 상태 연결 담당
- Presentational Component는 props 기반 렌더링 담당
- Form Component는 입력 상태와 검증 책임 명확화
- Error / Loading / Empty State를 별도 컴포넌트로 분리 가능
- 너무 작은 컴포넌트 분리는 오히려 탐색 비용 증가

주의:

- Page에 모든 로직 몰아넣기 금지
- UI Component에서 API 직접 호출 금지
- 공통 컴포넌트에 비즈니스 조건 넣기 금지
- Feature Component를 Shared UI로 성급히 승격 금지
- 컴포넌트 이름은 역할을 드러내야 함

---

### [FAQ]

Q. Page Component는 어떤 역할을 해야 하나?

A.
Route 단위 화면을 조립하고 필요한 Feature, Widget, Layout을 연결하는 역할을 한다.

Q. UI Component에서 API를 호출해도 되나?

A.
권장하지 않는다. UI Component는 재사용 가능한 표시와 상호작용에 집중하고 API 호출은 Feature나 Container에서 처리하는 것이 좋다.

Q. 컴포넌트는 작을수록 좋은가?

A.
항상 그렇지는 않다. 책임이 명확해지는 수준으로 나누되, 과도한 분리는 탐색 비용을 높인다.

---

# 9. Data Flow Rules

## 9.1 데이터 흐름 설계

### [개념]

Data Flow는 사용자 액션, 상태 변경, API 요청, 응답 처리, UI 렌더링이 어떤 순서로 연결되는지 정의하는 구조이다.

---

### [핵심]

기본 Flow:

```text
User Action
→ Event Handler
→ State Update or Action
→ API Request
→ Server Response
→ Cache Update / Revalidation
→ UI Render
```

필수 포함:

- Unidirectional Data Flow
- User Action
- Event Handler
- State Update
- API Request
- Response Mapping
- Error Handling
- Loading State
- Cache Update
- UI Render
- Side Effect Boundary

---

### [실무]

Data Flow 작성 기준:

- 데이터 흐름은 단방향으로 유지
- UI 이벤트와 API 요청의 연결 지점 명확화
- 응답 데이터를 View Model로 변환할 수 있음
- Error / Loading / Empty State를 별도 상태로 처리
- Mutation 후 Cache Invalidation 또는 Revalidation 수행
- Server State와 Client State를 혼동하지 않기
- Side Effect는 Hook, Action, Service로 분리
- 컴포넌트 렌더링 중 Side Effect 실행 금지

---

### [FAQ]

Q. 프론트엔드 데이터 흐름은 어떻게 설계해야 하나?

A.
사용자 액션에서 상태 변경 또는 API 요청으로 이어지고, 응답 처리 후 UI가 다시 렌더링되는 단방향 흐름으로 설계한다.

Q. Side Effect는 어디에 두는 게 좋은가?

A.
컴포넌트 렌더링 내부가 아니라 Hook, Action, Service, Event Handler 같은 명확한 경계에 둔다.

Q. API 응답을 그대로 화면에 써도 되나?

A.
단순한 경우 가능하지만 화면 요구와 서버 응답이 다르면 View Model로 변환하는 것이 좋다.

---

# 10. State Architecture Rules

## 10.1 상태 분류와 위치

### [개념]

State Architecture는 프론트엔드 상태를 성격별로 분류하고 적절한 위치와 도구를 선택하는 설계 기준이다.

---

### [핵심]

상태 분류:

- Local UI State
- Shared UI State
- Global UI State
- Server State
- URL State
- Form State
- Auth State
- Derived State
- Persistent State

상태별 권장 위치:

| 상태             | 예시              | 권장 위치                      |
| ---------------- | ----------------- | ------------------------------ |
| Local UI State   | Modal open        | Component                      |
| Shared UI State  | selected tab      | Parent / Context               |
| Global UI State  | theme             | Context / Store                |
| Server State     | posts, user list  | Server Component / Query Cache |
| URL State        | search, page      | URL Search Params              |
| Form State       | input, validation | Form Component / Form Library  |
| Auth State       | current user      | Server Session / Auth Provider |
| Derived State    | filtered list     | 계산값                         |
| Persistent State | preference        | localStorage / cookie          |

---

### [실무]

상태 설계 기준:

- 상태는 사용하는 위치와 가장 가까운 곳에 둔다
- 서버 데이터는 Server State로 분리
- URL과 공유해야 하는 값은 URL State로 관리
- Form 입력은 Form State로 분리
- Derived State는 중복 저장하지 않음
- 인증 상태는 보안 경계와 연결
- 전역 상태는 최소화
- Context는 변경 빈도가 낮은 공유 값에 적합
- 복잡한 비동기 서버 데이터는 Query Cache 도구 고려

---

### [FAQ]

Q. 프론트엔드 상태는 어떻게 분류해야 하나?

A.
Local UI State, Server State, URL State, Form State, Auth State, Global UI State, Derived State로 구분한다.

Q. 모든 상태를 Zustand나 Redux에 넣어도 되나?

A.
권장하지 않는다. 서버 데이터, URL 상태, Form 상태, Local UI 상태는 각각 적합한 위치가 다르다.

Q. 검색 조건은 어디에 저장하는 게 좋나?

A.
공유 가능한 페이지 상태라면 URL Search Params에 저장하는 것이 좋다.

---

# 11. API Layer Rules

## 11.1 API Client 구조

### [개념]

API Layer는 프론트엔드에서 Backend API와 통신하는 코드의 위치, 책임, 에러 처리, 타입 변환 기준을 정의한다.

---

### [핵심]

필수 포함:

- API Client
- HTTP Client
- Fetch Wrapper
- Axios Instance
- Request Config
- Response Type
- Error Mapping
- Auth Header
- Token Refresh
- Timeout
- Retry
- Base URL
- Environment Variable
- API Module
- DTO
- View Model

API Layer 구조 예시:

```text
shared
└ api
   ├ client.ts
   ├ error.ts
   └ types.ts

features
└ posts
   └ api
      ├ getPosts.ts
      ├ createPost.ts
      └ post.dto.ts
```

---

### [실무]

API Layer 작성 기준:

- HTTP Client 설정은 공통화
- Feature별 API 함수는 Feature 내부에 배치 가능
- Request / Response 타입 명시
- API Error를 UI가 처리 가능한 형태로 변환
- 인증 헤더 주입 위치 명확화
- Token Refresh 로직은 중복 구현 금지
- Timeout / Abort / Retry 정책 검토
- API URL은 환경변수로 관리
- 서버 DTO와 화면 View Model을 분리할 수 있음
- API 함수 이름은 동작 중심으로 작성

예시:

```ts
export async function getPostList(): Promise<PostListItem[]> {
  const response = await apiClient.get<PostListResponse>("/posts");
  return response.data.items.map(toPostListItem);
}
```

---

### [FAQ]

Q. API 호출 코드는 어디에 둬야 하나?

A.
공통 HTTP Client는 `shared/api`에 두고, 기능별 API 함수는 해당 Feature의 `api` 폴더에 두는 방식이 좋다.

Q. API 응답 타입과 화면 타입은 같아야 하나?

A.
항상 같을 필요는 없다. 서버 DTO와 화면 View Model이 다르면 변환 함수를 두는 것이 좋다.

Q. Token Refresh는 각 API 함수마다 넣어야 하나?

A.
아니다. HTTP Client interceptor나 공통 wrapper에서 처리하는 것이 좋다.

---

# 12. Data Fetching Architecture Rules

## 12.1 Data Fetching 구조

### [개념]

Data Fetching Architecture는 데이터를 언제, 어디서, 어떤 방식으로 가져오고 캐시하며 UI 상태와 연결할지 정의한다.

---

### [핵심]

필수 포함:

- Server-side Fetching
- Client-side Fetching
- Query Cache
- Mutation
- Cache Invalidation
- Revalidation
- Loading State
- Error State
- Empty State
- Pagination
- Infinite Scroll
- Optimistic Update
- Background Refetch

판단 기준:

| 상황                      | 권장 방식                 |
| ------------------------- | ------------------------- |
| 초기 페이지 데이터        | Server Component / Loader |
| 사용자 이벤트 기반 데이터 | Client Fetch / Query      |
| SEO 중요 데이터           | Server-side Fetching      |
| 실시간성 높은 데이터      | Client Fetch / WebSocket  |
| Mutation                  | Action / Mutation Hook    |
| 목록 캐시                 | Query Cache               |
| Form Submit               | Server Action / Mutation  |
| 검색 Query                | URL State + Fetch         |

---

### [실무]

작성 기준:

- 데이터 조회 위치를 명확히 결정
- Server State는 Client State와 분리
- Query Key 또는 Cache Key 설계 포함
- Mutation 후 Invalidation / Revalidation 처리
- Loading / Error / Empty State 필수
- 페이지네이션과 무한 스크롤은 API 계약과 함께 설계
- 중복 요청 방지
- Abort / Race Condition 고려
- Optimistic Update는 rollback 포함
- 사용자별 데이터 Cache 보안 주의

---

### [FAQ]

Q. 데이터 패칭은 컴포넌트 안에서 바로 해도 되나?

A.
단순한 경우 가능하지만, 반복되거나 복잡해지면 API 함수와 Fetch Hook / Server Function으로 분리하는 것이 좋다.

Q. Server State와 Client State 차이는?

A.
Server State는 서버에서 온 데이터이고, Client State는 UI 상호작용이나 브라우저 상태를 표현하는 데이터이다.

Q. Mutation 후 목록이 갱신되지 않으면 무엇을 확인해야 하나?

A.
Cache Invalidation, Revalidation, Query Key, Router Refresh 여부를 확인해야 한다.

---

# 13. Routing and Layout Architecture Rules

## 13.1 Routing / Layout 구조

### [개념]

Routing Architecture는 URL 구조와 페이지 구성 방식을 정의하고, Layout Architecture는 공통 UI와 화면 조립 경계를 정의한다.

---

### [핵심]

필수 포함:

- Route Structure
- Nested Route
- Dynamic Route
- Route Group
- Protected Route
- Public Route
- Layout
- Nested Layout
- Page Composition
- Navigation
- Breadcrumb
- Search Params
- Route Params

URL 구조 예시:

```text
/
├ /login
├ /signup
├ /dashboard
├ /dashboard/settings
├ /posts
├ /posts/[postId]
└ /admin/users
```

---

### [실무]

설계 기준:

- URL은 사용자와 도메인 관점에서 설계
- Layout은 반복 UI를 공유
- 인증 영역과 공개 영역 분리
- 관리자 영역은 별도 Route Group 또는 Layout 분리
- Dynamic Route는 타입과 검증 포함
- Search Params는 필터, 정렬, 페이지네이션에 사용
- Page는 Feature와 Widget 조립 역할
- Layout에 무거운 비즈니스 로직 과다 배치 금지
- Navigation 권한 표시와 실제 권한 검사는 분리

---

### [FAQ]

Q. Routing 구조는 어떻게 설계해야 하나?

A.
사용자 입장에서 이해 가능한 URL을 먼저 설계하고, 공개 영역, 인증 영역, 관리자 영역을 Layout과 Route Group으로 분리한다.

Q. Layout에는 무엇을 넣어야 하나?

A.
Header, Sidebar, Footer, Auth Guard, 공통 Provider처럼 하위 페이지가 공유하는 요소를 넣는다.

Q. Search Params는 언제 쓰나?

A.
검색어, 필터, 정렬, 페이지 번호처럼 URL로 공유하거나 복원해야 하는 상태에 사용한다.

---

# 14. Authentication Frontend Architecture Rules

## 14.1 인증 / 권한 프론트엔드 구조

### [개념]

Authentication Frontend Architecture는 로그인 상태 확인, 보호 Route, Token 처리, 권한별 UI 표시, API 인증 헤더 연결 구조를 정의한다.

---

### [핵심]

필수 포함:

- Login Flow
- Logout Flow
- Signup Flow
- Current User
- Session
- Token
- Cookie
- JWT
- Refresh Token
- Protected Route
- Role-based UI
- Auth Provider
- Auth Guard
- Redirect
- API Auth Header
- Unauthorized State

기본 Flow:

```text
User Login
→ Submit Credentials
→ Server Auth
→ Store Session / Token
→ Fetch Current User
→ Render Protected UI
```

---

### [실무]

인증 구조 기준:

- 인증 검증은 서버 기준으로 신뢰
- Client Auth State는 UX 개선용
- Token 저장 위치는 보안 기준으로 결정
- HttpOnly Cookie 사용 시 Client에서 Token 직접 접근하지 않음
- Authorization Header 주입 위치를 공통화
- Refresh Token 처리 중 중복 요청 방지
- 권한별 메뉴 표시와 실제 API 권한 검사는 분리
- 보호 페이지 접근 시 Redirect 처리
- 401 / 403 Error Handling 분리
- Logout 시 Client Cache / Auth State 정리

주의:

- Local Storage Token 저장은 XSS 위험 검토
- Client에서 Role만 보고 보안 판단 금지
- Token을 Console / Error Log에 출력 금지
- Refresh 실패 시 명확히 로그아웃 처리
- 인증 로직을 여러 Feature에 중복 구현 금지

---

### [FAQ]

Q. 프론트엔드에서 인증 상태는 어떻게 관리해야 하나?

A.
서버 세션이나 Token을 기준으로 현재 사용자를 확인하고, Client Auth State는 화면 표시와 UX 개선용으로 사용한다.

Q. 권한별 버튼을 숨기면 보안 처리가 된 건가?

A.
아니다. 버튼 숨김은 UX일 뿐이고 실제 권한 검사는 서버 API와 Server Action에서 해야 한다.

Q. 401과 403은 어떻게 다르게 처리하나?

A.
401은 인증 필요 또는 세션 만료, 403은 인증은 되었지만 권한이 없는 상태로 처리한다.

---

# 15. UI Layer and Design System Rules

## 15.1 UI Layer 분리

### [개념]

UI Layer는 공통 버튼, 입력, 모달, 카드, 레이아웃 컴포넌트처럼 여러 기능에서 재사용되는 화면 요소를 관리하는 계층이다.

---

### [핵심]

필수 포함:

- Shared UI
- Design System
- Base Component
- Composite Component
- Variant
- Theme
- Token
- Accessibility
- Storybook
- Component API
- Style Boundary

UI Layer 구조 예시:

```text
shared
└ ui
   ├ button
   │  ├ Button.tsx
   │  ├ Button.test.tsx
   │  └ index.ts
   ├ input
   ├ modal
   └ card
```

---

### [실무]

UI Layer 기준:

- 공통 UI에는 비즈니스 로직을 넣지 않음
- 공통 UI는 props 기반으로 동작
- 접근성 기본값 포함
- variant / size / disabled / loading 상태 정의
- Feature 전용 UI는 Feature 내부에 유지
- 반복 사용이 확인된 후 Shared UI로 승격
- 스타일 토큰과 컴포넌트 API를 분리
- Storybook 또는 문서화 권장
- Button과 Link의 역할 구분

주의:

- 모든 컴포넌트를 공통화하지 않기
- 비즈니스 조건이 들어간 컴포넌트는 Shared UI로 부적합
- Variant가 과도하게 많아지면 API 재설계
- 디자인과 기능 책임 혼합 금지

---

### [FAQ]

Q. 어떤 컴포넌트를 Shared UI로 빼야 하나?

A.
여러 Feature에서 반복 사용되고 비즈니스 로직이 없는 Button, Input, Modal, Card 같은 컴포넌트를 Shared UI로 분리한다.

Q. Feature 전용 컴포넌트도 공통 UI로 빼야 하나?

A.
반복 사용이 확인되기 전까지는 Feature 내부에 두는 것이 좋다.

Q. Design System 컴포넌트에 API 호출을 넣어도 되나?

A.
안 된다. Design System 컴포넌트는 UI 표현과 접근성 중심이어야 한다.

---

# 16. TypeScript Architecture Rules

## 16.1 Type 구조 설계

### [개념]

TypeScript Architecture는 프론트엔드 전체 타입 위치, DTO, View Model, Props, Domain Type, Utility Type을 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Domain Type
- DTO Type
- View Model
- Props Type
- API Response Type
- API Request Type
- Form Type
- Utility Type
- Shared Type
- Type Guard
- Schema Validation
- Discriminated Union

구조 예시:

```text
features
└ posts
   ├ types
   │  ├ post.dto.ts
   │  ├ post.model.ts
   │  └ post.view.ts
   └ model
      └ post.schema.ts
```

---

### [실무]

타입 작성 기준:

- API DTO와 화면 View Model 구분 가능
- Feature 전용 타입은 Feature 내부에 둠
- 여러 Feature에서 공유되는 도메인 타입은 Entity 또는 Shared로 이동
- Props 타입은 컴포넌트 가까이에 둘 수 있음
- 복잡한 Form은 Schema 기반 타입 추론 고려
- 외부 API 응답은 런타임 검증 고려
- `any` 지양
- `unknown`은 검증 후 사용
- Union Type으로 상태를 명확히 표현
- Type Guard로 안전한 분기 작성

상태 타입 예시:

```ts
type AsyncState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };
```

---

### [FAQ]

Q. API 응답 타입과 화면 타입은 분리해야 하나?

A.
서버 응답 구조와 화면 요구가 다르면 분리하는 것이 좋다. 변환 함수를 두면 변경 영향이 줄어든다.

Q. 공통 타입은 어디에 둬야 하나?

A.
여러 Feature에서 사용하는 안정적인 타입은 `shared/types` 또는 `entities`에 둔다.

Q. `any`를 써도 되나?

A.
권장하지 않는다. 외부 데이터는 `unknown`으로 받은 뒤 검증하거나 명확한 타입을 선언한다.

---

# 17. Import Boundary Rules

## 17.1 Import / Dependency 규칙

### [개념]

Import Boundary는 모듈 간 의존성 방향을 제한해 구조 붕괴, 순환 참조, 내부 구현 노출을 방지하는 규칙이다.

---

### [핵심]

필수 포함:

- Dependency Direction
- Public API
- Barrel Export
- Path Alias
- Circular Dependency
- Internal Import
- Deep Import
- Layer Boundary
- Feature Boundary
- ESLint Boundary Rule

권장 Import Flow:

```text
app
→ pages/widgets
→ features
→ entities
→ shared
```

금지 예시:

```text
shared → features
entities → features
features/auth → features/payment 내부 구현 직접 import
```

---

### [실무]

Import 규칙:

- Feature 외부에서는 `features/featureName` Public API로 import
- Feature 내부 상세 경로 deep import 금지
- Shared는 Feature를 알면 안 됨
- Entity는 Feature를 알면 안 됨
- 공통 타입과 유틸은 Shared로 이동
- Path Alias는 가독성 향상용으로 사용
- Barrel Export는 공개 API를 제한하는 용도로 사용
- 모든 폴더에 무분별한 `index.ts` 생성 금지
- 순환 참조는 구조 문제로 보고 수정
- ESLint / Boundary Rule로 강제 가능

---

### [FAQ]

Q. Deep Import는 왜 피해야 하나?

A.
모듈 내부 구현에 직접 의존하게 되어 리팩토링이 어려워지고 Feature 경계가 무너질 수 있기 때문이다.

Q. Barrel Export는 항상 좋은가?

A.
아니다. Public API를 명확히 제한할 때 유용하지만, 무분별하게 사용하면 의존성 추적이 어려워질 수 있다.

Q. 순환 참조가 생기면 어떻게 해야 하나?

A.
공통 로직을 Shared나 Entity로 이동하거나 Layer 책임을 재분리해야 한다.

---

# 18. Error Handling Architecture Rules

## 18.1 에러 처리 구조

### [개념]

Error Handling Architecture는 API 실패, 인증 실패, 권한 실패, 렌더링 오류, Form 검증 오류를 사용자와 개발자가 이해 가능한 형태로 처리하는 구조이다.

---

### [핵심]

에러 분류:

- API Error
- Network Error
- Validation Error
- Auth Error
- Authorization Error
- Not Found Error
- Business Error
- Render Error
- Unknown Error

Error Flow:

```text
Error Occurs
→ Classify Error
→ Map to UI Message
→ Log Technical Detail
→ Show Recovery Action
```

---

### [실무]

에러 처리 기준:

- API Error를 공통 Error Type으로 변환
- 사용자 메시지와 개발자 로그 분리
- 401 / 403 / 404 / 500 처리 구분
- Form Validation Error는 Field 단위 표시
- 재시도 가능한 오류는 Retry 제공
- Error Boundary로 렌더링 오류 격리
- 알 수 없는 오류는 안전한 기본 메시지 표시
- 민감한 서버 에러 상세 노출 금지
- 공통 Toast / Alert 정책 정의
- 에러 로깅 / 모니터링 연계 고려

공통 에러 타입 예시:

```ts
type AppError =
  | { type: "network"; message: string }
  | { type: "validation"; fieldErrors: Record<string, string> }
  | { type: "auth"; message: string }
  | { type: "forbidden"; message: string }
  | { type: "notFound"; message: string }
  | { type: "unknown"; message: string };
```

---

### [FAQ]

Q. 프론트엔드 에러 처리는 어떻게 구조화해야 하나?

A.
에러를 네트워크, 검증, 인증, 권한, 404, 서버 오류로 분류하고 UI 메시지와 개발자 로그를 분리한다.

Q. 서버 에러 메시지를 그대로 보여줘도 되나?

A.
권장하지 않는다. 민감 정보가 포함될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Error Boundary는 API 에러도 잡나?

A.
렌더링 중 throw된 에러는 잡을 수 있지만 이벤트 핸들러나 비동기 에러는 별도 처리해야 한다.

---

# 19. Loading and Empty State Architecture Rules

## 19.1 Loading / Empty / Pending 상태

### [개념]

Loading and Empty State Architecture는 데이터 요청 중, 데이터 없음, 사용자 액션 처리 중 상태를 명확히 구분하는 UI 상태 설계 기준이다.

---

### [핵심]

상태 분류:

- Initial Loading
- Background Loading
- Pending Mutation
- Skeleton UI
- Spinner
- Empty State
- Error State
- Disabled State
- Optimistic State
- Success State

Flow:

```text
Request Start
→ Loading
→ Success
→ Empty or Data UI
→ Error if Failed
```

---

### [실무]

작성 기준:

- Loading과 Empty를 혼동하지 않기
- 초기 로딩은 Skeleton UI 권장
- 사용자 액션 중에는 Pending 표시
- 중복 제출 방지를 위해 버튼 disabled 처리
- 빈 목록은 Empty State UI 제공
- Empty State에는 다음 행동 안내 가능
- Background Refetch는 전체 화면 로딩 대신 작은 표시
- Error State에는 Retry 가능 여부 표시
- Optimistic UI는 실패 시 rollback 포함

---

### [FAQ]

Q. Loading State와 Empty State 차이는?

A.
Loading은 데이터를 기다리는 상태이고, Empty는 요청은 성공했지만 표시할 데이터가 없는 상태이다.

Q. Mutation Pending은 Loading과 같은가?

A.
비슷하지만 목적이 다르다. Pending은 사용자의 제출, 저장, 삭제 같은 액션 처리 중 상태이다.

Q. Empty State에는 무엇을 보여줘야 하나?

A.
데이터가 없다는 사실과 사용자가 다음에 할 수 있는 행동을 보여주는 것이 좋다.

---

# 20. Testing Architecture Rules

## 20.1 테스트 구조 설계

### [개념]

Testing Architecture는 프론트엔드 기능을 단위, 컴포넌트, 통합, E2E 수준으로 나누고 어떤 영역을 어떻게 검증할지 정의한다.

---

### [핵심]

테스트 유형:

- Unit Test
- Component Test
- Hook Test
- Integration Test
- E2E Test
- Visual Regression Test
- Accessibility Test
- API Mock Test

테스트 대상:

| 대상             | 테스트 방식             |
| ---------------- | ----------------------- |
| Utility Function | Unit Test               |
| Custom Hook      | Hook Test               |
| UI Component     | Component Test          |
| Feature Flow     | Integration Test        |
| Page Flow        | E2E Test                |
| Form Validation  | Component / Integration |
| API Error        | Mock Test               |
| Auth Flow        | Integration / E2E       |
| Design System    | Component / Visual      |

---

### [실무]

테스트 구조 기준:

- 사용자 행동 중심 테스트 작성
- 구현 세부 state 직접 검증 지양
- Feature별 테스트 배치 가능
- 공통 UI는 독립 Component Test
- API는 Mock으로 제어
- 인증 상태는 Mock Provider 또는 Test Session 사용
- Error / Loading / Empty State 검증
- 접근성 쿼리 사용
- E2E는 핵심 Flow 중심
- Snapshot Test 남용 금지
- 테스트 데이터와 실제 데이터 분리

---

### [FAQ]

Q. 프론트엔드 테스트는 무엇부터 해야 하나?

A.
핵심 사용자 Flow, Form Validation, API Error State, 인증 Flow부터 우선 검증하는 것이 좋다.

Q. 모든 컴포넌트를 테스트해야 하나?

A.
아니다. 비즈니스 영향이 큰 컴포넌트와 재사용 공통 UI를 우선 테스트한다.

Q. E2E 테스트는 많이 작성해야 하나?

A.
핵심 Flow 중심으로 작성한다. 너무 많으면 느리고 유지보수가 어려워질 수 있다.

---

# 21. Performance Architecture Rules

## 21.1 성능 중심 구조 설계

### [개념]

Performance Architecture는 프론트엔드 성능을 코드 구조, 번들 크기, 렌더링 비용, 데이터 패칭, 이미지, 캐시 전략으로 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Bundle Size
- Code Splitting
- Lazy Loading
- Dynamic Import
- Rendering Cost
- Re-render Optimization
- Memoization
- Image Optimization
- Font Optimization
- Cache Strategy
- Prefetch
- Virtualization
- Web Vitals
- Hydration Cost
- Server Rendering
- Client Bundle Reduction

---

### [실무]

성능 설계 기준:

- Route 단위 Code Splitting 활용
- 무거운 라이브러리는 필요한 곳에서만 로드
- 초기 번들에 모든 기능을 넣지 않음
- 공통 컴포넌트에 무거운 의존성 추가 주의
- 큰 리스트는 Virtualization 고려
- 이미지 최적화 적용
- 폰트 로딩 전략 검토
- Hydration 비용을 줄이기 위해 Client Component 범위 최소화
- Cache / Revalidation 전략 명확화
- 불필요한 re-render는 State 위치와 Context 범위부터 점검
- 성능 최적화는 측정 후 적용

---

### [FAQ]

Q. 프론트엔드 성능 최적화는 무엇부터 해야 하나?

A.
초기 번들 크기, 이미지, 데이터 패칭, 불필요한 Client Component, 큰 리스트 렌더링을 우선 확인한다.

Q. Memoization을 많이 쓰면 성능이 좋아지나?

A.
항상 그렇지 않다. 실제 병목을 확인한 뒤 필요한 곳에만 적용해야 한다.

Q. Client Component가 많으면 왜 성능에 영향을 주나?

A.
브라우저로 보내는 JavaScript와 Hydration 비용이 증가하기 때문이다.

---

# 22. Security Architecture Rules

## 22.1 프론트엔드 보안 구조

### [개념]

Frontend Security Architecture는 브라우저 환경에서 발생할 수 있는 Token 노출, XSS, CSRF, 권한 우회, 민감정보 노출, 환경변수 노출 위험을 줄이는 구조이다.

---

### [핵심]

필수 포함:

- Token Storage
- XSS
- CSRF
- Environment Variable Exposure
- Secret Management
- Auth Guard
- Authorization Check
- Input Validation
- Output Escaping
- Safe Redirect
- Dependency Security
- Secure Cookie
- CSP
- Error Message Sanitization
- Cache Data Leak

---

### [실무]

보안 기준:

- Secret은 Frontend Bundle에 포함하지 않음
- `NEXT_PUBLIC_` 환경변수는 공개 가능 값만 사용
- Token 저장 위치는 XSS / CSRF 위험을 비교해 결정
- HttpOnly Cookie 사용 시 서버와 연계
- Client 권한 검사는 UX용이며 서버 검사가 필수
- 사용자 입력은 서버에서 다시 검증
- HTML 직접 삽입은 XSS 위험 검토
- 외부 Redirect URL 검증
- Error 메시지에 Stack Trace / Token / 내부 정보 노출 금지
- 사용자별 데이터 Cache 주의
- Dependency 취약점 점검
- 파일 업로드는 확장자 / MIME / 크기 검증 필요

---

### [FAQ]

Q. 프론트엔드에 API Secret을 넣어도 되나?

A.
안 된다. 프론트엔드 번들에 포함된 값은 사용자에게 노출될 수 있다.

Q. Local Storage에 Token을 저장해도 되나?

A.
가능은 하지만 XSS 위험이 있으므로 보안 요구사항에 따라 HttpOnly Cookie 등 대안을 검토해야 한다.

Q. Client 권한 검사는 보안인가?

A.
아니다. Client 권한 검사는 UI 제어용이고 실제 보안은 서버에서 검증해야 한다.

---

# 23. Environment and Config Rules

## 23.1 환경 설정 구조

### [개념]

Environment and Config Architecture는 개발, 테스트, 운영 환경별 설정값과 API URL, Feature Flag, 공개 환경변수를 관리하는 구조이다.

---

### [핵심]

필수 포함:

- Environment Variable
- `.env`
- `.env.local`
- Development Config
- Production Config
- Test Config
- API Base URL
- Feature Flag
- Public Config
- Secret Config
- Runtime Config
- Build-time Config

구조 예시:

```text
shared
└ config
   ├ env.ts
   ├ routes.ts
   └ featureFlags.ts
```

---

### [실무]

Config 관리 기준:

- 환경변수 접근을 `env.ts` 같은 파일로 중앙화
- 필수 환경변수 누락 시 명확한 에러 발생
- 공개 설정과 Secret 설정 구분
- Frontend에 Secret 주입 금지
- Feature Flag는 명확한 이름 사용
- API Base URL은 환경별로 분리
- 테스트 환경에서는 Mock URL 또는 Test Config 사용
- `.env.local`은 Git에 올리지 않음
- 배포 플랫폼의 환경변수 설정 확인

예시:

```ts
export const env = {
  apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL,
};

if (!env.apiBaseUrl) {
  throw new Error("NEXT_PUBLIC_API_BASE_URL is required");
}
```

---

### [FAQ]

Q. 환경변수 접근을 왜 중앙화해야 하나?

A.
누락 검증, 타입 처리, 공개 변수와 Secret 구분을 한 곳에서 관리할 수 있기 때문이다.

Q. `NEXT_PUBLIC_` 환경변수는 안전한가?

A.
브라우저에 노출되는 값이므로 Secret에는 안전하지 않다. 공개 가능한 값에만 사용해야 한다.

Q. API Base URL은 어디에 둬야 하나?

A.
환경변수로 관리하고, 공통 Config 파일에서 읽어 API Client가 사용하도록 구성한다.

---

# 24. Build and Deployment Architecture Rules

## 24.1 빌드 / 배포 구조

### [개념]

Build and Deployment Architecture는 프론트엔드 애플리케이션이 개발 환경에서 운영 환경으로 안정적으로 배포되도록 빌드 설정, 환경변수, 정적 자산, 에러 확인 구조를 정의한다.

---

### [핵심]

필수 포함:

- Build Script
- Environment Mode
- Static Assets
- Output Directory
- Source Map
- Bundle Analysis
- CI Check
- Lint
- Type Check
- Test
- Preview Deployment
- Production Deployment
- Rollback
- Runtime Error Monitoring

---

### [실무]

배포 전 확인:

- Type Check 통과
- Lint 통과
- Unit / Component Test 통과
- E2E 핵심 Flow 통과
- 환경변수 설정 확인
- API Base URL 운영값 확인
- Source Map 공개 정책 확인
- Bundle Size 확인
- 정적 자산 경로 확인
- 인증 Redirect URL 확인
- CORS 설정 확인
- Error Monitoring 연결 확인
- 배포 후 Smoke Test 수행

---

### [FAQ]

Q. 프론트엔드 배포 전 무엇을 확인해야 하나?

A.
Type Check, Lint, Test, 환경변수, API URL, 인증 Redirect, Bundle Size, 정적 자산 경로를 확인해야 한다.

Q. 개발 환경에서는 되는데 운영에서 안 되는 이유는?

A.
환경변수 누락, API URL 차이, CORS, 인증 Redirect URL, 빌드 시점 설정 차이일 가능성이 높다.

---

# 25. Scalability Rules

## 25.1 확장 가능한 구조

### [개념]

Scalability는 기능, 팀, 코드량이 증가해도 구조가 무너지지 않고 변경 영향 범위를 통제할 수 있는 능력이다.

---

### [핵심]

확장 기준:

- Feature Boundary
- Public API
- Shared Layer Control
- Import Rule
- Test Coverage
- Design System
- API Contract
- State Ownership
- Documentation
- Incremental Refactoring
- Code Ownership
- Dependency Management

---

### [실무]

확장 전략:

- 기능이 커지면 Feature Module로 분리
- 공통 UI는 반복 사용 확인 후 Shared UI로 승격
- 공통 로직은 의미 있는 이름의 Shared Lib로 이동
- Feature 내부 구현은 외부에 숨김
- 의존성 방향을 자동화 도구로 검증
- API 계약 변경 영향 범위 관리
- 도메인별 타입과 View Model 관리
- 테스트 가능한 구조 유지
- 문서화된 폴더 규칙 유지
- 오래된 구조는 점진적으로 리팩토링

주의:

- Shared Layer 비대화 방지
- Feature 간 강한 결합 방지
- 팀마다 다른 구조를 임의로 만들지 않기
- 과도한 추상화로 개발 속도 저하시키지 않기

---

### [FAQ]

Q. 프론트엔드 구조가 확장 가능하다는 것은 무슨 뜻인가?

A.
기능과 코드가 늘어나도 어디에 코드를 추가해야 하는지 명확하고 변경 영향 범위가 통제되는 상태를 의미한다.

Q. Shared 폴더가 너무 커지면 어떻게 해야 하나?

A.
역할별로 `ui`, `api`, `lib`, `hooks`, `types`를 분리하고, 도메인성이 강한 코드는 Entity나 Feature로 이동한다.

---

# 26. Refactoring Rules

## 26.1 구조 리팩토링 기준

### [개념]

Frontend Architecture Refactoring은 동작을 유지하면서 구조를 개선해 변경 용이성, 테스트 가능성, 가독성을 높이는 작업이다.

---

### [핵심]

리팩토링 신호:

- Page가 너무 큼
- Component가 API / 상태 / UI를 모두 담당
- 같은 API 호출 코드 반복
- 상태가 여러 곳에 중복 저장
- Feature 간 순환 참조 발생
- Shared 폴더가 잡동사니화
- `utils`에 불명확한 함수 증가
- Props Drilling 과다
- Context Provider 비대화
- 테스트 작성 어려움
- 같은 Loading / Error UI 반복
- 타입 중복 발생

---

### [실무]

리팩토링 순서:

1. 중복 코드 식별
2. 책임 단위 분리
3. Feature 경계 설정
4. 공통 UI / 공통 Lib 분리
5. API Layer 정리
6. 상태 위치 재검토
7. 타입 정리
8. 테스트 추가
9. Import Boundary 정리
10. 문서 업데이트

주의:

- 대규모 일괄 리팩토링보다 작은 단위로 진행
- 동작 변경과 구조 변경을 분리
- 테스트 없이 핵심 구조 변경 금지
- 공통화는 반복이 확인된 후 진행
- 추상화 이름은 역할을 명확히 표현

---

### [FAQ]

Q. 언제 프론트엔드 구조를 리팩토링해야 하나?

A.
파일이 커지고, 중복이 늘고, 변경 영향 범위가 예측되지 않고, 테스트가 어려워질 때 리팩토링을 고려한다.

Q. 공통화는 언제 해야 하나?

A.
실제로 두세 곳 이상 반복되고 책임이 명확할 때 공통화하는 것이 좋다.

Q. 리팩토링에서 가장 조심할 점은?

A.
동작 변경과 구조 변경을 섞지 않는 것이다. 가능하면 테스트를 먼저 확보한다.

---

# 27. Troubleshooting Rules

## 27.1 자주 발생하는 구조 문제

### [개념]

Troubleshooting 문서는 Agent가 구조 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Circular Dependency
- Deep Import
- Shared Folder Bloat
- Feature Boundary Collapse
- Page Component Bloat
- API Logic Duplication
- State Duplication
- Context Overuse
- Global State Overuse
- Props Drilling
- Type Duplication
- Environment Variable Undefined
- Auth Redirect Loop
- Cache Stale Data
- Build Environment Mismatch

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- 순환 참조 발생

원인:

- Feature가 서로 직접 import함
- Shared 또는 Entity로 분리해야 할 로직이 Feature 내부에 있음

해결:

- 공통 타입 / 로직을 Shared 또는 Entity로 이동
- Feature 간 직접 의존을 제거
- Page 또는 Widget에서 Feature를 조합
```

예시:

```md
문제:

- Page Component가 너무 커짐

원인:

- 데이터 조회, 상태 관리, Form 로직, UI 렌더링이 한 파일에 섞임

해결:

- API 함수 분리
- Custom Hook 분리
- Presentational Component 분리
- Feature Module로 이동
```

---

### [FAQ]

Q. 순환 참조는 왜 위험한가?

A.
모듈 초기화 순서 문제, 테스트 어려움, 구조 경계 붕괴를 일으킬 수 있기 때문이다.

Q. Page Component가 커지면 어떻게 해야 하나?

A.
데이터 조회, 상태 관리, UI 렌더링을 Feature, Hook, Presentational Component로 분리한다.

Q. Shared 폴더가 잡동사니가 되면 어떻게 정리하나?

A.
`ui`, `api`, `lib`, `hooks`, `types`, `config`처럼 역할별로 나누고 도메인 코드는 Feature나 Entity로 이동한다.

---

# 28. Code Example Rules

## 28.1 코드 예제 작성 기준

### [개념]

Frontend Architecture 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- 폴더 구조 예시는 짧게 작성
- 핵심 책임 중심
- 불필요한 import 최소화
- 긴 전체 프로젝트 코드 금지
- API Key 하드코딩 금지
- `any` 남용 금지
- Layer / Feature 위치 명시
- Error / Loading 상태 포함 권장
- 테스트 가능성 고려

---

### [실무]

권장 예제 유형:

- Feature Module 구조
- Shared API Client
- Feature API Function
- Container / Presentational 분리
- State 분류 예시
- Auth Flow 예시
- Error Type 예시
- Environment Config 예시
- Import Boundary 예시
- Testing Structure 예시

금지 예제:

- 모든 코드를 Page에 몰아넣는 예제
- UI Component에서 API 직접 호출하는 예제
- Secret을 Client에 노출하는 예제
- Feature 내부 구현을 외부에서 Deep Import하는 예제
- `utils`에 모든 함수를 넣는 예제
- 테스트 불가능한 거대한 컴포넌트 예제
- Error를 무시하는 API 예제

---

### [FAQ]

Q. 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. 폴더 구조 예시는 꼭 필요하나?

A.
Frontend Architecture 문서에서는 구조 판단이 핵심이므로 짧은 폴더 구조 예시를 포함하는 것이 좋다.

---

# 29. Comparison Rules

## 29.1 필수 비교 대상

### [개념]

Frontend Architecture 문서는 Agent의 구조 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Feature-based Architecture vs Layer-based Architecture
- Simple Structure vs Modular Structure
- Page Component vs Feature Component
- UI Component vs Feature Component
- Container Component vs Presentational Component
- Server State vs Client State
- Local State vs Global State
- URL State vs Client State
- DTO vs View Model
- Shared UI vs Feature UI
- Shared Lib vs Feature Lib
- Context vs External Store
- API Client vs Feature API Function
- Public API Import vs Deep Import
- Unit Test vs Integration Test vs E2E Test
- Client Auth State vs Server Auth Check
- Static Config vs Runtime Config

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 책임 / 위치 / 장점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Feature-based와 Layer-based 중 무엇이 더 좋은가?

A.
프로젝트 규모와 팀 구조에 따라 다르다. 기능 중심 변경이 많으면 Feature-based가 유리하고, 작은 프로젝트는 단순 Layer 구조가 충분할 수 있다.

Q. Shared UI와 Feature UI는 어떻게 구분하나?

A.
여러 기능에서 재사용되고 비즈니스 로직이 없으면 Shared UI, 특정 기능에 종속되면 Feature UI로 둔다.

---

# 30. Checklist Rules

## 30.1 문서 품질 체크리스트

### [개념]

Frontend Architecture RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Architecture 목적이 명확한가?
- [ ] Project Structure 기준을 포함했는가?
- [ ] Feature-based Architecture 기준을 포함했는가?
- [ ] Layered Architecture 기준을 포함했는가?
- [ ] Component Architecture 기준을 포함했는가?
- [ ] Data Flow 기준을 포함했는가?
- [ ] State Architecture 기준을 포함했는가?
- [ ] API Layer 기준을 포함했는가?
- [ ] Data Fetching Architecture 기준을 포함했는가?
- [ ] Routing / Layout 기준을 포함했는가?
- [ ] Authentication Frontend Flow 기준을 포함했는가?
- [ ] UI Layer / Design System 경계를 포함했는가?
- [ ] TypeScript Architecture 기준을 포함했는가?
- [ ] Import Boundary 기준을 포함했는가?
- [ ] Error / Loading / Empty State 기준을 포함했는가?
- [ ] Testing Architecture 기준을 포함했는가?
- [ ] Performance Architecture 기준을 포함했는가?
- [ ] Security Architecture 기준을 포함했는가?
- [ ] Environment / Config 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Next.js App Router / Advanced React Pattern 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- App Router / React Pattern / Design System 문서와 역할이 겹치지 않도록 조정

---

### [FAQ]

Q. Frontend Architecture 문서 품질에서 가장 중요한 것은?

A.
폴더 구조 자체보다 Feature 경계, Layer 책임, 상태 분리, API Layer, Import Boundary, 테스트 가능성이 명확해야 한다.

---

# 31. Retrieval Optimization Rules

## 31.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Architecture
- Frontend Project Structure
- React Architecture
- Next.js Architecture
- Feature-based Architecture
- Layered Architecture
- Modular Architecture
- Feature Module
- Layer Boundary
- Import Boundary
- Public API
- Deep Import
- Circular Dependency
- Shared Layer
- Feature Layer
- Entity Layer
- Component Architecture
- UI Component
- Feature Component
- Container Component
- Presentational Component
- Data Flow
- State Architecture
- Server State
- Client State
- URL State
- Form State
- Global State
- API Layer
- API Client
- Data Fetching Architecture
- Authentication Frontend Flow
- Protected Route
- Design System Layer
- Shared UI
- TypeScript Architecture
- DTO
- View Model
- Error Handling Architecture
- Loading State
- Empty State
- Testing Architecture
- Performance Architecture
- Security Architecture
- Environment Config
- Frontend Refactoring

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- 프론트엔드 폴더 구조 어떻게 잡아?
- Feature-based Architecture는 언제 써?
- Layered Architecture는 어떻게 나눠?
- React 프로젝트 구조 추천해줘
- Next.js App Router에서 app 밖에 features 둬도 돼?
- API 호출 코드는 어디에 둬?
- 상태 관리는 어디에 둬야 해?
- Server State와 Client State 차이는?
- Shared 폴더에는 무엇을 넣어?
- Feature 폴더에는 무엇을 넣어?
- UI Component와 Feature Component 차이는?
- Page Component가 너무 커졌어
- 순환 참조 어떻게 해결해?
- Deep Import는 왜 피해야 해?
- DTO와 View Model 차이는?
- 인증 흐름은 프론트에서 어떻게 설계해?
- 에러 처리는 어떻게 공통화해?
- Loading과 Empty State는 어떻게 나눠?
- 프론트엔드 테스트 구조는 어떻게 잡아?
- 프론트엔드 성능 구조는 어떻게 봐?
- 프론트엔드 보안 체크리스트 알려줘

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 32. Version Rules

## 32.1 기준 버전

### [개념]

Frontend Architecture 문서는 Modern Frontend 기준으로 작성하며 React / Next.js / TypeScript 기반 구조와 연계한다.

---

### [핵심]

기준:

- Modern Frontend
- React 19+
- TypeScript
- Next.js App Router 연계 가능
- Function Component
- Hooks
- Feature-based Architecture
- Modular Architecture
- Server State / Client State 분리
- API Layer 분리
- Design System Layer
- Testing-first Structure
- Security-aware Frontend
- Performance-aware Frontend

Legacy 제외:

- jQuery 중심 구조
- Class Component 중심 설계
- 모든 파일을 `components`에 몰아넣는 구조
- 모든 상태를 Redux에 넣는 구조
- API 호출을 모든 컴포넌트에 직접 작성하는 구조
- Secret을 Frontend Bundle에 포함하는 구조
- 테스트 불가능한 Page 중심 거대 컴포넌트 구조

---

### [실무]

문서 작성 시 주의:

- Next.js App Router의 `app` 구조와 충돌하지 않게 작성
- Advanced React Pattern 문서와 중복되는 상세 Hook 설명은 최소화
- Design System 문서와 중복되는 UI 토큰 심화 설명은 최소화
- Monorepo 문서와 중복되는 패키지 전략 심화 설명은 최소화
- 구조 규칙은 프로젝트 규모별로 다르게 적용 가능함을 명시
- 절대적인 폴더 구조보다 책임과 의존성 방향을 우선

---

### [FAQ]

Q. Frontend Architecture 문서는 React 19 기준이어야 하나?

A.
Modern React 기준으로 작성하고, React 19 이후의 패턴과 Next.js App Router 연계를 고려하는 것이 좋다.

Q. 모든 프로젝트에 Feature-based 구조를 강제해야 하나?

A.
아니다. 작은 프로젝트는 단순 구조가 더 적합할 수 있다.

---

# 33. Common Mistakes

## 33.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 코드 리뷰와 구조 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- 모든 파일을 `components`에 넣음
- Page Component가 모든 로직을 담당
- UI Component에서 API 직접 호출
- Feature 내부 구현을 외부에서 Deep Import
- Feature 간 직접 의존 증가
- Shared 폴더가 잡동사니화
- `utils`에 모든 유틸 함수 저장
- Server State를 Global Client State에 중복 저장
- Derived State 중복 저장
- API 응답 DTO를 화면 전역 타입으로 남용
- 환경변수 접근이 여러 파일에 흩어짐
- 인증 로직이 Feature마다 중복됨
- 401 / 403 처리를 구분하지 않음
- Error / Loading / Empty State 누락
- 공통 UI에 비즈니스 로직 포함
- `any` 타입 남용
- 순환 참조 방치
- Barrel Export 남용
- 테스트하기 어려운 구조 방치
- 성능 측정 없이 memoization 남용
- Client에 Secret 노출

---

### [실무]

리뷰 기준:

- 폴더 구조와 책임 일치 여부 확인
- Feature / Shared / Entity 경계 확인
- Import 방향 확인
- 순환 참조 확인
- API Layer 중복 확인
- 상태 위치 확인
- Error / Loading / Empty State 확인
- 인증 / 권한 처리 위치 확인
- TypeScript 타입 분리 확인
- 테스트 가능성 확인
- 성능 병목 구조 확인
- 보안 위험 확인

---

### [FAQ]

Q. Frontend Architecture에서 가장 흔한 실수는?

A.
Page나 Component에 API, 상태, 비즈니스 로직, UI를 모두 몰아넣는 것이다.

Q. Shared 폴더가 커지면 왜 문제인가?

A.
책임이 불명확해지고 모든 코드가 서로 의존하기 쉬워져 구조 경계가 무너질 수 있다.

Q. Feature 간 직접 import가 많으면 왜 위험한가?

A.
기능 간 결합도가 높아지고 변경 영향 범위가 커지며 순환 참조가 발생할 수 있다.

---

# 34. Final Goal

## 34.1 최종 목표

### [개념]

Frontend Architecture RAG 문서는 Agent가 프론트엔드 프로젝트 구조를 설계, 생성, 검토, 리팩토링할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Frontend Project Structure 설계
- Feature-based Architecture 적용
- Layered Architecture 적용
- Feature Boundary 판단
- Shared Layer 설계
- Component Architecture 설계
- Data Flow 설계
- State Architecture 판단
- Server State / Client State 분리
- API Layer 설계
- Data Fetching 구조 설계
- Routing / Layout 구조 설계
- Authentication Frontend Flow 설계
- UI Layer / Design System 경계 판단
- TypeScript 타입 구조 설계
- Import Boundary 검토
- Error / Loading / Empty State 구조화
- Testing Architecture 제안
- Performance Architecture 리뷰
- Security Architecture 리뷰
- Environment Config 구조 설계
- Frontend Refactoring 제안
- 구조 문제 Troubleshooting
- Frontend Architecture 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 폴더 구조 예시는 짧고 명확하게 작성
- Feature / Layer / Import Boundary 명확화
- 상태 / API / 인증 / 테스트 / 보안 기준 포함
- Next.js App Router / Advanced React Pattern 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Architecture Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 폴더 구조, Feature 경계, Layer 책임, 상태 관리, API Layer, 인증, 테스트, 성능, 보안을 설계하고 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Architecture 문서는 어떤 기준으로 작성해야 해?

A.
Project Structure, Feature-based Architecture, Layer Boundary, Component Architecture, Data Flow, State Architecture, API Layer, Auth Flow, Testing, Performance, Security 중심으로 작성해야 한다.

Q. 프론트엔드 폴더 구조 어떻게 잡아?

A.
작은 프로젝트는 단순 구조로 시작하고, 기능이 많아지면 `features`, `shared`, `entities`, `app` 같은 구조로 분리한다.

Q. React 프로젝트 구조 추천해줘.

A.
기능 중심 변경이 많다면 Feature-based 구조를 권장한다. 공통 UI와 유틸은 `shared`, 기능별 UI / API / Hook은 `features`에 둔다.

Q. Next.js App Router에서 app 밖에 features 둬도 돼?

A.
가능하다. `app`은 라우팅과 페이지 조립 중심으로 두고 기능 로직은 `features`나 `shared`로 분리할 수 있다.

Q. Feature-based Architecture는 언제 써?

A.
기능이 많아지고 화면, API, 상태, 타입이 섞이기 시작할 때 사용한다.

Q. Feature는 어떤 단위로 나눠?

A.
사용자 행동이나 비즈니스 기능 단위로 나눈다. 로그인, 게시글 작성, 프로필 수정 같은 단위가 적합하다.

Q. Layered Architecture는 어떻게 나눠?

A.
App, Page, Widget, Feature, Entity, Shared, API, Config처럼 책임과 의존성 방향을 기준으로 나눈다.

Q. Layered Architecture에서 가장 중요한 규칙은?

A.
의존성 방향이다. 하위 Layer가 상위 Layer를 import하지 않도록 해야 한다.

Q. Shared 폴더에는 무엇을 넣어?

A.
공통 UI, 공통 Hook, API Client, 유틸, 타입, 설정처럼 여러 Feature에서 재사용되는 안정적인 코드를 넣는다.

Q. Feature 폴더에는 무엇을 넣어?

A.
해당 기능에 필요한 API, Component, Hook, Model, Type, Test를 함께 배치한다.

Q. UI Component와 Feature Component 차이는?

A.
UI Component는 비즈니스 로직 없는 재사용 UI이고, Feature Component는 특정 기능 흐름에 종속된 컴포넌트이다.

Q. Page Component는 어떤 역할을 해야 해?

A.
Route 단위 화면을 조립하고 Feature, Widget, Layout을 연결하는 역할을 한다.

Q. Page Component가 너무 커졌어. 어떻게 나눠?

A.
API 함수, Custom Hook, Feature Component, Presentational Component로 책임을 분리한다.

Q. API 호출 코드는 어디에 둬?

A.
공통 HTTP Client는 `shared/api`, 기능별 API 함수는 해당 Feature의 `api` 폴더에 둔다.

Q. API 응답 타입과 화면 타입은 같아야 해?

A.
항상 같을 필요는 없다. 서버 DTO와 화면 View Model이 다르면 변환 함수를 둔다.

Q. DTO와 View Model 차이는?

A.
DTO는 서버 API 응답 / 요청 구조이고, View Model은 화면 표시와 상호작용에 맞춘 프론트엔드 데이터 구조이다.

Q. 상태 관리는 어디에 둬야 해?

A.
상태를 사용하는 위치와 가장 가까운 곳에 둔다. 서버 데이터, URL 상태, Form 상태, UI 상태를 구분해야 한다.

Q. Server State와 Client State 차이는?

A.
Server State는 서버에서 온 데이터이고, Client State는 브라우저 UI 상호작용을 표현하는 상태이다.

Q. 검색 조건은 어디에 저장하는 게 좋아?

A.
공유, 복원, 북마크가 필요한 검색 조건은 URL Search Params에 저장하는 것이 좋다.

Q. 모든 상태를 전역 Store에 넣어도 돼?

A.
권장하지 않는다. Local UI State, Server State, URL State, Form State는 각각 적합한 관리 위치가 다르다.

Q. 인증 흐름은 프론트에서 어떻게 설계해?

A.
서버 세션 또는 Token 기준으로 현재 사용자를 확인하고, Client Auth State는 UX 개선용으로 사용한다.

Q. 권한별 버튼 숨기면 보안 처리 된 거야?

A.
아니다. Client UI 숨김은 UX이고 실제 권한 검사는 서버에서 해야 한다.

Q. 401과 403은 어떻게 다르게 처리해?

A.
401은 인증 필요 또는 세션 만료이고, 403은 인증은 되었지만 권한이 없는 상태이다.

Q. Design System 컴포넌트에는 무엇을 넣어?

A.
Button, Input, Modal, Card처럼 비즈니스 로직이 없는 재사용 UI와 접근성 기본 동작을 넣는다.

Q. Feature 전용 컴포넌트도 Shared UI로 빼야 해?

A.
반복 사용이 확인되기 전까지는 Feature 내부에 두는 것이 좋다.

Q. Import Boundary는 왜 필요해?

A.
모듈 간 의존성 방향을 제한해 순환 참조, 구조 붕괴, 내부 구현 노출을 방지하기 위해 필요하다.

Q. Deep Import는 왜 피해야 해?

A.
모듈 내부 구현에 직접 의존하게 되어 리팩토링이 어려워지고 Feature 경계가 무너질 수 있기 때문이다.

Q. 순환 참조 어떻게 해결해?

A.
공통 타입이나 로직을 Shared 또는 Entity로 이동하고, Feature 간 직접 의존을 제거한다.

Q. Barrel Export는 항상 써야 해?

A.
아니다. Public API를 제한할 때 유용하지만 무분별하게 사용하면 의존성 추적이 어려워질 수 있다.

Q. 에러 처리는 어떻게 공통화해?

A.
API Error를 공통 Error Type으로 변환하고, 사용자 메시지와 개발자 로그를 분리한다.

Q. Loading과 Empty State는 어떻게 나눠?

A.
Loading은 데이터를 기다리는 상태이고, Empty는 요청은 성공했지만 표시할 데이터가 없는 상태이다.

Q. Mutation Pending은 어떻게 처리해?

A.
버튼 disabled, pending 표시, 중복 제출 방지, 성공 후 cache invalidation 또는 revalidation을 처리한다.

Q. 프론트엔드 테스트 구조는 어떻게 잡아?

A.
Utility는 Unit Test, UI는 Component Test, Feature Flow는 Integration Test, 핵심 사용자 흐름은 E2E Test로 검증한다.

Q. 모든 컴포넌트를 테스트해야 해?

A.
아니다. 핵심 사용자 Flow, Form, 인증, API Error, 공통 UI를 우선 테스트한다.

Q. 프론트엔드 성능 구조는 어떻게 봐?

A.
Bundle Size, Code Splitting, 이미지 최적화, 데이터 패칭, Client Component 범위, Re-render 비용을 확인한다.

Q. Memoization부터 적용하면 돼?

A.
아니다. 성능 병목을 측정하고 State 위치, 컴포넌트 분리, Context 범위를 먼저 점검한다.

Q. 프론트엔드 보안 체크리스트는?

A.
Secret 노출, Token 저장 위치, XSS, CSRF, 환경변수 노출, 권한 서버 검증, Error 메시지 노출, Cache 데이터 누수를 확인한다.

Q. 프론트엔드에 API Secret 넣어도 돼?

A.
안 된다. 프론트엔드 번들에 포함된 값은 사용자에게 노출될 수 있다.

Q. 환경변수 접근은 어떻게 구조화해?

A.
`env.ts` 같은 Config 파일로 중앙화하고 필수 환경변수 누락을 명확히 검증한다.

Q. 개발에서는 되는데 운영에서 안 되는 이유는?

A.
환경변수 누락, API URL 차이, CORS, 인증 Redirect URL, 빌드 시점 설정 차이일 가능성이 높다.

Q. Shared 폴더가 너무 커지면 어떻게 해?

A.
`ui`, `api`, `lib`, `hooks`, `types`, `config`로 역할별 분리하고 도메인성 코드는 Feature나 Entity로 이동한다.

Q. 공통화는 언제 해야 해?

A.
실제로 두세 곳 이상 반복되고 책임이 명확할 때 공통화하는 것이 좋다.

Q. 프론트엔드 구조 리팩토링은 언제 해?

A.
파일이 커지고 중복이 늘며 변경 영향 범위가 예측되지 않고 테스트가 어려워질 때 리팩토링한다.

Q. Frontend Architecture 코드 리뷰에서 가장 중요한 것은?

A.
Feature 경계, Layer 책임, Import 방향, 상태 위치, API Layer, Error State, 인증 보안, 테스트 가능성을 확인하는 것이다.

Q. Frontend Architecture RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 폴더 구조, Feature 경계, Layer 책임, 상태 관리, API Layer, 인증, 테스트, 성능, 보안을 설계하고 리뷰하게 만드는 것이다.

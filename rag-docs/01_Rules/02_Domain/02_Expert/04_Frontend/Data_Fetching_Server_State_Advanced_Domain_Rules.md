# Data Fetching / Server State Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Data Fetching / Server State Advanced Domain 목적

### [개념]

Data Fetching / Server State Advanced Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent용 RAG 문서 제작 규칙이다.

Data Fetching은 프론트엔드가 서버 API, Database API, Route Handler, Server Action, 외부 API에서 데이터를 가져오고 화면에 반영하는 과정이다.

Server State는 클라이언트가 소유하지 않지만 화면에 표시하고 조작해야 하는 서버 데이터 상태이다. 예를 들어 게시글 목록, 사용자 프로필, 상품 상세, 검색 결과, 알림 목록, 결제 상태, 권한 정보, 좋아요 상태, 댓글 목록 등이 Server State이다.

목적:

- 서버 상태와 클라이언트 상태 구분 지원
- Data Fetching 전략 설계 지원
- React Query / TanStack Query 계열 Server State 패턴 지원
- SWR 계열 stale-while-revalidate 패턴 지원
- Next.js App Router Data Fetching 전략 지원
- Server Component / Client Component 데이터 경계 판단 지원
- Cache / Revalidation / Invalidation 설계 지원
- Optimistic Update / Mutation 전략 지원
- Pagination / Infinite Query 설계 지원
- Search / Filter / Sort URL State 연계 지원
- Request Waterfall / 중복 요청 문제 진단 지원
- Error / Loading / Empty 상태 설계 지원
- Offline / Retry / Background Refetch 판단 지원
- Server State 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Server State vs Client State
2. Fetching Location Decision
3. Server Component Fetching
4. Client-side Fetching
5. Query Key Design
6. Cache Strategy
7. Stale Time / Cache Time
8. Invalidation
9. Revalidation
10. Mutation
11. Optimistic Update
12. Pagination
13. Infinite Query
14. Search / Filter / Sort
15. Request Deduplication
16. Request Waterfall Prevention
17. Error / Loading / Empty State
18. Authentication-aware Fetching
19. Next.js App Router Integration
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / TypeScript / Next.js App Router 기준 예제 우선
- Server State를 `useState`로 직접 관리하는 패턴 지양
- 서버 데이터는 Query Cache / Framework Cache / URL State / Server Component Fetching 기준으로 분리
- Client Component에서 필요한 데이터와 Server Component에서 가져올 데이터를 명확히 구분
- 사용자별 데이터와 공개 데이터를 캐시 정책에서 분리
- Query Key는 데이터 식별자와 필터 조건을 명확히 포함
- Mutation 이후 Invalidation / Cache Update / Optimistic Update 기준 포함
- Loading / Error / Empty / Success 상태를 UI 설계에 포함
- 중복 요청과 Request Waterfall을 성능 병목으로 다룸
- 검색 / 필터 / 페이지네이션은 URL State와 연계 가능하게 작성
- 인증 만료 / 권한 없음 / 서버 오류를 구분
- Agent가 Data Fetching 구조와 Server State 코드를 리뷰할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Data Fetching / Server State Advanced 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드에서 서버 데이터를 가져오고 캐싱, 갱신, mutation, pagination, 검색, 에러 상태를 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. Server State는 Client State와 무엇이 다른가?

A.
Server State는 서버가 소유하고 여러 사용자가 공유할 수 있는 비동기 데이터이고, Client State는 현재 브라우저 UI가 소유하는 로컬 상태이다.

Q. Server State를 그냥 `useState`로 관리하면 안 되나?

A.
간단한 경우는 가능하지만 cache, refetch, stale data, retry, pagination, invalidation이 필요해지면 전용 Server State 관리 전략이 필요하다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Data Fetching / Server State Advanced Domain은 프론트엔드에서 서버 데이터를 가져오고, 캐싱하고, 변경하고, 동기화하고, 오류를 처리하는 고급 전략을 포함한다.

---

### [핵심]

포함 범위:

- Data Fetching
- Server State
- Client State
- Query
- Mutation
- Query Key
- Query Cache
- Stale Data
- Fresh Data
- Stale Time
- Cache Time
- Garbage Collection
- Invalidation
- Revalidation
- Refetch
- Background Refetch
- Optimistic Update
- Pessimistic Update
- Request Deduplication
- Request Waterfall
- Parallel Fetching
- Dependent Query
- Conditional Query
- Pagination
- Infinite Query
- Cursor Pagination
- Offset Pagination
- Search Query
- Filter
- Sort
- URL State
- Abort Request
- Race Condition
- Retry
- Error Boundary
- Loading State
- Empty State
- Suspense
- Streaming
- TanStack Query
- React Query
- SWR
- Next.js Fetch Cache
- Server Component Fetching
- Client Component Fetching
- Server Action Mutation
- Route Handler
- API Client Layer
- Authentication-aware Fetching
- 401 / 403 Handling
- Offline Support
- Hydration / Dehydration
- Prefetch
- Cache Persistence
- Real-time Sync
- WebSocket / SSE Update
- Contract / DTO / View Model Mapping

---

### [실무]

제외 범위:

- Backend Query Tuning 심화
- Database Index 설계 심화
- CDN Cache 운영 심화
- GraphQL Schema 설계 심화 전체
- WebSocket 서버 구현 심화
- Next.js App Router 전체 기능 설명
- React Query / SWR 전체 API 레퍼런스
- REST API 설계 전체
- 인증 프로토콜 심화
- DevOps Monitoring 심화

단, Server State 판단에 필요한 수준의 API 설계, Next.js Cache, 인증, 에러 처리, 성능, 테스트, 보안 지식은 포함 가능하다.

---

### [FAQ]

Q. React Query나 SWR 도구 사용법 전체를 포함해야 하나?

A.
아니다. 전체 API 레퍼런스보다 Server State 설계 원칙, Query Key, Cache, Mutation, Invalidation 판단 기준에 집중한다.

Q. Next.js Cache 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 Domain은 프론트엔드 데이터 흐름과 서버 상태 관리 관점에서 Next.js Cache를 연결한다.

Q. Backend API 설계도 포함하나?

A.
심화는 제외한다. 단, 프론트엔드 Server State가 안정적으로 동작하기 위해 필요한 DTO, pagination, error response, idempotency 기준은 포함한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Data Fetching / Server State Advanced RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Data Fetching / Server State 문서는 데이터 흐름과 상태 전이가 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Fetch → Cache → Render → Mutate → Invalidate → Refetch
- `[Comparison]`: Server State vs Client State, Query vs Mutation
- `[Best Practice]`: Query Key 설계, Invalidation, Error State
- `[Troubleshooting]`: 데이터가 안 바뀜, 중복 요청, stale data, race condition
- `[Checklist]`: Data Fetching 코드 리뷰

---

### [FAQ]

Q. Data Fetching 문서에 Flow가 중요한 이유는?

A.
서버 데이터는 가져오기, 캐싱, 표시, 변경, 무효화, 재조회 흐름이 연결되어야 올바르게 동작하기 때문이다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Server State Core Concept Rules

## 4.1 Server State 기본 개념

### [개념]

Server State는 클라이언트가 직접 소유하지 않고 서버에서 관리되는 데이터이다.

Server State는 비동기적이고, 여러 사용자나 여러 화면에서 공유될 수 있으며, 시간이 지나면 stale 상태가 될 수 있다.

---

### [핵심]

Server State 특징:

- Remote Source
- Async Data
- Shared Data
- Cached Data
- Stale Data
- Refetchable Data
- Mutatable Data
- Error-prone Data
- Network-dependent Data
- User-dependent Data
- Permission-dependent Data

Client State 특징:

- Local UI State
- Synchronous State
- Temporary State
- Component-owned State
- Form Draft State
- Modal Open State
- Tab State
- Hover State
- Theme State

---

### [실무]

구분 기준:

| 상태          | 소유자      | 예시                            | 관리 방식                  |
| ------------- | ----------- | ------------------------------- | -------------------------- |
| Server State  | 서버        | 게시글, 댓글, 상품, 사용자 정보 | Query Cache / Server Fetch |
| Client State  | 브라우저 UI | 모달 열림, 탭 선택, 입력 중 값  | `useState` / store         |
| URL State     | URL         | 검색어, 필터, 페이지 번호       | search params              |
| Form State    | 사용자 입력 | 제출 전 Form 값                 | form library / local state |
| Derived State | 계산 결과   | 필터링된 목록                   | memoized calculation       |

주의:

- Server State를 전역 Client Store에 복사하지 않기
- 서버 데이터와 편집 중 Form Draft를 혼동하지 않기
- URL로 표현 가능한 검색 / 필터는 URL State 검토
- 서버에서 다시 가져올 수 있는 데이터를 로컬에 과도하게 복제하지 않기
- Server State가 stale될 수 있음을 UI와 cache 정책에 반영

---

### [FAQ]

Q. Server State의 핵심 특징은?

A.
서버가 소유하고 비동기적으로 가져오며, 캐시될 수 있고, 시간이 지나면 stale 상태가 될 수 있다는 점이다.

Q. Server State를 Zustand나 Redux에 넣어도 되나?

A.
가능은 하지만 cache, refetch, invalidation을 직접 구현해야 하므로 전용 Server State 도구나 Framework Cache가 더 적합한 경우가 많다.

Q. Form 입력값은 Server State인가?

A.
제출 전 입력값은 Form State이고, 제출 후 서버에 저장된 결과는 Server State이다.

---

# 5. Fetching Location Decision Rules

## 5.1 데이터를 어디서 가져올지 결정

### [개념]

Fetching Location Decision은 데이터를 Server Component, Client Component, Route Handler, Server Action, API Client 중 어디에서 가져오거나 변경할지 결정하는 규칙이다.

---

### [핵심]

Fetching 위치:

- Server Component Fetching
- Client Component Fetching
- Route Handler Fetching
- Server Action Mutation
- API Client Layer
- Edge / Middleware Fetching
- Prefetch
- Background Refetch

판단 기준:

```text
SEO가 중요한 초기 데이터인가?
→ Server Component Fetching 검토

사용자 상호작용 후 갱신되는 데이터인가?
→ Client-side Query 검토

Form 제출 / mutation인가?
→ Server Action 또는 API Mutation 검토

브라우저 전용 정보가 필요한가?
→ Client Component Fetching 검토

Secret이 필요한 외부 API인가?
→ Server-side Fetching 검토
```

---

### [실무]

Server Component Fetching 적합:

- SEO 중요 콘텐츠
- 초기 렌더링에 필요한 공개 데이터
- 서버 secret이 필요한 데이터
- 사용자별 데이터지만 서버에서 안전하게 처리해야 하는 데이터
- Hydration 비용을 줄이고 싶은 데이터

Client Component Fetching 적합:

- 사용자 입력 후 검색
- 무한 스크롤
- 실시간 갱신
- 대시보드 일부 위젯
- 브라우저 상태 기반 요청
- background refetch
- optimistic update가 필요한 데이터

주의:

- 모든 데이터를 Client Component에서 fetch하면 초기 HTML과 SEO가 약해질 수 있음
- 모든 데이터를 Server Component에서만 가져오면 사용자 상호작용 후 갱신이 불편할 수 있음
- Secret이 필요한 요청은 Client에서 직접 호출 금지
- 사용자별 데이터는 public cache에 섞이지 않게 처리
- Route Handler를 불필요하게 내부 proxy로 남용하지 않기

---

### [FAQ]

Q. 데이터는 Server Component에서 가져오는 게 좋은가 Client Component에서 가져오는 게 좋은가?

A.
초기 렌더링과 SEO가 중요하면 Server Component, 사용자 상호작용 후 갱신이나 cache interaction이 중요하면 Client Component Query가 적합하다.

Q. 외부 API Secret이 필요한 요청은 어디서 해야 하나?

A.
Server Component, Route Handler, Backend처럼 서버에서 처리해야 한다. Client Component에 secret을 노출하면 안 된다.

Q. Route Handler를 항상 거쳐야 하나?

A.
아니다. Server Component에서 직접 서버 로직을 호출할 수 있으면 불필요한 내부 HTTP 호출을 피할 수 있다.

---

# 6. Query Key Design Rules

## 6.1 Query Key 설계

### [개념]

Query Key는 Server State Cache에서 데이터를 식별하는 고유한 키이다.

Query Key가 정확해야 cache hit, refetch, invalidation, pagination, filter 상태가 올바르게 동작한다.

---

### [핵심]

Query Key 구성 요소:

- Resource Name
- Resource ID
- Search Keyword
- Filter
- Sort
- Page
- Cursor
- Locale
- User Scope
- Permission Scope
- Tenant
- Feature Flag
- API Version

좋은 Query Key 예시:

```ts
const postListKey = ["posts", { keyword, category, page, sort }];
const postDetailKey = ["posts", postId];
const userProfileKey = ["users", userId, "profile"];
```

---

### [실무]

작성 기준:

- 같은 데이터는 같은 Query Key
- 조건이 다른 데이터는 다른 Query Key
- search / filter / sort / page 조건 포함
- detail과 list key 구분
- 사용자별 데이터는 user scope 포함 검토
- locale별 데이터는 locale 포함
- object key는 안정적인 구조로 작성
- 불필요하게 매번 바뀌는 값 포함 금지
- token 자체를 Query Key에 넣지 않기
- Invalidation 범위를 고려해 계층형 key 설계

Query Key 구조 예시:

```text
["posts"]
["posts", "list", { category, page }]
["posts", "detail", postId]
["posts", "comments", postId]
["me"]
["notifications", { unreadOnly }]
```

주의:

- Query Key에 함수, class instance, random 값 넣지 않기
- filter 조건 누락 시 잘못된 cache 재사용 가능
- Query Key가 너무 넓으면 불필요한 refetch 증가
- Query Key가 너무 세분화되면 cache 관리 복잡도 증가
- 개인정보나 token을 key로 사용하지 않기

---

### [FAQ]

Q. Query Key는 왜 중요한가?

A.
Server State Cache에서 데이터를 구분하고 refetch, invalidation, pagination을 정확히 수행하기 위해 중요하다.

Q. 검색어와 필터도 Query Key에 넣어야 하나?

A.
그렇다. 검색어와 필터가 다르면 다른 데이터이므로 Query Key에 포함해야 한다.

Q. Query Key에 token을 넣어도 되나?

A.
안 된다. token은 민감정보이며 key 노출과 cache 복잡도 문제를 만들 수 있다.

---

# 7. Cache Strategy Rules

## 7.1 Server State Cache 전략

### [개념]

Cache Strategy는 서버 데이터를 얼마나 오래 신선하다고 볼지, 언제 다시 가져올지, 언제 버릴지, 어떤 mutation 이후 무효화할지 결정하는 규칙이다.

---

### [핵심]

필수 포함:

- Cache
- Query Cache
- Stale Data
- Fresh Data
- Stale Time
- Cache Time
- Garbage Collection
- Invalidation
- Refetch
- Background Refetch
- Cache Update
- Cache Hydration
- Cache Persistence
- Public Cache
- Private Cache

데이터별 cache 성격:

| 데이터        | Cache 전략                     |
| ------------- | ------------------------------ |
| 공지사항      | 긴 stale time 가능             |
| 상품 상세     | 중간 stale time / revalidation |
| 검색 결과     | 조건별 cache                   |
| 알림 목록     | 짧은 stale time                |
| 사용자 프로필 | 사용자별 private cache         |
| 권한 정보     | 짧거나 명시적 refetch          |
| 실시간 채팅   | query cache + realtime sync    |
| 관리자 통계   | 짧은 stale time 또는 no cache  |

---

### [실무]

작성 기준:

- 자주 바뀌지 않는 데이터는 stale time 길게 설정 가능
- 자주 바뀌는 데이터는 짧은 stale time 또는 실시간 갱신 검토
- 사용자별 데이터와 공개 데이터 cache 분리
- Mutation 이후 관련 Query invalidation
- 같은 데이터가 여러 화면에서 공유되면 key 설계 중요
- cache가 오래된 데이터를 보여줄 수 있음을 UI에서 고려
- background refetch로 UX 개선 가능
- cache persistence는 로그인 사용자 데이터 보안 검토 필요
- 브라우저 탭 복귀 시 refetch 여부 판단
- 네트워크 재연결 시 refetch 여부 판단

주의:

- stale time을 무조건 0으로 두면 refetch가 과도해질 수 있음
- cache를 너무 오래 유지하면 데이터 신선도 문제
- 사용자별 데이터를 persistent cache에 저장할 때 보안 검토
- mutation 후 invalidation 누락은 오래된 화면의 주요 원인
- cache 정책은 제품 요구사항과 데이터 성격 기준으로 결정

---

### [FAQ]

Q. stale time은 무엇인가?

A.
캐시된 데이터를 신선하다고 간주하는 시간이다. 이 시간이 지나면 stale 상태가 되어 refetch 대상이 될 수 있다.

Q. cache time은 무엇인가?

A.
사용되지 않는 cache 데이터가 메모리에 남아있는 시간이다. 도구별로 garbage collection time이라고 부를 수 있다.

Q. cache를 많이 쓰면 좋은가?

A.
항상 그렇지는 않다. 데이터 신선도, 보안, invalidation 전략이 함께 있어야 한다.

---

# 8. Invalidation and Revalidation Rules

## 8.1 Cache Invalidation / Revalidation

### [개념]

Invalidation은 특정 cache를 stale 상태로 표시하거나 제거해 다시 가져오게 하는 작업이다.

Revalidation은 stale 상태의 데이터를 다시 검증하거나 새 데이터로 갱신하는 과정이다.

---

### [핵심]

Invalidation 대상:

- List Query
- Detail Query
- Related Query
- User Query
- Notification Query
- Search Query
- Infinite Query
- Permission Query
- Dashboard Query

Mutation 이후 Flow:

```text
Mutation 요청
→ 서버 성공
→ 관련 Query Invalidate
→ Refetch
→ UI 갱신
```

---

### [실무]

작성 기준:

- 생성 mutation 후 list query invalidation
- 수정 mutation 후 detail query와 list query 갱신
- 삭제 mutation 후 list query invalidation + detail cache 제거
- 좋아요 / 찜 같은 작은 mutation은 cache update 또는 optimistic update 검토
- 댓글 생성 후 댓글 목록과 댓글 수 갱신
- 사용자 정보 변경 후 `me` / profile 관련 query 갱신
- 권한 변경 후 permission / menu / protected data 갱신
- broad invalidation과 precise invalidation 균형
- Next.js App Router에서는 `revalidatePath` / `revalidateTag`와 client query invalidation 관계 구분

주의:

- 너무 넓은 invalidation은 불필요한 refetch 증가
- 너무 좁은 invalidation은 stale data 남음
- mutation 성공 전에 invalidation하면 실패 시 UI 불일치 가능
- optimistic update와 invalidation 순서 관리
- 같은 데이터가 여러 key에 흩어지지 않도록 key 설계 중요

---

### [FAQ]

Q. Mutation 후 데이터가 안 바뀌면 무엇을 확인해야 하나?

A.
관련 Query Key invalidation, cache update, refetch 조건, stale time, Next.js revalidation 여부를 확인해야 한다.

Q. 생성 후 어떤 query를 invalidate해야 하나?

A.
일반적으로 목록 query를 invalidate하고, 필요하면 관련 count / dashboard query도 갱신한다.

Q. 삭제 후 detail cache는 어떻게 해야 하나?

A.
삭제된 entity의 detail cache를 제거하거나 접근 시 not found 상태가 되도록 처리해야 한다.

---

# 9. Mutation Rules

## 9.1 Mutation 설계

### [개념]

Mutation은 서버 상태를 변경하는 요청이다.

예를 들어 생성, 수정, 삭제, 좋아요, 찜, 결제 요청, 댓글 작성, 프로필 수정, 파일 업로드 등이 mutation이다.

---

### [핵심]

Mutation 유형:

- Create
- Update
- Delete
- Toggle
- Upload
- Submit
- Approve
- Cancel
- Payment
- Retry
- Bulk Mutation

Mutation 상태:

- Idle
- Pending
- Success
- Error
- Settled

Mutation Flow:

```text
User Action
→ Validate Input
→ Run Mutation
→ Pending UI
→ Success or Error
→ Cache Update / Invalidate
→ User Feedback
```

---

### [실무]

작성 기준:

- mutation 함수는 API Client 또는 Server Action으로 분리
- pending 상태에서 중복 제출 방지
- 성공 시 toast / redirect / cache update 처리
- 실패 시 사용자 친화적 에러 표시
- validation error와 server error 구분
- idempotent하지 않은 요청은 retry 주의
- 결제 / 주문 / 삭제 mutation은 중복 실행 방지
- mutation response를 cache update에 활용 가능
- 관련 query invalidation 기준 명확화
- optimistic update 적용 가능성 판단

예시:

```ts
async function updatePost(input: UpdatePostInput) {
  const response = await api.patch(`/posts/${input.postId}`, input);
  return response.data;
}
```

주의:

- client에서 보낸 userId / role 신뢰 금지
- mutation 실패를 무시하지 않기
- pending 중 버튼 활성화로 중복 요청 발생 주의
- 삭제 mutation은 confirmation UX 검토
- retry가 위험한 mutation에 자동 retry 적용 금지

---

### [FAQ]

Q. Mutation은 Query와 무엇이 다른가?

A.
Query는 서버 데이터를 읽는 작업이고, Mutation은 서버 데이터를 변경하는 작업이다.

Q. Mutation 후에는 항상 invalidation해야 하나?

A.
대부분 필요하다. 다만 mutation response로 cache를 직접 업데이트할 수도 있다.

Q. 결제 요청에 자동 retry를 적용해도 되나?

A.
주의해야 한다. 중복 결제 위험이 있으므로 idempotency key와 서버 설계가 필요하다.

---

# 10. Optimistic Update Rules

## 10.1 Optimistic Update 기준

### [개념]

Optimistic Update는 서버 응답을 기다리지 않고 성공할 것으로 가정해 UI를 먼저 업데이트하는 전략이다.

사용자 체감 속도는 좋아지지만 실패 시 rollback이 필요하다.

---

### [핵심]

적합 대상:

- Like Toggle
- Favorite Toggle
- Follow Toggle
- Simple Reaction
- Checkbox Update
- Local Ordering
- Low-risk Preference
- Comment Draft Insert

부적합 대상:

- Payment
- Order Submit
- Money Transfer
- Permission Change
- Destructive Delete
- High-risk Admin Action
- Security-sensitive Mutation

Optimistic Flow:

```text
현재 cache snapshot 저장
→ UI 먼저 업데이트
→ mutation 요청
→ 성공 시 확정
→ 실패 시 rollback
→ 필요 시 refetch
```

---

### [실무]

작성 기준:

- 이전 cache snapshot 저장
- 실패 시 rollback
- 중복 클릭 처리
- 서버 응답과 optimistic state reconcile
- 낙관 업데이트 후 관련 query refetch 검토
- 좋아요 수 / 찜 상태처럼 작은 변경에 적합
- 에러 발생 시 사용자에게 복구 메시지 표시
- 권한 / 결제 / 삭제에는 신중
- offline mutation과 결합 시 conflict 처리 필요

예시:

```text
좋아요 클릭
→ 즉시 좋아요 상태 true 표시
→ 서버 요청
→ 실패하면 false로 rollback
→ 성공하면 서버 응답 기준으로 정리
```

주의:

- rollback 누락 시 UI와 서버 데이터 불일치
- 여러 mutation이 동시에 발생하면 순서 충돌 가능
- optimistic update가 실제 서버 권한 실패를 숨기지 않게 처리
- 사용자에게 성공한 것처럼 보였는데 실패하는 UX 고려
- 중요한 거래성 작업에는 부적합

---

### [FAQ]

Q. Optimistic Update는 언제 쓰면 좋나?

A.
좋아요, 찜, 팔로우처럼 실패 가능성이 낮고 되돌리기 쉬운 작은 mutation에 적합하다.

Q. Optimistic Update에서 가장 중요한 것은?

A.
실패 시 rollback할 수 있도록 이전 상태를 저장하고 서버 응답과 최종 상태를 맞추는 것이다.

Q. 결제나 주문에도 Optimistic Update를 써도 되나?

A.
권장하지 않는다. 금전이나 재고, 권한이 관련된 작업은 서버 확정 후 UI를 갱신하는 것이 안전하다.

---

# 11. Pagination Rules

## 11.1 Pagination / Infinite Query

### [개념]

Pagination은 큰 목록 데이터를 여러 페이지로 나누어 가져오는 전략이다.

Infinite Query는 사용자가 스크롤하거나 버튼을 눌러 다음 페이지를 계속 이어 붙이는 UX 패턴이다.

---

### [핵심]

Pagination 유형:

- Offset Pagination
- Cursor Pagination
- Page Number Pagination
- Infinite Scroll
- Load More
- Slice Pagination
- Keyset Pagination

검토 요소:

- Page Size
- Cursor
- Has Next Page
- Total Count
- Sort Stability
- Duplicate Item
- Missing Item
- Cache Key
- URL State
- Scroll Restoration

---

### [실무]

Offset Pagination 적합:

- 관리자 목록
- 검색 결과
- 페이지 번호 UI
- 총 개수 필요
- 정렬이 안정적이고 데이터 변경이 적은 목록

Cursor Pagination 적합:

- 피드
- 댓글
- 알림
- 실시간성이 있는 목록
- 무한 스크롤
- 데이터 변경이 잦은 목록

Infinite Query 기준:

- `getNextPageParam` 또는 cursor 기준 명확화
- 중복 item 제거 전략
- 이전 페이지 cache 유지
- query key에 filter / sort 포함
- filter 변경 시 페이지 reset
- scroll restoration 고려
- error 발생 시 특정 page retry UX 제공
- 접근성을 위해 load more 버튼 고려

주의:

- offset pagination은 데이터 삽입 / 삭제 시 중복이나 누락 가능
- cursor pagination은 cursor 설계가 API와 맞아야 함
- infinite scroll은 footer 접근성과 URL 복원성 문제
- filter 변경 시 기존 infinite pages가 섞이지 않게 주의
- page size가 너무 크면 응답과 렌더링이 느려짐

---

### [FAQ]

Q. Offset Pagination과 Cursor Pagination 차이는?

A.
Offset은 페이지 번호와 offset 기준이고, Cursor는 마지막 item 기준으로 다음 데이터를 가져온다. 데이터 변경이 잦으면 Cursor가 더 안정적이다.

Q. Infinite Query에서 가장 중요한 것은?

A.
cursor, hasNextPage, query key, 중복 제거, filter 변경 시 reset 처리가 중요하다.

Q. 무한 스크롤은 항상 좋은가?

A.
아니다. 접근성, SEO, footer 접근, URL 복원성이 중요하면 pagination이나 load more가 더 적합할 수 있다.

---

# 12. Search / Filter / Sort Rules

## 12.1 검색 / 필터 / 정렬 Server State

### [개념]

Search / Filter / Sort는 사용자가 조건을 바꿀 때 서버 데이터를 다시 가져오고 cache key와 URL state를 함께 관리해야 하는 대표적인 Server State 패턴이다.

---

### [핵심]

필수 포함:

- Search Keyword
- Filter
- Sort
- URL Search Params
- Debounce
- Abort Request
- Query Key
- Reset Page
- Empty Result
- Loading State
- Race Condition
- Search History
- Shareable URL

---

### [실무]

작성 기준:

- 검색어 / 필터 / 정렬 조건을 Query Key에 포함
- 공유 가능한 검색 상태는 URL search params 사용
- 검색 입력에는 debounce 검토
- 입력 변경 시 이전 요청 abort 검토
- 필터 변경 시 page reset
- 결과 없음 상태 제공
- loading 중 이전 결과 유지 여부 결정
- 검색어 normalization 기준 작성
- sort key는 allowlist로 제한
- 서버 API와 query param 계약 명확화

예시 Query Key:

```ts
const key = ["festivals", "search", { keyword, region, theme, sort, page }];
```

주의:

- 검색 조건이 Query Key에 빠지면 잘못된 cache 사용
- debounce가 너무 길면 UX 지연
- 이전 요청이 늦게 도착해 최신 결과를 덮는 race condition 주의
- filter state를 local에만 두면 새로고침 / 공유 링크 복원 어려움
- sort key를 사용자 입력 그대로 서버에 전달하지 않기

---

### [FAQ]

Q. 검색어를 Query Key에 넣어야 하나?

A.
그렇다. 검색어가 다르면 다른 결과이므로 Query Key에 포함해야 한다.

Q. 검색 상태는 URL에 넣는 게 좋은가?

A.
공유, 새로고침, 뒤로가기 복원이 필요하면 URL search params에 넣는 것이 좋다.

Q. 필터 변경 시 pagination은 어떻게 해야 하나?

A.
일반적으로 첫 페이지로 reset해야 한다. 기존 page가 새 필터 조건에서 유효하지 않을 수 있기 때문이다.

---

# 13. Request Waterfall and Deduplication Rules

## 13.1 Request Waterfall / 중복 요청 방지

### [개념]

Request Waterfall은 독립적인 요청이 불필요하게 순차 실행되어 전체 로딩 시간이 길어지는 문제이다.

Request Deduplication은 같은 요청이 동시에 여러 번 발생할 때 하나로 합치거나 cache를 재사용하는 전략이다.

---

### [핵심]

문제 유형:

- Sequential Independent Requests
- Duplicate Requests
- Parent-child Fetch Waterfall
- Client Refetch after Server Fetch
- Same Query Multiple Components
- Route Transition Refetch
- Provider Remount Refetch
- Search Race Condition
- Redundant API Client Call

개선 Flow:

```text
Network Waterfall 확인
→ 독립 요청 식별
→ 병렬화 가능 여부 판단
→ 공통 상위에서 fetch
→ Query Cache 공유
→ 중복 요청 제거
```

---

### [실무]

작성 기준:

- 독립 요청은 병렬 처리
- 의존 관계가 있는 요청만 순차 처리
- 같은 데이터를 여러 컴포넌트에서 요청하면 Query Key 공유
- Server Component에서 가져온 데이터를 Client Query가 즉시 다시 요청하지 않게 설계
- prefetch / hydration으로 중복 초기 요청 감소
- provider remount로 query가 반복 실행되는지 확인
- route 이동 시 필요한 데이터 prefetch 검토
- API client request dedupe 가능성 검토
- DevTools Network로 실제 요청 수 확인

주의:

- 병렬화가 항상 좋은 것은 아니며 서버 부하 고려
- 인증 선행 요청이 필요한 경우 dependent query 사용
- 같은 URL이어도 auth / locale / params가 다르면 다른 요청일 수 있음
- 중복 요청 제거가 데이터 신선도 문제를 만들지 않게 stale time 확인

---

### [FAQ]

Q. Request Waterfall은 왜 문제인가?

A.
독립적인 요청이 순차 실행되면 전체 대기 시간이 길어져 초기 렌더링과 사용자 체감 속도가 느려진다.

Q. 같은 API가 여러 번 호출되면 어떻게 해야 하나?

A.
Query Key를 공유하고 cache / deduplication을 활용하거나 상위에서 한 번 fetch해 전달하는 구조를 검토한다.

Q. Server Component에서 가져온 데이터를 Client에서 다시 가져오면 안 되나?

A.
필요할 수 있지만 의도하지 않은 중복 요청이면 hydration, initialData, prefetch 전략을 검토해야 한다.

---

# 14. Error Handling Rules

## 14.1 Server State Error 처리

### [개념]

Server State Error Handling은 API 실패, 네트워크 오류, 인증 만료, 권한 없음, validation error, timeout, 서버 장애를 구분하고 사용자에게 적절히 안내하는 기준이다.

---

### [핵심]

Error 유형:

- Network Error
- Timeout Error
- 400 Validation Error
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 429 Rate Limit
- 500 Server Error
- Unknown Error
- Abort Error

UI 상태:

- Field Error
- Form Error
- Page Error
- Inline Error
- Toast Error
- Error Boundary
- Retry UI
- Fallback UI

---

### [실무]

작성 기준:

- API Client에서 error normalization
- 사용자 메시지와 개발자 로그 분리
- 401은 로그인 만료 / 재인증 처리
- 403은 권한 없음 처리
- 404는 not found UI 처리
- validation error는 field와 연결
- 500은 일반 오류 메시지 + retry 가능성 제공
- timeout / network error는 재시도 안내
- abort error는 일반 오류로 표시하지 않음
- Error Boundary와 Query Error Reset Boundary 연계 가능
- Observability에 endpoint / status / trace id 기록

예시:

```ts
type ApiError =
  | { type: "unauthorized"; message: string }
  | { type: "forbidden"; message: string }
  | { type: "validation"; fieldErrors: Record<string, string> }
  | { type: "network"; message: string }
  | { type: "server"; message: string };
```

주의:

- 서버 raw error를 사용자에게 그대로 노출 금지
- 모든 error를 toast 하나로 처리하면 UX가 나빠질 수 있음
- 401과 403을 혼동하지 않기
- retry가 위험한 mutation에 자동 retry 금지
- error logging에 request body / token 포함 금지

---

### [FAQ]

Q. API Error는 어떻게 처리해야 하나?

A.
API Client에서 error를 정규화하고 status별로 사용자 메시지, retry 여부, 로그인 만료, 권한 없음, validation error를 구분한다.

Q. 401과 403은 어떻게 다르게 처리하나?

A.
401은 인증 만료나 로그인 필요 상태이고, 403은 로그인은 되었지만 권한이 없는 상태이다.

Q. 서버 에러 메시지를 그대로 보여줘도 되나?

A.
권장하지 않는다. 사용자에게는 안전한 메시지를 보여주고 상세 정보는 로그에 남긴다.

---

# 15. Loading / Empty / Success State Rules

## 15.1 서버 상태 UI 상태 설계

### [개념]

Server State UI는 데이터를 가져오는 동안 Loading, 데이터가 없을 때 Empty, 성공 시 Success, 실패 시 Error 상태를 명확히 제공해야 한다.

---

### [핵심]

상태 유형:

- Initial Loading
- Background Loading
- Refetching
- Pending Mutation
- Empty State
- Partial Empty
- Success State
- Error State
- Stale State
- Offline State
- Skeleton
- Spinner
- Disabled State

---

### [실무]

작성 기준:

- 최초 로딩과 background refetch 구분
- 전체 페이지 skeleton과 부분 skeleton 구분
- 빈 목록에는 다음 행동 안내
- 검색 결과 없음과 데이터 없음 구분
- mutation pending 중 중복 제출 방지
- background refetch 중 기존 데이터 유지 가능
- stale data 표시 여부 결정
- error 후 retry 버튼 제공
- Suspense 사용 시 fallback 위치 신중히 설계
- 접근성을 위해 loading 상태 전달

주의:

- 매 refetch마다 전체 화면 spinner로 바꾸면 UX가 나쁨
- Empty State를 Error State처럼 표시하지 않기
- Skeleton 공간이 실제 콘텐츠와 달라 CLS 발생 주의
- pending 중 버튼 disable만 하고 안내가 없으면 혼란 가능
- 오래 걸리는 요청에는 사용자 피드백 필요

---

### [FAQ]

Q. 최초 Loading과 Refetching은 다르게 보여야 하나?

A.
대부분 다르게 처리하는 것이 좋다. 최초 로딩은 skeleton, refetching은 기존 데이터 유지 + 작은 loading indicator가 더 자연스럽다.

Q. Empty State는 왜 중요한가?

A.
데이터가 없을 때 화면이 비어 보이지 않고 사용자가 다음 행동을 이해할 수 있게 하기 위해 중요하다.

Q. 검색 결과 없음과 전체 데이터 없음은 같은가?

A.
아니다. 검색 결과 없음은 조건을 바꾸도록 안내하고, 전체 데이터 없음은 생성이나 시작 행동을 안내하는 것이 좋다.

---

# 16. Authentication-aware Fetching Rules

## 16.1 인증 상태 기반 Fetching

### [개념]

Authentication-aware Fetching은 로그인 상태, 세션 만료, 권한, role, token refresh에 따라 데이터 요청과 UI 상태를 안전하게 처리하는 전략이다.

---

### [핵심]

검토 대상:

- Current User Query
- Authenticated Query
- Protected Query
- Permission Query
- Token Refresh
- 401 Handling
- 403 Handling
- Logout Cleanup
- Cache Clear
- User Scope
- Private Cache
- Session Expiration

---

### [실무]

작성 기준:

- `me` / current user query를 인증 상태 기준으로 관리
- 로그인 전에는 protected query 비활성화
- 401 발생 시 refresh 또는 logout flow
- 403 발생 시 권한 없음 UI
- logout 시 사용자별 query cache 정리
- 다른 계정 로그인 시 이전 사용자 cache 노출 방지
- query key에 user scope 포함 검토
- auth token을 query key나 log에 넣지 않기
- refresh token 중복 요청 방지
- protected route와 protected query를 함께 설계

주의:

- client auth state만 믿고 서버 데이터 요청 권한을 판단하지 않기
- logout 후 이전 사용자 데이터가 화면에 남지 않도록 처리
- refresh 실패 시 무한 retry 방지
- 권한 변경 후 menu / permission query invalidation 필요
- 401과 403 처리 분리

---

### [FAQ]

Q. 로그인 전 protected query는 어떻게 해야 하나?

A.
인증 상태가 확인되기 전에는 query를 비활성화하거나 current user 확인 후 실행해야 한다.

Q. 로그아웃할 때 query cache를 지워야 하나?

A.
사용자별 민감 데이터가 있다면 반드시 정리해야 한다. 다른 계정으로 로그인했을 때 이전 데이터가 보이면 안 된다.

Q. Token을 Query Key에 넣어도 되나?

A.
안 된다. token은 민감정보이며 cache key로 사용하면 보안과 관리 문제가 생긴다.

---

# 17. Next.js App Router Data Fetching Rules

## 17.1 App Router Data Fetching 기준

### [개념]

Next.js App Router에서는 Server Component, Client Component, Server Action, Route Handler, Fetch Cache, Revalidation을 조합해 Data Fetching을 설계한다.

---

### [핵심]

검토 대상:

- Server Component Fetching
- Client Component Query
- Server Action Mutation
- Route Handler
- Fetch Cache
- Revalidation
- Dynamic Rendering
- Static Rendering
- Streaming
- Suspense
- `loading.tsx`
- `error.tsx`
- `not-found.tsx`
- `revalidatePath`
- `revalidateTag`
- Search Params
- Dynamic Route

---

### [실무]

작성 기준:

- 초기 SEO 콘텐츠는 Server Component Fetching 검토
- 사용자 상호작용 후 갱신 데이터는 Client Query 검토
- mutation은 Server Action 또는 API mutation으로 분리
- mutation 후 Next.js Cache와 Client Query Cache 모두 고려
- Server Component에서 가져온 데이터를 Client Component에 최소한으로 전달
- 사용자별 데이터는 public cache 금지
- Search Params 기반 데이터는 URL State와 연결
- 느린 영역은 Suspense / Streaming으로 분리 가능
- `notFound()`와 404 UI 처리
- App Router의 Cache 정책과 Client Query cache를 혼동하지 않기

예시 구조:

```text
Server Component
→ 초기 데이터 fetch
→ Client Component에 필요한 최소 props 전달
→ Client Query로 상호작용 이후 refetch / mutation 처리
```

주의:

- Server Component 데이터를 Client Query Cache에 자동으로 넣는다고 가정하지 않기
- Server Action에서 mutation 후 client cache invalidation도 필요할 수 있음
- `revalidatePath`가 Client Query Cache를 직접 무효화하는 것은 아님
- Client Component에 민감 데이터 전체를 props로 전달하지 않기
- Route Handler를 내부 fetch proxy로 남용하지 않기

---

### [FAQ]

Q. Next.js App Router에서 Data Fetching은 어디서 해야 하나?

A.
초기 렌더링과 SEO 데이터는 Server Component, 사용자 상호작용과 빈번한 갱신은 Client Query, mutation은 Server Action 또는 API 계층에서 처리한다.

Q. `revalidatePath`를 호출하면 React Query cache도 갱신되나?

A.
아니다. Next.js Cache와 Client Query Cache는 별개이므로 필요하면 client query invalidation도 해야 한다.

Q. Server Component 데이터를 Client Component에 넘겨도 되나?

A.
가능하지만 화면에 필요한 최소 데이터만 전달해야 하며 민감 데이터 노출에 주의해야 한다.

---

# 18. Hydration / Dehydration Rules

## 18.1 Query Cache Hydration

### [개념]

Hydration / Dehydration은 서버에서 미리 가져온 데이터를 클라이언트 Query Cache에 전달해 초기 중복 요청을 줄이는 전략이다.

---

### [핵심]

필수 포함:

- Dehydration
- Hydration
- Initial Data
- Prefetch Query
- Query Cache Transfer
- Server Prefetch
- Client Query
- Duplicate Request Prevention
- Stale Time
- Serialization
- Sensitive Data

Flow:

```text
Server에서 query prefetch
→ dehydrated state 생성
→ HTML과 함께 전달
→ Client에서 hydrate
→ 같은 Query Key로 cache 재사용
```

---

### [실무]

작성 기준:

- 서버에서 prefetch한 query key와 client query key를 동일하게 유지
- stale time을 설정해 즉시 refetch 여부 제어
- 민감 데이터 직렬화 주의
- 너무 큰 dehydrated state는 HTML 크기 증가
- public data와 user data 구분
- 검색 / 상세 초기 데이터에 유용
- Server Component props 전달과 Query Hydration 중 선택 기준 명확화
- hydration mismatch와 혼동하지 않기
- 초기 중복 요청이 실제로 줄었는지 Network 확인

주의:

- 모든 query를 hydrate하지 않기
- 큰 목록 hydrate는 HTML payload 증가
- 사용자별 데이터 hydrate 시 보안 검토
- Query Key 불일치 시 cache 재사용 실패
- stale time 0이면 mount 후 즉시 refetch될 수 있음

---

### [FAQ]

Q. Query Hydration은 왜 사용하나?

A.
서버에서 미리 가져온 데이터를 클라이언트 Query Cache에 넣어 초기 중복 요청을 줄이고 빠르게 화면을 보여주기 위해 사용한다.

Q. Hydration하면 refetch가 안 되나?

A.
stale time 설정에 따라 다르다. stale 상태라면 mount 후 refetch될 수 있다.

Q. 모든 데이터를 hydrate하면 좋은가?

A.
아니다. HTML 크기와 민감 데이터 노출 위험이 있으므로 초기 화면에 필요한 데이터 중심으로 제한한다.

---

# 19. Prefetching Rules

## 19.1 Data Prefetch 전략

### [개념]

Prefetching은 사용자가 곧 필요로 할 가능성이 높은 데이터를 미리 가져와 route 이동이나 상호작용 시 대기 시간을 줄이는 전략이다.

---

### [핵심]

Prefetch 대상:

- Next Route Data
- Detail Page Data
- Hovered Item Detail
- Search Suggestion
- Next Page
- Infinite Query Next Cursor
- Authenticated User Data
- Critical Dashboard Widget

Prefetch Trigger:

- Link Visibility
- Hover
- Focus
- Idle Time
- Route Intent
- User Action
- Background Task

---

### [실무]

작성 기준:

- 사용 가능성이 높은 데이터만 prefetch
- 목록에서 상세 hover / focus 시 detail prefetch 가능
- 다음 페이지 / 다음 cursor prefetch 검토
- 로그인 후 `me` / 권한 / 메뉴 prefetch 가능
- prefetch 데이터도 Query Key 정확히 설계
- stale time 설정으로 prefetch 유효 시간 제어
- 모바일 네트워크에서 과도한 prefetch 주의
- 사용자별 데이터 prefetch는 인증과 보안 검토
- prefetch 실패는 사용자 오류로 표시하지 않음

주의:

- 무분별한 prefetch는 네트워크 낭비
- 사용하지 않는 데이터 cache 증가
- 저속 네트워크 / 데이터 절약 모드 고려
- prefetch가 서버 부하를 증가시킬 수 있음
- 민감 데이터 prefetch는 접근 권한 확인 필요

---

### [FAQ]

Q. Prefetch는 언제 유용한가?

A.
사용자가 곧 이동할 가능성이 높은 상세 페이지나 다음 페이지 데이터를 미리 가져올 때 유용하다.

Q. 모든 링크 데이터를 prefetch하면 좋은가?

A.
아니다. 네트워크 낭비와 서버 부하가 생길 수 있으므로 가능성이 높은 경로에 제한해야 한다.

Q. Prefetch 실패를 사용자에게 보여줘야 하나?

A.
일반적으로 아니다. 실제 사용자가 해당 데이터를 요청할 때 다시 fetch하면 된다.

---

# 20. Abort / Race Condition Rules

## 20.1 요청 취소 / 경쟁 상태 방지

### [개념]

Abort / Race Condition 처리는 사용자의 빠른 입력, route 이동, 조건 변경으로 인해 오래된 요청 결과가 최신 UI를 덮어쓰는 문제를 방지하는 전략이다.

---

### [핵심]

문제 상황:

- Search Input Rapid Change
- Filter Change
- Route Change
- Component Unmount
- Slow Previous Request
- Fast Latest Request
- Duplicate Submit
- Mutation Race
- Stale Response Override

방어 기준:

- AbortController
- Request Cancellation
- Latest-only Update
- Query Key Isolation
- Debounce
- Disable During Pending
- Idempotency Key
- Version Check

---

### [실무]

작성 기준:

- 검색어 변경 시 이전 요청 취소 검토
- query key에 조건을 포함해 응답 섞임 방지
- 컴포넌트 unmount 후 state update 방지
- 중복 제출 방지
- mutation 순서가 중요한 경우 pending 관리
- 느린 이전 응답이 최신 결과를 덮지 않게 처리
- Abort Error는 일반 오류로 표시하지 않음
- 결제 / 생성 요청은 idempotency key 검토
- 빠른 입력에는 debounce + abort 조합 가능

예시:

```ts
const controller = new AbortController();

fetch("/api/search?q=react", {
  signal: controller.signal,
});

controller.abort();
```

주의:

- abort가 서버 작업까지 항상 취소하는 것은 아님
- retry와 abort가 충돌하지 않게 관리
- debounce만으로 race condition이 완전히 사라지지 않을 수 있음
- mutation race는 cache 불일치 원인
- request cancellation은 API client 계층에서 일관되게 처리

---

### [FAQ]

Q. Race Condition은 언제 발생하나?

A.
이전 요청이 늦게 도착해 최신 요청 결과를 덮어쓸 때 발생한다. 검색, 필터, route 이동에서 자주 발생한다.

Q. AbortController는 왜 쓰나?

A.
불필요한 요청을 취소하고 오래된 응답이 UI에 반영되는 문제를 줄이기 위해 사용한다.

Q. Abort Error도 사용자에게 보여줘야 하나?

A.
보통 아니다. 사용자가 조건을 바꾸거나 이동해서 취소된 요청은 오류로 안내하지 않는 것이 자연스럽다.

---

# 21. Retry and Offline Rules

## 21.1 Retry / Offline 지원

### [개념]

Retry는 실패한 요청을 다시 시도하는 전략이고, Offline Support는 네트워크가 불안정하거나 끊긴 상황에서도 사용자 경험을 관리하는 전략이다.

---

### [핵심]

검토 대상:

- Retry Count
- Retry Delay
- Exponential Backoff
- Retry Condition
- Idempotent Query
- Non-idempotent Mutation
- Offline State
- Reconnect Refetch
- Persisted Query Cache
- Offline Mutation Queue
- Conflict Resolution
- Network Status

---

### [실무]

작성 기준:

- GET query는 제한적 retry 가능
- 500 / network error는 retry 후보
- 400 / 401 / 403은 일반적으로 retry 대상 아님
- mutation retry는 idempotency가 보장될 때만 검토
- 결제 / 주문 / 삭제는 자동 retry 주의
- offline 상태 UI 제공
- reconnect 시 stale query refetch 검토
- offline mutation queue는 conflict 정책 필요
- retry 횟수와 delay 제한
- 사용자가 직접 retry할 수 있는 UI 제공

주의:

- 무한 retry 금지
- retry가 서버 부하를 증가시킬 수 있음
- 권한 오류를 retry해도 해결되지 않음
- offline cache에는 민감 데이터 저장 주의
- mutation retry는 중복 처리 위험

---

### [FAQ]

Q. API 실패 시 자동 retry를 항상 해야 하나?

A.
아니다. 네트워크 오류나 500 계열에는 유용할 수 있지만 400, 401, 403이나 위험한 mutation에는 부적합할 수 있다.

Q. 결제 요청을 retry해도 되나?

A.
주의해야 한다. 중복 결제 방지를 위한 idempotency key와 서버 보장이 없으면 자동 retry하면 안 된다.

Q. 오프라인 상태에서는 어떻게 처리해야 하나?

A.
offline UI를 제공하고, 캐시된 데이터 표시 여부와 재연결 시 refetch 기준을 정해야 한다.

---

# 22. Real-time Server State Rules

## 22.1 실시간 서버 상태 동기화

### [개념]

Real-time Server State는 WebSocket, Server-Sent Events, Polling, Push Notification 등으로 서버 변경 사항을 클라이언트 cache와 UI에 반영하는 전략이다.

---

### [핵심]

실시간 방식:

- WebSocket
- Server-Sent Events
- Polling
- Long Polling
- Push Notification
- Background Refetch
- Cache Update
- Query Invalidation
- Event-driven Update

적합 대상:

- Chat Message
- Notification
- Live Dashboard
- Stock / Price
- Order Status
- Collaboration
- Realtime Count
- Presence

---

### [실무]

작성 기준:

- 실시간성이 필요한 데이터인지 먼저 판단
- 단순 최신화는 polling / background refetch로 충분할 수 있음
- WebSocket 이벤트를 query cache update와 연결
- 새 메시지는 list cache에 append
- 알림 count는 별도 query 갱신
- 이벤트 누락 대비 refetch 전략 유지
- 연결 끊김 / 재연결 처리
- 중복 이벤트 dedupe
- 오래된 이벤트 ordering 처리
- 권한 없는 실시간 채널 접근 금지
- 메모리 누수 방지를 위해 subscription cleanup

주의:

- 모든 데이터에 WebSocket을 쓰지 않기
- 이벤트 기반 update와 query invalidation 중 선택
- optimistic update와 서버 이벤트 중복 반영 주의
- 실시간 이벤트 payload를 과신하지 말고 필요 시 refetch
- 다중 탭 연결 수 증가 고려

---

### [FAQ]

Q. 실시간 데이터는 항상 WebSocket을 써야 하나?

A.
아니다. 요구사항에 따라 polling, background refetch, SSE, WebSocket 중 선택한다.

Q. WebSocket 이벤트를 받으면 query를 invalidate해야 하나 cache를 직접 업데이트해야 하나?

A.
작은 변경은 cache 직접 update, 복잡하거나 일관성이 중요하면 invalidation 후 refetch를 고려한다.

Q. 실시간 이벤트가 중복으로 오면 어떻게 하나?

A.
id 기준 dedupe와 timestamp / sequence 기반 ordering 처리가 필요하다.

---

# 23. DTO / View Model Mapping Rules

## 23.1 API 응답과 화면 모델 분리

### [개념]

DTO / View Model Mapping은 서버 API 응답 구조를 화면에서 바로 사용하지 않고 필요한 형태로 변환하는 기준이다.

---

### [핵심]

모델 유형:

- Request DTO
- Response DTO
- Domain Model
- View Model
- Form Model
- Cache Model
- API Error Model

Mapping 기준:

```text
API Response DTO
→ Validation / Normalization
→ View Model
→ Component Props
```

---

### [실무]

작성 기준:

- API Response DTO와 Component Props를 분리
- 서버 필드명을 화면에 직접 강하게 결합하지 않기
- 날짜 / 금액 / enum은 mapping 계층에서 normalize
- nullable field 처리 기준 명확화
- 화면 표시용 derived value는 View Model에서 계산 가능
- API 변경 영향 범위를 API Client / Mapper에 제한
- TypeScript type과 runtime validation을 구분
- 외부 API 응답은 runtime validation 검토
- cache에는 DTO 또는 normalized model 중 하나를 일관되게 사용

예시:

```ts
type FestivalResponseDto = {
  festivalId: number;
  title: string;
  eventStartDate: string;
};

type FestivalCardViewModel = {
  id: number;
  title: string;
  periodText: string;
};
```

주의:

- API 응답을 모든 컴포넌트에 직접 전달하면 변경 영향 증가
- mapper가 너무 비대하면 domain logic 분리 검토
- 같은 데이터를 여러 형태로 cache하면 동기화 어려움
- nullable 처리 누락은 runtime error 원인

---

### [FAQ]

Q. API 응답 타입을 그대로 컴포넌트 props로 써도 되나?

A.
작은 프로젝트에서는 가능하지만 변경 영향과 화면 요구가 커지면 DTO와 View Model을 분리하는 것이 좋다.

Q. Mapping 계층은 왜 필요한가?

A.
API 변경 영향 범위를 줄이고 화면에 필요한 형식으로 데이터를 안정적으로 변환하기 위해 필요하다.

Q. TypeScript 타입만 있으면 runtime validation은 필요 없나?

A.
아니다. TypeScript는 컴파일 타임 검증이고 외부 API 응답은 런타임에 깨질 수 있다.

---

# 24. API Client Layer Rules

## 24.1 API Client 계층 설계

### [개념]

API Client Layer는 fetch / axios 같은 HTTP 호출을 직접 컴포넌트에 흩뿌리지 않고 공통 요청, 응답, 에러, 인증, timeout, trace id를 처리하는 계층이다.

---

### [핵심]

책임:

- Base URL
- Request Config
- Auth Header
- Timeout
- Retry Policy
- Error Normalization
- Response Parsing
- DTO Typing
- Trace ID
- Abort Signal
- Token Refresh
- Logging / Observability
- Upload / Download

---

### [실무]

작성 기준:

- 컴포넌트에서 raw fetch 반복 금지
- API 함수는 resource 단위로 분리
- Error normalization을 API Client에서 수행
- 인증 header 주입 위치 명확화
- token refresh 중복 요청 방지
- timeout 설정
- AbortSignal 전달 가능하게 설계
- request / response logging에 민감정보 제외
- DTO type과 mapper 연결
- 테스트에서 mock하기 쉬운 구조
- Server-only API Client와 Browser API Client 구분

예시 구조:

```text
src
├ api
│  ├ client.ts
│  ├ postApi.ts
│  ├ userApi.ts
│  └ error.ts
```

주의:

- API Client가 UI toast를 직접 띄우면 재사용성이 낮아질 수 있음
- Browser client에 server secret 포함 금지
- 모든 error를 같은 type으로 뭉개지 않기
- token refresh 무한 루프 주의
- file upload / download는 별도 처리 기준 필요

---

### [FAQ]

Q. API Client Layer는 왜 필요한가?

A.
요청 설정, 인증, 에러 정규화, timeout, trace id, DTO typing을 일관되게 처리하기 위해 필요하다.

Q. 컴포넌트 안에서 fetch를 직접 호출하면 안 되나?

A.
간단한 경우는 가능하지만 프로젝트가 커지면 중복 코드와 에러 처리 불일치가 생기므로 API Client 계층이 좋다.

Q. API Client에서 toast를 바로 띄워도 되나?

A.
권장하지 않는다. API 계층은 에러 정보를 반환하고 UI 계층에서 표시 방식을 결정하는 것이 더 유연하다.

---

# 25. Suspense and Error Boundary Rules

## 25.1 Suspense / Error Boundary 연계

### [개념]

Suspense와 Error Boundary는 비동기 데이터 로딩과 오류 상태를 UI 경계 단위로 분리하는 React 패턴이다.

Server State 관리에서는 loading fallback, error fallback, retry/reset 흐름을 안정적으로 설계해야 한다.

---

### [핵심]

검토 대상:

- Suspense Boundary
- Error Boundary
- Query Error Reset
- Loading Fallback
- Error Fallback
- Retry
- Reset
- Partial Loading
- Route Segment Loading
- Route Segment Error
- Streaming
- Progressive Rendering

---

### [실무]

작성 기준:

- 느린 데이터 영역을 Suspense Boundary로 분리
- 전체 페이지를 불필요하게 fallback으로 가리지 않기
- Error Boundary는 feature / route 단위로 배치
- Error fallback에 retry 또는 reset 제공
- Query Error Reset과 Error Boundary 연계
- Next.js `loading.tsx` / `error.tsx`와 중복 역할 구분
- fallback UI는 layout shift를 최소화
- Suspense 적용 시 data fetching library의 지원 여부 확인
- Error Boundary에서 Observability 연계 가능

주의:

- Suspense가 API 자체를 빠르게 만들지는 않음
- fallback이 너무 많으면 UI가 조각나 보일 수 있음
- Error Boundary 없이 Suspense만 두면 오류 복구가 부족
- 모든 데이터를 Suspense로 처리할 필요는 없음
- 서버 / 클라이언트 Suspense 경계 차이를 이해해야 함

---

### [FAQ]

Q. Suspense는 언제 사용하나?

A.
느린 데이터 영역을 분리하고 준비된 UI부터 보여주고 싶을 때 사용한다.

Q. Error Boundary는 Server State에 왜 필요한가?

A.
데이터 요청 실패로 화면 전체가 깨지지 않도록 feature 또는 route 단위 fallback을 제공하기 위해 필요하다.

Q. Suspense를 쓰면 loading state를 직접 처리하지 않아도 되나?

A.
일부는 fallback으로 처리할 수 있지만 pending mutation, background refetch, empty state는 별도 설계가 필요하다.

---

# 26. Security and Privacy Rules

## 26.1 Data Fetching 보안 / 개인정보 기준

### [개념]

Server State는 사용자별 데이터와 민감정보를 포함할 수 있으므로 cache, log, URL, storage, hydration, prefetch에서 보안과 개인정보 보호 기준을 지켜야 한다.

---

### [핵심]

검토 대상:

- User-specific Data
- Private Cache
- Public Cache
- Token Exposure
- Query Key PII
- URL PII
- LocalStorage Cache
- Persisted Cache
- Hydrated Data
- API Log
- Request Body
- Response Body
- Authorization Header
- Role / Permission Data

---

### [실무]

작성 기준:

- 사용자별 데이터는 public cache 금지
- query key에 token / email / phone 같은 개인정보 넣지 않기
- URL search params에 민감정보 넣지 않기
- persisted cache에 민감 데이터 저장 주의
- logout 시 private cache 정리
- 다른 사용자 로그인 시 cache isolation
- API error log에 request body / token 포함 금지
- Client Component props로 민감 데이터 전달 최소화
- prefetch는 권한 확인 후 수행
- Server Action / Route Handler에서 권한 재검증
- optimistic update가 권한 실패를 숨기지 않게 처리

주의:

- Client Query Cache는 브라우저에서 접근 가능한 데이터
- Hydrated State는 HTML payload에 포함될 수 있음
- URL은 history / referrer / analytics에 남을 수 있음
- token refresh flow에서 token log 금지
- cache persistence는 보안 요구사항 확인 필요

---

### [FAQ]

Q. Query Key에 이메일을 넣어도 되나?

A.
권장하지 않는다. 사용자 ID 같은 내부 식별자도 필요한 경우에만 사용하고 개인정보는 피해야 한다.

Q. Hydration 데이터에 민감정보를 넣어도 되나?

A.
주의해야 한다. Hydrated State는 클라이언트로 전달되므로 화면에 필요한 최소 데이터만 포함해야 한다.

Q. 로그아웃 시 Query Cache를 지워야 하나?

A.
사용자별 데이터가 cache에 있다면 지워야 한다. 다른 계정이 이전 데이터를 볼 수 있으면 안 된다.

---

# 27. Testing Rules

## 27.1 Server State 테스트 기준

### [개념]

Server State Testing은 query, mutation, cache, invalidation, loading, error, optimistic update, pagination이 올바르게 동작하는지 검증하는 테스트이다.

---

### [핵심]

테스트 대상:

- Query Success
- Query Loading
- Query Error
- Empty State
- Mutation Success
- Mutation Error
- Cache Invalidation
- Optimistic Update
- Rollback
- Pagination
- Infinite Query
- Search / Filter
- Auth Error
- Retry
- Abort
- Query Key
- API Mock

---

### [실무]

작성 기준:

- API 응답은 MSW 등 네트워크 mock 사용
- Query Client는 테스트마다 새로 생성
- cache가 테스트 간 공유되지 않게 관리
- loading / success / error / empty 상태 검증
- mutation 후 invalidation 검증
- optimistic update rollback 검증
- pagination next page 검증
- filter 변경 시 page reset 검증
- 401 / 403 처리 검증
- race condition은 빠른 입력 / 지연 응답으로 테스트 가능
- 테스트에서 실제 token / 개인정보 사용 금지

예시 Flow:

```text
목록 조회 성공
→ 항목 표시
→ 새 항목 생성 mutation
→ 목록 query invalidation
→ 새 항목 표시
```

주의:

- 실제 API 호출하는 unit / component test 지양
- stale time 때문에 테스트 결과가 달라질 수 있음
- retry가 테스트를 느리게 만들 수 있음
- Query Cache reset 누락은 flaky test 원인
- optimistic update 테스트는 성공 / 실패 둘 다 필요

---

### [FAQ]

Q. Server State 테스트에서 가장 중요한 것은?

A.
loading, success, error, empty, mutation 후 invalidation, optimistic update rollback을 검증하는 것이다.

Q. Query Client는 테스트마다 새로 만들어야 하나?

A.
그렇다. cache 공유로 테스트가 오염되는 것을 막기 위해 테스트마다 독립 인스턴스를 쓰는 것이 좋다.

Q. API mock은 어디서 하는 것이 좋은가?

A.
Integration Test에서는 MSW 같은 네트워크 레벨 mock이 실제 흐름과 가까워 유용하다.

---

# 28. Troubleshooting Rules

## 28.1 자주 발생하는 Server State 문제

### [개념]

Troubleshooting 문서는 Agent가 Data Fetching / Server State 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- 데이터가 갱신되지 않음
- Mutation 후 목록이 안 바뀜
- 중복 요청 발생
- Request Waterfall 발생
- 검색 결과가 이전 요청으로 덮임
- 필터 변경 후 이전 페이지 데이터가 섞임
- Infinite Query 중복 item 발생
- Optimistic Update rollback 안 됨
- 401 이후 무한 retry
- 로그아웃 후 이전 사용자 데이터 보임
- Query Key 충돌
- Query Key 조건 누락
- Cache가 너무 빨리 stale됨
- Cache가 너무 오래 유지됨
- Hydration 후 즉시 refetch됨
- Server Component fetch 후 Client에서 재요청
- Error가 toast로만 표시됨
- Loading spinner가 계속 표시됨
- Race condition 발생
- Abort Error가 사용자에게 표시됨

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

- Mutation 성공 후 목록이 갱신되지 않음

원인:

- 관련 list query invalidation 누락
- Query Key가 mutation 대상과 다름
- stale time이 길고 refetch가 발생하지 않음
- cache update 로직 누락

해결:

- mutation 성공 후 관련 Query Key invalidate
- detail / list / count query 관계 확인
- mutation response로 cache update 검토
- DevTools로 Query Key 확인
```

예시:

```md
문제:

- 검색 결과가 이전 요청 결과로 덮임

원인:

- 검색어가 Query Key에 포함되지 않음
- 이전 요청 abort 처리 없음
- 느린 이전 응답이 최신 상태를 overwrite
- local state로 직접 응답을 저장

해결:

- 검색어 / 필터를 Query Key에 포함
- AbortController 적용
- 최신 요청만 반영
- Server State 도구의 cache isolation 사용
```

예시:

```md
문제:

- 로그아웃 후 이전 사용자 데이터가 보임

원인:

- 사용자별 Query Cache 정리 누락
- Query Key에 user scope 없음
- persistent cache에 private data 저장
- current user 상태만 초기화하고 server state cache는 유지

해결:

- logout 시 private query cache clear
- user scope가 필요한 key 재설계
- persisted cache에서 민감 데이터 제외
- 새 로그인 시 current user 기준 refetch
```

---

### [FAQ]

Q. 데이터가 안 바뀌면 무엇을 확인해야 하나?

A.
Query Key, invalidation, stale time, cache update, refetch 조건, Next.js revalidation과 client cache 관계를 확인해야 한다.

Q. 중복 요청이 계속 발생하면 무엇을 봐야 하나?

A.
Query Key 안정성, provider remount, stale time, Server Component와 Client Query 중복 fetch, 같은 API를 여러 위치에서 호출하는지 확인한다.

Q. 검색 결과가 꼬이면 무엇을 확인해야 하나?

A.
검색어 / 필터가 Query Key에 포함되는지, 이전 요청 취소와 race condition 처리가 있는지 확인한다.

---

# 29. Code Example Rules

## 29.1 코드 예제 작성 기준

### [개념]

Data Fetching / Server State Advanced 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- Query Key가 명확해야 함
- Error / Loading 상태 포함 권장
- Mutation 후 invalidation 포함 권장
- Optimistic Update는 rollback 포함
- 긴 전체 파일 금지
- Secret 하드코딩 금지
- Token / 개인정보 logging 금지
- 실제 API 키 포함 금지
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Query Key Factory
- API Client Function
- Query Hook
- Mutation Hook
- Invalidation
- Optimistic Update
- Pagination
- Infinite Query
- Search Query with URL State
- Abort Request
- Error Normalization
- Server Component Fetching
- Client Query Hydration
- Server Action Mutation
- Cache Clear on Logout
- MSW Test Handler

금지 예제:

- Server State를 전역 Client Store에 무분별하게 복사
- Query Key에 token 포함
- mutation 후 invalidation 없음
- optimistic update rollback 없음
- 모든 에러를 무시
- 모든 요청을 retry
- 결제 mutation 자동 retry
- 사용자별 데이터를 public cache
- Client Component에 secret 포함
- request body 전체 logging
- 거대한 API Client 단일 파일

---

### [FAQ]

Q. Server State 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. Optimistic Update 예제에는 무엇이 꼭 있어야 하나?

A.
이전 cache snapshot 저장, UI 선반영, 실패 시 rollback, 성공 후 정리 또는 refetch가 있어야 한다.

---

# 30. Comparison Rules

## 30.1 필수 비교 대상

### [개념]

Data Fetching / Server State Advanced 문서는 Agent의 데이터 전략 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Server State vs Client State
- Query vs Mutation
- Fetching vs Prefetching
- Refetch vs Invalidation
- Invalidation vs Direct Cache Update
- Optimistic Update vs Pessimistic Update
- Offset Pagination vs Cursor Pagination
- Pagination vs Infinite Scroll
- Polling vs WebSocket vs SSE
- Server Component Fetching vs Client Component Fetching
- Next.js Cache vs Client Query Cache
- `revalidatePath` vs Query Invalidation
- Initial Data vs Hydration
- `useState` Fetching vs Server State Library
- API DTO vs View Model
- Public Cache vs Private Cache
- Retry vs Manual Retry
- Debounce vs Abort
- Loading State vs Refetching State
- Empty State vs Error State

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 장점 / 위험 / 적합 상황 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Query와 Mutation 차이는?

A.
Query는 서버 데이터를 읽는 작업이고, Mutation은 서버 데이터를 변경하는 작업이다.

Q. Next.js Cache와 React Query Cache는 같은가?

A.
아니다. Next.js Cache는 framework/server rendering과 연결되고, React Query Cache는 client server state cache이다.

Q. Optimistic Update와 Pessimistic Update 차이는?

A.
Optimistic은 서버 응답 전 UI를 먼저 바꾸고 실패 시 rollback하며, Pessimistic은 서버 성공 후 UI를 바꾼다.

---

# 31. Checklist Rules

## 31.1 문서 품질 체크리스트

### [개념]

Data Fetching / Server State Advanced RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Data Fetching / Server State 목적이 명확한가?
- [ ] Server State와 Client State 차이를 포함했는가?
- [ ] Fetching 위치 결정 기준을 포함했는가?
- [ ] Server Component / Client Component Fetching 기준을 포함했는가?
- [ ] Query Key 설계 기준을 포함했는가?
- [ ] Cache Strategy 기준을 포함했는가?
- [ ] Invalidation / Revalidation 기준을 포함했는가?
- [ ] Mutation 기준을 포함했는가?
- [ ] Optimistic Update / Rollback 기준을 포함했는가?
- [ ] Pagination / Infinite Query 기준을 포함했는가?
- [ ] Search / Filter / Sort 기준을 포함했는가?
- [ ] Request Waterfall / 중복 요청 기준을 포함했는가?
- [ ] Error Handling 기준을 포함했는가?
- [ ] Loading / Empty / Success 상태 기준을 포함했는가?
- [ ] 인증 상태 기반 Fetching 기준을 포함했는가?
- [ ] Next.js App Router Data Fetching 기준을 포함했는가?
- [ ] Hydration / Dehydration 기준을 포함했는가?
- [ ] Prefetch 기준을 포함했는가?
- [ ] Abort / Race Condition 기준을 포함했는가?
- [ ] Retry / Offline 기준을 포함했는가?
- [ ] Real-time Server State 기준을 포함했는가?
- [ ] DTO / View Model Mapping 기준을 포함했는가?
- [ ] API Client Layer 기준을 포함했는가?
- [ ] Suspense / Error Boundary 기준을 포함했는가?
- [ ] Security / Privacy 기준을 포함했는가?
- [ ] Testing 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Next.js / Performance / Security / Testing 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 도구 사용법보다 데이터 흐름과 판단 기준 중심으로 작성
- Frontend Architecture / Next.js / Performance / Security / Testing 문서와 연계 가능해야 함

---

### [FAQ]

Q. Data Fetching / Server State 문서 품질에서 가장 중요한 것은?

A.
Server State와 Client State 구분, Query Key, Cache, Invalidation, Mutation, Error State, Next.js Cache와 Client Query Cache의 경계가 명확해야 한다.

---

# 32. Retrieval Optimization Rules

## 32.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Data Fetching
- Server State
- Client State
- Query
- Mutation
- Query Key
- Query Cache
- Cache Invalidation
- Revalidation
- Refetch
- Stale Time
- Cache Time
- Garbage Collection
- Optimistic Update
- Rollback
- Pagination
- Infinite Query
- Cursor Pagination
- Offset Pagination
- Search Params
- URL State
- Request Waterfall
- Request Deduplication
- Race Condition
- AbortController
- Retry
- Offline Support
- React Query
- TanStack Query
- SWR
- Next.js Data Fetching
- Server Component Fetching
- Client Component Fetching
- Server Action Mutation
- Route Handler
- Fetch Cache
- Hydration
- Dehydration
- Prefetch
- API Client
- Error Normalization
- DTO Mapping
- View Model
- Query Key Factory
- Background Refetch
- Stale Data
- Private Cache
- Public Cache

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Server State가 뭐야?
- Server State와 Client State 차이
- Data Fetching은 어디서 해야 해?
- Server Component에서 fetch할까 Client에서 fetch할까?
- Query Key는 어떻게 설계해?
- stale time은 뭐야?
- cache time은 뭐야?
- mutation 후 데이터가 안 바뀌어
- query invalidation은 언제 해?
- optimistic update는 언제 써?
- optimistic update rollback 어떻게 해?
- offset pagination과 cursor pagination 차이
- infinite query 중복 데이터 발생
- 검색어를 Query Key에 넣어야 해?
- 필터 변경 시 page reset 해야 해?
- request waterfall 어떻게 줄여?
- 같은 API가 여러 번 호출돼
- 검색 결과가 이전 요청으로 덮여
- AbortController는 언제 써?
- 401과 403은 어떻게 처리해?
- 로그아웃 후 이전 사용자 데이터가 보여
- Next.js Cache와 React Query Cache 차이
- revalidatePath 하면 client query도 갱신돼?
- hydration 후 즉시 refetch돼
- Server State 테스트는 어떻게 해?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 33. Version Rules

## 33.1 기준 버전

### [개념]

Data Fetching / Server State Advanced 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern React
- React 19+
- Next.js App Router
- TypeScript
- Server Component
- Client Component
- Server Action
- Route Handler
- TanStack Query / React Query 계열
- SWR 계열
- Fetch Cache
- Revalidation
- Suspense
- Streaming
- URL State
- API Client Layer
- Privacy-aware Cache
- Testable Data Layer

Legacy 제외:

- 모든 서버 데이터를 `useState`와 `useEffect`로 직접 관리하는 방식
- 모든 데이터를 Redux / 전역 store에 복사하는 방식
- Query Key 없이 임의 cache 관리
- mutation 후 invalidation 없는 구조
- loading / error state 없는 fetch
- token을 Query Key에 넣는 방식
- 사용자별 데이터를 public cache하는 방식
- 모든 요청을 자동 retry하는 방식
- race condition을 무시하는 검색 구현
- Server Component와 Client Query Cache를 혼동하는 설명

---

### [실무]

문서 작성 시 주의:

- TanStack Query / SWR / Next.js API는 버전별 차이가 있을 수 있음
- 특정 도구 API보다 Server State 원칙과 판단 기준을 우선
- Next.js App Router Cache 정책은 버전별 변화 가능성 있음
- React Server Component와 Client Component 경계를 명확히 설명
- Frontend Performance 문서의 Request Waterfall / Hydration 기준과 연계
- Frontend Security 문서의 사용자별 데이터 / token / cache 보안 기준과 연계
- Frontend Testing 문서의 API Mock / Query Cache 테스트 기준과 연계

---

### [FAQ]

Q. Data Fetching 문서는 특정 라이브러리 기준이어야 하나?

A.
아니다. React Query, TanStack Query, SWR, Next.js Cache를 다룰 수 있지만 핵심은 Server State 관리 원칙과 판단 기준이다.

Q. Next.js App Router 기준을 고려해야 하나?

A.
그렇다. Server Component Fetching, Client Query, Server Action, Revalidation의 경계를 고려해야 한다.

---

# 34. Common Mistakes

## 34.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Data Fetching / Server State 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Server State와 Client State를 구분하지 않음
- 서버 데이터를 전역 Client Store에 무분별하게 복사
- Query Key에 filter / page / sort 누락
- Query Key에 token / 개인정보 포함
- Mutation 후 invalidation 누락
- Optimistic Update rollback 누락
- 모든 mutation에 자동 retry 적용
- 결제 / 주문 mutation을 중복 제출 가능하게 둠
- 검색 요청 race condition 방치
- 이전 요청 abort 처리 없음
- Infinite Query에서 중복 item 제거 없음
- 필터 변경 후 page reset 누락
- 같은 API를 여러 컴포넌트에서 중복 호출
- Server Component fetch 후 Client에서 즉시 재요청
- Hydration Query Key 불일치
- stale time 설정 없이 불필요한 refetch 반복
- cache를 너무 오래 유지해 stale data 표시
- 로그아웃 후 사용자별 cache 정리 누락
- 401과 403 처리 혼동
- raw server error를 그대로 표시
- request body / token을 log에 남김
- API DTO를 모든 컴포넌트 props로 직접 전달
- Loading / Error / Empty 상태 누락
- Query Client를 테스트마다 초기화하지 않음

---

### [실무]

리뷰 기준:

- Server State / Client State 구분 확인
- Fetching 위치 확인
- Query Key 조건 포함 여부 확인
- Cache 정책 확인
- Mutation 후 invalidation 확인
- Optimistic Update rollback 확인
- Pagination cursor / page 처리 확인
- Search / Filter / Sort URL State 확인
- Request Waterfall 확인
- 중복 API 요청 확인
- Error normalization 확인
- 401 / 403 처리 확인
- Logout cache clear 확인
- Next.js Cache와 Client Cache 경계 확인
- 민감 데이터 cache / log 여부 확인
- 테스트에서 Query Cache 초기화 확인

---

### [FAQ]

Q. Server State에서 가장 흔한 실수는?

A.
Query Key를 잘못 설계하고 mutation 후 invalidation을 누락해 stale data가 화면에 남는 것이다.

Q. 검색 기능에서 가장 흔한 실수는?

A.
검색어와 필터를 Query Key에 넣지 않거나 이전 요청 취소 / race condition 처리를 하지 않는 것이다.

Q. Next.js와 React Query를 같이 쓸 때 흔한 실수는?

A.
Next.js Cache와 Client Query Cache를 같은 것으로 착각하고 `revalidatePath`만 호출하면 client cache도 갱신된다고 생각하는 것이다.

---

# 35. Final Goal

## 35.1 최종 목표

### [개념]

Data Fetching / Server State Advanced RAG 문서는 Agent가 프론트엔드 프로젝트에서 서버 데이터 흐름과 cache, mutation, revalidation, error state를 설계, 생성, 검토, 개선할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Server State와 Client State 구분
- Data Fetching 위치 판단
- Server Component / Client Component Fetching 경계 설계
- Query Key 설계
- Cache Strategy 제안
- Stale Time / Cache Time 판단
- Invalidation / Revalidation 설계
- Mutation Flow 설계
- Optimistic Update / Rollback 설계
- Pagination / Infinite Query 설계
- Search / Filter / Sort URL State 설계
- Request Waterfall 진단
- 중복 요청 제거 제안
- Error Handling / Error Normalization 설계
- Loading / Empty / Success State 설계
- Authentication-aware Fetching 설계
- Next.js App Router Data Fetching 리뷰
- Hydration / Dehydration 전략 제안
- Prefetch 전략 제안
- Abort / Race Condition 문제 진단
- Retry / Offline 전략 판단
- Real-time Server State 설계
- DTO / View Model Mapping 제안
- API Client Layer 설계
- Server State 테스트 기준 제안
- Data Fetching 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Query Key / Cache / Mutation / Error / Pagination 경계 명확화
- Next.js Cache와 Client Query Cache의 차이 명확화
- Security / Performance / Testing 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Data Fetching / Server State Advanced Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 서버 데이터 fetching, cache, mutation, invalidation, pagination, error state, Next.js Cache와 Client Query Cache의 경계를 설계하고 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Data Fetching / Server State Advanced 문서는 어떤 기준으로 작성해야 해?

A.
Server State와 Client State 구분, Fetching 위치, Query Key, Cache, Invalidation, Mutation, Pagination, Error Handling, Next.js Cache 경계를 중심으로 작성해야 한다.

Q. Server State가 뭐야?

A.
서버가 소유하고 클라이언트가 비동기적으로 가져와 화면에 표시하는 데이터이다. 게시글, 댓글, 사용자 정보, 상품 목록, 알림 등이 해당한다.

Q. Server State와 Client State 차이는?

A.
Server State는 서버가 소유하고 stale될 수 있는 비동기 데이터이고, Client State는 브라우저 UI가 소유하는 로컬 상태이다.

Q. Form 입력값은 Server State야?

A.
제출 전 입력값은 Form State이고, 제출 후 서버에 저장된 결과는 Server State이다.

Q. Server State를 Redux나 Zustand에 넣어도 돼?

A.
가능은 하지만 cache, refetch, invalidation을 직접 관리해야 하므로 전용 Server State 도구가 더 적합한 경우가 많다.

Q. Data Fetching은 어디서 해야 해?

A.
초기 렌더링과 SEO 데이터는 Server Component, 사용자 상호작용 후 갱신되는 데이터는 Client Query, mutation은 Server Action 또는 API 계층에서 처리한다.

Q. Server Component에서 fetch할까 Client에서 fetch할까?

A.
SEO와 초기 HTML이 중요하면 Server Component, 상호작용과 background refetch가 중요하면 Client Component Query가 적합하다.

Q. 외부 API Secret이 필요한 요청은 어디서 해야 해?

A.
Server Component, Route Handler, Backend처럼 서버에서 처리해야 한다. Client Component에 secret을 노출하면 안 된다.

Q. Route Handler를 항상 거쳐야 해?

A.
아니다. Server Component에서 직접 서버 로직을 호출할 수 있으면 불필요한 내부 HTTP 호출을 피할 수 있다.

Q. Query Key는 어떻게 설계해?

A.
resource name, id, search keyword, filter, sort, page, cursor, locale, user scope처럼 데이터를 식별하는 조건을 안정적으로 포함한다.

Q. 검색어를 Query Key에 넣어야 해?

A.
그렇다. 검색어가 다르면 다른 결과이므로 Query Key에 포함해야 한다.

Q. 필터와 정렬도 Query Key에 넣어야 해?

A.
그렇다. filter와 sort가 다르면 서버 응답도 달라지므로 Query Key에 포함해야 한다.

Q. Query Key에 token 넣어도 돼?

A.
안 된다. token은 민감정보이며 cache key로 사용하면 보안과 관리 문제가 생긴다.

Q. stale time은 뭐야?

A.
캐시된 데이터를 신선하다고 간주하는 시간이다. 이 시간이 지나면 stale 상태가 되어 refetch 대상이 될 수 있다.

Q. cache time은 뭐야?

A.
사용되지 않는 cache 데이터가 메모리에 남아있는 시간이다. 도구에 따라 garbage collection time이라고 부르기도 한다.

Q. cache를 많이 쓰면 좋아?

A.
항상 그렇지는 않다. 데이터 신선도, 보안, invalidation 전략이 함께 있어야 한다.

Q. mutation 후 데이터가 안 바뀌어. 무엇을 봐?

A.
관련 Query Key invalidation, cache update, refetch 조건, stale time, Next.js revalidation 여부를 확인해야 한다.

Q. query invalidation은 언제 해?

A.
생성, 수정, 삭제, 좋아요, 댓글 작성처럼 서버 데이터가 변경된 후 관련 list, detail, count, dashboard query를 갱신해야 할 때 한다.

Q. 생성 후 어떤 query를 invalidate해?

A.
일반적으로 목록 query를 invalidate하고, 필요하면 관련 count나 dashboard query도 갱신한다.

Q. 수정 후 어떤 query를 invalidate해?

A.
수정된 detail query와 해당 항목이 포함된 list query를 함께 고려한다.

Q. 삭제 후 detail cache는 어떻게 해?

A.
삭제된 entity의 detail cache를 제거하거나 접근 시 not found 상태가 되도록 처리한다.

Q. Query와 Mutation 차이는?

A.
Query는 서버 데이터를 읽는 작업이고, Mutation은 서버 데이터를 변경하는 작업이다.

Q. Mutation 후에는 항상 invalidation해야 해?

A.
대부분 필요하다. 다만 mutation response로 cache를 직접 업데이트할 수도 있다.

Q. mutation pending 중에는 무엇을 해야 해?

A.
중복 제출을 막고 pending UI를 보여주며, 실패 시 복구 가능한 에러 메시지를 제공해야 한다.

Q. 결제 요청에 자동 retry를 적용해도 돼?

A.
주의해야 한다. 중복 결제 위험이 있으므로 idempotency key와 서버 보장이 없으면 자동 retry하면 안 된다.

Q. optimistic update는 언제 써?

A.
좋아요, 찜, 팔로우처럼 실패 가능성이 낮고 되돌리기 쉬운 작은 mutation에 적합하다.

Q. optimistic update rollback 어떻게 해?

A.
이전 cache snapshot을 저장하고 UI를 먼저 업데이트한 뒤, 실패하면 snapshot으로 되돌리고 필요하면 refetch한다.

Q. Optimistic Update를 결제나 주문에 써도 돼?

A.
권장하지 않는다. 금전, 재고, 권한이 관련된 작업은 서버 확정 후 UI를 갱신하는 것이 안전하다.

Q. offset pagination과 cursor pagination 차이는?

A.
Offset은 페이지 번호와 offset 기준이고, Cursor는 마지막 item 기준으로 다음 데이터를 가져온다. 데이터 변경이 잦으면 Cursor가 더 안정적이다.

Q. Infinite Query에서 중요한 것은?

A.
cursor, hasNextPage, Query Key, 중복 제거, filter 변경 시 reset 처리가 중요하다.

Q. infinite query 중복 데이터 발생하면?

A.
cursor 기준, 정렬 안정성, 중복 item dedupe, 같은 page 중복 요청 여부를 확인해야 한다.

Q. 무한 스크롤은 항상 좋아?

A.
아니다. 접근성, SEO, footer 접근, URL 복원성이 중요하면 pagination이나 load more가 더 적합할 수 있다.

Q. 검색 상태는 URL에 넣는 게 좋아?

A.
공유, 새로고침, 뒤로가기 복원이 필요하면 URL search params에 넣는 것이 좋다.

Q. 필터 변경 시 page reset 해야 해?

A.
일반적으로 첫 페이지로 reset해야 한다. 기존 page가 새 필터 조건에서 유효하지 않을 수 있다.

Q. 검색 결과가 이전 요청으로 덮여. 왜?

A.
검색어가 Query Key에 없거나 이전 요청 abort 처리 없이 느린 이전 응답이 최신 상태를 덮었을 수 있다.

Q. AbortController는 언제 써?

A.
검색어 변경, 필터 변경, route 이동, component unmount처럼 이전 요청이 더 이상 필요 없을 때 사용한다.

Q. Abort Error도 사용자에게 보여줘야 해?

A.
보통 아니다. 사용자가 조건을 바꾸거나 이동해서 취소된 요청은 오류로 안내하지 않는 것이 자연스럽다.

Q. request waterfall 어떻게 줄여?

A.
독립 요청을 병렬 처리하고, 같은 데이터를 공유 Query Key로 cache하며, Server Component와 Client Query 중복 요청을 줄인다.

Q. 같은 API가 여러 번 호출돼. 어떻게 해?

A.
Query Key 안정성, provider remount, stale time, 같은 API를 여러 위치에서 호출하는지, Server Component와 Client Query 중복 fetch를 확인한다.

Q. Client에서 같은 데이터를 여러 컴포넌트가 요청하면?

A.
같은 Query Key를 사용해 Query Cache를 공유하거나 상위에서 fetch해 필요한 곳에 전달한다.

Q. API Error는 어떻게 처리해?

A.
API Client에서 error를 정규화하고 status별로 사용자 메시지, retry 여부, 로그인 만료, 권한 없음, validation error를 구분한다.

Q. 401과 403은 어떻게 처리해?

A.
401은 인증 만료나 로그인 필요 상태로 처리하고, 403은 권한 없음 UI로 처리한다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?

A.
권장하지 않는다. 사용자에게는 안전한 메시지를 보여주고 상세 정보는 로그에 남긴다.

Q. Loading State는 어떻게 설계해?

A.
최초 로딩, background refetch, mutation pending을 구분하고 skeleton, inline loading, disabled state를 상황에 맞게 사용한다.

Q. Empty State는 왜 필요해?

A.
데이터가 없을 때 화면이 비어 보이지 않고 사용자가 다음 행동을 이해할 수 있게 하기 위해 필요하다.

Q. 검색 결과 없음과 데이터 없음은 같아?

A.
아니다. 검색 결과 없음은 조건 변경을 안내하고, 전체 데이터 없음은 생성이나 시작 행동을 안내하는 것이 좋다.

Q. 로그인 전 protected query는 어떻게 해?

A.
인증 상태가 확인되기 전에는 query를 비활성화하거나 current user 확인 후 실행해야 한다.

Q. 로그아웃 후 이전 사용자 데이터가 보여. 왜?

A.
사용자별 Query Cache 정리 누락, Query Key user scope 누락, persisted cache에 private data 저장이 원인일 수 있다.

Q. 로그아웃할 때 query cache 지워야 해?

A.
사용자별 민감 데이터가 있다면 반드시 정리해야 한다. 다른 계정으로 로그인했을 때 이전 데이터가 보이면 안 된다.

Q. Next.js Cache와 React Query Cache 차이는?

A.
Next.js Cache는 framework/server rendering과 연결되고, React Query Cache는 client server state cache이다.

Q. revalidatePath 하면 client query도 갱신돼?

A.
아니다. Next.js Cache와 Client Query Cache는 별개이므로 필요하면 client query invalidation도 해야 한다.

Q. Server Component 데이터를 Client Query Cache에 자동으로 넣어줘?

A.
자동으로 들어간다고 가정하면 안 된다. initialData, prefetch, hydration 전략을 명확히 설계해야 한다.

Q. Hydration은 왜 사용해?

A.
서버에서 미리 가져온 데이터를 클라이언트 Query Cache에 넣어 초기 중복 요청을 줄이고 빠르게 화면을 보여주기 위해 사용한다.

Q. hydration 후 즉시 refetch돼. 왜?

A.
Query Key가 다르거나 stale time이 0이라 mount 후 stale 상태로 판단되어 refetch될 수 있다.

Q. 모든 데이터를 hydrate하면 좋아?

A.
아니다. HTML 크기와 민감 데이터 노출 위험이 있으므로 초기 화면에 필요한 데이터 중심으로 제한한다.

Q. Prefetch는 언제 유용해?

A.
사용자가 곧 이동할 가능성이 높은 상세 페이지나 다음 페이지 데이터를 미리 가져올 때 유용하다.

Q. 모든 링크 데이터를 prefetch하면 좋아?

A.
아니다. 네트워크 낭비와 서버 부하가 생길 수 있으므로 가능성이 높은 경로에 제한해야 한다.

Q. API 실패 시 자동 retry를 항상 해야 해?

A.
아니다. 네트워크 오류나 500 계열에는 유용할 수 있지만 400, 401, 403이나 위험한 mutation에는 부적합할 수 있다.

Q. 오프라인 상태에서는 어떻게 처리해?

A.
offline UI를 제공하고, 캐시된 데이터 표시 여부와 재연결 시 refetch 기준을 정해야 한다.

Q. 실시간 데이터는 항상 WebSocket 써야 해?

A.
아니다. 요구사항에 따라 polling, background refetch, SSE, WebSocket 중 선택한다.

Q. WebSocket 이벤트 받으면 invalidate해야 해?

A.
작은 변경은 cache 직접 update, 복잡하거나 일관성이 중요하면 invalidation 후 refetch를 고려한다.

Q. API 응답 타입을 그대로 컴포넌트 props로 써도 돼?

A.
작은 프로젝트에서는 가능하지만 변경 영향과 화면 요구가 커지면 DTO와 View Model을 분리하는 것이 좋다.

Q. DTO와 View Model은 왜 분리해?

A.
API 변경 영향 범위를 줄이고 화면에 필요한 형식으로 데이터를 안정적으로 변환하기 위해 분리한다.

Q. TypeScript 타입만 있으면 runtime validation 필요 없어?

A.
아니다. TypeScript는 컴파일 타임 검증이고 외부 API 응답은 런타임에 깨질 수 있다.

Q. API Client Layer는 왜 필요해?

A.
요청 설정, 인증, 에러 정규화, timeout, trace id, DTO typing을 일관되게 처리하기 위해 필요하다.

Q. 컴포넌트 안에서 fetch 직접 호출하면 안 돼?

A.
간단한 경우는 가능하지만 프로젝트가 커지면 중복 코드와 에러 처리 불일치가 생기므로 API Client 계층이 좋다.

Q. API Client에서 toast를 바로 띄워도 돼?

A.
권장하지 않는다. API 계층은 에러 정보를 반환하고 UI 계층에서 표시 방식을 결정하는 것이 더 유연하다.

Q. Suspense는 언제 써?

A.
느린 데이터 영역을 분리하고 준비된 UI부터 보여주고 싶을 때 사용한다.

Q. Error Boundary는 Server State에 왜 필요해?

A.
데이터 요청 실패로 화면 전체가 깨지지 않도록 feature 또는 route 단위 fallback을 제공하기 위해 필요하다.

Q. Query Key에 이메일 넣어도 돼?

A.
권장하지 않는다. 개인정보나 민감정보는 Query Key, URL, log에 넣지 않는 것이 좋다.

Q. Hydration 데이터에 민감정보 넣어도 돼?

A.
주의해야 한다. Hydrated State는 클라이언트로 전달되므로 화면에 필요한 최소 데이터만 포함해야 한다.

Q. Server State 테스트는 어떻게 해?

A.
API mock을 사용해 loading, success, error, empty, mutation 후 invalidation, optimistic update rollback을 검증한다.

Q. Query Client는 테스트마다 새로 만들어야 해?

A.
그렇다. cache 공유로 테스트가 오염되는 것을 막기 위해 테스트마다 독립 인스턴스를 쓰는 것이 좋다.

Q. Data Fetching 코드 리뷰 기준은?

A.
Server State 구분, Fetching 위치, Query Key, Cache 정책, Mutation 후 Invalidation, Error 처리, Security, Next.js Cache와 Client Cache 경계를 확인한다.

Q. Data Fetching / Server State Advanced RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 서버 데이터 fetching, cache, mutation, invalidation, pagination, error state, Next.js Cache와 Client Query Cache의 경계를 설계하고 리뷰하게 만드는 것이다.

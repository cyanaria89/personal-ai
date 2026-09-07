# Next.js App Router Domain Rules

---

# 1. Domain Purpose

## 1.1 Next.js App Router Domain 목적

### [개념]

Next.js App Router Domain 문서는 Frontend Agent / Fullstack Agent / Review Agent용 RAG 문서 제작 규칙이다.

Next.js App Router는 `app` 디렉터리 기반 File-System Router이며, React Server Components, Suspense, Server Functions 같은 React 최신 기능을 활용하는 Router이다.

목적:

- Next.js App Router 구조 이해
- Server Component / Client Component 구분 지원
- Layout / Page / Route Segment 설계 지원
- Data Fetching / Caching / Revalidation 판단 지원
- Server Actions / Server Functions 작성 지원
- Route Handlers 작성 지원
- Metadata / SEO 구성 지원
- Loading / Error / Not Found UI 구성 지원
- Frontend Authentication Flow 지원
- Backend API 연동 지원
- Fullstack Feature 구현 지원
- Frontend 코드 리뷰 지원

---

### [핵심]

우선순위:

1. App Router 구조
2. Server Component 기본 원칙
3. Client Component 최소화
4. Data Fetching 위치 판단
5. Caching / Revalidation 전략
6. Server Actions / Mutating Data
7. Route Handlers
8. Layout / Page / Metadata
9. Error / Loading / Not Found 처리
10. Security / Authentication / Authorization
11. Performance / Streaming
12. Deployment Readiness

---

### [실무]

2026 실무 기준:

- App Router 기준으로 문서 작성
- Pages Router 중심 설명 금지
- Server Component 기본값 전제
- Client Component는 필요한 경우만 사용
- `use client` 남용 금지
- 데이터 조회는 가능한 Server Component에서 처리
- 데이터 변경은 Server Actions / Server Functions 또는 Route Handlers로 분리
- 외부 클라이언트가 호출해야 하는 API는 Route Handler 고려
- UI 상태와 브라우저 API 사용 시 Client Component 사용
- 인증 정보 / Secret / Token은 Client Component에 직접 노출 금지
- Caching / Revalidation / Dynamic Rendering 판단 기준 포함
- Loading / Error / Not Found 파일 기반 처리 포함
- TypeScript 기준 예제 우선

---

### [FAQ]

Q. Next.js App Router Domain 문서는 무엇을 위한 문서인가?

A.
Next.js App Router 기반 프로젝트에서 Agent가 라우팅, 컴포넌트 경계, 데이터 패칭, 캐싱, 서버 액션, Route Handler를 올바르게 설계하도록 돕는 RAG 문서 제작 규칙이다.

Q. Next.js App Router 문서는 사람 학습용인가?

A.
아니다. AI Agent Retrieval, 코드 생성, 코드 리뷰, 구조 판단을 위한 검색 최적화 문서이다.

Q. Next.js 문서는 Pages Router도 같이 다뤄야 하나?

A.
아니다. 이 Domain은 App Router 중심이다. Pages Router는 비교나 마이그레이션 문맥에서만 최소 언급한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Next.js App Router Domain 문서는 App Router 기반 프론트엔드 / 풀스택 개발에 필요한 핵심 주제를 포함한다.

---

### [핵심]

포함 범위:

- Next.js App Router
- `app` directory
- File-System Routing
- Route Segment
- `layout.tsx`
- `page.tsx`
- `template.tsx`
- `loading.tsx`
- `error.tsx`
- `global-error.tsx`
- `not-found.tsx`
- `route.ts`
- Server Component
- Client Component
- `use client`
- Server Functions
- Server Actions
- Mutating Data
- Route Handlers
- Request / Response Web API
- Data Fetching
- Fetch Cache
- Revalidation
- Dynamic Rendering
- Static Rendering
- Streaming
- Suspense
- Metadata API
- Dynamic Metadata
- Image Optimization
- Font Optimization
- Link / Navigation
- Redirect
- Middleware / Proxy
- Authentication Flow
- Protected Route
- Environment Variable
- Error Handling
- Form Handling
- Search Params
- Dynamic Route
- Parallel Route
- Intercepting Route
- Route Group
- Frontend Performance
- Frontend Security
- Frontend Testing Basics
- Deployment / Build

---

### [실무]

제외 범위:

- Pages Router 심화
- Legacy `pages/api` 중심 API Routes
- React Native
- Deep CSS Design System 상세
- Backend Framework 상세
- Database ORM 상세
- Kubernetes / Infra 심화
- React 기초 문법 전체 설명
- JavaScript 기초 문법 전체 설명

단, Backend API 연동, 인증, 배포 연결에 필요한 범위는 포함 가능하다.

---

### [FAQ]

Q. App Router 문서에 React 기초도 포함해야 하나?

A.
전체 React 기초를 포함하지 않는다. Server Component / Client Component / Suspense / Hooks 경계 판단에 필요한 React 지식만 포함한다.

Q. Route Handler는 Backend 문서인가 Frontend 문서인가?

A.
Next.js App Router에서는 Fullstack 경계 문서이다. 외부 요청 처리, BFF, Webhook, API Proxy 문맥에서 포함한다.

Q. Server Actions는 반드시 포함해야 하나?

A.
포함해야 한다. App Router에서 form submit, mutation, revalidation 처리의 핵심 패턴이다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Next.js App Router RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Next.js 문서는 구조 판단이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: 요청 → Routing → Rendering → Data Fetching → Response
- `[Comparison]`: Server Component vs Client Component
- `[Best Practice]`: Client Boundary 최소화
- `[Troubleshooting]`: Hydration Error, Cache Confusion, Dynamic Route 오류
- `[Checklist]`: 배포 전 점검

---

### [FAQ]

Q. Next.js 문서에 Flow가 필요한 이유는?

A.
App Router는 라우팅, 렌더링, 데이터 패칭, 캐싱이 연결되어 있어 요청 흐름을 명확히 해야 Retrieval과 코드 생성 품질이 좋아진다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. App Router Structure Rules

## 4.1 App Directory 구조

### [개념]

App Router는 `app` 디렉터리 내부의 폴더와 특수 파일을 기반으로 라우트를 구성한다. App Router는 layouts, nested routing, loading states, error handling 등을 지원한다.

---

### [핵심]

필수 포함:

- `app/`
- Route Segment
- Nested Route
- `layout.tsx`
- `page.tsx`
- `loading.tsx`
- `error.tsx`
- `not-found.tsx`
- `route.ts`
- Route Group
- Dynamic Segment
- Catch-all Segment

권장 구조:

```text
app
├ layout.tsx
├ page.tsx
├ loading.tsx
├ error.tsx
├ not-found.tsx
├ dashboard
│  ├ layout.tsx
│  ├ page.tsx
│  └ settings
│     └ page.tsx
├ posts
│  ├ page.tsx
│  └ [postId]
│     └ page.tsx
└ api
   └ health
      └ route.ts
```

---

### [실무]

문서 작성 기준:

- `page.tsx`는 URL에 대응되는 UI
- `layout.tsx`는 하위 Segment에 공유되는 UI
- `loading.tsx`는 Suspense 기반 로딩 UI
- `error.tsx`는 Route Segment 단위 에러 UI
- `not-found.tsx`는 404 UI
- `route.ts`는 HTTP 요청 처리
- Route Group은 URL에 영향을 주지 않는 구조화 용도
- Dynamic Segment는 `[id]` 패턴 사용
- URL 설계와 폴더 구조를 함께 설명

---

### [FAQ]

Q. `app` 폴더 안의 모든 폴더가 URL이 되나?

A.
기본적으로 Route Segment가 되지만 Route Group `(group)`은 URL 경로에 포함되지 않는다.

Q. `page.tsx`와 `layout.tsx` 차이는?

A.
`page.tsx`는 특정 Route의 화면이고, `layout.tsx`는 하위 Route들이 공유하는 공통 UI이다.

Q. `route.ts`는 언제 사용하나?

A.
HTTP 요청을 직접 처리해야 할 때 사용한다. 예를 들어 Webhook, API Proxy, 외부 클라이언트용 API에 적합하다.

---

# 5. Server Component Rules

## 5.1 Server Component 기본 원칙

### [개념]

App Router에서 Layout과 Page는 기본적으로 Server Component이다. Server Component는 서버에서 데이터를 가져오고 UI 일부를 서버에서 렌더링하며, 필요한 경우 결과를 캐시하고 클라이언트로 스트리밍할 수 있다.

---

### [핵심]

필수 포함:

- Server Component
- Default Component Type
- Server-side Rendering
- Direct Data Fetching
- Secret Protection
- Reduced Client JavaScript
- Streaming
- Async Component
- Database / Backend API 호출 위치

예시:

```tsx
export default async function PostsPage() {
  const posts = await getPosts();

  return (
    <main>
      {posts.map((post) => (
        <article key={post.id}>{post.title}</article>
      ))}
    </main>
  );
}
```

---

### [실무]

Server Component에 적합한 작업:

- 초기 데이터 조회
- SEO가 중요한 페이지 렌더링
- 민감한 Token / Secret을 사용하는 서버 로직
- Database / Backend API 호출
- Markdown / CMS / File 기반 콘텐츠 조회
- 사용자별 서버 검증
- 큰 의존성을 클라이언트 번들에서 제외

Server Component에서 피할 것:

- `useState`
- `useEffect`
- Browser API
- DOM 직접 접근
- 이벤트 핸들러 직접 사용
- 클라이언트 전용 라이브러리 직접 사용

---

### [FAQ]

Q. App Router에서 컴포넌트는 기본적으로 Server Component인가?

A.
그렇다. `app` 디렉터리의 Layout과 Page는 기본적으로 Server Component이다.

Q. Server Component에서 `useState`를 사용할 수 있나?

A.
사용할 수 없다. 상태, 이벤트, 브라우저 API가 필요하면 Client Component로 분리해야 한다.

Q. Server Component에서 데이터를 직접 가져와도 되나?

A.
가능하다. App Router에서는 Server Component에서 데이터 조회를 직접 수행하는 패턴이 일반적이다.

---

# 6. Client Component Rules

## 6.1 Client Component 사용 기준

### [개념]

Client Component는 브라우저에서 실행되는 상호작용 UI를 담당한다. `use client` 지시어는 해당 파일을 Client Component 경계로 만든다.

---

### [핵심]

Client Component가 필요한 경우:

- `useState`
- `useEffect`
- `useRef`
- Browser API
- Event Handler
- Form Interactive State
- Modal / Dropdown
- Carousel
- Client-side Validation
- Client-only Library
- Local Storage
- WebSocket Client

예시:

```tsx
"use client";

import { useState } from "react";

export function LikeButton() {
  const [liked, setLiked] = useState(false);

  return (
    <button onClick={() => setLiked(!liked)}>{liked ? "Liked" : "Like"}</button>
  );
}
```

---

### [실무]

Client Component 작성 규칙:

- `use client`는 필요한 Leaf Component에만 선언
- Page 전체를 Client Component로 만들지 않기
- Server Component에서 데이터 조회 후 Client Component에 props 전달
- 민감정보를 props로 전달하지 않기
- Client Bundle 크기 증가 주의
- UI Interaction 단위로 작게 분리

권장 구조:

```text
Server Page
→ Fetch Data
→ Render Static UI
→ Pass Safe Props
→ Client Component handles interaction
```

---

### [FAQ]

Q. `use client`는 어디에 붙이는 게 좋은가?

A.
상호작용이 필요한 가장 작은 컴포넌트 파일에 붙이는 것이 좋다.

Q. Page 전체에 `use client`를 붙여도 되나?

A.
가능하지만 권장하지 않는다. 서버 렌더링, 보안, 번들 최적화 장점이 줄어든다.

Q. Server Component에서 Client Component를 import할 수 있나?

A.
가능하다. Server Component가 데이터를 가져오고 Client Component에 안전한 props를 전달하는 구조가 일반적이다.

---

# 7. Server Component vs Client Component Comparison Rules

## 7.1 Component Boundary 판단

### [개념]

Server Component와 Client Component의 경계는 App Router 설계 품질을 결정한다.

---

### [핵심]

비교 기준:

| 기준        | Server Component        | Client Component       |
| ----------- | ----------------------- | ---------------------- |
| 실행 위치   | Server                  | Browser                |
| 기본 여부   | 기본값                  | `use client` 필요      |
| 데이터 조회 | 적합                    | 제한적                 |
| Secret 사용 | 가능                    | 금지                   |
| 상태 관리   | 불가                    | 가능                   |
| 이벤트 처리 | 불가                    | 가능                   |
| Browser API | 불가                    | 가능                   |
| 번들 영향   | 작음                    | 증가                   |
| SEO         | 유리                    | 상대적으로 불리        |
| 사용 예     | Page, Layout, Data View | Button, Modal, Form UI |

---

### [실무]

판단 Flow:

```text
Component가 상태나 이벤트를 사용하는가?
→ Yes: Client Component

Browser API가 필요한가?
→ Yes: Client Component

Secret / DB / Backend 내부 호출이 필요한가?
→ Yes: Server Component

단순 데이터 표시인가?
→ Server Component
```

---

### [FAQ]

Q. Server Component와 Client Component 중 무엇을 기본으로 선택해야 하나?

A.
Server Component를 기본으로 선택하고, 상호작용이 필요한 부분만 Client Component로 분리한다.

Q. Client Component가 많아지면 어떤 문제가 생기나?

A.
Client JavaScript Bundle이 커지고 Hydration 비용이 증가하며 서버 렌더링 장점이 줄어든다.

---

# 8. Data Fetching Rules

## 8.1 Data Fetching 위치 판단

### [개념]

App Router의 Data Fetching은 Server Component, Server Functions, Route Handlers, Client Component 중 어디에서 수행할지 판단하는 것이 중요하다.

---

### [핵심]

필수 포함:

- Server Component Fetching
- Backend API Fetching
- Database Fetching
- `fetch`
- Cache Option
- Revalidation
- Parallel Fetching
- Sequential Fetching
- Error Handling
- Loading UI

예시:

```tsx
async function getPosts() {
  const response = await fetch("https://api.example.com/posts", {
    next: { revalidate: 60 },
  });

  if (!response.ok) {
    throw new Error("Failed to fetch posts");
  }

  return response.json();
}
```

---

### [실무]

Data Fetching 판단 기준:

| 상황                        | 권장 위치                                        |
| --------------------------- | ------------------------------------------------ |
| 페이지 초기 데이터          | Server Component                                 |
| SEO 필요한 데이터           | Server Component                                 |
| 사용자 이벤트 후 조회       | Client Component 또는 Server Action              |
| 외부 앱도 호출해야 하는 API | Route Handler                                    |
| Form Mutation               | Server Action                                    |
| Webhook 처리                | Route Handler                                    |
| Secret 필요한 요청          | Server Component / Server Action / Route Handler |
| 브라우저 상태 기반 요청     | Client Component                                 |

---

### [FAQ]

Q. App Router에서 데이터를 어디서 가져와야 하나?

A.
초기 렌더링 데이터는 Server Component에서 가져오는 것이 기본이다. 사용자 이벤트 기반 조회는 Client Component나 Server Action을 고려한다.

Q. Client Component에서 fetch하면 안 되나?

A.
가능하지만 초기 페이지 데이터나 Secret이 필요한 요청은 Server Component에서 처리하는 것이 좋다.

Q. Route Handler를 거쳐서 내부 데이터를 다시 fetch해야 하나?

A.
항상 그럴 필요는 없다. Server Component는 서버 로직을 직접 호출할 수 있다.

---

# 9. Caching and Revalidation Rules

## 9.1 Cache 전략

### [개념]

Caching은 데이터 조회와 렌더링 결과를 저장해 반복 요청의 성능을 높이는 전략이다. Next.js는 App Router에서 Cache Components 및 이전 모델의 Caching / Revalidating 가이드를 제공한다. Cache Components는 `cacheComponents: true` 설정으로 활성화한다.

---

### [핵심]

필수 포함:

- Static Rendering
- Dynamic Rendering
- Fetch Cache
- Revalidation
- Cache Tag
- Path Revalidation
- Router Cache
- Request Memoization
- Cache Components
- `revalidatePath`
- `revalidateTag`
- `no-store`
- Dynamic Data

예시:

```tsx
const response = await fetch("https://api.example.com/posts", {
  next: { revalidate: 60 },
});
```

예시:

```tsx
const response = await fetch("https://api.example.com/me", {
  cache: "no-store",
});
```

---

### [실무]

Cache 판단 기준:

| 데이터 유형           | 권장 전략                     |
| --------------------- | ----------------------------- |
| 공지사항 / 블로그     | Revalidate                    |
| 상품 목록             | Revalidate 또는 Tag 기반 갱신 |
| 로그인 사용자 정보    | No Store                      |
| 관리자 통계           | Dynamic                       |
| 실시간 알림           | No Store 또는 Client Fetch    |
| 빌드 시 고정 콘텐츠   | Static                        |
| 자주 바뀌는 검색 결과 | Dynamic 또는 Query 기준 Fetch |

주의:

- 사용자별 데이터는 Static Cache에 저장하지 않기
- 인증 기반 응답은 Cache 정책 명확히 지정
- Mutation 이후 `revalidatePath` 또는 `revalidateTag` 고려
- Cache 동작은 Next.js 버전과 설정에 따라 달라질 수 있으므로 문서에 기준 버전 명시

---

### [FAQ]

Q. Next.js App Router에서 Cache가 중요한 이유는?

A.
렌더링 성능, 데이터 신선도, 사용자별 보안 응답에 직접 영향을 주기 때문이다.

Q. 로그인 사용자 정보는 Cache해도 되나?

A.
주의해야 한다. 사용자별 민감 데이터는 `no-store` 또는 Dynamic Rendering을 고려한다.

Q. Mutation 후 화면이 갱신되지 않으면 무엇을 확인해야 하나?

A.
`revalidatePath`, `revalidateTag`, Router Refresh, Cache 정책을 확인해야 한다.

---

# 10. Server Actions and Mutating Data Rules

## 10.1 Server Actions / Server Functions

### [개념]

Server Function은 서버에서 실행되는 비동기 함수이며, Action 또는 Mutation 문맥에서는 Server Action이라고 부른다. Server Action은 form submit, mutation 처리에 사용되며 호출 시 UI와 새 데이터를 한 번의 서버 왕복으로 반환할 수 있다.

---

### [핵심]

필수 포함:

- Server Function
- Server Action
- `"use server"`
- Form Action
- Mutation
- Validation
- Authentication Check
- Authorization Check
- Revalidation
- Redirect
- Error Result
- Progressive Enhancement

예시:

```tsx
"use server";

import { revalidatePath } from "next/cache";

export async function createPost(formData: FormData) {
  const title = String(formData.get("title") ?? "");

  if (!title) {
    return { ok: false, message: "Title is required" };
  }

  await savePost({ title });
  revalidatePath("/posts");

  return { ok: true };
}
```

---

### [실무]

Server Action 사용 기준:

- Form Submit
- Create / Update / Delete
- Like / Bookmark
- Profile Update
- Admin Mutation
- 서버 검증이 필요한 사용자 액션
- Mutation 후 Revalidation이 필요한 작업

주의:

- Server Action 내부에서 권한 검증 필수
- Client에서 전달한 값 신뢰 금지
- DB 변경 전 Validation 수행
- 성공 후 `revalidatePath` / `revalidateTag` / `redirect` 고려
- Error는 UI에서 처리 가능한 구조로 반환
- 민감한 작업은 CSRF / Origin / 인증 정책 확인
- Server Action은 POST 방식으로 호출된다.

---

### [FAQ]

Q. Server Action은 언제 사용하나?

A.
Form 제출이나 데이터 생성, 수정, 삭제 같은 Mutation 작업에 사용한다.

Q. Server Action 내부에서도 인증 검사가 필요한가?

A.
필요하다. Client에서 호출된다고 가정하고 서버에서 사용자 인증과 권한을 반드시 검증해야 한다.

Q. Server Action과 일반 서버 함수는 같은가?

A.
일반 서버 함수는 서버 내부에서 호출되는 함수이고, Server Action은 Client 또는 Form Action에서 호출 가능한 Mutation 진입점이다.

---

# 11. Route Handler Rules

## 11.1 Route Handler 작성 기준

### [개념]

Route Handler는 `app` 디렉터리 내부에서 Web Request / Response API를 사용해 특정 Route의 HTTP 요청을 처리하는 방식이다. Route Handlers는 `app` 디렉터리에서만 사용할 수 있으며 Pages Router의 API Routes에 대응되는 기능이다.

---

### [핵심]

필수 포함:

- `route.ts`
- GET
- POST
- PUT
- PATCH
- DELETE
- Request
- Response
- NextRequest
- NextResponse
- Dynamic Route Handler
- Webhook
- API Proxy
- BFF
- External Client API

예시:

```ts
export async function GET() {
  return Response.json({
    status: "ok",
  });
}
```

예시:

```ts
export async function POST(request: Request) {
  const body = await request.json();

  return Response.json({
    received: body,
  });
}
```

---

### [실무]

Route Handler 사용 기준:

| 상황                              | Route Handler 적합도 |
| --------------------------------- | -------------------- |
| 외부 서비스 Webhook               | 높음                 |
| 모바일 앱 / 외부 클라이언트 API   | 높음                 |
| Backend API Proxy                 | 높음                 |
| 파일 다운로드                     | 높음                 |
| 단순 Page 내부 데이터 조회        | 낮음                 |
| Server Component 내부 데이터 조회 | 낮음                 |
| Form Mutation                     | Server Action 우선   |
| 인증 콜백 처리                    | 높음                 |

주의:

- Route Handler는 `app` 디렉터리 안에서만 사용
- `pages/api`와 혼용하지 않기
- HTTP Method별 함수 명확히 작성
- 인증 / 권한 / Rate Limit 고려
- GET Route Handler의 Cache 동작 확인
- 외부 API Key는 서버 환경변수 사용

---

### [FAQ]

Q. Route Handler는 API Routes와 같은가?

A.
App Router에서 Route Handler는 Pages Router의 API Routes에 대응되는 기능이다. App Router에서는 `app/**/route.ts`를 사용한다.

Q. Server Component에서 데이터를 가져오기 위해 항상 Route Handler를 만들어야 하나?

A.
아니다. Server Component는 서버 함수나 DB 로직을 직접 호출할 수 있다.

Q. Route Handler는 언제 꼭 필요한가?

A.
외부 클라이언트가 호출해야 하거나 Webhook, API Proxy, 파일 응답처럼 HTTP 엔드포인트가 필요한 경우 적합하다.

---

# 12. Layout and Page Rules

## 12.1 Layout / Page 설계

### [개념]

`layout.tsx`는 하위 Route Segment에서 공유되는 UI이고, `page.tsx`는 URL에 대응되는 실제 화면이다.

---

### [핵심]

필수 포함:

- Root Layout
- Nested Layout
- Shared UI
- Page Component
- Children Prop
- Segment Layout
- Auth Layout
- Dashboard Layout
- Marketing Layout

예시:

```tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section>
      <nav>Dashboard Menu</nav>
      {children}
    </section>
  );
}
```

---

### [실무]

Layout 설계 기준:

- Root Layout에는 `html`, `body` 포함
- 공통 Header / Sidebar / Footer는 Layout에 배치
- 인증 영역과 비인증 영역은 Route Group으로 분리 가능
- Layout은 상태 유지 특성을 가질 수 있음
- Page는 Route별 데이터 조회와 화면 조립 담당
- 너무 많은 비즈니스 로직을 Layout에 넣지 않기

권장 구조:

```text
app
├ (public)
│  ├ layout.tsx
│  └ login
│     └ page.tsx
└ (protected)
   ├ layout.tsx
   └ dashboard
      └ page.tsx
```

---

### [FAQ]

Q. Header는 Page에 넣어야 하나 Layout에 넣어야 하나?

A.
여러 하위 페이지가 공유하면 Layout에 넣는 것이 좋다.

Q. 로그인 페이지와 대시보드 Layout을 다르게 하려면?

A.
Route Group을 사용해 `(public)`과 `(protected)`처럼 분리할 수 있다.

---

# 13. Loading / Error / Not Found Rules

## 13.1 Special UI Files

### [개념]

App Router는 파일 기반으로 Loading, Error, Not Found UI를 구성할 수 있다.

---

### [핵심]

필수 포함:

- `loading.tsx`
- `error.tsx`
- `global-error.tsx`
- `not-found.tsx`
- Suspense
- Error Boundary
- `notFound()`
- Retry
- Segment-level Error

예시:

```tsx
export default function Loading() {
  return <p>Loading...</p>;
}
```

예시:

```tsx
"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <p>{error.message}</p>
      <button onClick={reset}>Retry</button>
    </div>
  );
}
```

---

### [실무]

작성 기준:

- `loading.tsx`는 빠른 Skeleton UI 제공
- `error.tsx`는 Client Component로 작성
- `not-found.tsx`는 존재하지 않는 리소스 처리
- 데이터 없음과 404를 구분
- 민감한 에러 상세를 사용자에게 노출하지 않기
- 로그에는 원인 파악 정보 포함
- Retry 가능한 오류와 불가능한 오류 구분

---

### [FAQ]

Q. `error.tsx`에 `use client`가 필요한가?

A.
필요하다. Error Boundary는 Client Component로 동작한다.

Q. `loading.tsx`는 언제 보이나?

A.
Route Segment가 데이터를 기다리거나 Suspense 경계에서 대기할 때 표시된다.

Q. 데이터가 없으면 무조건 `notFound()`를 호출해야 하나?

A.
아니다. 실제로 존재하지 않는 리소스는 404 처리하고, 빈 목록은 Empty State UI로 처리한다.

---

# 14. Metadata and SEO Rules

## 14.1 Metadata API

### [개념]

Metadata API는 App Router에서 페이지의 title, description, Open Graph, Twitter Card, canonical URL 등을 설정하는 기능이다.

---

### [핵심]

필수 포함:

- Static Metadata
- Dynamic Metadata
- `metadata`
- `generateMetadata`
- Title Template
- Description
- Open Graph
- Twitter Card
- Canonical URL
- Robots
- Sitemap
- SEO

예시:

```tsx
export const metadata = {
  title: "Posts",
  description: "Post list page",
};
```

예시:

```tsx
export async function generateMetadata({
  params,
}: {
  params: Promise<{ postId: string }>;
}) {
  const { postId } = await params;
  const post = await getPost(postId);

  return {
    title: post.title,
    description: post.summary,
  };
}
```

---

### [실무]

Metadata 작성 기준:

- 정적 페이지는 `metadata`
- 상세 페이지는 `generateMetadata`
- 제목 / 설명 / OG 이미지 포함
- 동적 Metadata에서 불필요한 중복 API 호출 주의
- SEO가 중요한 페이지는 Server Component 중심 구성
- 인증 페이지 / 관리자 페이지는 robots 정책 검토

---

### [FAQ]

Q. 정적 Metadata와 동적 Metadata 차이는?

A.
정적 Metadata는 고정 값이고, 동적 Metadata는 params나 데이터 조회 결과에 따라 생성된다.

Q. 상세 페이지 SEO는 어떻게 처리하나?

A.
`generateMetadata`에서 상세 데이터를 조회해 title, description, Open Graph 정보를 구성한다.

---

# 15. Navigation Rules

## 15.1 Link / Redirect / Router

### [개념]

Next.js App Router의 Navigation은 `next/link`, `redirect`, `notFound`, Client Router Hook을 상황에 따라 사용한다.

---

### [핵심]

필수 포함:

- `Link`
- `redirect`
- `notFound`
- `useRouter`
- `usePathname`
- `useSearchParams`
- Search Params
- Dynamic Route Navigation
- Client Navigation
- Server Redirect

예시:

```tsx
import Link from "next/link";

export function PostLink({ postId }: { postId: string }) {
  return <Link href={`/posts/${postId}`}>Post Detail</Link>;
}
```

예시:

```tsx
import { redirect } from "next/navigation";

export default async function AdminPage() {
  const user = await getCurrentUser();

  if (!user) {
    redirect("/login");
  }

  return <main>Admin</main>;
}
```

---

### [실무]

Navigation 판단 기준:

| 상황                       | 사용                                  |
| -------------------------- | ------------------------------------- |
| 일반 링크                  | `Link`                                |
| 서버에서 인증 실패 후 이동 | `redirect`                            |
| 리소스 없음                | `notFound`                            |
| 버튼 클릭 후 이동          | `useRouter`                           |
| URL Query 읽기             | `searchParams` 또는 `useSearchParams` |
| 현재 경로 확인             | `usePathname`                         |

주의:

- Server Component에서는 Client Hook 사용 금지
- Client Hook이 필요하면 Client Component로 분리
- 인증 리다이렉트는 서버에서 처리 우선
- Query String은 검증 후 사용

---

### [FAQ]

Q. `redirect`는 어디서 사용하나?

A.
Server Component, Server Action, Route Handler 등 서버 실행 문맥에서 사용할 수 있다.

Q. `useRouter`는 Server Component에서 사용할 수 있나?

A.
사용할 수 없다. `useRouter`는 Client Component에서 사용한다.

---

# 16. Authentication and Authorization Rules

## 16.1 App Router 인증 흐름

### [개념]

App Router의 인증은 서버에서 사용자 상태를 검증하고, 보호된 Route 접근을 제한하는 구조로 작성한다.

---

### [핵심]

필수 포함:

- Authentication
- Authorization
- Protected Route
- Session
- Cookie
- JWT
- Server-side Auth Check
- Middleware / Proxy
- Role Check
- Redirect
- Unauthorized UI
- Token Exposure Prevention

기본 Flow:

```text
Request
→ Read Cookie / Session
→ Validate User
→ Check Role
→ Allow Page or Redirect
```

---

### [실무]

인증 문서 작성 기준:

- 보호 페이지는 Server Component에서 인증 확인
- 민감한 Token은 Client Component에 전달하지 않기
- Cookie는 HttpOnly / Secure / SameSite 고려
- Role 기반 접근 제어 포함
- Middleware / Proxy는 경량 검사용으로 사용
- DB 조회가 필요한 상세 권한은 서버 로직에서 처리
- Client UI 숨김은 보안이 아님
- Route Handler / Server Action에서도 인증 재검증

---

### [FAQ]

Q. Client에서 버튼을 숨기면 권한 처리가 된 건가?

A.
아니다. UI 숨김은 편의 기능일 뿐이고 실제 권한 검사는 서버에서 해야 한다.

Q. Server Action에서도 권한 검사를 해야 하나?

A.
해야 한다. Mutation은 항상 서버에서 인증과 권한을 다시 확인해야 한다.

Q. 보호 페이지 인증은 어디서 하는 게 좋은가?

A.
Server Component 또는 Layout에서 사용자 세션을 확인하고 실패 시 `redirect` 처리하는 방식이 좋다.

---

# 17. Form Handling Rules

## 17.1 Form / Server Action / Validation

### [개념]

App Router에서 Form은 Server Action과 결합해 Progressive Enhancement 방식으로 Mutation을 처리할 수 있다. Next.js의 `<Form>` 컴포넌트는 HTML form을 확장해 loading UI prefetch, client-side navigation, progressive enhancement를 제공한다.

---

### [핵심]

필수 포함:

- HTML Form
- `next/form`
- Server Action
- FormData
- Validation
- Error Message
- Pending State
- Optimistic UI
- Progressive Enhancement
- Redirect After Submit

예시:

```tsx
import { createPost } from "./actions";

export function PostForm() {
  return (
    <form action={createPost}>
      <input name="title" required />
      <button type="submit">Create</button>
    </form>
  );
}
```

---

### [실무]

Form 설계 기준:

- 간단한 Mutation은 Server Action 사용
- 복잡한 Client Interaction은 Client Component로 분리
- 서버에서 Validation 재수행
- 성공 후 `redirect` 또는 `revalidatePath`
- 실패 메시지는 구조화하여 반환
- Pending UI 제공
- 중복 제출 방지 고려
- 파일 업로드는 크기 제한과 보안 검증 포함

---

### [FAQ]

Q. Form Submit은 Client Component 없이 가능한가?

A.
가능하다. Server Action을 form action에 연결하면 기본 Form Submit 처리가 가능하다.

Q. Client Validation만 해도 되나?

A.
안 된다. Client Validation은 UX용이고 서버 Validation이 필수이다.

---

# 18. Environment Variable Rules

## 18.1 환경변수 관리

### [개념]

Next.js 환경변수는 서버 전용 값과 클라이언트 노출 값을 구분해야 한다.

---

### [핵심]

필수 포함:

- `.env.local`
- Server Environment Variable
- `NEXT_PUBLIC_`
- Secret
- API Key
- Build Time Variable
- Runtime Variable
- Deployment Environment

예시:

```ts
const apiKey = process.env.EXTERNAL_API_KEY;

if (!apiKey) {
  throw new Error("EXTERNAL_API_KEY is required");
}
```

---

### [실무]

환경변수 규칙:

- Secret은 `NEXT_PUBLIC_` prefix 사용 금지
- 브라우저에 노출해도 되는 값만 `NEXT_PUBLIC_` 사용
- `.env.local`은 Git에 올리지 않기
- 배포 환경 변수 별도 설정
- 누락된 필수 환경변수는 명확한 에러 발생
- 로그에 Secret 출력 금지
- Route Handler / Server Action / Server Component에서 서버 환경변수 사용

---

### [FAQ]

Q. `NEXT_PUBLIC_`은 무엇인가?

A.
브라우저 번들에 노출되는 환경변수 prefix이다. Secret에는 사용하면 안 된다.

Q. API Key를 Client Component에서 사용해도 되나?

A.
공개 가능한 Key가 아니라면 안 된다. Secret API Key는 서버에서만 사용해야 한다.

---

# 19. Security Rules

## 19.1 App Router 보안 기준

### [개념]

Next.js App Router 보안은 서버 / 클라이언트 경계, 인증 검증, 환경변수 보호, 입력 검증, Cache 정책을 함께 고려해야 한다.

---

### [핵심]

필수 포함:

- Server-only Secret
- Input Validation
- Output Escaping
- Authentication Check
- Authorization Check
- CSRF Consideration
- Server Action Origin
- Cookie Security
- XSS Prevention
- Cache Data Leak Prevention
- Dependency Security
- Error Message Sanitization

Server Actions 설정에는 허용 Origin과 Body Size Limit 같은 보안 옵션이 있다. Next.js는 Server Action 요청의 Origin과 Host를 비교하여 CSRF 방어에 활용한다.

---

### [실무]

보안 체크:

- Client 입력은 항상 서버에서 재검증
- Server Action / Route Handler에 권한 검증 추가
- 사용자별 데이터를 Static Cache하지 않기
- Secret을 Client Props로 전달하지 않기
- Error 상세를 사용자에게 노출하지 않기
- 파일 업로드 시 확장자 / MIME / 크기 검증
- 외부 URL Redirect 검증
- HTML 직접 삽입 시 XSS 검토
- Cookie 보안 옵션 적용
- API Rate Limit 고려

---

### [FAQ]

Q. Server Component면 무조건 안전한가?

A.
아니다. 서버에서 실행되지만 입력 검증, 권한 확인, Cache 정책을 잘못 설정하면 보안 문제가 생길 수 있다.

Q. Server Action은 보안 검사가 필요 없나?

A.
필요하다. Server Action은 서버에서 실행되지만 Client가 호출할 수 있으므로 인증, 권한, 입력 검증이 필수이다.

---

# 20. Performance Rules

## 20.1 App Router 성능 최적화

### [개념]

App Router 성능 최적화는 Server Component 활용, Client Bundle 최소화, Streaming, Caching, Image / Font Optimization을 중심으로 한다.

---

### [핵심]

필수 포함:

- Server Component First
- Client Bundle Reduction
- Streaming
- Suspense
- Loading UI
- Parallel Data Fetching
- Image Optimization
- Font Optimization
- Dynamic Import
- Bundle Analysis
- Cache Strategy
- Partial Rendering
- Route Segment Optimization

---

### [실무]

성능 기준:

- 상호작용 없는 UI는 Server Component 유지
- `use client` 범위 최소화
- 무거운 Client Library는 Dynamic Import 고려
- 이미지에는 `next/image` 사용 검토
- 폰트에는 Next Font 사용 검토
- 병렬 Fetch 가능한 요청은 병렬 처리
- 긴 요청은 Suspense / Streaming 고려
- 자주 변하지 않는 데이터는 Revalidation 고려
- 사용자별 데이터는 Cache 누수 주의
- Hydration Error 발생 시 Server / Client 출력 차이 확인

---

### [FAQ]

Q. App Router 성능 최적화의 첫 번째 원칙은?

A.
Server Component를 기본으로 사용하고 Client Component 범위를 최소화하는 것이다.

Q. Streaming은 왜 중요한가?

A.
느린 데이터가 있어도 가능한 UI를 먼저 보내 사용자 체감 속도를 높일 수 있기 때문이다.

---

# 21. Testing Rules

## 21.1 Next.js App Router 테스트 기준

### [개념]

Next.js App Router 테스트는 UI 컴포넌트, 서버 로직, Route Handler, Server Action, 인증 흐름을 분리해 검증한다.

---

### [핵심]

필수 포함:

- Unit Test
- Component Test
- Integration Test
- E2E Test
- Server Action Test
- Route Handler Test
- Mock API
- Auth Mock
- Error State Test
- Loading State Test

---

### [실무]

테스트 기준:

- 순수 함수는 Unit Test
- UI 컴포넌트는 Component Test
- Route Handler는 Request / Response 기준 테스트
- Server Action은 입력 / 권한 / 결과 / Revalidation 기준 검증
- 인증 페이지는 로그인 / 비로그인 / 권한 없음 케이스 검증
- Form은 성공 / 실패 / Validation Error 검증
- E2E는 핵심 사용자 Flow 중심
- 외부 API는 Mock 사용
- Snapshot 남용 금지

---

### [FAQ]

Q. App Router에서 무엇을 테스트해야 하나?

A.
Server Action, Route Handler, 인증 흐름, Form 제출, Error / Loading 상태, 핵심 사용자 Flow를 테스트해야 한다.

Q. 외부 API를 테스트마다 직접 호출해도 되나?

A.
권장하지 않는다. Mock을 사용해 테스트 안정성과 속도를 확보한다.

---

# 22. Troubleshooting Rules

## 22.1 자주 발생하는 문제

### [개념]

Troubleshooting 문서는 Agent가 오류 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Hydration Error
- `use client` 누락
- Server Component에서 Hook 사용
- Client Component에서 Server-only 코드 사용
- Fetch Cache 혼동
- Mutation 후 데이터 미갱신
- Dynamic Route params 오류
- Environment Variable undefined
- Route Handler Cache 문제
- Auth Redirect Loop
- Build Error
- Deployment Environment 차이

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

- Hydration Error 발생

원인:

- Server에서 렌더링한 HTML과 Client 렌더링 결과가 다름
- 날짜, 랜덤 값, 브라우저 API를 서버 렌더링 중 사용

해결:

- Client 전용 로직은 Client Component로 분리
- 렌더링 결과가 서버와 클라이언트에서 같도록 수정
- 필요 시 `useEffect` 이후 Client에서만 계산
```

---

### [FAQ]

Q. Hydration Error는 왜 발생하나?

A.
Server에서 만든 HTML과 Client가 Hydration할 때 만든 결과가 다를 때 발생한다.

Q. Mutation 후 데이터가 안 바뀌면 무엇을 봐야 하나?

A.
Cache 정책, `revalidatePath`, `revalidateTag`, Router Refresh 여부를 확인해야 한다.

---

# 23. Code Example Rules

## 23.1 코드 예제 작성 기준

### [개념]

Next.js App Router 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- 핵심 로직 중심
- 불필요한 import 최소화
- 긴 전체 파일 금지
- Server / Client 경계 명확히 표시
- App Router 경로 명시
- 보안 위험 예제 금지
- API Key 하드코딩 금지
- Error Handling 포함 권장
- Validation 포함 권장

---

### [실무]

권장 예제 유형:

- Server Component Data Fetching
- Client Component Interaction
- Server Action Mutation
- Route Handler GET / POST
- Protected Page Redirect
- Dynamic Metadata
- Loading / Error UI
- Revalidation
- Environment Variable Check

금지 예제:

- `use client`를 Page 전체에 무분별하게 붙이는 예제
- Secret을 Client에 전달하는 예제
- Timeout / Error Handling 없는 외부 API 예제
- 인증 없는 Mutation 예제
- Cache 정책이 불명확한 사용자별 데이터 예제

---

### [FAQ]

Q. 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. JavaScript 예제도 허용되나?

A.
가능하지만 TypeScript 예제를 우선한다.

---

# 24. Comparison Rules

## 24.1 필수 비교 대상

### [개념]

Next.js App Router 문서는 Agent의 구조 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- App Router vs Pages Router
- Server Component vs Client Component
- Server Action vs Route Handler
- Server Action vs Client Fetch
- Static Rendering vs Dynamic Rendering
- Revalidate vs No Store
- Layout vs Template
- Page vs Route Handler
- Middleware / Proxy vs Server-side Auth Check
- `metadata` vs `generateMetadata`
- Route Group vs Dynamic Route
- Loading UI vs Skeleton Component
- Client Validation vs Server Validation

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 실행 위치 / 사용 목적 / 보안 / 성능 / 예시로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Server Action과 Route Handler 중 무엇을 써야 하나?

A.
Form Mutation처럼 앱 내부 UI에서 호출하면 Server Action을 우선 고려하고, 외부 클라이언트나 Webhook처럼 HTTP API가 필요하면 Route Handler를 사용한다.

Q. Static Rendering과 Dynamic Rendering은 어떻게 구분하나?

A.
데이터가 고정적이면 Static, 사용자별이거나 요청마다 달라지면 Dynamic을 고려한다.

---

# 25. Checklist Rules

## 25.1 문서 품질 체크리스트

### [개념]

Next.js App Router RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] App Router 기준으로 작성했는가?
- [ ] Pages Router 중심 설명을 피했는가?
- [ ] Server Component 기본 원칙을 포함했는가?
- [ ] Client Component 사용 기준을 포함했는가?
- [ ] `use client` 남용 주의를 포함했는가?
- [ ] Data Fetching 위치 판단 기준을 포함했는가?
- [ ] Caching / Revalidation 기준을 포함했는가?
- [ ] Server Actions / Server Functions를 포함했는가?
- [ ] Route Handler 사용 기준을 포함했는가?
- [ ] Layout / Page 구조를 포함했는가?
- [ ] Loading / Error / Not Found 처리를 포함했는가?
- [ ] Metadata / SEO 기준을 포함했는가?
- [ ] 인증 / 권한 / 보안 기준을 포함했는가?
- [ ] 환경변수 보안 기준을 포함했는가?
- [ ] Performance 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성

---

### [FAQ]

Q. Next.js App Router 문서 품질에서 가장 중요한 것은?

A.
Server / Client 경계, Data Fetching 위치, Cache 전략, Mutation 처리 기준이 명확해야 한다.

---

# 26. Retrieval Optimization Rules

## 26.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Next.js
- Next.js App Router
- App Router
- File-System Routing
- app directory
- Route Segment
- Server Component
- Client Component
- React Server Components
- `use client`
- Server Function
- Server Action
- Mutating Data
- Route Handler
- `route.ts`
- Data Fetching
- Fetch Cache
- Revalidation
- `revalidatePath`
- `revalidateTag`
- Static Rendering
- Dynamic Rendering
- Streaming
- Suspense
- Layout
- Page
- Loading UI
- Error Boundary
- Not Found
- Metadata API
- `generateMetadata`
- Authentication
- Protected Route
- Environment Variable
- `NEXT_PUBLIC_`
- Hydration Error
- Frontend Performance
- Frontend Security

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Next.js App Router 구조 어떻게 잡아?
- Server Component와 Client Component 차이는?
- `use client` 언제 붙여?
- App Router에서 fetch 어디서 해?
- Server Action은 언제 써?
- Route Handler는 언제 써?
- Mutation 후 데이터 갱신 어떻게 해?
- Next.js Cache 때문에 데이터가 안 바뀌어
- 로그인 필요한 페이지는 어떻게 보호해?
- 환경변수는 어떻게 관리해?
- Hydration Error 왜 나?
- `loading.tsx`와 `error.tsx`는 어떻게 써?
- `generateMetadata`는 언제 써?
- App Router에서 API Route는 어떻게 만들어?
- Server Action과 Route Handler 차이는?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 27. Version Rules

## 27.1 기준 버전

### [개념]

Next.js App Router 문서는 Modern Next.js 기준으로 작성하며, 버전 변화 가능성을 명확히 기록한다.

---

### [핵심]

기준:

- Next.js App Router
- React Server Components
- React 19 Compatibility
- TypeScript
- Node.js Modern Runtime
- App Directory
- Server Actions / Server Functions
- Route Handlers
- Metadata API
- Cache Components / Revalidation
- Modern Deployment Platform

Legacy 제외:

- Pages Router 중심 설계
- `getServerSideProps`
- `getStaticProps`
- `getStaticPaths`
- `pages/api` 중심 구조
- `_app.tsx`
- `_document.tsx`
- Class Component 중심 설명
- jQuery 기반 UI
- Secret 하드코딩

---

### [실무]

문서 작성 시 주의:

- Next.js는 버전별 Cache / Server Action / Runtime 동작이 바뀔 수 있음
- 코드 예제에는 App Router 기준 경로를 표시
- 최신 문서 기준이 필요한 항목은 공식 문서 확인 필요
- Experimental 기능은 명확히 표시
- 안정 기능과 실험 기능을 혼동하지 않기

---

### [FAQ]

Q. `getServerSideProps`를 App Router 문서에 넣어도 되나?

A.
기본적으로 넣지 않는다. Pages Router와 비교하거나 마이그레이션 문맥에서만 언급한다.

Q. App Router 문서는 최신성을 신경 써야 하나?

A.
그렇다. Next.js는 App Router, Cache, Server Actions 관련 동작이 변경될 수 있으므로 기준 버전을 명시해야 한다.

---

# 28. Common Mistakes

## 28.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 코드 리뷰와 오류 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Page 전체에 `use client` 선언
- Server Component에서 `useState` 사용
- Client Component에서 서버 전용 함수 import
- Secret을 `NEXT_PUBLIC_`으로 선언
- 사용자별 데이터를 Static Cache
- Mutation 후 Revalidation 누락
- Route Handler와 Server Action 역할 혼동
- Server Component에서 브라우저 API 사용
- Error Boundary에 `use client` 누락
- Dynamic Route params 타입 처리 누락
- 인증 검사를 Client UI에만 의존
- Form Validation을 Client에서만 수행
- Hydration Error 원인 무시
- `loading.tsx` 없이 느린 페이지 구성
- Metadata 누락
- 외부 API Timeout / Error Handling 누락
- 환경변수 배포 설정 누락
- App Router와 Pages Router 패턴 혼용

---

### [실무]

리뷰 기준:

- `use client` 범위 확인
- Server / Client import 방향 확인
- Cache 정책 확인
- 인증 / 권한 서버 검증 확인
- Mutation 후 Revalidation 확인
- Route Handler가 필요한 상황인지 확인
- Error / Loading / Empty State 확인
- 환경변수 노출 여부 확인
- Metadata / SEO 확인
- Bundle 증가 요인 확인

---

### [FAQ]

Q. App Router에서 가장 흔한 실수는?

A.
`use client`를 과도하게 사용하거나 Server Component와 Client Component의 역할을 혼동하는 것이다.

Q. Cache 관련 실수는 왜 위험한가?

A.
오래된 데이터 표시뿐 아니라 사용자별 민감 데이터가 잘못 캐시될 위험이 있기 때문이다.

---

# 29. Final Goal

## 29.1 최종 목표

### [개념]

Next.js App Router RAG 문서는 Agent가 App Router 기반 프론트엔드와 풀스택 기능을 설계, 생성, 검토, 수정할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- App Router 폴더 구조 설계
- Layout / Page 구성
- Server Component / Client Component 경계 판단
- `use client` 위치 결정
- Server Component Data Fetching 코드 생성
- Server Action Mutation 코드 생성
- Route Handler API 코드 생성
- Cache / Revalidation 전략 선택
- Loading / Error / Not Found UI 구성
- Metadata / SEO 구성
- Protected Route 구현
- Environment Variable 보안 검토
- Hydration Error 원인 진단
- Performance 개선 제안
- Security Review 수행
- App Router 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Server / Client 경계 명확화
- Cache / Auth / Security 위험 명시
- Retrieval Queries 포함

---

### [FAQ]

Q. Next.js App Router Domain Rules의 최종 목적은?

A.
Agent가 App Router 기반 프로젝트에서 구조 설계, 코드 생성, 데이터 패칭, 캐싱, 인증, 보안, 성능 리뷰를 수행하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Next.js App Router 문서는 어떤 기준으로 작성해야 해?

A.
App Router, Server Component, Client Component, Data Fetching, Cache, Server Action, Route Handler 중심으로 작성해야 한다.

Q. Next.js App Router 구조는 어떻게 잡아?

A.
`app` 디렉터리 아래 Route Segment를 만들고 `layout.tsx`, `page.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`, `route.ts`를 역할에 맞게 배치한다.

Q. Server Component와 Client Component 차이는?

A.
Server Component는 서버에서 실행되고 데이터 조회와 보안에 유리하다. Client Component는 브라우저에서 실행되고 상태, 이벤트, Browser API가 필요할 때 사용한다.

Q. `use client`는 언제 붙여?

A.
`useState`, `useEffect`, 이벤트 핸들러, Browser API, Client-only Library가 필요한 가장 작은 컴포넌트에 붙인다.

Q. App Router에서 fetch는 어디서 하는 게 좋아?

A.
초기 렌더링 데이터는 Server Component에서 처리하는 것이 기본이다. 사용자 이벤트 기반 조회는 Client Component나 Server Action을 고려한다.

Q. Server Action은 언제 사용해?

A.
Form Submit, Create, Update, Delete, Like, Bookmark 같은 Mutation 작업에 사용한다.

Q. Route Handler는 언제 사용해?

A.
Webhook, API Proxy, 외부 클라이언트 API, 파일 응답처럼 HTTP 엔드포인트가 필요한 경우 사용한다.

Q. Server Action과 Route Handler 차이는?

A.
Server Action은 앱 내부 UI의 Mutation 처리에 적합하고, Route Handler는 외부 HTTP 요청을 처리하는 API 엔드포인트에 적합하다.

Q. Mutation 후 데이터가 갱신되지 않으면?

A.
`revalidatePath`, `revalidateTag`, Router Refresh, Fetch Cache 정책을 확인해야 한다.

Q. Next.js Cache 때문에 데이터가 안 바뀌는 이유는?

A.
Static Rendering, Fetch Cache, Revalidation 설정 때문에 이전 데이터가 유지될 수 있다. 데이터 성격에 맞게 `revalidate` 또는 `no-store`를 설정해야 한다.

Q. 로그인 사용자 정보는 Cache해도 돼?

A.
주의해야 한다. 사용자별 민감 데이터는 `no-store` 또는 Dynamic Rendering을 고려한다.

Q. App Router에서 보호 페이지는 어떻게 만들어?

A.
Server Component 또는 Layout에서 세션을 확인하고 인증 실패 시 `redirect("/login")` 처리한다.

Q. 권한 검사는 Client에서 버튼 숨기면 충분해?

A.
아니다. Client UI 숨김은 UX일 뿐이고 실제 권한 검사는 Server Action, Route Handler, Server Component에서 수행해야 한다.

Q. 환경변수는 어떻게 관리해?

A.
Secret은 서버 환경변수로 관리하고, 브라우저에 노출 가능한 값만 `NEXT_PUBLIC_` prefix를 사용한다.

Q. `NEXT_PUBLIC_`은 언제 써?

A.
브라우저에 노출되어도 되는 공개 설정값에만 사용한다. Secret API Key에는 사용하지 않는다.

Q. Hydration Error는 왜 발생해?

A.
Server에서 렌더링한 결과와 Client에서 Hydration할 때의 결과가 다를 때 발생한다.

Q. `loading.tsx`는 언제 써?

A.
Route Segment의 데이터 로딩 중 사용자에게 Skeleton 또는 Loading UI를 보여줄 때 사용한다.

Q. `error.tsx`는 어떻게 작성해?

A.
`use client`를 선언하고 Error Boundary UI와 reset 동작을 제공한다.

Q. `not-found.tsx`는 언제 써?

A.
존재하지 않는 리소스나 잘못된 Dynamic Route 접근을 404 UI로 처리할 때 사용한다.

Q. `generateMetadata`는 언제 써?

A.
게시글 상세, 상품 상세처럼 params나 데이터 조회 결과에 따라 title, description, Open Graph를 동적으로 만들 때 사용한다.

Q. App Router에서 API Route는 어떻게 만들어?

A.
`app/api/.../route.ts` 파일을 만들고 `GET`, `POST`, `PUT`, `PATCH`, `DELETE` 같은 HTTP Method 함수를 export한다.

Q. Server Component에서 `useRouter`를 쓸 수 있어?

A.
사용할 수 없다. `useRouter`는 Client Component에서 사용한다.

Q. Server Component에서 DB나 Backend API를 직접 호출해도 돼?

A.
가능하다. 단, 인증, 권한, 에러 처리, Cache 정책을 명확히 해야 한다.

Q. Page 전체를 Client Component로 만들면 안 돼?

A.
가능은 하지만 권장하지 않는다. Client Bundle 증가, Hydration 비용 증가, Server Component 장점 감소 문제가 생긴다.

Q. App Router 문서에서 가장 중요한 리뷰 포인트는?

A.
Server / Client 경계, Data Fetching 위치, Cache 정책, Mutation 후 Revalidation, 인증 / 권한 서버 검증이다.

Q. Next.js App Router RAG 문서 최종 목표는?

A.
Agent가 App Router 기반 구조 설계, 코드 생성, 데이터 패칭, 캐싱, 인증, 보안, 성능 리뷰를 수행하게 만드는 것이다.

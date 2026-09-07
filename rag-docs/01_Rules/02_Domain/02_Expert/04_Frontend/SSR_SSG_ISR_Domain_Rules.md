# SSR / SSG / ISR Domain Rules

---

# 1. Domain Purpose

## 1.1 SSR / SSG / ISR Domain 목적

### [개념]

SSR / SSG / ISR Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent용 RAG 문서 제작 규칙이다.

SSR, SSG, ISR은 웹 페이지를 언제, 어디서, 어떤 주기로 렌더링하고 캐시할지 결정하는 Rendering Strategy이다.

Next.js App Router 기준에서는 전통적인 Pages Router 용어인 SSR / SSG / ISR을 그대로 외우기보다 아래 개념으로 연결해 이해해야 한다.

- SSR → Dynamic Rendering / Request-time Rendering
- SSG → Static Rendering / Prerendering
- ISR → Revalidation / Incremental Static Regeneration
- Streaming → Suspense 기반 Progressive Rendering
- PPR → Static Shell + Dynamic Content 조합

Next.js App Router는 Server Components를 기반으로 Static, Dynamic, Streaming Rendering 전략을 제공한다. Static Rendering은 빌드 시점 또는 revalidation 이후 결과를 캐시할 수 있고, Dynamic Rendering은 요청 시점에 렌더링한다.

---

### [핵심]

우선순위:

1. Rendering Strategy 선택 기준
2. SSR / SSG / ISR 개념 구분
3. App Router Rendering 모델 이해
4. Static Rendering 판단
5. Dynamic Rendering 판단
6. Revalidation / ISR 판단
7. Cache Strategy 판단
8. Data Freshness 요구사항 분석
9. SEO / Performance / Personalization 균형
10. Server Component / Client Component 경계
11. Streaming / Suspense 활용
12. Dynamic Route / `generateStaticParams`
13. On-demand Revalidation
14. Hosting / Runtime 제약
15. Rendering Strategy 코드 리뷰 기준

---

### [실무]

2026 실무 기준:

- Next.js App Router 기준으로 작성
- Pages Router의 `getServerSideProps`, `getStaticProps`, `getStaticPaths` 중심 설명 금지
- SSR / SSG / ISR 용어는 App Router의 Dynamic Rendering / Static Rendering / Revalidation과 연결
- Server Component 기본 전제
- Client Component는 rendering strategy 결정의 핵심이 아니라 hydration cost 판단 요소로 설명
- 사용자별 데이터는 Dynamic Rendering 또는 private / no-store cache로 판단
- 자주 바뀌지 않는 공개 콘텐츠는 Static Rendering 또는 Revalidation 검토
- CMS / 블로그 / 상품 상세는 ISR / Revalidation 후보
- 관리자 통계 / 로그인 사용자 대시보드는 Dynamic Rendering 후보
- `generateStaticParams`, `revalidate`, `revalidatePath`, `revalidateTag` 사용 기준 포함
- Next.js 버전별 Cache 정책 변화 가능성을 명시
- Agent가 페이지별 Rendering Strategy를 선택하고 코드 리뷰할 수 있도록 판단 기준 중심으로 작성

Next.js ISR은 전체 사이트를 다시 빌드하지 않고 정적 콘텐츠를 업데이트하고, 대부분 요청에 prerendered static page를 제공하여 서버 부하를 줄이는 방식이다.

---

### [FAQ]

Q. SSR / SSG / ISR 문서는 무엇을 위한 문서인가?

A.
Agent가 Next.js App Router 기반 프로젝트에서 페이지별 Rendering Strategy, Cache, Revalidation, SEO, 성능, 데이터 신선도 기준을 판단하도록 돕는 RAG 문서 제작 규칙이다.

Q. SSR / SSG / ISR은 Pages Router 용어 아닌가?

A.
전통적으로 Pages Router에서 많이 사용된 용어지만, App Router에서도 Dynamic Rendering, Static Rendering, Revalidation 개념으로 연결해 판단해야 한다.

Q. App Router에서는 무엇을 기준으로 작성해야 하나?

A.
`app` directory, Server Component, Static Rendering, Dynamic Rendering, Revalidation, Streaming, Cache 정책을 기준으로 작성해야 한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

SSR / SSG / ISR Domain은 Next.js Rendering Strategy와 Cache / Revalidation 판단에 필요한 주제를 포함한다.

---

### [핵심]

포함 범위:

- SSR
- SSG
- ISR
- Static Rendering
- Dynamic Rendering
- Streaming
- Server Component
- Client Component
- React Server Components
- App Router
- Pages Router Comparison
- Prerendering
- Request-time Rendering
- Build-time Rendering
- Revalidation
- Time-based Revalidation
- On-demand Revalidation
- `revalidate`
- `revalidatePath`
- `revalidateTag`
- `generateStaticParams`
- Dynamic Route
- Static Route
- Cache
- Fetch Cache
- Data Cache
- Full Route Cache
- Router Cache
- Cache Key
- Cache Invalidation
- `no-store`
- `force-dynamic`
- `force-static`
- `dynamicParams`
- SEO
- TTFB
- LCP
- CDN Cache
- Personalized Data
- Public Data
- Private Data
- CMS Content
- Product Page
- Blog Page
- Dashboard Page
- Admin Page
- Search Page
- Partial Prerendering
- Edge Runtime 제약
- Hosting Platform 제약

---

### [실무]

제외 범위:

- Pages Router 심화 구현
- `getServerSideProps` 상세 패턴
- `getStaticProps` 상세 패턴
- `getStaticPaths` 상세 패턴
- Backend Cache 심화
- CDN 운영 심화
- Database Cache 심화
- React 기초 문법 전체
- Next.js App Router 전체 기능 설명
- Server Component 내부 구현 심화
- Infra / Kubernetes 배포 심화

단, Rendering Strategy 판단에 필요한 수준의 Cache, SEO, Performance, Hosting, Data Fetching 지식은 포함 가능하다.

---

### [FAQ]

Q. Pages Router 방식도 포함해야 하나?

A.
상세 구현은 제외한다. SSR / SSG / ISR 용어 비교와 마이그레이션 이해에 필요한 정도만 포함한다.

Q. Cache 문서와 중복되지 않나?

A.
이 Domain은 Cache 자체보다 Rendering Strategy 선택과 Revalidation 판단에 집중한다.

Q. Performance Tuning 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 Domain은 SSR / SSG / ISR 선택이 성능에 주는 영향을 중심으로 다룬다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 SSR / SSG / ISR RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

SSR / SSG / ISR 문서는 선택 기준과 판단 흐름이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Request → Rendering Strategy → Cache → Response → Revalidation
- `[Comparison]`: SSR vs SSG vs ISR
- `[Best Practice]`: 공개 콘텐츠 Static / 사용자별 콘텐츠 Dynamic
- `[Troubleshooting]`: 데이터가 안 바뀜, 빌드 시간이 김, Cache 누수
- `[Checklist]`: 페이지별 Rendering Strategy 검수

---

### [FAQ]

Q. SSR / SSG / ISR 문서에 Comparison이 필요한 이유는?

A.
같은 페이지도 데이터 신선도, SEO, 사용자별 여부, 빌드 시간, 성능 요구에 따라 전략이 달라지므로 비교 기준이 필요하다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Rendering Strategy Core Rules

## 4.1 Rendering Strategy 기본 개념

### [개념]

Rendering Strategy는 HTML과 데이터가 생성되는 시점과 캐시되는 방식을 결정한다.

핵심 질문:

- 페이지가 모든 사용자에게 같은가?
- 데이터가 얼마나 자주 바뀌는가?
- SEO가 중요한가?
- 요청마다 최신 데이터가 필요한가?
- 로그인 사용자별 데이터인가?
- 빌드 시점에 경로를 알 수 있는가?
- 캐시해도 안전한가?

---

### [핵심]

전략 요약:

| 전략                    | 생성 시점                          | 캐시             | 적합한 데이터                  |
| ----------------------- | ---------------------------------- | ---------------- | ------------------------------ |
| SSR / Dynamic Rendering | 요청 시점                          | 제한적 또는 없음 | 사용자별 / 실시간 데이터       |
| SSG / Static Rendering  | 빌드 시점 또는 사전 생성           | 높음             | 변경 적은 공개 콘텐츠          |
| ISR / Revalidation      | 정적 생성 후 주기적 또는 수동 갱신 | 높음             | 주기적으로 바뀌는 공개 콘텐츠  |
| Streaming               | 서버 렌더링 중 점진 전송           | 조합 가능        | 느린 일부 데이터 포함 페이지   |
| PPR                     | Static Shell + Dynamic Slot        | 조합 가능        | 정적 레이아웃 + 동적 일부 영역 |

---

### [실무]

판단 Flow:

```text
페이지가 사용자별 데이터인가?
→ Yes: Dynamic Rendering / no-store 검토

공개 콘텐츠이고 자주 안 바뀌는가?
→ Yes: Static Rendering 검토

공개 콘텐츠이지만 주기적으로 바뀌는가?
→ Yes: ISR / Revalidation 검토

일부 데이터만 느리거나 동적인가?
→ Streaming / Suspense / PPR 검토

검색 / 필터처럼 요청마다 조건이 달라지는가?
→ Dynamic Rendering 또는 Client-side Query 검토
```

---

### [FAQ]

Q. Rendering Strategy 선택에서 가장 먼저 봐야 하는 것은?

A.
데이터가 사용자별인지, 공개 데이터인지, 얼마나 자주 바뀌는지 먼저 봐야 한다.

Q. SEO가 중요하면 항상 SSG인가?

A.
아니다. SEO가 중요해도 데이터가 요청마다 달라지면 SSR / Dynamic Rendering이 필요할 수 있다.

Q. 성능만 보면 SSG가 항상 좋은가?

A.
대부분 빠르지만 데이터 신선도, 빌드 시간, 경로 수, 개인화 요구를 함께 고려해야 한다.

---

# 5. SSR Rules

## 5.1 SSR / Dynamic Rendering

### [개념]

SSR은 요청이 들어올 때마다 서버에서 HTML을 생성하는 방식이다.

Next.js Pages Router에서는 SSR을 `getServerSideProps`로 구현했지만, App Router에서는 Dynamic Rendering과 Server Component의 요청 시점 데이터 접근으로 이해하는 것이 적합하다.

공식 문서 기준 Pages Router SSR은 page HTML이 각 요청마다 생성되는 방식이며 Dynamic Rendering이라고도 부른다.

---

### [핵심]

SSR / Dynamic Rendering 적합 상황:

- 로그인 사용자별 페이지
- 개인화된 대시보드
- 관리자 통계
- 권한별 콘텐츠
- 실시간성이 중요한 데이터
- 요청 헤더 / 쿠키 / 세션 기반 렌더링
- 검색 조건이 요청마다 다른 페이지
- 캐시하면 위험한 민감 데이터
- A/B Test 또는 Geo 기반 응답
- 결제 / 주문 / 마이페이지

---

### [실무]

App Router 기준 Dynamic Rendering 후보:

```tsx
export default async function DashboardPage() {
  const user = await getCurrentUser();
  const dashboard = await getUserDashboard(user.id);

  return <DashboardView dashboard={dashboard} />;
}
```

Dynamic Rendering 판단 기준:

- `cookies`, `headers`, 세션 정보를 사용
- 사용자별 DB 조회
- 인증 / 권한 검사 필요
- 요청마다 결과가 달라짐
- public cache 불가
- 최신성이 매우 중요
- 데이터 누수 위험이 있음

주의:

- SSR은 요청마다 서버 작업이 발생해 서버 부하가 증가할 수 있음
- TTFB가 SSG보다 느릴 수 있음
- Cache 전략 없이 모든 요청을 SSR로 처리하면 비용 증가
- 사용자별 데이터를 Static Cache에 저장하면 보안 문제 발생
- SSR이 필요 없는 공개 콘텐츠까지 Dynamic으로 만들지 않기

---

### [FAQ]

Q. SSR은 언제 사용하나?

A.
사용자별 데이터, 요청마다 달라지는 데이터, 인증 / 권한이 필요한 페이지, 실시간성이 중요한 페이지에 사용한다.

Q. SSR은 SEO에 좋은가?

A.
서버에서 HTML을 생성하므로 SEO에 유리할 수 있다. 다만 요청마다 렌더링하므로 서버 응답 시간도 함께 관리해야 한다.

Q. SSR의 단점은?

A.
요청마다 서버 렌더링 비용이 발생하고 TTFB가 느려질 수 있다.

---

# 6. SSG Rules

## 6.1 SSG / Static Rendering

### [개념]

SSG는 페이지 HTML을 빌드 시점에 생성하고 요청 시 재사용하는 방식이다.

Next.js Pages Router 문서 기준 Static Generation은 production에서 `next build` 시 HTML을 생성하고, 이 HTML을 각 요청에서 재사용하며 CDN에 캐시할 수 있다.

App Router에서는 Static Rendering이 기본 최적화 전략 중 하나이며, 정적 결과를 캐시하고 여러 사용자 요청에서 공유할 수 있다.

---

### [핵심]

SSG / Static Rendering 적합 상황:

- 블로그 목록
- 문서 페이지
- 마케팅 페이지
- 랜딩 페이지
- 회사 소개
- 제품 소개
- FAQ 페이지
- 가격 정책 페이지
- 변경이 적은 공개 콘텐츠
- SEO가 중요하고 데이터가 자주 바뀌지 않는 페이지
- CDN 캐시 효과가 큰 페이지

---

### [실무]

Static Rendering 후보:

```tsx
export default async function BlogPage() {
  const posts = await getPublishedPosts();

  return <BlogList posts={posts} />;
}
```

Static Rendering 판단 기준:

- 모든 사용자에게 같은 HTML 제공 가능
- 데이터 변경 빈도가 낮음
- 요청마다 최신 데이터가 필요하지 않음
- 사용자별 권한 / 세션에 의존하지 않음
- SEO 중요
- CDN 캐시 가능
- 경로 수가 과도하지 않음

주의:

- 데이터가 자주 바뀌면 오래된 콘텐츠가 보일 수 있음
- 경로 수가 많으면 build time 증가
- 빌드 시점에 데이터를 가져올 수 있어야 함
- 사용자별 데이터 포함 금지
- 정적 페이지에서 동적 API를 사용하면 Dynamic Rendering으로 전환될 수 있음

---

### [FAQ]

Q. SSG는 언제 사용하나?

A.
모든 사용자에게 같은 공개 콘텐츠를 제공하고 데이터 변경이 적으며 SEO가 중요한 페이지에 사용한다.

Q. SSG의 장점은?

A.
CDN 캐시가 가능하고 요청 시 서버 렌더링 비용이 낮아 빠른 응답을 제공할 수 있다.

Q. SSG의 단점은?

A.
콘텐츠 변경 시 재빌드나 revalidation이 필요하고, 경로 수가 많으면 빌드 시간이 길어질 수 있다.

---

# 7. ISR Rules

## 7.1 ISR / Revalidation

### [개념]

ISR은 정적으로 생성된 페이지나 데이터를 전체 재빌드 없이 일정 시간 또는 특정 이벤트 이후 다시 생성하는 방식이다.

App Router에서는 `next.revalidate`, `revalidatePath`, `revalidateTag`를 통해 시간 기반 또는 이벤트 기반 revalidation을 구성할 수 있다.

Next.js 공식 ISR 가이드는 ISR이 전체 사이트 rebuild 없이 정적 콘텐츠를 업데이트하고, 대부분 요청에 prerendered static page를 제공하며, 대량 콘텐츠 페이지의 build time 문제를 완화할 수 있다고 설명한다.

---

### [핵심]

ISR / Revalidation 적합 상황:

- CMS 기반 블로그
- 뉴스 / 공지사항
- 상품 상세
- 카테고리 목록
- 이벤트 상세
- 축제 상세
- 문서 사이트
- 가격 정보가 주기적으로 바뀌는 공개 페이지
- SEO 중요 + 데이터가 가끔 바뀜
- 경로 수가 많아 전체 빌드가 부담됨
- CMS Webhook으로 갱신 필요

---

### [실무]

시간 기반 Revalidation 예시:

```tsx
export const revalidate = 3600;

export default async function PostPage() {
  const post = await getPost();

  return <PostView post={post} />;
}
```

Fetch 단위 Revalidation 예시:

```tsx
async function getPosts() {
  const response = await fetch("https://api.example.com/posts", {
    next: { revalidate: 60 },
  });

  return response.json();
}
```

On-demand Revalidation 예시:

```ts
import { revalidatePath } from "next/cache";

export async function POST() {
  revalidatePath("/posts");

  return Response.json({ revalidated: true });
}
```

판단 기준:

- 공개 데이터
- SEO 중요
- 최신성은 필요하지만 초 단위 실시간은 아님
- 일정 주기 갱신 가능
- CMS / 관리자 변경 이벤트로 갱신 가능
- 서버 부하를 줄이고 싶음
- 전체 rebuild는 부담됨

주의:

- Revalidation 주기를 너무 길게 잡으면 오래된 데이터 표시
- 너무 짧게 잡으면 서버 부하 증가
- 사용자별 데이터에는 부적합
- Mutation 후 `revalidatePath` / `revalidateTag` 누락 시 화면이 갱신되지 않을 수 있음
- On-demand Revalidation endpoint는 인증 / 서명 검증 필요
- `revalidatePath`는 지정 경로의 다음 방문 시 갱신되는 동작을 고려해야 한다.

---

### [FAQ]

Q. ISR은 언제 사용하나?

A.
SEO가 중요하고 공개 콘텐츠이며 데이터가 가끔 바뀌는 페이지에 사용한다.

Q. ISR과 SSG 차이는?

A.
SSG는 빌드 시 생성 후 고정에 가깝고, ISR은 정적 생성 결과를 일정 시간이나 이벤트 이후 갱신할 수 있다.

Q. ISR은 사용자별 데이터에 사용해도 되나?

A.
권장하지 않는다. 사용자별 민감 데이터는 Dynamic Rendering 또는 private cache를 고려해야 한다.

---

# 8. App Router Mapping Rules

## 8.1 SSR / SSG / ISR과 App Router 매핑

### [개념]

App Router에서는 Pages Router의 SSR / SSG / ISR 함수를 그대로 쓰지 않는다.

대신 Server Component, `fetch` cache option, route segment config, `generateStaticParams`, `revalidatePath`, `revalidateTag` 등을 조합해 Rendering Strategy를 구성한다.

---

### [핵심]

매핑 기준:

| 전통 용어        | Pages Router         | App Router 기준                                 |
| ---------------- | -------------------- | ----------------------------------------------- |
| SSR              | `getServerSideProps` | Dynamic Rendering                               |
| SSG              | `getStaticProps`     | Static Rendering                                |
| Dynamic SSG Path | `getStaticPaths`     | `generateStaticParams`                          |
| ISR              | `revalidate` option  | `revalidate`, `revalidatePath`, `revalidateTag` |
| API Routes       | `pages/api`          | Route Handlers                                  |
| Loading          | 직접 구현            | `loading.tsx`, Suspense                         |
| Streaming        | 제한적               | App Router 기본 패턴                            |

---

### [실무]

App Router 문서 작성 기준:

- `getServerSideProps` 예제 중심 금지
- `getStaticProps` 예제 중심 금지
- `getStaticPaths` 대신 `generateStaticParams` 설명
- SSR은 Dynamic Rendering으로 연결
- SSG는 Static Rendering으로 연결
- ISR은 Revalidation으로 연결
- Route Segment Config는 필요 시 포함
- Cache 동작은 Next.js 버전별 차이를 명시

Next.js 공식 문서는 App Router가 Server Components 같은 React 신규 기능을 지원하는 새로운 Router이고, Pages Router도 여전히 지원된다고 구분한다.

---

### [FAQ]

Q. App Router에서 `getServerSideProps`를 쓰나?

A.
아니다. App Router에서는 Server Component와 Dynamic Rendering 개념으로 처리한다.

Q. App Router에서 `getStaticProps`를 쓰나?

A.
아니다. Static Rendering, `fetch` cache option, `revalidate`, `generateStaticParams`를 사용한다.

Q. App Router에서 ISR은 어떻게 구현하나?

A.
`revalidate`, `fetch`의 `next.revalidate`, `revalidatePath`, `revalidateTag`를 사용한다.

---

# 9. Rendering Strategy Decision Rules

## 9.1 페이지별 전략 선택

### [개념]

Rendering Strategy Decision은 페이지의 데이터 성격, 사용자별 여부, SEO, 성능, 신선도 요구를 기준으로 SSR / SSG / ISR / Streaming을 선택하는 규칙이다.

---

### [핵심]

선택 기준:

| 페이지 유형      | 권장 전략                         |
| ---------------- | --------------------------------- |
| 랜딩 페이지      | SSG / Static                      |
| 블로그 목록      | SSG 또는 ISR                      |
| 블로그 상세      | SSG 또는 ISR                      |
| CMS 문서         | ISR                               |
| 상품 목록        | ISR 또는 Dynamic                  |
| 상품 상세        | ISR                               |
| 검색 결과        | Dynamic 또는 Client Fetch         |
| 로그인 페이지    | Static 가능                       |
| 마이페이지       | SSR / Dynamic                     |
| 관리자 대시보드  | SSR / Dynamic                     |
| 실시간 알림      | Dynamic / Client Fetch            |
| 결제 페이지      | Dynamic                           |
| 권한별 콘텐츠    | Dynamic                           |
| 대량 상세 페이지 | ISR + `generateStaticParams` 일부 |

---

### [실무]

판단 체크:

- 공개 페이지인가?
- 사용자별 데이터인가?
- 검색 엔진 색인이 필요한가?
- 데이터 변경 빈도는 어느 정도인가?
- 빌드 시 경로를 모두 생성할 수 있는가?
- 경로 수가 너무 많은가?
- stale data 허용 시간이 있는가?
- CMS Webhook이 있는가?
- 요청 시점 인증 / 권한 검사가 필요한가?
- 서버 부하와 TTFB 요구는 어떤가?

---

### [FAQ]

Q. 블로그 상세 페이지는 SSR / SSG / ISR 중 무엇이 좋나?

A.
대부분 SSG 또는 ISR이 적합하다. CMS에서 자주 수정된다면 ISR과 on-demand revalidation을 고려한다.

Q. 마이페이지는 SSG로 만들 수 있나?

A.
권장하지 않는다. 사용자별 민감 데이터이므로 Dynamic Rendering이 적합하다.

Q. 검색 페이지는 ISR이 적합한가?

A.
검색 조건이 다양하고 요청마다 결과가 달라지면 Dynamic Rendering 또는 Client-side Fetch가 더 적합하다.

---

# 10. Static Rendering Rules

## 10.1 Static Rendering 작성 기준

### [개념]

Static Rendering은 렌더링 결과를 미리 생성하고 캐시해 여러 사용자에게 재사용하는 전략이다.

---

### [핵심]

Static Rendering 조건:

- 사용자별 데이터 없음
- 요청 헤더 / 쿠키 의존 없음
- 데이터 변경이 적음
- SEO 중요
- CDN 캐시 가능
- 빌드 시 데이터 접근 가능
- 경로 수 관리 가능
- 공개 콘텐츠

---

### [실무]

권장 패턴:

```tsx
export default async function DocsPage() {
  const docs = await getDocs();

  return <DocsView docs={docs} />;
}
```

검수 기준:

- `cookies()` / `headers()` 사용 여부 확인
- 사용자 세션 접근 여부 확인
- public cache 가능 여부 확인
- 데이터 변경 주기 확인
- 정적 생성 경로 수 확인
- 빌드 시간 영향 확인
- 정적 페이지에 민감 데이터 포함 여부 확인
- dynamic API 사용 여부 확인

주의:

- 정적 페이지에 사용자별 정보 포함 금지
- 경로 수가 많으면 build time 증가
- 동적 데이터가 필요한 일부 영역은 Client Fetch / Streaming / PPR 검토
- Static Rendering이 의도치 않게 Dynamic으로 바뀌는지 확인

---

### [FAQ]

Q. Static Rendering이 적합한 데이터는?

A.
모든 사용자에게 동일하고 변경이 적은 공개 데이터이다.

Q. Static Rendering에서 쿠키를 읽어도 되나?

A.
쿠키를 읽으면 요청별 결과가 달라질 수 있으므로 Dynamic Rendering으로 전환될 수 있다.

Q. Static Rendering의 주요 장점은?

A.
빠른 응답, CDN 캐시, 낮은 서버 부하, 좋은 SEO이다.

---

# 11. Dynamic Rendering Rules

## 11.1 Dynamic Rendering 작성 기준

### [개념]

Dynamic Rendering은 요청 시점의 정보, 사용자 상태, 쿠키, 헤더, 실시간 데이터에 따라 서버에서 렌더링하는 전략이다.

---

### [핵심]

Dynamic Rendering 조건:

- 사용자별 데이터
- 인증 / 권한 필요
- 요청 헤더 / 쿠키 필요
- 실시간 데이터 필요
- 요청마다 결과가 달라짐
- public cache 불가
- 최신 데이터 필요
- 보안상 stale data 위험
- Search Params 기반 조건 처리

---

### [실무]

권장 패턴:

```tsx
export default async function MyPage() {
  const user = await requireUser();
  const profile = await getProfile(user.id);

  return <ProfileView profile={profile} />;
}
```

검수 기준:

- 인증 / 권한 검사가 서버에서 수행되는가?
- 사용자별 데이터가 public cache에 저장되지 않는가?
- TTFB가 너무 느리지 않은가?
- 요청마다 필요한 데이터만 조회하는가?
- DB / API 호출이 병렬화 가능한가?
- Error / Loading UI가 있는가?
- Cache가 필요한 일부 공개 데이터와 분리 가능한가?

주의:

- 모든 페이지를 Dynamic으로 만들면 서버 부하 증가
- Dynamic Rendering은 cache 이점이 줄어들 수 있음
- 사용자별 데이터와 공개 데이터를 한 컴포넌트에 섞으면 최적화 어려움
- Client에서만 권한을 가리면 보안 아님

---

### [FAQ]

Q. Dynamic Rendering은 언제 필요한가?

A.
사용자별 데이터, 인증 / 권한, 요청마다 달라지는 결과, 최신성이 중요한 데이터에 필요하다.

Q. Dynamic Rendering은 느린가?

A.
항상 느린 것은 아니지만 요청마다 서버 작업이 필요하므로 Static Rendering보다 TTFB가 증가할 수 있다.

Q. Dynamic Rendering을 줄이는 방법은?

A.
공개 정적 영역과 사용자별 동적 영역을 분리하고, 일부 데이터는 cache / revalidation을 적용한다.

---

# 12. Revalidation Rules

## 12.1 Time-based / On-demand Revalidation

### [개념]

Revalidation은 캐시된 정적 결과를 일정 시간 또는 특정 이벤트 이후 다시 생성하는 방식이다.

---

### [핵심]

Revalidation 유형:

- Time-based Revalidation
- On-demand Revalidation
- Path Revalidation
- Tag Revalidation
- Cache Invalidation
- Stale Data
- Fresh Data
- CMS Webhook
- Admin Mutation
- Server Action Revalidation
- Route Handler Revalidation

---

### [실무]

Time-based Revalidation:

```tsx
export const revalidate = 600;
```

Fetch Revalidation:

```tsx
await fetch("https://api.example.com/products", {
  next: { revalidate: 300 },
});
```

Path Revalidation:

```ts
revalidatePath("/products");
```

Tag Revalidation:

```ts
revalidateTag("products");
```

사용 기준:

- 시간 기반 갱신 → 데이터 변경 주기가 예측 가능
- On-demand 갱신 → CMS publish, 관리자 수정, 상품 변경
- Path 단위 갱신 → 특정 페이지 갱신
- Tag 단위 갱신 → 관련 데이터 묶음 갱신
- Mutation 이후 → 관련 path / tag revalidation

주의:

- Revalidation 누락 시 오래된 데이터 표시
- 너무 잦은 revalidation은 서버 부하 증가
- On-demand endpoint 보안 필수
- tag 이름 규칙 필요
- path 갱신과 data cache 갱신 범위 차이 이해 필요

---

### [FAQ]

Q. Time-based Revalidation은 언제 쓰나?

A.
데이터가 일정 주기로 바뀌고 몇 초 또는 몇 분 정도 stale 상태를 허용할 수 있을 때 사용한다.

Q. On-demand Revalidation은 언제 쓰나?

A.
CMS publish, 관리자 수정, 상품 변경처럼 이벤트 발생 시 즉시 캐시를 무효화해야 할 때 사용한다.

Q. `revalidatePath`와 `revalidateTag` 차이는?

A.
`revalidatePath`는 특정 경로를 갱신하고, `revalidateTag`는 같은 tag로 연결된 캐시 항목들을 갱신한다.

---

# 13. Dynamic Route and generateStaticParams Rules

## 13.1 Dynamic Route 정적 생성

### [개념]

`generateStaticParams`는 Dynamic Route Segment에서 빌드 시점에 정적으로 생성할 경로 목록을 지정하는 App Router 함수이다.

Next.js 공식 문서 기준 `generateStaticParams`는 dynamic route segment와 함께 사용되어 요청 시점이 아니라 빌드 시점에 route를 정적으로 생성할 수 있다.

---

### [핵심]

필수 포함:

- Dynamic Segment
- `generateStaticParams`
- Static Params
- Dynamic Params
- Build-time Path Generation
- On-demand Generation
- Large Path Count
- Fallback Behavior
- `dynamicParams`
- ISR with Dynamic Route

예시:

```tsx
export async function generateStaticParams() {
  const posts = await getPopularPosts();

  return posts.map((post) => ({
    slug: post.slug,
  }));
}
```

---

### [실무]

사용 기준:

- 경로 수가 제한적이고 빌드 시 알 수 있음 → 전체 생성 가능
- 경로 수가 매우 많음 → 인기 경로만 생성 + 나머지 on-demand 검토
- CMS / 상품 상세 → ISR과 조합 가능
- 없는 경로 처리 → `notFound()` 고려
- slug / id 타입 검증 필요
- build time 증가 주의
- 데이터 소스 장애 시 build 실패 가능성 고려

주의:

- 모든 경로를 무조건 build time에 생성하지 않기
- 대량 페이지는 빌드 시간이 크게 늘어남
- `generateStaticParams` 데이터와 실제 상세 데이터 불일치 주의
- 삭제된 콘텐츠는 revalidation / notFound 처리 필요

---

### [FAQ]

Q. `generateStaticParams`는 언제 사용하나?

A.
Dynamic Route 중 미리 생성할 경로를 빌드 시점에 알 수 있을 때 사용한다.

Q. 상품 상세가 수십만 개면 전부 `generateStaticParams`에 넣어야 하나?

A.
권장하지 않는다. 인기 상품만 사전 생성하고 나머지는 on-demand 또는 dynamic 전략을 검토한다.

Q. `generateStaticParams`는 Pages Router의 무엇과 비슷한가?

A.
Pages Router의 `getStaticPaths`와 비슷한 역할이다.

---

# 14. Streaming Rules

## 14.1 Streaming / Suspense Rendering

### [개념]

Streaming은 route를 작은 chunk로 나누어 준비된 부분부터 점진적으로 클라이언트에 전송하는 렌더링 방식이다.

Next.js 학습 문서 기준 Streaming은 route를 작은 chunk로 나누고 준비되는 대로 서버에서 클라이언트로 점진 전송하는 데이터 전송 기법이다.

---

### [핵심]

필수 포함:

- Streaming
- Suspense
- Progressive Rendering
- Loading UI
- `loading.tsx`
- Slow Data
- Partial UI
- Server Component
- Route Segment
- Perceived Performance
- Waterfall Reduction

---

### [실무]

사용 기준:

- 페이지 일부 데이터가 느림
- 전체 페이지를 기다리지 않고 일부 UI를 먼저 보여주고 싶음
- Header / Layout / Static Shell은 빠르게 표시 가능
- 상세 데이터 / 추천 목록 / 통계만 느림
- Suspense Boundary로 느린 영역 분리 가능
- `loading.tsx`로 Route Segment fallback 제공 가능

예시:

```tsx
export default function DashboardPage() {
  return (
    <>
      <Summary />
      <React.Suspense fallback={<ChartSkeleton />}>
        <SlowChart />
      </React.Suspense>
    </>
  );
}
```

주의:

- 너무 많은 Suspense Boundary는 UI 복잡도 증가
- fallback UI는 layout shift를 줄이도록 설계
- Streaming은 느린 데이터 자체를 빠르게 만드는 것이 아님
- Error Boundary와 함께 설계 필요
- 사용자에게 중요한 핵심 정보가 너무 늦게 나오지 않게 조정

---

### [FAQ]

Q. Streaming은 언제 사용하나?

A.
일부 데이터가 느리지만 페이지의 다른 영역은 먼저 보여줄 수 있을 때 사용한다.

Q. Streaming이 API 응답 속도를 빠르게 하나?

A.
아니다. 느린 API 자체를 빠르게 하지는 않지만 준비된 UI를 먼저 보여줘 체감 성능을 개선한다.

Q. Streaming과 SSR은 같이 쓸 수 있나?

A.
가능하다. 서버에서 렌더링하면서 준비된 chunk를 점진적으로 전송할 수 있다.

---

# 15. Partial Prerendering Rules

## 15.1 PPR / Static Shell + Dynamic Content

### [개념]

Partial Prerendering은 정적 shell과 동적 콘텐츠를 한 route 안에서 조합하는 렌더링 최적화 개념이다.

Next.js Glossary는 Partial Prerendering을 static shell은 즉시 제공하고 dynamic content는 함께 조합하는 rendering optimization으로 설명한다.

---

### [핵심]

필수 포함:

- Partial Prerendering
- Static Shell
- Dynamic Content
- Suspense Boundary
- Streaming
- Static Layout
- Dynamic Slot
- Personalized Section
- Performance Optimization
- App Router

---

### [실무]

적합한 상황:

- 페이지 대부분은 정적
- 일부 영역만 사용자별 또는 실시간
- Header / Layout / Product Info는 정적
- Cart / Notification / Recommendation은 동적
- 정적 shell을 빠르게 제공하고 싶음
- 동적 영역을 Suspense로 분리 가능

주의:

- PPR 지원 여부와 설정은 Next.js 버전 / Hosting 환경 확인 필요
- 정적 영역과 동적 영역 경계가 명확해야 함
- 사용자별 데이터가 정적 shell에 섞이면 안 됨
- fallback UI 품질 중요
- Cache 정책과 Dynamic API 사용 범위 확인 필요

---

### [FAQ]

Q. Partial Prerendering은 무엇인가?

A.
페이지의 정적 shell은 빠르게 제공하고 일부 동적 영역은 요청 시점에 렌더링하는 전략이다.

Q. PPR은 언제 유용한가?

A.
대부분 정적이지만 일부 사용자별 영역이 있는 페이지에서 유용하다.

Q. PPR은 SSR / SSG / ISR 중 어디에 속하나?

A.
단일 전략이라기보다 Static Rendering과 Dynamic Rendering을 한 route 안에서 조합하는 방식이다.

---

# 16. Cache Strategy Rules

## 16.1 Rendering Strategy와 Cache

### [개념]

Cache Strategy는 Rendering Strategy의 성능과 데이터 신선도를 결정한다.

SSR / SSG / ISR 판단은 Cache 가능 여부와 Cache 무효화 방식까지 함께 결정해야 한다.

---

### [핵심]

Cache 기준:

- Public Cache
- Private Cache
- No Store
- Fetch Cache
- Data Cache
- Full Route Cache
- Router Cache
- Cache Key
- Cache Tag
- Revalidation
- Invalidation
- CDN Cache
- Browser Cache
- User-specific Cache

---

### [실무]

Cache 판단 표:

| 데이터             | 권장 전략                    |
| ------------------ | ---------------------------- |
| 공개 마케팅 페이지 | Static / CDN Cache           |
| 블로그 상세        | ISR / Revalidation           |
| CMS 문서           | ISR + On-demand Revalidation |
| 상품 상세          | ISR + Tag Revalidation       |
| 로그인 사용자 정보 | Dynamic / no-store           |
| 장바구니           | Dynamic / private            |
| 관리자 통계        | Dynamic / short cache        |
| 검색 결과          | Dynamic 또는 Query Cache     |
| 실시간 알림        | no-store / Client Fetch      |

주의:

- 사용자별 데이터를 public cache하지 않기
- Cache Key에 locale / search params / auth 영향을 반영
- Mutation 후 revalidation 누락 주의
- Cache가 stale data를 만들 수 있음을 문서화
- 캐시 전략은 Next.js 버전별 동작 차이를 확인해야 함
- Next.js 16 이후 Cache Components 중심으로 caching이 opt-in 방향으로 변경된 점을 고려해야 한다.

---

### [FAQ]

Q. SSR / SSG / ISR 선택에서 Cache가 왜 중요한가?

A.
렌더링 결과를 재사용할 수 있는지, 데이터가 얼마나 신선해야 하는지, 사용자별 데이터가 섞이는지 결정하기 때문이다.

Q. 사용자별 데이터를 public cache하면 왜 위험한가?

A.
다른 사용자에게 민감 데이터가 노출될 수 있다.

Q. Cache 때문에 데이터가 안 바뀌면 무엇을 확인하나?

A.
Revalidation 설정, cache key, tag, path invalidation, mutation 후 갱신 로직을 확인한다.

---

# 17. SEO Rules

## 17.1 SEO와 Rendering Strategy

### [개념]

SEO는 검색 엔진이 페이지 콘텐츠와 metadata를 읽고 색인할 수 있도록 렌더링 전략과 metadata를 설계하는 기준이다.

---

### [핵심]

SEO에 유리한 전략:

- Static Rendering
- ISR
- Dynamic Rendering
- Server Component
- Metadata API
- `generateMetadata`
- Sitemap
- Robots
- Canonical URL
- Open Graph
- Structured Data
- Fast LCP
- Stable HTML

---

### [실무]

SEO 기준:

- 공개 콘텐츠는 서버에서 HTML 제공
- 블로그 / 문서 / 상품 상세는 SSG 또는 ISR 우선 검토
- 동적 사용자 페이지는 robots 정책 검토
- 상세 페이지는 `generateMetadata` 사용 가능
- stale metadata 방지를 위해 content revalidation과 metadata revalidation 연결
- 검색 결과 페이지 색인 여부 결정
- Client-only rendering에 SEO 핵심 콘텐츠 의존 금지
- 페이지 속도와 Core Web Vitals도 SEO에 영향

주의:

- 관리자 / 마이페이지는 색인 금지
- 개인화 콘텐츠를 SEO 대상으로 만들지 않기
- metadata와 실제 콘텐츠 불일치 주의
- ISR 페이지의 metadata stale 가능성 확인

---

### [FAQ]

Q. SEO가 중요한 페이지는 어떤 전략이 좋나?

A.
공개 콘텐츠라면 Static Rendering 또는 ISR이 적합하다. 요청마다 달라지는 공개 데이터는 Dynamic Rendering도 가능하다.

Q. Client-side Fetch만으로 SEO 콘텐츠를 보여줘도 되나?

A.
권장하지 않는다. SEO 핵심 콘텐츠는 서버 렌더링 결과에 포함되는 것이 좋다.

Q. ISR에서 metadata도 갱신되나?

A.
콘텐츠와 metadata 생성 로직이 같은 revalidation 흐름에 연결되어야 최신 상태를 유지할 수 있다.

---

# 18. Performance Rules

## 18.1 성능과 Rendering Strategy

### [개념]

Rendering Strategy는 TTFB, LCP, 서버 부하, CDN Cache, JavaScript Hydration 비용에 직접 영향을 준다.

---

### [핵심]

성능 영향:

| 전략      | 장점                   | 주의                    |
| --------- | ---------------------- | ----------------------- |
| SSR       | 최신 데이터 / 개인화   | TTFB 증가 가능          |
| SSG       | 빠른 응답 / CDN 캐시   | stale data / build time |
| ISR       | 빠른 응답 + 갱신 가능  | revalidation 복잡도     |
| Streaming | 체감 속도 개선         | fallback 설계 필요      |
| PPR       | 정적 shell + 동적 영역 | 환경 / 경계 설계 필요   |

---

### [실무]

성능 기준:

- 공개 페이지는 Static / ISR로 서버 부하 감소
- 사용자별 페이지는 Dynamic이 필요하지만 데이터 병렬화로 TTFB 관리
- 느린 일부 영역은 Streaming으로 분리
- Client Component를 줄여 Hydration Cost 감소
- LCP 콘텐츠가 서버에서 빨리 제공되는지 확인
- ISR 주기를 조정해 신선도와 서버 부하 균형
- Dynamic API 사용으로 정적 최적화가 깨지는지 확인
- 캐시 가능한 데이터와 캐시 불가 데이터를 분리

---

### [FAQ]

Q. SSR은 성능에 나쁜가?

A.
항상 나쁜 것은 아니다. 최신성과 개인화가 필요한 경우 적합하지만 TTFB와 서버 부하를 관리해야 한다.

Q. SSG가 가장 빠른가?

A.
대체로 빠르지만 콘텐츠 stale, build time, 대량 route 문제를 고려해야 한다.

Q. ISR은 성능과 최신성을 모두 잡는가?

A.
많은 공개 콘텐츠에 유용하지만 revalidation 주기와 invalidation 설계가 필요하다.

---

# 19. Security Rules

## 19.1 Rendering Strategy와 보안

### [개념]

Rendering Strategy 보안은 사용자별 데이터, 쿠키, 세션, 권한 정보가 정적 캐시나 public cache에 잘못 저장되지 않도록 하는 기준이다.

---

### [핵심]

보안 위험:

- User Data Cache Leak
- Public Cache Leak
- Static Page Personalization
- Token Exposure
- Cookie-based Rendering
- Authorization Check
- Server-only Secret
- On-demand Revalidation Secret
- Webhook Signature
- Preview Mode Security
- Error Message Exposure

---

### [실무]

보안 기준:

- 사용자별 데이터는 Static Rendering 금지
- 인증 / 권한 검사는 서버에서 수행
- Client UI 숨김만으로 권한 처리 금지
- On-demand Revalidation endpoint는 secret 또는 signature 검증
- CMS Webhook 검증
- Preview / Draft Mode 접근 제한
- Error page에 민감 정보 노출 금지
- Server Component에서 Secret 사용 가능하지만 Client props로 전달 금지
- Cache Header와 데이터 성격 일치 확인
- 개인화 데이터와 공개 캐시 분리

---

### [FAQ]

Q. 사용자별 데이터를 ISR로 처리해도 되나?

A.
권장하지 않는다. ISR은 공개 정적 콘텐츠 갱신에 적합하며 사용자별 민감 데이터는 Dynamic Rendering이 안전하다.

Q. On-demand Revalidation endpoint는 공개해도 되나?

A.
안 된다. secret token, webhook signature, 인증 검증이 필요하다.

Q. Client에서 버튼만 숨기면 권한 처리가 되나?

A.
아니다. 서버에서 인증과 권한을 반드시 검증해야 한다.

---

# 20. Hosting and Runtime Rules

## 20.1 배포 환경 / Runtime 제약

### [개념]

SSR / SSG / ISR 전략은 Hosting Platform, Runtime, Cache Storage, Serverless 환경, CDN 지원 여부에 영향을 받는다.

---

### [핵심]

필수 포함:

- Node Runtime
- Edge Runtime
- Serverless
- Static Hosting
- CDN
- Cache Storage
- ISR Support
- Revalidation Support
- Route Handler
- Server Action
- Deployment Platform
- Build Output
- Cold Start
- Region
- Runtime Compatibility

---

### [실무]

검토 기준:

- Hosting Platform이 SSR을 지원하는가?
- ISR / Revalidation을 지원하는가?
- Edge Runtime에서 필요한 API가 동작하는가?
- Cache가 여러 region에서 일관되게 동작하는가?
- Static export만 가능한 환경인가?
- Serverless cold start 영향은 어떤가?
- On-demand Revalidation endpoint가 배포 환경에서 동작하는가?
- CDN Cache Header가 의도대로 적용되는가?
- Build output과 runtime 요구사항이 맞는가?

주의:

- Static Hosting만 지원하면 SSR / ISR 제약 가능
- Edge Runtime은 Node API 사용에 제약 가능
- ISR 지원은 hosting platform에 따라 다를 수 있음
- 자체 호스팅 시 cache / revalidation 인프라 요구 확인
- Next.js 배포 문서는 static / dynamic boundary와 hosting requirements를 함께 설명한다.

---

### [FAQ]

Q. SSR / ISR은 모든 배포 환경에서 되나?

A.
아니다. Hosting Platform과 Runtime 지원 여부를 확인해야 한다.

Q. Static Hosting만 가능하면 어떤 전략이 적합한가?

A.
정적 export 가능한 SSG 중심 전략이 적합하다. SSR이나 ISR은 제한될 수 있다.

Q. Edge Runtime에서 ISR을 쓸 수 있나?

A.
지원 여부는 Next.js 버전과 배포 플랫폼 기준으로 확인해야 한다. Runtime 제약을 반드시 검토한다.

---

# 21. Troubleshooting Rules

## 21.1 자주 발생하는 Rendering 문제

### [개념]

Troubleshooting 문서는 Agent가 SSR / SSG / ISR 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Static으로 예상했는데 Dynamic으로 렌더링됨
- Dynamic이어야 하는데 캐시됨
- ISR 데이터가 갱신되지 않음
- Revalidation 후에도 stale data 표시
- Build Time이 너무 김
- Dynamic Route가 404 발생
- `generateStaticParams` 누락
- 사용자별 데이터가 캐시됨
- CMS Webhook revalidation 실패
- `revalidatePath` 범위 오해
- `revalidateTag` tag 누락
- LCP 느림
- TTFB 느림
- Hydration Error
- Hosting에서 ISR 미동작
- Edge Runtime 제약 오류

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

- ISR 페이지 데이터가 갱신되지 않음

원인:

- revalidate 시간이 너무 김
- mutation 후 revalidatePath / revalidateTag 호출 누락
- fetch cache tag가 설정되지 않음
- on-demand endpoint 인증 실패

해결:

- revalidate 주기 확인
- mutation 후 path 또는 tag revalidation 추가
- fetch에 명확한 tag 설정
- webhook secret / signature 검증 로직 확인
```

예시:

```md
문제:

- Static으로 예상한 페이지가 Dynamic Rendering됨

원인:

- cookies / headers / searchParams 같은 dynamic data 사용
- 사용자 세션 조회 포함
- cache: no-store 사용
- route segment config가 dynamic으로 설정됨

해결:

- dynamic API 사용 위치 확인
- 사용자별 영역을 분리
- 정적 데이터와 동적 데이터를 분리
- Rendering Strategy를 명시적으로 재검토
```

예시:

```md
문제:

- Build Time이 너무 김

원인:

- generateStaticParams에서 너무 많은 경로 생성
- 빌드 중 느린 외부 API 호출
- 모든 상세 페이지를 사전 생성
- 이미지 / 데이터 처리 작업이 build에 집중됨

해결:

- 인기 경로만 사전 생성
- ISR / on-demand generation 검토
- 빌드 중 API 호출 최적화
- 경로 생성 범위 축소
```

---

### [FAQ]

Q. ISR 데이터가 안 바뀌면 무엇을 확인해야 하나?

A.
`revalidate`, `revalidatePath`, `revalidateTag`, fetch tag, mutation 후 invalidation, webhook 인증을 확인해야 한다.

Q. Static으로 만들었는데 Dynamic이 되면 무엇을 봐야 하나?

A.
cookies, headers, searchParams, no-store, 사용자 세션 접근, route segment config를 확인한다.

Q. Build Time이 너무 길면 어떻게 해야 하나?

A.
모든 경로를 사전 생성하지 말고 인기 경로만 생성하거나 ISR / on-demand generation을 검토한다.

---

# 22. Code Example Rules

## 22.1 코드 예제 작성 기준

### [개념]

SSR / SSG / ISR 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- App Router 기준 예제 우선
- Pages Router 함수 중심 예제 금지
- 핵심 Rendering Strategy만 포함
- 긴 전체 파일 금지
- 보안 위험 예제 금지
- 사용자별 데이터 cache 예제 금지
- Revalidation 예제에는 보안 주의 포함
- `generateStaticParams` 예제 포함 권장
- `revalidatePath` / `revalidateTag` 예제 포함 권장
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Static Page
- Dynamic Page
- ISR Page
- Time-based Revalidation
- On-demand Revalidation
- Tag Revalidation
- Dynamic Route + `generateStaticParams`
- `notFound()` 처리
- Suspense / Streaming
- 사용자별 Dynamic Page
- CMS Webhook Route Handler
- Rendering Strategy Decision Table

금지 예제:

- App Router 문서에서 `getServerSideProps` 중심 예제
- App Router 문서에서 `getStaticProps` 중심 예제
- Secret 없는 On-demand Revalidation endpoint
- 사용자별 데이터를 `revalidate`로 캐시하는 예제
- 모든 페이지를 `force-dynamic`으로 처리하는 예제
- 모든 route를 build time에 생성하는 예제
- Hydration Error를 무조건 suppress하는 예제

---

### [FAQ]

Q. SSR / SSG / ISR 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. Pages Router 예제를 넣어도 되나?

A.
비교 목적이면 가능하지만 App Router 기준 문서에서는 중심 예제로 사용하지 않는다.

---

# 23. Comparison Rules

## 23.1 필수 비교 대상

### [개념]

SSR / SSG / ISR 문서는 Agent의 Rendering Strategy 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- SSR vs SSG
- SSG vs ISR
- SSR vs ISR
- Static Rendering vs Dynamic Rendering
- Static Rendering vs Streaming
- ISR vs On-demand Revalidation
- `revalidatePath` vs `revalidateTag`
- Public Cache vs Private Cache
- Build-time Rendering vs Request-time Rendering
- Server Component vs Client Component
- Pages Router Rendering vs App Router Rendering
- `generateStaticParams` vs Runtime Dynamic Params
- Static Route vs Dynamic Route
- PPR vs SSR
- PPR vs ISR
- CDN Cache vs Next.js Cache
- SEO Page vs Personalized Page

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 생성 시점 / 캐시 / 데이터 신선도 / SEO / 서버 부하 / 사용 예시로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. SSR과 SSG 중 무엇이 더 좋은가?

A.
공개 정적 콘텐츠는 SSG가 유리하고, 사용자별 최신 데이터는 SSR이 적합하다.

Q. SSG와 ISR 중 무엇을 써야 하나?

A.
거의 바뀌지 않는 콘텐츠는 SSG, 가끔 바뀌고 전체 재빌드가 부담되면 ISR이 적합하다.

Q. `revalidatePath`와 `revalidateTag` 중 무엇을 써야 하나?

A.
특정 경로만 갱신하면 `revalidatePath`, 여러 페이지에서 공유하는 데이터 묶음을 갱신하면 `revalidateTag`가 적합하다.

---

# 24. Checklist Rules

## 24.1 문서 품질 체크리스트

### [개념]

SSR / SSG / ISR RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] SSR / SSG / ISR 목적이 명확한가?
- [ ] App Router 기준으로 작성했는가?
- [ ] Pages Router 중심 설명을 피했는가?
- [ ] SSR을 Dynamic Rendering과 연결했는가?
- [ ] SSG를 Static Rendering과 연결했는가?
- [ ] ISR을 Revalidation과 연결했는가?
- [ ] Rendering Strategy 선택 기준을 포함했는가?
- [ ] 사용자별 데이터와 공개 데이터 구분을 포함했는가?
- [ ] Cache Strategy 기준을 포함했는가?
- [ ] Revalidation 기준을 포함했는가?
- [ ] `generateStaticParams` 기준을 포함했는가?
- [ ] Dynamic Route 기준을 포함했는가?
- [ ] Streaming / Suspense 기준을 포함했는가?
- [ ] PPR 개념을 포함했는가?
- [ ] SEO와 Performance 기준을 포함했는가?
- [ ] 보안 / Cache 누수 주의를 포함했는가?
- [ ] Hosting / Runtime 제약을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Next.js App Router / Performance / Cache 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- App Router / Performance / Frontend Architecture 문서와 연계 가능해야 함

---

### [FAQ]

Q. SSR / SSG / ISR 문서 품질에서 가장 중요한 것은?

A.
Rendering Strategy 선택 기준, 사용자별 데이터와 공개 데이터 구분, Cache / Revalidation / SEO / Performance / 보안 기준이 명확해야 한다.

---

# 25. Retrieval Optimization Rules

## 25.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- SSR
- SSG
- ISR
- Server-side Rendering
- Static Site Generation
- Incremental Static Regeneration
- Next.js Rendering
- App Router Rendering
- Static Rendering
- Dynamic Rendering
- Streaming
- Partial Prerendering
- PPR
- Server Component
- Client Component
- Revalidation
- Time-based Revalidation
- On-demand Revalidation
- `revalidate`
- `revalidatePath`
- `revalidateTag`
- `generateStaticParams`
- Dynamic Route
- Static Route
- Fetch Cache
- Data Cache
- Full Route Cache
- Router Cache
- Public Cache
- Private Cache
- `no-store`
- `force-dynamic`
- `force-static`
- CDN Cache
- SEO Rendering
- TTFB
- LCP
- CMS Webhook
- Cache Invalidation
- Stale Data
- User-specific Data
- Public Content
- Personalized Page
- Build Time
- Request Time
- Rendering Strategy

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- SSR SSG ISR 차이
- App Router에서 SSR 어떻게 해?
- App Router에서 SSG 어떻게 해?
- App Router에서 ISR 어떻게 해?
- Static Rendering과 Dynamic Rendering 차이
- `revalidatePath`와 `revalidateTag` 차이
- `generateStaticParams` 언제 써?
- 블로그는 SSR SSG ISR 중 뭐가 좋아?
- 상품 상세는 ISR이 좋아?
- 마이페이지는 SSG 가능해?
- 검색 페이지는 어떤 렌더링 전략?
- 사용자별 데이터 캐시해도 돼?
- ISR 데이터가 안 바뀌어
- Static으로 예상했는데 Dynamic 됨
- Build Time이 너무 김
- On-demand Revalidation 어떻게 해?
- CMS Webhook으로 ISR 갱신
- Next.js Cache 때문에 데이터가 안 바뀜
- Streaming은 언제 써?
- PPR은 뭐야?
- SSR은 SEO에 좋아?
- SSG는 항상 빠른가?
- ISR은 언제 쓰면 안 돼?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 26. Version Rules

## 26.1 기준 버전

### [개념]

SSR / SSG / ISR 문서는 Modern Next.js App Router 기준으로 작성하며, Next.js 버전별 Cache / Rendering 정책 변화 가능성을 명확히 기록한다.

---

### [핵심]

기준:

- Modern Next.js
- App Router
- React Server Components
- Server Component
- Static Rendering
- Dynamic Rendering
- Streaming
- Revalidation
- `generateStaticParams`
- `revalidatePath`
- `revalidateTag`
- Fetch Cache
- Cache Components
- Partial Prerendering
- TypeScript
- Modern Hosting Platform

Legacy 제외:

- Pages Router 중심 설계
- `getServerSideProps` 중심 설명
- `getStaticProps` 중심 설명
- `getStaticPaths` 중심 설명
- `_app.tsx` 중심 구조
- CSR만으로 SEO 콘텐츠 처리
- 사용자별 데이터를 Static Cache하는 구조
- Revalidation 보안 검증 없는 Webhook
- 모든 페이지를 무조건 SSR로 처리하는 구조

---

### [실무]

문서 작성 시 주의:

- Next.js는 App Router Cache / Rendering 동작이 버전별로 바뀔 수 있음
- Next.js 16은 Cache Components와 opt-in caching 방향을 강조하므로 최신 공식 문서 확인 필요
- Stable 기능과 Experimental 기능을 구분
- PPR은 프로젝트 버전 / hosting 지원 여부 확인
- Edge Runtime / Node Runtime 제약 확인
- App Router 기준 예제 우선
- Pages Router는 비교와 마이그레이션 문맥으로 제한
- 공식 문서 기준을 우선하며 블로그 자료는 보조로만 사용

---

### [FAQ]

Q. SSR / SSG / ISR 문서는 최신성이 중요한가?

A.
중요하다. Next.js App Router의 Cache와 Rendering 정책은 버전별 차이가 있으므로 최신 공식 문서를 기준으로 확인해야 한다.

Q. Pages Router 방식은 완전히 버려야 하나?

A.
기존 프로젝트 유지보수와 비교를 위해 이해는 필요하지만, 새 문서는 App Router 기준으로 작성한다.

Q. PPR은 항상 사용할 수 있나?

A.
아니다. Next.js 버전, 설정, 배포 플랫폼 지원 여부를 확인해야 한다.

---

# 27. Common Mistakes

## 27.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Rendering Strategy 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- App Router 문서에서 `getServerSideProps` 중심으로 설명
- SSR / SSG / ISR 용어를 App Router 개념과 연결하지 않음
- 모든 페이지를 SSR로 처리
- 모든 페이지를 SSG로 처리
- 사용자별 데이터를 Static Cache
- 인증 페이지에 public cache 적용
- CMS 콘텐츠에 Revalidation 누락
- Mutation 후 `revalidatePath` / `revalidateTag` 누락
- On-demand Revalidation endpoint에 인증 없음
- `generateStaticParams`로 너무 많은 경로 생성
- 빌드 시점에 느린 외부 API를 과도하게 호출
- 검색 페이지를 무리하게 SSG 처리
- `cookies` / `headers` 사용으로 의도치 않게 Dynamic Rendering 전환
- `no-store` 남용
- Cache tag 이름 규칙 없음
- stale data 허용 범위 문서화 없음
- Streaming fallback UI 품질 낮음
- Edge Runtime 제약 무시
- Hosting Platform의 ISR 지원 여부 미확인
- Hydration 비용과 Rendering Strategy를 혼동

---

### [실무]

리뷰 기준:

- 페이지별 데이터 성격 확인
- 공개 데이터 / 사용자별 데이터 구분
- Rendering Strategy 명시 여부 확인
- Cache 정책 확인
- Revalidation 주기 확인
- On-demand Revalidation 보안 확인
- Dynamic API 사용 여부 확인
- `generateStaticParams` 경로 수 확인
- Build Time 영향 확인
- SEO metadata 갱신 여부 확인
- Streaming / Suspense fallback 확인
- Hosting / Runtime 지원 확인
- Next.js 버전별 Cache 정책 확인

---

### [FAQ]

Q. SSR / SSG / ISR에서 가장 흔한 실수는?

A.
데이터 성격을 구분하지 않고 모든 페이지에 같은 Rendering Strategy를 적용하는 것이다.

Q. 사용자별 데이터를 Static Cache하면 왜 위험한가?

A.
다른 사용자에게 민감 데이터가 노출될 수 있기 때문이다.

Q. ISR에서 가장 자주 누락되는 것은?

A.
Mutation 이후 revalidation 처리와 On-demand Revalidation endpoint 보안 검증이다.

---

# 28. Final Goal

## 28.1 최종 목표

### [개념]

SSR / SSG / ISR RAG 문서는 Agent가 Next.js App Router 기반 프로젝트에서 페이지별 Rendering Strategy를 설계, 생성, 검토, 최적화할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- SSR / SSG / ISR 차이 설명
- App Router Rendering Strategy 매핑
- Static Rendering 후보 판단
- Dynamic Rendering 후보 판단
- ISR / Revalidation 후보 판단
- 사용자별 데이터 Cache 위험 진단
- 공개 콘텐츠 Cache 전략 제안
- SEO 페이지 Rendering Strategy 제안
- Dynamic Route + `generateStaticParams` 설계
- `revalidatePath` / `revalidateTag` 선택
- CMS Webhook Revalidation 설계
- Build Time 문제 진단
- Stale Data 문제 진단
- Streaming / Suspense 적용 판단
- PPR 적용 가능성 검토
- Hosting / Runtime 제약 검토
- SSR / SSG / ISR 코드 리뷰
- Cache / Revalidation Troubleshooting

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- App Router 기준 설명
- Pages Router 패턴과 혼동 방지
- 코드 예제는 짧고 안전하게 작성
- 사용자별 데이터 / 공개 데이터 / Cache 경계 명확화
- SEO / Performance / Security / Hosting 기준 포함
- Next.js App Router / Performance / Cache 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. SSR / SSG / ISR Domain Rules의 최종 목적은?

A.
Agent가 Next.js App Router 기반 프로젝트에서 페이지별 Static Rendering, Dynamic Rendering, Revalidation, Streaming 전략을 선택하고 Cache / SEO / 성능 / 보안 관점에서 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. SSR SSG ISR 문서는 어떤 기준으로 작성해야 해?

A.
App Router 기준으로 Static Rendering, Dynamic Rendering, Revalidation, Cache, SEO, Performance, Security, Hosting 제약을 중심으로 작성해야 한다.

Q. SSR SSG ISR 차이는?

A.
SSR은 요청 시점 렌더링, SSG는 빌드 시점 정적 생성, ISR은 정적 생성 결과를 일정 시간 또는 이벤트 이후 갱신하는 전략이다.

Q. App Router에서 SSR은 어떻게 해?

A.
`getServerSideProps`가 아니라 Server Component와 Dynamic Rendering으로 처리한다. 사용자별 데이터, cookies, headers, 세션 접근이 대표적인 Dynamic Rendering 후보이다.

Q. App Router에서 SSG는 어떻게 해?

A.
Static Rendering과 `generateStaticParams`, cache 가능한 fetch, 정적 route 구성을 통해 처리한다.

Q. App Router에서 ISR은 어떻게 해?

A.
`revalidate`, `fetch`의 `next.revalidate`, `revalidatePath`, `revalidateTag`를 사용한다.

Q. Static Rendering과 Dynamic Rendering 차이는?

A.
Static Rendering은 결과를 미리 생성하고 캐시해 재사용하며, Dynamic Rendering은 요청 시점 정보에 따라 서버에서 렌더링한다.

Q. SSR은 언제 사용해?

A.
사용자별 데이터, 인증 / 권한, 요청마다 달라지는 데이터, 최신성이 중요한 페이지에 사용한다.

Q. SSG는 언제 사용해?

A.
모든 사용자에게 같은 공개 콘텐츠를 제공하고 데이터 변경이 적으며 SEO가 중요한 페이지에 사용한다.

Q. ISR은 언제 사용해?

A.
SEO가 중요하고 공개 콘텐츠이지만 데이터가 가끔 바뀌는 페이지에 사용한다.

Q. 블로그는 SSR SSG ISR 중 뭐가 좋아?

A.
대부분 SSG 또는 ISR이 적합하다. CMS에서 자주 수정된다면 ISR과 on-demand revalidation을 고려한다.

Q. 상품 상세는 ISR이 좋아?

A.
공개 상품 정보이고 주기적으로 바뀐다면 ISR이 적합하다. 가격 / 재고 신선도 요구가 높으면 revalidation 주기를 짧게 하거나 Dynamic 영역을 분리한다.

Q. 마이페이지는 SSG 가능해?

A.
권장하지 않는다. 사용자별 민감 데이터이므로 Dynamic Rendering이 적합하다.

Q. 관리자 대시보드는 어떤 전략이 좋아?

A.
권한 검사가 필요하고 데이터가 자주 바뀌므로 Dynamic Rendering이 적합하다.

Q. 검색 페이지는 어떤 렌더링 전략이 좋아?

A.
검색 조건이 다양하고 요청마다 결과가 달라지면 Dynamic Rendering 또는 Client-side Fetch가 적합하다.

Q. 로그인 페이지는 SSG 가능해?

A.
로그인 Form 자체는 정적으로 가능하지만 이미 로그인한 사용자 redirect 같은 처리가 있으면 Dynamic 판단이 필요하다.

Q. 사용자별 데이터 캐시해도 돼?

A.
public cache는 금지해야 한다. private cache 또는 no-store, Dynamic Rendering을 고려한다.

Q. 공개 콘텐츠는 무조건 SSG야?

A.
아니다. 자주 바뀌면 ISR, 요청 조건에 따라 달라지면 Dynamic Rendering을 고려한다.

Q. `generateStaticParams` 언제 써?

A.
Dynamic Route 중 빌드 시점에 미리 생성할 경로 목록을 알 수 있을 때 사용한다.

Q. 상품 상세가 수십만 개면 전부 `generateStaticParams`에 넣어?

A.
권장하지 않는다. 인기 경로만 사전 생성하고 나머지는 ISR 또는 on-demand generation을 검토한다.

Q. `generateStaticParams`는 Pages Router의 무엇과 비슷해?

A.
`getStaticPaths`와 비슷한 역할이다.

Q. `revalidatePath`와 `revalidateTag` 차이는?

A.
`revalidatePath`는 특정 경로를 갱신하고, `revalidateTag`는 같은 tag로 묶인 여러 캐시 항목을 갱신한다.

Q. `revalidatePath`는 언제 써?

A.
특정 페이지나 route path를 갱신해야 할 때 사용한다.

Q. `revalidateTag`는 언제 써?

A.
상품 목록과 상세처럼 여러 페이지에서 공유하는 데이터 묶음을 한 번에 갱신할 때 사용한다.

Q. Time-based Revalidation은 언제 써?

A.
데이터 변경 주기가 예측 가능하고 일정 시간 stale 상태를 허용할 수 있을 때 사용한다.

Q. On-demand Revalidation은 언제 써?

A.
CMS publish, 관리자 수정, 상품 변경처럼 이벤트 발생 시 즉시 캐시를 무효화해야 할 때 사용한다.

Q. CMS Webhook으로 ISR 갱신하려면?

A.
Webhook Route Handler에서 secret 또는 signature를 검증하고 `revalidatePath` 또는 `revalidateTag`를 호출한다.

Q. On-demand Revalidation endpoint는 공개해도 돼?

A.
안 된다. secret token, webhook signature, 인증 검증이 필요하다.

Q. ISR 데이터가 안 바뀌어. 무엇을 확인해?

A.
`revalidate`, `revalidatePath`, `revalidateTag`, fetch tag, mutation 후 invalidation, webhook 인증을 확인한다.

Q. Next.js Cache 때문에 데이터가 안 바뀌어. 무엇을 봐?

A.
Cache key, fetch cache option, tag, path revalidation, stale time, Router Cache를 확인한다.

Q. Static으로 예상했는데 Dynamic 됨. 왜?

A.
cookies, headers, searchParams, no-store, 사용자 세션 접근, dynamic route config가 원인일 수 있다.

Q. Dynamic이어야 하는데 캐시되는 것 같아. 왜?

A.
public cache 설정, fetch cache option, revalidate 설정, CDN Cache Header를 확인해야 한다.

Q. Build Time이 너무 김. 어떻게 해?

A.
모든 경로를 사전 생성하지 말고 인기 경로만 생성하거나 ISR / on-demand generation을 검토한다.

Q. SSG의 단점은?

A.
콘텐츠 변경 시 재빌드나 revalidation이 필요하고 경로 수가 많으면 빌드 시간이 길어질 수 있다.

Q. SSR의 단점은?

A.
요청마다 서버 렌더링 비용이 발생하고 TTFB가 느려질 수 있다.

Q. ISR의 단점은?

A.
Revalidation 설계가 필요하고 stale data 허용 범위와 cache invalidation을 관리해야 한다.

Q. Streaming은 언제 써?

A.
일부 데이터가 느리지만 페이지의 다른 영역은 먼저 보여줄 수 있을 때 사용한다.

Q. Streaming이 API를 빠르게 해?

A.
아니다. 느린 API 자체를 빠르게 하지는 않지만 준비된 UI를 먼저 보여줘 체감 성능을 개선한다.

Q. `loading.tsx`는 SSR SSG ISR과 어떤 관계야?

A.
Route Segment가 데이터를 기다리는 동안 fallback UI를 제공해 Streaming과 체감 성능 개선에 도움을 준다.

Q. PPR은 뭐야?

A.
Partial Prerendering은 정적 shell을 먼저 제공하고 일부 동적 영역을 요청 시점에 렌더링하는 전략이다.

Q. PPR은 언제 유용해?

A.
페이지 대부분은 정적이지만 장바구니, 알림, 추천처럼 일부 영역만 동적인 경우 유용하다.

Q. SSR은 SEO에 좋아?

A.
서버에서 HTML을 생성하므로 SEO에 유리할 수 있다. 다만 TTFB와 서버 부하도 함께 관리해야 한다.

Q. SSG는 SEO에 좋아?

A.
공개 콘텐츠를 정적 HTML로 제공할 수 있어 SEO와 성능에 유리하다.

Q. ISR에서 metadata도 갱신돼?

A.
콘텐츠와 metadata 생성 로직이 같은 revalidation 흐름에 연결되어야 최신 상태를 유지할 수 있다.

Q. Client-side Fetch만으로 SEO 콘텐츠를 보여줘도 돼?

A.
권장하지 않는다. SEO 핵심 콘텐츠는 서버 렌더링 결과에 포함되는 것이 좋다.

Q. SSG는 항상 빠른가?

A.
대체로 빠르지만 경로 수, CDN Cache, 리소스 크기, Hydration Cost에 따라 체감 성능은 달라질 수 있다.

Q. SSR은 항상 느린가?

A.
아니다. 최신성과 개인화가 필요한 경우 적합하며 데이터 병렬화와 cache 조합으로 성능을 개선할 수 있다.

Q. ISR은 언제 쓰면 안 돼?

A.
사용자별 민감 데이터, 초 단위 실시간 데이터, stale data 허용이 불가능한 데이터에는 부적합하다.

Q. Edge Runtime에서 ISR 가능해?

A.
Next.js 버전과 배포 플랫폼 지원 여부를 확인해야 한다. Runtime 제약은 반드시 검토해야 한다.

Q. Static Hosting만 가능하면 어떤 전략이 좋아?

A.
정적 export 가능한 SSG 중심 전략이 적합하다. SSR이나 ISR은 제한될 수 있다.

Q. Route Handler를 거쳐 내부 데이터를 fetch해야 해?

A.
항상 그럴 필요는 없다. Server Component에서 서버 로직을 직접 호출할 수 있다.

Q. Rendering Strategy 코드 리뷰에서 가장 중요한 것은?

A.
사용자별 데이터 여부, 공개 캐시 가능 여부, revalidation 필요 여부, SEO, TTFB, build time, 보안 위험을 확인하는 것이다.

Q. SSR / SSG / ISR RAG 문서 최종 목표는?

A.
Agent가 Next.js App Router 기반 프로젝트에서 페이지별 Static Rendering, Dynamic Rendering, Revalidation, Streaming 전략을 선택하고 Cache / SEO / 성능 / 보안 관점에서 리뷰하게 만드는 것이다.

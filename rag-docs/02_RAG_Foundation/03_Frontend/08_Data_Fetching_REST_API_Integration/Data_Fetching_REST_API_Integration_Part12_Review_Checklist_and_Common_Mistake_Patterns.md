# Data Fetching & REST API Integration Part12 - Review Checklist and Common Mistake Patterns

---

# 1. Final Review Overview

## 1.1 최종 검수 기본 개념

### [개념]

Final Review는 Frontend REST API Integration 코드가 Backend API 명세, Domain Rules, UI State, Error Handling, Security 기준과 일치하는지 최종 확인하는 과정이다.

Frontend Agent는 API 연동 코드를 생성한 뒤 URL, Method, Params, Body, Header, Response Mapping, Loading / Error / Empty UI, TanStack Query, CORS / Auth, File Upload, Pagination 기준을 전체적으로 검수해야 한다.

기본 Flow:

```text
API Spec 확인
→ API Function 검수
→ Axios Instance 검수
→ Request Mapping 검수
→ Response Mapping 검수
→ UI State 검수
→ Error Handling 검수
→ Network Debug 기준 검수
→ Security 기준 검수
→ Final Checklist 통과
```

---

### [핵심]

Final Review 핵심 키워드:

- API Review
- REST API Integration Review
- API Layer Review
- Axios Instance Review
- Request Mapping Review
- Response Mapping Review
- DTO Mapping Review
- UI State Review
- Error Handling Review
- TanStack Query Review
- Pagination Review
- File Upload Review
- CORS Review
- Auth Error Review
- Network Debugging Review
- Security Review
- Common Mistake Pattern
- Final Checklist

최종 검수 목적:

- API 경로 오류 방지
- Method 오류 방지
- Params / Body 혼동 방지
- Header 누락 방지
- Response Shape Mismatch 방지
- Loading / Error / Empty 누락 방지
- 인증 API 오류 방지
- Pagination / Infinite Scroll 오류 방지
- File Upload 오류 방지
- CORS / 401 / 403 문제 진단 가능
- Frontend Agent 코드 품질 안정화

---

### [실무]

2026 실무 기준에서 Data Fetching 코드는 다음 기준을 통과해야 한다.

```text
1. Component에서 URL을 직접 작성하지 않는다.
2. API Function이 도메인별 파일로 분리되어 있다.
3. Axios Instance가 publicApi / authApi로 분리되어 있다.
4. 인증 필요 API는 authApi를 사용한다.
5. GET 요청은 params를 사용한다.
6. POST / PUT / PATCH 요청은 request body를 사용한다.
7. File Upload는 FormData를 사용한다.
8. Response Wrapper 처리 기준이 일관된다.
9. Page / Slice / Cursor Response를 구분한다.
10. Loading / Error / Empty / Success UI를 구분한다.
11. TanStack Query queryKey에 params / id / page가 포함된다.
12. Mutation 성공 후 관련 Query를 invalidate한다.
13. Network 탭 기준으로 디버깅 가능하다.
14. token 원문과 민감정보를 로그로 남기지 않는다.
```

---

### [FAQ]

Q. Final Review는 왜 필요해?
A. API 연동은 작은 경로, Header, Response Mapping 오류만으로도 화면 전체가 깨질 수 있으므로 최종 검수가 필요하다.

Q. API 연동 코드에서 가장 먼저 검수할 것은 뭐야?
A. Request URL, Method, Params / Body, Authorization Header, Response Body mapping을 먼저 확인한다.

Q. Final Review는 코드 작성 전이야 후야?
A. API 명세 확인은 작성 전, Network와 UI 검수는 작성 후에 수행한다.

Q. Final Review의 최종 기준은 뭐야?
A. 실제 Browser Network Request / Response와 UI State가 API 명세와 일치하는 것이다.

---

# 2. API Spec Review Checklist

## 2.1 Backend API 명세 검수

### [개념]

API Spec Review는 Frontend API Function 작성 전에 Backend API 명세를 읽고 요청 / 응답 기준을 확정하는 과정이다.

Frontend Agent는 API 명세 없이 추측으로 URL, Method, DTO, Header를 만들지 않아야 한다.

---

### [핵심]

확인 대상:

- Base URL
- API Prefix
- Endpoint Path
- HTTP Method
- Path Variable
- Query Parameter
- Request Body
- Request Header
- Response Body
- Status Code
- Auth Required
- Role Required
- Pagination Type
- File Upload Type
- Error Response Shape

API Spec 검수 질문:

```md
- [ ] Endpoint URL이 무엇인가?
- [ ] HTTP Method가 무엇인가?
- [ ] 인증이 필요한가?
- [ ] 어떤 Axios Instance를 사용해야 하는가?
- [ ] Path Variable이 있는가?
- [ ] Query Parameter가 있는가?
- [ ] Request Body가 있는가?
- [ ] multipart/form-data가 필요한가?
- [ ] Response Wrapper가 있는가?
- [ ] Page / Slice / Cursor 응답인가?
- [ ] Error Response 구조가 무엇인가?
```

---

### [실무]

API 명세 예:

```text
GET /api/festivals/search
Auth: Public
Query Params: keyword, regionCode, themeCode, page, size, sort
Response: ApiResponse<PageResponse<FestivalSummaryResponse>>
```

Frontend 변환:

```typescript
export async function searchFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals/search", {
    params: cleanParams(params),
  });

  return response.data.data;
}
```

인증 API 명세 예:

```text
POST /api/reviews
Auth: Required
Body: ReviewCreateRequest
Response: ApiResponse<ReviewResponse>
```

Frontend 변환:

```typescript
export async function createReview(
  requestBody: ReviewCreateRequest,
): Promise<ReviewResponse> {
  const response = await authApi.post<ApiResponse<ReviewResponse>>(
    "/reviews",
    requestBody,
  );

  return response.data.data;
}
```

---

### [FAQ]

Q. API 명세에서 가장 먼저 봐야 할 것은 뭐야?
A. URL, Method, 인증 필요 여부, Request 구조, Response 구조를 먼저 확인해야 한다.

Q. API 명세가 없으면 어떻게 해?
A. Swagger, Backend Controller, Network Response, Backend 개발자 확인을 통해 기준을 확정해야 한다.

Q. Auth Required는 왜 중요해?
A. publicApi와 authApi 선택, Authorization Header 포함 여부가 달라지기 때문이다.

Q. Response Type은 어디서 확정해?
A. Backend DTO와 실제 Network Response Body를 함께 보고 확정한다.

---

# 3. API Layer Review Checklist

## 3.1 API Layer 구조 검수

### [개념]

API Layer Review는 API Function, Axios Instance, Domain API File, Custom Hook, Query Hook의 역할이 분리되었는지 확인하는 과정이다.

Component가 API URL, Method, Header 세부사항을 직접 알지 않는 구조가 권장된다.

---

### [핵심]

검수 대상:

- `axiosInstance.ts`
- `publicApi`
- `authApi`
- Domain API File
- API Function Naming
- API Function Return
- API Path Management
- Custom Hook
- Query Hook
- Component Dependency

Checklist:

```md
- [ ] Component에 API URL이 직접 작성되어 있지 않은가?
- [ ] API Function이 도메인별 파일에 있는가?
- [ ] API Function 이름이 도메인 동작을 표현하는가?
- [ ] publicApi / authApi가 분리되어 있는가?
- [ ] Axios Instance가 baseURL / timeout을 관리하는가?
- [ ] authApi interceptor가 Authorization Header를 추가하는가?
- [ ] API Function이 UI setState를 직접 호출하지 않는가?
- [ ] Hook이 API Function을 호출하고 UI State를 관리하는가?
```

---

### [실무]

좋은 구조:

```text
Component
→ useFestivalQuery
→ getFestivals
→ publicApi
→ Backend API
```

나쁜 구조:

```tsx
function FestivalListPage() {
  useEffect(() => {
    axios.get("http://localhost:8080/api/festivals").then((response) => {
      setFestivals(response.data.data.content);
    });
  }, []);
}
```

수정 방향:

```typescript
export async function getFestivals(params: FestivalSearchParams) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data;
}
```

Component:

```tsx
const { data, isLoading, error } = useFestivalQuery(params);
```

---

### [FAQ]

Q. Component에서 API URL을 직접 쓰면 왜 안 좋아?
A. URL, Method, Header, Response Mapping이 화면마다 중복되어 유지보수와 디버깅이 어려워진다.

Q. API Function은 어디에 둬?
A. `src/api/festivalApi.ts`, `src/api/reviewApi.ts`처럼 도메인별 API 파일에 둔다.

Q. API Function에서 setState를 해도 돼?
A. 권장하지 않는다. API Function은 데이터를 반환하고 상태 관리는 Hook이나 Component가 담당한다.

Q. API Layer Review의 핵심은 뭐야?
A. Component, Hook, API Function, Axios Instance의 책임이 섞이지 않았는지 확인하는 것이다.

---

# 4. Request Review Checklist

## 4.1 Request URL / Method / Params / Body 검수

### [개념]

Request Review는 Frontend가 Backend에 보내는 HTTP Request가 API 명세와 정확히 일치하는지 확인하는 과정이다.

URL, Method, Path Variable, Query Parameter, Request Body, Header 중 하나만 틀려도 API 오류가 발생할 수 있다.

---

### [핵심]

검수 대상:

- Request URL
- HTTP Method
- Base URL
- API Prefix
- Path Variable
- Query Parameter
- Request Body
- Request Header
- Content-Type
- FormData
- Authorization Header

Checklist:

```md
- [ ] baseURL이 올바른가?
- [ ] /api prefix가 중복되지 않았는가?
- [ ] Endpoint path가 Backend Mapping과 일치하는가?
- [ ] Path Variable이 undefined / null이 아닌가?
- [ ] GET 요청은 params를 사용하는가?
- [ ] POST / PUT / PATCH 요청은 body를 사용하는가?
- [ ] DELETE 요청의 body 필요 여부를 명세로 확인했는가?
- [ ] JSON 요청에 Content-Type이 필요한가?
- [ ] File Upload는 FormData를 사용하는가?
- [ ] 인증 API에 Authorization Header가 포함되는가?
```

---

### [실무]

GET Params 검수:

```typescript
publicApi.get("/festivals/search", {
  params: {
    keyword,
    page: 0,
    size: 20,
  },
});
```

POST Body 검수:

```typescript
authApi.post("/reviews", {
  festivalId: 1,
  rating: 5,
  content: "좋았어요",
});
```

Path Variable 검수:

```typescript
export async function getFestivalDetail(festivalId: number) {
  assertRequired(festivalId, "festivalId");

  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

Network 검수 Flow:

```text
Network Request 클릭
→ Request URL 확인
→ Method 확인
→ Query String 확인
→ Payload 확인
→ Request Headers 확인
```

---

### [FAQ]

Q. Request Review에서 가장 흔한 오류는?
A. URL prefix 중복, Method 불일치, params/body 혼동, Authorization Header 누락이다.

Q. GET 요청에 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 Query Parameter로 보내는 것이 일반적이다.

Q. Path Variable undefined는 어떻게 막아?
A. API 함수 호출 전 route param을 검증하거나 API 함수 내부에서 assertRequired를 사용한다.

Q. Request가 맞는지 최종 확인은 어디서 해?
A. 브라우저 Network 탭의 실제 Request URL, Method, Payload, Headers에서 확인한다.

---

# 5. Response Review Checklist

## 5.1 Response DTO / Wrapper / Mapping 검수

### [개념]

Response Review는 Backend 응답 구조와 Frontend API Function 반환 구조, Component 접근 경로가 일치하는지 확인하는 과정이다.

Response Shape Mismatch는 화면 데이터 오류의 대표 원인이다.

---

### [핵심]

검수 대상:

- Response Body
- ApiResponse Wrapper
- `response.data`
- `response.data.data`
- Page Response
- Slice Response
- Cursor Response
- content 위치
- nullable field
- date string
- enum value
- nested object
- Error Response
- TypeScript Type

Checklist:

```md
- [ ] 실제 Response Body를 Network 탭에서 확인했는가?
- [ ] ApiResponse Wrapper가 있는가?
- [ ] API Function return 기준이 일관되는가?
- [ ] Page Response의 content 위치를 확인했는가?
- [ ] Slice Response의 hasNext / last를 확인했는가?
- [ ] null 가능 필드를 Type에 반영했는가?
- [ ] 날짜 필드는 string으로 처리하는가?
- [ ] enum value와 label mapping을 구분했는가?
- [ ] Error Response 구조를 확인했는가?
- [ ] Component 접근 경로가 실제 응답과 일치하는가?
```

---

### [실무]

Response Wrapper 검수:

```json
{
  "success": true,
  "message": "조회 성공",
  "data": {
    "content": [],
    "number": 0,
    "totalPages": 0
  }
}
```

API Function 반환:

```typescript
const response = await publicApi.get<
  ApiResponse<PageResponse<FestivalSummaryResponse>>
>("/festivals", { params });

return response.data.data;
```

Component 접근:

```typescript
const pageData = await getFestivals(params);

setItems(pageData.content);
setTotalPages(pageData.totalPages);
```

문제 패턴:

```text
API Function이 response.data 반환
Component가 response.data.data.content 기대
→ 접근 경로 불일치
```

---

### [FAQ]

Q. Response Review에서 가장 중요한 것은 뭐야?
A. 실제 Network Response Body와 API Function return, Component 접근 경로가 일치하는지 확인하는 것이다.

Q. response.data.data가 항상 맞아?
A. 아니다. Backend Wrapper와 Axios Interceptor unwrap 기준에 따라 달라진다.

Q. Page Response에서 목록 배열은 어디에 있어?
A. 보통 `content` 필드에 있다.

Q. map is not a function은 어떤 검수에서 잡아?
A. Response Review에서 배열인지 Page 객체인지 content 위치를 확인하면 잡을 수 있다.

---

# 6. UI State Review Checklist

## 6.1 Loading / Error / Empty / Success 검수

### [개념]

UI State Review는 API 요청 생명주기에 따라 화면이 Loading, Error, Empty, Success 상태를 올바르게 보여주는지 확인하는 과정이다.

API 요청이 성공해도 데이터가 없으면 Error가 아니라 Empty State로 처리해야 한다.

---

### [핵심]

검수 대상:

- Initial Loading
- Refetch Loading
- Submit Loading
- Error State
- Empty State
- Success State
- Field Error
- Global Error
- Retry Button
- Button Disabled
- Skeleton
- Spinner
- Accessibility

Checklist:

```md
- [ ] 최초 로딩 UI가 있는가?
- [ ] 재조회 로딩 UI가 필요한가?
- [ ] Error State와 Empty State를 구분하는가?
- [ ] 요청 실패 시 loading이 종료되는가?
- [ ] finally에서 loading false 처리하는가?
- [ ] Submit 중 버튼이 disabled 되는가?
- [ ] 중복 제출을 handler에서도 막는가?
- [ ] Field Error와 Global Error를 구분하는가?
- [ ] Retry Button이 같은 요청을 다시 실행하는가?
- [ ] Error 객체 전체를 화면에 노출하지 않는가?
- [ ] Empty State에 사용자 다음 행동이 있는가?
```

---

### [실무]

검수 대상 코드:

```tsx
if (isLoading) {
  return <FestivalListSkeleton />;
}

if (error) {
  return (
    <ErrorState message={getApiErrorMessage(error)} onRetry={() => refetch()} />
  );
}

if (!data || data.content.length === 0) {
  return <EmptyState title="검색 결과가 없습니다." />;
}

return <FestivalList festivals={data.content} />;
```

Submit Loading:

```tsx
<button type="submit" disabled={mutation.isPending}>
  {mutation.isPending ? "작성 중..." : "작성"}
</button>
```

검수 Flow:

```text
느린 네트워크 테스트
→ Loading UI 확인
→ 성공 응답 확인
→ 빈 배열 응답 확인
→ 실패 응답 확인
→ 중복 클릭 확인
```

---

### [FAQ]

Q. UI State Review에서 가장 중요한 것은 뭐야?
A. Loading, Error, Empty, Success를 명확히 구분하고 실패 시 loading이 종료되는지 확인하는 것이다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. API 요청이 성공했다면 Empty State다.

Q. Submit 버튼 disabled만 하면 충분해?
A. 대부분 가능하지만 handler에서도 submitting guard를 두면 중복 제출을 더 안전하게 막을 수 있다.

Q. Error 객체를 그대로 보여줘도 돼?
A. 안 된다. 사용자에게 안전한 메시지로 변환해서 보여주는 것이 좋다.

---

# 7. TanStack Query Review Checklist

## 7.1 Query / Mutation / Cache 검수

### [개념]

TanStack Query Review는 queryKey, queryFn, mutationFn, invalidation, enabled, staleTime, infinite query가 API Layer와 올바르게 연결되어 있는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- QueryClient
- QueryClientProvider
- queryKey
- queryFn
- useQuery
- useMutation
- invalidateQueries
- enabled
- select
- staleTime
- useInfiniteQuery
- getNextPageParam
- hasNextPage
- isLoading / isFetching
- isPending

Checklist:

```md
- [ ] QueryClientProvider가 App 상단에 있는가?
- [ ] queryKey에 resource name이 포함되는가?
- [ ] queryKey에 id / params / page / size / sort가 포함되는가?
- [ ] queryFn이 API Function을 호출하는가?
- [ ] queryFn과 queryKey 인자가 일치하는가?
- [ ] undefined id는 enabled로 방지하는가?
- [ ] mutationFn이 API Function을 사용하는가?
- [ ] mutation 성공 후 관련 query를 invalidate하는가?
- [ ] invalidate queryKey가 실제 queryKey와 일치하는가?
- [ ] isLoading과 isFetching을 구분하는가?
- [ ] useInfiniteQuery에서 pages를 flatMap하는가?
```

---

### [실무]

좋은 queryKey:

```typescript
useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

나쁜 queryKey:

```typescript
useQuery({
  queryKey: ["festivals"],
  queryFn: () => getFestivals(params),
});
```

Mutation invalidation:

```typescript
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: (_, variables) => {
    queryClient.invalidateQueries({
      queryKey: ["reviews", variables.festivalId],
    });
  },
});
```

Infinite Query 검수:

```typescript
const items = query.data?.pages.flatMap((page) => page.content) ?? [];
```

---

### [FAQ]

Q. TanStack Query Review에서 가장 흔한 오류는?
A. queryKey에 params나 page를 빠뜨리거나 mutation 후 invalidate를 하지 않는 것이다.

Q. queryKey와 queryFn 인자가 다르면 어떻게 돼?
A. Cache와 실제 요청 데이터가 불일치해 화면이 갱신되지 않거나 잘못된 데이터가 보일 수 있다.

Q. undefined id API 호출은 어떻게 막아?
A. `enabled: Boolean(id)` 또는 명시적 조건으로 query 실행을 제어한다.

Q. mutation 후 목록이 안 바뀌면 뭘 확인해?
A. invalidateQueries 대상 queryKey가 실제 목록 queryKey와 일치하는지 확인한다.

---

# 8. Pagination / Infinite Scroll Review Checklist

## 8.1 목록 분할 조회 검수

### [개념]

Pagination / Infinite Scroll Review는 Page / Slice / Cursor Response를 기준으로 목록 교체, append, page reset, duplicate request prevention이 정상 동작하는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- Page Response
- Slice Response
- Cursor Response
- page
- size
- sort
- content
- totalPages
- totalElements
- hasNext
- last
- nextCursor
- append
- replace
- reset
- loadingMore
- duplicate request

Checklist:

```md
- [ ] Page / Slice / Cursor Response를 구분하는가?
- [ ] UI page 1-based와 Backend page 0-based를 변환하는가?
- [ ] queryKey에 page / size / sort / filter가 포함되는가?
- [ ] 검색 조건 변경 시 page를 reset하는가?
- [ ] size 변경 시 page를 reset하는가?
- [ ] sort 변경 시 page를 reset하는가?
- [ ] Pagination은 content를 교체하는가?
- [ ] Load More / Infinite Scroll은 content를 append하는가?
- [ ] loadingMore 중복 요청을 막는가?
- [ ] hasNext false 또는 last true면 추가 요청을 중단하는가?
- [ ] Cursor 방식에서 nextCursor를 갱신하는가?
```

---

### [실무]

Pagination 검수:

```typescript
const backendPage = uiPage - 1;

const pageData = await getFestivals({
  ...params,
  page: backendPage,
  size: 20,
});

setItems(pageData.content);
```

Load More 검수:

```typescript
setItems((prev) => [...prev, ...sliceData.content]);
setHasNext(sliceData.hasNext);
setPage(sliceData.number + 1);
```

Reset 검수:

```typescript
function handleSearch(nextParams: FestivalSearchParams) {
  setSubmittedParams({
    ...nextParams,
    page: 0,
  });

  setUiPage(1);
}
```

문제 패턴:

```text
검색 조건 변경 후 빈 화면
→ 기존 page 번호 유지
→ page reset 누락
```

---

### [FAQ]

Q. Pagination Review에서 가장 중요한 것은?
A. UI page와 Backend page 변환, queryKey page 포함, 검색 조건 변경 시 page reset이다.

Q. Infinite Scroll Review에서 가장 중요한 것은?
A. content append, loadingMore guard, hasNext 기준, page / cursor 갱신이다.

Q. 더보기에서 기존 목록이 사라지면 뭐가 문제야?
A. append가 아니라 replace로 처리했을 가능성이 높다.

Q. 같은 데이터가 반복되면 뭘 확인해?
A. page 증가, nextCursor 갱신, 중복 요청 방지, key 중복 여부를 확인한다.

---

# 9. File Upload Review Checklist

## 9.1 파일 업로드 검수

### [개념]

File Upload Review는 File Input, Validation, FormData, multipart request, Upload UI State, Response Mapping, Security 기준이 올바르게 적용되었는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- File Input
- File Object
- FileList
- FormData
- multipart/form-data
- FormData key
- Backend multipart field name
- File Size Validation
- File Type Validation
- Preview URL
- revokeObjectURL
- Upload Loading
- Upload Progress
- Upload Response DTO
- File Delete
- Security

Checklist:

```md
- [ ] File 객체를 input files에서 얻는가?
- [ ] 파일 크기 검증이 있는가?
- [ ] 파일 타입 / 확장자 검증이 있는가?
- [ ] Backend 검증이 필요하다는 기준이 명시되었는가?
- [ ] FormData를 사용하는가?
- [ ] FormData key가 Backend field name과 일치하는가?
- [ ] 여러 파일은 같은 key로 append하는가?
- [ ] multipart Content-Type을 수동 고정하지 않는가?
- [ ] 업로드 중 버튼 disabled가 있는가?
- [ ] preview URL을 revoke하는가?
- [ ] previewUrl과 server imageUrl을 구분하는가?
- [ ] 업로드 응답의 imageId / imageUrl을 mapping하는가?
```

---

### [실무]

FormData 검수:

```typescript
const formData = new FormData();

files.forEach((file) => {
  formData.append("images", file);
});
```

Network 검수:

```text
Network
→ Request Payload
→ Form Data
→ images: File
→ Content-Type: multipart/form-data; boundary=...
```

Preview cleanup:

```typescript
useEffect(() => {
  if (!file) {
    return;
  }

  const previewUrl = URL.createObjectURL(file);

  return () => {
    URL.revokeObjectURL(previewUrl);
  };
}, [file]);
```

문제 패턴:

```text
Backend MultipartFile null
→ FormData key와 @RequestPart name 불일치
```

---

### [FAQ]

Q. File Upload Review에서 가장 흔한 오류는?
A. FormData key와 Backend multipart field name 불일치, Content-Type boundary 문제다.

Q. 파일 업로드가 실패하면 어디서 확인해?
A. Network 탭의 Form Data, Content-Type, Authorization Header, Response Body를 확인한다.

Q. previewUrl을 서버에 저장해도 돼?
A. 안 된다. previewUrl은 브라우저 임시 URL이고 서버 imageUrl이나 imageId와 다르다.

Q. Frontend 파일 검증만으로 충분해?
A. 아니다. Frontend 검증은 UX용이고 Backend 검증이 최종 기준이다.

---

# 10. CORS / Auth Review Checklist

## 10.1 CORS / 401 / 403 검수

### [개념]

CORS / Auth Review는 Browser 환경에서 CORS, Preflight, Authorization Header, 401, 403, Token Refresh, Cookie Credentials가 의도대로 처리되는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- Origin
- OPTIONS Preflight
- CORS Response Header
- Authorization Header
- Bearer Token
- publicApi / authApi
- 401 Unauthorized
- 403 Forbidden
- Token Refresh
- Cookie Credentials
- Route Guard
- Backend API Auth
- Security Logging

Checklist:

```md
- [ ] Browser Network에서 OPTIONS 요청을 확인할 수 있는가?
- [ ] Access-Control-Allow-Origin이 올바른가?
- [ ] Access-Control-Allow-Headers에 Authorization이 포함되는가?
- [ ] credentials 사용 시 Allow-Credentials와 Origin이 올바른가?
- [ ] 인증 필요 API가 authApi를 사용하는가?
- [ ] Authorization Header가 Bearer 형식인가?
- [ ] 401과 403을 구분해 처리하는가?
- [ ] token 만료 시 refresh 또는 logout 기준이 있는가?
- [ ] Route Guard와 Backend API Auth를 구분하는가?
- [ ] token 원문을 로그에 남기지 않는가?
```

---

### [실무]

401 검수:

```text
Network Request Headers
→ Authorization: Bearer <token>
→ 없으면 authApi / interceptor 확인
```

403 검수:

```text
Authorization Header 존재
→ 403 발생
→ role / permission / owner 확인
```

CORS 검수:

```text
OPTIONS Request
→ Access-Control-Allow-Origin 확인
→ Access-Control-Allow-Headers 확인
→ Access-Control-Allow-Methods 확인
```

문제 패턴:

```text
Postman 성공 / Browser 실패
→ CORS 가능성 우선 확인
```

---

### [FAQ]

Q. CORS / Auth Review에서 가장 먼저 볼 것은?
A. Browser Network 탭의 OPTIONS 요청, 실제 API 요청, Authorization Header, Status Code를 본다.

Q. token은 있는데 401이면?
A. 실제 Request Header에 Authorization이 포함되었는지, Bearer 형식이 맞는지 확인한다.

Q. 403이면 token 문제야?
A. 보통 인증은 되었지만 권한이 부족한 문제다. role, permission, owner 정책을 확인한다.

Q. Postman 성공인데 Browser 실패면?
A. CORS, Authorization Header, credentials, Browser Origin 정책을 확인해야 한다.

---

# 11. Error Handling Review Checklist

## 11.1 Error Mapping / Error UI 검수

### [개념]

Error Handling Review는 API Error를 사용자에게 안전한 메시지로 변환하고, 개발자가 디버깅할 수 있는 정보는 별도로 관리하는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- AxiosError
- Status Code
- Error Response Body
- Error Mapper
- Field Error
- Global Error
- Retry UI
- Unauthorized Handling
- Forbidden Handling
- Network Error
- Timeout
- Server Error
- Sensitive Info Exposure

Checklist:

```md
- [ ] Error 객체 전체를 화면에 노출하지 않는가?
- [ ] Status Code별 사용자 메시지를 제공하는가?
- [ ] 400 / 422 field error를 input 근처에 표시하는가?
- [ ] 401 로그인 필요 메시지 또는 refresh flow가 있는가?
- [ ] 403 권한 없음 메시지를 제공하는가?
- [ ] 404 Not Found UI가 있는가?
- [ ] 500 일반 서버 오류 메시지를 제공하는가?
- [ ] Network Error와 Timeout 메시지를 구분하는가?
- [ ] Retry 가능한 오류에 Retry Button이 있는가?
- [ ] token / 개인정보를 로그에 남기지 않는가?
```

---

### [실무]

Error Mapper:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (status === 401) {
      return "로그인이 필요합니다.";
    }

    if (status === 403) {
      return "접근 권한이 없습니다.";
    }

    if (status === 404) {
      return "요청한 데이터를 찾을 수 없습니다.";
    }

    if (status && status >= 500) {
      return "서버 오류가 발생했습니다.";
    }

    if (!error.response) {
      return "네트워크 연결을 확인해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Field Error:

```typescript
export function getFieldErrors(error: unknown): Record<string, string> {
  if (axios.isAxiosError<ApiErrorResponse>(error)) {
    return error.response?.data?.errors ?? {};
  }

  return {};
}
```

---

### [FAQ]

Q. Error Handling Review에서 가장 중요한 것은?
A. 사용자 메시지와 개발 로그를 구분하고 Status Code별로 적절한 UI를 제공하는 것이다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 민감한 정보가 포함될 수 있으므로 안전한 일반 메시지를 보여준다.

Q. Validation Error는 어떻게 검수해?
A. Response Body의 errors 구조와 field error UI 연결을 확인한다.

Q. Network Error는 Status Code로 처리해?
A. response가 없을 수 있으므로 error.response 존재 여부를 먼저 확인한다.

---

# 12. Security Review Checklist

## 12.1 Data Fetching 보안 검수

### [개념]

Security Review는 API 연동 과정에서 token, 사용자 정보, 파일, 환경변수, 권한 검증이 안전하게 처리되는지 확인하는 과정이다.

Frontend 보안 처리는 UX와 노출 방지를 돕지만 최종 보안 검증은 Backend가 담당한다.

---

### [핵심]

검수 대상:

- Access Token
- Refresh Token
- Authorization Header
- localStorage
- Cookie
- HttpOnly Cookie
- Frontend env
- API Secret
- File Upload
- User Role
- Route Guard
- Permission UI
- Error Logging
- Sensitive Payload

Checklist:

```md
- [ ] token 원문을 console.log로 남기지 않는가?
- [ ] Authorization Header를 오류 보고서에 원문으로 포함하지 않는가?
- [ ] Frontend env에 secret key를 넣지 않는가?
- [ ] API Key가 public key인지 secret key인지 구분하는가?
- [ ] Route Guard를 실제 보안으로 착각하지 않는가?
- [ ] Backend 권한 검증이 필요하다는 기준이 있는가?
- [ ] File Upload는 Backend 검증이 필요하다는 기준이 있는가?
- [ ] 사용자 개인정보를 Error Log에 남기지 않는가?
- [ ] logout 시 민감 query cache를 정리하는가?
- [ ] 공개 API와 인증 API를 구분하는가?
```

---

### [실무]

나쁜 로그:

```typescript
console.log("accessToken", accessToken);
console.log("Authorization", config.headers.Authorization);
```

나은 로그:

```typescript
console.log("auth request debug", {
  url: config.url,
  method: config.method,
  hasAuthorization: Boolean(config.headers.Authorization),
});
```

Frontend env 주의:

```text
VITE_API_BASE_URL → 가능
REACT_APP_API_BASE_URL → 가능
SECRET_API_KEY → 금지
PRIVATE_KEY → 금지
```

권한 기준:

```text
Frontend button hidden → UX
Backend permission check → Security
```

---

### [FAQ]

Q. Frontend env에 secret을 넣어도 돼?
A. 안 된다. Frontend env 값은 빌드 결과에 포함될 수 있으므로 secret을 넣으면 안 된다.

Q. token을 로그로 찍으면 왜 위험해?
A. token이 노출되면 API 요청을 도용당할 수 있다.

Q. Route Guard가 있으면 Backend 권한 검증은 없어도 돼?
A. 아니다. Route Guard는 UX용이고 Backend 권한 검증이 최종 보안이다.

Q. logout 시 query cache를 지워야 해?
A. 사용자 민감 데이터가 cache에 남을 수 있으므로 clear 또는 관련 query remove를 고려한다.

---

# 13. Network Debug Review Checklist

## 13.1 Network 기준 최종 검수

### [개념]

Network Debug Review는 실제 브라우저 요청이 기대한 대로 발생하는지 확인하는 최종 검수 단계다.

코드상으로 맞아 보여도 Network Request가 다르면 실제 동작은 실패한다.

---

### [핵심]

Network 최종 확인 항목:

- Request 발생 여부
- Request URL
- Request Method
- Status Code
- Query String Parameters
- Request Payload
- Form Data
- Request Headers
- Authorization Header
- Content-Type
- Response Body
- Response Headers
- Timing
- CORS Header

Checklist:

```md
- [ ] 요청이 실제로 발생하는가?
- [ ] Request URL이 기대와 일치하는가?
- [ ] Request Method가 기대와 일치하는가?
- [ ] Query String Parameters가 기대와 일치하는가?
- [ ] Request Payload가 Backend DTO와 일치하는가?
- [ ] Authorization Header가 필요한 요청에 포함되는가?
- [ ] File Upload는 Form Data로 보이는가?
- [ ] Status Code가 기대와 일치하는가?
- [ ] Response Body가 Type과 일치하는가?
- [ ] CORS Header가 필요한 경우 포함되는가?
```

---

### [실무]

Network 검수 Flow:

```text
Page Action
→ Network Request 발생 확인
→ Request URL / Method 확인
→ Header / Payload 확인
→ Status Code 확인
→ Response Body 확인
→ UI State 확인
```

문제 분류:

```text
Request 없음
→ Event Handler / enabled / useEffect 조건 확인

Request URL 틀림
→ baseURL / path / params 확인

Status 401
→ Authorization Header 확인

Status 403
→ Role / Permission 확인

Status 200인데 화면 빈 값
→ Response Mapping / Component 접근 확인
```

---

### [FAQ]

Q. 코드가 맞아 보이는데 안 되면?
A. Network 탭에서 실제 Request / Response가 코드 의도와 일치하는지 확인해야 한다.

Q. 요청 자체가 안 나가면?
A. Event Handler, useEffect 조건, TanStack Query enabled, button disabled 상태를 확인한다.

Q. 200인데 화면에 데이터가 없어?
A. Response Body와 API Function return, Component 접근 경로가 일치하는지 확인한다.

Q. Network 검수는 언제 해?
A. API Function 작성 후 실제 화면에서 동작을 확인할 때 반드시 수행한다.

---

# 14. Common Mistake Pattern Catalog

## 14.1 공통 실수 패턴 모음

### [개념]

Common Mistake Pattern Catalog는 Data Fetching & REST API Integration에서 반복적으로 발생하는 실수를 증상, 원인, 해결 방향으로 정리한 목록이다.

Frontend Agent는 오류 발생 시 이 패턴 목록을 우선 검색하여 원인을 빠르게 좁혀야 한다.

---

### [핵심]

패턴 형식:

```text
증상
→ 원인 후보
→ 확인 위치
→ 해결 방향
```

주요 패턴 그룹:

- URL Pattern
- Method Pattern
- Params Pattern
- Body Pattern
- Header Pattern
- Response Pattern
- UI State Pattern
- Query Pattern
- Pagination Pattern
- File Upload Pattern
- CORS Pattern
- Auth Pattern
- Security Pattern

---

### [실무]

URL Pattern:

```text
증상: 404 Not Found
원인: /api prefix 중복 또는 누락
확인: Network Request URL
해결: baseURL과 API path prefix 기준 통일
```

Method Pattern:

```text
증상: 405 Method Not Allowed
원인: Backend는 POST인데 Frontend가 GET 요청
확인: Network Request Method, Backend Mapping
해결: API Function의 axios method 수정
```

Params Pattern:

```text
증상: 검색 결과가 이상함
원인: Query Parameter 누락 또는 page 변환 오류
확인: Network Query String Parameters
해결: params 옵션과 UI page → backend page 변환 확인
```

Response Pattern:

```text
증상: map is not a function
원인: PageResponse 객체를 배열로 처리
확인: Network Response Body
해결: pageData.content 사용
```

Auth Pattern:

```text
증상: 로그인했는데 401
원인: authApi 대신 publicApi 사용 또는 Authorization Header 누락
확인: API Function, Network Request Headers
해결: authApi 사용 및 interceptor 확인
```

File Upload Pattern:

```text
증상: Backend MultipartFile null
원인: FormData key와 Backend @RequestPart name 불일치
확인: Network Form Data, Backend API Spec
해결: formData.append key 수정
```

---

### [FAQ]

Q. Common Mistake Pattern은 언제 써?
A. API 오류의 증상은 보이지만 원인이 명확하지 않을 때 우선 검색한다.

Q. 404가 나면 무조건 URL 문제야?
A. URL 문제일 수 있지만 Resource 없음, Method 불일치, SPA fallback 문제도 함께 확인해야 한다.

Q. 200인데 화면이 안 나오면 어떤 패턴이야?
A. Response Shape Mismatch, API Function return 불일치, Component 접근 경로 오류일 가능성이 높다.

Q. 로그인 후 401은 어떤 패턴이야?
A. Authorization Header 누락, authApi 선택 오류, token 만료, Bearer 형식 오류 패턴을 확인한다.

---

# 15. Review Report Template

## 15.1 API Review Report 기준

### [개념]

API Review Report는 특정 API 연동 코드가 검수를 통과했는지 기록하는 문서 형식이다.

Frontend Agent는 복잡한 API 연동을 리뷰할 때 Request, Response, UI State, Error Handling, Security 기준을 짧게 요약할 수 있어야 한다.

---

### [핵심]

Report 포함 항목:

- API Name
- Endpoint
- Method
- Auth Required
- API Function
- Request Mapping
- Response Mapping
- UI State
- Error Handling
- TanStack Query
- Security
- Network Verification
- Issues
- Fix Recommendation
- Final Result

---

### [실무]

Review Report Template:

```md
# API Review Report

## API

- Name:
- Endpoint:
- Method:
- Auth Required:
- Axios Instance:

## Request Review

- Path Variable:
- Query Parameter:
- Request Body:
- Header:

## Response Review

- Response Type:
- Wrapper:
- Mapping:
- Nullable Fields:

## UI State Review

- Loading:
- Error:
- Empty:
- Success:

## Query Review

- queryKey:
- queryFn:
- mutationFn:
- invalidate:

## Network Verification

- Request URL:
- Request Method:
- Status Code:
- Response Body Checked:

## Issues

- Issue 1:
- Issue 2:

## Fix Recommendation

- Recommendation 1:
- Recommendation 2:

## Final Result

- PASS / NEEDS_FIX
```

간단 예:

```md
# API Review Report

## API

- Name: createReview
- Endpoint: /api/reviews
- Method: POST
- Auth Required: true
- Axios Instance: authApi

## Request Review

- Body: ReviewCreateRequest
- Header: Authorization Bearer Token required

## Response Review

- Response Type: ApiResponse<ReviewResponse>
- Mapping: response.data.data

## Issues

- None

## Final Result

- PASS
```

---

### [FAQ]

Q. API Review Report는 언제 작성해?
A. 복잡한 API 연동, 오류 수정, 리뷰 단계에서 작성하면 좋다.

Q. 모든 API마다 Report가 필요해?
A. 필수는 아니지만 중요한 인증, 결제, 파일 업로드, 복잡한 목록 API는 작성하는 것이 좋다.

Q. Report에서 가장 중요한 항목은?
A. Endpoint, Method, Auth Required, Request Mapping, Response Mapping, Network Verification이다.

Q. Final Result는 어떻게 표시해?
A. 문제가 없으면 PASS, 수정 필요하면 NEEDS_FIX로 표시할 수 있다.

---

# 16. Final Integration Checklist

## 16.1 Data Fetching 전체 최종 Checklist

### [개념]

Final Integration Checklist는 Data Fetching & REST API Integration 문서 세트 전체를 기준으로 Frontend Agent가 API 연동 코드를 최종 검수하는 체크리스트다.

---

### [핵심]

전체 Checklist:

```md
# Data Fetching & REST API Integration Final Checklist

## REST API Basics

- [ ] HTTP Method와 URL이 Backend 명세와 일치한다.
- [ ] Path Variable / Query Parameter / Request Body를 구분한다.
- [ ] Status Code별 의미를 구분한다.
- [ ] JSON Request / Response 구조를 확인한다.

## fetch / Axios

- [ ] fetch 사용 시 response.ok를 확인한다.
- [ ] Axios 사용 시 response.data 구조를 확인한다.
- [ ] Axios params와 body 위치를 구분한다.
- [ ] fetch / Axios Error Handling 기준이 있다.

## Axios Instance

- [ ] publicApi / authApi가 분리되어 있다.
- [ ] baseURL / timeout이 설정되어 있다.
- [ ] authApi interceptor가 Authorization Header를 추가한다.
- [ ] response interceptor가 error를 삼키지 않는다.

## API Layer

- [ ] Component에 API URL을 직접 작성하지 않는다.
- [ ] Domain API File에 API Function을 둔다.
- [ ] API Function 이름이 도메인 동작을 표현한다.
- [ ] API Function에서 UI setState를 직접 호출하지 않는다.

## DTO Mapping

- [ ] Request Type과 Response Type을 분리한다.
- [ ] ApiResponse Wrapper를 처리한다.
- [ ] Page / Slice / Cursor Response를 구분한다.
- [ ] Nullable / Date / Enum / Nested Object를 처리한다.

## UI State

- [ ] Loading / Error / Empty / Success를 구분한다.
- [ ] Submit Loading과 중복 제출 방지 기준이 있다.
- [ ] Field Error와 Global Error를 구분한다.
- [ ] Error 객체 전체를 화면에 노출하지 않는다.

## TanStack Query

- [ ] queryKey에 id / params / page / size / sort가 포함된다.
- [ ] queryFn은 API Function을 호출한다.
- [ ] mutationFn은 API Function을 호출한다.
- [ ] mutation 성공 후 관련 query를 invalidate한다.
- [ ] enabled로 undefined id 요청을 방지한다.

## Pagination / Infinite Scroll

- [ ] UI page와 Backend page를 변환한다.
- [ ] 검색 조건 변경 시 page를 reset한다.
- [ ] Load More / Infinite Scroll은 content를 append한다.
- [ ] loadingMore와 hasNext로 중복 요청을 방지한다.

## File Upload

- [ ] File Input에서 File 객체를 얻는다.
- [ ] 파일 크기 / 타입 / 개수를 검증한다.
- [ ] FormData key와 Backend field name이 일치한다.
- [ ] previewUrl과 server imageUrl을 구분한다.
- [ ] preview URL cleanup을 수행한다.

## Troubleshooting

- [ ] Network 탭에서 Request / Response를 확인한다.
- [ ] URL / Method / Params / Body / Header를 검수한다.
- [ ] Status Code와 Response Body를 함께 확인한다.
- [ ] Response Shape Mismatch를 분석할 수 있다.

## CORS / Auth

- [ ] OPTIONS Preflight를 확인할 수 있다.
- [ ] Authorization Header Bearer 형식을 확인한다.
- [ ] 401과 403을 구분한다.
- [ ] publicApi / authApi 선택이 올바르다.
- [ ] token 원문을 로그에 남기지 않는다.

## Security

- [ ] Frontend env에 secret을 넣지 않는다.
- [ ] Route Guard와 Backend Auth를 구분한다.
- [ ] File Upload Backend 검증이 필요함을 인지한다.
- [ ] 민감정보를 로그 / 보고서에 노출하지 않는다.
```

---

### [실무]

최종 검수 Flow:

```text
API Spec
→ API Layer
→ Request
→ Response
→ UI State
→ Query / Mutation
→ Pagination / File Upload
→ CORS / Auth
→ Security
→ Network Verification
→ PASS or NEEDS_FIX
```

최종 판단 기준:

```text
PASS:
- API 명세와 실제 요청 / 응답이 일치
- UI State가 정상 작동
- Error Handling 기준 통과
- Network 검수 완료
- 보안상 치명적 노출 없음

NEEDS_FIX:
- URL / Method / Header 오류
- Response Mapping 불일치
- Loading / Error / Empty 누락
- 인증 / 권한 처리 오류
- token / secret 노출
```

---

### [FAQ]

Q. Final Integration Checklist는 언제 사용해?
A. API 연동 기능 구현 후 최종 리뷰 단계에서 사용한다.

Q. Checklist를 모두 통과하면 완성으로 봐도 돼?
A. 기본적인 API 연동 품질은 확보되지만, 실제 사용자 시나리오와 Backend Log까지 함께 확인하는 것이 좋다.

Q. NEEDS_FIX는 어떤 경우야?
A. URL, Method, Header, Response Mapping, UI State, Auth, Security 기준에 문제가 있으면 NEEDS_FIX다.

Q. 최종 PASS 기준은 뭐야?
A. 실제 Network Request / Response와 UI 동작이 API 명세와 일치하고 보안상 치명적 노출이 없는 상태다.

---

# 17. Part12 Checklist

## 17.1 Review Checklist and Common Mistake Patterns 검수 기준

### [개념]

Part12 Review Checklist and Common Mistake Patterns 문서는 Data Fetching & REST API Integration 문서 세트의 최종 검수 문서다.

Frontend Agent가 API 연동 코드를 생성한 뒤 전체 품질을 점검하고, 반복 실수 패턴을 빠르게 찾도록 만드는 것이 목적이다.

---

### [핵심]

Checklist:

```md
- [ ] Final Review Overview가 포함되었는가?
- [ ] API Spec Review Checklist가 포함되었는가?
- [ ] API Layer Review Checklist가 포함되었는가?
- [ ] Request Review Checklist가 포함되었는가?
- [ ] Response Review Checklist가 포함되었는가?
- [ ] UI State Review Checklist가 포함되었는가?
- [ ] TanStack Query Review Checklist가 포함되었는가?
- [ ] Pagination / Infinite Scroll Review Checklist가 포함되었는가?
- [ ] File Upload Review Checklist가 포함되었는가?
- [ ] CORS / Auth Review Checklist가 포함되었는가?
- [ ] Error Handling Review Checklist가 포함되었는가?
- [ ] Security Review Checklist가 포함되었는가?
- [ ] Network Debug Review Checklist가 포함되었는가?
- [ ] Common Mistake Pattern Catalog가 포함되었는가?
- [ ] Review Report Template이 포함되었는가?
- [ ] Final Integration Checklist가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part12 최종 검수 Flow:

```text
Draft
→ Checklist Coverage Check
→ Domain Rule Alignment Check
→ Common Mistake Pattern Check
→ Final Integration Checklist Check
→ Retrieval Query Check
→ Fatal Issue Check
→ Final Review
```

최종 기준:

- API 연동 전체 검수 가능
- 반복 실수 패턴 검색 가능
- API Review Report 작성 가능
- Final Integration Checklist로 PASS / NEEDS_FIX 판단 가능
- Frontend Agent가 Data Fetching REST API Integration 결과물을 최종 리뷰 가능
- Data Fetching & REST API Integration 문서 세트 종료 가능

---

### [FAQ]

Q. Part12의 목적은 뭐야?
A. Data Fetching & REST API Integration 전체 문서 세트를 마무리하는 최종 검수 체크리스트와 실수 패턴 문서다.

Q. Part12에서 가장 중요한 기준은 뭐야?
A. API Spec, Request, Response, UI State, Query, Auth, Security를 한 번에 검수할 수 있는 Final Integration Checklist다.

Q. Part12 이후에 이 도메인은 완료로 봐도 돼?
A. 기존 Part01~Part11까지 완료되었다면 Part12는 최종 리뷰 문서이므로 이 도메인 문서 세트를 완료로 볼 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Final Review는 왜 필요해?
A. API 연동은 작은 경로, Header, Response Mapping 오류만으로도 화면 전체가 깨질 수 있으므로 최종 검수가 필요하다.

Q. API 연동 코드에서 가장 먼저 검수할 것은 뭐야?
A. Request URL, Method, Params / Body, Authorization Header, Response Body mapping을 먼저 확인한다.

Q. Final Review는 코드 작성 전이야 후야?
A. API 명세 확인은 작성 전, Network와 UI 검수는 작성 후에 수행한다.

Q. Final Review의 최종 기준은 뭐야?
A. 실제 Browser Network Request / Response와 UI State가 API 명세와 일치하는 것이다.

Q. API 명세에서 가장 먼저 봐야 할 것은 뭐야?
A. URL, Method, 인증 필요 여부, Request 구조, Response 구조를 먼저 확인해야 한다.

Q. API 명세가 없으면 어떻게 해?
A. Swagger, Backend Controller, Network Response, Backend 개발자 확인을 통해 기준을 확정해야 한다.

Q. Auth Required는 왜 중요해?
A. publicApi와 authApi 선택, Authorization Header 포함 여부가 달라지기 때문이다.

Q. Response Type은 어디서 확정해?
A. Backend DTO와 실제 Network Response Body를 함께 보고 확정한다.

Q. Component에서 API URL을 직접 쓰면 왜 안 좋아?
A. URL, Method, Header, Response Mapping이 화면마다 중복되어 유지보수와 디버깅이 어려워진다.

Q. API Function은 어디에 둬?
A. `src/api/festivalApi.ts`, `src/api/reviewApi.ts`처럼 도메인별 API 파일에 둔다.

Q. API Function에서 setState를 해도 돼?
A. 권장하지 않는다. API Function은 데이터를 반환하고 상태 관리는 Hook이나 Component가 담당한다.

Q. API Layer Review의 핵심은 뭐야?
A. Component, Hook, API Function, Axios Instance의 책임이 섞이지 않았는지 확인하는 것이다.

Q. Request Review에서 가장 흔한 오류는?
A. URL prefix 중복, Method 불일치, params/body 혼동, Authorization Header 누락이다.

Q. GET 요청에 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 Query Parameter로 보내는 것이 일반적이다.

Q. Path Variable undefined는 어떻게 막아?
A. API 함수 호출 전 route param을 검증하거나 API 함수 내부에서 assertRequired를 사용한다.

Q. Request가 맞는지 최종 확인은 어디서 해?
A. 브라우저 Network 탭의 실제 Request URL, Method, Payload, Headers에서 확인한다.

Q. Response Review에서 가장 중요한 것은 뭐야?
A. 실제 Network Response Body와 API Function return, Component 접근 경로가 일치하는지 확인하는 것이다.

Q. response.data.data가 항상 맞아?
A. 아니다. Backend Wrapper와 Axios Interceptor unwrap 기준에 따라 달라진다.

Q. Page Response에서 목록 배열은 어디에 있어?
A. 보통 `content` 필드에 있다.

Q. map is not a function은 어떤 검수에서 잡아?
A. Response Review에서 배열인지 Page 객체인지 content 위치를 확인하면 잡을 수 있다.

Q. UI State Review에서 가장 중요한 것은 뭐야?
A. Loading, Error, Empty, Success를 명확히 구분하고 실패 시 loading이 종료되는지 확인하는 것이다.

Q. 검색 결과가 없으면 Error State야?
A. 아니다. API 요청이 성공했다면 Empty State다.

Q. Submit 버튼 disabled만 하면 충분해?
A. 대부분 가능하지만 handler에서도 submitting guard를 두면 중복 제출을 더 안전하게 막을 수 있다.

Q. Error 객체를 그대로 보여줘도 돼?
A. 안 된다. 사용자에게 안전한 메시지로 변환해서 보여주는 것이 좋다.

Q. TanStack Query Review에서 가장 흔한 오류는?
A. queryKey에 params나 page를 빠뜨리거나 mutation 후 invalidate를 하지 않는 것이다.

Q. queryKey와 queryFn 인자가 다르면 어떻게 돼?
A. Cache와 실제 요청 데이터가 불일치해 화면이 갱신되지 않거나 잘못된 데이터가 보일 수 있다.

Q. undefined id API 호출은 어떻게 막아?
A. `enabled: Boolean(id)` 또는 명시적 조건으로 query 실행을 제어한다.

Q. mutation 후 목록이 안 바뀌면 뭘 확인해?
A. invalidateQueries 대상 queryKey가 실제 목록 queryKey와 일치하는지 확인한다.

Q. Pagination Review에서 가장 중요한 것은?
A. UI page와 Backend page 변환, queryKey page 포함, 검색 조건 변경 시 page reset이다.

Q. Infinite Scroll Review에서 가장 중요한 것은?
A. content append, loadingMore guard, hasNext 기준, page / cursor 갱신이다.

Q. 더보기에서 기존 목록이 사라지면 뭐가 문제야?
A. append가 아니라 replace로 처리했을 가능성이 높다.

Q. 같은 데이터가 반복되면 뭘 확인해?
A. page 증가, nextCursor 갱신, 중복 요청 방지, key 중복 여부를 확인한다.

Q. File Upload Review에서 가장 흔한 오류는?
A. FormData key와 Backend multipart field name 불일치, Content-Type boundary 문제다.

Q. 파일 업로드가 실패하면 어디서 확인해?
A. Network 탭의 Form Data, Content-Type, Authorization Header, Response Body를 확인한다.

Q. previewUrl을 서버에 저장해도 돼?
A. 안 된다. previewUrl은 브라우저 임시 URL이고 서버 imageUrl이나 imageId와 다르다.

Q. Frontend 파일 검증만으로 충분해?
A. 아니다. Frontend 검증은 UX용이고 Backend 검증이 최종 기준이다.

Q. CORS / Auth Review에서 가장 먼저 볼 것은?
A. Browser Network 탭의 OPTIONS 요청, 실제 API 요청, Authorization Header, Status Code를 본다.

Q. token은 있는데 401이면?
A. 실제 Request Header에 Authorization이 포함되었는지, Bearer 형식이 맞는지 확인한다.

Q. 403이면 token 문제야?
A. 보통 인증은 되었지만 권한이 부족한 문제다. role, permission, owner 정책을 확인한다.

Q. Postman 성공인데 Browser 실패면?
A. CORS, Authorization Header, credentials, Browser Origin 정책을 확인해야 한다.

Q. Error Handling Review에서 가장 중요한 것은?
A. 사용자 메시지와 개발 로그를 구분하고 Status Code별로 적절한 UI를 제공하는 것이다.

Q. 서버 에러 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 민감한 정보가 포함될 수 있으므로 안전한 일반 메시지를 보여준다.

Q. Validation Error는 어떻게 검수해?
A. Response Body의 errors 구조와 field error UI 연결을 확인한다.

Q. Network Error는 Status Code로 처리해?
A. response가 없을 수 있으므로 error.response 존재 여부를 먼저 확인한다.

Q. Frontend env에 secret을 넣어도 돼?
A. 안 된다. Frontend env 값은 빌드 결과에 포함될 수 있으므로 secret을 넣으면 안 된다.

Q. token을 로그로 찍으면 왜 위험해?
A. token이 노출되면 API 요청을 도용당할 수 있다.

Q. Route Guard가 있으면 Backend 권한 검증은 없어도 돼?
A. 아니다. Route Guard는 UX용이고 Backend 권한 검증이 최종 보안이다.

Q. logout 시 query cache를 지워야 해?
A. 사용자 민감 데이터가 cache에 남을 수 있으므로 clear 또는 관련 query remove를 고려한다.

Q. 코드가 맞아 보이는데 안 되면?
A. Network 탭에서 실제 Request / Response가 코드 의도와 일치하는지 확인해야 한다.

Q. 요청 자체가 안 나가면?
A. Event Handler, useEffect 조건, TanStack Query enabled, button disabled 상태를 확인한다.

Q. 200인데 화면에 데이터가 없어?
A. Response Body와 API Function return, Component 접근 경로가 일치하는지 확인한다.

Q. Network 검수는 언제 해?
A. API Function 작성 후 실제 화면에서 동작을 확인할 때 반드시 수행한다.

Q. Common Mistake Pattern은 언제 써?
A. API 오류의 증상은 보이지만 원인이 명확하지 않을 때 우선 검색한다.

Q. 404가 나면 무조건 URL 문제야?
A. URL 문제일 수 있지만 Resource 없음, Method 불일치, SPA fallback 문제도 함께 확인해야 한다.

Q. 200인데 화면이 안 나오면 어떤 패턴이야?
A. Response Shape Mismatch, API Function return 불일치, Component 접근 경로 오류일 가능성이 높다.

Q. 로그인 후 401은 어떤 패턴이야?
A. Authorization Header 누락, authApi 선택 오류, token 만료, Bearer 형식 오류 패턴을 확인한다.

Q. API Review Report는 언제 작성해?
A. 복잡한 API 연동, 오류 수정, 리뷰 단계에서 작성하면 좋다.

Q. 모든 API마다 Report가 필요해?
A. 필수는 아니지만 중요한 인증, 결제, 파일 업로드, 복잡한 목록 API는 작성하는 것이 좋다.

Q. Report에서 가장 중요한 항목은?
A. Endpoint, Method, Auth Required, Request Mapping, Response Mapping, Network Verification이다.

Q. Final Result는 어떻게 표시해?
A. 문제가 없으면 PASS, 수정 필요하면 NEEDS_FIX로 표시할 수 있다.

Q. Final Integration Checklist는 언제 사용해?
A. API 연동 기능 구현 후 최종 리뷰 단계에서 사용한다.

Q. Checklist를 모두 통과하면 완성으로 봐도 돼?
A. 기본적인 API 연동 품질은 확보되지만, 실제 사용자 시나리오와 Backend Log까지 함께 확인하는 것이 좋다.

Q. NEEDS_FIX는 어떤 경우야?
A. URL, Method, Header, Response Mapping, UI State, Auth, Security 기준에 문제가 있으면 NEEDS_FIX다.

Q. 최종 PASS 기준은 뭐야?
A. 실제 Network Request / Response와 UI 동작이 API 명세와 일치하고 보안상 치명적 노출이 없는 상태다.

Q. Part12 Review Checklist and Common Mistake Patterns의 목적은 뭐야?
A. Data Fetching & REST API Integration 전체 문서 세트를 마무리하는 최종 검수 체크리스트와 실수 패턴 문서다.

Q. Part12 이후에 이 도메인은 완료로 봐도 돼?
A. 기존 Part01~Part11까지 완료되었다면 Part12는 최종 리뷰 문서이므로 이 도메인 문서 세트를 완료로 볼 수 있다.

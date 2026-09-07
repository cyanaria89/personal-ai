# React Router Part03 Params SearchParams

---

# 1. Route Parameters and Search Params

## 1.1 Purpose

### [개념]

React Router에서 Route Parameter와 Search Params는 URL에서 값을 읽어 Page Component 동작을 결정하는 핵심 구조다.

Route Parameter는 특정 리소스를 식별하는 값이고 Search Params는 검색, 필터, 정렬, 페이지 같은 선택 조건을 표현하는 값이다.

이 문서는 Frontend Agent가 Dynamic Route, useParams, Query String, useSearchParams를 안정적으로 구현하고 URL 상태 설계를 검토하도록 지원한다.

---

### [핵심]

- Dynamic Route
- Route Parameter
- Path Parameter
- useParams
- Query String
- Search Params
- useSearchParams
- URLSearchParams
- Resource Identity
- Filter State
- Search State
- Pagination State
- Type Conversion
- Undefined Guard
- URL State
- Bookmarkable URL

기본 선택 기준:

```text
Resource Identity
→ Path Parameter

Search / Filter / Sort / Page
→ Query String

Temporary Navigation Data
→ Navigation State
```

---

### [실무]

2026 실무 기준에서 URL 상태 설계는 단순 문자열 처리가 아니다.

실무에서 URL은 아래 역할을 수행한다.

- 상세 페이지 리소스 식별
- 목록 검색 조건 유지
- 필터 상태 공유
- 페이지네이션 상태 유지
- 새로고침 후 상태 복원
- 뒤로가기 / 앞으로가기 UX 유지
- 링크 공유 가능성 제공
- API 요청 parameter 구성 기준 제공

예:

```text
/festivals/123
→ festivalId = 123
→ 특정 축제 상세 페이지

/festivals?keyword=꽃&region=seoul&page=2
→ keyword = 꽃
→ region = seoul
→ page = 2
→ 축제 목록 검색 상태
```

URL State 설계 Flow:

```text
User Page Requirement
→ Identify Resource ID
→ Define Path Parameter
→ Identify Search / Filter Conditions
→ Define Query String
→ Read Params in Page Component
→ Validate and Convert Type
→ Request API
→ Render Result
```

---

### [FAQ]

Q. Route Parameter와 Search Params는 왜 필요해?
A. URL에서 리소스 ID, 검색 조건, 필터 조건, 페이지 번호를 읽어 화면과 API 요청을 결정하기 위해 필요하다.

Q. ID는 Path Parameter와 Query String 중 어디에 둬?
A. 특정 리소스를 식별하는 ID는 일반적으로 Path Parameter가 적합하다.

Q. 검색 조건은 Path Parameter와 Query String 중 어디에 둬?
A. 검색, 필터, 정렬, 페이지 조건은 Query String이 적합하다.

Q. React Router에서 URL 값을 읽을 때 중요한 점은?
A. URL에서 읽은 값은 문자열이며 undefined 가능성이 있으므로 검증과 타입 변환이 필요하다.

---

# 2. Dynamic Route

## 2.1 Dynamic Route Concept

### [개념]

Dynamic Route는 URL 일부를 변수처럼 받는 Route다.

React Router에서는 path에 `:paramName` 형식을 사용해 Path Parameter를 정의한다.

---

### [핵심]

- Dynamic Route
- Path Parameter
- Route Parameter
- `:paramName`
- Detail Page
- Resource ID
- useParams
- String Value
- Undefined Guard
- Type Conversion

기본 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

동작:

```text
URL: /festivals/123
Route Pattern: /festivals/:festivalId
festivalId: "123"
```

---

### [실무]

Dynamic Route는 상세 페이지에서 가장 자주 사용된다.

예:

```text
/users/:userId
/posts/:postId
/festivals/:festivalId
/products/:productId
/orders/:orderId
```

축제 상세 Route 예:

```jsx
<Routes>
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
</Routes>
```

실무 기준:

- 특정 리소스 상세는 Dynamic Route 사용
- param 이름은 도메인 의미가 드러나게 작성
- `:id`보다 `:festivalId`, `:userId`, `:postId`처럼 명확한 이름 권장
- Route path와 useParams key 이름 일치
- Link URL은 실제 값으로 생성
- API 요청 전 param 검증
- 숫자 ID는 Number 변환 후 NaN 확인

---

### [FAQ]

Q. Dynamic Route는 뭐야?
A. URL 일부를 변수처럼 받는 Route다. 예: `/festivals/:festivalId`.

Q. `:festivalId`는 무슨 뜻이야?
A. URL의 해당 위치 값을 festivalId라는 이름의 Path Parameter로 받겠다는 뜻이다.

Q. 상세 페이지 path는 어떻게 잡아?
A. 일반적으로 `/resources/:resourceId` 형태를 사용한다. 예: `/festivals/:festivalId`.

Q. `:id`와 `:festivalId` 중 뭐가 좋아?
A. 작은 예제는 `:id`도 가능하지만 실무 문서와 Agent 출력에서는 `:festivalId`처럼 의미 있는 이름이 좋다.

---

## 2.2 Dynamic Route Link Generation

### [개념]

Dynamic Route pattern은 Route 정의용이고 실제 이동 URL은 값이 채워진 path여야 한다.

예를 들어 `/festivals/:festivalId`는 Route pattern이고 `/festivals/123`은 실제 URL이다.

---

### [핵심]

- Route Pattern
- Actual URL
- Link to
- Path Builder
- Dynamic Value
- Route Constants
- Parameter Name Consistency
- Undefined ID Guard

구분:

```text
Route Pattern
→ /festivals/:festivalId

Actual URL
→ /festivals/123
```

---

### [실무]

Route 정의:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

잘못된 Link:

```jsx
<Link to="/festivals/:festivalId">Detail</Link>
```

문제:

```text
실제 URL이 /festivals/:festivalId로 이동함
festivalId 값이 123으로 채워지지 않음
```

올바른 Link:

```jsx
<Link to={`/festivals/${festival.festivalId}`}>{festival.title}</Link>
```

path builder 권장:

```javascript
export function createFestivalDetailPath(festivalId) {
  return `/festivals/${festivalId}`;
}
```

사용:

```jsx
<Link to={createFestivalDetailPath(festival.festivalId)}>{festival.title}</Link>
```

실무 주의:

- id 값이 undefined인 상태에서 URL 생성 금지
- path builder 함수로 URL 생성 기준 통일
- Route Constants의 pattern과 실제 URL 생성 함수를 분리
- 목록 데이터의 ID 필드명과 Route param 이름 정합성 유지

---

### [FAQ]

Q. `/festivals/:festivalId`를 Link to에 그대로 넣어도 돼?
A. 안 된다. Link에는 `/festivals/123`처럼 실제 값이 들어간 URL을 넣어야 한다.

Q. Dynamic Route URL은 어떻게 만들어?
A. template string이나 path builder 함수를 사용해 실제 ID 값을 넣어 만든다.

Q. path builder 함수는 왜 필요해?
A. URL 생성 기준을 통일하고 오타와 undefined URL 생성을 줄이기 위해 필요하다.

Q. Link URL에 undefined가 들어가면 왜 그래?
A. 상세 URL 생성 시 필요한 ID 값이 아직 없거나 필드명이 잘못되었을 가능성이 있다.

---

# 3. useParams

## 3.1 useParams Concept

### [개념]

useParams는 현재 매칭된 Dynamic Route의 Path Parameter 값을 읽는 React Router Hook이다.

useParams로 읽은 값은 문자열이며 param이 없으면 undefined일 수 있다.

---

### [핵심]

- useParams
- Path Parameter Read
- Dynamic Route Match
- string value
- undefined 가능성
- Number conversion
- NaN check
- Param Name Match
- Detail Page
- API Request Parameter

기본 예:

```jsx
import { useParams } from "react-router";

function FestivalDetailPage() {
  const { festivalId } = useParams();

  return <p>{festivalId}</p>;
}
```

---

### [실무]

상세 페이지 예:

```jsx
import { useParams } from "react-router";

function FestivalDetailPage() {
  const { festivalId } = useParams();

  if (!festivalId) {
    return <p>Invalid festival id.</p>;
  }

  const parsedFestivalId = Number(festivalId);

  if (Number.isNaN(parsedFestivalId)) {
    return <p>Invalid festival id.</p>;
  }

  return <FestivalDetail festivalId={parsedFestivalId} />;
}
```

API 요청 예:

```jsx
function FestivalDetailPage() {
  const { festivalId } = useParams();
  const parsedFestivalId = Number(festivalId);

  if (!festivalId || Number.isNaN(parsedFestivalId)) {
    return <NotFoundPage />;
  }

  return <FestivalDetailContainer festivalId={parsedFestivalId} />;
}
```

실무 기준:

- useParams 값은 문자열로 취급
- 숫자 ID는 Number 변환
- 변환 후 Number.isNaN 확인
- param 누락 시 NotFoundPage 또는 Error UI 처리
- API 요청 전에 param 검증
- Route path param 이름과 useParams key 이름 통일
- TypeScript 사용 시 타입 정의와 undefined 처리

---

### [FAQ]

Q. useParams는 뭐야?
A. 현재 Dynamic Route에서 Path Parameter 값을 읽는 React Router Hook이다.

Q. useParams 값은 number야 string이야?
A. 문자열이다. 숫자 ID로 쓰려면 Number로 변환해야 한다.

Q. useParams가 undefined일 수 있어?
A. 가능하다. Route path에 param이 없거나 param 이름이 맞지 않으면 undefined가 될 수 있다.

Q. useParams 값으로 바로 API 호출해도 돼?
A. 숫자 ID가 필요하면 변환과 검증 후 API 호출하는 것이 안전하다.

---

## 3.2 Param Name Consistency

### [개념]

Param Name Consistency는 Route path에 정의한 param 이름과 useParams에서 꺼내는 key 이름을 일치시키는 규칙이다.

이름이 다르면 useParams 값이 undefined가 될 수 있다.

---

### [핵심]

- Param Name
- Route path
- useParams key
- Naming Consistency
- undefined problem
- Dynamic Route Debug
- Detail Page Error

나쁜 예:

```jsx
<Route path="/festivals/:id" element={<FestivalDetailPage />} />;

function FestivalDetailPage() {
  const { festivalId } = useParams();
}
```

문제:

```text
Route param name: id
useParams key: festivalId
결과: festivalId undefined
```

좋은 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />;

function FestivalDetailPage() {
  const { festivalId } = useParams();
}
```

---

### [실무]

실무 naming 기준:

```text
Route path
→ /festivals/:festivalId

useParams
→ const { festivalId } = useParams();

API
→ getFestivalDetail(festivalId)

Component props
→ <FestivalDetail festivalId={parsedFestivalId} />
```

권장:

- param 이름은 도메인 ID 이름과 맞춤
- Entity / API / DTO에서 사용하는 ID 의미와 최대한 일치
- `id`, `festivalId`, `festival_id` 혼용 금지
- JavaScript 변수는 camelCase 사용
- URL path segment는 소문자 리소스명 사용
- Route Constants와 path builder도 동일 naming 기준 사용

Debug Flow:

```text
useParams undefined
→ Current URL 확인
→ Route path 확인
→ param name 확인
→ useParams key 확인
→ Link actual URL 확인
→ Nested Route 위치 확인
```

---

### [FAQ]

Q. useParams가 undefined인 가장 흔한 이유는?
A. Route path의 param 이름과 useParams에서 꺼내는 key 이름이 다르기 때문이다.

Q. Route는 `:id`인데 useParams에서 festivalId로 꺼낼 수 있어?
A. 안 된다. Route가 `:id`면 useParams에서도 `id`로 꺼내야 한다.

Q. param 이름은 어떻게 정하는 게 좋아?
A. `festivalId`, `userId`, `postId`처럼 도메인 의미가 드러나는 이름이 좋다.

Q. param 이름과 API parameter 이름도 맞추는 게 좋아?
A. 가능하면 맞추는 것이 Agent 코드 생성과 유지보수에 유리하다.

---

## 3.3 Params Undefined Problem

### [개념]

Params Undefined Problem은 useParams에서 기대한 Path Parameter 값이 undefined로 나오는 문제다.

Route path, Link URL, param 이름, 중첩 Route 구조가 원인일 수 있다.

---

### [핵심]

문제:

- festivalId가 undefined
- userId가 undefined
- 상세 API URL에 undefined 포함
- Number(undefined)로 NaN 발생
- NotFoundPage로 이동
- API 400 / 404 발생

원인:

- Route path에 param 없음
- param 이름 불일치
- Link URL 생성 오류
- Dynamic Route pattern을 실제 URL로 사용
- 중첩 Route 위치 오류
- optional param 처리 누락
- Router 외부에서 잘못 렌더링

---

### [실무]

문제 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />

<Link to="/festivals">Detail</Link>
```

문제:

```text
/festivals에는 festivalId 값이 없음
FestivalDetailPage가 /festivals/:festivalId에서 렌더링되지 않음
```

문제 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />

<Link to={`/festivals/${festival.id}`}>
  Detail
</Link>
```

확인:

```text
festival.id가 실제 데이터에 존재하는가?
실제 필드명이 festival.festivalId인가?
```

Debug Flow:

```text
Params Undefined
→ Current URL 확인
→ Route pattern 확인
→ Link actual URL 확인
→ param name 확인
→ useParams key 확인
→ data id field 확인
→ Nested Route 구조 확인
→ NotFound / Error UI 처리 확인
```

방어 코드:

```jsx
const { festivalId } = useParams();

if (!festivalId) {
  return <NotFoundPage />;
}
```

---

### [FAQ]

Q. useParams가 undefined인 이유는?
A. Route path에 해당 param이 없거나 param 이름이 맞지 않거나 Link URL이 잘못되었을 수 있다.

Q. 상세 API 요청 URL에 undefined가 들어가?
A. useParams 값이 없거나 Link URL 생성에 필요한 ID 값이 undefined일 가능성이 있다.

Q. Number(undefined)는 어떻게 돼?
A. NaN이 된다. Number 변환 후 Number.isNaN으로 검증해야 한다.

Q. params undefined 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, Route pattern, Link URL, param 이름, useParams key를 순서대로 확인한다.

---

# 4. Query String

## 4.1 Query String Concept

### [개념]

Query String은 URL에서 `?key=value` 형태로 검색 조건, 필터 조건, 정렬 조건, 페이지 번호 같은 선택 상태를 표현하는 방식이다.

React Router에서는 useSearchParams로 Query String을 읽고 수정할 수 있다.

---

### [핵심]

- Query String
- Search Params
- URLSearchParams
- key value
- filter state
- search keyword
- sort state
- pagination state
- bookmarkable URL
- refresh persistence
- back button UX

예:

```text
/festivals?keyword=꽃&region=seoul&page=2&sort=latest
```

값:

```text
keyword = 꽃
region = seoul
page = 2
sort = latest
```

---

### [실무]

Query String 사용 상황:

- 검색어
- 지역 필터
- 카테고리 필터
- 날짜 필터
- 정렬 기준
- 페이지 번호
- 탭 상태
- 목록 view mode
- 공개 가능한 화면 상태

예:

```text
/festivals?keyword=music
/festivals?region=seoul
/festivals?category=flower&page=1
/festivals?startDate=2026-07-01&endDate=2026-07-31
/festivals?sort=popular&page=3
```

실무 장점:

- URL 공유 가능
- 새로고침 후 상태 유지
- 뒤로가기 / 앞으로가기 복원
- 검색 결과 링크 전달 가능
- 서버 API query parameter와 매핑 쉬움

주의:

- Query String 값은 문자열
- 숫자와 boolean은 변환 필요
- 빈 값 처리 기준 필요
- 민감정보 저장 금지
- 지나치게 복잡한 객체 상태 저장 금지
- URL 길이와 가독성 고려

---

### [FAQ]

Q. Query String은 뭐야?
A. URL에서 `?keyword=spring&page=1`처럼 검색 조건이나 옵션을 표현하는 부분이다.

Q. 검색 조건은 왜 Query String으로 둬?
A. URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하기 때문이다.

Q. Query String 값은 문자열이야?
A. 그렇다. 숫자와 boolean 값은 직접 변환해야 한다.

Q. Query String에 민감정보를 넣어도 돼?
A. 안 된다. URL에 노출되고 공유될 수 있으므로 민감정보를 넣지 않는다.

---

## 4.2 Query String Design Rules

### [개념]

Query String Design은 목록 화면의 검색, 필터, 정렬, 페이지 상태를 URL에 일관되게 표현하는 규칙이다.

Agent가 API 요청 parameter와 화면 상태를 안정적으로 연결하기 위해 필요하다.

---

### [핵심]

Query key 예:

- `keyword`
- `region`
- `category`
- `theme`
- `startDate`
- `endDate`
- `page`
- `size`
- `sort`
- `tab`

설계 기준:

```text
Search Keyword
→ keyword

Filter
→ region / category / theme

Date Range
→ startDate / endDate

Pagination
→ page / size

Sorting
→ sort

Tab State
→ tab
```

---

### [실무]

축제 검색 URL 예:

```text
/festivals?keyword=꽃&region=seoul&theme=spring&page=1&sort=popular
```

React 화면 상태:

```text
keyword: "꽃"
region: "seoul"
theme: "spring"
page: 1
sort: "popular"
```

API 요청 예:

```text
GET /api/festivals?keyword=꽃&region=seoul&theme=spring&page=1&sort=popular
```

실무 기준:

- Query key naming 통일
- URL query key와 API parameter naming 최대한 일치
- 빈 문자열은 URL에서 제거하는 방식 권장
- 검색 조건 변경 시 page는 1로 reset
- page 기본값 정의
- sort 기본값 정의
- 날짜 포맷 통일
- 배열 필터 표현 방식 통일

빈 값 처리 예:

```text
keyword=""
→ query string에서 keyword 제거

region=""
→ query string에서 region 제거
```

---

### [FAQ]

Q. Query key 이름은 어떻게 정해?
A. keyword, region, category, page, sort처럼 의미가 명확하고 API parameter와 맞추기 쉬운 이름을 사용한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 일반적으로 page를 1로 reset한다.

Q. 빈 검색어도 Query String에 남겨?
A. 보통 빈 값은 제거해 URL을 깔끔하게 유지한다.

Q. URL query key와 API parameter 이름을 맞추는 게 좋아?
A. 가능하면 맞추는 것이 코드 생성, 디버깅, 유지보수에 유리하다.

---

# 5. useSearchParams

## 5.1 useSearchParams Concept

### [개념]

useSearchParams는 현재 URL의 Query String을 읽고 수정하는 React Router Hook이다.

searchParams.get으로 값을 읽고 setSearchParams로 Query String을 변경한다.

---

### [핵심]

- useSearchParams
- searchParams
- setSearchParams
- URLSearchParams
- get
- set
- delete
- query string update
- navigation 발생
- string value
- type conversion

기본 예:

```jsx
import { useSearchParams } from "react-router";

function FestivalSearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();

  const keyword = searchParams.get("keyword") ?? "";
  const page = Number(searchParams.get("page") ?? "1");

  return null;
}
```

---

### [실무]

읽기 예:

```jsx
const [searchParams] = useSearchParams();

const keyword = searchParams.get("keyword") ?? "";
const region = searchParams.get("region") ?? "";
const page = Number(searchParams.get("page") ?? "1");
const sort = searchParams.get("sort") ?? "latest";
```

수정 예:

```jsx
setSearchParams({
  keyword: "꽃",
  region: "seoul",
  page: "1",
  sort: "popular",
});
```

기존 param 유지 예:

```jsx
const nextParams = new URLSearchParams(searchParams);

nextParams.set("keyword", keyword);
nextParams.set("page", "1");

setSearchParams(nextParams);
```

삭제 예:

```jsx
const nextParams = new URLSearchParams(searchParams);

if (keyword) {
  nextParams.set("keyword", keyword);
} else {
  nextParams.delete("keyword");
}

nextParams.set("page", "1");

setSearchParams(nextParams);
```

실무 기준:

- searchParams 값은 문자열
- Number / boolean 변환 필요
- setSearchParams 호출 시 navigation 발생
- 기존 params 보존 여부 확인
- 빈 값은 delete 기준 정의
- 검색 조건 변경 시 page reset
- URL을 source of truth로 둘지 Component State와 동기화할지 결정

---

### [FAQ]

Q. useSearchParams는 뭐야?
A. 현재 URL의 Query String을 읽고 수정하는 React Router Hook이다.

Q. useSearchParams는 어떻게 써?
A. searchParams.get으로 값을 읽고 setSearchParams로 query string을 수정한다.

Q. useSearchParams 값은 number로 바로 받아?
A. 아니다. 문자열로 읽히므로 Number 변환이 필요하다.

Q. setSearchParams를 호출하면 페이지 이동이야?
A. URL search params가 바뀌므로 navigation이 발생한다.

---

## 5.2 Search Params State Sync

### [개념]

Search Params State Sync는 URL Query String과 Component State를 일관되게 유지하는 구조다.

검색 input, filter select, pagination UI가 URL 상태와 불일치하지 않도록 설계해야 한다.

---

### [핵심]

- URL State
- Component State
- Source of Truth
- Search Form
- Filter UI
- Pagination
- Back Button
- Refresh Persistence
- Initial Value
- Sync Problem

상태 기준 선택:

```text
URL 공유 / 새로고침 유지 / 뒤로가기 복원 필요
→ URL Search Params를 source of truth로 사용

입력 중 임시 값
→ Component State 사용 가능

검색 submit 후 조건 확정
→ setSearchParams로 URL 반영
```

---

### [실무]

검색 form 예:

```jsx
function FestivalSearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();

  const initialKeyword = searchParams.get("keyword") ?? "";
  const [keywordInput, setKeywordInput] = useState(initialKeyword);

  function handleSearchSubmit(event) {
    event.preventDefault();

    const nextParams = new URLSearchParams(searchParams);

    if (keywordInput.trim()) {
      nextParams.set("keyword", keywordInput.trim());
    } else {
      nextParams.delete("keyword");
    }

    nextParams.set("page", "1");

    setSearchParams(nextParams);
  }

  return null;
}
```

목록 데이터 요청 기준:

```jsx
const keyword = searchParams.get("keyword") ?? "";
const page = Number(searchParams.get("page") ?? "1");

useEffect(() => {
  fetchFestivals({ keyword, page });
}, [keyword, page]);
```

실무 주의:

- URL과 input state가 달라질 수 있음
- 뒤로가기 시 input state도 갱신 필요 가능
- 검색 조건 변경 시 page reset
- setSearchParams에서 기존 params를 덮어쓸 수 있음
- 빈 값 제거 기준 필요
- URL을 source of truth로 두면 동기화 문제가 줄어듦

---

### [FAQ]

Q. 검색 조건은 State로 둬야 해 Query String으로 둬야 해?
A. URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하면 Query String으로 관리하는 것이 좋다.

Q. URL query와 input 값이 달라?
A. URL search params와 input state를 중복 관리하면서 동기화가 누락되었을 수 있다.

Q. 입력 중인 검색어도 바로 Query String에 반영해야 해?
A. 프로젝트 UX에 따라 다르다. 일반적으로 submit 시 URL에 반영하는 방식이 단순하다.

Q. URL을 source of truth로 둔다는 뜻은 뭐야?
A. 화면의 검색 조건 기준을 Component State가 아니라 현재 Query String 값으로 삼는다는 뜻이다.

---

## 5.3 Search Params Update Rules

### [개념]

Search Params Update Rules는 Query String 수정 시 기존 조건 유지, 빈 값 제거, page reset, 타입 문자열 변환을 일관되게 처리하는 기준이다.

---

### [핵심]

업데이트 기준:

- 기존 params 보존 여부 확인
- 빈 값은 delete
- 검색 조건 변경 시 page reset
- 숫자는 문자열로 저장
- boolean은 문자열 기준 정의
- 배열 필터 표현 방식 통일
- 불필요한 query key 제거
- API parameter와 매핑 확인

---

### [실무]

단일 조건 업데이트:

```jsx
function updateKeyword(keyword) {
  const nextParams = new URLSearchParams(searchParams);

  if (keyword.trim()) {
    nextParams.set("keyword", keyword.trim());
  } else {
    nextParams.delete("keyword");
  }

  nextParams.set("page", "1");

  setSearchParams(nextParams);
}
```

필터 업데이트:

```jsx
function updateRegion(region) {
  const nextParams = new URLSearchParams(searchParams);

  if (region) {
    nextParams.set("region", region);
  } else {
    nextParams.delete("region");
  }

  nextParams.set("page", "1");

  setSearchParams(nextParams);
}
```

페이지 이동:

```jsx
function updatePage(page) {
  const nextParams = new URLSearchParams(searchParams);

  nextParams.set("page", String(page));

  setSearchParams(nextParams);
}
```

정렬 변경:

```jsx
function updateSort(sort) {
  const nextParams = new URLSearchParams(searchParams);

  nextParams.set("sort", sort);
  nextParams.set("page", "1");

  setSearchParams(nextParams);
}
```

주의:

- `setSearchParams({ keyword })`는 기존 params를 지울 수 있음
- 기존 필터 유지가 필요하면 URLSearchParams 복사 후 수정
- page 값을 숫자로 넣지 말고 문자열로 변환
- 잘못된 page 값은 기본값으로 보정
- query key naming 통일

---

### [FAQ]

Q. setSearchParams를 쓰면 기존 query가 사라져?
A. 새 객체로 교체하면 기존 params가 사라질 수 있다. 유지하려면 URLSearchParams를 복사해 수정한다.

Q. 검색 조건이 바뀌면 page를 왜 1로 바꿔?
A. 기존 page가 새 검색 결과 범위를 벗어날 수 있으므로 첫 페이지로 reset하는 것이 일반적이다.

Q. 빈 값은 query string에 남겨?
A. 보통 delete로 제거하는 것이 URL을 깔끔하게 유지하는 데 좋다.

Q. page 값을 setSearchParams에 number로 넣어도 돼?
A. Query String은 문자열이므로 String(page)처럼 명시적으로 변환하는 것이 안전하다.

---

# 6. Path Parameter vs Query String

## 6.1 Comparison

### [개념]

Path Parameter는 특정 리소스를 식별하는 URL 일부다.

Query String은 검색, 필터, 정렬, 페이지 같은 선택 조건을 표현하는 URL 일부다.

---

### [핵심]

| 비교     | Path Parameter             | Query String                |
| -------- | -------------------------- | --------------------------- |
| 형태     | `/festivals/1`             | `/festivals?keyword=꽃`     |
| 목적     | 리소스 식별                | 조건 / 옵션                 |
| 예       | festivalId, userId, postId | keyword, region, page, sort |
| 필수성   | 대체로 필수                | 선택적                      |
| Hook     | useParams                  | useSearchParams             |
| 화면     | 상세 페이지                | 목록 / 검색 페이지          |
| API 매핑 | path variable              | query parameter             |

선택 기준:

```text
Resource Identity
→ Path Parameter

Filter / Search / Sort / Page
→ Query String
```

---

### [실무]

권장 예:

```text
축제 목록
→ /festivals

축제 상세
→ /festivals/123

축제 검색
→ /festivals?keyword=꽃&region=seoul

축제 리뷰 목록
→ /festivals/123/reviews?page=2

마이페이지 탭
→ /mypage?tab=favorites
```

나쁜 설계 예:

```text
/festivals/search/flower/seoul/page/2
```

문제:

- 검색 조건 확장 어려움
- optional filter 처리 복잡
- URL 의미가 불명확해질 수 있음

권장 설계:

```text
/festivals?keyword=flower&region=seoul&page=2
```

---

### [FAQ]

Q. Path Parameter와 Query String 차이는?
A. Path Parameter는 리소스 식별에 사용하고 Query String은 검색, 필터, 정렬, 페이지 같은 옵션에 사용한다.

Q. ID는 path param이 좋아 query string이 좋아?
A. 특정 리소스 식별 ID는 path parameter가 일반적으로 적합하다.

Q. 검색어는 path param으로 넣어도 돼?
A. 가능은 하지만 필터와 검색 조건은 Query String이 더 적합한 경우가 많다.

Q. 페이지 번호는 Path Parameter로 둬?
A. 보통 Query String으로 둔다. 예: `/festivals?page=2`.

---

## 6.2 REST API Mapping Awareness

### [개념]

Frontend Route의 Path Parameter와 Query String은 Backend API의 Path Variable, Request Parameter와 비슷한 구조로 매핑될 수 있다.

하지만 Frontend Route와 Backend API Endpoint는 같은 것이 아니다.

---

### [핵심]

Frontend Route:

```text
/festivals/:festivalId
/festivals?keyword=꽃&page=1
```

Backend API:

```text
GET /api/festivals/{festivalId}
GET /api/festivals?keyword=꽃&page=1
```

구분:

- Frontend Route는 화면 URL
- Backend API는 데이터 요청 URL
- Path Parameter는 API Path Variable과 매핑 가능
- Query String은 API Request Param과 매핑 가능
- `/api` prefix로 충돌 방지 권장

---

### [실무]

상세 페이지 Flow:

```text
User visits /festivals/123
→ React Router matches /festivals/:festivalId
→ useParams reads festivalId = "123"
→ Convert Number
→ Request GET /api/festivals/123
→ Render FestivalDetailPage
```

검색 페이지 Flow:

```text
User visits /festivals?keyword=꽃&page=1
→ useSearchParams reads keyword, page
→ Request GET /api/festivals?keyword=꽃&page=1
→ Render FestivalListPage
```

실무 주의:

- Frontend Route와 API endpoint를 혼동하지 않음
- Axios baseURL과 React Router path를 분리
- API 요청에 index.html이 응답되면 fallback / path collision 확인
- Backend API는 `/api` prefix 권장
- URL query key와 API parameter naming 통일 권장

---

### [FAQ]

Q. Frontend Route와 Backend API URL은 같은 거야?
A. 아니다. Frontend Route는 화면 URL이고 Backend API URL은 서버 데이터 요청 URL이다.

Q. `/festivals/123`에서 바로 API가 호출돼?
A. 아니다. React Router가 화면을 렌더링하고 Page Component나 Hook에서 별도로 API를 호출한다.

Q. useParams 값은 API Path Variable로 넘겨도 돼?
A. 가능하다. 다만 숫자 변환과 검증 후 API 요청에 사용하는 것이 안전하다.

Q. useSearchParams 값은 API query parameter로 넘겨도 돼?
A. 가능하다. 빈 값 제거와 타입 변환 기준을 적용한 뒤 요청하는 것이 좋다.

---

# 7. Params and Search Params Error Handling

## 7.1 Invalid Path Parameter Handling

### [개념]

Invalid Path Parameter Handling은 URL Path Parameter가 없거나 잘못된 형식일 때 NotFoundPage 또는 Error UI로 처리하는 기준이다.

상세 페이지에서는 잘못된 ID로 API를 호출하지 않도록 사전에 검증해야 한다.

---

### [핵심]

처리 대상:

- missing param
- undefined param
- invalid number
- NaN
- negative id
- unsupported id format
- resource not found
- API 404
- NotFoundPage
- Error UI

---

### [실무]

숫자 ID 검증 예:

```jsx
function FestivalDetailPage() {
  const { festivalId } = useParams();
  const parsedFestivalId = Number(festivalId);

  if (!festivalId || Number.isNaN(parsedFestivalId) || parsedFestivalId <= 0) {
    return <NotFoundPage />;
  }

  return <FestivalDetail festivalId={parsedFestivalId} />;
}
```

API 404 처리 기준:

```text
Invalid URL Parameter
→ Frontend NotFoundPage

Valid Parameter but Resource Missing
→ API 404
→ Resource Not Found UI

Server Error
→ Error UI
```

실무 기준:

- param 누락은 NotFoundPage
- 숫자 변환 실패는 NotFoundPage
- API 404는 리소스 없음 UI
- API 401은 login redirect
- API 403은 forbidden UI
- API 500은 error message
- 사용자 메시지와 개발자 로그 구분

---

### [FAQ]

Q. 잘못된 URL parameter는 어떻게 처리해?
A. Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. festivalId가 음수면 어떻게 해?
A. ID 정책에 따라 invalid param으로 보고 NotFoundPage 또는 Error UI를 보여주는 것이 좋다.

Q. API 404와 Route 404는 어떻게 달라?
A. Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

Q. 잘못된 param으로 API 호출해도 돼?
A. 권장하지 않는다. 프론트에서 기본 검증 후 잘못된 값은 요청하지 않는 것이 좋다.

---

## 7.2 Invalid Search Params Handling

### [개념]

Invalid Search Params Handling은 Query String 값이 없거나 잘못된 형식일 때 기본값으로 보정하거나 URL에서 제거하는 기준이다.

검색 / 필터 페이지는 잘못된 query 값에도 안정적으로 동작해야 한다.

---

### [핵심]

처리 대상:

- page가 숫자가 아님
- page가 0 이하
- sort 값이 허용 범위 밖
- unknown filter
- empty keyword
- invalid date
- unsupported boolean value
- duplicated param
- stale query key

---

### [실무]

page 보정 예:

```jsx
const rawPage = searchParams.get("page") ?? "1";
const parsedPage = Number(rawPage);

const page = Number.isNaN(parsedPage) || parsedPage < 1 ? 1 : parsedPage;
```

sort 보정 예:

```jsx
const allowedSorts = ["latest", "popular", "rating"];
const rawSort = searchParams.get("sort") ?? "latest";

const sort = allowedSorts.includes(rawSort) ? rawSort : "latest";
```

keyword 처리 예:

```jsx
const keyword = searchParams.get("keyword")?.trim() ?? "";
```

실무 기준:

- page 기본값은 1
- sort 기본값 정의
- 허용되지 않은 sort는 기본값으로 보정
- 빈 keyword는 검색 조건 없음으로 처리
- 잘못된 날짜는 제거 또는 error UI
- API 요청 전 query 값 정리
- URL 정규화가 필요하면 setSearchParams로 보정 가능

---

### [FAQ]

Q. page query가 abc면 어떻게 해?
A. Number 변환 실패로 보고 기본 page 1로 보정하는 것이 일반적이다.

Q. sort query가 허용되지 않은 값이면?
A. allowedSorts 기준으로 확인하고 기본 sort로 보정한다.

Q. 빈 keyword는 어떻게 처리해?
A. 검색 조건 없음으로 처리하거나 query string에서 제거한다.

Q. 잘못된 query string 때문에 화면이 깨져도 돼?
A. 안 된다. 기본값 보정이나 Error UI로 안정적으로 처리해야 한다.

---

# 8. Search Params Sync Problem

## 8.1 Common Sync Problems

### [개념]

Search Params Sync Problem은 URL Query String과 Component State가 서로 불일치하는 문제다.

검색 input, filter select, pagination UI, API 요청 parameter가 서로 다른 값을 바라볼 때 발생한다.

---

### [핵심]

문제:

- URL에는 keyword가 있는데 input은 비어 있음
- input에는 값이 있는데 API 요청은 이전 keyword로 수행
- 뒤로가기 시 화면 상태가 맞지 않음
- 새로고침하면 검색 조건이 사라짐
- page 값이 문자열이라 계산 오류 발생
- setSearchParams 후 기존 filter가 사라짐
- 검색 조건 변경 후 page가 이전 값 유지

원인:

- URL과 State를 중복 관리
- 초기값 동기화 누락
- searchParams 변경 감지 누락
- setSearchParams에서 기존 param 미보존
- 타입 변환 누락
- 빈 값 처리 기준 없음

---

### [실무]

Debug Flow:

```text
Search Params Sync Problem
→ Current URL 확인
→ searchParams.get 값 확인
→ input state 확인
→ setSearchParams 로직 확인
→ 기존 params 보존 여부 확인
→ Type Conversion 확인
→ Back Button 동작 확인
→ API Request Params 확인
```

권장 기준:

```text
검색 결과 기준
→ URL searchParams

입력 중 임시 값
→ Component State

검색 submit
→ setSearchParams

API 요청
→ searchParams 기반
```

주의:

- searchParams 값 변경 시 API 요청 dependency 확인
- searchParams 값 변경 시 input state 동기화 필요 여부 검토
- page reset 누락 주의
- query key 오타 주의
- URL과 API 요청 parameter 차이 확인

---

### [FAQ]

Q. URL query와 input 값이 달라?
A. URL search params와 input state를 중복 관리하면서 동기화가 누락되었을 수 있다.

Q. 뒤로가기 했는데 검색 결과가 안 바뀌어?
A. API 요청이 searchParams 변경을 dependency로 감지하는지 확인해야 한다.

Q. setSearchParams 후 기존 필터가 사라졌어?
A. 기존 params를 복사하지 않고 새 객체로 교체했을 가능성이 있다.

Q. 검색 후 page가 이상해?
A. 검색 조건 변경 시 page reset이 누락되었는지 확인한다.

---

# 9. Params SearchParams Checklist

## 9.1 Part03 Checklist

### [개념]

Params SearchParams 문서는 URL 값 읽기, 검증, 변환, API 연결 기준을 검수하기 위한 체크리스트를 포함한다.

---

### [핵심]

Checklist:

```md
- [ ] Dynamic Route 개념이 설명되었는가?
- [ ] Path Parameter와 Route Parameter 용어가 통일되었는가?
- [ ] useParams 사용법이 포함되었는가?
- [ ] useParams 값이 문자열이라는 설명이 포함되었는가?
- [ ] undefined guard가 포함되었는가?
- [ ] Number 변환과 NaN 검증이 포함되었는가?
- [ ] param name consistency가 포함되었는가?
- [ ] Dynamic Route pattern과 actual URL 차이가 포함되었는가?
- [ ] Query String 개념이 설명되었는가?
- [ ] useSearchParams 사용법이 포함되었는가?
- [ ] searchParams 값이 문자열이라는 설명이 포함되었는가?
- [ ] setSearchParams 시 기존 params 보존 주의가 포함되었는가?
- [ ] 검색 조건 변경 시 page reset 기준이 포함되었는가?
- [ ] 빈 값 delete 기준이 포함되었는가?
- [ ] Path Parameter vs Query String 비교가 포함되었는가?
- [ ] Frontend Route와 Backend API 구분이 포함되었는가?
- [ ] Invalid Params Error Handling이 포함되었는가?
- [ ] Search Params Sync Problem이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Dynamic Route Check
→ useParams Check
→ Param Naming Check
→ Type Conversion Check
→ Query String Check
→ useSearchParams Check
→ Update Rule Check
→ Path vs Query Comparison Check
→ API Mapping Check
→ Error Handling Check
→ Sync Problem Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. Part03 검수에서 가장 중요한 것은?
A. useParams와 useSearchParams 값 검증, 타입 변환, Path Parameter와 Query String 선택 기준이다.

Q. Part03에서 Navigation State도 다뤄?
A. 아니다. Navigation State는 Navigation Part에서 다루고 Part03은 URL에 보이는 params와 query string을 다룬다.

Q. Part03에서 Data Fetching을 깊게 다뤄?
A. 아니다. API 요청 parameter 연결 기준만 언급하고 Data Fetching 심화는 별도 문서에서 다룬다.

---

# 10. Params SearchParams Common Mistakes

## 10.1 Common Mistakes

### [개념]

Params SearchParams에서 자주 발생하는 실수는 param 이름 불일치, 문자열 타입 오해, query 상태 동기화 실패, Path Parameter와 Query String 선택 오류다.

---

### [핵심]

자주 발생:

- Route path param 이름과 useParams key 불일치
- useParams 값이 number라고 착각
- Number 변환 없이 숫자 비교 수행
- Number(undefined)로 NaN 발생
- Dynamic Route pattern을 Link to에 그대로 사용
- id undefined 상태로 URL 생성
- Path Parameter와 Query String 역할 혼동
- 검색 조건을 Path Parameter로 과도하게 설계
- 리소스 ID를 Query String으로 숨김
- useSearchParams 값이 number라고 착각
- setSearchParams에서 기존 params 삭제
- 검색 조건 변경 시 page reset 누락
- 빈 query value를 URL에 계속 유지
- URL과 input state 불일치
- 뒤로가기 시 API 요청 갱신 누락
- Query String에 민감정보 저장
- Frontend Route와 Backend API URL 혼동

---

### [실무]

대표 문제 1:

```text
문제: festivalId가 undefined
원인: Route path는 :id인데 useParams는 festivalId를 읽음
해결: param 이름 통일
```

대표 문제 2:

```text
문제: API 요청이 /api/festivals/undefined로 나감
원인: Link URL 생성 시 festivalId 값이 undefined
해결: ID 필드명 확인 후 path builder 사용
```

대표 문제 3:

```text
문제: 검색 후 region 필터가 사라짐
원인: setSearchParams가 기존 params를 보존하지 않음
해결: URLSearchParams(searchParams)로 복사 후 수정
```

대표 문제 4:

```text
문제: page 계산 오류
원인: searchParams.get("page") 값은 문자열
해결: Number 변환과 기본값 보정
```

Debug Flow:

```text
URL Value Problem
→ Current URL 확인
→ Route pattern 확인
→ useParams / useSearchParams 값 확인
→ Type Conversion 확인
→ State Sync 확인
→ API Request URL 확인
→ Error UI 확인
```

---

### [FAQ]

Q. React Router params 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, Route pattern, Link URL, useParams key, 타입 변환, API 요청 URL을 순서대로 확인한다.

Q. searchParams 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, searchParams.get 값, input state, setSearchParams 로직, API 요청 parameter를 확인한다.

Q. URL 값은 왜 항상 검증해야 해?
A. 사용자가 직접 URL을 수정하거나 잘못된 링크로 접근할 수 있기 때문이다.

Q. URL 상태 설계에서 가장 중요한 기준은?
A. 리소스 식별은 Path Parameter, 검색과 필터 조건은 Query String으로 분리하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part03은 뭘 다뤄?
A. Dynamic Route, useParams, Path Parameter, Query String, useSearchParams, Path Parameter vs Query String 기준을 다룬다.

Q. Dynamic Route는 뭐야?
A. URL 일부를 변수처럼 받는 Route다. 예: `/festivals/:festivalId`.

Q. Path Parameter는 뭐야?
A. URL path 안에서 특정 리소스를 식별하기 위해 사용하는 값이다. 예: `/festivals/123`의 `123`.

Q. Route Parameter는 뭐야?
A. Dynamic Route에서 `:festivalId`처럼 URL 일부를 변수로 받는 parameter다.

Q. `:festivalId`는 무슨 뜻이야?
A. URL의 해당 위치 값을 festivalId라는 이름의 Path Parameter로 받겠다는 뜻이다.

Q. 상세 페이지 path는 어떻게 잡아?
A. 일반적으로 `/resources/:resourceId` 형태를 사용한다. 예: `/festivals/:festivalId`.

Q. `/festivals/:festivalId`를 Link to에 그대로 넣어도 돼?
A. 안 된다. Link에는 `/festivals/123`처럼 실제 값이 들어간 URL을 넣어야 한다.

Q. Dynamic Route pattern과 실제 URL 차이는?
A. `/festivals/:festivalId`는 Route 정의용 pattern이고 `/festivals/123`은 실제 이동 URL이다.

Q. Dynamic Route URL은 어떻게 만들어?
A. template string이나 path builder 함수를 사용해 실제 ID 값을 넣어 만든다.

Q. path builder 함수는 왜 필요해?
A. URL 생성 기준을 통일하고 오타와 undefined URL 생성을 줄이기 위해 필요하다.

Q. useParams는 뭐야?
A. 현재 Dynamic Route에서 Path Parameter 값을 읽는 React Router Hook이다.

Q. useParams는 어떻게 써?
A. `const { festivalId } = useParams();`처럼 Route path에 정의한 param 이름으로 값을 꺼낸다.

Q. useParams 값은 number야 string이야?
A. 문자열이다. 숫자 ID로 쓰려면 Number로 변환해야 한다.

Q. useParams가 undefined일 수 있어?
A. 가능하다. Route path에 param이 없거나 param 이름이 맞지 않으면 undefined가 될 수 있다.

Q. useParams가 undefined인 이유는?
A. Route path에 해당 param이 없거나 param 이름이 맞지 않거나 Link URL이 잘못되었을 수 있다.

Q. Route는 `:id`인데 useParams에서 festivalId로 꺼낼 수 있어?
A. 안 된다. Route가 `:id`면 useParams에서도 `id`로 꺼내야 한다.

Q. param 이름은 어떻게 정하는 게 좋아?
A. `festivalId`, `userId`, `postId`처럼 도메인 의미가 드러나는 이름이 좋다.

Q. useParams 값으로 바로 API 호출해도 돼?
A. 숫자 ID가 필요하면 변환과 검증 후 API 호출하는 것이 안전하다.

Q. Number(undefined)는 어떻게 돼?
A. NaN이 된다. Number 변환 후 Number.isNaN으로 검증해야 한다.

Q. 잘못된 URL parameter는 어떻게 처리해?
A. Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. festivalId가 음수면 어떻게 해?
A. ID 정책에 따라 invalid param으로 보고 NotFoundPage 또는 Error UI를 보여주는 것이 좋다.

Q. API 404와 Route 404는 어떻게 달라?
A. Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

Q. Query String은 뭐야?
A. URL에서 `?keyword=spring&page=1`처럼 검색 조건이나 옵션을 표현하는 부분이다.

Q. Search Params는 뭐야?
A. Query String에 들어 있는 key-value 형식의 검색 조건과 옵션 값이다.

Q. 검색 조건은 왜 Query String으로 둬?
A. URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하기 때문이다.

Q. Query String 값은 문자열이야?
A. 그렇다. 숫자와 boolean 값은 직접 변환해야 한다.

Q. Query String에 민감정보를 넣어도 돼?
A. 안 된다. URL에 노출되고 공유될 수 있으므로 민감정보를 넣지 않는다.

Q. Query key 이름은 어떻게 정해?
A. keyword, region, category, page, sort처럼 의미가 명확하고 API parameter와 맞추기 쉬운 이름을 사용한다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 일반적으로 page를 1로 reset한다.

Q. 빈 검색어도 Query String에 남겨?
A. 보통 빈 값은 제거해 URL을 깔끔하게 유지한다.

Q. useSearchParams는 뭐야?
A. 현재 URL의 Query String을 읽고 수정하는 React Router Hook이다.

Q. useSearchParams는 어떻게 써?
A. searchParams.get으로 값을 읽고 setSearchParams로 query string을 수정한다.

Q. useSearchParams 값은 number로 바로 받아?
A. 아니다. 문자열로 읽히므로 Number 변환이 필요하다.

Q. setSearchParams를 호출하면 페이지 이동이야?
A. URL search params가 바뀌므로 navigation이 발생한다.

Q. setSearchParams를 쓰면 기존 query가 사라져?
A. 새 객체로 교체하면 기존 params가 사라질 수 있다. 유지하려면 URLSearchParams를 복사해 수정한다.

Q. 검색 조건은 State로 둬야 해 Query String으로 둬야 해?
A. URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하면 Query String으로 관리하는 것이 좋다.

Q. URL query와 input 값이 달라?
A. URL search params와 input state를 중복 관리하면서 동기화가 누락되었을 수 있다.

Q. 입력 중인 검색어도 바로 Query String에 반영해야 해?
A. 프로젝트 UX에 따라 다르다. 일반적으로 submit 시 URL에 반영하는 방식이 단순하다.

Q. URL을 source of truth로 둔다는 뜻은 뭐야?
A. 화면의 검색 조건 기준을 Component State가 아니라 현재 Query String 값으로 삼는다는 뜻이다.

Q. 검색 조건이 바뀌면 page를 왜 1로 바꿔?
A. 기존 page가 새 검색 결과 범위를 벗어날 수 있으므로 첫 페이지로 reset하는 것이 일반적이다.

Q. 빈 값은 query string에 남겨?
A. 보통 delete로 제거하는 것이 URL을 깔끔하게 유지하는 데 좋다.

Q. page 값을 setSearchParams에 number로 넣어도 돼?
A. Query String은 문자열이므로 String(page)처럼 명시적으로 변환하는 것이 안전하다.

Q. Path Parameter와 Query String 차이는?
A. Path Parameter는 리소스 식별에 사용하고 Query String은 검색, 필터, 정렬, 페이지 같은 옵션에 사용한다.

Q. ID는 path param이 좋아 query string이 좋아?
A. 특정 리소스 식별 ID는 path parameter가 일반적으로 적합하다.

Q. 검색어는 path param으로 넣어도 돼?
A. 가능은 하지만 필터와 검색 조건은 Query String이 더 적합한 경우가 많다.

Q. 페이지 번호는 Path Parameter로 둬?
A. 보통 Query String으로 둔다. 예: `/festivals?page=2`.

Q. Frontend Route와 Backend API URL은 같은 거야?
A. 아니다. Frontend Route는 화면 URL이고 Backend API URL은 서버 데이터 요청 URL이다.

Q. `/festivals/123`에서 바로 API가 호출돼?
A. 아니다. React Router가 화면을 렌더링하고 Page Component나 Hook에서 별도로 API를 호출한다.

Q. useParams 값은 API Path Variable로 넘겨도 돼?
A. 가능하다. 다만 숫자 변환과 검증 후 API 요청에 사용하는 것이 안전하다.

Q. useSearchParams 값은 API query parameter로 넘겨도 돼?
A. 가능하다. 빈 값 제거와 타입 변환 기준을 적용한 뒤 요청하는 것이 좋다.

Q. page query가 abc면 어떻게 해?
A. Number 변환 실패로 보고 기본 page 1로 보정하는 것이 일반적이다.

Q. sort query가 허용되지 않은 값이면?
A. allowedSorts 기준으로 확인하고 기본 sort로 보정한다.

Q. 뒤로가기 했는데 검색 결과가 안 바뀌어?
A. API 요청이 searchParams 변경을 dependency로 감지하는지 확인해야 한다.

Q. setSearchParams 후 기존 필터가 사라졌어?
A. 기존 params를 복사하지 않고 새 객체로 교체했을 가능성이 있다.

Q. React Router params 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, Route pattern, Link URL, useParams key, 타입 변환, API 요청 URL을 순서대로 확인한다.

Q. searchParams 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, searchParams.get 값, input state, setSearchParams 로직, API 요청 parameter를 확인한다.

Q. URL 값은 왜 항상 검증해야 해?
A. 사용자가 직접 URL을 수정하거나 잘못된 링크로 접근할 수 있기 때문이다.

Q. URL 상태 설계에서 가장 중요한 기준은?
A. 리소스 식별은 Path Parameter, 검색과 필터 조건은 Query String으로 분리하는 것이다.

Q. Part03 다음에는 뭘 다뤄?
A. Part04 Nested Layout Route에서 Nested Route, Outlet, Layout Route, Page Route Structure를 다룬다.

# React Component Design Part05 - Container, Presentational, Custom Hook

---

# 1. Container and Presentational Pattern

## 1.1 Container and Presentational Definition

### [개념]

Container and Presentational Pattern은 React Component에서 데이터 흐름과 UI 표시 책임을 분리하는 설계 방식이다.

Container Component는 데이터 로딩, State 관리, Event Handler, API 흐름을 담당한다.

Presentational Component는 전달받은 Props를 기반으로 UI를 표시한다.

이 패턴은 모든 Component에 강제하는 규칙이 아니라, Component가 복잡해질 때 책임을 분리하기 위한 선택적 설계 기준이다.

---

### [핵심]

- Container Component는 데이터와 흐름을 담당한다.
- Presentational Component는 UI 표시를 담당한다.
- Container는 API 요청, State, Event Handler를 가질 수 있다.
- Presentational은 Props 기반 렌더링을 우선한다.
- Presentational은 API 호출을 지양한다.
- Page Component가 Container 역할을 겸할 수 있다.
- 단순 화면에서는 분리하지 않아도 된다.
- 복잡한 화면에서는 책임 분리를 위해 유용하다.
- Container / Presentational 분리는 Component Responsibility를 명확히 한다.
- 과도한 분리는 Over-Engineering이 될 수 있다.

---

### [실무]

2026 실무 기준에서는 Container / Presentational Pattern을 무조건 적용하지 않는다.

적용 기준:

```text
Component가 단순하다
→ 분리하지 않아도 됨

API Logic과 UI Markup이 섞여 복잡하다
→ Container / Presentational 분리 검토

Page가 데이터 흐름을 담당한다
→ Page가 Container 역할 가능

동일 UI를 여러 데이터 흐름에서 재사용한다
→ Presentational Component 분리 유리
```

기본 구조:

```text
FestivalListContainer
- API 요청
- loading / error / data 관리
- 이벤트 처리
- FestivalList에 Props 전달

FestivalList
- festivals 표시
- loading / error / empty UI 표시
- onSelect callback 호출
```

예:

```tsx
function FestivalListContainer() {
  const { festivals, loading, error } = useFestivals();

  function handleSelectFestival(festivalId: number) {
    // 상세 이동 또는 선택 상태 변경
  }

  return (
    <FestivalList
      festivals={festivals}
      loading={loading}
      error={error}
      onSelectFestival={handleSelectFestival}
    />
  );
}
```

Presentational Component:

```tsx
function FestivalList({
  festivals,
  loading,
  error,
  onSelectFestival,
}: FestivalListProps) {
  if (loading) {
    return <LoadingView />;
  }

  if (error) {
    return <ErrorMessage message="축제 목록을 불러오지 못했습니다." />;
  }

  if (festivals.length === 0) {
    return <EmptyState title="검색 결과가 없습니다." />;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          festival={festival}
          onSelect={onSelectFestival}
        />
      ))}
    </section>
  );
}
```

---

### [FAQ]

Q. Container and Presentational Pattern이 뭐야?
A. 데이터 흐름과 UI 표시 책임을 분리하는 React Component 설계 방식이다.

Q. Container Component는 뭐야?
A. API 요청, State 관리, Event Handler, 데이터 변환 같은 흐름을 담당하는 Component다.

Q. Presentational Component는 뭐야?
A. 전달받은 Props를 기반으로 UI를 표시하는 Component다.

Q. Container와 Presentational은 항상 분리해야 해?
A. 아니다. 복잡도를 줄일 때만 사용한다. 단순 Component에는 과한 설계가 될 수 있다.

---

## 1.2 Container Component Rules

### [개념]

Container Component는 데이터 로딩, State Ownership, Event Flow, API 요청, 데이터 변환을 담당하는 Component다.

Container Component는 화면에 필요한 데이터를 준비하고 Presentational Component에 Props로 전달한다.

---

### [핵심]

Container Component 역할:

- API 요청 시작
- Server State 관리
- Page State 관리 가능
- loading / error / data 관리
- Event Handler 정의
- Callback Props 연결
- 데이터 변환
- Response Mapping
- Presentational Component에 Props 전달
- Custom Hook 사용

Container Component 주의:

- UI Markup을 과도하게 작성하지 않는다.
- 너무 많은 Container를 만들지 않는다.
- 단순 Page에서는 Page가 Container 역할을 겸할 수 있다.
- Container가 여러 Feature 책임을 모두 가지면 다시 분리한다.

---

### [실무]

Container 예:

```tsx
function FestivalSearchContainer() {
  const [keyword, setKeyword] = useState("");
  const [page, setPage] = useState(1);

  const { festivals, loading, error, refetch } = useFestivalSearch({
    keyword,
    page,
  });

  function handleSearch(nextKeyword: string) {
    setKeyword(nextKeyword);
    setPage(1);
  }

  return (
    <FestivalSearchView
      keyword={keyword}
      festivals={festivals}
      loading={loading}
      error={error}
      page={page}
      onSearch={handleSearch}
      onChangePage={setPage}
      onRefresh={refetch}
    />
  );
}
```

Container 책임:

```text
FestivalSearchContainer
- keyword State 소유
- page State 소유
- useFestivalSearch 호출
- 검색 이벤트 처리
- pagination 이벤트 처리
- View Component에 Props 전달
```

주의:

```text
Container 내부 JSX가 너무 많다
→ Presentational Component로 분리

Container가 여러 API를 모두 관리한다
→ Feature별 Container 또는 Custom Hook 분리

Container가 단순히 Props만 전달한다
→ 불필요한 Container인지 검토
```

---

### [FAQ]

Q. Container Component는 어떤 책임을 가져?
A. 데이터 로딩, State 관리, Event Handler, API 흐름, 데이터 변환을 담당한다.

Q. Container Component가 JSX를 렌더링하면 안 돼?
A. 일부 렌더링은 가능하다. 다만 핵심 책임은 데이터와 흐름 관리이며 UI Markup이 과도하면 분리한다.

Q. Page Component가 Container 역할을 해도 돼?
A. 가능하다. 많은 경우 Page Component가 화면 단위 Container 역할을 한다.

Q. Container Component를 많이 만들면 좋아?
A. 아니다. 흐름 분리에 도움이 될 때만 만들고 단순 Props 전달용 Container는 피한다.

---

## 1.3 Presentational Component Rules

### [개념]

Presentational Component는 외부에서 전달받은 Props를 기반으로 UI를 표시하는 Component다.

Presentational Component는 API 요청이나 서버 구조를 직접 알지 않고, 표시와 사용자 이벤트 알림에 집중한다.

---

### [핵심]

Presentational Component 역할:

- Props 기반 UI 렌더링
- loading / error / empty 표시 가능
- Callback Props 호출
- 도메인 로직 최소화
- API 호출 없음
- 서버 응답 구조 직접 의존 지양
- 재사용성 높음
- 테스트 가능성 높음
- Local UI State는 가질 수 있음

---

### [실무]

Presentational Component 예:

```tsx
type FestivalListProps = {
  festivals: FestivalSummary[];
  loading: boolean;
  error: Error | null;
  onSelectFestival: (festivalId: number) => void;
};

function FestivalList({
  festivals,
  loading,
  error,
  onSelectFestival,
}: FestivalListProps) {
  if (loading) {
    return <LoadingView />;
  }

  if (error) {
    return <ErrorMessage message="축제 목록을 불러오지 못했습니다." />;
  }

  if (festivals.length === 0) {
    return <EmptyState title="표시할 축제가 없습니다." />;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          festival={festival}
          onSelect={onSelectFestival}
        />
      ))}
    </section>
  );
}
```

좋은 점:

```text
- API 호출 없음
- Props Contract 명확
- loading / error / empty 상태 표시
- onSelectFestival callback으로 이벤트 전달
- 테스트하기 쉬움
```

주의:

```text
Presentational Component가 API URL을 안다
→ 책임 위반

Presentational Component가 직접 fetch 호출
→ Container 또는 Hook으로 이동

Presentational Component가 전역 상태에 강하게 의존
→ Props 기반 구조 검토
```

---

### [FAQ]

Q. Presentational Component는 State를 가지면 안 돼?
A. 항상 금지는 아니다. dropdown open 같은 Local UI State는 가질 수 있다. 다만 API 데이터 흐름은 최소화한다.

Q. Presentational Component의 장점은 뭐야?
A. UI 책임이 명확하고 재사용성과 테스트 가능성이 높다.

Q. Presentational Component에서 loading이나 error를 표시해도 돼?
A. 가능하다. loading과 error 값을 Props로 받아 표시만 하는 것은 Presentational 책임에 맞다.

Q. Presentational Component에서 API 호출하면 왜 안 좋아?
A. 서버 구조에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

---

# 2. Container vs Presentational Comparison

## 2.1 Container vs Presentational Comparison

### [개념]

Container Component와 Presentational Component는 책임이 다르다.

Container는 데이터와 흐름을 준비하고, Presentational은 준비된 데이터를 UI로 표시한다.

---

### [핵심]

비교:

| 비교          | Container Component           | Presentational Component |
| ------------- | ----------------------------- | ------------------------ |
| 핵심 책임     | 데이터 / 상태 / 흐름 관리     | UI 표시                  |
| API 호출      | 가능                          | 지양                     |
| State         | 주요 State 가능               | Local UI State 정도      |
| Props         | 하위 Component에 전달         | 외부에서 받음            |
| Event Handler | 실제 처리 가능                | Callback 호출            |
| 재사용성      | 낮거나 중간                   | 높음                     |
| 테스트        | 흐름 테스트                   | 렌더링 테스트            |
| 위치          | pages / containers / features | components / features    |
| 예            | FestivalSearchContainer       | FestivalList             |

---

### [실무]

사용 기준:

```text
단순 Component
→ 분리하지 않음

복잡한 API + UI 혼합
→ Container / Presentational 분리

동일 UI에 다른 데이터 흐름 연결
→ Presentational 분리

Page 전체 흐름
→ Page가 Container 역할 가능
```

예:

```text
FestivalPage
→ useFestivalSearch
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalResultView
```

이 구조에서는 `FestivalPage`가 Container 역할을 수행하고, `FestivalResultView`가 Presentational 역할을 수행할 수 있다.

---

### [FAQ]

Q. Container와 Presentational 차이는 뭐야?
A. Container는 데이터와 흐름을 관리하고 Presentational은 Props 기반으로 UI를 표시한다.

Q. Page Component는 Container야?
A. 많은 경우 Page Component가 Container 역할을 할 수 있다.

Q. Presentational Component는 도메인 Component가 될 수 있어?
A. 가능하다. 도메인 데이터를 Props로 받아 표시만 한다면 Presentational 성격을 가질 수 있다.

Q. Container와 Presentational을 폴더로 꼭 나눠야 해?
A. 필수는 아니다. 프로젝트 규모와 컨벤션에 따라 구조를 단순하게 유지할 수 있다.

---

## 2.2 When to Separate Container and Presentational

### [개념]

Container and Presentational 분리는 복잡도를 줄이기 위한 선택적 리팩터링 기준이다.

처음부터 모든 Component를 두 계층으로 나누는 것은 불필요할 수 있다.

---

### [핵심]

분리 권장 상황:

- API Logic과 JSX가 섞여 길어진다.
- loading / error / data 상태 분기가 복잡하다.
- Event Handler가 많다.
- 동일 UI를 다른 데이터에서 재사용해야 한다.
- 테스트 단위를 분리하고 싶다.
- Page Component가 너무 커진다.
- Server State와 UI 표시가 강하게 결합되어 있다.

분리 보류 상황:

- Component가 단순하다.
- API 호출이 없다.
- UI와 State 흐름이 간단하다.
- 분리하면 Props만 늘어난다.
- Container가 단순 전달만 한다.
- 프로젝트 규모가 작다.

---

### [실무]

Decision Flow:

```text
Is component simple?
→ Keep together

Is API logic mixed with large JSX?
→ Separate Container and Presentational

Is UI reused with different data source?
→ Extract Presentational Component

Does split reduce complexity?
→ Separate

Does split only add files and props?
→ Keep together
```

좋은 분리 예:

```text
Before:
FestivalSearchPage
- API 요청
- 검색 조건 State
- 목록 렌더링
- 카드 렌더링
- Error UI
- Empty UI
- Pagination

After:
FestivalSearchPage
- State / API 흐름 관리

FestivalSearchView
- 화면 표시

FestivalSearchForm
- 검색 Form

FestivalList
- 목록 표시

FestivalCard
- 단일 항목 표시
```

---

### [FAQ]

Q. Container / Presentational은 언제 분리해?
A. API 로직과 UI Markup이 섞여 복잡해지거나 동일 UI를 다른 데이터 흐름에서 재사용해야 할 때 분리한다.

Q. 처음부터 Container와 Presentational을 나눠야 해?
A. 아니다. 처음에는 단순하게 만들고 복잡해질 때 분리해도 된다.

Q. 분리했는데 Props가 너무 많아지면 어떻게 해?
A. Component Boundary, State Ownership, Props Contract를 다시 검토해야 한다.

Q. Container가 Props만 전달하면 좋은 설계야?
A. 아닐 수 있다. 자체 책임이 없다면 불필요한 중간 Component일 수 있다.

---

# 3. Custom Hook Design

## 3.1 Custom Hook Definition

### [개념]

Custom Hook은 React Component에서 재사용 가능한 State Logic, Effect Logic, API Logic, Event Logic을 분리한 함수다.

Custom Hook 이름은 반드시 `use`로 시작한다.

Custom Hook은 UI를 반환하는 Component가 아니라, 상태, 함수, 계산값, ref 같은 로직 결과를 반환한다.

---

### [핵심]

Custom Hook 분리 대상:

- 반복되는 State Logic
- 반복되는 API Fetch Logic
- Form Logic
- Browser Event Logic
- Timer Logic
- LocalStorage Logic
- Complex Effect Logic
- Pagination Logic
- Search Logic
- Modal Control Logic

Custom Hook 원칙:

- 이름은 `use`로 시작한다.
- UI JSX를 반환하지 않는다.
- 재사용 가능한 로직을 분리한다.
- Component를 읽기 쉽게 만든다.
- Hook 내부에서 다른 Hook을 사용할 수 있다.
- 반환 값은 명확해야 한다.
- Object Return과 Array Return 기준을 구분한다.
- 과도한 Custom Hook 생성은 피한다.

---

### [실무]

분리 전:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<FestivalSummary[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    setLoading(true);
    getFestivals()
      .then(setFestivals)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  return <FestivalList festivals={festivals} loading={loading} error={error} />;
}
```

분리 후:

```tsx
function useFestivals() {
  const [festivals, setFestivals] = useState<FestivalSummary[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    setLoading(true);
    getFestivals()
      .then(setFestivals)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  return { festivals, loading, error };
}
```

사용:

```tsx
function FestivalPage() {
  const { festivals, loading, error } = useFestivals();

  return <FestivalList festivals={festivals} loading={loading} error={error} />;
}
```

---

### [FAQ]

Q. Custom Hook이 뭐야?
A. Component에서 재사용 가능한 상태 로직이나 Effect 로직을 분리한 함수다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?
A. React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

Q. Custom Hook은 UI를 반환해?
A. 일반적으로 UI가 아니라 상태, 함수, 계산값 같은 로직 결과를 반환한다.

Q. Custom Hook은 언제 만들어?
A. 상태 로직이나 Effect 로직이 반복되거나 Component를 복잡하게 만들 때 만든다.

---

## 3.2 Custom Hook Extraction Rules

### [개념]

Custom Hook Extraction은 Component 내부 로직을 Custom Hook으로 분리할지 판단하는 기준이다.

Custom Hook은 Component의 책임을 줄이고, 반복 로직을 재사용하며, API Logic과 UI Logic을 분리하는 데 사용한다.

---

### [핵심]

분리 권장 상황:

- 같은 State Logic이 여러 Component에서 반복된다.
- API 요청 로직이 길다.
- loading / error / data 패턴이 반복된다.
- useEffect가 복잡하다.
- Form 상태 로직이 길다.
- Browser Event Listener가 있다.
- Timer / Interval 로직이 있다.
- LocalStorage 동기화가 있다.
- Component가 로직 때문에 읽기 어렵다.

분리 보류 상황:

- 한 Component에서만 짧게 사용한다.
- 분리 후 이름이 애매하다.
- Hook 반환 값이 너무 많다.
- Hook이 여러 책임을 가진다.
- Hook 내부가 Component보다 더 이해하기 어렵다.

---

### [실무]

Extraction Flow:

```text
Find Complex Logic
→ Check Reuse Possibility
→ Check Effect Complexity
→ Check State Group
→ Define Hook Responsibility
→ Define Return Contract
→ Extract Hook
→ Review Hook Name
```

API Hook 분리 기준:

```text
API 함수 호출
+ loading state
+ error state
+ data state
+ refetch function
→ Custom Hook 후보
```

Form Hook 분리 기준:

```text
Form values
+ validation
+ submit handler
+ reset
+ touched state
→ Custom Hook 후보
```

주의:

```text
useFestivalEverything
→ 너무 많은 책임

useFestivalSearch
→ 검색 기능 API 상태 관리로 명확

useReviewForm
→ 리뷰 Form 상태와 검증으로 명확
```

---

### [FAQ]

Q. Custom Hook으로 분리하는 기준은 뭐야?
A. 로직이 반복되거나 useEffect와 State 관리가 복잡해져 Component 가독성을 떨어뜨릴 때 분리한다.

Q. Custom Hook을 너무 많이 만들면 안 좋아?
A. 그렇다. 이름이 애매하거나 재사용성이 낮은 Hook을 과도하게 만들면 구조가 더 복잡해질 수 있다.

Q. API 요청 로직은 Custom Hook으로 빼는 게 좋아?
A. 반복되거나 loading/error/data 상태가 길어지면 Custom Hook으로 분리하는 것이 좋다.

Q. useEffect가 있으면 무조건 Custom Hook으로 분리해야 해?
A. 아니다. 짧고 Component 책임 안에 있으면 그대로 둘 수 있다.

---

# 4. Custom Hook Return Design

## 4.1 Custom Hook Return Rules

### [개념]

Custom Hook Return Design은 Custom Hook이 Component에 어떤 상태, 함수, 계산값을 제공할지 정의하는 계약이다.

Custom Hook Return은 Component가 Hook을 사용할 때 이해하기 쉽고 안정적이어야 한다.

---

### [핵심]

반환 대상:

- data
- loading
- error
- value
- state
- action function
- refetch
- reset
- submit
- handlers
- computed value

반환 방식:

- Object Return
- Array Return

Object Return 적합:

- 반환 값이 여러 개다.
- 반환 값 이름이 중요하다.
- API Hook이다.
- Form Hook이다.
- loading / error / data가 있다.
- refetch / reset 같은 함수가 있다.

Array Return 적합:

- 반환 값이 짧다.
- 순서 의미가 명확하다.
- useState처럼 `[value, setter]` 구조다.
- useToggle처럼 단순하다.

---

### [실무]

Object Return 예:

```tsx
function useFestivalSearch(params: FestivalSearchParams) {
  return {
    festivals,
    loading,
    error,
    pageInfo,
    refetch,
  };
}
```

사용:

```tsx
const { festivals, loading, error, refetch } = useFestivalSearch(params);
```

Array Return 예:

```tsx
function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  function toggle() {
    setValue((prev) => !prev);
  }

  return [value, toggle, setValue] as const;
}
```

사용:

```tsx
const [isOpen, toggleOpen, setIsOpen] = useToggle(false);
```

선택 기준:

```text
API Hook
→ Object Return

Form Hook
→ Object Return

Toggle Hook
→ Array Return 가능

복잡한 Hook
→ Object Return 우선

반환 값이 3개 이상
→ Object Return 우선
```

---

### [FAQ]

Q. Custom Hook은 Object로 반환하는 게 좋아?
A. 반환 값이 여러 개이고 의미가 중요하면 Object Return이 좋다.

Q. Array Return은 언제 좋아?
A. useState나 useToggle처럼 반환 값의 순서와 의미가 명확하고 짧을 때 적합하다.

Q. Hook 반환 값이 많으면 어떻게 해?
A. Hook 책임이 너무 넓은지 확인하고 여러 Hook으로 분리할 수 있는지 검토한다.

Q. API Hook은 어떤 반환 방식이 좋아?
A. data, loading, error, refetch처럼 의미가 중요한 값이 많으므로 Object Return이 일반적으로 좋다.

---

## 4.2 Custom Hook Return Contract

### [개념]

Custom Hook Return Contract는 Hook이 외부 Component에 제공하는 상태와 함수의 명확한 계약이다.

Hook도 Component와 마찬가지로 외부 사용법이 안정적이어야 한다.

---

### [핵심]

Return Contract 원칙:

- 반환 값 이름을 명확히 한다.
- 반환 값 타입을 안정적으로 유지한다.
- loading / error / data 이름을 통일한다.
- action function 이름을 동사로 작성한다.
- refetch, reset, submit 같은 의도를 드러낸다.
- Hook 내부 구현을 외부에 노출하지 않는다.
- API Response를 그대로 반환할지 ViewModel로 반환할지 결정한다.
- null 가능성을 명확히 한다.

---

### [실무]

좋은 예:

```tsx
type UseFestivalDetailResult = {
  festival: FestivalDetail | null;
  loading: boolean;
  error: Error | null;
  refetch: () => void;
};

function useFestivalDetail(festivalId: number | null): UseFestivalDetailResult {
  // logic
  return { festival, loading, error, refetch };
}
```

나쁜 예:

```tsx
function useFestivalDetail(id: number) {
  return {
    data,
    flag,
    err,
    doIt,
  };
}
```

문제:

```text
data가 무엇인지 모호하다.
flag가 loading인지 success인지 알 수 없다.
doIt이 어떤 함수인지 알 수 없다.
Return Contract가 불명확하다.
```

권장 Naming:

```text
data 이름
→ festival, festivals, reviews, notifications

상태 이름
→ loading, error, success

동작 이름
→ refetch, reset, submit, loadMore
```

---

### [FAQ]

Q. Custom Hook Return Contract가 뭐야?
A. Hook이 외부 Component에 어떤 상태와 함수를 제공하는지 정의하는 계약이다.

Q. Hook 반환 값 이름은 어떻게 지어?
A. data, flag 같은 모호한 이름보다 festivals, loading, error, refetch처럼 의미가 명확한 이름을 사용한다.

Q. Hook이 API Response를 그대로 반환해도 돼?
A. 가능하지만 UI가 서버 구조에 강하게 의존하지 않도록 ViewModel Mapping을 검토할 수 있다.

Q. Hook 반환 타입은 꼭 작성해야 해?
A. TypeScript에서는 복잡한 Hook일수록 반환 타입을 명시하면 Contract가 안정적이다.

---

# 5. API Custom Hook

## 5.1 API Custom Hook Rules

### [개념]

API Custom Hook은 API 요청, loading, error, data, refetch 같은 Server State 흐름을 Component에서 분리하는 Custom Hook이다.

API Custom Hook은 Page Component나 Container Component가 서버 데이터 상태를 쉽게 사용할 수 있게 한다.

---

### [핵심]

API Custom Hook 역할:

- API 함수 호출
- request parameter 사용
- loading 관리
- error 관리
- data 관리
- refetch 제공
- pagination 상태 관리 가능
- response mapping 가능
- cleanup 처리 가능
- race condition 주의

API Custom Hook 원칙:

- UI JSX를 반환하지 않는다.
- API 함수는 별도 api 파일로 분리한다.
- UI Component에서 직접 호출하지 않는다.
- 요청 조건을 parameter로 받는다.
- 반환 값은 Object Return을 우선한다.
- data / loading / error 이름을 일관되게 사용한다.
- 필요한 경우 refetch를 제공한다.

---

### [실무]

API 함수:

```ts
async function getFestivalDetail(festivalId: number): Promise<FestivalDetail> {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return response.json();
}
```

API Hook:

```tsx
function useFestivalDetail(festivalId: number | null) {
  const [festival, setFestival] = useState<FestivalDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const fetchFestival = useCallback(() => {
    if (!festivalId) {
      return;
    }

    setLoading(true);
    setError(null);

    getFestivalDetail(festivalId)
      .then(setFestival)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [festivalId]);

  useEffect(() => {
    fetchFestival();
  }, [fetchFestival]);

  return {
    festival,
    loading,
    error,
    refetch: fetchFestival,
  };
}
```

사용:

```tsx
function FestivalDetailPage({ festivalId }: FestivalDetailPageProps) {
  const { festival, loading, error, refetch } = useFestivalDetail(festivalId);

  return (
    <FestivalDetailView
      festival={festival}
      loading={loading}
      error={error}
      onRetry={refetch}
    />
  );
}
```

---

### [FAQ]

Q. API Custom Hook이 뭐야?
A. API 요청과 loading/error/data 상태를 Component에서 분리한 Custom Hook이다.

Q. API 함수와 API Hook은 뭐가 달라?
A. API 함수는 서버 요청만 담당하고 API Hook은 요청 결과 상태와 React 생명주기 흐름을 관리한다.

Q. API Hook은 어디에서 호출해?
A. Page Component, Container Component, Feature Component에서 호출할 수 있다. 공통 UI Component에서는 지양한다.

Q. API Hook은 무엇을 반환해야 해?
A. 일반적으로 data, loading, error, refetch 같은 값을 Object로 반환한다.

---

## 5.2 API Hook Parameter Rules

### [개념]

API Hook Parameter Rules는 API Custom Hook에 검색 조건, ID, 필터, 페이지 번호 같은 요청 조건을 전달하는 기준이다.

API Hook parameter는 요청 조건을 명확하게 표현해야 하며, Hook 내부에서 API request parameter로 사용된다.

---

### [핵심]

Parameter 대상:

- id
- keyword
- filters
- page
- size
- sort
- enabled
- date range
- query params

Parameter 원칙:

- 단일 ID는 primitive parameter로 받을 수 있다.
- 여러 조건은 object parameter로 묶는다.
- parameter 이름은 API 요청 목적을 드러낸다.
- optional parameter와 enabled 조건을 명확히 한다.
- 불필요하게 Component 전체 Props를 넘기지 않는다.
- API Hook 내부에서 request mapping을 담당할 수 있다.

---

### [실무]

단일 ID Hook:

```tsx
function useFestivalDetail(festivalId: number | null) {
  // festivalId 기반 상세 조회
}
```

검색 조건 Hook:

```tsx
type FestivalSearchParams = {
  keyword: string;
  regionCode?: string;
  themeCode?: string;
  page: number;
  size: number;
};

function useFestivalSearch(params: FestivalSearchParams) {
  // params 기반 검색
}
```

enabled 조건:

```tsx
function useFestivalDetail(festivalId: number | null) {
  useEffect(() => {
    if (!festivalId) {
      return;
    }

    // fetch
  }, [festivalId]);
}
```

주의:

```text
useFestivalSearch(props)
→ props가 너무 포괄적이면 Hook Contract 불명확

useFestivalSearch({ keyword, filters, page })
→ 요청 조건 명확
```

---

### [FAQ]

Q. API Hook parameter는 어떻게 설계해?
A. 단일 ID는 primitive로 받고 여러 검색 조건은 object parameter로 묶는 것이 좋다.

Q. festivalId가 null일 수 있으면 어떻게 해?
A. Hook 내부에서 null일 때 요청하지 않도록 enabled 조건을 둔다.

Q. API Hook에 Component props 전체를 넘겨도 돼?
A. 권장하지 않는다. 요청에 필요한 값만 명확히 전달하는 것이 좋다.

Q. 검색 Hook에는 어떤 parameter가 필요해?
A. keyword, filters, page, size, sort 같은 요청 조건이 필요하다.

---

# 6. Form Custom Hook

## 6.1 Form Custom Hook Rules

### [개념]

Form Custom Hook은 Form values, validation, submit, reset 같은 Form 상태 로직을 Component에서 분리하는 Hook이다.

Form 상태가 복잡하거나 여러 Form에서 반복되는 패턴이 있을 때 Custom Hook으로 분리할 수 있다.

---

### [핵심]

Form Custom Hook 역할:

- form values 관리
- field change 처리
- validation error 관리
- submit handler 제공
- reset 제공
- touched 상태 관리 가능
- dirty 상태 관리 가능
- initial values 관리
- derived validation result 계산

Form Custom Hook 원칙:

- UI JSX를 반환하지 않는다.
- values와 errors 이름을 명확히 한다.
- onSubmit은 외부 callback과 연결한다.
- 단순 Form은 Component 내부 State로 충분할 수 있다.
- 복잡한 Form은 Form Library도 검토 가능하다.
- Hook 책임을 하나의 Form 목적에 맞춘다.

---

### [실무]

Review Form Hook 예:

```tsx
type ReviewFormValues = {
  rating: number;
  content: string;
};

function useReviewForm(onSubmit: (values: ReviewFormValues) => void) {
  const [values, setValues] = useState<ReviewFormValues>({
    rating: 5,
    content: "",
  });

  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  function updateContent(content: string) {
    setValues((prev) => ({ ...prev, content }));
  }

  function updateRating(rating: number) {
    setValues((prev) => ({ ...prev, rating }));
  }

  function submit() {
    if (!values.content.trim()) {
      setErrorMessage("리뷰 내용을 입력해야 합니다.");
      return;
    }

    onSubmit({
      rating: values.rating,
      content: values.content.trim(),
    });
  }

  function reset() {
    setValues({ rating: 5, content: "" });
    setErrorMessage(null);
  }

  return {
    values,
    errorMessage,
    updateContent,
    updateRating,
    submit,
    reset,
  };
}
```

사용:

```tsx
function ReviewForm({ onSubmit }: ReviewFormProps) {
  const { values, errorMessage, updateContent, updateRating, submit } =
    useReviewForm(onSubmit);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    submit();
  }

  return (
    <form onSubmit={handleSubmit}>
      <RatingInput value={values.rating} onChange={updateRating} />
      <textarea
        value={values.content}
        onChange={(event) => updateContent(event.target.value)}
      />
      {errorMessage && <p>{errorMessage}</p>}
      <button type="submit">등록</button>
    </form>
  );
}
```

---

### [FAQ]

Q. Form Custom Hook은 언제 만들어?
A. Form 상태, validation, submit, reset 로직이 길어지거나 반복될 때 만든다.

Q. 모든 Form을 Custom Hook으로 분리해야 해?
A. 아니다. 단순 Form은 Component 내부 State로 충분하다.

Q. Form Hook은 UI를 반환해?
A. 아니다. values, errors, update 함수, submit 함수 같은 로직 결과를 반환한다.

Q. Form Library와 Custom Hook 중 뭐가 좋아?
A. 간단한 Form은 Custom Hook이나 Local State로 충분하고 복잡한 Form은 React Hook Form 같은 라이브러리를 검토할 수 있다.

---

## 6.2 Form Hook Validation Rules

### [개념]

Form Hook Validation Rules는 Form 입력값 검증 로직을 Custom Hook에서 관리할지 결정하는 기준이다.

Validation은 Form Component 내부에 둘 수도 있고, 복잡해지면 Custom Hook 또는 validation utility로 분리할 수 있다.

---

### [핵심]

Validation 대상:

- required
- min length
- max length
- pattern
- email format
- password rule
- rating range
- date range
- file size
- custom business rule

Validation 분리 기준:

- 검증 규칙이 여러 field에 걸쳐 있다.
- submit 전에 여러 검증이 필요하다.
- 실시간 validation이 필요하다.
- 여러 Form에서 같은 validation을 사용한다.
- Component 내부 조건문이 길어진다.
- error state 관리가 복잡하다.

---

### [실무]

Hook 내부 validation 예:

```tsx
function validateReview(values: ReviewFormValues): string | null {
  if (!values.content.trim()) {
    return "리뷰 내용을 입력해야 합니다.";
  }

  if (values.rating < 1 || values.rating > 5) {
    return "평점은 1점부터 5점까지 입력할 수 있습니다.";
  }

  return null;
}
```

사용:

```tsx
function useReviewForm(onSubmit: (values: ReviewFormValues) => void) {
  const [values, setValues] = useState<ReviewFormValues>({
    rating: 5,
    content: "",
  });
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  function submit() {
    const validationError = validateReview(values);

    if (validationError) {
      setErrorMessage(validationError);
      return;
    }

    onSubmit(values);
  }

  return { values, errorMessage, submit };
}
```

분리 판단:

```text
검증이 짧다
→ Component 또는 Hook 내부 유지

검증이 반복된다
→ validation utility 분리

검증이 복잡하다
→ Form Hook 또는 Form Library 검토
```

---

### [FAQ]

Q. Form validation은 어디에 둬야 해?
A. 단순하면 Component 내부에 둘 수 있고, 복잡하거나 반복되면 Custom Hook이나 validation utility로 분리한다.

Q. validation function을 따로 빼는 이유는 뭐야?
A. 검증 규칙을 테스트하기 쉽고 여러 Form에서 재사용할 수 있기 때문이다.

Q. Form Hook이 validation error도 관리해도 돼?
A. 가능하다. values와 errors는 Form Hook에서 함께 관리하는 경우가 많다.

Q. 실시간 validation은 Custom Hook으로 빼는 게 좋아?
A. 검증 로직과 상태 관리가 길어지면 Custom Hook으로 분리하는 것이 좋다.

---

# 7. UI Logic Custom Hook

## 7.1 UI Logic Hook Rules

### [개념]

UI Logic Hook은 Modal, Toggle, Dropdown, Tabs, Pagination 같은 UI 상태 로직을 Component에서 분리하는 Custom Hook이다.

UI Logic Hook은 반복되는 UI 상태 제어 패턴을 재사용 가능하게 만든다.

---

### [핵심]

UI Logic Hook 후보:

- useToggle
- useModal
- useTabs
- useDropdown
- usePagination
- useDisclosure
- useStep
- useDebounce
- useClickOutside
- useLocalStorage

UI Logic Hook 원칙:

- UI 상태와 제어 함수를 반환한다.
- DOM 접근이 필요하면 ref를 반환할 수 있다.
- Hook 이름은 상태 목적을 드러낸다.
- 단순 State 하나는 Hook으로 분리하지 않아도 된다.
- 여러 Component에서 반복될 때 분리한다.
- 접근성 관련 상태를 함께 제공할 수 있다.

---

### [실무]

useToggle 예:

```tsx
function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  function toggle() {
    setValue((prev) => !prev);
  }

  function open() {
    setValue(true);
  }

  function close() {
    setValue(false);
  }

  return {
    value,
    toggle,
    open,
    close,
    setValue,
  };
}
```

사용:

```tsx
function FilterPanel() {
  const { value: isOpen, toggle, close } = useToggle(false);

  return (
    <section>
      <button type="button" aria-expanded={isOpen} onClick={toggle}>
        필터
      </button>
      {isOpen && <FilterOptions onClose={close} />}
    </section>
  );
}
```

usePagination 예:

```tsx
function usePagination(initialPage = 1) {
  const [page, setPage] = useState(initialPage);

  function nextPage() {
    setPage((prev) => prev + 1);
  }

  function prevPage() {
    setPage((prev) => Math.max(1, prev - 1));
  }

  function resetPage() {
    setPage(1);
  }

  return {
    page,
    setPage,
    nextPage,
    prevPage,
    resetPage,
  };
}
```

---

### [FAQ]

Q. UI Logic Hook은 뭐야?
A. Modal, Toggle, Dropdown, Pagination 같은 UI 상태 로직을 분리한 Custom Hook이다.

Q. useToggle은 언제 만들어?
A. open/close/toggle 상태 제어가 여러 Component에서 반복될 때 만든다.

Q. 단순 useState도 Hook으로 빼야 해?
A. 아니다. 반복되거나 제어 함수가 함께 필요할 때 분리한다.

Q. UI Logic Hook은 API 요청을 포함해도 돼?
A. 일반적으로 분리하는 것이 좋다. UI 상태 Hook과 API Hook의 책임을 구분한다.

---

## 7.2 Browser Event Hook Rules

### [개념]

Browser Event Hook은 window, document, DOM event listener 같은 브라우저 이벤트 로직을 Component에서 분리하는 Custom Hook이다.

Event Listener 등록과 cleanup을 안정적으로 관리하기 위해 사용한다.

---

### [핵심]

Browser Event Hook 후보:

- resize event
- scroll event
- keydown event
- click outside
- online / offline status
- visibility change
- media query
- intersection observer

Browser Event Hook 원칙:

- useEffect cleanup을 반드시 고려한다.
- event handler reference 안정성을 고려한다.
- DOM ref가 필요한 경우 ref를 parameter로 받는다.
- SSR 환경이면 window 존재 여부를 확인한다.
- UI Component 내부에 event listener 로직이 길어지면 Hook으로 분리한다.

---

### [실무]

useClickOutside 예:

```tsx
function useClickOutside(
  ref: React.RefObject<HTMLElement>,
  onClickOutside: () => void,
) {
  useEffect(() => {
    function handleMouseDown(event: MouseEvent) {
      if (!ref.current) {
        return;
      }

      if (!ref.current.contains(event.target as Node)) {
        onClickOutside();
      }
    }

    document.addEventListener("mousedown", handleMouseDown);

    return () => {
      document.removeEventListener("mousedown", handleMouseDown);
    };
  }, [ref, onClickOutside]);
}
```

사용:

```tsx
function Dropdown({ onClose }: DropdownProps) {
  const dropdownRef = useRef<HTMLDivElement | null>(null);

  useClickOutside(dropdownRef, onClose);

  return <div ref={dropdownRef}>Dropdown Content</div>;
}
```

주의:

```text
addEventListener만 있고 cleanup이 없다
→ memory leak 위험

event handler가 매번 바뀐다
→ 의도치 않은 재등록 가능

window를 바로 사용한다
→ SSR 환경에서 오류 가능
```

---

### [FAQ]

Q. Browser Event Hook은 언제 만들어?
A. resize, scroll, keydown, click outside 같은 이벤트 등록과 cleanup 로직이 필요할 때 만든다.

Q. Event Listener cleanup은 왜 중요해?
A. Component unmount 후에도 listener가 남으면 memory leak이나 중복 이벤트 문제가 생길 수 있다.

Q. useClickOutside는 어떤 Hook이야?
A. 특정 DOM 영역 밖을 클릭했을 때 callback을 실행하는 Browser Event Hook이다.

Q. SSR 환경에서 Browser Hook은 뭘 주의해야 해?
A. window와 document가 존재하지 않을 수 있으므로 접근 시점을 주의해야 한다.

---

# 8. Custom Hook Anti Patterns

## 8.1 Overgrown Hook Problem

### [개념]

Overgrown Hook Problem은 하나의 Custom Hook이 너무 많은 책임을 가져 이해하기 어렵고 재사용하기 어려워지는 문제다.

Custom Hook도 Component처럼 Single Responsibility가 필요하다.

---

### [핵심]

문제:

- Hook 이름이 포괄적이다.
- 반환 값이 너무 많다.
- State가 너무 많다.
- API 요청이 여러 개 섞여 있다.
- Form Logic과 API Logic과 UI Logic이 섞여 있다.
- Hook 내부 useEffect가 너무 많다.
- 특정 Page에 강하게 결합되어 있다.
- 테스트하기 어렵다.

원인:

- Page 로직을 그대로 Hook 하나로 이동
- Hook Responsibility 미정의
- Custom Hook 분리 기준 부재
- 재사용성 과도 예측
- 여러 Feature Logic 혼합

---

### [실무]

나쁜 예:

```tsx
function useFestivalPage() {
  // search state
  // filter state
  // festival list API
  // festival detail API
  // modal state
  // review form state
  // pagination state
  // navigation logic
}
```

문제:

```text
useFestivalPage가 Page 전체 책임을 모두 가진다.
반환 값이 많아진다.
재사용성이 낮다.
Hook 내부 구조가 Page보다 더 복잡해질 수 있다.
```

개선:

```text
useFestivalSearch
- 검색 조건 기반 목록 API 상태

useFestivalFilters
- 필터 UI 상태

useFestivalDetail
- 선택된 축제 상세 API 상태

useReviewForm
- 리뷰 Form 상태와 검증

useModal
- Modal open / close 상태
```

판단 기준:

```text
Hook 이름이 useSomethingPage처럼 포괄적이다
→ 책임 분리 검토

반환 값이 10개 이상이다
→ Hook 분리 검토

서로 독립적인 useEffect가 많다
→ Hook 분리 검토
```

---

### [FAQ]

Q. Overgrown Hook이 뭐야?
A. 하나의 Custom Hook이 너무 많은 State, Effect, API 로직을 가져 복잡해진 문제다.

Q. Page 로직을 Hook 하나로 빼면 좋은 거 아니야?
A. 항상 좋지 않다. Page 전체 로직을 Hook 하나에 몰아넣으면 Hook이 새로운 Overgrown Component가 될 수 있다.

Q. Hook 반환 값이 많으면 어떻게 해?
A. Hook 책임이 너무 넓은지 확인하고 여러 Custom Hook으로 분리한다.

Q. Custom Hook도 Single Responsibility가 필요해?
A. 필요하다. Hook도 하나의 명확한 로직 책임을 가져야 한다.

---

## 8.2 Unnecessary Hook Problem

### [개념]

Unnecessary Hook Problem은 분리할 필요가 없는 짧고 단순한 로직을 Custom Hook으로 만들어 구조를 불필요하게 복잡하게 만드는 문제다.

Custom Hook은 재사용성이나 복잡도 감소 목적이 있을 때 만들어야 한다.

---

### [핵심]

문제:

- Hook 이름이 애매하다.
- Hook 내부 코드가 useState 한 줄뿐이다.
- 한 Component에서만 사용된다.
- 분리 후 코드 이해가 더 어렵다.
- 파일 수만 증가한다.
- 로직 위치 추적이 어려워진다.
- 재사용 가능성이 실제로 없다.

Hook 생성 보류 기준:

- 단순 Local State
- 짧은 useEffect
- 한 번만 사용되는 이벤트 Handler
- Component 책임 안에 자연스럽게 포함되는 로직
- 분리 후 이름이 불명확한 로직

---

### [실무]

불필요한 Hook 예:

```tsx
function useInputText() {
  return useState("");
}
```

사용:

```tsx
const [title, setTitle] = useInputText();
```

문제:

```text
useState("")보다 의미가 좋아지지 않는다.
Hook 이름이 도메인 의도를 충분히 드러내지 않는다.
재사용성이 낮다.
```

유지해도 되는 예:

```tsx
function SearchForm() {
  const [keyword, setKeyword] = useState("");

  return (
    <input
      value={keyword}
      onChange={(event) => setKeyword(event.target.value)}
    />
  );
}
```

분리할 만한 예:

```tsx
function useDebouncedValue<T>(value: T, delayMs: number) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timeoutId = window.setTimeout(() => {
      setDebouncedValue(value);
    }, delayMs);

    return () => {
      window.clearTimeout(timeoutId);
    };
  }, [value, delayMs]);

  return debouncedValue;
}
```

---

### [FAQ]

Q. Unnecessary Hook이 뭐야?
A. 분리할 필요가 없는 단순 로직을 Custom Hook으로 만들어 구조를 복잡하게 하는 문제다.

Q. useState 하나도 Hook으로 빼야 해?
A. 보통은 아니다. 단순 Local State는 Component 내부에 두는 것이 더 읽기 쉽다.

Q. Custom Hook을 만들기 전에 뭘 확인해야 해?
A. 재사용성, 복잡도 감소, 이름 명확성, 반환 Contract가 있는지 확인해야 한다.

Q. 한 번만 쓰는 Hook은 만들면 안 돼?
A. 항상 금지는 아니지만, 분리로 Component 가독성이 크게 좋아지는 경우가 아니라면 보류할 수 있다.

---

## 8.3 Hook Responsibility Mixing

### [개념]

Hook Responsibility Mixing은 하나의 Custom Hook에 API Logic, UI Logic, Form Logic, Navigation Logic 등 서로 다른 책임이 섞이는 문제다.

Custom Hook은 명확한 목적을 가진 로직 단위로 분리해야 한다.

---

### [핵심]

책임 혼합 예:

- API 요청 + Modal State + Form Validation
- Pagination + Login State + Theme State
- Review Form + Festival Detail API
- Dropdown UI State + Server Mutation
- Navigation Logic + Form Draft State

문제:

- Hook 이름이 포괄적이 된다.
- 재사용성이 낮아진다.
- 반환 값이 많아진다.
- 테스트가 어려워진다.
- 변경 영향 범위가 커진다.
- Component Responsibility가 Hook으로만 이동된다.

해결:

- API Hook 분리
- Form Hook 분리
- UI Logic Hook 분리
- Navigation은 Page 또는 Router 계층에서 처리
- Hook 이름을 책임 단위로 구체화

---

### [실무]

나쁜 예:

```tsx
function useReviewFeature(festivalId: number) {
  // review list API
  // review form values
  // modal open state
  // login redirect navigation
  // toast state
}
```

개선:

```text
useReviews(festivalId)
- 리뷰 목록 API 상태

useReviewForm(onSubmit)
- 리뷰 Form 상태와 validation

useModal()
- Modal open / close 상태

Page Component
- 로그인 여부 확인과 navigation 처리
```

책임 분리 Flow:

```text
List Hook Responsibilities
→ Classify API / Form / UI / Navigation
→ Split by Responsibility
→ Define Return Contract
→ Compose Hooks in Page or Feature Component
```

---

### [FAQ]

Q. Hook Responsibility Mixing이 뭐야?
A. 하나의 Custom Hook에 API, UI, Form, Navigation 같은 서로 다른 책임이 섞이는 문제다.

Q. Hook 안에서 Modal 상태와 API 요청을 같이 관리해도 돼?
A. 관련성이 강하면 가능하지만 재사용성과 책임 분리를 위해 UI Hook과 API Hook을 나누는 것이 좋다.

Q. 여러 Hook은 어디에서 조합해?
A. Page Component, Container Component, Feature Component에서 조합할 수 있다.

Q. Hook 책임은 어떻게 나눠?
A. API Logic, Form Logic, UI Logic, Browser Event Logic, Navigation Logic을 기준으로 나눈다.

---

# 9. Container, Presentational, Custom Hook Integration

## 9.1 Integration Design

### [개념]

Container, Presentational, Custom Hook Integration은 Page 또는 Feature Component에서 Custom Hook으로 로직을 분리하고, Presentational Component에 Props로 UI 상태를 전달하는 구조다.

이 통합 구조는 API Logic, State Logic, UI Logic을 분리하면서도 Component Tree를 명확하게 유지한다.

---

### [핵심]

Integration 구조:

- Page Component는 화면 조립자 역할
- Custom Hook은 로직 담당
- Container는 데이터 흐름 담당
- Presentational은 UI 표시 담당
- UI Component는 재사용 표시 담당
- Callback Props는 이벤트 전달
- Data Down, Action Up 흐름 유지
- API Logic과 UI Logic 분리
- State Ownership 명확화

---

### [실무]

통합 예:

```text
FestivalSearchPage
→ useFestivalSearch
→ usePagination
→ FestivalSearchView
  → FestivalSearchForm
  → FestivalFilterPanel
  → FestivalResultSection
    → FestivalList
      → FestivalCard
```

Page / Container 역할:

```tsx
function FestivalSearchPage() {
  const [keyword, setKeyword] = useState("");
  const { page, setPage, resetPage } = usePagination(1);

  const { festivals, loading, error, refetch } = useFestivalSearch({
    keyword,
    page,
    size: 10,
  });

  function handleSearch(nextKeyword: string) {
    setKeyword(nextKeyword);
    resetPage();
  }

  return (
    <FestivalSearchView
      keyword={keyword}
      festivals={festivals}
      loading={loading}
      error={error}
      page={page}
      onSearch={handleSearch}
      onChangePage={setPage}
      onRetry={refetch}
    />
  );
}
```

Presentational View:

```tsx
function FestivalSearchView({
  festivals,
  loading,
  error,
  page,
  onSearch,
  onChangePage,
  onRetry,
}: FestivalSearchViewProps) {
  return (
    <main>
      <FestivalSearchForm onSearch={onSearch} />
      <FestivalResultSection
        festivals={festivals}
        loading={loading}
        error={error}
        onRetry={onRetry}
      />
      <Pagination page={page} onChangePage={onChangePage} />
    </main>
  );
}
```

---

### [FAQ]

Q. Custom Hook과 Presentational Component는 어떻게 연결해?
A. Page나 Container에서 Custom Hook을 호출하고 결과를 Presentational Component에 Props로 전달한다.

Q. Page가 여러 Hook을 조합해도 돼?
A. 가능하다. Page는 화면 단위 흐름을 조립하는 역할을 할 수 있다.

Q. Integration 구조의 장점은 뭐야?
A. API Logic, State Logic, UI Logic이 분리되어 유지보수와 테스트가 쉬워진다.

Q. Hook을 Presentational Component 안에서 호출해도 돼?
A. 도메인 Presentational에서는 가능할 수 있지만, 공통 UI Component에서는 지양한다. 표시 전용 책임을 유지하는 것이 좋다.

---

## 9.2 Responsibility Mapping

### [개념]

Responsibility Mapping은 Container, Presentational, Custom Hook, UI Component가 각각 어떤 책임을 가져야 하는지 명확히 배치하는 작업이다.

Responsibility Mapping은 Component 설계와 Review에서 기준표로 사용된다.

---

### [핵심]

책임 배치:

| 책임             | 위치 후보                    |
| ---------------- | ---------------------------- |
| API 요청 함수    | api 파일                     |
| API 상태 관리    | API Custom Hook              |
| Page State       | Page / Container             |
| Form Draft State | Form Component / Form Hook   |
| UI Open State    | UI Component / UI Logic Hook |
| Event Handler    | Page / Feature / Container   |
| UI 표시          | Presentational Component     |
| 공통 버튼 표시   | UI Component                 |
| Response Mapping | API Hook / Mapper            |
| Navigation       | Page / Router 계층           |
| Global State     | Context / Store              |

---

### [실무]

Festival Detail 책임 배치:

```text
festivalApi.ts
- getFestivalDetail

useFestivalDetail
- festival detail API 상태
- loading / error / refetch

FestivalDetailPage
- festivalId 획득
- useFestivalDetail 호출
- navigation 처리

FestivalDetailView
- festival detail 표시
- loading / error / empty 표시

FestivalMap
- 지도 영역 표시

Button
- 공통 버튼 표시
```

Review 기준:

```text
API URL이 UI Component에 있다
→ api 파일 또는 API Hook으로 이동

Form validation이 Page에 너무 많다
→ Form Hook 또는 Form Component로 이동

Modal open State가 App에 있다
→ 가까운 Feature 또는 UI Logic Hook으로 이동

Navigation이 UI Button 내부에 있다
→ Page 또는 Router 계층으로 이동
```

---

### [FAQ]

Q. Responsibility Mapping이 뭐야?
A. API, State, Event, UI 표시 책임을 적절한 파일과 Component에 배치하는 작업이다.

Q. API 요청 함수는 어디에 둬?
A. 일반적으로 api 파일에 두고 Hook이나 Page에서 호출한다.

Q. Navigation Logic은 어디에 둬?
A. Page Component나 Router 계층에서 처리하는 것이 좋다. 공통 UI Component 내부에 넣지 않는다.

Q. Response Mapping은 어디서 해?
A. API Hook, mapper 함수, Container에서 처리할 수 있다.

---

# 10. Review Checklist

## 10.1 Container Presentational Custom Hook Checklist

### [개념]

Container, Presentational, Custom Hook Checklist는 데이터 흐름, UI 표시, 로직 분리가 적절한지 검수하기 위한 기준이다.

Frontend Agent와 Review Agent는 Component 코드 생성 전후에 책임 배치와 Hook 설계를 함께 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Container Component의 책임이 데이터와 흐름 관리로 명확한가?
- [ ] Presentational Component가 Props 기반으로 UI를 표시하는가?
- [ ] Presentational Component가 API 호출을 하지 않는가?
- [ ] Page Component가 Container 역할을 겸하는 경우 책임이 과도하지 않은가?
- [ ] Container / Presentational 분리가 실제 복잡도를 줄이는가?
- [ ] 불필요한 Container가 생기지 않았는가?
- [ ] Custom Hook 이름이 use로 시작하는가?
- [ ] Custom Hook 책임이 한 문장으로 설명되는가?
- [ ] Custom Hook이 UI JSX를 반환하지 않는가?
- [ ] API Logic과 UI Logic이 Hook 안에서 섞이지 않았는가?
- [ ] API Hook이 data/loading/error/refetch를 명확히 반환하는가?
- [ ] Form Hook이 values/errors/submit/reset을 명확히 반환하는가?
- [ ] UI Logic Hook이 상태와 제어 함수를 명확히 반환하는가?
- [ ] Hook 반환 값이 너무 많지 않은가?
- [ ] Hook 이름이 너무 포괄적이지 않은가?
- [ ] 단순 Local State를 불필요하게 Hook으로 분리하지 않았는가?
- [ ] Event Listener Hook에 cleanup이 있는가?
- [ ] Page / Container에서 여러 Hook을 적절히 조합하는가?
- [ ] Responsibility Mapping이 명확한가?
```

---

### [실무]

Review Flow:

```text
Component Tree Review
→ Container Responsibility Check
→ Presentational Responsibility Check
→ API Logic Location Check
→ Custom Hook Responsibility Check
→ Hook Return Contract Check
→ Hook Anti Pattern Check
→ Integration Flow Check
```

치명적 문제:

```text
- Presentational Component가 직접 API 호출
- UI Component가 서버 데이터 State 소유
- Custom Hook이 Page 전체 책임을 모두 가짐
- Hook 반환 값이 과도하게 많음
- API Logic / Form Logic / UI Logic이 하나의 Hook에 섞임
- Event Listener cleanup 누락
- Container가 책임 없이 Props만 전달
- 분리 후 구조가 더 복잡해짐
```

---

### [FAQ]

Q. Container / Presentational / Custom Hook 검수에서 가장 중요한 것은?
A. 데이터 흐름, UI 표시, 로직 책임이 명확히 분리되어 있는지 확인하는 것이다.

Q. 치명적인 문제는 뭐야?
A. Presentational Component가 API를 호출하거나 Custom Hook이 너무 많은 책임을 가지는 경우다.

Q. Hook 검수에서 가장 먼저 볼 것은?
A. Hook 이름과 책임이 명확한지, 반환 Contract가 안정적인지 확인해야 한다.

Q. 분리 후 구조가 더 복잡해지면 어떻게 해?
A. Container / Presentational 분리나 Custom Hook 추출을 되돌리거나 더 단순한 구조로 재설계한다.

---

# 11. Agent Output Rules

## 11.1 Frontend Agent Output Rules

### [개념]

Frontend Agent는 React 화면 코드를 생성하기 전에 Container, Presentational, Custom Hook 책임을 명확히 설계해야 한다.

Agent Output은 Component 역할, Hook 역할, 데이터 흐름, Props 흐름, Anti Pattern Review를 포함해야 한다.

---

### [핵심]

Frontend Agent 출력 항목:

- Page Component
- Container Component 여부
- Presentational Component 여부
- Custom Hook 목록
- API Hook 목록
- Form Hook 목록
- UI Logic Hook 목록
- Responsibility Mapping
- Data Down Flow
- Action Up Flow
- Hook Return Contract
- Props Contract
- Anti Pattern Review

---

### [실무]

출력 예:

```text
Page:
FestivalSearchPage
- role: Container 역할 겸함
- responsibility: 검색 조건 State, API Hook 호출, 이벤트 흐름 관리

Custom Hooks:
useFestivalSearch
- responsibility: 축제 검색 API 상태 관리
- return: festivals, loading, error, refetch

usePagination
- responsibility: page State와 페이지 변경 함수 관리
- return: page, setPage, nextPage, prevPage, resetPage

Presentational:
FestivalSearchView
- responsibility: 검색 화면 UI 조립
- props: festivals, loading, error, page, onSearch, onChangePage, onRetry

Feature Components:
FestivalSearchForm
- responsibility: 검색어 입력과 submit 이벤트 전달

FestivalResultSection
- responsibility: loading / error / empty / list 상태 표시

Reusable UI:
Button, EmptyState, ErrorMessage, Pagination
```

Anti Pattern Review:

```text
- Presentational Component API 호출 없음
- UI Component 서버 데이터 직접 소유 없음
- Hook 반환 값 과도하지 않음
- API Logic과 Form Logic 분리
- Container가 단순 Props 전달만 하지 않음
```

---

### [FAQ]

Q. Frontend Agent는 Container와 Hook을 언제 설계해야 해?
A. Component 코드 생성 전에 데이터 흐름과 로직 분리 기준을 먼저 설계해야 한다.

Q. Agent Output에는 Hook Return Contract도 포함해야 해?
A. 포함하는 것이 좋다. Hook 사용법과 반환 값이 명확해야 코드 생성 품질이 높아진다.

Q. Presentational Component Output에는 무엇이 필요해?
A. Props Contract, 표시 책임, loading/error/empty 처리 여부, Callback Props가 필요하다.

Q. Review Agent는 이 출력에서 무엇을 검토해야 해?
A. 책임 분리, Hook 과도화, API Logic 위치, Props 흐름, Anti Pattern 여부를 검토해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Container and Presentational Pattern이 뭐야?
A. 데이터 흐름과 UI 표시 책임을 분리하는 React Component 설계 방식이다.

Q. Container Component는 뭐야?
A. API 요청, State 관리, Event Handler, 데이터 변환 같은 흐름을 담당하는 Component다.

Q. Presentational Component는 뭐야?
A. 전달받은 Props를 기반으로 UI를 표시하는 Component다.

Q. Container와 Presentational은 항상 분리해야 해?
A. 아니다. 복잡도를 줄일 때만 사용한다. 단순 Component에는 과한 설계가 될 수 있다.

Q. Container Component는 어떤 책임을 가져?
A. 데이터 로딩, State 관리, Event Handler, API 흐름, 데이터 변환을 담당한다.

Q. Container Component가 JSX를 렌더링하면 안 돼?
A. 일부 렌더링은 가능하다. 다만 핵심 책임은 데이터와 흐름 관리이며 UI Markup이 과도하면 분리한다.

Q. Page Component가 Container 역할을 해도 돼?
A. 가능하다. 많은 경우 Page Component가 화면 단위 Container 역할을 한다.

Q. Presentational Component는 State를 가지면 안 돼?
A. 항상 금지는 아니다. dropdown open 같은 Local UI State는 가질 수 있다. 다만 API 데이터 흐름은 최소화한다.

Q. Presentational Component의 장점은 뭐야?
A. UI 책임이 명확하고 재사용성과 테스트 가능성이 높다.

Q. Presentational Component에서 API 호출하면 왜 안 좋아?
A. 서버 구조에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

Q. Container와 Presentational 차이는 뭐야?
A. Container는 데이터와 흐름을 관리하고 Presentational은 Props 기반으로 UI를 표시한다.

Q. Page Component는 Container야?
A. 많은 경우 Page Component가 Container 역할을 할 수 있다.

Q. Container / Presentational은 언제 분리해?
A. API 로직과 UI Markup이 섞여 복잡해지거나 동일 UI를 다른 데이터 흐름에서 재사용해야 할 때 분리한다.

Q. 처음부터 Container와 Presentational을 나눠야 해?
A. 아니다. 처음에는 단순하게 만들고 복잡해질 때 분리해도 된다.

Q. Custom Hook이 뭐야?
A. Component에서 재사용 가능한 상태 로직이나 Effect 로직을 분리한 함수다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?
A. React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

Q. Custom Hook은 UI를 반환해?
A. 일반적으로 UI가 아니라 상태, 함수, 계산값 같은 로직 결과를 반환한다.

Q. Custom Hook은 언제 만들어?
A. 상태 로직이나 Effect 로직이 반복되거나 Component를 복잡하게 만들 때 만든다.

Q. Custom Hook으로 분리하는 기준은 뭐야?
A. 로직이 반복되거나 useEffect와 State 관리가 복잡해져 Component 가독성을 떨어뜨릴 때 분리한다.

Q. Custom Hook을 너무 많이 만들면 안 좋아?
A. 그렇다. 이름이 애매하거나 재사용성이 낮은 Hook을 과도하게 만들면 구조가 더 복잡해질 수 있다.

Q. API 요청 로직은 Custom Hook으로 빼는 게 좋아?
A. 반복되거나 loading/error/data 상태가 길어지면 Custom Hook으로 분리하는 것이 좋다.

Q. useEffect가 있으면 무조건 Custom Hook으로 분리해야 해?
A. 아니다. 짧고 Component 책임 안에 있으면 그대로 둘 수 있다.

Q. Custom Hook은 Object로 반환하는 게 좋아?
A. 반환 값이 여러 개이고 의미가 중요하면 Object Return이 좋다.

Q. Array Return은 언제 좋아?
A. useState나 useToggle처럼 반환 값의 순서와 의미가 명확하고 짧을 때 적합하다.

Q. Hook 반환 값이 많으면 어떻게 해?
A. Hook 책임이 너무 넓은지 확인하고 여러 Hook으로 분리할 수 있는지 검토한다.

Q. API Hook은 어떤 반환 방식이 좋아?
A. data, loading, error, refetch처럼 의미가 중요한 값이 많으므로 Object Return이 일반적으로 좋다.

Q. Custom Hook Return Contract가 뭐야?
A. Hook이 외부 Component에 어떤 상태와 함수를 제공하는지 정의하는 계약이다.

Q. Hook 반환 값 이름은 어떻게 지어?
A. data, flag 같은 모호한 이름보다 festivals, loading, error, refetch처럼 의미가 명확한 이름을 사용한다.

Q. API Custom Hook이 뭐야?
A. API 요청과 loading/error/data 상태를 Component에서 분리한 Custom Hook이다.

Q. API 함수와 API Hook은 뭐가 달라?
A. API 함수는 서버 요청만 담당하고 API Hook은 요청 결과 상태와 React 생명주기 흐름을 관리한다.

Q. API Hook은 어디에서 호출해?
A. Page Component, Container Component, Feature Component에서 호출할 수 있다. 공통 UI Component에서는 지양한다.

Q. API Hook parameter는 어떻게 설계해?
A. 단일 ID는 primitive로 받고 여러 검색 조건은 object parameter로 묶는 것이 좋다.

Q. festivalId가 null일 수 있으면 어떻게 해?
A. Hook 내부에서 null일 때 요청하지 않도록 enabled 조건을 둔다.

Q. Form Custom Hook은 언제 만들어?
A. Form 상태, validation, submit, reset 로직이 길어지거나 반복될 때 만든다.

Q. 모든 Form을 Custom Hook으로 분리해야 해?
A. 아니다. 단순 Form은 Component 내부 State로 충분하다.

Q. Form Hook은 UI를 반환해?
A. 아니다. values, errors, update 함수, submit 함수 같은 로직 결과를 반환한다.

Q. Form validation은 어디에 둬야 해?
A. 단순하면 Component 내부에 둘 수 있고, 복잡하거나 반복되면 Custom Hook이나 validation utility로 분리한다.

Q. UI Logic Hook은 뭐야?
A. Modal, Toggle, Dropdown, Pagination 같은 UI 상태 로직을 분리한 Custom Hook이다.

Q. useToggle은 언제 만들어?
A. open/close/toggle 상태 제어가 여러 Component에서 반복될 때 만든다.

Q. Browser Event Hook은 언제 만들어?
A. resize, scroll, keydown, click outside 같은 이벤트 등록과 cleanup 로직이 필요할 때 만든다.

Q. Event Listener cleanup은 왜 중요해?
A. Component unmount 후에도 listener가 남으면 memory leak이나 중복 이벤트 문제가 생길 수 있다.

Q. Overgrown Hook이 뭐야?
A. 하나의 Custom Hook이 너무 많은 State, Effect, API 로직을 가져 복잡해진 문제다.

Q. Page 로직을 Hook 하나로 빼면 좋은 거 아니야?
A. 항상 좋지 않다. Page 전체 로직을 Hook 하나에 몰아넣으면 Hook이 새로운 Overgrown Component가 될 수 있다.

Q. Unnecessary Hook이 뭐야?
A. 분리할 필요가 없는 단순 로직을 Custom Hook으로 만들어 구조를 복잡하게 하는 문제다.

Q. useState 하나도 Hook으로 빼야 해?
A. 보통은 아니다. 단순 Local State는 Component 내부에 두는 것이 더 읽기 쉽다.

Q. Hook Responsibility Mixing이 뭐야?
A. 하나의 Custom Hook에 API, UI, Form, Navigation 같은 서로 다른 책임이 섞이는 문제다.

Q. Hook 책임은 어떻게 나눠?
A. API Logic, Form Logic, UI Logic, Browser Event Logic, Navigation Logic을 기준으로 나눈다.

Q. Custom Hook과 Presentational Component는 어떻게 연결해?
A. Page나 Container에서 Custom Hook을 호출하고 결과를 Presentational Component에 Props로 전달한다.

Q. Responsibility Mapping이 뭐야?
A. API, State, Event, UI 표시 책임을 적절한 파일과 Component에 배치하는 작업이다.

Q. Container / Presentational / Custom Hook 검수에서 가장 중요한 것은?
A. 데이터 흐름, UI 표시, 로직 책임이 명확히 분리되어 있는지 확인하는 것이다.

Q. React Component Design Part05의 핵심은 뭐야?
A. Container, Presentational, Custom Hook을 통해 데이터 흐름, UI 표시, API Logic, Form Logic, UI Logic 책임을 명확히 분리하는 것이다.

# React Component Design Part06 - Reusable Component, API Logic Separation, TypeScript Component

---

# 1. Reusable Component

## 1.1 Reusable Component Definition

### [개념]

Reusable Component는 여러 화면과 Feature에서 반복 사용할 수 있도록 도메인 의존성을 줄이고 Props 기반으로 동작과 표시를 제어하는 React Component다.

Reusable Component는 단순히 여러 곳에서 사용할 수 있게 만든 Component가 아니다.

Reusable Component는 Component Responsibility가 명확하고, Props Contract가 안정적이며, 도메인 데이터와 API Logic에 강하게 결합되지 않아야 한다.

---

### [핵심]

- Reusable Component는 여러 화면에서 반복 사용 가능한 Component다.
- Reusable Component는 도메인 의존성을 줄인다.
- Reusable Component는 API 호출을 하지 않는다.
- Reusable Component는 Props 기반으로 표시한다.
- Reusable Component는 Callback Props로 이벤트를 알린다.
- Reusable Component는 children, variant, size, disabled 같은 일반 Props를 사용할 수 있다.
- Reusable Component는 접근성 기본 구조를 포함해야 한다.
- Reusable Component는 className 확장을 고려할 수 있다.
- 실제 반복이 확인된 후 추출하는 것이 안전하다.
- 미래 재사용성을 과도하게 예측하면 Over-Abstraction이 된다.

---

### [실무]

2026 실무 기준에서 Reusable Component는 Design System 전체를 처음부터 만드는 방식이 아니다.

먼저 Feature 내부에서 반복되는 UI를 확인하고, 실제 반복 패턴이 안정되면 공통 Component로 추출한다.

Reusable Component 후보:

```text
Button
Input
Select
Checkbox
Modal
Card
Badge
Spinner
EmptyState
ErrorMessage
Pagination
PageHeader
SectionHeader
```

좋은 Reusable Component 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section className="empty-state">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

좋은 점:

```text
- 도메인 데이터 의존 없음
- title, description, action으로 역할 명확
- 여러 화면에서 재사용 가능
- ReactNode action으로 버튼 영역 커스터마이징 가능
```

나쁜 Reusable Component 예:

```tsx
function EmptyState() {
  return (
    <section>
      <h2>축제가 없습니다.</h2>
      <button onClick={() => (window.location.href = "/festivals")}>
        축제 보러가기
      </button>
    </section>
  );
}
```

문제:

```text
- 축제 도메인에 강하게 결합
- 페이지 이동 정책을 직접 가짐
- 다른 화면에서 재사용하기 어려움
```

---

### [FAQ]

Q. Reusable Component가 뭐야?
A. 여러 화면과 Feature에서 반복 사용할 수 있도록 도메인 의존성을 줄이고 Props 기반으로 설계한 Component다.

Q. Reusable Component는 언제 만들어?
A. 여러 화면에서 같은 UI가 반복되고 도메인 로직 없이 Props로 제어할 수 있을 때 만든다.

Q. 처음부터 공통 Component를 많이 만들면 좋아?
A. 아니다. 실제 반복과 필요가 확인된 후 추출하는 것이 안전하다.

Q. Reusable Component는 API 호출을 해도 돼?
A. 권장하지 않는다. Reusable Component는 표시와 상호작용만 담당하고 API Logic은 Page, Feature, Hook, API 계층에서 처리한다.

---

## 1.2 Reusable Component Criteria

### [개념]

Reusable Component Criteria는 어떤 Component를 공통 Component로 추출할지 판단하는 기준이다.

Reusable Component는 반복 사용 가능성, 도메인 독립성, Props 안정성, 접근성, 스타일 확장성을 기준으로 검토한다.

---

### [핵심]

Reusable Component 판단 기준:

- 여러 화면에서 반복되는가?
- 도메인 로직 없이 동작 가능한가?
- Props로 데이터와 상태를 주입할 수 있는가?
- API Response 구조를 몰라도 되는가?
- Callback Props로 이벤트만 알릴 수 있는가?
- variant와 size가 제한된 값으로 설계되는가?
- 접근성 기본 기준을 포함할 수 있는가?
- className 확장이 필요한가?
- Component 이름이 범용 역할을 드러내는가?
- 실제 반복 패턴이 확인되었는가?

추출 보류 기준:

- 한 화면에서만 사용된다.
- 도메인 데이터에 강하게 의존한다.
- Props가 너무 많아진다.
- variant가 과도하게 늘어난다.
- 이름이 모호하다.
- 추출 후 사용법이 더 어려워진다.

---

### [실무]

판단 Flow:

```text
Find Repeated UI
→ Check Domain Dependency
→ Check Props Contract
→ Check Event Flow
→ Check Accessibility
→ Check Variant Need
→ Extract Reusable Component
```

좋은 추출 후보:

```text
여러 Form에서 같은 Button 사용
→ Button 추출

여러 화면에서 같은 빈 상태 표시
→ EmptyState 추출

여러 Feature에서 같은 Modal 구조 사용
→ Modal 추출

여러 목록에서 같은 Loading 표시
→ Spinner 또는 LoadingView 추출
```

추출 보류 후보:

```text
FestivalCard
→ 축제 도메인 데이터 사용
→ Feature Component 유지 가능

ReviewItem
→ 리뷰 도메인 데이터 사용
→ Feature Component 유지 가능

OneLineTitleText
→ 책임이 약함
→ 추출 보류
```

---

### [FAQ]

Q. Reusable Component 추출 기준은 뭐야?
A. 반복 사용, 도메인 독립성, Props 안정성, 접근성, 스타일 확장성을 기준으로 판단한다.

Q. FestivalCard는 Reusable Component야?
A. 축제 도메인 데이터에 의존하면 Feature Component 또는 Domain Component에 가깝다.

Q. Button은 Reusable Component야?
A. 일반적으로 그렇다. 도메인과 무관하고 여러 화면에서 반복 사용되기 때문이다.

Q. 반복되지 않는 Component도 공통화해야 해?
A. 권장하지 않는다. 실제 반복이 확인된 후 추출하는 것이 안전하다.

---

# 2. Variant and Style Props

## 2.1 Variant Props Design

### [개념]

Variant Props는 Reusable Component의 시각적 또는 의미적 변형을 제한된 값으로 표현하는 Props다.

Variant는 여러 boolean props보다 안정적이고, Component 변형을 명확하게 제한할 수 있다.

---

### [핵심]

Variant Props 사용 대상:

- Button variant
- Badge status
- Alert type
- Toast type
- Card tone
- Text intent
- Size
- Color intent
- Semantic status

Variant Props 원칙:

- 가능한 값을 union type으로 제한한다.
- 의미 기반 이름을 사용한다.
- boolean 여러 개보다 variant를 우선한다.
- variant와 size를 분리한다.
- variant가 너무 많아지면 Component 책임을 재검토한다.
- 시각 이름보다 의미 이름을 우선한다.
- variant 조합이 복잡하면 Component 분리를 검토한다.

---

### [실무]

Button Variant 예:

```tsx
type ButtonVariant = "primary" | "secondary" | "danger";
type ButtonSize = "sm" | "md" | "lg";

type ButtonProps = {
  type?: "button" | "submit" | "reset";
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  type = "button",
  variant = "primary",
  size = "md",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button-${variant} button-${size}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

나쁜 예:

```tsx
type ButtonProps = {
  primary?: boolean;
  secondary?: boolean;
  danger?: boolean;
};
```

문제:

```text
primary와 danger가 동시에 true가 될 수 있다.
불가능한 상태가 생긴다.
조건부 className이 복잡해진다.
```

개선:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
};
```

---

### [FAQ]

Q. Variant Props가 뭐야?
A. Component의 상태나 스타일 변형을 제한된 문자열 값으로 표현하는 Props다.

Q. variant는 왜 써?
A. Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. boolean props 대신 variant를 쓰는 기준은 뭐야?
A. 여러 상태 중 하나만 선택되어야 하면 boolean 여러 개보다 variant가 적합하다.

Q. variant와 size는 왜 분리해?
A. variant는 의미나 의도, size는 크기를 나타내므로 책임이 다르기 때문이다.

---

## 2.2 className and Style Responsibility

### [개념]

className and Style Responsibility는 Component가 어떤 스타일 책임을 내부에서 가지고, 어떤 배치 책임을 부모에게 맡길지 결정하는 기준이다.

Reusable Component는 자체 스타일을 가질 수 있지만 외부 배치 margin과 layout 책임은 부모가 관리하는 경우가 많다.

---

### [핵심]

Style Responsibility 기준:

- Component 자체 스타일은 내부 className으로 관리한다.
- 외부 배치와 margin은 부모 Layout이 관리할 수 있다.
- Reusable Component는 className 확장을 고려할 수 있다.
- inline style 남용은 피한다.
- variant class를 명확히 만든다.
- layout style과 component style을 구분한다.
- 도메인 Component와 UI Component의 스타일 책임을 구분한다.
- style prop으로 모든 스타일을 주입하는 방식은 주의한다.

---

### [실무]

className 확장 예:

```tsx
type CardProps = {
  title?: string;
  className?: string;
  children: React.ReactNode;
};

function Card({ title, className = "", children }: CardProps) {
  return (
    <section className={`card ${className}`}>
      {title && <h2>{title}</h2>}
      {children}
    </section>
  );
}
```

Style 책임 구분:

```text
Card
- border
- background
- padding
- radius

Parent Layout
- margin
- grid placement
- section spacing
```

주의:

```tsx
function Button({ style }: { style: React.CSSProperties }) {
  return <button style={style}>Button</button>;
}
```

문제:

```text
모든 스타일을 외부에서 주입하면 Component 일관성이 무너질 수 있다.
variant, size, className 중심 설계를 우선 검토한다.
```

---

### [FAQ]

Q. Component margin은 내부에서 줘도 돼?
A. 상황에 따라 다르지만 Reusable UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?
A. 재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

Q. inline style은 쓰면 안 돼?
A. 금지는 아니지만 반복 UI에서는 className, variant, CSS class 기반 스타일이 더 유지보수에 좋다.

Q. style prop으로 모든 스타일을 주입하면 안 좋아?
A. 일관성이 떨어질 수 있다. variant와 className 확장으로 해결 가능한지 먼저 검토한다.

---

# 3. API Logic Separation

## 3.1 API Logic Separation Definition

### [개념]

API Logic Separation은 Component 내부의 서버 요청 로직을 api 함수, Custom Hook, Data Fetching 계층으로 분리하는 설계 기준이다.

React Component는 UI 표시와 사용자 이벤트에 집중하고, API URL, request parameter mapping, response mapping, error handling은 별도 계층으로 분리할 수 있다.

---

### [핵심]

API Logic Separation 대상:

- fetch / axios request
- request URL
- request parameter mapping
- request body mapping
- response mapping
- error handling
- loading / error / data state
- retry / refetch
- pagination data loading
- authorization header handling

분리 원칙:

- API 요청 함수는 api 파일에 둔다.
- API 상태 로직은 Custom Hook으로 분리할 수 있다.
- UI Component는 API 호출을 직접 하지 않는다.
- Page 또는 Container는 API Hook을 호출할 수 있다.
- Response Mapping은 API Hook 또는 mapper에서 처리한다.
- API Response 구조를 Presentational Component에 강제하지 않는다.

---

### [실무]

나쁜 예:

```tsx
function FestivalCard({ festivalId }: { festivalId: number }) {
  useEffect(() => {
    fetch(`/api/festivals/${festivalId}`)
      .then((res) => res.json())
      .then((data) => console.log(data));
  }, [festivalId]);

  return <article>Festival</article>;
}
```

문제:

```text
FestivalCard가 API URL을 알고 있다.
UI 표시 Component가 서버 요청 책임을 가진다.
재사용성과 테스트 가능성이 낮다.
```

개선 API 함수:

```ts
async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalDetailResponse> {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return response.json();
}
```

개선 API Hook:

```tsx
function useFestivalDetail(festivalId: number | null) {
  const [festival, setFestival] = useState<FestivalDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!festivalId) {
      return;
    }

    setLoading(true);
    setError(null);

    getFestivalDetail(festivalId)
      .then((response) => setFestival(mapFestivalDetail(response)))
      .catch(setError)
      .finally(() => setLoading(false));
  }, [festivalId]);

  return { festival, loading, error };
}
```

Component:

```tsx
function FestivalDetailPage({ festivalId }: FestivalDetailPageProps) {
  const { festival, loading, error } = useFestivalDetail(festivalId);

  return (
    <FestivalDetailView festival={festival} loading={loading} error={error} />
  );
}
```

---

### [FAQ]

Q. API Logic Separation이 뭐야?
A. Component 내부의 서버 요청 로직을 api 함수, Custom Hook, Data Fetching 계층으로 분리하는 설계 기준이다.

Q. API 호출을 Component 안에 쓰면 안 돼?
A. 간단한 화면에서는 가능하지만 재사용되거나 길어지면 api 함수나 Custom Hook으로 분리하는 것이 좋다.

Q. UI Component에서 fetch를 하면 왜 안 좋아?
A. UI Component가 서버 구조에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

Q. API URL은 어디에 두는 게 좋아?
A. 일반적으로 api 파일에 두고 Component는 API 함수나 API Hook을 통해 사용한다.

---

## 3.2 API Function Rules

### [개념]

API Function은 서버 요청 자체를 담당하는 함수다.

API Function은 React Component와 분리되어 request URL, method, parameter, body, response parsing, error throwing을 처리한다.

---

### [핵심]

API Function 역할:

- endpoint 호출
- HTTP method 지정
- query parameter 구성
- request body 구성
- response parsing
- error throwing
- 인증 header 연결 가능
- API Response Type 반환

API Function 원칙:

- UI JSX를 알지 않는다.
- React Hook을 사용하지 않는다.
- Component State를 직접 변경하지 않는다.
- 요청에 필요한 parameter만 받는다.
- API Response Type을 명확히 한다.
- 네트워크 오류와 서버 오류를 처리할 기준을 둔다.
- axios instance 또는 fetch wrapper를 사용할 수 있다.

---

### [실무]

API Function 예:

```ts
type FestivalSearchRequest = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  page: number;
  size: number;
};

async function searchFestivals(
  request: FestivalSearchRequest,
): Promise<FestivalSearchResponse> {
  const params = new URLSearchParams();

  if (request.keyword) {
    params.set("keyword", request.keyword);
  }

  if (request.regionCode) {
    params.set("regionCode", request.regionCode);
  }

  if (request.themeCode) {
    params.set("themeCode", request.themeCode);
  }

  params.set("page", String(request.page));
  params.set("size", String(request.size));

  const response = await fetch(`/api/festivals?${params.toString()}`);

  if (!response.ok) {
    throw new Error("Failed to search festivals");
  }

  return response.json();
}
```

좋은 점:

```text
- React Component와 분리
- request parameter mapping 명확
- response type 명확
- error 기준 명확
```

금지:

```tsx
async function searchFestivalsAndSetState(setFestivals) {
  const response = await fetch("/api/festivals");
  setFestivals(await response.json());
}
```

문제:

```text
API Function이 React State setter에 의존한다.
Component와 API 계층이 결합된다.
```

---

### [FAQ]

Q. API Function은 뭐야?
A. 서버 요청 자체를 담당하는 함수다.

Q. API Function에서 useState를 써도 돼?
A. 안 된다. API Function은 React Hook을 사용하지 않고 요청과 응답 처리만 담당해야 한다.

Q. API Function은 State setter를 받아도 돼?
A. 권장하지 않는다. API Function은 State 변경이 아니라 서버 요청 결과 반환에 집중해야 한다.

Q. API Function의 반환 타입은 왜 중요해?
A. API Hook과 Component가 응답 구조를 안정적으로 사용할 수 있게 해주기 때문이다.

---

# 4. API Response Mapping

## 4.1 Response Mapping Definition

### [개념]

Response Mapping은 서버 API Response를 UI Component가 사용하기 쉬운 ViewModel 또는 Props 구조로 변환하는 작업이다.

Response Mapping은 서버 응답 필드와 화면 표시 Component 사이의 결합도를 줄인다.

---

### [핵심]

Response Mapping 대상:

- field name 변경
- null 처리
- 날짜 표시 문자열 변환
- status code를 label로 변환
- image URL 보정
- region code를 regionName으로 변환
- API nested data flatten
- 화면 표시용 boolean 계산
- pagination 정보 정리

Response Mapping 원칙:

- API Response를 UI Component에 그대로 강제하지 않는다.
- 화면 표시용 ViewModel을 만들 수 있다.
- Mapping 위치는 API Hook, mapper 함수, Container가 될 수 있다.
- 원본 데이터와 표시용 데이터를 구분한다.
- Reusable UI Component는 API Response Type을 몰라야 한다.

---

### [실무]

API Response:

```ts
type FestivalResponse = {
  id: number;
  name: string;
  img_url: string | null;
  sigungu: string;
  start_date: string;
  end_date: string;
};
```

ViewModel:

```ts
type FestivalCardViewModel = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  periodText: string;
};
```

Mapper:

```ts
function mapFestivalToCardViewModel(
  festival: FestivalResponse,
): FestivalCardViewModel {
  return {
    festivalId: festival.id,
    title: festival.name,
    imageUrl: festival.img_url,
    regionName: festival.sigungu,
    periodText: `${festival.start_date} ~ ${festival.end_date}`,
  };
}
```

사용:

```tsx
function FestivalList({ festivals }: { festivals: FestivalCardViewModel[] }) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

---

### [FAQ]

Q. Response Mapping이 뭐야?
A. API Response를 UI Component가 사용하기 쉬운 ViewModel 또는 Props 구조로 변환하는 작업이다.

Q. API Response를 그대로 Component에 넘기면 왜 문제야?
A. 서버 응답 필드 변경이 UI Component에 직접 영향을 주고 재사용성이 떨어질 수 있다.

Q. Response Mapping은 어디서 해?
A. API Hook, mapper 함수, Container에서 처리할 수 있다.

Q. ViewModel은 왜 만들어?
A. 화면 표시 목적에 맞는 안정적인 데이터 구조를 만들어 UI와 서버 응답의 결합도를 낮추기 위해서다.

---

## 4.2 Null and Optional Response Handling

### [개념]

Null and Optional Response Handling은 API Response의 null, undefined, optional field를 Component에서 안전하게 처리하는 기준이다.

서버 응답은 누락되거나 null일 수 있으므로 UI Component는 안정적인 fallback을 가져야 한다.

---

### [핵심]

처리 대상:

- imageUrl null
- description null
- averageRating null
- date null
- optional nested object
- empty list
- missing label
- unknown status
- nullable user profile

처리 원칙:

- null 가능성을 TypeScript Type에 반영한다.
- mapper에서 fallback을 만들 수 있다.
- UI Component에서 조건부 렌더링을 명확히 한다.
- 이미지 alt를 안전하게 제공한다.
- 빈 문자열과 null 의미를 구분한다.
- Optional Chaining 남용으로 오류를 숨기지 않는다.
- Empty State와 Error State를 구분한다.

---

### [실무]

nullable image 처리:

```tsx
type FestivalCardProps = {
  title: string;
  imageUrl: string | null;
};

function FestivalCard({ title, imageUrl }: FestivalCardProps) {
  return (
    <article>
      {imageUrl ? (
        <img src={imageUrl} alt={title} />
      ) : (
        <div aria-label={`${title} 이미지 없음`} />
      )}
      <h2>{title}</h2>
    </article>
  );
}
```

mapper fallback:

```ts
function mapFestival(response: FestivalResponse): FestivalCardViewModel {
  return {
    festivalId: response.id,
    title: response.name || "제목 없음",
    imageUrl: response.img_url,
    regionName: response.sigungu || "지역 정보 없음",
    periodText: formatPeriod(response.start_date, response.end_date),
  };
}
```

주의:

```tsx
<p>{festival.detail.info.name}</p>
```

문제:

```text
detail 또는 info가 null이면 runtime error 발생 가능
```

개선:

```tsx
<p>{festival.detail?.info?.name ?? "상세 정보 없음"}</p>
```

---

### [FAQ]

Q. API Response의 null 값은 어디서 처리해?
A. mapper, API Hook, UI Component에서 처리할 수 있다. 표시용 fallback은 mapper에서 정리하면 UI가 단순해진다.

Q. imageUrl이 null이면 어떻게 해?
A. 이미지를 렌더링하지 않거나 placeholder를 제공하고 alt 또는 aria-label을 안전하게 처리한다.

Q. Optional Chaining을 많이 쓰면 괜찮아?
A. 남용하면 데이터 문제를 숨길 수 있다. fallback과 Type 정의를 함께 명확히 해야 한다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청은 성공했지만 데이터가 없는 상태이고, Error State는 요청 자체가 실패한 상태다.

---

# 5. TypeScript Component Design

## 5.1 TypeScript Props Type Design

### [개념]

TypeScript Props Type Design은 Component가 외부에서 받는 데이터, Callback Props, children, variant, event handler의 타입을 명확히 정의하는 작업이다.

Props Type은 Component Contract를 코드 수준에서 표현한다.

---

### [핵심]

Props Type 포함 대상:

- Required Props
- Optional Props
- Callback Props
- Children Type
- ReactNode
- Event Handler Type
- Variant Union
- Object Props Type
- Generic Props
- Nullable Field
- readonly concept

Props Type 원칙:

- Component 전용 Props Type은 같은 파일에 둔다.
- 공유 타입은 별도 types 파일로 분리한다.
- Props Type 이름은 ComponentNameProps로 작성한다.
- Callback parameter와 return type을 명확히 한다.
- children은 일반적으로 ReactNode를 사용한다.
- 불필요한 React.FC 강제는 피한다.
- any 사용을 피한다.
- Optional Props에는 기본값을 고려한다.
- nullable field를 명확히 표시한다.

---

### [실무]

Props Type 예:

```tsx
import type { ReactNode } from "react";

type ModalProps = {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
};

function Modal({ isOpen, title, onClose, children }: ModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <h2 id="modal-title">{title}</h2>
      <button type="button" onClick={onClose}>
        닫기
      </button>
      {children}
    </section>
  );
}
```

Callback Props Type 예:

```tsx
type ReviewFormValues = {
  rating: number;
  content: string;
};

type ReviewFormProps = {
  initialValues?: Partial<ReviewFormValues>;
  onSubmit: (values: ReviewFormValues) => void;
  onCancel?: () => void;
};
```

Variant Type 예:

```tsx
type AlertVariant = "success" | "warning" | "error";

type AlertProps = {
  variant: AlertVariant;
  message: string;
};
```

---

### [FAQ]

Q. TypeScript Props Type은 왜 중요해?
A. Component가 외부에서 요구하는 데이터 구조를 명확히 해 잘못된 사용을 줄인다.

Q. Props Type 이름은 어떻게 지어?
A. Component 이름 뒤에 Props를 붙인다. 예를 들어 ModalProps, FestivalCardProps처럼 작성한다.

Q. children 타입은 뭐로 써?
A. 일반적으로 ReactNode를 사용한다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용할 수 있지만 불필요하게 강제하지 않는다.

---

## 5.2 Required, Optional, Nullable Props

### [개념]

Required, Optional, Nullable Props는 Component Props에서 반드시 필요한 값, 생략 가능한 값, null이 가능한 값을 구분하는 타입 설계 기준이다.

이 구분이 명확해야 Component Contract가 안정적이다.

---

### [핵심]

Required Props:

- Component 동작에 반드시 필요한 값
- 없으면 정상 렌더링이 어려운 값
- 예: title, value, onSubmit

Optional Props:

- 없어도 기본값으로 처리 가능한 값
- 예: description, disabled, variant, className

Nullable Props:

- 값이 없을 수 있음을 명시적으로 표현
- API Response나 이미지 URL에 자주 사용
- 예: imageUrl: string | null

원칙:

- optional과 nullable을 혼동하지 않는다.
- Optional Props에는 기본값을 고려한다.
- nullable 값은 조건부 렌더링한다.
- Required Props를 불필요하게 optional로 만들지 않는다.
- null 가능성을 Type에 반영한다.

---

### [실무]

예:

```tsx
type UserProfileCardProps = {
  username: string;
  imageUrl: string | null;
  bio?: string;
  disabled?: boolean;
};

function UserProfileCard({
  username,
  imageUrl,
  bio,
  disabled = false,
}: UserProfileCardProps) {
  return (
    <article aria-disabled={disabled}>
      {imageUrl && <img src={imageUrl} alt={`${username} 프로필 이미지`} />}
      <h2>{username}</h2>
      {bio && <p>{bio}</p>}
    </article>
  );
}
```

구분:

```text
username
→ Required

imageUrl
→ Nullable

bio
→ Optional

disabled
→ Optional with Default Value
```

주의:

```tsx
type Props = {
  title?: string;
};
```

문제:

```text
title이 실제로 필수라면 optional로 두면 Component 사용 오류를 TypeScript가 막지 못한다.
```

---

### [FAQ]

Q. Optional Props와 Nullable Props 차이는 뭐야?
A. Optional Props는 생략 가능하고 Nullable Props는 값이 명시적으로 null일 수 있다는 의미다.

Q. Required Props를 optional로 만들면 왜 문제야?
A. Component가 정상 동작하는 데 필요한 값이 없어도 TypeScript가 오류를 잡지 못한다.

Q. imageUrl은 optional이 좋아 nullable이 좋아?
A. API에서 null로 내려올 수 있다면 `string | null`로 명확히 표현하는 것이 좋다.

Q. Optional Props에는 기본값을 줘야 해?
A. 가능하면 기본값을 제공해 Component 내부 조건 분기를 줄이는 것이 좋다.

---

# 6. TypeScript Event Handler Type

## 6.1 Event Handler Type Rules

### [개념]

Event Handler Type은 React DOM Event를 처리하는 함수의 TypeScript 타입을 명확히 지정하는 규칙이다.

Form submit, input change, button click 같은 이벤트는 적절한 React Event Type을 사용해야 한다.

---

### [핵심]

자주 쓰는 Event Type:

- React.MouseEvent
- React.ChangeEvent
- React.FormEvent
- React.KeyboardEvent
- React.FocusEvent

대상 Element Type:

- HTMLButtonElement
- HTMLInputElement
- HTMLTextAreaElement
- HTMLFormElement
- HTMLSelectElement

원칙:

- DOM Event를 직접 처리하는 Handler는 React Event Type을 명시한다.
- Callback Props는 가능하면 도메인 값으로 추상화할 수 있다.
- 범용 Input은 event를 받을 수 있다.
- 도메인 Form은 values를 전달하는 것이 더 명확할 수 있다.
- any event는 피한다.

---

### [실무]

Form Event 예:

```tsx
function ReviewForm({ onSubmit }: ReviewFormProps) {
  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSubmit(values);
  }

  return <form onSubmit={handleSubmit}>...</form>;
}
```

Input Change Event 예:

```tsx
function TextInput() {
  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    setValue(event.target.value);
  }

  return <input value={value} onChange={handleChange} />;
}
```

Callback Props로 value만 전달:

```tsx
type TextInputProps = {
  value: string;
  onValueChange: (value: string) => void;
};

function TextInput({ value, onValueChange }: TextInputProps) {
  return (
    <input
      value={value}
      onChange={(event) => onValueChange(event.target.value)}
    />
  );
}
```

---

### [FAQ]

Q. input onChange 타입은 뭐야?
A. 일반적으로 `React.ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. 일반적으로 `React.FormEvent<HTMLFormElement>`를 사용한다.

Q. Callback Props에도 event 타입을 그대로 넘겨야 해?
A. 범용 Component는 가능하지만 도메인 Component는 value나 values로 추상화하는 것이 더 명확할 수 있다.

Q. event 타입을 any로 써도 돼?
A. 권장하지 않는다. event target 타입 안정성이 사라진다.

---

## 6.2 Callback Props Type Rules

### [개념]

Callback Props Type은 부모가 자식 Component에 전달하는 이벤트 함수의 parameter와 return type을 명확히 정의하는 규칙이다.

Callback Props Type은 Component 이벤트 계약이다.

---

### [핵심]

Callback Props Type 원칙:

- 이름은 `on` prefix를 사용한다.
- parameter는 최소한으로 전달한다.
- return type은 일반적으로 void다.
- ID만 필요하면 ID만 전달한다.
- Form submit은 values 객체를 전달한다.
- DOM Event를 노출할지 값으로 추상화할지 결정한다.
- Promise 반환이 필요하면 명확히 표시한다.
- optional callback은 호출 전 존재 여부를 확인한다.

---

### [실무]

ID Callback:

```tsx
type FestivalCardProps = {
  festivalId: number;
  title: string;
  onSelect: (festivalId: number) => void;
};
```

Form Submit Callback:

```tsx
type LoginFormValues = {
  email: string;
  password: string;
};

type LoginFormProps = {
  onSubmit: (values: LoginFormValues) => void;
};
```

Async Callback:

```tsx
type ReviewFormProps = {
  onSubmit: (values: ReviewFormValues) => Promise<void>;
};
```

Optional Callback:

```tsx
type ModalProps = {
  onClose?: () => void;
};

function Modal({ onClose }: ModalProps) {
  return (
    <button type="button" onClick={() => onClose?.()}>
      닫기
    </button>
  );
}
```

---

### [FAQ]

Q. Callback Props return type은 보통 뭐야?
A. 일반적으로 void다. 비동기 제출이 필요하면 Promise<void>로 명확히 표현할 수 있다.

Q. onSelect에는 객체 전체를 넘겨야 해?
A. 부모가 ID만 필요하면 ID만 넘기는 것이 좋다. 객체 전체가 필요하면 타입을 명확히 한다.

Q. optional callback은 어떻게 호출해?
A. `onClose?.()`처럼 optional chaining으로 안전하게 호출할 수 있다.

Q. Callback Props Type이 중요한 이유는 뭐야?
A. 자식이 어떤 이벤트와 값을 부모에게 전달하는지 명확히 하는 계약이기 때문이다.

---

# 7. Generic Component Basics

## 7.1 Generic Component Definition

### [개념]

Generic Component는 여러 데이터 타입에 재사용 가능한 Component를 만들 때 사용하는 TypeScript React 패턴이다.

Generic Component는 List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

---

### [핵심]

Generic Component 적합 대상:

- List
- Select
- Table
- Combobox
- Option List
- Data Renderer
- Generic Card List

Generic Component 원칙:

- 실제 반복 패턴이 있을 때 사용한다.
- renderItem, getKey 같은 명확한 Props를 제공한다.
- Generic이 사용성을 해치면 명시적 Component가 낫다.
- 너무 추상적인 Generic Component는 피한다.
- Foundation 단계에서는 단순 Generic만 사용한다.
- 도메인별 차이가 크면 도메인 Component를 유지한다.

---

### [실무]

Generic List 예:

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, getKey, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={getKey(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

사용:

```tsx
<List
  items={festivals}
  getKey={(festival) => festival.festivalId}
  renderItem={(festival) => <FestivalCard festival={festival} />}
/>
```

도입 보류:

```text
FestivalList와 ReviewList의 UI 구조가 많이 다르다
→ Generic List보다 명시적 List 유지

Generic Props가 너무 많다
→ 과도한 추상화 의심

render 함수가 복잡하다
→ 도메인 Component가 더 명확할 수 있음
```

---

### [FAQ]

Q. Generic Component는 언제 써?
A. List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Generic Component를 많이 만들면 좋아?
A. 아니다. 과도한 Generic은 사용성과 가독성을 떨어뜨릴 수 있다.

Q. renderItem Props는 뭐야?
A. Generic Component가 각 item을 어떻게 렌더링할지 외부에서 전달받는 함수 Props다.

Q. Generic이 어렵다면 어떻게 해?
A. 명시적인 도메인 Component를 유지하는 것이 더 나을 수 있다.

---

## 7.2 Generic Component Caution

### [개념]

Generic Component Caution은 Generic Component를 과도하게 추상화해 사용성이 떨어지는 문제를 방지하는 규칙이다.

Generic은 타입 재사용성을 높일 수 있지만, Component API가 복잡해지면 오히려 유지보수성이 낮아진다.

---

### [핵심]

주의 사항:

- Generic Props가 너무 많다.
- renderItem, getKey, getLabel, getValue가 과도하다.
- 도메인마다 UI 구조가 다르다.
- Generic Component 사용 코드가 더 길다.
- 타입 추론이 어렵다.
- 오류 메시지가 복잡하다.
- 실제 재사용 빈도가 낮다.
- 명시적 Component가 더 읽기 쉽다.

---

### [실무]

과도한 Generic 예:

```tsx
type DataRendererProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  getTitle: (item: T) => string;
  getDescription: (item: T) => string;
  getImage: (item: T) => string | null;
  getStatus: (item: T) => string;
  onSelect: (item: T) => void;
  renderAction?: (item: T) => React.ReactNode;
};
```

문제:

```text
Props가 많다.
도메인별 표시 차이를 Generic Props로 모두 처리하려 한다.
사용법이 복잡하다.
```

대안:

```text
FestivalCardList
ReviewList
NotificationList

각 도메인 Component를 명시적으로 유지하고,
공통 UI는 Card, Button, Badge로 조합한다.
```

판단 기준:

```text
Generic이 중복을 줄이는가?
Generic 사용법이 명확한가?
명시적 Component보다 읽기 쉬운가?
실제 반복 패턴이 안정적인가?
```

---

### [FAQ]

Q. Generic Component의 위험은 뭐야?
A. Props가 많아지고 타입 추론이 어려워져 사용성과 가독성이 떨어질 수 있다.

Q. Generic보다 명시적 Component가 나은 경우는 언제야?
A. 도메인별 UI 구조가 다르거나 Generic Props가 너무 많아질 때 명시적 Component가 더 낫다.

Q. Generic List는 항상 좋은 선택이야?
A. 아니다. 단순한 반복 구조가 여러 곳에서 안정적으로 반복될 때만 적합하다.

Q. Generic Component 도입 전 확인할 것은 뭐야?
A. 실제 반복 패턴, 사용법 단순성, 타입 추론 안정성, 명시적 Component 대비 장점을 확인해야 한다.

---

# 8. File and Type Structure

## 8.1 Component File Structure

### [개념]

Component File Structure는 Component, Hook, API Function, Type, Mapper, Style을 어떻게 배치할지 정하는 구조다.

React Component Design에서는 Component Responsibility와 Feature Boundary에 맞게 파일을 배치해야 한다.

---

### [핵심]

구조 기준:

- pages
- features
- components
- hooks
- api
- types
- mappers
- styles
- utils

역할:

- pages: 라우트 화면 단위
- features: 도메인 기능 단위
- components: 공통 UI Component
- hooks: 재사용 로직
- api: 서버 요청 함수
- types: 공유 타입
- mappers: Response Mapping
- styles: 스타일 파일
- utils: 순수 유틸 함수

---

### [실무]

기본 구조:

```text
src
├ pages
│  └ FestivalSearchPage
│     └ FestivalSearchPage.tsx
├ features
│  └ festival
│     ├ components
│     │  ├ FestivalSearchForm.tsx
│     │  ├ FestivalList.tsx
│     │  └ FestivalCard.tsx
│     ├ hooks
│     │  └ useFestivalSearch.ts
│     ├ api
│     │  └ festivalApi.ts
│     ├ mappers
│     │  └ festivalMapper.ts
│     └ types
│        └ festivalTypes.ts
├ components
│  ├ Button
│  │  └ Button.tsx
│  ├ Modal
│  │  └ Modal.tsx
│  └ EmptyState
│     └ EmptyState.tsx
└ utils
```

권장:

```text
Feature 관련 Component / Hook / API / Type은 feature 폴더에 모은다.
도메인과 무관한 UI Component는 components에 둔다.
공유 타입은 types 파일로 분리한다.
작은 프로젝트에서는 구조를 단순화한다.
```

주의:

```text
작은 프로젝트에 과도한 폴더 구조 적용
→ 오히려 탐색 비용 증가

모든 Component를 components에 몰아넣음
→ Feature Boundary 불명확

API 함수가 Component 파일 안에 있음
→ API Logic Separation 약화
```

---

### [FAQ]

Q. Component File Structure는 어떻게 잡아?
A. pages, features, components, hooks, api, types 기준으로 역할을 나눌 수 있다.

Q. Feature 기반 폴더 구조는 언제 좋아?
A. 도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. 작은 프로젝트도 features 구조를 써야 해?
A. 필수는 아니다. 작은 프로젝트는 pages, components, api, hooks 정도로 단순하게 시작해도 된다.

Q. 공통 UI Component는 어디에 둬?
A. 도메인과 무관한 Button, Modal, EmptyState 같은 Component는 components에 둔다.

---

## 8.2 Type File Structure

### [개념]

Type File Structure는 TypeScript 타입을 Component 파일 내부에 둘지, feature types 파일에 분리할지 결정하는 기준이다.

타입 위치는 사용 범위와 재사용성을 기준으로 정한다.

---

### [핵심]

타입 위치 기준:

- Component 전용 Props Type은 Component 파일 내부
- 여러 Component가 공유하는 도메인 타입은 feature types 파일
- API Response Type은 api 또는 feature types 파일
- ViewModel Type은 mapper 또는 feature types 파일
- 전역 공통 타입은 shared types 파일
- 너무 빨리 모든 타입을 중앙화하지 않는다.

---

### [실무]

Component 내부 Type:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary";
  children: React.ReactNode;
};

function Button({ variant = "primary", children }: ButtonProps) {
  return <button className={`button-${variant}`}>{children}</button>;
}
```

Feature 공유 Type:

```ts
export type FestivalSummary = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
};

export type FestivalSearchParams = {
  keyword: string;
  regionCode?: string;
  page: number;
  size: number;
};
```

API Response Type:

```ts
export type FestivalSearchResponse = {
  content: FestivalResponse[];
  page: number;
  totalPages: number;
};
```

판단:

```text
한 Component에서만 사용
→ Component 파일 내부

Feature 여러 파일에서 사용
→ feature/types

앱 전체에서 사용
→ shared/types
```

---

### [FAQ]

Q. Props Type은 어디에 둬?
A. Component 전용이면 같은 파일에 두고 여러 곳에서 공유하면 types 파일로 분리한다.

Q. API Response Type은 어디에 둬?
A. api 파일 근처 또는 feature types 파일에 둘 수 있다.

Q. 모든 타입을 types 폴더에 모으면 좋아?
A. 항상 좋지는 않다. 사용 위치와 가까운 곳에 두는 것이 유지보수에 더 좋을 수 있다.

Q. ViewModel Type은 어디에 둬?
A. mapper와 함께 두거나 feature types 파일에 둘 수 있다.

---

# 9. Anti Patterns

## 9.1 Over-Abstraction Reusable Component

### [개념]

Over-Abstraction Reusable Component는 실제 필요보다 과도하게 공통화해서 Component 사용성이 떨어지는 문제다.

Reusable Component는 반복과 패턴이 확인된 후 추출해야 한다.

---

### [핵심]

문제:

- Props가 너무 많다.
- variant가 너무 많다.
- 도메인별 차이를 억지로 하나에 통합한다.
- Generic Component가 과도하다.
- 실제 재사용 빈도가 낮다.
- Component 사용법이 어렵다.
- 작은 UI 수정도 공통 Component 변경이 필요하다.

원인:

- 미래 재사용성 과도 예측
- Design System 없이 공통화 남발
- Component 책임 과다
- 도메인 차이를 무시한 통합
- slot / render props / generic 남용

해결:

- 실제 반복 확인 후 추출
- 단순 Component 유지
- 도메인별 Component 분리 허용
- variant 수 줄이기
- 명시적 Component 검토
- Props Contract 재설계

---

### [실무]

나쁜 예:

```text
UniversalCard
- festival mode
- review mode
- user mode
- notification mode
- donation mode
- ranking mode
```

문제:

```text
도메인별 요구사항이 모두 UniversalCard에 들어간다.
Props가 계속 증가한다.
하나의 수정이 여러 도메인에 영향을 준다.
```

개선:

```text
Card
- 공통 wrapper

FestivalCard
- 축제 도메인 표시

ReviewCard
- 리뷰 도메인 표시

NotificationItem
- 알림 도메인 표시
```

판단 Flow:

```text
Is it reused now?
→ Does abstraction reduce duplication?
→ Is Props API understandable?
→ Are variants limited?
→ Is explicit component simpler?
```

---

### [FAQ]

Q. Over-Abstraction Reusable Component가 뭐야?
A. 실제 필요보다 과도하게 공통화해 Props가 복잡하고 사용성이 떨어지는 Component다.

Q. 재사용 가능하게 만들수록 좋은 거 아니야?
A. 아니다. 실제 사용성이 떨어지는 추상화는 유지보수를 어렵게 만든다.

Q. 중복 코드가 조금 있으면 바로 공통화해야 해?
A. 아니다. 반복 패턴이 명확해지고 변경 방향이 보일 때 공통화하는 것이 안전하다.

Q. UniversalCard 같은 Component는 왜 위험해?
A. 여러 도메인 요구사항이 한 Component에 모여 Props가 계속 증가하고 책임이 불명확해지기 때문이다.

---

## 9.2 API Logic in UI Component Problem

### [개념]

API Logic in UI Component Problem은 Button, Card, Modal, EmptyState 같은 UI Component 내부에서 서버 요청을 직접 수행하는 문제다.

UI Component는 서버 구조와 비즈니스 흐름을 몰라야 재사용 가능하다.

---

### [핵심]

문제:

- UI Component가 API URL을 안다.
- UI Component가 서버 Response 구조를 안다.
- UI Component가 인증 흐름에 의존한다.
- UI Component가 특정 도메인 동작을 강제한다.
- 테스트가 어려워진다.
- 재사용성이 떨어진다.
- Component Responsibility가 깨진다.

해결:

- API 요청은 api 파일로 분리한다.
- API 상태는 API Hook으로 분리한다.
- UI Component는 Props와 Callback Props만 사용한다.
- Page 또는 Feature에서 API Hook을 호출한다.
- UI Component는 이벤트만 알린다.

---

### [실무]

나쁜 예:

```tsx
function Button() {
  async function handleClick() {
    await fetch("/api/festivals/like", { method: "POST" });
  }

  return <button onClick={handleClick}>좋아요</button>;
}
```

문제:

```text
공통 Button이 축제 좋아요 API를 알고 있다.
Button이 도메인 기능에 결합된다.
```

개선:

```tsx
type ButtonProps = {
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({ children, onClick }: ButtonProps) {
  return (
    <button type="button" onClick={onClick}>
      {children}
    </button>
  );
}
```

Feature에서 처리:

```tsx
function FestivalLikeButton({ festivalId }: FestivalLikeButtonProps) {
  const { likeFestival } = useFestivalLike();

  return <Button onClick={() => likeFestival(festivalId)}>좋아요</Button>;
}
```

---

### [FAQ]

Q. UI Component에서 API 호출하면 왜 문제야?
A. UI Component가 서버 구조와 도메인 동작에 결합되어 재사용성과 테스트 가능성이 떨어진다.

Q. 좋아요 버튼은 어디에 만들어야 해?
A. 공통 Button이 아니라 FestivalLikeButton 같은 Feature Component에서 API Hook과 Button을 조합하는 것이 좋다.

Q. API Logic은 어디에 둬야 해?
A. api 함수, API Custom Hook, Page 또는 Feature 계층에 둔다.

Q. UI Component는 API 대신 무엇을 받아야 해?
A. 값은 Props로 받고 이벤트는 Callback Props로 받아야 한다.

---

## 9.3 TypeScript Any Props Problem

### [개념]

TypeScript Any Props Problem은 Props Type을 `any`로 작성해 Component Contract가 무너지는 문제다.

`any`를 사용하면 TypeScript가 Props 구조 오류를 검출하지 못한다.

---

### [핵심]

문제:

- Props Contract가 사라진다.
- 잘못된 Props 전달을 막지 못한다.
- Callback parameter 타입이 불명확해진다.
- API Response 구조 변경을 감지하기 어렵다.
- Component 사용법이 문서화되지 않는다.
- refactoring 안정성이 떨어진다.

해결:

- 명확한 Props Type 정의
- unknown 사용 후 narrowing 검토
- API Response Type 정의
- ViewModel Type 정의
- Callback parameter 타입 명시
- Generic이 필요한 경우 Generic Props 사용
- nullable / optional 구분

---

### [실무]

나쁜 예:

```tsx
function FestivalCard({ data, onClick }: any) {
  return (
    <article onClick={() => onClick(data.id)}>
      <h2>{data.name}</h2>
    </article>
  );
}
```

문제:

```text
data 구조를 알 수 없다.
onClick parameter를 알 수 없다.
data.id와 data.name 존재 여부를 TypeScript가 보장하지 않는다.
```

개선:

```tsx
type FestivalCardProps = {
  festival: {
    festivalId: number;
    title: string;
    imageUrl: string | null;
  };
  onSelect: (festivalId: number) => void;
};

function FestivalCard({ festival, onSelect }: FestivalCardProps) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <button type="button" onClick={() => onSelect(festival.festivalId)}>
        상세 보기
      </button>
    </article>
  );
}
```

---

### [FAQ]

Q. Props Type에 any를 쓰면 왜 문제야?
A. Component Contract가 사라져 잘못된 Props 전달을 TypeScript가 막을 수 없다.

Q. any 대신 뭘 써야 해?
A. 명확한 Props Type, API Response Type, ViewModel Type을 정의한다. 불확실한 값은 unknown 후 narrowing을 검토한다.

Q. data: any는 왜 안 좋아?
A. data 구조를 알 수 없어 Component 사용법과 타입 안정성이 모두 떨어진다.

Q. TypeScript를 쓰면 Props 문서가 필요 없어?
A. 아니다. TypeScript는 Contract를 코드로 표현하지만 FAQ, 예제, Retrieval Query도 RAG 문서에는 필요하다.

---

# 10. Review Checklist

## 10.1 Reusable API TypeScript Checklist

### [개념]

Reusable API TypeScript Checklist는 Reusable Component, API Logic Separation, TypeScript Component 설계가 적절한지 검수하기 위한 기준이다.

Frontend Agent와 Review Agent는 Component 코드 생성 전후에 재사용성, API 책임 위치, Props Type 안정성을 함께 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Reusable Component가 도메인 로직에 의존하지 않는가?
- [ ] Reusable Component가 API 호출을 하지 않는가?
- [ ] Reusable Component Props Contract가 명확한가?
- [ ] 실제 반복이 확인된 Component만 공통화했는가?
- [ ] variant가 union type으로 제한되는가?
- [ ] boolean props 여러 개로 불가능한 상태를 만들지 않는가?
- [ ] className 확장 필요성이 검토되었는가?
- [ ] Component 자체 스타일과 부모 layout 스타일이 구분되는가?
- [ ] API 요청 함수가 api 파일로 분리되었는가?
- [ ] API Function이 React State setter에 의존하지 않는가?
- [ ] API Hook이 data/loading/error/refetch를 명확히 관리하는가?
- [ ] UI Component가 API URL을 직접 알지 않는가?
- [ ] Response Mapping으로 UI와 API Response 결합도를 낮췄는가?
- [ ] null / optional response 처리가 명확한가?
- [ ] Props Type이 Component Contract 역할을 하는가?
- [ ] Required / Optional / Nullable Props가 구분되는가?
- [ ] Callback Props Type이 명확한가?
- [ ] Event Handler Type이 any가 아닌가?
- [ ] Generic Component가 과도하게 추상화되지 않았는가?
- [ ] Type 파일 위치가 사용 범위에 맞는가?
```

---

### [실무]

Review Flow:

```text
Component Review
→ Reusability Check
→ Domain Dependency Check
→ Variant Check
→ Style Responsibility Check
→ API Logic Location Check
→ Response Mapping Check
→ TypeScript Props Check
→ Generic Abstraction Check
→ Anti Pattern Check
```

치명적 문제:

```text
- Reusable UI Component가 API 호출
- 공통 Component가 특정 도메인 Response에 강하게 결합
- Props Type이 any
- API Function이 React State setter를 직접 사용
- API Response를 UI Component에 그대로 강제
- nullable field를 Type에 반영하지 않음
- variant 대신 boolean 여러 개로 불가능한 상태 생성
- Generic Component가 과도하게 복잡함
```

---

### [FAQ]

Q. Reusable Component 검수에서 가장 중요한 것은?
A. 도메인 의존성, API 호출 여부, Props Contract, 실제 반복 여부를 확인하는 것이다.

Q. API Logic Separation 검수에서 가장 중요한 것은?
A. API 요청 함수와 API 상태 로직이 Component UI 표시 책임과 분리되어 있는지 확인하는 것이다.

Q. TypeScript Component 검수에서 가장 중요한 것은?
A. Props Type이 any 없이 Required, Optional, Nullable, Callback Type을 명확히 표현하는지 확인하는 것이다.

Q. 치명적인 문제는 뭐야?
A. UI Component가 API를 호출하거나 Props Type이 any이거나 API Response를 UI에 그대로 강제하는 것이다.

---

# 11. Agent Output Rules

## 11.1 Frontend Agent Output Rules

### [개념]

Frontend Agent는 Component 코드를 생성하기 전에 Reusable Component, API Logic Separation, TypeScript Props Type을 명확히 설계해야 한다.

Agent Output은 Component 재사용성, API 책임 위치, Response Mapping, Props Type, Anti Pattern Review를 포함해야 한다.

---

### [핵심]

Frontend Agent 출력 항목:

- Reusable Component 후보
- Feature Component 후보
- API Function 목록
- API Hook 목록
- Response Mapping 여부
- ViewModel Type
- Props Type
- Required Props
- Optional Props
- Nullable Props
- Callback Props Type
- Variant Type
- File Structure
- Anti Pattern Review

---

### [실무]

출력 예:

```text
Reusable Components:
Button
- responsibility: 공통 버튼 표시
- props: type, variant, size, disabled, children, onClick
- API 호출 없음

EmptyState
- responsibility: 빈 상태 표시
- props: title, description, action

Feature Components:
FestivalCard
- responsibility: 축제 단일 항목 표시
- props: festival, onSelect
- domain dependency: FestivalSummary

API Functions:
searchFestivals(request)
- responsibility: 축제 검색 API 요청
- location: features/festival/api/festivalApi.ts

API Hooks:
useFestivalSearch(params)
- responsibility: 검색 API 상태 관리
- return: festivals, loading, error, refetch

Mapping:
FestivalResponse → FestivalCardViewModel

Types:
FestivalResponse
FestivalCardViewModel
FestivalCardProps
FestivalSearchParams
```

Anti Pattern Review:

```text
- Reusable UI Component API 호출 없음
- Props Type any 없음
- Response Mapping 적용
- nullable imageUrl 처리
- variant union type 적용
- Generic 과도 추상화 없음
```

---

### [FAQ]

Q. Frontend Agent는 Reusable Component를 언제 제안해야 해?
A. 여러 화면에서 반복되고 도메인 의존성이 낮은 UI가 확인될 때 제안해야 한다.

Q. Agent Output에 API Function도 포함해야 해?
A. API 연동 Component라면 포함하는 것이 좋다. API 책임 위치가 명확해야 코드 생성 품질이 높아진다.

Q. ViewModel Type은 언제 출력해야 해?
A. API Response와 UI 표시 구조가 다르거나 null 처리와 표시 문자열 변환이 필요할 때 출력한다.

Q. Review Agent는 이 출력에서 무엇을 검토해야 해?
A. 재사용성 판단, API Logic 위치, Props Type 안정성, Response Mapping, Anti Pattern 여부를 검토해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Reusable Component가 뭐야?
A. 여러 화면과 Feature에서 반복 사용할 수 있도록 도메인 의존성을 줄이고 Props 기반으로 설계한 Component다.

Q. Reusable Component는 언제 만들어?
A. 여러 화면에서 같은 UI가 반복되고 도메인 로직 없이 Props로 제어할 수 있을 때 만든다.

Q. 처음부터 공통 Component를 많이 만들면 좋아?
A. 아니다. 실제 반복과 필요가 확인된 후 추출하는 것이 안전하다.

Q. Reusable Component는 API 호출을 해도 돼?
A. 권장하지 않는다. Reusable Component는 표시와 상호작용만 담당하고 API Logic은 Page, Feature, Hook, API 계층에서 처리한다.

Q. Reusable Component 추출 기준은 뭐야?
A. 반복 사용, 도메인 독립성, Props 안정성, 접근성, 스타일 확장성을 기준으로 판단한다.

Q. FestivalCard는 Reusable Component야?
A. 축제 도메인 데이터에 의존하면 Feature Component 또는 Domain Component에 가깝다.

Q. Button은 Reusable Component야?
A. 일반적으로 그렇다. 도메인과 무관하고 여러 화면에서 반복 사용되기 때문이다.

Q. Variant Props가 뭐야?
A. Component의 상태나 스타일 변형을 제한된 문자열 값으로 표현하는 Props다.

Q. variant는 왜 써?
A. Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. boolean props 대신 variant를 쓰는 기준은 뭐야?
A. 여러 상태 중 하나만 선택되어야 하면 boolean 여러 개보다 variant가 적합하다.

Q. Component margin은 내부에서 줘도 돼?
A. 상황에 따라 다르지만 Reusable UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?
A. 재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

Q. API Logic Separation이 뭐야?
A. Component 내부의 서버 요청 로직을 api 함수, Custom Hook, Data Fetching 계층으로 분리하는 설계 기준이다.

Q. API 호출을 Component 안에 쓰면 안 돼?
A. 간단한 화면에서는 가능하지만 재사용되거나 길어지면 api 함수나 Custom Hook으로 분리하는 것이 좋다.

Q. UI Component에서 fetch를 하면 왜 안 좋아?
A. UI Component가 서버 구조에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

Q. API URL은 어디에 두는 게 좋아?
A. 일반적으로 api 파일에 두고 Component는 API 함수나 API Hook을 통해 사용한다.

Q. API Function은 뭐야?
A. 서버 요청 자체를 담당하는 함수다.

Q. API Function에서 useState를 써도 돼?
A. 안 된다. API Function은 React Hook을 사용하지 않고 요청과 응답 처리만 담당해야 한다.

Q. API Function은 State setter를 받아도 돼?
A. 권장하지 않는다. API Function은 State 변경이 아니라 서버 요청 결과 반환에 집중해야 한다.

Q. Response Mapping이 뭐야?
A. API Response를 UI Component가 사용하기 쉬운 ViewModel 또는 Props 구조로 변환하는 작업이다.

Q. API Response를 그대로 Component에 넘기면 왜 문제야?
A. 서버 응답 필드 변경이 UI Component에 직접 영향을 주고 재사용성이 떨어질 수 있다.

Q. Response Mapping은 어디서 해?
A. API Hook, mapper 함수, Container에서 처리할 수 있다.

Q. ViewModel은 왜 만들어?
A. 화면 표시 목적에 맞는 안정적인 데이터 구조를 만들어 UI와 서버 응답의 결합도를 낮추기 위해서다.

Q. API Response의 null 값은 어디서 처리해?
A. mapper, API Hook, UI Component에서 처리할 수 있다. 표시용 fallback은 mapper에서 정리하면 UI가 단순해진다.

Q. imageUrl이 null이면 어떻게 해?
A. 이미지를 렌더링하지 않거나 placeholder를 제공하고 alt 또는 aria-label을 안전하게 처리한다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청은 성공했지만 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. TypeScript Props Type은 왜 중요해?
A. Component가 외부에서 요구하는 데이터 구조를 명확히 해 잘못된 사용을 줄인다.

Q. Props Type 이름은 어떻게 지어?
A. Component 이름 뒤에 Props를 붙인다. 예를 들어 ModalProps, FestivalCardProps처럼 작성한다.

Q. children 타입은 뭐로 써?
A. 일반적으로 ReactNode를 사용한다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용할 수 있지만 불필요하게 강제하지 않는다.

Q. Optional Props와 Nullable Props 차이는 뭐야?
A. Optional Props는 생략 가능하고 Nullable Props는 값이 명시적으로 null일 수 있다는 의미다.

Q. Required Props를 optional로 만들면 왜 문제야?
A. Component가 정상 동작하는 데 필요한 값이 없어도 TypeScript가 오류를 잡지 못한다.

Q. imageUrl은 optional이 좋아 nullable이 좋아?
A. API에서 null로 내려올 수 있다면 `string | null`로 명확히 표현하는 것이 좋다.

Q. input onChange 타입은 뭐야?
A. 일반적으로 `React.ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. 일반적으로 `React.FormEvent<HTMLFormElement>`를 사용한다.

Q. Callback Props return type은 보통 뭐야?
A. 일반적으로 void다. 비동기 제출이 필요하면 Promise<void>로 명확히 표현할 수 있다.

Q. Generic Component는 언제 써?
A. List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Generic Component를 많이 만들면 좋아?
A. 아니다. 과도한 Generic은 사용성과 가독성을 떨어뜨릴 수 있다.

Q. Generic보다 명시적 Component가 나은 경우는 언제야?
A. 도메인별 UI 구조가 다르거나 Generic Props가 너무 많아질 때 명시적 Component가 더 낫다.

Q. Component File Structure는 어떻게 잡아?
A. pages, features, components, hooks, api, types 기준으로 역할을 나눌 수 있다.

Q. Feature 기반 폴더 구조는 언제 좋아?
A. 도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. Props Type은 어디에 둬?
A. Component 전용이면 같은 파일에 두고 여러 곳에서 공유하면 types 파일로 분리한다.

Q. Over-Abstraction Reusable Component가 뭐야?
A. 실제 필요보다 과도하게 공통화해 Props가 복잡하고 사용성이 떨어지는 Component다.

Q. UI Component에서 API 호출하면 왜 문제야?
A. UI Component가 서버 구조와 도메인 동작에 결합되어 재사용성과 테스트 가능성이 떨어진다.

Q. Props Type에 any를 쓰면 왜 문제야?
A. Component Contract가 사라져 잘못된 Props 전달을 TypeScript가 막을 수 없다.

Q. Reusable Component 검수에서 가장 중요한 것은?
A. 도메인 의존성, API 호출 여부, Props Contract, 실제 반복 여부를 확인하는 것이다.

Q. API Logic Separation 검수에서 가장 중요한 것은?
A. API 요청 함수와 API 상태 로직이 Component UI 표시 책임과 분리되어 있는지 확인하는 것이다.

Q. TypeScript Component 검수에서 가장 중요한 것은?
A. Props Type이 any 없이 Required, Optional, Nullable, Callback Type을 명확히 표현하는지 확인하는 것이다.

Q. React Component Design Part06의 핵심은 뭐야?
A. Reusable Component, API Logic Separation, Response Mapping, TypeScript Props Type을 통해 재사용성과 타입 안정성이 높은 Component 구조를 만드는 것이다.

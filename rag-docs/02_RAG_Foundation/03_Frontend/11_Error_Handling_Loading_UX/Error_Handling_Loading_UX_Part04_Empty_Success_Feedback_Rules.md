# Error Handling & Loading UX Part04 - Empty State & Success Feedback Rules

---

# 1. Empty State Overview

## 1.1 Empty State Purpose

### [개념]

Empty State는 API 요청이 성공했지만 화면에 표시할 데이터가 없는 상태를 사용자에게 안내하는 UI 상태다.

Empty State는 Error State가 아니며, 데이터가 없는 이유와 사용자가 다음에 할 수 있는 행동을 함께 제공하는 것이 핵심이다.

---

### [핵심]

Empty State 주요 대상:

- Search Result Empty
- First Use Empty
- Filter Result Empty
- Favorite List Empty
- Review List Empty
- Notification Empty
- Chat Message Empty
- Visit History Empty
- Upload File Empty
- Dashboard Empty
- Table Empty
- Resource Collection Empty

핵심 규칙:

- Empty State와 Error State를 혼동하지 않는다.
- 요청 성공 후 데이터가 없을 때만 Empty State를 표시한다.
- 요청 중에는 Empty State를 표시하지 않는다.
- 초기 빈 배열을 바로 Empty State로 처리하지 않는다.
- 데이터 없음의 이유를 설명한다.
- 사용자가 할 수 있는 다음 행동을 제공한다.
- 검색 결과 없음과 첫 사용 Empty를 구분한다.
- Empty State는 부정적인 문구보다 다음 행동 중심 문구를 사용한다.

---

### [실무]

2026 실무 기준에서 Empty State는 단순히 “데이터 없음”만 보여주는 UI가 아니다.

Empty State 처리 흐름:

```text
Request Start
→ Loading State
→ Request Success
→ Data Empty Check
→ Empty Type 분류
→ Empty Message 작성
→ Next Action 제공
```

Empty State 선택 기준:

| Empty 유형          | 의미                               | 권장 Action               |
| ------------------- | ---------------------------------- | ------------------------- |
| First Use Empty     | 사용자가 아직 데이터를 만들지 않음 | 생성 / 탐색 CTA           |
| Search Result Empty | 검색 조건에 맞는 결과 없음         | 검색어 변경 / 필터 초기화 |
| Filter Result Empty | 필터 조건에 맞는 결과 없음         | 필터 초기화               |
| Favorite Empty      | 찜한 항목 없음                     | 항목 둘러보기             |
| Notification Empty  | 알림 없음                          | 별도 CTA 생략 가능        |
| Review Empty        | 리뷰 없음                          | 리뷰 작성 유도            |
| Chat Empty          | 메시지 없음                        | 첫 메시지 작성 유도       |

---

### [FAQ]

Q. Empty State는 뭐야?
A. 요청이 성공했지만 표시할 데이터가 없는 상태를 안내하는 UI다.

Q. Empty State와 Error State 차이는?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 실패 상태다.

Q. 검색 결과 없음은 Error State야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. Empty State에는 무엇을 넣어야 해?
A. 데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

---

# 2. Empty State Classification Rules

## 2.1 First Use Empty State

### [개념]

First Use Empty State는 사용자가 아직 데이터를 만들거나 저장하지 않은 초기 상태를 안내하는 Empty State다.

First Use Empty State는 사용자의 첫 행동을 유도하는 역할을 한다.

---

### [핵심]

First Use Empty State 사용 상황:

- 찜 목록 없음
- 리뷰 작성 내역 없음
- 알림 없음
- 방문 기록 없음
- 업로드 이미지 없음
- 작성한 게시글 없음
- 저장한 검색 조건 없음
- 등록한 결제 수단 없음
- 생성한 프로젝트 없음

핵심 규칙:

- 사용자를 탓하는 문구를 피한다.
- 다음 행동 중심 메시지를 작성한다.
- 서비스 핵심 기능으로 이동하는 CTA를 제공할 수 있다.
- 검색 결과 없음과 구분한다.
- 데이터가 없는 상태를 자연스럽게 안내한다.
- 불필요한 Error Tone을 사용하지 않는다.

---

### [실무]

찜 목록 Empty 예:

```jsx
<EmptyState
  title="아직 찜한 축제가 없습니다."
  description="마음에 드는 축제를 찾아 찜해 보세요."
  action={<Link to="/festivals">축제 둘러보기</Link>}
/>
```

리뷰 Empty 예:

```jsx
<EmptyState
  title="아직 작성한 리뷰가 없습니다."
  description="다녀온 축제의 후기를 남겨 보세요."
  action={<Link to="/festivals">리뷰 작성할 축제 찾기</Link>}
/>
```

알림 Empty 예:

```jsx
<EmptyState
  title="새로운 알림이 없습니다."
  description="중요한 소식이 생기면 이곳에 표시됩니다."
/>
```

권장:

- 첫 사용 상태에는 서비스 사용을 시작할 수 있는 CTA를 제공한다.
- CTA가 필요 없는 알림 없음 상태는 안내 메시지만 제공할 수 있다.
- “없습니다”만 반복하지 않고 다음 행동을 제안한다.
- 첫 사용 Empty와 검색 결과 Empty를 다른 메시지로 작성한다.

주의:

- “아무것도 하지 않았습니다”처럼 사용자를 탓하는 문구를 피한다.
- 데이터 없음 상태를 오류처럼 표현하지 않는다.
- CTA가 너무 많으면 사용자가 다음 행동을 고르기 어렵다.
- First Use Empty에서 필터 초기화 버튼을 제공하면 문맥이 맞지 않을 수 있다.

---

### [FAQ]

Q. First Use Empty State는 뭐야?
A. 사용자가 아직 데이터를 만들거나 저장하지 않은 초기 상태를 안내하는 Empty State다.

Q. 첫 사용 Empty State에는 버튼을 넣어도 돼?
A. 좋다. 사용자가 다음 행동을 쉽게 시작할 수 있도록 CTA를 제공할 수 있다.

Q. 알림이 없을 때도 CTA가 필요해?
A. 항상 필요하지는 않다. 단순 안내 메시지만으로 충분한 경우도 있다.

Q. First Use Empty와 Search Empty는 달라?
A. 다르다. First Use Empty는 아직 데이터가 없는 상태이고 Search Empty는 조건에 맞는 결과가 없는 상태다.

---

## 2.2 Search Result Empty State

### [개념]

Search Result Empty State는 검색 요청은 성공했지만 검색어 또는 조건에 맞는 결과가 없을 때 표시하는 Empty State다.

Search Result Empty는 사용자가 검색어, 필터, 정렬 조건을 조정할 수 있도록 안내해야 한다.

---

### [핵심]

Search Result Empty 사용 상황:

- Keyword Search Empty
- Region Search Empty
- Theme Search Empty
- Date Range Search Empty
- Combined Filter Empty
- Sort Result Empty
- Advanced Search Empty

핵심 규칙:

- 검색 결과가 없다는 사실을 명확히 안내한다.
- 검색어 변경을 제안한다.
- 필터 초기화 액션을 제공할 수 있다.
- 적용된 조건을 보여줄 수 있다.
- Error State와 혼동하지 않는다.
- 검색 요청 실패와 검색 결과 없음은 분리한다.
- 너무 단정적인 표현을 피한다.

---

### [실무]

검색 결과 Empty 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={
    <button type="button" onClick={resetFilters}>
      필터 초기화
    </button>
  }
/>
```

조건 표시 예:

```jsx
<EmptyState
  title="조건에 맞는 축제가 없습니다."
  description="지역, 테마, 기간 조건을 줄여 다시 검색해 보세요."
  action={<button type="button">검색 조건 초기화</button>}
/>
```

권장:

- 검색어가 있다면 검색어를 화면에 표시할 수 있다.
- 필터가 여러 개면 “필터 초기화” CTA를 제공한다.
- 검색 결과가 없는 상태와 API 실패 상태를 분리한다.
- 검색 조건을 완화할 수 있는 안내를 제공한다.

주의:

- API 실패를 검색 결과 없음으로 보여주지 않는다.
- 요청 완료 전 빈 배열을 검색 결과 없음으로 처리하지 않는다.
- 검색어가 틀렸다고 사용자를 탓하지 않는다.
- 필터 초기화 후 page index 또는 cursor 초기화를 고려한다.

---

### [FAQ]

Q. Search Result Empty State는 뭐야?
A. 검색 요청은 성공했지만 검색어 또는 조건에 맞는 결과가 없을 때 표시하는 Empty State다.

Q. 검색 결과 없음에는 어떤 행동을 제공하면 좋아?
A. 검색어 변경, 필터 초기화, 조건 완화 같은 행동을 제공하는 것이 좋다.

Q. API 실패도 검색 결과 없음으로 보여줘도 돼?
A. 아니다. API 실패는 Error State로 처리해야 한다.

Q. 필터 초기화 버튼은 언제 제공해?
A. 검색 조건이나 필터 때문에 결과가 없을 가능성이 있을 때 제공하면 좋다.

---

## 2.3 Filter Empty State

### [개념]

Filter Empty State는 특정 필터 조건에 맞는 데이터가 없을 때 표시하는 Empty State다.

Filter Empty State는 Search Result Empty와 유사하지만, 검색어보다 필터 조건 조정이 핵심이다.

---

### [핵심]

Filter Empty State 사용 상황:

- Category Filter Empty
- Region Filter Empty
- Date Range Filter Empty
- Status Filter Empty
- Price Range Filter Empty
- Theme Filter Empty
- Multi Filter Empty

핵심 규칙:

- 어떤 조건 때문에 결과가 없는지 안내한다.
- 필터 초기화 또는 조건 완화 CTA를 제공한다.
- 필터 변경 중 Loading과 구분한다.
- 필터 변경 실패와 필터 결과 없음은 구분한다.
- 필터 조건이 바뀌면 pagination state를 초기화한다.
- 기존 결과가 새 조건 결과처럼 보이지 않게 한다.

---

### [실무]

예:

```jsx
<EmptyState
  title="조건에 맞는 결과가 없습니다."
  description="선택한 필터를 줄이거나 초기화해 보세요."
  action={
    <button type="button" onClick={clearFilters}>
      필터 초기화
    </button>
  }
/>
```

필터 변경 Flow:

```text
Filter Change
→ Page Index Reset
→ Request Start
→ Loading or Refetch Indicator
→ Request Success
→ Data Empty
→ Filter Empty State
```

권장:

- 선택된 필터 목록을 함께 보여줄 수 있다.
- 조건이 많을수록 “필터 초기화” CTA가 유용하다.
- 날짜 범위 필터는 유효한 범위인지 함께 확인한다.
- 필터 변경 중에는 Empty State를 먼저 보여주지 않는다.

주의:

- 필터 결과 없음과 서버 오류를 혼동하지 않는다.
- 필터 변경 중 이전 데이터를 지울지 유지할지 기준을 정한다.
- page가 유지되어 결과가 없는 것처럼 보이는 문제를 확인한다.
- 필터 상태와 URL Query Param 동기화를 확인한다.

---

### [FAQ]

Q. Filter Empty State는 뭐야?
A. 특정 필터 조건에 맞는 데이터가 없을 때 표시하는 Empty State다.

Q. 필터 결과가 없을 때 무엇을 제공해야 해?
A. 필터 초기화, 조건 완화, 다른 조건 선택 같은 다음 행동을 제공하는 것이 좋다.

Q. 필터 변경 중 Empty State가 잠깐 보여도 돼?
A. 권장하지 않는다. 필터 요청 중에는 Loading 또는 Refetch Indicator를 보여주는 것이 좋다.

Q. 필터 변경 시 페이지 번호는 어떻게 해?
A. 보통 1페이지로 초기화하는 것이 안전하다.

---

# 3. Empty State Message Rules

## 3.1 Empty Message Writing Rules

### [개념]

Empty Message Writing은 데이터가 없는 상태를 사용자에게 이해 가능한 문장으로 전달하는 기준이다.

Empty Message는 현재 상태, 이유, 다음 행동을 짧고 명확하게 포함하는 것이 좋다.

---

### [핵심]

Empty Message 구성 요소:

- Title
- Description
- Action
- Context
- Friendly Tone
- Next Step
- Optional CTA

핵심 규칙:

- Title은 현재 상태를 명확히 말한다.
- Description은 이유 또는 다음 행동을 안내한다.
- Action은 필요한 경우에만 제공한다.
- 부정적인 표현을 줄인다.
- 사용자를 탓하는 문구를 피한다.
- Error처럼 보이는 문구를 피한다.
- 화면 문맥에 맞게 작성한다.
- 너무 긴 설명을 피한다.

---

### [실무]

좋은 Empty Message 구조:

```text
Title: 검색 결과가 없습니다.
Description: 검색어를 바꾸거나 필터를 초기화해 보세요.
Action: 필터 초기화
```

나쁜 예:

```text
데이터 없음.
```

좋은 예:

```text
검색 결과가 없습니다.
검색어를 바꾸거나 필터를 초기화해 보세요.
```

First Use 예:

```text
아직 찜한 축제가 없습니다.
마음에 드는 축제를 찾아 찜해 보세요.
```

Notification Empty 예:

```text
새로운 알림이 없습니다.
중요한 소식이 생기면 이곳에 표시됩니다.
```

권장:

- 짧은 Title + 보조 Description 구조를 사용한다.
- 사용자 행동이 필요한 경우 CTA를 제공한다.
- 데이터 없음 자체보다 다음 행동을 중심으로 작성한다.
- 서비스 톤에 맞게 부드럽게 작성한다.

주의:

- “잘못 검색했습니다”처럼 사용자 탓을 하지 않는다.
- “오류가 없습니다”처럼 의미가 모호한 문구를 쓰지 않는다.
- 서버 실패 상황을 Empty Message로 숨기지 않는다.
- 모든 Empty State에 무조건 CTA를 넣지 않는다.

---

### [FAQ]

Q. Empty State 문구는 어떻게 쓰면 좋아?
A. 현재 상태, 이유, 다음 행동을 짧고 명확하게 작성하는 것이 좋다.

Q. Empty State에 항상 버튼이 필요해?
A. 아니다. 사용자가 할 다음 행동이 명확할 때만 CTA를 제공하면 된다.

Q. “데이터 없음”만 써도 돼?
A. 권장하지 않는다. 사용자가 다음에 무엇을 할 수 있는지 알기 어렵다.

Q. Empty Message에서 피해야 할 표현은?
A. 사용자를 탓하는 문구, 오류처럼 보이는 문구, 너무 기술적인 표현을 피해야 한다.

---

## 3.2 Empty CTA Rules

### [개념]

Empty CTA는 Empty State에서 사용자가 다음 행동을 쉽게 수행하도록 제공하는 버튼, 링크, 액션이다.

Empty CTA는 모든 Empty State에 필요한 것은 아니며, 사용자가 실제로 할 수 있는 의미 있는 행동이 있을 때 제공한다.

---

### [핵심]

Empty CTA 후보:

- 필터 초기화
- 검색어 변경
- 새 항목 만들기
- 목록으로 이동
- 축제 둘러보기
- 리뷰 작성하기
- 첫 메시지 보내기
- 설정 변경
- 새로고침
- 도움말 보기

핵심 규칙:

- CTA는 Empty 원인과 연결되어야 한다.
- CTA는 하나 또는 두 개 이하로 제한한다.
- Primary CTA와 Secondary CTA를 구분한다.
- 사용자가 실제로 수행 가능한 행동만 제공한다.
- Error Retry와 Empty CTA를 혼동하지 않는다.
- 권한이 없는 행동을 CTA로 제공하지 않는다.

---

### [실무]

검색 Empty CTA:

```jsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={
    <button type="button" onClick={resetFilters}>
      필터 초기화
    </button>
  }
/>
```

First Use CTA:

```jsx
<EmptyState
  title="아직 작성한 게시글이 없습니다."
  description="첫 게시글을 작성해 보세요."
  action={<Link to="/posts/new">게시글 작성하기</Link>}
/>
```

권한 조건 예:

```tsx
<EmptyState
  title="아직 리뷰가 없습니다."
  description="첫 번째 리뷰를 남겨 보세요."
  action={
    isLoggedIn ? (
      <Link to="/reviews/new">리뷰 작성하기</Link>
    ) : (
      <Link to="/login">로그인하기</Link>
    )
  }
/>
```

권장:

- CTA는 Empty State 해결에 직접 연결한다.
- Search Empty는 필터 초기화가 자연스럽다.
- First Use Empty는 생성 또는 탐색 CTA가 자연스럽다.
- 로그인 필요 액션은 로그인 CTA로 연결할 수 있다.

주의:

- Empty CTA를 너무 많이 제공하지 않는다.
- “다시 시도”는 요청 실패 Error State에 더 적합하다.
- 사용자가 권한 없는 기능을 누르게 하지 않는다.
- CTA 클릭 후 상태 갱신 기준을 명확히 한다.

---

### [FAQ]

Q. Empty CTA는 뭐야?
A. Empty State에서 사용자가 다음 행동을 수행하도록 제공하는 버튼이나 링크다.

Q. Empty State에는 항상 CTA가 필요해?
A. 아니다. 사용자가 할 수 있는 의미 있는 다음 행동이 있을 때 제공하면 된다.

Q. Empty State의 “다시 시도” 버튼은 적절해?
A. 요청 성공 후 데이터가 없는 Empty State라면 보통 필터 초기화나 탐색 CTA가 더 적합하다. 다시 시도는 Error State에 더 적합하다.

Q. CTA는 몇 개가 적당해?
A. 보통 하나가 가장 좋고, 필요하면 Primary와 Secondary 두 개 정도로 제한하는 것이 좋다.

---

# 4. Empty State Implementation Rules

## 4.1 EmptyState Component Design

### [개념]

EmptyState Component는 데이터 없음 상태를 일관되게 보여주기 위한 재사용 가능한 UI 컴포넌트다.

EmptyState Component는 title, description, action을 props로 받아 화면별 문맥에 맞게 사용할 수 있다.

---

### [핵심]

EmptyState Component 구성:

- title
- description
- action
- icon optional
- className optional
- size optional
- variant optional
- test id optional

핵심 규칙:

- 공통 구조를 유지한다.
- 메시지는 화면별 props로 전달한다.
- action slot을 제공한다.
- 너무 추상화하지 않는다.
- ErrorState와 분리한다.
- LoadingState와 분리한다.
- 접근성을 고려한다.

---

### [실무]

기본 예:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: React.ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section>
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

사용 예:

```tsx
<EmptyState
  title="검색 결과가 없습니다."
  description="검색어를 바꾸거나 필터를 초기화해 보세요."
  action={
    <button type="button" onClick={resetFilters}>
      필터 초기화
    </button>
  }
/>
```

파일 구조 예:

```text
src
├ components
│  └ states
│     ├ LoadingState.tsx
│     ├ ErrorState.tsx
│     ├ EmptyState.tsx
│     └ SuccessMessage.tsx
```

권장:

- 반복되는 Empty UI는 공통 컴포넌트로 분리한다.
- 도메인별 메시지는 컴포넌트 내부에 하드코딩하지 않는다.
- action은 ReactNode로 받아 유연하게 처리한다.
- 목록 Empty와 상세 NotFound는 필요하면 다른 컴포넌트로 분리한다.

주의:

- EmptyState가 ErrorState 역할까지 하게 만들지 않는다.
- 모든 도메인 문구를 공통 컴포넌트에 몰아넣지 않는다.
- icon이나 illustration은 선택 요소로 둔다.
- 너무 많은 variant로 복잡하게 만들지 않는다.

---

### [FAQ]

Q. EmptyState는 공통 컴포넌트로 만들 수 있어?
A. 가능하다. title, description, action을 props로 받으면 여러 화면에서 재사용할 수 있다.

Q. EmptyState와 ErrorState를 하나로 합쳐도 돼?
A. 권장하지 않는다. 데이터 없음과 요청 실패는 의미와 사용자 행동이 다르기 때문에 분리하는 것이 좋다.

Q. EmptyState에 action slot이 필요한 이유는?
A. 화면별로 필터 초기화, 생성, 탐색 같은 다른 액션을 전달하기 위해 필요하다.

Q. EmptyState 문구를 컴포넌트 안에 하드코딩해도 돼?
A. 권장하지 않는다. 화면 문맥에 맞는 메시지를 props로 전달하는 것이 좋다.

---

## 4.2 Empty State Conditional Rendering

### [개념]

Empty State Conditional Rendering은 Loading, Error, Empty, Success 중 Empty State를 안전한 시점에 렌더링하는 조건부 렌더링 기준이다.

Empty State는 요청 성공 이후 데이터가 없을 때만 렌더링해야 한다.

---

### [핵심]

조건부 렌더링 순서:

```text
1. Loading State
2. Error State
3. Empty State
4. Success State
```

핵심 규칙:

- Loading 확인 후 Empty를 검사한다.
- Error 확인 후 Empty를 검사한다.
- 요청 성공 전 Empty를 표시하지 않는다.
- data null / undefined와 빈 배열을 구분한다.
- API 실패를 빈 배열로 변환하지 않는다.
- TanStack Query에서는 isLoading, isError 이후 data empty를 검사한다.

---

### [실무]

나쁜 예:

```tsx
if (items.length === 0) {
  return <EmptyState title="검색 결과가 없습니다." />;
}

if (isLoading) {
  return <LoadingState />;
}
```

문제:

- 요청 중 초기 빈 배열을 Empty로 오판할 수 있다.

개선 예:

```tsx
if (isLoading) {
  return <LoadingState />;
}

if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} />;
}

if (!items || items.length === 0) {
  return <EmptyState title="검색 결과가 없습니다." />;
}

return <ItemList items={items} />;
```

TanStack Query 예:

```tsx
const { data, isLoading, isError, error } = useQuery({
  queryKey: ["favorites"],
  queryFn: getFavorites,
});

if (isLoading) {
  return <LoadingState message="찜 목록을 불러오는 중입니다." />;
}

if (isError) {
  return <ErrorState message="찜 목록을 불러오지 못했습니다." />;
}

if (!data || data.length === 0) {
  return (
    <EmptyState
      title="아직 찜한 축제가 없습니다."
      description="마음에 드는 축제를 찾아 찜해 보세요."
    />
  );
}

return <FavoriteList favorites={data} />;
```

권장:

- Empty State는 Error State 다음에 배치한다.
- data shape를 안전하게 확인한다.
- 응답이 배열인지 페이지 객체인지 확인한다.
- 페이지네이션 데이터는 `items.length`, `totalElements`, `pages` 구조를 구분한다.

주의:

- `data?.length === 0`만으로 모든 Empty를 판단하지 않는다.
- `undefined`는 요청 전 또는 실패 상태일 수 있다.
- `[]`가 API 성공 결과인지 초기값인지 구분한다.
- Empty 판정 시점이 빠르면 Flicker가 발생한다.

---

### [FAQ]

Q. Empty State는 조건부 렌더링에서 언제 검사해?
A. Loading과 Error를 먼저 검사한 뒤 요청 성공 상태에서 데이터가 없을 때 검사한다.

Q. 초기 빈 배열 때문에 Empty가 먼저 보여?
A. Loading보다 Empty를 먼저 검사했거나 요청 완료 여부를 구분하지 않았을 가능성이 있다.

Q. data가 undefined면 Empty State야?
A. 항상 아니다. 요청 전, 로딩 중, 오류 상태일 수 있으므로 상태값과 함께 판단해야 한다.

Q. API 실패를 빈 배열로 변환하면 안 되는 이유는?
A. 실패 상태가 사라져 Error State를 보여줄 수 없기 때문이다.

---

# 5. Success Feedback Overview

## 5.1 Success Feedback Purpose

### [개념]

Success Feedback은 사용자 요청이 성공적으로 처리되었음을 알려주는 UX다.

Success Feedback은 사용자가 자신의 액션 결과를 인지하고 다음 행동을 결정할 수 있게 한다.

---

### [핵심]

Success Feedback 사용 상황:

- Create Success
- Update Success
- Delete Success
- Login Success
- Signup Success
- Favorite Success
- Like Success
- Upload Success
- Payment Success
- Password Change Success
- Form Submit Success
- Data Refetch Success

핵심 규칙:

- 중요한 사용자 액션 성공 후 결과를 인지시킨다.
- 성공 후 화면 상태를 갱신한다.
- 성공 후 redirect 여부를 결정한다.
- 성공 후 form reset 여부를 결정한다.
- 관련 Query를 invalidate 또는 refetch한다.
- 화면 변화만으로 충분하면 Toast를 남발하지 않는다.
- 성공 메시지는 짧고 명확하게 작성한다.

---

### [실무]

Success Feedback 방식:

| 방식                | 사용 상황         | 예                         |
| ------------------- | ----------------- | -------------------------- |
| Toast               | 짧은 성공 알림    | 리뷰가 등록되었습니다      |
| Inline Message      | 화면 내 결과 안내 | 프로필이 저장되었습니다    |
| Redirect            | 생성 후 상세 이동 | 게시글 작성 후 상세 페이지 |
| Modal Close         | 수정 완료         | 프로필 수정 모달 닫기      |
| Data Refetch        | 목록 최신화       | 리뷰 등록 후 목록 갱신     |
| Button State Change | 찜 / 좋아요       | 선택 상태 변경             |
| Confirmation Page   | 결제 / 가입 완료  | 결제 완료 페이지           |

Success 처리 Flow:

```text
Mutation Success
→ UI Feedback 선택
→ Data Refetch / Invalidate
→ Form Reset or Redirect
→ Button State Restore
→ User Next Action 제공
```

---

### [FAQ]

Q. Success Feedback은 뭐야?
A. 사용자 요청이 성공적으로 처리되었음을 알려주는 UX다.

Q. 성공할 때마다 Toast를 띄워야 해?
A. 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. Success Feedback에서 가장 중요한 것은?
A. 사용자가 요청 결과를 인지하고 화면 상태가 서버 상태와 동기화되는 것이다.

Q. 성공 후 데이터를 다시 불러와야 해?
A. 관련 화면이 서버 상태에 의존한다면 refetch 또는 query invalidate를 고려해야 한다.

---

# 6. Success Feedback Pattern Rules

## 6.1 Toast Success Rules

### [개념]

Toast Success는 사용자 액션이 성공했음을 짧게 알려주는 일시적 메시지다.

Toast는 저장, 삭제, 등록, 업로드 같은 액션 성공을 간단히 알릴 때 적합하다.

---

### [핵심]

Toast Success 사용 상황:

- Save Success
- Create Success
- Update Success
- Delete Success
- Review Submit Success
- Upload Success
- Favorite Toggle Success optional
- Copy Success
- Settings Save Success

핵심 규칙:

- 짧고 명확한 메시지를 사용한다.
- 중요하지만 화면 변화만으로 부족한 성공에 사용한다.
- 너무 사소한 액션에는 남발하지 않는다.
- Toast만 띄우고 데이터 갱신을 생략하지 않는다.
- 사용자가 반드시 알아야 하는 정보는 Toast에만 의존하지 않는다.
- 접근성 기준을 고려한다.

---

### [실무]

Toast Success 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews"] });
    toast.success("리뷰가 등록되었습니다.");
  },
});
```

삭제 성공 예:

```tsx
const deleteMutation = useMutation({
  mutationFn: deletePost,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["posts"] });
    toast.success("게시글이 삭제되었습니다.");
  },
});
```

권장 메시지:

```text
저장되었습니다.
리뷰가 등록되었습니다.
게시글이 삭제되었습니다.
프로필이 수정되었습니다.
파일이 업로드되었습니다.
```

권장:

- 성공 대상과 결과를 짧게 말한다.
- 성공 후 관련 목록이나 상세를 갱신한다.
- Toast 위치와 지속 시간을 일관되게 유지한다.
- 중복 Toast가 쌓이지 않게 관리한다.

주의:

- 좋아요 / 찜처럼 버튼 상태가 바로 바뀌는 액션에는 Toast가 과할 수 있다.
- Toast만 보여주고 목록 갱신을 하지 않으면 stale UI가 남는다.
- 결제 완료처럼 중요한 결과는 Toast보다 완료 페이지가 적합할 수 있다.
- Toast에 너무 긴 설명을 넣지 않는다.

---

### [FAQ]

Q. Toast Success는 언제 쓰면 좋아?
A. 저장, 삭제, 등록, 업로드처럼 짧게 성공을 알려도 되는 액션에 적합하다.

Q. 좋아요 성공마다 Toast를 띄워야 해?
A. 보통은 필요 없다. 버튼 상태 변화만으로 충분한 경우가 많다.

Q. Toast만 띄우면 성공 처리가 끝난 거야?
A. 아니다. 관련 데이터 갱신, 버튼 상태 복구, 화면 전환 등 필요한 처리를 함께 해야 한다.

Q. 중요한 성공 정보도 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 중요한 정보는 화면에 남는 방식으로 보여주는 것이 좋다.

---

## 6.2 Inline Success Message Rules

### [개념]

Inline Success Message는 특정 화면 영역이나 Form 안에서 성공 결과를 표시하는 메시지다.

Inline Success는 Toast보다 화면 문맥에 가깝고 사용자가 결과를 다시 확인하기 쉽다.

---

### [핵심]

Inline Success 사용 상황:

- Profile Save Success
- Settings Save Success
- Password Change Success
- Email Verification Sent
- Form Submit Success
- Draft Save Success
- Section Update Success

핵심 규칙:

- 성공한 영역 근처에 표시한다.
- 사용자가 결과를 확인할 수 있게 일정 시간 유지한다.
- Field Error와 시각적으로 구분한다.
- Toast보다 문맥이 중요한 성공에 사용한다.
- 성공 후 Form reset 여부를 결정한다.
- 중복 메시지를 관리한다.

---

### [실무]

Form Inline Success 예:

```tsx
function ProfileForm() {
  const [successMessage, setSuccessMessage] = useState("");

  async function handleSave(values) {
    await updateProfile(values);
    setSuccessMessage("프로필이 저장되었습니다.");
  }

  return (
    <form onSubmit={handleSubmit(handleSave)}>
      {successMessage && <p role="status">{successMessage}</p>}
      <ProfileFields />
      <button type="submit">저장</button>
    </form>
  );
}
```

Settings 저장 예:

```jsx
<section>
  <h2>알림 설정</h2>
  {saved && <p role="status">알림 설정이 저장되었습니다.</p>}
  <NotificationSettingsForm />
</section>
```

권장:

- Form 상단 또는 Submit Button 근처에 표시한다.
- 성공 메시지는 Error Message와 색상, 아이콘, 문구를 구분한다.
- 저장 후 일정 시간이 지나면 사라지게 할 수 있다.
- 다시 수정하면 성공 메시지를 초기화할 수 있다.

주의:

- 성공 메시지가 오래 남아 현재 상태와 불일치하지 않게 한다.
- 여러 저장 영역이 있는 화면에서는 어떤 영역이 저장되었는지 명확히 한다.
- Inline Success와 Toast를 동시에 남발하지 않는다.
- role status 등 접근성 속성을 고려한다.

---

### [FAQ]

Q. Inline Success Message는 언제 써?
A. Form이나 설정 화면처럼 특정 영역의 성공 결과를 화면 안에서 보여줄 때 적합하다.

Q. Toast와 Inline Success를 같이 써도 돼?
A. 가능하지만 중복 알림이 과하면 불필요하므로 하나를 선택하는 것이 좋다.

Q. Inline Success는 어디에 보여줘?
A. 성공한 Form 상단, Submit Button 근처, 또는 관련 섹션 안에 보여주는 것이 좋다.

Q. Inline Success 메시지는 계속 보여줘도 돼?
A. 상황에 따라 다르지만 현재 상태와 불일치하지 않도록 관리해야 한다.

---

## 6.3 Redirect Success Rules

### [개념]

Redirect Success는 요청 성공 후 사용자를 다른 화면으로 이동시켜 성공 결과를 자연스럽게 보여주는 방식이다.

Redirect Success는 생성, 가입, 결제, 로그인 같은 액션에서 자주 사용한다.

---

### [핵심]

Redirect Success 사용 상황:

- Post Create Success
- Review Create Success optional
- Signup Success
- Login Success
- Payment Success
- Order Complete
- Delete Success
- Resource Created Detail Move

핵심 규칙:

- Redirect 목적지를 명확히 한다.
- 사용자가 성공 여부를 인지할 수 있게 한다.
- 필요하면 Success Message를 함께 전달한다.
- 생성 성공 후 상세 페이지로 이동할 수 있다.
- 삭제 성공 후 목록 페이지로 이동할 수 있다.
- 결제 성공은 완료 페이지가 적합하다.
- Redirect가 너무 빠르면 성공 인지가 어려울 수 있다.

---

### [실무]

생성 후 상세 이동 예:

```tsx
const mutation = useMutation({
  mutationFn: createPost,
  onSuccess: (createdPost) => {
    navigate(`/posts/${createdPost.id}`, {
      state: { message: "게시글이 등록되었습니다." },
    });
  },
});
```

삭제 후 목록 이동 예:

```tsx
const deleteMutation = useMutation({
  mutationFn: deletePost,
  onSuccess: () => {
    navigate("/posts", {
      state: { message: "게시글이 삭제되었습니다." },
    });
  },
});
```

결제 성공 예:

```text
Payment Success
→ Payment Complete Page
→ 결제 결과 요약 표시
→ 주문 / 후원 내역 이동 제공
```

권장:

- 생성 성공 후 상세 페이지 이동을 고려한다.
- 삭제 성공 후 더 이상 존재하지 않는 상세 페이지에 머물지 않는다.
- 로그인 성공 후 원래 접근하려던 페이지로 복귀할 수 있다.
- 결제 성공은 Toast보다 완료 화면이 적합하다.
- redirect 후 message state 또는 query param으로 성공 메시지를 전달할 수 있다.

주의:

- 저장 성공 후 무조건 이동하면 사용자가 계속 편집해야 할 때 불편할 수 있다.
- redirect 후 성공 메시지가 사라지면 사용자가 결과를 인지하지 못할 수 있다.
- 결제 성공 / 실패 redirect는 보안과 검증 흐름을 함께 고려해야 한다.
- 삭제 후 기존 상세 데이터를 계속 보여주지 않는다.

---

### [FAQ]

Q. 저장 성공 후 바로 이동해도 돼?
A. 가능하다. 다만 사용자가 성공 여부를 이해할 수 있도록 메시지나 자연스러운 화면 전환을 제공하는 것이 좋다.

Q. 생성 성공 후 어디로 이동하는 게 좋아?
A. 생성된 리소스의 상세 페이지나 목록 페이지로 이동하는 것이 일반적이다.

Q. 삭제 성공 후 현재 상세 페이지에 남아도 돼?
A. 삭제된 리소스의 상세 페이지에 남는 것은 혼란스러울 수 있으므로 목록 이동이 자연스럽다.

Q. 결제 성공은 Toast로 충분해?
A. 보통은 결제 완료 페이지처럼 화면에 남는 확인 UX가 더 적합하다.

---

# 7. Success Data Synchronization Rules

## 7.1 Query Invalidation After Success

### [개념]

Query Invalidation은 Mutation 성공 후 관련 서버 데이터를 다시 조회하도록 표시하는 작업이다.

Success Feedback은 메시지만 보여주는 것이 아니라 서버 상태와 화면 상태를 동기화해야 완성된다.

---

### [핵심]

Query Invalidation 사용 상황:

- Review Create Success
- Review Delete Success
- Favorite Toggle Success
- Like Toggle Success
- Profile Update Success
- Post Create / Update / Delete
- Notification Read Success
- Comment Create / Delete
- Upload Success

핵심 규칙:

- Mutation 성공 후 관련 Query를 invalidate한다.
- 목록, 상세, 카운트 데이터를 함께 고려한다.
- Toast만 띄우고 데이터 갱신을 생략하지 않는다.
- Optimistic UI 사용 시 rollback 기준을 둔다.
- 서버 상태와 클라이언트 캐시가 어긋나지 않게 한다.
- 필요한 경우 직접 cache update를 사용할 수 있다.

---

### [실무]

리뷰 등록 후 목록 갱신:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews", festivalId] });
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    toast.success("리뷰가 등록되었습니다.");
  },
});
```

찜 성공 후 상세 갱신:

```tsx
const favoriteMutation = useMutation({
  mutationFn: toggleFavorite,
  onSuccess: () => {
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
    queryClient.invalidateQueries({ queryKey: ["favorites"] });
  },
});
```

알림 읽음 처리:

```tsx
const readMutation = useMutation({
  mutationFn: markNotificationAsRead,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["notifications"] });
    queryClient.invalidateQueries({ queryKey: ["notification-count"] });
  },
});
```

권장:

- 성공한 mutation이 영향을 주는 화면을 모두 식별한다.
- 목록과 상세의 캐시가 동시에 바뀌는지 확인한다.
- count, badge, summary 데이터도 갱신한다.
- 불필요한 전체 invalidate는 피하고 queryKey를 명확히 한다.
- 사용자에게 보이는 상태가 즉시 반영되어야 하면 optimistic update를 고려한다.

주의:

- 성공 Toast만 띄우고 목록을 갱신하지 않으면 stale UI가 된다.
- 좋아요 수, 리뷰 수, 알림 수 같은 count 갱신을 놓치기 쉽다.
- queryKey가 불일치하면 invalidate가 동작하지 않는다.
- 과도한 invalidate는 불필요한 네트워크 요청을 만든다.

---

### [FAQ]

Q. 성공 후 Query Invalidation은 왜 필요해?
A. 서버 상태가 바뀐 뒤 화면의 캐시 데이터도 최신 상태로 동기화해야 하기 때문이다.

Q. Toast만 띄우면 성공 처리가 충분해?
A. 아니다. 관련 목록, 상세, 카운트 데이터가 갱신되어야 한다.

Q. 어떤 Query를 invalidate해야 해?
A. Mutation이 영향을 주는 목록, 상세, 카운트, 요약 데이터를 기준으로 결정한다.

Q. queryKey가 틀리면 어떻게 돼?
A. invalidate가 제대로 동작하지 않아 화면이 오래된 데이터를 계속 보여줄 수 있다.

---

## 7.2 Optimistic Success Feedback

### [개념]

Optimistic Success Feedback은 서버 응답을 기다리기 전에 UI를 먼저 성공한 것처럼 갱신하는 방식이다.

Optimistic UI는 좋아요, 찜, 토글처럼 즉각적인 반응이 중요한 액션에서 사용할 수 있다.

---

### [핵심]

Optimistic UI 사용 상황:

- Like Toggle
- Favorite Toggle
- Follow Toggle
- Notification Read
- Simple Status Toggle
- Small Reversible Action

핵심 규칙:

- 실패 시 rollback이 가능해야 한다.
- 중요한 결제 / 삭제 요청에는 신중하게 사용한다.
- 서버 상태와 최종 동기화한다.
- 충돌 발생 시 refetch한다.
- 사용자에게 빠른 피드백을 제공한다.
- pending 중 중복 클릭을 방지한다.

---

### [실무]

좋아요 Optimistic 예:

```tsx
const likeMutation = useMutation({
  mutationFn: toggleLike,
  onMutate: async () => {
    await queryClient.cancelQueries({
      queryKey: ["festival-detail", festivalId],
    });

    const previous = queryClient.getQueryData(["festival-detail", festivalId]);

    queryClient.setQueryData(["festival-detail", festivalId], (old) => ({
      ...old,
      liked: !old.liked,
      likeCount: old.liked ? old.likeCount - 1 : old.likeCount + 1,
    }));

    return { previous };
  },
  onError: (_error, _variables, context) => {
    queryClient.setQueryData(
      ["festival-detail", festivalId],
      context?.previous,
    );
    toast.error("좋아요 처리에 실패했습니다.");
  },
  onSettled: () => {
    queryClient.invalidateQueries({
      queryKey: ["festival-detail", festivalId],
    });
  },
});
```

권장:

- rollback을 위해 이전 상태를 저장한다.
- 실패 시 사용자에게 오류를 안내한다.
- 최종적으로 invalidate하여 서버 상태와 맞춘다.
- 토글 버튼은 요청 중 disabled 처리할 수 있다.
- 409 Conflict 발생 시 서버 상태를 refetch한다.

주의:

- 결제, 삭제, 예약처럼 되돌리기 어려운 요청에는 Optimistic UI를 신중히 사용한다.
- rollback 없이 Optimistic UI를 적용하면 서버 실패 후 UI가 틀어질 수 있다.
- 좋아요 수가 음수가 되지 않도록 방어한다.
- 동시 요청이 많으면 상태 충돌이 발생할 수 있다.

---

### [FAQ]

Q. Optimistic UI는 뭐야?
A. 서버 응답을 기다리기 전에 UI를 먼저 성공한 것처럼 갱신하는 방식이다.

Q. Optimistic UI는 언제 쓰면 좋아?
A. 좋아요, 찜, 팔로우처럼 즉각 반응이 중요하고 되돌리기 쉬운 액션에 적합하다.

Q. Optimistic UI 실패 시 어떻게 해?
A. 이전 상태로 rollback하고 오류 메시지를 보여준 뒤 서버 상태를 다시 조회하는 것이 좋다.

Q. 결제에도 Optimistic UI를 써도 돼?
A. 권장하지 않는다. 결제는 처리 여부 확인이 중요하므로 서버 결과를 기준으로 UX를 구성해야 한다.

---

# 8. Success Feedback Message Rules

## 8.1 Success Message Writing Rules

### [개념]

Success Message Writing은 사용자 요청이 성공했음을 짧고 명확하게 전달하는 문구 작성 기준이다.

Success Message는 액션 결과를 분명히 말하되 과도하게 길거나 반복적이지 않아야 한다.

---

### [핵심]

Success Message 구성:

- Action Result
- Target Resource
- Short Sentence
- Friendly Tone
- Optional Next Step

핵심 규칙:

- 무엇이 성공했는지 명확히 말한다.
- 짧게 작성한다.
- 기술 용어를 피한다.
- 현재 화면 상태와 일치해야 한다.
- 성공했지만 추가 조치가 필요하면 다음 행동을 안내한다.
- 불필요한 감탄사나 과장 표현을 피한다.
- 실패 가능성이 남아 있는 상태를 성공으로 단정하지 않는다.

---

### [실무]

권장 문구:

```text
저장되었습니다.
리뷰가 등록되었습니다.
프로필이 수정되었습니다.
게시글이 삭제되었습니다.
파일이 업로드되었습니다.
이메일 인증 링크를 보냈습니다.
비밀번호가 변경되었습니다.
```

나쁜 예:

```text
성공!!!
작업 완료됨.
OK.
데이터 처리가 성공적으로 수행되었습니다.
```

좋은 예:

```text
리뷰가 등록되었습니다.
```

다음 행동 포함 예:

```text
이메일 인증 링크를 보냈습니다. 메일함을 확인해 주세요.
```

권장:

- 사용자가 수행한 액션과 결과를 연결한다.
- Toast 메시지는 한 줄로 작성한다.
- Inline Success는 필요하면 보조 설명을 포함한다.
- 성공 후 이동이 있다면 이동한 화면 문맥과 메시지가 맞아야 한다.

주의:

- 너무 많은 성공 메시지를 반복하지 않는다.
- 자동 저장처럼 빈번한 성공에는 조용한 표시가 더 적합할 수 있다.
- 서버 처리 확정 전 성공 메시지를 보여주지 않는다.
- “완벽히 처리되었습니다”처럼 과장하지 않는다.

---

### [FAQ]

Q. Success Message는 어떻게 쓰면 좋아?
A. 무엇이 성공했는지 짧고 명확하게 작성하는 것이 좋다.

Q. Success Toast 문구는 길어도 돼?
A. 권장하지 않는다. Toast는 짧은 문구가 적합하다.

Q. 성공 메시지에 다음 행동을 넣어도 돼?
A. 이메일 인증처럼 추가 행동이 필요한 경우에는 넣는 것이 좋다.

Q. 성공 메시지를 너무 자주 보여주면 문제야?
A. 가능하다. 사소한 액션마다 Toast를 띄우면 사용자가 피로감을 느낄 수 있다.

---

# 9. Empty / Success Accessibility Rules

## 9.1 Empty State Accessibility

### [개념]

Empty State Accessibility는 보조 기술 사용자도 데이터가 없는 상태와 다음 행동을 이해할 수 있게 하는 기준이다.

Empty State는 시각적 일러스트에만 의존하지 않고 텍스트와 의미 있는 구조를 제공해야 한다.

---

### [핵심]

접근성 기준:

- Semantic Section
- Heading
- Text Description
- Accessible Button / Link
- Focus Order
- Icon aria-hidden
- Keyboard Accessible CTA
- Clear Label

핵심 규칙:

- Empty State 제목을 heading으로 제공한다.
- CTA는 button 또는 link 역할에 맞게 사용한다.
- 장식용 아이콘은 `aria-hidden` 처리한다.
- 색상이나 그림만으로 의미를 전달하지 않는다.
- Empty State가 동적으로 나타나면 필요한 경우 status role을 고려한다.
- CTA는 키보드로 접근 가능해야 한다.

---

### [실무]

접근 가능한 EmptyState 예:

```tsx
function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section aria-labelledby="empty-state-title">
      <h2 id="empty-state-title">{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

아이콘 예:

```jsx
<div aria-hidden="true">
  <EmptyIcon />
</div>
```

권장:

- Empty State의 제목과 설명을 텍스트로 제공한다.
- CTA의 label은 구체적으로 작성한다.
- “여기를 클릭”보다 “필터 초기화”처럼 행동을 명확히 쓴다.
- Empty State 진입 시 무조건 focus를 이동하지 않는다.
- 사용자가 다음 행동으로 자연스럽게 tab 이동할 수 있게 한다.

주의:

- 일러스트만 있고 텍스트가 없으면 접근성이 낮다.
- 버튼처럼 보이는 div를 사용하지 않는다.
- CTA가 키보드로 접근 불가능하면 안 된다.
- Empty State를 Error처럼 role alert로 처리하지 않는다.

---

### [FAQ]

Q. Empty State에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 데이터가 없는 상태와 다음 행동을 이해할 수 있어야 한다.

Q. Empty State 아이콘은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소라면 aria-hidden 처리하는 것이 좋다.

Q. Empty State CTA는 button이 좋아 link가 좋아?
A. 화면 내 동작이면 button, 다른 페이지 이동이면 link가 적합하다.

Q. Empty State에 role alert를 써도 돼?
A. 보통은 필요하지 않다. Error State와 달리 긴급 오류가 아니기 때문이다.

---

## 9.2 Success Feedback Accessibility

### [개념]

Success Feedback Accessibility는 성공 메시지를 보조 기술 사용자가 인지할 수 있게 하는 기준이다.

Success Message는 시각적 Toast나 색상 변화에만 의존하지 않고 텍스트와 적절한 ARIA 역할을 고려해야 한다.

---

### [핵심]

접근성 기준:

- `role="status"`
- `aria-live="polite"`
- Text Message
- Button Text Change
- Focus Preservation
- Non-color-only Feedback
- Toast Accessibility
- Confirmation Page Heading

핵심 규칙:

- 성공 메시지는 텍스트로 제공한다.
- Inline Success에는 `role="status"`를 고려한다.
- Toast는 스크린 리더가 인식할 수 있어야 한다.
- 색상만으로 성공을 표시하지 않는다.
- 성공 후 focus 이동이 필요한지 검토한다.
- 페이지 이동 후 완료 화면에는 명확한 heading을 제공한다.

---

### [실무]

Inline Success 예:

```jsx
{
  successMessage && (
    <p role="status" aria-live="polite">
      {successMessage}
    </p>
  );
}
```

버튼 상태 예:

```jsx
<button type="submit" disabled={isPending}>
  {isPending ? "저장 중..." : "저장"}
</button>
```

완료 페이지 예:

```jsx
<main>
  <h1>결제가 완료되었습니다.</h1>
  <p>후원 내역에서 상세 정보를 확인할 수 있습니다.</p>
  <Link to="/donations">후원 내역 보기</Link>
</main>
```

권장:

- 성공 메시지는 스크린 리더가 읽을 수 있는 텍스트로 제공한다.
- Toast 시스템이 접근성을 지원하는지 확인한다.
- 결제 완료 같은 중요한 성공은 완료 페이지로 명확히 표시한다.
- 성공 후 focus를 어디에 둘지 화면 전환 기준으로 검토한다.

주의:

- 색상만 초록색으로 바꾸고 텍스트를 제공하지 않는 것은 부족하다.
- Toast가 너무 빨리 사라지면 내용을 놓칠 수 있다.
- 성공 후 focus가 사라지거나 페이지 상단으로 튀는 문제를 확인한다.
- 반복되는 자동 저장 성공 메시지는 과도한 live announcement가 될 수 있다.

---

### [FAQ]

Q. Success Message에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청이 성공했음을 인지할 수 있어야 한다.

Q. Inline Success에는 어떤 role이 좋아?
A. 일반적인 성공 알림에는 role status와 aria-live polite를 고려할 수 있다.

Q. 색상만 초록색으로 바꾸면 성공 표시로 충분해?
A. 아니다. 텍스트나 아이콘 label 등 색상 외 정보가 필요하다.

Q. Toast는 접근성 문제가 있을 수 있어?
A. 있다. 스크린 리더 인식, 표시 시간, focus 흐름을 고려해야 한다.

---

# 10. Empty / Success Troubleshooting Rules

## 10.1 Empty State Flicker Troubleshooting

### [개념]

Empty State Flicker는 요청 완료 전에 Empty State가 잠깐 표시되었다가 실제 데이터가 나타나는 문제다.

이 문제는 초기 배열, loading 초기값, 조건부 렌더링 순서, query enabled 조건 오류에서 자주 발생한다.

---

### [핵심]

주요 원인:

- 초기 data가 빈 배열
- Loading 판정보다 Empty 판정을 먼저 실행
- 요청 완료 여부 구분 없음
- query enabled 조건 누락
- placeholderData 사용 기준 없음
- Refetch 중 기존 데이터 제거
- Auth Initialized 구분 없음
- Filter Change 중 Empty 판정

핵심 규칙:

- Loading State를 Empty State보다 먼저 검사한다.
- 요청 완료 후에만 Empty State를 표시한다.
- `isLoading`, `isFetched`, `isSuccess` 같은 상태를 함께 고려한다.
- Auth 확인 전 Empty를 표시하지 않는다.
- Filter 변경 중에는 Loading 또는 Refetch Indicator를 표시한다.

---

### [실무]

Debug Flow:

```text
Empty Flicker 발생
→ 초기 data 값 확인
→ loading 초기값 확인
→ 조건부 렌더링 순서 확인
→ 요청 완료 여부 확인
→ query enabled 조건 확인
→ refetch 중 data 유지 여부 확인
```

나쁜 예:

```tsx
if (items.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}

if (loading) {
  return <LoadingState />;
}
```

개선 예:

```tsx
if (loading) {
  return <LoadingState />;
}

if (error) {
  return <ErrorState message="데이터를 불러오지 못했습니다." />;
}

if (items.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}
```

TanStack Query 기준:

```tsx
if (isLoading) {
  return <LoadingState />;
}

if (isError) {
  return <ErrorState message={getApiErrorMessage(error)} />;
}

if (isSuccess && data.length === 0) {
  return <EmptyState title="결과가 없습니다." />;
}
```

권장:

- Empty 판정에 요청 성공 상태를 포함한다.
- 요청 완료 전에는 Empty를 보여주지 않는다.
- Refetch 중에는 기존 데이터를 유지하거나 갱신 표시를 사용한다.
- 조건부 렌더링 순서를 문서화한다.

주의:

- 초기 빈 배열은 실제 빈 결과가 아닐 수 있다.
- `data?.length === 0`만으로 Empty를 판단하면 Flicker가 생길 수 있다.
- Search / Filter 화면에서 조건 변경 중 Empty가 깜빡일 수 있다.
- Auth 기반 데이터는 인증 초기화 후 조회해야 한다.

---

### [FAQ]

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Empty Flicker를 막으려면?
A. Loading과 Error를 먼저 검사하고 요청 성공 후에만 Empty를 표시해야 한다.

Q. TanStack Query에서 Empty는 언제 검사해?
A. isLoading과 isError를 처리한 뒤 isSuccess 상태에서 data가 비었는지 검사하는 것이 안전하다.

Q. Refetch 중 Empty가 보이면?
A. 기존 데이터를 지우는 구조일 수 있으므로 placeholderData, keep previous data, isFetching 표시 기준을 확인해야 한다.

---

## 10.2 Success Feedback Missing Troubleshooting

### [개념]

Success Feedback Missing은 요청은 성공했지만 사용자가 성공 여부를 인지하지 못하는 문제다.

이 문제는 성공 메시지 누락, 화면 갱신 누락, redirect 기준 누락, cache invalidation 누락에서 발생한다.

---

### [핵심]

주요 원인:

- onSuccess 처리 누락
- Toast / Inline Message 누락
- Query Invalidation 누락
- Button State 복구 누락
- Redirect 누락
- Form Reset 기준 없음
- Stale UI 유지
- Optimistic UI 실패 처리 없음
- 성공 후 화면 변화 없음

핵심 규칙:

- 성공 후 사용자가 결과를 인지할 수 있어야 한다.
- 관련 데이터를 갱신해야 한다.
- 버튼 pending 상태를 복구해야 한다.
- Form reset 또는 유지 기준을 정해야 한다.
- 성공 후 이동이 필요하면 redirect한다.
- 중요한 성공은 화면에 남는 방식으로 표시한다.

---

### [실무]

Debug Flow:

```text
요청 성공
→ onSuccess 실행 여부 확인
→ Success Message 표시 여부 확인
→ Query Invalidation 확인
→ 화면 데이터 갱신 확인
→ Button State 복구 확인
→ Redirect 필요 여부 확인
```

나쁜 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
});
```

문제:

- 성공 후 메시지, 데이터 갱신, Form reset 기준이 없다.

개선 예:

```tsx
const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews", festivalId] });
    toast.success("리뷰가 등록되었습니다.");
    resetForm();
  },
});
```

권장:

- 성공 시 어떤 화면 상태가 바뀌어야 하는지 먼저 정의한다.
- onSuccess에 메시지와 데이터 동기화 처리를 둔다.
- 화면 변화가 명확하면 Toast를 생략할 수 있다.
- 중요한 성공은 완료 페이지 또는 Inline Message로 보여준다.

주의:

- 성공했는데 UI가 그대로면 사용자는 실패로 오해할 수 있다.
- Toast만 있고 데이터가 갱신되지 않으면 신뢰가 떨어진다.
- redirect 후 메시지가 전달되지 않으면 성공 인지가 어렵다.
- pending 상태가 남아 버튼이 계속 disabled 될 수 있다.

---

### [FAQ]

Q. 요청은 성공했는데 사용자가 성공했는지 몰라?
A. Success Message, 화면 갱신, redirect, 버튼 상태 복구가 누락되었을 수 있다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

Q. 성공 후 버튼이 계속 disabled야?
A. pending 상태가 정상적으로 종료되는지, mutation 상태를 올바르게 사용하는지 확인해야 한다.

Q. 성공 후 Form을 reset해야 해?
A. 상황에 따라 다르다. 작성 완료 후 새 입력을 받을 때는 reset하고, 설정 저장은 입력값을 유지하는 경우가 많다.

---

# 11. Empty / Success Checklist

## 11.1 Empty State Review Checklist

### [개념]

Empty State Review Checklist는 데이터 없음 상태가 Error, Loading, Success와 올바르게 분리되었는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Empty State와 Error State를 구분했는가?
- [ ] 요청 성공 후 데이터 없음일 때만 Empty State를 표시하는가?
- [ ] 요청 중 Empty State가 표시되지 않는가?
- [ ] 초기 빈 배열을 바로 Empty State로 처리하지 않는가?
- [ ] First Use Empty와 Search Empty를 구분했는가?
- [ ] Filter Empty에서 필터 초기화 CTA를 제공하는가?
- [ ] Empty Message가 현재 상태와 다음 행동을 설명하는가?
- [ ] 사용자를 탓하는 문구가 없는가?
- [ ] Empty CTA가 문맥에 맞는가?
- [ ] Empty CTA가 너무 많지 않은가?
- [ ] EmptyState Component가 ErrorState와 분리되어 있는가?
- [ ] Empty State 접근성을 고려했는가?
- [ ] Empty Flicker 가능성을 점검했는가?
```

---

### [실무]

검수 흐름:

```text
Empty 발생 조건 확인
→ 요청 성공 여부 확인
→ Empty 유형 분류
→ Message 확인
→ CTA 확인
→ Accessibility 확인
→ Flicker 가능성 확인
```

화면별 기준:

| 화면        | Empty 기준                             |
| ----------- | -------------------------------------- |
| 검색 화면   | 검색 결과 없음 + 필터 초기화           |
| 찜 목록     | 아직 찜한 항목 없음 + 탐색 CTA         |
| 리뷰 목록   | 아직 리뷰 없음 + 작성 CTA              |
| 알림 목록   | 새로운 알림 없음                       |
| 채팅방      | 아직 메시지 없음 + 첫 메시지 유도      |
| 상세 페이지 | 일반 Empty보다 Resource Not Found 고려 |

---

### [FAQ]

Q. Empty State 검수에서 가장 중요한 것은?
A. 요청 성공 후 데이터 없음 상태인지 확인하고 Error State와 혼동하지 않는 것이다.

Q. Empty Message 검수 기준은?
A. 현재 상태, 이유, 다음 행동이 짧고 명확하게 포함되어야 한다.

Q. Empty CTA 검수 기준은?
A. 사용자가 실제로 수행 가능한 의미 있는 다음 행동인지 확인해야 한다.

Q. 상세 페이지 데이터 없음도 Empty State로 검수해?
A. 상세 페이지는 일반 Empty보다 Resource Not Found UI로 검수하는 것이 적합한 경우가 많다.

---

## 11.2 Success Feedback Review Checklist

### [개념]

Success Feedback Review Checklist는 사용자 액션 성공 후 결과 인지, 데이터 동기화, 화면 전환이 올바르게 처리되었는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] 중요한 사용자 액션 성공 후 Feedback이 있는가?
- [ ] 성공 메시지가 짧고 명확한가?
- [ ] Toast, Inline Message, Redirect 중 적절한 방식을 선택했는가?
- [ ] 화면 변화만으로 충분한 액션에 Toast를 남발하지 않는가?
- [ ] 성공 후 관련 Query를 invalidate 또는 update하는가?
- [ ] 목록, 상세, count 데이터가 동기화되는가?
- [ ] 성공 후 Form reset 또는 유지 기준이 명확한가?
- [ ] 성공 후 redirect가 필요한 경우 목적지가 적절한가?
- [ ] 결제 / 가입 완료 같은 중요한 성공은 화면에 남는가?
- [ ] Optimistic UI 사용 시 rollback 기준이 있는가?
- [ ] 성공 메시지 접근성을 고려했는가?
- [ ] 성공 후 pending / disabled 상태가 복구되는가?
- [ ] Success Feedback Missing 가능성을 점검했는가?
```

---

### [실무]

검수 흐름:

```text
Mutation Success 확인
→ Feedback 방식 선택 확인
→ Data Synchronization 확인
→ Form / Button State 확인
→ Redirect 확인
→ Accessibility 확인
→ Stale UI 가능성 확인
```

액션별 기준:

| 액션          | 권장 Success UX                            |
| ------------- | ------------------------------------------ |
| 리뷰 등록     | Toast + 리뷰 목록 invalidate               |
| 프로필 수정   | Inline Success + 프로필 query invalidate   |
| 좋아요        | Button State Change + count update         |
| 찜            | Button State Change + favorites invalidate |
| 게시글 삭제   | Toast + 목록 이동                          |
| 결제 완료     | Complete Page                              |
| 회원가입 완료 | 완료 안내 / 로그인 이동                    |
| 알림 읽음     | 상태 변경 + count invalidate               |

---

### [FAQ]

Q. Success Feedback 검수에서 가장 중요한 것은?
A. 사용자가 성공 결과를 인지하고 화면 데이터가 서버 상태와 동기화되는지 확인하는 것이다.

Q. 성공 후 Toast가 꼭 필요해?
A. 아니다. 버튼 상태 변화나 화면 이동으로 충분한 경우에는 생략할 수 있다.

Q. 성공 후 stale UI를 막으려면?
A. 관련 Query를 invalidate하거나 cache update를 수행해야 한다.

Q. Optimistic UI 검수 핵심은?
A. 실패 시 rollback 가능 여부와 최종 서버 상태 동기화 여부다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part04는 무엇을 다뤄?
A. Empty State, First Use Empty, Search Empty, Filter Empty, Success Feedback, Toast Success, Query Invalidation 기준을 다룬다.

Q. Empty State는 뭐야?
A. 요청이 성공했지만 표시할 데이터가 없는 상태를 안내하는 UI다.

Q. Empty State와 Error State 차이는?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 실패 상태다.

Q. 검색 결과 없음은 Error State야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. Empty State에는 무엇을 넣어야 해?
A. 데이터가 없다는 메시지, 이유, 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

Q. First Use Empty State는 뭐야?
A. 사용자가 아직 데이터를 만들거나 저장하지 않은 초기 상태를 안내하는 Empty State다.

Q. 첫 사용 Empty State에는 버튼을 넣어도 돼?
A. 좋다. 사용자가 다음 행동을 쉽게 시작할 수 있도록 CTA를 제공할 수 있다.

Q. 알림이 없을 때도 CTA가 필요해?
A. 항상 필요하지는 않다. 단순 안내 메시지만으로 충분한 경우도 있다.

Q. First Use Empty와 Search Empty는 달라?
A. 다르다. First Use Empty는 아직 데이터가 없는 상태이고 Search Empty는 조건에 맞는 결과가 없는 상태다.

Q. Search Result Empty State는 뭐야?
A. 검색 요청은 성공했지만 검색어 또는 조건에 맞는 결과가 없을 때 표시하는 Empty State다.

Q. 검색 결과 없음에는 어떤 행동을 제공하면 좋아?
A. 검색어 변경, 필터 초기화, 조건 완화 같은 행동을 제공하는 것이 좋다.

Q. API 실패도 검색 결과 없음으로 보여줘도 돼?
A. 아니다. API 실패는 Error State로 처리해야 한다.

Q. 필터 초기화 버튼은 언제 제공해?
A. 검색 조건이나 필터 때문에 결과가 없을 가능성이 있을 때 제공하면 좋다.

Q. Filter Empty State는 뭐야?
A. 특정 필터 조건에 맞는 데이터가 없을 때 표시하는 Empty State다.

Q. 필터 결과가 없을 때 무엇을 제공해야 해?
A. 필터 초기화, 조건 완화, 다른 조건 선택 같은 다음 행동을 제공하는 것이 좋다.

Q. 필터 변경 중 Empty State가 잠깐 보여도 돼?
A. 권장하지 않는다. 필터 요청 중에는 Loading 또는 Refetch Indicator를 보여주는 것이 좋다.

Q. 필터 변경 시 페이지 번호는 어떻게 해?
A. 보통 1페이지로 초기화하는 것이 안전하다.

Q. Empty State 문구는 어떻게 쓰면 좋아?
A. 현재 상태, 이유, 다음 행동을 짧고 명확하게 작성하는 것이 좋다.

Q. Empty State에 항상 버튼이 필요해?
A. 아니다. 사용자가 할 다음 행동이 명확할 때만 CTA를 제공하면 된다.

Q. “데이터 없음”만 써도 돼?
A. 권장하지 않는다. 사용자가 다음에 무엇을 할 수 있는지 알기 어렵다.

Q. Empty Message에서 피해야 할 표현은?
A. 사용자를 탓하는 문구, 오류처럼 보이는 문구, 너무 기술적인 표현을 피해야 한다.

Q. Empty CTA는 뭐야?
A. Empty State에서 사용자가 다음 행동을 수행하도록 제공하는 버튼이나 링크다.

Q. Empty State의 “다시 시도” 버튼은 적절해?
A. 요청 성공 후 데이터가 없는 Empty State라면 보통 필터 초기화나 탐색 CTA가 더 적합하다. 다시 시도는 Error State에 더 적합하다.

Q. CTA는 몇 개가 적당해?
A. 보통 하나가 가장 좋고, 필요하면 Primary와 Secondary 두 개 정도로 제한하는 것이 좋다.

Q. EmptyState는 공통 컴포넌트로 만들 수 있어?
A. 가능하다. title, description, action을 props로 받으면 여러 화면에서 재사용할 수 있다.

Q. EmptyState와 ErrorState를 하나로 합쳐도 돼?
A. 권장하지 않는다. 데이터 없음과 요청 실패는 의미와 사용자 행동이 다르기 때문에 분리하는 것이 좋다.

Q. EmptyState에 action slot이 필요한 이유는?
A. 화면별로 필터 초기화, 생성, 탐색 같은 다른 액션을 전달하기 위해 필요하다.

Q. EmptyState 문구를 컴포넌트 안에 하드코딩해도 돼?
A. 권장하지 않는다. 화면 문맥에 맞는 메시지를 props로 전달하는 것이 좋다.

Q. Empty State는 조건부 렌더링에서 언제 검사해?
A. Loading과 Error를 먼저 검사한 뒤 요청 성공 상태에서 데이터가 없을 때 검사한다.

Q. 초기 빈 배열 때문에 Empty가 먼저 보여?
A. Loading보다 Empty를 먼저 검사했거나 요청 완료 여부를 구분하지 않았을 가능성이 있다.

Q. data가 undefined면 Empty State야?
A. 항상 아니다. 요청 전, 로딩 중, 오류 상태일 수 있으므로 상태값과 함께 판단해야 한다.

Q. API 실패를 빈 배열로 변환하면 안 되는 이유는?
A. 실패 상태가 사라져 Error State를 보여줄 수 없기 때문이다.

Q. Success Feedback은 뭐야?
A. 사용자 요청이 성공적으로 처리되었음을 알려주는 UX다.

Q. 성공할 때마다 Toast를 띄워야 해?
A. 아니다. 화면 변화만으로 충분한 경우도 있고 중요한 액션에는 Toast가 도움이 된다.

Q. Success Feedback에서 가장 중요한 것은?
A. 사용자가 요청 결과를 인지하고 화면 상태가 서버 상태와 동기화되는 것이다.

Q. 성공 후 데이터를 다시 불러와야 해?
A. 관련 화면이 서버 상태에 의존한다면 refetch 또는 query invalidate를 고려해야 한다.

Q. Toast Success는 언제 쓰면 좋아?
A. 저장, 삭제, 등록, 업로드처럼 짧게 성공을 알려도 되는 액션에 적합하다.

Q. 좋아요 성공마다 Toast를 띄워야 해?
A. 보통은 필요 없다. 버튼 상태 변화만으로 충분한 경우가 많다.

Q. Toast만 띄우면 성공 처리가 끝난 거야?
A. 아니다. 관련 데이터 갱신, 버튼 상태 복구, 화면 전환 등 필요한 처리를 함께 해야 한다.

Q. 중요한 성공 정보도 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 중요한 정보는 화면에 남는 방식으로 보여주는 것이 좋다.

Q. Inline Success Message는 언제 써?
A. Form이나 설정 화면처럼 특정 영역의 성공 결과를 화면 안에서 보여줄 때 적합하다.

Q. Toast와 Inline Success를 같이 써도 돼?
A. 가능하지만 중복 알림이 과하면 불필요하므로 하나를 선택하는 것이 좋다.

Q. Inline Success는 어디에 보여줘?
A. 성공한 Form 상단, Submit Button 근처, 또는 관련 섹션 안에 보여주는 것이 좋다.

Q. 저장 성공 후 바로 이동해도 돼?
A. 가능하다. 다만 사용자가 성공 여부를 이해할 수 있도록 메시지나 자연스러운 화면 전환을 제공하는 것이 좋다.

Q. 생성 성공 후 어디로 이동하는 게 좋아?
A. 생성된 리소스의 상세 페이지나 목록 페이지로 이동하는 것이 일반적이다.

Q. 삭제 성공 후 현재 상세 페이지에 남아도 돼?
A. 삭제된 리소스의 상세 페이지에 남는 것은 혼란스러울 수 있으므로 목록 이동이 자연스럽다.

Q. 결제 성공은 Toast로 충분해?
A. 보통은 결제 완료 페이지처럼 화면에 남는 확인 UX가 더 적합하다.

Q. 성공 후 Query Invalidation은 왜 필요해?
A. 서버 상태가 바뀐 뒤 화면의 캐시 데이터도 최신 상태로 동기화해야 하기 때문이다.

Q. 어떤 Query를 invalidate해야 해?
A. Mutation이 영향을 주는 목록, 상세, 카운트, 요약 데이터를 기준으로 결정한다.

Q. queryKey가 틀리면 어떻게 돼?
A. invalidate가 제대로 동작하지 않아 화면이 오래된 데이터를 계속 보여줄 수 있다.

Q. Optimistic UI는 뭐야?
A. 서버 응답을 기다리기 전에 UI를 먼저 성공한 것처럼 갱신하는 방식이다.

Q. Optimistic UI는 언제 쓰면 좋아?
A. 좋아요, 찜, 팔로우처럼 즉각 반응이 중요하고 되돌리기 쉬운 액션에 적합하다.

Q. Optimistic UI 실패 시 어떻게 해?
A. 이전 상태로 rollback하고 오류 메시지를 보여준 뒤 서버 상태를 다시 조회하는 것이 좋다.

Q. 결제에도 Optimistic UI를 써도 돼?
A. 권장하지 않는다. 결제는 처리 여부 확인이 중요하므로 서버 결과를 기준으로 UX를 구성해야 한다.

Q. Success Message는 어떻게 쓰면 좋아?
A. 무엇이 성공했는지 짧고 명확하게 작성하는 것이 좋다.

Q. Success Toast 문구는 길어도 돼?
A. 권장하지 않는다. Toast는 짧은 문구가 적합하다.

Q. 성공 메시지에 다음 행동을 넣어도 돼?
A. 이메일 인증처럼 추가 행동이 필요한 경우에는 넣는 것이 좋다.

Q. Empty State에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 데이터가 없는 상태와 다음 행동을 이해할 수 있어야 한다.

Q. Empty State CTA는 button이 좋아 link가 좋아?
A. 화면 내 동작이면 button, 다른 페이지 이동이면 link가 적합하다.

Q. Success Message에도 접근성이 필요해?
A. 필요하다. 보조 기술 사용자도 요청이 성공했음을 인지할 수 있어야 한다.

Q. Inline Success에는 어떤 role이 좋아?
A. 일반적인 성공 알림에는 role status와 aria-live polite를 고려할 수 있다.

Q. Empty State가 잠깐 보였다가 목록이 보여?
A. 요청 완료 전 빈 배열을 Empty로 판정했을 가능성이 있다.

Q. Empty Flicker를 막으려면?
A. Loading과 Error를 먼저 검사하고 요청 성공 후에만 Empty를 표시해야 한다.

Q. 성공 Toast는 있는데 목록이 그대로야?
A. Query Invalidation 또는 cache update가 누락되었을 가능성이 높다.

Q. 성공 후 버튼이 계속 disabled야?
A. pending 상태가 정상적으로 종료되는지, mutation 상태를 올바르게 사용하는지 확인해야 한다.

Q. Empty State 검수에서 가장 중요한 것은?
A. 요청 성공 후 데이터 없음 상태인지 확인하고 Error State와 혼동하지 않는 것이다.

Q. Success Feedback 검수에서 가장 중요한 것은?
A. 사용자가 성공 결과를 인지하고 화면 데이터가 서버 상태와 동기화되는지 확인하는 것이다.

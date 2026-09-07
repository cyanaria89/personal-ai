# UI Component Pattern Part05 - List Table Navigation

---

# 1. List Table Navigation Overview

## 1.1 List Table Navigation Purpose

### [개념]

List Table Navigation UI는 여러 데이터를 반복 표시하거나, 사용자가 화면 안에서 정보를 탐색하고 선택하도록 돕는 UI Component Pattern이다.

이 문서는 List, Table, Pagination, Tab, Dropdown, Accordion 같은 UI Component를 Frontend Agent가 일관되게 설계하고 Review Agent가 검토할 수 있도록 만드는 RAG 문서다.

List Table Navigation UI는 데이터 렌더링, empty state, loading state, key, semantic HTML, 접근성, 사용자 탐색 흐름을 함께 고려해야 한다.

---

### [핵심]

List Table Navigation 핵심 대상:

- List Component
- List Item Component
- Table Component
- Pagination Component
- Tab Component
- Dropdown Component
- Accordion Component

핵심 기준:

- 반복 데이터는 안정적인 key 사용
- index key 지양
- EmptyState 포함
- LoadingState / ErrorState 연결
- semantic HTML 우선
- List와 Item 책임 분리
- Table은 실제 표 데이터에 사용
- Tab은 같은 화면 내부 패널 전환에 사용
- Route는 페이지 수준 이동에 사용
- Dropdown은 메뉴 액션 또는 선택 UI에 사용
- Select와 Dropdown 구분
- Accordion은 접힘 / 펼침 상태 관리
- 접근성 role과 aria 속성 고려

---

### [실무]

2026 실무 기준에서 List Table Navigation UI는 데이터 표시만 하는 단순 Component가 아니다.

Frontend Agent는 데이터 상태와 사용자 탐색 흐름을 함께 설계해야 한다.

```text
Data Request
→ Loading State
→ Error State
→ Empty State
→ Data Rendering
→ List / Table / Navigation UI
→ Interaction
→ Accessibility Review
```

Component 책임 분리:

```text
Page Component
→ API 호출, server state, filter state, pagination state

List / Table Component
→ 데이터 렌더링 구조

Item / Row Component
→ 개별 데이터 표시

Navigation UI
→ tab, dropdown, pagination, accordion 상호작용

State UI
→ LoadingState, ErrorState, EmptyState
```

---

### [FAQ]

Q. List Table Navigation 문서는 왜 필요해?
A. Frontend Agent가 목록, 표, 탭, 드롭다운 같은 반복 UI와 탐색 UI를 일관되게 설계하고 접근성 문제를 줄이기 위해 필요하다.

Q. List와 Table은 어떻게 구분해?
A. 단순 카드나 항목 반복은 List가 적합하고, 행과 열로 비교하는 표 데이터는 Table이 적합하다.

Q. Navigation UI에서 가장 중요한 기준은 뭐야?
A. 사용자가 현재 위치와 선택 상태를 이해할 수 있어야 하고, keyboard 접근성과 aria 상태가 제공되어야 한다.

---

# 2. List Component Pattern

## 2.1 List Component Responsibility

### [개념]

List Component는 여러 데이터를 반복 렌더링하는 UI Pattern이다.

List Component는 items를 받아 반복 구조를 만들고, 개별 데이터 표현은 Item Component에 위임하는 것이 좋다.

List Component는 key, empty state, loading state, semantic list 구조를 함께 고려해야 한다.

---

### [핵심]

List 기본 책임:

- items 반복 렌더링
- stable key 사용
- empty state 표시
- item component 조합
- list semantics 제공
- loading / error 상태와 연결
- infinite scroll 또는 pagination 기준 분리
- item click 이벤트 전달 가능

List 필수 고려:

- items
- key
- item component
- EmptyState
- LoadingState
- ErrorState
- ul / ol / li
- map
- unique id
- pagination
- infinite scroll

주의:

- index key 지양
- 빈 목록을 아무것도 표시하지 않는 방식 지양
- List 내부에서 API 직접 호출 지양
- List가 너무 많은 도메인 로직을 갖지 않도록 주의
- Item Component와 List Component 책임 분리

---

### [실무]

기본 List 예:

```tsx
type FestivalListProps = {
  festivals: Festival[];
};

function FestivalList({ festivals }: FestivalListProps) {
  if (festivals.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
  }

  return (
    <ul className="festival-list">
      {festivals.map((festival) => (
        <li key={festival.festivalId}>
          <FestivalCard festival={festival} />
        </li>
      ))}
    </ul>
  );
}
```

Common List 구조 예:

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  renderItem: (item: T) => React.ReactNode;
  emptyState?: React.ReactNode;
};

function List<T>({ items, getKey, renderItem, emptyState }: ListProps<T>) {
  if (items.length === 0) {
    return <>{emptyState ?? <EmptyState title="표시할 항목이 없습니다." />}</>;
  }

  return (
    <ul>
      {items.map((item) => (
        <li key={getKey(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

Feature 사용 예:

```tsx
<List
  items={festivals}
  getKey={(festival) => festival.festivalId}
  renderItem={(festival) => <FestivalCard festival={festival} />}
  emptyState={<EmptyState title="검색 결과가 없습니다." />}
/>
```

---

### [FAQ]

Q. List key로 index를 써도 돼?
A. 정렬, 추가, 삭제가 있는 목록에서는 index key를 지양하고 고유 id를 사용하는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. EmptyState를 보여주는 것이 사용자 경험에 좋다.

Q. List Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. API 호출은 Page Component나 Custom Hook에서 처리하고 List는 렌더링에 집중하는 것이 좋다.

---

## 2.2 List Item Component Pattern

### [개념]

List Item Component는 List 안에서 반복되는 개별 항목 UI다.

List Item은 하나의 데이터 항목을 표시하고, 클릭 / 선택 / 액션 같은 사용자 상호작용을 외부로 전달한다.

---

### [핵심]

List Item 기본 책임:

- 개별 항목 표시
- item data 표시
- item action 제공
- selected 상태 표현 가능
- disabled 상태 표현 가능
- onClick / onSelect 이벤트 전달
- 접근 가능한 interactive element 사용
- leftArea / rightArea 조합 가능

List Item 사용 대상:

- NotificationItem
- ChatMessageItem
- SearchResultItem
- MenuItem
- UserListItem
- FestivalListItem
- ReviewListItem

주의:

- div onClick 남용 금지
- 이동이면 Link / anchor 사용
- 액션이면 button 사용
- Item 내부 API 호출은 Feature 성격이면 가능하지만 Hook 분리 권장
- 공통 ListItem에 도메인 필드 직접 포함 금지

---

### [실무]

Common ListItem 예:

```tsx
type ListItemProps = {
  selected?: boolean;
  disabled?: boolean;
  leftArea?: React.ReactNode;
  rightArea?: React.ReactNode;
  onClick?: () => void;
  children: React.ReactNode;
};

function ListItem({
  selected = false,
  disabled = false,
  leftArea,
  rightArea,
  onClick,
  children,
}: ListItemProps) {
  if (onClick) {
    return (
      <button
        type="button"
        className="list-item"
        aria-selected={selected}
        disabled={disabled}
        onClick={onClick}
      >
        {leftArea}
        <span className="list-item-content">{children}</span>
        {rightArea}
      </button>
    );
  }

  return (
    <div className="list-item" aria-selected={selected}>
      {leftArea}
      <span className="list-item-content">{children}</span>
      {rightArea}
    </div>
  );
}
```

Feature Item 예:

```tsx
function NotificationItem({ notification }: { notification: Notification }) {
  return (
    <ListItem
      selected={!notification.read}
      rightArea={<Badge>{notification.type}</Badge>}
    >
      <strong>{notification.title}</strong>
      <p>{notification.message}</p>
    </ListItem>
  );
}
```

Link Item 예:

```tsx
function FestivalSearchResultItem({ festival }: { festival: Festival }) {
  return (
    <li>
      <Link to={`/festivals/${festival.festivalId}`}>
        <h3>{festival.title}</h3>
        <p>{festival.regionName}</p>
      </Link>
    </li>
  );
}
```

---

### [FAQ]

Q. 클릭 가능한 List Item은 div에 onClick을 붙이면 돼?
A. 권장하지 않는다. 페이지 이동이면 Link나 anchor, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. ListItem에 leftArea, rightArea를 둬도 돼?
A. 가능하다. 아이콘, badge, action처럼 위치가 명확한 UI를 넣을 때 유용하다.

Q. NotificationItem은 Common UI야 Feature UI야?
A. notification 데이터 구조에 의존하므로 보통 Feature UI다.

---

# 3. Table Component Pattern

## 3.1 Table Component Responsibility

### [개념]

Table Component는 행과 열 구조의 데이터를 표현하는 UI Pattern이다.

Table은 데이터 비교, 관리자 목록, 통계 화면, 정렬 가능한 목록처럼 column 구조가 중요한 화면에 적합하다.

Table은 semantic table 요소와 caption, th scope, empty row, pagination 관계를 함께 고려해야 한다.

---

### [핵심]

Table 기본 책임:

- table 구조 제공
- caption 제공
- thead / tbody 구성
- th / td 사용
- row key 사용
- empty state 처리
- column 정의 가능
- row action 제공 가능
- sorting 상태 연결 가능
- pagination과 연동 가능
- responsive 기준 필요

Table 필수 요소:

- table
- caption
- thead
- tbody
- th
- td
- scope
- row key
- empty row
- sorting
- pagination

주의:

- 표 형태 데이터는 div보다 table 사용
- caption 누락 주의
- th scope 누락 주의
- row key로 index 지양
- 복잡한 responsive table 기준 필요
- Table 내부 API 호출 지양

---

### [실무]

기본 Table 예:

```tsx
function UserTable({ users }: { users: User[] }) {
  if (users.length === 0) {
    return <EmptyState title="사용자 목록이 없습니다." />;
  }

  return (
    <table>
      <caption>사용자 목록</caption>
      <thead>
        <tr>
          <th scope="col">닉네임</th>
          <th scope="col">권한</th>
          <th scope="col">가입일</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user) => (
          <tr key={user.userId}>
            <td>{user.nickname}</td>
            <td>{user.role}</td>
            <td>{user.createdAt}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

Column 기반 Table 예:

```tsx
type Column<T> = {
  key: string;
  header: string;
  render: (item: T) => React.ReactNode;
};

type DataTableProps<T> = {
  caption: string;
  rows: T[];
  columns: Column<T>[];
  getRowKey: (row: T) => string | number;
};

function DataTable<T>({
  caption,
  rows,
  columns,
  getRowKey,
}: DataTableProps<T>) {
  if (rows.length === 0) {
    return <EmptyState title="표시할 데이터가 없습니다." />;
  }

  return (
    <table>
      <caption>{caption}</caption>
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key} scope="col">
              {column.header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => (
          <tr key={getRowKey(row)}>
            {columns.map((column) => (
              <td key={column.key}>{column.render(row)}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

---

### [FAQ]

Q. Table 대신 div로 만들어도 돼?
A. 표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. Table에 caption이 꼭 필요해?
A. 권장한다. 특히 복잡한 표에서는 표의 목적을 설명하는 데 도움이 된다.

Q. Table row key로 index를 써도 돼?
A. 정렬, 추가, 삭제가 가능하면 index key를 지양하고 고유 id를 사용하는 것이 좋다.

---

## 3.2 Table Sorting and Action Pattern

### [개념]

Table Sorting and Action Pattern은 Table에서 정렬, 상세 보기, 수정, 삭제 같은 상호작용을 처리하는 기준이다.

Table은 데이터 구조를 표시하고, 정렬 상태와 row action은 Props나 상위 Component에서 관리하는 것이 좋다.

---

### [핵심]

Sorting 기준:

- sortKey
- sortDirection
- onSort
- sortable column
- aria-sort
- button inside th
- server sorting / client sorting 구분

Row Action 기준:

- action column 제공
- button 또는 Link 사용
- icon button은 aria-label 필요
- destructive action은 ConfirmDialog 연결
- API 호출은 Feature Hook 또는 Page에서 처리

주의:

- th 자체에 onClick만 붙이지 않음
- 정렬 가능한 column은 button으로 명확히 제공
- aria-sort 상태 제공
- 삭제 액션은 즉시 실행 지양
- row 전체 click과 내부 button 충돌 주의

---

### [실무]

정렬 Header 예:

```tsx
type SortDirection = "asc" | "desc";

type SortableHeaderProps = {
  label: string;
  sortDirection?: SortDirection;
  onSort: () => void;
};

function SortableHeader({ label, sortDirection, onSort }: SortableHeaderProps) {
  return (
    <th
      scope="col"
      aria-sort={
        sortDirection === "asc"
          ? "ascending"
          : sortDirection === "desc"
            ? "descending"
            : "none"
      }
    >
      <button type="button" onClick={onSort}>
        {label}
      </button>
    </th>
  );
}
```

Action Cell 예:

```tsx
function UserActionCell({ user }: { user: User }) {
  return (
    <td>
      <Button variant="secondary">상세</Button>
      <Button variant="danger">삭제</Button>
    </td>
  );
}
```

삭제 Confirm 연결 예:

```tsx
function DeleteUserAction({ userId }: { userId: number }) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <Button variant="danger" onClick={() => setOpen(true)}>
        삭제
      </Button>

      <ConfirmDialog
        open={open}
        title="사용자를 삭제할까요?"
        description="삭제한 사용자는 복구할 수 없습니다."
        confirmText="삭제"
        variant="danger"
        onConfirm={() => deleteUser(userId)}
        onCancel={() => setOpen(false)}
      />
    </>
  );
}
```

---

### [FAQ]

Q. Table 정렬은 th에 onClick을 붙이면 돼?
A. 권장하지 않는다. 정렬 가능한 헤더 내부에 button을 두고 aria-sort로 정렬 상태를 제공하는 것이 좋다.

Q. Table에서 삭제 버튼을 바로 실행해도 돼?
A. 중요한 데이터 삭제는 ConfirmDialog를 연결하는 것이 안전하다.

Q. Table sorting은 Table Component가 직접 처리해야 해?
A. 단순 client sorting은 가능하지만 server sorting이나 filter 연동은 Page 또는 Feature Hook에서 관리하는 것이 좋다.

---

# 4. Pagination Component Pattern

## 4.1 Pagination Component Responsibility

### [개념]

Pagination Component는 여러 페이지로 나뉜 데이터를 사용자가 이동할 수 있게 하는 Navigation UI Component다.

Pagination은 현재 페이지, 전체 페이지, 이전 / 다음 이동, 페이지 번호 이동, disabled 상태, 접근성을 고려해야 한다.

---

### [핵심]

Pagination 기본 책임:

- currentPage 표시
- totalPages 표시
- previous / next 버튼 제공
- page number 버튼 제공
- disabled 상태 처리
- onPageChange 이벤트 전달
- aria-current 제공
- nav 영역 제공
- page size 변경은 별도 Component 가능

필수 Props:

- currentPage
- totalPages
- onPageChange
- siblingCount
- disabled

주의:

- API 호출 직접 포함 금지
- page index 기준 0-based / 1-based 통일
- currentPage 범위 검증
- totalPages가 1이면 숨김 여부 기준 필요
- 무한 스크롤과 Pagination 구분

---

### [실무]

Pagination 예:

```tsx
type PaginationProps = {
  currentPage: number;
  totalPages: number;
  disabled?: boolean;
  onPageChange: (page: number) => void;
};

function Pagination({
  currentPage,
  totalPages,
  disabled = false,
  onPageChange,
}: PaginationProps) {
  if (totalPages <= 1) {
    return null;
  }

  const pages = Array.from({ length: totalPages }, (_, index) => index + 1);

  return (
    <nav aria-label="페이지 이동">
      <button
        type="button"
        disabled={disabled || currentPage <= 1}
        onClick={() => onPageChange(currentPage - 1)}
      >
        이전
      </button>

      {pages.map((page) => (
        <button
          key={page}
          type="button"
          aria-current={page === currentPage ? "page" : undefined}
          disabled={disabled}
          onClick={() => onPageChange(page)}
        >
          {page}
        </button>
      ))}

      <button
        type="button"
        disabled={disabled || currentPage >= totalPages}
        onClick={() => onPageChange(currentPage + 1)}
      >
        다음
      </button>
    </nav>
  );
}
```

Page 사용 예:

```tsx
function FestivalListPage() {
  const [page, setPage] = useState(1);
  const { data } = useFestivals({ page });

  return (
    <>
      <FestivalList festivals={data.items} />
      <Pagination
        currentPage={page}
        totalPages={data.totalPages}
        onPageChange={setPage}
      />
    </>
  );
}
```

---

### [FAQ]

Q. Pagination 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Pagination은 onPageChange만 전달하고 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

Q. currentPage는 0부터 시작하는 게 좋아 1부터 시작하는 게 좋아?
A. 프로젝트 기준으로 통일해야 한다. UI 표시에는 보통 1-based가 자연스럽다.

Q. totalPages가 1이면 Pagination을 보여줘야 해?
A. 보통 숨기는 것이 자연스럽지만 프로젝트 UX 기준에 따라 결정할 수 있다.

---

# 5. Tab Component Pattern

## 5.1 Tab Component Responsibility

### [개념]

Tab Component는 같은 화면 영역 안에서 여러 패널을 전환하는 Navigation UI Pattern이다.

Tab은 선택 상태, tablist, tab, tabpanel, keyboard navigation, aria-selected 같은 접근성 기준을 함께 고려해야 한다.

---

### [핵심]

Tab 기본 책임:

- selected tab 상태 표시
- tab list 제공
- tab trigger 제공
- tab panel 제공
- value 기반 선택
- onChange 이벤트 전달
- aria-selected 제공
- role tablist / tab / tabpanel 고려
- URL state 여부 판단
- keyboard navigation 고려

Tab 사용 기준:

- 같은 페이지 내부 패널 전환
- 정보 / 리뷰 / 지도 같은 상세 화면 섹션 전환
- route 수준 이동이 아닌 UI 내부 전환
- 새로고침 유지 필요 시 URL State 검토

---

### [실무]

기본 Tab 예:

```tsx
type TabValue = "info" | "review" | "map";

function FestivalTabs() {
  const [selectedTab, setSelectedTab] = useState<TabValue>("info");

  return (
    <section>
      <div role="tablist" aria-label="축제 상세 정보">
        <button
          type="button"
          role="tab"
          aria-selected={selectedTab === "info"}
          onClick={() => setSelectedTab("info")}
        >
          정보
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={selectedTab === "review"}
          onClick={() => setSelectedTab("review")}
        >
          리뷰
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={selectedTab === "map"}
          onClick={() => setSelectedTab("map")}
        >
          지도
        </button>
      </div>

      {selectedTab === "info" && <div role="tabpanel">축제 정보</div>}

      {selectedTab === "review" && <div role="tabpanel">리뷰 목록</div>}

      {selectedTab === "map" && <div role="tabpanel">지도</div>}
    </section>
  );
}
```

Controlled Tab 예:

```tsx
type TabsProps<T extends string> = {
  value: T;
  options: { label: string; value: T }[];
  onChange: (value: T) => void;
};

function Tabs<T extends string>({ value, options, onChange }: TabsProps<T>) {
  return (
    <div role="tablist">
      {options.map((option) => (
        <button
          key={option.value}
          type="button"
          role="tab"
          aria-selected={value === option.value}
          onClick={() => onChange(option.value)}
        >
          {option.label}
        </button>
      ))}
    </div>
  );
}
```

---

### [FAQ]

Q. Tab 상태는 Local State로 둬도 돼?
A. 해당 화면 내부에서만 필요하면 Local State로 충분하다. 공유나 새로고침 유지가 필요하면 URL State를 검토한다.

Q. Tab과 Route는 어떻게 구분해?
A. 페이지 수준 이동이면 Route, 같은 페이지 내부 패널 전환이면 Tab이 적합하다.

Q. Tab에 role을 꼭 넣어야 해?
A. 접근성을 고려하면 role tablist, tab, tabpanel과 aria-selected를 함께 제공하는 것이 좋다.

---

## 5.2 Tab vs Route

### [개념]

Tab vs Route는 화면 내부 상태 전환과 페이지 수준 이동을 구분하는 기준이다.

Tab은 같은 화면 안에서 콘텐츠 패널을 바꾸는 UI이고, Route는 URL 기반 페이지 이동이다.

---

### [핵심]

Tab이 적합한 경우:

- 같은 페이지 내부 섹션 전환
- 정보 / 리뷰 / 지도 패널 전환
- 화면 맥락 유지
- 데이터 일부만 전환
- route 분리 필요 없음

Route가 적합한 경우:

- 별도 페이지
- URL 공유 필요
- 브라우저 뒤로가기 의미 중요
- 권한 / layout / data loading이 다름
- SEO나 deep link 필요

비교:

| 기준      | Tab                 | Route                      |
| --------- | ------------------- | -------------------------- |
| 목적      | 내부 패널 전환      | 페이지 이동                |
| URL       | 선택적              | 필수                       |
| 상태      | Local / URL State   | Router State               |
| 예        | 상세 정보 / 리뷰 탭 | /login, /users, /festivals |
| 뒤로가기  | 선택적              | 기본 동작                  |
| Component | Tabs                | React Router               |

---

### [실무]

Tab 적합 예:

```text
FestivalDetailPage
→ Info Tab
→ Review Tab
→ Map Tab
```

Route 적합 예:

```text
/festivals
/festivals/:festivalId
/festivals/:festivalId/reviews
/login
/my-page
```

URL State Tab 예:

```text
/festivals/10?tab=review
```

권장:

- 사용자가 링크 공유해야 하면 URL State 검토
- 페이지 수준이면 Route 사용
- 같은 화면 내부 전환이면 Tab 사용
- Tab 선택이 중요한 검색 조건이면 query parameter 검토

---

### [FAQ]

Q. 상세 페이지의 정보 / 리뷰 / 지도는 Tab이 좋아 Route가 좋아?
A. 같은 페이지 내부 패널 전환이면 Tab이 적합하고, 각 패널을 직접 공유해야 하면 query parameter나 nested route를 검토한다.

Q. Tab 선택을 새로고침 후에도 유지하려면?
A. URL query parameter나 storage state를 사용할 수 있다. 공유가 필요하면 URL State가 더 적합하다.

Q. 모든 화면 전환을 Tab으로 처리해도 돼?
A. 아니다. 페이지 수준 이동은 Route로 처리하는 것이 좋다.

---

# 6. Dropdown Component Pattern

## 6.1 Dropdown Component Responsibility

### [개념]

Dropdown Component는 trigger를 기준으로 메뉴나 선택지를 펼쳐 보여주는 Navigation UI Pattern이다.

Dropdown은 open 상태, trigger, menu, item, onSelect, onClose, keyboard navigation, aria-expanded를 함께 고려해야 한다.

---

### [핵심]

Dropdown 기본 책임:

- open state 관리
- trigger 제공
- menu 표시
- item 렌더링
- onSelect 이벤트 전달
- 선택 후 닫기
- outside click 고려
- ESC 닫기 고려
- aria-haspopup 제공
- aria-expanded 제공
- keyboard navigation 고려

Dropdown 사용 대상:

- menu action
- profile menu
- sort menu
- filter menu
- context action
- more action
- custom select basics

주의:

- Select와 Dropdown 구분
- Form 값 선택은 native select 우선 고려
- 중요한 액션은 ConfirmDialog 연결 가능
- 접근성 구현 난도 있음
- 복잡하면 Headless UI 라이브러리 검토 가능

---

### [실무]

Dropdown 예:

```tsx
type DropdownItem = {
  label: string;
  value: string;
  disabled?: boolean;
};

type DropdownProps = {
  label: string;
  items: DropdownItem[];
  onSelect: (value: string) => void;
};

function Dropdown({ label, items, onSelect }: DropdownProps) {
  const [open, setOpen] = useState(false);

  function handleSelect(value: string) {
    onSelect(value);
    setOpen(false);
  }

  return (
    <div className="dropdown">
      <button
        type="button"
        aria-haspopup="menu"
        aria-expanded={open}
        onClick={() => setOpen((prev) => !prev)}
      >
        {label}
      </button>

      {open && (
        <ul role="menu">
          {items.map((item) => (
            <li key={item.value}>
              <button
                type="button"
                role="menuitem"
                disabled={item.disabled}
                onClick={() => handleSelect(item.value)}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

Profile Menu 예:

```tsx
<Dropdown
  label="내 메뉴"
  items={[
    { label: "마이페이지", value: "my-page" },
    { label: "로그아웃", value: "logout" },
  ]}
  onSelect={handleProfileMenu}
/>
```

---

### [FAQ]

Q. Dropdown은 그냥 div로 열고 닫으면 돼?
A. 시각적으로는 가능하지만 키보드 접근성, aria-expanded, 닫기 동작을 고려해야 한다.

Q. Select와 Dropdown은 같아?
A. 다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

Q. Dropdown이 복잡해지면 어떻게 해?
A. keyboard navigation과 focus 관리가 복잡하면 Headless UI 라이브러리 사용을 검토할 수 있다.

---

## 6.2 Dropdown vs Select

### [개념]

Dropdown vs Select는 메뉴 액션 UI와 Form 값 선택 UI를 구분하는 기준이다.

Dropdown은 주로 액션 메뉴나 사용자 메뉴에 적합하고, Select는 Form 입력값 선택에 적합하다.

---

### [핵심]

Dropdown 적합:

- 메뉴 액션
- 프로필 메뉴
- 더보기 메뉴
- 정렬 메뉴
- 필터 메뉴
- 컨텍스트 액션
- 링크 / 버튼 혼합 메뉴

Select 적합:

- Form field
- 하나의 값 선택
- native input 제출
- label / error 연결
- required 검증
- 접근성 기본 제공

비교:

| 기준      | Dropdown       | Select           |
| --------- | -------------- | ---------------- |
| 목적      | 메뉴 / 액션    | Form 값 선택     |
| 요소      | button + menu  | select           |
| 값 제출   | 직접 처리      | Form과 자연 연결 |
| 접근성    | 구현 난도 높음 | native 지원      |
| 예        | 프로필 메뉴    | 지역 선택        |
| 오류 표시 | 직접 설계      | FormField와 연결 |

---

### [실무]

Select 적합 예:

```tsx
<Select
  id="region"
  label="지역"
  value={region}
  options={regionOptions}
  onChange={setRegion}
/>
```

Dropdown 적합 예:

```tsx
<Dropdown
  label="더보기"
  items={[
    { label: "수정", value: "edit" },
    { label: "삭제", value: "delete" },
  ]}
  onSelect={handleAction}
/>
```

판단 Flow:

```text
Form 값 선택인가?
→ Select

메뉴 액션인가?
→ Dropdown

복잡한 custom select인가?
→ 접근성 구현 가능성 검토
→ 필요 시 Headless UI 검토
```

---

### [FAQ]

Q. 지역 선택 필터는 Select야 Dropdown이야?
A. Form 값 선택 성격이 강하면 Select가 적합하고, 복잡한 필터 메뉴라면 Dropdown이나 FilterBar를 검토할 수 있다.

Q. 더보기 메뉴는 Select로 만들어도 돼?
A. 권장하지 않는다. 수정, 삭제 같은 액션 메뉴는 Dropdown Menu가 더 적합하다.

Q. custom select를 직접 만들면 안 돼?
A. 가능하지만 keyboard navigation, focus 관리, aria 속성 구현이 필요하므로 복잡하면 검증된 라이브러리를 검토한다.

---

# 7. Accordion Component Pattern

## 7.1 Accordion Component Responsibility

### [개념]

Accordion Component는 제목 영역을 클릭해 관련 콘텐츠를 펼치거나 접는 UI Pattern이다.

Accordion은 open 상태, trigger, panel, aria-expanded, aria-controls를 함께 고려해야 한다.

---

### [핵심]

Accordion 기본 책임:

- item 목록 표시
- open state 관리
- trigger 제공
- panel 표시
- single open / multiple open 기준
- aria-expanded 제공
- aria-controls 연결
- keyboard navigation 고려
- content unmount 여부 기준

사용 대상:

- FAQ
- 설정 섹션
- 필터 그룹
- 상세 정보 접힘 영역
- 모바일 UI 섹션

주의:

- 중요한 정보를 지나치게 숨기지 않음
- trigger는 button 사용
- 제목과 panel 연결 필요
- animation만으로 상태 전달 금지
- SEO / 접근성 요구 확인

---

### [실무]

Accordion 예:

```tsx
type AccordionItem = {
  id: string;
  title: string;
  content: React.ReactNode;
};

type AccordionProps = {
  items: AccordionItem[];
};

function Accordion({ items }: AccordionProps) {
  const [openId, setOpenId] = useState<string | null>(null);

  function toggle(id: string) {
    setOpenId((prev) => (prev === id ? null : id));
  }

  return (
    <div className="accordion">
      {items.map((item) => {
        const open = openId === item.id;
        const panelId = `${item.id}-panel`;

        return (
          <section key={item.id}>
            <h3>
              <button
                type="button"
                aria-expanded={open}
                aria-controls={panelId}
                onClick={() => toggle(item.id)}
              >
                {item.title}
              </button>
            </h3>

            {open && <div id={panelId}>{item.content}</div>}
          </section>
        );
      })}
    </div>
  );
}
```

FAQ Accordion 예:

```tsx
<Accordion
  items={[
    {
      id: "q1",
      title: "환불은 어떻게 하나요?",
      content: <p>마이페이지 결제 내역에서 환불 요청할 수 있습니다.</p>,
    },
  ]}
/>
```

---

### [FAQ]

Q. Accordion trigger는 div로 만들어도 돼?
A. 권장하지 않는다. 펼침 / 접힘 액션은 button을 사용하는 것이 접근성에 좋다.

Q. Accordion에는 aria-expanded가 필요해?
A. 필요하다. 현재 패널이 열려 있는지 보조기술에 전달할 수 있다.

Q. FAQ는 Accordion으로 만들어도 돼?
A. 가능하다. 단 중요한 안내를 숨기지 않도록 UX 기준을 함께 고려해야 한다.

---

# 8. List Table Navigation Checklist

## 8.1 Review Checklist

### [개념]

List Table Navigation Checklist는 반복 데이터 UI와 탐색 UI가 적절히 설계되었는지 검수하는 기준이다.

Frontend Agent와 Review Agent는 List, Table, Pagination, Tab, Dropdown, Accordion 생성 후 이 체크리스트로 치명적 문제를 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] List에 안정적인 key를 사용했는가?
- [ ] index key를 지양했는가?
- [ ] EmptyState가 포함되었는가?
- [ ] LoadingState / ErrorState와 연결 가능한가?
- [ ] List와 Item Component 책임이 분리되었는가?
- [ ] 클릭 가능한 Item에 div onClick을 남용하지 않았는가?
- [ ] Table이 실제 표 데이터에 사용되었는가?
- [ ] Table caption이 제공되었는가?
- [ ] th scope가 지정되었는가?
- [ ] Table sorting에 aria-sort가 제공되었는가?
- [ ] Pagination에 aria-current가 제공되었는가?
- [ ] Pagination이 API 호출을 직접 하지 않는가?
- [ ] Tab과 Route 기준이 구분되었는가?
- [ ] Tab에 aria-selected가 제공되었는가?
- [ ] Dropdown에 aria-expanded가 제공되었는가?
- [ ] Select와 Dropdown 역할이 구분되었는가?
- [ ] Accordion trigger가 button인가?
- [ ] Accordion에 aria-expanded / aria-controls가 있는가?
- [ ] destructive action에 ConfirmDialog가 연결되었는가?
- [ ] Common UI에 도메인 로직이 과도하게 들어가지 않았는가?
```

---

### [실무]

검수 Flow:

```text
List / Table / Navigation Draft
→ Data State Check
→ Key Check
→ Semantic HTML Check
→ Interaction Check
→ Accessibility Check
→ Component Responsibility Check
→ Anti Pattern Check
→ Final Review
```

치명적 문제:

```text
List key로 index 사용
빈 목록 EmptyState 없음
Table을 div로 구현
caption 없는 복잡한 Table
th scope 누락
Tab과 Route 혼동
Dropdown aria-expanded 누락
Select로 액션 메뉴 구현
Accordion trigger를 div로 구현
클릭 가능한 item에 div onClick 사용
Pagination 내부 API 호출
```

---

### [FAQ]

Q. List Table Navigation 검수에서 가장 중요한 것은 뭐야?
A. 반복 데이터 key, EmptyState, semantic HTML, 접근성 상태, Component 책임 분리를 먼저 확인해야 한다.

Q. 치명적인 List UI 문제는 뭐야?
A. index key 사용, EmptyState 누락, 클릭 가능한 div 사용, List 내부 API 호출이 치명적이다.

Q. 치명적인 Navigation UI 문제는 뭐야?
A. Tab과 Route 혼동, Dropdown 접근성 누락, Accordion trigger를 div로 만드는 문제가 크다.

---

# Retrieval Queries

### [FAQ]

Q. List Table Navigation 문서는 왜 필요해?
A. Frontend Agent가 목록, 표, 탭, 드롭다운 같은 반복 UI와 탐색 UI를 일관되게 설계하고 접근성 문제를 줄이기 위해 필요하다.

Q. List와 Table은 어떻게 구분해?
A. 단순 카드나 항목 반복은 List가 적합하고, 행과 열로 비교하는 표 데이터는 Table이 적합하다.

Q. Navigation UI에서 가장 중요한 기준은 뭐야?
A. 사용자가 현재 위치와 선택 상태를 이해할 수 있어야 하고, keyboard 접근성과 aria 상태가 제공되어야 한다.

Q. List Component는 어떻게 설계해?
A. items를 반복 렌더링하고, stable key, EmptyState, Item Component 분리, semantic list 구조를 포함한다.

Q. List key로 index를 써도 돼?
A. 정렬, 추가, 삭제가 있는 목록에서는 index key를 지양하고 고유 id를 사용하는 것이 좋다.

Q. 목록이 비어 있으면 그냥 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. EmptyState를 보여주는 것이 사용자 경험에 좋다.

Q. List Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. API 호출은 Page Component나 Custom Hook에서 처리하고 List는 렌더링에 집중하는 것이 좋다.

Q. 클릭 가능한 List Item은 div에 onClick을 붙이면 돼?
A. 권장하지 않는다. 페이지 이동이면 Link나 anchor, 액션이면 button을 사용하는 것이 접근성에 좋다.

Q. ListItem에 leftArea, rightArea를 둬도 돼?
A. 가능하다. 아이콘, badge, action처럼 위치가 명확한 UI를 넣을 때 유용하다.

Q. NotificationItem은 Common UI야 Feature UI야?
A. notification 데이터 구조에 의존하므로 보통 Feature UI다.

Q. Table Component는 어떻게 설계해?
A. caption, thead, tbody, th, td, row key, EmptyState, sorting, pagination 관계를 포함해 설계한다.

Q. Table 대신 div로 만들어도 돼?
A. 표 형태의 데이터라면 table 요소를 사용하는 것이 의미와 접근성에 좋다.

Q. Table에 caption이 꼭 필요해?
A. 권장한다. 특히 복잡한 표에서는 표의 목적을 설명하는 데 도움이 된다.

Q. Table row key로 index를 써도 돼?
A. 정렬, 추가, 삭제가 가능하면 index key를 지양하고 고유 id를 사용하는 것이 좋다.

Q. Table 정렬은 th에 onClick을 붙이면 돼?
A. 권장하지 않는다. 정렬 가능한 헤더 내부에 button을 두고 aria-sort로 정렬 상태를 제공하는 것이 좋다.

Q. Table에서 삭제 버튼을 바로 실행해도 돼?
A. 중요한 데이터 삭제는 ConfirmDialog를 연결하는 것이 안전하다.

Q. Table sorting은 Table Component가 직접 처리해야 해?
A. 단순 client sorting은 가능하지만 server sorting이나 filter 연동은 Page 또는 Feature Hook에서 관리하는 것이 좋다.

Q. Pagination Component는 어떻게 설계해?
A. currentPage, totalPages, previous, next, page button, aria-current, onPageChange를 기준으로 설계한다.

Q. Pagination 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Pagination은 onPageChange만 전달하고 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

Q. currentPage는 0부터 시작하는 게 좋아 1부터 시작하는 게 좋아?
A. 프로젝트 기준으로 통일해야 한다. UI 표시에는 보통 1-based가 자연스럽다.

Q. totalPages가 1이면 Pagination을 보여줘야 해?
A. 보통 숨기는 것이 자연스럽지만 프로젝트 UX 기준에 따라 결정할 수 있다.

Q. Tab Component는 어떻게 설계해?
A. selected value, tablist, tab trigger, tabpanel, onChange, aria-selected를 기준으로 설계한다.

Q. Tab 상태는 Local State로 둬도 돼?
A. 해당 화면 내부에서만 필요하면 Local State로 충분하다. 공유나 새로고침 유지가 필요하면 URL State를 검토한다.

Q. Tab과 Route는 어떻게 구분해?
A. 페이지 수준 이동이면 Route, 같은 페이지 내부 패널 전환이면 Tab이 적합하다.

Q. Tab에 role을 꼭 넣어야 해?
A. 접근성을 고려하면 role tablist, tab, tabpanel과 aria-selected를 함께 제공하는 것이 좋다.

Q. 상세 페이지의 정보 / 리뷰 / 지도는 Tab이 좋아 Route가 좋아?
A. 같은 페이지 내부 패널 전환이면 Tab이 적합하고, 각 패널을 직접 공유해야 하면 query parameter나 nested route를 검토한다.

Q. Tab 선택을 새로고침 후에도 유지하려면?
A. URL query parameter나 storage state를 사용할 수 있다. 공유가 필요하면 URL State가 더 적합하다.

Q. 모든 화면 전환을 Tab으로 처리해도 돼?
A. 아니다. 페이지 수준 이동은 Route로 처리하는 것이 좋다.

Q. Dropdown Component는 어떻게 설계해?
A. trigger, open state, menu, item, onSelect, onClose, aria-haspopup, aria-expanded를 기준으로 설계한다.

Q. Dropdown은 그냥 div로 열고 닫으면 돼?
A. 시각적으로는 가능하지만 키보드 접근성, aria-expanded, 닫기 동작을 고려해야 한다.

Q. Select와 Dropdown은 같아?
A. 다르다. Form 값 선택에는 select가 적합할 수 있고, 메뉴 액션에는 Dropdown Menu가 적합하다.

Q. Dropdown이 복잡해지면 어떻게 해?
A. keyboard navigation과 focus 관리가 복잡하면 Headless UI 라이브러리 사용을 검토할 수 있다.

Q. 지역 선택 필터는 Select야 Dropdown이야?
A. Form 값 선택 성격이 강하면 Select가 적합하고, 복잡한 필터 메뉴라면 Dropdown이나 FilterBar를 검토할 수 있다.

Q. 더보기 메뉴는 Select로 만들어도 돼?
A. 권장하지 않는다. 수정, 삭제 같은 액션 메뉴는 Dropdown Menu가 더 적합하다.

Q. custom select를 직접 만들면 안 돼?
A. 가능하지만 keyboard navigation, focus 관리, aria 속성 구현이 필요하므로 복잡하면 검증된 라이브러리를 검토한다.

Q. Accordion Component는 어떻게 설계해?
A. trigger, panel, open state, aria-expanded, aria-controls, button trigger를 기준으로 설계한다.

Q. Accordion trigger는 div로 만들어도 돼?
A. 권장하지 않는다. 펼침 / 접힘 액션은 button을 사용하는 것이 접근성에 좋다.

Q. Accordion에는 aria-expanded가 필요해?
A. 필요하다. 현재 패널이 열려 있는지 보조기술에 전달할 수 있다.

Q. FAQ는 Accordion으로 만들어도 돼?
A. 가능하다. 단 중요한 안내를 숨기지 않도록 UX 기준을 함께 고려해야 한다.

Q. List Table Navigation 검수에서 가장 중요한 것은 뭐야?
A. 반복 데이터 key, EmptyState, semantic HTML, 접근성 상태, Component 책임 분리를 먼저 확인해야 한다.

Q. 치명적인 List UI 문제는 뭐야?
A. index key 사용, EmptyState 누락, 클릭 가능한 div 사용, List 내부 API 호출이 치명적이다.

Q. 치명적인 Navigation UI 문제는 뭐야?
A. Tab과 Route 혼동, Dropdown 접근성 누락, Accordion trigger를 div로 만드는 문제가 크다.

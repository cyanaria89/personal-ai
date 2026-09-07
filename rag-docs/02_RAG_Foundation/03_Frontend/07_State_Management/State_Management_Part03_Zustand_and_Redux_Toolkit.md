# State Management Part03 - Zustand and Redux Toolkit

---

# 1. Global Store Overview

## 1.1 Global Store Purpose

### [개념]

Global Store는 여러 Page, 여러 Feature, 깊은 Component Tree에서 반복적으로 필요한 Client State를 중앙에서 관리하는 구조다.

Global Store는 Local State, Shared State, URL State, Server State로 해결하기 어려운 앱 단위 상태를 관리할 때 사용한다.

Global Store는 모든 State를 넣는 저장소가 아니다.

---

### [핵심]

Global Store 주요 목적:

- App-wide Client State 관리
- 여러 Page 공유 상태 관리
- Auth State 요약 관리
- Global UI State 관리
- Notification Count 관리
- User Preference 관리
- Store Action 통합
- State Reset 기준 제공
- Props Drilling 완화
- State Flow 추적 지원

Global Store 후보:

- Zustand
- Redux Toolkit
- Context + useReducer
- External Store
- Feature Store

---

### [실무]

2026 실무 기준에서 Global Store는 아래 순서로 검토한다.

```text
State 발견
→ Local State로 충분한가?
→ Shared State로 충분한가?
→ URL State가 더 적합한가?
→ Server State가 아닌가?
→ Derived State가 아닌가?
→ 여러 Page에서 반복 사용되는가?
→ Global Store 검토
```

Global Store 적합 상태:

```text
authenticated
auth user summary
theme
language
global toast
global modal
sidebar state
notification unread count
cart
user preference
app layout state
```

Global Store 부적합 상태:

```text
단일 input value
단일 Component modal open
Page 내부 filter
API list cache 전체
Derived State
Form 입력값 전체
Server pagination result
임시 hover state
```

---

### [FAQ]

Q. Global Store는 언제 필요해?
A. 여러 Page나 여러 Feature에서 반복적으로 필요한 Client State가 있고 Local State나 Shared State로 해결하기 어려울 때 필요하다.

Q. 모든 State를 Global Store에 넣으면 편하지 않아?
A. 권장하지 않는다. Store가 커지고 데이터 흐름 추적, reset, persistence, Re-render 관리 비용이 증가한다.

Q. API 응답 데이터도 Global Store에 넣어야 해?
A. 대부분 아니다. API 응답 데이터는 Server State로 보고 TanStack Query 같은 Server State 도구를 우선 검토한다.

---

# 2. Global Store Classification

## 2.1 Store State Type

### [개념]

Store State Type은 Global Store에 넣을 수 있는 State와 넣지 말아야 할 State를 구분하는 기준이다.

Global Store는 Client State 중에서도 앱 단위 공유가 필요한 값만 관리한다.

---

### [핵심]

Store 적합 State:

- Auth State
- UI Global State
- Layout State
- Preference State
- Notification Summary State
- Cart State
- Feature Shared State
- Non-sensitive Persistence State

Store 부적합 State:

- Local UI State
- Form Local State
- Server State
- Derived State
- URL State
- API Cache
- Temporary Draft State
- Sensitive Persistence State

---

### [실무]

Store State 판단표:

| State 예시                | Store 적합성 | 권장 위치                    |
| ------------------------- | -----------: | ---------------------------- |
| authenticated             |         높음 | authStore                    |
| user summary              |         높음 | authStore                    |
| user profile detail       |         낮음 | TanStack Query               |
| theme                     |         높음 | uiStore / themeStore         |
| global toast              |         높음 | uiStore                      |
| sidebarOpen               |         중간 | uiStore 또는 Layout State    |
| searchKeyword             |         낮음 | URL State                    |
| festivalList              |         낮음 | TanStack Query               |
| reviewFormContent         |         낮음 | Form Local State             |
| filteredFestivalList      |         낮음 | Derived Value                |
| notification unread count |         중간 | notificationStore 또는 Query |
| access token              |         주의 | 인증 구조 기준               |
| refresh token             |         주의 | 보안 기준 우선               |

---

### [FAQ]

Q. Store에 넣어도 되는 State는 뭐야?
A. 여러 Page에서 반복적으로 필요한 Client State, Auth Summary, Global UI State, User Preference 등이 적합하다.

Q. Store에 넣으면 안 되는 State는 뭐야?
A. 단일 Component State, Form 입력값, Server State, Derived State, URL State는 보통 Store에 넣지 않는다.

Q. notification unread count는 Store에 둬도 돼?
A. 여러 화면에서 반복적으로 필요하면 Store 후보가 될 수 있지만 서버 동기화가 중요하면 Query와 함께 설계해야 한다.

---

## 2.2 Store Boundary Rules

### [개념]

Store Boundary는 Store가 책임지는 범위와 책임지지 않는 범위를 구분하는 규칙이다.

Store Boundary가 불명확하면 Server State와 Client State가 섞이고 Store가 비대해진다.

---

### [핵심]

Store Boundary 기준:

- Client State만 Store 후보
- Server State는 Query Cache 우선
- Derived State 저장 금지
- URL State 중복 저장 금지
- Form State 전역화 금지
- 민감정보 persist 금지
- Store별 책임 분리
- logout reset 범위 명확화

---

### [실무]

Store Boundary Flow:

```text
State 추가 요청
→ Client State인가?
→ 여러 Page에서 필요한가?
→ Store 도메인에 맞는가?
→ reset 기준이 있는가?
→ persist 필요 여부 확인
→ 민감정보 여부 확인
→ Store 추가 또는 다른 위치 선택
```

Store Boundary 예:

```text
authStore 책임:
- authenticated
- user summary
- login
- logout
- clearAuth

authStore 비책임:
- user profile detail
- order history
- festival list
- review form input
- filtered user data
```

주의:

- Store는 API 응답의 임시 보관소가 아니다.
- Store는 모든 Component State를 모으는 곳이 아니다.
- Store는 도메인별 책임이 명확해야 한다.
- Store가 비대해지면 State Classification을 다시 수행한다.

---

### [FAQ]

Q. Store Boundary가 왜 중요해?
A. Store 책임을 명확히 해야 Server State 중복 저장, Derived State 저장, Form State 전역화 문제를 막을 수 있다.

Q. authStore에 user profile 전체를 넣어도 돼?
A. 사용자 요약 정보는 가능하지만 상세 프로필은 Server State로 관리하는 것이 더 적합할 수 있다.

Q. Store가 커지면 어떻게 해?
A. State Type을 재분류하고 Local, Shared, URL, Server State로 분리한 뒤 Store를 도메인별로 나눈다.

---

# 3. Zustand Overview

## 3.1 Zustand Purpose

### [개념]

Zustand는 간단한 API로 전역 상태 Store를 만들 수 있는 React 상태관리 라이브러리다.

Zustand는 Context보다 action과 상태가 많고 Redux Toolkit보다 가벼운 Global State가 필요할 때 적합하다.

---

### [핵심]

Zustand 주요 특징:

- create 기반 Store 생성
- Hook 기반 사용
- Selector 기반 구독
- 간단한 API
- 적은 Boilerplate
- Store 내부 action 정의
- 도메인별 Store 분리 가능
- Persistence Middleware 가능
- Lightweight Global Store
- TypeScript 친화적

---

### [실무]

Zustand 적합 상황:

```text
Global State 필요
→ 상태와 action이 Context보다 많음
→ Redux Toolkit은 과함
→ selector 기반 구독이 필요함
→ Zustand 검토
```

Zustand 적합 예:

```text
auth summary
theme
sidebar state
global toast
global modal
notification unread count
user preference
cart
medium complexity global state
```

Zustand 부적합 예:

```text
API list cache 전체
pagination response
Form input 전체
단일 Component UI State
Derived State
검색 URL Query
복잡한 enterprise state architecture
```

---

### [FAQ]

Q. Zustand는 언제 써?
A. Context보다 action과 상태가 많고 Redux Toolkit보다 가벼운 전역 상태가 필요할 때 적합하다.

Q. Zustand는 Redux보다 쉬워?
A. 일반적으로 코드량이 적고 API가 단순해서 작은 전역 Store에는 더 간단하게 사용할 수 있다.

Q. Zustand에 API 데이터를 전부 넣어도 돼?
A. 권장하지 않는다. 서버 데이터 캐싱은 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

---

## 3.2 Zustand Basic Store

### [개념]

Zustand Basic Store는 create 함수를 사용해 State와 Action을 함께 정의하는 전역 Store 구조다.

Component는 Store Hook을 호출하고 Selector로 필요한 값만 구독한다.

---

### [핵심]

Zustand 기본 구성:

- create
- state field
- action function
- set
- get
- selector
- custom store hook
- TypeScript Store Type
- initial value
- reset action

---

### [실무]

기본 예:

```typescript
import { create } from "zustand";

type UiStore = {
  sidebarOpen: boolean;
  toggleSidebar: () => void;
  closeSidebar: () => void;
};

export const useUiStore = create<UiStore>((set) => ({
  sidebarOpen: false,

  toggleSidebar: () =>
    set((state) => ({
      sidebarOpen: !state.sidebarOpen,
    })),

  closeSidebar: () =>
    set({
      sidebarOpen: false,
    }),
}));
```

사용 예:

```tsx
const sidebarOpen = useUiStore((state) => state.sidebarOpen);
const toggleSidebar = useUiStore((state) => state.toggleSidebar);
```

권장 기준:

- Store Hook 이름은 `use도메인Store` 형태로 작성한다.
- 필요한 값만 selector로 구독한다.
- State와 Action을 같은 Store에 정의한다.
- reset action을 제공한다.
- Server State 전체를 저장하지 않는다.
- Store를 도메인별로 분리한다.

---

### [FAQ]

Q. Zustand Store는 어떻게 만들어?
A. create 함수로 State field와 Action function을 함께 정의해 Store Hook을 만든다.

Q. Zustand에서 action 함수를 Store 안에 넣어도 돼?
A. 가능하다. Zustand에서는 상태와 상태 변경 함수를 함께 정의하는 방식이 일반적이다.

Q. Zustand Store Hook 이름은 어떻게 지어?
A. useAuthStore, useUiStore, useNotificationStore처럼 도메인 책임을 드러내는 이름이 좋다.

---

# 4. Zustand Selector Rules

## 4.1 Zustand Selector Purpose

### [개념]

Zustand Selector는 Store에서 Component가 필요한 값만 선택해 구독하는 방식이다.

Selector를 사용하면 불필요한 Re-render를 줄이고 Component 의존성을 명확히 할 수 있다.

---

### [핵심]

Selector 목적:

- 필요한 State만 구독
- 필요한 Action만 구독
- Re-render 범위 축소
- Component 의존성 명확화
- Store 구조 캡슐화
- 성능 최적화 기반 제공

---

### [실무]

좋은 예:

```tsx
const authenticated = useAuthStore((state) => state.authenticated);
const logout = useAuthStore((state) => state.logout);
```

주의 예:

```tsx
const authStore = useAuthStore();
```

권장 기준:

```text
Component에서 필요한 값만 selector로 선택
→ 불필요한 Store 전체 구독 방지
→ 상태 변경 영향 범위 감소
```

주의:

- Store 전체를 구독하지 않는다.
- Component마다 필요한 값만 선택한다.
- 여러 값을 객체로 선택할 때 Re-render 기준을 고려한다.
- Derived Value는 Store에 저장하기보다 selector 또는 계산 함수로 처리한다.

---

### [FAQ]

Q. Zustand selector는 왜 써?
A. 필요한 상태만 구독해 불필요한 Re-render를 줄이기 위해 사용한다.

Q. useAuthStore()처럼 전체 Store를 가져오면 안 돼?
A. 가능은 하지만 Store 변경 시 불필요한 Re-render가 늘 수 있어 필요한 값만 선택하는 것이 좋다.

Q. action 함수도 selector로 가져와야 해?
A. 권장된다. Component가 사용하는 action만 선택하면 의존성이 명확해진다.

---

## 4.2 Multiple Selector Rules

### [개념]

Multiple Selector Rules는 Zustand Store에서 여러 값을 가져올 때 selector를 어떻게 구성할지 결정하는 기준이다.

여러 값을 한 번에 객체로 반환하면 참조 변경으로 Re-render가 발생할 수 있으므로 주의가 필요하다.

---

### [핵심]

여러 값 선택 방식:

- 개별 selector 사용
- object selector 사용
- shallow comparison 검토
- custom selector hook
- derived selector function
- store slice selector

---

### [실무]

개별 selector 예:

```tsx
const user = useAuthStore((state) => state.user);
const authenticated = useAuthStore((state) => state.authenticated);
const logout = useAuthStore((state) => state.logout);
```

객체 selector 예:

```tsx
const auth = useAuthStore((state) => ({
  user: state.user,
  authenticated: state.authenticated,
  logout: state.logout,
}));
```

권장 기준:

```text
값 1~2개 필요
→ 개별 selector 사용

여러 값 묶음 필요
→ shallow comparison 또는 custom hook 검토

반복되는 선택 로직
→ custom selector hook 검토
```

주의:

- 객체 selector는 매번 새 객체를 반환할 수 있다.
- shallow 비교가 필요한 경우 팀 컨벤션을 정한다.
- 불필요한 selector 추상화는 피한다.
- 성능 문제는 측정 후 최적화한다.

---

### [FAQ]

Q. Zustand에서 여러 값을 가져올 때 어떻게 해?
A. 개별 selector를 사용하거나 필요하면 shallow comparison이 적용된 객체 selector를 검토한다.

Q. 객체 selector는 위험해?
A. 무조건 위험한 것은 아니지만 새 객체 반환으로 Re-render가 늘 수 있어 비교 전략을 고려해야 한다.

Q. Zustand selector를 custom hook으로 감싸도 돼?
A. 가능하다. 반복되는 selector 조합은 custom hook으로 감싸 사용성을 높일 수 있다.

---

# 5. Zustand Store Design

## 5.1 Domain Store Separation

### [개념]

Domain Store Separation은 Zustand Store를 auth, ui, notification처럼 책임 기준으로 분리하는 설계 규칙이다.

Store를 하나의 거대한 객체로 만들면 유지보수와 reset 관리가 어려워진다.

---

### [핵심]

Store 분리 후보:

- authStore
- uiStore
- themeStore
- toastStore
- notificationStore
- cartStore
- preferenceStore
- layoutStore
- featureStore

---

### [실무]

Store 분리 예:

```text
authStore
- user
- authenticated
- setUser
- clearAuth

uiStore
- sidebarOpen
- toggleSidebar
- toast
- showToast
- hideToast

notificationStore
- unreadCount
- setUnreadCount
- resetNotification
```

분리 기준:

```text
상태 책임이 다른가?
→ Store 분리 검토

logout 시 reset 대상이 다른가?
→ Store 분리 검토

사용하는 Component 범위가 다른가?
→ Store 분리 검토

persist 대상이 다른가?
→ Store 분리 검토
```

주의:

- 모든 field마다 Store를 만들지 않는다.
- 관련 상태와 action은 같은 Store에 둔다.
- Store 간 순환 의존을 피한다.
- 공통 reset 전략을 정한다.
- Server State Store를 별도로 만들지 않는다.

---

### [FAQ]

Q. Zustand Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. Store를 하나로 만들면 안 돼?
A. 작은 프로젝트에서는 가능하지만 규모가 커지면 책임이 섞여 유지보수가 어려워질 수 있다.

Q. Store를 너무 잘게 나누면 문제야?
A. 관련 상태가 흩어져 흐름 추적이 어려워질 수 있으므로 책임 단위로 적절히 나누는 것이 좋다.

---

## 5.2 Zustand Auth Store

### [개념]

Zustand Auth Store는 인증 여부와 사용자 요약 정보를 앱 전역에서 관리하는 Store다.

Auth Store는 Frontend UX를 위한 상태이며 실제 인증/인가는 Backend에서 검증해야 한다.

---

### [핵심]

Auth Store 구성:

- user
- authenticated
- loading
- role
- setUser
- clearAuth
- setAuthenticated
- logout
- reset
- user-specific cache reset trigger

---

### [실무]

Auth Store 예:

```typescript
import { create } from "zustand";

type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthStore = {
  user: AuthUser | null;
  authenticated: boolean;
  loading: boolean;
  setUser: (user: AuthUser) => void;
  clearAuth: () => void;
  setLoading: (loading: boolean) => void;
};

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  authenticated: false,
  loading: true,

  setUser: (user) =>
    set({
      user,
      authenticated: true,
      loading: false,
    }),

  clearAuth: () =>
    set({
      user: null,
      authenticated: false,
      loading: false,
    }),

  setLoading: (loading) =>
    set({
      loading,
    }),
}));
```

주의:

- JWT 존재만으로 authenticated를 완전히 신뢰하지 않는다.
- user detail 전체를 Store에 과도하게 저장하지 않는다.
- 민감정보 저장을 최소화한다.
- logout 시 authStore와 user-specific Store를 reset한다.
- Query Cache reset 또는 invalidate를 함께 고려한다.
- role check는 Backend에서도 반드시 수행한다.

---

### [FAQ]

Q. Auth State는 Zustand에 적합해?
A. 여러 Page에서 필요하고 action이 명확하므로 Zustand authStore에 적합한 경우가 많다.

Q. Auth Store에 access token을 저장해도 돼?
A. 인증 구조와 보안 요구사항에 따라 신중히 결정해야 하며 민감정보 저장은 최소화해야 한다.

Q. logout 시 Auth Store만 초기화하면 돼?
A. 아니다. user-specific cache, notificationStore, 민감한 화면 상태도 함께 초기화해야 할 수 있다.

---

## 5.3 Zustand UI Store

### [개념]

Zustand UI Store는 앱 전역 UI 상태를 관리하는 Store다.

Global Toast, Global Modal, Sidebar, Theme처럼 여러 화면에서 제어할 수 있는 UI 상태가 대상이다.

---

### [핵심]

UI Store 구성:

- sidebarOpen
- theme
- globalToast
- globalModal
- openModal
- closeModal
- showToast
- hideToast
- toggleSidebar
- resetUi

---

### [실무]

UI Store 예:

```typescript
type Toast = {
  message: string;
  type: "success" | "error" | "info";
} | null;

type UiStore = {
  sidebarOpen: boolean;
  toast: Toast;
  toggleSidebar: () => void;
  showToast: (toast: NonNullable<Toast>) => void;
  hideToast: () => void;
  resetUi: () => void;
};

export const useUiStore = create<UiStore>((set) => ({
  sidebarOpen: false,
  toast: null,

  toggleSidebar: () =>
    set((state) => ({
      sidebarOpen: !state.sidebarOpen,
    })),

  showToast: (toast) =>
    set({
      toast,
    }),

  hideToast: () =>
    set({
      toast: null,
    }),

  resetUi: () =>
    set({
      sidebarOpen: false,
      toast: null,
    }),
}));
```

주의:

- 단일 Component에서만 쓰는 modal open은 Local State가 적합하다.
- Page 내부 UI State를 무조건 uiStore에 넣지 않는다.
- Global Toast는 Store에 적합할 수 있다.
- Theme은 Context 또는 Store 모두 가능하다.
- UI Store가 Form State를 포함하지 않게 한다.

---

### [FAQ]

Q. UI State는 Zustand에 넣어도 돼?
A. 여러 Page에서 제어되는 Global Toast, Sidebar, Global Modal 같은 UI State는 Zustand에 적합할 수 있다.

Q. 단일 modal open도 uiStore에 넣어야 해?
A. 아니다. 특정 Component 내부 modal이면 Local State가 적합하다.

Q. Theme은 Context와 Zustand 중 어디가 좋아?
A. 단순 Theme은 Context로 충분하고 다른 UI Store와 함께 관리하려면 Zustand도 가능하다.

---

# 6. Zustand Persistence Rules

## 6.1 Zustand Persist Purpose

### [개념]

Zustand Persist는 Store 일부 값을 localStorage, sessionStorage 같은 저장소에 유지하는 방식이다.

Persistence는 새로고침 후에도 유지해야 하는 비민감 설정에만 제한적으로 사용한다.

---

### [핵심]

Persist 적합 대상:

- theme
- language
- sidebar preference
- user preference
- simple non-sensitive setting
- recent search basics

Persist 주의 대상:

- access token
- refresh token
- password
- personal sensitive data
- payment data
- full server cache
- form sensitive input
- auth detail data

---

### [실무]

Persist 판단 Flow:

```text
Store State 발견
→ 새로고침 후 유지가 필요한가?
→ URL State가 더 적합하지 않은가?
→ 서버 저장이 더 적합하지 않은가?
→ 민감정보가 아닌가?
→ 최소 field만 persist
```

주의:

- localStorage는 JavaScript에서 접근 가능하다.
- XSS 발생 시 노출 위험이 있다.
- 민감정보 persist를 피한다.
- persist 대상은 최소화한다.
- logout 시 사용자별 저장 값을 제거할지 검토한다.
- version migration 기준을 고려한다.

---

### [FAQ]

Q. Zustand Persist는 언제 써?
A. 새로고침 후 유지해야 하는 비민감 사용자 설정을 저장할 때 사용한다.

Q. 모든 Store를 persist하면 좋아?
A. 아니다. 필요한 최소 field만 persist해야 한다.

Q. access token을 persist해도 돼?
A. 보안 위험이 있으므로 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

---

## 6.2 Persist Partialize Rules

### [개념]

Persist Partialize는 Store 전체가 아니라 필요한 일부 State만 저장하는 규칙이다.

Store 전체를 persist하면 민감정보, 임시 상태, 오래된 데이터가 저장될 수 있다.

---

### [핵심]

Partialize 목적:

- persist field 제한
- 민감정보 저장 방지
- 임시 UI State 저장 방지
- Server State 저장 방지
- 저장 데이터 크기 축소
- version migration 관리 용이

---

### [실무]

개념 예:

```typescript
persist(
  (set) => ({
    theme: "light",
    sidebarOpen: false,
    toast: null,
    setTheme: (theme) => set({ theme }),
  }),
  {
    name: "ui-store",
    partialize: (state) => ({
      theme: state.theme,
    }),
  },
);
```

판단 기준:

```text
theme
→ persist 가능

toast
→ persist 불필요

sidebarOpen
→ preference라면 persist 가능

auth user detail
→ persist 주의

server cache
→ persist 금지
```

주의:

- partialize 없이 Store 전체 저장을 피한다.
- 임시 상태는 저장하지 않는다.
- logout 시 persist cleanup을 검토한다.
- persist schema 변경 시 version 전략을 검토한다.

---

### [FAQ]

Q. partialize는 왜 필요해?
A. Store 전체가 아니라 필요한 값만 저장해 민감정보와 임시 상태 저장을 방지하기 위해 필요하다.

Q. toast 상태를 persist해야 해?
A. 보통 필요 없다. toast는 임시 UI State이므로 새로고침 후 유지 대상이 아니다.

Q. theme만 persist하고 나머지는 제외할 수 있어?
A. 가능하다. partialize로 저장할 field를 제한할 수 있다.

---

# 7. Zustand Anti Patterns

## 7.1 Massive Zustand Store

### [개념]

Massive Zustand Store는 하나의 Zustand Store에 관련 없는 모든 상태를 넣어 거대한 Store가 되는 문제다.

Massive Store는 전역 상태 남용과 동일하게 유지보수 비용을 키운다.

---

### [핵심]

문제:

- Store 책임 불명확
- 상태 변경 영향 범위 증가
- action 이름 충돌
- reset 기준 불명확
- persist 대상 혼합
- Auth / UI / Server State 혼합
- Component 의존성 증가
- Store 테스트 어려움

---

### [실무]

나쁜 예:

```text
useAppStore
- user
- authenticated
- theme
- sidebarOpen
- festivalList
- searchKeyword
- reviewFormContent
- filteredFestivalList
- toast
- selectedTab
```

개선 예:

```text
useAuthStore
- user
- authenticated
- clearAuth

useUiStore
- theme
- sidebarOpen
- toast

URL State
- searchKeyword

TanStack Query
- festivalList

Local State
- reviewFormContent

Derived Value
- filteredFestivalList
```

Debug Flow:

```text
Store Field 목록화
→ State Type 분류
→ 책임 기준 분리
→ Server State 제거
→ Derived State 제거
→ Form State 제거
→ Persist 대상 최소화
```

---

### [FAQ]

Q. Zustand Store 하나에 전부 넣으면 안 돼?
A. 작은 프로젝트에서는 가능하지만 규모가 커지면 책임이 섞이고 유지보수가 어려워진다.

Q. Massive Store를 어떻게 줄여?
A. State Type을 재분류하고 authStore, uiStore처럼 책임별로 분리한다.

Q. Zustand Store에 festivalList를 넣으면 안 돼?
A. 서버 API 데이터라면 TanStack Query 같은 Server State 도구가 더 적합하다.

---

## 7.2 Server State in Zustand Problem

### [개념]

Server State in Zustand Problem은 서버가 원본인 API 데이터를 Zustand Store에 복사해 캐시처럼 사용하는 문제다.

이 방식은 stale data, refetch, pagination, mutation invalidation 문제를 수동으로 관리하게 만든다.

---

### [핵심]

문제:

- stale data 발생
- refetch 기준 불명확
- mutation 후 갱신 누락
- pagination 관리 복잡
- loading / error 상태 중복
- Query Cache와 Store 불일치
- 서버 원본과 클라이언트 복사본 불일치

---

### [실무]

나쁜 예:

```text
festivalStore
- festivals
- setFestivals
- filteredFestivals
- loading
- error
- page
- totalCount
```

개선 예:

```text
TanStack Query
- festivals API data
- loading
- error
- pagination result
- refetch
- invalidation

URL State
- keyword
- region
- page

Zustand
- 필요한 경우 selected UI option 또는 global preference만 관리
```

판단 기준:

```text
서버가 원본인가?
→ Server State

캐시 / refetch / stale data가 필요한가?
→ TanStack Query

여러 Page에서 API 데이터를 재사용하는가?
→ Query Cache 우선

단순 전역 Client State인가?
→ Zustand 가능
```

---

### [FAQ]

Q. Zustand에 API 데이터를 넣으면 왜 문제야?
A. 서버 데이터 동기화, stale data, refetch, mutation 갱신을 직접 관리해야 해서 복잡해질 수 있다.

Q. API 데이터는 무조건 TanStack Query를 써야 해?
A. 필수는 아니지만 캐시와 동기화가 필요하면 TanStack Query가 더 적합한 경우가 많다.

Q. Zustand와 TanStack Query를 같이 써도 돼?
A. 가능하다. Zustand는 Client Global State, TanStack Query는 Server State를 담당하도록 역할을 분리한다.

---

## 7.3 Derived State in Store Problem

### [개념]

Derived State in Store Problem은 Store 안에 원본 값과 계산 가능한 파생 값을 함께 저장하는 문제다.

Derived State는 Store에 저장하지 않고 selector, 계산 함수, useMemo로 계산하는 것이 기본이다.

---

### [핵심]

문제 예:

- items + filteredItems
- cartItems + totalPrice
- users + activeUsers
- selectedId + selectedItem
- firstName + lastName + fullName
- serverData + mappedData

---

### [실무]

나쁜 예:

```typescript
type CartStore = {
  items: CartItem[];
  totalPrice: number;
  setItems: (items: CartItem[]) => void;
};
```

좋은 예:

```typescript
const items = useCartStore((state) => state.items);

const totalPrice = items.reduce(
  (sum, item) => sum + item.price * item.quantity,
  0,
);
```

판단 기준:

```text
Store State로 계산 가능한가?
→ Store에 저장 금지

계산이 반복되는가?
→ selector function 검토

계산 비용이 큰가?
→ useMemo 검토

서버 데이터 변환인가?
→ mapping function 검토
```

주의:

- Store action에서 원본과 파생 값을 동시에 업데이트하지 않는다.
- selectedItem보다 selectedId를 저장한다.
- filtered list는 조건과 원본 list로 계산한다.
- Server State의 Derived Value는 Query data 기반으로 계산한다.

---

### [FAQ]

Q. Store에 totalPrice를 저장해도 돼?
A. cartItems로 계산 가능하면 저장하지 않고 계산하는 것이 좋다.

Q. selectedItem과 selectedId를 Store에 같이 넣어도 돼?
A. 권장하지 않는다. selectedId만 저장하고 selectedItem은 원본 데이터에서 계산하는 것이 좋다.

Q. Derived State를 Store에 넣으면 왜 위험해?
A. 원본 값과 파생 값이 서로 달라져 데이터 불일치가 생길 수 있다.

---

# 8. Redux Toolkit Overview

## 8.1 Redux Toolkit Purpose

### [개념]

Redux Toolkit은 Redux를 현대적인 방식으로 사용하기 위한 공식 권장 도구 모음이다.

Redux Toolkit은 복잡한 전역 상태, 명확한 action / reducer 흐름, DevTools 기반 추적, 팀 컨벤션이 필요한 경우에 적합하다.

---

### [핵심]

Redux Toolkit 특징:

- configureStore
- createSlice
- PayloadAction
- Immer 기반 immutable update
- Redux DevTools
- action / reducer 구조화
- predictable update flow
- centralized store
- typed hooks
- middleware extension
- large scale global state

---

### [실무]

Redux Toolkit 적합 상황:

```text
전역 상태 도메인이 많음
→ 상태 변경 흐름 추적 필요
→ action history와 DevTools 필요
→ 팀 컨벤션 중요
→ 복잡한 reducer 구조 필요
→ Redux Toolkit 검토
```

Redux Toolkit 적합 예:

```text
large scale global state
complex domain state
cart with complex rules
permission state summary
multi-feature global state
team convention required state
state transition audit needed
```

Redux Toolkit 부적합 예:

```text
단순 theme
단일 modal open
작은 UI State
단순 auth summary
Component 내부 Form State
Server State cache 전체
```

---

### [FAQ]

Q. Redux Toolkit은 언제 써?
A. 복잡한 전역 상태와 예측 가능한 상태 변경 흐름, DevTools 기반 추적이 필요한 큰 프로젝트에 적합하다.

Q. 작은 프로젝트에도 Redux Toolkit을 써야 해?
A. 필수는 아니다. 작은 프로젝트는 useState, Context, Zustand만으로 충분할 수 있다.

Q. Redux와 Redux Toolkit은 달라?
A. Redux Toolkit은 Redux를 더 쉽게 사용하기 위한 공식 권장 도구다.

---

## 8.2 Redux Toolkit vs Classic Redux

### [개념]

Redux Toolkit은 기존 Redux의 Boilerplate를 줄이고 createSlice, configureStore, Immer 기반 업데이트를 제공한다.

신규 프로젝트에서는 Redux Toolkit 방식이 우선이다.

---

### [핵심]

Redux Toolkit 개선점:

- createSlice로 action/reducer 자동 생성
- configureStore로 Store 설정 단순화
- Immer로 immutable update 간소화
- DevTools 기본 연동
- middleware 기본 설정
- TypeScript 사용성 개선
- Boilerplate 감소

Legacy Redux 특징:

- action type 상수 직접 작성
- action creator 직접 작성
- reducer 직접 작성
- immutable update 수동 작성
- store setup 수동 구성
- connect / mapStateToProps 중심 사용

---

### [실무]

신규 문서 기준:

```text
권장:
Redux Toolkit
createSlice
configureStore
useSelector
useDispatch
typed hooks

비권장:
Legacy Redux boilerplate
connect 중심 신규 코드
mapStateToProps 중심 신규 코드
action type 상수 남발
```

주의:

- 기존 프로젝트 유지보수에서는 legacy Redux를 볼 수 있다.
- 신규 코드에서는 Redux Toolkit과 Hook 기반 사용을 우선한다.
- Redux Toolkit 내부 reducer는 Immer 덕분에 mutation처럼 작성할 수 있다.
- Redux Toolkit도 작은 상태에는 과할 수 있다.

---

### [FAQ]

Q. Redux connect를 써야 해?
A. 신규 문서에서는 Redux Toolkit과 Hook 기반 사용을 우선한다. 기존 코드 유지보수에서 connect를 볼 수는 있다.

Q. Redux Toolkit에서 state를 직접 바꿔도 돼?
A. createSlice 내부 reducer에서는 Immer가 불변 업데이트로 변환하므로 mutation처럼 작성할 수 있다.

Q. Redux Toolkit을 쓰면 Boilerplate가 줄어?
A. 맞다. createSlice와 configureStore로 기존 Redux보다 코드량이 줄어든다.

---

# 9. Redux Store Setup

## 9.1 configureStore

### [개념]

configureStore는 Redux Toolkit에서 Redux Store를 생성하는 표준 API다.

Reducer 등록, middleware 설정, DevTools 설정을 간단하게 구성할 수 있다.

---

### [핵심]

configureStore 구성:

- reducer
- middleware
- devTools
- preloadedState
- store export
- RootState
- AppDispatch
- Provider connection

---

### [실무]

기본 예:

```typescript
import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./authSlice";
import uiReducer from "./uiSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
    ui: uiReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

Provider 연결:

```tsx
import { Provider } from "react-redux";

root.render(
  <Provider store={store}>
    <App />
  </Provider>,
);
```

권장 기준:

- reducer key는 도메인 이름으로 작성한다.
- RootState와 AppDispatch를 export한다.
- typed hooks를 별도 파일로 제공한다.
- Store 설정 파일은 명확한 위치에 둔다.
- Server State 전체를 Redux Store에 넣지 않는다.

---

### [FAQ]

Q. configureStore는 뭐야?
A. Redux Toolkit에서 Redux Store를 생성하고 reducer, middleware, DevTools를 설정하는 API다.

Q. RootState는 왜 필요해?
A. useSelector에서 전체 Store State 타입을 안전하게 사용하기 위해 필요하다.

Q. AppDispatch는 왜 필요해?
A. useDispatch를 TypeScript에서 안전하게 사용하기 위해 필요하다.

---

## 9.2 Typed Redux Hooks

### [개념]

Typed Redux Hooks는 useSelector와 useDispatch에 RootState와 AppDispatch 타입을 적용한 Custom Hook이다.

TypeScript 프로젝트에서는 typed hooks를 사용하는 것이 권장된다.

---

### [핵심]

Typed Hooks 구성:

- useAppDispatch
- useAppSelector
- RootState
- AppDispatch
- typed selector
- typed dispatch
- react-redux hooks

---

### [실무]

예:

```typescript
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "./store";

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

사용 예:

```tsx
const authenticated = useAppSelector((state) => state.auth.authenticated);
const dispatch = useAppDispatch();

dispatch(logout());
```

권장 기준:

- 일반 useSelector 대신 useAppSelector를 사용한다.
- 일반 useDispatch 대신 useAppDispatch를 사용한다.
- hooks 파일을 Store 설정 근처에 둔다.
- Slice별 selector 함수를 별도로 정의할 수 있다.

---

### [FAQ]

Q. useAppSelector는 왜 써?
A. RootState 타입을 적용해 Redux State를 TypeScript에서 안전하게 선택하기 위해 사용한다.

Q. useAppDispatch는 왜 써?
A. AppDispatch 타입을 적용해 dispatch 타입을 안전하게 사용하기 위해 필요하다.

Q. 일반 useSelector를 쓰면 안 돼?
A. 가능하지만 TypeScript 프로젝트에서는 typed hook을 사용하는 것이 좋다.

---

# 10. Redux Slice Rules

## 10.1 createSlice

### [개념]

createSlice는 Redux Toolkit에서 특정 도메인의 state, reducer, action을 함께 정의하는 API다.

Slice는 Redux Store를 도메인 책임 기준으로 나누는 단위다.

---

### [핵심]

createSlice 구성:

- name
- initialState
- reducers
- action
- reducer export
- PayloadAction
- Immer update
- selector
- slice domain

---

### [실무]

기본 예:

```typescript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type UiState = {
  sidebarOpen: boolean;
};

const initialState: UiState = {
  sidebarOpen: false,
};

const uiSlice = createSlice({
  name: "ui",
  initialState,
  reducers: {
    toggleSidebar(state) {
      state.sidebarOpen = !state.sidebarOpen;
    },
    setSidebarOpen(state, action: PayloadAction<boolean>) {
      state.sidebarOpen = action.payload;
    },
    resetUi() {
      return initialState;
    },
  },
});

export const { toggleSidebar, setSidebarOpen, resetUi } = uiSlice.actions;
export default uiSlice.reducer;
```

권장 기준:

- Slice는 도메인 책임 기준으로 나눈다.
- initialState 타입을 명확히 정의한다.
- action 이름은 상태 변경 의도를 드러낸다.
- PayloadAction 타입을 명확히 지정한다.
- reset action을 제공한다.
- Derived State를 Slice State에 저장하지 않는다.

---

### [FAQ]

Q. Redux Slice는 뭐야?
A. 특정 도메인의 state, reducer, action을 함께 정의하는 Redux Toolkit 단위다.

Q. Slice는 어떻게 나눠?
A. auth, ui, notification, cart처럼 도메인 책임 기준으로 나눈다.

Q. createSlice 내부에서 state를 직접 수정해도 돼?
A. 가능하다. Redux Toolkit이 Immer로 불변 업데이트를 처리한다.

---

## 10.2 Redux Action Naming

### [개념]

Redux Action Naming은 reducer action의 의도를 명확하게 표현하는 이름을 정하는 규칙이다.

Action 이름이 불명확하면 상태 변경 흐름 추적이 어려워진다.

---

### [핵심]

권장 Action Naming:

- setUser
- clearAuth
- loginSuccess
- logout
- toggleSidebar
- showToast
- hideToast
- setUnreadCount
- incrementQuantity
- decrementQuantity
- resetCart
- resetUi

비권장 Naming:

- update
- change
- process
- handle
- doSomething
- setData
- commonUpdate

---

### [실무]

Naming 기준:

```text
상태 설정
→ setUser, setTheme, setUnreadCount

상태 초기화
→ clearAuth, resetUi, resetCart

이벤트 결과
→ loginSuccess, submitFailure

토글
→ toggleSidebar

명령성 UI action
→ showToast, hideToast
```

주의:

- action 이름은 Domain 안에서 의미가 명확해야 한다.
- 너무 일반적인 update, setData를 남용하지 않는다.
- Payload 구조를 action 이름과 맞춘다.
- 팀 컨벤션을 유지한다.

---

### [FAQ]

Q. Redux action 이름은 어떻게 지어?
A. setUser, clearAuth, toggleSidebar처럼 상태 변경 의도를 명확히 드러내는 이름이 좋다.

Q. updateData 같은 이름은 안 좋아?
A. 구체적인 변경 의도를 알기 어렵기 때문에 권장하지 않는다.

Q. action 이름에 도메인명을 항상 넣어야 해?
A. Slice 이름이 도메인을 나타내므로 action 내부 이름은 중복 없이 의도를 드러내면 된다.

---

# 11. Redux Toolkit Store Design

## 11.1 Slice Separation Rules

### [개념]

Slice Separation은 Redux State를 auth, ui, notification, cart처럼 도메인 책임 기준으로 나누는 설계 규칙이다.

Slice 분리가 적절해야 Redux Store가 예측 가능하고 유지보수 가능해진다.

---

### [핵심]

Slice 후보:

- authSlice
- uiSlice
- notificationSlice
- cartSlice
- preferenceSlice
- layoutSlice
- permissionSlice
- featureSlice

---

### [실무]

Slice 분리 예:

```text
authSlice
- user
- authenticated
- loading
- setUser
- clearAuth

uiSlice
- sidebarOpen
- toast
- showToast
- hideToast
- resetUi

notificationSlice
- unreadCount
- setUnreadCount
- resetNotification

cartSlice
- items
- addItem
- removeItem
- updateQuantity
- resetCart
```

분리 기준:

```text
도메인 책임이 다른가?
→ Slice 분리

상태 변경 규칙이 다른가?
→ Slice 분리

reset 시점이 다른가?
→ Slice 분리

여러 Feature에서 공통 사용되는가?
→ Global Slice 후보
```

주의:

- 너무 거대한 appSlice를 만들지 않는다.
- 너무 작은 field 단위 Slice도 피한다.
- Server State cache용 Slice를 남발하지 않는다.
- Slice 간 직접 의존을 줄인다.
- logout 시 reset할 Slice를 명확히 한다.

---

### [FAQ]

Q. Redux Slice는 어떻게 나누는 게 좋아?
A. auth, ui, notification, cart처럼 도메인 책임과 reset 기준에 따라 나누는 것이 좋다.

Q. appSlice 하나로 모든 상태를 관리해도 돼?
A. 권장하지 않는다. 책임이 섞이면 유지보수와 디버깅이 어려워진다.

Q. Slice를 너무 많이 나누면 문제야?
A. 관련 상태 흐름이 흩어질 수 있으므로 책임 기준으로 적절히 나누는 것이 좋다.

---

## 11.2 Redux Auth Slice

### [개념]

Redux Auth Slice는 인증 여부, 사용자 요약 정보, 인증 loading 상태를 Redux Store에서 관리하는 Slice다.

Auth Slice는 Frontend UX용 상태이며 실제 인증/인가는 Backend에서 검증해야 한다.

---

### [핵심]

Auth Slice 구성:

- user
- authenticated
- loading
- role
- setUser
- clearAuth
- setAuthLoading
- logout
- resetAuth
- token expired state

---

### [실무]

Auth Slice 예:

```typescript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthState = {
  user: AuthUser | null;
  authenticated: boolean;
  loading: boolean;
};

const initialState: AuthState = {
  user: null,
  authenticated: false,
  loading: true,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    setUser(state, action: PayloadAction<AuthUser>) {
      state.user = action.payload;
      state.authenticated = true;
      state.loading = false;
    },
    clearAuth(state) {
      state.user = null;
      state.authenticated = false;
      state.loading = false;
    },
    setAuthLoading(state, action: PayloadAction<boolean>) {
      state.loading = action.payload;
    },
  },
});

export const { setUser, clearAuth, setAuthLoading } = authSlice.actions;
export default authSlice.reducer;
```

주의:

- access token 저장 위치는 보안 기준에 따라 결정한다.
- JWT 존재만으로 인증 상태를 완전히 신뢰하지 않는다.
- user detail 전체를 Redux에 과도하게 저장하지 않는다.
- logout 시 user-specific Slice와 Query Cache reset을 고려한다.
- role check는 Backend에서도 반드시 수행한다.

---

### [FAQ]

Q. Auth State를 Redux Toolkit으로 관리해도 돼?
A. 가능하다. 인증 상태 흐름이 복잡하고 DevTools 추적이 필요하면 Redux Toolkit이 적합할 수 있다.

Q. Auth Slice에 user detail 전체를 넣어도 돼?
A. 사용자 요약 정보는 가능하지만 상세 프로필은 Server State로 관리하는 것이 더 적합할 수 있다.

Q. Auth Slice만으로 권한 보안이 해결돼?
A. 아니다. Frontend 권한 상태는 UX용이고 실제 접근 제어는 Backend에서 반드시 처리해야 한다.

---

## 11.3 Redux UI Slice

### [개념]

Redux UI Slice는 앱 전역 UI 상태를 Redux Store에서 관리하는 Slice다.

Global Toast, Global Modal, Sidebar처럼 여러 Feature에서 공통으로 제어하는 UI State가 대상이다.

---

### [핵심]

UI Slice 구성:

- sidebarOpen
- toast
- modal
- theme
- showToast
- hideToast
- openModal
- closeModal
- toggleSidebar
- resetUi

---

### [실무]

UI Slice 예:

```typescript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type Toast = {
  message: string;
  type: "success" | "error" | "info";
} | null;

type UiState = {
  sidebarOpen: boolean;
  toast: Toast;
};

const initialState: UiState = {
  sidebarOpen: false,
  toast: null,
};

const uiSlice = createSlice({
  name: "ui",
  initialState,
  reducers: {
    toggleSidebar(state) {
      state.sidebarOpen = !state.sidebarOpen;
    },
    showToast(state, action: PayloadAction<NonNullable<Toast>>) {
      state.toast = action.payload;
    },
    hideToast(state) {
      state.toast = null;
    },
    resetUi() {
      return initialState;
    },
  },
});

export const { toggleSidebar, showToast, hideToast, resetUi } = uiSlice.actions;
export default uiSlice.reducer;
```

주의:

- 단일 Component 내부 UI State는 Redux에 넣지 않는다.
- Page 내부 tab, modal, dropdown은 Local State가 적합할 수 있다.
- Redux UI Slice는 전역 UI에 제한한다.
- Theme은 Context, Zustand, Redux 중 프로젝트 기준으로 선택한다.
- Toast는 새로고침 후 유지 대상이 아니다.

---

### [FAQ]

Q. UI State를 Redux에 넣어도 돼?
A. Global Toast, Sidebar, Global Modal처럼 앱 전역에서 제어되는 UI State는 가능하다.

Q. 단일 dropdown open 상태도 Redux에 넣어야 해?
A. 아니다. 특정 Component 내부 dropdown은 Local State가 적합하다.

Q. Toast 상태는 persist해야 해?
A. 보통 필요 없다. Toast는 임시 UI State이므로 새로고침 후 유지할 필요가 없다.

---

# 12. Redux Selector Rules

## 12.1 Redux Selector Purpose

### [개념]

Redux Selector는 Store State에서 Component가 필요한 값을 선택하는 함수다.

Selector는 Component와 Store 구조의 결합을 줄이고 Derived Value 계산 위치를 명확히 한다.

---

### [핵심]

Selector 목적:

- 필요한 State 선택
- Store 구조 캡슐화
- Derived Value 계산
- Component 의존성 축소
- 재사용 가능한 조회 로직
- TypeScript 타입 안정성
- Memoized Selector 확장 가능

---

### [실무]

기본 selector 예:

```typescript
export const selectAuthenticated = (state: RootState) =>
  state.auth.authenticated;

export const selectAuthUser = (state: RootState) => state.auth.user;

export const selectSidebarOpen = (state: RootState) => state.ui.sidebarOpen;
```

사용 예:

```tsx
const authenticated = useAppSelector(selectAuthenticated);
const user = useAppSelector(selectAuthUser);
```

권장 기준:

- Slice별 selector를 정의한다.
- Component에서 깊은 State 경로를 반복하지 않는다.
- Derived Value는 selector로 계산할 수 있다.
- 복잡한 Derived Value는 memoized selector를 검토한다.
- Server State의 Derived Value는 Query data 기준으로 계산한다.

---

### [FAQ]

Q. Redux selector는 왜 필요해?
A. Component가 Store 구조에 직접 강하게 의존하지 않도록 하고 필요한 값만 선택하기 위해 필요하다.

Q. selector 없이 state.auth.user를 직접 써도 돼?
A. 가능하지만 여러 곳에서 반복되면 Store 구조 변경에 취약해질 수 있다.

Q. Derived Value를 selector에서 계산해도 돼?
A. 가능하다. 원본 State로 계산 가능한 값은 Store에 저장하지 않고 selector에서 계산하는 것이 좋다.

---

## 12.2 Memoized Selector Rules

### [개념]

Memoized Selector는 계산 비용이 있거나 같은 입력에 같은 결과를 재사용해야 하는 Derived Value를 캐싱하는 selector다.

Redux Toolkit 환경에서는 필요할 때 memoized selector를 검토할 수 있다.

---

### [핵심]

Memoized Selector 대상:

- filtered list
- sorted list
- total price
- selected item
- grouped data
- expensive derived value
- repeated calculation
- stable reference 필요 값

---

### [실무]

판단 기준:

```text
Selector 계산이 단순함
→ 일반 selector

filter / sort / group 계산 반복
→ memoized selector 검토

계산 비용이 큼
→ memoized selector 검토

Component Re-render 문제가 있음
→ memoized selector 검토
```

주의:

- 모든 selector를 memoize하지 않는다.
- 단순 값 선택은 memoization이 필요 없다.
- Derived State를 Store에 저장하기보다 selector로 계산한다.
- 성능 문제는 측정 후 최적화한다.
- Server State cache와 Redux Store를 섞지 않는다.

---

### [FAQ]

Q. 모든 Redux selector를 memoize해야 해?
A. 아니다. 단순 값 선택은 일반 selector로 충분하다.

Q. filtered list는 Store에 저장해야 해?
A. 원본 list와 filter 조건으로 계산 가능하면 selector에서 계산하는 것이 좋다.

Q. Memoized Selector는 언제 필요해?
A. filter, sort, group처럼 계산 비용이 있거나 결과 참조 안정성이 필요할 때 검토한다.

---

# 13. Redux Toolkit Anti Patterns

## 13.1 Redux Overuse

### [개념]

Redux Overuse는 단순한 Local State나 작은 UI State까지 Redux Store에 넣는 문제다.

Redux Toolkit은 강력하지만 모든 상태에 필요한 도구는 아니다.

---

### [핵심]

문제:

- 코드량 증가
- Slice 증가
- action / reducer 과다
- Local State 흐름 복잡화
- Component 재사용성 저하
- Store 비대화
- 단순 UI 수정 비용 증가

원인:

- Redux를 기본 선택지로 사용
- State Classification 생략
- Local State와 Global State 혼동
- Props 전달을 모두 문제로 판단
- 팀 컨벤션을 과도하게 적용

---

### [실무]

Redux 도입 전 Flow:

```text
State 발견
→ Local State로 충분한가?
→ Shared State로 충분한가?
→ Context로 충분한가?
→ Zustand로 충분한가?
→ Redux Toolkit이 필요한 복잡도인가?
```

Redux 부적합 예:

```text
input value 하나
modal open 하나
dropdown open
hover state
Page 내부 selected tab
단순 theme만 있는 프로젝트
```

주의:

- Redux Toolkit은 큰 프로젝트에 유리하다.
- 작은 프로젝트는 Zustand나 Context가 더 단순할 수 있다.
- Redux Store는 Server State 캐시 저장소가 아니다.
- Redux 도입은 팀 컨벤션과 디버깅 요구를 함께 고려한다.

---

### [FAQ]

Q. Redux Toolkit을 쓰면 무조건 좋은 구조야?
A. 아니다. 단순 상태에는 과할 수 있으며 useState, Context, Zustand가 더 적합할 수 있다.

Q. 모든 UI State를 Redux에 넣어야 해?
A. 아니다. 단일 Component UI State는 Local State가 적합하다.

Q. Redux Overuse는 어떻게 줄여?
A. State Classification을 먼저 수행하고 Local, Shared, URL, Server State로 충분한지 확인한다.

---

## 13.2 Server State in Redux Problem

### [개념]

Server State in Redux Problem은 서버가 원본인 API 데이터를 Redux Store에 직접 캐시처럼 저장하는 문제다.

Server State는 캐시, stale data, refetch, mutation, invalidation 관리가 필요하므로 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

단, Redux Toolkit 생태계를 기준으로 프로젝트를 설계하는 경우 RTK Query도 선택 후보가 될 수 있다.

---

### [핵심]

문제:

- stale data 발생
- mutation 후 Store 갱신 누락
- pagination 상태 복잡화
- loading / error 중복 관리
- cache invalidation 수동 구현
- API 응답 정규화 부담
- Query Cache와 Redux Store 불일치

---

### [실무]

나쁜 예:

```text
festivalSlice
- festivals
- festivalDetail
- loading
- error
- page
- totalCount
- fetchFestivals
- updateFestival
- deleteFestival
```

개선 예:

```text
TanStack Query 또는 RTK Query
- festival list
- festival detail
- loading
- error
- refetch
- invalidation
- pagination result

Redux Slice
- global UI state
- auth summary
- user preference
```

판단 기준:

```text
API 데이터인가?
→ Server State

cache / refetch / invalidation이 필요한가?
→ TanStack Query 또는 RTK Query

복잡한 Client Global State인가?
→ Redux Toolkit

단순 전역 Client State인가?
→ Zustand도 검토
```

---

### [FAQ]

Q. API 데이터를 Redux에 저장하면 안 돼?
A. 가능은 하지만 캐시와 동기화 관리가 복잡해질 수 있어 Server State 도구를 우선 검토하는 것이 좋다.

Q. Redux Toolkit과 TanStack Query를 같이 써도 돼?
A. 가능하다. Redux Toolkit은 Client Global State, TanStack Query는 Server State를 담당하게 분리하면 된다.

Q. RTK Query는 어디에 해당해?
A. Redux Toolkit 생태계의 Server State 데이터 fetching 도구다. 이 문서 세트는 TanStack Query를 기본 기준으로 설명하지만, Redux Toolkit 중심 프로젝트에서는 RTK Query도 선택 후보가 될 수 있다.

---

## 13.3 Derived State in Redux Problem

### [개념]

Derived State in Redux Problem은 Redux Store에 원본 값과 계산 가능한 파생 값을 함께 저장하는 문제다.

Derived State는 Store에 저장하지 않고 selector로 계산하는 것이 기본이다.

---

### [핵심]

문제 예:

- items + filteredItems
- cartItems + totalPrice
- users + activeUsers
- selectedId + selectedItem
- serverData + mappedData
- firstName + lastName + fullName

---

### [실무]

나쁜 예:

```typescript
type CartState = {
  items: CartItem[];
  totalPrice: number;
};
```

좋은 예:

```typescript
export const selectCartItems = (state: RootState) => state.cart.items;

export const selectTotalPrice = (state: RootState) =>
  state.cart.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
```

주의:

- Derived State를 reducer에서 동기화하려 하지 않는다.
- selectedItem보다 selectedId를 저장한다.
- filtered list는 selector에서 계산한다.
- 계산 비용이 크면 memoized selector를 검토한다.
- Server State 기반 Derived Value는 Query data 기준으로 계산한다.

---

### [FAQ]

Q. Redux Store에 totalPrice를 저장해도 돼?
A. cartItems로 계산 가능하면 selector에서 계산하는 것이 좋다.

Q. filteredItems를 Slice State에 넣으면 안 돼?
A. 원본 list와 filter 조건으로 계산 가능하면 Store에 저장하지 않는 것이 좋다.

Q. Derived State는 Redux에서 어떻게 처리해?
A. selector 또는 memoized selector로 계산한다.

---

# 14. Zustand vs Redux Toolkit

## 14.1 Zustand vs Redux Toolkit Comparison

### [개념]

Zustand와 Redux Toolkit은 모두 Global State를 관리할 수 있지만 적합한 규모와 목적이 다르다.

Zustand는 가볍고 단순한 Store에 적합하고 Redux Toolkit은 복잡하고 추적 가능한 전역 상태 흐름에 적합하다.

---

### [핵심]

비교 기준:

- 프로젝트 규모
- 상태 복잡도
- 코드량
- DevTools 필요성
- 팀 컨벤션
- action history
- selector 사용
- Store 구조
- Boilerplate
- 학습 비용

---

### [실무]

Zustand vs Redux Toolkit:

| 비교        | Zustand              | Redux Toolkit             |
| ----------- | -------------------- | ------------------------- |
| 성격        | 가벼운 전역 Store    | 구조화된 전역 상태관리    |
| 코드량      | 적음                 | 상대적으로 많음           |
| 적합 규모   | 소규모~중규모        | 중규모~대규모             |
| Action 구조 | Store 내부 함수      | Slice reducer action      |
| DevTools    | 가능                 | 강력함                    |
| 팀 컨벤션   | 유연함               | 명확함                    |
| Selector    | Hook selector        | useSelector selector      |
| Boilerplate | 낮음                 | 중간                      |
| 적합 예     | auth, ui, preference | 복잡한 cart, domain state |
| 부적합      | 복잡한 감사 추적     | 단순 UI State             |

---

### [FAQ]

Q. Zustand와 Redux Toolkit 중 뭐가 좋아?
A. 가볍고 단순한 전역 상태는 Zustand가 편하고, 복잡한 상태 변경 추적과 팀 컨벤션이 필요하면 Redux Toolkit이 적합하다.

Q. 작은 프로젝트에는 Zustand가 더 좋아?
A. 보통 Zustand가 더 단순할 수 있다. 단, 팀 컨벤션이나 DevTools 요구가 크면 Redux Toolkit도 가능하다.

Q. 큰 프로젝트에는 무조건 Redux Toolkit이야?
A. 무조건은 아니지만 복잡한 전역 상태 흐름과 팀 단위 컨벤션이 중요하면 Redux Toolkit이 유리할 수 있다.

---

## 14.2 Tool Selection Decision

### [개념]

Tool Selection Decision은 Zustand와 Redux Toolkit 중 어떤 Global Store 도구를 선택할지 결정하는 기준이다.

도구 선택 전에 State Classification과 Store Boundary를 먼저 확인해야 한다.

---

### [핵심]

Zustand 선택 기준:

- 가벼운 Global State
- 빠른 구현
- 작은 코드량
- selector 기반 구독
- 유연한 Store 구조
- Context보다 복잡
- Redux보다 단순

Redux Toolkit 선택 기준:

- 복잡한 Global State
- action / reducer 패턴 필요
- DevTools 추적 중요
- 팀 컨벤션 중요
- 대규모 상태 구조
- Slice 기반 관리
- 예측 가능한 update flow

---

### [실무]

선택 Flow:

```text
Global State 필요
→ Server State가 아닌가?
→ Derived State가 아닌가?
→ 단순 전역 상태인가?
→ Zustand 검토
→ 복잡한 상태 전환과 추적이 필요한가?
→ Redux Toolkit 검토
```

결과 예:

```text
theme
→ Context 또는 Zustand

auth summary
→ Context 또는 Zustand 또는 Redux Toolkit

global toast
→ Zustand 또는 Redux Toolkit

cart complex rules
→ Redux Toolkit 검토

festival list API cache
→ TanStack Query

search filter
→ URL State

review form input
→ Local State 또는 Form Library
```

---

### [FAQ]

Q. 상태관리 도구는 뭘 먼저 써야 해?
A. 먼저 상태 종류와 범위를 분류한 뒤 가장 단순한 도구부터 선택한다.

Q. Zustand와 Redux Toolkit 선택 기준은 뭐야?
A. 가벼운 전역 상태는 Zustand, 복잡한 상태 흐름과 팀 컨벤션이 필요하면 Redux Toolkit이 적합하다.

Q. 도구 선택 전에 반드시 확인할 것은 뭐야?
A. 해당 State가 Server State, URL State, Derived State, Local State로 충분한지 먼저 확인해야 한다.

---

# 15. Store Reset and Logout Rules

## 15.1 Store Reset Purpose

### [개념]

Store Reset은 특정 이벤트에서 Store State를 초기 상태로 되돌리는 규칙이다.

특히 logout, account switch, permission change, sensitive flow 종료 시 Store Reset이 중요하다.

---

### [핵심]

Reset 대상:

- authStore
- notificationStore
- user preference 일부
- user-specific UI state
- cartStore
- sensitive draft state
- permission summary
- Query Cache
- persisted storage

Reset 트리거:

- logout
- token expired
- refresh failure
- account switch
- role changed
- session expired
- user deleted

---

### [실무]

logout reset Flow:

```text
Logout 요청
→ Backend logout 또는 token cleanup
→ authStore reset
→ notificationStore reset
→ user-specific Store reset
→ Query Cache clear 또는 invalidate
→ persisted sensitive data cleanup
→ redirect login page
```

Zustand reset 예:

```typescript
const initialAuthState = {
  user: null,
  authenticated: false,
  loading: false,
};

clearAuth: () => set(initialAuthState);
```

Redux reset 예:

```typescript
clearAuth(state) {
  state.user = null;
  state.authenticated = false;
  state.loading = false;
}
```

주의:

- logout 시 Auth State만 초기화하면 부족할 수 있다.
- Query Cache에 사용자별 데이터가 남을 수 있다.
- persisted storage cleanup이 필요할 수 있다.
- 민감한 화면 상태를 reset한다.
- Reset 순서를 팀 컨벤션으로 정한다.

---

### [FAQ]

Q. logout 시 어떤 Store를 초기화해야 해?
A. auth, notification, user-specific Store, 민감한 화면 상태, Query Cache를 함께 검토해야 한다.

Q. Auth Store만 clear하면 충분해?
A. 아닐 수 있다. 사용자별 캐시나 알림 상태가 남으면 다른 사용자에게 잘못 보일 수 있다.

Q. Store reset action은 왜 필요해?
A. logout, token expired, account switch 같은 이벤트에서 상태를 안전하게 초기화하기 위해 필요하다.

---

## 15.2 User-Specific State Cleanup

### [개념]

User-Specific State Cleanup은 특정 사용자에게 종속된 Store, Cache, Persistence 값을 로그아웃 또는 계정 전환 시 제거하는 규칙이다.

사용자별 상태가 남으면 보안과 UX 문제가 발생할 수 있다.

---

### [핵심]

Cleanup 대상:

- user summary
- unread notification count
- user-specific preference
- cart
- favorite summary
- private dashboard state
- sensitive draft
- user query cache
- persisted user data

---

### [실무]

Cleanup 판단 Flow:

```text
State가 특정 사용자에게 종속되는가?
→ logout 후 남아 있으면 위험한가?
→ account switch 시 다른 사용자에게 보이면 안 되는가?
→ reset 또는 remove persist 필요
```

예:

```text
notification unread count
→ 사용자별 값
→ logout reset 필요

theme
→ 사용자별일 수도 있지만 비민감 설정
→ 정책에 따라 유지 가능

favorite list cache
→ 사용자별 Server State
→ Query Cache clear 필요

review draft
→ 민감할 수 있음
→ reset 또는 임시저장 정책 필요
```

주의:

- 사용자별 Server State는 Query Cache cleanup을 고려한다.
- persist된 사용자 데이터는 remove가 필요할 수 있다.
- 비민감 UI preference는 유지할 수 있지만 정책을 명확히 한다.
- account switch는 logout보다 더 엄격하게 처리한다.

---

### [FAQ]

Q. User-Specific State는 왜 cleanup해야 해?
A. 로그아웃 후 이전 사용자 데이터가 남거나 계정 전환 시 다른 사용자에게 잘못 보이는 문제를 막기 위해 필요하다.

Q. theme도 logout 때 지워야 해?
A. 보통 비민감 설정이라 유지할 수 있지만 사용자별 설정 정책이면 제거할 수 있다.

Q. Query Cache도 cleanup해야 해?
A. 사용자별 API 데이터가 포함되어 있으면 logout 또는 account switch 시 clear 또는 invalidate를 검토해야 한다.

---

# 16. Store Persistence Security

## 16.1 Sensitive Data Persistence

### [개념]

Sensitive Data Persistence는 민감정보를 localStorage, sessionStorage, persisted Store에 저장할 때 발생하는 보안 위험을 다루는 규칙이다.

Frontend Store Persistence는 편의 기능이지만 보안 위험을 동반한다.

---

### [핵심]

민감정보 예:

- access token
- refresh token
- password
- 주민등록번호
- 결제 정보
- 개인 식별 정보
- private message
- sensitive form input
- admin permission data
- security answer

---

### [실무]

보안 판단 Flow:

```text
Persist 대상 발견
→ 민감정보인가?
→ JavaScript 접근 가능 저장소인가?
→ XSS 노출 위험이 있는가?
→ 서버 저장이 더 적합한가?
→ 저장 최소화 또는 금지
```

주의:

- localStorage는 JavaScript로 접근 가능하다.
- XSS가 발생하면 저장 값이 노출될 수 있다.
- token 저장 방식은 프로젝트 보안 설계에 따른다.
- refresh token 저장은 특히 신중해야 한다.
- 민감 Form 입력값은 persist하지 않는다.
- Persist는 UX 편의보다 보안 기준을 우선한다.

---

### [FAQ]

Q. localStorage에 token을 저장해도 돼?
A. 보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. Persist Store에 민감정보를 넣으면 왜 위험해?
A. XSS 등으로 JavaScript 접근 저장소의 값이 노출될 수 있기 때문이다.

Q. 비밀번호 입력값을 persist해도 돼?
A. 안 된다. password 같은 민감 입력값은 persist하지 않는다.

---

## 16.2 Persistence Scope Rules

### [개념]

Persistence Scope는 Store에서 어떤 값을 저장하고 어떤 값을 저장하지 않을지 결정하는 기준이다.

Persistence는 필요한 값만 최소 범위로 적용한다.

---

### [핵심]

Persist 가능 후보:

- theme
- language
- sidebar preference
- simple layout preference
- non-sensitive user preference
- recent search keyword basics

Persist 부적합 후보:

- toast
- modal open
- loading
- error
- API cache 전체
- Form sensitive input
- Auth detail data
- Derived State
- temporary selected state

---

### [실무]

Persistence Scope 판단:

```text
새로고침 후 유지가 필요한가?
→ 비민감 정보인가?
→ URL State가 더 적합하지 않은가?
→ 서버 저장이 더 적합하지 않은가?
→ 최소 field만 persist
```

예시:

```text
theme
→ persist 적합

language
→ persist 적합

toast
→ persist 부적합

search page filter
→ URL State 우선

festivalList cache
→ Server State cache 우선

review content
→ 민감 가능성 있으므로 신중
```

주의:

- Store 전체 persist를 피한다.
- persist schema 변경 시 migration을 고려한다.
- 사용자별 persist data는 logout cleanup을 고려한다.
- persistence는 상태관리 설계의 마지막 단계에서 검토한다.

---

### [FAQ]

Q. 어떤 Store 값을 persist해야 해?
A. 새로고침 후 유지해야 하는 비민감 사용자 설정만 최소한으로 저장하는 것이 좋다.

Q. loading이나 error도 persist해야 해?
A. 보통 필요 없다. loading과 error는 현재 요청 상태이므로 새로고침 후 유지 대상이 아니다.

Q. 검색 조건은 persist보다 URL State가 좋아?
A. 공유와 새로고침 복원이 필요하면 localStorage보다 URL Query String이 더 적합한 경우가 많다.

---

# 17. Store Debugging Rules

## 17.1 Zustand Debugging

### [개념]

Zustand Debugging은 Store 값, action 호출 위치, selector 구독 범위, persist 상태를 확인하는 과정이다.

Zustand는 간단하지만 Store가 커지면 상태 흐름 추적이 어려워질 수 있다.

---

### [핵심]

확인 대상:

- current store value
- action call location
- selector usage
- unnecessary subscription
- persist storage
- reset action
- stale server copy
- derived state duplication
- store boundary

---

### [실무]

Zustand Debug Flow:

```text
UI 문제 발생
→ Store 값 확인
→ Selector가 필요한 값만 구독하는지 확인
→ Action 호출 위치 확인
→ Server State 복사 여부 확인
→ Derived State 저장 여부 확인
→ Persist 값 확인
→ Reset 누락 확인
```

점검 예:

```text
화면에 이전 사용자 알림 수 표시
→ notificationStore reset 여부 확인
→ Query Cache cleanup 확인
→ persist 값 확인
```

주의:

- Store 전체 구독을 피한다.
- API 데이터 stale copy를 확인한다.
- persist된 값이 오래된 상태를 복원할 수 있다.
- logout reset 누락을 확인한다.

---

### [FAQ]

Q. Zustand 상태 문제는 어떻게 디버깅해?
A. Store 값, selector 구독 범위, action 호출 위치, persist 값, reset 누락을 순서대로 확인한다.

Q. Zustand에서 이전 사용자 데이터가 보이면 뭘 확인해?
A. logout reset, user-specific Store cleanup, Query Cache cleanup, persist storage를 확인한다.

Q. Zustand Re-render가 많으면 뭘 확인해?
A. Store 전체 구독 여부와 selector 사용 방식을 먼저 확인한다.

---

## 17.2 Redux Toolkit Debugging

### [개념]

Redux Toolkit Debugging은 Redux DevTools, action history, selector, Slice State를 통해 상태 변경 흐름을 추적하는 과정이다.

Redux Toolkit은 DevTools 기반 추적이 강력한 것이 장점이다.

---

### [핵심]

확인 대상:

- Redux DevTools
- dispatched action
- action payload
- Slice State
- selector result
- reducer update
- reset action
- derived state duplication
- server state copy
- persist storage

---

### [실무]

Redux Debug Flow:

```text
UI 문제 발생
→ Redux DevTools에서 action 확인
→ action payload 확인
→ Slice State 변경 확인
→ selector 결과 확인
→ Derived State 중복 여부 확인
→ Server State copy 여부 확인
→ reset action 누락 확인
```

점검 예:

```text
logout 후 user가 남아 있음
→ clearAuth action dispatch 여부 확인
→ authSlice state 확인
→ 관련 Slice reset 여부 확인
→ Query Cache cleanup 확인
```

주의:

- action이 dispatch되지 않았는지 확인한다.
- reducer가 예상한 State를 변경했는지 확인한다.
- selector가 올바른 값을 반환하는지 확인한다.
- Store에 저장된 Server State가 stale인지 확인한다.
- reset action을 누락하지 않는다.

---

### [FAQ]

Q. Redux Toolkit 상태 문제는 어떻게 디버깅해?
A. Redux DevTools에서 action, payload, Slice State 변화, selector 결과를 순서대로 확인한다.

Q. Redux DevTools의 장점은 뭐야?
A. 어떤 action이 언제 dispatch되었고 State가 어떻게 바뀌었는지 추적할 수 있다.

Q. Redux에서 화면 값이 Store와 다르면 뭘 확인해?
A. selector, Component props, Derived State 계산, Server State 중복 저장 여부를 확인한다.

---

# 18. Global Store Checklist

## 18.1 Zustand Checklist

### [개념]

Zustand Checklist는 Zustand Store 도입 전 적합성을 검수하는 기준이다.

Zustand는 가벼운 Global Store에 적합하지만 Server State나 Derived State 저장소로 사용하면 안 된다.

---

### [핵심]

Checklist:

```md
- [ ] 이 State는 Global Client State인가?
- [ ] Local State로 충분하지 않은가?
- [ ] Shared State로 충분하지 않은가?
- [ ] URL State가 더 적합하지 않은가?
- [ ] Server State가 아닌가?
- [ ] Derived State가 아닌가?
- [ ] Zustand가 Context보다 더 단순한가?
- [ ] Redux Toolkit은 과한가?
- [ ] Store 도메인이 명확한가?
- [ ] action 이름이 명확한가?
- [ ] selector로 필요한 값만 구독하는가?
- [ ] reset action이 있는가?
- [ ] persist 대상이 최소화되었는가?
- [ ] 민감정보 persist가 없는가?
```

---

### [실무]

Zustand 도입 Flow:

```text
Global State 후보 발견
→ State Classification
→ Store Boundary 확인
→ Zustand 적합성 확인
→ Store Type 정의
→ State / Action 작성
→ Selector 사용
→ Reset / Persist 검토
```

결과 예:

```text
auth summary
→ Zustand 가능

global toast
→ Zustand 가능

festival list
→ TanStack Query

search filter
→ URL State

review form input
→ Local State

filtered items
→ Derived Value
```

---

### [FAQ]

Q. Zustand 도입 전에 무엇을 확인해야 해?
A. 해당 State가 Global Client State인지, Server State나 Derived State가 아닌지 먼저 확인해야 한다.

Q. Zustand Checklist에서 가장 중요한 것은 뭐야?
A. Server State를 Zustand에 넣지 않고 selector로 필요한 값만 구독하는 것이다.

Q. Zustand Store에 reset action은 왜 필요해?
A. logout, account switch, feature 종료 시 상태를 안전하게 초기화하기 위해 필요하다.

---

## 18.2 Redux Toolkit Checklist

### [개념]

Redux Toolkit Checklist는 Redux Toolkit 도입 전 적합성을 검수하는 기준이다.

Redux Toolkit은 복잡한 전역 상태와 추적 가능한 상태 흐름이 필요할 때 선택한다.

---

### [핵심]

Checklist:

```md
- [ ] 복잡한 Global State가 필요한가?
- [ ] Local State / Shared State / Context / Zustand로 부족한가?
- [ ] State 변경 흐름 추적이 중요한가?
- [ ] Redux DevTools가 필요한가?
- [ ] 팀 컨벤션이 필요한가?
- [ ] Slice 도메인이 명확한가?
- [ ] action naming이 명확한가?
- [ ] RootState / AppDispatch 타입을 정의했는가?
- [ ] typed hooks를 제공하는가?
- [ ] Server State를 Redux에 저장하지 않는가?
- [ ] Derived State를 selector로 계산하는가?
- [ ] reset action이 있는가?
- [ ] logout 시 관련 Slice reset 기준이 있는가?
```

---

### [실무]

Redux Toolkit 도입 Flow:

```text
Global State 후보 발견
→ Zustand로 충분한지 확인
→ 복잡한 상태 흐름 확인
→ DevTools / 팀 컨벤션 필요 확인
→ configureStore 작성
→ Slice 설계
→ Typed Hooks 작성
→ Selector 작성
→ Reset Strategy 작성
```

결과 예:

```text
복잡한 cart rule
→ Redux Toolkit 검토

단순 theme
→ Context 또는 Zustand

auth summary 단순
→ Context 또는 Zustand 가능

auth lifecycle 복잡
→ Redux Toolkit 가능

API cache
→ TanStack Query 또는 RTK Query
```

---

### [FAQ]

Q. Redux Toolkit 도입 전에 무엇을 확인해야 해?
A. 복잡한 전역 상태 흐름과 DevTools 추적, 팀 컨벤션이 실제로 필요한지 확인해야 한다.

Q. Redux Toolkit Checklist에서 가장 중요한 것은 뭐야?
A. Redux가 필요한 복잡도인지 확인하고 Server State와 Derived State를 Store에 넣지 않는 것이다.

Q. Redux Toolkit보다 Zustand가 나은 경우는 언제야?
A. 전역 상태가 가볍고 코드량을 줄이고 싶으며 복잡한 action history가 필요 없을 때 Zustand가 더 단순할 수 있다.

---

# 19. Part03 Final Review

## 19.1 Part03 Scope Summary

### [개념]

Part03은 Global Store 도구인 Zustand와 Redux Toolkit의 사용 기준, Store 설계, Anti Pattern, 도구 선택 기준을 다룬다.

이 문서는 전역 상태를 무작정 도입하지 않고 State Classification 이후 필요한 경우에만 Store를 선택하도록 지원한다.

---

### [핵심]

Part03 포함 범위:

- Global Store Purpose
- Store State Type
- Store Boundary
- Zustand Purpose
- Zustand Basic Store
- Zustand Selector
- Zustand Store Design
- Zustand Auth Store
- Zustand UI Store
- Zustand Persistence
- Zustand Anti Patterns
- Redux Toolkit Purpose
- configureStore
- Typed Redux Hooks
- createSlice
- Redux Store Design
- Redux Selector
- Redux Anti Patterns
- Zustand vs Redux Toolkit
- Store Reset and Logout
- Store Persistence Security
- Store Debugging
- Global Store Checklist

---

### [실무]

Part03 이후 문서 연결:

```text
Part01 State Classification and Ownership
→ Part02 Context API and useReducer
→ Part03 Zustand and Redux Toolkit
→ Part04 TanStack Query and Server State
→ Part05 Form State and Auth State
→ Part06 State Debugging and Anti Patterns
```

Agent 사용 기준:

```text
User Frontend Global State Request
→ Part01로 State Type과 Owner 판단
→ Part02로 Context/useReducer 가능성 확인
→ Part03으로 Zustand/Redux Toolkit 선택
→ Server State면 Part04로 이동
→ Form/Auth 세부 흐름이면 Part05로 이동
→ 문제 분석이면 Part06으로 이동
```

---

### [FAQ]

Q. Part03의 핵심 목적은 뭐야?
A. Zustand와 Redux Toolkit을 언제 쓰고 언제 쓰지 말아야 하는지 판단하게 하는 것이다.

Q. Part03은 모든 State를 Global Store로 관리하라는 문서야?
A. 아니다. Global Store는 필요한 Client State에만 제한적으로 사용해야 한다.

Q. Part03 다음에는 무엇을 다뤄야 해?
A. Server State와 TanStack Query 기준을 다루는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Global Store는 언제 필요해?
A. 여러 Page나 여러 Feature에서 반복적으로 필요한 Client State가 있고 Local State나 Shared State로 해결하기 어려울 때 필요하다.

Q. 모든 State를 Global Store에 넣으면 편하지 않아?
A. 권장하지 않는다. Store가 커지고 데이터 흐름 추적, reset, persistence, Re-render 관리 비용이 증가한다.

Q. API 응답 데이터도 Global Store에 넣어야 해?
A. 대부분 아니다. API 응답 데이터는 Server State로 보고 TanStack Query 같은 Server State 도구를 우선 검토한다.

Q. Store에 넣어도 되는 State는 뭐야?
A. 여러 Page에서 반복적으로 필요한 Client State, Auth Summary, Global UI State, User Preference 등이 적합하다.

Q. Store에 넣으면 안 되는 State는 뭐야?
A. 단일 Component State, Form 입력값, Server State, Derived State, URL State는 보통 Store에 넣지 않는다.

Q. notification unread count는 Store에 둬도 돼?
A. 여러 화면에서 반복적으로 필요하면 Store 후보가 될 수 있지만 서버 동기화가 중요하면 Query와 함께 설계해야 한다.

Q. Store Boundary가 왜 중요해?
A. Store 책임을 명확히 해야 Server State 중복 저장, Derived State 저장, Form State 전역화 문제를 막을 수 있다.

Q. authStore에 user profile 전체를 넣어도 돼?
A. 사용자 요약 정보는 가능하지만 상세 프로필은 Server State로 관리하는 것이 더 적합할 수 있다.

Q. Store가 커지면 어떻게 해?
A. State Type을 재분류하고 Local, Shared, URL, Server State로 분리한 뒤 Store를 도메인별로 나눈다.

Q. Zustand는 언제 써?
A. Context보다 action과 상태가 많고 Redux Toolkit보다 가벼운 전역 상태가 필요할 때 적합하다.

Q. Zustand는 Redux보다 쉬워?
A. 일반적으로 코드량이 적고 API가 단순해서 작은 전역 Store에는 더 간단하게 사용할 수 있다.

Q. Zustand에 API 데이터를 전부 넣어도 돼?
A. 권장하지 않는다. 서버 데이터 캐싱은 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. Zustand Store는 어떻게 만들어?
A. create 함수로 State field와 Action function을 함께 정의해 Store Hook을 만든다.

Q. Zustand에서 action 함수를 Store 안에 넣어도 돼?
A. 가능하다. Zustand에서는 상태와 상태 변경 함수를 함께 정의하는 방식이 일반적이다.

Q. Zustand Store Hook 이름은 어떻게 지어?
A. useAuthStore, useUiStore, useNotificationStore처럼 도메인 책임을 드러내는 이름이 좋다.

Q. Zustand selector는 왜 써?
A. 필요한 상태만 구독해 불필요한 Re-render를 줄이기 위해 사용한다.

Q. useAuthStore()처럼 전체 Store를 가져오면 안 돼?
A. 가능은 하지만 Store 변경 시 불필요한 Re-render가 늘 수 있어 필요한 값만 선택하는 것이 좋다.

Q. action 함수도 selector로 가져와야 해?
A. 권장된다. Component가 사용하는 action만 선택하면 의존성이 명확해진다.

Q. Zustand에서 여러 값을 가져올 때 어떻게 해?
A. 개별 selector를 사용하거나 필요하면 shallow comparison이 적용된 객체 selector를 검토한다.

Q. 객체 selector는 위험해?
A. 무조건 위험한 것은 아니지만 새 객체 반환으로 Re-render가 늘 수 있어 비교 전략을 고려해야 한다.

Q. Zustand selector를 custom hook으로 감싸도 돼?
A. 가능하다. 반복되는 selector 조합은 custom hook으로 감싸 사용성을 높일 수 있다.

Q. Zustand Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. Store를 하나로 만들면 안 돼?
A. 작은 프로젝트에서는 가능하지만 규모가 커지면 책임이 섞여 유지보수가 어려워질 수 있다.

Q. Store를 너무 잘게 나누면 문제야?
A. 관련 상태가 흩어져 흐름 추적이 어려워질 수 있으므로 책임 단위로 적절히 나누는 것이 좋다.

Q. Auth State는 Zustand에 적합해?
A. 여러 Page에서 필요하고 action이 명확하므로 Zustand authStore에 적합한 경우가 많다.

Q. Auth Store에 access token을 저장해도 돼?
A. 인증 구조와 보안 요구사항에 따라 신중히 결정해야 하며 민감정보 저장은 최소화해야 한다.

Q. logout 시 Auth Store만 초기화하면 돼?
A. 아니다. user-specific cache, notificationStore, 민감한 화면 상태도 함께 초기화해야 할 수 있다.

Q. UI State는 Zustand에 넣어도 돼?
A. 여러 Page에서 제어되는 Global Toast, Sidebar, Global Modal 같은 UI State는 Zustand에 적합할 수 있다.

Q. 단일 modal open도 uiStore에 넣어야 해?
A. 아니다. 특정 Component 내부 modal이면 Local State가 적합하다.

Q. Theme은 Context와 Zustand 중 어디가 좋아?
A. 단순 Theme은 Context로 충분하고 다른 UI Store와 함께 관리하려면 Zustand도 가능하다.

Q. Zustand Persist는 언제 써?
A. 새로고침 후 유지해야 하는 비민감 사용자 설정을 저장할 때 사용한다.

Q. 모든 Store를 persist하면 좋아?
A. 아니다. 필요한 최소 field만 persist해야 한다.

Q. access token을 persist해도 돼?
A. 보안 위험이 있으므로 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. partialize는 왜 필요해?
A. Store 전체가 아니라 필요한 값만 저장해 민감정보와 임시 상태 저장을 방지하기 위해 필요하다.

Q. toast 상태를 persist해야 해?
A. 보통 필요 없다. toast는 임시 UI State이므로 새로고침 후 유지 대상이 아니다.

Q. theme만 persist하고 나머지는 제외할 수 있어?
A. 가능하다. partialize로 저장할 field를 제한할 수 있다.

Q. Zustand Store 하나에 전부 넣으면 안 돼?
A. 작은 프로젝트에서는 가능하지만 규모가 커지면 책임이 섞이고 유지보수가 어려워진다.

Q. Massive Store를 어떻게 줄여?
A. State Type을 재분류하고 authStore, uiStore처럼 책임별로 분리한다.

Q. Zustand Store에 festivalList를 넣으면 안 돼?
A. 서버 API 데이터라면 TanStack Query 같은 Server State 도구가 더 적합하다.

Q. Zustand에 API 데이터를 넣으면 왜 문제야?
A. 서버 데이터 동기화, stale data, refetch, mutation 갱신을 직접 관리해야 해서 복잡해질 수 있다.

Q. API 데이터는 무조건 TanStack Query를 써야 해?
A. 필수는 아니지만 캐시와 동기화가 필요하면 TanStack Query가 더 적합한 경우가 많다.

Q. Zustand와 TanStack Query를 같이 써도 돼?
A. 가능하다. Zustand는 Client Global State, TanStack Query는 Server State를 담당하도록 역할을 분리한다.

Q. Store에 totalPrice를 저장해도 돼?
A. cartItems로 계산 가능하면 저장하지 않고 계산하는 것이 좋다.

Q. selectedItem과 selectedId를 Store에 같이 넣어도 돼?
A. 권장하지 않는다. selectedId만 저장하고 selectedItem은 원본 데이터에서 계산하는 것이 좋다.

Q. Derived State를 Store에 넣으면 왜 위험해?
A. 원본 값과 파생 값이 서로 달라져 데이터 불일치가 생길 수 있다.

Q. Redux Toolkit은 언제 써?
A. 복잡한 전역 상태와 예측 가능한 상태 변경 흐름, DevTools 기반 추적이 필요한 큰 프로젝트에 적합하다.

Q. 작은 프로젝트에도 Redux Toolkit을 써야 해?
A. 필수는 아니다. 작은 프로젝트는 useState, Context, Zustand만으로 충분할 수 있다.

Q. Redux와 Redux Toolkit은 달라?
A. Redux Toolkit은 Redux를 더 쉽게 사용하기 위한 공식 권장 도구다.

Q. Redux connect를 써야 해?
A. 신규 문서에서는 Redux Toolkit과 Hook 기반 사용을 우선한다. 기존 코드 유지보수에서 connect를 볼 수는 있다.

Q. Redux Toolkit에서 state를 직접 바꿔도 돼?
A. createSlice 내부 reducer에서는 Immer가 불변 업데이트로 변환하므로 mutation처럼 작성할 수 있다.

Q. Redux Toolkit을 쓰면 Boilerplate가 줄어?
A. 맞다. createSlice와 configureStore로 기존 Redux보다 코드량이 줄어든다.

Q. configureStore는 뭐야?
A. Redux Toolkit에서 Redux Store를 생성하고 reducer, middleware, DevTools를 설정하는 API다.

Q. RootState는 왜 필요해?
A. useSelector에서 전체 Store State 타입을 안전하게 사용하기 위해 필요하다.

Q. AppDispatch는 왜 필요해?
A. useDispatch를 TypeScript에서 안전하게 사용하기 위해 필요하다.

Q. useAppSelector는 왜 써?
A. RootState 타입을 적용해 Redux State를 TypeScript에서 안전하게 선택하기 위해 사용한다.

Q. useAppDispatch는 왜 써?
A. AppDispatch 타입을 적용해 dispatch 타입을 안전하게 사용하기 위해 필요하다.

Q. 일반 useSelector를 쓰면 안 돼?
A. 가능하지만 TypeScript 프로젝트에서는 typed hook을 사용하는 것이 좋다.

Q. Redux Slice는 뭐야?
A. 특정 도메인의 state, reducer, action을 함께 정의하는 Redux Toolkit 단위다.

Q. Slice는 어떻게 나눠?
A. auth, ui, notification, cart처럼 도메인 책임 기준으로 나눈다.

Q. createSlice 내부에서 state를 직접 수정해도 돼?
A. 가능하다. Redux Toolkit이 Immer로 불변 업데이트를 처리한다.

Q. Redux action 이름은 어떻게 지어?
A. setUser, clearAuth, toggleSidebar처럼 상태 변경 의도를 명확히 드러내는 이름이 좋다.

Q. updateData 같은 이름은 안 좋아?
A. 구체적인 변경 의도를 알기 어렵기 때문에 권장하지 않는다.

Q. action 이름에 도메인명을 항상 넣어야 해?
A. Slice 이름이 도메인을 나타내므로 action 내부 이름은 중복 없이 의도를 드러내면 된다.

Q. Redux Slice는 어떻게 나누는 게 좋아?
A. auth, ui, notification, cart처럼 도메인 책임과 reset 기준에 따라 나누는 것이 좋다.

Q. appSlice 하나로 모든 상태를 관리해도 돼?
A. 권장하지 않는다. 책임이 섞이면 유지보수와 디버깅이 어려워진다.

Q. Slice를 너무 많이 나누면 문제야?
A. 관련 상태 흐름이 흩어질 수 있으므로 책임 기준으로 적절히 나누는 것이 좋다.

Q. Auth State를 Redux Toolkit으로 관리해도 돼?
A. 가능하다. 인증 상태 흐름이 복잡하고 DevTools 추적이 필요하면 Redux Toolkit이 적합할 수 있다.

Q. Auth Slice에 user detail 전체를 넣어도 돼?
A. 사용자 요약 정보는 가능하지만 상세 프로필은 Server State로 관리하는 것이 더 적합할 수 있다.

Q. Auth Slice만으로 권한 보안이 해결돼?
A. 아니다. Frontend 권한 상태는 UX용이고 실제 접근 제어는 Backend에서 반드시 처리해야 한다.

Q. UI State를 Redux에 넣어도 돼?
A. Global Toast, Sidebar, Global Modal처럼 앱 전역에서 제어되는 UI State는 가능하다.

Q. 단일 dropdown open 상태도 Redux에 넣어야 해?
A. 아니다. 특정 Component 내부 dropdown은 Local State가 적합하다.

Q. Toast 상태는 persist해야 해?
A. 보통 필요 없다. Toast는 임시 UI State이므로 새로고침 후 유지할 필요가 없다.

Q. Redux selector는 왜 필요해?
A. Component가 Store 구조에 직접 강하게 의존하지 않도록 하고 필요한 값만 선택하기 위해 필요하다.

Q. selector 없이 state.auth.user를 직접 써도 돼?
A. 가능하지만 여러 곳에서 반복되면 Store 구조 변경에 취약해질 수 있다.

Q. Derived Value를 selector에서 계산해도 돼?
A. 가능하다. 원본 State로 계산 가능한 값은 Store에 저장하지 않고 selector에서 계산하는 것이 좋다.

Q. 모든 Redux selector를 memoize해야 해?
A. 아니다. 단순 값 선택은 일반 selector로 충분하다.

Q. filtered list는 Store에 저장해야 해?
A. 원본 list와 filter 조건으로 계산 가능하면 selector에서 계산하는 것이 좋다.

Q. Memoized Selector는 언제 필요해?
A. filter, sort, group처럼 계산 비용이 있거나 결과 참조 안정성이 필요할 때 검토한다.

Q. Redux Toolkit을 쓰면 무조건 좋은 구조야?
A. 아니다. 단순 상태에는 과할 수 있으며 useState, Context, Zustand가 더 적합할 수 있다.

Q. 모든 UI State를 Redux에 넣어야 해?
A. 아니다. 단일 Component UI State는 Local State가 적합하다.

Q. Redux Overuse는 어떻게 줄여?
A. State Classification을 먼저 수행하고 Local, Shared, URL, Server State로 충분한지 확인한다.

Q. API 데이터를 Redux에 저장하면 안 돼?
A. 가능은 하지만 캐시와 동기화 관리가 복잡해질 수 있어 Server State 도구를 우선 검토하는 것이 좋다.

Q. Redux Toolkit과 TanStack Query를 같이 써도 돼?
A. 가능하다. Redux Toolkit은 Client Global State, TanStack Query는 Server State를 담당하게 분리하면 된다.

Q. RTK Query는 어디에 해당해?
A. Redux Toolkit 생태계의 Server State 데이터 fetching 도구이며 API cache 관리에 사용할 수 있다.

Q. Redux Store에 totalPrice를 저장해도 돼?
A. cartItems로 계산 가능하면 selector에서 계산하는 것이 좋다.

Q. filteredItems를 Slice State에 넣으면 안 돼?
A. 원본 list와 filter 조건으로 계산 가능하면 Store에 저장하지 않는 것이 좋다.

Q. Derived State는 Redux에서 어떻게 처리해?
A. selector 또는 memoized selector로 계산한다.

Q. Zustand와 Redux Toolkit 중 뭐가 좋아?
A. 가볍고 단순한 전역 상태는 Zustand가 편하고, 복잡한 상태 변경 추적과 팀 컨벤션이 필요하면 Redux Toolkit이 적합하다.

Q. 작은 프로젝트에는 Zustand가 더 좋아?
A. 보통 Zustand가 더 단순할 수 있다. 단, 팀 컨벤션이나 DevTools 요구가 크면 Redux Toolkit도 가능하다.

Q. 큰 프로젝트에는 무조건 Redux Toolkit이야?
A. 무조건은 아니지만 복잡한 전역 상태 흐름과 팀 단위 컨벤션이 중요하면 Redux Toolkit이 유리할 수 있다.

Q. 상태관리 도구는 뭘 먼저 써야 해?
A. 먼저 상태 종류와 범위를 분류한 뒤 가장 단순한 도구부터 선택한다.

Q. Zustand와 Redux Toolkit 선택 기준은 뭐야?
A. 가벼운 전역 상태는 Zustand, 복잡한 상태 흐름과 팀 컨벤션이 필요하면 Redux Toolkit이 적합하다.

Q. 도구 선택 전에 반드시 확인할 것은 뭐야?
A. 해당 State가 Server State, URL State, Derived State, Local State로 충분한지 먼저 확인해야 한다.

Q. logout 시 어떤 Store를 초기화해야 해?
A. auth, notification, user-specific Store, 민감한 화면 상태, Query Cache를 함께 검토해야 한다.

Q. Auth Store만 clear하면 충분해?
A. 아닐 수 있다. 사용자별 캐시나 알림 상태가 남으면 다른 사용자에게 잘못 보일 수 있다.

Q. Store reset action은 왜 필요해?
A. logout, token expired, account switch 같은 이벤트에서 상태를 안전하게 초기화하기 위해 필요하다.

Q. User-Specific State는 왜 cleanup해야 해?
A. 로그아웃 후 이전 사용자 데이터가 남거나 계정 전환 시 다른 사용자에게 잘못 보이는 문제를 막기 위해 필요하다.

Q. theme도 logout 때 지워야 해?
A. 보통 비민감 설정이라 유지할 수 있지만 사용자별 설정 정책이면 제거할 수 있다.

Q. Query Cache도 cleanup해야 해?
A. 사용자별 API 데이터가 포함되어 있으면 logout 또는 account switch 시 clear 또는 invalidate를 검토해야 한다.

Q. localStorage에 token을 저장해도 돼?
A. 보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. Persist Store에 민감정보를 넣으면 왜 위험해?
A. XSS 등으로 JavaScript 접근 저장소의 값이 노출될 수 있기 때문이다.

Q. 비밀번호 입력값을 persist해도 돼?
A. 안 된다. password 같은 민감 입력값은 persist하지 않는다.

Q. 어떤 Store 값을 persist해야 해?
A. 새로고침 후 유지해야 하는 비민감 사용자 설정만 최소한으로 저장하는 것이 좋다.

Q. loading이나 error도 persist해야 해?
A. 보통 필요 없다. loading과 error는 현재 요청 상태이므로 새로고침 후 유지 대상이 아니다.

Q. 검색 조건은 persist보다 URL State가 좋아?
A. 공유와 새로고침 복원이 필요하면 localStorage보다 URL Query String이 더 적합한 경우가 많다.

Q. Zustand 상태 문제는 어떻게 디버깅해?
A. Store 값, selector 구독 범위, action 호출 위치, persist 값, reset 누락을 순서대로 확인한다.

Q. Zustand에서 이전 사용자 데이터가 보이면 뭘 확인해?
A. logout reset, user-specific Store cleanup, Query Cache cleanup, persist storage를 확인한다.

Q. Zustand Re-render가 많으면 뭘 확인해?
A. Store 전체 구독 여부와 selector 사용 방식을 먼저 확인한다.

Q. Redux Toolkit 상태 문제는 어떻게 디버깅해?
A. Redux DevTools에서 action, payload, Slice State 변화, selector 결과를 순서대로 확인한다.

Q. Redux DevTools의 장점은 뭐야?
A. 어떤 action이 언제 dispatch되었고 State가 어떻게 바뀌었는지 추적할 수 있다.

Q. Redux에서 화면 값이 Store와 다르면 뭘 확인해?
A. selector, Component props, Derived State 계산, Server State 중복 저장 여부를 확인한다.

Q. Zustand 도입 전에 무엇을 확인해야 해?
A. 해당 State가 Global Client State인지, Server State나 Derived State가 아닌지 먼저 확인해야 한다.

Q. Zustand Checklist에서 가장 중요한 것은 뭐야?
A. Server State를 Zustand에 넣지 않고 selector로 필요한 값만 구독하는 것이다.

Q. Zustand Store에 reset action은 왜 필요해?
A. logout, account switch, feature 종료 시 상태를 안전하게 초기화하기 위해 필요하다.

Q. Redux Toolkit 도입 전에 무엇을 확인해야 해?
A. 복잡한 전역 상태 흐름과 DevTools 추적, 팀 컨벤션이 실제로 필요한지 확인해야 한다.

Q. Redux Toolkit Checklist에서 가장 중요한 것은 뭐야?
A. Redux가 필요한 복잡도인지 확인하고 Server State와 Derived State를 Store에 넣지 않는 것이다.

Q. Redux Toolkit보다 Zustand가 나은 경우는 언제야?
A. 전역 상태가 가볍고 코드량을 줄이고 싶으며 복잡한 action history가 필요 없을 때 Zustand가 더 단순할 수 있다.

Q. Part03의 핵심 목적은 뭐야?
A. Zustand와 Redux Toolkit을 언제 쓰고 언제 쓰지 말아야 하는지 판단하게 하는 것이다.

Q. Part03은 모든 State를 Global Store로 관리하라는 문서야?
A. 아니다. Global Store는 필요한 Client State에만 제한적으로 사용해야 한다.

Q. Part03 다음에는 무엇을 다뤄야 해?
A. Server State와 TanStack Query 기준을 다루는 것이 좋다.

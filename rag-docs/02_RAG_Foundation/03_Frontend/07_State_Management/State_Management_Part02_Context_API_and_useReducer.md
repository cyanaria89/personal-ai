# State Management Part02 - Context API and useReducer

---

# 1. Context API Overview

## 1.1 Context API Purpose

### [개념]

Context API는 Component Tree 아래로 값을 직접 전달하지 않고 하위 Component들이 공유 값을 읽을 수 있게 하는 React 기능이다.

Context API는 Props Drilling을 줄일 수 있지만 모든 State를 넣는 전역 상태관리 도구는 아니다.

Context API는 주로 변경 빈도가 낮고 여러 하위 Component에서 반복적으로 필요한 값을 공급할 때 사용한다.

---

### [핵심]

Context API 핵심 목적:

- Component Tree 값 공유
- Props Drilling 완화
- Provider 기반 값 공급
- useContext 기반 값 소비
- Theme 공유
- Auth Summary 공유
- Language 공유
- App Config 공유
- Layout Preference 공유
- Low Frequency Shared State 관리

---

### [실무]

2026 실무 기준에서 Context API는 아래 상황에 적합하다.

```text
값이 여러 하위 Component에서 필요함
→ Props 전달이 반복됨
→ 값 변경 빈도가 낮음
→ 복잡한 action이 많지 않음
→ Context API 검토
```

Context API는 아래 State에 적합하다.

```text
theme
language
auth summary
app config
layout preference
feature flag
low-frequency shared state
```

Context API는 아래 State에 부적합하다.

```text
자주 바뀌는 input value
대량 API list cache
복잡한 Form State 전체
빠르게 변경되는 pagination data
mutation이 많은 complex domain state
Server State cache 전체
```

---

### [FAQ]

Q. Context API는 뭐야?
A. Component Tree 아래로 Props를 계속 전달하지 않고 하위 Component들이 공유 값을 읽을 수 있게 하는 React 기능이다.

Q. Context API는 전역 상태관리야?
A. 전역처럼 값을 공유할 수 있지만 상태관리 라이브러리라기보다 Component Tree에 값을 공급하는 React 기능에 가깝다.

Q. Context API는 언제 써?
A. Theme, Auth Summary, Language처럼 여러 하위 Component에서 반복적으로 필요한 값을 전달할 때 사용한다.

---

# 2. Context API Basic Structure

## 2.1 createContext and Provider

### [개념]

createContext는 Context 객체를 생성하고 Provider는 하위 Component Tree에 값을 공급한다.

Provider 하위 Component는 useContext를 통해 Provider value를 읽을 수 있다.

---

### [핵심]

Context 기본 구성:

- createContext
- Provider
- value
- useContext
- Custom Hook
- Provider 위치
- Consumer Component
- Context Value Type
- Default Value
- Null Guard

---

### [실무]

기본 구조 예:

```jsx
const ThemeContext = createContext(null);

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

사용 예:

```jsx
function ThemeToggleButton() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
      Toggle Theme
    </button>
  );
}
```

권장 기준:

- Context는 역할별로 분리한다.
- Provider 위치를 명확히 정한다.
- value 구조를 작게 유지한다.
- Provider value 변경 시 Re-render 범위를 고려한다.
- useContext 직접 사용보다 Custom Hook으로 감싸는 것을 권장한다.

---

### [FAQ]

Q. createContext는 뭐야?
A. 하위 Component에 공유 값을 제공하기 위한 Context 객체를 만드는 React API다.

Q. Provider는 뭐야?
A. Context 값을 하위 Component Tree에 공급하는 Component다.

Q. useContext는 뭐야?
A. Provider가 공급한 Context value를 읽기 위한 React Hook이다.

---

## 2.2 Context Provider Placement

### [개념]

Context Provider Placement는 Provider를 Component Tree의 어느 위치에 둘지 결정하는 기준이다.

Provider는 Context 값이 필요한 범위를 감싸야 하지만 필요 이상으로 넓게 두면 Re-render 범위와 의존성이 커질 수 있다.

---

### [핵심]

Provider 위치 판단 기준:

- 값을 읽는 Component 범위
- 값을 변경하는 Component 범위
- 여러 Page에서 필요한지 여부
- 특정 Feature 내부만 필요한지 여부
- Auth / Theme처럼 App 전체 대상인지 여부
- Provider 중첩 복잡도
- Re-render 영향 범위

---

### [실무]

Provider Placement Flow:

```text
Context Value 발견
→ 값을 읽는 Component 확인
→ 값을 변경하는 Component 확인
→ 필요한 가장 좁은 Tree 범위 확인
→ 해당 범위의 공통 부모에 Provider 배치
→ App 전체 필요 여부 확인
```

예시:

```text
theme
→ 전체 App에서 필요
→ App Root 근처 Provider

language
→ 전체 App에서 필요
→ App Root 근처 Provider

festival filter context
→ Festival Feature 내부에서만 필요
→ FestivalPage 또는 FestivalLayout Provider

modal context
→ 전역 modal이면 App Root
→ 특정 Page modal이면 Page 내부
```

주의:

- 모든 Provider를 무조건 App 최상단에 두지 않는다.
- Feature 내부 전용 Context는 Feature Root에 둔다.
- Provider 범위가 넓을수록 값 변경 영향 범위가 커진다.
- Provider Hell이 생기면 Provider Composition을 검토한다.

---

### [FAQ]

Q. Context Provider는 어디에 둬야 해?
A. Context 값을 사용하는 Component들을 포함하는 가장 좁은 공통 부모에 두는 것이 기본이다.

Q. 모든 Provider를 App 최상단에 둬도 돼?
A. 권장하지 않는다. App 전체에서 필요한 값만 Root 근처에 두고 Feature 전용 값은 Feature 내부에 두는 것이 좋다.

Q. Provider 위치가 너무 넓으면 어떤 문제가 생겨?
A. 불필요한 의존성이 생기고 value 변경 시 Re-render 영향 범위가 커질 수 있다.

---

# 3. Context Custom Hook Rules

## 3.1 Context Custom Hook Purpose

### [개념]

Context Custom Hook은 Context 사용 코드를 안전하고 일관되게 감싸는 Custom Hook이다.

useContext를 직접 여러 곳에서 호출하는 대신 전용 Hook을 제공하면 Provider 누락 검증과 사용 API 통일이 쉬워진다.

---

### [핵심]

Context Custom Hook 목적:

- useContext 직접 사용 숨김
- Provider 누락 감지
- Context 사용 API 통일
- TypeScript 타입 안정성 강화
- Error Message 명확화
- 재사용성 향상
- 테스트 편의성 향상

---

### [실무]

TypeScript 예:

```tsx
type AuthContextValue = {
  authenticated: boolean;
  user: {
    userId: number;
    nickname: string;
    role: "ROLE_USER" | "ROLE_ADMIN";
  } | null;
  logout: () => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return context;
}
```

권장 기준:

- Context마다 전용 Hook을 제공한다.
- Hook 이름은 use로 시작한다.
- Provider 외부 사용 오류를 명확히 처리한다.
- Context 기본값은 null로 두고 Hook에서 검사할 수 있다.
- Hook 반환 타입을 명확히 유지한다.

---

### [FAQ]

Q. Context Custom Hook은 왜 필요해?
A. Provider 누락 검증, 사용 API 통일, 타입 안정성 강화를 위해 필요하다.

Q. useContext를 직접 쓰면 안 돼?
A. 가능하지만 Custom Hook으로 감싸면 Provider 누락 오류를 명확히 처리할 수 있다.

Q. Context 기본값은 null로 둬도 돼?
A. 가능하다. 대신 Custom Hook에서 null을 검사해 Provider 누락 오류를 명확히 처리해야 한다.

---

## 3.2 Context Custom Hook Naming

### [개념]

Context Custom Hook Naming은 Context를 사용하는 Hook 이름을 일관되게 정하는 규칙이다.

Hook 이름은 Context의 역할을 명확히 드러내야 한다.

---

### [핵심]

Naming 예:

- AuthContext → useAuth
- ThemeContext → useTheme
- LanguageContext → useLanguage
- ToastContext → useToast
- ModalContext → useModal
- LayoutContext → useLayout
- FeatureFlagContext → useFeatureFlag

---

### [실무]

권장 Naming:

```text
Context Name
→ AuthContext
→ ThemeContext
→ NotificationContext

Hook Name
→ useAuth
→ useTheme
→ useNotification
```

피해야 할 Naming:

```text
useContextValue
useGlobal
useCommon
useData
useStateValue
```

주의:

- Hook 이름은 역할 중심으로 작성한다.
- Store Hook과 이름 충돌을 피한다.
- Auth Store를 Zustand로 쓰는 경우 `useAuthStore`, Context는 `useAuthContext`처럼 구분할 수 있다.
- 불명확한 common, global, data 표현을 피한다.

---

### [FAQ]

Q. Context Hook 이름은 어떻게 지어?
A. useAuth, useTheme처럼 Context의 역할을 드러내는 이름이 좋다.

Q. useGlobal 같은 이름은 괜찮아?
A. 권장하지 않는다. 어떤 상태를 제공하는지 알기 어렵기 때문이다.

Q. Zustand Store Hook과 Context Hook 이름이 겹치면 어떻게 해?
A. useAuthStore, useAuthContext처럼 역할이나 구현 방식을 이름에 반영해 구분한다.

---

# 4. Context Value Design

## 4.1 Context Value Structure

### [개념]

Context Value Structure는 Provider가 하위 Component에 공급하는 값의 구조를 설계하는 기준이다.

Context value가 너무 크거나 자주 바뀌면 구독 Component의 Re-render가 증가할 수 있다.

---

### [핵심]

Context Value 설계 요소:

- state value
- setter function
- action function
- derived value
- stable function
- memoization
- value object size
- responsibility boundary

---

### [실무]

단순 Context Value 예:

```tsx
type ThemeContextValue = {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
};
```

Auth Context Value 예:

```tsx
type AuthContextValue = {
  authenticated: boolean;
  user: AuthUser | null;
  login: (user: AuthUser) => void;
  logout: () => void;
};
```

권장 기준:

- Context value는 작게 유지한다.
- 관련 없는 상태를 하나의 Context에 넣지 않는다.
- 자주 바뀌는 값과 거의 바뀌지 않는 값을 분리한다.
- Derived State를 value에 과도하게 넣지 않는다.
- action 함수 이름은 의도를 드러내게 작성한다.
- 필요하면 Context를 역할별로 나눈다.

---

### [FAQ]

Q. Context value에는 무엇을 넣어?
A. 하위 Component가 실제로 필요한 상태값과 변경 함수만 넣는 것이 좋다.

Q. Context value를 큰 객체로 만들어도 돼?
A. 권장하지 않는다. value가 커질수록 불필요한 의존성과 Re-render 문제가 생길 수 있다.

Q. Context에 여러 도메인 상태를 같이 넣어도 돼?
A. 권장하지 않는다. auth, theme, language처럼 역할별로 분리하는 것이 좋다.

---

## 4.2 State Context and Action Context Split

### [개념]

State Context and Action Context Split은 상태값 Context와 변경 함수 Context를 분리하는 패턴이다.

상태값을 읽는 Component와 action만 호출하는 Component의 Re-render 영향을 줄이는 데 도움이 될 수 있다.

---

### [핵심]

분리 대상:

- State Context
- Action Context
- Read Component
- Write Component
- Re-render Boundary
- Provider Composition
- Context Value Stability

---

### [실무]

분리 예:

```tsx
const AuthStateContext = createContext<AuthState | null>(null);
const AuthActionContext = createContext<AuthActions | null>(null);

function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(authReducer, initialAuthState);

  const actions = useMemo(
    () => ({
      login: (user) => dispatch({ type: "LOGIN", payload: user }),
      logout: () => dispatch({ type: "LOGOUT" }),
    }),
    [],
  );

  return (
    <AuthStateContext.Provider value={state}>
      <AuthActionContext.Provider value={actions}>
        {children}
      </AuthActionContext.Provider>
    </AuthStateContext.Provider>
  );
}
```

사용 기준:

```text
action만 필요한 Component가 많음
→ Action Context 분리 검토

state 변경이 잦음
→ State Context 구독 범위 축소 검토

Context value가 커짐
→ Context 분리 검토
```

주의:

- 작은 Context에는 과한 구조일 수 있다.
- 성능 문제를 측정하기 전 과도하게 복잡하게 만들지 않는다.
- Context 분리보다 Zustand 같은 selector 기반 Store가 더 적합할 수 있다.

---

### [FAQ]

Q. State Context와 Action Context를 왜 나눠?
A. action만 필요한 Component가 State 변경으로 Re-render되는 범위를 줄이기 위해 나눌 수 있다.

Q. 항상 State Context와 Action Context를 나눠야 해?
A. 아니다. 작은 Context에서는 불필요하게 복잡해질 수 있으므로 필요할 때만 적용한다.

Q. Context 분리 대신 Zustand를 써도 돼?
A. 가능하다. 상태와 action이 많고 selector 기반 구독이 필요하면 Zustand가 더 단순할 수 있다.

---

# 5. Context Performance Caution

## 5.1 Context Re-render Problem

### [개념]

Context Re-render Problem은 Provider value가 변경될 때 해당 Context를 구독하는 Component들이 다시 렌더링될 수 있는 문제다.

Context 자체가 느린 것이 아니라 value 설계와 구독 범위가 중요하다.

---

### [핵심]

Re-render 원인:

- Provider value 객체가 매 렌더링마다 새로 생성됨
- 자주 바뀌는 상태를 큰 Context에 넣음
- 많은 Component가 같은 Context를 구독함
- 관련 없는 상태가 하나의 Context에 섞임
- Context Provider 범위가 너무 넓음
- 대량 데이터가 Context value에 포함됨

---

### [실무]

주의 예:

```jsx
<AuthContext.Provider value={{ user, login, logout }}>
  {children}
</AuthContext.Provider>
```

개선 후보:

```text
Context value memoization 고려
Context 역할별 분리
Provider 범위 축소
자주 바뀌는 State 분리
대량 Server State는 TanStack Query로 이동
복잡한 Global State는 Zustand / Redux Toolkit 검토
```

주의:

- memoization을 무조건 먼저 적용하지 않는다.
- 실제 성능 문제가 있을 때 측정 후 개선한다.
- Context 자체보다 value 설계가 중요하다.
- Context는 selector 기반 구독이 기본 제공되지 않는다.
- 자주 변경되는 값은 전용 Store를 검토한다.

---

### [FAQ]

Q. Context를 쓰면 무조건 성능 문제가 생겨?
A. 아니다. 하지만 큰 value나 자주 바뀌는 상태를 많은 Component가 구독하면 Re-render 문제가 생길 수 있다.

Q. Context 성능 문제는 어떻게 줄여?
A. Context를 역할별로 분리하고 Provider 범위를 줄이며 자주 바뀌는 상태는 전용 Store를 검토한다.

Q. Context value에 API 목록 데이터를 넣어도 돼?
A. 권장하지 않는다. API 목록 데이터는 Server State로 보고 TanStack Query 같은 도구를 검토하는 것이 좋다.

---

## 5.2 Context Memoization Rules

### [개념]

Context Memoization은 Provider value의 불필요한 객체 재생성을 줄이기 위해 useMemo, useCallback을 검토하는 방식이다.

Memoization은 성능 문제를 해결하는 도구이지 기본적으로 모든 Context에 적용해야 하는 규칙은 아니다.

---

### [핵심]

Memoization 대상:

- Provider value object
- action function
- callback function
- derived context value
- expensive computation
- stable reference

---

### [실무]

예:

```tsx
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");

  const value = useMemo(
    () => ({
      theme,
      setTheme,
    }),
    [theme],
  );

  return (
    <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
  );
}
```

검토 기준:

```text
Provider가 자주 렌더링됨
→ value object가 매번 새로 생성됨
→ Context Consumer Re-render 확인
→ useMemo / useCallback 검토
```

주의:

- useMemo는 성능 보장 도구가 아니다.
- dependency array를 정확히 작성해야 한다.
- 불필요한 memoization은 코드 복잡도를 높인다.
- Context 구조가 잘못된 경우 memoization보다 Context 분리가 우선일 수 있다.

---

### [FAQ]

Q. Context value에는 항상 useMemo를 써야 해?
A. 아니다. 성능 문제가 있거나 value reference 안정성이 필요할 때 검토한다.

Q. useMemo를 쓰면 Context Re-render가 완전히 사라져?
A. 아니다. value에 포함된 상태가 바뀌면 해당 Context를 구독하는 Component는 다시 렌더링될 수 있다.

Q. Context 성능 최적화의 우선순위는 뭐야?
A. 먼저 Context 역할과 범위를 분리하고, 그 다음 memoization을 검토하는 것이 좋다.

---

# 6. Context API Use Cases

## 6.1 Theme Context

### [개념]

Theme Context는 light mode, dark mode, system theme 같은 UI 테마 값을 하위 Component에 공급하는 Context다.

Theme은 여러 Component에서 필요하고 변경 빈도가 낮기 때문에 Context API에 적합한 대표 사례다.

---

### [핵심]

Theme Context 구성:

- theme
- setTheme
- toggleTheme
- system theme
- localStorage persistence
- CSS class relation
- design token relation

---

### [실무]

Theme Context 예:

```tsx
type Theme = "light" | "dark";

type ThemeContextValue = {
  theme: Theme;
  toggleTheme: () => void;
};

const ThemeContext = createContext<ThemeContextValue | null>(null);

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState<Theme>("light");

  function toggleTheme() {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

권장 기준:

- Theme은 App Root 근처 Provider에 둘 수 있다.
- 새로고침 유지가 필요하면 localStorage를 검토한다.
- CSS class, CSS variable, design token과 연결할 수 있다.
- 민감정보가 아니므로 persistence 대상이 될 수 있다.
- 너무 많은 UI State를 Theme Context에 섞지 않는다.

---

### [FAQ]

Q. Theme은 Context API에 적합해?
A. 적합하다. Theme은 여러 Component에서 필요하고 변경 빈도가 낮은 대표적인 Context 사용 사례다.

Q. Theme을 localStorage에 저장해도 돼?
A. 가능하다. Theme은 비민감 사용자 설정이므로 새로고침 후 유지가 필요하면 저장할 수 있다.

Q. Theme Context에 sidebar 상태도 같이 넣어도 돼?
A. 권장하지 않는다. theme과 layout state는 책임이 다르므로 분리하는 것이 좋다.

---

## 6.2 Auth Context

### [개념]

Auth Context는 인증 여부와 사용자 요약 정보를 여러 Component에 공급하는 Context다.

Auth State는 여러 페이지에서 필요하므로 Context 또는 Global Store 후보가 된다.

---

### [핵심]

Auth Context 구성:

- authenticated
- auth loading
- user summary
- role
- login
- logout
- refresh
- protected route
- reset user cache

---

### [실무]

Auth Context 예:

```tsx
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthContextValue = {
  authenticated: boolean;
  loading: boolean;
  user: AuthUser | null;
  logout: () => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);
```

Auth Context 적합 조건:

```text
인증 여부를 여러 Page에서 읽음
Header / Layout / Protected Route에서 사용
사용자 요약 정보만 필요
action이 단순함
변경 빈도가 낮음
```

Zustand 또는 Redux Toolkit 검토 조건:

```text
Auth action이 많음
refresh lifecycle이 복잡함
여러 Store reset이 필요함
selector 기반 구독이 필요함
전역 상태 흐름 추적이 중요함
```

주의:

- Frontend Auth State는 UX용이다.
- 실제 인증/인가는 Backend에서 검증해야 한다.
- JWT 존재만으로 완전히 신뢰하지 않는다.
- 민감정보를 Context나 localStorage에 과도하게 저장하지 않는다.
- logout 시 user-specific cache reset을 고려한다.

---

### [FAQ]

Q. Auth State는 Context로 관리해도 돼?
A. 가능하다. 인증 여부와 사용자 요약 정보가 단순하면 Auth Context가 적합할 수 있다.

Q. Auth Context와 Zustand authStore 중 뭐가 좋아?
A. 단순 인증 상태는 Context로 충분할 수 있고 action과 reset 흐름이 복잡하면 Zustand를 검토할 수 있다.

Q. Auth Context만 있으면 보안이 돼?
A. 아니다. Frontend Auth State는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

---

## 6.3 Language Context

### [개념]

Language Context는 현재 언어 설정과 언어 변경 함수를 하위 Component에 공급하는 Context다.

Language는 여러 화면에서 필요하고 변경 빈도가 낮아 Context API에 적합하다.

---

### [핵심]

Language Context 구성:

- language
- setLanguage
- locale
- translation dictionary relation
- date format relation
- number format relation
- persistence
- i18n library relation

---

### [실무]

Language Context 판단:

```text
다국어 지원 필요
→ 현재 language를 여러 Component가 참조
→ language 변경 빈도 낮음
→ Context API 적합
```

권장 기준:

- language 값은 App Root 근처에서 관리할 수 있다.
- 새로고침 후 유지가 필요하면 localStorage를 검토한다.
- 번역 데이터 전체를 무거운 Context value로 넣지 않는다.
- i18n library 사용 시 Provider 구조와 중복되지 않게 설계한다.
- date format, currency format과 연결할 수 있다.

---

### [FAQ]

Q. Language는 Context API에 적합해?
A. 적합하다. 여러 Component에서 필요하고 변경 빈도가 낮은 설정값이기 때문이다.

Q. 번역 데이터 전체를 Context에 넣어도 돼?
A. 권장하지 않는다. 무거운 데이터는 별도 i18n 도구나 모듈로 관리하는 것이 좋다.

Q. Language도 localStorage에 저장할 수 있어?
A. 가능하다. 비민감 사용자 설정이므로 새로고침 후 유지가 필요하면 저장할 수 있다.

---

# 7. Context API Anti Patterns

## 7.1 Overused Context

### [개념]

Overused Context는 Local State나 Shared State로 충분한 값을 Context에 과도하게 넣는 문제다.

Context 남용은 전역 상태 남용과 비슷하게 데이터 흐름을 불필요하게 복잡하게 만든다.

---

### [핵심]

문제:

- Context가 너무 커짐
- 관련 없는 State가 섞임
- Provider 위치가 너무 넓어짐
- Consumer Re-render 증가
- Component 재사용성 저하
- State Owner 불명확
- Server State와 Client State 혼합

원인:

- Props 전달을 모두 문제로 판단
- State Classification 생략
- Context를 전역 Store처럼 사용
- Form State를 Context에 넣음
- API cache를 Context에 넣음
- Derived State를 Context에 넣음

---

### [실무]

Overused Context Debug Flow:

```text
Context Value Review
→ State Type 확인
→ Local State 가능 여부 확인
→ Shared State 가능 여부 확인
→ Server State 여부 확인
→ Derived State 여부 확인
→ Context Split 또는 State Relocation
```

잘못된 예:

```text
AppContext
- user
- theme
- searchKeyword
- festivalList
- reviewFormContent
- filteredFestivalList
- modalOpen
```

개선 예:

```text
AuthContext
- user summary
- authenticated

ThemeContext
- theme

URL State
- searchKeyword

TanStack Query
- festivalList

ReviewForm Local State
- reviewFormContent

Derived Value
- filteredFestivalList
```

---

### [FAQ]

Q. Context에 모든 상태를 넣으면 안 돼?
A. 권장하지 않는다. Context가 커지면 Re-render와 유지보수 문제가 커질 수 있다.

Q. Context가 너무 커졌으면 어떻게 해?
A. State Type을 다시 분류하고 Local State, URL State, Server State, 별도 Store로 분리한다.

Q. API 응답 데이터를 Context에 넣어도 돼?
A. 권장하지 않는다. API 응답 데이터는 Server State로 보고 TanStack Query 같은 도구를 검토하는 것이 좋다.

---

## 7.2 Context as Global Store Problem

### [개념]

Context as Global Store Problem은 Context를 복잡한 전역 Store처럼 사용하면서 action, side effect, server cache, derived state를 모두 넣는 문제다.

Context는 값 공급 기능이며 복잡한 상태 변경 추적과 selector 기반 구독을 기본 제공하지 않는다.

---

### [핵심]

문제 증상:

- Context value가 거대한 객체가 됨
- reducer와 action이 과도하게 많아짐
- side effect가 Provider 내부에 집중됨
- Consumer가 필요 없는 값까지 구독함
- Debugging이 어려움
- State 변경 추적이 어려움
- Server State와 Client State가 혼합됨

---

### [실무]

전환 검토 기준:

```text
Context action이 많아짐
→ Zustand 검토

상태 변경 흐름 추적이 중요함
→ Redux Toolkit 검토

API cache와 refetch가 필요함
→ TanStack Query 검토

Form State가 복잡함
→ React Hook Form 검토

State Machine 성격이 강함
→ Advanced State Management 검토
```

주의:

- 작은 규모의 Context + useReducer는 가능하다.
- 복잡도가 커지면 전용 도구가 더 적합하다.
- Context만으로 모든 상태관리 요구를 해결하려 하지 않는다.

---

### [FAQ]

Q. Context를 Global Store처럼 써도 돼?
A. 작은 규모에서는 가능하지만 복잡한 전역 상태와 많은 action이 있으면 Zustand나 Redux Toolkit이 더 적합할 수 있다.

Q. Context와 Zustand의 차이는 뭐야?
A. Context는 값을 공급하는 React 기능이고 Zustand는 selector 기반 구독과 action을 가진 전역 상태 Store다.

Q. Context가 복잡해지면 언제 다른 도구로 바꿔?
A. action이 많아지고 Re-render 제어, 상태 추적, 도메인 분리가 필요해질 때 전용 Store를 검토한다.

---

# 8. useReducer Overview

## 8.1 useReducer Purpose

### [개념]

useReducer는 여러 상태 전환을 action 기반으로 관리하는 React Hook이다.

복잡한 Local State, 복잡한 Form State, Step State, 작은 규모의 Context State에 사용할 수 있다.

---

### [핵심]

useReducer 사용 대상:

- 복잡한 상태 전환
- 여러 action type
- 상태 변경 규칙 명확화
- Form State
- Step State
- Local UI State Machine Basics
- useState가 많아진 Component
- Context Provider 내부 상태
- predictable local transition

---

### [실무]

useReducer 판단 Flow:

```text
State가 여러 개로 늘어남
→ 상태 변경 규칙이 action 단위로 명확함
→ 이전 상태 기반 업데이트가 많음
→ reset / submit / validate 같은 전환 존재
→ useReducer 검토
```

useReducer 적합 예:

```text
검색 조건 Form
다단계 Wizard Form
복잡한 filter panel
장바구니 local draft
modal step flow
복잡한 local UI state
Auth Context 내부 간단 reducer
```

useReducer 부적합 예:

```text
단순 boolean
단순 input value
단순 tab 선택
API cache 관리
전역 복잡 상태 전체
Server State 관리
```

---

### [FAQ]

Q. useReducer는 언제 써?
A. 상태 필드가 많고 변경 규칙이 action 단위로 명확할 때 사용한다.

Q. useState와 useReducer 중 뭐가 좋아?
A. 단순 상태는 useState가 좋고, 상태 전환이 복잡하면 useReducer가 적합하다.

Q. useReducer는 전역 상태관리 도구야?
A. 아니다. React Hook이며 Local State나 Context 내부 상태 전환을 구조화할 때 사용한다.

---

# 9. useReducer Basic Structure

## 9.1 Reducer Function

### [개념]

Reducer Function은 현재 state와 action을 받아 다음 state를 반환하는 순수 함수다.

Reducer는 상태 변경 규칙을 한 곳에 모아 예측 가능한 전환을 만든다.

---

### [핵심]

Reducer 구성:

- state
- action
- action.type
- action.payload
- switch
- return next state
- initialState
- pure function
- immutable update

---

### [실무]

기본 예:

```jsx
const initialState = {
  keyword: "",
  region: "",
};

function reducer(state, action) {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload };
    case "SET_REGION":
      return { ...state, region: action.payload };
    case "RESET":
      return initialState;
    default:
      return state;
  }
}
```

사용 예:

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

Reducer 작성 기준:

- reducer는 순수 함수로 작성한다.
- reducer 내부에서 API 호출을 하지 않는다.
- 기존 state를 직접 변경하지 않는다.
- action type은 의도를 드러내게 작성한다.
- default case 처리 기준을 통일한다.
- initialState를 명확히 분리한다.

---

### [FAQ]

Q. reducer는 뭐야?
A. 현재 state와 action을 받아 다음 state를 반환하는 순수 함수다.

Q. reducer 안에서 API 호출해도 돼?
A. 권장하지 않는다. reducer는 순수 함수로 유지하고 API 호출은 외부에서 처리해야 한다.

Q. reducer에서 state를 직접 변경해도 돼?
A. 일반 useReducer reducer에서는 직접 변경하지 말고 새 객체를 반환해야 한다.

---

## 9.2 Action Object

### [개념]

Action Object는 상태 변경 의도를 표현하는 객체다.

Action은 reducer에게 어떤 상태 전환을 수행해야 하는지 전달한다.

---

### [핵심]

Action 구성:

- type
- payload
- action naming
- discriminated union
- reducer switch
- default case
- action creator
- event handler dispatch

---

### [실무]

Action 예:

```tsx
type SearchAction =
  | { type: "SET_KEYWORD"; payload: string }
  | { type: "SET_REGION"; payload: string }
  | { type: "SET_PAGE"; payload: number }
  | { type: "RESET" };
```

Dispatch 예:

```tsx
dispatch({ type: "SET_KEYWORD", payload: event.target.value });
dispatch({ type: "RESET" });
```

Action Naming 기준:

```text
SET_KEYWORD
SET_REGION
RESET_FORM
SUBMIT_START
SUBMIT_SUCCESS
SUBMIT_FAILURE
OPEN_MODAL
CLOSE_MODAL
NEXT_STEP
PREV_STEP
```

주의:

- action type 문자열 오타를 줄인다.
- payload 타입을 명확히 한다.
- 너무 추상적인 UPDATE, CHANGE만 남용하지 않는다.
- action은 상태 변경 의도를 표현해야 한다.

---

### [FAQ]

Q. useReducer action type은 어떻게 지어?
A. SET_KEYWORD, RESET_FORM처럼 상태 변경 의도를 드러내는 이름이 좋다.

Q. action payload는 뭐야?
A. 상태 변경에 필요한 추가 데이터다.

Q. action type을 UPDATE로만 통일해도 돼?
A. 권장하지 않는다. 변경 의도가 불명확해져 reducer 추적이 어려워질 수 있다.

---

# 10. useReducer with TypeScript

## 10.1 TypeScript Reducer Type

### [개념]

TypeScript Reducer Type은 state와 action의 타입을 명확히 정의해 잘못된 상태 변경을 방지하는 방식이다.

useReducer는 action type별 payload 구조가 다르기 때문에 Discriminated Union과 잘 어울린다.

---

### [핵심]

TypeScript 구성:

- State Type
- Action Union
- Payload Type
- Discriminated Union
- Reducer Return Type
- Exhaustive Check
- Dispatch Type
- Initial State Type

---

### [실무]

TypeScript 예:

```tsx
type SearchState = {
  keyword: string;
  region: string;
  page: number;
};

type SearchAction =
  | { type: "SET_KEYWORD"; payload: string }
  | { type: "SET_REGION"; payload: string }
  | { type: "SET_PAGE"; payload: number }
  | { type: "RESET" };

const initialState: SearchState = {
  keyword: "",
  region: "",
  page: 1,
};

function searchReducer(state: SearchState, action: SearchAction): SearchState {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload, page: 1 };
    case "SET_REGION":
      return { ...state, region: action.payload, page: 1 };
    case "SET_PAGE":
      return { ...state, page: action.payload };
    case "RESET":
      return initialState;
  }
}
```

권장 기준:

- State Type을 먼저 정의한다.
- Action은 Union Type으로 정의한다.
- action.type별 payload를 구체화한다.
- reducer 반환 타입을 명시한다.
- RESET action은 payload 없이 정의할 수 있다.

---

### [FAQ]

Q. TypeScript에서 useReducer action은 어떻게 정의해?
A. Discriminated Union으로 action type별 payload를 명확히 정의하는 방식이 좋다.

Q. RESET action에도 payload가 필요해?
A. 보통 필요 없다. 초기 상태로 되돌리는 action은 payload 없이 정의할 수 있다.

Q. reducer 반환 타입을 명시해야 해?
A. 명시하는 것이 좋다. reducer가 항상 올바른 State를 반환하는지 확인하기 쉽다.

---

## 10.2 Exhaustive Check

### [개념]

Exhaustive Check는 reducer switch에서 모든 action type을 처리했는지 TypeScript로 검증하는 방식이다.

Action이 추가되었는데 reducer 처리가 누락되는 문제를 줄일 수 있다.

---

### [핵심]

Exhaustive Check 목적:

- action 누락 방지
- reducer 안정성 강화
- type safety
- 유지보수성 향상
- action 추가 시 컴파일 검출

---

### [실무]

Exhaustive Check 예:

```tsx
function assertNever(value: never): never {
  throw new Error(`Unhandled action: ${JSON.stringify(value)}`);
}

function reducer(state: SearchState, action: SearchAction): SearchState {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload };
    case "SET_REGION":
      return { ...state, region: action.payload };
    case "RESET":
      return initialState;
    default:
      return assertNever(action);
  }
}
```

적용 기준:

```text
Action type이 많음
→ reducer 누락 가능성 있음
→ TypeScript Exhaustive Check 검토
```

주의:

- 작은 reducer에서는 필수는 아니다.
- default에서 단순 state 반환 시 action 누락을 놓칠 수 있다.
- 팀 컨벤션에 따라 적용 여부를 정한다.

---

### [FAQ]

Q. Exhaustive Check는 왜 써?
A. action type이 추가되었는데 reducer 처리가 누락되는 문제를 TypeScript로 잡기 위해 사용한다.

Q. default에서 state를 반환하면 안 돼?
A. 가능하지만 action 누락을 조용히 무시할 수 있어 유지보수에 불리할 수 있다.

Q. 모든 reducer에 assertNever가 필요해?
A. 필수는 아니지만 action type이 많거나 안정성이 중요한 reducer에는 유용하다.

---

# 11. useReducer Use Cases

## 11.1 Form State with useReducer

### [개념]

Form State with useReducer는 여러 입력값, 검증 상태, 제출 상태를 action 기반으로 관리하는 방식이다.

입력 필드가 많고 상태 전환이 명확하면 useState 여러 개보다 useReducer가 더 구조적일 수 있다.

---

### [핵심]

Form Reducer 대상:

- input value
- validation error
- touched
- dirty
- submit status
- server error
- reset
- submit start
- submit success
- submit failure

---

### [실무]

Form Reducer 예:

```tsx
type FormState = {
  email: string;
  password: string;
  error: string | null;
  submitting: boolean;
};

type FormAction =
  | { type: "SET_EMAIL"; payload: string }
  | { type: "SET_PASSWORD"; payload: string }
  | { type: "SUBMIT_START" }
  | { type: "SUBMIT_FAILURE"; payload: string }
  | { type: "RESET" };

function formReducer(state: FormState, action: FormAction): FormState {
  switch (action.type) {
    case "SET_EMAIL":
      return { ...state, email: action.payload };
    case "SET_PASSWORD":
      return { ...state, password: action.payload };
    case "SUBMIT_START":
      return { ...state, submitting: true, error: null };
    case "SUBMIT_FAILURE":
      return { ...state, submitting: false, error: action.payload };
    case "RESET":
      return initialFormState;
  }
}
```

적합 조건:

```text
입력 필드가 여러 개
검증 상태가 있음
제출 상태가 있음
서버 오류 반영 필요
reset 필요
상태 전환 규칙이 명확함
```

주의:

- 단순 input 1~2개는 useState가 더 간단하다.
- 복잡한 Form은 React Hook Form 같은 Form Library가 더 적합할 수 있다.
- API 호출은 reducer 외부에서 처리한다.
- 민감한 입력값을 persist하지 않는다.

---

### [FAQ]

Q. Form State에 useReducer를 언제 써?
A. 입력 필드와 상태 전환이 많고 submit, error, reset 같은 action이 명확할 때 사용한다.

Q. 모든 Form에 useReducer를 써야 해?
A. 아니다. 단순 Form은 useState가 더 간단하고 복잡한 Form은 Form Library가 더 적합할 수 있다.

Q. Form submit API 호출을 reducer 안에서 해도 돼?
A. 권장하지 않는다. API 호출은 event handler나 effect에서 처리하고 reducer는 상태 전환만 담당해야 한다.

---

## 11.2 Step State with useReducer

### [개념]

Step State with useReducer는 다단계 화면, Wizard Form, Onboarding Flow처럼 단계 전환이 있는 UI를 action 기반으로 관리하는 방식이다.

단계 이동 규칙이 명확하면 useReducer가 흐름을 표현하기 좋다.

---

### [핵심]

Step State 구성:

- currentStep
- next step
- previous step
- completed step
- validation per step
- step data
- reset
- submit
- step guard

---

### [실무]

Step Reducer 예:

```tsx
type StepState = {
  currentStep: number;
  completedSteps: number[];
};

type StepAction =
  | { type: "NEXT" }
  | { type: "PREV" }
  | { type: "GO_TO"; payload: number }
  | { type: "COMPLETE_STEP"; payload: number }
  | { type: "RESET" };

function stepReducer(state: StepState, action: StepAction): StepState {
  switch (action.type) {
    case "NEXT":
      return { ...state, currentStep: state.currentStep + 1 };
    case "PREV":
      return { ...state, currentStep: Math.max(0, state.currentStep - 1) };
    case "GO_TO":
      return { ...state, currentStep: action.payload };
    case "COMPLETE_STEP":
      return {
        ...state,
        completedSteps: [...state.completedSteps, action.payload],
      };
    case "RESET":
      return initialStepState;
  }
}
```

적합 조건:

```text
단계 전환이 있음
이전 / 다음 / 특정 단계 이동이 있음
단계별 검증이 있음
reset이 있음
상태 전환 규칙이 많음
```

주의:

- Step 수가 적고 단순하면 useState로 충분하다.
- 복잡한 상태 머신은 Advanced State Management 또는 XState 같은 도구를 별도 검토한다.
- URL로 step 복원이 필요하면 URL State와 연동할 수 있다.

---

### [FAQ]

Q. Step UI에 useReducer가 적합해?
A. 단계 이동 규칙이 많고 next, prev, reset 같은 action이 명확하면 적합하다.

Q. currentStep 하나만 있으면 useReducer가 필요해?
A. 아니다. 단순 currentStep 숫자 하나는 useState가 더 간단하다.

Q. Step을 URL에 저장해야 해?
A. 새로고침 복원이나 공유가 필요하면 URL State를 검토할 수 있다.

---

## 11.3 Filter State with useReducer

### [개념]

Filter State with useReducer는 여러 필터 조건을 action 기반으로 관리하는 방식이다.

검색 조건, 카테고리, 정렬, 페이지 번호가 함께 움직이는 목록 화면에서 유용할 수 있다.

---

### [핵심]

Filter State 구성:

- keyword
- category
- region
- sort
- page
- date range
- reset
- apply filter
- clear filter

---

### [실무]

Filter Reducer 예:

```tsx
type FilterState = {
  keyword: string;
  region: string;
  sort: "latest" | "popular";
  page: number;
};

type FilterAction =
  | { type: "SET_KEYWORD"; payload: string }
  | { type: "SET_REGION"; payload: string }
  | { type: "SET_SORT"; payload: "latest" | "popular" }
  | { type: "SET_PAGE"; payload: number }
  | { type: "RESET" };

function filterReducer(state: FilterState, action: FilterAction): FilterState {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload, page: 1 };
    case "SET_REGION":
      return { ...state, region: action.payload, page: 1 };
    case "SET_SORT":
      return { ...state, sort: action.payload, page: 1 };
    case "SET_PAGE":
      return { ...state, page: action.payload };
    case "RESET":
      return initialFilterState;
  }
}
```

실무 기준:

```text
입력 중 임시 필터 → Local Reducer 가능
적용된 검색 조건 → URL State 권장
Server State 조회 조건 → queryKey 포함
```

주의:

- 검색 결과 공유와 새로고침 복원이 필요하면 URL State를 우선 검토한다.
- API 데이터 자체는 reducer에 저장하지 않는다.
- reducer는 filter 조건만 관리하고 목록 데이터는 Server State로 관리한다.

---

### [FAQ]

Q. 목록 필터에 useReducer를 써도 돼?
A. 필터 조건이 여러 개이고 reset, page 초기화 같은 전환 규칙이 있으면 적합할 수 있다.

Q. 검색 조건은 useReducer와 URL State 중 뭐가 좋아?
A. 입력 중 임시 조건은 useReducer로 관리할 수 있고, 적용된 검색 조건은 URL State가 적합한 경우가 많다.

Q. 필터 결과 목록도 reducer에 저장해?
A. 권장하지 않는다. API 목록 데이터는 Server State로 관리하고 filter 조건만 reducer에서 관리하는 것이 좋다.

---

# 12. useReducer and Context

## 12.1 Context with useReducer

### [개념]

Context with useReducer는 Context Provider 내부에서 useReducer로 상태 전환을 관리하고 하위 Component에 state와 dispatch 또는 action 함수를 제공하는 패턴이다.

작은 규모의 전역 유사 상태나 Feature 범위 상태에 사용할 수 있다.

---

### [핵심]

구성 요소:

- Context Provider
- useReducer
- initialState
- reducer
- dispatch
- action function
- custom hook
- state context
- action context

---

### [실무]

예:

```tsx
function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(authReducer, initialAuthState);

  function logout() {
    dispatch({ type: "LOGOUT" });
  }

  const value = {
    authenticated: state.authenticated,
    user: state.user,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
```

적합 조건:

```text
Context 값이 단순하지 않음
상태 전환 규칙이 action 기반임
Provider 내부에서 상태를 관리해야 함
Feature 범위 상태 공유가 필요함
Redux Toolkit 도입은 과함
```

주의:

- Context + useReducer가 커지면 유지보수가 어려워질 수 있다.
- dispatch를 그대로 노출할지 action 함수를 노출할지 기준을 정한다.
- Server State를 reducer에 저장하지 않는다.
- 복잡한 전역 Store가 필요하면 Zustand나 Redux Toolkit을 검토한다.

---

### [FAQ]

Q. Context와 useReducer를 같이 써도 돼?
A. 가능하다. Provider 내부 상태 전환이 복잡하고 하위 Component에서 공유해야 할 때 사용할 수 있다.

Q. Context + useReducer는 Redux 대체야?
A. 작은 규모에서는 비슷한 역할을 할 수 있지만 복잡한 전역 상태 추적과 DevTools가 필요하면 Redux Toolkit이 더 적합하다.

Q. dispatch를 Context로 그대로 내려도 돼?
A. 가능하지만 action 함수를 감싸서 제공하면 사용 API가 명확해질 수 있다.

---

## 12.2 Dispatch Exposure Rules

### [개념]

Dispatch Exposure Rules는 Context에서 dispatch를 그대로 제공할지, action 함수로 감싸서 제공할지 결정하는 기준이다.

Action 함수로 감싸면 Consumer가 reducer action 구조를 몰라도 된다.

---

### [핵심]

노출 방식:

- dispatch 직접 노출
- action function 노출
- state/action context 분리
- reducer action 숨김
- consumer API 안정화

---

### [실무]

dispatch 직접 노출:

```tsx
const { dispatch } = useSearchContext();

dispatch({ type: "SET_KEYWORD", payload: "react" });
```

action function 노출:

```tsx
const { setKeyword, reset } = useSearchContext();

setKeyword("react");
reset();
```

판단 기준:

```text
내부 Feature 전용
→ dispatch 직접 노출 가능

공용 Context
→ action function 노출 권장

Action 구조 변경 가능성 있음
→ action function 노출 권장

팀 컨벤션이 reducer 중심
→ dispatch 노출 가능
```

권장:

- 외부 사용 API는 action function으로 단순화한다.
- action type 문자열을 Consumer에 흩뿌리지 않는다.
- reducer 내부 구조 변경이 Consumer에 영향을 주지 않게 한다.
- 복잡한 action payload는 함수 인자로 감춘다.

---

### [FAQ]

Q. Context에서 dispatch를 그대로 내려도 돼?
A. 가능하지만 공용 Context에서는 action 함수로 감싸 제공하는 것이 사용성이 좋다.

Q. action function으로 감싸면 뭐가 좋아?
A. Consumer가 action type과 payload 구조를 몰라도 되어 API가 안정적이고 읽기 쉬워진다.

Q. dispatch 노출이 나쁜 패턴이야?
A. 무조건 나쁜 것은 아니다. Feature 내부 전용이고 팀 규칙이 명확하면 사용할 수 있다.

---

# 13. useReducer Anti Patterns

## 13.1 Reducer Side Effect Problem

### [개념]

Reducer Side Effect Problem은 reducer 내부에서 API 호출, localStorage 쓰기, navigation 같은 side effect를 수행하는 문제다.

Reducer는 순수 함수로 유지해야 예측 가능한 상태 전환이 가능하다.

---

### [핵심]

Reducer 내부 금지 대상:

- API request
- localStorage write
- sessionStorage write
- navigation
- toast side effect
- random value 생성
- Date.now 직접 사용
- DOM 조작
- 외부 변수 변경

---

### [실무]

나쁜 예:

```tsx
function reducer(state, action) {
  switch (action.type) {
    case "LOGIN_SUCCESS":
      localStorage.setItem("token", action.payload.token);
      return { ...state, authenticated: true };
    default:
      return state;
  }
}
```

개선 예:

```tsx
async function handleLogin(formValues) {
  const result = await loginApi(formValues);

  localStorage.setItem("token", result.token);

  dispatch({
    type: "LOGIN_SUCCESS",
    payload: result.user,
  });
}
```

권장 기준:

- reducer는 next state만 반환한다.
- side effect는 event handler, service function, effect, middleware 성격의 코드에서 처리한다.
- reducer 테스트가 쉬워야 한다.
- 같은 입력에 같은 출력이 나와야 한다.

---

### [FAQ]

Q. reducer 안에서 API 호출하면 안 돼?
A. 권장하지 않는다. reducer는 순수 함수로 유지하고 API 호출은 외부에서 처리해야 한다.

Q. reducer 안에서 localStorage를 써도 돼?
A. 권장하지 않는다. 저장 작업은 reducer 외부에서 처리하고 reducer는 State 전환만 담당하는 것이 좋다.

Q. reducer가 순수 함수여야 하는 이유는?
A. 같은 state와 action에 대해 항상 같은 next state를 반환해야 예측과 테스트가 쉽기 때문이다.

---

## 13.2 Overused useReducer

### [개념]

Overused useReducer는 단순한 상태까지 모두 useReducer로 관리해 코드 복잡도를 불필요하게 높이는 문제다.

useReducer는 상태 전환이 복잡할 때 사용하는 도구이지 useState의 기본 대체제가 아니다.

---

### [핵심]

문제:

- 단순 boolean에 reducer 사용
- 단순 input 하나에 reducer 사용
- action type이 불필요하게 많음
- reducer 파일이 과도하게 분리됨
- Component 이해 비용 증가
- 상태 변경 추적이 오히려 복잡해짐

---

### [실무]

useState가 더 적합한 경우:

```tsx
const [open, setOpen] = useState(false);
const [keyword, setKeyword] = useState("");
const [selectedTab, setSelectedTab] = useState("info");
```

useReducer가 적합한 경우:

```text
상태 필드가 많음
상태 전환 규칙이 많음
reset이 필요함
submit lifecycle이 있음
이전 상태 기반 전환이 많음
action naming으로 의도를 표현할 수 있음
```

판단 기준:

```text
State 하나 + 단순 setter
→ useState

State 여러 개 + 전환 규칙 단순
→ useState 여러 개 가능

State 여러 개 + 전환 규칙 복잡
→ useReducer 검토
```

---

### [FAQ]

Q. useReducer를 많이 쓰면 좋은 구조야?
A. 아니다. 단순 상태에는 useState가 더 읽기 쉽고 간단하다.

Q. boolean toggle에도 useReducer를 써야 해?
A. 보통 필요 없다. 단순 boolean은 useState가 적합하다.

Q. useState가 여러 개면 무조건 useReducer로 바꿔야 해?
A. 아니다. 상태 전환 규칙이 서로 강하게 연결되고 복잡할 때 useReducer를 검토한다.

---

## 13.3 Reducer State Duplication

### [개념]

Reducer State Duplication은 reducer state 안에 원본 값과 계산 가능한 파생 값을 함께 저장해 불일치가 발생하는 문제다.

Derived State는 reducer state에 저장하지 않는 것이 기본이다.

---

### [핵심]

중복 저장 예:

- items + filteredItems
- price + totalPrice
- firstName + lastName + fullName
- selectedId + selectedItem
- values + isValid
- serverData + mappedData

---

### [실무]

나쁜 예:

```tsx
type State = {
  items: Item[];
  keyword: string;
  filteredItems: Item[];
};
```

좋은 예:

```tsx
type State = {
  items: Item[];
  keyword: string;
};

const filteredItems = state.items.filter((item) =>
  item.title.includes(state.keyword),
);
```

판단 기준:

```text
기존 reducer state로 계산 가능
→ reducer state에 저장 금지

계산 비용이 큼
→ selector function 또는 useMemo 검토

서버 데이터 변환 필요
→ mapping function 분리
```

주의:

- reducer에서 Derived State를 매 action마다 동기화하려 하지 않는다.
- selectedItem보다 selectedId를 저장한다.
- Server State 복사본을 reducer에 저장하지 않는다.
- Single Source of Truth를 유지한다.

---

### [FAQ]

Q. reducer state에 filteredItems를 넣어도 돼?
A. items와 keyword로 계산 가능하면 넣지 않는 것이 좋다.

Q. selectedItem과 selectedId를 둘 다 저장해도 돼?
A. 권장하지 않는다. selectedId만 저장하고 selectedItem은 계산하는 것이 좋다.

Q. reducer에서도 Derived State 저장은 위험해?
A. 맞다. 원본과 파생 값이 불일치할 수 있다.

---

# 14. Context API vs useReducer vs Store

## 14.1 Context API vs useReducer

### [개념]

Context API와 useReducer는 역할이 다르다.

Context API는 값을 하위 Component에 공급하는 기능이고 useReducer는 상태 전환을 action 기반으로 관리하는 Hook이다.

---

### [핵심]

비교 기준:

- 목적
- 사용 위치
- 상태 소유
- 값 공유
- 상태 전환
- action 관리
- Re-render 영향
- 대체 관계 여부

---

### [실무]

Context API vs useReducer:

| 비교      | Context API                | useReducer                         |
| --------- | -------------------------- | ---------------------------------- |
| 목적      | 하위 Tree 값 공유          | 복잡한 State 전환 관리             |
| 역할      | Provider / Consumer        | reducer / dispatch                 |
| 사용 위치 | Component Tree             | Component 또는 Provider 내부       |
| 값 공유   | 가능                       | 자체 공유 기능 없음                |
| 상태 전환 | 직접 담당 아님             | action 기반 전환                   |
| 단독 사용 | 가능                       | 가능                               |
| 함께 사용 | Provider 내부 reducer 가능 | Context로 state/dispatch 공유 가능 |

판단 기준:

```text
Props 전달 문제
→ Context API 검토

상태 전환 복잡
→ useReducer 검토

값 공유 + 상태 전환 복잡
→ Context + useReducer 검토
```

---

### [FAQ]

Q. Context API와 useReducer는 같은 거야?
A. 아니다. Context는 값 공유 기능이고 useReducer는 상태 전환 관리 Hook이다.

Q. Context 없이 useReducer만 써도 돼?
A. 가능하다. 단일 Component 내부의 복잡한 상태 전환에는 useReducer만 써도 된다.

Q. useReducer 없이 Context만 써도 돼?
A. 가능하다. Theme처럼 단순한 값 공유는 Context와 useState만으로 충분할 수 있다.

---

## 14.2 Context API vs Zustand

### [개념]

Context API와 Zustand는 모두 여러 Component에서 상태를 사용할 수 있게 하지만 목적과 기능이 다르다.

Context API는 React의 값 공급 기능이고 Zustand는 전역 상태 Store 라이브러리다.

---

### [핵심]

Context API 적합:

- Theme
- Language
- Auth Summary
- App Config
- 낮은 변경 빈도
- 단순 값 공유
- React 내장 기능 선호

Zustand 적합:

- 여러 action
- Global Store 필요
- selector 기반 구독 필요
- 상태 변경이 비교적 많음
- Store 분리 필요
- Context보다 가벼운 전역 Store 필요

---

### [실무]

Context API vs Zustand:

| 비교           | Context API            | Zustand            |
| -------------- | ---------------------- | ------------------ |
| 성격           | React 값 공급 기능     | 전역 상태 Store    |
| 설치           | React 내장             | 외부 라이브러리    |
| Selector       | 기본 제공 아님         | selector 사용      |
| Re-render 제어 | Context 분리 필요      | 필요한 값 구독     |
| Action 관리    | 직접 설계              | Store 내부 action  |
| 적합           | 낮은 변경 빈도 공유 값 | 가벼운 전역 상태   |
| 예             | theme, language        | authStore, uiStore |

판단 기준:

```text
단순 공유 값 + 낮은 변경 빈도
→ Context API

상태와 action이 많음
→ Zustand

selector 기반 구독 필요
→ Zustand

React 내장 기능만으로 충분
→ Context API
```

---

### [FAQ]

Q. Context와 Zustand 중 뭐가 좋아?
A. Theme처럼 단순하고 변경 빈도가 낮은 값은 Context가 적합하고, 상태와 action이 많으면 Zustand가 편할 수 있다.

Q. Zustand를 쓰면 Context가 필요 없어?
A. 대부분 전역 상태 공유에는 Zustand로 대체 가능하지만 Theme Provider나 외부 라이브러리 Provider는 여전히 사용할 수 있다.

Q. Context의 Re-render 문제가 걱정되면 바로 Zustand를 써야 해?
A. 먼저 Context 범위와 value 구조를 점검하고, selector 기반 구독이 필요하면 Zustand를 검토한다.

---

## 14.3 useReducer vs Redux Toolkit

### [개념]

useReducer와 Redux Toolkit은 모두 reducer 개념을 사용하지만 범위와 목적이 다르다.

useReducer는 React Component 또는 Context 내부 상태 전환을 관리하고 Redux Toolkit은 애플리케이션 규모의 전역 상태를 구조화한다.

---

### [핵심]

useReducer 적합:

- Component 내부 복잡 상태
- Feature 내부 상태
- Context Provider 내부 상태
- 작은 규모 action
- 단순 reducer

Redux Toolkit 적합:

- 복잡한 Global State
- DevTools 기반 추적
- 팀 컨벤션
- 여러 Slice
- 중앙 집중 Store
- 예측 가능한 전역 상태 흐름

---

### [실무]

useReducer vs Redux Toolkit:

| 비교        | useReducer          | Redux Toolkit       |
| ----------- | ------------------- | ------------------- |
| 범위        | Component / Context | App Global Store    |
| 설치        | React 내장          | 외부 라이브러리     |
| DevTools    | 기본 없음           | 강력함              |
| Slice 구조  | 직접 설계           | createSlice 제공    |
| 상태 공유   | Context 필요        | Store Provider 사용 |
| 적합        | Local 복잡 상태     | 복잡한 전역 상태    |
| Boilerplate | 작음                | 상대적으로 많음     |

판단 기준:

```text
단일 Component 내부 복잡 상태
→ useReducer

Feature 내부 공유 상태
→ Context + useReducer

App 전체 복잡 전역 상태
→ Redux Toolkit

상태 변경 이력 추적 중요
→ Redux Toolkit
```

---

### [FAQ]

Q. useReducer와 Redux Toolkit은 같은 거야?
A. 아니다. 둘 다 reducer 개념을 쓰지만 useReducer는 React Hook이고 Redux Toolkit은 전역 상태관리 도구다.

Q. useReducer를 쓰면 Redux Toolkit이 필요 없어?
A. 작은 범위에서는 필요 없을 수 있지만 복잡한 전역 상태와 DevTools 추적이 필요하면 Redux Toolkit이 적합하다.

Q. Redux Toolkit 대신 Context + useReducer를 써도 돼?
A. 작은 규모에서는 가능하지만 규모가 커지면 Re-render 제어와 디버깅 측면에서 Redux Toolkit이 유리할 수 있다.

---

# 15. Context and useReducer Checklist

## 15.1 Context API Checklist

### [개념]

Context API Checklist는 Context 도입 전 적합성을 검수하는 기준이다.

Context는 Props Drilling 완화 도구로 유용하지만 State Classification 이후에 선택해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 이 값이 여러 하위 Component에서 필요한가?
- [ ] Props 전달이 실제로 반복되고 깊은가?
- [ ] 값 변경 빈도가 낮은가?
- [ ] Context value가 너무 크지 않은가?
- [ ] Local State나 Shared State로 충분하지 않은가?
- [ ] URL State가 더 적합하지 않은가?
- [ ] Server State가 아닌가?
- [ ] Derived State가 아닌가?
- [ ] Provider 위치가 필요한 범위로 제한되었는가?
- [ ] Custom Hook이 제공되는가?
- [ ] Provider 누락 오류를 처리하는가?
- [ ] Context 분리가 필요한가?
```

---

### [실무]

Context 도입 Flow:

```text
Shared Value 발견
→ Props Drilling 여부 확인
→ State Type 확인
→ 변경 빈도 확인
→ Provider 범위 결정
→ Context Value 설계
→ Custom Hook 작성
→ Re-render 영향 검토
```

결과 예:

```text
theme
→ Context 적합

reviewFormContent
→ Local State 적합

festivalList
→ Server State 적합

searchKeyword
→ URL State 적합

complex auth lifecycle
→ Zustand 또는 Redux Toolkit 검토
```

---

### [FAQ]

Q. Context 도입 전에 무엇을 확인해야 해?
A. 값 공유 범위, 변경 빈도, Provider 위치, Server State 여부, Derived State 여부를 확인해야 한다.

Q. Context가 필요한지 어떻게 판단해?
A. 여러 하위 Component에서 같은 값을 읽고 Props 전달이 깊어질 때 Context를 검토한다.

Q. Context Checklist에서 가장 중요한 것은 뭐야?
A. Context에 넣을 값이 정말 공유 값인지, 변경 빈도가 낮은지, Server State가 아닌지 확인하는 것이다.

---

## 15.2 useReducer Checklist

### [개념]

useReducer Checklist는 useState 대신 useReducer를 도입할지 판단하는 기준이다.

useReducer는 상태 전환 복잡도가 있을 때 선택한다.

---

### [핵심]

Checklist:

```md
- [ ] State field가 여러 개인가?
- [ ] 상태 전환 규칙이 복잡한가?
- [ ] action type으로 의도를 표현할 수 있는가?
- [ ] reset이 필요한가?
- [ ] submit lifecycle이 있는가?
- [ ] 이전 State 기반 업데이트가 많은가?
- [ ] reducer를 순수 함수로 유지할 수 있는가?
- [ ] API 호출을 reducer 밖에서 처리하는가?
- [ ] Derived State를 reducer state에 저장하지 않는가?
- [ ] TypeScript Action Union을 정의했는가?
- [ ] 단순 useState보다 읽기 쉬운가?
```

---

### [실무]

useReducer 도입 Flow:

```text
State 복잡도 증가
→ useState로 충분한지 확인
→ action 단위 전환 가능 여부 확인
→ reducer 순수성 확인
→ State / Action Type 정의
→ initialState 정의
→ reducer 작성
→ dispatch 사용
```

결과 예:

```text
modalOpen
→ useState

keyword input
→ useState

filter panel
→ useReducer 검토

wizard step
→ useReducer 검토

API list cache
→ TanStack Query

complex global domain state
→ Redux Toolkit 검토
```

---

### [FAQ]

Q. useReducer 도입 전에 무엇을 확인해야 해?
A. 상태 전환이 복잡한지, action으로 표현 가능한지, useState보다 구조가 명확해지는지 확인해야 한다.

Q. useReducer Checklist에서 가장 중요한 것은 뭐야?
A. reducer를 순수 함수로 유지하고 단순 상태에 과도하게 사용하지 않는 것이다.

Q. useReducer가 복잡해지면 어떻게 해?
A. 범위가 전역으로 커졌다면 Zustand나 Redux Toolkit을 검토하고, Form이 복잡하면 Form Library를 검토한다.

---

# 16. Part02 Final Review

## 16.1 Part02 Scope Summary

### [개념]

Part02는 Context API와 useReducer의 사용 기준, 구조, 성능 주의사항, Anti Pattern을 다룬다.

이 문서는 전역 상태 라이브러리 도입 전에 React 내장 기능으로 해결 가능한 범위를 판단하는 데 집중한다.

---

### [핵심]

Part02 포함 범위:

- Context API Purpose
- createContext
- Provider
- useContext
- Context Custom Hook
- Context Value Design
- Provider Placement
- Context Performance Caution
- Theme Context
- Auth Context
- Language Context
- Context Anti Patterns
- useReducer Purpose
- Reducer Function
- Action Object
- TypeScript Reducer Type
- useReducer Use Cases
- Context with useReducer
- Context vs Zustand
- useReducer vs Redux Toolkit
- Context and useReducer Checklist

---

### [실무]

Part02 이후 문서 연결:

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
User Frontend State Request
→ Part01로 State Type과 Owner 판단
→ Props Drilling 또는 하위 Tree 공유면 Part02 Context API 검토
→ 복잡한 Local State 전환이면 Part02 useReducer 검토
→ 전역 Store가 필요하면 Part03으로 이동
→ Server State면 Part04로 이동
```

---

### [FAQ]

Q. Part02의 핵심 목적은 뭐야?
A. Context API와 useReducer를 언제 쓰고 언제 쓰지 말아야 하는지 판단하게 하는 것이다.

Q. Part02는 전역 상태 라이브러리 문서야?
A. 아니다. React 내장 기능인 Context API와 useReducer의 사용 기준을 다룬다.

Q. Part02 다음에는 무엇을 다뤄야 해?
A. Zustand와 Redux Toolkit 같은 전역 상태 Store 선택 기준과 설계 규칙을 다루는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Context API는 뭐야?
A. Component Tree 아래로 Props를 계속 전달하지 않고 하위 Component들이 공유 값을 읽을 수 있게 하는 React 기능이다.

Q. Context API는 전역 상태관리야?
A. 전역처럼 값을 공유할 수 있지만 상태관리 라이브러리라기보다 Component Tree에 값을 공급하는 React 기능에 가깝다.

Q. Context API는 언제 써?
A. Theme, Auth Summary, Language처럼 여러 하위 Component에서 반복적으로 필요한 값을 전달할 때 사용한다.

Q. createContext는 뭐야?
A. 하위 Component에 공유 값을 제공하기 위한 Context 객체를 만드는 React API다.

Q. Provider는 뭐야?
A. Context 값을 하위 Component Tree에 공급하는 Component다.

Q. useContext는 뭐야?
A. Provider가 공급한 Context value를 읽기 위한 React Hook이다.

Q. Context Provider는 어디에 둬야 해?
A. Context 값을 사용하는 Component들을 포함하는 가장 좁은 공통 부모에 두는 것이 기본이다.

Q. 모든 Provider를 App 최상단에 둬도 돼?
A. 권장하지 않는다. App 전체에서 필요한 값만 Root 근처에 두고 Feature 전용 값은 Feature 내부에 두는 것이 좋다.

Q. Provider 위치가 너무 넓으면 어떤 문제가 생겨?
A. 불필요한 의존성이 생기고 value 변경 시 Re-render 영향 범위가 커질 수 있다.

Q. Context Custom Hook은 왜 필요해?
A. Provider 누락 검증, 사용 API 통일, 타입 안정성 강화를 위해 필요하다.

Q. useContext를 직접 쓰면 안 돼?
A. 가능하지만 Custom Hook으로 감싸면 Provider 누락 오류를 명확히 처리할 수 있다.

Q. Context 기본값은 null로 둬도 돼?
A. 가능하다. 대신 Custom Hook에서 null을 검사해 Provider 누락 오류를 명확히 처리해야 한다.

Q. Context Hook 이름은 어떻게 지어?
A. useAuth, useTheme처럼 Context의 역할을 드러내는 이름이 좋다.

Q. useGlobal 같은 이름은 괜찮아?
A. 권장하지 않는다. 어떤 상태를 제공하는지 알기 어렵기 때문이다.

Q. Zustand Store Hook과 Context Hook 이름이 겹치면 어떻게 해?
A. useAuthStore, useAuthContext처럼 역할이나 구현 방식을 이름에 반영해 구분한다.

Q. Context value에는 무엇을 넣어?
A. 하위 Component가 실제로 필요한 상태값과 변경 함수만 넣는 것이 좋다.

Q. Context value를 큰 객체로 만들어도 돼?
A. 권장하지 않는다. value가 커질수록 불필요한 의존성과 Re-render 문제가 생길 수 있다.

Q. Context에 여러 도메인 상태를 같이 넣어도 돼?
A. 권장하지 않는다. auth, theme, language처럼 역할별로 분리하는 것이 좋다.

Q. State Context와 Action Context를 왜 나눠?
A. action만 필요한 Component가 State 변경으로 Re-render되는 범위를 줄이기 위해 나눌 수 있다.

Q. 항상 State Context와 Action Context를 나눠야 해?
A. 아니다. 작은 Context에서는 불필요하게 복잡해질 수 있으므로 필요할 때만 적용한다.

Q. Context 분리 대신 Zustand를 써도 돼?
A. 가능하다. 상태와 action이 많고 selector 기반 구독이 필요하면 Zustand가 더 단순할 수 있다.

Q. Context를 쓰면 무조건 성능 문제가 생겨?
A. 아니다. 하지만 큰 value나 자주 바뀌는 상태를 많은 Component가 구독하면 Re-render 문제가 생길 수 있다.

Q. Context 성능 문제는 어떻게 줄여?
A. Context를 역할별로 분리하고 Provider 범위를 줄이며 자주 바뀌는 상태는 전용 Store를 검토한다.

Q. Context value에 API 목록 데이터를 넣어도 돼?
A. 권장하지 않는다. API 목록 데이터는 Server State로 보고 TanStack Query 같은 도구를 검토하는 것이 좋다.

Q. Context value에는 항상 useMemo를 써야 해?
A. 아니다. 성능 문제가 있거나 value reference 안정성이 필요할 때 검토한다.

Q. useMemo를 쓰면 Context Re-render가 완전히 사라져?
A. 아니다. value에 포함된 상태가 바뀌면 해당 Context를 구독하는 Component는 다시 렌더링될 수 있다.

Q. Context 성능 최적화의 우선순위는 뭐야?
A. 먼저 Context 역할과 범위를 분리하고, 그 다음 memoization을 검토하는 것이 좋다.

Q. Theme은 Context API에 적합해?
A. 적합하다. Theme은 여러 Component에서 필요하고 변경 빈도가 낮은 대표적인 Context 사용 사례다.

Q. Theme을 localStorage에 저장해도 돼?
A. 가능하다. Theme은 비민감 사용자 설정이므로 새로고침 후 유지가 필요하면 저장할 수 있다.

Q. Theme Context에 sidebar 상태도 같이 넣어도 돼?
A. 권장하지 않는다. theme과 layout state는 책임이 다르므로 분리하는 것이 좋다.

Q. Auth State는 Context로 관리해도 돼?
A. 가능하다. 인증 여부와 사용자 요약 정보가 단순하면 Auth Context가 적합할 수 있다.

Q. Auth Context와 Zustand authStore 중 뭐가 좋아?
A. 단순 인증 상태는 Context로 충분할 수 있고 action과 reset 흐름이 복잡하면 Zustand를 검토할 수 있다.

Q. Auth Context만 있으면 보안이 돼?
A. 아니다. Frontend Auth State는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Language는 Context API에 적합해?
A. 적합하다. 여러 Component에서 필요하고 변경 빈도가 낮은 설정값이기 때문이다.

Q. 번역 데이터 전체를 Context에 넣어도 돼?
A. 권장하지 않는다. 무거운 데이터는 별도 i18n 도구나 모듈로 관리하는 것이 좋다.

Q. Language도 localStorage에 저장할 수 있어?
A. 가능하다. 비민감 사용자 설정이므로 새로고침 후 유지가 필요하면 저장할 수 있다.

Q. Context에 모든 상태를 넣으면 안 돼?
A. 권장하지 않는다. Context가 커지면 Re-render와 유지보수 문제가 커질 수 있다.

Q. Context가 너무 커졌으면 어떻게 해?
A. State Type을 다시 분류하고 Local State, URL State, Server State, 별도 Store로 분리한다.

Q. API 응답 데이터를 Context에 넣어도 돼?
A. 권장하지 않는다. API 응답 데이터는 Server State로 보고 TanStack Query 같은 도구를 검토하는 것이 좋다.

Q. Context를 Global Store처럼 써도 돼?
A. 작은 규모에서는 가능하지만 복잡한 전역 상태와 많은 action이 있으면 Zustand나 Redux Toolkit이 더 적합할 수 있다.

Q. Context와 Zustand의 차이는 뭐야?
A. Context는 값을 공급하는 React 기능이고 Zustand는 selector 기반 구독과 action을 가진 전역 상태 Store다.

Q. Context가 복잡해지면 언제 다른 도구로 바꿔?
A. action이 많아지고 Re-render 제어, 상태 추적, 도메인 분리가 필요해질 때 전용 Store를 검토한다.

Q. useReducer는 언제 써?
A. 상태 필드가 많고 변경 규칙이 action 단위로 명확할 때 사용한다.

Q. useState와 useReducer 중 뭐가 좋아?
A. 단순 상태는 useState가 좋고, 상태 전환이 복잡하면 useReducer가 적합하다.

Q. useReducer는 전역 상태관리 도구야?
A. 아니다. React Hook이며 Local State나 Context 내부 상태 전환을 구조화할 때 사용한다.

Q. reducer는 뭐야?
A. 현재 state와 action을 받아 다음 state를 반환하는 순수 함수다.

Q. reducer 안에서 API 호출해도 돼?
A. 권장하지 않는다. reducer는 순수 함수로 유지하고 API 호출은 외부에서 처리해야 한다.

Q. reducer에서 state를 직접 변경해도 돼?
A. 일반 useReducer reducer에서는 직접 변경하지 말고 새 객체를 반환해야 한다.

Q. useReducer action type은 어떻게 지어?
A. SET_KEYWORD, RESET_FORM처럼 상태 변경 의도를 드러내는 이름이 좋다.

Q. action payload는 뭐야?
A. 상태 변경에 필요한 추가 데이터다.

Q. action type을 UPDATE로만 통일해도 돼?
A. 권장하지 않는다. 변경 의도가 불명확해져 reducer 추적이 어려워질 수 있다.

Q. TypeScript에서 useReducer action은 어떻게 정의해?
A. Discriminated Union으로 action type별 payload를 명확히 정의하는 방식이 좋다.

Q. RESET action에도 payload가 필요해?
A. 보통 필요 없다. 초기 상태로 되돌리는 action은 payload 없이 정의할 수 있다.

Q. reducer 반환 타입을 명시해야 해?
A. 명시하는 것이 좋다. reducer가 항상 올바른 State를 반환하는지 확인하기 쉽다.

Q. Exhaustive Check는 왜 써?
A. action type이 추가되었는데 reducer 처리가 누락되는 문제를 TypeScript로 잡기 위해 사용한다.

Q. default에서 state를 반환하면 안 돼?
A. 가능하지만 action 누락을 조용히 무시할 수 있어 유지보수에 불리할 수 있다.

Q. 모든 reducer에 assertNever가 필요해?
A. 필수는 아니지만 action type이 많거나 안정성이 중요한 reducer에는 유용하다.

Q. Form State에 useReducer를 언제 써?
A. 입력 필드와 상태 전환이 많고 submit, error, reset 같은 action이 명확할 때 사용한다.

Q. 모든 Form에 useReducer를 써야 해?
A. 아니다. 단순 Form은 useState가 더 간단하고 복잡한 Form은 Form Library가 더 적합할 수 있다.

Q. Form submit API 호출을 reducer 안에서 해도 돼?
A. 권장하지 않는다. API 호출은 event handler나 effect에서 처리하고 reducer는 상태 전환만 담당해야 한다.

Q. Step UI에 useReducer가 적합해?
A. 단계 이동 규칙이 많고 next, prev, reset 같은 action이 명확하면 적합하다.

Q. currentStep 하나만 있으면 useReducer가 필요해?
A. 아니다. 단순 currentStep 숫자 하나는 useState가 더 간단하다.

Q. Step을 URL에 저장해야 해?
A. 새로고침 복원이나 공유가 필요하면 URL State를 검토할 수 있다.

Q. 목록 필터에 useReducer를 써도 돼?
A. 필터 조건이 여러 개이고 reset, page 초기화 같은 전환 규칙이 있으면 적합할 수 있다.

Q. 검색 조건은 useReducer와 URL State 중 뭐가 좋아?
A. 입력 중 임시 조건은 useReducer로 관리할 수 있고, 적용된 검색 조건은 URL State가 적합한 경우가 많다.

Q. 필터 결과 목록도 reducer에 저장해?
A. 권장하지 않는다. API 목록 데이터는 Server State로 관리하고 filter 조건만 reducer에서 관리하는 것이 좋다.

Q. Context와 useReducer를 같이 써도 돼?
A. 가능하다. Provider 내부 상태 전환이 복잡하고 하위 Component에서 공유해야 할 때 사용할 수 있다.

Q. Context + useReducer는 Redux 대체야?
A. 작은 규모에서는 비슷한 역할을 할 수 있지만 복잡한 전역 상태 추적과 DevTools가 필요하면 Redux Toolkit이 더 적합하다.

Q. dispatch를 Context로 그대로 내려도 돼?
A. 가능하지만 action 함수를 감싸서 제공하면 사용 API가 명확해질 수 있다.

Q. Context에서 dispatch를 그대로 내려도 돼?
A. 가능하지만 공용 Context에서는 action 함수로 감싸 제공하는 것이 사용성이 좋다.

Q. action function으로 감싸면 뭐가 좋아?
A. Consumer가 action type과 payload 구조를 몰라도 되어 API가 안정적이고 읽기 쉬워진다.

Q. dispatch 노출이 나쁜 패턴이야?
A. 무조건 나쁜 것은 아니다. Feature 내부 전용이고 팀 규칙이 명확하면 사용할 수 있다.

Q. reducer 안에서 localStorage를 써도 돼?
A. 권장하지 않는다. 저장 작업은 reducer 외부에서 처리하고 reducer는 State 전환만 담당하는 것이 좋다.

Q. reducer가 순수 함수여야 하는 이유는?
A. 같은 state와 action에 대해 항상 같은 next state를 반환해야 예측과 테스트가 쉽기 때문이다.

Q. useReducer를 많이 쓰면 좋은 구조야?
A. 아니다. 단순 상태에는 useState가 더 읽기 쉽고 간단하다.

Q. boolean toggle에도 useReducer를 써야 해?
A. 보통 필요 없다. 단순 boolean은 useState가 적합하다.

Q. useState가 여러 개면 무조건 useReducer로 바꿔야 해?
A. 아니다. 상태 전환 규칙이 서로 강하게 연결되고 복잡할 때 useReducer를 검토한다.

Q. reducer state에 filteredItems를 넣어도 돼?
A. items와 keyword로 계산 가능하면 넣지 않는 것이 좋다.

Q. selectedItem과 selectedId를 둘 다 저장해도 돼?
A. 권장하지 않는다. selectedId만 저장하고 selectedItem은 계산하는 것이 좋다.

Q. reducer에서도 Derived State 저장은 위험해?
A. 맞다. 원본과 파생 값이 불일치할 수 있다.

Q. Context API와 useReducer는 같은 거야?
A. 아니다. Context는 값 공유 기능이고 useReducer는 상태 전환 관리 Hook이다.

Q. Context 없이 useReducer만 써도 돼?
A. 가능하다. 단일 Component 내부의 복잡한 상태 전환에는 useReducer만 써도 된다.

Q. useReducer 없이 Context만 써도 돼?
A. 가능하다. Theme처럼 단순한 값 공유는 Context와 useState만으로 충분할 수 있다.

Q. Context와 Zustand 중 뭐가 좋아?
A. Theme처럼 단순하고 변경 빈도가 낮은 값은 Context가 적합하고, 상태와 action이 많으면 Zustand가 편할 수 있다.

Q. Zustand를 쓰면 Context가 필요 없어?
A. 대부분 전역 상태 공유에는 Zustand로 대체 가능하지만 Theme Provider나 외부 라이브러리 Provider는 여전히 사용할 수 있다.

Q. Context의 Re-render 문제가 걱정되면 바로 Zustand를 써야 해?
A. 먼저 Context 범위와 value 구조를 점검하고, selector 기반 구독이 필요하면 Zustand를 검토한다.

Q. useReducer와 Redux Toolkit은 같은 거야?
A. 아니다. 둘 다 reducer 개념을 쓰지만 useReducer는 React Hook이고 Redux Toolkit은 전역 상태관리 도구다.

Q. useReducer를 쓰면 Redux Toolkit이 필요 없어?
A. 작은 범위에서는 필요 없을 수 있지만 복잡한 전역 상태와 DevTools 추적이 필요하면 Redux Toolkit이 적합하다.

Q. Redux Toolkit 대신 Context + useReducer를 써도 돼?
A. 작은 규모에서는 가능하지만 규모가 커지면 Re-render 제어와 디버깅 측면에서 Redux Toolkit이 유리할 수 있다.

Q. Context 도입 전에 무엇을 확인해야 해?
A. 값 공유 범위, 변경 빈도, Provider 위치, Server State 여부, Derived State 여부를 확인해야 한다.

Q. Context가 필요한지 어떻게 판단해?
A. 여러 하위 Component에서 같은 값을 읽고 Props 전달이 깊어질 때 Context를 검토한다.

Q. Context Checklist에서 가장 중요한 것은 뭐야?
A. Context에 넣을 값이 정말 공유 값인지, 변경 빈도가 낮은지, Server State가 아닌지 확인하는 것이다.

Q. useReducer 도입 전에 무엇을 확인해야 해?
A. 상태 전환이 복잡한지, action으로 표현 가능한지, useState보다 구조가 명확해지는지 확인해야 한다.

Q. useReducer Checklist에서 가장 중요한 것은 뭐야?
A. reducer를 순수 함수로 유지하고 단순 상태에 과도하게 사용하지 않는 것이다.

Q. useReducer가 복잡해지면 어떻게 해?
A. 범위가 전역으로 커졌다면 Zustand나 Redux Toolkit을 검토하고, Form이 복잡하면 Form Library를 검토한다.

Q. Part02의 핵심 목적은 뭐야?
A. Context API와 useReducer를 언제 쓰고 언제 쓰지 말아야 하는지 판단하게 하는 것이다.

Q. Part02는 전역 상태 라이브러리 문서야?
A. 아니다. React 내장 기능인 Context API와 useReducer의 사용 기준을 다룬다.

Q. Part02 다음에는 무엇을 다뤄야 해?
A. Zustand와 Redux Toolkit 같은 전역 상태 Store 선택 기준과 설계 규칙을 다루는 것이 좋다.

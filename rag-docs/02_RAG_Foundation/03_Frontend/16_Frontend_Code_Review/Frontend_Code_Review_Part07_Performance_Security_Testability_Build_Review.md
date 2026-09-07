# Frontend Code Review Part07 - Performance, Security, Testability, and Build Review

---

# 1. Performance Review Rules

## 1.1 Rendering Performance Review

### [개념]

Rendering Performance Review는 React 화면이 불필요하게 자주 렌더링되거나 무거운 계산으로 인해 사용자 경험이 저하되는지 검토하는 과정이다.

성능 리뷰는 추측보다 실제 느린 지점, 큰 리스트, 이미지, 반복 계산, 불안정한 참조를 중심으로 판단한다.

Review Agent는 성능 최적화 자체보다 사용자 흐름을 느리게 만드는 위험을 먼저 확인해야 한다.

---

### [핵심]

Rendering Performance Review 검토 항목:

- 불필요한 state update가 없는가?
- 부모 렌더링으로 자식이 과도하게 다시 렌더링되지 않는가?
- 큰 리스트 렌더링이 최적화되어 있는가?
- list key가 안정적인가?
- index를 key로 남용하지 않는가?
- 무거운 filter / sort / map 계산이 매 렌더링마다 반복되지 않는가?
- inline object / inline function이 memoization을 깨지 않는가?
- React.memo / useMemo / useCallback을 적절히 사용하는가?
- memoization을 남용하지 않는가?
- 이미지 로딩이 렌더링을 지연시키지 않는가?
- 조건부 렌더링이 불필요하게 전체 화면을 교체하지 않는가?

---

### [실무]

성능 최적화 우선순위:

```text
Actual Slow User Flow
→ Large List Rendering
→ Unstable List Key
→ Heavy Calculation
→ Image Optimization
→ Unnecessary Re-render
→ Memoization
```

나쁜 key 예:

```jsx
{
  items.map((item, index) => <FestivalItem key={index} festival={item} />);
}
```

좋은 key 예:

```jsx
{
  items.map((festival) => (
    <FestivalItem key={festival.festivalId} festival={festival} />
  ));
}
```

무거운 계산 예:

```jsx
const filteredFestivals = useMemo(() => {
  return festivals
    .filter((festival) => festival.region === selectedRegion)
    .sort((a, b) => a.startDate.localeCompare(b.startDate));
}, [festivals, selectedRegion]);
```

리뷰 코멘트 예:

```text
[Medium] 축제 목록 렌더링에서 index를 key로 사용하고 있습니다. 목록 정렬, 삭제, 추가가 발생하면 잘못된 항목 재사용 문제가 생길 수 있으므로 festivalId 같은 안정적인 고유 값을 key로 사용해야 합니다.
```

---

### [FAQ]

Q. Rendering Performance Review는 왜 필요해?
A. 불필요한 렌더링과 무거운 계산은 화면 지연, 입력 끊김, 리스트 렌더링 오류를 만들 수 있기 때문이다.

Q. React.memo를 모든 컴포넌트에 써야 해?
A. 아니다. 실제 성능 문제가 있거나 props 참조 안정성이 필요한 경우에 사용한다.

Q. map에서 index를 key로 써도 돼?
A. 정적 목록이면 가능할 수 있지만 정렬, 삭제, 추가가 발생하면 렌더링 버그가 생길 수 있다. 고유 id가 좋다.

Q. 성능 최적화는 언제 우선순위가 높아져?
A. 실제 사용자 흐름이 느려지거나 큰 리스트, 이미지, 반복 계산으로 주요 기능 사용이 어려울 때 우선순위가 높아진다.

---

## 1.2 Large List Review

### [개념]

Large List Review는 많은 데이터를 렌더링하는 목록 화면이 pagination, infinite scroll, virtualization, lazy rendering 전략을 적절히 사용하는지 검토하는 과정이다.

큰 리스트를 한 번에 렌더링하면 초기 로딩 지연, 스크롤 끊김, 메모리 사용 증가가 발생할 수 있다.

---

### [핵심]

Large List Review 검토 항목:

- 서버 pagination 또는 Slice API를 사용하는가?
- 무한 스크롤에서 hasNext 처리가 있는가?
- 더보기 버튼 중복 클릭이 방지되는가?
- 큰 리스트에 virtualization이 필요한가?
- list item key가 안정적인가?
- 스크롤 이벤트가 throttle / debounce 되는가?
- loading / error / empty 상태가 목록 단위로 처리되는가?
- 이전 페이지 데이터와 새 페이지 데이터 병합이 안전한가?
- 중복 item이 추가되지 않는가?
- 필터 변경 시 목록 초기화가 되는가?

---

### [실무]

무한 스크롤 Flow:

```text
Initial List Request
→ Render Content
→ Scroll Near Bottom
→ Check hasNext
→ Request Next Slice
→ Append Content
→ Prevent Duplicate Request
→ Stop When hasNext False
```

더보기 버튼 예:

```jsx
<button
  type="button"
  disabled={!hasNext || isFetchingNextPage}
  onClick={fetchNextPage}
>
  {isFetchingNextPage ? "불러오는 중..." : "더보기"}
</button>
```

리뷰 코멘트 예:

```text
[High] 더보기 버튼 클릭 중 disabled 처리가 없어 같은 page 요청이 중복으로 발생할 수 있습니다. isFetchingNextPage guard와 disabled 처리를 추가해야 합니다.
```

---

### [FAQ]

Q. Large List Review는 언제 필요해?
A. 축제 목록, 알림 목록, 리뷰 목록, 채팅 메시지처럼 데이터가 계속 늘어날 수 있는 화면에서 필요하다.

Q. 모든 리스트에 virtualization이 필요해?
A. 아니다. 수백 개 이상 렌더링하거나 스크롤 성능 문제가 있을 때 검토한다.

Q. 무한 스크롤에서 가장 중요한 것은 뭐야?
A. hasNext 처리, 중복 요청 방지, loading 표시, page 병합 안정성이다.

Q. 필터 변경 시 기존 목록은 어떻게 해야 해?
A. 이전 조건의 목록을 초기화하고 새 조건으로 첫 페이지부터 다시 조회해야 한다.

---

## 1.3 Image Performance Review

### [개념]

Image Performance Review는 이미지 파일 크기, 로딩 방식, 크기 지정, fallback 처리가 화면 성능과 UX를 해치지 않는지 검토하는 과정이다.

프론트엔드 성능 문제는 이미지에서 자주 발생한다.

---

### [핵심]

Image Performance Review 검토 항목:

- 이미지 크기가 과도하지 않은가?
- WebP 등 최적화 포맷을 고려했는가?
- width / height 또는 aspect-ratio가 지정되어 있는가?
- lazy loading이 필요한 이미지에 적용되어 있는가?
- above-the-fold 주요 이미지는 과도하게 지연되지 않는가?
- 이미지 로딩 실패 fallback이 있는가?
- list image가 동일 크기로 표시되는가?
- background image가 불필요하게 큰 파일이 아닌가?
- 외부 이미지 URL이 깨질 경우 UI가 안전한가?
- alt text가 제공되는가?

---

### [실무]

lazy loading 예:

```jsx
<img
  src={festival.imageUrl}
  alt={`${festival.title} 대표 이미지`}
  loading="lazy"
/>
```

layout shift 방지 예:

```css
.festival-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
```

fallback 예:

```jsx
<img
  src={imageUrl || "/images/fallback-festival.png"}
  alt={`${festivalTitle} 대표 이미지`}
  onError={(event) => {
    event.currentTarget.src = "/images/fallback-festival.png";
  }}
/>
```

리뷰 코멘트 예:

```text
[Medium] 축제 카드 이미지에 크기 또는 aspect-ratio가 지정되어 있지 않아 이미지 로딩 시 layout shift가 발생할 수 있습니다. 고정 비율 컨테이너를 사용하는 것이 좋습니다.
```

---

### [FAQ]

Q. Image Performance Review는 왜 필요해?
A. 큰 이미지와 layout shift는 초기 로딩과 모바일 UX를 크게 저하시킬 수 있기 때문이다.

Q. 모든 이미지에 loading="lazy"를 붙이면 돼?
A. 아니다. 첫 화면 핵심 이미지는 lazy loading이 오히려 표시를 늦출 수 있다.

Q. 이미지 width와 height는 왜 필요해?
A. 브라우저가 공간을 미리 확보해 layout shift를 줄일 수 있기 때문이다.

Q. 이미지 fallback은 왜 필요해?
A. 외부 이미지 URL이 깨지거나 응답하지 않을 때 UI가 깨지는 것을 막기 위해 필요하다.

---

## 1.4 Bundle Review

### [개념]

Bundle Review는 프론트엔드 빌드 결과물의 크기와 초기 로딩 성능에 영향을 주는 dependency, import 방식, code splitting을 검토하는 과정이다.

번들 크기는 사용자의 첫 로딩 시간과 네트워크 비용에 직접 영향을 준다.

---

### [핵심]

Bundle Review 검토 항목:

- 큰 라이브러리를 전체 import하지 않는가?
- 사용하지 않는 dependency가 없는가?
- route-based lazy loading이 필요한가?
- chart / editor / map 같은 무거운 기능이 초기 번들에 포함되지 않는가?
- 중복 dependency가 없는가?
- 이미지와 font가 과도하게 포함되지 않는가?
- source map 공개 여부가 적절한가?
- dynamic import 경로가 안전한가?
- tree shaking이 가능한 import 방식인가?

---

### [실무]

나쁜 예:

```js
import _ from "lodash";
```

개선 예:

```js
import debounce from "lodash/debounce";
```

route lazy loading 예:

```jsx
const AdminPage = lazy(() => import("./pages/AdminPage"));
```

리뷰 코멘트 예:

```text
[Suggestion] 관리자 페이지는 일반 사용자 초기 화면에 필요하지 않습니다. 초기 번들 크기를 줄이기 위해 route-based lazy loading을 검토할 수 있습니다.
```

---

### [FAQ]

Q. Bundle Review는 왜 필요해?
A. 번들 크기가 커지면 초기 로딩 시간이 증가하고 모바일 네트워크에서 UX가 나빠질 수 있기 때문이다.

Q. 큰 라이브러리를 import하면 항상 문제야?
A. 항상은 아니지만 사용 범위가 작다면 부분 import나 대체 라이브러리를 검토해야 한다.

Q. route-based lazy loading은 언제 필요해?
A. 관리자 페이지, 차트, 에디터, 지도처럼 초기 화면에 필요 없는 큰 기능에 적합하다.

Q. source map은 항상 공개해도 돼?
A. 운영 정책에 따라 판단해야 한다. 공개 시 소스 구조가 노출될 수 있다.

---

# 2. Frontend Security Review Rules

## 2.1 Secret Exposure Review

### [개념]

Secret Exposure Review는 프론트엔드 코드, 환경 변수, 빌드 결과물에 민감한 secret key가 포함되어 있지 않은지 검토하는 과정이다.

브라우저에서 실행되는 프론트엔드 코드는 사용자에게 노출될 수 있으므로 secret을 저장하면 안 된다.

---

### [핵심]

프론트엔드에 저장하면 안 되는 값:

```text
JWT_SECRET
DB_PASSWORD
TOSS_SECRET_KEY
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
AWS_SECRET_KEY
ADMIN_PASSWORD
PRIVATE_KEY
SMTP_PASSWORD
OAuth Client Secret
```

검토 항목:

- `.env`에 secret key가 없는가?
- API Secret이 `REACT_APP_` 또는 `VITE_` prefix로 노출되지 않는가?
- 코드에 secret이 하드코딩되지 않았는가?
- Git에 secret이 커밋되지 않았는가?
- console.log에 secret이 출력되지 않는가?
- 빌드 결과물에 secret이 포함되지 않는가?
- public key와 secret key를 구분하는가?
- secret이 필요한 작업은 백엔드에서 처리하는가?

---

### [실무]

위험 예:

```env
REACT_APP_TOSS_SECRET_KEY=test_sk_xxxxx
REACT_APP_OPENAI_API_KEY=sk-xxxxx
```

문제:

```text
REACT_APP_ prefix가 붙은 값은 frontend bundle에 포함될 수 있음
→ 사용자 브라우저에서 노출 가능
```

리뷰 코멘트 예:

```text
[Critical] 프론트엔드 환경 변수에 TOSS_SECRET_KEY가 포함되어 있습니다. Secret Key는 브라우저에 노출되면 안 되므로 백엔드 환경 변수로 이동해야 합니다.
```

---

### [FAQ]

Q. 프론트엔드에 Secret Key를 넣어도 돼?
A. 안 된다. 브라우저 코드와 빌드 결과물에서 노출될 수 있다.

Q. REACT*APP* 또는 VITE\_ 환경 변수는 안전해?
A. 아니다. 해당 prefix 변수는 브라우저 번들에 포함될 수 있으므로 public 값만 넣어야 한다.

Q. API Secret이 필요한 기능은 어디서 처리해야 해?
A. 백엔드에서 처리해야 한다. 프론트엔드는 백엔드 API를 호출하는 구조가 안전하다.

Q. Secret 노출은 어떤 우선순위야?
A. Critical이다. 즉시 제거하고 키 폐기 또는 재발급까지 검토해야 한다.

---

## 2.2 XSS Review

### [개념]

XSS Review는 사용자 입력이나 외부 API 데이터를 HTML로 렌더링할 때 스크립트 실행 위험이 있는지 검토하는 과정이다.

React는 일반 문자열 렌더링을 escape하지만 `dangerouslySetInnerHTML` 사용 시 개발자가 직접 안전성을 책임져야 한다.

---

### [핵심]

XSS Review 검토 항목:

- `dangerouslySetInnerHTML` 사용 여부
- 사용자 입력 HTML 렌더링 여부
- markdown 렌더링 sanitize 여부
- rich text editor 결과 sanitize 여부
- 외부 API 응답을 HTML로 신뢰하지 않는가?
- URL 입력값 검증이 있는가?
- link protocol 검증이 있는가?
- script / event handler 제거가 있는가?
- DOMPurify 같은 sanitize 도구 사용 여부
- token 또는 개인정보가 XSS에 노출될 수 있는 저장소에 있는가?

---

### [실무]

위험한 예:

```jsx
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

HTML 렌더링이 필요한 경우 Flow:

```text
HTML Rendering Required
→ Sanitize
→ Allowed Tags Limit
→ Remove Script
→ Remove Event Handler
→ Validate Link Protocol
→ Render
```

리뷰 코멘트 예:

```text
[High] 사용자 입력을 sanitize 없이 dangerouslySetInnerHTML로 렌더링하고 있습니다. XSS 위험이 있으므로 DOMPurify 같은 sanitize 처리를 적용해야 합니다.
```

---

### [FAQ]

Q. XSS Review는 왜 필요해?
A. 사용자 입력이나 외부 데이터를 HTML로 렌더링하면 악성 스크립트가 실행될 수 있기 때문이다.

Q. React는 XSS를 자동으로 막아줘?
A. 일반 문자열 렌더링은 escape하지만 dangerouslySetInnerHTML을 사용하면 개발자가 직접 책임져야 한다.

Q. dangerouslySetInnerHTML은 절대 쓰면 안 돼?
A. 절대 금지는 아니지만 사용자 입력이나 외부 데이터를 넣을 때는 sanitize가 반드시 필요하다.

Q. markdown 렌더링도 sanitize가 필요해?
A. 필요하다. markdown이 HTML을 포함하거나 link protocol을 악용할 수 있기 때문이다.

---

## 2.3 Token Security Review

### [개념]

Token Security Review는 Access Token, Refresh Token, 사용자 정보가 브라우저 환경에서 안전하게 다뤄지는지 검토하는 과정이다.

프론트엔드 token 관리는 XSS, URL 노출, console 출력, storage 정책과 직접 연결된다.

---

### [핵심]

Token Security Review 검토 항목:

- token이 console에 출력되지 않는가?
- token이 URL query string에 포함되지 않는가?
- token이 localStorage에 저장될 경우 XSS 위험을 인지하는가?
- logout 시 token이 제거되는가?
- 만료 token이 계속 사용되지 않는가?
- Authorization header가 필요한 요청에만 붙는가?
- token이 error message에 노출되지 않는가?
- 사용자 개인정보를 storage에 과도하게 저장하지 않는가?
- refresh token 저장 방식이 프로젝트 보안 기준과 맞는가?

---

### [실무]

위험한 예:

```js
console.log("token", accessToken);
```

위험한 예:

```text
/callback?token=eyJhbGciOi...
```

리뷰 코멘트 예:

```text
[High] access token이 console에 출력되고 있습니다. 운영 브라우저 로그와 디버깅 도구에서 노출될 수 있으므로 제거해야 합니다.
```

```text
[Critical] access token이 URL query string에 포함되어 있습니다. 브라우저 기록, 서버 로그, referrer를 통해 유출될 수 있으므로 즉시 수정해야 합니다.
```

---

### [FAQ]

Q. Token Security Review는 왜 필요해?
A. token이 노출되면 사용자 계정 접근이나 API 오남용으로 이어질 수 있기 때문이다.

Q. token을 console.log로 찍어도 돼?
A. 권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

Q. token을 URL에 넣으면 왜 위험해?
A. 브라우저 기록, 서버 로그, referrer, 공유 URL에 노출될 수 있기 때문이다.

Q. localStorage token 저장은 무조건 금지야?
A. 무조건 금지는 아니지만 XSS 위험이 있으므로 보안 요구사항에 따라 httpOnly Cookie 방식도 검토해야 한다.

---

## 2.4 External Link Security Review

### [개념]

External Link Security Review는 외부 링크, 새 탭 링크, 사용자 입력 URL이 보안 위험 없이 처리되는지 검토하는 과정이다.

외부 링크는 reverse tabnabbing, 악성 URL, 잘못된 protocol 문제를 만들 수 있다.

---

### [핵심]

External Link Security Review 검토 항목:

- target="\_blank"에 rel="noreferrer" 또는 rel="noopener noreferrer"가 있는가?
- 사용자 입력 URL의 protocol을 검증하는가?
- javascript: URL을 차단하는가?
- 외부 링크와 내부 route를 구분하는가?
- 다운로드 링크가 신뢰 가능한가?
- 외부 이미지 / 링크 fallback이 있는가?
- 링크 텍스트가 목적을 설명하는가?

---

### [실무]

좋은 예:

```jsx
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  공식 사이트 열기
</a>
```

URL protocol 검증 개념:

```text
Allowed Protocol
→ https:
→ http: if allowed
Blocked Protocol
→ javascript:
→ data:
→ file:
```

리뷰 코멘트 예:

```text
[Medium] target=\"_blank\" 외부 링크에 rel 속성이 없습니다. reverse tabnabbing 방지를 위해 rel=\"noopener noreferrer\"를 추가해야 합니다.
```

---

### [FAQ]

Q. target="\_blank"에 rel이 왜 필요해?
A. 새 탭에서 원래 페이지를 조작할 수 있는 reverse tabnabbing 위험을 줄이기 위해 필요하다.

Q. rel="noreferrer"와 noopener는 뭐야?
A. noopener는 window.opener 접근을 막고, noreferrer는 referrer 정보 전달도 막는다.

Q. 사용자 입력 URL은 그대로 링크로 만들어도 돼?
A. 안 된다. javascript: 같은 위험한 protocol을 차단해야 한다.

Q. 내부 이동에도 a target="\_blank"를 써야 해?
A. 일반적인 SPA 내부 이동은 React Router Link를 사용하는 것이 좋다.

---

## 2.5 Frontend Permission Boundary Review

### [개념]

Frontend Permission Boundary Review는 프론트엔드 권한 UI 제한이 백엔드 권한 검증을 대체하지 않도록 설계되어 있는지 검토하는 과정이다.

프론트엔드는 사용자가 수정할 수 있는 환경이므로 권한 검증의 최종 책임을 가질 수 없다.

---

### [핵심]

검토 항목:

- 관리자 버튼 숨김만으로 권한 검증을 끝내지 않는가?
- 수정 / 삭제 API가 백엔드에서 권한 검증되는가?
- 프론트엔드 role 값만 신뢰하지 않는가?
- 권한 없음 403 응답을 처리하는가?
- 권한 변경 시 UI가 갱신되는가?
- ROLE_USER / ROLE_ADMIN naming이 백엔드와 일치하는가?
- 일반 사용자가 hidden button을 조작해도 서버에서 막을 수 있는가?

---

### [실무]

위험한 사고 방식:

```text
삭제 버튼을 관리자에게만 보여줌
→ 일반 사용자는 삭제할 수 없음
```

문제:

```text
브라우저에서 직접 API 요청 가능
→ 백엔드 권한 검증이 없으면 삭제 가능
```

올바른 기준:

```text
Frontend UI Permission
→ UX 목적

Backend Authorization
→ 실제 보안 검증
```

리뷰 코멘트 예:

```text
[High] 삭제 버튼은 관리자에게만 보이지만 삭제 API의 403 처리 흐름이 없습니다. UI 제한은 UX 목적이며 백엔드 권한 검증과 403 안내가 함께 필요합니다.
```

---

### [FAQ]

Q. 권한 버튼을 숨기면 보안이 되는 거야?
A. 아니다. UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. 프론트엔드 role 값을 믿어도 돼?
A. UI 표시에는 사용할 수 있지만 보안 판단의 최종 근거로 사용하면 안 된다.

Q. 403 응답도 프론트에서 처리해야 해?
A. 해야 한다. 권한 없음 상태를 사용자에게 안내해야 한다.

Q. Frontend Permission Boundary의 핵심은 뭐야?
A. 프론트엔드는 UX를 담당하고 실제 권한 검증은 백엔드가 담당해야 한다는 점이다.

---

# 3. Testability Review Rules

## 3.1 Testability Review

### [개념]

Testability Review는 프론트엔드 코드가 테스트하기 쉬운 구조인지 검토하는 과정이다.

테스트 코드가 없더라도 testability가 낮은 코드는 유지보수, 리팩토링, 버그 수정 비용이 커진다.

Review Agent는 코드가 mock 가능하고 사용자 흐름 단위로 검증 가능한지 확인해야 한다.

---

### [핵심]

테스트하기 좋은 코드 기준:

- UI와 비즈니스 로직이 적절히 분리됨
- API 호출이 module로 분리되어 mock 가능함
- 복잡한 로직이 pure function으로 분리됨
- side effect가 custom hook으로 분리 가능함
- 입력과 출력이 명확함
- 접근성 기반 query 사용 가능
- label, role, text가 명확함
- 시간 / 랜덤 값 / storage 접근이 분리됨
- routing, auth, API 의존성을 mock 가능함
- loading / error / empty / success 상태가 분리되어 있음

테스트하기 어려운 코드:

- 컴포넌트 내부에 모든 로직 집중
- API 호출 하드코딩
- 직접 window.location 변경
- DOM 구조에 강하게 의존
- 테스트 가능한 label / role 없음
- 시간 / 랜덤 값 직접 사용
- 외부 상태를 숨겨진 방식으로 참조
- 조건부 렌더링이 과도하게 복잡함

---

### [실무]

개선 방향:

```text
API Module 분리
→ Custom Hook 분리
→ Pure Function 분리
→ Dependency Injection 일부 적용
→ Role / Label 기반 UI 작성
→ Loading / Error / Empty 상태 분리
```

리뷰 코멘트 예:

```text
[Medium] 검색 validation 로직이 컴포넌트 내부 submit handler에 직접 작성되어 있어 단위 테스트가 어렵습니다. validateSearchForm 같은 pure function으로 분리하면 테스트 가능성이 좋아집니다.
```

---

### [FAQ]

Q. Testability Review는 왜 필요해?
A. 테스트하기 어려운 코드는 유지보수와 리팩토링 비용이 커지고 버그를 찾기 어렵기 때문이다.

Q. 테스트 코드가 없어도 testability를 리뷰해야 해?
A. 해야 한다. 테스트 가능성이 낮은 구조는 나중에 테스트를 추가하기 어렵다.

Q. 테스트하기 좋은 UI는 어떤 UI야?
A. role, label, text가 명확하고 사용자 행동 기준으로 접근 가능한 UI다.

Q. API 호출이 컴포넌트 내부에 있으면 테스트가 어려워?
A. API mock과 상태 제어가 어려워질 수 있으므로 API module이나 custom hook 분리가 좋다.

---

## 3.2 Unit Testability Review

### [개념]

Unit Testability Review는 validation, formatter, mapper, reducer, utility function 같은 작은 로직이 독립적으로 테스트 가능한지 검토하는 과정이다.

복잡한 로직을 컴포넌트에 직접 넣으면 테스트가 어렵고 재사용성이 낮아진다.

---

### [핵심]

Unit Test 대상:

- form validation
- API response mapper
- date formatter
- number formatter
- filter function
- sort function
- permission checker
- reducer
- custom hook 일부 로직
- file validation
- query parameter parser

---

### [실무]

나쁜 예:

```jsx
function LoginForm() {
  function handleSubmit(event) {
    event.preventDefault();

    if (!email.includes("@")) {
      setError("올바른 이메일 형식이 아닙니다.");
      return;
    }

    submit();
  }
}
```

개선 예:

```js
function validateLoginForm(values) {
  const errors = {};

  if (!values.email.includes("@")) {
    errors.email = "올바른 이메일 형식이 아닙니다.";
  }

  return errors;
}
```

리뷰 코멘트 예:

```text
[Suggestion] 로그인 validation이 submit handler에 직접 포함되어 있습니다. validateLoginForm 함수로 분리하면 단위 테스트와 재사용이 쉬워집니다.
```

---

### [FAQ]

Q. Unit Testability Review는 무엇을 봐?
A. validation, formatter, mapper, reducer 같은 작은 로직이 독립 함수로 테스트 가능한지 본다.

Q. 모든 함수를 분리해야 해?
A. 아니다. 복잡하거나 재사용되거나 버그 위험이 있는 로직을 우선 분리한다.

Q. form validation은 분리하는 게 좋아?
A. 복잡한 validation이면 pure function으로 분리하는 것이 테스트와 유지보수에 좋다.

Q. mapper 함수는 왜 테스트해야 해?
A. API 응답 구조와 화면 데이터 구조 변환 오류를 빠르게 잡을 수 있기 때문이다.

---

## 3.3 UI Interaction Testability Review

### [개념]

UI Interaction Testability Review는 사용자의 클릭, 입력, 제출, 이동, 에러 복구 같은 흐름을 테스트할 수 있는 구조인지 검토하는 과정이다.

프론트엔드 테스트는 구현 세부사항보다 사용자 행동과 화면 결과를 기준으로 작성하기 쉬워야 한다.

---

### [핵심]

UI Interaction Test 대상:

- input 입력
- button click
- form submit
- validation error 표시
- API success state
- API error state
- loading state
- empty state
- modal open / close
- protected route redirect
- pagination 더보기
- 검색 결과 표시
- 권한별 버튼 표시

---

### [실무]

테스트 가능한 UI 기준:

```md
- [ ] button text가 명확한가?
- [ ] input label이 있는가?
- [ ] error message가 text 또는 role로 접근 가능한가?
- [ ] loading text 또는 aria 상태가 있는가?
- [ ] modal role이 있는가?
- [ ] test id 없이도 role / label / text로 찾을 수 있는가?
```

나쁜 테스트 구조:

```text
CSS selector와 DOM 구조에 의존
→ .container > div:nth-child(2) 클릭
```

좋은 테스트 구조:

```text
Role / Label / Text 기반
→ screen.getByRole("button", { name: "저장" })
→ screen.getByLabelText("이메일")
```

리뷰 코멘트 예:

```text
[Medium] 검색 input에 label이 없어 테스트에서 사용자 관점 query로 접근하기 어렵습니다. 접근성과 테스트 가능성을 위해 label을 연결하는 것이 좋습니다.
```

---

### [FAQ]

Q. UI Interaction Testability Review는 왜 필요해?
A. 사용자의 실제 행동 흐름을 안정적으로 테스트할 수 있어야 기능 변경 시 회귀 버그를 줄일 수 있기 때문이다.

Q. test id를 많이 넣으면 좋아?
A. role, label, text로 찾을 수 있으면 우선 사용하고, 어려운 경우에만 test id를 고려한다.

Q. CSS selector 기반 테스트는 왜 나빠?
A. DOM 구조나 class 변경에 쉽게 깨져 사용자 흐름과 무관한 테스트가 될 수 있다.

Q. 접근성이 좋으면 테스트도 쉬워져?
A. 그렇다. label, role, text가 명확하면 사용자 관점 테스트가 쉬워진다.

---

## 3.4 Mocking Review

### [개념]

Mocking Review는 API, storage, router, auth context, time, random 값 같은 외부 의존성을 테스트에서 대체할 수 있는 구조인지 검토하는 과정이다.

mock이 어려운 코드는 테스트가 느리고 불안정해진다.

---

### [핵심]

Mocking 대상:

- API module
- Axios instance
- custom hook
- Auth Context
- Router navigation
- localStorage / sessionStorage
- Date / timer
- random id
- file upload
- WebSocket
- browser API

---

### [실무]

mock이 쉬운 구조:

```text
Component
→ useFestivalDetail hook
→ festivalApi module
```

mock이 어려운 구조:

```text
Component 내부에서 직접 axios.get 호출
→ 테스트에서 API 흐름 제어 어려움
```

리뷰 코멘트 예:

```text
[Medium] 컴포넌트 내부에서 직접 localStorage와 axios를 호출하고 있어 테스트에서 의존성 제어가 어렵습니다. authStorage와 api module로 분리하는 것이 좋습니다.
```

---

### [FAQ]

Q. Mocking Review는 왜 필요해?
A. 외부 의존성을 대체할 수 있어야 테스트가 빠르고 안정적으로 실행되기 때문이다.

Q. API module 분리가 mock에 도움이 돼?
A. 그렇다. API 호출 지점을 한 곳으로 모으면 테스트에서 성공, 실패 응답을 제어하기 쉽다.

Q. localStorage 직접 호출은 왜 테스트가 어려워?
A. 여러 컴포넌트에 흩어지면 초기화와 상태 검증이 복잡해진다. storage wrapper를 두면 관리가 쉽다.

Q. 시간이나 random 값도 mock해야 해?
A. 테스트 결과가 매번 달라질 수 있으므로 중요한 로직에서는 mock 가능하게 분리하는 것이 좋다.

---

# 4. Build and Deploy Review Rules

## 4.1 Build Risk Review

### [개념]

Build Risk Review는 프론트엔드 코드가 개발 서버에서는 동작하지만 운영 빌드에서 실패하거나 배포 후 문제를 일으킬 수 있는지 검토하는 과정이다.

개발 환경과 운영 빌드는 환경 변수, 파일 경로, 최적화, 대소문자, source map, asset path에서 차이가 날 수 있다.

---

### [핵심]

Build Risk Review 검토 항목:

- `npm run build` 또는 `yarn build`가 성공하는가?
- TypeScript error가 없는가?
- ESLint error가 build를 막지 않는가?
- 환경 변수가 누락되지 않았는가?
- CRA / Vite 환경 변수 prefix가 맞는가?
- localhost 하드코딩이 없는가?
- 파일명 대소문자 import 문제가 없는가?
- unused import가 과도하지 않은가?
- dynamic import 경로가 안전한가?
- asset path가 배포 환경과 맞는가?
- build output 경로가 백엔드 통합 배포와 맞는가?
- source map 공개 여부가 정책과 맞는가?

---

### [실무]

배포 전 확인:

```bash
npm run build
```

또는:

```bash
yarn build
```

가능하면 함께 확인:

```bash
npm run lint
npm test
```

리뷰 코멘트 예:

```text
[Critical] import 경로의 파일명 대소문자가 실제 파일명과 다릅니다. Windows에서는 동작할 수 있지만 Linux 배포 환경에서는 build 실패가 발생할 수 있습니다.
```

---

### [FAQ]

Q. Build Risk Review는 왜 필요해?
A. 개발 서버에서 정상이어도 운영 빌드에서 타입, 경로, 환경 변수 문제가 발생할 수 있기 때문이다.

Q. 개발 서버에서 잘 되면 build 확인 안 해도 돼?
A. 안 된다. 운영 빌드에서만 발생하는 문제가 있을 수 있다.

Q. Windows에서는 되는데 Linux 배포에서 import 에러가 나는 이유는?
A. Linux는 파일명 대소문자를 구분하므로 import 경로 대소문자 문제가 발생할 수 있다.

Q. npm run build 실패는 어떤 우선순위야?
A. Critical이다. 배포를 막는 문제다.

---

## 4.2 Environment Variable Review

### [개념]

Environment Variable Review는 프론트엔드 환경 변수가 안전하고 올바르게 분리되어 있으며 빌드 환경별로 정확히 주입되는지 검토하는 과정이다.

환경 변수 오류는 API 연결 실패, secret 노출, 빌드 실패의 주요 원인이다.

---

### [핵심]

Environment Variable Review 검토 항목:

- `.env`에 secret이 없는가?
- `.env.example`이 제공되는가?
- CRA는 `REACT_APP_` prefix를 사용하는가?
- Vite는 `VITE_` prefix를 사용하는가?
- API Base URL이 환경별로 분리되는가?
- 운영 빌드에 localhost가 남아 있지 않은가?
- public key와 secret key를 구분하는가?
- Kakao JavaScript Key 같은 public key에 도메인 제한이 있는가?
- env 값이 undefined일 때 fallback 또는 오류 처리가 있는가?
- `.env.local` 같은 로컬 파일이 Git에 커밋되지 않는가?

---

### [실무]

CRA 예:

```env
REACT_APP_API_BASE_URL=https://api.example.com
REACT_APP_KAKAO_JS_KEY=public_js_key
```

Vite 예:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_KAKAO_JS_KEY=public_js_key
```

위험 예:

```env
REACT_APP_DB_PASSWORD=secret
VITE_OPENAI_API_KEY=sk-xxxxx
```

리뷰 코멘트 예:

```text
[High] 운영 API baseURL이 http://localhost:8080으로 설정되어 있습니다. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하므로 환경 변수로 분리해야 합니다.
```

---

### [FAQ]

Q. Environment Variable Review는 왜 필요해?
A. API URL, secret 노출, 빌드 오류의 주요 원인이 환경 변수이기 때문이다.

Q. CRA 환경 변수 prefix는 뭐야?
A. 브라우저에 노출할 변수는 REACT*APP* prefix를 사용한다. 단, secret은 넣으면 안 된다.

Q. Vite 환경 변수 prefix는 뭐야?
A. 브라우저에 노출할 변수는 VITE\_ prefix를 사용한다. 단, secret은 넣으면 안 된다.

Q. 운영 코드에 localhost가 있으면 왜 문제야?
A. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하기 때문이다.

---

## 4.3 Asset Path Review

### [개념]

Asset Path Review는 이미지, 폰트, 정적 파일, manifest, favicon 경로가 개발과 배포 환경에서 모두 정상적으로 로드되는지 검토하는 과정이다.

asset path 오류는 개발 환경에서는 보이지 않다가 배포 후 404로 나타나는 경우가 많다.

---

### [핵심]

Asset Path Review 검토 항목:

- public asset 경로가 올바른가?
- 상대 경로와 절대 경로 사용이 배포 환경과 맞는가?
- basename 또는 homepage 설정이 필요한가?
- 이미지 import 방식이 bundler와 맞는가?
- CSS background-image 경로가 올바른가?
- favicon / manifest 경로가 배포 후 유효한가?
- 대소문자 import 문제가 없는가?
- 깨진 이미지 fallback이 있는가?
- CDN 경로가 환경별로 분리되는가?

---

### [실무]

문제 예:

```jsx
<img src="/images/banner.png" alt="배너" />
```

주의:

```text
앱이 도메인 root가 아닌 /app 하위 경로에 배포되면 /images/banner.png가 잘못된 경로가 될 수 있음
```

import 예:

```jsx
import bannerImage from "../assets/banner.png";

<img src={bannerImage} alt="배너" />;
```

리뷰 코멘트 예:

```text
[Medium] 정적 이미지 경로가 root 절대 경로로 작성되어 있습니다. 하위 경로 배포 환경에서는 asset 404가 발생할 수 있으므로 bundler import 또는 base path 설정을 확인해야 합니다.
```

---

### [FAQ]

Q. Asset Path Review는 왜 필요해?
A. 개발 환경에서는 보이던 이미지와 정적 파일이 배포 후 404가 날 수 있기 때문이다.

Q. public 폴더 이미지는 항상 /경로로 쓰면 돼?
A. root 배포에서는 가능하지만 하위 경로 배포라면 base path나 import 방식을 검토해야 한다.

Q. CSS background image도 리뷰해야 해?
A. 해야 한다. CSS 파일 기준 상대 경로가 배포 후 달라질 수 있다.

Q. favicon과 manifest도 확인해야 해?
A. 해야 한다. PWA, 브라우저 탭 표시, 모바일 홈 화면 추가에 영향을 줄 수 있다.

---

## 4.4 Deploy Configuration Review

### [개념]

Deploy Configuration Review는 프론트엔드 배포 방식이 정적 호스팅, 백엔드 통합 배포, CDN, Docker, CI/CD 환경과 맞는지 검토하는 과정이다.

배포 설정이 맞지 않으면 build는 성공해도 운영에서 API 연결, route refresh, asset loading 문제가 발생한다.

---

### [핵심]

Deploy Configuration Review 검토 항목:

- build output 경로가 배포 서버와 맞는가?
- Spring Boot 통합 배포 시 static 경로가 맞는가?
- SPA route fallback이 설정되어 있는가?
- API path가 fallback에서 제외되는가?
- CORS 설정이 운영 도메인과 맞는가?
- HTTPS 사용 여부가 적절한가?
- 환경 변수 주입 방식이 CI/CD와 맞는가?
- Docker build context가 올바른가?
- cache header 정책이 적절한가?
- source map 공개 여부가 정책과 맞는가?

---

### [실무]

백엔드 통합 배포 Flow:

```text
React Build
→ build output 생성
→ Spring Boot static 경로로 복사
→ API path는 Controller 처리
→ SPA path는 index.html fallback
→ Static asset은 그대로 제공
```

정적 호스팅 Flow:

```text
React Build
→ static hosting upload
→ rewrite all SPA routes to index.html
→ API baseURL points to backend domain
```

리뷰 코멘트 예:

```text
[High] BrowserRouter 기반 SPA인데 배포 서버의 rewrite 또는 index.html fallback 설정이 없습니다. 직접 URL 접근과 새로고침 시 404가 발생할 수 있습니다.
```

---

### [FAQ]

Q. Deploy Configuration Review는 왜 필요해?
A. build가 성공해도 route fallback, API URL, CORS, asset path 문제로 운영에서 실패할 수 있기 때문이다.

Q. Spring Boot 통합 배포에서 무엇을 확인해야 해?
A. React build output 위치, static serving, API path와 SPA fallback 충돌 여부를 확인해야 한다.

Q. 정적 호스팅에서는 무엇이 중요해?
A. SPA route rewrite, API baseURL, env 주입, asset cache 정책이 중요하다.

Q. build 성공이면 배포 성공이야?
A. 아니다. 배포 서버 설정과 runtime 환경까지 맞아야 한다.

---

# 5. Performance Security Testability Build Checklist

## 5.1 Performance Review Checklist

### [개념]

Performance Review Checklist는 Review Agent가 프론트엔드 성능 위험을 빠르게 검토할 때 사용하는 최종 점검 목록이다.

성능 리뷰는 사용자 흐름을 느리게 만드는 실제 위험 중심으로 수행한다.

---

### [핵심]

Performance Review Checklist:

```md
## Rendering

- [ ] 불필요한 state update가 없는가?
- [ ] 큰 리스트 렌더링 문제가 없는가?
- [ ] list key가 안정적인가?
- [ ] index key를 남용하지 않는가?
- [ ] 무거운 계산이 매 렌더링마다 반복되지 않는가?
- [ ] memoization이 필요한 지점에 적용되어 있는가?
- [ ] memoization을 남용하지 않는가?

## Large List

- [ ] pagination 또는 infinite scroll 전략이 있는가?
- [ ] hasNext 처리가 있는가?
- [ ] 더보기 중복 요청이 방지되는가?
- [ ] 필터 변경 시 목록이 초기화되는가?
- [ ] virtualization이 필요한 규모인가?

## Image

- [ ] 이미지 크기가 과도하지 않은가?
- [ ] lazy loading이 적절히 적용되는가?
- [ ] width / height 또는 aspect-ratio가 있는가?
- [ ] 이미지 fallback이 있는가?
- [ ] alt text가 제공되는가?

## Bundle

- [ ] 큰 라이브러리 전체 import가 없는가?
- [ ] 사용하지 않는 dependency가 없는가?
- [ ] route-based lazy loading이 필요한가?
- [ ] source map 공개 여부가 정책과 맞는가?
```

---

### [실무]

Performance Review 우선순위:

```text
User Flow Slowdown
→ Large List Freeze
→ Duplicate Rendering
→ Image Layout Shift
→ Bundle Size Increase
→ Memoization Suggestion
```

우선순위 판단:

```text
사용자 입력이 끊김
→ High

큰 리스트로 화면이 멈춤
→ High

index key로 렌더링 오류 가능
→ Medium

이미지 layout shift
→ Medium

route lazy loading 제안
→ Suggestion

불필요한 useMemo
→ Low
```

---

### [FAQ]

Q. Performance Review에서 가장 먼저 볼 것은 뭐야?
A. 실제 사용자 흐름 지연, 큰 리스트, 이미지, 중복 렌더링, 번들 크기 위험을 먼저 본다.

Q. 성능 문제는 모두 High야?
A. 아니다. 핵심 사용자 흐름을 방해하면 High, 개선 여지는 Medium 또는 Suggestion이다.

Q. memoization이 없으면 무조건 문제야?
A. 아니다. 실제 성능 문제가 있거나 계산 비용이 클 때만 필요하다.

Q. index key는 어떤 우선순위야?
A. 목록 변경 가능성이 있으면 Medium으로 볼 수 있다.

---

## 5.2 Security Review Checklist

### [개념]

Security Review Checklist는 Review Agent가 프론트엔드 보안 위험을 빠르게 검토할 때 사용하는 최종 점검 목록이다.

프론트엔드 보안 리뷰는 secret 노출, XSS, token 처리, 외부 링크, 권한 경계 문제를 우선 확인한다.

---

### [핵심]

Security Review Checklist:

```md
## Secret

- [ ] 프론트엔드 코드에 Secret Key가 없는가?
- [ ] REACT*APP* / VITE\_ 환경 변수에 secret이 없는가?
- [ ] API Secret이 브라우저 bundle에 포함되지 않는가?
- [ ] public key와 secret key가 구분되는가?

## XSS

- [ ] dangerouslySetInnerHTML 사용이 안전한가?
- [ ] 사용자 입력 HTML이 sanitize 되는가?
- [ ] markdown / rich text 렌더링이 sanitize 되는가?
- [ ] URL protocol 검증이 있는가?

## Token

- [ ] token이 console에 출력되지 않는가?
- [ ] token이 URL query string에 포함되지 않는가?
- [ ] logout 시 token이 제거되는가?
- [ ] Authorization header가 필요한 요청에만 포함되는가?

## External Link

- [ ] target="\_blank"에 rel="noopener noreferrer"가 있는가?
- [ ] 사용자 입력 URL에서 javascript: protocol을 차단하는가?

## Permission

- [ ] UI 권한 제한만으로 보안을 대체하지 않는가?
- [ ] 403 응답을 처리하는가?
- [ ] role naming이 백엔드와 일치하는가?
```

---

### [실무]

Security Review 우선순위:

```text
Secret Exposure
→ Token URL Exposure
→ Unsafe HTML Rendering
→ Token Console Logging
→ Permission Boundary Violation
→ External Link Missing rel
```

우선순위 판단:

```text
Secret Key 노출
→ Critical

Token URL 노출
→ Critical

sanitize 없는 dangerouslySetInnerHTML
→ High

token console 출력
→ High

권한 UI만 믿는 구조
→ High

target blank rel 누락
→ Medium
```

---

### [FAQ]

Q. Security Review에서 가장 먼저 볼 것은 뭐야?
A. Secret Key 노출, token URL 노출, XSS 위험, token console 출력, 권한 경계 문제를 먼저 본다.

Q. Secret Key 노출은 어떤 우선순위야?
A. Critical이다. 즉시 제거하고 키 폐기 또는 재발급까지 검토해야 한다.

Q. dangerouslySetInnerHTML은 어떤 우선순위야?
A. 사용자 입력이나 외부 데이터가 sanitize 없이 들어가면 High 이상으로 판단할 수 있다.

Q. target blank rel 누락은 어떤 우선순위야?
A. 보통 Medium이다. 외부 링크 보안 위험을 줄이기 위해 수정하는 것이 좋다.

---

## 5.3 Testability Review Checklist

### [개념]

Testability Review Checklist는 Review Agent가 프론트엔드 코드의 테스트 가능성을 검토할 때 사용하는 최종 점검 목록이다.

테스트 가능성은 코드 구조, 접근성, API 분리, 사용자 흐름 검증 가능성과 연결된다.

---

### [핵심]

Testability Review Checklist:

```md
## Structure

- [ ] UI와 비즈니스 로직이 적절히 분리되어 있는가?
- [ ] 복잡한 로직이 pure function으로 분리되어 있는가?
- [ ] custom hook으로 분리 가능한 side effect가 있는가?
- [ ] API 호출이 module로 분리되어 mock 가능한가?

## Unit

- [ ] validation 함수가 독립 테스트 가능한가?
- [ ] formatter / mapper 함수가 독립 테스트 가능한가?
- [ ] reducer가 pure function으로 테스트 가능한가?
- [ ] permission checker가 분리되어 있는가?

## UI Interaction

- [ ] input label이 있어 테스트 query가 가능한가?
- [ ] button text가 명확한가?
- [ ] loading / error / empty state가 테스트 가능한가?
- [ ] modal role이 있는가?
- [ ] protected route redirect를 테스트할 수 있는가?

## Mocking

- [ ] API module mock이 가능한가?
- [ ] Auth Context mock이 가능한가?
- [ ] Router navigation mock이 가능한가?
- [ ] storage 접근이 wrapper로 분리되어 있는가?
- [ ] 시간 / random 값이 테스트에서 제어 가능한가?
```

---

### [실무]

Testability Review 우선순위:

```text
Core User Flow Untestable
→ API Mock Impossible
→ Validation Logic Hidden
→ Accessibility Query Missing
→ Storage / Router Dependency Hardcoded
→ Test Id Suggestion
```

우선순위 판단:

```text
핵심 사용자 흐름 테스트 불가
→ Medium 또는 High

API mock 어려움
→ Medium

복잡한 validation 미분리
→ Medium

label 누락으로 테스트 어려움
→ Medium

test id 추가 제안
→ Suggestion
```

---

### [FAQ]

Q. Testability Review에서 가장 먼저 볼 것은 뭐야?
A. 핵심 사용자 흐름, API mock 가능성, validation 분리, role / label 기반 query 가능성을 먼저 본다.

Q. 테스트 코드가 없어도 testability를 봐야 해?
A. 해야 한다. 테스트하기 어려운 구조는 나중에 테스트 추가와 리팩토링을 어렵게 만든다.

Q. API mock이 어려운 구조는 어떤 우선순위야?
A. 보통 Medium이다. 핵심 흐름 검증을 막으면 High로 볼 수 있다.

Q. test id는 언제 추가해?
A. role, label, text로 접근하기 어려운 경우에만 보조적으로 사용한다.

---

## 5.4 Build Deploy Review Checklist

### [개념]

Build Deploy Review Checklist는 Review Agent가 프론트엔드 build와 deploy 위험을 검토할 때 사용하는 최종 점검 목록이다.

빌드와 배포 문제는 기능 구현이 끝난 뒤에도 release를 차단할 수 있으므로 Critical / High 기준으로 확인한다.

---

### [핵심]

Build Deploy Review Checklist:

```md
## Build

- [ ] npm run build 또는 yarn build가 성공하는가?
- [ ] TypeScript error가 없는가?
- [ ] ESLint error가 build를 막지 않는가?
- [ ] import path 대소문자 문제가 없는가?
- [ ] dynamic import 경로가 안전한가?

## Environment

- [ ] .env에 secret이 없는가?
- [ ] .env.example이 제공되는가?
- [ ] CRA / Vite env prefix가 맞는가?
- [ ] API Base URL이 환경별로 분리되는가?
- [ ] 운영 빌드에 localhost가 없는가?

## Asset

- [ ] 이미지 / 폰트 / favicon / manifest 경로가 올바른가?
- [ ] 하위 경로 배포 시 asset path가 안전한가?
- [ ] CSS background-image 경로가 올바른가?
- [ ] 깨진 이미지 fallback이 있는가?

## Deploy

- [ ] build output 경로가 배포 서버와 맞는가?
- [ ] SPA route fallback이 설정되어 있는가?
- [ ] API path는 fallback 대상에서 제외되는가?
- [ ] CORS 설정이 운영 도메인과 맞는가?
- [ ] source map 공개 여부가 정책과 맞는가?
```

---

### [실무]

Build Deploy Review 우선순위:

```text
Build Failure
→ Secret Env Exposure
→ Production API URL Failure
→ SPA Refresh 404
→ Asset 404
→ Source Map Policy
```

우선순위 판단:

```text
build 실패
→ Critical

secret env 노출
→ Critical

운영 localhost 잔존
→ High

SPA 새로고침 404
→ High

asset path 오류
→ Medium

source map 정책 미확인
→ Low 또는 Medium
```

---

### [FAQ]

Q. Build Deploy Review에서 가장 먼저 볼 것은 뭐야?
A. build 실패, secret env 노출, 운영 API URL, SPA refresh fallback, asset path를 먼저 본다.

Q. build 실패는 어떤 우선순위야?
A. Critical이다. 배포를 막는 문제다.

Q. 운영 localhost 잔존은 어떤 우선순위야?
A. High다. 운영 사용자의 브라우저에서 API 연결이 실패할 수 있다.

Q. SPA refresh 404는 어떤 우선순위야?
A. 주요 페이지 직접 접근을 막으므로 High로 판단할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Rendering Performance Review는 뭐야?
A. React 화면이 불필요하게 자주 렌더링되거나 무거운 계산으로 사용자 경험이 저하되는지 검토하는 과정이다.

Q. React.memo를 모든 컴포넌트에 써야 해?
A. 아니다. 실제 성능 문제가 있거나 props 참조 안정성이 필요한 경우에 사용한다.

Q. map에서 index를 key로 써도 돼?
A. 정적 목록이면 가능할 수 있지만 정렬, 삭제, 추가가 발생하면 렌더링 버그가 생길 수 있다.

Q. Large List Review는 뭐야?
A. 많은 데이터를 렌더링하는 목록 화면이 pagination, infinite scroll, virtualization 전략을 적절히 사용하는지 검토하는 과정이다.

Q. 무한 스크롤에서 가장 중요한 것은 뭐야?
A. hasNext 처리, 중복 요청 방지, loading 표시, page 병합 안정성이다.

Q. Image Performance Review는 뭐야?
A. 이미지 파일 크기, 로딩 방식, 크기 지정, fallback 처리가 화면 성능과 UX를 해치지 않는지 검토하는 과정이다.

Q. 모든 이미지에 loading="lazy"를 붙이면 돼?
A. 아니다. 첫 화면 핵심 이미지는 lazy loading이 오히려 표시를 늦출 수 있다.

Q. 이미지 width와 height는 왜 필요해?
A. 브라우저가 공간을 미리 확보해 layout shift를 줄일 수 있기 때문이다.

Q. Bundle Review는 뭐야?
A. 프론트엔드 빌드 결과물의 크기와 초기 로딩 성능에 영향을 주는 dependency, import 방식, code splitting을 검토하는 과정이다.

Q. route-based lazy loading은 언제 필요해?
A. 관리자 페이지, 차트, 에디터, 지도처럼 초기 화면에 필요 없는 큰 기능에 적합하다.

Q. Secret Exposure Review는 뭐야?
A. 프론트엔드 코드, 환경 변수, 빌드 결과물에 민감한 secret key가 포함되어 있지 않은지 검토하는 과정이다.

Q. 프론트엔드에 Secret Key를 넣어도 돼?
A. 안 된다. 브라우저 코드와 빌드 결과물에서 노출될 수 있다.

Q. REACT*APP* 또는 VITE\_ 환경 변수는 안전해?
A. 아니다. 해당 prefix 변수는 브라우저 번들에 포함될 수 있으므로 public 값만 넣어야 한다.

Q. XSS Review는 뭐야?
A. 사용자 입력이나 외부 API 데이터를 HTML로 렌더링할 때 스크립트 실행 위험이 있는지 검토하는 과정이다.

Q. React는 XSS를 자동으로 막아줘?
A. 일반 문자열 렌더링은 escape하지만 dangerouslySetInnerHTML을 사용하면 개발자가 직접 책임져야 한다.

Q. dangerouslySetInnerHTML은 절대 쓰면 안 돼?
A. 절대 금지는 아니지만 사용자 입력이나 외부 데이터를 넣을 때는 sanitize가 반드시 필요하다.

Q. Token Security Review는 뭐야?
A. Access Token, Refresh Token, 사용자 정보가 브라우저 환경에서 안전하게 다뤄지는지 검토하는 과정이다.

Q. token을 console.log로 찍어도 돼?
A. 권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

Q. token을 URL에 넣으면 왜 위험해?
A. 브라우저 기록, 서버 로그, referrer, 공유 URL에 노출될 수 있기 때문이다.

Q. External Link Security Review는 뭐야?
A. 외부 링크, 새 탭 링크, 사용자 입력 URL이 보안 위험 없이 처리되는지 검토하는 과정이다.

Q. target="\_blank"에 rel이 왜 필요해?
A. 새 탭에서 원래 페이지를 조작할 수 있는 reverse tabnabbing 위험을 줄이기 위해 필요하다.

Q. 사용자 입력 URL은 그대로 링크로 만들어도 돼?
A. 안 된다. javascript: 같은 위험한 protocol을 차단해야 한다.

Q. Frontend Permission Boundary Review는 뭐야?
A. 프론트엔드 권한 UI 제한이 백엔드 권한 검증을 대체하지 않도록 설계되어 있는지 검토하는 과정이다.

Q. 권한 버튼을 숨기면 보안이 되는 거야?
A. 아니다. UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. Testability Review는 뭐야?
A. 프론트엔드 코드가 테스트하기 쉬운 구조인지 검토하는 과정이다.

Q. 테스트 코드가 없어도 testability를 리뷰해야 해?
A. 해야 한다. 테스트하기 어려운 구조는 나중에 테스트 추가와 리팩토링을 어렵게 만든다.

Q. Unit Testability Review는 뭐야?
A. validation, formatter, mapper, reducer, utility function 같은 작은 로직이 독립적으로 테스트 가능한지 검토하는 과정이다.

Q. UI Interaction Testability Review는 뭐야?
A. 사용자의 클릭, 입력, 제출, 이동, 에러 복구 같은 흐름을 테스트할 수 있는 구조인지 검토하는 과정이다.

Q. CSS selector 기반 테스트는 왜 나빠?
A. DOM 구조나 class 변경에 쉽게 깨져 사용자 흐름과 무관한 테스트가 될 수 있다.

Q. Mocking Review는 뭐야?
A. API, storage, router, auth context, time, random 값 같은 외부 의존성을 테스트에서 대체할 수 있는 구조인지 검토하는 과정이다.

Q. API module 분리가 mock에 도움이 돼?
A. 그렇다. API 호출 지점을 한 곳으로 모으면 테스트에서 성공, 실패 응답을 제어하기 쉽다.

Q. Build Risk Review는 뭐야?
A. 프론트엔드 코드가 개발 서버에서는 동작하지만 운영 빌드에서 실패하거나 배포 후 문제를 일으킬 수 있는지 검토하는 과정이다.

Q. npm run build 실패는 어떤 우선순위야?
A. Critical이다. 배포를 막는 문제다.

Q. Windows에서는 되는데 Linux 배포에서 import 에러가 나는 이유는?
A. Linux는 파일명 대소문자를 구분하므로 import 경로 대소문자 문제가 발생할 수 있다.

Q. Environment Variable Review는 뭐야?
A. 프론트엔드 환경 변수가 안전하고 올바르게 분리되어 있으며 빌드 환경별로 정확히 주입되는지 검토하는 과정이다.

Q. 운영 코드에 localhost가 있으면 왜 문제야?
A. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하기 때문이다.

Q. Asset Path Review는 뭐야?
A. 이미지, 폰트, 정적 파일, manifest, favicon 경로가 개발과 배포 환경에서 모두 정상적으로 로드되는지 검토하는 과정이다.

Q. Deploy Configuration Review는 뭐야?
A. 프론트엔드 배포 방식이 정적 호스팅, 백엔드 통합 배포, CDN, Docker, CI/CD 환경과 맞는지 검토하는 과정이다.

Q. build 성공이면 배포 성공이야?
A. 아니다. 배포 서버 설정과 runtime 환경까지 맞아야 한다.

Q. Performance Security Testability Build Review의 최종 목적은 뭐야?
A. 프론트엔드 코드가 성능, 보안, 테스트 가능성, 빌드와 배포 측면에서 운영 가능한 수준인지 판단하는 것이다.

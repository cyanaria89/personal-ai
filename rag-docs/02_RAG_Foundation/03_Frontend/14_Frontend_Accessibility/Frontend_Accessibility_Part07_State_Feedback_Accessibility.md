# Frontend Accessibility Part07 - State Feedback Accessibility

---

# 1. State Feedback Accessibility

## 1.1 State Feedback Purpose

### [개념]

State Feedback Accessibility는 Loading, Success, Error, Empty, Disabled, Pending, Offline 같은 UI 상태를 사용자가 명확히 인식할 수 있게 만드는 기준이다.

Frontend UI는 데이터 요청, 저장, 삭제, 검색, 필터링, 인증, 결제 과정에서 상태가 자주 바뀐다.

상태 변화는 시각 사용자뿐 아니라 키보드 사용자, 스크린 리더 사용자, 저시력 사용자도 이해할 수 있어야 한다.

---

### [핵심]

State Feedback 핵심 상태:

- Loading State
- Success State
- Error State
- Empty State
- Disabled State
- Pending State
- Offline State
- Retry State
- Validation State
- Search Result State
- Upload State
- Submit State
- Permission State

핵심 기준:

- 상태 메시지 제공
- spinner only 지양
- color only 지양
- icon only 지양
- `role="status"` 고려
- `role="alert"` 고려
- `aria-live` 고려
- `aria-busy` 고려
- retry action 제공
- focus management 검토
- keyboard 조작 가능
- 사용자용 문구 제공

---

### [실무]

State Feedback 검토 Flow:

```text
UI 상태 확인
→ 사용자에게 전달해야 하는 상태인지 판단
→ 시각 메시지 제공
→ 보조기술 전달 방식 선택
→ focus 이동 필요 여부 판단
→ retry / next action 제공
→ Testing Library Query 검증
→ Manual Keyboard Check
```

실무 기준:

- Loading에는 텍스트 상태 제공
- Success에는 완료 메시지 제공
- Error에는 원인과 다음 행동 제공
- Empty에는 빈 상태 이유와 다음 행동 제공
- Disabled에는 이유 제공 고려
- Pending에는 중복 제출 방지
- Offline에는 네트워크 상태와 재시도 안내
- 상태 메시지는 내부 시스템 문구가 아니라 사용자용 문구로 작성
- 상태 변경이 중요하면 live region 사용 검토
- 상태 변경 후 focus를 빼앗지 않도록 주의

---

### [FAQ]

Q. State Feedback Accessibility는 왜 필요해?
A. 사용자가 현재 화면이 로딩 중인지, 성공했는지, 실패했는지, 데이터가 없는지 이해해야 하기 때문이다.

Q. 상태 메시지는 화면에 보이면 충분해?
A. 아니다. 중요한 상태 변화는 보조기술 사용자도 인식할 수 있게 role status, role alert, aria-live 등을 고려해야 한다.

Q. spinner만 보여주면 안 돼?
A. 스크린 리더 사용자는 spinner 의미를 알기 어렵다. loading text를 함께 제공해야 한다.

Q. 상태 문구는 기술적으로 작성해도 돼?
A. 권장하지 않는다. 사용자가 이해하고 다음 행동을 알 수 있는 문구로 작성해야 한다.

---

# 2. Loading State Accessibility

## 2.1 Loading State Basics

### [개념]

Loading State는 데이터 요청, 화면 전환, 검색, 저장, 업로드 같은 비동기 작업이 진행 중임을 사용자에게 알려주는 상태다.

Loading State는 spinner나 skeleton만으로 끝내지 않고 텍스트 상태와 보조기술 전달을 함께 고려해야 한다.

---

### [핵심]

Loading State 구성:

- loading text
- spinner
- skeleton
- progress indicator
- `role="status"`
- `aria-live="polite"`
- `aria-busy`
- disabled action
- pending button text
- timeout / retry handling

Loading State 유형:

- Page Loading
- Section Loading
- Button Loading
- Search Loading
- Upload Loading
- Infinite Scroll Loading
- Skeleton Loading
- Background Refresh

---

### [실무]

기본 Loading:

```jsx
<div role="status" aria-live="polite">
  데이터를 불러오는 중입니다.
</div>
```

Spinner + Text:

```jsx
<div role="status">
  <Spinner aria-hidden="true" />
  <span>목록을 불러오는 중입니다.</span>
</div>
```

Section Loading:

```jsx
<section aria-busy={loading}>
  {loading && <div role="status">축제 정보를 불러오는 중입니다.</div>}

  {!loading && <FestivalList />}
</section>
```

Button Loading:

```jsx
<button type="submit" disabled={loading} aria-busy={loading}>
  {loading ? "저장 중..." : "저장"}
</button>
```

실무 기준:

- spinner 단독 사용 지양
- loading text는 짧고 명확하게 작성
- skeleton은 장식이면 `aria-hidden`
- section 단위 로딩에는 `aria-busy` 고려
- button loading은 text 변경과 disabled 처리 고려
- loading 중 중복 클릭 / 중복 제출 방지
- loading이 길어질 수 있으면 취소 / 재시도 / 안내 제공 검토
- live region 남발 금지

---

### [FAQ]

Q. Loading State에는 무엇이 필요해?
A. 사용자가 현재 작업이 진행 중임을 알 수 있는 텍스트와 시각적 표시가 필요하다.

Q. spinner만 있으면 왜 부족해?
A. 스크린 리더 사용자는 spinner 의미를 알기 어렵고, 시각 사용자도 무엇이 진행 중인지 모를 수 있다.

Q. aria-busy는 어디에 써?
A. 특정 section이나 button이 처리 중임을 전달할 때 사용할 수 있다.

Q. loading text는 어떻게 써?
A. “데이터를 불러오는 중입니다”, “저장 중입니다”처럼 현재 작업을 구체적으로 작성한다.

---

## 2.2 Skeleton Loading

### [개념]

Skeleton Loading은 실제 콘텐츠가 로드되기 전 콘텐츠 형태를 미리 보여주는 loading UI다.

Skeleton은 시각적 기대감을 줄 수 있지만 보조기술에는 의미 없는 장식으로 처리하고 별도 loading message를 제공하는 것이 좋다.

---

### [핵심]

Skeleton 접근성 기준:

- skeleton 자체는 장식 처리
- `aria-hidden="true"` 고려
- 별도 loading text 제공
- `role="status"` 제공 가능
- animation reduced motion 고려
- shimmer 과도 사용 주의
- 실제 콘텐츠와 혼동 방지
- loading 완료 후 skeleton 제거

---

### [실무]

Skeleton + Status:

```jsx
<div aria-hidden="true" className="skeleton-list">
  <div className="skeleton-card" />
  <div className="skeleton-card" />
  <div className="skeleton-card" />
</div>

<div role="status">
  축제 목록을 불러오는 중입니다.
</div>
```

Reduced Motion:

```css
@media (prefers-reduced-motion: reduce) {
  .skeleton-card {
    animation: none;
  }
}
```

실무 기준:

- skeleton은 보조기술이 읽지 않게 처리
- loading message는 별도로 제공
- skeleton animation은 reduced motion 고려
- loading 완료 후 실제 콘텐츠로 대체
- skeleton과 실제 콘텐츠가 동시에 중복 노출되지 않게 함
- skeleton만 있고 text가 없으면 접근성 검토 대상

---

### [FAQ]

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

Q. Skeleton만 있으면 loading 표시가 충분해?
A. 아니다. 보조기술 사용자에게 loading 상태를 전달하는 텍스트가 필요하다.

Q. Skeleton shimmer는 접근성 문제가 될 수 있어?
A. 과도한 움직임은 불편을 줄 수 있으므로 prefers-reduced-motion을 고려한다.

Q. Skeleton이 실제 콘텐츠처럼 읽히면 문제야?
A. 문제다. 의미 없는 placeholder가 콘텐츠처럼 전달될 수 있다.

---

## 2.3 Button Pending State

### [개념]

Button Pending State는 사용자가 버튼을 눌러 비동기 작업이 진행되는 동안 버튼 상태를 변경해 중복 실행을 방지하고 진행 중임을 알리는 상태다.

저장, 로그인, 결제, 업로드, 삭제 같은 작업에서 중요하다.

---

### [핵심]

Button Pending 기준:

- 버튼 텍스트 변경
- `disabled` 처리 고려
- `aria-busy` 고려
- 중복 제출 방지
- focus 유지
- 결과 메시지 제공
- 실패 시 retry 가능
- 성공 시 다음 상태 제공

사용 대상:

- 로그인
- 회원가입
- 저장
- 삭제
- 결제
- 업로드
- 검색
- 재시도

---

### [실무]

저장 버튼:

```jsx
<button type="submit" disabled={saving} aria-busy={saving}>
  {saving ? "저장 중..." : "저장"}
</button>
```

삭제 버튼:

```jsx
<button type="button" disabled={deleting} aria-busy={deleting}>
  {deleting ? "삭제 중..." : "삭제"}
</button>
```

결제 버튼:

```jsx
<button type="submit" disabled={paying} aria-busy={paying}>
  {paying ? "결제 처리 중..." : "결제하기"}
</button>
```

실무 기준:

- 버튼 클릭 후 pending text 제공
- pending 중 중복 클릭 방지
- disabled 상태에서도 현재 작업을 이해할 수 있어야 함
- focus가 갑자기 사라지지 않게 함
- 작업 완료 후 success 또는 error message 제공
- 네트워크 실패 시 retry action 제공
- 단순 spinner만 버튼 안에 넣지 않음

---

### [FAQ]

Q. 버튼 loading 상태는 어떻게 표시해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 중복 실행을 막기 위해 disabled와 aria-busy를 고려한다.

Q. pending 중 버튼을 disabled 해도 돼?
A. 가능하다. 다만 사용자가 현재 진행 중임을 알 수 있게 텍스트 상태를 제공해야 한다.

Q. 버튼 안 spinner만 보여주면 돼?
A. 권장하지 않는다. 버튼의 작업 상태를 설명하는 텍스트가 필요하다.

Q. pending이 끝나면 뭘 보여줘야 해?
A. 성공 메시지, 오류 메시지, 다음 화면 이동 등 결과 상태를 명확히 제공해야 한다.

---

# 3. Success State Accessibility

## 3.1 Success Message

### [개념]

Success State는 저장, 삭제, 제출, 업로드, 결제 같은 작업이 성공적으로 완료되었음을 사용자에게 알려주는 상태다.

Success Message는 사용자가 작업 결과를 확신하고 다음 행동을 결정할 수 있게 한다.

---

### [핵심]

Success State 구성:

- success text
- `role="status"` 고려
- toast message
- inline success
- page success
- next action
- focus management 검토
- color only success 금지
- icon only success 금지

좋은 문구:

- 저장되었습니다.
- 리뷰가 등록되었습니다.
- 이미지 업로드가 완료되었습니다.
- 결제가 완료되었습니다.
- 비밀번호가 변경되었습니다.

나쁜 문구:

- OK
- Done
- Success
- 처리됨
- 200

---

### [실무]

Inline Success:

```jsx
<div role="status">저장되었습니다.</div>
```

Toast Success:

```jsx
<div role="status" aria-live="polite">
  리뷰가 등록되었습니다.
</div>
```

Form Success:

```jsx
<section aria-labelledby="success-title">
  <h2 id="success-title">회원가입이 완료되었습니다.</h2>
  <p>이제 로그인할 수 있습니다.</p>
  <Link to="/login">로그인하러 가기</Link>
</section>
```

실무 기준:

- 성공 상태는 텍스트로 제공
- 성공 icon은 장식 처리 가능
- 저장 완료 같은 non-critical 상태는 `role="status"` 고려
- 성공 후 다음 행동이 필요하면 link 또는 button 제공
- toast가 너무 빨리 사라지지 않게 함
- 성공 메시지와 화면 이동이 동시에 일어날 때 사용자 인식 여부 검토

---

### [FAQ]

Q. Success Message는 왜 필요해?
A. 사용자가 작업이 정상 완료되었는지 확신할 수 있어야 하기 때문이다.

Q. 성공 상태에 초록색 체크 아이콘만 보여주면 돼?
A. 아니다. 텍스트로 성공 상태를 함께 제공해야 한다.

Q. 성공 메시지에는 role status를 써도 돼?
A. 저장 완료 같은 긴급하지 않은 상태 알림에는 role status를 사용할 수 있다.

Q. 성공 후 바로 페이지 이동하면 메시지는 필요 없어?
A. 상황에 따라 다르다. 사용자가 결과를 인식하기 어려우면 완료 화면이나 명확한 상태 표시가 필요하다.

---

## 3.2 Toast Success Accessibility

### [개념]

Toast Success는 화면 한쪽에 잠시 나타나는 성공 알림이다.

Toast는 사용자에게 중요한 상태를 전달할 수 있지만 너무 빨리 사라지거나 keyboard focus와 무관하게 표시되면 놓치기 쉽다.

---

### [핵심]

Toast Success 기준:

- 짧은 성공 문구
- `role="status"` 고려
- 충분한 표시 시간
- 자동 닫힘 주의
- 닫기 버튼 제공 고려
- keyboard 접근 가능한 action
- 색상만으로 성공 표시 금지
- 중복 toast 관리

---

### [실무]

Toast 예:

```jsx
<div role="status" aria-live="polite">
  저장되었습니다.
</div>
```

Action Toast:

```jsx
<div role="status" aria-live="polite">
  리뷰가 삭제되었습니다.
  <button type="button" onClick={onUndo}>
    실행 취소
  </button>
</div>
```

실무 기준:

- toast는 텍스트를 포함
- 중요한 상태는 role status 또는 live region 고려
- action이 있는 toast는 keyboard로 접근 가능해야 함
- 자동 닫힘 시간이 너무 짧지 않게 함
- 여러 toast가 동시에 쌓이면 읽기 어려울 수 있음
- 삭제 성공 후 undo 제공 시 focus와 keyboard 조작 검토

---

### [FAQ]

Q. Toast에도 접근성이 필요해?
A. 필요하다. Toast가 중요한 상태를 전달하면 보조기술 사용자도 인식해야 한다.

Q. Toast가 자동으로 사라져도 돼?
A. 가능하지만 너무 빨리 사라지면 사용자가 읽기 어렵다. 중요한 메시지는 충분한 시간이나 닫기 제어를 고려한다.

Q. Toast에 role status를 붙이면 돼?
A. 긴급하지 않은 성공 알림에는 role status를 고려할 수 있다.

Q. Toast 안 버튼은 keyboard로 접근 가능해야 해?
A. 그렇다. 실행 취소 같은 action이 있으면 keyboard로 조작 가능해야 한다.

---

# 4. Error State Accessibility

## 4.1 Error State Basics

### [개념]

Error State는 요청 실패, 저장 실패, 로그인 실패, 결제 실패, validation 실패, 권한 문제처럼 사용자가 원하는 작업을 완료하지 못한 상태다.

Error State는 사용자가 오류를 인식하고 다음 행동을 결정할 수 있게 작성해야 한다.

---

### [핵심]

Error State 구성:

- error title
- error message
- field error
- global error
- page error
- retry action
- support action
- `role="alert"` 고려
- focus management 검토
- 내부 정보 노출 방지

좋은 오류 문구:

- 저장에 실패했습니다. 잠시 후 다시 시도해 주세요.
- 이메일을 입력해 주세요.
- 결제 수단을 확인한 후 다시 시도해 주세요.
- 네트워크 연결을 확인해 주세요.

나쁜 오류 문구:

- Error
- Failed
- Exception
- 500
- null
- undefined
- token expired stack trace

---

### [실무]

Page Error:

```jsx
<section role="alert">
  <h2>축제 정보를 불러오지 못했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Form Error:

```jsx
<div role="alert">이메일 또는 비밀번호가 올바르지 않습니다.</div>
```

Field Error:

```jsx
<input
  id="email"
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>;
{
  error && (
    <p id="email-error" role="alert">
      이메일을 입력해 주세요.
    </p>
  );
}
```

실무 기준:

- 오류는 텍스트로 명확히 제공
- 색상만으로 오류 표시 금지
- field error는 input과 연결
- page error는 retry action 제공
- 내부 서버 에러는 사용자용 문구로 변환
- 인증 실패는 보안상 과도하게 구체화하지 않음
- 긴 Form에서는 Error Summary 고려
- 오류 발생 후 focus 이동이 필요한지 검토

---

### [FAQ]

Q. Error State에는 무엇이 필요해?
A. 오류를 설명하는 문구, 수정 방법, 재시도 가능 여부, 필요한 경우 focus 이동이 필요하다.

Q. 서버 에러를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 되지만 alert 남발은 사용자를 방해할 수 있다.

Q. 오류 문구는 어떻게 써?
A. 사용자가 무엇을 수정하거나 다시 시도해야 하는지 짧고 명확하게 작성한다.

---

## 4.2 Field Error vs Global Error

### [개념]

Field Error는 특정 입력 필드에 연결된 오류이고 Global Error는 Form 전체, 서버 요청, 인증 실패, 권한 문제처럼 특정 field에만 연결하기 어려운 오류다.

두 오류는 역할이 다르므로 상황에 맞게 구분해야 한다.

---

### [핵심]

Field Error 대상:

- 필수값 누락
- 형식 오류
- 글자 수 오류
- 범위 오류
- 비밀번호 불일치
- 파일 형식 오류
- select 미선택

Global Error 대상:

- 로그인 실패
- 서버 저장 실패
- 네트워크 오류
- 결제 실패
- 권한 없음
- 세션 만료
- 전체 제출 실패

---

### [실무]

Field Error:

```jsx
<label htmlFor="nickname">닉네임</label>
<input
  id="nickname"
  aria-invalid={Boolean(errors.nickname)}
  aria-describedby={errors.nickname ? "nickname-error" : undefined}
/>
{errors.nickname && (
  <p id="nickname-error" role="alert">
    닉네임을 입력해 주세요.
  </p>
)}
```

Global Error:

```jsx
{
  submitError && (
    <div role="alert">저장에 실패했습니다. 잠시 후 다시 시도해 주세요.</div>
  );
}
```

함께 사용하는 경우:

```text
Form Submit 실패
→ Form 상단 Global Error Summary
→ 각 input 아래 Field Error
→ Error Summary Link로 Field 이동
```

실무 기준:

- field 수정이 필요한 오류는 field error 제공
- 전체 요청 실패는 global error 제공
- 로그인 실패는 global error로 처리하는 경우가 많음
- global error만으로 field error를 대체하지 않음
- field error 문구와 error summary 문구 일관성 유지
- role alert 남발 주의

---

### [FAQ]

Q. Field Error와 Global Error 차이는?
A. Field Error는 특정 input의 오류이고 Global Error는 Form 전체나 요청 실패 같은 전체 상태 오류다.

Q. 로그인 실패는 field error야 global error야?
A. 보안상 어떤 필드가 틀렸는지 구체화하지 않고 global error로 처리하는 경우가 많다.

Q. Global Error만 보여주면 충분해?
A. field 수정이 필요한 오류라면 field error도 함께 제공하는 것이 좋다.

Q. 서버 저장 실패는 어디에 표시해?
A. 일반적으로 Form 상단이나 관련 section에 global error로 표시하고 retry action을 제공한다.

---

## 4.3 Retry and Recovery Action

### [개념]

Retry and Recovery Action은 오류 발생 후 사용자가 다시 시도하거나 문제를 해결할 수 있게 하는 행동 수단이다.

Error State는 단순히 실패를 알리는 것에서 끝나지 않고 다음 행동을 제공해야 한다.

---

### [핵심]

Recovery Action 예:

- 다시 시도
- 새로고침
- 입력값 수정
- 필터 초기화
- 로그인 다시 하기
- 결제 수단 변경
- 파일 다시 선택
- 네트워크 확인
- 고객센터 문의
- 이전 화면으로 이동

---

### [실무]

Retry Button:

```jsx
<section role="alert">
  <h2>목록을 불러오지 못했습니다.</h2>
  <p>네트워크 연결을 확인한 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Filter Recovery:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onResetFilter}>
    필터 초기화
  </button>
</section>
```

Auth Recovery:

```jsx
<section role="alert">
  <h2>로그인이 필요합니다.</h2>
  <p>이 기능을 사용하려면 로그인해 주세요.</p>
  <Link to="/login">로그인하러 가기</Link>
</section>
```

실무 기준:

- retry는 button
- 페이지 이동은 Link
- action 목적을 명확히 작성
- 오류 원인과 recovery action이 연결되어야 함
- retry 중 loading state 제공
- retry 실패 시 같은 오류만 반복하지 않게 문구 검토
- recovery action도 keyboard 접근 가능해야 함

---

### [FAQ]

Q. Error State에 retry button이 꼭 필요해?
A. 재시도 가능한 오류라면 제공하는 것이 좋다.

Q. retry는 Button이야 Link야?
A. 현재 화면에서 다시 요청하는 액션이면 button이 적합하다.

Q. 로그인하러 가기는 Button이야 Link야?
A. 로그인 페이지로 이동한다면 Link가 적합하다.

Q. 오류 해결 방법을 꼭 알려줘야 해?
A. 사용자가 무엇을 해야 할지 알 수 있도록 가능한 recovery action을 제공하는 것이 좋다.

---

# 5. Empty State Accessibility

## 5.1 Empty State Basics

### [개념]

Empty State는 요청은 정상적으로 완료되었지만 표시할 데이터가 없는 상태다.

Empty State는 Error State와 다르다.

사용자는 데이터가 없는 것인지, 로딩 중인지, 오류가 발생한 것인지 구분할 수 있어야 한다.

---

### [핵심]

Empty State 사용 대상:

- 검색 결과 없음
- 필터 결과 없음
- 찜 목록 없음
- 리뷰 없음
- 알림 없음
- 결제 내역 없음
- 업로드 파일 없음
- 댓글 없음
- 장바구니 없음
- 방문 기록 없음

Empty State 구성:

- 제목
- 설명
- 다음 행동
- 필터 초기화
- 검색어 변경
- 생성 버튼
- 추천 link
- 오류와 구분

---

### [실무]

검색 결과 없음:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onResetFilter}>
    필터 초기화
  </button>
</section>
```

리뷰 없음:

```jsx
<section>
  <h2>아직 등록된 리뷰가 없습니다.</h2>
  <p>첫 번째 리뷰를 작성해 보세요.</p>
  <button type="button" onClick={onOpenReviewForm}>
    리뷰 작성하기
  </button>
</section>
```

찜 목록 없음:

```jsx
<section>
  <h2>찜한 축제가 없습니다.</h2>
  <p>관심 있는 축제를 찾아 찜해 보세요.</p>
  <Link to="/festivals">축제 둘러보기</Link>
</section>
```

실무 기준:

- 빈 배열만 렌더링하지 않음
- “데이터 없음”만 표시하지 않음
- 사용자에게 다음 행동 제공
- Error State와 문구를 구분
- 검색 / 필터 결과 없음은 조건 변경 action 제공
- 생성 가능한 목록은 생성 action 제공
- Empty State에도 heading 구조 제공

---

### [FAQ]

Q. Empty State는 왜 필요해?
A. 사용자가 데이터가 없는 정상 상태인지 오류인지 이해하고 다음 행동을 결정해야 하기 때문이다.

Q. 데이터가 없으면 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. Empty State 메시지와 다음 행동을 제공해야 한다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 정상 응답이지만 데이터가 없는 상태이고 Error State는 요청이나 작업이 실패한 상태다.

Q. Empty State에는 버튼이 필요해?
A. 상황에 따라 필터 초기화, 작성하기, 둘러보기 같은 다음 행동을 제공하는 것이 좋다.

---

## 5.2 Search Empty State

### [개념]

Search Empty State는 검색 요청이 정상적으로 처리되었지만 결과가 없는 상태다.

검색 결과 없음은 오류가 아니므로 사용자가 검색어를 수정하거나 필터를 초기화할 수 있게 안내해야 한다.

---

### [핵심]

Search Empty State 구성:

- 검색 결과 없음 제목
- 검색어 / 필터 조건 언급
- 검색어 변경 안내
- 필터 초기화 버튼
- 추천 검색어
- 전체 목록 보기 link
- result count status

---

### [실무]

검색 결과 없음:

```jsx
<section aria-labelledby="empty-search-title">
  <h2 id="empty-search-title">검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 적용한 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onResetFilter}>
    필터 초기화
  </button>
</section>
```

검색 결과 수:

```jsx
<p role="status">검색 결과 0건</p>
```

전체 목록 이동:

```jsx
<Link to="/festivals">전체 축제 목록 보기</Link>
```

실무 기준:

- 검색 결과 0건을 명확히 표시
- loading / error와 구분되는 문구 사용
- 필터 초기화는 button
- 전체 목록 이동은 Link
- 검색어가 길거나 오타 가능성이 있으면 수정 안내
- result count는 `role="status"` 고려
- focus 이동은 상황에 따라 검토

---

### [FAQ]

Q. 검색 결과 없음은 Error야?
A. 아니다. 요청이 정상 처리되었고 결과가 없는 Empty State다.

Q. 검색 결과 없음에는 무엇을 보여줘야 해?
A. 결과가 없다는 메시지와 검색어 변경, 필터 초기화 같은 다음 행동을 제공한다.

Q. 필터 초기화는 Button이야 Link야?
A. 현재 조건을 변경하는 액션이므로 button이 적합하다.

Q. 검색 결과 0건을 스크린 리더에 알려야 해?
A. 동적으로 바뀌는 결과라면 role status를 고려할 수 있다.

---

## 5.3 List Empty State

### [개념]

List Empty State는 목록 데이터가 없는 상태다.

리뷰, 댓글, 알림, 결제 내역, 찜 목록, 방문 기록 등 사용자가 목록을 기대하는 화면에서는 빈 상태를 명확히 설명해야 한다.

---

### [핵심]

List Empty State 대상:

- Review List
- Comment List
- Notification List
- Favorite List
- Payment History
- Visit History
- Upload List
- Cart List
- Admin Search Result
- Chat Message List

구성:

- 목록 없음 제목
- 이유 설명
- 다음 action
- 생성 action
- 탐색 link
- filter reset

---

### [실무]

리뷰 목록 없음:

```jsx
<section>
  <h2>아직 리뷰가 없습니다.</h2>
  <p>방문 경험을 공유해 보세요.</p>
  <button type="button" onClick={onOpenReviewForm}>
    리뷰 작성하기
  </button>
</section>
```

알림 없음:

```jsx
<section>
  <h2>새 알림이 없습니다.</h2>
  <p>축제 시작 알림이나 댓글 알림이 생기면 이곳에 표시됩니다.</p>
</section>
```

결제 내역 없음:

```jsx
<section>
  <h2>결제 내역이 없습니다.</h2>
  <p>후원 결제를 완료하면 내역이 표시됩니다.</p>
</section>
```

실무 기준:

- 목록이 비어 있는 이유를 문맥에 맞게 설명
- 사용자가 할 수 있는 다음 행동 제공
- 작성 action은 button 또는 Link 역할 구분
- 단순히 빈 `ul`만 렌더링하지 않음
- heading을 제공해 section 의미를 명확히 함
- 필터 때문에 비어 있는지 실제 데이터가 없는지 구분

---

### [FAQ]

Q. 빈 목록은 ul만 비워두면 돼?
A. 권장하지 않는다. 사용자가 상태를 이해할 수 있도록 Empty State를 제공해야 한다.

Q. 리뷰가 없으면 어떤 메시지가 좋아?
A. “아직 리뷰가 없습니다. 첫 번째 리뷰를 작성해 보세요.”처럼 다음 행동을 제공한다.

Q. 알림이 없으면 버튼이 꼭 필요해?
A. 꼭 필요하지는 않다. 사용자가 이해할 수 있는 설명만으로 충분한 경우도 있다.

Q. 필터 결과 없음과 전체 목록 없음은 다르게 써야 해?
A. 그렇다. 필터 결과 없음은 필터 초기화 안내가 필요하고 전체 목록 없음은 데이터 생성 또는 탐색 안내가 적합하다.

---

# 6. Offline and Network State

## 6.1 Network Error State

### [개념]

Network Error State는 서버 요청 실패, 연결 불안정, timeout, offline 상태처럼 네트워크 문제로 데이터를 가져오거나 저장하지 못한 상태다.

Network Error는 사용자가 직접 해결할 수 있는 행동과 재시도 수단을 제공해야 한다.

---

### [핵심]

Network Error 유형:

- offline
- timeout
- server unreachable
- request failed
- fetch failed
- upload failed
- retry exceeded
- stale data
- slow network

구성:

- 사용자용 오류 제목
- 네트워크 확인 안내
- 다시 시도 버튼
- offline 상태 표시
- 마지막 업데이트 시각 선택
- 저장되지 않은 변경 경고
- pending action 재시도

---

### [실무]

네트워크 오류:

```jsx
<section role="alert">
  <h2>네트워크 연결을 확인해 주세요.</h2>
  <p>인터넷 연결이 불안정해 데이터를 불러오지 못했습니다.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

업로드 실패:

```jsx
<div role="alert">
  이미지 업로드에 실패했습니다. 네트워크 연결을 확인한 후 다시 시도해 주세요.
</div>
```

오래된 데이터 안내:

```jsx
<p role="status">
  현재 오프라인 상태입니다. 마지막으로 저장된 정보를 표시합니다.
</p>
```

실무 기준:

- 네트워크 오류는 사용자용 문구로 표시
- retry action 제공
- retry는 button 사용
- offline 상태와 server error를 가능한 구분
- 저장 실패 시 사용자의 입력값을 보존
- 업로드 실패 시 파일 재선택 여부 안내
- 오류 상태는 color only로 전달하지 않음

---

### [FAQ]

Q. Network Error에는 무엇을 보여줘야 해?
A. 연결 문제 설명, 다시 시도 버튼, 필요한 경우 입력값 보존 안내를 제공한다.

Q. 네트워크 오류 retry는 Button이야 Link야?
A. 현재 요청을 다시 실행하는 액션이므로 button이 적합하다.

Q. 서버 오류와 네트워크 오류는 다르게 보여줘야 해?
A. 가능하면 다르게 안내하는 것이 좋다. 사용자가 해결할 수 있는 행동이 다를 수 있다.

Q. 저장 실패 시 입력값을 지워도 돼?
A. 권장하지 않는다. 사용자가 다시 입력하지 않도록 가능한 입력값을 보존해야 한다.

---

## 6.2 Offline State

### [개념]

Offline State는 사용자의 네트워크 연결이 끊겼거나 서버에 접근할 수 없는 상태를 UI에 알려주는 방식이다.

오프라인 상태에서는 사용 가능한 기능과 제한되는 기능을 명확히 안내해야 한다.

---

### [핵심]

Offline State 구성:

- offline notice
- limited functionality 안내
- retry / reconnect action
- cached data 표시
- unsaved changes warning
- disabled action reason
- status message
- focus 방해 최소화

---

### [실무]

Offline Notice:

```jsx
<div role="status">오프라인 상태입니다. 일부 기능이 제한될 수 있습니다.</div>
```

저장 제한 안내:

```jsx
<section role="alert">
  <h2>현재 저장할 수 없습니다.</h2>
  <p>네트워크 연결 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Cached Data:

```jsx
<p role="status">마지막으로 불러온 데이터를 표시하고 있습니다.</p>
```

실무 기준:

- 오프라인 상태를 명확히 안내
- 사용 가능한 기능과 제한 기능 구분
- 사용자의 입력 내용 보존 고려
- 자동 재연결 시 status message 제공 가능
- 오프라인 알림이 사용자의 현재 focus를 불필요하게 빼앗지 않게 함
- retry 또는 refresh action 제공

---

### [FAQ]

Q. Offline State는 꼭 보여줘야 해?
A. 네트워크 의존 기능이 제한된다면 사용자가 상태를 알 수 있게 보여주는 것이 좋다.

Q. 오프라인 알림에는 role alert를 써야 해?
A. 즉시 중요한 제한이면 alert를 고려할 수 있지만 일반 상태 알림이면 role status가 적합할 수 있다.

Q. 오프라인 상태에서 입력값은 어떻게 해?
A. 가능하면 보존하고, 저장 제한이나 재시도 방법을 안내해야 한다.

Q. cached data를 보여주면 어떻게 알려줘?
A. “마지막으로 불러온 데이터를 표시하고 있습니다”처럼 현재 데이터 상태를 설명한다.

---

# 7. Permission and Auth State

## 7.1 Permission Denied State

### [개념]

Permission Denied State는 사용자가 특정 기능이나 페이지에 접근할 권한이 없을 때 보여주는 상태다.

권한 오류는 사용자가 왜 막혔는지, 무엇을 해야 하는지 이해할 수 있어야 한다.

---

### [핵심]

Permission State 유형:

- login required
- role required
- owner only
- admin only
- expired session
- blocked action
- private resource
- deleted resource
- forbidden request

구성:

- 권한 상태 제목
- 이유 설명
- 로그인 이동
- 이전 화면 이동
- 권한 요청 안내
- 민감정보 노출 방지
- 내부 정책 노출 최소화

---

### [실무]

로그인 필요:

```jsx
<section role="alert">
  <h2>로그인이 필요합니다.</h2>
  <p>이 기능을 사용하려면 로그인해 주세요.</p>
  <Link to="/login">로그인하러 가기</Link>
</section>
```

권한 없음:

```jsx
<section role="alert">
  <h2>접근 권한이 없습니다.</h2>
  <p>이 페이지를 볼 수 있는 권한이 없습니다.</p>
  <Link to="/">홈으로 이동</Link>
</section>
```

세션 만료:

```jsx
<section role="alert">
  <h2>로그인이 만료되었습니다.</h2>
  <p>계속하려면 다시 로그인해 주세요.</p>
  <Link to="/login">다시 로그인하기</Link>
</section>
```

실무 기준:

- 권한 상태는 명확한 제목과 설명 제공
- 로그인 이동은 Link 사용
- 내부 권한 정책이나 리소스 존재 여부를 과도하게 노출하지 않음
- 세션 만료 시 사용자의 작업 중 데이터 보존 고려
- 권한 없는 action은 disabled reason 제공 검토
- alert 사용은 중요도에 따라 결정

---

### [FAQ]

Q. 권한 없음 상태에는 무엇을 보여줘야 해?
A. 접근할 수 없다는 설명과 로그인, 홈 이동, 이전 화면 이동 같은 다음 행동을 제공한다.

Q. 로그인하러 가기는 Button이야 Link야?
A. 로그인 페이지로 이동하는 것이므로 Link가 적합하다.

Q. 권한 오류에 내부 정책을 자세히 보여줘도 돼?
A. 권장하지 않는다. 필요한 안내만 사용자용 문구로 제공한다.

Q. 세션 만료 시 입력값은 어떻게 해?
A. 가능하면 사용자의 작업 내용을 보존하거나 손실 가능성을 안내해야 한다.

---

## 7.2 Disabled Action Reason

### [개념]

Disabled Action Reason은 사용자가 특정 버튼이나 기능을 사용할 수 없는 이유를 설명하는 기준이다.

비활성화된 버튼만 보여주면 사용자는 무엇을 해야 활성화되는지 알기 어렵다.

---

### [핵심]

Disabled Reason 대상:

- submit button
- payment button
- upload button
- next step button
- delete button
- admin action
- reservation button
- send message button

이유 예:

- 필수 항목 미입력
- 약관 미동의
- 권한 없음
- 네트워크 연결 없음
- 업로드 중
- 결제 처리 중
- 이미 완료됨
- 기간 종료

---

### [실무]

필수값 미입력:

```jsx
<button type="submit" disabled={!canSubmit}>
  제출
</button>
<p id="submit-help">
  필수 항목을 모두 입력하면 제출할 수 있습니다.
</p>
```

권한 없음:

```jsx
<button type="button" disabled>
  삭제
</button>
<p>작성자만 삭제할 수 있습니다.</p>
```

업로드 중:

```jsx
<button type="button" disabled={uploading} aria-busy={uploading}>
  {uploading ? "업로드 중..." : "업로드"}
</button>
```

실무 기준:

- disabled 이유가 명확하지 않으면 설명 제공
- 설명은 button 근처에 배치
- native disabled button은 focus되지 않을 수 있음
- tooltip에만 이유를 제공하면 keyboard / touch 사용자가 놓칠 수 있음
- 상황에 따라 disabled 대신 클릭 후 오류 안내가 더 적합할 수 있음
- `aria-disabled` 사용 시 동작 차단 직접 구현 필요

---

### [FAQ]

Q. disabled button에 이유를 꼭 써야 해?
A. 사용자가 왜 사용할 수 없는지 알기 어렵다면 이유를 제공하는 것이 좋다.

Q. disabled 이유를 tooltip에만 넣어도 돼?
A. 권장하지 않는다. keyboard나 touch 사용자가 접근하기 어려울 수 있다.

Q. disabled 대신 누르면 오류를 보여주는 방식도 가능해?
A. 가능하다. 사용자가 이유를 이해해야 하는 중요한 action에서는 더 나은 UX가 될 수 있다.

Q. aria-disabled는 disabled와 같아?
A. 아니다. aria-disabled는 상태만 전달하고 실제 클릭 차단은 직접 처리해야 한다.

---

# 8. Upload and Progress State

## 8.1 Upload State Accessibility

### [개념]

Upload State는 파일 선택, 업로드 진행, 성공, 실패, 취소 상태를 사용자에게 전달하는 기준이다.

파일 업로드는 진행 시간이 길 수 있고 실패 가능성이 있으므로 상태 메시지와 복구 action이 중요하다.

---

### [핵심]

Upload State 구성:

- file selected state
- upload progress
- uploading message
- upload success
- upload error
- retry upload
- cancel upload
- file type error
- file size error
- selected file name
- progress text
- `role="status"`
- `role="alert"`

---

### [실무]

파일 선택 안내:

```jsx
<label htmlFor="review-image">리뷰 이미지</label>
<input
  id="review-image"
  name="reviewImage"
  type="file"
  accept="image/png,image/jpeg"
  aria-describedby="review-image-help"
/>
<p id="review-image-help">
  PNG 또는 JPG 파일을 업로드할 수 있습니다. 최대 5MB까지 가능합니다.
</p>
```

업로드 중:

```jsx
<div role="status">이미지 업로드 중입니다.</div>
```

업로드 실패:

```jsx
<div role="alert">
  이미지 업로드에 실패했습니다. 파일 크기와 네트워크 연결을 확인해 주세요.
</div>
<button type="button" onClick={onRetryUpload}>
  다시 업로드
</button>
```

실무 기준:

- 선택된 파일명을 표시
- 업로드 조건은 helper text로 제공
- 업로드 중 상태 제공
- 진행률이 있으면 텍스트로도 제공
- 실패 원인을 구체적으로 안내
- retry / cancel action 제공 검토
- drag and drop만 제공하지 않음
- 업로드 실패 후 파일 재선택 필요 여부 안내

---

### [FAQ]

Q. Upload State에는 무엇이 필요해?
A. 선택된 파일, 업로드 중, 성공, 실패, 재시도 가능 여부를 사용자가 알 수 있어야 한다.

Q. 업로드 진행률은 시각 bar만 있으면 돼?
A. 가능하면 텍스트로도 진행 상태를 제공하는 것이 좋다.

Q. 업로드 실패 문구는 어떻게 써?
A. 파일 형식, 크기, 네트워크 등 사용자가 확인할 수 있는 원인을 안내한다.

Q. drag and drop만 제공해도 돼?
A. 권장하지 않는다. keyboard 사용자를 위한 파일 선택 버튼이 필요하다.

---

## 8.2 Progress Indicator

### [개념]

Progress Indicator는 작업 진행 정도를 사용자에게 알려주는 UI다.

업로드, 다운로드, 단계 진행, 긴 처리 작업에서는 진행 상태를 텍스트와 함께 제공해야 한다.

---

### [핵심]

Progress 유형:

- determinate progress
- indeterminate progress
- upload progress
- step progress
- processing progress
- background sync progress

구성:

- progress bar
- progress text
- current value
- max value
- `role="progressbar"` 고려
- `aria-valuenow`
- `aria-valuemin`
- `aria-valuemax`
- status message

---

### [실무]

Progress Bar:

```jsx
<div
  role="progressbar"
  aria-valuemin={0}
  aria-valuemax={100}
  aria-valuenow={progress}
  aria-label="이미지 업로드 진행률"
>
  {progress}%
</div>
```

Step Progress:

```jsx
<ol aria-label="회원가입 단계">
  <li aria-current="step">이메일 인증</li>
  <li>프로필 입력</li>
  <li>가입 완료</li>
</ol>
```

Indeterminate:

```jsx
<div role="status">처리 중입니다. 잠시만 기다려 주세요.</div>
```

실무 기준:

- 진행률을 알 수 있으면 value 제공
- 진행률을 알 수 없으면 status text 제공
- progress text는 시각적으로도 제공
- 너무 잦은 progress live update 주의
- stepper는 현재 단계에 `aria-current="step"` 고려
- 작업 완료 또는 실패 상태를 명확히 제공

---

### [FAQ]

Q. progress bar에는 ARIA가 필요해?
A. 진행률을 전달해야 한다면 role progressbar와 aria-valuenow 등을 고려할 수 있다.

Q. 진행률을 모르면 어떻게 해?
A. “처리 중입니다” 같은 status message로 indeterminate 상태를 전달한다.

Q. 단계 진행 UI는 어떻게 접근성 있게 만들어?
A. 현재 단계에 aria-current="step"을 사용하고 단계 이름을 명확히 제공한다.

Q. progress 숫자를 너무 자주 업데이트해도 돼?
A. 너무 잦은 live update는 방해가 될 수 있으므로 적절히 제한하는 것이 좋다.

---

# 9. State Feedback Testing

## 9.1 Testing Library State Query

### [개념]

Testing Library State Query는 Loading, Success, Error, Empty 같은 상태가 사용자에게 인식 가능한 방식으로 렌더링되는지 검증하는 방식이다.

상태 UI는 text, role, accessible name 기준으로 테스트할 수 있어야 한다.

---

### [핵심]

검증 Query:

- `getByRole("status")`
- `getByRole("alert")`
- `getByText`
- `getByRole("button", { name })`
- `getByRole("link", { name })`
- `queryByText`
- `findByText`
- `findByRole`

검증 대상:

- loading message
- success message
- error message
- retry button
- empty state heading
- disabled button
- pending button text
- upload status
- progress indicator

---

### [실무]

Loading Test:

```tsx
expect(screen.getByRole("status")).toHaveTextContent(
  "데이터를 불러오는 중입니다.",
);
```

Error Test:

```tsx
expect(screen.getByRole("alert")).toHaveTextContent("저장에 실패했습니다.");
expect(screen.getByRole("button", { name: "다시 시도" })).toBeInTheDocument();
```

Empty Test:

```tsx
expect(
  screen.getByRole("heading", { name: "검색 결과가 없습니다." }),
).toBeInTheDocument();
expect(screen.getByRole("button", { name: "필터 초기화" })).toBeInTheDocument();
```

Button Pending Test:

```tsx
expect(screen.getByRole("button", { name: "저장 중..." })).toBeDisabled();
```

실무 기준:

- 상태 메시지는 role 또는 text로 찾을 수 있어야 함
- retry action은 role/name으로 검증
- empty state는 heading으로 검증 가능
- pending button은 text 변경과 disabled 상태 검증
- testId보다 사용자 인식 가능한 query 우선
- 비동기 상태는 `findByRole`, `findByText` 활용

---

### [FAQ]

Q. Loading 상태는 어떻게 테스트해?
A. role status나 loading text로 사용자가 인식 가능한 상태를 검증한다.

Q. Error 상태는 어떻게 테스트해?
A. role alert와 error message, retry button을 함께 확인한다.

Q. Empty State는 어떻게 테스트해?
A. heading, 설명 문구, 다음 action button 또는 link를 확인한다.

Q. pending button은 어떻게 테스트해?
A. 버튼 text가 “저장 중...”처럼 바뀌고 disabled 또는 aria-busy 상태인지 확인한다.

---

## 9.2 Manual State Feedback Check

### [개념]

Manual State Feedback Check는 실제 사용 흐름에서 Loading, Success, Error, Empty, Disabled 상태가 이해 가능한지 직접 확인하는 절차다.

자동화 테스트는 상태 존재 여부를 검증할 수 있지만 문구 품질과 focus 흐름은 수동 검토가 필요하다.

---

### [핵심]

수동 점검 항목:

- loading text 확인
- spinner only 여부 확인
- success message 확인
- error message 구체성 확인
- retry action keyboard 접근 확인
- empty state next action 확인
- disabled reason 확인
- focus lost 확인
- role alert 남발 여부 확인
- color only state 여부 확인
- network failure UX 확인

---

### [실무]

Manual Check Flow:

```text
요청 시작
→ Loading 상태 확인
→ 성공 상태 확인
→ 실패 상태 확인
→ Retry 조작 확인
→ Empty State 확인
→ Disabled Reason 확인
→ Keyboard-only 조작 확인
→ Focus 흐름 확인
```

우선 점검 화면:

- Login
- Signup
- Search
- Festival List
- Festival Detail
- Review Submit
- Payment
- File Upload
- Notification List
- Favorite List
- Admin Table
- Modal Form

실무 기준:

- 마우스 없이 상태 변화 후 다음 행동 가능해야 함
- 오류 발생 후 사용자가 무엇을 해야 할지 알 수 있어야 함
- loading과 empty와 error가 문구상 구분되어야 함
- 상태 메시지가 너무 빨리 사라지지 않아야 함
- focus가 사라지거나 숨겨진 요소로 가지 않아야 함
- disabled 상태가 사용자를 막기만 하지 않아야 함

---

### [FAQ]

Q. State Feedback은 자동화 테스트만으로 충분해?
A. 아니다. 문구 품질, focus 흐름, 사용자가 다음 행동을 이해하는지는 수동 검토가 필요하다.

Q. State Feedback 수동 점검은 어디부터 해?
A. 로그인, 검색, 저장, 업로드, 결제처럼 상태 변화가 많은 핵심 흐름부터 확인한다.

Q. Error와 Empty를 왜 구분해서 봐야 해?
A. 사용자가 오류인지 데이터 없음인지에 따라 다음 행동이 달라지기 때문이다.

Q. retry action도 keyboard로 확인해야 해?
A. 그렇다. retry button도 keyboard로 focus하고 실행할 수 있어야 한다.

---

# 10. State Feedback Review

## 10.1 Review Checklist

### [개념]

State Feedback Review는 Loading, Success, Error, Empty, Disabled, Offline, Upload 상태가 접근성 기준을 만족하는지 검토하는 과정이다.

Review Agent는 상태 UI가 화면에 보이는지뿐 아니라 보조기술 전달, keyboard 조작, 다음 행동 제공 여부를 함께 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Loading 상태에 텍스트 메시지가 있는가?
- [ ] spinner only 상태가 아닌가?
- [ ] skeleton이 장식 처리되고 별도 loading text가 있는가?
- [ ] loading 영역에 aria-busy가 필요한지 검토했는가?
- [ ] button pending 상태에서 text가 변경되는가?
- [ ] pending 중 중복 제출이 방지되는가?
- [ ] Success 상태에 완료 메시지가 있는가?
- [ ] Success 상태가 색상 / 아이콘만으로 전달되지 않는가?
- [ ] Error 상태에 사용자용 오류 문구가 있는가?
- [ ] Error 상태가 내부 서버 메시지를 노출하지 않는가?
- [ ] Error 상태에 retry / recovery action이 있는가?
- [ ] Field Error와 Global Error를 구분했는가?
- [ ] Empty State가 Error State와 구분되는가?
- [ ] Empty State에 다음 행동이 있는가?
- [ ] Search Empty State에 필터 초기화 또는 검색어 변경 안내가 있는가?
- [ ] Disabled 상태에 이유가 필요한지 검토했는가?
- [ ] Offline / Network Error 상태에 재시도 안내가 있는가?
- [ ] Upload 상태에 선택 / 진행 / 성공 / 실패 메시지가 있는가?
- [ ] Progress 상태가 텍스트로도 전달되는가?
- [ ] State action이 keyboard로 조작 가능한가?
- [ ] role status / role alert를 적절히 사용했는가?
- [ ] role alert를 남발하지 않았는가?
- [ ] Testing Library로 상태 메시지를 찾을 수 있는가?
```

---

### [실무]

Review Flow:

```text
State UI 확인
→ Loading / Success / Error / Empty 구분
→ Text Message 확인
→ ARIA role 확인
→ Action 제공 여부 확인
→ Keyboard 조작 확인
→ Focus 흐름 확인
→ Color Only 여부 확인
→ Testing Query 확인
```

대표 수정 패턴:

```text
문제: spinner만 표시
해결: role status + loading text 제공
```

```text
문제: 빈 목록에 아무것도 표시하지 않음
해결: Empty State heading + 설명 + 다음 action 제공
```

```text
문제: 서버 에러 원문 노출
해결: 사용자용 오류 메시지로 변환
```

```text
문제: disabled button 이유 없음
해결: helper text 또는 클릭 후 안내 제공 검토
```

---

### [FAQ]

Q. State Feedback Review에서 가장 먼저 볼 것은?
A. Loading, Error, Empty, Success 상태가 서로 구분되고 텍스트로 전달되는지 먼저 본다.

Q. Review Agent는 상태 문구도 검토해야 해?
A. 그렇다. 상태 문구는 사용자가 다음 행동을 이해할 수 있어야 한다.

Q. role status와 role alert는 어떻게 구분해?
A. status는 긴급하지 않은 상태 알림이고 alert는 즉시 알려야 하는 오류나 중요한 메시지에 사용한다.

Q. 상태 UI에도 keyboard 검토가 필요해?
A. 필요하다. retry, reset, undo, login 이동 같은 action은 keyboard로 조작 가능해야 한다.

---

# 11. Common State Feedback Mistakes

## 11.1 State Feedback Anti Patterns

### [개념]

State Feedback Anti Pattern은 화면상 상태가 있는 것처럼 보이지만 사용자가 현재 상태를 이해하거나 다음 행동을 수행하기 어려운 구현 방식이다.

상태 UI는 문구, 역할, focus, action을 함께 설계해야 한다.

---

### [핵심]

자주 발생하는 실수:

- spinner만 표시
- skeleton만 표시
- loading text 없음
- loading이 끝나지 않는 상태 방치
- button pending text 없음
- pending 중 중복 제출 가능
- 성공 상태를 초록색 체크 아이콘만으로 표시
- toast가 너무 빨리 사라짐
- error message가 “오류”처럼 모호함
- 서버 stack trace 노출
- field error와 input 미연결
- global error만 있고 field error 없음
- retry button 없음
- empty state 없이 빈 화면 표시
- 검색 결과 없음과 오류를 같은 문구로 표시
- disabled button 이유 없음
- offline 상태 안내 없음
- 업로드 실패 후 복구 안내 없음
- progress bar에 텍스트 없음
- role alert 남발
- 상태 action이 keyboard로 접근 불가

---

### [실무]

Anti Pattern:

```jsx
<Spinner />
```

개선:

```jsx
<div role="status">
  <Spinner aria-hidden="true" />
  <span>데이터를 불러오는 중입니다.</span>
</div>
```

Anti Pattern:

```jsx
{
  items.length === 0 && null;
}
```

개선:

```jsx
{
  items.length === 0 && (
    <section>
      <h2>검색 결과가 없습니다.</h2>
      <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
      <button type="button" onClick={onResetFilter}>
        필터 초기화
      </button>
    </section>
  );
}
```

Anti Pattern:

```jsx
<div>Error: Cannot read properties of undefined</div>
```

개선:

```jsx
<section role="alert">
  <h2>요청을 처리하지 못했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Anti Pattern:

```jsx
<button disabled>제출</button>
```

개선:

```jsx
<button disabled>제출</button>
<p>필수 항목을 모두 입력하면 제출할 수 있습니다.</p>
```

---

### [FAQ]

Q. State Feedback 초보가 가장 많이 하는 실수는?
A. spinner만 표시하거나, empty state를 비워두거나, 오류 문구를 모호하게 작성하는 실수가 많다.

Q. Empty State 없이 빈 화면을 보여주면 왜 문제야?
A. 사용자가 로딩 중인지, 오류인지, 데이터가 없는 정상 상태인지 알 수 없기 때문이다.

Q. 서버 오류 원문을 보여주면 왜 문제야?
A. 내부 정보가 노출될 수 있고 사용자가 이해하기 어렵다.

Q. disabled button만 보여주면 왜 문제야?
A. 사용자가 왜 사용할 수 없는지 알 수 없어 다음 행동을 결정하기 어렵다.

---

# Retrieval Queries

### [FAQ]

Q. State Feedback Accessibility는 왜 필요해?
A. 사용자가 현재 화면이 로딩 중인지, 성공했는지, 실패했는지, 데이터가 없는지 이해해야 하기 때문이다.

Q. 상태 메시지는 화면에 보이면 충분해?
A. 아니다. 중요한 상태 변화는 보조기술 사용자도 인식할 수 있게 role status, role alert, aria-live 등을 고려해야 한다.

Q. Loading State에는 무엇이 필요해?
A. 사용자가 현재 작업이 진행 중임을 알 수 있는 텍스트와 시각적 표시가 필요하다.

Q. spinner만 있으면 왜 부족해?
A. 스크린 리더 사용자는 spinner 의미를 알기 어렵고, 시각 사용자도 무엇이 진행 중인지 모를 수 있다.

Q. aria-busy는 어디에 써?
A. 특정 section이나 button이 처리 중임을 전달할 때 사용할 수 있다.

Q. loading text는 어떻게 써?
A. “데이터를 불러오는 중입니다”, “저장 중입니다”처럼 현재 작업을 구체적으로 작성한다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

Q. Skeleton만 있으면 loading 표시가 충분해?
A. 아니다. 보조기술 사용자에게 loading 상태를 전달하는 텍스트가 필요하다.

Q. Skeleton shimmer는 접근성 문제가 될 수 있어?
A. 과도한 움직임은 불편을 줄 수 있으므로 prefers-reduced-motion을 고려한다.

Q. Skeleton이 실제 콘텐츠처럼 읽히면 문제야?
A. 문제다. 의미 없는 placeholder가 콘텐츠처럼 전달될 수 있다.

Q. 버튼 loading 상태는 어떻게 표시해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 중복 실행을 막기 위해 disabled와 aria-busy를 고려한다.

Q. pending 중 버튼을 disabled 해도 돼?
A. 가능하다. 다만 사용자가 현재 진행 중임을 알 수 있게 텍스트 상태를 제공해야 한다.

Q. 버튼 안 spinner만 보여주면 돼?
A. 권장하지 않는다. 버튼의 작업 상태를 설명하는 텍스트가 필요하다.

Q. pending이 끝나면 뭘 보여줘야 해?
A. 성공 메시지, 오류 메시지, 다음 화면 이동 등 결과 상태를 명확히 제공해야 한다.

Q. Success Message는 왜 필요해?
A. 사용자가 작업이 정상 완료되었는지 확신할 수 있어야 하기 때문이다.

Q. 성공 상태에 초록색 체크 아이콘만 보여주면 돼?
A. 아니다. 텍스트로 성공 상태를 함께 제공해야 한다.

Q. 성공 메시지에는 role status를 써도 돼?
A. 저장 완료 같은 긴급하지 않은 상태 알림에는 role status를 사용할 수 있다.

Q. 성공 후 바로 페이지 이동하면 메시지는 필요 없어?
A. 상황에 따라 다르다. 사용자가 결과를 인식하기 어려우면 완료 화면이나 명확한 상태 표시가 필요하다.

Q. Toast에도 접근성이 필요해?
A. 필요하다. Toast가 중요한 상태를 전달하면 보조기술 사용자도 인식해야 한다.

Q. Toast가 자동으로 사라져도 돼?
A. 가능하지만 너무 빨리 사라지면 사용자가 읽기 어렵다. 중요한 메시지는 충분한 시간이나 닫기 제어를 고려한다.

Q. Toast에 role status를 붙이면 돼?
A. 긴급하지 않은 성공 알림에는 role status를 고려할 수 있다.

Q. Toast 안 버튼은 keyboard로 접근 가능해야 해?
A. 그렇다. 실행 취소 같은 action이 있으면 keyboard로 조작 가능해야 한다.

Q. Error State에는 무엇이 필요해?
A. 오류를 설명하는 문구, 수정 방법, 재시도 가능 여부, 필요한 경우 focus 이동이 필요하다.

Q. 서버 에러를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 되지만 alert 남발은 사용자를 방해할 수 있다.

Q. 오류 문구는 어떻게 써?
A. 사용자가 무엇을 수정하거나 다시 시도해야 하는지 짧고 명확하게 작성한다.

Q. Field Error와 Global Error 차이는?
A. Field Error는 특정 input의 오류이고 Global Error는 Form 전체나 요청 실패 같은 전체 상태 오류다.

Q. 로그인 실패는 field error야 global error야?
A. 보안상 어떤 필드가 틀렸는지 구체화하지 않고 global error로 처리하는 경우가 많다.

Q. Global Error만 보여주면 충분해?
A. field 수정이 필요한 오류라면 field error도 함께 제공하는 것이 좋다.

Q. 서버 저장 실패는 어디에 표시해?
A. 일반적으로 Form 상단이나 관련 section에 global error로 표시하고 retry action을 제공한다.

Q. Error State에 retry button이 꼭 필요해?
A. 재시도 가능한 오류라면 제공하는 것이 좋다.

Q. retry는 Button이야 Link야?
A. 현재 화면에서 다시 요청하는 액션이면 button이 적합하다.

Q. 로그인하러 가기는 Button이야 Link야?
A. 로그인 페이지로 이동한다면 Link가 적합하다.

Q. 오류 해결 방법을 꼭 알려줘야 해?
A. 사용자가 무엇을 해야 할지 알 수 있도록 가능한 recovery action을 제공하는 것이 좋다.

Q. Empty State는 왜 필요해?
A. 사용자가 데이터가 없는 정상 상태인지 오류인지 이해하고 다음 행동을 결정해야 하기 때문이다.

Q. 데이터가 없으면 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. Empty State 메시지와 다음 행동을 제공해야 한다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 정상 응답이지만 데이터가 없는 상태이고 Error State는 요청이나 작업이 실패한 상태다.

Q. Empty State에는 버튼이 필요해?
A. 상황에 따라 필터 초기화, 작성하기, 둘러보기 같은 다음 행동을 제공하는 것이 좋다.

Q. 검색 결과 없음은 Error야?
A. 아니다. 요청이 정상 처리되었고 결과가 없는 Empty State다.

Q. 검색 결과 없음에는 무엇을 보여줘야 해?
A. 결과가 없다는 메시지와 검색어 변경, 필터 초기화 같은 다음 행동을 제공한다.

Q. 필터 초기화는 Button이야 Link야?
A. 현재 조건을 변경하는 액션이므로 button이 적합하다.

Q. 검색 결과 0건을 스크린 리더에 알려야 해?
A. 동적으로 바뀌는 결과라면 role status를 고려할 수 있다.

Q. 빈 목록은 ul만 비워두면 돼?
A. 권장하지 않는다. 사용자가 상태를 이해할 수 있도록 Empty State를 제공해야 한다.

Q. 리뷰가 없으면 어떤 메시지가 좋아?
A. “아직 리뷰가 없습니다. 첫 번째 리뷰를 작성해 보세요.”처럼 다음 행동을 제공한다.

Q. 알림이 없으면 버튼이 꼭 필요해?
A. 꼭 필요하지는 않다. 사용자가 이해할 수 있는 설명만으로 충분한 경우도 있다.

Q. 필터 결과 없음과 전체 목록 없음은 다르게 써야 해?
A. 그렇다. 필터 결과 없음은 필터 초기화 안내가 필요하고 전체 목록 없음은 데이터 생성 또는 탐색 안내가 적합하다.

Q. Network Error에는 무엇을 보여줘야 해?
A. 연결 문제 설명, 다시 시도 버튼, 필요한 경우 입력값 보존 안내를 제공한다.

Q. 네트워크 오류 retry는 Button이야 Link야?
A. 현재 요청을 다시 실행하는 액션이므로 button이 적합하다.

Q. 서버 오류와 네트워크 오류는 다르게 보여줘야 해?
A. 가능하면 다르게 안내하는 것이 좋다. 사용자가 해결할 수 있는 행동이 다를 수 있다.

Q. 저장 실패 시 입력값을 지워도 돼?
A. 권장하지 않는다. 사용자가 다시 입력하지 않도록 가능한 입력값을 보존해야 한다.

Q. Offline State는 꼭 보여줘야 해?
A. 네트워크 의존 기능이 제한된다면 사용자가 상태를 알 수 있게 보여주는 것이 좋다.

Q. 오프라인 알림에는 role alert를 써야 해?
A. 즉시 중요한 제한이면 alert를 고려할 수 있지만 일반 상태 알림이면 role status가 적합할 수 있다.

Q. 오프라인 상태에서 입력값은 어떻게 해?
A. 가능하면 보존하고, 저장 제한이나 재시도 방법을 안내해야 한다.

Q. cached data를 보여주면 어떻게 알려줘?
A. “마지막으로 불러온 데이터를 표시하고 있습니다”처럼 현재 데이터 상태를 설명한다.

Q. 권한 없음 상태에는 무엇을 보여줘야 해?
A. 접근할 수 없다는 설명과 로그인, 홈 이동, 이전 화면 이동 같은 다음 행동을 제공한다.

Q. 로그인하러 가기는 Button이야 Link야?
A. 로그인 페이지로 이동하는 것이므로 Link가 적합하다.

Q. 권한 오류에 내부 정책을 자세히 보여줘도 돼?
A. 권장하지 않는다. 필요한 안내만 사용자용 문구로 제공한다.

Q. 세션 만료 시 입력값은 어떻게 해?
A. 가능하면 사용자의 작업 내용을 보존하거나 손실 가능성을 안내해야 한다.

Q. disabled button에 이유를 꼭 써야 해?
A. 사용자가 왜 사용할 수 없는지 알기 어렵다면 이유를 제공하는 것이 좋다.

Q. disabled 이유를 tooltip에만 넣어도 돼?
A. 권장하지 않는다. keyboard나 touch 사용자가 접근하기 어려울 수 있다.

Q. disabled 대신 누르면 오류를 보여주는 방식도 가능해?
A. 가능하다. 사용자가 이유를 이해해야 하는 중요한 action에서는 더 나은 UX가 될 수 있다.

Q. aria-disabled는 disabled와 같아?
A. 아니다. aria-disabled는 상태만 전달하고 실제 클릭 차단은 직접 처리해야 한다.

Q. Upload State에는 무엇이 필요해?
A. 선택된 파일, 업로드 중, 성공, 실패, 재시도 가능 여부를 사용자가 알 수 있어야 한다.

Q. 업로드 진행률은 시각 bar만 있으면 돼?
A. 가능하면 텍스트로도 진행 상태를 제공하는 것이 좋다.

Q. 업로드 실패 문구는 어떻게 써?
A. 파일 형식, 크기, 네트워크 등 사용자가 확인할 수 있는 원인을 안내한다.

Q. drag and drop만 제공해도 돼?
A. 권장하지 않는다. keyboard 사용자를 위한 파일 선택 버튼이 필요하다.

Q. progress bar에는 ARIA가 필요해?
A. 진행률을 전달해야 한다면 role progressbar와 aria-valuenow 등을 고려할 수 있다.

Q. 진행률을 모르면 어떻게 해?
A. “처리 중입니다” 같은 status message로 indeterminate 상태를 전달한다.

Q. 단계 진행 UI는 어떻게 접근성 있게 만들어?
A. 현재 단계에 aria-current="step"을 사용하고 단계 이름을 명확히 제공한다.

Q. progress 숫자를 너무 자주 업데이트해도 돼?
A. 너무 잦은 live update는 방해가 될 수 있으므로 적절히 제한하는 것이 좋다.

Q. Loading 상태는 어떻게 테스트해?
A. role status나 loading text로 사용자가 인식 가능한 상태를 검증한다.

Q. Error 상태는 어떻게 테스트해?
A. role alert와 error message, retry button을 함께 확인한다.

Q. Empty State는 어떻게 테스트해?
A. heading, 설명 문구, 다음 action button 또는 link를 확인한다.

Q. pending button은 어떻게 테스트해?
A. 버튼 text가 “저장 중...”처럼 바뀌고 disabled 또는 aria-busy 상태인지 확인한다.

Q. State Feedback은 자동화 테스트만으로 충분해?
A. 아니다. 문구 품질, focus 흐름, 사용자가 다음 행동을 이해하는지는 수동 검토가 필요하다.

Q. State Feedback 수동 점검은 어디부터 해?
A. 로그인, 검색, 저장, 업로드, 결제처럼 상태 변화가 많은 핵심 흐름부터 확인한다.

Q. Error와 Empty를 왜 구분해서 봐야 해?
A. 사용자가 오류인지 데이터 없음인지에 따라 다음 행동이 달라지기 때문이다.

Q. retry action도 keyboard로 확인해야 해?
A. 그렇다. retry button도 keyboard로 focus하고 실행할 수 있어야 한다.

Q. State Feedback Review에서 가장 먼저 볼 것은?
A. Loading, Error, Empty, Success 상태가 서로 구분되고 텍스트로 전달되는지 먼저 본다.

Q. Review Agent는 상태 문구도 검토해야 해?
A. 그렇다. 상태 문구는 사용자가 다음 행동을 이해할 수 있어야 한다.

Q. role status와 role alert는 어떻게 구분해?
A. status는 긴급하지 않은 상태 알림이고 alert는 즉시 알려야 하는 오류나 중요한 메시지에 사용한다.

Q. 상태 UI에도 keyboard 검토가 필요해?
A. 필요하다. retry, reset, undo, login 이동 같은 action은 keyboard로 조작 가능해야 한다.

Q. State Feedback 초보가 가장 많이 하는 실수는?
A. spinner만 표시하거나, empty state를 비워두거나, 오류 문구를 모호하게 작성하는 실수가 많다.

Q. Empty State 없이 빈 화면을 보여주면 왜 문제야?
A. 사용자가 로딩 중인지, 오류인지, 데이터가 없는 정상 상태인지 알 수 없기 때문이다.

Q. 서버 오류 원문을 보여주면 왜 문제야?
A. 내부 정보가 노출될 수 있고 사용자가 이해하기 어렵다.

Q. disabled button만 보여주면 왜 문제야?
A. 사용자가 왜 사용할 수 없는지 알 수 없어 다음 행동을 결정하기 어렵다.

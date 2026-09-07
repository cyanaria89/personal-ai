# Frontend Testing Part05 - Unit Test

---

# 1. Unit Test Overview

## 1.1 Unit Test Definition

### [개념]

Unit Test는 입력과 출력이 명확한 작은 단위의 로직을 독립적으로 검증하는 테스트다.

Frontend Unit Test는 React Component 렌더링보다 순수 함수, validation, formatter, mapper, filter, sorting, utility 검증에 적합하다.

---

### [핵심]

- Unit Test
- Pure Function Test
- Validation Function Test
- Formatter Test
- Mapper Test
- Utility Test
- Filter Function Test
- Sorting Function Test
- Date Utility Test
- Error Message Mapper
- Request DTO Mapper
- Edge Case
- Boundary Value
- Fast Test
- Isolated Test

---

### [실무]

2026 실무 기준에서 Frontend Unit Test는 UI 테스트를 대체하는 용도가 아니다.

Unit Test는 아래 조건에 적합하다.

```text
입력이 명확함
→ 출력이 명확함
→ React render가 필요 없음
→ 외부 API 의존이 없음
→ 빠르게 edge case 검증 가능
```

적합한 예:

```text
이메일 형식 검증
날짜 포맷 변환
API 응답을 View Model로 변환
Form 값을 Request DTO로 변환
목록 필터링
정렬 기준 함수
에러 코드를 사용자 메시지로 변환
```

부적합한 예:

```text
버튼 클릭 후 Modal 표시
API 응답 후 Loading 제거
로그인 후 Router 이동
Form 입력 후 오류 메시지 표시
```

위 항목은 Component Test 또는 Integration Test가 더 적합하다.

---

### [FAQ]

Q. Frontend Unit Test는 뭐야?
A. validation, formatter, mapper처럼 입력과 출력이 명확한 작은 로직을 독립적으로 검증하는 테스트다.

Q. Unit Test는 React Component 테스트와 달라?
A. 다르다. Unit Test는 보통 React render 없이 순수 함수나 utility를 검증한다.

Q. Unit Test만 있으면 충분해?
A. 아니다. 사용자 UI 흐름은 Component Test와 Integration Test로 검증해야 한다.

---

## 1.2 Unit Test Role

### [개념]

Unit Test의 역할은 빠르고 안정적으로 작은 로직의 정확성을 검증하는 것이다.

Frontend에서는 복잡한 Component 내부 로직을 순수 함수로 분리하고 Unit Test로 검증할 수 있다.

---

### [핵심]

Unit Test 역할:

- 빠른 피드백
- 로직 정확성 검증
- edge case 검증
- boundary value 검증
- regression 방지
- Component 복잡도 감소
- 비즈니스 규칙 분리
- 테스트 안정성 확보

---

### [실무]

권장 구조:

```text
Component 내부 복잡 로직
→ 별도 pure function으로 분리
→ Unit Test 작성
→ Component Test에서는 사용자 결과 검증
```

예:

```text
ReviewForm
→ validateReviewForm()
→ toCreateReviewRequest()
→ formatRatingLabel()
```

Unit Test로 검증:

```text
validateReviewForm()
→ 입력 오류 검증

toCreateReviewRequest()
→ Request DTO 변환 검증

formatRatingLabel()
→ 표시 문구 변환 검증
```

Component Test로 검증:

```text
사용자가 리뷰 입력
→ 등록 클릭
→ 오류 메시지 또는 성공 메시지 표시
```

---

### [FAQ]

Q. Component 내부 로직은 어떻게 테스트해?
A. 복잡한 로직은 순수 함수로 분리해 Unit Test하고, Component에서는 사용자 결과를 테스트한다.

Q. Unit Test의 장점은 뭐야?
A. 빠르고 안정적이며 edge case를 많이 검증하기 좋다.

Q. Unit Test가 많으면 Component Test를 줄여도 돼?
A. 일부 로직 검증은 줄일 수 있지만 사용자 흐름 검증은 여전히 필요하다.

---

# 2. Pure Function Test

## 2.1 Pure Function Definition

### [개념]

Pure Function은 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Unit Test에 가장 적합한 대상이다.

---

### [핵심]

Pure Function 조건:

- same input same output
- no side effect
- no DOM dependency
- no API dependency
- no Date now 직접 의존
- no random 직접 의존
- no localStorage 직접 의존
- predictable output
- deterministic test

---

### [실무]

좋은 Pure Function 예:

```ts
export function formatPrice(value: number) {
  return `${value.toLocaleString()}원`;
}
```

테스트:

```ts
test("금액을 원화 표시 문자열로 변환한다", () => {
  expect(formatPrice(12000)).toBe("12,000원");
});
```

나쁜 Unit Test 대상:

```ts
export function getTodayLabel() {
  return new Date().toISOString();
}
```

개선:

```ts
export function formatDateLabel(date: Date) {
  return date.toISOString().slice(0, 10);
}
```

테스트:

```ts
test("날짜를 yyyy-MM-dd 문자열로 변환한다", () => {
  expect(formatDateLabel(new Date("2026-07-06T00:00:00Z"))).toBe("2026-07-06");
});
```

권장:

- 현재 시간, 랜덤, 외부 저장소는 함수 밖에서 주입
- 함수 입력과 출력을 명확히 설계
- 테스트 데이터는 작고 의미 있게 작성
- edge case를 포함

---

### [FAQ]

Q. Pure Function은 뭐야?
A. 같은 입력이면 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Pure Function이 Unit Test에 좋은 이유는?
A. 외부 환경에 의존하지 않아 빠르고 안정적으로 검증할 수 있기 때문이다.

Q. Date나 Random이 들어간 함수는 어떻게 테스트해?
A. 현재 시간이나 랜덤 값을 함수 내부에서 직접 만들지 말고 인자로 주입하는 방식이 좋다.

---

## 2.2 Pure Function Test Pattern

### [개념]

Pure Function Test Pattern은 함수 입력, 실행 결과, 기대 출력을 명확히 분리해 검증하는 방식이다.

Given / When / Then 구조를 적용할 수 있다.

---

### [핵심]

Test Pattern:

- Given input
- When function called
- Then output equals expected
- edge case
- boundary case
- invalid input
- null / undefined caution
- deterministic assertion

---

### [실무]

예:

```ts
export function getFestivalStatus(
  startDate: string,
  endDate: string,
  today: string,
) {
  if (today < startDate) return "UPCOMING";
  if (today > endDate) return "ENDED";
  return "ACTIVE";
}
```

테스트:

```ts
describe("getFestivalStatus", () => {
  test("오늘이 시작일 전이면 UPCOMING을 반환한다", () => {
    expect(getFestivalStatus("2026-08-01", "2026-08-10", "2026-07-20")).toBe(
      "UPCOMING",
    );
  });

  test("오늘이 기간 안이면 ACTIVE를 반환한다", () => {
    expect(getFestivalStatus("2026-08-01", "2026-08-10", "2026-08-05")).toBe(
      "ACTIVE",
    );
  });

  test("오늘이 종료일 후면 ENDED를 반환한다", () => {
    expect(getFestivalStatus("2026-08-01", "2026-08-10", "2026-08-11")).toBe(
      "ENDED",
    );
  });
});
```

권장:

- 함수명 기준 describe 사용
- 테스트명은 입력 상황과 기대 결과 포함
- boundary value 포함
- 한 테스트에 하나의 핵심 기대 결과
- 불필요한 mock 사용 지양

---

### [FAQ]

Q. Pure Function Test 이름은 어떻게 써?
A. 어떤 입력 상황에서 어떤 결과를 반환하는지 드러나게 작성한다.

Q. 하나의 함수에 테스트를 몇 개 써야 해?
A. 정상 케이스, 실패 케이스, 경계값을 기준으로 필요한 만큼 작성한다.

Q. Pure Function Test에 mock이 필요해?
A. 대부분 필요 없다. 외부 의존이 있다면 함수 설계를 먼저 점검한다.

---

# 3. Validation Function Test

## 3.1 Validation Function Definition

### [개념]

Validation Function Test는 Form 입력값 검증 로직을 독립적으로 검증하는 Unit Test다.

Frontend Form 검증 로직이 복잡할수록 validation function을 분리해 테스트하는 것이 좋다.

---

### [핵심]

Validation 대상:

- required
- email format
- password format
- password confirm
- min length
- max length
- number range
- date range
- file size
- file type
- whitespace
- forbidden word
- cross field validation

---

### [실무]

예:

```ts
type LoginValues = {
  email: string;
  password: string;
};

export function validateLogin(values: LoginValues) {
  const errors: Partial<Record<keyof LoginValues, string>> = {};

  if (!values.email.trim()) {
    errors.email = "이메일을 입력해 주세요.";
  }

  if (!values.password.trim()) {
    errors.password = "비밀번호를 입력해 주세요.";
  }

  return errors;
}
```

테스트:

```ts
test("이메일이 비어 있으면 email 오류를 반환한다", () => {
  const errors = validateLogin({
    email: "",
    password: "password123",
  });

  expect(errors.email).toBe("이메일을 입력해 주세요.");
});

test("비밀번호가 비어 있으면 password 오류를 반환한다", () => {
  const errors = validateLogin({
    email: "test@example.com",
    password: "",
  });

  expect(errors.password).toBe("비밀번호를 입력해 주세요.");
});
```

권장:

- 공백 입력 테스트
- 정상 입력 테스트
- 필드별 오류 테스트
- 여러 필드 간 관계 테스트
- Backend validation 기준과 일치 여부 확인

---

### [FAQ]

Q. Validation Function Test는 뭐야?
A. Form 입력값 검증 로직을 함수 단위로 분리해 검증하는 테스트다.

Q. Validation은 Component Test만 하면 안 돼?
A. 간단하면 가능하지만 검증 규칙이 복잡하면 Unit Test가 더 빠르고 명확하다.

Q. 공백 입력도 테스트해야 해?
A. 중요하다. 빈 문자열과 공백 문자열은 validation에서 자주 문제가 된다.

---

## 3.2 Required Field Validation Test

### [개념]

Required Field Validation Test는 필수 입력값이 비었을 때 적절한 오류가 반환되는지 검증하는 테스트다.

Form validation의 가장 기본적인 Unit Test다.

---

### [핵심]

Required 검증 대상:

- empty string
- whitespace only
- null caution
- undefined caution
- unchecked checkbox
- unselected radio
- unselected select
- empty array
- missing file

---

### [실무]

예:

```ts
export function validateReview(values: {
  rating: number | null;
  content: string;
}) {
  const errors: {
    rating?: string;
    content?: string;
  } = {};

  if (values.rating == null) {
    errors.rating = "평점을 선택해 주세요.";
  }

  if (!values.content.trim()) {
    errors.content = "리뷰 내용을 입력해 주세요.";
  }

  return errors;
}
```

테스트:

```ts
test("평점이 없으면 rating 오류를 반환한다", () => {
  const errors = validateReview({
    rating: null,
    content: "좋았어요",
  });

  expect(errors.rating).toBe("평점을 선택해 주세요.");
});

test("리뷰 내용이 공백이면 content 오류를 반환한다", () => {
  const errors = validateReview({
    rating: 5,
    content: "   ",
  });

  expect(errors.content).toBe("리뷰 내용을 입력해 주세요.");
});
```

권장:

- 빈 문자열과 공백 문자열 모두 고려
- checkbox / select / file 필수값도 검증
- 오류 key가 field name과 일치하는지 확인
- 오류 메시지가 자주 바뀌면 error code 방식 고려

---

### [FAQ]

Q. Required Validation에서 공백 문자열도 실패로 봐야 해?
A. 일반적으로 필수 텍스트 입력은 trim 후 빈 값이면 실패로 처리한다.

Q. rating이 0이면 비어 있는 값이야?
A. 도메인 규칙에 따라 다르다. 평점 범위가 1~5라면 0은 invalid로 처리할 수 있다.

Q. 오류 메시지 문자열까지 테스트해야 해?
A. 사용자에게 중요한 메시지라면 가능하다. 문구 변경이 잦으면 error code 테스트를 고려한다.

---

## 3.3 Format Validation Test

### [개념]

Format Validation Test는 이메일, 비밀번호, 전화번호, URL 같은 입력값 형식이 규칙에 맞는지 검증하는 테스트다.

---

### [핵심]

Format 검증 대상:

- email format
- password pattern
- phone number
- URL
- nickname pattern
- file extension
- date format
- number string
- regex validation

---

### [실무]

이메일 검증 예:

```ts
export function isValidEmail(email: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
```

테스트:

```ts
test("올바른 이메일 형식이면 true를 반환한다", () => {
  expect(isValidEmail("test@example.com")).toBe(true);
});

test("이메일에 @가 없으면 false를 반환한다", () => {
  expect(isValidEmail("test.example.com")).toBe(false);
});

test("이메일에 도메인이 없으면 false를 반환한다", () => {
  expect(isValidEmail("test@")).toBe(false);
});
```

비밀번호 검증 예:

```ts
export function isValidPassword(password: string) {
  return password.length >= 8;
}
```

권장:

- 정상 케이스와 실패 케이스 모두 작성
- regex가 너무 복잡하면 유지보수성 검토
- Backend validation과 기준 일치
- 보안상 실제 비밀번호 사용 금지

---

### [FAQ]

Q. 이메일 정규식은 완벽해야 해?
A. 실무에서는 과도하게 복잡한 정규식보다 서비스 기준에 맞는 현실적인 검증을 사용한다.

Q. Format Validation은 Backend와 같아야 해?
A. 가능하면 동일한 기준을 유지해야 사용자 경험과 서버 오류를 줄일 수 있다.

Q. 비밀번호 테스트에 실제 비밀번호를 써도 돼?
A. 안 된다. 테스트용 더미 문자열을 사용한다.

---

## 3.4 Range Validation Test

### [개념]

Range Validation Test는 숫자, 날짜, 길이, 파일 크기 같은 값이 허용 범위 안에 있는지 검증하는 테스트다.

경계값 테스트가 중요하다.

---

### [핵심]

Range 검증 대상:

- min length
- max length
- min value
- max value
- rating range
- date range
- file size
- array length
- pagination size
- boundary value

---

### [실무]

평점 검증 예:

```ts
export function isValidRating(rating: number) {
  return rating >= 1 && rating <= 5;
}
```

테스트:

```ts
test("평점이 1이면 true를 반환한다", () => {
  expect(isValidRating(1)).toBe(true);
});

test("평점이 5이면 true를 반환한다", () => {
  expect(isValidRating(5)).toBe(true);
});

test("평점이 0이면 false를 반환한다", () => {
  expect(isValidRating(0)).toBe(false);
});

test("평점이 6이면 false를 반환한다", () => {
  expect(isValidRating(6)).toBe(false);
});
```

문자 길이 검증:

```ts
export function isValidContentLength(content: string) {
  return content.trim().length >= 10 && content.trim().length <= 500;
}
```

권장:

- 최소값 바로 아래 / 최소값 / 최대값 / 최대값 바로 위 테스트
- 빈 값 검증과 range 검증 구분
- 숫자 문자열은 Number 변환 기준 명확히 설정
- 날짜 range는 timezone 영향 주의

---

### [FAQ]

Q. Range Validation에서 가장 중요한 테스트는 뭐야?
A. 최소값, 최대값, 최소값 바로 아래, 최대값 바로 위 같은 boundary value 테스트다.

Q. 숫자 문자열은 Unit Test에서 어떻게 처리해?
A. 문자열을 Number로 변환하는지, 변환 실패 시 어떻게 처리하는지 명확히 테스트한다.

Q. 날짜 range 테스트는 왜 조심해야 해?
A. timezone과 날짜 포맷 차이로 결과가 달라질 수 있기 때문이다.

---

# 4. Formatter Test

## 4.1 Formatter Function Definition

### [개념]

Formatter Function은 숫자, 날짜, 상태값, 코드값을 사용자가 읽기 쉬운 문자열로 변환하는 함수다.

Formatter Test는 표시 규칙이 올바른지 검증한다.

---

### [핵심]

Formatter 대상:

- price formatter
- date formatter
- date range formatter
- rating formatter
- count formatter
- status label formatter
- category label formatter
- region label formatter
- relative time formatter
- file size formatter

---

### [실무]

금액 formatter 예:

```ts
export function formatWon(value: number) {
  return `${value.toLocaleString("ko-KR")}원`;
}
```

테스트:

```ts
test("숫자를 원화 문자열로 변환한다", () => {
  expect(formatWon(1234567)).toBe("1,234,567원");
});

test("0원을 표시한다", () => {
  expect(formatWon(0)).toBe("0원");
});
```

상태 formatter 예:

```ts
export function formatFestivalStatus(status: "UPCOMING" | "ACTIVE" | "ENDED") {
  const labels = {
    UPCOMING: "예정",
    ACTIVE: "진행 중",
    ENDED: "종료",
  };

  return labels[status];
}
```

권장:

- locale 명시
- 0, 음수, 큰 수 테스트
- unknown code 처리 기준 정의
- UI 문구 변경 가능성 관리
- i18n 적용 시 translation key 전략 검토

---

### [FAQ]

Q. Formatter Test는 왜 필요해?
A. 사용자에게 표시되는 금액, 날짜, 상태 문구가 규칙대로 변환되는지 빠르게 검증할 수 있기 때문이다.

Q. toLocaleString은 테스트에서 조심해야 해?
A. locale을 명시하지 않으면 환경에 따라 결과가 달라질 수 있다.

Q. unknown code는 어떻게 테스트해?
A. 도메인 정책에 따라 기본값을 반환할지 오류를 낼지 정하고 테스트한다.

---

## 4.2 Date Formatter Test

### [개념]

Date Formatter Test는 날짜와 시간 값을 사용자 표시 문자열로 변환하는 규칙을 검증한다.

날짜 테스트는 timezone, locale, input format 영향을 주의해야 한다.

---

### [핵심]

Date Formatter 대상:

- yyyy-MM-dd
- yyyy.MM.dd
- date range
- time label
- relative time
- start date
- end date
- timezone caution
- locale caution
- invalid date

---

### [실무]

권장 예:

```ts
export function formatDate(dateText: string) {
  const date = new Date(`${dateText}T00:00:00`);
  return new Intl.DateTimeFormat("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(date);
}
```

테스트:

```ts
test("날짜 문자열을 ko-KR 날짜 표시로 변환한다", () => {
  expect(formatDate("2026-07-06")).toBe("2026. 07. 06.");
});
```

단순 문자열 변환이 더 안정적인 경우:

```ts
export function formatDateDot(dateText: string) {
  return dateText.replaceAll("-", ".");
}
```

테스트:

```ts
test("yyyy-MM-dd를 yyyy.MM.dd로 변환한다", () => {
  expect(formatDateDot("2026-07-06")).toBe("2026.07.06");
});
```

권장:

- 테스트 입력 날짜 고정
- 현재 날짜 직접 사용 지양
- timezone이 필요한 경우 명시
- 날짜 범위 formatter는 시작일 / 종료일 모두 검증
- invalid date 처리 기준 테스트

---

### [FAQ]

Q. Date Formatter Test가 자주 깨지는 이유는?
A. timezone, locale, 현재 시간 의존 때문에 환경별 결과가 달라질 수 있기 때문이다.

Q. 현재 날짜 기준 함수는 어떻게 테스트해?
A. 현재 날짜를 함수 인자로 주입하거나 timer mock을 사용한다.

Q. 날짜 포맷은 Intl을 써야 해?
A. 복잡한 locale 표시에는 Intl이 좋고, 단순 yyyy-MM-dd 변환은 문자열 처리도 가능하다.

---

## 4.3 Count Formatter Test

### [개념]

Count Formatter Test는 조회수, 좋아요 수, 댓글 수, 알림 수 같은 숫자를 사용자 표시 문구로 변환하는 규칙을 검증한다.

---

### [핵심]

Count Formatter 대상:

- like count
- comment count
- notification count
- view count
- review count
- compact number
- 999+
- 1K
- empty count
- zero count

---

### [실무]

예:

```ts
export function formatNotificationCount(count: number) {
  if (count <= 0) return "";
  if (count > 99) return "99+";
  return String(count);
}
```

테스트:

```ts
test("알림 개수가 0이면 빈 문자열을 반환한다", () => {
  expect(formatNotificationCount(0)).toBe("");
});

test("알림 개수가 5이면 5를 반환한다", () => {
  expect(formatNotificationCount(5)).toBe("5");
});

test("알림 개수가 100 이상이면 99+를 반환한다", () => {
  expect(formatNotificationCount(100)).toBe("99+");
});
```

권장:

- 0 처리
- 음수 처리
- 최대 표시 기준 테스트
- 큰 수 축약 기준 테스트
- 도메인별 표시 정책 통일

---

### [FAQ]

Q. Count Formatter는 왜 테스트해?
A. 0, 큰 수, 최대 표시값 같은 edge case가 UI에서 자주 문제 되기 때문이다.

Q. 알림 수 0은 어떻게 표시해?
A. 도메인 정책에 따라 빈 문자열, 0, 숨김 중 하나로 정하고 테스트한다.

Q. 99+ 같은 표시는 Unit Test가 적합해?
A. 적합하다. 입력과 출력이 명확한 formatter 로직이기 때문이다.

---

# 5. Mapper Test

## 5.1 Mapper Function Definition

### [개념]

Mapper Function은 API 응답, Form 입력값, 내부 상태 값을 다른 구조로 변환하는 함수다.

Mapper Test는 데이터 구조 변환이 올바른지 검증한다.

---

### [핵심]

Mapper 대상:

- API response mapper
- View Model mapper
- Form values mapper
- Request DTO mapper
- Error response mapper
- Select option mapper
- Table row mapper
- Card props mapper
- enum label mapper

---

### [실무]

Form values → Request DTO 예:

```ts
type ReviewFormValues = {
  rating: string;
  content: string;
};

export function toCreateReviewRequest(
  festivalId: number,
  values: ReviewFormValues,
) {
  return {
    festivalId,
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

테스트:

```ts
test("리뷰 form 값을 리뷰 등록 요청 DTO로 변환한다", () => {
  const result = toCreateReviewRequest(1, {
    rating: "5",
    content: " 좋았어요 ",
  });

  expect(result).toEqual({
    festivalId: 1,
    rating: 5,
    content: "좋았어요",
  });
});
```

권장:

- field name 변환 검증
- type 변환 검증
- trim / default value 검증
- optional field 처리 검증
- Backend API request shape와 일치 확인

---

### [FAQ]

Q. Mapper Test는 뭐야?
A. API 응답, Form 값, 내부 상태 값을 다른 데이터 구조로 변환하는 로직을 검증하는 테스트다.

Q. Form 값을 Request DTO로 바꾸는 함수도 Unit Test 대상이야?
A. 그렇다. 입력과 출력이 명확하므로 Unit Test에 적합하다.

Q. Mapper Test에서 가장 중요한 건 뭐야?
A. field 이름, 타입 변환, optional/default 처리, Backend API shape와의 일치다.

---

## 5.2 API Response Mapper Test

### [개념]

API Response Mapper Test는 Backend API 응답을 Frontend 화면에서 쓰기 좋은 View Model로 변환하는 로직을 검증한다.

API shape 변경에 따른 회귀를 줄이는 데 유용하다.

---

### [핵심]

API Response Mapper 대상:

- response field rename
- null handling
- default image
- code to label
- date format
- nested object flatten
- pagination data
- list item mapper
- optional field
- backend shape consistency

---

### [실무]

예:

```ts
type FestivalResponse = {
  festivalId: number;
  title: string;
  regionName: string | null;
  imageUrl: string | null;
};

export function toFestivalCardView(response: FestivalResponse) {
  return {
    id: response.festivalId,
    title: response.title,
    region: response.regionName ?? "지역 정보 없음",
    imageUrl: response.imageUrl ?? "/images/default-festival.png",
  };
}
```

테스트:

```ts
test("축제 응답을 카드 View Model로 변환한다", () => {
  const result = toFestivalCardView({
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: "서울",
    imageUrl: "/festival.png",
  });

  expect(result).toEqual({
    id: 1,
    title: "봄꽃 축제",
    region: "서울",
    imageUrl: "/festival.png",
  });
});

test("지역과 이미지가 null이면 기본값을 사용한다", () => {
  const result = toFestivalCardView({
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: null,
    imageUrl: null,
  });

  expect(result.region).toBe("지역 정보 없음");
  expect(result.imageUrl).toBe("/images/default-festival.png");
});
```

권장:

- null response 처리
- 기본 이미지 / 기본 문구 처리
- nested response flatten 검증
- API 변경 시 mapper test 실패로 감지
- 실제 Backend DTO와 field명 맞춤

---

### [FAQ]

Q. API Response Mapper는 왜 필요해?
A. Backend 응답 구조와 Frontend 화면 구조를 분리하고 변환 규칙을 명확히 하기 위해 필요하다.

Q. API response에 null이 올 수 있으면 테스트해야 해?
A. 해야 한다. null 처리 누락은 UI 오류로 이어지기 쉽다.

Q. Mapper Test가 API 통합 테스트를 대체해?
A. 아니다. Mapper 로직 검증은 가능하지만 실제 API 연동은 별도 Integration 또는 E2E 검증이 필요하다.

---

## 5.3 Error Mapper Test

### [개념]

Error Mapper Test는 API error code, HTTP status, validation error를 사용자 메시지로 변환하는 로직을 검증한다.

Error UX의 일관성을 유지하는 데 중요하다.

---

### [핵심]

Error Mapper 대상:

- HTTP status
- error code
- field error
- global error
- network error
- timeout error
- unauthorized
- forbidden
- not found
- conflict
- server error
- fallback message

---

### [실무]

예:

```ts
export function mapApiErrorMessage(status?: number) {
  if (status === 401) return "로그인이 필요합니다.";
  if (status === 403) return "접근 권한이 없습니다.";
  if (status === 404) return "요청한 정보를 찾을 수 없습니다.";
  if (status === 500)
    return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";

  return "알 수 없는 오류가 발생했습니다.";
}
```

테스트:

```ts
test("401이면 로그인 필요 메시지를 반환한다", () => {
  expect(mapApiErrorMessage(401)).toBe("로그인이 필요합니다.");
});

test("403이면 권한 없음 메시지를 반환한다", () => {
  expect(mapApiErrorMessage(403)).toBe("접근 권한이 없습니다.");
});

test("알 수 없는 status면 fallback 메시지를 반환한다", () => {
  expect(mapApiErrorMessage(undefined)).toBe("알 수 없는 오류가 발생했습니다.");
});
```

권장:

- 주요 HTTP status별 메시지 테스트
- fallback 메시지 테스트
- field error와 global error 구분
- AxiosError shape와 연결되는 경우 별도 테스트
- 서버 내부 에러 상세 노출 금지

---

### [FAQ]

Q. Error Mapper Test는 왜 필요해?
A. API 실패 상황에서 사용자에게 일관되고 안전한 메시지를 표시하기 위해 필요하다.

Q. 500 에러 메시지는 어떻게 처리해야 해?
A. 서버 내부 상세를 노출하지 않고 일반적인 안내 메시지를 반환하는 것이 좋다.

Q. 알 수 없는 에러도 테스트해야 해?
A. 해야 한다. fallback 메시지는 예외 상황에서 사용자 경험을 보호한다.

---

# 6. Filter and Sorting Test

## 6.1 Filter Function Test

### [개념]

Filter Function Test는 목록 데이터가 검색어, 카테고리, 상태, 권한, 날짜 조건에 따라 올바르게 필터링되는지 검증하는 테스트다.

---

### [핵심]

Filter 대상:

- keyword filter
- category filter
- region filter
- status filter
- active item filter
- permission filter
- date range filter
- empty result
- case insensitive
- whitespace trim

---

### [실무]

예:

```ts
type Festival = {
  title: string;
  region: string;
};

export function filterFestivalsByKeyword(
  festivals: Festival[],
  keyword: string,
) {
  const normalizedKeyword = keyword.trim().toLowerCase();

  if (!normalizedKeyword) return festivals;

  return festivals.filter((festival) =>
    festival.title.toLowerCase().includes(normalizedKeyword),
  );
}
```

테스트:

```ts
const festivals = [
  { title: "봄꽃 축제", region: "서울" },
  { title: "음악 축제", region: "부산" },
];

test("검색어가 포함된 축제만 반환한다", () => {
  expect(filterFestivalsByKeyword(festivals, "봄꽃")).toEqual([
    { title: "봄꽃 축제", region: "서울" },
  ]);
});

test("검색어가 공백이면 전체 목록을 반환한다", () => {
  expect(filterFestivalsByKeyword(festivals, "   ")).toEqual(festivals);
});
```

권장:

- empty keyword 처리
- 공백 trim 처리
- 대소문자 처리
- 결과 없음 처리
- 원본 배열 mutation 여부 주의

---

### [FAQ]

Q. Filter Function은 Unit Test 대상이야?
A. 입력 배열과 조건에 따라 출력 배열이 명확하므로 Unit Test에 적합하다.

Q. 검색어 공백도 테스트해야 해?
A. 해야 한다. 공백 검색어 처리는 실제 검색 UI에서 자주 발생한다.

Q. filter 함수가 원본 배열을 바꾸면 안 돼?
A. 일반적으로 원본 배열을 변경하지 않는 방식이 안전하다.

---

## 6.2 Sorting Function Test

### [개념]

Sorting Function Test는 목록 데이터가 날짜, 인기순, 이름순, 평점순, 생성일순 등 기준에 따라 올바르게 정렬되는지 검증하는 테스트다.

---

### [핵심]

Sorting 대상:

- date sort
- createdAt sort
- rating sort
- like count sort
- review count sort
- name sort
- priority sort
- null handling
- stable sort caution
- ascending
- descending

---

### [실무]

예:

```ts
type Festival = {
  title: string;
  likeCount: number | null;
};

export function sortByLikeCountDesc(festivals: Festival[]) {
  return [...festivals].sort((a, b) => (b.likeCount ?? 0) - (a.likeCount ?? 0));
}
```

테스트:

```ts
test("좋아요 수 기준 내림차순으로 정렬한다", () => {
  const result = sortByLikeCountDesc([
    { title: "A 축제", likeCount: 10 },
    { title: "B 축제", likeCount: 30 },
    { title: "C 축제", likeCount: 20 },
  ]);

  expect(result.map((item) => item.title)).toEqual([
    "B 축제",
    "C 축제",
    "A 축제",
  ]);
});

test("likeCount가 null이면 0으로 처리한다", () => {
  const result = sortByLikeCountDesc([
    { title: "A 축제", likeCount: null },
    { title: "B 축제", likeCount: 5 },
  ]);

  expect(result.map((item) => item.title)).toEqual(["B 축제", "A 축제"]);
});
```

권장:

- 원본 배열 mutation 방지
- null / undefined 처리
- asc / desc 명확히 테스트
- 동률 처리 기준이 있으면 테스트
- 날짜 정렬은 ISO 문자열 또는 timestamp 기준 권장

---

### [FAQ]

Q. Sorting Function도 Unit Test 대상이야?
A. 그렇다. 입력 목록과 기대 순서가 명확하므로 Unit Test에 적합하다.

Q. sort는 원본 배열을 바꿔?
A. JavaScript `sort`는 원본 배열을 변경한다. 테스트 대상 함수에서 복사 후 정렬하는 것이 안전하다.

Q. null 값 정렬은 테스트해야 해?
A. 해야 한다. null 처리 기준이 없으면 실제 목록 UI에서 오류나 예상치 못한 순서가 발생할 수 있다.

---

# 7. Select Option Mapper Test

## 7.1 Select Option Mapper Definition

### [개념]

Select Option Mapper는 API 코드 목록이나 도메인 enum을 select option 형태로 변환하는 함수다.

Filter Form, Search Form, Category Select, Region Select에서 자주 사용한다.

---

### [핵심]

Select Option Mapper 대상:

- category code
- region code
- theme code
- enum to option
- label
- value
- disabled option
- default option
- all option
- sorted option
- API code list

---

### [실무]

예:

```ts
type CategoryCode = {
  code: string;
  name: string;
};

export function toCategoryOptions(categories: CategoryCode[]) {
  return [
    { label: "전체", value: "" },
    ...categories.map((category) => ({
      label: category.name,
      value: category.code,
    })),
  ];
}
```

테스트:

```ts
test("카테고리 코드를 select option으로 변환한다", () => {
  const result = toCategoryOptions([
    { code: "MUSIC", name: "음악" },
    { code: "FLOWER", name: "꽃" },
  ]);

  expect(result).toEqual([
    { label: "전체", value: "" },
    { label: "음악", value: "MUSIC" },
    { label: "꽃", value: "FLOWER" },
  ]);
});
```

권장:

- 기본 옵션 포함 여부 테스트
- label / value 매핑 정확성 테스트
- 빈 배열 처리 테스트
- 정렬 기준이 있으면 테스트
- Backend code 변경에 취약한 부분 관리

---

### [FAQ]

Q. Select Option Mapper는 왜 테스트해?
A. API 코드와 화면 select option의 label/value 매핑 오류를 빠르게 잡을 수 있기 때문이다.

Q. 전체 옵션도 테스트해야 해?
A. 필터 UI에서 중요하다면 기본 옵션 포함 여부를 테스트하는 것이 좋다.

Q. API 코드 이름이 바뀌면 어떻게 돼?
A. Mapper Test가 실패해 Frontend 매핑 수정 필요를 빠르게 알 수 있다.

---

# 8. Unit Test Naming and Structure

## 8.1 Unit Test Naming Rules

### [개념]

Unit Test 이름은 어떤 입력 상황에서 어떤 결과가 나오는지 명확하게 작성해야 한다.

테스트 실패 시 원인을 빠르게 파악할 수 있어야 한다.

---

### [핵심]

좋은 이름:

- 입력 상황 포함
- 기대 결과 포함
- 도메인 규칙 포함
- edge case 명시
- 모호한 이름 지양
- implementation name보다 behavior 중심

---

### [실무]

좋은 예:

```ts
test("리뷰 내용이 공백이면 content 오류를 반환한다", () => {});
test("평점이 0이면 false를 반환한다", () => {});
test("likeCount가 null이면 0으로 처리해 정렬한다", () => {});
test("API 응답의 imageUrl이 null이면 기본 이미지를 사용한다", () => {});
```

나쁜 예:

```ts
test("works", () => {});
test("valid test", () => {});
test("case1", () => {});
test("function returns value", () => {});
```

권장:

- 한국어 프로젝트면 한글 테스트명 가능
- describe는 함수명 중심
- test는 조건과 결과 중심
- 실패 메시지를 보지 않아도 의도가 드러나야 함

---

### [FAQ]

Q. Unit Test 이름은 어떻게 작성해?
A. 입력 조건과 기대 결과가 드러나게 작성한다.

Q. 테스트 이름을 한글로 써도 돼?
A. 가능하다. 팀 컨벤션에 맞추되 의미가 명확해야 한다.

Q. works 같은 테스트명이 왜 안 좋아?
A. 무엇이 동작해야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

---

## 8.2 Unit Test Structure Rules

### [개념]

Unit Test Structure는 테스트 파일과 테스트 케이스를 일관되게 구성하는 기준이다.

함수별 describe와 케이스별 test를 사용하면 검색성과 유지보수성이 좋아진다.

---

### [핵심]

구조 기준:

- describe by function
- test by scenario
- Arrange Act Assert
- Given When Then
- small input data
- expected output explicit
- one reason to fail
- no unnecessary mock

---

### [실무]

권장 구조:

```ts
describe("validateReview", () => {
  test("리뷰 내용이 공백이면 content 오류를 반환한다", () => {
    const values = {
      rating: 5,
      content: "   ",
    };

    const errors = validateReview(values);

    expect(errors.content).toBe("리뷰 내용을 입력해 주세요.");
  });
});
```

파일 위치 예:

```text
src/features/review/utils/validateReview.ts
src/features/review/utils/validateReview.test.ts
```

또는:

```text
src/features/review/__tests__/validateReview.test.ts
```

권장:

- 테스트 대상 함수와 가까운 위치에 배치 가능
- 공통 test data는 과도하게 추상화하지 않음
- 한 파일에 너무 많은 도메인을 섞지 않음
- 함수가 비대하면 함수 분리 검토

---

### [FAQ]

Q. Unit Test 파일은 어디에 둬?
A. 테스트 대상 함수 옆에 두거나 feature의 `__tests__` 폴더에 둘 수 있다.

Q. Arrange Act Assert 구조는 뭐야?
A. 입력 준비, 함수 실행, 결과 검증을 분리하는 테스트 구조다.

Q. 한 테스트에 여러 assertion을 넣어도 돼?
A. 같은 행동의 결과라면 가능하지만 실패 원인이 흐려질 정도로 많이 넣지 않는다.

---

# 9. Unit Test Anti Pattern

## 9.1 Common Unit Test Anti Patterns

### [개념]

Unit Test Anti Pattern은 테스트를 느리고 불안정하게 만들거나 테스트 의도를 흐리는 잘못된 작성 방식이다.

Frontend Unit Test는 작고 명확하며 외부 의존이 적어야 한다.

---

### [핵심]

Anti Pattern:

- React Component를 Unit Test로 억지 검증
- DOM 의존 utility
- API 호출 포함
- localStorage 직접 의존
- Date.now 직접 의존
- Math.random 직접 의존
- 과도한 mock
- 테스트 데이터 과대화
- snapshot으로 함수 결과 검증
- implementation detail 과도 검증
- 하나의 테스트에 여러 시나리오 혼합
- 실제 secret / token 사용

---

### [실무]

나쁜 예:

```ts
test("오늘 날짜 라벨을 반환한다", () => {
  expect(getTodayLabel()).toBe("2026-07-06");
});
```

문제:

```text
현재 날짜에 직접 의존
→ 날짜가 바뀌면 실패
```

개선:

```ts
test("입력 날짜를 날짜 라벨로 변환한다", () => {
  expect(formatDateLabel("2026-07-06")).toBe("2026.07.06");
});
```

나쁜 예:

```ts
test("사용자 정보를 가져온다", async () => {
  const user = await fetchUser();
  expect(user.name).toBe("tester");
});
```

문제:

```text
실제 API 의존
→ Unit Test가 아님
```

---

### [FAQ]

Q. Unit Test에서 실제 API를 호출해도 돼?
A. 안 된다. API 호출은 mock을 사용하거나 Integration Test에서 다룬다.

Q. Date.now를 직접 쓰는 함수는 어떻게 테스트해?
A. 날짜를 인자로 주입하거나 timer mock을 사용한다.

Q. Unit Test에 mock이 많으면 문제야?
A. 외부 의존이 많다는 신호일 수 있다. 함수 설계를 먼저 점검한다.

---

## 9.2 Over Testing Caution

### [개념]

Over Testing은 테스트 가치가 낮은 구현 세부사항까지 과도하게 검증해 유지보수 비용을 높이는 문제다.

Unit Test는 중요한 로직과 edge case를 중심으로 작성한다.

---

### [핵심]

Over Testing 대상:

- 단순 getter
- 단순 object spread
- trivial wrapper
- 타입 시스템이 이미 보장하는 내용
- 구현 순서
- 내부 변수명
- 사소한 중간값
- 의미 없는 branch
- 과도한 private helper 테스트

---

### [실무]

낮은 가치 예:

```ts
export function getTitle(item: { title: string }) {
  return item.title;
}
```

테스트 필요성이 낮음:

```ts
test("title을 반환한다", () => {
  expect(getTitle({ title: "축제" })).toBe("축제");
});
```

테스트 가치 높은 예:

```ts
export function calculateDiscountPrice(price: number, rate: number) {
  if (price < 0) throw new Error("price must be positive");
  if (rate < 0 || rate > 100) throw new Error("invalid rate");

  return Math.floor(price * (1 - rate / 100));
}
```

테스트 가치 판단:

```text
버그 가능성이 있는가?
도메인 규칙이 있는가?
edge case가 있는가?
반복 사용되는가?
실패 영향이 큰가?
```

---

### [FAQ]

Q. 모든 utility 함수를 Unit Test해야 해?
A. 아니다. 도메인 규칙, 변환 로직, edge case가 있는 함수를 우선 테스트한다.

Q. 단순 getter도 테스트해야 해?
A. 대부분 테스트 가치가 낮다.

Q. Over Testing이 왜 문제야?
A. 작은 리팩토링에도 테스트 수정이 많아지고 유지보수 비용이 커진다.

---

# 10. Unit Test Security Rules

## 10.1 Test Data Security

### [개념]

Test Data Security는 Unit Test 코드에 실제 개인정보, token, secret, 운영 URL, 결제 정보가 포함되지 않도록 하는 기준이다.

Frontend Unit Test도 보안 검수 대상이다.

---

### [핵심]

금지 대상:

- real password
- real access token
- real refresh token
- API secret
- OAuth secret
- personal email
- phone number
- address
- production URL
- payment information
- real user data
- private file content

---

### [실무]

권장 더미 데이터:

```ts
const testUser = {
  userId: 1,
  email: "test@example.com",
  nickname: "tester",
};
```

금지 예:

```ts
const token = "실제_운영_ACCESS_TOKEN";
const email = "real-user-company-email@example.com";
```

권장:

- 테스트용 더미 email 사용
- 실제 token / secret commit 금지
- 실제 운영 API URL 사용 금지
- snapshot에 민감정보 포함 주의
- 업로드 파일 테스트에는 더미 File 사용

---

### [FAQ]

Q. Unit Test에 실제 token을 넣어도 돼?
A. 안 된다. 테스트에는 더미 token을 사용하고 실제 secret은 절대 commit하지 않는다.

Q. 테스트용 email은 어떻게 써?
A. `test@example.com` 같은 명확한 더미 값을 사용한다.

Q. 운영 API URL을 테스트 상수로 넣어도 돼?
A. 권장하지 않는다. 테스트는 운영 환경과 분리되어야 한다.

---

# 11. Unit Test Checklist

## 11.1 Unit Test Checklist

### [개념]

Unit Test Checklist는 Frontend Unit Test가 빠르고 명확하며 독립적인지 검수하는 기준이다.

Agent는 Unit Test 작성 전 테스트 대상이 Unit Test에 적합한지 먼저 판단해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 입력과 출력이 명확한가?
- [ ] React render 없이 테스트 가능한가?
- [ ] 외부 API에 의존하지 않는가?
- [ ] DOM에 의존하지 않는가?
- [ ] Date.now / Math.random 직접 의존을 피했는가?
- [ ] 정상 케이스와 실패 케이스를 포함했는가?
- [ ] boundary value를 검증했는가?
- [ ] null / undefined / empty 처리를 검증했는가?
- [ ] 원본 배열 mutation 여부를 고려했는가?
- [ ] 테스트명이 조건과 기대 결과를 포함하는가?
- [ ] mock을 과도하게 사용하지 않았는가?
- [ ] 실제 secret / token / 개인정보를 사용하지 않았는가?
```

---

### [실무]

Agent Unit Test 작성 Flow:

```text
Identify Logic
→ Check Pure Function 가능 여부
→ Define Input Cases
→ Define Expected Output
→ Include Edge Cases
→ Write Unit Test
→ Check Anti Pattern
→ Check Security Data
```

예:

```text
Review Validation
→ content required
→ rating range
→ whitespace content
→ valid input
→ error object 검증
```

---

### [FAQ]

Q. Unit Test 작성 전 무엇을 확인해야 해?
A. 입력과 출력이 명확한지, 외부 의존 없이 테스트 가능한지 먼저 확인한다.

Q. Unit Test에서 edge case는 왜 중요해?
A. 작은 로직의 버그는 주로 빈 값, 경계값, null, 잘못된 형식에서 발생하기 때문이다.

Q. Unit Test Checklist의 핵심은 뭐야?
A. 독립성, 명확한 입력/출력, edge case, 외부 의존 제거다.

---

# 12. Part05 Summary

## 12.1 Unit Test Final Rule

### [개념]

Frontend Testing Part05는 Frontend Unit Test의 대상, 작성 기준, validation, formatter, mapper, filter, sorting 테스트 기준을 정의한다.

이 Part의 목적은 Agent가 React render 없이 검증 가능한 작은 로직을 안정적으로 테스트하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Unit Test는 입력과 출력이 명확한 로직에 사용
- Pure Function Test 우선
- Validation Function Test는 Form 규칙 검증에 적합
- Formatter Test는 사용자 표시 문자열 검증
- Mapper Test는 API / Form / View Model 변환 검증
- Filter / Sorting Test는 목록 로직 검증
- Date / Random / API 직접 의존 지양
- 정상 / 실패 / 경계값 테스트 포함
- 테스트명은 조건과 결과 중심
- 실제 secret / token / 개인정보 사용 금지
- Component 사용자 흐름은 Component Test 또는 Integration Test로 검증

---

### [실무]

Agent 작업 Flow:

```text
Unit Test Request
→ Identify Pure Logic
→ Separate from Component if Needed
→ Define Test Cases
→ Include Edge Cases
→ Assert Exact Output
→ Review Mutation / External Dependency
→ Check Test Data Security
```

Part06 이후 연결:

```text
Part05 Unit Test
→ Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
```

---

### [FAQ]

Q. Part05의 최종 목적은 뭐야?
A. Frontend Agent가 validation, formatter, mapper 같은 작은 로직을 Unit Test로 안정적으로 검증하게 만드는 것이다.

Q. Unit Test에서 가장 중요한 기준은 뭐야?
A. 입력과 출력이 명확하고 외부 의존 없이 빠르게 검증 가능해야 한다.

Q. Part05 다음에는 어떤 내용이 이어져야 해?
A. Presentational Component와 Interactive Component를 검증하는 Component Test 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Unit Test는 뭐야?
A. validation, formatter, mapper처럼 입력과 출력이 명확한 작은 로직을 독립적으로 검증하는 테스트다.

Q. Frontend Unit Test는 언제 써?
A. 순수 함수, validation, formatter, mapper, filter, sorting, utility 검증에 사용한다.

Q. Unit Test는 React Component 테스트와 달라?
A. 다르다. Unit Test는 보통 React render 없이 순수 함수나 utility를 검증한다.

Q. Unit Test만 있으면 충분해?
A. 아니다. 사용자 UI 흐름은 Component Test와 Integration Test로 검증해야 한다.

Q. Pure Function은 뭐야?
A. 같은 입력이면 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Pure Function이 Unit Test에 좋은 이유는?
A. 외부 환경에 의존하지 않아 빠르고 안정적으로 검증할 수 있기 때문이다.

Q. Date나 Random이 들어간 함수는 어떻게 테스트해?
A. 현재 시간이나 랜덤 값을 함수 내부에서 직접 만들지 말고 인자로 주입하는 방식이 좋다.

Q. Pure Function Test 이름은 어떻게 써?
A. 어떤 입력 상황에서 어떤 결과를 반환하는지 드러나게 작성한다.

Q. Validation Function Test는 뭐야?
A. Form 입력값 검증 로직을 함수 단위로 분리해 검증하는 테스트다.

Q. Validation은 Component Test만 하면 안 돼?
A. 간단하면 가능하지만 검증 규칙이 복잡하면 Unit Test가 더 빠르고 명확하다.

Q. Required Validation에서 공백 문자열도 실패로 봐야 해?
A. 일반적으로 필수 텍스트 입력은 trim 후 빈 값이면 실패로 처리한다.

Q. 오류 메시지 문자열까지 테스트해야 해?
A. 사용자에게 중요한 메시지라면 가능하다. 문구 변경이 잦으면 error code 테스트를 고려한다.

Q. 이메일 정규식은 완벽해야 해?
A. 실무에서는 과도하게 복잡한 정규식보다 서비스 기준에 맞는 현실적인 검증을 사용한다.

Q. Format Validation은 Backend와 같아야 해?
A. 가능하면 동일한 기준을 유지해야 사용자 경험과 서버 오류를 줄일 수 있다.

Q. Range Validation에서 가장 중요한 테스트는 뭐야?
A. 최소값, 최대값, 최소값 바로 아래, 최대값 바로 위 같은 boundary value 테스트다.

Q. 날짜 range 테스트는 왜 조심해야 해?
A. timezone과 날짜 포맷 차이로 결과가 달라질 수 있기 때문이다.

Q. Formatter Test는 왜 필요해?
A. 사용자에게 표시되는 금액, 날짜, 상태 문구가 규칙대로 변환되는지 빠르게 검증할 수 있기 때문이다.

Q. toLocaleString은 테스트에서 조심해야 해?
A. locale을 명시하지 않으면 환경에 따라 결과가 달라질 수 있다.

Q. Date Formatter Test가 자주 깨지는 이유는?
A. timezone, locale, 현재 시간 의존 때문에 환경별 결과가 달라질 수 있기 때문이다.

Q. 현재 날짜 기준 함수는 어떻게 테스트해?
A. 현재 날짜를 함수 인자로 주입하거나 timer mock을 사용한다.

Q. Count Formatter는 왜 테스트해?
A. 0, 큰 수, 최대 표시값 같은 edge case가 UI에서 자주 문제 되기 때문이다.

Q. 99+ 같은 표시는 Unit Test가 적합해?
A. 적합하다. 입력과 출력이 명확한 formatter 로직이기 때문이다.

Q. Mapper Test는 뭐야?
A. API 응답, Form 값, 내부 상태 값을 다른 데이터 구조로 변환하는 로직을 검증하는 테스트다.

Q. Form 값을 Request DTO로 바꾸는 함수도 Unit Test 대상이야?
A. 그렇다. 입력과 출력이 명확하므로 Unit Test에 적합하다.

Q. Mapper Test에서 가장 중요한 건 뭐야?
A. field 이름, 타입 변환, optional/default 처리, Backend API shape와의 일치다.

Q. API Response Mapper는 왜 필요해?
A. Backend 응답 구조와 Frontend 화면 구조를 분리하고 변환 규칙을 명확히 하기 위해 필요하다.

Q. API response에 null이 올 수 있으면 테스트해야 해?
A. 해야 한다. null 처리 누락은 UI 오류로 이어지기 쉽다.

Q. Error Mapper Test는 왜 필요해?
A. API 실패 상황에서 사용자에게 일관되고 안전한 메시지를 표시하기 위해 필요하다.

Q. 500 에러 메시지는 어떻게 처리해야 해?
A. 서버 내부 상세를 노출하지 않고 일반적인 안내 메시지를 반환하는 것이 좋다.

Q. Filter Function은 Unit Test 대상이야?
A. 입력 배열과 조건에 따라 출력 배열이 명확하므로 Unit Test에 적합하다.

Q. 검색어 공백도 테스트해야 해?
A. 해야 한다. 공백 검색어 처리는 실제 검색 UI에서 자주 발생한다.

Q. Sorting Function도 Unit Test 대상이야?
A. 그렇다. 입력 목록과 기대 순서가 명확하므로 Unit Test에 적합하다.

Q. sort는 원본 배열을 바꿔?
A. JavaScript `sort`는 원본 배열을 변경한다. 테스트 대상 함수에서 복사 후 정렬하는 것이 안전하다.

Q. null 값 정렬은 테스트해야 해?
A. 해야 한다. null 처리 기준이 없으면 실제 목록 UI에서 오류나 예상치 못한 순서가 발생할 수 있다.

Q. Select Option Mapper는 왜 테스트해?
A. API 코드와 화면 select option의 label/value 매핑 오류를 빠르게 잡을 수 있기 때문이다.

Q. Unit Test 이름은 어떻게 작성해?
A. 입력 조건과 기대 결과가 드러나게 작성한다.

Q. 테스트 이름을 한글로 써도 돼?
A. 가능하다. 팀 컨벤션에 맞추되 의미가 명확해야 한다.

Q. Unit Test 파일은 어디에 둬?
A. 테스트 대상 함수 옆에 두거나 feature의 `__tests__` 폴더에 둘 수 있다.

Q. Arrange Act Assert 구조는 뭐야?
A. 입력 준비, 함수 실행, 결과 검증을 분리하는 테스트 구조다.

Q. Unit Test에서 실제 API를 호출해도 돼?
A. 안 된다. API 호출은 mock을 사용하거나 Integration Test에서 다룬다.

Q. Date.now를 직접 쓰는 함수는 어떻게 테스트해?
A. 날짜를 인자로 주입하거나 timer mock을 사용한다.

Q. 모든 utility 함수를 Unit Test해야 해?
A. 아니다. 도메인 규칙, 변환 로직, edge case가 있는 함수를 우선 테스트한다.

Q. Over Testing이 왜 문제야?
A. 작은 리팩토링에도 테스트 수정이 많아지고 유지보수 비용이 커진다.

Q. Unit Test에 실제 token을 넣어도 돼?
A. 안 된다. 테스트에는 더미 token을 사용하고 실제 secret은 절대 commit하지 않는다.

Q. Unit Test 작성 전 무엇을 확인해야 해?
A. 입력과 출력이 명확한지, 외부 의존 없이 테스트 가능한지 먼저 확인한다.

Q. Unit Test Checklist의 핵심은 뭐야?
A. 독립성, 명확한 입력/출력, edge case, 외부 의존 제거다.

Q. Part05 Unit Test의 최종 목표는 뭐야?
A. Frontend Agent가 validation, formatter, mapper 같은 작은 로직을 Unit Test로 안정적으로 검증하게 만드는 것이다.

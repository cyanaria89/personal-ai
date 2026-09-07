# JavaScript Foundation Part05 - Array and Object

---

# 1. Array

## 1.1 Array Concept

### [개념]

Array는 순서가 있는 여러 값을 저장하는 JavaScript Reference Type이다.

Frontend JavaScript에서는 API 응답 목록, 검색 결과, 리뷰 목록, 축제 목록, 렌더링 데이터 목록을 처리할 때 Array를 자주 사용한다.

예:

```javascript
const festivals = [
  { id: 1, title: "Spring Festival" },
  { id: 2, title: "Summer Festival" },
];
```

---

### [핵심]

- Array
- ordered list
- Reference Type
- list data
- API response list
- map
- filter
- find
- reduce
- sort
- slice
- splice
- includes
- some
- every
- Array.isArray
- React list rendering

---

### [실무]

2026 실무 기준에서 Frontend Agent는 Array를 단순 반복문보다 데이터 가공 단위로 이해해야 한다.

Array 실무 사용처:

- API Response 목록 처리
- 화면 카드 목록 생성
- 검색 결과 필터링
- 리뷰 목록 정렬
- 선택된 항목 찾기
- Pagination 목록 처리
- Empty State 판단
- React List Rendering 준비

예:

```javascript
const festivalCards = festivals.map((festival) => ({
  id: festival.id,
  title: festival.title,
  imageUrl: festival.imageUrl ?? "/default.png",
}));
```

주의:

- Array는 Reference Type이다.
- 배열 원본 변경 여부를 확인해야 한다.
- `sort`, `splice`, `push`, `pop`은 원본을 변경한다.
- `map`, `filter`, `slice`는 새 배열을 반환한다.
- API 응답 목록은 null 또는 undefined일 수 있다.
- 배열 여부 확인에는 `Array.isArray()`를 사용한다.

---

### [FAQ]

Q. Array가 뭐야?
A. 순서가 있는 여러 값을 저장하는 JavaScript Reference Type이다.

Q. Frontend에서 Array는 어디에 많이 쓰여?
A. API 응답 목록, 검색 결과, 리뷰 목록, 카드 렌더링 데이터 처리에 많이 사용된다.

Q. 배열 여부는 어떻게 확인해?
A. `Array.isArray()`로 확인하는 것이 좋다.

Q. Array가 Reference Type이라는 건 무슨 뜻이야?
A. 값 자체가 아니라 참조를 다루므로 원본 변경이 다른 코드에 영향을 줄 수 있다는 뜻이다.

---

# 2. Array Access and Length

## 2.1 Array Index and Length Rules

### [개념]

Array 요소는 index로 접근한다.

JavaScript Array index는 0부터 시작한다.

`length`는 배열 요소 개수를 반환한다.

예:

```javascript
const festivals = ["Spring", "Summer", "Winter"];

const firstFestival = festivals[0];
const festivalCount = festivals.length;
```

---

### [핵심]

- index
- zero based index
- length
- first element
- last element
- empty array
- out of range
- optional chaining
- default value

---

### [실무]

배열 접근 시 요소가 없을 가능성을 고려해야 한다.

첫 번째 요소 접근:

```javascript
const firstFestival = festivals[0] ?? null;
```

마지막 요소 접근:

```javascript
const lastFestival = festivals[festivals.length - 1] ?? null;
```

API 응답 첫 항목 안전 접근:

```javascript
const firstTitle = response?.data?.content?.[0]?.title ?? "제목 없음";
```

Empty State 판단:

```javascript
const isEmpty = festivals.length === 0;
```

주의:

- index는 0부터 시작한다.
- 존재하지 않는 index 접근 결과는 `undefined`다.
- 빈 배열에서 `[0]` 접근 시 `undefined`가 나온다.
- 배열이 아닌 값에 `length`를 사용하면 오류가 발생할 수 있다.
- API 응답 목록은 배열 검증 후 사용한다.

---

### [FAQ]

Q. JavaScript Array index는 몇부터 시작해?
A. 0부터 시작한다.

Q. 배열의 개수는 어떻게 확인해?
A. `length` property로 확인한다.

Q. 빈 배열에서 첫 번째 요소에 접근하면 뭐가 나와?
A. `undefined`가 나온다.

Q. API 응답 첫 항목에 안전하게 접근하려면 어떻게 해?
A. optional chaining을 사용해 `response?.data?.content?.[0]` 형태로 접근한다.

---

# 3. Array Mutation

## 3.1 Mutable Array Method Rules

### [개념]

Array Mutation은 배열 원본을 직접 변경하는 동작이다.

JavaScript Array에는 원본을 변경하는 Method와 원본을 유지하고 새 배열을 반환하는 Method가 있다.

원본 변경 Method 예:

- push
- pop
- shift
- unshift
- splice
- sort
- reverse

---

### [핵심]

- Array Mutation
- mutable method
- push
- pop
- shift
- unshift
- splice
- sort
- reverse
- original array change
- side effect
- immutable update

---

### [실무]

Frontend Agent는 배열 Method 사용 시 원본 변경 여부를 반드시 판단해야 한다.

원본 변경 예:

```javascript
const festivals = ["Spring", "Summer"];

festivals.push("Winter");
```

`sort` 원본 변경:

```javascript
festivals.sort((a, b) => a.title.localeCompare(b.title));
```

원본 변경을 피하는 정렬:

```javascript
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

주의:

- `sort`는 원본 배열을 변경한다.
- `splice`는 원본 배열을 변경한다.
- React State 배열은 직접 변경하면 안 된다.
- 원본 유지가 필요하면 spread 또는 slice로 복사 후 처리한다.
- Review Agent는 mutation method 사용 목적을 확인해야 한다.

---

### [FAQ]

Q. Array Mutation이 뭐야?
A. 배열 원본을 직접 변경하는 동작이다.

Q. sort는 원본 배열을 바꿔?
A. 바꾼다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

Q. splice는 원본 배열을 바꿔?
A. 바꾼다. 원본을 유지하려면 slice나 filter를 고려한다.

Q. React State 배열에 push를 써도 돼?
A. 직접 push로 변경하면 안 된다. 새 배열을 만들어 update해야 한다.

---

## 3.2 Immutable Array Update Rules

### [개념]

Immutable Array Update는 기존 배열을 직접 변경하지 않고 새 배열을 만들어 변경 결과를 표현하는 방식이다.

Frontend와 React에서는 Immutable Update가 중요하다.

예:

```javascript
const nextFestivals = [...festivals, newFestival];
```

---

### [핵심]

- Immutable Update
- new array
- spread syntax
- map update
- filter remove
- slice copy
- React State
- no direct mutation
- predictable update

---

### [실무]

추가:

```javascript
const nextFestivals = [...festivals, newFestival];
```

삭제:

```javascript
const nextFestivals = festivals.filter(
  (festival) => festival.id !== deletedFestivalId,
);
```

수정:

```javascript
const nextFestivals = festivals.map((festival) =>
  festival.id === updatedFestival.id ? updatedFestival : festival,
);
```

정렬:

```javascript
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

주의:

- spread는 얕은 복사다.
- 중첩 객체 내부는 같은 참조를 유지할 수 있다.
- 상태 업데이트 시 원본 변경 금지
- 변경 목적에 맞는 Array Method 선택
- Review Agent는 push, splice, sort 사용 시 원본 변경 위험을 검토해야 한다.

---

### [FAQ]

Q. Immutable Array Update가 뭐야?
A. 기존 배열을 직접 변경하지 않고 새 배열을 만들어 변경 결과를 표현하는 방식이다.

Q. 배열에 항목을 추가할 때 원본을 유지하려면 어떻게 해?
A. `[...items, newItem]`처럼 spread syntax로 새 배열을 만든다.

Q. 배열에서 항목을 삭제할 때는 무엇을 써?
A. `filter`를 사용해 삭제할 항목을 제외한 새 배열을 만든다.

Q. 배열 항목을 수정할 때는 무엇을 써?
A. `map`을 사용해 특정 조건의 항목만 새 값으로 교체한다.

---

# 4. map

## 4.1 map Rules

### [개념]

`map`은 배열의 각 요소를 변환해 새 배열을 반환하는 Array Method다.

원본 배열은 변경하지 않는다.

예:

```javascript
const titles = festivals.map((festival) => festival.title);
```

---

### [핵심]

- map
- array transformation
- new array
- callback return
- list mapping
- API response mapping
- React list rendering
- no original mutation

---

### [실무]

`map`은 API 응답 목록을 화면용 데이터로 변환할 때 자주 사용한다.

예:

```javascript
const festivalCards = festivals.map((festival) => ({
  id: festival.id,
  title: festival.title,
  region: festival.regionName ?? "지역 정보 없음",
  imageUrl: festival.imageUrl ?? "/default.png",
}));
```

React 렌더링 준비 데이터:

```javascript
const reviewItems = reviews.map((review) => ({
  id: review.id,
  writerName: review.writer?.name ?? "익명",
  content: review.content,
  rating: review.rating ?? 0,
}));
```

주의:

- `map` callback은 반드시 값을 return해야 한다.
- 중괄호 `{}`를 사용하면 명시적 return이 필요하다.
- 객체를 바로 반환할 때는 `({})` 형태를 사용한다.
- 단순 반복 실행만 필요하면 `forEach` 또는 `for...of`를 고려한다.
- 배열이 아닌 값에 map을 호출하면 오류가 발생한다.

나쁜 예:

```javascript
const titles = festivals.map((festival) => {
  festival.title;
});
```

좋은 예:

```javascript
const titles = festivals.map((festival) => festival.title);
```

---

### [FAQ]

Q. map은 언제 써?
A. 배열의 각 요소를 변환해 새 배열을 만들 때 사용한다.

Q. map은 원본 배열을 바꿔?
A. 아니다. 새 배열을 반환하고 원본은 유지한다.

Q. map callback에서 return을 빼먹으면 어떻게 돼?
A. 결과 배열에 undefined가 들어갈 수 있다.

Q. 객체를 map에서 바로 반환하려면 어떻게 해?
A. `festival => ({ id: festival.id })`처럼 객체를 괄호로 감싸서 반환한다.

---

# 5. filter

## 5.1 filter Rules

### [개념]

`filter`는 배열에서 조건에 맞는 요소만 모아 새 배열을 반환하는 Array Method다.

원본 배열은 변경하지 않는다.

예:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
```

---

### [핵심]

- filter
- condition
- boolean callback
- new array
- list filtering
- search result
- active item
- remove item
- no original mutation

---

### [실무]

`filter`는 검색 결과 필터링, 활성 데이터 추출, 삭제 처리에 자주 사용된다.

활성 축제 필터링:

```javascript
const activeFestivals = festivals.filter(
  (festival) => festival.status === "ACTIVE",
);
```

검색어 필터링:

```javascript
const filteredFestivals = festivals.filter((festival) =>
  festival.title.toLowerCase().includes(keyword.toLowerCase()),
);
```

삭제 처리:

```javascript
const nextReviews = reviews.filter((review) => review.id !== deletedReviewId);
```

주의:

- `filter` callback은 boolean을 반환해야 한다.
- 조건에 맞는 요소가 없으면 빈 배열을 반환한다.
- 하나의 요소만 찾을 때는 `find`가 더 적합하다.
- 원본 배열은 변경하지 않는다.
- 검색어 비교 시 대소문자와 공백 처리를 고려한다.

---

### [FAQ]

Q. filter는 언제 써?
A. 배열에서 조건에 맞는 요소만 모아 새 배열을 만들 때 사용한다.

Q. filter는 원본 배열을 바꿔?
A. 아니다. 조건에 맞는 요소를 담은 새 배열을 반환한다.

Q. filter 결과가 없으면 뭐가 나와?
A. 빈 배열이 반환된다.

Q. 하나의 요소만 찾을 때 filter를 써도 돼?
A. 가능하지만 첫 번째 요소 하나만 필요하면 `find`가 더 적합하다.

---

# 6. find

## 6.1 find Rules

### [개념]

`find`는 배열에서 조건에 맞는 첫 번째 요소를 반환하는 Array Method다.

조건에 맞는 요소가 없으면 `undefined`를 반환한다.

예:

```javascript
const selectedFestival = festivals.find(
  (festival) => festival.id === selectedFestivalId,
);
```

---

### [핵심]

- find
- first matched item
- undefined
- search item
- selected item
- id matching
- optional chaining
- default value
- single item lookup

---

### [실무]

`find`는 id 기반 상세 데이터 검색이나 선택 항목 조회에 적합하다.

예:

```javascript
const selectedFestival = festivals.find(
  (festival) => festival.id === selectedFestivalId,
);

const selectedTitle = selectedFestival?.title ?? "선택된 축제 없음";
```

권한 대상 조회:

```javascript
const myReview = reviews.find((review) => review.writerId === loginUserId);
```

주의:

- 결과가 없으면 `undefined`다.
- 결과 사용 시 optional chaining 또는 null check 필요
- 여러 개 결과가 필요하면 `filter` 사용
- id 타입이 string / number인지 확인
- URL parameter와 비교할 때 타입 변환 필요

예:

```javascript
const selectedId = Number(searchParams.get("festivalId"));
const selectedFestival = festivals.find(
  (festival) => festival.id === selectedId,
);
```

---

### [FAQ]

Q. find는 언제 써?
A. 배열에서 조건에 맞는 첫 번째 요소 하나를 찾을 때 사용한다.

Q. find 결과가 없으면 뭐가 나와?
A. `undefined`가 반환된다.

Q. find 결과를 바로 사용해도 돼?
A. 결과가 undefined일 수 있으므로 optional chaining이나 null check가 필요하다.

Q. filter와 find 차이는 뭐야?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고, find는 첫 번째 요소 하나를 반환한다.

---

# 7. reduce

## 7.1 reduce Rules

### [개념]

`reduce`는 배열의 요소를 누적해 하나의 값으로 만드는 Array Method다.

합계, 그룹화, 객체 변환, 카운트 계산에 사용할 수 있다.

예:

```javascript
const totalPrice = prices.reduce((sum, price) => sum + price, 0);
```

---

### [핵심]

- reduce
- accumulator
- current value
- initial value
- sum
- count
- grouping
- object mapping
- data aggregation
- single result

---

### [실무]

`reduce`는 단순 변환보다 누적 계산에 적합하다.

평점 합계:

```javascript
const totalRating = reviews.reduce((sum, review) => sum + review.rating, 0);
```

평균 평점:

```javascript
const averageRating =
  reviews.length === 0
    ? 0
    : reviews.reduce((sum, review) => sum + review.rating, 0) / reviews.length;
```

카테고리별 개수:

```javascript
const countByRegion = festivals.reduce((acc, festival) => {
  const region = festival.regionName ?? "기타";

  acc[region] = (acc[region] ?? 0) + 1;

  return acc;
}, {});
```

주의:

- initial value를 명시한다.
- 단순 변환은 `map`이 더 명확하다.
- 단순 필터링은 `filter`가 더 명확하다.
- reduce callback이 복잡하면 별도 함수로 분리한다.
- 빈 배열 reduce는 initial value가 없으면 오류가 날 수 있다.

---

### [FAQ]

Q. reduce는 언제 써?
A. 배열을 하나의 값으로 누적 계산할 때 사용한다.

Q. reduce의 initial value는 왜 필요해?
A. 빈 배열 처리와 반환 타입 예측을 위해 필요하다.

Q. 합계 계산에는 reduce를 써도 돼?
A. 적합하다. 숫자 합계, 평균, 카운트 계산에 사용할 수 있다.

Q. reduce가 너무 복잡하면 어떻게 해?
A. map, filter로 나누거나 callback 함수를 별도로 분리한다.

---

# 8. some and every

## 8.1 some Rules

### [개념]

`some`은 배열 요소 중 하나라도 조건을 만족하면 `true`를 반환하는 Array Method다.

조건을 만족하는 요소가 없으면 `false`를 반환한다.

예:

```javascript
const hasActiveFestival = festivals.some((festival) => festival.active);
```

---

### [핵심]

- some
- any match
- boolean result
- condition check
- existence check
- permission check
- validation
- list status

---

### [실무]

`some`은 목록 안에 특정 조건을 만족하는 요소가 있는지 확인할 때 사용한다.

즐겨찾기 여부:

```javascript
const isFavorite = favorites.some(
  (favorite) => favorite.festivalId === festivalId,
);
```

오류 여부:

```javascript
const hasError = formFields.some((field) => field.error);
```

주의:

- 결과는 boolean이다.
- 요소 자체가 필요하면 `find`를 사용한다.
- 여러 요소 목록이 필요하면 `filter`를 사용한다.
- 조건 이름을 의미 있게 작성한다.

---

### [FAQ]

Q. some은 언제 써?
A. 배열 요소 중 하나라도 조건을 만족하는지 확인할 때 사용한다.

Q. some은 무엇을 반환해?
A. true 또는 false를 반환한다.

Q. 요소 자체가 필요하면 some을 써도 돼?
A. 아니다. 요소 자체가 필요하면 find를 사용한다.

---

## 8.2 every Rules

### [개념]

`every`는 배열의 모든 요소가 조건을 만족하면 `true`를 반환하는 Array Method다.

하나라도 조건을 만족하지 않으면 `false`를 반환한다.

예:

```javascript
const allValid = formFields.every((field) => field.valid);
```

---

### [핵심]

- every
- all match
- boolean result
- validation
- all checked
- all active
- form validation
- list condition

---

### [실무]

`every`는 전체 입력값 검증이나 전체 선택 상태 판단에 유용하다.

Form Validation:

```javascript
const canSubmit = formFields.every((field) => field.value.trim().length > 0);
```

전체 선택 여부:

```javascript
const allSelected = items.every((item) => selectedIds.includes(item.id));
```

주의:

- 빈 배열에 `every`를 호출하면 true가 반환된다.
- 빈 배열 처리 조건이 별도로 필요한지 확인한다.
- 하나라도 만족하는지 확인하려면 `some`을 사용한다.
- 전체 유효성 검증에는 의미 있는 변수명 사용

예:

```javascript
const canSubmit =
  formFields.length > 0 &&
  formFields.every((field) => field.value.trim().length > 0);
```

---

### [FAQ]

Q. every는 언제 써?
A. 배열의 모든 요소가 조건을 만족하는지 확인할 때 사용한다.

Q. every는 무엇을 반환해?
A. true 또는 false를 반환한다.

Q. 빈 배열에서 every 결과는 뭐야?
A. true가 반환된다. 빈 배열을 별도로 처리해야 할 수 있다.

Q. some과 every 차이는 뭐야?
A. some은 하나라도 만족하면 true, every는 모두 만족해야 true다.

---

# 9. includes

## 9.1 includes Rules

### [개념]

`includes`는 배열이나 문자열에 특정 값이 포함되어 있는지 확인하는 Method다.

배열에서 사용하면 특정 요소 포함 여부를 boolean으로 반환한다.

예:

```javascript
const selectedIds = [1, 2, 3];

const isSelected = selectedIds.includes(2);
```

---

### [핵심]

- includes
- contains
- boolean result
- selected ids
- keyword search
- string includes
- array includes
- exact match
- case sensitivity

---

### [실무]

배열 `includes`는 선택 목록, 권한 목록, 카테고리 목록 확인에 사용한다.

선택 여부:

```javascript
const isSelected = selectedFestivalIds.includes(festival.id);
```

권한 확인:

```javascript
const canAccess = allowedRoles.includes(userRole);
```

문자열 검색:

```javascript
const matched = festival.title.toLowerCase().includes(keyword.toLowerCase());
```

주의:

- 배열 includes는 정확한 값 비교다.
- 객체 배열에서 특정 property 기준 검색은 `some` 또는 `find` 사용
- 문자열 includes는 대소문자를 구분한다.
- 검색어는 trim과 lowerCase 처리를 고려한다.
- id 타입이 string / number로 다르면 false가 될 수 있다.

---

### [FAQ]

Q. includes는 언제 써?
A. 배열이나 문자열에 특정 값이 포함되어 있는지 확인할 때 사용한다.

Q. includes는 무엇을 반환해?
A. true 또는 false를 반환한다.

Q. 객체 배열에서 id 포함 여부도 includes로 확인해?
A. 객체 property 기준이면 some이나 find를 사용하는 것이 좋다.

Q. 문자열 includes는 대소문자를 구분해?
A. 구분한다. 검색 시 toLowerCase를 함께 사용할 수 있다.

---

# 10. slice and splice

## 10.1 slice Rules

### [개념]

`slice`는 배열의 일부를 복사해 새 배열을 반환하는 Method다.

원본 배열은 변경하지 않는다.

예:

```javascript
const firstThree = festivals.slice(0, 3);
```

---

### [핵심]

- slice
- copy
- partial array
- start index
- end index
- no original mutation
- pagination
- shallow copy

---

### [실무]

`slice`는 목록 일부 표시, pagination, 원본 유지 복사에 사용한다.

상위 N개 추출:

```javascript
const topFestivals = festivals.slice(0, 5);
```

페이지 데이터 추출:

```javascript
const startIndex = (page - 1) * pageSize;
const endIndex = startIndex + pageSize;
const pageItems = festivals.slice(startIndex, endIndex);
```

얕은 복사:

```javascript
const copiedFestivals = festivals.slice();
```

주의:

- end index는 포함되지 않는다.
- 원본 배열을 변경하지 않는다.
- 반환 결과는 새 배열이다.
- 내부 객체는 같은 참조를 유지한다.
- 깊은 복사가 필요한 경우 별도 처리 필요

---

### [FAQ]

Q. slice는 언제 써?
A. 배열 일부를 복사하거나 원본을 유지한 채 새 배열을 만들 때 사용한다.

Q. slice는 원본 배열을 바꿔?
A. 아니다. 새 배열을 반환하고 원본은 유지한다.

Q. slice의 end index는 포함돼?
A. 포함되지 않는다.

Q. slice는 깊은 복사야?
A. 아니다. 배열은 새로 만들지만 내부 객체는 같은 참조를 유지한다.

---

## 10.2 splice Rules

### [개념]

`splice`는 배열의 요소를 추가, 삭제, 교체하는 Method다.

`splice`는 원본 배열을 직접 변경한다.

예:

```javascript
festivals.splice(1, 1);
```

---

### [핵심]

- splice
- original mutation
- remove item
- insert item
- replace item
- start index
- delete count
- mutation caution
- React state caution

---

### [실무]

`splice`는 원본 변경이 필요한 경우에만 사용한다.

요소 삭제:

```javascript
const removedItems = festivals.splice(1, 1);
```

하지만 Frontend State나 React 전환을 고려하면 `filter`가 더 안전하다.

권장:

```javascript
const nextFestivals = festivals.filter((festival) => festival.id !== targetId);
```

주의:

- `splice`는 원본 배열을 변경한다.
- React State 배열에 직접 사용하면 안 된다.
- 삭제 목적이면 `filter`를 먼저 고려한다.
- 일부 복사 목적이면 `slice`를 사용한다.
- Review Agent는 `splice` 사용 시 원본 변경 의도를 확인해야 한다.

---

### [FAQ]

Q. splice는 언제 써?
A. 배열 원본에서 요소를 추가, 삭제, 교체할 때 사용한다.

Q. splice는 원본 배열을 바꿔?
A. 바꾼다.

Q. slice와 splice 차이는 뭐야?
A. slice는 원본을 유지하고 새 배열을 반환하며, splice는 원본 배열을 변경한다.

Q. 삭제에는 splice보다 무엇이 좋아?
A. 원본 유지가 필요하면 filter를 사용하는 것이 좋다.

---

# 11. sort

## 11.1 sort Rules

### [개념]

`sort`는 배열 요소를 정렬하는 Method다.

`sort`는 원본 배열을 직접 변경한다.

예:

```javascript
festivals.sort((a, b) => a.title.localeCompare(b.title));
```

---

### [핵심]

- sort
- original mutation
- compare function
- ascending
- descending
- numeric sort
- string sort
- date sort
- localeCompare
- copy before sort

---

### [실무]

정렬은 원본 변경 여부를 반드시 확인해야 한다.

문자열 정렬:

```javascript
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

숫자 오름차순:

```javascript
const sortedReviews = [...reviews].sort((a, b) => a.rating - b.rating);
```

숫자 내림차순:

```javascript
const sortedReviews = [...reviews].sort((a, b) => b.rating - a.rating);
```

날짜 정렬:

```javascript
const sortedFestivals = [...festivals].sort(
  (a, b) => new Date(a.startDate) - new Date(b.startDate),
);
```

주의:

- `sort`는 원본 배열을 변경한다.
- 원본 유지가 필요하면 spread로 복사 후 sort한다.
- 숫자 정렬에는 compare function을 반드시 사용한다.
- 날짜 문자열은 Date 변환 또는 ISO 형식 확인 필요
- null 값 정렬 기준을 명확히 한다.

---

### [FAQ]

Q. sort는 언제 써?
A. 배열 요소를 정렬할 때 사용한다.

Q. sort는 원본 배열을 바꿔?
A. 바꾼다. 원본을 유지하려면 복사 후 sort해야 한다.

Q. 숫자 정렬에서 compare function이 필요한 이유는?
A. 기본 sort는 문자열 기준 정렬이므로 숫자 정렬 결과가 예상과 다를 수 있기 때문이다.

Q. 문자열 정렬에는 무엇을 써?
A. `localeCompare`를 사용할 수 있다.

---

# 12. Object

## 12.1 Object Concept

### [개념]

Object는 key-value 구조로 데이터를 저장하는 JavaScript Reference Type이다.

Frontend JavaScript에서는 사용자 정보, 축제 정보, 검색 조건, API 응답, UI 상태 객체를 표현할 때 사용한다.

예:

```javascript
const festival = {
  id: 1,
  title: "Spring Festival",
  region: "Seoul",
  active: true,
};
```

---

### [핵심]

- Object
- key-value
- property
- method
- Reference Type
- API response object
- UI state object
- nested object
- dot notation
- bracket notation
- Object.keys
- Object.values
- Object.entries
- object spread

---

### [실무]

API Response는 대부분 Object와 Array가 중첩된 형태다.

예:

```javascript
const response = {
  data: {
    content: [
      { id: 1, title: "Festival A" },
      { id: 2, title: "Festival B" },
    ],
    page: 1,
    totalCount: 2,
  },
};
```

안전한 접근:

```javascript
const festivals = response?.data?.content ?? [];
```

UI 상태 객체:

```javascript
const listState = {
  loading: false,
  error: null,
  items: [],
};
```

주의:

- Object는 Reference Type이다.
- 같은 객체 참조를 공유하면 한쪽 변경이 다른 곳에 영향을 줄 수 있다.
- 중첩 객체 접근 시 optional chaining을 사용한다.
- 객체 원본 변경 여부를 확인한다.
- API 원본 객체와 화면용 객체를 분리하는 것이 좋다.

---

### [FAQ]

Q. Object가 뭐야?
A. key-value 구조로 데이터를 저장하는 JavaScript Reference Type이다.

Q. Frontend에서 Object는 어디에 많이 쓰여?
A. API 응답, 사용자 정보, 검색 조건, UI 상태, 화면용 데이터 객체에 많이 사용된다.

Q. Object도 Reference Type이야?
A. 맞다. 객체 참조를 다루므로 원본 변경에 주의해야 한다.

Q. API 응답은 보통 어떤 구조야?
A. Object 안에 Array가 포함되거나 Object가 중첩된 구조가 많다.

---

# 13. Object Property Access

## 13.1 Dot Notation and Bracket Notation Rules

### [개념]

Object Property는 dot notation 또는 bracket notation으로 접근할 수 있다.

dot notation은 고정 property에 사용한다.

bracket notation은 동적 key에 사용한다.

예:

```javascript
const title = festival.title;
const value = festival["title"];
```

---

### [핵심]

- dot notation
- bracket notation
- property access
- dynamic key
- fixed key
- nested object
- optional chaining
- null guard

---

### [실무]

고정 property는 dot notation을 우선 사용한다.

```javascript
const title = festival.title;
const region = festival.regionName;
```

동적 key는 bracket notation을 사용한다.

```javascript
function getFieldValue(object, fieldName) {
  return object?.[fieldName];
}
```

중첩 객체 안전 접근:

```javascript
const writerName = review?.writer?.name ?? "익명";
```

주의:

- 존재하지 않는 property 접근 결과는 `undefined`다.
- 중첩 객체 접근 시 optional chaining 사용
- 동적 key는 오타와 타입에 주의
- 사용자 입력을 그대로 key로 사용할 때 검증 필요
- property 이름이 특수문자나 공백을 포함하면 bracket notation 필요

---

### [FAQ]

Q. dot notation과 bracket notation 차이는 뭐야?
A. dot notation은 고정 property 접근에 사용하고, bracket notation은 동적 key 접근에 사용한다.

Q. 존재하지 않는 property에 접근하면 뭐가 나와?
A. `undefined`가 나온다.

Q. 중첩 객체에 안전하게 접근하려면 어떻게 해?
A. optional chaining을 사용한다.

Q. 동적 property 접근은 언제 필요해?
A. field name이 변수로 전달되는 경우 bracket notation이 필요하다.

---

# 14. Object Method

## 14.1 Object Method Rules

### [개념]

Object Method는 Object property로 저장된 Function이다.

Method는 객체의 동작을 표현할 때 사용한다.

예:

```javascript
const user = {
  name: "jun",
  getName() {
    return this.name;
  },
};
```

---

### [핵심]

- Object Method
- method syntax
- this
- property function
- arrow function caution
- object behavior
- method call

---

### [실무]

Object Method에서 `this`가 필요하면 일반 method syntax를 사용한다.

권장:

```javascript
const user = {
  name: "jun",
  getName() {
    return this.name;
  },
};
```

비권장:

```javascript
const user = {
  name: "jun",
  getName: () => this.name,
};
```

주의:

- Arrow Function은 자체 `this`를 가지지 않는다.
- Object Method에서 `this`가 필요하면 Arrow Function을 피한다.
- 단순 데이터 객체에는 Method보다 별도 Function이 더 명확할 수 있다.
- API 응답 객체에 Method를 직접 추가하지 않는 것이 좋다.
- Review Agent는 Object Method 내부 `this` 사용을 검토해야 한다.

---

### [FAQ]

Q. Object Method가 뭐야?
A. Object property로 저장된 Function이다.

Q. Object Method에서 Arrow Function을 써도 돼?
A. this가 필요 없다면 가능하지만, this가 필요하면 일반 method syntax가 적합하다.

Q. Object Method에서 this는 무엇을 가리켜?
A. 일반 method syntax에서는 호출한 객체를 가리킨다.

Q. API 응답 객체에 Method를 추가해도 돼?
A. 가능하지만 원본 응답 객체를 변경할 수 있으므로 별도 Mapping을 권장한다.

---

# 15. Object.keys, Object.values, Object.entries

## 15.1 Object.keys Rules

### [개념]

`Object.keys()`는 객체의 key 목록을 배열로 반환한다.

예:

```javascript
const keys = Object.keys(searchCondition);
```

---

### [핵심]

- Object.keys
- key list
- object iteration
- dynamic fields
- validation
- query params
- filter condition

---

### [실무]

`Object.keys()`는 객체 필드 순회와 검증에 사용할 수 있다.

빈 검색 조건 제거:

```javascript
const activeKeys = Object.keys(searchCondition).filter(
  (key) => searchCondition[key] !== null && searchCondition[key] !== "",
);
```

주의:

- 반환값은 배열이다.
- key 순회 시 value 접근에는 bracket notation 사용
- 중첩 객체는 직접 펼쳐지지 않는다.
- 객체가 null 또는 undefined이면 오류가 발생한다.
- Object.keys 호출 전 객체 여부 확인이 필요할 수 있다.

---

### [FAQ]

Q. Object.keys는 언제 써?
A. 객체의 key 목록을 배열로 가져와 순회할 때 사용한다.

Q. Object.keys 결과는 뭐야?
A. key 문자열 배열이다.

Q. Object.keys에 null을 넣으면 어떻게 돼?
A. 오류가 발생한다.

---

## 15.2 Object.values Rules

### [개념]

`Object.values()`는 객체의 value 목록을 배열로 반환한다.

예:

```javascript
const values = Object.values(searchCondition);
```

---

### [핵심]

- Object.values
- value list
- object values
- validation
- form values
- empty check
- array result

---

### [실무]

`Object.values()`는 전체 value 검증에 사용할 수 있다.

Form 값 검증:

```javascript
const allFilled = Object.values(formValues).every(
  (value) => String(value).trim().length > 0,
);
```

검색 조건 존재 여부:

```javascript
const hasCondition = Object.values(searchCondition).some(
  (value) => value !== null && value !== "",
);
```

주의:

- 반환값은 배열이다.
- null 객체에는 사용할 수 없다.
- value 타입이 다양하면 검증 로직이 필요하다.
- number 0, boolean false가 유효한 값인지 확인해야 한다.

---

### [FAQ]

Q. Object.values는 언제 써?
A. 객체의 value 목록을 배열로 가져와 검증하거나 순회할 때 사용한다.

Q. Object.values 결과는 뭐야?
A. 객체 value들의 배열이다.

Q. Form Validation에 Object.values를 써도 돼?
A. 가능하다. 다만 0이나 false가 유효한 값인지 확인해야 한다.

---

## 15.3 Object.entries Rules

### [개념]

`Object.entries()`는 객체의 key-value 쌍을 배열로 반환한다.

각 요소는 `[key, value]` 형태다.

예:

```javascript
const entries = Object.entries(searchCondition);
```

---

### [핵심]

- Object.entries
- key value pair
- object iteration
- query string
- mapping
- filtering
- dynamic object processing

---

### [실무]

`Object.entries()`는 객체를 순회하며 key와 value를 함께 사용할 때 적합하다.

검색 조건을 query string으로 변환:

```javascript
function createQueryString(params) {
  return Object.entries(params)
    .filter(([, value]) => value !== null && value !== "")
    .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
    .join("&");
}
```

주의:

- 반환값은 `[key, value]` 배열 목록이다.
- value 검증 기준을 명확히 해야 한다.
- URL query 생성 시 `encodeURIComponent()` 사용
- null 객체에는 사용할 수 없다.
- 복잡한 변환은 별도 Function으로 분리한다.

---

### [FAQ]

Q. Object.entries는 언제 써?
A. 객체의 key와 value를 함께 순회할 때 사용한다.

Q. Object.entries 결과는 어떤 형태야?
A. `[key, value]` 쌍을 담은 배열이다.

Q. query string 만들 때 Object.entries를 써도 돼?
A. 적합하다. key와 value를 함께 처리할 수 있기 때문이다.

---

# 16. Destructuring

## 16.1 Object Destructuring Rules

### [개념]

Object Destructuring은 객체에서 필요한 property를 간결하게 꺼내는 문법이다.

예:

```javascript
const festival = {
  id: 1,
  title: "Spring Festival",
  region: "Seoul",
};

const { id, title } = festival;
```

---

### [핵심]

- Object Destructuring
- property extraction
- default value
- alias
- function parameter destructuring
- API response
- readability

---

### [실무]

Object Destructuring은 API 응답 객체나 Function Parameter에서 자주 사용된다.

기본값:

```javascript
const { title = "제목 없음", imageUrl = "/default.png" } = festival;
```

alias:

```javascript
const { title: festivalTitle } = festival;
```

Function Parameter:

```javascript
function toFestivalCard({ id, title, imageUrl }) {
  return {
    id,
    title,
    imageUrl: imageUrl ?? "/default.png",
  };
}
```

주의:

- destructuring 대상이 null 또는 undefined이면 오류 발생
- 안전한 기본값을 사용한다.
- 너무 많은 property를 한 번에 꺼내면 가독성이 떨어진다.
- 중첩 destructuring은 복잡하면 피한다.
- API 응답 구조가 불안정하면 optional chaining을 먼저 고려한다.

안전한 예:

```javascript
function toFestivalCard(festival = {}) {
  const { id, title = "제목 없음" } = festival;

  return { id, title };
}
```

---

### [FAQ]

Q. Object Destructuring은 뭐야?
A. 객체에서 필요한 property를 간결하게 꺼내는 문법이다.

Q. Destructuring에 기본값을 줄 수 있어?
A. 가능하다. `const { title = "제목 없음" } = festival;`처럼 작성한다.

Q. null에서 Destructuring하면 어떻게 돼?
A. 오류가 발생한다. 기본값이나 null check가 필요하다.

Q. Function Parameter에도 Destructuring을 쓸 수 있어?
A. 가능하다. 객체 parameter에서 필요한 값을 바로 꺼낼 수 있다.

---

## 16.2 Array Destructuring Rules

### [개념]

Array Destructuring은 배열에서 위치 기준으로 값을 꺼내는 문법이다.

예:

```javascript
const colors = ["red", "blue"];

const [primaryColor, secondaryColor] = colors;
```

---

### [핵심]

- Array Destructuring
- position based extraction
- first item
- second item
- default value
- skip item
- React Hook readiness
- tuple pattern

---

### [실무]

Array Destructuring은 고정 위치 값이나 tuple 형태 데이터에 사용한다.

첫 번째 요소:

```javascript
const [firstFestival] = festivals;
```

기본값:

```javascript
const [firstFestival = null] = festivals;
```

값 건너뛰기:

```javascript
const [, secondFestival] = festivals;
```

React Hook 학습 전 준비:

```javascript
const [value, setValue] = statePair;
```

주의:

- 배열 위치에 의존한다.
- 목록 데이터 전체 처리에는 map / filter가 더 적합하다.
- 값이 없으면 undefined가 될 수 있다.
- 기본값을 지정할 수 있다.
- 의미가 불명확하면 변수명을 명확히 작성한다.

---

### [FAQ]

Q. Array Destructuring은 뭐야?
A. 배열에서 위치 기준으로 값을 꺼내는 문법이다.

Q. 첫 번째 요소만 꺼내려면 어떻게 해?
A. `const [firstItem] = items;`처럼 작성한다.

Q. Array Destructuring은 React와 관련 있어?
A. 관련 있다. React Hook의 `[state, setState]` 패턴 이해에 필요하다.

Q. 배열 값이 없으면 어떻게 돼?
A. undefined가 될 수 있으므로 기본값을 지정할 수 있다.

---

# 17. Spread and Rest

## 17.1 Object Spread Rules

### [개념]

Object Spread는 객체 property를 펼쳐 새 객체를 만드는 문법이다.

객체 복사, 병합, 일부 property 수정에 사용한다.

예:

```javascript
const updatedUser = {
  ...user,
  name: "newName",
};
```

---

### [핵심]

- Object Spread
- object copy
- object merge
- update property
- shallow copy
- immutable update
- React state
- original object preservation

---

### [실무]

Object Spread는 API 응답 객체를 화면용 객체로 변환하거나 상태 객체를 갱신할 때 사용한다.

객체 수정:

```javascript
const updatedFestival = {
  ...festival,
  isFavorite: true,
};
```

기본값 병합:

```javascript
const normalizedFestival = {
  imageUrl: "/default.png",
  regionName: "지역 정보 없음",
  ...festival,
};
```

주의:

- Spread는 얕은 복사다.
- 중첩 객체는 내부 참조가 공유된다.
- 뒤에 오는 property가 앞의 property를 덮어쓴다.
- 원본 객체 변경 여부를 확인한다.
- API 원본 응답을 직접 변경하지 않는 것이 좋다.

---

### [FAQ]

Q. Object Spread는 뭐야?
A. 객체 property를 펼쳐 새 객체를 만드는 문법이다.

Q. Object Spread는 깊은 복사야?
A. 아니다. 기본적으로 얕은 복사다.

Q. Spread에서 같은 property가 있으면 어떻게 돼?
A. 뒤에 작성된 property가 앞의 값을 덮어쓴다.

Q. React State 객체 수정에 Spread를 써도 돼?
A. 적합하다. 기존 객체를 직접 변경하지 않고 새 객체를 만들 수 있다.

---

## 17.2 Array Spread Rules

### [개념]

Array Spread는 배열 요소를 펼쳐 새 배열을 만드는 문법이다.

배열 복사, 병합, 항목 추가에 사용한다.

예:

```javascript
const nextFestivals = [...festivals, newFestival];
```

---

### [핵심]

- Array Spread
- array copy
- array merge
- add item
- shallow copy
- immutable update
- React state
- original array preservation

---

### [실무]

Array Spread는 원본 배열을 유지하고 새 배열을 만들 때 사용한다.

배열 복사:

```javascript
const copiedFestivals = [...festivals];
```

배열 병합:

```javascript
const allFestivals = [...domesticFestivals, ...globalFestivals];
```

항목 추가:

```javascript
const nextReviews = [...reviews, newReview];
```

정렬 전 복사:

```javascript
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

주의:

- Array Spread도 얕은 복사다.
- 내부 객체는 같은 참조를 유지한다.
- 중첩 데이터 수정은 추가 복사가 필요할 수 있다.
- 큰 배열을 자주 복사하면 성능 고려 필요
- 원본 변경 Method와 함께 사용할 때 의도를 명확히 한다.

---

### [FAQ]

Q. Array Spread는 뭐야?
A. 배열 요소를 펼쳐 새 배열을 만드는 문법이다.

Q. Array Spread는 깊은 복사야?
A. 아니다. 배열은 새로 만들지만 내부 객체는 같은 참조를 유지한다.

Q. 배열을 병합하려면 어떻게 해?
A. `[...arrayA, ...arrayB]`처럼 작성한다.

Q. sort 전에 Spread를 쓰는 이유는?
A. sort가 원본 배열을 변경하므로 복사본을 정렬하기 위해서다.

---

## 17.3 Rest Parameter Rules

### [개념]

Rest Parameter는 여러 Argument를 배열로 모아 받는 문법이다.

Function Parameter에서 `...`를 사용한다.

예:

```javascript
function sum(...numbers) {
  return numbers.reduce((total, number) => total + number, 0);
}
```

---

### [핵심]

- Rest Parameter
- collect arguments
- array
- function parameter
- variable arguments
- reduce
- utility function
- spread difference

---

### [실무]

Rest Parameter는 인자 개수가 유동적인 유틸 함수에 적합하다.

예:

```javascript
function mergeClassNames(...classNames) {
  return classNames.filter(Boolean).join(" ");
}
```

사용:

```javascript
const className = mergeClassNames("button", isActive && "active");
```

주의:

- Rest Parameter는 Function Parameter에서 사용한다.
- Spread Syntax는 값을 펼칠 때 사용한다.
- Rest Parameter는 항상 배열로 수집한다.
- Rest Parameter는 일반적으로 마지막 parameter로 사용한다.
- 너무 많은 유동 인자는 API 명확성을 떨어뜨릴 수 있다.

---

### [FAQ]

Q. Rest Parameter가 뭐야?
A. 여러 Argument를 배열로 모아 받는 Function Parameter 문법이다.

Q. Rest Parameter와 Spread 차이는 뭐야?
A. Rest는 여러 값을 모으고, Spread는 배열이나 객체를 펼친다.

Q. Rest Parameter는 어디에 써?
A. 인자 개수가 유동적인 유틸 함수에 사용한다.

---

# 18. Shallow Copy and Deep Copy

## 18.1 Shallow Copy Rules

### [개념]

Shallow Copy는 최상위 구조만 복사하고 중첩 객체는 같은 참조를 공유하는 복사 방식이다.

Spread, slice, Object.assign은 기본적으로 Shallow Copy다.

예:

```javascript
const copiedFestival = {
  ...festival,
};
```

---

### [핵심]

- Shallow Copy
- shallow clone
- shared nested reference
- spread
- slice
- Object.assign
- nested object caution
- mutation risk

---

### [실무]

Shallow Copy는 단순 객체나 배열 복사에 적합하다.

하지만 중첩 객체 수정에는 주의해야 한다.

예:

```javascript
const copiedFestival = {
  ...festival,
};

copiedFestival.region.name = "Busan";
```

위 코드는 `festival.region`도 영향을 받을 수 있다.

중첩 객체 안전 수정:

```javascript
const updatedFestival = {
  ...festival,
  region: {
    ...festival.region,
    name: "Busan",
  },
};
```

주의:

- Spread는 깊은 복사가 아니다.
- 중첩 객체 수정 시 각 단계 복사 필요
- API 응답 원본 변경 금지
- React State 중첩 객체 수정 시 주의
- Review Agent는 nested object mutation을 검토해야 한다.

---

### [FAQ]

Q. Shallow Copy가 뭐야?
A. 최상위 구조만 복사하고 중첩 객체는 같은 참조를 공유하는 복사 방식이다.

Q. Spread는 Shallow Copy야?
A. 맞다. Object Spread와 Array Spread는 기본적으로 얕은 복사다.

Q. 중첩 객체를 수정하려면 어떻게 해?
A. 수정하려는 중첩 단계마다 새 객체를 만들어야 한다.

---

## 18.2 Deep Copy Rules

### [개념]

Deep Copy는 중첩 객체까지 모두 새 참조로 복사하는 방식이다.

JavaScript에서 Deep Copy는 상황에 따라 별도 방식이 필요하다.

---

### [핵심]

- Deep Copy
- nested object copy
- structuredClone
- JSON stringify parse caution
- Date caution
- function caution
- clone strategy
- immutable nested update

---

### [실무]

단순 데이터는 `structuredClone`을 사용할 수 있다.

```javascript
const copiedData = structuredClone(originalData);
```

주의:

- `structuredClone`은 환경 지원 여부 확인 필요
- 함수, DOM Node 등 복사 제한이 있을 수 있음
- `JSON.parse(JSON.stringify())`는 Date, undefined, function 손실 가능
- Deep Copy가 항상 정답은 아님
- 필요한 경로만 복사하는 Immutable Update가 더 적합할 수 있음

중첩 상태 일부 수정:

```javascript
const updatedUser = {
  ...user,
  profile: {
    ...user.profile,
    nickname: "newNickname",
  },
};
```

Review Agent는 Deep Copy가 필요한 상황인지, 얕은 복사로 충분한지 판단해야 한다.

---

### [FAQ]

Q. Deep Copy가 뭐야?
A. 중첩 객체까지 모두 새 참조로 복사하는 방식이다.

Q. structuredClone은 언제 써?
A. 중첩 데이터 전체 복사가 필요하고 환경에서 지원될 때 사용할 수 있다.

Q. JSON.parse(JSON.stringify())로 Deep Copy해도 돼?
A. 가능하지만 Date, undefined, function 같은 값이 손실될 수 있어 주의해야 한다.

Q. Deep Copy가 항상 좋아?
A. 아니다. 필요한 부분만 복사하는 Immutable Update가 더 명확하고 효율적일 수 있다.

---

# 19. API Response Processing with Array and Object

## 19.1 API Response List Processing

### [개념]

API Response Processing은 서버 응답 데이터를 화면에서 사용하기 좋은 Array와 Object 구조로 변환하는 과정이다.

Frontend Agent는 API 원본 구조와 UI 데이터 구조를 분리해야 한다.

---

### [핵심]

- API Response
- response data
- content
- pagination
- array validation
- object mapping
- null handling
- default value
- normalize function
- UI data

---

### [실무]

API 응답 예:

```javascript
const response = {
  data: {
    content: [
      {
        id: 1,
        title: "Spring Festival",
        imageUrl: null,
        regionName: "Seoul",
      },
    ],
  },
};
```

정규화 함수:

```javascript
function normalizeFestivalList(response) {
  const content = response?.data?.content;

  if (!Array.isArray(content)) {
    return [];
  }

  return content.map((festival) => ({
    id: festival.id,
    title: festival.title ?? "제목 없음",
    imageUrl: festival.imageUrl ?? "/default.png",
    regionName: festival.regionName ?? "지역 정보 없음",
  }));
}
```

주의:

- 응답 구조 변경 가능성 고려
- `content`가 배열인지 확인
- null / undefined 기본값 처리
- UI용 필드명 통일
- API 원본 객체 직접 변경 금지
- Mapping Function은 Pure Function으로 작성

---

### [FAQ]

Q. API Response Processing이 뭐야?
A. 서버 응답 데이터를 화면에서 사용하기 좋은 구조로 변환하는 과정이다.

Q. API 응답 목록은 바로 map 해도 돼?
A. 응답 구조가 확실하지 않다면 Array.isArray로 확인 후 map 하는 것이 안전하다.

Q. normalize 함수는 왜 필요해?
A. API 원본 구조와 UI 데이터 구조를 분리해 유지보수성을 높이기 위해 필요하다.

Q. API 응답의 null 값은 어떻게 처리해?
A. nullish coalescing으로 기본값을 지정한다.

---

# 20. Array and Object Comparison

## 20.1 Required Comparisons

### [개념]

Array와 Object 문서에서는 헷갈리는 Method와 문법을 비교해 Retrieval 정확도를 높여야 한다.

비교 표는 Agent가 코드 생성 시 적절한 Method를 선택하도록 돕는다.

---

### [핵심]

필수 비교 대상:

- map vs forEach
- filter vs find
- some vs every
- slice vs splice
- spread vs rest
- shallow copy vs deep copy
- dot notation vs bracket notation
- Object.keys vs Object.values vs Object.entries
- mutable update vs immutable update

---

### [실무]

map vs forEach:

| 비교      | map                | forEach                     |
| --------- | ------------------ | --------------------------- |
| 목적      | 새 배열 생성       | 반복 실행                   |
| 반환값    | 새 배열            | undefined                   |
| 적합      | 데이터 변환        | 로그, DOM 처리, side effect |
| 원본 변경 | 보통 변경하지 않음 | callback 내용에 따라 가능   |

filter vs find:

| 비교      | filter                | find                |
| --------- | --------------------- | ------------------- |
| 목적      | 조건에 맞는 모든 요소 | 조건에 맞는 첫 요소 |
| 반환값    | 배열                  | 요소 또는 undefined |
| 결과 없음 | 빈 배열               | undefined           |
| 적합      | 목록 필터링           | 단일 항목 조회      |

slice vs splice:

| 비교        | slice     | splice             |
| ----------- | --------- | ------------------ |
| 목적        | 일부 복사 | 추가 / 삭제 / 교체 |
| 원본 변경   | 안 함     | 함                 |
| 반환값      | 새 배열   | 제거된 요소 배열   |
| React State | 안전      | 직접 사용 주의     |

---

### [FAQ]

Q. map과 forEach 차이는 뭐야?
A. map은 새 배열을 반환하고 forEach는 반복 실행만 하며 반환값은 undefined다.

Q. filter와 find 차이는 뭐야?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. slice와 splice 차이는 뭐야?
A. slice는 원본을 유지하고 일부를 반환하며 splice는 원본 배열을 변경한다.

Q. Spread와 Rest 차이는 뭐야?
A. Spread는 값을 펼치고 Rest는 여러 값을 하나로 모은다.

---

# 21. Array and Object Common Mistakes

## 21.1 Common Mistakes

### [개념]

Array와 Object 실수는 API 응답 처리 오류, 화면 렌더링 오류, React State 변경 오류로 이어질 수 있다.

Review Agent는 원본 변경, null 방어, Method 선택, 복사 방식, 응답 구조 처리를 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 배열이 아닌 값에 map 호출
- map callback return 누락
- forEach 결과를 새 배열로 착각
- filter와 find 혼동
- sort 원본 변경 인지 못함
- splice 원본 변경 인지 못함
- push로 원본 배열 직접 변경
- slice와 splice 혼동
- object spread를 deep copy로 오해
- 중첩 객체 얕은 복사 후 내부 변경
- API 원본 객체 직접 변경
- 존재하지 않는 property 직접 접근
- null 객체 destructuring
- Object.keys에 null 전달
- includes로 객체 배열 property 검색 시도
- `||`로 0, false, 빈 문자열 덮어쓰기

---

### [실무]

Review Flow:

```text
Array Object Review
→ API Response Shape Check
→ Array.isArray Check
→ map / filter / find Selection Check
→ Callback Return Check
→ Original Mutation Check
→ Immutable Update Check
→ Object Property Access Check
→ Destructuring Safety Check
→ Shallow Copy Risk Check
→ Default Value Check
```

나쁜 예:

```javascript
const titles = response.data.content.map((festival) => {
  festival.title;
});

response.data.content.sort((a, b) => a.title.localeCompare(b.title));
```

개선 예:

```javascript
const content = response?.data?.content;
const festivals = Array.isArray(content) ? content : [];

const titles = festivals.map((festival) => festival.title);

const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

주의:

- API 응답 목록은 배열 검증 후 처리
- callback return 확인
- 원본 변경 Method 사용 시 복사 우선 고려
- 중첩 객체는 단계별 복사 필요
- UI용 데이터는 Mapping Function으로 분리

---

### [FAQ]

Q. Array에서 가장 흔한 실수는 뭐야?
A. 배열이 아닌 값에 map 호출, map return 누락, sort 원본 변경, forEach 반환값 오해다.

Q. Object에서 가장 흔한 실수는 뭐야?
A. null 객체 접근, 중첩 객체 얕은 복사 후 내부 변경, 존재하지 않는 property 직접 접근이다.

Q. Review Agent는 Array와 Object에서 무엇을 우선 검토해야 해?
A. 배열 검증, Method 선택, 원본 변경 여부, null 방어, 복사 방식, API 응답 Mapping을 우선 검토해야 한다.

Q. API 응답 객체를 직접 수정해도 돼?
A. 지양한다. 원본 응답과 UI용 데이터를 분리하는 것이 좋다.

---

# 22. Array and Object Checklist

## 22.1 Document Quality Checklist

### [개념]

Array and Object 문서는 Frontend Agent가 API 응답 목록과 화면용 객체를 안전하게 처리하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Array 개념이 포함되었는가?
- [ ] Array index와 length 설명이 포함되었는가?
- [ ] Mutable Array Method 설명이 포함되었는가?
- [ ] Immutable Array Update 기준이 포함되었는가?
- [ ] map 설명과 return 주의가 포함되었는가?
- [ ] filter 설명이 포함되었는가?
- [ ] find 설명과 undefined 처리 기준이 포함되었는가?
- [ ] reduce 설명과 initial value 기준이 포함되었는가?
- [ ] some / every 설명이 포함되었는가?
- [ ] includes 설명이 포함되었는가?
- [ ] slice / splice 차이가 포함되었는가?
- [ ] sort 원본 변경 주의가 포함되었는가?
- [ ] Object 개념이 포함되었는가?
- [ ] dot notation / bracket notation 설명이 포함되었는가?
- [ ] Object Method와 this 주의가 포함되었는가?
- [ ] Object.keys / values / entries 설명이 포함되었는가?
- [ ] Object / Array Destructuring 설명이 포함되었는가?
- [ ] Spread / Rest 설명이 포함되었는가?
- [ ] Shallow Copy / Deep Copy 설명이 포함되었는가?
- [ ] API Response Processing 예제가 포함되었는가?
- [ ] Comparison 표가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?

---

### [실무]

검수 Flow:

```text
Draft
→ MASTER_RAG_RULES Section Check
→ JavaScript Domain Scope Check
→ Array Method Rule Check
→ Object Access Rule Check
→ Mutation Risk Check
→ API Response Mapping Check
→ Comparison Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part04_Function_Scope_Closure
→ JavaScript_Foundation_Part05_Array_Object
→ JavaScript_Foundation_Part06_DOM_Event_Form
```

---

### [FAQ]

Q. Array and Object 문서 검수에서 가장 중요한 것은 뭐야?
A. Array Method 선택, 원본 변경 여부, Object 접근 안정성, Shallow Copy 위험, API Response Mapping 기준이다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React 목록 렌더링, State 배열 업데이트, Props 객체 전달, API 응답 가공의 기반이 된다.

Q. 다음 Part와 어떻게 연결돼?
A. Part05는 데이터 처리 기준을 만들고, Part06은 DOM, Event, Form Handling으로 화면 동작을 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Array가 뭐야?
A. 순서가 있는 여러 값을 저장하는 JavaScript Reference Type이다.

Q. Frontend에서 Array는 어디에 많이 쓰여?
A. API 응답 목록, 검색 결과, 리뷰 목록, 카드 렌더링 데이터 처리에 많이 사용된다.

Q. 배열 여부는 어떻게 확인해?
A. Array.isArray()로 확인하는 것이 좋다.

Q. JavaScript Array index는 몇부터 시작해?
A. 0부터 시작한다.

Q. 배열의 개수는 어떻게 확인해?
A. length property로 확인한다.

Q. 빈 배열에서 첫 번째 요소에 접근하면 뭐가 나와?
A. undefined가 나온다.

Q. Array Mutation이 뭐야?
A. 배열 원본을 직접 변경하는 동작이다.

Q. 원본 배열을 변경하는 Method는 뭐가 있어?
A. push, pop, shift, unshift, splice, sort, reverse가 있다.

Q. sort는 원본 배열을 바꿔?
A. 바꾼다. 원본을 유지하려면 복사 후 sort해야 한다.

Q. splice는 원본 배열을 바꿔?
A. 바꾼다.

Q. Immutable Array Update가 뭐야?
A. 기존 배열을 직접 변경하지 않고 새 배열을 만들어 변경 결과를 표현하는 방식이다.

Q. 배열에 항목을 추가할 때 원본을 유지하려면 어떻게 해?
A. `[...items, newItem]`처럼 spread syntax로 새 배열을 만든다.

Q. 배열에서 항목을 삭제할 때는 무엇을 써?
A. filter를 사용해 삭제할 항목을 제외한 새 배열을 만든다.

Q. 배열 항목을 수정할 때는 무엇을 써?
A. map을 사용해 특정 조건의 항목만 새 값으로 교체한다.

Q. map은 언제 써?
A. 배열의 각 요소를 변환해 새 배열을 만들 때 사용한다.

Q. map은 원본 배열을 바꿔?
A. 아니다. 새 배열을 반환하고 원본은 유지한다.

Q. map callback에서 return을 빼먹으면 어떻게 돼?
A. 결과 배열에 undefined가 들어갈 수 있다.

Q. filter는 언제 써?
A. 배열에서 조건에 맞는 요소만 모아 새 배열을 만들 때 사용한다.

Q. filter 결과가 없으면 뭐가 나와?
A. 빈 배열이 반환된다.

Q. find는 언제 써?
A. 배열에서 조건에 맞는 첫 번째 요소 하나를 찾을 때 사용한다.

Q. find 결과가 없으면 뭐가 나와?
A. undefined가 반환된다.

Q. filter와 find 차이는 뭐야?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. reduce는 언제 써?
A. 배열을 하나의 값으로 누적 계산할 때 사용한다.

Q. reduce의 initial value는 왜 필요해?
A. 빈 배열 처리와 반환 타입 예측을 위해 필요하다.

Q. some은 언제 써?
A. 배열 요소 중 하나라도 조건을 만족하는지 확인할 때 사용한다.

Q. every는 언제 써?
A. 배열의 모든 요소가 조건을 만족하는지 확인할 때 사용한다.

Q. some과 every 차이는 뭐야?
A. some은 하나라도 만족하면 true, every는 모두 만족해야 true다.

Q. 빈 배열에서 every 결과는 뭐야?
A. true가 반환된다. 빈 배열을 별도로 처리해야 할 수 있다.

Q. includes는 언제 써?
A. 배열이나 문자열에 특정 값이 포함되어 있는지 확인할 때 사용한다.

Q. 객체 배열에서 id 포함 여부도 includes로 확인해?
A. 객체 property 기준이면 some이나 find를 사용하는 것이 좋다.

Q. slice는 언제 써?
A. 배열 일부를 복사하거나 원본을 유지한 채 새 배열을 만들 때 사용한다.

Q. slice는 원본 배열을 바꿔?
A. 아니다. 새 배열을 반환하고 원본은 유지한다.

Q. slice와 splice 차이는 뭐야?
A. slice는 원본을 유지하고 일부를 반환하며 splice는 원본 배열을 변경한다.

Q. JavaScript Object가 뭐야?
A. key-value 구조로 데이터를 저장하는 JavaScript Reference Type이다.

Q. Frontend에서 Object는 어디에 많이 쓰여?
A. API 응답, 사용자 정보, 검색 조건, UI 상태, 화면용 데이터 객체에 많이 사용된다.

Q. Object도 Reference Type이야?
A. 맞다. 객체 참조를 다루므로 원본 변경에 주의해야 한다.

Q. dot notation과 bracket notation 차이는 뭐야?
A. dot notation은 고정 property 접근에 사용하고, bracket notation은 동적 key 접근에 사용한다.

Q. 존재하지 않는 property에 접근하면 뭐가 나와?
A. undefined가 나온다.

Q. 중첩 객체에 안전하게 접근하려면 어떻게 해?
A. optional chaining을 사용한다.

Q. Object Method가 뭐야?
A. Object property로 저장된 Function이다.

Q. Object Method에서 Arrow Function을 써도 돼?
A. this가 필요 없다면 가능하지만, this가 필요하면 일반 method syntax가 적합하다.

Q. Object.keys는 언제 써?
A. 객체의 key 목록을 배열로 가져와 순회할 때 사용한다.

Q. Object.values는 언제 써?
A. 객체의 value 목록을 배열로 가져와 검증하거나 순회할 때 사용한다.

Q. Object.entries는 언제 써?
A. 객체의 key와 value를 함께 순회할 때 사용한다.

Q. Object Destructuring은 뭐야?
A. 객체에서 필요한 property를 간결하게 꺼내는 문법이다.

Q. Array Destructuring은 뭐야?
A. 배열에서 위치 기준으로 값을 꺼내는 문법이다.

Q. Destructuring에 기본값을 줄 수 있어?
A. 가능하다.

Q. null에서 Destructuring하면 어떻게 돼?
A. 오류가 발생한다. 기본값이나 null check가 필요하다.

Q. Object Spread는 뭐야?
A. 객체 property를 펼쳐 새 객체를 만드는 문법이다.

Q. Array Spread는 뭐야?
A. 배열 요소를 펼쳐 새 배열을 만드는 문법이다.

Q. Rest Parameter가 뭐야?
A. 여러 Argument를 배열로 모아 받는 Function Parameter 문법이다.

Q. Spread와 Rest 차이는 뭐야?
A. Spread는 값을 펼치고 Rest는 여러 값을 하나로 모은다.

Q. Shallow Copy가 뭐야?
A. 최상위 구조만 복사하고 중첩 객체는 같은 참조를 공유하는 복사 방식이다.

Q. Spread는 Shallow Copy야?
A. 맞다. Object Spread와 Array Spread는 기본적으로 얕은 복사다.

Q. Deep Copy가 뭐야?
A. 중첩 객체까지 모두 새 참조로 복사하는 방식이다.

Q. structuredClone은 언제 써?
A. 중첩 데이터 전체 복사가 필요하고 환경에서 지원될 때 사용할 수 있다.

Q. API Response Processing이 뭐야?
A. 서버 응답 데이터를 화면에서 사용하기 좋은 구조로 변환하는 과정이다.

Q. API 응답 목록은 바로 map 해도 돼?
A. 응답 구조가 확실하지 않다면 Array.isArray로 확인 후 map 하는 것이 안전하다.

Q. normalize 함수는 왜 필요해?
A. API 원본 구조와 UI 데이터 구조를 분리해 유지보수성을 높이기 위해 필요하다.

Q. Array에서 가장 흔한 실수는 뭐야?
A. 배열이 아닌 값에 map 호출, map return 누락, sort 원본 변경, forEach 반환값 오해다.

Q. Object에서 가장 흔한 실수는 뭐야?
A. null 객체 접근, 중첩 객체 얕은 복사 후 내부 변경, 존재하지 않는 property 직접 접근이다.

Q. Review Agent는 Array와 Object에서 무엇을 우선 검토해야 해?
A. 배열 검증, Method 선택, 원본 변경 여부, null 방어, 복사 방식, API 응답 Mapping을 우선 검토해야 한다.

Q. JavaScript Foundation Part05 다음에는 무엇을 다뤄야 해?
A. DOM, Event, Form Handling을 다루는 Part06으로 이어지는 것이 좋다.

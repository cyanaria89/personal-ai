# Frontend Accessibility Part06 - Image Icon Color Visual Accessibility

---

# 1. Image Accessibility

## 1.1 Image Alt Text Purpose

### [개념]

Image Accessibility는 이미지가 전달하는 정보, 기능, 장식 여부를 판단하고 적절한 text alternative를 제공하는 기준이다.

`alt` text는 이미지를 시각적으로 자세히 묘사하는 것이 아니라 이미지의 목적과 의미를 텍스트로 전달하는 것이다.

이미지가 정보 전달, 링크 이동, 버튼 기능, 상태 표현, 차트 설명 역할을 한다면 보조기술 사용자도 같은 의미를 이해할 수 있어야 한다.

---

### [핵심]

Image Accessibility 핵심 요소:

- `alt`
- empty alt `alt=""`
- informative image
- decorative image
- functional image
- linked image
- complex image
- chart description
- avatar image
- thumbnail image
- background image
- icon image
- duplicate content
- accessible name

Image 판단 기준:

1. 이미지가 정보를 전달하는가?
2. 이미지가 기능을 수행하는가?
3. 이미지가 링크 안에 있는가?
4. 이미지가 주변 텍스트와 중복되는가?
5. 이미지가 단순 장식인가?
6. 이미지가 복잡한 데이터나 차트인가?

---

### [실무]

Image alt 판단 Flow:

```text
Image 확인
→ 정보 전달 여부 확인
→ 기능 / 링크 여부 확인
→ 주변 텍스트 중복 여부 확인
→ 장식 여부 확인
→ alt 작성 또는 empty alt 처리
→ 복잡한 이미지면 별도 설명 제공
```

실무 기준:

- 정보 이미지는 의미 있는 `alt` 제공
- 장식 이미지는 `alt=""` 제공
- 링크 이미지의 `alt`는 이동 목적 중심
- 버튼 이미지의 `alt`는 기능 목적 중심
- 주변 텍스트와 완전 중복이면 장식 처리 검토
- 차트 / 그래프는 `alt`만으로 부족할 수 있으므로 별도 설명 제공
- “이미지”, “사진” 같은 불필요한 단어 지양
- 민감정보를 `alt`에 과도하게 포함하지 않음

---

### [FAQ]

Q. Image Accessibility는 왜 필요해?
A. 이미지를 볼 수 없는 사용자도 이미지의 정보, 기능, 목적을 이해할 수 있어야 하기 때문이다.

Q. alt text는 이미지를 자세히 묘사하면 돼?
A. 아니다. 이미지의 목적과 의미를 전달하는 것이 중요하다.

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 필요하다. 정보 이미지는 의미 있는 alt, 장식 이미지는 alt=""를 사용한다.

Q. alt에 “이미지”나 “사진”을 넣어야 해?
A. 보통 넣지 않는다. 스크린 리더가 이미 이미지임을 전달할 수 있다.

---

# 2. Image Type Rules

## 2.1 Informative Image

### [개념]

Informative Image는 사용자에게 의미 있는 정보를 전달하는 이미지다.

이미지 자체가 콘텐츠 이해에 필요하다면 `alt`를 통해 핵심 의미를 제공해야 한다.

---

### [핵심]

Informative Image 대상:

- 행사장 사진
- 프로필 사진
- 상품 이미지
- 축제 대표 이미지
- 상태를 전달하는 이미지
- 설명용 스크린샷
- 위치나 장소를 보여주는 이미지
- 콘텐츠 이해에 필요한 썸네일

Alt 작성 기준:

- 이미지의 목적 중심
- 문맥에 맞는 설명
- 짧고 명확함
- 주변 텍스트와 중복 최소화
- 파일명 사용 금지

---

### [실무]

축제 대표 이미지:

```jsx
<img src="/festival-spring.jpg" alt="봄꽃 축제 행사장 전경" />
```

장소 이미지:

```jsx
<img src="/seoul-plaza.jpg" alt="서울광장 야외 공연 무대" />
```

프로필 이미지:

```jsx
<img src={user.profileImageUrl} alt={`${user.nickname} 프로필 이미지`} />
```

실무 기준:

- 이미지가 콘텐츠 이해에 필요하면 alt 제공
- alt는 문맥에 따라 다르게 작성
- 같은 이미지라도 카드, 상세, 링크에서 목적이 다를 수 있음
- 주변 제목이 동일 정보를 제공하면 중복 여부 검토
- AI 생성 이미지나 외부 API 이미지도 alt 기준 동일 적용

---

### [FAQ]

Q. 정보 이미지는 어떻게 alt를 써?
A. 이미지가 전달하는 핵심 의미를 짧고 명확하게 작성한다.

Q. 축제 대표 이미지 alt는 어떻게 써?
A. 이미지가 정보 전달 역할이면 축제명이나 행사장 의미를 포함한다.

Q. 프로필 이미지는 alt를 어떻게 써?
A. 사용자를 식별하는 목적이면 “닉네임 프로필 이미지”처럼 작성할 수 있다.

Q. 파일명을 alt로 써도 돼?
A. 안 된다. 파일명은 사용자에게 의미 있는 대체 텍스트가 아니다.

---

## 2.2 Decorative Image

### [개념]

Decorative Image는 콘텐츠 의미 전달 없이 시각적 장식만 담당하는 이미지다.

장식 이미지는 스크린 리더가 읽지 않도록 empty alt `alt=""`를 제공한다.

---

### [핵심]

Decorative Image 대상:

- 배경 장식
- 구분선 이미지
- 장식 패턴
- 의미 없는 일러스트
- 텍스트 옆 장식 아이콘
- 카드 제목과 완전히 중복되는 썸네일
- skeleton decoration
- visual effect image

처리 기준:

- `alt=""`
- CSS background image 검토
- `aria-hidden="true"` 고려
- 불필요한 설명 금지
- 중요한 이미지 장식 처리 금지

---

### [실무]

장식 이미지:

```jsx
<img src="/decoration.png" alt="" />
```

카드 제목과 중복되는 이미지:

```jsx
<article>
  <img src="/festival.jpg" alt="" />
  <h3>봄꽃 축제</h3>
  <p>서울에서 열리는 봄꽃 축제입니다.</p>
</article>
```

CSS 배경 이미지:

```css
.hero {
  background-image: url("/decorative-pattern.png");
}
```

실무 기준:

- 장식 이미지는 `alt=""`
- 의미 있는 이미지를 장식 처리하지 않음
- 주변 텍스트와 완전 중복이면 empty alt 검토
- CSS background는 보조기술에 일반적으로 전달되지 않으므로 정보 이미지에 사용 주의
- 장식 여부는 디자인 기준이 아니라 정보 전달 여부로 판단

---

### [FAQ]

Q. 장식 이미지는 alt를 비워도 돼?
A. 그렇다. 장식 이미지는 alt=""로 스크린 리더가 건너뛰게 하는 것이 적합하다.

Q. 모든 이미지에 자세한 설명을 넣는 게 더 좋아?
A. 아니다. 장식 이미지를 읽게 하면 오히려 불필요한 정보가 늘어난다.

Q. 카드 이미지가 제목과 완전히 중복되면?
A. 카드 제목이 충분히 정보를 제공한다면 이미지 alt=""를 검토할 수 있다.

Q. CSS background image는 접근성에 안전해?
A. 장식이면 괜찮지만 정보 전달 이미지라면 대체 텍스트를 별도로 제공해야 한다.

---

## 2.3 Functional Image

### [개념]

Functional Image는 이미지 자체가 버튼, 링크, 제어 요소의 기능을 전달하는 이미지다.

Functional Image의 대체 텍스트는 이미지 묘사가 아니라 기능이나 목적을 설명해야 한다.

---

### [핵심]

Functional Image 대상:

- 이미지 링크
- 이미지 버튼
- 아이콘 버튼
- 로고 홈 링크
- 지도 확대 / 축소 버튼
- carousel control
- 파일 업로드 이미지 버튼

Alt 작성 기준:

- 기능 중심
- 이동 목적 중심
- 버튼 목적 중심
- 이미지 외형 묘사 지양
- 주변 accessible name과 중복 주의

---

### [실무]

링크 이미지:

```jsx
<Link to="/festivals/1">
  <img src="/festival.jpg" alt="봄꽃 축제 상세 보기" />
</Link>
```

로고 홈 링크:

```jsx
<Link to="/">
  <img src="/logo.svg" alt="FestaPick 홈" />
</Link>
```

이미지 버튼보다 button + label 권장:

```jsx
<button type="button" aria-label="지도 확대">
  <ZoomInIcon aria-hidden="true" />
</button>
```

나쁜 예:

```jsx
<Link to="/">
  <img src="/logo.svg" alt="로고 이미지" />
</Link>
```

실무 기준:

- 링크 안 이미지 alt는 링크 목적을 설명
- 버튼 안 아이콘은 icon이 아니라 button에 accessible name 제공
- 로고가 홈 링크라면 “서비스명 홈”처럼 목적 제공
- functional image에 `alt=""` 사용 금지
- 이미지 설명보다 사용자가 수행할 동작 중심으로 작성

---

### [FAQ]

Q. 링크 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크의 이동 목적을 전달하는 alt를 제공한다.

Q. 로고가 홈으로 이동하면 alt는 뭐가 좋아?
A. “서비스명 홈”처럼 링크 목적을 포함하는 것이 좋다.

Q. 버튼 안 아이콘에는 alt를 써야 해?
A. SVG 아이콘이면 보통 aria-hidden 처리하고 button에 aria-label을 제공한다.

Q. Functional Image alt에 외형 설명을 쓰면 안 돼?
A. 기능을 이해해야 하므로 외형보다 동작 목적을 설명해야 한다.

---

## 2.4 Complex Image and Chart

### [개념]

Complex Image는 `alt` 한 줄만으로 의미를 충분히 전달하기 어려운 이미지다.

차트, 그래프, 지도, 인포그래픽, 복잡한 스크린샷은 별도 설명, 데이터 테이블, 요약 텍스트가 필요할 수 있다.

---

### [핵심]

Complex Image 대상:

- chart
- graph
- map
- infographic
- architecture diagram
- flow diagram
- data visualization
- complex screenshot

제공 방식:

- 짧은 `alt`
- 인접한 설명
- 데이터 테이블
- 요약 문단
- 다운로드 가능한 원본 데이터
- `aria-describedby`

---

### [실무]

차트 예:

```jsx
<img
  src="/monthly-sales-chart.png"
  alt="월별 매출 추이 그래프"
  aria-describedby="monthly-sales-description"
/>

<p id="monthly-sales-description">
  2026년 1월부터 6월까지 매출은 전반적으로 증가했으며,
  6월에 가장 높은 매출을 기록했습니다.
</p>
```

차트 데이터 테이블:

```jsx
<table>
  <caption>월별 매출 데이터</caption>
  <thead>
    <tr>
      <th scope="col">월</th>
      <th scope="col">매출</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">2026년 1월</th>
      <td>120,000원</td>
    </tr>
  </tbody>
</table>
```

실무 기준:

- 복잡한 이미지는 alt만으로 끝내지 않음
- 핵심 insight를 텍스트로 제공
- 데이터 차트는 table 제공 검토
- 지도 이미지는 위치 / 목적 설명 제공
- architecture diagram은 주요 흐름을 텍스트로 제공
- 스크린샷은 사용자에게 필요한 정보 중심으로 설명

---

### [FAQ]

Q. 차트 이미지는 alt만 쓰면 충분해?
A. 대체로 부족하다. 핵심 요약이나 데이터 테이블을 함께 제공하는 것이 좋다.

Q. 복잡한 이미지는 어떻게 설명해?
A. 짧은 alt와 함께 인접한 설명, 표, 요약 텍스트를 제공한다.

Q. 지도 이미지는 alt를 어떻게 써?
A. 장소나 이동 목적, 핵심 위치 정보를 전달해야 한다.

Q. architecture diagram도 접근성 설명이 필요해?
A. 필요하다. 주요 구성 요소와 흐름을 텍스트로 제공하는 것이 좋다.

---

# 3. Icon Accessibility

## 3.1 Icon Purpose

### [개념]

Icon Accessibility는 아이콘이 장식인지, 정보인지, 기능인지에 따라 보조기술 전달 방식을 결정하는 기준이다.

아이콘은 시각적으로 의미를 전달하지만 스크린 리더에는 불필요하게 읽히거나 이름 없이 노출될 수 있다.

---

### [핵심]

Icon 유형:

- decorative icon
- informative icon
- functional icon
- icon button
- status icon
- loading icon
- social icon
- navigation icon

판단 기준:

1. 텍스트 옆 장식인가?
2. 아이콘만으로 기능을 수행하는가?
3. 상태를 전달하는가?
4. 색상과 함께 의미를 전달하는가?
5. loading 상태를 나타내는가?

---

### [실무]

Icon 처리 Flow:

```text
Icon 확인
→ 장식인지 확인
→ 기능인지 확인
→ 상태 전달인지 확인
→ accessible name 필요 여부 판단
→ aria-hidden / aria-label / visible text 적용
```

실무 기준:

- 텍스트 옆 장식 아이콘은 `aria-hidden`
- 아이콘만 있는 버튼은 button에 `aria-label`
- 상태 아이콘은 텍스트 또는 accessible name 함께 제공
- 로딩 아이콘은 loading text 함께 제공
- 색상 아이콘만으로 의미 전달 금지
- SVG title 중복 노출 주의
- icon library 사용 시 기본 aria 처리 확인

---

### [FAQ]

Q. Icon Accessibility는 왜 필요해?
A. 아이콘이 기능이나 상태를 전달할 때 보조기술 사용자도 그 의미를 이해해야 하기 때문이다.

Q. 아이콘에 항상 aria-label을 붙여야 해?
A. 아니다. 장식 아이콘은 aria-hidden이 적합하고 기능 아이콘은 부모 control에 이름을 제공한다.

Q. 아이콘만 있는 버튼은 어떻게 해야 해?
A. button에 aria-label을 제공하고 내부 icon은 aria-hidden 처리한다.

Q. 텍스트 옆 아이콘은 어떻게 처리해?
A. 텍스트가 의미를 이미 전달한다면 아이콘은 aria-hidden으로 장식 처리할 수 있다.

---

## 3.2 Decorative Icon

### [개념]

Decorative Icon은 이미 텍스트가 의미를 전달하고 있고 시각적 장식만 담당하는 아이콘이다.

장식 아이콘은 보조기술이 읽지 않도록 `aria-hidden="true"`를 사용한다.

---

### [핵심]

Decorative Icon 대상:

- 버튼 텍스트 옆 아이콘
- 링크 텍스트 옆 아이콘
- 제목 옆 장식 아이콘
- 입력창 앞 검색 아이콘
- 리스트 bullet 대체 아이콘
- 시각적 강조 아이콘

처리 기준:

- `aria-hidden="true"`
- focus 불가
- accessible name에 포함하지 않음
- 중요한 정보는 텍스트로 제공

---

### [실무]

텍스트 버튼 아이콘:

```jsx
<button type="button">
  <PlusIcon aria-hidden="true" />
  추가
</button>
```

검색 input 장식 아이콘:

```jsx
<div className="search-field">
  <SearchIcon aria-hidden="true" />
  <label htmlFor="keyword">검색어</label>
  <input id="keyword" name="keyword" type="search" />
</div>
```

링크 장식 아이콘:

```jsx
<Link to="/festivals">
  축제 목록
  <ArrowIcon aria-hidden="true" />
</Link>
```

실무 기준:

- 텍스트가 의미를 전달하면 아이콘은 장식 처리
- icon 자체에 focus가 가지 않도록 함
- icon에 불필요한 title이 노출되지 않게 확인
- icon이 없어도 기능 이해가 가능해야 함
- 색상이나 아이콘만으로 상태 전달 금지

---

### [FAQ]

Q. 텍스트가 있는 버튼의 아이콘도 읽혀야 해?
A. 보통 필요 없다. 텍스트가 의미를 전달하므로 아이콘은 aria-hidden 처리한다.

Q. 검색 input 앞 돋보기 아이콘은 어떻게 해?
A. label이 따로 있다면 돋보기 아이콘은 장식으로 보고 aria-hidden 처리할 수 있다.

Q. 장식 아이콘에 title을 넣어도 돼?
A. 불필요한 중복 정보가 될 수 있으므로 지양한다.

Q. 아이콘이 없어도 의미가 통해야 해?
A. 그렇다. 중요한 의미는 텍스트나 accessible name으로 제공해야 한다.

---

## 3.3 Icon Button

### [개념]

Icon Button은 시각적 텍스트 없이 아이콘만으로 기능을 나타내는 버튼이다.

Icon Button은 반드시 accessible name이 필요하다.

보통 button에 `aria-label`을 제공하고 내부 icon은 `aria-hidden="true"` 처리한다.

---

### [핵심]

Icon Button 대상:

- 닫기 버튼
- 검색 버튼
- 알림 열기
- 메뉴 열기
- 좋아요
- 공유
- 삭제
- 수정
- 지도 확대 / 축소
- 이전 / 다음

필수 기준:

- `button`
- `type="button"`
- `aria-label`
- icon `aria-hidden`
- focus visible
- disabled / pressed state 고려
- loading state 고려

---

### [실무]

닫기 버튼:

```jsx
<button type="button" aria-label="닫기" onClick={onClose}>
  <CloseIcon aria-hidden="true" />
</button>
```

검색 버튼:

```jsx
<button type="submit" aria-label="축제 검색">
  <SearchIcon aria-hidden="true" />
</button>
```

알림 버튼:

```jsx
<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

좋아요 토글:

```jsx
<button
  type="button"
  aria-label={liked ? "좋아요 취소" : "좋아요"}
  aria-pressed={liked}
  onClick={toggleLike}
>
  <HeartIcon aria-hidden="true" />
</button>
```

실무 기준:

- icon button에는 accessible name 필수
- label은 기능 중심으로 작성
- toggle button은 `aria-pressed` 고려
- icon 자체는 장식 처리
- 같은 icon button이 반복되면 대상 이름 포함
- button focus visible 확인
- button type 명시

---

### [FAQ]

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. 아이콘 버튼에는 aria-label을 어디에 붙여?
A. 아이콘이 아니라 button 요소에 붙이는 것이 적합하다.

Q. 좋아요 버튼은 aria-label이 어떻게 바뀌어야 해?
A. 상태에 따라 “좋아요” 또는 “좋아요 취소”처럼 실제 동작을 설명할 수 있다.

Q. icon button 내부 SVG는 어떻게 처리해?
A. 보통 aria-hidden="true"로 장식 처리한다.

---

## 3.4 Status Icon

### [개념]

Status Icon은 성공, 오류, 경고, 진행 중, 선택됨 같은 상태를 시각적으로 전달하는 아이콘이다.

상태 아이콘은 색상이나 모양만으로 의미를 전달하면 안 되고 텍스트 또는 accessible name으로 상태를 함께 제공해야 한다.

---

### [핵심]

Status Icon 대상:

- success icon
- error icon
- warning icon
- info icon
- selected icon
- favorite icon
- required icon
- validation icon
- loading icon

처리 기준:

- 텍스트와 함께 제공
- icon은 장식 처리 가능
- 상태 이름 제공
- 색상만으로 전달 금지
- live region과 연결 가능

---

### [실무]

성공 상태:

```jsx
<p>
  <CheckIcon aria-hidden="true" />
  저장되었습니다.
</p>
```

오류 상태:

```jsx
<p role="alert">
  <ErrorIcon aria-hidden="true" />
  이메일을 입력해 주세요.
</p>
```

아이콘만 표시해야 하는 경우:

```jsx
<span aria-label="성공">
  <CheckIcon aria-hidden="true" />
</span>
```

선택 상태:

```jsx
<span>
  <CheckIcon aria-hidden="true" />
  선택됨
</span>
```

실무 기준:

- 상태는 텍스트로 함께 제공
- icon은 보통 `aria-hidden`
- 색상만으로 성공 / 오류 / 경고 전달 금지
- 오류 상태는 `role="alert"` 또는 field error 연결 고려
- 성공 / 저장 완료는 `role="status"` 고려
- 반복 상태 아이콘은 문맥을 명확히 제공

---

### [FAQ]

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?
A. 색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

Q. 오류 아이콘만 표시하면 충분해?
A. 아니다. 오류 메시지 텍스트와 수정 방법을 함께 제공해야 한다.

Q. 상태 아이콘은 aria-hidden 처리해도 돼?
A. 텍스트가 상태를 전달한다면 아이콘은 장식 처리해도 된다.

Q. 상태를 색상과 아이콘으로만 표시해도 돼?
A. 권장하지 않는다. 텍스트나 aria 상태를 함께 제공해야 한다.

---

# 4. Color Accessibility

## 4.1 Color Contrast

### [개념]

Color Contrast는 텍스트와 배경, UI 요소와 주변 영역 사이의 명도 차이가 충분한지 판단하는 기준이다.

색상 대비가 낮으면 저시력 사용자, 밝은 환경 사용자, 다크모드 사용자, 색각 이상 사용자가 콘텐츠를 읽기 어렵다.

---

### [핵심]

검토 대상:

- body text
- heading text
- button text
- link text
- placeholder
- disabled text
- error text
- helper text
- badge text
- focus outline
- icon color
- chart label
- toast text
- modal text

대비 확인 환경:

- light mode
- dark mode
- hover state
- focus state
- disabled state
- error state
- selected state
- high contrast environment

---

### [실무]

실무 검토 Flow:

```text
Text / UI 색상 확인
→ 배경색 확인
→ contrast tool로 측정
→ normal / hover / focus / disabled 상태 확인
→ dark mode 확인
→ token 수정 또는 색상 변경
```

주의 예:

```css
.helper-text {
  color: #b8b8b8;
}
```

개선 기준:

```text
중요한 안내 텍스트는 충분한 대비 확보
placeholder를 중요한 정보 전달에 사용하지 않음
disabled text도 완전히 읽을 수 없게 만들지 않음
focus ring도 배경과 구분되게 제공
```

실무 기준:

- 디자인 감각만으로 색상 대비를 판단하지 않음
- 도구로 실제 contrast 확인
- 다크모드와 라이트모드 모두 확인
- placeholder 대비가 낮을 수 있으므로 중요한 정보 금지
- disabled 상태도 의미가 필요한 경우 읽을 수 있어야 함
- focus ring contrast 확인
- 에러 색상은 텍스트 / 아이콘과 함께 제공

---

### [FAQ]

Q. Color Contrast는 왜 중요해?
A. 텍스트와 UI 요소가 배경과 충분히 구분되어야 사용자가 읽고 조작할 수 있기 때문이다.

Q. 회색 글씨가 예쁘면 그냥 써도 돼?
A. 텍스트 대비가 낮으면 읽기 어려울 수 있다. 도구로 확인하는 것이 좋다.

Q. 다크모드에서도 색상 대비를 따로 봐야 해?
A. 그렇다. 라이트모드에서 괜찮은 색상이 다크모드에서는 부족할 수 있다.

Q. focus outline도 대비가 필요해?
A. 필요하다. keyboard 사용자가 현재 위치를 명확히 볼 수 있어야 한다.

---

## 4.2 Color Only Meaning

### [개념]

Color Only Meaning은 색상만으로 상태나 의미를 전달하는 문제를 말한다.

색상을 구분하기 어려운 사용자는 오류, 성공, 선택, 활성 상태, 위험 상태를 인식하지 못할 수 있다.

---

### [핵심]

Color Only 문제 예:

- 빨간색만으로 error 표시
- 초록색만으로 success 표시
- 색상만 다른 chart line
- 필수값을 색상만으로 표시
- 활성 tab을 색상만으로 표시
- 현재 메뉴를 색상만으로 표시
- disabled 상태를 색상만으로 표시
- 좋아요 상태를 색상만으로 표시
- 캘린더 이벤트 종류를 색상만으로 구분

개선 방식:

- 색상 + 텍스트
- 색상 + 아이콘
- 색상 + 패턴
- 색상 + 형태
- 색상 + underline
- 색상 + `aria-current`
- 색상 + `aria-selected`
- 색상 + `aria-invalid`

---

### [실무]

오류 개선:

```jsx
<p id="email-error" role="alert">
  오류: 이메일을 입력해 주세요.
</p>
```

활성 메뉴 개선:

```jsx
<NavLink to="/calendar" aria-current={isActive ? "page" : undefined}>
  캘린더
</NavLink>
```

Tab 선택 개선:

```jsx
<button type="button" role="tab" aria-selected={selectedTab === "review"}>
  리뷰
</button>
```

차트 개선 기준:

```text
색상만 다른 선 그래프
→ legend 제공
→ 선 모양 / label 추가
→ 데이터 테이블 제공
```

실무 기준:

- 상태는 텍스트로도 전달
- 오류는 `aria-invalid`와 error message 연결
- 현재 위치는 `aria-current`
- 선택 상태는 `aria-selected`
- chart는 legend와 label 제공
- 필수값은 별표만이 아니라 설명 또는 “필수” 텍스트 제공
- 성공 / 실패 toast는 문구 제공

---

### [FAQ]

Q. 색상만으로 에러 표시해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘, aria 속성을 함께 제공해야 한다.

Q. 빨간색이면 에러라는 걸 알 수 있지 않아?
A. 모든 사용자가 색상을 동일하게 인식하지 않는다. 텍스트나 아이콘을 함께 제공해야 한다.

Q. 활성 메뉴를 색상만 다르게 해도 돼?
A. 권장하지 않는다. aria-current, 밑줄, 굵기, 텍스트 등 추가 단서를 제공하는 것이 좋다.

Q. 차트 선 색상만 다르면 충분해?
A. 아니다. legend, label, 선 모양, 데이터 테이블 같은 추가 단서가 필요할 수 있다.

---

## 4.3 Link Color and Underline

### [개념]

Link는 사용자가 클릭하거나 이동할 수 있는 텍스트다.

Link가 일반 텍스트와 색상만으로 구분되면 일부 사용자가 링크를 인식하기 어렵다.

---

### [핵심]

Link 시각 기준:

- 충분한 색상 대비
- 일반 텍스트와 구분
- underline 고려
- hover style
- focus visible
- visited state 선택
- active state
- aria-current for current link

주의:

- 색상만으로 링크 구분 지양
- hover에서만 underline 표시 지양
- focus style 누락 금지
- 버튼처럼 보이는 링크와 실제 역할 일치 필요

---

### [실무]

기본 link style 예:

```css
a {
  text-decoration: underline;
}

a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

현재 link:

```jsx
<NavLink to="/festivals" aria-current={isActive ? "page" : undefined}>
  축제
</NavLink>
```

실무 기준:

- 본문 링크는 underline 제공 권장
- 색상만으로 일반 텍스트와 구분하지 않음
- focus style은 hover와 별도로 제공
- navigation current state는 시각 표시와 `aria-current` 함께 제공
- 링크처럼 보이지만 action이면 button 사용
- 버튼처럼 스타일링한 link도 이동 목적이면 link 유지 가능

---

### [FAQ]

Q. 링크는 색상만 다르면 충분해?
A. 권장하지 않는다. 밑줄이나 형태 같은 추가 단서가 있으면 더 명확하다.

Q. hover 때만 밑줄이 생기면 괜찮아?
A. 기본 상태에서 링크인지 알기 어려울 수 있다. 본문 링크는 기본 밑줄을 고려한다.

Q. 현재 페이지 링크는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. 링크처럼 보이는 버튼은 괜찮아?
A. 역할이 이동이면 Link, 액션이면 button을 사용해야 한다.

---

# 5. Visual State Accessibility

## 5.1 Focus Visual State

### [개념]

Focus Visual State는 keyboard focus가 현재 어디에 있는지 시각적으로 보여주는 상태다.

시각적 focus가 없으면 keyboard 사용자는 UI를 탐색하거나 조작할 수 없다.

---

### [핵심]

Focus Visual 기준:

- focus ring
- outline
- outline-offset
- sufficient contrast
- not clipped
- not removed
- visible in dark mode
- visible in light mode
- distinct from hover
- applied to all interactive elements

---

### [실무]

나쁜 예:

```css
button:focus {
  outline: none;
}
```

개선:

```css
button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

Card Link focus:

```css
.card-link:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 4px;
}
```

실무 기준:

- `outline: none` 사용 시 대체 focus style 필수
- 모든 interactive element에 focus 확인
- overflow hidden으로 focus ring이 잘리지 않게 함
- focus와 hover를 구분
- focus style은 디자인 시스템 token으로 관리 가능
- dark mode / light mode 모두 확인

---

### [FAQ]

Q. focus outline을 없애도 돼?
A. 대체 focus style 없이 제거하면 안 된다.

Q. focus style은 hover style과 같아도 돼?
A. 구분되는 것이 좋다. keyboard focus 위치를 명확히 보여야 한다.

Q. focus ring이 잘리면 문제야?
A. 문제다. 사용자가 현재 focus 위치를 보기 어려워진다.

Q. focus style은 모든 interactive element에 필요해?
A. 필요하다. 버튼, 링크, input, custom trigger 모두 확인해야 한다.

---

## 5.2 Disabled State

### [개념]

Disabled State는 사용자가 현재 조작할 수 없는 UI 상태다.

Disabled 상태는 시각적으로 구분되어야 하지만, 너무 낮은 대비로 정보를 읽기 어렵게 만들면 안 된다.

---

### [핵심]

Disabled 대상:

- button
- input
- select
- checkbox
- radio
- link-like control
- menu item
- submit button
- pagination control

기준:

- 조작 불가 상태 명확화
- 너무 낮은 대비 주의
- disabled 이유 제공 고려
- native `disabled` 사용
- `aria-disabled`는 custom control에서 고려
- focus 여부 정책 명확화

---

### [실무]

Native disabled:

```jsx
<button type="submit" disabled={loading}>
  {loading ? "저장 중..." : "저장"}
</button>
```

Custom aria-disabled:

```jsx
<div role="button" aria-disabled="true" tabIndex={-1}>
  제출
</div>
```

비활성 이유 제공:

```jsx
<button type="submit" disabled={!canSubmit}>
  제출
</button>
<p id="submit-help">
  필수 항목을 모두 입력하면 제출할 수 있습니다.
</p>
```

실무 기준:

- native control은 `disabled` 사용
- disabled text가 지나치게 흐리지 않게 함
- disabled 이유가 불명확하면 helper text 제공
- `aria-disabled`는 동작 차단을 자동으로 하지 않음
- disabled button은 focus 대상에서 제외될 수 있음
- 비활성 버튼만 있고 이유가 없으면 사용자가 막힐 수 있음

---

### [FAQ]

Q. disabled 버튼은 흐리게만 만들면 돼?
A. 조작 불가 상태는 보여야 하지만 텍스트를 읽기 어려울 정도로 낮은 대비는 피해야 한다.

Q. aria-disabled와 disabled는 같아?
A. 아니다. disabled는 native 동작을 막고 aria-disabled는 상태만 전달하므로 동작 차단은 직접 처리해야 한다.

Q. disabled button은 focus돼?
A. native disabled button은 일반적으로 focus 대상에서 제외된다.

Q. disabled 이유를 알려줘야 해?
A. 사용자가 왜 조작할 수 없는지 알기 어려운 경우 helper text를 제공하는 것이 좋다.

---

## 5.3 Loading Visual State

### [개념]

Loading Visual State는 데이터 요청이나 작업 처리 중임을 사용자에게 보여주는 상태다.

Loading은 spinner만 보여주는 것이 아니라 텍스트 상태와 보조기술 전달을 함께 고려해야 한다.

---

### [핵심]

Loading 구성:

- loading text
- spinner
- skeleton
- progress
- `role="status"`
- `aria-live="polite"`
- `aria-busy`
- disabled submit button
- visual stability

주의:

- spinner only 지양
- skeleton only 지양
- 무한 loading 방치 금지
- focus 이동 여부 검토
- submit 중 중복 제출 방지

---

### [실무]

Loading section:

```jsx
<section aria-busy={loading}>
  {loading && (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  )}
</section>
```

Loading button:

```jsx
<button type="submit" disabled={loading} aria-busy={loading}>
  {loading ? "저장 중..." : "저장"}
</button>
```

Spinner + text:

```jsx
<div role="status">
  <Spinner aria-hidden="true" />
  <span>처리 중입니다.</span>
</div>
```

Skeleton:

```jsx
<div aria-hidden="true" className="skeleton-list" />
<div role="status">목록을 불러오는 중입니다.</div>
```

실무 기준:

- spinner에는 텍스트 상태 제공
- skeleton은 장식이면 `aria-hidden`
- loading 중 submit button text 변경
- loading 영역에 `aria-busy` 고려
- loading이 끝나면 상태 메시지 제거 또는 결과 표시
- 너무 잦은 live region 업데이트 주의

---

### [FAQ]

Q. Spinner만 보이면 충분해?
A. 아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

Q. Loading button은 어떻게 표시해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 disabled 또는 aria-busy를 고려한다.

Q. aria-busy만 있으면 loading 접근성이 충분해?
A. 아니다. 사용자가 이해할 수 있는 loading text도 함께 제공하는 것이 좋다.

---

## 5.4 Error Visual State

### [개념]

Error Visual State는 오류가 발생했음을 사용자에게 명확히 보여주는 상태다.

오류는 색상, 아이콘, 텍스트, ARIA 상태, focus 정책을 함께 고려해야 한다.

---

### [핵심]

Error State 구성:

- error text
- error icon
- color
- `aria-invalid`
- `aria-describedby`
- `role="alert"`
- retry button
- field error
- global error
- focus management

주의:

- color only error 금지
- icon only error 금지
- stack trace 노출 금지
- 모호한 오류 문구 지양
- 오류 위치 명확화

---

### [실무]

Field Error:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>
{error && (
  <p id="email-error" role="alert">
    이메일을 입력해 주세요.
  </p>
)}
```

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

실무 기준:

- 오류는 텍스트로 명확히 제공
- 오류 field와 message 연결
- 오류 아이콘은 장식 처리 가능
- 오류 색상 외 추가 단서 제공
- 페이지 오류는 재시도 action 제공
- 서버 내부 오류는 사용자 메시지로 변환
- 긴 Form에서는 Error Summary 고려

---

### [FAQ]

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. 오류 아이콘만 있으면 충분해?
A. 아니다. 오류 메시지 텍스트와 수정 방법을 함께 제공해야 한다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 되지만 alert 남발은 사용자를 방해할 수 있다.

Q. 오류 문구는 어떻게 써?
A. 사용자가 무엇을 수정해야 하는지 짧고 명확하게 작성한다.

---

# 6. Visual Layout Accessibility

## 6.1 Text Readability

### [개념]

Text Readability는 사용자가 텍스트를 쉽게 읽고 이해할 수 있도록 글자 크기, 줄 간격, 문단 길이, 대비, 정렬을 관리하는 기준이다.

접근성은 스크린 리더만의 문제가 아니라 시각적으로 읽기 쉬운 UI를 포함한다.

---

### [핵심]

검토 대상:

- font size
- line height
- paragraph length
- text contrast
- text alignment
- letter spacing
- responsive text
- zoom behavior
- dark mode readability
- dense UI text
- helper text readability
- error text readability

---

### [실무]

실무 기준:

```text
텍스트 크기 확인
→ 줄 간격 확인
→ 대비 확인
→ 모바일 줄바꿈 확인
→ 확대 시 레이아웃 깨짐 확인
→ helper / error text 가독성 확인
```

CSS 예:

```css
.body-text {
  line-height: 1.5;
}

.helper-text {
  line-height: 1.4;
}
```

주의:

- 너무 작은 helper text 지양
- 긴 문단은 bullet 또는 section으로 분리
- 가운데 정렬 긴 문단 지양
- placeholder를 중요한 안내로 사용하지 않음
- 확대 시 text clipping 방지
- line height가 너무 좁으면 가독성 저하

---

### [FAQ]

Q. Text Readability도 접근성이야?
A. 그렇다. 텍스트를 읽기 어려우면 사용자가 정보를 이해하기 어렵다.

Q. helper text는 작게 써도 돼?
A. 너무 작거나 대비가 낮으면 읽기 어렵다. 중요한 안내라면 충분히 읽을 수 있어야 한다.

Q. 긴 설명 문단은 어떻게 처리해?
A. 짧은 문단, bullet, heading으로 구조화하는 것이 좋다.

Q. 확대했을 때 텍스트가 잘리면 문제야?
A. 문제다. 사용자가 확대 환경에서도 내용을 읽을 수 있어야 한다.

---

## 6.2 Responsive and Zoom Accessibility

### [개념]

Responsive and Zoom Accessibility는 화면 확대, 브라우저 zoom, 작은 화면, 큰 글꼴 환경에서도 UI가 읽히고 조작 가능하도록 만드는 기준이다.

사용자는 브라우저 확대나 OS 글꼴 크기 확대를 사용할 수 있다.

---

### [핵심]

검토 대상:

- browser zoom
- text scaling
- mobile viewport
- responsive layout
- horizontal scroll
- text clipping
- button target size
- modal overflow
- sticky header overlap
- focus ring clipping
- table responsive behavior

---

### [실무]

검토 Flow:

```text
Browser Zoom 적용
→ Text clipping 확인
→ Button / Link 조작 가능 확인
→ Modal overflow 확인
→ Form label / error 표시 확인
→ Table / Card layout 확인
→ Focus ring 표시 확인
```

실무 기준:

- 확대 시 텍스트가 잘리지 않아야 함
- content가 겹치지 않아야 함
- button target이 너무 작지 않아야 함
- modal은 작은 화면에서 스크롤 가능해야 함
- sticky header가 skip link / focus target을 가리지 않게 함
- table은 작은 화면에서 의미를 잃지 않게 설계
- absolute position text clipping 주의

---

### [FAQ]

Q. 브라우저 zoom도 접근성 검토 대상이야?
A. 그렇다. 확대 환경에서도 UI를 읽고 조작할 수 있어야 한다.

Q. 모바일에서 버튼이 작으면 접근성 문제야?
A. 조작하기 어려울 수 있으므로 충분한 클릭 영역을 제공하는 것이 좋다.

Q. Modal이 작은 화면에서 잘리면 문제야?
A. 문제다. Modal 내부 스크롤이나 responsive layout을 고려해야 한다.

Q. sticky header가 focus target을 가리면 문제야?
A. 문제다. keyboard 사용자가 focus 위치를 확인하기 어려울 수 있다.

---

## 6.3 Motion and Animation Basics

### [개념]

Motion Accessibility는 애니메이션, 전환 효과, 자동 재생 움직임이 사용자에게 불편이나 혼란을 주지 않도록 관리하는 기준이다.

Frontend Accessibility Foundation에서는 기본적인 모션 절제와 사용자 선호 설정 대응을 다룬다.

---

### [핵심]

검토 대상:

- auto animation
- carousel autoplay
- loading animation
- parallax
- skeleton shimmer
- modal transition
- hover animation
- focus animation
- motion sensitivity
- `prefers-reduced-motion`

기준:

- 불필요한 모션 지양
- 자동 재생 제어 제공
- 중요한 정보가 애니메이션에만 의존하지 않음
- reduced motion 환경 고려
- focus 이동을 애니메이션으로 숨기지 않음

---

### [실무]

Reduced Motion 예:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

Carousel 기준:

```text
자동 재생 Carousel
→ 일시정지 / 정지 버튼 제공
→ keyboard 조작 가능
→ focus 시 자동 이동 방지 검토
→ reduced motion 고려
```

실무 기준:

- 자동 움직임은 제어 수단 제공
- skeleton shimmer는 reduced motion 고려
- scroll-behavior smooth는 reduced motion에서 비활성화 고려
- modal animation이 focus 이동을 방해하지 않게 함
- hover에만 의존하는 정보 표시 금지
- 애니메이션이 loading / success / error의 유일한 단서가 되지 않게 함

---

### [FAQ]

Q. Animation도 접근성 이슈가 있어?
A. 있다. 과도한 움직임은 일부 사용자에게 불편을 줄 수 있고 정보 인식을 방해할 수 있다.

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 움직임 감소를 선호하는 환경 설정을 CSS에서 감지하는 미디어 쿼리다.

Q. Carousel 자동 재생은 괜찮아?
A. 사용자가 일시정지하거나 제어할 수 있어야 하며 keyboard 조작도 가능해야 한다.

Q. hover animation만으로 정보를 보여줘도 돼?
A. 권장하지 않는다. keyboard와 touch 사용자도 정보를 접근할 수 있어야 한다.

---

# 7. Design Token Accessibility

## 7.1 Accessible Color Token

### [개념]

Accessible Color Token은 Design System에서 색상 대비와 상태 전달 기준을 만족하도록 색상 값을 관리하는 방식이다.

색상 token은 brand color만이 아니라 text, background, border, focus, error, success, warning, disabled 상태를 접근성 기준으로 정의해야 한다.

---

### [핵심]

Color Token 대상:

- text primary
- text secondary
- text disabled
- background
- surface
- border
- focus ring
- link
- error
- success
- warning
- info
- selected
- hover
- active
- disabled

검토 기준:

- contrast
- light / dark mode
- state distinction
- color only prevention
- semantic token naming
- design consistency

---

### [실무]

Token 예:

```css
:root {
  --color-text-primary: #111111;
  --color-text-secondary: #555555;
  --color-background: #ffffff;
  --color-focus-ring: currentColor;
  --color-error-text: #b00020;
}
```

Semantic Token 예:

```text
Bad:
--red-500
--gray-300

Good:
--color-error-text
--color-focus-ring
--color-text-secondary
--color-border-disabled
```

실무 기준:

- 색상은 의미 기반 token으로 관리
- error / success / warning은 텍스트와 아이콘도 함께 제공
- focus ring token은 모든 interactive component에 적용
- 다크모드 token도 대비 확인
- disabled token은 너무 낮은 대비를 피함
- token 변경 시 주요 Component 시각 회귀 확인

---

### [FAQ]

Q. Color Token도 접근성과 관련 있어?
A. 그렇다. token 단계에서 대비가 낮으면 모든 Component에 접근성 문제가 퍼질 수 있다.

Q. semantic color token이 왜 좋아?
A. 색상의 역할이 명확해져 error, focus, disabled 같은 상태를 일관되게 관리할 수 있다.

Q. brand color가 대비가 낮으면 어떻게 해?
A. 텍스트나 중요한 UI에는 대비를 만족하는 보정 색상을 별도로 정의해야 한다.

Q. 다크모드 token도 따로 검수해야 해?
A. 그렇다. 라이트모드와 다크모드의 대비는 다르게 나타날 수 있다.

---

## 7.2 Focus Token

### [개념]

Focus Token은 Design System에서 focus ring의 두께, offset, 색상, 형태를 일관되게 관리하는 기준이다.

Focus Token이 없으면 Component마다 focus style이 누락되거나 불일치할 수 있다.

---

### [핵심]

Focus Token 구성:

- focus ring color
- focus ring width
- focus ring offset
- focus ring radius
- focus shadow
- high contrast fallback
- dark mode focus
- component override rule

---

### [실무]

Focus Token 예:

```css
:root {
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-color: currentColor;
}
```

공통 focus class:

```css
.focus-ring:focus-visible {
  outline: var(--focus-ring-width) solid var(--focus-ring-color);
  outline-offset: var(--focus-ring-offset);
}
```

Component 적용:

```jsx
<button type="button" className="focus-ring">
  저장
</button>
```

실무 기준:

- 공통 Component에 focus ring 기본 적용
- outline 제거 reset 코드 검토
- focus token은 배경과 충분히 구분되어야 함
- border radius가 있는 Component에서도 focus가 잘 보여야 함
- focus ring이 parent overflow로 잘리지 않게 함
- dark mode에서도 확인

---

### [FAQ]

Q. Focus Token은 왜 필요해?
A. 모든 interactive component에 일관된 focus style을 제공하기 위해 필요하다.

Q. focus ring 색상은 brand color로 해도 돼?
A. 가능하지만 배경과 충분히 대비되어야 한다.

Q. focus ring이 디자인과 안 맞으면 없애도 돼?
A. 없애면 안 된다. 디자인에 맞는 대체 focus style을 제공해야 한다.

Q. focus token은 어디에 적용해?
A. button, link, input, select, checkbox, custom trigger 등 모든 interactive component에 적용한다.

---

# 8. Image Icon Color Testing

## 8.1 Manual Visual Accessibility Check

### [개념]

Manual Visual Accessibility Check는 이미지, 아이콘, 색상, focus, loading, error, zoom 상태를 사람이 직접 확인하는 절차다.

자동화 도구는 일부 대비와 alt 누락을 찾을 수 있지만 이미지 목적, 색상 의미, 텍스트 가독성은 수동 판단이 필요하다.

---

### [핵심]

수동 점검 항목:

- 이미지 alt 목적 적합성
- 장식 이미지 empty alt
- 아이콘 버튼 accessible name
- 상태 아이콘 텍스트 제공
- 색상만으로 의미 전달 여부
- 텍스트 대비
- focus visible
- loading text
- error text
- dark mode contrast
- browser zoom
- reduced motion
- chart description

---

### [실무]

Manual Check Flow:

```text
Image 확인
→ alt 의미 확인
→ Icon Button 이름 확인
→ 색상만 의미 전달 여부 확인
→ Error / Success 텍스트 확인
→ Focus Visible 확인
→ Dark Mode 확인
→ Zoom 확인
→ Motion 설정 확인
```

우선 점검 화면:

- Login
- Signup
- Search
- Festival Card
- Festival Detail
- Review Form
- Payment
- Modal
- Dropdown
- Toast
- Chart
- Admin Table
- Dashboard

실무 기준:

- 이미지 목적은 사람 판단 필요
- 색상 대비는 도구로 확인
- 색상만 의미 전달하는 UI를 우선 수정
- icon button은 Testing Library로 이름 확인
- zoom / responsive 확인
- focus ring은 keyboard로 직접 확인
- chart는 설명 또는 table 확인

---

### [FAQ]

Q. 이미지 alt는 자동화 도구만으로 검증 가능해?
A. alt 누락은 잡을 수 있지만 alt가 적절한지는 사람이 문맥을 보고 판단해야 한다.

Q. 색상만 의미 전달하는 문제는 어떻게 찾아?
A. 색상을 제거하거나 흑백으로 봐도 상태를 이해할 수 있는지 확인한다.

Q. focus visible은 어떻게 확인해?
A. keyboard Tab으로 이동하면서 현재 위치가 명확히 보이는지 확인한다.

Q. dark mode도 접근성 테스트 대상이야?
A. 그렇다. 다크모드에서 대비와 focus가 충분한지 확인해야 한다.

---

## 8.2 Testing Library Visual Query

### [개념]

Testing Library Visual Query는 이미지 alt, icon button accessible name, status message, alert message 등을 사용자 관점에서 검증하는 방식이다.

이미지와 아이콘 접근성은 `getByAltText`, `getByRole`, `getByLabelText`, `getByText`로 일부 검증할 수 있다.

---

### [핵심]

검증 Query:

- `getByAltText`
- `queryByAltText`
- `getByRole("img")`
- `getByRole("button", { name })`
- `getByRole("status")`
- `getByRole("alert")`
- `getByText`
- `getByLabelText`

검증 대상:

- informative image alt
- decorative image exclusion
- icon button name
- loading status
- error alert
- success status
- link accessible name

---

### [실무]

정보 이미지:

```tsx
expect(screen.getByAltText("봄꽃 축제 행사장 전경")).toBeInTheDocument();
```

아이콘 버튼:

```tsx
expect(screen.getByRole("button", { name: "알림 열기" })).toBeInTheDocument();
```

장식 이미지:

```tsx
expect(screen.queryByAltText("장식 이미지")).not.toBeInTheDocument();
```

Loading:

```tsx
expect(screen.getByRole("status")).toHaveTextContent(
  "데이터를 불러오는 중입니다.",
);
```

Error:

```tsx
expect(screen.getByRole("alert")).toHaveTextContent("이메일을 입력해 주세요.");
```

실무 기준:

- icon button은 role/name으로 검증
- 정보 이미지는 alt text 검증
- 장식 이미지는 불필요한 alt가 없는지 검토
- loading / success는 status로 검증 가능
- error는 alert 또는 text로 검증 가능
- 색상 대비 자체는 Testing Library보다 시각/도구 검증 필요

---

### [FAQ]

Q. 이미지 alt는 Testing Library로 테스트할 수 있어?
A. 가능하다. getByAltText로 정보 이미지의 alt를 확인할 수 있다.

Q. 아이콘 버튼 접근성은 어떻게 테스트해?
A. getByRole("button", { name: "알림 열기" })처럼 accessible name으로 찾는다.

Q. 장식 이미지는 어떻게 테스트해?
A. 장식 이미지가 불필요한 alt로 노출되지 않는지 queryByAltText 등으로 확인할 수 있다.

Q. 색상 대비도 Testing Library로 확인해?
A. 일반적으로 색상 대비는 전용 도구나 수동 검증이 필요하다.

---

## 8.3 axe Visual and ARIA Check

### [개념]

axe 같은 자동화 도구는 이미지 alt 누락, 일부 color contrast 문제, ARIA 오류, label 누락을 탐지할 수 있다.

하지만 이미지 alt의 품질, 색상만 의미 전달, 차트 설명 적절성은 자동으로 완전히 판단하기 어렵다.

---

### [핵심]

axe 탐지 가능 예:

- missing image alt
- empty button name
- missing form label
- some color contrast issue
- invalid ARIA
- aria-hidden focus issue 일부
- landmark issue
- heading issue 일부

axe 한계:

- alt text 품질
- 장식 이미지 판단
- color only meaning
- chart 설명 충분성
- focus ring 시각 품질
- dark mode 전체 대비
- motion discomfort
- responsive zoom usability

---

### [실무]

axe 적용 우선순위:

```text
Common Components
→ Button / Icon Button
→ Image Card
→ Form
→ Modal
→ Toast
→ Table
→ Dashboard / Chart
```

실무 기준:

- axe 오류는 실제 UI와 함께 확인
- missing alt는 이미지 목적에 따라 alt 또는 empty alt 결정
- contrast 오류는 디자인 token 수정으로 연결
- empty button name은 icon button aria-label 확인
- axe 통과만으로 접근성 완료 판단 금지
- 수동 keyboard / visual check와 함께 사용

---

### [FAQ]

Q. axe가 이미지 alt 누락을 잡아줘?
A. 잡을 수 있다. 하지만 alt가 문맥에 맞는지는 사람이 확인해야 한다.

Q. axe가 색상 대비를 다 잡아줘?
A. 일부는 잡지만 모든 상태, 다크모드, focus ring 품질을 완전히 보장하지는 못한다.

Q. axe 통과하면 이미지 접근성 완료야?
A. 아니다. 이미지 목적과 설명 품질은 수동 검토가 필요하다.

Q. icon button name 누락도 axe가 잡을 수 있어?
A. empty button name 같은 문제는 탐지할 수 있다.

---

# 9. Image Icon Color Review

## 9.1 Review Checklist

### [개념]

Image Icon Color Review는 이미지, 아이콘, 색상, 시각 상태가 접근성 기준을 만족하는지 검토하는 과정이다.

Review Agent는 이미지 alt 누락뿐 아니라 이미지 목적, 아이콘 기능, 색상만 의미 전달, focus visible까지 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 정보 이미지에 의미 있는 alt가 있는가?
- [ ] 장식 이미지에 alt=""가 적용되었는가?
- [ ] 링크 이미지의 alt가 이동 목적을 설명하는가?
- [ ] 버튼 이미지의 alt 또는 accessible name이 기능을 설명하는가?
- [ ] 복잡한 차트 / 그래프에 별도 설명이 있는가?
- [ ] 차트 데이터가 표나 텍스트로 제공되는가?
- [ ] 텍스트 옆 장식 아이콘이 aria-hidden 처리되었는가?
- [ ] icon only button에 accessible name이 있는가?
- [ ] icon button 내부 icon이 aria-hidden 처리되었는가?
- [ ] 상태 아이콘에 텍스트 또는 accessible name이 함께 제공되는가?
- [ ] 색상만으로 error / success / selected 상태를 전달하지 않는가?
- [ ] 텍스트와 배경의 color contrast가 충분한가?
- [ ] dark mode에서도 대비가 충분한가?
- [ ] focus visible이 명확한가?
- [ ] focus ring이 잘리지 않는가?
- [ ] disabled 상태가 읽을 수 있게 표시되는가?
- [ ] loading 상태가 spinner만으로 제공되지 않는가?
- [ ] error 상태가 색상만으로 제공되지 않는가?
- [ ] zoom / responsive 환경에서 텍스트가 잘리지 않는가?
- [ ] prefers-reduced-motion을 고려했는가?
```

---

### [실무]

Review Flow:

```text
Image 확인
→ alt 목적 검토
→ Icon 역할 검토
→ Icon Button name 검토
→ Status Icon text 검토
→ Color Only Meaning 검토
→ Contrast 검토
→ Focus Visible 검토
→ Loading / Error State 검토
→ Zoom / Motion 검토
→ Testing Query / axe 확인
```

대표 수정 패턴:

```text
문제: icon button accessible name 없음
해결: button aria-label 제공 + icon aria-hidden
```

```text
문제: 장식 이미지가 불필요하게 읽힘
해결: alt="" 적용
```

```text
문제: 오류를 빨간색으로만 표시
해결: error text + aria-invalid + aria-describedby 적용
```

```text
문제: 차트 이미지에 alt만 있음
해결: 핵심 요약 + 데이터 테이블 제공
```

---

### [FAQ]

Q. Image Review에서 가장 먼저 볼 것은?
A. 이미지가 정보인지 장식인지 기능인지 먼저 판단하고 alt를 결정한다.

Q. Icon Review에서 가장 먼저 볼 것은?
A. 아이콘이 장식인지 기능인지 상태 전달인지 판단하고 accessible name 필요 여부를 확인한다.

Q. Color Review에서 가장 먼저 볼 것은?
A. 색상만으로 의미를 전달하는지와 텍스트 대비가 충분한지 확인한다.

Q. Visual Review는 자동화만으로 충분해?
A. 아니다. alt 품질, 색상 의미, focus 시각 품질은 수동 검토가 필요하다.

---

# 10. Common Image Icon Color Mistakes

## 10.1 Visual Accessibility Anti Patterns

### [개념]

Visual Accessibility Anti Pattern은 이미지, 아이콘, 색상, focus, loading, error 상태가 시각적으로는 동작하지만 보조기술 사용자나 시각적 제약이 있는 사용자에게 의미를 충분히 전달하지 못하는 구현 방식이다.

---

### [핵심]

자주 발생하는 실수:

- 정보 이미지 alt 누락
- 장식 이미지에 불필요한 alt 제공
- 링크 이미지 alt가 목적을 설명하지 않음
- 파일명을 alt로 사용
- 모든 이미지에 “이미지”라는 단어 포함
- 차트 이미지에 별도 설명 없음
- icon button accessible name 누락
- icon button의 SVG만 label 처리
- 상태 아이콘만으로 성공 / 오류 표시
- 색상만으로 error 표시
- 색상만으로 selected 표시
- 색상만으로 chart line 구분
- focus outline 제거
- focus ring 대비 부족
- focus ring clipping
- placeholder 대비 부족
- disabled text 대비 과도하게 낮음
- spinner만으로 loading 표시
- skeleton만으로 loading 표시
- animation 자동 재생 제어 없음
- reduced motion 미고려

---

### [실무]

Anti Pattern:

```jsx
<img src="/festival.jpg" />
```

개선:

```jsx
<img src="/festival.jpg" alt="봄꽃 축제 행사장 전경" />
```

Anti Pattern:

```jsx
<button type="button">
  <CloseIcon />
</button>
```

개선:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

Anti Pattern:

```jsx
<p className="error-red-only">이메일</p>
```

개선:

```jsx
<p id="email-error" role="alert">
  오류: 이메일을 입력해 주세요.
</p>
```

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

---

### [FAQ]

Q. 이미지 접근성 초보가 가장 많이 하는 실수는?
A. alt 누락, 파일명 alt 사용, 장식 이미지 설명, 차트 설명 누락이 많다.

Q. 아이콘 접근성 초보가 가장 많이 하는 실수는?
A. icon button에 accessible name을 제공하지 않는 실수가 많다.

Q. 색상 접근성 초보가 가장 많이 하는 실수는?
A. 빨간색만으로 오류를 표시하거나 색상만으로 선택 상태를 표시하는 실수가 많다.

Q. Loading 접근성 초보가 가장 많이 하는 실수는?
A. spinner나 skeleton만 보여주고 loading text를 제공하지 않는 실수가 많다.

---

# Retrieval Queries

### [FAQ]

Q. Image Accessibility는 왜 필요해?
A. 이미지를 볼 수 없는 사용자도 이미지의 정보, 기능, 목적을 이해할 수 있어야 하기 때문이다.

Q. alt text는 무엇을 써야 해?
A. 이미지의 외형보다 이미지가 전달하는 목적과 의미를 짧고 명확하게 작성한다.

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 필요하다. 정보 이미지는 의미 있는 alt, 장식 이미지는 alt=""를 사용한다.

Q. alt에 이미지나 사진이라는 말을 넣어야 해?
A. 보통 넣지 않는다. 스크린 리더가 이미 이미지임을 전달할 수 있다.

Q. 정보 이미지는 어떻게 alt를 써?
A. 이미지가 전달하는 핵심 의미를 짧고 명확하게 작성한다.

Q. 축제 대표 이미지 alt는 어떻게 써?
A. 이미지가 정보 전달 역할이면 축제명이나 행사장 의미를 포함한다.

Q. 프로필 이미지는 alt를 어떻게 써?
A. 사용자를 식별하는 목적이면 “닉네임 프로필 이미지”처럼 작성할 수 있다.

Q. 파일명을 alt로 써도 돼?
A. 안 된다. 파일명은 사용자에게 의미 있는 대체 텍스트가 아니다.

Q. 장식 이미지는 alt를 비워도 돼?
A. 그렇다. 장식 이미지는 alt=""로 스크린 리더가 건너뛰게 하는 것이 적합하다.

Q. 모든 이미지에 자세한 설명을 넣는 게 더 좋아?
A. 아니다. 장식 이미지를 읽게 하면 오히려 불필요한 정보가 늘어난다.

Q. 카드 이미지가 제목과 완전히 중복되면?
A. 카드 제목이 충분히 정보를 제공한다면 이미지 alt=""를 검토할 수 있다.

Q. CSS background image는 접근성에 안전해?
A. 장식이면 괜찮지만 정보 전달 이미지라면 대체 텍스트를 별도로 제공해야 한다.

Q. 링크 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크의 이동 목적을 전달하는 alt를 제공한다.

Q. 로고가 홈으로 이동하면 alt는 뭐가 좋아?
A. “서비스명 홈”처럼 링크 목적을 포함하는 것이 좋다.

Q. 버튼 안 아이콘에는 alt를 써야 해?
A. SVG 아이콘이면 보통 aria-hidden 처리하고 button에 aria-label을 제공한다.

Q. Functional Image alt에 외형 설명을 쓰면 안 돼?
A. 기능을 이해해야 하므로 외형보다 동작 목적을 설명해야 한다.

Q. 차트 이미지는 alt만 쓰면 충분해?
A. 대체로 부족하다. 핵심 요약이나 데이터 테이블을 함께 제공하는 것이 좋다.

Q. 복잡한 이미지는 어떻게 설명해?
A. 짧은 alt와 함께 인접한 설명, 표, 요약 텍스트를 제공한다.

Q. 지도 이미지는 alt를 어떻게 써?
A. 장소나 이동 목적, 핵심 위치 정보를 전달해야 한다.

Q. architecture diagram도 접근성 설명이 필요해?
A. 필요하다. 주요 구성 요소와 흐름을 텍스트로 제공하는 것이 좋다.

Q. Icon Accessibility는 왜 필요해?
A. 아이콘이 기능이나 상태를 전달할 때 보조기술 사용자도 그 의미를 이해해야 하기 때문이다.

Q. 아이콘에 항상 aria-label을 붙여야 해?
A. 아니다. 장식 아이콘은 aria-hidden이 적합하고 기능 아이콘은 부모 control에 이름을 제공한다.

Q. 아이콘만 있는 버튼은 어떻게 해야 해?
A. button에 aria-label을 제공하고 내부 icon은 aria-hidden 처리한다.

Q. 텍스트 옆 아이콘은 어떻게 처리해?
A. 텍스트가 의미를 이미 전달한다면 아이콘은 aria-hidden으로 장식 처리할 수 있다.

Q. 텍스트가 있는 버튼의 아이콘도 읽혀야 해?
A. 보통 필요 없다. 텍스트가 의미를 전달하므로 아이콘은 aria-hidden 처리한다.

Q. 검색 input 앞 돋보기 아이콘은 어떻게 해?
A. label이 따로 있다면 돋보기 아이콘은 장식으로 보고 aria-hidden 처리할 수 있다.

Q. 장식 아이콘에 title을 넣어도 돼?
A. 불필요한 중복 정보가 될 수 있으므로 지양한다.

Q. 아이콘이 없어도 의미가 통해야 해?
A. 그렇다. 중요한 의미는 텍스트나 accessible name으로 제공해야 한다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. 아이콘 버튼에는 aria-label을 어디에 붙여?
A. 아이콘이 아니라 button 요소에 붙이는 것이 적합하다.

Q. 좋아요 버튼은 aria-label이 어떻게 바뀌어야 해?
A. 상태에 따라 “좋아요” 또는 “좋아요 취소”처럼 실제 동작을 설명할 수 있다.

Q. icon button 내부 SVG는 어떻게 처리해?
A. 보통 aria-hidden="true"로 장식 처리한다.

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?
A. 색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

Q. 오류 아이콘만 표시하면 충분해?
A. 아니다. 오류 메시지 텍스트와 수정 방법을 함께 제공해야 한다.

Q. 상태 아이콘은 aria-hidden 처리해도 돼?
A. 텍스트가 상태를 전달한다면 아이콘은 장식 처리해도 된다.

Q. 상태를 색상과 아이콘으로만 표시해도 돼?
A. 권장하지 않는다. 텍스트나 aria 상태를 함께 제공해야 한다.

Q. Color Contrast는 왜 중요해?
A. 텍스트와 UI 요소가 배경과 충분히 구분되어야 사용자가 읽고 조작할 수 있기 때문이다.

Q. 회색 글씨가 예쁘면 그냥 써도 돼?
A. 텍스트 대비가 낮으면 읽기 어려울 수 있다. 도구로 확인하는 것이 좋다.

Q. 다크모드에서도 색상 대비를 따로 봐야 해?
A. 그렇다. 라이트모드에서 괜찮은 색상이 다크모드에서는 부족할 수 있다.

Q. focus outline도 대비가 필요해?
A. 필요하다. keyboard 사용자가 현재 위치를 명확히 볼 수 있어야 한다.

Q. 색상만으로 에러 표시해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘, aria 속성을 함께 제공해야 한다.

Q. 빨간색이면 에러라는 걸 알 수 있지 않아?
A. 모든 사용자가 색상을 동일하게 인식하지 않는다. 텍스트나 아이콘을 함께 제공해야 한다.

Q. 활성 메뉴를 색상만 다르게 해도 돼?
A. 권장하지 않는다. aria-current, 밑줄, 굵기, 텍스트 등 추가 단서를 제공하는 것이 좋다.

Q. 차트 선 색상만 다르면 충분해?
A. 아니다. legend, label, 선 모양, 데이터 테이블 같은 추가 단서가 필요할 수 있다.

Q. 링크는 색상만 다르면 충분해?
A. 권장하지 않는다. 밑줄이나 형태 같은 추가 단서가 있으면 더 명확하다.

Q. hover 때만 밑줄이 생기면 괜찮아?
A. 기본 상태에서 링크인지 알기 어려울 수 있다. 본문 링크는 기본 밑줄을 고려한다.

Q. 현재 페이지 링크는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. 링크처럼 보이는 버튼은 괜찮아?
A. 역할이 이동이면 Link, 액션이면 button을 사용해야 한다.

Q. focus outline을 없애도 돼?
A. 대체 focus style 없이 제거하면 안 된다.

Q. focus style은 hover style과 같아도 돼?
A. 구분되는 것이 좋다. keyboard focus 위치를 명확히 보여야 한다.

Q. focus ring이 잘리면 문제야?
A. 문제다. 사용자가 현재 focus 위치를 보기 어려워진다.

Q. focus style은 모든 interactive element에 필요해?
A. 필요하다. 버튼, 링크, input, custom trigger 모두 확인해야 한다.

Q. disabled 버튼은 흐리게만 만들면 돼?
A. 조작 불가 상태는 보여야 하지만 텍스트를 읽기 어려울 정도로 낮은 대비는 피해야 한다.

Q. aria-disabled와 disabled는 같아?
A. 아니다. disabled는 native 동작을 막고 aria-disabled는 상태만 전달하므로 동작 차단은 직접 처리해야 한다.

Q. disabled button은 focus돼?
A. native disabled button은 일반적으로 focus 대상에서 제외된다.

Q. disabled 이유를 알려줘야 해?
A. 사용자가 왜 조작할 수 없는지 알기 어려운 경우 helper text를 제공하는 것이 좋다.

Q. Spinner만 보이면 충분해?
A. 아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

Q. Loading button은 어떻게 표시해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 disabled 또는 aria-busy를 고려한다.

Q. aria-busy만 있으면 loading 접근성이 충분해?
A. 아니다. 사용자가 이해할 수 있는 loading text도 함께 제공하는 것이 좋다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 되지만 alert 남발은 사용자를 방해할 수 있다.

Q. 오류 문구는 어떻게 써?
A. 사용자가 무엇을 수정해야 하는지 짧고 명확하게 작성한다.

Q. Text Readability도 접근성이야?
A. 그렇다. 텍스트를 읽기 어려우면 사용자가 정보를 이해하기 어렵다.

Q. helper text는 작게 써도 돼?
A. 너무 작거나 대비가 낮으면 읽기 어렵다. 중요한 안내라면 충분히 읽을 수 있어야 한다.

Q. 긴 설명 문단은 어떻게 처리해?
A. 짧은 문단, bullet, heading으로 구조화하는 것이 좋다.

Q. 확대했을 때 텍스트가 잘리면 문제야?
A. 문제다. 사용자가 확대 환경에서도 내용을 읽을 수 있어야 한다.

Q. 브라우저 zoom도 접근성 검토 대상이야?
A. 그렇다. 확대 환경에서도 UI를 읽고 조작할 수 있어야 한다.

Q. 모바일에서 버튼이 작으면 접근성 문제야?
A. 조작하기 어려울 수 있으므로 충분한 클릭 영역을 제공하는 것이 좋다.

Q. Modal이 작은 화면에서 잘리면 문제야?
A. 문제다. Modal 내부 스크롤이나 responsive layout을 고려해야 한다.

Q. sticky header가 focus target을 가리면 문제야?
A. 문제다. keyboard 사용자가 focus 위치를 확인하기 어려울 수 있다.

Q. Animation도 접근성 이슈가 있어?
A. 있다. 과도한 움직임은 일부 사용자에게 불편을 줄 수 있고 정보 인식을 방해할 수 있다.

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 움직임 감소를 선호하는 환경 설정을 CSS에서 감지하는 미디어 쿼리다.

Q. Carousel 자동 재생은 괜찮아?
A. 사용자가 일시정지하거나 제어할 수 있어야 하며 keyboard 조작도 가능해야 한다.

Q. hover animation만으로 정보를 보여줘도 돼?
A. 권장하지 않는다. keyboard와 touch 사용자도 정보를 접근할 수 있어야 한다.

Q. Color Token도 접근성과 관련 있어?
A. 그렇다. token 단계에서 대비가 낮으면 모든 Component에 접근성 문제가 퍼질 수 있다.

Q. semantic color token이 왜 좋아?
A. 색상의 역할이 명확해져 error, focus, disabled 같은 상태를 일관되게 관리할 수 있다.

Q. brand color가 대비가 낮으면 어떻게 해?
A. 텍스트나 중요한 UI에는 대비를 만족하는 보정 색상을 별도로 정의해야 한다.

Q. Focus Token은 왜 필요해?
A. 모든 interactive component에 일관된 focus style을 제공하기 위해 필요하다.

Q. focus ring 색상은 brand color로 해도 돼?
A. 가능하지만 배경과 충분히 대비되어야 한다.

Q. focus ring이 디자인과 안 맞으면 없애도 돼?
A. 없애면 안 된다. 디자인에 맞는 대체 focus style을 제공해야 한다.

Q. 이미지 alt는 자동화 도구만으로 검증 가능해?
A. alt 누락은 잡을 수 있지만 alt가 적절한지는 사람이 문맥을 보고 판단해야 한다.

Q. 색상만 의미 전달하는 문제는 어떻게 찾아?
A. 색상을 제거하거나 흑백으로 봐도 상태를 이해할 수 있는지 확인한다.

Q. 이미지 alt는 Testing Library로 테스트할 수 있어?
A. 가능하다. getByAltText로 정보 이미지의 alt를 확인할 수 있다.

Q. 아이콘 버튼 접근성은 어떻게 테스트해?
A. getByRole("button", { name: "알림 열기" })처럼 accessible name으로 찾는다.

Q. 장식 이미지는 어떻게 테스트해?
A. 장식 이미지가 불필요한 alt로 노출되지 않는지 queryByAltText 등으로 확인할 수 있다.

Q. 색상 대비도 Testing Library로 확인해?
A. 일반적으로 색상 대비는 전용 도구나 수동 검증이 필요하다.

Q. axe가 이미지 alt 누락을 잡아줘?
A. 잡을 수 있다. 하지만 alt가 문맥에 맞는지는 사람이 확인해야 한다.

Q. axe가 색상 대비를 다 잡아줘?
A. 일부는 잡지만 모든 상태, 다크모드, focus ring 품질을 완전히 보장하지는 못한다.

Q. Image Review에서 가장 먼저 볼 것은?
A. 이미지가 정보인지 장식인지 기능인지 먼저 판단하고 alt를 결정한다.

Q. Icon Review에서 가장 먼저 볼 것은?
A. 아이콘이 장식인지 기능인지 상태 전달인지 판단하고 accessible name 필요 여부를 확인한다.

Q. Color Review에서 가장 먼저 볼 것은?
A. 색상만으로 의미를 전달하는지와 텍스트 대비가 충분한지 확인한다.

Q. Visual Review는 자동화만으로 충분해?
A. 아니다. alt 품질, 색상 의미, focus 시각 품질은 수동 검토가 필요하다.

Q. 이미지 접근성 초보가 가장 많이 하는 실수는?
A. alt 누락, 파일명 alt 사용, 장식 이미지 설명, 차트 설명 누락이 많다.

Q. 아이콘 접근성 초보가 가장 많이 하는 실수는?
A. icon button에 accessible name을 제공하지 않는 실수가 많다.

Q. 색상 접근성 초보가 가장 많이 하는 실수는?
A. 빨간색만으로 오류를 표시하거나 색상만으로 선택 상태를 표시하는 실수가 많다.

Q. Loading 접근성 초보가 가장 많이 하는 실수는?
A. spinner나 skeleton만 보여주고 loading text를 제공하지 않는 실수가 많다.

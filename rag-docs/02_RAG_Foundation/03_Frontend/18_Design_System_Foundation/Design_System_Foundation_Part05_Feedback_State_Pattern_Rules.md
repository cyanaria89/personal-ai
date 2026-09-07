# Design System Foundation Part05 - Feedback State Pattern Rules

---

# 1. Feedback State Pattern Core

## 1.1 Feedback State Pattern Definition

### [개념]

Feedback State Pattern은 사용자 행동, 데이터 요청, 시스템 처리 결과에 대해 UI가 현재 상태를 명확히 알려주는 공통 패턴이다.

Feedback State Pattern은 Loading, Empty, Error, Success, Disabled, Validation 상태를 포함한다.

Feedback State Pattern은 Frontend Agent가 화면을 생성할 때 반드시 고려해야 하는 UI 품질 기준이며, Review Agent가 사용자 흐름 누락을 검토하는 핵심 기준이다.

---

### [핵심]

Feedback State Pattern 대상:

- Loading State
- Empty State
- Error State
- Success State
- Disabled State
- Validation State
- Skeleton State
- Progress State
- Retry State
- Offline State
- Permission State

Feedback State Pattern 목적:

- 사용자에게 현재 상태 전달
- 처리 중 여부 전달
- 실패 원인과 복구 방법 안내
- 데이터 없음 상태 명확화
- 성공 완료 피드백 제공
- 중복 클릭 / 중복 제출 방지
- Form Validation 품질 확보
- 사용자 흐름 중단 최소화
- PM Agent 화면 완료 판단 지원
- Review Agent 승인 / 반려 기준 제공

---

### [실무]

Feedback State 기본 Flow:

```text
User Action
→ Request Start
→ Loading State
→ Success / Empty / Error
→ Feedback Message
→ Recovery Action or Next Action
```

데이터 조회 Flow:

```text
Page Load
→ Loading State
→ Data Exists
→ Content Render
```

```text
Page Load
→ Loading State
→ Data Empty
→ Empty State
→ Optional Action
```

```text
Page Load
→ Loading State
→ Request Failed
→ Error State
→ Retry Action
```

Form 제출 Flow:

```text
Submit
→ Validation
→ Button Loading
→ Success Toast / Success State
→ Form Reset or Navigation
```

---

### [FAQ]

Q. Feedback State Pattern이 뭐야?
A. 사용자 행동이나 데이터 요청 결과에 대해 loading, empty, error, success 같은 상태를 UI로 알려주는 패턴이다.

Q. Feedback State는 왜 필요해?
A. 사용자가 화면이 멈췄는지, 성공했는지, 실패했는지, 데이터가 없는지 알 수 있어야 하기 때문이다.

Q. 모든 화면에 Feedback State가 필요해?
A. 데이터 요청, form 제출, 사용자 action이 있는 화면에는 loading, error, empty, success 상태를 검토해야 한다.

Q. Review Agent는 Feedback State에서 뭘 봐야 해?
A. Loading, Empty, Error, Success, Retry, Validation 상태가 필요한 곳에 제공되는지 확인해야 한다.

---

## 1.2 Feedback State Scope

### [개념]

Feedback State Scope는 Design System Foundation 단계에서 반드시 정의해야 하는 사용자 피드백 상태의 범위다.

Feedback State는 단순 메시지가 아니라 화면 흐름, 컴포넌트 상태, 접근성, 복구 action을 포함한다.

---

### [핵심]

포함 범위:

- Page Loading
- Section Loading
- Button Loading
- Skeleton Loading
- Progress Loading
- Empty State
- Search Empty State
- Filter Empty State
- Table Empty State
- Error State
- Network Error
- Server Error
- Permission Error
- Authentication Error
- Validation Error
- Success Toast
- Success Alert
- Success Page
- Retry Pattern
- Disabled State
- Offline State

제외 범위:

- 고급 장애 대응 시스템
- Observability Dashboard
- Backend Error Taxonomy 심화
- Advanced Error Boundary 전략
- 고급 A/B 테스트 UX
- Product Analytics 심화
- Enterprise Incident UX

---

### [실무]

Feedback State는 다음 문서와 연결된다.

```text
Error Handling Loading UX
→ UI Component Pattern
→ Frontend Accessibility
→ Design System Foundation
→ Frontend Code Review
```

역할 분리:

```text
Error Handling Loading UX
→ 비동기 상태 처리와 UX 흐름

Design System Feedback State
→ 공통 UI Pattern, 문구, 컴포넌트 사용 기준

Frontend Accessibility
→ aria-live, role alert, focus, keyboard 기준

Frontend Code Review
→ 구현 품질 검토 기준
```

---

### [FAQ]

Q. Feedback State Scope는 어디까지야?
A. Loading, Empty, Error, Success, Retry, Validation, Disabled, Offline 상태의 UI 패턴과 검토 기준까지다.

Q. Error Handling 문서와 겹치지 않아?
A. Error Handling 문서는 비동기 처리 흐름 중심이고, 이 문서는 Design System의 공통 UI Pattern 기준이다.

Q. Skeleton도 Feedback State에 포함돼?
A. 포함된다. Skeleton은 Loading State의 한 종류다.

Q. Permission Error도 포함돼?
A. 포함된다. 권한 없음은 사용자가 다음 행동을 알아야 하는 중요한 Error State다.

---

# 2. Loading State Pattern

## 2.1 Loading State Definition

### [개념]

Loading State는 데이터 요청이나 작업 처리 중임을 사용자에게 알려주는 UI 패턴이다.

Loading State는 사용자가 화면이 멈춘 것이 아니라 처리 중임을 이해하도록 만든다.

---

### [핵심]

Loading UI 종류:

- Spinner
- Skeleton
- Progress Bar
- Button Loading
- Page Loading
- Section Loading
- Inline Loading
- Table Loading
- Card Loading

사용 기준:

```text
짧은 작업
→ Button Loading 또는 Spinner

목록 / 카드 로딩
→ Skeleton

파일 업로드 / 긴 작업
→ Progress Bar

페이지 최초 로딩
→ Page Loading

일부 영역 갱신
→ Section Loading

테이블 데이터 로딩
→ Table Skeleton 또는 Row Skeleton
```

Loading State 목적:

- 처리 중 상태 전달
- 중복 클릭 방지
- 사용자 불안 감소
- 화면 전환 흐름 유지
- 데이터 구조 예상 제공
- 실패 전까지 대기 상태 명확화

---

### [실무]

Page Loading 예:

```jsx
if (isLoading) {
  return <PageLoading message="데이터를 불러오는 중입니다." />;
}
```

Section Loading 예:

```jsx
<section>
  <h2>생산 현황</h2>
  {isLoading ? <SkeletonList count={5} /> : <ProductionList items={items} />}
</section>
```

Button Loading 예:

```jsx
<Button type="submit" isLoading={isSubmitting} disabled={isSubmitting}>
  저장
</Button>
```

Review 기준:

```md
- [ ] 데이터 요청 중 Loading State가 있는가?
- [ ] loading 중 중복 action이 방지되는가?
- [ ] loading UI가 콘텐츠 구조와 맞는가?
- [ ] 너무 짧은 작업에 과도한 loading UI를 띄우지 않는가?
```

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. 사용자가 화면이 멈췄는지 처리 중인지 알 수 있어야 하기 때문이다.

Q. Loading State는 언제 필요해?
A. 데이터 조회, 저장, 삭제, 로그인, 파일 업로드처럼 시간이 걸리는 작업에 필요하다.

Q. 짧은 작업에도 Loading State가 필요해?
A. 중복 클릭 가능성이 있거나 사용자가 처리 여부를 알아야 하면 필요하다.

Q. Loading 중 버튼은 disabled 처리해야 해?
A. 대부분 그렇다. 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

---

## 2.2 Spinner Pattern

### [개념]

Spinner는 짧은 처리 중 상태를 표시하는 Loading UI다.

Spinner는 작업의 진행률을 알 수 없고 대기 시간이 짧을 때 적합하다.

---

### [핵심]

Spinner 사용 기준:

- 짧은 API 요청
- 작은 영역 로딩
- 버튼 내부 loading
- 데이터 구조를 예측하기 어려운 경우
- 진행률 표시가 불가능한 경우

Spinner 사용 주의:

- 긴 작업에는 Progress Bar 고려
- 목록 / 카드 로딩에는 Skeleton 권장
- Spinner만 오래 표시하면 사용자가 불안함
- 메시지를 함께 제공하면 명확함
- 무한 Spinner 방지 필요

---

### [실무]

Inline Spinner 예:

```jsx
<div role="status" aria-live="polite">
  <Spinner />
  <span>불러오는 중입니다.</span>
</div>
```

Button Spinner 예:

```jsx
<Button isLoading={isSaving} disabled={isSaving}>
  저장
</Button>
```

나쁜 예:

```jsx
<Spinner />
```

위 예는 맥락과 메시지가 없어 사용자가 무엇을 기다리는지 알기 어렵다.

Review 기준:

```md
- [ ] Spinner에 필요한 경우 상태 문구가 있는가?
- [ ] 긴 작업에 Spinner만 사용하지 않는가?
- [ ] role status 또는 aria-live를 고려했는가?
- [ ] 무한 로딩 상태가 방치되지 않는가?
```

---

### [FAQ]

Q. Spinner는 언제 써?
A. 짧은 작업이나 진행률을 알 수 없는 작은 영역 로딩에 사용한다.

Q. Spinner만 보여줘도 충분해?
A. 짧은 경우 가능하지만 문맥이 불명확하면 “불러오는 중입니다” 같은 문구를 함께 제공한다.

Q. 긴 작업에도 Spinner를 써도 돼?
A. 권장하지 않는다. 긴 작업은 Progress Bar나 단계 안내가 더 적합하다.

Q. Spinner 접근성에는 무엇이 필요해?
A. 필요한 경우 `role="status"`와 상태 문구를 제공한다.

---

## 2.3 Skeleton Pattern

### [개념]

Skeleton은 실제 콘텐츠가 로드되기 전 콘텐츠 구조를 미리 보여주는 Loading UI다.

Skeleton은 카드, 목록, 테이블처럼 로딩 후 구조가 예상 가능한 콘텐츠에 적합하다.

---

### [핵심]

Skeleton 사용 기준:

- 카드 목록
- 테이블 row
- 리스트 item
- 프로필 영역
- 대시보드 통계 카드
- 이미지 + 텍스트 구조
- 페이지 일부 영역 로딩

Skeleton 장점:

- 화면 구조 예측 가능
- 체감 대기 시간 감소
- layout shift 감소
- 목록 / 카드 로딩에 적합

Skeleton 주의:

- 실제 콘텐츠 구조와 유사해야 함
- 과도한 shimmer animation 주의
- reduced motion 고려
- 무한 skeleton 방지
- Error State 전환 필요

---

### [실무]

Skeleton List 예:

```jsx
if (isLoading) {
  return <SkeletonList count={5} />;
}
```

Card Skeleton 예:

```jsx
<Card>
  <Skeleton width="60%" height="24px" />
  <Skeleton width="100%" height="120px" />
  <Skeleton width="80%" height="16px" />
</Card>
```

Table Skeleton 예:

```jsx
<TableSkeleton rows={10} columns={5} />
```

Review 기준:

```md
- [ ] Skeleton이 실제 콘텐츠 구조와 유사한가?
- [ ] 목록 / 카드 로딩에 Spinner만 쓰지 않는가?
- [ ] reduced motion을 고려했는가?
- [ ] loading 실패 시 Error State로 전환되는가?
```

---

### [FAQ]

Q. Skeleton은 언제 써?
A. 카드나 목록처럼 로딩 후 구조가 예상 가능한 콘텐츠에 적합하다.

Q. Skeleton이 Spinner보다 좋은 경우는?
A. 목록, 카드, 테이블처럼 화면 구조를 미리 보여줄 수 있는 경우 Skeleton이 더 좋다.

Q. Skeleton은 실제 콘텐츠와 비슷해야 해?
A. 그렇다. 실제 구조와 너무 다르면 사용자가 로딩 후 화면을 예측하기 어렵다.

Q. Skeleton animation은 항상 넣어도 돼?
A. 과도한 animation은 피하고 prefers-reduced-motion을 고려해야 한다.

---

## 2.4 Progress Pattern

### [개념]

Progress Pattern은 작업 진행률이나 단계가 있는 긴 작업을 사용자에게 알려주는 Loading UI다.

Progress Pattern은 파일 업로드, 데이터 처리, 배치 작업, 긴 요청에 적합하다.

---

### [핵심]

Progress 사용 대상:

- 파일 업로드
- 대용량 데이터 처리
- 장비 시뮬레이션 연결
- 배치 작업
- 단계별 처리
- 긴 저장 작업
- 가져오기 / 내보내기

Progress 종류:

- Determinate Progress
- Indeterminate Progress
- Step Progress
- Upload Progress
- Processing Status

기준:

- 가능한 경우 진행률 표시
- 진행률 불가 시 단계나 상태 문구 제공
- 취소 가능 여부 명확화
- 실패 시 Error State 제공
- 완료 시 Success State 제공

---

### [실무]

Progress Bar 예:

```jsx
<ProgressBar value={uploadPercent} label="파일을 업로드하는 중입니다." />
```

Step Progress 예:

```jsx
<StepProgress
  currentStep={2}
  steps={["파일 확인", "데이터 처리", "저장 완료"]}
/>
```

진행 상태 문구 예:

```text
생산 데이터를 처리하는 중입니다.
잠시만 기다려 주세요.
```

Review 기준:

```md
- [ ] 긴 작업에 진행 상태를 제공하는가?
- [ ] 진행률 또는 단계가 명확한가?
- [ ] 실패 시 Error State가 있는가?
- [ ] 완료 시 Success Feedback이 있는가?
```

---

### [FAQ]

Q. Progress Pattern은 언제 써?
A. 파일 업로드, 긴 데이터 처리, 단계가 있는 작업처럼 시간이 오래 걸리는 작업에 사용한다.

Q. 진행률을 모르면 어떻게 해?
A. Indeterminate Progress나 단계 문구를 제공한다.

Q. Progress와 Spinner는 뭐가 달라?
A. Spinner는 짧은 대기 상태이고, Progress는 긴 작업의 진행 상태를 보여준다.

Q. 긴 작업 성공 후에는 무엇이 필요해?
A. Success State 또는 Success Toast로 완료 여부를 알려야 한다.

---

## 2.5 Loading State Mistakes

### [개념]

Loading State Mistakes는 처리 중 상태를 누락하거나 부적절한 loading UI를 사용하는 실수다.

Loading 실수는 중복 요청, 사용자 혼란, 무한 대기 문제를 만든다.

---

### [핵심]

자주 발생하는 실수:

- Loading State 없음
- Button loading 중 중복 클릭 가능
- 페이지 전체 Spinner만 남발
- 목록 로딩에 Skeleton 없이 빈 화면 표시
- 무한 Spinner 방치
- loading 실패 후 Error State 없음
- loading 중 기존 데이터 제거로 화면 깜빡임
- 너무 짧은 작업에 과도한 full page loading
- progress 필요한 긴 작업에 Spinner만 사용
- loading message 없음
- reduced motion 고려 없음

---

### [실무]

Troubleshooting:

```text
저장 버튼이 여러 번 눌림
→ Button Loading + disabled 확인

목록 로딩 중 빈 화면
→ Skeleton List 추가

계속 Spinner만 보임
→ timeout / error state 확인

파일 업로드 상태가 불명확
→ Progress Bar 추가

페이지가 자주 깜빡임
→ 기존 데이터 유지 + section loading 검토
```

Review Checklist:

```md
- [ ] loading이 필요한 요청에 상태가 있는가?
- [ ] 중복 action이 방지되는가?
- [ ] skeleton / spinner / progress 선택이 적절한가?
- [ ] 실패 시 Error State로 전환되는가?
- [ ] 무한 loading이 방치되지 않는가?
```

---

### [FAQ]

Q. Loading State에서 가장 흔한 실수는?
A. loading 상태를 만들지 않거나, loading 중 중복 클릭을 막지 않는 것이다.

Q. 무한 Spinner는 왜 문제야?
A. 사용자는 처리 중인지 실패인지 알 수 없고 복구 행동을 할 수 없다.

Q. 목록 로딩 중 빈 화면이어도 돼?
A. 권장하지 않는다. Skeleton이나 Loading State를 제공해야 한다.

Q. 저장 중 버튼을 그대로 활성화해도 돼?
A. 안 된다. 중복 저장 요청이 발생할 수 있다.

---

# 3. Empty State Pattern

## 3.1 Empty State Definition

### [개념]

Empty State는 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 UI 패턴이다.

Empty State는 오류가 아니라 데이터가 없는 정상 상태를 사용자에게 설명하고 다음 행동을 안내한다.

---

### [핵심]

Empty State 구성:

```text
Title
→ Description
→ Optional Action
```

Empty State 사용 대상:

- 검색 결과 없음
- 필터 결과 없음
- 찜 목록 없음
- 리뷰 없음
- 알림 없음
- 채팅 없음
- 테이블 데이터 없음
- 등록된 사용자 없음
- 생산 이력 없음
- 불량 이력 없음
- 설비 알람 이력 없음
- LOT 목록 없음

Empty State 기준:

- 빈 화면만 표시 금지
- 사용자 친화적 title 제공
- 다음 행동 안내
- 필요한 경우 action button 제공
- Error State와 구분
- 검색 / 필터 context 반영

---

### [실무]

기본 Empty State 예:

```jsx
<EmptyState
  title="데이터가 없습니다"
  description="아직 등록된 항목이 없습니다."
/>
```

검색 Empty State 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다"
  description="다른 키워드나 조건으로 다시 검색해 보세요."
  action={<Button variant="secondary">필터 초기화</Button>}
/>
```

테이블 Empty State 예:

```jsx
<TableEmptyState
  title="등록된 사용자가 없습니다"
  description="관리자 계정으로 사용자를 등록해 주세요."
  action={<Button variant="primary">사용자 등록</Button>}
/>
```

---

### [FAQ]

Q. Empty State가 뭐야?
A. 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 UI 패턴이다.

Q. Empty State에는 무엇이 들어가야 해?
A. 데이터가 없다는 설명과 사용자가 다음에 할 수 있는 행동이 들어가면 좋다.

Q. 데이터가 없으면 빈 화면이면 안 돼?
A. 안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터 없음이고, Error State는 요청 실패나 처리 오류다.

---

## 3.2 Search Empty State

### [개념]

Search Empty State는 검색 요청은 성공했지만 검색 결과가 없을 때 보여주는 Empty State다.

검색 결과 없음은 사용자가 조건을 조정할 수 있도록 안내해야 한다.

---

### [핵심]

Search Empty State 구성:

- 검색 결과 없음 title
- 검색어 또는 조건 반영
- 다른 키워드 제안
- 필터 초기화 action
- 이전 목록으로 돌아가기 action
- 오타 가능성 안내
- 너무 기술적인 메시지 금지

좋은 문구:

```text
검색 결과가 없습니다.
다른 키워드나 조건으로 다시 검색해 보세요.
```

나쁜 문구:

```text
No data.
0 results.
null
```

---

### [실무]

검색 Empty State 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다"
  description={`"${keyword}"에 대한 결과를 찾지 못했습니다. 다른 키워드로 검색해 보세요.`}
  action={
    <Button variant="secondary" onClick={resetSearch}>
      검색 초기화
    </Button>
  }
/>
```

필터 Empty State 예:

```jsx
<EmptyState
  title="조건에 맞는 항목이 없습니다"
  description="필터를 줄이거나 조건을 변경해 보세요."
  action={
    <Button variant="secondary" onClick={resetFilters}>
      필터 초기화
    </Button>
  }
/>
```

Review 기준:

```md
- [ ] 검색 결과 없음 상태가 있는가?
- [ ] 검색어 또는 필터 context가 반영되는가?
- [ ] 필터 초기화 같은 다음 action이 있는가?
- [ ] 오류 상태와 혼동되지 않는가?
```

---

### [FAQ]

Q. Search Empty State는 언제 필요해?
A. 검색 요청은 성공했지만 결과가 0개일 때 필요하다.

Q. 검색 결과가 없을 때 어떤 action이 좋아?
A. 필터 초기화, 검색어 변경, 전체 목록 보기 같은 action이 좋다.

Q. 검색 결과 없음은 Error State야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. 필터 결과 없음도 Empty State야?
A. 그렇다. 조건에 맞는 데이터가 없는 정상 상태다.

---

## 3.3 Table Empty State

### [개념]

Table Empty State는 테이블 데이터가 없을 때 빈 tbody 대신 사용자에게 상태와 다음 행동을 안내하는 패턴이다.

관리자 목록, 생산 이력, LOT 목록, 알람 이력 같은 테이블에는 Empty State가 필요하다.

---

### [핵심]

Table Empty State 사용 대상:

- 사용자 목록 없음
- LOT 목록 없음
- 생산 이력 없음
- 불량 이력 없음
- 설비 알람 이력 없음
- 결제 내역 없음
- 검색 결과 없음
- 필터 결과 없음

Table Empty State 기준:

- 빈 tbody만 표시 금지
- table context 유지
- column span 처리
- title / description 제공
- 필요한 경우 등록 action 제공
- 검색 / 필터 결과 없음 구분
- loading과 empty 구분

---

### [실무]

Table Empty State 예:

```jsx
<tbody>
  <tr>
    <td colSpan={5}>
      <EmptyState
        title="등록된 LOT가 없습니다"
        description="생산 지시를 등록하면 LOT 목록이 표시됩니다."
        action={<Button variant="primary">생산 지시 등록</Button>}
      />
    </td>
  </tr>
</tbody>
```

검색 Table Empty State 예:

```jsx
<tbody>
  <tr>
    <td colSpan={6}>
      <EmptyState
        title="조건에 맞는 이력이 없습니다"
        description="기간이나 설비 조건을 변경해 보세요."
        action={<Button variant="secondary">필터 초기화</Button>}
      />
    </td>
  </tr>
</tbody>
```

Review 기준:

```md
- [ ] Table Empty State가 있는가?
- [ ] loading과 empty를 구분하는가?
- [ ] colSpan이 올바른가?
- [ ] 다음 action이 필요한 경우 제공되는가?
```

---

### [FAQ]

Q. Table Empty State는 왜 필요해?
A. 빈 테이블만 보여주면 사용자가 데이터가 없는지 오류인지 알 수 없기 때문이다.

Q. 빈 tbody만 두면 안 돼?
A. 권장하지 않는다. Empty State 문구를 제공해야 한다.

Q. Table Empty State에 버튼이 꼭 필요해?
A. 필수는 아니지만 등록이나 필터 초기화 같은 다음 행동이 있으면 좋다.

Q. Table Loading과 Empty는 어떻게 구분해?
A. 요청 중이면 Loading, 요청 성공 후 데이터가 없으면 Empty State다.

---

## 3.4 Empty State Message Rules

### [개념]

Empty State Message Rules는 데이터 없음 상태에서 사용자에게 보여줄 title, description, action 문구 기준이다.

Empty State 문구는 짧고 명확하며 다음 행동을 안내해야 한다.

---

### [핵심]

문구 구조:

```text
상태 설명
→ 맥락 설명
→ 다음 행동
```

좋은 Empty State 문구:

```text
검색 결과가 없습니다.
다른 키워드나 조건으로 다시 검색해 보세요.
```

```text
등록된 사용자가 없습니다.
관리자 계정으로 사용자를 등록해 주세요.
```

나쁜 Empty State 문구:

```text
없음
No data
0
null
데이터 미존재
```

---

### [실무]

도메인별 문구 예:

```text
등록된 LOT가 없습니다.
생산 지시를 등록하면 LOT 목록이 표시됩니다.
```

```text
불량 이력이 없습니다.
선택한 기간에 등록된 불량 이력이 없습니다.
```

```text
알림이 없습니다.
새로운 알림이 생기면 이곳에 표시됩니다.
```

Review 기준:

```md
- [ ] Empty State title이 명확한가?
- [ ] description이 다음 행동을 안내하는가?
- [ ] 기술 용어가 과하지 않은가?
- [ ] Error State처럼 보이지 않는가?
```

---

### [FAQ]

Q. Empty State 문구는 어떻게 작성해?
A. 데이터가 없다는 사실과 사용자가 다음에 할 수 있는 행동을 짧고 명확하게 작성한다.

Q. “No data”라고만 써도 돼?
A. 권장하지 않는다. 사용자가 맥락과 다음 행동을 알기 어렵다.

Q. Empty State에 기술 용어를 써도 돼?
A. 사용자 화면에서는 최소화한다. 사용자가 이해할 수 있는 문장을 우선한다.

Q. Empty State는 실패처럼 보여야 해?
A. 아니다. 요청 성공 후 데이터가 없는 정상 상태로 보여야 한다.

---

## 3.5 Empty State Mistakes

### [개념]

Empty State Mistakes는 데이터 없음 상태를 빈 화면이나 오류처럼 처리하는 실수다.

Empty State 실수는 사용자가 화면 상태를 이해하지 못하게 만든다.

---

### [핵심]

자주 발생하는 실수:

- 빈 화면만 표시
- 빈 table body만 표시
- 검색 결과 없음과 오류를 혼동
- “No data”만 표시
- 다음 action 없음
- 필터 초기화 action 없음
- loading과 empty 구분 실패
- Empty State를 error 색상으로 표시
- 도메인 context 없는 문구
- 빈 목록에서 layout 깨짐
- Empty State에도 raw error 문구 사용

---

### [실무]

Troubleshooting:

```text
검색 결과가 없는데 오류처럼 보임
→ Search Empty State로 변경

테이블이 빈 화면임
→ Table Empty State 추가

필터 결과가 없음
→ 필터 초기화 action 제공

데이터 없음인지 로딩 중인지 불명확
→ loading / empty 조건 분리

문구가 너무 짧음
→ title + description 구조 적용
```

Review Checklist:

```md
- [ ] 데이터 없음 상태가 명확한가?
- [ ] loading과 empty가 구분되는가?
- [ ] 검색 / 필터 context가 반영되는가?
- [ ] 다음 action이 필요한 경우 제공되는가?
- [ ] Empty State가 오류처럼 보이지 않는가?
```

---

### [FAQ]

Q. Empty State에서 가장 흔한 실수는?
A. 데이터가 없을 때 빈 화면만 보여주거나 “No data”만 표시하는 것이다.

Q. 검색 결과 없음은 오류처럼 보여도 돼?
A. 안 된다. 검색 결과 없음은 정상 상태이므로 Empty State로 표현해야 한다.

Q. Empty State에 action이 없으면 무조건 문제야?
A. 항상은 아니지만 사용자가 다음 행동을 할 수 있는 경우 action을 제공하는 것이 좋다.

Q. loading과 empty를 같은 UI로 처리해도 돼?
A. 권장하지 않는다. 처리 중 상태와 데이터 없음 상태는 의미가 다르다.

---

# 4. Error State Pattern

## 4.1 Error State Definition

### [개념]

Error State는 요청 실패, 처리 오류, 권한 문제, 인증 문제, 네트워크 오류, 검증 실패가 발생했을 때 사용자에게 문제와 복구 방법을 안내하는 UI 패턴이다.

Error State는 개발자용 오류를 노출하는 영역이 아니라 사용자가 이해하고 행동할 수 있게 만드는 피드백 패턴이다.

---

### [핵심]

Error State 구성:

```text
Error Title
→ User Friendly Message
→ Recovery Action
→ Optional Detail
```

Error State 사용 대상:

- 데이터 로드 실패
- 저장 실패
- 삭제 실패
- 네트워크 오류
- 서버 오류
- 인증 필요
- 권한 없음
- 유효성 검증 실패
- 파일 업로드 실패
- 외부 API 실패

Error State 기준:

- raw error 그대로 노출 금지
- 사용자 친화적 메시지 사용
- 가능한 경우 retry action 제공
- 인증 오류는 로그인 이동 제공
- 권한 오류는 접근 불가 안내
- 입력 오류는 필드 가까이에 표시
- 중요한 오류는 Toast만으로 처리 금지

---

### [실무]

Page Error State 예:

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

Permission Error 예:

```jsx
<ErrorState
  title="접근 권한이 없습니다"
  description="이 화면은 관리자 권한이 있어야 사용할 수 있습니다."
/>
```

Authentication Error 예:

```jsx
<ErrorState
  title="로그인이 필요합니다"
  description="이 기능을 사용하려면 먼저 로그인해 주세요."
  action={<Button onClick={goToLogin}>로그인하기</Button>}
/>
```

---

### [FAQ]

Q. Error State가 뭐야?
A. 요청 실패나 처리 오류가 발생했을 때 문제와 복구 방법을 안내하는 UI 패턴이다.

Q. Error State에는 무엇이 필요해?
A. 사용자 친화적 title, 설명, 가능한 경우 복구 action이 필요하다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 민감한 정보가 포함될 수 있으므로 사용자 친화 메시지로 바꿔야 한다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?
A. 권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State도 함께 제공하는 것이 좋다.

---

## 4.2 Network Server Error Pattern

### [개념]

Network Server Error Pattern은 네트워크 연결 실패, 서버 오류, 타임아웃, 외부 API 실패 상황을 사용자에게 안내하는 Error State다.

---

### [핵심]

대상 오류:

- Network Error
- Timeout
- 500 Server Error
- 502 Bad Gateway
- 503 Service Unavailable
- External API Failure
- Connection Failed

메시지 기준:

```text
기술적 원인 직접 노출
→ 최소화

사용자 행동
→ 다시 시도 / 네트워크 확인 / 잠시 후 재시도

복구 가능
→ Retry Action 제공
```

좋은 메시지:

```text
데이터를 불러오지 못했습니다.
네트워크 상태를 확인한 뒤 다시 시도해 주세요.
```

나쁜 메시지:

```text
AxiosError: Request failed with status code 500
SQLSyntaxErrorException
Internal Server Error
```

---

### [실무]

Network Error 예:

```jsx
<ErrorState
  title="연결에 문제가 있습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

Server Error 예:

```jsx
<ErrorState
  title="요청을 처리하지 못했습니다"
  description="잠시 후 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

Review 기준:

```md
- [ ] raw error를 그대로 노출하지 않는가?
- [ ] retry action이 필요한 경우 제공되는가?
- [ ] 사용자에게 원인과 다음 행동을 안내하는가?
- [ ] Error State가 화면 문맥 안에 표시되는가?
```

---

### [FAQ]

Q. Network Error는 어떻게 보여줘?
A. 네트워크 상태를 확인하고 다시 시도할 수 있도록 사용자 친화 메시지와 retry action을 제공한다.

Q. 500 서버 오류는 그대로 보여줘도 돼?
A. 권장하지 않는다. “요청을 처리하지 못했습니다. 잠시 후 다시 시도해 주세요.”처럼 표현한다.

Q. Retry 버튼은 항상 필요해?
A. 재시도 가능한 오류에는 권장된다.

Q. AxiosError를 화면에 보여줘도 돼?
A. 안 된다. 개발자용 오류는 사용자에게 직접 노출하지 않는다.

---

## 4.3 Authentication Permission Error Pattern

### [개념]

Authentication Permission Error Pattern은 로그인 필요, 세션 만료, 권한 없음, 접근 제한 상황을 안내하는 Error State다.

인증 오류와 권한 오류는 사용자에게 가능한 다음 행동을 명확히 제공해야 한다.

---

### [핵심]

구분:

```text
Authentication Error
→ 로그인 필요
→ 세션 만료
→ 인증 정보 없음

Permission Error
→ 로그인은 되었지만 권한 부족
→ 관리자 권한 필요
→ 접근 제한
```

Action 기준:

```text
로그인 필요
→ 로그인하기

세션 만료
→ 다시 로그인하기

권한 없음
→ 이전 화면으로 돌아가기 / 관리자에게 문의

관리자 권한 필요
→ 권한 요청 또는 안내
```

---

### [실무]

로그인 필요 예:

```jsx
<ErrorState
  title="로그인이 필요합니다"
  description="이 기능을 사용하려면 먼저 로그인해 주세요."
  action={<Button onClick={goToLogin}>로그인하기</Button>}
/>
```

세션 만료 예:

```jsx
<ErrorState
  title="로그인이 만료되었습니다"
  description="계속 사용하려면 다시 로그인해 주세요."
  action={<Button onClick={goToLogin}>다시 로그인하기</Button>}
/>
```

권한 없음 예:

```jsx
<ErrorState
  title="접근 권한이 없습니다"
  description="관리자 권한이 필요한 화면입니다."
  action={
    <Button variant="secondary" onClick={goBack}>
      이전으로 돌아가기
    </Button>
  }
/>
```

---

### [FAQ]

Q. Authentication Error와 Permission Error는 뭐가 달라?
A. Authentication Error는 로그인 상태 문제이고, Permission Error는 로그인은 되었지만 권한이 부족한 상태다.

Q. 로그인 필요 오류에는 어떤 action이 좋아?
A. 로그인하기 버튼이 적합하다.

Q. 권한 없음 오류에는 어떤 메시지가 좋아?
A. 접근 권한이 없다는 사실과 필요한 권한 또는 다음 행동을 안내해야 한다.

Q. 세션 만료는 Toast만으로 알려도 돼?
A. 중요한 흐름이면 로그인 이동을 포함한 Error State나 Modal 안내가 필요할 수 있다.

---

## 4.4 Form Validation Error Pattern

### [개념]

Form Validation Error Pattern은 사용자의 입력값이 유효하지 않을 때 입력 필드 가까이에 오류를 표시하는 패턴이다.

Form Validation Error는 field-level error와 form-level error를 구분해야 한다.

---

### [핵심]

Validation Error 종류:

```text
Field-level Error
→ 특정 입력 필드 오류

Form-level Error
→ 전체 제출 실패 또는 여러 필드 관련 오류

Server Validation Error
→ 서버 검증 실패

Required Error
→ 필수값 누락

Format Error
→ 이메일, 전화번호, 숫자 형식 오류
```

Field Error 기준:

- input 가까이에 표시
- label / input / error message 연결
- aria-invalid 사용
- aria-describedby 사용
- 색상만으로 표시 금지
- 사용자 친화 문구 사용

---

### [실무]

Field Error 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid={Boolean(emailError)}
  aria-describedby={emailError ? "email-error" : undefined}
/>
{emailError && (
  <p id="email-error" role="alert">
    올바른 이메일 형식이 아닙니다.
  </p>
)}
```

Form-level Error 예:

```jsx
<Alert variant="error" title="저장하지 못했습니다">
  입력 내용을 확인한 뒤 다시 시도해 주세요.
</Alert>
```

Review 기준:

```md
- [ ] field error가 input 가까이에 표시되는가?
- [ ] aria-invalid가 적용되는가?
- [ ] error message와 input이 연결되는가?
- [ ] form-level error와 field-level error가 구분되는가?
```

---

### [FAQ]

Q. Form Validation Error는 어디에 표시해야 해?
A. 가능하면 오류가 발생한 입력 필드 가까이에 표시해야 한다.

Q. Form-level Error와 Field-level Error는 뭐가 달라?
A. Field-level Error는 특정 입력 오류이고, Form-level Error는 전체 제출 실패나 공통 오류다.

Q. error border만 있으면 충분해?
A. 아니다. error message와 aria 속성 연결이 필요하다.

Q. 서버 검증 오류도 Form에 표시해야 해?
A. 해야 한다. 가능한 경우 해당 필드에 연결하고, 공통 오류는 Alert로 표시한다.

---

## 4.5 Error Message Rules

### [개념]

Error Message Rules는 오류 상황에서 사용자에게 보여줄 문구 작성 기준이다.

Error Message는 개발자용 오류가 아니라 사용자가 이해하고 다음 행동을 할 수 있는 문장이어야 한다.

---

### [핵심]

좋은 Error Message 기준:

- 짧고 명확함
- 사용자 행동 안내
- 기술 용어 최소화
- raw error 노출 금지
- 책임 전가 표현 금지
- 복구 가능성 안내
- 위험하거나 민감한 정보 노출 금지
- 필드 오류는 구체적으로 작성

좋은 예:

```text
데이터를 불러오지 못했습니다.
네트워크 상태를 확인한 뒤 다시 시도해 주세요.
```

```text
올바른 이메일 형식이 아닙니다.
```

나쁜 예:

```text
Error occurred.
Bad Request.
500 Internal Server Error.
SQL constraint violation.
```

---

### [실무]

상황별 문구:

```text
저장 실패
→ 저장하지 못했습니다. 입력 내용을 확인한 뒤 다시 시도해 주세요.

삭제 실패
→ 삭제하지 못했습니다. 잠시 후 다시 시도해 주세요.

권한 없음
→ 접근 권한이 없습니다. 관리자 권한이 필요한 화면입니다.

로그인 필요
→ 로그인이 필요합니다. 먼저 로그인해 주세요.

검색 실패
→ 검색 결과를 불러오지 못했습니다. 다시 시도해 주세요.
```

Review 기준:

```md
- [ ] raw error가 노출되지 않는가?
- [ ] 사용자가 이해할 수 있는 문장인가?
- [ ] 복구 action이 필요한 경우 안내되는가?
- [ ] 오류 원인을 과도하게 기술적으로 설명하지 않는가?
```

---

### [FAQ]

Q. Error Message는 어떻게 작성해?
A. 사용자가 이해할 수 있는 문장으로 실패 상황과 다음 행동을 안내한다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 민감한 정보가 포함될 수 있으므로 사용자 친화 메시지로 바꿔야 한다.

Q. Error Message는 자세할수록 좋아?
A. 아니다. 사용자가 이해하고 행동할 수 있을 만큼만 명확히 쓰는 것이 좋다.

Q. “Error occurred”라고 써도 돼?
A. 권장하지 않는다. 어떤 문제가 있었고 무엇을 하면 되는지 알려줘야 한다.

---

## 4.6 Error State Mistakes

### [개념]

Error State Mistakes는 오류를 사용자에게 제대로 전달하지 못하거나 복구 행동을 제공하지 않는 실수다.

Error State 실수는 사용자 흐름을 중단시키고 문제 해결을 어렵게 만든다.

---

### [핵심]

자주 발생하는 실수:

- console.log만 하고 UI Error State 없음
- raw error 그대로 노출
- 500 / 400 같은 코드만 표시
- retry action 없음
- 중요한 오류를 Toast만으로 표시
- form field error를 상단에만 표시
- error를 색상만으로 표시
- 인증 오류와 권한 오류 혼동
- Empty State를 Error State처럼 표시
- 서버 오류와 사용자 입력 오류 혼동
- Error 후 loading 상태가 계속 유지됨
- 복구 방법 없음

---

### [실무]

Troubleshooting:

```text
사용자가 실패 원인을 모름
→ 사용자 친화 Error Message 추가

다시 시도할 수 없음
→ Retry Action 추가

입력 오류 위치를 모름
→ Field-level Error 추가

권한 오류가 로그인 오류처럼 보임
→ Authentication / Permission 구분

오류 후 계속 loading
→ loading false 처리 + Error State 전환
```

Review Checklist:

```md
- [ ] 오류가 UI에 표시되는가?
- [ ] raw error가 노출되지 않는가?
- [ ] 복구 action이 필요한 경우 제공되는가?
- [ ] field error와 form error가 구분되는가?
- [ ] 중요한 오류가 Toast만으로 처리되지 않는가?
```

---

### [FAQ]

Q. Error State에서 가장 흔한 실수는?
A. console.log만 하고 사용자에게 오류와 복구 방법을 보여주지 않는 것이다.

Q. Error는 console.log만 해도 돼?
A. 안 된다. 사용자에게 실패 상태와 복구 방법을 알려야 한다.

Q. 중요한 오류를 Toast만으로 보여주면 왜 문제야?
A. Toast는 사라질 수 있어 사용자가 문제와 복구 방법을 놓칠 수 있다.

Q. Error 후 loading이 계속되면 왜 문제야?
A. 사용자가 실패인지 처리 중인지 알 수 없고 다음 행동을 할 수 없다.

---

# 5. Success State Pattern

## 5.1 Success State Definition

### [개념]

Success State는 사용자의 작업이 성공했음을 알려주는 UI 패턴이다.

Success State는 저장, 삭제, 로그인, 회원가입, 등록, 결제, 업로드 같은 작업 완료 후 사용자가 결과를 확신할 수 있게 한다.

---

### [핵심]

Success State 사용 상황:

- 저장 완료
- 삭제 완료
- 로그인 성공
- 회원가입 완료
- 리뷰 등록 완료
- 결제 완료
- 복사 완료
- 업로드 완료
- 권한 변경 완료
- 생산 지시 등록 완료
- LOT 생성 완료

Success Feedback 종류:

```text
Toast
→ 가벼운 작업 성공

Alert
→ 화면 문맥 안 성공 안내

Success Page
→ 중요한 완료 화면

Inline Success
→ Form Field 검증 성공

State Update
→ 목록 / 카드 / 테이블 갱신
```

---

### [실무]

Success Toast 예:

```jsx
showToast({
  variant: "success",
  message: "저장되었습니다.",
});
```

삭제 성공 예:

```jsx
showToast({
  variant: "success",
  message: "삭제되었습니다.",
});
```

중요 완료 화면 예:

```jsx
<SuccessState
  title="회원가입이 완료되었습니다"
  description="로그인 후 서비스를 이용할 수 있습니다."
  action={<Button onClick={goToLogin}>로그인하기</Button>}
/>
```

Review 기준:

```md
- [ ] 성공 후 사용자에게 완료 여부가 전달되는가?
- [ ] 필요한 경우 목록 / 상태가 갱신되는가?
- [ ] 과도한 success toast를 남발하지 않는가?
- [ ] 중요한 완료에는 다음 action이 제공되는가?
```

---

### [FAQ]

Q. Success State는 언제 필요해?
A. 저장, 삭제, 로그인, 회원가입, 리뷰 등록 같은 작업 성공을 알려야 할 때 필요하다.

Q. 성공 메시지는 꼭 필요해?
A. 사용자가 작업 완료를 확신해야 하는 경우 필요하다.

Q. 모든 성공에 Toast를 띄워도 돼?
A. 과하면 방해가 될 수 있다. 중요한 행동 중심으로 사용한다.

Q. 성공 후 목록 갱신도 Feedback이야?
A. 그렇다. 사용자가 결과가 반영되었음을 확인할 수 있어야 한다.

---

## 5.2 Success Toast Pattern

### [개념]

Success Toast Pattern은 가벼운 작업 성공을 짧게 알려주는 패턴이다.

저장, 삭제, 복사, 등록 같은 action 후 사용자가 즉시 결과를 알 수 있게 한다.

---

### [핵심]

Success Toast 사용 대상:

- 저장 완료
- 삭제 완료
- 복사 완료
- 등록 완료
- 수정 완료
- 권한 변경 완료
- 간단한 설정 변경 완료

문구 기준:

```text
저장되었습니다.
삭제되었습니다.
등록되었습니다.
수정되었습니다.
복사되었습니다.
권한이 변경되었습니다.
```

주의:

- 너무 많은 Toast 남발 금지
- 긴 설명 금지
- 중요한 완료는 Success Page 고려
- 성공 후 실제 상태 갱신 필요
- 실패를 success toast로 표시 금지

---

### [실무]

Success Toast 예:

```jsx
showToast({
  variant: "success",
  message: "등록되었습니다.",
});
```

상태 갱신 포함 Flow:

```text
Submit
→ API Success
→ Toast 표시
→ Form Reset
→ List Refetch or Local Update
```

Review 기준:

```md
- [ ] 성공 Toast 문구가 짧고 명확한가?
- [ ] 성공 후 실제 UI 상태가 갱신되는가?
- [ ] 너무 많은 Toast가 동시에 표시되지 않는가?
- [ ] variant가 success와 일치하는가?
```

---

### [FAQ]

Q. Success Toast는 언제 써?
A. 저장, 삭제, 복사, 등록처럼 가벼운 작업 성공을 짧게 알려줄 때 사용한다.

Q. Success Toast 문구는 어떻게 써?
A. “저장되었습니다”, “삭제되었습니다”처럼 짧고 명확하게 작성한다.

Q. 성공 Toast만 띄우고 목록 갱신을 안 해도 돼?
A. 안 된다. 사용자는 실제 결과가 화면에 반영된 것을 확인할 수 있어야 한다.

Q. 중요한 완료에도 Toast만 써도 돼?
A. 회원가입 완료, 결제 완료 같은 중요한 완료는 Success Page나 명확한 다음 action을 고려한다.

---

## 5.3 Success Page Pattern

### [개념]

Success Page Pattern은 중요한 작업이 완료된 뒤 별도 완료 화면이나 완료 상태를 보여주는 패턴이다.

Success Page는 회원가입, 결제, 신청 완료, 대규모 제출 같은 중요 흐름에 적합하다.

---

### [핵심]

Success Page 사용 대상:

- 회원가입 완료
- 결제 완료
- 신청 완료
- 주문 완료
- 생산 지시 등록 완료
- 파일 업로드 완료
- 중요한 설정 완료

Success Page 구성:

```text
Success Title
→ Completion Description
→ Summary
→ Next Action
```

기준:

- 완료 사실 명확화
- 다음 행동 제공
- 필요한 경우 결과 요약 제공
- 성공 상태를 error / warning과 구분
- 사용자가 이전 화면으로 돌아갈 수 있게 함

---

### [실무]

Success Page 예:

```jsx
<SuccessState
  title="생산 지시가 등록되었습니다"
  description="등록된 생산 지시는 LOT 목록에서 확인할 수 있습니다."
  action={<Button onClick={goToLots}>LOT 목록 보기</Button>}
/>
```

결제 완료 예:

```jsx
<SuccessState
  title="결제가 완료되었습니다"
  description="결제 내역은 마이페이지에서 확인할 수 있습니다."
  action={<Button onClick={goToMyPage}>내역 확인</Button>}
/>
```

Review 기준:

```md
- [ ] 중요한 완료에 명확한 Success State가 있는가?
- [ ] 다음 action이 제공되는가?
- [ ] 결과 요약이 필요한 경우 제공되는가?
- [ ] 완료 후 사용자가 흐름을 이어갈 수 있는가?
```

---

### [FAQ]

Q. Success Page는 언제 필요해?
A. 회원가입, 결제, 신청 완료처럼 중요한 완료 흐름에 필요하다.

Q. Success Page에는 무엇이 들어가야 해?
A. 완료 title, 설명, 결과 요약, 다음 action이 들어가면 좋다.

Q. 저장 성공에도 Success Page가 필요해?
A. 대부분은 Toast로 충분하다. 중요한 흐름일 때 Success Page를 사용한다.

Q. Success Page에 다음 action이 필요한 이유는?
A. 사용자가 완료 후 어디로 가야 하는지 알 수 있어야 하기 때문이다.

---

## 5.4 Success State Mistakes

### [개념]

Success State Mistakes는 성공 결과를 사용자에게 명확히 전달하지 못하거나 실제 UI 상태를 갱신하지 않는 실수다.

---

### [핵심]

자주 발생하는 실수:

- 성공 피드백 없음
- Toast는 표시했지만 목록 갱신 없음
- 성공 메시지가 모호함
- 모든 성공에 Toast 남발
- 중요한 완료를 Toast만으로 처리
- 성공 후 다음 action 없음
- success variant와 메시지 불일치
- 저장 성공 후 form loading 유지
- 삭제 성공 후 삭제된 항목이 화면에 남음
- 성공과 실패 상태가 같은 UI로 표시됨

---

### [실무]

Troubleshooting:

```text
저장 성공했는지 모름
→ Success Toast 추가

삭제 후 항목이 남아 있음
→ 목록 refetch 또는 local update

회원가입 후 다음 행동 모름
→ Success Page + 로그인 action

Toast가 너무 많음
→ 중요한 action 중심으로 제한

성공 후 button loading 유지
→ success 후 loading false 처리
```

Review Checklist:

```md
- [ ] 성공 후 완료 피드백이 있는가?
- [ ] 실제 UI 상태가 갱신되는가?
- [ ] 중요한 완료에는 다음 action이 있는가?
- [ ] Toast가 과도하지 않은가?
- [ ] 성공과 실패 UI가 명확히 구분되는가?
```

---

### [FAQ]

Q. Success State에서 가장 흔한 실수는?
A. 성공 Toast는 띄우지만 실제 목록이나 화면 상태를 갱신하지 않는 것이다.

Q. 성공 피드백이 없어도 사용자가 알 수 있지 않아?
A. 항상 그렇지 않다. 저장, 삭제, 등록 같은 작업은 완료 피드백이 필요하다.

Q. 성공 후 loading 상태가 계속되면 왜 문제야?
A. 사용자가 작업이 끝났는지 알 수 없고 중복 행동이 막힐 수 있다.

Q. 모든 성공을 크게 보여줘야 해?
A. 아니다. 가벼운 성공은 Toast, 중요한 완료는 Success Page가 적합하다.

---

# 6. Disabled Retry Offline Pattern

## 6.1 Disabled State Pattern

### [개념]

Disabled State는 사용자가 현재 조작할 수 없는 상태를 표현하는 패턴이다.

Disabled State는 단순히 흐리게 보이는 스타일이 아니라 실제 조작 차단과 이유 전달을 포함해야 한다.

---

### [핵심]

Disabled State 사용 대상:

- loading 중 button
- 권한 부족 action
- 필수 입력 전 submit
- 선택 조건 미충족
- 비활성 menu item
- 사용 불가 form field
- 이전 / 다음 pagination 경계

기준:

- 실제 disabled 속성 또는 조작 차단 필요
- disabled 이유가 추론 가능해야 함
- 필요한 경우 helper text 제공
- disabled와 readonly 구분
- disabled text contrast 고려
- cursor / focus 정책 명확화
- disabled 상태에서 action 실행 금지

---

### [실무]

Button disabled 예:

```jsx
<Button disabled={!isFormValid}>저장</Button>
```

이유 안내 예:

```jsx
<Button disabled={!canDelete}>
  삭제
</Button>
<p className="helperText">삭제 권한이 없습니다.</p>
```

Pagination disabled 예:

```jsx
<Button disabled={currentPage === 1}>이전</Button>
```

Review 기준:

```md
- [ ] disabled 상태에서 실제 action이 차단되는가?
- [ ] disabled 이유가 명확한가?
- [ ] disabled와 readonly를 구분하는가?
- [ ] disabled text가 읽을 수 있는가?
```

---

### [FAQ]

Q. Disabled State는 뭐야?
A. 사용자가 현재 조작할 수 없는 상태를 표현하는 패턴이다.

Q. disabled 스타일만 있으면 충분해?
A. 아니다. 실제 조작이 차단되어야 한다.

Q. disabled 이유를 꼭 보여줘야 해?
A. 상황에 따라 필요하다. 사용자가 왜 사용할 수 없는지 모르면 혼란이 생긴다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있다.

---

## 6.2 Retry Pattern

### [개념]

Retry Pattern은 요청 실패 후 사용자가 다시 시도할 수 있게 하는 복구 action 패턴이다.

Retry Pattern은 네트워크 오류, 서버 오류, 데이터 로드 실패처럼 재시도 가능성이 있는 오류에 필요하다.

---

### [핵심]

Retry Pattern 사용 대상:

- 네트워크 오류
- 서버 일시 오류
- 데이터 로드 실패
- 외부 API 실패
- 파일 업로드 실패
- 검색 요청 실패
- 목록 조회 실패

Retry 기준:

- Error State 안에 Retry Button 제공
- retry 중 loading state 제공
- retry 실패 시 error 유지
- retry 성공 시 content render
- 중복 retry 방지
- 사용자가 직접 해결할 수 없는 오류에는 다른 안내 제공

---

### [실무]

Retry 예:

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="잠시 후 다시 시도해 주세요."
  action={
    <Button onClick={refetch} isLoading={isRetrying}>
      다시 시도
    </Button>
  }
/>
```

Retry Flow:

```text
Request Failed
→ Error State
→ Retry Click
→ Retry Loading
→ Success Content or Error State
```

Review 기준:

```md
- [ ] 재시도 가능한 오류에 Retry Action이 있는가?
- [ ] retry 중 loading state가 있는가?
- [ ] retry 중 중복 클릭이 방지되는가?
- [ ] retry 성공 후 content로 전환되는가?
```

---

### [FAQ]

Q. Retry Pattern은 언제 필요해?
A. 네트워크 오류나 일시적 서버 오류처럼 다시 시도하면 해결될 수 있는 경우 필요하다.

Q. 모든 오류에 Retry 버튼이 필요해?
A. 아니다. 권한 없음이나 입력 오류처럼 재시도로 해결되지 않는 경우에는 적절하지 않다.

Q. retry 중에도 loading이 필요해?
A. 필요하다. 중복 retry를 막고 처리 중임을 알려야 한다.

Q. Retry 버튼 문구는 뭐가 좋아?
A. “다시 시도”가 명확하고 일반적으로 적합하다.

---

## 6.3 Offline State Pattern

### [개념]

Offline State는 네트워크 연결이 끊겼거나 요청을 수행할 수 없는 상태를 사용자에게 알려주는 패턴이다.

Offline State는 네트워크 의존 기능에서 사용자 혼란을 줄이고 복구 행동을 안내한다.

---

### [핵심]

Offline State 사용 대상:

- 네트워크 연결 없음
- 서버 연결 불가
- 실시간 연결 끊김
- WebSocket 연결 실패
- TCP/IP 장비 연결 끊김 UI 표시
- 동기화 실패
- 외부 API 접근 실패

Offline State 기준:

- 연결 끊김 사실 표시
- 가능한 경우 자동 재연결 상태 표시
- 수동 재시도 action 제공
- 오프라인 중 제한되는 기능 안내
- 기존 데이터가 있으면 유지 가능
- 실시간 기능에서는 연결 상태 Badge 제공

---

### [실무]

Offline Banner 예:

```jsx
<Alert variant="warning" title="네트워크 연결이 끊겼습니다">
  연결 상태를 확인한 뒤 다시 시도해 주세요.
</Alert>
```

실시간 연결 상태 예:

```jsx
<Badge variant={isConnected ? "success" : "error"}>
  {isConnected ? "연결됨" : "연결 끊김"}
</Badge>
```

장비 연결 예:

```jsx
<Alert variant="error" title="설비 연결이 끊겼습니다">
  EQ1 장비와 통신할 수 없습니다. 연결 상태를 확인해 주세요.
</Alert>
```

Review 기준:

```md
- [ ] 연결 끊김 상태가 사용자에게 표시되는가?
- [ ] 재연결 또는 다시 시도 action이 있는가?
- [ ] 기존 데이터 유지 정책이 명확한가?
- [ ] 실시간 기능에서 연결 상태가 표시되는가?
```

---

### [FAQ]

Q. Offline State는 언제 필요해?
A. 네트워크 연결이 끊기거나 실시간 연결, 장비 연결, 외부 API 접근이 실패했을 때 필요하다.

Q. Offline State는 Error State와 같아?
A. Offline State는 네트워크 연결 문제에 특화된 Error State로 볼 수 있다.

Q. 실시간 연결 상태는 어떻게 표시해?
A. 연결됨 / 연결 끊김 Badge나 Alert로 표시할 수 있다.

Q. 오프라인 중 기존 데이터를 지워야 해?
A. 항상 그렇지 않다. 기존 데이터를 유지하고 연결 상태를 함께 표시하는 것이 좋을 수 있다.

---

## 6.4 Disabled Retry Offline Mistakes

### [개념]

Disabled Retry Offline Mistakes는 비활성, 재시도, 오프라인 상태를 명확히 처리하지 못하는 실수다.

이 실수는 사용자가 왜 action을 할 수 없는지, 어떻게 복구할 수 있는지 알지 못하게 만든다.

---

### [핵심]

자주 발생하는 실수:

- disabled 스타일만 있고 action 실행 가능
- disabled 이유 설명 없음
- 권한 부족 action을 disabled만 처리
- retry 가능한 오류에 Retry 버튼 없음
- retry 중 중복 클릭 가능
- retry 실패 후 상태 꼬임
- offline 상태 표시 없음
- 실시간 연결 끊김 미표시
- 기존 데이터를 모두 지워 빈 화면 표시
- disabled와 readonly 혼동
- 네트워크 오류와 권한 오류를 같은 UI로 처리

---

### [실무]

Troubleshooting:

```text
버튼이 비활성인데 이유를 모름
→ helper text 또는 tooltip 안내

다시 시도할 방법 없음
→ Retry Button 추가

재시도 중 여러 번 클릭됨
→ retry loading + disabled 처리

실시간 연결이 끊겼는데 모름
→ connection status Badge 추가

네트워크 오류가 빈 화면처럼 보임
→ Offline / Error State로 변경
```

Review Checklist:

```md
- [ ] disabled action이 실제로 차단되는가?
- [ ] disabled 이유가 필요한 경우 설명되는가?
- [ ] retry 가능한 오류에 Retry Action이 있는가?
- [ ] offline 상태가 표시되는가?
- [ ] 실시간 연결 상태가 명확한가?
```

---

### [FAQ]

Q. Disabled State에서 가장 흔한 실수는?
A. 버튼은 흐리게 보이지만 실제 클릭이 가능한 상태로 두는 것이다.

Q. Retry Pattern에서 가장 흔한 실수는?
A. 다시 시도 버튼을 제공하지 않거나 retry 중 중복 클릭을 막지 않는 것이다.

Q. Offline State에서 가장 흔한 실수는?
A. 연결 끊김 상태를 사용자에게 표시하지 않는 것이다.

Q. 네트워크 오류와 권한 오류를 같은 문구로 보여줘도 돼?
A. 권장하지 않는다. 원인과 다음 행동이 다르므로 구분해야 한다.

---

# 7. Feedback Message Rules

## 7.1 UI Message Structure

### [개념]

UI Message Structure는 Loading, Empty, Error, Success 상태에서 사용자에게 보여주는 문구의 구조다.

UI Message는 짧고 명확하며 사용자가 현재 상태와 다음 행동을 이해할 수 있어야 한다.

---

### [핵심]

기본 구조:

```text
상태 설명
→ 이유 또는 맥락
→ 다음 행동
```

상태별 구조:

```text
Loading
→ 무엇을 처리 중인지 설명

Empty
→ 무엇이 없는지 설명 + 다음 행동

Error
→ 무엇이 실패했는지 설명 + 복구 행동

Success
→ 무엇이 완료되었는지 설명

Disabled
→ 왜 사용할 수 없는지 설명

Offline
→ 연결 문제 설명 + 재시도 안내
```

---

### [실무]

좋은 문구:

```text
데이터를 불러오는 중입니다.
```

```text
검색 결과가 없습니다.
다른 키워드나 조건으로 다시 검색해 보세요.
```

```text
저장하지 못했습니다.
입력 내용을 확인한 뒤 다시 시도해 주세요.
```

```text
저장되었습니다.
```

나쁜 문구:

```text
Loading...
No data
Error
Success
Bad Request
```

---

### [FAQ]

Q. UI Message는 어떻게 작성해?
A. 상태 설명, 맥락, 다음 행동을 짧고 명확하게 작성한다.

Q. Loading 문구는 꼭 필요해?
A. 문맥이 불명확하거나 긴 작업이면 필요하다.

Q. Error Message에 기술 용어를 써도 돼?
A. 사용자 화면에서는 최소화하고 이해 가능한 문장을 우선한다.

Q. Success Message는 길게 써야 해?
A. 대부분 짧고 명확한 문구가 좋다. 예: 저장되었습니다.

---

## 7.2 Domain Message Examples

### [개념]

Domain Message Examples는 실제 프로젝트 도메인에서 사용할 수 있는 Feedback Message 예시다.

도메인 예시는 Frontend Agent가 프로젝트 맥락에 맞는 문구를 생성하도록 돕는다.

---

### [핵심]

MES / EV Relay 도메인 예시:

```text
생산 지시를 불러오는 중입니다.
```

```text
등록된 LOT가 없습니다.
생산 지시를 등록하면 LOT 목록이 표시됩니다.
```

```text
설비 연결이 끊겼습니다.
EQ1 장비와 통신할 수 없습니다. 연결 상태를 확인해 주세요.
```

```text
불량 이력을 불러오지 못했습니다.
기간이나 설비 조건을 확인한 뒤 다시 시도해 주세요.
```

```text
생산 지시가 등록되었습니다.
```

---

### [실무]

관리자 / 회원 도메인 예시:

```text
등록된 사용자가 없습니다.
관리자 계정으로 사용자를 등록해 주세요.
```

```text
접근 권한이 없습니다.
관리자 권한이 필요한 화면입니다.
```

```text
권한이 변경되었습니다.
```

일반 서비스 도메인 예시:

```text
알림이 없습니다.
새로운 알림이 생기면 이곳에 표시됩니다.
```

```text
리뷰가 등록되었습니다.
```

Review 기준:

```md
- [ ] 도메인 문맥이 반영되는가?
- [ ] 사용자가 이해할 수 있는 문장인가?
- [ ] raw technical message가 아닌가?
- [ ] 다음 행동이 필요한 경우 안내되는가?
```

---

### [FAQ]

Q. Domain Message Example이 왜 필요해?
A. Agent가 실제 프로젝트 맥락에 맞는 피드백 문구를 생성하기 쉽게 하기 위해 필요하다.

Q. MES 화면에서는 어떤 문구가 좋아?
A. 생산 지시, LOT, 설비, 불량 이력처럼 사용자가 아는 도메인 용어를 명확히 사용한다.

Q. 설비 연결 오류는 어떻게 표현해?
A. “설비 연결이 끊겼습니다. EQ1 장비와 통신할 수 없습니다.”처럼 대상과 상태를 명확히 쓴다.

Q. 관리자 권한 오류는 어떻게 표현해?
A. “접근 권한이 없습니다. 관리자 권한이 필요한 화면입니다.”처럼 권한 문제와 필요한 조건을 안내한다.

---

## 7.3 Message Mistakes

### [개념]

Message Mistakes는 UI 상태 문구가 모호하거나 기술적이거나 다음 행동을 안내하지 못하는 실수다.

문구 실수는 기능이 정상이어도 사용자가 화면을 이해하지 못하게 만든다.

---

### [핵심]

자주 발생하는 실수:

- “Error”만 표시
- “No data”만 표시
- “OK” 같은 모호한 버튼
- raw server error 노출
- 개발자 용어 과다
- 다음 행동 없음
- success / error 문구 불일치
- 같은 상황에서 다른 문구 사용
- 비난하는 문구 사용
- 도메인 context 없음
- 너무 긴 Toast 문구
- 색상만으로 상태 전달

---

### [실무]

나쁜 문구 → 좋은 문구:

```text
Error
→ 데이터를 불러오지 못했습니다. 다시 시도해 주세요.
```

```text
No data
→ 검색 결과가 없습니다. 다른 키워드로 검색해 보세요.
```

```text
OK
→ 저장
```

```text
Bad Request
→ 입력 내용을 확인해 주세요.
```

Review Checklist:

```md
- [ ] 문구가 짧고 명확한가?
- [ ] 사용자가 다음 행동을 알 수 있는가?
- [ ] 기술 오류를 그대로 노출하지 않는가?
- [ ] 같은 상황에서 같은 표현을 사용하는가?
```

---

### [FAQ]

Q. UI Message에서 가장 흔한 실수는?
A. “Error”, “No data”, “OK”처럼 모호하고 행동을 안내하지 않는 문구를 쓰는 것이다.

Q. 버튼 텍스트는 어떻게 작성해?
A. 저장, 삭제, 검색, 다시 시도처럼 사용자가 수행할 행동을 동사 중심으로 작성한다.

Q. Toast 문구는 길어도 돼?
A. 권장하지 않는다. 긴 설명은 Alert나 Error State가 적합하다.

Q. 같은 오류에 문구가 달라도 돼?
A. 같은 상황이면 같은 표현을 사용하는 것이 일관성에 좋다.

---

# 8. Accessibility for Feedback State

## 8.1 Feedback Accessibility Rules

### [개념]

Feedback Accessibility Rules는 Loading, Error, Success, Empty 상태가 키보드 사용자와 스크린 리더 사용자에게도 전달되도록 하는 기준이다.

Feedback State는 시각적으로 보이는 것뿐 아니라 보조기기에서도 인식 가능해야 한다.

---

### [핵심]

접근성 기준:

- 중요한 동적 메시지는 `role="alert"` 고려
- 상태 변경에는 `aria-live` 고려
- loading에는 `role="status"` 고려
- error message는 input과 연결
- focus 이동 필요성 검토
- 색상만으로 상태 전달 금지
- icon은 보조 텍스트와 함께 사용
- Toast screen reader 전달 고려
- Modal error는 Modal 내부에서 접근 가능해야 함

---

### [실무]

Loading 접근성 예:

```jsx
<div role="status" aria-live="polite">
  데이터를 불러오는 중입니다.
</div>
```

Error 접근성 예:

```jsx
<p id="email-error" role="alert">
  올바른 이메일 형식이 아닙니다.
</p>
```

Status Message 예:

```jsx
<div aria-live="polite">저장되었습니다.</div>
```

Review 기준:

```md
- [ ] 중요한 상태 변경이 보조기기에 전달되는가?
- [ ] error message가 input과 연결되는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] focus 이동이 필요한 상황을 고려했는가?
```

---

### [FAQ]

Q. Feedback State에도 접근성이 필요해?
A. 필요하다. 상태 변경은 스크린 리더 사용자에게도 전달되어야 한다.

Q. role alert는 언제 써?
A. 동적으로 나타나는 중요한 오류 메시지에 사용할 수 있다.

Q. aria-live는 언제 써?
A. 화면 내용이 동적으로 변경되어 사용자에게 알려야 할 때 고려한다.

Q. Error Message는 input과 연결해야 해?
A. 해야 한다. `aria-describedby`로 연결하면 스크린 리더 사용자가 오류를 알 수 있다.

---

## 8.2 Focus Management for Error State

### [개념]

Focus Management for Error State는 오류 발생 후 사용자의 focus를 적절한 위치로 이동하거나 유지하는 기준이다.

오류가 발생했는데 focus가 엉뚱한 곳에 있으면 사용자가 문제를 찾기 어렵다.

---

### [핵심]

Focus 관리 대상:

- Form Submit Error
- Page Error
- Modal Error
- Validation Error
- Permission Error
- Authentication Error

기준:

```text
Form field error
→ 첫 번째 오류 field로 focus 이동 고려

Page level error
→ Error State heading으로 focus 이동 고려

Modal error
→ Modal 내부 error 영역 접근 가능

Toast only
→ focus 이동 일반적으로 불필요

Inline validation
→ 현재 field focus 유지 가능
```

---

### [실무]

Form Submit Error Flow:

```text
Submit
→ Validation Failed
→ Error Summary 표시
→ First invalid field focus
→ Field Error Message 연결
```

Error Summary 예:

```jsx
<div role="alert" tabIndex={-1} ref={errorSummaryRef}>
  입력 내용을 확인해 주세요.
</div>
```

Review 기준:

```md
- [ ] form submit 실패 후 오류 위치를 찾을 수 있는가?
- [ ] page-level error가 keyboard 사용자에게 전달되는가?
- [ ] modal 내부 error가 focus 흐름 안에 있는가?
- [ ] focus 이동이 사용자를 방해하지 않는가?
```

---

### [FAQ]

Q. Error State 발생 시 focus 이동이 필요해?
A. 상황에 따라 필요하다. Form 제출 실패나 page-level error는 오류 위치로 focus 이동을 고려한다.

Q. 모든 오류에 focus를 이동해야 해?
A. 아니다. inline validation이나 Toast 같은 가벼운 피드백에는 필요하지 않을 수 있다.

Q. Form 오류 시 어디로 focus를 이동해?
A. 첫 번째 오류 field 또는 error summary로 이동하는 것이 일반적이다.

Q. Modal 내부 오류는 어떻게 처리해?
A. Modal 내부에서 접근 가능한 Alert나 Error Message로 표시하고 focus 흐름 안에 둔다.

---

# 9. Feedback State Review Rules

## 9.1 Frontend Agent Feedback Rules

### [개념]

Frontend Agent Feedback Rules는 Frontend Agent가 화면을 만들 때 Feedback State를 반드시 포함하도록 하는 기준이다.

Frontend Agent는 정상 상태만 구현하지 않고 loading, empty, error, success 상태를 함께 고려해야 한다.

---

### [핵심]

Frontend Agent 생성 기준:

- 데이터 요청에는 Loading State 포함
- 데이터 없음에는 Empty State 포함
- 요청 실패에는 Error State 포함
- 작업 성공에는 Success Feedback 포함
- 제출 중 Button Loading 포함
- 실패 시 Retry Action 검토
- Form Validation Error 포함
- 중요한 오류는 Toast만 사용 금지
- 상태 메시지는 사용자 친화적으로 작성
- Feedback Accessibility 고려

---

### [실무]

Frontend Agent 화면 생성 Flow:

```text
Requirement 분석
→ Data Fetch 여부 확인
→ User Action 여부 확인
→ Loading State 설계
→ Empty State 설계
→ Error State 설계
→ Success State 설계
→ Retry / Disabled / Offline 검토
→ Accessibility 적용
→ UI Output
```

생성 전 체크:

```md
- [ ] 이 화면은 데이터를 조회하는가?
- [ ] 데이터가 없을 수 있는가?
- [ ] 요청이 실패할 수 있는가?
- [ ] 사용자가 저장 / 삭제 / 제출을 하는가?
- [ ] 성공 후 어떤 피드백이 필요한가?
- [ ] 재시도 action이 필요한가?
```

---

### [FAQ]

Q. Frontend Agent는 Feedback State를 어떻게 적용해?
A. 데이터 요청과 사용자 action을 분석해 loading, empty, error, success, retry 상태를 함께 생성한다.

Q. 정상 화면만 구현하면 안 돼?
A. 안 된다. 실제 서비스에서는 loading, empty, error 상태가 반드시 발생할 수 있다.

Q. 데이터가 없을 가능성이 있으면 무엇을 넣어야 해?
A. Empty State를 넣어야 한다.

Q. 요청 실패 가능성이 있으면 무엇을 넣어야 해?
A. Error State와 필요한 경우 Retry Action을 넣어야 한다.

---

## 9.2 Review Agent Feedback Checklist

### [개념]

Review Agent Feedback Checklist는 구현된 화면이 Feedback State 기준을 만족하는지 검토하는 기준이다.

Review Agent는 정상 상태뿐 아니라 비정상 상태와 빈 상태까지 검토해야 한다.

---

### [핵심]

Review Checklist:

```md
## Loading

- [ ] 데이터 요청 중 Loading State가 있는가?
- [ ] Button loading 중 중복 클릭이 방지되는가?
- [ ] Skeleton / Spinner / Progress 선택이 적절한가?
- [ ] 무한 loading이 방치되지 않는가?

## Empty

- [ ] 데이터 없음 상태가 있는가?
- [ ] 검색 / 필터 결과 없음 상태가 구분되는가?
- [ ] Table Empty State가 있는가?
- [ ] 다음 action이 필요한 경우 제공되는가?

## Error

- [ ] 요청 실패 Error State가 있는가?
- [ ] raw error가 노출되지 않는가?
- [ ] Retry Action이 필요한 경우 제공되는가?
- [ ] Authentication / Permission Error가 구분되는가?
- [ ] Field Error와 Form Error가 구분되는가?

## Success

- [ ] 성공 후 완료 피드백이 있는가?
- [ ] 성공 후 실제 UI 상태가 갱신되는가?
- [ ] 중요한 완료에는 다음 action이 있는가?

## Accessibility

- [ ] error message가 input과 연결되는가?
- [ ] 중요한 상태 변경이 보조기기에 전달되는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
```

---

### [실무]

Review Decision:

```text
Approved
→ 주요 Feedback State가 있고 사용자 흐름이 안정적임

Needs Fix
→ 일부 loading / empty / success / retry 기준 미흡

Blocked
→ 주요 오류 상태 누락, 중복 제출 가능, 빈 화면 방치, 접근성 심각 문제
```

Blocked 예:

```text
저장 중 중복 클릭 가능
데이터 로드 실패 시 빈 화면
검색 결과 없음 상태 없음
Input error message 없음
raw server error 노출
중요 오류를 Toast만으로 표시
```

---

### [FAQ]

Q. Review Agent는 Feedback State에서 뭘 봐야 해?
A. Loading, Empty, Error, Success, Retry, Validation, Accessibility 상태가 필요한 곳에 있는지 확인해야 한다.

Q. 어떤 Feedback 문제는 Blocked야?
A. 중복 제출 가능, 주요 Error State 누락, 빈 화면 방치, raw error 노출, 필수 field error 누락은 Blocked가 될 수 있다.

Q. Empty State가 없으면 항상 Blocked야?
A. 핵심 목록이나 검색 화면에서는 Blocked 또는 Needs Fix가 될 수 있다.

Q. Success Feedback이 없으면 문제야?
A. 저장, 삭제, 등록처럼 사용자가 결과를 확신해야 하는 작업에서는 문제다.

---

## 9.3 PM Agent Feedback Completion Rules

### [개념]

PM Agent Feedback Completion Rules는 PM Agent가 화면 완료 여부를 판단할 때 Feedback State를 확인하는 기준이다.

PM Agent는 정상 상태만 보고 완료 판단하지 않고 loading, empty, error, success 상태가 사용자 흐름을 방해하지 않는지 확인해야 한다.

---

### [핵심]

PM Agent 확인 기준:

- 사용자가 데이터 로딩 상태를 알 수 있는가
- 데이터가 없을 때 다음 행동을 알 수 있는가
- 실패했을 때 복구 방법을 알 수 있는가
- 저장 / 삭제 / 등록 성공 여부를 알 수 있는가
- 오류 메시지가 사용자 친화적인가
- 모바일에서도 상태 UI가 깨지지 않는가
- 권한 오류와 로그인 오류가 명확한가
- 기능 사용을 막는 피드백 누락이 없는가

---

### [실무]

PM 판단 Flow:

```text
Normal State 확인
→ Loading State 확인
→ Empty State 확인
→ Error State 확인
→ Success Feedback 확인
→ User Flow 확인
→ Completion Decision
```

PM Decision:

```text
UI Complete
→ 정상 / loading / empty / error / success 흐름이 사용 가능

UI Partial
→ 기능은 가능하지만 일부 피드백 상태 미흡

UI Blocked
→ 사용자가 실패 / 빈 상태 / 처리 중 상태를 이해할 수 없음
```

PM 체크 예:

```md
- [ ] 검색 결과가 없을 때 안내가 있는가?
- [ ] 저장 중 버튼이 처리 중으로 바뀌는가?
- [ ] 저장 성공 후 완료 메시지가 있는가?
- [ ] 데이터 로드 실패 시 다시 시도할 수 있는가?
```

---

### [FAQ]

Q. PM Agent는 Feedback State를 어떻게 봐야 해?
A. 사용자가 loading, empty, error, success 상태에서 다음 행동을 이해할 수 있는지 확인한다.

Q. 정상 화면이 동작하면 완료야?
A. 아니다. 빈 상태, 오류 상태, 처리 중 상태도 사용 가능해야 완료로 볼 수 있다.

Q. Feedback State 누락이 Blocker가 될 수 있어?
A. 그렇다. 사용자가 기능을 사용할 수 없거나 상태를 이해할 수 없다면 Blocker가 될 수 있다.

Q. PM Agent가 문구까지 봐야 해?
A. 세부 구현보다 사용자 친화적이고 다음 행동을 안내하는지 확인해야 한다.

---

# 10. Final Checklist

## 10.1 Part05 Quality Checklist

### [개념]

Part05 Quality Checklist는 Feedback State Pattern Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Core

- [ ] Feedback State Pattern 정의가 명확한가?
- [ ] Loading / Empty / Error / Success 기준이 있는가?
- [ ] Disabled / Retry / Offline 기준이 있는가?
- [ ] Feedback Message 기준이 있는가?
- [ ] Accessibility 기준이 있는가?

## Loading

- [ ] Spinner 기준이 있는가?
- [ ] Skeleton 기준이 있는가?
- [ ] Progress 기준이 있는가?
- [ ] Button Loading 기준이 있는가?
- [ ] Loading Mistakes가 포함되어 있는가?

## Empty

- [ ] Empty State 구조가 있는가?
- [ ] Search Empty 기준이 있는가?
- [ ] Table Empty 기준이 있는가?
- [ ] Empty Message 기준이 있는가?
- [ ] Empty Mistakes가 포함되어 있는가?

## Error

- [ ] Error State 구조가 있는가?
- [ ] Network / Server Error 기준이 있는가?
- [ ] Authentication / Permission Error 기준이 있는가?
- [ ] Form Validation Error 기준이 있는가?
- [ ] Error Message 기준이 있는가?
- [ ] Error Mistakes가 포함되어 있는가?

## Success

- [ ] Success State 기준이 있는가?
- [ ] Success Toast 기준이 있는가?
- [ ] Success Page 기준이 있는가?
- [ ] Success Mistakes가 포함되어 있는가?

## Agent Usage

- [ ] Frontend Agent 생성 기준이 있는가?
- [ ] Review Agent 검토 기준이 있는가?
- [ ] PM Agent 완료 판단 기준이 있는가?
- [ ] Approved / Needs Fix / Blocked 기준이 있는가?
```

---

### [실무]

Part05는 Part04 Core Component Rules와 연결되어 Alert, Toast, Button Loading, Empty State, Error State 사용 기준을 확장한다.

Part 연계:

```text
Part01 Design System Core
→ Part02 Design Token Rules
→ Part03 Component Specification Rules
→ Part04 Core Component Rules
→ Part05 Feedback State Pattern Rules
→ Part06 Layout Responsive Theme Rules
→ Part07 Accessibility Documentation Review Rules
```

Part05 기준은 Frontend Agent가 정상 화면 외의 비정상 상태와 빈 상태를 생성할 때 사용한다.

---

### [FAQ]

Q. Part05의 역할은 뭐야?
A. Loading, Empty, Error, Success, Retry, Disabled, Offline 같은 Feedback State Pattern 기준을 정의하는 문서다.

Q. Part05는 Part04와 어떻게 연결돼?
A. Part04의 Alert, Toast, Button, Table, Form Field 컴포넌트가 Part05의 feedback state 기준을 사용한다.

Q. Part05에서 가장 중요한 것은 뭐야?
A. Loading, Empty, Error, Success 상태를 정상 화면과 함께 반드시 고려하도록 만드는 것이다.

Q. Part05 최종 승인 기준은 뭐야?
A. Frontend Agent가 feedback state를 생성하고 Review Agent가 누락 여부를 검토할 수 있을 만큼 기준과 FAQ가 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Feedback State Pattern이 뭐야?
A. 사용자 행동이나 데이터 요청 결과에 대해 loading, empty, error, success 같은 상태를 UI로 알려주는 패턴이다.

Q. Feedback State는 왜 필요해?
A. 사용자가 화면이 멈췄는지, 성공했는지, 실패했는지, 데이터가 없는지 알 수 있어야 하기 때문이다.

Q. Loading State는 왜 필요해?
A. 사용자가 화면이 멈췄는지 처리 중인지 알 수 있어야 하기 때문이다.

Q. Loading State는 언제 필요해?
A. 데이터 조회, 저장, 삭제, 로그인, 파일 업로드처럼 시간이 걸리는 작업에 필요하다.

Q. Loading 중 버튼은 disabled 처리해야 해?
A. 대부분 그렇다. 중복 클릭과 중복 API 요청을 막기 위해 필요하다.

Q. Spinner는 언제 써?
A. 짧은 작업이나 진행률을 알 수 없는 작은 영역 로딩에 사용한다.

Q. Skeleton은 언제 써?
A. 카드나 목록처럼 로딩 후 구조가 예상 가능한 콘텐츠에 적합하다.

Q. Progress Pattern은 언제 써?
A. 파일 업로드, 긴 데이터 처리, 단계가 있는 작업처럼 시간이 오래 걸리는 작업에 사용한다.

Q. Loading State에서 가장 흔한 실수는?
A. loading 상태를 만들지 않거나, loading 중 중복 클릭을 막지 않는 것이다.

Q. Empty State가 뭐야?
A. 요청은 성공했지만 표시할 데이터가 없을 때 보여주는 UI 패턴이다.

Q. Empty State에는 무엇이 들어가야 해?
A. 데이터가 없다는 설명과 사용자가 다음에 할 수 있는 행동이 들어가면 좋다.

Q. 데이터가 없으면 빈 화면이면 안 돼?
A. 안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터 없음이고, Error State는 요청 실패나 처리 오류다.

Q. Search Empty State는 언제 필요해?
A. 검색 요청은 성공했지만 결과가 0개일 때 필요하다.

Q. 검색 결과 없음은 Error State야?
A. 아니다. 요청이 성공했다면 Empty State다.

Q. Table Empty State는 왜 필요해?
A. 빈 테이블만 보여주면 사용자가 데이터가 없는지 오류인지 알 수 없기 때문이다.

Q. Empty State 문구는 어떻게 작성해?
A. 데이터가 없다는 사실과 사용자가 다음에 할 수 있는 행동을 짧고 명확하게 작성한다.

Q. Empty State에서 가장 흔한 실수는?
A. 데이터가 없을 때 빈 화면만 보여주거나 “No data”만 표시하는 것이다.

Q. Error State가 뭐야?
A. 요청 실패나 처리 오류가 발생했을 때 문제와 복구 방법을 안내하는 UI 패턴이다.

Q. Error State에는 무엇이 필요해?
A. 사용자 친화적 title, 설명, 가능한 경우 복구 action이 필요하다.

Q. 서버 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 민감한 정보가 포함될 수 있으므로 사용자 친화 메시지로 바꿔야 한다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?
A. 권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State도 함께 제공하는 것이 좋다.

Q. Network Error는 어떻게 보여줘?
A. 네트워크 상태를 확인하고 다시 시도할 수 있도록 사용자 친화 메시지와 retry action을 제공한다.

Q. Authentication Error와 Permission Error는 뭐가 달라?
A. Authentication Error는 로그인 상태 문제이고, Permission Error는 로그인은 되었지만 권한이 부족한 상태다.

Q. 로그인 필요 오류에는 어떤 action이 좋아?
A. 로그인하기 버튼이 적합하다.

Q. Form Validation Error는 어디에 표시해야 해?
A. 가능하면 오류가 발생한 입력 필드 가까이에 표시해야 한다.

Q. Form-level Error와 Field-level Error는 뭐가 달라?
A. Field-level Error는 특정 입력 오류이고, Form-level Error는 전체 제출 실패나 공통 오류다.

Q. Error Message는 어떻게 작성해?
A. 사용자가 이해할 수 있는 문장으로 실패 상황과 다음 행동을 안내한다.

Q. Error는 console.log만 해도 돼?
A. 안 된다. 사용자에게 실패 상태와 복구 방법을 알려야 한다.

Q. Success State는 언제 필요해?
A. 저장, 삭제, 로그인, 회원가입, 리뷰 등록 같은 작업 성공을 알려야 할 때 필요하다.

Q. 성공 메시지는 꼭 필요해?
A. 사용자가 작업 완료를 확신해야 하는 경우 필요하다.

Q. 모든 성공에 Toast를 띄워도 돼?
A. 과하면 방해가 될 수 있다. 중요한 행동 중심으로 사용한다.

Q. Success Toast는 언제 써?
A. 저장, 삭제, 복사, 등록처럼 가벼운 작업 성공을 짧게 알려줄 때 사용한다.

Q. Success Page는 언제 필요해?
A. 회원가입, 결제, 신청 완료처럼 중요한 완료 흐름에 필요하다.

Q. Disabled State는 뭐야?
A. 사용자가 현재 조작할 수 없는 상태를 표현하는 패턴이다.

Q. disabled 스타일만 있으면 충분해?
A. 아니다. 실제 조작이 차단되어야 한다.

Q. Retry Pattern은 언제 필요해?
A. 네트워크 오류나 일시적 서버 오류처럼 다시 시도하면 해결될 수 있는 경우 필요하다.

Q. Retry 버튼 문구는 뭐가 좋아?
A. “다시 시도”가 명확하고 일반적으로 적합하다.

Q. Offline State는 언제 필요해?
A. 네트워크 연결이 끊기거나 실시간 연결, 장비 연결, 외부 API 접근이 실패했을 때 필요하다.

Q. 실시간 연결 상태는 어떻게 표시해?
A. 연결됨 / 연결 끊김 Badge나 Alert로 표시할 수 있다.

Q. UI Message는 어떻게 작성해?
A. 상태 설명, 맥락, 다음 행동을 짧고 명확하게 작성한다.

Q. MES 화면에서는 어떤 문구가 좋아?
A. 생산 지시, LOT, 설비, 불량 이력처럼 사용자가 아는 도메인 용어를 명확히 사용한다.

Q. 설비 연결 오류는 어떻게 표현해?
A. “설비 연결이 끊겼습니다. EQ1 장비와 통신할 수 없습니다.”처럼 대상과 상태를 명확히 쓴다.

Q. Feedback State에도 접근성이 필요해?
A. 필요하다. 상태 변경은 스크린 리더 사용자에게도 전달되어야 한다.

Q. role alert는 언제 써?
A. 동적으로 나타나는 중요한 오류 메시지에 사용할 수 있다.

Q. Error State 발생 시 focus 이동이 필요해?
A. 상황에 따라 필요하다. Form 제출 실패나 page-level error는 오류 위치로 focus 이동을 고려한다.

Q. Frontend Agent는 Feedback State를 어떻게 적용해?
A. 데이터 요청과 사용자 action을 분석해 loading, empty, error, success, retry 상태를 함께 생성한다.

Q. Review Agent는 Feedback State에서 뭘 봐야 해?
A. Loading, Empty, Error, Success, Retry, Validation, Accessibility 상태가 필요한 곳에 있는지 확인해야 한다.

Q. PM Agent는 Feedback State를 어떻게 봐야 해?
A. 사용자가 loading, empty, error, success 상태에서 다음 행동을 이해할 수 있는지 확인한다.

Q. Part05의 역할은 뭐야?
A. Loading, Empty, Error, Success, Retry, Disabled, Offline 같은 Feedback State Pattern 기준을 정의하는 문서다.

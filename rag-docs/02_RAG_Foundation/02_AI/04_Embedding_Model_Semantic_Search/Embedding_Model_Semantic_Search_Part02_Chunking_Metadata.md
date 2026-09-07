# Embedding Model & Semantic Search Part02 Chunking Metadata

---

# 1. Chunking Core

## 1.1 Chunking

### [개념]

Chunking은 긴 Document를 RAG Retrieval에 적합한 검색 단위인 Chunk로 나누는 과정이다.

RAG에서 검색되는 단위는 보통 문서 전체가 아니라 Chunk다.
따라서 Chunk 품질은 Embedding 품질과 함께 Retrieval 품질을 결정한다.

기본 Flow:

```text
Markdown Document
→ Header Based Split
→ Semantic Boundary Check
→ Code Block Preservation
→ Metadata Attach
→ Chunk Embedding
→ Vector Store
```

Chunk의 목적:

- 하나의 개념을 독립 검색 가능하게 분리
- Query와 의미적으로 매칭될 수 있는 단위 생성
- LLM이 답변 근거로 사용할 수 있는 Context 제공
- Code Example과 설명의 의미 연결 유지
- Retrieval Precision과 Recall 균형 확보

---

### [핵심]

- Chunk는 RAG 검색의 기본 단위다.
- Chunk는 하나의 개념만 다루는 것이 좋다.
- Chunk 제목은 Retrieval 품질에 직접 영향을 준다.
- Header는 Chunk 경계로 활용할 수 있다.
- Code Block과 설명은 가능하면 같은 Chunk에 유지한다.
- FAQ Chunk는 실제 사용자 Query와 잘 매칭된다.
- Retrieval Queries Chunk는 검색 매칭을 강화한다.
- Chunk가 너무 크면 여러 개념이 섞인다.
- Chunk가 너무 작으면 문맥이 부족하다.
- Chunking 실패는 Embedding Model 교체만으로 해결되지 않는다.

---

### [실무]

2026 실무 기준에서 RAG 문서는 사람이 읽기 좋은 문서보다 검색되기 좋은 Chunk 구조가 우선이다.

좋은 Chunk 조건:

- 제목이 명확함
- 핵심 키워드 포함
- 하나의 주제만 설명
- 독립 검색 가능
- 짧은 예제 포함
- FAQ 포함 가능
- Code Block이 설명과 분리되지 않음
- Metadata와 연결 가능

좋은 Chunk 예시:

```md
# Chunk Size

### [개념]

Chunk Size는 하나의 검색 단위가 포함하는 Token 양이다.

### [핵심]

- 너무 작으면 문맥이 부족하다.
- 너무 크면 여러 개념이 섞인다.
- Medium Chunk는 일반 RAG 문서에 적합하다.
```

나쁜 Chunk 예시:

```md
# 기타

검색도 중요하고 모델도 중요하고 문서도 중요하다.
상황에 따라 적절히 조정한다.
```

나쁜 이유:

- 제목이 불명확함
- 검색 Keyword 부족
- 여러 개념 혼합
- Query Matching 약함
- Agent가 근거로 사용하기 어려움

---

### [주의]

- Code Block 중간에서 Chunk를 자르지 않는다.
- 여러 개념을 하나의 Chunk에 과도하게 섞지 않는다.
- 제목 없는 Chunk를 만들지 않는다.
- 긴 서론을 Chunk 앞에 배치하지 않는다.
- 너무 많은 중복 문장을 여러 Chunk에 반복하지 않는다.
- FAQ를 질문만 작성하고 답변 없이 두지 않는다.
- Retrieval Queries를 문서 마지막에서 누락하지 않는다.
- Chunk Overlap을 과도하게 설정하지 않는다.

---

### [FAQ]

Q. Chunking이 뭐야?

A.
긴 문서를 RAG 검색에 적합한 작은 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk가 왜 중요해?

A.
RAG는 Chunk 단위로 문서를 검색하므로 Chunk 품질이 Retrieval 품질을 크게 좌우한다.

Q. 좋은 Chunk는 어떤 구조야?

A.
하나의 개념을 다루고 제목이 명확하며 핵심 키워드, 설명, 예제, FAQ가 검색 가능하게 포함된 구조다.

Q. Chunking이 안 좋으면 Embedding Model을 바꾸면 해결돼?

A.
아니다. Chunk 구조가 나쁘면 좋은 Embedding Model을 사용해도 검색 품질이 낮을 수 있다.

---

# 2. Chunk Size

## 2.1 Chunk Size Strategy

### [개념]

Chunk Size는 하나의 Chunk가 포함하는 Text 또는 Token의 양이다.

Chunk Size는 Retrieval Precision, Retrieval Recall, Context Budget에 영향을 준다.

- Small Chunk: 정밀 검색에 유리하지만 문맥 부족 가능
- Medium Chunk: 개념 설명과 실무 문서에 균형적
- Large Chunk: 문맥은 풍부하지만 주제 혼합 가능

---

### [핵심]

- Chunk Size는 고정 정답이 없다.
- RAG 문서 목적과 Domain에 따라 조정한다.
- FAQ는 Small Chunk로도 효과적이다.
- 개념 설명은 Medium Chunk가 적합하다.
- 긴 코드 예제는 설명과 함께 유지해야 한다.
- Large Chunk는 복합 예제에는 유용하지만 검색 정밀도가 낮아질 수 있다.
- Chunk Size는 Context Window와 함께 고려해야 한다.
- 검색 결과가 자주 빗나가면 Chunk Size보다 Chunk 구조를 먼저 점검한다.

---

### [실무]

권장 기준:

| Chunk Size | 장점           | 단점           | 적합               |
| ---------- | -------------- | -------------- | ------------------ |
| Small      | 정밀 검색 유리 | 문맥 부족      | FAQ, 단일 개념     |
| Medium     | 균형 좋음      | 설계 필요      | 일반 RAG 문서      |
| Large      | 문맥 풍부      | 주제 혼합 가능 | 복합 예제, 긴 흐름 |

RAG 문서 제작 기준:

```text
FAQ / Retrieval Queries
→ Small Chunk 가능

[개념] + [핵심] + 짧은 [실무]
→ Medium Chunk 권장

Code Example + 설명 + 주의사항
→ Code Block 보존을 우선하여 Medium 또는 Large Chunk 허용
```

일반 권장 범위:

```text
RAG 문서 Chunk:
300 ~ 1200 tokens

FAQ Chunk:
짧게 유지 가능

Code Example Chunk:
코드와 설명이 분리되지 않는 범위 우선
```

Chunk Size 판단 Flow:

```text
Chunk가 하나의 개념만 다루는가?
→ 단독 검색되어도 의미가 유지되는가?
→ Code Block이 중간에서 잘리지 않는가?
→ 너무 많은 개념이 섞이지 않았는가?
→ Retrieved Context로 답변 가능성이 높은가?
```

---

### [주의]

- 무조건 작은 Chunk가 좋은 것은 아니다.
- 무조건 큰 Chunk가 좋은 것도 아니다.
- 너무 작은 Chunk는 LLM이 답변할 근거가 부족할 수 있다.
- 너무 큰 Chunk는 관련 없는 정보가 같이 검색될 수 있다.
- Code Block을 Chunk Size 기준으로 강제 분리하지 않는다.
- Chunk Size 조정 전에 제목, Section, FAQ, Metadata 품질을 먼저 확인한다.

---

### [FAQ]

Q. Chunk Size는 어떻게 정해?

A.
하나의 개념이 독립적으로 이해될 정도로 유지하되 여러 개념이 섞이지 않도록 조정한다.

Q. 작은 Chunk가 항상 좋아?

A.
아니다. 정밀 검색에는 유리하지만 문맥이 부족해 답변 품질이 낮아질 수 있다.

Q. 큰 Chunk가 항상 좋아?

A.
아니다. 문맥은 풍부하지만 여러 개념이 섞여 관련 없는 Chunk가 검색될 수 있다.

Q. 코드 예제는 어떻게 Chunking해야 해?

A.
Code Block 중간에서 자르지 말고 설명과 같은 Chunk에 유지하는 것이 좋다.

---

# 3. Chunk Overlap

## 3.1 Chunk Overlap Strategy

### [개념]

Chunk Overlap은 인접한 Chunk 사이에 일부 Text를 중복 포함하는 방식이다.

Chunk 경계에서 문맥이 끊기는 문제를 줄이는 데 사용한다.

기본 구조:

```text
Chunk A:
내용 1 + 내용 2 + 내용 3

Chunk B:
내용 3 + 내용 4 + 내용 5
```

여기서 `내용 3`이 Overlap이다.

---

### [핵심]

- Chunk Overlap은 문맥 단절을 줄인다.
- Overlap은 Retrieval Recall 개선에 도움될 수 있다.
- Overlap이 너무 많으면 중복 검색이 증가한다.
- 중복 Chunk가 Top-K를 차지하면 Context 품질이 낮아질 수 있다.
- FAQ와 Retrieval Queries를 과도하게 중복하면 검색 결과가 비슷해질 수 있다.
- Code Block 보존이 Overlap 설정보다 우선이다.
- Header Based Chunking에서는 Overlap을 작게 유지할 수 있다.

---

### [실무]

Overlap이 필요한 경우:

- 긴 설명이 여러 Chunk로 나뉘는 경우
- 이전 문맥 없이는 다음 Chunk 이해가 어려운 경우
- 개념 흐름이 이어지는 경우
- 문서 Splitter가 기계적으로 분리하는 경우

Overlap이 불필요하거나 적게 필요한 경우:

- Header 기준으로 명확히 분리된 문서
- FAQ 중심 문서
- 독립적인 개념 Chunk
- 짧은 실무 체크리스트
- Retrieval Queries Block

권장 판단 기준:

```text
문맥 단절이 자주 발생함
→ Overlap 증가 검토

중복 Chunk가 너무 많이 검색됨
→ Overlap 감소 검토

Header 기준 Chunk가 명확함
→ Overlap 최소화 가능

Code Block이 잘릴 위험 있음
→ Split 기준을 조정하고 Code Block 보존 우선
```

---

### [주의]

- Overlap은 무조건 크게 설정하지 않는다.
- Overlap이 크면 저장 공간과 검색 중복이 증가한다.
- 유사한 Chunk가 Top-K를 차지하면 다양한 근거를 놓칠 수 있다.
- Retrieval Queries를 모든 문서에 동일하게 반복하면 중복 검색이 늘어난다.
- Overlap으로 Chunk 구조 문제를 덮으려 하지 않는다.
- 먼저 Semantic Boundary를 기준으로 Chunk를 설계한다.

---

### [FAQ]

Q. Chunk Overlap은 왜 써?

A.
Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다.

Q. Overlap은 크게 잡을수록 좋아?

A.
아니다. 너무 크면 중복 Chunk가 많이 검색되어 Context 품질이 낮아질 수 있다.

Q. Header 기준으로 잘 나눈 문서도 Overlap이 필요해?

A.
필요성이 낮을 수 있다. 각 Chunk가 독립적이면 Overlap을 최소화할 수 있다.

Q. 중복 문서가 너무 많이 검색되면 어떻게 해?

A.
Overlap을 줄이고 중복 설명을 제거하며 결과 Deduplication을 적용한다.

---

# 4. Semantic Chunking

## 4.1 Semantic Boundary

### [개념]

Semantic Chunking은 의미 단위로 문서를 나누는 방식이다.

단순히 글자 수나 Token 수만 기준으로 나누지 않고, 개념의 경계와 문맥의 완결성을 기준으로 Chunk를 나눈다.

Semantic Boundary는 의미가 자연스럽게 끊기는 지점이다.

예시:

```text
Embedding 개념 설명 끝
→ Query Embedding 설명 시작
```

이 지점은 Semantic Boundary가 될 수 있다.

---

### [핵심]

- Semantic Chunking은 의미 경계를 기준으로 분리한다.
- 하나의 Chunk는 하나의 주요 개념을 담는다.
- Header, Sub Header, FAQ, Code Block은 Chunk 경계 후보가 된다.
- 개념 설명과 예제는 가능하면 같은 Chunk에 둔다.
- 서로 다른 주제를 Token 기준으로 억지로 붙이지 않는다.
- 의미가 이어지는 문단을 기계적으로 자르지 않는다.
- Semantic Boundary는 Retrieval 품질과 답변 근거 품질에 영향을 준다.

---

### [실무]

Semantic Chunking 기준:

```text
새로운 핵심 개념이 시작되는가?
→ Chunk 분리 후보

예제 코드가 앞 설명에 의존하는가?
→ 같은 Chunk 유지

FAQ가 특정 개념에 대한 질문인가?
→ 해당 개념 Chunk 근처 유지 가능

여러 개념이 한 Section에 섞였는가?
→ Sub Section으로 분리
```

좋은 분리 예시:

```text
# 1. Embedding Core
## 1.1 Embedding

# 2. Query Embedding
## 2.1 Query Embedding

# 3. Document Embedding
## 3.1 Document Embedding
```

나쁜 분리 예시:

```text
# Embedding

Embedding은 Text를 Vector로 변환한다.
Query Embedding은...
Document Embedding은...
Vector Dimension은...
Top-K는...
Reranking은...
```

나쁜 이유:

- 여러 개념이 한 Chunk에 섞임
- Query Matching이 분산됨
- 검색 결과가 불명확해짐
- Agent가 특정 근거를 찾기 어려움

---

### [주의]

- Token 수만 보고 Chunk를 자르지 않는다.
- 개념 중간에서 Chunk를 자르지 않는다.
- 코드와 설명을 분리하지 않는다.
- FAQ를 관련 개념과 완전히 동떨어진 위치에만 두지 않는다.
- 제목이 모호하면 Semantic Boundary가 약해진다.
- Chunk가 커지더라도 Code Block 보존이 더 중요할 수 있다.

---

### [FAQ]

Q. Semantic Chunking이 뭐야?

A.
문서를 의미 단위로 나누는 방식이다. 개념의 경계와 문맥의 완결성을 기준으로 Chunk를 만든다.

Q. Token 기준 Chunking과 뭐가 달라?

A.
Token 기준은 길이를 중심으로 나누고, Semantic Chunking은 의미와 개념 경계를 중심으로 나눈다.

Q. Semantic Boundary는 뭐야?

A.
하나의 개념이 끝나고 다른 개념이 시작되는 자연스러운 의미 경계다.

Q. RAG 문서에는 Semantic Chunking이 왜 좋아?

A.
검색된 Chunk가 독립적인 의미를 유지해 LLM이 답변 근거로 사용하기 쉽다.

---

# 5. Header Based Chunking

## 5.1 Markdown Header Chunking

### [개념]

Header Based Chunking은 Markdown Header를 기준으로 문서를 나누는 방식이다.

RAG 문서에서 Header는 Chunk의 의미를 설명하는 검색 신호 역할을 한다.

Header 예시:

```md
# Embedding Model & Semantic Search

## Query Embedding

### [개념]
```

Header는 Vector에 포함되는 Text와 Metadata 양쪽에서 Retrieval 품질을 높일 수 있다.

---

### [핵심]

- Header는 Chunk 경계로 활용할 수 있다.
- Header는 Chunk의 주제를 명확히 한다.
- Header에 핵심 Keyword를 포함하는 것이 좋다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`는 RAG 문서의 표준 Section이다.
- 모호한 Header는 검색 품질을 낮춘다.
- Header와 Metadata의 Section 값을 일치시키는 것이 좋다.
- Header Based Chunking은 Semantic Chunking과 함께 사용한다.

---

### [실무]

좋은 Header:

```md
# Query Embedding

## Query Rewrite

## Query Expansion

## Korean English Mixed Query
```

나쁜 Header:

```md
# 기타

## 참고

## 내용

## 여러 가지
```

Header 작성 기준:

```text
Domain Keyword 포함
→ Embedding, Semantic Search, Chunking, Metadata

사용자 Query와 매칭 가능
→ Chunk Size는 어떻게 정해?

기술 용어 병기
→ Query Embedding / 사용자 질문 벡터화

Agent Routing 가능
→ domain=AI, section=Chunking
```

RAG 문서 표준 Section:

```md
### [개념]

### [핵심]

### [실무]

### [FAQ]
```

추가 권장 Section:

```md
### [Flow]

### [예제]

### [주의]

### [Best Practice]

### [Troubleshooting]

### [Checklist]

### [Comparison]
```

---

### [주의]

- `# 기타`, `# 참고`, `# 내용` 같은 모호한 제목을 피한다.
- Header에 핵심 용어가 없으면 검색 신호가 약해진다.
- Header 구조를 지나치게 깊게 만들지 않는다.
- Header와 실제 내용이 다르면 잘못된 검색 결과를 유발한다.
- Metadata의 section 값과 Header가 불일치하지 않게 한다.
- Retrieval Queries는 문서 마지막에 별도 Header로 유지한다.

---

### [FAQ]

Q. Header Based Chunking이 뭐야?

A.
Markdown Header를 기준으로 문서를 Chunk로 나누는 방식이다.

Q. Header가 검색 품질에 영향을 줘?

A.
그렇다. Header는 Chunk의 주제를 명확히 하고 Query Matching을 강화한다.

Q. 좋은 Header는 어떤 형태야?

A.
핵심 Domain Keyword가 포함되고 사용자가 검색할 표현과 매칭될 수 있는 제목이다.

Q. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`는 왜 반복해?

A.
RAG 문서 구조를 표준화하고 Agent가 Chunk를 해석하기 쉽게 만들기 위해 사용한다.

---

# 6. Code Block Preservation

## 6.1 Code Block Chunking

### [개념]

Code Block Preservation은 코드 예제를 Chunking할 때 Code Block 중간에서 자르지 않는 규칙이다.

코드는 설명과 함께 검색되어야 코드 생성, 코드 리뷰, 오류 분석에 사용할 수 있다.

좋은 구조:

````md
### [실무]

Service Layer에서는 Transaction Boundary를 명확히 한다.

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
        .orElseThrow(UserNotFoundException::new);

    user.update(request.name());
}
```
````

위 구조는 설명과 코드가 함께 있어 Retrieval Context로 사용하기 좋다.

---

### [핵심]

- Code Block 중간에서 Chunk를 분리하지 않는다.
- 코드와 설명은 가능하면 같은 Chunk에 유지한다.
- 코드만 단독으로 검색되면 의도 해석이 어려울 수 있다.
- 설명만 검색되고 코드가 누락되면 코드 생성 품질이 낮아진다.
- 긴 코드는 핵심 Snippet 중심으로 작성한다.
- 불필요한 import와 boilerplate는 줄일 수 있다.
- Code Block 주변에 핵심 Keyword를 배치한다.

---

### [실무]

좋은 Code Chunk 조건:

- 코드 목적 설명 포함
- 핵심 로직만 포함
- 관련 Domain Keyword 포함
- 주의사항 포함 가능
- 너무 긴 전체 파일 코드 제외
- 검색 Query와 매칭될 표현 포함

좋은 예시:

````md
# Transaction Boundary

### [실무]

Transaction Boundary는 Service Layer에 두는 것이 일반적이다.

```java
@Transactional
public void createOrder(OrderCreateRequest request) {
    Order order = Order.create(request);
    orderRepository.save(order);
}
```

핵심:

- Controller가 아니라 Service에서 Transaction 관리
- 하나의 Use Case 단위로 Transaction 설정
````

나쁜 예시:

````md
```java
@Transactional
public void createOrder(OrderCreateRequest request) {
```
````

나쁜 이유:

- 코드가 중간에서 잘림
- 설명 없음
- 검색 근거로 사용 불가
- Agent가 완성된 코드로 오해할 수 있음

---

### [주의]

- Code Block에 불필요하게 긴 전체 프로젝트 코드를 넣지 않는다.
- Code Block 시작과 끝을 분리하지 않는다.
- 설명 없이 코드만 넣지 않는다.
- 코드와 관련 없는 설명을 같은 Chunk에 섞지 않는다.
- 코드 예제에 사용한 용어와 Section 제목을 일치시킨다.
- Markdown Code Fence가 깨지지 않게 한다.
- 코드블록에 불필요한 id 속성을 넣지 않는다.

---

### [FAQ]

Q. Code Block은 어떻게 Chunking해야 해?

A.
Code Block 중간에서 자르지 말고 가능하면 설명과 같은 Chunk에 유지한다.

Q. 코드만 Chunk로 저장하면 안 돼?

A.
가능은 하지만 권장하지 않는다. 설명이 없으면 Agent가 코드의 목적과 사용 조건을 오해할 수 있다.

Q. 긴 코드는 전부 넣어야 해?

A.
아니다. Retrieval과 코드 생성에 필요한 핵심 Snippet 중심으로 작성하는 것이 좋다.

Q. 코드 예제 주변에는 무엇을 넣어야 해?

A.
코드 목적, 핵심 Keyword, 사용 조건, 주의사항을 함께 넣는 것이 좋다.

---

# 7. FAQ Chunk

## 7.1 FAQ for Retrieval

### [개념]

FAQ Chunk는 실제 사용자가 질문할 형태의 문장과 짧은 답변을 함께 제공하는 Retrieval 강화 구조다.

FAQ는 Semantic Search와 Query Matching에 유리하다.

형식:

```md
### [FAQ]

Q. 질문?

A.  
짧고 명확한 답변
```

FAQ는 질문만 작성하면 안 된다.
반드시 Q와 A를 함께 작성해야 한다.

---

### [핵심]

- FAQ는 실제 사용자 질문 형태로 작성한다.
- Q only 형식은 금지한다.
- A는 1~4줄로 짧게 작성한다.
- FAQ는 Query Matching을 강화한다.
- FAQ는 Semantic Search 품질을 보완한다.
- 기술 용어는 한국어 + 영어 병기를 활용한다.
- 문서 마지막 Retrieval Queries에도 FAQ 형식을 사용한다.
- `[면접]` 섹션 대신 `[FAQ]`를 사용한다.

---

### [실무]

좋은 FAQ:

```md
Q. Chunk Size는 어떻게 정해?

A.  
하나의 개념이 독립적으로 이해될 정도로 유지하되 여러 개념이 섞이지 않도록 조정한다.
```

좋은 이유:

- 실제 사용자 질문 형태
- 핵심 Keyword 포함
- 답변 짧음
- Retrieval Query와 직접 매칭 가능

나쁜 FAQ:

```md
Q. Chunk
```

나쁜 이유:

- 질문 형태가 아님
- 답변 없음
- 검색 의도 불명확
- Agent가 활용하기 어려움

한국어 + 영어 병기 FAQ:

```md
Q. Query Embedding은 뭐야?

A.  
사용자 질문(User Query)을 Embedding Model로 Vector로 변환하는 과정이다.
```

---

### [주의]

- FAQ 내부에 무분별하게 `---`를 넣지 않는다.
- 질문만 있고 답변 없는 FAQ를 만들지 않는다.
- 답변을 장문으로 작성하지 않는다.
- 같은 FAQ를 모든 문서에 과도하게 반복하지 않는다.
- 질문이 너무 추상적이면 Retrieval 효과가 낮다.
- FAQ는 문서 내용과 직접 관련된 질문으로 작성한다.
- `[면접]` 섹션을 사용하지 않는다.

---

### [FAQ]

Q. FAQ는 왜 RAG 문서에 중요해?

A.
실제 사용자 질문과 문서 Chunk가 직접 매칭될 가능성을 높여 Retrieval 품질을 개선한다.

Q. FAQ 답변은 길게 써도 돼?

A.
권장하지 않는다. A는 1~4줄로 짧고 명확하게 작성한다.

Q. 질문만 있는 FAQ도 괜찮아?

A.
안 된다. FAQ는 반드시 Q와 A를 함께 작성해야 한다.

Q. `[면접]` 섹션을 써도 돼?

A.
사용하지 않는다. RAG 문서에서는 `[FAQ]` 섹션으로 통일한다.

---

# 8. Retrieval Queries Chunk

## 8.1 Retrieval Queries

### [개념]

Retrieval Queries는 문서 마지막에 배치하는 검색 강화용 FAQ Block이다.

사용자가 실제로 물어볼 가능성이 높은 질문을 모아 Query Matching을 강화한다.

기본 형식:

```md
# Retrieval Queries

### [FAQ]

Q. 질문
A. 답변
```

Retrieval Queries는 문서 전체의 검색 진입점을 만드는 역할을 한다.

---

### [핵심]

- 모든 RAG 문서 마지막에 Retrieval Queries를 포함한다.
- Retrieval Queries는 FAQ 형식을 사용한다.
- 실제 사용자 질문 형태로 작성한다.
- 핵심 Keyword를 포함한다.
- 한글 + 영어 기술 용어 병기를 활용한다.
- 답변은 짧고 명확하게 작성한다.
- 문서 내용과 직접 관련된 질문만 포함한다.
- 중복 질문을 과도하게 반복하지 않는다.

---

### [실무]

좋은 Retrieval Queries 예시:

```md
# Retrieval Queries

### [FAQ]

Q. Chunking이 뭐야?
A. 긴 문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk Size는 어떻게 정해?
A. 하나의 개념이 독립적으로 이해될 정도로 유지하되 여러 개념이 섞이지 않게 조정한다.

Q. Code Block은 어떻게 Chunking해야 해?
A. Code Block 중간에서 자르지 말고 설명과 같은 Chunk에 유지한다.
```

Retrieval Queries 작성 기준:

```text
문서 핵심 개념
→ 질문으로 변환

사용자가 실제로 물어볼 표현
→ 자연어 질문으로 작성

기술 용어
→ 한국어 + 영어 병기

답변
→ 1~3줄 이내
```

---

### [주의]

- Retrieval Queries를 누락하지 않는다.
- 문서와 관련 없는 질문을 넣지 않는다.
- 모든 문서에 동일한 질문을 반복하지 않는다.
- 답변을 장문으로 만들지 않는다.
- FAQ 내부 구분선을 과도하게 사용하지 않는다.
- Retrieval Queries는 별도 Header로 유지한다.

---

### [FAQ]

Q. Retrieval Queries는 뭐야?

A.
문서 마지막에 배치하는 검색 강화용 FAQ Block이다.

Q. Retrieval Queries는 왜 필요해?

A.
사용자 Query와 문서가 더 잘 매칭되도록 검색 진입점을 만들어 Retrieval 품질을 높인다.

Q. Retrieval Queries에는 어떤 질문을 넣어야 해?

A.
문서 핵심 개념과 실제 사용자가 물어볼 가능성이 높은 질문을 넣어야 한다.

Q. 모든 문서에 Retrieval Queries가 있어야 해?

A.
그렇다. RAG 문서에서는 문서 마지막에 Retrieval Queries를 포함하는 것이 필수다.

---

# 9. Metadata Core

## 9.1 Metadata

### [개념]

Metadata는 Chunk의 출처, 도메인, 레벨, 섹션, 제목, 태그 같은 부가 정보다.

Metadata는 Vector 자체보다 사람이 이해할 수 있는 문맥 정보를 제공한다.
Agent는 Metadata를 사용해 검색 결과의 출처와 우선순위를 판단할 수 있다.

Metadata 예시:

```json
{
  "source": "RAG Doc",
  "fileName": "Embedding_Model_Semantic_Search_Part02_Chunking_Metadata.md",
  "domain": "AI",
  "level": "Foundation",
  "part": "Part02",
  "section": "Chunking",
  "title": "Chunking Core",
  "tags": ["chunking", "metadata", "rag", "semantic-search"],
  "version": "2026.06"
}
```

---

### [핵심]

- Metadata는 검색 결과의 출처와 문맥을 보존한다.
- fileName은 원본 문서 추적에 필요하다.
- domain은 Agent Routing에 중요하다.
- level은 문서 난이도와 적용 범위 판단에 사용한다.
- part는 문서 세트 내 위치를 나타낸다.
- section은 답변 근거 제시에 유용하다.
- tags는 Filtered Retrieval과 검색 보강에 활용 가능하다.
- version은 문서 최신성 판단에 필요하다.
- Metadata 필드명은 문서 세트 전체에서 통일해야 한다.

---

### [실무]

권장 Metadata 필드:

| 필드      | 목적                     |
| --------- | ------------------------ |
| source    | 원본 출처                |
| fileName  | 파일명                   |
| domain    | 문서 도메인              |
| level     | Foundation / Expert 구분 |
| part      | Part 번호                |
| section   | 문서 Section             |
| title     | Chunk 제목               |
| tags      | 검색 필터 / 키워드       |
| version   | 문서 버전                |
| createdAt | 최초 작성일              |
| updatedAt | 수정일                   |

Agent 활용 예시:

```text
User Query:
Chunk Size 기준 알려줘

Retrieved Metadata:
domain=AI
level=Foundation
fileName=Embedding_Model_Semantic_Search_Part02_Chunking_Metadata.md
section=Chunk Size

Agent 판단:
AI Foundation 문서의 Chunk Size Section을 우선 근거로 사용
```

Filtered Retrieval 예시:

```text
domain=AI
level=Foundation
tags contains chunking
```

---

### [주의]

- Metadata 없이 Vector만 저장하지 않는다.
- Metadata 필드명을 문서마다 다르게 쓰지 않는다.
- domain / level / section을 누락하지 않는다.
- fileName이 실제 문서명과 다르면 출처 추적이 어렵다.
- section 값이 Header와 다르면 잘못된 근거 제시가 발생할 수 있다.
- version이 없으면 최신 문서 판단이 어렵다.
- 잘못된 Metadata는 잘못된 Agent Routing을 유발한다.

---

### [FAQ]

Q. Metadata는 왜 필요해?

A.
검색 결과의 출처, 도메인, 레벨, 섹션을 파악하고 필터링하기 위해 필요하다.

Q. Metadata가 없으면 어떻게 돼?

A.
검색은 될 수 있지만 출처 추적, Agent Routing, 근거 제시, 필터링이 어려워진다.

Q. Metadata에 꼭 들어가야 하는 값은?

A.
source, fileName, domain, level, part, section, title, tags, version을 권장한다.

Q. Metadata 필드명은 문서마다 달라도 돼?

A.
권장하지 않는다. 문서 세트 전체에서 동일한 필드명을 유지해야 한다.

---

# 10. Metadata for Agent Routing

## 10.1 Domain Level Section Metadata

### [개념]

Agent Routing은 사용자 요청을 적절한 Agent와 RAG 문서로 연결하는 과정이다.

Metadata는 Agent가 어떤 문서를 우선 참조해야 하는지 판단하는 기준이 된다.

기본 Routing 구조:

```text
User Query
→ Intent Detection
→ Domain Selection
→ Level Selection
→ Section Filtering
→ Retrieved Context
→ Agent Answer
```

---

### [핵심]

- domain은 어떤 Agent가 참조할지 결정하는 데 사용한다.
- level은 Foundation / Expert 문서 선택에 사용한다.
- section은 세부 근거 위치를 찾는 데 사용한다.
- tags는 Filtered Retrieval에 활용된다.
- part는 문서 세트의 흐름을 파악하는 데 도움된다.
- fileName은 근거 출처 표시와 문서 유지보수에 필요하다.
- Metadata가 정확해야 Multi-Agent System에서 잘못된 문서 참조를 줄일 수 있다.

---

### [실무]

Agent Routing Metadata 예시:

```json
{
  "domain": "AI",
  "level": "Foundation",
  "part": "Part02",
  "section": "Chunking",
  "title": "Chunk Size Strategy",
  "tags": ["chunk-size", "chunk-overlap", "rag-retrieval"]
}
```

Routing 예시:

```text
질문:
RAG 문서 Chunk Size는 어떻게 잡아?

Routing:
domain=AI
level=Foundation
section=Chunking
tags=chunk-size

참조 문서:
Embedding_Model_Semantic_Search_Part02_Chunking_Metadata.md
```

Multi-Agent 활용:

| Agent          | Metadata 활용                      |
| -------------- | ---------------------------------- |
| PM Agent       | 요청 의도와 domain 결정            |
| AI Agent       | AI / RAG 관련 문서 우선 검색       |
| Review Agent   | Retrieved Context와 근거 문서 검증 |
| Backend Agent  | Backend domain 문서 우선 검색      |
| Frontend Agent | Frontend domain 문서 우선 검색     |

---

### [주의]

- domain을 너무 넓게 지정하면 관련 없는 문서가 검색될 수 있다.
- level을 누락하면 Foundation과 Expert 문서가 섞일 수 있다.
- section이 부정확하면 답변 근거가 흐려진다.
- tags를 과도하게 많이 넣으면 필터링 기준이 약해질 수 있다.
- Agent Routing은 Metadata와 Query를 함께 사용해야 한다.
- Metadata만으로 Semantic Search를 완전히 대체하지 않는다.

---

### [FAQ]

Q. Agent Routing에서 Metadata가 왜 중요해?

A.
사용자 요청을 적절한 Domain, Level, Section 문서로 연결하는 기준이 되기 때문이다.

Q. domain Metadata는 뭐에 써?

A.
AI, Backend, Frontend, DevOps 같은 문서 도메인을 구분하고 Agent가 참조할 문서를 선택하는 데 사용한다.

Q. level Metadata는 뭐에 써?

A.
Foundation 문서와 Expert 문서를 구분해 현재 단계에 맞는 문서를 선택하는 데 사용한다.

Q. Metadata만 있으면 Semantic Search가 필요 없어?

A.
아니다. Metadata는 필터링과 Routing에 도움을 주고, Semantic Search는 의미 기반 검색을 수행한다.

---

# 11. Chunking Troubleshooting

## 11.1 Retrieval Failure from Chunking

### [개념]

Chunking 문제는 RAG 검색 실패의 주요 원인이다.

검색 결과가 없거나 관련 없는 문서가 검색될 때 Embedding Model을 교체하기 전에 Chunk 구조를 먼저 점검해야 한다.

---

### [Troubleshooting]

문제:

- 관련 문서가 있는데 Retrieval 결과에 나타나지 않음

원인:

- Chunk 제목이 불명확함
- Query 표현과 문서 표현 불일치
- 핵심 Keyword 누락
- Chunk가 너무 큼
- Chunk가 너무 작음
- Metadata 누락
- Embedding 재생성 누락

해결:

- Header에 핵심 Keyword 추가
- FAQ / Retrieval Queries 추가
- 한글 + 영어 기술 용어 병기
- Chunk를 주제별로 재분리
- Metadata에 domain / level / section 추가
- 문서 수정 후 Embedding 재생성

---

문제:

- 관련 없는 Chunk가 Top-K에 포함됨

원인:

- Chunk에 여러 개념 혼합
- Top-K가 너무 큼
- Similarity Threshold가 낮음
- Overlap이 과도함
- 공통 단어가 많음
- Metadata Filter 없음

해결:

- Chunk를 하나의 개념 중심으로 분리
- Top-K 조정
- Threshold 조정
- Overlap 줄이기
- Metadata Filter 적용
- Reranking 적용 검토

---

문제:

- 검색은 됐는데 답변이 틀림

원인:

- Retrieved Context가 불충분함
- 코드와 설명이 분리됨
- Chunk가 너무 단편적임
- 서로 충돌하는 Chunk 포함
- Prompt Grounding 규칙 부족

해결:

- Code Block과 설명을 같은 Chunk에 유지
- 관련 개념이 함께 검색되도록 Section 구조 개선
- 충돌 문서 Version 정리
- Prompt에 문서 근거 우선 규칙 추가
- Review Agent가 Retrieved Context 검증

---

문제:

- 비슷한 문서가 너무 많이 검색됨

원인:

- Chunk Overlap 과다
- 중복 설명 반복
- Retrieval Queries가 문서마다 동일
- Deduplication 없음

해결:

- Overlap 축소
- 중복 문장 제거
- Retrieval Queries를 문서별로 차별화
- 검색 결과 Deduplication 적용
- Metadata 기준 중복 제거

---

### [FAQ]

Q. 검색 결과가 안 나오면 무엇부터 봐야 해?

A.
Query 표현, Chunk 제목, 핵심 Keyword, Metadata, Embedding 재생성 여부를 먼저 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?

A.
Chunk를 주제별로 분리하고 Top-K, Threshold, Metadata Filter, Reranking을 검토한다.

Q. 중복 Chunk가 너무 많이 검색되면 어떻게 해?

A.
Chunk Overlap을 줄이고 중복 설명을 제거하며 Deduplication을 적용한다.

Q. 검색은 됐는데 답변이 틀리면 Chunking 문제일 수 있어?

A.
있다. Context가 부족하거나 코드와 설명이 분리된 경우 답변 품질이 낮아질 수 있다.

---

# 12. Best Practice

## 12.1 Chunking Metadata Best Practice

### [Best Practice]

Chunking Best Practice:

- Header 중심으로 문서 작성
- 하나의 Chunk는 하나의 개념만 다룸
- Chunk 제목에 핵심 Keyword 포함
- Code Block과 설명을 같은 Chunk에 유지
- FAQ를 실제 사용자 질문 형태로 작성
- Retrieval Queries를 문서 마지막에 포함
- Chunk Size는 문서 목적에 따라 조정
- Chunk Overlap은 문맥 단절 방지용으로 최소 사용
- Semantic Boundary 기준으로 분리
- 중복 설명을 과도하게 반복하지 않음

Metadata Best Practice:

- source / fileName / domain / level / part / section / title / tags / version 포함
- Metadata 필드명 통일
- Header와 section Metadata 일치
- Agent Routing을 고려해 domain과 level 명확히 작성
- tags는 핵심 검색어 중심으로 작성
- version과 updatedAt 관리
- 문서 수정 후 Embedding 재생성
- Embedding Model 변경 시 전체 재색인

---

### [Checklist]

- [ ] Chunk 제목이 명확한가?
- [ ] Chunk가 하나의 개념만 다루는가?
- [ ] Chunk가 독립 검색되어도 의미를 유지하는가?
- [ ] Code Block이 중간에 잘리지 않았는가?
- [ ] 코드와 설명이 같은 Chunk에 있는가?
- [ ] FAQ가 실제 사용자 질문 형태인가?
- [ ] FAQ에 Q와 A가 모두 있는가?
- [ ] Retrieval Queries가 문서 마지막에 있는가?
- [ ] Chunk Size가 너무 작거나 크지 않은가?
- [ ] Chunk Overlap이 과도하지 않은가?
- [ ] Header에 핵심 Keyword가 포함되어 있는가?
- [ ] Metadata에 domain / level / section이 포함되어 있는가?
- [ ] fileName이 실제 문서명과 일치하는가?
- [ ] tags가 검색과 필터링에 유효한가?
- [ ] 문서 수정 후 Embedding 재생성 규칙이 있는가?

---

### [FAQ]

Q. Chunking Best Practice 핵심은 뭐야?

A.
하나의 Chunk가 하나의 개념을 명확히 다루고 독립 검색 가능하도록 만드는 것이다.

Q. Metadata Best Practice 핵심은 뭐야?

A.
출처, 도메인, 레벨, 섹션, 제목, 태그, 버전을 일관되게 기록하는 것이다.

Q. Chunk와 Metadata 중 뭐가 더 중요해?

A.
둘 다 중요하다. Chunk는 검색 단위이고 Metadata는 검색 결과의 출처와 Routing 기준이다.

Q. RAG 문서 검수에서 가장 먼저 볼 것은?

A.
Chunk 제목, 하나의 개념 여부, FAQ 품질, Metadata 누락, Retrieval Queries 포함 여부를 먼저 확인한다.

---

# Retrieval Queries

### [FAQ]

Q. Chunking이 뭐야?
A. 긴 문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk가 왜 중요해?
A. RAG는 Chunk 단위로 문서를 검색하므로 Chunk 품질이 Retrieval 품질을 크게 좌우한다.

Q. 좋은 Chunk는 어떤 구조야?
A. 하나의 개념을 다루고 제목이 명확하며 핵심 키워드, 설명, 예제, FAQ가 검색 가능하게 포함된 구조다.

Q. Chunk Size는 어떻게 정해?
A. 하나의 개념이 독립적으로 이해될 정도로 유지하되 여러 개념이 섞이지 않도록 조정한다.

Q. 작은 Chunk가 항상 좋아?
A. 아니다. 정밀 검색에는 유리하지만 문맥이 부족해 답변 품질이 낮아질 수 있다.

Q. 큰 Chunk가 항상 좋아?
A. 아니다. 문맥은 풍부하지만 여러 개념이 섞여 관련 없는 정보가 검색될 수 있다.

Q. Chunk Overlap은 왜 써?
A. Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다.

Q. Overlap은 크게 잡을수록 좋아?
A. 아니다. 너무 크면 중복 Chunk가 많이 검색되어 Context 품질이 낮아질 수 있다.

Q. Semantic Chunking이 뭐야?
A. 문서를 의미 단위로 나누는 방식이다. 개념의 경계와 문맥의 완결성을 기준으로 Chunk를 만든다.

Q. Header Based Chunking이 뭐야?
A. Markdown Header를 기준으로 문서를 Chunk로 나누는 방식이다.

Q. Header가 검색 품질에 영향을 줘?
A. 그렇다. Header는 Chunk의 주제를 명확히 하고 Query Matching을 강화한다.

Q. Code Block은 어떻게 Chunking해야 해?
A. Code Block 중간에서 자르지 말고 가능하면 설명과 같은 Chunk에 유지한다.

Q. 코드만 Chunk로 저장하면 안 돼?
A. 가능은 하지만 권장하지 않는다. 설명이 없으면 Agent가 코드의 목적과 사용 조건을 오해할 수 있다.

Q. FAQ는 왜 RAG 문서에 중요해?
A. 실제 사용자 질문과 문서 Chunk가 직접 매칭될 가능성을 높여 Retrieval 품질을 개선한다.

Q. FAQ 답변은 길게 써도 돼?
A. 권장하지 않는다. A는 1~4줄로 짧고 명확하게 작성한다.

Q. 질문만 있는 FAQ도 괜찮아?
A. 안 된다. FAQ는 반드시 Q와 A를 함께 작성해야 한다.

Q. Retrieval Queries는 뭐야?
A. 문서 마지막에 배치하는 검색 강화용 FAQ Block이다.

Q. Retrieval Queries는 왜 필요해?
A. 사용자 Query와 문서가 더 잘 매칭되도록 검색 진입점을 만들어 Retrieval 품질을 높인다.

Q. Metadata는 왜 필요해?
A. 검색 결과의 출처, 도메인, 레벨, 섹션을 파악하고 필터링하기 위해 필요하다.

Q. Metadata에 꼭 들어가야 하는 값은?
A. source, fileName, domain, level, part, section, title, tags, version을 권장한다.

Q. Agent Routing에서 Metadata가 왜 중요해?
A. 사용자 요청을 적절한 Domain, Level, Section 문서로 연결하는 기준이 되기 때문이다.

Q. domain Metadata는 뭐에 써?
A. AI, Backend, Frontend, DevOps 같은 문서 도메인을 구분하고 Agent가 참조할 문서를 선택하는 데 사용한다.

Q. level Metadata는 뭐에 써?
A. Foundation 문서와 Expert 문서를 구분해 현재 단계에 맞는 문서를 선택하는 데 사용한다.

Q. 검색 결과가 안 나오면 무엇부터 봐야 해?
A. Query 표현, Chunk 제목, 핵심 Keyword, Metadata, Embedding 재생성 여부를 먼저 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?
A. Chunk를 주제별로 분리하고 Top-K, Threshold, Metadata Filter, Reranking을 검토한다.

Q. 중복 Chunk가 너무 많이 검색되면 어떻게 해?
A. Chunk Overlap을 줄이고 중복 설명을 제거하며 Deduplication을 적용한다.

Q. Chunking Best Practice 핵심은 뭐야?
A. 하나의 Chunk가 하나의 개념을 명확히 다루고 독립 검색 가능하도록 만드는 것이다.

Q. Metadata Best Practice 핵심은 뭐야?
A. 출처, 도메인, 레벨, 섹션, 제목, 태그, 버전을 일관되게 기록하는 것이다.

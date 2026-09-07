# Vector Database & RAG Part03 Chunking and Metadata

---

# 1. Chunking Core

## 1.1 Chunking Definition

### [개념]

Chunking은 원본 문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Chunk는 Vector Database에 저장되고 Retrieval 단계에서 검색되는 최소 문서 단위다.

RAG에서 LLM은 보통 전체 문서를 직접 읽지 않는다.

LLM은 사용자 Query와 관련성이 높은 Chunk를 Retrieved Context로 받아 답변을 생성한다.

기본 흐름은 다음과 같다.

```text
Markdown Document
→ Header Split
→ Semantic Boundary Check
→ Chunk Size Check
→ Metadata Attach
→ Embedding
→ Vector Store
```

Chunking 품질이 낮으면 문서가 존재해도 검색되지 않거나, 검색되어도 답변에 필요한 문맥이 부족할 수 있다.

---

### [핵심]

- Chunking은 문서를 검색 단위로 분리하는 과정
- Chunk는 Retrieval의 최소 단위
- 하나의 Chunk는 하나의 핵심 개념만 다루는 것이 좋음
- Chunk는 독립 검색되어도 의미를 가져야 함
- Header는 Chunk Boundary로 활용 가능
- Code Block은 중간에 분리하지 않음
- FAQ와 Retrieval Queries는 Query Matching을 강화함
- Chunk 품질은 Retrieval 품질과 직접 연결됨

---

### [실무]

2026 실무 기준 RAG 문서의 Chunking은 단순 글자 수 분할보다 의미 단위 분할을 우선한다.

개인 AI Agent용 RAG에서는 다음 기준을 적용한다.

- Header 기반 Chunking 우선
- 의미 단위가 깨지지 않도록 분리
- Code Example과 설명은 가능한 같은 Chunk에 유지
- FAQ는 실제 사용자 질문 표현과 가깝게 작성
- Retrieval Queries는 문서 마지막에 별도 강화 블록으로 작성
- Metadata로 Chunk의 출처와 역할을 추적
- Chunk 수정 후 Reindex 수행

RAG 문서 제작 시 Chunk는 사람이 읽는 문단보다 Agent가 검색하고 재사용하기 좋은 단위로 설계한다.

---

### [FAQ]

Q. Chunking이 뭐야?

A.
문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk는 왜 중요해?

A.
Chunk가 검색 단위이기 때문에 Chunk가 나쁘면 관련 문서가 있어도 검색되지 않을 수 있다.

Q. Chunk는 어느 정도 크기가 좋아?

A.
일반적으로 300~1200 tokens 범위가 권장되지만, 문서 성격과 검색 결과에 따라 조정해야 한다.

Q. Chunk는 글자 수 기준으로만 나누면 돼?

A.
아니다. 의미 단위와 Header 구조를 우선 고려해야 한다.

Q. Chunking 실패는 어떤 문제를 만들 수 있어?

A.
검색 누락, 문맥 부족, 무관한 Context 포함, 답변 오류를 만들 수 있다.

---

# 2. Chunk Design Principles

## 2.1 Independent Chunk

### [개념]

Independent Chunk는 단독으로 검색되어도 의미를 이해할 수 있는 Chunk다.

RAG Retrieval에서는 전체 문서가 아니라 특정 Chunk만 검색될 수 있다.

따라서 Chunk 내부에는 주제, 핵심 개념, 사용 상황, 주의점이 최소한으로 포함되어야 한다.

나쁜 Chunk는 앞뒤 문맥이 없으면 의미가 사라진다.

좋은 Chunk는 해당 Chunk만 검색되어도 Agent가 답변이나 코드 생성에 활용할 수 있다.

---

### [핵심]

- Chunk는 독립 검색 가능해야 함
- 하나의 Chunk에는 하나의 핵심 주제만 포함
- 제목과 본문이 같은 주제를 다뤄야 함
- 정의, 핵심, 실무 기준이 함께 있으면 검색 활용성이 높음
- 앞 Chunk에만 의존하는 표현 금지
- `위 내용`, `아래 내용`, `앞에서 말한 것` 같은 표현 최소화
- Agent가 단독 Chunk로 판단할 수 있어야 함

---

### [실무]

좋은 Chunk 구조는 다음과 같다.

```text
## 2.1 Independent Chunk

### [개념]

Independent Chunk는 단독으로 검색되어도 의미를 이해할 수 있는 Chunk다.

### [핵심]

- Chunk는 독립 검색 가능해야 함
- 하나의 Chunk에는 하나의 핵심 주제만 포함

### [실무]

Agent가 단독 Chunk로 답변 또는 검증에 활용할 수 있도록 작성한다.

### [FAQ]

Q. Independent Chunk가 뭐야?

A.
단독으로 검색되어도 의미를 이해할 수 있는 Chunk다.
```

나쁜 Chunk 구조는 다음과 같다.

```text
## 2.1 기타

앞에서 설명한 것처럼 이것도 중요하다.
자세한 기준은 아래를 보면 된다.
```

두 번째 예시는 검색되더라도 주제와 의미가 불명확하다.

---

### [FAQ]

Q. Independent Chunk가 뭐야?

A.
단독으로 검색되어도 의미를 이해할 수 있는 Chunk다.

Q. Chunk가 독립적이어야 하는 이유는 뭐야?

A.
RAG는 전체 문서가 아니라 일부 Chunk만 검색해서 LLM Context로 넣기 때문이다.

Q. Chunk에서 피해야 하는 표현은 뭐야?

A.
`위 내용`, `앞에서 설명한 것`, `아래 예시`처럼 외부 문맥에 의존하는 표현이다.

Q. 좋은 Chunk는 어떤 구조야?

A.
명확한 제목, 정의, 핵심 포인트, 실무 기준, FAQ를 포함한 구조다.

Q. Chunk가 독립적이지 않으면 어떻게 돼?

A.
검색은 되더라도 문맥이 부족해 Agent가 잘못 판단할 수 있다.

---

## 2.2 Single Concept Chunk

### [개념]

Single Concept Chunk는 하나의 Chunk가 하나의 핵심 개념만 다루도록 설계하는 원칙이다.

한 Chunk에 여러 주제가 섞이면 Similarity Search에서 Chunk의 의미가 흐려진다.

예를 들어 Chunking, Metadata, Embedding, Retrieval을 한 Chunk에 모두 넣으면 사용자 Query가 어느 주제와 매칭되어야 하는지 모호해진다.

Chunk는 검색 정밀도를 높이기 위해 주제 단위로 분리해야 한다.

---

### [핵심]

- 하나의 Chunk는 하나의 핵심 개념 중심
- 여러 개념 혼합 금지
- Chunk 제목과 본문 주제 일치 필요
- 비교가 필요한 경우 Comparison Table로 구조화
- 관련 개념은 별도 Chunk로 분리 후 상호 참조 가능
- Chunk가 너무 넓으면 Retrieval Precision 저하
- Chunk가 너무 좁으면 Context 부족 가능

---

### [실무]

Single Concept Chunk 분리 예시는 다음과 같다.

```text
Chunk 1: Chunking Definition
Chunk 2: Chunk Size
Chunk 3: Chunk Overlap
Chunk 4: Semantic Chunking
Chunk 5: Metadata Attach
Chunk 6: Chunk ID Policy
```

나쁜 분리:

```text
Chunk 1: Chunking, Metadata, Embedding, Retrieval 전체 설명
```

AI Agent용 RAG 문서에서는 한 Chunk가 하나의 판단 기준으로 사용될 수 있어야 한다.

Review Agent가 Chunk를 검색했을 때 해당 Chunk만으로 검증 기준을 확인할 수 있어야 한다.

---

### [FAQ]

Q. Single Concept Chunk가 뭐야?

A.
하나의 Chunk가 하나의 핵심 개념만 다루도록 설계하는 원칙이다.

Q. 여러 개념을 한 Chunk에 넣으면 왜 안 좋아?

A.
Chunk 의미가 흐려져 Similarity Search 정밀도가 낮아질 수 있기 때문이다.

Q. 관련 개념은 같은 Chunk에 넣어도 돼?

A.
비교나 연결 설명은 가능하지만 핵심 주제가 다르면 별도 Chunk로 분리하는 것이 좋다.

Q. 너무 작은 Chunk는 괜찮아?

A.
너무 작으면 답변에 필요한 문맥이 부족할 수 있다.

Q. Chunk 분리 기준은 뭐야?

A.
사용자 Query 하나에 답할 수 있는 하나의 핵심 개념 단위로 분리한다.

---

# 3. Chunk Size

## 3.1 Chunk Size Rule

### [개념]

Chunk Size는 하나의 Chunk에 포함되는 Text 양이다.

Chunk Size는 Retrieval Precision, Recall, Context Quality에 영향을 준다.

Chunk가 너무 작으면 검색은 정밀할 수 있지만 답변에 필요한 문맥이 부족할 수 있다.

Chunk가 너무 크면 문맥은 충분할 수 있지만 여러 주제가 섞여 검색 정밀도가 떨어질 수 있다.

RAG 문서 제작 기준에서는 300~1200 tokens 범위를 기본 권장값으로 사용한다.

---

### [핵심]

- Chunk Size는 검색 단위의 크기
- 작은 Chunk는 정밀도에 유리
- 큰 Chunk는 문맥 확보에 유리
- 너무 작은 Chunk는 Context 부족 위험
- 너무 큰 Chunk는 주제 혼합 위험
- 권장 범위는 300~1200 tokens
- 문서 유형과 Retrieval 결과에 따라 조정 필요

---

### [실무]

Chunk Size 결정 기준은 다음과 같다.

| Chunk Size   | 장점               | 단점                | 적합한 경우          |
| ------------ | ------------------ | ------------------- | -------------------- |
| Small Chunk  | 검색 정밀도 높음   | 문맥 부족 가능      | FAQ, 정의, 설정값    |
| Medium Chunk | 정밀도와 문맥 균형 | 구조 설계 필요      | 기술 개념, 실무 기준 |
| Large Chunk  | 문맥 풍부          | 무관 정보 포함 가능 | 긴 절차, 복합 Flow   |

개인 AI RAG 문서에서는 Medium Chunk를 기본으로 사용한다.

단, FAQ와 Retrieval Queries는 검색 매칭 강화를 위해 짧고 반복적인 형태를 허용한다.

Code Example은 중간 분리하지 않고 설명과 함께 유지한다.

---

### [FAQ]

Q. Chunk Size가 뭐야?

A.
하나의 Chunk에 포함되는 Text 양이다.

Q. Chunk Size 권장 범위는 얼마야?

A.
일반적으로 300~1200 tokens 범위를 권장한다.

Q. Chunk가 너무 작으면 뭐가 문제야?

A.
답변에 필요한 문맥이 부족할 수 있다.

Q. Chunk가 너무 크면 뭐가 문제야?

A.
여러 주제가 섞여 검색 정밀도가 떨어질 수 있다.

Q. Chunk Size는 고정값이면 돼?

A.
아니다. 문서 유형, Query 유형, Retrieval 결과에 따라 조정해야 한다.

---

## 3.2 Chunk Size Optimization

### [개념]

Chunk Size Optimization은 검색 결과를 평가하면서 Chunk 크기를 조정하는 과정이다.

처음부터 완벽한 Chunk Size를 정하기는 어렵다.

Golden Query로 Retrieval 결과를 확인하고, 기대 Chunk가 검색되는지, 검색된 Chunk가 답변에 충분한지 평가해야 한다.

Chunk Size는 문서 구조, Embedding Model, Top-K, Threshold, Context Window와 함께 조정한다.

---

### [핵심]

- Chunk Size는 평가 기반으로 조정
- Golden Query로 검색 결과 확인
- 기대 Chunk가 Top-K에 들어오는지 확인
- 검색된 Chunk가 답변에 충분한지 확인
- 무관 정보가 섞이면 Chunk를 줄임
- 문맥이 부족하면 Chunk를 키우거나 Overlap 적용
- Chunk 변경 후 Reindex 필요

---

### [실무]

Chunk Size Optimization 절차는 다음과 같다.

```text
Golden Query 작성
→ Retrieval 실행
→ Expected Chunk 포함 여부 확인
→ Context Sufficiency 확인
→ Noise 포함 여부 확인
→ Chunk Size 조정
→ Reindex
→ 재검증
```

실패 사례별 조정 기준은 다음과 같다.

| 문제                      | 원인                   | 조정                    |
| ------------------------- | ---------------------- | ----------------------- |
| 기대 문서가 검색되지 않음 | Chunk 제목/키워드 약함 | Header, FAQ 보강        |
| 검색되지만 답변 불충분    | Chunk가 너무 작음      | Chunk 확대 또는 Overlap |
| 무관 내용이 많이 포함됨   | Chunk가 너무 큼        | 주제별 분리             |
| 중복 Chunk가 많이 검색됨  | Overlap 과다           | Overlap 축소            |
| 특정 용어 검색 실패       | 키워드 부족            | 한글/영어 용어 병기     |

---

### [FAQ]

Q. Chunk Size Optimization이 뭐야?

A.
검색 결과를 평가하면서 Chunk 크기를 조정하는 과정이다.

Q. Chunk Size는 어떻게 검증해?

A.
Golden Query로 기대 Chunk가 Top-K에 들어오는지 확인한다.

Q. 검색되지만 답변이 부족하면 어떻게 해?

A.
Chunk를 조금 키우거나 Chunk Overlap을 적용할 수 있다.

Q. 검색 결과에 무관한 내용이 많으면 어떻게 해?

A.
Chunk를 더 작은 주제 단위로 분리해야 한다.

Q. Chunk Size를 바꾸면 Reindex해야 해?

A.
해야 한다. Chunk 구조가 바뀌면 Embedding Vector도 다시 생성해야 한다.

---

# 4. Chunk Overlap

## 4.1 Chunk Overlap Definition

### [개념]

Chunk Overlap은 인접한 Chunk 사이에 일부 내용을 중복 포함하는 방식이다.

Chunk Overlap은 Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다.

예를 들어 중요한 설명이 Chunk 끝과 다음 Chunk 시작에 걸쳐 있으면, Overlap이 없을 때 Retrieval Context가 불완전할 수 있다.

하지만 Overlap이 과하면 중복 Chunk가 많이 검색되고 Context Budget을 낭비할 수 있다.

---

### [핵심]

- Chunk Overlap은 인접 Chunk 간 문맥 중복
- Chunk 경계의 문맥 손실을 줄임
- 너무 적으면 문맥 단절 가능
- 너무 많으면 중복 검색 증가
- Overlap 과다는 Context Budget 낭비
- Code Block 중간 분리 방지와 함께 고려
- Header 기반 Chunking에서는 Overlap을 과하게 쓰지 않음

---

### [실무]

Chunk Overlap은 다음 상황에서 유용하다.

- 절차 설명이 여러 Chunk에 걸쳐 이어질 때
- 용어 정의와 예제가 분리될 위험이 있을 때
- 긴 문단을 크기 기준으로 나눠야 할 때
- 앞뒤 문맥이 검색 정확도에 영향을 줄 때

Chunk Overlap이 불필요하거나 줄여야 하는 경우는 다음과 같다.

- Header 단위로 의미가 명확히 분리된 문서
- FAQ처럼 독립 질문/답변 구조인 문서
- 중복 검색이 자주 발생하는 문서
- Context Window가 작아 중복이 비용이 되는 구조

---

### [FAQ]

Q. Chunk Overlap이 뭐야?

A.
인접한 Chunk 사이에 일부 내용을 중복 포함하는 방식이다.

Q. Chunk Overlap은 왜 써?

A.
Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다.

Q. Overlap이 많으면 좋은 거 아니야?

A.
아니다. 너무 많으면 중복 검색이 늘고 Context Budget을 낭비한다.

Q. Header 기반 Chunking에도 Overlap이 필요해?

A.
경우에 따라 필요하지만 의미 단위가 명확하면 과한 Overlap은 피하는 것이 좋다.

Q. FAQ에도 Overlap을 적용해야 해?

A.
대부분 필요하지 않다. FAQ는 독립 질문/답변 구조이기 때문이다.

---

## 4.2 Overlap Failure

### [개념]

Overlap Failure는 Chunk Overlap 설정이 부적절해 Retrieval 품질이 떨어지는 문제다.

Overlap이 부족하면 문맥이 끊기고, Overlap이 과하면 중복 Chunk가 많이 검색된다.

RAG에서는 Context Budget이 제한되어 있기 때문에 중복 Chunk가 많으면 중요한 다른 Chunk가 제외될 수 있다.

---

### [핵심]

- Overlap 부족은 문맥 단절 유발
- Overlap 과다는 중복 검색 유발
- 중복 Context는 답변 품질 저하 가능
- 중요한 Chunk가 Top-K에서 밀릴 수 있음
- Deduplication 기준 필요
- Overlap 변경 후 Reindex 필요
- Golden Query로 검증 필요

---

### [실무]

Overlap Failure 해결 형식은 다음과 같다.

```text
문제:
검색 결과에 비슷한 Chunk가 반복됨

원인:
Chunk Overlap 과다
Chunk Size 과소
유사한 FAQ 반복
Deduplication 없음

해결:
Overlap 축소
Chunk Size 재조정
중복 FAQ 정리
Context Deduplication 적용
Reindex 후 Golden Query 검증
```

문맥 단절이 발생하는 경우는 다음과 같이 처리한다.

```text
문제:
검색된 Chunk만으로 답변 문맥이 부족함

원인:
Chunk Overlap 부족
Chunk Size 과소
Code Example과 설명 분리

해결:
Overlap 소폭 증가
Chunk 통합
Code Example과 설명 같은 Chunk 유지
Reindex 후 검증
```

---

### [FAQ]

Q. Overlap Failure가 뭐야?

A.
Chunk Overlap 설정이 부적절해 검색 품질이 떨어지는 문제다.

Q. Overlap이 부족하면 어떻게 돼?

A.
Chunk 경계에서 문맥이 끊겨 답변에 필요한 정보가 부족할 수 있다.

Q. Overlap이 과하면 어떻게 돼?

A.
중복 Chunk가 많이 검색되어 Context Budget을 낭비할 수 있다.

Q. Overlap 문제는 어떻게 확인해?

A.
Golden Query 검색 결과에서 중복 Chunk 비율과 문맥 충분성을 확인한다.

Q. Overlap을 바꾸면 Reindex해야 해?

A.
해야 한다. Chunk 내용과 Embedding Vector가 바뀌기 때문이다.

---

# 5. Semantic Chunking

## 5.1 Semantic Boundary

### [개념]

Semantic Chunking은 문서의 의미 경계를 기준으로 Chunk를 나누는 방식이다.

단순 글자 수나 토큰 수 기준으로 자르는 것이 아니라, 개념, 절차, 코드 예제, FAQ, 비교표 같은 의미 단위를 기준으로 분리한다.

RAG 문서에서는 Semantic Chunking이 중요하다.

사용자 Query는 보통 특정 개념이나 문제를 묻기 때문에, Chunk도 그 질문에 답할 수 있는 의미 단위여야 한다.

---

### [핵심]

- Semantic Chunking은 의미 경계 기반 분리
- 단순 길이 기준보다 Retrieval 품질에 유리
- 개념, 절차, 예제, 주의점 단위로 분리
- Header 기반 Chunking과 함께 사용 가능
- Code Block과 설명의 의미 연결 유지
- FAQ는 질문/답변 단위로 의미 분리
- 의미 경계 변경 시 Reindex 필요

---

### [실무]

Semantic Chunking 기준은 다음과 같다.

| 의미 단위       | Chunk 분리 기준                 |
| --------------- | ------------------------------- |
| 개념 정의       | 하나의 용어 또는 구조 설명      |
| 실무 기준       | 하나의 적용 기준 또는 운영 규칙 |
| 코드 예제       | 설명 + 핵심 코드 + 주의점       |
| 비교            | 비교 대상과 판단 기준           |
| Troubleshooting | 문제 + 원인 + 해결              |
| FAQ             | 질문 + 답변                     |
| Checklist       | 하나의 검수 목적 단위           |

Semantic Chunking은 기술 문서에서 특히 중요하다.

예를 들어 `Chunk Size`, `Chunk Overlap`, `Semantic Chunking`은 모두 Chunking 관련이지만 검색 의도가 다르므로 별도 Chunk로 분리해야 한다.

---

### [FAQ]

Q. Semantic Chunking이 뭐야?

A.
문서의 의미 경계를 기준으로 Chunk를 나누는 방식이다.

Q. 글자 수 기준 Chunking과 뭐가 달라?

A.
글자 수 기준은 길이에 맞춰 자르고, Semantic Chunking은 개념과 문맥 단위로 나눈다.

Q. RAG 문서에서 Semantic Chunking이 중요한 이유는 뭐야?

A.
사용자 Query가 특정 개념이나 문제를 묻기 때문에 Chunk도 의미 단위로 답할 수 있어야 하기 때문이다.

Q. Semantic Chunking은 Header 기반 Chunking과 같이 쓸 수 있어?

A.
그렇다. Header를 1차 경계로 사용하고 의미 단위로 세부 조정할 수 있다.

Q. Semantic Boundary를 바꾸면 Reindex해야 해?

A.
해야 한다. Chunk 내용이 바뀌면 Embedding Vector도 다시 생성해야 한다.

---

# 6. Header Based Chunking

## 6.1 Header as Chunk Boundary

### [개념]

Header Based Chunking은 Markdown Header를 기준으로 Chunk를 나누는 방식이다.

RAG 문서에서 Header는 단순 제목이 아니라 검색 신호이자 Chunk Boundary다.

명확한 Header는 사용자 Query와 문서 Chunk의 의미를 연결한다.

예를 들어 `# 4. Chunk Overlap`은 Chunk Overlap 관련 질문과 매칭되기 쉽다.

반대로 `# 기타`, `# 설명`, `# 참고` 같은 Header는 검색 의미가 약하다.

---

### [핵심]

- Header는 Chunk Boundary로 활용 가능
- Header는 Retrieval Signal 역할
- Header에는 핵심 키워드 포함 필요
- Header Level을 일관되게 유지
- 모호한 Header 사용 금지
- 한글과 영어 핵심 용어 병기 가능
- Header 변경 후 Reindex 필요

---

### [실무]

권장 Header 구조는 다음과 같다.

```text
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

RAG 문서에서 좋은 Header 예시는 다음과 같다.

```text
# 3. Chunk Size

## 3.1 Chunk Size Rule

# 4. Chunk Overlap

## 4.1 Chunk Overlap Definition

# 5. Semantic Chunking

## 5.1 Semantic Boundary
```

나쁜 Header 예시는 다음과 같다.

```text
# 설명

## 기타

## 정리

## 내용
```

Header에는 실제 사용자가 검색할 가능성이 높은 용어를 포함한다.

---

### [FAQ]

Q. Header Based Chunking이 뭐야?

A.
Markdown Header를 기준으로 Chunk를 나누는 방식이다.

Q. Header가 왜 Retrieval에 중요해?

A.
Header는 Chunk의 주제를 명확히 보여주는 검색 신호이기 때문이다.

Q. 좋은 Header는 뭐야?

A.
핵심 키워드가 포함되고 Chunk의 주제를 명확히 설명하는 Header다.

Q. 나쁜 Header는 뭐야?

A.
`기타`, `설명`, `내용`처럼 검색 의미가 약한 Header다.

Q. Header를 수정하면 Reindex해야 해?

A.
해야 한다. Header는 Chunk 의미와 Embedding 결과에 영향을 준다.

---

# 7. Code Block Chunking

## 7.1 Code Example Boundary

### [개념]

Code Block Chunking은 코드 예제를 Chunk로 나눌 때 코드 문법과 설명의 연결을 보존하는 규칙이다.

RAG Agent는 코드 예제를 검색하여 Code Generation, Code Review, Troubleshooting에 사용한다.

코드가 중간에 잘리면 Agent가 잘못된 패턴을 학습하거나 불완전한 코드를 생성할 수 있다.

Code Block은 가능한 설명, 사용 상황, 주의점과 같은 Chunk에 유지한다.

---

### [핵심]

- Code Block 중간 분리 금지
- 코드 설명과 Code Example은 같은 Chunk에 유지 권장
- 긴 전체 클래스보다 핵심 Snippet 권장
- 코드 언어 표시 권장
- 불필요한 import와 boilerplate 최소화
- 코드블록 `id=""` 제거
- Code Review용 주의점 포함 권장

---

### [실무]

RAG 문서에 적합한 Code Chunk 구조는 다음과 같다.

```text
### [개념]

Service Layer에서 조회 로직은 Repository 조회, 예외 처리, DTO 변환으로 구성한다.

### [예제]

Java Example:

public UserResDto getUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new EntityNotFoundException("User not found"));

    return UserResDto.from(user);
}

### [주의]

- Entity를 Controller로 직접 반환하지 않는다.
- 조회 실패 시 명확한 예외를 던진다.
```

실제 RAG 문서에 코드 예제를 넣을 때는 아래처럼 단일 Code Block을 사용한다.

```java
public UserResDto getUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new EntityNotFoundException("User not found"));

    return UserResDto.from(user);
}
```

Code Chunk는 다음 검색 표현과 매칭될 수 있어야 한다.

- Service 조회 코드
- Repository findById 예외 처리
- DTO 변환 예제
- Entity 직접 반환 금지
- Code Review 기준

---

### [FAQ]

Q. Code Block Chunking이 뭐야?

A.
코드 예제를 Chunk로 나눌 때 코드 문법과 설명의 연결을 보존하는 규칙이다.

Q. Code Block을 중간에 잘라도 돼?

A.
안 된다. 코드 문법이 깨지고 Agent가 불완전한 코드를 사용할 수 있다.

Q. 코드와 설명은 같은 Chunk에 있어야 해?

A.
가능하면 같은 Chunk에 있어야 코드 목적과 사용 조건을 함께 검색할 수 있다.

Q. 긴 전체 클래스를 넣어도 돼?

A.
가능은 하지만 RAG 문서에서는 핵심 로직 중심의 짧은 Snippet이 더 적합하다.

Q. 코드블록 id=""는 제거해야 해?

A.
해야 한다. 불필요한 속성은 RAG 문서 노이즈가 될 수 있다.

---

# 8. FAQ Chunk

## 8.1 FAQ for Retrieval

### [개념]

FAQ Chunk는 실제 사용자 질문 표현과 문서 개념을 연결하는 Retrieval 강화 Chunk다.

RAG에서 사용자 Query는 문서 제목과 다르게 입력될 수 있다.

FAQ는 사용자가 실제로 물어볼 문장을 문서 안에 포함시켜 Semantic Search와 Query Pattern Matching을 강화한다.

FAQ는 반드시 질문과 답변이 함께 있어야 한다.

Q만 있고 A가 없는 FAQ는 RAG 문서로 부적절하다.

---

### [핵심]

- FAQ는 Retrieval Hit를 높이는 핵심 구조
- 실제 사용자 질문 표현을 포함
- Q와 A를 반드시 함께 작성
- A는 짧고 명확하게 작성
- `[면접]` 대신 `[FAQ]` 사용
- 무분별한 구분선 사용 금지
- FAQ는 문서 마지막 Retrieval Queries와 함께 검색 강화 역할

---

### [실무]

좋은 FAQ 예시는 다음과 같다.

```text
### [FAQ]

Q. Chunking이 뭐야?

A.
문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk가 너무 크면 왜 문제야?

A.
여러 주제가 섞여 Similarity Search 정밀도가 떨어질 수 있다.
```

나쁜 FAQ 예시는 다음과 같다.

```text
### [FAQ]

Q. Chunking?

Q. 크기?

Q. 문제?
```

FAQ 작성 기준은 다음과 같다.

- 사용자가 실제로 물어볼 문장 사용
- 한글 질문과 영어 기술 용어 병기 가능
- 답변은 1~4줄 유지
- 질문은 개념, 실무, 문제 해결 중심으로 작성
- 동일 질문을 과도하게 반복하지 않음

---

### [FAQ]

Q. FAQ Chunk가 뭐야?

A.
실제 사용자 질문 표현과 문서 개념을 연결하는 Retrieval 강화 Chunk다.

Q. FAQ가 Retrieval에 왜 좋아?

A.
사용자 Query와 유사한 질문 문장을 문서에 포함하기 때문이다.

Q. FAQ에는 Q만 있어도 돼?

A.
안 된다. 반드시 Q와 A를 함께 작성해야 한다.

Q. FAQ 답변은 길어도 돼?

A.
길지 않은 것이 좋다. 보통 1~4줄로 명확하게 작성한다.

Q. `[면접]` 섹션을 써도 돼?

A.
쓰지 않는다. RAG 문서에서는 `[FAQ]`를 사용한다.

---

# 9. Retrieval Queries Chunk

## 9.1 Retrieval Queries Purpose

### [개념]

Retrieval Queries Chunk는 문서 마지막에 배치하는 검색 최적화 질문/답변 블록이다.

Retrieval Queries는 사용자가 입력할 수 있는 다양한 질문 표현을 문서에 포함하여 검색 매칭을 강화한다.

Retrieval Queries는 FAQ와 비슷하지만 문서 전체의 핵심 검색 진입점을 모아둔다는 점이 다르다.

모든 RAG 문서 마지막에는 `# Retrieval Queries` 블록을 포함해야 한다.

---

### [핵심]

- Retrieval Queries는 문서 마지막 필수 블록
- 사용자 Query Matching 강화
- Semantic Retrieval 강화
- 핵심 용어 반복 허용
- Q와 A를 함께 작성
- 문서 전체 핵심 질문을 포함
- Agent가 검색할 가능성이 높은 표현 포함

---

### [실무]

Retrieval Queries 작성 기준은 다음과 같다.

```text
# Retrieval Queries

### [FAQ]

Q. Chunking이 뭐야?
A. 문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk Size는 어떻게 정해?
A. 300~1200 tokens를 기본으로 하되 Golden Query 검증 결과에 따라 조정한다.

Q. Metadata는 왜 필요해?
A. 출처 추적, 검색 필터링, Agent Routing, 최신성 판단에 필요하다.
```

Retrieval Queries에는 다음 표현을 포함하는 것이 좋다.

- 정식 용어
- 사용자가 쉽게 묻는 표현
- 한글 표현
- 영어 기술 용어
- 오류 상황
- 실무 판단 질문
- Agent 작업 질문

---

### [FAQ]

Q. Retrieval Queries가 뭐야?

A.
문서 마지막에 배치하는 검색 최적화 질문/답변 블록이다.

Q. Retrieval Queries는 필수야?

A.
RAG 문서에서는 필수로 포함하는 것이 원칙이다.

Q. FAQ와 Retrieval Queries는 뭐가 달라?

A.
FAQ는 섹션 단위 질문이고, Retrieval Queries는 문서 전체 검색 진입점이다.

Q. Retrieval Queries에 핵심 키워드를 반복해도 돼?

A.
가능하다. 검색 최적화를 위해 자연스러운 반복은 허용된다.

Q. Retrieval Queries에도 A가 필요해?

A.
필요하다. Q만 있으면 RAG 검색 후 답변 근거로 쓰기 어렵다.

---

# 10. Metadata Core

## 10.1 Metadata Definition

### [개념]

Metadata는 Chunk의 출처, 위치, 역할, 도메인, 레벨, 버전 정보를 설명하는 구조화 데이터다.

Vector Database는 Embedding Vector와 함께 Original Text, Metadata를 저장해야 한다.

Metadata는 RAG에서 다음 기능을 지원한다.

```text
Source Tracking
→ Filtered Search
→ Agent Routing
→ Version Control
→ Review Validation
```

Metadata가 없으면 검색 결과가 어떤 문서에서 왔는지 확인하기 어렵고, Agent가 적절한 도메인 기준을 판단하기 어렵다.

---

### [핵심]

- Metadata는 Chunk 설명 데이터
- Source Tracking에 필요
- Filtered Search에 필요
- Agent Routing에 필요
- Version Control에 필요
- Review Validation에 필요
- Vector만 저장하고 Metadata를 생략하면 안 됨
- Metadata 필드명은 문서 전체에서 통일

---

### [실무]

권장 Metadata 필드는 다음과 같다.

```json
{
  "source": "Vector_Database_RAG_Part03_Chunking_Metadata.md",
  "fileName": "Vector_Database_RAG_Part03_Chunking_Metadata.md",
  "documentId": "vector-database-rag-part03",
  "chunkId": "vector-database-rag-part03-010",
  "domain": "AI",
  "level": "Foundation",
  "category": "Vector Database & RAG",
  "section": "Metadata Core",
  "title": "Metadata Definition",
  "tags": ["rag", "chunking", "metadata", "vector-database"],
  "version": "2026-06",
  "updatedAt": "2026-06-30"
}
```

개인 AI 프로젝트에서는 Metadata를 Agent Routing 기준으로 사용한다.

예를 들어 AI Agent는 `domain: AI` 문서를 우선 검색하고, Review Agent는 `section`, `category`, `version`을 통해 검증 기준을 확인할 수 있다.

---

### [FAQ]

Q. Metadata가 뭐야?

A.
Chunk의 출처, 위치, 역할, 도메인, 레벨, 버전 정보를 설명하는 구조화 데이터다.

Q. Metadata는 왜 필요해?

A.
출처 추적, 검색 필터링, Agent Routing, 버전 관리, 검증에 필요하다.

Q. Vector만 저장하면 안 돼?

A.
안 된다. Original Text와 Metadata가 연결되어야 RAG 답변 근거로 사용할 수 있다.

Q. Metadata 필드명은 꼭 통일해야 해?

A.
통일해야 한다. 필드명이 흔들리면 Filtered Search와 Agent Routing이 불안정해진다.

Q. Metadata는 답변 품질에도 영향을 줘?

A.
그렇다. 올바른 문서를 찾고 출처를 검증하는 데 영향을 준다.

---

# 11. Metadata Field Rules

## 11.1 Required Metadata Fields

### [개념]

Required Metadata Fields는 RAG Chunk에 기본적으로 포함해야 하는 Metadata 항목이다.

Metadata 필드는 문서 검색, 출처 추적, 문서 업데이트, Agent Routing을 위해 표준화되어야 한다.

필드가 누락되면 검색 결과를 검증하거나 오래된 문서를 제거하기 어렵다.

---

### [핵심]

- source는 원본 출처
- fileName은 파일명
- documentId는 문서 고유 ID
- chunkId는 Chunk 고유 ID
- domain은 기술 도메인
- level은 문서 수준
- category는 문서 분류
- section은 섹션명
- title은 Chunk 제목
- tags는 검색 보조 키워드
- version은 문서 버전
- updatedAt은 업데이트 일자

---

### [실무]

필수 권장 Metadata Field는 다음과 같다.

| Field      | 의미       | 예시                                            |
| ---------- | ---------- | ----------------------------------------------- |
| source     | 원본 출처  | Vector_Database_RAG_Part03_Chunking_Metadata.md |
| fileName   | 파일명     | Vector_Database_RAG_Part03_Chunking_Metadata.md |
| documentId | 문서 ID    | vector-database-rag-part03                      |
| chunkId    | Chunk ID   | vector-database-rag-part03-011                  |
| domain     | 도메인     | AI                                              |
| level      | 레벨       | Foundation                                      |
| category   | 분류       | Vector Database & RAG                           |
| section    | 섹션       | Metadata Field Rules                            |
| title      | Chunk 제목 | Required Metadata Fields                        |
| tags       | 검색 태그  | rag, metadata, chunking                         |
| version    | 버전       | 2026-06                                         |
| updatedAt  | 수정일     | 2026-06-30                                      |

Metadata는 문서 제작 단계에서 설계하고, Vector Store Upsert 단계에서 함께 저장한다.

---

### [FAQ]

Q. 필수 Metadata에는 뭐가 있어?

A.
source, fileName, documentId, chunkId, domain, level, category, section, title, tags, version, updatedAt을 권장한다.

Q. documentId는 왜 필요해?

A.
문서 단위 업데이트, 삭제, Reindex를 추적하기 위해 필요하다.

Q. chunkId는 왜 필요해?

A.
Chunk 단위 검색 결과, 수정, 검증을 추적하기 위해 필요하다.

Q. tags는 왜 필요해?

A.
검색 보조 키워드와 Agent Routing 힌트로 사용할 수 있기 때문이다.

Q. updatedAt은 왜 필요해?

A.
문서 최신성 판단과 오래된 문서 제거에 필요하다.

---

## 11.2 Metadata Naming Consistency

### [개념]

Metadata Naming Consistency는 모든 RAG 문서와 Chunk에서 Metadata 필드명을 일관되게 사용하는 규칙이다.

같은 의미를 가진 필드가 여러 이름으로 섞이면 Filtered Search와 Agent Routing이 불안정해진다.

예를 들어 `fileName`, `filename`, `file_name`이 혼용되면 검색 필터가 일부 Chunk에 적용되지 않을 수 있다.

Metadata 필드명은 프로젝트 전체에서 하나로 통일해야 한다.

---

### [핵심]

- Metadata 필드명은 통일 필요
- 같은 의미의 필드명 혼용 금지
- 대소문자 일관성 유지
- camelCase 사용 권장
- domain / level / category 값도 통일
- 태그 표기 방식 통일
- 필드명 변경 시 Reindex 필요

---

### [실무]

권장 필드명은 다음과 같다.

```json
{
  "source": "...",
  "fileName": "...",
  "documentId": "...",
  "chunkId": "...",
  "domain": "...",
  "level": "...",
  "category": "...",
  "section": "...",
  "title": "...",
  "tags": ["..."],
  "version": "...",
  "updatedAt": "..."
}
```

피해야 할 혼용 예시는 다음과 같다.

```json
{
  "filename": "...",
  "file_name": "...",
  "doc_id": "...",
  "chunk_id": "...",
  "updated_at": "..."
}
```

프로젝트 기준을 바꾸는 경우 기존 Vector Metadata와 새 Metadata가 충돌하지 않도록 전체 Reindex를 수행한다.

---

### [FAQ]

Q. Metadata Naming Consistency가 뭐야?

A.
모든 RAG 문서와 Chunk에서 Metadata 필드명을 일관되게 사용하는 규칙이다.

Q. fileName과 filename을 섞어도 돼?

A.
안 된다. Filtered Search에서 일부 Chunk가 누락될 수 있다.

Q. Metadata는 camelCase를 써도 돼?

A.
가능하다. 프로젝트에서 camelCase로 통일하면 된다.

Q. Metadata 필드명을 바꾸면 Reindex해야 해?

A.
해야 한다. 기존 Vector Metadata와 새 Metadata 구조를 맞춰야 한다.

Q. Metadata 값도 통일해야 해?

A.
그렇다. domain, level, category, tags 값도 일관되게 관리해야 한다.

---

# 12. Chunk ID Policy

## 12.1 Chunk ID Design

### [개념]

Chunk ID는 각 Chunk를 고유하게 식별하는 ID다.

Chunk ID는 검색 결과 추적, Reindex, Delete, Update, Citation, Review Validation에 사용된다.

Chunk ID가 없으면 특정 Chunk의 문제를 기록하거나 수정하기 어렵다.

Chunk ID는 documentId와 순번 또는 섹션 정보를 조합해 설계한다.

---

### [핵심]

- Chunk ID는 Chunk 고유 식별자
- 검색 결과 추적에 필요
- Update / Delete / Reindex에 필요
- Citation과 Source Reference에 필요
- Review Agent 검증에 필요
- documentId 기반으로 생성 권장
- 중복 Chunk ID 금지

---

### [실무]

Chunk ID 예시는 다음과 같다.

```text
documentId:
vector-database-rag-part03

chunkId:
vector-database-rag-part03-001
vector-database-rag-part03-002
vector-database-rag-part03-003
```

섹션 기반 Chunk ID 예시는 다음과 같다.

```text
vector-database-rag-part03-chunking-core-001
vector-database-rag-part03-metadata-core-001
vector-database-rag-part03-retrieval-queries-001
```

개인 AI 프로젝트에서는 관리 편의성을 위해 문서 ID + 순번 방식을 기본으로 사용할 수 있다.

Chunk 구조가 자주 변경되는 문서는 기존 Chunk를 삭제하고 새 Chunk ID로 재적재하는 것이 안전하다.

---

### [FAQ]

Q. Chunk ID가 뭐야?

A.
각 Chunk를 고유하게 식별하는 ID다.

Q. Chunk ID는 왜 필요해?

A.
검색 결과 추적, 수정, 삭제, Reindex, Citation, Review Validation에 필요하다.

Q. Chunk ID는 어떻게 만들면 돼?

A.
documentId와 순번 또는 섹션명을 조합해 만들면 된다.

Q. Chunk ID가 중복되면 어떻게 돼?

A.
Upsert 충돌, 잘못된 갱신, 검색 결과 혼란이 발생할 수 있다.

Q. Chunk 구조가 바뀌면 Chunk ID도 바꿔야 해?

A.
의미 단위가 크게 바뀌면 기존 Chunk를 삭제하고 새 ID로 재적재하는 것이 안전하다.

---

# 13. Metadata Filter

## 13.1 Filtered Search

### [개념]

Metadata Filter는 Vector Search 결과를 Metadata 조건으로 제한하는 방식이다.

RAG에서는 모든 문서를 항상 같은 범위에서 검색하지 않는다.

Agent 역할, Domain, Level, Version, Project 상태에 따라 검색 범위를 좁힐 수 있다.

예를 들어 AI Agent는 `domain: AI` 문서를 우선 검색하고, Frontend Agent는 `domain: Frontend` 문서를 우선 검색할 수 있다.

---

### [핵심]

- Metadata Filter는 검색 범위를 제한
- Domain 기반 검색 가능
- Level 기반 검색 가능
- Version 기반 최신 문서 검색 가능
- Agent Routing에 활용 가능
- 검색 Precision 향상 가능
- Filter가 너무 좁으면 필요한 문서가 누락될 수 있음

---

### [실무]

Metadata Filter 예시는 다음과 같다.

```json
{
  "domain": "AI",
  "level": "Foundation",
  "category": "Vector Database & RAG"
}
```

Agent별 Filter 예시는 다음과 같다.

| Agent          | 우선 Filter                              |
| -------------- | ---------------------------------------- |
| PM Agent       | project, progress, domain rules          |
| Backend Agent  | domain: Backend                          |
| Frontend Agent | domain: Frontend                         |
| Review Agent   | domain rules, checklist, troubleshooting |
| DevOps Agent   | domain: DevOps                           |
| AI Agent       | domain: AI                               |

Metadata Filter는 정확도를 높이지만 과하게 제한하면 필요한 문서를 찾지 못할 수 있다.

따라서 Filter 실패 시 fallback 검색 전략이 필요하다.

---

### [FAQ]

Q. Metadata Filter가 뭐야?

A.
Vector Search 결과를 Metadata 조건으로 제한하는 방식이다.

Q. Metadata Filter는 왜 써?

A.
Domain, Level, Version, Agent 역할에 맞게 검색 범위를 줄이기 위해 사용한다.

Q. Filter를 많이 걸면 좋은 거 아니야?

A.
아니다. 너무 좁게 걸면 필요한 문서가 검색되지 않을 수 있다.

Q. Agent Routing에 Metadata Filter를 쓸 수 있어?

A.
쓸 수 있다. Agent 역할별로 우선 검색할 Domain과 Category를 지정할 수 있다.

Q. Filter 실패 시 어떻게 해야 해?

A.
조건을 완화하거나 fallback 검색을 수행해야 한다.

---

# 14. Metadata Failure

## 14.1 Missing Metadata

### [개념]

Missing Metadata는 Chunk에 필요한 Metadata가 누락된 상태다.

Metadata가 없거나 부족하면 검색 결과의 출처, 도메인, 섹션, 버전을 판단하기 어렵다.

RAG 시스템에서는 답변 근거를 검증해야 하므로 Metadata 누락은 신뢰도 문제로 이어진다.

Agent 기반 시스템에서는 Metadata 누락이 Agent Routing 실패로 이어질 수 있다.

---

### [핵심]

- Metadata 누락은 출처 추적 실패 원인
- domain 누락 시 Agent Routing 불안정
- version 누락 시 최신성 판단 어려움
- chunkId 누락 시 Chunk 수정과 검증 어려움
- source 누락 시 Citation 불가능
- Filtered Search 품질 저하
- Metadata 보강 후 Reindex 필요

---

### [실무]

Missing Metadata 문제 해결 형식은 다음과 같다.

```text
문제:
검색 결과의 출처와 도메인을 추적할 수 없음

원인:
source 누락
documentId 누락
chunkId 누락
domain 누락
section 누락
version 누락
updatedAt 누락

해결:
Metadata Schema 정의
필수 필드 보강
필드명 통일
기존 Vector 삭제 또는 갱신
Reindex 수행
Golden Query 재검증
```

Metadata 누락은 단순 문서 포맷 문제가 아니라 운영 문제다.

문서가 많아질수록 Metadata가 없으면 오래된 문서와 최신 문서를 구분하기 어렵다.

---

### [FAQ]

Q. Missing Metadata가 뭐야?

A.
Chunk에 필요한 Metadata가 누락된 상태다.

Q. Metadata가 누락되면 뭐가 문제야?

A.
출처 추적, Agent Routing, Filtered Search, 최신성 판단이 어려워진다.

Q. source가 없으면 어떻게 돼?

A.
검색 결과의 원본 문서를 표시하거나 검증하기 어렵다.

Q. version이 없으면 어떻게 돼?

A.
최신 문서와 오래된 문서를 구분하기 어렵다.

Q. Metadata를 추가하면 Reindex해야 해?

A.
해야 한다. Vector Store의 Metadata도 갱신되어야 한다.

---

## 14.2 Wrong Metadata

### [개념]

Wrong Metadata는 Chunk에 잘못된 Metadata가 붙은 상태다.

Wrong Metadata는 Missing Metadata보다 더 위험할 수 있다.

Metadata가 없으면 누락을 발견할 수 있지만, 잘못된 Metadata는 잘못된 검색 결과를 정상 결과처럼 보이게 만들 수 있다.

예를 들어 AI 문서에 `domain: Backend`가 붙으면 Backend Agent가 잘못된 문서를 기준으로 답변할 수 있다.

---

### [핵심]

- Wrong Metadata는 잘못된 검색 결과 유발
- Agent Routing 오류 가능
- Domain / Level / Category 오분류 주의
- version 오류는 오래된 문서 우선 문제 유발
- source 오류는 Citation 신뢰도 저하
- 잘못된 Metadata는 전체 Reindex 대상 가능
- Metadata 검수 필요

---

### [실무]

Wrong Metadata 문제 해결 형식은 다음과 같다.

```text
문제:
Backend Agent가 AI 문서를 검색함

원인:
domain Metadata 오입력
category Metadata 오입력
tags 과다 또는 부정확
Metadata Filter 기준 불일치

해결:
Metadata Schema 재검수
domain / level / category 값 통일
잘못된 Chunk 검색 결과 기록
Metadata 수정
Reindex 수행
Agent별 Golden Query 재검증
```

Metadata 검수는 문서 제작 완료 후, Vector Store 적재 전, Reindex 후에 반복한다.

---

### [FAQ]

Q. Wrong Metadata가 뭐야?

A.
Chunk에 잘못된 Metadata가 붙은 상태다.

Q. Wrong Metadata가 위험한 이유는 뭐야?

A.
잘못된 문서가 정상 검색 결과처럼 사용될 수 있기 때문이다.

Q. domain Metadata가 틀리면 어떻게 돼?

A.
Agent가 자기 도메인과 맞지 않는 문서를 검색할 수 있다.

Q. source Metadata가 틀리면 어떻게 돼?

A.
Citation과 문서 검증 신뢰도가 떨어진다.

Q. Wrong Metadata는 어떻게 고쳐?

A.
Metadata를 수정하고 기존 Vector를 갱신하거나 Reindex해야 한다.

---

# 15. Chunking and Metadata Checklist

## 15.1 Final Checklist

### [개념]

Chunking and Metadata Checklist는 RAG 문서를 Vector Database에 적재하기 전 Chunk 구조와 Metadata 품질을 검수하는 기준이다.

이 Checklist는 Retrieval Hit, Source Tracking, Agent Routing, Reindex 안정성을 높이기 위해 사용한다.

---

### [핵심]

- Chunk 의미 독립성 확인
- Single Concept Chunk 확인
- Chunk Size 확인
- Chunk Overlap 확인
- Code Block 보존 확인
- FAQ 품질 확인
- Retrieval Queries 포함 확인
- Metadata 필수 필드 확인
- Chunk ID 중복 확인
- Metadata Filter 가능 여부 확인

---

### [실무]

최종 Checklist는 다음과 같다.

```text
### [Checklist]

- [ ] Chunk가 독립 검색되어도 의미가 유지되는가?
- [ ] 하나의 Chunk가 하나의 핵심 개념만 다루는가?
- [ ] Chunk Size가 300~1200 tokens 범위에서 관리되는가?
- [ ] Chunk가 너무 작아 문맥이 부족하지 않은가?
- [ ] Chunk가 너무 커서 여러 주제가 섞이지 않았는가?
- [ ] Chunk Overlap이 과도하지 않은가?
- [ ] Chunk Overlap 부족으로 문맥이 끊기지 않는가?
- [ ] Header가 Chunk Boundary로 적절한가?
- [ ] Header에 핵심 키워드가 포함되어 있는가?
- [ ] Code Block이 중간에 분리되지 않았는가?
- [ ] Code Block 설명이 같은 Chunk에 있는가?
- [ ] 코드블록 id=""가 제거되었는가?
- [ ] FAQ에 Q와 A가 모두 있는가?
- [ ] FAQ 답변이 짧고 명확한가?
- [ ] Retrieval Queries가 문서 마지막에 있는가?
- [ ] source Metadata가 있는가?
- [ ] fileName Metadata가 있는가?
- [ ] documentId Metadata가 있는가?
- [ ] chunkId Metadata가 있는가?
- [ ] domain / level / category가 통일되어 있는가?
- [ ] section / title Metadata가 정확한가?
- [ ] tags가 검색에 도움이 되는가?
- [ ] version / updatedAt Metadata가 있는가?
- [ ] Chunk ID가 중복되지 않는가?
- [ ] Metadata Filter로 Agent Routing이 가능한가?
- [ ] Chunking 또는 Metadata 변경 후 Reindex했는가?
- [ ] Golden Query로 Retrieval 검증을 했는가?
```

Checklist는 Part03 문서뿐 아니라 모든 RAG 문서 제작과 검수에 공통 적용할 수 있다.

---

### [FAQ]

Q. Chunking and Metadata Checklist는 왜 필요해?

A.
검색 품질, 출처 추적, Agent Routing, Reindex 안정성을 높이기 위해 필요하다.

Q. Chunk 검수에서 가장 중요한 건 뭐야?

A.
독립 검색 가능성, 단일 개념, 적절한 크기, Code Block 보존이다.

Q. Metadata 검수에서 가장 중요한 건 뭐야?

A.
source, documentId, chunkId, domain, level, section, version, updatedAt의 정확성이다.

Q. Checklist는 언제 사용해?

A.
문서 제작 완료 후, Vector Store 적재 전, Reindex 후에 사용한다.

Q. Checklist 통과 후에도 검증이 필요해?

A.
필요하다. Golden Query로 실제 Retrieval 결과를 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Chunking이 뭐야?
A. 문서를 RAG 검색 단위인 Chunk로 나누는 과정이다.

Q. Chunk는 왜 중요해?
A. Chunk가 Retrieval의 최소 단위이기 때문에 Chunk 품질이 검색 품질과 답변 품질을 결정한다.

Q. RAG Chunk는 무엇을 기준으로 나눠?
A. Header, 의미 경계, Chunk Size, Code Block 보존, FAQ 구조를 기준으로 나눈다.

Q. 좋은 Chunk는 뭐야?
A. 독립 검색되어도 의미가 유지되고 하나의 핵심 개념만 다루는 Chunk다.

Q. Independent Chunk가 뭐야?
A. 단독으로 검색되어도 의미를 이해할 수 있는 Chunk다.

Q. Single Concept Chunk가 뭐야?
A. 하나의 Chunk가 하나의 핵심 개념만 다루도록 설계된 Chunk다.

Q. Chunk가 여러 개념을 섞으면 왜 안 좋아?
A. Chunk 의미가 흐려져 Similarity Search 정밀도가 낮아질 수 있다.

Q. Chunk Size는 뭐야?
A. 하나의 Chunk에 포함되는 Text 양이다.

Q. Chunk Size 권장 범위는 얼마야?
A. 일반적으로 300~1200 tokens 범위를 권장한다.

Q. Chunk가 너무 작으면 왜 문제야?
A. 답변에 필요한 문맥이 부족할 수 있다.

Q. Chunk가 너무 크면 왜 문제야?
A. 여러 주제가 섞여 검색 정밀도가 떨어질 수 있다.

Q. Chunk Size는 어떻게 최적화해?
A. Golden Query로 검색 결과를 확인하고 기대 Chunk 포함 여부와 Context 충분성을 기준으로 조정한다.

Q. Chunk Size를 바꾸면 Reindex해야 해?
A. 해야 한다. Chunk 내용과 Embedding Vector가 바뀌기 때문이다.

Q. Chunk Overlap이 뭐야?
A. 인접한 Chunk 사이에 일부 내용을 중복 포함하는 방식이다.

Q. Chunk Overlap은 왜 써?
A. Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다.

Q. Overlap이 많으면 좋은 거 아니야?
A. 아니다. 너무 많으면 중복 검색이 늘고 Context Budget을 낭비한다.

Q. Overlap이 부족하면 어떻게 돼?
A. Chunk 경계에서 문맥이 끊겨 답변에 필요한 정보가 부족할 수 있다.

Q. Overlap 문제는 어떻게 확인해?
A. Golden Query 검색 결과에서 중복 Chunk 비율과 문맥 충분성을 확인한다.

Q. Semantic Chunking이 뭐야?
A. 문서의 의미 경계를 기준으로 Chunk를 나누는 방식이다.

Q. Semantic Chunking은 왜 중요해?
A. 사용자 Query가 특정 개념이나 문제를 묻기 때문에 Chunk도 의미 단위로 답할 수 있어야 하기 때문이다.

Q. Header Based Chunking이 뭐야?
A. Markdown Header를 기준으로 Chunk를 나누는 방식이다.

Q. Header가 Retrieval에 왜 중요해?
A. Header는 Chunk 주제를 보여주는 검색 신호이자 Chunk Boundary이기 때문이다.

Q. 좋은 Header는 뭐야?
A. 핵심 키워드가 포함되고 Chunk의 주제를 명확히 설명하는 Header다.

Q. 나쁜 Header는 뭐야?
A. `기타`, `설명`, `내용`처럼 검색 의미가 약한 Header다.

Q. Code Block Chunking이 뭐야?
A. 코드 예제를 Chunk로 나눌 때 코드 문법과 설명의 연결을 보존하는 규칙이다.

Q. Code Block을 중간에 잘라도 돼?
A. 안 된다. 코드 문법이 깨지고 Agent가 불완전한 코드를 사용할 수 있다.

Q. 코드와 설명은 같은 Chunk에 있어야 해?
A. 가능하면 같은 Chunk에 있어야 코드 목적과 사용 조건을 함께 검색할 수 있다.

Q. 코드블록 id=""는 제거해야 해?
A. 해야 한다. 불필요한 속성은 RAG 문서 노이즈가 될 수 있다.

Q. FAQ Chunk가 뭐야?
A. 실제 사용자 질문 표현과 문서 개념을 연결하는 Retrieval 강화 Chunk다.

Q. FAQ가 Retrieval에 왜 좋아?
A. 사용자 Query와 유사한 질문 문장을 문서에 포함하기 때문이다.

Q. FAQ에는 Q만 있어도 돼?
A. 안 된다. 반드시 Q와 A를 함께 작성해야 한다.

Q. Retrieval Queries가 뭐야?
A. 문서 마지막에 배치하는 검색 최적화 질문/답변 블록이다.

Q. Retrieval Queries는 필수야?
A. RAG 문서에서는 필수로 포함하는 것이 원칙이다.

Q. FAQ와 Retrieval Queries 차이는 뭐야?
A. FAQ는 섹션 단위 질문이고, Retrieval Queries는 문서 전체 검색 진입점이다.

Q. Metadata가 뭐야?
A. Chunk의 출처, 위치, 역할, 도메인, 레벨, 버전 정보를 설명하는 구조화 데이터다.

Q. Metadata는 왜 필요해?
A. 출처 추적, 검색 필터링, Agent Routing, 버전 관리, 검증에 필요하다.

Q. 필수 Metadata에는 뭐가 있어?
A. source, fileName, documentId, chunkId, domain, level, category, section, title, tags, version, updatedAt을 권장한다.

Q. documentId는 왜 필요해?
A. 문서 단위 업데이트, 삭제, Reindex를 추적하기 위해 필요하다.

Q. chunkId는 왜 필요해?
A. Chunk 단위 검색 결과, 수정, 검증을 추적하기 위해 필요하다.

Q. Metadata 필드명은 통일해야 해?
A. 통일해야 한다. 필드명이 흔들리면 Filtered Search와 Agent Routing이 불안정해진다.

Q. Metadata Filter가 뭐야?
A. Vector Search 결과를 Metadata 조건으로 제한하는 방식이다.

Q. Metadata Filter는 왜 써?
A. Domain, Level, Version, Agent 역할에 맞게 검색 범위를 줄이기 위해 사용한다.

Q. Agent Routing에 Metadata Filter를 쓸 수 있어?
A. 쓸 수 있다. Agent 역할별로 우선 검색할 Domain과 Category를 지정할 수 있다.

Q. Missing Metadata가 뭐야?
A. Chunk에 필요한 Metadata가 누락된 상태다.

Q. Metadata가 누락되면 뭐가 문제야?
A. 출처 추적, Agent Routing, Filtered Search, 최신성 판단이 어려워진다.

Q. Wrong Metadata가 뭐야?
A. Chunk에 잘못된 Metadata가 붙은 상태다.

Q. Wrong Metadata가 위험한 이유는 뭐야?
A. 잘못된 문서가 정상 검색 결과처럼 사용될 수 있기 때문이다.

Q. Chunk ID가 뭐야?
A. 각 Chunk를 고유하게 식별하는 ID다.

Q. Chunk ID는 어떻게 만들면 돼?
A. documentId와 순번 또는 섹션명을 조합해 만들면 된다.

Q. Chunk ID가 중복되면 어떻게 돼?
A. Upsert 충돌, 잘못된 갱신, 검색 결과 혼란이 발생할 수 있다.

Q. Chunking and Metadata Checklist는 왜 필요해?
A. 검색 품질, 출처 추적, Agent Routing, Reindex 안정성을 높이기 위해 필요하다.

Q. Chunking 또는 Metadata 변경 후 무엇을 해야 해?
A. Reindex를 수행하고 Golden Query로 Retrieval 결과를 검증해야 한다.

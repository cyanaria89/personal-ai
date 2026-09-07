# Vector Database & RAG Part04 Retrieval and Search

---

# 1. Retrieval Core

## 1.1 Retrieval Definition

### [개념]

Retrieval은 사용자 Query와 관련 있는 문서 Chunk를 검색하는 과정이다.

RAG에서 Retrieval은 Generation 이전에 수행된다.

LLM은 Retrieval 단계에서 검색된 Retrieved Context를 근거로 답변을 생성한다.

기본 흐름은 다음과 같다.

```text
User Query
→ Query Embedding
→ Vector Search
→ Metadata Filter
→ Top-K Selection
→ Retrieved Context
```

Retrieval 품질은 RAG 답변 품질을 결정하는 핵심 요소다.

관련 Chunk가 검색되지 않으면 문서에 내용이 있어도 LLM은 해당 내용을 근거로 답변할 수 없다.

---

### [핵심]

- Retrieval은 관련 Chunk를 찾는 단계
- RAG 답변 품질은 Retrieval 품질에 크게 의존
- User Query는 Query Embedding으로 변환됨
- Vector Search는 Query Vector와 Chunk Vector의 유사도를 비교
- Metadata Filter는 검색 범위를 제한
- Top-K는 가져올 검색 결과 개수
- Threshold는 최소 관련도 기준
- Retrieval 실패와 Generation 실패는 분리해서 분석해야 함

---

### [실무]

2026 실무 기준 RAG Retrieval은 단순 유사도 검색만으로 판단하지 않는다.

검색 결과는 다음 기준으로 검증한다.

- 기대 Chunk가 Top-K 안에 포함되는가
- 검색된 Chunk가 질문에 직접 답할 수 있는가
- Chunk 제목과 본문이 Query와 의미적으로 연결되는가
- Metadata Filter가 너무 좁거나 넓지 않은가
- 오래된 문서가 최신 문서보다 우선 검색되지 않는가
- 중복 Chunk가 Context Budget을 낭비하지 않는가
- 검색 결과가 Agent 역할과 맞는 Domain 문서인가

개인 AI Agent 구조에서는 Retrieval 단계가 Agent 판단의 시작점이다.

Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI Agent는 각자의 Domain에 맞는 문서를 검색해야 한다.

---

### [FAQ]

Q. Retrieval이 뭐야?

A.
사용자 Query와 관련 있는 문서 Chunk를 검색하는 과정이다.

Q. Retrieval이 RAG에서 중요한 이유는 뭐야?

A.
검색된 Chunk가 LLM 답변의 근거가 되기 때문이다.

Q. 문서에 있는데 답변이 안 나오면 Retrieval 문제야?

A.
가능성이 높다. 기대 Chunk가 Top-K에 검색되는지 먼저 확인해야 한다.

Q. Retrieval 실패와 Generation 실패는 달라?

A.
다르다. Retrieval 실패는 관련 문서를 못 찾는 문제이고, Generation 실패는 검색된 문서를 잘못 사용하는 문제다.

Q. Retrieval 품질은 어떻게 확인해?

A.
Golden Query로 기대 Chunk가 검색되는지 확인한다.

---

# 2. Query Processing

## 2.1 User Query

### [개념]

User Query는 사용자가 RAG 시스템에 입력하는 질문 또는 요청이다.

RAG에서 Query는 단순 문자열이 아니라 Retrieval의 출발점이다.

Query 표현이 문서 표현과 너무 다르면 관련 문서가 존재해도 검색 품질이 낮아질 수 있다.

예를 들어 사용자는 `문서에 있는데 왜 못 찾아?`라고 묻지만 문서에는 `Retrieval Failure`라고 작성되어 있을 수 있다.

이 간극을 줄이기 위해 FAQ, Retrieval Queries, Query Rewrite, 한글/영어 용어 병기를 사용한다.

---

### [핵심]

- User Query는 Retrieval의 시작점
- Query 표현과 문서 표현이 다르면 검색 실패 가능
- FAQ는 Query 표현을 문서에 포함하는 역할
- Retrieval Queries는 문서 전체 검색 진입점
- Query Rewrite는 검색 의도를 명확히 바꾸는 과정
- 한글과 영어 기술 용어 병기는 검색 매칭에 도움
- 모호한 Query는 Agent가 Domain과 의도를 판단해야 함

---

### [실무]

실무 RAG에서는 사용자가 정식 용어로 질문한다고 가정하지 않는다.

다음과 같은 표현 차이를 문서에 반영해야 한다.

| 사용자 표현               | 문서 용어                              |
| ------------------------- | -------------------------------------- |
| 문서에 있는데 왜 못 찾아? | Retrieval Failure                      |
| 검색 결과가 이상해        | Retrieval Quality Issue                |
| 관련 없는 문서가 나와     | Irrelevant Context                     |
| 문서 다시 넣어야 해?      | Reindex                                |
| 검색 개수 몇 개로 해?     | Top-K                                  |
| 유사도 기준 뭐야?         | Similarity Threshold                   |
| 답변이 문서랑 달라        | Generation Failure / Grounding Failure |

RAG 문서는 사용자가 입력할 가능성이 높은 표현을 FAQ와 Retrieval Queries에 포함해야 한다.

---

### [FAQ]

Q. User Query가 뭐야?

A.
사용자가 RAG 시스템에 입력하는 질문 또는 요청이다.

Q. Query 표현이 왜 중요해?

A.
Query 표현과 문서 표현이 너무 다르면 관련 문서가 검색되지 않을 수 있기 때문이다.

Q. 사용자가 정식 용어를 몰라도 검색되게 하려면 어떻게 해?

A.
FAQ와 Retrieval Queries에 실제 사용자 표현을 포함해야 한다.

Q. 한글과 영어 용어를 같이 쓰면 좋아?

A.
기술 문서에서는 좋다. Semantic Search와 Keyword Search 모두에 도움이 된다.

Q. Query가 모호하면 어떻게 해?

A.
Agent가 Domain, 의도, 필요한 문서 범위를 판단하고 Query Rewrite 또는 Filter 완화를 적용해야 한다.

---

## 2.2 Query Embedding

### [개념]

Query Embedding은 User Query를 Embedding Model로 Vector화한 결과다.

Vector Search는 Query Embedding과 Document Chunk Embedding의 유사도를 비교한다.

Query와 Document Chunk는 같은 Embedding Model로 Embedding되어야 한다.

다른 Embedding Model을 사용하면 Vector 공간이 달라져 Similarity Search 품질이 깨질 수 있다.

---

### [핵심]

- Query Embedding은 사용자 질문의 Vector 표현
- Query와 Document Chunk는 같은 Embedding Model 사용
- Vector Dimension 일치 필요
- Query Embedding 품질은 검색 품질에 영향
- 짧고 모호한 Query는 검색 품질이 낮을 수 있음
- Query Rewrite로 검색 의도를 보강할 수 있음
- Embedding Model 변경 시 전체 Reindex 필요

---

### [실무]

Query Embedding 처리 흐름은 다음과 같다.

```text
User Query
→ Query Normalize
→ Optional Query Rewrite
→ Embedding Model
→ Query Vector
→ Vector Search
```

Query Normalize 대상은 다음과 같다.

- 불필요한 공백 제거
- 오타 보정
- 약어 확장
- 한글/영어 용어 보강
- Agent Domain 힌트 추가
- 검색 의도 명확화

예를 들어 다음 Query는 Rewrite할 수 있다.

```text
원본 Query:
문서에 있는데 왜 못 찾아?

Rewrite Query:
Retrieval Failure, 문서에 있는 Chunk가 검색되지 않는 문제, Header, FAQ, Metadata, Reindex 확인
```

---

### [FAQ]

Q. Query Embedding이 뭐야?

A.
사용자 질문을 Embedding Model로 Vector화한 결과다.

Q. Query와 문서는 같은 Embedding Model을 써야 해?

A.
그렇다. 같은 Vector 공간에서 비교해야 Similarity Search가 가능하다.

Q. Query가 짧으면 검색 품질이 떨어질 수 있어?

A.
그럴 수 있다. 짧고 모호한 Query는 의미 정보가 부족할 수 있다.

Q. Query Rewrite는 왜 필요해?

A.
사용자 표현을 검색에 유리한 핵심 용어와 의도로 바꾸기 위해 필요하다.

Q. Embedding Model을 바꾸면 어떻게 해야 해?

A.
기존 문서를 다시 Embedding하고 Vector Database를 Reindex해야 한다.

---

# 3. Vector Search

## 3.1 Similarity Search

### [개념]

Similarity Search는 Query Vector와 저장된 Chunk Vector의 유사도를 비교해 관련 Chunk를 찾는 검색 방식이다.

Vector Database는 Embedding Vector 간 거리를 계산하여 의미적으로 가까운 문서를 검색한다.

일반적인 Keyword Search가 정확한 단어 매칭에 강하다면, Similarity Search는 의미가 비슷한 표현을 찾는 데 강하다.

예를 들어 `문서 다시 넣어야 해?`라는 Query는 `Reindex` 관련 Chunk와 의미적으로 연결될 수 있다.

---

### [핵심]

- Similarity Search는 Vector 유사도 기반 검색
- 의미가 비슷한 Chunk를 찾는 데 강함
- Query Vector와 Chunk Vector를 비교
- Embedding Model 품질에 영향 받음
- Chunk 품질에 크게 영향 받음
- 정확한 키워드 검색은 약할 수 있음
- 기술 문서에서는 Keyword Search와 병행 가능

---

### [실무]

Similarity Search는 다음 상황에 적합하다.

- 개념 질문
- 유사 표현 검색
- 사용자가 정식 용어를 모르는 경우
- 자연어 기반 문서 검색
- 설명형 RAG 답변
- Agent가 관련 기준을 찾아야 하는 경우

하지만 다음 상황에서는 Similarity Search만으로 부족할 수 있다.

- 클래스명 검색
- 메서드명 검색
- API Endpoint 검색
- 에러 메시지 검색
- 정확한 설정값 검색
- 버전명 검색

기술 RAG 문서에서는 Similarity Search와 Keyword Search를 함께 고려해야 한다.

---

### [FAQ]

Q. Similarity Search가 뭐야?

A.
Query Vector와 Chunk Vector의 유사도를 비교해 의미적으로 가까운 문서를 찾는 검색 방식이다.

Q. Vector Search와 Similarity Search는 같은 말이야?

A.
대부분 RAG 문맥에서는 유사한 의미로 사용된다.

Q. Similarity Search는 어떤 질문에 좋아?

A.
개념 질문, 자연어 질문, 정식 용어를 모르는 질문에 좋다.

Q. Similarity Search가 약한 경우는 뭐야?

A.
클래스명, 메서드명, API 경로, 에러 메시지처럼 정확한 문자열 검색이 필요한 경우다.

Q. 기술 문서에서 Similarity Search만 쓰면 돼?

A.
항상 그렇지 않다. Keyword Search 또는 Hybrid Search가 필요할 수 있다.

---

## 3.2 Vector Search Failure

### [개념]

Vector Search Failure는 관련 문서가 Vector Database에 있지만 Similarity Search 결과에 나타나지 않는 문제다.

이 문제는 Embedding Model 문제일 수도 있지만, 대부분 Chunk 구조, Header, 키워드, Metadata, Top-K, Threshold 문제와 함께 발생한다.

Vector Search Failure는 RAG에서 자주 발생하는 Retrieval Failure 유형이다.

---

### [핵심]

- 관련 문서가 있어도 Vector Search에서 누락될 수 있음
- Chunk 제목이 약하면 검색 Signal 부족
- Query와 문서 표현 차이가 크면 검색 실패 가능
- Embedding Model이 도메인 표현을 잘 처리하지 못할 수 있음
- Top-K가 낮으면 기대 Chunk가 누락될 수 있음
- Threshold가 높으면 관련 Chunk가 제외될 수 있음
- Metadata Filter가 잘못되면 검색 범위에서 제외될 수 있음

---

### [실무]

Vector Search Failure 해결 형식은 다음과 같다.

```text
문제:
문서에 있는 내용이 Vector Search 결과에 나오지 않음

원인:
Query 표현과 문서 표현 불일치
Header 키워드 부족
FAQ 부족
Retrieval Queries 부족
Chunk Size 부적절
Metadata Filter 오류
Top-K 부족
Threshold 과도
Embedding 재생성 누락

해결:
FAQ와 Retrieval Queries 보강
한글/영어 핵심 용어 병기
Header 키워드 보강
Chunk 재분리
Metadata Filter 확인
Top-K 증가 테스트
Threshold 완화 테스트
Reindex 수행
Golden Query 재검증
```

Vector Search Failure를 모델 문제로만 판단하지 않는다.

문서 구조와 검색 설정을 먼저 확인해야 한다.

---

### [FAQ]

Q. Vector Search Failure가 뭐야?

A.
관련 문서가 Vector Database에 있지만 Similarity Search 결과에 나오지 않는 문제다.

Q. Vector Search가 실패하면 Embedding Model 문제야?

A.
항상 그렇지 않다. Chunk, Header, FAQ, Metadata, Top-K, Threshold 문제일 수 있다.

Q. 문서 표현과 Query 표현이 다르면 어떻게 해?

A.
FAQ와 Retrieval Queries에 사용자 표현과 정식 용어를 함께 포함해야 한다.

Q. Top-K를 늘리면 해결돼?

A.
일부 해결될 수 있지만 무관 문서도 함께 늘어날 수 있어 검증이 필요하다.

Q. Vector Search 실패 후 무엇을 해야 해?

A.
Golden Query로 검색 결과를 확인하고 문서 구조와 검색 설정을 조정해야 한다.

---

# 4. Keyword Search

## 4.1 Keyword Search Definition

### [개념]

Keyword Search는 Query에 포함된 정확한 단어, 문구, 문자열을 기준으로 문서를 검색하는 방식이다.

Keyword Search는 BM25 같은 Sparse Retrieval 방식으로 구현될 수 있다.

Vector Search가 의미 유사도에 강하다면, Keyword Search는 정확한 용어 매칭에 강하다.

기술 문서에서는 클래스명, 메서드명, API Endpoint, 에러 메시지, 설정값 검색에 Keyword Search가 매우 중요하다.

---

### [핵심]

- Keyword Search는 정확한 문자열 검색에 강함
- BM25는 대표적인 Keyword Search 방식
- 클래스명 검색에 적합
- 메서드명 검색에 적합
- API Endpoint 검색에 적합
- 에러 메시지 검색에 적합
- Vector Search와 상호 보완 관계

---

### [실무]

Keyword Search가 필요한 Query 예시는 다음과 같다.

| Query 유형   | 예시                          |
| ------------ | ----------------------------- |
| 클래스명     | SecurityConfig                |
| 메서드명     | findByUserId                  |
| API Endpoint | GET /api/users/{id}           |
| 에러 메시지  | EntityNotFoundException       |
| 설정값       | spring.jpa.hibernate.ddl-auto |
| 파일명       | application.properties        |
| 토큰명       | Access Token                  |

RAG 문서에서는 정확한 키워드를 Header, 본문, FAQ, Retrieval Queries에 포함해야 한다.

예를 들어 API 문서라면 다음 키워드가 직접 포함되어야 한다.

```text
GET /api/posts
POST /api/posts
PostReqDto
PostResDto
PostController
PostService
PostRepository
```

---

### [FAQ]

Q. Keyword Search가 뭐야?

A.
정확한 단어, 문구, 문자열을 기준으로 문서를 검색하는 방식이다.

Q. Keyword Search는 언제 필요해?

A.
클래스명, 메서드명, API Endpoint, 에러 메시지, 설정값 검색에 필요하다.

Q. BM25가 뭐야?

A.
문서 내 키워드 빈도와 중요도를 기반으로 검색 점수를 계산하는 대표적인 Keyword Search 방식이다.

Q. Vector Search가 있는데 Keyword Search도 필요해?

A.
기술 문서에서는 필요할 수 있다. 정확한 문자열 검색은 Vector Search보다 Keyword Search가 강할 수 있다.

Q. RAG 문서에서 Keyword Search를 강화하려면 어떻게 해?

A.
핵심 클래스명, 메서드명, API 경로, 설정값을 Header, 본문, FAQ, Retrieval Queries에 명시해야 한다.

---

# 5. Hybrid Search

## 5.1 Hybrid Search Definition

### [개념]

Hybrid Search는 Vector Search와 Keyword Search를 함께 사용하는 검색 방식이다.

Vector Search는 의미 기반 검색에 강하고, Keyword Search는 정확한 용어 검색에 강하다.

Hybrid Search는 두 검색 결과를 결합하여 기술 문서 Retrieval 품질을 높인다.

기본 흐름은 다음과 같다.

```text
User Query
→ Vector Search
→ Keyword Search
→ Score Fusion
→ Deduplication
→ Final Retrieved Chunks
```

---

### [핵심]

- Hybrid Search는 Vector Search + Keyword Search
- Semantic Search와 Exact Term Matching을 결합
- 기술 문서 검색에 유리
- 에러 메시지 검색에 유리
- 클래스명 / 메서드명 검색에 유리
- API Endpoint 검색에 유리
- Score Fusion과 Deduplication 기준 필요
- 시스템 복잡도와 Latency 증가 가능

---

### [실무]

Hybrid Search는 다음 Query에 특히 적합하다.

```text
SecurityConfig에서 CORS 설정 어디 있어?
findByUsers_UserIdOrderByCreatedAtDesc 설명해줘
GET /calendar/monthly 응답 구조 알려줘
EntityNotFoundException 발생 원인 뭐야?
Chunking이 왜 검색 품질에 중요해?
```

위 Query들은 자연어 의미와 정확한 키워드가 섞여 있다.

Hybrid Search를 사용하면 다음 두 경로를 모두 활용할 수 있다.

- Vector Search: 질문 의미와 관련 개념 검색
- Keyword Search: 정확한 클래스명, 메서드명, Endpoint 검색

개인 AI 개발팀 RAG에서는 Backend, Frontend, DevOps 문서 검색 시 Hybrid Search가 유용하다.

---

### [FAQ]

Q. Hybrid Search가 뭐야?

A.
Vector Search와 Keyword Search를 함께 사용하는 검색 방식이다.

Q. Hybrid Search는 왜 필요해?

A.
의미 검색과 정확한 키워드 검색을 함께 활용해 검색 품질을 높이기 위해 필요하다.

Q. Hybrid Search는 어떤 문서에 좋아?

A.
코드, API, 에러 메시지, 설정값, 기술 용어가 많은 문서에 좋다.

Q. Hybrid Search의 단점은 뭐야?

A.
구현 복잡도와 Latency가 증가할 수 있다.

Q. 개인 AI Agent에도 Hybrid Search가 필요해?

A.
Backend, Frontend, DevOps, AI 기술 문서를 검색할 때 유용하다.

---

## 5.2 Score Fusion

### [개념]

Score Fusion은 Vector Search 결과와 Keyword Search 결과의 점수를 결합해 최종 순위를 만드는 과정이다.

Hybrid Search에서는 두 검색 방식의 점수 체계가 다를 수 있다.

Vector Search는 유사도 점수를 사용하고, Keyword Search는 키워드 기반 점수를 사용한다.

따라서 두 결과를 정규화하고 결합하는 기준이 필요하다.

---

### [핵심]

- Score Fusion은 검색 점수 결합 과정
- Vector Score와 Keyword Score를 함께 고려
- 점수 정규화 필요
- 가중치 설정 가능
- Query 유형에 따라 가중치 조정 가능
- 중복 결과 제거 필요
- 최종 Top-K 선정 기준 필요

---

### [실무]

Score Fusion 예시는 다음과 같다.

```text
Final Score = Vector Score × 0.6 + Keyword Score × 0.4
```

Query 유형에 따라 가중치를 다르게 줄 수 있다.

| Query 유형        | Vector Weight | Keyword Weight |
| ----------------- | ------------: | -------------: |
| 개념 질문         |          높음 |           낮음 |
| 에러 메시지       |          중간 |           높음 |
| 클래스명 검색     |          낮음 |           높음 |
| API Endpoint 검색 |          낮음 |           높음 |
| 실무 판단 질문    |          높음 |           중간 |

Score Fusion 이후에는 Deduplication을 수행해야 한다.

같은 Chunk가 Vector Search와 Keyword Search에서 동시에 검색될 수 있기 때문이다.

---

### [FAQ]

Q. Score Fusion이 뭐야?

A.
Vector Search와 Keyword Search 결과의 점수를 결합해 최종 순위를 만드는 과정이다.

Q. Score Fusion이 필요한 이유는 뭐야?

A.
Hybrid Search에서 두 검색 방식의 결과를 하나의 Ranking으로 합치기 위해 필요하다.

Q. Query 유형에 따라 가중치를 바꿔도 돼?

A.
가능하다. 개념 질문은 Vector 비중을 높이고, 정확한 문자열 검색은 Keyword 비중을 높일 수 있다.

Q. Score Fusion 후 중복 제거가 필요해?

A.
필요하다. 같은 Chunk가 두 검색 방식에서 동시에 나올 수 있기 때문이다.

Q. Score Fusion은 항상 정답이야?

A.
아니다. Golden Query 평가를 통해 가중치와 Ranking 기준을 조정해야 한다.

---

# 6. Top-K Retrieval

## 6.1 Top-K Definition

### [개념]

Top-K는 Retrieval 단계에서 가져올 상위 검색 결과 개수다.

예를 들어 Top-K가 5이면 검색 점수가 높은 Chunk 5개를 Retrieved Context 후보로 가져온다.

Top-K는 Recall과 Precision에 영향을 준다.

Top-K가 너무 낮으면 필요한 문서가 누락될 수 있고, Top-K가 너무 높으면 관련 없는 문서가 포함될 수 있다.

---

### [핵심]

- Top-K는 검색 결과 개수
- Top-K가 낮으면 Precision 증가 가능
- Top-K가 낮으면 필요한 Chunk 누락 가능
- Top-K가 높으면 Recall 증가 가능
- Top-K가 높으면 무관 Chunk 포함 가능
- Context Budget과 함께 고려 필요
- Top-K는 Golden Query 평가 기반으로 조정

---

### [실무]

Top-K 설정 비교는 다음과 같다.

| 설정          | 장점                      | 단점                         |
| ------------- | ------------------------- | ---------------------------- |
| Top-K 낮음    | 정밀도 증가, Context 간결 | 필요한 문서 누락 가능        |
| Top-K 높음    | 재현율 증가, 후보 확보    | 무관 문서 포함, Context 과다 |
| Dynamic Top-K | Query별 조정 가능         | 구현 복잡도 증가             |

개인 AI RAG 초기 설정에서는 다음 방식이 적합하다.

```text
Initial Top-K:
5~10

Evaluation:
Golden Query로 기대 Chunk 포함 여부 확인

Adjustment:
기대 Chunk 누락 → Top-K 증가 또는 문서 구조 보강
무관 Chunk 과다 → Top-K 감소 또는 Threshold 적용
```

Top-K를 무조건 크게 설정하는 것은 좋은 방법이 아니다.

검색 결과가 많아질수록 Context Assembly와 Grounding 품질이 더 중요해진다.

---

### [FAQ]

Q. Top-K가 뭐야?

A.
Retrieval 단계에서 가져올 상위 검색 결과 개수다.

Q. Top-K를 높이면 좋은 거 아니야?

A.
항상 좋지 않다. 관련 없는 Chunk가 포함되어 답변 품질이 떨어질 수 있다.

Q. Top-K가 낮으면 뭐가 문제야?

A.
필요한 Chunk가 검색 결과에서 누락될 수 있다.

Q. Top-K는 어떻게 정해?

A.
Golden Query로 기대 Chunk가 포함되는지 평가하면서 조정한다.

Q. 개인 AI RAG에서는 Top-K를 몇으로 시작하면 돼?

A.
초기에는 5~10 범위에서 시작하고 평가 결과에 따라 조정하는 것이 적절하다.

---

# 7. Similarity Threshold

## 7.1 Threshold Definition

### [개념]

Similarity Threshold는 Retrieval 결과로 사용할 최소 유사도 기준이다.

Threshold보다 낮은 검색 결과는 Retrieved Context에서 제외할 수 있다.

Threshold는 무관한 Chunk가 Context에 들어가는 것을 줄이는 데 도움이 된다.

하지만 Threshold가 너무 높으면 필요한 Chunk도 제외될 수 있다.

---

### [핵심]

- Threshold는 최소 관련도 기준
- 낮은 관련도 Chunk 제거에 사용
- Threshold가 높으면 Precision 증가 가능
- Threshold가 높으면 검색 실패 증가 가능
- Threshold가 낮으면 Recall 증가 가능
- Threshold가 낮으면 노이즈 증가 가능
- Top-K와 함께 조정해야 함

---

### [실무]

Top-K와 Threshold 비교는 다음과 같다.

| 설정              | 장점              | 단점                   |
| ----------------- | ----------------- | ---------------------- |
| Threshold 높음    | 무관 문서 제거    | 관련 문서도 제외 가능  |
| Threshold 낮음    | 검색 결과 확보    | 노이즈 증가            |
| Threshold 없음    | 후보 확보 쉬움    | Context 품질 저하 가능 |
| Dynamic Threshold | Query별 조정 가능 | 평가 기준 필요         |

Threshold 설정은 Embedding Model, 문서 구조, Query 유형에 따라 달라진다.

낮은 Score라도 중요한 문서일 수 있으므로 Score만 보고 무조건 제외하지 않는다.

초기 RAG 시스템에서는 Threshold를 너무 높게 잡기보다 검색 결과를 관찰하면서 조정한다.

---

### [FAQ]

Q. Similarity Threshold가 뭐야?

A.
Retrieval 결과로 사용할 최소 유사도 기준이다.

Q. Threshold를 높이면 좋은 거 아니야?

A.
항상 좋지 않다. 필요한 Chunk가 제외되어 검색 실패가 늘 수 있다.

Q. Threshold가 낮으면 뭐가 문제야?

A.
관련 없는 Chunk가 Retrieved Context에 포함될 수 있다.

Q. Threshold는 Top-K와 같이 봐야 해?

A.
그렇다. Top-K와 Threshold는 함께 Retrieval 범위를 조정하는 기준이다.

Q. 낮은 Score 문서는 항상 버려야 해?

A.
아니다. 낮은 Score라도 중요한 문서일 수 있어 Golden Query 평가가 필요하다.

---

# 8. Metadata Filter

## 8.1 Metadata Filter in Retrieval

### [개념]

Metadata Filter는 검색 결과를 Metadata 조건으로 제한하는 방식이다.

Vector Search는 의미적으로 가까운 Chunk를 찾지만, 모든 Domain의 문서를 함께 검색하면 무관한 문서가 섞일 수 있다.

Metadata Filter를 사용하면 Domain, Level, Category, Section, Version 기준으로 검색 범위를 줄일 수 있다.

Agent 기반 RAG에서는 Metadata Filter가 Agent Routing과 연결된다.

---

### [핵심]

- Metadata Filter는 검색 범위 제한
- Domain 기반 검색 가능
- Level 기반 검색 가능
- Category 기반 검색 가능
- Version 기반 최신 문서 검색 가능
- Agent Routing에 활용 가능
- 검색 Precision 향상 가능
- Filter가 과하면 필요한 문서 누락 가능

---

### [실무]

Agent별 Metadata Filter 예시는 다음과 같다.

| Agent          | 우선 검색 Metadata                       |
| -------------- | ---------------------------------------- |
| PM Agent       | project, progress, rules                 |
| Backend Agent  | domain: Backend                          |
| Frontend Agent | domain: Frontend                         |
| Review Agent   | checklist, troubleshooting, domain rules |
| DevOps Agent   | domain: DevOps                           |
| AI Agent       | domain: AI                               |

Metadata Filter 예시는 다음과 같다.

```json
{
  "domain": "AI",
  "level": "Foundation",
  "category": "Vector Database & RAG"
}
```

Filter가 너무 좁으면 필요한 문서가 누락될 수 있다.

따라서 다음 Fallback 전략이 필요하다.

```text
Strict Metadata Filter
→ Relax Category
→ Relax Level
→ Domain Only Search
→ Global Search
```

---

### [FAQ]

Q. Metadata Filter가 뭐야?

A.
검색 결과를 Metadata 조건으로 제한하는 방식이다.

Q. Metadata Filter는 왜 써?

A.
Domain, Level, Category, Version 기준으로 검색 범위를 줄이기 위해 사용한다.

Q. Agent Routing에 Metadata Filter를 쓸 수 있어?

A.
쓸 수 있다. Agent 역할에 맞는 Domain 문서를 우선 검색하게 만들 수 있다.

Q. Filter를 강하게 걸면 좋은 거 아니야?

A.
아니다. 너무 강하면 필요한 문서가 검색되지 않을 수 있다.

Q. Filter 실패 시 어떻게 해야 해?

A.
Category, Level, Domain 조건을 단계적으로 완화하는 Fallback 검색을 수행해야 한다.

---

# 9. Reranking

## 9.1 Reranking Definition

### [개념]

Reranking은 1차 Retrieval 결과를 다시 평가하여 최종 순서를 재정렬하는 단계다.

Vector Search는 빠르게 후보 Chunk를 찾지만, 검색 결과 순서가 항상 최적은 아닐 수 있다.

Reranker는 후보 Chunk와 Query의 관련성을 더 정밀하게 판단하여 최종 Ranking을 개선한다.

기본 흐름은 다음과 같다.

```text
Vector Search Top-20
→ Reranker
→ Final Top-5
→ Context Assembly
```

---

### [핵심]

- Reranking은 검색 결과 재정렬 단계
- 1차 검색 후보를 더 정밀하게 평가
- Cross Encoder 기반 Reranker 사용 가능
- Final Top-K 품질 개선 가능
- 무관 Chunk 제거에 도움
- Latency와 비용 증가 가능
- Chunk 품질 문제를 완전히 해결하지는 못함

---

### [실무]

Reranking은 다음 상황에서 유용하다.

- Top-K 결과는 나오지만 순서가 부정확한 경우
- 무관 Chunk가 상위에 섞이는 경우
- 질문이 복합적이라 단순 유사도만으로 부족한 경우
- 중요한 답변 품질이 필요한 경우
- Review Agent가 정확한 근거를 찾아야 하는 경우

Reranking 적용 예시는 다음과 같다.

```text
Initial Retrieval:
Top-20 후보 검색

Reranking:
Query와 Candidate Chunk 관련도 재평가

Final Selection:
상위 5개 Chunk만 Context Assembly로 전달
```

실시간 응답에서는 Latency를 고려해야 한다.

개인 AI 서버에서는 성능 여유가 부족할 경우 Reranking을 선택적으로 적용할 수 있다.

---

### [FAQ]

Q. Reranking이 뭐야?

A.
1차 Retrieval 결과를 다시 평가하여 최종 순서를 재정렬하는 단계다.

Q. Reranking은 왜 필요해?

A.
Vector Search 결과의 순서가 부정확하거나 무관 Chunk가 섞일 수 있기 때문이다.

Q. Reranking은 언제 쓰면 좋아?

A.
검색 후보는 나오지만 최종 관련도 순서가 불안정할 때 좋다.

Q. Reranking의 단점은 뭐야?

A.
Latency와 비용이 증가할 수 있다.

Q. Reranking이 Chunk 품질 문제를 해결해줘?

A.
완전히 해결하지는 못한다. Chunk 구조가 나쁘면 Reranking 효과도 제한된다.

---

# 10. Deduplication

## 10.1 Duplicate Retrieval

### [개념]

Deduplication은 검색 결과에서 중복되거나 거의 동일한 Chunk를 제거하는 과정이다.

Chunk Overlap이 크거나 FAQ가 반복되거나 같은 문서가 여러 번 적재되면 비슷한 Chunk가 여러 개 검색될 수 있다.

중복 Chunk가 많으면 Context Budget을 낭비하고, 중요한 다른 Chunk가 제외될 수 있다.

Deduplication은 Context Assembly 이전에 수행하는 것이 좋다.

---

### [핵심]

- Deduplication은 중복 검색 결과 제거
- Chunk Overlap 과다 시 중복 증가
- 중복 문서 적재 시 검색 결과 오염
- 같은 Chunk ID 중복 금지
- 유사 Chunk 반복은 Context Budget 낭비
- Context Assembly 전 중복 제거 권장
- Deduplication 후 최종 Context 품질 확인 필요

---

### [실무]

Deduplication 기준은 다음과 같다.

| 기준                 | 설명                    |
| -------------------- | ----------------------- |
| chunkId              | 같은 Chunk ID 중복 제거 |
| documentId + section | 같은 섹션 반복 제거     |
| Text Similarity      | 거의 동일한 본문 제거   |
| Metadata Version     | 오래된 버전 제거        |
| Source Priority      | 우선순위 높은 문서 유지 |

Deduplication 흐름은 다음과 같다.

```text
Retrieved Chunks
→ Check chunkId Duplicate
→ Check Text Similarity
→ Check Version Priority
→ Remove Duplicates
→ Final Candidate Context
```

중복 검색이 반복되면 Retrieval 설정만 보지 말고 Ingestion과 Chunking을 함께 점검해야 한다.

---

### [FAQ]

Q. Deduplication이 뭐야?

A.
검색 결과에서 중복되거나 거의 동일한 Chunk를 제거하는 과정이다.

Q. 중복 Chunk가 왜 문제야?

A.
Context Budget을 낭비하고 중요한 다른 Chunk가 제외될 수 있기 때문이다.

Q. 중복 검색은 왜 발생해?

A.
Chunk Overlap 과다, FAQ 반복, 중복 문서 적재, Reindex 실패 때문에 발생할 수 있다.

Q. Deduplication은 언제 해야 해?

A.
Context Assembly 이전에 수행하는 것이 좋다.

Q. 중복 검색이 계속되면 어떻게 해?

A.
Chunk Overlap, 중복 문서, Chunk ID, Reindex 상태를 점검해야 한다.

---

# 11. Retrieval Failure

## 11.1 Expected Chunk Missing

### [개념]

Expected Chunk Missing은 기대한 Chunk가 Retrieval 결과에 포함되지 않는 문제다.

문서에 내용이 있어도 해당 Chunk가 Top-K에 들어오지 않으면 LLM은 그 내용을 사용할 수 없다.

이 문제는 RAG 시스템에서 가장 자주 발생하는 Retrieval Failure다.

---

### [핵심]

- 기대 Chunk가 Top-K에 없는 문제
- 문서에 있어도 검색되지 않을 수 있음
- Header 키워드 부족 가능
- FAQ 부족 가능
- Query와 문서 표현 불일치 가능
- Metadata Filter 오류 가능
- Top-K / Threshold 설정 문제 가능
- Reindex 누락 가능

---

### [실무]

문제 해결 형식은 다음과 같다.

```text
문제:
기대 Chunk가 Retrieval Top-K에 없음

원인:
Header가 모호함
Chunk가 여러 주제를 섞음
FAQ 질문 표현 부족
Retrieval Queries 부족
Query와 문서 표현 불일치
Metadata Filter가 과도함
Top-K가 낮음
Threshold가 높음
Embedding 재생성 누락

해결:
Header에 핵심 키워드 추가
Chunk를 단일 개념으로 재분리
FAQ와 Retrieval Queries 보강
한글/영어 용어 병기
Metadata Filter 완화
Top-K 증가 테스트
Threshold 완화 테스트
Reindex 수행
Golden Query 재검증
```

Expected Chunk Missing은 LLM 답변 단계 이전의 문제다.

먼저 검색 결과를 확인하고, 그 다음 Generation 문제를 판단해야 한다.

---

### [FAQ]

Q. Expected Chunk Missing이 뭐야?

A.
기대했던 Chunk가 Retrieval 결과 Top-K에 포함되지 않는 문제다.

Q. 문서에 있는데 검색되지 않으면 왜 그래?

A.
Header, Chunk 구조, FAQ, Metadata Filter, Top-K, Threshold, Reindex 문제일 수 있다.

Q. Expected Chunk Missing은 LLM 문제야?

A.
대부분 Retrieval 문제다. 먼저 검색 결과를 확인해야 한다.

Q. 해결하려면 무엇을 보강해야 해?

A.
Header, FAQ, Retrieval Queries, Metadata, Chunk 구조를 보강하고 Reindex해야 한다.

Q. Top-K를 늘리면 해결돼?

A.
일부 해결될 수 있지만 무관 문서도 늘 수 있으므로 Golden Query로 검증해야 한다.

---

## 11.2 Irrelevant Chunk Retrieved

### [개념]

Irrelevant Chunk Retrieved는 사용자 Query와 관련 없는 Chunk가 검색 결과에 포함되는 문제다.

Top-K가 너무 크거나 Threshold가 너무 낮거나 Chunk가 여러 주제를 섞고 있을 때 발생할 수 있다.

관련 없는 Chunk가 Context에 포함되면 LLM이 잘못된 답변을 생성할 가능성이 높아진다.

---

### [핵심]

- 무관 Chunk가 검색되는 문제
- Top-K 과다 가능
- Threshold 과소 가능
- Chunk Size 과대 가능
- 여러 주제 혼합 가능
- Metadata Filter 부족 가능
- Reranking으로 개선 가능
- Context Assembly에서 제거 필요

---

### [실무]

문제 해결 형식은 다음과 같다.

```text
문제:
관련 없는 Chunk가 Retrieval 결과에 포함됨

원인:
Top-K가 너무 큼
Threshold가 너무 낮음
Chunk가 너무 큼
Chunk에 여러 주제가 섞임
Metadata Filter가 없음
Query가 모호함
Reranking 없음

해결:
Top-K 축소
Threshold 조정
Chunk를 주제별로 분리
Metadata Filter 적용
Query Rewrite 적용
Reranking 적용 검토
Context Assembly에서 제거
Golden Query 재검증
```

무관 Chunk는 단순히 검색 결과에 있는 것만으로도 답변 품질을 낮출 수 있다.

특히 Grounding Rule이 약하면 LLM이 무관 Context를 근거처럼 사용할 수 있다.

---

### [FAQ]

Q. Irrelevant Chunk Retrieved가 뭐야?

A.
사용자 Query와 관련 없는 Chunk가 검색 결과에 포함되는 문제다.

Q. 관련 없는 Chunk가 왜 검색돼?

A.
Top-K 과다, Threshold 과소, Chunk Size 과대, Metadata Filter 부족 때문일 수 있다.

Q. 무관 Chunk가 답변에 영향을 줘?

A.
그렇다. LLM이 잘못된 Context를 근거로 답변할 수 있다.

Q. 어떻게 줄일 수 있어?

A.
Top-K, Threshold, Chunk 구조, Metadata Filter, Reranking을 조정한다.

Q. Context Assembly에서도 제거해야 해?

A.
해야 한다. Retrieval 결과를 그대로 모두 Prompt에 넣으면 답변 품질이 떨어질 수 있다.

---

# 12. Low Confidence Retrieval

## 12.1 Low Confidence

### [개념]

Low Confidence Retrieval은 검색 결과의 관련도가 낮거나, 기대 Chunk가 없거나, 검색 결과가 서로 충돌하여 답변 신뢰도가 낮은 상태다.

RAG 시스템은 Low Confidence 상황에서 억지로 답변을 생성하지 않아야 한다.

Low Confidence에서는 문서 부족, 검색 실패, Query 모호성, Metadata 문제를 명확히 표시해야 한다.

---

### [핵심]

- Low Confidence는 검색 신뢰도 낮은 상태
- 기대 Chunk가 없으면 Low Confidence 가능
- 관련도 Score가 낮으면 주의 필요
- 검색 결과가 충돌하면 답변 신뢰도 낮음
- 문서 근거 부족 시 Missing Information Rule 적용
- 확정 답변 금지
- 필요한 추가 정보 또는 문서 보강 항목 제시

---

### [실무]

Low Confidence 처리 규칙은 다음과 같다.

```text
If retrieval result is insufficient:
- Do not invent project-specific facts.
- Say the retrieved context is insufficient.
- Explain what information is missing.
- Suggest which document or metadata should be checked.
```

Agent 답변 예시는 다음과 같다.

```text
검색된 문서만으로는 확정할 수 없음.

부족한 정보:
- 해당 기능의 Controller 문서
- API Endpoint 정의
- Request / Response DTO
- 최신 Project Progress

다음 확인 필요:
- Backend Domain 문서 검색
- API Design 문서 검색
- Project Progress Reindex 여부 확인
```

Low Confidence는 실패가 아니라 안전한 답변 제어 전략이다.

---

### [FAQ]

Q. Low Confidence Retrieval이 뭐야?

A.
검색 결과의 관련도나 근거가 부족해 답변 신뢰도가 낮은 상태다.

Q. Low Confidence일 때 답변해도 돼?

A.
확정 답변은 피하고, 부족한 정보와 필요한 문서를 명확히 표시해야 한다.

Q. 검색 결과가 없으면 어떻게 해?

A.
문서에 근거가 부족하다고 말하고 필요한 문서 또는 확인 항목을 제시해야 한다.

Q. Low Confidence는 실패야?

A.
아니다. 근거 없는 답변을 막기 위한 안전한 처리 상태다.

Q. Agent는 Low Confidence를 어떻게 처리해야 해?

A.
추정과 근거를 분리하고, 필요한 문서와 검증 항목을 안내해야 한다.

---

# 13. Retrieval Evaluation

## 13.1 Golden Query Evaluation

### [개념]

Golden Query Evaluation은 미리 정한 테스트 질문으로 Retrieval 품질을 평가하는 방식이다.

Golden Query는 실제 사용자가 물어볼 가능성이 높은 질문이어야 한다.

각 Golden Query에는 Expected Document, Expected Section, Expected Chunk가 연결되어야 한다.

Retrieval 평가에서는 답변이 아니라 검색 결과를 먼저 본다.

---

### [핵심]

- Golden Query는 검색 품질 테스트 질문
- 실제 사용자 질문 표현 기반
- Expected Document 지정
- Expected Section 지정
- Expected Chunk 지정 가능
- Top-K 포함 여부 확인
- Retrieval과 Generation 평가 분리
- 실패 사례를 문서 개선에 반영

---

### [실무]

Golden Query Evaluation 예시는 다음과 같다.

```text
Golden Query:
Top-K는 어떻게 정해?

Expected Document:
Vector_Database_RAG_Part04_Retrieval_Search.md

Expected Section:
Top-K Retrieval

Pass Criteria:
Expected Chunk appears in Top-K.
Retrieved Chunk explains Top-K, Precision, Recall, Context Budget.
```

평가 기록 형식은 다음과 같다.

| 항목             | 내용                                           |
| ---------------- | ---------------------------------------------- |
| Query            | Top-K는 어떻게 정해?                           |
| Expected File    | Vector_Database_RAG_Part04_Retrieval_Search.md |
| Expected Section | Top-K Retrieval                                |
| Top-K Hit        | Yes / No                                       |
| Rank             | 1~K                                            |
| Context Quality  | Good / Weak / Bad                              |
| Failure Cause    | Header, FAQ, Metadata, Threshold               |
| Action           | 문서 보강, Reindex, 설정 조정                  |

Golden Query는 문서 제작 후, Reindex 후, 검색 설정 변경 후 반복 실행한다.

---

### [FAQ]

Q. Golden Query Evaluation이 뭐야?

A.
미리 정한 테스트 질문으로 Retrieval 품질을 평가하는 방식이다.

Q. Golden Query는 어떻게 만들어?

A.
실제 사용자가 물어볼 질문을 기준으로 만들고 기대 문서와 기대 섹션을 연결한다.

Q. Retrieval 평가에서 답변을 먼저 보면 돼?

A.
아니다. 먼저 기대 Chunk가 검색 결과에 포함되는지 확인해야 한다.

Q. Golden Query는 언제 실행해?

A.
문서 제작 후, Reindex 후, 검색 설정 변경 후 실행한다.

Q. 평가 실패는 어떻게 활용해?

A.
Header, FAQ, Retrieval Queries, Metadata, Chunk 구조 개선에 반영한다.

---

# 14. Retrieval Checklist

## 14.1 Final Checklist

### [개념]

Retrieval Checklist는 RAG 검색 품질을 검수하기 위한 기준이다.

이 Checklist는 Vector Search, Keyword Search, Hybrid Search, Top-K, Threshold, Metadata Filter, Reranking, Deduplication을 함께 점검한다.

Retrieval Checklist는 문서 제작 후, Vector Store 적재 후, Reindex 후, 검색 설정 변경 후 사용한다.

---

### [핵심]

- Query 표현과 문서 표현 매칭 확인
- Query Embedding과 Document Embedding Model 일치 확인
- Vector Search 결과 확인
- Keyword Search 필요 여부 확인
- Hybrid Search 필요 여부 확인
- Top-K 적절성 확인
- Threshold 적절성 확인
- Metadata Filter 적절성 확인
- Reranking 필요성 확인
- 중복 Chunk 제거 확인
- Golden Query 평가 수행

---

### [실무]

Retrieval Checklist는 다음과 같다.

```md
### [Checklist]

- [ ] User Query와 문서 핵심 용어가 매칭되는가?
- [ ] FAQ에 실제 사용자 질문 표현이 포함되어 있는가?
- [ ] Retrieval Queries가 문서 마지막에 포함되어 있는가?
- [ ] Query Embedding과 Document Embedding이 같은 Embedding Model을 사용하는가?
- [ ] Vector Dimension이 일치하는가?
- [ ] Expected Chunk가 Top-K에 포함되는가?
- [ ] Top-K가 너무 낮아 필요한 Chunk가 누락되지 않는가?
- [ ] Top-K가 너무 높아 무관 Chunk가 과도하게 포함되지 않는가?
- [ ] Threshold가 너무 높아 검색 실패를 만들지 않는가?
- [ ] Threshold가 너무 낮아 노이즈를 만들지 않는가?
- [ ] Metadata Filter가 필요한 문서를 제외하지 않는가?
- [ ] Agent 역할에 맞는 Domain 문서가 검색되는가?
- [ ] 클래스명, 메서드명, API Endpoint는 Keyword Search로 검색 가능한가?
- [ ] Hybrid Search가 필요한 Query 유형을 식별했는가?
- [ ] Reranking이 필요한 검색 품질 문제를 기록했는가?
- [ ] 중복 Chunk가 Context Budget을 낭비하지 않는가?
- [ ] 오래된 문서가 검색되지 않는가?
- [ ] Low Confidence 상황에서 확정 답변을 막는가?
- [ ] Golden Query 평가 결과를 기록했는가?
- [ ] 실패 사례를 문서 구조와 검색 설정 개선에 반영했는가?
```

Checklist 통과 후에도 실제 Retrieval 결과를 확인해야 한다.

RAG 검색 품질은 문서 구조와 검색 설정이 함께 만든다.

---

### [FAQ]

Q. Retrieval Checklist는 왜 필요해?

A.
RAG 검색 품질을 체계적으로 검수하기 위해 필요하다.

Q. Retrieval Checklist는 언제 사용해?

A.
문서 제작 후, Vector Store 적재 후, Reindex 후, 검색 설정 변경 후 사용한다.

Q. 가장 중요한 Retrieval 검수 항목은 뭐야?

A.
Expected Chunk가 Top-K에 포함되는지 확인하는 것이다.

Q. Keyword Search 필요 여부도 확인해야 해?

A.
해야 한다. 기술 문서는 정확한 용어 검색이 중요하기 때문이다.

Q. Checklist 통과 후에도 Golden Query가 필요해?

A.
필요하다. 실제 검색 결과로 검증해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval이 뭐야?
A. 사용자 Query와 관련 있는 문서 Chunk를 검색하는 과정이다.

Q. RAG에서 Retrieval이 중요한 이유는 뭐야?
A. 검색된 Chunk가 LLM 답변의 근거가 되기 때문이다.

Q. Retrieval 실패와 Generation 실패는 뭐가 달라?
A. Retrieval 실패는 관련 문서를 못 찾는 문제이고, Generation 실패는 검색된 문서를 잘못 사용하는 문제다.

Q. User Query가 뭐야?
A. 사용자가 RAG 시스템에 입력하는 질문 또는 요청이다.

Q. Query 표현이 왜 중요해?
A. Query 표현과 문서 표현이 너무 다르면 관련 Chunk가 검색되지 않을 수 있기 때문이다.

Q. Query Rewrite가 뭐야?
A. 사용자 질문을 검색에 유리한 핵심 용어와 의도로 다시 표현하는 과정이다.

Q. Query Embedding이 뭐야?
A. 사용자 질문을 Embedding Model로 Vector화한 결과다.

Q. Query와 Document Chunk는 같은 Embedding Model을 써야 해?
A. 그렇다. 같은 Vector 공간에서 비교해야 Similarity Search가 가능하다.

Q. Similarity Search가 뭐야?
A. Query Vector와 Chunk Vector의 유사도를 비교해 의미적으로 가까운 문서를 찾는 검색 방식이다.

Q. Vector Search는 어떤 질문에 좋아?
A. 개념 질문, 자연어 질문, 정식 용어를 모르는 질문에 좋다.

Q. Vector Search가 약한 경우는 뭐야?
A. 클래스명, 메서드명, API Endpoint, 에러 메시지처럼 정확한 문자열 검색이 필요한 경우다.

Q. Vector Search Failure가 뭐야?
A. 관련 문서가 Vector Database에 있지만 Similarity Search 결과에 나오지 않는 문제다.

Q. Vector Search가 실패하면 무엇을 확인해야 해?
A. Header, FAQ, Retrieval Queries, Chunk 구조, Metadata Filter, Top-K, Threshold, Reindex 여부를 확인해야 한다.

Q. Keyword Search가 뭐야?
A. 정확한 단어, 문구, 문자열을 기준으로 문서를 검색하는 방식이다.

Q. Keyword Search는 언제 필요해?
A. 클래스명, 메서드명, API Endpoint, 에러 메시지, 설정값 검색에 필요하다.

Q. BM25가 뭐야?
A. 문서 내 키워드 빈도와 중요도를 기반으로 검색 점수를 계산하는 대표적인 Keyword Search 방식이다.

Q. Hybrid Search가 뭐야?
A. Vector Search와 Keyword Search를 함께 사용하는 검색 방식이다.

Q. Hybrid Search는 왜 필요해?
A. 의미 검색과 정확한 키워드 검색을 함께 활용해 검색 품질을 높이기 위해 필요하다.

Q. Hybrid Search는 어떤 문서에 좋아?
A. 코드, API, 에러 메시지, 설정값, 기술 용어가 많은 문서에 좋다.

Q. Score Fusion이 뭐야?
A. Vector Search와 Keyword Search 결과의 점수를 결합해 최종 순위를 만드는 과정이다.

Q. Top-K가 뭐야?
A. Retrieval 단계에서 가져올 상위 검색 결과 개수다.

Q. Top-K를 높이면 좋은 거 아니야?
A. 항상 좋지 않다. 관련 없는 Chunk가 포함되어 답변 품질이 떨어질 수 있다.

Q. Top-K가 낮으면 뭐가 문제야?
A. 필요한 Chunk가 검색 결과에서 누락될 수 있다.

Q. Top-K는 어떻게 정해?
A. Golden Query로 기대 Chunk가 포함되는지 평가하면서 조정한다.

Q. Similarity Threshold가 뭐야?
A. Retrieval 결과로 사용할 최소 유사도 기준이다.

Q. Threshold를 높이면 좋은 거 아니야?
A. 항상 좋지 않다. 필요한 Chunk가 제외되어 검색 실패가 늘 수 있다.

Q. Threshold가 낮으면 뭐가 문제야?
A. 관련 없는 Chunk가 Retrieved Context에 포함될 수 있다.

Q. Top-K와 Threshold는 같이 봐야 해?
A. 그렇다. 둘 다 Retrieval 범위를 조정하는 기준이다.

Q. Metadata Filter가 뭐야?
A. 검색 결과를 Metadata 조건으로 제한하는 방식이다.

Q. Metadata Filter는 왜 써?
A. Domain, Level, Category, Version 기준으로 검색 범위를 줄이기 위해 사용한다.

Q. Metadata Filter가 너무 강하면 어떻게 돼?
A. 필요한 문서가 검색되지 않을 수 있다.

Q. Filter 실패 시 어떻게 해야 해?
A. Category, Level, Domain 조건을 단계적으로 완화하는 Fallback 검색을 수행해야 한다.

Q. Reranking이 뭐야?
A. 1차 Retrieval 결과를 다시 평가하여 최종 순서를 재정렬하는 단계다.

Q. Reranking은 언제 필요해?
A. 검색 후보는 나오지만 최종 관련도 순서가 불안정하거나 무관 Chunk가 섞일 때 필요하다.

Q. Reranking의 단점은 뭐야?
A. Latency와 비용이 증가할 수 있다.

Q. Deduplication이 뭐야?
A. 검색 결과에서 중복되거나 거의 동일한 Chunk를 제거하는 과정이다.

Q. 중복 Chunk가 왜 문제야?
A. Context Budget을 낭비하고 중요한 다른 Chunk가 제외될 수 있기 때문이다.

Q. Expected Chunk Missing이 뭐야?
A. 기대했던 Chunk가 Retrieval 결과 Top-K에 포함되지 않는 문제다.

Q. Expected Chunk Missing은 어떻게 해결해?
A. Header, FAQ, Retrieval Queries, Metadata, Chunk 구조를 보강하고 Reindex해야 한다.

Q. Irrelevant Chunk Retrieved가 뭐야?
A. 사용자 Query와 관련 없는 Chunk가 검색 결과에 포함되는 문제다.

Q. Irrelevant Chunk는 어떻게 줄여?
A. Top-K, Threshold, Chunk 구조, Metadata Filter, Reranking을 조정한다.

Q. Low Confidence Retrieval이 뭐야?
A. 검색 결과의 관련도나 근거가 부족해 답변 신뢰도가 낮은 상태다.

Q. Low Confidence일 때 어떻게 답해야 해?
A. 확정 답변을 피하고 부족한 정보와 필요한 문서를 명확히 표시해야 한다.

Q. Golden Query Evaluation이 뭐야?
A. 미리 정한 테스트 질문으로 Retrieval 품질을 평가하는 방식이다.

Q. Golden Query는 언제 실행해?
A. 문서 제작 후, Reindex 후, 검색 설정 변경 후 실행한다.

Q. Retrieval Checklist는 왜 필요해?
A. RAG 검색 품질을 체계적으로 검수하기 위해 필요하다.

Q. Retrieval 검수에서 가장 중요한 것은 뭐야?
A. Expected Chunk가 Top-K에 포함되는지 확인하는 것이다.

Q. Agent별 Retrieval은 어떻게 달라져?
A. Agent 역할에 따라 Domain, Level, Category Metadata Filter를 다르게 적용할 수 있다.

Q. Backend Agent 검색에는 무엇이 중요해?
A. 클래스명, 메서드명, API Endpoint, 코드 패턴을 검색할 수 있도록 Keyword Search와 Hybrid Search가 중요하다.

Q. AI Agent 검색에는 무엇이 중요해?
A. RAG, Retrieval, Embedding, Metadata, Evaluation 같은 AI Domain 문서가 우선 검색되어야 한다.

Q. Review Agent 검색에는 무엇이 중요해?
A. Checklist, Troubleshooting, Domain Rules, Source Metadata가 우선 검색되어야 한다.

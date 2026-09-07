# Graph RAG Domain Rules

---

# 1. Domain Purpose

## 1.1 Graph RAG 문서 목적

### [개념]

Graph RAG Domain 문서는 AI Agent / AI/ML Agent / Backend Agent / Review Agent / Architecture Review Agent가 Graph 기반 RAG 시스템을 설계, 구현, 검토, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

Graph RAG는 문서 Chunk를 단순 Vector Similarity로 검색하는 방식에서 확장하여, Entity, Relation, Community, Path, Graph Context를 활용해 정보를 검색하고 답변을 생성하는 RAG 구조이다.

Graph RAG는 특히 복잡한 관계, 도메인 지식 연결, 장문 문서 간 연결, 조직 지식, 코드 구조 분석, Multi-Hop Reasoning이 필요한 상황에서 사용한다.

---

### [핵심]

- Graph RAG = Retrieval + Knowledge Graph + Entity + Relation + Path + Community
- 단순 Vector Search보다 관계 검색에 강함
- Entity 중심 검색 가능
- Relation 중심 검색 가능
- Multi-Hop Reasoning 지원
- 문서 간 연결 구조 표현 가능
- Global Search와 Local Search 구분 필요
- Graph Construction 품질이 Retrieval 품질을 결정
- Vector RAG를 대체하기보다 보완하는 구조로 작성
- Agentic RAG / Multi-Agent System과 연결 가능

---

### [실무]

2026 실무 기준 Graph RAG 문서는 다음 목적을 우선한다.

- Knowledge Graph 기반 Retrieval 설계
- Entity Extraction 기준 제공
- Relation Extraction 기준 제공
- Community Detection 기준 제공
- Local Search / Global Search 전략 제공
- Hybrid Retrieval 전략 제공
- Multi-Hop Query 처리 기준 제공
- Graph Context 생성 기준 제공
- Graph RAG Evaluation 기준 제공
- Graph RAG Failure Handling 기준 제공

Graph RAG 문서는 사람이 그래프 이론을 공부하기 위한 문서가 아니라, Agent가 지식 연결 구조를 검색하고 판단할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Graph RAG 문서는 무엇을 위한 문서인가?

A. Agent가 Entity, Relation, Path, Community 기반으로 지식을 검색하고 답변할 수 있도록 기준을 제공하는 문서이다.

Q. Graph RAG는 일반 Vector RAG와 무엇이 다른가?

A. Vector RAG는 의미 유사도 중심이고, Graph RAG는 Entity와 Relation을 이용한 관계 기반 검색이 중심이다.

Q. Graph RAG는 Vector RAG를 대체하는가?

A. 아니다. Graph RAG는 Vector RAG를 보완하며, 실무에서는 Hybrid Retrieval로 함께 사용하는 경우가 많다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Graph RAG Domain 문서는 Graph 기반 Retrieval을 설계하고 운영하기 위한 개념, 구조, 작성 규칙, 검색 전략, 검증 기준을 포함한다.

---

### [핵심]

포함 범위:

- Graph RAG 개념
- Knowledge Graph
- Entity Extraction
- Relation Extraction
- Entity Resolution
- Graph Construction
- Graph Schema
- Node
- Edge
- Property
- Community Detection
- Local Search
- Global Search
- Hybrid Retrieval
- Multi-Hop Retrieval
- Path Search
- Graph Context
- Graph Summarization
- Graph Database
- Graph Embedding
- Graph RAG Evaluation
- Graph RAG Troubleshooting

제외 범위:

- 그래프 이론 수학 상세
- Graph Neural Network 상세 이론
- Neo4j 전체 매뉴얼 복붙
- Cypher 전체 문법 사전식 정리
- 특정 클라우드 Graph DB 운영 상세
- Vector Database 설치 상세
- LLM 내부 구조 상세

---

### [실무]

Graph RAG 문서는 아래 질문에 답할 수 있어야 한다.

- 어떤 정보를 Entity로 추출해야 하는가?
- 어떤 관계를 Edge로 저장해야 하는가?
- Graph Schema는 어떻게 정의해야 하는가?
- 사용자의 질문이 Local Search 대상인가 Global Search 대상인가?
- Vector Search와 Graph Search를 어떻게 결합해야 하는가?
- Multi-Hop 질문을 어떻게 처리해야 하는가?
- Graph Context를 어떻게 생성해야 하는가?
- Graph 검색 결과가 답변 근거로 충분한가?
- Graph RAG의 실패 원인은 무엇인가?

---

### [FAQ]

Q. Graph RAG 문서에 그래프 이론 수학을 자세히 넣어야 하는가?

A. 아니다. Agent가 Retrieval에 사용할 수 있는 Entity, Relation, Path, Community 중심으로 작성한다.

Q. Graph Database 설치법도 포함해야 하는가?

A. 설치법은 별도 DevOps 또는 Database 문서로 분리하고, Graph RAG에서는 검색 구조와 판단 기준을 다룬다.

Q. Graph RAG는 언제 필요한가?

A. 정보 간 관계, 계층, 원인, 의존성, 연결 경로, 전체 요약이 중요한 경우 필요하다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Graph RAG 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

검색 흐름이 중요한 주제는 `[Flow]`를 추가한다.

비교가 필요한 주제는 `[Comparison]`을 추가한다.

검증이 필요한 주제는 `[Checklist]` 또는 `[Evaluation]`을 추가한다.

---

### [핵심]

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Comparison]
- [Checklist]
- [Troubleshooting]

Optional:

- [Graph Schema]
- [Query Pattern]
- [Evaluation]
- [Anti-Pattern]
- [Review Point]

---

### [실무]

Graph RAG 문서는 단순 개념 설명보다 검색 판단 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Entity Extraction 기준
- Relation Extraction 기준
- Graph Construction Flow
- Local Search 기준
- Global Search 기준
- Hybrid Retrieval 기준
- Multi-Hop Retrieval 기준
- Graph Context 생성 기준
- Evaluation Checklist

---

### [FAQ]

Q. Graph RAG 문서에 Flow는 필수인가?

A. Graph Construction, Local Search, Global Search, Hybrid Retrieval 주제에서는 필수에 가깝다.

Q. Graph RAG 문서에 Comparison이 필요한 이유는?

A. Vector RAG, Keyword Search, Graph Search의 사용 기준을 Agent가 구분해야 하기 때문이다.

Q. Graph Schema 섹션은 언제 필요한가?

A. Node, Edge, Property 구조를 정의해야 하는 문서에서 필요하다.

---

# 4. Core Concept Rules

## 4.1 Graph RAG 핵심 개념 작성 규칙

### [개념]

Graph RAG 핵심 개념은 Vector RAG와 구분되도록 작성한다.

Graph RAG는 의미 유사도 검색만으로 부족한 관계형 지식 검색을 보완하기 위한 구조이다.

Entity와 Relation을 명확히 추출하고, 이를 Graph로 구성한 뒤, 사용자 질문에 맞는 Graph Context를 생성하는 흐름을 포함해야 한다.

---

### [핵심]

반드시 포함할 개념:

- Graph RAG
- Knowledge Graph
- Entity
- Relation
- Node
- Edge
- Property
- Entity Extraction
- Relation Extraction
- Entity Resolution
- Graph Construction
- Community
- Local Search
- Global Search
- Multi-Hop Retrieval
- Path Search
- Graph Context
- Hybrid Retrieval
- Graph Evaluation

용어 통일:

- Graph RAG
- Knowledge Graph
- Entity
- Relation
- Node
- Edge
- Property
- Community
- Local Search
- Global Search
- Multi-Hop Retrieval
- Graph Context
- Hybrid Retrieval

---

### [실무]

Graph RAG 설명은 아래 구조를 기준으로 작성한다.

```text
Documents
→ Chunking
→ Entity Extraction
→ Relation Extraction
→ Entity Resolution
→ Graph Construction
→ Community Detection
→ Graph Retrieval
→ Graph Context Generation
→ Answer Synthesis
```

Graph RAG 문서는 “그래프를 사용한다” 수준에서 멈추면 안 된다.

Agent가 어떤 정보를 Node로 만들고, 어떤 연결을 Edge로 만들고, 어떤 Query에서 Graph Search를 선택해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Graph RAG의 핵심은 무엇인가?

A. 문서에서 Entity와 Relation을 추출해 Knowledge Graph를 만들고, 관계 기반으로 검색하는 것이다.

Q. Entity는 무엇인가?

A. 사람, 조직, 기술, 서비스, 파일, 클래스, 메서드, 개념처럼 그래프의 Node가 될 수 있는 핵심 대상이다.

Q. Relation은 무엇인가?

A. Entity 간 의미 있는 연결이다. 예를 들어 “uses”, “depends_on”, “belongs_to”, “calls”, “causes” 같은 관계이다.

---

# 5. Graph Construction Rules

## 5.1 Graph Construction 작성 규칙

### [개념]

Graph Construction은 문서, 코드, 로그, 데이터에서 Entity와 Relation을 추출하여 Knowledge Graph를 구성하는 과정이다.

Graph RAG 품질은 Graph Construction 품질에 크게 의존한다.

---

### [핵심]

Graph Construction 단계:

```text
Source Documents
→ Chunking
→ Entity Extraction
→ Relation Extraction
→ Entity Resolution
→ Graph Schema Mapping
→ Node Creation
→ Edge Creation
→ Property Assignment
→ Community Detection
→ Graph Indexing
```

필수 작성 요소:

- Source 유형
- Chunking 기준
- Entity 추출 기준
- Relation 추출 기준
- 중복 Entity 병합 기준
- Node Label 기준
- Edge Type 기준
- Property 기준
- Graph 품질 검증 기준

---

### [실무]

Graph Construction 문서는 아래 형식을 권장한다.

```md
### [Graph Schema]

Node:

- Document
- Concept
- Technology
- Class
- Method
- API
- Error
- Rule

Edge:

- references
- depends_on
- implements
- calls
- configures
- causes
- resolves
- belongs_to
```

Backend / AI Agent용 Graph RAG에서는 코드 구조와 문서 구조를 함께 표현할 수 있어야 한다.

예:

```text
SpringSecurityConfig
→ configures
→ SecurityFilterChain

JwtAuthenticationFilter
→ validates
→ AccessToken

AccessToken
→ belongs_to
→ JWT Authentication
```

---

### [FAQ]

Q. Graph Construction에서 가장 중요한 단계는?

A. Entity Extraction, Relation Extraction, Entity Resolution이 가장 중요하다.

Q. Graph Schema는 왜 필요한가?

A. Node와 Edge 구조가 일관되지 않으면 검색 결과가 불안정해지기 때문이다.

Q. Relation을 너무 많이 만들면 좋은가?

A. 아니다. 불필요한 Edge가 많으면 Graph Noise가 증가하고 검색 품질이 낮아진다.

---

# 6. Entity Extraction Rules

## 6.1 Entity Extraction 작성 규칙

### [개념]

Entity Extraction은 문서나 코드에서 Graph Node가 될 핵심 대상을 추출하는 과정이다.

Graph RAG 문서는 어떤 정보를 Entity로 볼지 명확히 정의해야 한다.

---

### [핵심]

Entity 후보:

- 사람
- 조직
- 프로젝트
- 시스템
- 서비스
- 기술
- 프레임워크
- 라이브러리
- 개념
- 정책
- 문서
- 파일
- 패키지
- 클래스
- 메서드
- API Endpoint
- Database Table
- Error Message
- Configuration
- Rule
- Checklist

Entity 작성 기준:

- 검색 가치가 있는가?
- 다른 Entity와 관계를 만들 수 있는가?
- 중복 병합 가능한 이름인가?
- Domain 용어로 안정적인가?
- 너무 일반적인 단어는 아닌가?

---

### [실무]

Entity Extraction 예시:

```text
문장:
Spring Security는 SecurityFilterChain을 통해 인증과 인가 흐름을 구성한다.

Entity:
- Spring Security
- SecurityFilterChain
- Authentication
- Authorization
```

코드 기반 Entity 예시:

```text
File:
SecurityConfig.java

Entity:
- SecurityConfig
- SecurityFilterChain
- JwtAuthenticationFilter
- PasswordEncoder
```

너무 일반적인 단어는 Entity로 만들지 않는다.

부적절한 Entity:

```text
사용
처리
기능
데이터
관리
설정
```

---

### [FAQ]

Q. Entity Extraction은 왜 중요한가?

A. Entity가 Graph의 Node가 되므로 잘못 추출하면 Graph Search 품질이 낮아진다.

Q. 모든 명사를 Entity로 추출해야 하는가?

A. 아니다. 검색 가치가 있고 관계를 만들 수 있는 핵심 명사만 추출한다.

Q. 코드 파일명도 Entity가 될 수 있는가?

A. 가능하다. 파일, 클래스, 메서드, API Endpoint는 코드 분석 Graph RAG에서 중요한 Entity이다.

---

# 7. Relation Extraction Rules

## 7.1 Relation Extraction 작성 규칙

### [개념]

Relation Extraction은 Entity 간 의미 있는 연결을 Edge로 추출하는 과정이다.

Graph RAG 문서는 관계 이름과 방향을 일관되게 작성해야 한다.

---

### [핵심]

대표 Relation Type:

- references
- depends_on
- belongs_to
- implements
- extends
- calls
- uses
- configures
- validates
- generates
- stores
- reads
- writes
- causes
- resolves
- related_to
- part_of
- precedes
- follows

Relation 작성 기준:

- 방향성이 명확한가?
- 의미가 중복되지 않는가?
- 검색에 도움이 되는가?
- 너무 포괄적이지 않은가?
- Domain 전체에서 용어가 일관되는가?

---

### [실무]

Relation Extraction 예시:

```text
문장:
JwtAuthenticationFilter는 Access Token을 검증하고 SecurityContext에 Authentication을 저장한다.

Entity:
- JwtAuthenticationFilter
- Access Token
- SecurityContext
- Authentication

Relation:
- JwtAuthenticationFilter validates Access Token
- JwtAuthenticationFilter writes SecurityContext
- SecurityContext stores Authentication
```

관계 방향을 명확히 작성한다.

나쁜 예:

```text
JwtAuthenticationFilter related_to Access Token
```

좋은 예:

```text
JwtAuthenticationFilter validates Access Token
```

---

### [FAQ]

Q. Relation Extraction에서 중요한 것은?

A. 관계 방향, 관계 이름, 검색 가치, 일관성이 중요하다.

Q. related_to를 많이 사용해도 되는가?

A. 권장하지 않는다. related_to는 의미가 약하므로 가능하면 구체적인 Relation Type을 사용한다.

Q. Relation에도 Property를 넣을 수 있는가?

A. 가능하다. confidence, source, createdAt, relationType 같은 Property를 사용할 수 있다.

---

# 8. Entity Resolution Rules

## 8.1 Entity Resolution 작성 규칙

### [개념]

Entity Resolution은 같은 대상을 가리키는 여러 표현을 하나의 Entity로 병합하는 과정이다.

Graph RAG에서는 Entity 중복이 많아지면 검색 품질이 급격히 낮아진다.

---

### [핵심]

Entity Resolution 대상:

- 약어와 풀네임
- 대소문자 차이
- 띄어쓰기 차이
- 한글 / 영어 혼용
- 버전명 포함 여부
- 파일명 / 클래스명 차이
- 같은 개념의 다른 표현

예:

```text
JWT
Json Web Token
JSON Web Token
Access Token 기반 JWT
```

Entity Resolution 기준:

- canonicalName 지정
- alias 목록 관리
- Domain 용어 우선
- 문서 제목과 코드 명칭 우선
- 불확실한 병합 금지

---

### [실무]

Entity Resolution 문서는 아래 형식을 권장한다.

```md
Canonical Entity:

- SecurityFilterChain

Aliases:

- Security Filter Chain
- Spring Security Filter Chain
- 필터 체인

Resolution Rule:

- Spring Security 문맥에서는 SecurityFilterChain으로 통일
```

잘못된 병합은 Graph RAG 품질에 치명적이다.

예:

```text
Access Token
Refresh Token
```

두 Entity는 모두 Token이지만 역할이 다르므로 병합하면 안 된다.

---

### [FAQ]

Q. Entity Resolution은 왜 필요한가?

A. 같은 Entity가 여러 이름으로 저장되면 Graph Search가 분산되고 검색 품질이 떨어지기 때문이다.

Q. 비슷한 Entity는 모두 병합해야 하는가?

A. 아니다. 역할이 다르면 분리해야 한다.

Q. canonicalName은 어떻게 정하는가?

A. Domain에서 가장 표준적인 용어, 코드 명칭, 문서 제목을 우선한다.

---

# 9. Graph Schema Rules

## 9.1 Graph Schema 작성 규칙

### [개념]

Graph Schema는 Knowledge Graph의 Node Label, Edge Type, Property 구조를 정의하는 규칙이다.

Graph RAG 문서에서는 Graph Schema가 Retrieval 목적에 맞게 설계되어야 한다.

---

### [핵심]

Graph Schema 구성 요소:

- Node Label
- Edge Type
- Node Property
- Edge Property
- Constraint
- Index
- Source Metadata
- Version Metadata

Node Property 예시:

- id
- name
- canonicalName
- aliases
- type
- description
- source
- domain
- version
- confidence

Edge Property 예시:

- type
- source
- confidence
- evidence
- createdAt
- updatedAt

---

### [실무]

Graph Schema 예시:

```text
Node Labels:
- Document
- Chunk
- Concept
- Technology
- CodeFile
- Class
- Method
- API
- Error
- Rule

Edge Types:
- contains
- references
- depends_on
- calls
- implements
- configures
- causes
- resolves
- belongs_to

Properties:
- canonicalName
- aliases
- sourceFile
- domain
- confidence
- evidence
```

Graph Schema는 너무 복잡하게 시작하지 않는다.

초기에는 Node Label과 Edge Type을 제한하고, 실제 Query Pattern이 늘어나면 확장한다.

---

### [FAQ]

Q. Graph Schema는 꼭 필요한가?

A. 필요하다. Schema가 없으면 Node와 Edge가 일관되지 않아 Retrieval 품질이 낮아진다.

Q. 처음부터 복잡한 Schema를 만들어야 하는가?

A. 아니다. 핵심 Node와 Edge부터 시작하고 Query Pattern에 따라 확장한다.

Q. Edge Property에는 무엇을 넣는가?

A. source, confidence, evidence, relationType, createdAt 같은 검증 가능한 정보를 넣는다.

---

# 10. Local Search Rules

## 10.1 Local Search 작성 규칙

### [개념]

Local Search는 특정 Entity나 좁은 주제 주변의 관계를 따라 검색하는 방식이다.

특정 기술, 클래스, 오류, API, 설정, 기능의 세부 관계를 찾을 때 사용한다.

---

### [핵심]

Local Search 사용 상황:

- 특정 Entity 중심 질문
- 특정 코드 파일 분석
- 특정 오류 원인 분석
- 특정 API 영향 범위 확인
- 특정 기술의 의존 관계 확인
- 특정 설정값의 역할 확인
- 특정 기능의 연결 구조 확인

Local Search 흐름:

```text
User Query
→ Entity Detection
→ Entity Matching
→ Neighbor Search
→ Path Search
→ Context Selection
→ Answer Synthesis
```

---

### [실무]

Local Search 예시:

```text
질문:
JwtAuthenticationFilter가 어떤 역할을 해?

Local Search:
1. JwtAuthenticationFilter Entity 검색
2. 연결된 Access Token, SecurityContext, Authentication 검색
3. validates, writes, stores Relation 확인
4. 관련 Chunk 선택
5. 역할 설명 생성
```

Local Search는 Entity Matching 품질이 중요하다.

Entity를 찾지 못하면 Vector Search로 보완한다.

---

### [FAQ]

Q. Local Search는 언제 사용하는가?

A. 특정 Entity, 파일, 클래스, 오류, API, 기술에 대한 세부 관계를 찾을 때 사용한다.

Q. Local Search의 핵심은 무엇인가?

A. 정확한 Entity Matching과 주변 Relation 탐색이다.

Q. Entity를 찾지 못하면 어떻게 하는가?

A. Vector Search 또는 Keyword Search로 후보 Chunk를 찾고 Entity를 다시 추출한다.

---

# 11. Global Search Rules

## 11.1 Global Search 작성 규칙

### [개념]

Global Search는 전체 Graph 또는 Community 단위 요약을 기반으로 넓은 범위의 질문에 답하는 검색 방식이다.

문서 전체 흐름, 시스템 전체 구조, 도메인 요약, 아키텍처 이해에 사용한다.

---

### [핵심]

Global Search 사용 상황:

- 전체 시스템 요약
- 프로젝트 구조 요약
- 도메인 전체 개념 설명
- 기술 스택 관계 설명
- 여러 문서의 공통 패턴 분석
- Architecture Review
- 전체 영향 범위 파악
- 큰 주제의 요약 답변

Global Search 흐름:

```text
User Query
→ Topic Detection
→ Community Search
→ Community Summary Retrieval
→ Key Entity Selection
→ Global Context Assembly
→ Answer Synthesis
```

---

### [실무]

Global Search 예시:

```text
질문:
이 프로젝트의 인증 구조 전체를 설명해줘

Global Search:
1. Authentication 관련 Community 검색
2. SecurityConfig, JWT, Filter, User, Token Entity 확인
3. Community Summary 검색
4. 주요 Entity와 Relation 선택
5. 전체 인증 Flow 생성
```

Global Search는 전체 맥락을 제공하지만 세부 구현 검증에는 Local Search를 함께 사용한다.

---

### [FAQ]

Q. Global Search는 언제 사용하는가?

A. 전체 구조, 전체 요약, 여러 문서의 공통 주제, 아키텍처 흐름을 파악할 때 사용한다.

Q. Global Search만으로 충분한가?

A. 아니다. 세부 구현이나 특정 오류 분석은 Local Search와 함께 사용해야 한다.

Q. Community Summary는 왜 필요한가?

A. 전체 Graph를 직접 모두 넣을 수 없기 때문에 Community 단위 요약으로 Context를 압축하기 위해 필요하다.

---

# 12. Hybrid Retrieval Rules

## 12.1 Hybrid Retrieval 작성 규칙

### [개념]

Hybrid Retrieval은 Graph Search, Vector Search, Keyword Search를 함께 사용하는 검색 전략이다.

Graph RAG는 Graph Search만 사용하는 구조가 아니라, 질문 유형에 따라 여러 검색 방식을 조합해야 한다.

---

### [핵심]

검색 방식별 강점:

- Graph Search: Entity, Relation, Path, 영향 범위
- Vector Search: 의미 유사도, 개념 설명, 자연어 질문
- Keyword Search: 코드, 명령어, 에러 메시지, 설정값
- Metadata Search: 버전, Domain, 문서 유형, 작성 시점
- Re-Ranking: 검색 결과 정렬 및 노이즈 제거

Hybrid Retrieval 선택 기준:

- 특정 Entity 질문 → Graph Search
- 개념 설명 질문 → Vector Search
- 에러 메시지 질문 → Keyword Search
- 최신 버전 필요 → Metadata Search
- 복합 질문 → Graph + Vector + Keyword Search

---

### [실무]

Hybrid Retrieval Flow:

```text
User Query
→ Query Classification
→ Entity Detection
→ Keyword Extraction
→ Graph Search
→ Vector Search
→ Keyword Search
→ Result Merge
→ Re-Ranking
→ Context Selection
→ Answer Synthesis
```

예시:

```text
질문:
SecurityFilterChain 설정 오류 때문에 JWT 인증이 안 돼

검색 전략:
1. SecurityFilterChain Entity Graph Search
2. JWT Authentication Vector Search
3. 오류 메시지 Keyword Search
4. Security Common Mistakes 검색
5. Troubleshooting Chunk 선택
```

---

### [FAQ]

Q. Graph RAG에서 Vector Search가 여전히 필요한가?

A. 필요하다. Graph Search는 관계에 강하고 Vector Search는 의미 유사도와 개념 검색에 강하다.

Q. Hybrid Retrieval의 핵심은 무엇인가?

A. 질문 유형에 따라 Graph, Vector, Keyword, Metadata Search를 조합하는 것이다.

Q. 검색 결과 병합 후 무엇을 해야 하는가?

A. 중복 제거, Re-Ranking, Context Selection, 충돌 검증을 수행해야 한다.

---

# 13. Multi-Hop Retrieval Rules

## 13.1 Multi-Hop Retrieval 작성 규칙

### [개념]

Multi-Hop Retrieval은 하나의 Entity에서 다른 Entity로 여러 관계를 따라가며 정보를 찾는 검색 방식이다.

Graph RAG는 Multi-Hop 질문 처리에 강하다.

---

### [핵심]

Multi-Hop Retrieval 사용 상황:

- A가 B에 어떤 영향을 주는가?
- 특정 오류의 원인은 무엇인가?
- 특정 설정 변경이 어떤 기능에 영향을 주는가?
- API 변경이 어떤 Service와 Entity에 연결되는가?
- Agent Workflow에서 어떤 단계가 누락되었는가?
- 기술 A와 기술 B는 어떤 경로로 연결되는가?

Multi-Hop Search 흐름:

```text
Start Entity
→ 1-Hop Neighbor
→ 2-Hop Neighbor
→ Path Filtering
→ Evidence Selection
→ Context Generation
```

---

### [실무]

Multi-Hop Retrieval 예시:

```text
질문:
Refresh Token 로직 변경이 로그인 응답에 어떤 영향을 줘?

Graph Path:
Refresh Token
→ generated_by
→ AuthService
→ returns
→ LoginResDto
→ used_by
→ AuthController
```

Path는 짧고 설명 가능한 경로를 우선한다.

너무 긴 Path는 근거성이 약해질 수 있으므로 제한한다.

---

### [FAQ]

Q. Multi-Hop Retrieval은 언제 필요한가?

A. 여러 Entity의 연결 관계를 따라가야 답할 수 있는 질문에서 필요하다.

Q. Hop 수는 많을수록 좋은가?

A. 아니다. Hop 수가 많아질수록 노이즈와 잘못된 연결 가능성이 커진다.

Q. Multi-Hop 결과는 어떻게 검증하는가?

A. 각 Edge의 evidence와 source를 확인하고, 필요한 경우 원문 Chunk를 함께 검색한다.

---

# 14. Graph Context Rules

## 14.1 Graph Context 작성 규칙

### [개념]

Graph Context는 Graph Search 결과를 LLM이 사용할 수 있는 입력 Context로 변환한 것이다.

Node와 Edge를 그대로 나열하는 것보다, 질문에 맞는 Evidence 중심 구조로 정리해야 한다.

---

### [핵심]

Graph Context 구성 요소:

- Query
- Matched Entity
- Related Entity
- Relation Path
- Evidence Chunk
- Source Document
- Confidence
- Community Summary
- Conflict Note
- Missing Information

Graph Context 작성 기준:

- 질문과 직접 관련된 Node / Edge 우선
- Path는 짧고 명확하게
- Evidence Chunk 포함
- Source Metadata 포함
- 충돌 정보 표시
- 불확실한 Relation은 낮은 confidence 표시

---

### [실무]

Graph Context 예시:

```text
Matched Entity:
- JwtAuthenticationFilter

Relevant Path:
- JwtAuthenticationFilter validates Access Token
- JwtAuthenticationFilter writes SecurityContext
- SecurityContext stores Authentication

Evidence:
- Security_Advanced_Part03_Filter_Chain.md
- Security_Advanced_Part04_JWT.md

Answer Focus:
- JWT 검증
- 인증 객체 저장
- Filter Chain 내 위치
```

Graph Context는 최종 답변용으로 압축되어야 한다.

전체 Graph를 그대로 Context에 넣지 않는다.

---

### [FAQ]

Q. Graph Context는 무엇인가?

A. Graph Search 결과를 LLM이 답변 생성에 사용할 수 있도록 정리한 Context이다.

Q. Node와 Edge를 모두 넣어야 하는가?

A. 아니다. 질문과 직접 관련된 Node, Edge, Evidence만 선택해야 한다.

Q. Graph Context에 Evidence가 필요한 이유는?

A. Graph Relation이 실제 문서 근거에 기반했는지 검증하기 위해 필요하다.

---

# 15. Community Detection Rules

## 15.1 Community Detection 작성 규칙

### [개념]

Community Detection은 Graph 내에서 서로 강하게 연결된 Entity 그룹을 찾는 과정이다.

Graph RAG에서는 Community Summary를 생성하여 전체 주제 요약과 Global Search에 활용한다.

---

### [핵심]

Community 사용 목적:

- 전체 주제 요약
- 대규모 문서 압축
- Global Search 지원
- 관련 Entity 묶음 제공
- 도메인별 지식 그룹화
- Architecture 단위 분석
- 시스템 영향 범위 분석

Community Summary 포함 요소:

- Community 이름
- 핵심 Entity
- 핵심 Relation
- 주요 Source
- 요약 설명
- 사용 가능한 Query Pattern

---

### [실무]

Community Summary 예시:

```text
Community:
JWT Authentication

Key Entities:
- Access Token
- Refresh Token
- JwtAuthenticationFilter
- SecurityContext
- Authentication

Key Relations:
- JwtAuthenticationFilter validates Access Token
- SecurityContext stores Authentication
- Refresh Token regenerates Access Token

Use Cases:
- 인증 흐름 설명
- JWT 오류 분석
- Security Filter Chain 검토
```

Community는 너무 크게 만들지 않는다.

너무 큰 Community는 검색 정확도를 낮추고, 너무 작은 Community는 Global Search 품질을 낮춘다.

---

### [FAQ]

Q. Community Detection은 왜 필요한가?

A. 대규모 Graph를 주제 단위로 압축하고 Global Search에 활용하기 위해 필요하다.

Q. Community Summary에는 무엇을 넣어야 하는가?

A. Community 이름, 핵심 Entity, 핵심 Relation, 주요 Source, 사용 가능한 Query Pattern을 넣는다.

Q. Community가 너무 크면 어떤 문제가 생기는가?

A. 요약이 모호해지고 검색 결과가 넓어져 Retrieval Precision이 낮아진다.

---

# 16. Graph Evaluation Rules

## 16.1 Graph RAG Evaluation 작성 규칙

### [개념]

Graph RAG Evaluation은 Graph Construction, Graph Search, Graph Context, 최종 답변 품질을 평가하는 기준이다.

Graph RAG는 일반 RAG 평가에 더해 Entity, Relation, Path 품질을 평가해야 한다.

---

### [핵심]

평가 항목:

- Entity Extraction Accuracy
- Relation Extraction Accuracy
- Entity Resolution Quality
- Graph Schema Consistency
- Graph Connectivity
- Graph Noise
- Local Search Precision
- Global Search Coverage
- Multi-Hop Path Validity
- Context Groundedness
- Evidence Completeness
- Answer Faithfulness
- Answer Completeness
- Retrieval Latency

---

### [실무]

Graph RAG 평가 Checklist:

```md
### [Checklist]

- 핵심 Entity가 누락되지 않았는가?
- 중복 Entity가 과도하게 생성되지 않았는가?
- Relation 방향이 올바른가?
- Edge Type이 구체적인가?
- Entity Resolution이 잘못 병합하지 않았는가?
- Local Search 결과가 질문과 직접 관련 있는가?
- Global Search 결과가 전체 맥락을 충분히 제공하는가?
- Multi-Hop Path에 Evidence가 있는가?
- Graph Context가 답변에 실제 사용되었는가?
- 답변이 Graph Evidence와 일치하는가?
```

평가는 Graph 생성 단계와 답변 생성 단계를 분리해서 수행한다.

---

### [FAQ]

Q. Graph RAG 평가는 일반 RAG 평가와 무엇이 다른가?

A. Entity, Relation, Path, Community, Graph Context 품질까지 평가해야 한다.

Q. Relation 방향도 평가해야 하는가?

A. 해야 한다. Relation 방향이 틀리면 Multi-Hop Retrieval 결과가 잘못될 수 있다.

Q. Graph Noise는 무엇인가?

A. 검색 가치가 낮거나 잘못된 Node와 Edge가 많아져 검색 품질을 떨어뜨리는 상태이다.

---

# 17. Troubleshooting Rules

## 17.1 Graph RAG 장애 대응 작성 규칙

### [개념]

Graph RAG Troubleshooting 문서는 Graph 생성, 검색, Context 구성, 답변 생성 과정에서 발생하는 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- Entity 누락
- Entity 과다 추출
- Entity 중복
- 잘못된 Entity 병합
- Relation 누락
- Relation 방향 오류
- related_to 남발
- Graph Schema 불일치
- Graph Noise 증가
- Community Summary 부정확
- Local Search 실패
- Global Search 과다 일반화
- Multi-Hop Path 오류
- Graph Context 과다
- Evidence 없는 답변 생성

---

### [실무]

Troubleshooting 형식:

```md
문제:
Local Search가 관련 Entity를 찾지 못함

원인:

- Entity Alias 누락
- Entity Resolution 실패
- Keyword와 canonicalName 불일치
- Graph Index 미반영

해결:

- Alias 목록 추가
- Entity Resolution Rule 보완
- Keyword Search로 후보 Chunk 검색
- Graph 재색인 수행
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. Graph RAG에서 가장 흔한 실패는?

A. Entity 추출 오류, Relation 방향 오류, Entity 중복, Graph Noise, Evidence 없는 답변 생성이다.

Q. related_to Edge가 너무 많으면 어떻게 해야 하는가?

A. 구체적인 Relation Type으로 대체하고 검색 가치가 낮은 Edge를 제거한다.

Q. Multi-Hop 결과가 이상하면 무엇을 확인해야 하는가?

A. 각 Hop의 Relation 방향, Edge Evidence, Entity Resolution 결과를 확인해야 한다.

---

# 18. Common Mistakes

## 18.1 자주 발생하는 작성 오류

### [개념]

Graph RAG 문서는 단순히 “그래프를 이용한 RAG”를 설명하는 문서가 아니다.

Agent가 Entity와 Relation을 기준으로 검색 전략을 선택하고, Graph Context를 생성하며, 답변 근거를 검증할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- Graph RAG를 Vector RAG 대체제로만 설명
- Entity Extraction 기준 누락
- Relation Extraction 기준 누락
- Entity Resolution 기준 누락
- Graph Schema 없이 Node / Edge 생성
- related_to 관계 남발
- Relation 방향성 누락
- Evidence 없는 Edge 생성
- Local Search / Global Search 구분 누락
- Multi-Hop Retrieval 기준 누락
- Community Summary 기준 누락
- Graph Context 생성 기준 누락
- Evaluation Checklist 누락
- Troubleshooting 누락
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Graph RAG는 Knowledge Graph를 이용해서 RAG 성능을 높이는 방법이다.
Neo4j를 사용하면 Graph RAG를 만들 수 있다.
```

좋은 문서 예시:

```text
Graph RAG는 Entity와 Relation을 추출해 Knowledge Graph를 구성하고, Local Search, Global Search, Multi-Hop Retrieval로 Graph Context를 생성하는 RAG 구조이다.

Flow:
Documents
→ Entity Extraction
→ Relation Extraction
→ Graph Construction
→ Local / Global Search
→ Graph Context
→ Answer Synthesis
```

---

### [FAQ]

Q. Graph RAG 문서에서 가장 피해야 할 것은?

A. Entity, Relation, Schema, Search Strategy 없이 개념 설명만 길게 작성하는 것이다.

Q. Graph RAG에서 related_to는 사용하면 안 되는가?

A. 사용할 수 있지만 남발하면 안 된다. 가능하면 구체적인 Relation Type을 사용한다.

Q. Graph RAG 문서에 Neo4j 코드만 많이 넣으면 좋은가?

A. 아니다. Domain Rules에서는 도구보다 Graph 구조, 검색 전략, 검증 기준이 더 중요하다.

---

# 19. Document Split Rules

## 19.1 Graph RAG 문서 분할 기준

### [개념]

Graph RAG는 Graph Construction, Search Strategy, Context Generation, Evaluation 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Graph_RAG_Part01_Core.md
Graph_RAG_Part02_Entity_Relation_Extraction.md
Graph_RAG_Part03_Graph_Schema_Construction.md
Graph_RAG_Part04_Local_Global_Search.md
Graph_RAG_Part05_Hybrid_Multi_Hop_Retrieval.md
Graph_RAG_Part06_Graph_Context_Community.md
Graph_RAG_Part07_Evaluation_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Entity / Relation은 별도 Part 권장
- Search Strategy는 Local / Global / Hybrid로 분리
- Evaluation은 Checklist 중심
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Graph RAG 문서 Set은 AI Expert Level에서 사용한다.

단, PM Agent와 Review Agent도 참조할 수 있으므로 도구 종속 설명보다 구조, 판단 기준, 검증 기준을 우선한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Graph_RAG_Domain_Rules.md
Neo4j_Domain_Rules.md
LangGraph_Graph_RAG_Part.md
VectorDB_Graph_Hybrid_Search_Part.md
```

---

### [FAQ]

Q. Graph RAG 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 6~7개 Part를 권장한다. Core, Entity/Relation, Schema, Search, Hybrid/Multi-Hop, Context/Community, Evaluation/Troubleshooting으로 분리한다.

Q. Neo4j 문서와 Graph RAG 문서를 합쳐도 되는가?

A. 권장하지 않는다. Graph RAG는 검색 구조와 전략 중심이고, Neo4j는 구현 도구 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 20. Agent Usage Rules

## 20.1 Agent별 사용 기준

### [개념]

Graph RAG Domain Rules는 여러 Agent가 Graph 기반 지식 검색과 검증을 동일한 기준으로 수행하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Graph RAG Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- Graph RAG 적용 여부 판단
- User Request 분해
- Local Search / Global Search 선택
- Specialist Agent Routing

AI/ML Agent:

- Graph RAG 구조 설계
- Entity / Relation 추출 기준 설계
- Graph Search 전략 설계
- Evaluation 설계

Backend Agent:

- Graph 저장 구조 구현
- Entity / Relation API 구현
- Graph DB 연동
- Hybrid Retrieval Pipeline 구현

DevOps Agent:

- Graph DB 운영
- Index 관리
- Graph Pipeline 배포
- Monitoring 구성

Review Agent:

- Entity 누락 검토
- Relation 방향 검토
- Evidence 검증
- Graph Context 품질 검토
- Hallucination 검토

Architecture Review Agent:

- 시스템 구조 Graph 분석
- 의존성 분석
- 영향 범위 분석
- 모듈 경계 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Core Concept / Local Search / Global Search / Document Split

AI/ML Agent
→ Graph Construction / Entity Extraction / Relation Extraction / Hybrid Retrieval / Evaluation

Backend Agent
→ Graph Schema / Graph DB / API / Pipeline / Index

DevOps Agent
→ Graph DB 운영 / Monitoring / Pipeline Failure Handling

Review Agent
→ Evaluation / Evidence / Common Mistakes / Troubleshooting

Architecture Review Agent
→ Multi-Hop Retrieval / Dependency Graph / Community Summary
```

---

### [FAQ]

Q. Graph RAG Domain Rules는 AI Agent만 사용하는가?

A. 아니다. PM Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent도 역할별로 사용한다.

Q. Review Agent는 Graph RAG에서 무엇을 검토하는가?

A. Entity 누락, Relation 방향, Evidence, Graph Context, Hallucination 가능성을 검토한다.

Q. Backend Agent는 어떤 부분을 우선 검색해야 하는가?

A. Graph Schema, Entity / Relation 저장 구조, Graph DB 연동, Hybrid Retrieval Pipeline을 우선 검색한다.

---

# 21. Final Goal

## 21.1 최종 목표

### [개념]

Graph RAG Domain Rules의 최종 목표는 Agent가 Graph 기반 Retrieval 구조를 설계하고, Entity와 Relation을 활용해 지식 연결을 검색하며, 근거 기반 답변을 생성할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Graph RAG 개념 검색 가능
- Knowledge Graph 설계 가능
- Entity Extraction 기준 판단 가능
- Relation Extraction 기준 판단 가능
- Entity Resolution 가능
- Graph Schema 설계 가능
- Local Search 선택 가능
- Global Search 선택 가능
- Hybrid Retrieval 설계 가능
- Multi-Hop Retrieval 수행 가능
- Graph Context 생성 가능
- Community Summary 활용 가능
- Graph RAG Evaluation 가능
- Troubleshooting 가능

---

### [실무]

Graph RAG RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Query Classification
→ Entity Detection
→ Graph Search 선택
→ Vector / Keyword Search 보완
→ Graph Context 생성
→ Evidence 검증
→ Answer Synthesis
→ Review Agent 검토
```

Graph RAG 문서 품질은 Entity, Relation, Schema, Search Strategy, Evidence 품질로 결정된다.

---

### [FAQ]

Q. Graph RAG Domain Rules의 최종 목적은?

A. Agent가 Entity, Relation, Path, Community 기반으로 Graph Retrieval을 수행할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Graph 기반 검색 판단 품질을 높이기 위한 문서이다.

Q. Graph RAG 문서 품질은 무엇으로 판단하는가?

A. Agent가 필요한 Entity와 Relation을 검색하고, Graph Context를 근거로 답변할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Graph RAG란?
A. 문서에서 Entity와 Relation을 추출해 Knowledge Graph를 구성하고, 관계 기반으로 검색하는 RAG 구조이다.

Q. Graph RAG와 Vector RAG의 차이는?
A. Vector RAG는 의미 유사도 검색 중심이고, Graph RAG는 Entity, Relation, Path 기반 관계 검색 중심이다.

Q. Graph RAG는 Vector RAG를 대체하는가?
A. 아니다. Graph RAG는 Vector RAG를 보완하며 실무에서는 Hybrid Retrieval로 함께 사용한다.

Q. Graph RAG Workflow는?
A. Documents → Entity Extraction → Relation Extraction → Graph Construction → Graph Search → Graph Context → Answer Synthesis 흐름이다.

Q. Entity Extraction이란?
A. 문서나 코드에서 Graph Node가 될 핵심 대상을 추출하는 과정이다.

Q. Relation Extraction이란?
A. Entity 간 의미 있는 연결을 Edge로 추출하는 과정이다.

Q. Entity Resolution이란?
A. 같은 대상을 가리키는 여러 표현을 하나의 canonical Entity로 병합하는 과정이다.

Q. Graph Schema란?
A. Knowledge Graph의 Node Label, Edge Type, Property 구조를 정의하는 규칙이다.

Q. Local Search란?
A. 특정 Entity 주변의 관계와 경로를 검색하는 방식이다.

Q. Global Search란?
A. 전체 Graph 또는 Community Summary를 기반으로 넓은 범위의 질문에 답하는 검색 방식이다.

Q. Hybrid Retrieval이란?
A. Graph Search, Vector Search, Keyword Search, Metadata Search를 함께 사용하는 검색 전략이다.

Q. Multi-Hop Retrieval이란?
A. 하나의 Entity에서 다른 Entity로 여러 Relation을 따라가며 정보를 찾는 검색 방식이다.

Q. Graph Context란?
A. Graph Search 결과를 LLM이 답변 생성에 사용할 수 있도록 정리한 Context이다.

Q. Community Detection은 왜 필요한가?
A. 대규모 Graph를 주제 단위로 압축하고 Global Search에 활용하기 위해 필요하다.

Q. Graph RAG Evaluation 항목은?
A. Entity Accuracy, Relation Accuracy, Entity Resolution, Path Validity, Graph Context Groundedness, Answer Faithfulness이다.

Q. Graph RAG에서 흔한 실패는?
A. Entity 누락, Entity 중복, Relation 방향 오류, related_to 남발, Evidence 없는 답변 생성이다.

Q. Graph RAG 문서 분할은 어떻게 하는가?
A. Core, Entity/Relation, Schema, Search, Hybrid/Multi-Hop, Context/Community, Evaluation/Troubleshooting으로 분리한다.

Q. Review Agent는 Graph RAG에서 무엇을 검토하는가?
A. Entity 누락, Relation 방향, Edge Evidence, Graph Context 품질, Hallucination 가능성을 검토한다.

Q. Graph RAG 문서에서 피해야 할 것은?
A. Entity, Relation, Schema, Search Strategy 없이 개념 설명만 길게 작성하는 것이다.

Q. Graph RAG Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

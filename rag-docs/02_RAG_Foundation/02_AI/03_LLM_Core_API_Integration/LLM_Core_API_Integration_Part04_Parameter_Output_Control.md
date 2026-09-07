# LLM Core & API Integration Part04 - Parameter & Output Control

---

# 1. Parameter Control

## 1.1 LLM Parameter

### [개념]

LLM Parameter는 모델의 출력 방식, 길이, 다양성, 형식, 중단 조건을 제어하는 설정값이다.

Parameter는 LLM API Request Body에 포함되며 작업 목적에 따라 다르게 설정한다.

주요 Parameter:

- Temperature
- Top-p
- Max Tokens
- Stop Sequence
- Frequency Penalty
- Presence Penalty
- Seed
- Response Format
- Stream
- Tool Choice

Parameter Control Flow:

```text
User Task
→ Select Model
→ Set Parameter
→ Call LLM API
→ Validate Output
→ Adjust Parameter if Needed
```

---

### [핵심]

- Parameter는 출력 품질과 안정성에 직접 영향을 준다.
- 정확성 중심 작업은 낮은 Temperature를 사용한다.
- 창의성 중심 작업은 Temperature 또는 Top-p를 높일 수 있다.
- Max Tokens는 출력 길이, 비용, Latency를 제어한다.
- Stop Sequence는 출력 중단 조건을 제어한다.
- JSON Output은 낮은 Temperature와 Schema Validation을 함께 사용한다.
- Provider마다 지원 Parameter가 다를 수 있다.

---

### [실무]

2026 실무 기준 Parameter는 Agent Role과 작업 유형별로 기본값을 분리한다.

작업별 Parameter 기준:

| 작업              | Temperature |       Max Tokens | Output          |
| ----------------- | ----------: | ---------------: | --------------- |
| RAG 답변          |        낮게 |             중간 | Markdown        |
| 코드 생성         |        낮게 |        중간~크게 | Code            |
| 코드 리뷰         |        낮게 |             중간 | Markdown / JSON |
| JSON Output       |        낮게 | Schema 크기 기준 | JSON            |
| 요약              |   낮게~중간 |             중간 | Markdown        |
| 기획 브레인스토밍 |        중간 |             중간 | Markdown        |
| 창작              |   중간~높게 |        작업 기준 | Free Text       |

Agent별 Parameter 예:

```text
PM Agent
→ temperature: 0.2 ~ 0.5
→ planning, requirement summary

Backend Agent
→ temperature: 0.1 ~ 0.3
→ code generation, API design

Review Agent
→ temperature: 0.0 ~ 0.2
→ validation, risk detection

RAG Answer Agent
→ temperature: 0.0 ~ 0.2
→ grounded answer
```

주의:

- Parameter 조정만으로 Hallucination이 사라지지 않는다.
- 낮은 Temperature가 사실 정확성을 보장하지 않는다.
- Max Tokens가 작으면 출력이 잘린다.
- Provider가 지원하지 않는 Parameter를 보내면 400 Bad Request가 발생할 수 있다.
- Parameter 변경은 테스트 결과와 함께 관리한다.

---

### [FAQ]

Q. LLM Parameter가 뭐야?

A. LLM의 출력 다양성, 길이, 형식, 중단 조건 등을 제어하는 설정값이다.

Q. Parameter는 왜 중요해?

A. 같은 Prompt라도 Parameter에 따라 응답의 안정성, 창의성, 길이, 비용이 달라지기 때문이다.

Q. 코드 생성에는 어떤 Parameter가 좋아?

A. 낮은 Temperature, 적절한 Max Tokens, 명확한 출력 형식이 적합하다.

Q. RAG 답변에는 어떤 Parameter가 좋아?

A. 낮은 Temperature와 충분한 Max Tokens를 사용하고, 문서 근거 기반 답변 규칙을 함께 적용한다.

Q. Parameter만 잘 조정하면 정확한 답이 나와?

A. 아니다. Retrieved Context, Prompt, Validation, Tool Result 검증이 함께 필요하다.

---

## 1.2 Temperature

### [개념]

Temperature는 LLM 출력의 무작위성과 다양성을 조절하는 Parameter이다.

Temperature가 낮으면 모델은 확률이 높은 Token을 더 안정적으로 선택한다.

Temperature가 높으면 다양한 Token을 선택할 가능성이 커진다.

Temperature 효과:

```text
Low Temperature
→ Stable Output
→ Deterministic-like Response
→ Suitable for Code / RAG / Review

High Temperature
→ Diverse Output
→ Creative Response
→ Higher Hallucination Risk
```

---

### [핵심]

- Temperature는 출력 다양성을 조절한다.
- 낮은 Temperature는 일관성과 안정성에 유리하다.
- 높은 Temperature는 창의성과 다양성에 유리하다.
- 코드 생성, 코드 리뷰, RAG 답변은 낮은 Temperature가 적합하다.
- 창작, 아이디어 발산은 중간~높은 Temperature를 사용할 수 있다.
- Temperature 0이어도 완전한 결정론을 보장하지 않는다.

---

### [실무]

작업별 Temperature 기준:

| 작업               | 권장 방향 |
| ------------------ | --------- |
| 코드 생성          | 낮게      |
| 코드 리뷰          | 낮게      |
| RAG 문서 기반 답변 | 낮게      |
| JSON Output        | 낮게      |
| 테스트 케이스 생성 | 낮게~중간 |
| 문서 요약          | 낮게~중간 |
| 요구사항 정리      | 낮게~중간 |
| 기획 아이디어      | 중간      |
| 창작               | 중간~높게 |

예시 Request:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "You are a backend code review assistant."
    },
    {
      "role": "user",
      "content": "Review this service code."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200
}
```

실무 기준:

```text
정확성 중요
→ Temperature 낮게
→ Response Validation 적용

창의성 중요
→ Temperature 중간 이상 가능
→ 결과 후보 검토

JSON Output 중요
→ Temperature 낮게
→ Schema Validation 필수
```

주의:

- 높은 Temperature는 근거 없는 생성 가능성을 높인다.
- 낮은 Temperature라도 잘못된 Context가 있으면 오답이 나온다.
- Temperature만 바꾸며 문제를 해결하려 하지 않는다.
- RAG 답변 품질은 Temperature보다 Retrieved Context 품질의 영향이 크다.

---

### [FAQ]

Q. Temperature가 뭐야?

A. LLM 출력의 무작위성과 다양성을 조절하는 Parameter다.

Q. Temperature가 낮으면 뭐가 좋아?

A. 응답이 더 일관적이고 보수적으로 생성되어 코드 생성, RAG, 리뷰에 유리하다.

Q. Temperature가 높으면 뭐가 좋아?

A. 다양한 아이디어와 창의적인 표현을 만들 수 있지만 Hallucination 가능성이 증가한다.

Q. Temperature 0이면 완전히 같은 답이 나와?

A. 항상 그렇지 않다. 모델 구현, 서버 설정, Sampling 방식에 따라 완전한 결정론이 보장되지 않을 수 있다.

Q. RAG 답변에서 Temperature는 낮게 해야 해?

A. 그렇다. 문서 근거에 맞춘 안정적인 답변이 중요하므로 낮게 설정하는 것이 좋다.

---

## 1.3 Top-p

### [개념]

Top-p는 Nucleus Sampling Parameter이다.

Top-p는 다음 Token 후보를 누적 확률 기준으로 제한한다.

Top-p가 낮으면 후보 Token 범위가 좁아지고, Top-p가 높으면 더 많은 후보 Token을 허용한다.

Top-p Flow:

```text
Token Probability Distribution
→ Sort by Probability
→ Select Tokens until Cumulative Probability reaches Top-p
→ Sample Next Token
```

---

### [핵심]

- Top-p는 후보 Token 범위를 확률 질량 기준으로 제한한다.
- 낮은 Top-p는 출력 다양성을 줄인다.
- 높은 Top-p는 출력 다양성을 높인다.
- Temperature와 Top-p는 모두 Sampling에 영향을 준다.
- 두 값을 동시에 크게 조정하면 출력 예측이 어려워진다.
- 실무에서는 Temperature를 우선 조정하고 Top-p는 기본값을 유지하는 경우가 많다.

---

### [실무]

작업별 Top-p 기준:

| 작업          | Top-p 기준       |
| ------------- | ---------------- |
| 코드 생성     | 기본값 또는 낮게 |
| 코드 리뷰     | 기본값 또는 낮게 |
| RAG 답변      | 기본값 또는 낮게 |
| JSON Output   | 기본값 또는 낮게 |
| 요약          | 기본값           |
| 아이디어 발산 | 중간~높게        |
| 창작          | 높게 가능        |

예시:

```json
{
  "temperature": 0.2,
  "top_p": 0.9,
  "max_tokens": 1000
}
```

권장 설정 방식:

```text
일관성 중심 작업
→ Temperature 낮게
→ Top-p 기본값 유지

창의성 중심 작업
→ Temperature 또는 Top-p 중 하나만 조정
→ 결과 품질 테스트

RAG / Code / Review
→ 다양성보다 안정성 우선
```

주의:

- Top-p 지원 여부는 Provider마다 다르다.
- Top-p를 높인다고 품질이 항상 좋아지지 않는다.
- Temperature와 Top-p를 동시에 과도하게 높이지 않는다.
- JSON Output에서는 출력 변동성을 낮추는 것이 좋다.

---

### [FAQ]

Q. Top-p가 뭐야?

A. 다음 Token 후보를 누적 확률 기준으로 제한하는 Sampling Parameter다.

Q. Temperature와 Top-p 차이는?

A. Temperature는 확률 분포의 무작위성을 조절하고, Top-p는 후보 Token 범위를 제한한다.

Q. Top-p는 꼭 설정해야 해?

A. 아니다. 실무에서는 기본값을 유지하고 Temperature만 조정하는 경우도 많다.

Q. 코드 생성에서 Top-p를 높게 잡아도 돼?

A. 권장하지 않는다. 코드 생성은 다양성보다 일관성과 정확성이 중요하다.

Q. RAG 답변에서 Top-p는 어떻게 설정해?

A. 기본값 또는 낮은 값이 적합하며, 관련 문서 기반의 안정적 응답을 우선한다.

---

## 1.4 Max Tokens

### [개념]

Max Tokens는 LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter이다.

Max Tokens는 출력 길이, 비용, Latency, 응답 잘림에 직접 영향을 준다.

Max Tokens는 입력 Token 제한이 아니라 출력 Token 제한이다.

Max Tokens 관계:

```text
Context Window
= Input Tokens
+ Output Tokens

Max Tokens
= Maximum Output Tokens
```

---

### [핵심]

- Max Tokens는 Output Token의 최대 길이를 제한한다.
- 값이 너무 작으면 응답이 중간에 잘린다.
- 값이 너무 크면 비용과 Latency가 증가한다.
- `finish_reason=length`는 출력이 잘렸다는 신호일 수 있다.
- JSON Output은 잘리면 파싱 실패가 발생한다.
- 긴 문서 생성은 Part 분할이 필요할 수 있다.

---

### [실무]

작업별 Max Tokens 기준:

| 작업           | 권장 기준           |
| -------------- | ------------------- |
| 짧은 FAQ 답변  | 작게                |
| 단일 개념 설명 | 작게~중간           |
| 코드 리뷰      | 중간                |
| 코드 생성      | 중간~크게           |
| 긴 문서 요약   | 중간~크게           |
| RAG 답변       | 중간                |
| JSON Output    | Schema 크기 기준    |
| RAG 문서 생성  | 크게 또는 Part 분할 |

Output Reserve 예:

```text
Model Context Window: 32000 tokens
Input Tokens: 20000 tokens
Expected Output: 4000 tokens
Safety Margin: 8000 tokens

Max Tokens
→ 4000 이하로 설정
```

Response 처리 기준:

```text
LLM Response
→ finish_reason 확인
→ length이면 잘림 처리
→ JSON이면 Parse 확인
→ Markdown이면 Required Section 확인
```

주의:

- Max Tokens를 크게 설정해도 Context Window 한도는 넘을 수 없다.
- Output Reserve 없이 입력을 꽉 채우면 응답 생성 공간이 부족하다.
- 잘린 응답을 완성본처럼 사용하지 않는다.
- JSON Output이 잘리면 임의로 닫는 괄호를 추가해 완료 처리하지 않는다.
- 긴 결과물은 문서 Part, 파일 단위, 섹션 단위로 나눈다.

---

### [FAQ]

Q. Max Tokens가 뭐야?

A. LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter다.

Q. Max Tokens는 입력 길이 제한이야?

A. 아니다. Max Tokens는 주로 출력 길이 제한이며 입력은 Context Window와 별도로 관리해야 한다.

Q. Max Tokens가 너무 작으면 어떻게 돼?

A. 응답이 중간에 잘리고 `finish_reason=length`가 발생할 수 있다.

Q. Max Tokens를 크게 하면 항상 좋아?

A. 아니다. 비용과 Latency가 증가하고 불필요하게 긴 응답이 나올 수 있다.

Q. JSON Output에서 Max Tokens가 중요한 이유는?

A. 출력이 잘리면 JSON 구조가 깨져 파싱과 Schema Validation이 실패할 수 있기 때문이다.

---

## 1.5 Stop Sequence

### [개념]

Stop Sequence는 LLM이 특정 문자열을 생성하면 출력을 중단하도록 하는 Parameter이다.

Stop Sequence는 대화 경계, 섹션 종료, 형식 제어, 불필요한 후속 출력을 막는 데 사용한다.

Stop Sequence Flow:

```text
LLM Generates Tokens
→ Stop Sequence Appears
→ Generation Stops
→ Return Response
```

---

### [핵심]

- Stop Sequence는 출력 중단 조건이다.
- 특정 문자열이 생성되면 모델 응답이 종료된다.
- 출력 형식 제어에 사용할 수 있다.
- 잘못 설정하면 필요한 내용도 잘릴 수 있다.
- Provider마다 Stop Sequence 지원 방식이 다를 수 있다.
- Stop Sequence는 Schema Validation을 대체하지 않는다.

---

### [실무]

Stop Sequence 예:

```json
{
  "stop": ["\nUser:", "\nSystem:", "---END---"]
}
```

사용 사례:

| 사용 사례             | Stop Sequence |
| --------------------- | ------------- |
| 대화 재현 방지        | `\nUser:`     |
| System Role 출력 방지 | `\nSystem:`   |
| 섹션 종료             | `---END---`   |
| 템플릿 경계           | `<END>`       |

실무 기준:

```text
Plain Text Output
→ Stop Sequence 사용 가능

Markdown Output
→ 구분자 충돌 주의

JSON Output
→ Stop Sequence 신중히 사용

Code Output
→ 코드 내부 문자열과 충돌 주의
```

주의:

- Markdown 문서에서 `---`를 Stop Sequence로 사용하면 문서가 중간에 잘릴 수 있다.
- JSON Output에서 Stop Sequence가 잘못 작동하면 JSON이 깨진다.
- 코드 생성에서는 문자열 리터럴 내부 Stop Sequence 충돌을 주의한다.
- Stop Sequence는 출력 형식을 보조할 뿐 검증 로직을 대신하지 않는다.

---

### [FAQ]

Q. Stop Sequence가 뭐야?

A. 모델이 특정 문자열을 생성하면 응답 생성을 멈추게 하는 Parameter다.

Q. Stop Sequence는 언제 사용해?

A. 대화 경계, 섹션 종료, 불필요한 추가 출력을 막고 싶을 때 사용한다.

Q. Stop Sequence를 잘못 설정하면 어떻게 돼?

A. 필요한 답변이나 코드가 중간에서 잘릴 수 있다.

Q. Markdown 문서 생성에서 Stop Sequence를 조심해야 하는 이유는?

A. `---` 같은 구분자가 문서 내부에서 자주 사용되어 출력이 예상보다 빨리 멈출 수 있기 때문이다.

Q. Stop Sequence는 JSON Schema 검증을 대체해?

A. 아니다. Stop Sequence는 중단 조건일 뿐이며 JSON Schema Validation은 별도로 필요하다.

---

# 2. Penalty and Determinism

## 2.1 Frequency Penalty

### [개념]

Frequency Penalty는 이미 많이 등장한 Token의 반복 생성을 줄이기 위한 Parameter이다.

Frequency Penalty가 높을수록 같은 표현을 반복할 가능성이 낮아진다.

반복 제어 대상:

- 동일 단어 반복
- 동일 문장 반복
- 동일 구조 반복
- 과도한 문체 반복

---

### [핵심]

- Frequency Penalty는 반복 출력을 줄인다.
- 긴 창작 문장이나 반복되는 답변을 줄이는 데 사용할 수 있다.
- 코드 생성에서는 불필요하게 적용하지 않는 것이 좋다.
- RAG 답변에서는 용어 반복이 필요한 경우가 있으므로 신중하게 사용한다.
- Provider마다 지원 여부와 값 범위가 다르다.

---

### [실무]

사용 기준:

| 작업           | Frequency Penalty       |
| -------------- | ----------------------- |
| 코드 생성      | 보통 사용하지 않음      |
| 코드 리뷰      | 낮게 또는 사용하지 않음 |
| RAG 답변       | 신중히 사용             |
| 마케팅 문구    | 사용 가능               |
| 긴 창작 문서   | 사용 가능               |
| 반복 요약 개선 | 낮게 사용 가능          |

예시:

```json
{
  "frequency_penalty": 0.2
}
```

주의:

- 코드에서는 동일 변수명, 메서드명, 클래스명이 반복되어야 할 수 있다.
- RAG 문서에서는 핵심 키워드 반복이 Retrieval에 유리할 수 있다.
- 반복을 줄이려다 핵심 용어 일관성이 깨질 수 있다.
- 모든 Provider가 Frequency Penalty를 지원하지 않는다.

---

### [FAQ]

Q. Frequency Penalty가 뭐야?

A. 이미 많이 등장한 Token의 반복 생성을 줄이는 Parameter다.

Q. Frequency Penalty는 언제 써?

A. 같은 표현이 과도하게 반복되는 긴 텍스트나 창작 출력에서 사용할 수 있다.

Q. 코드 생성에서 Frequency Penalty를 써도 돼?

A. 권장하지 않는다. 코드에서는 동일 변수명과 구조 반복이 필요할 수 있다.

Q. RAG 문서에서 Frequency Penalty는 조심해야 해?

A. 그렇다. RAG 문서는 핵심 키워드 반복이 검색 품질에 도움이 될 수 있다.

---

## 2.2 Presence Penalty

### [개념]

Presence Penalty는 이미 등장한 주제나 Token이 다시 등장하는 것을 억제하고 새로운 주제 생성을 유도하는 Parameter이다.

Presence Penalty는 출력의 주제 다양성을 높이는 데 사용할 수 있다.

---

### [핵심]

- Presence Penalty는 새로운 주제나 표현을 유도한다.
- 창의적 아이디어 생성에 사용할 수 있다.
- 정확성 중심 작업에는 부적합할 수 있다.
- RAG 답변에서는 문서 근거 밖으로 확장될 위험이 있다.
- 코드 생성에서는 일관성을 깨뜨릴 수 있다.

---

### [실무]

사용 기준:

| 작업         | Presence Penalty          |
| ------------ | ------------------------- |
| RAG 답변     | 사용하지 않거나 매우 낮게 |
| 코드 생성    | 사용하지 않음             |
| 코드 리뷰    | 사용하지 않음             |
| 요약         | 보통 사용하지 않음        |
| 브레인스토밍 | 사용 가능                 |
| 창작         | 사용 가능                 |

예시:

```json
{
  "presence_penalty": 0.3
}
```

주의:

- Presence Penalty는 새로운 내용을 유도하므로 Hallucination 가능성을 높일 수 있다.
- 문서 기반 답변에서는 근거 없는 확장을 만들 수 있다.
- Agent Review 작업에서는 보수적 판단이 필요하므로 사용하지 않는 것이 좋다.
- Provider마다 지원 범위가 다르다.

---

### [FAQ]

Q. Presence Penalty가 뭐야?

A. 이미 등장한 주제를 반복하지 않고 새로운 내용을 생성하도록 유도하는 Parameter다.

Q. Presence Penalty는 언제 써?

A. 아이디어 발산, 창작, 다양한 후보 생성이 필요할 때 사용할 수 있다.

Q. RAG 답변에서 Presence Penalty를 써도 돼?

A. 권장하지 않는다. 문서 근거 밖의 내용을 생성할 가능성이 있다.

Q. Frequency Penalty와 Presence Penalty 차이는?

A. Frequency Penalty는 반복 빈도를 줄이고, Presence Penalty는 새로운 주제 생성을 유도한다.

---

## 2.3 Seed and Determinism

### [개념]

Seed는 모델 출력의 재현성을 높이기 위해 사용하는 Parameter이다.

Determinism은 같은 입력과 같은 설정에서 같은 출력이 생성되는 성질이다.

Seed는 일부 Provider와 모델에서만 지원된다.

---

### [핵심]

- Seed는 재현성을 보조한다.
- Seed가 있어도 완전한 결정론을 보장하지 않을 수 있다.
- Temperature, Top-p, 모델 버전, 서버 구현이 결과에 영향을 준다.
- 테스트 환경에서는 Seed와 낮은 Temperature를 함께 사용할 수 있다.
- Production에서는 완전한 동일 응답을 기대하지 않는다.

---

### [실무]

재현성 관리 기준:

```text
Same Prompt
+ Same Model Version
+ Same Parameter
+ Same Seed
+ Same Context
→ More Reproducible Output
```

테스트 설정 예:

```json
{
  "temperature": 0,
  "seed": 42,
  "max_tokens": 1000
}
```

실무 테스트 기준:

| 대상             | 기준                   |
| ---------------- | ---------------------- |
| Prompt Builder   | Unit Test              |
| Response Parser  | Unit Test              |
| Schema Validator | Deterministic Test     |
| LLM Output       | 유연한 검증            |
| JSON Output      | Schema 기반 검증       |
| Code Output      | Compile/Test 기반 검증 |

주의:

- LLM 출력 텍스트 전체를 exact match로 테스트하지 않는다.
- 모델 업데이트 시 같은 Seed라도 결과가 달라질 수 있다.
- Local LLM과 API LLM의 Determinism 수준이 다를 수 있다.
- Seed가 지원되지 않는 Provider도 많다.

---

### [FAQ]

Q. Seed가 뭐야?

A. 모델 출력의 재현성을 높이기 위해 사용하는 Parameter다.

Q. Seed를 쓰면 항상 같은 답이 나와?

A. 아니다. 모델 구현, 서버 환경, Sampling 설정, 모델 버전에 따라 달라질 수 있다.

Q. LLM 테스트에서 exact match를 쓰면 돼?

A. 권장하지 않는다. JSON Schema, 핵심 필드, 코드 컴파일, 테스트 통과 여부를 검증하는 것이 좋다.

Q. Deterministic Output이 중요한 작업은?

A. JSON Output, 코드 생성, 코드 리뷰, 테스트 케이스 생성, Agent Workflow 검증에서 중요하다.

---

# 3. Output Format Control

## 3.1 Markdown Output

### [개념]

Markdown Output은 LLM 응답을 사람이 읽기 쉬운 문서형 구조로 출력하는 방식이다.

Markdown은 RAG 답변, 코드 리뷰, 문서 요약, 개발 가이드, 최종 응답에 적합하다.

Markdown 구성 요소:

- Heading
- Bullet List
- Table
- Code Block
- Quote
- Checklist
- Separator

---

### [핵심]

- Markdown은 최종 사용자 응답에 적합하다.
- 구조가 명확해 읽기 쉽다.
- 코드 블록과 표를 포함할 수 있다.
- 하지만 자동 파싱에는 JSON보다 불리하다.
- Agent 간 데이터 전달에는 Markdown보다 JSON이 더 안정적일 수 있다.
- RAG 문서 제작에서는 Heading과 FAQ가 Retrieval 품질을 높인다.

---

### [실무]

Markdown Output 예:

```md
# Review Result

## Summary

Service 계층의 Timeout 처리가 필요합니다.

## Issues

- Timeout 설정 누락
- Error Handling 부족
- Usage Logging 누락

## Recommended Fix

WebClient timeout과 Error Mapper를 추가합니다.
```

Markdown 사용 기준:

| 사용처           | 적합성 |
| ---------------- | ------ |
| 최종 사용자 답변 | 높음   |
| 코드 리뷰 결과   | 높음   |
| RAG 문서         | 높음   |
| 보고서           | 높음   |
| Agent 내부 전달  | 중간   |
| 자동 파싱        | 낮음   |
| Tool Arguments   | 낮음   |

주의:

- 자동 처리 대상은 Markdown보다 JSON을 우선한다.
- Markdown 표는 파싱이 까다로울 수 있다.
- Code Block 언어 태그는 명확히 붙인다.
- 불필요한 장문 서론을 피한다.
- RAG 문서에서는 Heading, FAQ, Retrieval Queries를 강화한다.

---

### [FAQ]

Q. Markdown Output은 언제 좋아?

A. 사용자에게 보여줄 문서, 코드 리뷰, 요약, RAG 문서 출력에 적합하다.

Q. Markdown은 Agent 간 전달에 적합해?

A. 가능하지만 자동 파싱이 필요하면 JSON Output이 더 안정적이다.

Q. RAG 문서에서 Markdown이 좋은 이유는?

A. Heading, Section, FAQ, Code Block을 구조적으로 만들 수 있어 Retrieval에 유리하다.

Q. Markdown Output의 단점은?

A. 구조가 느슨해서 프로그램이 안정적으로 파싱하기 어렵다.

---

## 3.2 JSON Output

### [개념]

JSON Output은 LLM 응답을 기계가 파싱 가능한 JSON 구조로 받는 방식이다.

JSON Output은 Agent Workflow, Tool Calling, 자동 처리, 상태 전달, 검증에 적합하다.

JSON Output 사용처:

- Agent Output
- Tool Arguments
- Review Result
- API Design Result
- Classification Result
- Structured Summary
- Validation Report

---

### [핵심]

- JSON Output은 자동 파싱에 유리하다.
- Required Field를 지정할 수 있다.
- Schema Validation과 함께 사용해야 한다.
- 유효한 JSON이어도 내용이 정확하다는 보장은 없다.
- 출력이 잘리면 JSON Parse Error가 발생한다.
- JSON 안에 설명 문장이 섞이면 파싱 실패가 발생할 수 있다.

---

### [실무]

JSON Output 예:

```json
{
  "status": "success",
  "summary": "LLM API integration review completed.",
  "issues": [
    {
      "severity": "high",
      "target": "LlmClient.chat",
      "problem": "Timeout handling is missing.",
      "recommendation": "Add request timeout and error mapping."
    }
  ]
}
```

JSON Output Prompt 예:

```text
Return valid JSON only.
Do not include Markdown.
Do not include explanation outside JSON.

Schema:
{
  "status": "success | needs_fix | failed",
  "summary": "string",
  "issues": []
}
```

검증 Flow:

```text
LLM Response
→ Empty Check
→ Finish Reason Check
→ JSON Parse
→ Schema Validation
→ Required Field Check
→ Content Validation
```

주의:

- JSON Mode가 내용 정확성을 보장하지 않는다.
- Schema가 너무 복잡하면 실패 가능성이 높아진다.
- Optional Field 처리 기준을 정한다.
- 숫자와 문자열 타입 불일치를 검증한다.
- JSON Parse 실패 시 재요청 또는 안전 실패 처리한다.

---

### [FAQ]

Q. JSON Output은 언제 사용해?

A. Agent 간 데이터 전달, Tool Arguments, 자동 파싱, 상태 관리, 검증 결과에 사용한다.

Q. JSON Output은 왜 검증해야 해?

A. LLM이 잘못된 JSON, 누락된 필드, 잘못된 타입, 잘린 응답을 생성할 수 있기 때문이다.

Q. JSON Mode를 쓰면 항상 정확한 JSON이 나와?

A. 유효한 JSON 가능성은 높아지지만 내용 정확성과 Schema 일치를 보장하지는 않는다.

Q. JSON Output에 설명 문장이 섞이면?

A. JSON Parser가 실패할 수 있으므로 JSON만 출력하도록 제한해야 한다.

Q. JSON이 잘리면 어떻게 해?

A. 잘린 JSON을 사용하지 말고 Max Tokens, Context 길이, Schema 복잡도를 조정해 재요청한다.

---

## 3.3 Structured Output

### [개념]

Structured Output은 LLM 응답을 정해진 Schema나 Field 구조에 맞춰 생성하는 방식이다.

Structured Output은 JSON Output보다 넓은 개념이며 Markdown Template, JSON Schema, XML, YAML, Table Format도 포함할 수 있다.

Agent 시스템에서는 Structured Output이 다음 단계 입력으로 사용된다.

Structured Output Flow:

```text
Prompt
→ Model Response
→ Parse Structured Output
→ Validate Schema
→ Use in Next Step
```

---

### [핵심]

- Structured Output은 자동화 Workflow에 중요하다.
- Agent 간 Output Schema를 통일할 수 있다.
- 후속 Tool 또는 Agent가 결과를 안정적으로 사용할 수 있다.
- Schema가 명확할수록 출력 안정성이 높다.
- Schema가 복잡할수록 실패 가능성도 증가한다.
- 출력 검증 로직이 반드시 필요하다.

---

### [실무]

Agent Review Output Schema 예:

```json
{
  "status": "success | needs_fix | failed",
  "summary": "string",
  "criticalIssues": [
    {
      "target": "string",
      "severity": "low | medium | high | critical",
      "problem": "string",
      "fix": "string"
    }
  ],
  "nextAction": "string"
}
```

Structured Output 설계 기준:

| 항목           | 기준                 |
| -------------- | -------------------- |
| Required Field | 반드시 필요한 필드만 |
| Optional Field | 없을 수 있는 데이터  |
| Enum           | 상태값 제한          |
| Array          | 반복 항목            |
| Object         | 중첩 구조            |
| Error Field    | 실패 상태 표현       |
| Version        | Schema 변경 관리     |

권장 구조:

```text
status
summary
data
issues
nextAction
error
```

주의:

- Schema를 과도하게 복잡하게 만들지 않는다.
- Required Field가 많으면 실패 가능성이 높아진다.
- 후속 Agent가 실제로 필요한 필드만 포함한다.
- Schema 변경 시 Consumer Agent도 함께 수정한다.
- Structured Output은 생성 후 반드시 Validation한다.

---

### [FAQ]

Q. Structured Output이 뭐야?

A. LLM 응답을 정해진 Field, Schema, Template 구조에 맞춰 출력하는 방식이다.

Q. Structured Output은 왜 중요해?

A. Agent Workflow와 자동 처리에서 후속 단계가 결과를 안정적으로 파싱하고 사용할 수 있기 때문이다.

Q. Structured Output과 JSON Output 차이는?

A. JSON Output은 Structured Output의 한 종류이고, Structured Output은 Markdown Template이나 Schema 기반 출력까지 포함한다.

Q. Schema는 복잡할수록 좋아?

A. 아니다. 복잡할수록 모델이 필드를 누락하거나 잘못 출력할 가능성이 높아진다.

Q. Structured Output은 검증이 필요해?

A. 반드시 필요하다. 유효한 구조인지, 필수 필드가 있는지, 내용이 맞는지 확인해야 한다.

---

## 3.4 JSON Schema

### [개념]

JSON Schema는 JSON Output의 구조, 타입, 필수 필드, 허용 값을 정의하는 표준적인 Schema 방식이다.

JSON Schema는 LLM Output 검증과 자동 파싱 안정성에 사용된다.

JSON Schema 요소:

- type
- properties
- required
- enum
- array
- object
- additionalProperties
- description

---

### [핵심]

- JSON Schema는 출력 구조를 제한한다.
- Required Field 누락을 검출할 수 있다.
- Enum으로 상태값을 제한할 수 있다.
- 타입 불일치를 검출할 수 있다.
- Schema Validation 실패 시 재요청하거나 안전 실패 처리한다.
- JSON Schema는 내용의 사실 정확성을 보장하지 않는다.

---

### [실무]

JSON Schema 예:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "needs_fix", "failed"]
    },
    "summary": {
      "type": "string"
    },
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "severity": {
            "type": "string",
            "enum": ["low", "medium", "high", "critical"]
          },
          "problem": {
            "type": "string"
          },
          "fix": {
            "type": "string"
          }
        },
        "required": ["severity", "problem", "fix"]
      }
    }
  },
  "required": ["status", "summary", "issues"]
}
```

Validation Flow:

```text
LLM JSON Output
→ JSON Parse
→ JSON Schema Validation
→ Required Field Check
→ Enum Check
→ Type Check
→ Content Validation
```

재시도 기준:

```text
Invalid JSON
→ Retry with shorter prompt

Schema Validation Failed
→ Retry with clearer schema

Required Field Missing
→ Retry with explicit required fields

Content Invalid
→ Review or Tool Verification
```

주의:

- Schema가 너무 깊으면 실패 가능성이 증가한다.
- Required Field를 과도하게 늘리지 않는다.
- Optional Field의 기본값 처리 기준을 정한다.
- additionalProperties 허용 여부를 정한다.
- Schema Version을 관리한다.

---

### [FAQ]

Q. JSON Schema가 뭐야?

A. JSON Output의 구조, 타입, 필수 필드, 허용 값을 정의하는 Schema다.

Q. JSON Schema는 왜 필요해?

A. LLM Output이 파싱 가능한 구조인지 자동으로 검증하기 위해 필요하다.

Q. JSON Schema를 쓰면 내용도 정확해져?

A. 아니다. 구조 검증은 가능하지만 내용의 사실 정확성은 별도 검증이 필요하다.

Q. Required Field는 많이 넣을수록 좋아?

A. 아니다. 필수 필드가 많으면 출력 실패나 누락 가능성이 높아질 수 있다.

Q. Schema Validation 실패 시 어떻게 해?

A. 오류 유형에 따라 재요청, Schema 단순화, Prompt 수정, 안전 실패 처리를 한다.

---

# 4. Output Validation

## 4.1 Empty Response Check

### [개념]

Empty Response Check는 LLM API 응답이 비어 있거나 사용할 수 없는 상태인지 확인하는 검증이다.

LLM API는 정상 HTTP Status를 반환해도 Content가 비어 있을 수 있다.

Empty Response 유형:

- Empty Choices
- Missing Message
- Empty Content
- Null Content
- Tool Calls Without Final Answer
- Blocked Response
- Truncated Response

---

### [핵심]

- HTTP 200이어도 LLM Output이 유효하다는 보장은 없다.
- `choices`가 비어 있을 수 있다.
- `message.content`가 비어 있을 수 있다.
- Tool Calling 응답은 content 없이 tool_calls만 있을 수 있다.
- Empty Response는 재요청 또는 안전 실패 처리가 필요하다.
- Empty Response는 로그에 남겨야 한다.

---

### [실무]

Empty Response Check Flow:

```text
Response Body
→ choices exists?
→ message exists?
→ content or tool_calls exists?
→ finish_reason valid?
→ output usable?
```

Python 예:

```python
def validate_response(data: dict) -> str:
    choices = data.get("choices") or []
    if not choices:
        raise ValueError("Empty choices")

    message = choices[0].get("message") or {}
    content = message.get("content")
    tool_calls = message.get("tool_calls")

    if not content and not tool_calls:
        raise ValueError("Empty content and no tool calls")

    return content or ""
```

처리 기준:

| 상황             | 처리                  |
| ---------------- | --------------------- |
| Empty Choices    | 실패 처리             |
| Empty Content    | 재요청 또는 실패      |
| Tool Calls 존재  | Tool 실행 단계로 이동 |
| Content Filter   | 안전 실패 처리        |
| Truncated Output | 재요청 또는 작업 분할 |

주의:

- Empty Content를 정상 답변으로 사용자에게 반환하지 않는다.
- Tool Calling 응답은 Empty Content일 수 있으므로 분기 처리한다.
- Empty Response가 반복되면 Prompt, Max Tokens, Provider 상태를 확인한다.
- Error Body에 Secret이 포함되지 않도록 로그를 Redaction한다.

---

### [FAQ]

Q. Empty Response Check가 뭐야?

A. LLM 응답이 비어 있거나 사용할 수 없는 상태인지 확인하는 검증이다.

Q. HTTP 200이면 응답을 믿어도 돼?

A. 아니다. HTTP 200이어도 content가 비어 있거나 finish_reason이 비정상일 수 있다.

Q. Content가 없으면 무조건 실패야?

A. Tool Calling 응답은 content 대신 tool_calls가 있을 수 있으므로 분기 처리해야 한다.

Q. Empty Response가 반복되면 뭘 확인해?

A. Prompt, Max Tokens, Provider 상태, Safety Filter, Tool Calling 설정을 확인한다.

---

## 4.2 Finish Reason Check

### [개념]

Finish Reason Check는 LLM 응답이 어떤 이유로 종료되었는지 확인하는 검증이다.

Finish Reason은 응답을 그대로 사용해도 되는지 판단하는 핵심 정보이다.

대표 Finish Reason:

- stop
- length
- tool_calls
- content_filter
- null
- error

---

### [핵심]

- `stop`은 정상 종료를 의미한다.
- `length`는 출력이 잘렸을 가능성을 의미한다.
- `tool_calls`는 Tool 실행이 필요함을 의미한다.
- `content_filter`는 안전 정책으로 응답이 차단된 상태일 수 있다.
- Streaming 중에는 중간 Chunk의 finish_reason이 null일 수 있다.
- Provider마다 Finish Reason 값이 다를 수 있다.

---

### [실무]

Finish Reason 처리 Flow:

```text
finish_reason
→ stop: 정상 처리
→ length: 잘림 처리
→ tool_calls: Tool 실행
→ content_filter: 안전 실패
→ unknown: 보수적 실패
```

처리 예:

```python
def handle_finish_reason(reason: str | None) -> str:
    if reason == "stop":
        return "ok"

    if reason == "length":
        raise ValueError("LLM output truncated")

    if reason == "tool_calls":
        return "tool_required"

    if reason == "content_filter":
        raise ValueError("LLM output blocked")

    raise ValueError(f"Unknown finish reason: {reason}")
```

주의:

- `finish_reason=length`인 응답을 완성 결과로 사용하지 않는다.
- JSON Output에서 `length`가 발생하면 파싱 실패 가능성이 높다.
- Tool Calling 응답은 Final Answer가 아니라 중간 상태일 수 있다.
- Streaming은 최종 Chunk 기준으로 Finish Reason을 판단한다.
- Unknown Finish Reason은 안전하게 실패 처리한다.

---

### [FAQ]

Q. Finish Reason Check가 뭐야?

A. LLM 응답 종료 사유를 확인해 응답 사용 가능 여부를 판단하는 검증이다.

Q. `finish_reason=stop`은 뭐야?

A. 모델이 정상적으로 응답 생성을 종료했다는 의미다.

Q. `finish_reason=length`는 뭐야?

A. Max Tokens 또는 Context 제한 때문에 응답이 중간에 잘렸을 가능성이 있다는 의미다.

Q. `finish_reason=tool_calls`는 뭐야?

A. 모델이 최종 답변 대신 Tool 호출을 요청했다는 의미다.

Q. Finish Reason이 unknown이면?

A. Provider 문서를 확인하고, 기본적으로 보수적 실패 처리하는 것이 안전하다.

---

## 4.3 Schema Validation

### [개념]

Schema Validation은 LLM Output이 사전에 정의한 구조, 타입, 필수 필드, 허용 값에 맞는지 검증하는 과정이다.

Schema Validation은 JSON Output, Agent Output, Tool Arguments, Review Report에 필수적이다.

---

### [핵심]

- LLM Output은 항상 검증해야 한다.
- JSON Parse 성공이 Schema Validation 성공을 의미하지 않는다.
- Required Field 누락을 확인해야 한다.
- 타입 불일치를 확인해야 한다.
- Enum 값 범위를 확인해야 한다.
- Tool Arguments는 실행 전에 반드시 검증해야 한다.
- Schema Validation 실패 시 재요청 또는 안전 실패 처리한다.

---

### [실무]

Schema Validation Flow:

```text
Raw LLM Output
→ Parse JSON
→ Validate Schema
→ Check Required Fields
→ Check Enum Values
→ Check Business Rules
→ Execute Next Step
```

검증 예:

```text
Required:
- status
- summary
- issues

Enum:
status = success | needs_fix | failed

Business Rule:
if status = needs_fix
→ issues must not be empty
```

Tool Arguments 검증 예:

```json
{
  "toolName": "search_documents",
  "arguments": {
    "query": "LLM API Timeout 처리 방법",
    "topK": 5
  }
}
```

검증 기준:

| 필드        | 검증             |
| ----------- | ---------------- |
| query       | 빈 문자열 금지   |
| topK        | 1 이상 20 이하   |
| filters     | 허용된 값만      |
| destructive | 사용자 승인 필요 |
| secret      | 포함 금지        |

주의:

- 유효한 JSON이어도 업무적으로 잘못된 값일 수 있다.
- Tool Arguments 검증 없이 실행하면 보안 사고가 발생할 수 있다.
- 파일 삭제, 결제, 배포 같은 위험 작업은 추가 승인 절차가 필요하다.
- Validation 실패 로그에는 Secret을 남기지 않는다.
- 재요청은 Max Retry를 제한한다.

---

### [FAQ]

Q. Schema Validation이 뭐야?

A. LLM Output이 정해진 구조, 타입, 필수 필드, 허용 값에 맞는지 확인하는 검증이다.

Q. JSON Parse가 성공하면 충분해?

A. 아니다. 구조는 JSON이어도 필수 필드 누락이나 타입 오류가 있을 수 있다.

Q. Tool Arguments도 Schema Validation이 필요해?

A. 반드시 필요하다. 잘못된 인자로 Tool을 실행하면 오류나 위험 작업이 발생할 수 있다.

Q. Schema Validation 실패 시 어떻게 해?

A. 재요청, Schema 단순화, Prompt 수정, 안전 실패 처리 중 하나를 선택한다.

Q. Business Rule Validation도 필요해?

A. 필요하다. Schema가 맞아도 업무 규칙상 잘못된 결과일 수 있기 때문이다.

---

## 4.4 Content Validation

### [개념]

Content Validation은 LLM Output의 구조뿐 아니라 내용이 실제 요구사항, 문서 근거, 도메인 규칙, 보안 기준과 맞는지 확인하는 검증이다.

Content Validation은 Hallucination, 근거 없는 답변, 위험한 Tool 실행, 잘못된 코드 생성을 줄인다.

---

### [핵심]

- Schema가 맞아도 내용이 틀릴 수 있다.
- RAG 답변은 Retrieved Context와 일치해야 한다.
- 코드 생성 결과는 컴파일, 테스트, 보안 검토가 필요하다.
- API 설계 결과는 프로젝트 규칙과 충돌하지 않아야 한다.
- Agent Output은 다음 Agent가 실행 가능한 수준이어야 한다.
- 내용 검증은 Review Agent 또는 Validator가 수행할 수 있다.

---

### [실무]

Content Validation Flow:

```text
LLM Output
→ Match User Requirement
→ Check Retrieved Context
→ Check Domain Rules
→ Check Security Rules
→ Check Completeness
→ Approve or Reject
```

검증 기준:

| 출력 유형   | 검증 기준                         |
| ----------- | --------------------------------- |
| RAG 답변    | 문서 근거와 일치                  |
| 코드 생성   | 컴파일 가능, Convention 준수      |
| 코드 리뷰   | 실제 코드 근거 필요               |
| JSON Output | Schema + Business Rule            |
| API 설계    | REST Convention, Error Response   |
| Agent Plan  | 실행 가능성, Step 누락 여부       |
| Tool Call   | 인자 안전성, 권한, 승인 필요 여부 |

RAG Content Validation 예:

```text
Answer Claim:
"Chat Completion은 messages 배열을 사용한다."

Retrieved Context:
"Chat Completion은 messages 배열을 기반으로 응답 생성"

Validation:
Supported
```

주의:

- LLM의 그럴듯한 설명을 근거 없이 통과시키지 않는다.
- Retrieved Context에 없는 내용은 Missing Information으로 처리한다.
- 코드 리뷰는 실제 코드 위치와 문제를 연결해야 한다.
- 보안 관련 출력은 Conservative하게 검증한다.
- Review Agent의 검증 결과도 필요하면 재검증한다.

---

### [FAQ]

Q. Content Validation이 뭐야?

A. LLM Output의 내용이 요구사항, 문서 근거, 도메인 규칙과 맞는지 확인하는 검증이다.

Q. Schema Validation만 하면 충분해?

A. 아니다. 구조가 맞아도 내용이 틀릴 수 있으므로 Content Validation이 필요하다.

Q. RAG 답변은 어떻게 검증해?

A. 답변의 핵심 주장과 Retrieved Context가 일치하는지 확인한다.

Q. 코드 생성 결과는 어떻게 검증해?

A. 컴파일, 테스트, Convention, 보안 기준, 요구사항 충족 여부를 확인한다.

Q. Content Validation은 누가 수행해?

A. Validator 코드, Rule Engine, Review Agent, 테스트 도구가 수행할 수 있다.

---

# 5. Output Control in RAG

## 5.1 Grounded Answer Control

### [개념]

Grounded Answer Control은 RAG 답변이 Retrieved Context에 근거하도록 제한하는 출력 제어 방식이다.

RAG에서 LLM은 일반 지식을 자유롭게 생성하는 것이 아니라 검색된 문서를 기반으로 답변해야 한다.

Grounded Answer Flow:

```text
User Query
→ Retrieve Context
→ Build Grounded Prompt
→ Generate Answer
→ Validate Against Context
→ Return Answer or Missing Information
```

---

### [핵심]

- RAG 답변은 Retrieved Context를 우선한다.
- 문서에 없는 내용은 추측하지 않는다.
- 일반 지식과 문서 근거를 구분한다.
- Missing Information Rule이 필요하다.
- 낮은 Temperature를 사용한다.
- 답변 후 근거 일치 여부를 검증한다.

---

### [실무]

Grounded Prompt 예:

```text
You are a RAG-based assistant.

Rules:
- Answer only using Retrieved Context.
- Do not guess.
- If the answer is not found, say "문서에서 확인되지 않습니다."
- Keep the answer concise.

Retrieved Context:
{context}

User Question:
{question}
```

출력 제어 기준:

| 항목              | 기준           |
| ----------------- | -------------- |
| Temperature       | 낮게           |
| Retrieved Context | 관련 Chunk만   |
| Missing Rule      | 필수           |
| Citation          | 가능하면 포함  |
| Validation        | Context Match  |
| General Knowledge | 제한 또는 명시 |
| Output Length     | 질문 범위 기준 |

주의:

- RAG를 사용해도 Hallucination은 발생할 수 있다.
- 검색 결과가 틀리면 답변도 틀릴 수 있다.
- Context가 부족하면 추가 검색 또는 Missing Information 처리한다.
- 문서 근거와 모델 추론을 혼합하지 않는다.
- 최신 정보가 필요한 질문은 외부 검색 Tool이 필요할 수 있다.

---

### [FAQ]

Q. Grounded Answer Control이 뭐야?

A. RAG 답변이 검색된 문서 Context에 근거하도록 제한하는 출력 제어 방식이다.

Q. RAG 답변에서 가장 중요한 규칙은?

A. 문서에 없는 내용은 추측하지 않고 확인되지 않는다고 답하는 것이다.

Q. RAG에서 낮은 Temperature를 쓰는 이유는?

A. 문서 근거에 맞춘 안정적인 답변을 생성하기 위해서다.

Q. Retrieved Context가 부족하면?

A. 추가 검색을 하거나 문서에서 확인되지 않는다고 답해야 한다.

Q. RAG 답변은 일반 지식을 섞어도 돼?

A. 문서 기반 답변이 목적이라면 일반 지식은 제한하거나 명확히 구분해야 한다.

---

## 5.2 Missing Information Rule

### [개념]

Missing Information Rule은 Retrieved Context에 답변 근거가 없을 때 LLM이 추측하지 않고 정보 부족을 명시하도록 하는 규칙이다.

Missing Information Rule은 RAG Hallucination을 줄이는 핵심 출력 제어 규칙이다.

---

### [핵심]

- 문서에 없는 내용은 없다고 답한다.
- 불확실한 내용은 확정적으로 말하지 않는다.
- 추가 검색이 필요하면 명시한다.
- Missing Response는 짧고 명확해야 한다.
- Agent Workflow에서는 Missing 상태를 구조화할 수 있다.

---

### [실무]

Missing Information Prompt 예:

```text
If the retrieved context does not contain the answer, respond:
"문서에서 확인되지 않습니다."

Do not use outside knowledge.
Do not infer missing facts.
```

Markdown 답변 예:

```text
문서에서 확인되지 않습니다.

현재 Retrieved Context에는 해당 질문에 대한 직접적인 근거가 없습니다.
```

JSON Output 예:

```json
{
  "status": "missing_information",
  "answer": null,
  "reason": "The retrieved context does not contain enough information.",
  "requiredContext": ["LLM API provider-specific response format"]
}
```

사용 기준:

| 상황           | 처리                         |
| -------------- | ---------------------------- |
| 근거 없음      | Missing Information          |
| 근거 일부 있음 | 제한적 답변 + 부족 정보 명시 |
| 근거 충돌      | 충돌 정보 명시               |
| 최신 정보 필요 | Web Search 또는 Tool 필요    |
| 코드 근거 부족 | 파일 또는 코드 추가 요청     |

주의:

- Missing Information을 실패로만 보지 않는다.
- 근거 없는 답변보다 Missing Information이 더 안전하다.
- 사용자에게 없는 정보를 있는 것처럼 말하지 않는다.
- RAG 문서 제작 시 Retrieval Queries로 누락 가능성을 줄인다.
- Agent는 Missing 상태를 다음 검색 또는 사용자 확인 단계로 연결할 수 있다.

---

### [FAQ]

Q. Missing Information Rule이 뭐야?

A. 문서에 답변 근거가 없을 때 추측하지 않고 정보 부족을 명시하는 규칙이다.

Q. 왜 Missing Information Rule이 필요해?

A. RAG 답변에서 Hallucination을 줄이고 근거 없는 답변을 방지하기 위해 필요하다.

Q. 문서에 일부 정보만 있으면 어떻게 해?

A. 확인 가능한 범위만 답하고 부족한 정보를 명시한다.

Q. Missing Information은 실패야?

A. 아니다. 근거 없는 답변을 막는 안전한 응답이다.

Q. Agent에서는 Missing Information을 어떻게 처리해?

A. `missing_information` 상태로 구조화하고 추가 검색, Tool 호출, 사용자 확인 단계로 넘길 수 있다.

---

# 6. Output Control in Agent Workflow

## 6.1 Agent Output Schema

### [개념]

Agent Output Schema는 Agent가 다음 Agent나 Tool이 사용할 수 있도록 결과를 정해진 구조로 출력하는 규칙이다.

Agent Workflow에서는 자연어 답변보다 구조화된 출력이 안정적이다.

Agent Output Schema 구성:

- status
- summary
- data
- issues
- nextAction
- toolRequest
- error
- confidence
- references

---

### [핵심]

- Agent Output은 다음 단계가 파싱 가능해야 한다.
- `status` 필드는 Workflow 분기에 중요하다.
- `summary`는 사람이 읽는 요약이다.
- `data`는 후속 처리용 구조화 데이터이다.
- `issues`는 Review Agent 결과에 적합하다.
- `error`는 실패 원인 전달에 필요하다.
- Schema Validation 실패 시 다음 Agent로 넘기지 않는다.

---

### [실무]

Agent Output Schema 예:

```json
{
  "status": "success",
  "summary": "Backend API design completed.",
  "data": {
    "endpoints": [
      {
        "method": "GET",
        "path": "/api/posts",
        "description": "게시글 목록 조회"
      }
    ]
  },
  "issues": [],
  "nextAction": "Generate controller code",
  "error": null
}
```

상태값 기준:

| status                      | 의미             |
| --------------------------- | ---------------- |
| success                     | 정상 완료        |
| needs_fix                   | 수정 필요        |
| failed                      | 실패             |
| missing_information         | 정보 부족        |
| tool_required               | Tool 호출 필요   |
| human_confirmation_required | 사용자 승인 필요 |

Agent Output Flow:

```text
Agent Task
→ Generate Structured Output
→ Schema Validation
→ Content Validation
→ Route to Next Agent
```

주의:

- Agent마다 상태값을 다르게 만들지 않는다.
- 다음 Agent가 사용하지 않는 필드를 과도하게 넣지 않는다.
- 실패 상태에도 error와 nextAction을 포함한다.
- 위험 작업은 human_confirmation_required로 분기한다.
- Agent Output은 로그와 디버깅에 사용할 수 있도록 명확해야 한다.

---

### [FAQ]

Q. Agent Output Schema가 뭐야?

A. Agent가 결과를 다음 Agent나 Tool이 사용할 수 있도록 정해진 구조로 출력하는 규칙이다.

Q. Agent Output에 status가 왜 필요해?

A. 성공, 실패, 수정 필요, 정보 부족, Tool 필요 같은 Workflow 분기를 위해 필요하다.

Q. Agent Output은 Markdown이 좋아 JSON이 좋아?

A. 자동 처리가 필요하면 JSON이 좋고, 사용자 최종 응답은 Markdown이 좋다.

Q. Schema Validation에 실패하면?

A. 다음 Agent로 넘기지 말고 재요청, 수정, 안전 실패 처리를 해야 한다.

Q. 위험 작업은 어떤 status로 처리해?

A. `human_confirmation_required`로 분기해 사용자 승인을 받아야 한다.

---

## 6.2 Tool Argument Control

### [개념]

Tool Argument Control은 LLM이 생성한 Tool Calling 인자를 검증하고 제한하는 출력 제어 방식이다.

Tool Arguments는 외부 함수, API, 파일, DB, 검색, 배포 명령에 사용될 수 있으므로 실행 전 검증이 필수이다.

---

### [핵심]

- Tool Arguments는 그대로 신뢰하면 안 된다.
- Schema Validation을 먼저 수행한다.
- Business Rule Validation을 추가한다.
- 위험 작업은 사용자 승인이 필요하다.
- 허용된 Tool과 허용된 Argument만 실행한다.
- Secret, 파일 경로, 권한, 범위 제한을 확인한다.

---

### [실무]

Tool Argument 예:

```json
{
  "tool": "search_documents",
  "arguments": {
    "query": "LLM API Timeout 처리 방법",
    "topK": 5,
    "domain": "LLM_Core_API_Integration"
  }
}
```

검증 기준:

| 항목        | 검증                 |
| ----------- | -------------------- |
| tool        | 허용된 Tool인지 확인 |
| query       | 빈 문자열 금지       |
| topK        | 범위 제한            |
| filePath    | 허용 경로 확인       |
| operation   | 위험 작업 여부 확인  |
| secret      | 포함 금지            |
| destructive | 승인 필요            |
| externalApi | Rate Limit 확인      |

Tool Argument Control Flow:

```text
LLM Tool Call
→ Parse Arguments
→ Schema Validation
→ Permission Check
→ Risk Check
→ Execute Tool
→ Return Tool Result
```

위험 작업 예:

```text
File Delete
Database Write
Payment
Deployment
Email Send
Calendar Update
Production Config Change
```

주의:

- LLM이 생성한 파일 경로를 그대로 사용하지 않는다.
- 삭제, 결제, 배포, 전송 작업은 승인 없이 실행하지 않는다.
- Tool Arguments에 API Key가 포함되면 즉시 차단한다.
- Tool 실패 결과를 명확히 LLM에게 전달한다.
- Tool Result도 다시 검증한다.

---

### [FAQ]

Q. Tool Argument Control이 뭐야?

A. LLM이 생성한 Tool 실행 인자를 검증하고 안전하게 제한하는 출력 제어 방식이다.

Q. Tool Arguments를 그대로 실행하면 안 되는 이유는?

A. 잘못된 인자나 위험 작업이 실행되어 파일 삭제, 비용 발생, 보안 사고가 생길 수 있기 때문이다.

Q. Tool Arguments는 어떻게 검증해?

A. Schema Validation, 허용 Tool 확인, 권한 확인, 위험 작업 여부, 값 범위를 검증한다.

Q. 위험 작업은 어떻게 처리해?

A. 사용자 승인 상태로 분기하고 승인 전에는 실행하지 않는다.

Q. Tool Result도 검증해야 해?

A. 그렇다. Tool 실패, 빈 결과, 잘못된 타입, Secret 포함 여부를 확인해야 한다.

---

# 7. Common Mistakes

## 7.1 Parameter and Output Control Common Mistakes

### [개념]

Parameter and Output Control Common Mistakes는 LLM 출력 제어를 잘못 설계해 발생하는 품질, 비용, 안정성, 보안 문제이다.

---

### [핵심]

자주 발생하는 실수:

- Temperature를 작업 목적과 무관하게 높게 설정
- RAG 답변에 높은 Temperature 사용
- Max Tokens를 너무 작게 설정
- Output Reserve 없이 Context를 꽉 채움
- `finish_reason=length`를 무시
- Stop Sequence를 잘못 설정해 출력이 잘림
- JSON Output을 검증하지 않음
- JSON Mode만 믿고 Schema Validation을 생략
- Markdown Output을 자동 파싱에 사용
- Agent Output Schema를 통일하지 않음
- Tool Arguments를 검증 없이 실행
- 위험 Tool을 사용자 승인 없이 실행
- Frequency Penalty로 핵심 용어 일관성 훼손
- Presence Penalty로 근거 없는 주제 확장
- Seed를 완전한 결정론으로 오해
- Provider별 Parameter 지원 차이 무시

---

### [실무]

문제 진단 Flow:

```text
Output Problem
→ Check Task Type
→ Check Temperature
→ Check Top-p
→ Check Max Tokens
→ Check Finish Reason
→ Check Output Format
→ Check Schema Validation
→ Check Content Validation
```

대응 기준:

| 문제              | 해결                                    |
| ----------------- | --------------------------------------- |
| 답변이 흔들림     | Temperature 낮춤                        |
| 답변이 잘림       | Max Tokens 조정, 작업 분할              |
| JSON 파싱 실패    | JSON Mode, Schema 단순화                |
| RAG Hallucination | Grounded Prompt, Missing Rule           |
| Tool 실행 오류    | Argument Validation                     |
| Agent 분기 실패   | status Enum 통일                        |
| 반복 표현 많음    | Prompt 수정 또는 Frequency Penalty 검토 |
| 창의성 부족       | Temperature 또는 Top-p 조정             |
| 비용 증가         | Max Tokens 제한, Context 축소           |

검수 Checklist:

```text
작업 목적에 맞는 Temperature인가?
Top-p를 과도하게 조정하지 않았는가?
Max Tokens와 Output Reserve가 충분한가?
Stop Sequence가 출력 본문과 충돌하지 않는가?
JSON Output은 Parse와 Schema Validation을 거치는가?
Markdown Output을 자동 파싱에 사용하지 않는가?
RAG 답변은 Retrieved Context에 근거하는가?
Missing Information Rule이 있는가?
Agent Output Schema가 통일되어 있는가?
Tool Arguments를 실행 전 검증하는가?
위험 Tool은 사용자 승인 절차가 있는가?
```

---

### [FAQ]

Q. Parameter 설정에서 가장 흔한 실수는?

A. 작업 목적과 무관하게 Temperature를 높게 설정하거나 Max Tokens를 너무 작게 잡는 것이다.

Q. RAG 답변에서 흔한 실수는?

A. 높은 Temperature를 사용하거나 문서에 없는 내용을 추측하게 두는 것이다.

Q. JSON Output에서 흔한 실수는?

A. JSON Mode만 믿고 JSON Parse, Schema Validation, Required Field Check를 생략하는 것이다.

Q. Agent Output에서 흔한 실수는?

A. Agent마다 Output Schema와 status 값을 다르게 만들어 Workflow 분기가 깨지는 것이다.

Q. Tool Calling에서 가장 위험한 실수는?

A. LLM이 생성한 Tool Arguments를 검증 없이 실행하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. LLM Parameter가 뭐야?
A. LLM 출력의 다양성, 길이, 형식, 중단 조건 등을 제어하는 설정값이다.

Q. Temperature가 뭐야?
A. LLM 출력의 무작위성과 다양성을 조절하는 Parameter다.

Q. Temperature는 어떻게 설정해?
A. 코드 생성, 코드 리뷰, RAG 답변, JSON Output은 낮게 설정하고 창의적 작업은 중간 이상을 사용할 수 있다.

Q. RAG 답변에서 Temperature를 낮게 설정하는 이유는?
A. 문서 근거에 맞춘 안정적인 답변을 생성해야 하기 때문이다.

Q. Temperature 0이면 항상 같은 답이 나와?
A. 아니다. 모델 구현, 서버 설정, Sampling 방식, 모델 버전에 따라 완전한 결정론이 보장되지 않을 수 있다.

Q. Top-p가 뭐야?
A. 다음 Token 후보를 누적 확률 기준으로 제한하는 Sampling Parameter다.

Q. Temperature와 Top-p 차이는?
A. Temperature는 확률 분포의 무작위성을 조절하고 Top-p는 후보 Token 범위를 제한한다.

Q. Top-p는 꼭 설정해야 해?
A. 아니다. 실무에서는 기본값을 유지하고 Temperature를 우선 조정하는 경우가 많다.

Q. Max Tokens가 뭐야?
A. LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter다.

Q. Max Tokens는 입력 길이 제한이야?
A. 아니다. Max Tokens는 주로 출력 길이 제한이며 입력은 Context Window로 관리한다.

Q. `finish_reason=length`는 뭐야?
A. Max Tokens 또는 Context 제한으로 출력이 중간에 잘렸을 가능성이 있다는 의미다.

Q. Stop Sequence가 뭐야?
A. 모델이 특정 문자열을 생성하면 응답 생성을 멈추게 하는 Parameter다.

Q. Stop Sequence를 잘못 설정하면?
A. 필요한 답변, 코드, JSON, Markdown 문서가 중간에서 잘릴 수 있다.

Q. Frequency Penalty가 뭐야?
A. 이미 많이 등장한 Token의 반복 생성을 줄이는 Parameter다.

Q. Presence Penalty가 뭐야?
A. 이미 등장한 주제를 반복하지 않고 새로운 내용을 생성하도록 유도하는 Parameter다.

Q. Seed가 뭐야?
A. 모델 출력의 재현성을 높이기 위해 사용하는 Parameter다.

Q. Seed를 쓰면 완전히 같은 답이 나와?
A. 아니다. Seed는 재현성을 보조하지만 완전한 결정론을 보장하지 않는다.

Q. Markdown Output은 언제 사용해?
A. 최종 사용자 답변, 코드 리뷰, 문서 요약, RAG 문서 생성에 적합하다.

Q. JSON Output은 언제 사용해?
A. Agent 간 데이터 전달, Tool Arguments, 자동 파싱, 상태 관리, 검증 결과에 사용한다.

Q. Structured Output이 뭐야?
A. LLM 응답을 정해진 Field, Schema, Template 구조에 맞춰 출력하는 방식이다.

Q. JSON Schema가 뭐야?
A. JSON Output의 구조, 타입, 필수 필드, 허용 값을 정의하는 Schema다.

Q. JSON Schema를 쓰면 내용도 정확해져?
A. 아니다. 구조 검증은 가능하지만 내용의 사실 정확성은 별도 검증이 필요하다.

Q. Empty Response Check가 뭐야?
A. LLM 응답이 비어 있거나 사용할 수 없는 상태인지 확인하는 검증이다.

Q. Finish Reason Check가 뭐야?
A. LLM 응답 종료 사유를 확인해 응답 사용 가능 여부를 판단하는 검증이다.

Q. Schema Validation이 뭐야?
A. LLM Output이 정해진 구조, 타입, 필수 필드, 허용 값에 맞는지 확인하는 검증이다.

Q. Content Validation이 뭐야?
A. LLM Output의 내용이 요구사항, 문서 근거, 도메인 규칙과 맞는지 확인하는 검증이다.

Q. Grounded Answer Control이 뭐야?
A. RAG 답변이 검색된 문서 Context에 근거하도록 제한하는 출력 제어 방식이다.

Q. Missing Information Rule이 뭐야?
A. 문서에 답변 근거가 없을 때 추측하지 않고 정보 부족을 명시하는 규칙이다.

Q. Agent Output Schema가 뭐야?
A. Agent가 결과를 다음 Agent나 Tool이 사용할 수 있도록 정해진 구조로 출력하는 규칙이다.

Q. Tool Argument Control이 뭐야?
A. LLM이 생성한 Tool 실행 인자를 검증하고 안전하게 제한하는 출력 제어 방식이다.

Q. Tool Arguments를 그대로 실행하면 안 되는 이유는?
A. 잘못된 인자나 위험 작업이 실행되어 파일 삭제, 비용 발생, 보안 사고가 생길 수 있기 때문이다.

Q. Parameter 조정만으로 Hallucination을 막을 수 있어?
A. 아니다. RAG Context, Prompt, Missing Rule, Response Validation, Tool Result 검증이 함께 필요하다.

Q. Agent Workflow에서 Output Control이 중요한 이유는?
A. 다음 Agent가 결과를 안정적으로 파싱하고 안전하게 실행할 수 있어야 하기 때문이다.

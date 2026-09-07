# Fine-Tuning Domain Rules

---

# 1. Domain Purpose

## 1.1 Fine-Tuning 문서 목적

### [개념]

Fine-Tuning Domain 문서는 AI Agent / AI/ML Agent / PM Agent / Backend Agent / Review Agent가 LLM Fine-Tuning 기반 시스템을 설계, 구현, 검토, 평가할 때 참조하는 RAG 제작 규칙 문서이다.

Fine-Tuning은 기존 Foundation Model 또는 Open-Weight Model에 특정 목적의 데이터셋을 추가 학습시켜, 모델의 응답 스타일, 작업 형식, 도메인 지식 적용 방식, 출력 패턴을 조정하는 기법이다.

Fine-Tuning은 RAG를 대체하는 기술이 아니다.

Fine-Tuning은 모델의 행동 패턴을 조정하는 데 강하고, RAG는 외부 지식 검색과 최신 정보 반영에 강하다.

---

### [핵심]

- Fine-Tuning = 모델 가중치 조정
- RAG = 외부 지식 검색
- Prompt Engineering = 입력 지시 최적화
- Fine-Tuning은 반복 작업 패턴에 적합
- Fine-Tuning은 출력 형식 고정에 적합
- Fine-Tuning은 도메인 스타일 학습에 적합
- Fine-Tuning은 최신 지식 저장소로 사용하면 안 됨
- 학습 데이터 품질이 모델 품질을 결정
- Evaluation 없이 Fine-Tuning 금지
- Overfitting 주의
- Hallucination 감소 목적만으로 Fine-Tuning을 남용하지 않음
- RAG / Prompt / Fine-Tuning 선택 기준 필요

---

### [실무]

2026 실무 기준 Fine-Tuning 문서는 다음 목적을 우선한다.

- Fine-Tuning 적용 여부 판단
- RAG / Prompt / Fine-Tuning 선택 기준 제공
- 학습 데이터셋 설계 기준 제공
- Instruction Dataset 작성 기준 제공
- Input / Output Format 통일 기준 제공
- 데이터 정제 기준 제공
- 학습 / 검증 / 테스트 분리 기준 제공
- 모델 평가 기준 제공
- Overfitting 방지 기준 제공
- LoRA / QLoRA / Full Fine-Tuning 선택 기준 제공
- 배포 전 검증 기준 제공
- Fine-Tuning 실패 대응 기준 제공

Fine-Tuning 문서는 사람이 모델 학습 이론을 공부하기 위한 문서가 아니라, Agent가 Fine-Tuning 적용 여부와 데이터 품질, 평가 기준을 판단할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Fine-Tuning Domain 문서는 무엇을 위한 문서인가?

A. Agent가 Fine-Tuning 적용 여부, 데이터셋 구성, 학습 방식, 평가 기준을 판단할 수 있도록 기준을 제공하는 문서이다.

Q. Fine-Tuning은 RAG를 대체하는가?

A. 아니다. Fine-Tuning은 모델 행동과 출력 패턴 조정에 강하고, RAG는 외부 지식 검색과 최신 정보 반영에 강하다.

Q. Fine-Tuning에서 가장 중요한 것은?

A. 학습 데이터 품질, 적용 목적 명확화, 평가 기준, Overfitting 방지이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Fine-Tuning Domain 문서는 LLM Fine-Tuning을 적용할지 판단하고, 데이터셋을 설계하고, 학습 방식을 선택하고, 결과를 평가하기 위한 규칙을 포함한다.

---

### [핵심]

포함 범위:

- Fine-Tuning 개념
- Supervised Fine-Tuning
- Instruction Tuning
- LoRA
- QLoRA
- Full Fine-Tuning
- Adapter Tuning
- Dataset Design
- Dataset Cleaning
- Dataset Formatting
- Train / Validation / Test Split
- Input / Output Schema
- Token Budget
- Hyperparameter 기준
- Evaluation
- Overfitting
- Catastrophic Forgetting
- Model Selection
- RAG vs Fine-Tuning
- Prompt Engineering vs Fine-Tuning
- Deployment Review
- Fine-Tuning Troubleshooting

제외 범위:

- Transformer 수학 이론 상세
- GPU 커널 최적화 상세
- 분산 학습 내부 구현 상세
- 특정 플랫폼 API 전체 문서 복붙
- 논문 중심 이론 설명
- 무분별한 학습 데이터 수집 방법
- 저작권 불명확 데이터 사용 권장
- 개인정보 포함 데이터 학습 권장
- 최신 지식 저장소로 Fine-Tuning을 사용하는 방식

---

### [실무]

Fine-Tuning 문서는 아래 질문에 답할 수 있어야 한다.

- 이 문제는 Fine-Tuning이 필요한가?
- Prompt Engineering으로 충분한가?
- RAG로 해결해야 하는가?
- 학습 데이터는 어떤 형식이어야 하는가?
- 좋은 Instruction Dataset은 무엇인가?
- 학습 데이터에 무엇을 넣으면 안 되는가?
- LoRA와 QLoRA 중 무엇을 선택해야 하는가?
- Fine-Tuning 결과를 어떻게 평가해야 하는가?
- Overfitting은 어떻게 감지하는가?
- Fine-Tuning 후 배포해도 되는가?

---

### [FAQ]

Q. Fine-Tuning 문서에 모델 학습 수식을 자세히 넣어야 하는가?

A. 아니다. Agent가 적용 여부, 데이터셋 품질, 학습 방식, 평가 기준을 판단할 수 있도록 작성한다.

Q. 특정 플랫폼 API 문서를 그대로 넣어야 하는가?

A. 아니다. 플랫폼별 상세 API는 별도 구현 문서로 분리하고, Domain Rules에서는 판단 기준과 품질 기준을 다룬다.

Q. Fine-Tuning은 언제 고려해야 하는가?

A. 같은 유형의 출력 형식, 스타일, 작업 절차, 도메인 응답 패턴을 반복적으로 안정화해야 할 때 고려한다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Fine-Tuning 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

선택 기준이 필요한 주제는 `[Comparison]`을 추가한다.

평가가 필요한 주제는 `[Evaluation]`, `[Checklist]`를 추가한다.

실패 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

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
- [Evaluation]
- [Troubleshooting]

Optional:

- [Dataset Schema]
- [Training Config]
- [Review Point]
- [Anti-Pattern]
- [Decision Rule]

---

### [실무]

Fine-Tuning 문서는 단순 개념 설명보다 적용 판단과 품질 검증 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Fine-Tuning 적용 조건
- Fine-Tuning 비적합 조건
- Dataset 품질 기준
- 학습 방식 선택 기준
- Evaluation 기준
- Overfitting 방지 기준
- RAG / Prompt와 비교 기준
- 배포 전 Checklist
- Troubleshooting 기준

---

### [FAQ]

Q. Fine-Tuning 문서에 Checklist가 필요한가?

A. 필요하다. Fine-Tuning은 데이터 품질과 평가 기준이 중요하므로 Agent가 검증 기준으로 사용할 수 있어야 한다.

Q. Fine-Tuning 문서에 Comparison이 필요한 이유는?

A. Prompt Engineering, RAG, Fine-Tuning 중 어떤 방법을 선택할지 판단해야 하기 때문이다.

Q. Fine-Tuning 문서에 Troubleshooting이 필요한가?

A. 필요하다. Overfitting, 출력 형식 붕괴, 성능 저하, 데이터 누수 같은 문제가 자주 발생하기 때문이다.

---

# 4. Core Concept Rules

## 4.1 Fine-Tuning 핵심 개념 작성 규칙

### [개념]

Fine-Tuning 핵심 개념은 Prompt Engineering, RAG, Long-Term Memory, Model Quantization과 구분되도록 작성한다.

Fine-Tuning은 모델 가중치나 Adapter를 학습하여 모델 행동을 조정하는 방식이다.

외부 지식을 검색하는 방식이 아니며, 장기 기억 저장소도 아니다.

---

### [핵심]

반드시 포함할 개념:

- Fine-Tuning
- Supervised Fine-Tuning
- Instruction Tuning
- LoRA
- QLoRA
- Full Fine-Tuning
- Adapter
- Dataset
- Training Data
- Validation Data
- Test Data
- Input Format
- Output Format
- Hyperparameter
- Evaluation
- Overfitting
- Catastrophic Forgetting
- Data Leakage
- RAG
- Prompt Engineering

용어 통일:

- Fine-Tuning
- Supervised Fine-Tuning
- Instruction Tuning
- LoRA
- QLoRA
- Full Fine-Tuning
- Training Dataset
- Validation Dataset
- Test Dataset
- Evaluation Dataset
- Overfitting
- Catastrophic Forgetting
- Data Leakage

---

### [실무]

Fine-Tuning 설명은 아래 구분을 반드시 포함한다.

```text
Prompt Engineering
→ 입력 지시를 개선하여 모델 응답을 조정

RAG
→ 외부 문서를 검색해 Context로 제공

Long-Term Memory
→ 사용자 선호와 프로젝트 맥락을 장기 저장

Fine-Tuning
→ 학습 데이터로 모델 행동과 출력 패턴을 조정

Model Quantization
→ 모델 크기와 추론 비용을 줄이기 위해 수치 정밀도 축소
```

Fine-Tuning 문서는 “모델을 추가 학습한다” 수준에서 멈추면 안 된다.

Agent가 언제 Fine-Tuning을 선택하고, 어떤 데이터를 준비하고, 어떤 평가를 해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Fine-Tuning은 무엇인가?

A. 기존 모델에 특정 목적의 데이터셋을 추가 학습시켜 응답 패턴, 스타일, 형식, 작업 수행 방식을 조정하는 기법이다.

Q. Fine-Tuning과 RAG의 차이는?

A. Fine-Tuning은 모델 행동을 조정하고, RAG는 외부 지식을 검색해 답변 근거로 제공한다.

Q. Fine-Tuning과 Prompt Engineering의 차이는?

A. Prompt Engineering은 입력 지시를 조정하고, Fine-Tuning은 학습을 통해 모델의 응답 패턴을 조정한다.

---

# 5. Use Case Decision Rules

## 5.1 Fine-Tuning 적용 여부 판단 규칙

### [개념]

Fine-Tuning 적용 여부 판단은 Fine-Tuning이 필요한 문제와 필요하지 않은 문제를 구분하는 과정이다.

Fine-Tuning은 비용과 위험이 있으므로 모든 문제에 적용하지 않는다.

---

### [핵심]

Fine-Tuning 적합 상황:

- 반복되는 출력 형식 고정
- 특정 도메인 응답 스타일 학습
- 특정 작업 절차 학습
- 분류 / 라벨링 패턴 학습
- 코드 리뷰 기준 반복 적용
- Agent 응답 형식 안정화
- 특정 말투나 정책 준수 패턴 학습
- Prompt가 지나치게 길어지는 문제 완화
- 소형 모델의 특정 작업 성능 개선

Fine-Tuning 비적합 상황:

- 최신 정보 반영
- 자주 바뀌는 지식 저장
- 문서 기반 정확한 근거 답변
- 데이터가 적거나 품질이 낮음
- 한두 번 사용하는 작업
- 프롬프트로 충분히 해결 가능
- RAG로 해결 가능한 지식 검색 문제
- 개인정보나 민감정보가 포함된 데이터 학습
- 평가 데이터가 없음

---

### [실무]

Fine-Tuning 선택 Flow:

```text
User Requirement
→ Prompt로 해결 가능한가?
→ RAG로 해결 가능한가?
→ 반복되는 출력 / 행동 패턴인가?
→ 고품질 학습 데이터가 충분한가?
→ 평가 데이터가 있는가?
→ Fine-Tuning 후보
```

선택 기준 예시:

```text
문제:
RAG 문서 출력 형식을 매번 동일하게 유지하고 싶음

판단:
- 반복 출력 형식
- 예시 데이터 생성 가능
- 평가 기준 명확
→ Fine-Tuning 후보 가능

문제:
최신 Spring Security 변경사항을 답변하고 싶음

판단:
- 최신성 필요
- 외부 문서 검색 필요
→ RAG 또는 Web Search 대상
```

---

### [FAQ]

Q. Fine-Tuning은 언제 해야 하는가?

A. 반복되는 출력 형식, 작업 절차, 스타일, 분류 패턴을 모델이 안정적으로 수행해야 할 때 고려한다.

Q. Fine-Tuning으로 최신 지식을 넣는 것이 좋은가?

A. 아니다. 최신 지식은 RAG나 검색 시스템으로 처리하는 것이 적합하다.

Q. Prompt로 해결되는 문제도 Fine-Tuning해야 하는가?

A. 아니다. Prompt로 충분하면 Fine-Tuning보다 Prompt Engineering을 우선한다.

---

# 6. RAG vs Fine-Tuning Rules

## 6.1 RAG / Fine-Tuning 선택 기준

### [개념]

RAG와 Fine-Tuning은 서로 대체 관계가 아니라 상호 보완 관계이다.

RAG는 외부 지식 검색과 근거 기반 답변에 강하고, Fine-Tuning은 모델 행동과 출력 패턴 조정에 강하다.

---

### [핵심]

RAG 적합:

- 최신 정보 필요
- 문서 근거 필요
- 출처 기반 답변 필요
- 지식이 자주 변경됨
- 대량 문서 검색 필요
- 사용자별 문서가 다름
- Hallucination을 근거 검색으로 줄이고 싶음

Fine-Tuning 적합:

- 출력 형식 반복
- 스타일 반복
- 작업 절차 반복
- 특정 라벨링 패턴
- 도메인 응답 습관
- 짧은 Prompt로 안정적 동작 필요
- 소형 모델 성능 개선

Hybrid 적합:

- RAG 문서를 검색하되 출력 형식은 Fine-Tuning으로 안정화
- Agent Workflow는 Fine-Tuning하고 지식은 RAG로 제공
- 도메인 답변 스타일은 Fine-Tuning하고 최신 근거는 RAG로 제공

---

### [실무]

비교 표:

| 기준             | RAG              | Fine-Tuning               |
| ---------------- | ---------------- | ------------------------- |
| 목적             | 외부 지식 검색   | 모델 행동 조정            |
| 최신성           | 강함             | 약함                      |
| 출처 근거        | 강함             | 약함                      |
| 출력 형식 안정화 | 보통             | 강함                      |
| 반복 작업 패턴   | 보통             | 강함                      |
| 데이터 변경 대응 | 쉬움             | 재학습 필요               |
| 비용 구조        | 검색 / 저장 비용 | 학습 / 배포 비용          |
| 위험             | 검색 실패        | Overfitting / 데이터 오염 |

Hybrid Flow:

```text
User Request
→ RAG Retrieval
→ Retrieved Context
→ Fine-Tuned Model
→ Stable Format Output
→ Review Validation
```

---

### [FAQ]

Q. RAG와 Fine-Tuning 중 무엇을 먼저 고려해야 하는가?

A. 최신 지식과 근거가 필요하면 RAG를 우선하고, 반복 출력 패턴과 행동 조정이 필요하면 Fine-Tuning을 고려한다.

Q. RAG와 Fine-Tuning을 함께 사용할 수 있는가?

A. 가능하다. 지식은 RAG로 제공하고 출력 형식이나 작업 패턴은 Fine-Tuning으로 안정화할 수 있다.

Q. Hallucination을 줄이기 위해 Fine-Tuning만 하면 되는가?

A. 아니다. 근거 기반 답변이 필요하면 RAG와 Grounding 검증이 필요하다.

---

# 7. Dataset Design Rules

## 7.1 Fine-Tuning Dataset 설계 규칙

### [개념]

Dataset Design은 Fine-Tuning 목적에 맞는 입력과 출력 예시를 설계하는 과정이다.

Fine-Tuning 성능은 모델보다 데이터셋 품질에 더 크게 좌우된다.

---

### [핵심]

Dataset 구성 요소:

- instruction
- input
- output
- system message
- user message
- assistant message
- metadata
- taskType
- domain
- difficulty
- source
- qualityScore

좋은 Dataset 조건:

- 목적이 명확함
- 입력 / 출력 형식이 일관됨
- 정답 품질이 높음
- 중복이 적음
- 도메인 용어가 통일됨
- 예외 케이스 포함
- 실패 케이스 포함
- 평가 데이터와 분리됨
- 개인정보 제거
- 저작권 위험 낮음

---

### [실무]

Instruction Dataset 예시:

```json
{
  "instruction": "다음 요구사항을 RAG 문서 형식으로 변환하라.",
  "input": "Spring Security JWT 인증 흐름 설명",
  "output": "# FileName\n\n# Document Title\n\n---\n\n# 1. JWT Authentication\n\n### [개념]\nJWT 인증 흐름 설명..."
}
```

Chat Dataset 예시:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "너는 RAG 문서 제작 Agent이다."
    },
    {
      "role": "user",
      "content": "JWT 인증 Domain Rules 작성"
    },
    {
      "role": "assistant",
      "content": "정해진 문서 형식에 맞춘 출력..."
    }
  ]
}
```

Dataset은 모델에게 원하는 행동을 반복적으로 보여주는 예시 집합이다.

부정확한 예시는 성능 저하를 유발한다.

---

### [FAQ]

Q. Fine-Tuning Dataset에서 가장 중요한 것은?

A. 목적에 맞는 고품질 입력 / 출력 쌍과 일관된 형식이다.

Q. Dataset에 다양한 형식을 섞어도 되는가?

A. 목적이 다르면 분리하는 것이 좋다. 출력 형식이 섞이면 모델 응답이 불안정해질 수 있다.

Q. 평가 데이터도 학습에 넣어도 되는가?

A. 안 된다. 평가 데이터가 학습에 포함되면 Data Leakage가 발생한다.

---

# 8. Dataset Cleaning Rules

## 8.1 Dataset 정제 규칙

### [개념]

Dataset Cleaning은 Fine-Tuning 학습 데이터에서 오류, 중복, 개인정보, 저품질 예시, 형식 불일치를 제거하는 과정이다.

정제되지 않은 데이터는 Fine-Tuned Model의 품질을 낮춘다.

---

### [핵심]

정제 대상:

- 중복 데이터
- 오타
- 잘못된 정답
- 형식 불일치
- 너무 긴 예시
- 너무 짧은 예시
- 목적과 무관한 예시
- 개인정보
- API Key / Password
- 저작권 위험 데이터
- 편향적 표현
- 안전하지 않은 응답
- 평가 데이터와 중복되는 학습 데이터

Cleaning Checklist:

```md
### [Checklist]

- 중복 예시를 제거했는가?
- 출력 형식이 일관되는가?
- 정답이 실제로 맞는가?
- 개인정보가 제거되었는가?
- API Key나 비밀번호가 없는가?
- 학습 목적과 무관한 예시를 제거했는가?
- 평가 데이터와 중복되지 않는가?
- 너무 긴 예시를 분리하거나 제거했는가?
```

---

### [실무]

나쁜 데이터 예시:

```text
instruction:
RAG 문서 만들어줘

output:
좋아요! 아래는 문서입니다. 대충 이런 식으로 쓰면 됩니다...
```

좋은 데이터 예시:

```text
instruction:
Spring Security JWT 인증 흐름을 RAG 문서 형식으로 작성하라.

output:
정해진 Header, Section, FAQ, Retrieval Queries 형식을 준수한 완성 문서
```

Fine-Tuning Dataset은 모델이 따라 해야 할 정답이다.

정답이 흔들리면 모델 출력도 흔들린다.

---

### [FAQ]

Q. Dataset Cleaning은 왜 중요한가?

A. 모델은 학습 데이터의 오류와 불일치도 함께 학습하기 때문이다.

Q. 중복 데이터는 모두 나쁜가?

A. 완전 중복은 제거하는 것이 좋고, 중요한 패턴은 다양한 표현으로 확장하는 것이 좋다.

Q. 개인정보가 포함된 데이터를 학습해도 되는가?

A. 안 된다. 개인정보와 민감정보는 제거하거나 익명화해야 한다.

---

# 9. Dataset Format Rules

## 9.1 Fine-Tuning Dataset Format 작성 규칙

### [개념]

Dataset Format은 Fine-Tuning 데이터를 모델이나 학습 프레임워크가 사용할 수 있도록 구조화하는 방식이다.

형식이 일관되지 않으면 학습 품질과 추론 출력이 불안정해진다.

---

### [핵심]

대표 Format:

- Instruction Format
- Chat Format
- Completion Format
- Preference Format
- Classification Format
- JSONL Format

형식 작성 기준:

- 하나의 Dataset에는 하나의 주요 Format 사용
- system / user / assistant 역할 구분
- input과 output 명확히 분리
- JSON 문법 오류 금지
- 줄바꿈 일관성 유지
- Escape 처리 확인
- 불필요한 설명 제거
- 출력 예시는 최종 정답만 포함

---

### [실무]

JSONL Chat Format 예시:

```json
{
  "messages": [
    { "role": "system", "content": "너는 코드 리뷰 Agent이다." },
    { "role": "user", "content": "다음 Service 코드를 검토해줘." },
    {
      "role": "assistant",
      "content": "검토 결과:\n- 트랜잭션 누락\n- 예외 처리 필요\n- 테스트 케이스 추가 필요"
    }
  ]
}
```

Instruction Format 예시:

```json
{
  "instruction": "다음 코드를 리뷰하라.",
  "input": "public void save(User user) { repository.save(user); }",
  "output": "검토 결과:\n- null 검증 필요\n- 트랜잭션 경계 확인 필요"
}
```

Dataset Format은 학습 대상 모델과 플랫폼 요구사항에 맞춰 작성한다.

---

### [FAQ]

Q. Fine-Tuning Dataset Format은 왜 중요한가?

A. 모델이 입력과 출력 구조를 학습하므로 형식이 흔들리면 추론 결과도 불안정해진다.

Q. JSONL을 사용할 때 주의할 점은?

A. 한 줄에 하나의 JSON 객체를 작성하고 문법 오류, 줄바꿈, 따옴표 Escape를 검증해야 한다.

Q. 여러 Format을 한 Dataset에 섞어도 되는가?

A. 권장하지 않는다. 목적이 다르면 Dataset을 분리하는 것이 좋다.

---

# 10. Data Split Rules

## 10.1 Train / Validation / Test 분리 규칙

### [개념]

Data Split은 Fine-Tuning Dataset을 학습용, 검증용, 테스트용으로 나누는 과정이다.

Data Split이 잘못되면 모델 평가 결과를 신뢰할 수 없다.

---

### [핵심]

Dataset 분리:

- Training Dataset: 모델 학습에 사용
- Validation Dataset: 학습 중 성능 확인과 튜닝에 사용
- Test Dataset: 최종 평가에 사용

주의 사항:

- 동일 예시 중복 금지
- 유사한 예시 누수 주의
- Test Dataset은 학습에 사용 금지
- Validation과 Test 목적 구분
- 시간 순서가 중요한 데이터는 시간 기준 분리 고려
- 프로젝트별 데이터는 프로젝트 단위 분리 고려
- 사용자별 데이터는 사용자 단위 분리 고려

---

### [실무]

권장 분리 예시:

```text
Small Dataset:
- Train 80%
- Validation 10%
- Test 10%

Medium / Large Dataset:
- Train 90%
- Validation 5%
- Test 5%

중요:
- 비율보다 Data Leakage 방지가 우선
```

데이터가 적을수록 Test Dataset 품질이 중요하다.

평가용 데이터가 너무 적으면 Fine-Tuning 효과를 판단하기 어렵다.

---

### [FAQ]

Q. Test Dataset을 학습에 사용하면 안 되는 이유는?

A. 모델이 평가 정답을 미리 학습해 실제 성능보다 높게 측정되는 Data Leakage가 발생하기 때문이다.

Q. Validation Dataset과 Test Dataset의 차이는?

A. Validation은 학습 중 조정에 사용하고, Test는 최종 성능 평가에 사용한다.

Q. 데이터가 적으면 어떻게 해야 하는가?

A. Fine-Tuning보다 Prompt Engineering이나 RAG를 우선 검토하고, 필요한 경우 고품질 평가 세트를 먼저 확보한다.

---

# 11. Training Method Rules

## 11.1 Fine-Tuning 방식 선택 규칙

### [개념]

Training Method는 모델을 어떤 방식으로 추가 학습할지 결정하는 기준이다.

Fine-Tuning 방식은 데이터 규모, 하드웨어, 목표, 비용, 배포 방식에 따라 선택한다.

---

### [핵심]

대표 방식:

- Full Fine-Tuning
- LoRA
- QLoRA
- Adapter Tuning
- Instruction Tuning
- Preference Tuning

선택 기준:

- 제한된 GPU / VRAM → LoRA 또는 QLoRA
- 전체 모델 행동 대폭 변경 → Full Fine-Tuning 검토
- 출력 형식 / 작업 패턴 조정 → LoRA 또는 Instruction Tuning
- 저비용 실험 → QLoRA
- 배포 모델 크기 유지 필요 → Adapter 기반 방식
- 개인 AI 서버 환경 → LoRA / QLoRA 우선 검토

---

### [실무]

Training Method 비교:

| 방식               | 장점              | 단점                  | 사용 상황             |
| ------------------ | ----------------- | --------------------- | --------------------- |
| Full Fine-Tuning   | 변경 폭 큼        | 비용 큼, 위험 큼      | 대규모 데이터와 자원  |
| LoRA               | 효율적, 관리 쉬움 | 변경 폭 제한          | 일반 실무 Fine-Tuning |
| QLoRA              | VRAM 절약         | 품질 / 속도 Trade-off | 제한된 하드웨어       |
| Adapter            | 모듈 교체 용이    | 프레임워크 의존       | 다중 Task 관리        |
| Instruction Tuning | 지시 수행 개선    | 데이터 품질 의존      | 작업 형식 학습        |

개인 AI 서버나 제한된 하드웨어에서는 Full Fine-Tuning보다 LoRA / QLoRA를 우선 검토한다.

---

### [FAQ]

Q. LoRA는 무엇인가?

A. 전체 모델을 모두 학습하지 않고 작은 Adapter 행렬을 학습해 효율적으로 모델 행동을 조정하는 방식이다.

Q. QLoRA는 무엇인가?

A. 양자화된 모델 위에서 LoRA 학습을 수행해 VRAM 사용량을 줄이는 방식이다.

Q. Full Fine-Tuning은 언제 필요한가?

A. 대규모 고품질 데이터와 충분한 자원이 있고 모델 행동을 크게 바꿔야 할 때 검토한다.

---

# 12. Hyperparameter Rules

## 12.1 Hyperparameter 작성 규칙

### [개념]

Hyperparameter는 Fine-Tuning 학습 과정을 제어하는 설정값이다.

Hyperparameter는 모델 품질, Overfitting, 학습 안정성, 비용에 영향을 준다.

---

### [핵심]

주요 Hyperparameter:

- learningRate
- batchSize
- epoch
- warmupRatio
- weightDecay
- maxSequenceLength
- gradientAccumulationSteps
- loraRank
- loraAlpha
- loraDropout
- targetModules
- scheduler
- optimizer

작성 기준:

- 기본값 맹신 금지
- 작은 실험부터 시작
- Validation Loss 추적
- Overfitting 감시
- 데이터 크기에 따라 epoch 조정
- maxSequenceLength는 실제 데이터 길이에 맞춤
- LoRA rank는 성능과 비용 Trade-off 고려

---

### [실무]

Hyperparameter 문서는 특정 고정값보다 조정 기준을 우선 작성한다.

```text
learningRate:
- 너무 높으면 학습 불안정
- 너무 낮으면 학습 부족
- 작은 실험으로 탐색

epoch:
- 너무 많으면 Overfitting 위험
- 데이터가 작을수록 주의

batchSize:
- VRAM에 맞춰 조정
- gradientAccumulation으로 보완 가능

maxSequenceLength:
- 데이터 길이를 분석한 뒤 설정
- 불필요하게 크면 비용 증가
```

Hyperparameter는 Evaluation 결과와 함께 기록한다.

---

### [FAQ]

Q. Hyperparameter는 왜 중요한가?

A. 같은 데이터와 모델이라도 Hyperparameter에 따라 성능, 비용, Overfitting이 크게 달라질 수 있다.

Q. epoch는 많을수록 좋은가?

A. 아니다. epoch가 많으면 Overfitting 위험이 커진다.

Q. maxSequenceLength는 크게 잡는 것이 좋은가?

A. 아니다. 실제 데이터 길이에 맞게 설정해야 비용과 메모리 낭비를 줄일 수 있다.

---

# 13. Evaluation Rules

## 13.1 Fine-Tuning Evaluation 작성 규칙

### [개념]

Fine-Tuning Evaluation은 Fine-Tuned Model이 목표 작업을 실제로 더 잘 수행하는지 평가하는 과정이다.

Fine-Tuning은 학습 완료가 아니라 평가 통과가 완료 기준이다.

---

### [핵심]

평가 항목:

- Task Accuracy
- Format Compliance
- Instruction Following
- Domain Consistency
- Output Stability
- Hallucination Rate
- Groundedness
- Safety Compliance
- Regression
- Overfitting
- Latency
- Cost
- Human Preference
- Baseline Comparison

평가 비교 대상:

- Base Model
- Prompt-only Model
- RAG-only Model
- Fine-Tuned Model
- Fine-Tuned + RAG Model

---

### [실무]

Evaluation Checklist:

```md
### [Checklist]

- Base Model보다 성능이 개선되었는가?
- Prompt-only 방식보다 안정적인가?
- 출력 형식을 더 잘 지키는가?
- Test Dataset에서 성능이 유지되는가?
- Validation 성능만 좋아진 것은 아닌가?
- Hallucination이 증가하지 않았는가?
- 기존 일반 능력이 심하게 저하되지 않았는가?
- 안전하지 않은 응답이 늘어나지 않았는가?
- RAG와 함께 사용할 때 근거 기반 답변이 유지되는가?
```

Fine-Tuning 평가는 정량 평가와 정성 평가를 함께 사용한다.

---

### [FAQ]

Q. Fine-Tuning Evaluation은 왜 필요한가?

A. Fine-Tuning이 실제로 개선을 만들었는지 확인하지 않으면 비용만 들고 성능이 나빠질 수 있기 때문이다.

Q. Base Model과 비교해야 하는가?

A. 반드시 비교해야 한다. Fine-Tuned Model이 Base Model보다 나아졌는지 확인해야 한다.

Q. 출력 형식도 평가해야 하는가?

A. 해야 한다. Fine-Tuning의 주요 목적이 형식 안정화인 경우 Format Compliance가 핵심 평가 항목이다.

---

# 14. Overfitting Rules

## 14.1 Overfitting 방지 규칙

### [개념]

Overfitting은 모델이 학습 데이터에는 잘 맞지만 새로운 입력에는 성능이 떨어지는 상태이다.

Fine-Tuning에서는 데이터가 작거나 반복 예시가 많을수록 Overfitting 위험이 커진다.

---

### [핵심]

Overfitting 징후:

- Training Loss는 감소하지만 Validation Loss 증가
- 학습 예시와 유사한 답변만 반복
- 새로운 입력에 취약
- 출력 다양성 감소
- 특정 문구 과다 반복
- Test Dataset 성능 저하
- Base Model 일반 능력 저하
- 과도하게 정해진 형식만 출력

방지 방법:

- Validation Dataset 확보
- Test Dataset 분리
- epoch 제한
- learningRate 조정
- 중복 데이터 제거
- 다양한 예시 포함
- Early Stopping
- LoRA Dropout 활용
- 학습 전후 비교 평가

---

### [실무]

Overfitting 점검 Flow:

```text
Training
→ Training Loss 확인
→ Validation Loss 확인
→ Test Dataset 평가
→ Base Model 비교
→ 출력 다양성 확인
→ Regression Test
```

데이터가 적은 경우 Fine-Tuning보다 Prompt Template, RAG, Few-shot Prompt를 우선 검토한다.

---

### [FAQ]

Q. Overfitting은 무엇인가?

A. 모델이 학습 데이터에는 잘 맞지만 새로운 입력에는 일반화하지 못하는 상태이다.

Q. Overfitting은 어떻게 감지하는가?

A. Training Loss와 Validation Loss 차이, Test 성능 저하, 출력 반복, 일반 능력 저하로 감지한다.

Q. 데이터가 적어도 Fine-Tuning해도 되는가?

A. 가능은 하지만 위험이 크다. 먼저 Prompt Engineering, RAG, 데이터 확충을 검토하는 것이 좋다.

---

# 15. Catastrophic Forgetting Rules

## 15.1 Catastrophic Forgetting 방지 규칙

### [개념]

Catastrophic Forgetting은 Fine-Tuning 후 모델이 기존에 잘하던 일반 능력이나 다른 작업 능력을 잃는 현상이다.

특정 데이터에 과도하게 학습하면 모델의 범용성이 떨어질 수 있다.

---

### [핵심]

발생 원인:

- 데이터셋이 너무 좁음
- epoch 과다
- learningRate 과다
- 특정 출력 패턴만 반복
- Full Fine-Tuning 남용
- 평가 범위가 너무 좁음
- 기존 능력 회귀 테스트 누락

방지 방법:

- 다양한 평가 세트 사용
- Regression Test 수행
- LoRA / QLoRA 우선 검토
- 학습률 낮게 시작
- epoch 제한
- 일반 능력 평가 포함
- 학습 목적 범위 제한

---

### [실무]

Regression Test 예시:

```text
Fine-Tuning 목적:
- RAG 문서 출력 형식 안정화

Regression Test:
- 일반 질문 답변 능력
- 코드 설명 능력
- 요약 능력
- 지시문 준수 능력
- 한국어 응답 품질
- 안전 정책 준수
```

Fine-Tuned Model은 목표 작업 성능뿐 아니라 기존 필수 능력도 유지해야 한다.

---

### [FAQ]

Q. Catastrophic Forgetting은 무엇인가?

A. Fine-Tuning 후 모델이 기존에 잘하던 능력을 잃는 현상이다.

Q. Catastrophic Forgetting은 왜 위험한가?

A. 특정 작업은 좋아져도 전체 Agent 품질이 떨어질 수 있기 때문이다.

Q. 어떻게 방지하는가?

A. LoRA / QLoRA 사용, 학습률 조정, epoch 제한, Regression Test로 방지한다.

---

# 16. Safety and Privacy Rules

## 16.1 Fine-Tuning Safety / Privacy 작성 규칙

### [개념]

Fine-Tuning Safety / Privacy는 학습 데이터와 모델 출력이 개인정보, 민감정보, 보안정보, 저작권, 안전 정책을 침해하지 않도록 관리하는 규칙이다.

Fine-Tuning은 데이터를 모델 행동에 반영하므로 데이터 안전성이 매우 중요하다.

---

### [핵심]

학습 금지 또는 주의 데이터:

- 개인정보
- 민감정보
- 비밀번호
- API Key
- Access Token
- Refresh Token
- 인증서
- 개인 연락처
- 상세 주소
- 결제 정보
- 의료 / 정치 / 종교 등 민감 속성
- 저작권 불명확 대량 텍스트
- 내부 기밀 문서
- 악성 코드 작성 데이터
- 안전하지 않은 응답 예시

안전 기준:

- 개인정보 제거
- 비식별화
- 저작권 확인
- 데이터 출처 기록
- 안전하지 않은 출력 제거
- 평가 단계에서 Safety Test 수행
- 배포 전 Review Agent 검증
- 사용자 데이터 학습 시 명시적 기준 필요

---

### [실무]

Safety Checklist:

```md
### [Checklist]

- 학습 데이터에 개인정보가 없는가?
- API Key나 Token이 제거되었는가?
- 민감정보가 포함되지 않았는가?
- 저작권 문제가 없는 데이터인가?
- 내부 기밀이 포함되지 않았는가?
- 안전하지 않은 응답 패턴을 학습하지 않는가?
- 모델 출력 Safety Test를 수행했는가?
- 삭제 요청 데이터를 학습에서 제외했는가?
```

Fine-Tuning 데이터는 RAG 문서보다 더 엄격하게 관리한다.

한 번 학습된 데이터 영향은 단순 삭제보다 제거가 어렵다.

---

### [FAQ]

Q. 개인정보가 포함된 데이터로 Fine-Tuning해도 되는가?

A. 원칙적으로 피해야 하며, 필요한 경우 비식별화와 명시적 관리 기준이 필요하다.

Q. API Key가 포함된 데이터를 학습하면 어떤 문제가 생기는가?

A. 모델이 보안정보를 출력하거나 내부적으로 학습할 위험이 있으므로 반드시 제거해야 한다.

Q. Fine-Tuning 데이터는 왜 RAG 문서보다 더 조심해야 하는가?

A. RAG 문서는 제거가 쉽지만 Fine-Tuning된 데이터 영향은 모델 내부에 반영되어 제거가 어렵기 때문이다.

---

# 17. Deployment Rules

## 17.1 Fine-Tuned Model 배포 규칙

### [개념]

Fine-Tuned Model 배포는 학습된 모델을 실제 Agent 시스템이나 서비스에 적용하는 과정이다.

배포 전에는 성능, 안전성, 비용, 기존 Workflow와의 호환성을 검증해야 한다.

---

### [핵심]

배포 전 확인 항목:

- Evaluation 통과
- Base Model 대비 개선 확인
- Regression Test 통과
- Safety Test 통과
- Output Format 검증
- RAG 연동 검증
- Tool Calling 연동 검증
- Latency 확인
- Cost 확인
- Rollback 가능 여부
- Version 관리
- Monitoring 설정
- 사용자 영향 범위 확인

---

### [실무]

Deployment Checklist:

```md
### [Checklist]

- 모델 버전이 명확한가?
- 학습 데이터 버전이 기록되었는가?
- 평가 결과가 기록되었는가?
- 배포 전 비교 테스트를 수행했는가?
- RAG Pipeline과 충돌하지 않는가?
- Agent Output Format이 유지되는가?
- 실패 시 Base Model로 Rollback 가능한가?
- Monitoring과 Logging이 설정되었는가?
```

Fine-Tuned Model은 바로 기존 모델을 대체하지 않는다.

Canary, A/B Test, 제한된 Agent부터 적용하는 방식을 권장한다.

---

### [FAQ]

Q. Fine-Tuned Model을 바로 Production에 배포해도 되는가?

A. 권장하지 않는다. Evaluation, Safety Test, Regression Test, Rollback 계획이 필요하다.

Q. Rollback 계획은 왜 필요한가?

A. Fine-Tuned Model이 예상치 못한 성능 저하나 출력 오류를 일으킬 수 있기 때문이다.

Q. 배포 후 무엇을 모니터링해야 하는가?

A. 출력 품질, 형식 준수율, Hallucination, Latency, Cost, 사용자 피드백, 오류율을 모니터링한다.

---

# 18. Observability Rules

## 18.1 Fine-Tuning Observability 작성 규칙

### [개념]

Fine-Tuning Observability는 학습 데이터, 학습 설정, 평가 결과, 배포 후 성능 변화를 추적하는 구조이다.

Fine-Tuning은 실험과 운영 이력이 중요하므로 추적 가능해야 한다.

---

### [핵심]

관측 대상:

- modelName
- baseModel
- fineTunedModelVersion
- datasetVersion
- trainingConfig
- hyperparameters
- trainingLoss
- validationLoss
- evaluationResult
- safetyTestResult
- regressionTestResult
- deploymentVersion
- rollbackVersion
- inferenceLatency
- inferenceCost
- userFeedback
- failureCase

기록 기준:

- Dataset 버전 기록
- 학습 설정 기록
- 평가 결과 기록
- 실패 사례 기록
- 배포 버전 기록
- Rollback 기준 기록

---

### [실무]

Fine-Tuning Trace 예시:

```text
modelName: qwen-finetuned-rag-doc-agent
baseModel: qwen2.5
datasetVersion: rag-doc-format-v1
trainingMethod: LoRA
evaluationResult: format compliance improved
regressionTest: passed
deploymentStatus: staging
rollbackVersion: qwen2.5-base
```

Observability가 없으면 어떤 데이터와 설정이 성능 개선 또는 악화를 만들었는지 알 수 없다.

---

### [FAQ]

Q. Fine-Tuning Observability는 왜 필요한가?

A. 데이터, 설정, 평가, 배포 결과를 추적해야 성능 개선과 문제 원인을 분석할 수 있기 때문이다.

Q. Dataset Version을 기록해야 하는가?

A. 반드시 기록해야 한다. Fine-Tuning 결과는 데이터 버전에 크게 의존한다.

Q. 실패 사례도 기록해야 하는가?

A. 기록해야 한다. 실패 사례는 다음 Dataset 개선과 Evaluation 강화에 중요하다.

---

# 19. Troubleshooting Rules

## 19.1 Fine-Tuning 장애 대응 작성 규칙

### [개념]

Fine-Tuning Troubleshooting 문서는 학습 데이터, 학습 과정, 평가, 배포 후 발생하는 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- 학습 효과 없음
- 출력 형식 불안정
- Overfitting
- Catastrophic Forgetting
- Hallucination 증가
- 특정 문구 반복
- Validation Loss 증가
- Test 성능 저하
- 데이터 품질 낮음
- Data Leakage
- Safety 성능 저하
- RAG Context 무시
- Tool Calling 형식 붕괴
- 배포 후 Latency 증가
- 비용 증가

---

### [실무]

Troubleshooting 형식:

```md
문제:
Fine-Tuned Model이 출력 형식을 계속 어김

원인:

- Dataset 출력 형식이 일관되지 않음
- 학습 데이터 수가 부족함
- System Prompt와 Fine-Tuning 목표가 충돌함
- Evaluation 기준이 형식 준수를 충분히 측정하지 않음

해결:

- Dataset 출력 형식 통일
- 잘못된 예시 제거
- Format Compliance 평가 추가
- Prompt와 Fine-Tuning 목표 정렬
- 필요 시 추가 Fine-Tuning 또는 Prompt 보완
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. Fine-Tuning 후 성능이 좋아지지 않으면 무엇을 확인해야 하는가?

A. 데이터 품질, 학습 목적, 평가 기준, Hyperparameter, Base Model과의 비교를 확인해야 한다.

Q. Fine-Tuning 후 Hallucination이 늘면 어떻게 해야 하는가?

A. 데이터 품질, RAG Grounding, 평가 기준, 안전 테스트를 점검하고 Fine-Tuning 목표를 재검토한다.

Q. RAG Context를 무시하면 어떻게 해야 하는가?

A. RAG 사용 예시를 Dataset에 포함하고, Prompt와 Evaluation에서 Context Grounding을 강화해야 한다.

---

# 20. Common Mistakes

## 20.1 자주 발생하는 작성 오류

### [개념]

Fine-Tuning 문서는 “모델을 학습하면 성능이 좋아진다”는 단순 설명 문서가 아니다.

Fine-Tuning은 적용 여부 판단, 데이터 품질, 학습 방식, 평가, 안전성, 배포 검증을 모두 포함해야 한다.

---

### [핵심]

금지 또는 주의:

- Fine-Tuning을 RAG 대체제로 설명
- 최신 지식 저장 목적으로 Fine-Tuning 권장
- 데이터 품질 기준 누락
- Dataset Cleaning 기준 누락
- Train / Validation / Test 분리 누락
- Evaluation 없이 학습 완료 처리
- Base Model 비교 누락
- Overfitting 기준 누락
- Catastrophic Forgetting 누락
- Safety / Privacy 기준 누락
- 개인정보 포함 데이터 학습 권장
- Hyperparameter 고정값만 제시
- 배포 전 검증 누락
- Rollback 기준 누락
- Troubleshooting 누락
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Fine-Tuning은 모델을 추가 학습해서 더 똑똑하게 만드는 방법이다.
데이터를 많이 넣으면 성능이 좋아진다.
```

좋은 문서 예시:

```text
Fine-Tuning은 반복되는 출력 형식, 작업 패턴, 도메인 응답 스타일을 모델에 학습시키는 방식이다.

Flow:
Use Case 판단
→ Dataset 설계
→ Cleaning
→ Train / Validation / Test 분리
→ LoRA / QLoRA 선택
→ Training
→ Evaluation
→ Regression Test
→ Deployment Review
```

---

### [FAQ]

Q. Fine-Tuning 문서에서 가장 피해야 할 것은?

A. RAG와 구분하지 않고, 데이터 품질과 평가 기준 없이 Fine-Tuning을 만능 해결책처럼 설명하는 것이다.

Q. Fine-Tuning에 데이터를 많이 넣으면 무조건 좋은가?

A. 아니다. 품질 낮은 데이터는 모델 성능을 오히려 떨어뜨린다.

Q. Evaluation 없이 Fine-Tuning을 완료해도 되는가?

A. 안 된다. Fine-Tuning 완료 기준은 학습 완료가 아니라 평가 통과이다.

---

# 21. Document Split Rules

## 21.1 Fine-Tuning 문서 분할 기준

### [개념]

Fine-Tuning은 적용 판단, 데이터셋 설계, 학습 방식, 평가, 안전성, 배포 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Fine_Tuning_Part01_Core.md
Fine_Tuning_Part02_Use_Case_Decision.md
Fine_Tuning_Part03_Dataset_Design_Cleaning.md
Fine_Tuning_Part04_Dataset_Format_Split.md
Fine_Tuning_Part05_LoRA_QLoRA_Training_Method.md
Fine_Tuning_Part06_Hyperparameter_Overfitting.md
Fine_Tuning_Part07_Evaluation_Safety.md
Fine_Tuning_Part08_Deployment_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Use Case 판단은 RAG / Prompt 비교 포함
- Dataset 문서는 Design과 Cleaning 중심
- Format과 Split은 함께 작성 가능
- Training Method는 LoRA / QLoRA 중심
- Evaluation은 Checklist 중심
- Safety는 개인정보 / 보안정보 제거 기준 포함
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Fine-Tuning 문서 Set은 AI Expert Level에서 사용한다.

단, Backend Agent와 DevOps Agent도 구현과 배포 과정에서 참조할 수 있으므로 특정 프레임워크 API보다 판단 기준, 데이터 기준, 평가 기준을 우선한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Fine_Tuning_Domain_Rules.md
LoRA_QLoRA_Domain_Rules.md
Dataset_Preparation_Part.md
Model_Evaluation_Part.md
Fine_Tuned_Model_Deployment_Part.md
```

---

### [FAQ]

Q. Fine-Tuning 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 7~8개 Part를 권장한다. Core, Use Case, Dataset, Format, Training Method, Hyperparameter, Evaluation/Safety, Deployment/Troubleshooting으로 분리한다.

Q. LoRA / QLoRA 문서와 Fine-Tuning 문서를 합쳐도 되는가?

A. 기본 개념은 포함하되, 상세 구현과 설정은 별도 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 22. Agent Usage Rules

## 22.1 Agent별 사용 기준

### [개념]

Fine-Tuning Domain Rules는 여러 Agent가 Fine-Tuning 적용 여부를 판단하고, 데이터셋 품질을 검토하고, 학습 방식과 평가 기준을 선택하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Fine-Tuning Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- Fine-Tuning 필요 여부 판단
- RAG / Prompt / Fine-Tuning 선택
- 작업 범위 정의
- 평가 기준 요청
- Human Review 필요 여부 판단

AI/ML Agent:

- Dataset 설계
- Training Method 선택
- Hyperparameter 기준 설정
- Evaluation 설계
- Overfitting / Regression 점검

Backend Agent:

- Fine-Tuning API 연동
- Dataset Pipeline 구현
- Model Serving 연동
- RAG + Fine-Tuned Model 통합

DevOps Agent:

- 학습 환경 구성
- GPU / VRAM 자원 관리
- Model Version 관리
- 배포 / Rollback / Monitoring 구성

Review Agent:

- Dataset 품질 검토
- Evaluation 결과 검토
- Safety / Privacy 검토
- RAG 대체 오용 검토
- 배포 전 Checklist 검토

Architecture Review Agent:

- Fine-Tuning 적용 타당성 검토
- RAG / Memory / Agent 구조와 충돌 여부 검토
- 장기 유지보수성 검토
- 비용 / 확장성 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Use Case Decision / RAG vs Fine-Tuning / Evaluation Requirement

AI/ML Agent
→ Dataset Design / Training Method / Hyperparameter / Evaluation

Backend Agent
→ Dataset Pipeline / Model API / RAG Integration

DevOps Agent
→ Training Environment / Deployment / Observability / Rollback

Review Agent
→ Dataset Cleaning / Safety / Overfitting / Common Mistakes / Evaluation

Architecture Review Agent
→ System Fit / Cost / Scalability / Long-Term Maintenance
```

Fine-Tuning은 AI/ML Agent 단독 결정으로 진행하지 않는다.

PM Agent의 목적 정의와 Review Agent의 평가 검증이 필요하다.

---

### [FAQ]

Q. Fine-Tuning Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. PM Agent는 Fine-Tuning에서 무엇을 판단해야 하는가?

A. Fine-Tuning이 필요한 문제인지, RAG나 Prompt로 충분한지, 평가 기준이 있는지 판단해야 한다.

Q. Review Agent는 Fine-Tuning에서 무엇을 검토해야 하는가?

A. Dataset 품질, 개인정보 제거, Evaluation 결과, Overfitting, RAG 대체 오용, 배포 전 위험을 검토해야 한다.

---

# 23. Final Goal

## 23.1 최종 목표

### [개념]

Fine-Tuning Domain Rules의 최종 목표는 Agent가 Fine-Tuning을 만능 해결책으로 오용하지 않고, 적절한 상황에서만 데이터 품질과 평가 기준을 갖춘 상태로 적용할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Fine-Tuning 개념 검색 가능
- RAG / Prompt / Fine-Tuning 구분 가능
- Fine-Tuning 적용 여부 판단 가능
- Dataset 설계 가능
- Dataset Cleaning 가능
- Dataset Format 선택 가능
- Train / Validation / Test 분리 가능
- LoRA / QLoRA / Full Fine-Tuning 선택 가능
- Hyperparameter 기준 판단 가능
- Evaluation 가능
- Overfitting 감지 가능
- Catastrophic Forgetting 감지 가능
- Safety / Privacy 검토 가능
- Deployment Review 가능
- Troubleshooting 가능

---

### [실무]

Fine-Tuning RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Use Case 분석
→ RAG / Prompt / Fine-Tuning 선택
→ Dataset 설계
→ Dataset Cleaning
→ Training Method 선택
→ Fine-Tuning 실행
→ Evaluation
→ Safety / Regression Test
→ Deployment Review
→ Monitoring
```

문서 품질은 Fine-Tuning 적용 판단 정확도, 데이터 품질 검증력, 평가 기준 명확성, 안전성 검토 가능성으로 결정된다.

---

### [FAQ]

Q. Fine-Tuning Domain Rules의 최종 목적은?

A. Agent가 Fine-Tuning 적용 여부, 데이터셋 품질, 학습 방식, 평가 기준, 배포 가능성을 판단할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Fine-Tuning 운영 판단 품질을 높이기 위한 문서이다.

Q. Fine-Tuning 문서 품질은 무엇으로 판단하는가?

A. Agent가 Fine-Tuning을 오용하지 않고, 적합한 상황에서 데이터와 평가 기준을 갖춘 상태로 적용할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Fine-Tuning이란?
A. 기존 모델에 특정 목적의 데이터셋을 추가 학습시켜 응답 패턴, 스타일, 형식, 작업 수행 방식을 조정하는 기법이다.

Q. Fine-Tuning과 RAG의 차이는?
A. Fine-Tuning은 모델 행동을 조정하고, RAG는 외부 지식을 검색해 답변 근거로 제공한다.

Q. Fine-Tuning과 Prompt Engineering의 차이는?
A. Prompt Engineering은 입력 지시를 조정하고, Fine-Tuning은 학습을 통해 모델 응답 패턴을 조정한다.

Q. Fine-Tuning은 언제 필요한가?
A. 반복되는 출력 형식, 작업 절차, 도메인 응답 스타일, 분류 패턴을 안정화해야 할 때 필요하다.

Q. Fine-Tuning이 적합하지 않은 경우는?
A. 최신 정보 반영, 문서 근거 답변, 자주 바뀌는 지식, 데이터가 적은 작업, Prompt로 충분한 작업에는 적합하지 않다.

Q. Fine-Tuning은 RAG를 대체하는가?
A. 아니다. Fine-Tuning은 행동 조정에 강하고 RAG는 외부 지식 검색과 근거 제공에 강하다.

Q. RAG와 Fine-Tuning을 함께 사용할 수 있는가?
A. 가능하다. 지식은 RAG로 제공하고 출력 형식이나 작업 패턴은 Fine-Tuning으로 안정화할 수 있다.

Q. Fine-Tuning Dataset에서 가장 중요한 것은?
A. 목적에 맞는 고품질 입력 / 출력 쌍과 일관된 형식이다.

Q. Dataset Cleaning은 왜 필요한가?
A. 모델은 데이터의 오류와 불일치도 학습하므로 중복, 오답, 개인정보, 형식 오류를 제거해야 한다.

Q. Dataset Format은 왜 중요한가?
A. 모델이 입력과 출력 구조를 학습하므로 형식이 흔들리면 추론 결과도 불안정해진다.

Q. Train / Validation / Test Split은 왜 필요한가?
A. 학습, 튜닝, 최종 평가를 분리해야 Fine-Tuning 성능을 신뢰할 수 있기 때문이다.

Q. Data Leakage란?
A. 평가 데이터가 학습 데이터에 포함되어 실제보다 성능이 높게 측정되는 문제이다.

Q. LoRA란?
A. 전체 모델을 모두 학습하지 않고 작은 Adapter 행렬을 학습해 효율적으로 모델 행동을 조정하는 방식이다.

Q. QLoRA란?
A. 양자화된 모델 위에서 LoRA 학습을 수행해 VRAM 사용량을 줄이는 방식이다.

Q. Full Fine-Tuning은 언제 필요한가?
A. 대규모 고품질 데이터와 충분한 자원이 있고 모델 행동을 크게 바꿔야 할 때 검토한다.

Q. Hyperparameter에는 무엇이 있는가?
A. learningRate, batchSize, epoch, maxSequenceLength, loraRank, loraAlpha, loraDropout 등이 있다.

Q. Fine-Tuning Evaluation은 왜 필요한가?
A. Fine-Tuning이 실제로 개선을 만들었는지 확인하지 않으면 비용만 들고 성능이 나빠질 수 있기 때문이다.

Q. Overfitting이란?
A. 모델이 학습 데이터에는 잘 맞지만 새로운 입력에는 일반화하지 못하는 상태이다.

Q. Catastrophic Forgetting이란?
A. Fine-Tuning 후 모델이 기존에 잘하던 일반 능력이나 다른 작업 능력을 잃는 현상이다.

Q. Fine-Tuning 데이터에 개인정보를 넣어도 되는가?
A. 안 된다. 개인정보, 민감정보, API Key, Password, Token은 제거하거나 비식별화해야 한다.

Q. Fine-Tuned Model 배포 전 확인할 것은?
A. Evaluation, Regression Test, Safety Test, RAG 연동, Output Format, Rollback 계획, Monitoring 설정을 확인해야 한다.

Q. Fine-Tuning Observability는 무엇인가?
A. 학습 데이터, 학습 설정, 평가 결과, 배포 후 성능 변화를 추적하는 구조이다.

Q. Fine-Tuning에서 흔한 실패는?
A. 학습 효과 없음, 출력 형식 불안정, Overfitting, Catastrophic Forgetting, Hallucination 증가, 데이터 품질 저하이다.

Q. Fine-Tuning 문서 분할은 어떻게 하는가?
A. Core, Use Case, Dataset, Format, Training Method, Hyperparameter, Evaluation/Safety, Deployment/Troubleshooting으로 분리한다.

Q. Fine-Tuning 문서에서 피해야 할 것은?
A. RAG와 구분하지 않고, 데이터 품질과 평가 기준 없이 Fine-Tuning을 만능 해결책처럼 설명하는 것이다.

Q. Fine-Tuning Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

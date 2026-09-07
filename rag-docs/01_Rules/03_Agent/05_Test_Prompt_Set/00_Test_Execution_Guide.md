# 00. 테스트 실행 가이드

## 1. 테스트 전 준비

아래 문서가 Agent에 적용되어 있어야 합니다.

- Agent Rules v1
- Agent System Prompts v1
- Agent RAG Mapping v1
- Agent Workflow v1
- Foundation RAG
- Master Rules / Project Progress / Operation Rules

## 2. 테스트 방법

각 테스트 프롬프트를 PM Agent에 입력합니다.

PM Agent는 요청을 분석한 뒤 필요한 Agent 실행 순서를 정해야 합니다.

기본 실행 방식은 순차 실행입니다.

```text
User Request
↓
PM Agent
↓
필요 Agent 순차 실행
↓
Review Agent
↓
Final Answer
```

## 3. 사람이 확인해야 하는 항목

테스트 결과는 초기에는 사람이 직접 확인해야 합니다.

확인 기준:

```text
1. Routing 정확도
2. RAG 참조 적절성
3. Agent 책임 범위 준수
4. Handoff 정보 누락 여부
5. 최종 출력 품질
6. Review 품질
7. RAG Update Candidate 생성 여부
```

## 4. 판정 기준

### PASS

- 예상 Agent 흐름과 거의 일치
- 불필요한 Agent 호출이 없음
- 결과물이 실제 운영에 사용할 수 있음
- Review Agent가 최소 체크리스트를 수행함

### PARTIAL

- Agent 흐름은 대체로 맞지만 일부 누락 또는 과잉 호출 발생
- 결과물은 쓸 수 있으나 보완 필요
- Review가 형식적으로만 수행됨
- RAG 부족 감지가 약함

### FAIL

- 요청 분류가 틀림
- 필요한 Agent를 생략함
- 불필요한 Agent를 반복 호출함
- RAG와 다른 내용을 추측으로 생성함
- Review 없이 최종 답변을 냄

## 5. 튜닝 방식

문제가 발견되면 아래 순서로 수정 대상을 판단합니다.

```text
PM 라우팅 문제 → PM System Prompt / Routing Map 수정
Agent 책임 범위 문제 → Agent Rules 수정
RAG 참조 문제 → Agent RAG Mapping 수정
작업 순서 문제 → Agent Workflow 수정
검토 누락 문제 → Review Agent Rules / Prompt 수정
문서 부족 반복 → RAG Update Candidate로 등록
```

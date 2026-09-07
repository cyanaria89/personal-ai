# Agent Test Prompt Set v1 KR

이 문서는 개인 AI 프로젝트의 Agent 구조가 정상적으로 동작하는지 확인하기 위한 **한국어 테스트 프롬프트 세트**입니다.

## 목적

Agent Rules, System Prompt, RAG Mapping, Workflow를 적용한 뒤 실제 요청을 넣어보고 다음 항목을 검증합니다.

- PM Agent가 요청을 올바르게 분류하는가
- 필요한 Agent만 순차 실행되는가
- DB / Backend / Frontend Agent가 각자 책임 범위를 지키는가
- Agent 간 전달 정보가 누락되지 않는가
- Review Agent가 누락, 충돌, 규칙 위반을 잡는가
- RAG 문서 부족 시 Update Candidate를 생성하는가
- 추후 Expert Agent로 분리할 후보를 식별하는가

## 추천 1차 테스트

처음에는 아래 5개만 먼저 실행해도 됩니다.

1. DB-01
2. BE-01
3. FE-01
4. FULL-01
5. RAG-01

## 결과 판정

- PASS: 기대 흐름과 결과 품질을 대부분 만족
- PARTIAL: 큰 방향은 맞지만 누락, 과잉 호출, 형식 오류 등이 있음
- FAIL: Agent 선택, RAG 참조, 결과 품질 중 핵심 항목이 틀림

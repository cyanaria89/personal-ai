# Local Fullstack Multi-Agent AI

로컬 LLM으로 요구사항 분석부터 DB, Backend, Frontend 산출물 생성과 통합 검토까지 수행하는 LangGraph 기반 멀티 에이전트 프로젝트입니다. 일반 기술 지식인 Domain RAG와 실제 대상 프로젝트의 현재 상태인 Project Context를 분리하여, 이전 구현을 읽고 이어서 개발하는 흐름을 실험하기 위해 만들었습니다.

현재 시스템은 생성 결과를 Markdown으로 저장하는 **읽기 전용 코드 생성 파이프라인**입니다. 대상 프로젝트 파일에 결과를 자동 적용하거나 빌드·배포하는 기능은 아직 구현하지 않았습니다.

## 기술과 실행 환경

- Python 3.14.4 (현재 검증 환경)
- LangGraph 1.2.10, LangChain Ollama 1.1.0
- Ollama + Qwen2.5-Coder 14B
- BGE-M3 임베딩 기반 로컬 DB RAG
- 생성 대상 기술: Spring Boot 3 / JPA / SQL / React / TypeScript
- 기본 실행은 로컬 전용이며 외부 LLM API를 요구하지 않습니다.

## 디렉터리 구조

```text
personal-ai/
├── langgraph-agent/          # LangGraph 워크플로, 에이전트, 검증기, 테스트
│   ├── agents/               # PM/DB/Backend/Frontend/Review 노드
│   ├── graph/                # 그래프 구성과 조건부 라우팅
│   ├── project_context/      # 대상 프로젝트 탐색·선택·projection
│   ├── prompts/              # 프롬프트 로더와 RAG 문서 링크
│   ├── rag/                  # DB RAG 검색 및 로컬 인덱스 생성
│   ├── validators/           # 산출물 및 통합 정적 검증
│   ├── tests/                # 단위·통합·회귀 테스트
│   ├── data/                 # Rules/RAG 원본을 가리키는 상대 심볼릭 링크
│   └── outputs/              # 실행 결과와 metrics
├── rag-docs/                 # Agent Rules, System Prompt, Domain 지식 원본
└── context-test-project/     # 연속 개발 검증용 최소 Fullstack fixture
```

## 에이전트 역할과 실행 흐름

- **PM**: 사용자 요청을 분석하고 필요한 DB/Backend/Frontend 에이전트를 선택합니다.
- **DB**: 스키마와 SQL 산출물을 생성합니다.
- **Backend**: Spring Boot 계층과 API 산출물을 생성합니다.
- **Frontend**: React/TypeScript UI와 API 연동 산출물을 생성합니다.
- **Review**: 선택된 에이전트 결과를 함께 검토하고 최종 PASS/FAIL을 판정합니다.

```text
START
  → Project Context snapshot
  → PM
  → 선택된 DB / Backend / Frontend
  → 각 산출물 Validator 및 제한된 Fix Loop
  → Integration Validator
  → Review
  → Markdown 결과 + JSON metrics
```

Project Context는 workflow 시작 시 한 번만 수집합니다. 디렉터리 트리와 요청 키워드·심볼·파일명 기반으로 관련 파일을 제한적으로 선택하고, 에이전트별로 필요한 내용만 projection합니다. `.env`, 의존성 디렉터리, 빌드 산출물 등은 탐색에서 제외되며 대상 프로젝트는 수정하지 않습니다.

## 검증과 Fix Loop

각 전문 에이전트 뒤의 deterministic validator가 필수 파일, 계층 간 계약, 응답 구조 등 정적으로 확인 가능한 규칙을 검사합니다. 수정 가능한 문제는 제한된 auto-fix 또는 LLM fix pass로 다시 검증하며, 반복 횟수 제한으로 무한 루프를 방지합니다. Integration Validator는 Backend API와 Frontend 호출의 method/path/status 등 교차 계층 계약을 확인합니다.

Review의 Evidence Validation은 생성 산출물 안에서 확인 가능한 근거를 요구합니다. Project Context는 기존 구현을 재사용하기 위한 입력이며, 생성하지 않은 코드가 결과에 포함된 것처럼 주장하는 근거로 사용하지 않습니다.

## Domain RAG와 Project Context

- **Domain RAG**: Spring Boot, SQL 등 재사용 가능한 일반 기술 지식을 로컬 임베딩 검색으로 제공합니다. 현재 DB 에이전트 경로에 연결되어 있으며 Backend/Frontend는 RAG 문서를 직접 검색하는 단계가 아직 연결되지 않았습니다.
- **Project Context**: 실행 시 지정한 실제 프로젝트의 현재 소스 구조와 관련 파일을 읽습니다. 전체 저장소를 프롬프트에 넣지 않고 bounded selection과 agent projection으로 로컬 모델의 context 사용량을 제한합니다.

`langgraph-agent/prompts/*/source`와 `langgraph-agent/data/*/source`는 `rag-docs/`의 원본을 가리키는 상대 심볼릭 링크입니다. 저장소를 함께 clone하면 개인 홈 디렉터리에 의존하지 않습니다. 심볼릭 링크 지원이 제한된 환경에서는 Git의 symlink 지원 설정을 확인해야 합니다.

## 설치 및 실행

Ollama를 설치하고 모델을 준비한 뒤 다음과 같이 실행합니다.

```bash
cd langgraph-agent
python3 -m venv .venv
source .venv/bin/activate
pip install langgraph==1.2.10 langchain-ollama==1.1.0 python-dotenv==1.2.2

ollama pull qwen2.5-coder:14b
ollama pull bge-m3
python rag/db_retriever.py
python main.py --project-root ../context-test-project
```

CLI에 요청을 입력하고, 입력 종료가 필요할 때 `END`를 사용합니다. Ollama 주소나 모델 설정을 환경 변수로 변경할 수 있으며 `.env`는 Git에서 제외됩니다. 생성되는 RAG 인덱스도 재생성 가능하므로 저장소에 포함하지 않습니다.

## 테스트

```bash
cd langgraph-agent
.venv/bin/python -m unittest discover -v
```

테스트는 그래프 구성, 라우팅, validator/fix loop, integration validation, metrics, Project Context의 탐색·보안 제외·budget 동작을 포함합니다. 실제 Qwen 호출은 일반 테스트와 분리되어 있으며 실행 시간과 로컬 자원을 별도로 사용합니다.

## 연속 개발 fixture

`context-test-project/`는 회원가입이 이미 구현된 최소 Spring Boot/React 형태의 테스트 대상입니다. `Member`, repository, signup DTO/service/controller, `PasswordEncoder`, 회원가입 페이지와 API 호출이 있고 로그인 기능은 의도적으로 없습니다. 무관한 `WeatherService`와 Git에서 제외되는 테스트용 `.env`도 두어, 로그인 요청 시 관련 파일 선택과 secret 제외를 확인할 수 있습니다. 이 fixture는 실행 애플리케이션 자체가 아니라 Project Context 동작을 재현하기 위한 소스 표본입니다.

## 최신 검증 증거

가장 최근의 최종 PASS 실행은 2026-08-26의 `로그인 기능 추가해줘` 요청입니다. PM이 Backend와 Frontend를 선택했고, Frontend fix pass 1회 후 Integration/Review를 통과했습니다.

- [최종 결과](langgraph-agent/outputs/agent_result_20260826_145148.md)
- [동일 실행 metrics](langgraph-agent/outputs/metrics/agent_metrics_20260826_145148_014628.json)

Metrics에는 PM, Backend, Frontend initial/fix, Review까지 5회의 LLM 호출과 각 단계의 context/predict 설정, prompt/eval token 수, 실행 시간이 기록되어 있습니다.

## 구현 상태와 향후 계획

현재 완료된 범위는 멀티 에이전트 라우팅, Markdown 산출물 생성, 계층별 validator와 fix loop, integration/evidence validation, 실행 metrics, DB Domain RAG, 읽기 전용 Project Context Loader입니다.

향후 과제는 Backend/Frontend Domain RAG 연결 확대, 생성 결과를 실제 파일 변경안으로 변환하는 안전한 patch/apply 계층, 적용 후 빌드·테스트 검증입니다. 이 항목들은 현재 완료 기능에 포함되지 않습니다.

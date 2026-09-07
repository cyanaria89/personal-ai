# MLOps Domain Rules

---

# 1. Domain Purpose

## 1.1 MLOps 문서 목적

### [개념]

MLOps Domain 문서는 AI Agent / AI/ML Agent / DevOps Agent / Backend Agent / Review Agent / Architecture Review Agent가 Machine Learning Model과 LLM 기반 시스템을 개발, 배포, 운영, 모니터링, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

MLOps는 Machine Learning과 DevOps를 결합한 운영 체계이다.

MLOps는 단순히 모델을 학습시키는 과정이 아니라, 데이터 준비, 실험 관리, 모델 학습, 평가, 배포, 모니터링, 재학습, 버전 관리, 장애 대응을 포함하는 전체 Model Lifecycle 운영 구조이다.

---

### [핵심]

- MLOps = ML Lifecycle + DevOps + Automation + Monitoring
- 모델 학습보다 운영 안정성이 중요
- Dataset Version 관리 필요
- Experiment Tracking 필요
- Model Registry 필요
- CI/CD Pipeline 필요
- Model Serving 기준 필요
- Monitoring / Logging 필요
- Data Drift / Model Drift 감지 필요
- Rollback 기준 필요
- 재학습 Pipeline 필요
- LLMOps / RAGOps와 연결 가능
- AI Agent 운영 품질과 직접 연결됨

---

### [실무]

2026 실무 기준 MLOps 문서는 다음 목적을 우선한다.

- ML / LLM Model Lifecycle 설계
- Dataset Version 관리 기준 제공
- Experiment Tracking 기준 제공
- Model Evaluation 기준 제공
- Model Registry 운영 기준 제공
- Model Serving 기준 제공
- CI/CD Pipeline 기준 제공
- Monitoring / Logging 기준 제공
- Drift Detection 기준 제공
- Rollback / Canary / A/B Test 기준 제공
- Retraining Pipeline 기준 제공
- AI Agent / RAG / LLM 운영 연계 기준 제공

MLOps 문서는 사람이 머신러닝 이론을 공부하기 위한 문서가 아니라, Agent가 모델 운영 시스템을 설계하고 검토할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. MLOps 문서는 무엇을 위한 문서인가?

A. Agent가 모델 학습, 평가, 배포, 모니터링, 재학습까지 전체 ML Lifecycle을 운영할 수 있도록 기준을 제공하는 문서이다.

Q. MLOps는 모델 학습만 의미하는가?

A. 아니다. 데이터, 실험, 모델, 배포, 모니터링, Drift, Rollback, 재학습까지 포함하는 운영 체계이다.

Q. MLOps에서 가장 중요한 것은?

A. 재현성, 버전 관리, 평가, 배포 안정성, 모니터링, 장애 대응이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

MLOps Domain 문서는 ML / LLM / RAG / Agent 시스템의 모델 운영과 Lifecycle 관리를 위한 개념, 구성 요소, Pipeline, 평가, 배포, 모니터링, 장애 대응 기준을 포함한다.

---

### [핵심]

포함 범위:

- MLOps 개념
- ML Lifecycle
- Data Pipeline
- Dataset Versioning
- Feature Store
- Experiment Tracking
- Training Pipeline
- Validation Pipeline
- Evaluation Pipeline
- Model Registry
- Model Versioning
- Model Serving
- Batch Inference
- Real-Time Inference
- CI/CD for ML
- CT
- Monitoring
- Logging
- Metrics
- Data Drift
- Model Drift
- Concept Drift
- Retraining Pipeline
- Rollback
- Canary Deployment
- A/B Testing
- Shadow Deployment
- Governance
- LLMOps
- RAGOps
- AgentOps

제외 범위:

- 머신러닝 알고리즘 수학 상세
- 딥러닝 모델 내부 구조 상세
- 특정 MLOps 플랫폼 API 전체 문서 복붙
- Kubernetes 운영 전체 상세
- 클라우드 벤더별 콘솔 사용법 중심 설명
- 모델 학습 코드만 나열하는 문서
- 단순 라이브러리 설치법 중심 문서
- 데이터 수집 윤리와 보안 기준 없는 Pipeline 설명

---

### [실무]

MLOps 문서는 아래 질문에 답할 수 있어야 한다.

- Dataset은 어떻게 버전 관리해야 하는가?
- 실험 결과는 어떻게 추적해야 하는가?
- 모델 평가는 어떤 기준으로 해야 하는가?
- 배포 가능한 모델 기준은 무엇인가?
- Model Registry는 어떻게 운영해야 하는가?
- 모델 배포 후 무엇을 모니터링해야 하는가?
- Drift는 어떻게 감지해야 하는가?
- 성능 저하가 발생하면 어떻게 Rollback해야 하는가?
- 재학습은 언제 트리거해야 하는가?
- LLM / RAG / Agent 시스템은 기존 MLOps와 어떻게 연결되는가?

---

### [FAQ]

Q. MLOps 문서에 ML 알고리즘 수학을 자세히 넣어야 하는가?

A. 아니다. Agent가 운영 Pipeline, 평가, 배포, 모니터링, 재학습을 판단할 수 있도록 작성한다.

Q. MLOps와 DevOps는 같은가?

A. 아니다. DevOps는 소프트웨어 배포 운영 중심이고, MLOps는 데이터와 모델 Lifecycle까지 포함한다.

Q. LLM 시스템에도 MLOps가 필요한가?

A. 필요하다. LLMOps, RAGOps, AgentOps도 MLOps 원칙을 확장해 모델, 데이터, 평가, 배포, 모니터링을 관리한다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

MLOps 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

Pipeline 흐름이 필요한 주제는 `[Flow]`를 추가한다.

운영 검증이 필요한 주제는 `[Checklist]`, `[Evaluation]`을 추가한다.

장애 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

배포 방식 비교가 필요한 주제는 `[Comparison]`을 추가한다.

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
- [Checklist]
- [Evaluation]
- [Troubleshooting]
- [Comparison]

Optional:

- [Pipeline]
- [Model Registry]
- [Monitoring Metric]
- [Deployment Strategy]
- [Review Point]
- [Anti-Pattern]

---

### [실무]

MLOps 문서는 단순 개념 설명보다 운영 기준과 검증 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Pipeline Flow
- Versioning 기준
- Evaluation 기준
- Deployment 기준
- Monitoring Metric
- Drift Detection 기준
- Rollback 기준
- Retraining 기준
- Troubleshooting 기준
- Review Checklist

---

### [FAQ]

Q. MLOps 문서에 Flow는 필수인가?

A. Data Pipeline, Training Pipeline, Deployment Pipeline, Retraining Pipeline 주제에서는 필수이다.

Q. Evaluation 섹션은 왜 필요한가?

A. 모델은 배포 전 정량 / 정성 평가를 통과해야 하며, 평가 기준이 없으면 품질을 보장할 수 없기 때문이다.

Q. Troubleshooting 섹션이 필요한 이유는?

A. 모델 운영에서는 Drift, 성능 저하, 배포 실패, 데이터 오류가 자주 발생하기 때문이다.

---

# 4. Core Concept Rules

## 4.1 MLOps 핵심 개념 작성 규칙

### [개념]

MLOps 핵심 개념은 DevOps, DataOps, LLMOps, RAGOps, AgentOps와 구분되도록 작성한다.

MLOps는 모델을 만드는 과정이 아니라 모델을 안정적으로 운영하는 전체 Lifecycle 관리 체계이다.

---

### [핵심]

반드시 포함할 개념:

- MLOps
- ML Lifecycle
- Data Pipeline
- Dataset Versioning
- Feature Store
- Experiment Tracking
- Training Pipeline
- Evaluation Pipeline
- Model Registry
- Model Serving
- CI/CD
- Continuous Training
- Monitoring
- Data Drift
- Model Drift
- Concept Drift
- Retraining
- Rollback
- Governance
- LLMOps
- RAGOps
- AgentOps

용어 통일:

- MLOps
- ML Lifecycle
- Dataset Versioning
- Experiment Tracking
- Model Registry
- Model Serving
- Continuous Training
- Data Drift
- Model Drift
- Concept Drift
- Retraining Pipeline
- Model Rollback
- LLMOps
- RAGOps
- AgentOps

---

### [실무]

MLOps 설명은 아래 구분을 반드시 포함한다.

```text
DevOps
→ 애플리케이션 빌드, 배포, 운영 자동화

DataOps
→ 데이터 수집, 정제, 품질, Pipeline 운영

MLOps
→ 데이터, 실험, 모델, 평가, 배포, 모니터링, 재학습 운영

LLMOps
→ LLM Prompt, Fine-Tuning, Evaluation, Serving, Safety 운영

RAGOps
→ Retrieval, Vector DB, Chunk, Embedding, Grounding 품질 운영

AgentOps
→ Agent Workflow, Tool Calling, State, Trace, Evaluation 운영
```

MLOps 문서는 “모델을 배포한다” 수준에서 멈추면 안 된다.

Agent가 데이터부터 배포 후 재학습까지 전체 흐름을 판단할 수 있어야 한다.

---

### [FAQ]

Q. MLOps란?

A. ML 모델의 데이터, 실험, 학습, 평가, 배포, 모니터링, 재학습을 운영하는 Lifecycle 관리 체계이다.

Q. MLOps와 DevOps의 차이는?

A. DevOps는 애플리케이션 운영 중심이고, MLOps는 데이터와 모델 Lifecycle 관리까지 포함한다.

Q. MLOps와 LLMOps의 관계는?

A. LLMOps는 LLM 운영에 특화된 MLOps 확장 영역이다.

---

# 5. ML Lifecycle Rules

## 5.1 ML Lifecycle 작성 규칙

### [개념]

ML Lifecycle은 모델이 데이터 준비부터 운영 후 개선까지 거치는 전체 흐름이다.

MLOps 문서는 Lifecycle 각 단계의 입력, 출력, 검증 기준을 명확히 작성해야 한다.

---

### [핵심]

기본 ML Lifecycle:

```text
Problem Definition
→ Data Collection
→ Data Validation
→ Feature Engineering
→ Dataset Versioning
→ Experiment Tracking
→ Model Training
→ Model Evaluation
→ Model Registry
→ Model Deployment
→ Model Monitoring
→ Drift Detection
→ Retraining
→ Rollback or Promotion
```

단계별 작성 요소:

- 단계 목적
- 입력 데이터
- 출력 산출물
- 검증 기준
- 실패 조건
- 다음 단계 이동 기준

---

### [실무]

ML Lifecycle 문서는 아래 형식을 권장한다.

```md
### [Flow]

Problem Definition
→ Data Pipeline
→ Training Pipeline
→ Evaluation
→ Registry
→ Deployment
→ Monitoring
→ Retraining

입력:

- rawData
- trainingConfig
- evaluationDataset

출력:

- trainedModel
- evaluationReport
- modelVersion
- deploymentStatus
```

Lifecycle 문서는 Agent가 Pipeline 누락을 검토할 수 있도록 작성한다.

---

### [FAQ]

Q. ML Lifecycle은 왜 중요한가?

A. 모델 개발과 운영은 일회성 작업이 아니라 데이터 변경, 모델 변경, 재평가, 재배포가 반복되는 과정이기 때문이다.

Q. ML Lifecycle에서 가장 자주 누락되는 단계는?

A. Dataset Versioning, Evaluation, Monitoring, Drift Detection, Rollback이 자주 누락된다.

Q. 모델 학습이 끝나면 Lifecycle도 끝나는가?

A. 아니다. 배포 후 모니터링, Drift 감지, 재학습, Rollback까지 포함해야 한다.

---

# 6. Data Pipeline Rules

## 6.1 Data Pipeline 작성 규칙

### [개념]

Data Pipeline은 모델 학습과 평가에 사용할 데이터를 수집, 정제, 검증, 변환, 저장하는 흐름이다.

MLOps에서 데이터 품질은 모델 품질의 핵심이다.

---

### [핵심]

Data Pipeline 구성 요소:

- Data Source
- Data Ingestion
- Data Validation
- Data Cleaning
- Data Transformation
- Feature Engineering
- Dataset Versioning
- Data Quality Check
- Data Lineage
- Data Access Control

검증 항목:

- Schema 일치
- Null 비율
- 중복 데이터
- 이상치
- Label 품질
- 데이터 분포
- 데이터 누수
- 개인정보 포함 여부
- 학습 / 평가 데이터 분리

---

### [실무]

Data Pipeline Flow:

```text
Raw Data
→ Ingestion
→ Schema Validation
→ Cleaning
→ Transformation
→ Feature Engineering
→ Dataset Versioning
→ Train / Validation / Test Split
→ Training Pipeline
```

Data Validation Checklist:

```md
### [Checklist]

- 데이터 Schema가 기대값과 일치하는가?
- Null / Missing 값이 허용 범위 안인가?
- 중복 데이터가 제거되었는가?
- Label이 올바른가?
- Train / Test Data Leakage가 없는가?
- 개인정보와 민감정보가 제거되었는가?
- Dataset Version이 기록되었는가?
```

---

### [FAQ]

Q. Data Pipeline은 왜 중요한가?

A. 잘못된 데이터로 학습하면 모델이 잘못된 패턴을 학습하고 운영 중 성능 문제가 발생하기 때문이다.

Q. Data Validation은 언제 수행해야 하는가?

A. 데이터 수집 후, 변환 후, 학습 전, 재학습 전마다 수행해야 한다.

Q. Data Leakage란?

A. 평가 데이터나 미래 정보가 학습 데이터에 섞여 모델 성능이 실제보다 높게 측정되는 문제이다.

---

# 7. Dataset Versioning Rules

## 7.1 Dataset Versioning 작성 규칙

### [개념]

Dataset Versioning은 학습, 검증, 테스트에 사용한 데이터셋의 버전과 변경 이력을 관리하는 과정이다.

모델 성능을 재현하려면 코드 버전뿐 아니라 데이터 버전도 추적해야 한다.

---

### [핵심]

Dataset Version 관리 대상:

- Raw Data Version
- Cleaned Data Version
- Feature Dataset Version
- Training Dataset Version
- Validation Dataset Version
- Test Dataset Version
- Label Version
- Data Schema Version
- Data Split Version

기록 항목:

- datasetId
- version
- source
- createdAt
- schema
- rowCount
- featureList
- labelDefinition
- splitRule
- preprocessingRule
- owner
- qualityReport

---

### [실무]

Dataset Version 예시:

```text
datasetId: rag-eval-dataset
version: v1.2
source: RAG document QA set
rowCount: 1200
splitRule: train 80 / validation 10 / test 10
labelDefinition: expectedAnswer + sourceChunk
qualityReport: passed
```

Dataset Version이 없으면 모델 성능 악화 원인을 추적하기 어렵다.

모델 버전은 반드시 Dataset Version과 연결한다.

---

### [FAQ]

Q. Dataset Versioning은 왜 필요한가?

A. 어떤 데이터로 학습한 모델인지 알아야 성능 재현, 비교, Rollback, 장애 분석이 가능하기 때문이다.

Q. Raw Data와 Training Dataset을 모두 버전 관리해야 하는가?

A. 가능하면 둘 다 관리해야 한다. 원본 데이터와 전처리 후 학습 데이터는 다를 수 있기 때문이다.

Q. Dataset Version과 Model Version은 연결해야 하는가?

A. 반드시 연결해야 한다. 모델 성능은 학습 데이터에 크게 의존하기 때문이다.

---

# 8. Experiment Tracking Rules

## 8.1 Experiment Tracking 작성 규칙

### [개념]

Experiment Tracking은 모델 학습 실험의 설정, 데이터, 코드, 결과, Metric을 기록하고 비교하는 과정이다.

실험 추적이 없으면 어떤 변경이 성능 개선이나 악화를 만들었는지 알 수 없다.

---

### [핵심]

Tracking 대상:

- experimentId
- runId
- modelName
- modelVersion
- datasetVersion
- codeVersion
- trainingConfig
- hyperparameters
- metrics
- artifacts
- logs
- evaluationReport
- notes
- owner
- status

Tracking Metric 예시:

- accuracy
- precision
- recall
- f1
- auc
- rmse
- mae
- loss
- latency
- throughput
- memoryUsage
- hallucinationRate
- groundedness
- formatCompliance

---

### [실무]

Experiment Tracking 예시:

```text
experimentId: EXP-RAG-001
runId: RUN-0007
modelName: qwen2.5-14b
datasetVersion: rag-eval-v1.2
config: contextLength=20000, topK=10
metric: groundedness=0.92, formatCompliance=0.97
status: candidate
```

Experiment Tracking은 모델 성능 비교와 배포 후보 선정의 근거가 된다.

LLM / RAG / Agent 시스템에서는 정량 Metric과 Human Evaluation 결과를 함께 기록한다.

---

### [FAQ]

Q. Experiment Tracking은 왜 필요한가?

A. 데이터, 코드, 설정, 평가 결과를 추적해야 어떤 실험이 성능 개선을 만들었는지 알 수 있기 때문이다.

Q. Hyperparameter도 기록해야 하는가?

A. 반드시 기록해야 한다. 같은 모델과 데이터도 설정에 따라 결과가 달라진다.

Q. LLM 실험도 Experiment Tracking이 필요한가?

A. 필요하다. Prompt, RAG 설정, Model Version, Evaluation 결과를 추적해야 한다.

---

# 9. Training Pipeline Rules

## 9.1 Training Pipeline 작성 규칙

### [개념]

Training Pipeline은 데이터 준비부터 모델 학습, 검증, Artifact 저장까지 자동화된 학습 흐름이다.

Training Pipeline은 재현 가능해야 하며, Dataset Version과 Experiment Tracking과 연결되어야 한다.

---

### [핵심]

Training Pipeline 단계:

```text
Load Dataset
→ Validate Dataset
→ Preprocess
→ Train / Validation Split
→ Train Model
→ Validate Model
→ Save Artifact
→ Log Experiment
→ Register Candidate Model
```

필수 기준:

- Dataset Version 입력
- Code Version 기록
- Config Version 기록
- Random Seed 관리
- Hyperparameter 기록
- Training Log 저장
- Validation Metric 저장
- Artifact 저장
- 실패 시 Error Log 저장

---

### [실무]

Training Pipeline Checklist:

```md
### [Checklist]

- Dataset Version이 명시되었는가?
- 학습 Config가 저장되었는가?
- Random Seed가 관리되는가?
- Validation Metric이 기록되는가?
- Model Artifact가 저장되는가?
- Experiment Tracking에 연결되었는가?
- 실패 시 원인을 추적할 수 있는가?
```

Training Pipeline은 수동 노트북 실행에 의존하지 않도록 설계한다.

개인 프로젝트에서는 처음에는 단순 Script 기반으로 시작하되, Dataset / Config / Result 기록은 반드시 남긴다.

---

### [FAQ]

Q. Training Pipeline은 왜 필요한가?

A. 모델 학습을 재현하고, 실험 결과를 비교하고, 배포 가능한 Artifact를 일관되게 만들기 위해 필요하다.

Q. 수동으로 학습해도 되는가?

A. 초기 실험은 가능하지만 운영 모델은 Pipeline으로 재현 가능해야 한다.

Q. Random Seed를 기록해야 하는가?

A. 기록해야 한다. 재현성과 실험 비교에 중요하다.

---

# 10. Evaluation Pipeline Rules

## 10.1 Evaluation Pipeline 작성 규칙

### [개념]

Evaluation Pipeline은 학습된 모델 또는 배포 후보 모델이 품질 기준을 만족하는지 자동 또는 반자동으로 평가하는 흐름이다.

MLOps에서 Evaluation은 배포 승인 기준이다.

---

### [핵심]

Evaluation 대상:

- Model Accuracy
- Model Loss
- Task Metric
- Latency
- Throughput
- Memory Usage
- Robustness
- Safety
- Bias
- Regression
- Data Slice Performance
- LLM Response Quality
- RAG Groundedness
- Agent Workflow Success Rate

Evaluation 유형:

- Offline Evaluation
- Online Evaluation
- Human Evaluation
- Regression Test
- Shadow Evaluation
- A/B Test

---

### [실무]

Evaluation Pipeline Flow:

```text
Candidate Model
→ Load Evaluation Dataset
→ Run Evaluation
→ Compare Baseline
→ Generate Evaluation Report
→ Pass / Fail Decision
→ Register or Reject Model
```

Evaluation Checklist:

```md
### [Checklist]

- Baseline Model과 비교했는가?
- Test Dataset은 학습에 사용되지 않았는가?
- 주요 Metric이 기준값을 넘었는가?
- Regression Test를 통과했는가?
- Latency와 Cost가 허용 범위인가?
- Safety Test를 통과했는가?
- 배포 승인 기준이 명확한가?
```

---

### [FAQ]

Q. Evaluation Pipeline은 왜 필요한가?

A. 모델이 배포 기준을 만족하는지 일관되게 검증해야 하기 때문이다.

Q. Baseline과 비교해야 하는가?

A. 반드시 비교해야 한다. 새 모델이 기존 모델보다 나아졌는지 확인해야 한다.

Q. LLM Evaluation은 어떻게 다른가?

A. 정답 정확도뿐 아니라 Groundedness, Hallucination, Format Compliance, Human Preference도 평가해야 한다.

---

# 11. Model Registry Rules

## 11.1 Model Registry 작성 규칙

### [개념]

Model Registry는 학습된 모델 Artifact, 버전, 평가 결과, 배포 상태, 승인 이력을 관리하는 저장소이다.

Model Registry는 배포 가능한 모델과 실험용 모델을 구분하는 기준점이다.

---

### [핵심]

Model Registry 기록 항목:

- modelId
- modelName
- modelVersion
- baseModel
- datasetVersion
- codeVersion
- trainingConfig
- evaluationResult
- artifactLocation
- approvalStatus
- deploymentStatus
- owner
- createdAt
- updatedAt
- rollbackTarget
- changelog

Model Stage:

- experimental
- candidate
- staging
- production
- deprecated
- archived
- rejected

---

### [실무]

Model Registry 예시:

```text
modelName: rag-answer-model
modelVersion: v2.1
baseModel: qwen2.5-14b
datasetVersion: rag-eval-v1.2
stage: staging
evaluationStatus: passed
deploymentStatus: canary
rollbackTarget: v2.0
```

Model Registry는 배포 자동화와 Rollback의 기준이 된다.

평가 결과가 없는 모델은 production으로 승격하지 않는다.

---

### [FAQ]

Q. Model Registry는 왜 필요한가?

A. 어떤 모델이 어떤 데이터와 설정으로 만들어졌고, 어떤 평가를 통과했으며, 어디에 배포되었는지 관리하기 위해 필요하다.

Q. Model Registry와 파일 저장소는 같은가?

A. 아니다. 파일 저장소는 Artifact를 보관하고, Model Registry는 버전, 상태, 평가, 승인 정보를 관리한다.

Q. 평가 결과 없는 모델을 배포해도 되는가?

A. 권장하지 않는다. production 승격은 Evaluation 통과 후 수행해야 한다.

---

# 12. Model Serving Rules

## 12.1 Model Serving 작성 규칙

### [개념]

Model Serving은 학습된 모델을 API, Batch Job, Streaming, Agent Runtime에서 사용할 수 있도록 배포하고 추론 요청을 처리하는 구조이다.

MLOps 문서는 Serving 방식과 운영 기준을 명확히 작성해야 한다.

---

### [핵심]

Serving 유형:

- Real-Time Inference
- Batch Inference
- Streaming Inference
- Async Inference
- Edge Serving
- Local Serving
- Model API Serving
- Embedding Serving
- LLM Serving

Serving 기준:

- latency
- throughput
- concurrency
- memoryUsage
- gpuUsage
- cpuUsage
- timeout
- retryPolicy
- rateLimit
- scalingPolicy
- healthCheck
- fallbackModel

---

### [실무]

Model Serving Flow:

```text
Client Request
→ API Gateway
→ Preprocessing
→ Model Inference
→ Postprocessing
→ Response
→ Logging
→ Monitoring
```

Serving Checklist:

```md
### [Checklist]

- Model Version이 명확한가?
- Health Check가 있는가?
- Timeout 기준이 있는가?
- 오류 시 Fallback이 있는가?
- 추론 요청과 응답이 Logging되는가?
- Latency와 Throughput을 모니터링하는가?
- Scale-out 기준이 있는가?
```

LLM Serving에서는 Context Length, Token Throughput, Streaming, Tool Calling 출력 형식도 평가한다.

---

### [FAQ]

Q. Model Serving은 무엇인가?

A. 학습된 모델을 API나 Pipeline에서 호출 가능하게 배포하고 추론 요청을 처리하는 구조이다.

Q. Real-Time Inference와 Batch Inference의 차이는?

A. Real-Time은 즉시 응답이 필요하고, Batch는 대량 데이터를 일정 단위로 처리한다.

Q. LLM Serving에서 추가로 봐야 할 것은?

A. Context Length, Token 속도, Streaming, Tool Calling 형식, 메모리 사용량을 봐야 한다.

---

# 13. CI/CD and CT Rules

## 13.1 ML CI/CD / Continuous Training 작성 규칙

### [개념]

ML CI/CD는 모델 코드, 데이터 Pipeline, 학습 Pipeline, 평가 Pipeline, 배포 Pipeline을 자동화하는 구조이다.

CT는 Continuous Training으로, 데이터 변화나 성능 저하에 따라 모델을 자동 또는 반자동으로 재학습하는 구조이다.

---

### [핵심]

CI 대상:

- Code Test
- Data Validation
- Pipeline Test
- Config Validation
- Unit Test
- Integration Test
- Model Smoke Test

CD 대상:

- Model Packaging
- Model Registry Update
- Staging Deployment
- Canary Deployment
- Production Deployment
- Rollback

CT 대상:

- New Data Trigger
- Drift Trigger
- Performance Drop Trigger
- Scheduled Retraining
- Manual Approval Retraining

---

### [실무]

ML CI/CD Flow:

```text
Code / Data Change
→ CI Validation
→ Training Pipeline
→ Evaluation Pipeline
→ Model Registry
→ Staging Deployment
→ Canary
→ Production
→ Monitoring
```

CT Flow:

```text
Monitoring
→ Drift or Performance Drop Detected
→ Retraining Trigger
→ Training Pipeline
→ Evaluation
→ Approval
→ Deployment
```

모든 재학습을 자동 배포로 연결하지 않는다.

Evaluation과 승인 기준을 반드시 둔다.

---

### [FAQ]

Q. MLOps에서 CI/CD는 일반 DevOps와 무엇이 다른가?

A. 코드뿐 아니라 데이터, 모델, 평가 결과, Artifact까지 Pipeline에 포함된다.

Q. CT는 무엇인가?

A. Continuous Training으로, 데이터 변화나 성능 저하에 따라 모델을 재학습하는 운영 구조이다.

Q. 재학습된 모델은 자동으로 Production에 배포해도 되는가?

A. 권장하지 않는다. Evaluation과 승인 기준을 통과해야 한다.

---

# 14. Monitoring Rules

## 14.1 Model Monitoring 작성 규칙

### [개념]

Model Monitoring은 배포된 모델의 성능, 입력 데이터, 출력 결과, 시스템 상태, 오류, 사용자 피드백을 지속적으로 관측하는 과정이다.

MLOps에서는 배포 후 모니터링이 모델 품질 유지의 핵심이다.

---

### [핵심]

Monitoring 대상:

- Prediction Quality
- Input Distribution
- Output Distribution
- Data Drift
- Model Drift
- Concept Drift
- Latency
- Throughput
- Error Rate
- Timeout Rate
- Resource Usage
- Memory Usage
- GPU Usage
- Cost
- User Feedback
- Safety Violation
- Hallucination Rate
- RAG Groundedness
- Agent Success Rate

---

### [실무]

Monitoring Metric 예시:

```text
System Metric:
- latency
- throughput
- errorRate
- memoryUsage
- gpuUsage

Model Metric:
- accuracy
- f1
- rmse
- calibration
- predictionDistribution

LLM / RAG Metric:
- groundedness
- hallucinationRate
- retrievalHitRate
- answerCompleteness
- formatCompliance

Agent Metric:
- workflowSuccessRate
- toolCallErrorRate
- retryCount
- reviewFailureRate
```

모니터링은 단순 서버 상태만 보면 안 된다.

모델 품질과 데이터 변화까지 함께 관측해야 한다.

---

### [FAQ]

Q. Model Monitoring은 왜 필요한가?

A. 배포 후 데이터와 사용자 행동이 변하면 모델 성능이 떨어질 수 있기 때문이다.

Q. 서버 Metric만 모니터링하면 충분한가?

A. 아니다. Data Drift, Model Drift, Prediction Quality, RAG 품질, Agent 성공률도 봐야 한다.

Q. LLM 시스템에서는 무엇을 모니터링해야 하는가?

A. Hallucination, Groundedness, Format Compliance, Tool Calling Error, Latency, Cost를 모니터링해야 한다.

---

# 15. Drift Detection Rules

## 15.1 Data Drift / Model Drift 작성 규칙

### [개념]

Drift Detection은 운영 중 데이터 분포, 모델 성능, 실제 개념 관계가 학습 시점과 달라졌는지 감지하는 과정이다.

Drift는 모델 성능 저하와 재학습 필요성을 판단하는 핵심 신호이다.

---

### [핵심]

Drift 유형:

- Data Drift
- Model Drift
- Concept Drift
- Label Drift
- Feature Drift
- Prompt Drift
- Retrieval Drift
- User Behavior Drift

Drift 감지 대상:

- 입력 데이터 분포
- Feature 분포
- Label 분포
- Prediction 분포
- Error Rate
- User Feedback
- Retrieval Hit Rate
- Embedding Similarity 분포
- Prompt 응답 품질
- Agent Workflow 성공률

---

### [실무]

Drift Detection Flow:

```text
Production Data
→ Distribution Monitoring
→ Baseline Distribution Compare
→ Drift Score Calculation
→ Alert
→ Evaluation
→ Retraining Decision
```

LLM / RAG Drift 예시:

```text
Retrieval Drift:
- 기존 Query가 더 이상 적절한 문서를 찾지 못함
- Chunk 변경 후 검색 순위가 흔들림
- Embedding Model 변경 후 Top-K 품질 저하

Prompt Drift:
- Prompt 변경 후 출력 형식 준수율 저하
- Agent Tool Calling 형식 오류 증가
```

Drift 감지는 재학습 자동 실행이 아니라 재평가와 조치 판단의 트리거이다.

---

### [FAQ]

Q. Data Drift란?

A. 운영 입력 데이터 분포가 학습 데이터 분포와 달라지는 현상이다.

Q. Concept Drift란?

A. 입력과 정답 사이의 관계 자체가 시간에 따라 바뀌는 현상이다.

Q. Drift가 감지되면 바로 재학습해야 하는가?

A. 아니다. 먼저 평가와 원인 분석을 수행하고 재학습 여부를 판단해야 한다.

---

# 16. Deployment Strategy Rules

## 16.1 Model Deployment Strategy 작성 규칙

### [개념]

Model Deployment Strategy는 새 모델을 운영 환경에 안전하게 적용하는 방식이다.

모델은 코드보다 예측 품질 문제가 발생할 수 있으므로 단계적 배포와 Rollback 기준이 중요하다.

---

### [핵심]

배포 전략:

- Staging Deployment
- Canary Deployment
- Blue-Green Deployment
- A/B Testing
- Shadow Deployment
- Rolling Deployment
- Manual Approval Deployment

선택 기준:

- 위험 낮음 → Staging 후 배포
- 부분 사용자 테스트 → Canary
- 빠른 Rollback 필요 → Blue-Green
- 모델 성능 비교 → A/B Testing
- 운영 영향 없이 검증 → Shadow Deployment
- 고위험 모델 → Manual Approval

---

### [실무]

Deployment Flow:

```text
Candidate Model
→ Evaluation Passed
→ Registry Promotion
→ Staging Deployment
→ Canary or Shadow Test
→ Monitoring
→ Production Promotion
→ Rollback if Failure
```

Deployment Checklist:

```md
### [Checklist]

- Evaluation을 통과했는가?
- Model Registry에서 Stage가 갱신되었는가?
- Rollback Target이 존재하는가?
- Canary 기준이 명확한가?
- Monitoring Alert가 설정되었는가?
- 사용자 영향 범위가 제한되었는가?
```

모델 배포는 “성공적으로 실행됨”보다 “품질 기준을 유지함”이 중요하다.

---

### [FAQ]

Q. Canary Deployment는 무엇인가?

A. 새 모델을 일부 트래픽에만 적용해 품질과 안정성을 확인하는 배포 방식이다.

Q. Shadow Deployment는 무엇인가?

A. 실제 사용자 응답에는 영향을 주지 않고 새 모델에 동일 요청을 보내 결과를 비교하는 방식이다.

Q. 모델 배포에서 Rollback이 중요한 이유는?

A. 새 모델이 예상치 못한 성능 저하나 오류를 만들 수 있기 때문이다.

---

# 17. Retraining Rules

## 17.1 Retraining Pipeline 작성 규칙

### [개념]

Retraining Pipeline은 새 데이터, Drift, 성능 저하, 정책 변경에 따라 모델을 다시 학습하고 평가하는 흐름이다.

재학습은 자동화할 수 있지만, 배포는 평가와 승인 기준을 거쳐야 한다.

---

### [핵심]

Retraining Trigger:

- New Data Available
- Data Drift Detected
- Model Drift Detected
- Concept Drift Detected
- Performance Drop
- User Feedback Deterioration
- Policy Change
- Feature Change
- Scheduled Retraining
- Manual Request

Retraining Pipeline 단계:

```text
Trigger
→ Data Validation
→ Dataset Versioning
→ Training
→ Evaluation
→ Baseline Comparison
→ Registry Update
→ Approval
→ Deployment
→ Monitoring
```

---

### [실무]

Retraining Checklist:

```md
### [Checklist]

- 재학습 Trigger가 명확한가?
- 새 Dataset Version이 생성되었는가?
- 기존 Baseline과 비교했는가?
- Test Dataset이 오염되지 않았는가?
- 성능 개선이 실제로 확인되었는가?
- Regression Test를 통과했는가?
- 배포 승인 기준을 만족하는가?
```

재학습은 모델 성능을 항상 개선하지 않는다.

새 데이터 품질이 낮으면 재학습 후 성능이 악화될 수 있다.

---

### [FAQ]

Q. Retraining은 언제 해야 하는가?

A. 새 데이터, Drift, 성능 저하, 정책 변경, 사용자 피드백 악화가 발생했을 때 검토한다.

Q. Retraining 후 바로 배포해도 되는가?

A. 아니다. Evaluation, Baseline Comparison, Regression Test, 승인 기준을 통과해야 한다.

Q. 정기 재학습은 항상 좋은가?

A. 아니다. 데이터 품질과 성능 개선 여부를 확인하지 않으면 오히려 성능이 악화될 수 있다.

---

# 18. LLMOps / RAGOps / AgentOps Rules

## 18.1 LLM / RAG / Agent 운영 연계 규칙

### [개념]

LLMOps, RAGOps, AgentOps는 MLOps 원칙을 LLM, RAG, Agent 시스템에 확장한 운영 체계이다.

LLM 기반 시스템은 모델뿐 아니라 Prompt, Retrieval, Vector DB, Tool Calling, Agent Workflow까지 함께 운영해야 한다.

---

### [핵심]

LLMOps 관리 대상:

- Model Version
- Prompt Version
- Fine-Tuning Dataset
- Evaluation Dataset
- Safety Test
- Response Quality
- Cost
- Latency

RAGOps 관리 대상:

- Document Version
- Chunk Strategy
- Embedding Model
- Vector Index
- Retrieval Quality
- Groundedness
- Citation Quality
- Hallucination Rate

AgentOps 관리 대상:

- Agent Workflow
- Tool Calling
- Agent State
- Memory
- Trace
- Retry
- Review Result
- Workflow Success Rate

---

### [실무]

LLM / RAG / Agent 운영 Flow:

```text
User Request
→ Prompt Version
→ Retrieval Pipeline
→ LLM Inference
→ Tool Calling
→ Agent Workflow
→ Evaluation
→ Monitoring
→ Feedback
→ Improvement
```

운영 Metric 예시:

```text
LLMOps:
- formatCompliance
- hallucinationRate
- safetyViolationRate

RAGOps:
- retrievalHitRate
- groundedness
- citationAccuracy

AgentOps:
- workflowSuccessRate
- toolCallErrorRate
- retryCount
```

LLM 시스템의 품질 저하는 모델만의 문제가 아닐 수 있다.

Prompt, Retrieval, Tool, Memory, Agent Workflow를 함께 점검해야 한다.

---

### [FAQ]

Q. LLMOps는 MLOps와 무엇이 다른가?

A. LLMOps는 LLM 모델, Prompt, 평가, 비용, Safety, 응답 품질 운영에 특화된 MLOps 확장이다.

Q. RAGOps는 무엇인가?

A. RAG 문서, Chunk, Embedding, Vector Index, Retrieval 품질, Groundedness를 운영하는 체계이다.

Q. AgentOps는 무엇인가?

A. Agent Workflow, Tool Calling, State, Memory, Trace, Retry, Review 결과를 운영하는 체계이다.

---

# 19. Governance and Security Rules

## 19.1 MLOps Governance / Security 작성 규칙

### [개념]

Governance and Security는 모델, 데이터, 실험, 배포, 접근 권한, 감사 로그, 안전 기준을 관리하는 규칙이다.

MLOps는 데이터와 모델을 다루므로 보안과 책임 추적이 필수이다.

---

### [핵심]

Governance 대상:

- Data Access
- Model Access
- Experiment Access
- Deployment Approval
- Audit Log
- Model Lineage
- Dataset Lineage
- Bias Review
- Safety Review
- Privacy Review
- Compliance Review

Security 기준:

- 개인정보 제거
- 민감정보 보호
- API Key / Token 저장 금지
- 학습 데이터 접근 제한
- Model Artifact 접근 제한
- 배포 권한 분리
- 로그 민감정보 마스킹
- Audit Trail 유지

---

### [실무]

Governance Checklist:

```md
### [Checklist]

- 학습 데이터 접근 권한이 제한되어 있는가?
- 개인정보와 민감정보가 제거되었는가?
- Model Artifact 접근 권한이 관리되는가?
- 배포 승인자가 명확한가?
- Audit Log가 남는가?
- Dataset과 Model Lineage가 추적되는가?
- Safety Review를 수행했는가?
```

개인 AI 프로젝트에서도 API Key, 개인 문서, 프로젝트 코드, 모델 Artifact 접근 권한을 구분하는 것이 좋다.

---

### [FAQ]

Q. MLOps에서 Governance가 왜 필요한가?

A. 데이터, 모델, 배포 결정의 출처와 책임을 추적하고 보안 위험을 줄이기 위해 필요하다.

Q. Model Lineage란?

A. 모델이 어떤 데이터, 코드, 설정, 실험 결과로 만들어졌는지 추적하는 정보이다.

Q. MLOps 로그에 민감정보를 남겨도 되는가?

A. 안 된다. 개인정보, API Key, Token, 비밀번호는 마스킹하거나 저장하지 않아야 한다.

---

# 20. Observability Rules

## 20.1 MLOps Observability 작성 규칙

### [개념]

MLOps Observability는 데이터 Pipeline, 학습 Pipeline, 모델 배포, 추론, 모니터링, Drift, 재학습 흐름을 추적 가능한 상태로 만드는 구조이다.

관측 가능성이 없으면 모델 성능 저하와 장애 원인을 파악하기 어렵다.

---

### [핵심]

관측 대상:

- pipelineId
- datasetVersion
- modelVersion
- experimentId
- runId
- deploymentId
- servingEndpoint
- inferenceLog
- predictionMetric
- systemMetric
- driftMetric
- evaluationResult
- alert
- rollbackEvent
- retrainingEvent
- userFeedback

Trace 기준:

- Data Trace
- Training Trace
- Evaluation Trace
- Deployment Trace
- Inference Trace
- Drift Trace
- Agent Workflow Trace
- RAG Retrieval Trace

---

### [실무]

MLOps Trace 예시:

```text
pipelineId: TRAIN-2026-001
datasetVersion: customer-v3
modelVersion: churn-model-v2.4
experimentId: EXP-018
evaluationStatus: passed
deploymentId: DEPLOY-045
monitoringStatus: active
driftStatus: none
```

LLM / RAG / Agent 운영에서는 모델 Trace만으로 부족하다.

Prompt Version, Retrieval Result, Tool Call, Agent State, Review Result까지 연결해야 한다.

---

### [FAQ]

Q. MLOps Observability는 왜 필요한가?

A. 데이터, 모델, 배포, 추론, Drift, 재학습 흐름을 추적해야 장애 원인을 분석할 수 있기 때문이다.

Q. 어떤 Trace가 중요한가?

A. Data Trace, Training Trace, Evaluation Trace, Deployment Trace, Inference Trace, Drift Trace가 중요하다.

Q. LLM Agent 시스템에서는 무엇을 추가로 추적해야 하는가?

A. Prompt Version, Retrieval Result, Tool Call, Agent State, Review Result, Workflow Success Rate를 추적해야 한다.

---

# 21. Troubleshooting Rules

## 21.1 MLOps 장애 대응 작성 규칙

### [개념]

MLOps Troubleshooting 문서는 데이터, Pipeline, 모델, 배포, 모니터링, Drift, 재학습 과정에서 발생하는 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- Data Pipeline 실패
- Dataset Schema 변경
- Label 품질 저하
- Data Leakage
- Experiment Tracking 누락
- 학습 재현 실패
- Evaluation 누락
- Model Registry 미사용
- 배포 후 성능 저하
- Latency 증가
- Resource 부족
- Data Drift 감지
- Model Drift 감지
- Retraining 실패
- Rollback 실패
- Monitoring 누락
- 로그에 민감정보 포함
- LLM Hallucination 증가
- RAG Retrieval 품질 저하
- Agent Workflow 실패

---

### [실무]

Troubleshooting 형식:

```md
문제:
배포 후 모델 성능이 급격히 저하됨

원인:

- 학습 데이터와 운영 데이터 분포 차이
- Data Drift 발생
- 잘못된 Model Version 배포
- Evaluation Dataset이 운영 케이스를 반영하지 못함
- Feature Pipeline이 학습 시점과 다르게 동작

해결:

- 운영 데이터 분포 확인
- Dataset Version과 Model Version 확인
- Drift Metric 확인
- 이전 Model로 Rollback
- Evaluation Dataset 보강
- Retraining Pipeline 실행
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. MLOps에서 가장 흔한 장애는?

A. Data Pipeline 오류, Dataset Version 누락, Evaluation 누락, 배포 후 성능 저하, Drift 미감지, Rollback 실패이다.

Q. 모델 성능이 운영에서만 떨어지면 무엇을 확인해야 하는가?

A. Data Drift, Feature Pipeline 차이, Dataset Version, Model Version, Evaluation Dataset 적합성을 확인해야 한다.

Q. RAG 품질 저하는 MLOps 문제인가?

A. RAGOps 관점에서 MLOps 문제로 볼 수 있다. Document Version, Embedding Model, Vector Index, Retrieval Metric을 확인해야 한다.

---

# 22. Common Mistakes

## 22.1 자주 발생하는 작성 오류

### [개념]

MLOps 문서는 “모델을 학습하고 배포하는 방법”만 설명하는 문서가 아니다.

Agent가 데이터, 실험, 모델, 평가, 배포, 모니터링, Drift, 재학습, Governance를 전체 Lifecycle로 판단할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- 모델 학습 코드 중심 작성
- Dataset Versioning 누락
- Experiment Tracking 누락
- Evaluation 기준 누락
- Model Registry 누락
- 배포 전략 누락
- Monitoring 누락
- Drift Detection 누락
- Retraining 기준 누락
- Rollback 기준 누락
- Governance / Security 누락
- Data Leakage 검토 누락
- LLMOps / RAGOps / AgentOps 연계 누락
- 운영 Metric 없이 정확도만 설명
- 특정 도구 설치법 중심 작성
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
MLOps는 머신러닝 모델을 학습하고 서버에 배포하는 것이다.
학습 코드를 작성하고 API로 제공하면 된다.
```

좋은 문서 예시:

```text
MLOps는 데이터 수집, Dataset Versioning, Experiment Tracking, Training, Evaluation, Model Registry, Deployment, Monitoring, Drift Detection, Retraining, Rollback을 포함하는 ML Lifecycle 운영 체계이다.

Flow:
Data Pipeline
→ Training Pipeline
→ Evaluation
→ Model Registry
→ Deployment
→ Monitoring
→ Drift Detection
→ Retraining
```

---

### [FAQ]

Q. MLOps 문서에서 가장 피해야 할 것은?

A. 모델 학습과 배포만 설명하고 Dataset Version, Evaluation, Monitoring, Drift, Rollback을 누락하는 것이다.

Q. 정확도만 높으면 운영 가능한 모델인가?

A. 아니다. Latency, Cost, Drift, Safety, Monitoring, Rollback 가능성도 확인해야 한다.

Q. Model Registry 없이 배포해도 되는가?

A. 권장하지 않는다. 모델 버전, 평가 결과, 배포 상태, Rollback 기준을 추적하기 어렵다.

---

# 23. Document Split Rules

## 23.1 MLOps 문서 분할 기준

### [개념]

MLOps는 Data Pipeline, Training, Evaluation, Registry, Serving, Monitoring, Drift, Retraining, Governance 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
MLOps_Part01_Core.md
MLOps_Part02_Data_Pipeline_Dataset_Versioning.md
MLOps_Part03_Experiment_Tracking_Training_Pipeline.md
MLOps_Part04_Evaluation_Model_Registry.md
MLOps_Part05_Model_Serving_CICD_CT.md
MLOps_Part06_Monitoring_Drift_Detection.md
MLOps_Part07_Deployment_Retraining_Rollback.md
MLOps_Part08_LLMOps_RAGOps_AgentOps_Governance.md
MLOps_Part09_Troubleshooting_Best_Practice.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Data Pipeline과 Dataset Versioning은 함께 작성 가능
- Experiment Tracking과 Training Pipeline은 함께 작성 권장
- Evaluation과 Model Registry는 함께 작성 권장
- Monitoring과 Drift Detection은 함께 작성 권장
- LLMOps / RAGOps / AgentOps는 MLOps 확장 문서로 작성
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

MLOps 문서 Set은 AI Expert Level과 DevOps Expert Level에서 함께 사용한다.

AI/ML Agent는 모델 운영 기준을 참조하고, DevOps Agent는 배포 / 모니터링 / Rollback 기준을 참조한다.

특정 도구는 별도 문서로 분리한다.

예:

```text
MLOps_Domain_Rules.md
MLflow_Domain_Rules.md
DVC_Domain_Rules.md
Kubeflow_Domain_Rules.md
LLMOps_Domain_Rules.md
RAGOps_Domain_Rules.md
AgentOps_Domain_Rules.md
```

---

### [FAQ]

Q. MLOps 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 8~9개 Part를 권장한다. Core, Data, Training, Evaluation, Serving, Monitoring, Deployment, LLMOps/RAGOps/AgentOps, Troubleshooting으로 분리한다.

Q. LLMOps와 MLOps 문서를 합쳐도 되는가?

A. 기본 연결은 포함하되, LLMOps 상세 운영은 별도 Domain Rules로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 24. Agent Usage Rules

## 24.1 Agent별 사용 기준

### [개념]

MLOps Domain Rules는 여러 Agent가 모델 Lifecycle 운영을 동일한 기준으로 설계, 배포, 검토, 개선하도록 돕는다.

각 Agent는 자신의 역할에 맞는 MLOps Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- MLOps 적용 필요 여부 판단
- 모델 운영 요구사항 정리
- 배포 승인 기준 확인
- Human Review 필요 여부 판단
- 최종 Workflow 통합

AI/ML Agent:

- Data Pipeline 설계
- Training Pipeline 설계
- Evaluation 기준 설계
- Drift Detection 기준 설계
- Retraining 기준 설계

Backend Agent:

- Model Serving API 구현
- Inference Endpoint 연동
- Prediction Logging 구현
- RAG / Agent Backend 통합

DevOps Agent:

- CI/CD / CT Pipeline 구성
- Model Deployment 운영
- Monitoring / Alert 구성
- Rollback / Canary / A/B Test 운영
- Resource 관리

Review Agent:

- Dataset Version 누락 검토
- Evaluation 기준 검토
- Model Registry 사용 검토
- Monitoring 누락 검토
- Rollback 기준 검토
- Security / Governance 검토

Architecture Review Agent:

- MLOps 전체 구조 검토
- LLMOps / RAGOps / AgentOps 연계 검토
- 확장성 검토
- 비용 / 운영 복잡도 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ ML Lifecycle / Deployment Strategy / Human Review / Final Decision

AI/ML Agent
→ Data Pipeline / Training / Evaluation / Drift / Retraining

Backend Agent
→ Model Serving / API Integration / Logging / Inference Contract

DevOps Agent
→ CI/CD / CT / Monitoring / Deployment / Rollback

Review Agent
→ Evaluation / Common Mistakes / Governance / Troubleshooting

Architecture Review Agent
→ MLOps Architecture / LLMOps / RAGOps / AgentOps / Scalability
```

MLOps는 AI/ML Agent 단독 영역이 아니다.

DevOps Agent, Backend Agent, Review Agent와 함께 운영 기준을 검토해야 한다.

---

### [FAQ]

Q. MLOps Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. DevOps Agent는 MLOps에서 무엇을 담당하는가?

A. CI/CD, CT, 배포, 모니터링, Rollback, Resource 운영을 담당한다.

Q. Review Agent는 MLOps에서 무엇을 검토해야 하는가?

A. Dataset Version, Evaluation, Model Registry, Monitoring, Drift Detection, Rollback, Governance 누락 여부를 검토해야 한다.

---

# 25. Final Goal

## 25.1 최종 목표

### [개념]

MLOps Domain Rules의 최종 목표는 Agent가 모델을 단순히 학습하거나 배포하는 것이 아니라, 데이터부터 운영 후 재학습까지 전체 Lifecycle을 안정적으로 관리할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- MLOps 개념 검색 가능
- ML Lifecycle 설계 가능
- Data Pipeline 설계 가능
- Dataset Versioning 가능
- Experiment Tracking 가능
- Training Pipeline 설계 가능
- Evaluation Pipeline 설계 가능
- Model Registry 운영 가능
- Model Serving 설계 가능
- CI/CD / CT 설계 가능
- Monitoring 구성 가능
- Drift Detection 가능
- Deployment Strategy 선택 가능
- Retraining Pipeline 설계 가능
- Governance / Security 검토 가능
- LLMOps / RAGOps / AgentOps 연계 가능
- Troubleshooting 가능

---

### [실무]

MLOps RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ ML / LLM 운영 요구사항 분석
→ Data Pipeline 설계
→ Training / Evaluation Pipeline 설계
→ Model Registry 등록
→ Deployment Strategy 선택
→ Monitoring / Drift Detection 구성
→ Retraining / Rollback 기준 정의
→ Review Agent 검토
→ 운영 개선
```

문서 품질은 Agent가 모델 Lifecycle을 재현 가능하고, 평가 가능하고, 배포 가능하고, 모니터링 가능한 구조로 설계할 수 있는지로 결정된다.

---

### [FAQ]

Q. MLOps Domain Rules의 최종 목적은?

A. Agent가 데이터, 실험, 모델, 평가, 배포, 모니터링, 재학습까지 전체 모델 Lifecycle을 운영할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 모델 운영 판단 품질을 높이기 위한 문서이다.

Q. MLOps 문서 품질은 무엇으로 판단하는가?

A. Agent가 Dataset Versioning, Evaluation, Registry, Serving, Monitoring, Drift, Retraining, Rollback을 누락 없이 설계할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. MLOps란?
A. ML 모델의 데이터, 실험, 학습, 평가, 배포, 모니터링, 재학습을 운영하는 Lifecycle 관리 체계이다.

Q. MLOps와 DevOps의 차이는?
A. DevOps는 애플리케이션 운영 중심이고, MLOps는 데이터와 모델 Lifecycle 관리까지 포함한다.

Q. MLOps와 LLMOps의 관계는?
A. LLMOps는 LLM 모델, Prompt, 평가, 비용, Safety, 응답 품질 운영에 특화된 MLOps 확장이다.

Q. ML Lifecycle은 무엇인가?
A. Problem Definition → Data Pipeline → Training → Evaluation → Registry → Deployment → Monitoring → Retraining 흐름이다.

Q. Data Pipeline은 무엇인가?
A. 모델 학습과 평가에 사용할 데이터를 수집, 정제, 검증, 변환, 저장하는 흐름이다.

Q. Data Validation은 왜 필요한가?
A. 잘못된 Schema, Null, 중복, 이상치, Label 오류, Data Leakage를 학습 전에 감지하기 위해 필요하다.

Q. Dataset Versioning이란?
A. 학습, 검증, 테스트에 사용한 데이터셋의 버전과 변경 이력을 관리하는 과정이다.

Q. Dataset Versioning은 왜 필요한가?
A. 어떤 데이터로 학습한 모델인지 추적해야 성능 재현, 비교, Rollback, 장애 분석이 가능하기 때문이다.

Q. Experiment Tracking이란?
A. 모델 학습 실험의 설정, 데이터, 코드, Metric, Artifact, 평가 결과를 기록하고 비교하는 과정이다.

Q. Training Pipeline이란?
A. 데이터 준비부터 모델 학습, 검증, Artifact 저장까지 자동화된 학습 흐름이다.

Q. Evaluation Pipeline이란?
A. 후보 모델이 품질 기준을 만족하는지 평가하고 배포 가능 여부를 판단하는 흐름이다.

Q. Model Registry란?
A. 모델 Artifact, 버전, 평가 결과, 배포 상태, 승인 이력을 관리하는 저장소이다.

Q. Model Serving이란?
A. 학습된 모델을 API, Batch Job, Streaming, Agent Runtime에서 사용할 수 있도록 배포하고 추론 요청을 처리하는 구조이다.

Q. ML CI/CD는 일반 CI/CD와 무엇이 다른가?
A. 코드뿐 아니라 데이터, 모델, 평가 결과, Artifact까지 Pipeline에 포함된다.

Q. CT란?
A. Continuous Training으로, 데이터 변화나 성능 저하에 따라 모델을 재학습하는 운영 구조이다.

Q. Model Monitoring은 무엇을 관측하는가?
A. Prediction Quality, Input Distribution, Drift, Latency, Throughput, Error Rate, Resource Usage, User Feedback을 관측한다.

Q. Data Drift란?
A. 운영 입력 데이터 분포가 학습 데이터 분포와 달라지는 현상이다.

Q. Model Drift란?
A. 운영 중 모델의 예측 성능이나 출력 품질이 시간이 지나며 저하되는 현상이다.

Q. Concept Drift란?
A. 입력과 정답 사이의 관계 자체가 시간에 따라 바뀌는 현상이다.

Q. Drift가 감지되면 바로 재학습해야 하는가?
A. 아니다. 먼저 평가와 원인 분석을 수행하고 재학습 여부를 판단해야 한다.

Q. Canary Deployment란?
A. 새 모델을 일부 트래픽에만 적용해 품질과 안정성을 확인하는 배포 방식이다.

Q. Shadow Deployment란?
A. 실제 사용자 응답에는 영향을 주지 않고 새 모델에 동일 요청을 보내 결과를 비교하는 방식이다.

Q. Retraining은 언제 필요한가?
A. 새 데이터, Drift, 성능 저하, 정책 변경, 사용자 피드백 악화가 발생했을 때 검토한다.

Q. RAGOps란?
A. RAG 문서, Chunk, Embedding, Vector Index, Retrieval 품질, Groundedness를 운영하는 체계이다.

Q. AgentOps란?
A. Agent Workflow, Tool Calling, State, Memory, Trace, Retry, Review 결과를 운영하는 체계이다.

Q. MLOps Governance는 왜 필요한가?
A. 데이터, 모델, 배포 결정의 출처와 책임을 추적하고 보안 위험을 줄이기 위해 필요하다.

Q. Model Lineage란?
A. 모델이 어떤 데이터, 코드, 설정, 실험 결과로 만들어졌는지 추적하는 정보이다.

Q. MLOps Observability란?
A. 데이터 Pipeline, 학습, 평가, 배포, 추론, Drift, 재학습 흐름을 추적 가능한 상태로 만드는 구조이다.

Q. MLOps에서 흔한 장애는?
A. Data Pipeline 오류, Dataset Version 누락, Evaluation 누락, 배포 후 성능 저하, Drift 미감지, Rollback 실패이다.

Q. MLOps 문서 분할은 어떻게 하는가?
A. Core, Data, Training, Evaluation, Serving, Monitoring, Deployment, LLMOps/RAGOps/AgentOps, Troubleshooting으로 분리한다.

Q. MLOps 문서에서 피해야 할 것은?
A. 모델 학습과 배포만 설명하고 Dataset Version, Evaluation, Monitoring, Drift, Rollback을 누락하는 것이다.

Q. MLOps Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

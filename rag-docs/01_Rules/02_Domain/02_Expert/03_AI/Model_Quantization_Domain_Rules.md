# Model Quantization Domain Rules

---

# 1. Domain Purpose

## 1.1 Model Quantization 문서 목적

### [개념]

Model Quantization Domain 문서는 AI Agent / AI/ML Agent / DevOps Agent / Backend Agent / Review Agent가 LLM, Embedding Model, Vision Model의 Quantization을 설계, 적용, 검토, 평가할 때 참조하는 RAG 제작 규칙 문서이다.

Model Quantization은 모델의 Weight, Activation, KV Cache 등의 수치 정밀도를 낮춰 모델 크기, 메모리 사용량, 추론 비용을 줄이는 최적화 기법이다.

Quantization은 모델 성능을 무조건 향상시키는 기술이 아니다.

Quantization은 제한된 하드웨어에서 모델을 실행하거나, 더 큰 모델을 적은 메모리로 운영하거나, 추론 속도와 비용을 개선하기 위한 Trade-off 기술이다.

---

### [핵심]

- Model Quantization = 수치 정밀도 축소 기반 모델 최적화
- 목적은 모델 크기 감소, 메모리 절약, 추론 비용 감소
- 품질 손실 가능성 존재
- Quantization Level이 낮을수록 메모리 절약은 크지만 품질 손실 위험 증가
- LLM Quantization은 Weight Quantization 중심
- KV Cache Quantization은 긴 Context 운영에 중요
- Embedding Model Quantization은 검색 품질 평가 필수
- Vision Model Quantization은 이미지 이해 성능 평가 필수
- GGUF / GPTQ / AWQ / EXL2 / BitsAndBytes 등 형식 구분 필요
- 하드웨어 / 런타임 / 모델 형식 호환성 확인 필요
- Evaluation 없이 Quantized Model 운영 금지

---

### [실무]

2026 실무 기준 Model Quantization 문서는 다음 목적을 우선한다.

- Quantization 적용 여부 판단
- Quantization 방식 선택 기준 제공
- 모델 크기 / 메모리 / 품질 Trade-off 판단
- CPU / GPU / iGPU / VRAM / RAM 환경별 선택 기준 제공
- GGUF / GPTQ / AWQ / EXL2 / BitsAndBytes 구분 기준 제공
- LLM / Embedding / Vision Model별 Quantization 검토 기준 제공
- RAG 품질 영향 평가 기준 제공
- Agent Workflow 품질 영향 평가 기준 제공
- 배포 전 Evaluation 기준 제공
- Quantization Troubleshooting 제공

Model Quantization 문서는 사람이 양자화 이론을 공부하기 위한 문서가 아니라, Agent가 제한된 하드웨어에서 어떤 Quantized Model을 선택하고 검증해야 하는지 판단할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Model Quantization 문서는 무엇을 위한 문서인가?

A. Agent가 모델 양자화 적용 여부, 방식 선택, 메모리 절감, 품질 손실, 배포 가능성을 판단할 수 있도록 기준을 제공하는 문서이다.

Q. Model Quantization은 모델 성능을 높이는 기술인가?

A. 아니다. 주 목적은 모델 크기와 메모리 사용량, 추론 비용을 줄이는 것이며 품질 손실이 발생할 수 있다.

Q. Quantization에서 가장 중요한 것은?

A. 하드웨어 호환성, 메모리 절감 효과, 응답 품질, RAG 품질, 추론 속도, Evaluation 결과이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Model Quantization Domain 문서는 LLM과 관련 모델을 제한된 하드웨어에서 효율적으로 운영하기 위한 양자화 개념, 방식, 선택 기준, 평가 기준, 장애 대응 기준을 포함한다.

---

### [핵심]

포함 범위:

- Model Quantization 개념
- Weight Quantization
- Activation Quantization
- KV Cache Quantization
- Post-Training Quantization
- Quantization-Aware Training
- Dynamic Quantization
- Static Quantization
- 8-bit Quantization
- 6-bit Quantization
- 5-bit Quantization
- 4-bit Quantization
- 3-bit Quantization
- GGUF
- GPTQ
- AWQ
- EXL2
- BitsAndBytes
- llama.cpp
- Ollama
- vLLM
- TensorRT-LLM
- Memory Estimation
- Quality Evaluation
- RAG Evaluation
- Agent Evaluation
- Quantization Troubleshooting

제외 범위:

- 수치해석 이론 상세
- GPU 커널 내부 구현 상세
- 양자컴퓨터 양자화 개념
- Fine-Tuning 전체 절차
- Vector Database 튜닝 상세
- 특정 벤더 API 전체 문서 복붙
- 모델 다운로드 사이트 목록 중심 문서
- 벤치마크 수치만 나열하는 문서

---

### [실무]

Model Quantization 문서는 아래 질문에 답할 수 있어야 한다.

- 이 모델을 Quantization해야 하는가?
- 몇 bit Quantization을 선택해야 하는가?
- GGUF, GPTQ, AWQ, EXL2 중 무엇을 선택해야 하는가?
- CPU / GPU / iGPU 환경에서 어떤 형식이 적합한가?
- VRAM이 부족하면 어떤 선택지가 있는가?
- RAM 기반 추론에서는 어떤 모델 형식이 적합한가?
- RAG 품질에 Quantization이 어떤 영향을 주는가?
- Embedding Model도 Quantization해도 되는가?
- Quantized Model 배포 전 무엇을 평가해야 하는가?
- Quantization 후 답변 품질이 떨어지면 무엇을 확인해야 하는가?

---

### [FAQ]

Q. Model Quantization 문서에 수학 이론을 자세히 넣어야 하는가?

A. 아니다. Agent가 모델 선택, 하드웨어 호환성, 품질 평가, 배포 가능성을 판단할 수 있도록 작성한다.

Q. Quantization은 Fine-Tuning과 같은가?

A. 아니다. Fine-Tuning은 모델 행동을 학습으로 조정하고, Quantization은 모델 수치 정밀도를 낮춰 메모리와 비용을 줄인다.

Q. Quantized Model은 항상 원본 모델보다 나쁜가?

A. 반드시 그렇지는 않지만 낮은 bit로 갈수록 품질 손실 가능성이 커지므로 Evaluation이 필요하다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Model Quantization 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

방식 비교가 필요한 주제는 `[Comparison]`을 추가한다.

운영 판단이 필요한 주제는 `[Checklist]`를 추가한다.

성능 검증이 필요한 주제는 `[Evaluation]`을 추가한다.

문제 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

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

- [Memory Estimate]
- [Runtime Compatibility]
- [Hardware Rule]
- [Decision Rule]
- [Anti-Pattern]
- [Review Point]

---

### [실무]

Model Quantization 문서는 단순 개념 설명보다 선택 기준과 검증 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Quantization 적용 조건
- Quantization 비적합 조건
- 모델 형식 선택 기준
- 하드웨어 호환성 기준
- 메모리 추정 기준
- 품질 평가 기준
- RAG 영향 평가 기준
- 배포 전 Checklist
- Troubleshooting 기준

---

### [FAQ]

Q. Model Quantization 문서에 Comparison이 필요한 이유는?

A. GGUF, GPTQ, AWQ, EXL2, BitsAndBytes 등 방식별 사용 환경이 다르기 때문이다.

Q. Evaluation 섹션은 왜 필요한가?

A. Quantization은 품질 손실을 만들 수 있으므로 Base Model과 비교 평가해야 한다.

Q. Troubleshooting이 필요한 이유는?

A. Quantized Model은 로딩 실패, 속도 저하, 품질 저하, Runtime 불일치 문제가 자주 발생하기 때문이다.

---

# 4. Core Concept Rules

## 4.1 Model Quantization 핵심 개념 작성 규칙

### [개념]

Model Quantization 핵심 개념은 Fine-Tuning, Model Compression, Distillation, Pruning과 구분되도록 작성한다.

Model Quantization은 모델의 수치 표현 정밀도를 낮춰 메모리 사용량과 연산 비용을 줄이는 최적화 방식이다.

Quantization은 모델 지식을 새로 추가하는 기술이 아니며, 출력 형식을 학습시키는 기술도 아니다.

---

### [핵심]

반드시 포함할 개념:

- Model Quantization
- Weight Quantization
- Activation Quantization
- KV Cache Quantization
- Precision
- FP32
- FP16
- BF16
- INT8
- INT4
- 8-bit
- 4-bit
- Post-Training Quantization
- Quantization-Aware Training
- GGUF
- GPTQ
- AWQ
- EXL2
- BitsAndBytes
- Quality Degradation
- Memory Footprint
- Inference Latency
- Throughput

용어 통일:

- Model Quantization
- Quantized Model
- Weight Quantization
- Activation Quantization
- KV Cache Quantization
- Quantization Level
- Precision
- Memory Footprint
- Quality Degradation
- Inference Runtime
- Base Model

---

### [실무]

Model Quantization 설명은 아래 구분을 반드시 포함한다.

```text
Fine-Tuning
→ 학습 데이터로 모델 행동과 출력 패턴을 조정

Model Quantization
→ 모델 수치 정밀도를 낮춰 메모리와 추론 비용을 절감

Distillation
→ 큰 모델의 지식을 작은 모델에 학습

Pruning
→ 중요도가 낮은 Weight나 구조를 제거

RAG
→ 외부 문서를 검색해 Context로 제공
```

Quantization 문서는 “모델을 가볍게 만든다” 수준에서 멈추면 안 된다.

Agent가 어떤 모델 형식을 선택하고, 어떤 하드웨어에서 실행하며, 어떤 품질 평가를 수행해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Model Quantization이란?

A. 모델의 Weight, Activation, KV Cache 등의 수치 정밀도를 낮춰 모델 크기와 메모리 사용량, 추론 비용을 줄이는 기법이다.

Q. Quantization과 Fine-Tuning의 차이는?

A. Quantization은 수치 정밀도를 낮추는 최적화이고, Fine-Tuning은 데이터를 추가 학습해 모델 행동을 조정하는 방식이다.

Q. Quantization은 모델 지식을 추가하는가?

A. 아니다. Quantization은 기존 모델을 더 적은 자원으로 실행하기 위한 최적화이다.

---

# 5. Use Case Decision Rules

## 5.1 Quantization 적용 여부 판단 규칙

### [개념]

Quantization 적용 여부 판단은 모델 운영 목적, 하드웨어 제약, 품질 요구사항, 비용 조건을 기준으로 양자화가 필요한지 결정하는 과정이다.

모든 모델에 Quantization을 적용하는 것은 적절하지 않다.

---

### [핵심]

Quantization 적합 상황:

- VRAM 부족
- RAM 부족
- 더 큰 모델을 제한된 하드웨어에서 실행해야 함
- 추론 비용 절감 필요
- 로컬 LLM 운영 필요
- 개인 AI 서버 운영
- Edge Device 운영
- 다중 모델 동시 실행 필요
- 긴 Context로 KV Cache 부담 증가
- 응답 속도 개선 필요
- 배포 비용 절감 필요

Quantization 비적합 상황:

- 최고 품질이 최우선
- 평가 데이터가 없음
- 수치 정밀도 손실이 치명적
- 작은 모델로 충분함
- Runtime이 Quantized Format을 지원하지 않음
- 모델 품질 손실을 감당할 수 없음
- Embedding 검색 품질 저하가 허용되지 않음
- Vision 인식 정확도 저하가 허용되지 않음

---

### [실무]

Quantization 선택 Flow:

```text
Deployment Requirement
→ Hardware Limit 확인
→ Base Model 크기 확인
→ Runtime Compatibility 확인
→ Quantization Format 후보 선택
→ Memory Estimate
→ Quality Evaluation
→ RAG / Agent Evaluation
→ 배포 여부 결정
```

판단 예시:

```text
상황:
개인 AI 서버 RAM 32GB에서 14B 모델을 운영해야 함

판단:
- Full Precision 운영 어려움
- Quantized Model 필요
- GGUF 또는 Ollama 호환 모델 우선 검토
- RAG 품질 평가 필요
```

---

### [FAQ]

Q. Quantization은 언제 필요할까?

A. 제한된 VRAM, RAM, 비용 환경에서 더 큰 모델을 실행하거나 추론 비용을 줄여야 할 때 필요하다.

Q. 최고 품질이 필요해도 Quantization을 해야 하는가?

A. 아니다. 최고 품질이 우선이면 Base Model 또는 낮은 손실의 8-bit / FP16 운영을 우선 검토한다.

Q. 로컬 LLM 운영에서는 Quantization이 중요한가?

A. 중요하다. 로컬 환경은 메모리 제약이 크기 때문에 Quantized Model 선택이 운영 가능성을 결정할 수 있다.

---

# 6. Quantization Level Rules

## 6.1 Quantization Level 선택 규칙

### [개념]

Quantization Level은 모델 Weight나 Activation을 몇 bit 정밀도로 표현할지 결정하는 기준이다.

낮은 bit는 메모리 절약 효과가 크지만 품질 손실 위험이 증가한다.

---

### [핵심]

대표 Precision:

- FP32
- FP16
- BF16
- INT8
- INT6
- INT5
- INT4
- INT3
- INT2

일반 경향:

- FP16 / BF16: 품질 손실 적음, 메모리 사용량 큼
- INT8: 품질 손실 낮음, 안정적
- 6-bit: 품질과 메모리 절감 균형
- 5-bit: 로컬 LLM 실무에서 균형 선택지
- 4-bit: 메모리 절감 큼, 품질 평가 필수
- 3-bit 이하: 메모리 절감 매우 큼, 품질 손실 위험 큼

---

### [실무]

Quantization Level 선택 기준:

```text
품질 우선:
FP16 / BF16 / INT8

균형 우선:
6-bit / 5-bit

메모리 우선:
4-bit

극단적 메모리 절약:
3-bit 이하
```

LLM 운영에서는 4-bit 또는 5-bit Quantized Model이 로컬 환경에서 자주 사용된다.

단, RAG 문서 생성, 코드 생성, Agent 판단 작업은 품질 손실에 민감하므로 4-bit 이하 사용 시 평가가 필수이다.

---

### [FAQ]

Q. 4-bit Quantization은 항상 좋은 선택인가?

A. 아니다. 메모리 절감은 크지만 답변 품질, 추론 안정성, 코드 생성 품질이 떨어질 수 있어 평가가 필요하다.

Q. 8-bit Quantization은 어떤 경우 적합한가?

A. 품질 손실을 최소화하면서 메모리를 줄이고 싶은 경우 적합하다.

Q. bit 수가 낮을수록 무조건 빠른가?

A. 아니다. Runtime, 하드웨어, Kernel 지원 여부에 따라 속도는 달라질 수 있다.

---

# 7. Quantization Format Rules

## 7.1 GGUF / GPTQ / AWQ / EXL2 / BitsAndBytes 선택 규칙

### [개념]

Quantization Format은 Quantized Model을 저장하고 실행하는 방식이다.

형식마다 지원 Runtime, 하드웨어, 속도, 품질, 사용 목적이 다르다.

---

### [핵심]

대표 형식:

- GGUF
- GPTQ
- AWQ
- EXL2
- BitsAndBytes
- ONNX Quantization
- TensorRT Quantization

형식별 일반 기준:

- GGUF: llama.cpp / Ollama / CPU / RAM 기반 로컬 운영에 적합
- GPTQ: GPU 기반 Quantized Inference에 사용
- AWQ: GPU 추론 최적화와 품질 균형에 사용
- EXL2: ExLlama 계열 GPU 추론 최적화에 사용
- BitsAndBytes: Python 기반 8-bit / 4-bit 로딩과 QLoRA 학습에 사용
- ONNX Quantization: 범용 배포와 Runtime 최적화에 사용
- TensorRT Quantization: NVIDIA GPU 최적화 배포에 사용

---

### [실무]

Format 선택 기준:

| 상황                          | 우선 검토 형식        |
| ----------------------------- | --------------------- |
| Ollama 로컬 운영              | GGUF                  |
| llama.cpp 직접 운영           | GGUF                  |
| CPU / RAM 중심 추론           | GGUF                  |
| NVIDIA GPU 기반 고속 추론     | GPTQ / AWQ / EXL2     |
| QLoRA 학습                    | BitsAndBytes          |
| Python Transformers 기반 실험 | BitsAndBytes          |
| ONNX Runtime 배포             | ONNX Quantization     |
| NVIDIA 최적화 서버 배포       | TensorRT Quantization |

개인 AI 서버에서 Ollama를 사용하는 경우 GGUF 계열 Quantized Model을 우선 고려한다.

GPU 서버 운영에서는 AWQ, GPTQ, EXL2, TensorRT 지원 여부를 확인한다.

---

### [FAQ]

Q. GGUF는 언제 사용하는가?

A. llama.cpp, Ollama, CPU / RAM 기반 로컬 LLM 운영에서 주로 사용한다.

Q. GPTQ와 AWQ는 언제 사용하는가?

A. GPU 기반 Quantized Inference에서 사용하며, Runtime 지원 여부와 품질 평가를 확인해야 한다.

Q. BitsAndBytes는 언제 사용하는가?

A. Transformers 기반 8-bit / 4-bit 로딩이나 QLoRA 학습에서 자주 사용한다.

---

# 8. Runtime Compatibility Rules

## 8.1 Runtime 호환성 작성 규칙

### [개념]

Runtime Compatibility는 Quantized Model 형식이 실제 실행 환경과 호환되는지 확인하는 기준이다.

Quantized Model은 형식이 맞지 않으면 로딩 자체가 실패하거나 성능이 급격히 떨어질 수 있다.

---

### [핵심]

확인 대상:

- Ollama
- llama.cpp
- vLLM
- Transformers
- ExLlama
- Text Generation Inference
- TensorRT-LLM
- ONNX Runtime
- LM Studio
- Open WebUI 연동
- AnythingLLM 연동

호환성 확인 항목:

- 모델 형식 지원 여부
- Quantization Type 지원 여부
- GPU Offload 지원 여부
- KV Cache Quantization 지원 여부
- Context Length 지원 여부
- Tool Calling 출력 안정성
- Streaming 지원 여부
- Embedding Model 지원 여부
- Vision Model 지원 여부

---

### [실무]

Runtime Compatibility Checklist:

```md
### [Checklist]

- Runtime이 모델 Format을 지원하는가?
- Runtime이 해당 Quantization Type을 지원하는가?
- CPU / GPU Offload 설정이 가능한가?
- Context Length가 요구사항을 만족하는가?
- 메모리 사용량이 하드웨어 범위 안인가?
- Token 생성 속도가 운영 기준을 만족하는가?
- RAG / Agent 시스템과 API 호환되는가?
- Tool Calling 또는 JSON 출력이 안정적인가?
```

Runtime 지원 여부를 확인하지 않고 모델만 다운로드하면 운영 실패 가능성이 높다.

---

### [FAQ]

Q. Quantized Model이 있는데 왜 실행이 안 될 수 있는가?

A. Runtime이 해당 모델 형식이나 Quantization Type을 지원하지 않을 수 있기 때문이다.

Q. Ollama에서는 어떤 형식을 주로 사용하는가?

A. Ollama는 GGUF 계열 모델 운영과 잘 맞는다.

Q. Runtime Compatibility를 언제 확인해야 하는가?

A. 모델 다운로드 전, 배포 전, Runtime 업그레이드 전후에 확인해야 한다.

---

# 9. Hardware Selection Rules

## 9.1 하드웨어별 Quantization 선택 규칙

### [개념]

하드웨어별 Quantization 선택은 CPU, GPU, iGPU, VRAM, RAM, Storage 환경에 맞춰 모델 형식과 Quantization Level을 결정하는 과정이다.

같은 Quantized Model이라도 하드웨어에 따라 속도와 안정성이 달라진다.

---

### [핵심]

확인할 하드웨어 요소:

- CPU 성능
- RAM 용량
- GPU 종류
- VRAM 용량
- iGPU 공유 메모리
- Memory Bandwidth
- Storage 속도
- OS
- Driver
- Runtime Backend
- Thermal Limit
- Power Limit

환경별 기준:

- CPU Only: GGUF, 낮은 Thread 최적화, RAM 중요
- NVIDIA GPU: AWQ / GPTQ / EXL2 / TensorRT 검토
- AMD GPU: Runtime 지원 확인 필수
- iGPU: 공유 메모리와 Runtime 지원 확인
- RAM 중심 운영: GGUF, 메모리 여유 중요
- Edge Device: 4-bit / 3-bit 검토 가능하나 품질 평가 필수

---

### [실무]

개인 AI 서버 선택 예시:

```text
환경:
- RAM 32GB ~ 64GB
- AMD iGPU
- Ollama
- 로컬 RAG / Agent 운영

선택 기준:
- GGUF 기반 Quantized Model 우선
- 14B 모델은 4-bit / 5-bit 검토
- Embedding Model은 품질 저하에 주의
- RAG 품질 평가 필수
- 다중 Agent 동시 실행보다 순차 실행 우선
```

하드웨어가 제한될수록 모델 크기, Context Length, 동시 실행 수를 함께 줄여야 한다.

Quantization만으로 모든 성능 문제가 해결되지는 않는다.

---

### [FAQ]

Q. VRAM이 부족하면 무조건 Quantization하면 되는가?

A. Quantization이 도움이 되지만 Context Length, Batch Size, 동시 실행 수, GPU Offload 설정도 함께 조정해야 한다.

Q. CPU 기반 로컬 LLM에서는 어떤 형식이 적합한가?

A. GGUF 형식이 CPU / RAM 기반 로컬 운영에 적합하다.

Q. iGPU 환경에서도 Quantized Model을 사용할 수 있는가?

A. 가능하지만 Runtime 지원, 공유 메모리, 속도, 안정성 확인이 필요하다.

---

# 10. Memory Estimation Rules

## 10.1 모델 메모리 추정 규칙

### [개념]

Memory Estimation은 모델을 실행하기 전에 Weight, KV Cache, Runtime Overhead, Context Length를 고려해 필요한 메모리를 예측하는 과정이다.

Quantized Model 운영에서는 메모리 추정이 필수이다.

---

### [핵심]

메모리 구성 요소:

- Model Weight Memory
- KV Cache Memory
- Runtime Overhead
- Context Buffer
- Batch Memory
- GPU Offload Memory
- Embedding Model Memory
- OS / Container Memory
- Vector DB Memory
- Agent Runtime Memory

기본 관계:

```text
Total Memory
≈ Model Weight
+ KV Cache
+ Runtime Overhead
+ Context Buffer
+ Application Memory
```

주의:

- 모델 파일 크기만 보고 실행 가능 여부 판단 금지
- Context Length 증가 시 KV Cache 증가
- 동시 요청 수 증가 시 메모리 증가
- GPU Offload 설정에 따라 VRAM 사용량 변화
- Agent 시스템은 LLM 외에도 Tool / RAG / DB 메모리 사용

---

### [실무]

Memory Estimation Checklist:

```md
### [Checklist]

- Quantized Model 파일 크기를 확인했는가?
- Context Length에 따른 KV Cache를 고려했는가?
- Runtime Overhead를 고려했는가?
- Embedding Model 메모리를 고려했는가?
- Vector DB / RAG Pipeline 메모리를 고려했는가?
- OS와 Docker 메모리를 남겨두었는가?
- 동시 실행 Agent 수를 고려했는가?
- 실제 로딩 테스트를 수행했는가?
```

개인 서버에서는 “모델 하나가 로딩되는가”보다 “RAG / Agent Workflow가 안정적으로 끝나는가”를 기준으로 판단한다.

---

### [FAQ]

Q. 모델 파일 크기만큼 메모리가 있으면 실행 가능한가?

A. 아니다. KV Cache, Runtime Overhead, Context Buffer, OS, RAG 시스템 메모리도 필요하다.

Q. Context Length가 늘어나면 왜 메모리가 증가하는가?

A. Attention 계산을 위한 KV Cache가 길이에 따라 증가하기 때문이다.

Q. Agent 시스템에서는 무엇을 추가로 고려해야 하는가?

A. Embedding Model, Vector DB, Tool Runtime, Agent State, 로그, 컨테이너 메모리를 함께 고려해야 한다.

---

# 11. KV Cache Quantization Rules

## 11.1 KV Cache Quantization 작성 규칙

### [개념]

KV Cache Quantization은 긴 Context 추론에서 Key / Value Cache의 메모리 사용량을 줄이기 위한 양자화 방식이다.

긴 문서 RAG, Agentic RAG, Multi-Agent Workflow에서는 KV Cache 메모리가 중요한 병목이 될 수 있다.

---

### [핵심]

KV Cache Quantization 사용 상황:

- Long Context 사용
- RAG Context가 큼
- Agent Workflow가 길어짐
- Multi-turn 대화 유지
- 동시 요청 증가
- VRAM / RAM 부족
- 긴 코드 파일 분석
- 긴 문서 요약

주의 사항:

- 출력 품질 영향 가능
- 긴 Context에서 정보 회수 성능 저하 가능
- Runtime 지원 여부 확인 필요
- 모델별 지원 여부 확인 필요
- RAG 정확도 평가 필요

---

### [실무]

KV Cache Quantization 판단 Flow:

```text
Long Context 필요
→ KV Cache Memory 부담 확인
→ Runtime 지원 여부 확인
→ KV Cache Quantization 적용
→ Long Context Evaluation
→ RAG Retrieval + Answer Quality 평가
```

긴 Context를 많이 쓰는 Agent 시스템에서는 Weight Quantization만으로 부족할 수 있다.

KV Cache, Context Length, Chunk Selection, Context Compression을 함께 조정한다.

---

### [FAQ]

Q. KV Cache Quantization은 왜 필요한가?

A. 긴 Context를 사용할 때 KV Cache 메모리가 크게 증가하므로 이를 줄이기 위해 필요하다.

Q. KV Cache Quantization은 품질에 영향을 주는가?

A. 영향을 줄 수 있다. 특히 긴 Context에서 정보 회수와 답변 정확도를 평가해야 한다.

Q. KV Cache Quantization만 적용하면 긴 Context 문제가 해결되는가?

A. 아니다. Context Selection, Chunk Compression, Top-K 조정, RAG 품질 개선도 함께 필요하다.

---

# 12. LLM Quantization Rules

## 12.1 LLM Quantization 작성 규칙

### [개념]

LLM Quantization은 대형 언어 모델의 Weight와 관련 추론 구조를 낮은 정밀도로 변환하여 메모리와 비용을 줄이는 과정이다.

LLM Quantization은 Chat, Code Generation, RAG Answering, Agent Reasoning 품질에 직접 영향을 준다.

---

### [핵심]

LLM Quantization 평가 대상:

- 일반 답변 품질
- 한국어 응답 품질
- 코드 생성 품질
- RAG 기반 답변 품질
- 긴 Context 처리 능력
- 지시문 준수 능력
- JSON 출력 안정성
- Tool Calling 형식 안정성
- Hallucination Rate
- 추론 속도
- 메모리 사용량

LLM 용도별 주의:

- Chat Model: 응답 자연성 평가
- Code Model: 코드 정확성 평가
- Agent Model: 지시 준수와 Tool Calling 평가
- RAG Model: Groundedness 평가
- Review Model: 누락 탐지와 오류 지적 능력 평가

---

### [실무]

LLM Quantization Evaluation 예시:

```md
### [Checklist]

- Base Model 대비 답변 품질이 유지되는가?
- RAG 문서 근거를 잘 따르는가?
- 코드 생성 오류가 증가하지 않았는가?
- JSON / Markdown 출력 형식을 유지하는가?
- 긴 Context에서 앞부분 정보를 잃지 않는가?
- Tool Calling 형식이 깨지지 않는가?
- 한국어 응답 품질이 유지되는가?
- Review Agent 역할에서 누락 탐지 성능이 유지되는가?
```

Agent 시스템에서는 단순 대화 품질보다 Workflow 수행 품질을 평가해야 한다.

---

### [FAQ]

Q. LLM Quantization에서 무엇을 평가해야 하는가?

A. 답변 품질, 코드 생성, RAG Grounding, 지시문 준수, 출력 형식, Tool Calling, 속도, 메모리를 평가해야 한다.

Q. Code Model도 Quantization해도 되는가?

A. 가능하지만 코드 정확성과 문법 오류 증가 여부를 반드시 평가해야 한다.

Q. Agent Model은 어떤 점을 더 봐야 하는가?

A. 지시문 준수, 단계 수행, Tool Calling 형식, Self-Validation 능력을 평가해야 한다.

---

# 13. Embedding Model Quantization Rules

## 13.1 Embedding Model Quantization 작성 규칙

### [개념]

Embedding Model Quantization은 문서와 Query를 Vector로 변환하는 Embedding Model의 메모리와 추론 비용을 줄이는 과정이다.

Embedding Model Quantization은 RAG 검색 품질에 직접 영향을 줄 수 있다.

---

### [핵심]

Embedding Quantization 평가 대상:

- Retrieval Precision
- Retrieval Recall
- Semantic Similarity 품질
- Query-Document Matching
- 한국어 검색 품질
- 코드 검색 품질
- FAQ 검색 품질
- Chunk Ranking 품질
- Near-Duplicate 구분 능력
- Vector DB 호환성
- Index 재생성 필요 여부

주의 사항:

- LLM 답변이 좋아도 Embedding 품질이 낮으면 RAG 실패
- Quantization 후 기존 Vector Index 재생성 필요 가능
- Embedding Dimension 변경 여부 확인
- Vector Distance Metric 호환성 확인
- 검색 품질 평가 없이 적용 금지

---

### [실무]

Embedding Quantization Evaluation 예시:

```md
### [Checklist]

- 기존 Embedding 대비 Top-K 검색 결과가 유지되는가?
- 핵심 문서가 검색 상위에 유지되는가?
- 한국어 Query 검색 품질이 유지되는가?
- 코드 / 명령어 검색 품질이 떨어지지 않는가?
- FAQ Query Matching이 유지되는가?
- Vector DB Index를 재생성해야 하는가?
- Retrieval Evaluation Set으로 비교했는가?
```

RAG 시스템에서는 LLM Quantization보다 Embedding Quantization이 더 위험할 수 있다.

검색 단계에서 문서를 못 찾으면 LLM이 좋은 모델이어도 답변 품질이 낮아진다.

---

### [FAQ]

Q. Embedding Model도 Quantization해도 되는가?

A. 가능하지만 Retrieval Precision과 Recall 저하가 발생할 수 있어 반드시 검색 품질 평가가 필요하다.

Q. Embedding Quantization 후 Vector Index를 다시 만들어야 하는가?

A. 모델 출력 Vector가 달라지면 기존 Index를 재생성해야 한다.

Q. RAG에서 Embedding Quantization이 위험한 이유는?

A. 검색 품질이 떨어지면 LLM이 올바른 문서를 받지 못해 답변 품질이 크게 저하되기 때문이다.

---

# 14. Vision Model Quantization Rules

## 14.1 Vision Model Quantization 작성 규칙

### [개념]

Vision Model Quantization은 이미지 이해, OCR 보조, 멀티모달 입력 처리 모델의 메모리와 추론 비용을 줄이는 과정이다.

Vision Model은 언어 모델보다 입력 특성과 평가 기준이 다르므로 별도 검증이 필요하다.

---

### [핵심]

Vision Quantization 평가 대상:

- 이미지 설명 품질
- OCR 보조 품질
- UI Screenshot 이해
- Diagram 이해
- Chart 이해
- Table 이해
- 코드 Screenshot 이해
- 작은 글자 인식
- 위치 관계 이해
- 객체 누락 여부
- Hallucination 여부
- 응답 속도
- 메모리 사용량

주의 사항:

- 낮은 bit Quantization은 시각 정보 손실 가능
- 작은 텍스트 인식 품질 저하 가능
- 복잡한 UI Screenshot 분석 성능 저하 가능
- OCR 전용 모델과 역할 구분 필요
- Vision RAG에서는 이미지와 텍스트 Evidence 관리 필요

---

### [실무]

Vision Quantization Evaluation 예시:

```md
### [Checklist]

- Screenshot의 주요 텍스트를 놓치지 않는가?
- UI 버튼 / 메뉴 / 오류 메시지를 정확히 인식하는가?
- Chart와 Table을 잘못 해석하지 않는가?
- 이미지에 없는 내용을 생성하지 않는가?
- 작은 글자와 코드 Screenshot 품질이 유지되는가?
- Base Vision Model과 비교했는가?
```

개인 AI 서버에서 Vision Model은 상시 고성능 운영보다 필요 시 호출 구조로 설계하는 것이 좋다.

Vision Model Quantization은 메모리 절감 효과와 인식 품질 손실을 함께 평가한다.

---

### [FAQ]

Q. Vision Model도 Quantization할 수 있는가?

A. 가능하지만 이미지 이해, 작은 글자 인식, UI Screenshot 분석 품질 저하를 평가해야 한다.

Q. Vision Quantization에서 가장 중요한 평가는?

A. 이미지에 있는 정보를 정확히 읽고, 없는 내용을 생성하지 않는지 확인하는 것이다.

Q. OCR과 Vision Model은 같은가?

A. 아니다. OCR은 텍스트 추출에 특화되고, Vision Model은 이미지 맥락 이해와 설명에 강하다.

---

# 15. RAG Quality Impact Rules

## 15.1 Quantization이 RAG 품질에 미치는 영향 작성 규칙

### [개념]

Quantization은 RAG 시스템의 Retrieval, Context Understanding, Answer Generation, Grounding 품질에 영향을 줄 수 있다.

RAG 시스템에서는 모델이 작동하는지만 확인하지 않고, 검색된 문서를 기반으로 정확히 답하는지 평가해야 한다.

---

### [핵심]

RAG 영향 평가 대상:

- Query Understanding
- Retrieved Context 이해
- Grounded Answer 생성
- Citation / Source 사용
- 긴 Context 처리
- Chunk 간 관계 이해
- FAQ 매칭 답변
- Code Snippet 활용
- Hallucination Rate
- 문서에 없는 내용 거절
- Re-Retrieval 판단
- Review Agent 검증 품질

Quantization 위험:

- 긴 Context에서 근거 누락
- 코드 Snippet 오해
- FAQ 답변 형식 붕괴
- 문서에 없는 내용 생성
- Retrieval 결과를 무시
- 한국어 문서 이해 품질 저하
- 지시문 준수 저하

---

### [실무]

RAG Evaluation Set 구성 예시:

```text
Test Query:
- 개념 질문
- 실무 질문
- 코드 생성 질문
- 설정 오류 질문
- FAQ 기반 질문
- 문서에 없는 내용 질문
- 긴 Context 기반 질문
- 여러 Chunk 조합 질문
```

Quantized Model 평가 기준:

```md
### [Checklist]

- 검색된 문서 근거를 정확히 사용했는가?
- 문서에 없는 내용을 단정하지 않았는가?
- 긴 Context에서 핵심 규칙을 놓치지 않았는가?
- 코드 예제를 정확히 반영했는가?
- FAQ Query에 짧고 명확히 답했는가?
- Base Model 대비 RAG 답변 품질이 유지되는가?
```

---

### [FAQ]

Q. Quantization은 RAG 품질에 영향을 주는가?

A. 줄 수 있다. 특히 긴 Context 이해, Grounding, 코드 활용, 문서에 없는 내용 거절 능력을 평가해야 한다.

Q. RAG에서는 어떤 Quantization 평가가 필요한가?

A. 검색된 Context를 정확히 사용하고, 문서 근거 없는 답변을 생성하지 않는지 평가해야 한다.

Q. Embedding Model과 LLM 중 무엇이 RAG 품질에 더 중요할까?

A. 둘 다 중요하다. Embedding은 문서 검색 품질을 결정하고, LLM은 검색된 Context 이해와 답변 생성을 결정한다.

---

# 16. Agent Quality Impact Rules

## 16.1 Quantization이 Agent 품질에 미치는 영향 작성 규칙

### [개념]

Agent Quality Impact는 Quantized Model이 Agent Workflow, Tool Calling, State 관리, Self-Validation, Review 능력에 미치는 영향을 평가하는 기준이다.

Agent 시스템에서는 단순 답변 품질보다 작업 수행 안정성이 중요하다.

---

### [핵심]

Agent 영향 평가 대상:

- Instruction Following
- Task Decomposition
- Agent Routing
- Tool Calling Format
- JSON Output
- Markdown Output
- Self-Validation
- Re-Retrieval 판단
- Error Handling
- Multi-Step Reasoning
- Long Context 유지
- Review Accuracy
- Final Output Format Compliance

Quantization 위험:

- 단계 누락
- Tool Calling JSON 형식 오류
- 출력 형식 붕괴
- Self-Validation 약화
- 복잡한 작업 분해 실패
- Review Agent의 누락 탐지 저하
- 긴 Workflow 중 앞 지시 망각
- 반복 오류 증가

---

### [실무]

Agent Evaluation Checklist:

```md
### [Checklist]

- PM Agent가 Task를 올바르게 분해하는가?
- Agent Routing 판단이 유지되는가?
- Tool Calling JSON 형식이 깨지지 않는가?
- Review Agent가 오류와 누락을 잡아내는가?
- 출력 형식을 안정적으로 유지하는가?
- 긴 Workflow에서 초기 요구사항을 유지하는가?
- Base Model 대비 Agent 성공률이 유지되는가?
```

Agent용 모델은 너무 낮은 bit Quantization을 피하는 것이 좋다.

특히 PM Agent와 Review Agent는 추론 품질과 형식 안정성이 중요하다.

---

### [FAQ]

Q. Quantization은 Agent 성능에도 영향을 주는가?

A. 영향을 준다. Task 분해, Tool Calling, JSON 출력, 검증, 긴 Workflow 유지 능력이 떨어질 수 있다.

Q. Agent용 모델은 몇 bit가 적절한가?

A. 하드웨어에 따라 다르지만 PM Agent와 Review Agent는 품질 손실이 적은 Quantization을 우선 검토한다.

Q. Tool Calling 모델에서 주의할 점은?

A. JSON Schema, Function Call Format, 인자 누락, 형식 오류 증가 여부를 반드시 평가해야 한다.

---

# 17. Evaluation Rules

## 17.1 Model Quantization Evaluation 작성 규칙

### [개념]

Model Quantization Evaluation은 Quantized Model이 Base Model 대비 필요한 품질, 속도, 메모리, 안정성을 유지하는지 평가하는 과정이다.

Quantization 완료 기준은 모델 변환이 아니라 평가 통과이다.

---

### [핵심]

평가 항목:

- Answer Quality
- Format Compliance
- Instruction Following
- Code Generation Quality
- RAG Groundedness
- Retrieval Quality
- Tool Calling Accuracy
- JSON Validity
- Long Context Accuracy
- Korean Quality
- Hallucination Rate
- Latency
- Throughput
- Memory Usage
- CPU / GPU Utilization
- Stability
- Crash Rate

비교 대상:

- Base Model
- FP16 Model
- 8-bit Model
- 6-bit Model
- 5-bit Model
- 4-bit Model
- 기존 운영 모델
- 다른 Quantization Format

---

### [실무]

Evaluation Checklist:

```md
### [Checklist]

- Base Model 대비 품질 저하가 허용 범위인가?
- 메모리 절감 효과가 충분한가?
- 추론 속도가 개선되었는가?
- RAG 답변 품질이 유지되는가?
- Tool Calling 형식이 유지되는가?
- JSON / Markdown 출력이 깨지지 않는가?
- 긴 Context에서 정보 누락이 없는가?
- 한국어 응답 품질이 유지되는가?
- 코드 생성 품질이 유지되는가?
- 배포 환경에서 안정적으로 동작하는가?
```

Quantization 평가는 단일 벤치마크 점수보다 실제 사용 Workflow 기준으로 수행한다.

---

### [FAQ]

Q. Quantization Evaluation은 왜 필요한가?

A. Quantization은 메모리를 줄이는 대신 품질 손실이 발생할 수 있으므로 실제 작업 기준 평가가 필요하다.

Q. Base Model과 비교해야 하는가?

A. 반드시 비교해야 한다. Quantized Model의 품질 손실과 효율 개선을 판단해야 한다.

Q. 속도만 빠르면 Quantization 성공인가?

A. 아니다. 품질, 형식 안정성, RAG Grounding, Tool Calling, 메모리 안정성을 함께 평가해야 한다.

---

# 18. Deployment Rules

## 18.1 Quantized Model 배포 규칙

### [개념]

Quantized Model 배포는 양자화된 모델을 실제 RAG / Agent / Backend 시스템에 적용하는 과정이다.

배포 전에는 Runtime 호환성, 모델 품질, 메모리 안정성, Rollback 가능성을 확인해야 한다.

---

### [핵심]

배포 전 확인 항목:

- 모델 Format 확인
- Quantization Level 확인
- Runtime Compatibility 확인
- Hardware Compatibility 확인
- Memory Estimate 확인
- 실제 로딩 테스트
- RAG Evaluation 통과
- Agent Evaluation 통과
- Tool Calling Evaluation 통과
- Latency / Throughput 확인
- Monitoring 설정
- Version 관리
- Rollback 계획

---

### [실무]

Deployment Checklist:

```md
### [Checklist]

- 모델 이름과 버전이 명확한가?
- Quantization Type이 기록되었는가?
- Runtime에서 정상 로딩되는가?
- 실제 요청에서 OOM이 발생하지 않는가?
- RAG Pipeline과 호환되는가?
- Embedding Model과 충돌하지 않는가?
- Agent Workflow가 완료되는가?
- 실패 시 Base Model 또는 이전 Quantized Model로 Rollback 가능한가?
- Monitoring과 로그가 설정되었는가?
```

배포는 한 번에 전체 Agent 시스템에 적용하지 않는다.

먼저 단일 Agent 또는 테스트 Workspace에서 검증한 뒤 단계적으로 적용한다.

---

### [FAQ]

Q. Quantized Model을 바로 운영 환경에 적용해도 되는가?

A. 권장하지 않는다. Runtime 호환성, RAG 품질, Agent Workflow, 메모리 안정성 평가가 필요하다.

Q. Rollback 계획은 왜 필요한가?

A. Quantized Model이 품질 저하, 로딩 실패, OOM, Tool Calling 오류를 일으킬 수 있기 때문이다.

Q. 배포 후 무엇을 모니터링해야 하는가?

A. 메모리 사용량, 응답 속도, 오류율, RAG 품질, Tool Calling 오류, 사용자 피드백을 모니터링한다.

---

# 19. Observability Rules

## 19.1 Quantization Observability 작성 규칙

### [개념]

Quantization Observability는 Quantized Model의 모델 버전, 양자화 방식, 메모리 사용량, 추론 속도, 품질 변화, 오류를 추적하는 구조이다.

Quantized Model 운영에서는 성능과 품질 변화를 지속적으로 관찰해야 한다.

---

### [핵심]

관측 대상:

- modelName
- baseModel
- quantizedModelVersion
- quantizationFormat
- quantizationLevel
- runtime
- hardware
- contextLength
- memoryUsage
- vramUsage
- ramUsage
- latency
- throughput
- tokensPerSecond
- errorRate
- oomCount
- loadFailure
- ragQualityScore
- toolCallErrorRate
- userFeedback
- rollbackEvent

기록 기준:

- 모델 변경 이력 기록
- Runtime 변경 이력 기록
- 성능 측정 기록
- 품질 평가 결과 기록
- 실패 사례 기록
- Rollback 사유 기록

---

### [실무]

Quantization Trace 예시:

```text
modelName: qwen2.5-14b
quantizationFormat: GGUF
quantizationLevel: 4-bit
runtime: Ollama
hardware: local AI server
contextLength: 20000
memoryUsage: stable
ragEvaluation: passed
toolCallingEvaluation: not applicable
deploymentStatus: testing
```

Observability가 없으면 어떤 Quantization 방식이 품질 저하나 OOM을 유발했는지 추적하기 어렵다.

---

### [FAQ]

Q. Quantization Observability는 왜 필요한가?

A. 모델 형식, 메모리, 속도, 품질 저하, 오류 원인을 추적하기 위해 필요하다.

Q. 어떤 정보를 반드시 기록해야 하는가?

A. modelName, quantizationFormat, quantizationLevel, runtime, hardware, memoryUsage, latency, evaluationResult를 기록해야 한다.

Q. 사용자 피드백도 기록해야 하는가?

A. 기록하는 것이 좋다. 실제 사용 품질은 벤치마크만으로 판단하기 어렵다.

---

# 20. Troubleshooting Rules

## 20.1 Model Quantization 장애 대응 작성 규칙

### [개념]

Model Quantization Troubleshooting 문서는 Quantized Model 로딩, 추론, 품질, RAG, Agent Workflow에서 발생하는 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- 모델 로딩 실패
- Runtime 형식 불일치
- OOM
- 추론 속도 저하
- 답변 품질 저하
- 코드 생성 품질 저하
- 한국어 품질 저하
- JSON 출력 붕괴
- Tool Calling 실패
- RAG Context 무시
- 긴 Context 정보 누락
- Embedding 검색 품질 저하
- Vision 인식 품질 저하
- GPU Offload 실패
- KV Cache 메모리 부족
- Runtime Crash

---

### [실무]

Troubleshooting 형식:

```md
문제:
Quantized Model 로딩 중 OOM 발생

원인:

- 모델 Weight 외 KV Cache와 Runtime Overhead를 고려하지 않음
- Context Length가 너무 큼
- GPU Offload 설정이 과도함
- 다른 모델 또는 Vector DB가 메모리를 사용 중

해결:

- 더 높은 Quantization 적용
- Context Length 축소
- GPU Offload Layer 조정
- 동시 실행 모델 수 축소
- RAG Top-K와 Chunk Size 조정
- 실제 메모리 사용량 모니터링
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. Quantized Model에서 가장 흔한 문제는?

A. 로딩 실패, OOM, Runtime 호환성 문제, 품질 저하, 긴 Context 정보 누락이다.

Q. Quantization 후 답변 품질이 나빠지면 어떻게 해야 하는가?

A. 더 높은 bit 모델을 사용하거나, 다른 Quantization Format을 테스트하고, RAG / Agent Evaluation을 다시 수행한다.

Q. JSON 출력이 깨지면 무엇을 확인해야 하는가?

A. Quantization Level, Base Model 대비 형식 준수율, Prompt, Tool Calling Evaluation, Runtime 설정을 확인한다.

---

# 21. Common Mistakes

## 21.1 자주 발생하는 작성 오류

### [개념]

Model Quantization 문서는 “모델을 작게 만드는 방법”만 설명하는 문서가 아니다.

Agent가 하드웨어, Runtime, 품질, RAG 영향, Agent Workflow 영향, 배포 가능성을 함께 판단할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- Quantization을 성능 향상 기술로만 설명
- bit 수만 비교하고 Evaluation 누락
- 모델 파일 크기만 보고 메모리 판단
- Runtime Compatibility 확인 누락
- RAG 품질 영향 누락
- Agent Workflow 영향 누락
- Embedding Model Quantization 평가 누락
- Vision Model Quantization 평가 누락
- KV Cache 메모리 고려 누락
- Tool Calling 형식 평가 누락
- GGUF / GPTQ / AWQ / EXL2 구분 누락
- 하드웨어 환경 구분 누락
- 배포 전 Rollback 계획 누락
- Troubleshooting 누락
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Quantization은 모델을 4-bit로 줄이면 메모리를 적게 쓰고 빨라지는 기술이다.
```

좋은 문서 예시:

```text
Model Quantization은 모델 Weight, Activation, KV Cache의 수치 정밀도를 낮춰 메모리와 추론 비용을 줄이는 최적화이다.

Flow:
Hardware Limit 확인
→ Runtime Compatibility 확인
→ Quantization Format 선택
→ Memory Estimate
→ RAG / Agent Evaluation
→ 배포
→ Monitoring
```

---

### [FAQ]

Q. Model Quantization 문서에서 가장 피해야 할 것은?

A. bit 수와 모델 크기만 설명하고 Runtime, 품질 평가, RAG 영향, Agent 영향, 배포 검증을 누락하는 것이다.

Q. 4-bit 모델이면 무조건 좋은가?

A. 아니다. 메모리는 줄지만 품질 손실과 출력 형식 오류가 생길 수 있어 평가가 필요하다.

Q. 모델 파일 크기만 보면 메모리 요구량을 알 수 있는가?

A. 아니다. KV Cache, Runtime Overhead, Context Length, RAG 시스템 메모리도 고려해야 한다.

---

# 22. Document Split Rules

## 22.1 Model Quantization 문서 분할 기준

### [개념]

Model Quantization은 방식 선택, Runtime 호환성, 하드웨어, 메모리, LLM / Embedding / Vision 평가, 배포 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Model_Quantization_Part01_Core.md
Model_Quantization_Part02_Quantization_Level_Format.md
Model_Quantization_Part03_Runtime_Hardware_Compatibility.md
Model_Quantization_Part04_Memory_KV_Cache.md
Model_Quantization_Part05_LLM_Quantization.md
Model_Quantization_Part06_Embedding_Vision_Quantization.md
Model_Quantization_Part07_RAG_Agent_Evaluation.md
Model_Quantization_Part08_Deployment_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Quantization Level과 Format은 함께 작성 가능
- Runtime과 Hardware는 함께 작성 권장
- Memory와 KV Cache는 함께 작성 권장
- LLM, Embedding, Vision 평가는 분리 또는 묶음 작성 가능
- RAG / Agent Evaluation은 Checklist 중심
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Model Quantization 문서 Set은 AI Expert Level에서 사용한다.

단, DevOps Agent와 Backend Agent도 배포와 모델 서빙 과정에서 참조할 수 있으므로 특정 도구 문서보다 선택 기준, 호환성 기준, 평가 기준을 우선한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Model_Quantization_Domain_Rules.md
GGUF_Ollama_Domain_Rules.md
GPTQ_AWQ_Domain_Rules.md
KV_Cache_Optimization_Part.md
Local_LLM_Deployment_Part.md
```

---

### [FAQ]

Q. Model Quantization 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 7~8개 Part를 권장한다. Core, Level/Format, Runtime/Hardware, Memory/KV Cache, LLM, Embedding/Vision, RAG/Agent Evaluation, Deployment/Troubleshooting으로 분리한다.

Q. Ollama 문서와 Quantization 문서를 합쳐도 되는가?

A. 권장하지 않는다. Quantization은 선택 기준과 평가 기준 중심이고, Ollama는 Runtime 운영 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 23. Agent Usage Rules

## 23.1 Agent별 사용 기준

### [개념]

Model Quantization Domain Rules는 여러 Agent가 Quantized Model 선택, 실행, 평가, 배포를 동일한 기준으로 수행하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Quantization Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- Quantization 적용 필요 여부 판단
- 품질 / 비용 / 속도 Trade-off 확인
- Agent Workflow 영향 판단
- Review 필요 여부 판단

AI/ML Agent:

- Quantization 방식 선택
- Model Format 선택
- RAG / Agent Evaluation 설계
- Embedding / Vision 품질 평가
- Base Model 비교

Backend Agent:

- Model Serving 연동
- Runtime API 연동
- RAG Pipeline 통합
- Tool Calling 안정성 확인

DevOps Agent:

- Hardware Compatibility 확인
- Runtime 설치 / 운영
- Memory / VRAM 모니터링
- 배포 / Rollback / Monitoring 구성

Review Agent:

- Quantization 적용 타당성 검토
- 품질 저하 검토
- RAG Grounding 검토
- Tool Calling 형식 검토
- 배포 전 Checklist 검토

Architecture Review Agent:

- 장기 운영 구조 검토
- 모델 선택 전략 검토
- 비용 / 확장성 검토
- Multi-Agent 모델 배치 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Use Case Decision / Quality Trade-off / Agent Impact

AI/ML Agent
→ Quantization Level / Format / RAG Evaluation / Agent Evaluation

Backend Agent
→ Runtime API / Model Serving / RAG Integration / Tool Calling

DevOps Agent
→ Runtime Compatibility / Hardware / Memory / Deployment / Observability

Review Agent
→ Evaluation / Common Mistakes / Troubleshooting / Safety

Architecture Review Agent
→ Model Strategy / Cost / Scalability / Multi-Agent Deployment
```

Quantization은 AI/ML Agent 단독 결정으로 끝내지 않는다.

DevOps Agent의 하드웨어 검증과 Review Agent의 품질 검증이 필요하다.

---

### [FAQ]

Q. Model Quantization Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. DevOps Agent는 무엇을 우선 확인해야 하는가?

A. Runtime Compatibility, Hardware Compatibility, Memory Usage, 배포 안정성, Rollback 가능성을 확인해야 한다.

Q. Review Agent는 Quantization에서 무엇을 검토해야 하는가?

A. Base Model 대비 품질 저하, RAG Grounding, Tool Calling 형식, 출력 형식, 배포 전 Checklist를 검토해야 한다.

---

# 24. Final Goal

## 24.1 최종 목표

### [개념]

Model Quantization Domain Rules의 최종 목표는 Agent가 제한된 하드웨어와 운영 환경에서 적절한 Quantized Model을 선택하고, 품질 손실을 평가하고, 안정적으로 배포할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Model Quantization 개념 검색 가능
- Fine-Tuning / RAG / Distillation과 구분 가능
- Quantization 적용 여부 판단 가능
- Quantization Level 선택 가능
- Quantization Format 선택 가능
- Runtime Compatibility 판단 가능
- Hardware Compatibility 판단 가능
- Memory Estimate 가능
- KV Cache 영향 판단 가능
- LLM Quantization 평가 가능
- Embedding Quantization 평가 가능
- Vision Quantization 평가 가능
- RAG 품질 영향 평가 가능
- Agent Workflow 영향 평가 가능
- Deployment Review 가능
- Observability 구성 가능
- Troubleshooting 가능

---

### [실무]

Model Quantization RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Hardware Constraint 확인
→ Model Requirement 분석
→ Quantization 적용 여부 판단
→ Format / Level 선택
→ Runtime Compatibility 확인
→ Memory Estimate
→ RAG / Agent Evaluation
→ Deployment Review
→ Monitoring
→ 필요 시 Rollback
```

문서 품질은 Agent가 적절한 Quantized Model을 선택하고, 품질 손실과 메모리 절감 효과를 검증하고, 안정적으로 운영할 수 있는지로 결정된다.

---

### [FAQ]

Q. Model Quantization Domain Rules의 최종 목적은?

A. Agent가 제한된 하드웨어에서 적절한 Quantized Model을 선택, 평가, 배포할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Quantized Model 운영 판단 품질을 높이기 위한 문서이다.

Q. Model Quantization 문서 품질은 무엇으로 판단하는가?

A. Agent가 하드웨어, Runtime, 메모리, 품질, RAG 영향, Agent 영향, 배포 가능성을 함께 판단할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Model Quantization이란?
A. 모델의 Weight, Activation, KV Cache 등의 수치 정밀도를 낮춰 모델 크기와 메모리 사용량, 추론 비용을 줄이는 기법이다.

Q. Quantization과 Fine-Tuning의 차이는?
A. Quantization은 수치 정밀도를 낮추는 최적화이고, Fine-Tuning은 데이터를 추가 학습해 모델 행동을 조정하는 방식이다.

Q. Quantization은 모델 성능을 높이는 기술인가?
A. 아니다. 주 목적은 메모리 절감과 추론 비용 감소이며 품질 손실이 발생할 수 있다.

Q. Quantization은 언제 필요한가?
A. VRAM, RAM, 비용이 제한된 환경에서 더 큰 모델을 실행하거나 추론 비용을 줄여야 할 때 필요하다.

Q. Quantization이 적합하지 않은 경우는?
A. 최고 품질이 최우선이거나, 평가 데이터가 없거나, Runtime이 Quantized Format을 지원하지 않는 경우 적합하지 않다.

Q. 4-bit Quantization은 무엇인가?
A. 모델 Weight를 4-bit 수준으로 표현해 메모리를 크게 줄이는 방식이며 품질 평가가 필수이다.

Q. 8-bit Quantization은 언제 적합한가?
A. 품질 손실을 최소화하면서 메모리를 줄이고 싶은 경우 적합하다.

Q. GGUF는 언제 사용하는가?
A. llama.cpp, Ollama, CPU / RAM 기반 로컬 LLM 운영에서 주로 사용한다.

Q. GPTQ는 언제 사용하는가?
A. GPU 기반 Quantized Inference에서 사용하며 Runtime 지원 여부 확인이 필요하다.

Q. AWQ는 언제 사용하는가?
A. GPU 추론 최적화와 품질 균형이 필요한 경우 사용한다.

Q. EXL2는 언제 사용하는가?
A. ExLlama 계열 GPU 추론 최적화 환경에서 사용한다.

Q. BitsAndBytes는 언제 사용하는가?
A. Transformers 기반 8-bit / 4-bit 로딩이나 QLoRA 학습에서 사용한다.

Q. Runtime Compatibility란?
A. Quantized Model 형식과 Quantization Type이 실제 실행 Runtime에서 지원되는지 확인하는 기준이다.

Q. Ollama에서는 어떤 Quantization 형식이 적합한가?
A. GGUF 계열 모델이 Ollama 로컬 운영과 잘 맞는다.

Q. Quantized Model 메모리 추정 시 무엇을 고려해야 하는가?
A. Model Weight, KV Cache, Runtime Overhead, Context Buffer, OS, RAG Pipeline 메모리를 고려해야 한다.

Q. KV Cache Quantization이란?
A. 긴 Context 추론에서 Key / Value Cache의 메모리 사용량을 줄이기 위한 양자화 방식이다.

Q. LLM Quantization에서 무엇을 평가해야 하는가?
A. 답변 품질, 코드 생성, RAG Grounding, 지시문 준수, 출력 형식, Tool Calling, 속도, 메모리를 평가해야 한다.

Q. Embedding Model도 Quantization해도 되는가?
A. 가능하지만 Retrieval Precision과 Recall 저하가 발생할 수 있어 반드시 검색 품질 평가가 필요하다.

Q. Embedding Quantization 후 Vector Index를 다시 만들어야 하는가?
A. 모델 출력 Vector가 달라지면 기존 Index를 재생성해야 한다.

Q. Vision Model도 Quantization할 수 있는가?
A. 가능하지만 이미지 이해, 작은 글자 인식, UI Screenshot 분석 품질 저하를 평가해야 한다.

Q. Quantization은 RAG 품질에 영향을 주는가?
A. 영향을 줄 수 있다. 긴 Context 이해, Grounding, 코드 활용, 문서에 없는 내용 거절 능력을 평가해야 한다.

Q. Quantization은 Agent 성능에 영향을 주는가?
A. 영향을 준다. Task 분해, Tool Calling, JSON 출력, 검증, 긴 Workflow 유지 능력이 떨어질 수 있다.

Q. Model Quantization Evaluation 항목은?
A. Answer Quality, Format Compliance, RAG Groundedness, Tool Calling Accuracy, Long Context Accuracy, Latency, Memory Usage이다.

Q. Quantized Model 배포 전 확인할 것은?
A. Runtime Compatibility, Hardware Compatibility, Memory Estimate, RAG Evaluation, Agent Evaluation, Rollback 계획을 확인해야 한다.

Q. Quantization Observability는 무엇인가?
A. Quantized Model의 버전, 양자화 방식, 메모리 사용량, 추론 속도, 품질 변화, 오류를 추적하는 구조이다.

Q. Quantization에서 흔한 실패는?
A. 로딩 실패, OOM, Runtime 호환성 문제, 품질 저하, 긴 Context 정보 누락, Tool Calling 형식 오류이다.

Q. Model Quantization 문서 분할은 어떻게 하는가?
A. Core, Level/Format, Runtime/Hardware, Memory/KV Cache, LLM, Embedding/Vision, RAG/Agent Evaluation, Deployment/Troubleshooting으로 분리한다.

Q. Model Quantization 문서에서 피해야 할 것은?
A. bit 수와 모델 크기만 설명하고 Runtime, 품질 평가, RAG 영향, Agent 영향, 배포 검증을 누락하는 것이다.

Q. Model Quantization Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

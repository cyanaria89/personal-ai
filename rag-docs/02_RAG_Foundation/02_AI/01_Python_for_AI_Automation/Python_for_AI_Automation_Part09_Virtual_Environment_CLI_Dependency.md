# Python for AI Automation Part09 - Virtual Environment CLI Dependency

---

# 1. Virtual Environment Overview

## 1.1 Virtual Environment Role

### [개념]

Virtual Environment는 Python 프로젝트별로 패키지 의존성을 격리하는 실행 환경이다.

Python for AI Automation에서 Virtual Environment는 RAG Document Automation, Agent Tool Script, API Client, CSV Processing, Markdown Processing에 필요한 패키지를 프로젝트 단위로 관리하기 위해 사용한다.

Part09는 Part06의 환경변수 관리, Part08의 ToolOutput 타입 구조, Part10의 Agent Tool 실행 구조와 연결된다.

기본 Flow:

```text
Project Folder
→ Create Virtual Environment
→ Activate Virtual Environment
→ Install Dependencies
→ Run Automation Script
→ Freeze Dependencies
```

---

### [핵심]

- Virtual Environment는 프로젝트별 Python 패키지를 분리한다.
- 전역 Python 환경 오염을 방지한다.
- 패키지 버전 충돌을 줄인다.
- 자동화 스크립트 재현성을 높인다.
- `.venv` 폴더는 Git에 올리지 않는다.
- `requirements.txt` 또는 `pyproject.toml`로 의존성을 기록한다.
- Agent Tool Script 실행 환경을 명확히 만들 수 있다.
- `.env`는 실제 Secret 저장용이고, `.env.example`은 필요한 환경변수 이름 공유용이다.

---

### [실무]

2026 실무 기준 Python 자동화 프로젝트는 기본적으로 Virtual Environment를 사용한다.

권장 구조:

```text
python_ai_automation
├ .venv
├ .env
├ .env.example
├ main.py
├ requirements.txt
├ .gitignore
├ src
└ tests
```

기본 절차:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests python-dotenv pyyaml pandas pytest
python -m pip freeze > requirements.txt
```

Windows 활성화:

```bash
.venv\Scripts\activate
```

Linux / macOS 활성화:

```bash
source .venv/bin/activate
```

`.env`와 `.env.example` 역할:

```text
.env
→ 실제 Secret 저장
→ Git 제외
→ 로컬 개발 환경에서 사용

.env.example
→ 필요한 환경변수 이름 공유
→ 실제 Secret 미포함
→ Git 포함 가능
```

---

### [FAQ]

Q. Virtual Environment는 왜 필요해?

A. 프로젝트별 Python 패키지 버전을 분리해 의존성 충돌과 전역 환경 오염을 막기 위해 필요하다.

Q. Python 자동화 프로젝트마다 venv를 만들어야 해?

A. 권장한다. 프로젝트별 실행 환경을 독립적으로 관리할 수 있기 때문이다.

Q. `.venv` 폴더는 Git에 올려도 돼?

A. 안 된다. `.gitignore`에 추가하고 의존성 목록만 기록한다.

Q. Virtual Environment 없이 pip install 해도 돼?

A. 가능하지만 전역 환경이 오염되고 다른 프로젝트와 패키지 버전이 충돌할 수 있으므로 권장하지 않는다.

Q. `.env.example`은 왜 같이 두는 게 좋아?

A. 실제 Secret을 공유하지 않고 필요한 환경변수 이름과 기본 설정 구조를 문서화할 수 있기 때문이다.

---

# 2. venv

## 2.1 venv Create

### [개념]

`venv`는 Python 표준 라이브러리로 제공되는 Virtual Environment 생성 도구이다.

별도 설치 없이 `python -m venv .venv` 명령으로 프로젝트 내부에 가상환경을 만들 수 있다.

```bash
python -m venv .venv
```

---

### [핵심]

- `venv`는 Python 표준 기능이다.
- `.venv`는 프로젝트 내부 가상환경 폴더명으로 자주 사용된다.
- 가상환경은 Python 실행 파일과 설치 패키지를 독립적으로 가진다.
- 가상환경 생성 후 활성화가 필요하다.
- Python 버전은 가상환경 생성 시점의 Python을 따른다.
- `.venv` 폴더는 Git 관리 대상에서 제외한다.
- Python 3.11+ 기준을 권장한다.
- Python 3.12를 사용할 수 있으면 우선 고려한다.

---

### [실무]

프로젝트 폴더 생성:

```bash
mkdir python_ai_automation
cd python_ai_automation
```

가상환경 생성:

```bash
python -m venv .venv
```

Linux / macOS 확인:

```bash
ls .venv
```

Windows 확인:

```bash
dir .venv
```

`.gitignore` 설정:

```text
.venv
__pycache__/
.pytest_cache/
.env
```

---

### [FAQ]

Q. venv는 설치해야 해?

A. 일반적으로 Python 표준 라이브러리에 포함되어 있어 별도 설치가 필요 없다.

Q. `.venv`라는 이름을 꼭 써야 해?

A. 필수는 아니지만 Python 프로젝트에서 관례적으로 많이 사용한다.

Q. 가상환경은 Python 버전을 따로 설치해?

A. 가상환경은 생성에 사용한 Python 실행 파일 기준으로 구성된다.

Q. `.venv`를 삭제해도 돼?

A. 가능하다. `requirements.txt` 또는 `pyproject.toml`이 있으면 다시 만들 수 있다.

---

## 2.2 venv Activate and Deactivate

### [개념]

Activate는 현재 터미널 세션에서 Virtual Environment의 Python과 pip를 사용하도록 전환하는 작업이다.

Deactivate는 활성화된 Virtual Environment에서 빠져나오는 작업이다.

---

### [핵심]

- 가상환경을 사용하려면 activate가 필요하다.
- 활성화 후 `python`, `pip` 명령은 가상환경 내부를 기준으로 동작한다.
- 터미널 Prompt에 `(.venv)`가 표시될 수 있다.
- 작업이 끝나면 `deactivate`로 빠져나올 수 있다.
- IDE는 프로젝트 Interpreter를 `.venv`로 지정해야 한다.
- `python -m pip`를 사용하면 현재 Interpreter 기준 pip를 명확히 사용할 수 있다.

---

### [실무]

Linux / macOS 활성화:

```bash
source .venv/bin/activate
```

Windows PowerShell 활성화:

```bash
.venv\Scripts\Activate.ps1
```

Windows CMD 활성화:

```bash
.venv\Scripts\activate.bat
```

비활성화:

```bash
deactivate
```

현재 Python 확인:

```bash
which python
```

Windows 확인:

```bash
where python
```

pip 위치 확인:

```bash
python -m pip --version
```

---

### [FAQ]

Q. venv 활성화는 왜 필요해?

A. 현재 터미널에서 프로젝트 전용 Python과 패키지를 사용하기 위해 필요하다.

Q. 활성화되었는지 어떻게 확인해?

A. Prompt의 `(.venv)` 표시, `which python`, `where python`, `python -m pip --version`으로 확인한다.

Q. deactivate는 무엇을 해?

A. 현재 터미널에서 활성화된 가상환경을 종료한다.

Q. VS Code나 IDE에서도 venv를 설정해야 해?

A. 그렇다. IDE Interpreter를 프로젝트 `.venv`로 지정해야 설치 패키지를 정상 인식한다.

---

# 3. pip

## 3.1 pip Role

### [개념]

`pip`는 Python 패키지를 설치, 제거, 조회하는 기본 패키지 관리 도구이다.

Python for AI Automation에서는 `requests`, `httpx`, `python-dotenv`, `pyyaml`, `pandas`, `pytest`, `ruff` 같은 외부 패키지를 설치하는 데 사용한다.

```bash
python -m pip install requests
```

---

### [핵심]

- pip는 Python 패키지 설치 도구이다.
- `python -m pip` 형태를 권장한다.
- 가상환경 활성화 후 설치한다.
- 설치 패키지는 `requirements.txt`에 기록한다.
- 사용하지 않는 패키지는 제거한다.
- 패키지 버전 충돌을 주의한다.
- 자동화 스크립트 재현성을 위해 버전을 기록한다.
- 패키지 추가 후 최소 실행 테스트를 수행한다.

---

### [실무]

패키지 설치:

```bash
python -m pip install requests
```

여러 패키지 설치:

```bash
python -m pip install requests httpx python-dotenv pyyaml pandas pytest
```

패키지 제거:

```bash
python -m pip uninstall requests
```

설치 목록 확인:

```bash
python -m pip list
```

패키지 정보 확인:

```bash
python -m pip show requests
```

pip 업그레이드:

```bash
python -m pip install --upgrade pip
```

---

### [FAQ]

Q. pip는 무엇이야?

A. Python 외부 패키지를 설치하고 관리하는 도구이다.

Q. `pip install`과 `python -m pip install` 중 무엇을 권장해?

A. `python -m pip install`을 권장한다. 현재 Python Interpreter와 연결된 pip를 명확히 사용할 수 있기 때문이다.

Q. 패키지는 가상환경 활성화 후 설치해야 해?

A. 그렇다. 그래야 프로젝트별 의존성이 분리된다.

Q. 설치한 패키지 목록은 어떻게 확인해?

A. `python -m pip list`를 사용한다.

---

## 3.2 Install Automation Dependencies

### [개념]

Automation Dependencies는 Python 자동화 스크립트 실행에 필요한 외부 패키지이다.

AI Automation Script는 HTTP API, YAML Config, CSV 분석, 테스트, 코드 품질 검사를 위해 외부 패키지를 사용할 수 있다.

---

### [핵심]

- HTTP API 호출에는 `requests` 또는 `httpx`를 사용한다.
- `.env` 로딩에는 `python-dotenv`를 사용한다.
- YAML 처리에는 `pyyaml`을 사용한다.
- CSV / 표 데이터 처리에는 `pandas`를 사용할 수 있다.
- 테스트에는 `pytest`를 사용할 수 있다.
- 코드 품질 검사에는 `ruff`를 사용할 수 있다.
- 코드 포맷팅에는 `black`을 사용할 수 있다.
- 사용하지 않는 패키지는 설치하지 않는다.
- 표준 라이브러리로 충분한 작업에는 외부 패키지를 추가하지 않는다.

---

### [실무]

기본 자동화 패키지:

```bash
python -m pip install requests python-dotenv pyyaml pytest
```

데이터 처리 포함:

```bash
python -m pip install requests python-dotenv pyyaml pandas pytest
```

비동기 API 포함:

```bash
python -m pip install httpx
```

코드 품질 도구 포함:

```bash
python -m pip install ruff black
```

권장 분류:

```text
API Request
→ requests / httpx

Environment Variable
→ python-dotenv

YAML Processing
→ pyyaml

Data Processing
→ pandas

Testing
→ pytest

Lint / Format
→ ruff / black
```

---

### [FAQ]

Q. Python 자동화 기본 패키지는 무엇이야?

A. `requests`, `python-dotenv`, `pyyaml`, `pytest`를 기본으로 고려할 수 있다.

Q. pandas는 항상 설치해야 해?

A. 아니다. 표 형태 데이터 분석이나 CSV 가공이 필요할 때만 설치한다.

Q. httpx는 언제 설치해?

A. 비동기 API 호출이나 Async Workflow가 필요할 때 설치한다.

Q. black과 ruff는 꼭 필요해?

A. 필수는 아니지만 코드 포맷팅과 정적 품질 검사를 위해 권장할 수 있다.

---

# 4. requirements.txt

## 4.1 requirements.txt Role

### [개념]

`requirements.txt`는 Python 프로젝트에서 필요한 패키지 목록과 버전을 기록하는 파일이다.

Python for AI Automation에서는 자동화 스크립트를 다른 환경에서 재현 가능하게 실행하기 위해 사용한다.

```text
requests==2.32.3
python-dotenv==1.0.1
pytest==8.3.3
```

---

### [핵심]

- `requirements.txt`는 패키지 의존성 목록이다.
- 다른 환경에서 동일 패키지를 설치할 수 있다.
- `pip freeze > requirements.txt`로 생성할 수 있다.
- `pip install -r requirements.txt`로 설치할 수 있다.
- 필요 없는 패키지가 들어가지 않도록 관리한다.
- 버전 고정은 재현성에 유리하다.
- 너무 오래된 버전은 보안 취약점이 있을 수 있다.
- Agent Tool 실행 환경 재현에 중요하다.

---

### [실무]

생성:

```bash
python -m pip freeze > requirements.txt
```

설치:

```bash
python -m pip install -r requirements.txt
```

수동 작성 예시:

```text
requests==2.32.3
httpx==0.27.2
python-dotenv==1.0.1
pyyaml==6.0.2
pandas==2.2.3
pytest==8.3.3
ruff==0.6.9
```

검증:

```bash
python -m pip check
```

권장 운영:

```text
Install Package
→ Test Script
→ Freeze Requirements
→ Commit requirements.txt
→ Exclude .venv
```

---

### [FAQ]

Q. requirements.txt는 왜 필요해?

A. 자동화 스크립트를 다른 환경에서도 같은 패키지 버전으로 실행하기 위해 필요하다.

Q. requirements.txt는 어떻게 생성해?

A. `python -m pip freeze > requirements.txt` 명령으로 생성한다.

Q. requirements.txt로 설치하려면?

A. `python -m pip install -r requirements.txt`를 사용한다.

Q. `.venv` 대신 requirements.txt를 Git에 올리는 이유는?

A. `.venv`는 크고 환경 의존적이므로 제외하고 의존성 목록만 공유하기 위해서이다.

---

## 4.2 Version Pinning

### [개념]

Version Pinning은 패키지 버전을 명시적으로 고정하는 방식이다.

자동화 스크립트는 패키지 버전 변화에 따라 동작이 달라질 수 있으므로 재현성이 중요한 경우 Version Pinning을 사용한다.

```text
requests==2.32.3
```

---

### [핵심]

- `==`는 정확한 버전을 고정한다.
- `>=`는 최소 버전을 지정한다.
- `~=`는 호환 가능한 버전을 허용한다.
- 정확한 고정은 재현성에 유리하다.
- 너무 엄격한 고정은 업데이트를 어렵게 할 수 있다.
- 보안 업데이트를 위해 주기적 점검이 필요하다.
- 배포형 Tool은 버전 범위 관리가 필요할 수 있다.
- 개인 자동화는 정확한 버전 고정으로 재현성을 확보하기 쉽다.

---

### [실무]

정확한 버전 고정:

```text
requests==2.32.3
pytest==8.3.3
```

최소 버전 지정:

```text
requests>=2.32.0
```

호환 버전 지정:

```text
requests~=2.32
```

자동화 프로젝트 권장:

```text
개인 로컬 자동화
→ requirements.txt + 주요 패키지 버전 고정

배포형 Tool
→ pyproject.toml + 의존성 범위 관리

장기 운영 자동화
→ 보안 업데이트 주기 설정
```

---

### [FAQ]

Q. Version Pinning은 왜 필요해?

A. 패키지 업데이트로 자동화 스크립트 동작이 바뀌는 것을 줄이기 위해 필요하다.

Q. `==`는 무엇을 의미해?

A. 정확히 해당 버전만 설치하겠다는 의미이다.

Q. `>=`는 무엇을 의미해?

A. 해당 버전 이상을 허용한다는 의미이다.

Q. 모든 패키지를 최신으로만 두면 좋아?

A. 아니다. 최신 버전이 기존 코드와 호환되지 않을 수 있으므로 검증이 필요하다.

---

# 5. pyproject.toml

## 5.1 pyproject.toml Role

### [개념]

`pyproject.toml`은 Python 프로젝트의 메타데이터, 빌드 설정, 의존성, 도구 설정을 관리하는 표준 설정 파일이다.

Python 자동화 프로젝트가 단순 스크립트를 넘어 Package 구조로 확장될 때 유용하다.

```toml
[project]
name = "python-ai-automation"
version = "0.1.0"
dependencies = [
  "requests",
  "python-dotenv"
]
```

---

### [핵심]

- `pyproject.toml`은 Python 프로젝트 표준 설정 파일이다.
- 프로젝트 이름, 버전, 의존성을 정의할 수 있다.
- ruff, black, pytest 같은 도구 설정을 함께 관리할 수 있다.
- Package 구조 프로젝트에 적합하다.
- 단순 스크립트는 requirements.txt만으로 충분할 수 있다.
- 프로젝트가 커지면 pyproject.toml을 고려한다.
- Agent Tool Script가 여러 모듈로 분리되면 pyproject.toml이 유용하다.

---

### [실무]

기본 예시:

```toml
[project]
name = "python-ai-automation"
version = "0.1.0"
description = "Python automation tools for RAG documents and agent scripts"
requires-python = ">=3.11"
dependencies = [
  "requests",
  "python-dotenv",
  "pyyaml",
]

[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
  "black",
]
```

pytest 설정:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

ruff 설정:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"
```

---

### [FAQ]

Q. pyproject.toml은 언제 사용해?

A. Python 프로젝트가 Package 구조로 커지고 의존성, 테스트, 린트 설정을 통합 관리하고 싶을 때 사용한다.

Q. requirements.txt와 pyproject.toml 중 무엇을 써야 해?

A. 단순 스크립트는 requirements.txt로 충분하고, Package 구조나 도구 설정이 필요하면 pyproject.toml을 고려한다.

Q. pyproject.toml에 테스트 설정도 넣을 수 있어?

A. 가능하다. pytest, ruff, black 같은 도구 설정을 넣을 수 있다.

Q. 개인 자동화 스크립트에도 pyproject.toml이 꼭 필요해?

A. 아니다. 단순 자동화라면 requirements.txt만으로도 충분하다.

---

# 6. Dependency Management

## 6.1 Dependency Management Role

### [개념]

Dependency Management는 Python 프로젝트에서 사용하는 외부 패키지와 버전을 안정적으로 관리하는 작업이다.

AI Automation Script는 API 호출, 파일 처리, 데이터 처리, 테스트 도구에 의존하므로 의존성 관리가 코드 재현성과 안정성에 직접 영향을 준다.

기본 Flow:

```text
Select Package
→ Install in venv
→ Test Script
→ Record Dependency
→ Review Version
→ Update Safely
```

---

### [핵심]

- 필요한 패키지만 설치한다.
- 패키지 설치 후 자동화 스크립트를 테스트한다.
- 의존성 목록을 기록한다.
- 버전 충돌을 확인한다.
- 사용하지 않는 패키지는 제거한다.
- 보안 취약 패키지는 업데이트한다.
- 새 패키지 추가 전 표준 라이브러리로 가능한지 검토한다.
- Agent Tool 배포 시 실행 환경을 문서화한다.
- 의존성 변경 후 requirements.txt 또는 pyproject.toml을 갱신한다.

---

### [실무]

의존성 관리 Checklist:

```text
- venv 활성화 확인
- 필요한 패키지만 설치
- requirements.txt 갱신
- python -m pip check 실행
- 테스트 실행
- 사용하지 않는 패키지 제거
- 보안 업데이트 확인
- README에 실행 방법 기록
```

패키지 충돌 확인:

```bash
python -m pip check
```

패키지 제거:

```bash
python -m pip uninstall package-name
```

새 환경 재현 테스트:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

---

### [FAQ]

Q. Dependency Management는 왜 중요해?

A. 패키지 버전 차이로 자동화 스크립트가 실패하거나 다르게 동작할 수 있기 때문이다.

Q. 새 패키지는 바로 추가해도 돼?

A. 표준 라이브러리로 가능한지 먼저 검토하고, 필요할 때만 추가한다.

Q. 사용하지 않는 패키지는 지워야 해?

A. 그렇다. 불필요한 의존성은 보안 위험과 관리 부담을 늘린다.

Q. pip check는 무엇을 해?

A. 설치된 패키지들의 의존성 충돌 여부를 확인한다.

---

## 6.2 Security Update

### [개념]

Security Update는 Python 패키지의 보안 취약점을 줄이기 위해 의존성을 점검하고 필요한 업데이트를 적용하는 작업이다.

자동화 스크립트가 API Key, 파일, 외부 입력을 다루는 경우 패키지 보안 관리가 중요하다.

---

### [핵심]

- 오래된 패키지는 보안 취약점이 있을 수 있다.
- 무조건 최신 버전으로 올리기보다 테스트 후 업데이트한다.
- API Key 처리 패키지, YAML Parser, HTTP Client는 특히 주의한다.
- 업데이트 후 자동화 테스트를 실행한다.
- requirements.txt를 갱신한다.
- 사용하지 않는 패키지는 제거한다.
- 신뢰할 수 없는 패키지 설치를 피한다.
- Secret 처리와 외부 입력 처리 패키지는 우선 점검한다.

---

### [실무]

패키지 업데이트:

```bash
python -m pip install --upgrade requests
```

requirements 갱신:

```bash
python -m pip freeze > requirements.txt
```

업데이트 후 테스트:

```bash
python -m pytest
```

권장 정책:

```text
Patch Update
→ 테스트 후 반영

Major Update
→ 변경사항 확인 후 반영

Unknown Package
→ 설치 전 검토

Unused Package
→ 제거
```

---

### [FAQ]

Q. Python 패키지는 항상 최신으로 유지해야 해?

A. 보안상 업데이트는 필요하지만, 자동화 코드 호환성을 테스트한 뒤 반영해야 한다.

Q. 보안상 특히 주의할 패키지는?

A. HTTP Client, YAML Parser, 인증 관련 패키지, 외부 입력 처리 패키지이다.

Q. 패키지 업데이트 후 무엇을 해야 해?

A. 자동화 스크립트와 테스트를 실행해 기존 동작이 유지되는지 확인한다.

Q. 모르는 패키지를 설치해도 돼?

A. 권장하지 않는다. 출처, 유지보수 상태, 필요성을 확인해야 한다.

---

# 7. CLI Script Overview

## 7.1 CLI Script Role

### [개념]

CLI Script는 터미널에서 명령어와 옵션으로 실행할 수 있는 Python 자동화 스크립트이다.

Python for AI Automation에서는 RAG 문서 검사, Markdown 변환, JSON 리포트 생성, CSV 메타데이터 생성, Agent Tool 로컬 실행에 CLI Script를 사용할 수 있다.

Part09의 CLI 구조는 Part10의 Agent Tool Script 실행 기반이 된다.

기본 Flow:

```text
Command
→ Parse Arguments
→ Validate Arguments
→ Execute Task
→ Print Structured Output
→ Return Exit Code
```

---

### [핵심]

- CLI Script는 반복 작업 자동화에 적합하다.
- 입력 파일, 입력 폴더, 출력 경로를 인자로 받는다.
- `argparse`를 사용해 인자를 처리할 수 있다.
- `--help` 메시지를 제공한다.
- 오류 발생 시 명확한 메시지와 Exit Code를 반환한다.
- 위험 작업에는 `--dry-run` 옵션을 제공한다.
- 하드코딩된 경로를 줄인다.
- Agent Tool Runner와 연결할 경우 JSON 출력이 유리하다.
- Part08의 TypedDict / dataclass 결과를 CLI JSON 출력으로 반환할 수 있다.

---

### [실무]

CLI 사용 예시:

```bash
python main.py --input docs --output reports/validation.json
```

dry-run 예시:

```bash
python main.py --input docs --output reports --dry-run
```

권장 CLI 옵션:

```text
--input
→ 입력 파일 또는 폴더

--output
→ 출력 파일 또는 폴더

--format
→ json / csv / markdown

--dry-run
→ 실제 수정 없이 미리보기

--verbose
→ 상세 로그 출력
```

Agent Tool 연결 관점:

```text
CLI Script
→ JSON stdout
→ Exit Code
→ Agent Tool Runner
→ Agent 후속 판단
```

---

### [FAQ]

Q. CLI Script는 왜 필요해?

A. 매번 코드를 수정하지 않고 명령어 옵션으로 자동화 작업을 반복 실행하기 위해 필요하다.

Q. CLI Script에 입력 경로를 하드코딩해도 돼?

A. 권장하지 않는다. `--input`, `--output` 인자로 받는 것이 좋다.

Q. dry-run 옵션은 왜 필요해?

A. 파일 수정이나 삭제 같은 위험 작업 전에 실제 변경 없이 결과를 확인하기 위해 필요하다.

Q. CLI Script는 Agent Tool과 연결될 수 있어?

A. 가능하다. Agent가 명령어 형태로 Tool Script를 호출할 수 있다.

Q. CLI 출력은 왜 JSON이 유리해?

A. Agent Tool Runner가 결과를 구조적으로 파싱하고 후속 판단을 하기 쉽기 때문이다.

---

# 8. argparse

## 8.1 argparse Basics

### [개념]

`argparse`는 Python 표준 라이브러리로 CLI 인자를 정의하고 파싱하는 도구이다.

입력 경로, 출력 경로, 실행 모드, 출력 형식 같은 옵션을 명령어에서 받을 수 있다.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
args = parser.parse_args()
```

---

### [핵심]

- argparse는 Python 표준 라이브러리이다.
- CLI 인자와 옵션을 정의한다.
- `required=True`로 필수 인자를 지정할 수 있다.
- `default`로 기본값을 지정할 수 있다.
- `choices`로 허용 값을 제한할 수 있다.
- help 메시지를 자동 생성한다.
- 인자 검증은 별도 함수로 보강할 수 있다.
- `--dry-run` 같은 Boolean Flag를 만들 수 있다.

---

### [실무]

기본 CLI 인자:

```python
import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate RAG Markdown documents."
    )

    parser.add_argument("--input", required=True, help="Input file or directory")
    parser.add_argument("--output", required=True, help="Output report path")
    parser.add_argument(
        "--format",
        choices=["json", "csv", "markdown"],
        default="json",
        help="Output report format",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files",
    )

    return parser.parse_args()
```

사용:

```python
from pathlib import Path

def main() -> None:
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    print(input_path)
    print(output_path)
    print(args.format)
    print(args.dry_run)


if __name__ == "__main__":
    main()
```

---

### [FAQ]

Q. argparse는 무엇이야?

A. Python에서 CLI 명령어 인자와 옵션을 처리하는 표준 라이브러리이다.

Q. required=True는 무엇이야?

A. 해당 CLI 인자를 필수로 입력하게 만드는 설정이다.

Q. choices는 언제 사용해?

A. `json`, `csv`, `markdown`처럼 허용 가능한 값이 정해져 있을 때 사용한다.

Q. action="store_true"는 언제 사용해?

A. `--dry-run` 같은 Boolean Flag 옵션을 만들 때 사용한다.

---

## 8.2 Argument Validation

### [개념]

Argument Validation은 CLI로 입력받은 값이 실제로 유효한지 검사하는 작업이다.

자동화 스크립트는 잘못된 입력 경로, 잘못된 출력 형식, 위험한 실행 모드를 초기에 차단해야 한다.

---

### [핵심]

- CLI 인자는 문자열로 들어온다.
- 입력 경로 존재 여부를 확인한다.
- 입력이 파일인지 폴더인지 확인한다.
- 출력 폴더 생성 가능 여부를 확인한다.
- 숫자 인자는 범위를 확인한다.
- 허용 값은 `choices` 또는 별도 검증으로 제한한다.
- 위험 작업은 명시적 옵션을 요구한다.
- Agent Tool에서 전달한 인자도 신뢰하지 않고 검증한다.

---

### [실무]

입력 경로 검증:

```python
from pathlib import Path

def validate_input_path(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Input path not found: {path}")
```

출력 경로 준비:

```python
from pathlib import Path

def prepare_output_path(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
```

chunk_size 검증:

```python
def validate_chunk_size(chunk_size: int) -> None:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
```

CLI 통합:

```python
from pathlib import Path

def main() -> None:
    args = parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    validate_input_path(input_path)
    prepare_output_path(output_path)
```

---

### [FAQ]

Q. CLI Argument Validation은 왜 필요해?

A. 잘못된 입력으로 파일 훼손, 실행 실패, 잘못된 리포트 생성을 막기 위해 필요하다.

Q. argparse가 모든 검증을 자동으로 해줘?

A. 아니다. required, choices 같은 기본 검증은 가능하지만 파일 존재 여부 같은 검증은 직접 해야 한다.

Q. 입력 경로는 무엇을 검사해야 해?

A. 존재 여부, 파일 여부, 폴더 여부, 접근 권한을 검사한다.

Q. 위험 작업은 어떻게 보호해?

A. `--dry-run`, `--confirm`, `--overwrite` 같은 명시적 옵션을 요구한다.

---

# 9. Exit Code

## 9.1 Exit Code Role

### [개념]

Exit Code는 CLI Script 실행 결과를 운영체제나 다른 자동화 도구에 전달하는 숫자 코드이다.

일반적으로 `0`은 성공, `0이 아닌 값`은 실패를 의미한다.

```text
0 → Success
1 → General Error
2 → Invalid Argument
```

---

### [핵심]

- Exit Code는 자동화 파이프라인에서 중요하다.
- 성공 시 `0`을 반환한다.
- 실패 시 `1` 또는 의미 있는 오류 코드를 반환한다.
- CI/CD, Shell Script, Agent Tool Runner가 Exit Code를 확인할 수 있다.
- Python에서는 `sys.exit(code)`를 사용할 수 있다.
- 오류 메시지와 Exit Code를 함께 제공하는 것이 좋다.
- Agent Tool Runner는 Exit Code와 JSON Output을 함께 해석할 수 있다.

---

### [실무]

기본 Exit Code:

```python
import sys

def main() -> int:
    try:
        run_task()
        return 0
    except ValueError as error:
        print(f"Invalid input: {error}")
        return 2
    except Exception as error:
        print(f"Task failed: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

권장 코드:

```text
0
→ Success

1
→ General Error

2
→ Invalid Argument

3
→ Validation Failed

4
→ File Error

5
→ API Error
```

Agent Tool Runner 연결:

```text
CLI Script
→ Exit Code
→ JSON stdout
→ Agent Tool Runner
→ Success / Error Handling
```

---

### [FAQ]

Q. Exit Code는 왜 필요해?

A. 자동화 도구나 Agent Runner가 스크립트 성공 여부를 판단하기 위해 필요하다.

Q. 성공 Exit Code는 무엇이야?

A. 일반적으로 `0`이다.

Q. 실패 Exit Code는 무엇이야?

A. 일반적으로 `1` 또는 오류 유형별 숫자를 사용한다.

Q. Python에서 Exit Code는 어떻게 반환해?

A. `sys.exit(code)`를 사용한다.

---

# 10. CLI Script Best Practice

## 10.1 Best Practice

### [개념]

CLI Script Best Practice는 Python 자동화 스크립트를 터미널, Agent Tool Runner, Batch Workflow에서 안정적으로 실행하기 위한 기준이다.

목표:

```text
Parse Arguments
→ Validate Inputs
→ Execute Task
→ Save Output
→ Print JSON Summary
→ Return Exit Code
```

---

### [핵심]

- `argparse`로 CLI 인자를 정의한다.
- `--help` 메시지를 제공한다.
- 입력 경로와 출력 경로를 인자로 받는다.
- 인자 검증을 수행한다.
- 출력 폴더를 준비한다.
- 위험 작업은 `--dry-run` 또는 `--confirm`을 요구한다.
- 오류 메시지는 명확하게 작성한다.
- Exit Code를 반환한다.
- 핵심 로직은 main 밖의 함수로 분리한다.
- CLI 출력과 로그를 구분한다.
- Agent Tool에서 호출 가능한 구조를 고려한다.
- Agent Tool 연동용 출력은 JSON 구조가 좋다.
- Part08의 ToolOutput 구조와 맞추면 후속 처리가 쉽다.

---

### [실무]

통합 CLI 예시:

```python
import argparse
import json
import sys
from pathlib import Path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate RAG Markdown documents."
    )

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
    )
    parser.add_argument("--dry-run", action="store_true")

    return parser.parse_args()


def validate_input_path(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Input path not found: {path}")


def build_result(input_path: Path) -> dict:
    return {
        "status": "success",
        "result": {
            "input": str(input_path),
        },
        "error": None,
    }


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    try:
        args = parse_args()
        input_path = Path(args.input)
        output_path = Path(args.output)

        validate_input_path(input_path)

        result = build_result(input_path)

        if not args.dry_run:
            save_json(output_path, result)

        print(json.dumps(result, ensure_ascii=False))
        return 0

    except FileNotFoundError as error:
        output = {
            "status": "error",
            "result": None,
            "error": str(error),
        }
        print(json.dumps(output, ensure_ascii=False))
        return 4

    except Exception as error:
        output = {
            "status": "error",
            "result": None,
            "error": str(error),
        }
        print(json.dumps(output, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

검수 Checklist:

```text
- argparse 사용
- --help 제공
- input/output 인자 사용
- 입력 경로 검증
- 출력 폴더 준비
- dry-run 지원
- overwrite 보호
- 명확한 오류 메시지
- JSON stdout 지원
- Exit Code 반환
- 핵심 로직 함수 분리
```

---

### [FAQ]

Q. CLI Script Best Practice는 무엇이야?

A. argparse 사용, 입력 검증, dry-run, 구조화된 출력, 명확한 오류 메시지, Exit Code 반환을 적용하는 기준이다.

Q. CLI Script에서 핵심 로직은 어디에 둬야 해?

A. 테스트 가능하도록 main 밖의 독립 함수에 둔다.

Q. CLI 출력은 어떤 형태가 좋아?

A. Agent Tool Runner와 연결할 수 있도록 JSON 문자열 또는 명확한 Summary가 좋다.

Q. CLI Script에서 파일 수정은 어떻게 보호해?

A. `--dry-run`, `--confirm`, `--overwrite` 같은 옵션으로 보호한다.

---

# 11. Script Packaging

## 11.1 Script vs Package Execution

### [개념]

Script Execution은 Python 파일을 직접 실행하는 방식이고, Package Execution은 Package 구조에서 Module을 실행하는 방식이다.

자동화 프로젝트가 커지면 단일 Script 실행보다 Package Execution 구조가 안정적일 수 있다.

```bash
python main.py
python -m ai_automation.main
```

---

### [핵심]

- `python main.py`는 단일 파일 실행에 적합하다.
- `python -m package.module`은 Package 구조 실행에 적합하다.
- Package Execution은 Import 경로 관리에 유리하다.
- 프로젝트가 커지면 `src` 구조와 Package Execution을 고려한다.
- Agent Tool Script는 실행 방식을 문서화해야 한다.
- 실행 명령, 입력 인자, 출력 형식, Exit Code를 함께 기록한다.

---

### [실무]

단순 Script 실행:

```bash
python main.py --input docs --output reports/result.json
```

Package 실행:

```bash
python -m ai_automation.main --input docs --output reports/result.json
```

권장 Package 구조:

```text
python_ai_automation
├ pyproject.toml
├ .env.example
├ src
│  └ ai_automation
│     ├ __init__.py
│     ├ main.py
│     ├ cli.py
│     ├ validator.py
│     └ report.py
└ tests
```

`cli.py` 역할:

```text
parse_args
→ validate_args
→ call_service
→ print_result
→ return_exit_code
```

---

### [FAQ]

Q. `python main.py`와 `python -m package.module` 차이는?

A. 전자는 파일 직접 실행이고 후자는 Package Module 실행이다.

Q. Package Execution은 왜 좋아?

A. Import 경로가 안정적이고 프로젝트 구조가 커져도 관리하기 쉽다.

Q. 단순 자동화는 main.py 실행으로 충분해?

A. 그렇다. 작은 프로젝트는 `python main.py`로 충분하다.

Q. Agent Tool Script 실행 방식은 문서화해야 해?

A. 그렇다. 실행 명령, 인자, 출력 형식, Exit Code를 명확히 기록해야 한다.

---

# 12. Virtual Environment CLI Dependency Best Practice

## 12.1 Best Practice

### [개념]

Virtual Environment CLI Dependency Best Practice는 Python 자동화 프로젝트의 실행 환경, 의존성, CLI 실행 방식을 안정적으로 관리하기 위한 기준이다.

목표:

```text
Isolated Environment
→ Recorded Dependency
→ Validated CLI
→ JSON Output
→ Reproducible Execution
→ Agent Tool Ready
```

---

### [핵심]

- 프로젝트마다 Virtual Environment를 사용한다.
- `.venv`는 Git에 올리지 않는다.
- `python -m pip`를 사용한다.
- 설치한 패키지는 `requirements.txt` 또는 `pyproject.toml`에 기록한다.
- 단순 자동화는 requirements.txt로 시작한다.
- Package 구조는 pyproject.toml을 고려한다.
- 패키지 추가 후 테스트한다.
- 사용하지 않는 패키지는 제거한다.
- CLI는 argparse로 작성한다.
- CLI는 input, output, format, dry-run 옵션을 제공한다.
- 인자 검증과 Exit Code를 제공한다.
- Agent Tool 실행용으로 JSON 출력 구조를 고려한다.
- `.env`와 `.env.example` 역할을 분리한다.
- 실행 방법을 README 또는 RAG 문서에 기록한다.

---

### [실무]

프로젝트 초기화 예시:

```bash
mkdir python_ai_automation
cd python_ai_automation
python -m venv .venv
source .venv/bin/activate
python -m pip install requests python-dotenv pyyaml pytest
python -m pip freeze > requirements.txt
```

`.gitignore` 예시:

```text
.venv
.env
__pycache__/
.pytest_cache/
*.pyc
```

`.env.example` 예시:

```text
LLM_API_KEY=
LLM_BASE_URL=
DEFAULT_TIMEOUT=30
MODEL_NAME=qwen2.5
```

실행 문서 예시:

```text
Setup
→ python -m venv .venv
→ source .venv/bin/activate
→ python -m pip install -r requirements.txt

Run
→ python main.py --input docs --output reports/result.json --format json

Test
→ python -m pytest
```

Agent Tool Ready Checklist:

```text
- 실행 명령 명확
- 입력 인자 명확
- 출력 JSON 구조 명확
- Exit Code 명확
- requirements.txt 존재
- .env.example 존재
- .venv Git 제외
- 테스트 명령 존재
```

---

### [FAQ]

Q. Virtual Environment CLI Dependency Best Practice는 무엇이야?

A. 가상환경, 의존성 기록, CLI 인자 검증, Exit Code, JSON 출력, 재현 가능한 실행 방법을 관리하는 기준이다.

Q. Python 자동화 프로젝트를 처음 만들 때 순서는?

A. 프로젝트 폴더 생성 → venv 생성 → 활성화 → 패키지 설치 → requirements.txt 생성 → CLI 작성 → 테스트 순서가 좋다.

Q. Agent Tool로 쓰려면 CLI에 무엇이 필요해?

A. 명확한 입력 인자, JSON 출력, Exit Code, 구조화된 오류 메시지가 필요하다.

Q. 실행 방법은 어디에 기록해야 해?

A. README, RAG 문서, Agent Tool Description에 기록하는 것이 좋다.

Q. `.env`와 `.env.example`은 어떻게 다르게 관리해?

A. `.env`는 실제 Secret을 저장하고 Git에서 제외하며, `.env.example`은 필요한 변수 이름만 기록해 Git에 포함할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Python Virtual Environment는 무엇이야?
A. 프로젝트별 Python 패키지 의존성을 격리하는 실행 환경이다.

Q. Python 자동화에서 Virtual Environment는 왜 필요해?
A. 프로젝트별 패키지 버전을 분리해 의존성 충돌과 전역 환경 오염을 막기 위해 필요하다.

Q. Python 프로젝트마다 venv를 만들어야 해?
A. 권장한다. 프로젝트별 실행 환경을 독립적으로 관리할 수 있기 때문이다.

Q. `.venv` 폴더는 Git에 올려도 돼?
A. 안 된다. `.gitignore`에 추가하고 의존성 목록만 기록한다.

Q. `.env.example`은 왜 같이 두는 게 좋아?
A. 실제 Secret을 공유하지 않고 필요한 환경변수 이름과 기본 설정 구조를 문서화할 수 있기 때문이다.

Q. Virtual Environment 없이 pip install 해도 돼?
A. 가능하지만 전역 환경이 오염되고 다른 프로젝트와 패키지 버전이 충돌할 수 있으므로 권장하지 않는다.

Q. Python venv는 설치해야 해?
A. 일반적으로 Python 표준 라이브러리에 포함되어 있어 별도 설치가 필요 없다.

Q. Python venv는 어떻게 생성해?
A. `python -m venv .venv` 명령으로 생성한다.

Q. `.venv`라는 이름을 꼭 써야 해?
A. 필수는 아니지만 Python 프로젝트에서 관례적으로 많이 사용한다.

Q. 가상환경은 Python 버전을 따로 설치해?
A. 가상환경은 생성에 사용한 Python 실행 파일 기준으로 구성된다.

Q. `.venv`를 삭제해도 돼?
A. 가능하다. `requirements.txt` 또는 `pyproject.toml`이 있으면 다시 만들 수 있다.

Q. venv 활성화는 왜 필요해?
A. 현재 터미널에서 프로젝트 전용 Python과 패키지를 사용하기 위해 필요하다.

Q. Linux에서 venv는 어떻게 활성화해?
A. `source .venv/bin/activate` 명령을 사용한다.

Q. macOS에서 venv는 어떻게 활성화해?
A. `source .venv/bin/activate` 명령을 사용한다.

Q. Windows PowerShell에서 venv는 어떻게 활성화해?
A. `.venv\Scripts\Activate.ps1` 명령을 사용한다.

Q. Windows CMD에서 venv는 어떻게 활성화해?
A. `.venv\Scripts\activate.bat` 명령을 사용한다.

Q. venv가 활성화되었는지 어떻게 확인해?
A. Prompt의 `(.venv)` 표시, `which python`, `where python`, `python -m pip --version`으로 확인한다.

Q. deactivate는 무엇을 해?
A. 현재 터미널에서 활성화된 가상환경을 종료한다.

Q. VS Code나 IDE에서도 venv를 설정해야 해?
A. 그렇다. IDE Interpreter를 프로젝트 `.venv`로 지정해야 설치 패키지를 정상 인식한다.

Q. Python pip는 무엇이야?
A. Python 외부 패키지를 설치하고 관리하는 도구이다.

Q. `pip install`과 `python -m pip install` 중 무엇을 권장해?
A. `python -m pip install`을 권장한다. 현재 Python Interpreter와 연결된 pip를 명확히 사용할 수 있기 때문이다.

Q. 패키지는 가상환경 활성화 후 설치해야 해?
A. 그렇다. 그래야 프로젝트별 의존성이 분리된다.

Q. 설치한 패키지 목록은 어떻게 확인해?
A. `python -m pip list`를 사용한다.

Q. Python 자동화 기본 패키지는 무엇이야?
A. `requests`, `python-dotenv`, `pyyaml`, `pytest`를 기본으로 고려할 수 있다.

Q. pandas는 항상 설치해야 해?
A. 아니다. 표 형태 데이터 분석이나 CSV 가공이 필요할 때만 설치한다.

Q. httpx는 언제 설치해?
A. 비동기 API 호출이나 Async Workflow가 필요할 때 설치한다.

Q. black과 ruff는 꼭 필요해?
A. 필수는 아니지만 코드 포맷팅과 정적 품질 검사를 위해 권장할 수 있다.

Q. requirements.txt는 왜 필요해?
A. 자동화 스크립트를 다른 환경에서도 같은 패키지 버전으로 실행하기 위해 필요하다.

Q. requirements.txt는 어떻게 생성해?
A. `python -m pip freeze > requirements.txt` 명령으로 생성한다.

Q. requirements.txt로 설치하려면?
A. `python -m pip install -r requirements.txt`를 사용한다.

Q. `.venv` 대신 requirements.txt를 Git에 올리는 이유는?
A. `.venv`는 크고 환경 의존적이므로 제외하고 의존성 목록만 공유하기 위해서이다.

Q. Version Pinning은 왜 필요해?
A. 패키지 업데이트로 자동화 스크립트 동작이 바뀌는 것을 줄이기 위해 필요하다.

Q. requirements.txt에서 `==`는 무엇을 의미해?
A. 정확히 해당 버전만 설치하겠다는 의미이다.

Q. requirements.txt에서 `>=`는 무엇을 의미해?
A. 해당 버전 이상을 허용한다는 의미이다.

Q. 모든 패키지를 최신으로만 두면 좋아?
A. 아니다. 최신 버전이 기존 코드와 호환되지 않을 수 있으므로 검증이 필요하다.

Q. pyproject.toml은 언제 사용해?
A. Python 프로젝트가 Package 구조로 커지고 의존성, 테스트, 린트 설정을 통합 관리하고 싶을 때 사용한다.

Q. requirements.txt와 pyproject.toml 중 무엇을 써야 해?
A. 단순 스크립트는 requirements.txt로 충분하고, Package 구조나 도구 설정이 필요하면 pyproject.toml을 고려한다.

Q. pyproject.toml에 테스트 설정도 넣을 수 있어?
A. 가능하다. pytest, ruff, black 같은 도구 설정을 넣을 수 있다.

Q. 개인 자동화 스크립트에도 pyproject.toml이 꼭 필요해?
A. 아니다. 단순 자동화라면 requirements.txt만으로도 충분하다.

Q. Dependency Management는 왜 중요해?
A. 패키지 버전 차이로 자동화 스크립트가 실패하거나 다르게 동작할 수 있기 때문이다.

Q. 새 패키지는 바로 추가해도 돼?
A. 표준 라이브러리로 가능한지 먼저 검토하고, 필요할 때만 추가한다.

Q. 사용하지 않는 패키지는 지워야 해?
A. 그렇다. 불필요한 의존성은 보안 위험과 관리 부담을 늘린다.

Q. pip check는 무엇을 해?
A. 설치된 패키지들의 의존성 충돌 여부를 확인한다.

Q. Python 패키지는 항상 최신으로 유지해야 해?
A. 보안상 업데이트는 필요하지만, 자동화 코드 호환성을 테스트한 뒤 반영해야 한다.

Q. 보안상 특히 주의할 패키지는?
A. HTTP Client, YAML Parser, 인증 관련 패키지, 외부 입력 처리 패키지이다.

Q. 패키지 업데이트 후 무엇을 해야 해?
A. 자동화 스크립트와 테스트를 실행해 기존 동작이 유지되는지 확인한다.

Q. 모르는 패키지를 설치해도 돼?
A. 권장하지 않는다. 출처, 유지보수 상태, 필요성을 확인해야 한다.

Q. Python CLI Script는 무엇이야?
A. 터미널에서 명령어와 옵션으로 실행할 수 있는 Python 자동화 스크립트이다.

Q. CLI Script는 왜 필요해?
A. 매번 코드를 수정하지 않고 명령어 옵션으로 자동화 작업을 반복 실행하기 위해 필요하다.

Q. CLI Script에 입력 경로를 하드코딩해도 돼?
A. 권장하지 않는다. `--input`, `--output` 인자로 받는 것이 좋다.

Q. dry-run 옵션은 왜 필요해?
A. 파일 수정이나 삭제 같은 위험 작업 전에 실제 변경 없이 결과를 확인하기 위해 필요하다.

Q. CLI Script는 Agent Tool과 연결될 수 있어?
A. 가능하다. Agent가 명령어 형태로 Tool Script를 호출할 수 있다.

Q. CLI 출력은 왜 JSON이 유리해?
A. Agent Tool Runner가 결과를 구조적으로 파싱하고 후속 판단을 하기 쉽기 때문이다.

Q. argparse는 무엇이야?
A. Python에서 CLI 명령어 인자와 옵션을 처리하는 표준 라이브러리이다.

Q. argparse required=True는 무엇이야?
A. 해당 CLI 인자를 필수로 입력하게 만드는 설정이다.

Q. argparse choices는 언제 사용해?
A. `json`, `csv`, `markdown`처럼 허용 가능한 값이 정해져 있을 때 사용한다.

Q. argparse action="store_true"는 언제 사용해?
A. `--dry-run` 같은 Boolean Flag 옵션을 만들 때 사용한다.

Q. CLI Argument Validation은 왜 필요해?
A. 잘못된 입력으로 파일 훼손, 실행 실패, 잘못된 리포트 생성을 막기 위해 필요하다.

Q. argparse가 모든 검증을 자동으로 해줘?
A. 아니다. required, choices 같은 기본 검증은 가능하지만 파일 존재 여부 같은 검증은 직접 해야 한다.

Q. CLI 입력 경로는 무엇을 검사해야 해?
A. 존재 여부, 파일 여부, 폴더 여부, 접근 권한을 검사한다.

Q. CLI 위험 작업은 어떻게 보호해?
A. `--dry-run`, `--confirm`, `--overwrite` 같은 명시적 옵션을 요구한다.

Q. Exit Code는 왜 필요해?
A. 자동화 도구나 Agent Runner가 스크립트 성공 여부를 판단하기 위해 필요하다.

Q. 성공 Exit Code는 무엇이야?
A. 일반적으로 `0`이다.

Q. 실패 Exit Code는 무엇이야?
A. 일반적으로 `1` 또는 오류 유형별 숫자를 사용한다.

Q. Python에서 Exit Code는 어떻게 반환해?
A. `sys.exit(code)`를 사용한다.

Q. CLI Script Best Practice는 무엇이야?
A. argparse 사용, 입력 검증, dry-run, 구조화된 출력, 명확한 오류 메시지, Exit Code 반환을 적용하는 기준이다.

Q. CLI Script에서 핵심 로직은 어디에 둬야 해?
A. 테스트 가능하도록 main 밖의 독립 함수에 둔다.

Q. CLI 출력은 어떤 형태가 좋아?
A. Agent Tool Runner와 연결할 수 있도록 JSON 문자열 또는 명확한 Summary가 좋다.

Q. CLI Script에서 파일 수정은 어떻게 보호해?
A. `--dry-run`, `--confirm`, `--overwrite` 같은 옵션으로 보호한다.

Q. `python main.py`와 `python -m package.module` 차이는?
A. 전자는 파일 직접 실행이고 후자는 Package Module 실행이다.

Q. Package Execution은 왜 좋아?
A. Import 경로가 안정적이고 프로젝트 구조가 커져도 관리하기 쉽다.

Q. 단순 자동화는 main.py 실행으로 충분해?
A. 그렇다. 작은 프로젝트는 `python main.py`로 충분하다.

Q. Agent Tool Script 실행 방식은 문서화해야 해?
A. 그렇다. 실행 명령, 인자, 출력 형식, Exit Code를 명확히 기록해야 한다.

Q. Python 자동화 프로젝트를 처음 만들 때 순서는?
A. 프로젝트 폴더 생성 → venv 생성 → 활성화 → 패키지 설치 → requirements.txt 생성 → CLI 작성 → 테스트 순서가 좋다.

Q. Agent Tool로 쓰려면 CLI에 무엇이 필요해?
A. 명확한 입력 인자, JSON 출력, Exit Code, 구조화된 오류 메시지가 필요하다.

Q. 실행 방법은 어디에 기록해야 해?
A. README, RAG 문서, Agent Tool Description에 기록하는 것이 좋다.

Q. `.env`와 `.env.example`은 어떻게 다르게 관리해?
A. `.env`는 실제 Secret을 저장하고 Git에서 제외하며, `.env.example`은 필요한 변수 이름만 기록해 Git에 포함할 수 있다.

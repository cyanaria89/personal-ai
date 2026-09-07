import unittest

import agents.nodes as nodes


PROJECT_PLAN = """```text
REQUIRED_AGENTS: db, backend, frontend

REQUEST_SUMMARY:
KEEP_REQUEST_SUMMARY 회원가입 구현

EXECUTION_ORDER:
REMOVE_EXECUTION_ORDER

DB_HANDOFF:
REMOVE_DB_HANDOFF

BACKEND_HANDOFF:
REMOVE_BACKEND_HANDOFF

FRONTEND_HANDOFF:
- KEEP_FRONTEND_HANDOFF
- Submit 시 /api/signup 호출
```"""

BACKEND_RESULT = """# Backend Agent Output

## Implementation

### Entity

```java
class REMOVE_ENTITY {}
```

### Repository

```java
interface REMOVE_REPOSITORY {}
```

### Service

```java
class REMOVE_SERVICE {}
```

### Controller

```java
class KEEP_CONTROLLER {
    // POST /api/signup returns 200
}
```

## Notes

REMOVE_NOTES

## Frontend Handoff

- KEEP_FRONTEND_HANDOFF_CONTRACT
- POST /api/signup
- Success: 200
"""

PREVIOUS_FRONTEND = "KEEP_PREVIOUS_FRONTEND_RESULT"
USER_REQUEST = "KEEP_USER_REQUEST 회원가입 화면 구현"


def base_state() -> dict:
    return {
        "user_request": USER_REQUEST,
        "required_agents": ["backend", "frontend"],
        "project_plan": PROJECT_PLAN,
        "backend_result": BACKEND_RESULT,
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": PREVIOUS_FRONTEND,
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "NOT_RUN", "issues": []},
        "integration_fix_count": 0,
        "llm_metrics": [],
    }


def validator_fix_state() -> dict:
    state = base_state()
    state["frontend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "rule": "UNSAFE_CATCH_ERROR_ACCESS",
            "required_fix": "KEEP_VALIDATOR_ISSUE",
        }],
    }
    return state


def integration_fix_state() -> dict:
    state = base_state()
    state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "rule": "SUCCESS_STATUS_MISMATCH",
            "target_agent": "frontend",
            "required_fix": "KEEP_INTEGRATION_ISSUE",
        }],
    }
    return state


def run_frontend_agent(state: dict) -> tuple[dict, object, str]:
    captured = {}
    original_invoke_agent = nodes.invoke_agent

    def fake_invoke(llm, system_prompt, user_prompt):
        del system_prompt
        captured["llm"] = llm
        captured["prompt"] = user_prompt
        return "UPDATED_FRONTEND"

    nodes.invoke_agent = fake_invoke
    try:
        result = nodes.frontend_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent

    return result, captured["llm"], captured["prompt"]


def assert_compact_context(prompt: str) -> None:
    assert "KEEP_REQUEST_SUMMARY" in prompt
    assert "KEEP_FRONTEND_HANDOFF" in prompt
    assert "REMOVE_DB_HANDOFF" not in prompt
    assert "REMOVE_BACKEND_HANDOFF" not in prompt
    assert "REMOVE_EXECUTION_ORDER" not in prompt
    assert "KEEP_CONTROLLER" in prompt
    assert "KEEP_FRONTEND_HANDOFF_CONTRACT" in prompt
    assert "REMOVE_ENTITY" not in prompt
    assert "REMOVE_REPOSITORY" not in prompt
    assert "REMOVE_SERVICE" not in prompt
    assert "REMOVE_NOTES" not in prompt


def test_project_context_extracts_only_required_sections() -> None:
    context = nodes.extract_frontend_fix_project_context(PROJECT_PLAN)
    assert "REQUEST_SUMMARY:" in context
    assert "KEEP_REQUEST_SUMMARY" in context
    assert "FRONTEND_HANDOFF:" in context
    assert "KEEP_FRONTEND_HANDOFF" in context
    assert "DB_HANDOFF:" not in context
    assert "BACKEND_HANDOFF:" not in context
    assert "REQUIRED_AGENTS:" not in context
    assert "EXECUTION_ORDER:" not in context


def test_project_context_uses_full_fallback_for_incomplete_or_ambiguous_input() -> None:
    incomplete = "REQUEST_SUMMARY:\n회원가입 구현\n\nDB_HANDOFF:\nDB 작업"
    ambiguous = PROJECT_PLAN + "\nREQUEST_SUMMARY:\n중복 요약"
    assert nodes.extract_frontend_fix_project_context(incomplete) == incomplete
    assert nodes.extract_frontend_fix_project_context(ambiguous) == ambiguous


def test_backend_context_extracts_controller_and_frontend_handoff_only() -> None:
    context = nodes.extract_frontend_fix_backend_context(BACKEND_RESULT)
    assert "### Controller" in context
    assert "KEEP_CONTROLLER" in context
    assert "## Frontend Handoff" in context
    assert "KEEP_FRONTEND_HANDOFF_CONTRACT" in context
    assert "REMOVE_ENTITY" not in context
    assert "REMOVE_REPOSITORY" not in context
    assert "REMOVE_SERVICE" not in context
    assert "REMOVE_NOTES" not in context


def test_backend_context_uses_full_fallback_for_incomplete_or_ambiguous_input() -> None:
    incomplete = "## Controller\n\n```java\nclass Controller {}\n```"
    ambiguous = BACKEND_RESULT + "\n### API Controller\n\nSECOND_CONTROLLER"
    broken_fence = BACKEND_RESULT + "\n```java\nunclosed"
    assert nodes.extract_frontend_fix_backend_context(incomplete) == incomplete
    assert nodes.extract_frontend_fix_backend_context(ambiguous) == ambiguous
    assert nodes.extract_frontend_fix_backend_context(broken_fence) == broken_fence


def test_validator_and_integration_fix_prompts_use_compact_context() -> None:
    validator_result, validator_llm, validator_prompt = run_frontend_agent(
        validator_fix_state()
    )
    integration_result, integration_llm, integration_prompt = run_frontend_agent(
        integration_fix_state()
    )

    for prompt in (validator_prompt, integration_prompt):
        assert_compact_context(prompt)
        assert PREVIOUS_FRONTEND in prompt
        assert USER_REQUEST in prompt
        assert "[PM 관련 계획]" in prompt
        assert "[현재 Backend 관련 API 계약]" in prompt

    assert "KEEP_VALIDATOR_ISSUE" in validator_prompt
    assert "KEEP_INTEGRATION_ISSUE" in integration_prompt
    assert validator_llm is nodes.frontend_fix_llm
    assert integration_llm is nodes.frontend_fix_llm
    assert validator_result["frontend_fix_count"] == 1
    assert validator_result["integration_fix_count"] == 0
    assert integration_result["frontend_fix_count"] == 0
    assert integration_result["integration_fix_count"] == 1


def test_initial_frontend_prompt_projects_pm_and_falls_back_for_backend_without_dto() -> None:
    state = base_state()
    state["frontend_result"] = ""
    result, selected_llm, prompt = run_frontend_agent(state)

    assert "KEEP_REQUEST_SUMMARY" in prompt
    assert "KEEP_FRONTEND_HANDOFF" in prompt
    assert BACKEND_RESULT in prompt
    assert "REMOVE_DB_HANDOFF" not in prompt
    assert "REMOVE_BACKEND_HANDOFF" not in prompt
    assert "REMOVE_ENTITY" in prompt
    assert "[PM 계획 및 Handoff]" in prompt
    assert "[Backend Agent 결과]" in prompt
    assert selected_llm is nodes.frontend_llm
    assert result["frontend_fix_count"] == 0
    assert result["integration_fix_count"] == 0


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)

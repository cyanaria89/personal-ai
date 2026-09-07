import unittest

import agents.nodes as nodes


PREVIOUS_FRONTEND = "UNIQUE_PREVIOUS_FRONTEND_RESULT_7F3A"
BACKEND_RESULT = "UNIQUE_BACKEND_RESULT_91BC"
USER_REQUEST = "UNIQUE_USER_REQUEST 회원가입 화면을 구현해줘"
PROJECT_PLAN = "UNIQUE_PROJECT_PLAN Frontend 구현 계획"


def base_state() -> dict:
    return {
        "user_request": USER_REQUEST,
        "required_agents": ["backend", "frontend"],
        "project_plan": PROJECT_PLAN,
        "db_result": "",
        "db_validation": {"status": "NOT_RUN", "issues": []},
        "db_fix_count": 0,
        "backend_result": BACKEND_RESULT,
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": PREVIOUS_FRONTEND,
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "NOT_RUN", "issues": []},
        "integration_fix_count": 0,
        "review_result": "",
        "review_status": "",
        "review_count": 0,
        "final_result": "",
    }


def run_frontend_agent(state: dict) -> tuple[dict, str]:
    captured = {}
    original_invoke_agent = nodes.invoke_agent

    def fake_invoke(llm, system_prompt, user_prompt):
        del llm, system_prompt
        captured["prompt"] = user_prompt
        return "UPDATED_FRONTEND_RESULT"

    nodes.invoke_agent = fake_invoke
    try:
        result = nodes.frontend_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent

    return result, captured["prompt"]


def frontend_validator_failure_state() -> dict:
    state = base_state()
    state["frontend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "UNSAFE_CATCH_ERROR_ACCESS",
            "message": "unsafe catch access",
            "required_fix": "error type guard를 추가하세요.",
        }],
    }
    return state


def frontend_integration_failure_state() -> dict:
    state = base_state()
    state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "SUCCESS_STATUS_MISMATCH",
            "target_agent": "frontend",
            "message": "status mismatch",
            "required_fix": "success status를 일치시키세요.",
        }],
    }
    return state


def test_validator_failure_uses_frontend_validator_fix_mode() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert "[Frontend Validator Fix Mode]" in prompt


def test_validator_fix_prompt_contains_previous_frontend_result() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert PREVIOUS_FRONTEND in prompt


def test_validator_fix_prompt_contains_validator_issues() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert "UNSAFE_CATCH_ERROR_ACCESS" in prompt
    assert "error type guard를 추가하세요." in prompt


def test_validator_fix_prompt_contains_backend_result() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert BACKEND_RESULT in prompt


def test_validator_fix_prompt_contains_user_request() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert USER_REQUEST in prompt


def test_validator_fix_prompt_contains_project_plan() -> None:
    _, prompt = run_frontend_agent(frontend_validator_failure_state())
    assert PROJECT_PLAN in prompt


def test_validator_fix_increments_frontend_fix_count() -> None:
    state = frontend_validator_failure_state()
    state["frontend_fix_count"] = 1
    state["integration_fix_count"] = 1
    result, _ = run_frontend_agent(state)
    assert result["frontend_fix_count"] == 2


def test_validator_fix_does_not_increment_integration_fix_count() -> None:
    state = frontend_validator_failure_state()
    state["integration_fix_count"] = 1
    result, _ = run_frontend_agent(state)
    assert result["integration_fix_count"] == 1


def test_validator_and_integration_fix_modes_are_separate() -> None:
    validator_state = frontend_validator_failure_state()
    validator_state["integration_validation"] = (
        frontend_integration_failure_state()["integration_validation"]
    )
    validator_result, validator_prompt = run_frontend_agent(validator_state)
    assert "[Frontend Validator Fix Mode]" in validator_prompt
    assert "[Frontend Integration Fix Mode]" not in validator_prompt
    assert validator_result["frontend_fix_count"] == 1
    assert validator_result["integration_fix_count"] == 0


def test_existing_frontend_integration_fix_mode_remains_active() -> None:
    integration_result, integration_prompt = run_frontend_agent(
        frontend_integration_failure_state()
    )
    assert "[Frontend Integration Fix Mode]" in integration_prompt
    assert "[Frontend Validator Fix Mode]" not in integration_prompt
    assert integration_result["frontend_fix_count"] == 0
    assert integration_result["integration_fix_count"] == 1


def test_initial_frontend_execution_keeps_existing_prompt_behavior() -> None:
    state = base_state()
    state["frontend_result"] = ""
    _, prompt = run_frontend_agent(state)
    assert prompt.startswith("다음 정보를 기반으로 Frontend 담당 범위의 결과를 작성하세요.")
    assert "[Frontend Validator Fix Mode]" not in prompt
    assert "[Frontend Integration Fix Mode]" not in prompt
    assert "[요청 유형별 실행 지시]" in prompt


def test_frontend_validator_pass_does_not_activate_fix_mode() -> None:
    state = base_state()
    _, prompt = run_frontend_agent(state)
    assert "[Frontend Validator Fix Mode]" not in prompt
    assert "[Frontend Integration Fix Mode]" not in prompt
    assert PREVIOUS_FRONTEND not in prompt


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)

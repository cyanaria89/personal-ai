import os
import unittest
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import (
    route_after_backend_validator,
    route_after_frontend_validator,
    route_after_integration_validator,
)


def integration_issue(target: str, rule: str = "SUCCESS_STATUS_MISMATCH") -> dict:
    return {
        "severity": "Major",
        "rule": rule,
        "target_agent": target,
        "message": "status mismatch",
        "required_fix": "success status를 일치시키세요.",
    }


def base_state(target: str = "frontend") -> dict:
    return {
        "user_request": "회원가입을 구현해줘",
        "required_agents": ["backend", "frontend"],
        "project_plan": "회원가입 Backend와 Frontend 구현",
        "db_result": "",
        "db_validation": {"status": "NOT_RUN", "issues": []},
        "db_fix_count": 0,
        "backend_result": "PREVIOUS_BACKEND_RESULT",
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": "PREVIOUS_FRONTEND_RESULT",
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {
            "status": "FAIL",
            "issues": [integration_issue(target)],
        },
        "integration_fix_count": 0,
        "review_result": "",
        "review_status": "",
        "review_count": 0,
        "final_result": "",
    }


def test_frontend_target_routes_to_frontend_fix() -> None:
    assert route_after_integration_validator(base_state("frontend")) == "frontend"


def test_backend_target_routes_to_backend_fix() -> None:
    assert route_after_integration_validator(base_state("backend")) == "backend"


def test_unknown_target_routes_to_review() -> None:
    assert route_after_integration_validator(base_state("UNKNOWN")) == "review"


def test_mixed_targets_route_to_review() -> None:
    state = base_state("frontend")
    state["integration_validation"]["issues"].append(
        integration_issue("backend")
    )
    assert route_after_integration_validator(state) == "review"


def test_max_integration_fix_count_routes_to_review() -> None:
    state = base_state("frontend")
    state["integration_fix_count"] = 2
    with patch.dict(os.environ, {"MAX_INTEGRATION_FIX_COUNT": "2"}):
        assert route_after_integration_validator(state) == "review"


def test_frontend_integration_fix_prompt_contains_previous_result() -> None:
    state = base_state("frontend")
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

    assert "[Frontend Integration Fix Mode]" in captured["prompt"]
    assert "PREVIOUS_FRONTEND_RESULT" in captured["prompt"]
    assert "PREVIOUS_BACKEND_RESULT" in captured["prompt"]
    assert result["integration_fix_count"] == 1
    assert result["frontend_fix_count"] == 0


def test_backend_integration_fix_prompt_contains_previous_result() -> None:
    state = base_state("backend")
    captured = {}
    original_invoke_agent = nodes.invoke_agent

    def fake_invoke(llm, system_prompt, user_prompt):
        del llm, system_prompt
        captured["prompt"] = user_prompt
        return "UPDATED_BACKEND_RESULT"

    nodes.invoke_agent = fake_invoke
    try:
        result = nodes.backend_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent

    assert "[Backend Integration Fix Mode]" in captured["prompt"]
    assert "PREVIOUS_BACKEND_RESULT" in captured["prompt"]
    assert "PREVIOUS_FRONTEND_RESULT" in captured["prompt"]
    assert result["integration_fix_count"] == 1
    assert result["backend_fix_count"] == 0


def test_frontend_validator_pass_returns_to_integration() -> None:
    state = base_state("frontend")
    state["frontend_validation"] = {"status": "PASS", "issues": []}
    assert route_after_frontend_validator(state) == "integration"


def test_backend_validator_pass_returns_to_integration_without_frontend() -> None:
    state = base_state("backend")
    state["backend_validation"] = {"status": "PASS", "issues": []}
    assert route_after_backend_validator(state) == "integration"


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest

import agents.nodes as nodes


PREVIOUS_FRONTEND = "UNIQUE_PREVIOUS_FRONTEND_FOR_LLM_SELECTION"


def base_state() -> dict:
    return {
        "user_request": "회원가입 화면을 구현해줘",
        "required_agents": ["backend", "frontend"],
        "project_plan": "회원가입 Frontend 구현 계획",
        "db_result": "",
        "db_validation": {"status": "NOT_RUN", "issues": []},
        "db_fix_count": 0,
        "backend_result": "BACKEND_CONTRACT_RESULT",
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


def validator_fix_state() -> dict:
    state = base_state()
    state["frontend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "UNSAFE_CATCH_ERROR_ACCESS",
            "message": "unsafe catch access",
            "required_fix": "타입 가드를 추가하세요.",
        }],
    }
    return state


def integration_fix_state() -> dict:
    state = base_state()
    state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "SUCCESS_STATUS_MISMATCH",
            "target_agent": "frontend",
            "message": "status mismatch",
            "required_fix": "성공 status를 일치시키세요.",
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
        return "UPDATED_FRONTEND_RESULT"

    nodes.invoke_agent = fake_invoke
    try:
        result = nodes.frontend_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent

    return result, captured["llm"], captured["prompt"]


def test_initial_frontend_uses_original_llm_and_prompt() -> None:
    state = base_state()
    state["frontend_result"] = ""
    result, selected_llm, prompt = run_frontend_agent(state)

    assert selected_llm is nodes.frontend_llm
    assert prompt.startswith("다음 정보를 기반으로 Frontend 담당 범위의 결과를 작성하세요.")
    assert "[Frontend Validator Fix Mode]" not in prompt
    assert "[Frontend Integration Fix Mode]" not in prompt
    assert result["frontend_fix_count"] == 0
    assert result["integration_fix_count"] == 0


def test_validator_fix_uses_fix_llm_and_preserves_state_policy() -> None:
    state = validator_fix_state()
    state["frontend_fix_count"] = 1
    state["integration_fix_count"] = 1
    result, selected_llm, prompt = run_frontend_agent(state)

    assert selected_llm is nodes.frontend_fix_llm
    assert "[Frontend Validator Fix Mode]" in prompt
    assert "[Frontend Integration Fix Mode]" not in prompt
    assert PREVIOUS_FRONTEND in prompt
    assert result["frontend_fix_count"] == 2
    assert result["integration_fix_count"] == 1


def test_integration_fix_uses_fix_llm_and_preserves_state_policy() -> None:
    state = integration_fix_state()
    state["frontend_fix_count"] = 1
    state["integration_fix_count"] = 1
    result, selected_llm, prompt = run_frontend_agent(state)

    assert selected_llm is nodes.frontend_fix_llm
    assert "[Frontend Integration Fix Mode]" in prompt
    assert "[Frontend Validator Fix Mode]" not in prompt
    assert PREVIOUS_FRONTEND in prompt
    assert result["frontend_fix_count"] == 1
    assert result["integration_fix_count"] == 2


def test_frontend_initial_llm_reserves_output_and_rag_space() -> None:
    assert nodes.frontend_llm.num_ctx == 12288
    assert nodes.frontend_llm.num_predict == 2048


def test_frontend_fix_llm_settings() -> None:
    assert nodes.frontend_fix_llm.num_ctx == 12288
    assert nodes.frontend_fix_llm.num_predict == 2048


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)

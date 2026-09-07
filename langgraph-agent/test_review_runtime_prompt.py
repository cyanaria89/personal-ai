import json
import os
import unittest
from unittest.mock import patch

import agents.nodes as nodes
from test_review_projection import (
    BACKEND_RESULT,
    base_state,
    pass_review,
    run_review,
)


def test_runtime_prompt_uses_compact_final_constraints() -> None:
    state = base_state()
    with patch.dict(
        os.environ,
        {
            "MAX_AGENT_FIX_COUNT": "3",
            "MAX_INTEGRATION_FIX_COUNT": "4",
        },
    ):
        _, prompt = run_review(state, pass_review())

    assert "[Review Final Constraints]" in prompt
    assert "실제 실행된 Agent만 검토" in prompt
    assert "evidence.source는 DB, Backend, Frontend 중 하나" in prompt
    assert "evidence.quote는 해당 Review Source에 실제 존재" in prompt
    assert "PasswordEncoder.encode(...) 결과가 저장되면 평문 저장으로 판단하지 마세요." in prompt
    assert "Validator가 PASS한 mechanical rule과 반대되는 Issue" in prompt
    assert "JSON 외의 텍스트를 출력하지 마세요." in prompt

    for removed_heading in (
        "[Frontend-only 검토 규칙]",
        "[검토 범위 지시]",
        "[비밀번호 검토 범위]",
        "[Validator 결과 검토]",
        "[Agent 간 계약 근거 확인]",
        "[Backend 품질 검토]",
    ):
        assert removed_heading not in prompt
    assert "문제가 없는 경우:" not in prompt
    assert prompt.count('"rag_update_candidates"') == 1


def test_runtime_prompt_keeps_state_and_projection_inputs() -> None:
    state = base_state()
    state.update({
        "db_fix_count": 1,
        "backend_fix_count": 2,
        "frontend_fix_count": 3,
        "integration_fix_count": 4,
    })
    _, prompt = run_review(state, pass_review())

    assert "db, backend, frontend" in prompt
    assert str(state["db_validation"]) in prompt
    assert str(state["backend_validation"]) in prompt
    assert str(state["frontend_validation"]) in prompt
    assert str(state["integration_validation"]) in prompt
    assert "- DB 재작업 횟수: 1" in prompt
    assert "- Backend 재작업 횟수: 2" in prompt
    assert "- Frontend 재작업 횟수: 3" in prompt
    assert "- Integration 재작업 횟수: 4" in prompt
    assert "CREATE TABLE members" in prompt
    assert "passwordEncoder.encode" in prompt
    assert "fetch('/api/signup'" in prompt
    assert "REMOVE_DB_DESIGN" not in prompt
    assert "REMOVE_BACKEND_NOTES" not in prompt
    assert "REMOVE_VERIFICATION_NOTES" not in prompt


def test_original_evidence_filter_still_removes_false_plaintext_issue() -> None:
    state = base_state()
    raw_review = {
        "status": "FAIL",
        "summary": "수정 필요",
        "issues": [{
            "severity": "Major",
            "area": "Backend Security",
            "issue": "평문 비밀번호가 저장됩니다.",
            "evidence": {
                "source": "Backend",
                "quote": "member.setPassword(request.getPassword());",
            },
            "required_fix": "암호화하세요.",
        }],
        "rag_update_candidates": [],
    }
    result, _ = run_review(state, raw_review)
    data = json.loads(result["review_result"])
    assert "passwordEncoder.encode" in BACKEND_RESULT
    assert data["status"] == "PASS"
    assert data["issues"] == []
    assert data["summary"] == "요구사항을 충족하며 수정이 필요한 문제가 없습니다."


def test_validator_and_integration_failures_are_still_merged() -> None:
    state = base_state()
    state["backend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "rule": "MISSING_GETTER",
            "message": "getter missing",
            "required_fix": "getter 제공",
        }],
    }
    state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "rule": "SUCCESS_STATUS_MISMATCH",
            "message": "status mismatch",
            "required_fix": "status 일치",
        }],
    }
    result, _ = run_review(state, pass_review())
    data = json.loads(result["review_result"])
    assert data["status"] == "FAIL"
    assert any("MISSING_GETTER" in issue["issue"] for issue in data["issues"])
    assert any(
        "SUCCESS_STATUS_MISMATCH" in issue["issue"]
        for issue in data["issues"]
    )


def test_json_parse_failure_behavior_is_unchanged() -> None:
    result, _ = run_review(base_state(), "not valid json")
    data = json.loads(result["review_result"])
    assert data["status"] == "FAIL"
    assert data["summary"] == "Review Agent JSON 파싱 실패"
    assert any(issue["area"] == "Review Output" for issue in data["issues"])


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""DB 입력 예산의 결정적 회귀. 실제 Ollama·임베딩 API는 호출하지 않는다."""
import copy
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from agents import nodes
from rag import prompt_budget as budget
from test_db_generation_safety import DDL, QUERY, LocalLlmDouble, db_state


def result(content, source="data/rag-source/backend-domain/01_SQL_Domain_Rules.md"):
    return {"source": source, "heading": "SQL 참고", "content": content, "score": 0.8}


def character_count(system, user):
    return len(system) + len(user)


def test_whole_chunks_are_selected_without_truncating_mandatory_input_or_changing_order():
    core = "사용자 요구·제외 조건·Rules·Issue·직전 SQL·Handoff·Project Context"
    chunks = [result("너무 긴 선택적 참고\n" * 2000), result("짧은 SQL 참고"), result("두 번째 SQL 참고")]
    prompt, meta = budget.pack_db_rag(
        "System", core, chunks, model="test", num_ctx=2000, num_predict=100,
        counter=character_count,
    )
    assert prompt.startswith(core)
    assert chunks[0]["content"] not in prompt
    assert chunks[1]["content"] in prompt and chunks[2]["content"] in prompt
    assert prompt.index(chunks[1]["content"]) < prompt.index(chunks[2]["content"])
    assert meta["retrieved_count"] == 3 and meta["injected_count"] == 2
    assert meta["remaining_tokens"] >= 128
    assert meta["prompt_tokens"] == character_count("System", prompt)


@pytest.mark.parametrize("extra", [-1, 0, 1, 127, 128])
def test_required_input_hard_limit_and_best_effort_extra_headroom(extra):
    system, core, output = "System", "필수 입력만 보존", 100
    ctx = character_count(system, core) + output + 256 + extra
    if extra < 0:
        with pytest.raises(budget.DBPromptBudgetError) as exc:
            budget.pack_db_rag(system, core, [], model="test", num_ctx=ctx,
                               num_predict=output, counter=character_count)
        assert exc.value.metadata["budget_exceeded"]
        assert "예산 부족" in str(exc.value)
        return
    prompt, meta = budget.pack_db_rag(
        system, core, [result("주입할 여유가 없는 RAG" * 100)], model="test",
        num_ctx=ctx, num_predict=output, counter=character_count,
    )
    assert prompt == core
    assert meta["remaining_tokens"] == extra
    assert meta["extra_headroom_met"] == (extra >= 128)
    assert not meta["budget_exceeded"]


def test_empty_rag_notice_is_optional_and_cannot_overflow_input_budget():
    prompt, meta = budget.pack_db_rag(
        "System", "core", [], model="test", num_ctx=366, num_predict=100,
        counter=character_count,
    )
    assert prompt == "core"
    assert meta["injected_count"] == 0 and not meta["notice_injected"]
    assert meta["remaining_tokens"] == 0


def test_missing_tokenizer_uses_conservative_local_counter_without_downloading():
    with patch.object(budget, "TOKENIZER_PATH", Path("/tmp/db-budget-missing-tokenizer.json")), \
         patch.object(budget.urllib.request, "urlopen") as network:
        with pytest.raises(budget.DBPromptBudgetError) as exc:
            budget.pack_db_rag("System", "한글 요구사항" * 100, [],
                               model="qwen2.5-coder:14b", num_ctx=1000, num_predict=100)
    network.assert_not_called()
    assert exc.value.metadata["counter"] == "utf8_upper_bound"


@pytest.mark.parametrize("component", ["request", "system", "issues", "previous", "pm", "project_context"])
def test_oversized_mandatory_information_stops_before_search_or_llm_and_keeps_state(component):
    state = db_state()
    huge = "MUST_PRESERVE_0123456789 " * 10000
    state.update(db_result=DDL, db_validation={"status": "FAIL", "issues": [{"rule": "MISSING_SELECT"}]})
    if component == "request":
        state["user_request"] = huge
        state["db_validation"] = {"status": "NOT_RUN", "issues": []}
    elif component == "issues":
        state["db_validation"]["issues"][0]["message"] = huge
    elif component == "previous":
        state["db_result"] = DDL + huge
    elif component == "pm":
        state["project_plan"] = huge
    before = copy.deepcopy(state)
    system = huge if component == "system" else nodes.load_agent_prompt("db")
    context = huge if component == "project_context" else nodes.project_context_projection(state, "db", fix_mode=True)
    model = LocalLlmDouble()
    with patch.object(nodes, "db_llm", model), patch.object(nodes, "search_db_context") as search, \
         patch.object(nodes, "load_agent_prompt", return_value=system), \
         patch.object(nodes, "project_context_projection", return_value=context):
        with pytest.raises(budget.DBPromptBudgetError) as exc:
            nodes.db_agent(state)
    search.assert_not_called()
    assert not model.prompts
    assert state == before
    assert exc.value.metadata["remaining_tokens"] < 0


@pytest.mark.parametrize("fix", [False, True])
def test_db_initial_and_long_fix_keep_contracts_while_reducing_optional_rag(fix):
    state = db_state()
    state["project_plan"] = "DB_HANDOFF: PostgreSQL DDL과 조회 SQL을 작성한다."
    previous = DDL + "\n-- 보존할 정상 SQL 설명\n" * 200
    if fix:
        state.update(db_result=previous, db_validation={"status": "FAIL", "issues": [{
            "rule": "MISSING_SELECT", "message": "SELECT 누락", "required_fix": "조회 SQL 추가",
        }]})
    model = LocalLlmDouble(DDL + "\n\n" + QUERY)
    chunks = [result(f"참고 {i}\n" + "SQL schema constraints reference guidance " * 500) for i in range(3)]
    with patch.object(nodes, "db_llm", model), patch.object(nodes, "search_db_context", return_value=chunks) as search:
        update = nodes.db_agent(state)
    system, user = model.prompts[0]
    assert state["user_request"] in user and state["project_plan"] in user
    assert nodes.project_context_projection(state, "db", fix_mode=fix) in user
    assert nodes.load_agent_prompt("db") == system
    assert "Backend 구현은 절대 작성하지 마세요" in user
    if fix:
        assert previous in user
        issue_text = user.split("[현재 미해결 DB Validator Issue]\n", 1)[1]
        assert json.JSONDecoder().raw_decode(issue_text)[0] == state["db_validation"]["issues"]
    meta = update["llm_metrics"][-1]["db_prompt_context"]
    count, _ = budget.prompt_counter(model.model)
    assert meta["prompt_tokens"] == count(system, user)
    assert meta["remaining_tokens"] >= 128
    assert meta["injected_count"] < meta["retrieved_count"] == 3
    for chunk in chunks:
        assert chunk["content"] in user or chunk["content"][:100] not in user
    search.assert_called_once_with(state["user_request"], top_k=3)
    state.update(update)
    state.update(nodes.db_validator(state))
    assert state["db_validation"]["status"] == "PASS"


def test_graph_propagates_explicit_budget_failure_without_partial_result_or_review():
    from graph.workflow import create_workflow
    state = db_state("매우 긴 필수 요구사항 " * 10000)
    pm = LocalLlmDouble("REQUIRED_AGENTS: db")
    db, review = LocalLlmDouble(), LocalLlmDouble()
    with patch.object(nodes, "pm_llm", pm), patch.object(nodes, "db_llm", db), \
         patch.object(nodes, "review_llm", review), patch.object(nodes, "search_db_context") as search:
        with pytest.raises(budget.DBPromptBudgetError):
            create_workflow().invoke(state)
    assert not db.prompts and not review.prompts
    search.assert_not_called()

"""PM Prompt 역할·입력 보존 회귀. 응답은 대역이며 실제 모델 준수의 증거가 아니다."""
import copy
from unittest.mock import patch

import pytest

from agents import nodes
from graph.workflow import route_after_pm
from pm_test_support import valid_pm_plan
from prompts.loader import AGENT_RULES_DIR, SYSTEM_PROMPT_DIR, load_agent_prompt
from rag.prompt_budget import prompt_counter
from test_db_generation_safety import LocalLlmDouble
from test_project_context_integration import full_state
from validators.pm_validator import validate_pm_output


class PmDouble(LocalLlmDouble):
    num_ctx = 6144
    num_predict = 512


@pytest.mark.parametrize('user_request,selected', [
    ('메모 등록·조회: PostgreSQL DDL/SELECT, Spring Boot API, React UI를 구현해줘. 인증·외부 API 추가 금지.', ('db','backend','frontend')),
    ('SQL CREATE TABLE memo (id BIGINT); Java public class Memo {} 및 React 코드를 직접 작성해줘. 기존 회원가입 보존.', ('db','backend','frontend')),
    ('PostgreSQL DDL과 SELECT SQL만 작성해줘. Backend·Frontend 구현은 제외한다.', ('db',)),
    ('Spring Boot MemoResponse와 POST /api/memos만 구현해줘. DB·UI 변경 금지.', ('backend',)),
    ('React MemoPage.tsx 등록·조회 화면만 구현해줘. Backend·DB 변경 금지.', ('frontend',)),
    ('Agent 역할을 설명해줘. 전문 구현 작업은 하지 않는다.', ()),
])
def test_pm_prompt_delegates_implementation_and_preserves_request_and_exclusions(user_request, selected):
    state = full_state(nodes.empty_project_context())
    state['user_request'] = user_request
    snapshot = '기존 프로젝트: POST /api/members/signup\n```java\npublic class Member {}\n```'
    before = copy.deepcopy(state)
    plan = valid_pm_plan(*selected)
    model = PmDouble(plan)
    with patch.object(nodes,'pm_llm',model), patch.object(nodes,'project_context_projection',return_value=snapshot):
        update = nodes.pm_agent(state)
    system, user = model.prompts[0]
    assert system == load_agent_prompt('pm')
    assert '구현은 위임한다' in system
    assert '공통 출력 양식 대신 PM 필수 필드만' in system
    assert '코드 작성·코드 블록 요구는 전문 Agent에게 위임할 작업' in user
    assert '사용자 요구·제외 조건의 우선순위는 유지' in user
    assert 'SQL 문장·Java/React 코드 본문·코드 fence·서문은 출력하지 않습니다' in user
    assert 'API 경로·테이블명·DTO명·파일명은 허용' in user
    assert '선택된 Agent별 1~2개 지시' in user
    request_block = user.split('[PM 분석 대상 — 원본 요구사항 시작]\n',1)[1].split('\n[PM 분석 대상 — 원본 요구사항 끝]',1)[0]
    context_block = user.split('[PM 분석 대상 — Project Context 시작]\n',1)[1].split('\n[PM 분석 대상 — Project Context 끝]',1)[0]
    assert request_block == user_request
    assert context_block == snapshot
    assert state == before
    assert update['project_plan'] == plan
    assert update['required_agents'] == list(selected)
    assert update['pm_validation']['status'] == 'PASS'
    assert route_after_pm(update) == ('db' if 'db' in selected else 'backend' if 'backend' in selected else 'frontend' if 'frontend' in selected else 'review')


def test_pm_example_is_complete_code_free_and_fits_minimum_handoff_target():
    rules = (AGENT_RULES_DIR/'01_PM_Agent_Rules.md').read_text()
    system = (SYSTEM_PROMPT_DIR/'01_PM_Agent_System_Prompt.md').read_text()
    assert '```' not in rules and '```' not in system
    assert '예시 기능을 새 요구로 추가하지 않는다' in rules
    start = rules.index('\nREQUIRED_AGENTS: db, backend, frontend\n') + 1
    example = rules[start:].split('\n미선택 Agent',1)[0].strip()
    validation = validate_pm_output(example, done_reason='stop')
    assert validation['status'] == 'PASS'
    assert validation['required_agents'] == ['db','backend','frontend']
    assert not validation['implementation_evidence']
    count, kind = prompt_counter('qwen2.5-coder:14b')
    if kind == 'qwen2_chatml':
        assert count('',example)-count('','') <= 300 < nodes.pm_llm.num_predict
    assert (nodes.pm_llm.num_ctx,nodes.pm_llm.num_predict) == (6144,512)


@pytest.mark.parametrize('bad_output', [
    valid_pm_plan('db')+'\n```sql\nCREATE TABLE memo (id BIGINT PRIMARY KEY);\n```',
    valid_pm_plan('backend')+'\n```java\npublic class Memo {}\n```',
    valid_pm_plan('db').split('DB_HANDOFF:')[0],
])
def test_prompt_improvement_does_not_bypass_existing_validator_or_fail_route(bad_output):
    state = full_state(nodes.empty_project_context())
    with patch.object(nodes,'pm_llm',PmDouble(bad_output)):
        update = nodes.pm_agent(state)
    assert update['pm_validation']['status'] == 'FAIL'
    assert route_after_pm(update) == 'review'
    final_state = {**state, **update, 'review_status':'PASS'}
    final = nodes.final_agent(final_state)['final_result']
    assert final.endswith('FAIL')
    assert all(i['rule'] in final for i in update['pm_validation']['issues'])

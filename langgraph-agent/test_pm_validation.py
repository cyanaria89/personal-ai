"""PM 응답 검증 및 차단의 결정적 회귀. 실제 LLM·RAG는 호출하지 않는다."""
import copy
import json
from unittest.mock import patch

import pytest

from agents import nodes
from graph.workflow import create_workflow, route_after_pm
from pm_test_support import valid_pm_plan
from test_db_generation_safety import LocalLlmDouble
from test_project_context_integration import full_state
from validators.pm_validator import validate_pm_output


def rules(validation):
    return {issue['rule'] for issue in validation['issues']}


@pytest.mark.parametrize('agents,route', [
    (('db',), 'db'), (('backend',), 'backend'), (('frontend',), 'frontend'),
    (('db', 'backend'), 'db'), (('backend', 'frontend'), 'backend'),
    (('db', 'frontend'), 'db'), (('db', 'backend', 'frontend'), 'db'), ((), 'review'),
])
def test_valid_selection_and_none_keep_existing_routes(agents, route):
    plan = valid_pm_plan(*agents)
    validation = validate_pm_output(plan, done_reason='stop')
    assert validation['status'] == 'PASS'
    assert validation['required_agents'] == list(agents)
    assert validation['selection_status'] == ('SELECTED' if agents else 'NONE')
    assert nodes.parse_required_agents(plan) == list(agents)
    assert route_after_pm({'required_agents':list(agents), 'pm_validation':validation}) == route


@pytest.mark.parametrize('declaration', [
    'REQUIRED_AGENTS db', 'REQUIRED_AGENTS:', 'REQUIRED_AGENTS: qa',
    'REQUIRED_AGENTS: db, qa', 'REQUIRED_AGENTS: none, db', 'REQUIRED_AGENTS: db, db',
    'REQUIRED_AGENTS: db,', 'REQUIRED_AGENTS: db backend',
    'required_agents: db', '서문\nREQUIRED_AGENTS: db',
    'REQUIRED_AGENTS: db\nREQUIRED_AGENTS: backend',
])
def test_invalid_selection_is_not_normal_none(declaration):
    plan = valid_pm_plan('db').replace('REQUIRED_AGENTS: db', declaration, 1)
    validation = validate_pm_output(plan)
    assert validation['status'] == 'FAIL'
    assert validation['selection_status'] != 'NONE'
    assert route_after_pm({'required_agents':validation['required_agents'], 'pm_validation':validation}) == 'review'


@pytest.mark.parametrize('section', ['REQUEST_SUMMARY', 'EXECUTION_ORDER', 'DB_HANDOFF'])
def test_missing_required_section_blocks_execution(section):
    plan = valid_pm_plan('db')
    lines = plan.splitlines()
    index = next(i for i,line in enumerate(lines) if line.startswith(section+':'))
    del lines[index:index+2]
    validation = validate_pm_output('\n'.join(lines))
    assert validation['status'] == 'FAIL'
    assert any('MISSING' in rule for rule in rules(validation))


@pytest.mark.parametrize('body', ['', '- ', '- ...', '- 없음', '- N/A', '<필수 내용>', '<!-- TODO -->'])
def test_empty_or_placeholder_handoff_is_failure(body):
    plan = valid_pm_plan('db').split('DB_HANDOFF:')[0]+'DB_HANDOFF:\n'+body
    assert 'PM_MISSING_HANDOFF' in rules(validate_pm_output(plan))


@pytest.mark.parametrize('body', ['', '- 없음', '- Frontend 페이지를 작성한다.'])
def test_unselected_handoff_is_rejected_even_when_empty(body):
    validation = validate_pm_output(valid_pm_plan('db')+'\nFRONTEND_HANDOFF:\n'+body)
    assert 'PM_UNSELECTED_HANDOFF' in rules(validation)


@pytest.mark.parametrize('order', ['frontend -> db -> review', 'db', 'db -> backend -> review'])
def test_execution_order_must_match_selected_graph_order(order):
    plan = valid_pm_plan('db').replace('db -> review',order)
    assert 'PM_INVALID_EXECUTION_ORDER' in rules(validate_pm_output(plan))


@pytest.mark.parametrize('implementation', [
    '```sql\nCREATE TABLE memo (id BIGINT PRIMARY KEY);\n```',
    'SELECT id, title, content FROM memo ORDER BY id DESC;',
    'INSERT INTO memo (title) VALUES (\'memo\');',
    'UPDATE memo SET title = \'changed\';',
    '```java\npublic class Memo { private Long id; }\n```',
    'public record MemoResponse(Long id, String title) {}',
    'import jakarta.persistence.Entity;',
    'export function MemoPage() { return <form />; }',
    'const MemoPage = () => { return <form />; };',
    '<form><input /></form>',
])
def test_actual_specialist_implementation_is_rejected(implementation):
    validation = validate_pm_output(valid_pm_plan('db')+'\n'+implementation)
    assert 'PM_IMPLEMENTATION_CODE' in rules(validation)
    assert validation['implementation_evidence']


@pytest.mark.parametrize('instruction', [
    '- PostgreSQL CREATE TABLE DDL과 SELECT SQL을 작성하세요.',
    '- SELECT id, title, content FROM memo ORDER BY id DESC를 작성하세요.',
    '- 조회 계약은 `SELECT id, title, content FROM memo ORDER BY id DESC`입니다.',
    '- Spring Boot 3/JPA Entity·Repository·DTO 구현을 Backend에 위임한다.',
    '- POST /api/memos 및 GET /api/memos 계약을 보존한다.',
    '- React/TypeScript MemoPage에서 등록·조회 UI와 fetch 연동을 구현한다.',
    '- 함수 이름은 handleSubmit, 타입은 Promise<Memo[]>로 협의한다.',
])
def test_technical_instructions_are_not_implementation(instruction):
    validation = validate_pm_output(valid_pm_plan('db')+'\n'+instruction)
    assert validation['status'] == 'PASS'
    assert not validation['implementation_evidence']


class ReasonLlm(LocalLlmDouble):
    def __init__(self, output, reason):
        super().__init__(output)
        self.reason = reason

    def invoke(self, messages):
        response = super().invoke(messages)
        response.response_metadata['done_reason'] = self.reason
        return response


def test_only_pm_response_is_scanned_and_prior_length_metadata_is_not_reused():
    state = full_state(nodes.empty_project_context())
    state['user_request'] = '다음 기존 코드를 참고해줘: CREATE TABLE memo (id BIGINT); public class Memo {}'
    state['llm_metrics'] = [{'agent':'pm','done_reason':'length'}]
    before = copy.deepcopy(state)
    plan = valid_pm_plan('backend')
    with patch.object(nodes, 'pm_llm', ReasonLlm(plan,'stop')), \
         patch.object(nodes, 'project_context_projection', return_value='export function Page() { return <form />; }'):
        update = nodes.pm_agent(state)
    assert update['pm_validation']['status'] == 'PASS'
    assert update['project_plan'] == plan
    assert state == before


@pytest.mark.parametrize('reason', ['length', 'max_tokens', 'max_output_tokens'])
def test_truncated_complete_looking_plan_blocks_specialist_graph_execution(reason):
    state = full_state(nodes.empty_project_context())
    state['project_root'] = ''
    plan = valid_pm_plan('db','backend','frontend')
    pm, review = ReasonLlm(plan,reason), LocalLlmDouble(json.dumps({'status':'PASS','issues':[]}))
    blocked = LocalLlmDouble()
    with patch.object(nodes,'pm_llm',pm), patch.object(nodes,'review_llm',review), \
         patch.object(nodes,'db_llm',blocked), patch.object(nodes,'backend_llm',blocked), \
         patch.object(nodes,'frontend_llm',blocked), patch.object(nodes,'search_db_context') as rag:
        result = create_workflow().invoke(state)
    assert len(pm.prompts) == len(review.prompts) == 1
    assert not blocked.prompts
    rag.assert_not_called()
    assert result['required_agents'] == ['db','backend','frontend']
    assert result['user_request'] == state['user_request']
    assert result['project_plan'] == plan
    assert result['pm_validation']['status'] == 'FAIL'
    assert 'PM_TRUNCATED_OUTPUT' in rules(result['pm_validation'])
    assert result['review_status'] == 'FAIL'
    result['review_status'] = 'PASS'
    final = nodes.final_agent(result)['final_result']
    assert final.endswith('FAIL') and 'PM_TRUNCATED_OUTPUT' in final


def test_missing_handoff_fail_preserves_reason_even_when_review_llm_says_pass():
    state = full_state(nodes.empty_project_context())
    state['project_root'] = ''
    plan = valid_pm_plan('db').split('DB_HANDOFF:')[0]
    with patch.object(nodes,'pm_llm',ReasonLlm(plan,'stop')), \
         patch.object(nodes,'review_llm',LocalLlmDouble(json.dumps({'status':'PASS','issues':[]}))), \
         patch.object(nodes,'db_llm',LocalLlmDouble()):
        result = create_workflow().invoke(state)
    assert result['pm_validation']['status'] == 'FAIL'
    assert 'PM_MISSING_HANDOFF' in result['review_result']
    assert result['final_result'].endswith('FAIL')
    result['review_status'] = 'PASS'
    assert nodes.final_agent(result)['final_result'].endswith('FAIL')


def test_normal_none_can_finish_without_specialist_execution():
    state = full_state(nodes.empty_project_context())
    state['project_root'] = ''
    with patch.object(nodes,'pm_llm',ReasonLlm(valid_pm_plan(),'stop')), \
         patch.object(nodes,'review_llm',LocalLlmDouble(json.dumps({'status':'PASS','issues':[]}))), \
         patch.object(nodes,'db_llm',LocalLlmDouble()):
        result = create_workflow().invoke(state)
    assert result['required_agents'] == []
    assert result['pm_validation']['selection_status'] == 'NONE'
    assert result['review_status'] == 'PASS'
    assert result['final_result'].endswith('PASS')


def test_missing_validation_cannot_enter_specialist_route():
    assert route_after_pm({'required_agents':['db']}) == 'review'


def test_unknown_selection_keeps_original_declaration_for_diagnosis():
    validation = validate_pm_output(valid_pm_plan('db').replace('REQUIRED_AGENTS: db','REQUIRED_AGENTS: db, qa'))
    assert validation['declared_agents'] == ['db','qa']
    assert validation['required_agents'] == ['db']
    assert validation['status'] == 'FAIL'


def test_closed_text_wrapper_is_presentation_only_but_unclosed_wrapper_fails():
    plan = valid_pm_plan('db')
    closed = validate_pm_output('```text\n'+plan+'\n```')
    assert closed['status'] == 'PASS' and closed['outer_text_fence_normalized']
    unclosed = validate_pm_output('```text\n'+plan)
    assert unclosed['status'] == 'FAIL'
    assert 'PM_REQUIRED_AGENTS_FORMAT' in rules(unclosed)


def test_case_variant_unselected_handoff_is_not_silently_accepted():
    validation = validate_pm_output(valid_pm_plan('db')+'\nfrontend_handoff:\n- 불필요한 작업')
    assert 'PM_UNSELECTED_HANDOFF' in rules(validation)


def test_implementation_in_fence_cannot_hide_behind_instruction_like_comment():
    validation = validate_pm_output(valid_pm_plan('db')+'\n```sql\nCREATE TABLE memo (id BIGINT); -- 설계\n```')
    assert 'PM_IMPLEMENTATION_CODE' in rules(validation)


def test_truncated_none_is_pm_failure_even_without_other_validator_blockers():
    state = full_state(nodes.empty_project_context())
    state['project_root'] = ''
    with patch.object(nodes,'pm_llm',ReasonLlm(valid_pm_plan(),'length')), \
         patch.object(nodes,'review_llm',LocalLlmDouble(json.dumps({'status':'PASS','issues':[]}))):
        result = create_workflow().invoke(state)
    assert result['required_agents'] == []
    assert result['pm_validation']['status'] == 'FAIL'
    assert result['review_status'] == 'FAIL'
    assert 'PM_TRUNCATED_OUTPUT' in result['review_result']
    assert not nodes.integration_verification_blocker(result)
    assert not nodes.completeness_blockers(result)
    result['review_status'] = 'PASS'
    final = nodes.final_agent(result)['final_result']
    assert final.endswith('FAIL') and 'PM_TRUNCATED_OUTPUT' in final

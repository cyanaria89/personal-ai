from pm_test_support import valid_pm_plan
"""Backend Fix 계약/보존/진행 검사. 계약 source는 테스트 전용이며 실제 프로젝트 계약이 아니다."""
import copy
import json
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import create_workflow, route_after_backend_validator
from test_completeness_validator import backend
from test_project_context_integration import full_state
from validators.backend_fix_validator import prepare_backend_fix, assess_backend_fix
from validators.completeness_validator import attach_completeness


CONTRACT = {'path': 'src/TokenIssuer.java', 'content': '''public interface TokenIssuer {
    String createAccessToken(Object member);
    String createRefreshToken(Object member);
}''', 'truncated': False}
BAD = '''private final TokenIssuer issuer;
public Object signup() { return memberRepository.save(member); }
public Object login() {
    String accessToken = "fake-access";
    String refreshToken = "fake-refresh";
    return new LoginResponse(accessToken, refreshToken);
}'''
GOOD = BAD.replace('"fake-access"', 'issuer.createAccessToken(member)').replace('"fake-refresh"', 'issuer.createRefreshToken(member)')


def artifact(code=BAD):
    return '# Backend Agent Output\n## Implementation\n### Service\n#### AuthService.java\n```java\npublic class AuthService {\n' + code + '\n}\n```\n'


def state(contract=True):
    s = full_state(nodes.empty_project_context())
    s.update(required_agents=['backend'], user_request='로그인 기능 추가해줘', backend_result=artifact())
    if contract:
        s['project_context']['selected_files'] = [copy.deepcopy(CONTRACT)]
    s.update(nodes.backend_validator(s))
    return s


def evaluate(s, output):
    pending = prepare_backend_fix(s, s['backend_validation'])
    s['backend_validation']['fix'] = {**pending, 'status': 'RUNNING'}
    validation = attach_completeness({'status': 'PASS', 'issues': []}, output, s, 'backend')
    return assess_backend_fix(s, output, validation)


def test_missing_contract_blocks_without_llm_or_rag_and_keeps_fail():
    s = state(False)
    before = s['backend_result']
    with patch.object(nodes, 'invoke_agent_with_metrics') as llm, patch.object(nodes, 'search_backend_context') as rag:
        s.update(nodes.backend_agent(s))
    llm.assert_not_called(); rag.assert_not_called()
    assert s['backend_validation']['status'] == 'FAIL'
    assert s['backend_validation']['completeness']['status'] == 'FAIL'
    assert s['backend_validation']['fix']['status'] == 'BLOCKED'
    assert s['backend_result'] == before
    assert route_after_backend_validator(s) == 'review'
    assert s['backend_fix_count'] == 0


def test_complete_snapshot_contract_allows_fix_and_is_in_prompt():
    s = state()
    with patch.object(nodes, 'invoke_agent_with_metrics', return_value=artifact(GOOD)) as llm, patch.object(nodes, 'search_backend_context', return_value=[]):
        s.update(nodes.backend_agent(s))
    prompt = llm.call_args.args[2]
    assert 'src/TokenIssuer.java' in prompt and 'String createAccessToken' in prompt
    assert 'RAG 예제는 실제 프로젝트의 확정 계약' in prompt
    assert prompt.count(artifact()) == 1
    s.update(nodes.backend_validator(s))
    assert s['backend_validation']['status'] == 'PASS', s['backend_validation']
    assert s['backend_validation']['fix']['status'] == 'SUCCEEDED'
    assert s['backend_validation']['fix']['resolved_issues']


def test_incomplete_or_test_snapshot_is_not_contract():
    for overrides in ({'truncated': True}, {'content': ''}, {'path': 'src/test/TokenIssuer.java'}):
        s = state(False)
        s['backend_validation'].pop('fix', None)
        s['project_context']['selected_files'] = [{**CONTRACT, **overrides}]
        assert prepare_backend_fix(s, s['backend_validation'])['status'] == 'BLOCKED'


def test_constant_return_issuer_is_not_confirmed_implementation():
    s = state(False); s['backend_validation'].pop('fix', None)
    s['project_context']['selected_files'] = [{**CONTRACT, 'content': 'public class TokenIssuer { public String createAccessToken(Object member) { return "fake"; } }'}]
    assert prepare_backend_fix(s, s['backend_validation'])['status'] == 'BLOCKED'


def test_issuance_implementation_source_is_available_beyond_projection():
    s = state(False); s['backend_validation'].pop('fix', None)
    s['project_context']['selected_files'] = [{**CONTRACT, 'content': 'public class TokenIssuer { public String createAccessToken(Object member) { return configuredSigner.sign(member); } }'}]
    fix = prepare_backend_fix(s, s['backend_validation'])
    assert fix['status'] == 'READY'
    assert fix['contract']['confirmed'][0]['kind'] == 'implementation'


def test_changed_literal_is_no_progress():
    r = evaluate(state(), artifact(BAD.replace('fake-', 'renamed-')))
    assert r['status'] == 'FAIL' and r['fix']['status'] == 'NO_PROGRESS'
    assert len(r['completeness']['issues']) == 2


def test_undefined_provider_or_renamed_variables_do_not_bypass():
    for code in (GOOD.replace('issuer.', 'undefinedProvider.'), GOOD.replace('TokenIssuer', 'MissingIssuer'),
                 GOOD.replace('createAccessToken(member)', 'createAccessToken()'),
                 GOOD.replace('createRefreshToken(member)', 'createAccessToken(member)'),
                 GOOD.replace('private final TokenIssuer issuer;', 'public Object helper(TokenIssuer issuer) { return issuer; }'),
                 BAD.replace('accessToken', 'a').replace('refreshToken', 'b'),
                 GOOD.replace('accessToken', 'a').replace('refreshToken', 'b')):
        r = evaluate(state(), artifact(code))
        assert r['status'] == 'FAIL' and r['completeness']['status'] == 'FAIL'
        assert r['fix']['status'] == 'NO_PROGRESS'


def test_token_fields_removed_or_reassigned_do_not_bypass():
    for code in (GOOD.replace('return new LoginResponse(accessToken, refreshToken);', 'return new LoginResponse();'),
                 GOOD.replace('return new LoginResponse', 'accessToken = "other"; return new LoginResponse')):
        r = evaluate(state(), artifact(code))
        assert r['status'] == 'FAIL' and r['fix']['status'] == 'NO_PROGRESS'


def test_signup_deletion_is_regression_even_when_tokens_are_repaired():
    output = artifact(GOOD.replace('public Object signup() { return memberRepository.save(member); }', ''))
    r = evaluate(state(), output)
    assert r['status'] == 'FAIL' and r['fix']['status'] == 'REGRESSION'
    assert any(i['function'] == 'signup' for i in r['fix']['regressions'])


def test_unrelated_body_change_is_regression():
    r = evaluate(state(), artifact(GOOD.replace('memberRepository.save(member)', 'null')))
    assert r['fix']['preservation']['status'] == 'FAIL'


def test_unrelated_string_whitespace_change_is_not_ignored():
    s = state()
    s['backend_result'] = artifact(BAD.replace('memberRepository.save(member)', '"a  b"'))
    r = evaluate(s, artifact(GOOD.replace('memberRepository.save(member)', '"a b"')))
    assert r['fix']['preservation']['status'] == 'FAIL'


def test_explicit_signup_deletion_is_allowed_but_prohibition_is_not():
    output = artifact(GOOD.replace('public Object signup() { return memberRepository.save(member); }', ''))
    s = state(); s['user_request'] += '. signup()을 삭제해줘'
    assert evaluate(s, output)['fix']['status'] == 'SUCCEEDED'
    for request in ('로그인 기능 추가. signup()을 삭제하지 마', '로그인 기능 추가. signup 삭제 사례를 방지',
                    '로그인 기능 추가. signup 삭제된 기능 복구', '로그인 기능 추가. do not remove signup'):
        s['user_request'] = request
        assert evaluate(copy.deepcopy(s), output)['fix']['regressions']


def controller(method='Post', path='/signup'):
    return '\n## Implementation\n### Controller\n#### MemberController.java\n```java\n@RestController\n@RequestMapping("/api/members")\npublic class MemberController {\n@' + method + 'Mapping("' + path + '")\npublic Object signup() { return service.signup(); }\n}\n```\n'


def test_signup_endpoint_and_http_method_preserved():
    s = state(); s['backend_result'] += controller()
    s['backend_validation'].pop('fix', None)
    for output in (artifact(GOOD), artifact(GOOD) + controller('Get'), artifact(GOOD) + controller(path='/register')):
        r = evaluate(copy.deepcopy(s), output)
        assert r['status'] == 'FAIL' and r['fix']['regressions']
    r = evaluate(s, artifact(GOOD) + controller())
    assert r['fix']['preservation']['status'] == 'PASS'


def test_dto_change_is_not_unconditionally_accepted():
    dto = '\n## Implementation\n### DTO\n#### LoginResponse.java\n```java\npublic record LoginResponse(String accessToken, String refreshToken) {}\n```\n'
    s = state(); s['backend_result'] += dto
    r = evaluate(s, artifact(GOOD) + dto.replace(', String refreshToken', ''))
    assert r['status'] == 'FAIL'
    assert r['fix']['preservation']['status'] == 'FAIL'
    assert any('DTO 계약' in i['message'] for i in r['fix']['regressions'])


def test_same_defect_and_new_issue_reported_independently():
    code = BAD.replace('return memberRepository.save(member);', 'throw new UnsupportedOperationException("not implemented");')
    s = state(); s['user_request'] += '. 회원가입 기능도 구현'
    r = evaluate(s, artifact(code))
    assert r['fix']['status'] == 'NO_PROGRESS'
    assert r['fix']['new_issues']  # 다른 기능도 요청 범위에 포함시켜 검사
    assert r['fix']['regressions']


def test_fix_rechecked_after_auto_fix_and_counts_two():
    s = state(); bad = artifact(BAD)
    with patch.object(nodes, 'invoke_agent_with_metrics', return_value=bad), patch.object(nodes, 'search_backend_context', return_value=[]):
        for _ in range(2):
            s.update(nodes.backend_agent(s)); s.update(nodes.backend_validator(s))
            assert s['backend_validation']['fix']['status'] == 'NO_PROGRESS'
    assert s['backend_fix_count'] == 2 and route_after_backend_validator(s) == 'review'
    assert len(s['backend_validation']['fix']['baseline']['issues']) == 2


def test_required_safety_fail_blocks_review_and_even_stale_review_pass():
    s = state(False)
    with patch.object(nodes, 'invoke_agent', return_value=json.dumps({'status': 'PASS', 'issues': []})):
        s.update(nodes.review_agent(s))
    assert s['review_status'] == 'FAIL'
    s['review_status'] = 'PASS'
    assert nodes.final_agent(s)['final_result'].endswith('FAIL')
    s = state(); output = artifact(GOOD).replace('signup()', 'renamedSignup()')
    s['backend_validation'] = evaluate(s, output); s['backend_result'] = output
    s['review_status'] = 'PASS'
    assert nodes.final_agent(s)['final_result'].endswith('FAIL')


def test_model_blocked_response_keeps_original_and_stops_retry():
    s = state(); before = s['backend_result']
    with patch.object(nodes, 'invoke_agent_with_metrics', return_value='BACKEND_FIX_STATUS: BLOCKED\n반환 계약의 추가 확인 필요'), patch.object(nodes, 'search_backend_context', return_value=[]):
        s.update(nodes.backend_agent(s))
    s.update(nodes.backend_validator(s))
    assert s['backend_result'] == before and s['backend_fix_count'] == 1
    assert s['backend_validation']['fix']['status'] == 'BLOCKED'
    assert route_after_backend_validator(s) == 'review'


def test_blocked_graph_does_not_repeat_model_fix():
    s = full_state(nodes.empty_project_context())
    s.update(project_root='', user_request='로그인 기능 추가해줘')
    with patch.object(nodes, 'invoke_agent', side_effect=[valid_pm_plan('backend'), artifact(), json.dumps({'status':'PASS','issues':[]})]) as llm, patch.object(nodes, 'search_backend_context', return_value=[]):
        result = create_workflow().invoke(s)
    assert llm.call_count == 3 and result['backend_fix_count'] == 0
    assert result['backend_validation']['fix']['status'] == 'BLOCKED'
    assert result['final_result'].endswith('FAIL')


def test_prompt_budget_shortage_preserves_code_and_does_not_call_llm():
    s = state(); before = s['backend_result']
    with patch.object(nodes, 'prompt_counter', return_value=(lambda *_: 20000, 'test_counter')), patch.object(nodes, 'invoke_agent_with_metrics') as llm, patch.object(nodes, 'search_backend_context', return_value=[]):
        s.update(nodes.backend_agent(s))
    llm.assert_not_called()
    assert s['backend_result'] == before
    assert s['backend_validation']['fix']['status'] == 'BLOCKED'
    assert s['backend_fix_count'] == 0


def test_unsupported_changed_declaration_stays_not_verified_and_blocks_final():
    s = state()
    output = artifact(GOOD.replace('private final TokenIssuer issuer;', '@Custom\nprivate final TokenIssuer issuer;'))
    r = evaluate(s, output)
    assert r['status'] == 'NOT_VERIFIED'
    s.update(backend_result=output, backend_validation=r, review_status='PASS')
    assert nodes.final_agent(s)['final_result'].endswith('FAIL')


def test_revalidation_does_not_discard_existing_regression_or_allow_blocked_bypass():
    s = state()
    output = artifact(GOOD.replace('public Object signup() { return memberRepository.save(member); }', ''))
    s.update(backend_result=output, backend_validation=evaluate(s, output))
    s.update(nodes.backend_validator(s))
    assert s['backend_validation']['status'] == 'FAIL'
    assert s['backend_validation']['fix']['regressions']
    s = state(False)
    s['backend_result'] = artifact(GOOD)
    s.update(nodes.backend_validator(s))
    assert s['backend_validation']['status'] == 'FAIL'
    assert s['backend_validation']['completeness']['status'] == 'FAIL'

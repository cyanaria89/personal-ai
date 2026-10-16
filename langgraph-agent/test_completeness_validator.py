"""정적 완성도 검사와 기존 Graph 연계의 결정적 회귀 테스트."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import create_workflow
from validators.artifacts import extract_artifacts
from validators.completeness_validator import validate_completeness, fix_validation_payload
from test_integration_reliability import login_fixture
from test_project_context_integration import full_state


def backend(body, name='login'):
    return f'# Backend Agent Output\n## Implementation\n### Service\n#### AuthService.java\n```java\npublic class AuthService {{ public Object {name}() {{ {body}\n }} }}\n```\n'


def frontend(body, label='typescript', path='src/api/auth.ts'):
    return f'# Frontend Implementation\n## Files\n### {path}\n```{label}\nexport async function login() {{ {body} }}\n```\n'


def check(text, agent='backend', request='로그인 기능 구현해줘', **kwargs):
    return validate_completeness(text,agent=agent,user_request=request,required_agents=[agent],**kwargs)


class CompletenessRulesTest(unittest.TestCase):
    def test_fixed_token_flow_and_source_location(self):
        text=backend('String accessToken = "generated_access_token"; return new LoginResponse(accessToken);')
        r=check(text)
        self.assertEqual(r['status'],'FAIL')
        issue=r['issues'][0]
        self.assertEqual(issue['rule'],'FAKE_AUTH_TOKEN')
        self.assertEqual(issue['function'],'login')
        self.assertEqual(issue['file'],'AuthService.java')
        self.assertEqual(text[issue['offset']:issue['offset']+len(issue['evidence']['quote'])],issue['evidence']['quote'])
        self.assertEqual(issue['line'],text.count('\n',0,issue['offset'])+1)

    def test_real_issuance_and_session_delegation_and_constants(self):
        for body in ('String accessToken = issuer.issue(member); return new LoginResponse(accessToken);',
                     'return sessionService.authenticate(request);',
                     'String accessToken = "configuration-label"; return issuer.issue(request);',
                     'int PAGE_SIZE = 20; return authService.login(request);'):
            with self.subTest(body=body): self.assertEqual(check(backend(body))['status'],'PASS')
        self.assertEqual(check(backend('String accessToken = "initial"; accessToken = issuer.issue(request); return new LoginResponse(accessToken);'))['status'],'PASS')
        self.assertEqual(check(backend('String accessToken = "config-label"; return new Settings(accessToken);',name='getConfig'),request='설정 상수 추가해줘')['status'],'PASS')

    def test_unimplemented_exception_and_normal_failure(self):
        for body in ('throw new UnsupportedOperationException("not implemented");',
                     'throw new Error("미구현");'):
            with self.subTest(body=body): self.assertEqual(check(backend(body))['status'],'FAIL')
        self.assertEqual(check(backend('throw new IllegalArgumentException("Invalid password");'))['status'],'PASS')
        self.assertEqual(check(frontend('throw new NotImplementedError();'),agent='frontend')['status'],'FAIL')

    def test_js_token_object_and_aliases(self):
        for label in ('typescript','ts','tsx','javascript','js','jsx'):
            with self.subTest(label=label):
                self.assertEqual(check(frontend('return {accessToken:"fake"};',label),agent='frontend')['status'],'FAIL')
                self.assertEqual(check(frontend('return authClient.login();',label),agent='frontend')['status'],'PASS')

    def test_commented_api_with_success_and_real_callback(self):
        body='// await loginAPI(values);\n console.log("Login success");'
        r=check(frontend(body),agent='frontend')
        self.assertEqual(r['status'],'FAIL',r)
        self.assertEqual(r['issues'][0]['rule'],'COMMENTED_API_FAKE_SUCCESS')
        self.assertEqual(check(frontend(body+' await onSubmit(values);'),agent='frontend')['status'],'PASS')
        quoted=frontend('const example = "// await loginAPI(values);"; console.log("success");')
        self.assertEqual(check(quoted,agent='frontend')['status'],'PASS')

    def test_todo_comments_examples_and_test_mocks(self):
        text=backend('// TODO improve audit logging\n return authService.login(request);')
        self.assertEqual(check(text)['status'],'PASS')
        text='# Example\n### AuthService.java\n```java\nclass AuthService { public Object login() { throw new Error("not implemented"); } }\n```\n'
        r=check(text)
        self.assertEqual(r['status'],'NOT_VERIFIED')
        self.assertEqual(r['coverage']['excluded'][0]['role'],'example')
        r=check(frontend('return {accessToken:"fake"};',path='src/__tests__/auth.test.ts'),agent='frontend',request='Mock으로 로그인 UI 구현해줘')
        self.assertEqual(r['status'],'NOT_APPLICABLE')
        mocked=frontend('return client.login();').replace('export async','import client from "../mocks/client";\nexport async')
        self.assertEqual(check(mocked,agent='frontend')['status'],'NOT_VERIFIED')

    def test_unknown_scope_unsupported_language_and_empty_core(self):
        self.assertEqual(check('구현 내용 설명뿐입니다.')['status'],'NOT_VERIFIED')
        self.assertEqual(check('# Implementation\n### auth.py\n```python\ndef login(): pass\n```')['status'],'NOT_VERIFIED')
        self.assertEqual(check(backend(''))['status'],'FAIL')
        self.assertEqual(check(backend('// TODO later'))['status'],'FAIL')
        self.assertEqual(check(backend('return null;'))['status'],'FAIL')
        self.assertEqual(check(backend('return service.login();'),request='로그인 설계 설명해줘')['status'],'NOT_APPLICABLE')

    def test_deferred_auth_logic_and_unknown_task_are_not_verified(self):
        r=check(frontend('await loginAPI();\n// 여기서는 실제 로그인 처리를 추가해야 합니다.\nsetMessage("성공");'),agent='frontend')
        self.assertEqual(r['status'],'NOT_VERIFIED')
        self.assertEqual(r['issues'][0]['rule'],'COMPLETENESS_NOT_VERIFIED')
        self.assertEqual(check(backend('return service.run();'),request='확인해줘')['status'],'NOT_VERIFIED')

    def test_real_file_is_checked_even_when_example_exists(self):
        example='# Example\n### AuthService.java\n```java\npublic class AuthService { public Object login() { throw new Error("not implemented"); } }\n```\n'
        good=backend('return sessions.authenticate(request);')
        self.assertEqual(check(good+example)['status'],'PASS')
        broken=good.replace('return sessions.authenticate(request);','throw new Error("not implemented");')
        self.assertEqual(check(broken+example)['status'],'FAIL')

    def test_unknown_extra_file_and_broken_fence_are_not_verified(self):
        good=backend('return sessions.authenticate(request);')
        mixed=good+'\n## Implementation\n### helper.py\n```python\ndef helper(): pass\n```\n'
        self.assertEqual(check(mixed)['status'],'NOT_VERIFIED')
        self.assertEqual(check(good+'\n```java\nclass Broken {')['status'],'NOT_VERIFIED')

    def test_fix_payload_preserves_issue_evidence_without_duplicated_coverage(self):
        r=check(backend('String accessToken = "fake"; return new LoginResponse(accessToken);'))
        validation={'status':'FAIL','issues':r['issues'],'completeness':r}
        payload=fix_validation_payload(validation)
        self.assertEqual(payload,{'status':'FAIL','issues':r['issues']})
        self.assertIn('evidence',payload['issues'][0])

    def test_snapshot_reuse_and_partial_absence(self):
        context={'selected_files':[{'path':'src/AuthService.java','content':'public class AuthService { public Object login() { return sessions.authenticate(); } }','truncated':False}]}
        self.assertEqual(check('기존 src/AuthService.java 재사용',project_context=context)['status'],'PASS')
        partial=copy.deepcopy(context);partial['selected_files'][0]['truncated']=True
        self.assertEqual(check('기존 src/AuthService.java 재사용',project_context=partial)['status'],'NOT_VERIFIED')
        self.assertEqual(check('기존 Missing.java 재사용',project_context=context)['status'],'NOT_VERIFIED')

    def test_fix_rechecks_and_does_not_drop_core_or_truncation(self):
        state=full_state(nodes.empty_project_context())
        state['backend_result']=backend('String accessToken = "fake"; return new LoginResponse(accessToken);')
        first=nodes.backend_validator(state)
        self.assertEqual(first['backend_validation']['status'],'FAIL')
        state.update(first)
        state['backend_result']=backend('return issuer.issue(request);')
        second=nodes.backend_validator(state)
        # 선언/계약이 확인되지 않은 issuer 위임으로 원래 인증 결함을 없애지 않는다.
        self.assertEqual(second['backend_validation']['completeness']['status'],'FAIL')
        self.assertIn('FAKE_AUTH_TOKEN',str(second['backend_validation']))
        state['llm_metrics']=[{'agent':'backend','done_reason':'length'}]
        third=nodes.backend_validator(state)
        self.assertEqual(third['backend_validation']['status'],'FAIL')
        self.assertIn('TRUNCATED_LLM_OUTPUT',str(third))
        self.assertIn('completeness',third['backend_validation'])

    def test_no_new_requirement_from_unselected_or_other_feature(self):
        self.assertEqual(validate_completeness(backend('throw new Error("not implemented");'),agent='backend',user_request='로그인 구현',required_agents=['frontend'])['status'],'NOT_APPLICABLE')
        text=backend('return authService.login(request);')+backend('throw new Error("not implemented");',name='signup')
        self.assertEqual(check(text)['status'],'PASS')
        self.assertEqual(check(backend('return service.login();'),request='로그인 구현하고 설명해줘')['status'],'PASS')


class CompletenessGraphTest(unittest.TestCase):
    def state(self):
        s=full_state(nodes.empty_project_context())
        s.update(project_root='',required_agents=['backend'],user_request='로그인 기능 추가해줘')
        return s

    def test_fail_and_required_unverified_cannot_become_final_pass(self):
        for output in (backend('String accessToken = "fake"; return new LoginResponse(accessToken);'),'구현 근거가 부족합니다.'):
            with self.subTest(output=output):
                s=self.state();s['backend_result']=output;s.update(nodes.backend_validator(s))
                with patch.object(nodes,'invoke_agent',return_value=json.dumps({'status':'PASS','issues':[]})):
                    s.update(nodes.review_agent(s))
                self.assertEqual(s['review_status'],'FAIL')
                s['review_status']='PASS'
                final=nodes.final_agent(s)['final_result']
                self.assertTrue(final.endswith('FAIL'))
                self.assertIn('빌드·실행',final)

    def test_persistent_stub_stops_after_two_agent_fixes(self):
        s=self.state()
        bad=backend('throw new UnsupportedOperationException("not implemented");')
        with (patch.object(nodes,'search_backend_context',return_value=[]),
              patch.object(nodes,'invoke_agent',side_effect=['REQUIRED_AGENTS: backend',bad,bad,bad,json.dumps({'status':'PASS','issues':[]})])):
            result=create_workflow().invoke(s)
        self.assertEqual(result['backend_fix_count'],2)
        self.assertEqual(result['integration_fix_count'],0)
        self.assertTrue(result['final_result'].endswith('FAIL'))

    def test_repaired_stub_exits_loop_and_keeps_static_scope(self):
        s=self.state()
        bad=backend('throw new UnsupportedOperationException("not implemented");')
        good=backend('return issuer.issue(request);')
        with (patch.object(nodes,'search_backend_context',return_value=[]),
              patch.object(nodes,'invoke_agent',side_effect=['REQUIRED_AGENTS: backend',bad,good,json.dumps({'status':'PASS','issues':[]})])):
            result=create_workflow().invoke(s)
        self.assertEqual(result['backend_fix_count'],1)
        self.assertTrue(result['final_result'].endswith('PASS'))
        self.assertEqual(result['backend_validation']['completeness']['runtime']['status'],'NOT_VERIFIED')

    def test_existing_login_contract_fixture_remains_independent(self):
        # The old fixture uses member information rather than JWT. Do not add JWT requirements.
        fixture=login_fixture()
        r=check(fixture['backend'])
        self.assertEqual(r['status'],'PASS',r)

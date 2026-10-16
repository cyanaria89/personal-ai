"""Deterministic contract/coverage regressions; no live LLM or RAG dependency."""
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import (
    create_workflow, get_max_agent_fix_count, get_max_integration_fix_count,
    route_after_integration_validator,
)
from test_integration_validator import backend_fixture, frontend_fixture, issue_rules
from test_project_context_integration import full_state
from validators.integration_validator import validate_integration_result


def login_fixture():
    text = (Path(__file__).parent / 'outputs/agent_result_20260826_145148.md').read_text()
    def section(start, end):
        return text.split(start, 1)[1].split(end, 1)[0].strip().removesuffix('---').strip()
    return {
        'pm': section('## 2. PM 작업 계획', '## 3. DB Agent 결과'),
        'backend': section('## 4. Backend Agent 결과', '## 5. Frontend Agent 결과'),
        'frontend': section('## 5. Frontend Agent 결과', '## 6. Review Agent 결과'),
        'review': section('## 6. Review Agent 결과', '## 최종 판정'),
    }


class IntegrationCoverageTest(unittest.TestCase):
    def test_all_frontend_fence_aliases(self):
        for label in ('typescript', 'ts', 'tsx', 'javascript', 'js', 'jsx', 'TypeScript'):
            with self.subTest(label=label):
                f = frontend_fixture().replace('```tsx', '```' + label)
                result = validate_integration_result(backend_fixture(), f)
                self.assertEqual(result['status'], 'PASS', result)
                self.assertEqual(result['coverage']['matched_requests'], 1)

    def test_multiple_routes_and_requests_all_checked(self):
        b = backend_fixture() + backend_fixture(mapping='@PostMapping("/login")')
        f = frontend_fixture() + frontend_fixture('const r = await axios.post("/login", {});')
        r = validate_integration_result(b, f)
        self.assertEqual(r['status'], 'PASS', r)
        self.assertEqual(r['coverage']['matched_requests'], 2)
        for broken, rule in ((f.replace('/login', '/wrong'), 'ENDPOINT_PATH_MISMATCH'),
                             (f.replace('axios.post', 'axios.get'), 'HTTP_METHOD_MISMATCH')):
            with self.subTest(rule=rule):
                r = validate_integration_result(b, broken)
                self.assertEqual(r['status'], 'FAIL')
                self.assertIn(rule, issue_rules(r))

    def test_path_parameters_literals_templates_and_query(self):
        b = backend_fixture(mapping='@GetMapping("/members/{id}")')
        # Exercise nested parentheses in actual Java parameter annotations too.
        b = b.replace('SignupRequest request', '@PathVariable("id") Long id')
        for url in ('"/members/42"', '`/members/${memberId}`', '"/members/42?view=short#top"'):
            with self.subTest(url=url):
                f = frontend_fixture(f'const response = await fetch({url});')
                self.assertEqual(validate_integration_result(b, f)['status'], 'PASS')
        f = frontend_fixture('await fetch("/member/42");')
        self.assertEqual(validate_integration_result(b, f)['status'], 'FAIL')

    def test_no_evidence_and_partial_dynamic_calls_are_not_verified(self):
        for b, f in (
            ('', frontend_fixture()), (backend_fixture(), ''),
            (backend_fixture(), frontend_fixture('await callback();')),
            (backend_fixture(), frontend_fixture() + frontend_fixture('await fetch(url, options);')),
            (backend_fixture(), frontend_fixture() + frontend_fixture('await fetch(`${base}/signup`, {method:"POST"});')),
        ):
            with self.subTest(backend=bool(b), frontend=f):
                r = validate_integration_result(b, f)
                self.assertEqual(r['status'], 'NOT_VERIFIED', r)
                self.assertIn('INTEGRATION_NOT_VERIFIED', issue_rules(r))

    def test_partial_unsupported_backend_mapping_is_not_verified(self):
        for mapping in ('@PostMapping(API_PATH)', '@PostMapping("/other" + SUFFIX)',
                        '@RequestMapping("/other")', '@RequestMapping(\nmethod = RequestMethod.POST, path="/other")'):
            with self.subTest(mapping=mapping):
                b = backend_fixture() + backend_fixture(mapping=mapping)
                r = validate_integration_result(b, frontend_fixture())
                self.assertEqual(r['status'], 'NOT_VERIFIED', r)
                self.assertEqual(r['coverage']['matched_requests'], 1)

    def test_confirmed_mismatch_is_fail_even_with_unverified_call(self):
        f = frontend_fixture('await fetch("/wrong", {method:"POST"}); await fetch(url);')
        r = validate_integration_result(backend_fixture(), f)
        self.assertEqual(r['status'], 'FAIL')
        self.assertTrue({'ENDPOINT_PATH_MISMATCH','INTEGRATION_NOT_VERIFIED'} <= issue_rules(r))

    def test_comments_and_quoted_examples_do_not_count_as_requests(self):
        f = frontend_fixture('// await fetch("/signup", {method:"POST"});\n'
                             'const example = "axios.post(\'/signup\')";')
        r = validate_integration_result(backend_fixture(), f)
        self.assertEqual(r['status'], 'NOT_VERIFIED')
        self.assertEqual(r['coverage']['frontend_requests'], 0)

    def test_explicit_status_checked_per_endpoint(self):
        b = backend_fixture() + backend_fixture(mapping='@PostMapping("/login")')
        f = frontend_fixture() + frontend_fixture('const r = await axios.post("/login", {});',
                                                  'if (r.status === 201) {}')
        r = validate_integration_result(b, f)
        self.assertEqual(r['status'], 'FAIL')
        self.assertIn('SUCCESS_STATUS_MISMATCH', issue_rules(r))
        self.assertEqual(r['coverage']['explicit_status_checks'], 1)

    def test_unknown_backend_status_with_explicit_condition_is_not_verified(self):
        b = backend_fixture(return_type='ResponseEntity<SignupResponse>', body='return response;')
        f = frontend_fixture(condition='if (response.status === 201) {}')
        self.assertEqual(validate_integration_result(b, f)['status'], 'NOT_VERIFIED')

    def test_request_status_conditions_do_not_mix_between_functions(self):
        b = backend_fixture() + backend_fixture(mapping='@PostMapping("/login")')
        f = '''```typescript
async function signup() {
    const response = await fetch('/signup', {method:'POST'});
    if (response.status === 200) {}
}
async function login() {
    const response = await fetch('/login', {method:'POST'});
    if (response.status === 201) {}
}
```'''
        r = validate_integration_result(b, f)
        self.assertEqual(r['status'], 'FAIL', r)
        self.assertEqual(r['coverage']['explicit_status_checks'], 2)
        self.assertIn('SUCCESS_STATUS_MISMATCH', issue_rules(r))

    def test_unsupported_method_options_do_not_silently_default(self):
        for call in ('await fetch("/signup", {method:"POST", ...options});',
                     'await fetch("/signup", {method:"POST", method:"DELETE"});',
                     'await fetch("/signup", {method:verb});',
                     'await fetch("/signup" + suffix, {method:"POST"});',
                     'await axios({url:"/signup", method:"POST"});'):
            with self.subTest(call=call):
                r = validate_integration_result(backend_fixture(), frontend_fixture() + frontend_fixture(call))
                self.assertEqual(r['status'], 'NOT_VERIFIED', r)

    def test_existing_login_fixture_and_wrong_url(self):
        fixture = login_fixture()
        r = validate_integration_result(fixture['backend'], fixture['frontend'])
        self.assertEqual(r['status'], 'PASS', r)
        self.assertGreaterEqual(r['coverage']['matched_requests'], 1)
        broken = fixture['frontend'].replace('/api/members/login', '/api/wrong-login')
        self.assertNotEqual(broken, fixture['frontend'])
        r = validate_integration_result(fixture['backend'], broken)
        self.assertEqual(r['status'], 'FAIL', r)
        self.assertIn('ENDPOINT_PATH_MISMATCH', issue_rules(r))


class IntegrationDecisionTest(unittest.TestCase):
    def state(self):
        s = full_state(nodes.empty_project_context())
        s.update(required_agents=['backend','frontend'], review_status='PASS')
        return s

    def test_unverified_missing_and_fail_block_review_and_final(self):
        for status in ('NOT_VERIFIED','NOT_RUN','FAIL'):
            with self.subTest(status=status):
                s = self.state()
                s['integration_validation'] = {'status':status,'issues':[]}
                with patch.object(nodes, 'invoke_agent', return_value=json.dumps({'status':'PASS','issues':[]})):
                    review = nodes.review_agent(s)
                self.assertEqual(review['review_status'], 'FAIL')
                self.assertIn('INTEGRATION_NOT_VERIFIED', review['review_result'])
                s.update(review)
                final = nodes.final_agent(s)['final_result']
                self.assertIn(status, final)
                self.assertTrue(final.endswith('FAIL'))
                # Defense in depth: stale/external Review PASS cannot bypass Final.
                s['review_status'] = 'PASS'
                self.assertTrue(nodes.final_agent(s)['final_result'].endswith('FAIL'))

    def test_db_only_is_not_applicable_and_does_not_block_final(self):
        s = self.state()
        s['required_agents'] = ['db']
        with patch.object(nodes, 'validate_integration_result') as validate:
            result = nodes.integration_validator(s)
        validate.assert_not_called()
        self.assertEqual(result['integration_validation']['status'], 'NOT_RUN')
        s.update(result)
        with patch.object(nodes, 'invoke_agent', return_value=json.dumps({'status':'PASS','issues':[]})):
            s.update(nodes.review_agent(s))
        self.assertEqual(s['review_status'], 'PASS')
        self.assertTrue(nodes.final_agent(s)['final_result'].endswith('PASS'))

    def test_no_new_retry_loop_and_existing_limits_unchanged(self):
        self.assertEqual(get_max_agent_fix_count(), 2)
        self.assertEqual(get_max_integration_fix_count(), 2)
        s = self.state()
        s['integration_validation'] = {'status':'NOT_VERIFIED','issues':[]}
        self.assertEqual(route_after_integration_validator(s), 'review')
        s['integration_validation'] = {'status':'FAIL','issues':[{'target_agent':'frontend'}]}
        s['integration_fix_count'] = 1
        self.assertEqual(route_after_integration_validator(s), 'frontend')
        s['integration_fix_count'] = 2
        self.assertEqual(route_after_integration_validator(s), 'review')

    def test_login_graph_and_unverified_graph_reach_honest_final(self):
        fixture = login_fixture()
        unextractable = fixture['frontend'].replace('fetch(', 'customTransport(')
        self.assertNotEqual(unextractable, fixture['frontend'])
        for frontend, expected in ((fixture['frontend'], 'PASS'),
                                   (unextractable, 'NOT_VERIFIED'),
                                   (fixture['frontend'].replace('/api/members/login','/api/wrong-login'), 'FAIL')):
            with self.subTest(expected=expected):
                s = self.state()
                s.update(project_root='', project_plan='', frontend_result='', backend_result='')
                with (patch.object(nodes,'search_backend_context',return_value=[]),
                      patch.object(nodes,'search_frontend_context',return_value=[]),
                      patch.object(nodes,'invoke_agent',side_effect=[fixture['pm'],fixture['backend'],frontend,
                                             json.dumps({'status':'PASS','issues':[]})])):
                    result=create_workflow().invoke(s)
                self.assertEqual(result['frontend_validation']['status'], 'PASS')
                self.assertEqual(result['integration_validation']['status'],expected)
                self.assertEqual(result['review_status'], 'PASS' if expected=='PASS' else 'FAIL')
                self.assertTrue(result['final_result'].endswith('PASS' if expected=='PASS' else 'FAIL'))

    def test_persistent_integration_failure_stops_after_two_fixes(self):
        fixture = login_fixture()
        s = self.state()
        s.update(project_root='', project_plan='', frontend_result='', backend_result='')
        failed = {'status':'FAIL', 'issues':[{
            'severity':'Major', 'rule':'SUCCESS_STATUS_MISMATCH', 'target_agent':'frontend',
            'message':'Frontend 성공 조건이 Backend와 불일치합니다.',
            'required_fix':'성공 status 조건을 일치시키세요.',
        }]}
        responses = [fixture['pm'], fixture['backend'], fixture['frontend'],
                     fixture['frontend'], fixture['frontend'], json.dumps({'status':'PASS','issues':[]})]
        with (patch.object(nodes,'search_backend_context',return_value=[]),
              patch.object(nodes,'search_frontend_context',return_value=[]) as search,
              patch.object(nodes,'validate_integration_result',return_value=failed) as validator,
              patch.object(nodes,'invoke_agent',side_effect=responses)):
            result = create_workflow().invoke(s)
        self.assertEqual(result['integration_fix_count'], 2)
        self.assertEqual(result['frontend_fix_count'], 0)
        self.assertEqual(validator.call_count, 3)
        self.assertEqual(search.call_count, 3)
        self.assertEqual(result['review_status'], 'FAIL')
        self.assertTrue(result['final_result'].endswith('FAIL'))

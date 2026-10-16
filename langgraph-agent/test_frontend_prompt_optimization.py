"""Frontend 전용 projection/참고 출력 경계/예산 검증. 실제 LLM은 호출하지 않는다."""
import copy
from unittest.mock import patch

import pytest
import agents.nodes as nodes
from prompts.loader import load_agent_prompt, read_markdown, SYSTEM_PROMPT_DIR, AGENT_RULES_DIR
from prompts.frontend_context import project_frontend_rules, project_templates, project_previous_frontend, LEGACY_FIX_RULES
from rag.prompt_budget import pack_frontend_rag, prompt_counter
from validators.frontend_validator import validate_frontend_result, _extract_output_files
from test_frontend_fix_context import base_state, BACKEND_RESULT

FRONTEND = '''# Frontend Implementation
## Files
### src/api/auth.ts
```typescript
export async function login(payload: {loginId: string; password: string}) {
  const response = await fetch("/api/login", {method: "POST", body: JSON.stringify(payload)});
  if (!response.ok) throw new Error("로그인 실패");
  return response.json();
}
```
### src/LoginPage.tsx
```tsx
import { login } from "./api/auth";
import "./LoginPage.css";
export function LoginPage() { return <button onClick={() => login({loginId: "id", password: "value"})}>로그인</button>; }
```
### src/LoginPage.css
```css
button { color: black; }
```
## API Clarification
- Endpoint: POST /api/login
## Verification Notes
- API import/export 및 CSS 연결 유지
'''


def echo(frontend=FRONTEND, contract=None):
    contract = contract or nodes.extract_frontend_fix_backend_context(BACKEND_RESULT)
    return frontend.rstrip() + '\n\n[현재 Backend 관련 API 계약]\n' + contract + '\n\n[반드시 해결할 Frontend Validator Issues]\n{"status":"FAIL","issues":[]}\n\n' + LEGACY_FIX_RULES


def captured(mode, *, output=FRONTEND, counter=None):
    s = base_state(); s['user_request'] = '로그인 기능 구현해줘'; s['frontend_result'] = output
    s['llm_metrics'] = []
    issue = {'rule':'KEEP_ISSUE','severity':'Major','target_agent':'frontend','message':'근거','required_fix':'KEEP_COMPLETION'}
    s['frontend_validation'] = {'status':'FAIL' if mode=='validator_fix' else 'PASS','issues':[issue] if mode=='validator_fix' else []}
    s['integration_validation'] = {'status':'FAIL' if mode=='integration_fix' else 'PASS','issues':[issue] if mode=='integration_fix' else []}
    capture = {}
    def invoke(llm, system, user, **kwargs):
        capture.update(system=system,user=user,llm=llm)
        return FRONTEND
    def counter_value(model):
        return (counter, 'utf8_upper_bound') if counter else prompt_counter(model)
    with patch.object(nodes,'search_frontend_context',return_value=[]), patch.object(nodes,'invoke_agent_with_metrics',side_effect=invoke), patch('rag.prompt_budget.prompt_counter',side_effect=counter_value):
        update = nodes.frontend_agent(s)
    return s, update, capture


@pytest.mark.parametrize('mode',['initial','validator_fix','integration_fix'])
def test_projection_preserves_common_and_all_active_safety_rules(mode):
    projected = load_agent_prompt('frontend',mode=mode)
    original = load_agent_prompt('frontend')
    assert len(projected) < len(original)
    for directory, filename in ((SYSTEM_PROMPT_DIR,'00_Common_System_Prompt.md'),(AGENT_RULES_DIR,'00_Common_Agent_Rules.md')):
        assert read_markdown(directory/filename) in projected
    for phrase in ('## 9. Validation Checklist','## 10. Prohibitions','# 9. Validation Checklist','# 12. Prohibitions','## Files','## API Clarification','## Verification Notes','UNKNOWN (미확정)'):
        assert phrase in projected
    assert '7.2 Design Request' not in projected and '8.2 Design Request' not in projected
    assert '# Frontend → Review Handoff' not in projected


def test_projection_keeps_new_rules_inside_target_section_and_malformed_source():
    text='## 8. Handoff to Review Agent\n안전 규칙을 반드시 유지하세요.\n```md\n# Template\n```\n## 9. Next\nKEEP'
    assert project_templates(text, {'8. Handoff to Review Agent'}) == text
    broken=text+'\n```'
    assert project_templates(broken, {'8. Handoff to Review Agent'}) == broken


def test_non_frontend_agents_and_default_or_design_are_unchanged():
    for agent in ('db','backend','pm','review'):
        assert load_agent_prompt(agent,mode='validator_fix') == load_agent_prompt(agent)
    raw_system=read_markdown(SYSTEM_PROMPT_DIR/'04_Frontend_Agent_System_Prompt.md')
    raw_rules=read_markdown(AGENT_RULES_DIR/'04_Frontend_Agent_Rules.md')
    assert project_frontend_rules(raw_system,raw_rules,'design') == (raw_system,raw_rules)


@pytest.mark.parametrize('mode',['initial','validator_fix','integration_fix'])
def test_modes_preserve_request_project_contract_and_issue(mode):
    s,update,p = captured(mode)
    assert s['user_request'] in p['user']
    assert nodes.project_context_projection(s,'frontend',fix_mode=mode!='initial') in p['user']
    assert nodes.extract_frontend_fix_project_context(s['project_plan']) in p['user']
    expected_contract = (nodes.extract_frontend_initial_backend_context(BACKEND_RESULT)
                         if mode == 'initial' else nodes.extract_frontend_fix_backend_context(BACKEND_RESULT))
    assert expected_contract in p['user']
    if mode!='initial':
        assert FRONTEND in p['user'] and 'KEEP_ISSUE' in p['user'] and 'KEEP_COMPLETION' in p['user']
        assert '## Verification Notes만 출력' in p['user']
        assert '무관한 신규 파일' in p['user'] and 'diff나 부분 파일은 금지' in p['user']
    assert update['frontend_result'] == FRONTEND


def test_verified_echo_projection_preserves_every_frontend_file_import_export_css_and_call():
    previous = echo()
    clean = project_previous_frontend(previous,nodes.extract_frontend_fix_backend_context(BACKEND_RESULT))
    assert clean == FRONTEND.rstrip()
    assert _extract_output_files(previous) == _extract_output_files(clean)
    assert validate_frontend_result(clean,user_request='로그인 구현',required_agents=['backend','frontend'])['status']=='PASS'
    _,_,p=captured('integration_fix',output=previous)
    assert 'src/LoginPage.css' in p['user'] and 'export async function login' in p['user']
    assert p['user'].count('[현재 Backend 관련 API 계약]')==1


@pytest.mark.parametrize('change',['unknown_tail','different_contract','frontend_code'])
def test_unverified_tail_is_never_discarded(change):
    text=echo()
    contract=nodes.extract_frontend_fix_backend_context(BACKEND_RESULT)
    if change=='unknown_tail': text+='\n추가 필수 계약'
    if change=='different_contract': contract+='\n추가 계약'
    if change=='frontend_code': text+='\n```ts\nexport const keep = true;\n```'
    assert project_previous_frontend(text,contract)==text


def test_reference_marker_in_actual_code_is_not_removed_or_failed():
    source=FRONTEND.replace('export async function login', 'const text = `\n[현재 Backend 관련 API 계약]\n`;\nexport async function login')
    assert project_previous_frontend(source,'anything')==source
    assert validate_frontend_result(source)['status']=='PASS'


def test_reference_echo_is_fail_and_real_files_remain_available():
    result=validate_frontend_result(echo())
    assert result['status']=='FAIL'
    assert any(i['rule']=='COPIED_REFERENCE_OUTPUT' for i in result['issues'])
    assert set(_extract_output_files(echo()))==set(_extract_output_files(FRONTEND))


@pytest.mark.parametrize('tokens,allowed',[(9984,True),(9985,False)])
def test_fallback_counter_boundary_also_stops_before_llm(tokens,allowed):
    if allowed:
        _,_,p=captured('validator_fix',counter=lambda *_:tokens)
        assert p
    else:
        with pytest.raises(ValueError,match='LLM 호출을 중단'):
            captured('validator_fix',counter=lambda *_:tokens)


def test_optional_rag_reserves_extra_headroom_without_lowering_core_limit():
    count=lambda s,u:len(s)+len(u)
    r={'source':'s','heading':'h','content':'chunk','score':1.0}
    _,m=pack_frontend_rag('system','user',[r],model='test',num_ctx=12288,num_predict=2048,counter=count,rag_headroom=128)
    assert m['input_limit']==9984 and m['rag_input_limit']==9856
    assert m['injected_count']==1 and not m['budget_exceeded']


def test_compact_fix_contract_preserves_dto_method_path_status_and_handoff():
    from test_frontend_initial_projection import BACKEND_RESULT as backend
    s=base_state();s.update(user_request='로그인 구현',frontend_result=FRONTEND,backend_result=backend,
        frontend_validation={'status':'FAIL','issues':[{'rule':'SELF_IMPORT','required_fix':'imports 수정'}]})
    p={}
    def invoke(llm,system,user,**kw): p.update(user=user);return FRONTEND
    with patch.object(nodes,'invoke_agent_with_metrics',side_effect=invoke),patch.object(nodes,'search_frontend_context',return_value=[]):
        nodes.frontend_agent(s)
    contract=nodes.extract_frontend_initial_backend_context(backend)
    assert contract in p['user']
    for value in ('LoginRequest','LoginResponse','@RequestMapping','@PostMapping','@ResponseStatus','Frontend Handoff'):
        assert value in p['user']
    assert 'REMOVE_CONTROLLER_IMPLEMENTATION.login' not in p['user']


def test_initial_design_only_keeps_design_templates_even_when_request_mentions_implementation():
    s=base_state();s['user_request']='Frontend 구현 계획만 설명해줘'
    p={}
    def invoke(llm,system,user,**kw): p.update(system=system);return '설계 설명'
    with patch.object(nodes,'invoke_agent_with_metrics',side_effect=invoke),patch.object(nodes,'search_frontend_context',return_value=[]):
        nodes.frontend_agent(s)
    assert p['system']==load_agent_prompt('frontend')


def test_fixed_output_does_not_turn_existing_completeness_gaps_into_success():
    from validators.completeness_validator import attach_completeness
    output=FRONTEND.replace('return response.json();','throw new Error("not implemented");')
    s=base_state();s.update(required_agents=['backend','frontend'],user_request='로그인 구현')
    v=attach_completeness(validate_frontend_result(output),output,s,'frontend')
    assert v['status']=='FAIL' and v['completeness']['status']=='FAIL'
    output=FRONTEND.replace('return response.json();','// 여기서는 실제 로그인 처리를 추가해야 합니다.\nreturn response.json();')
    v=attach_completeness(validate_frontend_result(output),output,s,'frontend')
    assert v['status']=='NOT_VERIFIED' and v['completeness']['status']=='NOT_VERIFIED'

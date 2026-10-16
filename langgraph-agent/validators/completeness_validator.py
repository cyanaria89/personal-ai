"""1차 정적 완성도 검사: Java/JS/TS의 명확한 Stub만 확정한다.

PASS는 아래 지원 규칙의 검사 통과이며 실행/기능 전체의 증명이 아니다.
사용자 요청과 실제 전달 파일을 검사한다. PM/RAG 예제를 요구사항으로 쓰지 않는다.
"""
import re

from validators.artifacts import extract_artifacts
from validators.integration_validator import _matching_brace, _mask_non_code

SCOPE = 'static_stub_checks_v1'
RULES = ['UNIMPLEMENTED_EXCEPTION', 'FAKE_AUTH_TOKEN', 'COMMENTED_API_FAKE_SUCCESS', 'EMPTY_REQUIRED_FUNCTION']


def completeness_required(agent, request, required_agents):
    if agent not in required_agents or agent not in {'backend','frontend'}:
        return False
    if (re.search(r'설명만|분석만|계획만|analysis only', request, re.I)
        or (re.search(r'설명해|분석해|계획을|explain', request, re.I)
            and not re.search(r'구현|작성|추가|개발|만들|implement|create|build',request,re.I))):
        return False
    if re.search(r'(?:Mock|mock|모의)(?:으로|만| API| 데이터)|테스트용\s*Mock', request) and not re.search(r'제거|실제', request):
        return False
    return True


def _functions(content, language, unknown=None):
    # Only block-bodied Java methods and JS/TS functions/arrows are supported.
    if language == 'java':
        pattern = re.compile(r'\b(?:public|private|protected)\s+(?:(?:static|final|synchronized)\s+)*[\w.<>, ?\[\]]+\s+(\w+)\s*\(')
    else:
        pattern = re.compile(r'\b(?:async\s+)?function\s+(\w+)\s*\(|\b(?:const|let)\s+(\w+)\s*=\s*(?:async\s*)?\(')
    code = _mask_non_code(content)
    functions = []
    for match in pattern.finditer(code):
        if language == 'java' and re.match(r'\b(?:public|private|protected)\s+(?:record|class|interface|enum)\b', match.group(0)):
            continue
        end_params = _matching_brace(content, match.end()-1)
        if end_params is None:
            if unknown is not None: unknown.append(f"함수 parameter가 불완전합니다: {match.group(1)}")
            continue
        tail = content[end_params+1:]
        body = re.match(r'\s*(?::\s*[^={;\n]+)?\s*(?:=>\s*)?\{', tail)
        if body is None:
            # A Java declaration without a body can be an interface/abstract method.
            if unknown is not None and not (language == 'java' and re.match(r'\s*;',tail)):
                unknown.append(f"지원하지 않는 함수 본문 형식: {next(g for g in match.groups() if g)}")
            continue
        opening = end_params+1+body.end()-1
        closing = _matching_brace(content, opening)
        if closing is not None:
            functions.append({'name':next(g for g in match.groups() if g),
                              'start':opening+1,'end':closing})
        elif unknown is not None:
            unknown.append('닫히지 않은 함수 본문이 있습니다.')
    return functions


def _relevant(function, path, request):
    wanted = []
    if re.search(r'로그인|login|sign.?in', request, re.I): wanted.append('login')
    if re.search(r'회원가입|signup|register', request, re.I): wanted.append('signup')
    if not wanted:
        return True
    for feature, pattern in (('login',r'login|signin'),('signup',r'signup|register')):
        if re.search(pattern, function, re.I):
            return feature in wanted
    return True  # file-local handlers and generic helpers are delivered implementation


def _findings(artifact, request):
    text, language = artifact['content'], artifact['language']
    issues, unknown = [], []
    functions = _functions(text, language, unknown)
    for function in functions:
        if not _relevant(function['name'], artifact['path'], request):
            continue
        start, end = function['start'], function['end']
        body = text[start:end]
        comments_removed = _mask_non_code(body, strings=False)
        code = _mask_non_code(body)
        def issue(rule, match, message):
            local = start + match.start()
            if any(start < other['start'] <= local < other['end'] <= end for other in functions):
                return
            quote = text[local:local+len(match.group(0))]
            issues.append({'severity':'Major','rule':rule,'target_agent':None,
                'message':message, 'required_fix':'요청 범위와 확정된 계약에 맞게 해당 Stub을 실제 로직 또는 기존 구현 위임으로 교체하세요. 새로운 인증 방식이나 API를 임의로 추가하지 마세요.',
                'file':artifact['path'],'function':function['name'],
                'language':language, 'origin':artifact['origin'],
                'line':artifact['line']+text.count('\n',0,local),
                'offset':artifact['start']+local,
                'evidence':{'source':artifact['origin'],'quote':quote}, 'scope':SCOPE})
        if not code.strip() and re.search(r'login|signin|signup|register', function['name'], re.I):
            issue('EMPTY_REQUIRED_FUNCTION', re.match(r'[\s\S]*', body), '요청 범위의 핵심 함수 본문이 비어 있습니다.')
        if re.fullmatch(r'\s*return\s+null\s*;?\s*', code) and re.search(r'login|signin|signup|register',function['name'],re.I):
            issue('EMPTY_REQUIRED_FUNCTION',re.search(r'return\s+null\s*;?',body),'요청 범위의 핵심 함수가 다른 작업 없이 null만 반환합니다.')
        exception = re.compile(r'\bthrow\s+(?:new\s+)?(?:Error|UnsupportedOperationException|NotImplementedException|NotImplementedError)\s*\(\s*[\"\'][^\"\'\n]*(?:not\s+implemented|unimplemented|TODO|미구현|구현\s*필요)[^\"\'\n]*[\"\']\s*\)', re.I)
        for match in exception.finditer(comments_removed):
            if code[match.start():match.start()+5] == 'throw':
                issue('UNIMPLEMENTED_EXCEPTION',match,'실제 전달 함수가 미구현 예외를 던집니다.')
        for match in re.finditer(r'\bthrow\s+(?:new\s+)?(?:NotImplementedException|NotImplementedError)\s*\(\s*\)', comments_removed):
            if code[match.start():match.start()+5] == 'throw':
                issue('UNIMPLEMENTED_EXCEPTION',match,'실제 전달 함수가 명시적 미구현 예외를 던집니다.')
        # Local literal -> returned auth token. No JWT shape or storage policy assumed.
        auth_context = bool(re.search(r'login|signin|authenticate|(?:issue|generate|create).*token', function['name'], re.I)
                            or re.search(r'new\s+\w*(?:Login|Auth|Token)\w*Response\s*\(', code))
        token_assign = re.compile(r'\b(?:String|const|let|var)\s+(accessToken|refreshToken|authToken)\s*=\s*([\"\'])([^\"\'\n]+)\2\s*;',re.I)
        for match in token_assign.finditer(comments_removed):
            if not auth_context:
                continue
            name = match.group(1)
            if not code[match.start():match.start()+len(match.group(0).split('=')[0])].strip():
                continue
            returned = re.search(r'\breturn\b[\s\S]*?\b'+re.escape(name)+r'\b', code[match.end():])
            overwritten = returned and re.search(r'\b'+re.escape(name)+r'\s*=',code[match.end():match.end()+returned.end()])
            if returned and not overwritten:
                issue('FAKE_AUTH_TOKEN',match,'인증 응답에 지역 고정 문자열 Token을 반환합니다.')
        # JS object literal response (e.g. return { accessToken: "demo" }).
        literal_token = re.compile(r'\b(?:accessToken|refreshToken|authToken)\s*:\s*([\"\'])([^\"\'\n]+)\1',re.I)
        if language != 'java' and auth_context:
            for match in literal_token.finditer(comments_removed):
                if code[match.start():match.start()+len('accessToken')].strip() and re.search(r'\breturn\s*\{[^}]*$', code[:match.start()]):
                    issue('FAKE_AUTH_TOKEN',match,'인증 응답 객체에 고정 문자열 Token을 반환합니다.')
        commented_call = re.search(r'//[^\n]*(?:await\s+)?(?:fetch|axios\.\w+|\w*(?:signup|login|API)\w*)\s*\([^\n]*',body,re.I)
        success = re.search(r'(?:console\.log|setMessage|setSuccess)\s*\([^\n]*(?:성공|완료|success)',comments_removed,re.I)
        calls = re.findall(r'\b([A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)?)\s*\(',code)
        real_calls = [c for c in calls if c not in {'console.log','setMessage','setSuccess','setLoading','setError','preventDefault','event.preventDefault'} and c not in {'if','catch','Error'}]
        actual_comment = commented_call and not comments_removed[commented_call.start():commented_call.end()].strip()
        actual_success = success and bool(code[success.start():success.start()+len(success.group(0).split('(')[0])].strip())
        if actual_comment and actual_success and not real_calls:
            issue('COMMENTED_API_FAKE_SUCCESS',commented_call,'API 호출은 주석 처리되어 있고 실제 작업 없이 성공을 표시합니다.')
        if (re.search(r'로그인|인증',request) and
            re.search(r'//[^\n]*실제\s*(?:로그인|인증)[^\n]*(?:추가|필요)', body)):
            unknown.append(f"{artifact['path']}:{function['name']}: 로그인 후처리를 미룬 주석이 있으나 필요한 인증 상태 처리 방식은 확인할 수 없습니다.")
    return issues, functions, unknown


def validate_completeness(result, *, agent, user_request='', required_agents=(), project_context=None):
    required = completeness_required(agent,user_request,required_agents)
    artifacts, unknown = extract_artifacts(result,agent)
    if required and not re.search(r'구현|작성|추가|개발|만들|로그인|회원가입|implement|create|build',user_request,re.I):
        unknown.append('사용자 요청에서 구현 작업 범위를 확인하지 못했습니다.')
    production = [a for a in artifacts if a['role']=='implementation']
    reused = []
    # Explicit textual reuse may rely on a complete selected file, never on absence
    # from the bounded snapshot. Do not scan or execute the target project here.
    if required and not production and re.search(r'재사용|reuse',result,re.I):
        for item in (project_context or {}).get('selected_files',[]):
            path=item.get('path','')
            if path and (path in result or path.rsplit('/',1)[-1] in result):
                if item.get('truncated'):
                    unknown.append(f'재사용 파일 snapshot이 잘렸습니다: {path}')
                    continue
                suffix=path.rsplit('.',1)[-1]
                language={'java':'java','ts':'ts','tsx':'tsx','js':'js','jsx':'jsx'}.get(suffix)
                if language:
                    reused.append({'path':path,'language':language,'content':item.get('content',''),
                                   'start':0,'line':1,'role':'implementation','origin':'project_context'})
        production += reused
    issues=[]; checked=[]
    for artifact in production:
        if artifact['language'] not in {'java','ts','tsx','js','jsx'}:
            unknown.append(f"지원하지 않는 언어: {artifact['path']} ({artifact['language']})")
            continue
        if re.search(r"\b(?:from|import)\s*[\"'][^\"']*/(?:mocks?|fixtures?|__tests__|examples?)/",artifact['content']):
            unknown.append(f"실제 전달 파일이 Mock/Test/Example 모듈을 참조합니다. 사용 범위 확인이 필요합니다: {artifact['path']}")
        findings, functions, incomplete = _findings(artifact,user_request)
        unknown.extend(incomplete)
        checked.extend({'file':artifact['path'],'function':f['name'],'origin':artifact['origin']} for f in functions)
        for finding in findings:
            finding['target_agent']=agent
            finding['evidence']['source']=agent.title() if artifact['origin']=='generated' else 'Project Context'
        issues.extend(findings)
    if not required:
        status='NOT_APPLICABLE'; issues=[]
    elif not production or not checked or unknown:
        status='FAIL' if issues else 'NOT_VERIFIED'
    else:
        status='FAIL' if issues else 'PASS'
    reasons=list(unknown)
    if required and not production: reasons.append('실제 전달 파일 또는 명시적으로 재사용하는 완전한 snapshot을 확인하지 못했습니다.')
    if required and production and not checked: reasons.append('지원하는 block 함수 본문을 확인하지 못했습니다.')
    if status=='NOT_VERIFIED':
        issues.append({'severity':'Major','rule':'COMPLETENESS_NOT_VERIFIED','target_agent':agent,
                       'message':' '.join(reasons),'required_fix':'전달 파일과 검사 가능한 구현 근거를 명확히 제공하세요. 구현 부재를 추측하지 마세요.'})
    return {'status':status,'required':required,'scope':SCOPE,'issues':issues,
            'not_applicable_reason':None if required else 'Agent 미선택, DB 검사, 설명 또는 명시적 Mock 작업은 1차 기능 Stub 검사의 대상이 아닙니다.',
            'coverage':{'files':[{'path':a['path'],'language':a['language'],'origin':a['origin']} for a in production],
                        'functions':checked,'excluded':[{'path':a['path'],'role':a['role']} for a in artifacts if a['role']!='implementation'],
                        'rules':RULES,'reasons':reasons},
            'runtime':{'status':'NOT_VERIFIED','reason':'이 단계는 정적 Stub 검사이며 빌드·실행·기능 전체를 검증하지 않습니다.'}}


def attach_completeness(validation, result, state, agent):
    completeness=validate_completeness(result,agent=agent,user_request=state.get('user_request',''),
        required_agents=state.get('required_agents',[]),project_context=state.get('project_context'))
    status=validation.get('status','NOT_RUN')
    if completeness['required'] and completeness['status']=='FAIL': status='FAIL'
    elif completeness['required'] and completeness['status']=='NOT_VERIFIED' and status=='PASS': status='NOT_VERIFIED'
    print(f"[{agent.title()} Completeness Validator] 판정={completeness['status']}, 이슈={len(completeness['issues'])}개, 범위={SCOPE}")
    return {**validation,'status':status,'issues':[*validation.get('issues',[]),*completeness['issues']],
            'completeness':completeness}


def fix_validation_payload(validation):
    """Fix에는 Issue와 근거만 전달하고 저장용 coverage를 중복 주입하지 않는다."""
    return {key:value for key,value in validation.items() if key != 'completeness'}


def completeness_blockers(state):
    blocked={}
    for agent in ('backend','frontend'):
        if not completeness_required(agent,state.get('user_request',''),state.get('required_agents',[])):
            continue
        validation=state.get(agent+'_validation',{})
        completeness=validation.get('completeness')
        # Legacy/direct Review callers are evaluated too; missing metadata is not PASS.
        if completeness is None:
            completeness=validate_completeness(state.get(agent+'_result',''),agent=agent,
                user_request=state.get('user_request',''),required_agents=state.get('required_agents',[]),
                project_context=state.get('project_context'))
        if completeness['required'] and completeness['status'] not in {'PASS','NOT_APPLICABLE'}:
            blocked[agent]=completeness
    return blocked

"""Backend Validator Fix의 정적 안전 검사. 인증 방식이나 실행 성공을 추론하지 않는다.

제한된 Java block method/record/field 구문만 지원한다. source가 불완전하거나
변경을 설명할 수 없으면 NOT_VERIFIED로 남긴다. RAG는 계약 근거로 사용하지 않는다.
"""
import copy
import hashlib
import re

from validators.artifacts import extract_artifacts
from validators.completeness_validator import _functions
from validators.integration_validator import _extract_backend_routes, _mask_non_code


def _digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def _identity(issue):
    token = re.search(r'\bString\s+(\w+)\s*=', issue.get('evidence', {}).get('quote', ''))
    return (issue.get('rule'), issue.get('file'), issue.get('function'),
            token[1] if token and issue.get('rule') == 'FAKE_AUTH_TOKEN' else None)


def _normal(text):
    # 문자열 내부 공백/값은 보존한다.
    parts = re.split(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')',
                     _mask_non_code(text, strings=False))
    return ''.join(part if i % 2 else re.sub(r'\s+', ' ', part)
                   for i, part in enumerate(parts)).strip()


def _argument_count(text):
    code = _mask_non_code(text)
    if not code.strip():
        return 0
    depth, count = 0, 1
    for char in code:
        if char in '([{<':
            depth += 1
        elif char in ')]}>':
            depth -= 1
        elif char == ',' and depth == 0:
            count += 1
        if depth < 0:
            return None
    return count if depth == 0 else None


def _files(text):
    artifacts, unknown = extract_artifacts(text, 'backend')
    files = {}
    for artifact in artifacts:
        if artifact['role'] != 'implementation':
            continue
        path = artifact['path']
        if artifact['language'] != 'java' or path in files:
            unknown.append(f'지원하지 않는 파일 또는 중복 경로: {path}')
        else:
            files[path] = artifact
            if len(re.findall(r'\b(?:class|record|interface|enum)\s+\w+', _mask_non_code(artifact['content']))) != 1:
                unknown.append(f'파일 내부 타입 소유 관계를 확정하지 못했습니다: {path}')
    if not files:
        unknown.append('비교할 실제 Java 전달 파일이 없습니다.')
    return files, unknown


def _methods(content, unknown):
    result = {}
    for f in _functions(content, 'java', unknown):
        # 같은 이름의 overload도 parameter signature로 구분한다.
        prefix = content[:f['start'] - 1]
        signature = re.search(r'\b(?:public|private|protected)\s+[^{};]+\([^{};]*\)\s*$', _mask_non_code(prefix))
        if not signature:
            unknown.append(f"함수 signature를 확인하지 못했습니다: {f['name']}")
            continue
        key = _normal(signature.group())
        if key in result:
            unknown.append(f"클래스별 소유 관계가 불명확한 중복 method signature: {key}")
        annotation = re.search(r'(?:@\w+(?:\([^)]*\))?\s*)+$', prefix[:signature.start()])
        header_start = annotation.start() if annotation else signature.start()
        result[key] = {**f, 'body': content[f['start']:f['end']],
                       'header': content[header_start:f['start']],
                       'signature_start': header_start}
    return result


def _issue(rule, message, *, file='', function='', quote=''):
    return {'severity': 'Major', 'rule': rule, 'target_agent': 'backend',
            'file': file, 'function': function, 'message': message,
            'required_fix': '기존 정상 기능과 확정 계약을 보존하고 실제 근거로 수정 결과를 확인하세요.',
            'evidence': {'source': 'Backend Fix comparison', 'quote': quote}}


def _explicit_change(request, name):
    # 명시적으로 지목된 기능만 예외. 인접한 다른 문장의 삭제 명령을 확대 적용하지 않는다.
    if not name:
        return False
    aliases = {'signup': r'signup|회원가입', 'login': r'login|로그인'}
    term = aliases.get(name.lower(), re.escape(name))
    if (re.search(rf'(?:{term})[^.\n,;]*(?:하지\s*마|금지|보존|유지|말아|말 것|복구|되돌리|삭제\s*안)', request, re.I)
            or re.search(rf"\b(?:do\s+not|don't)\s+(?:delete|remove)\s+(?:{term})\b", request, re.I)):
        return False
    return bool(re.search(rf'(?:{term})(?:\(\))?(?:\s*(?:메서드|Endpoint|endpoint|API|기능))?\s*(?:을|를|은|는)?\s*(?:(?:삭제|제거|변경)(?:해(?:줘|주세요|라)?|하(?:세요|라|고)|할 것)?(?=\s*(?:$|[.!?,;\n]))|remove\b|delete\b)', request, re.I)
                or re.search(rf'\b(?:delete|remove)\s+(?:{term})\b', request, re.I))


def _contracts(state):
    """전체 snapshot의 실제 source만 조사한다. 미선택 source의 부재를 단정하지 않는다.

발급 구현/명시적 interface 계약과 호출 receiver type을 함께 확인한다.
단순 메서드명이나 RAG 예제의 일치는 근거로 인정하지 않는다.
"""
    confirmed, inspected, incomplete = [], [], []
    for item in state.get('project_context', {}).get('selected_files', []):
        path, text = item.get('path', ''), item.get('content', '')
        if not path.endswith('.java') or re.search(r'(?:^|/)(?:test|tests|examples?|mocks?)(?:/|$)', path, re.I):
            continue
        inspected.append(path)
        if item.get('truncated') or not text:
            incomplete.append(path)
            continue
        code = _mask_non_code(text)
        owners = list(re.finditer(r'\b(class|interface)\s+(\w+)', code))
        if len(owners) != 1:
            incomplete.append(path)
            continue
        owner = owners[0]
        # 인증 방식은 선택하지 않고 기존 Token 발급 계약만 채택한다.
        methods = _methods(text, [])
        for signature, method in methods.items():
            if not re.search(r'token', owner[2] + method['name'], re.I):
                continue
            if not re.search(r'issue|create|generate|mint', method['name'], re.I):
                continue
            if not re.search(r'\b(?:String|java\.lang\.String)\s+' + re.escape(method['name']) + r'\s*\(', signature):
                continue  # 현재 지원하는 지역 String Token 흐름과 반환 타입이 맞지 않는다.
            body = _mask_non_code(method['body'], strings=False)
            # 고정값 반환, 빈 함수, null, Stub은 발급 구현 근거로 쓰지 않는다.
            if (not body.strip() or re.search(r'NotImplemented|UnsupportedOperationException|\breturn\s+(?:null|"|\')|\bString\s+\w+\s*=\s*"', body)
                    or not re.search(r'\breturn\b.*\(', body, re.S)):
                continue
            confirmed.append({'type': owner[2], 'method': method['name'], 'file': path,
                              'parameter_count': _argument_count(signature.split('(', 1)[1].rsplit(')', 1)[0]),
                              'kind': 'implementation', 'source': text})
        if owner[1] == 'interface':
            for method in re.finditer(r'\b(?:String|java\.lang\.String)\s+((?:issue|create|generate|mint)\w*)\s*\([^;{}]*\)\s*;', code, re.I):
                if re.search(r'token', owner[2] + method[1], re.I):
                    confirmed.append({'type': owner[2], 'method': method[1], 'file': path,
                                      'parameter_count': _argument_count(method[0].split('(', 1)[1].rsplit(')', 1)[0]),
                                      'kind': 'declared_contract', 'source': text})
    return {'confirmed': confirmed, 'inspected_files': inspected, 'incomplete_files': incomplete,
            'scope': '완전한 Project Context source. 미선택 파일의 구현 존재 여부는 미확인.'}


def prepare_backend_fix(state, validation):
    """실제 Fix 전에 baseline과 계약 근거를 고정한다. 실패를 PASS로 바꾸지 않는다."""
    previous = validation.get('fix', {})
    baseline = previous.get('baseline') or {
        'result': state.get('backend_result', ''),
        'issues': copy.deepcopy(validation.get('issues', [])),
    }
    contract = _contracts(state)
    auth = [i for i in baseline['issues'] if i.get('rule') == 'FAKE_AUTH_TOKEN'
            and not _explicit_change(state.get('user_request', ''), i.get('function', ''))]
    blocked = bool(auth and not contract['confirmed'])
    return {'status': 'BLOCKED' if blocked else 'READY', 'baseline': baseline,
            'attempt_issues': copy.deepcopy(validation.get('issues', [])),
            'contract': contract, 'input_digest': _digest(state.get('backend_result', '')),
            'reason': '확인 가능한 source에서 필요한 Token 발급 구현/계약을 확인하지 못했습니다. 구현 부재를 단정하지 않습니다.' if blocked else '',
            'needed_information': ['기존 발급기 또는 인증 서비스의 실제 source/명시적 계약',
                                   'accessToken/refreshToken의 반환 계약과 의존성 연결 근거'] if blocked else []}


FIX_INSTRUCTION = """
[Backend Fix 완료 조건 / 근거 구분]
- 사용자 요구사항, 실제 Project Context source/계약, 기존 전달 코드, RAG 참고 예제를 구분하세요.
- RAG 예제는 실제 프로젝트의 확정 계약이나 사용 가능한 구현이 아닙니다.
- 고정 Token의 문자열 삭제/이름 변경, DTO 필드 삭제, 미정의 Provider 호출은 해결이 아닙니다.
- 아래 확인된 source의 발급 구현/명시적 계약에 맞게 실제 반환 흐름과 의존성을 연결하세요.
- signup() 및 /signup을 포함한 관련 없는 메서드, HTTP Method/Path, DTO 계약을 보존하세요.
- 새 JWT/Session/Security 방식을 임의로 만들지 마세요. 필수 계약이 부족하면
  첫 줄에 BACKEND_FIX_STATUS: BLOCKED를 쓰고 사유와 필요한 정보를 명시하세요.
  기존 코드를 보존하세요. 성공을 주장하지 마세요.
- 완료 조건은 Completeness 재검사와 기존 기능 보존 검사입니다. 문자열 변경만으로 완료되지 않습니다.
""".strip()


def assess_backend_fix(state, result, validation):
    pending = state.get('backend_validation', {}).get('fix', {})
    if pending.get('status') == 'BLOCKED':
        if _digest(result) == pending.get('input_digest'):
            validation['fix'] = copy.deepcopy(pending)
            return validation
    if not pending.get('baseline'):
        return validation
    fix = copy.deepcopy(pending)
    baseline = fix['baseline']
    before, unknown_before = _files(baseline['result'])
    after, unknown_after = _files(result)
    unknown = unknown_before + unknown_after
    regressions, unresolved = [], []
    targeted = {(i.get('file'), i.get('function')) for i in baseline['issues'] + fix.get('attempt_issues', [])}
    request = state.get('user_request', '')
    for path, old in before.items():
        old_methods = _methods(old['content'], unknown)
        new = after.get(path)
        if new is None:
            if not _explicit_change(request, path.rsplit('/', 1)[-1].split('.')[0]):
                regressions.append(_issue('FIX_REGRESSION', '기존 전달 파일이 삭제되었습니다.', file=path))
            continue
        new_methods = _methods(new['content'], unknown)
        old_classes = set(re.findall(r'\b(?:class|record|interface|enum)\s+(\w+)', _mask_non_code(old['content'])))
        new_classes = set(re.findall(r'\b(?:class|record|interface|enum)\s+(\w+)', _mask_non_code(new['content'])))
        for name in old_classes - new_classes:
            if not _explicit_change(request, name):
                regressions.append(_issue('FIX_REGRESSION', f'기존 클래스가 삭제/변경되었습니다: {name}', file=path))
        for signature, method in old_methods.items():
            name = method['name']
            if _explicit_change(request, name):
                continue
            if signature not in new_methods:
                regressions.append(_issue('FIX_REGRESSION', '기존 메서드 또는 signature가 삭제/변경되었습니다.', file=path, function=name, quote=signature))
            elif ((path, name) not in targeted
                  and (_normal(method['body']) != _normal(new_methods[signature]['body'])
                       or _normal(method['header']) != _normal(new_methods[signature]['header']))):
                regressions.append(_issue('FIX_REGRESSION', '수정 대상 외 메서드 본문이 변경되었습니다.', file=path, function=name, quote=method['body']))
            elif _normal(method['header']) != _normal(new_methods[signature]['header']):
                unknown.append(f'{path}:{name}: 수정 대상 함수 annotation 변경의 안전성 미확인')
        # 함수 본문을 제거한 클래스/필드/DTO/record/annotation 선언을 비교한다.
        def declarations(text, methods):
            for method in sorted(methods.values(), key=lambda m:m['start'], reverse=True):
                text = text[:method['signature_start']] + text[method['end']+1:]
            return [line.strip() for line in _normal(text).split(';')
                    if line.strip() and not re.fullmatch(r'(?:package|import)\b.*', line.strip())]
        def fields(text, methods):
            for method in sorted(methods.values(), key=lambda m:m['start'], reverse=True):
                text = text[:method['signature_start']] + text[method['end']+1:]
            code = _mask_non_code(text)
            declared = {(m[2], _normal(m[1])) for m in re.finditer(
                r'\b(?:public|private|protected)\s+(?:(?:static|final|volatile|transient)\s+)*([\w.<>,?\[\] ]+?)\s+(\w+)\s*(?:=[^;]*)?;', code)}
            for record in re.finditer(r'\brecord\s+\w+\s*\(([^()]*)\)', code):
                for component in record[1].split(','):
                    match = re.fullmatch(r'\s*([\w.\[\]]+)\s+(\w+)\s*', component)
                    if match:
                        declared.add((match[2], match[1]))
                    elif component.strip():
                        unknown.append(f'{path}: 지원하지 않는 record component 구문')
            return declared
        for name, field_type in fields(old['content'], old_methods) - fields(new['content'], new_methods):
            if not _explicit_change(request, name):
                regressions.append(_issue('FIX_REGRESSION', f'기존 필드/DTO 계약 삭제 또는 타입 변경: {field_type} {name}', file=path))
        if declarations(old['content'], old_methods) != declarations(new['content'], new_methods):
            unknown.append(f'{path}: 클래스/필드/DTO/annotation 등 함수 외 변경의 안전성 미확인')
        old_routes = _extract_backend_routes('```java\n' + old['content'] + '\n```', unknown)
        new_routes = _extract_backend_routes('```java\n' + new['content'] + '\n```', unknown)
        for route in old_routes:
            if not any(r['method'] == route['method'] and r['path'] == route['path'] for r in new_routes):
                if not any(_explicit_change(request, m['name']) and m['name'].lower() in route['path'].lower() for m in old_methods.values()):
                    regressions.append(_issue('FIX_REGRESSION', f"Endpoint 계약 삭제/변경: {route['method']} {route['path']}", file=path))

    if after.keys() - before.keys():
        unknown.append('새 파일 추가의 계약 적합성 미확인: ' + ', '.join(sorted(after.keys() - before.keys())))

    # 원래 fake token의 반환값이 확인된 프로젝트 발급 계약으로 연결됐는지 별도 확인.
    # 지원하지 않는 데이터 흐름은 성공으로 간주하지 않는다.
    for issue in baseline['issues']:
        if issue.get('rule') != 'FAKE_AUTH_TOKEN':
            continue
        if _explicit_change(request, issue.get('function', '')):
            continue
        artifact = after.get(issue.get('file'))
        token = re.search(r'\bString\s+(\w+)\s*=', issue.get('evidence', {}).get('quote', ''))
        accepted = False
        if artifact and token:
            text = artifact['content']
            methods = _methods(text, unknown)
            members = text
            for item in sorted(methods.values(), key=lambda m:m['start'], reverse=True):
                members = members[:item['signature_start']] + members[item['end']+1:]
            for method in methods.values():
                if method['name'] != issue.get('function'):
                    continue
                body = _mask_non_code(method['body'])
                for contract in fix['contract']['confirmed']:
                    kind = re.search(r'access|refresh', token[1], re.I)
                    other_kind = re.search(r'access|refresh', contract['method'], re.I)
                    if kind and other_kind and kind[0].lower() != other_kind[0].lower():
                        continue
                    receiver_type = r'\b' + re.escape(contract['type']) + r'\s+(\w+)'
                    receivers = re.findall(receiver_type + r'(?=\s*[;=])', _mask_non_code(members))
                    receivers += re.findall(receiver_type + r'(?=\s*[;=,)])', _mask_non_code(method['header'] + method['body']))
                    for receiver in receivers:
                        assignment = re.search(r'\bString\s+' + re.escape(token[1]) + r'\s*=\s*' + re.escape(receiver) + r'\.' + re.escape(contract['method']) + r'\(([^;]*)\)\s*;', body)
                        if assignment and contract['parameter_count'] is not None and _argument_count(assignment[1]) == contract['parameter_count']:
                            tail = body[assignment.end():]
                            # 재할당/문자열 위장 및 응답에서의 제거를 허용하지 않는다.
                            accepted |= bool(re.search(r'\breturn\s+new\s+\w+\s*\([^;]*\b' + re.escape(token[1]) + r'\b[^;]*\)\s*;', tail)
                                             and not re.search(r'\b' + re.escape(token[1]) + r'\s*=', tail))
        if not accepted:
            retained = copy.deepcopy(issue)
            retained['evidence']['source'] = 'Backend Fix baseline'
            retained['evidence_scope'] = 'original_defect_unresolved'
            unresolved.append(retained)
    existing_keys = {_identity(i) for i in validation.get('issues', [])}
    baseline_keys = {_identity(i) for i in baseline['issues']}
    remaining = existing_keys & baseline_keys
    resolved = baseline_keys - existing_keys - {_identity(i) for i in unresolved}
    if unresolved or remaining:
        status = 'NO_PROGRESS'
    elif regressions:
        status = 'REGRESSION'
    elif unknown or validation['status'] == 'NOT_VERIFIED':
        status = 'NOT_VERIFIED'
    elif validation['status'] == 'FAIL':
        status = 'PROGRESS'
    else:
        status = 'SUCCEEDED'
    fix.update(status=status,
               output_digest=_digest(result), regressions=regressions,
               resolved_issues=[dict(rule=k[0], file=k[1], function=k[2], token=k[3]) for k in sorted(resolved, key=str)],
               remaining_issues=[i for i in validation.get('issues', []) if _identity(i) in baseline_keys] + [i for i in unresolved if _identity(i) not in existing_keys],
               new_issues=[i for i in validation.get('issues', []) if _identity(i) not in baseline_keys],
               preservation={'status': 'FAIL' if regressions else 'NOT_VERIFIED' if unknown else 'PASS', 'reasons': list(dict.fromkeys(unknown))})
    if unresolved:
        # 이름 변경/DTO 제거/미정의 위임으로 정적 regex를 빠져나가도 원래 결함을 유지한다.
        comp = validation.get('completeness', {})
        comp['status'] = 'FAIL'
        comp_keys = {_identity(i) for i in comp.get('issues', [])}
        comp.setdefault('issues', []).extend(i for i in unresolved if _identity(i) not in comp_keys)
        validation['completeness'] = comp
    additions = [i for i in unresolved if _identity(i) not in existing_keys] + regressions
    if unknown:
        additions.append(_issue('BACKEND_FIX_NOT_VERIFIED', ' '.join(dict.fromkeys(unknown))))
    validation['issues'].extend(i for i in additions if i not in validation['issues'])
    if unresolved or regressions:
        validation['status'] = 'FAIL'
    elif unknown and validation['status'] == 'PASS':
        validation['status'] = 'NOT_VERIFIED'
    validation['fix'] = fix
    return validation


def backend_fix_blocker(state):
    if 'backend' not in state.get('required_agents', []):
        return None
    validation = state.get('backend_validation', {})
    fix = validation.get('fix', {})
    if fix and (validation.get('status') != 'PASS' or fix.get('status') != 'SUCCEEDED' or fix.get('output_digest') != _digest(state.get('backend_result', ''))):
        return {'status': 'FAIL', 'issues': validation.get('issues') or [_issue('BACKEND_FIX_NOT_VERIFIED', 'Backend Fix 완료 근거가 부족합니다.')],
                'fix': {k: v for k, v in fix.items() if k not in {'baseline', 'contract'}}}
    return None


def backend_fix_report(validation):
    """Review/Final에는 저장용 원본 코드와 발급기 source를 중복 주입하지 않는다."""
    fix = validation.get('fix', {})
    summary = {k: v for k, v in fix.items() if k not in {'baseline', 'contract', 'attempt_issues'}}
    if fix:
        contract = fix.get('contract', {})
        summary['contract'] = {**contract, 'confirmed': [
            {k: v for k, v in c.items() if k != 'source'} for c in contract.get('confirmed', [])
        ]}
    return {**validation, 'fix': summary} if fix else validation


def backend_contract_prompt(fix):
    contract = fix['contract']
    sources = {c['file']: c['source'] for c in contract['confirmed']}
    return {**contract, 'confirmed': [
        {k: v for k, v in c.items() if k != 'source'} for c in contract['confirmed']
    ], 'sources': sources}

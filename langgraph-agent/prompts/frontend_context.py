"""Frontend 전용 Prompt projection. 실제 코드와 공통 규칙은 축약하지 않는다."""
import json
import re

from validators.artifacts import _markdown_sections, _fenced_code_blocks

MODES = {'initial', 'validator_fix', 'integration_fix'}


def project_templates(text, titles):
    sections = _markdown_sections(text)
    if sections is None:
        return text
    for section in sorted(sections, key=lambda s: s['start'], reverse=True):
        if section['title'] not in titles:
            continue
        body = text[section['start']:section['end']]
        # 허용된 비대상 템플릿 외 새 규칙이 추가되면 원문을 유지한다.
        templates = re.findall(r'```md\n(.*?)\n```', body, re.S)
        outside = re.sub(r'```md\n.*?\n```', '', body, flags=re.S)
        outside = '\n'.join(outside.splitlines()[1:]).replace('---', '').strip()
        if outside not in {'', '설계 요청에서는 다음 구조 설명 형식을 사용할 수 있다.'}:
            continue
        if not templates or any(line.strip() and not line.lstrip().startswith('#')
                                for t in templates for line in t.splitlines()):
            continue
        text = text[:section['start']] + text[section['end']:]
    return text


def project_frontend_rules(system, rules, mode):
    if mode not in MODES:
        return system, rules
    system = project_templates(system, {'7.2 Design Request', '8. Handoff to Review Agent'})
    rules = project_templates(rules, {'8.2 Design Request', '10. Handoff to Review Agent'})
    # 실행 파일 출력 예시는 System에 같은 내용이 있을 때만 Rules에서 중복 제거한다.
    pattern = r'```md\n# Frontend Implementation\n.*?\n## Verification Notes\n```'
    examples = re.findall(pattern, rules, re.S)
    if len(examples) == 1 and examples[0] in system:
        rules = rules.replace(examples[0], '', 1)
    return system, rules


LEGACY_FIX_RULES = '''[Frontend Validator Fix Mode 수정 규칙]

- Validator의 required_fix를 실제 관련 코드에 반영하세요.
- Issue 해결에 필요한 최소 파일과 코드만 수정하세요.
- 정상인 UI 구조를 유지하세요.
- 기존 상태 관리와 이벤트 처리를 유지하세요.
- 기존 Loading/Error 처리와 API 연결을 유지하세요.
- 정상 CSS를 유지하세요.
- 새로운 기능이나 구조를 임의로 추가하지 마세요.
- 수정 조각만 출력하지 말고 수정된 전체 Frontend 결과를 다시 출력하세요.

수정된 전체 Frontend 결과만 출력하세요.'''


def project_previous_frontend(result, backend_contract):
    """과거 응답에 복사된 참고 tail만 분리한다. 불명확하면 전체 원문 유지."""
    marker = '[현재 Backend 관련 API 계약]'
    start = result.rfind(marker)
    blocks = _fenced_code_blocks(result)
    if start < 0 or blocks is None or any(b['start'] <= start < b['end'] for b in blocks):
        return result
    tail = result[start + len(marker):].strip()
    prefix = backend_contract.strip()
    if not prefix or not tail.startswith(prefix):
        return result
    tail = tail[len(prefix):].strip()
    issue_marker = '[반드시 해결할 Frontend Validator Issues]'
    if not tail.startswith(issue_marker):
        return result
    try:
        payload, end = json.JSONDecoder().raw_decode(tail[len(issue_marker):].lstrip())
    except (ValueError, TypeError):
        return result
    remaining = tail[len(issue_marker):].lstrip()[end:].strip()
    if (not isinstance(payload, dict) or payload.get('status') != 'FAIL'
            or not isinstance(payload.get('issues'), list) or remaining != LEGACY_FIX_RULES):
        return result
    # 참고 tail에 실제 Frontend 코드가 있으면 제거하지 않는다.
    if any(b['language'] in {'ts', 'typescript', 'tsx', 'js', 'javascript', 'jsx', 'css'}
           for b in blocks if b['start'] >= start):
        return result
    return result[:start].rstrip()


FIX_OUTPUT_RULES = '''[Frontend Fix 출력 계약]
- # Frontend Implementation 아래 ## Files, ## API Clarification, ## Verification Notes만 출력하세요.
- 기존 전달 파일은 정상 코드·import/export·CSS·API 호출을 보존한 전체 파일로 출력하세요. diff나 부분 파일은 금지합니다.
- Issue에 필요한 기존 타입/의존성 보완 외 무관한 신규 파일은 추가하지 마세요.
- 아래 Backend 계약·Handoff, Issue JSON, Fix 지침과 RAG 원문은 입력 참고 자료입니다. 응답에 복사하지 마세요.
- 필수 계약 설명과 미해결 사항만 짧게 기록하세요.'''

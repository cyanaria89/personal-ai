"""PM 출력만 검사한다. 입력 코드·기술명은 검사 대상이 아니며 의미 전체를 증명하지 않는다."""
import re


AGENTS = ("db", "backend", "frontend")
HEADER = re.compile(r"^\s*(REQUIRED_AGENTS|REQUEST_SUMMARY|EXECUTION_ORDER|[A-Z][A-Z0-9_]*_HANDOFF):[ \t]*(.*)$", re.M | re.I)
PLACEHOLDER = re.compile(r"^(?:none|없음|n/?a|\.{3}|…|todo|tbd|미정|<[^>]*>)$", re.I)


def _has_content(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = [line.strip().lstrip("-* ").strip().strip("`") for line in text.splitlines()
             if line.strip() and not line.strip().startswith("```")]
    return any(line and not PLACEHOLDER.fullmatch(line) for line in lines)


def _implementation_evidence(text):
    # 인라인 계약·기술 참조와 자연어 작업 지시는 실행 구현으로 분류하지 않는다.
    # 실제 SQL 문장 / Java 타입·import / JS 함수·JSX 같은 명확한 구문만 검사한다.
    lines = []
    implementation_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            implementation_fence = bool(re.match(r"```(?:sql|postgresql|java|javascript|typescript|js|ts|tsx|jsx|html)\s*$",line.strip(),re.I))
        if not implementation_fence:
            line = re.sub(r"(?<!`)`[^`\n]+`(?!`)", "INLINE_REFERENCE", line)
            if re.search(r"(?:작성|구현|검증|연동|설계|유지|보존|사용)(?:하세요|한다|해줘|할 것|한다\.|하라)?[.!。]?\s*$", line):
                continue
        lines.append(line)
    code = "\n".join(lines)
    patterns = (
        ("SQL", r"\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[\w.\"`]+\s*\("),
        ("SQL", r"\bSELECT\s+(?:DISTINCT\s+)?[\w.*\",\s]+\s+FROM\s+[\w.\"`]+"),
        ("SQL", r"\bINSERT\s+INTO\s+[\w.\"`]+[\s\S]*?\bVALUES\s*\("),
        ("SQL", r"\b(?:CREATE\s+(?:UNIQUE\s+)?INDEX\s+\w+\s+ON\s+\w+\s*\(|DROP\s+TABLE\s+\w+\s*;|SELECT\s+\d+\s*;)"),
        ("SQL", r"\b(?:ALTER\s+TABLE\s+\w+\s+(?:ADD|DROP|ALTER)|UPDATE\s+\w+\s+SET\s+\w+\s*=|DELETE\s+FROM\s+\w+\s*(?:WHERE|;))"),
        ("Java", r"\b(?:public\s+)?(?:class|interface|record)\s+\w+(?:\s*\([^)]*\))?[^;\n{}]*\{"),
        ("Java", r"(?m)^\s*(?:package\s+[\w.]+|import\s+(?:static\s+)?[\w.*]+)\s*;"),
        ("Java", r"\b(?:public|private|protected)\s+(?:static\s+)?[\w<>\[\]]+\s+\w+\s*\([^)]*\)\s*\{"),
        ("JavaScript/React", r"\b(?:async\s+)?function\s+\w+\s*\([^)]*\)\s*(?::[^\n{]+)?\{"),
        ("JavaScript/React", r"\b(?:const|let)\s+\w+\s*=\s*(?:async\s*)?(?:\([^)]*\)|\w+)\s*=>"),
        ("React/HTML", r"(?:^|\n|\breturn\s*\(?)\s*<(?:div|form|input|button|main|section)\b[^>]*>"),
    )
    findings = []
    for language, pattern in patterns:
        match = re.search(pattern, code, re.I)
        if match:
            findings.append({"language": language, "quote": match.group(0).strip()[:240]})
    return findings


def validate_pm_output(result, *, done_reason=None):
    """출력 계약·명백한 구현·잘림을 검사하고 선택 정보는 진단용으로 보존한다."""
    issues = []

    def issue(rule, message):
        issues.append({"severity": "Major", "rule": rule, "message": message,
                       "required_fix": f"PM 출력 계약을 충족하는 완전한 계획을 제공하세요: {rule}"})

    # 과거 정상 산출물의 닫힌 text fence는 표현용 외피로만 정규화한다.
    text = result.strip()
    lines = text.splitlines()
    wrapped = (len(lines) >= 3 and lines[0].strip() in {"```text", "```"}
               and lines[-1].strip() == "```"
               and not any(line.strip().startswith("```") for line in lines[1:-1]))
    if wrapped:
        text = "\n".join(lines[1:-1]).strip()
    headers = list(HEADER.finditer(text))
    sections = {}
    for index, match in enumerate(headers):
        name = match[1].upper()
        end = headers[index+1].start() if index+1 < len(headers) else len(text)
        body = (match[2] + "\n" + text[match.end():end]).strip()
        sections.setdefault(name, []).append(body)
    declarations = [m[2].strip() for m in headers if m[1].upper() == "REQUIRED_AGENTS"]
    declared = [part.strip().lower() for part in declarations[0].split(",")] if declarations else []
    selected = [agent for agent in declared if agent in AGENTS]
    valid_selection = bool(declared) and (
        declared == ["none"] or (all(a in AGENTS for a in declared) and len(set(declared)) == len(declared))
    )
    first_line = text.splitlines()[0] if text else ""
    if not re.fullmatch(r"REQUIRED_AGENTS:[ \t]*[^\n]+", first_line) or len(declarations) != 1:
        issue("PM_REQUIRED_AGENTS_FORMAT", "첫 줄에 유일한 REQUIRED_AGENTS 선언이 필요합니다.")
    if not valid_selection:
        issue("PM_INVALID_AGENT_SELECTION", "허용 값 db/backend/frontend 또는 단독 none만 사용할 수 있습니다.")

    for name in ("REQUEST_SUMMARY", "EXECUTION_ORDER"):
        values = sections.get(name, [])
        if len(values) != 1 or not _has_content(values[0]):
            issue("PM_MISSING_" + name, f"필수 {name}의 유일하고 비어 있지 않은 내용이 필요합니다.")
    if len(sections.get("EXECUTION_ORDER", [])) == 1 and valid_selection:
        order = sections["EXECUTION_ORDER"][0].strip().strip("`")
        actual = [a.strip().lower() for a in re.split(r"\s*(?:->|→)\s*", order)]
        expected = [a for a in AGENTS if a in selected] + ["review"]
        if actual != expected:
            issue("PM_INVALID_EXECUTION_ORDER", f"선택된 Agent의 기존 Graph 순서와 review가 필요합니다: {' -> '.join(expected)}")

    for agent in selected:
        values = sections.get(agent.upper() + "_HANDOFF", [])
        if len(values) != 1 or not _has_content(values[0]):
            issue("PM_MISSING_HANDOFF", f"선택된 {agent}의 비어 있지 않은 Handoff가 필요합니다.")
    for name in sections:
        if name.endswith("_HANDOFF") and name[:-8].lower() not in selected:
            issue("PM_UNSELECTED_HANDOFF", f"선택되지 않은 Agent의 Handoff가 있습니다: {name}")

    evidence = _implementation_evidence(result)
    if evidence:
        issue("PM_IMPLEMENTATION_CODE", "PM이 전문 구현 코드를 직접 출력했습니다.")
    if done_reason in {"length", "max_tokens", "max_output_tokens"}:
        issue("PM_TRUNCATED_OUTPUT", f"PM 출력이 제한으로 종료됐습니다: {done_reason}")
    return {
        "status": "FAIL" if issues else "PASS", "issues": issues,
        "required_agents": selected, "declared_agents": declared,
        "selection_status": "INVALID" if not valid_selection or len(declarations) != 1 else (
            "NONE" if declared == ["none"] else "SELECTED"
        ),
        "done_reason": done_reason, "implementation_evidence": evidence,
        "outer_text_fence_normalized": wrapped,
        "scope": "PM 응답 텍스트의 형식·Handoff 존재·명백한 구현 구문·종료 metadata. 의미 전체의 검증은 아님.",
    }

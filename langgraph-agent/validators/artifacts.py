"""Markdown 산출물 식별. 원문 offset을 유지하고 설명/테스트 코드를 구분한다."""
import re


def _markdown_sections(markdown: str) -> list[dict] | None:
    """fenced code를 제외한 Markdown heading의 안전한 섹션 범위를 구한다."""

    lines = markdown.splitlines(keepends=True)
    headings = []
    offset = 0
    fence_marker = None

    for line in lines:
        stripped = line.lstrip()
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence_match:
            marker = fence_match.group(1)
            if fence_marker is None:
                fence_marker = marker[0]
            elif marker[0] == fence_marker:
                fence_marker = None
            offset += len(line)
            continue

        if fence_marker is None:
            heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line.rstrip("\n"))
            if heading_match:
                headings.append({
                    "level": len(heading_match.group(1)),
                    "title": heading_match.group(2).strip(),
                    "start": offset,
                })
        offset += len(line)

    if fence_marker is not None:
        return None

    for index, heading in enumerate(headings):
        heading["end"] = len(markdown)
        for next_heading in headings[index + 1:]:
            if next_heading["level"] <= heading["level"]:
                heading["end"] = next_heading["start"]
                break

    return headings



def _fenced_code_blocks(markdown: str) -> list[dict] | None:
    """Markdown fenced code block의 언어와 원문 범위를 안전하게 구한다."""

    lines = markdown.splitlines(keepends=True)
    blocks = []
    opening = None
    offset = 0

    for line in lines:
        if opening is None:
            match = re.match(
                r"^\s*(?P<fence>`{3,}|~{3,})(?P<language>[\w+-]*)\s*$",
                line.rstrip("\r\n"),
            )
            if match:
                opening = {
                    "marker": match.group("fence")[0],
                    "length": len(match.group("fence")),
                    "language": match.group("language").lower(),
                    "start": offset,
                }
        else:
            closing = re.match(
                rf"^\s*{re.escape(opening['marker'])}"
                rf"{{{opening['length']},}}\s*$",
                line.rstrip("\r\n"),
            )
            if closing:
                blocks.append({
                    "language": opening["language"],
                    "start": opening["start"],
                    "end": offset + len(line),
                })
                opening = None
        offset += len(line)

    if opening is not None:
        return None

    return blocks



LANGUAGES = {'typescript':'ts', 'javascript':'js', 'ts':'ts', 'tsx':'tsx',
             'js':'js', 'jsx':'jsx', 'java':'java', 'css':'css', 'sql':'sql'}


def extract_artifacts(markdown, agent):
    blocks, sections = _fenced_code_blocks(markdown), _markdown_sections(markdown)
    if blocks is None or sections is None:
        return [], ['닫히지 않은 Markdown fence가 있습니다.']
    artifacts, unknown = [], []
    for block in blocks:
        parents = [s for s in sections if s['start'] < block['start'] < s['end']]
        parents.sort(key=lambda s:s['level'])
        title = parents[-1]['title'].strip('` ') if parents else ''
        filename = re.fullmatch(r'[^\n`]+\.[A-Za-z][A-Za-z0-9]*', title, re.I)
        context_section = re.search(r'\[(?:현재 Backend|Backend Agent|Domain RAG)', markdown[:block['start']].split('\n\n')[-1], re.I)
        example = any(re.search(r'\b(?:example|examples|sample|samples)\b|설명용|예제', s['title'], re.I) for s in parents)
        implementation = any(re.fullmatch(r'(?:Files|Implementation)', s['title'], re.I) for s in parents)
        language = LANGUAGES.get(block['language'], block['language'])
        # Backend's existing format also permits a Java class under a layer heading.
        layer = agent == 'backend' and language == 'java' and any(s['title'].lower() in {'entity','repository','dto','service','controller','config'} for s in parents)
        if not filename and not layer:
            continue
        content_start = markdown.find('\n', block['start']) + 1
        closing = markdown.rfind('\n', block['start'], block['end'] - 1)
        content = markdown[content_start:closing].rstrip('\r\n')
        path = title if filename else title + '.java'
        if layer and not filename:
            declarations = re.findall(r'\b(?:class|record|interface|enum)\s+(\w+)',content)
            if len(declarations) != 1:
                unknown.append(f'파일명을 확정할 수 없는 Backend 코드: {title}')
                continue
            path = declarations[0] + '.java'
        role = 'example' if example else 'implementation'
        if re.search(r'(?:^|/)(?:__tests__|tests?|fixtures?|mocks?|examples?)(?:/|$)|(?:Test|Tests|Spec)\.(?:java|[jt]sx?)$', path, re.I):
            role = 'test_or_mock'
        if not implementation and not layer and role == 'implementation':
            unknown.append(f'산출물 영역을 확정할 수 없습니다: {path}')
            continue
        if context_section:
            continue
        artifacts.append({'path':path, 'language':language, 'content':content,
                          'start':content_start, 'line':markdown.count('\n',0,content_start)+1,
                          'role':role, 'origin':'generated', 'path_inferred':not bool(filename)})
    return artifacts, unknown

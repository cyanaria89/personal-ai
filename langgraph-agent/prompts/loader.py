from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

SYSTEM_PROMPT_DIR = (
    PROJECT_ROOT
    / "prompts"
    / "system"
    / "source"
)

AGENT_RULES_DIR = (
    PROJECT_ROOT
    / "prompts"
    / "agent"
    / "source"
)

MASTER_DIR = (
    PROJECT_ROOT
    / "data"
    / "master"
    / "source"
)


AGENT_FILE_MAP = {
    "pm": {
        "system": "01_PM_Agent_System_Prompt.md",
        "rules": "01_PM_Agent_Rules.md",
    },
    "db": {
        "system": "02_DB_Agent_System_Prompt.md",
        "rules": "02_DB_Agent_Rules.md",
    },
    "backend": {
        "system": "03_Backend_Agent_System_Prompt.md",
        "rules": "03_Backend_Agent_Rules.md",
    },
    "frontend": {
        "system": "04_Frontend_Agent_System_Prompt.md",
        "rules": "04_Frontend_Agent_Rules.md",
    },
    "review": {
        "system": "05_Review_Agent_System_Prompt.md",
        "rules": "05_Review_Agent_Rules.md",
    },
}


def read_markdown(path: Path) -> str:
    """Markdown 파일을 UTF-8로 읽는다."""

    if not path.exists():
        raise FileNotFoundError(
            f"필수 문서를 찾을 수 없습니다: {path}"
        )

    if not path.is_file():
        raise ValueError(
            f"파일 경로가 아닙니다: {path}"
        )

    content = path.read_text(
        encoding="utf-8"
    ).strip()

    if not content:
        raise ValueError(
            f"문서 내용이 비어 있습니다: {path}"
        )

    return content


def load_agent_prompt(agent_name: str, *, mode: str | None = None) -> str:
    """
    공통 System Rules, Agent 전용 System Rules,
    공통 Agent Rules, Agent 전용 Rules를 결합한다.
    """

    agent_key = agent_name.lower().strip()

    if agent_key not in AGENT_FILE_MAP:
        raise ValueError(
            f"지원하지 않는 Agent 이름입니다: {agent_name}"
        )

    file_map = AGENT_FILE_MAP[agent_key]

    common_system = read_markdown(
        SYSTEM_PROMPT_DIR
        / "00_Common_System_Prompt.md"
    )

    agent_system = read_markdown(
        SYSTEM_PROMPT_DIR
        / file_map["system"]
    )

    common_rules = read_markdown(
        AGENT_RULES_DIR
        / "00_Common_Agent_Rules.md"
    )

    agent_rules = read_markdown(
        AGENT_RULES_DIR
        / file_map["rules"]
    )

    if agent_key == 'frontend' and mode is not None:
        from prompts.frontend_context import project_frontend_rules
        agent_system, agent_rules = project_frontend_rules(agent_system, agent_rules, mode)

    return "\n\n".join(
        [
            "# 공통 시스템 규칙",
            common_system,
            "# Agent 전용 시스템 규칙",
            agent_system,
            "# 공통 Agent 규칙",
            common_rules,
            "# Agent 전용 규칙",
            agent_rules,
        ]
    )


def load_master_context() -> str:
    """
    첫 구현에서는 Master Rules와 Project Progress만 읽는다.
    """

    master_rules = read_markdown(
        MASTER_DIR
        / "Master_RAG_Rules.md"
    )

    project_progress = read_markdown(
        MASTER_DIR
        / "Project_Progress.md"
    )

    return "\n\n".join(
        [
            "# Master RAG Rules",
            master_rules,
            "# Project Progress",
            project_progress,
        ]
    )

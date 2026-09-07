import argparse
import json
from datetime import datetime
from pathlib import Path

from graph.workflow import create_workflow
from state import AgentState


def save_result(
    content: str,
    run_timestamp: datetime | None = None,
) -> Path:
    output_directory = Path("outputs")
    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = (run_timestamp or datetime.now()).strftime(
        "%Y%m%d_%H%M%S"
    )

    output_path = (
        output_directory
        / f"agent_result_{timestamp}.md"
    )

    output_path.write_text(
        content,
        encoding="utf-8",
    )

    return output_path


def save_llm_metrics(
    metrics: list[dict],
    run_timestamp: datetime | None = None,
) -> Path:
    """LLM 호출 계측값만 별도 JSON 파일로 저장한다."""

    metrics_directory = Path("outputs") / "metrics"
    metrics_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = run_timestamp or datetime.now().astimezone()
    output_path = (
        metrics_directory
        / f"agent_metrics_{timestamp.strftime('%Y%m%d_%H%M%S_%f')}.json"
    )
    payload = {
        "schema_version": 1,
        "created_at": timestamp.isoformat(),
        "call_count": len(metrics),
        "calls": metrics,
    }
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return output_path


def read_multiline_request() -> str:
    print("\n개발 요청을 입력하세요.")
    print("입력을 마치려면 마지막 줄에 END를 입력하세요.")

    lines: list[str] = []

    while True:
        line = input("> " if not lines else "")

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines).strip()


def parse_arguments(
    argv: list[str] | None = None,
) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Personal AI LangGraph Agent",
    )
    parser.add_argument(
        "--project-root",
        default="",
        help=(
            "AI가 개발할 대상 프로젝트 디렉터리. "
            "생략하면 디스크를 자동 선택하지 않고 빈 프로젝트로 실행합니다."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_arguments(argv)
    print("=" * 60)
    print("Personal AI LangGraph Agent")
    print("=" * 60)

    user_request = read_multiline_request()

    if not user_request:
        print("요청 내용이 비어 있습니다.")
        return

    workflow = create_workflow()

    initial_state: AgentState = {
        "user_request": user_request,
        "project_root": args.project_root,
        "project_context": {
            "schema_version": 1,
            "status": "NOT_LOADED",
            "root": "",
            "detected_stack": [],
            "tree_summary": [],
            "selected_files": [],
            "warnings": [],
            "stats": {
                "scanned_file_count": 0,
                "eligible_file_count": 0,
                "selected_file_count": 0,
                "selected_char_count": 0,
                "excluded_count": 0,
                "truncated_file_count": 0,
            },
        },
        "llm_metrics": [],
        "required_agents": [],
        "project_plan": "",
        "db_result": "",
        "db_validation": {
            "status": "NOT_RUN",
            "issues": [],
        },
        "db_fix_count": 0,
        "backend_result": "",
        "backend_validation": {
            "status": "NOT_RUN",
            "issues": [],
        },
        "backend_fix_count": 0,
        "frontend_result": "",
        "frontend_validation": {
            "status": "NOT_RUN",
            "issues": [],
        },
        "frontend_fix_count": 0,
        "integration_validation": {
            "status": "NOT_RUN",
            "issues": [],
        },
        "integration_fix_count": 0,
        "review_result": "",
        "review_status": "",
        "review_count": 0,
        "final_result": "",
    }

    try:
        result = workflow.invoke(initial_state)
    except Exception as error:
        print("\nAgent 실행 중 오류가 발생했습니다.")
        print(f"오류 유형: {type(error).__name__}")
        print(f"오류 내용: {error}")
        return

    final_result = result["final_result"]

    print("\n" + "=" * 60)
    print(final_result)
    print("=" * 60)

    run_timestamp = datetime.now().astimezone()
    output_path = save_result(final_result, run_timestamp)
    metrics_path = save_llm_metrics(
        result.get("llm_metrics", []),
        run_timestamp,
    )

    print(f"\n결과 저장 위치: {output_path}")
    print(f"[LLM Metrics 저장] {metrics_path}")


if __name__ == "__main__":
    main()

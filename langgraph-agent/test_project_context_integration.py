from pm_test_support import valid_pm_plan
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import create_workflow
from main import parse_arguments
from project_context.loader import load_project_context


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def full_state(context: dict) -> dict:
    return {
        "user_request": "로그인 기능 추가해줘",
        "project_root": context["root"],
        "project_context": context,
        "llm_metrics": [],
        "required_agents": ["db", "backend", "frontend"],
        "project_plan": "KEEP_PM_PLAN",
        "db_result": "KEEP_DB_RESULT",
        "db_validation": {"status": "PASS", "issues": []},
        "db_fix_count": 0,
        "backend_result": "KEEP_BACKEND_RESULT",
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": "KEEP_FRONTEND_RESULT",
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "NOT_RUN", "issues": []},
        "integration_fix_count": 0,
        "review_result": "",
        "review_status": "",
        "review_count": 0,
        "final_result": "",
    }


class ProjectContextIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        files = {
            "src/main/java/app/member/Member.java": "@Entity class Member {}",
            "src/main/java/app/member/MemberRepository.java": "interface MemberRepository {}",
            "src/main/java/app/member/MemberService.java": "@Service class MemberService {}",
            "src/main/java/app/member/MemberController.java": "@PostMapping(\"/api/signup\") class MemberController {}",
            "src/main/java/app/member/SignupRequest.java": "record SignupRequest(String email) {}",
            "src/main/java/app/config/SecurityConfig.java": "class SecurityConfig {}",
            "src/pages/SignupPage.tsx": "export function SignupPage() { return <form />; }",
            "src/api/authApi.ts": "export const signup = () => fetch('/api/signup');",
            "src/unrelated/WeatherService.java": "class WeatherService {}",
        }
        for name, content in files.items():
            write(self.root / name, content)
        self.context = load_project_context(str(self.root), "로그인 기능 추가해줘")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def capture_agent_prompt(self, function, state: dict, *, rag: bool = False) -> str:
        captured = {}

        def fake_invoke(*args, **kwargs):
            del kwargs
            captured["prompt"] = args[2]
            if function is nodes.review_agent:
                return json.dumps({"status": "PASS", "summary": "ok", "issues": [], "rag_update_candidates": []})
            if function is nodes.pm_agent:
                return valid_pm_plan('backend')
            return "RESULT"

        patches = [patch.object(nodes, "invoke_agent", side_effect=fake_invoke)]
        if rag:
            patches.extend([
                patch.object(nodes, "search_db_context", return_value=[]),
                patch.object(nodes, "format_db_context", return_value="GENERAL_DB_GUIDANCE"),
            ])
        with patches[0]:
            if rag:
                with patches[1], patches[2]:
                    function(state)
            else:
                function(state)
        return captured["prompt"]

    def test_cli_default_does_not_select_working_directory(self) -> None:
        self.assertEqual(parse_arguments([]).project_root, "")
        self.assertEqual(parse_arguments(["--project-root", str(self.root)]).project_root, str(self.root))

    def test_graph_starts_with_project_context_then_pm(self) -> None:
        graph = create_workflow().get_graph()
        edges = {(edge.source, edge.target) for edge in graph.edges}
        self.assertIn(("__start__", "project_context"), edges)
        self.assertIn(("project_context", "pm"), edges)
        self.assertNotIn(("__start__", "pm"), edges)
        self.assertTrue(any(source == "pm" and target == "backend" for source, target in edges))

    def test_context_node_empty_invalid_and_single_load(self) -> None:
        empty = nodes.project_context_node({"project_root": "", "user_request": "회원가입"})
        self.assertEqual(empty["project_context"]["status"], "EMPTY")
        with self.assertRaisesRegex(ValueError, "대상 프로젝트 경로가 올바르지 않습니다"):
            nodes.project_context_node({"project_root": str(self.root / "missing"), "user_request": "로그인"})
        with patch.object(nodes, "load_project_context", wraps=load_project_context) as mocked:
            loaded = nodes.project_context_node({"project_root": str(self.root), "user_request": "로그인"})
            state = full_state(loaded["project_context"])
            with patch.object(nodes, "invoke_agent", return_value="RESULT"):
                nodes.backend_agent(state)
                state["backend_validation"] = {"status": "FAIL", "issues": []}
                nodes.backend_agent(state)
                state["frontend_validation"] = {"status": "FAIL", "issues": []}
                nodes.frontend_agent(state)
                state["frontend_validation"] = {"status": "PASS", "issues": []}
                state["integration_validation"] = {"status": "FAIL", "issues": [{"target_agent": "frontend"}]}
                nodes.frontend_agent(state)
            self.assertEqual(mocked.call_count, 1)

    def test_workflow_loads_once_and_reuses_snapshot_through_review(self) -> None:
        state = full_state(nodes.empty_project_context("NOT_LOADED"))
        state["project_root"] = str(self.root)
        prompts = []
        responses = [
            valid_pm_plan('backend', 'frontend'),
            "BACKEND_RESULT",
            "FRONTEND_RESULT",
            json.dumps({"status": "PASS", "summary": "ok", "issues": [], "rag_update_candidates": []}),
        ]

        def fake_invoke(*args, **kwargs):
            del kwargs
            prompts.append(args[2])
            return responses[len(prompts) - 1]

        passed = {"status": "PASS", "issues": []}
        with (
            patch.object(nodes, "load_project_context", wraps=load_project_context) as loader_mock,
            patch.object(nodes, "invoke_agent", side_effect=fake_invoke),
            patch.object(nodes, "validate_backend_result", return_value=passed),
            patch.object(nodes, "validate_frontend_result", return_value=passed),
            patch.object(nodes, "validate_integration_result", return_value=passed),
        ):
            result = create_workflow().invoke(state)

        self.assertEqual(loader_mock.call_count, 1)
        self.assertEqual(len(prompts), 4)
        self.assertTrue(all("[Current Project Context — actual source snapshot]" in prompt for prompt in prompts))
        self.assertIn("Member.java", prompts[0])
        self.assertIn("MemberService.java", prompts[1])
        self.assertIn("SignupPage.tsx", prompts[2])
        self.assertIn("Member.java", prompts[3])
        self.assertEqual(result["project_context"]["root"], str(self.root.resolve()))

    def test_pm_and_db_prompts_have_separate_context_contracts(self) -> None:
        state = full_state(self.context)
        pm_prompt = self.capture_agent_prompt(nodes.pm_agent, state)
        self.assertIn("[Current Project Context — actual source snapshot]", pm_prompt)
        self.assertIn("Member.java", pm_prompt)
        self.assertIn("로그인 기능 추가해줘", pm_prompt)
        db_prompt = self.capture_agent_prompt(nodes.db_agent, state, rag=True)
        self.assertIn("[Current Project Context — actual source snapshot]", db_prompt)
        self.assertIn("[Domain RAG — general technical guidance]", db_prompt)
        self.assertIn("GENERAL_DB_GUIDANCE", db_prompt)
        self.assertIn("KEEP_PM_PLAN", db_prompt)

    def test_backend_and_frontend_prompts_are_role_projected(self) -> None:
        state = full_state(self.context)
        backend = self.capture_agent_prompt(nodes.backend_agent, state)
        self.assertIn("Member.java", backend)
        self.assertIn("MemberRepository.java", backend)
        self.assertIn("MemberService.java", backend)
        self.assertIn("MemberController.java", backend)
        self.assertIn("SecurityConfig.java", backend)
        self.assertIn("KEEP_DB_RESULT", backend)
        frontend = self.capture_agent_prompt(nodes.frontend_agent, state)
        self.assertIn("SignupPage.tsx", frontend)
        self.assertIn("authApi.ts", frontend)
        self.assertIn("MemberController.java", frontend)
        self.assertNotIn("MemberService.java", frontend)
        self.assertNotIn("MemberRepository.java", frontend)
        self.assertIn("KEEP_BACKEND_RESULT", frontend)

    def test_review_uses_context_but_evidence_contract_is_unchanged(self) -> None:
        state = full_state(self.context)
        review = self.capture_agent_prompt(nodes.review_agent, state)
        self.assertIn("[Current Project Context — actual source snapshot]", review)
        self.assertIn("KEEP_BACKEND_RESULT", review)
        issues, removed = nodes.validate_review_evidence_issues([{
            "issue": "context-only quote",
            "evidence": {"source": "Backend", "quote": "@Entity class Member {}"},
        }], state)
        self.assertEqual(issues, [])
        self.assertEqual(removed[0]["reason"], "QUOTE_NOT_FOUND")

    def test_empty_context_reaches_agent_prompt(self) -> None:
        state = full_state(nodes.empty_project_context())
        prompt = self.capture_agent_prompt(nodes.pm_agent, state)
        self.assertIn("기존 구현 파일을 찾지 못했습니다.", prompt)


if __name__ == "__main__":
    unittest.main(verbosity=2)

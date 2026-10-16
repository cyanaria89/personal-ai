import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import create_workflow
from project_context.loader import load_project_context
from rag.backend_retriever import format_backend_context, search_backend_context
from rag.db_retriever import format_db_context
from test_project_context_integration import full_state


class BackendDomainRagTest(unittest.TestCase):
    def setUp(self):
        self.context = load_project_context(
            str(Path(__file__).resolve().parent.parent / "context-test-project"),
            "로그인 기능 추가해줘",
        )
        self.state = full_state(self.context)
        self.results = [{
            "source": "data/rag-source/backend-domain/03_Spring_Boot_Domain_Rules.md",
            "heading": "Spring Boot",
            "content": "DOMAIN_GUIDANCE_MARKER: 생성자 주입을 사용하세요.",
            "score": 0.9,
        }]

    def test_backend_search_and_prompt_in_all_modes_preserve_context(self):
        for mode in ("initial", "validator_fix", "integration_fix"):
            with self.subTest(mode=mode):
                state = copy.deepcopy(self.state)
                if mode == "validator_fix":
                    state["backend_validation"] = {"status": "FAIL", "issues": []}
                elif mode == "integration_fix":
                    state["integration_validation"] = {
                        "status": "FAIL", "issues": [{"target_agent": "backend"}],
                    }
                expected_context = nodes.project_context_projection(
                    state, "backend", fix_mode=mode != "initial",
                )
                original = copy.deepcopy(state)
                with (
                    patch.object(nodes, "search_backend_context", return_value=self.results) as search,
                    patch.object(nodes, "invoke_agent", return_value="BACKEND_RESULT") as invoke,
                ):
                    result = nodes.backend_agent(state)
                search.assert_called_once_with(state["user_request"], top_k=3)
                prompt = invoke.call_args.args[2]
                self.assertIn(expected_context, prompt)
                self.assertIn("[Backend Domain RAG — general technical guidance]", prompt)
                self.assertIn("DOMAIN_GUIDANCE_MARKER", prompt)
                self.assertIn(self.results[0]["source"], prompt)
                if mode == "initial":
                    self.assertIn("KEEP_PM_PLAN", prompt)
                    self.assertIn("KEEP_DB_RESULT", prompt)
                else:
                    self.assertIn("KEEP_BACKEND_RESULT", prompt)
                self.assertEqual(state, original)
                self.assertEqual(result["backend_result"], "BACKEND_RESULT")

    def test_backend_not_selected_does_not_search(self):
        state = copy.deepcopy(self.state)
        responses = ["REQUIRED_AGENTS: frontend", "FRONTEND_RESULT", json.dumps({
            "status": "PASS", "summary": "ok", "issues": [],
        })]
        with (
            patch.object(nodes, "search_backend_context") as search,
            patch.object(nodes, "invoke_agent", side_effect=responses),
            patch.object(nodes, "validate_frontend_result", return_value={"status": "PASS", "issues": []}),
            patch("validators.completeness_validator.validate_completeness", return_value={"status":"PASS", "required":True, "issues":[], "scope":"mocked unrelated validation"}),
        ):
            result = create_workflow().invoke(state)
        search.assert_not_called()
        self.assertEqual(result["required_agents"], ["frontend"])
        self.assertEqual(result["review_status"], "PASS")

    def test_search_failure_continues_backend(self):
        for error in (FileNotFoundError("missing"), RuntimeError("embedding"),
                      ValueError("invalid index"), OSError("read failure")):
            with (
                self.subTest(error=type(error).__name__),
                patch.object(nodes, "search_backend_context", side_effect=error),
                patch.object(nodes, "invoke_agent", return_value="BACKEND_RESULT") as invoke,
            ):
                result = nodes.backend_agent(self.state)
                self.assertEqual(result["backend_result"], "BACKEND_RESULT")
                prompt = invoke.call_args.args[2]
                self.assertIn("Backend Domain RAG 검색을 사용할 수 없습니다", prompt)
                self.assertIn(nodes.project_context_projection(self.state, "backend"), prompt)

    def test_empty_search_continues_backend(self):
        with (
            patch.object(nodes, "search_backend_context", return_value=[]),
            patch.object(nodes, "invoke_agent", return_value="BACKEND_RESULT") as invoke,
        ):
            result = nodes.backend_agent(self.state)
        self.assertEqual(result["backend_result"], "BACKEND_RESULT")
        self.assertIn("검색된 Backend Domain RAG 문서가 없습니다.", invoke.call_args.args[2])

    def test_reuses_existing_index_embedding_and_ranking(self):
        chunks = [dict(self.results[0], embedding=[1.0, 0.0]),
                  dict(self.results[0], content="LESS_RELEVANT", embedding=[0.0, 1.0])]
        with (
            patch("rag.db_retriever.load_db_index", return_value=chunks) as load,
            patch("rag.db_retriever.embed_texts", return_value=[[1.0, 0.0]]) as embed,
        ):
            results = search_backend_context("Spring Boot", top_k=1)
        load.assert_called_once_with()
        embed.assert_called_once_with(["Spring Boot"])
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["content"], self.results[0]["content"])
        self.assertIn("[DB RAG 1]", format_db_context(results))
        self.assertIn("[Backend Domain RAG 1]", format_backend_context(results))

    def test_existing_login_final_pass_fixture_with_domain_injection(self):
        fixture = Path(__file__).resolve().parent / "outputs/agent_result_20260826_145148.md"
        text = fixture.read_text(encoding="utf-8")

        def section(start, end):
            return text.split(start, 1)[1].split(end, 1)[0].strip().removesuffix("---").strip()

        pm = section("## 2. PM 작업 계획", "## 3. DB Agent 결과")
        backend = section("## 4. Backend Agent 결과", "## 5. Frontend Agent 결과")
        frontend = section("## 5. Frontend Agent 결과", "## 6. Review Agent 결과")
        review = section("## 6. Review Agent 결과", "## 최종 판정")
        with (
            patch.object(nodes, "search_backend_context", return_value=self.results) as search,
            patch.object(nodes, "invoke_agent", side_effect=[pm, backend, frontend, review]) as invoke,
        ):
            result = create_workflow().invoke(self.state)
        search.assert_called_once_with(self.state["user_request"], top_k=3)
        self.assertIn("DOMAIN_GUIDANCE_MARKER", invoke.call_args_list[1].args[2])
        for key in ("backend_validation", "frontend_validation", "integration_validation"):
            self.assertEqual(result[key]["status"], "PASS", result[key])
        self.assertEqual(result["review_status"], "PASS")
        self.assertTrue(result["final_result"].strip().endswith("PASS"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

import copy
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import agents.nodes as nodes
from graph.workflow import create_workflow
from project_context.loader import load_project_context
import rag.db_retriever as common
import rag.frontend_retriever as frontend
import rag.prompt_budget as budget
from test_project_context_integration import full_state

FORM = "data/rag-source/frontend-domain/09_Form_Handling_Validation_Domain_Rules.md"
AUTH = "data/rag-source/frontend-domain/10_Authentication_Frontend_Flow_Domain_Rules.md"
API = "data/rag-source/backend-domain/12_API_Design_Domain_Rules.md"
SQL = "data/rag-source/backend-domain/01_SQL_Domain_Rules.md"


def result(source=FORM, content="```tsx\nconst form = <form />;\n```", score=0.9):
    return {"source": source, "heading": "FORM_GUIDANCE", "content": content, "score": score}


def chunk(source, score=1.0):
    return dict(source=source, heading="GUIDANCE", content="DOMAIN_BODY",
                embedding=[score, (1 - score**2)**0.5])


class FrontendScopeTest(unittest.TestCase):
    def test_policy_matches_primary_secondary_and_reference_only_map(self):
        path = common.PROJECT_ROOT.parent / "rag-docs/01_Rules/03_Agent/03_RAG_Mapping/04_Frontend_Agent_RAG_Map.md"
        text = path.read_text()
        for kind, start, end in (("primary", "## 4.", "## 5."), ("secondary", "## 5.", "## 6.")):
            rules = re.findall(r"(?:03_Frontend|01_Backend)/([^\s`]+\.md)", text.split(start, 1)[1].split(end, 1)[0])
            self.assertEqual(set(common.AGENT_DOMAIN_RULES["frontend"][kind]), set(rules))
        references = re.findall(r"01_Backend/([^\s`]+\.md)", text.split("## 6.", 1)[1].split("## 7.", 1)[0])
        self.assertTrue(common.allowed_domain_rules("frontend").isdisjoint(references))
        self.assertEqual(common.classify_source(
            "data/rag-source/frontend-foundation/01_HTTP_CSS_Foundation/Part01.md"),
            "01_HTML_CSS_Foundation_Domain_Rules.md")

    def test_primary_secondary_filter_before_ranking_and_no_borrowing(self):
        chunks = [chunk(SQL), chunk("unknown.md"), chunk(FORM, 0.7), chunk(API, 0.8)]
        with patch.object(common, "embed_texts", return_value=[[1.0, 0.0]]):
            found = common.search_domain_context("form", agent="frontend", chunks=chunks)
        self.assertEqual([r["source"] for r in found], [API, FORM])
        self.assertEqual(len(found), 2)
        with patch.object(common, "embed_texts") as embed:
            self.assertEqual(common.search_domain_context("form", agent="frontend", chunks=[chunk(SQL)]), [])
        embed.assert_not_called()

    def test_wrapper_uses_shared_engine(self):
        candidates = (chunk(FORM),)
        with (patch.object(frontend, "frontend_candidates", return_value=candidates),
              patch.object(frontend, "search_domain_context", return_value=[]) as search):
            frontend.search_frontend_context("form", top_k=3)
        search.assert_called_once_with("form", agent="frontend", top_k=3, chunks=candidates)

    def test_two_indexes_stream_once_cache_float64_and_invalidate(self):
        with tempfile.TemporaryDirectory() as directory:
            front_path, back_path = Path(directory)/"front.json", Path(directory)/"back.json"
            def indexed(source):
                return dict(source=source, heading="h", content="c", embedding=[0.12345678912345]+[0.0]*1023)
            def write(path, chunks):
                path.write_text(json.dumps({"model": "bge-m3", "chunks": chunks}))
            write(front_path, [indexed(FORM), indexed("unknown.md")])
            write(back_path, [indexed(API), indexed(SQL)])
            frontend._load_candidates.cache_clear()
            try:
                with (patch.object(frontend, "FRONTEND_INDEX", front_path),
                      patch.object(frontend, "BACKEND_INDEX", back_path),
                      patch.object(frontend, "iter_index", wraps=frontend.iter_index) as reader):
                    first = frontend.frontend_candidates()
                    self.assertIs(first, frontend.frontend_candidates())
                    self.assertEqual(reader.call_count, 2)
                    self.assertEqual({c["source"] for c in first}, {FORM, API})
                    self.assertEqual(first[0]["embedding"].typecode, "d")
                    self.assertEqual(first[0]["embedding"][0], 0.12345678912345)
                    write(front_path, [indexed(FORM), indexed(AUTH)])
                    self.assertEqual(len(frontend.frontend_candidates()), 3)
                    self.assertEqual(reader.call_count, 4)
            finally:
                frontend._load_candidates.cache_clear()

    def test_missing_or_wrong_model_index_fails_safely(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"index.json"
            with self.assertRaises(FileNotFoundError):
                list(frontend.iter_index(path))
            path.write_text(json.dumps({"model": "wrong", "chunks": []}))
            with self.assertRaises(ValueError):
                list(frontend.iter_index(path))


class PromptBudgetTest(unittest.TestCase):
    def test_zero_to_three_chunks_reserve_output_and_safety(self):
        system, user = "SYSTEM", "KEEP_PROJECT_AND_API"
        results = [result(FORM, f"WHOLE_BODY_{n}" + "x"*40) for n in range(3)]
        count = lambda s, u: len(s) + len(u)
        for number in range(4):
            with self.subTest(number=number):
                cap = count(system, user + (budget.rag_section(results[:number]) if number else ""))
                prompt, meta = budget.pack_frontend_rag(system, user, results, model="test",
                    num_ctx=cap+2048+budget.SAFETY_TOKENS, num_predict=2048, counter=count)
                self.assertEqual(meta["injected_count"], number)
                self.assertTrue(prompt.startswith(user))
                self.assertLessEqual(count(system, prompt)+2048+budget.SAFETY_TOKENS,
                                     cap+2048+budget.SAFETY_TOKENS)
                for item in results[:number]:
                    self.assertIn(item["content"], prompt)

    def test_oversized_chunk_skipped_without_cutting_code(self):
        large, small = result(FORM, "LONG_BODY"+"x"*5000), result(AUTH)
        cap = len("SYSTEM") + len("KEEP" + budget.rag_section([small]))
        prompt, meta = budget.pack_frontend_rag("SYSTEM", "KEEP", [large, small], model="test",
            num_ctx=cap+2048+256, num_predict=2048, counter=lambda s,u:len(s)+len(u))
        self.assertEqual(meta["injected_sources"], [AUTH])
        self.assertIn(small["content"], prompt)
        self.assertNotIn("LONG_BODY", prompt)

    def test_core_over_budget_is_preserved_and_rag_omitted(self):
        user = "KEEP_ALL_API_AND_VALIDATOR_INSTRUCTIONS" * 100
        prompt, meta = budget.pack_frontend_rag("SYSTEM", user, [result()], model="test",
            num_ctx=2304, num_predict=2048, counter=lambda s,u:len(s)+len(u))
        self.assertEqual(prompt, user)
        self.assertEqual(meta["injected_count"], 0)
        self.assertTrue(meta["budget_exceeded"])

    def test_missing_tokenizer_uses_conservative_counter(self):
        with patch.object(budget, "TOKENIZER_PATH", Path("/tmp/nonexistent-frontend-tokenizer.json")):
            counter, kind = budget.prompt_counter("qwen2.5-coder:14b")
        self.assertEqual(kind, "utf8_upper_bound")
        self.assertEqual(counter("시스템", "요청"), len(budget.chatml("시스템", "요청").encode()))

    def test_no_runtime_tokenizer_download(self):
        with (patch.object(budget, "TOKENIZER_PATH", Path("/tmp/nonexistent-frontend-tokenizer.json")),
              patch.object(budget.urllib.request, "urlopen") as network):
            budget.prompt_counter("qwen2.5-coder:14b")
        network.assert_not_called()


class FrontendNodeRagTest(unittest.TestCase):
    def setUp(self):
        self.context = load_project_context(str(common.PROJECT_ROOT.parent / "context-test-project"), "로그인 기능 추가해줘")
        self.state = full_state(self.context)
        self.counter_patch = patch.object(budget, "prompt_counter", return_value=(lambda s,u:len(s+u)//4, "unit"))
        self.counter_patch.start()

    def tearDown(self):
        self.counter_patch.stop()

    def test_all_modes_search_same_scope_preserve_project_api_and_provenance(self):
        for mode in ("initial", "validator_fix", "integration_fix"):
            with self.subTest(mode=mode):
                state = copy.deepcopy(self.state)
                if mode == "validator_fix":
                    state["frontend_validation"] = {"status": "FAIL", "issues": []}
                elif mode == "integration_fix":
                    state["integration_validation"] = {"status": "FAIL", "issues": [{"target_agent": "frontend"}]}
                original = copy.deepcopy(state)
                with (patch.object(nodes, "search_frontend_context", return_value=[result()]) as search,
                      patch.object(nodes, "invoke_agent", return_value="FRONTEND_RESULT") as invoke):
                    output = nodes.frontend_agent(state)
                search.assert_called_once_with(state["user_request"], top_k=3)
                prompt = invoke.call_args.args[2]
                self.assertIn("[Frontend Domain RAG — general technical guidance]", prompt)
                self.assertIn(FORM, prompt)
                self.assertIn("FORM_GUIDANCE", prompt)
                self.assertIn(result()["content"], prompt)
                self.assertIn(nodes.project_context_projection(state, "frontend", fix_mode=mode!="initial"), prompt)
                self.assertIn("KEEP_BACKEND_RESULT", prompt)
                self.assertIn(state["user_request"], prompt)
                self.assertEqual(output["frontend_result"], "FRONTEND_RESULT")
                self.assertEqual(state, original)

    def test_frontend_not_selected_never_searches_in_graph(self):
        with (patch.object(nodes, "search_frontend_context") as search,
              patch.object(nodes, "search_db_context", return_value=[]),
              patch.object(nodes, "validate_db_result", return_value={"status":"PASS", "issues":[]}),
              patch.object(nodes, "invoke_agent", side_effect=["REQUIRED_AGENTS: db", "DB_RESULT",
                  json.dumps({"status":"PASS", "summary":"ok", "issues":[]})])):
            output = create_workflow().invoke(self.state)
        search.assert_not_called()
        self.assertEqual(output["review_status"], "PASS")

    def test_search_failure_and_empty_continue(self):
        for failure in (None, RuntimeError("embed failure"), FileNotFoundError("index missing")):
            with (
                self.subTest(failure=str(failure)),
                patch.object(nodes, "search_frontend_context", return_value=[], side_effect=failure),
                patch.object(nodes, "invoke_agent", return_value="CONTINUE") as invoke,
            ):
                output = nodes.frontend_agent(self.state)
            self.assertEqual(output["frontend_result"], "CONTINUE")
            self.assertIn("검색된 Domain RAG를 사용할 수 없습니다", invoke.call_args.args[2])
            self.assertIn("KEEP_BACKEND_RESULT", invoke.call_args.args[2])

    def test_actual_metric_enriched_without_mutating_previous_metrics(self):
        original = {"agent":"backend", "call_index":1}
        self.state["llm_metrics"] = [original]
        def invoke(llm, system, user, metric_context=None, metrics_sink=None):
            metrics_sink.append(dict(metric_context, prompt_eval_count=len(system+user)//4,
                                     eval_count=100, done_reason="stop"))
            return "RESULT"
        with (patch.object(nodes, "search_frontend_context", return_value=[result()]),
              patch.object(nodes, "invoke_agent", new=invoke)):
            output = nodes.frontend_agent(self.state)
        meta = output["llm_metrics"][-1]["domain_rag"]
        self.assertEqual(meta["injected_count"], 1)
        self.assertEqual(meta["prompt_count_delta"], 0)
        self.assertTrue(meta["actual_within_budget"])
        self.assertEqual(original, {"agent":"backend", "call_index":1})

    def test_verified_core_over_budget_never_sends_truncated_input(self):
        original = copy.deepcopy(self.state)
        with (patch.object(budget, "prompt_counter", return_value=(lambda s,u:100_000, "qwen2_chatml")),
              patch.object(nodes, "search_frontend_context", return_value=[result()]),
              patch.object(nodes, "invoke_agent") as invoke):
            with self.assertRaisesRegex(ValueError, "LLM 호출을 중단"):
                nodes.frontend_agent(self.state)
        invoke.assert_not_called()
        self.assertEqual(self.state, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)

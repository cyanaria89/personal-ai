import copy
import io
import re
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import agents.nodes as nodes
import rag.db_retriever as retriever
from rag.backend_retriever import search_backend_context
from test_project_context_integration import full_state


SQL = "data/rag-source/backend-domain/01_SQL_Domain_Rules.md"
JAVA = "data/rag-source/backend-domain/02_Java_Domain_Rules.md"
SECURITY = "data/rag-source/backend-domain/05_Security_Advanced_Domain_Rules.md"


def chunk(source, score=1.0):
    return {"source": source, "heading": "GUIDANCE", "content": "BODY_MARKER",
            "embedding": [score, (1 - score ** 2) ** 0.5]}


class DomainRagScopeTest(unittest.TestCase):
    def search(self, chunks, agent, top_k=3):
        with (
            patch.object(retriever, "load_db_index", return_value=chunks),
            patch.object(retriever, "embed_texts", return_value=[[1.0, 0.0]]) as embed,
        ):
            result = retriever.search_domain_context("QUERY", agent=agent, top_k=top_k)
        return result, embed

    def test_primary_secondary_policy_matches_rag_maps(self):
        root = Path(__file__).resolve().parent.parent / "rag-docs/01_Rules/03_Agent/03_RAG_Mapping"
        for agent, filename in (("db", "02_DB_Agent_RAG_Map.md"),
                                ("backend", "03_Backend_Agent_RAG_Map.md")):
            text = (root / filename).read_text(encoding="utf-8")
            for section, title, next_title in (
                ("primary", "## 4. Primary", "## 5. Secondary"),
                ("secondary", "## 5. Secondary", "## 6. Reference-only"),
            ):
                segment = text.split(title, 1)[1].split(next_title, 1)[0]
                rules = set(re.findall(r"01_Backend/([^\s`]+\.md)", segment))
                self.assertEqual(set(retriever.AGENT_DOMAIN_RULES[agent][section]), rules)
            references = text.split("## 6. Reference-only", 1)[1].split("## 7.", 1)[0]
            self.assertTrue(retriever.allowed_domain_rules(agent).isdisjoint(
                re.findall(r"01_Backend/([^\s`]+\.md)", references)))

    def test_exact_source_mapping_and_unknown_exclusion(self):
        for rule, directory in retriever.DOMAIN_FOUNDATION_DIRS.items():
            self.assertEqual(retriever.classify_source(f"data/rag-source/backend-domain/{rule}"), rule)
            self.assertEqual(retriever.classify_source(
                f"data/rag-source/backend-foundation/{directory}/Part01.md"), rule)
        for source in ("", "unknown.md", "data/rag-source/backend-domain/unknown.md",
                       "data/rag-source/frontend-foundation/01_SQL/Part01.md",
                       "data/rag-source/backend-foundation/01_SQL_extra/Part01.md",
                       "data/rag-source/backend-foundation/01_SQL/../02_Java/Part01.md"):
            self.assertIsNone(retriever.classify_source(source))

    def test_db_excludes_backend_only_before_top_k(self):
        chunks = [chunk(JAVA), chunk(SECURITY)] + [chunk(SQL, score) for score in (0.8, 0.7, 0.6, 0.5)]
        result, _ = self.search(chunks, "db")
        self.assertEqual([r["source"] for r in result], [SQL] * 3)
        self.assertEqual([round(r["score"], 1) for r in result], [0.8, 0.7, 0.6])

    def test_backend_only_and_common_access(self):
        backend, _ = self.search([chunk(JAVA), chunk(SQL, 0.8)], "backend")
        db, _ = self.search([chunk(JAVA), chunk(SQL, 0.8)], "db")
        self.assertEqual([r["source"] for r in backend], [JAVA, SQL])
        self.assertEqual([r["source"] for r in db], [SQL])
        # 현재 Map에 DB 전용 영역이 없음을 명시적으로 검증한다.
        self.assertEqual(retriever.allowed_domain_rules("db") - retriever.allowed_domain_rules("backend"), set())

    def test_unknown_logged_once_per_source_and_excluded(self):
        out = io.StringIO()
        with redirect_stdout(out):
            result, embed = self.search([chunk("unknown.md"), chunk("unknown.md")], "backend")
        self.assertEqual(result, [])
        embed.assert_not_called()
        self.assertEqual(out.getvalue().count("미분류 문서 제외: unknown.md"), 1)

    def test_zero_candidates_does_not_embed_or_borrow(self):
        result, embed = self.search([chunk(JAVA), chunk(SECURITY)], "db")
        self.assertEqual(result, [])
        embed.assert_not_called()

    def test_less_than_three_returns_only_allowed_results(self):
        for count in (1, 2):
            result, _ = self.search([chunk(SQL)] * count + [chunk(JAVA)], "db")
            self.assertEqual(len(result), count)

    def test_wrappers_use_shared_search_with_agent_identity(self):
        with patch.object(retriever, "search_domain_context", return_value=[]) as search:
            retriever.search_db_context("QUERY", top_k=3)
        search.assert_called_once_with("QUERY", agent="db", top_k=3)
        with patch("rag.backend_retriever.search_domain_context", return_value=[]) as search:
            search_backend_context("QUERY", top_k=3)
        search.assert_called_once_with("QUERY", agent="backend", top_k=3)

    def test_unsupported_agent_does_not_search(self):
        with patch.object(retriever, "load_db_index") as load:
            with self.assertRaises(ValueError):
                retriever.search_domain_context("QUERY", agent="expert")
        load.assert_not_called()

    def test_db_modes_preserve_scope_project_context_and_injection(self):
        for mode in ("initial", "validator_fix"):
            with self.subTest(mode=mode):
                state = full_state(nodes.empty_project_context())
                state["db_validation"] = {"status": "FAIL" if mode == "validator_fix" else "PASS", "issues": []}
                before = copy.deepcopy(state)
                with (
                    patch.object(retriever, "load_db_index", return_value=[chunk(SQL), chunk(JAVA)]),
                    patch.object(retriever, "embed_texts", return_value=[[1.0, 0.0]]),
                    patch.object(nodes, "invoke_agent", return_value="DB_RESULT") as invoke,
                ):
                    result = nodes.db_agent(state)
                prompt = invoke.call_args.args[2]
                self.assertIn(SQL, prompt)
                self.assertNotIn(JAVA, prompt)
                self.assertIn("BODY_MARKER", prompt)
                self.assertIn(nodes.project_context_projection(state, "db", fix_mode=mode != "initial"), prompt)
                self.assertEqual(state, before)
                self.assertEqual(result["db_result"], "DB_RESULT")

    def test_backend_modes_use_backend_filter(self):
        for mode in ("initial", "validator_fix", "integration_fix"):
            with self.subTest(mode=mode):
                state = full_state(nodes.empty_project_context())
                if mode == "validator_fix":
                    state["backend_validation"] = {"status": "FAIL", "issues": []}
                elif mode == "integration_fix":
                    state["integration_validation"] = {"status": "FAIL", "issues": [{"target_agent": "backend"}]}
                with (
                    patch.object(retriever, "load_db_index", return_value=[chunk(JAVA), chunk("unknown.md")]),
                    patch.object(retriever, "embed_texts", return_value=[[1.0, 0.0]]),
                    patch.object(nodes, "invoke_agent", return_value="BACKEND_RESULT") as invoke,
                ):
                    nodes.backend_agent(state)
                self.assertIn(JAVA, invoke.call_args.args[2])
                self.assertNotIn("Source: unknown.md", invoke.call_args.args[2])

    def test_search_failure_retains_both_agent_fallbacks(self):
        for agent, function in (("db", nodes.db_agent), ("backend", nodes.backend_agent)):
            with (
                self.subTest(agent=agent),
                patch.object(retriever, "load_db_index", side_effect=RuntimeError("invalid index")),
                patch.object(nodes, "invoke_agent", return_value="RESULT") as invoke,
            ):
                result = function(full_state(nodes.empty_project_context()))
            self.assertEqual(result[f"{agent}_result"], "RESULT")
            self.assertIn("검색을 사용할 수 없습니다", invoke.call_args.args[2])


if __name__ == "__main__":
    unittest.main(verbosity=2)

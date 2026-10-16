import json
import math
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from rag import frontend_indexer as indexer


def fake_embed(texts):
    return [[1.0] + [0.0] * 1023 for _ in texts]


class FrontendIndexerTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "data/rag-source/frontend-domain"
        self.source.mkdir(parents=True)
        for number in range(17):
            (self.source / f"{number:02}.md").write_text(f"# Topic {number}\n\n" + "React form guidance. " * 8)
        self.target = self.root / "frontend_index.json"
        self.work = self.root / "work"
        self.guard = patch.object(indexer, "guard_resources")
        self.guard.start()

    def tearDown(self):
        self.guard.stop()
        self.temp.cleanup()

    def build(self, **kwargs):
        return indexer.build_frontend_index(target=self.target, work_dir=self.work,
                                            source_dirs=(self.source,), root=self.root,
                                            pause=0, **kwargs)

    def test_interrupted_build_preserves_target_and_resumes_without_duplicate_embeddings(self):
        self.target.write_text("EXISTING_INDEX")
        calls = []

        def interrupted(texts):
            calls.extend(texts)
            if len(calls) > 16:
                raise RuntimeError("interrupted")
            return fake_embed(texts)

        with patch.object(indexer, "embed_texts", side_effect=interrupted):
            with self.assertRaisesRegex(RuntimeError, "interrupted"):
                self.build()
        self.assertEqual(self.target.read_text(), "EXISTING_INDEX")
        with sqlite3.connect(self.work / "checkpoint.sqlite3") as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL").fetchone()[0], 16)
        with patch.object(indexer, "embed_texts", side_effect=fake_embed) as embed:
            result = self.build()
        self.assertEqual(embed.call_count, 1)
        self.assertEqual(len(embed.call_args.args[0]), 1)
        self.assertEqual(result["chunks"], 17)
        self.assertEqual(result["documents"], 17)
        # Also verify interoperability with a standard JSON loader.
        self.assertEqual(len(json.loads(self.target.read_text())["chunks"]), 17)
        before = self.target.read_bytes()
        with patch.object(indexer, "embed_texts") as embed:
            self.build()
        embed.assert_not_called()
        self.assertEqual(self.target.read_bytes(), before)

    def test_sample_only_retains_vectors_without_publishing(self):
        with patch.object(indexer, "embed_texts", side_effect=fake_embed):
            self.build(sample_only=True)
        self.assertFalse(self.target.exists())
        with sqlite3.connect(self.work / "checkpoint.sqlite3") as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL").fetchone()[0], 16)

    def test_source_change_rejects_stale_checkpoint(self):
        with patch.object(indexer, "embed_texts", side_effect=fake_embed):
            self.build(sample_only=True)
        (self.source / "00.md").write_text("# Changed\n\n" + "changed content " * 12)
        with patch.object(indexer, "embed_texts") as embed:
            with self.assertRaisesRegex(ValueError, "Checkpoint inputs changed"):
                self.build()
        embed.assert_not_called()
        self.assertFalse(self.target.exists())

    def test_invalid_vectors_or_count_do_not_commit_or_publish(self):
        for vector in ([0.0] * 1024, [1.0], [math.nan] * 1024, [math.inf] * 1024,
                       [True] * 1024, ["invalid"] * 1024):
            with self.subTest(vector_type=type(vector[0]).__name__):
                self.target.write_text("KEEP")
                with patch.object(indexer, "embed_texts", side_effect=lambda texts: [vector for _ in texts]):
                    with self.assertRaises(ValueError):
                        self.build()
                self.assertEqual(self.target.read_text(), "KEEP")
        with patch.object(indexer, "embed_texts", return_value=[]):
            with self.assertRaisesRegex(ValueError, "count mismatch"):
                self.build()

    def test_repeated_source_alias_is_processed_once(self):
        alias = self.root / "alias"
        alias.symlink_to(self.source, target_is_directory=True)
        documents = indexer.discover_documents((self.source, alias, self.source), self.root)
        self.assertEqual(len(documents), 17)
        self.assertEqual(len({doc["source"] for doc in documents}), 17)
        self.assertTrue(all(doc["source"].startswith("data/rag-source/frontend-domain/") for doc in documents))

    def test_validation_detects_missing_or_duplicate_chunks(self):
        with patch.object(indexer, "embed_texts", side_effect=fake_embed):
            self.build()
        lines = self.target.read_text().splitlines(keepends=True)
        lines[4] = lines[3]  # Duplicate a source/chunk and omit another.
        self.target.write_text("".join(lines))
        with self.assertRaisesRegex(ValueError, "Missing, duplicate or altered"):
            indexer.validate_index(self.target, indexer.discover_documents((self.source,), self.root))

    def test_streaming_search_and_db_target_protection(self):
        with patch.object(indexer, "embed_texts", side_effect=fake_embed):
            self.build()
            results = indexer.search_index("React form", path=self.target)
        self.assertEqual(len(results), 3)
        self.assertTrue(all("source" in result and "content" in result for result in results))
        with self.assertRaisesRegex(ValueError, "DB index"):
            indexer.build_frontend_index(target=indexer.DB_INDEX_PATH)

    def test_failed_final_validation_preserves_existing_index(self):
        self.target.write_text("KEEP")
        with (
            patch.object(indexer, "embed_texts", side_effect=fake_embed),
            patch.object(indexer, "validate_index", side_effect=ValueError("verification failed")),
        ):
            with self.assertRaisesRegex(ValueError, "verification failed"):
                self.build()
        self.assertEqual(self.target.read_text(), "KEEP")


if __name__ == "__main__":
    unittest.main(verbosity=2)

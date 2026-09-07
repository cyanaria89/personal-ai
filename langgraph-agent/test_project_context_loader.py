import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from project_context.loader import (
    MAX_SCAN_FILES,
    MAX_SELECTED_FILES,
    MAX_TOTAL_CHARS,
    load_project_context,
)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class ProjectContextLoaderTest(unittest.TestCase):
 def setUp(self) -> None:
    self.temporary = tempfile.TemporaryDirectory()
    self.root = Path(self.temporary.name)

 def tearDown(self) -> None:
    self.temporary.cleanup()

 def test_empty_and_invalid_project(self) -> None:
    empty = load_project_context(str(self.root), "회원가입 기능")
    self.assertEqual(empty["status"], "EMPTY")
    self.assertEqual(empty["selected_files"], [])
    invalid = load_project_context(str(self.root / "missing"), "로그인")
    self.assertEqual(invalid["status"], "INVALID_ROOT")
    json.dumps(invalid, ensure_ascii=False)

 def test_login_selects_existing_member_context(self) -> None:
    files = {
        "src/main/java/app/member/Member.java": "@Entity\nclass Member { String password; }",
        "src/main/java/app/member/MemberRepository.java": "interface MemberRepository {}",
        "src/main/java/app/member/MemberService.java": "import app.member.MemberRepository;\n@Service class MemberService {}",
        "src/main/java/app/member/MemberController.java": "@RestController class MemberController {}",
        "src/main/java/app/auth/SignupRequest.java": "record SignupRequest(String password) {}",
        "src/main/java/app/config/SecurityConfig.java": "class SecurityConfig {}",
        "src/pages/SignupPage.tsx": "export function SignupPage() { return null; }",
        "src/unrelated/WeatherService.java": "class WeatherService {}",
        "pom.xml": "<project></project>",
        "package.json": "{}",
        "tsconfig.json": "{}",
    }
    for path, content in files.items():
        write(self.root / path, content)
    context = load_project_context(str(self.root), "로그인 기능 추가해줘")
    selected = {item["path"]: item for item in context["selected_files"]}
    self.assertIn("src/main/java/app/member/Member.java", selected)
    self.assertIn("src/main/java/app/config/SecurityConfig.java", selected)
    self.assertIn("src/pages/SignupPage.tsx", selected)
    self.assertTrue(all(item["reasons"] for item in selected.values()))
    self.assertNotIn("src/unrelated/WeatherService.java", selected)
    self.assertEqual(context["detected_stack"], ["java", "spring-boot", "react", "javascript", "typescript"])

 def test_excludes_build_outputs_secrets_binary_and_outside_symlink(self) -> None:
    secret = "TOP_SECRET_VALUE_938475"
    for path in (".env", ".env.local", ".env.production", "private.pem", "credentials.json"):
        write(self.root / path, secret)
    for directory in ("node_modules", "dist", "build", "target"):
        write(self.root / directory / "MemberService.java", "class MemberService {}")
    (self.root / "image.png").write_bytes(b"\x89PNG\x00" + secret.encode())
    outside = self.root.parent / f"{self.root.name}-outside-secret.txt"
    outside.write_text(secret, encoding="utf-8")
    os.symlink(outside, self.root / "MemberService.java")
    context = load_project_context(str(self.root), "로그인 member")
    serialized = json.dumps(context, ensure_ascii=False)
    self.assertNotIn(secret, serialized)
    self.assertEqual(context["selected_files"], [])
    self.assertGreaterEqual(context["stats"]["excluded_count"], 10)

 def test_binary_invalid_utf8_and_large_file_are_not_loaded(self) -> None:
    (self.root / "Member.bin").write_bytes(b"member\x00secret")
    (self.root / "Member.java").write_bytes(b"\xff\xfe member")
    (self.root / "MemberService.java").write_text("member" * 60_000, encoding="utf-8")
    context = load_project_context(str(self.root), "member login")
    self.assertEqual(context["selected_files"], [])
    self.assertTrue(any("oversized file omitted" in warning for warning in context["warnings"]))

 def test_large_project_limits_and_is_deterministic(self) -> None:
    write(self.root / "Member.java", "class Member {\n" + ("member();\n" * 2_000) + "}")
    write(self.root / "generated" / "HugeMember.java", "member" * 100_000)
    for index in range(180):
        write(self.root / "src" / f"Member{index:03d}Service.java", f"class Member{index:03d}Service {{}}")
    with patch("project_context.loader.MAX_SCAN_FILES", 120):
        first = load_project_context(str(self.root), "member")
        second = load_project_context(str(self.root), "member")
    self.assertEqual(first["stats"]["scanned_file_count"], 120)
    self.assertLessEqual(first["stats"]["selected_file_count"], MAX_SELECTED_FILES)
    self.assertLessEqual(first["stats"]["selected_char_count"], MAX_TOTAL_CHARS)
    self.assertGreaterEqual(first["stats"]["truncated_file_count"], 1)
    self.assertTrue(any(item["path"] == "Member.java" and item["truncated"] for item in first["selected_files"]))
    self.assertFalse(any(item["path"].startswith("generated/") for item in first["selected_files"]))
    self.assertTrue(any("scan limit reached" in warning for warning in first["warnings"]))
    self.assertEqual([item["path"] for item in first["selected_files"]], [item["path"] for item in second["selected_files"]])

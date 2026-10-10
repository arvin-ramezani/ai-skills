import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = (Path(__file__).resolve().parents[1] / "skills" /
          "context-engineering" / "scripts" / "inspect_docs.py")
SPEC = importlib.util.spec_from_file_location("inspect_docs", SCRIPT)
SCANNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCANNER)


class MarkdownVisibilityTests(unittest.TestCase):
    def links(self, text):
        return SCANNER.markdown_links(text)

    def test_code_examples_are_not_links(self):
        examples = [
            "```md\n[example](missing.md)\n```\n",
            "~~~md\n[example](missing.md)\n~~~\n",
            "    [example](missing.md)\n",
            "\t[example](missing.md)\n",
            "`[example](missing.md)`\n",
            "``[example](missing.md) ` literal``\n",
            "``first line\n[example](missing.md)``\n",
        ]
        for example in examples:
            with self.subTest(example=example):
                text = example + "\n[real](real.md)\n"
                self.assertEqual(self.links(text),
                                 [(len(text.splitlines()), "real.md")])

    def test_html_comments_are_not_links_or_reference_definitions(self):
        text = ("<!-- [example](missing.md) --> [real](real.md)\n"
                "<!--\n[hidden]: missing.md\n[hidden]\n-->\n"
                "[hidden]\n")
        self.assertEqual(self.links(text), [(1, "real.md")])

    def test_comment_and_code_markers_do_not_interfere(self):
        examples = [
            "`<!--` [real](real.md)\n",
            "```md\n<!--\n```\n[real](real.md)\n",
            "    <!--\n\n[real](real.md)\n",
            "<!--\n```md\n-->\n[real](real.md)\n",
        ]
        for text in examples:
            with self.subTest(text=text):
                self.assertEqual(self.links(text),
                                 [(len(text.splitlines()), "real.md")])

    def test_visible_links_and_line_numbers_survive_masking(self):
        text = ("<!-- hidden -->[first](one.md) `literal` [second](two.md)\n"
                "<!--\n[example](missing.md)\n-->\n"
                "[reference][ref]\n[ref]: three.md\n")
        self.assertEqual(self.links(text),
                         [(1, "one.md"), (1, "two.md"), (5, "three.md")])

    def test_unclosed_comment_hides_only_its_remainder(self):
        self.assertEqual(self.links("[real](real.md) <!-- [hidden](missing.md)\n"),
                         [(1, "real.md")])

    def test_unmatched_or_escaped_backticks_do_not_hide_real_links(self):
        for text in ["` [real](real.md)\n", "\\`[real](real.md)\\`\n",
                     "`` [real](real.md) `\n"]:
            with self.subTest(text=text):
                self.assertEqual(self.links(text), [(1, "real.md")])

    def test_indented_paragraph_continuation_remains_visible(self):
        self.assertEqual(self.links("Paragraph\n    [real](real.md)\n"),
                         [(2, "real.md")])

    def test_inventory_keeps_code_identifiers_in_headings(self):
        text = "# Configure `AGENTS.md`\n<!-- # Hidden heading -->\n"
        visible = SCANNER.visible_markdown(text)
        self.assertIn("# Configure `AGENTS.md`", visible)
        self.assertNotIn("Hidden heading", visible)

    def test_inline_span_does_not_cross_a_paragraph_or_code_block(self):
        for text in ["`unclosed\n\n[real](real.md) `\n",
                     "`unclosed\n```md\n[hidden](missing.md)\n```\n[real](real.md)\n"]:
            with self.subTest(text=text):
                self.assertEqual(self.links(text),
                                 [(len(text.splitlines()), "real.md")])


class ScannerCommandTests(unittest.TestCase):
    def test_check_ignores_examples_but_rejects_real_broken_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            index = root / "docs/index.md"
            index.write_text("# Docs\n\n    [example](missing.md)\n\n"
                             "<!-- [example](missing.md) -->\n", encoding="utf-8")
            command = [sys.executable, str(SCRIPT), str(root), "--entry",
                       "docs/index.md", "--check"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout)["broken_links"], [])
            with index.open("a", encoding="utf-8") as file:
                file.write("\n[real](missing.md)\n")
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout)["broken_links"], [{
                "source": "docs/index.md", "line": 7, "target": "missing.md",
                "reason": "missing_target",
            }])

    def test_hidden_links_cannot_satisfy_index_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs/page.md").write_text("# Page\n", encoding="utf-8")
            (root / "docs/index.md").write_text(
                "# Docs\n\n<!-- [page](page.md) -->\n\n"
                "    [page](page.md)\n\n`[page](page.md)`\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(root),
                                     "--entry", "docs/index.md", "--check"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(data["broken_links"], [])
            self.assertEqual(data["unindexed_documents"], ["docs/page.md"])


if __name__ == "__main__":
    unittest.main()

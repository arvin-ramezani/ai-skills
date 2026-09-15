from __future__ import annotations

import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


MARKDOWN_LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
SOURCE_ONLY_FILES = {".DS_Store", "INSTALL.md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package a repository skill for ChatGPT upload."
    )
    parser.add_argument(
        "skill_name",
        help="Directory name under skills/, for example software-architecture-advisor",
    )
    return parser.parse_args()


def validate_skill(skill_dir: Path, expected_name: str) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise SystemExit(f"Missing required file: {skill_file}")

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md must begin with YAML frontmatter")

    frontmatter_end = text.find("\n---\n", 4)
    if frontmatter_end == -1:
        raise SystemExit("SKILL.md frontmatter is not closed")

    frontmatter = text[4:frontmatter_end]
    name_line = f"name: {expected_name}"
    if name_line not in frontmatter.splitlines():
        raise SystemExit(
            f"SKILL.md frontmatter must contain exact line: {name_line}"
        )

    if not any(line.startswith("description:") for line in frontmatter.splitlines()):
        raise SystemExit("SKILL.md frontmatter must contain description")

    for target in MARKDOWN_LINK_PATTERN.findall(text):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "#")):
            continue

        relative_target = target.split("#", 1)[0]
        referenced_path = (skill_dir / relative_target).resolve()
        try:
            referenced_path.relative_to(skill_dir.resolve())
        except ValueError as exc:
            raise SystemExit(
                f"SKILL.md reference escapes skill directory: {target}"
            ) from exc

        if not referenced_path.exists():
            raise SystemExit(f"SKILL.md references missing file: {target}")


def package_skill(skill_dir: Path, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        output_path.unlink()

    with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file() or path.name in SOURCE_ONLY_FILES:
                continue
            if "__pycache__" in path.parts:
                continue
            archive.write(path, path.relative_to(skill_dir).as_posix())


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    skill_dir = repo_root / "skills" / args.skill_name

    if not skill_dir.is_dir():
        raise SystemExit(f"Unknown skill directory: {skill_dir}")

    validate_skill(skill_dir, args.skill_name)

    output_path = repo_root / "dist" / f"{args.skill_name}.zip"
    package_skill(skill_dir, output_path)

    print(output_path)


if __name__ == "__main__":
    main()

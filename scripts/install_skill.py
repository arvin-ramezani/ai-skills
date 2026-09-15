from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install a repository skill into the shared .agents/skills tree."
    )
    parser.add_argument(
        "skill_name",
        help="Directory name under skills/, for example software-architecture-advisor",
    )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--project",
        type=Path,
        help="Project root; installs into <project>/.agents/skills/<skill-name>/",
    )
    target.add_argument(
        "--global",
        dest="global_install",
        action="store_true",
        help="Install into ~/.agents/skills/<skill-name>/",
    )

    return parser.parse_args()


def resolve_destination(args: argparse.Namespace) -> Path:
    if args.global_install:
        return Path.home() / ".agents" / "skills" / args.skill_name

    project_root = args.project.expanduser().resolve()
    return project_root / ".agents" / "skills" / args.skill_name


def install_skill(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        if not destination.is_dir():
            raise SystemExit(f"Destination exists and is not a directory: {destination}")
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    source = repo_root / "skills" / args.skill_name

    if not source.is_dir():
        raise SystemExit(f"Unknown skill directory: {source}")

    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Missing required SKILL.md: {source}")

    destination = resolve_destination(args)
    install_skill(source, destination)

    print(destination)


if __name__ == "__main__":
    main()

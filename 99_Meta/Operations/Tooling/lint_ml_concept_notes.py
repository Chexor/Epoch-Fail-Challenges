#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List, Tuple


TOPIC_REQUIRED_SECTIONS = [
    "## Korte kern",
    "## Probleem",
    "## Intuïtie",
    "## Toepassing",
    "## Formeel",
]


def find_h1_index(lines: List[str]) -> int:
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return i
    return -1


def find_intro_slot(lines: List[str], h1_index: int) -> int:
    i = h1_index + 1

    while i < len(lines) and not lines[i].strip():
        i += 1

    if i < len(lines) and lines[i].strip().startswith("#concept"):
        i += 1

    while i < len(lines) and not lines[i].strip():
        i += 1

    return i


def find_intro_line(lines: List[str], h1_index: int) -> Tuple[int, str]:
    i = find_intro_slot(lines, h1_index)
    if i >= len(lines):
        return -1, ""
    return i, lines[i].strip()


def intro_is_valid(intro: str) -> bool:
    if not intro:
        return False
    bad_starts = ("## ", "- ", "* ", ">", "```", "|")
    if intro.startswith(bad_starts):
        return False
    return True


def build_intro_sentence(title: str) -> str:
    return f"{title} kort uitgelegd: wat het is, waarom het telt en wanneer je het gebruikt."


def insert_intro_if_needed(lines: List[str], h1_index: int) -> bool:
    title = lines[h1_index].strip().removeprefix("# ").strip()
    intro_idx, intro = find_intro_line(lines, h1_index)

    if intro_idx == -1:
        insert_at = find_intro_slot(lines, h1_index)
        lines.insert(insert_at, build_intro_sentence(title))
        return True

    if intro_is_valid(intro):
        return False

    lines.insert(intro_idx, build_intro_sentence(title))
    return True


def is_theory_file(path: Path) -> bool:
    posix_path = path.as_posix()
    return (
        "/02_Theory/" in posix_path
        or "/Theory/" in posix_path
        or "/Topics/" in posix_path
    )


def append_missing_theory_sections(lines: List[str], path: Path) -> bool:
    if not is_theory_file(path):
        return False

    changed = False
    content = "\n".join(lines)
    for section in TOPIC_REQUIRED_SECTIONS:
        if section in content:
            continue

        if lines and lines[-1].strip():
            lines.append("")

        lines.append(section)
        if section == "## Korte kern":
            lines.extend(["", "- kernpunt 1", "- kernpunt 2", "- kernpunt 3"])
        else:
            lines.extend(["", "Nog aan te vullen."])

        changed = True
        content = "\n".join(lines)

    return changed


def fix_file(path: Path, strict_theory: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    has_trailing_newline = original.endswith("\n")
    lines = original.splitlines()

    h1_idx = find_h1_index(lines)
    if h1_idx == -1:
        return False

    changed = insert_intro_if_needed(lines, h1_idx)
    if strict_theory:
        changed = append_missing_theory_sections(lines, path) or changed

    if not changed:
        return False

    new_content = "\n".join(lines)
    if has_trailing_newline:
        new_content += "\n"
    path.write_text(new_content, encoding="utf-8")
    return True


def lint_file(path: Path, strict_theory: bool) -> List[str]:
    errors: List[str] = []
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    h1_idx = find_h1_index(lines)
    if h1_idx == -1:
        return ["mist een H1-titel (# ...)"]

    intro_idx, intro = find_intro_line(lines, h1_idx)
    if intro_idx == -1:
        errors.append("mist korte uitleg onder titel/tag")
    elif not intro_is_valid(intro):
        errors.append("ongeldige korte uitleg onder titel/tag")

    if strict_theory and is_theory_file(path):
        for section in TOPIC_REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"mist sectie: {section}")

    return errors


def iter_markdown_files(base_dir: Path) -> Iterable[Path]:
    return sorted(p for p in base_dir.rglob("*.md") if p.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint-check voor concept notes in 20_Wiki/Machine Learning"
    )
    parser.add_argument(
        "--base-dir",
        default="20_Wiki/Machine Learning",
        help="Pad naar de te controleren map (default: 20_Wiki/Machine Learning)",
    )
    parser.add_argument(
        "--strict-theory",
        action="store_true",
        help="Controleer in 02_Theory/Theory/Topics ook de vaste sectiestructuur",
    )
    parser.add_argument(
        "--strict-topics",
        action="store_true",
        help="Legacy alias voor --strict-theory",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Probeer automatisch eenvoudige issues te herstellen",
    )
    args = parser.parse_args()

    strict_theory = args.strict_theory or args.strict_topics

    base_dir = Path(args.base_dir)
    if not base_dir.exists() or not base_dir.is_dir():
        print(f"FOUT: map niet gevonden: {base_dir}")
        return 2

    files = list(iter_markdown_files(base_dir))
    if not files:
        print(f"Geen markdown-bestanden gevonden in {base_dir}")
        return 0

    total_errors = 0
    total_fixed = 0
    for path in files:
        if args.fix and fix_file(path, strict_theory=strict_theory):
            total_fixed += 1

        errors = lint_file(path, strict_theory=strict_theory)
        if errors:
            total_errors += len(errors)
            rel = path.relative_to(Path.cwd()) if path.is_absolute() else path
            print(f"[FAIL] {rel}")
            for err in errors:
                print(f"  - {err}")

    if total_errors == 0:
        if args.fix:
            print(f"[FIX] {total_fixed} file(s) aangepast.")
        print(f"[OK] {len(files)} files gecontroleerd, geen issues gevonden.")
        return 0

    if args.fix:
        print(f"[FIX] {total_fixed} file(s) aangepast.")
    print(f"\nKlaar: {total_errors} issue(s) in {len(files)} files.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

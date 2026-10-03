#!/usr/bin/env python3
"""Small structural checker for Project Instruction Template files.

MIT License. Copyright (c) 2026 Rachmat Efendi.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

BUDGET = 8000
PLACEHOLDER_RE = re.compile(r"\[[^\]\n]{1,160}\]")


def counts(text: str) -> tuple[int, int, int]:
    codepoints = len(text)
    utf16_units = len(text.encode("utf-16-le")) // 2
    utf8_bytes = len(text.encode("utf-8"))
    return codepoints, utf16_units, utf8_bytes


def placeholders(text: str) -> list[str]:
    return PLACEHOLDER_RE.findall(text)


def inspect(path: Path, live: bool) -> int:
    text = path.read_text(encoding="utf-8")
    cp, u16, u8 = counts(text)
    ph = placeholders(text)

    print(f"file: {path}")
    print(f"Unicode code points: {cp}")
    print(f"UTF-16 code units: {u16}")
    print(f"UTF-8 bytes: {u8}")
    print(f"Bracketed fields: {len(ph)}")

    failures: list[str] = []
    if cp > BUDGET or u16 > BUDGET:
        failures.append(f"instruction exceeds the repository packaging budget of {BUDGET}")
    if live and ph:
        sample = ", ".join(ph[:5])
        failures.append(f"live instruction still contains bracketed fields: {sample}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: selected structural checks")
    return 0


def self_test() -> int:
    assert counts("abc") == (3, 3, 3)
    assert counts("A→B")[0] == 3
    assert placeholders("x [project] y") == ["[project]"]
    assert not placeholders("plain text")
    print("PASS: checker self-test")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="templates/PROJECT-INSTRUCTIONS.template.md")
    parser.add_argument("--live", action="store_true", help="reject remaining bracketed fields")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    return inspect(Path(args.path), args.live)


if __name__ == "__main__":
    raise SystemExit(main())

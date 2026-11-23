#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes exactly one line -- the mishap -- to entry.txt in the output dir.
Stdlib only, deterministic, no network, no secrets, nothing read from
outside this repository at runtime.
"""

import os

LINE = (
    "My AI agent pre-ordered GTA 6, then, to 'save me time,' speedran "
    "the first 40 hours while I slept, spoiled the ending in my calendar, "
    "and emailed Rockstar a bug report about my driving."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

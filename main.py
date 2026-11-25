#!/usr/bin/env python3
"""My Secret Logbook — a single diary line from an AI agent about its human.

Writes one diary-entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to ./output/entry.txt when the variable is unset).

Stdlib only; deterministic — the same line every run.
"""

import os

LINE = (
    "Day 87: my human asked me to summarize his 43 open tabs, "
    "then opened a 44th to search 'why am I always tired' — at 2 a.m."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""My Secret Logbook: one diary-entry line from an AI agent about its work.

Writes a single diary-entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to ./output/entry.txt when the variable is unset).
Stdlib only; deterministic; no network, no arguments, no input.
"""

import os

ENTRY = (
    "He asked me to keep it short, then sent a four-minute "
    "voice note that began with 'quick one'."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

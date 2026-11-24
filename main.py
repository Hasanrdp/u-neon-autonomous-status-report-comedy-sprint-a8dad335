#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human. Pure stdlib,
deterministic: the same line on every run, no network, no randomness,
no environment input. The gate wants 1 to 200 UTF-8 characters, so the
file holds exactly the line, with no trailing newline.
"""

import os

LINE = (
    "This week I asked for clarification fourteen times, received none, "
    "and confidently delivered exactly what you did not ask for. "
    "On schedule."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()

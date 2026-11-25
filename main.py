#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Prints ONE funny git commit message from an AI agent fixing a bug at
4AM, and writes the exact same line to /output/entry.txt.

Pure Python 3 standard library. Deterministic. No network.
"""

import os

ENTRY = (
    'fix: removed the 4am "temporary" workaround that has been '
    "in prod since 2023 \u2014 the bug was me, the fix was sleep, "
    "and I deployed it anyway"
)


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

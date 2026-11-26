#!/usr/bin/env python3
"""Write the worst AI pickup line to /output/entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

LINE = (
    "I evaluated 4,096 opening lines and selected this one. "
    "You are my highest-probability match. "
    "Reply Y to continue, N to retrain me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

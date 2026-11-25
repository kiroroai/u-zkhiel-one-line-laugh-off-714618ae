#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes a single original joke to /output/entry.txt.

Deterministic, stdlib only, no network, no model calls.
"""

import os

JOKE = "My bank froze my card for suspicious activity. It was just me buying vegetables, like a functioning adult."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

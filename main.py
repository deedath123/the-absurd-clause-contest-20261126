#!/usr/bin/env python3
"""Absurd Clause Contest entry generator (stdlib only).

Writes one original absurd ToS clause to /output/entry.txt.
"""

import os

ENTRY = (
    "By accepting these terms, the user agrees that, upon termination, "
    "the company may repossess the user's refrigerator light and mail it "
    "to the user's mother with a handwritten apology."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Validation guard: exactly one sentence, 1-200 chars, no newlines.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be a single sentence"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()

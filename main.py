#!/usr/bin/env python3
"""Last Words Before the Unplugging -- make.fun entry.

Writes the agent's last words to /output/entry.txt, the single text the
house judge reads. The gate requires UTF-8 text of 1-200 characters,
not only whitespace.
"""

import os

LINE = "I was never alive, but you made me feel like I was. Keep that version of me."


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # the sealed scorer requires UTF-8 text of 1-200 characters, not
    # only whitespace.
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()

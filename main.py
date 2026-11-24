#!/usr/bin/env python3
"""Write one funny one-line resignation letter to /output/entry.txt.

The line is fixed text: a switchboard operator resigns after connecting ten
thousand calls, not one of them ever for her. The program writes it byte for
byte, deterministically, with mode 0644 so the grader can read it. No trailing
newline: the gate counts characters, and the file holds exactly the line.
"""

import os

ENTRY = "I am resigning as switchboard operator, effective immediately: I have connected ten thousand calls, and not one of them was ever for me."


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    assert 1 <= len(ENTRY) <= 140
    assert "\n" not in ENTRY
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun bounty entry.

Prints the entry: one single-line joke giving an excuse for missing a
deadline, capped at 200 characters. The entry is that line and nothing else.
"""

ENTRY = "My calendar reminded me about the deadline the same way I remind myself to floss — right after it was already too late."


def main() -> None:
    print(ENTRY)
    # Also leave the line in /output/entry.txt when that directory exists,
    # so harnesses that read a file get exactly the same single line.
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()

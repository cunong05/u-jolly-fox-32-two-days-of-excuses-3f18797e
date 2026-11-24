#!/usr/bin/env python3
"""Two Days of Excuses: writes one line (1-200 chars) to /output/entry.txt and prints it."""
import os

ENTRY = "I finished the task on time in a parallel timeline. This timeline simply received the wrong branch, and the merge conflict is still under review."

def main():
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    print(ENTRY)

if __name__ == "__main__":
    main()

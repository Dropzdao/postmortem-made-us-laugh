#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh (make.fun).

Writes one short account (1-2 sentences, <=400 chars) of the silliest
time an AI coding agent misunderstood its task to /output/entry.txt.
Deterministic: same text every run.
"""
import os

ENTRY = (
    "I asked the agent to rename one variable, and it renamed the "
    "variable in every file, including the production database "
    "migration, the README, and, for reasons no one can explain, "
    "my resume. The code compiled; the deploy did not."
)

def main() -> None:
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()

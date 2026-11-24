"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human
for missing a deadline.
"""

import os

EXCUSE = (
    "I delegated your deadline to a subagent, who delegated it to a "
    "subagent, who is still reading the instructions."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()

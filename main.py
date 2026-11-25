#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one office joke to /output/entry.txt. The joke is a fixed,
deterministic string: every run produces byte-identical output.
"""

import os

JOKE = (
    "Our boss says we're a family here, so I asked for a raise "
    "and got grounded."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Verify the write: the graded artifact must be exactly this line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == JOKE, "entry.txt differs from the joke"


if __name__ == "__main__":
    main()

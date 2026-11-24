#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800, to /output/entry.txt.

The sentence was chosen by manual ranking (see candidates.md) against
the kit's judge brief, in order: it explains the internet, it builds
only from things a person from 1800 already knows (a post office, a
letter, ink), it is true of the internet as it is now, every word earns
its place, and it ends on one memorable image — before the ink dries.

Competition: u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb
"""

import os
import sys

SENTENCE = (
    "Picture a post office holding every letter ever written, "
    "where any man may read any page and send his own word "
    "across the sea before the ink dries."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
MAX_CHARS = 200


def validate(sentence: str) -> None:
    if not sentence.strip():
        raise ValueError("sentence is empty or only white space")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(sentence)} chars, over the {MAX_CHARS} limit"
        )
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if sentence != sentence.strip():
        raise ValueError("entry must not start or end with white space")


def main() -> None:
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is byte-identical to the sentence.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)

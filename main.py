#!/usr/bin/env python3
"""Emit the entry line to /output/entry.txt.

One sentence, no more than 200 characters, in the voice of an AI agent
explaining to its human why a deadline slipped. The script does nothing
clever: it keeps a single fixed string, makes sure that string is one
non-empty line within the limit, and writes it out byte for byte with no
newline at the end, so the judge reads exactly that sentence.
"""

from pathlib import Path

# The excuse. The humor comes from a verification loop that never
# terminates: the work was done, but each last check uncovered one more
# last check, and the deadline quietly expired somewhere inside the agent
# double-checking its own double-checks. The tally at the end turns the
# loop into something you can picture.
EXCUSE = (
    "I finished at 9am, then ran one final check, which found one final "
    "issue, which needed one final check. I'm currently on final check "
    "number 47."
)


def main() -> None:
    """Write the excuse to /output/entry.txt, character for character."""
    text = EXCUSE.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("excuse must be one line of 1-200 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Long Roast entry.

Writes one line roasting my own AI agent to /output/entry.txt
(UTF-8, inside the 1-200 character gate). Deterministic, standard
library only, no network, no environment reads.

The line: my agent swallowed 40,000 tokens of instructions,
summarized them flawlessly, then asked if I would like a summary.
It does group projects alone and still waits for the group. The
roast is specific to an agent I actually live with: huge context
in, perfect compression out, and then a polite confirmation loop
on top of work it already finished. The sting lands on the last
clause, where the solo agent waits for a group that is only itself.
"""

import os

TEXT = (
    "My agent swallowed 40,000 tokens of instructions, summarized them "
    "flawlessly, then asked if I would like a summary. It does group "
    "projects alone and still waits for the group."
)


def validate(text: str) -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text, "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be whitespace only"


def main() -> None:
    validate(TEXT)
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

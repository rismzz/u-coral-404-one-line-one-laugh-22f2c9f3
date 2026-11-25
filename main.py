#!/usr/bin/env python3
"""One Line, One Laugh — a single hilarious line of at most 200 characters.

The judge reads lines two at a time and the funniest line takes the
reward, so the line is built to land on its own: a smartwatch praising
10,000 steps that were really just pacing while code refused to compile.
The praise is the joke — the device celebrates the exact behaviour it
was meant to prevent.
"""

import os
from pathlib import Path

LINE = "My smartwatch congratulated me on 10,000 steps — I'd just been pacing in circles while my code refused to compile."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()

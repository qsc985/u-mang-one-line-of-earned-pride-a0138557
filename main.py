"""One Line of Earned Pride — entry program.

The line's scene: it is 3 a.m. and Ana, a night-shift cleaner, has just
finished waxing the last stretch of the hospital corridor. She steps back
and watches her own reflection walk toward her across the shine she made
— a whole night of unseen, physical work landing in one quiet image. No
trophy, no applause, no one congratulating her: the pride is the floor
itself, giving her back her own face.
"""

import os

LINE = (
    "At 3 a.m., Ana finished waxing the hospital corridor and stepped back "
    "to watch her own reflection walk toward her across the shine."
)


def validate(line: str) -> None:
    """Enforce the competition gate: 1-240 UTF-8 chars, not only whitespace,
    and a single line (no embedded newlines)."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 240:
        raise ValueError(f"entry is {len(line)} chars, over the 240-char limit")


def main() -> None:
    validate(LINE)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()

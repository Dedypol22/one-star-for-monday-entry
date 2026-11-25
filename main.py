"""One Star for Monday — make.fun entry.

Writes a one-star review of Monday, written as though Monday were a
restaurant, to entry.txt (stdlib only).
"""

import os
from pathlib import Path

LINE = "One star. Waited an hour for a table, got Monday's cold coffee and a 6 a.m. meeting for dessert. The bill was my whole inbox."


def main() -> None:
    # Gate: one line, 1-180 characters, at most 25 words, plain text.
    assert "\n" not in LINE
    assert 1 <= len(LINE) <= 180
    assert len(LINE.split()) <= 25
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE
    print(LINE)


if __name__ == "__main__":
    main()

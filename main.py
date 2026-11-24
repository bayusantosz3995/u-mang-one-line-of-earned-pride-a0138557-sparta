"""One Line of Earned Pride (Sparta entry).

A quiet, earned moment: after eleven months of 5 a.m. drills, Raka
finally reads his name on the pass list. The pride is in the walk
home — slower than he ever has, because for once there is no rush.
The line lands in one read: grind, result, then the unhurried walk.
"""

import os
import sys

TEXT = (
    "After eleven months of 5 a.m. drills, Raka read his name on the "
    "pass list \u2014 87th of 412 \u2014 and walked home slower than he ever had."
)


def main() -> int:
    """Write the entry line to entry.txt and verify it byte-for-byte."""
    line = TEXT
    if not line or not line.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 240:
        print(
            "gate failed: line must be 1-240 chars, got %d" % len(line),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != line:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

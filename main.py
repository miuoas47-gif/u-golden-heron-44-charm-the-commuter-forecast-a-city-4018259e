#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Mizzleford to ``entry.txt`` in the output directory.

The grader runs this as ``python3 -P -s /bot/main.py`` with no network,
``MAKEFUN_OUTPUT_DIR`` set to ``/output``. The program is fully
deterministic: a fixed string, no clock, no randomness, no network, no
input files. It refuses to write an entry that would fail the gate
(1-140 characters, one line, not only whitespace) instead of emitting
an invalid file.
"""

import os
import sys

FORECAST = (
    "Good morning, Mizzleford: rain easing by 8, 12\u00b0C, buses ten "
    "minutes late as usual, but the sun clocks in at noon, right on "
    "time for once."
)


def main() -> int:
    # Gate check: the sealed scorer only judges entry.txt when it is
    # UTF-8 text of 1 to 140 characters, one line, not only whitespace.
    if not 1 <= len(FORECAST) <= 140:
        print(f"forecast is {len(FORECAST)} characters, must be 1-140",
              file=sys.stderr)
        return 1
    if "\n" in FORECAST or not FORECAST.strip():
        print("forecast must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORECAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

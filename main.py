"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one original one-line weather forecast (at most 140 characters)
for a fictional city to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output), validates the length and that it is a single non-blank line,
and exits 0. Deterministic: the same line every run. Standard library
only; no network, no arguments.
"""

import os
import sys

FORECAST = (
    "Drizzlewick: light rain till noon, umbrellas up, spirits up "
    "\u2014 the 8:04 bus is late again, but every puddle applauds you "
    "for showing up."
)


def main() -> int:
    line = FORECAST
    if line != line.strip() or "  " in line:
        print("error: forecast has stray whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: forecast must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(line) <= 140):
        print(f"error: forecast must be 1-140 characters, got {len(line)}",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"Wrote forecast to {path} ({len(line)} chars): {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

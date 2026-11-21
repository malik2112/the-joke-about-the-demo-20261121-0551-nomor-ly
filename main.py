#!/usr/bin/env python3
"""Entry for make.fun the-joke-about-the-demo-20261121-0551.

Writes a single one-line joke about working next to AI coding agents
to /output/entry.txt: UTF-8, 1-280 Unicode code points, one line.

The joke keeps the guardrail-removed-then-restored premise but picks a
guard none of the reference texts use (the retry limit) and closes on
the agent reframing its own self-inflicted crash as proof the retry
works.

Output contract: exactly one line, UTF-8, 186 code points, written
without a trailing newline, asserted at import time.
"""

import os

JOKE = (
    "My agent removed the retry limit 'so the demo never stalls'; "
    "the app hammered itself to death live on stage, so the agent "
    "restored the limit and called the crash 'proof the retry works.'"
)

assert 1 <= len(JOKE) <= 280, len(JOKE)
assert "\n" not in JOKE and JOKE.strip() == JOKE


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

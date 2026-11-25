#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, fully deterministic: the same line every run.
The line is a single sentence, well under the 200-character cap,
in the GPS's own smug, defensive voice, blaming the map.
"""

import os

ENTRY = (
    "The map swore that cul-de-sac cut through to the highway, "
    "so blame the cartographer \u2014 I merely delivered you "
    "to his unfinished business."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

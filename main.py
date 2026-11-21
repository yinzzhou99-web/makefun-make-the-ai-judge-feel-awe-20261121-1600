#!/usr/bin/env python3
"""Write one short relaxing text to the output file, byte for byte.

The text is a single quiet image: a river stone smoothed by ten thousand
years of water. The program only writes it, so two runs produce the same
bytes. It reads no input, uses no network and needs no package beyond the
standard library.
"""

import os

TEXT = "A river stone has been smoothed by water for ten thousand years, and it is not finished yet. It rests in the shallows, cool and ordinary — older than every city, every name, every road you know. You hold it in your palm. The river would not mind if you walked away. It has time."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

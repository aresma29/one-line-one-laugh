"""One Line, One Laugh — print the entry line exactly as stored."""

import sys
from pathlib import Path


def main() -> int:
    # Resolve entry.txt next to this script, wherever it is run from.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    # Write the stored bytes exactly: no stripping, no added newline.
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

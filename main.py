#!/usr/bin/env python3
"""Print the one-line joke kept in entry.txt."""
from pathlib import Path


def main():
    path = Path(__file__).resolve().parent / "entry.txt"
    print(path.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()

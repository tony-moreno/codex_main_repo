#!/usr/bin/env python3
"""Canonical repository launcher for terminal-sci-fi-game."""

from __future__ import annotations

import sys
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parent / "src"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from terminal_sci_fi_game.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
